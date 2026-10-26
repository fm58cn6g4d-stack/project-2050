"""Climate portfolio pricing: grid financing windows, credit redesign in ledger terms, bill protection, and the
disaster preparedness and response package. Reads pricing.json and runs the carbon model for the named packages.
Never writes canonical inputs or shared outputs. Needs build/carbon-config.json (run `bash index/tools/run-all.sh`).

Usage: python3 index/tools/climate-portfolio/pricing.py [--write]
"""
import argparse, csv, hashlib, io, json
from pathlib import Path
import portfolio as P
import packages as K

HERE, ROOT = P.HERE, P.ROOT
SOURCES = K.SOURCES + ['index/tools/climate-portfolio/pricing.py', 'index/tools/climate-portfolio/pricing.json']
W10 = range(2030, 2040)


def tri(f):
    return [f(i) for i in range(3)]


def grid_finance(g):
    r, n = g['annuity']['rate'], g['annuity']['years']
    ann = r / (1 - (1 + r) ** -n)
    win = {w['id']: w for w in g['windows']}
    out = []
    for v in g['variants']:
        cost = tri(lambda i: v['grants'] * win['grants']['cost_share'][i] + v['loans'] * win['loans']['cost_share'][i]
                   + v['contracts'] * win['contracts']['cost_share'][i])
        build = v['grants'] + v['loans'] + v['contracts'] * win['contracts']['leverage']
        financing = v['grants'] + v['loans'] + v['contracts'] * win['contracts']['cost_share'][1]
        rev_req = v['loans'] * ann                                      # $B a year once lent
        cents = rev_req / g['retail_twh'] * 100                         # $B / TWh = $/kWh * 1e0 -> cents
        bill = cents / 100 * g['kwh_month']
        savings = [build * s for s in g['system_savings_per_dollar']]
        out.append(dict(id=v['id'], label=v['label'], grants=v['grants'], loans=v['loans'], contracts=v['contracts'],
                        deficit_cost_bn=cost, physical_build_bn=build, gross_financing_bn=financing,
                        loan_revenue_requirement_bn_yr=rev_req, bill_month_from_loans=bill, system_savings_bn_to_2050=savings))
    return out


def credit_pieces(rows, grid_on, years=W10, infl=0.022):
    """Credit outlays (credits less any grid-program cost) plus the industrial-support estimate, $T nominal."""
    gp = 12.0 if grid_on else 0.0
    return sum((rows[y]['credits'] - (gp if 2030 <= y <= 2039 else 0) + rows[y]['credInd']) * (1 + infl) ** (y - 2025) for y in years) / 1000


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--write', action='store_true')
    args = ap.parse_args()
    pr = json.loads((HERE / 'pricing.json').read_text())
    pk = json.loads((HERE / 'packages.json').read_text())
    pa = json.loads((HERE / 'assumptions.json').read_text())
    cfg = json.loads((ROOT / 'build/carbon-config.json').read_text())
    full = next(c for c in cfg['cases'] if c['id'] == 'full')
    levers = pk['levers']
    ids = [l['id'] for l in levers]
    base = {l['id']: l['options'][0]['key'] for l in levers}
    rec = pk['recommended']
    named = {
        'decided': base,
        'decided_standard_led': dict(base, credits='standard_led'),
        'recommended_keep_credits': dict(rec, credits='keep'),
        'recommended': rec,
    }
    cases = []
    for name, ch in named.items():
        c, _ = K.make_case(name, tuple(ch[i] for i in ids), levers, pk, full)
        cases.append(c)
    runs = K.run_cases(cases, cfg['world'])
    infl = pr['inflation']
    cp = {n: credit_pieces(runs[n]['rows'], named[n]['grid'] == 'on', infl=infl) for n in named}
    scale = pr['ledger_credit_scaling']['ledger_tn'] / pr['ledger_credit_scaling']['model_tn']
    credit = dict(model_tn=cp, ledger_scale=scale,
                  redesign_alone_model_tn=cp['decided_standard_led'] - cp['decided'],
                  redesign_in_package_model_tn=cp['recommended'] - cp['recommended_keep_credits'],
                  package_vs_decided_model_tn=cp['recommended'] - cp['decided'])
    credit['redesign_alone_ledger_tn'] = [credit['redesign_alone_model_tn'] * scale * f for f in (0.67, 1.0, 1.33)]
    credit['package_vs_decided_ledger_tn'] = [credit['package_vs_decided_model_tn'] * scale * f for f in (0.67, 1.0, 1.33)]

    # bill protection: offset the recommended package's residential bill increase for LMI households, 2033-39
    bp = pr['bill_protection']
    rr, rd = runs['recommended']['rows'], runs['decided']['rows']
    inc = {y: max(0.0, (rr[y]['retail'] - rd[y]['retail']) / 100 * pa['residential_kwh_month'] * 12) for y in range(bp['years'][0], bp['years'][1] + 1)}
    bill_cost = tri(lambda i: sum(inc.values()) * bp['households_m'][i] / 1000)   # $B 2025
    bill_cost_nom = tri(lambda i: sum(v * bp['households_m'][i] / 1000 * (1 + infl) ** (y - 2025) for y, v in inc.items()) / 1000)

    # disaster package
    D = pr['disaster']
    ramp = {int(k): v for k, v in D['ramp'].items()}
    rows, tiers = [], {}
    for c in D['components']:
        ann = c.get('annual', [0, 0, 0])
        ten = tri(lambda i: sum(ann[i] * ramp.get(y, 1.0) for y in W10))
        ten_nom = tri(lambda i: sum(ann[i] * ramp.get(y, 1.0) * (1 + infl) ** (y - 2025) for y in W10) / 1000)
        one = c.get('one_time', [0, 0, 0])
        avoided = tri(lambda i: ten[1] * c['bcr'][i]) if c.get('bcr') else None
        row = dict(id=c['id'], tier=c['tier'], policy=c['policy'], label=c['label'], annual_bn_2025=ann, ten_year_bn_2025=ten,
                   ten_year_nominal_tn=ten_nom, one_time_bn=one, d4=c['d4'], avoided_losses_bn_not_banked=avoided,
                   contingent_bn=c.get('contingent_bn'), basis=c['basis'])
        rows.append(row)
        t = tiers.setdefault(c['tier'], dict(ten=[0, 0, 0], nom=[0, 0, 0], one=[0, 0, 0]))
        for i in range(3):
            t['ten'][i] += ten[i]; t['nom'][i] += ten_nom[i]; t['one'][i] += one[i]
    perm = tri(lambda i: sum(r['ten_year_bn_2025'][i] for r in rows if r['tier'] in ('core', 'full') and r['d4'].startswith('permanent')))
    cap = tri(lambda i: sum(r['ten_year_bn_2025'][i] for r in rows if r['tier'] in ('core', 'full') and r['d4'].startswith('time-limited')))
    gf = grid_finance(pr['grid_financing'])

    # whole-package budget, 2030-39, $T nominal (low / mid / high), by D4 class and financing source
    nom = lambda bn_2025_by_year: sum(v * (1 + infl) ** (y - 2025) for y, v in bn_2025_by_year.items()) / 1000
    even = lambda total, years: {y: total / len(years) for y in years}
    ind = tri(lambda i: [0.67, 1.0, 1.33][i] * sum((rr[y]['credInd'] - rd[y]['credInd']) * (1 + infl) ** (y - 2025) for y in W10) / 1000)
    rev = sum(((rr[y]['gross'] - rr[y]['rev']['methane']) - (rd[y]['gross'] - rd[y]['rev']['methane'])) * (1 + infl) ** (y - 2025) for y in W10) / 1000
    wx_ext = [45.0, 67.5, 112.5]
    lean = next(v for v in gf if v['id'] == 'lean')
    om = {it['id']: it for it in pk['off_model']['items']}
    disaster_perm = tri(lambda i: sum(r['ten_year_nominal_tn'][i] for r in rows if r['tier'] == 'core' and r['d4'].startswith('permanent')))
    disaster_cap = tri(lambda i: sum(r['ten_year_nominal_tn'][i] for r in rows if r['tier'] == 'core' and r['d4'].startswith('time-limited')))
    disaster_full = tiers['full']['nom']
    lines = [
        ('Credit redesign (standard-led) under stronger standards, ledger terms', 'permanent', 'reduces CLI-1', sorted(credit['package_vs_decided_ledger_tn'], reverse=True)),
        ('Bill protection for low- and moderate-income households, 2033-39', 'permanent', 'general fund', bill_cost_nom),
        ('Disaster core: permanent pieces (D2, D3, D6, D7)', 'permanent', 'general fund', disaster_perm),
        ('CLI-13 agricultural payments', 'permanent', 'general fund', tri(lambda i: nom(even(om['ag']['cost_bn_2030_39'][i], W10)))),
        ('Public grid delivery, lean tranche 1 (deficit cost)', 'time-limited capital', 'D4-B borrowing; loans repaid by transmission charges', tri(lambda i: nom(even(lean['deficit_cost_bn'][i], W10)))),
        ('Low-income heat-pump retrofits (CLI-5W)', 'time-limited capital', 'credit-redesign savings (no borrowing)', tri(lambda i: nom(even(wx_ext[i], range(2031, 2040))))),
        ('Disaster core: capital pieces (D1 mitigation fund, D5 wildfire)', 'time-limited capital', 'D4-B borrowing', disaster_cap),
        ('Clean-industry contracts (model industrial-support estimate)', 'time-limited capital', 'process-fee receipts first', ind),
        ('CLI-13 forests and carbon-removal purchases', 'time-limited capital', 'process-fee receipts first', tri(lambda i: nom(even(om['land']['cost_bn_2030_39'][i] + om['removal']['cost_bn_2030_39'][i], W10)))),
        ('Disaster full tier (D8 insurance help, D9 buyouts): develop', 'mixed', 'not yet financed', disaster_full),
    ]
    budget = dict(lines=[dict(item=a_, d4=b_, source=c_, tn=v_) for a_, b_, c_, v_ in lines], process_fee_receipts_tn=rev,
                  freed_d4b_room_bn=pr['freed_d4b_room_bn'], freed_d4b_basis=pr['freed_d4b_basis'])
    for cls in ('permanent', 'time-limited capital'):
        budget[cls] = tri(lambda i: sum(l_[3][i] for l_ in lines if l_[1] == cls))
    budget['d4b_draw_tn'] = tri(lambda i: sum(l_[3][i] for l_ in lines if l_[2].startswith('D4-B')))
    budget['fee_financed_tn'] = tri(lambda i: sum(l_[3][i] for l_ in lines if l_[2].startswith('process-fee')))
    budget['credit_financed_tn'] = tri(lambda i: sum(l_[3][i] for l_ in lines if l_[2].startswith('credit-redesign')))
    budget['permanent_after_retrofits_tn'] = tri(lambda i: budget['permanent'][i] + budget['credit_financed_tn'][i])

    data = dict(budget=budget, grid_financing=gf, credit_redesign=credit, bill_protection=dict(cost_bn_2025=bill_cost, cost_nominal_tn=bill_cost_nom, annual_increase_per_household=inc),
                disaster=dict(rows=rows, tiers=tiers, permanent_ten_year_bn=perm, time_limited_ten_year_bn=cap,
                              unbudgeted_supplemental_gap_bn_yr=D['unbudgeted_supplemental_gap_bn_yr'], baseline=D['baseline']),
                source_sha256={p: hashlib.sha256((ROOT / p).read_bytes()).hexdigest() for p in SOURCES})
    md = report(pr, data)
    buf = io.StringIO()
    w = csv.writer(buf, lineterminator='\n')
    w.writerow(['id', 'tier', 'policy_id', 'component', 'annual_bn_2025_low', 'annual_mid', 'annual_high', 'ten_year_2030_39_bn_2025_low', 'ten_year_mid', 'ten_year_high',
                'ten_year_nominal_tn_mid', 'one_time_bn_low', 'one_time_mid', 'one_time_high', 'd4_class', 'avoided_losses_bn_mid_not_banked', 'contingent_exposure_bn_mid', 'basis'])
    for r in rows:
        w.writerow([r['id'], r['tier'], r['policy'], r['label'], *r['annual_bn_2025'], *[round(x, 2) for x in r['ten_year_bn_2025']], round(r['ten_year_nominal_tn'][1], 4),
                    *r['one_time_bn'], r['d4'], round(r['avoided_losses_bn_not_banked'][1], 1) if r['avoided_losses_bn_not_banked'] else '',
                    r['contingent_bn'][1] if r['contingent_bn'] else '', r['basis']])
    out = ROOT / 'build/climate-portfolio'
    out.mkdir(parents=True, exist_ok=True)
    files = {'climate-portfolio-pricing.md': md, 'climate-portfolio-pricing.json': json.dumps(data, indent=1, sort_keys=True) + '\n',
             'climate-portfolio-disaster-components.csv': buf.getvalue()}
    for name, text in files.items():
        (out / name).write_text(text)
        if args.write:
            (ROOT / 'sources' / name).write_text(text)
    print(f"grid lean deficit cost mid {gf[1]['deficit_cost_bn'][1]:.0f}B; disaster core mid {tiers['core']['ten'][1]:.0f}B")


def r3(x, d=0, sign=False):
    return ' / '.join(P.fmt(v, d, sign=sign) for v in x)


def report(pr, d):
    L = ['# Climate portfolio pricing: grid financing, credit redesign, bill protection and disaster preparedness', '',
         '*Generated by `index/tools/climate-portfolio/pricing.py` from `pricing.json`; do not edit by hand. Read with '
         '[climate-portfolio-allocation.md](climate-portfolio-allocation.md) and [climate-portfolio-disaster-resilience.md](climate-portfolio-disaster-resilience.md). '
         'Ranges are low / mid / high; 2025 dollars unless marked.*', '']
    bu = d['budget']
    L += ['## Whole-package budget, 2030-39 ($T nominal, low / mid / high)', '',
          'The recommended climate package plus the core disaster tier, by D4 class and financing source. Negative is a saving. The process-emissions fee '
          'is channel money, shown separately.', '',
          '| Item | D4 class | Financing | $T nominal |', '| --- | --- | --- | --- |']
    for l_ in bu['lines']:
        L.append(f"| {l_['item']} | {l_['d4']} | {l_['source']} | {r3(l_['tn'], 3, True)} |")
    L += ['', f"- Permanent items net: {r3(bu['permanent'], 3, True)}T. Credit savings exceed the permanent additions, so the D4-B maturity test is helped, not hurt.",
          f"- Time-limited capital: {r3(bu['time-limited capital'], 3, True)}T, of which D4-B borrowing {r3(bu['d4b_draw_tn'], 3, True)}T against about ${bu['freed_d4b_room_bn']}B of room ({bu['freed_d4b_basis']}).",
          f"- Paying the retrofits from the credit savings leaves permanent items at {r3(bu['permanent_after_retrofits_tn'], 3, True)}T: still a net saving, with no borrowing for retrofits. Borrowing then uses about {100*bu['d4b_draw_tn'][1]*1000/bu['freed_d4b_room_bn']:.0f}% of the freed room at the midpoint.",
          f"- Process-emissions fee receipts in the recommended package: {bu['process_fee_receipts_tn']:+.3f}T over 2030-39, against {r3(bu['fee_financed_tn'], 3, True)}T of clean-industry contracts, forests and removal purchases proposed to draw on them first.", '']
    L += ['## Grid financing windows', '',
         'Budget cost under the Federal Credit Reform Act counts grants in full, direct loans at their subsidy cost and contracts at expected net cost. '
         '"Gross financing" is what Treasury borrows to make the program work, much of it repaid. Loan repayments fall on transmission charges, '
         f"shown as a bill effect at {pr['grid_financing']['kwh_month']} kWh a month before system savings; the DOE National Transmission Planning Study "
         'finds $1.60-1.80 of system cost saved per $1 of transmission, so the net bill effect is likely a saving (not banked).', '',
         '| Variant | Grants / loans / contracts ($B) | Budget (deficit) cost, $B | Physical build enabled, $B | Gross Treasury financing, $B | Loan repayment on bills, $/month | System savings to 2050, $B (not banked) |',
         '| --- | --- | --- | --- | --- | --- | --- |']
    for v in d['grid_financing']:
        L.append(f"| {v['label']} | {v['grants']} / {v['loans']} / {v['contracts']} | {r3(v['deficit_cost_bn'])} | {v['physical_build_bn']:.0f} | {v['gross_financing_bn']:.0f} | "
                 f"{v['bill_month_from_loans']:.2f} | {r3(v['system_savings_bn_to_2050'])} |")
    L += ['', 'Windows:'] + [f"- **{w['label']}** ({w['instrument']}). {w.get('basis', '')}" for w in pr['grid_financing']['windows']]
    c = d['credit_redesign']
    L += ['', '## Credit redesign in ledger terms', '',
          f"Credit outlays in the model (credits less grid-program cost, plus the industrial-support estimate), $T nominal 2030-39. Ledger scaling factor {c['ledger_scale']:.2f} "
          f"({pr['ledger_credit_scaling']['basis']}).", '',
          '| Package | Model credit outlays, $T nominal 2030-39 |', '| --- | --- |']
    for k, v in c['model_tn'].items():
        L.append(f"| {k} | {v:.3f} |")
    L += ['', f"- Standard-led redesign alone (decided package otherwise): {c['redesign_alone_model_tn']:+.3f}T in the model; in ledger terms {r3(c['redesign_alone_ledger_tn'], 2, True)}T.",
          f"- Inside the recommended package (against the same package with credits kept): {c['redesign_in_package_model_tn']:+.3f}T in the model. Stronger standards raise credit claims if credits are kept, so the redesign saves more inside the package.",
          f"- Recommended package credit outlays against the decided package: {c['package_vs_decided_model_tn']:+.3f}T in the model; in ledger terms {r3(c['package_vs_decided_ledger_tn'], 2, True)}T.",
          'These are estimates on the model\'s take-up, not a JCT score; count the low end in D4 tests until scored.']
    b = d['bill_protection']
    L += ['', '## Bill protection', '', f"Offsetting the recommended package's residential bill increase for low- and moderate-income households over 2033-39 costs {r3(b['cost_bn_2025'], 1)} $B (2025 dollars), "
          f"{r3(b['cost_nominal_tn'], 3)} $T nominal. Annual increase per household: " + ', '.join(f"{y} ${v:.0f}" for y, v in b['annual_increase_per_household'].items()) + '.']
    D = d['disaster']
    L += ['', '## Disaster preparedness and response package', '', 'Starting from current law (sourced):', '']
    L += [f"- {x['item']}: {x['value']} ({x['source']})" for x in D['baseline']]
    L += ['', '| ID | Tier | Policy | Component | $B a year (2025 $) | 2030-39, $B 2025 | 2030-39, $T nominal (mid) | One-time, $B | D4 class | Avoided losses, $B (mid, not banked) |',
          '| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |']
    for r in D['rows']:
        av = P.fmt(r['avoided_losses_bn_not_banked'][1]) if r['avoided_losses_bn_not_banked'] else ('contingent ' + str(r['contingent_bn'][1]) + 'B' if r['contingent_bn'] else '')
        L.append(f"| {r['id']} | {r['tier']} | {r['policy']} | {r['label']} | {r3(r['annual_bn_2025'], 1)} | {r3(r['ten_year_bn_2025'])} | {r['ten_year_nominal_tn'][1]:.3f} | "
                 f"{r3(r['one_time_bn'], 1)} | {r['d4']} | {av} |")
    L += ['', '| Tier | 2030-39, $B 2025 | $T nominal | One-time, $B |', '| --- | --- | --- | --- |']
    for t, v in D['tiers'].items():
        L.append(f"| {t} | {r3(v['ten'])} | {r3(v['nom'], 3)} | {r3(v['one'], 1)} |")
    g = D['unbudgeted_supplemental_gap_bn_yr']
    L += ['', f"Core and full tiers by D4 class over 2030-39: permanent {r3(D['permanent_ten_year_bn'])} $B; time-limited capital {r3(D['time_limited_ten_year_bn'])} $B (2025 dollars). "
          f"Rows marked counted_elsewhere are in CAP-7/CAP-7S and are not added again.", '',
          f"**Unbudgeted disaster supplementals (current law).** About ${g[0]}-{g[2]}B a year (mid ${g[1]}B) of recurring disaster appropriations sits outside the extrapolated baseline. "
          f"{pr['disaster']['unbudgeted_basis']}.", '',
          '## Reproduction', '', '`bash index/tools/run-all.sh`, then `python3 index/tools/climate-portfolio/pricing.py --write`.', '',
          'Source hashes (SHA-256):', ''] + [f"- `{p}`: `{h}`" for p, h in d['source_sha256'].items()]
    return '\n'.join(L) + '\n'


if __name__ == '__main__':
    main()
