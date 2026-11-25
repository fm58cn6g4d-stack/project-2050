#!/usr/bin/env python3
"""Stage G step 9: the fiscal path revision for Espen's batch 3 answers (`DEC-2026-11-25-01` to `-11`).

Role: prices batch 4's forks. (1) Memo G23, the debt goal redrafted "a little more aggressive" (`-01`): four debt
paths on the conventional score, each with its deficit reduction by year, interest saved, debt in FY2040, FY2050 and
FY2056, the r - g readings and the rate shocks of step 8a. (2) Memo G24, G19's mix re-checked with a VAT allowed after
the first years: each mix's revenue, D3 by fifth in FY2040 and FY2050 (`DEC-2026-11-25-08`), the take-home test
(target 85-90%, `DEC-2026-11-15-10`) and when it reaches the middle class. Status: stage G step 9, tier 2; books
nothing. Writes `dossiers/foundations/fair-financing/notes/revision-results.md` with `--write`; `test_fiscal_revision.py`
checks it.

The base (`base()`): the settlement as booked (#480; case `mixed`) with three things the batch decided or found:
  * CLI-1's tail on the decided step-down (`cli1_tail.py`; a what-if until its tier-3 input row lands, then the booked
    case itself, so nothing is counted twice; "as booked" below is the old profile either way);
  * G17 B's hold of the clean-energy credits in FY2038-39 (PH-3, `fiscal_frontier.phasing`; `DEC-2026-11-25-03`);
  * G16 B and G18 D′ change nothing up front (triggers), and G20 B's rule measures, it doesn't raise.

Sources (`SOURCES`): FY2040 levels, $B, net of the income and payroll offset, grown with GDP and phased in from a
start year. Re-scored here on the post-2025 law (P.L. 119-21), the agent's arithmetic, not CBO's or JCT's:
  * DED, limits on itemized deductions beyond C39: CBO's December 2024 option 49 (123-312 scaled to FY2040) was priced
    on a baseline in which the 2017 law's individual provisions expired after 2025. P.L. 119-21 made them permanent
    (the larger standard deduction, the limited SALT deduction, a cap on the value of itemized deductions at the top),
    which leaves fewer itemizers and a smaller base: about 0.45 of the old yield (range 0.35-0.55) -> 95 (55-140).
  * CARB, a larger carbon fee (buildings and non-road transport, which the booked fee leaves out): about $85B gross in
    FY2040 on the energy model's economy-wide read (`dossiers/clean-power/6-cost.md` part 1: buildings and non-road
    $0.74T over 2030-39 [EV-CLP-714]). With the plan's 80% dividend and the 24.4% offset it raises nothing net; with a
    dividend that holds the bottom two fifths harmless (about 40%) about 30. Central 15 (0-30). Step 8b's 111-147 is
    CBO's economy-wide option 73 with no dividend netted and with the sectors the plan already prices.
  * SUR, an AGI surtax of 2 points above $100K/$200K: CBO option 46's upper alternative, about 225 in FY2040. AGI's
    base barely moves with P.L. 119-21; less the plan's avoidance allowance on the top rows (15%) -> 190 (160-215).
  * OUT, CRFB's SALT-workaround fix (step 8b's outside screen, to confirm against C39): 28, from FY2037.
  * VAT, a broad value-added tax: $90.3B a point in FY2040 net (`packages.VAT_POINT_2040`: CBO's broad base less the
    care the plan pays for), households bearing net / 0.75. **With a rebate of $150 a point for every adult** (2040
    dollars, indexed 2.3% a year): the VAT on the first $15,000 of each adult's spending, paid with the child benefit,
    Social Security or a refundable credit through systems that exist. It costs about $40B a point, so the VAT nets about
    $50B a point. P.L. 119-21 doesn't touch its base.
  * R, the health contribution's base rate above 3.80%: about $224B a point in FY2040 (`fiscal_path.per_point`).

D3 in FY2040 and FY2050 (`d3_mature`): the household model runs to FY2039. A mature year is read as the booked FY2039
position (scenario Q-G, `d3.D3.series`) carried forward with nominal income per household, less each new source's
incidence that year on the household model's keys (VAT gross on `consumption`, the rebate on `adults`; SUR, DED and OUT
on `surtax`, AGI above $100K/$200K, a proxy for DED; CARB on `energy`; R on `health_contrib`). Approximate; a full
mature-year run of the household model is a later model step.

The take-home test (`take_home_mix`): health's test in FY2040 (`take_home_vat.py`'s method), everything counted: each
worker's visible health costs at R, plus the new sources a unit pays: VAT by its fifth, less its rebate (adults in the
unit); SUR, DED and OUT by its AGI above $100K/$200K, scaled to each source's revenue; CARB by its fifth.

Project arithmetic on exploratory models, not official scores.

    python3 models/tools/fiscal_revision.py            # print
    python3 models/tools/fiscal_revision.py --write    # write the results note
"""
import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path[:0] = [str(ROOT / 'models/tools'), str(ROOT / 'models/tools/financing-protection')]
import fiscal_path as FP      # noqa: E402
import fiscal_frontier as FF  # noqa: E402
import cli1_tail as CT        # noqa: E402

K = FP.K
OUT = ROOT / 'dossiers/foundations/fair-financing/notes/revision-results.md'
YEARS = FP.YEARS
SHOW = (2035, 2037, 2039, 2040, 2045, 2050, 2056)
REBATE_PER_POINT_2040 = 150.0            # $ an adult a VAT point, 2040 dollars
REBATE_CPI = 0.023
VAT_GROSS = 1 / (1 - K.EXCISE_OFFSET)
SUR_THRESH = {'single': 100_000, 'joint': 200_000}
COEF_BP = (2.0, 3.0)                     # CBO working paper 2019-01: basis points per point of debt [EV-FIN-076]

# id: (label, FY2040 central $B, low, high, start, ramp, household key)
SOURCES = {
    'OUT': ('CRFB\'s SALT-workaround fix (outside screen)', 28.0, 20.0, 28.0, 2037, 1, 'surtax'),
    'DED': ('Limits on itemized deductions beyond C39', 95.0, 55.0, 140.0, 2037, 1, 'surtax'),
    'CARB': ('A larger carbon fee (buildings, non-road), dividend kept for the bottom two fifths', 15.0, 0.0, 30.0, 2037, 1, 'energy'),
    'SUR': ('An AGI surtax, 2 points above $100K/$200K', 190.0, 160.0, 215.0, 2040, 1, 'surtax'),
    'R50': ('The health contribution half a point above 3.80% (to 4.30%)', 112.0, 112.0, 112.0, 2040, 1, 'health_contrib'),
}
G19B = ('OUT', 'DED', 'CARB', 'SUR')
STEP8B = {'OUT': (28, 28), 'DED': (123, 312), 'CARB': (111, 147), 'SUR': (167, 225), 'R50': (112, 112)}

# G23: the redrafted debt goal. id: (label, test, ramp start). Every share is phased in over five years from the start.
GOALS = (
    ('A', 'Held flat from FY2040 (G15 B as decided, restated)', 'flat', 2035),
    ('B', 'Falling to 110% of GDP by FY2056', ('end', 2056, 110.0), 2035),
    ('C', 'Falling to 100% of GDP by FY2056', ('end', 2056, 100.0), 2035),
    ('D', 'Under 100% of GDP by FY2050', ('end', 2050, 100.0), 2033),
)

# G24: the financing mixes. Fixed sources, then the plug that closes the goal (a constant rate from its start).
MIXES = (
    ('1', 'G19 B as decided (re-scored), the health contribution last', ('OUT', 'DED', 'CARB', 'SUR'), ('R', 2040)),
    ('2', 'G19 B\'s deduction limits and surtax, then a rebated VAT from FY2035', ('OUT', 'DED', 'SUR'), ('VAT', 2035)),
    ('3', 'A rebated VAT from FY2035 alone (with the outside fix)', ('OUT',), ('VAT', 2035)),
    ('4', 'As 2, the VAT from FY2037', ('OUT', 'DED', 'SUR'), ('VAT', 2037)),
    ('5', 'As 2, the VAT from FY2033', ('OUT', 'DED', 'SUR'), ('VAT', 2033)),
    ('6', 'As 2, with the health contribution half a point higher from FY2040 (4.30%)', ('OUT', 'DED', 'SUR', 'R50'), ('VAT', 2035)),
)


# ---------------------------------------------------------------- the base
def base():
    f, b, old, u = K.m.load()
    c0, c1, p0, p1 = CT.what_if(f, b, old, u)
    booked = FP.Booked(case=c0)
    bk = FP.Booked(case=c1)
    ph3 = FF.phasing(booked)['PH-3']
    return dict(booked=booked, bk=bk, ph3=ph3, cli1_saving={y: p0[y] - p1[y] for y in YEARS},
                cli1_booked=CT.is_booked(f, b, old))


def path(bk, level, start, ramp=1):
    return {y: level * bk.gdp[y] / bk.gdp[2040] * K.m.phase(y, start, ramp) for y in YEARS}


def adults(y):
    c = K.m.A['recovery_credit']
    return c['population_m_2030'] * c['adult_share'] * (1 + c['population_growth']) ** (y - 2030)   # millions


def vat_point(bk, y, rebate=True):
    """Net $B a VAT point raises in year y, and the rebate's cost."""
    net = K.VAT_POINT_2040 * bk.gdp[y] / bk.gdp[2040]
    reb = REBATE_PER_POINT_2040 * (1 + REBATE_CPI) ** (y - 2040) * adults(y) / 1000 if rebate else 0.0
    return net - reb, reb


def source_paths(bk, ids, level='central'):
    i = {'central': 1, 'low': 2, 'high': 3}[level]
    return {k: path(bk, SOURCES[k][i], SOURCES[k][4], SOURCES[k][5]) for k in ids}


def plug_path(bk, kind, start, rate, pp):
    """$B by year of a plug at `rate` points from `start` (two-year ramp for a VAT; one for R)."""
    if kind == 'VAT':
        return {y: rate * vat_point(bk, y)[0] * K.m.phase(y, start, 2) for y in YEARS}
    return {y: rate * pp[y] * K.m.phase(y, start, 1) for y in YEARS}


# ---------------------------------------------------------------- the goals
def met(goal, sim):
    no_rise = all(sim[y]['debt_gdp'] <= sim[y - 1]['debt_gdp'] + 1e-9 for y in range(2041, 2057))
    if goal == 'flat':
        return no_rise
    _, year, level = goal
    return no_rise and sim[year]['debt_gdp'] <= level


def add(*paths):
    return {y: sum(p.get(y, 0.0) for p in paths) for y in YEARS}


def solve(bk, goal, fixed, shape, shift=0.0, shocks=()):
    """The smallest multiplier t >= 0 of `shape(t)` ({year: $B}) that, on top of `fixed`, meets the goal."""
    ok = lambda t: met(goal, FP.simulate(bk, add(fixed, shape(t)), shift, shocks=shocks))
    if ok(0.0):
        return 0.0
    lo, hi = 0.0, 1.0
    while not ok(hi):
        hi *= 2
        if hi > 64:
            return None
    for _ in range(40):
        mid = (lo + hi) / 2
        lo, hi = (lo, mid) if ok(mid) else (mid, hi)
    return hi


def goal_share(bk, goal, start, fixed, shift=0.0, shocks=()):
    s = solve(bk, goal, fixed, lambda t: FP.shape(bk, t, start), shift, shocks)
    return None if s is None else round(s + 0.0005, 3)


def r_minus_g_end(bk, sim, years=range(2050, 2057)):
    v = [100 * sim[y]['interest'] / sim[y - 1]['debt'] - 100 * (bk.gdp[y] / bk.gdp[y - 1] - 1) for y in years]
    return sum(v) / len(v)


def goals(B):
    bk, ph3 = B['bk'], B['ph3']
    # G19 B's FY2037-39 steps are decided (DEC-2026-11-25-05): the level "held flat" is measured after them
    early = add(*source_paths(bk, ('OUT', 'DED', 'CARB')).values())
    early = {y: v if y <= 2039 else 0.0 for y, v in early.items()}
    shift_lo, shift_hi = FP.shift_for(bk, -0.5), FP.shift_for(bk, 1.5)
    base_sim = FP.simulate(bk, ph3)
    out = {}
    for gid, label, goal, start in GOALS:
        fixed = add(ph3, early) if gid == 'A' else ph3
        if gid == 'A':
            # the literal minimum after FY2039: each year just enough to hold the ratio (fiscal_path.year_by_year)
            X = dict(fixed)
            for y in range(2040, 2057):
                sim = FP.simulate(bk, X)
                excess = sim[y]['debt'] - sim[y - 1]['debt_gdp'] / 100 * bk.gdp[y]
                if excess > 0:
                    X[y] = X.get(y, 0.0) + excess / (1 + bk.marginal(y, FP.step(0.0)) / 2)
            share = None
        else:
            share = goal_share(bk, goal, start, fixed)
            X = add(fixed, FP.shape(bk, share, start))
        sim = FP.simulate(bk, X)
        new = {y: X[y] - ph3.get(y, 0.0) for y in YEARS}          # the goal's own money, PH-3 netted out
        row = dict(label=label, goal=goal, start=start, share=share, X=X, new=new, sim=sim,
                   saved=sum(sim[y]['interest_saved'] for y in range(2030, 2057)),
                   rg_end=r_minus_g_end(bk, sim), rg_base_end=r_minus_g_end(bk, base_sim),
                   lower_debt=sum(base_sim[y]['debt_gdp'] - sim[y]['debt_gdp'] for y in range(2050, 2057)) / 7)
        if share is not None:
            row['readings'] = {t: goal_share(bk, goal, start, fixed, shift=sh) for t, sh in ((-0.5, shift_lo), (1.5, shift_hi))}
            row['shocks'] = {}
            for pts in (1.0, 2.0):
                at = FP.simulate(bk, X, shocks=[(pts, 2035)])
                row['shocks'][pts] = dict(debt56=at[2056]['debt_gdp'], debt50=at[2050]['debt_gdp'],
                                          share=goal_share(bk, goal, start, fixed, shocks=[(pts, 2035)]))
        else:
            row['shocks'] = {pts: dict(debt56=FP.simulate(bk, X, shocks=[(pts, 2035)])[2056]['debt_gdp'],
                                       debt50=FP.simulate(bk, X, shocks=[(pts, 2035)])[2050]['debt_gdp'], share=None)
                             for pts in (1.0, 2.0)}
        out[gid] = row
    return out, base_sim


# ---------------------------------------------------------------- the mixes
def mixes(B, G, pp):
    bk, ph3 = B['bk'], B['ph3']
    out = {}
    for gid in ('A', 'B', 'C', 'D'):
        goal = G[gid]['goal']
        for mid, label, fixed_ids, (kind, start) in MIXES:
            fx = source_paths(bk, fixed_ids)
            fixed = add(ph3, *fx.values())
            rate = solve(bk, goal, fixed, lambda t: plug_path(bk, kind, start, t, pp))
            if rate is None:
                out[(gid, mid)] = None
                continue
            rate = round(rate + 0.005, 2)
            plug = plug_path(bk, kind, start, rate, pp)
            sim = FP.simulate(bk, add(fixed, plug))
            out[(gid, mid)] = dict(label=label, kind=kind, start=start, rate=rate, fixed=fx, plug=plug, sim=sim,
                                   first_middle=min([SOURCES[k][4] for k in fixed_ids if k != 'OUT'] + [start]))
    return out


# ---------------------------------------------------------------- D3 in the mature years
class Mature:
    def __init__(self):
        self.hh = K.Household()
        D = self.hh.D
        name = next(n for n in D.SCEN if n.startswith('Q-G'))
        self.opts = D.SCEN[name][0]
        self.y2039 = D.series(self.opts)[2039]
        import provisions as P
        self.P = P
        self.share = {k: P.dist([(k, 1.0)], D.K) for k in ('consumption', 'adults', 'surtax', 'energy', 'health_contrib')}

    def households(self, y):
        return self.hh.D.HH * adults(y) / adults(2035)

    def per_hh(self, bn, key, g, y):
        n = self.households(y) * (0.01 if g == 'T1' else 0.2)
        return bn * self.share[key][g] * 1e9 / n

    def d3(self, bk, y, amounts):
        """amounts: [(key, $B paid by households, + a cost)]: net $ a household in year y, by fifth."""
        grow = (bk.gdp[y] / bk.gdp[2039]) / (self.households(y) / self.households(2039))
        out = {}
        for g in ('Q1', 'Q2', 'Q3', 'Q4', 'Q5', 'T1'):
            out[g] = self.y2039.get(g, 0.0) * grow - sum(self.per_hh(a, k, g, y) for k, a in amounts)
        return out


def incidence(bk, mix, y, pp):
    """What households pay in year y under a mix: [(key, $B)]."""
    am = []
    for k, p in mix['fixed'].items():
        am.append((SOURCES[k][6], p[y]))
    if mix['kind'] == 'VAT':
        pts = mix['plug'][y] / vat_point(bk, y)[0] if vat_point(bk, y)[0] else 0.0
        net = pts * K.VAT_POINT_2040 * bk.gdp[y] / bk.gdp[2040]
        am.append(('consumption', net * VAT_GROSS))
        am.append(('adults', -pts * vat_point(bk, y)[1]))
    else:
        am.append(('health_contrib', mix['plug'][y]))
    return am


# ---------------------------------------------------------------- the take-home test with every new source counted
class TakeHome:
    def __init__(self, mature):
        import health_cost_review as HC
        import health_financing as HF
        import take_home_vat as T
        self.HC, self.T = HC, T
        self.per_point = T.quintile_vat_per_point(mature.hh)       # FY2040 gross VAT a household a point, by fifth
        self.energy_hh = {g: mature.per_hh(1.0, 'energy', g, 2040) for g in ('Q1', 'Q2', 'Q3', 'Q4', 'Q5')}
        self.hctx = HF.context()
        self.case = HC.cost_cases(HC._g40())['design']
        self.fold = HC.h1b_restated(self.hctx)['fold_into_s_points']
        X = HF.keys()[4]
        self.units = X['B']['units']
        self.g5 = {h['hh']: h['g5'] for h in X['B']['households']}
        self.hh_units = {}
        for u in self.units:
            self.hh_units.setdefault(u['hh'], []).append(u)
        self.hgrow = 1.048 ** 11 / self.hctx['price_2040']
        self.igrow = X['grow'] / self.hctx['price_2040']
        HC._setup_visible(self.hctx)
        self.g, self.oop = HC._setup_visible(self.hctx)
        self.partb = HC.PART_B_2026 * HC.REAL_HEALTH_2040
        self.excess_total = sum(u['weight'] * self.excess(u) for u in self.units)

    def excess(self, u):
        fs = 'joint' if u['t_fs'] == 'joint' else 'single'
        return max(0.0, u['t_agi'] * self.igrow - SUR_THRESH[fs])

    def run(self, R, vat_rate=0.0, top_bn=0.0, carb_bn=0.0):
        """Workers ahead (%), FY2040: R; a VAT at vat_rate points with its rebate; top_bn ($B) of SUR, DED and OUT;
        carb_bn of CARB."""
        HC, price = self.HC, self.hctx['price_2040']
        o = HC.unified_package(self.hctx, self.case, HC.unified_spec(R=R, S=5.0 + self.fold, hi=2.5, form='linear'))
        reb_adult = vat_rate * REBATE_PER_POINT_2040 / price
        top_k = top_bn * 1e9 / price / self.excess_total if self.excess_total else 0.0
        n = ahead = n_low = ahead_low = 0.0
        for u in self.units:
            if not HC._is_worker(u):
                continue
            members = self.hh_units[u['hh']]
            share = max(u['n_people'], 1) / sum(max(v['n_people'], 1) for v in members)
            q = 'Q%d' % self.g5.get(u['hh'], 3)
            n_ad = max(u['n_people'] - u['n_dep'], 1)
            extra = (vat_rate * self.per_point[q] / price * share - reb_adult * n_ad
                     + top_k * self.excess(u) + carb_bn * self.energy_hh[q] / price * share)
            agi = u['t_agi'] * self.igrow
            fs = 'joint' if u['t_fs'] == 'joint' else 'single'
            nn = max(u['n_people'], 1)
            kind = 'job' if u['n_employer_cov'] > 0 else ('own' if u['n_marketplace'] > 0 else
                                                         ('medicaid' if u['n_medicaid'] > 0 else
                                                          ('medicare' if u['n_medicare'] > 0 else 'uninsured')))
            prem = u['premiums_paid'] * self.hgrow
            oop = self.oop
            oo = (u['n_employer_cov'] * oop['esi'] + u['n_marketplace'] * oop['ng_sub'] + u['n_medicaid'] * oop['medicaid']
                  + u['n_medicare'] * oop['medicare']
                  + max(nn - u['n_employer_cov'] - u['n_marketplace'] - u['n_medicaid'] - u['n_medicare'], 0)
                  * oop['uninsured']) + u['n_medicare'] * self.partb
            today, plan = HC.visible(agi, fs, nn, kind, prem if kind == 'job' else 0.0,
                                     oo + (prem if kind != 'job' else 0.0), o, HC.fpl200(nn),
                                     earn=HC.earn_unit(u) * self.igrow, low2=False)
            w = u['weight']
            ok = plan + extra <= today
            n += w
            ahead += w * ok
            if agi / (HC.fpl200(nn) / 2) < 2:
                n_low += w
                ahead_low += w * ok
        return dict(workers=round(100 * ahead / n, 1), below_200fpl=round(100 * ahead_low / n_low, 1))


def take_home_mix(th, bk, mix, pp):
    y = 2040
    R = FP.R_BOOKED + (mix['plug'][y] / pp[y] if mix['kind'] == 'R' else 0.0) + (0.5 if 'R50' in mix['fixed'] else 0.0)
    vat = mix['plug'][y] / vat_point(bk, y)[0] if mix['kind'] == 'VAT' else 0.0
    top = sum(p[y] for k, p in mix['fixed'].items() if SOURCES[k][6] == 'surtax')
    carb = sum(p[y] for k, p in mix['fixed'].items() if k == 'CARB')
    return dict(R=R, vat=vat, **th.run(R, vat, top, carb))


# ---------------------------------------------------------------- build
def build(take_home=True):
    B = base()
    bk = B['bk']
    pp = FP.per_point(K.Context())
    G, base_sim = goals(B)
    M = mixes(B, G, pp)
    mat = Mature()
    d3 = {}
    for key, mix in M.items():
        if mix is None:
            continue
        d3[key] = {y: mat.d3(bk, y, incidence(bk, mix, y, pp)) for y in (2040, 2050)}
    d3['base'] = {y: mat.d3(bk, y, []) for y in (2040, 2050)}
    th = {}
    if take_home:
        T = TakeHome(mat)
        th['base'] = dict(R=FP.R_BOOKED, vat=0.0, **T.run(FP.R_BOOKED))
        for key, mix in M.items():
            if mix is not None and key[0] in ('A', 'B', 'C'):
                th[key] = take_home_mix(T, bk, mix, pp)
    return dict(B=B, bk=bk, pp=pp, G=G, base_sim=base_sim, M=M, d3=d3, th=th, y2039=mat.y2039)


# ---------------------------------------------------------------- the note
f0, f1, f2 = FP.f0, FP.f1, FP.f2


def money(v):
    return '—' if v is None else f2(v)


def markdown(d):
    B, bk, G, M = d['B'], d['bk'], d['G'], d['M']
    base_sim = d['base_sim']
    L = ['# The fiscal path revision for batch 3 (results)', '',
         'Generated by `models/tools/fiscal_revision.py --write` after the common rebuild (stage G step 9). Read with '
         '[`../7-batch3-revision.md`](../7-batch3-revision.md). Central r − g (CBO\'s February 2026 rates), the '
         'conventional score, nominal $B or % of GDP by federal fiscal year. Project arithmetic on exploratory models, '
         'not official scores.', '',
         '**The base:** the settlement as booked, %s, and G17 B\'s hold of the credits in FY2038-39 (PH-3: $%sB in '
         'FY2038-39). Debt on it: FY2040 %s%%, FY2050 %s%%, FY2056 %s%% (as booked: %s%%, %s%%, %s%%).' % (
             'with CLI-1\'s tail on the decided step-down (booked)' if B['cli1_booked'] else
             'with CLI-1\'s tail on the decided step-down (`cli1_tail.py`; a what-if until its tier-3 row lands; '
             '$%sB over FY2040-56)' % f0(sum(B['cli1_saving'][y] for y in range(2040, 2057))),
             f0(sum(B['ph3'].values())), f1(base_sim[2040]['debt_gdp']), f1(base_sim[2050]['debt_gdp']),
             f1(base_sim[2056]['debt_gdp']), f1(B['booked'].rows[2040]['debt_gdp']), f1(B['booked'].rows[2050]['debt_gdp']),
             f1(B['booked'].rows[2056]['debt_gdp'])), '']
    # 1. sources
    L += ['## 1. The sources, re-scored on the post-2025 law (FY2040, $B, net)', '',
          '| ID | Source | Central | Range | Step 8b\'s figure | From |', '| --- | --- | --- | --- | --- | --- |']
    for k, (lab, c, lo, hi, st, _, _) in SOURCES.items():
        L.append('| %s | %s | %s | %s-%s | %s-%s | FY%d |' % (k, lab, f0(c), f0(lo), f0(hi), STEP8B[k][0], STEP8B[k][1], st))
    vn, vr = vat_point(bk, 2040)
    L += ['| VAT | A broad VAT, a point, with a $%d rebate for every adult | %s net (%s before the rebate; the rebate %s) | — | 362-549 for 5%% (CBO option 72) | the mix\'s |' % (
        REBATE_PER_POINT_2040, f1(vn), f1(vn + vr), f1(vr)),
          '| R | The health contribution, a point above 3.80%% | %s | — | 224 | FY2040 |' % f0(d['pp'][2040]), '',
          'G19 B as decided (OUT, DED, CARB from FY2037; SUR from FY2040) re-scores to about $%sB in FY2040 (range $%s-%sB), against step 8b\'s $430-460B.' % (
              f0(sum(SOURCES[k][1] for k in G19B)), f0(sum(SOURCES[k][2] for k in G19B)), f0(sum(SOURCES[k][3] for k in G19B))), '']
    # 2. the goals
    L += ['## 2. Memo G23: the debt goal, redrafted', '',
          'Each goal\'s new deficit reduction (X, $B; PH-3 netted out) on the conventional score, phased in over five '
          'years from its start. A is the literal minimum that holds FY2039\'s level, measured after G19 B\'s decided '
          'FY2037-39 steps (OUT, DED, CARB). No rise after FY2040 in any of them.', '',
          '| Goal | Share of GDP | Start | ' + ' | '.join('X FY%d' % y for y in SHOW) + ' | Interest saved FY2030-56 | Debt FY2040 / FY2050 / FY2056 | Peak |',
          '| --- | --- | --- |' + ' --- |' * len(SHOW) + ' --- | --- | --- |']
    for gid in ('A', 'B', 'C', 'D'):
        g = G[gid]; s = g['sim']
        top = max(s[y]['debt_gdp'] for y in range(2030, 2057))
        peak = min(y for y in range(2030, 2057) if s[y]['debt_gdp'] >= top - 0.05)   # earliest, so a flat path reads stably
        L.append('| %s. %s | %s | FY%d | ' % (gid, g['label'], '—' if g['share'] is None else f2(g['share']) + '%', g['start']) +
                 ' | '.join(f0(g['new'][y]) for y in SHOW) +
                 ' | $%sT | %s / %s / %s | FY%d, %s |' % (f1(g['saved'] / 1000), f1(s[2040]['debt_gdp']), f1(s[2050]['debt_gdp']),
                                                       f1(s[2056]['debt_gdp']), peak, f1(s[peak]['debt_gdp'])))
    L += ['', '**X as a share of GDP:** ' + '; '.join('%s FY2040 %s%%, FY2050 %s%%, FY2056 %s%%' % (
        gid, f2(100 * G[gid]['new'][2040] / bk.gdp[2040]), f2(100 * G[gid]['new'][2050] / bk.gdp[2050]),
        f2(100 * G[gid]['new'][2056] / bk.gdp[2056])) for gid in ('A', 'B', 'C', 'D')) + '.', '']
    L += ['### r − g, the readings and the rate shocks', '',
          '| Goal | r − g FY2050-56, conventional | With CBO\'s 2-3 bp per point of lower debt (not counted) | Share needed at r − g −0.5 / +1.5 | +100 bp from FY2035: debt FY2050 / FY2056; share needed | +200 bp |',
          '| --- | --- | --- | --- | --- | --- |']
    for gid in ('A', 'B', 'C', 'D'):
        g = G[gid]
        lo_rg = g['rg_end'] - COEF_BP[1] / 100 * g['lower_debt']
        hi_rg = g['rg_end'] - COEF_BP[0] / 100 * g['lower_debt']
        rd = g.get('readings') or {}
        sh = g['shocks']
        L.append('| %s | %s | %s to %s (debt %s points below the base) | %s / %s | %s / %s; %s | %s / %s; %s |' % (
            gid, f2(g['rg_end']), f2(lo_rg), f2(hi_rg), f1(g['lower_debt']),
            money(rd.get(-0.5)), money(rd.get(1.5)),
            f1(sh[1.0]['debt50']), f1(sh[1.0]['debt56']), money(sh[1.0]['share']),
            f1(sh[2.0]['debt50']), f1(sh[2.0]['debt56']), money(sh[2.0]['share'])))
    L += ['', 'The base\'s own r − g over FY2050-56 is %s. Under the hard rule the rate feedback counts toward no goal; it shows what each goal does to the risk Espen named.' % f2(G['A']['rg_base_end']), '']
    # 3. mixes
    L += ['## 3. Memo G24: how each goal is financed', '',
          'Each mix enacts its fixed sources on their dates and closes the goal with one plug at a constant rate from its start: '
          'the health contribution\'s base rate R above 3.80%, or a VAT (points) with its rebate. "Reaches the middle class" is the first year a broad source starts.', '',
          '| Goal | Mix | Plug | Plug\'s rate | Fixed sources FY2040 ($B) | Plug FY2040 / FY2050 ($B) | Debt FY2050 / FY2056 | Reaches the middle class |',
          '| --- | --- | --- | --- | --- | --- | --- | --- |']
    for gid in ('A', 'B', 'C', 'D'):
        for mid, label, _, _ in MIXES:
            mx = M[(gid, mid)]
            if mx is None:
                L.append('| %s | %s. %s | — | not reachable | | | | |' % (gid, mid, label))
                continue
            L.append('| %s | %s. %s | %s from FY%d | %s | %s | %s / %s | %s / %s | FY%d |' % (
                gid, mid, label, mx['kind'], mx['start'],
                ('%s points (R %s%%)' % (f2(mx['rate']), f2(FP.R_BOOKED + mx['rate']))) if mx['kind'] == 'R' else '%s%%' % f2(mx['rate']),
                f0(sum(p[2040] for p in mx['fixed'].values())), f0(mx['plug'][2040]), f0(mx['plug'][2050]),
                f1(mx['sim'][2050]['debt_gdp']), f1(mx['sim'][2056]['debt_gdp']), mx['first_middle']))
    L.append('')
    # 4. D3
    L += ['## 4. D3 in FY2040 and FY2050 ($ a household a year, nominal)', '',
          'The booked FY2039 position (scenario Q-G: ' + ' / '.join('%s %s' % (g, f0(d['y2039'][g])) for g in ('Q1', 'Q2', 'Q3', 'Q4', 'Q5')) +
          ') carried forward with income per household, less each mix\'s new sources that year. Approximate (the model\'s header).', '',
          '| Goal, mix | Year | Q1 | Q2 | Q3 | Q4 | Q5 | Every fifth below the top ahead? |',
          '| --- | --- | --- | --- | --- | --- | --- | --- |']
    rows = [('base', 'The base, no new source')] + [((gid, mid), '%s, mix %s' % (gid, mid)) for gid in ('A', 'B', 'C', 'D') for mid, *_ in MIXES]
    for key, lab in rows:
        if key not in d['d3']:
            continue
        for y in (2040, 2050):
            v = d['d3'][key][y]
            L.append('| %s | FY%d | %s | %s |' % (lab, y, ' | '.join(f0(v[g]) for g in ('Q1', 'Q2', 'Q3', 'Q4', 'Q5')),
                                               'yes' if all(v[g] > 0 for g in ('Q1', 'Q2', 'Q3', 'Q4')) else '**no**'))
    L.append('')
    # 5. take-home
    if d['th']:
        L += ['## 5. The take-home test, FY2040, everything counted (target 85-90%)', '',
              'Workers whose visible health costs plus the new sources they pay fall under the plan (health\'s test, `take_home_vat.py`\'s method).', '',
              '| Goal, mix | R | VAT | Workers ahead | Below 200% of poverty |', '| --- | --- | --- | --- | --- |']
        for key, v in d['th'].items():
            lab = 'The base (R 3.80%, nothing new)' if key == 'base' else '%s, mix %s' % key
            L.append('| %s | %s%% | %s%% | %s%% | %s%% |' % (lab, f2(v['R']), f2(v['vat']), f1(v['workers']), f1(v['below_200fpl'])))
        L.append('')
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
