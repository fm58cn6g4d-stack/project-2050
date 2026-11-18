# Fair pay and real power at work: L2/L3 milestone review

Role: the independent milestone review of the work dossier (flagship 5; `charter/PLAN.md` 3.2 and 5, "Review"; `charter/STANDARDS.md`, "Milestone review"), stage F. The reviewer wrote none of the dossier. It tries to break the work on four fronts: weak evidence, missing populations, optimistic assumptions and cheaper alternatives. It also:
- applies the design lens (`DEC-2026-11-09-13`);
- checks the fiscal-rule report against `DEC-2026-11-10-05`;
- checks every decided item against `DEC-2026-11-17-01` to `-36`, `-95` and `-96`;
- checks section 9 against sections 1-8;
- reproduces section 6 from `tools/work_path.py` and section 7 from `tools/floor_household.py` and the budget model.

Status: current, as of main at commit `76cf3c9` (November 18, 2026, after #436). Reviewer: Claude Code, `session_01UQzgBty3TQAyLiZiGGh8Cf`. It changes nothing in the dossier: every fix below is a later step.

Espen's decisions are settled. Where a decided choice has a cost or gap the dossier does not show, this review says so as a question for Espen; it does not argue the choice. Under `DEC-2026-11-10-07`, a clearly bounded uncertainty is not a defect. Open and provisional, and not defects in themselves: memo 10 (LAB-19), points 5 and 11 (LAB-14.01, LAB-17.01), good-cause quits (LAB-18.03), section 5's two new items (LAB-4.10, LAB-18.08) and section 6's credit-size question (LAB-5.01), the decision sheet's W1 to W7. The single adult's 2030-34 result (#433) is routed to the secure floor's owners and stage G; this review checks only that it is carried honestly (it is: part E).

## Verdicts

| Level | What it needs (`charter/PLAN.md` 3.2) | Verdict |
| --- | --- | --- |
| **L2, design** | Key parameters chosen (who, what, how much, who administers), with the main alternatives weighed | **Pass.** Record fixes only (W-6, C-items), none blocking |
| **L3, specified** | Provisions section by section (eligibility, benefit, administration, phase-in, remedies); evidence for each load-bearing claim; a cost range validated by models with stated limits; a delivery plan | **Not yet: close.** Three blockers: O-1 (the unemployment benefit line is not derived from the standard section 4 specifies), M-1 (Puerto Rico's floor is unanalyzed) and C-1 (LAB-4.08 contradicts the decided 14(c) phase-out) |

**Why L2 passes.** Memos 1-10 weigh two to four options at each fork, with outside scores (CBO 2019, 2021, 2023; JCT 2007; OMB FY2017; CBO 2018 and 2020), a bill-by-bill table (`3-design.md:106-118`) and an inherited-assumptions table (`3-design.md:120-144`) that says which assumptions Espen chose. Every fork is decided and recorded (`DEC-2026-11-17-01` to `-36`, `-95`, `-96`); the sweep below found every memo status line citing its DEC id, every decided row in `agenda/agenda.csv` at L2 `decided`, and LAB-14, LAB-17 and LAB-19 at L1 `option`, provisional. One option was misdescribed when it was weighed (W-6, LAB-4B); Espen chose B over it, so that is a record fix, not a reason to reopen.

**Why L3 is not yet.** Most of L3 is in place: 84 provisions with parameters, agency, vehicle and evidence; a delivery plan with a dated timeline, remedies, states' roles and rural channels; a cost path that reproduces exactly from its tool and in the budget model; benchmarks, objections, triggers and hard stops. The blockers:
1. **O-1. The trust funds' benefit line rests on "replacement toward about half", but LAB-11.01 specifies 75% of high-quarter weekly pay up to at least two-thirds of the state's average weekly wage.** On the dossier's own inputs that roughly doubles the decided cost to employers, and moves the general-fund and Social Security offsets that are scaled from it. The L3 test is a cost range validated against the specified design; this line is not.
2. **M-1. The $17 floor applies in Puerto Rico with no analysis of its bite.** Puerto Rico's wages are far below the states' (BLS: a May 2023 nonmetro median of $11.42 an hour), so $17 in 2035 would sit near 100% of the local median, far beyond the range section 2 says the evidence covers. Section 2 found the Puerto Rico studies and did not enter them (`2-what-works.md:336`). American Samoa and the Northern Mariana Islands got a provision (LAB-4.10); Puerto Rico, with about 0.8-0.9 million jobs, did not. That is a decision-changing omission.
3. **C-1. LAB-4.08 bars renewal of existing 14(c) certificates from enactment** (`4-specification.md:62`). Certificates must be renewed, so most would lapse within about two years, not end over five years as `DEC-2026-11-17-03` and memo 2 (`memos/2-subminimums.md:32`: "existing ones end over five years") decided. An inconsistent commitment for 35,534 workers.

**What can reach L3 once those land.** Every provision. The rest are fixes and notes, plus Espen's open items, which are bounded and drafted on their recommendations.

## How this review was done

- Read in full: sections 3-7, the memo index, memos 1, 2, 7, 8 (cost parts), the README and the follow-up note's status; sections 1, 2, 8 and 9 in the parts the findings rest on; the work DEC rows; `legacy/domains/domain-labor.md` (SRC-0025) as evidence; precedent reviews for format (immigration, housing, transportation).
- Subagents ran four mechanical sweeps, read-only, and this reviewer re-checked each finding used here against the files: (1) every DEC row against sections 3-9, `provisions.json`, the agenda rows, the README and memo status lines; (2) every number in section 9 traced to sections 1-8 and the register; (3) reproduction of `work_path.py`, `floor_household.py` and the budget-model booking run in scratch copies; (4) evidence grades, corroboration, the registry checker and the legacy comparison.
- New research (`DEC-2026-11-12-02`, WebSearch): Puerto Rico's OEWS wages (M-1). The repository was searched first (`DEC-2026-11-13-15`). Nothing new was added to the register; M-1's figure is to be catalogued in its fix step.
- Line numbers are at `76cf3c9`.

## Checks run

| Check | Result |
| --- | --- |
| `python3 dossiers/work/tools/work_path.py --parts` | Every row and total in `6-cost.md` parts 1, 2 and 4 is identical to the tool's output. Firm lines 195.1 (96.3 to 349.0) over FY2030-39 and 27.36 (12.9 to 43.9) in FY2040; spending 149.7 / 20.42; revenue 13.4 / 1.44; floor's indirect effect 32.0 / 5.50; booking −54.8 / +6.76; 4.54% of the $602.7 billion gap (4.98% with the tranche); 0.051% of GDP. **Matches** |
| `work_path.py --check` | "OK: 84 provisions, 24 lines, 34 with no line." `provisions.json` holds 84 unique IDs (79 from section 4, 5 from section 5). The check compares ID sets and that each central value sits in its range; it does not test hand-entered figures (part 3's capacity rows, LAB-12.01's Medicaid cost) |
| `floor_household.py` | Every cell of `7-validation.md:39-46` and every prose figure in part 1B match (39% against 59%; $874 premium; 81-98%; 116-132%; 91% to 167% of the guideline). **Matches** |
| Budget model on section 6's booking rows (`--booking-scenario --apply` into a scratch copy, `models/tools/run-all.sh`) | 602.69 to 609.66 in FY2040 and 3,773.41 to 3,719.41 over FY2030-39: **+$6.97 billion and −$54.00 billion**, as section 7 says. The two expected failures (provision specs, health's pinned-gap check) failed as described. The gap from section 6's −$54.8 billion is the ledger's three-decimal rounding (+$0.85 billion), as `7-validation.md:70` explains |
| `python3 models/registry/check.py` | Exit 0; no "figure missing from passage" warning for work. 79 warnings: 1 overdue re-check (EV-WRK-183), 31 analyses without independent corroboration, 47 contested entries (W-items) |
| Counts | 390 unique evidence entries, split by section as `README.md:41` says |

## Findings

IDs: **O** optimistic assumptions; **M** missing populations; **A** cheaper alternatives; **W** weak evidence; **L** design lens; **F** fiscal-rule report and the money; **E** section 9 against sections 1-8; **C** consistency and record. Severity: **blocker** (blocks L3), **fix** (a later step should change it), **note** (worth knowing; no change required). "Changes" names the decision or figure a different answer would change.

### O. Optimistic assumptions

**O-1. The UI benefit line is not derived from LAB-11.01's standard. Blocker.**
- *Where:* `3-design.md:100` and `memos/7-unemployment-insurance.md:35` set the basis: "recipiency toward 40% and replacement toward about half" lifts regular benefits 40-60%, $15-25 billion at FY2025 levels. `6-cost.md:107` and `:309` carry it unchanged into $259 billion over FY2031-39 and $35.7 billion in FY2040; `7-validation.md:94` says it is memo 7's judgment, not a model.
- *The scenario:* LAB-11.01 (`4-specification.md:162`; the 2025 bill's sec. 202-203, `library/text/wrk-3-ui-modernization-act-2025-sxs.txt:90-94`, with no phase-in) pays 75% of high-quarter weekly earnings, capped at a state maximum of at least two-thirds of the state average weekly wage (SAWW). Recipients today replace 43% of their wages [EV-WRK-302], which puts their average weekly wage near three-quarters of SAWW. At that wage the 75% rate is below the cap, so the typical recipient's replacement rises to 75%; only those above about 0.89 SAWW are capped. A rough average under the standard is 60-70%, about 1.4-1.6 times today's. With the dossier's own 40% more recipients (`6-cost.md:60`), benefits rise about 2.0-2.2 times: **+$40-50 billion a year at FY2025 levels, not $15-25 billion** (reviewer's arithmetic, labeled judgment; the 26-week floor and claim-length response [EV-WRK-368] push it higher). "Replacement toward about half" is below today's 43%-of-wages figure plus the standard's floor of 75%; it is not a reading of the specified design.
- *What follows:* the trust funds' lines roughly double (about $450-550 billion over FY2031-39, $65-80 billion in FY2040, matched by employers' state taxes); the general-fund tax offset (5%, `6-cost.md:93`) rises from $13 billion to roughly $25-30 billion over the decade; Social Security's loss from about $21 billion to roughly $40 billion; the workload line and Extended Benefits' ordinary-year line rise with benefit levels. The general-fund change is a few billion a year, small against the gap; the employers' cost and the states' solvency path change a lot.
- *Changes:* memo 7's stated cost (Espen decided B seeing $15-25 billion a year); the solvency review trigger (`7-validation.md:227`); whether the $25,000 wage base (LAB-11.05) finances the standard. Question 1 for Espen.

**O-2. Wage insurance: the tool's figure is about 40% above its own derivation, and the basis leaves out eligible discharges. Fix.**
- `6-cost.md:62-69` and `tools/work_path.py:173-180`: 1.1 million × 0.88 × 0.6 × 0.5 × 0.6 is about 0.17 million new recipients a year, about 0.27 million on the rolls at $6,000-6,500, **about $1.7 billion a year**; the tool hard-codes $2.4 billion for FY2033 (line 180) with no step between.
- The basis counts the displaced-worker survey's layoffs only [EV-WRK-315] (plant closings, slack work, abolished positions). `DEC-2026-11-17-95` and LAB-18.03 also make eligible a long-tenured worker discharged not for misconduct, "so a worker fired for poor performance qualifies". Those are not in the survey and not priced; section 4 prices quits (`4-specification.md:201`) but not these.
- `work_path.py:180` grows the line 3% a year after 2035, when the cap's freeze ends; `WAGE_G` (line 35) is defined and unused.
- *Changes:* LAB-18's line and booking row (`6-cost.md:284`). The two errors run in opposite directions; the fix states the chain and the discharge share explicitly (judgment with a range).

**O-3. The state UI agencies' 2031 date rests on a $20-40 million-a-state systems grant. Note.** `5-delivery.md:66` sizes LAB-11.09 at $1-2 billion with no evidence on what a state UI system modernization costs; the dossier itself names the state agencies the largest delivery risk and cites the pandemic record [EV-DEM-295]. A fix step should add one or two state modernization costs to the register and either confirm the grant or offer the phased alternative (the benefit standards in 2031, wage insurance and the new fields later) in section 5. Changes: LAB-11.09's size and the one-date simplification (`5-delivery.md:39`).

**O-4. Wage insurance's 60% take-up is benchmarked against a figure that is not a take-up rate. Fix.** EV-WRK-332's 11% is the share of *all* TAA participants who collected wage insurance, not of those eligible (aged 50 and over, reemployed at lower pay). It is used as a take-up benchmark at `6-cost.md:67`, `7-validation.md:97` and `:205` ("at TAA's 11% the line would cost about a fifth as much"), `4-specification.md:184-185` and memo 8. The 60% may still be reasonable with the automatic offer, but the comparison overstates how far it departs from experience. Changes: the take-up range and the review trigger at `7-validation.md:229`.

**O-5. National service's cost omits the grantees' match. Fix.** EV-WRK-398's $25,200 is the *maximum federal* request per member service year, and the same entry says first-time grantees match 24% of costs (the share rises for continuing grantees). `6-cost.md:79` prices 150,000 positions at that federal cap; `5-delivery.md:154` says "No provision adds a state matching cost". At 150,000 positions the match is on the order of $1-2 billion a year that host organizations and states must raise, or the federal share rises. `5-delivery.md:74` names host sites as the binding constraint; the match is part of it. Changes: LAB-9's line or the delivery risk; a working assumption (keep the match, waive it for the new positions, or federalize part of it) should be written into LAB-9.01.

**O-6. The credit's size rests on unsourced wage-cost inputs. Note.** `work_path.py:91` uses added wage costs of $1.0, $3.5 and $6.0 billion by step with no evidence ID; `7-validation.md:258` lists the missing share of minimum-wage workers at firms under 50. Bounded and labeled; JCT scores it (point 15). It is already with Espen (W7).

### M. Missing populations

**M-1. Puerto Rico (and the other territories under the full floor) get the national schedule with no analysis. Blocker.**
- *Where:* `4-specification.md:277` and `5-delivery.md:155` ("The floor and wage law apply in Puerto Rico, Guam and the U.S. Virgin Islands as federal wage law does today"). No bite figure for any territory; the national-median bite (about half in 2035) is the only one used.
- *The scenario:* BLS's OEWS put Puerto Rico's nonmetropolitan median at $11.42 an hour in May 2023 and the San Juan metro area's mean at $17.98 in May 2024 (against $32.66 nationally) (BLS, OEWS area tables; reviewer's search, not yet in the register). At the dossier's 3.5% a year, $17 in 2035 is close to 100% of the local median outside San Juan, far above the 60% (state studies) and 81-82% (one county study) the dossier treats as the evidence's reach (`2-what-works.md:71`). The classic evidence on the federal floor's extension to Puerto Rico (Castillo-Freeman and Freeman) found real job losses; section 2 found those studies and did not enter them for lack of source IDs (`2-what-works.md:336`).
- *Changes:* whether Puerto Rico follows LAB-4.01, gets its own path on LAB-4.10's model, or the commission's report drives it. Section 5 recommended a separate path for American Samoa on exactly this reasoning (`5-delivery.md:161`). Guam's and the Virgin Islands' medians should be checked in the same step. Question 2 for Espen, after the fix step drafts options.

**M-2. Wage insurance's 12-quarter tenure test drops workers with one empty quarter. Fix.** LAB-18.01 (`4-specification.md:180`) reads three years' tenure as "earnings with that employer in each of the 12 quarters". A worker on unpaid family or medical leave, a long strike, a disability spell, or a seasonal layoff with recall has a zero quarter and fails, though they held the job for three years; so does a worker whose employer was acquired and reports under a new account. These are not rare among long-tenured workers. A working choice that counts protected-leave quarters and successor employers (records states already hold for experience-rating transfers) closes it at little burden. Changes: LAB-18.01's eligibility.

**M-3. Farmworkers and domestic workers stay outside the labor act, and the farm overtime exemptions stay. Note, sent as a question.** The dossier records this honestly as "a gap for later work, not a decision" (`4-specification.md:270-271`; `7-validation.md:134`). Leaving a large, low-paid group outside card check, penalties and first contracts is a commitment choice, not only a research gap. Question 3 for Espen.

**M-4. Young entrants and short-tenure workers miss wage insurance. Note.** Stated plainly (`4-specification.md:274`), and memo 10 (provisional) addresses it in a displacement period. Bounded.

**M-5. Workers in states that do not conform by 2031. Note.** Covered by LAB-11.10's provisional fix (`6-cost.md:113-121`), which this review finds sound in design: a separate conformity reduction into a federal account, and authority for Labor to pay the difference through the state agency. It needs its authorities written into `provisions.json` text as statute language at the next touch, and a register entry for the agent-state authority (`6-cost.md:337`).

### A. Cheaper alternatives

**A-1. Apprenticeship grants pay for the 55% of starts that would happen anyway. Note.** `6-cost.md:73`: grants go to "apprentices who would have started anyway, about 55% of today's starts", about $1.5 billion a year of the line at full scale. Paying only for starts above each sponsor's recent baseline would cut that, at the cost of a baseline test the design lens warns against. The dossier should state the trade-off in one line; the decided design (memo 8 C, per apprentice) stands.

**A-2. Wage insurance's $10,000 cap and the trust funds. Note.** No cheaper design reaches the same people; OMB's FY2017 design at a $10,000 two-year cap is half LAB-18's (`6-cost.md:217`). Decided; no change.

**A-3. The UI standard's cost (O-1) has a cheaper route Espen may want shown:** phase the 75% replacement in (for example 50% rising to 75% over the decade), or hold the maximum at two-thirds of SAWW with a lower replacement rate. Memo 7's own "What would change this" names narrowing replacement first (`memos/7-unemployment-insurance.md:73`). For Espen with question 1, not argued here.

### W. Weak evidence

**W-1. Circular corroboration on the floor's central evidence. Fix.** EV-WRK-051 (Dube's review, grade C) says its 81% county figure *is* Godøy and Reich, which is EV-WRK-063; 063 is recorded as corroborating 051. `7-validation.md:163` cites the 81% and `:171` the 0.82 as two pieces of evidence. The register should record them as one finding, and the prose ("Moderate to strong", `memos/1-wage-floor.md:21`) should match a review contested by EV-WRK-034, 060 and 064. Changes: how strongly section 7 answers "a $17 floor will cost jobs"; not the decision.

**W-2. County bite claims carry no evidence and contradict each other. Fix.** `memos/1-wage-floor.md:32` says half the national median "sits nearer 60% of the local median" in low-wage places; `7-validation.md:171` says "in their lowest-wage counties $17 is well above 60% of the median". The register has no county measure (`7-validation.md:91`). Both should be labeled judgment and reconciled; OEWS state and nonmetro medians would give a first, cheap measure without waiting for the commission. Changes: the right-to-work-state objection's answer and M-1.

**W-3. Inspections, publication and posted pay ranges rest on single uncorroborated studies stated as fact. Fix.** EV-WRK-249, 250 and 251 (LAB-7.02, 7.03) and EV-WRK-407 (LAB-7.08) have no independent corroboration (checker warnings). `4-specification.md:124-125` and `7-validation.md:150` omit EV-WRK-251's own caveats (the deterrence held where unions were strong; the "210 inspections" depends on cost assumptions). Present as one study's finding until corroborated. Changes: nothing decided; the prose.

**W-4. The 600,000 apprenticeship target has no basis beyond "about double". Fix.** `memos/8-training-wage-insurance.md:31` and `4-specification.md:212`; it is decided (`DEC-2026-11-17-11`), so it needs only to be labeled a decided target with no evidence of feasibility. `3-design.md:101` attributes "about 300,000 more starts a year" to EV-WRK-349, which holds only the FY2025 count.

**W-5. Smaller evidence items. Note.**
- Card check's case is one province's natural experiment (EV-WRK-168), called "the strongest in memo 3" (`4-specification.md:111`); fine, but "one province" should be said. Memo 3's "first-contract arbitration works" goes further than EV-WRK-169, which measures strikes.
- EV-WRK-365 (older TAA workers) is generalized to all ages at `4-specification.md:181` and `7-validation.md:181`.
- New Hampshire's 14(c) result (`4-specification.md:63`) omits EV-WRK-074's caveat that the state had no certificate workers at repeal.
- EV-WRK-077 (indexing raises job losses) is in the register but not presented in memo 1.
- Working papers graded B (EV-WRK-365, 067, 068, 258, 407): grade C until published, or say why B.
- EV-WRK-438 (OMB FY2017, the anchor for the $31 billion Extended Benefits line) is one executive-branch analysis of its own proposal, uncorroborated; `6-cost.md:336` says so. Bounded.
- 44 citation rows were read through search extracts; the load-bearing ones to spot-check against originals are EV-WRK-168, 189, 350, 396, 407 and 409, and the CBO rows 029, 032, 435 and 450.

**W-6. Legacy LAB-4B was misdescribed when it was weighed. Fix (record).** The legacy option is "$15, then indexed to the median" (`legacy/domains/domain-labor.md:100`). Memo 1 C (`memos/1-wage-floor.md:48-50`, also `3-design.md:48`) describes it through Hawley-Welch's price-indexed bill and counts price indexing against it, a drawback the legacy option does not have. Espen chose B; a status-line note in memo 1 corrects the record without reopening it. LAB-4C is likewise described with a commission the legacy option lacks (`memos/1-wage-floor.md:52`).

**W-7. Legacy items dropped without a stated reason. Note.** LAB-9's age band (18-26), the boards' cost moving from about zero to $1-3 billion, and the legacy large-firm definition (500+ workers or $1 billion of revenue). The dossier has no `restatement.json`; `models/registry/restatement.py` lists 5 numbers and 15 cross-dossier IDs not carried over, none logged. A short restatement log closes it.

**W-8. No second-Trump-administration analysis carries a recommendation alone. Pass.** EV-WRK-220 sits beside five other IDs at `4-specification.md:129`; EV-WRK-379 beside GAO's 378. The administration's data (BLS 078, 315, 317; DOL 349) is used as data, as the rule allows.

### L. Design lens (`DEC-2026-11-09-13`)

The dossier's lens table (`4-specification.md:302-324`) is good and mostly honest. Each test, document, deadline or cap checked against its burden:

**L-1. The credit's burden is understated. Fix.** `4-specification.md:309` says "a line on Form 941; the employer counts its workers below each step". LAB-5.01 (`:58`) actually requires, for each worker below a step in the prior quarter, the new rate less that worker's old wage, times hours, for four quarters, at 50%, 35% and 20%, against a controlled-group test. For a credit priced at about $3 billion across many small employers, that is a real paperwork cost for a small amount each. A flat amount per hour for each worker paid below the new rate would be simpler at the same size. This belongs beside W7 as an alternative form, not as a re-argument of C. Changes: LAB-5.01's form (with Espen's W7).

**L-2. LAB-8.05's "at least half" of WIOA training money is a quota on local boards. Note.** The lens prefers published counts with a review trigger. The evidence for sector training is strong [EV-SEC-143], so the share may earn its place, but section 4 should say why a published share with a review trigger would not do. Working choice; no decision changes.

**L-3. The service tranche's gate adds an Inspector General certification. Note.** LAB-9.03's two-year, 90%-filled and completion test is decided ("gated", `DEC-2026-11-17-32`); the IG certification is a working choice that adds a step and a likely delay. Consider the agency's published report alone, which the lens prefers.

**L-4. Earns its place.** One national schedule; the commission using data agencies already hold; attestation in place of contact counts (one fewer weekly test); wage insurance read from the state's own separation finding with no new adjudication; the automatic offer on the claim form; completion payments on records programs already file; mixing as a published target. LAB-11.03's work-sharing cap (52 weeks in five years) is justified by EV-WRK-383.

### F. The fiscal-rule report (`DEC-2026-11-10-05`) and the money

**F-1. The report has all three parts, on one basis. Pass.** `6-cost.md:240-269`: the yearly cost ($4 billion in FY2030 rising to $27 billion in FY2040), the permanent cost from FY2040 ($27.4 billion, $30 billion with the tranche), and the share of the plan-wide margin (4.5% of the $602.7 billion gap; a booking adds $6.8 billion, 1.1%). Spending, revenue effects and the floor's indirect effect are kept apart; contingent and provisional lines are shown from zero and not added; trust funds and Social Security are off the general fund. It does not treat the dossier's gap as a defect, and it sends one money choice to Espen (the credit's size). The budget model confirms it (Checks run). O-1 will move the general-fund offset and Social Security lines; the report should be rerun after that fix.

**F-2. LAB-5.01 should say the general fund makes Social Security and Medicare whole. Fix.** `6-cost.md:57` notes the credit runs against the employer's payroll tax and "should" carry a make-whole clause "at the next touch"; `provisions.json` does not yet. Without it the credit is a trust-fund loss, not a general-fund one.

**F-3. Small arithmetic and rounding. Fix (bundle).** `6-cost.md:234` says booked work rows of 250.0 and `:253` 249.9 (the tool's constants are rounded; LAB-8's change is +3.7 against them); part 9's FY2040 column rounds 0.15, 0.06 and −0.05 to one decimal (`:280-286`); `:70` calls $0.30 billion "the low end" of $0.2-0.4 billion; `:265`'s $3,718 billion is $3,718.6 billion. The trust funds' two lines net to zero every year by construction (`work_path.py:130-132`), though `:107` says they do not in any one year: say the tool shows the cycle average.

**F-4. Section 4 quotes section 6's old total. Fix.** `4-specification.md:328` gives section 6's firm lines as "+$0.18 trillion ... and +$25 billion"; section 6 gives +$0.20 trillion ($195.1 billion) and +$27.4 billion. `:386` says the README carries section 4's +$0.18-0.38 trillion; it carries only +$0.20 trillion. `:342` and `:384` keep "+$7-8.5 billion" for service in FY2040 against section 6's $6.7 billion civic and $9.4 billion with the tranche.

**F-5. Questions mainly about money.** The credit's size is already with Espen. O-1 makes memo 7's employer cost one too (question 1).

### E. Section 9 against sections 1-8

Every one of section 9's 61 evidence IDs exists and holds its figure. Every promise date matches section 4's provisions and section 5's timeline. Every provisional item is shown as provisional. **The single adult's result is carried honestly**: about 39% of a raise from $7.25 to $12.50 kept in 2032, against 59% at 2029 law, full time, on the marketplace in a non-expansion state, "on our estimates", with both causes and the 52-59% from 2035 (`9-public-case.md:55`, `:68`, `:118`; matching `7-validation.md:54` and `8-change-our-minds.md:79-86`; reproduced from the tool). Findings:

**E-1. A range is attributed to the wrong family. Fix.** `9-public-case.md:78`: "A full-time single parent ... keeps 81-98%". The single parent's range is 81-89% (`7-validation.md:39`); 98% is the married couple with the rent. ":68" and the source table use "full-time parents", which is right.

**E-2. Conditions dropped. Fix.**
- `:93`, the line cook: drops "on the marketplace" from the 39%, and cites section 7 part 4, which has no such household (the figures are part 1B's).
- `:56` and `:85` say UI "still runs" without the labor act; if the Byrd rule strikes the standards from R1 they ride the labor act (`4-specification.md:44`), and LAB-11.07 rides only the labor act. `5-delivery.md:111` says "UI's money".
- `:48-51`: the cost total includes the floor's indirect effect (about $32 billion), which exists only if the labor act passes; and "2030-39" and "2031-39" are fiscal years.
- `:35` and `:125`: the investigator numbers depend on appropriations (a statutory floor with a report to Congress, LAB-7.01).
- `:37`: "OSHA finishes its rule on January 20, 2029" promises a rule on day one; LAB-6.02 says OSHA finalizes it then if none exists.
- `:36`: penalties apply "for violations after signing" (`5-delivery.md:89`).
- `:61`: no 2031 date for UI and wage insurance; and "has been without a quorum" reads as ongoing (the quorum returned January 7, 2026).

**E-3. Source table and counts. Fix.** `:140` says "the eight already listed in the README"; the README lists seven (the known #436 nit). The heat row (`:178`) cites EV-WRK-237 for dates that are LAB-6.01's working choices; the overtime and layoff-notice rows (`:180`, `:181`) cite evidence for dates that are working choices in section 5; `:205` repeats `:161`; a few numbers have no row (`:5`, `:33`, `:46`, `:102`). `:3` says every tag names its source; bare tags remain at `:70`, `:71`, `:116`, `:126`.

**E-4. "Five steps." Fix.** See C-2; section 9 repeats it at `:61`.

### C. Consistency and record

**C-1. LAB-4.08's renewal bar contradicts the decided five-year phase-out. Blocker.** See Verdicts. The fix: no *new* certificates after enactment; existing certificates continue (renewed on the existing terms) at the rising wage until repeal on January 1, 2034.

**C-2. The floor is called "five steps" but has six dated rates. Fix.** $9.50 (2030), $11.00, $12.50, $14.00, $15.50 and $17.00 (2035). The credit's "first three steps", ending 2032, counts $9.50 as the first step, as do the tipped and 14(c) schedules, so "five annual steps" in LAB-4.01's title (`provisions.json:4`, `4-specification.md:54`), `7-validation.md:163`, `8-change-our-minds.md:16` and `9-public-case.md:61` is inconsistent. `DEC-2026-11-17-01` gives no count; pick one and use it everywhere.

**C-3. LAB-5.01's status does not say provisional. Fix.** `provisions.json:126` reads "decided ... the shares and cap are working choices"; the size is with Espen (W7). And `6-cost.md:306` lists the credit's shares and cap under "Commitments (decided)", against section 4's "working choices".

**C-4. LAB-4.04 adds a power the decision did not give. Fix.** The commission "may recommend a higher target or a slower step" for counties (`4-specification.md:57`); `DEC-2026-11-17-01` and memo 1 give it a higher target only. Mark the slower step as a working choice (it is advisory; Congress decides), or drop it.

**C-5. National service "by 2034". Fix.** The working ramp reaches 150,000 in 2034 and the tranche opens in 2035, so "about 200,000 positions by 2034" (`DEC-2026-11-17-32`) cannot be met on it. Sections 4, 6 and 9 say so; `3-design.md:26`, `memos/9-national-service.md:3`, the LAB-9 agenda note and `8-change-our-minds.md:66` (which also says "150,000 ... by 2033") do not.

**C-6. Record slips. Fix (bundle).**
- "LAB-3B" is cited for sectoral bargaining (`DEC-2026-11-17-06`, `3-design.md:53`, LAB-3.04, memo 5, `memos/README.md:13`), but `agenda/agenda.csv` has no LAB-3B row. Add it as an option row or cite memo 5 C.
- `README.md:9` says the work rows are "22 rows"; there are 31. `README.md:29` gives section 3's status as `-01` to `-36`, omitting `-95` and `-96`.
- `memos/README.md:15` and memo 7's status line still say "proposed LAB-11"; `3-design.md:181` still carries the "proposed note for rule 6 ... once Espen decides" (it is in `dossiers/shared-rules.md`); `3-design.md:167` asks for scores of "memo 3 B" where `DEC-2026-11-17-28` says memo 3 as decided, D. These files are kept as sent; a bracketed "decided" marker is enough.
- `4-specification.md:113` and `:145`: "Point 9/12, decided no" where the decisions are "yes" to a "no" recommendation; reword.
- `6-cost.md:113` cites the reviewer's note on #428, `:120` on #429.
- Agenda notes: no work row mentions section 9; LAB-18's note omits its two provisional pieces (18.03, 18.08). Outside work's rows (for their owners, not this dossier): COM-4's note is empty although `DEC-2026-11-17-26` directs it; AI-4 and AI-4D do not mention memo 10 or LAB-19.

**C-7. Checked and consistent. Pass.** Every DEC amount matches across sections 3-9, `provisions.json`, the agenda rows and the memos: the $17 schedule and median indexing; the credit's scope; seven years for the tipped wage and five for 14(c); 1,200 investigators by FY2034; treble damages; pay ranges at 15 or more employees and the pay-discussion right with its one exception; 600,000 apprentices by 2034 with about a third paid at completion; wage insurance's half the drop, $10,000, two years and four rules; 150,000 plus 50,000 service positions, gated; 90-day notice; the overtime method, never below $1,128, about $1,310-1,370 in 2030; the 18-month fast-food deadline. `DEC-2026-11-17-30`'s wording is in LAB-12.01 word for word. No provisional item is shown as decided anywhere.

### Seams with other dossiers

- **Secure floor and stage G:** the single adult's 2030-34 result (part E); incidence rows for LAB-11 and LAB-18 at booking (`7-validation.md:89`), or D3 understates work's benefits.
- **Democratic renewal (CAP-7):** work's seven written needs are answered (`6-cost.md:299`); OSHA's high end and FMCS are claims on the contingency. Nothing to change here.
- **AI topic:** AI-4's $200 billion row overlaps LAB-18 and LAB-19; re-scoping is the AI topic's (`6-cost.md:298`).
- **Immigration:** UI and wage insurance follow shared rule 3. Consistent.

## For Espen

Each is a separate question; none re-argues a decision.

1. **Memo 7's cost to employers** (O-1, after fix step 1 re-derives it). As specified, the unemployment benefit standard (75% of pay up to two-thirds of the state's average wage) looks to cost employers roughly twice what memo 7 showed: about $40-50 billion a year more at FY2025 levels, not $15-25 billion. Keep the standard as decided, or phase the 75% in (for example from 50% over the decade)? The general fund changes by only a few billion dollars a year either way.
2. **Puerto Rico's minimum wage** (M-1, after fix step 2 drafts options). $17 in 2035 would sit near Puerto Rico's whole median wage outside San Juan. Follow the national schedule, a separate path like American Samoa's (LAB-4.10), or the commission's report first?
3. **Farmworkers and domestic workers** (M-3). They stay outside the labor act's organizing rights, and farm overtime exemptions stay, in the first bill. Leave that for later work, as the dossier says, or bring options now?

Espen's open items W1 to W7 are unaffected by this review, except that L-1 adds a simpler form for the credit to W7's alternatives.

## Fix steps, in order (each sized for one session)

1. **The UI and wage insurance cost lines** (Most capable; `6-cost.md`, `tools/work_path.py`, `7-validation.md`, memo 7's and memo 8's status lines, the README). Re-derive regular benefits from LAB-11.01's parameters (replacement, recipiency, the 26-week floor, claim-length response), with ranges; rerun the tax offset, Social Security, workload and Extended Benefits lines; restate the fiscal-rule report (O-1). Reconcile wage insurance's chain with its figure, add discharges not for misconduct, and fix the take-up benchmark (O-2, O-4). Add the AmeriCorps match as a working assumption in LAB-9.01 and its line (O-5). Bundle F-3 and F-4. Prepare question 1 with A-3's alternatives for the lead.
2. **Puerto Rico and the territories' bite** (Most capable; `1-problem.md`, `2-what-works.md`, `4-specification.md`, `5-delivery.md`, LAB-4.10, the register). Catalogue OEWS medians for Puerto Rico, Guam and the Virgin Islands and the Puerto Rico minimum-wage studies; compute the floor's bite in each in 2030-35; draft options for Puerto Rico in LAB-4.10's form, provisional on a recommendation, with sections 6-9 updated (M-1). Use the same OEWS state and nonmetro medians to replace the unsourced county claims (W-2).
3. **Specification fixes** (Standard; `4-specification.md`, `provisions.json`, section 5 where it repeats them). C-1 (14(c) renewals); C-2 (the step count, everywhere); C-3 and F-2 (LAB-5.01's status and make-whole clause); C-4 (the commission's slower step); M-2 (tenure test: protected-leave quarters, successor employers); L-1 (the credit's burden row, and the flat-rate form as an alternative for W7); L-2 and L-3 (say why the WIOA share and the IG certification earn their place, or drop them); M-5 (LAB-11.10's authorities as statute text).
4. **Evidence and record** (Standard; `evidence.json`, memos 1, 3 and 8, sections 2-4 and 7, a restatement log). W-1 (record 051 and 063 as one finding; soften the prose); W-3; W-4; W-5; W-6 (memo 1 status note on LAB-4B and 4C); W-7 (restatement log); C-5; C-6, except agenda rows owned by other dossiers, which go to the lead as notes.
5. **Section 9 and the README** (Standard; `9-public-case.md`, `README.md`). E-1 to E-4, and every figure that steps 1 and 2 change, in the same PR as the last of them.
6. **L3 re-check** on the close-out PR (a fresh or the standing reviewer, `charter/STANDARDS.md`), then booking (tier 3, `6-cost.md` part 9, with the incidence rows `7-validation.md:76` lists).

Steps 1 and 2 can run in parallel; steps 3 and 4 can run in parallel with them on different files; step 5 follows.
