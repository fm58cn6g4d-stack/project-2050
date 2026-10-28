"""International climate finance for the 2035 benchmark: what verified mitigation abroad could add and cost, beside
loss-and-damage and adaptation money. Reads international.json and the committed package results. Never writes
canonical inputs or shared outputs.

Usage: python3 models/tools/climate-portfolio/international.py [--write]
"""
import argparse, hashlib, json
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
W10 = range(2030, 2040)
SOURCES = ['models/tools/climate-portfolio/international.py', 'models/tools/climate-portfolio/international.json',
           'legacy/sources/climate-portfolio-packages.json']


def tri(f):
    return [f(i) for i in range(3)]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--write', action='store_true')
    args = ap.parse_args()
    a = json.loads((HERE / 'international.json').read_text())
    pk = json.loads((ROOT / 'legacy/sources/climate-portfolio-packages.json').read_text())
    rec = next(r for r in pk['robustness'] if r['name'] == 'recommended')['central']
    om = pk['off_model']['items']
    cli13 = tri(lambda i: sum(it['mt_2035'][i] for it in om))
    base = a['net_ghg_2005_mt']
    dom_pts = tri(lambda i: rec['net_ghg_below_2005_2035'] + cli13[i] / base)
    gap = {f'{int(100 * t)}%': tri(lambda i: max(0.0, (t - dom_pts[2 - i]) * base)) for t in a['benchmark_2035']}   # low gap uses the high domestic case
    srcs = a['sources']
    vol = tri(lambda i: sum(s['mt_2035'][i] for s in srcs))
    cost35 = tri(lambda i: sum(s['mt_2035'][i] * s['price'][i] for s in srcs) / 1000 * (1 + a['buffer_share'][i]))   # $B in 2035
    avg_price = tri(lambda i: cost35[i] * 1000 / vol[i])
    ramp = {int(k): v for k, v in a['ramp'].items()}
    share = {y: ramp.get(y, 1.0) for y in W10}
    defl = lambda y: (1 + a['inflation']) ** (y - 2025)
    ten = tri(lambda i: sum(cost35[i] * share[y] for y in W10))
    ten_nom = tri(lambda i: sum(cost35[i] * share[y] * defl(y) for y in W10) / 1000)
    tons10 = tri(lambda i: sum(vol[i] * share[y] for y in W10) / 1000)
    pts = tri(lambda i: vol[i] / base)
    floor = a['domestic_floor']
    dg = pk['diagnostics']; fm = a['floor_measures']
    if fm.get('included'):                                                   # floor measures already inside Package A (Oct 26)
        fm_pts = fm_cost = fm_bill = 0.0
    else:
        fm_pts = dg[fm['diagnostic_to']]['net_ghg_below_2005_2035'] - dg[fm['diagnostic_from']]['net_ghg_below_2005_2035']
        fm_cost = dg[fm['diagnostic_to']]['outlays_bn_2025_2030_39'] - dg[fm['diagnostic_from']]['outlays_bn_2025_2030_39']
        fm_bill = dg[fm['diagnostic_to']]['bill_change_month_2040'] - dg[fm['diagnostic_from']]['bill_change_month_2040']
    dom_fm = tri(lambda i: dom_pts[i] + fm_pts)
    counted = lambda dom, i: pts[i] if dom[i] >= floor else 0.0          # threshold rule
    total_no_fm = tri(lambda i: dom_pts[i] + counted(dom_pts, i))
    total_fm = tri(lambda i: dom_fm[i] + counted(dom_fm, i))
    ldad_run = tri(lambda i: (a['loss_and_damage']['annual_bn'][i] + a['adaptation']['annual_bn'][i]))
    ld = a['loss_and_damage']['annual_bn']; ad = a['adaptation']['annual_bn']
    ld10 = tri(lambda i: ld[i] * 10); ad10 = tri(lambda i: ad[i] * 10)
    per_source = [dict(id=s['id'], label=s['label'], mt_2035=s['mt_2035'], price=s['price'],
                       cost_2035_bn=tri(lambda i: s['mt_2035'][i] * s['price'][i] / 1000 * (1 + a['buffer_share'][i])), basis=s['basis']) for s in srcs]
    data = dict(package_a_2035=rec['net_ghg_below_2005_2035'], cli13_mt_2035=cli13, domestic_2035=dom_pts, gap_mt_2035=gap,
                volume_mt_2035=vol, points_2035=pts, total_2035=tri(lambda i: dom_pts[1] + pts[i]),
                domestic_floor=floor, floor_measures=dict(label=fm['label'], points_2035=fm_pts, outlays_bn_2025_2030_39=fm_cost, bill_2040_month=fm_bill),
                domestic_with_floor_measures_2035=dom_fm, floor_met_without_measures=[d >= floor for d in dom_pts], floor_met_with_measures=[d >= floor for d in dom_fm],
                counted_total_without_measures_2035=total_no_fm, counted_total_with_measures_2035=total_fm,
                ld_adaptation_run_rate_bn_2025=ldad_run, ld_adaptation_fy2040_nominal_bn=[x * (1 + a['inflation']) ** 15 for x in ldad_run],
                ld_adaptation_fy2050_nominal_bn=[x * (1 + a['inflation']) ** 25 for x in ldad_run],
                cost_2035_bn=cost35, avg_price=avg_price, cost_2030_39_bn=ten, cost_2030_39_nominal_tn=ten_nom, tons_2030_39_gt=tons10,
                loss_and_damage_2030_39_bn=ld10, adaptation_2030_39_bn=ad10, sources=per_source,
                source_sha256={p: hashlib.sha256((ROOT / p).read_bytes()).hexdigest() for p in SOURCES})
    md = report(a, data)
    out = ROOT / 'build/climate-portfolio'
    out.mkdir(parents=True, exist_ok=True)
    files = {'climate-portfolio-international-pricing.md': md,
             'climate-portfolio-international-pricing.json': json.dumps(data, indent=1, sort_keys=True) + '\n'}
    for n, t in files.items():
        (out / n).write_text(t)
        if args.write:
            (ROOT / 'legacy/sources' / n).write_text(t)
    print(f"mid: {vol[1]} Mt in 2035 at ${avg_price[1]:.0f}/t, ${cost35[1]:.1f}B in 2035; total {100*(dom_pts[1]+pts[1]):.1f}%")


def r3(x, d=0):
    return ' / '.join(f"{v:,.{d}f}" for v in x)


def report(a, d):
    L = ['# International climate finance: pricing', '',
         '*Generated by `models/tools/climate-portfolio/international.py` from `international.json`; do not edit by hand. Read with '
         '[climate-portfolio-international.md](climate-portfolio-international.md). 2025 dollars; low / mid / high.*', '',
         '## The 2035 gap after domestic action', '',
         f"- Package A (as approved) in the carbon model: {100*d['package_a_2035']:.1f}% below 2005 in net greenhouse gases in 2035.",
         f"- Plus CLI-13 farms, forests and removal (outside the model): {r3(d['cli13_mt_2035'])} Mt, giving {r3([100*x for x in d['domestic_2035']], 1)}% domestically.",
         f"- Gap to 61%: {r3(d['gap_mt_2035']['61%'])} Mt a year in 2035; gap to 66%: {r3(d['gap_mt_2035']['66%'])} Mt.", '',
         '## What verified mitigation abroad could supply in 2035', '',
         '| Source | Mt CO2e a year, 2035 | Price, $/t | Cost in 2035, $B (with integrity reserve) | Basis |', '| --- | --- | --- | --- | --- |']
    for s in d['sources']:
        L.append(f"| {s['label']} | {r3(s['mt_2035'])} | {r3(s['price'])} | {r3(s['cost_2035_bn'], 1)} | {s['basis']} |")
    L += ['', f"**Together:** {r3(d['volume_mt_2035'])} Mt in 2035 ({r3([100*x for x in d['points_2035']], 1)} points of the 2005 baseline), "
          f"at an average {r3(d['avg_price'])} $/t including the integrity reserve ({r3([100*x for x in a['buffer_share']])}%). "
          f"Cost in 2035: {r3(d['cost_2035_bn'], 1)} $B.", '',
          '## The 50% domestic floor', '',
          f"Rule: {a['floor_rule']}", '',
          f"- Domestic 2035 (Package A plus CLI-13): {r3([100*x for x in d['domestic_2035']], 1)}%. Floor met: {' / '.join('yes' if f else 'no' for f in d['floor_met_without_measures'])}. "
          f"Counted total: {r3([100*x for x in d['counted_total_without_measures_2035']], 1)}%.",
          f"- With the floor measures ({d['floor_measures']['label']}: +{100*d['floor_measures']['points_2035']:.2f} points in 2035, {d['floor_measures']['outlays_bn_2025_2030_39']:+.0f} $B outlays over 2030-39 in 2025 dollars, "
          f"{d['floor_measures']['bill_2040_month']:+.2f} $/month on the 2040 bill): domestic {r3([100*x for x in d['domestic_with_floor_measures_2035']], 1)}%; floor met: "
          f"{' / '.join('yes' if f else 'no' for f in d['floor_met_with_measures'])}; counted total {r3([100*x for x in d['counted_total_with_measures_2035']], 1)}%.",
          f"- {a['taper_note']}", '',
          f"**2030-39**, ramping from 10% of the 2035 volume in 2030: {r3(d['tons_2030_39_gt'], 1)} Gt bought for {r3(d['cost_2030_39_bn'])} $B (2025 dollars), "
          f"{r3(d['cost_2030_39_nominal_tn'], 3)} $T nominal.", '',
          f"**Beside it, counted as climate finance but never toward emissions:** loss and damage {r3(d['loss_and_damage_2030_39_bn'])} $B and adaptation above DEV-P {r3(d['adaptation_2030_39_bn'])} $B over 2030-39. "
          f"As standing commitments they are permanent under D4: about {r3(d['ld_adaptation_fy2040_nominal_bn'], 1)} $B in FY2040 and {r3(d['ld_adaptation_fy2050_nominal_bn'], 1)} $B in FY2050 (nominal), to add to the maturity test beside the climate package's run rate.", '',
          f"Context: {a['climate_finance_context']}. {a['domestic_marginal_reference']}.", '',
          '## Reproduction', '', '`python3 models/tools/climate-portfolio/international.py --write` (reads the committed package results).', '',
          'Source hashes (SHA-256):', ''] + [f"- `{p}`: `{h}`" for p, h in d['source_sha256'].items()]
    return '\n'.join(L) + '\n'


if __name__ == '__main__':
    main()
