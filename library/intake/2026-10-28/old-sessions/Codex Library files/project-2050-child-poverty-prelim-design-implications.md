# Project 2050: child-poverty design implications

**Preliminary options note · October 23, 2026.** Companion to the preliminary evidence review. Source baseline: `claude/pensive-mendel-g1lwl5`, `e15c5c4a711b4cd2b482bac8300de45f2e08721f`. These are questions and proposals for further research, not adopted changes or a completed Deep Research assessment.

## Preserve the strongest components

Preserve FAM-1’s full refundability, regular payments and indexing as the starting design. Preserve the standing-authority rule intended to keep payments going through shutdowns. Preserve FAM-2’s attention to supply and its early low-income tier, EDU-3’s universal school-year access and current-rate reimbursement, and housing’s combination of immediate aid, recurring assistance and production. Each addresses a different obstacle; replacing them all with a single poverty statistic would obscure what they accomplish. [P1–P4 in the evidence review]

The central design question is whether their combination provides enough resources and dependable access for the children left behind. A credit can arrive every month and still be insufficient. A family can qualify for free care and have no available provider. An apartment can be financed without its rent being affordable to a family with no earnings.

## Choices most likely to explain the remaining gap

| Priority question | Initial diagnosis | Comparison to commission |
| --- | --- | --- |
| Who is legally covered? | **Missing specification:** “full 2021 design” does not resolve every rule inherited from current law, particularly adult SSNs. | Explicitly retaining current identification restrictions versus restoring 2021 adult eligibility versus broader child/caregiver inclusion. Price each and obtain tax/immigration specialist review. |
| Who receives the full payment on time? | **Missing delivery analysis:** a portal and standing authority do not establish enrollment, updates, successful payment or correction. | Ordinary tax-filing pathway versus proactive enrollment with a non-filer route, offline assistance, birth/custody updates and enforceable correction procedures. Model receipt by subgroup rather than a flat national haircut. |
| Is the credit adequate for children still far below the line? | **Design limitation:** a per-child payment is not a household income guarantee. | Existing FAM-1A versus refundability-only FAM-1C, larger FAM-1D, and a clearly labeled residual-gap supplement. Examine deep-poverty gaps as well as headcounts. Do not add an earnings condition to the baseline. |
| Does rent absorb the gain? | **Design limitation plus missing local analysis:** HOU-4’s 400,000 additional vouchers are rationed; HOU-1 is temporary. | Adopted vouchers and emergency aid versus HOU-4C’s phased extremely-low-income entitlement, with realistic lease-up, landlord participation and recurring subsidy costs. Supply finance remains a complementary channel. |
| Does subsidized care exist where needed? | **Missing implementation specification:** FAM-2’s schedule does not guarantee slots, compatible hours or accessible care. | Adopted phase-in versus faster subsidy expansion paired with demonstrated supply; explicit infant/toddler, disability and nonstandard-hours access; direct local/Tribal routes where legally feasible. FAM-2D is an option, not a baseline assumption. |
| Do food benefits reach children beyond the school day? | **Unresolved coverage:** school-year universality does not establish summer universality. | Clarify Summer EBT eligibility, state participation, direct certification, nonparticipating-school coverage and appeals; compare targeted and universal summer access. |

These alternatives need joint comparison. Do not add their separate poverty effects: the same child can benefit from several programs, and one change can alter another program’s eligibility or measured contribution.

## Correct or qualify weak claims

The education source analysis asserts that meals, Summer EBT and care affordability together remove 1–2 percentage points of child poverty and may add 1–1.5 million workers. Those are session projections, not results from a simulation of the adopted package. Retain them as hypotheses for examination, not public outcome estimates.

The education file’s universal-meals argument includes the claim that universality defeats racialized deservingness politics. Treat that as scenario reasoning, not an empirical guarantee. The useful administrative and access arguments for universality do not depend on that stronger assertion.

The same file describes the chosen reimbursement design as current rates indexed but discusses a cost calculation using Senate-proposal rates. This is a **record/basis question**, not proof the total is wrong: the research handoff should reconcile the rate schedule before using it for costs or service-capacity conclusions. Do not silently repair the ledger.

The FAM-2 file names a canonical working baseline while acknowledging that the author selected its phase-in without a separate Espen decision. Report that provenance. Do not turn an unresolved approval history into a newly adopted policy or switch to the full cap from 2030.

## Minimum specification for a useful microsimulation

Commission a reproducible household analysis, not a redistribution of spending totals across quintiles. Its minimum specification should include:

1. **Population and counterfactual:** a named CPS ASEC/SPM vintage, documented benefit-underreporting adjustments, tax and resource-sharing units, treatment of immigration status and missing identifiers, survey coverage limits, and a separately constructed 2030 current-law baseline. Do not freeze the exceptional 2021 pandemic package into the counterfactual.
2. **Policy rules:** dollar year and indexing, ages, phase-outs and the retained base credit, child/caregiver SSN and residency rules, territories, annual eligibility versus monthly advances, reconciliation and repayment protection. Undefined rules get labeled alternative scenarios.
3. **Program interaction rules:** existing CTC/EITC, SNAP, TANF, SSI, housing and food assistance; income and asset exclusions; taxes and contributions; care and medical expenses. Include relevant adopted household burdens and benefits, including the adult-only climate dividend, without expanding into a general package audit.
4. **Actual receipt and supply:** subgroup-specific enrollment and payment scenarios, interruptions and correction, voucher allocations and lease-up, care slots and hours, school-meal use and summer participation. Give full-coverage statutory effects separately from plausible delivered effects.
5. **Outputs and uncertainty:** 2030 transition and a mature-service year such as 2034, with annual child SPM, deep poverty, poverty-gap dollars and near poverty; subgroup counts and remaining exclusions. Add monthly liquidity/hardship analysis separately. Report no-behavior and supported employment-response cases; avoid treating every care dollar as cash or every reduction in paid work as equivalent welfare loss.

At minimum, disaggregate age, family structure and number of children, earnings/nonemployment, child and caregiver disability, citizenship and mixed-status households, race/ethnicity, geography and housing tenure. Explain unreliable small cells and children poorly represented in household surveys. The model cannot substitute for legal review or evidence on provider capacity.

## Decisions and handoff

No policy change is recommended for immediate adoption. First, resolve the eligibility and payment-rule ambiguities and complete the focused evidence review. Then ask Espen to choose which alternatives deserve costing and simulation, with implications for D3’s household-net principle, D4’s funding-at-maturity rule and D5’s implementation timing. Any new permanent benefit or broader entitlement needs financing and an operational account; a promising result does not authorize a model-input change.

**Immediate next action:** port `project-2050-child-poverty-deep-research-handoff.md` to a Deep Research chat. Complete the two substantive reviews there, retaining these filenames and replacing their preliminary status only when the remaining work is done. Sources and access limits are recorded in the companion evidence review; no repository files were changed and no PR was opened.
