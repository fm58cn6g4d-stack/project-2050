# Fair pay and real power at work: cost

Role: section 6 of the work dossier (flagship 5). It prices every provision of `4-specification.md` and `5-delivery.md` (84 in `provisions.json`) on federal fiscal years against the January 2029 law. It reports the fiscal-rule effect to the financing settlement (`charter/STANDARDS.md`, "Fiscal rule in dossiers: report, don't gate", `DEC-2026-11-10-05`). Status: **draft** (stage F), on `DEC-2026-11-17-01` to `-36`, `-95` and `-96`. Every figure is project arithmetic or judgment on outside anchors, not an official score; point 15 (`DEC-2026-11-17-28`) asks CBO and JCT for scores in 2027-28. **Nothing is booked here.** Booking follows the milestone review (`charter/STANDARDS.md`, "Milestone review"), and part 9 lists the ledger rows a booking would change. Items still with Espen are priced on their recommendations and marked **provisional** (part 4).

## Counting rules

- **Conventions.** Federal cost in nominal $ billion unless marked, against the January 2029 law, a cost positive. FY y runs from October of y-1. A calendar-year amount lands three-quarters in its own fiscal year and a quarter in the next, as care's, health's and the secure floor's paths count.
- **The path.** `tools/work_path.py` lays every line on FY2030-40, with a central, low and high path. Run `python3 dossiers/work/tools/work_path.py` for the tables, `--parts` for this section's blocks and `--check` for the coverage test: every one of the 84 provisions is on a line or listed with its reason for having none (part 5). Its anchors are evidence IDs or labeled judgment, in its comments and below. Ranges are bounds: they put each line's inputs at their low or high values and sum line by line. They are not probability intervals, and the lines are not independent.
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
| Extended Benefits, federal share, ordinary years | LAB-11.04 | 0.0 | 2.2 | 3.1 | 3.2 | 3.3 | 3.5 | 3.6 | 3.8 | 3.9 | 4.1 | **30.7** | **4.2** | 10.2 to 61.4 | 1.4 to 8.5 |
| State UI administration: the floor and the larger program's workload | LAB-11.06, LAB-11.08 | 0.42 | 0.73 | 0.85 | 0.88 | 0.91 | 0.94 | 0.97 | 1.00 | 1.0 | 1.1 | **8.8** | **1.1** | 6.7 to 12.9 | 0.82 to 1.7 |
| UI conformity and systems grant | LAB-11.09 | 0.50 | 0.50 | 0.50 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | **1.5** | **0.0** | 1.0 to 2.0 | 0.0 to 0.0 |
| Hours in state wage records, one-time grant | LAB-18.06 | 0.0 | 0.05 | 0.10 | 0.05 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | **0.20** | **0.0** | 0.10 to 0.40 | 0.0 to 0.0 |
| Wage insurance benefits | LAB-18.01, LAB-18.02, LAB-18.04, LAB-18.05, LAB-18.07 | 0.0 | 0.20 | 1.4 | 2.4 | 2.5 | 2.5 | 2.6 | 2.7 | 2.8 | 2.9 | **20.0** | **3.0** | 10.0 to 32.0 | 1.5 to 4.7 |
| Wage insurance administration, including the monthly statement | LAB-18.08 | 0.15 | 0.17 | 0.14 | 0.24 | 0.25 | 0.25 | 0.26 | 0.27 | 0.28 | 0.29 | **2.3** | **0.30** | 1.00 to 4.2 | 0.12 to 0.57 |
| Apprenticeship grants: instalments, completion, instructors, supports | LAB-8.01, LAB-8.02, LAB-8.03, LAB-8.04, LAB-8.06, LAB-8.07 | 0.87 | 1.8 | 2.2 | 3.1 | 3.6 | 4.0 | 4.2 | 4.5 | 4.6 | 4.8 | **33.6** | **4.9** | 23.6 to 53.8 | 3.4 to 7.9 |
| National service: 150,000 more civic positions | LAB-9.01, LAB-9.02, LAB-9.04, LAB-9.05, LAB-9.06 | 1.1 | 2.2 | 3.4 | 4.7 | 5.9 | 6.1 | 6.2 | 6.3 | 6.4 | 6.6 | **49.0** | **6.7** | 41.6 to 56.3 | 5.7 to 7.7 |
| **Spending lines** | | **3.5** | **8.4** | **12.2** | **15.0** | **17.1** | **17.5** | **18.1** | **18.7** | **19.3** | **19.8** | **149.7** | **20.4** | **96.2 to 230.2** | **13.1 to 31.5** |
| Small-business transition credit, first three steps (revenue effect) | LAB-5.01 | 0.38 | 1.0 | 1.2 | 0.30 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | **2.9** | **0.0** | 1.5 to 7.3 | 0.0 to 0.0 |
| Income-tax offset on employers' larger UI taxes, net of tax on benefits | LAB-11.05 | 0.0 | 0.95 | 1.3 | 1.4 | 1.4 | 1.5 | 1.5 | 1.6 | 1.6 | 1.7 | **13.0** | **1.8** | 3.9 to 32.4 | 0.54 to 4.5 |
| Income tax on wage insurance payments (receipts) | LAB-18.02 | 0.0 | -0.02 | -0.14 | -0.24 | -0.25 | -0.25 | -0.26 | -0.27 | -0.28 | -0.29 | **-2.0** | **-0.30** | -3.8 to -0.80 | -0.57 to -0.12 |
| Civil penalties under the labor act and wage law (receipts) | LAB-2.01, LAB-7.04, LAB-13.01 | 0.0 | -0.05 | -0.05 | -0.05 | -0.05 | -0.05 | -0.05 | -0.05 | -0.05 | -0.05 | **-0.45** | **-0.05** | -1.4 to -0.09 | -0.15 to -0.01 |
| **Revenue effects** | | **0.38** | **1.9** | **2.3** | **1.4** | **1.1** | **1.2** | **1.2** | **1.3** | **1.3** | **1.4** | **13.4** | **1.4** | **0.16 to 38.8** | **-0.18 to 4.3** |
| The wage floor's indirect effect on the budget (CBO's net method) | LAB-4.01, LAB-4.02, LAB-4.03, LAB-4.06, LAB-4.07, LAB-4.08 | 0.30 | 0.80 | 1.5 | 2.3 | 3.2 | 4.0 | 4.6 | 4.9 | 5.1 | 5.3 | **32.0** | **5.5** | 0.0 to 80.0 | 0.0 to 8.0 |
| **Work on the general fund, firm lines** | | **4.2** | **11.2** | **16.1** | **18.7** | **21.4** | **22.6** | **23.9** | **24.9** | **25.7** | **26.5** | **195.1** | **27.4** | **96.3 to 349.0** | **12.9 to 43.9** |

- **The decided set, firm lines:** about **+$0.20 trillion over FY2030-39 (range about +$0.10 to +$0.35 trillion) and about +$27 billion in FY2040 (range about $13-44 billion)** on the general fund. Of the FY2040 figure, spending lines are $20.4 billion, revenue effects $1.4 billion and the floor's indirect effect $5.5 billion.
- **With the service tranche** (contingent on its gate, part 3): about +$0.21 trillion and +$30.0 billion. **With the provisional items** on their recommendations (part 4): about +$2 billion more over the decade and +$0.3 billion in FY2040; the standby trigger adds up to $5 billion a year when on, from about 2035.
- **Against section 4's decided set** (+$0.18-0.38 trillion and +$19-35 billion), the decade sits at the low end and FY2040 near the middle. What moved, line by line:
  - *The credit* (LAB-5.01): about $3 billion, not $20-40 billion (below and part 4, item 1).
  - *Unemployment insurance:* the recession average moves to a contingent line (part 2). The firm general-fund spending is about $41 billion over FY2030-39. Two lines are new: the administration of the larger program's workload, about $4 billion, and the general fund's tax offset on employers' larger UI taxes, about $13 billion (part 2).
  - *Apprenticeship* (LAB-8): about $0.034 trillion, below section 4's $0.04-0.07 trillion, once the decided payment rules and attrition are counted (below).
  - *Wage insurance* (LAB-18): about $20 billion of benefits, at the low end of memo 8's range, plus about $2.3 billion of administration, a line section 5 added and memo 8's figure did not include (below).
  - *National service* (LAB-9): the decade is unchanged ($0.049 trillion civic, $0.060 trillion with the tranche). FY2040 is about $6.7 billion civic and $9.4 billion with the tranche, above the note's $7-8.5 billion, which was not in FY2040 dollars (below).
  - *The boards and the commission:* about $1 billion over the decade and $0.15 billion in FY2040, at the low end of section 3's $1-3 billion (below).

**The basis of each line.** Judgment unless marked. Every anchor is in section 3, "What the options cost", or cited here.
- **The credit (LAB-5.01), re-derived bottom-up from the specification.** It pays a share of each step's added wage cost for the four quarters after the step, only for workers paid below the step's rate, and only at employers under 50 workers. The steps reach workers mostly where the federal floor binds: the 12 states at $7.25 [EV-WRK-013] and those with no minimum or a lower one. By 2030-32 even $12.50 sits far below the all-jobs median of about $29-31 an hour (project arithmetic on [EV-WRK-078] at 3.5% a year). The added wage cost at small employers comes to about $1.0 billion for the first step, $3.5 billion for the second and $6.0 billion for the third (judgment: workers below each step, about 40% of them at small employers). At 50%, 35% and 20%, the credit comes to about **$2.9 billion over FY2030-33 (range $1.5-7.3 billion)**, claimed on the quarterly Form 941. The $20,000 cap rarely binds at these amounts. Section 4's $0.02-0.04 trillion was memo 1's judgment, "a third of the legacy credit's range" [EV-WRK-703], set before the credit's form was decided (`DEC-2026-11-17-34`). That legacy credit was built for a $17 floor phased in over eight years, and the decided credit covers three steps and the new increment only. The provision as written is priced here. Whether to keep it at this size is put to Espen (part 4, item 1). *Basis note:* a credit against the employer's share of payroll tax would reduce Social Security's and Medicare's receipts. The specification should say that the general fund makes the trust funds whole, as it did for the 2020-21 payroll credits (working assumption, to add to LAB-5.01 at the next touch). It is priced here as a general-fund revenue effect.
- **The floor's indirect effect (memo 1 B).** CBO put $15 by 2025 at +$54 billion over 2021-31 [EV-WRK-032], a floor at about 61% of 2025's median [EV-WRK-078]. Memo 1 B's $17 is about half the median in 2035. CBO's figure nets higher federal costs (prices of what the government buys, unemployment compensation) against higher revenue and lower income support. Scaled to the smaller bite and the later steps, it is about $32 billion over FY2030-39 and $5.5 billion in FY2040, with section 3's range kept (zero to +$0.08 trillion; $3-8 billion in FY2040, widened to zero at the low end because the sign of a smaller bite's effect is not tested). The budget model carries the floor at zero (LAB-1) and in its distributional row DY4 [EV-WRK-707].
- **Extended Benefits, ordinary years (LAB-11.04).** Under the January 2029 law the federal half of Extended Benefits rarely triggers. The new triggers include a state's own three-month rate at 5.5%. Some states sit near that rate in ordinary years, so with a 100% federal share the program pays in a few states even without a recession: about $3 billion in calendar 2031 (range $1-6 billion), growing with benefits. That is $31 billion over FY2031-39 and $4.2 billion in FY2040 (judgment). OMB scored the FY2017 budget's Extended Benefits reform, fully federal with new triggers, at $36.7 billion over 2017-26 on a projection with no recession, about $3.7 billion a year (OMB, FY2017 budget, Obama administration, 2016) [EV-WRK-438]; it is the anchor here. The states' unemployment rates are not yet in the register ("Evidence still needed").
- **State UI administration (LAB-11.06, 11.08).** The floor restores about $0.38 billion a year above FY2026's $2.76 billion [EV-WRK-309] [EV-WRK-308], indexed. Section 5 said the floor "pays for running the larger program". This section adds the larger program's workload: about 40% more recipients need more claims-taking, adjudication and appeals. That is about $0.4 billion a year from 2031 (range $0.2-0.8 billion; judgment). The appropriations acts already add administrative money automatically when claims rise above a base, and that mechanism would carry it (the rate per 100,000 claimants is not yet in the register). Both are appropriated from the administration account that FUTA finances [EV-WRK-310]. They are counted on the general fund here, as memo 7 counted them, which is the cautious reading (part 2).
- **The conformity grant (LAB-11.09)** is section 5's $1-2 billion over FY2030-32. **The hours field (LAB-18.06)** is the decided part of section 5's $0.2-0.5 billion one-time grant for new wage-record fields, about $0.2 billion. The occupation part is memo 10's (part 4).
- **Wage insurance (LAB-18.01-18.05, 18.07), re-derived.** Separations count from January 1, 2031, and payments start on reemployment within 12 months and last up to two years. In steady state:
  - about 1.1 million long-tenured workers are displaced a year (3.3 million over 2023-25) [EV-WRK-315];
  - about 88% earned under the cap of twice the median (judgment);
  - about 60% are reemployed within a year (66.1% were reemployed by the survey date) [EV-WRK-315];
  - about half of those are paid less (49% of the full-time reemployed earned as much or more) [EV-WRK-317];
  - about 60% take it up with the automatic offer on the claim form (judgment; TAA's documented route reached 11% [EV-WRK-332]).

  That is about 0.17 million new recipients a year, each paid for about 1.6 years at about $6,000-6,500 a year: **about $2.4 billion in FY2033, rising about 3% a year**, because the $10,000 cap is fixed until 2035 (LAB-18.02). That is $20 billion over FY2031-39 (range $10-32 billion) and $3.0 billion in FY2040. Memo 8's $2-4 billion a year counted every reemployed worker paid less, at full take-up, without the 12-month window. This figure sits at that range's low end. The two-year overlap of cohorts puts about 0.27 million on the rolls at a time, near the low end of section 5's 0.3-0.6 million. *Clean power's guarantee comes first* (LAB-18.07): about 8,000 covered layoffs a year (`dossiers/clean-power/5-delivery.md`, part 2), too few to move the line.
- **Wage insurance administration (LAB-18.08's monthly statement included)** is about 10% of benefits (range 8-12%), the ratio of state UI administration to pre-pandemic unemployment outlays ($3.14 billion against $29.9 billion) [EV-WRK-309] [EV-WRK-413], plus about $0.15 billion of set-up in each of FY2030 and FY2031. Section 5 asked whether memo 8's $2-4 billion already included it. It did not: memo 8's basis is a count of workers times an average payment. So administration is its own line, about $2.3 billion over FY2030-39 and $0.3 billion in FY2040 (range $0.1-0.6 billion). That is at the low end of section 5's $0.2-0.4 billion because the benefit line is lower.
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

  That is about **$49 billion over FY2030-39 and $6.7 billion in FY2040** (range ±15%). The note's $7-8.5 billion in FY2040 (`notes/espen-questions-2026-11-17.md`, part e) used today's costs. In FY2040 dollars the decided 200,000 cost about $9.4 billion with the tranche (part 3). The decade figure, $0.060 trillion with the tranche, sits inside `DEC-2026-11-17-32`'s $0.04-0.065 trillion. Whichever route funds it, the authorization (appropriated) or R1's fallback (direct spending, LAB-9.06), the cost is the same. The route decides only whether it is mandatory or subject to appropriation.
- **The 14(c) grant (LAB-4.09)** is section 4's $1-3 billion, spread evenly over FY2030-34.
- **The boards office and the commission (LAB-3.01-3.04, 4.04)** are built bottom-up:
  - the commission's staff, about $15 million a year;
  - a boards office of 100-200 staff at about $0.25 million a staff year;
  - about $5-10 million a year for each board's hearings, one board from 2030 rising to about ten by the late 2030s.

  That is about $1.0 billion over FY2030-39 and $0.15 billion in FY2040, appropriated. Section 3's $1-3 billion and $0.2-0.4 billion are kept as the range. Enforcing the boards' standards is Wage and Hour's work, counted in CAP-7.
- **Outreach grants (LAB-7.05)** are section 4's $50 million a year, indexed, appropriated.
- **Revenue effects.**
  - *The UI tax offset.* Employers' larger UI taxes lower taxable wages. Under the scorekeepers' convention about a quarter of a new employer tax comes back as lower income and payroll tax. About 15 points of that falls on income tax, and about 10 points return as income tax on the larger, taxable benefits. So about 5% of the tax increase is a general-fund loss: about $13 billion over FY2030-39 and $1.8 billion in FY2040 (range 2-10%; judgment). The payroll part, about 8%, falls on Social Security (part 2). JCT would score this with the wage base (point 15).
  - *Income tax on wage insurance:* the payments are taxable as wages (INC-5.01), at about 10%, a gain of about $2 billion over FY2030-39.
  - *Civil penalties:* CBO put the 2019 bill's labor-board penalties at $39 million over ten years [EV-WRK-176]. The wage-law penalties add more once there are 1,200 investigators. In all about $50 million a year in receipts (judgment).

## 2. Unemployment insurance on each budget

The UI system is a federal-state trust fund on the federal budget. State benefits and employers' state taxes both pass through the Unemployment Trust Fund, and the federal accounts are financed by the federal unemployment tax (FUTA) [EV-WRK-310]. Memo 7 B changes all three: the state accounts, the federal accounts and the general fund.

| Line | Provisions | 2030 | 2031 | 2032 | 2033 | 2034 | 2035 | 2036 | 2037 | 2038 | 2039 | **FY2030-39** | **2040** | Range FY2030-39 | Range 2040 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| UI regular benefits from the state trust funds (employer-financed) | LAB-11.01, LAB-11.02, LAB-11.03, LAB-11.07 | 0.0 | 19.0 | 26.1 | 27.1 | 28.2 | 29.3 | 30.5 | 31.7 | 33.0 | 34.3 | **259.2** | **35.7** | 194.4 to 323.9 | 26.8 to 44.6 |
| Employers' state UI taxes on the larger base (receipts, matching the benefits) | LAB-11.05 | 0.0 | -19.0 | -26.1 | -27.1 | -28.2 | -29.3 | -30.5 | -31.7 | -33.0 | -34.3 | **-259.2** | **-35.7** | -323.9 to -194.4 | -44.6 to -26.8 |
| Payroll-tax offset on employers' larger UI taxes (Social Security) | LAB-11.05 | 0.0 | 1.5 | 2.1 | 2.2 | 2.3 | 2.3 | 2.4 | 2.5 | 2.6 | 2.7 | **20.7** | **2.9** | 9.7 to 32.4 | 1.3 to 4.5 |

- **The trust funds' side: about $15-25 billion a year at FY2025 levels, employer-financed, on its own line.** Regular benefits rise about 40-60% in an ordinary year (memo 7; FY2025 outlays $41.8 billion [EV-WRK-413]), from benefit weeks starting January 1, 2031. In nominal dollars that is about **$26 billion in FY2032 and $36 billion in FY2040 (range $27-45 billion)**, and $259 billion over FY2031-39. States pay it from their own accounts and refill them with employers' state taxes on the larger base (LAB-11.05), so over the cycle the two match. The wage base makes the match possible: 18 states met the solvency standard at the start of 2026 [EV-WRK-304]. On the unified budget the two lines net to about zero over the cycle. In any one year they do not: a state builds reserves in good years and draws them down in bad ones, or borrows from the federal account [EV-WRK-305]. Neither line is on the general fund, and neither is added to section 1's total.
- **Social Security loses about $21 billion over FY2031-39 and $2.9 billion in FY2040** (off budget, range $1.3-4.5 billion). This is the payroll part of the offset on the larger employer taxes.
- **FUTA itself barely moves.** The net federal rate falls as the base rises (LAB-11.05): about $42 a worker today and about $50 at the $25,000 base (project arithmetic, section 4). The federal accounts gain perhaps $0.5-1.5 billion a year from FY2033, net of the offset (judgment; JCT scores it). That gain goes to the administration account and the extended-benefit account. It would cover the administration floor and part of the ordinary-year Extended Benefits, which section 1 counts on the general fund. Counting both there, and not netting this receipt against them, is the cautious reading. The alternative booking, which pays them from the federal accounts first, would lower the general-fund line by up to about $1-1.5 billion a year.
- **Extended Benefits in a downturn (contingent).** A moderate two-year recession in the window would pay 26-39 weeks beyond the regular 26 in most states, fully federal: about **$70-100 billion** over the downturn (judgment: about two million exhaustees a year at 30 weeks and about $600 a week on the new benefit levels is about $36 billion a year, and a deeper downturn costs more). That compares with the emergency programs Congress enacted ad hoc in 2008-13, which CBO's baseline does not carry either. The line is zero in the budget model's projection, which has no recession, and shown from zero to that figure. Its effect on unemployment is disputed, from 2 points [EV-WRK-374] to at most 0.3 [EV-WRK-375].
- **Work sharing, attestation, the ABC test, the compelling-reason quits and the identity checks** (LAB-11.02, 11.03, 11.06, 11.07) are inside the trust funds' 40-60% and the administration line. The identity checks should lower improper payments, which this section does not count as a saving.

**LAB-11.10: "charged to the reduced credit", in law and in the budget** (the reviewer's third note on #428).
- **What the law does today.** Federal law applies 100% of the added federal tax collected because of reduced credits to repaying the state's Title XII advances (42 U.S.C. 1101(d)(1)(A)) [EV-WRK-429]. Any excess goes to the state's own account in the Unemployment Trust Fund (1101(d)(1)(B)) [EV-WRK-430]. Advances are paid into that same state account [EV-WRK-431]. Money in a state's account may be withdrawn only to pay compensation under the state's own law [EV-WRK-432]. The section still cites the reduction as 3302(c)(3); it is now 3302(c)(2) [EV-WRK-428].
- **So LAB-11.10 does not work as drafted.** In a state with a loan, the added tax would repay the loan. In a state without one, it would land in the state's own account, which pays benefits only under the state's law: the law that fails the standard. None of the sections read gives the Labor Department authority to pay claimants directly. That is a finding from the sections read, not a search of the whole Code.
- **Proposed fix (provisional, a working choice for the milestone review).** Two amendments in R1:
  1. A *conformity reduction*, separate from today's loan reduction, whose added tax goes to a federal account in the trust fund instead of the loan or the state's account. Where a state also carries a loan, today's loan reduction keeps priority, so the two do not compete.
  2. *Authority for Labor to pay* the difference between the state's benefit and the federal standard through the state agency, under an agreement. States already pay federal benefits as Labor's agents; trade adjustment's wage insurance is one example [EV-WRK-331]. Labor pays directly only if a state refuses the agreement.

  Section 5's text (`5-delivery.md`, part 4) and LAB-11.10's entry in `provisions.json` are marked with this finding. The fix changes no figure in part 1.
- **In the budget.** The added tax is federal revenue to the trust fund. State accounts are on the federal budget, as CBO describes them [EV-WRK-436], so the revenue and the top-up are both on budget and off the general fund. Over time they net to about zero, but not at first. The first step raises 0.3 point of the base, about $75 a worker a year at the $25,000 base (project arithmetic), while topping up a state far below the standard could cost more than that in the first years. The federal account would advance the difference and recover it from later steps, so the general fund pays nothing by design. The line is contingent and zero if every state conforms (part 3).

## 3. What the total leaves out

The firm total in part 1 does not include these items. Each is reported here with its amount, and none is added to a booked figure.

| Item | Provisions | FY2030-39 | FY2040 | Why it is not in the total | Firm or contingent |
| --- | --- | --- | --- | --- | --- |
| The service-to-apprenticeship tranche | LAB-9.03 | 0 to $12.8 billion ($11.3 billion if it opens in 2035 on the working ramp) | 0 to $3.0 billion | Paid only when the gate is met | Contingent |
| Extended Benefits in a downturn | LAB-11.04 | 0 to about $100 billion | zero in the projection | The budget model's projection, like CBO's, has no recession (part 2) | Contingent |
| The standby displacement trigger | LAB-19.04, 19.05 | 0 to $25 billion | 0 to $5 billion | Zero while off; capped; provisional (part 4) | Contingent, provisional |
| Good-cause quits and the displacement measure | LAB-18.03; LAB-19.01-19.03 | about $2.1 billion | about $0.3 billion | Provisional, for Espen (part 4) | Provisional |
| LAB-11.10's top-up in a state that does not conform | LAB-11.10 | zero if every state conforms | zero | Financed from the reduced credit once authorized, inside the trust fund (part 2) | Contingent |
| UI benefits from the state trust funds, and employers' state taxes | LAB-11.01-11.03, 11.05, 11.07 | about +$259 billion and −$259 billion | about +$36 billion and −$36 billion | Trust funds, matched over the cycle (part 2) | Firm, outside the general fund |
| Social Security's payroll offset on the larger UI taxes | LAB-11.05 | about −$21 billion to the funds | about −$2.9 billion | Off budget (part 2) | Firm, off budget |
| The NLRB's staff | LAB-2.05 | about $1.0-1.4 billion | about $0.10-0.15 billion | CAP-7, democratic renewal's booked lines; replaces the review's $1.9 billion (range $1.3-3.3 billion) [EV-DEM-330] (section 5, part 7) | Booked there |
| FMCS's mediators and arbitration panels | LAB-1.05 | about $0.1-0.2 billion | about $0.01-0.02 billion | CAP-7; a written need against its contingency (CAP-7S.02) | To take up there |
| Wage and Hour's and OSHA's inspectors | LAB-7.01-7.03, LAB-6.01, LAB-12, 13, 15 | about $2.4-4.0 billion | about $0.3-0.5 billion | Inside Labor's $4.6 billion in CAP-7 [EV-DEM-329] | Booked there |
| OSHA above CAP-7's +700 | LAB-7.01 | inside the line above at its high end | about $0.08 billion | A written need against CAP-7's contingency | To take up there |
| The Office of Apprenticeship's registration staff, and the FLRA | LAB-8.04, LAB-16.01 | not yet sized; small | not yet sized; small | CAP-7 (section 5, part 7) | To size |
| Home care workers' overtime and travel time in Medicaid | LAB-12.01 | about $1 billion if the 2013 rule is gone by 2029 (judgment); zero if it stands | from 2035 inside care's rates | The rule is in force today, but its enforcement was suspended in 2025 [EV-WRK-225]. If it stands in January 2029, writing it into statute costs nothing. If it is rescinded, restoring it raises federal Medicaid's home care costs, about $0.1-0.3 billion a year until the single plan's rates take over in 2035. No register entry sizes it | Open (the 2029 baseline) |
| The contractor minimum wage | LAB-4.05 | not priced | not priced | Executive action; contractors' higher costs fall inside agencies' appropriations, which the baseline holds at their level. The 2021 rule's own analysis is not yet in the register | Within appropriations |
| Higher wages' tax effects beyond the floor | LAB-7.08, 12.02, 15.01, LAB-1 | not counted | not counted | Conventional scoring holds the economy's size fixed; posted pay ranges raised wages 1.3-3.6% [EV-WRK-407], and unions' wage effects are in section 2 | Not counted |
| Employers' compliance costs | LAB-6.01, 7.08, 13.01, 15.01 | outside the budget | outside | Private costs; the heat standard's were $7.8 billion a year against $9.18 billion of benefits in the Biden administration's analysis [EV-WRK-255] | Not federal |
| AI-4's booked row | AI-4 (the AI topic's) | $200 billion booked | $29.5 billion booked | Booked as "displacement-triggered wage insurance and training accounts", the AI topic's row; wage insurance (LAB-18) and the trigger (LAB-19) would cover its wage-insurance part (parts 7 and 9) | Booked there; to re-scope |

## 4. Items still with Espen, priced on their recommendations (provisional)

| Line | Provisions | 2030 | 2031 | 2032 | 2033 | 2034 | 2035 | 2036 | 2037 | 2038 | 2039 | **FY2030-39** | **2040** | Range FY2030-39 | Range 2040 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Wage insurance for work-connected good-cause quits (provisional) | LAB-18.03 | 0.0 | 0.02 | 0.11 | 0.18 | 0.19 | 0.20 | 0.20 | 0.21 | 0.21 | 0.22 | **1.5** | **0.23** | 0.30 to 4.2 | 0.04 to 0.62 |
| Displacement measure: occupation field and BLS's report (provisional) | LAB-19.01, LAB-19.02, LAB-19.03 | 0.0 | 0.07 | 0.13 | 0.09 | 0.04 | 0.04 | 0.04 | 0.04 | 0.04 | 0.04 | **0.51** | **0.04** | 0.29 to 0.87 | 0.02 to 0.06 |
| **Provisional lines** | | **0.0** | **0.09** | **0.24** | **0.27** | **0.23** | **0.23** | **0.24** | **0.25** | **0.25** | **0.26** | **2.1** | **0.27** | **0.59 to 5.1** | **0.07 to 0.69** |

1. **The small-business credit's size (LAB-5.01), new: mainly about money.** As specified, the credit costs about **$3 billion (range $1.5-7 billion)**, not the $0.02-0.04 trillion Espen saw when choosing memo 1 part 2 C (part 1). This is a choice mainly about money (`charter/STANDARDS.md`), so it goes to Espen:
   - *Recommended: keep the credit as specified, at about $3 billion.* Espen asked for "a small, temporary credit". Espen's own precedent is about this size: JCT put the 2007 package's small-business provisions at $4.8 billion over 2007-17 [EV-WRK-445]. They were a political cushion, not a tested way of softening job effects (`notes/espen-questions-2026-11-17.md`, part a). Section 4, `provisions.json`, the agenda row, memo 1's status line and the README now carry both figures, memo 1's judgment and this price. Drafted on the recommendation, provisional.
   - *Alternative: widen it toward the decided range.* Paying the credit for five steps instead of three, or at 50% in every year, would raise it to roughly $8-15 billion (judgment). Paying it for all workers below the new rate, at every employer, would raise it about two and a half times more. Each change adds claims and Form 941 lines.
2. **Memo 10 part 1 C, measuring displacement (LAB-19.01-19.03):** about $0.5 billion over FY2030-39 (range $0.3-0.9 billion): occupation's part of the one-time grant for wage-record fields (about $0.2 billion) and BLS's yearly report with an annual displaced-worker survey (about $35 million a year). That is inside memo 10's $0.5-1 billion, which also counted the hours field now in part 1. Part 1 B would cost about zero, and part 1 D slightly more.
3. **Memo 10 part 2 C, the standby trigger (LAB-19.04, 19.05):** **zero while off, contingent**, up to the $5 billion yearly cap when on, from about 2035: from $0 to $25 billion over FY2035-39 and up to $5 billion in FY2040. Its expected cost is near the low end, because broad displacement does not yet show in the data [EV-WRK-358]. Part 2 A or B would cost nothing; D would add an entry-level hiring credit, about $0.21 trillion at the legacy scenario's scale (memo 10).
4. **Wage insurance for work-connected good-cause quits (LAB-18.03's working reading):** about **$1.5 billion over FY2030-39 and $0.2 billion in FY2040** (range $0.3-4.2 billion). That is about 7% more recipients (range 3-12%; judgment, since no register entry counts quits found for good cause attributable to the employer), with their administration. *Alternatives:* excluding all quits costs nothing; including every good-cause quit, the personal ones under LAB-11.01's compelling reasons too, would roughly double this line (judgment).
5. **Point 5, severance (LAB-14.01), and point 11, codetermination (LAB-17.01):** no cost on the recommendation, since neither the mandate nor the board seats are in the first bill. A federal severance mandate would cost the budget little directly: employers pay it, and severance does not reduce unemployment benefits in most states (judgment).
6. **American Samoa's wage path (LAB-4.10):** zero federal cost under any option. The territories' wage schedules are a mandate on employers. Federal outlays in American Samoa would change only through programs that follow wages, too small to price here.
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
| LAB-9.01, 9.02, 9.04-9.06 | Part 1, civic service | Authorization or R1 fallback |
| LAB-9.03 | Part 3, contingent | The gate |
| LAB-19.01-19.05 | Part 4, items 2 and 3 | Provisional |

## 6. Against outside scores

Each line checked against a published score or estimate. None is a score of this design: point 15 asks CBO and JCT for those.

| Line | This section | Outside figure (publisher, year, stake) | Verdict |
| --- | --- | --- | --- |
| The floor's indirect effect | About $32 billion over FY2030-39; $5.5 billion in FY2040 | CBO, 2021: +$54 billion over 2021-31 for $15 by 2025 [EV-WRK-032] | **Holds as scaled:** CBO's floor bit at about 61% of the median, memo 1 B's at about half |
| Organizing, penalties and the board | About zero; penalties a small gain | CBO, 2023: $4 million to run S. 567 [EV-WRK-189]; CBO, 2019: +$39 million of penalty revenue over ten years [EV-WRK-176] | **Holds** |
| The small-business credit | About $2.9 billion | JCT, 2007: the small-business package passed with the 2007 raise lost $7.1 billion over 2007-12 and $4.8 billion over 2007-17 [EV-WRK-445]; it was mostly the work opportunity credit and expensing, not a credit tied to the raise | **Supports the bottom-up figure's order of size**, far below $0.02-0.04 trillion; Espen's own precedent is a few billion dollars (part 4, item 1) |
| Extended Benefits, ordinary years | About $31 billion over FY2031-39 | OMB, FY2017 budget (Obama administration; its own proposal): $36.7 billion over 2017-26 for a fully federal program with new triggers, on a projection with no recession [EV-WRK-438] | **The anchor.** The figure was raised from a first estimate of $15 billion to match it. The triggers differ, so the line keeps a wide range ($10-61 billion) |
| UI modernization and administration | About $10 billion (administration and the conformity grant) | OMB, FY2017: $14.1 billion over 2017-26 to modernize UI and $1.8 billion for short-time compensation [EV-WRK-438] | **Same order.** OMB's modernization paid states to adopt standards; memo 7 B requires them and pays for systems |
| The wage base and solvency | Trust funds matched over the cycle; FUTA's own receipts about $0.5-1.5 billion a year | CBO, 2018 options: a $40,000 base, indexed, with the net rate cut to 0.167%, raises $18 billion over 2019-28, mostly through state taxes in the first years [EV-WRK-435]. OMB, FY2017: solvency receipts of $46.3 billion over 2017-26, which made the whole UI package cost only $1.1 billion net over ten years [EV-WRK-439] | **Qualifies the presentation.** The scorekeepers count state UI taxes as federal revenue, and state accounts are on the budget [EV-WRK-436]. So a score in the window will show a net revenue gain while states rebuild reserves, where part 2 shows the trust funds net to zero over the cycle. The general-fund lines are unaffected |
| The UI systems grant | $1.5 billion over FY2030-32 | The 2021 rescue act: $2 billion for fraud prevention, equitable access and timely payment [EV-WRK-434]; the 2009 recovery act: $7 billion of incentive payments and $0.5 billion for administration [EV-WRK-433] | **Holds**, near ARPA's scale |
| Wage insurance | About $2.4 billion in FY2033 and $3.0 billion in FY2040; $20 billion over FY2031-39 | OMB, FY2017: $11.2 billion over 2017-26, $1.5 billion in 2026 [EV-WRK-437], for up to $10,000 over two years for new jobs under $50,000 [EV-WRK-440]. Kletzer and Litan (Peterson Institute and Brookings, 2001): about $3-3.5 billion a year in 1999 dollars, with a health subsidy [EV-WRK-443]. Jacobson, LaLonde and Sullivan (Hamilton Project, 2011): about $15 billion a year for a broader design [EV-WRK-444]. CBO, 2015: trade adjustment's version, +$0.4 billion over 2015-25 [EV-WRK-441] | **Holds.** LAB-18 allows $10,000 a year, twice OMB's cap, so about twice OMB's mature year in nominal dollars is expected. It sits between Kletzer-Litan and Jacobson-LaLonde-Sullivan. The last two share an author, so they are one view, not two |
| Apprenticeship | About $34 billion over FY2030-39 | CBO, 2020: $3.1 billion over five years for the National Apprenticeship Act's authorizations [EV-WRK-396] | **Larger by design**, per apprentice (memo 8) |
| National service | About $49 billion civic; $60 billion with the tranche | CBO, 2009, as reported by the NonProfit Times: about $5.7 billion over 2010-14 for the Serve America Act [EV-WRK-446], whose plan to reach 250,000 positions by FY2017 [EV-WRK-447] was never funded; legacy LAB-9B: about $0.05 trillion for 150,000 [EV-WRK-709] | **Holds** against the legacy figure; the 2009 law shows that authorization alone does not fund the positions, which is why LAB-9.06's fallback is in R1 |

**What has no outside score:** the credit's own design; the UI standards in the 2025 bill (S. 2312, no CBO or JCT score found); the tax offset on employers' UI taxes; the boards; and the trigger.

## 7. Against the booked rows

The budget model books three work rows and one AI row (case `mixed`, $ billion):

| Row | Booked FY2030-39 | Booked FY2040 | This section | Change a booking would make |
| --- | --- | --- | --- | --- |
| LAB-5, the legacy credit | 100.0 | 0 | 2.9 and 0 (LAB-5.01) | −97 over the decade |
| LAB-8, apprenticeships | 30.0 | 3.8 | 33.6 and 4.9 | +3.6 and +1.1 |
| LAB-9, national service | 120.0 | 16.8 | 49.0 and 6.7 civic; 60.3 and 9.4 with the tranche | −71 and −10.1 (−60 and −7.4 with the tranche) |
| LAB-1, the labor bill | 0 | 0 | the floor's indirect effect, 32.0 and 5.5 | +32 and +5.5 |
| Not booked: UI, wage insurance, the 14(c) grant, boards, outreach, revenue effects | — | — | 77.6 and 10.2 (part 1, the other lines) | +78 and +10.2 |
| **Work's rows** | **250.0** | **20.6** | **195.1 and 27.4** (firm) | **−55 and +6.8** (firm); −43 and +9.4 with the tranche |
| AI-4, AI and work (the AI topic's) | 200.0 | 29.5 | Its wage-insurance part is LAB-18 here (part 3) | To re-scope with the AI topic (part 9) |

- **Why the decade falls and FY2040 rises.** The legacy credit ($100 billion) and the legacy universal service row ($120 billion at 250,000 slots [EV-WRK-705]) drop to the decided designs. Unemployment insurance, wage insurance and the floor's indirect effect were never booked, and they are permanent, so FY2040 rises.
- **The legacy labor file's own total** was $0.25 trillion (0.13-0.41) [EV-WRK-708], which matches the booked rows. The decided set is smaller over the decade and different in kind.

## 8. The fiscal-rule report

One basis: federal fiscal years, $ billion, a cost positive, the general fund's primary balance, against what the budget model books (case `mixed`).

| Measure | FY2030-39 | FY2040 (permanent) |
| --- | --- | --- |
| Work on the general fund, firm lines (part 1) | about **+$195.1 billion** (range +$96 to +$349 billion) | about **+$27.4 billion** (0.051% of GDP; range $13-44 billion) |
| *of which:* spending lines | +$149.7 billion | +$20.4 billion |
| *of which:* revenue effects (the credit, the UI tax offset, income tax on wage insurance, penalties) | +$13.4 billion | +$1.4 billion |
| *of which:* the floor's indirect effect (CBO's net) | +$32.0 billion | +$5.5 billion |
| Contingent: the service tranche | 0 to +$12.8 billion (+$11.3 billion if the gate opens on the working ramp) | 0 to +$3.0 billion (+$2.7 billion) |
| Contingent: Extended Benefits in a downturn | 0 to about +$100 billion | zero in the projection |
| Provisional (part 4): quits and the measure; the trigger | +$2.1 billion; the trigger 0 to +$25 billion | +$0.3 billion; the trigger 0 to +$5 billion |
| Booked for the same purposes: LAB-5, LAB-8, LAB-9 | $249.9 billion | $20.6 billion |
| **Net change a booking would make (firm)** | **about −$55 billion** | **about +$6.8 billion** |
| Net change with the tranche | about −$43 billion | about +$9.4 billion |
| UI trust funds (part 2) | benefits +$259 billion, matched by employers' state taxes | +$36 billion, matched |
| Social Security's funds (part 2) | about −$21 billion | about −$2.9 billion |

- **The yearly cost** (firm lines): about $4 billion in FY2030, $11 billion in FY2031, $16 billion in FY2032, rising to $23 billion in FY2035 and $27 billion in FY2040.
- **Permanent cost from FY2040:** about **$27 billion a year** on the general fund (about $30 billion with the tranche), growing with wages and prices. Wage insurance, unemployment insurance, apprenticeship, service and the floor's effect are permanent. The credit, the 14(c) grant, the conformity grant and the record fields end by FY2034.
- **Its share of the plan-wide margin.**
  - *The gap:* the plan-wide general-fund primary gap in FY2040 is **$602.7 billion short** (1.11% of GDP; `agenda_gf_primary_bn`, case `mixed`, on main after #402); a positive figure is a shortfall.
  - *Work's whole general-fund cost* in FY2040, $27.4 billion, is **about 4.5% of the gap**, or 5.0% with the tranche.
  - *A booking of the decided set* would replace $20.6 billion of booked work rows. It adds about **$6.8 billion, to about $609.4 billion short (1.13% of GDP): about 1.1% of the gap.** With the tranche it adds $9.4 billion (to $612.1 billion, 1.6% of the gap); with the provisional items too, $9.7 billion.
  - *Over FY2030-39* a booking lowers the decade gap by about $55 billion (from $3,773 billion to about $3,718 billion), because the booked legacy credit and service row are larger than the decided designs.
  - *AI-4:* if the AI topic re-scopes AI-4 so that its wage-insurance part is carried here, the plan-wide figure falls by that part, up to about $3 billion in FY2040. Its size inside AI-4 is not split in the ledger (part 3).
  - *Basis:* additive on the primary balance before interest, like every dossier's report.
- **The test years.** Nothing sunsets after FY2034, and the floor's indirect effect, unemployment insurance and wage insurance grow with wages. Without the floor's indirect effect, which is CBO's net and the least certain line, FY2040 is about $21.9 billion.
- **Report, don't gate** (`DEC-2026-11-10-05`). Work's FY2040 share is a figure for the financing settlement, not a defect to fix. One choice here is mainly about money, the credit's size (part 4, item 1). It goes to Espen.

## 9. What a booking would change (proposed, not made)

Tier 3, for the lead after the milestone review (`charter/STANDARDS.md`, "Milestone review": book once, after the fixes). This PR changes nothing in `models/data/inputs/`. The rows below are low / mid / high over FY2030-39 in $ trillion, from `tools/work_path.py` (`booking_rows()`), with FY2040 in $ billion. Year shapes go in `fiscal-years.csv` from the same tool.

| Row | Lines | Low / mid / high, FY2030-39 ($T) | FY2040 ($B) |
| --- | --- | --- | --- |
| LAB-4 indirect (DY4 or LAB-1) | The floor's indirect effect | 0.000 / 0.032 / 0.080 | 5.5 |
| LAB-5 | The credit (revenue row) | 0.001 / 0.003 / 0.007 | 0.0 |
| LAB-4.09 | 14(c) grant | 0.001 / 0.002 / 0.003 | 0.0 |
| LAB-3 and 4.04 | Boards and commission (appropriated) | 0.001 / 0.001 / 0.003 | 0.1 |
| LAB-7.05 | Outreach (appropriated) | 0.000 / 0.001 / 0.001 | 0.1 |
| LAB-11 (general-fund spending) | Extended Benefits, administration, conformity grant | 0.018 / 0.041 / 0.076 | 5.3 |
| LAB-11 tax offset (revenue row) | The UI tax offset | 0.004 / 0.013 / 0.032 | 1.8 |
| LAB-18 (spending) | Wage insurance, its administration, the hours field | 0.011 / 0.022 / 0.037 | 3.2 |
| LAB-18 income tax (revenue row) | Income tax on wage insurance | -0.004 / -0.002 / -0.001 | -0.3 |
| Penalties (revenue row) | Civil penalties | -0.001 / 0.000 / 0.000 | -0.1 |
| LAB-8 | Apprenticeship | 0.024 / 0.034 / 0.054 | 4.9 |
| LAB-9 | Civic service | 0.042 / 0.049 / 0.056 | 6.7 |
| LAB-9.03 (contingent) | The tranche | 0.000 / 0.011 / 0.013 | 2.7 |

Further steps:
1. **`ledger-bills.csv`, line 38 (LAB-5, 0.05 / 0.10 / 0.15):** replace with LAB-5.01 at about 0.001 / 0.003 / 0.007 (provisional, part 4, item 1), as a revenue row with the trust funds made whole.
2. **Line 39 (LAB-8, 0.02 / 0.03 / 0.05):** to 0.024 / 0.034 / 0.054.
3. **Line 40 (LAB-9, 0.06 / 0.12 / 0.20):** to the civic line, 0.042 / 0.049 / 0.056, with the tranche as a contingent component (0 / 0.011 / 0.013). Move its rail from R2 to R1 (point 16), with the authorization as the regular-order route.
4. **New rows:** LAB-11's general-fund spending, LAB-18 with its administration and the hours field, the 14(c) grant, the boards and outreach (appropriated), and the revenue rows (the UI tax offset, income tax on wage insurance, penalties). Each goes on its own line, with spending and revenue apart.
5. **The floor's indirect effect:** a component of LAB-1, or a replacement for DY4's distributional row [EV-WRK-707], not both.
6. **The UI trust funds:** the funds model's state accounts and the federal accounts, if the model carries them. They stay off the general fund, and Social Security's payroll offset (about −$21 billion) goes on the funds model's payroll line.
7. **AI-4:** for the AI topic. Its row's wage-insurance part (wage insurance is "AI-4A's benefit", memo 8) is carried by LAB-18 and, if Espen chooses memo 10 C, LAB-19. The rest (training accounts) stays the AI topic's.
8. **CAP-7:** democratic renewal takes up the NLRB's line and the written needs (section 5, part 7). Nothing here.
9. **Rails:** the money moves to R1 (point 16). The budget model books LAB-5, LAB-8 and LAB-9 on R2 today.

## 10. What each figure is

| Input | Treatment (`DEC-2026-11-10-07`) |
| --- | --- |
| The floor's schedule; the credit's form, shares and cap; the subminimums' end; the UI standards and Extended Benefits' triggers and share; wage insurance's eligibility, benefit and four rules; the apprenticeship line's payment rules and target; national service's scale and gate | Commitments (decided) |
| The floor's indirect effect (CBO's 2021 pattern scaled to a smaller bite) | Working assumption: central $5.5 billion in FY2040, range zero to $8 billion; CBO's score of memo 1 B (point 15) replaces it |
| The credit's added wage cost by step | Working assumption, bottom-up (part 1); JCT scores it (point 15) |
| The trust funds' benefit increase (40-60%) | Working assumption on memo 7's basis [EV-WRK-413] [EV-SEC-045]; studied in implementation from the claims states already report |
| Extended Benefits in ordinary years | Working assumption ($1-6 billion a year in 2031), anchored on OMB's FY2017 score [EV-WRK-438]; the states' unemployment rates to add to the register |
| Extended Benefits in a downturn | Contingent; zero in the projection, about $70-100 billion in a moderate two-year downturn |
| UI administration's workload | Working assumption ($0.2-0.8 billion a year) |
| The tax offset's general-fund share (5%, range 2-10%) | Working assumption on the scorekeepers' 25% convention; JCT scores it with the wage base (point 15) |
| Wage insurance's take-up (60%) and reemployment within a year (60%) | Working assumptions; studied in implementation from the first two years' state counts (section 5, part 8) |
| Wage insurance's administration (10%) | Working assumption on state UI's ratio [EV-WRK-309] [EV-WRK-413] |
| Apprenticeship's funded share (55% of today's starts) and attrition (75% retained, 45% complete) | Working assumptions; completion from [EV-WRK-350]; studied in implementation from the records programs file (LAB-8.04) |
| National service's cost per position | Working assumption on AmeriCorps' rules [EV-WRK-398] [EV-WRK-399] |
| The tranche's opening year (2035) | Working assumption from the ramp; the gate decides it |
| The boards' number and cost | Working assumption; open whether more than a few boards are convened |
| Home care's Medicaid cost | Open: turns on whether the 2013 rule stands in January 2029 |
| LAB-11.10's channel | Open: needs a new authorization (part 2) |
| The credit's size, the trigger, the measure, good-cause quits, American Samoa, the monthly statement | Provisional, for Espen (part 4) |
| Growth rates (wages 3.5%, prices 2.5%, UI benefits 4%) | Working assumptions |

## Evidence still needed

- CBO and JCT scores of memo 1 B, memo 3 as decided, memo 7 B, the credit (LAB-5.01) and the wage-base schedule (LAB-11.05) with its offsets, on the 2029 baseline (point 15).
- **GAO's reports on American Samoa's minimum wage** (LAB-4.10; the reviewer's first note on #428). The statute the dossier saved, `library/text/wrk-5-usc-29-206-minimum-wage.txt`, lines 676-720, directs GAO to report on the impact of the increases by April 1, 2017 and April 1, 2020, and on alternative ways to raise the wage within a year of October 7, 2015. GAO reported under that mandate in 2010, 2011, 2014, 2016 and 2020 [EV-WRK-448] [EV-WRK-449]: GAO-10-333 (April 8, 2010), GAO-11-427 (June 23, 2011), GAO-14-381 (March 31, 2014), GAO-17-83, *American Samoa: Alternatives for Raising Minimum Wages to Keep Pace with the Cost of Living and Reach the Federal Level* (December 2, 2016, the alternatives report, which also served for 2017), and GAO-20-467, *American Samoa: Economic Trends, Status of the Tuna Canning Industry, and Stakeholders' Views on Minimum Wage Increases* (June 11, 2020). These are the studies `5-delivery.md`, part 5, says are missing. They exist but have not been read (GAO blocks downloads; an upload from Espen or a citation row with a hand check).
- The states' unemployment rates over a recent cycle, to size Extended Benefits' ordinary-year cost (BLS's local area unemployment statistics).
- The appropriations acts' automatic administrative funding per 100,000 insured unemployed, for the workload line.
- A count of quits found for good cause attributable to the employer (Labor's benefit accuracy data), for LAB-18.03.
- The 2021 contractor minimum wage rule's regulatory analysis (LAB-4.05), and the 2013 home care rule's (LAB-12.01).
- The four sectors' share of registered apprenticeship starts, from Labor's apprenticeship data.
- CBO's own estimate of the Serve America Act (2009): the figure here is a press report of it [EV-WRK-446].
- CBO's 2018 FUTA option, read from a verbatim copy on a third-party site; to check against cbo.gov [EV-WRK-435] [EV-WRK-436].
- Independent corroboration of OMB's FY2017 UI scores [EV-WRK-438] and of CBO's FUTA option [EV-WRK-435] and trade adjustment estimate [EV-WRK-442]; each is one publisher's analysis until then.
- Authority for states to pay federal benefits for federal workers and veterans as Labor's agents (the model for LAB-11.10's agreement), not yet in the register.

## Questions for Espen

New in this section:
1. **The small-business credit's size** (LAB-5.01): as specified it costs about $3 billion, not the $0.02-0.04 trillion you saw. Recommended: keep it as specified (small and temporary, as you asked); the alternative is to widen it to five steps or every employer (part 4, item 1). This choice is mainly about money.

Carried from sections 4 and 5, each priced here on its recommendation and still provisional:
2. Memo 10, measuring displacement and a standby trigger (LAB-19): about $0.5 billion for the measure; the trigger is zero while off, up to $5 billion a year when on.
3. Point 5, severance (LAB-14.01): no cost on the recommendation.
4. Point 11, codetermination (LAB-17.01): no cost on the recommendation.
5. Wage insurance and quits for good cause (LAB-18.03): about $1.5 billion over FY2030-39.
6. American Samoa's wage path (LAB-4.10): no federal cost under any option. GAO's reports exist and have not been read (Evidence still needed).
7. Wage insurance's monthly statement (LAB-18.08): inside administration; the alternatives cost about the same.
