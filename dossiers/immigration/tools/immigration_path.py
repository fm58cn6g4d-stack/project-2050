#!/usr/bin/env python3
"""Immigration's decided general-fund lines on federal fiscal years, FY2030-40.

Role: section 6's path (`dossiers/immigration/6-cost.md`, part 1). Status: draft (board row
I4). Project arithmetic on the anchors section 3 and the memos give, as decided in
DEC-2026-11-12-07; not a score. Run: python3 dossiers/immigration/tools/immigration_path.py

Conventions: nominal $ billion, federal cost against the January 2029 law, a cost positive,
on the general fund (on-budget) unless a line says otherwise. FY y runs from October of y-1.
Every anchor and shape below is judgment unless an evidence ID is given (DEC-2026-11-10-07);
`3-design.md`, "What the options cost" and "IMM-1's score, re-derived", gives each basis.
Each line carries (central path, FY2030-39 low, FY2030-39 high, FY2040 low, FY2040 high).
Ranges are summed linearly for the set, as section 3 did, so the set's range is wide.

Working timeline (4-specification.md, "Dates"): the 2029 reconciliation act (R1) by about
mid-2029; the regular-order immigration act signed by about December 2029; registration and
the rolling registry open by October 1, 2030 (FY2031); the single plan's first wave January 1,
2031; the E-Verify start trigger met by about October 2031, so the first tranche no earlier
than October 1, 2032 (FY2033) and one tranche a year after it.
"""

YEARS = list(range(2030, 2041))
WINDOW = range(2030, 2040)


def path(values):
    return dict(zip(YEARS, values))


def grow(base_year, amount, rate, start):
    return {y: (amount * (1 + rate) ** (y - base_year) if y >= start else 0.0) for y in YEARS}


def lines():
    out = {}
    # Memo 1 A with the three changes, point 1 as recommended here (signature-date cutoff).
    # Section 3's bound: about +$50 billion over FY2030-39 (range -50 to +150) and about +$10
    # billion in FY2040 (-5 to +20), rising through the decade as in CBO's 2021 tables
    # (EV-IMM-600, EV-IMM-602). The later cutoff (signature, not introduction) adds a few
    # months of arrivals to registration: inside the range, not added.
    out['IMM-1.01-1.14: status, tiers A and B and registration (memo 1)'] = (
        path([0, 1, 2, 3.5, 5, 5.5, 6.5, 8, 9, 9.5, 10]), -50, 150, -5, 20)
    # Memo 2 C: waived fees below 200% of poverty and the IRS-SSA-USCIS matching build,
    # $3-6 billion over FY2030-39 and $0.2-0.5 billion in FY2040 (memo 2; EV-IMM-638,
    # EV-IMM-627). The build lands first, the waived fees with the 2031-33 filing peak.
    out['IMM-1.05-1.09: records-first registry and fee waivers (memo 2)'] = (
        path([0.5, 1.0, 0.9, 0.6, 0.4, 0.3, 0.2, 0.2, 0.2, 0.2, 0.3]), 3, 6, 0.2, 0.5)
    # Memo 3 B and B: about -$0.02 to -$0.06 trillion and -$5-8 billion in FY2040, from added
    # workers' taxes (EV-IMM-219, EV-IMM-220), growing as the added population builds.
    out['IMM-2.01-2.12: legal immigration and the workforce routes (memo 3)'] = (
        path([-1, -1.5, -2.5, -3.5, -4, -4.5, -5, -5.5, -6, -6.5, -7]), -60, -20, -8, -5)
    # Memo 4 D with counsel B: asylum corps $6-10B, refugee floor $5-10B, regional access
    # $3-5B, counsel $6-12B over FY2030-39 (memo 4; EV-IMM-302, EV-IMM-574), about $28.5B
    # central; FY2040 about $3B as the backlog clears (range 2.5-4).
    out['IMM-3.01-3.04, 3.12: asylum, refugees, regional access, counsel (memo 4)'] = (
        path([1.5, 2.5, 3.0, 3.2, 3.2, 3.2, 3.1, 3.0, 2.9, 2.9, 3.0]), 20, 40, 2.5, 4)
    # Point 8: repeal of the $100-a-year asylum-pending fee and the $550 first work-permit
    # charge (EV-IMM-043, EV-IMM-045). Roughly 1-2 million payers of the yearly fee falling as
    # the backlog clears and 300,000-400,000 first permits a year (judgment), net of CBO's 25%
    # offset for lower tax receipts (EV-IMM-621): about $0.25-0.35 billion a year.
    out['IMM-3.06: asylum fee repeals, net of the 25% offset (point 8)'] = (
        path([0.35, 0.35, 0.3, 0.3, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25]), 2, 5, 0.15, 0.4)
    # Memo 5 part 1, A's rules: the 30,000 cap against the base account's 41,500 beds
    # (EV-IMM-362) at about $150-190 a bed-day (EV-IMM-359, EV-IMM-628) nets against case
    # management at $20-40 a day for about 100,000 people (EV-IMM-355): about zero.
    out['IMM-4.05-4.06: the detention cap and case management (memo 5, A\'s rules)'] = (
        path([0] * 11), -10, 10, -1, 1)
    # Memo 5 part 1 B: replacing ICE. Transition (systems, facilities, re-credentialing,
    # legal) about $1-3 billion over FY2030-34, central $2 billion; the independent detention
    # inspector about $0.1 billion a year from FY2031 (judgment; no cost study in the register).
    restructure = path([0.2, 0.6, 0.6, 0.4, 0.2, 0, 0, 0, 0, 0, 0])
    inspector = grow(2031, 0.1, 0.025, 2031)
    out['IMM-4.01-4.02, 4.09: the DHS restructure and the detention inspector (memo 5, B)'] = (
        {y: restructure[y] + inspector[y] for y in YEARS}, 1.5, 5, 0.05, 0.3)
    # Memo 5 part 2: E-Verify operations at USCIS and SSA for a mandate, with the contest
    # and correction capacity IMM-4.14 requires. CBO put H.R. 1772's implementation at about
    # $635 million over five years (EV-IMM-394), about $0.13 billion a year in 2014-18;
    # grown and with faster correction, about $0.3-0.45 billion a year (judgment).
    out['IMM-4.12-4.15: E-Verify operations and error correction (memo 5, A)'] = (
        path([0, 0.15, 0.3, 0.35, 0.4, 0.4, 0.41, 0.42, 0.43, 0.44, 0.45]), 2.5, 6, 0.3, 0.7)
    # Memo 6 C: health coverage for people without status from the single plan's first wave
    # (January 1, 2031), $3-9 billion a year, and no five-year wait for memo 1's new permanent
    # residents, $2-4 billion a year, both rising with the population and prices (memo 6).
    out['IMM-1.20-1.35: the one eligibility table (memo 6)'] = (
        path([0, 4, 7, 8, 8.5, 9, 9.5, 10, 10.5, 11, 11.5]), 50, 110, 8, 15)
    # Memo 7 B: USCIS's appropriated public-interest work beyond memos 2 and 4 (backlog
    # clearance about $3 billion, EV-IMM-575; online filing and the Office of New Americans
    # about $1 billion; the naturalization discount and waivers $3-5 billion; the rest of the
    # registration surge): about $9.5 billion over FY2030-39, $1-2 billion in FY2040.
    out['IMM-6.01, IMM-5.04: USCIS beyond memos 2 and 4; naturalization fees (memo 7)'] = (
        path([0.6, 1.0, 1.3, 1.2, 1.0, 0.9, 0.9, 0.9, 0.9, 0.8, 1.5]), 5, 15, 1, 2)
    # Point 7 as decided: unobligated wall money redirected, not rescinded. Against CBO's
    # baseline, which projects the appropriation as spent (EV-IMM-034), about zero.
    out['IMM-3.07: wall money redirected (point 7)'] = (path([0] * 11), 0, 0, 0, 0)
    return out


def revenue_lines():
    """Revenue effects kept on their own lines (dossiers/TEMPLATE.md, 'One basis')."""
    # The H-1B fee (IF1, about $0.015 trillion, EV-IMM-577) is retained by USCIS and a
    # training fund. CBO nets fee collections by about 25% for lower tax receipts
    # (EV-IMM-621), which falls on the general fund: about $0.4 billion a year from FY2031.
    fee = grow(2031, 1.5, 0.025, 2031)
    return {'IF1: income-tax offset on the retained H-1B fee (25%)': (
                {y: 0.25 * fee[y] for y in YEARS}, 2.3, 4.5, 0.3, 0.5),
            'IMM-4.12: E-Verify mandate, on-budget revenue (JCT convention; memo 5, A)': everify()['on']}


def everify():
    """Memo 5 part 2 A on CBO and JCT's 2013 pattern (EV-IMM-394, EV-IMM-395).

    A national mandate: off-budget payroll revenue -$88 billion and on-budget revenue +$49
    billion (higher business profits, JCT's convention) over 2014-23, deficit +$30 billion.
    Per full year, about 85% of the decade being at full effect (judgment): off-budget -$10.4
    billion and on-budget +$5.8 billion in about 2018 dollars. Grown 4% a year (wages) to 2036
    and scaled by 0.3, the unauthorized workforce left after memo 1 against 2013's (judgment:
    about 2-3.5 million against about 8 million). Coverage of that workforce by tranche
    (judgment; unauthorized workers sit mostly in small firms and households): FY2033 0.2,
    FY2034 0.45, FY2035 0.7, FY2036 on 1.0.
    """
    cover = {2033: 0.2, 2034: 0.45, 2035: 0.7}
    share = {y: (1.0 if y >= 2036 else cover.get(y, 0.0)) for y in YEARS}
    full = lambda per_year: {y: per_year * 1.04 ** (y - 2018) * 0.3 for y in YEARS}
    on_full, off_full = full(49 / 8.5), full(88 / 8.5)
    on = {y: -on_full[y] * share[y] for y in YEARS}       # a general-fund gain (negative cost)
    off = {y: off_full[y] * share[y] for y in YEARS}      # Social Security's loss (a cost)
    on_sum = sum(on[y] for y in WINDOW)
    # Range: up to half as much again (a larger pool), down to no on-budget gain at all
    # (JCT's profit shift not realized).
    return {'on': (on, round(on_sum * 1.5, 1), 0.0, round(on[2040] * 1.5, 1), 0.0), 'off': off}


def total(rows):
    t = {y: sum(r[0][y] for r in rows.values()) for y in YEARS}
    lo = sum(r[1] for r in rows.values()); hi = sum(r[2] for r in rows.values())
    lo40 = sum(r[3] for r in rows.values()); hi40 = sum(r[4] for r in rows.values())
    return t, lo, hi, lo40, hi40


def fmt(row):
    return ' | '.join(f'{row[y]:.1f}' for y in YEARS[:-1])


def main():
    spend, rev = lines(), revenue_lines()
    print('| Line | ' + ' | '.join(str(y) for y in WINDOW) + ' | FY2030-39 | 2040 | Range FY2030-39 | Range 2040 |')
    print('| --- ' * 16 + '|')
    for name, (p, lo, hi, lo40, hi40) in {**spend, **rev}.items():
        print(f'| {name} | {fmt(p)} | {sum(p[y] for y in WINDOW):.1f} | {p[2040]:.1f} | {lo:.0f} to {hi:.0f} | {lo40:.1f} to {hi40:.1f} |')
    for label, rows in (('Spending lines', spend), ('Revenue effects', rev), ('All on the general fund', {**spend, **rev})):
        t, lo, hi, lo40, hi40 = total(rows)
        print(f'| **{label}** | {fmt(t)} | **{sum(t[y] for y in WINDOW):.1f}** | **{t[2040]:.1f}** | {lo:.0f} to {hi:.0f} | {lo40:.1f} to {hi40:.1f} |')
    off = everify()['off']
    print(f"\nOff-budget (Social Security's funds), the E-Verify mandate: {sum(off[y] for y in WINDOW):.1f} "
          f"over FY2030-39 and {off[2040]:.1f} in FY2040 (a loss to the funds).")
    on = everify()['on'][0]
    adm = spend['IMM-4.12-4.15: E-Verify operations and error correction (memo 5, A)'][0]
    unified = sum(off[y] + on[y] + adm[y] for y in WINDOW)
    print(f'E-Verify on the unified budget (both funds, with operations): {unified:.1f} over FY2030-39, '
          f'{off[2040] + on[2040] + adm[2040]:.1f} in FY2040.')


if __name__ == '__main__':
    main()
