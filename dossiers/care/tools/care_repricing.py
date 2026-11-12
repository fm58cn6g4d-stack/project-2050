#!/usr/bin/env python3
"""Project arithmetic for the care repricing after Espen's decisions (board row D-8; `DEC-2026-11-11-02` to
`-05`): part B at three daily activities, part D's workforce lines at the federal cost only, each part's
state-share options, and memo 17's cost-down options.

Not a model and not an official score. Every input is a figure already in the dossier (with its tag or the
file it comes from) or a judgment labeled as one, with a range. Calendar years, nominal dollars, against
current law, as in sections 3b, 3c and 3d; section 6 converts to fiscal years. Run:

    python3 dossiers/care/tools/care_repricing.py

Readings are (low, central, high). The low reading pairs each piece's low; the high reading each piece's
high, as section 3b's ranges do.
"""
from math import erf, exp, log, sqrt

YEARS_B = range(2035, 2040)          # memo 6 B's years inside FY2030-39
GROWTH = 1.055                       # part B's nominal growth (3b, working assumption)

# ---------- Part B: the pieces of memo 6 B (3b, "What the options cost", as revised in #244) ----------
RELIEF_2035 = (29e9, 73e9, 147e9)    # states' home-care share, net of maintenance of effort at 50%
RICHER_2035 = (15e9, 30e9, 45e9)     # tier budgets for today's Medicaid users (hold-harmless)
NEW_USERS_2ADL = (5.0e6, 6.5e6, 8.0e6)
COST_EACH_2ADL = (28_000, 42_000, 66_000)
# Three activities or the equivalent (DEC-2026-11-11-02, memo 7 part 1 C). Share of the two-activity new
# users who still qualify (judgment). Basis: Freedman and Spillman (NHATS 2011) count nearly 3 million older
# people outside nursing homes receiving help with three or more self-care or mobility activities, against
# ASPE's 5.7 million meeting the two-activity test, most nursing-home residents among them (EV-CAR-482,
# EV-CAR-641): about 0.6-0.7 in the whole population. The "equivalent" keeps severe cognitive impairment.
# Among people not now served the share is lower, because people with three or more limitations are far
# likelier to get help (85% against 45%, CBO 2013) and to be on Medicaid already (24%, about five times the
# rate of people without limitations) (EV-CAR-642, EV-CAR-643).
RETAINED = (0.55, 0.60, 0.70)
# Cost per retained new user rises, because the lightest-need tier drops out (judgment; CBO counts about 9
# hours a day of help, paid and unpaid, for people with three or more limitations, EV-CAR-644).
COST_LIFT = (1.12, 1.20, 1.25)
# The hold-harmless as decided covers everyone on Medicaid home care on December 31, 2034. People who would
# later have entered Medicaid home care below the three-activity line (in states whose level of care is
# lower, or under the 2025 law's lower-need waiver, EV-CAR-414) are not covered. Share of the Medicaid
# home-care line that this removes by FY2040, net of people whose needs grow past the line (judgment; the
# share of users with three or more limitations runs from about a third in California's home-care sample to
# about 95% under Washington's definitions, EV-CAR-645, EV-CAR-646). Ramps linearly from zero in 2035.
ATTRITION_2040 = (0.03, 0.06, 0.10)
MEDICAID_HOME_2023 = 164e9           # EV-CAR-404, EV-CAR-406
MEMO8C_2035 = (50e9, 70e9, 90e9)     # memo 8 C, unchanged: 84% of nursing-home residents have three or more
                                     # limitations (EV-CAR-647); the rest qualify by the equivalent test
BRIDGE_TOTAL = 0.13e12               # point 1, FY2030-34, unchanged
URBAN_2ADL = (500e9, 740e9)          # Urban 2020 option 1, adjusted to memo 6 B (3b): low-cost case, best guess
CBO_2ADL = (350e9, 400e9)            # CBO 2020 option 5 against 4, adjusted to memo 6 B (3b)
NOT_NEW_USE = 103e9                  # relief plus richer budgets inside those benchmarks (central pieces)


def three(f):
    return tuple(f(i) for i in range(3))


def medicaid_home(y):
    return MEDICAID_HOME_2023 * GROWTH ** (y - 2023)


def ramp(y, end_share):
    return end_share * (y - 2035) / 5 if y >= 2035 else 0.0


def part_b(new_users, cost_each):
    first = three(lambda i: RELIEF_2035[i] + RICHER_2035[i] + new_users[i] * cost_each[i])
    yrs = three(lambda i: sum(first[i] * GROWTH ** (y - 2035) for y in YEARS_B))
    fy40 = three(lambda i: first[i] * GROWTH ** 5)
    return first, yrs, fy40


# ---------- Part D: the wage floor (memo 14) ----------
# The payroll increase a floor causes, as a share of payroll, for wages lognormal around the median. The
# dossier's judgment (5%, 12%, 25% at $18, $20, $22.50) matches a floor measured against 2026 wages, not 2024
# wages: grown 4% a year (part B's wage growth), the 2024 median of $16.77 (EV-CAR-613) is about $18.14 in 2026.
def floor_lift(floor, median, sigma):
    d = log(floor / median) / sigma
    n = lambda x: 0.5 * (1 + erf(x / sqrt(2)))
    return (floor / median * n(d) - exp(sigma ** 2 / 2) * n(d - sigma)) / exp(sigma ** 2 / 2)


LABOR_SHARE = 0.6
FLOOR_LIFT = (0.08, 0.12, 0.18)      # $20, the dossier's range (3d), kept: the check below confirms it
NURSING_HOMES_2035 = 3e9             # $20 floor in nursing homes (3d, judgment)


# ---------- State shares ----------
FMAP_REGULAR = 0.60                  # judgment: home care's average federal share, close to the 60.4% for
                                     # long-term care (EV-CAR-460)
BRIDGE_POINTS = 0.08                 # judgment: average of 6 entry points and up to 4 for progress
STATE_LTC_SHARE = 0.47               # EV-CAR-448
MEDICAID_INST_2023 = 93e9            # 3b: $257.0 billion less 63.8% for home care (EV-CAR-404, EV-CAR-406)

# Part C at maturity (3c): child care net direct services, pre-K gross, CCDF and administration.
CC_NET_2033 = 100e9
CC_CCDF = 12e9
CC_ADMIN = 6e9
CC_FY40_RATIO = 110 / 84             # 3c's FY2040 over its 2033 figure
PREK_GROSS = 91e9
PREK_STATE_NOW = 14.4e9              # EV-CAR-519
PARITY_FY40 = 60e9                   # memo 15 B in FY2040 at 90% (3d)
PARITY_YRS = 0.25e12                 # memo 15 B over FY2030-39 at 90%, nearly all from 2033 (3d)


def main():
    print('PART B AT TWO AND AT THREE DAILY ACTIVITIES')
    users3 = three(lambda i: NEW_USERS_2ADL[i] * RETAINED[i])
    cost3 = three(lambda i: COST_EACH_2ADL[i] * COST_LIFT[i])
    b2 = part_b(NEW_USERS_2ADL, COST_EACH_2ADL)
    b3 = part_b(users3, cost3)
    print('  new users qualifying, 2035 (millions): two activities',
          ', '.join(f'{x / 1e6:.1f}' for x in NEW_USERS_2ADL), '| three',
          ', '.join(f'{x / 1e6:.1f}' for x in users3))
    print('  cost per new user ($):                 two', ', '.join(f'{x:,}' for x in COST_EACH_2ADL),
          '| three', ', '.join(f'{x:,.0f}' for x in cost3))
    print('  new-user line 2035 ($B):               two',
          ', '.join(f'{NEW_USERS_2ADL[i] * COST_EACH_2ADL[i] / 1e9:.0f}' for i in range(3)), '| three',
          ', '.join(f'{users3[i] * cost3[i] / 1e9:.0f}' for i in range(3)))
    att = three(lambda i: [medicaid_home(y) * ramp(y, ATTRITION_2040[i]) for y in range(2035, 2041)])
    att_yrs = three(lambda i: sum(att[i][:5]))
    att_40 = three(lambda i: att[i][5])
    for name, (first, yrs, fy40), a_yrs, a_40 in (('two', b2, (0, 0, 0), (0, 0, 0)),
                                                   ('three', b3, att_yrs, att_40)):
        print(f'  memo 6 B, {name:>5}: 2035 ' + ', '.join(f'{x / 1e9:.0f}' for x in first) +
              ' | 2035-39 ($T) ' + ', '.join(f'{(yrs[i] - a_yrs[i]) / 1e12:.2f}' for i in range(3)) +
              ' | FY2040 ' + ', '.join(f'{(fy40[i] - a_40[i]) / 1e9:.0f}' for i in range(3)))
    print('  attrition below the line (decided hold-harmless), 2035-39 ($T) ' +
          ', '.join(f'{x / 1e12:.2f}' for x in att_yrs) + ' | FY2040 ($B) ' +
          ', '.join(f'{x / 1e9:.0f}' for x in att_40))
    factor = RETAINED[1] * COST_LIFT[1]
    print(f'  benchmarks at three activities (new use scaled by {factor:.2f}):')
    print('    Urban 2020: ' + ', '.join(f'{(NOT_NEW_USE + (u - NOT_NEW_USE) * factor) / 1e9:.0f}'
                                       for u in URBAN_2ADL) + ' (low-cost case, best guess)')
    print('    CBO 2020:   ' + ', '.join(f'{(NOT_NEW_USE + (c - NOT_NEW_USE) * factor) / 1e9:.0f}'
                                       for c in CBO_2ADL))
    m8 = three(lambda i: sum(MEMO8C_2035[i] * GROWTH ** (y - 2035) for y in YEARS_B))
    tot_b = three(lambda i: BRIDGE_TOTAL + b3[1][i] - att_yrs[i] + m8[i])
    tot_b40 = three(lambda i: b3[2][i] - att_40[i] + MEMO8C_2035[i] * GROWTH ** 5)
    print('  part B recommended set, FY2030-39 ($T): ' + ', '.join(f'{x / 1e12:.2f}' for x in tot_b) +
          ' | FY2040 ($B): ' + ', '.join(f'{x / 1e9:.0f}' for x in tot_b40))

    print()
    print('PART D: THE FLOOR AGAINST BASELINE WAGES')
    med24, med26 = 16.77, 16.77 * 1.04 ** 2
    for s in (0.15, 0.20):
        print(f'  sigma {s}: against 2024 wages ' +
              ', '.join(f'{floor_lift(f, med24, s):.0%}' for f in (18, 20, 22.5)) +
              ' | against 2026 baseline wages ' +
              ', '.join(f'{floor_lift(f, med26, s):.0%}' for f in (18, 20, 22.5)))
    base2 = medicaid_home(2035) + RICHER_2035[1] + NEW_USERS_2ADL[1] * COST_EACH_2ADL[1]
    base3 = three(lambda i: medicaid_home(2035) + RICHER_2035[i] + users3[i] * cost3[i])
    print(f'  home-care base that buys hours, 2035 ($B): two activities {base2 / 1e9:.0f}; three ' +
          ', '.join(f'{x / 1e9:.0f}' for x in base3))
    m14_35 = three(lambda i: base3[i] * LABOR_SHARE * FLOOR_LIFT[i] + NURSING_HOMES_2035)
    bridge_gross = sum(medicaid_home(y) * LABOR_SHARE * FLOOR_LIFT[1] for y in range(2030, 2035))
    print('  memo 14 B ($20), 2035 ($B): ' + ', '.join(f'{x / 1e9:.0f}' for x in m14_35))
    print(f'  bridge-period added payroll, 2030-34, gross: ${bridge_gross / 1e9:.0f}B')

    print()
    print('STATE SHARES (federal cost; cost to states)')
    shares = {'90% (memo 14 now)': 0.90,
              "the state's bridge rate (regular plus the bridge's points)": FMAP_REGULAR + BRIDGE_POINTS,
              'the regular match': FMAP_REGULAR}
    for k, s in shares.items():
        print(f'  bridge floor at {k}: federal ${bridge_gross * s / 1e9:.0f}B, states '
              f'${bridge_gross * (1 - s) / 1e9:.0f}B over 2030-34')
    for moe in (0.5, 0.65, 0.8):
        home = STATE_LTC_SHARE * medicaid_home(2035) * (1 - moe)
        inst = STATE_LTC_SHARE * MEDICAID_INST_2023 * GROWTH ** 12 * (1 - moe)
        print(f'  part B maintenance of effort {moe:.0%}: federal relief of states in 2035, home care '
              f'${home / 1e9:.0f}B, institutions ${inst / 1e9:.0f}B; states keep paying '
              f'${STATE_LTC_SHARE * (medicaid_home(2035) + MEDICAID_INST_2023 * GROWTH ** 12) * moe / 1e9:.0f}B')
    print(f'  part B, states also pay 10% of new benefit cost: about '
          f'${0.10 * (RICHER_2035[1] + users3[1] * cost3[1]) / 1e9:.0f}B in 2035')
    for s in (0.90, 0.80, 0.75):
        fed = CC_NET_2033 * s - CC_CCDF + CC_ADMIN
        print(f'  child care at {s:.0%} after three years: federal 2033 ${fed / 1e9:.0f}B, FY2040 '
              f'${fed * CC_FY40_RATIO / 1e9:.0f}B; states ${CC_NET_2033 * (1 - s) / 1e9:.0f}B in 2033; '
              f'parity FY2040 ${PARITY_FY40 * s / 0.9 / 1e9:.0f}B, FY2030-39 ${PARITY_YRS * s / 0.9 / 1e12:.2f}T')
    for s in (0.90, 0.75, 0.60):
        fed = (PREK_GROSS - PREK_STATE_NOW) * s
        print(f'  pre-K at {s:.0%} after three years: federal at maturity ${fed / 1e9:.0f}B, '
              f'states ${(PREK_GROSS - fed) / 1e9:.0f}B (their ${PREK_STATE_NOW / 1e9:.1f}B included)')


if __name__ == '__main__':
    main()
