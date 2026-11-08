#!/usr/bin/env python3
"""The defense lock-in: three FY2027-28 defense paths and their effect on NSC-1A's 2030-39 base.

Role: the arithmetic behind dossiers/scenario/compounding-defense.md. Status: exploratory (stage B,
November 8, 2026); not a core model. Inputs, all typed in below:
  - FY2026 enacted Defense appropriations bill, base discretionary budget authority: $838.7 billion
    (the Lame-Duck Ledger's sourced FY2026 figure, SRC-0545).
  - GDP price index growth: 2.4% FY2027 and 2.3% FY2028 (the Ledger's deflators); 2.1% a year from
    FY2029 (this project's assumption; sensitivity at 1.8% and 2.5%).
  - Paths: (1) flat real from FY2026; (2) a middle path: the Ledger's FY2027 likely deal ($870 billion),
    then flat real into FY2028; (3) the Ledger's parity path: $870 billion, then its FY2028 target
    ($905 billion). A fourth row shows the Ledger's FY2027 stretch deal ($895 billion) held flat in real
    terms into FY2028 (an upper case; the Ledger's own FY2028 target, $905 billion, sits below it).
  - NSC-1A: defense flat in real terms from the FY2029 base. The FY2029 level is FY2028 grown by one
    year of the deflator.
Outputs are nominal billions. The Defense bill is a proxy for the national defense function (050),
which also includes DOE nuclear programs and other agencies; the gaps scale roughly in proportion.

  python3 dossiers/scenario/tools/compounding-defense.py      (standard library only)
"""
FY26 = 838.7
D27, D28 = 0.024, 0.023
PATHS = {
    'Flat real from FY2026': (FY26 * (1 + D27), FY26 * (1 + D27) * (1 + D28)),
    'Middle: FY2027 deal, then flat real': (870.0, 870.0 * (1 + D28)),
    'Ledger parity: deal, then FY2028 target': (870.0, 905.0),
    'Ledger stretch, then flat real': (895.0, 895.0 * (1 + D28)),
}


def decade(fy28, d):
    """FY2030-39 sum and FY2039 level under NSC-1A, with deflator d from FY2029."""
    levels = {2028: fy28}
    for y in range(2029, 2040):
        levels[y] = levels[y - 1] * (1 + d)
    return sum(levels[y] for y in range(2030, 2040)), levels[2029], levels[2039]


def main():
    base = PATHS['Flat real from FY2026'][1]
    print('Path | FY2027 | FY2028 | FY2028 real growth over FY2026 | FY2029 base | 2030-39 sum | '
          'gap vs flat real, 2030-39 (2.1%; 1.8%-2.5%)')
    for name, (fy27, fy28) in PATHS.items():
        real = (fy28 / ((1 + D27) * (1 + D28)) / FY26 - 1) * 100
        s, b29, _ = decade(fy28, 0.021)
        gaps = [decade(fy28, d)[0] - decade(base, d)[0] for d in (0.021, 0.018, 0.025)]
        print(f'{name} | {fy27:.1f} | {fy28:.1f} | {real:+.1f}% | {b29:.1f} | {s:,.0f} | '
              f'{gaps[0]:+,.0f} ({gaps[1]:+,.0f} to {gaps[2]:+,.0f})')


if __name__ == '__main__':
    main()
