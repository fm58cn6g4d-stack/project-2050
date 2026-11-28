"""Stage G's financing settlement, booked (step 7): derives each booked item's year-by-year path and its D3 rows.

Role: one derivation for the settlement the budget model books. `models/data/inputs/settlement.json` holds the booked
choices (the switches, the health contribution's base rate and the items, each with its DEC- row). This script prices
each item with the same option functions the settlement's screens used (`financing-protection/packages.py` and
`budget_scan.py`), on the plan before the booking (`build_case(..., settlement=False)`), and writes:
  * `models/data/inputs/settlement-paths.csv`: each item's path, FY2026-56, $B (positive raises the general-fund gap),
    which `models/tools/recovery-budget/model.py` books as "Settlement Snn: ..." lines in every case;
  * the settlement's D3 rows in `models/data/inputs/incidence-rows.csv` (the `HCUg`, `HCUwg`, `HCAg`, `HS2g`, `EDUPg`
    and `GXg` rows) and scenario Q-G in `scenarios.json`, which is Q-H7 with them.
Step 12 (`DEC-2026-11-28-01`) adds G24 B's decided sources and G17 B's PH-3 as items S12-S17, priced by
`fiscal_revision.booking()` on the plan without them (`model.without_items`), with their D3 rows (`OUTg`, `DEDg`, `VATg`,
`VATRg`, the rebate on G30's `vat_rebate` key), each row's year profile and the key, written by `--write`
(`write_d3`); `test_decided_revenue.py` checks every decided revenue source is booked.
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
sys.path.insert(0, str(ROOT / 'models/bookings'))
import packages as K      # noqa: E402
import budget_scan as S   # noqa: E402

INPUTS = ROOT / 'models/data/inputs'
YEARS = K.YEARS
COLS = ['id', 'line', 'side', 'dec'] + ['y%d' % y for y in YEARS]


def doc():
    return json.loads((INPUTS / 'settlement.json').read_text())


def option(ctx, item, rate, rate_path=None):
    params = dict(item['params'])
    if params.get('rate') == 'health_contribution_base_rate':
        params['rate'] = rate
    if params.get('rate_path') == 'health_contribution_rate_path':
        params['rate_path'] = doc()['health_contribution_base_rate'].get('path', {}) if rate_path is None else rate_path
    fn = S.OPTIONS.get(item['option']) or REVISION_OPTIONS.get(item['option']) or K.OPTIONS[item['option']]
    return fn(ctx, **params)


# ---------------------------------------------------------------- G24 B and PH-3 (DEC-2026-11-28-01)
# The decided revenue sources of memo G24 B (the deduction limits, the AGI surtax, the outside fix, and the 2.88% VAT
# from FY2035 with G30's rebate) and G17 B's PH-3, priced by fiscal_revision.booking() on the plan without them.
# + raises the gap. D3: each source's FY2030-39 amount on the household model's keys, as fiscal_revision's mature
# years read them (the VAT gross on consumption, the rebate on G30's phased-out adults key, DED and OUT on surtax).
REVISION_D3 = {   # source: (D3 row, side, key, label)
    'OUT': ('OUTg', 'cost', 'surtax', "The SALT-workaround fix (G24 B's outside fix), from FY2037"),
    'DED': ('DEDg', 'cost', 'surtax', 'Limits on itemized deductions beyond C39 (G24 B), from FY2037; the surtax key, a proxy'),
    'VAT': ('VATg', 'cost', 'consumption', 'A broad VAT at 2.88% from FY2035 (G24 B), gross: what households bear'),
    'VATR': ('VATRg', 'benefit', 'vat_rebate', "The VAT's rebate, $150 an adult a point, phased out over $60-80K / $120-160K of AGI (G30)"),
}


assert tuple(v[0] for v in REVISION_D3.values()) == ('OUTg', 'DEDg', 'VATg', 'VATRg')   # fiscal_revision.REVISION_D3_ROWS


def revision_source(ctx, key):
    import fiscal_revision as FR
    p = FR.booking()[key]
    sign = 1 if key in ('VATR',) else -1   # the rebate is an outlay; the others raise revenue or cut outlays
    path = {y: sign * p.get(y, 0.0) for y in YEARS}
    d3 = []
    if key in REVISION_D3:
        rid, side, k, label = REVISION_D3[key]
        amt = sum(p.get(y, 0.0) for y in K.m.W) / 1000 * (FR.VAT_GROSS if key == 'VAT' else 1.0)
        d3.append(('add', rid, side, amt, k, label))
    return dict(label=key, adjust={key: path}, d3=d3)


REVISION_OPTIONS = {'revision_source': revision_source}


def derive(ctx, d=None, rate=None, rate_path=None):
    """[(item, option result, path)] for every booked item; the path is the option's one adjustment, FY2026-56.
    A screen at a single `rate` (rate given, rate_path None) holds that rate in every year from 2035."""
    d = d or doc()
    if rate is not None and rate_path is None:
        rate_path = {}
    rate = d['health_contribution_base_rate']['rate'] if rate is None else rate
    if rate_path is None:
        rate_path = d['health_contribution_base_rate'].get('path', {})
    out = []
    for it in d['items']:
        o = option(ctx, it, rate, rate_path)
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


def screened_case(ctx, d, rate, rate_path=None):
    """The same package priced the screens' way on the pre-settlement base, as a check on the booking."""
    opts = [o for it, o, p in derive(ctx, d, rate, rate_path)]
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


# ---------------------------------------------------------------- the health fund's rate rule (G27 A)
def rate_rule(ctx, d=None):
    """The base rate from FY2041 under the health fund's own rule (G27 A, DEC-2026-11-25-31), on the booked case.

    The contribution pays a fixed share s of the fund's cost from FY2040: its FY2040 yield at 3.80% over the fund's
    spending that year (G26 A, DEC-2026-11-25-30: the 3.80% re-founded as that share). The general fund pays the rest
    (the law's share, recovery-budget/model.py's health_fund()), so the fund's reserve moves only by the contribution's
    yield less s x its cost. Each year from FY2041 the trustees project the reserve one year ahead at the current rate;
    if it would leave the band (15-25%) the rate steps a quarter point, at most once a year, never below 3.25%. No
    yearly reset. Decided (G27.1a A, DEC-2026-11-26-01): the band is read on the contribution's own share of the
    fund's cost and tested one year ahead (part 8 of 2-settlement.md shows the other readings). The reserve starts at FY2039's (the $250B standing reserve). Interest on the reserve is not modeled.
    Returns dict(share, path {year: rate}, reserve {year: $B}, needed {year: the smooth share's rate})."""
    d = d or doc()
    hf, hr = d['health_fund'], d['health_contribution_base_rate']
    case = booked_case(ctx)
    fund = case['health_fund']
    L = K.m.audit_lines(case['audit'])
    hcu = ctx.line('HCU')
    pp = {y: S.PER_POINT_2040 * hcu[y] / hcu[2040] for y in YEARS}
    booked = {y: hr.get('path', {}).get(str(y), hr['rate']) for y in YEARS}
    # the contribution's yield at the base rate held at 3.80%, with the booked path's own steps taken out
    c0 = {y: -sum(L.get(n, {}).get(y, 0.0) for n in hf['contribution']) - (booked[y] - hr['rate']) * pp[y] for y in YEARS}
    y0 = hf['share_from']
    share = c0[y0] / fund[y0]['spending']
    lo, hi = hf['band']
    rate, res = hr['rate'], fund[y0 - 1]['reserve']
    path, reserve, needed = {}, {}, {}
    for y in range(y0, 2057):
        target = share * fund[y]['spending']
        if y > y0:
            proj = res + c0[y] + (rate - hr['rate']) * pp[y] - target
            if proj < lo * target:
                rate = rate + hf['step']
            elif proj > hi * target and rate - hf['step'] >= hf['floor'] - 1e-9:
                rate = rate - hf['step']
            path[y] = round(rate, 2)
        res += c0[y] + (rate - hr['rate']) * pp[y] - target
        reserve[y] = res
        needed[y] = hr['rate'] + (target - c0[y]) / pp[y]
    return dict(share=share, path=path, reserve=reserve, needed=needed)


def write_ss_part(ctx):
    """funds-ss-hx.csv: HX-SS (G29 A), the OASDI part of HX and HEX from FY2031 (HX's first year), % of the funds model's taxable payroll,
    negative (a gain to the funds), from the booked case (recovery-budget/model.py social_security_part())."""
    case = booked_case(ctx)
    ssp = K.m.social_security_part(case['audit'], doc()['health_fund'])
    rows = ['year,hx_ss_pct_payroll,basis']
    for i, y in enumerate(sorted(ssp)):
        note = ('"G29 A (DEC-2026-11-26-03): recovery-budget/model.py social_security_part() on the booked case ($B) over '
                'funds-model.py payroll(); settlement_booking.py --write"') if i == 0 else ''
        rows.append('%d,%.4f,%s' % (y, -100 * ssp[y] / ctx.u.payroll(y), note))
    (INPUTS / 'funds-ss-hx.csv').write_text('\n'.join(rows) + '\n')


def write_rule(rule):
    """settlement.json's health fund share and the rate path, written in place (the file's other text unchanged)."""
    import re
    fn = INPUTS / 'settlement.json'
    t = fn.read_text()
    path = '{' + ', '.join('"%d": %.2f' % (y, v) for y, v in sorted(rule['path'].items())) + '}'
    t = re.sub(r'"path": \{[^}]*\}', '"path": ' + path, t, count=1)
    t = re.sub(r'"contribution_share": [0-9.]+', '"contribution_share": %.6f' % rule['share'], t, count=1)
    json.loads(t)
    fn.write_text(t)


# ---------------------------------------------------------------- D3
D3_ROWS = {   # new row id: (Q-H7 row it replaces, or None for a row added beside the package's rows)
    'HCUg': 'HCU', 'HCUwg': 'HCUw', 'HCAg': 'HCA', 'HS2g': 'HS2', 'EDUPg': 'EDUP', 'GXg': None,
    'OUTg': None, 'DEDg': None, 'VATg': None, 'VATRg': None}   # G24 B's sources in FY2030-39 (DEC-2026-11-28-01)


def revision_d3(derived):
    """G24 B's D3 rows: {row id: (side, $T over FY2030-39, key, label, {year: $B}, the source's id)}."""
    out = {}
    for it, o, p in derived:
        for e in o.get('d3', []):
            if e[0] == 'add':
                _, rid, side, amt, key, label = e
                out[rid] = (side, round(amt, 4), key, label, {y: abs(p[y]) for y in K.m.W}, o['label'])
    return out


def rebate_key(hh=None):
    """The VAT rebate's D3 key under G30: the measured adults key times the share of each fifth's adults who keep the
    rebate (fiscal_revision.rebate_kept), renormalized; the top 1% are above every limit. (q1..q5, top1), %."""
    import fiscal_revision as FR
    hh = hh or K.Household()
    sh, _ = hh.D.K['adults']
    k = FR.rebate_kept()
    w = [s * k['Q%d' % (i + 1)] for i, s in enumerate(sh)]
    out = [round(100 * v / sum(w), 4) for v in w[:4]]
    return out + [round(100 - sum(out), 4)], 0.0   # sums to 100 exactly (provisions.dist checks it)


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
    out = {r: round(v, 4) for r, v in out.items()}
    out.update({rid: v[1] for rid, v in revision_d3(derived).items()})
    return out


def _csv_line(vals):
    import io
    s = io.StringIO()
    csv.writer(s, lineterminator='\n').writerow(vals)
    return s.getvalue()


def _put_line(fn, rid, line, col=0):
    """Replace the line whose field `col` is rid, or append it; the file's other lines unchanged."""
    lines = fn.read_text().splitlines(keepends=True)
    for i, l in enumerate(lines):
        if next(csv.reader([l]))[col:col + 1] == [rid]:
            lines[i] = line
            break
    else:
        lines.append(line)
    fn.write_text(''.join(lines))


def write_d3(derived):
    """G24 B's D3 inputs: its rows in incidence-rows.csv, their year profiles in incidence-phase-in.csv (each row's own
    FY2030-39 path), the rebate's key in incidence-keys.csv, and the rows in scenario Q-G."""
    rev = revision_d3(derived)
    for rid, (side, amt, key, label, path, src) in rev.items():
        basis = ('stage G step 12, DEC-2026-11-28-01: settlement_booking.py revision_d3(), fiscal_revision.booking()\'s %s '
                 'over FY2030-39%s; scenario Q-G' % (src, ', gross of the income and payroll offset (what households bear)' if rid == 'VATg' else ''))
        _put_line(INPUTS / 'incidence-rows.csv', rid, _csv_line(['option', rid, label, side, '%.4f' % amt, key, '', basis]), col=1)
        lv = [path[y] for y in K.m.W]
        top = max(lv) or 1.0
        _put_line(INPUTS / 'incidence-phase-in.csv', rid, _csv_line(
            [rid, 'norm', ''] + ['%.4g' % (v / top) for v in lv] + ['stage G step 12: the source\'s booked FY2030-39 path (settlement_booking.py write_d3)']))
    sh, t1 = rebate_key()
    _put_line(INPUTS / 'incidence-keys.csv', 'vat_rebate', _csv_line(
        ['vat_rebate'] + ['%.4f' % s for s in sh] + ['%g' % t1, "G24 B's VAT rebate under G30's phase-out (DEC-2026-11-26-04): the measured adults key times the share of each fifth's adults who keep the rebate (fiscal_revision.rebate_kept()), renormalized; none in the top 1% (settlement_booking.py rebate_key())"]))
    fn = INPUTS / 'scenarios.json'
    s = json.loads(fn.read_text())
    q = next(x for x in s['incidence'] if x['id'] == 'Q-G')
    for rid in rev:
        if rid not in q['options']:
            q['options'].append(rid)
    fn.write_text(json.dumps(s, indent=1, ensure_ascii=False) + '\n')


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


def risk_rows(ctx, d, booked):
    """The settlement's other risks, one at a time on the booked case (screen.py's rows, without the VAT's): the gap
    in FY2040, FY2045 and FY2056 ($B) and the base-rate points that would cover FY2040."""
    lines = {}
    for a in booked['audit']:
        lines.setdefault(a['line'], {y: 0.0 for y in YEARS})[a['year']] += a['primary_deficit_change_bn']
    L = lambda k: lines.get(k, {y: 0.0 for y in YEARS})
    top = ['G1', 'G3', 'G9', 'C18', 'C43', 'H1b', 'GX']
    wage = {y: sum(L(r)[y] for r in top) for y in YEARS}
    k_stack = 140.0 / -wage[2040]
    old = {y: sum(L(r)[y] for r in ('G1', 'G3', 'G5', 'G6', 'G7', 'G10', 'G11', 'H1a', 'H1b', 'C18', 'C38',
                                     'New indexed income contributions')) for y in YEARS}
    item = {it['option']: p for it, o, p in derive(ctx, d)}
    hs2 = ctx.line('HS2')
    hcu = ctx.line('HCU')
    per_point = lambda y: S.PER_POINT_2040 * hcu[y] / hcu[2040]
    rows = [
        ('The wage stack yields at the working elasticity (0.25)', 'stack note part 3: about $140B in FY2040 (rough, unverified)',
         {y: -k_stack * wage[y] for y in YEARS}),
        ('Pre-2025-law scores come in 10% low', '1-audit.md item 22', {y: -0.10 * old[y] for y in YEARS}),
        ('Joint yield risk: both of the above', 'review F-2, without the VAT row', {y: -k_stack * wage[y] - 0.10 * old[y] for y in YEARS}),
        ('The avoidance allowance stays at 20% on the base rate', '1-audit.md item 9: the range is 10-25%',
         {y: -item['avoidance_by_tier'][y] for y in YEARS}),
        ('The stack cap at its high end ($55B)', 'stack note part 4', {y: 15.0 * hs2[y] / hs2[2040] for y in YEARS}),
        ('C3A, the clean electricity compliance payments, vanish', '1-audit.md item 43', {y: -L('C3A')[y] for y in YEARS}),
    ]
    out = []
    for label, basis, path in rows:
        g = gap(K.m.build_case('risk', ctx.f, ctx.b, ctx.old, ctx.u,
                               spending_adjustments={'risk': {'annual_bn': {str(y): v for y, v in path.items()}}}))
        out.append((label, basis, round(g[2040], 1), round(g[2045], 1), round(g[2056], 1), round(max(g[2040], 0) / per_point(2040), 2)))
    # the HI grant kept: a scorer counting the fold-in's HI shortfall as new (2-settlement.md part 6)
    sw = dict(d['switches'])
    pts = K.m.A['hi']['gf_support_payroll_points']
    orig = K.m.SETTLEMENT['switches']['hi_grant_payroll_points']
    K.m.SETTLEMENT['switches']['hi_grant_payroll_points'] = pts
    try:
        g = gap(K.m.build_case('risk', ctx.f, ctx.b, ctx.old, ctx.u))
    finally:
        K.m.SETTLEMENT['switches']['hi_grant_payroll_points'] = orig
    out.append(("If a scorer counted the fold-in's HI shortfall as new", "the grant's size; the correction stands (F-1)",
                round(g[2040], 1), round(g[2045], 1), round(g[2056], 1), round(max(g[2040], 0) / per_point(2040), 2)))
    return out


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
               path={y: d['health_contribution_base_rate'].get('path', {}).get(str(y), d['health_contribution_base_rate']['rate'])
                     for y in range(2040, 2057)},
               fund={y: (round(c['health_fund'][y]['transfer'], 1), round(c['health_fund'][y]['reserve'], 1))
                     for y in (2030, 2034, 2035, 2039, 2040, 2045, 2050, 2056)},
               r_needed={y: round(out_r, 2) for y, out_r in
                         ((y, d['health_contribution_base_rate'].get('path', {}).get(str(y), d['health_contribution_base_rate']['rate'])
                           + g[y] / per_point(y)) for y in (2040, 2042, 2045, 2050, 2056))})
    risks = {}
    for name, w in (('without D2', ('D2',)), ('without HS2', ('HS2',)), ('without both', ('D2', 'HS2'))):
        r = gap(risk_case(ctx, d, w))
        risks[name] = {y: (round(r[y], 1), round(max(r[y], 0) / per_point(y), 2)) for y in (2040, 2045, 2056)}
    out['risks'] = risks
    out['risk_rows'] = risk_rows(ctx, d, c)
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
    out['take_home'] = S.take_home(sorted({3.25, out['rate'], 4.45} | set(out['path'].values())))
    # with G24 B's booked sources counted (DEC-2026-11-28-01): fiscal_revision's test, FY2040, at the booked base rate
    import fiscal_revision as FR
    bkp = FR.booking()
    top = sum(bkp[k][2040] for k in FR.BOOKED_MIX)
    th = FR.TakeHome(FR.Mature())
    out['take_home_g24b'] = dict(R=out['rate'], vat=FR.VAT_RATE, top=round(top, 1), **th.run(out['rate'], FR.VAT_RATE, top),
                                 before=th.run(out['rate']))
    return out


def markdown(r):
    yrs = (2030, 2033, 2035, 2036, 2037, 2038, 2039, 2040, 2041, 2042, 2045, 2050, 2056)
    L = ['# The financing settlement as booked: results', '',
         'Generated by `models/bookings/settlement_booking.py --report` after the common rebuild (stage G step 7; regenerated in steps 11 and 12, the last with G24 B and PH-3 booked, `DEC-2026-11-28-01`). The budget '
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
          '- Health contribution base rate R = %.2f%% from 2035, re-founded as the health fund\'s rate (G26 A); from FY2041 the fund\'s own rule (G27 A; the band on the contribution\'s own share, tested one year ahead, G27.1a A, `DEC-2026-11-26-01`): %s.' % (
              r['rate'], ', '.join('FY%d %.2f%%' % (y, v) for y, v in r['path'].items() if y == 2040 or v != r['path'][y - 1])),
          '- The health fund as its own account (`DEC-2026-11-25-28`, `-31`): the general fund\'s transfer to the fund / the fund\'s reserve ($B): ' + ', '.join(
              'FY%d %.1f / %.1f' % (y, t, v) for y, (t, v) in r['fund'].items()) + '. The general fund\'s gap counts only the transfer; FY2030-34\'s surplus stays in the fund.',
          ('- Every year FY2040-56 closes: worst FY%d, %.1f.' % (r['worst_year'], r['worst']) if r['worst'] <= 0.05 else
           '- Short in FY2040-56 (+ short; G29 A sends the Social Security part to Social Security from the start, memo G29\'s question G29.1): '
           + ', '.join('FY%d %.1f' % (y, r['gap'][y]) for y in range(2040, 2057) if r['gap'][y] > 0.05)
           + '; worst FY%d, %.1f.' % (r['worst_year'], r['worst'])),
          '- A general-fund reading only, not a rate under `DEC-2026-11-25-12`: the base rate at which the general fund would just close each year: ' + ', '.join('FY%d %.2f%%' % kv for kv in r['r_needed'].items()) + '.',
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
          '## The other risks, one at a time on the booked package', '',
          '| Risk | Basis | FY2040 | FY2045 | FY2056 | Base-rate points to cover FY2040 |', '| --- | --- | --- | --- | --- | --- |']
    for row in r['risk_rows']:
        L.append('| %s | %s | %.1f | %.1f | %.1f | +%.2f |' % row)
    L += ['',
          '## D3 (scenario Q-G; FY2030-39 average, $ a household a year)', '',
          '| | Q1 | Q2 | Q3 | Q4 | Q5 | Top 1% |', '| --- | --- | --- | --- | --- | --- | --- |',
          '| Q-H7 (before the settlement) | ' + ' | '.join('%+d' % r['d3_q_h7'][g] for g in ('Q1', 'Q2', 'Q3', 'Q4', 'Q5', 'T1')) + ' |',
          '| **Q-G (booked)** | ' + ' | '.join('**%+d**' % r['d3'][g] for g in ('Q1', 'Q2', 'Q3', 'Q4', 'Q5', 'T1')) + ' |', '',
          '- Revenue-mix test (top 1%% and corporations; health\'s contributions out), FY2030-39: %d%%.' % r['revenue_mix']]
    if r.get('d3_by_year'):
        L.append('- By year (Q1 / Q2 / Q3 / Q4 / Q5): ' + '; '.join('FY%d %s' % (y, ' / '.join('%+d' % v[g] for g in ('Q1', 'Q2', 'Q3', 'Q4', 'Q5'))) for y, v in r['d3_by_year'].items()) + '.')
    g = r['take_home_g24b']
    L += ['', '## The take-home test with G24 B counted (FY2040)', '',
          'Workers whose visible health costs plus the new sources they pay fall under the plan (`fiscal_revision.TakeHome`, '
          'health\'s test with everything counted): the base rate at %.2f%%, the VAT at %.2f%% less its rebate under G30, and the '
          'deduction limits, AGI surtax and outside fix ($%.1fB in FY2040) on AGI above $100K/$200K. The method reads a VAT about '
          '2 points low (revision-results.md part 5).' % (g['R'], g['vat'], g['top']), '',
          '| | Workers ahead | Below 200% of poverty |', '| --- | --- | --- |',
          '| Before G24 B (R %.2f%%, nothing new) | %.1f%% | %.1f%% |' % (g['R'], g['before']['workers'], g['before']['below_200fpl']),
          '| **G24 B booked** | **%.1f%%** | **%.1f%%** |' % (g['workers'], g['below_200fpl'])]
    L += ['', '## The take-home test, both ways, before G24 B (FY2040; no VAT; budget_scan.take_home)', '',
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
    rule = rate_rule(ctx, d)
    print('health fund: contribution share %.4f; rate path %s' % (rule['share'], rule['path']))
    if a.write:
        write_rule(rule)
        write_ss_part(ctx)
        d = doc()
        der = derive(ctx, d)
        write_paths(der)
        write_d3(der)
        print('wrote settlement.json (the health fund\'s share and rate path), funds-ss-hx.csv and settlement-paths.csv; '
              'rerun after the next rebuild: the rule reads the booked case')


if __name__ == '__main__':
    main()
