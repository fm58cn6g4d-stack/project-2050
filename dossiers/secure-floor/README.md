# Dossier: A secure floor for every household (flagship 1)

Role: the secure floor flagship (`charter/PLAN.md` 3.1). Status: started, stage D (board rows S1 and S2). Sections 1 and 2 are drafted; no design choice is made here. Level: every item is at L1 (`DEC-2026-10-30-03`); the legacy designs are working choices, weighed as options (`DEC-2026-10-30-02`). The target is L3, with priority pieces at L4.

**What it brings together** (`charter/PLAN.md` 3.1, exactly):
- a monthly child benefit;
- income support and participation help;
- paid leave;
- Social Security protection.

## Scope

**In the flagship** (`agenda/agenda.csv`, `home_dossier` = `secure-floor`):

| Part | Agenda items | Legacy design (`legacy/domains/`) | Who chose it |
| --- | --- | --- | --- |
| A. The child benefit | FAM-1; FAM-1A to 1D | `domain-family.md`, FAM-1. FAM-1D, the American Family Act, chosen | Espen, October 24, 2026 (`legacy/governing/project-2050-governing-decisions.md`, "Family package adopted"); a working choice under `DEC-2026-10-30-02` |
| B. Income support and participation help | LAB-10 | `domain-labor.md`, LAB-10: a $100 billion FY2030-39 envelope, run by the Labor Department, "an offer, not a work condition" | Espen, October 26, 2026 (governing decisions, "Recovery and Solvency recommendations approved": the envelope; "Strategic-review response": the direction); a working choice |
| C. Paid leave | FAM-3; FAM-3A to 3E | `domain-family.md`, FAM-3. FAM-3A, 12 weeks of social insurance at 0.6% of wages with a step-up toward 1.10%, run by the Social Security Administration | The 12 weeks and 0.6% are the legacy file's choice, not a recorded decision of Espen's; the no-backstop rule is in legacy D4's reading (governing decisions, D4); Espen approved the 1.10% ceiling ("Recovery and Solvency recommendations approved") and SSA administration ("Development agency and paid-leave administration accepted"), both October 26, 2026; a working choice |
| D. Social Security | SS-1 to SS-10, SS-10A to 10C | `domain-social-security.md`. Legacy decision D8: solvency first with a targeted increase, as its own bill in spring 2030; SS-5 added October 26 | D8 by Espen before October 28 (governing decisions, D8); SS-5 selected October 26; a working choice |

**Income support: what the flagship covers and what it leaves.** The plan's "income support" has no legacy design of its own. The agenda has no item for SNAP, SSI, unemployment insurance, TANF or the earned income credit, and the legacy domain files design none of them. They appear only as context: the household model's food assistance channel, AI-4's transition benefit, which "sits on the unemployment-insurance base" (`legacy/domains/domain-ai.md`, AI-4, home `agenda/ai`), and LAB-10's rule that participation is never a condition on "income, housing, health or food assistance". This dossier therefore:
- maps all of them in section 1, as they will stand in January 2029, because they make up the floor a family actually stands on and because their phase-outs stack with the plan's (shared rules 1 and 2);
- weighs in section 2 what the evidence says about each where it bears on the flagship;
- adds no agenda item. Whether the flagship should carry SNAP, SSI or earned income credit items (for example undoing the 2025 law's SNAP changes) is a fork for S3 (below);
- leaves unemployment insurance to the work flagship (flagship 5, "support when jobs change"), with AI-4, unless Espen moves it. The minimum wage (LAB-4) is the work flagship's.

**Outcomes it serves** (`charter/outcomes.md`):
- OUT-01, child poverty comes as close to eradicated as possible (the child benefit, income support);
- OUT-02, households can plan beyond the next paycheck (paid leave, Social Security, income support);
- OUT-06, fair pay and real power at work (paid-leave access is one of its measures);
- OUT-08, time and practical freedom (paid leave);
- OUT-11, the fairness and fiscal tests (D3, D4), which every dossier answers to.

## Layout and order of work

**Layout (chosen November 12, 2026, board row S1).** Sections 1 and 2 are one file each, `1-problem.md` and `2-what-works.md`, with a part for each subject (A to D, as in the scope table) and a fifth, cross-cutting part E on how the floor fits together: income definitions, phase-outs and income lines (shared rules 1, 2 and 4). *Why:* the four parts are drafted together, and they meet in the same households through the shared rules. A map of stacked phase-outs has to see every program at once, and it would be split across four files otherwise. Care used separate part files because health was already decided when part B began (`dossiers/care/README.md`); that reason does not apply here. Sections 3 onward may split by part, because Social Security travels in its own bill (section 310(g) of the Budget Act keeps it out of reconciliation) and is financed by its own trust fund. That choice is made with S3's memo set.

| Section | File | Status |
| --- | --- | --- |
| 1. The problem | `1-problem.md`: child poverty and who the current credit misses; income support's holes; paid leave access; Social Security's depletion date and what happens then; the stacked phase-outs; the January 2029 baseline | Draft (S2) |
| 2. What works | `2-what-works.md`: the 2021 expanded credit (poverty and the contested employment evidence), Canada's child benefit, cash trials, the earned income credit literature; state paid leave programs and the research; Social Security's anti-poverty record, minimum benefits, caregiver credits, solvency packages; coordinating phase-outs at home and abroad; each against the bills | Draft (S2) |
| 3. Design choices | `3-design.md` and `memos/`, one batched memo set (S3) | Next |
| 4-9 | Specification, delivery, cost, validation, what would change our minds, public case | Later |

## Files and ID ranges

- `evidence.json`: evidence code **EV-SEC**. Blocks: 001-099 the January 2029 baseline and the size of the problem; 100-199 kept free; 200-299 the child benefit and work-linked credits; 300-399 paid leave; 400-499 Social Security; 500-599 income definitions and phase-outs; 600-699 kept for S3.
- Sources: **SRC-3600 to SRC-3999 are reserved for the secure floor** (this README, November 12, 2026). Sub-blocks: 3600-3669 baseline; 3670-3739 child benefit; 3740-3809 paid leave; 3810-3879 Social Security; 3880-3949 phase-outs; 3950-3999 kept for S3. IDs are assigned by hand, because `library/build_catalog.py` assigns the next free number even inside a reserved block (`charter/PROGRESS.md`, "Known gaps").
- The register also cites other dossiers' entries where they already cover a fact (for example EV-HOU-401, CBO's average effective marginal tax rate; EV-HOU-416 to 418, the earned income credit's and SNAP's rates; EV-CAR-001 to 050, the 2025 law's Medicaid changes; EV-CAR-501, 502 and 584, the dependent care credit).

## Shared rules the secure floor owns or touches

From `dossiers/shared-rules.md`; this dossier proposes answers in section 3 and never rewrites another owner's rule:
- **Rule 1, what counts as income for rent and benefits:** owned here. The secure floor designs each benefit and decides whether it counts for other programs. Housing's working answer is that no new benefit raises rent, with a range of 0 to 30 cents a dollar; Espen decided that voucher rent ignores the value of free or capped child care (`DEC-2026-11-10-03`).
- **Rule 2, how fast help falls as earnings rise:** owned here, with the household model. The secure floor sets a ceiling on the combined rate for typical households; each flagship designs within it. Housing (30% of adjusted income, no new phase-out) and care (child care's 7% of income above 85% of state median income, `DEC-2026-11-11-03`) have already set layers.
- **Rule 4, income lines and household definitions:** owned here, for the definitions and the translation between them (poverty guidelines, area median income, state median income, tax units).
- **Rule 5, who verifies, pays and answers for mistakes:** owned by the democratic renewal foundation. The secure floor states its own needs there (the IRS for monthly payments, SSA for leave and Social Security).
- **Rule 3, immigrant eligibility:** owned by the immigration flagship. The 2025 law's Social Security number rules for the child credit are a current-law fact this dossier maps.
- **Rule 6, conditions on help:** the work flagship records the principle; LAB-10's "an offer, not a work condition" is this dossier's working direction.

## Seams with other dossiers

| Seam | Other dossier | What is settled | What the secure floor does |
| --- | --- | --- | --- |
| Child care costs | Care, part C (`DEC-2026-11-11-03`; `dossiers/care/3c-design-child-care.md`, point 4) | Child care free at or below 85% of state median income, at most 7% of income above it; the 2025 law's dependent care tax changes kept | Decides whether the child and dependent care credit becomes refundable (care left it here); stacks the 7% cap in the phase-out ceiling |
| Paid family caregivers and caregiver credits | Care, part B (memo 9 E, `DEC-2026-11-11-02`) | Care pays family caregivers through the home benefit | Decides any Social Security caregiver credit (care's memo 9 left it here; legacy SS-B4, unscored) |
| Rental help | Housing (`dossiers/home/4-specification.md`, rules 1 and 2) | Rent is 30% of adjusted income; refundable credits are not income (26 U.S.C. 6409) | Decides whether paid leave, Social Security increases and any cash benefit outside the tax code count for rent; sets the ceiling with housing in it |
| Health coverage | Care, part A (`DEC-2026-11-10-09`, `-11`) | Single-payer by 2035; the premium credits and Medicaid lines fall away at the endpoint | Counts the health layers in the phase-out map for 2029-34, when they still bind |
| The minimum wage, unemployment insurance, support when jobs change | Work (flagship 5); AI-4 (`agenda/ai`) | Nothing decided | Leaves them there; maps unemployment insurance as part of the floor in section 1 |
| Financing | Fair financing (Codex) | D3 and D4 (OUT-11) | Designs no taxes. SS-1, SS-2 and SS-5 are Social Security's own financing and FAM-3's contribution is the leave fund's: this dossier describes them, and the settlement weighs them |
| Delivery | Democratic renewal (rule 5; CAP-7) | Nothing decided | States what the IRS and SSA need |

## What S3 needs from the household model

The household model (`charter/PLAN.md` 3.4, `MOD-household`) is not built yet; it unifies the incidence model (`models/tools/incidence-model.py`) and the child-poverty microsimulation (`models/tools/child-poverty/`), which has no model card. No model code is written in this step. S3's memos will need from it:
1. **Combined phase-out rates by family type**: cents lost per added dollar for a single parent with two children, a married couple with two children and a single adult, at 50% to 300% of the poverty line, with each layer shown (taxes, the child credit, the earned income credit, SNAP, housing, health premiums in 2029-34, child care's 7% cap). Section 1, part E gives the statutory rates by hand; the model gives the distribution and the share of families at each rate.
2. **Child poverty and deep poverty under each child-benefit option** (FAM-1A to 1D and any new one) on the Supplemental Poverty Measure, with take-up shown and without any employment response, then with the range the employment literature supports (section 2, part A).
3. **Who the current credit misses and who each option reaches**: children below the full credit, children excluded by the Social Security number rule, non-filers.
4. **Paid leave benefits and contributions by earnings**, for the D3 household test at the 0.6% and 1.10% rates.
5. **Social Security**: the minimum benefit's and caregiver credit's reach by lifetime earnings, and the cut each household would face at depletion. The 75-year balance stays with SSA's actuaries and the budget model's fund module.
6. **The rent and benefit offsets** (rule 1) at 0 and 30 cents, for the housing dossier.

## Forks for S3 (not questions for Espen yet)

No decision blocks S3, so nothing goes on the board's "Questions for Espen". S3's memo set should put these to Espen, two to four options each:
1. **The child benefit's design.** FAM-1D (the American Family Act) against the 2021 design (FAM-1A), a supplement (FAM-1B), full refundability of today's $2,200 credit (FAM-1C), and a Canada-style income-tested benefit; its age profile, the newborn payment, indexing and phase-out.
2. **Who the child benefit reaches.** The 2025 law's Social Security number rules against an ITIN or child-only test (shared rule 3, with the immigration flagship); a non-filer route; who receives it (the caregiver or the tax filer).
3. **Delivery.** Through the IRS as a refundable credit with monthly advances (the legacy choice; it keeps the benefit out of rent under section 6409 and is paid without appropriations), or as a benefit paid by SSA or Treasury outside the tax code, with what that would cost families under rule 1.
4. **The earned income credit.** Leave it, expand the childless credit, or fold part of it into the child benefit (as Romney's Family Security Act would), given the contested employment evidence.
5. **Income support beyond the credits.** Whether the flagship carries SNAP, SSI or other items: undoing the 2025 law's SNAP changes, raising SSI's $2,000 asset limit, the SSI benefit level. New agenda items would start at L1.
6. **Participation help (LAB-10).** Its form, scale and agency against the $100 billion envelope, and its line with apprenticeships, national service and AI-4.
7. **Paid leave.** Weeks, wage replacement (progressive, higher for low earners), job protection, the contribution and its step-up (FAM-3A against 3B to 3E), a federal program against a floor that state programs meet, and SSA as administrator.
8. **Social Security.** The D8 package (SS-1 to SS-4 with SS-5) against the closers (SS-6 to SS-9) and the bipartisan track (SS-10A to 10C), re-tested on the 2026 Trustees Report; the minimum benefit, CPI-E and a caregiver credit; what the plan does if depletion comes before a law does.
9. **The phase-out ceiling** (shared rule 2): its level, which layers count, and whether the plan's new benefits are excluded from other programs' income (rule 1).
10. **The dependent care credit's refundability** (from care, part C).

## Open questions for Espen

None yet. S3 brings the memo set.
