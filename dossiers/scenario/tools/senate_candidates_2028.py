#!/usr/bin/env python3
"""How sensitive each 2028 Senate race is to candidate quality (for `2028-senate-candidates.md`).

Uses `senate_model.simulate_2028` unchanged, through its `overrides` argument (extra points toward D in one
race). It does not re-tune the model: it measures what a candidate-quality shift of a given size would do,
so b-3 can decide later whether to add a nominee-quality term.

  python3 senate_candidates_2028.py           # prints the tables (markdown)
  python3 senate_candidates_2028.py --quick   # fewer runs, for a smoke test

Standard library only; seeded, so the output is reproducible.
"""
import sys

import senate_model as sm

RACES = ['NH', 'GA', 'NV', 'PA', 'AZ', 'NC', 'WI', 'OH', 'IA', 'AK', 'FL', 'KS']
ENVS = [('neutral', 0.0), ('D+3', 3.0)]
SHIFT = 2.0  # points toward D in one race; the per-point slope is (shift result - base) / SHIFT


def control(out):
    """P(Democratic Senate control): 51+ seats, or 50 with a Democratic Vice President."""
    n = out['n']
    return sum(1 for s, d in zip(out['seats'], out['dpres']) if s >= 51 or (s == 50 and d)) / n


def p55(out):
    """P(55 or more Democratic-caucus seats), the project's filibuster-relevant threshold."""
    return sum(1 for x in out['seats'] if x >= 55) / out['n']


def mean_seats(out):
    return sum(out['seats']) / out['n']


def p_win(out, k):
    return out['wins'][k] / out['n']


def run(n):
    rows = []
    for name, env in ENVS:
        base = sm.simulate_2028(env, n=n, seed=2028)
        for k in RACES + ['ALL']:
            keys = [r for r in RACES if r not in ('KS',)] if k == 'ALL' else [k]
            up = sm.simulate_2028(env, n=n, seed=2028, overrides={x: SHIFT for x in keys})
            dn = sm.simulate_2028(env, n=n, seed=2028, overrides={x: -SHIFT for x in keys})
            rows.append(dict(env=name, race=k,
                             p=p_win(base, k) if k != 'ALL' else None,
                             p_up=p_win(up, k) if k != 'ALL' else None,
                             p_dn=p_win(dn, k) if k != 'ALL' else None,
                             ctrl=control(base), c_up=control(up), c_dn=control(dn),
                             f=p55(base), f_up=p55(up), f_dn=p55(dn),
                             s=mean_seats(base), s_up=mean_seats(up), s_dn=mean_seats(dn)))
    return rows


def pct(x):
    return '%d%%' % round(100 * x) if 0.005 <= x <= 0.995 else ('<1%' if x < 0.005 else '>99%')


def pts(x):
    return '%+.1f' % (100 * x)


def main():
    n = 4000 if '--quick' in sys.argv else 20000
    rows = run(n)
    print('# 2028 Senate candidate-quality sensitivity (n = %d per row, seeded)\n' % n)
    print('A shift of %.0f points toward the Democrat (+) or the Republican (-) in one race at a time, with' % SHIFT)
    print('everything else as in `senate_model.py`. Alaska runs through the model\'s branch logic, so its')
    print('shift applies to the underlying margin. 55+ = Democratic-caucus seats; "seats per point" is the change')
    print('in expected seats per point of shift. The last row shifts every listed race but Kansas together.\n')
    for name, _ in ENVS:
        sub = [r for r in rows if r['env'] == name]
        b = sub[0]
        print('## Environment: %s (base: control %s, 55+ seats %s, mean %.1f seats)\n' % (
            name, pct(b['ctrl']), pct(b['f']), b['s']))
        print('| Race | P(D) at -2 / base / +2 | Race odds per point | P(55+) at -2 / +2 | P(55+) per point | Seats per point |')
        print('| --- | --- | --- | --- | --- | --- |')
        races = sorted([r for r in sub if r['race'] != 'ALL'], key=lambda r: -(r['f_up'] - r['f_dn']))
        for r in races + [r for r in sub if r['race'] == 'ALL']:
            if r['race'] == 'ALL':
                label, odds = '**All but KS at once**', '-'
                pd = '-'
            else:
                label = r['race']
                pd = '%s / %s / %s' % (pct(r['p_dn']), pct(r['p']), pct(r['p_up']))
                odds = '%s pts' % pts((r['p_up'] - r['p_dn']) / (2 * SHIFT))
            print('| %s | %s | %s | %s / %s | %s pts | %+.2f |' % (
                label, pd, odds, pct(r['f_dn']), pct(r['f_up']),
                pts((r['f_up'] - r['f_dn']) / (2 * SHIFT)), (r['s_up'] - r['s_dn']) / (2 * SHIFT)))
        print()


if __name__ == '__main__':
    main()
