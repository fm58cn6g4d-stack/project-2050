#!/usr/bin/env python3
"""The secure floor's decided general-fund lines on federal fiscal years, FY2030-40.

Role: section 6's path (`dossiers/secure-floor/6-cost.md`, part 1). Status: draft (board
row S4). Project arithmetic on the anchors section 3 and the memos give, as decided in
DEC-2026-11-12-06; not a score. Run: python3 dossiers/secure-floor/tools/secure_floor_path.py

Conventions: nominal $ billion, federal cost against the January 2029 law, a cost positive.
FY y runs from October of y-1.
  * A benefit paid monthly in calendar (tax) year y: FY y = 0.75 * CY y + 0.25 * CY (y-1),
    as care's and health's paths count calendar years.
  * A refundable credit claimed on the return (the childless earned income credit, the
    refundable dependent care credit, the repayment safe harbor) is paid in the filing
    season after its tax year, so tax year y lands in FY y+1.
  * SNAP and SSI changes are fiscal-year amounts from FY2030 (enactment in 2029, R1).
Growth rates and anchors are labeled judgment (DEC-2026-11-10-07); each line's basis is
in its comment.
"""

YEARS = list(range(2030, 2041))
WINDOW = range(2030, 2040)

# Booked in the budget model, case `mixed`, at commit 34faa21 (fiscal-model.py build();
# recovery-budget audit lines `FAM-1` and `participation`), FY2030-40.
BOOKED_FAM1 = [171.42, 175.30, 179.26, 183.31, 187.45, 191.69, 196.02, 200.53, 205.14, 209.86, 214.69]
BOOKED_LAB10 = [2.42, 5.02, 7.81, 10.80, 11.21, 11.64, 12.08, 12.53, 13.00, 13.49, 14.00]

# The $2,200 floor's value by tax year 2030-40 (tools/afa_floor.py on the official CPS ASEC
# 2026 archive; real AGI growth 1% a year). Declined (point 2, DEC-2026-11-12-06).
FLOOR_TY = dict(zip(YEARS, [3.97, 3.92, 4.57, 4.53, 5.12, 4.83, 5.32, 5.77, 5.37, 5.69, 5.90]))


def monthly_to_fy(cy):
    return {y: 0.75 * cy.get(y, 0) + 0.25 * cy.get(y - 1, 0) for y in YEARS}


def filed_to_fy(ty):
    return {y: ty.get(y - 1, 0) for y in YEARS}


def grown(first_year, amount, rate, years=range(2029, 2041)):
    return {y: amount * (1 + rate) ** (y - first_year) for y in years if y >= first_year}


def lines():
    out = {}
    floor_fy = monthly_to_fy(FLOOR_TY)
    out['FAM-1, as booked (memo 1 A, legacy planning range)'] = dict(zip(YEARS, BOOKED_FAM1))
    out['less: the $2,200 floor, declined (point 2)'] = {y: -floor_fy[y] for y in YEARS}
    # Part 2 B, the child's own ID: about 500,000 children (EV-SEC-016) at about $5,000 a
    # year in 2030 (judgment; memo 1's $4,000-5,000 in 2026 dollars, indexed), prices 2.3%.
    out['FAM-1.04, the child\'s own ID (part 2 B)'] = monthly_to_fy(grown(2030, 2.5, 0.023))
    # Memo 2 B: $1-2 billion a year to build and run (judgment), central $1.5 billion, prices.
    out['FAM-1.08-1.10, records-based delivery (memo 2 B)'] = {y: 1.5 * 1.023 ** (y - 2030) for y in YEARS}
    # Point 4, the repayment safe harbor: small (judgment), $1 billion a year from TY2030.
    out['FAM-1.06, the repayment safe harbor (point 4)'] = filed_to_fy(grown(2030, 1.0, 0.023))
    # Memo 3 part 1 B: TPC's $135.4 billion over FY2025-34 (EV-SEC-610) grown 2% a year
    # to tax year 2030: about $14.9 billion, then 2% a year (judgment).
    out['INC-1.01, the childless earned income credit (memo 3 part 1 B)'] = filed_to_fy(grown(2030, 14.9, 0.02))
    # Memo 3 part 2 B, SNAP: CBO's nutrition subtitle, almost $187 billion of savings over
    # FY2025-34 (EV-SEC-035), with every cut in force by 2030; about $20.5 billion in FY2030,
    # growing 2.5% a year (judgment). Excludes sec. 10108 (immigrant eligibility), which
    # immigration's table (DEC-2026-11-12-07, memo 6 C) restores and prices.
    out['INC-2.01, SNAP restored (memo 3 part 2 B)'] = grown(2030, 20.5, 0.025, YEARS)
    # SSI's asset limits: SSA's actuaries' $8.9 billion over 2025-34 (EV-SEC-630); about
    # $1.1 billion in FY2030, growing 3% (judgment). Point 8, the indexed exclusions: about
    # $0.6 billion in FY2030, growing as the gap to prices widens (judgment).
    out['INC-3.01, SSI\'s asset limits (memo 3 part 2 B)'] = grown(2030, 1.1, 0.03, YEARS)
    out['INC-3.02, SSI\'s exclusions indexed (point 8)'] = {y: 0.6 + 0.1 * (y - 2030) for y in YEARS}
    # Point 7: $3-6 billion a year (judgment), central $4.5 billion in tax year 2030.
    out['INC-4.01, the refundable dependent care credit (point 7)'] = filed_to_fy(grown(2030, 4.5, 0.025))
    # Memo 7 part 1 B: $1-3 billion a year of forgone offsets (judgment), central $2 billion
    # from FY2031, when the stipends begin, growing 3%.
    out['INC-5.01, the exclusion rule (memo 7 part 1 B)'] = grown(2031, 2.0, 0.03, YEARS)
    out['LAB-10, as booked (memo 4 B, inside the envelope)'] = dict(zip(YEARS, BOOKED_LAB10))
    return out


def table():
    rows = lines()
    new = [k for k in rows if 'booked' not in k and 'floor' not in k]
    print('| Line | ' + ' | '.join(str(y) for y in YEARS) + ' | FY2030-39 |')
    print('| --- |' + ' --- |' * (len(YEARS) + 1))
    totals = {y: 0.0 for y in YEARS}
    for name, path in rows.items():
        for y in YEARS:
            totals[y] += path.get(y, 0)
        cells = ' | '.join(f'{path.get(y, 0):.1f}' for y in YEARS)
        print(f'| {name} | {cells} | {sum(path.get(y, 0) for y in WINDOW):.1f} |')
    print('| **All** | ' + ' | '.join(f'{totals[y]:.1f}' for y in YEARS) + f' | {sum(totals[y] for y in WINDOW):.1f} |')
    new_tot = {y: sum(rows[k].get(y, 0) for k in new) for y in YEARS}
    print(f'\nNew lines, not booked: FY2030-39 {sum(new_tot[y] for y in WINDOW):.1f}, FY2040 {new_tot[2040]:.1f}')
    floor = rows['less: the $2,200 floor, declined (point 2)']
    print(f'Floor declined: FY2030-39 {sum(floor[y] for y in WINDOW):.1f}, FY2040 {floor[2040]:.1f}')


if __name__ == '__main__':
    table()
