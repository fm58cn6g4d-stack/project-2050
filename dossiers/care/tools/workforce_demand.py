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
RN_2025 = 3_465_400        # BLS, 2025 (SRC-3330 table)
NA_2025 = 1_505_900        # nursing assistants, BLS 2025
PHYSICIANS = 1_000_000     # judgment: about a million active physicians (not in the register)

# ---------- Nursing homes: the 2024 staffing standards (memo 16) ----------
RN_HIRES_2024_RULE = 16_000  # CMS's own estimate (89 FR 40876, regulatory impact analysis)

# ---------- Wage options (memo 14) ----------
# The care part of part B's benefit and Medicaid home care that is labor: about 60% (part B's judgment).
# A floor that raises home-care pay by 20% costs about 12% of the benefit; part B put that at about
# $55 billion a year on top of memo 6 B in 2035. Here the same arithmetic is run on the whole publicly
# paid home-care base in 2035: today's Medicaid home care (about $164 billion in 2023, EV-CAR-404,
# EV-CAR-406) grown 5.5% a year (part B's working assumption) plus memo 6 B's new money (about $215
# billion, 3b). Under memo 6 B the plan pays the whole benefit and states' maintenance of effort is a fixed
# amount, so a raise falls on federal money; under memo 6 A states would pay about 47% of it (EV-CAR-448).
MEDICAID_HOME_2023 = 164e9
GROWTH = 1.055
NEW_BENEFIT_2035 = 215e9
LABOR_SHARE = 0.6


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

    medicaid_home_2035 = MEDICAID_HOME_2023 * GROWTH ** 12
    base_2035 = medicaid_home_2035 + NEW_BENEFIT_2035
    print()
    print(f'Publicly paid home care, 2035: Medicaid ${medicaid_home_2035 / 1e9:.0f}B '
          f'+ memo 6 B new money ${NEW_BENEFIT_2035 / 1e9:.0f}B = ${base_2035 / 1e9:.0f}B')
    for raise_ in (0.10, 0.20, 0.30):
        print(f'  a {raise_:.0%} raise on the labor share: ${base_2035 * LABOR_SHARE * raise_ / 1e9:.0f}B a year')


if __name__ == '__main__':
    main()
