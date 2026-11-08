#!/usr/bin/env python3
"""The 2028 House on the current maps, and the 2029 trifecta, chained to the Senate model's runs.

Role: the arithmetic behind dossiers/scenario/house-model-2028.md. Status: exploratory scenario model (stage B,
November 8, 2026); this project's own analysis, not a forecast. It is a seats-votes curve, not a district-by-
district model: no district-level 2028 data exists yet, and the curve is pinned by three published facts about
the 2026 lines. ASSUMPTIONS are marked, with the ranges tested in the sensitivity table.

Calibration (data, `2028-outlook.md` section 2):
  - Under the 2026 lines Trump carried 234 districts to 201 while winning the nation by 1.48 points [SRC-0817]
    [SRC-0459]: at a national presidential margin of R+1.48, Democrats would win 201 seats on uniform swing.
  - The median district (WI-1) is Trump +4.5, 3.0 points right of the nation [SRC-0817]; Wang puts the
    Democratic break-even near D+3 [SRC-0818]. So 217.5 seats at about D+3.0.
  - Check: in 2026 Democrats won about 259 seats (1-results.md) at a House vote of D+12.9.
The curve is seats(E) = 435 * Phi((E + inc - median) / spread), where E is the presidential margin, inc the net
incumbency shift in 2028 and spread fitted to the first two facts. Run:

  python3 dossiers/scenario/tools/house_model.py            print the tables
  python3 dossiers/scenario/tools/house_model.py --write    regenerate dossiers/scenario/house-model-outputs.md
"""
import math
import os
import random
import statistics as st
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import senate_model as sm  # noqa: E402

SEATS = 435
MAJORITY = 218
TRUMP_DISTRICTS_2024 = 234   # under the 2026 lines [SRC-0817]
NAT_PRES_2024 = sm.NAT[2024]  # -1.48
MEDIAN_LEAN = -3.0           # WI-1 Trump +4.5 against national Trump +1.5 [SRC-0817]


def phi(x):
    return 0.5 * (1 + math.erf(x / math.sqrt(2)))


def inv_phi(p):
    lo, hi = -10.0, 10.0
    for _ in range(100):
        mid = (lo + hi) / 2
        if phi(mid) < p:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def fit_spread(median=-MEDIAN_LEAN, d_at_2024=SEATS - TRUMP_DISTRICTS_2024):
    """Spread such that Democrats win d_at_2024 seats at the 2024 national margin."""
    z = inv_phi(d_at_2024 / SEATS)
    return (NAT_PRES_2024 - median) / z


PARAMS = {
    'median': -MEDIAN_LEAN,  # break-even presidential margin on the 2026 lines, before incumbency; 2-4 tested
    'inc': 1.5,       # ASSUMPTION: net incumbency shift toward D in 2028 (about 45 freshmen Democrats hold seats
                      # won from Republicans; worth about 2-3 points each where it matters); 0.5-3.0 tested
    'sd_house': 1.5,  # ASSUMPTION: national House-vs-presidential deviation (ticket splitting), SD in points
    'sd_seats': 5.0,  # ASSUMPTION: seat noise from district idiosyncrasy and curve error, SD in seats
}

# Map changes that could still land before 2028 (`2028-outlook.md` section 2). ASSUMPTIONS: (probability, seat
# change for Democrats). Sources: New York amendment and referendum [SRC-0815]; Maryland Question 3 [SRC-0957];
# Wisconsin map suits [SRC-0959]; Mississippi [SRC-0815]; further Republican redraws after Callais [SRC-0816].
MAP_CHANGES = {
    'New York redraw (2027 referendum)': (0.45, 3.0),
    'Maryland MD-1': (0.70, 1.0),
    'Wisconsin new map': (0.30, 1.5),
    'Mississippi redraw': (0.40, -1.0),
    'Other Republican redraws or Callais rulings': (0.30, -2.0),
}


def map_shift(rng):
    return sum(d for p, d in MAP_CHANGES.values() if rng.random() < p)


def house_seats(pres, rng, prm, spread):
    """Democratic House seats in one run, given the presidential margin `pres`."""
    e = pres + rng.gauss(0, prm['sd_house'])
    s = SEATS * phi((e + prm['inc'] - prm['median']) / spread) + map_shift(rng) + rng.gauss(0, prm['sd_seats'])
    return int(round(min(SEATS, max(0, s))))


def simulate(env, n=20000, seed=2028, env_sd=0.0, prm=None):
    """Senate runs from senate_model, with a House draw per run. Returns per-run tuples."""
    prm = dict(PARAMS, **(prm or {}))
    spread = fit_spread(prm['median'])
    o = sm.simulate_2028(env, n=n, seed=seed, env_sd=env_sd)
    rng = random.Random(seed + 7)
    runs = []
    for i in range(n):
        h = house_seats(o['env'][i], rng, prm, spread)
        sen = o['seats'][i]
        dp = o['dpres'][i]
        sen_ctrl = sen >= 51 or (sen == 50 and dp)
        runs.append((h, sen, dp, sen_ctrl))
    return runs


def summary(runs, cond=None):
    rr = [r for r in runs if cond is None or r[2] == (cond == 'D')]
    m = len(rr)
    hs = sorted(r[0] for r in rr)
    return dict(
        n=m, mean=st.mean(hs), p5=hs[int(0.05 * m)], p95=hs[min(m - 1, int(0.95 * m))],
        house=sum(r[0] >= MAJORITY for r in rr) / m,
        trifecta=sum(r[0] >= MAJORITY and r[2] and r[3] for r in rr) / m,
        house_and_senate=sum(r[0] >= MAJORITY and r[3] for r in rr) / m,
        h230=sum(r[0] >= 230 for r in rr) / m,
    )


def fmt(x):
    return sm.fmt_pct(x)


def report(n=20000):
    L = []
    w = L.append
    sp = fit_spread()
    w('# House model outputs (generated)\n')
    w('Role: the tables `tools/house_model.py --write` produces, read by `house-model-2028.md`. Status: generated; do not '
      'edit by hand. This project\'s exploratory scenario arithmetic, not a forecast. n = %d runs per row, seeded; '
      'the Senate and presidency in each run come from `senate_model.py`.\n' % n)
    w('## 1. The curve\n')
    w('Fitted spread %.1f points; seats per point of national margin near the median: %.1f. Democratic seats on the '
      '2026 lines by presidential margin, before incumbency, map changes and noise:\n' % (sp, SEATS / math.sqrt(2 * math.pi) / sp))
    w('| Presidential margin | R+3 | R+1.5 | Even | D+3 | D+6 | D+9 | D+12.9 |')
    w('| --- | --- | --- | --- | --- | --- | --- | --- |')
    w('| Democratic seats | ' + ' | '.join('%d' % round(SEATS * phi((e - PARAMS['median']) / sp))
                                          for e in (-3, -1.48, 0, 3, 6, 9, 12.9)) + ' |')
    w('\nCheck against 2026: the curve gives %d seats at D+12.9 against about 259 won (House vote D+12.9; '
      '1-results.md), so 2026 Democrats ran about %.1f points ahead of uniform swing.\n' % (
          round(SEATS * phi((12.9 - PARAMS['median']) / sp)), PARAMS['median'] + inv_phi(259 / SEATS) * sp - 12.9))
    w('## 2. The House and the trifecta in January 2029\n')
    w('| Environment | Mean D seats | 90% range | P(D House) | P(230+) | P(D House and D Senate) | P(trifecta) |')
    w('| --- | --- | --- | --- | --- | --- | --- |')
    allruns = {}
    for label, e, sd in sm.SCENARIOS + [sm.PRIOR]:
        runs = simulate(e, n=n, env_sd=sd)
        allruns[label] = runs
        s = summary(runs)
        w('| %s | %.0f | %d-%d | %s | %s | %s | %s |' % (label, s['mean'], s['p5'], s['p95'], fmt(s['house']),
                                                        fmt(s['h230']), fmt(s['house_and_senate']), fmt(s['trifecta'])))
    w('\n## 3. By presidential winner (evidence-weighted prior)\n')
    w('| Winner | Share | Mean D House seats | P(D House) | P(D Senate control) | P(trifecta) |')
    w('| --- | --- | --- | --- | --- | --- |')
    runs = allruns[sm.PRIOR[0]]
    for cond in ('D', 'R'):
        s = summary(runs, cond)
        sen = sum(r[3] for r in runs if r[2] == (cond == 'D')) / s['n']
        w('| %s president | %s | %.0f | %s | %s | %s |' % ('Democratic' if cond == 'D' else 'Republican',
                                                         fmt(s['n'] / len(runs)), s['mean'], fmt(s['house']),
                                                         fmt(sen), fmt(s['trifecta'])))
    w('\n## 4. Sensitivity (D+3)\n')
    w('| Change | Mean D seats | P(D House) | P(trifecta) |')
    w('| --- | --- | --- | --- |')
    for label, prm in [('Base', {}), ('Incumbency shift 0.5', {'inc': 0.5}), ('Incumbency shift 3.0', {'inc': 3.0}),
                       ('Break-even D+2', {'median': 2.0}), ('Break-even D+4', {'median': 4.0}),
                       ('House-vs-presidential SD 3', {'sd_house': 3.0}), ('Seat noise SD 10', {'sd_seats': 10.0})]:
        s = summary(simulate(3.0, n=n // 2, seed=5, prm=prm))
        w('| %s | %.0f | %s | %s |' % (label, s['mean'], fmt(s['house']), fmt(s['trifecta'])))
    rng = random.Random(1)
    shifts = [map_shift(rng) for _ in range(20000)]
    w('\nMap changes before 2028 (assumptions): mean %+.1f Democratic seats, range %+.0f to %+.0f. ' % (
        st.mean(shifts), min(shifts), max(shifts)) + '; '.join('%s %s chance of %+.1f' % (k, fmt(p), d)
                                                               for k, (p, d) in MAP_CHANGES.items()) + '.\n')
    w('## 5. Break-even environments\n')
    w('The presidential margin at which each outcome reaches 50% (scan in 0.5-point steps, fixed environment):\n')
    targets = {'D House': None, 'trifecta': None}
    for e10 in range(-40, 101, 5):
        e = e10 / 10
        s = summary(simulate(e, n=4000, seed=9))
        if targets['D House'] is None and s['house'] >= 0.5:
            targets['D House'] = e
        if targets['trifecta'] is None and s['trifecta'] >= 0.5:
            targets['trifecta'] = e
    w('| Outcome | 50% at |')
    w('| --- | --- |')
    for k, v in targets.items():
        w('| %s | %s |' % (k, ('D+%.1f' % v if v >= 0 else 'R+%.1f' % -v) if v is not None else 'above D+10'))
    w('\n## 6. Is "Senate control with a Democratic president" really near 100%?\n')
    w('Evidence-weighted prior, runs with a Democratic president. "Narrow win" means a presidential margin under 3 points. '
      'Every run already carries race, regional and Senate-wide errors, so a split result is possible; the stressed rows '
      'widen them (race SD 8, regional SD 4, Senate-wide SD 2) and/or lose all three uncertain seats not up (Alaska and '
      'Mississippi 2026, Minnesota 2027).\n')
    w('| Case | 51+ seats | Exactly 50 (+ VP) | 49 or fewer | Narrow wins: 50 or fewer | Narrow wins: 49 or fewer |')
    w('| --- | --- | --- | --- | --- | --- |')
    for label, kw in [('Base', {}),
                      ('Lose AK, MS and MN (37 not up)', {'uncertain': {'AK-2026': 0.0, 'MS-2026': 0.0, 'MN-2027': 0.0}}),
                      ('Wider errors', {'prm': {'sd_race': 8.0, 'sd_reg': 4.0, 'sd_tick': 2.0}}),
                      ('Both', {'prm': {'sd_race': 8.0, 'sd_reg': 4.0, 'sd_tick': 2.0},
                                'uncertain': {'AK-2026': 0.0, 'MS-2026': 0.0, 'MN-2027': 0.0}})]:
        o = sm.simulate_2028(3.0, n=n, env_sd=4.5, **kw)
        d = [i for i in range(o['n']) if o['dpres'][i]]
        nar = [i for i in d if o['env'][i] < 3.0]
        f = lambda idx, cond: sum(1 for i in idx if cond(o['seats'][i])) / len(idx)
        w('| %s | %s | %s | %s | %s | %s |' % (label, fmt(f(d, lambda s: s >= 51)), fmt(f(d, lambda s: s == 50)),
                                               fmt(f(d, lambda s: s <= 49)), fmt(f(nar, lambda s: s <= 50)),
                                               fmt(f(nar, lambda s: s <= 49))))
    return '\n'.join(L) + '\n'


if __name__ == '__main__':
    text = report()
    if '--write' in sys.argv:
        path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'house-model-outputs.md')
        with open(path, 'w') as f:
            f.write(text)
        print('wrote', os.path.normpath(path))
    else:
        print(text)
