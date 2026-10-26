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
# In-window revenue per enforcement dollar, all CBO, for funding spread over a ten-year window:
# 2024 $20B rescission of enforcement (2.2), 2020 $40B (2.58) and $20B (3.05) exam/collection increases.
ENF_RATIOS = {'low': 2.2, 'mid': 2.58, 'high': 3.05}
IRA_RATIO, IRA_ENF_SHARE = 180.4 / 79.6, 45.6 / 78.9   # CBO memo yield on the whole IRA package; its enforcement share
LAGS = (1, 2)   # years before an enforcement dollar yields; bounds the back-loading of this path
AGENCIES = list(OLD)


def factor(y):
    return RAMP.get(y, 1.0) * (1 + GROWTH) ** (y - 2026)


def num(x):
    return float(x) if x not in ('', None) else None


def load():
    rows = [r for r in csv.DictReader(open(CSV)) if r['row_type'] == 'proposal']
    z = lambda: [0, 0, 0]
    out = {a: {'surge': z(), 'rate': z(), 'enf_rate': z(), 'cash29': z(), 'oblig29': z(), 'unpriced': []} for a in AGENCIES}
    fees = {}
    for r in rows:
        a, env = r['agency'], r['envelope']
        mid = num(r['value'])
        if env == 'program_row':
            fees[r['component']] = (num(r['low']), mid, num(r['high']), r['unit'])
            continue
        if mid is None:
            out[a]['unpriced'].append(r['component'])
            continue
        trio = [num(r['low']), mid, num(r['high'])]
        keys = {'surge': ['surge'], 'sustained': ['rate'],
                'fy2029': ['cash29' if r['measure'] == 'cash' else 'oblig29']}[env]
        if r.get('revenue_role') == 'enforcement':
            keys = keys + ['enf_rate']
        for key in keys:
            out[a][key] = [s + v for s, v in zip(out[a][key], trio)]
    return out, fees


def lagged_yield(rate, ratio, lag):
    """In-window revenue from an enforcement path, $B. A flat ten-year program at this lag yields ratio x funding
    inside the window, so the steady multiple is ratio x 10 / (10 - lag)."""
    m = ratio * 10 / (10 - lag)
    return m * sum(rate * factor(y) for y in YEARS if y + lag <= 2039)


def main():
    adopt = json.load(open(ADOPT))['spending']
    surge_env, sust_env = adopt['cap_surge_tn'] * 1000, adopt['cap_sustained_tn'] * 1000
    fsum = sum(factor(y) for y in YEARS)
    (data, fees), res = load(), {}
    for a, d in data.items():
        sust = [r * fsum for r in d['rate']]
        share = OLD[a] / 600
        res[a] = {'surge': d['surge'], 'sustained': sust, 'total': [s + t for s, t in zip(d['surge'], sust)],
                  'fy2040_rate': [r * (1 + GROWTH) ** 14 for r in d['rate']],
                  'old_total': OLD[a] + 490 * share, 'pro_rata_new': share * (surge_env + sust_env),
                  'unpriced': d['unpriced']}
    tot = {k: [sum(res[a][k][i] for a in AGENCIES) for i in range(3)] for k in ('surge', 'sustained', 'total', 'fy2040_rate')}
    irs, enf = res['IRS']['total'], data['IRS']['enf_rate']
    enf_total = [r * fsum for r in enf]
    enf_yield = {lag: {k: lagged_yield(enf[i], v, lag) / 1000 for i, (k, v) in enumerate(ENF_RATIOS.items())} for lag in LAGS}
    mix = enf_total[1] / irs[1]
    g8 = {'enforcement_bn': enf_total, 'support_bn': [t - e for t, e in zip(irs, enf_total)], 'enforcement_share': mix,
          'enforcement_yield_tn': enf_yield,
          'ira_mix_adjusted_tn': irs[1] * IRA_RATIO * mix / IRA_ENF_SHARE / 1000,
          'ira_unadjusted_tn': irs[1] * IRA_RATIO / 1000,
          'enforcement_needed_bn': {f'{t}T': {k: t * 1000 / v for k, v in ENF_RATIOS.items()} for t in (0.1, 0.2)}}
    fy29 = {k: [sum(data[a][k][i] for a in AGENCIES) for i in range(3)] for k in ('cash29', 'oblig29')}
    path = {y: round(sum(data[a]['rate'][1] for a in AGENCIES) * factor(y), 2) for y in YEARS}
    out = {'agencies': res, 'totals': tot, 'envelopes_bn': {'surge': surge_env, 'sustained': sust_env},
           'remainder_bn': {'surge': surge_env - tot['surge'][1], 'sustained': sust_env - tot['sustained'][1]},
           'g8': g8, 'fy2029_bn': fy29, 'program_row_fees': fees, 'sustained_path_mid_bn': path, 'factor_sum': fsum}
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
    print(f"\nIRS split, FY2030-39: enforcement {f(g8['enforcement_bn'])}; support (service, systems, payments) {f(g8['support_bn'])}; enforcement share {g8['enforcement_share']:.0%} (IRA: {IRA_ENF_SHARE:.0%}).")
    for lag, y in g8['enforcement_yield_tn'].items():
        print(f"REV-G8 from the enforcement row only, {lag}-year lag, CBO ratios 2.2/2.58/3.05 on low/mid/high funding: ${y['low']:.3f}T / ${y['mid']:.3f}T / ${y['high']:.3f}T.")
    print(f"Cross-check, IRA package ratio on the whole IRS total: ${g8['ira_unadjusted_tn']:.3f}T unadjusted; ${g8['ira_mix_adjusted_tn']:.3f}T adjusted to this mix.")
    for t, d in g8['enforcement_needed_bn'].items():
        print(f"Enforcement funding needed for ${t} at CBO ratios (no extra lag): ${d['high']:.0f}-{d['low']:.0f}B.")
    c, o = fy29['cash29'], fy29['oblig29']
    print(f"\nFY2029, four agencies: cash {f(c)}; obligations {f(o)}; against the $10B of surge cash shifted to FY2029.")
    for k, (l, m, h, u) in fees.items():
        print(f"Program row: {k}: {m} {u}" + (f" ({l}-{h})" if l is not None else ''))
    print('\nFour-agency sustained path, midpoint, $B nominal: ' + ', '.join(f'FY{k} {v}' for k, v in path.items()))


if __name__ == '__main__':
    main()
