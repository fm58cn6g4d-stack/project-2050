# Shared rules across dossiers

Role: the few rules that more than one flagship depends on. For each rule, the note gives current law, the working answer the first dossier uses, and which dossier owns the final answer. Status: draft working note (stage C). It records no decisions. Espen decides each rule in the owner dossier's design section, and this note is updated to match.

## Why this note exists

The flagships interact mainly through a few shared rules, not through every design choice. Examples include what counts as income, which immigrants are eligible, who verifies and pays, and what conditions attach to help. The plan keeps its order: depth first, one dossier at a time (`charter/PLAN.md` 3 and 6). This note keeps a dossier written early from silently fixing a rule that a later dossier owns.

## How dossiers use it

1. **State the dependency.** A dossier's design section lists each shared rule it relies on. The list gives the working answer and a range, the way models label an assumption (`charter/PLAN.md` 3.4). The specification keeps that rule in one place, so it can change without rewriting the rest.
2. **The owner decides.** The owner dossier's design section brings the rule to Espen, in a decision memo where it is a real fork. This note is then updated to the decided answer.
3. **Collisions reopen by memo.** When an owner's answer conflicts with an earlier dossier's working answer, the owner's memo says so. Espen then decides whether the earlier choice is reopened. Decision memos already state what would change them, so no other machinery is needed.

A rule is added here only when two dossiers actually depend on it. Every other choice stays in its own dossier.

## The rules

### 1. What counts as income for rent and benefits

- **Current law.**
  - Families in public housing and most other HUD-assisted housing pay the highest of three amounts: 30% of monthly adjusted income, 10% of monthly gross income, or a welfare rent where one applies (42 U.S.C. 1437a(a)(1)).
  - Public housing families may instead choose a flat rent each year (1437a(a)(2)). It is set per unit and may not fall below 80% of the area's fair market rent (1437a(a)(2)(B)(i)), so a flat-rent family's rent does not rise with income or new benefits.
  - Voucher holders are excluded from that rule. Their payment rules are in 42 U.S.C. 1437f(o), not yet checked for this note.
  - "Income" counts all sources, minus listed exclusions and any amount another federal law excludes (1437a(b)(4)).
  - Tax refunds and advance payments of refundable credits under the tax code do not count as income for any federally funded program (26 U.S.C. 6409).
- **Why it is shared.** Every new cash benefit from another flagship could raise rent in the 1437a programs: about 30 cents of each dollar, or a similar share for voucher holders. That cancels part of the benefit for assisted renters and lowers the housing subsidy in the budget.
  - The child benefit (FAM-1) is designed as a monthly refundable credit with advance payments (`legacy/domains/domain-family.md`, FAM-1). On that design, section 6409 already keeps it out of rent. If it were paid some other way, it would count unless a statute excludes it.
  - Paid leave (FAM-3), wage floors (LAB-4) and any income support outside the tax code would count. For wages this is how the rent rule is meant to work. For new benefits it is a choice.
- **Housing's working answer.**
  - Keep the 30%-of-adjusted-income rule.
  - Assume no new benefit from another flagship raises tenant rent.
  - Range: from no effect up to 30 cents per dollar of any new benefit paid outside the tax code. Section 6 of the housing dossier tests both ends.
- **Owner:** the secure floor (flagship 1). It designs the benefits and how they are paid, and it decides whether each one counts for other programs. The household model checks the combined effect.

### 2. How fast help falls as earnings rise

- **Current law.**
  - Housing help falls by about 30 cents per added dollar of adjusted income (rule 1).
  - In most cases, a rise in earnings is not counted until the next annual review (1437a(a)(6)(A)(iv)).
  - Tax credits, health subsidies and food aid each phase out on their own schedules.
- **Why it is shared.** When phase-outs stack, a raise can leave a family barely better off, or worse off. The housing, secure floor, care and work flagships each set one layer.
- **Housing's working answer.** Keep the 30% rate and current review timing. Add no new phase-out.
- **Owner:** the secure floor, with the household model. It sets a ceiling on the combined rate at which help falls for typical households, and each flagship designs within it. Until then, each dossier reports its own phase-out rate in section 4.

### 3. Which immigrants are eligible

- **Current law.**
  - HUD housing help goes only to the immigrant statuses listed in Section 214 of the Housing and Community Development Act of 1980 (42 U.S.C. 1436a(a)): lawful permanent residents, refugees and asylees, and a few others.
  - Families whose members have mixed statuses receive prorated help (1436a(b)(2)). When at least one member's eligibility is established and no other member is established as ineligible, help is prorated by the number of members whose eligibility is established.
  - Before help starts, eligibility of at least one family member must be established and verified (1436a(i)(1)); a housing agency may elect not to verify before providing help (1436a(i)(2)(A)). The sentence that "eligibility" of a family means that of each member (1436a(i)(3)) only defines the word for that subsection. It does not require every member to be verified before help starts.
  - Other programs follow the 1996 welfare law's own lists.
- **Why it is shared.** Earned legalization (IMM-1) creates new statuses. The immigration file's baseline bars its second tier from means-tested federal benefits for five years, on the 2013 Senate bill's model, while the ACA subsidies and the child credit follow their own rules (`legacy/domains/domain-immigration.md`, IMM-1 cost).
  - A new status would not appear on Section 214's list unless the law adds it.
  - So the immigration, housing, care and secure-floor flagships could each give the same family a different answer.
  - The guarantee's reach to homeless people and families with children (housing fork 8) depends on this.
- **Housing's working answer.**
  - Current law, unchanged: Section 214's list, with proration for mixed-status families.
  - The housing dossier proposes no new status rules of its own.
- **Owner:** the immigration flagship (flagship 6). It sets one eligibility table for every program a new status touches. Each other flagship states any exception it needs in its own design section.

### 4. Income lines and household definitions

- **Current law.**
  - HUD sets eligibility by area median income. "Extremely low income" means a very low-income family whose income does not exceed the higher of the federal poverty guideline for its size and 30% of area median (1437a(b)(2)(C)). The line is therefore capped at the very-low-income limit, and the poverty-guideline alternative does not apply in Puerto Rico or other territories.
  - Health and food programs use the federal poverty guidelines.
  - Tax credits use tax-filing units.
- **Why it is shared.** Housing's guarantee is defined by area median income (housing fork 2). Other flagships will likely use poverty lines or tax units. Families moving between programs face different tests, and models must translate between them.
- **Housing's working answer.** Keep area median income for housing, which reflects local rents.
- **Owner:** the secure floor, for the definitions and the translation between them. The democratic renewal foundation owns any common application or shared verification (rule 5).

### 5. Who verifies, pays and answers for mistakes

- **Current law.**
  - Housing agencies administer vouchers and verify income themselves.
  - They may rely on timely income determinations from other means-tested programs such as TANF, Medicaid and SNAP, to the extent the information is available to them (1437a(a)(7)(D)). That safe harbor covers income before deductions, so the agency still applies the housing deductions itself. They also get federal income-matching data (1437a(a)(7)(E)).
  - The IRS pays the child credit; states run Medicaid.
- **Why it is shared.** Each flagship adds caseloads to agencies that are already stretched. Emergency rental aid started slowly, and improper payments went unmeasured [EV-HOU-150] [EV-HOU-154]. Verifying income once and reusing it saves work in every program.
- **Housing's working answer.**
  - Housing agencies keep administering.
  - The dossier's delivery section uses the income-reuse authority already in law.
  - A federal sponsor or backstop where state or local participation fails, as Espen's October 26 housing direction says.
- **Owner:** the democratic renewal foundation (state capacity: CAP-13, payment systems). Each flagship's delivery section states its own needs (`charter/PLAN.md` 3.1).

### 6. Conditions on help

- **Current law.** It varies by program.
  - TANF holds states to minimum work-participation rates (42 U.S.C. 607).
  - Every adult resident of public housing must give 8 hours a month of community service or join an economic self-sufficiency program, with exemptions for older adults, people with disabilities, and others (42 U.S.C. 1437j(c)).
  - The Medicaid and food-assistance rules are not read for this note.
- **The direction so far.** The participation-support program (LAB-10, approved October 26) is "an offer, not a work condition on income, housing, health or food assistance" (`legacy/domains/domain-labor.md`, LAB-10). Housing's recommended homelessness approach offers services without requiring them (housing fork 5, option 5B, not yet decided).
- **Housing's working answer.**
  - Work half: no work conditions on the guarantee. This departs from the public housing service requirement above, which the housing dossier would have to address in section 4.
  - Treatment half: a range, because housing memo 5 is still open. It runs from no treatment condition (memo 5 options A and B, where services and recovery housing are offered, never required) to treatment as a condition of help (option C, the July 2025 executive order's approach) at the other.
- **Owner:** the work flagship (flagship 5) records the cross-program principle; each flagship applies it. If Espen decides otherwise in any dossier, the others are reviewed.

### 7. Services that make housing work

- **Current law.** Medicaid can pay for home and community-based services at state option, through waivers (42 U.S.C. 1396n(c)(1)) or a state plan amendment for people with incomes up to 150% of the poverty line (1396n(i)(1)). Both exclude room and board. Whether a state pays for particular housing-related services under these authorities is a matter of federal and state guidance that this note has not read.
- **Why it is shared.** Housing First depends on services being available (housing fork 5). Care at home for older and disabled people depends on homes they can stay in.
- **Housing's working answer.** Services are offered through existing Medicaid and local programs; the housing dossier does not pay for them.
- **Owner:** the care flagship (flagship 2, HLT-4).

### 8. Workforce

- **Why it is shared.** About a third of construction trades workers are immigrants [EV-HOU-055]. Care workers are needed for the care flagship. Both depend on immigration and apprenticeship design.
- **Housing's working answer.** Supply estimates are conditional on the construction workforce and tested against a scenario where it shrinks (housing fork 7, recommended, not yet decided).
- **Owners:**
  - the immigration flagship, for visas and legalization;
  - the work flagship, for apprenticeships (LAB-8).

### Already shared and settled

- **How programs are paid for and who gains.** These rules are already Espen's, recorded in `charter/outcomes.md` (OUT-11) and the legacy D3 and D4 decisions.
  - Every income group below the top is better off on net, with new revenue mostly from the top 1% and corporations (D3).
  - Permanent programs are paid for at maturity, from FY2040 (D4).
  - Every dossier applies them. Fair financing settles the totals once designs are fixed (`charter/PLAN.md` 3.1).

## Open checks

- **Voucher payment rules.** The voucher program's tenant-payment rule is in 42 U.S.C. 1437f(o), not checked here. Check it before housing section 4.
- **HUD's own exclusions.** HUD's regulations list further income exclusions (24 CFR 5.609). Read them when the secure floor designs its benefits.
