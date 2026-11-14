# Dossier: Clean, affordable power and a prepared country (flagship 4)

Role: the clean power flagship (`charter/PLAN.md` 3.1). Status: **decided**, stage E; sections 4-9 **reviewed (L2)** by the milestone review (`review-milestone.md`, #344), with its fixes applied; L3 after the booking and a short re-check. Espen decided the memo batch on November 13: memos 1-7 all as recommended, with memo 7's wage insurance set by Espen (`DEC-2026-11-13-06`), and points 1-14 all yes (`DEC-2026-11-13-07`). Level: the decided items are at **L2** (`agenda/agenda.csv`, `home_dossier` = `clean-power`); options no memo weighed stay at L1. **Not booked:** the legacy climate rows in the budget model stay as they are until the booking step, after the milestone review. The decided set is about **$1.85 trillion over FY2030-39 and $146 billion in FY2040** on the general fund, about +$0.04 trillion and −$18.5 billion against the booked rows (`6-cost.md`), on the ledger's convention for the transition share; re-reviewed on the energy model (`review-m4.md`, `DEC-2026-11-13-12`).

**What it brings together** (`charter/PLAN.md` 3.1, exactly): "Carbon fee and dividend, clean power and grid, adaptation and insurance, the clean-industry transition."

## Scope

**In the flagship:** the legacy climate and energy file (`legacy/domains/domain-climate.md`, rows CLI-1 to CLI-13 and the October 28 "Package A" components) and the carbon fee rows of the legacy revenue file (REV-C1, REV-C2, REV-C3 and their options), which the agenda already homes here. One more item is re-homed here in this step: REV-CB1, the carbon fee's combustion receipts change under Package A, which is part of the carbon fee's own accounting (it was under fair financing).

| Part | Agenda items | Legacy design |
| --- | --- | --- |
| A. Carbon fee and dividend | REV-C1 (C1A chosen; C1B-C1F), REV-C1P, REV-CB1, REV-C2, REV-C2B, REV-C3; CLI-2 (2A chosen; 2B-2I), CLI-2O | $25 a ton in 2030 rising to $150 by 2037, road fuels exempt; 80% returned equally per adult; 20% to a transition share; a border adjustment; the IRA methane charge reinstated |
| B. Clean power and the grid | CLI-1 (1A chosen; 1B-1E), CLI-3 (3A; 3B-3E), CLI-4 (4A; 4B-4H), CLI-6 (6A; 6B-6E), CLI-9, CLI-10, CLI-10G | Restored and refundable clean-energy credits; a Clean Energy Standard; Clean Air Act authority in statute; grid and utility rules; contracts for difference; public power as builder of last resort |
| C. Households and bills | CLI-5 (5F chosen; 5A-5E), CLI-5L, CLI-5W | Bill protection, LIHEAP and Weatherization, low-income heat pumps |
| D. Adaptation and insurance | CLI-7, CLI-7B, CLI-7C, CLI-7K, CLI-7N, CLI-8 (8B declined, 8C option), CLI-13, CLI-13A, CLI-13F | FEMA and mitigation, NFIP, a federal reinsurance facility, climate risk in federal lending, farms and forests |
| E. Workers and places in transition | CLI-11, CLI-12; the transition share of REV-C1 | Coal securitization and worker guarantees; state payments for results |

Every one of these is a legacy working choice, not a decision of Espen's for this plan (`DEC-2026-10-30-02`, `DEC-2026-10-30-03`); section 3 weighed them as options, and Espen decided them (`DEC-2026-11-13-06`, `DEC-2026-11-13-07`).

**Outside the flagship, named where they touch it:** fossil-fuel tax preferences (REV-TS3) and the public investment corporation (REV-E2) stay with fair financing; the heat standard (LAB-6) and workforce programs (LAB-8) with work; road-fuel pricing and the clean-vehicle charges (MOV-29, MR2 to MR4) with transportation; data-center rules shared with the AI file (AI-6A); international climate finance (NSC-9) with national security; home repair's front door to the clean-power programs (HOU-12) with housing.

**Outcomes it serves** (`charter/outcomes.md`): named in section 1.

## Files and status

| Section | File | Status |
| --- | --- | --- |
| 1. The problem | `1-problem.md`: bills and energy hardship; demand and reliability; emissions; climate damage and insurance; workers and places; the January 2029 baseline table; the legacy record restated | Draft (E-C1, PR #315) |
| 2. What works | `2-what-works.md`: carbon pricing and dividends at home and abroad; the IRA's record and the 2025 repeal; grid and permitting; public power and finance; clean and firm power costs; clean industry; adaptation and insurance; transitions; failures to avoid | Draft (E-C1, PR #315) |
| 3. Design choices | `3-design.md` and `memos/`: eleven forks in seven memos, fourteen yes-or-no points, inherited assumptions traced, the fiscal report against the booked rows | **Decided** (`DEC-2026-11-13-06`, `DEC-2026-11-13-07`; E-C1, PRs #315, #317) |
| 4. Specification | `4-specification.md` and `provisions.json` (53 provisions, built by `tools/build_provisions.py`): the price and the dividend, credits and industry, standards and goals, the grid, bills, adaptation, the transition guarantee, farms and forests | Reviewed (L2), fixes applied |
| 5. Delivery | `5-delivery.md`: every job through an existing agency, record and payment system (`DEC-2026-11-13-08`); capacity, timeline, remedies, states, rural delivery | Reviewed (L2), fixes applied |
| 6. Cost | `6-cost.md`, with `tools/clean_power_path.py` and `tools/coverage_read.py` (a read of the carbon model for memo 1 B): the decided set by fiscal year against the booked rows, what the total leaves out, the fiscal-rule report, the booking's steps | Reviewed (L2), fixes applied; not booked |
| 7. Validation | `7-validation.md`: against outside figures; what the models miss; how it lands with the plan; who it reaches (the carbon channel by quintile under memo 1 B); emissions; objections; signs of failure | Reviewed (L2), fixes applied |
| 8. What would change our minds | `8-change-our-minds.md` | Reviewed (L2), fixes applied |
| 9. Public case | `9-public-case.md`, with its source table | Reviewed (L2), fixes applied |
| Milestone review | `review-milestone.md`: the L2/L3 review (#344); its fixes are #346 | Current |
| Re-review on the energy model | `review-m4.md`: the decided set run on MOD-energy (`DEC-2026-11-13-12`), with what the booking must use | Current |

## Evidence and sources

- `evidence.json`: evidence code **EV-CLP**. 364 entries in the first PR. Blocks by subject: 001-099 power bills, demand and reliability; 100-199 emissions, climate damage and insurance; 200-299 federal law (the IRA, the 2025 law, the Clean Air Act, permitting); 300-399 carbon pricing at home and abroad; 400-499 grid, permitting, public power and clean industry; 500-599 workers and places in transition; 600-649 adaptation and insurance programs; 700-799 legacy figures restated (grade D).
- Sources: **Source IDs numbered 4400 to 4799 are reserved for the clean power dossier** (this README, November 13, 2026; `library/reserved-blocks.csv`). Sub-blocks follow the evidence blocks: 4400-4459, 4460-4519, 4520-4579, 4580-4659, 4660-4719, 4720-4769, 4770-4799 (spare).

## Open questions for Espen

None. The re-review's question (`review-m4.md`, R-3), where the transition share's remainder goes after FY2039, is decided: it stays in the general fund (`DEC-2026-11-13-13`, option A). From FY2040 the 20% share, about $33 billion a year, pays the guarantee and the bill credit first, about $11 billion; the rest, about $23 billion, stays in the general fund. That brings clean power's FY2040 cost to about $113 billion.

Next: the booking (tier 3, the lead's), then a short L3 re-check.
