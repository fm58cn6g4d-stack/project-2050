# Democratic renewal: validation

Role: section 7 of the democratic renewal foundation. It runs the models that can be run on sections 4 to 6, sets the foundation's figures against outside ones, says what the models miss, names the outcomes the foundation moves and how they would be seen, answers the strongest objections from the left, the right, election officials and the courts, and lists the signs of failure. Part 8 checks that every one of the 137 provisions in `provisions.json` is covered. Status: **draft** (stage F, step 7), on `DEC-2026-11-17-40` to `-99`, with every provisional item of sections 4 and 5 kept provisional and one new one added (part 10). **Nothing is booked here** and no adopted input changes. Every figure is project arithmetic or a restated outside score, not an official score. Outcomes it serves (`charter/outcomes.md`): **OUT-09**, its own; **OUT-10**, with work; and, through delivery, **OUT-01 to OUT-07**.

## How to read this section

- **Conventions** follow section 6: nominal $ billion by federal fiscal year, a cost positive, on the general fund, against the January 2029 law and the budget model's booking (case `mixed`, on main after #431).
- **What each input is** (commitment, working assumption, open question or study in implementation) is in part 9, for every material input this section uses.
- **The vote model's odds are relative, not forecasts.** Its own page says so: every vote parameter is the legacy war game's or an estimate, and the Senate roster is the war game's mid-2026 map (`legacy/index/vote-simulation.md`, line 3).
- **Two notes from #430's review are carried** and closed in part 2: the match's legacy high against DEM-1's ledger high, and the JUDGES Act's seat count.
- **Legal holdings** are cited from the Court's own syllabus or opinion, saved in `library/text/` [EV-DEM-359] to [EV-DEM-368]. A holding says what the Court decided then; it is not a prediction of what this Court would do with these statutes.

## 1. Model runs

Six models touch this foundation. Each was run on this branch from the committed inputs.

| Model | What it covers here | Run | Result |
| --- | --- | --- | --- |
| The budget model's common rebuild (`models/tools/run-all.sh`, dry run) | The nine booked rows and the plan-wide gap | Rebuilt every generated output; "unchanged" for all of them, `vote-simulation.md` and `capacity-funding-model.md` included | The booked figures section 6 quotes follow from the committed inputs: $507.2 billion over FY2030-39 and $50.0 billion in FY2040, against the $602.7 billion FY2040 gap |
| Section 6's draft scenario (`models/tools/democratic_renewal_cost.py --check`) | The booked rows by year, the unbooked lines, IMM-1's later rebooking | "All checks passed" | Reproduces section 6: booked rows 8.29% of the FY2040 gap; unbooked $19.4 billion (range $10.8-28.8 billion) and $2.54 billion; memo 10's contingency $43.2 billion, $29.7 billion and $4.7 billion |
| The vote simulator (`models/tools/votes-model.py`, 4,000 Congresses a scenario, fixed seed) | Whether this foundation's bills pass the 2029-30 Congress, by Senate rules path and seat count | Through the rebuild; output identical to the committed page | Part 1.1 |
| The capacity funding model (`models/tools/capacity-funding.py`) | CAP-7S's availability and cash | Through the rebuild; its checks pass | Part 1.2 |
| **New: the hiring-pace check** (`models/tools/democratic_renewal_pace.py`, draft; `--check` passes) | Whether CAP-7's sustained money can be spent at the pace agencies can hire | Three paces by three pay shares | Part 1.3 |
| The immigration model (`dossiers/immigration/tools/immigration_model.py`) | The immigration court's corps (CRT-5.06) | Run with no flag | Part 1.4 |

No model exists for turnout, registration, campaign finance, court workloads or civil legal aid. Those are tested against outside evidence in part 2, and part 3 says what a model would add.

### 1.1 The vote simulator: does any of it pass?

Share of 4,000 simulated Congresses in which each bill is enacted, at 53 Senate seats (the middle of D1's 52-54) and 221 House seats, with one senator who opposes any rules change (`legacy/index/vote-simulation.md`; the seat runs from the rebuild's `votes.json`):

| Bill (the model's row) | What it carries here | F, graduated cloture (decided) | G, the democracy carve-out (fallback) | No rules change | At 51 / 52 / 54 seats, under F |
| --- | --- | --- | --- | --- | --- |
| DEM-1 | The democracy act, Divisions A to E | **72%** | **91%** | 0% | 14% / 46% / 88% |
| INT-1 | The ethics and accountability act | 55% | 0% | 0% | 5% / 28% / 76% |
| CRT-P1 | The judgeships, integrity and terms bills, as one | **31%** | 0% | 0% | 2% / 12% / 50% |
| CAP-8 | The civil service and delivery act, with Congress's capacity | 73% | 0% | 0% | 13% / 46% / 88% |
| DEM-5 | D.C. statehood | 26% | 32% | 0% | 1% / 10% / 44% |
| DEM-6 | Puerto Rico's status vote | 62% | 79% | 0% | 7% / 34% / 82% |
| CAP-7S (in R1) | The surge | In **87%** of passed R1 packages; some version of R1 is enacted in 98% | same | same | 80% / 84% / 90% |
| DEM-17 (in R3) | The capital fund | In 96% of passed R3 packages | same | same | 84% / 92% / 97% |
| The appropriations omnibus | CAP-7, DEM-11, DEM-16 (the model's routing) | 73% | 1% | 1% | 15% / 47% / 88% |

**What it says.**
- **Everything regular-order rests on the rules change.** With no rules change every bill here is at zero, and the rules change is adopted in 73% of runs with one holdout, 42% with two and 11% with three. D2 decides which of these items can pass at all, as section 1 recorded; this section does not reopen it.
- **The carve-out favors the democracy act.** Under G, DEM-1 rises to 91% because it is the bill the carve-out covers, while INT-1, CRT-P1 and CAP-8 fall to zero. That supports section 4's choice to carry DEM-2, the match and DISCLOSE inside the democracy act (memo 2 B; memo 3 D): outside it they would get no carve-out.
- **The courts package is the weakest bill,** at 31% under F. The model scores it as one bill on the war game's Supreme Court parameters, with no Republican crossover. Section 4 already splits it: the judgeships go first as their own bill aimed at 60 votes, because the 2024 bill passed the Senate by unanimous consent before a veto [EV-DEM-044]. The model cannot see the split (part 3).
- **The surge is the capacity money most likely to arrive,** inside R1 at 87%, ahead of the omnibus at 73% under F and about 1% under G.

### 1.2 The capacity funding model

It checks that CAP-7S is multi-year money available on enactment, routed to R1, with FY2029 cash left unpriced rather than set to zero. Its checks pass. **What it does not see:** it works on the ledger row before the October 26 scaling, $560 billion, while the booking scales the surge to $98.0 billion (`models/tools/budget/note-cap7-sizes.md`). Its cash shape (about 11.7%, 20%, 21.7%, 20%, 16.7% and 10% over FY2030-35) is the shape the booked $98.0 billion follows, so the shape holds; the level on its page is not the booked one. Bringing the row to the booked size is the clean-up `note-cap7-sizes.md` names (section 6, part 9, item 5).

### 1.3 The hiring-pace check: can CAP-7's money be spent at the pace set?

Sections 3 and 5 say hiring, not money, sets the pace [EV-DEM-277] [EV-DEM-085], and assume about a quarter of each agency's added-staff target is hired a year from FY2030 (range a fifth to a third; `3-design.md`, part G, "Timing and pace"). The new draft script asks whether the money path matches that pace. It lays part G's sustained allocation ($32.5 billion in FY2040, deflated at the booked path's own growth of about 3.8% a year) on staff on board; a share of each line (pay) follows staff and the rest (systems, space, contracts) follows the booked ramp.

| | FY2030 | FY2031 | FY2032 | FY2033 | FY2030-33 | FY2030-39 |
| --- | --- | --- | --- | --- | --- | --- |
| **Booked CAP-7** | 8.6 | 17.8 | 27.7 | 28.7 | **82.8** | **279.2** |
| Booked, as a share of its own full run rate | 33% | 67% | 100% | 100% | | |
| The review's midpoint path, which CAP-7.02 names as the working path [EV-DEM-328] | 10.4 | 18.1 | 24.4 | 25.9 | 78.8 | 254.6 |
| **Part G's allocation at the working pace** (a quarter a year; 70% pay) | | | | | **55.7** | **227.3** |
| Range across paces and pay shares (a fifth to a third; 60-100% pay) | | | | | 38.9 to 65.2 | 207.9 to 236.9 |

**Findings.**
- **The money path runs about two years ahead of the hiring assumption.** The booked path reaches its full run rate in FY2032, which matches hiring about half of each target a year, twice the working pace. The ledger row's note says the same: "stepping up over FY2030-32" (`models/data/inputs/ledger-bills.csv`, CAP-7). The review's midpoint path does the same (about 44%, 75% and 97% of its run rate in FY2030-32). Section 3's "most hiring lands by FY2033-34" and its money path do not agree. The legacy IRS row is at the fast end: 24,000 enforcement staff "hired over three years (30/60/90% in FY2030-32)", "about 8,000 hires a year, near the FY2024 pace" (`legacy/sources/capacity-recovery-budget-review.md`:27).
- **At the working pace, about $52 billion of the booked $279.2 billion is not spent in FY2030-39** (range $42-71 billion). It has two parts, which answer different questions:
  - **(a) About $22 billion (range $13-42 billion) is timing:** part G's own allocation reached later than its path, about $23 billion less in FY2030-33 than the review's midpoint path, which CAP-7.02 names as the working path (78.8 against 55.7). CAP-7.02 keeps unspent money available and every run reaches the full $32.5 billion by FY2034, so FY2040, the year the fiscal rule tests, does not change. This is the booking question (part 10, question 4).
  - **(b) $29.7 billion is memo 10's sustained contingency** (CAP-7S.02), money above the allocation that is released only against a written need. It is not timing: if never released it is never spent, and it stays booked at $4.7 billion in FY2040 too. Whether it (and the surge's $43.2 billion) stays booked is stage G's question, with the October 26 allowance (section 6, part 1.3), not a pace finding.
- **Net hiring needed** for the six agencies sized, about 54,000 added staff [EV-DEM-331]: about 13,500 a year at the working pace (10,800 at a fifth, 18,000 at a third), the IRS about 7,500 of it. Those are net of attrition; gross hiring is higher. The IRS onboarded nearly 19,000 external hires in FY2024 [EV-DEM-370], so gross hiring at the needed scale has been done recently. Against it: large agencies hired 65,953 people and lost 134,122 in January to June 2025 [EV-DEM-085]; the IRS lost more revenue agents than it hired in the first half of FY2023 with the money in hand [EV-DEM-277], and 31,273 of its staff left between January 2025 and January 2026, a 28% net decrease [EV-DEM-089]; SSA's staff fell from 56,645 in FY2024 to 48,530 in FY2026 [EV-DEM-105]. The pace needs CAP-11's tools in force from R1, and the 141,084 people who took deferred resignation [EV-DEM-083] are a pool that already knows the work.
- **For the design:** nothing in sections 4 or 5 changes. The release rule (CAP-7.02) already pays against hiring, so a slow path holds money rather than losing it. The IRS's enforcement yield (G8) is the line most exposed, because a slow path delays the yield more than it saves outlays (section 6, part 1.3). **For the booking step** (recommended, provisional; part 10, question 4): lay part G's allocation inside CAP-7 on the hiring pace, about $22 billion less over FY2030-39 and no change in FY2040, and lag G8's yield with it. The contingency's $29.7 billion and $4.7 billion are left as booked for stage G.

### 1.4 The immigration model: the court's corps

The model's central case needs about **1,673 judges in all (920 added)**, hired about 250 a year, to clear the backlog by **FY2035**; at 150 hires a year it clears in FY2037, and at the 800-judge cap that takes effect on November 1, 2028 [EV-IMM-105] it does not clear (the low and high cases are 2,403 and 863 judges). Judges on board rise from 1,003 in FY2030 to 1,253 in FY2031 and 1,503 in FY2032. So the court takes over on October 1, 2031 (working) with about 1,250 sitting judges, each needing a merit screen and a 14-year appointment by a court of appeals. That confirms section 5's "more than 1,000" and the need for provisional fix 2 (interim appointments of up to two years, CRT-5.03). The term-limited increment's steady-state need is about 726 judges, the basis for memo 9 part 2's split of about 200 of the 920 added judges on regular terms (section 6, part 5). The corps is reset in 2033 from receipts after legalization (CRT-5.06).

## 2. Against outside figures

| Line | This foundation | Outside figure (publisher, year) | How they compare |
| --- | --- | --- | --- |
| **The voting floor's federal cost** (DEM-1, Division A) | Near zero beyond DEM-11's money | The Freedom to Vote: John R. Lewis Act, which joined this floor and preclearance: −$131 million net over 2022-2031 (CBO and JCT, 2022) [EV-DEM-322]; the 2019 For the People Act: $2.4 billion of costs over 2019-2024, $750 million of it security grants (CBO, 2019) [EV-DEM-320] | Same direction: the floor binds states; its federal cost is the money that comes with it |
| **Election administration** (DEM-11) | About $2 billion a year (range $1-4 billion), $20 billion over FY2030-39 | More than $50 billion over ten years is needed, and an average federal election year costs $4-6 billion (Institute for Responsive Government and Project for Election Infrastructure, advocates, no method published) [EV-DEM-356]; over $1 billion of security grants since 2018 [EV-DEM-171]; $45 million in FY2026 [EV-DEM-017] | About two-fifths of the advocates' figure: a federal share of running costs, not the whole need. About 40 times FY2026's grant, and recurring. No independent cost study exists (part 3) |
| **Registration from records** (DEM-1.01) | Registration by default from records | Australia: 97.8% of eligible people enrolled in September 2026 [EV-DEM-168], up from 90.9% in 2010 after direct enrolment began in 2012 [EV-DEM-169]; Canada's register 96.4% in 2019 [EV-DEM-170]; the United States 73.6% registered by self-report in 2024 [EV-DEM-001] | The direction is well supported; the size of a U.S. gain is not. State AVR raised registration 9 to 94% in the states studied (Brennan Center, an advocate) [EV-DEM-145]; turnout effects are small, about 1 point or less [EV-DEM-146] |
| **The other floor rules' effects** | No target is set (`charter/outcomes.md`) | Same-day registration: youth turnout +3.2 to +7.3 points [EV-DEM-148]; mail voting: about +2 points, no partisan effect [EV-DEM-150] [EV-DEM-151]; preclearance: long-run turnout +4 to 8 points [EV-DEM-157]; cure notices: 25 points more likely to have the vote counted [EV-DEM-167]; a restored-rights mailing: registration +1.8 points [EV-DEM-161] | Each effect is measured in one or a few studies; they do not add up to a total, and part 3 says why none is claimed |
| **The match** (INT-5.01) | About $6 billion over FY2030-39 (range $4-8 billion; up to $12 billion at high ceilings) | H.R. 1's House-only match: about $620 million for 2028 and $850 million for 2030 (CBO, 2021) [EV-DEM-355] | Scaled for Senate candidates and in-state gifts (section 6, part 2). **Review note 1, closed below** |
| **The stock ban** (INT-1) | Near zero; revenue −$3 million | The ETHICS Act: −$3 million of revenue over 2024-2034 and $0-0.5 million of administration (CBO, 2024) [EV-DEM-325] | Matches |
| **The judgeships** (CRT-1.01) | About $0.4-0.6 billion over FY2030-39 for 71 seats in three tranches | The JUDGES Act of 2024: $98 million direct and $251 million subject to appropriation over 2024-2034 for **63 permanent plus 3 temporary seats, 66 in all** [EV-DEM-324]; per new judge, compensation of $275,000 in 2025 rising to $340,000 by 2034 and court costs of about $700,000 a year once established (CBO, on the Administrative Office's figures, for the 63 permanent seats) [EV-DEM-357] | **Review note 2, closed below.** About $1.0-1.1 million a seat-year; 71 seats arriving in 2030, 2033 and 2035 give about 520 seat-years in the window, about $0.55 billion |
| **The judges' corps** (CRT-5.06) | About 1,673 in all, 920 added (range 863-2,403) | 700 more than 649, 1,349 in all, to clear a smaller backlog by FY2032 (CRS, 2023) [EV-IMM-642]; about 250 more a year at 957 completions a judge (Manhattan Institute, 2025) [EV-IMM-646] | Both point to several hundred more judges; the model uses a slower completions rate because hearings with counsel are slower [EV-IMM-106] |
| **The court's structure** (CRT-5.09) | About $6.9 billion (range $3.2-9.7 billion) | EOIR $790.0 million in FY2026 (CRS, 2026) [EV-DEM-354]; the Administrative Office $107.0 million [EV-DEM-347]; the immigration review's re-score, $3-10 billion (project's own) | No CBO or judiciary estimate exists (Evidence still needed) |
| **Legal aid** (CRT-20.01) | About $4.6 billion (range $2.3-8.5 billion); LSC about doubled by FY2035 | LSC $540.0 million in FY2026 and $21.0 million requested for FY2027, for closure (CRS, 2026) [EV-DEM-352] [EV-DEM-353]; New York's eviction right fell to 30% representation in March 2025 as funding and providers lagged [EV-DEM-243] | The schedule is paced by grantees' hiring for that reason. If LSC is closed before 2029, restoring it comes first (about $5.5 billion; section 6, part 3) |
| **The library line** (DEM-17.02) | About $0.75 billion a year | IMLS's Grants to States, $180.0 million in FY2024 [EV-DEM-338] | 2.8 to 5.6 times today's line; no outside benchmark beyond it |
| **The regulators and integrity units** | About $3.0 billion over the decade | EAC $58.9 million, FEC $80.9 million, OGE $23.0 million, MSPB $51.5 million in FY2026 (CRS) [EV-DEM-347] | Several times today's bases: the restoration part G sized |
| **The agency rebuild** (CAP-7S, CAP-7) | Allocation $54.8 billion and $249.5 billion; booked $98.0 billion and $279.2 billion | The legacy second-round review: $59.8 billion of surge (range $31.4-103.3 billion) and $254.6 billion sustained (range $160.7-355.1 billion) [EV-DEM-328] | The allocation sits near the review's midpoint and the booking near its high case for the surge; the review is the project's own (grade D), with no outside score of the rebuild as designed |
| **IRS hiring** (CAP-11.01, the IRS's line) | About 7,500 net added a year at the working pace | Nearly 19,000 external hires in FY2024 (TIGTA) [EV-DEM-370]; the legacy row's 8,000 a year "near the FY2024 pace" | Gross hiring at that scale has been done; net growth depends on attrition, which rose sharply in 2025 [EV-DEM-089] |
| **Inspectors general** (CAP-7.05) | Staffed to follow the money, in the integrity line | About 13,800 inspector general staff reported about $65.6 billion of potential savings in FY2025 [EV-DEM-223] | No saving is counted from them |

**Review note 1: the match's legacy high against DEM-1's ledger high.** Section 6, part 2 ran two different highs together. INT-5's own legacy range is "$0.00T to $0.03T" for the match alone (`legacy/domains/domain-integrity.md`:78). DEM-1's ledger row, which carries the whole democracy act, runs to **$0.04 trillion** (`models/data/inputs/ledger-bills.csv`, DEM-1, `cost_hi`). CBO's scale supports neither for the match, whose high here is about $12 billion. The democracy act's other costs are small (DEM-2.05's commission grants, a few hundred million dollars at most on judgment; the floor and the Voting Rights titles about zero), so **DEM-1's whole contents are about $4-15 billion over FY2030-39**, against the row's $0-40 billion. The row's midpoint, $10 billion, holds; a booking could narrow its range to about $0.004-0.015 trillion, as section 6 said. Section 6, part 2 and section 4's INT-5.01 now state the two highs separately.

**Review note 2: the JUDGES Act's seats.** CBO's 2024 estimate covers **63 new permanent district judgeships phased over 2025-2035 plus 3 temporary judgeships in 2025, 66 seats in all** [EV-DEM-324]. Its per-judge figures are for a new permanent judgeship [EV-DEM-357]. The per-seat arithmetic here uses that one denominator, the new judgeship: about $1.0-1.1 million a seat-year (compensation of about $0.28-0.34 million plus court costs of about $0.70-0.75 million). The 66-seat total of $349 million is a check, not the basis: at $1.0-1.1 million a seat-year it implies about 320-350 seat-years over 2024-2034, about five years a seat, which fits seats phased in across that decade. Section 6's parts 1.2 and 6 and section 4's CRT-1.01 now say "63 permanent plus 3 temporary, 66 in all". This foundation's 71 seats are the Judicial Conference's 2025 request, 2 court of appeals and 69 district judgeships [EV-DEM-041]; a court of appeals seat costs somewhat more than a district seat, which the range carries.

**What the benchmarks do not test.** No outside score exists for the Voting Rights titles alone [EV-DEM-323], a term statute, the immigration court's structure, the library line, the agency rebuild as designed or shared rule 5's records statute. Where those are priced, the price is the project's.

## 3. What the models miss

| Missing | Direction | Size or note | What would answer it |
| --- | --- | --- | --- |
| **The democracy act's added titles in the vote model** | Lower odds than the model's 72% | The model scores DEM-1 on the war game's Freedom to Vote parameters. Section 4's act also carries DEM-2's ban and criteria, the House state option, the match, DISCLOSE, the coordination presumption and shareholder authorization, which get no objection rate of their own. INT-15 is the item most likely to cost a fast track (legacy, `domain-integrity.md`:179) | A per-title objection rate in `votes-bills.csv` (a model input, tier 3) |
| **The courts package's split** | Higher odds for the judgeships | The model's CRT-P1 is one bill on Supreme Court parameters, with no Republican crossover; the judgeships alone have bipartisan history [EV-DEM-044] | Separate rows for the judgeships act and the integrity and terms bills |
| **CAP-7's vehicle** | Lower odds, or a Byrd problem | Section 4 puts CAP-7.01, a **permanent** increase, in R1 as a direct appropriation; the ledger and the vote model route it through annual appropriations (the omnibus, 73% under F, about 1% under G). Permanent new spending in reconciliation runs into the Byrd rule's bar on raising the deficit beyond the window unless it is offset there or ends with it. **Open question for the vehicle step:** CAP-7 in R1 as money for FY2030-39, renewed later; in R1 with out-year offsets; or by annual appropriations at the omnibus's odds | The Parliamentarian's view in 2029; the vehicle checker on the models roadmap |
| **Byrd eligibility of the hiring tools** | Delivery risk | CAP-11.01's hiring authority is a rule riding R1 as a condition on the money and moves to the civil service act if struck. The vote model assumes R1 eligibility and does not certify it (`votes-model.py`, docstring) | The Parliamentarian |
| **Hiring as the limit on outlays** | Lower outlays in FY2030-33 | At the working pace part G's allocation is reached about $22 billion later in FY2030-39 than the booked ramp (part 1.3); the budget model spends on the booked ramp, and also books memo 10's $29.7 billion contingency as if spent. The pace check treats every entity in part G alike, including the $67.0 billion for entities outside the flagships, whose hiring is not sized | The time-to-hire and net-hiring series CAP-11.01 builds; OPM's quarterly counts |
| **Turnout and registration** | — | No model. The effects in part 2 come from separate studies of single rules; rules interact and populations differ, so no turnout total is claimed | A state panel of the floor's rules before and after, from 2030 (study in implementation) |
| **Behavior of states** | Uneven reach | States that resist the floor are reached only by enforcement (DEM-1.13, provisional fix 3); nineteen states had banned ranked-choice voting by March 2026 [EV-DEM-255], so DEM-4.01's uptake will be one-sided | The EAC's survey every cycle [EV-DEM-346] |
| **Litigation** | Delay or loss of a part | Every new statute here will be challenged; severability (DEM-1.13, 1.19, 2.06, INT-1.05, INT-15.01, CRT-5.10, CRT-15.02) limits the loss to the struck part. No model prices delay | The three-judge courts' calendars (CRT-3.02) |
| **Money in politics** | — | No model of how candidates and donors respond to the match, the coordination presumption or DISCLOSE; New York's first matched cycle is the nearest evidence [EV-DEM-193] [EV-DEM-194] | The FEC's published participation in the first two matched cycles (study in implementation) |
| **Court workloads** | — | No docket model for the federal courts; the judgeships rest on the Judicial Conference's weighted filings [EV-DEM-042] [EV-DEM-043]. The immigration model sizes CRT-5's corps but not the appellate panels' load | The Administrative Office's caseload statistics |
| **Civil legal need** | Need above supply | LSC's survey finds 92% of substantial problems get no or not enough help (LSC, which has a stake) [EV-DEM-240]; the schedule follows provider hiring, not need | Grantees' hiring reports; a current LSC attorney count (the register's is 2015 [EV-DEM-349]) |
| **Shared rule 5 and improper payments** | Possibly lower improper payments | Agencies attribute about 73% of FY2021-24 overpayments to not using data they held [EV-DEM-291]; no saving is counted, because a match is a flag, never a denial [EV-DEM-292] | Each program's improper-payment rate before and after (CAP-7.03) |
| **The two delivery contingencies' overlap** | Booked money no program has claimed | Memo 10's $72.9 billion and the October 26 allowance's $100 billion: up to about $173 billion over FY2030-39 and $19 billion in FY2040 (section 6, part 1.3) | Stage G's choice |
| **Interest and economic feedback** | Higher deficit before financing | None of the models computes interest on these rows or any growth effect of a more capable state | The budget model, once booked |

## 4. The outcomes it moves

No numerical targets are set (`charter/outcomes.md`; targets are Espen's). Each row gives the baseline in the register, the provisions that move it and how the plan will see it. A good trend would not show that a provision caused it.

| Outcome | Measure and baseline | What moves it | How the plan will see it |
| --- | --- | --- | --- |
| **OUT-09, influence: registration and turnout gaps** | 73.6% registered and 65.3% voted in 2024; about 28.0 million citizens unregistered, a floor [EV-DEM-001] [EV-DEM-002]; underrepresentation of 4.4 points for ages 18-29, 5.6 for people with a high school credential only, 3.1 for Hispanic citizens [EV-DEM-003] [EV-DEM-004] [EV-DEM-005]; a disability turnout gap of 7.3 points (one working paper) [EV-DEM-006] | Registration from records (DEM-1.01, 1.02), same-day and preregistration (1.03), early and mail voting (1.04, 1.05), identity by statement (1.06), cure (1.09), restored rights (DEM-12.01), paid time (DEM-13.01), preclearance (DEM-1.16) | The CPS supplement every federal election; the EAC's survey [EV-DEM-346]; registration against Australia's and Canada's [EV-DEM-168] [EV-DEM-170] |
| **OUT-09, influence: representation** | The 2025-26 mid-decade maps; Section 2 limited to intent [EV-DEM-007]; the House at 435 since 1913 [EV-DEM-074] | DEM-2's ban, criteria and fast track; DEM-1.17, 1.18; DEM-4.01 and the 2031 and 2033 decisions; the match (INT-5.01), widening who gives [EV-DEM-193] | Maps' partisan bias each cycle [EV-DEM-261]; small donors' share and geography in the FEC's data |
| **OUT-09, a government that delivers: times and errors** | Improper payments about $186 billion in FY2025 [EV-DEM-113]; SSA callback waits averaging 108.6 minutes and about 25 million calls ended without service [EV-DEM-106]; federal service satisfaction 68.6 [EV-DEM-129] | The rebuild (CAP-7S, CAP-7, CAP-11, CAP-12, CAP-13), its measures and release rule (CAP-7.02, 7.03), shared rule 5 (CAP-19), payments in a lapse (CAP-4.01) | CAP-7.03's quarterly measures for every plan program; GAO's yearly audits (CAP-7.05) |
| **OUT-09, remedies** | 17 inspectors general fired without the notice the law requires in 2025 [EV-DEM-036]; the FEC without a quorum [EV-DEM-031]; civil legal help missing for 92% of problems [EV-DEM-240] | The remedies in section 5, part 5; LSC's growth (CRT-20.01); the immigration court's review (CRT-5.04, 5.05); recovery protections (CAP-19.05) | Appeal times and outcomes; LSC grantees' counts; the FEC's time to act on complaints |
| **OUT-09, trust** | 17% trust the government in Washington most of the time (Pew, 2025) [EV-DEM-065]; 34% approve of the Supreme Court (Gallup, 2026) [EV-DEM-062]; 79% favor fixed terms and 89% a strict ethics code (Marquette, 2026) [EV-DEM-063] | The stock ban, the ethics rules and the court integrity act; delivery that works (renewals without forms went with more trust in one Medicaid survey [EV-DEM-186]) | The same polls; no target. Trust lags delivery and moves with events this plan does not control |
| **OUT-10, connection** | 28.3% volunteered through an organization in 2022-23 [EV-DEM-067]; 54.2% helped neighbors [EV-DEM-068] | Civic education (DEM-16.01), libraries and public space (DEM-17.01, 17.02), the assemblies (DEM-18.01); national service is work's LAB-9, whose placements include election offices | The CPS Civic Engagement supplement; the assemblies' published evaluations |
| **OUT-01 to OUT-07, through delivery** | Each flagship's own baseline | The dated needs in section 5, part 3.1: the IRS's monthly payment file by July 2030 (OUT-01, OUT-02), SSA's paid leave mid-2030 (OUT-02, OUT-08), HUD's first awards in 2030 (OUT-04), ACF's free tier for 2030-31 and CMS's wave 1 on January 1, 2031 (OUT-03), FEMA's line (OUT-05), Wage and Hour and OSHA by FY2034 (OUT-06), the immigration court from October 2031 (OUT-07) | Whether each dated need is met on its date; the flagships' own signs of failure. **A miss here is a miss in their outcomes,** which is why the hiring pace (part 1.3) is this foundation's largest risk to the plan |
| **OUT-11, the guardrail** | — | Booked rows $50.0 billion in FY2040, 8.3% of the gap; unbooked about $2.5 billion | Section 6, part 8: reported, not gated |

## 5. Reach: for whom

| Group | Size (register) | What they get | When |
| --- | --- | --- | --- |
| Citizens not registered | About 28.0 million, a floor [EV-DEM-002] | Registration from records, with a notice and a way to decline | By the 2032 general election (provisional effective dates) |
| Voters without a current ID | Not counted in the register | Any listed card or a signed statement; a free mailed card, optional | From any federal election 180 days after enactment (provisional) |
| Mail voters whose ballots are rejected | 584,463 ballots in 2024 [EV-DEM-018] | Notice within two business days and a cure period | By 2032 |
| People disenfranchised by a conviction | About 4 million in 2024, about 72% living in their communities [EV-DEM-159] [EV-DEM-160] | Federal voting on release, with an official notice | 180 days after enactment |
| Voters in places with a record of violations | Set each year by the rolling formula | Preclearance; the results test and the intent claim | On enactment |
| People who give small amounts | — | A $25 gift worth $175 to a candidate who opts in | From the 2032 cycle (working) |
| People before the immigration court | A corps of about 1,000 to 1,670 judges over FY2030-35; counsel for children, people with serious mental illness and everyone detained (IMM-3.12) | A court outside the prosecutor's department, with review in the courts of appeals | October 1, 2031 (working) |
| Low-income people with civil legal problems | 74% of low-income households had at least one in the past year [EV-DEM-240] | More LSC-funded lawyers, paced by hiring | Stepped to FY2035 |
| Everyone in a plan program | Every flagship's population | Eligibility from records, a fact proved once, sampling after payment, recovery limits, payment in a lapse | From each program's start |
| Federal career staff | About 50,000 positions moved, by OPM's estimate (CAP-8.01) | Appeal rights restored, with a faster performance process | 2029 |

**Who is not reached, and why.**
- *Voters in states that resist the floor* are reached only after notice and a suit (DEM-1.13, provisional); the 2032 date gives offices time, and the Attorney General can sue first.
- *State and local elections* are outside the floor: Congress's Elections Clause power reaches congressional elections (part 6.1). The state tracks (DEM-10, 19, 20) are campaigns.
- *Districts drawn under current law* stay until 2031 if the democracy act is late (section 5, part 4).
- *Residents of D.C. and the territories* wait on admission acts and the second wave (DEM-5.01, DEM-6.01, DEM-7.01).
- *People with civil legal problems beyond what LSC's grantees can hire for:* no right to counsel is created now (memo 9 part 3 B).

## 6. Objections answered

### 6.1 Federalism and the Elections Clause

| Objection | Answer | Evidence |
| --- | --- | --- |
| "Elections belong to the states; this is a federal takeover." (right; many state officials) | The Elections Clause gives states the duty to set the rules for congressional elections and gives Congress the power to alter those rules or supplant them altogether; in 2013 the Court held that power lets the NVRA's federal form displace Arizona's documentary-proof rule [EV-DEM-359]. The floor governs federal elections only; states keep running them, run their own elections as they choose and keep their own privacy law (DEM-1.14). The parts that rest on other powers, presidential elections and the enforcement clauses, are severable by part (DEM-1.13) | EV-DEM-359, EV-DEM-262 |
| "Congress is commandeering state officials." | Congress already directs how states run federal elections through the NVRA and HAVA (HAVA's statewide list [EV-DEM-345]), under the same clause. The money comes with the duties: DEM-11's recurring grant and CAP-13's build money, with no new state match (section 5, part 6) | EV-DEM-359, EV-DEM-345 |
| "A one-size floor ignores local conditions." (election officials) | The floor sets minimums, not methods: sites, drop boxes beyond one a county, formats and staffing stay local. The rules that need new systems wait until 2032 (provisional), and a state that is ready can start sooner | — |
| "DEM-2 dictates how states draw maps." | Title I bans only mid-decade redraws and binds every state alike; Title II's criteria are severable from its fairness test; commissions are a safe harbor, never a mandate. The Court has held the Elections Clause lets a state's voters give mapmaking to a commission [EV-DEM-262], and *Rucho* left partisan fairness to Congress | EV-DEM-262 |

### 6.2 The Voting Rights Act after *Brnovich* and *Callais*

| Objection | Answer | Evidence |
| --- | --- | --- |
| "*Callais* makes a restored results test pointless." (right, and many on the left) | Section 4 claims no survival for Title III-A: *Callais* limits Section 2 to a strong inference of intent [EV-DEM-007], on constitutional as well as statutory grounds as section 4 reads it. That is why Title III-B stands alone, giving the intent claim rules of proof it can be won on, and why Title II's preclearance rests on a current, rolling record, the answer to *Shelby County*'s objection to a frozen formula [EV-DEM-011]. Each title is severable (DEM-1.19); if intent claims also narrow, III-B's record supports an amendment (AMD-5) | EV-DEM-007, EV-DEM-011 |
| "*Brnovich* already set how vote-denial claims work; leave it." | *Brnovich* read Section 2's text and listed the circumstances that matter, among them the size of a rule's burden and how far it departs from standard practice in 1982, and held a state may act against fraud without waiting for it to occur within its own borders [EV-DEM-360]. Those guideposts are a reading of the statute, which Congress may change by amending the text: Title III-A states the results test with findings on the current record. *Callais*'s reasoning is the harder limit, and III-B is drafted for it | EV-DEM-360, EV-DEM-007 |
| "Preclearance treats states unequally." | Coverage turns on violations found in a recent rolling window and is recalculated each year, so it follows conduct, not 1965's history. Preclearance raised long-run turnout 4 to 8 points [EV-DEM-157]. No CBO score of the title alone exists [EV-DEM-323] | EV-DEM-157, EV-DEM-011 |

### 6.3 Voter rolls and ID

| Objection | Answer | Evidence |
| --- | --- | --- |
| "Registration from records will put noncitizens on the rolls." (right) | Citizenship is checked against federal records (SSA, USCIS, passports), and household records pass on only the person known to be a citizen of voting age (DEM-1.02, 1.08). Audits find noncitizen registration rare: 20 among 8.2 million in Georgia [EV-DEM-163], 27 of 2,069,640 records in Utah [EV-DEM-164]. A non-match is a flag for a person, with notice | EV-DEM-163, EV-DEM-164 |
| "Without documentary proof of citizenship, how do you know?" | The records answer it without a trip to an office. The House-passed SAVE America Act's documentary proof [EV-DEM-015] puts the burden on every voter to find a document; the federal form asks only for an attestation under penalty of perjury, and the Court held Arizona could not add documentary proof to it on its own [EV-DEM-359] | EV-DEM-015, EV-DEM-359 |
| "No photo ID requirement invites fraud." (right) | The Court upheld Indiana's photo ID law against a facial challenge [EV-DEM-361]; that permits ID, it does not show ID is needed. A national panel found strict ID had no effect on turnout [EV-DEM-154]; GAO found turnout fell in Kansas and Tennessee [EV-DEM-155], which Heritage disputes [EV-DEM-156]. The design mails every registrant a free card from records (DEM-1.07), so ID becomes easy to have, and keeps the signed statement under penalty of perjury, checked afterward, so no eligible voter is turned away | EV-DEM-361, EV-DEM-154, EV-DEM-155, EV-DEM-156 |
| "A national voter card is ID creep." (left) | It is optional, free, mailed from records and never a condition of voting; the statement route stays, and the photo is optional (DEM-1.06, 1.07) | — |
| "Limits on removals will leave the dead and movers on the rolls." | Removals continue on records evidence (death, a recorded move, the voter's request) with notice; only removal for not voting alone and mass third-party challenges without individual evidence are barred (DEM-1.10), and the NVRA's quiet period before an election is kept | — |
| "Sharing federal records with states is a surveillance risk." (left; privacy groups) | Each use is logged, a person can see what was used, and no record shared under the rule may be used for immigration or criminal enforcement (CAP-19.02, DEM-1.14). The Justice Department's 2025-26 suits for unredacted rolls [EV-DEM-021] are why | EV-DEM-021 |

### 6.4 Money in politics and the First Amendment

| Objection | Answer | Evidence |
| --- | --- | --- |
| "The Court has closed off campaign finance reform." | It has closed some doors and left others open. Public financing was upheld in *Buckley* as an effort "to use public money to facilitate and enlarge public discussion", while mandatory spending limits were struck [EV-DEM-363]; the match has no spending cap and no trigger, which *Arizona Free Enterprise* forbids [EV-DEM-208]. Disclosure won 8-1 in *Citizens United* [EV-DEM-205], and DISCLOSE is tailored to money used or earmarked for election spending, with a donor's right to restrict a gift, as *Bonta* requires [EV-DEM-206]. The Court accepts only quid pro quo corruption or its appearance as a ground to restrict political money [EV-DEM-364], so the coordination presumption (INT-8.01) treats single-candidate super PACs' spending as contributions to the campaign, the category limits still reach, inside what *NRSC* left standing [EV-DEM-027] | EV-DEM-363, EV-DEM-208, EV-DEM-205, EV-DEM-206, EV-DEM-364, EV-DEM-027 |
| "The coordination presumption and shareholder authorization will be struck." | Either may be, and each is written to fail alone: the presumption is rebuttable and severable; INT-15's disclosure and board-vote sections stand if the shareholder vote falls, and its First Amendment footing and the union asymmetry go to legal review before drafting (legacy open item 2) | — |
| "Public money for politicians." (right) | About $6 billion over FY2030-39 on our estimates, against $5.8 billion that presidential and congressional candidates raised in the 2023-24 cycle alone [EV-DEM-023]. It is paid only to candidates who opt in and raise small in-state gifts | EV-DEM-355, EV-DEM-023 |
| "The match will not change who runs or who gives." (left and right) | The evidence is modest: New York City's matched donors came from 89% of block groups against 30% for unmatched races [EV-DEM-193]; state public financing came with 12 to 18 more candidates a state-year [EV-DEM-198]. The first two cycles' FEC data are the test | EV-DEM-193, EV-DEM-198 |
| "A citizen suit will flood courts with partisan complaints." | It opens only after 120 days without FEC action, against the violator, not the agency; a five-member FEC with a quorum of three should act within that time. The FEC deadlocked on about 13% to 24.4% of closed matters [EV-DEM-209], the problem the suit answers | EV-DEM-209 |
| "The stock ban is too broad, or too narrow." | Diversified funds, Treasuries and retirement accounts stay out; there is no forced sale, and 1043's deferral means compliance is not taxed [EV-DEM-334]. CBO scored a similar ban near zero [EV-DEM-325]. *Provisional:* new individual-stock purchases inside a self-directed retirement account count (part 10, question 1) | EV-DEM-325, EV-DEM-334 |

### 6.5 Judicial independence and the legitimacy of court reform

| Objection | Answer | Evidence |
| --- | --- | --- |
| "Term limits by statute violate 'good Behaviour'." (right; some scholars) | The Presidential Commission was divided on exactly this [EV-DEM-233]. CRT-15.01 keeps Article III pay and tenure for life, moving a Justice to senior service after 18 years, and applies only to Justices appointed after enactment; the part that moves sitting Justices is separate and severable (CRT-15.02) because it is the part most likely to fall. The amendment (CRT-15.03) goes beside the statute | EV-DEM-233, EV-DEM-232 |
| "Court reform is court-packing by another name." (right) | The Court stays at nine (28 U.S.C. 1 [EV-DEM-343]); seats open on a schedule, two years apart, so each President gets two appointments a term. Expansion, including 13 Justices to match the circuits, stays an option, not enacted (`DEC-2026-11-17-85`). Fixed terms are popular: 79% favor them [EV-DEM-063] | EV-DEM-343, EV-DEM-063 |
| "Without expansion, the current majority stays for years." (left) | It does: the first statutory term ends about 2047, and sitting Justices move only if CRT-15.02 survives. The plan answers the Court's rulings in statute: the Voting Rights titles, the *Corner Post* fix, remedies after *CASA*, express delegations after *Loper Bright* and penalties written for district court (CRT-7.02, 8.01, 9.01, 10.01) [EV-DEM-051] [EV-DEM-052] [EV-DEM-047]. Expansion stays on the table if those fail | EV-DEM-051, EV-DEM-052, EV-DEM-047 |
| "A binding code and an inspector general threaten judicial independence." (judges) | The Court adopts its own code and decides its own recusal motions; no outside body decides (CRT-2.01, 2.02). The inspector general is appointed by the Chief Justice after consulting the Judicial Conference, on EXE-5's notice-and-reasons template. The Commission found a binding framework would raise difficulties but even an advisory code would help [EV-DEM-248]; 131 judges sat in 685 matters with a financial conflict [EV-DEM-229] | EV-DEM-248, EV-DEM-229 |
| "Recorded votes and reasons on emergency orders micromanage the Court." | They ask the Court to say what it decided and why, within 30 days, so lower courts know what an order means; they do not limit what the Court may grant | — |
| "Random assignment and three-judge courts take discretion from judges." | They codify the Judicial Conference's March 2024 policy on random assignment, which some districts declined, and use the three-judge court Congress already provides for apportionment cases [EV-DEM-344] | EV-DEM-344 |
| "An impeachment norm invites impeaching judges for their rulings." | The norm says the opposite: never for a ruling, always for corruption; the House impeached Judge Porteous for kickbacks [EV-DEM-341] | EV-DEM-341 |

### 6.6 The immigration court and Article III

| Objection | Answer | Evidence |
| --- | --- | --- |
| "Judges without life tenure deciding removal cases violate Article III." | The Court's public-rights doctrine lets Congress assign certain matters to judges outside Article III, and in 2024 it listed "immigration law" among the recognized categories, while adding that the presumption is in favor of Article III courts [EV-DEM-365]. The limit is on private-rights claims: a bankruptcy court could not enter final judgment on a common law counterclaim [EV-DEM-366], though parties may consent [EV-DEM-367]. Here the courts of appeals review questions of law de novo (CRT-5.05), and CRT-5.10 sends any class of cases a court holds needs an Article III judge to the district court, keeping the rest | EV-DEM-365, EV-DEM-366, EV-DEM-367 |
| "Appointment by the courts of appeals breaks the Appointments Clause." | Courts of law may appoint inferior officers; the Court has held even an Article I court can be a "Court of Law" for that purpose [EV-DEM-368], and the courts of appeals already appoint bankruptcy judges for 14-year terms [EV-DEM-333]. Because the judges sit in the judicial branch and are removable only by judges, *Slaughter*'s holding on executive removal [EV-DEM-037] does not reach them | EV-DEM-368, EV-DEM-333, EV-DEM-037 |
| "An Article I court on the Tax Court model would have been the usual design." | Memo 9 A proposed it [EV-DEM-244] [EV-DEM-245], as most outside proposals do. CRS reports that the bar associations and the immigration judges' association back an independent court, while opponents raise the executive's foreign-policy authority, slower hiring during a restructuring and funding disputes [EV-DEM-369]. After *Slaughter*, an Article I court's independence would rest on removal protection the Court has just struck for agencies, so section 4 placed the court as a unit of the district courts (A′), where judges remove judges. The hiring risk is real: the transfer is set for 21 months after the act, and EOIR keeps hiring until then (section 5, part 4) | EV-DEM-244, EV-DEM-245, EV-DEM-369, EV-DEM-037 |
| "Federal judges do not want an immigration docket." (courts) | The court is its own unit with its own judges, staff and appellate panels. The district judges' added load is the restored habeas and pattern-and-practice jurisdiction and any class CRT-5.10 sends them. The structure line (CRT-5.09) pays for the court office, so the Administrative Office's existing budget [EV-DEM-347] is not drawn on | EV-DEM-347 |
| "Screening 1,250 judges by October 2031 is impossible." | It may be. Provisional fix 2 continues unscreened sitting judges for up to two years under interim appointments (part 1.4) | — |

### 6.7 Can the capacity money be spent at the pace set?

| Objection | Answer | Evidence |
| --- | --- | --- |
| "Agencies cannot hire this fast." (right, and career managers) | They are right about the booked path: it assumes full strength in FY2032, about twice the working pace (part 1.3). The design does not depend on it: money is released against published hiring paths, a slow agency's tranche waits and the money stays available (CAP-7.02), and the flagships' dated needs are met first through each program's own rule (provisional fix 1). At the working pace about $22 billion of the allocation is spent later than booked in FY2030-39, with no change in FY2040; the $29.7 billion contingency on top is spent only against a written need, which is stage G's question | EV-DEM-277, EV-DEM-085, EV-DEM-328 |
| "The IRS showed it cannot use new money." | In the first half of FY2023 it lost more revenue agents than it hired [EV-DEM-277]; but it onboarded nearly 19,000 external hires in FY2024 [EV-DEM-370], and the 2023 filing season met the 85% phone goal after IRA hiring [EV-DEM-276]. Revenue agents take a year or more to become productive (legacy review), so the yield (G8) is the line most exposed to a slow path and should be lagged with it at booking (part 10, question 4) | EV-DEM-277, EV-DEM-370, EV-DEM-276 |
| "The contingency is a slush fund." (right) | It is released only against a published written need, for enacted programs, with 30 days' notice to the Appropriations Committees and GAO's yearly audit of every release (CAP-7S.02, 7.05). It is inside the booked figures, not added to them | EV-DEM-328 |
| "Two contingencies are one too many." | Possibly. Memo 10's and the October 26 allowance together hold up to about $173 billion over the decade that no program has claimed; the first known claims on memo 10's are about $0.7-1.1 billion (section 6, part 1.3). Whether both stay is stage G's | — |
| "A hostile administration will sit on the money." (left) | EXE-3's cause of action is wave three; until then DEM-11's and CAP-13's formula money carries its own 60-day payment clock, enforceable by the recipient (provisional fix 4). The released tranches still depend on OMB | — |
| "The rebuild restores staff only to repeat 2025." | The civil service statute bars schedules that strip appeal rights (CAP-8.01) and pairs it with a faster performance process (CAP-9.01). Georgia's at-will reform left employees pessimistic and resignations rising [EV-DEM-311] [EV-DEM-312]; federal personnel records show almost no political cycles in the career service [EV-DEM-314] | EV-DEM-311, EV-DEM-312, EV-DEM-314 |

### 6.8 Election officials' practical objections

| Objection | Answer | Evidence |
| --- | --- | --- |
| "We cannot rebuild registration for 2030." | The provisional effective dates agree: rules that need new systems wait until the 2032 general election, and only barrier-removing rules apply 180 days after enactment (section 5, part 4). The Court has warned that court orders changing election rules can confuse voters, a risk that grows as an election nears [EV-DEM-362]; the 180-day rule leaves time for enforcement suits to be settled early | EV-DEM-362 |
| "One-time grants never pay for running costs." | That is why DEM-11 is a recurring, indexed block grant with a separate equipment fund (`-94`): every federal dollar since 2003 has been one-time (Stewart, 2022) | EV-DEM-017, EV-DEM-171 |
| "Poll workers and staff are leaving, and we are threatened." | More than 770,000 poll workers served in 2024, most 61 or older, and 47.9% of jurisdictions struggled to recruit [EV-DEM-019]; 32% of local officials reported threats [EV-DEM-022]. The election-worker protections ride the act (DEM-1.20), and national service places members in election offices (LAB-9) | EV-DEM-019, EV-DEM-022 |
| "The EAC cannot certify equipment without a quorum." | It has had no commissioners since July 2026 [EV-DEM-020]; DEM-1.15 lets the executive director keep the form and guidelines in force and run DEM-11's formula without a quorum, and nominees are named in 2029 under current law | EV-DEM-020 |

## 7. Signs of failure

Published counts, each with what it triggers (none is a gate; `DEC-2026-11-09-13`):

| Measure | Expected | A sign of failure | Response |
| --- | --- | --- | --- |
| The rules change (D2) | Adopted in 2029 | Not adopted by mid-2029 | Under the carve-out (G), the democracy act alone; the ethics, courts and civil service bills need 60 votes (part 1.1) |
| The democracy act's date | Enacted by spring 2030 at the latest | Not law before the 2031 census data | Divisions B and C miss the 2031 maps; the ban applies from enactment (section 5, part 4) |
| Registration by state, each federal election | Rising toward Australia's and Canada's levels where registration from records is in force | Flat in a state after 2032 | The Attorney General's suit after notice (DEM-1.13, provisional); the EAC's survey |
| Citizenship flags | Few, cleared by a person | Many eligible voters flagged | Fix the records match before any removal; the flag never removes |
| Mail ballots rejected | Below 2024's 584,463 [EV-DEM-018] | No fall once cure is in force | Audit the notice times |
| Maps' partisan bias | Lower than the 2021 cycle [EV-DEM-261] | No change, or challenges unresolved by the filing deadline | The three-judge fast track's schedule |
| The FEC's complaints | Acted on within 120 days | Citizen suits become the main route | The quorum and the staff line |
| Matched cycles | Participation across both parties and many states | Few candidates opt in, or payments far above the scaling | The ceiling's formula; the FEC's report |
| Judgeships filled | Each tranche confirmed in its term | Vacancies pile up | Weighted filings and vacancy months [EV-DEM-238] |
| The immigration court's screens | Done within the two-year interim | Interim appointments expire unscreened | Circuits add panels; the Administrative Office's transition office |
| The immigration backlog | Clearing by about FY2035 | Hires below 150 a year (clears FY2037 or later) | More judges, not a cap |
| **Agency hiring against paths** | Near the working pace, about 13,500 net a year across the six agencies | Below 75% of a path at mid-year, or net losses | The tranche waits; the delivery unit's corrective plan; the contingency against a written need |
| The flagships' dated needs | Met on their dates (section 5, part 3.1) | A date missed | The program's own rule (provisional fix 1) |
| Time to hire | Toward OPM's 80-day goal [EV-DEM-348] | Well above it in delivery jobs | Pooled announcements; direct hire |
| Improper payments | Falling with records-first eligibility | Rising, or wrongful denials from matches | Sampling rules; a match is never a denial (CAP-19.04) |
| Payments in a lapse | Uninterrupted | Any benefit payment stopped | EXE-18's per-program clause |
| LSC grantees' hiring | On the steps' path | Steps unreleased for lack of hires | Hold the step; providers' plans |
| Contingency releases | Few, each with a published need | Releases without a need, or money unspent while a dated need is missed | GAO's audit; stage G's review of both contingencies |

## 8. Every provision, checked

All 137 provisions in `provisions.json` fall in one of the groups below. Each group is tested by a model run, an outside benchmark or the register's evidence, and answered in part 6 where an objection bites.

| Provisions | Tested by | Result | Objections | Input type (part 9) |
| --- | --- | --- | --- | --- |
| **The voting floor:** DEM-1F.01, DEM-1.01 to 1.15, DEM-11.01, 11.02, 11.03, DEM-12.01, DEM-13.01, DEM-1.20, 1.21 | Vote model (1.1); CBO's 2019 and 2022 scores; the advocates' and EAC's election-funding figures; Australia's and Canada's registers; the turnout studies (part 2) | Federal cost near zero beyond DEM-11, as CBO found; DEM-11 at two-fifths of the advocates' need; passes in 72% under F, 91% under G | 6.1, 6.3, 6.8 | The rules: commitments. DEM-11's size and split: working assumption. The effective dates and DEM-1.13's enforcement: provisional |
| **The Voting Rights titles:** DEM-1.16 to 1.19 | *Callais*, *Shelby County*, *Brnovich*; the preclearance turnout study | No survival claimed for III-A; III-B and II stand alone | 6.2 | Commitments; litigation risk an open question |
| **Redistricting and the state option:** DEM-2.01 to 2.06, DEM-4.01 | The commission evidence [EV-DEM-259] [EV-DEM-260] [EV-DEM-261]; the Elections Clause cases | Commissions with final power drew less biased maps; the evidence is mixed on competitiveness | 6.1 | Commitments; DEM-4.01's uptake a study in implementation |
| **Long-run representation:** DEM-3.01, DEM-4.02, DEM-9.01, DEM-8.01, DEM-8.02 | The cube-root yardstick, contested [EV-DEM-249] [EV-DEM-250]; the compact's consent question [EV-DEM-266] | Decisions set for 2031 and 2033 on evidence still to come; the chamber build unpriced | — | Directions; the build an open question until the Architect's report |
| **Statehood and state tracks:** DEM-5.01, DEM-6.01, DEM-7.01, DEM-10.01, DEM-19.01, DEM-20.01 | Vote model: DEM-5 26%, DEM-6 62% under F | No cost in the window; Puerto Rico's fiscal effect scored before the vote | — | Commitments |
| **Civic life:** DEM-16.01, DEM-17.01, DEM-17.02, DEM-18.01 | IMLS's base [EV-DEM-338]; the assemblies' implementation record [EV-DEM-181]; DEM-17 survives R3 in 96% | The library line is 2.8-5.6 times today's, unbooked | — | Working assumptions on Espen's direction |
| **Money in politics:** INT-5.01, INT-2.01, INT-8.01, INT-16.01, INT-6.01, INT-7.01, INT-15.01 | CBO's H.R. 1 match; *Buckley*, *Arizona Free Enterprise*, *Citizens United*, *Bonta*, *Cruz*, *NRSC*; the FEC deadlock record | The match about $6 billion (note 1 closed); each rule written to the current case law, the riskiest severable | 6.4 | Rules: commitments. The match's cost: working assumption, studied in implementation |
| **The stock ban:** INT-1.01 to 1.06 | CBO's ETHICS Act score; vote model INT-1 55% under F | Near zero; revenue −$3 million | 6.4 | Commitments; the retirement-account element provisional |
| **The other ethics rules:** INT-3.01, INT-4.01, INT-9.01, INT-10.01, INT-11.01, INT-13.01, INT-14.01, 14.02, 14.03, INT-12.02, INT-17.01 | OGE's, FinCEN's and the FARA unit's staffing in the integrity line [EV-DEM-329]; the emoluments suits' dismissal [EV-DEM-039] | About zero beyond the integrity line | — | Commitments; thresholds working choices |
| **The immigration court:** CRT-5.01 to 5.10 | The immigration model (1.4); CRS's and the Manhattan Institute's judge counts; EOIR's and the AO's budgets; the public-rights and appointments cases [EV-DEM-365] to [EV-DEM-368]; CRS on Article I proposals [EV-DEM-369] | 1,673 judges clear the backlog by FY2035; about 1,250 to screen at the transfer; structure about $6.9 billion, unbooked, inside CRT-P1's room | 6.6 | Form and tenure: commitments. Corps size, structure cost and the effective date: working assumptions. Interim appointments: provisional |
| **Civil legal aid:** CRT-20.01 | LSC's appropriations and offices; New York's eviction right | About $4.6 billion, paced by hiring | 6.5 (left) | Working assumption; LSC's 2029 baseline an open question |
| **The judgeships:** CRT-1.01, CRT-13.01 | CBO's JUDGES Act score (note 2 closed); weighted filings | About $0.55 billion; bipartisan history the vote model misses | 6.5 | Commitments; tranche years working choices |
| **Court integrity:** CRT-2.01 to 2.03, INT-12.01, CRT-3.01, 3.02, CRT-4.01, CRT-6.01, CRT-7.01, 7.02, CRT-11.01, 11.02 | CBO's S. 359 score [EV-DEM-327]; the Commission's report; the Chief Justice's count of conflicts | A few million dollars a year | 6.5 | Commitments; deadlines working choices |
| **Supreme Court terms:** CRT-15.01 to 15.03 | The Commission's divided view; Marquette's 79% | About zero; CRT-15.02 the likeliest part to fall | 6.5 | Commitments; litigation risk an open question |
| **Drafting rules, the second Congress, norms and the state track:** CRT-8.01, CRT-10.01, CRT-9.01, CRT-10.02, CRT-17.01, CRT-18.01, CRT-19.01 | *Loper Bright*, *Corner Post*, *CASA* [EV-DEM-051] [EV-DEM-052] [EV-DEM-047]; CRS on *CASA* a year on [EV-DEM-246]; *Jarkesy* [EV-DEM-365] | About zero; drafting practice | 6.5 | Commitments |
| **The agency rebuild and its accountability:** CAP-7S.01, CAP-7.01, CAP-7S.02, CAP-7.02, CAP-11.01, CAP-7.03, 7.04, 7.05, CAP-12.01, CAP-13.01 | The budget model (1); the capacity funding model (1.2); the hiring-pace check (1.3); the legacy review's range; hiring and attrition data | Allocation fits inside the booking; the money path runs two years ahead of hiring; about $22 billion of the allocation reached later in the window at the working pace, none lost, beside the $29.7 billion contingency for stage G; CAP-7's vehicle an open question | 6.7 | Allocation and release rule: commitments. Pace: working assumption, studied in implementation. Fix 1 (CAP-7.02's start rule) and fix 4 (CAP-13.01's clock): provisional |
| **Shared rule 5:** CAP-19.01 to 19.06 | The improper-payment evidence [EV-DEM-291] [EV-DEM-292]; Jharkhand and Andhra Pradesh [EV-DEM-286] [EV-DEM-287]; the Medicaid unwinding's ex parte rates [EV-DEM-319] | No saving counted; verification cuts both ways, so a match is never a denial | 6.3 (privacy) | Commitments |
| **The civil service and lapses:** CAP-8.01, CAP-9.01, CAP-4.01 | The state at-will studies [EV-DEM-311] [EV-DEM-312] [EV-DEM-313]; CRS on CBO's scoring of automatic continuing resolutions [EV-DEM-315]; the 2025-26 lapses [EV-DEM-127] | About zero; MSPB's load a study in implementation | 6.7 | Commitments |
| **Congress's own capacity:** CAP-1.01, CAP-14.01, CAP-2.01, CAP-3.01, CAP-5.01, CAP-6.01, CAP-15.01, CAP-16.01, CAP-17.01, CAP-18.01 | Vote model CAP-8 73% under F; legacy estimates; the Law Revision Counsel's budget [EV-DEM-339] | About $30-50 billion with the civil service, at or a little above CAP-8's row; staffing counts not yet on one method | — | Working assumptions on legacy estimates; Evidence still needed |

(Count: 23, 4, 7, 5, 6, 4, 7, 6, 11, 10, 1, 2, 12, 3, 7, 10, 6, 3 and 10, which is 137.)

## 9. What each input is

| Input | Treatment (`DEC-2026-11-10-07`) |
| --- | --- |
| What each provision commits to (sections 4 and 5) | Commitment (decided) |
| The vote model's parameters and the Senate roster | Working assumption: the war game's estimates, read as relative odds; re-baselined after the November 3 election (the model's own page) |
| D2, the Senate rules path | Decided outside this dossier (legacy D2, graduated cloture); not reopened |
| The hiring pace, a quarter of each target a year (range a fifth to a third) | Working assumption (section 3, part G); OPM's quarterly time-to-hire series and agencies' net hiring answer it (study in implementation) |
| The pay share of CAP-7's lines (70%, range 60-100%) | Working assumption (judgment), used only in the pace check |
| The booked CAP-7 path's FY2030-32 ramp | Booked input, not changed here; reshaping the allocation's ramp is a booking step (part 10, question 4); the contingency's size is stage G's |
| CAP-7's vehicle (R1 or annual appropriations) | Open question, for the vehicle step and the Parliamentarian |
| The court's corps (1,673, range 863-2,403) and its hires (250 a year) | Working assumption (the immigration model); reset in 2033 from receipts (study in implementation) |
| The court's effective date, October 1, 2031 | Working assumption |
| Per-seat judgeship cost ($1.0-1.1 million a seat-year) | Working assumption on CBO's per-judge figures (note 2) |
| The match's cost ($4-8 billion, up to $12 billion) | Working assumption; the first two matched cycles answer it (study in implementation) |
| DEM-1's whole contents ($4-15 billion against the row's $0-40 billion) | Working assumption (note 1); a narrower range is a booking step |
| Turnout and registration effects | Not estimated; each study's effect is evidence for one rule. A state panel from 2030 (study in implementation) |
| The legal risks: III-A after *Callais*, CRT-15.02, INT-8.01, INT-15.01, CRT-5.10's public-rights class | Open questions; each part is severable, so the answer changes what survives, not today's choice |
| The two delivery contingencies | Open question, for stage G |
| Every figure section 6 lists in its part 10 | As section 6 records them |

## 10. Changes made here, and the questions for Espen

**Changes to sections 4 and 6 (no figure changes):**
- *Note 1:* section 6, part 2 now separates INT-5's own legacy high ($30 billion, the match) from DEM-1's ledger high ($40 billion, the whole act); section 4's INT-5.01 says the same.
- *Note 2:* section 6, parts 1.2 and 6, and section 4's CRT-1.01 now say the JUDGES Act's 66 seats are 63 permanent plus 3 temporary, and that the per-seat figures are for a new permanent judgeship.

**Questions for Espen.** Every earlier provisional item stays provisional, drafted on its recommendation under the overnight relay (Espen, November 18) and revised for Espen's answer. None is a cost question (section 6, part 7):
1. *Section 4:* new purchases of individual stocks inside a self-directed retirement account count under the stock ban; existing holdings and plan-managed accounts never. **Recommended: yes.**
2. *Section 5:* the four delivery fixes, each recommended yes: (a) CAP-7.02's start rule follows each program's statute, which **amends a sentence of decided memo 10 B** ("a program whose agency is behind starts later; it does not shrink"), so Espen would be revising their own choice; (b) unscreened sitting immigration judges continue up to two years at the transfer (CRT-5.03), which part 1.4's count of about 1,250 judges supports; (c) the voting floor is enforceable by the Attorney General and by voters after notice (DEM-1.13); (d) formula grants are paid within 60 days (DEM-11.01, CAP-13.01).
3. *Section 5:* the floor's effective dates: barrier-removing rules for any federal election 180 days after enactment, rules needing new systems by the 2032 general election. **Recommended: yes.**
4. **New, from this section (provisional):** at the booking step, lay part G's allocation inside CAP-7 on the hiring pace sections 3 and 5 assume: about $22 billion less over FY2030-39 (range $13-42 billion), no change in FY2040, with the IRS's enforcement yield (G8) lagged with it. It changes an adopted input's timing, so it is Espen's at booking (tier 3); it changes no commitment and no FY2040 figure. Memo 10's sustained contingency ($29.7 billion over FY2030-39, $4.7 billion in FY2040) is left as booked: whether it stays is stage G's question, with the October 26 allowance (section 6, part 1.3). **Recommended: yes.** *The alternative:* keep the booked ramp, which shows FY2030-33 outlays and G8's early yield about two years early.

## Evidence still needed

- A time-to-hire and net-hiring series for each agency in part G (CAP-11.01 builds it; the register holds OPM's three occupations [EV-DEM-348] and the IRS's FY2024 gross hires [EV-DEM-370]).
- The Parliamentarian's view of a permanent CAP-7 in R1, and of CAP-11.01's hiring authority as a condition on the money.
- An independent (non-CRS) analysis of an immigration court outside the Justice Department, to corroborate EV-DEM-369.
- The NVRA's list-maintenance text (52 U.S.C. 20507), saved, for DEM-1.10's limits on removal.
- A county or state study of election costs per registered voter (DEM-11).
- A per-title objection rate for the democracy act in `votes-bills.csv`, and separate rows for the judgeships act and the other court bills (model inputs, tier 3).
- An estimate of the immigration court's structure from the judiciary or CBO (CRT-5.09).
- FEC data on small gifts by the donor's state (INT-5.01).
- LSC's current grantee and attorney counts (CRT-20.01).
- Congressional staffing in 1979 and today, on one method (CAP-1.01, CAP-3.01).
