# Fair pay and real power at work: validation

Role: section 7 of the work dossier (flagship 5). It covers the model runs behind sections 4-6, how they compare with outside estimates, and what the models miss. It also covers how the decided set lands with the rest of the plan, whom it reaches, the outcomes it moves, the strongest objections from the left, the right and practitioners, and the signs of failure. Status: **draft** (stage F), on `DEC-2026-11-17-01` to `-36`, `-95` and `-96`. It covers all 84 provisions in `provisions.json` (sections 4 and 5) and section 6's prices: about +$0.20 trillion over FY2030-39 and +$27.4 billion in FY2040 on the general fund (firm lines). Items still with Espen are tested on their recommendations and stay **provisional** (part 8). **Nothing is booked here.**

Figures marked "project arithmetic" come from three runs:
- `tools/work_path.py`, section 6's path;
- `tools/floor_household.py`, new here: the household model's typical families (`models/tools/household/families.py`) run at the wage floor's steps;
- the budget model run on section 6's booking rows in a scratch copy (part 1C), with nothing written to `models/`.

Outcomes it serves (`charter/outcomes.md`): OUT-06, its own; OUT-08; OUT-10; and OUT-01, OUT-02 and OUT-11, through the point where the wage floor meets income support (part 5).

## 1. Model runs and benchmarks

### 1A. The cost lines against outside scores

Section 6, part 6 checks each line against a published score. That check is summarized here with this section's reading. None of the outside figures scores this design: point 15 (`DEC-2026-11-17-28`) asks CBO and JCT for those in 2027-28.

| Line | This dossier (general fund) | Outside figure | Reading |
| --- | --- | --- | --- |
| The floor's indirect effect (LAB-4.01-4.03) | About $32 billion over FY2030-39, $5.5 billion in FY2040; range zero to $80 billion | CBO, 2021: +$54 billion over 2021-31 for $15 by 2025 [EV-WRK-032] | **Holds as scaled.** CBO's floor bit at about 61% of 2025's median; memo 1 B's $17 is about half the median in 2035 [EV-WRK-078]. The sign of a smaller bite's effect is not tested, so the range reaches zero |
| Who gains and who pays for the floor (distribution) | Not in the budget model's D3 rows (part 2) | CBO, 2019, for $15 by 2025, at its median job loss: real income up $7.7 billion (5.2%) for families below the poverty line and $14.2 billion (3.5%) at one to three times it; down $2.2 billion at three to six times and $28.4 billion (0.3%) above six times, mostly business income; −$8.8 billion in all, in 2018 dollars [EV-WRK-450] | **Supports the D3 pattern.** The gains fall below three times poverty and the losses at the top. CBO counts income before tax and transfers, so part 1B's household test and Dube's 66% [EV-WRK-066] show what is left after benefits phase out |
| Organizing, the board and penalties (LAB-1, 2) | About zero; penalties a small gain | CBO, 2023: $4 million to run S. 567 [EV-WRK-189]; CBO, 2019: +$39 million of penalties over ten years [EV-WRK-176] | **Holds** |
| The small-business credit (LAB-5.01) | About $2.9 billion | JCT, 2007: the package passed with the 2007 raise lost $4.8 billion over 2007-17 [EV-WRK-445] | **Supports the bottom-up size**, far below memo 1's $0.02-0.04 trillion (provisional, part 8) |
| Extended Benefits, ordinary years (LAB-11.04) | About $31 billion over FY2031-39 | OMB, FY2017 budget (Obama administration, its own proposal): $36.7 billion over 2017-26 [EV-WRK-438] | **The anchor**, with a wide range ($10-61 billion), because the triggers differ. OMB's figure is one publisher's analysis until corroborated |
| UI administration and the systems grant (LAB-11.06, 11.08, 11.09) | About $10 billion | OMB, FY2017: $14.1 billion to modernize [EV-WRK-438]; the 2021 rescue act's $2 billion [EV-WRK-434]; the 2009 act's $7 billion of incentives [EV-WRK-433] | **Same order** |
| The wage base and solvency (LAB-11.05) | Trust funds matched over the cycle | CBO, 2018: a $40,000 indexed base raises $18 billion over 2019-28 [EV-WRK-435]; OMB, FY2017: solvency receipts of $46.3 billion [EV-WRK-439] | **Qualifies the presentation.** A score will show a net gain while states rebuild reserves (section 6, part 6) |
| Wage insurance (LAB-18) | About $20 billion over FY2031-39; $3.0 billion in FY2040 | OMB, FY2017: $11.2 billion over 2017-26 at half LAB-18's cap [EV-WRK-437]; Kletzer and Litan, about $3-3.5 billion a year in 1999 dollars [EV-WRK-443]; Jacobson, LaLonde and Sullivan, about $15 billion a year for a broader design [EV-WRK-444] | **Holds**, at the low end. The take-up assumption moves it most (part 6, "wage insurance") |
| Apprenticeship (LAB-8) | About $34 billion | CBO, 2020: $3.1 billion over five years for the 2020 bill's authorizations [EV-WRK-396] | **Larger by design**, paid per apprentice |
| National service (LAB-9) | About $49 billion civic; $60 billion with the tranche | Legacy LAB-9B: about $0.05 trillion for 150,000 [EV-WRK-709]; the Serve America Act's unfunded plan [EV-WRK-446] [EV-WRK-447] | **Holds** against the legacy figure |

**What no outside figure tests:** the credit's design, the UI standards in the 2025 bill (S. 2312 has no score), the tax offset on employers' UI taxes, the standards boards, the standby trigger and card check's effect on how many workers win a union. Section 6's ranges are bounds, not probability intervals (`6-cost.md`, "Counting rules").

### 1B. The household test: how much of the floor's raise a family keeps

Sections 1 and 2 left one question for the household model: how much of a raise a family keeps once taxes and benefits respond (`1-problem.md`, A.6; `2-what-works.md`, A.4). `tools/floor_household.py` answers it for the three families of the 65-cent check (INC-5.02). It uses the household model's own calculator at 2029 law and with every plan layer: FAM-1's child benefit, INC-1.01, INC-2 with INC-2.02's 45% earnings deduction, paid leave's worker share and, in 2030-34, the premium credit. Dollars are 2029 dollars. The floor's $17.00 in 2035 is about **$14.87** in 2029 dollars on the model's price path, and without the act the federal $7.25 is worth about **$6.34** by 2035. Hours are held fixed: job loss is part 6's question. The table gives the raise in net resources a year, and in brackets the share of the gross raise the family keeps.

| Family | Starting wage | Hours | Gross raise | 2029 law | 2029 law, with the rent | The plan, 2035 on | The plan, with the rent |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Single parent, two children | The federal $7.25 | Full time | $17,736 | $15,569 (88%) | $15,492 (87%) | $14,347 (81%) | $15,821 (89%) |
| | | Half time | $8,868 | $10,939 (123%) | $13,007 (147%) | $10,247 (116%) | $11,710 (132%) |
| | $12.00 in an indexing state | Full time | $5,965 | $3,189 (53%) | $2,627 (44%) | $2,885 (48%) | $2,885 (48%) |
| Married couple, two children, one earner | The federal $7.25 | Full time | $17,736 | $16,688 (94%) | $16,612 (94%) | $15,968 (90%) | $17,443 (98%) |
| | $12.00 in an indexing state | Full time | $5,965 | $4,308 (72%) | $3,746 (63%) | $4,506 (76%) | $4,506 (76%) |
| Single adult | The federal $7.25 | Full time | $17,736 | $12,881 (73%) | $10,529 (59%) | $10,513 (59%) | $9,151 (52%) |
| | | Half time | $8,868 | $5,977 (67%) | $8,045 (91%) | $7,515 (85%) | $8,979 (101%) |
| | $12.00 in an indexing state | Full time | $5,965 | $4,900 (82%) | $4,900 (82%) | $4,511 (76%) | $4,511 (76%) |

"With the rent" adds a $1,400 monthly rent (2025 dollars) to SNAP's shelter deduction, as the ceiling check does. The script prints the remaining rows (half time from $12.00) and each layer's part.

**What it shows.**
- **Families with children at the bottom keep most of the raise.** A full-time parent moving from $7.25 to the floor keeps 81-98% of it under the plan. A half-time parent keeps more than the raise (116-132%), because the earned income credit's phase-in still adds to earnings at those incomes. Dube's estimate that net income gains are about 66% of gross [EV-WRK-066] is an average across all affected families, and it sits between these rows and the $12.00 rows.
- **Workers already above $7.25 keep about half to three quarters.** A worker at $12.00 who rises to the floor keeps 48-76%, because the earned income credit and SNAP phase out over that range. That is below the 65-cent ceiling's marginal test for small raises (INC-5.02), but it is the range where a raise buys least.
- **The plan pays more at every wage, so a raise adds a little less on top.** The single parent at $7.25 full time has about $34,960 of net resources under the plan before the floor, against $26,910 at 2029 law. With the floor that rises to $49,310 against $42,475. In both cases the family is far better off with the floor than without it. FAM-1's child benefit does not phase in with earnings, as the 2029 child credit does, so the raise no longer "earns" a credit. That is why the plan's share is lower in the first row. It is not a loss.
- **The one weak case is the single adult in 2030-34.** On the marketplace in a state that has not expanded Medicaid, a full-time single adult moving from $7.25 to the third step ($12.50 in 2032) keeps about **39% under the plan, against 59% at 2029 law**. INC-1.01's larger childless credit and INC-2.02's SNAP deduction phase out over the same range, and the premium credit starts at 100% of poverty. About 9 points of that is a premium for coverage the worker does not have below the line, since the calculator gives the plan's coverage-gap fix (HLT-1) no value. So the share kept is understated, but not by enough to close the gap. From 2035 the single plan removes the premium, and the single adult keeps 52-59% at full time. This is a phase-out finding for the secure floor's rule 2 owners and stage G (part 3), not a reason to change the floor.
- **At no wage is a family worse off under the plan than at 2029 law,** except by paid leave's worker share (about $90 a year for the single adult at the floor), which buys twelve weeks of leave.
- **Poverty.** A single parent working full time at $7.25 has net cash resources of about 91% of the 2029 poverty guideline at 2029 law. With the floor and the plan's layers that becomes about 167%, before child care and health care, which the plan also provides (the guideline is a reference line, not the SPM threshold).
- **If the job is lost.** With no earnings, the single parent's net resources are about $18,910 under the plan (64% of the guideline), against $10,200 at 2029 law (35%), before unemployment insurance. The child benefit does not depend on work. For the single adult the plan adds nothing at zero earnings (22% of the guideline, SNAP only), so unemployment insurance (LAB-11) is the floor that matters.

**What the test does not measure:** job or hours loss (part 6), the floor's price effects (part 6, "jobs"), a second earner, state taxes, the cliffs the calculator lists apart (adult Medicaid at 138% of poverty at 2029 law, which the single plan ends from 2035), and the real distribution of who earns what. The household model's extract keeps no hours, so it cannot yet put the floor on real CPS workers (part 2).

### 1C. The budget model run on section 6's booking rows

Section 6, part 9 lists the rows a booking would change. They were run through the whole model chain (`models/tools/run-all.sh --write`) in a throwaway copy of the repository, which was then discarded; nothing in `models/` is changed by this PR. The run changed four rows: LAB-1 carries the floor's indirect effect; LAB-5 is set to the credit; LAB-8 and LAB-9 (civic positions only, without the tranche) are set to section 6's lines. It added eight rows for the other firm lines (the 14(c) grant, boards and commission, outreach, LAB-11's general-fund spending and tax offset, LAB-18's spending and income tax, penalties). Each row was given section 6's central FY2030-39 path. Plan-wide general-fund primary balance, case `mixed`, a shortfall positive:

| | Main today | With the booking rows | Change | Section 6's arithmetic |
| --- | --- | --- | --- | --- |
| FY2040 | $602.7 billion | $609.7 billion | **+$7.0 billion** | +$6.8 billion |
| FY2030-39 | $3,773.4 billion | $3,719.4 billion | **−$54.0 billion** | −$54.8 billion |

- **The model confirms section 6's report** within $0.2 billion in FY2040 and $0.8 billion over the decade. The work rows come to $27.6 billion in FY2040 in the model, against section 6's $27.4 billion. The difference has two causes. The ledger keeps three decimals in $ trillion, so each row rounds to the nearest $1 billion over the decade (outreach $0.56 to $1.0 billion; penalties −$0.45 billion to zero). And the model grows each row from its 2039 level with GDP, where section 6 builds FY2040 line by line.
- **D3 moves down a little, for a reason that is the model's, not the policy's.** On the decided scenario (Q-H7, model keys) every quintile below the top stays ahead. Q1 goes from +$14,691 to +$14,632 a household a year and Q4 from +$8,130 to +$8,096 (FY2030-39 average). The fall comes from LAB-9's incidence row, which shrinks with the smaller service line. The new rows (unemployment and wage insurance, the floor) have no incidence rows, so D3 counts none of their benefits. A booking should add them (part 2), or D3 will understate what work gives the lower quintiles.
- **What the run needs at booking** (tier 3, after the milestone review):
  - provision specs for the new rows: the budget model's provision test fails without them, as it should;
  - the rails (R1, point 16), which the run did not set;
  - the penalties row on a revenue line, not a rounded spending row;
  - incidence rows for LAB-11 and LAB-18 with measured keys.

### 1D. The path's own checks

- `work_path.py --check`: all 84 provisions match `provisions.json`. Each is on one of 24 lines or listed with its reason for having none (34). Every central value lies inside its range.
- `floor_household.py` calls the household model's calculator unchanged and adds no rule of its own. The same calculator reproduces the model's published baseline (`models/tools/household/results.md`, section 4): at 100-125% of poverty, at 2029 law, the single parent loses 52.7 cents of each added dollar without the shelter deduction.
- The fiscal-rule report (section 6, part 8): +$27.4 billion in FY2040 is 0.051% of GDP and 4.5% of the $602.7 billion gap. A booking adds about $6.8 billion, because it replaces $20.6 billion of booked work rows.

## 2. What the models miss

| Missing | Direction | Size or note | What would answer it |
| --- | --- | --- | --- |
| **Who earns what, by hour, in the household model** | Distribution only | The extract (`models/data/household/`) has annual earnings but no hours, so it cannot put the floor on real workers by quintile. D3 carries no row for the floor; CBO's 2019 table is the stand-in [EV-WRK-450] | Add usual hours and weeks worked (`HRSWK`, `WKSWORK`, already read by `extract.py` for SNAP's work rule) to the extract, then a rule for the floor's steps. A model change for `MOD-household`, not this dossier |
| **Incidence rows for the new lines** | D3 understates work's benefits | Only LAB-8 and LAB-9 have incidence rows (`incidence-rows.csv`). In part 1C's run, D3's lower quintiles fall by about $35-60 a household a year because LAB-9 shrinks, while UI, wage insurance and the floor add nothing | Incidence rows for LAB-11 and LAB-18 at booking, on keys the household model measures (UI recipients, displaced workers' earnings) |
| Job and hours loss | Lower gains, higher income support | CBO: about 0.9% of employment at $15 [EV-WRK-032]; studies at or below 60% of the median find little [EV-WRK-050] [EV-WRK-033]. The floor's indirect effect ($5.5 billion in FY2040) nets CBO's pattern, scaled | CBO's score of memo 1 B (point 15); the commission's county reports (LAB-4.04) |
| The floor's bite by county | Larger effects where wages are low | $17 in 2035 is about half the national median, but far more in the lowest-wage counties; the register has no county measure (`2-what-works.md`, A.1) | The commission's first task, within 18 months (LAB-4.04) |
| The floor's indirect effect | Either sign | Scaled from CBO's 2021 $15 score; a smaller bite's sign is not tested. It overlaps the legacy dynamic row DY4 (−$0.07 trillion, never in a total) [EV-WRK-707], so a booking uses one or the other (`6-cost.md`, part 9, step 5) | CBO's score (point 15) |
| States raising their own floors before 2029 | Lower federal bite, smaller credit | 30 states and DC were above $7.25 in 2024 [EV-WRK-021]; several index [EV-WRK-017]. The path holds the 20 states at $7.25 | The Labor Department's table in 2029 |
| Unemployment insurance behavior | Slightly higher trust-fund cost | Benefits lengthen claims (U.S. elasticity 0.38) [EV-WRK-368]. The pandemic's supplements barely slowed job finding [EV-WRK-370] [EV-WRK-371]. The 40-60% benefit rise is memo 7's judgment, not a model | The claims states already report; studied in implementation |
| The UI trust funds and Social Security's offset | Outside the general fund | About +$259 billion of benefits matched by employers' state taxes; about −$21 billion to Social Security (`6-cost.md`, part 2). The budget model's funds engine carries no state UI accounts | The funds model at stage G |
| A recession | Higher cost | Extended Benefits in a moderate two-year downturn: about $70-100 billion, contingent; zero in the projection | — (reported, not booked) |
| Wage insurance's take-up and new hires' wages | Cost and incidence | 60% take-up is judgment, against TAA's 11% [EV-WRK-332]. Whether employers offer displaced workers lower wages because the subsidy tops them up has no study in the register | The first two years' state counts (section 5, part 8) |
| Card check's effect on unionization and wages | Distribution, revenue | British Columbia's 19-point swing in certification success [EV-WRK-168] is the closest test. No model turns it into bargaining coverage or pay | The Board's yearly counts |
| The standards boards' standards | Distribution | No U.S. board has been evaluated (`3-design.md`, "Evidence still needed"). The cost line counts their offices, not their wage effects | The first board's standard (LAB-3.02) |
| Coverage-gap adults in 2030-34 | Overstates the single adult's loss | `families.py` gives HLT-1's coverage-gap fix no value (part 1B) | A coverage layer in the typical-family calculator |
| AI displacement | Cost of the trigger | No broad displacement yet [EV-WRK-358]; entry-level effects disputed [EV-WRK-355] [EV-WRK-361]. The trigger (provisional) is $0 to $5 billion a year | LAB-19.03's yearly report, if Espen chooses memo 10 C |
| Interest and economic feedback | Higher deficit before financing | Like every dossier's figure: the primary balance, no feedback | The budget model, once booked |
| Employers' compliance costs | Outside the budget | The heat standard's analysis: $7.8 billion a year of costs against $9.18 billion of benefits (Biden administration) [EV-WRK-255] | — |

## 3. How it lands with the rest of the plan

- **Secure floor.** Rule 2 (phase-outs) is the secure floor's. Part 1B is the first measurement of how the floor meets it. Families with children keep most of the raise, and the plan never leaves a family worse off than 2029 law. The single adult in 2030-34 keeps about 39% of a raise from $7.25 to $12.50 on the marketplace, so INC-1.01's and INC-2.02's phase-outs overlap there. That is a finding for the secure floor's owners and the household model's yearly report (INC-5.02), not a ceiling breach: the ceiling is a marginal test, and this is an average over a large raise. LAB-10's participation support and LAB-11.07's attestation are one rule (shared rule 6, work's).
- **Care.** Home care's wages run through the payer (LAB-3.03 with HLT-10.04), and its overtime coverage is LAB-12.01. The care training line pays once (LAB-8.07 with HLT-10.06). The single plan (HLT-7) ends Medicaid's cliff for workers whose raise crosses 138% of poverty, from 2035.
- **Clean power.** The transition guarantee comes first for its workers (LAB-18.07). Higher UI benefits lower the guarantee's top-up, since benefits count toward its 90% (`3-design.md`, seams).
- **Immigration.** Retaliation by immigration threat is retaliation (LAB-7.06), with immigration's deferred action and firewall (IMM-4.17, 4.11). This is the labor-standards half of the E-Verify mandate (`DEC-2026-11-12-07`).
- **Democratic renewal.** CAP-7 carries the agencies' staff (`6-cost.md`, part 3). The NLRB fits inside the legacy row; FMCS, OSHA's high end, apprenticeship registration and the FLRA are claims on the delivery contingency (`dossiers/foundations/democratic-renewal/5-delivery.md`).
- **The AI topic.** AI-4's booked row ($200 billion over FY2030-39, $29.5 billion in FY2040) overlaps LAB-18 and, if Espen chooses memo 10 C, LAB-19. Re-scoping AI-4 would lower the plan-wide figure by its wage-insurance part, up to about $3 billion in FY2040 (`6-cost.md`, part 8).
- **Financing (OUT-11).** Work's whole firm general-fund cost is about 4.5% of the plan-wide FY2040 gap. A booking adds about $6.8 billion in FY2040 and lowers the decade by about $55 billion; the budget model's own run gives +$7.0 billion and −$54.0 billion (part 1C). The floor itself puts its cost mostly on employers and consumers, not the general fund. CBO's 2019 table puts the net losses on families above three times poverty [EV-WRK-450], which is the direction D3 asks for.

## 4. Reach: for whom

| Group | What they get | When |
| --- | --- | --- |
| Workers paid under $17 | The floor's steps; $17 by January 1, 2035 (LAB-4.01), then indexed to the median (LAB-4.02). Oxfam's modeled estimate is over 39 million workers under $17 in 2024 [EV-WRK-028], not checked against a government count | January 1, 2030, then each January |
| Tipped workers and workers under 20 | The full floor in seven steps (LAB-4.07); the youth wage ends with the first step (LAB-4.06) | 2030-36; 2030 |
| 35,534 workers under 14(c) certificates [EV-WRK-008] | The floor over five years, a funded move into supported jobs and no loss of day services (LAB-4.08, 4.09) | 2030-34 |
| Workers who want a union: 5.9% of the private sector have one [EV-WRK-101] | Card check, fast elections, first-contract arbitration, penalties in federal court and a private right of action (LAB-1, 2) | The labor act, 2029 |
| Fast-food workers, then other industries | Standards set by a board within 18 months (LAB-3.02), more boards on petition | From about 2031 |
| Workers whose pay is taken | Twice as many investigators by FY2034, treble damages, class actions and no forced arbitration (LAB-7) | Hiring from FY2030 |
| Outdoor and warehouse workers | A heat standard in statute with interim minimums (LAB-6) | January 2029 (rule) and the act |
| Unemployed workers: 27-29% receive UI today [EV-SEC-045] [EV-SEC-046] | Federal standards: 26 weeks, 75% of high-quarter earnings up to two-thirds of the state's average wage, part-time workers and the latest quarter counted, the ABC test (LAB-11) | Benefit weeks from January 1, 2031 |
| Long-tenured displaced workers: about 1.1 million a year [EV-WRK-315] | Wage insurance: half the hourly drop for two years, up to $10,000 a year (LAB-18) | Separations from January 1, 2031 |
| New and would-be apprentices | Starts from 311,035 [EV-WRK-349] to 600,000 a year by 2034, with supports (LAB-8) | FY2030-34 |
| People who want to serve | 150,000 more full-time civic positions by 2034, up to 50,000 more on the gate (LAB-9) | FY2030-34 |
| Large retail, food and warehouse workers | Schedules posted 14 days ahead (LAB-15.01) | The labor act |
| Federal workers | Bargaining restored (LAB-16.01) | The labor act |

**Who is not reached, and why.**
- *Farmworkers and domestic workers* keep the labor act's exclusions and the farm overtime exemptions. The floor, the heat standard and the right to discuss pay reach them (`4-specification.md`, "Where particular groups fall"). This is a gap for later work, not a decision.
- *Young entrants and short-tenure workers* have no three-year job to lose, so wage insurance misses them. Memo 10's trigger (provisional) would lower the tenure test to one year in a displacement period (LAB-19.05).
- *Workers in states that do not conform to LAB-11 by 2031* reach the federal standard only through LAB-11.10's remedy, which needs two new authorities (provisional fix, part 8).
- *Contract workers who pass the ABC test* stay outside UI and the labor act (LAB-1.07, 11.02).
- *American Samoa's workers* stay on their own path under the recommendation (LAB-4.10, provisional).
- *Workers whose jobs the floor costs.* If CBO's pattern holds, some lose work (part 6). The single parent keeps the child benefit (part 1B); the single adult relies on UI.

**Illustrative households** (2029 dollars; project arithmetic, `floor_household.py`):
- *A single mother of two at $7.25, full time, in Texas:* gross pay rises from about $13,190 to $30,925 by 2035. Under the plan she keeps about $14,350 a year more, and her net resources reach about 167% of the guideline.
- *A warehouse worker at $12.00 in an indexing state, single:* the floor adds about $5,965 a year gross, and he keeps about $4,510.
- *A machinist laid off at $32 who takes a $24 job:* $4 for every hour worked, up to $10,000 a year for two years (LAB-18.02).

## 5. The outcomes it moves

| Outcome | What the dossier changes | Measure to watch (`charter/outcomes.md`) | What the evidence says |
| --- | --- | --- | --- |
| **OUT-06**, fair pay and real power at work | The floor to $17 and indexed; card check, penalties and first contracts; standards boards; twice the investigators; pay ranges; home care and overtime coverage | Earnings at the low end; bargaining coverage; wage theft recoveries (FY2025: $259 million [EV-WRK-200]) | Floors up to about 60% of the median raise pay with small job effects [EV-WRK-050]. Card check raised certification success [EV-WRK-168]. Randomized inspections cut injuries with no job loss [EV-WRK-249] |
| **OUT-08**, time and practical freedom | Predictable schedules (LAB-15.01); the heat standard; 90 days' notice of layoffs (LAB-13.01) | Schedule predictability; time use (ATUS) | Fair Workweek laws raised two weeks' notice 13 points with no fall in hours [EV-WRK-409] |
| **OUT-10**, connection | 150,000 more service positions by 2034, mixing reported (LAB-9) | Participation in national service | Members' civic engagement rose in AmeriCorps' early study [EV-WRK-391] |
| **OUT-01**, child poverty | The floor meets the child benefit: a full-time single parent at $7.25 goes from about 91% to 167% of the guideline (part 1B) | Child SPM poverty | CBO: 0.9-1.3 million fewer people in poverty at $15 [EV-WRK-032] [EV-WRK-029]; Dube's poverty elasticity −0.22 to −0.46 [EV-WRK-066] |
| **OUT-02**, planning beyond the next paycheck | UI that reaches more people for 26 weeks; wage insurance; notice; Extended Benefits automatic | Income volatility; ability to cover an emergency (SHED) | Spending falls 12% when benefits run out, and longer benefits protect it most [EV-WRK-372] |
| **OUT-11**, the fairness and fiscal tests | D3: the floor's gains go below three times poverty and its costs to the top [EV-WRK-450]. D4-B: about $27 billion a year permanent from FY2040, reported to the settlement | The D3 report; the fiscal-rule report | The floor has no D3 row yet (part 2). Every other row is on section 6's basis |

A good trend in these measures will not show that the dossier caused it (`charter/outcomes.md`). The signs of failure (part 7) name the counts that would show it is not working.

## 6. Objections answered

**From the right**

**"A $17 floor will cost jobs."** It may cost some. CBO put $15 by 2025, a floor at about 61% of that year's median, at 1.3-1.4 million fewer jobs (median; a two-thirds range from about zero to 3.7 million) [EV-WRK-029] [EV-WRK-032]. At $12 it found 0.3 million [EV-WRK-030]. Memo 1 B's $17 comes in 2035, when it is about half the median. That is below CBO's $15 in bite and inside the range where reviews find small effects: up to about 59% of the median in state studies and 81% in county studies [EV-WRK-050] [EV-WRK-051]; 138 state increases left low-wage job counts unchanged [EV-WRK-033]. The other view is real: most estimates in one broad review are negative [EV-WRK-034], and the 2007-09 federal steps cut low-skilled employment in a recession [EV-WRK-064]. The design answers that last finding with a recession pause (LAB-4.03), the commission's county reports (LAB-4.04) and five annual steps, not one jump. If a job is lost, the plan's child benefit and UI are there (part 1B). CBO's score of memo 1 B (point 15) is the test.

**"It will crush small business."** The floor is one national schedule, with no size tiers or county schedules to track (design lens). Employers under 50 workers get a temporary credit for the first three steps, about $3 billion (LAB-5.01; its size is provisional, for Espen). No evaluation shows that a phase-in or credit softens job effects (`2-what-works.md`, A.3), so the credit is a cushion, not a remedy. The cost mostly passes into prices, about 0.36% on groceries for a 10% raise [EV-WRK-065]. Small firms in states that already pay more face no new step until the floor passes their own. Two-thirds of workers at or below $7.25 are in leisure and hospitality [EV-WRK-020], where every competitor faces the same floor.

**"Card check takes away the secret ballot."** A union may still choose an election, held within 20 days (LAB-1.02), and cards are checked against payroll within 14 days (LAB-1.01). Espen chose card check (memo 3 D). British Columbia's evidence is that mandatory votes cut certification success 19 points, and it rose back when card check returned [EV-WRK-168]. The answer to pressure on either side is LAB-1.03 (no captive-audience meetings) and the penalties, not a second vote.

**"Overriding right-to-work laws tramples the states."** Fair-share fees (LAB-1A.01) override the laws of 26 states [EV-WRK-141] in a separate, severable title, so the rest of the act stands if it is struck or dropped. Every study agrees that right-to-work lowers unionization [EV-WRK-165] [EV-WRK-166]. The wage effect is contested: a loss on one design, none on another, and a growth gain on a weaker design from an advocate of the laws [EV-WRK-187]. Members-only dues stay voluntary, and public-sector fees stay barred by *Janus*. This is the most contested provision politically (`2-what-works.md`, B.3), and Espen chose it knowing that (memo 4 A).

**"The floor bites hardest in right-to-work states."** It does. Nearly all of the 20 states where $7.25 is the working floor also have right-to-work laws (project count: the register gives the 26 states' number [EV-WRK-141], not their list; `1-problem.md`, A.2), and in their lowest-wage counties $17 is well above 60% of the median. The evidence there is thinner: one county study finds no loss up to 0.82 of the local median [EV-WRK-063]. The commission reports those counties first (LAB-4.04), the pause applies nationwide, and the credit reaches their small employers most.

**"Unemployment insurance keeps people out of work."** Higher benefits lengthen claims somewhat (U.S. elasticity 0.38) [EV-WRK-368]. In the one recent test at scale, the pandemic's large supplements had small effects on job finding against large effects on spending [EV-WRK-370]. When states ended them early, benefits fell $2,529 and earnings rose $292 [EV-WRK-371]. The design keeps "able and available" by attestation, with registration and an offered session (LAB-11.07, shared rule 6), and identity and wage checks against records the government holds (LAB-11.06), the lesson of pandemic fraud [EV-WRK-378].

**"National service is a costly boondoggle."** It costs about $49 billion over FY2030-39, about $6.7 billion a year at full scale. That is less than the $120 billion the budget model books today for a universal year [EV-WRK-705]. It is authorized first with bipartisan support, its second tranche opens only on a gate (LAB-9.03), and it may not displace paid workers (LAB-9.05). Its case is civic (OUT-10), not a labor-market claim (`2-what-works.md`, D.8).

**From the left**

**"$17 in 2035 is too little, too late."** Washington state is above $17 already, and the District of Columbia is at $18.40 [EV-WRK-015]. Higher state and city floors stand (29 U.S.C. 218). The federal schedule is Raise the Wage's [EV-WRK-042] and then follows the median, so it never erodes again, as the $7.25 has since 2009 [EV-WRK-002]. Two-thirds of the median, the legacy design and the United Kingdom's target [EV-WRK-053], goes beyond what U.S. evidence covers in low-wage places (memo 1). The commission may recommend more once its county reports show the reach (LAB-4.04).

**"Wage insurance subsidizes bad jobs."** It pays half the drop for two years to long-tenured workers who take a lower-paid job, up to $10,000 a year. TAA's version raised employment 8-17 points and paid for itself [EV-WRK-365]. It does not replace UI, which is larger and reaches more people (LAB-11). Rehiring by the same or a related employer does not count (LAB-18.04), so a firm cannot lay off and rehire at lower pay.

**"Without sectoral bargaining, this leaves most workers alone."** The standards boards bind by rule (LAB-3.01), and LAB-3.04 reports on sectoral bargaining in 2034, the direction Espen set (`DEC-2026-11-17-06`). Abroad, coordinated bargaining goes with higher employment and narrower pay gaps [EV-WRK-173]. New Zealand's repeal a year in [EV-WRK-175] is why the first step is a board with a deadline.

**On the law**

**"After *Slaughter* and *Jarkesy*, the labor board can't enforce any of this."** The act is built for that. Penalties are sought by the General Counsel in federal district court, where either side may demand a jury (LAB-2.01), which meets *Jarkesy*'s holding for civil penalties [EV-WRK-131]. The Board does not rely on protection from removal, which *Slaughter* and two circuits have undone in practice (LAB-2.04) [EV-WRK-136] [EV-WRK-134] [EV-WRK-137]. If it lacks a quorum for 90 days, workers take their cases to court and regional certifications stand without Board review. Workers and unions have a private right of action (LAB-2.02). What *Slaughter* leaves is that doctrine can change with each president. The statute writes the main rules (card check, first contracts, the ABC test) into law, so adjudication cannot undo them. Remaining exposure:
- three appeals courts set aside the board's broader damages awards [EV-WRK-132]; the act's remedies are statutory, not the board's own;
- *Cemex*'s bargaining orders are contested [EV-WRK-138]; LAB-1.04 puts them in the statute;
- first-contract arbitration and binding standards boards face challenges not yet tested in court. The register holds no case on either, so their legal footing is an open question for drafting, not settled.

**From practitioners**

**"State UI agencies can't change everything by 2031."** This is the largest delivery risk (`5-delivery.md`, part 2). In the pandemic, 17 of 50 states said their systems could not implement the CARES Act [EV-DEM-295]. The design gives:
- a one-time systems grant (LAB-11.09);
- a floor under administration funding (LAB-11.08);
- a cure period and a graduated remedy before any loss of certification (LAB-11.10, with section 6's provisional fix);
- an effective date a full legislative session after enactment.

If a state cannot change by 2031, its date slips under the remedy and the standard stays the same.

**"Unemployment insurance trust funds can't carry bigger benefits."** Only 18 states met the solvency standard at the start of 2026 [EV-WRK-304], and two owed $21.4 billion [EV-WRK-305]. Larger benefits are paid for by a larger wage base: from $7,000 [EV-WRK-310] to $25,000 by 2033, indexed (LAB-11.05). The federal tax per worker barely moves, from about $42 to about $50. States set their own rates on the larger base, so benefits and taxes match over the cycle (`6-cost.md`, part 2). CBO's 2018 option shows a larger indexed base raises state revenue mostly in the first years [EV-WRK-435]. The cost falls on employers, about $36 billion a year by FY2040. The general fund bears about a 5% income-tax offset, and Social Security about 8% (`6-cost.md`, part 2). A recession is the test: Extended Benefits, fully federal, carries the long claims (contingent, $70-100 billion in a moderate downturn).

**"Wage insurance's take-up will be low, or it will be gamed."** Both are possible.
- *Take-up.* TAA's documented route reached 11% [EV-WRK-332], and its evaluation found the program "challenging to implement at first" [EV-WRK-367]. LAB-18 offers it automatically on the UI claim form, and section 6 assumes 60%. At TAA's 11% the line would cost about a fifth as much. At full take-up it would be about two-thirds higher, near memo 8's $2-4 billion a year (project arithmetic on section 6's basis).
- *Gaming.* The rules guard against it. The separation test is the state's own finding (LAB-18.03). Rehiring by a related employer is excluded (LAB-18.04). Hours are checked against employers' reports and then wage records (LAB-18.06, 18.08). The cap is twice the median wage.
- *What is unknown.* Whether employers cut offers to displaced workers because the subsidy tops them up has no study in the register (part 2). The first two years' counts show take-up and starting wages (section 5, part 8).

**"Labor can't hire 1,200 investigators."** Wage and Hour needs about 120 net hires a year from FY2030, and a new investigator takes about two years to carry a full load (`5-delivery.md`, part 2). If hiring limits in 2029 slow it, the dates move, not the floors. The statutory staffing floor (LAB-7.01) and the private right of action (LAB-7.05) keep enforcement from resting on appropriations alone.

**On the future**

**"AI will make all this obsolete; or it means nothing yet."** The evidence supports neither. There is no broad displacement so far [EV-WRK-357] [EV-WRK-358], and in Denmark effects on earnings were precise zeros [EV-WRK-364]. Young workers in exposed occupations are 19% below trend in one payroll study [EV-WRK-355], against little sign in job postings [EV-WRK-361]. The design does not ask what caused a job loss (LAB-18.01), so wage insurance and UI reach AI-displaced workers on the same terms. Memo 10 C (provisional, for Espen) would measure displacement by occupation every year and switch on a capped expansion only when the data show it (LAB-19). It costs zero while off. A trigger of this kind has never been evaluated, and Extended Benefits' own macro effects are disputed [EV-WRK-374] [EV-WRK-375], so the cap ($5 billion a year) is the guard.

## 7. Signs of failure

Published counts with a review trigger, not gates (`DEC-2026-11-09-13`). The thresholds are working choices.

| Measure | Expected | A sign of failure | Response |
| --- | --- | --- | --- |
| Employment of teens and low-wage workers in the lowest-wage counties after each step (the commission's report) | No break from trend | A fall beyond the commission's published band for two quarters | The commission reports and may recommend a pause or a slower step (LAB-4.03, 4.04) |
| Share of a raise kept by the household model's typical families | Most for families with children | Any family type above 65 cents at the margin for two years | INC-5.02's review by the owning dossiers |
| Union certifications by card and by election; first contracts within a year | Rising | Certifications flat after two years | Look at unit disputes and the Board's 14-day checks |
| Board quorum and median case age (245 days in FY2025 [EV-WRK-115]) | Under 180 days | Above 180 days for a year | District-court route (LAB-2.04) |
| Wage and Hour investigators against the 1,200 floor | About 120 more a year | Below the path two years running | The statutory report to Congress (LAB-7.01) |
| UI recipiency (27-29% [EV-SEC-045] [EV-SEC-046]) and first payments within 21 days | Recipiency up by 2032; Labor's 87% standard | Recipiency unchanged, or a state below 70% timely [EV-WRK-427] | The conformity grant, then LAB-11.10's steps |
| States meeting the solvency standard (18 [EV-WRK-304]) | Most by 2035 | Fewer than half by 2035 | Review the wage-base schedule |
| UI improper payment rate | Falling with LAB-11.06's checks | Rising | Review the identity and wage checks |
| Wage insurance take-up among eligible workers | About 60% | Below 30% after two years | Fix the claim form's offer; look at employers' hour reports |
| Starting wages of wage insurance recipients against similar workers who are not | No gap | Lower | Study the offer effect before any extension |
| Apprenticeship starts and completions (42% complete within a year of the expected date [EV-WRK-350]) | 600,000 starts a year by 2034 | Starts flat, or completion falling | Supports and the worker-side pilot (LAB-8.03, 8.06) |
| Service positions filled and completing; the mixing report | 150,000 by 2034 | Unfilled positions | The tranche stays closed (LAB-9.03) |
| The displacement measure, if memo 10 C | No trigger | A displacement period | The capped expansion (LAB-19.05) |

## 8. What each figure is

Section 6, part 10 gives each cost input's treatment. Section 7 adds these:

| Input | Treatment (`DEC-2026-11-10-07`) |
| --- | --- |
| The floor's schedule, the pause, the credit's form, the UI standards, wage insurance's rules, the apprenticeship and service designs | Commitments (decided) |
| The household test's conventions: 2029 dollars, the model's price path to 2035, fixed hours, the three family types | Working assumptions, from the household model (`MODEL-CARD.md`, A-1 to A-10). The single-plan and coverage-gap layers are not valued in the calculator |
| The floor's distribution by income group | Working assumption on CBO's 2019 pattern [EV-WRK-450], until the household model holds hours (part 2) |
| Job loss at memo 1 B | Open: CBO's 2019 and 2021 pattern against the state and county studies. CBO's score (point 15) and the commission's reports answer it |
| Wage insurance's take-up (60%) and its effect on starting wages | Working assumption (take-up); studied in implementation (both), from the first two years' state counts |
| LAB-11.10's two authorities | **Provisional fix** (section 6, part 2), drafted into `provisions.json` and section 5 in place of the old clause; for the milestone review |
| First-contract arbitration's and binding standards boards' legal footing | Open: to check in drafting |
| The signs-of-failure thresholds | Working choices |
| The credit's size, memo 10, points 5 and 11, good-cause quits, American Samoa, the monthly statement | **Provisional**, for Espen (below) |

## Evidence still needed

- A CBO score of memo 1 B on the 2029 baseline, with its family-income table (point 15); until then CBO's 2019 table for $15 stands in [EV-WRK-450]. That table was read from a third-party copy of CBO's PDF and should be checked against cbo.gov.
- Hours in the household model's extract, so the floor can be distributed on real workers (part 2).
- A county-level measure of the floor's bite (LAB-4.04's first task).
- A study of whether wage insurance lowers employers' wage offers to displaced workers.
- Case law or analysis on first-contract arbitration and binding wage boards under current doctrine.
- The share of minimum-wage workers at firms under 50 workers, to size who the credit reaches.
- Everything listed in sections 1-6's "Evidence still needed", including CBO's 2018 FUTA option against cbo.gov [EV-WRK-435] [EV-WRK-436].

## Questions for Espen

No new question in this section. Each item below is tested here on its recommendation and stays provisional:
1. **The small-business credit's size** (LAB-5.01): about $3 billion as specified, not the $0.02-0.04 trillion memo 1 carried. Recommended: keep it as specified (section 6, part 4, item 1). This choice is mainly about money.
2. **Memo 10** (LAB-19), measuring displacement and a standby trigger: recommended C and C. Part 6 answers the AI objection on it.
3. **Point 5**, severance (LAB-14.01): no mandate in the first bill; study, then recommend.
4. **Point 11**, codetermination (LAB-17.01): no board seats in the first bill; still being studied.
5. **Good-cause quits in wage insurance** (LAB-18.03): work-connected quits in, personal ones out (about $1.5 billion over FY2030-39).
6. **American Samoa's wage path** (LAB-4.10): recommended B.
7. **Wage insurance's monthly statement** (LAB-18.08): the worker confirms hours each month.

For the milestone review, not Espen: LAB-11.10's provisional fix (part 8), and part 1B's single-adult finding for the secure floor's owners.
