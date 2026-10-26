"""Capacity review: add up sources/capacity-recovery-components.csv for every reviewed CAP-7 agency.

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
RAMP = {2030: 0.5, 2031: 0.8}      # estimate: hiring takes two years; 1.0 afterward. A row's ramp column overrides it
# domain-capacity.md historical split of $600B (unsourced). Batch 4 items (State, civil rights, CAISI, ATF/NICS and
# USCIS's asylum $6B) were proposals against its $37B reserve.
OLD = {'IRS': 130, 'CMS': 50, 'HUD': 45, 'ED': 40, 'SSA': 55, 'USCIS': 46, 'DEV': 60, 'STATE': 8, 'CDC': 15,
       'FEMA': 8, 'NOAA': 40, 'FTA': 30, 'EPA': 5, 'DOE': 4, 'DOL': 6, 'NLRB': 4, 'FTC-DOJ': 3, 'INTEGRITY': 12,
       'FEC': 3, 'EAC': 3, 'OPM': 10, 'CIVIL-RIGHTS': 6, 'CAISI': 6, 'ATF-NICS': 5}
OLD_UNLISTED = 37 - 31   # reserve not proposed for any batch 4 item
# In-window revenue per enforcement dollar for funding spread over a ten-year window. CBO: 2024 $20B
# rescission of enforcement 2.2; 2020 exam/collection increases 3.05 at $20B and 2.58 at $40B. Returns fall
# with scale, so for an enforcement row near $60B the mid is 2.3 (extrapolated from CBO's two 2020 points)
# and the high is CBO's $40B ratio.
ENF_RATIOS = {'low': 2.2, 'mid': 2.3, 'high': 2.58}
IRA_RATIO, IRA_ENF_SHARE = 180.4 / 79.6, 45.6 / 78.9   # CBO memo yield on the whole IRA package; its enforcement share
LAGS = (1, 2)   # years before an enforcement dollar yields; bounds the back-loading of this path


AGENCIES = []
layers = {}   # (envelope, layer) -> [low, mid, high] in FY2030-39 nominal $B


def factor(y, ramp=None):
    return (ramp or RAMP).get(y, 1.0) * (1 + GROWTH) ** (y - 2026)


def parse_ramp(text):
    """'0.3/0.6/0.9' -> {2030: 0.3, 2031: 0.6, 2032: 0.9}; empty -> the default."""
    return {2030 + i: float(v) for i, v in enumerate(text.split('/'))} if text else None


def num(x):
    return float(x) if x not in ('', None) else None


def load():
    rows = [r for r in csv.DictReader(open(CSV)) if r['row_type'] == 'proposal']
    AGENCIES[:] = list(dict.fromkeys(r['agency'] for r in rows))
    z = lambda: [0, 0, 0]
    zp = lambda: {y: z() for y in YEARS}
    out = {a: {'surge': z(), 'rate': z(), 'enf_rate': z(), 'cash29': z(), 'oblig29': z(), 'unpriced': [],
               'path': zp(), 'enf_path': zp()} for a in AGENCIES}
    fees = {}
    layers.clear()
    for r in rows:
        a, env = r['agency'], r['envelope']
        mid = num(r['value'])
        if env in ('program_row', 'new_program'):
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
        if env in ('surge', 'sustained'):
            lay = layers.setdefault((env, r.get('layer') or 'agenda'), [0, 0, 0])
            for i in range(3):
                lay[i] += trio[i] if env == 'surge' else trio[i] * sum(factor(y, parse_ramp(r.get('ramp', ''))) for y in YEARS)
        if env == 'sustained':
            ramp = parse_ramp(r.get('ramp', ''))
            for pk in ['path'] + (['enf_path'] if r.get('revenue_role') == 'enforcement' else []):
                for y in YEARS:
                    out[a][pk][y] = [s + v * factor(y, ramp) for s, v in zip(out[a][pk][y], trio)]
    return out, fees


def boundaries():
    """Every cost kept out of capacity, and the ones whose home row has no price."""
    rows = [r for r in csv.DictReader(open(CSV)) if r['row_type'] == 'boundary']
    return {'rows': len(rows), 'unpriced': [f"{r['agency']}: {r['component']}" for r in rows if r.get('priced') == 'no']}


def lagged_yield(path, ratio, lag):
    """In-window revenue from an enforcement path ({year: $B}). A flat ten-year program at this lag yields
    ratio x funding inside the window, so the steady multiple is ratio x 10 / (10 - lag)."""
    m = ratio * 10 / (10 - lag)
    return m * sum(v for y, v in path.items() if y + lag <= 2039)


def main():
    adopt = json.load(open(ADOPT))['spending']
    surge_env, sust_env = adopt['cap_surge_tn'] * 1000, adopt['cap_sustained_tn'] * 1000
    fsum = sum(factor(y) for y in YEARS)
    (data, fees), res = load(), {}
    for a, d in data.items():
        sust = [sum(d['path'][y][i] for y in YEARS) for i in range(3)]
        share = OLD.get(a, 0) / 600
        res[a] = {'surge': d['surge'], 'sustained': sust, 'total': [s + t for s, t in zip(d['surge'], sust)],
                  'fy2040_rate': [r * (1 + GROWTH) ** 14 for r in d['rate']],
                  'old_total': OLD.get(a, 0) * (1 + 490 / 600), 'pro_rata_new': share * (surge_env + sust_env),
                  'unpriced': d['unpriced']}
    tot = {k: [sum(res[a][k][i] for a in AGENCIES) for i in range(3)] for k in ('surge', 'sustained', 'total', 'fy2040_rate')}
    irs, enf = res['IRS']['total'], data['IRS']['enf_path']
    enf_total = [sum(enf[y][i] for y in YEARS) for i in range(3)]
    enf_yield = {lag: {k: lagged_yield({y: enf[y][i] for y in YEARS}, v, lag) / 1000
                       for i, (k, v) in enumerate(ENF_RATIOS.items())} for lag in LAGS}
    mix = enf_total[1] / irs[1]
    g8 = {'enforcement_bn': enf_total, 'support_bn': [t - e for t, e in zip(irs, enf_total)], 'enforcement_share': mix,
          'enforcement_yield_tn': enf_yield,
          'ira_mix_adjusted_tn': irs[1] * IRA_RATIO * mix / IRA_ENF_SHARE / 1000,
          'ira_unadjusted_tn': irs[1] * IRA_RATIO / 1000,
          'enforcement_needed_bn': {f'{t}T': {k: t * 1000 / v for k, v in ENF_RATIOS.items()} for t in (0.1, 0.2)}}
    fy29 = {k: [sum(data[a][k][i] for a in AGENCIES) for i in range(3)] for k in ('cash29', 'oblig29')}
    path = {y: round(sum(data[a]['path'][y][1] for a in AGENCIES), 2) for y in YEARS}
    out = {'agencies': res, 'totals': tot, 'envelopes_bn': {'surge': surge_env, 'sustained': sust_env},
           'remainder_bn': {'surge': surge_env - tot['surge'][1], 'sustained': sust_env - tot['sustained'][1]},
           'g8': g8, 'fy2029_bn': fy29, 'layers_bn': {f'{e}/{l}': v for (e, l), v in layers.items()},
           'boundaries': boundaries(), 'program_row_fees': fees, 'sustained_path_mid_bn': path, 'factor_sum': fsum}
    if '--json' in sys.argv:
        print(json.dumps(out, indent=1, default=str))
        return
    f = lambda t: f'{t[1]:.1f} ({t[0]:.1f}-{t[2]:.1f})'
    print('| Agency | Surge, lifetime | Sustained, FY2030-39 | Total | FY2040 run rate | Old allocation | Pro rata of $300B+$300B | Unpriced items |')
    print('| --- | --- | --- | --- | --- | --- | --- | --- |')
    for a in AGENCIES:
        r = res[a]
        print(f"| {a} | {f(r['surge'])} | {f(r['sustained'])} | {f(r['total'])} | {f(r['fy2040_rate'])} | {r['old_total']:.1f} | {r['pro_rata_new']:.1f} | {len(r['unpriced'])} |")
    print(f"| **All reviewed** | {f(tot['surge'])} | {f(tot['sustained'])} | {f(tot['total'])} | {f(tot['fy2040_rate'])} | {sum(res[a]['old_total'] for a in AGENCIES):.1f} | {sum(res[a]['pro_rata_new'] for a in AGENCIES):.1f} | |")
    print(f"\nRemainder at the midpoint: surge ${out['remainder_bn']['surge']:.0f}B, sustained ${out['remainder_bn']['sustained']:.0f}B.")
    print(f"Run-rate factor FY2030-39 at the default ramp (ramp x growth from FY2026): {fsum:.2f}.")
    print(f"\nIRS split, FY2030-39: enforcement {f(g8['enforcement_bn'])}; support (service, systems, payments) {f(g8['support_bn'])}; enforcement share {g8['enforcement_share']:.0%} (IRA: {IRA_ENF_SHARE:.0%}).")
    for lag, y in g8['enforcement_yield_tn'].items():
        print(f"REV-G8 from the enforcement row only, {lag}-year lag, ratios 2.2/2.3/2.58 on low/mid/high funding: ${y['low']:.3f}T / ${y['mid']:.3f}T / ${y['high']:.3f}T.")
    print(f"Cross-check, IRA package ratio on the whole IRS total: ${g8['ira_unadjusted_tn']:.3f}T unadjusted; ${g8['ira_mix_adjusted_tn']:.3f}T adjusted to this mix.")
    for t, d in g8['enforcement_needed_bn'].items():
        print(f"Enforcement funding needed for ${t} at these ratios (no extra lag): ${d['high']:.0f}-{d['low']:.0f}B.")
    c, o = fy29['cash29'], fy29['oblig29']
    print(f"\nFY2029, reviewed agencies (small agencies omitted, under $0.1B): cash {f(c)}; obligations {f(o)}; against the $10B of surge cash shifted to FY2029.")
    print('\nBy layer, FY2030-39: ' + '; '.join(f'{e} {l} {v[1]:.1f} ({v[0]:.1f}-{v[2]:.1f})' for (e, l), v in sorted(layers.items())))
    for k, (l, m, h, u) in fees.items():
        print(f"Program row: {k}: {m} {u}" + (f" ({l}-{h})" if l is not None else ''))
    b = out['boundaries']
    print(f"\nBoundary ledger: {b['rows']} excluded items; unpriced: " + '; '.join(b['unpriced']))
    print('\nSustained path for all reviewed agencies, midpoint, $B nominal: ' + ', '.join(f'FY{k} {v}' for k, v in path.items()))


if __name__ == '__main__':
    main()
