#!/usr/bin/env python3
"""Stage G step 8a: the fiscal path review's debt goals, priced on the conventional score.

Role: prices the three debt goals of `DEC-2026-11-24-15` against the settlement as booked (#480; case `mixed`,
`models/tools/recovery-budget/model.py`), at three readings of the interest rate against growth (r - g), with a
rate-shock stress and the frontier against health's take-home test (`DEC-2026-11-24-12`) and the health contribution's
base rate. Status: stage G step 8a, tier 2 (analysis; books nothing). Writes
`dossiers/foundations/fair-financing/notes/debt-gap-results.md` with `--write`; `test_fiscal_path.py` checks it.

Definitions (the review's own; `4-fiscal-path.md` part 1):
  * Debt is federal debt held by the public, end of fiscal year, % of GDP: the budget model's unified reading, the
    settlement's reading of record (`2-settlement.md` part 6, item 9).
  * Trust funds: CBO's rule (`models/tools/budget/CONVENTIONS.md`): scheduled benefits are paid in full after a trust
    fund is exhausted, so exhaustion moves no outlay; a fund's surplus lowers debt held by the public.
  * "Extra deficit reduction" X is a cut in the primary deficit, $B, beyond the booked plan, on the conventional
    score (no macroeconomic feedback). Its interest saving is rolled at the model's marginal rate (ASM-RATE-MARGINAL,
    half a year of interest on the year's own flow).
  * r - g: the effective interest rate on debt held by the public less nominal GDP growth, averaged over FY2036-56.
    The booked path's own rates are CBO's (February 2026). The other readings shift every rate by a constant from
    FY2030; the shift reaches old debt only as it rolls over (Treasury's maturity structure, ASM-RATE-ROLLOVER,
    `fiscal-model.py` rate_shift_interest), and growth is held at CBO's path.
  * The consolidation's shape (the speed goals): nothing in FY2029-31 (the populist start, `DEC-2026-11-24-18`),
    phased in over FY2032-36, then a constant share of GDP. Goal 1 is also priced year by year (the primary balance
    that holds the debt ratio flat), which is what "stabilize" literally takes.

Project arithmetic on exploratory models, not official scores.

    python3 models/tools/fiscal_path.py            # print the tables
    python3 models/tools/fiscal_path.py --write    # write the results note
"""
import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'models/tools'))
sys.path.insert(0, str(ROOT / 'models/tools/financing-protection'))
import packages as K   # noqa: E402

YEARS = range(2026, 2057)
OUT = ROOT / 'dossiers/foundations/fair-financing/notes/debt-gap-results.md'
RAMP_START, RAMP_YEARS = 2032, 5           # FY2032-36, full from FY2036
WINDOW = range(2036, 2057)                 # the r - g average and goal 1's test years
TARGETS = (-0.5, 0.5, 1.5)                 # r - g readings, points
SHOW = (2033, 2035, 2036, 2038, 2040, 2045, 2050, 2056)
GOALS = (('g1', 'Debt falling as a share of GDP from the mid-2030s (no rise after FY2035)'),
         ('g2', 'Under 100% of GDP by FY2050'),
         ('g3', 'Under 100% of GDP by FY2055'))
QUARTER_POINT_2040 = K.HCU_PER_QUARTER_POINT_2040      # $56B: a quarter point of the base rate R in FY2040, net
R_BOOKED = 3.80


class Booked:
    """The settlement as booked: case `mixed` rows, and the model's rate functions."""

    def __init__(self, case=None):
        self.f, self.b, self.old, self.u = K.m.load()
        c = case or K.m.build_case('mixed', self.f, self.b, self.old, self.u)
        self.case = c
        self.rows = {r['year']: r for r in c['rows']}
        self.gdp = {y: self.rows[y]['gdp_bn'] for y in YEARS}
        self.debt = {y: self.rows[y]['debt_bn'] for y in YEARS}
        self.interest = {y: self.rows[y]['interest_bn'] for y in YEARS}
        self.pb = {y: self.rows[y]['revenue_bn'] - self.rows[y]['primary_outlays_bn'] for y in YEARS}   # + surplus
        self.rollover = self.f.read_rollover()
        self._rate = {}

    def marginal(self, y, shift):
        return self.f.marginal_rate(self.b, y) + shift(y) / 100

    def rate_effect(self, shift_points, start=2030):
        """{year: added interest, $B} on the booked debt when every rate is shift_points higher from `start`."""
        key = (shift_points, start)
        if key not in self._rate:
            if shift_points == 0:
                self._rate[key] = {y: 0.0 for y in YEARS}
            else:
                add = self.f.rate_shift_interest(self.b, lambda y: self.debt[y], shift_points, start, self.rollover)
                self._rate[key] = {y: add.get(y, 0.0) for y in YEARS}
        return self._rate[key]


def step(shift_points, start=2030):
    return lambda y: shift_points if y >= start else 0.0


def simulate(bk, X=None, shift_points=0.0, start=2030, shocks=()):
    """Debt, interest and primary balance by year with extra deficit reduction X ({year: $B}, + lowers the deficit)
    and every rate shift_points higher from `start`; `shocks` adds (points, start) rate shocks on top."""
    X = X or {}
    parts = [(shift_points, start)] + list(shocks)
    added = {y: sum(bk.rate_effect(p, s)[y] for p, s in parts) for y in YEARS}
    shift = lambda y: sum(p for p, s in parts if y >= s)
    out, prev, cum = {}, 0.0, 0.0
    for y in YEARS:
        r = bk.marginal(y, shift)
        x = X.get(y, 0.0)
        ix = r * prev + r * (-x) / 2
        prev += -x + ix
        cum += added[y]
        debt = bk.debt[y] + cum + prev
        interest = bk.interest[y] + added[y] + ix
        out[y] = dict(debt=debt, debt_gdp=100 * debt / bk.gdp[y], interest=interest, interest_saved=-ix,
                      x=x, x_gdp=100 * x / bk.gdp[y], pb=bk.pb[y] + x, pb_gdp=100 * (bk.pb[y] + x) / bk.gdp[y])
    return out


def r_minus_g(bk, sim):
    """FY2036-56 average of the effective rate (interest over last year's debt) less nominal GDP growth, points."""
    v = [100 * sim[y]['interest'] / sim[y - 1]['debt'] - 100 * (bk.gdp[y] / bk.gdp[y - 1] - 1) for y in WINDOW]
    return sum(v) / len(v)


def shift_for(bk, target):
    """The constant rate shift from FY2030 whose FY2036-56 average r - g on the booked path is `target`."""
    lo, hi = -4.0, 4.0
    for _ in range(40):
        mid = (lo + hi) / 2
        if r_minus_g(bk, simulate(bk, shift_points=mid)) < target:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def shape(bk, s, start=None):
    """s % of GDP, phased in over five years from `start` (FY2032: nothing in FY2029-31), then constant."""
    return {y: s / 100 * bk.gdp[y] * K.m.phase(y, start or RAMP_START, RAMP_YEARS) for y in YEARS}


def met(goal, sim):
    if goal == 'g1':
        return all(sim[y]['debt_gdp'] <= sim[y - 1]['debt_gdp'] + 1e-9 for y in WINDOW)
    if goal == 'g2':
        return sim[2050]['debt_gdp'] < 100
    return sim[2055]['debt_gdp'] < 100


def solve_share(bk, goal, shift_points, start=2030, shocks=(), ramp=None):
    """The smallest constant share of GDP (the five-year ramp from `ramp`, FY2032 by default) that meets the goal,
    to 0.001 point."""
    lo, hi = 0.0, 8.0
    if met(goal, simulate(bk, shape(bk, 0.0, ramp), shift_points, start, shocks)):
        return 0.0
    for _ in range(40):
        mid = (lo + hi) / 2
        if met(goal, simulate(bk, shape(bk, mid, ramp), shift_points, start, shocks)):
            hi = mid
        else:
            lo = mid
    return round(hi + 0.0005, 3)


def year_by_year(bk, shift_points, first=2036):
    """Goal 1 at its literal minimum: in each year from `first` the smallest X >= 0 that keeps the debt ratio at or
    below the year before's, given the X already chosen."""
    X = {}
    for y in range(first, 2057):
        sim = simulate(bk, X, shift_points)
        excess = sim[y]['debt'] - sim[y - 1]['debt_gdp'] / 100 * bk.gdp[y]
        if excess > 0:
            r = bk.marginal(y, step(shift_points))
            X[y] = excess / (1 + r / 2)
    return X


def stabilizing_pb(bk, sim, y):
    """The primary balance, % of GDP, that holds the debt ratio at last year's level in year y."""
    r = sim[y]['interest'] / sim[y - 1]['debt']
    g = bk.gdp[y] / bk.gdp[y - 1] - 1
    return 100 * sim[y - 1]['debt'] / bk.gdp[y - 1] * (r - g) / (1 + g)


def decomposition(bk):
    """What the remaining deficit is made of, % of GDP: current law's and the booked plan's."""
    u, b = bk.u, bk.b
    s0, h0 = u.run_ss([]), u.run_hi(False)
    ss = {r['year']: r for r in s0['rows']}; hi = {r['year']: r for r in h0['rows']}
    out = {}
    for y in (2035, 2040, 2045, 2050, 2056):
        r = bk.rows[y]; G = r['gdp_bn'] / 100
        base_def = r['baseline_primary_outlays_bn'] + r['baseline_interest_bn'] - r['baseline_revenue_bn']
        base_pd = r['baseline_primary_outlays_bn'] - r['baseline_revenue_bn']
        ss_gap = (ss[y]['cost'] - ss[y]['income']) / 100 * u.payroll(y) / u.gdp(y) * 100
        hi_gap = (hi[y]['cost'] - hi[y]['income']) / 100 * u.hi_payroll(y) / u.gdp(y) * 100
        out[y] = dict(base_deficit=base_def / G, base_interest=r['baseline_interest_bn'] / G, base_primary=base_pd / G,
                      base_ss=ss_gap, base_hi=hi_gap, base_other=base_pd / G - ss_gap - hi_gap,
                      plan_deficit=r['deficit_gdp'], plan_interest=r['interest_gdp'],
                      plan_primary=-bk.pb[y] / G, plan_gf=r['agenda_gf_primary_bn'] / G,
                      plan_funds=(r['program_primary_bn'] - r['agenda_gf_primary_bn']) / G,
                      base_debt=100 * r['baseline_debt_bn'] / r['gdp_bn'])
    return out


def per_point(ctx):
    """$B a full point of R raises each year: four quarter points, grown on HCU's path (packages.opt_fold_broad_points)."""
    hcu = ctx.line('HCU')
    return {y: 4 * QUARTER_POINT_2040 * hcu[y] / hcu[2040] for y in YEARS}


def take_home_curve(rates=(2.25, 2.5, 2.55, 2.75, 3.0, 3.25, 3.5, 3.8, 4.0, 4.25, 4.5, 4.75, 5.0, 5.5, 6.0, 6.5, 7.0, 7.5, 8.0)):
    import budget_scan as S
    o = S.take_home(list(rates))
    return [(r, o['R = %.2f%%' % r]['workers']) for r in rates]


def interp(curve, r):
    if r <= curve[0][0]:
        return curve[0][1]
    for (r0, w0), (r1, w1) in zip(curve, curve[1:]):
        if r0 <= r <= r1:
            return w0 + (w1 - w0) * (r - r0) / (r1 - r0)
    (r0, w0), (r1, w1) = curve[-2], curve[-1]
    return w1 + (w1 - w0) * (r - r1) / (r1 - r0)


def rate_for(curve, workers):
    for (r0, w0), (r1, w1) in zip(curve, curve[1:]):
        if w1 <= workers <= w0:
            return r0 + (r1 - r0) * (w0 - workers) / (w0 - w1)
    raise ValueError(workers)


def build(take_home=True):
    bk = Booked()
    ctx = K.Context()
    pp = per_point(ctx)
    central = r_minus_g(bk, simulate(bk))
    cases = []
    for t in TARGETS:
        # the central reading is the booked path itself (CBO's rates; r - g about +0.45), so its figures are #480's
        sh = 0.0 if t == TARGETS[1] else shift_for(bk, t)
        base = simulate(bk, shift_points=sh)
        goals = {}
        for g, _ in GOALS:
            s = solve_share(bk, g, sh)
            sim = simulate(bk, shape(bk, s), sh)
            goals[g] = dict(share=s, sim=sim)
        yby = year_by_year(bk, sh)
        goals['g1y'] = dict(share=None, sim=simulate(bk, yby, sh))
        stab = {y: stabilizing_pb(bk, base, y) for y in (2036, 2040, 2045, 2050, 2056)}
        cases.append(dict(target=t, shift=sh, rg=r_minus_g(bk, base), base=base, goals=goals, stab=stab))
    mid = cases[1]
    # The rate shock: +1 and +2 points from FY2035, on the central reading, rolling over as debt matures
    shocks = []
    for pts in (1.0, 2.0):
        row = dict(points=pts, base=simulate(bk, shift_points=mid['shift'], shocks=[(pts, 2035)]), goals={})
        for g, _ in GOALS:
            s0 = mid['goals'][g]['share']
            row['goals'][g] = dict(
                at_central_share=simulate(bk, shape(bk, s0), mid['shift'], shocks=[(pts, 2035)]),
                share=solve_share(bk, g, mid['shift'], shocks=[(pts, 2035)]))
        shocks.append(row)
    # a later start: the ramp over FY2036-40 (the first term carries none of it), central reading
    late = {}
    for g, _ in GOALS[1:]:      # goal 1 forbids any rise after FY2035, so it can't wait for a FY2036 start
        s = solve_share(bk, g, mid['shift'], ramp=2036)
        late[g] = dict(share=s, sim=simulate(bk, shape(bk, s, 2036), mid['shift']))
    curve = take_home_curve() if take_home else None
    return dict(bk=bk, central=central, cases=cases, shocks=shocks, late=late, per_point=pp, curve=curve,
                decomp=decomposition(bk))


# ---------------------------------------------------------------- the note
def f0(v):
    return '{:,.0f}'.format(v).replace('-', '−')


def f1(v):
    return '{:,.1f}'.format(v).replace('-', '−')


def f2(v):
    return '{:.2f}'.format(v).replace('-', '−')


def markdown(d):
    bk, cases, mid = d['bk'], d['cases'], d['cases'][1]
    L = ['# The fiscal path review, part 1: the debt gap (results)', '',
         'Generated by `models/tools/fiscal_path.py --write` after the common rebuild (stage G step 8a). Read with '
         '[`../4-fiscal-path.md`](../4-fiscal-path.md) part 1. The settlement as booked (#480; case `mixed`). Since stage G step 12 (`DEC-2026-11-28-01`) the plan as booked carries G24 B\'s decided sources (the deduction limits, the AGI surtax, the outside fix and the 2.88% VAT from FY2035 with G30\'s rebate) and G17 B\'s PH-3, settlement items S12-S17, so what is shown here is on top of them. Nominal '
         '$B or % of GDP by federal fiscal year. **Conventional score:** no macroeconomic feedback and no "works as '
         'designed" savings. Project arithmetic on exploratory models, not official scores.', '',
         '**Debt** is debt held by the public. **Trust funds** follow CBO\'s rule: scheduled benefits are paid in full '
         'after a fund is exhausted, so exhaustion changes no outlay, and a fund\'s surplus lowers debt held by the '
         'public. **X** is extra primary deficit reduction beyond the booked plan. **r − g** is the effective rate on '
         'the debt less nominal GDP growth, averaged over FY2036-56; the booked path\'s own reading is %s points '
         '(CBO\'s February 2026 rates and growth). The other readings shift every rate from FY2030, reaching old debt '
         'as it rolls over; growth stays on CBO\'s path. **The speed goals\' shape:** nothing in FY2029-31 (the '
         'populist start, `DEC-2026-11-24-18`), phased in over FY2032-36, then a constant share of GDP.' % f2(d['central']), '']
    # the booked path
    L += ['## 1. The booked path', '', '| % of GDP | ' + ' | '.join('FY%d' % y for y in SHOW) + ' |',
          '| --- |' + ' --- |' * len(SHOW)]
    b = mid['base']
    for lab, k in (('Debt', 'debt_gdp'), ('Primary balance (+ surplus)', 'pb_gdp')):
        L.append('| %s | ' % lab + ' | '.join(f1(b[y][k]) if k == 'debt_gdp' else f2(b[y][k]) for y in SHOW) + ' |')
    L.append('| Net interest | ' + ' | '.join(f2(100 * b[y]['interest'] / bk.gdp[y]) for y in SHOW) + ' |')
    L.append('| Baseline (current law) debt | ' + ' | '.join(f1(100 * bk.rows[y]['baseline_debt_bn'] / bk.gdp[y]) for y in SHOW) + ' |')
    L.append('')
    # decomposition
    dc = d['decomp']
    ys = sorted(dc)
    L += ['## 2. What the remaining deficit is made of', '', '| % of GDP | ' + ' | '.join('FY%d' % y for y in ys) + ' |',
          '| --- |' + ' --- |' * len(ys)]
    for lab, k in (('**Current law: deficit**', 'base_deficit'), ('net interest', 'base_interest'),
                   ('primary deficit', 'base_primary'), ('of which Social Security\'s cash shortfall (cost less payroll and benefit-tax income)', 'base_ss'),
                   ('of which Medicare HI\'s cash shortfall', 'base_hi'), ('of which everything else', 'base_other'),
                   ('**The booked plan: deficit**', 'plan_deficit'), ('net interest', 'plan_interest'),
                   ('primary deficit', 'plan_primary'), ('the plan\'s general-fund effect (− lowers the deficit)', 'plan_gf'),
                   ('the plan\'s trust-fund effect (Social Security, HI, education, leave)', 'plan_funds')):
        L.append('| %s | ' % lab + ' | '.join(f2(dc[y][k]) for y in ys) + ' |')
    L.append('')
    # r - g readings and the stabilizing primary balance
    L += ['## 3. The three readings of r − g, and the primary balance that holds debt flat', '',
          '| r − g target | Rate shift from FY2030 | r − g, FY2036-56 | Debt FY2040 | Debt FY2050 | Debt FY2056 | Stabilizing primary balance FY2040 | FY2056 | Booked primary balance FY2040 | FY2056 |',
          '| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |']
    for c in cases:
        b = c['base']
        L.append('| %+.1f | %+.2f | %+.2f | %s | %s | %s | %s | %s | %s | %s |' % (
            c['target'], c['shift'], c['rg'], f1(b[2040]['debt_gdp']), f1(b[2050]['debt_gdp']), f1(b[2056]['debt_gdp']),
            f2(c['stab'][2040]), f2(c['stab'][2056]), f2(b[2040]['pb_gdp']), f2(b[2056]['pb_gdp'])))
    L.append('')
    # the goals
    L += ['## 4. The goals: extra deficit reduction needed (conventional score)', '']
    for c in cases:
        L += ['### r − g %+.1f%s' % (c['target'], ' (the booked path\'s own rates: %s)' % f2(c['rg']) if c['shift'] == 0 else ''), '',
              '| Goal | Share of GDP from FY2036 | | ' + ' | '.join('FY%d' % y for y in SHOW) + ' | Interest saved FY2030-56 | Debt FY2040 | FY2050 | FY2056 | Peak |',
              '| --- | --- | --- |' + ' --- |' * len(SHOW) + ' --- | --- | --- | --- | --- |']
        for g, lab in GOALS + (('g1y', 'Goal 1, year by year (the literal minimum)'),):
            G = c['goals'][g]; s = G['sim']
            share = '—' if G['share'] is None else f2(G['share'])
            peak = max(range(2030, 2057), key=lambda y: s[y]['debt_gdp'])
            saved = sum(s[y]['interest_saved'] for y in range(2030, 2057))
            L.append('| %s | %s | X, $B | ' % (lab, share) + ' | '.join(f0(s[y]['x']) for y in SHOW) +
                     ' | %s | %s | %s | %s | FY%d, %s |' % (f0(saved), f1(s[2040]['debt_gdp']), f1(s[2050]['debt_gdp']),
                                                          f1(s[2056]['debt_gdp']), peak, f1(s[peak]['debt_gdp'])))
            L.append('| | | X, % of GDP | ' + ' | '.join(f2(s[y]['x_gdp']) for y in SHOW) + ' | | | | | |')
            L.append('| | | Interest saved, $B | ' + ' | '.join(f0(s[y]['interest_saved']) for y in SHOW) + ' | | | | | |')
        L.append('')
    # the later start
    L += ['### A later start (central reading): the ramp over FY2036-40, so the first term (FY2029-32) carries none of it', '',
          'Goal 1 can\'t start this late: it allows no rise after FY2035.', '',
          '| Goal | Share of GDP from FY2040 | X FY2036 | FY2038 | FY2040 | FY2045 | FY2050 | FY2056 | Debt FY2040 | FY2050 | FY2056 | Against the FY2032 start: share |',
          '| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |']
    for g, lab in GOALS[1:]:
        G = d['late'][g]; s = G['sim']
        L.append('| %s | %s | ' % (lab, f2(G['share'])) + ' | '.join(f0(s[y]['x']) for y in (2036, 2038, 2040, 2045, 2050, 2056)) +
                 ' | %s | %s | %s | %s |' % (f1(s[2040]['debt_gdp']), f1(s[2050]['debt_gdp']), f1(s[2056]['debt_gdp']), f2(mid['goals'][g]['share'])))
    L.append('')
    # the shock
    L += ['## 5. Stress: a rate shock of +100 to +200 basis points from FY2035 (the reserve-currency tail)', '',
          'On the central reading (r − g %+.1f), every rate up from FY2035, reaching old debt as it rolls over.' % mid['target'], '',
          '| Shock | Booked path: debt FY2040 | FY2050 | FY2056 | Interest FY2056, % of GDP | ' +
          ' | '.join('%s at its central share: debt FY2050 / FY2056 | share needed' % g.upper() for g, _ in GOALS) + ' |',
          '| --- | --- | --- | --- | --- |' + ' --- | --- |' * len(GOALS)]
    for sh in d['shocks']:
        b = sh['base']
        cells = []
        for g, _ in GOALS:
            G = sh['goals'][g]; s = G['at_central_share']
            cells += ['%s / %s' % (f1(s[2050]['debt_gdp']), f1(s[2056]['debt_gdp'])), f2(G['share'])]
        L.append('| +%d bp | %s | %s | %s | %s | %s |' % (100 * sh['points'], f1(b[2040]['debt_gdp']), f1(b[2050]['debt_gdp']),
                                                       f1(b[2056]['debt_gdp']), f2(100 * b[2056]['interest'] / bk.gdp[2056]), ' | '.join(cells)))
    L.append('')
    # frontier
    if d['curve']:
        pp, curve = d['per_point'], d['curve']
        L += ['## 6. The frontier: the take-home test and the health contribution', '',
              'Central reading. A full point of the base rate R raises about $%sB in FY2040 (four quarter points of $%sB, '
              'grown on HCU\'s path) and $%sB in FY2056; beyond 6.5%% the curve is extrapolated in a straight line. The take-home curve is `budget_scan.take_home` (FY2040, no VAT, '
              'workers ahead on health costs, which equals "everything counted" here).' % (f0(pp[2040]), f0(QUARTER_POINT_2040), f0(pp[2056])), '',
              '| Goal | X FY2040 | X FY2056 | If R carried all of it: R in FY2040 | workers ahead | R in FY2056 terms | Other money needed in FY2040 to hold R at 3.80%% (69.0%%) | at 3.25%% (76.2%%) | at the 85%% target (R %s%%) |' % f2(rate_for(curve, 85.0)),
              '| --- | --- | --- | --- | --- | --- | --- | --- | --- |']
        r85 = rate_for(curve, 85.0)
        for g, lab in GOALS:
            s = mid['goals'][g]['sim']
            x40, x56 = s[2040]['x'], s[2056]['x']
            r40 = R_BOOKED + x40 / pp[2040]; r56 = R_BOOKED + x56 / pp[2056]
            L.append('| %s | %s | %s | %s%% | %s%% | %s%% | %s | %s | %s |' % (
                lab, f0(x40), f0(x56), f2(r40), f1(interp(curve, r40)), f2(r56), f0(x40),
                f0(x40 + (R_BOOKED - 3.25) * pp[2040]), f0(x40 + (R_BOOKED - r85) * pp[2040])))
        L += ['', 'The take-home curve (FY2040): ' + '; '.join('R %s%%: %s%%' % (f2(r), f1(w)) for r, w in curve) + '.', '']
    return '\n'.join(L) + '\n'


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--write', action='store_true')
    ap.add_argument('--no-take-home', action='store_true')
    a = ap.parse_args()
    md = markdown(build(take_home=not a.no_take_home))
    if a.write:
        OUT.write_text(md)
        print('wrote', OUT.relative_to(ROOT))
    else:
        print(md)


if __name__ == '__main__':
    main()
