#!/usr/bin/env python3
"""Who holds the 2031 redistricting pens, and what DEM-2 Titles I-II are worth on the 2032 House maps.

Role: the arithmetic behind dossiers/scenario/redistricting-2030-model.md. Status: exploratory scenario model
(stage B, November 8, 2026); this project's own analysis, not a forecast. It complements, and does not repeat,
the qualitative state ranking in compounding-redistricting.md (PR #86), whose per-state partisan swings it uses.

Method. Each run of senate_model.simulate_chain gives a 2028 presidency and the 2030 and 2032 national
environments (the 2030 midterm swing against the president's party is drawn from 1990-2026). For each of
twelve states the 2030 offices that decide the maps (governor, chambers) are won or lost on that shared 2030
environment plus a regional error and an office error. A state's pen is Democratic or Republican if one party
holds every office the map needs, and neutral otherwise (a court, a commission or a deadlock). A Democratic pen
moves the state's 2032 House delegation by +g seats against a neutral map, a Republican pen by -g, where 2g is
the D-drawn-to-R-drawn swing in #86's table. The national House in 2032 is the house_model.py curve at the 2032
environment, built on geography alone, plus every state's partisan map effect. DEM-2's Title II (federal
criteria with a partisan-fairness standard, enforceable in court) shrinks every partisan effect by a share f;
Title I (the mid-decade ban) does not touch the decennial 2031 maps and is valued separately.

  python3 dossiers/scenario/tools/redistricting_2030.py            print the tables
  python3 dossiers/scenario/tools/redistricting_2030.py --write    regenerate redistricting-2030-outputs.md
"""
import math
import os
import random
import statistics as st
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import senate_model as sm  # noqa: E402
import house_model as hm   # noqa: E402

# --------------------------------------------------------------------------------------------------
# Inputs. Seats after the 2030 census and partisan swings (D-drawn minus R-drawn map) follow #86's table
# (compounding-redistricting.md, section 4), midpoints of its ranges; AZ, NV and VA are this project's
# assumptions (AZ and MI draw by independent commission). Break-even environments B (the national D margin
# at which Democrats have an even chance of the office in 2030) are ASSUMPTIONS, derived as stated in the
# dossier: governors from the state's lean and incumbency; chambers from their 2022-26 results.
# --------------------------------------------------------------------------------------------------
STATES = {
    # state: seats, swing (D map minus R map), rule, offices {name: B}
    'TX': (42, 10.0, 'all', {'gov': 5.6, 'house': 9.0, 'senate': 18.0}),
    'FL': (31, 6.5, 'all', {'gov': 14.6, 'house': 20.0, 'senate': 20.0}),
    'NC': (15, 5.5, 'all', {'house': 10.0, 'senate': 13.5}),          # no governor's veto over maps
    'PA': (16, 5.0, 'all', {'gov': -1.1, 'house': -2.5, 'senate': 10.0}),
    'GA': (14, 4.5, 'all', {'gov': -2.0, 'house': 12.5, 'senate': 15.0}),
    'OH': (15, 5.0, 'all', {'gov': 6.1, 'legislature': 18.0}),        # a D governor forces a bipartisan or commission map
    'WI': (8, 2.5, 'all', {'gov': -1.1, 'assembly': 4.0, 'senate': 4.0}),
    'NV': (4, 1.5, 'all', {'gov': -1.1, 'legislature': -4.0}),
    'MI': (13, 0.0, 'commission', {}),
    'AZ': (10, 0.0, 'commission', {}),
    'VA': (11, 3.0, 'virginia', {}),   # commission unless a 2028-29 amendment passes; elected 2029, not 2030
    'NY': (24, 6.0, 'newyork', {}),    # legislature draws by simple majority only if the 2027 referendum passes
}
P_NY_REFERENDUM = 0.45   # as in house_model.MAP_CHANGES
P_VA_AMENDMENT = 0.25    # ASSUMPTION: a restart of the voided amendment passes in time for 2031
SD_GOV = 7.0             # office error for a governor's race (governor races stray about 4 points further
SD_CHAMBER = 5.0         # from partisan lean than Senate races [SRC-0589]); chambers are map-anchored
# Partisan map effects in the other 38 states, in Democratic seats (negative = net Republican), fixed by who
# already holds the pens there (ASSUMPTION): D-drawn IL, MD, OR, NM about +6; R-drawn TN, LA, AL, SC, IN, MO,
# KY, KS, UT, MS about -10. The PNAS study of the 2021 maps found partisan effects of +8.6 R and +6.2 D seats
# nationally, a net of about 2 Republican (compounding-redistricting.md, section 2).
REST_NET = -4.0
REST_SD = 2.0
B_GEO = 1.9   # ASSUMPTION: break-even from geography alone, i.e. the 2026 lines' 3.0 less about 1.1 points
              # (about 4 seats) of net Republican partisan effects on those lines
F_TITLE2 = 0.65  # ASSUMPTION: share of each partisan effect that Title II's criteria remove (0.4-0.85 tested)


def office_win(B, e30, reg, rng, sd):
    return e30 + reg + rng.gauss(0, sd) > B


def pen(state, e30, reg, rng):
    seats, swing, rule, offices = STATES[state]
    if rule == 'commission':
        return 'N'
    if rule == 'newyork':
        return 'D' if rng.random() < P_NY_REFERENDUM else 'N'
    if rule == 'virginia':
        return 'D' if rng.random() < P_VA_AMENDMENT else 'N'
    wins = [office_win(B, e30, reg, rng, SD_GOV if name == 'gov' else SD_CHAMBER) for name, B in offices.items()]
    if all(wins):
        return 'D'
    if not any(wins):
        return 'R'
    return 'N'


def simulate(env28=3.0, env_sd=4.5, n=20000, seed=2031, f=F_TITLE2, b_geo=B_GEO, rest=REST_NET, geo_cut=0.0):
    """Returns per-run dicts: pres28, pens, partisan effect, 2032 D seats with and without Title II."""
    res = sm.simulate_chain(env28, n=n, seed=seed, env_sd=env_sd)
    rng = random.Random(seed + 3)
    spread = hm.fit_spread()
    regions = sorted(sm.REGION)
    runs = []
    for i in range(res['kept']):
        e30 = res['e30'][i]
        e32 = res['e32'][i]
        reg = {r: rng.gauss(0, sm.BASE_PARAMS['sd_reg']) for r in regions}
        pens = {s: pen(s, e30, reg[sm.REGION_OF[s]], rng) for s in STATES}
        eff12 = sum(STATES[s][1] / 2 * (1 if p == 'D' else -1 if p == 'R' else 0) for s, p in pens.items())
        eff_rest = rest + rng.gauss(0, REST_SD)
        eff = eff12 + eff_rest
        e_house = e32 + rng.gauss(0, hm.PARAMS['sd_house'])
        noise = rng.gauss(0, hm.PARAMS['sd_seats'])
        base = hm.SEATS * hm.phi((e_house - b_geo) / spread)
        base_t2 = hm.SEATS * hm.phi((e_house - b_geo * (1 - geo_cut)) / spread)
        without = base + eff + noise
        with_t2 = base_t2 + (1 - f) * eff + noise
        runs.append(dict(dp28=res['dpres28'][i], e30=e30, e32=e32, pens=pens, eff=eff, eff12=eff12,
                         without=without, with_t2=with_t2))
    return runs


def summarize(runs, cond):
    rr = [r for r in runs if cond is None or r['dp28'] == (cond == 'D')]
    m = len(rr)
    out = dict(n=m, e30=st.mean(r['e30'] for r in rr), e32=st.mean(r['e32'] for r in rr))
    out['pens'] = {s: tuple(sum(1 for r in rr if r['pens'][s] == k) / m for k in 'DNR') for s in STATES}
    out['eff'] = st.mean(r['eff'] for r in rr)
    out['eff12'] = st.mean(r['eff12'] for r in rr)
    out['without'] = st.mean(r['without'] for r in rr)
    out['with'] = st.mean(r['with_t2'] for r in rr)
    vals = sorted(r['with_t2'] - r['without'] for r in rr)
    out['value'] = st.mean(vals)
    out['v10'] = vals[int(0.1 * m)]
    out['v90'] = vals[int(0.9 * m)]
    out['h_without'] = sum(r['without'] >= hm.MAJORITY for r in rr) / m
    out['h_with'] = sum(r['with_t2'] >= hm.MAJORITY for r in rr) / m
    return out


def fmt(x):
    return sm.fmt_pct(x)


def report(n=20000):
    L = []
    w = L.append
    w('# Redistricting model outputs (generated)\n')
    w('Role: the tables `tools/redistricting_2030.py --write` produces, read by `redistricting-2030-model.md`. Status: '
      'generated; do not edit by hand. This project\'s exploratory scenario arithmetic, not a forecast. Runs come from '
      '`senate_model.simulate_chain` (evidence-weighted 2028 environment, D+3 with SD 4.5), n = %d, seeded.\n' % n)
    runs = simulate(n=n)
    S = {c: summarize(runs, c) for c in ('D', 'R')}
    w('## 1. Who holds the 2031 pens\n')
    w('Share of runs in which each state\'s 2031 congressional map is Democratic-drawn / neutral (court, commission, '
      'deadlock) / Republican-drawn. Average 2030 environment: %s with a Democratic president, %s with a Republican '
      'president.\n' % (envs(S['D']['e30']), envs(S['R']['e30'])))
    w('| State | Seats | Swing (D map − R map) | Democratic president: D / N / R | Republican president: D / N / R |')
    w('| --- | --- | --- | --- | --- |')
    for s, (seats, swing, rule, _) in STATES.items():
        a = S['D']['pens'][s]
        b = S['R']['pens'][s]
        w('| %s | %d | %.1f | %s / %s / %s | %s / %s / %s |' % (s, seats, swing, *map(fmt, a), *map(fmt, b)))
    w('\n## 2. The 2032 House maps, with and without DEM-2 Titles I-II\n')
    w('| 2028 president | Net partisan map effect, 12 states (D seats) | Net, all states | Expected D House seats 2032, no DEM-2 | With Titles I-II | Value of Titles I-II (10th-90th percentile) | P(D House 2033), no DEM-2 | With |')
    w('| --- | --- | --- | --- | --- | --- | --- | --- |')
    for c in ('D', 'R'):
        s = S[c]
        w('| %s | %+.1f | %+.1f | %.0f | %.0f | %+.1f (%+.1f to %+.1f) | %s | %s |' % (
            'Democratic' if c == 'D' else 'Republican', s['eff12'], s['eff'], s['without'], s['with'], s['value'],
            s['v10'], s['v90'], fmt(s['h_without']), fmt(s['h_with'])))
    w('\nAverage 2032 environment: %s (Democratic president elected 2028), %s (Republican). ' % (
        envs(S['D']['e32']), envs(S['R']['e32'])) + 'Title I (the mid-decade ban) does not change the decennial 2031 '
      'maps, so the 2032 value is Title II\'s; Title I\'s value is in section 4.\n')
    w('## 3. Sensitivity (Democratic president)\n')
    w('| Change | Value of Titles I-II, D seats 2032 | P(D House 2033): without / with |')
    w('| --- | --- | --- |')
    for label, kw in [('Base (f = 0.65)', {}), ('Title II removes 40%', {'f': 0.40}), ('Title II removes 85%', {'f': 0.85}),
                      ('Rest-of-country net effect 0', {'rest': 0.0}), ('Rest-of-country net effect -8', {'rest': -8.0}),
                      ('Partisan-fairness standard also cuts geographic bias by a quarter', {'geo_cut': 0.25}),
                      ('2028 environment neutral (SD 2)', {'env28': 0.0, 'env_sd': 2.0})]:
        s = summarize(simulate(n=n // 2, seed=7, **kw), 'D')
        w('| %s | %+.1f | %s / %s |' % (label, s['value'], fmt(s['h_without']), fmt(s['h_with'])))
    w('\n## 4. Title I, the mid-decade ban\n')
    w('Title I matters after the 2031 maps: it stops a party that gains a trifecta in 2032-36 from redrawing again '
      'before 2041, as in 2025-26. Illustration (ASSUMPTION): without the ban, a mid-decade round happens in a given '
      'cycle with probability 0.5, moving each redrawing state by a quarter of its swing toward the party in power. '
      'The 2025-26 round moved little net (most Republican redraws were offset or backfired, per #86), so its expected '
      'seat value is near zero and its main effect is on variance:\n')
    rng = random.Random(4)
    moves = []
    for _ in range(20000):
        m = 0.0
        if rng.random() < 0.5:
            for s, (seats, swing, rule, _) in STATES.items():
                if rule in ('all',) and rng.random() < 0.5:
                    m += (swing / 4) * (1 if rng.random() < 0.5 else -1)
        moves.append(m)
    moves.sort()
    w('Mid-decade move without Title I: mean %+.1f seats, 10th-90th percentile %+.1f to %+.1f; with Title I: 0.\n' % (
        st.mean(moves), moves[2000], moves[18000]))
    return '\n'.join(L) + '\n'


def envs(e):
    return 'D+%.1f' % e if e >= 0 else 'R+%.1f' % -e


if __name__ == '__main__':
    text = report()
    if '--write' in sys.argv:
        path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'redistricting-2030-outputs.md')
        with open(path, 'w') as fh:
            fh.write(text)
        print('wrote', os.path.normpath(path))
    else:
        print(text)
