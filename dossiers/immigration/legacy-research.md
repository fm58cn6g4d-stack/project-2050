# A new consensus on immigration: what the legacy research and models found

Role: the restatement of the legacy project's immigration design, scores, ledger rows, capacity figures, vote and calendar results, and the immigration content of its other files. Each figure keeps its file and line, its basis tag and whether it must be re-run on the January 2029 baseline (`DEC-2026-10-29-01`). Status: draft (board row I2), compiled November 12, 2026 from `legacy/`, `models/tools/` and the October 28 intake by a Standard-tier subagent, and checked line by line by the dossier author. The legacy designs are working choices, not decisions (`DEC-2026-10-30-02`). Section 1 states the current facts from the register; this file only records what the legacy said and how far it can be used.

**Basis tags** are the legacy file's own (`legacy/domains/domain-immigration.md`, line 5):
- **sourced:** taken from a cited source;
- **scaled:** an outside figure adjusted by the legacy author;
- **estimate:** the legacy author's own number.

A fourth tag, **model**, marks output of a legacy script. "Re-run" says what a 2029 version needs.

## 0. Findings that change how the legacy may be used (read first)

1. **The immigration bill has never been scored.** The ledger's -$0.14 trillion is the 2013 Senate bill's CBO pattern, not a score of this design: "S.744 CBO pattern (~$175B first decade), not rescored" (`legacy/index/2029-trifecta-master-ledger.md:330`). The legacy file says it "needs a real score" (`domain-immigration.md:57`, `:158`, `:179`). Three things have changed since 2013 and push the figure in both directions (`domain-immigration.md:57`):
   - the labor market;
   - the design's lack of S. 744's guest-worker expansion;
   - the 2025 law's benefit and fee changes.

   The figure can stand only as a labeled working assumption until it is rescored.

   **The "$175B" is a superseded CBO figure, and the sign of the pattern is in doubt.** It is CBO's preliminary figure for S. 744 as amended by the Corker-Hoeven border amendment: its June 24, 2013 letter put the first-decade saving at about $175 billion. That reading of the letter is the standing reviewer's, on PR #264. The register's quotation from the same letter says the saving would be smaller than the committee bill's $197 billion "by something less than $40 billion" [EV-IMM-207]. CBO's estimates were:
   - the committee-approved S. 744: $197 billion less deficit over 2014-2023 [EV-IMM-200];
   - the amended bill, preliminary: about $175 billion (the June 24 letter) [EV-IMM-207];
   - the Senate-passed bill, in the final estimate, which supersedes the letter: $158 billion, with $23 billion of discretionary costs [EV-IMM-205];
   - and either way, on-budget deficits rose in the first decade, because the gain was off-budget Social Security tax [EV-IMM-208].

   S. 744 bundled legalization with large new legal and guest-worker flows that added about 10 million people by 2023 [EV-IMM-203]. CBO's 2021 scores of the narrower legalizations, closer to tiers A and B, show deficit increases [EV-IMM-213] [EV-IMM-215]. Section 2, part A sets out the evidence. The legacy sign (a saving) is therefore not a safe working assumption either.
2. **The court that decides the cases is unscored too.** CRT-5 is "about $0.03T, range $0.02T to $0.06T (estimate; unscored)" and "needs a real score" with IMM-1 (`legacy/domains/domain-courts.md:108`, `:246`, `:251`). It is in no ledger total (`2029-trifecta-master-ledger.md:15`).
3. **The USCIS money is counted in three places that have never been reconciled.**
   - The capacity line carries USCIS at $40 billion (`domain-capacity.md:127`).
   - IMM-3 carries about $10 billion of asylum and refugee processing.
   - The capacity review's bottom-up need for that processing is about $5.4 billion: "IMM-3 is about double the bottom-up figure; the immigration owner may trim it" (`legacy/sources/capacity-recovery-other-agencies-review.md:199`).
   - The overlap of E11 and the USCIS line is "Unchecked" (`domain-capacity.md:149`).
   - The $6 billion asylum reserve is "pending Espen" (`legacy/governing/project-2050-governing-decisions.md:239`).
4. **The world-state facts were news-sourced.** The October 2026 border, detention, TPS, DACA and H-1B facts in `domain-immigration.md:21-30` cite news sites (Voz, Deseret, Latin Times, WJLA, Bloomberg Law, CDF Labor Law). Section 1 re-checks each one against primary or stronger sources and says where they differ.
5. **The legacy noted that the 2025 law's enforcement money expires, but never checked the dates.** It says the multi-year funding "runs out before or around FY2029 (my reading; check the expiry dates)" (`domain-immigration.md:25`, open item 2 at `:180`). Whether detention savings can be booked turns on this. Section 1, part D, gives what the statute says.
6. **Some legacy facts are the author's memory, not a source.** These are marked "my knowledge; not re-checked":
   - the parliamentarian's three 2021 rulings (`domain-immigration.md:59`);
   - the refugee floor's basis (`:182`);
   - the ports-of-entry fentanyl claim (`:80`).

   Section 2 sources each one or drops it.
7. **The child-poverty model has no immigration-status data.** It applies no Social Security number test: "No automatic immigration/SSN imputation" (`models/tools/child-poverty/model.py:435`). Its three identification branches are "incomplete legal branches" (`models/tools/child-poverty/README.md:70`). The single-payer model's residual uninsured share for status is a placeholder, 1% (range 0-3%), "project judgment under shared rule 3 ... no register source yet" (`models/tools/health-coverage/inputs.csv:182`).
8. **No household, labor-market or fiscal model of immigration exists.** The incidence model leaves out "the H-1B fee ... and immigration's legalization effects" (`legacy/index/revenue-household-incidence-model.md:119`). The plan's immigration model is "new, built during that dossier" (`charter/PLAN.md` 3.4).

## 1. The design and its ledger row

| Item | Legacy figure | Basis | Where | Re-run for 2029? |
| --- | --- | --- | --- | --- |
| Bill total, general fund, FY2030-39 | -$0.14T (-$0.25T to -$0.02T); 12 floor days | estimate (scaled from S. 744) | `domain-immigration.md:17`, `:19`; ledger `:330`, rollup `:45` | Yes: a real score of the chosen design on CBO's current baseline, with CRT-5 |
| Ledger row status | "Unverified", confidence 82, "estimate" | ledger | `2029-trifecta-master-ledger.md:330` | — |
| IMM-1 and IMM-2 together | -$0.15T (-$0.25T to -$0.05T) | estimate, from "CBO's score of S. 744 (2013), which cut deficits by about $175B in its first decade (sourced, via the ledger)" | `domain-immigration.md:11`, `:57` | Yes. Section 2 restates CBO's 2013 figures from CBO itself |
| IMM-3, asylum and border processing | $0.01T ($0 to $0.02T) | estimate | `domain-immigration.md:13`, `:83` | Yes, against the capacity review's $5.4B (finding 3) |
| IMM-4, enforcement | 0 against the baseline: "no savings can be booked" because the 2025 law's detention money is time-limited | estimate | `domain-immigration.md:14`, `:97` | Yes, once the expiry dates are read (section 1, part D) |
| IMM-5, citizenship | $0.00T ($0.00T to $0.01T) | estimate | `domain-immigration.md:15` | Fee waivers need a cost |
| IMM-6, delivery | "in CAP-7S / CAP-7 (USCIS, $40B) plus fees" | estimate | `domain-immigration.md:16`, `:120` | Yes, bottom-up |
| Dynamic sensitivity DY8 (never a pay-for) | +$0.02T / +$0.06T / +$0.15T / +$0.20T. "CBO's 2013 S.744 score: $197B deficit cut with labor-supply effects vs $175B without (via CRFB, CBPP)" | scaled; secondhand | `2029-trifecta-master-ledger.md:135` | Both are CBO figures, but the ledger mislabels them: $197B is the committee bill [EV-IMM-200], and about $175B is the preliminary letter on the amended bill [EV-IMM-207]. They are not with and without labor-supply effects. CBO's final figure is $158B as passed [EV-IMM-205] |
| Long-term model | IMM-1 -0.140 over the window; -0.034 in each later year shown: "Net saving grows as legalized workers enter the tax base" | model | `legacy/index/fiscal-long-term-model.md:176` | Yes, with the score |
| How to read the saving | "IMM-1's net saving is a dated planning estimate, not guaranteed current-baseline revenue. Fee receipts spent on enforcement are not general-fund fiscal space" | judgment | `legacy/sources/fiscal-recovery-and-education-redesign.md:117` | Carried as a caution |
| H-1B fee, ledger IF1 | $0.015T ($0.010T to $0.020T), "Spent within receipts on adjudication and training; employers, not households"; fee about $5,000 to $10,000 by employer size | estimate | ledger `:399`, channel summary `:62`; `domain-immigration.md:68`, `:71` | Yes, against the 2025-26 fee law and rules (section 1) |
| Registration window | 18 months, opening within 180 days of enactment | design | `domain-immigration.md:44` | — |
| Tier B benefit bar | Five years from means-tested federal benefits, "on the S. 744 model" | design | `domain-immigration.md:57` | Rule 3 table (I3) |
| Detention cap | About 30,000 average daily, with an emergency waiver; current level "about 65,000" | estimate | `domain-immigration.md:90`, `:97` | I3 sizes it |
| Refugee floor | About 50,000, "chosen to sit below every ceiling set from 1980 to 2016 (my knowledge; not re-checked)" | estimate | `domain-immigration.md:79`, `:182` | Section 2 checks the ceilings |
| USCIS rebuild | About 12,000 hires (Bill Book 15); a six-month target | design | `domain-immigration.md:119` | Bottom-up in I3 |
| Asylum timeline | Merits decided within 180 days, "on the 2022 Asylum Processing Rule model" | design | `domain-immigration.md:77` | Section 2 weighs the rule's record |

## 2. Capacity: the USCIS and asylum lines

| Item | Legacy figure | Basis | Where |
| --- | --- | --- | --- |
| USCIS share of the agency rebuild | $40B, 7% of the line: "Administration of comprehensive immigration reform (ledger E11)" | estimate | `legacy/domains/domain-capacity.md:127` |
| Batch 4 reserve | $37B held; $31B proposed, of which "USCIS asylum and refugee processing $6B"; "pending Espen" | estimate | `domain-capacity.md:141`, `:144`; governing decisions `:239`; options register `legacy/index/options-register.md:347` |
| Immigration court administration | "0 here": funded in CRT-5, "not counted twice" | design | `domain-capacity.md:140`; governing decisions `:237` |
| Asylum officer corps and refugee processing, bottom-up | +1,500 officers (range 1,000-2,500), $0.43B a year, about $5.4B over FY2030-39; reconciled with IMM-3 | estimate | `legacy/sources/capacity-recovery-components.csv:107`; `capacity-recovery-other-agencies-review.md:154` (3.8, range 1.9-6.6, $B), `:199` |
| Office of New Americans administration | $0.02B a year (range 0.01-0.05) | estimate | `capacity-recovery-components.csv:108` |
| USCIS backlog clearance | $3.0B lifetime (range 1.5-5.0), "About $0.7B a year for four to five years (member request anchor)" | scaled | `capacity-recovery-components.csv:109` |
| Online filing for every form | $0.5B lifetime (range 0.3-1.0) | estimate | `capacity-recovery-components.csv:110` |
| USCIS pending cases | 12,000,000 in 2026, "Up almost 2M since Jan 2025", from a member of Congress's press release; "About 97% of USCIS funding is fee revenue" | sourced (secondhand) | `capacity-recovery-components.csv:39` |
| Backlog appropriation request | $0.7B, a request by 126 members, not enacted | sourced (secondhand) | `capacity-recovery-components.csv:40` |
| Legalization adjudication | "about 12000 hires ... Fee-funded ... not CAP money" | design | `capacity-recovery-components.csv:183` |
| Overlap check | "CMS, HUD, Education, USCIS against their program rows ... E11 may ... already include administration. Unchecked" | open | `domain-capacity.md:149` |

*Re-run:* all of it. D9 asks for a bottom-up rebuild "from agency funding history" (governing decisions `:237`), and the next agency review was to be "SSA, then USCIS" (`:478`). I3 sizes USCIS from the workload the chosen design creates.

## 3. The court (CRT-5)

| Item | Legacy figure | Basis | Where |
| --- | --- | --- | --- |
| Design | Real Courts, Rule of Law Act of 2026 (H.R. 7836; S. 5094), outside the executive, Tax Court model; restored Article III habeas and de novo review; appointed counsel for children and people with serious mental illness; A-file access; limits on in absentia orders; bond hearings | design | `domain-courts.md:102` |
| *Slaughter* fallback | Fixed terms with for-cause removal; an express fallback folding the court into the judicial branch | design | `domain-courts.md:104` |
| Cost | $0.03T ($0.02T to $0.06T), unscored; 5B about $0.01T; 5C "700-1,000 Senate confirmations" | estimate | `domain-courts.md:17`, `:108`, `:114-116` |
| Scale (October 2026) | "About 3.1 million active cases pending at the end of August 2026 (TRAC)"; judges from 726 (February 2025) to 520 judges and 33 assistant chief judges (February 2026); the 2025 law "capped immigration judges at 800"; "94% of asylum cases denied in June 2026" | sourced (TRAC, news) | `domain-courts.md:106` |
| Fuller account | 279 judges fired or resigned in FY2025-26, "about 38% of 735"; 3,092,988 active cases at the end of August 2026, down from more than 4.18 million; a 2026 Merit Systems Protection Board ruling that judges are removable at will | sourced (TRAC/EOIR, news) | `legacy/sources/courts-rebalancing-the-three-branches-2026.md:162` and following |

*Re-run:* section 1, part C states the caseload, judge counts and grant rates from EOIR and TRAC directly.

## 4. Votes, floor time and the calendar

| Item | Legacy figure | Basis | Where |
| --- | --- | --- | --- |
| Must pass in the first trifecta | IMM-1, with HLT-3, CLI-6/CLI-7 and AI-1/AI-4 | decision (D1 stipulation) | governing decisions `:52`; ledger `:160`; `models/tools/votes-model.py:56` |
| Survival at 51 | ◐ for every row: needs D2's majority-precedent path | design | `domain-immigration.md:9-16` |
| Vote simulation | IMM-1 passes in 29% of runs under F (decided), 33% under C, 0% under G and with no rules change | model (`votes-model.py`) | `legacy/index/vote-simulation.md:41`; final-passage table `:90` (37%, 80%, 29%, "war game: imm") |
| Bill Book war game | "Under F or C: the bill passes with every vote at 52-54 if D2 holds, but it carries the most defection risk of any first-Congress bill after statehood" | judgment | `domain-immigration.md:125` |
| Under G or at 51 | The bill fails; only executive pieces survive, "All of them are reversible" | judgment | `domain-immigration.md:126-127` |
| Calendar | 12 floor days, scheduled for September 2029 | model | `legacy/sources/calendar-c-development.md:33` |
| Talarico stress test | Immigration "Fails in 2032; passes March 2033 after 23 days"; "The scenario's floor cost is double the ledger's"; 54-46 on March 28, 2033 | scenario | `legacy/frameworks/scenario-stress-test-talarico-2029-2037.md:30`; `legacy/sources/scenario-talarico-2029-2037.md:102` |
| Path C sensitivity | Swapping in the bills the minority is proud to block (IMM-1, RTS-3) changes the total by about a day | model (`ledger-paths.py`) | ledger `:154` |

*Re-run:* the vote model's inputs are from before the November 2026 election. `dossiers/scenario/` holds the rebaselined Senate (D1 updated, `DEC-2026-11-08-01`). The 29% is kept as history, not as a forecast.

## 5. Immigration in other legacy files

| Topic | Legacy content | Where | What this dossier does with it |
| --- | --- | --- | --- |
| Health: immigrant waiting period | "End five-year wait for lawfully present immigrants | H.R. 9432 | ... | Unscored; tens of billions"; a restoration item "unpriced" with its date undecided | `legacy/sources/health-working-group-memo-analysis.md:125`; `legacy/sources/health-delivery-component-register.csv:11` | Rule 3 table; care has since decided to restore lawfully present immigrants in 2029 (HLT-1.02, `DEC-2026-11-10-09`) |
| Health: the 2025 law's immigrant limits | Secs. 71109 (Medicaid and CHIP, from October 1, 2026), 71301 (premium credits, 2027), 71302 | `legacy/sources/health-restoration-remedy-cohorts.csv:2`, `:6`, `:7` | Section 1, part G, with care's register entries |
| Health: H-1B fee and clinicians | An exemption for clinicians from the $100,000 fee (H.R. 7961) | `health-working-group-memo-analysis.md:68`, `:255` | Section 1, part B |
| Family: the child credit's number rule | "Immigration rules create a real coverage boundary"; the adult claimant rule a "Conflicting/underspecified record"; the child's number a "likely legal exclusion, not a take-up problem" | `legacy/sources/family-child-poverty-report-1.md:54-62` | Rule 3 seam with the secure floor (memo 1, part 2) |
| Voter registration from benefit records | No record is passed on for a known noncitizen household member; one adult's record and action cannot establish other members' eligibility to vote | `legacy/sources/democracy-medicaid-registration-transaction.md:52-60` | A seam with democratic renewal (noted in the README) |
| Public safety | Little support for immigration enforcement as a cause of the crime decline; "IMM-4's priorities are consistent with that" | `legacy/domains/domain-public-safety.md:176` | Section 2, part D context |
| AI and due process | AI-5's due-process rules reach "benefit, tax, immigration or enforcement decisions", first at SSA, the IRS, CMS and USCIS | `legacy/domains/domain-ai.md:120` | A delivery seam for I3 |
| Care workforce | "a care workforce of ~4M, which makes immigration and care policy the same bill"; HLT-4 and the care-worker visa "flagged for both files" | `scenario-talarico-2029-2037.md:215`; `legacy/frameworks/scenario-stress-test-talarico-2029-2037.md:138` | Rule 8 seam (care point 8) |
| Long-range plan | "Immigration levels (IMM-) as a fiscal and labor-force lever" | `legacy/frameworks/long-range-plan-2030-2050.md:66` | Context for I3; levels are not a legacy design |

## 6. Older sources the legacy drew on (provenance only)

Superseded inputs, recorded because their figures recur in public debate. None is a project figure.

- **The Project 2029 chapter on immigration** (`library/intake/2026-10-28/project-2029/project_2029/project_2029_chapter3_immigration.md`, catalog SRC-0273; external intake, March 2026, not project canon). It proposes:
  - legalization for about 10-12 million people with 5+ years' presence;
  - a 200-day asylum standard (line 195);
  - refugee admissions of 125,000 a year with a 95,000 floor (lines 199, 345);
  - mandatory E-Verify for employers with 20+ employees over 24 months (line 202);
  - $3.6 billion for backlogs and per-country caps raised from 7% to 15% (lines 210-211);
  - pathway provisions that activate only after enforcement milestones are certified (line 553).

  Its fiscal claims are its own and are not used:
  - "$1.5–2.0 trillion over 10 years" in added tax revenue from legalization (line 430);
  - mass deportation at "$88 billion/year" (line 432).

  It cites outside figures that section 2 checks at their source before any use:
  - Peterson Institute: deporting 8.3 million people would cut GDP 7.4% (line 70);
  - OBBBA's "$170.1 billion" for enforcement (line 58);
  - Gallup July 2025: 78% back citizenship (line 36);
  - Third Way: a 30-point trust deficit (line 19).
- **The archived CBO score simulator inputs** (`legacy/archive/ideas-project-2029-cbo-score-simulator-inputs.md:247-285`):
  - $6 billion a year for five years for border technology;
  - 5,000 judges and 4,500 court attorneys at about $3-4 billion a year;
  - detention at about $350 a person a day against about $17 for alternatives, and about $8.4 billion a year for about 66,000 people;
  - counsel for detained asylum seekers and children at $0.5-1 billion a year;
  - refugees at 125,000 with a 95,000 floor at about $14,000 each;
  - $1.6 billion a year for Central America;
  - $3.6 billion for backlogs.

  All are unsourced in the file. The daily costs are checked in section 1, part D.
- **The war-game simulator** (`legacy/archive/wargame-trifecta-2029-simulator.jsx:109-110`): the "Comprehensive Immigration Reform" bill with a 180-day timeline and the DHS split into a Humanitarian Processing Service, the source of IMM-4B and of the vote simulation's "war game: imm" label.
- **The executive action inventory** (`legacy/archive/ideas-project-2029-master-executive-action-inventory.md:36`, `:72-82`): day-one immigration orders (DACA, refugees, deportation review), with a note that restoring DACA by order carries legal risk. Relevant to the 2029 preparation exception, not designed here.

## 7. Open items the legacy left, and where this dossier takes them

| Legacy open item | Where | Taken up in |
| --- | --- | --- |
| Rescore the bill with CRT-5 | `domain-immigration.md:179`; ledger `:266`; options register `:100`; governing decisions `:333` | I3 benchmarks; a real score in section 6 |
| The 2025 law's detention money: expiry dates | `domain-immigration.md:180` | Section 1, part D |
| Tier C | `domain-immigration.md:181`; options register `:278` | I3, fork 1 |
| Refugee floor size | `domain-immigration.md:182` | Section 2, part C; I3, fork 6 |
| IMM-3 about double the bottom-up processing need | `capacity-recovery-other-agencies-review.md:199` | I3, fork 12 |
| USCIS overlap with E11 | `domain-capacity.md:149` | I3, fork 12 |
| The $6B asylum reserve, pending Espen | governing decisions `:239` | I3, fork 12 (put to Espen there) |
| The child credit's number rule for adults and children | `family-child-poverty-report-1.md:125-126`, `:184` | Rule 3 table, I3 fork 11, with the secure floor |
| Coverage of people without status | `models/tools/health-coverage/inputs.csv:182` | Rule 3 table, I3 fork 11, with care |
