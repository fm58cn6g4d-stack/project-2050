"""Capacity review: add up sources/capacity-recovery-components.csv for IRS, CMS, HUD and ED.

Reads the proposal rows, turns annual run rates (FY2026 dollars) into FY2030-39 nominal totals,
compares them with the approved envelopes and the old pro-rata shares, and tests REV-G8's yield.
Prints a markdown report; --json prints the numbers. Reads only; writes nothing.
"""
import csv, json, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
CSV = ROOT / 'sources' / 'capacity-recovery-components.csv'
ADOPT = ROOT / 'index' / 'data' / 'inputs' / 'recovery-adoption.json'

YEARS = range(2030, 2040)
GROWTH = 0.035                     # estimate: federal pay and prices, nominal, a year from FY2026
RAMP = {2030: 0.5, 2031: 0.8}      # estimate: hiring takes two years; 1.0 afterward
OLD = {'IRS': 130, 'CMS': 50, 'HUD': 45, 'ED': 40}   # domain-capacity.md historical split of $600B (unsourced)
CBO_RATIOS = {'low': 2.2, 'mid': 2.27, 'high': 3.05}  # revenue per IRS funding dollar: CBO 2024 rescission, IRA memo, CBO 2020 $20B
AGENCIES = list(OLD)


def factor(y):
    return RAMP.get(y, 1.0) * (1 + GROWTH) ** (y - 2026)


def num(x):
    return float(x) if x not in ('', None) else None


def load():
    rows = [r for r in csv.DictReader(open(CSV)) if r['row_type'] == 'proposal']
    out = {a: {'surge': [0, 0, 0], 'rate': [0, 0, 0], 'unpriced': []} for a in AGENCIES}
    for r in rows:
        a, env = r['agency'], r['envelope']
        mid = num(r['value'])
        if mid is None:
            out[a]['unpriced'].append(r['component'])
            continue
        trio = [num(r['low']), mid, num(r['high'])]
        key = 'surge' if env == 'surge' else 'rate'
        out[a][key] = [s + v for s, v in zip(out[a][key], trio)]
    return out


def main():
    adopt = json.load(open(ADOPT))['spending']
    surge_env, sust_env = adopt['cap_surge_tn'] * 1000, adopt['cap_sustained_tn'] * 1000
    fsum = sum(factor(y) for y in YEARS)
    data, res = load(), {}
    for a, d in data.items():
        sust = [r * fsum for r in d['rate']]
        share = OLD[a] / 600
        res[a] = {'surge': d['surge'], 'sustained': sust, 'total': [s + t for s, t in zip(d['surge'], sust)],
                  'fy2040_rate': [r * (1 + GROWTH) ** 14 for r in d['rate']],
                  'old_total': OLD[a] + 490 * share, 'pro_rata_new': share * (surge_env + sust_env),
                  'unpriced': d['unpriced']}
    tot = {k: [sum(res[a][k][i] for a in AGENCIES) for i in range(3)] for k in ('surge', 'sustained', 'total', 'fy2040_rate')}
    irs = res['IRS']['total']
    g8 = {'yield_tn': {k: irs[1] * v / 1000 for k, v in CBO_RATIOS.items()},
          'yield_range_tn': [irs[0] * CBO_RATIOS['low'] / 1000, irs[2] * CBO_RATIOS['high'] / 1000],
          'funding_needed_bn': {f'{t}T': {k: t * 1000 / v for k, v in CBO_RATIOS.items()} for t in (0.2, 0.4)}}
    path = {y: round(sum(data[a]['rate'][1] for a in AGENCIES) * factor(y), 2) for y in YEARS}
    out = {'agencies': res, 'totals': tot, 'envelopes_bn': {'surge': surge_env, 'sustained': sust_env},
           'remainder_bn': {'surge': surge_env - tot['surge'][1], 'sustained': sust_env - tot['sustained'][1]},
           'g8': g8, 'sustained_path_mid_bn': path, 'factor_sum': fsum}
    if '--json' in sys.argv:
        print(json.dumps(out, indent=1, default=str))
        return
    f = lambda t: f'{t[1]:.1f} ({t[0]:.1f}-{t[2]:.1f})'
    print('| Agency | Surge, lifetime | Sustained, FY2030-39 | Total | FY2040 run rate | Old allocation | Pro rata of $300B+$300B | Unpriced items |')
    print('| --- | --- | --- | --- | --- | --- | --- | --- |')
    for a in AGENCIES:
        r = res[a]
        print(f"| {a} | {f(r['surge'])} | {f(r['sustained'])} | {f(r['total'])} | {f(r['fy2040_rate'])} | {r['old_total']:.1f} | {r['pro_rata_new']:.1f} | {len(r['unpriced'])} |")
    print(f"| **Four agencies** | {f(tot['surge'])} | {f(tot['sustained'])} | {f(tot['total'])} | {f(tot['fy2040_rate'])} | {sum(res[a]['old_total'] for a in AGENCIES):.1f} | {sum(res[a]['pro_rata_new'] for a in AGENCIES):.1f} | |")
    print(f"\nRemainder at the midpoint for other agencies: surge ${out['remainder_bn']['surge']:.0f}B, sustained ${out['remainder_bn']['sustained']:.0f}B.")
    print(f"Run-rate factor FY2030-39 (ramp x growth from FY2026): {fsum:.2f}.")
    y = g8['yield_tn']
    print(f"\nREV-G8 at CBO-convention yields on the IRS total: mid ${y['mid']:.2f}T (ratio range on the mid ${y['low']:.2f}-{y['high']:.2f}T; full range ${g8['yield_range_tn'][0]:.2f}-{g8['yield_range_tn'][1]:.2f}T).")
    for t, d in g8['funding_needed_bn'].items():
        print(f"IRS funding needed for G8 = ${t}: ${d['high']:.0f}-{d['low']:.0f}B (mid ratio ${d['mid']:.0f}B).")
    print('\nFour-agency sustained path, midpoint, $B nominal: ' + ', '.join(f'FY{k} {v}' for k, v in path.items()))


if __name__ == '__main__':
    main()
