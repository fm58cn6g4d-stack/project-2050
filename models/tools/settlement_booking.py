"""Stage G's financing settlement, booked (step 7): derives each booked item's year-by-year path and its D3 rows.

Role: one derivation for the settlement the budget model books. `models/data/inputs/settlement.json` holds the booked
choices (the switches, the health contribution's base rate and the items, each with its DEC- row). This script prices
each item with the same option functions the settlement's screens used (`financing-protection/packages.py` and
`budget_scan.py`), on the plan before the booking (`build_case(..., settlement=False)`), and writes:
  * `models/data/inputs/settlement-paths.csv`: each item's path, FY2026-56, $B (positive raises the general-fund gap),
    which `models/tools/recovery-budget/model.py` books as "Settlement Snn: ..." lines in every case;
  * the settlement's D3 rows in `models/data/inputs/incidence-rows.csv` (the `HCUg`, `HCUwg`, `HCAg`, `HS2g`, `EDUPg`
    and `GXg` rows) and scenario Q-G in `scenarios.json`, which is Q-H7 with them.
Status: booked inputs; `test_settlement_booking.py` checks that the committed tables equal this derivation and that the
booked package closes FY2040-56. The same pattern as `health_booking.py` and `care_booking.py`.

Run after the common rebuild:
    python3 models/tools/settlement_booking.py           # print the derivation and the check
    python3 models/tools/settlement_booking.py --write   # rewrite settlement-paths.csv and the D3 amounts
    python3 models/tools/settlement_booking.py --solve   # the lowest base rate, to 0.05, that closes FY2040-56
"""
import argparse
import csv
import json
import math
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'models/tools/financing-protection'))
import packages as K      # noqa: E402
import budget_scan as S   # noqa: E402

INPUTS = ROOT / 'models/data/inputs'
YEARS = K.YEARS
COLS = ['id', 'line', 'side', 'dec'] + ['y%d' % y for y in YEARS]


def doc():
    return json.loads((INPUTS / 'settlement.json').read_text())


def option(ctx, item, rate):
    params = dict(item['params'])
    if params.get('rate') == 'health_contribution_base_rate':
        params['rate'] = rate
    fn = S.OPTIONS.get(item['option']) or K.OPTIONS[item['option']]
    return fn(ctx, **params)


def derive(ctx, d=None, rate=None):
    """[(item, option result, path)] for every booked item; the path is the option's one adjustment, FY2026-56."""
    d = d or doc()
    rate = d['health_contribution_base_rate']['rate'] if rate is None else rate
    out = []
    for it in d['items']:
        o = option(ctx, it, rate)
        (label, path), = o['adjust'].items()
        out.append((it, o, {y: path.get(y, 0.0) for y in YEARS}))
    return out


def switch_options(d):
    """The switches as the screens' options, so a screen on the pre-settlement base reproduces the booked case."""
    sw = d['switches']
    return [K.OPTIONS['end_adult_credit'](None) if sw['recovery_credit_multiple'] == 0 else None,
            dict(kw=dict(education_rate=sw['education_rate_points'])),
            dict(kw=dict(hi_grant_points=sw['hi_grant_payroll_points']))]


def rows(derived):
    return [dict(id=it['id'], line=it['line'], side=it['side'], dec=it['dec'],
                 **{'y%d' % y: '%.4f' % p[y] for y in YEARS}) for it, o, p in derived]


def write_paths(derived):
    with (INPUTS / 'settlement-paths.csv').open('w', newline='') as fh:
        w = csv.DictWriter(fh, fieldnames=COLS, lineterminator='\n')
        w.writeheader()
        w.writerows(rows(derived))


# ---------------------------------------------------------------- the booked case and the rule
def booked_case(ctx):
    """case `mixed` as the budget model now books it (settlement on)."""
    return K.m.build_case('mixed', ctx.f, ctx.b, ctx.old, ctx.u)


def screened_case(ctx, d, rate):
    """The same package priced the screens' way on the pre-settlement base, as a check on the booking."""
    opts = [o for it, o, p in derive(ctx, d, rate)]
    # the switches: the credit, the 2 points (the fold's kw), the education rate, the HI grant, the delivery line
    adj = {}
    for o in opts:
        for k, v in o['adjust'].items():
            adj[k] = {'annual_bn': {str(y): v.get(y, 0.0) for y in YEARS}}
    dl = ctx.line('delivery_contingency')
    adj['delivery line removed'] = {'annual_bn': {str(y): -dl[y] for y in YEARS}}
    sw = d['switches']
    with K.education_rate(sw['education_rate_points']), K.hi_grant(sw['hi_grant_payroll_points']):
        c = K.m.build_case('screen', ctx.f, ctx.b, ctx.old, ctx.u, spending_adjustments=adj, settlement=False,
                           broad_rate=sw['broad_rate_points'], credit_multiple=sw['recovery_credit_multiple'])
    return c


def gap(c):
    return {r['year']: r['agenda_gf_primary_bn'] for r in c['rows']}


def solve(ctx, d):
    """The lowest base rate, to 0.05 points, at which the screened package closes every year FY2040-56."""
    r = 3.25
    while r < 6:
        g = gap(screened_case(ctx, d, r))
        if all(g[y] <= 0.05 for y in range(2040, 2057)):
            return round(r, 2), g
        r = round(r + 0.05, 2)
    raise ValueError('no rate below 6% closes FY2040-56')


# ---------------------------------------------------------------- D3
D3_ROWS = {   # new row id: (Q-H7 row it replaces, or None for a delta row added beside a package row)
    'HCUg': 'HCU', 'HCUwg': 'HCUw', 'HCAg': 'HCA', 'HS2g': 'HS2', 'EDUPg': 'EDUP', 'GXg': None}


def d3_amounts(derived, hh=None):
    """The settlement's D3 amounts ($T, FY2030-39), from the items' own D3 edits (packages' convention) and EDUP at
    gross on the booked rate: {row id: amount}."""
    hh = hh or K.Household()
    table = dict(hh.D.OPTIONS)
    base = {rid: table[rid][1] for rid in ('HCU', 'HCUw', 'HCA', 'HS2', 'EDUP')}
    gx = next(r[3] for r in hh.D.ROWS if r[0] == 'GX')
    k = {rid: 1.0 for rid in list(base) + ['GX']}
    for it, o, p in derived:
        for e in o.get('d3', []):
            if e[0] == 'scale' and e[1] in k:
                k[e[1]] *= e[2]
            elif e[0] == 'drop' and e[1] not in ('ICB',):
                raise ValueError('unexpected D3 drop ' + str(e))
    rate = doc()['switches']['education_rate_points']
    out = {'HCUg': base['HCU'] * k['HCU'], 'HCUwg': base['HCUw'] * k['HCUw'], 'HCAg': base['HCA'] * k['HCA'],
           'HS2g': base['HS2'] * k['HS2'],
           # EDUP: Q-H7 carries it net of its 12.5% income-tax offset at 1.4 points; booked gross (what workers pay,
           # the convention of every other payroll row; the reviewer's note on #467) at the booked rate
           'EDUPg': base['EDUP'] * rate / 1.4 / (1 - 0.125),
           'GXg': gx * (k['GX'] - 1)}
    return {r: round(v, 4) for r, v in out.items()}


# ---------------------------------------------------------------- the restated figures (--report)
def risk_case(ctx, d, without):
    """The booked case with D2 and/or the wealth tax lost. Without HS2 the loss is HS2 net of the stack cap (S04),
    since the cap only trims HS2; the step 4b scan counted the cap's +$40B again (a correction, 2-settlement.md)."""
    adj = {}
    if 'D2' in without:
        adj['Without D2'] = {'annual_bn': {str(y): -v for y, v in ctx.component('HLT-7', 'national-budget').items()}}
    if 'HS2' in without:
        hs2 = ctx.line('HS2')
        cap = next(p for it, o, p in derive(ctx, d) if it['option'] == 'stack_cap')
        adj['Without HS2'] = {'annual_bn': {str(y): -hs2[y] - cap[y] for y in YEARS}}
    return K.m.build_case('risk', ctx.f, ctx.b, ctx.old, ctx.u, spending_adjustments=adj)


def report(ctx, d):
    der = derive(ctx, d)
    c = booked_case(ctx)
    before = K.m.build_case('before', ctx.f, ctx.b, ctx.old, ctx.u, settlement=False)
    g, g0 = gap(c), gap(before)
    by = {r['year']: r for r in c['rows']}
    hcu = ctx.line('HCU')
    per_point = lambda y: S.PER_POINT_2040 * hcu[y] / hcu[2040]
    out = dict(rate=d['health_contribution_base_rate']['rate'],
               gap={y: round(g[y], 1) for y in YEARS if y >= 2030}, gap_before={y: round(g0[y], 1) for y in YEARS if y >= 2030},
               gap_2030_39=round(sum(g[y] for y in K.m.W), 1), gap_before_2030_39=round(sum(g0[y] for y in K.m.W), 1),
               worst_year=max(range(2040, 2057), key=lambda y: g[y]), worst=round(max(g[y] for y in range(2040, 2057)), 1),
               debt={y: round(by[y]['debt_gdp'], 1) for y in (2039, 2040, 2045, 2050, 2056)},
               baseline_debt={y: round(100 * by[y]['baseline_debt_bn'] / by[y]['gdp_bn'], 1) for y in (2039, 2040, 2056)},
               debt_before={y: round(r['debt_gdp'], 1) for r in before['rows'] for y in (r['year'],) if y in (2040, 2056)},
               summary={k: c['summary'][k] for k in ('ss_depletion', 'ss_actuarial_balance', 'hi_depletion', 'education_depletion')},
               education_reserve_2040=round(next(r['reserve'] for r in c['education']['rows'] if r['year'] == 2040), 1),
               items=[(it['id'], it['line'], it['dec'], round(p[2040], 1), round(p[2045], 1), round(p[2056], 1),
                       round(sum(p[y] for y in K.m.W), 1)) for it, o, p in der],
               r_needed={y: round(out_r, 2) for y, out_r in
                         ((y, d['health_contribution_base_rate']['rate'] + g[y] / per_point(y)) for y in (2040, 2042, 2045, 2050, 2056))})
    risks = {}
    for name, w in (('without D2', ('D2',)), ('without HS2', ('HS2',)), ('without both', ('D2', 'HS2'))):
        r = gap(risk_case(ctx, d, w))
        risks[name] = {y: (round(r[y], 1), round(max(r[y], 0) / per_point(y), 2)) for y in (2040, 2045, 2056)}
    out['risks'] = risks
    # D3 on scenario Q-G, and its revenue-mix test
    hh = K.Household()
    name = next(n for n in hh.D.SCEN if n.startswith('Q-G'))
    o, drop = hh.D.SCEN[name]
    res, _ = hh.D.run(o, drop)
    out['d3'] = {g_: round(res[g_]['net']) for g_ in ('Q1', 'Q2', 'Q3', 'Q4', 'Q5', 'T1')}
    out['revenue_mix'] = hh.D.gf_test(o)[3]
    name7 = next(n for n in hh.D.SCEN if n.startswith('Q-H7'))
    o7, d7 = hh.D.SCEN[name7]
    out['d3_q_h7'] = {g_: round(hh.D.run(o7, d7)[0][g_]['net']) for g_ in ('Q1', 'Q2', 'Q3', 'Q4', 'Q5', 'T1')}
    out['d3_by_year'] = {y: v for y, v in hh.D.series(o).items() if y in (2033, 2035, 2037, 2039)} if hasattr(hh.D, 'series') else None
    out['take_home'] = S.take_home(sorted({3.25, out['rate'], 4.45}))
    return out


def markdown(r):
    yrs = (2030, 2033, 2035, 2036, 2037, 2038, 2039, 2040, 2041, 2042, 2045, 2050, 2056)
    L = ['# The financing settlement as booked: results', '',
         'Generated by `models/tools/settlement_booking.py --report` after the common rebuild (stage G step 7). The budget '
         'model\'s case `mixed` with the settlement booked (`models/data/inputs/settlement.json`), against the plan before '
         'it. Nominal $B; a positive gap is a shortfall. Project arithmetic on exploratory models, not official scores. '
         'Read with [`../2-settlement.md`](../2-settlement.md).', '',
         '## The booked items ($B; − lowers the gap)', '', '| Item | What | Decided by | FY2040 | FY2045 | FY2056 | FY2030-39 |',
         '| --- | --- | --- | --- | --- | --- | --- |']
    for i in r['items']:
        L.append('| %s | %s | %s | %.1f | %.1f | %.1f | %.1f |' % i)
    L += ['', 'The switches (no path of their own): the $300 credit ended, the 2 points ended, the education fund at 1.65 points, '
          'the HI grant ended, the $100B delivery line removed. The duty to house\'s HOU-1 component is removed in the ledger.', '',
          '## The general-fund gap', '', '| | ' + ' | '.join('FY%d' % y for y in yrs) + ' | FY2030-39 |',
          '| --- |' + ' --- |' * (len(yrs) + 1),
          '| Before the settlement | ' + ' | '.join('%.1f' % r['gap_before'][y] for y in yrs) + ' | %.1f |' % r['gap_before_2030_39'],
          '| **Booked** | ' + ' | '.join('**%.1f**' % r['gap'][y] for y in yrs) + ' | **%.1f** |' % r['gap_2030_39'], '',
          '- Health contribution base rate R = %.2f%% from 2035 (one rate; working assumption for the later years, memo G8 open).' % r['rate'],
          '- Every year FY2040-56 closes: worst FY%d, %.1f.' % (r['worst_year'], r['worst']),
          '- The rate each year would need on its own: ' + ', '.join('FY%d %.2f%%' % kv for kv in r['r_needed'].items()) + '.',
          '- Debt, %% of GDP: %s (baseline FY2040 %.1f, FY2056 %.1f; before the settlement %.1f and %.1f).' % (
              ', '.join('FY%d %.1f' % kv for kv in r['debt'].items()), r['baseline_debt'][2040], r['baseline_debt'][2056],
              r['debt_before'][2040], r['debt_before'][2056]),
          '- Social Security: depletion %s, 75-year balance %+.2f%% of payroll. HI (a current-law comparison after 2035): %s. '
          'The education fund: %s, reserve $%.0fB in FY2040.' % (
              r['summary']['ss_depletion'] or 'none', r['summary']['ss_actuarial_balance'], r['summary']['hi_depletion'],
              'depletes ' + str(r['summary']['education_depletion']) if r['summary']['education_depletion'] else 'solvent', r['education_reserve_2040']),
          '', '## The backstop (memos G5, G13): the gap if D2 or the wealth tax fails, and the base-rate points that close it', '',
          '| | FY2040 gap | R points | FY2045 gap | R points | FY2056 gap | R points |', '| --- | --- | --- | --- | --- | --- | --- |']
    for k, v in r['risks'].items():
        L.append('| %s | %.1f | +%.2f | %.1f | +%.2f | %.1f | +%.2f |' % (k, v[2040][0], v[2040][1], v[2045][0], v[2045][1], v[2056][0], v[2056][1]))
    L += ['', 'Without the wealth tax, the loss is HS2 net of the stack cap.', '',
          '## D3 (scenario Q-G; FY2030-39 average, $ a household a year)', '',
          '| | Q1 | Q2 | Q3 | Q4 | Q5 | Top 1% |', '| --- | --- | --- | --- | --- | --- | --- |',
          '| Q-H7 (before the settlement) | ' + ' | '.join('%+d' % r['d3_q_h7'][g] for g in ('Q1', 'Q2', 'Q3', 'Q4', 'Q5', 'T1')) + ' |',
          '| **Q-G (booked)** | ' + ' | '.join('**%+d**' % r['d3'][g] for g in ('Q1', 'Q2', 'Q3', 'Q4', 'Q5', 'T1')) + ' |', '',
          '- Revenue-mix test (top 1%% and corporations; health\'s contributions out), FY2030-39: %d%%.' % r['revenue_mix']]
    if r.get('d3_by_year'):
        L.append('- By year (Q1 / Q2 / Q3 / Q4 / Q5): ' + '; '.join('FY%d %s' % (y, ' / '.join('%+d' % v[g] for g in ('Q1', 'Q2', 'Q3', 'Q4', 'Q5'))) for y, v in r['d3_by_year'].items()) + '.')
    L += ['', '## The take-home test, both ways (FY2040; no VAT)', '',
          '| Base rate R | Workers ahead, health costs only | Workers ahead, everything counted | Below 200% of poverty | 250-400% of poverty | Retirees and others |',
          '| --- | --- | --- | --- | --- | --- |']
    for k, v in r['take_home'].items():
        L.append('| %s | %s%% | %s%% | %s%% | %s%% | %s%% |' % (k, v['workers_no_vat'], v['workers'], v['workers_below_200fpl'], v['workers_250_400fpl'], v['others_b']))
    return '\n'.join(L) + '\n'


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--write', action='store_true')
    ap.add_argument('--solve', action='store_true')
    ap.add_argument('--report', action='store_true')
    a = ap.parse_args()
    ctx = K.Context()
    d = doc()
    if a.report:
        print(markdown(report(ctx, d)))
        return
    if a.solve:
        r, g = solve(ctx, d)
        print('lowest base rate closing FY2040-56: %.2f%%; worst year FY%d at %.1f' % (
            r, max(range(2040, 2057), key=lambda y: g[y]), max(g[y] for y in range(2040, 2057))))
        return
    der = derive(ctx, d)
    for it, o, p in der:
        print('%s %-80s FY2040 %7.1f  FY2056 %7.1f  FY2030-39 %8.1f' % (
            it['id'], it['line'][:80], p[2040], p[2056], sum(p[y] for y in K.m.W)))
    print('D3:', d3_amounts(der))
    if a.write:
        write_paths(der)
        print('wrote settlement-paths.csv')


if __name__ == '__main__':
    main()
