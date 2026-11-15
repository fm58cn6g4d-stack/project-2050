# Paying for the single health plan: the whole system's cost, then its financing

Role: the stage E memo on the single health plan (HLT-1 to HLT-8). It prices the plan as a whole system, year by year from FY2030 to FY2040, and then designs its financing from scratch. It replaces these parts of `checkpoint-financing.md`, which are marked superseded there: part B; the health items of its "In plain terms"; part C's arithmetic; and part D's questions (memos F1 to F3 and part B4's points).

Status: **for Espen's decision, November 15, 2026.** It recommends and books nothing. The questions in part 9 are Espen's, and any booking that follows is a separate tier-3 change to adopted inputs.

How it is built, following Espen's three directions of November 15:
1. Cost the planned system in full first, then design its financing.
2. Don't carry today's tax rates into the new system.
3. Reopen parts of the design only by decision memo, where the evidence is strong.

The decided design (care memos 1 to 5: `DEC-2026-11-10-09` to `-13`, `DEC-2026-11-12-19`, `DEC-2026-11-13-02`) is the baseline throughout. Part 6's design memos are compared against it, not adopted.

Units and sources:
- Federal fiscal years, nominal dollars, $B = billions, $T = trillions, case `mixed`.
- **Every figure is project arithmetic on the project's own exploratory models, not an official score.**
- The figures come from one run of `models/tools/health_financing.py` (tests: `models/tools/test_health_financing.py`).
- An independent agent re-derived the key figures; part 8 records what it found and what was corrected.

## In plain terms

1. **What the new system costs.** The single plan pays for nearly everyone's care. Its gross cost is about **$8.4 trillion in FY2040**: what it pays doctors, hospitals and drug makers, plus its administration and the other items the plan adds. It grows from about $1.2 trillion in FY2032 to about $5.7 trillion in FY2035, when everyone is in.
2. **The country still spends less.** All health spending in FY2040 is about **$11.7 trillion under the plan against $12.4 trillion under today's law: about $0.8 trillion (6%) less**, while about 34 million more people are covered.
3. **Your question, answered: yes.** In FY2040 households, employers, states and the other payers stop paying about $5.7 trillion for health care. The new public money the plan needs is about $4.9 trillion. The difference, about $0.8 trillion, is what single payer saves on prices and administration.
4. **How package A pays the $8.4 trillion** (FY2040):
   - **Federal money already spent on health: $2.7 trillion (32%).** This is the general revenue the government already spends on Medicare, Medicaid and marketplace subsidies for these people, kept for the plan.
   - **An employer health contribution: $2.2 trillion (26%).** It is set so employers as a whole pay what they would otherwise have spent on premiums: about **19.5% of each worker's pay between $20,000 and the Social Security wage base** (about $185,000 today). That is about 12% of all pay. Nothing is due on the first $20,000 of anyone's pay.
   - **A household health contribution: $1.9 trillion (23%).** It is about **10.35% of income above $20,000 (single) or $40,000 (couple)**, collected with the income tax.
   - **A health payroll contribution of 2.9% on all pay: $0.6 trillion (7%).** That is 1.45% each from workers and employers. It is today's Medicare payroll tax, kept as one of the plan's own contributions because it is the plan's only charge on top earners' pay.
   - **The states: $0.7 trillion (8%).** They keep paying what they pay now for the Medicaid patients who move into the plan.
   - **Tax on the pay workers used to put into premiums before tax: $0.3 trillion (3%).**
   - **What ends:** premiums, deductibles, coinsurance, and Medicare's Part B and D premiums.
5. **What it means for households** (FY2040, average per household a year):

   | Fifth of households | Poorest | Second | Middle | Fourth | Top | Top 1% |
   | --- | --- | --- | --- | --- | --- | --- |
   | Net effect | **+$6,800** | **+$10,300** | **+$9,500** | **+$1,500** | −$23,000 | −$132,000 |

   The middle fifth pays about 5.6% of its income in the household contribution, and stops paying about 10% of its income in premiums and medical bills.
6. **Affordable at every income? Not yet for everyone.**
   - About **30 million households in the bottom four fifths** (of about 121 million) pay more in cash than they save, and 16 million of them by more than 5% of their income.
   - Half the fourth fifth is among them. Two groups dominate: workers whose job coverage cost little relative to their pay, and workers whose employers offered no coverage. Most in the second group gain coverage they don't have now, which the cash count leaves out.
   - Two of the design changes in part 6 bring this down to about **25 million** and the household rate to about **8.4%**.
7. **Your 5-6% household rate: what it costs.** It needs about $1 trillion a year from somewhere else.
   - **The top end is already used.** With the plan's other taxes, the top federal rate on wages is about 63% before health. A top tier big enough would push it past 80%, where on the evidence it would raise little.
   - **The other routes:** a value-added tax of about 11.5% with a rebate (package B), or employers paying about 31% of pay in the band (package C).
   - **Both leave the bottom three fifths worse off than package A.**
8. **Design changes worth considering (part 6):**
   - book administration at 4% instead of 5%, with 3% as the target: about −$0.09 trillion;
   - a national health budget that holds growth to the economy's growth plus 1 point from 2037: about −$0.27 trillion in FY2040, more each year after.
   - Recommended unchanged, with their price: the payment rate (1.15 times Medicare; each 0.05 is about $0.34 trillion) and the small copays (removing them costs about $0.25 trillion).
9. **The transition years.** Each payer starts paying when its group moves into the plan. The household contribution starts at about **3% in 2031**, when children and the uninsured move, reaches about **5.4% in 2034** and about **10% from 2036**.

## Part 1. What the new system costs

### 1.1 The gross cost, year by year

The plan's gross cost each year is everything it pays out:
- doctors', hospitals' and drug claims for everyone enrolled, at the decided rates (about 1.15 times Medicare after the hospital glide to 2036), less the small copays;
- its administration (5%, the working figure);
- the items the plan adds: the 2030 restoration, Medicare's upgrades and Medicare at 60 before the endpoint, the hospital transition fund, worker help, the territories, and health's safety-net items;
- less two corrections already booked: the status rule (`DEC-2026-11-12-19`), and federal coverage priced twice (FEHB, TRICARE and the VA, about $150B in FY2040).

It does not include Medicaid's long-term care, which stays in Medicaid (HLT-7.07), or the care flagship's long-term care, care wage floor and staffing rows (HLT-9 to HLT-11).

| FY | 2030 | 2031 | 2032 | 2033 | 2034 | 2035 | 2036 | 2037 | 2038 | 2039 | **2040** | FY2030-39 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Gross cost of the single system ($B)** | 50 | 813 | 1,169 | 1,885 | 2,823 | 5,670 | 6,778 | 7,147 | 7,549 | 7,959 | **8,407** | 41,842 |

What moves in when:
- **2030:** the restoration.
- **2031, wave 1:** the uninsured, the individual market, every child, and Medicare at 60.
- **2033 to 2035, wave 2:** Medicaid and employer groups, a third each year.
- **2035, the endpoint:** everyone else, including today's Medicare enrollees.
- **2036:** the hospital glide ends.

How it is built: the booked health spending (corrected for the Medicare seam, 1.2) plus the money it nets out, namely the federal money it replaces and the states' booked payment (`system_view()`, `replaced_path()`). The independent check reached the same $8,407B by a second route: the rebased plan outlays of $5,575B (2032) × 1.533, plus the other booked items, −$140B.

### 1.2 One correction first: the Medicare seam

- **What was wrong.** The coverage model started Medicare from CMS's projection, made before the 2025 law: $2,024B in 2032. CBO's February 2026 baseline, which the project uses (`DEC-2026-11-08-03`), puts Medicare's 2032 outlays at **$1,867B**, with $340B of premiums and other receipts [EV-CAR-718].
- **Why CBO's figure is the right one.** The two measures agree for 2025: CBO's gross is about $1,197B on a calendar basis, against CMS's $1,204B. So the 2032 gap is in their growth projections (about 6.8% against 7.7% a year), not in how they define Medicare.
- **The effect of the fix.** Re-running on CBO's figure lowers the plan's cost by:
  - **$196B in 2032**: $181B for today's Medicare enrollees and $14B for the newly covered, whose average claims fall with it;
  - **$300B in FY2040**;
  - **$1,281B over FY2030-39**.
- **Timing.** Before 2035 the effect is small, because today's Medicare enrollees move only at the endpoint.
- **Booking.** Every figure here uses the corrected cost. The booked rows change only in a later tier-3 booking PR (part 10). The uncorrected reading appears in part 5 as the cautious case.

### 1.3 National health spending: today against the plan, every payer named

At the full-scale year (2032, the coverage model, decided design, corrected; $B):

| Who pays | Today | Under the plan, before its new financing | Change |
| --- | --- | --- | --- |
| Federal: today, Medicare net of premiums, Medicaid's federal share and premium credits; under the plan, its outlays net of the states' payment | 2,405 | 5,601 | +3,196 |
| States: today, Medicaid's state share; under the plan, the booked 50% payment plus long-term care | 614 | 389 | −225 |
| Employers: premiums | 1,611 | 0 | −1,611 |
| Households: today, premiums, Medicare's premiums, Medigap and out-of-pocket costs; under the plan, copays and costs outside it | 1,891 | 186 | −1,705 |
| Hospitals, states and localities, and charities: care for the uninsured | 174 | 0 | −174 |
| Health spending the plan doesn't take over (the VA, defense health, public health, research and so on) | 1,423 | 1,423 | 0 |
| **National health spending** | **8,119** | **7,600** | **−519 (−6.4%)** |

On FY2040's scale (×1.533) that is **$12,447B today and $11,651B under the plan, a fall of $796B**.

Where the change comes from (2032):
- Lower prices and lower administration for people with employer and individual coverage save about $1.3T.
- Covering the uninsured and paying Medicaid's doctors and hospitals the plan's rates add about $0.8T.

CBO's five illustrative single-payer options changed national spending in 2030 by between −$0.7T and +$0.3T [EV-CAR-218]; the plan's −$0.52T in 2032 sits inside that range.

**The checkpoint's "no named payer" term, resolved** (2032, $B; FY2040 is ×1.533):

| Part | Size | Who pays it | Treatment |
| --- | --- | --- | --- |
| CMS's Medicare figure above CBO's, and CBO's net above its subsidy table | 157 + 15 | Nobody: a seam in the model | Removed by the rebase (1.2) |
| Medicare's premiums and other receipts the model leaves out | 93 | Enrollees, and states through their Part D payments | Named: households (a working split) |
| Private premiums for about 7 million people the model counts twice | 88 | Employers 65, workers 23 | Named |
| Other private premiums and out-of-pocket costs | 36 | Households | Named |
| Care for the uninsured that others pay for | 174 | Hospitals, states and localities, charity | Named; it ends when nearly everyone is covered |

**The identity, every term named** (2032): new federal spending, $3,196B, equals what everyone else stops paying, $3,715B, less the national saving, $519B.

**The direct answer, FY2040:**
- Everyone else stops paying about **$5.70T**: households $2.61T, employers $2.47T, states $0.34T and others $0.27T.
- The plan's new federal spending is about **$4.90T** on the model, or $4.76T as booked and corrected.
- So the new public money is about **$0.8T less** than what everyone else stops paying.
- The first draft found the two "about equal" because it left out $0.6T that other payers stop paying and kept the $0.26T seam.

## Part 2. The financing, designed for the new system

### 2.1 The sources, and the choice behind each

1. **Federal general revenue already spent on health, committed to the plan.**
   - What it is: the general revenue the federal government already spends on these people, for Medicare (net of premiums and of the payroll contribution in item 4), Medicaid's federal share outside long-term care, and marketplace subsidies.
   - The plan's law commits it to the plan's fund, growing with the plan's costs: **$2,724B in FY2040**.
   - This is the only general revenue package A uses. It is money the budget already spends, so it is not new.
2. **An employer health contribution.**
   - **Base:** each worker's pay between a low-pay line of $20,000 (price-indexed) and the Social Security wage base, about 61% of all pay. This share comes from the household model's CPS data, with a top-coding allowance; the independent check found 0.608 against the code's 0.609. The contribution is collected with the payroll tax.
   - **Size:** employers as a whole contribute what they would otherwise have spent on premiums for their workers, $2,197B in FY2040. That covers private, state and local employers; the federal government's own share is federal money already. This follows the structure of Warren's 2019 plan, which set the employer contribution against what employers would otherwise pay [EV-CAR-725]. It makes the move neutral for employers as a group, so nothing depends on whether they pass premium savings into pay.
   - **Rate: about 19.5%** of pay in the band, or about 11.9% of all pay.
   - **Why the low-pay line:** without it, low-paid workers whose employers offer no coverage today carry the contribution through their pay with nothing to offset it. With it, the poorest fifth's households that lose fall from 4.5 million to 2.0 million (part 4.3).
   - **Why the cap at the wage base:** like a premium, the contribution doesn't rise with a top earner's pay. It therefore adds nothing to the top tax rate (part 2.4).
   - **The self-employed** pay it on 92.35% of net earnings, in the same band, as SECA does today.
3. **A household health contribution.**
   - **Base:** adjusted gross income above $20,000 single or $40,000 joint (price-indexed), collected with the income tax and by withholding. It is not a payroll tax: it falls on wages, pensions and investment income alike.
   - **Rate:** whatever closes the rest. In package A that is **10.35%** in FY2040 ($1,939B).
   - **Yield:** a point raises about $187B collected. That includes the pay workers used to put into premiums before tax, which is now income, and it is net of the budget model's 20% allowance for avoidance (part 2.5).
4. **A health payroll contribution of 2.9% on all pay.**
   - Workers and employers pay 1.45% each, and the self-employed 2.9%, on the same base and with the same collection as today's Medicare hospital insurance (HI) tax. It raises about **$580B** in FY2040.
   - **It is kept as one of the plan's own contributions, a design choice.** It is the plan's only charge on top earners' pay, where the capped employer contribution stops.
   - **Folding it into the employer contribution** (24.3% in the band, so that workers pay no payroll tax for health) is cleaner. It moves the charge on top pay onto the fourth fifth, which falls to about −$170 a household (part 5). It also costs about $108B of other tax: the worker's half leaves taxable cash pay, and the tax on former premiums loses its HI part.
   - **Until 2035** this money keeps paying Medicare's hospital claims for the people still in Medicare. HI's trust fund lasts to the endpoint (care `6-cost.md`, part 5) and then folds into the plan's fund (memo 3 B).
5. **The states' payment.**
   - States pay **100%** of what they would have spent on Medicaid outside long-term care for the people who move, indexed to the plan's growth: $689B in FY2040, which is $344B more than the booked 50%.
   - They still come out ahead: hospitals' uncompensated care ends, their share of Medicare's Part D payments ends, and their employees' premiums become the employer contribution at the same total cost.
6. **The tax on pay workers used to put into premiums before tax.**
   - The end of the employer exclusion is decided (memo 3 B). Once premiums end, the pay workers used to put into them before tax is taxed like other pay: **$279B** in FY2040.
   - Employers' own premium money never becomes pay in package A, because it goes into the employer contribution.

**What ends, explicitly:**
- **Premiums, deductibles and coinsurance** end as each group moves. Only the plan's small copays above 200% of poverty remain (memo 4 C).
- **Medicare's premiums** (Parts B and D, and in practice Medigap) end at the endpoint. They are in what households stop paying, and the plan's cost covers them.
- **The exclusion for job-based coverage** ends with the premiums it excluded.
- **The 0.9% Additional Medicare Tax and H1b** stay as they are, as general revenue.

**Where each piece goes by law:**

| Piece | Goes to |
| --- | --- |
| Employer health contribution; household health contribution | **The plan's fund** (HLT-7.22), by the plan's law. The budget model books them on the general fund |
| Health payroll contribution (2.9%) | The HI trust fund until 2034; **the plan's fund from the 2035 endpoint** (memo 3 B) |
| Federal general revenue committed to the plan | The plan's fund, by appropriation in the plan's law |
| The states' payment | The plan's fund, as a clawback-style obligation (HLT-7.17) |
| Tax on pay formerly put into premiums | Its income-tax part to the general fund. By law its payroll-tax part goes to the Social Security and HI trust funds. It is booked on the general fund (care `6-cost.md`, part 5, item 4) |
| Social Security's 12.4%, with SS-1 above $250,000 | Unchanged: the Social Security trust funds |

### 2.2 Package A, FY2040: sources and rates

| Source | FY2040 ($B) | Share | Rate and base |
| --- | --- | --- | --- |
| Federal general revenue already spent on these programs | 2,724 | 32% | An appropriation, indexed to the plan's growth |
| Employer health contribution | 2,197 | 26% | 19.5% of each worker's pay between $20,000 and the wage base (11.9% of all pay) |
| Household health contribution | 1,939 | 23% | 10.35% of income above $20,000/$40,000 |
| Health payroll contribution | 580 | 7% | 2.9% of all pay (1.45% from workers, 1.45% from employers) |
| States' payment | 689 | 8% | 100% of former Medicaid spending for the people who move, indexed |
| Tax on pay formerly put into premiums | 279 | 3% | Ordinary income and payroll tax on it |
| **The system's gross cost** | **8,407** | 100% | |

**The federal budget's view.** The new money these sources raise is **$3,794B**: the booked net cost ($4,094B) less the seam ($300B). It is made up of:
- the employer contribution's net yield, $1,511B. It lowers other tax by $686B, because those premiums never become taxable pay;
- households, $1,939B;
- the states' extra, $344B.

### 2.3 Year by year: how each year is paid (package A, $B)

| FY | Gross cost | Federal general revenue committed | Health payroll contribution | States | Employers | Households | Tax on former pre-tax premiums | Household rate |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2030 | 50 | 0 | 0 | 0 | 0 | 50 | 0 | 0.4% |
| 2031 | 813 | 187 | 0 | 92 | 112 | 408 | 14 | 3.0% |
| 2032 | 1,169 | 259 | 0 | 127 | 156 | 607 | 20 | 4.4% |
| 2033 | 1,885 | 371 | 0 | 219 | 503 | 728 | 64 | 5.0% |
| 2034 | 2,823 | 528 | 0 | 350 | 1,002 | 815 | 127 | 5.4% |
| 2035 | 5,670 | 1,695 | 357 | 494 | 1,553 | 1,373 | 198 | 8.8% |
| 2036 | 6,778 | 2,156 | 495 | 553 | 1,763 | 1,586 | 224 | 9.8% |
| 2037 | 7,147 | 2,285 | 515 | 584 | 1,862 | 1,665 | 237 | 9.9% |
| 2038 | 7,549 | 2,423 | 536 | 617 | 1,968 | 1,756 | 250 | 10.1% |
| 2039 | 7,959 | 2,569 | 557 | 652 | 2,079 | 1,837 | 264 | 10.2% |
| **2040** | **8,407** | **2,724** | **580** | **689** | **2,197** | **1,939** | **279** | **10.35%** |
| FY2030-39 | 41,842 | 12,472 | 2,461 | 3,687 | 10,999 | 10,824 | 1,399 | |

How the transition years are paid:
- **Employers start paying as each group moves:** for children's coverage from 2031, then for each third of employer groups in 2033-35. They pay on the premiums they paid for the workers who have moved. From the endpoint they pay the payroll-based contribution.
- **States pay with each Medicaid third.**
- **The 2.9% payroll contribution** goes to the plan from the endpoint. Before then it pays Medicare's hospital claims.
- **The household rate rises with the waves.** It starts near 3% because the early years carry costs that no payer moves with: the restoration, Medicare's upgrades and Medicare at 60.
- **Recommended:** set the rate in law as steps that follow this path (about 3% from 2031, 5% from 2033, 9% at the endpoint, then set each year to balance the fund), with the FY2030 restoration ($50B) on the general fund.
- **The catch:** a household whose own coverage hasn't moved yet (for example, a childless worker with job coverage in 2031-34) pays the contribution and its own premium share for two to four years. Part 9, question 7.
- **Growth.** After full adoption the household rate drifts up about 0.14 point a year, because the plan's cost grows at CBO's health rate (about 5.7% a year), faster than incomes. Design memo D2 addresses this.

### 2.4 The top end, and why it can't carry much more

- **The stack before health.** With the plan's decided and booked measures, the combined top federal rate on wages is about **63% before health**:
  - 39.6% income tax (G9);
  - 12.4% Social Security above $250,000 (SS-1);
  - 5% Medicare (H1b), which includes today's 2.9%;
  - the booked 4 + 2 income points.

  The handover notes' 50.6% left out SS-1. Package A adds the 10.35% household contribution, for **73.3%**. The capped employer contribution adds nothing at the top.
- **The evidence.**
  - Diamond and Saez's revenue-maximizing top rate is about 73%, counting federal, state, payroll and sales taxes (`legacy/domains/domain-revenue.md`, "Combined top rates").
  - Reported income at the top responds with an elasticity of about 0.12-0.4 (Saez, Slemrod and Giertz, 2012, not yet in the register; Gruber and Saez [EV-CAR-720]).
- **The stacking check** (`stacking_check()`). Suppose the elasticity is 0.25. Then the top 1%'s income shrinks as the rate rises, and the taxes already on it shrink with it. Counting both, the top 1% yields about **44%** of its new charge under package A.
  - That costs about $67B, or 0.36 point on the household rate. The fourth fifth falls to about +$900.
  - An uncapped employer contribution, on HI's base, would add 11.9 points at the top. The top 1% would then yield only about 21%, and the household rate would need about 12.2%.
  - **The stack is a plan-wide question for stage G.**

### 2.5 Avoidance, placed where it happens

The budget model's income-contribution yields carry a 20% allowance for avoidance, on top of JCT's own behavioral response. The household tables put all of it on the top fifth, shared in proportion to the charge, for three reasons:
- the base is AGI, so itemized deductions can't shrink it;
- withheld wages are misreported at about 1%, against 55% for income nobody reports [EV-CAR-719];
- measured responses below the top are small [EV-CAR-720].

So every household below the top fifth is charged its full statutory amount: the rate times its base. Part 5 shows the range: Gruber and Saez's elasticities applied to every fifth, and the first draft's even spread.

## Part 3. The packages

All four packages cover the FY2040 gross cost of $8,407B exactly. They share:
- the federal general revenue committed ($2,724B);
- the 2.9% payroll contribution;
- the states' payment (100%, $689B);
- the employer base.

They differ in how households and employers make up the rest.

| | **A. Contributions sized to the system (recommended)** | B. Household 5.5%, with a rebated VAT | C. Household 5.5%, larger employer contribution | D. Household 5.5%, with a top tier |
| --- | --- | --- | --- | --- |
| Household contribution above $20K/$40K | **10.35%** | 5.5% | 5.5% | 5.5% |
| Second tier above $100K/$200K | — | — | — | 13.6 points |
| Value-added tax (a quarter rebated per person) | — | 11.5% | — | — |
| Employer contribution in the band (share of all pay) | 19.5% (11.9%) | 19.5% (11.9%) | 31.2% (19.0%) | 19.5% (11.9%) |
| Health payroll contribution | 2.9% of all pay | 2.9% | 2.9% | 2.9% |
| Top federal rate on wages | 73.3% | 68.5% | 68.5% | 82.1% |
| **Net per household, FY2040: Q1 / Q2 / Q3 / Q4** | **+6,765 / +10,259 / +9,513 / +1,536** | +5,024 / +8,005 / +8,117 / +2,391 | +6,665 / +9,996 / +9,479 / +1,674 | +6,896 / +11,622 / +13,583 / +8,786 |
| Q5 / top 1% | −22,986 / −132,216 | −18,449 / −102,559 | −22,726 / −92,986 | −35,800 / −400,393 |
| Bottom-four households that lose (millions, of about 121) | 29.6 | 35.3 | 30.2 | 19.3 (on paper) |
| … losing more than 5% of their income | 16.1 | 20.6 | 17.9 | 9.4 (on paper) |
| New collection machinery | none | a federal VAT | none | none |
| On the evidence | holds; the top 1% yields about 44% of its new charge | holds; heaviest on the middle | holds; workers bear it through pay | **doesn't hold**: the top 1% yields about 29% of its new charge (part 2.4) |

**Why A:**
- **Health care as a right:** no premiums, no deductibles, care free at the point of use except small capped copays above 200% of poverty.
- **The single payer's savings are in the cost** (part 1).
- **The most affordable for the bottom three fifths** of the three credible packages (A, B, C).
- **Existing machinery only:** income tax withholding and the payroll tax system (`DEC-2026-11-13-08`).
- **It doesn't meet a 5-6% statutory household rate.** In effective terms it does: the middle fifth pays about 5.6% of its income and the second fifth about 3.2%.

**What 5-6% costs:**
- **B:**
  - a federal VAT of about 11.5% on top of state sales taxes;
  - the bottom three fifths lose $1,400-2,300 a year against A, and about 6 million more bottom-four households lose;
  - it needs a new federal collection system;
  - at a 6% household rate the VAT is 10.4%; at 5%, 12.7%.
- **C:**
  - employers pay about 1.6 times what they would otherwise have spent;
  - in the long run workers bear it through pay, so it is a worker payroll tax in all but name;
  - it is a big jump in labor cost for employers that offered no coverage.
- **D:**
  - it looks best on paper and is the least likely to deliver;
  - at about 82% on top wages, and near 96% if the top tier lost 60% to avoidance, most of it wouldn't be collected.

## Part 4. Households

### 4.1 Package A by fifth, a table to multiply (FY2040, dollars per household a year)

| | Q1 | Q2 | Q3 | Q4 | Q5 | Top 1% |
| --- | --- | --- | --- | --- | --- | --- |
| Expanded income (D3's ranking measure) | 33,634 | 91,643 | 155,789 | 245,592 | 561,562 | 1,875,845 |
| AGI | 15,783 | 63,866 | 131,823 | 221,196 | 525,542 | 1,813,694 |
| AGI above $20,000/$40,000 (the base, as the budget model's yield implies it) | 2,490 | 25,939 | 79,743 | 165,123 | 471,802 | 1,778,855 |
| × the household rate | 10.35% | 10.35% | 10.35% | 10.35% | 10.35% | 10.35% |
| **= household contribution charged** | **−258** | **−2,684** | **−8,250** | **−17,084** | **−48,814** | **−184,047** |
| … and on the pay formerly put into premiums before tax, now in income | −22 | −228 | −549 | −779 | −872 | −1,225 |
| Less what avoidance keeps from being collected (top fifth only) | 0 | 0 | 0 | 0 | +15,418 | +58,131 |
| Premiums and out-of-pocket costs they stop paying | +4,629 | +9,493 | +16,161 | +22,280 | +25,889 | +21,967 |
| Employer premiums that would have gone to coverage | +3,089 | +9,355 | +16,220 | +20,966 | +23,035 | +22,739 |
| Tax on former premiums, both shares, if paid as pay | −287 | −2,971 | −7,155 | −10,158 | −11,371 | −15,971 |
| Employer health contribution, borne through pay | −560 | −3,936 | −10,055 | −19,909 | −38,205 | −49,170 |
| Less the tax on the pay the contribution takes instead | +175 | +1,229 | +3,141 | +6,219 | +11,934 | +15,360 |
| **Net** | **+6,765** | **+10,259** | **+9,513** | **+1,536** | **−22,986** | **−132,216** |
| Net as a share of expanded income | +20.1% | +11.2% | +6.1% | +0.6% | −4.1% | −7.0% |
| Household contribution as a share of expanded income | 0.8% | 3.2% | 5.6% | 7.3% | 8.8% | 9.9% |

The 2.9% payroll contribution is not a row: households pay it today and keep paying it.

How the table is built:
- **Households:** about 151 million in FY2040, ranked by size-adjusted income, with equal numbers in each fifth.
- **Spreading rows across fifths:** each row uses one of the household model's measured keys (`models/tools/household/keys.csv`): `health_hh`, `employer_cov`, `exclusion_end`, the band of pay between $20,000 and the wage base, and AGI above the line.
- **Employer rows:** they follow CBO in assuming total pay is fixed. Premiums an employer no longer pays would become pay, and the contribution comes out of that pay instead. So in total those rows nearly cancel, but not within a fifth: premiums follow coverage, while the contribution follows pay.
- **Cash only:** the table doesn't count the value of coverage to people who are uninsured now.

### 4.2 Worked examples

Each example is in today's dollars, at FY2040's rates, with health costs at FY2040's relation to income.
- **Growth:** health costs per person grow about 5.4% a year [EV-CAR-056] against incomes on the model's path, so premiums are about 1.34 times today's relative to pay.
- **Premiums:** KFF's 2026 averages: single coverage $9,804, with the worker paying $1,672; family coverage $28,303, with the worker paying $7,471 [EV-CAR-722, EV-CAR-111].
- **Out-of-pocket costs, copays and the $3,500 Medicare premium:** the coverage model's averages.
- **Lines:** price-indexed, so in these terms the $20,000 line is about $17,700 and the $40,000 line about $35,400.
- **The contribution's base:** the household's income after the plan, which now includes its pay change and its former pre-tax premium share.
- **Tax on pay that changes:** the federal bracket plus both halves of the remaining payroll taxes.

Package A:

| Household | Stops paying (premiums + out of pocket − copays) | Employer: would have spent → pays | Pay change, then tax on it | Tax on former pre-tax premium | Household contribution (rate × base) | **Net a year** |
| --- | --- | --- | --- | --- | --- | --- |
| Single worker, $45,000, single job coverage | 2,247 + 2,101 − 462 = **3,885** | 10,927 → 5,316 | +5,612, −1,532 | −613 | 10.35% × 35,139 = −3,636 | **+3,716 (+8.3%)** |
| Single worker, $45,000, employer offers no coverage, uninsured today | 0 + 2,735 − 462 = **2,273** | 0 → 5,316 | −5,316, +1,451 | 0 | 10.35% × 21,965 = −2,273 | **−3,864 (−8.6%)**, and now covered |
| Family of four, $90,000, family job coverage | 10,039 + 8,403 − 1,849 = **16,593** | 27,992 → 14,084 | +13,909, −3,797 | −2,741 | 10.35% × 78,510 = −8,123 | **+15,842 (+17.6%)** |
| Family of four, $160,000, family job coverage | **16,593** | 27,992 → 27,723 | +270, −101 | −3,745 | 10.35% × 134,870 = −13,954 | **−936 (−0.6%)** |
| Retired couple on Medicare, $60,000 (Social Security $36,000 and pension $24,000; AGI about $33,000) | 6,861 + 7,185 − 924 = **13,121** | — | — | — | below the line: 0 | **+13,121 (+21.9%)** |
| Retired couple on Medicare, $110,000 (AGI about $102,500) | **13,121** | — | — | — | 10.35% × 67,062 = −6,938 | **+6,183 (+5.6%)** |
| Self-employed single, $70,000 net, buys an individual-market plan | 11,534 + 5,129 − 462 = **16,200** | pays the employer contribution, 19.5% × (92.35% × 70,000 − 17,719) = −9,143 | — | — | 10.35% × 47,281 = −4,892 | **+2,165 (+3.1%)** |

The same households under the other packages:

| Household | B | C | D |
| --- | --- | --- | --- |
| Single worker, job coverage | +1,021 | +3,272 | +5,419 |
| Uninsured worker | −7,198 | −4,947 | −2,800 |
| Family at $90,000 | +12,441 | +13,957 | +19,646 |
| Family at $160,000 | −7,030 | −3,932 | +5,600 |
| Retired couple at $60,000 | +7,614 | +13,121 | +13,121 |
| Retired couple at $110,000 | −287 | +9,433 | +9,433 |
| Self-employed | −2,279 | −1,040 | +4,456 |

D's figures rest on a top tier the evidence says wouldn't be collected.

### 4.3 Affordable at every income? Who loses, and how many (package A)

How this is counted (`micro()`): each fifth's total is spread over its own households in proportion to each one's base (its coverage on the CPS, its pay in the band, its AGI above the line). The fifths' averages are therefore exactly those in 4.1.

| | Q1 | Q2 | Q3 | Q4 | Q5 |
| --- | --- | --- | --- | --- | --- |
| Households paying more than they save (millions) | 2.0 | 5.3 | 7.5 | 14.8 | 24.7 |
| … losing more than 5% of their income | 0.9 | 3.4 | 3.9 | 8.0 | 16.6 |

- **About 29.6 million households in the bottom four fifths lose cash,** 16.1 million of them by more than 5% of their income. The median loss among them is about $6,000 a year.
- **Who they are:**
  - about half have job coverage that cost little relative to their pay, or high income for their fifth;
  - about 48% are working households with no job coverage. Their pay bears the employer contribution with nothing behind it. Most are now uninsured, on Medicaid or in the individual market, and they gain coverage, which the cash count leaves out;
  - about 8% are Medicare households with income well above the line.
- **The low-pay line protects the poorest.** Without it (the contribution at 14.3% on all pay up to the wage base), the poorest fifth's losers rise from 2.0 million to 4.5 million, and the bottom-four count to 34.4 million.
- **The fourth fifth is where affordability is thinnest:** half of it pays more. Design memos D1 and D2 (part 6) cut the bottom-four count to **25.4 million** (12.4 million losing more than 5%) and lift the fourth fifth to about +$4,900.
- **These counts are rough.** The CPS under-reports Medicaid, and the model gives every person in a coverage group that group's average cost. Real premiums and medical bills vary far more, so the true spread is wider in both directions.

## Part 5. What changes the numbers: sensitivities on package A (FY2040)

| Case | Household rate | Q1 | Q2 | Q3 | Q4 | Q5 | Top 1% |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **A as recommended** | **10.35%** | **+6,765** | **+10,259** | **+9,513** | **+1,536** | **−22,986** | **−132,216** |
| With design memos D1 and D2 | 8.4% | +6,817 | +10,803 | +11,157 | +4,872 | −16,586 | −108,473 |
| Savings booked (administration 3%, drugs 23% lower) | 9.0% | +6,801 | +10,633 | +10,642 | +3,828 | −18,589 | −115,904 |
| The seam not fixed (the cautious reading) | 12.0% | +6,722 | +9,809 | +8,153 | −1,226 | −28,284 | −151,874 |
| States at 80% / 50% / 0% | 11.1% / 12.2% / 14.0% | +6,745 / +6,715 / +6,666 | +10,052 / +9,742 / +9,225 | +8,888 / +7,951 / +6,388 | +267 / −1,636 / −4,808 | | |
| The 2.9% folded into the employer contribution (workers pay no health payroll tax; employer 24.3%) | 10.9% | +6,945 | +10,385 | +9,030 | −169 | −24,677 | −106,273 |
| The 2.9% repealed and its money split between the two contributions | 12.0% | +6,989 | +10,592 | +9,413 | +543 | −23,308 | −113,404 |
| Employer contribution with no low-pay line (14.3% up to the wage base) | 10.35% | +6,109 | +8,955 | +8,391 | +1,548 | −19,915 | −127,188 |
| Employer contribution on all pay, HI's base (11.9%) | 10.35% | +6,255 | +9,508 | +9,496 | +3,385 | −23,557 | −218,322 |
| Same, after the stacking check (elasticity 0.25) | 12.2% | +6,206 | +9,000 | +7,962 | +270 | −29,532 | −240,492 |
| A after the stacking check (elasticity 0.25 / 0.4) | 10.7% / 11.2% | +6,755 / +6,743 | +10,158 / +10,027 | +9,207 / +8,812 | +915 / +111 | | |
| Employers at 65% of what they'd otherwise spend (the first draft's share) | 13.2% | +6,824 | +10,412 | +9,533 | +1,455 | −23,137 | −155,057 |
| Avoidance spread "elastic" / "even" | 10.35% | +6,788 / +6,817 | +10,494 / +10,796 | +10,235 / +11,163 | +2,449 / +4,953 | | |
| Top 1% at its IRS share of the base (29%, against the CPS's 12%) | 10.35% | +6,815 | +10,779 | +11,112 | +4,846 | −28,464 | −395,293 |
| The first draft's package on the corrected method (65%, 80%, no seam fix) | 15.5% | +6,429 | +9,267 | +7,537 | −1,373 | −31,241 | −239,715 |

What the table shows:
- **Pass-through.** At 100%, nothing depends on how much of their savings employers pass into pay, because they keep no net saving. In the first draft's package, if employers passed on only half [EV-CAR-299], the fourth fifth would fall to about −$3,200.
- **The fourth fifth** stays positive except in these cases: the cautious seam reading, states at 50% or less, the 2.9% folded into the employer contribution, and the first draft's shares.
- **The rest of the plan.** Scenario Q, the rest of the plan without health, gives the fourth fifth +$552 (`models/tools/household/results.md`, section 8).

## Part 6. Design memos: changes to the decided design, for Espen to weigh

Espen, November 15: "it's ok to reopen parts of the design if compelling evidence suggests we should." Each memo keeps the decided design as the baseline and prices the change on the corrected model in FY2040. A point of the household rate is about $187B.

**D1. Administration.**
- **Options:**
  - A: 5%, the decided working figure;
  - B: book 4%, with 3% as the specification's target;
  - C: book 3%.
- **Effect:** B −$92B (0.5 point); C −$181B (1.0 point).
- **Evidence:**
  - Traditional Medicare's administration was 1.4% of its spending in 2017 [EV-CAR-217].
  - Warren's plan assumed 2.3%. Urban's researchers called that too low and 6% more reasonable [EV-CAR-742].
- **Quality and access:** little risk at 4%. At 3%, the budgets for payment integrity and member services would need protecting.
- **Recommendation: B.**

**D2. A national health budget.**
- **Options:**
  - A: no budget; growth follows CBO's health path, about 5.7% a year;
  - B: from 2037, hold the plan's spending growth to nominal GDP growth plus 1 point, with a review trigger and an automatic report to Congress if it's missed;
  - C: hold growth to GDP growth.
- **Effect in FY2040:** B −$270B (1.4 points); C −$590B (3.2 points). The effect grows every year after.
- **Evidence:**
  - Warren's plan assumed growth held to GDP [EV-CAR-744].
  - Urban's researchers note that this has never been done in the US [EV-CAR-742].
  - B leaves room above GDP for an older population and new treatments.
- **Quality and access:** if growth runs hot, a budget squeezes payment rates or volume. The review trigger is the guard against that.
- **Recommendation: B.** The specification would set the mechanism: global hospital budgets and an update rule for fees. This is the largest affordability lever after the payment rate, and it is the long-run answer to the household rate's drift.

**D3. The payment rate** (decided: about 1.15 times Medicare, with a hospital glide to 2036).
- **Options:** A: 1.15; B: 1.10; C: 1.05.
- **Effect:** B −$341B (1.8 points); C −$681B (3.6 points). The rate is the largest single driver of cost (care `6-cost.md`, part 6).
- **Evidence:**
  - Warren's plan paid hospitals 110% of Medicare; Urban assumed 115% [EV-CAR-732].
  - The decided glide protects hospitals moving down from commercial prices of about 2.1 times Medicare (memo 5 B).
- **Quality and access:** rural and safety-net hospitals are the most exposed.
- **Recommendation: A**, revisited when the glide ends in 2036, with data on hospital margins. The evidence doesn't yet compel a change.

**D4. Copays** (decided: small capped copays above 200% of poverty, memo 4 C).
- **Options:** A: as decided; B: none at all, as S. 1506 has.
- **Effect:** B +$251B (1.3 points).
- **Recommendation: A.** The copays are small, capped and waived below 200% of poverty. Removing them would raise the rate for everyone.

**Package A with D1 B and D2 B:** a household rate of **8.4%**, the fourth fifth at +$4,872, and 25.4 million bottom-four households losing cash.

## Part 7. Beside the Sanders, Jayapal and Warren plans

Sources:
- Sanders: S. 1506 (SRC-3260) and his options paper (SRC-3041) [EV-CAR-713];
- Jayapal: H.R. 3069 (SRC-3261);
- Warren: her 2019 financing plan (SRC-3356) [EV-CAR-723 to EV-CAR-730, EV-CAR-744], with independent reviews by CRFB [EV-CAR-737 to EV-CAR-741, EV-CAR-743], TPC [EV-CAR-735, EV-CAR-736] and Urban [EV-CAR-734, EV-CAR-742];
- the care dossier's comparison (`dossiers/care/research-s1506-comparison.md`).

Warren's figures are the sponsor's own (grade C) and predate the 2025 law. They are used for structure, not for figures.

| | Sanders (S. 1506 and options paper) | Jayapal (H.R. 3069) | Warren (2019) | This plan (package A) |
| --- | --- | --- | --- | --- |
| Cost first? | No program cost stated | No | Yes: about $52T national over ten years, $20.5T new federal [EV-CAR-723]. CRFB puts it at about $27T [EV-CAR-743] | Yes: gross cost by year (part 1) |
| Financing | None in the bill; the paper is a menu | None | A full plan | Part 2's six sources, in law |
| Employers | Paper: 7.5% of payroll, the first $2 million exempt. In the transition, per enrolling worker, the higher of 75% of premiums or the 7.5% | Nothing | 98% of each employer's prior per-worker spending, converging to the national average. Firms under 50 workers that don't offer coverage are exempt [EV-CAR-725, EV-CAR-726] | What employers as a whole would otherwise spend, as a contribution on pay between a $20,000 line and the wage base |
| States | Eligibility no stricter than January 2025's; a floor on institutional long-term care spending (sec. 204) | No maintenance of effort; long-term care moves into the program | A maintenance of effort of about $6T: Medicaid and CHIP, and state employee premiums [EV-CAR-727] | 100% of former Medicaid spending outside long-term care, indexed |
| Households | Paper: 4% above about $29,000 for a family of four | Nothing | "No new middle-class taxes": higher take-home pay is taxed under current law [EV-CAR-728] | 10.35% above $20,000/$40,000 |
| Top-end and other revenue | Paper: about $4.6T (rates to 52%, a 1% wealth tax, the estate tax and more) | None | Financial transactions tax, wealth and capital-gains taxes, corporate changes, the tax gap, immigration reform, ending overseas war funds [EV-CAR-729, EV-CAR-730] | None for health: the plan's top-end taxes fund its other flagships |
| HI payroll tax | Not mentioned | Not mentioned | Kept | Kept at 2.9% as the plan's own contribution; into the plan's fund from 2035 |
| Cost assumptions | — | — | Administration 2.3%, hospitals at 110% of Medicare, growth held to GDP [EV-CAR-744] | Administration 5% (D1: 4%); 1.15 times Medicare; CBO's growth (D2: GDP + 1) |
| What reviewers found | CRFB and TPC qualify the paper's figures [EV-CAR-714 to EV-CAR-716] | — | CRFB: the direct offsets about right, the extra revenue well short; +$6.1T to deficits, range −$1.2T to +$11.2T [EV-CAR-737 to EV-CAR-741]. TPC: the employer charge works like a head tax and penalizes hiring the 50th worker [EV-CAR-735]; the stacked top taxes could pass 100% [EV-CAR-736] | Part 8's cross-check; part 2.4's stack |

What this plan takes, and what it does differently:
- **From Warren:**
  - the order: cost first, then financing;
  - an employer contribution set against what employers would otherwise spend;
  - a maintenance of effort for the states.
- **Unlike Warren:**
  - The employer contribution is on pay, not a charge per worker. TPC found the per-worker charge works like a head tax [EV-CAR-735]. Here the low-pay line, rather than a small-firm exemption, protects low-paid workers.
  - There is a household contribution. This plan's top end is already spent, and the reviewers found Warren's top-end revenue short.
  - The cost assumptions are less aggressive. The design memos price Warren-like ones.
- **From Sanders:**
  - the per-worker "higher of" floor in the transition;
  - a flat household rate above a deduction.
- **Corrections to the checkpoint memo's part E:**
  - S. 1506's state obligations also cover eligibility standards and other state-plan services, and keep the federal match;
  - the transition floor applies per enrolling employee;
  - only Medicare trust fund amounts left after claims are paid transfer.
- **Jayapal:** still no separate financing plan found [SRC-3079].

## Part 8. Accuracy: the independent cross-check

A separate agent (November 15) re-derived the key figures from the underlying models, without using this tool's functions:
- the coverage model and the care path;
- the booking;
- the budget model's audit and paths;
- the household microdata.

**What it confirmed,** each reached independently:
- the seam: −$300B in FY2040, −$1,281B over FY2030-39, and −$181B and −$14B in 2032;
- national spending: $8,119B against $7,600B, and the ×1.533 scale (FY2040: $12,447B against $11,651B);
- the booked need: $4,093.7B, and $3,794B after the seam;
- the gross cost: $8,407B, by two routes;
- the employer pieces: $2,197B, and the $686B of tax they displace;
- the per-point yield: $180.2B;
- the middle fifth's net, within $4;
- the employer base share: 0.608 against 0.609.

**What it found, and what was done:**

| Finding | Size | Done |
| --- | --- | --- |
| Folding the 2.9% into the employer contribution moves the worker's half out of taxable cash pay. Income and Social Security tax on it fall, which the code had not counted, and HX's remainder still carried HI's 2.9 points | About $108B in FY2040 | Counted in the "folded" sensitivity. It is part of why package A keeps the 2.9% as its own contribution |
| The household contribution's base left out the pay workers used to put into premiums before tax, which is now income | About $74B of yield | Added: the rate falls from 10.76% to 10.35% |
| The worked examples charged the contribution on income before the plan, counted HI in the tax on pay changes after its repeal, and used lines at face value though they are price-indexed | The family at $90,000: about $2,600 too high | Fixed: the examples now use post-plan AGI, the remaining payroll taxes and indexed lines |
| The budget model's payroll point ($200B in FY2040) looks like 85-89% of all pay, not all of it | The employer rate in the band could be about 2 points lower; the 2.9%'s yield about $650-680B, not $580B | **Open.** It is the budget model's parameter and is not changed here. It doesn't move the household rate. To settle in the booking PR |
| CBO's fiscal-year 2032 Medicare figure is used as calendar 2032 | The seam would be about −$284B in FY2040, not −$300B | Open; small |
| The HX key (`exclusion_end`) is a typed legacy key, while `employer_cov` is measured | Small | Open; noted |
| Emergency Medicaid, which the status rule keeps, may sit in the states' base | Small | Open; noted |

**The top three remaining risks to accuracy:**
1. the payroll point;
2. the use of CBO's growth in net federal health subsidies, about 5.7% a year after 2036, as the plan's growth path;
3. the household model's coverage averages (part 4.3).

## Part 9. Questions for Espen

Each question is decided on its own; none is adopted by silence.

1. **The package:** A (recommended), B, C or D?
2. **"Mid single digits":** did you mean the household rate on income above the line, or what a typical household pays of its income? **Recommendation: judge it by what households pay.** Under A the middle fifth pays about 5.6% of its income, and workers' health payroll contribution is 1.45%. A 5-6% statutory rate needs about $1T a year from a VAT or a larger employer contribution, and costs the bottom three fifths more.
3. **The employer contribution's size:** what employers as a whole would otherwise have spent on premiums (recommended), or less (65%, as in the first draft)?
4. **Its base:**
   - pay between a $20,000 low-pay line and the wage base, about 19.5% (recommended);
   - pay up to the wage base with no line, about 14.3%;
   - all pay, about 11.9%.
5. **A phase-in for employers that offered no coverage in 2029:** their rate steps up over five years (recommended; to price at booking), or none?
6. **The 2.9% payroll contribution:**
   - keep it as the plan's own contribution on all pay (recommended);
   - fold it into the employer contribution, so workers pay no payroll tax for health. This costs about $108B of other tax, and the fourth fifth turns slightly negative.
7. **The household contribution in the transition:** steps that follow the waves (about 3% from 2031, 5% from 2033, 9% at the endpoint), with no credit for premiums still paid (recommended)? The alternatives:
   - a credit for premiums still paid: fairer, but FY2031-34 revenue falls by roughly $0.9T, and the early rate about doubles for everyone else;
   - a start in 2035, borrowing about $2.6T over FY2030-34.
8. **The states at 100%** of their former Medicaid spending for the people who move, indexed (recommended), or 80%, 50% (booked) or 0%?
9. **The self-employed** pay the employer contribution on net earnings, in the same band, as SECA does (recommended)?
10. **D1, administration:** book 4%, with a 3% target (recommended)?
11. **D2, a national health budget:** hold growth to GDP plus 1 point from 2037 (recommended)?
12. **D3 and D4:** keep the 1.15 payment rate and the small copays (recommended)?
13. **The Medicare seam:** rebook HLT-7 on CBO's Medicare figure in the booking PR: −$0.30T in FY2040, −$1.28T over FY2030-39 (recommended)?
14. **Counting and the fund:** count health's contributions outside D3's revenue-mix test, as replacements for premiums, and pay them into the plan's fund, with the general fund covering any shortfall (recommended)?

**For stage G** (no answer needed now):
- the top-rate stack across flagships (SS-1, H1b, the booked income points);
- the states' shares across health, long-term care, child care and pre-K, together (`DEC-2026-11-11-05`);
- Medicare "Part E" (board, "Directions for later stages").

## Part 10. What this replaces, and what a booking would change

- **What it replaces** in the checkpoint memo:
  - part B;
  - the health items of "In plain terms" (items 2 to 8);
  - part C's "what remains" arithmetic, where it rests on part B;
  - part D's questions 1 to 4 (memos F1 to F3 and B4).
- **What stays:** part A, part C's list for stage G, and part E, which part 7 here corrects and extends.
- **The rest of the plan is unchanged:** about $70B short in FY2040 (checkpoint part C). With the seam rebooked, health's own FY2040 net cost is $3,794B, so the plan-wide FY2040 gap before health's financing would be about $3.86T.
- **A booking PR (tier 3), after Espen answers,** would:
  - rebase HLT-7 on CBO's Medicare figure;
  - book the employer contribution's row, net of the tax it displaces;
  - book the states' share (HLT-7.17);
  - book the household contribution's rows and path, and `scenarios.json`;
  - price the phase-in and the transition choices;
  - settle the payroll point;
  - book any design memo Espen adopts.

## Method and sources

- **Code:** `models/tools/health_financing.py`: `coverage`, `seam`, `need_path`, `replaced_path`, `system_view`, `payers`, `payer_path`, `flow_path`, `package`, `package_path`, `micro`, `stacking_check`, `design_levers`, `growth_hold`, `examples`. Tests: `models/tools/test_health_financing.py`.
- **What the code reads** (it changes none of them): the coverage model; the care path (`dossiers/care/tools/health_path.py`); the booking (`health_booking.py`); the budget model's audit and paths; the household model's 2029 CPS households.
- **Evidence:**
  - CBO's Medicare baseline [EV-CAR-718];
  - the IRS tax gap [EV-CAR-719];
  - Gruber and Saez [EV-CAR-720];
  - IRS SOI's top-1% AGI share [EV-CAR-721];
  - KFF's 2026 premiums [EV-CAR-111, EV-CAR-722];
  - JCT's estimate of the exclusion [EV-CAR-052];
  - Medicare's administration [EV-CAR-217];
  - CBO's single-payer options [EV-CAR-218, EV-CAR-220];
  - Anand on pass-through [EV-CAR-299];
  - Vermont [EV-CAR-244, EV-CAR-245];
  - the bills and the options paper [EV-CAR-272 to EV-CAR-292, EV-CAR-713 to EV-CAR-716];
  - Warren's plan and its reviews [EV-CAR-723 to EV-CAR-744].
- **Legacy work,** weighed as evidence, not as defaults (`DEC-2026-11-13-15`):
  - `legacy/domains/domain-revenue.md`;
  - `legacy/sources/revenue-channels-and-full-menu.md`;
  - `legacy/sources/revenue-counted-reconciliation.md`;
  - `legacy/domains/domain-health.md`.
- **The handover notes** (`notes/health-financing-findings-2026-11-15.md`):
  - confirmed: the corrected method, the avoidance evidence, the seam's size, and HX covering both shares;
  - corrected: the top rate (SS-1 left out), HX's alignment with the booking, and federal coverage in the employer money.
