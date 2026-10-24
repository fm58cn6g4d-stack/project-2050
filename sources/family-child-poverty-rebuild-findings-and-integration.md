# Child-poverty microsimulation: recovery findings, rebuild and integration plan

October 24, 2026. Research and technical-development record; no policy adoption.

**The surviving records support a substantial rebuild, but not recovery of a complete, calibrated national model.** All four research-report exports have now been read locally. A new research engine, preprocessing constructor, validation suite and supporting files were implemented in the local workspace. The suite passed 60 tests under Python 3.12.14; the validation runner also reproduced the original sibling-attribution defect, exercised the raw-ZIP-to-baseline and policy CLIs, and generated 24 artificial scenario rows. The execution environment disconnected before the tested files could be transferred to GitHub or packaged. This commit preserves the findings and continuation plan; it does not claim the executable rebuild is committed.

## Authority and inspected records

Policy authority remains [claude/pensive-mendel-g1lwl5 at 14feb987a7d8aec416ba5bacc50880187a756383](https://github.com/fm58cn6g4d-stack/project-2050/tree/14feb987a7d8aec416ba5bacc50880187a756383). The governing decisions, design rules, shared instructions, canonical family/education/housing files, options register, consistency report and child-poverty model brief were inspected. Main is still the original import and was not used as current policy. The charter-era e15c5c4 pointer is historical, not a reset instruction.

The three preliminary Markdown notes were read from their saved identities. Espen confirmed that local Child Poverty report 1, 2 and 3 are exports of the corresponding native research reports. The fourth was supplied as Child Poverty Report 4.md and a Word export; the Markdown was read in full and its main weighting, calibration and reconstruction passages were also checked in the Word text. The approved charter and bibliography were retrieved through readable saved copies; the writing guide and relevant policy-memo reference were inspected. Saved-conversation retrieval supplied source excerpts about the model lineage and failed artifact recovery; a complete raw transcript of every research-session tool call was not available.

The native research objects could be listed but their text reads returned no readable content. The local exports resolved the content-access problem. They do not restore the code files linked to an earlier session's temporary /mnt/data/ directory.

## What the GitHub search actually recovered

The audit enumerated all 12 branch heads and inspected nontruncated file trees for all 51 distinct commits reachable from them. Pull-request head/merge references were checked as well. Relevant historical files were identified by path and blob identity, with direct inspection of the surviving engine, README, model brief and research-register passages. No claim is made about inaccessible, unreachable or garbage-collected Git objects.

| Recovered item | Verified identity | What it establishes |
| --- | --- | --- |
| First engine commit | 0d9c0d6aff2546e21135020458c5bce8deeca90b | The original prepared-input research prototype existed |
| Subsequent care/pre-K update | f0253e7df42cc5cbbd6bb72fc4504a4a22936fb3 | The prototype received a later technical change |
| Prototype head / PR 8 | 8a8f4b80681a00faea9119b1abd6b5b9b91b7266 | Only model.py and README.md constitute the committed child-poverty tool |
| Latest engine Git blob | 30372ab061e4570a513c63a7bf5d6ff635b51390 | Exact original bytes recovered locally |
| Original engine SHA-256 | 702c8e45badb933eb59851718a57dfaed7f0164e09a0961c7bdc1b9d88334bb9 | Independently matches the upstream-source hash printed in report 3 |
| Earlier engine blob | 59a5a1a285a666a8c6b04be9b40a5cef9cb6115e | Two distinct historical engine versions were found |
| Canonical minimum-model brief | sources/family-child-poverty-model-brief.md, blob 2479aaddad468e9a48ccfa7466af59c1ae69eb4f | The specification existed on the authoritative branch |

No preprocessing, fixtures, test suite, diagnostics, newer corrected engine or promised ZIP was found in those reachable trees. There were no releases and no PR-triggered workflow runs returned for the three prototype commits. PR 8 had no issue comments. Repository-wide artifact listing was not supported by the available endpoint, so absence of all conceivable CI artifacts is not asserted.

The strongest diagnosis is an **artifact persistence/delivery failure**, not a demonstrated deletion from GitHub. The reports repeatedly link session-local packages that were not committed. Whether each earlier claimed file was successfully created cannot now be independently established. A checksum printed in a report identifies a claimed artifact; it does not recover its bytes.

## Reconcile the four reports

| Record | Claim worth retaining | Qualification |
| --- | --- | --- |
| Preliminary notes and report 1 | Joint SPM model; four residual mechanisms; policy amounts and delivery distinctions | Evidence review/specification, not an executed national model |
| Report 2 | Separate SPM/tax units, source preprocessing, age-17 alternatives, cash/expense/in-kind accounting, five synthetic tests | Its claimed preprocessing/package could not be recovered or independently rerun |
| Report 3 | Exact original source, mixed-ID-sibling attribution bug, seven-test reconstruction | It explicitly says raw-CPS preprocessing is still absent; its corrected-source/ZIP hashes are not independently matched |
| Report 4 | Person weights, pre-K/award/lease-up gates, child-specific exclusions, reconstructed artifacts | Also says preprocessing and empirical calibration were not recovered; its benchmark correction requires correction itself |

Report 4 says that 13.4% was official child poverty rather than child SPM poverty. The [actual Census 2025 report, printed pages 6–7 and Figure 5](https://www2.census.gov/library/publications/2026/demo/p60-290.pdf), reports both child SPM and official+ child poverty at **13.4%**, at the published rounding. Its highlights also report ordinary official child poverty at 13.4%; overall SPM is 13.1%. Thus the number cannot be identified by its value alone. Benchmarks must name measure, universe, year, table and file vintage. The public-use replication target may differ from the internal-file published report; [Census's SPM README](https://www2.census.gov/programs-surveys/supplemental-poverty-measure/datasets/spm/readme.pdf) expressly explains that limitation.

## What was rebuilt locally

The rebuilt tool is a versioned research implementation rather than a byte-identical copy of an inaccessible package. It replaces the old three-CSV policy interface with an explicit schema-version-2 JSON contract; the exact original script remains separately preserved.

| Capability | Local implementation and verification |
| --- | --- |
| Source-year construction | CSV/ZIP reader; explicit field names/scales; string SPM_ID; household-namespaced TAX_ID; repeated-unit consistency checks; missing tax links retained; cross-SPM tax units rejected |
| Survey weighting | Child results use individual person weights; unit weights remain distinct; keyed replicate joins and a 4/R variance routine, including paired policy differences |
| Current-law baseline | Imports Census SPM resources/thresholds without invented taxes, IDs or receipt; a separate baseline-only command |
| Calibration | Predeclared child-SPM benchmark comparison; measure/year/population checks; explicit tolerances and a failure exit status; no forced fit |
| Target-year interface | Complete externally audited replacement/reweighting ledger and population controls required; no invented demographic or inflation path |
| FAM-1 | Adopted age amounts; explicit index/reference/age-17/phaseout branches; joint-return one-SSN nuance; current-law offset; explicit replacement versus increment-only receipt |
| Timing | Twelve monthly receipt fractions, including catch-up, separated from on-time months |
| FAM-2 | Income phase-in and usable-care/pre-K access; one shared paid-care pool; recomputation of the actually capped SPM deduction |
| EDU-3 | Incremental SPM-valued school meals and Summer EBT, net of baseline, with separate delivery gates |
| Housing | Eligibility, award and lease-up separated; cumulative weighted household voucher cap; incremental housing valuation cap; HOU-1 aid expires after 2031 |
| Outputs | 2030/2034 × three ID branches × four receipt scenarios; poverty/deep/near rates and counts; distinct child- and unit-weighted gaps; subgroups; ledgers; payment diagnostics |
| Attribution | Child-specific legal flags; overlapping mechanisms; ordered counts partition delivered-poor children only; coverage gaps among all children kept separate |
| Verification | 60 unit/logic tests passed; original defect reproduced against exact upstream bytes; raw ZIP and model CLI checks passed; 24 artificial diagnostic rows generated |

Two accounting choices are especially consequential. First, v1 silently clipped the proposed CTC increment at zero and applied receipt only to that increment. The rebuild makes that convention explicit and also supports replacement of the actual current-law credit with the received proposed award. Replacement can show losses; increment-only refuses statutory losers. The permanent advance-payment rules remain a legal/design question.

Second, raw child-care expenses are not necessarily the amount deducted in SPM. Census's [2026 variable definitions](https://api.census.gov/data/2026/cps/asec/mar/variables.html) distinguish uncapped SPM_CHILDCAREXPNS and SPM_WKXPNS from combined capped SPM_CAPWKCCXPNS. The rebuild computes private care savings jointly, then the reduction in the capped deduction under a fixed earnings cap/work expense. Pre-K and care cannot both claim the same saved dollar. Employment-response scenarios would require recomputing those inputs.

The synthetic suite does not reproduce the exact old fixture rates or claim to be the seven-test package in reports 3–4. There is no recovered golden fixture against which that equivalence could be demonstrated.

## What remains unimplemented or empirically unvalidated

No real CPS file was supplied or executed. Consequently there is still no nationally calibrated source-year reproduction, target-year current-law population, administrative-alignment baseline, or empirically calibrated receipt/service system. The constructor is tested on artificial raw-format records, not certified against every field/layout in the national file.

FAM-1's two-stage phaseout remains provisional. The tool imports actual current-law CTC; it does not fully calculate post-2025 taxes, ODC interactions, dependent assignments, custody, territories, recapture or safe harbors. SSN/ITIN classes require an audited source/imputation and are never inferred from citizenship. Joint tax/SPM interactions and all other benefits/taxes need review.

The projection adapter is a checked import/reweighting interface, not a cohort demographic model. The SDR code has a hand-calculated synthetic test; an empirical 160-replicate run remains pending. National all-child intervals are implemented; subgroup-specific intervals and unit-level cost uncertainty remain open. Supported employment sensitivities and hardship effects are not estimated. FAM-1D and HOU-4C are not falsely implemented by changing a single amount or removing a budget check.

## Integration plan

| Stage | Concrete work | Exit condition / policy boundary |
| --- | --- | --- |
| 1. Preserve the rebuilt research tool | Reconnect the local workspace; hash and rerun the exact saved files; transfer code, fixtures, tests, schema, provenance and generated diagnostics to a review branch from the then-current approved head | Reproduce the 60-test and CLI results; inspect changed-file list; merge only after review |
| 2. Establish the empirical source-year baseline | Obtain the exact public 2026 ASEC/SPM file/version, scales and 160 replicate weights; run constructor and baseline; compare named child counts/rate with predeclared tolerances | Explain public-use/internal differences; independently audit tax-unit and SPM identities |
| 3. Freeze or branch policy specifications | Legal/tax rule sheet for ID, residency, age 17, indexing, custody, monthly updating and reconciliation; document FAM-2 provenance and EDU-3 valuation/timing | Espen chooses substantive rules or authorizes clearly labeled branches; no silent adoption |
| 4. Prepare 2030 and 2034 baselines/delivery | Reviewed tax/transfer projection, population controls, subgroup receipt, usable care, meals/summer access, voucher selection and lease-up; separate administrative-alignment baseline | Reproducible inputs and independently reviewed delivery/volume constraints |
| 5. Produce focused joint estimates | Run no-response and supported behavioral cases; sampling/parameter sensitivities; matched external comparator; overlapping residuals and gaps | Publish focused child-policy results with uncertainty and exclusions, never borrowed component percentages |
| 6. Connect to the full project | Add other adopted household taxes/transfers, adult-only climate dividend, health/work/care expenses and interactions; reconcile benefit volumes and fiscal timing through existing generators | D3 household incidence and D4 fiscal sustainability remain separate tests; no double counting or automatic replacement of ledger costs |

The immediate PR should add the research tool and documentation without replacing the quintile model or inserting artificial rates into the public dashboard. run-all.sh and all fiscal/benefit inputs remain unchanged. A later PR can run lightweight tests in the common rebuild; national microdata execution should remain an explicit, separately reproducible workflow. If any policy number is changed, update canonical inputs and regenerate through the project scripts.

A focused SPM estimate would still not be the whole Project 2050 effect. SPM resource deltas are neither federal outlays nor social value. Child-weighted gaps repeat family shortfalls; they cannot price a residual supplement. A promising result for larger credits or vouchers does not adopt an alternative or relax D3/D4.

## Decisions and immediate continuation

No new policy approval is needed to finish the technical transfer and source-year calibration. Espen's eventual choices concern legal inclusion and payment protections, unresolved FAM-2 approval history, alternatives worth estimating and any poverty target. Researchers must supply the data, reviewed baseline and delivery evidence rather than ask Espen to invent technical parameters.

The next action is to restore the local execution environment and continue from the saved directory, not rebuild the code again from prose:

`rebuild-work/repository/index/tools/child-poverty/`

Implemented files there: model.py, preprocess.py, calibrate.py, project.py, fixtures.py, test_model.py, run_validation.py, run-validation.sh, README.md, schema.md, templates/, synthetic/, diagnostics/, and recovered/. The local forensic inventory is rebuild-work/history-inventory.json. A base-repository download was 96 of 185 nonarchive files complete when the environment disconnected. That snapshot is incomplete; no full-project rebuild is claimed.

Final verified validation before disconnection: **60 tests passed under Python 3.12.14; legacy regression passed; raw ZIP and policy CLI checks passed; 24 synthetic scenario rows generated.** A later small performance edit replaced repeated pre-K age scans with a precomputed set; that edit and the subsequent documentation additions still need the final rerun before code publication. No executable rebuild commit, complete ZIP or national estimate is represented by this checkpoint.
