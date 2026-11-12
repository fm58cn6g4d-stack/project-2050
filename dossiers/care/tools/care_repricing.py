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
# The hold-harmless's own cost: what the plan spends on people on Medicaid home care on December 31, 2034
# who are below the three-activity line. Their share of the Medicaid home-care line in 2035 (judgment, 10-20%:
# spending runs lower per person below the line, and people with intellectual or developmental disabilities,
# a large share of spending, mostly meet the equivalent test; EV-CAR-645, EV-CAR-646), shrinking as they
# leave the program or their needs grow past the line, to about 40% of the starting group by 2040 (judgment).
HOLD_SHARE_2035 = (0.10, 0.15, 0.20)
HOLD_SURVIVAL_5YR = 0.40
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
    surv = HOLD_SURVIVAL_5YR ** (1 / 5)
    hold = three(lambda i: [medicaid_home(2035) * HOLD_SHARE_2035[i] * (GROWTH * surv) ** t for t in range(6)])
    print('  the hold-harmless, inside the totals (2035 $B; 2035-39 $T; FY2040 $B): ' +
          '; '.join(f'{h[0] / 1e9:.0f}, {sum(h[:5]) / 1e12:.2f}, {h[5] / 1e9:.0f}' for h in hold))
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


    print()
    print('TOTALS BY PART, CENTRAL (FY2030-39 $T calendar years; FY2040 $B)')
    # Before: the figures for Espen's decision sheet (3b after #244; 3c; 3d after #246).
    before = {'B': (2.6, 590), 'C': (1.4, 190), 'D': (0.65, 130)}
    # After items 1-3. Part B from above. Part C: child care at 80% after three years (from the 2033-34
    # school year), about 12% off the federal line in 2034-39 and half a year of 2033. Part D: memo 14 on
    # the three-activity base with the bridge floor at the bridge rate; memo 15 at the child care share;
    # memo 16 fully federal from 2035 under memo 8 C; the points unchanged.
    cc_cut = sum(84e9 * GROWTH ** (y - 2033) * 10 / 84 for y in range(2034, 2040)) + 0.5 * 10e9
    m14_yrs = bridge_gross * (FMAP_REGULAR + BRIDGE_POINTS) + sum(m14_35[1] * GROWTH ** (y - 2035) for y in YEARS_B)
    m14_40 = m14_35[1] * GROWTH ** 5
    after = {'B': (tot_b[1] / 1e12, tot_b40[1] / 1e9),
             'C': (1.4 - cc_cut / 1e12, 190 - 13),
             'D': ((m14_yrs + PARITY_YRS * 0.8 / 0.9) / 1e12 + 0.04 + 0.02,
                   (m14_40 + PARITY_FY40 * 0.8 / 0.9) / 1e9 + 7 + 2)}
    for k in 'BCD':
        print(f'  part {k}: before {before[k][0]:.2f}T, {before[k][1]:.0f}B | after items 1-3 '
              f'{after[k][0]:.2f}T, {after[k][1]:.0f}B')
    # Steps 1 and 2 only, at today's working shares (bridge floor 90%, child care 90%, parity at 90%).
    working = {'B': after['B'], 'C': (1.4, 190),
               'D': (after['D'][0] + bridge_gross * (0.90 - FMAP_REGULAR - BRIDGE_POINTS) / 1e12
                     + PARITY_YRS * (1 - 0.8 / 0.9) / 1e12,
                     after['D'][1] + PARITY_FY40 * (1 - 0.8 / 0.9) / 1e9)}
    for k in 'BCD':
        print(f'  part {k}: steps 1-2 at working shares {working[k][0]:.2f}T, {working[k][1]:.0f}B')
    tw = sum(v[0] for v in working.values()), sum(v[1] for v in working.values())
    print(f'  all three, steps 1-2 at working shares: {tw[0]:.2f}T, {tw[1]:.0f}B')
    # If a third of states decline child care and pre-K and HHS pays all there (no obligation on them).
    q = 1 / 3
    cc_fed = lambda share: CC_NET_2033 * (share * (1 - q) + q)
    print(f'  a third of states out, no obligation: child care federal at 80% ${cc_fed(0.8) / 1e9:.0f}B against '
          f'${CC_NET_2033 * 0.9 / 1e9:.0f}B at 90% with all in (saving kept {(0.9 - 0.8 - q * 0.2) / 0.1:.0%}); '
          f'pre-K at 75% ${(PREK_GROSS - PREK_STATE_NOW) * (0.75 * (1 - q) + q) / 1e9:.0f}B against '
          f'${(PREK_GROSS - PREK_STATE_NOW) * 0.75 / 1e9:.0f}B')
    tb = sum(v[0] for v in before.values()), sum(v[1] for v in before.values())
    ta = sum(v[0] for v in after.values()), sum(v[1] for v in after.values())
    print(f'  all three: before {tb[0]:.2f}T, {tb[1]:.0f}B | after {ta[0]:.2f}T, {ta[1]:.0f}B')
    print(f'    memo 14 after: FY2030-39 {m14_yrs / 1e12:.2f}T, FY2040 {m14_40 / 1e9:.0f}B; '
          f'child care cut {cc_cut / 1e12:.2f}T')

    print()
    print("MEMO 17'S FURTHER OPTIONS (savings: FY2030-39 $T; FY2040 $B; judgment unless noted)")
    newb = users3[1] * cost3[1]
    opts = {
        '1 bridge at 6 points, not up to 10': (BRIDGE_TOTAL * 0.4, 0),
        '2 tier budgets 10% lower below the top tier (about 70% of spending)':
            (sum(0.07 * (RICHER_2035[1] + newb) * GROWTH ** (y - 2035) for y in YEARS_B),
             0.07 * (RICHER_2035[1] + newb) * GROWTH ** 5),
        '3 early-educator parity by 2038, not 2036': (0.04e12, 0),
        '4 new users phased in over 2035-36, heaviest needs first':
            (newb * 0.5 + newb * GROWTH * 0.2, 0),
        '5 residents contribute up to 20% of the care part from income left after room and board':
            (sum(8e9 * GROWTH ** (y - 2035) for y in YEARS_B), 8e9 * GROWTH ** 5),
        '6 a 10% copay on home-benefit hours above 200% of poverty, capped at 5% of income':
            (sum(12e9 * GROWTH ** (y - 2035) for y in YEARS_B), 12e9 * GROWTH ** 5),
        '7 part B maintenance of effort at 65% (with health)':
            (sum(34e9 * GROWTH ** (y - 2035) for y in YEARS_B), 34e9 * GROWTH ** 5),
    }
    for k, (yrs, fy40) in opts.items():
        print(f'  {k}: {yrs / 1e12:.2f}T, {fy40 / 1e9:.0f}B')
    rec = [opts[k] for k in opts if k[0] in '2345']
    print(f'  recommended (2, 3, 4, 5): {sum(r[0] for r in rec) / 1e12:.2f}T, {sum(r[1] for r in rec) / 1e9:.0f}B')
    print(f'  add-back, a continuing Medicaid route below the line: {att_yrs[1] / 1e12:.2f}T, {att_40[1] / 1e9:.0f}B '
          f'in all; federal at the regular match {att_yrs[1] * FMAP_REGULAR / 1e12:.3f}T, '
          f'{att_40[1] * FMAP_REGULAR / 1e9:.0f}B')
    net = (ta[0] - sum(r[0] for r in rec) / 1e12 + att_yrs[1] * FMAP_REGULAR / 1e12,
           ta[1] - sum(r[1] for r in rec) / 1e9 + att_40[1] * FMAP_REGULAR / 1e9)
    print(f'  all three with the recommended options and the state option: {net[0]:.2f}T, {net[1]:.0f}B')


if __name__ == '__main__':
    main()
