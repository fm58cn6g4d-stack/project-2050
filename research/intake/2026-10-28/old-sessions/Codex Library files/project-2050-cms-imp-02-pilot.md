# Project 2050: CMS-IMP-02 implementation and resource-planning pilot

October 23, 2026 · Oregon worked example for Espen Swanson

**Status:** Completed bounded research dossier and working prototype. The implementation alternatives, allocation examples, review arrangements and candidate measures below are proposals. This is not an agency-approved implementation plan, official budget score, legal opinion or change to adopted policy. Actual incremental costs and FY2029 cash remain unpriced.

**Policy source:** `fm58cn6g4d-stack/project-2050`, `claude/pensive-mendel-g1lwl5`, commit `e15c5c4a711b4cd2b482bac8300de45f2e08721f`. The approved charter’s Section 6 and Appendix C authorize this pilot. The companion file is `project-2050-cms-imp-02-resource-workbook.xlsx`.

## What the pilot establishes

Oregon provides enough public evidence to reconstruct selected funding presentations, distinguish funding from delivery capability, and test a shared-cost and funding bridge. It does **not** provide enough evidence to set CMS’s allocation, claim that existing staff are available for restoration, or price a new federal-state implementation plan.

Three findings matter for the next estimate. First, most of the apparent increase in Oregon Eligibility Partnership’s 2027–29 request comes from moving SNAP benefit funding into its reporting scope. The state explicitly connects that organizational proposal to H.R. 1. That connection does not make the transferred benefits administrative resources. Second, the state reports substantial existing eligibility work and overtime, while the new work required by restoration is not quantified. A reduction in one current-law activity is not a demonstrated staffing surplus. Third, the shared federal Data Services Hub and related services make CMS-IMP-13 a real dependency of CMS-IMP-02; public IT totals cannot establish the marginal cost or availability of that service. [E02, E05, E06, E08]

The preliminary assessment’s principal CMS findings are supported by the inspected records: HLT administrative overlap is unresolved, the CMS agency allocation is provisional, and FY2029 cash remains unpriced. The pilot adds a reconstructable state baseline and specific evidence gaps. It does not validate the assessment’s unrelated fiscal, legal or calendar findings. [P02–P05; L03, priority 3]

## 1. Authority, versions and scope

GitHub branch heads and comparisons were checked during this assignment. `claude/pensive-mendel-g1lwl5` remains at the assessment’s commit and is 31 commits ahead of `main`, which remains at `9dbfaa0139d6b0981a12dcbc5307481cbaa86c14`. The other Claude branches are ancestors. `codex/cms-cost-boundaries` is identical to the selected head; the surge implementation branch is one commit behind it.

There is a qualification: `codex/shared-project-authority` at `5587b1b75e6b664d687d3e83855bf6f6edbe5f8d` has divergent history. The selected head is three commits ahead and seven behind that branch. Their shared-instructions file is byte-identical; their governing files differ. The approved charter explicitly identifies `e15c5c4` as its policy baseline, and that merged baseline contains the approved surge availability decision and CMS annex. It therefore remains the controlling source **for this pilot**. No unmerged branch was treated as a new policy decision, and no merge was performed. A branch’s name or commit count alone does not establish authority. [P01, Document hierarchy; P06, Where things live]

The supplied `3797741` governing export predates the surge-timing changes and was not substituted for GitHub. The approved charter is the supplied October 23 revision, previously identified as Library version 13. The bibliography was read from the supplied JSON’s complete report text, including all annotations, architecture, reading paths and proposed timetable. Its citations are research leads; publications were independently inspected only to the extent stated in the source register. The writing guide was read in full: Library version 2 retains a Version 1 content header. No claim of a new review of the original writing samples is made. [L01–L04]

The pilot preserves **CMS-IMP-02**, “eligibility/subsidy conversion; caseworker training; state plans and systems,” covering HLT-1 and HLT-4. Its shared dependencies use the existing register IDs. Local task keys T01–T08, observation IDs F01–F35/S01–S50 and cost keys C01–C06 are record keys, not competing policy or work-package IDs. The project register, canonical files, adopted amounts, fiscal inputs and generated outputs were left unchanged. [P03, CMS implementation annex; P04, CMS-IMP-02]

## 2. Why Oregon

Oregon’s public materials describe an integrated platform, ONE, serving medical, food, cash and child-care eligibility; distinguish state organizations and funding sources; publish budget stages and workforce information; and identify actual system changes. That combination is useful for testing the charter’s six linked record families. The state is selected for accessible evidence and analytical usefulness, **not national representativeness**. [E03–E08]

This case tests restoration through an existing integrated eligibility system and a changing state marketplace interface. It cannot establish a delivery route for people in non-expansion states, the behavior of an uncooperative state, or a national staffing ratio. Those are important limitations rather than reasons to discard the case. The recommended next step is a better-priced Oregon chain; a second state should later test a contrasting institutional problem, particularly coverage-gap delivery, rather than merely replicate another state budget table.

### The SNAP shift and the Trump law

The 2027–29 agency request’s Revenue Narrative says that the SNAP program and related budgets would move from Self-Sufficiency Programs to OEP as a result of H.R. 1. OEP already determined eligibility; the proposed change would put the wider SNAP program under the same organization. The request’s $3.382 billion nonlimited federal addition is therefore a scope change, not evidence of new eligibility-system capacity. [E05, PDF pp.112–113, Revenue Narrative printed pp.9–10; BDV104 pp.34–36]

Separately, USDA’s June 2026 proposed implementing rule explains that the law reduces the standard federal share of SNAP administration from 50% to 25% starting in FY2027. These changes can occur together: a reporting unit can become much larger while the state faces greater own-source costs. The proposal’s discussion of statutory authority is what was inspected; this dossier does not certify the status of a final implementing rule. The OEP overview’s reference to a prior 75% standard federal match conflicts with that description and is retained as a source issue, not copied into a funding calculation. [E19, PDF pp.1, 3; E05, PDF p.33]

HLT-1 specifies repeal of H.R. 1’s **health** provisions. It does not authorize this pilot to assume repeal of SNAP provisions. Shared ONE changes must preserve the correct rules for each program. [P02, HLT-1; P07, Title I]

## 3. Findings kept in separate dimensions

| Dimension | Finding and type | Consequence |
| --- | --- | --- |
| Goal alignment | Affordable, continuous coverage supports dependable care and financial security. **Missing outcome analysis:** this pilot does not establish improved care access or household effects. | Measure access and remaining costs alongside enrollment; do not assign a wellbeing effect from administrative spending. |
| Design | Restoration and children’s continuous coverage have canonical homes. **Design weakness / missing specification:** the national coverage-gap promise lacks a sufficiently specified and costed noncooperating-state route in the reviewed health materials. | Oregon cannot resolve that national choice. Preserve the ambition while developing alternatives for review. |
| Evidence | Published funding and workload observations are usable. **Missing analysis:** approved APDs, task assignments, executed contracts and FY2029 resources are not established. | No spare-capacity claim, blanket reuse offset or national extrapolation. |
| Fiscal analysis | Selected budget displays reconcile; actual incremental requirements and HLT overlap do not. **Missing analysis**, with a separate state-chart **conflicting record**. | Do not turn a reproduced budget total into a priced resource request. |
| Legal route | R1 is the adopted target; enhanced systems match is conditional. **Specialist review:** actual text, purpose/time/amount, jurisdiction, data use and grant approvals. | An account name, staffing floor or 90% rate is insufficient authority for a particular obligation. |
| Delivery | ONE, federal verification, training, assistance and correction form a connected chain. **Missing analysis:** release effort, acquisition rights, staffing and critical-path duration. | Compare modification and modular alternatives before procuring; no benefit delay is adopted. |
| Measurement | Oregon discloses unreliable post-migration telephone measures. **Missing baseline**, not proof of poor or good performance. | Repair the series and publish missingness before using it as a current launch/service baseline. |

Sources: [P02–P04; E08–E15]. There is no combined readiness score.

## 4. Programs, organizations and accounts

The workbook’s **Program map** separates program, organization and funding mechanism. Its eight program records connect to observations, resources and work packages through stable keys.

| Work / funding perspective | Proposed responsible organizations | Funding and accounting boundary |
| --- | --- | --- |
| Federal rules, oversight and integration | CMS Medicaid and marketplace teams; retained acquisition, engineering, legal and security owners | CMS Program Management and relevant other funding sources; finite federal residual in CAP-7S, continuing functions in CAP-7 or reconciled HLT administration, once |
| State medical eligibility and conversion | OHA policy/program owners, ODHS OEP delivery and systems, relevant local partners | State expenditures and federal Medicaid contribution shown separately; matching is not federal CMS payroll |
| ONE co-users | OEP, DELC, relevant federal/state program owners | SNAP, TANF and child-care allocation/approval rules remain distinct; no blanket Medicaid match |
| Marketplace/subsidy handoff | OHA marketplace, CMS, Treasury/IRS, issuers | Administrative system costs separated from coverage subsidies; verify the state marketplace topology actually present in 2029 |
| Shared federal services | CMS service and acquisition owners; verification-data partners | CMS-IMP-13 owns common architecture/hosting/support; CMS-IMP-11 owns separately defined assurance; partner-agency costs recorded once |

The inspected state cross-reference is **10000-060-12-00-00000**, agency 10000. Federal account names are identified, but exact Treasury account symbols, availability periods, apportionments, balances and award-to-account links were not reconciled. No official identifier was invented to complete the map. [E01–E05; P03, Cost and funding rules]

## 5. Two baselines and the reconstructed observations

### Financial baseline

The workbook contains **85 numeric observations**, preserving original units, periods, vintages, status, scope, parent/non-add links and source locations. USD equivalents convert units only. The `Baseline` sheet reconstructs selected controls; it intentionally has no government-wide grand total.

| Selected observation / reconstruction | Amount | Status and interpretation |
| --- | ---: | --- |
| CMS FY2026 discretionary funding | $4,124.744 million | Final operating-plan presentation; lump sum plus additional Medicare operations provision |
| CMS FY2026 offsetting collections | $3,251.326 million | Plan includes estimated collections and sequestration conventions |
| CMS FY2026 program level | $7,376.070 million | Sum of the two preceding rows; not observed cash or uncommitted HLT capacity |
| CMS recovery-audit collections | $243.900 million | Explicit non-add; excluded from that sum |
| Federal marketplace eligibility/enrollment, FY2025 | $389.078 million | Actual obligations through September 30, 2025, in the FY2027 CJ; not outlays |
| OEP 2025–27 adopted funding | $975,397,783 | Legislatively adopted budget presentation |
| OEP subsequent adjustments | $88,671,526 | Included in the later approved baseline; not added again |
| OEP 2025–27 approved funding | $1,064,069,309 | Prior approved baseline reported in the 2027–29 request |
| OEP 2027–29 request | $4,708,816,490 | Requested, not enacted; changed reporting scope |
| Identified nonlimited federal SNAP addition | $3,381,868,127 | Benefit-flow scope addition, not eligibility administration |
| Request less that identified addition | $1,326,948,363 | **Derived partial scope bridge**; not a fully comparable administrative baseline |

Sources: [E01; E02, printed p.139; E04, PDF p.117; E05, PDF pp.71–73]. Observation keys F01–F35 and S12–S36 reconstruct these amounts.

The remaining nominal change is **$262,879,054**, derived from $1,326,948,363 less $1,064,069,309. The published position-action, vacancy, phase-in/out, inflation and technical-adjustment rows reconstruct it. Further mapping changes remain, so the difference cannot be described as real administrative growth, a restoration cost, or spare funding. No blanket inflation factor or division of a biennium into equal annual cash was imposed.

Three non-additivity rules are material. Federal contributions embedded in state gross expenditures cannot be added to those expenditures again. The CMS IT portfolio and marketplace activity tables cut across the funding display and cannot simply be added to Program Management. The marketplace call-center row is explicitly non-add within its parent. Actual obligations, estimated collections and appropriations are distinct measures even when expressed in dollars. [E01–E02; E05]

The older March 2025 Governor presentation remains useful for architecture, not as the current adopted control. Its broad ONE category includes CAM and Business Information Systems. Its exact fund-source sum is $198,238,694, while the rounded major-cost chart sums to $198.7 million: a **$461,306 unresolved difference**. The workbook retains both views and flags the difference instead of inventing an offset. The chart’s $20 million “Federal Data Services Hub” label also does not establish an uncommitted federal CMS balance or a project charge. [E03, slides 18–19; Baseline B30–B32]

### Delivery baseline

OEP reports two million tasks processed in 2025 and approximately 20,000 overtime hours a month, costing more than $1 million monthly. It reports 108 central systems positions, 56 training positions and 22 hearings positions in its February 2026 presentation. These measures describe different things and populations; they are not interchangeable FTE or spare hours. The approved 2025–27 budget itself distinguishes 2,969 positions from 2,773.81 FTE. [E06, slides 9, 12, 17; E05, BDV104 p.34]

The state’s work-rule scenario estimates 38,133 annual screening hours and 223,080 verification hours for Medicaid, a derived total of **261,213 hours**. It includes an agency attrition assumption. Repealing that requirement could remove work, but its gross removal does not establish net available staff: restoration may increase enrollment, create conversions and corrections, and change demand for assistance. SNAP work and the existing backlog remain. A funded/filled/vacant occupational inventory, case-specific time study, productive-hour assumptions, attrition and training/backfill plan are still needed. [E06, slide 21]

Oregon’s dashboard states that average wait, answered-call and abandonment data have been unreliable since its August 24, 2026 telephony migration. Historical calls cannot supply a current service baseline without a measurement bridge. No unreliable current value was imported. [E09, ONE Customer Service Center note]

## 6. Required work, alternatives and dependencies

The workbook’s `Work and review` sheet contains T01–T08, three implementation alternatives, twelve review/decision records and eight candidate outcome records. These are proposed operational assignments within the existing annex.

| Existing package | Pilot responsibility and dependency |
| --- | --- |
| **CMS-IMP-02** | Define changed rules and cohorts; prepare state plan/APD work; configure eligibility and subsidy handoffs; train staff; provide notices, assistance, correction and continuing casework |
| **CMS-IMP-01** | Retained delivery/acquisition leadership, requirements and integration ownership; the project needs an accountable government owner of vendor work |
| **CMS-IMP-13** | Confirm shared verification, identity, hosting, support, interface versions and capacity; own common costs once and document benefiting-package allocations |
| **CMS-IMP-11** | Independent integration/security/accessibility and notice testing, with clear boundaries against testing already in 02 and 13 |
| **CMS-IMP-08** | HCBS functional eligibility, service/payment and provider readiness outside 02’s financial-eligibility/interface scope |
| **CMS-IMP-06/07** | Later HLT-3 matching/default and public-plan service interfaces where shared; nationwide auto-enrollment in 2032 is **not** a prerequisite for HLT-1 restoration in 2030 |

CMS describes the Hub as supporting verification for state Medicaid and federal/state exchanges. Oregon’s September release bulletin describes verification changes, SSA-related workflows and handoffs to its planned 2027 marketplace, Explore Health. These are documented functions and plans, not a verified 2029 architecture or permission to use data for every new purpose. Partner agreements, capacity, operational support, retention and access/correction rules require confirmation. [E02, printed pp.113–114; E08]

**Proposed estimating path:** begin with modification of ONE and existing federal interfaces (A1), comparing a separate conversion/service module (A2). A replacement core (A3) remains a comparison alternative if evidence shows the current platform cannot deliver. Replacement would need a credible migration, procurement, approval, parallel-operation and retirement case. None of the alternatives has a supported price or completion date.

Work backward from plan year 2030. Before enactment, prepare specifications, legal questions and architecture alternatives without assuming opposition staff can obligate agency money. After R1 authority and funding, begin FY2029 leadership, state planning, procurement and interface work; test releases and notices before coverage changes. Retain trained staff, support and evaluation after launch. The schedule must validate procurement lead times, onboarding, state approvals and peak-load tests. Readiness reviews should trigger reporting and remediation, not a new executive power to withhold benefits or silently change adopted dates. [P02, Felt dates and Dependencies; P03, annex; E17]

The resources inventory includes procurement notice **S-10000-00017274** for ONE training redesign. The primary notice was inspected, but its attachments and an executed award were not verified. Vendor, award value, term, remaining hours, change rights and FY2029 applicability remain unknown. A notice or contract ceiling is not evidence of spare capacity or an offset. [E18]

## 7. Cost assignment and the funding bridge

Use comparable with- and without-proposal cases. Identify current work, avoided work, new requirements, transition and continuing operation separately. Trace costs directly where possible; use supported causal assignment next; otherwise document a reasonable consistent allocation. This is an adaptation of SFFAS 4’s cost-assignment order, not a claim that cost allocation creates appropriations authority. [E14, summary and paragraph 11]

### Working arithmetic, explicitly illustrative

The workbook contains two **invented USD2029 examples** solely to test the method:

1. A state component has $4 million of without-proposal refresh work. The with-proposal case retains that work and adds $6 million of configuration and $2 million of transition, giving $12 million gross and **$8 million incremental resource cost**. A proposed 600/400 benefiting-work driver attributes 60%, or $4.8 million, to Medicaid. **If** that incremental portion qualifies for 90% development matching, the federal contribution is $4.32 million and the state Medicaid share $0.48 million. The other-program $3.2 million has unresolved financing. Those three amounts reconcile to $8 million; adding $4.32 million to $8 million would count the federal contribution twice.
2. A $3 million shared federal release is owned once by **CMS-IMP-13**. Illustrative 60/40 work units attribute $1.8 million to CMS-IMP-02 and $1.2 million to CMS-IMP-06. These are non-add memorandum shares, not two extra funding lines alongside the $3 million owner.

Neither example prices Oregon, CMS or HLT-1. No illustrative amount is exported to project models. Allocation drivers require justification and review; direct attribution should supersede them where possible.

The real funding bridge is deliberately incomplete. Federal development/operations rates can be 90%/75% when conditions are met; general administration commonly uses the separate 50% rule. A multi-program component must first identify benefiting programs and claimable costs. Medicaid’s rate cannot be applied to all ONE costs, all caseworkers or the future public option. Required APD approval, other program approvals and state funding must be established. USDA receives a separate submission and issues its own response for SNAP. [E10–E13]

For each actual line, the workbook records gross **incremental** federal cost, the amount already included in HLT administration, legally usable existing funding for that same increment, residual funding, candidate home and review question. Unknown inputs leave the result **Unpriced**. Actual state conversion and ongoing-work rows separately calculate federal/state/other-program assignments when supported inputs are supplied; the federal shares feed C04/C05 once. Attributed full cost, incremental resource cost and additional funding are different quantities.

| Cost class | Current finding | Candidate home, subject to review |
| --- | --- | --- |
| Existing spending / resources | Published observations available; actual balances, commitments and FY2029 continuity unknown | Explicit without-proposal baseline; no blanket reuse deduction |
| Finite federal leadership/build/assurance | Work identified; incremental quantity and price unknown | CAP-7S residual after HLT overlap reconciliation; CMS-IMP-01/11/13 boundaries |
| State conversion and transition | Scope and APD evidence incomplete; no priced orders | HLT-1/4 administration and applicable federal matching; state share explicit |
| Continuing federal and state operation | Workload, skills and service levels incomplete | CAP-7 or reconciled HLT allowance for federal operations; applicable state administration financing |
| Avoided current-law work | One state workload forecast identified; no net releasable resource or savings established | Keep as a separate workload change; no budget offset booked |

Current agency funding may already finance part of a required service, but appropriated funds can also be committed, restricted, expiring or needed for existing duties. An analyst cannot convert their full amount into an offset. Similarly, HLT-1’s $2.45 trillion midpoint does not reveal its embedded administration. The register and source score do not provide that decomposition. A new CAP charge must not finance a cost already in an HLT score or a state federal claim. [P02, Chosen design and Dependencies; P03, Cost and funding rules; P04; P07]

## 8. FY2029 cash, staffing and fiscal export

Immediate legal availability of the full CAP-7S surge is adopted. CMS’s **$50 billion lifetime surge share remains provisional**, and it is not an FY2029 outlay forecast. The old implied $90.8 billion combined-window CMS increment must be restated after pre-window cash and overlap are priced. No extra CMS bridge appropriation, larger envelope, staffing floor or available balance is established here. [P01, D9; P03, annex; P05]

The workbook provides separate annual entries for federal obligations, federal cash including state draws, gross state cash, the federal draw subset and state own-source cash for FY2029–39. FY2029 entries are blank and summaries say Unpriced. Timing of approvals, state appropriation, contract orders, invoices, advance/reimbursement draws, training/backfill and post-2039 setup commitments are all unresolved. A state may need temporary cash while waiting for a federal draw even when the ultimate cost share is known; no state cash bridge is assumed funded.

Permanent hiring creates continuing costs beyond recruitment and initial training. Federal and state staffing requirements need occupations, effort, loaded rates, hiring dates and productive time, with contractor work separately specified. Aggregate CMS FTE and Oregon authorized positions cannot answer those questions. Existing staff may need backfill rather than merely reassignment. The 2027–29 state request also crosses only part of federal FY2029, which runs October 1, 2028–September 30, 2029; the July–September 2029 state period requires the next biennium’s authority. [E02, printed p.126; E05–E06]

**Fiscal-input export status: no supported changes.** Before export, require one accounting owner; reviewed gross/net overlap; federal/state and fund-channel treatment; a common price basis; availability, obligation and annual cash profiles including FY2029 and any tail; a continuing-operation profile; and documented review/approval. Then prepare changes to the existing hand-written inputs and regenerate through the project scripts. Moving a fixed lifetime amount into FY2029 requires reducing and restating later cash, not adding FY2029 on top and renormalizing the remainder. Recheck debt, interest, annual envelope, maturity and vehicle treatment. This pilot did not run or alter the aggregate fiscal models. [P05; P06]

D1’s planning case, D2’s rules posture, D3’s distributional test, D4’s fiscal conditions, D5’s vehicles and D6’s health design remain in force. This pilot creates no carbon or Social Security change under D7/D8, no new trust fund, no HI reserve sweep and no speculative productivity or fraud-recovery pay-for. D9’s timing is preserved; its sizing remains provisional.

## 9. HLT-1 explained publicly

HLT-1 is the restoration part of Project 2050’s health plan. It would repeal the Medicaid and marketplace cuts in H.R. 1, make enhanced ACA premium assistance permanent and close the coverage gap. The project targets restoration for the 2030 plan year. These are proposed changes in federal law; they are not benefits currently available through this project. The later public option and automatic enrollment belong to HLT-3, with different dates. [P02, HLT-1 and Felt dates]

For someone applying for coverage, restoration has to become a correct eligibility decision, an understandable notice, an affordable premium where relevant, and confirmation that coverage actually starts. In Oregon, much of that work would use an existing system and existing staff. Rules, data exchanges and training would still need to change, and people whose records do not match would need help from a person. A successful website transaction is not enough if the enrollment fails to reach the insurer or a mistaken denial cannot be corrected.

*Illustration, not a forecast:* a parent receives a confusing notice after a rule changes. They can reach an assisted channel, have the relevant record corrected and obtain a review of a disputed decision. The implementation proposal should explain who must respond and how coverage harm is remedied. It should not assume the parent can resolve the problem online or that every statutory restoration guarantees a nearby clinician. New coverage, financial protection and actual access to care need separate evidence.

## 10. Outcomes, correction and specialist questions

The workbook’s M01–M08 are candidate measures, not adopted targets. They cover continuous coverage; independent accuracy checks of both approvals and denials; median and upper-tail decision/correction time; assisted-service access; financial protection and unmet need; staff sustainability; and meaningful response to beneficiary and staff feedback. Define cohorts and denominators in advance, preserve missing values and disaggregate where statistically and legally appropriate. Include unsuccessful applicants and people who never complete the digital workflow. Dollars spent, people hired and tasks closed are intermediate outputs.

**Proposed correction arrangement:** use independent sampled review and end-to-end tests before releases; publish defects and unresolved risks; maintain accessible human correction and fair hearings; and require a named program owner to publish a response and remedial plan when evidence identifies harm. Track whether affected cases were actually reprocessed and coverage restored. Protect evaluation publication while retaining consequences for concealment, negligent implementation and refusal to correct. The independent evaluator, response deadlines, compensation for participation and any broader coverage-continuity authority require design, funding and legal review. None is adopted here. Existing Medicaid continuation pending hearing has specific notice, timing and other conditions; it is not a universal hold-harmless guarantee. [E15; E20]

| Reviewer role to seek | Questions needing review |
| --- | --- |
| CMS/state program and systems owners | What rules, cohorts, APDs, releases and existing commitments exist? Which interfaces, contracts and staff can lawfully support changed work? What breaks under loss of R1 or delayed state readiness? |
| Medicaid financial/APD specialist and budget scorer | Which expenditure category and allocation driver applies? What is already in HLT-1/4, current grants and state budgets? What federal/state costs and cash are genuinely incremental? |
| Counsel and parliamentary specialists | What requires legislation, rulemaking or state plan/waiver action? Are R1 provisions eligible and within jurisdiction? What data use, notice, appeal, continuity, grant and appropriations authorities apply? |
| Workforce and acquisition leads | What retained-government skills, contract rights, staffing, onboarding and procurement lead times are needed? What must continue after surge funding? |
| Independent evaluator and affected people | Can errors, delays, unmet need and excluded groups be measured credibly? What correction and remedy are meaningful, and what must the public authority do in response? |

No specialist, government program owner or affected-person panel was consulted. These are requests for review, not endorsements or assignments accepted by those organizations.

## 11. Workbook use and validation

The eight sheets have distinct purposes: **Pilot** gives findings and linked outputs; **Baseline** reconstructs source presentations; **Cost bridge** separates illustrative arithmetic, actual unpriced lines and cash; **Work and review** links tasks, alternatives, review and measures; **Resources** records workforce/contracts/systems; **Observations** preserves the 85 imported values and metadata; **Program map** links institutions and accounts; and **Evidence** gives versions, URLs and inspection limits.

Amber cells identify inputs or reviewer responses still needed. Blank actual amounts are unknown. Original observations are separate from interpretation and illustrative assumptions. Keyed lookups preserve observation links under sorting; adding records requires extending table/formula bounds and checking the source scope. Review statuses can be changed with evidence and a decision record; changing a workbook status does not adopt policy.

Validation performed: seven independent budget reconciliation checks; unit-conversion and selected source-table checks; live changes to allocation drivers; blank-versus-zero funding and cash behavior; a partial-cost test that retains an unpriced overall total; linked state-share calculation; formula-error scan; and rendered inspection of all eight sheets. Federal/state contributions, parent/child values, alternative budget stages and cross-cut IT displays are not combined in a false grand total. Native Microsoft Excel execution was not available; recalculation was tested in the workbook authoring engine, with formulas exported to XLSX.

Source/execution limits: the web reader could not ingest the large Oregon budget PDFs; they were downloaded, extracted locally and selected tables visually inspected. The first adopted-budget download was malformed; a successful second copy supplied the cited table. An attempted state technology-plan download returned 503 and its contents are not relied on. Some unrelated direct legal-page lookups failed; only the successfully inspected legal/guidance sources below support this dossier. Full CMS/state execution ledgers, APDs, award documents, current capacity tests and FY2029 staffing/cash were unavailable to this public-evidence pilot. The workspace was not a git checkout; source files were retrieved at the pinned GitHub commit. No repository branch, commit, PR or model-input export was created.

## 12. Short handoff

**Findings:** Oregon can demonstrate the method; its SNAP move is explicitly connected to H.R. 1 but must be removed from an eligibility-capacity comparison. Shared federal systems, state casework, overlap and cash must be analyzed together. No justified CMS allocation change, spare-capacity amount or completed new-funding estimate follows.

**Usable components:** 85 observations, eight program/account records, ten resource records, the reconstructed budget bridge, existing CMS-IMP links, three implementation alternatives, working allocation/funding formulas, FY2029 cash fields, public explanation and outcome/correction record.

**Unresolved:** APD and contract scope, score-embedded administration, actual workforce effort, legal/funding approvals, state cash, permanent operations and the national coverage-gap route. The ONE major-cost chart discrepancy and SNAP narrative share require source reconciliation.

**Decisions for Espen:** whether to develop A1 with A2 as the estimating fallback; which correction/public-response option to develop; and whether the next contrast case should examine non-expansion/noncooperation. No adopted design or spending decision is needed merely to use this pilot as a research tool.

**Source versions:** `claude/pensive-mendel-g1lwl5` at `e15c5c4a711b4cd2b482bac8300de45f2e08721f`; charter v13; bibliography report JSON v1; writing-guide Library v2 with v1 header; dated external sources below. Divergent feature branch and stale `3797741` exports disclosed above.

**Saved filenames:** `project-2050-cms-imp-02-pilot.md`; `project-2050-cms-imp-02-resource-workbook.xlsx`.

**Next action:** obtain or locate the actual Oregon APD/amendment and funded work-order inventory, reconcile HLT-1/4 administration with the federal/state cost owner, and price the earliest FY2029 work and its continuing commitments before any fiscal export.

## Source register and inspection extent

All external sources were retrieved October 23, 2026. Links below identify sources actually inspected, not every publication mentioned by the bibliography. Worksheet observation IDs and source locations allow reconstruction without relying on embedded citations from the bibliography’s earlier search session.

### Repository sources at the policy commit

- **P01.** [governing/project-2050-governing-decisions.md][P01]: D4–D6, D9, standing design rules, hierarchy and project instructions; read in full.
- **P02.** [domains/domain-health.md][P02]: HLT-1/4, chosen design, financing, felt dates and dependencies; read in full.
- **P03.** [domains/domain-capacity.md][P03]: CAP-7/7S, overlap rules, open items and CMS implementation annex; read in full.
- **P04.** [sources/health-cms-implementation-cost-register.csv][P04]: all thirteen rows; CMS-IMP-02 and dependencies retained unchanged.
- **P05.** [index/capacity-funding-model.md][P05]: availability/cash boundary and fiscal limitations; read in full. Also inspected [index/check-report.md][P08], health/capacity sections of [index/options-register.md][P09], and HLT/CAP rows of [index/data/inputs/ledger-bills.csv][P10].
- **P06.** [governing/project-instructions.md][P06] and [AGENTS.md][P11]: read in full; governing hierarchy and no manual generated-output changes followed.
- **P07.** [sources/health-go-big-bill-detail-and-financing.md][P07]: title and provision tables, score/financing limitations; canonical D6 changes control over older source designs.

### External primary sources

- **E01.** [CMS FY2026 Program Management operating plan][E01], one-page table and footnotes; extracted and visually inspected.
- **E02.** [CMS FY2027 Congressional Justification][E02], selected printed pp.5, 103, 112–115, 126 and 139, with comparability and obligation notes. The whole justification was not reviewed as a legal or budget audit.
- **E03.** [OEP March 27, 2025 Ways and Means presentation][E03], slides 8, 12, 18–19; selected funding charts visually checked. Older Governor proposal retained as such.
- **E04.** [ODHS 2025–27 adopted budget][E04], PDF p.117, BDV104 p.60 of 60, OEP total; not every page of the 3,049-page budget read.
- **E05.** [ODHS 2027–29 agency request, section 1][E05], PDF pp.33–34, 71–73 and 112–113; BDV104 pp.34–36 of 39 dated August 24, 2026; selected program/revenue narrative. OEP bridge columns visually verified.
- **E06.** [OEP Overview and Staffing, February 16, 2026][E06], selected slides 9, 11–12, 15, 17 and 21; agency-reported measures/forecasts.
- **E07.** [ODHS 2026 end-of-session report][E07], printed pp.4–5; agency explanation of budget changes, not independent award/execution data.
- **E08.** [ONE September 16, 2026 release bulletin][E08], HR1 rules, marketplace handoffs and verification/interface sections; deployment not independently tested.
- **E09.** [ONE operations dashboard documentation][E09], service-measure definitions and telephone-data reliability notice; embedded dashboard dataset not downloaded.
- **E10.** [Multi-Program APD guidance][E10], submission, allocation and separate SNAP response; linked CAM toolkit and Oregon APDs not substantively reviewed.
- **E11–E13.** [42 CFR 433.112][E11], [433.116][E12] and [433.15][E13], relevant development/operations/administration matching conditions. eCFR pages displayed through October 20–21, 2026; refresh for drafting and 2029 use.
- **E14.** [FASAB SFFAS 4][E14], handbook version 24 (September 2025), summary and paragraph 11 cost-assignment order.
- **E15.** [GAO-26-108017][E15], highlights, methods summary and recommendation status; published August 18, publicly released September 17, 2026. Selected states do not provide an Oregon or national staffing ratio.
- **E16–E17.** [GAO cost guide, GAO-20-195G][E16], and [schedule guide, GAO-16-89G][E17], publication overviews and described methods; no claim to full-guide compliance certification.
- **E18.** [OregonBuys S-10000-00017274][E18], June 2026 training-redesign special-procurement notice, item 1; executed award and attachments not verified.
- **E19.** [USDA administrative cost-sharing proposed rule, 2026-12696][E19], prepublication PDF pp.1 and 3, statutory-authority explanation; implementing proposal distinguished from the statutory change it describes.
- **E20.** [42 CFR 431.230][E20], continuation pending hearing and its conditions; broader remedy proposal not presented as current law.

### Supplied project materials

- **L01:** `project-2050-draft-charter-2026-10-22.md`, approved October 23 revision, Library v13; complete text, particularly Sections 6–7 and Appendix C.
- **L02:** *Project 2050: Prioritized Annotated Bibliography and Research Architecture*, report created October 22, JSON v1; complete report text read from supplied file. Underlying works were not all independently reviewed.
- **L03:** `project-2050-initial-agenda-assessment-2026-10-23.md`; preliminary findings tested within the scope stated above.
- **L04:** `Espen-Writing-Style-Guide.md`, Library v2; core voice and policy-analysis guidance applied; content header discrepancy preserved.

[P01]: https://github.com/fm58cn6g4d-stack/project-2050/blob/e15c5c4a711b4cd2b482bac8300de45f2e08721f/governing/project-2050-governing-decisions.md
[P02]: https://github.com/fm58cn6g4d-stack/project-2050/blob/e15c5c4a711b4cd2b482bac8300de45f2e08721f/domains/domain-health.md
[P03]: https://github.com/fm58cn6g4d-stack/project-2050/blob/e15c5c4a711b4cd2b482bac8300de45f2e08721f/domains/domain-capacity.md
[P04]: https://github.com/fm58cn6g4d-stack/project-2050/blob/e15c5c4a711b4cd2b482bac8300de45f2e08721f/sources/health-cms-implementation-cost-register.csv
[P05]: https://github.com/fm58cn6g4d-stack/project-2050/blob/e15c5c4a711b4cd2b482bac8300de45f2e08721f/index/capacity-funding-model.md
[P06]: https://github.com/fm58cn6g4d-stack/project-2050/blob/e15c5c4a711b4cd2b482bac8300de45f2e08721f/governing/project-instructions.md
[P07]: https://github.com/fm58cn6g4d-stack/project-2050/blob/e15c5c4a711b4cd2b482bac8300de45f2e08721f/sources/health-go-big-bill-detail-and-financing.md
[P08]: https://github.com/fm58cn6g4d-stack/project-2050/blob/e15c5c4a711b4cd2b482bac8300de45f2e08721f/index/check-report.md
[P09]: https://github.com/fm58cn6g4d-stack/project-2050/blob/e15c5c4a711b4cd2b482bac8300de45f2e08721f/index/options-register.md
[P10]: https://github.com/fm58cn6g4d-stack/project-2050/blob/e15c5c4a711b4cd2b482bac8300de45f2e08721f/index/data/inputs/ledger-bills.csv
[P11]: https://github.com/fm58cn6g4d-stack/project-2050/blob/e15c5c4a711b4cd2b482bac8300de45f2e08721f/AGENTS.md
[E01]: https://www.cms.gov/files/document/fy-2026-program-management-operating-plan.pdf
[E02]: https://www.cms.gov/files/document/fy-2027-justification-estimates-appropriations-committees.pdf
[E03]: https://www.oregon.gov/odhs/about/legislativeinformation/2025-wm-oep.pdf
[E04]: https://www.oregon.gov/odhs/about/budget/2025-2027-lab.pdf
[E05]: https://www.oregon.gov/odhs/about/budget/2027-2029-arb-section-1.pdf
[E06]: https://www.oregon.gov/odhs/about/legislativeinformation/2026-odhs-oep-overview-staffing-wm.pdf
[E07]: https://www.oregon.gov/odhs/about/legislativeinformation/2026-end-of-session-report.pdf
[E08]: https://content.govdelivery.com/accounts/ORDHS/bulletins/42b03b8
[E09]: https://www.oregon.gov/odhs/agency/pages/oep-one-dashboards.aspx
[E10]: https://www.medicaid.gov/medicaid/data-systems/multi-program-advance-planning-documents
[E11]: https://www.ecfr.gov/current/title-42/chapter-IV/subchapter-C/part-433/subpart-C/section-433.112
[E12]: https://www.ecfr.gov/current/title-42/chapter-IV/subchapter-C/part-433/subpart-C/section-433.116
[E13]: https://www.ecfr.gov/current/title-42/chapter-IV/subchapter-C/part-433/subpart-A/section-433.15
[E14]: https://files.fasab.gov/pdffiles/handbook_sffas_4.pdf
[E15]: https://www.gao.gov/products/gao-26-108017
[E16]: https://www.gao.gov/products/gao-20-195g
[E17]: https://www.gao.gov/products/gao-16-89g
[E18]: https://oregonbuys.gov/bso/external/bidDetail.sda?docId=S-10000-00017274&external=true&parentUrl=close
[E19]: https://public-inspection.federalregister.gov/2026-12696.pdf
[E20]: https://www.ecfr.gov/current/title-42/chapter-IV/subchapter-C/part-431/subpart-E/section-431.230
