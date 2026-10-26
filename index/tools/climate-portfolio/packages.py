"""Climate package search: every combination of the levers in packages.json, on the carbon model's decided package.

Finds the packages that avoid the most net greenhouse gases for each budget cap (with and without a bill cap), the
cost/emissions frontier, how each lever's value changes inside the best packages (layering), and how the leading
packages hold up under weak grid delivery and a 2037 repeal. Never writes canonical inputs or shared outputs.
Needs node and build/carbon-config.json (run `bash index/tools/run-all.sh` first).

Usage: python3 index/tools/climate-portfolio/packages.py [--write]
"""
import argparse, copy, hashlib, itertools, json
from pathlib import Path
import portfolio as P

HERE, ROOT = P.HERE, P.ROOT
INFL = 0.022
defl = lambda y: (1 + INFL) ** (y - 2025)
W10, W21 = range(2030, 2040), range(2030, 2051)
SOURCES = P.SOURCES + ['index/tools/climate-portfolio/packages.py', 'index/tools/climate-portfolio/packages.json']


def higher_path(full_price, spec):
    """REV-C1H in 2025 dollars: D7 through 2032, then linear (nominal) to the 2037 price, then growth."""
    p32 = full_price['2032'] * defl(2032)
    out = {}
    for y, real in full_price.items():
        y = int(y)
        if y <= 2032:
            out[str(y)] = real
        elif y <= 2037:
            out[str(y)] = (p32 + (spec['price_2037_nominal'] - p32) * (y - 2032) / 5) / defl(y)
        else:
            out[str(y)] = spec['price_2037_nominal'] * (1 + spec['growth_after']) ** (y - 2037) / defl(y)
    return out


def make_case(cid, choice, levers, a, full, extra_world=None, repeal_from=None, price_spec=None):
    c = copy.deepcopy(full)
    c['id'] = cid
    c['world'] = {}
    ext = 0.0
    for lev, key in zip(levers, choice):
        opt = next(o for o in lev['options'] if o['key'] == key)
        for k, v in opt.get('policy', {}).items():
            c['policy'][k] = copy.deepcopy(v)
        if 'policy_cover' in opt:
            c['policy']['cover'] = dict(c['policy']['cover'], **opt['policy_cover'])
        if opt.get('methane_x3'):
            mf = full['policy']['methaneFee']
            c['policy']['methaneFee'] = {'start': mf['start'], 'mult': 3, 'floor': 0, 'ogShare': mf['ogShare'], 'coal': True, 'landfill': False}
        c['world'].update(opt.get('world', {}))
        if opt.get('price') == 'old100':
            c['price'] = higher_path(full['price'], a['old100_price'])
        ext += opt.get('external_cost_bn_2025', 0.0)
    if price_spec:
        c['price'] = higher_path(full['price'], price_spec)
    c['world'].update(extra_world or {})
    if repeal_from:
        c['price'] = {y: (p if int(y) < repeal_from else 0.0) for y, p in c['price'].items()}
    for k in ('mc', 'households', 'householdsBase'):
        c.pop(k, None)
    return c, ext


def run_cases(cases, world, households=False):
    out = {}
    for i in range(0, len(cases), 400):
        batch = cases[i:i + 400]
        if households:
            for c in batch:
                if c['id'] != 'mov':
                    c['households'], c['householdsBase'] = 2035, 'mov'
        r = P.run_model({'world': world, 'cases': batch})
        for k, v in r['cases'].items():
            out[k] = {'rows': {row['year']: row for row in v}, 'households': r['households'].get(k)}
    return out


def metrics(rows, ext, base, base_ext, kwh):
    ext_y = lambda e: {y: (e / 9 if 2031 <= y <= 2039 else 0.0) for y in W21}
    e, be = ext_y(ext), ext_y(base_ext)
    out_y = {y: rows[y]['credits'] + rows[y]['credInd'] + e[y] - base[y]['credits'] - base[y]['credInd'] - be[y] for y in W21}
    c1 = lambda r: r['gross'] - r['rev']['methane']
    return dict(
        net_ghg_below_2005_2035=rows[2035]['ghgBelow2005'], net_ghg_below_2005_2040=rows[2040]['ghgBelow2005'],
        net_ghg_below_2005_2050=rows[2050]['ghgBelow2005'],
        energy_co2_below_2005_2035=1 - rows[2035]['energy'] / P.E2005, clean_share_2035=rows[2035]['cleanShare'],
        extra_avoided_net_ghg_gt_2030_50=sum(base[y]['ghgNet'] - rows[y]['ghgNet'] for y in W21) / 1000,
        extra_avoided_net_ghg_gt_2030_35=sum(base[y]['ghgNet'] - rows[y]['ghgNet'] for y in range(2030, 2036)) / 1000,
        outlays_bn_2025_2030_39=sum(out_y[y] for y in W10), outlays_bn_2025_2030_50=sum(out_y.values()),
        outlays_nominal_tn_2030_39=sum(out_y[y] * defl(y) for y in W10) / 1000,
        rev_c1_change_nominal_tn_2030_39=sum((c1(rows[y]) - c1(base[y])) * defl(y) for y in W10) / 1000,
        rev_c3_change_nominal_tn_2030_39=sum((rows[y]['rev']['methane'] - base[y]['rev']['methane']) * defl(y) for y in W10) / 1000,
        ces_payments_change_nominal_tn_2030_39=sum((rows[y]['cesAcp'] - base[y]['cesAcp']) * defl(y) for y in W10) / 1000,
        bill_change_month_2035=(rows[2035]['retail'] - base[2035]['retail']) / 100 * kwh,
        bill_change_month_2040=(rows[2040]['retail'] - base[2040]['retail']) / 100 * kwh,
    )


def frontier(res):
    """Packages not beaten on both lower outlays and more cumulative abatement."""
    pts = sorted(res, key=lambda r: (r['outlays_bn_2025_2030_39'], -r['extra_avoided_net_ghg_gt_2030_50']))
    front, best = [], -1e9
    for r in pts:
        if r['extra_avoided_net_ghg_gt_2030_50'] > best + 1e-6:
            front.append(r)
            best = r['extra_avoided_net_ghg_gt_2030_50']
    return front


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--write', action='store_true')
    args = ap.parse_args()
    a = json.loads((HERE / 'packages.json').read_text())
    pa = json.loads((HERE / 'assumptions.json').read_text())
    kwh = pa['residential_kwh_month']
    cfg = json.loads((ROOT / 'build/carbon-config.json').read_text())
    full = next(c for c in cfg['cases'] if c['id'] == 'full')
    levers = a['levers']
    combos = list(itertools.product(*[[o['key'] for o in lev['options']] for lev in levers]))
    base_choice = tuple(lev['options'][0]['key'] for lev in levers)
    cases, exts = [], {}
    for i, ch in enumerate(combos):
        c, e = make_case(f'p{i}', ch, levers, a, full)
        cases.append(c)
        exts[c['id']] = e
    runs = run_cases(cases, cfg['world'])
    base_id = f'p{combos.index(base_choice)}'
    base = runs[base_id]['rows']
    res = []
    for i, ch in enumerate(combos):
        cid = f'p{i}'
        m = metrics(runs[cid]['rows'], exts[cid], base, 0.0, kwh)
        res.append(dict(id=cid, choice=dict(zip([l['id'] for l in levers], ch)), **m))

    # best package for each budget cap, with and without the bill cap
    best = []
    for cap in a['budget_caps_bn_2025']:
        for billcap in (None, a['bill_cap_2040_month']):
            ok = [r for r in res if r['outlays_bn_2025_2030_39'] <= cap and (billcap is None or r['bill_change_month_2040'] <= billcap)]
            if ok:
                r = max(ok, key=lambda r: r['extra_avoided_net_ghg_gt_2030_50'])
                best.append(dict(cap_bn_2025=cap, bill_cap=billcap, **r))
    front = frontier(res)

    # recommended package and layering: drop or add each lever one at a time inside it
    rec_choice = tuple(a['recommended'][l['id']] for l in levers) if 'recommended' in a else None
    layering, robustness, households = [], [], {}
    lookup = {tuple(r['choice'].values()): r for r in res}
    if rec_choice:
        rec = lookup[rec_choice]
        for j, lev in enumerate(levers):
            alt = list(rec_choice)
            alt[j] = base_choice[j]
            if alt[j] == rec_choice[j]:
                continue
            r = lookup[tuple(alt)]
            alone = list(base_choice); alone[j] = rec_choice[j]
            ra = lookup[tuple(alone)]
            layering.append(dict(lever=lev['label'], option=rec_choice[j],
                                 alone_gt=ra['extra_avoided_net_ghg_gt_2030_50'], alone_bn=ra['outlays_bn_2025_2030_39'],
                                 in_package_gt=rec['extra_avoided_net_ghg_gt_2030_50'] - r['extra_avoided_net_ghg_gt_2030_50'],
                                 in_package_bn=rec['outlays_bn_2025_2030_39'] - r['outlays_bn_2025_2030_39']))
        # robustness and households for the decided package, the recommended package and the budget-cap winners
        named = {'decided': base_choice, 'recommended': rec_choice}
        for b in best:
            named.setdefault(f"best_{b['cap_bn_2025']}_{'bill' if b['bill_cap'] else 'nobill'}", tuple(b['choice'].values()))
        stress_cases, ext2 = [dict(copy.deepcopy(next(c for c in cfg['cases'] if c['id'] == 'mov')), id='mov')], {}
        for name, ch in named.items():
            for tag, kw in (('central', {}), ('weak', {'extra_world': pa['weak_grid_world']}),
                            ('repeal2037', {'extra_world': {'crYears': 7, 'crVehYears': 5 if dict(zip([l['id'] for l in levers], ch))['credits'] != 'keep' else 7}, 'repeal_from': 2037})):
                c, e = make_case(f'{name}|{tag}', ch, levers, a, full, **kw)
                stress_cases.append(c)
                ext2[c['id']] = e
        sr = run_cases(stress_cases, cfg['world'], households=True)
        for name, ch in named.items():
            row = dict(name=name, choice=dict(zip([l['id'] for l in levers], ch)))
            for tag in ('central', 'weak', 'repeal2037'):
                cid = f'{name}|{tag}'
                row[tag] = metrics(sr[cid]['rows'], ext2[cid], base, 0.0, kwh)
            hc, hb = sr[f'{name}|central']['households'], sr['decided|central']['households']
            row['household_net_2035_change'] = {q['name']: q['net'] - s['net'] for q, s in zip(hc, hb)}
            robustness.append(row)

    diagnostics = []
    if rec_choice and a.get('diagnostics'):
        dcases, dext = [], {}
        for j, dg in enumerate(a['diagnostics']):
            ch = dict(zip([l['id'] for l in levers], rec_choice)); ch.update(dg.get('choice', {}))
            c, e = make_case(f'diag{j}', tuple(ch[l['id']] for l in levers), levers, a, full, extra_world=dg.get('world'), price_spec=dg.get('price'))
            dcases.append(c); dext[c['id']] = e + dg.get('external_cost_bn_2025', 0.0)
        dr = run_cases(dcases, cfg['world'])
        for j, dg in enumerate(a['diagnostics']):
            diagnostics.append(dict(label=dg['label'], **metrics(dr[f'diag{j}']['rows'], dext[f'diag{j}'], base, 0.0, kwh)))
    hashes = {p: hashlib.sha256((ROOT / p).read_bytes()).hexdigest() for p in SOURCES}
    data = dict(levers=levers, n_packages=len(res), diagnostics=diagnostics, best=best, frontier=front, layering=layering, robustness=robustness,
                off_model=a['off_model'], results=res, source_sha256=hashes)
    md = report(a, data)
    out = ROOT / 'build/climate-portfolio'
    out.mkdir(parents=True, exist_ok=True)
    (out / 'climate-portfolio-packages.json').write_text(json.dumps(data, indent=1, sort_keys=True) + '\n')
    (out / 'climate-portfolio-packages.md').write_text(md)
    if args.write:
        # The committed copy omits the per-package rows (about 15 MB); rerun the tool for them in build/
        slim = dict(data, results=None, results_note=f'{len(res)} package rows omitted from the committed copy; build/climate-portfolio/ holds them')
        (ROOT / 'sources/climate-portfolio-packages.json').write_text(json.dumps(slim, indent=1, sort_keys=True) + '\n')
        (ROOT / 'sources/climate-portfolio-packages.md').write_text(md)
    print(f"{len(res)} packages; frontier {len(front)}")


def fmt(x, d=0, pct=False, sign=False):
    return P.fmt(x, d, pct, sign)


def choice_text(levers, ch, short=False):
    parts = []
    for lev in levers:
        k = ch[lev['id']]
        if k != lev['options'][0]['key']:
            parts.append(f"{lev['id']}={k}")
    return ', '.join(parts) or 'decided package'


def report(a, d):
    lv = d['levers']
    L = ['# Climate package search: results', '',
         '*Generated by `index/tools/climate-portfolio/packages.py`; do not edit by hand. Read with '
         '[climate-portfolio-allocation.md](climate-portfolio-allocation.md). Lever definitions: `index/tools/climate-portfolio/packages.json`.*', '',
         f"**What this is.** Every combination of {len(lv)} levers ({d['n_packages']:,} packages) run on the carbon model's decided package with identical physical "
         'assumptions. "Outlays" are changes in general-fund climate outlays against the decided package (credits, grid and nuclear programs, '
         "the model's industrial-support estimate and named external costs), constant 2025 dollars, 2030-39. Fee, methane and CES receipts are channel "
         'money and are shown separately, not netted. Tons are net greenhouse gases avoided against the decided package, 2030-50. Bills are the '
         'average residential bill. Packages are not scores, and the model is one structural model, conservative in its first decade.', '',
         '## Levers', '']
    for lev in lv:
        L.append(f"- **{lev['label']}** (`{lev['id']}`): " + '; '.join(f"`{o['key']}` {o['label']}" for o in lev['options']))
    L += ['', '## Best package for each budget cap', '',
          f"Highest cumulative abatement among packages whose 2030-39 outlays change is at or below the cap; the second row of each pair also holds the 2040 bill increase to ${a['bill_cap_2040_month']:.0f} a month or less.", '',
          '| Outlays cap ($B 2025) | Bill cap | Package (changes from decided) | Net GHG below 2005: 2035 / 2040 / 2050 | Extra net GHG avoided 2030-50 (Gt) | Outlays ($B 2025, 2030-39) | REV-C1 change ($T nominal) | Bill 2040 ($/month) |',
          '| --- | --- | --- | --- | --- | --- | --- | --- |']
    for b in d['best']:
        L.append(f"| {b['cap_bn_2025']:+,} | {'yes' if b['bill_cap'] else 'no'} | {choice_text(lv, b['choice'])} | {fmt(b['net_ghg_below_2005_2035'], pct=True)} / "
                 f"{fmt(b['net_ghg_below_2005_2040'], pct=True)} / {fmt(b['net_ghg_below_2005_2050'], pct=True)} | {fmt(b['extra_avoided_net_ghg_gt_2030_50'], 2, sign=True)} | "
                 f"{fmt(b['outlays_bn_2025_2030_39'], sign=True)} | {fmt(b['rev_c1_change_nominal_tn_2030_39'], 2, sign=True)} | {fmt(b['bill_change_month_2040'], 2, sign=True)} |")
    L += ['', '## Cost and abatement frontier', '', 'Packages that no other package beats on both lower outlays and more abatement (2030-39 outlays; 2030-50 tons).', '',
          '| Outlays ($B 2025) | Extra net GHG avoided 2030-50 (Gt) | Net GHG below 2005, 2035 / 2050 | Bill 2040 | Package |', '| --- | --- | --- | --- | --- |']
    for r in d['frontier']:
        L.append(f"| {fmt(r['outlays_bn_2025_2030_39'], sign=True)} | {fmt(r['extra_avoided_net_ghg_gt_2030_50'], 2, sign=True)} | {fmt(r['net_ghg_below_2005_2035'], pct=True)} / "
                 f"{fmt(r['net_ghg_below_2005_2050'], pct=True)} | {fmt(r['bill_change_month_2040'], 2, sign=True)} | {choice_text(lv, r['choice'])} |")
    if d['layering']:
        L += ['', '## Layering inside the recommended package', '',
              'Each lever alone (added to the decided package) against its marginal contribution inside the recommended package (the package with and without it). '
              'Differences are interactions: levers that do the same job crowd each other out; complements add more together.', '',
              '| Lever (option) | Alone: Gt / $B | Inside the package: Gt / $B |', '| --- | --- | --- |']
        for x in d['layering']:
            L.append(f"| {x['lever']} (`{x['option']}`) | {fmt(x['alone_gt'], 2, sign=True)} / {fmt(x['alone_bn'], sign=True)} | {fmt(x['in_package_gt'], 2, sign=True)} / {fmt(x['in_package_bn'], sign=True)} |")
    if d['robustness']:
        L += ['', '## Robustness: weak grid delivery and a 2037 repeal', '',
              'Net GHG below 2005 in 2035 / 2050, central case; then with weak grid delivery; then with the fee repealed and consumer credits closed in 2037.', '',
              '| Package | Changes | Central | Weak delivery | 2037 repeal | Outlays central ($B 2025) |', '| --- | --- | --- | --- | --- | --- |']
        for r in d['robustness']:
            f = lambda m: f"{fmt(m['net_ghg_below_2005_2035'], pct=True)} / {fmt(m['net_ghg_below_2005_2050'], pct=True)}"
            L.append(f"| {r['name']} | {choice_text(lv, r['choice'])} | {f(r['central'])} | {f(r['weak'])} | {f(r['repeal2037'])} | {fmt(r['central']['outlays_bn_2025_2030_39'], sign=True)} |")
        qs = list(d['robustness'][0]['household_net_2035_change'].keys())
        L += ['', '**Carbon channel per household in 2035, change against the decided package** ($, 2025 dollars):', '',
              '| Package | ' + ' | '.join(qs) + ' |', '| --- |' + ' --- |' * len(qs)]
        for r in d['robustness']:
            L.append(f"| {r['name']} | " + ' | '.join(fmt(r['household_net_2035_change'][q], sign=True) for q in qs) + ' |')
    if d.get('diagnostics'):
        L += ['', '## How far the model can go: cumulative ambition diagnostics', '',
              'Each row adds to the one above, starting from the recommended package. These test the ceiling of the instruments the model can represent; they are not recommendations.', '',
              '| Step | Net GHG below 2005: 2035 / 2040 / 2050 | Extra net GHG avoided 2030-50 (Gt) | Outlays ($B 2025, 2030-39) | REV-C1 change ($T nominal) | Bill 2040 ($/month) |', '| --- | --- | --- | --- | --- | --- |']
        for x in d['diagnostics']:
            L.append(f"| {x['label']} | {fmt(x['net_ghg_below_2005_2035'], pct=True)} / {fmt(x['net_ghg_below_2005_2040'], pct=True)} / {fmt(x['net_ghg_below_2005_2050'], pct=True)} | "
                     f"{fmt(x['extra_avoided_net_ghg_gt_2030_50'], 2, sign=True)} | {fmt(x['outlays_bn_2025_2030_39'], sign=True)} | {fmt(x['rev_c1_change_nominal_tn_2030_39'], 2, sign=True)} | {fmt(x['bill_change_month_2040'], 2, sign=True)} |")
    om = d['off_model']
    L += ['', '## Outside the model: farms, forests and removal (CLI-13)', '', om['note'], '',
          '| Item | Mt CO2e a year, 2035 (low / mid / high) | 2050 | Cost 2030-39, $B 2025 | Basis |', '| --- | --- | --- | --- | --- |']
    for it in om['items']:
        L.append(f"| {it['label']} | {' / '.join(map(str, it['mt_2035']))} | {' / '.join(map(str, it['mt_2050']))} | {' / '.join(map(str, it['cost_bn_2030_39']))} | {it['basis']} |")
    tot35 = [sum(it['mt_2035'][i] for it in om['items']) for i in range(3)]
    tot50 = [sum(it['mt_2050'][i] for it in om['items']) for i in range(3)]
    L += ['', f"Together: {tot35[0]}-{tot35[2]} Mt in 2035 (mid {tot35[1]}), about {100*tot35[1]/P.NET2005:.1f} points of the 2005 baseline; "
          f"{tot50[0]}-{tot50[2]} Mt in 2050 (mid {tot50[1]}), about {100*tot50[1]/P.NET2005:.1f} points.", '',
          '## Reproduction', '', '`bash index/tools/run-all.sh`, then `python3 index/tools/climate-portfolio/packages.py --write`.', '',
          'Source hashes (SHA-256):', ''] + [f"- `{p}`: `{h}`" for p, h in d['source_sha256'].items()]
    return '\n'.join(L) + '\n'


if __name__ == '__main__':
    main()
