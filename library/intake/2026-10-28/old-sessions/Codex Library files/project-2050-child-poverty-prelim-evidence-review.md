# Project 2050: child-poverty evidence review

**Preliminary research note · October 23, 2026.** This is an initial assessment and handoff, following Espen’s revised instruction to reserve the substantive evidence review for a chat with Deep Research. No poverty microsimulation was run, and no adopted policy or model input was changed.

## Initial judgment

FAM-1 has a strong evidentiary foundation for substantially reducing child poverty. Making the credit fully refundable removes the earnings barrier that withholds the full benefit from the poorest eligible families. Monthly payment can also help families meet recurring bills. Neither feature establishes that the adopted package would approach eradication. Its benefit amounts do not guarantee a family income floor, its reach is not yet fully specified, and the complementary housing and care programs have limits that cash cannot itself remove.

The defensible conclusion is therefore directional: a substantial reduction is plausible; a residual poverty rate, a percentage reduction, and the identity and number of remaining poor children require further specification and microsimulation. This is a finding about what the evidence currently supports, not a judgment that the project’s ambition is unattainable.

## Project baseline verified

The approved charter, version 13, identifies **`claude/pensive-mendel-g1lwl5` at `e15c5c4a711b4cd2b482bac8300de45f2e08721f`** as its policy baseline. Live branch lookup confirmed that head. `codex/cms-cost-boundaries` points to the same commit. GitHub comparisons confirmed that `claude/funny-brahmagupta-nd8vhl`, `claude/sharp-curie-2w569d`, and `codex/cms-capacity-and-surge-timing` are behind it. `main` remains the original import; it was not used as the policy baseline. The shared-authority branch was listed but its attempted comparison did not resolve; no evidence from it supersedes the approved charter’s baseline.

Read the governing decisions, including standing rules and instructions; shared project instructions; canonical family, education and housing files; consistency report; relevant options-register and incidence-model passages; and relevant education source-analysis passages. The approved charter and writing guide were read from their known saved identities, with a policy-memo sample consulted for style. Bibliography sections consulted include the architecture, housing entries, implementation entries and MOD-01–09, especially MOD-06 on SPM. This was a targeted review, not an audit of all 81 entries.

| Component | Adopted or canonical working design | Consequential limit |
| --- | --- | --- |
| FAM-1A | $3,600 under age six; $3,000 ages 6–17; fully refundable, monthly and indexed; 2021 increase phase-outs; R1 | Indexing base year, complete eligibility and payment rules are not specified. The file’s “full 2021 design” label coexists with building on post-2025 law. |
| FAM-2A | In 2030–31, voluntary universal pre-K for ages 3–4, free care below 75% of state median income, supply grants and wage parity; from 2032 a 7% cap through 250% of state median income | A subsidy schedule does not establish slots, compatible hours, disability access or participation in every state. The family file explicitly says this phased baseline originated as the author’s working selection rather than a separate Espen decision. |
| EDU-3A | Universal breakfast and lunch for enrolled children; current reimbursement rates indexed; Summer EBT at $60 monthly; school-year 2030–31 target | “Universal” school meals do not resolve summer eligibility, state participation, school participation, absences or children outside covered settings. |
| HOU-1 / HOU-4 | $85B emergency rental/construction aid in 2030–31; 400,000 new vouchers phased at 100,000 annually in 2030–33, targeted to extremely-low-income waiting-list households | Emergency aid ends; vouchers remain rationed and are household awards, not a count of children housed. |
| HOU-2 / HOU-3C / HOU-5 / HOU-8 | Credits, revolving-fund grants and direct loans, repair and a social-housing pilot | Financing and repairs cannot be counted as equivalent cash transfers or immediate reductions in tenants’ rent. |

HOU-4C’s voucher entitlement, HOU-9’s federal builder, FAM-1D’s larger credit and EDU-9B’s dedicated financing remain alternatives. Charter family scenes are illustrations. The quintile incidence model explicitly uses estimated distribution shares rather than household microsimulation; its favorable averages cannot establish a child-poverty result. [P1–P6]

## What the initial source review establishes

| Evidence | Baseline and finding inspected | What transfers to this question |
| --- | --- | --- |
| National Academies, *A Roadmap to Reducing Child Poverty* (2019), chapters 5–6 | TRIM3, 2015 population; separate 2015- and 2018-tax-law simulations. Two multi-program packages approximately halved poverty and deep poverty. The $3,000 child allowance alone came closest to halving poverty and approximately halved deep poverty. | Packages combined materially different instruments, including expanded SNAP or much broader vouchers, EITC/CDCTC changes, and in one package immigrant-eligibility changes. Their percentages do not score Project 2050. The allowance also replaced specified existing tax benefits. [E1] |
| National Academies, *Pathways to Reduce Child Poverty: Impacts of Federal Tax Credits* (2026), summary and chapters 4 and 8 | Examines 2021 credits and alternative designs. Chapter 8 assumes full tax-credit take-up in TRIM3 and explains differences from Census, including correction of other benefit underreporting. | Essential newer evidence. Its combined EITC/CTC comparison against no credits is different from the marginal effect of restoring an expanded CTC. Detailed alternatives and permanent employment assumptions still need review. [E2] |
| Census, *Poverty in the United States: 2025* | Latest annual report located: 2025 child SPM rate 13.4%; overall SPM 13.1%. | An observed starting point, not a projected 2030 current-law baseline. Taxes, transfers, expenses and housing geography matter; official poverty is unsuitable as the sole measure of refundable-credit effects. [E3] |
| Census, 2021 poverty report | Child SPM fell from 9.7% in 2020 to 5.2% in 2021. | A pandemic-era outcome with simultaneous interventions, not the effect of the CTC alone and not a forecast for FAM-1. [E4] |
| Bastian (2024), *National Tax Journal* | Published abstract reports a modeled permanent-2021-credit result: 28% less child poverty and 49% less deep poverty, with 367,000 fewer employed parents. | A sensitivity comparator, not a project estimate. Full methods and simulation baseline remain to be inspected. [E5] |
| Ananat et al. (2022), Corinth et al. (2021), Meyer and Sullivan (2022) | Located empirical short-run employment research and more pessimistic modeling/measurement counterarguments. Several full-text requests were blocked. | Review both causal identification and model assumptions. Neither temporary null employment effects nor an assumed permanent response should settle the question alone. [E6] |

SPM counts annual resources rather than proving that money arrived when a bill was due. A family can cross its annual threshold while experiencing food shortages, arrears or homelessness. Conversely, improved care, housing stability or disability support can be valuable without appearing as an equivalent cash-income gain. Report annual poverty, deep poverty below 50% of threshold, poverty gaps and hardship separately.

## The consequential gaps to investigate

**Eligibility and actual receipt.** Current IRS guidance requires an employment-valid SSN for the child and the claimant—or at least one spouse on a joint return. It does not require both spouses to have SSNs. FAM-1’s full refundability clearly changes the earnings rule; it does not explicitly settle the post-2025 adult SSN rule, child identification requirements, territorial treatment or residency conditions. Treat these as unresolved drafting choices rather than claiming either universal coverage or a decided exclusion. Legal eligibility, application, award and timely receipt need separate denominators. [E7]

**Family structure.** A tax child, tax unit and SPM resource-sharing unit are different objects. Separate custodial and noncustodial claims, kinship and foster care, shared custody, births, separations, homelessness and young people without a stable claimant. One adult with two children receives the same child credit as two adults with those children, but the adults’ resources, care constraints and needs differ. Family structure should be a distributional dimension, not an assumed behavioral remedy.

**Deep poverty and disability.** Full refundability preserves support when earnings are absent, including when care or disability limits work. It still does not assure sufficient total resources. Disability-related expenses and accessible care can remain binding even above SPM poverty. Do not automatically assume the credit reduces SSI or SNAP: federal tax refunds and advances have statutory income and temporary resource exclusions. Verify their application, implementation and treatment after the exclusion expires. [E8]

**Service access and housing.** Count care savings only where families actually obtain care; estimate earnings responses separately. Assess infant/toddler supply, hours and transport, additional disability costs and state resistance. For meals, verify that summer rules do not inherit gaps concealed by universal school-year provision. For housing, distinguish voucher issuance from successful lease-up and durable assistance from the emergency bridge. HUD’s randomized Family Options Study is a strong lead on the value of long-term subsidies for homeless families, but its population is not all poor children. [E9]

## Limits and handoff

Deep Research was unavailable, and Espen redirected the task to preliminary analysis plus a portable research brief. National Academies chapter passages and tables were inspected, not both complete books or their technical appendices. The 2026 alternatives chapter request timed out. NBER full-text requests returned 403, the NCBI mirror presented a browser check, and a newly located Census participation-paper URL returned 404. Do not use its search snippet as a settled participation estimate.

Library search returned no results even after simpler queries. Direct reads recovered the approved charter, writing guide and bibliography (`deep-research-report.md`, whose title matches the selected bibliography); the selected attachment ID itself did not resolve. Other relevant saved reports could not be comprehensively inventoried. These are retrieval limits, not evidence that no further reports exist.

**Next action:** use the companion Deep Research handoff to finish the bounded review. No adoption decision is needed now. Espen’s later decisions concern eligibility, coverage, delivery guarantees, benefit adequacy and the measure and date of any poverty target.

## References

Project links are fixed to the verified commit:

- **P1:** [Governing decisions](https://github.com/fm58cn6g4d-stack/project-2050/blob/e15c5c4a711b4cd2b482bac8300de45f2e08721f/governing/project-2050-governing-decisions.md) and [shared instructions](https://github.com/fm58cn6g4d-stack/project-2050/blob/e15c5c4a711b4cd2b482bac8300de45f2e08721f/governing/project-instructions.md).
- **P2:** [Family](https://github.com/fm58cn6g4d-stack/project-2050/blob/e15c5c4a711b4cd2b482bac8300de45f2e08721f/domains/domain-family.md).
- **P3:** [Education](https://github.com/fm58cn6g4d-stack/project-2050/blob/e15c5c4a711b4cd2b482bac8300de45f2e08721f/domains/domain-education.md).
- **P4:** [Housing](https://github.com/fm58cn6g4d-stack/project-2050/blob/e15c5c4a711b4cd2b482bac8300de45f2e08721f/domains/domain-housing.md).
- **P5:** [Incidence model](https://github.com/fm58cn6g4d-stack/project-2050/blob/e15c5c4a711b4cd2b482bac8300de45f2e08721f/index/revenue-household-incidence-model.md), [options register](https://github.com/fm58cn6g4d-stack/project-2050/blob/e15c5c4a711b4cd2b482bac8300de45f2e08721f/index/options-register.md) and [consistency report](https://github.com/fm58cn6g4d-stack/project-2050/blob/e15c5c4a711b4cd2b482bac8300de45f2e08721f/index/check-report.md).
- **P6:** Saved approved charter, `project-2050-draft-charter-2026-10-22.md`, version 13, approved October 23; bibliography, `deep-research-report.md`; `Espen-Writing-Style-Guide.md`, version 2. These were read, but are not public URLs.
- **E1:** [2019 Roadmap, chapter 5](https://www.nationalacademies.org/read/25246/chapter/7) and [chapter 6, tables 6-2 and 6-3](https://www.nationalacademies.org/read/25246/chapter/8). DOI: 10.17226/25246.
- **E2:** [2026 Pathways, summary](https://www.nationalacademies.org/read/29163/chapter/2), [take-up chapter](https://www.nationalacademies.org/read/29163/chapter/6), [2021 effects chapter](https://www.nationalacademies.org/read/29163/chapter/10); [alternatives chapter—retry](https://www.nationalacademies.org/read/29163/chapter/11). DOI: 10.17226/29163.
- **E3:** [Census 2025 report and tables](https://www.census.gov/library/publications/2026/demo/p60-290.html); [full report](https://www2.census.gov/library/publications/2026/demo/p60-290.pdf), especially printed pages 5–7.
- **E4:** [Census 2021 report](https://www.census.gov/library/publications/2022/demo/p60-277.html).
- **E5:** [Bastian, 2024, published abstract](https://www.journals.uchicago.edu/doi/abs/10.1086/728703).
- **E6:** [Ananat et al., employment](https://www.nber.org/papers/w29823); [Corinth et al., modeled labor responses](https://www.nber.org/papers/w29366); [Meyer and Sullivan, measurement and material wellbeing](https://www.nber.org/papers/w30371). Full-text reading remains outstanding.
- **E7:** [IRS CTC eligibility](https://www.irs.gov/credits-deductions/individuals/child-tax-credit); [2025 Schedule 8812 instructions](https://www.irs.gov/instructions/i1040s8).
- **E8:** [26 USC 6409](https://uscode.house.gov/view.xhtml?req=%28title%3A26+section%3A6409+edition%3Aprelim%29); [SSA resource-exclusion guidance](https://secure.ssa.gov/poms.nSf/lnx/0501130676). Statutory text was located in search; a subsequent full-page fetch failed, so verify before legal reliance.
- **E9:** [HUD Family Options Study, full report](https://www.huduser.gov/portal/sites/default/files/pdf/family-options-study-full-report.pdf), research lead; [HUD’s account of three-year findings](https://archives.hud.gov/news/2016/pr16-160.cfm).
