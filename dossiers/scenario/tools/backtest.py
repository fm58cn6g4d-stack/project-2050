#!/usr/bin/env python3
"""Back-test and stress test of the scenario model stack (Senate, House, environment prior).

Role: the arithmetic behind dossiers/scenario/model-credibility.md. Status: exploratory (stage B, November 8,
2026). The Senate back-test re-runs the senate_model method for the 2018, 2020, 2022 and 2024 Senate classes
with only what was known two years earlier: the two latest presidential results, the latest midterm Senate
results and the incumbents' own last races (FiveThirtyEight's results files [SRC-0600], extracted to
model-credibility-data.json). The House back-test re-fits house_model's curve on the previous election's
seats and votes (Brookings table 2-2 [SRC-0570]). The environment test scores simple two-years-out rules on
every presidential and midterm year since 1990.

  python3 dossiers/scenario/tools/backtest.py            print the tables
  python3 dossiers/scenario/tools/backtest.py --write    regenerate dossiers/scenario/model-credibility-outputs.md
"""
import json
import math
import os
import random
import statistics as st
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import senate_model as sm  # noqa: E402
import house_model as hm   # noqa: E402

DATA = json.load(open(os.path.join(HERE, '..', 'model-credibility-data.json')))
PRES = {int(k): v for k, v in DATA['pres'].items()}
# National margins (D minus R). Presidential [SRC-0588]; House vote, Brookings table 2-2 [SRC-0570].
NAT_PRES = {1988: -7.7, 1992: 5.6, 1996: 8.5, 2000: 0.5, 2004: -2.5, 2008: 7.3, 2012: 3.9, 2016: 2.1, 2020: 4.46,
            2024: -1.48}
NAT_HOUSE = {1990: 7.9, 1994: -7.0, 1998: -0.9, 2002: -4.6, 2006: 6.4, 2010: -6.6, 2012: 1.4, 2014: -5.1,
             2016: -0.9, 2018: 8.7, 2020: 3.0, 2022: -2.6, 2024: -2.5, 2026: 12.9}
HOUSE_SEATS_D = {2016: 194, 2018: 235, 2020: 222, 2022: 213, 2024: 215}   # Brookings table 2-2 (seat shares x 435)
PRES_PARTY = {2018: 'R', 2022: 'D', 2026: 'R', 2014: 'D', 2010: 'D', 2006: 'R', 2002: 'R', 1998: 'D', 1994: 'D',
              1990: 'R'}
MIDTERMS = [1990, 1994, 1998, 2002, 2006, 2010, 2014, 2018, 2022, 2026]


def midterm_swing(y):
    """Swing against the president's party at midterm y (from the previous presidential year)."""
    prev = NAT_HOUSE.get(y - 2, NAT_PRES.get(y - 2))
    if y - 2 in (1988, 1992, 1996, 2000, 2004, 2008):
        prev = {1988: 7.8, 1992: 5.2, 1996: -0.4, 2000: -0.3, 2004: -2.6, 2008: 10.6}[y - 2]  # House vote then
    d = NAT_HOUSE[y] - prev
    return -d if PRES_PARTY[y] == 'D' else d


# ---------------------------------------------------------------------------------------------- Senate
def races(cycle):
    return [r for r in DATA['senate'] if r['cycle'] == cycle and r['stage'] in ('general', 'runoff')]


def margin(r):
    if r['d'] is None or r['r'] is None:
        return None
    return r['d'] - r['r']


def prior_holder(r):
    """The most recent earlier race for the same seat: (race, winner name, party)."""
    prev = [x for x in DATA['senate'] if x['state'] == r['state'] and x['seat'] == r['seat'] and
            x['cycle'] < r['cycle'] and x['stage'] in ('general', 'runoff') and x['winner']]
    if not prev:
        return None
    p = max(prev, key=lambda x: (x['cycle'], x['stage'] == 'runoff'))
    m = margin(p)
    party = 'D' if (m is not None and m > 0) or p['winner_party'] in ('DEM', 'DFL', 'WFP') else 'R'
    return p, p['winner'], party


def latest(years, upto):
    return [y for y in years if y <= upto]


def lean_at(state, info_year, prm):
    pres_years = latest(sorted(PRES), info_year)[-2:]
    mid = latest([y for y in MIDTERMS if y in NAT_HOUSE and y <= 2022], info_year)
    mid = mid[-1] if mid else None
    la = PRES[pres_years[0]][state] - NAT_PRES[pres_years[0]]
    lb = PRES[pres_years[1]][state] - NAT_PRES[pres_years[1]]
    parts = [(prm['w20'], la), (prm['w24'], lb)]
    if mid is not None:
        ms = [r for r in races(mid) if r['state'] == state and margin(r) is not None]
        if ms:
            vals = []
            for r in ms:
                ph = prior_holder(r)
                adj = 0.0
                if ph and ph[1] in r['candidates']:
                    adj = prm['inc'] * (1 if ph[2] == 'D' else -1)
                vals.append(margin(r) - adj)
            parts.append((prm['w26'], st.mean(vals) - NAT_HOUSE[mid]))
    w = sum(p for p, _ in parts)
    return sum(p * v for p, v in parts) / w


def expected_then(state, year):
    if year in NAT_PRES and year in PRES:
        return PRES[year][state]
    yrs = sorted(PRES)
    before = max(y for y in yrs if y < year)
    after = min([y for y in yrs if y > year] or [before])
    mid = 0.5 * ((PRES[before][state] - NAT_PRES[before]) + (PRES[after][state] - NAT_PRES[after]))
    return NAT_HOUSE.get(year, 0.0) + mid


def cand_effect(r, prm):
    ph = prior_holder(r)
    if not ph or ph[1] not in r['candidates']:
        return 0.0, False, None
    p, name, party = ph
    sign = 1 if party == 'D' else -1
    m = margin(p)
    if m is None:
        return sign * prm['inc'], True, party
    was_inc = bool(prior_holder(p)) and prior_holder(p)[1] == name
    over = m - expected_then(r['state'], p['cycle'])
    resid = max(-12.0, min(12.0, over - (sign * prm['inc'] if was_inc else 0.0)))
    c = sign * prm['inc'] + prm['shrink'] * resid
    return max(-prm['cap'], min(prm['cap'], c)), True, party


def senate_backtest(target, env, env_sd=0.0, n=4000, seed=1, prm=None):
    prm = dict(sm.BASE_PARAMS, **(prm or {}))
    info = target - 2
    rows = []
    for r in races(target):
        m = margin(r)
        if m is None or r['state'] in ('ME', 'VT'):
            continue   # no D-v-R contest (independents, top-two), or an independent caucusing with Democrats
        L = lean_at(r['state'], info, prm)
        c, running, party = cand_effect(r, prm)
        rows.append(dict(state=r['state'] + ('*' if r['special'] else ''), L=L, c=c, open=not running, actual=m))
    rng = random.Random(seed)
    regions = sorted(sm.REGION)
    wins = [0] * len(rows)
    seat_err = []
    for _ in range(n):
        e = env + (rng.gauss(0, env_sd) if env_sd else 0.0) + rng.gauss(0, prm['sd_nat'] if env_sd else 0.0)
        tick = rng.gauss(0, prm['sd_tick'])
        reg = {g: rng.gauss(0, prm['sd_reg']) for g in regions}
        dw = 0
        for k, x in enumerate(rows):
            sd = prm['sd_race'] if not x['open'] else math.hypot(prm['sd_race'], prm['sd_open'])
            mm = x['L'] + e + x['c'] + prm.get('bias', 0.0) + tick + reg[sm.REGION_OF[x['state'].rstrip('*')]] + rng.gauss(0, sd)
            if mm > 0:
                wins[k] += 1
                dw += 1
        seat_err.append(dw)
    actual_d = sum(1 for x in rows if x['actual'] > 0)
    probs = [w / n for w in wins]
    brier = st.mean((p - (x['actual'] > 0)) ** 2 for p, x in zip(probs, rows))
    naive = st.mean((1.0 if PRES[max(latest(sorted(PRES), info))][x['state'].rstrip('*')] > 0 else 0.0) != (x['actual'] > 0)
                    for x in rows)
    seat_err.sort()
    mean_pred = st.mean(seat_err)
    lo, hi = seat_err[int(0.05 * n)], seat_err[int(0.95 * n)]
    misses = [(x['state'], round(p, 2), round(x['actual'], 1)) for p, x in zip(probs, rows)
              if (p >= 0.5) != (x['actual'] > 0)]
    return dict(n_races=len(rows), brier=brier, naive=naive, pred=mean_pred, lo=lo, hi=hi, actual=actual_d,
                misses=misses, inside=lo <= actual_d <= hi,
                calib=calibration(probs, [x['actual'] > 0 for x in rows]))


def calibration(probs, outs):
    bins = [(0.0, 0.1), (0.1, 0.35), (0.35, 0.65), (0.65, 0.9), (0.9, 1.01)]
    out = []
    for a, b in bins:
        sel = [(p, o) for p, o in zip(probs, outs) if a <= p < b]
        if sel:
            out.append((a, b, len(sel), st.mean(p for p, _ in sel), st.mean(o for _, o in sel)))
    return out


# ---------------------------------------------------------------------------------------------- environment
def env_rules():
    """Two-years-out rules for the presidential margin, scored on 1992-2024."""
    rows = []
    for y in (1992, 1996, 2000, 2004, 2008, 2012, 2016, 2020, 2024):
        mid, prev, act = NAT_HOUSE[y - 2], NAT_PRES[y - 4], NAT_PRES[y]
        rows.append((y, mid, prev, act))
    rules = {'Midterm House margin': lambda mid, prev: mid,
             'Previous presidential margin': lambda mid, prev: prev,
             'Average of the two': lambda mid, prev: (mid + prev) / 2,
             'Even (0)': lambda mid, prev: 0.0}
    res = {}
    for name, f in rules.items():
        err = [act - f(mid, prev) for y, mid, prev, act in rows]
        res[name] = (math.sqrt(st.mean(e * e for e in err)), st.mean(err), f(NAT_HOUSE[2026], NAT_PRES[2024]))
    return rows, res


def midterm_rule_errors():
    out = []
    for y in (2006, 2010, 2014, 2018, 2022, 2026):
        hist = [midterm_swing(z) for z in MIDTERMS if z < y]
        prev = {2006: -2.6, 2010: 10.6, 2014: 1.4, 2018: -0.9, 2022: 3.0, 2026: -2.5}[y]   # House vote two years before
        sign = -1 if PRES_PARTY[y] == 'D' else 1
        pred = prev + sign * st.mean(hist)
        out.append((y, pred, NAT_HOUSE[y], NAT_HOUSE[y] - pred, st.stdev(hist)))
    return out


def env_prior(target):
    """Ex-ante environment for a back-test year, by the same rules (midterm swing; average rule)."""
    if target in (2018, 2022):
        y, pred, act, err, sd = [x for x in midterm_rule_errors() if x[0] == target][0]
        return pred, sd
    rows, res = env_rules()
    prior_rows = [r for r in rows if r[0] < target]
    err = [act - (mid + prev) / 2 for y, mid, prev, act in prior_rows]
    sd = math.sqrt(st.mean(e * e for e in err))
    return (NAT_HOUSE[target - 2] + NAT_PRES[target - 4]) / 2, sd


# ---------------------------------------------------------------------------------------------- House
def house_backtest(target, env_house, env_sd=0.0, n=20000, seed=2):
    """Re-fit the curve on the previous election (seats, House vote) and predict target's seats."""
    prev = target - 2
    spread = hm.fit_spread()
    b = NAT_HOUSE[prev] - hm.inv_phi(HOUSE_SEATS_D[prev] / hm.SEATS) * spread
    rng = random.Random(seed)
    seats = []
    for _ in range(n):
        e = env_house + (rng.gauss(0, env_sd) if env_sd else 0.0)
        s = hm.SEATS * hm.phi((e - b) / spread) + rng.gauss(0, hm.PARAMS['sd_seats'])
        seats.append(s)
    seats.sort()
    act = HOUSE_SEATS_D[target]
    p_maj = sum(1 for s in seats if s >= hm.MAJORITY) / n
    return dict(b=b, pred=st.mean(seats), lo=seats[int(0.05 * n)], hi=seats[int(0.95 * n)], actual=act,
                p_maj=p_maj, brier=(p_maj - (act >= hm.MAJORITY)) ** 2)


# ---------------------------------------------------------------------------------------------- report
def fmt(x):
    return sm.fmt_pct(x)


def envs(e):
    return 'D+%.1f' % e if e >= 0 else 'R+%.1f' % -e


def report(n=4000):
    L = []
    w = L.append
    w('# Model credibility outputs (generated)\n')
    w('Role: the tables `tools/backtest.py --write` produces, read by `model-credibility.md`. Status: generated; do not '
      'edit by hand. This project\'s own back-test of its scenario models, seeded.\n')
    w('## 1. Senate back-test, with only what was known two years earlier\n')
    w('A: given the actual national environment (tests the state-level structure). B: with the environment drawn '
      'from a two-years-out rule (section 3), as the 2028 model does. Races without a Democrat-v-Republican contest, '
      'Maine and Vermont are left out.\n')
    w('| Year | Races | Environment used (A; B mean ± SD) | Brier, A | Brier, B | Naive (last presidential winner) | D seats predicted, A (90%) | B (90%) | Actual | Wrong calls in A |')
    w('| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |')
    allA, allB, alln = [], [], []
    for y in (2018, 2020, 2022, 2024):
        env_a = NAT_HOUSE[y] if y in (2018, 2022) else NAT_PRES[y]
        mu, sd = env_prior(y)
        a = senate_backtest(y, env_a, n=n)
        b = senate_backtest(y, mu, env_sd=sd, n=n, seed=3)
        allA.append((a['brier'], a['n_races']))
        allB.append((b['brier'], b['n_races']))
        alln.append((a['naive'], a['n_races']))
        w('| %d | %d | %s; %s ± %.1f | %.3f | %.3f | %.3f | %.1f (%d-%d) | %.1f (%d-%d) | %d | %s |' % (
            y, a['n_races'], envs(env_a), envs(mu), sd, a['brier'], b['brier'], a['naive'], a['pred'], a['lo'], a['hi'],
            b['pred'], b['lo'], b['hi'], a['actual'], ', '.join('%s (%.2f; actual %+.1f)' % m for m in a['misses']) or 'none'))
    tw = sum(k for _, k in allA)
    w('\nPooled Brier: A %.3f, B %.3f, naive %.3f (lower is better; always saying 50%% scores 0.250).\n' % (
        sum(b * k for b, k in allA) / tw, sum(b * k for b, k in allB) / tw, sum(b * k for b, k in alln) / tw))
    probs, outs = [], []
    w('Calibration, A, all four years pooled (predicted band: races, mean predicted, share Democrats won):\n')
    pooled = {}
    for y in (2018, 2020, 2022, 2024):
        env_a = NAT_HOUSE[y] if y in (2018, 2022) else NAT_PRES[y]
        for a_, b_, k, mp, mo in senate_backtest(y, env_a, n=n)['calib']:
            pp = pooled.setdefault((a_, b_), [0, 0.0, 0.0])
            pp[0] += k
            pp[1] += mp * k
            pp[2] += mo * k
    w('| Band | Races | Mean predicted P(D) | Share won by D |')
    w('| --- | --- | --- | --- |')
    for (a_, b_), (k, sp, so) in sorted(pooled.items()):
        w('| %d-%d%% | %d | %s | %s |' % (a_ * 100, min(100, b_ * 100), k, fmt(sp / k), fmt(so / k)))
    w('\n## 2. House back-test\n')
    w('The curve re-fitted on the previous election\'s seats and House vote (same spread as `house_model.py`), then given '
      'the actual House vote (A) or the two-years-out rule (B).\n')
    w('| Year | Implied break-even | Predicted D seats, A (90%) | P(D majority), A | Predicted, B (90%) | P(D majority), B | Actual D seats |')
    w('| --- | --- | --- | --- | --- | --- | --- |')
    for y in (2018, 2020, 2022, 2024):
        mu, sd = env_prior(y)
        mu_h = mu if y in (2018, 2022) else mu - 0.8   # House vote has run about 0.8 behind the presidential margin since 2004
        a = house_backtest(y, NAT_HOUSE[y])
        b = house_backtest(y, mu_h, env_sd=math.hypot(sd, 1.5))
        w('| %d | %s | %.0f (%.0f-%.0f) | %s | %.0f (%.0f-%.0f) | %s | %d |' % (
            y, envs(a['b']), a['pred'], a['lo'], a['hi'], fmt(a['p_maj']), b['pred'], b['lo'], b['hi'], fmt(b['p_maj']),
            a['actual']))
    w('\n## 3. The national environment two years out\n')
    rows, res = env_rules()
    w('Presidential years 1992-2024: the margin two years before the election, by four simple rules.\n')
    w('| Rule | Error (RMSE, points) | Mean error (actual minus rule) | What it gives for 2028 |')
    w('| --- | --- | --- | --- |')
    for name, (rmse, me, v28) in res.items():
        w('| %s | %.1f | %+.1f | %s |' % (name, rmse, me, envs(v28)))
    w('\nThis project\'s 2028 prior: D+3.0 with SD 4.5.\n')
    w('Midterm rule (the previous House vote moved against the president\'s party by the mean of earlier '
      'midterm swings):\n')
    w('| Midterm | Rule | Actual House vote | Error | SD of earlier swings |')
    w('| --- | --- | --- | --- | --- |')
    for y, pred, act, err, sd in midterm_rule_errors():
        w('| %d | %s | %s | %+.1f | %.1f |' % (y, envs(pred), envs(act), err, sd))
    w('\n## 4. How much the headline numbers move with the prior\n')
    w('Center and spread of the 2028 national environment (Democratic presidential margin):\n')
    import redistricting_2030 as rd
    w('| Prior | P(D president) | P(55+ Senate seats) | P(D House 2029) | P(trifecta) | P(D House 2033), no DEM-2 / with Titles I-II (D president) |')
    w('| --- | --- | --- | --- | --- | --- |')
    for mu, sd in ((0.0, 4.5), (1.5, 4.5), (3.0, 3.0), (3.0, 4.5), (3.0, 6.0), (4.5, 4.5), (5.7, 4.5), (7.0, 4.5)):
        o = sm.simulate_2028(mu, n=8000, seed=41, env_sd=sd)
        s = sm.summarize(o)
        runs = hm.simulate(mu, n=8000, seed=41, env_sd=sd)
        hsum = hm.summary(runs)
        r = rd.summarize(rd.simulate(env28=mu, env_sd=sd, n=8000, seed=41), 'D')
        w('| D+%.1f, SD %.1f | %s | %s | %s | %s | %s / %s |' % (mu, sd, fmt(sum(o['dpres']) / o['n']), fmt(s['p55']),
                                                               fmt(hsum['house']), fmt(hsum['trifecta']),
                                                               fmt(r['h_without']), fmt(r['h_with'])))
    w('\n## 5. The back-test bias, and what it would mean for 2028\n')
    w('A uniform shift toward Democrats in every back-test race (mode A) that would remove the Senate seat bias:\n')
    w('| Shift (points) | Predicted D seats, four classes | Actual | Pooled Brier |')
    w('| --- | --- | --- | --- |')
    for c in (0, 1, 2, 3, 4):
        tot = br = nr = 0
        act = 0
        for y in (2018, 2020, 2022, 2024):
            env_a = NAT_HOUSE[y] if y in (2018, 2022) else NAT_PRES[y]
            r = senate_backtest(y, env_a, n=n, prm={'bias': c})
            tot += r['pred']
            act += r['actual']
            br += r['brier'] * r['n_races']
            nr += r['n_races']
        w('| %+d | %.1f | %d | %.3f |' % (c, tot, act, br / nr))
    w('\nIf the same shift applied to 2028 (evidence-weighted prior; every 2028 race moved toward Democrats):\n')
    w('| Shift | Mean D seats, Jan 2029 | P(55+) | P(60+) | With a D president: mean, P(55+) |')
    w('| --- | --- | --- | --- | --- |')
    for c in (0.0, 2.0, 4.0):
        ov = {k: c for k in sm.RACES}
        o = sm.simulate_2028(3.0, n=8000, seed=43, env_sd=4.5, overrides=ov)
        s = sm.summarize(o)
        d = sm.summarize(o, 'D')
        w('| %+.0f | %.1f | %s | %s | %.1f, %s |' % (c, s['mean'], fmt(s['p55']), fmt(s['p60']), d['mean'], fmt(d['p55'])))
    return '\n'.join(L) + '\n'


if __name__ == '__main__':
    text = report()
    if '--write' in sys.argv:
        path = os.path.join(HERE, '..', 'model-credibility-outputs.md')
        with open(path, 'w') as fh:
            fh.write(text)
        print('wrote', os.path.normpath(path))
    else:
        print(text)
