#!/usr/bin/env python3
"""Project arithmetic for dossiers/care/1d-problem-workforce.md and 3d-design-workforce.md: how many more
paid care workers the decided health path and parts B and C's recommended options would need, and what the
part D wage options cost.

Not a model and not an official score. Every input is either a figure from the evidence register (tag in
the comment) or a judgment labeled as one, with a range. Run:

    python3 dossiers/care/tools/workforce_demand.py

It prints low, central and high readings. "Workers" are people employed, not full-time equivalents, because
most direct care jobs are part-time.
"""

# ---------- Home care: part B, memo 6 B (recommended, not decided) ----------
# New users and their paid cost: part B's own working assumption (3b-design-home-care.md, "What the options
# cost"): 3-5 million new users at $12,000-20,000 a year in 2022 dollars; waiting lists of about 650,000
# people (EV-HOU-691) at Medicaid's 2022 cost per home-care user, about $16,600 (EV-CAR-407).
NEW_USERS = (3.0e6, 4.0e6, 5.0e6)
COST_PER_NEW_USER = (12_000, 16_000, 20_000)
WAITLIST = 650_000
COST_PER_MEDICAID_USER = 16_600
# Cost per paid hour of agency or self-directed care, 2022 dollars (judgment): the aide median wage of
# $35,800 a year in 2025 (EV-CAR-422), about $17.20 an hour, over part B's labor share of about 60%,
# deflated to 2022, is about $26; agencies' overhead and benefits put it nearer $30. Range $26-36.
COST_PER_HOUR = (36.0, 30.0, 26.0)  # ordered so that the low reading uses the high cost
# Hours a direct care worker is paid in a year (judgment; most work part-time). Range 1,200-1,700.
HOURS_PER_WORKER = (1_700, 1_400, 1_200)
# Share of the new paid hours given by relatives already caring unpaid, under memo 9 A (judgment, from
# Cash and Counseling, where most hires were relatives, EV-CAR-488). They are counted as workers but are
# not new recruits to the labor market.
FAMILY_SHARE = (0.5, 0.4, 0.3)

# ---------- Child care and pre-K: part C, memos 10 B and 11 A (recommended, not decided) ----------
# Under-3 children in paid care under memo 10 B: about 4.5 million full-time equivalents, range 3.5-6.0
# (part C's judgment, 3c-design-child-care.md). How many are in paid care today is not in the register
# (part C, "Evidence still needed"); judgment: about 2.5 million full-time equivalents, so the guarantee
# adds 1.0-3.0 million.
UNDER3_ADDED = (1.0e6, 2.0e6, 3.0e6)
# Children per paid staff member in infant and toddler rooms, counting breaks, absences and non-ratio
# staff (judgment, on ratios of about 1:4 for infants and 1:6 for toddlers). Range 4-6.
UNDER3_PER_STAFF = (6.0, 5.0, 4.0)
# Pre-K under memo 11 A: about 5.2 million 3s and 4s (part C) against about 1.8 million in state pre-K now
# (EV-CAR-519), so about 3.4 million more children in pre-K classrooms. Many are already in child care or
# Head Start rooms that change funding, not staff (judgment: a third to two-thirds need new staff).
PREK_ADDED_CHILDREN = 3.4e6
PREK_NEW_STAFF_SHARE = (1 / 3, 0.5, 2 / 3)
PREK_PER_STAFF = 10.0  # a lead teacher and an assistant for 20 children (the NIEER benchmark class)

# ---------- Health: the decided path (HLT-7) ----------
# RAND: with no supply limit, Medicare for All with long-term care raises total spending 9.8% rather than
# 1.8% (EV-CAR-228). The gap, about 8% of spending, is care demanded that supply would not meet. Read as
# extra clinical labor demanded at the endpoint, before memo 4 C's copays damp it (judgment: 3-8%).
HEALTH_EXTRA_DEMAND = (0.03, 0.05, 0.08)
RN_2025 = 3_465_400        # BLS, 2025 (EV-CAR-610)
NA_2025 = 1_505_900        # nursing assistants, BLS 2025 (EV-CAR-609)
PHYSICIANS = 1_000_000     # judgment: about a million active physicians (not in the register)

# ---------- Nursing homes: the 2024 staffing standards (memo 16) ----------
RN_HIRES_2024_RULE = 16_000  # CMS's own estimate (89 FR 40876, regulatory impact analysis)

# ---------- Wage options (memo 14) ----------
# The payroll a floor raises is the publicly paid home care that pays for hours of work. In 2035, under
# memo 6 B, that is today's Medicaid home care (about $164 billion in 2023, EV-CAR-404, EV-CAR-406, federal
# and state money together) grown 5.5% a year (part B's working assumption), plus the parts of memo 6 B's
# new money that buy new hours: waiting lists served (about $22 billion) and new users (about $120
# billion). Memo 6 B's other part, relief of states' home-care share net of maintenance of effort (about
# $73 billion), moves state money already inside the Medicaid line onto the federal side and buys no new
# hours, so it is not added (review of PR #242). Part B's own 20% placeholder, about $55 billion on about
# 60% labor, implies the same base, about $458 billion. Under memo 6 B the plan pays the whole benefit and
# states' maintenance of effort is a fixed amount, so a raise falls on federal money; under memo 6 A states
# would pay about 47% of it (EV-CAR-448).
MEDICAID_HOME_2023 = 164e9
GROWTH = 1.055
NEW_HOURS_MONEY_2035 = 22e9 + 120e9   # part B memo 6 B: waiting lists and new users (3b-design-home-care.md)
LABOR_SHARE = 0.6
# Average payroll increase a floor causes, by level in 2026 dollars (judgment; section 3d): $18, $20, $22.50.
LEVELS = {'$18': 0.05, '$20': 0.12, '$22.50': 0.25}
# Nursing homes, where the median nursing assistant already earns about $20.30 an hour (EV-CAR-609):
# judgment, $ billion in 2035.
NURSING_HOMES_2035 = {'$18': 1e9, '$20': 3e9, '$22.50': 5e9}
FEDERAL_SHARE_BRIDGE = 0.9   # the federal government pays 90% of the floor's added cost in 2030-34 (judgment)


def three(f):
    return tuple(f(i) for i in range(3))


def fmt(x):
    return f'{x / 1e6:.2f}M'


def main():
    home = three(lambda i: (NEW_USERS[i] * COST_PER_NEW_USER[i] + WAITLIST * COST_PER_MEDICAID_USER)
                 / COST_PER_HOUR[i] / HOURS_PER_WORKER[i])
    home_recruits = three(lambda i: home[i] * (1 - FAMILY_SHARE[i]))
    under3 = three(lambda i: UNDER3_ADDED[i] / UNDER3_PER_STAFF[i])
    prek = three(lambda i: PREK_ADDED_CHILDREN * PREK_NEW_STAFF_SHARE[i] / PREK_PER_STAFF)
    child = three(lambda i: under3[i] + prek[i])
    rn = three(lambda i: RN_2025 * HEALTH_EXTRA_DEMAND[i])
    md = three(lambda i: PHYSICIANS * HEALTH_EXTRA_DEMAND[i])
    print('Added paid care workers at maturity (low, central, high)')
    print('  home care, memo 6 B (workers):          ', ', '.join(fmt(x) for x in home))
    print('    of whom new recruits (not relatives): ', ', '.join(fmt(x) for x in home_recruits))
    print('  child care under 3, memo 10 B:           ', ', '.join(fmt(x) for x in under3))
    print('  pre-K, memo 11 A:                        ', ', '.join(fmt(x) for x in prek))
    print('  child care and pre-K together:           ', ', '.join(fmt(x) for x in child))
    print('  registered nurses, HLT-7:                ', ', '.join(fmt(x) for x in rn))
    print('  physicians, HLT-7:                       ', ', '.join(fmt(x) for x in md))
    total = three(lambda i: home_recruits[i] + child[i])
    print('  care recruits, home care plus child care:', ', '.join(fmt(x) for x in total))
    print(f'  nursing-home RNs, 2024 rule restored:     {RN_HIRES_2024_RULE:,}')

    medicaid = {y: MEDICAID_HOME_2023 * GROWTH ** (y - 2023) for y in range(2030, 2041)}
    base_2035 = medicaid[2035] + NEW_HOURS_MONEY_2035
    print()
    print(f'Publicly paid home care that buys hours, 2035: Medicaid ${medicaid[2035] / 1e9:.0f}B '
          f'+ memo 6 B new hours ${NEW_HOURS_MONEY_2035 / 1e9:.0f}B = ${base_2035 / 1e9:.0f}B')
    print('Memo 14 B by level: 2035 ($B), FY2030-39 ($T, calendar years), FY2040 ($B)')
    for level, raise_ in LEVELS.items():
        bridge = sum(medicaid[y] * LABOR_SHARE * raise_ * FEDERAL_SHARE_BRIDGE for y in range(2030, 2035))
        first = base_2035 * LABOR_SHARE * raise_ + NURSING_HOMES_2035[level]
        later = sum(first * GROWTH ** (y - 2035) for y in range(2035, 2040))
        fy2040 = first * GROWTH ** 5
        print(f'  {level:>6}: 2035 {first / 1e9:5.0f}  FY2030-39 {(bridge + later) / 1e12:4.2f} '
              f'(bridge {bridge / 1e12:.2f})  FY2040 {fy2040 / 1e9:4.0f}')
    print(f'  under memo 6 A ($20, no new benefit): 2035 {medicaid[2035] * LABOR_SHARE * 0.12 / 1e9:.0f}')


if __name__ == '__main__':
    main()
