# Project 2050: a calendar model for uncertainty and strategy

October 23, 2026 · Research prototype and recommendations for Espen

The agenda should be assessed against a range of legislative demand and available capacity. Its strategy should protect consequential commitments and improve the chance of delivering their purposes across different conditions. A single overflow total cannot do that work. This package replaces that analytical framing with an executable, bicameral scenario model and an explorer for comparing its results.

The prototype is operational. Its numerical assumptions are **illustrative and uncalibrated**, so its results are conditional experiments, not forecasts or probability intervals. That qualification applies to every date and range below. A runnable model establishes what follows from its assumptions; it does not establish that those assumptions are right.

The authoritative branch was reverified as `claude/pensive-mendel-g1lwl5`, commit `214a7acc1144d86b547c1bc39d8f99c75533dc32`. No adopted policy, repository input or generated repository file was changed. This is a separate research sandbox. It supersedes the earlier report's recommendation to make closing a precise nine-day gap the organizing analytical task. Its inventory, climate-scope comparison and warnings about unsupported durations remain useful.

## Why reconciliation was charged 17 days

The exact code path is `RECON_DAYS = 15` in `index/tools/ledger-build.py`, plus two budget-resolution days per vehicle in the reconciliation allowance. Its cited source is the sequencing section of `frameworks/radical-means-moderate-ends.md`. That passage claims a reconciliation bill takes the same fifteen floor days whether it carries one provision or forty and that compliant additions are free at the margin. This is an analytical claim in a lower-authority framework, not a statutory rule or an empirical estimate established by the repository. The fixed 17-day allowance inherits it.

The fixed charge confuses several questions. Statutory debate limits constrain parts of a procedure. They do not fix preparation, voting, parliamentary review, coalition negotiation, chamber differences or enrollment. The Budget Act provides up to 50 Senate debate hours for a budget resolution and 20 for reconciliation; that does not mean the first necessarily takes two sitting days or the second fifteen. The replacement models the three vehicles separately. [S1–S3]

| Reconciliation package, including resolution | Favorable Senate hours | Central reference | Difficult |
| --- | ---: | ---: | ---: |
| R1 | 36 | 74 | 130 |
| R2 | 40 | 84 | 150 |
| R3 | 36 | 78 | 140 |

These hours include illustrative debate, voting and Senate return work. They exclude House work, preparation waits and non-agenda business, which have separate records. R2 has the largest illustrative voting/return allowance because its adopted scope spans many delivery and revenue titles. That is a judgment to test, not a finding that it must take longer. The range is not obtained by multiplying fifteen days by arbitrary percentages.

## What the system models

**Hours, sittings and elapsed dates are different resources.** Debate, voting and Senate return work consume active hours. The adopted graduated-cloture route also requires procedural stages across sittings. Preparation and chamber agreement may take elapsed days without consuming the floor continuously. The model keeps those mechanisms separate.

For ordinary contested bills it conservatively rounds the existing approximately 4.5-session-day F span to a minimum of five sittings for the initial Senate stage. The Senate floor slot stays occupied during that span, with unused hours recorded as blocked; the prototype assumes no ability to interleave another contested bill during it. This is a conservative representation for review, not new rules text. Favorable early-cloture agreements could shorten the span, but no supporting votes are assumed. Guaranteed amendments and equal time remain adopted; whether the illustrative debate allowances accommodate them requires procedural review.

Each vehicle has preparation/readiness dates, an initial Senate stage, an initial House stage, a negotiation delay, Senate return work, House concurrence and conditional completion. Budget resolutions gate their reconciliation bills in both chambers. Later resolutions conservatively follow completion of the preceding reconciliation vehicle; that is a management assumption for testing, not a universal legal prohibition on overlapping work. R1 may not complete before the incoming President takes office. Social Security is not put into reconciliation and is released for floor consideration from March 20, 2030 in this prototype, preserving a spring enactment route.

DEM-1 normally waits for R1 completion before its Senate start. If R1 remains unfinished on March 1, the model permits a recovery route and flags that an explicit recovery decision is needed. This is a conditional scenario, not an automatic authority to ignore the approved sequence. DEM's March floor-start and mid-2030 enactment checks are separate. Other priorities can prepare and move early; they are not all gated on R1 or DEM.

House processing can occur concurrently with Senate work. Both chambers have independent capacity accounts. The final concurrence stage assumes an agreement is obtainable after the specified work; it does not simulate every possible exchange of amendments. The model is deliberately conservative about initial Senate slot occupancy, while still optimistic about eventual agreement and successful votes. Both limitations matter.

### Full scope stays visible

There are **24 original package identifiers**: 21 regular-order bills and R1/R2/R3. Rules and three budget resolutions are enabling work. A full climate merger still represents two original package identifiers, CLI-3 and CLI-6, so it receives no artificial reward from counting bill numbers. CLI-4 remains carried by CLI-3; CLI-8 remains carried by CLI-7. All existing riders remain within their canonical packages. MOV-31 is outside this first-Congress inventory; its second-Congress demand remains unknown, not zero.

Coverage is a bookkeeping diagnostic. An immigration package, a rights bill and a reconciliation package are not equal units of public value. The model does not claim that completing 20 packages is always preferable to completing 19, or that all completed packages have equal consequence. No policy is silently dropped when capacity runs out: unfinished scope is listed by identifier.

### Conditions and strategies

Three coherent conditions combine readiness, debate, voting, return work and negotiation delay. The difficult condition also reduces both chambers' net capacity by 20%. A separate shared-disruption experiment delays R1/DEM preparation by 21 calendar days and reduces February–March capacity by a further 30%. These are deliberately correlated stress scenarios. There are no independent random draws, probability weights, percentiles or claims of expected enactments.

The four ordering strategies compare target-date order, earlier capacity/guardrail work, a short-stage-first order and a larger-stage-first order. Every ordering preserves priority for rules, R1, DEM and spring SS. They are feasible-list scheduling heuristics, not a proof of a globally optimal order. An unweighted Pareto screen marks a strategy as dominated only when another uses no more gross hours in either chamber, does no worse on every protected check and every original package's completion date, and improves at least one of those dimensions. It does not compare public-value scores or collapse rights into bill counts. The model also compares separate/full climate bills and a front-loaded January–March sitting-hour option.

The current implementation compares 144 combinations plus two shared-disruption cases. Its editable JSON contains every new numerical input and its status. Python uses only the standard library. An HTML explorer reads the precomputed comparisons without requiring a server or online account.

## Preliminary numerical experiment

The table is a deliberately wide **illustrative planning envelope**, not a projected confidence range. Ordinary bills use explicit standard/heavy/fast profiles; reconciliation uses separate profiles. Legacy day estimates are retained solely for provenance and initial complexity classification, rather than converted into new supposedly validated hours.

| Shared condition | Separate-bill Senate active hours | Eight-hour equivalents | House active hours | Combined-climate change in Senate hours |
| --- | ---: | ---: | ---: | ---: |
| Favorable | 485 | 60.6 | 114 | -4 |
| Central | 958 | 119.8 | 284 | -6 |
| Difficult | 1,830 | 228.8 | 616 | +24 |

Eight-hour equivalents are a normalization for comparing work quantities. They are not a count of actual Senate sitting days. They omit elapsed waits and any floor-slot blockage. The explorer also reports actual simulated agenda sitting dates, which depend on the chosen hours and availability. The figures must not be substituted into the legacy 163-day allowance as if the units matched.

### Capacity has an independent range

| Capacity case | Proposed available weekdays | Gross Senate/House hours per available date | Other-business share | Unallocated reserve |
| --- | --- | --- | ---: | ---: |
| Constrained | Monday–Thursday | 6 / 5 | 45% | 15% |
| Working illustration | Monday–Thursday | 6 / 4 | 35% | 10% |
| Expanded | Monday–Friday | 9 / 7 | 35% | 15% |

All are analyst-selected experiments, not leadership schedules. As a coarse blackout assumption, August and December are unavailable. The horizon is January 3, 2029–December 20, 2030. This can strongly affect late summer bills and should be replaced with weekly proposed schedules before claiming dated feasibility. The front-loaded option adds two gross Senate hours and one House hour to available dates through March 31, 2029; it does not assume extra weekdays. It also provisionally lowers other-business allocation to 15% during the opening. Every hour thus deferred is deducted from later agenda capacity until repaid; this is a change in timing, not free capacity. It assumes that portion of other business can lawfully and practically move, which requires review. Mandatory or urgent business cannot simply be postponed. Shares are subtracted once, rather than treating all routine business as additional bill-specific overhead. Difficult-condition disruption is a further, explicitly separate reduction.

Official 2021/2022 activity reports show about 2,042 Senate hours and 1,330 House hours over the two sessions. The working illustration with early extra hours produces 2,176 gross Senate hours and 1,434 gross House hours: roughly 7% and 8% above that historical pair. That is a plausibility comparison, not calibration or evidence that the same hours would be available in 2029–30. No nomination saving is credited in addition to these gross/net accounts. [S4–S5]

The expanded case is substantially more demanding, with 4,014 gross Senate hours when front-loaded—almost twice that historical pair. It should be understood as a high-effort stress bound, not an effortless remedy. Attendance, committees, scoring, drafting and staff would all have to support it. A bill can still miss its deadline in that case if readiness or chamber agreement is late.

| Condition | Capacity | Net Senate hours | Agenda sitting dates used | Original scope completed* | Missed checks |
| --- | --- | ---: | ---: | ---: | --- |
| Favorable | constrained | 870.4 | 168 | 24/24 | R2_summer |
| Favorable | working | 1,196.8 | 132 | 24/24 | None |
| Favorable | expanded | 2,007.0 | 106 | 24/24 | None |
| Central | constrained | 870.4 | 291 | 21/24 | R2_summer, R3_summer |
| Central | working | 1,196.8 | 258 | 24/24 | R1_preferred, R2_summer |
| Central | expanded | 2,007.0 | 189 | 24/24 | None |
| Difficult | constrained | 696.3 | 289 | 7/24 | rules_first_week, R1_preferred, R1_latest, SS_spring, R2_summer, R3_summer |
| Difficult | working | 957.4 | 314 | 10/24 | rules_first_week, R1_preferred, R1_latest, SS_spring, R2_summer, R3_summer |
| Difficult | expanded | 1,605.6 | 381 | 18/24 | rules_first_week, R1_preferred, R1_latest, SS_spring, R2_summer, R3_summer |

*All rows use target-date ordering, separate climate bills and early extra hours. “Completed” means the modeled procedural work finishes **assuming successful votes, eligibility and agreement**. It does not establish enactment probability, judicial survival, benefit receipt or policy success. First-week rules, February R1 and summer checks remain distinct from end-of-Congress coverage. The short labels match the explorer. March 31 is the R1 outer check; February 16 is the weeks-3–4 preference; June 30 is DEM's enactment outer check; June 20 is an analytical spring-SS check. August 31 operationalizes summer for testing, without adopting an exact month or deadline.

Three insights are worth keeping, while the numerical conclusions await better inputs. First, sufficient aggregate hours do not ensure the opening sequence. Second, additional sitting time does not solve unavailable text, votes or a House–Senate disagreement. Third, a full merger may save a repeated procedure while concentrating amendment and coalition risk. These mechanisms should guide investigation even if every starting number changes.

## Strategy: maximize consequential delivery without concealing tradeoffs

Use a transparent comparison in four stages. First identify whether a route preserves adopted scope, minority guarantees and lawful vehicles. Then examine each protected timing commitment and any required recovery decision. Next compare original policy coverage, unfinished protections and the time left for implementation. Finally assess evidence about substantive benefit, durability, coalition and delivery resources. Keep these judgments separate; do not turn them into a single readiness score.

The code deliberately does not choose public-value weights, award one point per bill as its objective, or decide which rights to sacrifice. Its strategy comparison supports human judgment. A mathematical optimizer over uncalibrated durations and invented benefit weights would produce a more precise answer than the evidence allows. This prototype is sufficient to test mechanisms and identify where an improved estimate could change the choice; richer optimization should follow defined values and stronger inputs.

**My current recommendation is an adaptive, deadline-led portfolio with early preparation across the agenda.** Protect an intensive opening sequence for rules and R1; have DEM text ready independently and a specific March recovery decision if necessary. Move capacity/guardrail and other ready priorities when they can advance without damaging those commitments. Protect spring SS through backward planning of its score and closer decision. Keep the entire remaining first-Congress scope on the board and identify contingencies before congestion arrives. Seek additional capacity where a named weekly bottleneck justifies it, rather than treating every uncertain legacy day as a physical shortage.

Retain output measures beyond legislative passage: statutory authority created, delivery capability funded, protections preserved, time left before relevant implementation deadlines, and who remains outside the service or remedy. The current model reports legislative timing and full-package coverage; those other outcome measures remain qualitative review fields, not quantified simulated benefits. Health plan launch in 2031 and automatic enrollment in 2032 remain adopted dates. No simulated signature accelerates them or establishes a household-receipt date.

### The full climate bill remains a serious candidate

The merger scenario preserves chosen CLI-3A/CLI-4A/CLI-6A: the CES and compliance design; AAJA override, damages cap, CWA and rail fixes; air-law restoration; transfer minimums; state consideration of performance-based ratemaking; utility accountability; RTO governance; large-load protections; and distribution/DER/inverter cyber standards with small-co-op support. It excludes unchosen accelerated standards, clean-load mandates, corridor approvals and new disclosures. It keeps the full CLI-7/8 disaster fallback outside the merger, without assuming earlier passage.

In the demonstrator, the merger changes active Senate demand by −4, −6 and +24 hours across the three conditions. These deliberately modest savings and an adverse case replace the old presumption that one combined bill will consume a chosen six-day allowance. They are stress assumptions, not estimates of this bill. The five-sitting initial-stage floor is preserved; a merger also avoids one such initial span. Negotiation waits and House work can offset the benefit. Opening-quarter readiness is largely independent of a later climate merger.

Develop combined text and the separate comparator in parallel. Decide between them on full-scope preservation, actual title-level support, jurisdiction, amendments, bicameral agreement, administration and durability. A valuable bipartisan grid route is a real consideration; a narrower CLI-6B is a substantive fallback and cannot be treated as equivalent. No vote probability is assigned to either route. The original report's detailed scope and jurisdiction matrix remains the starting packet.

## Evidence register and next work

| Item | What is supported | What remains judgment or unknown | Next check |
| --- | --- | --- | --- |
| Original bill scope and approved clocks | Pinned governing/domain files and adopted directions | Feasibility of each window | Floor manager and bicameral preparation map |
| 15 + 2 legacy allowance | Directly traced to builder and framework | Duration validity; claim that additions are free | Retire fixed charge from new analysis; preserve it only as legacy provenance |
| Debate ceilings | Budget Act text | Vote time, actual debate use, returns and agreements | Extract actual legislative episodes and get procedural review |
| Historical gross hours | Official session resumes | Future schedule, other-business mix and attendance | Weekly gross-to-net ledger, with no automatic 15-day nomination credit |
| New bill-hour ranges | Explicit scenario definitions, auditable code | Empirical calibration; profile classifications | Initial elicitation for D2, R1, DEM, R2 and climate, then other packages |
| Preparation and jurisdiction | Dependencies visible in charter/canonical records | Shared drafting/scoring staff and formal referrals | Named staff/workload constraints and readiness milestones |
| Policy benefits and durability | Charter purpose and domain designs | Comparable marginal outcomes under alternative timing | Use pilot/outcomes work; keep estimates separate from scheduling |

The most valuable next calibration is **the opening sequence**, not all 21 bills at once. Assemble a D2/R1/DEM procedural trace: available FY2029 instructions, common text, score/Byrd review, guaranteed amendment treatment, voting blocks, Senate and House readiness, return votes and enrollment. The framework's assertion of invariant reconciliation cost should not survive as a substitute for that trace. Then calibrate R2 and climate, because their scope and coalition interactions can change the strategy. Do not send external requests or communications without express permission.

For historical calibration, count active floor hours, occupied sittings and elapsed preparation separately in a small matched set of budget resolutions, reconciliation packages and contested omnibus/separate bills. Record scope and procedural differences rather than fit one average. Congress.gov action pages for H.R.1319, H.R.5376 and S.Con.Res.5 were inaccessible in this session; therefore no episode-specific active-hour estimate or fitted probability was produced. Official session totals and statutory texts were accessible. This is a concrete evidence limitation of the numerical prototype.

## Handoff and integration

The package contains `model/inputs.json`, input-builder provenance, `calendar_model.py`, substantive verification checks, 146 generated comparisons, the daily ledger for one reference case, this brief and an HTML explorer. Run `python model/verify.py` and `python model/calendar_model.py` from the unpacked package; regenerate the human-facing report/explorer with `python model/make_deliverables.py`. Rebuilding defaults with `build_inputs.py` reconstructs the original research assumptions; preserve edited inputs separately before doing that. No third-party installation is required.

Verification checks cover the full inventory; identical original scope under merger; retained disaster scope; debate ceilings; per-date resource conservation; procedural-span blockage; D2/SS dependencies; zero-capacity failure; and shared disruption. The 146 scenario runs complete. These tests verify the mechanism, not the assumptions.

The supplied October 21 governing/instructions exports and charter retain older branch/commit context. Current GitHub files at the verified working commit were used where timing differs. The charter's purpose and workflow were retained; its scenes are illustrations. The attached bibliography's JSON was successfully decoded to recover its text; IMP-03 and MOD/FIS methodological entries informed the design, without being treated as evidence of future legislative durations. The current saved writing guide was read.

No live repo changes or PR were made. The next focused integration should add the reviewed research engine under `sources/` and its runner under a research tools path, label the legacy 172/163 display as an assumption-based crosswalk, and leave canonical policy, fiscal and vote inputs unchanged. Replacing the production calendar display should follow an explicit method review and corresponding generator changes, rather than hand-editing generated index files. This authorization to build the research system does not adopt any new timing or scope choice.

### Source references

- **S1 — Legacy provenance:** [ledger-build.py](https://github.com/fm58cn6g4d-stack/project-2050/blob/214a7acc1144d86b547c1bc39d8f99c75533dc32/index/tools/ledger-build.py), RECON_DAYS and reconciliation calculation; [ledger-paths.py](https://github.com/fm58cn6g4d-stack/project-2050/blob/214a7acc1144d86b547c1bc39d8f99c75533dc32/index/tools/ledger-paths.py), F/fast treatment; [framework sequencing section](https://github.com/fm58cn6g4d-stack/project-2050/blob/214a7acc1144d86b547c1bc39d8f99c75533dc32/frameworks/radical-means-moderate-ends.md). A framework's strong assertion is not adopted procedural law.
- **S2 — Budget resolutions:** [2 USC 636](https://uscode.house.gov/us/usc/119-118/t2/s636/).
- **S3 — Reconciliation:** [2 USC 641](https://uscode.house.gov/us/usc/119-118/t2/s641/); see also [631](https://uscode.house.gov/us/usc/119-118/t2/s631/), [632](https://uscode.house.gov/us/usc/119-118/t2/s632/) and [644](https://uscode.house.gov/us/usc/119-118/t2/s644/) for timetable, framework and extraneous matter. FY2030 enactment before October is possible in principle, not clearance of actual instructions or text.
- **S4 — Observed capacity:** [2021 official activity report](https://www.senate.gov/reference/resources/pdf/Resumes/117_1.pdf), first page.
- **S5 — Observed capacity:** [2022 official activity report](https://www.senate.gov/reference/resources/pdf/Resumes/117_2.pdf).
- **S6 — Schedule method:** [GAO-16-89G](https://www.gao.gov/products/gao-16-89g). Its treatment of integrated schedules, dependencies and schedule risk informs the structure; it supplies none of the numerical legislative profiles.
- **S7 — Current authority:** [governing decisions](https://github.com/fm58cn6g4d-stack/project-2050/blob/214a7acc1144d86b547c1bc39d8f99c75533dc32/governing/project-2050-governing-decisions.md), D1/D2/D5/D8 and design rules; [shared instructions](https://github.com/fm58cn6g4d-stack/project-2050/blob/214a7acc1144d86b547c1bc39d8f99c75533dc32/governing/project-instructions.md); [Calendar C development](https://github.com/fm58cn6g4d-stack/project-2050/blob/214a7acc1144d86b547c1bc39d8f99c75533dc32/sources/calendar-c-development.md).
- **S8 — Scope/inventory:** [ledger-bills.csv](https://github.com/fm58cn6g4d-stack/project-2050/blob/214a7acc1144d86b547c1bc39d8f99c75533dc32/index/data/inputs/ledger-bills.csv); [climate domain](https://github.com/fm58cn6g4d-stack/project-2050/blob/214a7acc1144d86b547c1bc39d8f99c75533dc32/domains/domain-climate.md), CLI-3/4/6/7/8; [health](https://github.com/fm58cn6g4d-stack/project-2050/blob/214a7acc1144d86b547c1bc39d8f99c75533dc32/domains/domain-health.md), launch dates; [democracy](https://github.com/fm58cn6g4d-stack/project-2050/blob/214a7acc1144d86b547c1bc39d8f99c75533dc32/domains/domain-democracy.md), DEM-1E/F; [SS](https://github.com/fm58cn6g4d-stack/project-2050/blob/214a7acc1144d86b547c1bc39d8f99c75533dc32/domains/domain-social-security.md), D8 route/closer. Existing index consistency warnings were inspected and do not validate the new assumptions.
- **Saved sources:** approved charter attached to this task (its policy baseline pointer is older); bibliography `libfile_892f76624c088191a5ef802b20f316e7`; prior calendar/merger report `libfile_a0c22cfd6140819192e18b8883985bea`; writing guide `libfile_fe07fa0f02c88191a8e7cd366f20c26b`.

### Appendix: complete demand input crosswalk

Every hour range below has status **illustrative, uncalibrated**. Profile definitions in JSON expose debate/votes/return/House/lag/span components. Dates are existing planning targets operationalized for diagnostics; March 28 for spring SS and August 31 for summer are analytical conventions, not adopted new deadlines. Legacy raw days choose an initial complexity class for ordinary bills and remain a provenance field only. Initial readiness is independently varied. The combined climate profile is an alternative to its two rows, never added on top.

| Vehicle | Profile | Senate hours favorable / central / difficult | Planning target used for diagnostics |
| --- | --- | --- | --- |
| HLT-3 | heavy | 28 / 50 / 92 | 2030-02-28 |
| SS-1 | heavy | 28 / 50 / 92 | 2030-03-28 |
| CLI-3 | standard | 16 / 32 / 64 | 2030-01-28 |
| CLI-6 | standard | 16 / 32 / 64 | 2030-05-28 |
| CLI-7 | standard | 16 / 32 / 64 | 2030-05-28 |
| HOU-7 | standard | 16 / 32 / 64 | 2030-03-28 |
| LAB-1 | heavy | 28 / 50 / 92 | 2030-03-28 |
| LAB-9D | fast | 5 / 12 / 26 | 2029-09-28 |
| COM-1 | standard | 16 / 32 / 64 | 2030-03-28 |
| IMM-1 | heavy | 28 / 50 / 92 | 2029-09-28 |
| AI-1 | standard | 16 / 32 / 64 | 2030-05-28 |
| DEM-1 | heavy | 28 / 50 / 92 | 2029-03-28 |
| DEM-5 | standard | 16 / 32 / 64 | 2029-03-28 |
| DEM-6 | standard | 16 / 32 / 64 | 2029-03-28 |
| INT-1 | fast | 5 / 12 / 26 | 2029-05-28 |
| CRT-P1 | standard | 16 / 32 / 64 | 2029-07-28 |
| EXE-1 | standard | 16 / 32 / 64 | 2029-05-28 |
| CAP-8 | fast | 5 / 12 / 26 | 2029-06-28 |
| RTS-1 | standard | 16 / 32 / 64 | 2029-04-28 |
| RTS-3 | standard | 16 / 32 / 64 | 2029-06-28 |
| SAF-1 | standard | 16 / 32 / 64 | 2029-11-28 |
| D2 | rules | 10 / 20 / 40 | 2029-01-09 |
| R1-BR | resolution | 20 / 42 / 74 | 2029-02-01 |
| R1 | R1 | 16 / 32 / 56 | 2029-02-16 |
| R2-BR | resolution | 20 / 42 / 74 | 2029-06-01 |
| R2 | R2 | 20 / 42 / 76 | 2029-08-31 |
| R3-BR | resolution | 20 / 42 / 74 | 2030-06-01 |
| R3 | R3 | 16 / 36 / 66 | 2030-08-31 |
