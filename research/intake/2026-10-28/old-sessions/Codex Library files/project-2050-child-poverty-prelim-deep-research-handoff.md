# Project 2050: portable child-poverty research handoff

**October 23, 2026 · Initial research completed; Deep Research outstanding.** Attach this file to the next chat. The two companion preliminary notes are useful context, but this brief contains the essential scope and sources. If accessible, also attach the approved charter and Espen’s writing guide. Repository links below provide the policy documents without requiring this chat’s tool references.

## Paste this prompt

> Use Deep Research for a bounded assessment of how close Project 2050’s actual adopted package could plausibly come to eradicating child poverty, which children remain poor or unreached, and which design choices explain the gap. Use the attached handoff and preliminary notes as starting points to verify, not conclusions to ratify.
>
> Verify the authoritative branch before beginning. The approved charter’s baseline, confirmed October 23, 2026, is `claude/pensive-mendel-g1lwl5`, commit `e15c5c4a711b4cd2b482bac8300de45f2e08721f`, repository `fm58cn6g4d-stack/project-2050`; do not substitute main. Read the governing decisions, shared instructions and relevant canonical files. If newer work exists, establish its approval status and record any baseline change. Retrieve the current approved charter, relevant bibliography sections and saved reports if accessible; disclose anything unavailable. Espen owns policy decisions. Do not change adopted policies or model inputs.
>
> Focus on FAM-1 and interactions with FAM-2, EDU-3 and housing. Assess benefit adequacy, eligibility exclusions, take-up, reliable monthly payment, deep poverty, material hardship, family structure, disability and immigration rules. Separate cash, reduced expenses, services actually available and longer-run effects. Read substantive National Academies evidence from BOTH the 2019 Roadmap and 2026 Pathways report, including relevant methods and alternative-policy chapters; examine subsequent causal evidence and credible counterarguments. Identify each estimate’s population, tax-law baseline, policy version, participation and employment assumptions. Never transfer another package’s poverty reduction to Project 2050 or sum overlapping effects.
>
> Deliver `project-2050-child-poverty-evidence-review.md` and `project-2050-child-poverty-design-implications.md`, with sources, confidence, limitations and a brief handoff. Distinguish adopted policy, findings, proposals and illustrations; distinguish missing analysis, conflicting records, design weaknesses and specialist questions. Explain what can be concluded now, compare the most consequential alternatives, and specify the minimum microsimulation needed for a residual poverty estimate. Stop when the major exclusions and decisions are clear; do not conduct a general audit or exhaustive literature inventory. Apply Espen’s saved writing guide if available: connected explanatory prose, concrete mechanisms and precisely located uncertainty.

## Essential policy context

| Component | Verified working baseline |
| --- | --- |
| FAM-1A | $3,600 under six; $3,000 ages 6–17; fully refundable; monthly; indexed; 2021 increase phase-outs. Full identification, residency, update and repayment rules remain unclear. |
| FAM-2A | 2030–31 voluntary universal pre-K ages 3–4, free care below 75% state median income, supply grants and wage parity; full 7% cap through 250% state median income from 2032. File acknowledges phase-in was an author-selected baseline. |
| EDU-3A | Universal school breakfast/lunch; current rates indexed; Summer EBT $60 monthly; target school year 2030–31. Summer eligibility and delivery are not fully specified. |
| Housing | HOU-1: $85B temporary aid, 2030–31. HOU-4: 400,000 additional vouchers, 100,000 annually 2030–33. HOU-3C: revolving grants plus direct loans, with an extremely-low-income forgivable share. Credits, repair and pilot supplement these. |
| Alternatives | FAM-1D larger credit; FAM-1C refundability-only; HOU-4C phased voucher entitlement; FAM-2D additional standards. They are not adopted substitutes. HOU-9 federal builder remains an option. |

The approved charter makes approaching eradication a defining ambition, but adopts no new poverty target, instrument or spending through its illustrative family scenes. D3 tests household net effects; D4 requires permanent programs paid for at maturity; D5 establishes legislative sequencing. Existing incidence outputs are quintile averages, expressly not child-level microsimulation.

## First questions to resolve

1. Does “full 2021 design” restore adult eligibility displaced by the 2025 SSN rule? What remains excluded under each plausible interpretation? Current IRS guidance requires the claimant OR at least one joint-filing spouse to have a qualifying SSN, as well as the child; avoid the erroneous “both spouses” claim.
2. How much do actual enrollment, monthly payment failures, custody changes and non-filing reduce reach? Distinguish statutory coverage from full-year awards and on-time receipt.
3. What remains after a successful CTC payment: insufficient income, unsubsidized rent, care shortages, disability-related costs, missing food support or another mechanism? Identify subgroup intersections without double-counting children.
4. How do 2021 Census results, TRIM3-adjusted results and employment-response studies differ? What does the 2026 National Academies report actually assume? Its “current policy” comparison is not automatically post-2025 current law.
5. Which marginal changes matter most: reach and payment repair, a larger child payment, residual income support, broader recurring rent assistance, care access or food coverage? Compare outcome mechanisms, costs and limits before proposing a package.
6. What exact rules and receipt/supply assumptions must Espen choose before commissioning microsimulation? Report a 2030 transition separately from mature delivery; do not invent a residual rate.

## Resource set

**Project documents:** open the [verified source tree](https://github.com/fm58cn6g4d-stack/project-2050/tree/e15c5c4a711b4cd2b482bac8300de45f2e08721f). Read `governing/project-2050-governing-decisions.md`, `governing/project-instructions.md`, `domains/domain-family.md`, `domains/domain-education.md`, `domains/domain-housing.md`, `index/options-register.md`, `index/check-report.md` and the limits in `index/revenue-household-incidence-model.md`. Relevant source analysis: `sources/education-transforming-education-act-analysis-and-trust-fund.md`. Treat its poverty and labor-force projections as unvalidated session estimates.

**Saved project context:** approved charter `project-2050-draft-charter-2026-10-22.md` (version 13 was read); *Project 2050: Prioritized Annotated Bibliography and Research Architecture* (saved as `deep-research-report.md`); `Espen-Writing-Style-Guide.md` (version 2 was read). Relevant bibliography entries include MOD-06 SPM, MOD-09 microsimulation, HOU-01–05 and IMP-01–03. The bibliography is a research map, not an antipoverty effect estimate.

**Priority primary evidence:**

- [National Academies, 2019 Roadmap, substantive instruments chapter](https://www.nationalacademies.org/read/25246/chapter/7) and [packages chapter](https://www.nationalacademies.org/read/25246/chapter/8). Inspect methods and appendices. Baseline: 2015 population, 2015/2018 tax-law alternatives, TRIM3 corrections. The approximately half-poverty results belong to those packages.
- [National Academies, 2026 Pathways, summary](https://www.nationalacademies.org/read/29163/chapter/2), [take-up](https://www.nationalacademies.org/read/29163/chapter/6), [employment](https://www.nationalacademies.org/read/29163/chapter/9), [2021 effects](https://www.nationalacademies.org/read/29163/chapter/10) and [alternatives](https://www.nationalacademies.org/read/29163/chapter/11). The first pass inspected summary and selected take-up/effects passages; employment and alternatives still need substantive review.
- [Census 2025 poverty report and tables](https://www.census.gov/library/publications/2026/demo/p60-290.html), [2021 report](https://www.census.gov/library/publications/2022/demo/p60-277.html), [IRS current CTC eligibility](https://www.irs.gov/credits-deductions/individuals/child-tax-credit) and [Schedule 8812 instructions](https://www.irs.gov/instructions/i1040s8). Verify statutes and the 2030 counterfactual separately.
- [Bastian 2024](https://www.journals.uchicago.edu/doi/abs/10.1086/728703); [Ananat et al., employment](https://www.nber.org/papers/w29823); [Corinth et al., labor-supply modeling](https://www.nber.org/papers/w29366); [Meyer and Sullivan, measurement/counterevidence](https://www.nber.org/papers/w30371). Compare assumptions and identification, not just headline magnitudes.
- [2026 state-credit microsimulation paper, author-hosted PDF](https://wagner.nyu.edu/files/faculty/publications/Unrath-Tollett-Goldin-Homonoff-Lal-and-Michelmore-2026.pdf); [food and housing hardship study](https://www.aeaweb.org/articles?id=10.1257%2Fpandp.20231088); [HUD randomized Family Options Study](https://www.huduser.gov/portal/sites/default/files/pdf/family-options-study-full-report.pdf). These were located; full-text review remains outstanding.
- [SSA treatment of tax refunds and advance credits](https://secure.ssa.gov/poms.nSf/lnx/0501130676); verify 26 USC 6409. Do not presume a dollar-for-dollar SSI/SNAP offset.

## Access limits and stopping point

No Deep Research run occurred. The first pass read verified repository material, saved context and selected primary-source passages; it did not complete the literature synthesis. Several NBER full-text requests were blocked, one Academies chapter timed out, and a Census 2026 participation-paper URL failed. Search snippets are leads, not reviewed full texts. Library search failed, although known-ID reads worked; other saved reports were not comprehensively discoverable.

**Working hypothesis to test:** substantial child-poverty reduction is plausible, but near-eradication is unestablished. Eligibility, actual receipt, residual income adequacy and rent/care access likely explain much of the remaining gap. Do not treat this hypothesis as a modeled outcome or foreclose contrary evidence.
