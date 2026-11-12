#!/usr/bin/env python3
"""Immigration's decided general-fund lines on federal fiscal years, FY2030-40.

Role: section 6's path (`dossiers/immigration/6-cost.md`, part 1). Status: draft (board row
I4). Project arithmetic on the anchors section 3 and the memos give, as decided in
DEC-2026-11-12-07; not a score. Run: python3 dossiers/immigration/tools/immigration_path.py

Conventions: nominal $ billion, federal cost against the January 2029 law, a cost positive,
on the general fund (on-budget) unless a line says otherwise. FY y runs from October of y-1.
The status, registry, asylum and courts, detention and USCIS lines come from
`immigration_model.py`; the others are judgment unless an evidence ID is given (DEC-2026-11-10-07);
`3-design.md`, "What the options cost" and "IMM-1's score, re-derived", gives each basis.
Each line carries (central path, FY2030-39 low, FY2030-39 high, FY2040 low, FY2040 high).
Ranges are summed linearly for the set, as section 3 did, so the set's range is wide.

Working timeline (4-specification.md, "Dates"): the 2029 reconciliation act (R1) by about
mid-2029; the regular-order immigration act signed by about December 2029; registration and
the rolling registry open by October 1, 2030 (FY2031); the single plan's first wave January 1,
2031; the E-Verify mandate's first tranche no earlier than October 1, 2030, on a passing
Inspector General check, assumed to come about July 1, 2031 (FY2031 Q4), and one tranche a year
after it (IMM-4.13, DEC-2026-11-12-12).
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

YEARS = list(range(2030, 2041))
WINDOW = range(2030, 2040)


def path(values):
    return dict(zip(YEARS, values))


def grow(base_year, amount, rate, start):
    return {y: (amount * (1 + rate) ** (y - base_year) if y >= start else 0.0) for y in YEARS}


def lines():
    import immigration_model as m
    runs = {c: m.lines(c) for c in ('central', 'low', 'high')}

    def from_model(key):
        lo = min(m.window(runs[c][key]) for c in runs); hi = max(m.window(runs[c][key]) for c in runs)
        lo40 = min(runs[c][key][2040] for c in runs); hi40 = max(runs[c][key][2040] for c in runs)
        return (runs['central'][key], round(lo, 1), round(hi, 1), round(lo40, 1), round(hi40, 1))

    out = {}
    # Memo 1 A with the three changes (immigration_model.status_fiscal: CBO's H.R. 6 score,
    # EV-IMM-600, scaled, grown and netted for the single plan). The model's input range is
    # narrow; the range kept is section 3's bound (-50 to +150, -5 to +20), which also covers
    # the pattern itself (S. 744's sign, EV-IMM-205). The signature-date cutoff adds a few
    # months of arrivals to registration: inside the range, not added.
    p1 = from_model('memo1')
    out['IMM-1.01-1.14: status, tiers A and B and registration (memo 1)'] = (p1[0], -50, 150, -5, 20)
    # Memo 2 C: waived fees on the registry's filings and the matching build (immigration_model.uscis).
    out['IMM-1.05-1.09: records-first registry and fee waivers (memo 2)'] = from_model('memo2')
    # Memo 3 B and B: about -$0.02 to -$0.06 trillion and -$5-8 billion in FY2040, from added
    # workers' taxes (EV-IMM-219, EV-IMM-220), growing as the added population builds. Not in
    # the model: a fiscal reading of labor-market evidence, kept as cited judgment.
    out['IMM-2.01-2.12: legal immigration and the workforce routes (memo 3)'] = (
        path([-1, -1.5, -2.5, -3.5, -4, -4.5, -5, -5.5, -6, -6.5, -7]), -60, -20, -8, -5)
    # Memo 4 D with counsel B: the officer corps, the refugee floor, regional access and
    # appointed counsel (immigration_model.asylum_refugees and eoir).
    out['IMM-3.01-3.04, 3.12: asylum, refugees, regional access, counsel (memo 4)'] = from_model('memo4')
    # Memo 4 part 2: judge teams above today's 753 judges (EV-IMM-103), hired 250 a year to the
    # corps that clears the court backlog by FY2035, costed at about $1.5 million a team a year
    # (EV-IMM-644, EV-IMM-645), shrinking by attrition once it clears (immigration_model.eoir).
    out["IMM-3.08: judge teams above today's corps (memo 4, part 2)"] = from_model('judges')
    # Point 8: repeal of the $100-a-year asylum-pending fee and the $550 first work-permit
    # charge (EV-IMM-043, EV-IMM-045). Roughly 1-2 million payers of the yearly fee falling as
    # the backlog clears and 300,000-400,000 first permits a year (judgment), net of CBO's 25%
    # offset for lower tax receipts (EV-IMM-621): about $0.25-0.35 billion a year.
    out['IMM-3.06: asylum fee repeals, net of the 25% offset (point 8)'] = (
        path([0.35, 0.35, 0.3, 0.3, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25]), 2, 5, 0.15, 0.4)
    # Memo 5 part 1, A's rules: the cap against the base account's beds, against case
    # management's added cost over today's alternatives (immigration_model.detention).
    out['IMM-4.05-4.06: the detention cap and case management (memo 5, A\'s rules)'] = from_model('detention')
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
        path([0.15, 0.3, 0.35, 0.4, 0.4, 0.41, 0.42, 0.43, 0.44, 0.45, 0.46]), 3, 6.5, 0.3, 0.7)
    # Memo 6 C, amended for health (Espen, November 12, lead session): the single plan covers
    # lawful or registered status; no status, emergency care as today. Added coverage only for lawful
    # residents above care's population base (memo 3's added immigrants and refugees), on care's own
    # path, and no five-year wait, $2-4 billion a year (immigration_model.table).
    out['IMM-1.20-1.36: the one eligibility table (memo 6)'] = from_model('memo6')
    # Memo 7 B: USCIS's appropriated public work beyond memos 2 and 4: backlog clearance
    # (EV-IMM-575), online filing and the Office of New Americans, the naturalization discount
    # and waivers, and hiring ahead of fees (immigration_model.uscis).
    out['IMM-6.01, IMM-5.04: USCIS beyond memos 2 and 4; naturalization fees (memo 7)'] = from_model('memo7')
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
    (judgment; unauthorized workers sit mostly in small firms and households): 0.2, 0.45, 0.7
    and 1.0 by tranche, from the first tranche about July 2031 (immigration_model.everify_coverage).
    """
    import immigration_model as m
    share = m.everify_coverage()
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
