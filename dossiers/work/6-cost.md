# Fair pay and real power at work: cost

Role: section 6 of the work dossier (flagship 5). It prices every provision of `4-specification.md` and `5-delivery.md` (84 in `provisions.json`) on federal fiscal years against the January 2029 law. It reports the fiscal-rule effect to the financing settlement (`charter/STANDARDS.md`, "Fiscal rule in dossiers: report, don't gate", `DEC-2026-11-10-05`). Status: **draft** (stage F), on `DEC-2026-11-17-01` to `-36`, `-95` and `-96`; revised in the milestone review's fix step 1 (the unemployment and wage insurance lines and the AmeriCorps match, review O-1, O-2, O-4 and O-5). Every figure is project arithmetic or judgment on outside anchors, not an official score; point 15 (`DEC-2026-11-17-28`) asks CBO and JCT for scores in 2027-28. **Nothing is booked here.** Booking follows the milestone review (`charter/STANDARDS.md`, "Milestone review"), and part 9 lists the ledger rows a booking would change. Items still with Espen are priced on their recommendations and marked **provisional** (part 4).

## Counting rules

- **Conventions.** Federal cost in nominal $ billion unless marked, against the January 2029 law, a cost positive. FY y runs from October of y-1. A calendar-year amount lands three-quarters in its own fiscal year and a quarter in the next, as care's, health's and the secure floor's paths count.
- **The path.** `tools/work_path.py` lays every line on FY2030-40, with a central, low and high path. Run `python3 dossiers/work/tools/work_path.py` for the tables, `--parts` for this section's blocks, `--ui-options` for the unemployment options put to Espen and `--check` for the coverage test and the derivations: every one of the 84 provisions is on a line or listed with its reason for having none (part 5). Its anchors are evidence IDs or labeled judgment, in its comments and below. Ranges are bounds: they put each line's inputs at their low or high values and sum line by line. They are not probability intervals, and the lines are not independent.
- **One basis for each figure** (`dossiers/TEMPLATE.md`). Every fiscal-rule figure is on the budget model's basis: case `mixed`, the general fund, the primary balance before interest, against the plan-wide gap the model carries now (`models/data/recovery-budget-paths.csv`, `agenda_gf_primary_bn`). That gap is **$602.7 billion short in FY2040** (1.11% of GDP) and $3,773 billion over FY2030-39, on main after #402 (`charter/PROGRESS.md`; `dossiers/foundations/checkpoint-financing.md`, part A1). The booked work rows beside each figure are read from the model's audit lines (`legacy/sources/recovery-budget-audit.csv`, case `mixed`), not rebuilt.
- **Five kinds of line are kept apart and never added into each other:**
  1. *spending lines* on the general fund, mandatory (the 2029 reconciliation act, R1) or appropriated (marked "appropriated": an authorization whose outlay depends on annual appropriations);
  2. *revenue effects* on the general fund: the credit, tax offsets and receipts, each on its own line;
  3. *the wage floor's indirect effect*, which is CBO's net of spending and revenue together, so it is labeled as such and added to neither;
  4. *the UI trust funds*: benefits paid from the state accounts and the employers' state taxes that pay for them, outside the general fund (part 2);
  5. *Social Security's funds* (off budget).
- **Firm, contingent and provisional.** A *firm* line is money the decided law spends in the budget model's projection. A *contingent* line is zero unless an event or a gate occurs (a recession, the service tranche's gate, the standby trigger); it is shown from zero to its cap and is not added to the firm total (`dossiers/TEMPLATE.md`, "Say what a model figure leaves out"). A *provisional* line prices an item still with Espen on its recommendation.
- **No recession in the projection.** CBO's projection, and so the budget model's, has no recession. The firm lines follow it. Extended Benefits in a downturn is the contingent line (part 2). Memo 7's general-fund range averaged one moderate downturn into the decade; this section separates the two.
- **Each material input's status** (commitment, working assumption, open question, or study in implementation) is in part 10.

## 1. The decided set on the general fund, by fiscal year

Firm lines, central path, $ billion. Rows are rounded; totals are the tool's unrounded sums.

| Line | Provisions | 2030 | 2031 | 2032 | 2033 | 2034 | 2035 | 2036 | 2037 | 2038 | 2039 | **FY2030-39** | **2040** | Range FY2030-39 | Range 2040 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 14(c) transition grant to VR and developmental disability agencies | LAB-4.09 | 0.40 | 0.40 | 0.40 | 0.40 | 0.40 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | **2.0** | **0.0** | 1.0 to 3.0 | 0.0 to 0.0 |
| Standards boards office and the wage commission | LAB-3.01, LAB-3.02, LAB-3.04, LAB-4.04 | 0.05 | 0.07 | 0.08 | 0.09 | 0.10 | 0.11 | 0.12 | 0.13 | 0.14 | 0.14 | **1.0** | **0.15** | 0.62 to 3.0 | 0.09 to 0.40 |
| Wage and safety outreach grants | LAB-7.05 | 0.05 | 0.05 | 0.05 | 0.05 | 0.06 | 0.06 | 0.06 | 0.06 | 0.06 | 0.06 | **0.56** | **0.06** | 0.28 to 1.1 | 0.03 to 0.13 |
| Extended Benefits, federal share, ordinary years | LAB-11.04 | 0.0 | 3.6 | 4.9 | 5.1 | 5.3 | 5.5 | 5.7 | 5.9 | 6.2 | 6.4 | **48.5** | **6.7** | 15.0 to 107.2 | 2.1 to 14.8 |
| State UI administration: the floor and the larger program's workload | LAB-11.06, LAB-11.08 | 0.42 | 0.73 | 0.85 | 0.88 | 0.91 | 0.94 | 0.97 | 1.00 | 1.0 | 1.1 | **8.8** | **1.1** | 6.7 to 12.9 | 0.82 to 1.7 |
| UI conformity and systems grant | LAB-11.09 | 0.50 | 0.50 | 0.50 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | **1.5** | **0.0** | 1.0 to 2.0 | 0.0 to 0.0 |
| Hours in state wage records, one-time grant | LAB-18.06 | 0.0 | 0.05 | 0.10 | 0.05 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | **0.20** | **0.0** | 0.10 to 0.40 | 0.0 to 0.0 |
| Wage insurance benefits | LAB-18.01, LAB-18.02, LAB-18.04, LAB-18.05, LAB-18.07 | 0.0 | 0.08 | 0.89 | 1.8 | 2.1 | 2.1 | 2.2 | 2.3 | 2.3 | 2.4 | **16.2** | **2.5** | 8.1 to 25.8 | 1.2 to 3.9 |
| Wage insurance administration, including the monthly statement | LAB-18.08 | 0.15 | 0.16 | 0.09 | 0.18 | 0.21 | 0.21 | 0.22 | 0.23 | 0.23 | 0.24 | **1.9** | **0.25** | 0.85 to 3.5 | 0.10 to 0.47 |
| Apprenticeship grants: instalments, completion, instructors, supports | LAB-8.01, LAB-8.02, LAB-8.03, LAB-8.04, LAB-8.06, LAB-8.07 | 0.87 | 1.8 | 2.2 | 3.1 | 3.6 | 4.0 | 4.2 | 4.5 | 4.6 | 4.8 | **33.6** | **4.9** | 23.6 to 53.8 | 3.4 to 7.9 |
| National service: 150,000 more civic positions | LAB-9.01, LAB-9.02, LAB-9.04, LAB-9.05, LAB-9.06 | 1.1 | 2.2 | 3.4 | 4.7 | 5.9 | 6.1 | 6.2 | 6.3 | 6.4 | 6.6 | **49.0** | **6.7** | 41.6 to 56.3 | 5.7 to 7.7 |
| **Spending lines** | | **3.5** | **9.6** | **13.5** | **16.3** | **18.6** | **19.0** | **19.7** | **20.4** | **21.0** | **21.7** | **163.3** | **22.3** | **98.8 to 269.1** | **13.5 to 36.9** |
| Small-business transition credit, first three steps (revenue effect) | LAB-5.01 | 0.38 | 1.0 | 1.2 | 0.30 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | **2.9** | **0.0** | 1.5 to 7.3 | 0.0 to 0.0 |
| Income-tax offset on employers' larger UI taxes, net of tax on benefits | LAB-11.05 | 0.0 | 2.0 | 2.7 | 2.8 | 2.9 | 3.1 | 3.2 | 3.3 | 3.4 | 3.6 | **27.0** | **3.7** | 6.5 to 85.8 | 0.89 to 11.8 |
| Income tax on wage insurance payments (receipts) | LAB-18.02 | 0.0 | -0.01 | -0.09 | -0.18 | -0.21 | -0.21 | -0.22 | -0.23 | -0.23 | -0.24 | **-1.6** | **-0.25** | -3.1 to -0.65 | -0.47 to -0.10 |
| Civil penalties under the labor act and wage law (receipts) | LAB-2.01, LAB-7.04, LAB-13.01 | 0.0 | -0.05 | -0.05 | -0.05 | -0.05 | -0.05 | -0.05 | -0.05 | -0.05 | -0.05 | **-0.45** | **-0.05** | -1.4 to -0.09 | -0.15 to -0.01 |
| **Revenue effects** | | **0.38** | **3.0** | **3.8** | **2.9** | **2.7** | **2.8** | **2.9** | **3.0** | **3.2** | **3.3** | **27.9** | **3.4** | **3.5 to 92.4** | **0.27 to 11.7** |
| The wage floor's indirect effect on the budget (CBO's net method) | LAB-4.01, LAB-4.02, LAB-4.03, LAB-4.06, LAB-4.07, LAB-4.08 | 0.30 | 0.80 | 1.5 | 2.3 | 3.2 | 4.0 | 4.6 | 4.9 | 5.1 | 5.3 | **32.0** | **5.5** | 0.0 to 80.0 | 0.0 to 8.0 |
| **Work on the general fund, firm lines** | | **4.2** | **13.4** | **18.8** | **21.5** | **24.5** | **25.8** | **27.2** | **28.3** | **29.3** | **30.3** | **223.2** | **31.3** | **102.3 to 441.5** | **13.7 to 56.6** |

- **The decided set, firm lines:** about **+$0.22 trillion over FY2030-39 (range about +$0.10 to +$0.44 trillion) and about +$31 billion in FY2040 (range about $14-57 billion)** on the general fund. Of the FY2040 figure, spending lines are $22.3 billion, revenue effects $3.4 billion and the floor's indirect effect $5.5 billion. The milestone fix (review O-1 and O-2) derived the unemployment benefit lines from LAB-11.01's standard and wage insurance from its own chain; before it the totals were +$0.20 trillion and +$27.4 billion.
- **With the service tranche** (contingent on its gate, part 3): about +$0.23 trillion and +$33.9 billion. **With the provisional items** on their recommendations (part 4): about +$2 billion more over the decade and +$0.2 billion in FY2040; the standby trigger adds up to $5 billion a year when on, from about 2035.
- **Against section 4's decided set** (+$0.18-0.38 trillion and +$19-35 billion), the decade sits in the lower half and FY2040 in the upper half. What moved, line by line:
  - *The credit* (LAB-5.01): about $3 billion, not $20-40 billion (below and part 4, item 1).
  - *Unemployment insurance:* the recession average moves to a contingent line (part 2). The firm general-fund spending is about $59 billion over FY2030-39, most of it Extended Benefits in ordinary years at the standard's benefit levels. Two lines are new: the administration of the larger program's workload, about $4 billion, and the general fund's tax offset on employers' larger UI taxes, about $27 billion (part 2).
  - *Apprenticeship* (LAB-8): about $0.034 trillion, below section 4's $0.04-0.07 trillion, once the decided payment rules and attrition are counted (below).
  - *Wage insurance* (LAB-18): about $16 billion of benefits, below memo 8's range over the decade because payments ramp up from 2031, plus about $1.9 billion of administration, a line section 5 added and memo 8's figure did not include (below).
  - *National service* (LAB-9): the decade is unchanged ($0.049 trillion civic, $0.060 trillion with the tranche). FY2040 is about $6.7 billion civic and $9.4 billion with the tranche, above the note's $7-8.5 billion, which was not in FY2040 dollars (below).
  - *The boards and the commission:* about $1 billion over the decade and $0.15 billion in FY2040, at the low end of section 3's $1-3 billion (below).

**The basis of each line.** Judgment unless marked. Every anchor is in section 3, "What the options cost", or cited here.
- **The credit (LAB-5.01), re-derived bottom-up from the specification.** It pays a share of each step's added wage cost for the four quarters after the step, only for workers paid below the step's rate, and only at employers under 50 workers. The steps reach workers mostly where the federal floor binds: the 12 states at $7.25 [EV-WRK-013] and those with no minimum or a lower one. By 2030-32 even $12.50 sits far below the all-jobs median of about $29-31 an hour (project arithmetic on [EV-WRK-078] at 3.5% a year). The added wage cost at small employers comes to about $1.0 billion for the first step, $3.5 billion for the second and $6.0 billion for the third (judgment: workers below each step, about 40% of them at small employers). At 50%, 35% and 20%, the credit comes to about **$2.9 billion over FY2030-33 (range $1.5-7.3 billion)**, claimed on the quarterly Form 941. The $20,000 cap rarely binds at these amounts. Section 4's $0.02-0.04 trillion was memo 1's judgment, "a third of the legacy credit's range" [EV-WRK-703], set before the credit's form was decided (`DEC-2026-11-17-34`). That legacy credit was built for a $17 floor phased in over eight years, and the decided credit covers three steps and the new increment only. The provision as written is priced here. Whether to keep it at this size is put to Espen (part 4, item 1). *Basis note:* a credit against the employer's share of payroll tax would reduce Social Security's and Medicare's receipts. The specification should say that the general fund makes the trust funds whole, as it did for the 2020-21 payroll credits (working assumption, to add to LAB-5.01 at the next touch). It is priced here as a general-fund revenue effect.
- **The floor's indirect effect (memo 1 B).** CBO put $15 by 2025 at +$54 billion over 2021-31 [EV-WRK-032], a floor at about 61% of 2025's median [EV-WRK-078]. Memo 1 B's $17 is about half the median in 2035. CBO's figure nets higher federal costs (prices of what the government buys, unemployment compensation) against higher revenue and lower income support. Scaled to the smaller bite and the later steps, it is about $32 billion over FY2030-39 and $5.5 billion in FY2040, with section 3's range kept (zero to +$0.08 trillion; $3-8 billion in FY2040, widened to zero at the low end because the sign of a smaller bite's effect is not tested). The budget model carries the floor at zero (LAB-1) and in its distributional row DY4 [EV-WRK-707].
- **Extended Benefits, ordinary years (LAB-11.04).** Under the January 2029 law the federal half of Extended Benefits rarely triggers. The new triggers include a state's own three-month rate at 5.5%. Some states sit near that rate in ordinary years, so with a 100% federal share the program pays in a few states even without a recession: about $3 billion in calendar 2031 at today's weekly benefits (range $1-6 billion), growing with benefits. Each Extended Benefits week pays the regular weekly amount, so the line rises with LAB-11.01's standard: times about 1.58, the standard's replacement factor (part 2), with the number of weeks held (judgment: more claimants and the 26-week floor roughly offset in who reaches Extended Benefits). That is about $4.7 billion in calendar 2031, **$48.5 billion over FY2031-39 and $6.7 billion in FY2040** (range $15-107 billion and $2.1-14.8 billion; judgment). Before the milestone fix the line was $31 billion and $4.2 billion, at today's weekly benefits. OMB scored the FY2017 budget's Extended Benefits reform, fully federal with new triggers, at $36.7 billion over 2017-26 on a projection with no recession, about $3.7 billion a year (OMB, FY2017 budget, Obama administration, 2016) [EV-WRK-438]; it is the anchor here. The states' unemployment rates are not yet in the register ("Evidence still needed").
- **State UI administration (LAB-11.06, 11.08).** The floor restores about $0.38 billion a year above FY2026's $2.76 billion [EV-WRK-309] [EV-WRK-308], indexed. Section 5 said the floor "pays for running the larger program". This section adds the larger program's workload: about 40% more recipients need more claims-taking, adjudication and appeals. That is about $0.4 billion a year from 2031 (range $0.2-0.8 billion; judgment). Workload follows claims and weeks, not the size of each check: part 2's derivation puts weekly recipients at about 1.4 times today's (range 1.2-1.6), so the line stands after the milestone fix. The appropriations acts already add administrative money automatically when claims rise above a base, and that mechanism would carry it (the rate per 100,000 claimants is not yet in the register). Both are appropriated from the administration account that FUTA finances [EV-WRK-310]. They are counted on the general fund here, as memo 7 counted them, which is the cautious reading (part 2).
- **The conformity grant (LAB-11.09)** is section 5's $1-2 billion over FY2030-32. **The hours field (LAB-18.06)** is the decided part of section 5's $0.2-0.5 billion one-time grant for new wage-record fields, about $0.2 billion. The occupation part is memo 10's (part 4).
- **Wage insurance (LAB-18.01-18.05, 18.07), re-derived step by step** (milestone review O-2). Separations count from January 1, 2031, and payments start on reemployment within 12 months and last up to two years. In steady state:
  - about 1.1 million long-tenured workers are displaced a year (3.3 million over 2023-25) [EV-WRK-315]. The survey counts layoffs only: plant closings, slack work and abolished positions;
  - times about 1.15 for long-tenured workers discharged not for misconduct, whom LAB-18.03 makes eligible (`DEC-2026-11-17-95`: "a worker fired for poor performance qualifies") and the survey does not count (range 1.05-1.30; judgment: no register entry counts them, and misconduct is the narrow, willful standard most states use [EV-WRK-416]);
  - about 88% earned under the cap of twice the median (judgment);
  - about 60% are reemployed within a year (66.1% were reemployed by the survey date) [EV-WRK-315];
  - about half of those are paid less (49% of the full-time reemployed earned as much or more) [EV-WRK-317];
  - about 60% take it up with the automatic offer on the claim form (judgment). No take-up rate among eligible workers is in the register. TAA's 11% [EV-WRK-332] is the share of *all* trade adjustment participants who collected wage insurance, most of whom were not eligible for it (under 50, in training or not reemployed at lower pay), so it is not a take-up benchmark (milestone review O-4).

  That is about 0.20 million new recipients a year (1.1 × 1.15 × 0.88 × 0.6 × 0.5 × 0.6), each paid for about 1.6 years, so about 0.32 million on the rolls at a time, near the low end of section 5's 0.3-0.6 million. At about $6,000-6,500 a year each in 2033, that is **about $2.0 billion a year in steady state**, reached in FY2034 as the cohorts fill in ($0.9 billion in FY2032 and $1.8 billion in FY2033). The path grows about 3% a year: wages and the labor force, less about a point as more payments reach the $10,000 cap, which is fixed until the commission's 2035 report (LAB-18.02); indexing it then would raise growth toward 4% (not assumed). That is **$16.2 billion over FY2031-39 (range $8-26 billion) and $2.5 billion in FY2040**. Before the milestone fix the tool carried $2.4 billion for FY2033 with no step from the chain, $20 billion and $3.0 billion; the chain without discharges gives about $1.7 billion. Memo 8's $2-4 billion a year counted every reemployed worker paid less, at full take-up, without the 12-month window; this steady state sits at that range's low end. *Clean power's guarantee comes first* (LAB-18.07): about 8,000 covered layoffs a year (`dossiers/clean-power/5-delivery.md`, part 2), too few to move the line.
- **Wage insurance administration (LAB-18.08's monthly statement included)** is about 10% of benefits (range 8-12%), the ratio of state UI administration to pre-pandemic unemployment outlays ($3.14 billion against $29.9 billion) [EV-WRK-309] [EV-WRK-413], plus about $0.15 billion of set-up in each of FY2030 and FY2031. Section 5 asked whether memo 8's $2-4 billion already included it. It did not: memo 8's basis is a count of workers times an average payment. So administration is its own line, about $1.9 billion over FY2030-39 and $0.25 billion in FY2040 (range $0.1-0.5 billion), inside section 5's $0.2-0.4 billion a year.
- **Apprenticeship (LAB-8.01-8.04, 8.06, 8.07), re-derived with the decided payment rules.**
  - *Starts:* new starts rise from 311,035 (FY2025, held through FY2029) [EV-WRK-349] to 600,000 by FY2034 (LAB-8.04), then grow 0.5% a year.
  - *Who is paid:* grants go to sponsors per apprentice in the four sectors. That covers apprentices who would have started anyway, about 55% of today's starts (judgment), plus 90% of the growth.
  - *How much:* up to $12,000 (2030 dollars, indexed), paid about $4,000 at the start, $4,000 the next year for the about 75% still training, and $4,000 at completion three years on for the about 45% who complete (42% complete within a year of their expected date [EV-WRK-350]). An expected $8,800 a start, less about 2% for care training HLT-10.06 already pays (LAB-8.07).
  - *Instructors and supports* (LAB-8.02, 8.03) are shares of each grant, not money on top.

  The result is about **$33.6 billion over FY2030-39 (range $24-54 billion) and $4.9 billion in FY2040**. Memo 8's $4-7 billion a year at full scale paid $10,000-15,000 for each of 300,000 added starts in full. Against CBO's $3.1 billion over five years for the 2020 bill [EV-WRK-396] and $5,171 an apprentice in the federal initiative [EV-SEC-640], the line is larger and paid per apprentice, as memo 8 intended.
- **National service, civic positions (LAB-9.01, 9.02, 9.04-9.06).** The ramp adds 30,000 positions a year from FY2030 to 150,000 in FY2034. The federal cost per position is:
  - AmeriCorps' $25,200 per member service year (FY2026, indexed at 2.5%) [EV-WRK-398];
  - plus about 5% for child care and the agency;
  - plus the education award at the maximum Pell grant, $7,395, which the January 2029 law holds flat [EV-WRK-399].

  That is about **$49 billion over FY2030-39 and $6.7 billion in FY2040** (range ±15%).
  - *The grantees' match* (milestone review O-5; LAB-9.01's working assumption). The $25,200 is the *maximum* federal share per member service year [EV-WRK-398]. Grantees pay the rest of program costs: an overall share of 24% in grant years 1-3, rising to 26%, 28% and 30% from the tenth year, with a waiver for programs in rural or severely economically distressed communities (45 CFR 2521.60) [EV-WRK-454]. With the federal share at the maximum, the match per position is the federal grant times the share over one minus the share: about $8,000 in FY2026 dollars at 24%. Counting each year's 30,000 new positions as new grants that climb the schedule, the match is **about $1.5 billion in FY2034, $13.4 billion over FY2030-39 and $2.2 billion in FY2040** (range $10.7-16.4 billion and $1.7-2.3 billion: all at 30% at the top, a fifth less where the waiver is used at the bottom; project arithmetic on the rule). *It is not federal cost*: host organizations, states and their funders raise it, so it is reported beside LAB-9 and never added to the general fund. It is a delivery risk instead: the match is part of what limits host sites, the binding constraint (`5-delivery.md`, part 3). *Alternative:* if Congress waived the match for the new positions, or federalized it, the federal cost would rise by the same amount, to about $62 billion over FY2030-39 and $8.9 billion in FY2040 for the civic positions. The note's $7-8.5 billion in FY2040 (`notes/espen-questions-2026-11-17.md`, part e) used today's costs. In FY2040 dollars the decided 200,000 cost about $9.4 billion with the tranche (part 3). The decade figure, $0.060 trillion with the tranche, sits inside `DEC-2026-11-17-32`'s $0.04-0.065 trillion. Whichever route funds it, the authorization (appropriated) or R1's fallback (direct spending, LAB-9.06), the cost is the same. The route decides only whether it is mandatory or subject to appropriation.
- **The 14(c) grant (LAB-4.09)** is section 4's $1-3 billion, spread evenly over FY2030-34.
- **The boards office and the commission (LAB-3.01-3.04, 4.04)** are built bottom-up:
  - the commission's staff, about $15 million a year;
  - a boards office of 100-200 staff at about $0.25 million a staff year;
  - about $5-10 million a year for each board's hearings, one board from 2030 rising to about ten by the late 2030s.

  That is about $1.0 billion over FY2030-39 and $0.15 billion in FY2040, appropriated. Section 3's $1-3 billion and $0.2-0.4 billion are kept as the range. Enforcing the boards' standards is Wage and Hour's work, counted in CAP-7.
- **Outreach grants (LAB-7.05)** are section 4's $50 million a year, indexed, appropriated.
- **Revenue effects.**
  - *The UI tax offset.* Employers' larger UI taxes lower taxable wages. Under the scorekeepers' convention about a quarter of a new employer tax comes back as lower income and payroll tax. About 15 points of that falls on income tax, and about 10 points return as income tax on the larger, taxable benefits. So about 5% of the tax increase is a general-fund loss: about $27 billion over FY2030-39 and $3.7 billion in FY2040 (range 2-10% of part 2's range, $6.5-86 billion; judgment). Before the milestone fix it was $13 billion and $1.8 billion, on the old benefit line. The payroll part, about 8%, falls on Social Security (part 2). JCT would score this with the wage base (point 15).
  - *Income tax on wage insurance:* the payments are taxable as wages (INC-5.01), at about 10%, a gain of about $1.6 billion over FY2030-39.
  - *Civil penalties:* CBO put the 2019 bill's labor-board penalties at $39 million over ten years [EV-WRK-176]. The wage-law penalties add more once there are 1,200 investigators. In all about $50 million a year in receipts (judgment).

## 2. Unemployment insurance on each budget

The UI system is a federal-state trust fund on the federal budget. State benefits and employers' state taxes both pass through the Unemployment Trust Fund, and the federal accounts are financed by the federal unemployment tax (FUTA) [EV-WRK-310]. Memo 7 B changes all three: the state accounts, the federal accounts and the general fund.

| Line | Provisions | 2030 | 2031 | 2032 | 2033 | 2034 | 2035 | 2036 | 2037 | 2038 | 2039 | **FY2030-39** | **2040** | Range FY2030-39 | Range 2040 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| UI regular benefits from the state trust funds (employer-financed) | LAB-11.01, LAB-11.02, LAB-11.03, LAB-11.07 | 0.0 | 39.6 | 54.4 | 56.6 | 58.8 | 61.2 | 63.7 | 66.2 | 68.8 | 71.6 | **541.0** | **74.5** | 324.1 to 857.8 | 44.6 to 118.1 |
| Employers' state UI taxes on the larger base (receipts, matching the benefits) | LAB-11.05 | 0.0 | -39.6 | -54.4 | -56.6 | -58.8 | -61.2 | -63.7 | -66.2 | -68.8 | -71.6 | **-541.0** | **-74.5** | -857.8 to -324.1 | -118.1 to -44.6 |
| Payroll-tax offset on employers' larger UI taxes (Social Security) | LAB-11.05 | 0.0 | 3.2 | 4.4 | 4.5 | 4.7 | 4.9 | 5.1 | 5.3 | 5.5 | 5.7 | **43.3** | **6.0** | 16.2 to 85.8 | 2.2 to 11.8 |

**UI on one basis.** Federal fiscal years, nominal $ billion, a cost positive, from `tools/work_path.py`; each block is kept apart and none is added into another (`dossiers/TEMPLATE.md`, "One basis for each fiscal figure").

| Where it falls | Lines | FY2030-39 | FY2040 | Who pays |
| --- | --- | --- | --- | --- |
| State accounts in the Unemployment Trust Fund (on budget, off the general fund) | Regular benefits under LAB-11.01-11.03, 11.07 | +541.0 (324-858) | +74.5 (45-118) | Employers, through state UI taxes on the larger base (LAB-11.05), matched over the cycle: −541.0 and −74.5 |
| General fund, spending (part 1) | Extended Benefits in ordinary years, administration, the conformity grant | +58.8 (23-122) | +7.8 (2.9-16.4) | Federal taxpayers |
| General fund, revenue effect (part 1) | The income-tax offset on the larger employer taxes, net of tax on benefits | +27.0 (6.5-86) | +3.7 (0.9-11.8) | Federal taxpayers |
| **General fund, UI in all** | | **+85.9 (29-208)** | **+11.5 (3.8-28.2)** | Before the milestone fix: +54.0 and +7.1 |
| Social Security (off budget) | The payroll-tax offset | −43.3 to the funds (16-86) | −6.0 (2.2-11.8) | The trust funds' receipts |
| Contingent: Extended Benefits in a downturn (part 3) | LAB-11.04 | 0 to about +120 | zero in the projection | Federal taxpayers |

- **The trust funds' side, derived from LAB-11.01's standard: about +$42 billion a year at FY2025 levels (range $25-66 billion), employer-financed, on its own line** (milestone review O-1; judgment on the factors below, project arithmetic on the evidence tagged). Regular state benefits are about **$38 billion a year today**: OMB's $41.8 billion for FY2025 [EV-WRK-413] covers the whole unemployment compensation subfunction, which also carries about $3-4 billion of state administration [EV-WRK-309] and federal workers' and veterans' benefits (judgment for the second part); DOL's third quarter of 2026, $9.2 billion in a seasonally light quarter, is consistent [EV-WRK-451]. The standard multiplies them by four factors:
  1. *Replacement, about 1.58 times today's.* LAB-11.01 pays 75% of high-quarter weekly pay up to a maximum of at least two-thirds of the state's average weekly wage. Benefits replace 43% of recipients' wages today [EV-WRK-302]; at the $491 average weekly benefit [EV-WRK-451] that puts recipients' wages near $1,140 a week, about 0.72 of the average weekly wage in covered jobs (about $1,550-1,640 [EV-WRK-453]). Most recipients sit below the point where the cap binds (high-quarter pay of about 0.89 of the average wage), so their replacement rises to 75% of high-quarter pay; those above it are capped. With recipients' wages spread around that mean (lognormal, log-sd 0.5, range 0.4-0.6) and high-quarter pay about 1.05 times average weekly pay (range 1.0-1.15), the average replacement becomes about **68% (range 63-75%)**.
  2. *More claimants: first payments up about 20% (range 10-25%),* from covering part-time workers, the $1,000 / $1,500 test, the most recent quarter, ABC coverage and the compelling-reason quits. The 2009 modernization incentives moved first payments 6-10% at most [EV-WRK-377], and the standard goes further. New claimants earn less, so each draws about 70% of the average benefit (range 60-80%).
  3. *The 26-week floor: weeks up about 4% (range 3-6%).* The 16 states that pay fewer than 26 weeks [EV-SEC-048] pay about a tenth of today's benefit weeks (judgment).
  4. *Longer claims as benefits rise: weeks up about 12% (range 4-24%),* on a duration elasticity of 0.25 (range 0.1-0.38), between the pandemic-era 0.06-0.22 [EV-WRK-370] and the pre-pandemic U.S. median of 0.38 [EV-WRK-368].

  Together, weekly recipients rise about 1.4 times, taking recipiency from 29% toward 40% as memo 7 assumed, and **benefits rise about 2.1 times (range 1.7-2.7)**. From benefit weeks starting January 1, 2031, and growing 4% a year, that is about **$54 billion in FY2032 and $74 billion in FY2040 (range $45-118 billion), and $541 billion over FY2031-39**. The ranges are bounds that set every factor at its low or high value at once.
- **What changed, and why.** Memo 7 and section 4 put the increase at $15-25 billion a year (40-60%), on "recipiency toward 40% and replacement toward about half" [EV-WRK-413]. Half is what a 50% replacement rate gives: the same derivation at 50% of high-quarter pay comes to about $17 billion. LAB-11.01, as decided, pays 75%, so the specified standard costs about twice what memo 7 showed. The general fund moves by much less: about +$32 billion over FY2030-39 and +$4.4 billion in FY2040 (the table above), through Extended Benefits' weekly amounts and the tax offset. The cost to employers is put to Espen as a question (below, and "Questions for Espen", item 1).
- **What it means for employers and the states.** States' UI taxes raised about $42 billion in the 12 months to September 2026 [EV-WRK-452], about a third of a percent of total covered wages (about $3.2 trillion in the first quarter of 2026 [EV-WRK-453]; about $12-13 trillion a year, project arithmetic). The standard roughly doubles them: about $42 billion a year more at FY2025 levels, about $275 a covered worker (152.7 million covered jobs [EV-WRK-453]; project arithmetic), or about two-thirds of a percent of total wages in all. The larger wage base (LAB-11.05) spreads the added tax over more of each worker's pay; JCT and CBO score the schedule (point 15). The trust funds' starting point is weak (18 states met the solvency standard at the start of 2026 [EV-WRK-304]), so states pay the first years partly from reserves or federal advances [EV-WRK-305], and the solvency review trigger (`7-validation.md`, part 7) matters more than before.
- **The two trust-fund lines are the cycle average.** States pay benefits from their own accounts and refill them with employers' state taxes on the larger base, so over the cycle the two match, and the tool shows them netting to zero every year. In any one year they do not: a state builds reserves in good years and draws them down in bad ones, or borrows from the federal account [EV-WRK-305]. Neither line is on the general fund, and neither is added to section 1's total.
- **Social Security loses about $43 billion over FY2031-39 and $6.0 billion in FY2040** (off budget, range $2.2-11.8 billion in FY2040). This is the payroll part of the offset on the larger employer taxes, 8% of them; before the milestone fix it was $21 billion and $2.9 billion.
- **FUTA itself barely moves.** The net federal rate falls as the base rises (LAB-11.05): about $42 a worker today and about $50 at the $25,000 base (project arithmetic, section 4). The federal accounts gain perhaps $0.5-1.5 billion a year from FY2033, net of the offset (judgment; JCT scores it). That gain goes to the administration account and the extended-benefit account. It would cover the administration floor and part of the ordinary-year Extended Benefits, which section 1 counts on the general fund. Counting both there, and not netting this receipt against them, is the cautious reading. The alternative booking, which pays them from the federal accounts first, would lower the general-fund line by up to about $1-1.5 billion a year.
- **Extended Benefits in a downturn (contingent).** A moderate two-year recession in the window would pay 26-39 weeks beyond the regular 26 in most states, fully federal: about **$120 billion** over the downturn (range about $100-150 billion; judgment: about two million exhaustees a year at about 30 weeks, at about $1,000-1,150 a week in the mid-to-late 2030s on the standard's benefit levels, is about $60-65 billion a year, and a deeper downturn costs more). The weekly amount is today's $491 [EV-WRK-451] times the standard's 1.58, grown with wages (project arithmetic); before the milestone fix the line used about $600 a week and came to $70-100 billion. That compares with the emergency programs Congress enacted ad hoc in 2008-13, which CBO's baseline does not carry either. The line is zero in the budget model's projection, which has no recession, and shown from zero to that figure. Its effect on unemployment is disputed, from 2 points [EV-WRK-374] to at most 0.3 [EV-WRK-375].
- **Work sharing, attestation, the ABC test, the compelling-reason quits and the identity checks** (LAB-11.02, 11.03, 11.06, 11.07) are inside the trust funds' line (factor 2 above) and the administration line. The identity checks should lower improper payments, which this section does not count as a saving.

**LAB-11.10: "charged to the reduced credit", in law and in the budget** (the reviewer's third note on #428).
- **What the law does today.** Federal law applies 100% of the added federal tax collected because of reduced credits to repaying the state's Title XII advances (42 U.S.C. 1101(d)(1)(A)) [EV-WRK-429]. Any excess goes to the state's own account in the Unemployment Trust Fund (1101(d)(1)(B)) [EV-WRK-430]. Advances are paid into that same state account [EV-WRK-431]. Money in a state's account may be withdrawn only to pay compensation under the state's own law [EV-WRK-432]. The section still cites the reduction as 3302(c)(3); it is now 3302(c)(2) [EV-WRK-428].
- **So LAB-11.10 does not work as drafted.** In a state with a loan, the added tax would repay the loan. In a state without one, it would land in the state's own account, which pays benefits only under the state's law: the law that fails the standard. None of the sections read gives the Labor Department authority to pay claimants directly. That is a finding from the sections read, not a search of the whole Code.
- **Proposed fix (provisional, a working choice for the milestone review).** Two amendments in R1:
  1. A *conformity reduction*, separate from today's loan reduction, whose added tax goes to a federal account in the trust fund instead of the loan or the state's account. Where a state also carries a loan, today's loan reduction keeps priority, so the two do not compete.
  2. *Authority for Labor to pay* the difference between the state's benefit and the federal standard through the state agency, under an agreement. States already pay federal benefits as Labor's agents; trade adjustment's wage insurance is one example [EV-WRK-331]. Labor pays directly only if a state refuses the agreement.

  Section 5's text (`5-delivery.md`, part 4) and LAB-11.10's entry in `provisions.json` now carry the fix in place of the old clause, "charged to the reduced credit" (section 7, the reviewer's note 3 on #429), still provisional. The fix changes no figure in part 1.
- **In the budget.** The added tax is federal revenue to the trust fund. State accounts are on the federal budget, as CBO describes them [EV-WRK-436], so the revenue and the top-up are both on budget and off the general fund. Over time they net to about zero, but not at first. The first step raises 0.3 point of the base, about $75 a worker a year at the $25,000 base (project arithmetic), while topping up a state far below the standard could cost more than that in the first years. The federal account would advance the difference and recover it from later steps, so the general fund pays nothing by design. The line is contingent and zero if every state conforms (part 3).

## 3. What the total leaves out

The firm total in part 1 does not include these items. Each is reported here with its amount, and none is added to a booked figure.

| Item | Provisions | FY2030-39 | FY2040 | Why it is not in the total | Firm or contingent |
| --- | --- | --- | --- | --- | --- |
| The service-to-apprenticeship tranche | LAB-9.03 | 0 to $12.8 billion ($11.3 billion if it opens in 2035 on the working ramp) | 0 to $3.0 billion | Paid only when the gate is met | Contingent |
| Extended Benefits in a downturn | LAB-11.04 | 0 to about $120 billion | zero in the projection | The budget model's projection, like CBO's, has no recession (part 2) | Contingent |
| The standby displacement trigger | LAB-19.04, 19.05 | 0 to $25 billion | 0 to $5 billion | Zero while off; capped; provisional (part 4) | Contingent, provisional |
| Good-cause quits and the displacement measure | LAB-18.03; LAB-19.01-19.03 | about $1.8 billion | about $0.2 billion | Provisional, for Espen (part 4) | Provisional |
| LAB-11.10's top-up in a state that does not conform | LAB-11.10 | zero if every state conforms | zero | Financed from the reduced credit once authorized, inside the trust fund (part 2) | Contingent |
| UI benefits from the state trust funds, and employers' state taxes | LAB-11.01-11.03, 11.05, 11.07 | about +$541 billion and −$541 billion | about +$74 billion and −$74 billion | Trust funds, matched over the cycle (part 2) | Firm, outside the general fund |
| Social Security's payroll offset on the larger UI taxes | LAB-11.05 | about −$43 billion to the funds | about −$6.0 billion | Off budget (part 2) | Firm, off budget |
| AmeriCorps grantees' match on the new civic positions | LAB-9.01 | about $13.4 billion (range $10.7-16.4 billion) | about $2.2 billion | Not federal: grantees, states and host organizations raise it under 45 CFR 2521.60 [EV-WRK-454] (part 1); federalizing it would add the same amount | Firm, non-federal |
| The NLRB's staff | LAB-2.05 | about $1.0-1.4 billion | about $0.10-0.15 billion | CAP-7, democratic renewal's booked lines: it fits inside the legacy NLRB row of $1.9 billion (range $1.3-3.3 billion) [EV-DEM-330], which narrows to work's figure at stage G (`dossiers/foundations/democratic-renewal/5-delivery.md`, answer 1) | Booked there |
| FMCS's mediators and arbitration panels | LAB-1.05 | about $0.1-0.2 billion | about $0.01-0.02 billion | CAP-7: in no row, a claim on the delivery contingency (democratic renewal's answer 2) | A claim on the contingency |
| Wage and Hour's and OSHA's inspectors | LAB-7.01-7.03, LAB-6.01, LAB-12, 13, 15 | about $2.4-4.0 billion | about $0.3-0.5 billion | Inside Labor's $4.6 billion in CAP-7 [EV-DEM-329] | Booked there |
| OSHA above CAP-7's +700 | LAB-7.01 | inside the line above at its high end | about $0.08 billion | A claim on CAP-7's contingency, released as OSHA's hiring path shows the need (answer 3) | A claim on the contingency |
| The Office of Apprenticeship's registration staff, and the FLRA | LAB-8.04, LAB-16.01 | not yet sized; small | not yet sized; small | Claims on CAP-7's contingency once Labor's 2027-28 plan sizes the first, and if the first year's count shows the second (answers 4 and 5) | To size |
| Home care workers' overtime and travel time in Medicaid | LAB-12.01 | about $1 billion if the 2013 rule is gone by 2029 (judgment); zero if it stands | from 2035 inside care's rates | The rule is in force today, but its enforcement was suspended in 2025 [EV-WRK-225]. If it stands in January 2029, writing it into statute costs nothing. If it is rescinded, restoring it raises federal Medicaid's home care costs, about $0.1-0.3 billion a year until the single plan's rates take over in 2035. No register entry sizes it | Open (the 2029 baseline) |
| The contractor minimum wage | LAB-4.05 | not priced | not priced | Executive action; contractors' higher costs fall inside agencies' appropriations, which the baseline holds at their level. The 2021 rule's own analysis is not yet in the register | Within appropriations |
| Higher wages' tax effects beyond the floor | LAB-7.08, 12.02, 15.01, LAB-1 | not counted | not counted | Conventional scoring holds the economy's size fixed; posted pay ranges raised wages 1.3-3.6% [EV-WRK-407], and unions' wage effects are in section 2 | Not counted |
| Employers' compliance costs | LAB-6.01, 7.08, 13.01, 15.01 | outside the budget | outside | Private costs; the heat standard's were $7.8 billion a year against $9.18 billion of benefits in the Biden administration's analysis [EV-WRK-255] | Not federal |
| AI-4's booked row | AI-4 (the AI topic's) | $200 billion booked | $29.5 billion booked | Booked as "displacement-triggered wage insurance and training accounts", the AI topic's row; wage insurance (LAB-18) and the trigger (LAB-19) would cover its wage-insurance part (parts 7 and 9) | Booked there; to re-scope |

## 4. Items still with Espen, priced on their recommendations (provisional)

| Line | Provisions | 2030 | 2031 | 2032 | 2033 | 2034 | 2035 | 2036 | 2037 | 2038 | 2039 | **FY2030-39** | **2040** | Range FY2030-39 | Range 2040 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Wage insurance for work-connected good-cause quits (provisional) | LAB-18.03 | 0.0 | 0.01 | 0.07 | 0.14 | 0.16 | 0.16 | 0.17 | 0.17 | 0.18 | 0.18 | **1.2** | **0.19** | 0.24 to 3.4 | 0.04 to 0.52 |
| Displacement measure: occupation field and BLS's report (provisional) | LAB-19.01, LAB-19.02, LAB-19.03 | 0.0 | 0.07 | 0.13 | 0.09 | 0.04 | 0.04 | 0.04 | 0.04 | 0.04 | 0.04 | **0.51** | **0.04** | 0.29 to 0.87 | 0.02 to 0.06 |
| **Provisional lines** | | **0.0** | **0.08** | **0.20** | **0.23** | **0.19** | **0.20** | **0.21** | **0.21** | **0.22** | **0.22** | **1.8** | **0.23** | **0.53 to 4.3** | **0.06 to 0.58** |

1. **The small-business credit's size (LAB-5.01), new: mainly about money.** As specified, the credit costs about **$3 billion (range $1.5-7 billion)**, not the $0.02-0.04 trillion Espen saw when choosing memo 1 part 2 C (part 1). This is a choice mainly about money (`charter/STANDARDS.md`), so it goes to Espen:
   - *Recommended: keep the credit as specified, at about $3 billion.* Espen asked for "a small, temporary credit". The precedent Espen pointed to is about this size: JCT put the 2007 package's small-business provisions at $4.8 billion over 2007-17 [EV-WRK-445]. They were a political cushion, not a tested way of softening job effects (`notes/espen-questions-2026-11-17.md`, part a). Section 4, `provisions.json`, the agenda row, memo 1's status line and the README now carry both figures, memo 1's judgment and this price. Drafted on the recommendation, provisional.
   - *Alternative: widen it toward the decided range.* Paying the credit for five steps instead of three, or at 50% in every year, would raise it to roughly $8-15 billion (judgment). Paying it for all workers below the new rate, at every employer, would raise it about two and a half times more. Each change adds claims and Form 941 lines.
2. **Memo 10 part 1 C, measuring displacement (LAB-19.01-19.03):** about $0.5 billion over FY2030-39 (range $0.3-0.9 billion): occupation's part of the one-time grant for wage-record fields (about $0.2 billion) and BLS's yearly report with an annual displaced-worker survey (about $35 million a year). That is inside memo 10's $0.5-1 billion, which also counted the hours field now in part 1. Part 1 B would cost about zero, and part 1 D slightly more.
3. **Memo 10 part 2 C, the standby trigger (LAB-19.04, 19.05):** **zero while off, contingent**, up to the $5 billion yearly cap when on, from about 2035: from $0 to $25 billion over FY2035-39 and up to $5 billion in FY2040. Its expected cost is near the low end, because broad displacement does not yet show in the data [EV-WRK-358]. Part 2 A or B would cost nothing; D would add an entry-level hiring credit, about $0.21 trillion at the legacy scenario's scale (memo 10).
4. **Wage insurance for work-connected good-cause quits (LAB-18.03's working reading):** about **$1.2 billion over FY2030-39 and $0.2 billion in FY2040** (range $0.2-3.4 billion). That is about 7% more recipients (range 3-12%; judgment, since no register entry counts quits found for good cause attributable to the employer), with their administration. *Alternatives:* excluding all quits costs nothing; including every good-cause quit, the personal ones under LAB-11.01's compelling reasons too, would roughly double this line (judgment).
5. **Point 5, severance (LAB-14.01), and point 11, codetermination (LAB-17.01):** no cost on the recommendation, since neither the mandate nor the board seats are in the first bill. A federal severance mandate would cost the budget little directly: employers pay it, and severance does not reduce unemployment benefits in most states (judgment).
6. **The territories' wage floor (LAB-4.10, revised in the milestone review's fix step 2):** no federal cost to speak of under any option, the recommended cap at 75% of each territory's median included. The territories' wage schedules are a mandate on employers. Payroll taxes rise with territorial wages and fall with any jobs lost; Puerto Rico's largest federal programs, nutrition aid and Medicaid, run on capped grants that do not follow wages as they do in the states (judgment). Too small and too uncertain in sign to price; no line changes. What differs among the options is the bite: $17 would sit at about 93% of Puerto Rico's median in 2035 on the national schedule, against about 72% under the cap (`5-delivery.md`, part 5; `tools/territory_bite.py`).
7. **Wage insurance's monthly statement (LAB-18.08):** inside the administration line (part 1). The alternatives cost about the same. *Quarterly payment in arrears* shifts about $0.3-0.6 billion of first-year payments from FY2031-32 one quarter later and changes no decade total. *Monthly employer reports* move the cost onto employers.

## 5. Every provision and where it is priced

`work_path.py --check` confirms that the 84 IDs below match `provisions.json` exactly.

| Provisions | Where priced | Note |
| --- | --- | --- |
| LAB-4.01-4.03, 4.06-4.08 | Part 1, the floor's indirect effect | The mandate costs employers; the budget feels it through prices and programs |
| LAB-4.04, LAB-3.01, 3.02, 3.04 | Part 1, boards and commission | Appropriated |
| LAB-4.05 | Part 3, not priced | Executive action |
| LAB-4.09 | Part 1, the 14(c) grant | R1 |
| LAB-4.10 | Part 4, item 6, zero | Provisional |
| LAB-5.01 | Part 1, revenue effects | Size provisional (part 4, item 1) |
| LAB-1.01-1.04, 1.06, 1.07, LAB-1A.01, LAB-2.02-2.04, 2.06 | No budget line; rules and remedies | The Board's workload is in CAP-7 |
| LAB-1.05, LAB-2.05 | Part 3, CAP-7 | FMCS and the NLRB |
| LAB-2.01, LAB-7.04, LAB-13.01 | Part 1, penalties (revenue) | Receipts |
| LAB-3.03 | No line; care's rates (HLT-10.04) | Booked there |
| LAB-16.01 | Part 3, CAP-7 (FLRA, small) | — |
| LAB-6.01-6.03 | No federal line; OSHA's staff in CAP-7 | Employers' compliance costs are private |
| LAB-7.01-7.03 | Part 3, CAP-7 | Wage and Hour and OSHA |
| LAB-7.05 | Part 1, outreach grants | Appropriated |
| LAB-7.06-7.09, LAB-12.02, LAB-15.01 | No budget line | Rules on employers |
| LAB-12.01 | Part 3, open (Medicaid if the 2013 rule is gone) | — |
| LAB-14.01, LAB-17.01 | Part 4, item 5, zero | Provisional |
| LAB-11.01-11.03, 11.07 | Part 2, trust funds | Employer-financed |
| LAB-11.04 | Part 1 (ordinary years) and part 2 (downturn, contingent) | Fully federal |
| LAB-11.05 | Part 2 (trust funds), part 1 (the offset) | JCT to score |
| LAB-11.06, 11.08 | Part 1, administration | Appropriated |
| LAB-11.09 | Part 1, conformity grant | R1 |
| LAB-11.10 | Part 2: zero once part 2's two authorities are added | Contingent |
| LAB-18.01, 18.02, 18.04, 18.05, 18.07 | Part 1, wage insurance; 18.02 also income tax | R1 |
| LAB-18.03 | Part 4, item 4 (quits, provisional); separations otherwise inside part 1 | — |
| LAB-18.06 | Part 1, the hours field | R1 |
| LAB-18.08 | Part 1, administration; part 4, item 7 | Provisional |
| LAB-8.01-8.04, 8.06, 8.07 | Part 1, apprenticeship | R1 |
| LAB-8.05 | No new money | Moves existing WIOA funds |
| LAB-9.01, 9.02, 9.04-9.06 | Part 1, civic service; part 3, the grantees' match (non-federal) | Authorization or R1 fallback |
| LAB-9.03 | Part 3, contingent | The gate |
| LAB-19.01-19.05 | Part 4, items 2 and 3 | Provisional |

## 6. Against outside scores

Each line checked against a published score or estimate. None is a score of this design: point 15 asks CBO and JCT for those.

| Line | This section | Outside figure (publisher, year, stake) | Verdict |
| --- | --- | --- | --- |
| The floor's indirect effect | About $32 billion over FY2030-39; $5.5 billion in FY2040 | CBO, 2021: +$54 billion over 2021-31 for $15 by 2025 [EV-WRK-032] | **Holds as scaled:** CBO's floor bit at about 61% of the median, memo 1 B's at about half |
| Organizing, penalties and the board | About zero; penalties a small gain | CBO, 2023: $4 million to run S. 567 [EV-WRK-189]; CBO, 2019: +$39 million of penalty revenue over ten years [EV-WRK-176] | **Holds** |
| The small-business credit | About $2.9 billion | JCT, 2007: the small-business package passed with the 2007 raise lost $7.1 billion over 2007-12 and $4.8 billion over 2007-17 [EV-WRK-445]; it was mostly the work opportunity credit and expensing, not a credit tied to the raise | **Supports the bottom-up figure's order of size**, far below $0.02-0.04 trillion; the precedent Espen pointed to is a few billion dollars (part 4, item 1) |
| Extended Benefits, ordinary years | About $48.5 billion over FY2031-39, at the standard's weekly benefits ($31 billion at today's) | OMB, FY2017 budget (Obama administration; its own proposal): $36.7 billion over 2017-26 for a fully federal program with new triggers, on a projection with no recession [EV-WRK-438] | **The anchor.** The figure was raised from a first estimate of $15 billion to match it at today's weekly benefits, then scaled by the standard's replacement factor (part 1). The triggers differ, so the line keeps a wide range ($15-107 billion) |
| UI modernization and administration | About $10 billion (administration and the conformity grant) | OMB, FY2017: $14.1 billion over 2017-26 to modernize UI and $1.8 billion for short-time compensation [EV-WRK-438] | **Same order.** OMB's modernization paid states to adopt standards; memo 7 B requires them and pays for systems |
| The wage base and solvency | Trust funds matched over the cycle; FUTA's own receipts about $0.5-1.5 billion a year | CBO, 2018 options: a $40,000 base, indexed, with the net rate cut to 0.167%, raises $18 billion over 2019-28, mostly through state taxes in the first years [EV-WRK-435]. OMB, FY2017: solvency receipts of $46.3 billion over 2017-26, which made the whole UI package cost only $1.1 billion net over ten years [EV-WRK-439] | **Qualifies the presentation.** The scorekeepers count state UI taxes as federal revenue, and state accounts are on the budget [EV-WRK-436]. So a score in the window will show a net revenue gain while states rebuild reserves, where part 2 shows the trust funds net to zero over the cycle. The general-fund lines are unaffected |
| The UI systems grant | $1.5 billion over FY2030-32 | The 2021 rescue act: $2 billion for fraud prevention, equitable access and timely payment [EV-WRK-434]; the 2009 recovery act: $7 billion of incentive payments and $0.5 billion for administration [EV-WRK-433] | **Holds**, near ARPA's scale |
| Wage insurance | About $2.0 billion a year in steady state (FY2034) and $2.5 billion in FY2040; $16 billion over FY2031-39 | OMB, FY2017: $11.2 billion over 2017-26, $1.5 billion in 2026 [EV-WRK-437], for up to $10,000 over two years for new jobs under $50,000 [EV-WRK-440]. Kletzer and Litan (Peterson Institute and Brookings, 2001): about $3-3.5 billion a year in 1999 dollars, with a health subsidy [EV-WRK-443]. Jacobson, LaLonde and Sullivan (Hamilton Project, 2011): about $15 billion a year for a broader design [EV-WRK-444]. CBO, 2015: trade adjustment's version, +$0.4 billion over 2015-25 [EV-WRK-441] | **Holds, toward the low side.** LAB-18 allows $10,000 a year, twice OMB's cap, so up to twice OMB's mature year in nominal dollars would be expected at the same reach; the steady state is about 1.4 times it, because the three-year tenure test, the pay cap and the 12-month window narrow who qualifies. It sits below Kletzer-Litan, which added a health subsidy, and far below Jacobson-LaLonde-Sullivan's broader design. The last two share an author, so they are one view, not two |
| Apprenticeship | About $34 billion over FY2030-39 | CBO, 2020: $3.1 billion over five years for the National Apprenticeship Act's authorizations [EV-WRK-396] | **Larger by design**, per apprentice (memo 8) |
| National service | About $49 billion civic; $60 billion with the tranche (federal); grantees' match about $13 billion more, non-federal | CBO, 2009, as reported by the NonProfit Times: about $5.7 billion over 2010-14 for the Serve America Act [EV-WRK-446], whose plan to reach 250,000 positions by FY2017 [EV-WRK-447] was never funded; legacy LAB-9B: about $0.05 trillion for 150,000 [EV-WRK-709] | **Holds** against the legacy figure; the 2009 law shows that authorization alone does not fund the positions, which is why LAB-9.06's fallback is in R1 |

**What has no outside score:** the credit's own design; the UI standards in the 2025 bill (S. 2312, no CBO or JCT score found); the tax offset on employers' UI taxes; the boards; and the trigger.

## 7. Against the booked rows

The budget model books three work rows and one AI row (case `mixed`, $ billion):

| Row | Booked FY2030-39 | Booked FY2040 | This section | Change a booking would make |
| --- | --- | --- | --- | --- |
| LAB-5, the legacy credit | 99.9 | 0 | 2.9 and 0 (LAB-5.01) | −97.0 over the decade |
| LAB-8, apprenticeships | 29.9 | 3.8 | 33.6 and 4.9 | +3.7 and +1.1 |
| LAB-9, national service | 120.1 | 16.8 | 49.0 and 6.7 civic; 60.3 and 9.4 with the tranche | −71.1 and −10.1 (−59.8 and −7.4 with the tranche) |
| LAB-1, the labor bill | 0 | 0 | the floor's indirect effect, 32.0 and 5.5 | +32 and +5.5 |
| Not booked: UI, wage insurance, the 14(c) grant, boards, outreach, revenue effects | — | — | 105.7 and 14.1 (part 1, the other lines) | +106 and +14.1 |
| **Work's rows** | **249.9** | **20.6** | **223.2 and 31.3** (firm) | **−27 and +10.7** (firm); −15 and +13.3 with the tranche |
| AI-4, AI and work (the AI topic's) | 200.0 | 29.5 | Its wage-insurance part is LAB-18 here (part 3) | To re-scope with the AI topic (part 9) |

- **Why the decade falls and FY2040 rises.** The legacy credit ($100 billion) and the legacy universal service row ($120 billion at 250,000 slots [EV-WRK-705]) drop to the decided designs. Unemployment insurance, wage insurance and the floor's indirect effect were never booked, and they are permanent, so FY2040 rises.
- **The legacy labor file's own total** was $0.25 trillion (0.13-0.41) [EV-WRK-708], which matches the booked rows. The decided set is smaller over the decade and different in kind.

## 8. The fiscal-rule report

One basis: federal fiscal years, $ billion, a cost positive, the general fund's primary balance, against what the budget model books (case `mixed`).

| Measure | FY2030-39 | FY2040 (permanent) |
| --- | --- | --- |
| Work on the general fund, firm lines (part 1) | about **+$223.2 billion** (range +$102 to +$442 billion) | about **+$31.3 billion** (0.058% of GDP; range $14-57 billion) |
| *of which:* spending lines | +$163.3 billion | +$22.3 billion |
| *of which:* revenue effects (the credit, the UI tax offset, income tax on wage insurance, penalties) | +$27.9 billion | +$3.4 billion |
| *of which:* the floor's indirect effect (CBO's net) | +$32.0 billion | +$5.5 billion |
| Contingent: the service tranche | 0 to +$12.8 billion (+$11.3 billion if the gate opens on the working ramp) | 0 to +$3.0 billion (+$2.7 billion) |
| Contingent: Extended Benefits in a downturn | 0 to about +$120 billion | zero in the projection |
| Provisional (part 4): quits and the measure; the trigger | +$1.8 billion; the trigger 0 to +$25 billion | +$0.2 billion; the trigger 0 to +$5 billion |
| Booked for the same purposes: LAB-5, LAB-8, LAB-9 | $249.9 billion | $20.6 billion |
| **Net change a booking would make (firm)** | **about −$27 billion** | **about +$10.7 billion** |
| Net change with the tranche | about −$15 billion | about +$13.3 billion |
| UI trust funds (part 2) | benefits +$541 billion, matched by employers' state taxes | +$74 billion, matched |
| Social Security's funds (part 2) | about −$43 billion | about −$6.0 billion |
| Not federal: AmeriCorps grantees' match (part 1) | about $13 billion | about $2.2 billion |

- **The yearly cost** (firm lines): about $4 billion in FY2030, $13 billion in FY2031, $19 billion in FY2032, rising to $26 billion in FY2035 and $31 billion in FY2040.
- **Permanent cost from FY2040:** about **$31 billion a year** on the general fund (about $34 billion with the tranche), growing with wages and prices. Wage insurance, unemployment insurance, apprenticeship, service and the floor's effect are permanent. The credit, the 14(c) grant, the conformity grant and the record fields end by FY2034.
- **Its share of the plan-wide margin.**
  - *The gap:* the plan-wide general-fund primary gap in FY2040 is **$602.7 billion short** (1.11% of GDP; `agenda_gf_primary_bn`, case `mixed`, on main after #402); a positive figure is a shortfall.
  - *Work's whole general-fund cost* in FY2040, $31.3 billion, is **about 5.2% of the gap**, or 5.6% with the tranche.
  - *A booking of the decided set* would replace $20.6 billion of booked work rows. It adds about **$10.7 billion, to about $613.4 billion short (1.13% of GDP): about 1.8% of the gap.** With the tranche it adds $13.3 billion (to $616.0 billion, 2.2% of the gap); with the provisional items too, $13.6 billion. Before the milestone fix a booking added $6.8 billion; the change is the unemployment benefit lines (Extended Benefits and the tax offset), less wage insurance.
  - *Over FY2030-39* a booking lowers the decade gap by about $27 billion (from $3,773.4 billion to about $3,746.7 billion), because the booked legacy credit and service row are larger than the decided designs.
  - *AI-4:* if the AI topic re-scopes AI-4 so that its wage-insurance part is carried here, the plan-wide figure falls by that part, up to about $3 billion in FY2040. Its size inside AI-4 is not split in the ledger (part 3).
  - *Basis:* additive on the primary balance before interest, like every dossier's report.
- **The test years.** Nothing sunsets after FY2034, and the floor's indirect effect, unemployment insurance and wage insurance grow with wages. Without the floor's indirect effect, which is CBO's net and the least certain line, FY2040 is about $25.8 billion.
- **Report, don't gate** (`DEC-2026-11-10-05`). Work's FY2040 share is a figure for the financing settlement, not a defect to fix. Two choices here are mainly about money, so they go to Espen: the credit's size (part 4, item 1) and, after the milestone fix, the unemployment standard's cost to employers ("Questions for Espen", item 1). The second moves the general fund by only a few billion dollars a year; it is a money question because the cost to employers is about twice what memo 7 showed.

## 9. What a booking would change (proposed, not made)

Tier 3, for the lead after the milestone review (`charter/STANDARDS.md`, "Milestone review": book once, after the fixes). This PR changes nothing in `models/data/inputs/`. The rows below are low / mid / high over FY2030-39 in $ trillion, from `tools/work_path.py` (`booking_rows()`), with FY2040 in $ billion. Year shapes go in `fiscal-years.csv` from the same tool.

| Row | Lines | Low / mid / high, FY2030-39 ($T) | FY2040 ($B) |
| --- | --- | --- | --- |
| LAB-4 indirect (DY4 or LAB-1) | The floor's indirect effect | 0.000 / 0.032 / 0.080 | 5.5 |
| LAB-5 | The credit (revenue row) | 0.001 / 0.003 / 0.007 | 0.0 |
| LAB-4.09 | 14(c) grant | 0.001 / 0.002 / 0.003 | 0.0 |
| LAB-3 and 4.04 | Boards and commission (appropriated) | 0.001 / 0.001 / 0.003 | 0.15 |
| LAB-7.05 | Outreach (appropriated) | 0.000 / 0.001 / 0.001 | 0.06 |
| LAB-11 (general-fund spending) | Extended Benefits, administration, conformity grant | 0.023 / 0.059 / 0.122 | 7.8 |
| LAB-11 tax offset (revenue row) | The UI tax offset | 0.006 / 0.027 / 0.086 | 3.7 |
| LAB-18 (spending) | Wage insurance, its administration, the hours field | 0.009 / 0.018 / 0.030 | 2.7 |
| LAB-18 income tax (revenue row) | Income tax on wage insurance | -0.003 / -0.002 / -0.001 | -0.25 |
| Penalties (revenue row) | Civil penalties | -0.001 / 0.000 / 0.000 | -0.05 |
| LAB-8 | Apprenticeship | 0.024 / 0.034 / 0.054 | 4.9 |
| LAB-9 | Civic service | 0.042 / 0.049 / 0.056 | 6.7 |
| LAB-9.03 (contingent) | The tranche | 0.000 / 0.011 / 0.013 | 2.7 |

Further steps:
1. **`ledger-bills.csv`, line 38 (LAB-5, 0.05 / 0.10 / 0.15):** replace with LAB-5.01 at about 0.001 / 0.003 / 0.007 (provisional, part 4, item 1), as a revenue row with the trust funds made whole.
2. **Line 39 (LAB-8, 0.02 / 0.03 / 0.05):** to 0.024 / 0.034 / 0.054.
3. **Line 40 (LAB-9, 0.06 / 0.12 / 0.20):** to the civic line, 0.042 / 0.049 / 0.056, with the tranche as a contingent component (0 / 0.011 / 0.013). Move its rail from R2 to R1 (point 16), with the authorization as the regular-order route.
4. **New rows:** LAB-11's general-fund spending, LAB-18 with its administration and the hours field, the 14(c) grant, the boards and outreach (appropriated), and the revenue rows (the UI tax offset, income tax on wage insurance, penalties). Each goes on its own line, with spending and revenue apart.
5. **The floor's indirect effect:** a component of LAB-1, or a replacement for DY4's distributional row [EV-WRK-707], not both.
6. **The UI trust funds:** the funds model's state accounts and the federal accounts, if the model carries them. They stay off the general fund, and Social Security's payroll offset (about −$43 billion) goes on the funds model's payroll line.
7. **AI-4:** for the AI topic. Its row's wage-insurance part (wage insurance is "AI-4A's benefit", memo 8) is carried by LAB-18 and, if Espen chooses memo 10 C, LAB-19. The rest (training accounts) stays the AI topic's.
8. **CAP-7:** democratic renewal's section 5 has answered work's seven items: the NLRB fits inside the legacy row, which narrows to work's figure at stage G; FMCS, OSHA's high end, the apprenticeship registration staff and the FLRA are claims on the delivery contingency; the conformity grant stays on work's own R1 line, counted once there (part 1); the UI identity match (LAB-11.06) is a data agreement that may draw on CAP-13 for the state side. Nothing to book here.
9. **Rails:** the money moves to R1 (point 16). The budget model books LAB-5, LAB-8 and LAB-9 on R2 today.

## 10. What each figure is

| Input | Treatment (`DEC-2026-11-10-07`) |
| --- | --- |
| The floor's schedule; the credit's form, shares and cap; the subminimums' end; the UI standards and Extended Benefits' triggers and share; wage insurance's eligibility, benefit and four rules; the apprenticeship line's payment rules and target; national service's scale and gate | Commitments (decided) |
| The floor's indirect effect (CBO's 2021 pattern scaled to a smaller bite) | Working assumption: central $5.5 billion in FY2040, range zero to $8 billion; CBO's score of memo 1 B (point 15) replaces it |
| The credit's added wage cost by step | Working assumption, bottom-up (part 1); JCT scores it (point 15) |
| The trust funds' benefit increase (about 2.1 times today's regular benefits, range 1.7-2.7: +$42 billion a year at FY2025 levels, range $25-66 billion) | Working assumption derived from LAB-11.01's standard in four factors (part 2) [EV-WRK-302] [EV-WRK-451] [EV-WRK-453] [EV-WRK-368] [EV-WRK-370]; the replacement rate itself is a commitment (decided, 75% up to two-thirds of the state average wage). Studied in implementation from the claims and benefit amounts states already report |
| Extended Benefits' weekly amount (scaled by the standard's replacement factor, 1.58) | Working assumption: each Extended Benefits week pays the regular weekly amount; the number of weeks is held |
| Extended Benefits in ordinary years | Working assumption ($1-6 billion a year in 2031), anchored on OMB's FY2017 score [EV-WRK-438]; the states' unemployment rates to add to the register |
| Extended Benefits in a downturn | Contingent; zero in the projection, about $120 billion (range about $100-150 billion) in a moderate two-year downturn at the standard's benefit levels |
| UI administration's workload | Working assumption ($0.2-0.8 billion a year) |
| The tax offset's general-fund share (5%, range 2-10%) | Working assumption on the scorekeepers' 25% convention; JCT scores it with the wage base (point 15) |
| Wage insurance's take-up (60%) and reemployment within a year (60%) | Working assumptions; no take-up rate among eligible workers is in the register (TAA's 11% is a share of all participants, not a take-up rate [EV-WRK-332]); studied in implementation from the first two years' state counts (section 5, part 8) |
| Wage insurance's discharges not for misconduct (15% more eligible separations, range 5-30%) | Working assumption; no register entry counts them. Studied in implementation from the states' separation findings (LAB-18.03) |
| Wage insurance's administration (10%) | Working assumption on state UI's ratio [EV-WRK-309] [EV-WRK-413] |
| Apprenticeship's funded share (55% of today's starts) and attrition (75% retained, 45% complete) | Working assumptions; completion from [EV-WRK-350]; studied in implementation from the records programs file (LAB-8.04) |
| National service's cost per position | Working assumption on AmeriCorps' rules [EV-WRK-398] [EV-WRK-399] |
| The grantees' match (24% rising to 30%; about $13 billion over FY2030-39, not federal) | Working assumption written into LAB-9.01: today's rule applies to the new positions [EV-WRK-454]. The alternative, waiving or federalizing it, adds the same amount to federal cost |
| The tranche's opening year (2035) | Working assumption from the ramp; the gate decides it |
| The boards' number and cost | Working assumption; open whether more than a few boards are convened |
| Home care's Medicaid cost | Open: turns on whether the 2013 rule stands in January 2029 |
| LAB-11.10's channel | Open: needs a new authorization (part 2) |
| The credit's size, the trigger, the measure, good-cause quits, the territories' floor, the monthly statement | Provisional, for Espen (part 4) |
| Growth rates (wages 3.5%, prices 2.5%, UI benefits 4%) | Working assumptions |

## Evidence still needed

- CBO and JCT scores of memo 1 B, memo 3 as decided, memo 7 B, the credit (LAB-5.01) and the wage-base schedule (LAB-11.05) with its offsets, on the 2029 baseline (point 15).
- **GAO's reports on American Samoa's minimum wage** (LAB-4.10; the reviewer's first note on #428). The statute the dossier saved, `library/text/wrk-5-usc-29-206-minimum-wage.txt`, lines 676-720, directs GAO to report on the impact of the increases by April 1, 2017 and April 1, 2020, and on alternative ways to raise the wage within a year of October 7, 2015. GAO reported under that mandate in 2010, 2011, 2014, 2016 and 2020 [EV-WRK-448] [EV-WRK-449]: GAO-10-333 (April 8, 2010), GAO-11-427 (June 23, 2011), GAO-14-381 (March 31, 2014), GAO-17-83, *American Samoa: Alternatives for Raising Minimum Wages to Keep Pace with the Cost of Living and Reach the Federal Level* (December 2, 2016, the alternatives report, which also served for 2017), and GAO-20-467, *American Samoa: Economic Trends, Status of the Tuna Canning Industry, and Stakeholders' Views on Minimum Wage Increases* (June 11, 2020). GAO-17-83's findings and GAO-20-467's highlights are now read and in the register [EV-WRK-472] [EV-WRK-473] (milestone fix step 2); the full reports are not (GAO blocks downloads; an upload from Espen or a hand check).
- The states' unemployment rates over a recent cycle, to size Extended Benefits' ordinary-year cost (BLS's local area unemployment statistics).
- The appropriations acts' automatic administrative funding per 100,000 insured unemployed, for the workload line.
- The distribution of UI claimants' weekly wages against their state's average weekly wage (DOL's benefit accuracy measurement data), to replace the lognormal assumption behind the standard's replacement factor (part 2); and first payments and weeks in states that adopted broader eligibility, for the claimant factor.
- A count of long-tenured workers discharged not for misconduct (DOL's nonmonetary determination reports), for wage insurance's discharge factor.
- A take-up rate for trade adjustment's wage insurance among workers eligible for it (Labor's TAA participant data), to benchmark the 60%.
- A count of quits found for good cause attributable to the employer (Labor's benefit accuracy data), for LAB-18.03.
- The 2021 contractor minimum wage rule's regulatory analysis (LAB-4.05), and the 2013 home care rule's (LAB-12.01).
- The four sectors' share of registered apprenticeship starts, from Labor's apprenticeship data.
- CBO's own estimate of the Serve America Act (2009): the figure here is a press report of it [EV-WRK-446].
- CBO's 2018 FUTA option, read from a verbatim copy on a third-party site; to check against cbo.gov [EV-WRK-435] [EV-WRK-436].
- Independent corroboration of OMB's FY2017 UI scores [EV-WRK-438] and of CBO's FUTA option [EV-WRK-435] and trade adjustment estimate [EV-WRK-442]; each is one publisher's analysis until then.
- Authority for states to pay federal benefits for federal workers and veterans as Labor's agents (the model for LAB-11.10's agreement), not yet in the register.

## Questions for Espen

New from the milestone fix (provisional: drafted on the recommendation, not decided; review O-1 and A-3, `review-milestone.md`, "For Espen", question 1):
1. **The unemployment standard's cost to employers** (LAB-11.01, memo 7 B, `DEC-2026-11-17-10`). You chose memo 7 B seeing regular benefits rise about $15-25 billion a year. As specified (75% of pay up to two-thirds of the state's average weekly wage), they rise about **$42 billion a year at FY2025 levels (range $25-66 billion)**, about twice as much: roughly $275 more a covered worker a year, paid by employers through state UI taxes, which about double (part 2). The general fund changes far less, about $4 billion a year by FY2040. Keep the standard from 2031, or phase it in? Each option below is priced in `tools/work_path.py --ui-options` on part 2's basis ($ billion; the general fund column is the two lines that move with the rate, Extended Benefits in ordinary years and the tax offset; administration and the conformity grant do not change):

   | Option | Trust funds, FY2031-39 (employers) | Trust funds, FY2040 | General fund, FY2030-39 | General fund, FY2040 | Social Security, FY2030-39 | Permanent, a year at FY2025 levels |
   | --- | --- | --- | --- | --- | --- | --- |
   | **A. Keep 75% from 2031, as decided (recommended)** | 541 (324-858) | 74.5 | 75.6 | 10.4 | −43.3 | +42 (25-66) |
   | B. Phase in with the wage base: 60% in 2031, 65% in 2032, 70% in 2033, 75% from 2034 | 506 (300-810) | 74.5 | 72.5 | 10.4 | −40.5 | +42 (25-66) |
   | C. The review's example: 50% in 2031, rising about 3 points a year to 75% in 2039 | 394 (221-654) | 74.5 | 62.5 | 10.4 | −31.5 | +42 (25-66) |
   | D. Hold the rate at 60% of high-quarter pay, with the same two-thirds cap | 361 (198-609) | 49.7 | 59.7 | 8.2 | −28.9 | +28 (15-47) |

   - *Recommended: A, keep the decided standard from 2031.* The general fund differs by at most about $2 billion a year among the options. B saves employers about $35 billion over nine years (about 6%) and nothing after 2034, while making states program the formula four times. C saves about $150 billion but leaves the decided standard unreached until 2039 for most of the plan's first decade. The larger base (LAB-11.05) and interest-free loans for solvent states are the decided way to pay for it, and the solvency trigger (`7-validation.md`, part 7) is the check. Memo 7's evidence is that benefit length protects families' spending four times as much as benefit level (Ganong and Noel, *American Economic Review*) [EV-WRK-372], so if you want a lower cost, D is the option that follows memo 7's own rule ("narrow the replacement rate first, keep length"): it keeps 26 weeks and the cap, and lowers the permanent cost by about a third.
   - *What stays the same in every option:* 26 weeks, the coverage rules, Extended Benefits and the wage base. Every figure is project arithmetic on part 2's factors, not a score; CBO's score (point 15) replaces it.

Also new in this section:
2. **The small-business credit's size** (LAB-5.01): as specified it costs about $3 billion, not the $0.02-0.04 trillion you saw. Recommended: keep it as specified (small and temporary, as you asked); the alternative is to widen it to five steps or every employer (part 4, item 1). This choice is mainly about money.

Carried from sections 4 and 5, each priced here on its recommendation and still provisional:
3. Memo 10, measuring displacement and a standby trigger (LAB-19): about $0.5 billion for the measure; the trigger is zero while off, up to $5 billion a year when on.
4. Point 5, severance (LAB-14.01): no cost on the recommendation.
5. Point 11, codetermination (LAB-17.01): no cost on the recommendation.
6. Wage insurance and quits for good cause (LAB-18.03): about $1.2 billion over FY2030-39.
7. The territories' wage floor (LAB-4.10, revised in fix step 2; question in `4-specification.md`, item 5): no federal cost to speak of under any option; recommended, the national schedule capped at 75% of each territory's median.
8. Wage insurance's monthly statement (LAB-18.08): inside administration; the alternatives cost about the same.
