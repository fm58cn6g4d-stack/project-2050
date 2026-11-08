#!/usr/bin/env python3
"""A small state-by-state 2028 presidential model that shares the Senate model's national swing.

Role: the arithmetic behind dossiers/scenario/presidential-model-2028.md. Status: exploratory (stage B,
November 8, 2026); not a forecast and not a core model. It is built on, not forked from, the Senate model
in tools/senate_model.py (PR #82 and #84, session_01UQzgBuURXjhGUqdQTkebmN): it imports that model's state
leans (lean(): 2020 and 2024 presidential margins and 2026 statewide results, each against the national
margin), its regions and its national-error size, and it reads the national presidential margin of each
Senate-model run, so a presidency and a Senate drawn in the same run share one national swing.

Method. In each run the state's Democratic margin = lean(s) + P + R[region] + e_s, where P is the
national presidential margin of that Senate-model run (environment E plus the national error, sd_nat),
R is a regional error (sd_reg, drawn here, independent of the Senate model's own regional draw) and e_s
a state error (SD_STATE, an ASSUMPTION; tested 2-4). Electors are the 2020 apportionment, used in 2024
and 2028 [SRC-1051]; Maine and Nebraska are treated as winner-take-all (an approximation of +/-1
elector each; their district electors are not modeled). DC is safe Democratic.

  python3 dossiers/scenario/tools/presidential_2028.py           (standard library only; about a minute)
  python3 dossiers/scenario/tools/presidential_2028.py --quick   (fewer runs, for a check)
"""
import os
import random
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import senate_model as sm  # noqa: E402

EV = {
    'AL': 9, 'AK': 3, 'AZ': 11, 'AR': 6, 'CA': 54, 'CO': 10, 'CT': 7, 'DE': 3, 'DC': 3, 'FL': 30, 'GA': 16,
    'HI': 4, 'ID': 4, 'IL': 19, 'IN': 11, 'IA': 6, 'KS': 6, 'KY': 8, 'LA': 8, 'ME': 4, 'MD': 10, 'MA': 11,
    'MI': 15, 'MN': 10, 'MS': 6, 'MO': 10, 'MT': 4, 'NE': 5, 'NV': 6, 'NH': 4, 'NJ': 14, 'NM': 5, 'NY': 28,
    'NC': 16, 'ND': 3, 'OH': 17, 'OK': 7, 'OR': 8, 'PA': 19, 'RI': 4, 'SC': 9, 'SD': 3, 'TN': 11, 'TX': 40,
    'UT': 6, 'VT': 3, 'VA': 13, 'WA': 12, 'WV': 4, 'WI': 10, 'WY': 3,
}
assert sum(EV.values()) == 538
SD_STATE = 3.0   # ASSUMPTION: state error around lean + national + regional; tested 2-4
STATES = sorted(s for s in EV if s != 'DC')


def leans(prm=None):
    prm = dict(sm.BASE_PARAMS, **(prm or {}))
    return {s: sm.lean(s, prm) for s in STATES}


def ec_run(pres, ln, rng, sd_state=SD_STATE, sd_reg=None):
    """One Electoral College outcome given the national presidential margin pres."""
    sd_reg = sm.BASE_PARAMS['sd_reg'] if sd_reg is None else sd_reg
    reg = {r: rng.gauss(0, sd_reg) for r in sorted(sm.REGION)}
    m = {s: ln[s] + pres + reg[sm.REGION_OF[s]] + rng.gauss(0, sd_state) for s in STATES}
    d_ev = EV['DC'] + sum(EV[s] for s in STATES if m[s] > 0)
    acc, tip = EV['DC'], None
    for s in sorted(STATES, key=lambda s: -m[s]):
        acc += EV[s]
        if acc >= 270:
            tip = s
            break
    return d_ev, tip


def joint(env, n, seed=2028, prm=None, sd_state=SD_STATE, env_sd=0.0):
    """Run the Senate model at environment env and an Electoral College on each run's national margin."""
    out = sm.simulate_2028(env, n=n, seed=seed, prm=prm, env_sd=env_sd)
    ln = leans(prm)
    rng = random.Random(seed + 7)
    res = dict(n=n, dwin=0, tips={}, ctrl_d=0, ctrl_r=0, dwins=0, rwins=0, rule_agree=0, d_ev=[])
    for i in range(n):
        d_ev, tip = ec_run(out['env'][i], ln, rng, sd_state=sd_state)
        dwin = d_ev >= 270
        res['d_ev'].append(d_ev)
        res['tips'][tip] = res['tips'].get(tip, 0) + 1
        seats = out['seats'][i]
        ctrl = seats >= 51 or (seats == 50 and dwin)   # the Vice President breaks a 50-50 tie
        if dwin:
            res['dwin'] += 1
            res['ctrl_d'] += ctrl
        else:
            res['ctrl_r'] += ctrl
        res['rule_agree'] += (dwin == out['dpres'][i])
    return res


def ec_only(env, n, seed=11, prm=None, sd_state=SD_STATE):
    """P(Democratic Electoral College win) at environment env, without the Senate model."""
    prm = dict(sm.BASE_PARAMS, **(prm or {}))
    ln = leans(prm)
    rng = random.Random(seed)
    wins = 0
    for _ in range(n):
        pres = env + rng.gauss(0, prm['sd_nat'])
        wins += ec_run(pres, ln, rng, sd_state=sd_state)[0] >= 270
    return wins / n


def break_even(n, prm=None, sd_state=SD_STATE):
    """National margin at which P(D win) = 50%: the implied Electoral College bias."""
    lo, hi = -4.0, 6.0
    for _ in range(14):
        mid = (lo + hi) / 2
        if ec_only(mid, n, seed=13, prm=prm, sd_state=sd_state) < 0.5:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def pct(x):
    return '%d%%' % round(100 * x) if 0.005 <= x <= 0.995 else ('<1%' if x < 0.005 else '>99%')


def main():
    quick = '--quick' in sys.argv
    n = 4000 if quick else 20000
    nb = 2000 if quick else 6000
    print('# 2028 presidential model: outputs (n = %d per row, seeded)\n' % n)
    ln = leans()
    print('## 1. State leans (D margin relative to the nation, points; from senate_model.lean)\n')
    lp = leans({'w26': 0.0})
    close = sorted(STATES, key=lambda s: abs(ln[s] - 1.0))[:12]
    print('| State | Electors | Lean (base) | Lean (presidential results only) |\n| --- | --- | --- | --- |')
    for s in sorted(close, key=lambda s: -ln[s]):
        print('| %s | %d | %+.1f | %+.1f |' % (s, EV[s], ln[s], lp[s]))
    print('\n## 2. By national environment (shared national swing with the Senate model)\n')
    print('| Environment | P(D wins the Electoral College) | Mean D electors | Top tipping-point states | '
          'P(D Senate control), D president | P(D Senate control), R president | '
          'Runs where the Senate model\'s ec_bias rule picks the same winner |')
    print('| --- | --- | --- | --- | --- | --- | --- |')
    for env, esd in ((-3.0, 0.0), (0.0, 0.0), (3.0, 0.0), (6.0, 0.0), (3.0, 4.5)):
        r = joint(env, n, env_sd=esd)
        dw = r['dwin'] / n
        tips = sorted(r['tips'].items(), key=lambda kv: -kv[1])[:4]
        tip_s = ', '.join('%s %s' % (k, pct(v / n)) for k, v in tips)
        cd = r['ctrl_d'] / r['dwin'] if r['dwin'] else float('nan')
        cr = r['ctrl_r'] / (n - r['dwin']) if n - r['dwin'] else float('nan')
        label = {-3.0: 'R+3', 0.0: 'Neutral', 3.0: 'D+3', 6.0: 'D+6'}[env]
        if esd:
            label = 'Evidence-weighted (D+3, SD 4.5), as in the Senate model'
        print('| %s | %s | %.0f | %s | %s | %s | %s |' % (label, pct(dw), sum(r['d_ev']) / n, tip_s,
                                                          pct(cd), pct(cr), pct(r['rule_agree'] / n)))
    print('\nThe tipping-point shares do not depend on the environment: with a uniform national swing, the order '
          'of states is set by lean and the regional and state errors alone.')
    print('\n## 3. Implied Electoral College bias (national margin where P(D win) = 50%)\n')
    print('| Case | Break-even D margin |\n| --- | --- |')
    for label, prm, sds in (('Base (Senate-model leans, state SD 3)', None, SD_STATE),
                            ('State SD 2', None, 2.0), ('State SD 4', None, 4.0),
                            ('Presidential leans only (2026 weight 0)', {'w26': 0.0}, SD_STATE),
                            ('2026 weight 0.45', {'w26': 0.45}, SD_STATE)):
        print('| %s | %+.1f |' % (label, break_even(nb, prm=prm, sd_state=sds)))


if __name__ == '__main__':
    main()
