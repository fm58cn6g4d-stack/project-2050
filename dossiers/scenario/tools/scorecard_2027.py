#!/usr/bin/env python3
"""The pre-registered 2027 scorecard: what each November 2027 result should be if 2028 is on track for D+3.0,
and how far each result moves the 2028 environment estimate and the plan's headline odds.

Role: the arithmetic behind dossiers/scenario/2027-scorecard.md. Status: exploratory scenario model (stage B,
November 8, 2026); this project's own analysis, not a forecast. The rule is fixed now, before any 2027 result,
so that the November 2027 update is mechanical rather than a judgment made after the fact. ASSUMPTIONS are
marked; the ranges tested are in the sensitivity section.

How it works (all margins are Democratic minus Republican, in points):
  1. "On track" for each contest = the state's expected 2028 presidential margin at D+3.0 (senate_model.lean
     + 3.0), plus how far that kind of off-year contest has run ahead of the state's next presidential result
     (the "off-year excess", from 2015-2023 data below).
  2. The deviation of each 2027 result from on-track is averaged, weighting each contest by its precision.
  3. The 2028 prior (D+3.0, SD 4.5) moves by k times that average, where k is a Bayesian gain: 0.40 when the
     full slate reports (ASSUMPTION, calibrated in section 2 of the outputs), less for one contest alone.
  4. The moved prior is run through senate_model, house_model and redistricting_2030 unchanged.

Run:
  python3 dossiers/scenario/tools/scorecard_2027.py            print the tables
  python3 dossiers/scenario/tools/scorecard_2027.py --write    regenerate dossiers/scenario/2027-scorecard-outputs.md
"""
import contextlib
import math
import os
import statistics as st
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import senate_model as sm  # noqa: E402
import house_model as hm  # noqa: E402
import redistricting_2030 as rd  # noqa: E402

PRIOR_MEAN = 3.0      # published evidence-weighted prior (senate_model.PRIOR)
PRIOR_SD = 4.5
NAT = {2012: 3.86, 2016: 2.09, 2018: 8.56, 2020: sm.NAT[2020], 2022: sm.NAT[2022], 2024: sm.NAT[2024],
       2026: sm.NAT[2026]}   # presidential margins; House vote in 2018, 2022, 2026 [SRC-0600] [SRC-1070] [SRC-0570]
PRES = {2012: {'KY': -22.69, 'LA': -17.21, 'MS': -11.5, 'VA': 3.87, 'NJ': 17.72},
        2016: {'KY': -29.84, 'LA': -19.64, 'MS': -17.83, 'VA': 5.32, 'NJ': 14.10, 'PA': -0.72, 'WI': -0.76},
        2020: sm.P20, 2024: sm.P24}   # state presidential margins [SRC-0600] [SRC-0575] [SRC-0459]

# --------------------------------------------------------------------------------------------------
# 1. Calibration data: off-year results and the next cycle
# --------------------------------------------------------------------------------------------------
# Virginia and New Jersey governors (D margin) [SRC-1071] [SRC-1072] [SRC-1073] [SRC-1074] [SRC-1075] [SRC-1076].
VA_NJ = {2017: {'VA': 8.91, 'NJ': 14.14}, 2021: {'VA': -1.94, 'NJ': 3.22}, 2025: {'VA': 15.36, 'NJ': 14.36}}
# Kentucky, Louisiana, Mississippi governors (D margin), the year before a presidential election [SRC-1077]
# [SRC-1078] [SRC-1079] [SRC-1080] [SRC-1081] [SRC-1082] [SRC-1083] [SRC-1084]. Louisiana 2023 was decided
# in the all-candidate primary (Landry 51.6%) and has no two-candidate margin.
SOUTH = {2015: {'KY': -8.71, 'LA': 12.22, 'MS': -33.86}, 2019: {'KY': 0.37, 'LA': 2.66, 'MS': -5.08},
         2023: {'KY': 5.07, 'MS': -3.24}}
# Special-election average: Democratic margin minus the district's last presidential margin, every D-vs-R
# special in the calendar year with D + R at 90% or more, from the committed series specials-2017-2026.csv
# (The Downballot's trackers, extracted by tools/specials_extract.py) [SRC-1092].
SPECIALS_CSV = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'specials-2017-2026.csv')


def load_specials(path=SPECIALS_CSV):
    with open(path) as f:
        import csv
        return [r for r in csv.DictReader(line for line in f if not line.startswith('#'))]


def specials_by_year(rows=None):
    """{year: (races counted, average swing)} from the committed series."""
    out = {}
    for r in rows or load_specials():
        if r['counted'] == 'yes':
            out.setdefault(int(r['year']), []).append(float(r['swing']))
    return {y: (len(v), st.mean(v)) for y, v in sorted(out.items())}


SPECIALS = {y: a for y, (n, a) in specials_by_year().items() if y % 2 == 1}   # the off-years


def ols(xs, ys):
    mx, my = st.mean(xs), st.mean(ys)
    sxx = sum((x - mx) ** 2 for x in xs)
    b = sum((x - mx) * (y - my) for x, y in zip(xs, ys)) / sxx
    return b, my - b * mx


def calibration():
    """Rows (off-year, signal, next-cycle national change) for midterm and presidential targets."""
    mid = []
    for y, res in VA_NJ.items():
        prev = y - 1
        swing = st.mean(res[s] - PRES[prev][s] for s in res)
        mid.append((y, swing, SPECIALS.get(y), NAT[y + 1] - NAT[prev]))
    pres = []
    for y, res in SOUTH.items():
        prev = y - 3
        swing = st.mean(res[s] - PRES[prev][s] for s in res)
        pres.append((y, swing, SPECIALS.get(y), NAT[y + 1] - NAT[prev]))
    return mid, pres


# --------------------------------------------------------------------------------------------------
# 2. The off-year excess: how far each kind of contest runs ahead of the state's next presidential result
# --------------------------------------------------------------------------------------------------
# Non-governor statewide contests the spring or fall before a presidential election (D or liberal margin):
# Wisconsin Supreme Court April 2019 (Hagedorn 50.22, Neubauer 49.72) and April 2023 (Protasiewicz 55.43,
# Kelly 44.39) [SRC-1089] [SRC-1090]; Pennsylvania Supreme Court November 2023 (McCaffery 53, Carluccio 47,
# unofficial) [SRC-1091].
COURTS = [('WI', 2019, -0.50, 2020), ('WI', 2023, 11.04, 2024), ('PA', 2023, 6.0, 2024)]
G = st.mean(m - PRES[nxt][s] for s, y, m, nxt in COURTS)   # about +6.2
INC_GOV = sm.BASE_PARAMS['inc_gov']     # 3.0, removed when an incumbent governor ran
SHRINK = sm.BASE_PARAMS['shrink']       # 0.4: share of a state's own governor excess that carries over
# Specials' excess over the next national change, before each presidential year with data (2019, 2023): the
# rule uses their mean. Before the three midterms it was smaller (shown in the outputs, section 2).
PRES_YEARS = (2019, 2023)
SPECIALS_EXCESS = st.mean(SPECIALS[y] - (NAT[y + 1] - NAT[y - 3]) for y in PRES_YEARS)
GOV_INC = {('KY', 2019): 'R', ('KY', 2023): 'D', ('LA', 2019): 'D', ('MS', 2015): 'R', ('MS', 2023): 'R'}


def governor_excess(s):
    """Each past governor race's excess over the state's next presidential margin, incumbency removed."""
    out = []
    for y, res in SOUTH.items():
        if s in res:
            adj = {'D': -INC_GOV, 'R': INC_GOV, None: 0.0}[GOV_INC.get((s, y))]
            out.append(res[s] - PRES[y + 1][s] + adj)
    return out


def gov_x(s):
    v = governor_excess(s)
    return G + SHRINK * (st.mean(v) - G)


# --------------------------------------------------------------------------------------------------
# 3. The 2027 contests and their on-track benchmarks
# --------------------------------------------------------------------------------------------------
SD_STATE = math.sqrt(sm.BASE_PARAMS['sd_race'] ** 2 + sm.BASE_PARAMS['sd_open'] ** 2 + sm.BASE_PARAMS['sd_reg'] ** 2)
# Contest noise, SD in points (ASSUMPTIONS): the Senate special uses the Senate model's open-seat and regional
# errors; courts add the spread of their off-year excess; governors are candidate-driven; the specials average
# pools dozens of races but each cycle's excess varies.
CONTESTS = [
    # key, label, date, kind, state, sigma
    ('MN', 'Minnesota U.S. Senate special', 'Nov 2', 'senate', 'MN', SD_STATE),
    ('PA', 'Pennsylvania Supreme Court, open seat', 'Nov 2', 'court', 'PA', 7.0),
    ('WI', 'Wisconsin Supreme Court (only if a conservative runs)', 'Apr 6', 'court', 'WI', 7.0),
    ('KY', 'Kentucky governor (open D seat)', 'Nov 2', 'gov', 'KY', 9.0),
    ('MS', 'Mississippi governor (open R seat)', 'Nov 2', 'gov', 'MS', 9.0),
    ('LA', 'Louisiana governor (runoff, if a Democrat makes it)', 'Nov 20', 'gov', 'LA', 9.0),
    ('SP', 'Special-election average, all of 2027 (vs. Harris 2024)', 'all year', 'specials', None, 5.0),
]
LABEL = {c[0]: c[1] for c in CONTESTS}
SIGMA = {c[0]: c[5] for c in CONTESTS}
MN_APPOINTEE = 1.0   # as in senate_model.p_mn_2027


def on_track(key, env=PRIOR_MEAN):
    """The result consistent with a 2028 environment `env` (D margin)."""
    kind = [c for c in CONTESTS if c[0] == key][0]
    k, s = kind[3], kind[4]
    if k == 'specials':
        return (env - NAT[2024]) + SPECIALS_EXCESS
    base = sm.lean(s) + env
    if k == 'senate':
        return base + G + MN_APPOINTEE
    if k == 'court':
        return base + G
    return base + gov_x(s)


# The gain: TAU is the shared noise in translating a 2027 off-year reading into a 2028 presidential
# environment. ASSUMPTION: set so that the full slate gets gain K_FULL = 0.40 (section 2 of the outputs).
K_FULL = 0.40


def tau_for(k_full=K_FULL, keys=None):
    keys = keys or [c[0] for c in CONTESTS]
    v = PRIOR_SD ** 2
    pooled = 1.0 / sum(1.0 / SIGMA[k] ** 2 for k in keys)
    return math.sqrt(max(0.0, v / k_full - v - pooled))


TAU = tau_for()


def update(devs, k_full=K_FULL):
    """devs maps contest key -> deviation from on-track (points). Returns (mean, sd, gain, signal)."""
    if not devs:
        return PRIOR_MEAN, PRIOR_SD, 0.0, 0.0
    tau = tau_for(k_full)
    w = {k: 1.0 / SIGMA[k] ** 2 for k in devs}
    sw = sum(w.values())
    signal = sum(w[k] * d for k, d in devs.items()) / sw
    v = PRIOR_SD ** 2
    gain = v / (v + tau ** 2 + 1.0 / sw)
    return PRIOR_MEAN + gain * signal, math.sqrt((1 - gain) * v), gain, signal


def move_per_point(key, alone=False):
    """Points of 2028 environment per point of this contest's deviation (full slate, or alone)."""
    if alone:
        return update({key: 1.0})[0] - PRIOR_MEAN
    keys = [c[0] for c in CONTESTS]
    w = {k: 1.0 / SIGMA[k] ** 2 for k in keys}
    return update({k: 0.0 for k in keys})[2] * w[key] / sum(w.values())


# --------------------------------------------------------------------------------------------------
# 4. From a moved prior to the headline odds
# --------------------------------------------------------------------------------------------------
@contextlib.contextmanager
def fixed(mn=None, ny=None, va_senate=None):
    """Temporarily fix 2027 outcomes the models carry as probabilities."""
    unc = dict(sm.UNCERTAIN_NOT_UP)
    ny_key = 'New York redraw (2027 referendum)'
    mc = dict(hm.MAP_CHANGES)
    p_ny, p_va = rd.P_NY_REFERENDUM, rd.P_VA_AMENDMENT
    try:
        if mn is not None:
            sm.UNCERTAIN_NOT_UP['MN-2027'] = 1.0 if mn else 0.0
        if ny is not None:
            hm.MAP_CHANGES[ny_key] = (1.0 if ny else 0.0, mc[ny_key][1])
            rd.P_NY_REFERENDUM = 1.0 if ny else 0.0
        if va_senate is not None:
            # ASSUMPTION: the 0.25 restart chance already prices a 60% chance of holding the Senate; holding it
            # raises the chance to 0.40, losing it ends the 2031 restart.
            rd.P_VA_AMENDMENT = 0.40 if va_senate else 0.0
        yield
    finally:
        sm.UNCERTAIN_NOT_UP.clear()
        sm.UNCERTAIN_NOT_UP.update(unc)
        hm.MAP_CHANGES.clear()
        hm.MAP_CHANGES.update(mc)
        rd.P_NY_REFERENDUM, rd.P_VA_AMENDMENT = p_ny, p_va


def metrics(env, sd, n=20000, seed=2027, **fix):
    with fixed(**fix):
        h = hm.summary(hm.simulate(env, n=n, seed=seed, env_sd=sd))
        o = sm.simulate_2028(env, n=n, seed=seed, env_sd=sd)
        s_all, s_d = sm.summarize(o), sm.summarize(o, 'D')
        r = rd.summarize(rd.simulate(env, sd, n=n // 2, seed=seed), None)
    return dict(trifecta=h['trifecta'], p55=s_all['p55'], p55_d=s_d['p55'],
                mean_d=s_d['mean'], house33=r['h_without'], house33_t2=r['h_with'], p_dpres=s_d['share'])


def p_senate_band(env, sd, lo, hi, n=20000, seed=2027, **fix):
    """P(lo <= Democratic seats <= hi | Democratic president) and P(seats >= lo | D president)."""
    with fixed(**fix):
        o = sm.simulate_2028(env, n=n, seed=seed, env_sd=sd)
    idx = [i for i in range(n) if o['dpres'][i]]
    seats = [o['seats'][i] for i in idx]
    return (sum(lo <= s <= hi for s in seats) / len(seats), sum(s >= lo for s in seats) / len(seats),
            st.mean(seats), len(idx) / n, sm.d2f_summary(o, 'D')['p_pass'])


# --------------------------------------------------------------------------------------------------
# 5. Report
# --------------------------------------------------------------------------------------------------
def fmt(x):
    return sm.fmt_pct(x)


def mg(x):
    return 'D+%.1f' % x if x >= 0 else 'R+%.1f' % -x


def slate(delta, mn_floor=True):
    """Every numeric contest `delta` points from on-track; MN held unless its result is below zero."""
    devs = {c[0]: delta for c in CONTESTS if c[0] != 'WI'}
    mn = on_track('MN') + delta > 0
    return devs, mn


def report(n=20000):
    L = []
    w = L.append
    w('# 2027 scorecard outputs (generated)\n')
    w('Role: the tables `tools/scorecard_2027.py --write` produces, read by `2027-scorecard.md`. Status: generated; '
      'do not edit by hand. This project\'s exploratory scenario arithmetic, not a forecast. Headline odds come from '
      '`senate_model.py`, `house_model.py` and `redistricting_2030.py` run unchanged at the moved prior; n = %d '
      'runs per row (half that for the 2033 House), seeded.\n' % n)

    w('## 1. On-track benchmarks for D+3.0, and how far each result moves the 2028 estimate\n')
    w('Off-year excess (how far a contest ran ahead of the state\'s next presidential margin): courts and other '
      'non-governor statewide races %+.1f on average; specials %+.1f over the next presidential change (the '
      'mean of 2019 and 2023, section 2). Governor races keep %.0f%% of their own state\'s excess beyond '
      'that.\n' % (G, SPECIALS_EXCESS, 100 * SHRINK))
    w('| Contest | Date | Lean (vs nation) | On track for D+3.0 | On track for Even / D+6 | Noise SD | Move in 2028 estimate per point above track: full slate / alone |')
    w('| --- | --- | --- | --- | --- | --- | --- |')
    for key, label, date, kind, s, sig in CONTESTS:
        ln = '—' if s is None else mg(sm.lean(s))
        w('| %s | %s | %s | %s | %s / %s | %.1f | %.2f / %.2f |' % (
            label, date, ln, mg(on_track(key)), mg(on_track(key, 0.0)), mg(on_track(key, 6.0)), sig,
            move_per_point(key), move_per_point(key, alone=True)))
    for s in ('KY', 'MS', 'LA'):
        v = governor_excess(s)
        w('\n%s governor excess by race, incumbency removed: %s; carried over: %+.1f.' % (
            s, ', '.join('%+.1f' % x for x in v), gov_x(s)))
    w('\nTranslation noise (shared by every 2027 contest) TAU = %.1f points; full-slate gain %.2f; posterior SD '
      'after the full slate %.1f (from %.1f).\n' % (TAU, K_FULL, update({c[0]: 0.0 for c in CONTESTS})[1], PRIOR_SD))

    w('## 2. Calibration: did off-year results predict the next cycle?\n')
    mid, pres = calibration()
    w('Signal = average Democratic gain over the state\'s previous presidential margin (governor races), and the '
      'calendar-year special-election average from `specials-2017-2026.csv`. Next change = next national result '
      'minus the previous presidential margin.\n')
    w('| Off-year | Target | Governor-race swing | Specials average | Next national change |')
    w('| --- | --- | --- | --- | --- |')
    for y, swing, sp, nxt in mid:
        w('| %d (VA, NJ) | %d midterm | %+.1f | %s | %+.1f |' % (y, y + 1, swing, '—' if sp is None else '%+.1f' % sp, nxt))
    for y, swing, sp, nxt in pres:
        w('| %d (%s) | %d presidential | %+.1f | %s | %+.1f |' % (y, ', '.join(SOUTH[y]), y + 1, swing,
                                                                  '—' if sp is None else '%+.1f' % sp, nxt))
    bm, am = ols([r[1] for r in mid], [r[3] for r in mid])
    bs, as_ = ols([r[2] for r in mid], [r[3] for r in mid])
    bp, ap = ols([r[1] for r in pres], [r[3] for r in pres])
    resid = [r[3] - (am + bm * r[1]) for r in mid]
    w('\nFits: before midterms, next change = %+.1f + %.2f x governor swing (residuals %s); specials, slope %.2f. '
      'Before presidential years, slope %.2f: no usable relation, and in 2023 the sign was wrong.\n' % (
          am, bm, ', '.join('%+.1f' % r for r in resid), bs, bp))
    w('**The special-election series** (every counted D-vs-R special, by calendar year; swing against the last '
      'presidential margin in the district):\n')
    w('| Year | Races | Average swing | Next national change | Excess (swing minus next change) |')
    w('| --- | --- | --- | --- | --- |')
    for y, (cnt, avg) in specials_by_year().items():
        nxt = {2017: NAT[2018] - NAT[2016], 2019: NAT[2020] - NAT[2016], 2021: NAT[2022] - NAT[2020],
               2023: NAT[2024] - NAT[2020], 2025: NAT[2026] - NAT[2024]}.get(y)
        w('| %d | %d | %+.1f | %s | %s |' % (y, cnt, avg, '—' if nxt is None else '%+.1f' % nxt,
                                            '—' if nxt is None else '%+.1f' % (avg - nxt)))
    rows = load_specials()
    c2526 = [float(r['swing']) for r in rows if r['cycle'] == '2025-26' and r['counted'] == 'yes']
    w('\n2025-26 cycle: %d counted races, average swing %+.1f against Harris 2024. The specials benchmark for D+3.0 '
      'is the 2028 change from 2024 (%+.1f) plus the presidential-year excess (%+.1f) = %s.\n' % (
          len(c2526), st.mean(c2526), PRIOR_MEAN - NAT[2024], SPECIALS_EXCESS,
          'Harris %+.1f' % on_track('SP')))
    w('Gain sensitivity (same contests, all on track except a 5-point miss across the board):\n')
    w('| Full-slate gain k | Implied TAU | 2028 estimate after a 5-point miss | Posterior SD |')
    w('| --- | --- | --- | --- |')
    for k in (0.2, 0.4, 0.7):
        m, sd, g, _ = update({c[0]: -5.0 for c in CONTESTS if c[0] != 'WI'}, k_full=k)
        w('| %.1f%s | %.1f | %s | %.1f |' % (k, ' (pre-registered)' if k == K_FULL else '', tau_for(k), mg(m), sd))

    w('\n## 3. What each reading of 2027 does to the plan\'s odds\n')
    w('"Across the board" moves every numeric contest by the same amount (Wisconsin left out). Minnesota is fixed '
      'held or lost by its own result; New York and Virginia stay at their current probabilities.\n')
    w('| 2027 reading | 2028 estimate (SD) | Minnesota | P(trifecta) | P(55+ Senate) | P(55+), D president | Mean seats, D president | P(D House 2033), no DEM-2 / with |')
    w('| --- | --- | --- | --- | --- | --- | --- | --- |')
    base = metrics(PRIOR_MEAN, PRIOR_SD, n=n)
    w('| Today, before any 2027 result | %s (%.1f) | 90%% | %s | %s | %s | %.1f | %s / %s |' % (
        mg(PRIOR_MEAN), PRIOR_SD, fmt(base['trifecta']), fmt(base['p55']), fmt(base['p55_d']), base['mean_d'],
        fmt(base['house33']), fmt(base['house33_t2'])))
    for delta, label in ((10, '10 points ahead of track'), (5, '5 ahead'), (0, 'On track'), (-5, '5 behind'),
                         (-10, '10 behind'), (-15, '15 behind (a 2021-sized turn)')):
        devs, mn = slate(delta)
        m, sd, g, sig = update(devs)
        x = metrics(m, sd, n=n, mn=mn)
        w('| %s | %s (%.1f) | %s | %s | %s | %s | %.1f | %s / %s |' % (
            label, mg(m), sd, 'held' if mn else 'lost', fmt(x['trifecta']), fmt(x['p55']), fmt(x['p55_d']),
            x['mean_d'], fmt(x['house33']), fmt(x['house33_t2'])))

    w('\n**Single results, the rest on track.**\n')
    w('| Result | 2028 estimate | P(trifecta) | P(55+ Senate) | P(D House 2033), no DEM-2 |')
    w('| --- | --- | --- | --- | --- |')
    allk = [c[0] for c in CONTESTS if c[0] != 'WI']
    mn_t = on_track('MN')
    rows = [
        ('Minnesota held by 20 (%s above track)' % ('%.0f' % (20 - mn_t)), {'MN': 20 - mn_t}, dict(mn=True)),
        ('Minnesota held by 3', {'MN': 3 - mn_t}, dict(mn=True)),
        ('Minnesota lost by 2', {'MN': -2 - mn_t}, dict(mn=False)),
        ('Kentucky lost by 15', {'KY': -15 - on_track('KY')}, dict(mn=True)),
        ('Mississippi won by 3', {'MS': 3 - on_track('MS')}, dict(mn=True)),
        ('Specials average only Harris +5', {'SP': 5 - on_track('SP')}, dict(mn=True)),
        ('Specials average Harris +18', {'SP': 18 - on_track('SP')}, dict(mn=True)),
        ('New York referendum passes', {}, dict(mn=True, ny=True)),
        ('New York referendum fails', {}, dict(mn=True, ny=False)),
        ('Virginia Senate lost (21-19 flips)', {}, dict(mn=True, va_senate=False)),
        ('New York fails and Virginia Senate lost', {}, dict(mn=True, ny=False, va_senate=False)),
    ]
    for label, d, fx in rows:
        devs = {k: 0.0 for k in allk}
        devs.update(d)
        m, sd, g, _ = update(devs)
        x = metrics(m, sd, n=n, **fx)
        w('| %s | %s | %s | %s | %s |' % (label, mg(m), fmt(x['trifecta']), fmt(x['p55']), fmt(x['house33'])))

    w('\n## 4. Plan-change tests\n')
    w('Option B (#80) plans for a 53-56 Senate. With a Democratic president: P(53-56), P(53+), mean seats and '
      'P(D2-F has the votes, the round-4 whip count); and P(Democratic president) itself:\n')
    w('| Case | P(53-56) | P(53+) | Mean seats | P(D2-F has the votes) | P(D president) |')
    w('| --- | --- | --- | --- | --- | --- |')
    for label, env, sd, fx in (('Today (D+3.0, SD 4.5)', 3.0, 4.5, {}),
                               ('2027 on track, Minnesota held', *update({k: 0.0 for k in allk})[:2], dict(mn=True)),
                               ('Minnesota lost and mid-2028 environment D+1 (SD 3)', 1.0, 3.0, dict(mn=False)),
                               ('Minnesota lost and mid-2028 environment Even (SD 3)', 0.0, 3.0, dict(mn=False)),
                               ('Minnesota lost and mid-2028 environment R+3 (SD 3)', -3.0, 3.0, dict(mn=False)),
                               ('Minnesota held and mid-2028 environment D+6 (SD 3)', 6.0, 3.0, dict(mn=True))):
        a, b, c, d, f = p_senate_band(env, sd, 53, 56, n=n, **fx)
        w('| %s | %s | %s | %.1f | %s | %s |' % (label, fmt(a), fmt(b), c, fmt(f), fmt(d)))
    w('\nHow far the environment would have to fall before a Democratic president\'s Senate drops below option B '
      '(Minnesota lost, environment known to SD 2): mean seats and P(53+), by environment:\n')
    envs = (-6.0, -4.0, -2.0, 0.0, 2.0)
    w('| Environment | ' + ' | '.join(mg(e) for e in envs) + ' |')
    w('| --- |' + ' --- |' * len(envs))
    cells = [p_senate_band(e, 2.0, 53, 56, n=n, mn=False) for e in envs]
    w('| Mean seats, D president | ' + ' | '.join('%.1f' % c[2] for c in cells) + ' |')
    w('| P(53+), D president | ' + ' | '.join(fmt(c[1]) for c in cells) + ' |')
    w('| P(D president) | ' + ' | '.join(fmt(c[3]) for c in cells) + ' |')
    return '\n'.join(L) + '\n'


if __name__ == '__main__':
    text = report()
    if '--write' in sys.argv:
        path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '2027-scorecard-outputs.md')
        with open(path, 'w') as fh:
            fh.write(text)
        print('wrote', os.path.normpath(path))
    else:
        print(text)
