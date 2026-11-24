#!/usr/bin/env python3
"""Stage G step 8b: the frontier. Debt goal x take-home share x health contribution base rate (R), with memo G8's options.

Role: the one table every step 8b package is shown on (`dossiers/foundations/fair-financing/4-fiscal-path.md` part 3).
For each debt goal of `DEC-2026-11-24-15` (central r - g, the conventional score; `fiscal_path.py`), each take-home level
(`DEC-2026-11-24-12`, through the base rate R that gives it) and each G8 path (`DEC-2026-11-24-13`; memo G8's A to D),
it gives the money that has to come from sources other than R, by year. The goals, the take-home level and G8 draw on
the same money, so they are priced together, never one at a time. Status: stage G step 8b, tier 2; books nothing.
Writes `dossiers/foundations/fair-financing/notes/frontier-results.md` with `--write`; `test_fiscal_path.py` checks it.

Arithmetic (project arithmetic on exploratory models, not official scores):
  * X_goal(y): the extra deficit reduction a goal needs (fiscal_path.solve_share, the FY2032-36 ramp).
  * A point of R raises per_point(y) $B (four quarter points of $56B in FY2040, grown on HCU's path), linear.
  * Other money needed(y) = X_goal(y) + (R_booked(y) - R_path(y)) * per_point(y) from the 2035 endpoint, where
    R_booked is 3.80% and R_path is the package's rate path (the take-home level, then G8's steps).
  * The take-home share is health's test in FY2040 at that year's R (budget_scan.take_home), everything counted.

    python3 models/tools/fiscal_frontier.py            # print
    python3 models/tools/fiscal_frontier.py --write    # write the results note
"""
import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'models/tools'))
import fiscal_path as FP   # noqa: E402

OUT = ROOT / 'dossiers/foundations/fair-financing/notes/frontier-results.md'
YEARS = FP.YEARS
SHOW = (2036, 2038, 2040, 2045, 2050, 2056)
R_BOOKED = FP.R_BOOKED
TAKE_HOME = (('69.0% (booked)', 3.80), ('76.2%', 3.25), ('80%', None), ('85% (the target\'s floor)', None))
GOALS = (('none', 'No debt goal (the booked path)'),) + FP.GOALS


def g8_path(option, base_rate):
    """{year: R} from FY2035 for memo G8's option on a base rate. A: steps of 0.15 and 0.40 points below it from FY2046
    and FY2051 (memo G8's 3.65% and 3.40% on 3.80%); B: 3.25% in FY2035-39, then the base rate; C: flat; D: as C until a
    finding (on a debt goal, D's surplus finding must be measured against the goal's path, so it adds nothing here)."""
    out = {}
    for y in YEARS:
        if y < 2035:
            continue
        r = base_rate
        if option == 'A':
            r = base_rate - (0.40 if y >= 2051 else 0.15 if y >= 2046 else 0.0)
        elif option == 'B' and y <= 2039:
            r = min(base_rate, 3.25)
        out[y] = r
    return out


def other_money(bk, pp, x_goal, rate_path):
    return {y: x_goal.get(y, 0.0) + ((R_BOOKED - rate_path[y]) * pp[y] if y in rate_path else 0.0) for y in YEARS}


# Step 8b's phasing candidates for FY2036-39 (part 4 of 4-fiscal-path.md): each a cut in the booked line's path,
# $B by year (+ lowers the deficit), read from the booked case's own audit lines.
PHASING = (
    ('PH-1', 'Long-term care (HLT-9) reaches full benefit in FY2039, not on its own ramp: 40/55/70/85% of its FY2035-38 '
             'path, net of the states\' payment (S05)', ('HLT-9', "Settlement S05"), {2035: .60, 2036: .45, 2037: .30, 2038: .15}),
    ('PH-2', 'Housing stage 2 (housing_extra) held at its FY2036 enrollment level until FY2040', ('housing_extra',), 'hold2036'),
    ('PH-3', 'Clean-energy credits (CLI-1) held at their FY2037 level in FY2038-39', ('CLI-1',), 'hold2037'),
)


def line_paths(bk):
    P = {}
    for a in bk.case['audit']:
        P.setdefault(a['line'], {}).setdefault(a['year'], 0.0)
        P[a['line']][a['year']] += a['primary_deficit_change_bn']
    return P


def phasing(bk):
    """{id: {year: saving $B}} for each candidate."""
    P = line_paths(bk)
    def path(prefixes):
        out = {y: 0.0 for y in YEARS}
        for k, p in P.items():
            if any(k == pre or k.startswith(pre) for pre in prefixes):
                for y, v in p.items():
                    out[y] += v
        return out
    res = {}
    for pid, _, lines, rule in PHASING:
        p = path(lines)
        if isinstance(rule, dict):
            res[pid] = {y: rule.get(y, 0.0) * p[y] for y in YEARS}
        elif rule == 'hold2036':
            res[pid] = {y: (p[y] - p[2036]) if 2037 <= y <= 2039 else 0.0 for y in YEARS}
        else:
            res[pid] = {y: (p[y] - p[2037]) if 2038 <= y <= 2039 else 0.0 for y in YEARS}
    return res


def solve_with(bk, goal, base_x):
    """The smallest share (the FY2032-36 ramp) that meets the goal on top of a fixed deficit-reduction path base_x."""
    ok = lambda s: FP.met(goal, FP.simulate(bk, {y: base_x.get(y, 0.0) + v for y, v in FP.shape(bk, s).items()}))
    if ok(0.0):
        return 0.0
    lo, hi = 0.0, 8.0
    for _ in range(40):
        mid = (lo + hi) / 2
        lo, hi = (lo, mid) if ok(mid) else (mid, hi)
    return round(hi + 0.0005, 3)


def build(take_home=True):
    bk = FP.Booked()
    pp = FP.per_point(FP.K.Context())
    curve = FP.take_home_curve() if take_home else None
    rates = []
    for lab, r in TAKE_HOME:
        if r is None:
            r = round(FP.rate_for(curve, float(lab.split('%')[0])), 2) if curve else (2.95 if lab.startswith('80') else 2.57)
        rates.append((lab, r))
    shares = {g: (0.0 if g == 'none' else FP.solve_share(bk, g, 0.0)) for g, _ in GOALS}
    xs = {g: FP.shape(bk, s) for g, s in shares.items()}
    grid = {}
    for g, _ in GOALS:
        for lab, r in rates:
            for opt in ('A', 'B', 'C', 'D'):
                om = other_money(bk, pp, xs[g], g8_path(opt, r))
                sim = FP.simulate(bk, xs[g])   # the mix of sources moves no debt: other money replaces the R given up
                grid[(g, lab, opt)] = dict(rate=r, other=om, debt=sim)
    # If R carried everything (no other money): the R each goal needs, by year, and the take-home at the FY2040 rate
    r_all = {g: {y: R_BOOKED + xs[g][y] / pp[y] for y in YEARS if y >= 2035} for g, _ in GOALS}
    # G8's options on the booked path (no goal): the debt they leave (the surplus returned is not deficit reduction)
    g8_debt = {}
    for opt in ('A', 'B', 'C'):
        giveback = {y: -(R_BOOKED - r) * pp[y] for y, r in g8_path(opt, R_BOOKED).items()}
        g8_debt[opt] = FP.simulate(bk, giveback)
    ph = phasing(bk)
    allph = {y: sum(p[y] for p in ph.values()) for y in YEARS}
    ph_shares = {g: solve_with(bk, g, allph) for g, _ in GOALS if g != 'none'}
    return dict(bk=bk, pp=pp, curve=curve, rates=rates, shares=shares, xs=xs, grid=grid, r_all=r_all, g8_debt=g8_debt,
                phasing=ph, phasing_all=allph, phasing_shares=ph_shares)


def markdown(d):
    f0, f1, f2 = FP.f0, FP.f1, FP.f2
    bk, pp, curve = d['bk'], d['pp'], d['curve']
    gdp = bk.gdp
    th = (lambda r: f1(FP.interp(curve, r)) + '%') if curve else (lambda r: '—')
    L = ['# The fiscal path review, part 3: the frontier (results)', '',
         'Generated by `models/tools/fiscal_frontier.py --write` (stage G step 8b). Read with '
         '[`../4-fiscal-path.md`](../4-fiscal-path.md) part 3. Central r − g (the booked path\'s CBO rates), the '
         'conventional score. **Other money** is what must come from sources other than the health contribution\'s base '
         'rate R: cuts, phasing, other revenue. It equals the goal\'s extra deficit reduction plus the R points given up '
         'below the booked 3.80%%. A point of R is about $%sB in FY2040 and $%sB in FY2056. The take-home share is health\'s '
         'test in FY2040 at that R, everything counted, no VAT. Project arithmetic, not an official score.' % (
             f0(pp[2040]), f0(pp[2056])), '']
    # 1. the main grid, G8 C (the booked path's rule) for clarity
    L += ['## 1. Other money needed, by goal and take-home level (G8 C: one rate held)', '',
          '| Debt goal | Take-home (R) | Share of GDP for the goal | ' + ' | '.join('FY%d' % y for y in SHOW) +
          ' | FY2040, % of GDP | FY2056, % of GDP |', '| --- | --- | --- |' + ' --- |' * len(SHOW) + ' --- | --- |']
    for g, glab in GOALS:
        for lab, r in d['rates']:
            om = d['grid'][(g, lab, 'C')]['other']
            L.append('| %s | %s (R %s%%) | %s | ' % (glab, lab, f2(r), f2(d['shares'][g])) + ' | '.join(f0(om[y]) for y in SHOW) +
                     ' | %s | %s |' % (f2(100 * om[2040] / gdp[2040]), f2(100 * om[2056] / gdp[2056])))
    L.append('')
    # 2. R alone
    L += ['## 2. If R carried each goal alone (no other money)', '',
          '| Debt goal | R FY2036 | R FY2040 | R FY2050 | R FY2056 | Workers ahead at the FY2040 rate |', '| --- | --- | --- | --- | --- | --- |']
    for g, glab in GOALS:
        ra = d['r_all'][g]
        L.append('| %s | %s%% | %s%% | %s%% | %s%% | %s |' % (glab, f2(ra[2036]), f2(ra[2040]), f2(ra[2050]), f2(ra[2056]), th(ra[2040])))
    L.append('')
    # 3. G8
    L += ['## 3. Memo G8\'s options against the goals', '',
          'Each G8 option changes R after 2035, so it changes the other money a goal needs. On the booked path (no goal), '
          'the money G8 A or B gives back is not deficit reduction, so it raises debt. **On any debt goal, D\'s trigger '
          '(a general-fund surplus above 0.1% of GDP for two years) would fire on the goal\'s own deficit reduction and '
          'give it back, so D only works with its finding measured against the goal\'s path** (a surplus beyond what the '
          'goal needs); measured that way, it returns nothing on the central estimate, as C.', '',
          '| Debt goal | Take-home (R) | G8 | Other money FY2036 | FY2040 | FY2050 | FY2056 | Debt FY2056 |', '| --- | --- | --- | --- | --- | --- | --- | --- |']
    for g, glab in GOALS:
        lab, r = d['rates'][0]
        for opt in ('A', 'B', 'C', 'D'):
            cell = d['grid'][(g, lab, opt)]
            om = cell['other']
            debt56 = (d['g8_debt'][opt][2056]['debt_gdp'] if g == 'none' and opt in d['g8_debt'] else cell['debt'][2056]['debt_gdp'])
            L.append('| %s | %s | %s | %s | %s | %s | %s | %s |' % (glab, lab, opt, f0(om[2036]), f0(om[2040]), f0(om[2050]), f0(om[2056]), f1(debt56)))
    L.append('')
    # 4. phasing
    ph = d['phasing']
    L += ['## 4. Phasing candidates for FY2036-39 ($B saved; + lowers the deficit)', '',
          '| ID | What | FY2035 | FY2036 | FY2037 | FY2038 | FY2039 | FY2035-39 |', '| --- | --- | --- | --- | --- | --- | --- | --- |']
    for pid, lab, _, _ in PHASING:
        p = ph[pid]
        L.append('| %s | %s | %s | %s |' % (pid, lab, ' | '.join(f0(p[y]) for y in range(2035, 2040)), f0(sum(p[y] for y in range(2035, 2040)))))
    a = d['phasing_all']
    L.append('| | **All three** | %s | %s |' % (' | '.join(f0(a[y]) for y in range(2035, 2040)), f0(sum(a[y] for y in range(2035, 2040)))))
    L += ['', 'The goals\' share of GDP from FY2036 on top of all three: ' + '; '.join(
        '%s %s (without phasing %s)' % (lab.split(' (')[0], f2(d['phasing_shares'][g]), f2(d['shares'][g])) for g, lab in GOALS if g != 'none') + '.', '']
    if curve:
        L += ['The take-home curve (FY2040): ' + '; '.join('R %s%%: %s%%' % (f2(r), f1(w)) for r, w in curve) + '.', '']
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
