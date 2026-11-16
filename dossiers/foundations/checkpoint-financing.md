# Stage E checkpoint memo: the plan-wide gap after the single health plan is financed

Role: the financing checkpoint at the end of stage E (`charter/PLAN.md`, section 6, stage G's row). It records what the checkpoint settled for the single health plan (HLT-1 to HLT-8): what the plan costs, how it is paid for and who comes out ahead. It also gives the plan-wide gap that is left, what drives that gap, and the open items handed to stage G. The health detail has one home each, and this memo cites it by section rather than copying it:
- [`health-financing.md`](health-financing.md): the payer accounting, the employer contribution's rules, the worker transition credit and the comparison with the bills;
- [`health-cost-review.md`](health-cost-review.md): the corrected cost, the take-home test, package E and the five new streams;
- [`health-household-contribution.md`](health-household-contribution.md): the household contribution as decided.

Status: **decided and booked, November 16, 2026.**
- **Decided:** Espen's November 15 answers (`DEC-2026-11-15-01` to `-29`, #393) and November 16 answers (`DEC-2026-11-16-01` to `-03`, #395). The analysis behind them is in #385, #386, #388 and #392.
- **Booked:** the health financing booking, #394 (tier 3), on top of clean power's booking (#359, #372, #377).
- This memo books nothing and changes no decision.
- **Figures as of #402.** #402 priced HLT-7's status rule on the corrected base and counted HEC's phase-in after the window. That moved the plan-wide gap from #394's $588B and $3,592B to $603B and $3,773B, and health's first call from $518B to $532B. The figures below are restated from the model's outputs on main after #402.

Units:
- Federal fiscal years, case `mixed`.
- Budget totals are in nominal dollars: $B for billions, $T for trillions. Household figures are in 2026 dollars, as in the health memos.
- A positive gap is a shortfall.
- Every figure is project arithmetic on the project's exploratory models, not an official score.
- Budget figures come from the budget model's run on #394 (`models/data/recovery-budget-paths.csv`; audit lines in `legacy/sources/recovery-budget-audit.csv`) and from `models/tools/health_booking.py` (`financing()`, `first_call()`).

## In plain terms

1. **What the single health plan costs.** In FY2040 the whole system costs about **$7.35 trillion** (`health-cost-review.md` 2.2). That covers everyone's care, its administration and what the plan adds. The figure includes the cost review's corrections and three design changes: administration at 4%, a national health budget from 2037, and drug prices 25% below today's. On the corrected cost, the country spends about **$1 trillion (8%) less** on health than under today's law, while covering everyone (`health-cost-review.md`, in plain terms, item 2).
2. **How it is paid for, source by source** (FY2040, $B):

   | Source | $B |
   | --- | --- |
   | Federal money already spent on health (Medicare, Medicaid and the rest), committed to the plan | 2,876 |
   | Employers: a contribution equal to what they would have spent on premiums (19.3% of pay between $20,000 and the wage base), less a small-employer allowance on each firm's first $100,000 | 1,945 |
   | Households: the health contribution below, less the worker transition credit ($111B) | 659 |
   | States: 100% of what they used to spend on Medicaid for the people who move | 466 |
   | Tax on the pay that used to go to premiums | 358 |
   | Five new taxes at the top and on corporations: a wealth tax, a financial transactions tax, capital gains taxed like pay above $1 million, a higher corporate rate, and the investment-income tax on pass-through business income | 385 |
   | The Medicare payroll tax, 2.9% as today ($580B), less the Medicare taxes the health contribution replaces ($440B: the worker's 1.45%, $326B; the 0.9% Additional Medicare Tax, $53.5B; worker HI on former premiums, $16B; H1b's wage half, $43.5B) | 140 |
   | Revenue the plan already counted for its other flagships, which health now takes first | 516 |
   | **Total** | **7,345** |

   The household contribution's sections 6 and 7 explain the $440B. On the budget model's own run, health's call on booked revenue is $532B (after #402).
3. **The household contribution, as decided.** It is one health contribution in place of the worker's Medicare taxes (`DEC-2026-11-15-10` to `-13`, `DEC-2026-11-16-01`):
   - **2.25% of AGI** (adjusted gross income, the income on the tax return);
   - **plus 5.96 points on AGI above $205,400 single or $256,750 joint** (2026 dollars, indexed);
   - **nothing at or below 138% of poverty,** phasing up at one steady rate to the full charge at 250% of poverty, with no cliff and no form to file;
   - withheld from pay for wages, and paid on the tax return for other income;
   - **before 2035 the base rate rises in steps with the waves of people moving into the plan:** 0.6% in 2031-32, 1.0% in 2033, 1.4% in 2034, then 2.25% from 2035. The surcharge is 5 points from 2031 and 5.96 from 2035.
4. **Who comes out ahead** in what they see leave their pay and wallet for health care (the take-home test, `DEC-2026-11-15-02`):
   - **88.7% of workers,** including every worker below 200% of poverty;
   - **about 98.6% of retirees and non-workers,** because the plan ends Medicare premiums and most medical bills;
   - **an example:** a single worker at $72,000 with job coverage goes from about **$6,700 a year to about $3,000** (`health-household-contribution.md` 3).
5. **The plan-wide gap left for stage G:** **$603 billion in FY2040** (1.11% of GDP) and **$3,773 billion over FY2030-39**, as booked on #394 and restated after #402. Before the health booking it was $4,164B and $23,396B.
6. **What drives it.** In FY2040, **$532B of the $603B is health taking revenue the other flagships had counted on** (Espen: health comes first, `DEC-2026-11-15-04`). The other $70B is the rest of the plan's own shortfall. Among the rest of the plan, the largest net costs in FY2040 are:
   - care parts B to D (long-term care, child care and pre-K, the care wage floor): about $750B;
   - the secure floor: about $300B;
   - clean power: about $125B;
   - housing: about $120B.

   The revenue already booked and the dedicated funds' own lines cover most of those costs (part A2). Stage G closes the gap by cutting or refinancing other flagships, taking health's share from the top-end and corporate rows first (`DEC-2026-11-15-20`).
7. **The biggest risk to the gap.** The national health budget (D2) saves $249B in FY2040, and holding health spending's growth that close to GDP's has never been achieved [EV-CAR-742]. Without it, the FY2040 gap would be about **$852B** (part D).

## Part A. The plan-wide gap and what drives it

### A1. The gap as booked

The fiscal rule (`D4`) asks that permanent programs be paid for on the general fund in FY2040 and every later year, and that total debt and net interest stay below the baseline path. Only time-limited capital may be borrowed, inside an investment envelope (D4-B; `legacy/governing/decision-brief-02-trims-scope-and-fiscal-rule.md`). How the rule is read is decided:
- CBO's current-law baseline, with any changes disclosed (`DEC-2026-11-08-03`);
- midpoints, with a cautious reading beside them (`-04`);
- one FY2030-39 window, plus each bill's own CBO window (`-05`);
- CBO's interest rates, with a +1-point stress (`-06`);
- the unified budget for the debt guardrails, with the general fund beside it (`-07`);
- the counting inputs (`DEC-2026-11-12-08`, `-10`, `-11`).

Dossiers report their cost, and balancing happens here (`DEC-2026-11-10-05`).

| Measure (case `mixed`) | FY2030 | FY2031 | FY2032 | FY2033 | FY2034 | FY2035 | FY2036 | FY2037 | FY2038 | FY2039 | **FY2040** | FY2030-39 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| General-fund primary balance, short ($B) | −198 | −76 | 95 | 91 | −18 | 548 | 847 | 839 | 844 | 800 | **603** | **3,773** |
| Share of GDP | −0.53% | −0.19% | 0.24% | 0.22% | −0.04% | 1.22% | 1.81% | 1.73% | 1.68% | 1.53% | **1.11%** | — |

Source: `models/data/recovery-budget-paths.csv`, column `agenda_gf_primary_bn`, on main after #402. Primary means before interest; a negative figure is a surplus.
- **FY2030-34 run close to balance or in surplus.** The five new streams start in FY2030 (`DEC-2026-11-16-02`), and the household contribution and employer contribution step in with the waves, while health's spending grows as people move. So health's own sources exceed its need in those years by about $0.9T in all (`first_call()`: −$883B).
- **The gap jumps in FY2035,** when the plan reaches its endpoint and everyone is covered.
- **The unified reading,** which also counts the dedicated funds' own balances (Social Security, Medicare HI, education, paid leave), is a surplus of $251B in FY2040 (`program_primary_bn`).

### A2. What drives it

FY2040 and FY2030-39 by flagship, from the audit lines (case `mixed`, `primary_deficit_change_bn`). A cost is positive and revenue negative.

| Driver | Rows | FY2040 ($B) | FY2030-39 ($T) |
| --- | --- | --- | --- |
| Health, the single plan's spending (net of the federal money it replaces and the states' payment) | HLT-1 to HLT-8; HLT-7 is $3,532B (#394's components, with #402's status rule: the seam, the nine corrections, D1, D2, D5, the states at 100%, the credit) | 3,554 | 19.51 |
| Health's own financing | HEC −1,945, HX −966, HCU −770, HEX +608, the fold-in HCW, HCA, HCP and HCH +440, the five streams HS1-HS4 and H1a −385 | −3,019 | −17.39 |
| **Health, net: its call on revenue the plan had booked for other flagships** | | **535** | **2.12** |
| Care parts B to D: long-term care, child care and pre-K, the care wage floor | HLT-9 to HLT-11, FAM-2 | 748 | 3.43 |
| Secure floor (flagship 1) | FAM-1, INC-1 to INC-5, LAB-10 | 303 | 2.63 |
| Clean power (flagship 4) | CLI-*, CX, CXA, CXP, C1T | 125 | 1.90 |
| Housing (flagship 3) | HOU-1, HOU-4D, housing's extra items | 121 | 0.81 |
| Transportation | MOV-29 to MOV-31, MR6 | 54 | 0.72 |
| Immigration (flagship 6) | IMM-1, IMM-EV, IF1T | 23 | 0.15 |
| Everything else | Education, agency capacity, work and AI, democracy, the recovery credit | 350 | 3.05 |
| Revenue already booked: corporate, top-end, estate, enforcement | G1 to G11, H1b, GX, C3A, C18, C35, C38 to C43, the IRS allowance | −1,106 | −8.66 |
| Revenue already booked: the indexed income contributions | 4 points above $100K/$200K from 2033; 2 points above $20K/$40K from 2035, phasing in to 2044 | −484 | −1.91 |
| Fund-boundary items, net | The dedicated funds' own lines (Social Security −732, education −202, paid leave +16; −919 in all), with the general fund's grants to them added back (+853) | −65 | −0.47 |
| **General-fund gap** | | **603** | **3.77** |

**Reading it:**
- Health's rows net to $535B in FY2040 and $2.12T over the decade. Health's first call as #394 measures it is $532B in FY2040 and $1.89T over FY2030-39. The difference is in rows on the fund boundary: HLT-4's care parts, and H1a's early years, which are paid to Medicare's HI fund.
- **On #394's measure the gap splits in two.** Health's first call is $532B in FY2040 and $1.89T over the decade. The rest of the plan is about $70B and $1.89T, the same as before the health booking. The health booking moved the gap from health's own need ($4.09T in FY2040) to health's call on the other flagships' revenue.
- **The decade is driven by FY2035-39.** The rest of the plan's own shortfall runs at about $0.1T to $0.25T a year from FY2031. Health's first call is about −$0.9T over FY2030-34 and about +$2.8T over FY2035-39.

### A3. Inputs still moving

- **Health is booked** (#394). #402 did the small follow-ups in part D, items 10 to 12; item 11 raised FY2040 by about $15B. Item 13 would change FY2040 by a few billion dollars.
- **Clean power is booked** (#359, #372, #377) and paused at L3. Its parked items don't move FY2040 by more than a few billion dollars.
- **The secure floor is booked,** including D (#330). SS-8 is booked at zero (part D).
- **Known later items:**
  - a new CBO baseline: each one re-runs the settlement (plan, section 6);
  - E-Verify's Social Security funds line: about −$42B over FY2030-39, from #328;
  - the items dossiers sent the settlement (part C).

### A4. The revenue options the legacy work holds

**Already counted, so not available again:**
- **The general-fund reforms in the `mixed` case.** The legacy reconciliation traces them at $8.005T over FY2030-39 and $989B in FY2040 (`legacy/sources/revenue-counted-reconciliation.md`). Among them:
  - G1, the corporate rate to 28% ($1.65T);
  - G9, reversing the 2025 cuts above $450K ($1.45T);
  - C38, the sprint package REV-TS1 to TS11 ($0.89T);
  - G6, gains at death ($0.70T);
  - G7, G10, G11, G5, G8, G3, H1b, C18, C35, C39 to C41 and C43, less the GX and CX offsets.
- **The indexed income contributions** ($1.91T).
- **Health's own financing:**
  - HX ($4.84T);
  - the employer contribution (HEC);
  - the unified household contribution (HCU);
  - the five new streams: HS1, the financial transactions tax at 0.1%; HS2, the wealth tax; HS3, gains taxed as ordinary income above $1M; HS4, the corporate rate at 30% with expensing repealed; and H1a, the investment-income tax on active pass-through income. These used most of what the legacy menu held at the top end.

**Not yet counted.** FY2030-39 midpoints in $T come from the legacy menu, scaled from CBO and Treasury (`legacy/domains/domain-revenue.md`, "Closing the general-fund gap"; `legacy/sources/revenue-channels-and-full-menu.md`). FY2040 yields per point come from the budget model's parameters (`models/tools/recovery-budget/assumptions.json`).

| Family | Option (legacy ID) | FY2030-39, $T | FY2040, $B | Who pays; main risk |
| --- | --- | --- | --- | --- |
| Payroll | New general-fund payroll contribution, no cap (W1) | 1.6 per point | about 200 per point, gross | All workers. It stacks on the employer contribution and fails the take-home test for many workers. The payroll point may be a capped figure (part D) |
| Broad income | Contribution above $20K/$40K | 1.8 per point | about 180 per point | Most households. It taxes the same base as the health contribution: the booked 2 points already cut workers ahead from 88.7% to 70.1% (part D) |
| | Surtax above $100K/$200K (C20) | 0.67 per point | about 67 per point | Upper-middle incomes. It overlaps the 4 booked points and the health surcharge on the same base |
| Consumption | 5% value-added tax, narrow or broad base, before any rebate | 2.8 / 4.2 | about 105 per point, broad | Regressive without a rebate; needs a new collection system |
| Top end and capital | Top four brackets +1 more point; pass-through and deferred-pay reform (REV-SC2); stock-option deduction (REV-HP2) | 0.36 per point; 0.35; 0.02 | — | High earners. The top rate on wages is already about 67.7% (`health-household-contribution.md` 2). SC2 overlaps H1a, now booked as health stream (e) |
| Carbon and excise | Steeper carbon path (REV-C1F); road-fuel convergence (REV-C1D); alcohol and tobacco | — ; small; 0.13 and 0.06 | — | Shrinking bases. The carbon fee is dedicated to the dividend |
| Borrowing within the rule | Time-limited capital inside the investment envelope (precedent C21) | Doesn't help FY2040 | — | Capital only |

**Not available:**
- keeping today's tariffs, which are already in the baseline;
- the HI reserve, which folds into the plan's fund at the endpoint;
- C19b's cap on the exclusion once HX ends it;
- counted rows used a second time.

**A staleness check.** CBO's latest options volume is still *Options for Reducing the Deficit: 2025 to 2034* (December 2024), which predates P.L. 119-21. Options that interact with the 2025 law's rates and deductions need rescoring against the 2029 baseline before they are booked.

## Part B. What was decided

Each decision's home is `charter/decisions.md`. The lines below are labels, not restatements.

| ID | What |
| --- | --- |
| [DEC-2026-11-15-01](../../charter/decisions.md) | The goal: a fresh start on the plan's pricing and financing |
| [-02](../../charter/decisions.md) | The take-home test: visible health costs must fall |
| [-03](../../charter/decisions.md) | General revenue from other streams, sparing employers |
| [-04](../../charter/decisions.md) | Health comes first on the plan's revenue |
| [-05](../../charter/decisions.md) | Book the cost review's nine corrections |
| [-06](../../charter/decisions.md) | D5: drug prices 25% below today's |
| [-07](../../charter/decisions.md) | D1: administration at 4%, with a 3% target |
| [-08](../../charter/decisions.md) | D2: a national health budget at GDP + 1 from 2037 |
| [-09](../../charter/decisions.md) | Package E |
| [-10](../../charter/decisions.md) | The household contribution's shape: one contribution in place of the worker's Medicare taxes |
| [-11](../../charter/decisions.md) | Its base rate: 2.25% of AGI |
| [-12](../../charter/decisions.md) | Its exemption: one steady rate from 138% to 250% of poverty |
| [-13](../../charter/decisions.md) | H1b's wage half folded into the surcharge (5.96 points) |
| [-14](../../charter/decisions.md) | The small-employer allowance |
| [-15](../../charter/decisions.md) | Stream (a): the financial transactions tax at 0.1% |
| [-16](../../charter/decisions.md) | Stream (b): the wealth tax, with a fallback |
| [-17](../../charter/decisions.md) | Stream (c): capital gains and dividends as ordinary income above $1M |
| [-18](../../charter/decisions.md) | Stream (d): the corporate rate at 30%, permanent expensing repealed |
| [-19](../../charter/decisions.md) | Stream (e): the 3.8% investment-income tax on active pass-through income |
| [-20](../../charter/decisions.md) | Health's first call on booked revenue |
| [-21](../../charter/decisions.md) | The employer contribution equals what employers would otherwise spend |
| [-22](../../charter/decisions.md) | Its base: pay between $20,000 and the wage base |
| [-23](../../charter/decisions.md) | Its rules: mandatory, the phase-in, pay protections, savings into pay, union contracts |
| [-24](../../charter/decisions.md) | The worker transition credit, transitional |
| [-25](../../charter/decisions.md) | The states pay 100% of their former Medicaid spending for the people who move |
| [-26](../../charter/decisions.md) | The self-employed pay on net earnings, as SECA does |
| [-27](../../charter/decisions.md) | D3 and D4 kept: the hospital rate and the small copays |
| [-28](../../charter/decisions.md) | HLT-7 rebooked on CBO's Medicare figure |
| [-29](../../charter/decisions.md) | Counting and the fund |
| [DEC-2026-11-16-01](../../charter/decisions.md) | The household contribution before 2035 follows the waves |
| [-02](../../charter/decisions.md) | The five new streams start in FY2030 |
| [-03](../../charter/decisions.md) | The small-employer allowance also applies before 2035 |

The earlier health package in this memo is superseded and has been removed: memos F1 to F3 and the points in its part B4. They were never decided. For the record, see this file's Git history and `health-financing.md` part 10.

## Part C. The rest of the gap after health

**What remains for the rest of the plan:** about **$70B in FY2040** and about **$1.89T over FY2030-39** (part A2), on top of health's first call. The decade figure matters for the debt guardrail, not for the FY2040 test.

**Items dossiers sent the settlement** (each to be priced at stage G):
- housing's FY2040 and FY2041 maturity gaps (`DEC-2026-11-09-09`, `DEC-2026-11-10-04`), and HOU-2D's revenue row;
- the education fund going negative in 2035 at the 1.4-point rate (about 1.7 points keeps it solvent);
- R1's child benefit: about $2.3T in the ten years after its window (the Byrd rule);
- transportation's fuel-tax path (`DEC-2026-11-10-14`);
- SS-8's budget treatment, and E-Verify's funds line;
- the rebuild of the financing screens in `models/tools/financing-protection/`;
- the +1-point interest stress (`DEC-2026-11-08-06`).

**The menu for the non-health remainder:**
1. **Health's early surplus.** About $0.9T over FY2030-34 (part A1) is larger than the rest of the plan's shortfall in those years. Holding it as a reserve for the plan's fund, or counting it against the rest of the plan's decade gap, is a stage G choice (part D, item 3). It does nothing for FY2040.
2. **One more point above $100,000/$200,000:** about $67B in FY2040 at the legacy yield, which would close FY2040's remainder on its own. It now stacks on the 4 booked points and the health surcharge, on a top rate on wages of about 67.7%, so it would raise less than $67B (`health-financing.md` part 10).
3. **Top-end and capital options not yet used:** REV-HP2 and a fifth bracket point. REV-SC2 overlaps H1a. These total well under $1T over the decade, and they meet the capital-income cap (part D, item 4).
4. **A VAT with a per-person rebate,** or a broad base, if stage G needs more than trims. Each conflicts with the take-home test in a way that has to be shown.

## Part D. Stage G's open items

These are gathered from the decisions, #392's and #394's "For the board", and the health memos. None needs Espen's answer now: stage G re-audits what this checkpoint settled (`DEC-2026-11-14-06`).

**The household side:**
1. **The booked 2 points above $20K/$40K.** With them, 70.1% of workers come out ahead instead of 88.7%, and no rate from 2.0% to 2.5% reaches 85% (`health-household-contribution.md` 8; `DEC-2026-11-15-11`). Stage G drops that charge or folds it into the health contribution. In FY2040 it is roughly $0.2T of the $484B income-contribution row (rough arithmetic; it phases in to 2044). So dropping it raises the gap by about that much unless other rows replace it.

**Risks to the gap:**

2. **D2's risk.** The national health budget saves $249B in FY2040. Holding growth near GDP's has never been done [EV-CAR-742]. Stage G reports the gap without D2 (about **$852B** in FY2040) beside the gap with it ($603B) (`DEC-2026-11-15-08`).
3. **Health's sources exceed its need by about $0.9T over FY2030-34** (#394, restated after #402; `first_call()`: −$883B). `DEC-2026-11-15-29` pays them into the plan's fund. Stage G decides whether that is held as a reserve or counted against the rest of the plan's gap. The budget model books it on the general fund, as it books all of the plan's revenue.

**The top end:**

4. **The capital-income stack cap.** Gains taxed as ordinary income above $1M, H1b, C18, the 45% bracket above $5M, G11's mark-to-market and a 2% wealth tax can together pass 100% of the wealthiest households' return [EV-CAR-736]. Stage G adds up the stack, as `health-financing.md` 2.4 does for wages, and caps the wealth and accrual taxes together (`DEC-2026-11-15-16`; `health-cost-review.md` 2.8). The wealth tax ($150B) carries high legal risk. If it fell, booked revenue taken would rise by about that much (`health-cost-review.md` 2.8).
5. **The top rate on wages across flagships:** about 67.7% with health, against 63.0% before (`health-household-contribution.md` 2; `health-financing.md` part 9, "For stage G").

**Settling the gap:**

6. **Which flagships give way:** which rows, and which flagships are cut or refinanced, to cover health's $532B. Health's share comes from the top-end and corporate rows first (`DEC-2026-11-15-20`).
7. **The 20% avoidance allowance, set by tier.** It was set for high-income tiers. On a broad base collected by withholding, avoidance is likely smaller, so the gap may be overstated. Each 10 points moves booked revenue taken by about $104B (`health-household-contribution.md` 7).
8. **The budget model's payroll point against CBO's.** Its $135B a point for 2030 looks like CBO's capped taxable payroll ($131.6B), read as all pay. On all covered earnings a point is about $158B. Items priced on a capped base are slightly overstated, and items on all pay understated (`health-household-contribution.md` 6).
9. **SS-8,** the trust funds' stock investment, is booked at zero. Stage G needs CBO's and OMB's treatment of the purchases: outlays, a means of financing, or returns above Treasury's rate.

**Small follow-ups from #394,** none needing a decision:

10. The D3 household rows for health (`incidence-rows.csv` H7h, H7w, H7x) are still on the care dossier's uncorrected path, and the package's new rows have no incidence rows. *Done in #402.*
11. HLT-7's status-rule component stays on the care dossier's base, so it reads slightly high. *Done in #402: on the corrected base the saving is −$18.0B in FY2040 (was −$33.0B), which raised the gap by about $15B.*
12. HEC's after-window path leaves out the no-offer phase-in's last steps (2040-44), and D2's after-window path is cautious. Both err low on revenue, which is the cautious side. *HEC's part was done in #402 (FY2045's gap fell from $694B to $661B); D2's after-window path is unchanged.*
13. The 0.9% Additional Medicare Tax ($53.5B) is a working figure and probably low, nearer $70B. If it is higher, booked revenue taken rises by the same amount (`health-household-contribution.md` 6).

**Carried from the earlier checkpoint and `health-financing.md` part 9:**

14. The states' shares across health, long-term care, child care and pre-K, taken together (`DEC-2026-11-11-05`).
15. Whether to weigh Medicare "Part E" (board, "Directions for later stages"). It would reopen the 2035 endpoint.
16. How strictly to phase revenue to the FY2040 test and to the decade's debt path.

**Outside the settlement:** Espen's calculator page still shows package A.

## Part E. How the Medicare for All bills propose to pay, beside this plan

A comparison only. It changes no decision and no booked figure. `health-financing.md` part 7 holds the fuller comparison, Warren's 2019 plan included. This part keeps the two bills and the Sanders options paper.

Sources:
- Sen. Sanders's S. 1506 (SRC-3260) and his options paper (SRC-3041);
- Rep. Jayapal's H.R. 3069 (SRC-3261);
- the care dossier's comparison (`dossiers/care/research-s1506-comparison.md`, row "Trust fund and financing").

**What was found.**
- **Neither bill levies a tax.** Sec. 701(b)(1) of each credits the trust fund with 100 percent of the net revenue increase "attributable to" secs. 801 and 902, the end of duplicative employer plans and of the Exchanges [EV-CAR-287, EV-CAR-292]. The bills set no rate and no base. A search of H.R. 3069's text found no tax rate, employer contribution or state payment.
- **Sanders's options paper is a menu, not a plan.** It is the sponsor's own, undated, and written before S. 1506: it cites 2016 premiums and 2014 tax data. Sanders's site holds no 2025 version (searched November 13, 2026). Its main options [EV-CAR-713]:

| Option in the paper | Rate | Base and exemption | Revenue the paper claims, ten years |
| --- | --- | --- | --- |
| Employer income-based premium | 7.5% | Payroll; an employer's first $2 million exempt | $3.9T |
| Household income-based premium | 4% | Income after the standard deduction; a family of four under $29,000 pays none | $3.5T |
| End health tax expenditures | — | The employer-premium exclusion, cafeteria-plan exclusion, medical-expense deduction | $4.2T |
| More progressive income tax | 40% to 52% | Income above $250,000, capital gains taxed as work income, itemized deductions capped at 28% | $1.8T |
| Wealth tax | 1% | Net worth above $21 million, top 0.1% of households | $1.3T |
| Estate tax | 45% to 55% | Estates above $3.5M single or $7M couple, plus a 10% surtax above $500M | $0.25T |
| Offshore profits, bank fee, business-owner loophole, LIFO repeal | one-time tax; 0.07%; —; — | Corporate and financial | $0.77T, $0.12T, $0.25T, $0.11T |

All of these sum to about $16.2T (project arithmetic). The paper states no cost for the program, so it can't say whether that covers it.
- **Jayapal has published no separate financing plan that could be found.** In February 2019 she said she would release a list of suggested funding mechanisms for her earlier bill [SRC-3079]. Nothing like it turned up for H.R. 3069. An absence is hard to prove.

**How far to trust the paper's figures.** They are the sponsor's own estimates, grade C analysis [EV-CAR-714]. Two independent scorers looked at a later version of the options, from February 2020, so they qualify the figures rather than confirm them [EV-CAR-715, EV-CAR-716]:
- CRFB agreed with the campaign's $12.2T for three direct offsets, and with its $5.2T for the employer tax on the campaign's method. CRFB's own earlier estimate of that tax was $4T, and it puts the difference down to how interactions are distributed.
- The Tax Policy Center put the earmarked provisions at $13.4T for 2021 to 2030. The paper's five main items add to about $13.65T, so the totals are close, but the versions, windows and sets of items differ.
- The later version's household premium, employer premium and exclusion figures ($4.0T, $5.2T, $3.0T) differ from the paper's ($3.5T, $3.9T, $4.2T). Rely on the paper for what it proposes, not for what it raises. All of this predates the 2025 law's changes to the tax base.

**Side by side,** with `health-financing.md` part 7's three corrections:

| | Sanders (bill plus options paper) | Jayapal (House bill) | This plan, as decided |
| --- | --- | --- | --- |
| What the bill text funds | A trust fund fed by last year's federal Medicare, Medicaid, FEHB and similar money, by the Medicare trust fund amounts left after claims are paid, and by the revenue from ending employer plans and Exchange credits [EV-CAR-287] | The same, plus TRICARE's purchased care [EV-CAR-292] | The same federal streams, committed to the plan's fund, plus the tax on former premiums, all named as sources ($2,876B and $358B in FY2040) |
| New taxes, and where | None in the bill. The paper offers the menu above | None in the bill; no separate plan found | In law: a household contribution of 2.25% of AGI plus 5.96 points above $205,400/$256,750, replacing the worker's Medicare taxes; five top-end and corporate streams ($385B) |
| What employers pay | Nothing in the bill. The paper: 7.5% of payroll above $2 million. In the four-year transition, per enrolling employee, the higher of that or 75% of today's premiums | Nothing in the text | What employers as a whole would otherwise spend: 19.3% of pay between $20,000 and the wage base, less the first $100,000 of each firm's pay; mandatory, with pay protections ($1,945B) |
| What states pay | Eligibility standards and other state-plan services kept, with the federal match, and a floor for institutional long-term care spending (sec. 204) [EV-CAR-278] | Nothing; long-term care moves into the program [EV-CAR-291] | 100% of their former Medicaid spending for the people who move, outside long-term care, indexed ($466B) |
| The gap left open | All of the program's new money; the paper doesn't price the program | The same, with no menu | None for health: health's $532B call on booked revenue is part of the plan-wide $603B gap that stage G closes |

**An illustration for two families of four with one earner and employer coverage, on the paper's terms. This is not a model result.** It compares what the paper's household premium would cost with the worker premiums the family stops paying. Premiums are KFF's 2026 averages: $28,303 for family coverage, of which workers pay $7,471 [EV-CAR-111, EV-CAR-112], so employers pay about $20,832. Incomes are the household model's 2029 averages by quintile (`models/tools/household/results.md`, section 3).

| Family of four, one earner | Pays the 4% premium | Stops paying (worker share) | Difference for the family | Employer's side: 7.5% of pay against the premium it stops paying |
| --- | --- | --- | --- | --- |
| Fourth quintile, $173,693 | 4% of ($173,693 − $29,000) = about $5,800 | about $7,500 | about $1,700 better off | about $13,000 against $20,800 |
| Middle quintile, $110,181 | 4% of ($110,181 − $29,000) = about $3,200 | about $7,500 | about $4,200 better off | about $8,300 against $20,800 |

What it leaves out:
- it assumes the earner's pay is the whole income, an average employer plan and a large employer, so the $2 million payroll exemption doesn't bite;
- it uses the paper's $29,000 deduction, which CRFB equates to the pre-2018 standard deduction and exemptions, not today's;
- it leaves out out-of-pocket costs saved, the other options, and the tax that ending the exclusion adds on former premiums that become pay.

Who bears the employer's share is contested; studies find workers bear part of it through lower pay [EV-CAR-296, EV-CAR-299]. For this plan, the like-for-like figures are in `health-household-contribution.md` 3, and the take-home grid is in `health-cost-review.md` 2.5.
