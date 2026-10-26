"""Climate portfolio comparison on one common baseline; never writes canonical inputs or shared outputs.

Runs the carbon model (index/tools/carbon/) on the decided package and on cases that change one named lever or a named
combination (assumptions.json), with identical physical assumptions. Reports emissions against the 2035 NDC range and
net zero, modeled outlays (budget cost proxy), cost per extra ton, REV-C1 and dividend interactions, and retail
electricity bills. Needs node and build/carbon-config.json (run `bash index/tools/run-all.sh` first).

Usage: python3 index/tools/climate-portfolio/portfolio.py [--write]
  writes build/climate-portfolio/; --write also copies the report and JSON to sources/.
"""
import argparse, copy, hashlib, json, subprocess, tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
E2005, NET2005 = 5999, 6536
SOURCES = ['index/tools/climate-portfolio/portfolio.py', 'index/tools/climate-portfolio/assumptions.json',
           'index/tools/climate-portfolio/run.js', 'index/tools/carbon/cfd-model.js',
           'index/tools/carbon/cfd-households.js', 'index/tools/carbon/cfd-cex-2024.json', 'build/carbon-config.json']


def build_config(a, carbon_cfg):
    base = {c['id']: c for c in carbon_cfg['cases']}
    full, mov = base['full'], base['mov']
    cases = [dict(copy.deepcopy(mov), id='mov')]
    for spec in a['cases']:
        c = copy.deepcopy(full)
        c['id'] = spec['id']
        c['policy'].update(spec.get('policy', {}))
        world = dict(a[spec['world_ref']]) if 'world_ref' in spec else {}
        world.update(spec.get('world', {}))
        c['world'] = world
        if 'repeal_from' in spec:
            c['price'] = {y: (p if int(y) < spec['repeal_from'] else 0.0) for y, p in c['price'].items()}
        c['households'], c['householdsBase'] = 2035, 'mov'
        c.pop('mc', None)
        cases.append(c)
    return {'world': carbon_cfg['world'], 'cases': cases}


def run_model(conf):
    with tempfile.TemporaryDirectory() as tmp:
        f = Path(tmp) / 'config.json'
        f.write_text(json.dumps(conf))
        out = subprocess.run(['node', str(HERE / 'run.js'), str(f)], check=True, capture_output=True, text=True)
    return json.loads(out.stdout)


def analyse(a, runs):
    defl = lambda y: (1 + a['inflation']) ** (y - 2025)
    disc = lambda y: (1 + a['discount_rate_real']) ** -(y - 2030)
    kwh = a['residential_kwh_month']
    C = {k: {r['year']: r for r in v} for k, v in runs['cases'].items()}
    specs = {s['id']: s for s in a['cases']}
    c1 = lambda r: r['gross'] - r['rev']['methane']
    out = []
    def ext_of(spec):
        ext = spec.get('external_cost_bn_2025') or specs.get(spec.get('external_cost_from'), {}).get('external_cost_bn_2025')
        mid = ext['mid'] if ext else 0.0
        # external costs are spread evenly over 2031-39 (Weatherization starts in 2031)
        return ext, {y: (mid / 9 if 2031 <= y <= 2039 else 0.0) for y in range(2025, 2051)}

    for cid, spec in specs.items():
        yr = C[cid]
        ref_id = spec.get('compare_to', 'selected')
        sel = C[ref_id]
        ext, ext_y = ext_of(spec)
        _, ref_ext_y = ext_of(specs[ref_id])
        d_out = {y: yr[y]['credits'] + ext_y[y] - sel[y]['credits'] - ref_ext_y[y] for y in range(2030, 2051)}
        d_ton = {y: sel[y]['energy'] - yr[y]['energy'] for y in range(2030, 2051)}   # Mt, positive = more abatement
        d_ghg = {y: sel[y]['ghgNet'] - yr[y]['ghgNet'] for y in range(2030, 2051)}
        cost_50 = sum(d_out.values())
        tons_50 = sum(d_ton.values()) / 1000
        dcost = sum(d_out[y] * disc(y) for y in d_out)
        dtons = sum(d_ton[y] * disc(y) for y in d_ton) / 1000
        priced = not spec.get('unpriced', False)
        hh = runs['households'][cid]
        hh_sel = runs['households'][ref_id]
        out.append(dict(
            id=cid, group=spec['group'], label=spec['label'], compare_to=ref_id, priced=priced, cost_note=spec.get('cost_note'),
            external_cost=ext,
            energy_co2_below_2005={y: 1 - yr[y]['energy'] / E2005 for y in (2030, 2035, 2040, 2050)},
            net_ghg_below_2005={y: yr[y]['ghgBelow2005'] for y in (2035, 2040, 2050)},
            clean_share={y: yr[y]['cleanShare'] for y in (2035, 2040, 2050)},
            extra_avoided_energy_co2_gt={'2030_35': sum(d_ton[y] for y in range(2030, 2036)) / 1000,
                                         '2030_50': tons_50},
            extra_avoided_net_ghg_gt_2030_50=sum(d_ghg.values()) / 1000,
            extra_outlays_bn_2025={'2030_39': sum(d_out[y] for y in range(2030, 2040)), '2030_50': cost_50},
            extra_outlays_nominal_2030_39_tn=sum(d_out[y] * defl(y) for y in range(2030, 2040)) / 1000,
            model_outlays_nominal_2030_39_tn=sum((yr[y]['credits'] + ext_y[y]) * defl(y) for y in range(2030, 2040)) / 1000,
            power_side_outlays_nominal_2030_39_tn=sum(yr[y]['creditsPower'] * defl(y) for y in range(2030, 2040)) / 1000,
            cost_per_extra_ton_undiscounted=(cost_50 / tons_50) if priced and tons_50 > 0.01 and cost_50 > 0 else None,
            cost_per_extra_ton_discounted=(dcost / dtons) if priced and dtons > 0.01 and dcost > 0 else None,
            saving_per_ton_lost=(cost_50 / tons_50) if priced and tons_50 < -0.01 and cost_50 < 0 else None,
            rev_c1_nominal_2030_39_tn=sum(c1(yr[y]) * defl(y) for y in range(2030, 2040)) / 1000,
            rev_c1_change_nominal_2030_39_tn=sum((c1(yr[y]) - c1(sel[y])) * defl(y) for y in range(2030, 2040)) / 1000,
            dividend_per_adult_2035_nominal=0.8 * c1(yr[2035]) * defl(2035) * 1e9 / (yr[2035]['pop'] * 0.77 * 1e6),
            retail_cents_kwh_2025={y: yr[y]['retail'] for y in (2030, 2035, 2040, 2050)},
            residential_bill_change_month_2025={y: (yr[y]['retail'] - sel[y]['retail']) / 100 * kwh for y in (2030, 2035, 2040, 2050)},
            household_elec_cost_2035_vs_no_policy={q['name']: q['elec'] for q in hh},
            household_net_2035_change_vs_selected={q['name']: q['net'] - s['net'] for q, s in zip(hh, hh_sel)},
        ))
    return out


def fmt(x, d=0, pct=False, sign=False):
    if x is None:
        return 'n/a'
    if pct:
        return f"{100 * x:.{d}f}%"
    s = f"{x:+,.{d}f}" if sign else f"{x:,.{d}f}"
    return s


def report(a, res, hashes):
    r = {x['id']: x for x in res}
    for x in res:
        x['shown'] = x['label'] if x['compare_to'] == 'selected' else f"{x['label']} (changes against: {x['compare_to']})"
    lo, hi = a['benchmarks']['ndc_2035_net_ghg_below_2005']
    L = ['# Climate portfolio comparison: model results', '',
         '*Generated by `index/tools/climate-portfolio/portfolio.py`; do not edit by hand. Read with the recommendation in '
         '[climate-portfolio-allocation.md](climate-portfolio-allocation.md). Inputs: `index/tools/climate-portfolio/assumptions.json` '
         'and the carbon model case `full` written by `index/tools/carbon-model.py`.*', '',
         '**How to read this.** Every case starts from the decided package and changes the named levers, with identical physical '
         'assumptions. "Extra outlays" is the change in the model\'s spending accumulator (credits, grid and nuclear program costs) '
         'plus any external cost named in the assumptions, in constant 2025 dollars, undiscounted unless marked. It is a budget-cost '
         'proxy, not a CBO-style score, and it omits industrial-support costs. Tons are energy CO2 unless marked net GHG. A cost per '
         'ton is reported only where a case both costs more and cuts more; a negative row means the case saves money and loses tons. '
         'No modeled abatement is a pay-for, and no ratio here establishes a budget-neutral swap.', '',
         f'Benchmarks: the 2035 NDC range is {100*lo:.0f}-{100*hi:.0f}% below 2005 in net greenhouse gases; net zero by '
         f"{a['benchmarks']['net_zero_year']}. {a['benchmarks']['source']}", '',
         '## Emissions against the benchmarks', '',
         '| Case | Net GHG below 2005: 2035 / 2050 | Energy CO2 below 2005: 2035 / 2050 | Clean power 2035 | Extra energy CO2 avoided, Gt: 2030-35 / 2030-50 |',
         '| --- | --- | --- | --- | --- |']
    for x in res:
        L.append(f"| {x['shown']} | {fmt(x['net_ghg_below_2005'][2035], pct=True)} / {fmt(x['net_ghg_below_2005'][2050], pct=True)} | "
                 f"{fmt(x['energy_co2_below_2005'][2035], pct=True)} / {fmt(x['energy_co2_below_2005'][2050], pct=True)} | "
                 f"{fmt(x['clean_share'][2035], pct=True)} | {fmt(x['extra_avoided_energy_co2_gt']['2030_35'], 2, sign=True)} / "
                 f"{fmt(x['extra_avoided_energy_co2_gt']['2030_50'], 2, sign=True)} |")
    s = r['selected']
    gap35 = lo - s['net_ghg_below_2005'][2035]
    L += ['', f"The decided package reaches {fmt(s['net_ghg_below_2005'][2035], pct=True)} below 2005 in 2035 and "
          f"{fmt(s['net_ghg_below_2005'][2050], pct=True)} in 2050 in this model: {100*gap35:.0f} points short of the bottom of the NDC "
          f"range and {100*(1-s['net_ghg_below_2005'][2050]):.0f} points short of net zero. The model responds more slowly than "
          'the large published models in the first decade (see the carbon model report), so the shortfall is likely overstated, but no '
          'case below closes it.', '',
          '## Cost, cost per ton and fee interactions', '',
          '| Case | Extra outlays, $B 2025: 2030-39 / 2030-50 | Extra outlays 2030-39, $T nominal | Cost per extra ton, $ (undiscounted / 3% discounted) | REV-C1 change 2030-39, $T nominal | Dividend per adult 2035, $ nominal |',
          '| --- | --- | --- | --- | --- | --- |']
    for x in res:
        per = (f"{fmt(x['cost_per_extra_ton_undiscounted'])} / {fmt(x['cost_per_extra_ton_discounted'])}"
               if x['cost_per_extra_ton_undiscounted'] else
               (f"saves {fmt(x['saving_per_ton_lost'])} per ton lost" if x['saving_per_ton_lost'] else 'n/a'))
        L.append(f"| {x['shown']} | {fmt(x['extra_outlays_bn_2025']['2030_39'], sign=True)} / {fmt(x['extra_outlays_bn_2025']['2030_50'], sign=True)} | "
                 f"{fmt(x['extra_outlays_nominal_2030_39_tn'], 3, sign=True)} | {per} | {fmt(x['rev_c1_change_nominal_2030_39_tn'], 3, sign=True)} | "
                 f"{fmt(x['dividend_per_adult_2035_nominal'])} |")
    notes = [f"- {x['label']}: {x['cost_note']}." for x in res if x['cost_note']]
    notes += [f"- {x['label']}: external cost {x['external_cost']['mid']:.1f}B ({x['external_cost']['low']:.1f}-{x['external_cost']['high']:.1f}B), {x['external_cost']['basis']}."
              for x in res if x['external_cost']]
    L += ['', '**Cost notes.**'] + notes
    L += ['', f"The package's modeled outlays are {fmt(s['model_outlays_nominal_2030_39_tn'], 2)}T nominal in 2030-39 "
          f"(power side {fmt(s['power_side_outlays_nominal_2030_39_tn'], 2)}T), against the ledger's $0.90T for CLI-1A plus about $0.22T "
          "for CLI-5's transmission ITC and 45X lines. The model prices take-up off a larger clean build, so its absolute level is a high-end "
          "cross-check; the comparisons use its differences, which share that bias.", '',
          '## Household electricity bills', '',
          f"Change in the average residential bill against the decided package, $ a month in 2025 dollars at {a['residential_kwh_month']} kWh "
          f"({a['residential_kwh_source']}). Negative is cheaper. Federal program costs are not on bills here; the model's retail price "
          'tracks generation cost and does not add transmission capital recovery, so ratepayer-funded lines would add to these figures.', '',
          '| Case | 2030 | 2035 | 2040 | 2050 | Retail price 2035, cents/kWh (2025 $) |', '| --- | --- | --- | --- | --- | --- |']
    for x in res:
        b = x['residential_bill_change_month_2025']
        L.append(f"| {x['shown']} | {fmt(b[2030], 2, sign=True)} | {fmt(b[2035], 2, sign=True)} | {fmt(b[2040], 2, sign=True)} | "
                 f"{fmt(b[2050], 2, sign=True)} | {fmt(x['retail_cents_kwh_2025'][2035], 2)} |")
    L += ['', '**Carbon channel per household in 2035, change against the decided package** ($, 2025 dollars; dividend, fee costs and electricity together, '
          "from the model's household module):", '',
          '| Case | ' + ' | '.join(s['household_net_2035_change_vs_selected'].keys()) + ' |',
          '| --- |' + ' --- |' * len(s['household_net_2035_change_vs_selected'])]
    for x in res:
        L.append(f"| {x['shown']} | " + ' | '.join(fmt(v, 0, sign=True) for v in x['household_net_2035_change_vs_selected'].values()) + ' |')
    L += ['', '## Reproduction', '', '`bash index/tools/run-all.sh` (writes `build/carbon-config.json`), then '
          '`python3 index/tools/climate-portfolio/portfolio.py --write`. Tests: `python3 index/tools/climate-portfolio/test_portfolio.py`.', '',
          'Source hashes (SHA-256):', ''] + [f"- `{p}`: `{h}`" for p, h in hashes.items()]
    return '\n'.join(L) + '\n'


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--write', action='store_true')
    args = ap.parse_args()
    a = json.loads((HERE / 'assumptions.json').read_text())
    cfg_path = ROOT / 'build/carbon-config.json'
    if not cfg_path.exists():
        raise SystemExit('build/carbon-config.json missing: run `bash index/tools/run-all.sh` first')
    conf = build_config(a, json.loads(cfg_path.read_text()))
    runs = run_model(conf)
    res = analyse(a, runs)
    hashes = {p: hashlib.sha256((ROOT / p).read_bytes()).hexdigest() for p in SOURCES}
    data = dict(results=res, years={k: v for k, v in runs['cases'].items() if k != 'mov'}, source_sha256=hashes)
    md = report(a, res, hashes)
    out = ROOT / 'build/climate-portfolio'
    out.mkdir(parents=True, exist_ok=True)
    (out / 'climate-portfolio-model-results.json').write_text(json.dumps(data, indent=1, sort_keys=True) + '\n')
    (out / 'climate-portfolio-model-results.md').write_text(md)
    if args.write:
        for name in ('climate-portfolio-model-results.json', 'climate-portfolio-model-results.md'):
            (ROOT / 'sources' / name).write_text((out / name).read_text())
    print(f"{len(res)} cases; selected net GHG below 2005 in 2035: {res[0]['net_ghg_below_2005'][2035]:.3f}")


if __name__ == '__main__':
    main()
