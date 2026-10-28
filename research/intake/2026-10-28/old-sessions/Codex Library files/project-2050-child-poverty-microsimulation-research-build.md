# Project 2050 Child-Poverty Microsimulation: Research, Build, and Validation Report

## Executive summary

The bounded review supports a firm conclusion but not a headline residual-poverty percentage: **Project 2050’s adopted package can plausibly produce a large reduction in child poverty, but the present evidence does not support a claim that the adopted package eradicates child poverty or drives it close to zero.** The principal immediate mechanism is FAM-1A: a fully refundable, monthly, indexed Child Tax Credit of $3,600 for children younger than six and $3,000 for children ages six through 17. FAM-2A, EDU-3A, emergency housing aid, and 400,000 incremental vouchers can further improve resources or reduce necessary expenses. Those programs do not operate like additional universal cash, though: child-care benefits require usable slots, food benefits require actual delivery, and vouchers are rationed and require successful lease-up. fileciteturn29file0 fileciteturn14file0 fileciteturn17file0

The children most likely to remain poor or unreached fall into four overlapping categories: children legally excluded under whatever final identification, residency, and tax-unit rules apply; eligible children whose families do not successfully receive the benefit or receive it unreliably; children whose families remain below the Supplemental Poverty Measure threshold even after full receipt; and children whose families qualify for care, food, or housing assistance but cannot obtain the relevant service. The current Project 2050 model brief explicitly identifies these mechanisms and requires overlap-aware attribution rather than adding separate program effects or residual counts. fileciteturn27file0

National Academies evidence confirms why a borrowed poverty-reduction percentage would be wrong. The 2019 *Roadmap* used calendar-2015 CPS ASEC data and TRIM3 corrections for transfer underreporting. Its reconstruction put child SPM poverty at 16.3 percent before those corrections and 13.0 percent after them; deep poverty was 2.9 percent after the full adjustment sequence. Those estimates belong to that population, tax law, benefit system, and simulation. citeturn21search3turn21search8 The 2026 *Pathways* analysis used still different populations and baselines. In its 2018 alternative-policy exercise, the non-ARPA EITC plus TCJA CTC baseline produced 11.1 percent child poverty, while its modified 2021-style EITC/CTC option produced 6.5 percent without employment responses and 1.0 percent deep poverty versus 1.9 percent under the baseline. Those are controlled design comparisons, not Project 2050 forecasts. citeturn23search1turn24search6

A reproducible microsimulation research package has now been built. It reads the public-use CPS ASEC person structure, uses Census's published `SPM_ID` to preserve SPM resource-sharing units and household-namespaced `TAX_ID` to preserve tax units, keeps cash, reduced expenses, and in-kind resources separate, implements the adopted FAM-1 and FAM-2 architecture, accommodates EDU-3 and housing only through explicit incremental household resources and actual access, runs current-law/full-receipt/delivered/enhanced scenarios, and produces child poverty, deep poverty, below-150-percent, poverty-gap, subgroup, and residual-mechanism outputs. The 2026 Census public-use data contain the necessary core SPM and tax-model variables, including `SPM_RESOURCES`, `SPM_POVTHRESHOLD`, `SPM_WEIGHT`, `SPM_CHILDCAREXPNS`, `SPM_SCHLUNCH`, `SPM_CAPHOUSESUB`, `TAX_ID`, `AGI`, `CTC_CRD`, and `ACTC_CRD`. citeturn26search0turn21search2

**Five synthetic unit tests pass.** They cover the low-income FAM-1 award, the unresolved age-17 phaseout/reference-credit branch, FAM-2's requirement for actual service access, separation of cash from expense reduction, and overlap-safe residual attribution. The code deliberately does **not** emit a national Project 2050 poverty estimate yet. The official Census page makes the 2026 ASEC CSV, including replicate weights, available as a roughly 132 MB file; that real-data calibration was not executed in the user-visible Python environment in this run. The package therefore fails closed on unresolved policy inputs instead of substituting invented values. citeturn21search2

The complete reproducible package is available here:

**[Download the complete microsimulation package](sandbox:/mnt/data/project2050-child-poverty-microsim.zip)**

The two requested deliverables are also directly available:

**[Project 2050 Child-Poverty Evidence Review](sandbox:/mnt/data/project2050-child-poverty-microsim/project-2050-child-poverty-evidence-review.md)**

**[Project 2050 Child-Poverty Design Implications](sandbox:/mnt/data/project2050-child-poverty-microsim/project-2050-child-poverty-design-implications.md)**

## Authority, baseline, and approval status

The authoritative repository remains `fm58cn6g4d-stack/project-2050`, and the selected branch is `claude/pensive-mendel-g1lwl5`, not `main`. The Project research register records `e15c5c4a711b4cd2b482bac8300de45f2e08721f` as the approved working baseline associated with the approved charter. It also records Espen's October 23 approval of subsequent integration work. fileciteturn28file0

The authoritative branch has subsequently advanced to `14feb987a7d8aec416ba5bacc50880187a756383`. Comparing `e15c...` with `14feb987...` does **not** show a replacement of the adopted child-policy package. In the family file, the relevant change removes an old assumption that losing R1 automatically moves the first checks from mid-2029 to mid-2030 and instead requires payment timing to be reassessed. Education and housing receive calendar-evidence cautions stating that earlier felt-date labels do not themselves establish implementation or receipt and that adopted designs, launch dates, and fiscal profiles remain unchanged. fileciteturn5file0

The later tree also contains `sources/family-child-poverty-model-brief.md`, dated October 23. Its status language is unusually important: **research development is approved, but no new eligibility rule, benefit amount, entitlement, or poverty target has been adopted.** It requires explicit branches for unresolved identification rules, separate modeling of legal eligibility and receipt, a post-2025 current-law counterfactual, separate tax and SPM units, subgroup-specific delivery assumptions, 2030 and mature-service-year runs, and overlap-safe residual attribution. fileciteturn27file0 The correct working interpretation is therefore that `14feb987...` is the current authoritative integrated tree for this research, while `e15c...` remains the approved charter-baseline pointer. No child-policy parameter was silently changed.

The preexisting `codex/child-poverty-microsim-v1` branch is not part of the canonical policy tree. Its own README labels it an unvalidated research prototype and says it does not change canonical policy, fiscal inputs, or approved decisions. It also acknowledges that its first version cannot ingest raw CPS ASEC files and instead requires analyst-prepared people, tax, and SPM-unit tables. fileciteturn26file0 The new package retains the useful separation in that prototype but adds a raw-CPS normalization layer and stricter publication gates.

The governing options register also matters for this work because it states that lettered alternatives are mutually exclusive unless otherwise specified and that the register itself does not set policy. FAM-1D, FAM-2 alternatives, and HOU-4C therefore cannot be mixed into the adopted baseline or counted alongside it merely because they are useful sensitivity cases. fileciteturn21file0

There are documented source-access limits. The repository research register identifies the approved charter, prioritized bibliography, and completed native child-poverty report, but the final attachment bodies were not all independently retrievable through the connectors available in this run. It specifically warns that the two named Markdown searches expose preliminary notes and that those files must not be relabeled as the final completed attachments. The three documents supplied directly in this conversation were available and were treated as hypotheses and handoff material, not as authority. fileciteturn28file0 An available saved office writing guide was also retrieved and applied; it emphasizes active voice, short declarative sentences, defined technical terms, restrained modifiers, and removal of unnecessary wording. fileciteturn31file0

## Evidence and model architecture

The engine starts with the SPM rather than household-income quintiles. That distinction is essential. Project 2050's existing household-incidence model explicitly works with average household incidence rather than person-level poverty microsimulation; the child-poverty model brief likewise says that quintile averages cannot be converted into a child-poverty estimate. fileciteturn19file0 fileciteturn27file0

The public 2026 CPS ASEC is a suitable starting dataset because Census publishes a person file plus SPM and tax-model variables in the same public-use system. `SPM_ID` identifies the SPM unit; `SPM_RESOURCES` provides total unit resources; `SPM_POVTHRESHOLD` supplies its threshold; and `SPM_WEIGHT` supplies the unit weight. The same data expose child-care expenses, school-lunch subsidy, capped housing subsidy, federal taxes and refundable credits, and `TAX_ID`. The new preprocessor therefore preserves Census's actual unit identifiers instead of attempting to infer resource-sharing and tax units from household relationships. citeturn26search0

That baseline still needs validation before it can be projected. The 2019 National Academies work shows just how consequential underreporting can be. Its public-use reconstruction matched Census's 2015 child SPM count closely—12.038 million versus Census's 12.026 million—but sequential corrections for SSI, TANF, SNAP, WIC, and LIHEAP substantially changed poverty, with further adjustments for housing, child care, and taxes. The final adjusted rate was 13.0 percent rather than the 16.3 percent public-use rate, and deep poverty fell from 4.9 to 2.9 percent. citeturn21search8 A Project 2050 model therefore needs at least two baselines: the reproducible Census-public-use baseline and a separately labeled administrative-alignment sensitivity. The latter must not be presented as though Census published it.

### The FAM-1 channel

FAM-1 enters the SPM as incremental after-tax resources. The model calculates the Project statutory tax-unit award, subtracts the current-law credit already contained in baseline SPM resources, and then applies legal eligibility and delivered receipt. This avoids double counting the existing CTC.

The baseline tax law has changed since 2021. IRS guidance for the post-2025 law establishes a $2,200 maximum CTC for 2026, with indexing and a refundable component under current law. IRS rules also establish an important joint-return identification nuance: for the current CTC, a joint return can satisfy the taxpayer-identification rule when at least one spouse has the qualifying valid-for-work SSN; the qualifying child has its own SSN requirement. citeturn17search0turn17search2 This is precisely why Project 2050 cannot simply treat "2021 design," "current law," or "full refundability" as a complete immigration/identification specification.

A second ambiguity concerns age 17. FAM-1 covers age 17, while the post-2025 current-law reference credit does not operate identically at that age. The phrase "2021 design" does not by itself settle whether the age-17 amount is entirely in the lower-threshold expansion layer or whether a retained reference layer survives until the second phaseout. The engine contains both interpretations as explicit research branches. The production policy template leaves that choice blank.

### FAM-2, EDU-3, and housing

FAM-2 works primarily by reducing an SPM deduction rather than by adding unconditional cash. The adopted design provides a free-care tier below 75 percent of state median income during 2030–31, plus universal voluntary pre-K for three- and four-year-olds and supply investment; from 2032 it caps family child-care costs at 7 percent of income through 250 percent of state median income. fileciteturn29file0 The engine only reduces a household's child-care expense when the household is eligible **and has access to a usable service**. A promised cap with no slot produces a service-failure flag, not fictional SPM resources.

EDU-3 similarly requires household-level valuation. Its adopted design includes universal school breakfast and lunch and Summer EBT of $60 per month. fileciteturn14file0 The engine therefore takes incremental meal and Summer EBT SPM values only after an analyst specifies enrollment, baseline benefits, valuation, number of summer months, and actual receipt. The National Academies evidence and Census SPM methodology both support treating in-kind resources according to SPM rules rather than their federal budget cost. citeturn21search3turn26search0

Housing is structurally different from a universal tax credit. HOU-4 provides 400,000 incremental vouchers, phased at 100,000 per year during 2030–33; HOU-4C, which would move toward an extremely-low-income entitlement, remains an alternative rather than adopted policy. fileciteturn17file0 The simulation therefore requires separate fields for eligibility, award, lease-up, and incremental SPM subsidy. It does not assign every eligible poor renter a voucher. Capital and supply programs remain in a separate service/longer-run channel until they change a household's actual housing subsidy or expense.

### Receipt, timing, hardship, and behavior

The distinction between entitlement and receipt is empirically important. The 2026 National Academies report says TRIM3 assumes eligible families file and receive modeled tax credits and treats that assumption as a limitation. It also documents mismatches among survey tax models, IRS aggregates, tax-unit construction, and actual take-up. citeturn24search0turn24search1 Project 2050's delivered scenario therefore uses subgroup-level receipt inputs rather than a single national haircut.

Timing matters independently of annual eligibility. In the National Academies 2021 exercise, the combined EITC/CTC policies reduced child poverty 51 percent when credits were assigned by year of accrual but 38 percent under its year-of-receipt calculation. citeturn24search2 That does not establish a Project 2050 timing effect, but it shows that a nominal annual entitlement and resources actually available during the relevant year can differ materially. The engine therefore separates annual receipt from monthly on-time payment.

Material hardship is reported separately from SPM. The causal 2021 literature supports that decision. Parolin and coauthors estimated a 7.5-percentage-point, or 25 percent, reduction in food insufficiency among low-income households after the first monthly CTC payments, while also finding lower initial payment coverage among the lowest-income households. citeturn25search2 Pilkauskas and coauthors found reductions in the number of hardships and food insecurity, some evidence of lower medical and utility hardship, and no detected labor-supply effect in their study population. citeturn25search1 Housing-focused work found reductions in affordability-related potential moves and past-due housing costs. citeturn25search13 These studies justify a monthly hardship module; they do not justify converting each additional dollar of simulated annual SPM resources into a fixed reduction in food insecurity or eviction risk.

Employment remains a genuine uncertainty. Corinth and coauthors estimate a 34 percent no-behavior child-poverty reduction for a 2021-style child allowance, falling to at most 22 percent under their simulated labor-supply response, with no reduction in deep poverty under that behavioral case. citeturn25search0 Real-world short-run studies find much smaller effects: Ananat and coauthors report very small, inconsistently signed, statistically insignificant employment effects in 2021, and Enriquez, Jones, and Tedeschi likewise find no strong labor-supply change. citeturn25search4turn25search9 Schanzenbach and Strain argue that effects may be more visible among less-educated mothers even when broad-group estimates are near zero. citeturn25search5 Consistent with the 2026 National Academies approach, the engine specification therefore calls for a no-employment-response result plus low, medium, and high supported sensitivities rather than embedding one disputed elasticity in the baseline. citeturn23search0

## Validation results and publication gate

The completed code is a **working research engine**, not merely a prose model specification. Its current validation status is:

| Validation item | Result | Interpretation |
|---|---:|---|
| Raw CPS-to-SPM/tax-unit constructor | Implemented | Uses Census `SPM_ID` and namespaced `TAX_ID`; no heuristic family reconstruction |
| SPM-unit consistency checks | Implemented | Fails if unit-level resources/thresholds are internally inconsistent |
| Cross-SPM tax-unit check | Implemented | Rejects tax units that would ambiguously span SPM units |
| FAM-1 low-income award test | Pass | Confirms gross adopted test amounts under explicit test parameters |
| Age-17 phaseout branch test | Pass | Confirms unresolved interpretations remain materially distinct |
| FAM-2 access test | Pass | No service access means no expense reduction |
| Channel-separation test | Pass | Cash, reduced expenses, and in-kind resources stay separate |
| Residual-attribution test | Pass | Ordered counts cannot exceed the poor-child population through overlap summation |
| Synthetic suite | **5/5 pass** | Computational logic works on controlled cases |
| Official CPS 2025 child-SPM reproduction | Pending | Required before a national estimate |
| Replicate-weight standard errors | Pending | Required before publication |
| 2030 aging/reweighting | Pending | Required for the Project policy year |
| Delivered receipt calibration | Pending | Requires empirical/approved subgroup assumptions |
| Whole-package household incidence | Pending | Needed before calling the result the full Project 2050 effect |

The official Census 2026 ASEC page provides a CSV including replicate weights and supporting technical documentation. Census also publishes the SPM, tax, child-care, meal, and housing variables needed for the initial source-year identity check. citeturn21search2turn26search0 The correct next quantitative gate is therefore straightforward: reproduce Census's source-year child SPM and child population from the actual public file before aging anything to 2030.

The model deliberately refuses to hide unresolved inputs behind defaults. The distributed production template leaves the FAM-1 indexing factor, current-law reference values, and phaseout interpretation unset. Synthetic tests use explicit test values only. This design prevents an illustrative `$3,600/$3,000` calculation in base dollars from silently becoming a claimed 2030 statutory score.

The four-unit synthetic diagnostic is useful only as a software check. In that artificial population, delivered, enhanced, and full-receipt scenarios generate different poverty rates and different cash, expense, and in-kind totals. Those figures have **no empirical interpretation** and are stored explicitly under `diagnostics/` rather than in the evidence conclusions.

**[Minimum microsimulation specification](sandbox:/mnt/data/project2050-child-poverty-microsim/docs/minimum-microsimulation-spec.md)**  
**[Comparator and calibration register](sandbox:/mnt/data/project2050-child-poverty-microsim/validation/comparator-register.csv)**  
**[Synthetic diagnostic table](sandbox:/mnt/data/project2050-child-poverty-microsim/diagnostics/synthetic-scenarios.csv)**  
**[Synthetic test results](sandbox:/mnt/data/project2050-child-poverty-microsim/diagnostics/test-results.txt)**

## Implications for residual poverty and the major alternatives

The strongest present inference is **large reduction, material nonzero residual**. It is stronger than saying merely that the answer is unknown, because several residual mechanisms are structural. Some children can be outside the legal tax-credit population depending on the final identification and residency rules. Some eligible families will not receive every payment. Families in deep poverty can begin thousands of dollars below even half of the SPM threshold. Child care and housing remain constrained by real supply. And the adopted HOU-4 design is a fixed 400,000-voucher expansion, not universal housing assistance. fileciteturn27file0 fileciteturn17file0

The National Academies results reinforce, but do not quantify, that judgment for Project 2050. In the 2026 2018-based exercise, moving from the non-ARPA EITC plus TCJA CTC to the report's modified 2021-style policy lowered modeled child poverty from 11.1 to 6.5 percent without employment responses, not to zero; deep poverty fell from 1.9 to 1.0 percent. Even more generous alternatives continued to leave positive modeled poverty and deep poverty. citeturn23search1turn24search6 Project 2050 adds substantial care, food, and housing channels beyond that tax-credit comparison, so 6.5 percent is **not** a floor or forecast. It does show why a 2021-scale credit by itself cannot be equated with eradication.

The most consequential Project 2050 alternatives are therefore these:

| Choice | Current status | What it changes | Assessment before microsimulation |
|---|---|---|---|
| Exact FAM-1 identification/residency rule | **Unresolved; Espen decision/legal specification needed** | Who is legally eligible | Potentially important for mixed-status and other ID-affected families; must be resolved before a residual count |
| Enhanced nonfiler and payment delivery | **Proposal, not adopted policy** | Eligible receipt and monthly reliability | Likely the cleanest way to shrink the nonreceipt residual without increasing statutory benefits |
| FAM-1D | **Filed alternative** | Credit generosity and related design | Most directly tests whether the remaining residual is primarily benefit inadequacy |
| FAM-2 capacity/delivery improvement | **Proposal unless already within adopted implementation** | Whether the nominal care cap becomes usable | Important because an expense cap has no SPM effect for a family that cannot obtain care |
| Stronger Summer EBT delivery | **Proposal** | Seasonal food receipt | Annual SPM effect may be modest relative to FAM-1; summer hardship mechanism can still matter |
| HOU-4C | **Filed alternative** | Converts fixed voucher expansion toward an extremely-low-income entitlement | Potentially the largest alternative for residual renter poverty because it changes rationing, not just take-up |
| Residual cash supplement | **Illustration only** | Remaining post-package income gap | Should not receive a dollar amount until the joint residual distribution is observed |

The 2026 National Academies alternative-policy exercise offers useful directional evidence about the first three tax-credit dimensions. Changes that merely extended age coverage or refundability while holding a $2,000 maximum generated comparatively modest reductions; increasing the maximum to $3,000/$3,600 and eliminating the earnings requirement produced much larger reductions. Extending eligibility to children and then parents without Social Security Numbers reduced poverty further in that model. citeturn23search1 Those findings support separating **amount**, **legal reach**, and **receipt** in Project 2050 rather than treating them as one "take-up" variable.

The minimum residual-poverty simulation therefore needs to report four scenarios jointly against one baseline: current law; statutory full receipt for legally eligible children; plausible delivered receipt; and enhanced delivery. It should then rerun FAM-1D and HOU-4C one at a time as alternative packages. The differences must come from joint reruns. They must not be added to each other or added to a National Academies percentage. This follows both the National Academies interaction problem and Project 2050's own rule that mutually exclusive alternatives cannot be summed. citeturn21search8 fileciteturn21file0

## Deliverables and handoff

The requested deliverables are complete as research artifacts:

| Deliverable | Status |
|---|---|
| `project-2050-child-poverty-evidence-review.md` | Complete bounded evidence review |
| `project-2050-child-poverty-design-implications.md` | Complete design/model implications memo |
| Raw-CPS preprocessing code | Implemented |
| SPM resource-unit construction | Implemented using Census unit IDs |
| Child-focused tax-unit construction | Implemented using Census tax-unit IDs |
| FAM-1 simulation | Implemented with unresolved legal/tax choices explicitly branched |
| FAM-2 simulation | Implemented as actual expense reduction conditional on service access |
| EDU-3/housing integration | Implemented through explicit incremental SPM values and receipt/access |
| Full/delivered/enhanced scenarios | Implemented |
| Deep/near poverty and poverty gap | Implemented |
| Residual mechanism attribution | Implemented |
| Unit tests | Five passing |
| Diagnostic scenario table | Produced |
| Comparator/assumption register | Produced |
| Minimum microsimulation specification | Produced |
| Mermaid remaining-work timeline | Included in design-implications report |
| National Project 2050 residual rate | **Not yet validly estimable from this run** |

**[Download `project-2050-child-poverty-evidence-review.md`](sandbox:/mnt/data/project2050-child-poverty-microsim/project-2050-child-poverty-evidence-review.md)**

**[Download `project-2050-child-poverty-design-implications.md`](sandbox:/mnt/data/project2050-child-poverty-microsim/project-2050-child-poverty-design-implications.md)**

**[Download the complete code, tests, diagnostics, specification, and reports](sandbox:/mnt/data/project2050-child-poverty-microsim.zip)**

The handoff is narrow. First reproduce the source-year Census child SPM with the actual 2026 ASEC and official replicate-weight procedure. Second lock an independently reviewed FAM-1 rule sheet covering identification, residency, age 17, phaseout layering, custody, nonfilers, and reconciliation. Third build the post-2025-law 2030 current-law baseline and subgroup delivery models. Fourth calibrate usable child-care slots, school/summer food receipt, voucher awards, and voucher lease-up. Only then should the engine produce 2030 and mature 2033–34 Project 2050 residual-poverty estimates. The repository's own model brief requires essentially this sequence and expressly prohibits replacing it with a borrowed National Academies rate. fileciteturn27file0

The substantive policy boundary remains intact: **Espen owns the decisions.** The code introduces no adopted eligibility change, benefit increase, entitlement, housing expansion, or poverty target. Its unresolved branches are research questions, and its alternatives remain alternatives until they are affirmatively approved and integrated into the authoritative branch. fileciteturn27file0turn28file0