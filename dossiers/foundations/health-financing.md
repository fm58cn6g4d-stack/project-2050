# Paying for the single health plan: pricing and financing, a fresh start

Role: the stage E memo on how the single health plan (HLT-1 to HLT-8) is paid for, year by year in the transition (FY2030-34), at the 2035 endpoint and at full adoption (FY2040). It replaces part B of `checkpoint-financing.md`, the health parts of its "In plain terms", part C's arithmetic, and part D's questions (memos F1 to F3 and part B4's points); those parts are marked superseded there. Status: **for Espen's decision, November 15, 2026.** It recommends and books nothing: the questions in part 8 are Espen's, and any booking that follows is a separate tier-3 change to adopted inputs. The health design is decided (care memos 1 to 5: `DEC-2026-11-10-09` to `-13`, `DEC-2026-11-12-19`, `DEC-2026-11-13-02`) and is not reopened; where a design choice drives the cost, part 7 flags it with its size. Federal fiscal years, nominal dollars, $B = billions, $T = trillions, case `mixed`. **Every figure is project arithmetic on the project's own exploratory models, not an official score.** The figures come from one run of `models/tools/health_financing.py` (tests: `models/tools/test_health_financing.py`). It builds on the handover notes (`notes/health-financing-findings-2026-11-15.md`), whose findings it confirms, corrects (part 3.6: the top rate) or extends.

## In plain terms

1. **The country pays less.** National health spending in FY2040 is about **$12.4 trillion under today's law and $11.7 trillion under the plan: about $0.8 trillion (6%) less**, while about 34 million more people are covered.
2. **Every dollar now has a named payer.** The first draft had about $0.86 trillion (FY2040) with "no named payer". It is three things: a mistake in the model's starting point for Medicare (about $0.26 trillion), money real payers spend today that the model hadn't assigned (about $0.33 trillion), and care for uninsured people that hospitals, states and charities pay for today (about $0.27 trillion).
3. **The mistake is fixed, and it makes the plan cheaper to finance.** The model started Medicare from an older government projection that is higher than the Congressional Budget Office's. Using CBO's figure, as the project's rules require, lowers the plan's booked federal cost by about **$0.30 trillion in FY2040** (about $1.3 trillion over FY2030-39). The amount to finance in FY2040 is about **$3.79 trillion**, not $4.09 trillion.
4. **Your question, answered: yes.** In FY2040 households, employers, states and the other payers stop paying about **$5.7 trillion**. The new public money the plan needs is about **$4.8 trillion**. The difference, about $0.8 trillion, is the national saving. The first draft said the two were "about equal" only because it left payers out and carried the mistake.
5. **The recommended design (package A): everyone who pays for health care today keeps paying what they pay now, but into the public plan, fairly.**
   - **Employers** pay a health contribution equal, in total, to the premiums they pay today: about **14.3% of each worker's pay up to the Social Security wage base** (about 11.9% of all pay). With the existing 1.45% Medicare tax, that is 15.75% on pay below the base.
   - **States** keep paying what they pay now for the Medicaid patients who move into the plan (100%, growing with the plan's costs). Nursing-home care stays with Medicaid.
   - **Households** pay a health contribution of about **10.8% of income above $20,000 (single) or $40,000 (couple)**, collected with the income tax, in place of premiums, deductibles and copays. Because of that line, the middle fifth pays about **5.5% of its total income**, and it stops paying about 10.4% of its income in premiums and out-of-pocket costs.
   - **The Medicare payroll tax stays** at 1.45% each for workers and employers. It already pays for Medicare's hospital care and moves into the plan's fund in 2035. Workers' payroll tax does not go up at all under package A.
6. **Your 5-6% household rate, plainly.** It is reachable only by finding about **$1 trillion a year** somewhere else. The top end is already used: with the plan's other taxes, the top federal rate on wages is about 63% before health (the handover notes missed the Social Security piece). The other ways are a value-added tax of about 12% with a rebate (package B), or employers paying about 23% of pay (package C). Both leave the bottom three fifths worse off than package A. A higher top rate (package D) would push the top federal rate on wages past 80%, where on the evidence it would raise little.
7. **What households get under package A** (FY2040, average per household a year): the poorest fifth about **+$6,100**, the second **+$9,100**, the middle **+$8,600**, the fourth **+$1,600**. The top fifth pays about $20,400 more, the top 1% about $131,000 more. A family of four with job coverage and $90,000 of pay comes out about $19,500 a year ahead (in today's dollars).
8. **Who loses.** About **34 million households in the bottom four fifths** pay more in cash than they save (out of about 121 million). Most are workers whose employers don't offer coverage today: their pay bears the new employer contribution with no premium savings to offset it. Most of them gain coverage they don't have now, which this count leaves out. Part 5.4 describes them, and a softer phase-in for those employers is one of the questions in part 8.
9. **The transition years.** Each payer starts paying when its group moves. The household contribution starts low, about **3% in 2031** when children and the uninsured move, rises to about **5.5% by 2034**, and reaches about **10%** from 2036.
10. **The main risks.** The household rate drifts up about 0.1 point a year if health costs keep growing faster than incomes. The plan's top tax rates are already near what the evidence says raises the most. The cost depends most on the decided payment rate (1.15 times Medicare). All of it rests on the project's own models.

## Part 1. The whole picture: who pays for health care, today and under the plan

### 1.1 The Medicare seam, fixed

The coverage model (`models/tools/health-coverage/`) starts Medicare from CMS's national health expenditure projection, made before the 2025 law and grown 7.7% a year: $2,024B in 2032. CBO's February 2026 baseline puts Medicare's 2032 mandatory outlays at **$1,867B**, with $340B of premiums and other receipts [EV-CAR-718]. The project's baseline is CBO's (`DEC-2026-11-08-03`). So this memo re-runs the coverage model with Medicare at CBO's gross and its federal net at CBO's gross less receipts ($1,526B, against the subsidy table's $1,511B). Nothing else changes.

| Effect of the rebase on the decided path | 2032 full scale | FY2035 | FY2040 | FY2030-39 |
| --- | --- | --- | --- | --- |
| Net federal cost, today's Medicare enrollees | −181 | | | |
| Net federal cost, people newly covered (their average claims fall with Medicare's) | −14 | | | |
| **Booked federal cost reads high by** | **−196** | **−178** | **−300** | **−1,281** |

Before the endpoint the seam is small (about $10-16B a year, through the newly covered), because today's Medicare enrollees move only in 2035. **The financing below is sized to the rebased cost.** The booked rows stay as they are until a tier-3 booking PR rebases HLT-7 (part 9). The booked reading is shown beside each result as the cautious case: it adds about 1.7 points to the household rate.

### 1.2 National health spending by payer, both ways

At the full-scale year (2032, coverage model, decided variant, rebased), with every dollar on a named payer ($B):

| Payer | Today | Under the plan, before its new financing | Change |
| --- | --- | --- | --- |
| Federal: Medicare (net of premiums), Medicaid's federal share, premium credits; under the plan, the plan's outlays net of the states' payment, plus Medicaid long-term care's federal share | 2,405 | 5,601 | +3,196 |
| States: Medicaid's state share; under the plan, the states' payment (the booked 50%) plus long-term care | 614 | 389 | −225 |
| Employers: premiums (including $65B for people the model counts twice, below) | 1,611 | 0 | −1,611 |
| Households: premiums, Medicare's Parts B and D and Medigap, out-of-pocket costs (including $152B the model hadn't assigned, below); under the plan, copays above 200% of poverty and costs outside the plan | 1,891 | 186 | −1,705 |
| Hospitals, states and localities and charities: care for uninsured people today | 174 | 0 | −174 |
| Other health spending the plan doesn't take over (the VA, defense health, public health, research, structures, and so on) | 1,423 | 1,423 | 0 |
| **National health spending** | **8,119** | **7,600** | **−519 (−6.4%)** |

On FY2040's scale (×1.533, the booking's path for the full-scale amounts): **today $12,447B, the plan $11,651B, −$796B.** Before the rebase the columns were $8,276B and $7,785B (2032) and $12,688B and $11,936B (FY2040): the rebase lowers both columns by about the same amount, so the saving barely moves.

**The "no named payer" term, line by line** (2032; FY2040 is ×1.533). It was $389B on the four lines the plan takes over, plus $174B of care others pay for:

| Line | 2032 ($B) | Who pays it | Treatment here |
| --- | --- | --- | --- |
| CMS's Medicare figure above CBO's | 157 | Nobody: a seam in the model | **Removed** by the rebase |
| CBO's net Medicare above the subsidy table's | 15 | Federal (already in CBO's net) | **Removed** by the rebase |
| Medicare's premiums and other receipts the model leaves out (CBO's $340B less the model's $248B at $3,500 a person) | 93 | Enrollees (premiums above the model's average) and states (their Part D payments) | Named: households (working split; the states' part is not separated) |
| Private premiums for about 7 million people the model counts twice | 88 | Employers ($65B) and workers ($23B), at the model's employer share of private premiums | Named |
| Other private premiums; other out-of-pocket costs | 20; 16 | Households | Named |
| Care for the uninsured paid by others | 174 | Hospitals' uncompensated care, state and local programs, charity | Named; ends when nearly everyone is covered |

**The identity, every term named** (2032): new federal spending $3,196B = what everyone else stops paying, $3,715B (households $1,705B, employers $1,611B, states $225B, others' care for the uninsured $174B), less the national saving, $519B.

### 1.3 The direct answer: is the new money less than what people stop paying?

**Yes, by the national saving, about $0.8T in FY2040.**
- Everyone else stops paying about **$5.70T** (households $2.61T, employers $2.47T, states $0.34T, others' care for the uninsured $0.27T; FY2040 scale).
- The plan's new federal spending is about **$4.90T** on the model, or **$4.76T** as booked and rebased (the booking adds what the model doesn't price and takes off the status rule and federal coverage; part 2).
- Of that $4.76T, about $0.97T would come back automatically as income and payroll tax on former premiums (HX) if employers paid their premiums out as pay. Under package A they keep paying them as the contribution instead, so HX keeps only about $0.28T. The new contributions and taxes are therefore about **$4.76T gross**: employers $2.20T, households $1.94T plus $0.28T of HX, states $0.34T.

**Why the first draft found "about equal".** It compared the new federal money ($5.06T, before the rebase) with what households, employers and states stop paying ($5.09T), leaving out $0.6T that other payers stop paying and keeping the $0.26T seam. Named in full, the comparison is $4.76-4.90T against $5.70T.

**Why households still pay in more than some of them save.** Households as a whole stop paying $2.61T of premiums and out-of-pocket costs (FY2040, named). Under package A they pay $1.94T of contribution and $0.28T of HX, and they carry the employer contribution in place of the pay rise their employers' premium savings would otherwise give. They come out ahead in total. The money moves from those who pay a lot for coverage today, relative to their income, toward those with higher incomes: the bottom four fifths gain on average, and the top fifth pays (part 5).

## Part 2. Year by year, FY2030-40

The amount to finance is the booked health rows (HLT-1, -2, -6, -7, -8, health's parts of HLT-4, and HX), less the seam ($B):

| FY | Booked spending | HX | Booked net | Seam | **To finance** | Households stop paying | Employers stop paying (all) | States' former spending on movers | National spending change (model) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2030 | 50 | 0 | 50 | 0 | **50** | 0 | 0 | 0 | 0 |
| 2031 | 590 | −49 | 541 | −10 | **531** | 246 | 121 | 92 | +136 |
| 2032 | 860 | −68 | 792 | −14 | **778** | 341 | 168 | 127 | +188 |
| 2033 | 1,419 | −221 | 1,198 | −15 | **1,183** | 554 | 543 | 219 | +11 |
| 2034 | 2,136 | −441 | 1,695 | −16 | **1,679** | 855 | 1,082 | 350 | −250 |
| 2035 | 3,549 | −683 | 2,866 | −178 | **2,688** | 1,605 | 1,677 | 494 | −540 |
| 2036 | 4,091 | −775 | 3,316 | −241 | **3,075** | 1,904 | 1,903 | 553 | −639 |
| 2037 | 4,310 | −819 | 3,491 | −254 | **3,237** | 2,011 | 2,010 | 584 | −674 |
| 2038 | 4,551 | −865 | 3,686 | −269 | **3,417** | 2,125 | 2,124 | 617 | −713 |
| 2039 | 4,791 | −914 | 3,877 | −284 | **3,593** | 2,245 | 2,244 | 652 | −753 |
| **2040** | **5,060** | **−966** | **4,094** | **−300** | **3,794** | **2,372** | **2,372** | **689** | **−796** |
| FY2030-39 | 26,347 | −4,835 | 21,512 | −1,281 | **20,230** | | | | |

What the years show:
- **FY2030-33:** the restoration (HLT-1, 2030), Medicare's upgrades (HLT-2) and wave 1 (the uninsured, the individual market, every child, Medicare at 60, from January 2031). National spending is slightly higher in these years (about +$0.1-0.2T), because newly covered people use more care before the employer groups' lower prices arrive.
- **FY2033-35:** wave 2 moves Medicaid and employer groups by thirds; national spending falls from FY2034.
- **FY2035, the endpoint:** today's Medicare enrollees move; the HI fund folds into the plan's fund (HLT-7.22).
- **FY2036 on:** full adoption; the hospital glide reaches 1.15 times Medicare in 2036.

The year-by-year payer shares (households, employers, states, other payers, national) are in `health_financing.py`, `payer_path()`. They follow the 2032 table group by group as each group moves.

## Part 3. What there is to pay with

### 3.1 Employers

- **Today:** about $2.37T of premiums in FY2040 (all employers), about 11.9% of all pay. The private, state and local employers' part, without FEHB, TRICARE and the VA, is $2.20T: the booking already treats the federal government's own share as federal money (`health_booking.py`, `FEDCOV_REVENUE_2032`), so the government doesn't count a contribution it pays to itself.
- **Under the plan, recommended: 100% of former premiums, in total.** In the transition, each employer pays its former premiums for the workers who have moved (HLT-7.18 as designed, at 100% instead of the working 65%). From the January 2035 endpoint, every employer pays a payroll contribution of the same total yield.
- **Why 100%:**
  - Employers as a whole pay exactly what they pay now, so total pay doesn't depend on whether they pass savings into wages. At the first draft's 65%, employers keep about $0.4T a year if they pass on only half their savings [EV-CAR-299], and that package's fourth fifth falls to about −$3,200 (part 4.4).
  - It is the largest and least visible piece: no worker sees a new deduction.
- **Its base, recommended: each worker's pay up to the Social Security wage base** (about $205,000 in 2029, indexed), collected with the existing payroll tax. About 83% of all pay is below the base (household model, CPS, less three points for top-coding; a working figure), so the rate is about **14.3%**.
  - A premium is a per-worker amount: today, no employer's premium rises with a top executive's pay. A capped contribution keeps that, and so adds nothing to the top tax rate on wages (part 3.6).
  - On HI's uncapped base the rate would be **11.9%** (13.3% with HI's 1.45%). On a static reading that is about $150-1,800 a year better for the bottom four fifths. But it adds 11.9 points at the top, and on the evidence most of that wouldn't be collected (part 3.6).
- **The employer side alone and with the existing HI tax** (package A, FY2040):

| | On pay below the wage base | On pay above it | Average on all pay |
| --- | --- | --- | --- |
| New health contribution | 14.3% | 0% | 11.9% |
| Existing HI tax, employer's half | 1.45% | 1.45% | 1.45% |
| **Employer total** | **15.75%** | **1.45%** | **13.3%** |
| For comparison: today's premiums, paid only by employers that offer coverage | — | — | about 11.9% of all pay |

- **The net yield** is $2,197B gross less $686B of HX that is never collected, because the premiums don't become taxable pay: **$1,511B** in FY2040.
- **Who pays more and who pays less.** Employers that offer generous coverage to lower-paid workers pay less than today. Employers that offer none pay a new 14.3%. Their workers bear it over time through slower pay growth, and they are the main group that loses (part 5.4). Part 8, question 5 asks whether to phase it in for those employers.
- **The self-employed** pay it on 92.35% of net earnings, as SECA does for HI, in place of the individual-market premiums they buy today (worked example, part 5.3). The alternative, exempting them, invites relabeling employees as contractors.

### 3.2 States

- **Today:** Medicaid's state share for the people who move, about $689B in FY2040 (non-long-term-care).
- **Booked:** they keep paying 50% of it, as a maintenance of effort (memo 3 B; HLT-7.17).
- **Recommended: 100%,** growing with the plan's costs. The states then pay exactly what they would have paid, and the extra $344B in FY2040 lowers the household rate by about 1.9 points. States still gain: hospitals' uncompensated care ends (part of the $0.27T), their share of Medicare's Part D payments ends, and their employees' premiums become the employer contribution at the same total cost.
- **Each 10 points of the share is about $69B in FY2040.** At 80% the household rate is 11.5%, at 50% 12.7%, and at 0% 14.6% (part 4.4).
- **The legal risk** is the same at any share: the payment rests on a clawback-style obligation, and *NFIB v. Sebelius* limits coercion (HLT-7.17). The fallback if it fails is 0%.
- **Long-term care stays with Medicaid** (HLT-7.07), as decided; it is outside these figures.

### 3.3 The Medicare payroll tax (HI), the 2035 fold-in, and Medicare's premiums

- **HI stays.** The 2.9% tax (1.45% from workers, 1.45% from employers, on all pay; 2.9% on self-employment income) and the 0.9% Additional Medicare Tax above $200,000/$250,000 raise about **$0.58T** in FY2040 (2.9% times the budget model's payroll point, approximate). They are already in CBO's baseline and already pay for Medicare's hospital care, so they are part of the federal money the plan replaces, not new money.
- **The fold-in.** Until 2034, HI pays Medicare Part A claims. From the January 2035 endpoint its revenue goes into the plan's fund (HLT-7.22; memo 3 B). That changes where the money is credited, not how much there is. Repealing HI would add about $0.58T to the need. HI's projected solvency to 2040 on its program sources (care `6-cost.md`, part 5) is only quoted to the endpoint.
- **Medicare's premiums end** for today's enrollees at the endpoint (Part B and D and, in practice, Medigap). That is about $248B in 2032 on the model's $3,500 a person, and up to the $340B CBO counts with the states' Part D payments. It is in the households' "stop paying" column, and the plan's cost already covers it, because the plan pays Medicare's gross cost and replaces only its net. Until 2035, enrollees keep paying premiums and get the upgrades (HLT-2).
- **Where each payroll-tax piece goes by law:**

| Piece | Rate and base | Goes to, by law |
| --- | --- | --- |
| HI tax (IRC 3101(b)(1), 3111(b), 1401(b)) | 1.45% + 1.45% on all pay; 2.9% on self-employment income | HI trust fund (Social Security Act sec. 1817); **the plan's fund from 2035** (HLT-7.22) |
| Additional Medicare Tax (IRC 3101(b)(2)) | 0.9% on pay above $200,000/$250,000 | HI trust fund; the plan's fund from 2035 |
| H1b: Medicare and investment-income tax to 5% above $400,000 (booked, another flagship's) | +1.2 points | Booked on the general fund; its payroll part would by law go to HI unless the law says otherwise |
| Net investment income tax (IRC 1411) | 3.8% | General fund |
| SS-1: 12.4% on earnings above $250,000 (decided, secure floor) | 12.4% | Social Security trust funds |
| **New employer health contribution** (this memo) | 14.3% up to the wage base | **The plan's fund**, by the plan's law (HLT-7.22); the budget model books it on the general fund |
| **New household health contribution** (this memo) | 10.8% of income above $20,000/$40,000, with the income tax | **The plan's fund**, the same way |
| HX's payroll-tax part (tax on former pre-tax premiums now paid as pay) | Both shares | By law to the Social Security and HI trust funds; booked on the general fund (care `6-cost.md`, part 5, item 4) |
| HX's income-tax part | — | General fund |

### 3.4 HX: the tax on former premiums

- **What it is.** Ending the exclusion for job-based coverage makes former premiums taxable when they are paid as pay. It covers **both premium shares**: the employer's share (taxable only if it becomes pay) and the worker's share (paid before tax today through cafeteria plans, taxable once premiums end). As booked it is **$966B** in FY2040, on CBO's convention that total pay is fixed. The exclusion's tax value is 31% of all premiums (`tau`), on JCT's estimate [EV-CAR-052].
- **It falls when employers keep paying.** Premiums that go to the contribution never become pay. At 100%, HX falls by 31% of $2,197B, that is $686B, and keeps **$279B**: the tax on the pay workers used to put into premiums before tax.

| Package | Employers' share | HX kept, FY2040 ($B) |
| --- | --- | --- |
| As booked (no contribution) | 0% | 966 |
| First draft | 65% | 520 |
| A, B, D (recommended share) | 100% | 279 |
| C | 163% | none: −151, because pay falls and less tax is paid on it |

- **The household rows now use the booked HX** ($966B, without federal coverage), not the earlier $1,043B, which charged households about $77B the booking doesn't collect.

### 3.5 Households: the income-based health contribution

- **The design:** a single rate on adjusted gross income above $20,000 single or $40,000 joint (price-indexed), collected with the income tax and by withholding, as the budget model's booked 2 broad points are. It is not a payroll tax: it falls on wages, pensions and investment income alike, and the line keeps it off low incomes.
- **The yield:** about $225B a point gross in FY2040, $180B collected after the budget model's 20% allowance for avoidance (part 3.8). The base is about **$22.5T** in FY2040 (the budget model's yield; the CPS grown gives $22.2T).
- **The booked 2 points.** The household contribution sits beside the 2 points above $20,000/$40,000 already booked for other flagships from 2035. A household's combined rate on that base is therefore health's rate plus 2.

### 3.6 General revenue: what is left

- **The top end is used.** The other flagships already book the top-end taxes the Sanders options paper used for health: G1 (corporate rate to 28%), G9 (the 39.6% bracket), G6 and G11 (gains at death and yearly at the very top), H1b, C18 and others, about $8.0T over FY2030-39 (`legacy/sources/revenue-counted-reconciliation.md`).
- **The combined top federal rate on wages is about 63% before health:** 39.6% income tax, 12.4% Social Security above $250,000 (SS-1), 5% Medicare (H1b), and the booked 4 + 2 income points. The handover notes' 50.6% left out SS-1. With a top state rate it is about 76%.
- **The evidence.** Diamond and Saez's revenue-maximizing top rate is about 73%, counting federal, state, payroll and sales taxes (`legacy/domains/domain-revenue.md`, "Combined top rates"). Saez, Slemrod and Giertz put the elasticity of reported income at about 0.12-0.4, concentrated in the top 1%.
- **The stacking check** (`stacking_check()`). At an elasticity of 0.25, the top 1%'s income shrinks as the rate rises, and the taxes already on it shrink with it. Counting both:

| Package (FY2040) | Top federal rate on wages, with health | Share of the top 1%'s new charge actually collected (elasticity 0.25) | Household rate if that is all it yields |
| --- | --- | --- | --- |
| A (employer contribution capped) | 73.8% | about 44% | 11.2% (0.12: 10.8%; 0.4: 11.7%) |
| A on the uncapped HI base | 85.6% | about 20% | 12.7% (0.12: 11.5%; 0.4: 13.9%) |
| D (5.5% plus a 14.2-point top tier) | 82.7% | about 27% | the top tier raises a fraction of its static yield |

- **Cap or no cap.** On the static reading the uncapped base is better for the bottom four fifths. At an elasticity of 0.25 the capped base does as well or better for them (the fourth fifth about +$1,000 against +$300) and is far more robust. **Recommendation: cap it.**
- **What is left otherwise:** small top-end and corporate items, each well under $0.1T a year: a financial transaction tax at 0.01% (about $0.4T over the decade), full-rate tax on foreign income, LIFO repeal and similar (legacy menu). The rest is broad bases: more on the income contribution, a payroll tax, or a value-added tax (about $105B a point in FY2040, before any rebate, on CBO's estimate).

### 3.7 Savings: a sensitivity, not booked

- **Administration at 3%** of spending instead of the working 5%: −$181B in FY2040. Traditional Medicare's administration was 1.4% in 2017 [EV-CAR-217]. Administration at 5% is decided as the working figure.
- **Drug prices 23% below today's** instead of 15%: −$67B. This is CBO's lower-rate scenario [EV-CAR-220].
- **Together, about $249B in FY2040,** about 1.4 points of the household rate. They are not booked: the plan's administrative budget and drug negotiation are set in the specification, and the evidence supports them only as upside. Package A with them: 9.4%, the fourth fifth about +$3,900.

### 3.8 Avoidance, where it happens

- **The allowance.** The budget model's income-contribution yields carry a 20% allowance for avoidance (`assumptions.json`, `tax.additional_yield_haircut`), on top of JCT's own behavioral response.
- **Where it falls.** The base is AGI, so itemized deductions can't shrink it. Withheld wages are misreported at about 1%, against 55% for income nobody reports [EV-CAR-719]. Measured responses below the top are small, 0.11-0.18 for taxable income, against 0.57 above $100,000 in 1992 dollars [EV-CAR-720].
- **So the household tables charge every household the statutory amount** (rate × its base) **and credit the whole shortfall to the top fifth**, shared within it in proportion to the charge.
- **The range:**
  - "elastic" (Gruber and Saez's elasticities on every fifth): the fourth fifth +$2,600 under package A;
  - "even" (the first draft's method, not supported by the evidence): +$5,200.

## Part 4. The packages

All four close FY2040's $3,794B exactly. All four put states at 100% and the employer contribution on pay up to the wage base; A, B and D keep employers at 100% of former premiums.

### 4.1 The forks at a glance

| | **A. Premiums become contributions (recommended)** | B. Mid-single digits with a rebated VAT | C. Mid-single digits through employers | D. Mid-single digits with a top tier |
| --- | --- | --- | --- | --- |
| Household contribution above $20K/$40K | **10.8%** | 5.5% | 5.5% | 5.5% |
| Second tier above $100K/$200K | — | — | — | 14.2 points |
| Value-added tax (a quarter rebated per person) | — | 12.0% gross | — | — |
| Employer contribution, pay up to the wage base (with HI's 1.45%) | 14.3% (15.75%) | 14.3% (15.75%) | 23.3% (24.7%): 163% of former premiums | 14.3% (15.75%) |
| Employer contribution as a share of all pay (with HI) | 11.9% (13.3%) | 11.9% (13.3%) | 19.3% (20.8%) | 11.9% (13.3%) |
| Workers' payroll tax | 1.45% (HI, unchanged) | 1.45% | 1.45% | 1.45% |
| HX kept ($B) | 279 | 279 | −151 | 279 |
| Top federal rate on wages | 73.8% | 68.5% | 68.5% | 82.7% |
| FY2040 yield ($B): employers net / states / households | 1,511 / 344 / 1,939 | 1,511 / 344 / 991 + 947 VAT net | 2,458 / 344 / 991 | 1,511 / 344 / 991 + 947 |
| **Net per household, FY2040: Q1 / Q2 / Q3 / Q4** | **+6,120 / +9,077 / +8,612 / +1,648** | +4,298 / +6,665 / +7,048 / +2,491 | +5,598 / +7,925 / +7,764 / +1,751 | +6,251 / +10,440 / +12,750 / +9,163 |
| Q5 / top 1% | −20,370 / −130,963 | −15,414 / −98,176 | −17,951 / −85,035 | −33,517 / −408,920 |
| Households in the bottom four fifths who lose (millions, of about 121) | 34.4 | 39.1 | 36.6 | 23.2 |
| New collection machinery | None: income tax and payroll tax | A federal VAT | None | None |
| On the evidence | Holds; at the top about half collected (part 3.6) | Holds; regressive in the middle | Holds; workers bear it through pay, from the first dollar | **Doesn't hold**: about a quarter of the top tier collected |

### 4.2 Why A

- **It asks each payer for what it pays today:**
  - employers their premiums;
  - states their Medicaid share;
  - households a contribution in place of premiums and deductibles that, for the middle fifth, is about 5.5% of income against the 10.4% they stop paying.
- **It leaves the bottom three fifths best off** of the three credible packages (A, B, C).
- **It adds no worker payroll tax.**
- **It uses only existing machinery:** income tax withholding and the payroll tax system. There is no new federal VAT and no new premium collection, as the design lens asks (`DEC-2026-11-13-08`).
- **It doesn't meet a 5-6% statutory household rate.** In effective terms it does: the middle fifth pays about 5.5% of its income and the second fifth about 3%.

### 4.3 What reaching 5-6% costs, package by package

- **B (a rebated VAT):**
  - a federal VAT of about 12% (gross; a quarter returned as a flat rebate of about $560 a person in today's terms) on top of state sales taxes;
  - the bottom three fifths lose $1,600-2,400 a year against A, and 4.7 million more bottom-four households lose;
  - a new collection system for federal government.
  - At 6% the VAT is 10.9%; at 5%, 13.2%. With the savings booked, 8.9%.
  - If Espen's 5-6% includes the workers' existing 1.45% HI tax (a new health contribution of about 4%), the VAT is 15.4%.
- **C (employers pay more):**
  - employers pay 163% of their former premiums, 23.3% of pay below the wage base;
  - in the long run workers bear it through pay, from the first dollar, with no line. It is a worker payroll tax in all but name;
  - the bottom three fifths do slightly worse than under A;
  - for an employer that offers no coverage today, a 23% jump in labor cost.
- **D (a top tier):**
  - 14.2 more points above $100,000/$200,000 take the top federal rate on wages to about 83%;
  - on the evidence most of it would not be collected (part 3.6): if the top tier lost 60% instead of 20%, it would need 28 points;
  - it looks best for the bottom four fifths on paper and is the least likely to deliver.

### 4.4 Sensitivities on package A (FY2040)

| Case | Household rate | Q1 | Q2 | Q3 | Q4 | Q5 | Top 1% |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **A as recommended** | **10.8%** | **+6,120** | **+9,077** | **+8,612** | **+1,648** | **−20,370** | **−130,963** |
| Seam not fixed (as booked: the cautious reading) | 12.4% | +6,079 | +8,645 | +7,286 | −1,098 | −25,738 | −151,206 |
| Savings booked (administration 3%, drugs 23% lower) | 9.4% | +6,155 | +9,435 | +9,713 | +3,927 | −15,915 | −114,167 |
| States at 80% / 50% / 0% | 11.5% / 12.7% / 14.6% | +6,101 / +6,073 / +6,025 | +8,878 / +8,581 / +8,086 | +8,003 / +7,089 / +5,565 | +386 / −1,506 / −4,660 | | |
| Employers at 65% (the first draft's share) | 13.7% | +6,412 | +9,719 | +9,085 | +1,591 | −21,720 | −156,594 |
| Employer contribution on HI's uncapped base (11.9%) | 10.8% | +6,267 | +9,629 | +9,717 | +3,485 | −24,011 | −222,097 |
| Same, after the stacking check (elasticity 0.25) | 12.7% | +6,219 | +9,127 | +8,172 | +287 | −30,263 | −245,672 |
| A after the stacking check (elasticity 0.25) | 11.2% | +6,111 | +8,973 | +8,294 | +990 | −21,657 | −135,816 |
| Avoidance "elastic" / "even" | 10.8% | +6,144 / +6,174 | +9,321 / +9,635 | +9,363 / +10,328 | +2,598 / +5,201 | | |
| Top 1% at its IRS share of the base (29%, not the CPS's 12%) | 10.8% | +6,172 | +9,617 | +10,274 | +5,090 | −26,066 | −404,488 |
| The first draft's package (65%, 80%, no seam fix), corrected method | 16.1% | +6,447 | +9,449 | +7,868 | −1,223 | −31,922 | −245,372 |
| Same, if employers pass only half their saving into pay [EV-CAR-299] | +0.2 points | +6,038 | +8,333 | +6,160 | −3,180 | | |

What it shows:
- **Pass-through.** At 100% nothing depends on how much of their savings employers pass into pay, because they keep none. That is the strongest practical reason for 100%.
- **The fourth fifth is the thin one.** It is positive under every case except the cautious seam, states at 50% or less, and the first draft's shares.
- **Beside the rest of the plan.** Scenario Q, the rest of the plan without health, gives the fourth fifth +$552 (`models/tools/household/results.md`, section 8), so under A it is about +$2,200 overall.
- **Growth.** The rate drifts from 10.2% (FY2036) to 10.8% (FY2040), about 0.14 point a year, as the plan's cost grows at CBO's health rate and incomes grow more slowly. Holding the plan's growth near income growth is the specification's long-run question (care `6-cost.md`).

### 4.5 The transition years under package A

How each year is paid while the waves move ($B; the household rate is what closes that year):

| FY | To finance | Employers (net) | States (extra over the booked 50%) | Households | Household rate |
| --- | --- | --- | --- | --- | --- |
| 2030 | 50 | 0 | 0 | 50 | 0.4% |
| 2031 | 531 | 77 | 46 | 408 | 3.2% |
| 2032 | 778 | 107 | 63 | 607 | 4.5% |
| 2033 | 1,183 | 346 | 110 | 728 | 5.2% |
| 2034 | 1,679 | 689 | 175 | 815 | 5.6% |
| 2035 | 2,688 | 1,068 | 247 | 1,373 | 9.2% |
| 2036 | 3,075 | 1,213 | 276 | 1,586 | 10.2% |
| 2040 | 3,794 | 1,511 | 344 | 1,939 | 10.8% |
| FY2030-34 | 4,220 | 1,219 | 394 | 2,607 | |
| FY2030-39 | 20,230 | 7,563 | 1,844 | 10,824 | |

- **Employers pay from each group's move:** children's coverage in 2031, then thirds in 2033-35.
- **The early years carry costs no payer moves with:** the restoration in 2030, Medicare's upgrades and Medicare at 60 in 2031-34. That is why the household rate starts near 3%, not zero.
- **Recommended schedule:** set the rate in law as steps that follow this path (about 3% from 2031, 5% from 2033, 9% at the endpoint, then set each year to balance the fund). The FY2030 restoration ($50B) is left to the general fund.
- **The catch.** A household whose own coverage hasn't moved yet (a childless worker with job coverage, 2031-34) pays the contribution and still pays its premium share, for two to four years. The alternatives are a credit for premiums still paid, or starting the contribution in 2035 and borrowing.
  - A credit for premiums still paid is fairer, but it would cut FY2031-34 revenue by roughly $0.9T (rough project arithmetic), so everyone else's early rate would roughly double.
  - Starting the contribution in 2035 and borrowing about $2.6T of the household side over FY2030-34 adds to the debt the guardrail tests.
  - Part 8, question 6.

## Part 5. Households

### 5.1 Package A by fifth, a table to multiply (FY2040, dollars per household a year)

| | Q1 | Q2 | Q3 | Q4 | Q5 | Top 1% |
| --- | --- | --- | --- | --- | --- | --- |
| Expanded income (D3's ranking measure: cash income plus the employer's payroll tax) | 33,634 | 91,643 | 155,789 | 245,592 | 561,562 | 1,875,845 |
| AGI | 15,783 | 63,866 | 131,823 | 221,196 | 525,542 | 1,813,694 |
| AGI above $20,000/$40,000 (the base, as the budget model's yield implies it) | 2,490 | 25,939 | 79,743 | 165,123 | 471,802 | 1,778,855 |
| × the rate | 10.76% | 10.76% | 10.76% | 10.76% | 10.76% | 10.76% |
| **= the contribution charged** | **−268** | **−2,790** | **−8,578** | **−17,763** | **−50,753** | **−191,355** |
| Less what avoidance keeps from being collected (all in the top fifth) | 0 | 0 | 0 | 0 | +16,030 | +60,440 |
| Premiums and out-of-pocket costs they stop paying | +4,629 | +9,493 | +16,161 | +22,280 | +25,889 | +21,967 |
| Employer premiums that become pay | +3,089 | +9,355 | +16,220 | +20,966 | +23,035 | +22,739 |
| Tax on former premiums, both shares (HX) | −287 | −2,971 | −7,155 | −10,158 | −11,371 | −15,971 |
| Employer contribution, borne through pay (wages up to the wage base) | −1,515 | −5,832 | −11,687 | −19,892 | −33,739 | −41,858 |
| Less tax on the pay that no longer rises | +473 | +1,822 | +3,651 | +6,214 | +10,540 | +13,076 |
| **Net** | **+6,120** | **+9,077** | **+8,612** | **+1,648** | **−20,370** | **−130,963** |
| Net as a share of expanded income | +18.2% | +9.9% | +5.5% | +0.7% | −3.6% | −7.0% |
| The contribution as a share of expanded income | 0.8% | 3.0% | 5.5% | 7.2% | 9.0% | 10.2% |

Method:
- Households are ranked by size-adjusted income, equal numbers in each fifth: about 151 million households in FY2040.
- Each row is spread across the fifths on the household model's measured keys (`models/tools/household/keys.csv`): `health_hh`, `employer_cov`, `exclusion_end`, `wages_cap`, and AGI above the line.
- The employer premiums row and the employer contribution row nearly cancel in total, but not within a fifth: premiums follow coverage, and the contribution follows pay.
- It counts cash only, not the value of coverage to people who are uninsured now. It assumes full pass-through (HX's convention), which matters little at 100%.

### 5.2 The packages by fifth

The headline rows are in part 4.1. The full row-by-row tables for B, C and D are in `health_financing.py`'s `detail`; they differ from A in the household rows only. B's VAT falls on consumption (Q1 −$3,760, Q3 −$7,939, Q5 −$14,206), less a rebate of about $2,000-2,200 a household.

### 5.3 Worked examples

In today's dollars at FY2040's rates, with health costs at FY2040's relation to income. Health costs per person grow about 5.4% a year [EV-CAR-056] against incomes on the model's path, so premiums are about 1.34 times today's relative to pay. Sources:
- premiums: KFF's 2026 averages, single $9,804 with the worker paying $1,672, family $28,303 with the worker paying $7,471 [EV-CAR-722, EV-CAR-111];
- out-of-pocket costs, copays and Medicare premiums: the coverage model's averages.

Full pass-through, and tax on pay that changes at the federal bracket plus both halves of payroll tax. Package A unless marked:

| Household | Stops paying (premiums + out of pocket − copays) | Employer saves → pays | Pay change, after tax | Tax on former pre-tax premium | Health contribution (rate × base) | **Net a year** |
| --- | --- | --- | --- | --- | --- | --- |
| Single worker, $45,000, single job coverage | 2,247 + 2,101 − 462 = **3,885** | 10,927 → 6,434 | +4,493 − 1,227 | −613 | 10.76% × 25,000 = −2,689 | **+3,849 (+8.6%)** |
| Single worker, $45,000, employer offers no coverage, uninsured today | 0 + 2,735 − 462 = **2,273** | 0 → 6,434 | −6,434 + 1,757 | 0 | −2,689 | **−5,094 (−11.3%)**, and now covered |
| Family of four, $90,000, family job coverage | 10,039 + 8,403 − 1,849 = **16,593** | 27,992 → 12,868 | +15,124 − 4,129 | −2,741 | 10.76% × 50,000 = −5,379 | **+19,469 (+21.6%)** |
| Family of four, $160,000, family job coverage | **16,593** | 27,992 → 22,877 | +5,115 − 1,908 | −3,745 | 10.76% × 120,000 = −12,909 | **+3,148 (+2.0%)** |
| Retired couple on Medicare, $60,000 (Social Security $36,000, pension $24,000; AGI about $33,000) | 6,861 + 7,185 − 924 = **13,121** | — | — | — | below the line: 0 | **+13,121 (+21.9%)** |
| Retired couple on Medicare, $110,000 (AGI about $102,500) | **13,121** | — | — | — | 10.76% × 62,500 = −6,723 | **+6,398 (+5.8%)** |
| Self-employed single, $70,000 net, buys an individual-market plan | 11,534 + 5,129 − 462 = **16,200** | pays 14.3% × 92.35% × 70,000 = −9,243 | — | — | 10.76% × 45,000 = −4,841 | **+2,116 (+3.0%)** |

The same households under package B (5.5% and a 12% VAT with its rebate):
- single worker with coverage +$574;
- uninsured single worker −$8,369;
- family at $90,000 +$14,581;
- family at $160,000 −$3,721;
- retired couple at $60,000 +$7,375;
- retired couple at $110,000 −$458;
- self-employed −$2,546.

Every household above does worse under B than under A.

### 5.4 Who loses, and how many (package A)

The spread inside each fifth (`micro()`): each row's fifth total is spread over the fifth's households in proportion to the household's own amount of that row's base (its coverage counts on the CPS, its pay, its AGI above the line). The fifths' averages are exactly part 5.1's.

| | Q1 | Q2 | Q3 | Q4 | Q5 | Top 1% |
| --- | --- | --- | --- | --- | --- | --- |
| Households paying more than they save (millions) | 4.5 | 6.5 | 8.5 | 14.9 | 24.0 | 1.5 |
| Share of the fifth | 15% | 22% | 28% | 49% | 80% | 100% |

- **About 34 million households in the bottom four fifths lose cash,** out of about 121 million, with a median loss of about $5,800 a year. Of them:
  - about 54% are working households with no job coverage. Their employers don't offer coverage today, so their pay bears the contribution with no premium savings behind it. They are mostly now uninsured, on Medicaid or in the individual market, and they gain coverage, which the cash count leaves out;
  - about 44% have job coverage, but their premiums are low against their pay or their income is high within the fifth;
  - about 9% are Medicare households with income well above the line.
- **About 58 million households lose in all,** the top fifth's 24 million included.
- **The uncapped employer base** would cut the bottom-four count to about 31 million on the static reading, but it would raise less at the top (part 3.6).
- **These counts are rough.** The CPS's coverage counts under-report Medicaid. The model gives every person in a coverage group the group's average cost. Real premiums vary far more, so the true spread is wider both ways.

## Part 6. Beside the Sanders and Jayapal bills, and Sanders's options paper

Sources:
- Sen. Sanders's S. 1506 (SRC-3260) and his options paper (SRC-3041) [EV-CAR-713];
- Rep. Jayapal's H.R. 3069 (SRC-3261);
- the care dossier's comparison (`dossiers/care/research-s1506-comparison.md`);
- CRFB's and TPC's scores of the options' later version [EV-CAR-714, EV-CAR-715, EV-CAR-716].

| | S. 1506 and the options paper | H.R. 3069 | This plan (package A) |
| --- | --- | --- | --- |
| Taxes in the bill | None. Sec. 701(b)(1) credits the fund with the net revenue "attributable to" secs. 801 and 902 (ending duplicative employer plans and the Exchanges): an indirect stream, no rate [EV-CAR-287] | The same [EV-CAR-292] | The contributions in part 4, set in law, into the plan's fund |
| Existing federal money | One transfer of the prior year's Medicare (less premiums), Medicaid, FEHB and similar appropriations, indexed; Medicare trust fund amounts left after claims are paid (701(d)) | The same, plus TRICARE's purchased care | The same streams pooled (memo 3 B); HI's tax kept and folded in at 2035 |
| The HI payroll tax | Not mentioned: neither repealed nor redirected | Not mentioned | Kept; its revenue goes to the plan's fund from 2035 |
| Medicare premiums | Lapse when Title XVIII benefits end (sec. 901(a)(1)(A)) | The same | End at the 2035 endpoint |
| Employers | Nothing in the bill. The paper: 7.5% of payroll, the first $2 million exempt; in the four-year transition, per enrolling employee, the higher of 75% of current premiums or the 7.5% | Nothing | 100% of former premiums from each move, then 14.3% of pay up to the wage base |
| States | Eligibility standards no stricter than January 2025's, and a floor on institutional long-term care spending at FY2024's level plus growth, with the federal match kept for it (sec. 204; sec. 901(a)(3)(C)) | No maintenance of effort; long-term care moves into the program [EV-CAR-291] | 100% of their former Medicaid spending for the movers; long-term care stays with Medicaid |
| Households | The paper: 4% of income after a deduction of about $29,000 for a family of four | Nothing | 10.8% of income above $20,000/$40,000 |
| Top-end taxes | The paper: about $4.6T over ten years (rates of 40-52% above $250,000, a 1% wealth tax above $21 million, the estate tax, a one-time tax on offshore profits, and others) | None | None for health: the plan books its top-end taxes for its other flagships (part 3.6) |
| The transition | Four years (sec. 106); a Medicare buy-in at 55, 45 and 35 and a transition public plan, paid with premiums and credits | Two years; earlier enrollment for people 55 and over and children | Five years of waves (2031-35), each payer starting when its group moves |
| The gap left open | All new money (the paper prices no program cost) | All of it | None for health |

What this plan takes from them, and what it does differently:
- **Taken:**
  - the paper's transition floor, "the higher of" a share of premiums or the payroll rate, per enrolling worker (at 100% here, which also removes any reason to drop coverage early);
  - its household-premium shape: a flat rate above a deduction, with no cliff;
  - naming the employer-exclusion revenue as a stream (memo 3 B; HX).
- **Considered:** the $2 million payroll exemption. It protects the smallest employers but has no published cost or rationale, and it would raise the rate on everyone else. Part 8, question 5's phase-in for employers that don't offer coverage does the same job more narrowly.
- **Different, and why:**
  - the employer and household rates are larger than the paper's 7.5% and 4% because the paper also had about $4.6T of top-end taxes and $4.2T from ending health tax breaks, and this plan's top end is spent elsewhere;
  - the employer side is capped at the wage base (like the premiums it replaces), where the paper's is uncapped;
  - states keep paying.
- **Grading.** The paper's figures are the sponsor's own, grade C. CRFB and TPC scored a February 2020 version and qualify the figures rather than confirm them. All of it predates the 2025 law.
- **Corrections to the checkpoint memo's part E** (found in this check):
  - S. 1506's state obligation is broader than "a floor for nursing-home spending": it also covers eligibility standards and other state-plan services, and keeps the federal match for them;
  - the 75% transition floor applies per enrolling employee;
  - only Medicare trust fund amounts left after claims are paid transfer to the fund.
- **Jayapal:** still no separate financing plan found [SRC-3079].

## Part 7. Risks, and what would change the recommendation

- **The payment rate drives the cost.** Each 0.1 of the decided 1.15 target moves FY2040 by about $0.7T (care `6-cost.md`, part 6), about **3.9 points** of the household rate. It is decided (memo 5 B) and not reopened here. It is the largest single lever on affordability, and it is Espen's if they ever want to revisit it.
- **Medicaid's starting rates come next:** at 0.60 or 0.85 times Medicare, FY2040 moves +$455B or −$348B.
- **The household rate is visible.** At 10.8% on most income, plus the booked 2 points, it is the largest tax change in the plan, though it replaces more than it takes from most households. Vermont stopped when its full tax became visible [EV-CAR-245]. The public case has to show premiums and deductibles ending beside it.
- **Top rates.** About 74% federal on top wages under A (part 3.6). This is the whole plan's problem, not health's alone. Stage G should re-weigh the stack (SS-1, H1b, the 4 booked points) together.
- **Workers whose employers don't offer coverage** carry the contribution through pay (part 5.4). A phase-in softens it (question 5).
- **The states' payment may fail in court;** the 0% fallback raises the rate to 14.6%, and the fourth fifth turns negative.
- **Growth:** about +0.14 point a year after full adoption, unless the plan's budget holds its growth to income growth.
- **Model limits.** All of this is the project's exploratory models: the coverage model's cell averages, the CPS's top-coding, and the budget model's per-point yields scored before the 2025 law. The top 1%'s IRS share of the base would make the middle and fourth fifths' results better (part 4.4).

**What would change the recommendation:**
- If Espen holds to a 5-6% statutory household rate, **B** is the least bad way there.
- If the specification books the savings, A's rate falls to about 9.4%.
- If the states' share is set below 80%, the fourth fifth needs another lever, such as the savings, the top-1% re-keying or a small second tier.

## Part 8. Questions for Espen

Each point is decided on its own; none is adopted by silence.

1. **The package:** A (recommended), B, C or D?
2. **"Mid single digits":** did you mean the rate on income above the line, or what a typical household pays of its income? Recommendation: judge it by what households pay. Under A the middle fifth pays about 5.5% of its income, and workers' payroll tax stays at 1.45%. A 5-6% statutory rate needs about $1T a year from a VAT or a larger employer contribution, and costs the bottom three fifths more.
3. **Employers at 100% of their former premiums,** in the transition and after (recommended), or at the first draft's 65%?
4. **The employer contribution's base:** each worker's pay up to the Social Security wage base, about 14.3% (recommended), or all pay, about 11.9%, like HI?
5. **A phase-in for employers that offered no coverage in 2029:** their rate steps up over five years, so the cost comes out of future raises rather than current pay (recommended; to price at booking). Or no phase-in?
6. **The household contribution in the transition:** steps that follow the waves, about 3% from 2031, 5% from 2033, 9% at the endpoint, then balancing the fund each year, with no credit for premiums still paid (recommended). Or a credit for premiums still paid (fairer; early rates about double)? Or a start in 2035 with borrowing?
7. **States at 100%** of their former Medicaid spending for the people who move, indexed to the plan (recommended), or 80%, 50% (booked) or 0%?
8. **The self-employed** pay the employer contribution on 92.35% of net earnings, as SECA does (recommended), or not?
9. **Savings:** book none now (recommended); revisit when the specification sets the administrative budget and drug negotiation.
10. **The Medicare seam:** rebook HLT-7 on CBO's Medicare figure in the booking PR (recommended): about −$0.30T in FY2040 and −$1.28T over FY2030-39.
11. **Counting:** count health's contributions outside D3's revenue-mix test, as replacements for premiums, and judge them by the household net test (recommended; as the checkpoint's B4 point 2).
12. **Where the money goes:** all of health's contributions into the plan's fund (HLT-7.22), with the general fund covering any shortfall; the budget model keeps booking on the general fund (recommended; as B4 point 4).

**For stage G** (no answer needed now): the top-rate stack across flagships; the states' shares across health, long-term care, child care and pre-K together (`DEC-2026-11-11-05`); Medicare "Part E" (board, "Directions for later stages"), which would reopen the 2035 endpoint.

## Part 9. What this replaces, and what a booking would change

- **Replaces:** checkpoint memo part B (B1 to B5), the health items of "In plain terms" (2 to 8), part C's "what remains" arithmetic where it rests on part B's package, and part D's questions 1 to 4 (memos F1 to F3 and B4). Part A (the plan-wide gap), part C's list of items for stage G and part E (the bills) stay. Part E is corrected by part 6 here.
- **The rest of the plan** is unchanged: about $70B short in FY2040 and $1.89T over FY2030-39 (checkpoint part C). With the seam rebooked, health's own FY2040 net is $3,794B, so the plan-wide FY2040 gap would be about $3.86T before health's financing.
- **A booking PR (tier 3), after Espen answers,** would:
  - rebase HLT-7 to CBO's Medicare figure;
  - book the employer contribution's row and lower HX by the tax on premiums that no longer become pay;
  - book the states' share (HLT-7.17), the household contribution's rows and path, and the rows in `scenarios.json` for the household model;
  - price the phase-in and transition choices.

## Method and sources

- **Code:** `models/tools/health_financing.py`: `coverage()`, `seam()`, `need_path()`, `payers()`, `payer_path()`, `flow_path()`, `package()`, `package_path()`, `micro()`, `stacking_check()`, `examples()`. Tests: `models/tools/test_health_financing.py`. It reads, without changing, the coverage model, the care dossier's path (`dossiers/care/tools/health_path.py`), the booking (`health_booking.py`), the budget model's audit and paths, and the household model's 2029 CPS households.
- **Evidence:**
  - CBO's Medicare baseline [EV-CAR-718];
  - the IRS tax gap [EV-CAR-719];
  - Gruber and Saez [EV-CAR-720];
  - IRS SOI's top-1% AGI share [EV-CAR-721];
  - KFF's 2026 premiums [EV-CAR-111, EV-CAR-722];
  - JCT's exclusion [EV-CAR-052];
  - Medicare's administration [EV-CAR-217];
  - CBO's single-payer drug scenario [EV-CAR-220];
  - Anand on pass-through [EV-CAR-299];
  - Vermont [EV-CAR-244, EV-CAR-245];
  - the bills and the options paper [EV-CAR-272 to EV-CAR-292, EV-CAR-713 to EV-CAR-716].
- **Legacy** (cited as evidence, not as defaults; `DEC-2026-11-13-15`):
  - `legacy/domains/domain-revenue.md` (combined top rates; the menu);
  - `legacy/sources/revenue-channels-and-full-menu.md`;
  - `legacy/sources/revenue-counted-reconciliation.md`;
  - `legacy/domains/domain-health.md` (HI kept whole).
- **Confirmed from the handover notes:** the corrected method, the avoidance evidence, the seam's size, HX's two shares.
- **Corrected:** the top rate on wages (SS-1 left out), HX alignment, federal coverage in the employer money.
- **Not yet in the register:** Saez, Slemrod and Giertz (*Journal of Economic Literature*, 2012).
