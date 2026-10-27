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
    """Credit outlays only (credits less any grid-program cost; the industrial-support estimate is a separate line), $T nominal."""
    gp = 12.0 if grid_on else 0.0
    return sum((rows[y]['credits'] - (gp if 2030 <= y <= 2039 else 0)) * (1 + infl) ** (y - 2025) for y in years) / 1000


CASES = ('favorable', 'central', 'conservative', 'unfavorable')
SAVE = {'favorable': 1.33, 'central': 1.0, 'conservative': 0.67, 'unfavorable': 0.67}   # credit-saving multiplier
COST = {'favorable': 0, 'central': 1, 'conservative': 1, 'unfavorable': 2}              # index into low / mid / high costs
YEARS = range(2030, 2051)


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
        'decided_old100': dict(base, price='old100'),
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
    perm = tri(lambda i: sum(r['ten_year_bn_2025'][i] for r in rows if r['tier'] in ('core', 'fuller', 'backstop') and r['d4'].startswith('permanent')))
    cap = tri(lambda i: sum(r['ten_year_bn_2025'][i] for r in rows if r['tier'] in ('core', 'fuller') and r['d4'].startswith('time-limited')))
    gf = grid_finance(pr['grid_financing'])

    # whole-package budget by year and account, 2030-50, nominal $B. Accounts: general fund (not borrowed), D4-B borrowing,
    # and the carbon channel's transition share. Four cases pair savings and costs consistently (see CASES).
    defl = lambda y: (1 + infl) ** (y - 2025)
    gp = lambda n, y: 12.0 if named[n]['grid'] == 'on' and 2030 <= y <= 2039 else 0.0
    d_cred = {y: (rr[y]['credits'] - gp('recommended', y)) - (rd[y]['credits'] - gp('decided', y)) for y in YEARS}
    d_ind = {y: rr[y]['credInd'] - rd[y]['credInd'] for y in YEARS}
    c1 = lambda r: r['gross'] - r['rev']['methane']
    d_rev = {y: c1(rr[y]) - c1(rd[y]) for y in YEARS}
    d_proc = {y: rr[y]['rev']['process'] - rd[y]['rev']['process'] for y in YEARS}
    lean = next(v for v in gf if v['id'] == 'lean')
    om = {it['id']: it for it in pk['off_model']['items']}
    ch = pr['channel']
    comp = {c['id']: c for c in D['components']}
    rmp = lambda y: ramp.get(y, 1.0) if y <= 2039 else 1.0
    wx_ext = [45.0, 67.5, 112.5]
    items = []
    def item(iid, label, account, d4, fn):
        items.append(dict(id=iid, label=label, account=account, d4=d4,
                          path={k: {y: fn(k, y) * defl(y) for y in YEARS} for k in CASES}))
    item('credits', 'Credit redesign (standard-led, with snap-back), ledger terms; industrial support excluded', 'general fund', 'permanent',
         lambda k, y: d_cred[y] * scale * SAVE[k])
    item('cx', 'Income and payroll tax offset (CX, 25%) on the added REV-C1 receipts', 'general fund', 'permanent',
         lambda k, y: ch['cx_share'] * d_rev[y])
    item('bill', 'Bill protection for low- and moderate-income households (while the increase lasts)', 'general fund', 'permanent',
         lambda k, y: (max(0.0, (rr[y]['retail'] - rd[y]['retail']) / 100 * pa['residential_kwh_month'] * 12) * bp['households_m'][COST[k]] / 1000) if y >= bp['years'][0] else 0.0)
    item('disaster_perm', 'Disaster permanent pieces: D2, D3, D6, D7 and D8', 'general fund', 'permanent',
         lambda k, y: sum(comp[i]['annual'][COST[k]] for i in ('D2', 'D3', 'D6', 'D7', 'D8')) * rmp(y))
    item('reinsurance', 'CLI-7C reinsurance facility, expected net cost (decided Oct 27; $75-150B contingent liability disclosed, not scored)', 'general fund', 'permanent',
         lambda k, y: comp['D10']['annual'][COST[k]] if y >= 2031 else 0.0)
    item('nfip', 'NFIP debt resolution (scored cost, FY2030)', 'general fund', 'one-time',
         lambda k, y: comp['D4']['one_time'][COST[k]] if y == 2030 else 0.0)
    item('ag', 'CLI-13 agricultural payments (continuing)', 'general fund', 'permanent',
         lambda k, y: om['ag']['cost_bn_2030_39'][COST[k]] / 10)
    item('retrofits', 'Low-income heat-pump retrofits (CLI-5W), paid from credit savings', 'general fund', 'time-limited',
         lambda k, y: wx_ext[COST[k]] / 9 if 2031 <= y <= 2039 else 0.0)
    item('grid', 'Public grid delivery, lean tranche 1 (deficit cost)', 'D4-B borrowing', 'time-limited capital',
         lambda k, y: lean['deficit_cost_bn'][COST[k]] / 10 if y <= 2039 else 0.0)
    item('disaster_cap', 'Disaster capital pieces: D1 mitigation fund, D5 wildfire, D9 buyouts', 'D4-B borrowing', 'time-limited capital',
         lambda k, y: sum(comp[i]['annual'][COST[k]] for i in ('D1', 'D5', 'D9')) * rmp(y) if y <= 2039 else 0.0)
    item('industry', 'Clean-industry contracts (model industrial-support estimate)', 'carbon channel', 'time-limited',
         lambda k, y: d_ind[y] * [0.67, 1.0, 1.33][COST[k]])
    item('forests', 'CLI-13 forests and reforestation', 'carbon channel', 'time-limited',
         lambda k, y: om['land']['cost_bn_2030_39'][COST[k]] / 10 if y <= 2039 else 0.0)
    transition = {y: ch['transition_share'] * d_rev[y] * defl(y) for y in YEARS}
    dividend = {y: ch['dividend_share'] * d_rev[y] * defl(y) for y in YEARS}

    def acct(k, years, accounts=None, d4=None):
        return sum(it['path'][k][y] for it in items for y in years
                   if (accounts is None or it['account'] in accounts) and (d4 is None or it['d4'] in d4))
    budget = dict(cases=list(CASES), save_multiplier=SAVE, cost_index=COST, freed_d4b_room_bn=pr['freed_d4b_room_bn'],
                  freed_d4b_basis=pr['freed_d4b_basis'], channel=ch,
                  items=[dict(id=it['id'], label=it['label'], account=it['account'], d4=it['d4'],
                              window_bn={k: sum(it['path'][k][y] for y in W10) for k in CASES},
                              fy2040_bn={k: it['path'][k][2040] for k in CASES}, fy2050_bn={k: it['path'][k][2050] for k in CASES}) for it in items],
                  rev_c1_change_bn={'window': sum(d_rev[y] * defl(y) for y in W10), 'fy2040': d_rev[2040] * defl(2040), 'fy2050': d_rev[2050] * defl(2050)},
                  process_receipts_bn={'window': sum(d_proc[y] * defl(y) for y in W10)},
                  transition_bn={'window': sum(transition[y] for y in W10), 'fy2040': transition[2040], 'fy2050': transition[2050]},
                  dividend_bn={'window': sum(dividend[y] for y in W10), 'fy2040': dividend[2040], 'fy2050': dividend[2050]})
    res = {}
    for k in CASES:
        chan_use = {y: acct(k, [y], accounts={'carbon channel'}) for y in YEARS}
        shortfall = {y: max(0.0, chan_use[y] - transition[y]) for y in YEARS}       # channel uses beyond the transition share fall on the general fund
        surplus = {y: max(0.0, transition[y] - chan_use[y]) for y in YEARS}
        gf_y = {y: acct(k, [y], accounts={'general fund'}) + shortfall[y] for y in YEARS}
        res[k] = dict(general_fund_window_bn=sum(gf_y[y] for y in W10), d4b_window_bn=acct(k, W10, accounts={'D4-B borrowing'}),
                      channel_uses_window_bn=sum(chan_use[y] for y in W10), channel_shortfall_window_bn=sum(shortfall[y] for y in W10),
                      channel_surplus_window_bn=sum(surplus[y] for y in W10),
                      general_fund_fy2040_bn=gf_y[2040], general_fund_fy2050_bn=gf_y[2050],
                      general_fund_path_bn={str(y): gf_y[y] for y in YEARS})
        res[k]['d4b_over_room_bn'] = res[k]['d4b_window_bn'] - pr['freed_d4b_room_bn']
    budget['results'] = res
    # what the D7 split of the increment would need to change to cover the CX offset and any general-fund gap at FY2040
    adults_2035 = rr[2035]['pop'] * 0.77
    budget['dividend_per_adult_2035_from_increment'] = ch['dividend_share'] * d_rev[2035] * defl(2035) * 1e9 / (adults_2035 * 1e6)
    budget['cx_per_adult_2035'] = ch['cx_share'] * d_rev[2035] * defl(2035) * 1e9 / (adults_2035 * 1e6)
    budget['payment'] = payment_options(pr, items, CASES, YEARS, W10, d_rev, d_proc, defl, ch,
                                        {y: c1(rd[y]) - c1(runs['decided_old100']['rows'][y]) for y in YEARS}, adults_2035)
    removal = om['removal']
    budget['removal_outside'] = dict(window_bn_2025=removal['cost_bn_2030_39'], mt_2050=removal['mt_2050'], run_rate_2050_bn_2025=pr['removal_run_rate_2050_bn'])

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


PAY_OPTIONS = {
    'O1': 'D7 as is: every added dollar splits 80/20; the general fund pays CX and any channel shortfall',
    'O2': 'CX recapture: 25% of the added receipts go to the general fund; the dividend keeps 55% of the increment',
    'O3': 'Process fee outside the dividend (like REV-C3): process receipts fund the carbon channel first, any surplus to the general fund',
    'O5': "Process fee pays the package's net cost: each year process receipts cover the package's remaining general-fund cost "
          "(carbon-channel shortfall and general-fund items); the rest follows D7",
}
# O4 (withdrawn Oct 26 after review): it also spent the $150 step's transition increment, which the shared ledger already credits to CLI-5
# (ledger-build.py: CLI-5 own revenue = 0.2 x C1 + C2 + C3), so it double counted.
QUINTILE_ADULTS = (1.3, 1.7, 2.0, 2.2, 2.4)   # adults per consumer unit, lowest to highest quintile (index/climate-carbon-model.md)


def payment_options(pr, items, cases, years, w10, d_rev, d_proc, defl, ch, step_rev, adults_2035):
    """General-fund result and dividend change of each way to pay for the package increment, nominal $B."""
    out = {}
    for o in PAY_OPTIONS:
        res = {}
        for k in cases:
            gf, div = {}, {}
            for y in years:
                inc, proc = d_rev[y] * defl(y), d_proc[y] * defl(y)
                comb = inc - proc
                gf_items = sum(it['path'][k][y] for it in items if it['account'] == 'general fund' and it['id'] != 'cx')
                chan = sum(it['path'][k][y] for it in items if it['account'] == 'carbon channel')
                cx = ch['cx_share'] * inc
                if o == 'O1':
                    d, trans, gf_rcpt = ch['dividend_share'] * inc, ch['transition_share'] * inc, 0.0
                elif o == 'O2':
                    d, trans, gf_rcpt = (ch['dividend_share'] - ch['cx_share']) * inc, ch['transition_share'] * inc, ch['cx_share'] * inc
                else:
                    d, trans, gf_rcpt = ch['dividend_share'] * comb, ch['transition_share'] * comb + proc, 0.0
                if o == 'O5':
                    d, trans, gf_rcpt = ch['dividend_share'] * inc, ch['transition_share'] * inc, 0.0
                short, surplus = max(0.0, chan - trans), max(0.0, trans - chan)
                gf[y] = gf_items + cx + short - gf_rcpt - (surplus if o in ('O3', 'O5') else 0.0)
                if o == 'O5':
                    divert = min(max(0.0, gf[y]), ch['dividend_share'] * max(0.0, proc))
                    gf[y] -= divert; d -= divert
                div[y] = d
            res[k] = dict(general_fund_window_bn=sum(gf[y] for y in w10), general_fund_fy2040_bn=gf[2040], general_fund_fy2050_bn=gf[2050],
                          dividend_window_bn=sum(div[y] for y in w10), dividend_2035_bn=div[2035], dividend_fy2050_bn=div[2050],
                          dividend_vs_d7_window_bn=sum(div[y] - ch['dividend_share'] * d_rev[y] * defl(y) for y in w10),
                          dividend_vs_d7_fy2050_bn=div[2050] - ch['dividend_share'] * d_rev[2050] * defl(2050))
        # per adult against D7, central case: 2030-39 average and 2050, nominal dollars (adults held at the 2035 count; 2050 slightly overstated)
        pa_w = res['central']['dividend_vs_d7_window_bn'] / 10 * 1e9 / (adults_2035 * 1e6)
        pa_50 = res['central']['dividend_vs_d7_fy2050_bn'] * 1e9 / (adults_2035 * 1e6)
        out[o] = dict(label=PAY_OPTIONS[o], cases=res, dividend_change_per_adult_avg_2030_39=pa_w, dividend_change_per_adult_2050=pa_50,
                      dividend_change_per_household_avg_2030_39=[pa_w * a for a in QUINTILE_ADULTS],
                      dividend_change_per_household_2050=[pa_50 * a for a in QUINTILE_ADULTS])
    out['step_transition_bn'] = dict(window=sum(ch['transition_share'] * step_rev[y] * defl(y) for y in w10),
                                     fy2040=ch['transition_share'] * step_rev[2040] * defl(2040))
    return out


def r3(x, d=0, sign=False):
    return ' / '.join(P.fmt(v, d, sign=sign) for v in x)


def report(pr, d):
    L = ['# Climate portfolio pricing: grid financing, credit redesign, bill protection and disaster preparedness', '',
         '*Generated by `index/tools/climate-portfolio/pricing.py` from `pricing.json`; do not edit by hand. Read with '
         '[climate-portfolio-allocation.md](climate-portfolio-allocation.md) and [climate-portfolio-disaster-resilience.md](climate-portfolio-disaster-resilience.md). '
         'Ranges are low / mid / high; 2025 dollars unless marked.*', '']
    bu = d['budget']
    C = bu['cases']
    f4 = lambda dct: ' / '.join(P.fmt(dct[k], 0, sign=True) for k in C)
    L += ['## Whole-package budget by account, with annual paths', '',
          'Package A (with the approved $150-by-2037 price) plus the core and fuller disaster tiers, nominal $B. Four cases pair savings and costs consistently: '
          '**favorable** (credit savings x1.33, low costs) / **central** / **conservative** (credit savings x0.67, the project rule until scored; central costs) / '
          '**unfavorable** (credit savings x0.67, high costs). Negative is a saving. Removal purchases (CLI-13) are kept outside the package and shown separately.', '',
          '**Accounts.** *General fund* items are paid without borrowing. *D4-B borrowing* covers time-limited capital. The *carbon channel* covers clean-industry contracts and forests, '
          f"financed first from the transition share ({int(100*bu['channel']['transition_share'])}%) of the added REV-C1 receipts. Under D7 the dividend takes {int(100*bu['channel']['dividend_share'])}% "
          f"and the general fund books a {int(100*bu['channel']['cx_share'])}% income and payroll tax offset (CX). {bu['channel']['basis']}", '',
          '| Item | Account | D4 class | 2030-39 | FY2040 | FY2050 |', '| --- | --- | --- | --- | --- | --- |']
    for it in bu['items']:
        L.append(f"| {it['label']} | {it['account']} | {it['d4']} | {f4(it['window_bn'])} | {f4(it['fy2040_bn'])} | {f4(it['fy2050_bn'])} |")
    R = bu['results']
    g = lambda key: ' / '.join(P.fmt(R[k][key], 0, sign=True) for k in C)
    L += ['', '| Account result ($B nominal; favorable / central / conservative / unfavorable) | Value |', '| --- | --- |',
          f"| General fund, 2030-39 (includes any channel shortfall) | {g('general_fund_window_bn')} |",
          f"| General fund, FY2040 (the D4-B maturity year) | {g('general_fund_fy2040_bn')} |",
          f"| General fund, FY2050 | {g('general_fund_fy2050_bn')} |",
          f"| D4-B borrowing, 2030-39 | {g('d4b_window_bn')} |",
          f"| D4-B borrowing over the ${bu['freed_d4b_room_bn']}B freed room (positive = overshoot) | {g('d4b_over_room_bn')} |",
          f"| Carbon channel: uses, 2030-39 | {g('channel_uses_window_bn')} |",
          f"| Carbon channel: shortfall in years when uses exceed the transition share (charged to the general fund, included above) | {g('channel_shortfall_window_bn')} |",
          f"| Carbon channel: transition-share surplus left over | {g('channel_surplus_window_bn')} |", '',
          f"Added REV-C1 receipts: {bu['rev_c1_change_bn']['window']:+,.0f}B over 2030-39 (FY2040 {bu['rev_c1_change_bn']['fy2040']:+,.0f}B), of which process coverage {bu['process_receipts_bn']['window']:+,.0f}B. "
          f"The dividend takes {bu['dividend_bn']['window']:+,.0f}B and the transition share {bu['transition_bn']['window']:+,.0f}B. "
          f"In 2035 the increment adds about ${bu['dividend_per_adult_2035_from_increment']:.0f} to each adult's dividend, and its CX offset costs the general fund the equivalent of about ${bu['cx_per_adult_2035']:.0f} an adult.", '',
          '## Paying for the package: options', '',
          "Each option applies to the package's increment over the decided package (the $150 path is already in the shared ledger). "
          "General fund is nominal $B, favorable / central / conservative / unfavorable; a negative is a saving. The dividend columns are the change against D7 per consumer unit, "
          "central case, nominal dollars, lowest to highest quintile (adults per unit 1.3 / 1.7 / 2.0 / 2.2 / 2.4). "
          f"The $150 step's own transition share (about ${bu['payment']['step_transition_bn']['window']:,.0f}B over 2030-39 in the model) is already credited to CLI-5 in the shared ledger "
          "(CLI-5's own revenue is 20% of REV-C1 plus REV-C2 and REV-C3), so no option spends it again; O4, which did, is withdrawn. "
          "Options O2, O3 and O5 change how D7's split applies to new receipts, so they are Espen's.", '',
          '| Option | General fund 2030-39 | FY2040 | FY2050 | Dividend change per unit, 2030-39 average | Dividend change per unit, 2050 |',
          '| --- | --- | --- | --- | --- | --- |'] + [
          f"| **{o}**: {bu['payment'][o]['label']} | {' / '.join(P.fmt(bu['payment'][o]['cases'][k]['general_fund_window_bn'], 0, sign=True) for k in C)} | "
          f"{' / '.join(P.fmt(bu['payment'][o]['cases'][k]['general_fund_fy2040_bn'], 0, sign=True) for k in C)} | "
          f"{' / '.join(P.fmt(bu['payment'][o]['cases'][k]['general_fund_fy2050_bn'], 0, sign=True) for k in C)} | "
          f"{' / '.join(P.fmt(v, 0, sign=True) for v in bu['payment'][o]['dividend_change_per_household_avg_2030_39'])} | "
          f"{' / '.join(P.fmt(v, 0, sign=True) for v in bu['payment'][o]['dividend_change_per_household_2050'])} |"
          for o in PAY_OPTIONS] + ['',
          f"**Proposed: {pr['payment_rule']['proposed']}** ({pr['payment_rule']['status']}). {pr['payment_rule']['why']}", '',
          f"**Removal purchases, outside the package.** About {r3(bu['removal_outside']['window_bn_2025'])} $B (2025 dollars) over 2030-39, rising to roughly {r3(bu['removal_outside']['run_rate_2050_bn_2025'])} $B a year by 2050 at "
          f"{r3(bu['removal_outside']['mt_2050'])} Mt. That continuing obligation needs its own financing decision and maturity test before it enters any selected package.", '']
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
