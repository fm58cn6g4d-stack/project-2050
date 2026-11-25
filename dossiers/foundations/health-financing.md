# Paying for the single health plan: the whole system's cost, then its financing

Role: the stage E memo on the single health plan (HLT-1 to HLT-8). It prices the plan as a whole system, year by year from FY2030 to FY2040, and then designs its financing from scratch. It replaces these parts of `checkpoint-financing.md`, which are marked superseded there: part B; the health items of its "In plain terms"; part C's arithmetic; and part D's questions (memos F1 to F3 and part B4's points).

Status: **decided and booked, November 15, 2026** (written for Espen's decision; revised the same day in #386). Espen decided part 9's questions that `health-cost-review.md` doesn't replace as recommended (`DEC-2026-11-15-07`, `-08`, `-21` to `-29`); question 9, the household contribution's path in the transition, was decided on November 16 as recommended, adapted to the unified contribution (`DEC-2026-11-16-01`), with the streams' start (`-02`) and the allowance before 2035 (`-03`). The booking is the health financing booking PR (`models/bookings/health_booking.py`, `corrected()` and `financing()`; test `models/bookings/test_fiscal_health_financing.py`); its figures are the cost review's and the unified contribution's, read with this memo's payer accounting, protections and credit. The analysis tools measure the package against the budget as booked before that PR (`models/bookings/health_before_booking.json`).

**Superseded in part by `health-cost-review.md` (November 15, 2026).** An independent cost review found errors in the gross cost, in both directions, and redesigned the financing around Espen's take-home test. These parts are replaced there:
- the gross cost (FY2040 $8,407B, now $7,795B with the errors fixed) and part 1.2b's correction, which the review makes;
- the national saving (about 6%, now about 8%);
- the package choice (part 3) and part 9's questions 1, 2, 12 and 17.

The rest of this memo stands, read with the review's figures: the seam, the payer accounting, the employer protections, the worker transition credit and the states' payment.

How it is built, following Espen's three directions of November 15:
1. Cost the planned system in full first, then design its financing.
2. Don't carry today's tax rates into the new system.
3. Reopen parts of the design only by decision memo, where the evidence is strong.

The decided design (care memos 1 to 5: `DEC-2026-11-10-09` to `-13`, `DEC-2026-11-12-19`, `DEC-2026-11-13-02`) is the baseline throughout. Part 6's design memos are compared against it, not adopted.

Units and sources:
- **Households and people: 2026 dollars.** Every household and per-person figure is FY2040's amount with price growth taken out, so it reads as today's money. FY2040's own (nominal) dollars appear in brackets or a second column where the budget needs them. Each table's heading says which it uses.
- **Lines and thresholds are in 2026 dollars** and rise with prices each year, as the income tax's do.
- **Budget totals:** federal fiscal years, nominal dollars, $B = billions, $T = trillions, case `mixed`.
- **One income measure for households: AGI**, the adjusted gross income on the tax return. The one exception is the count of households losing "more than 5% of income", which uses D3's broader measure and says so.
- **Every figure is project arithmetic on the project's own exploratory models, not an official score.**
- The figures come from one run of `models/tools/health_financing.py` (tests: `models/bookings/test_health_financing.py`).
- An independent agent re-derived the key figures; part 8 records what it found and what was corrected.

## The contributions at a glance (package A, FY2040, 2026 dollars)

| Contribution | Rate | Charged on (the base) | Who pays | How it is collected |
| --- | --- | --- | --- | --- |
| **Household health contribution** | **10.6%** | **Taxable income:** AGI less the standard deduction ($16,100 single, $24,150 head of household, $32,200 couple; $2,050 more for a single person 65 or over, $1,650 more for each spouse 65 or over) | Every household with taxable income | With the income tax, by withholding and on the return |
| **Employer health contribution** | **19.3%** | Each worker's pay between **$20,000** and the Social Security wage base ($184,500 in 2026); about 11.9% of all pay | Every employer; the self-employed on 92.35% of net earnings | With payroll taxes on Form 941; SECA on Schedule SE |
| **Health payroll contribution** | **2.9%** | All pay, no cap | 1.45% from the worker, 1.45% from the employer; 2.9% from the self-employed | As today's Medicare tax |
| **Worker transition credit** (paid back) | 100% of the employer contribution on your pay | Your W-2s and Schedule SE | People who had earnings in 2028 and no job coverage, plan of their own or Medicare that year; phased out between AGI of $60,000 and $120,000 ($120,000 and $240,000 for couples) | Refundable on the return, paid through withholding; in full 2035-2044, then a fifth less each year, none from 2049 |
| **Phase-in** (for employers) | A tenth of the employer rate in 2035, rising a tenth a year | As the employer contribution | Employers that reported no health coverage for 2028 | Form 941; full rate from 2044 |

**Three ways to read a rate**, with one example: a single worker with $54,000 of AGI after the plan.
- **The statutory rate** is the rate on its base: 10.6% of taxable income ($54,000 − $16,100 = $37,900).
- **The charge** is the rate times the base: $4,020.
- **The share of income** is the charge over AGI: 7.4%.

This memo gives all three wherever a rate appears.

**Glossary:**
- **AGI (adjusted gross income):** the income on line 11 of Form 1040: pay, business income, investment income, pensions and the taxable part of Social Security.
- **Taxable income:** AGI less the standard deduction. On the tax return, people who itemize subtract their itemized deductions instead, and business owners also subtract the business-income deduction; this memo recommends that the health contribution not count those (part 9, question 5).
- **Base:** what a rate is charged on.
- **Line:** an amount of income below which nothing is due (for example, the employer contribution's $20,000).
- **Statutory rate:** the rate written in law, on its base.
- **Share of income (effective rate):** what is paid as a share of the household's whole income (here, AGI).
- **Nominal and real:** nominal dollars are the dollars of the year itself; real (here, 2026) dollars take out price growth, so years can be compared.
- **The fifths:** all households ranked by income adjusted for household size and split into five equal groups (Q1 poorest to Q5 richest), with the top 1% shown separately. FY2040 has about 151 million households, about 30 million in each fifth; "the bottom four fifths" is about 121 million.

## In plain terms

1. **What the new system costs.** The single plan pays for nearly everyone's care. Its gross cost is about **$8.4 trillion in FY2040**: what it pays doctors, hospitals and drug makers, plus its administration and the other items the plan adds. It grows from about $1.2 trillion in FY2032 to about $5.7 trillion in FY2035, when everyone is in.
2. **The country still spends less.** All health spending in FY2040 is about **$11.7 trillion under the plan against $12.4 trillion under today's law: about $0.8 trillion (6%) less**, while about 34 million more people are covered. Most of the saving comes from paying near-Medicare prices and lower administration. Covering everyone and ending most cost sharing push the other way (part 1.3).
3. **A pricing correction to come (part 1.2b):** the cost model pays doctors at the hospitals' 1.15 times Medicare, but the decided design pays them Medicare's fee schedule plus add-ons. Fixing that at booking lowers the FY2040 cost by about $0.28 trillion (range $0.14-0.41 trillion), about 1.4 points off the household rate (to about 9.2%). The figures below don't include it yet.
4. **Your question, answered: yes.** In FY2040 households, employers, states and the other payers stop paying about $5.7 trillion for health care. The new public money the plan needs is about $4.9 trillion. The difference, about $0.8 trillion, is what single payer saves on prices and administration.
5. **How package A pays the $8.4 trillion** (FY2040):
   - **Federal money already spent on health: $2.7 trillion (32%).** This is the general revenue the government already spends on Medicare, Medicaid and marketplace subsidies for these people, kept for the plan.
   - **An employer health contribution: $2.16 trillion (26%).** It is set so employers as a whole pay what they would otherwise have spent on premiums: **19.3% of each worker's pay between $20,000 and the Social Security wage base**. Nothing is due on the first $20,000 of anyone's pay. Every employer pays it; those that offered no coverage before the law start low and step up over ten years (item 8).
   - **A household health contribution: $2.0 trillion (23%) after the worker credit is paid back.** It is **10.6% of the taxable income on your tax return**, collected with the income tax.
   - **A health payroll contribution of 2.9% on all pay: $0.6 trillion (7%).** That is 1.45% each from workers and employers. It is today's Medicare payroll tax, kept as one of the plan's own contributions because it is the plan's only charge on top earners' pay.
   - **The states: $0.7 trillion (8%).** They keep paying what they pay now for the Medicaid patients who move into the plan.
   - **Tax on the pay workers used to put into premiums before tax: $0.3 trillion (3%).**
   - **What ends:** premiums, deductibles, coinsurance, and Medicare's Part B and D premiums.
6. **What it means for households** (FY2040, average per household a year, **2026 dollars**):

   | Fifth of households | Poorest | Second | Middle | Fourth | Top | Top 1% |
   | --- | --- | --- | --- | --- | --- | --- |
   | Average AGI | $11,500 | $46,400 | $95,700 | $160,700 | $381,700 | $1.32M |
   | Household contribution | $270 | $2,590 | $7,290 | $14,190 | $37,970 | $138,900 |
   | … as a share of AGI | 2.4% | 5.6% | 7.6% | 8.8% | 9.9% | 10.5% |
   | **Net effect of the whole plan** | **+$5,100** | **+$7,800** | **+$7,200** | **+$800** | −$17,200 | −$97,200 |

   The middle fifth pays 10.6% of about $68,700 of taxable income, $7,290, which is 7.6% of its AGI. It stops paying about $11,700 in premiums and medical bills. (The poorest fifth's AGI is small because most of its income, such as Social Security and benefits, isn't taxed.)
7. **Affordable at every income? Much closer, with the fix you asked for.**
   - **Before the fix,** about **30.7 million households in the bottom four fifths** (of about 121 million) paid more in cash than they saved, 12.4 million of them by more than 5% of their income. The hardest case was a $45,000 worker whose employer offered no coverage: **−$3,400 a year (−7.6%)**.
   - **The fix** (part 2.7) has two parts. Employers that offered no coverage start slowly (item 8). And workers who had **no job coverage, no plan of their own and no Medicare in 2028** get back the employer contribution charged on their pay, as a refundable credit on their tax return. It is paid in full up to $60,000 of AGI ($120,000 for a couple) and phases out by $120,000 ($240,000). It is paid in full from 2035 to 2044, then a fifth less each year, with none from 2049.
   - **After the fix:** **26.9 million** bottom-four households lose cash, and only **6.2 million** by more than 5%. In the bottom three fifths, those losing more than 5% fall from 6.9 million to under 0.8 million. The $45,000 worker is now **+$440 a year**, and covered.
   - **Who still loses:** mostly the fourth fifth (15.8 million households, 5.4 million by more than 5%). They are chiefly workers whose job coverage cost little next to their pay. A premium charges everyone the same; the plan charges by pay. A credit for every worker would reach them, but it would cost more than five times as much, and because everyone's rate would rise to pay for it, it would not cut the number losing more than 5% (part 4.3).
   - **What it costs:** about $150 billion in FY2040, **0.8 point on the household rate (9.8% to 10.6%)**.
   - **A correction:** the merged memo's count of 16.1 million losing more than 5% compared 2040 dollars with 2029 incomes. It is fixed here.
8. **The employer contribution: mandatory, and built so it can't cut pay** (part 2.6).
   - **Mandatory.** It is a tax, paid with payroll taxes on Form 941 and by the self-employed through SECA. There is no small-firm exemption and nothing to opt out of.
   - **A slower start for employers that offered no coverage in 2028:** a tenth of the rate in 2035, rising a tenth a year to the full rate in 2044. For a $45,000 worker each step is about $480, or 1.1% of pay. Pay normally grows faster than that, so pay never has to fall.
   - **Pay rates can't be cut.** Workers employed when their employer starts paying can't have their pay rate cut through 2044.
   - **Savings must reach pay.** Employers that pay less than their old premiums must pass the difference into pay for three years. Under a union contract, the members decide how: wages, pensions or other benefits.
   - **What the law can't do:** set future raises. Over time most of a payroll cost lands on pay growth. That is why the credit in item 7 exists, and why yearly published pay counts trigger a review if pay falls behind.
9. **The household base: taxable income.** As you suggested, the contribution is charged on the taxable income on your tax return, with no separate $20,000/$40,000 line. Charging it on AGI above that line instead would need 11.2% rather than 10.6%, and would leave 1.7 million fewer bottom-four households losing cash, because the standard deduction is a little below the line. The recommendation is to count only the standard deduction, not itemized deductions (part 9, question 5).
10. **Your 5-6% household rate: what it costs.** It needs about $1 trillion a year from somewhere else.
   - **The top end is already used.** With the plan's other taxes, the top federal rate on wages is about 63% before health. A top tier big enough would push it to about 84%, where on the evidence it would raise little.
   - **The other routes:** a value-added tax of about 13% with a rebate (package B), or employers paying about 34% of pay in the band (package C).
   - **Both leave the bottom three fifths worse off than package A.**
11. **Design changes worth considering (part 6):**
    - book administration at 4% instead of 5%, with 3% as the target: about −$0.09 trillion;
    - a national health budget that holds growth to the economy's growth plus 1 point from 2037: about −$0.27 trillion in FY2040, more each year after.
    - With both, the household rate is about **8.8%**, and 20.8 million bottom-four households lose cash (3.5 million by more than 5%).
    - Recommended unchanged, with their price: the payment rate (1.15 times Medicare; each 0.05 is about $0.34 trillion) and the small copays (removing them costs about $0.25 trillion).
12. **The transition years.** Each payer starts paying when its group moves into the plan. The household contribution starts at about **3% in 2031**, when children and the uninsured move. It reaches about **5% in 2034**, about **9% in 2035**, about **10% in 2036** and **10.6% by 2040**.
13. **The rest of the plan.** With health paid for this way, the rest of the plan is about $70 billion short in FY2040 and about $1.9 trillion over FY2030-39 (part 10).

## Part 1. What the new system costs

### 1.1 The gross cost, year by year

*Superseded: the FY2040 gross is $7,795B with the errors fixed (`health-cost-review.md`, part 1.2). The year path below is the uncorrected one.*

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

### 1.2b A second correction to make at booking: doctors are priced at the hospital rate

*Superseded: made in `health-cost-review.md`, part 1.2, step 1, with the households and loser counts re-run (its part 1.6).*

- **What is wrong.** The decided design pays hospitals about 1.15 times Medicare after a glide (HLT-7.10). It pays physicians and other clinicians at Medicare's fee schedule, with primary-care and rural add-ons and no glide (HLT-7.12, memo 5 B). But the booking path (`dossiers/care/tools/health_path.py`, `groups()`) prices all non-hospital, non-drug claims at the hospital target of 1.15. That covers physicians and clinical services ($1,110B of national spending in 2024), and with them the other professional and home health services, which the model doesn't split out.
- **The size,** on the same route as part 6's levers (the 2032 full-scale groups, scaled to FY2040; hospitals unchanged):

  | Rate on physician and other non-hospital claims | FY2040 cost | Household rate |
  | --- | --- | --- |
  | **1.05: Medicare's fee schedule, plus the 10% add-ons on about half of spending (central)** | **−$275B** | **−1.4 points** |
  | 1.00: Medicare's fee schedule only | −$413B | −2.1 points |
  | 1.10 | −$138B | −0.7 point |

  The other non-hospital services are taken at the same basis, because Medicare pays them on its own fee schedules.
- **What it means.** The gross cost, the booked net cost and the household rate in this memo are all too high by about this much. At the central figure, package A's household rate would be about 9.2% rather than 10.6%. The households' gains would rise and the loser counts fall; they are not re-run here.
- **What it does not change:** the hospital glide, the employer contribution (set by former premiums), the states' payment and the credit.
- **Booking.** The coverage model and the booked rows are not changed in this PR. The fix goes in the booking PR (part 10), with the payroll point, and part 9 question 17 asks Espen to confirm it. If physician rates at Medicare's level look too low for access, that is design memo D3's question (the rate), not this one.

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

**Why the plan saves about 6%, in plain terms,** beside Urban's 2019 single-payer estimates [SRC-3223, table 3 and figures 2-3; 2020 dollars, fully phased in, on a 2019 baseline, so for structure, not figures]:
- **Urban's "lite" variant cuts national spending about 6%** ($3,287B against $3,497B). It has ACA-level benefits, cost sharing that rises with income, Medicare's rates with hospitals at 115%, and covers legally present residents.
- **Urban's "enhanced" variant raises it about 21%** ($4,217B). It has no cost sharing, adds dental, vision, hearing and long-term services and supports, and covers all residents.
- **This plan sits near "lite" on prices and near "enhanced" on cost sharing:**
  - Hospitals end at about 1.15 times Medicare. That saving, and lower administration, is what cuts spending.
  - Only small capped copays are kept, above 200% of poverty. With little cost sharing, people use more care, which pushes spending up.
  - Long-term care stays in Medicaid and the care flagship (HLT-7.07), so it isn't in these figures. In Urban's enhanced variant it is a large part of the 21%.
- **Net, the price and administration savings outweigh the extra use and the newly covered,** which is why the plan comes out about 6% below today's law, like Urban's lite variant.
- **Urban's sensitivities point the same way as part 6:**
  - hospitals at 140% of Medicare add $127-231B a year;
  - a state maintenance of effort lowers the federal cost by $192-242B;
  - administration at 3% instead of 6% saves $77-117B, though the authors judge 3% insufficient [SRC-3223, table 14].
- **Urban also models reforms that keep employer coverage** and widen subsidies and enrollment instead. They cost the government much less, but leave premiums and cost sharing in place. The plan's single-payer design is decided (care memo 1); they are noted only as the other end of the range.

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
   - **Base:** each worker's pay between a low-pay line of $20,000 (2026 dollars, price-indexed) and the Social Security wage base, about 61% of all pay. This share comes from the household model's CPS data, with a top-coding allowance. (The line is now set in 2026 dollars; in 2025 dollars, as merged, the share was 0.609.) The contribution is collected with the payroll tax.
   - **Who pays:** every employer, collected with the payroll tax on Form 941, and the self-employed through SECA. Employers that offered no coverage in 2028 step up to the full rate over 2035-44 (part 2.6).
   - **Size:** employers as a whole contribute what they would otherwise have spent on premiums for their workers, $2,197B in FY2040 at the full rate, or $2,156B with the phase-in. That covers private, state and local employers; the federal government's own share is federal money already. This follows the structure of Warren's 2019 plan, which set the employer contribution against what employers would otherwise pay [EV-CAR-725]. It makes the move neutral for employers as a group, so nothing depends on whether they pass premium savings into pay.
   - **Rate: 19.3%** of pay in the band, or about 11.9% of all pay. For a worker on $45,000: 19.3% × ($45,000 − $20,000) = $4,830, which is 10.7% of pay.
   - **Why the low-pay line:** without it, low-paid workers whose employers offer no coverage today carry the contribution through their pay with nothing to offset it. With it, the poorest fifth's households that lose fall from 4.0 million to 0.9 million with the fix, and from 4.5 million to 2.0 million without it, as merged (part 4.3).
   - **Why the cap at the wage base:** like a premium, the contribution doesn't rise with a top earner's pay. It therefore adds nothing to the top tax rate (part 2.4).
   - **The self-employed** pay it on 92.35% of net earnings, in the same band, as SECA does today.
3. **A household health contribution.**
   - **Base: taxable income,** the income tax's own: AGI less the standard deduction ($16,100 single, $32,200 couple in 2026, more at 65). There is no separate line. It is collected with the income tax and by withholding, and it falls on wages, pensions and investment income alike. Itemized deductions and the business-income deduction don't count; that is part 9, question 5. (The household model has no itemized deductions, so its taxable income is exactly this.)
   - **The alternative base,** as merged: AGI above $20,000/$40,000 in 2025 dollars, about $20,500/$41,000 in 2026 dollars. The standard deduction is a little lower than that line, so taxable income is about 5% larger, and the rate is lower: 10.6% against 11.2%.
   - **Rate:** whatever closes the rest. In package A that is **10.6%** (10.61%) in FY2040: $2,090B collected, of which $123B goes back to workers as the transition credit (part 2.7), leaving $1,967B.
   - **Yield:** a point raises about $197B collected (about $187B on the alternative base). That includes the pay workers used to put into premiums before tax, which is now income, and it is net of the budget model's 20% allowance for avoidance (part 2.5).
4. **A health payroll contribution of 2.9% on all pay.**
   - Workers and employers pay 1.45% each, and the self-employed 2.9%, on the same base and with the same collection as today's Medicare hospital insurance (HI) tax. It raises about **$580B** in FY2040.
   - **It is kept as one of the plan's own contributions, a design choice.** It is the plan's only charge on top earners' pay, where the capped employer contribution stops.
   - **Folding it into the employer contribution** (24.0% in the band, so that workers pay no payroll tax for health) is cleaner. It moves the charge on top pay onto the fourth fifth, which falls to about −$470 a household in 2026 dollars (part 5). It also costs about $108B of other tax: the worker's half leaves taxable cash pay, and the tax on former premiums loses its HI part.
   - **Until 2035** this money keeps paying Medicare's hospital claims for the people still in Medicare. HI's trust fund lasts to the endpoint (care `6-cost.md`, part 5) and then folds into the plan's fund (memo 3 B).
5. **The states' payment.**
   - States pay **100%** of what they would have spent on Medicaid outside long-term care for the people who move, indexed to the plan's growth: $689B in FY2040, which is $344B more than the booked 50%.
   - They still come out ahead: hospitals' uncompensated care ends, their share of Medicare's Part D payments ends, and their employees' premiums become the employer contribution at the same total cost.
6. **The tax on pay workers used to put into premiums before tax.**
   - The end of the employer exclusion is decided (memo 3 B). Once premiums end, the pay workers used to put into them before tax is taxed like other pay: **$279B** in FY2040.
   - Employers' own premium money never becomes pay in package A, because it goes into the employer contribution.
   - With the phase-in, the pay that the contribution doesn't yet take is taxed too: another $13B, so **$292B** in all.

**Paid back:** the worker transition credit, $123B in FY2040, refunded through the income tax to workers who had no job coverage, no plan of their own and no Medicare in 2028 (part 2.7).

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
| Employer health contribution | 2,156 | 26% | 19.3% of each worker's pay between $20,000 and the wage base (11.9% of all pay); employers with no 2028 coverage at 57.5% of it in FY2040 |
| Household health contribution, net of the worker transition credit | 1,967 | 23% | 10.6% of taxable income ($2,090B), less the credit ($123B) |
| Health payroll contribution | 580 | 7% | 2.9% of all pay (1.45% from workers, 1.45% from employers) |
| States' payment | 689 | 8% | 100% of former Medicaid spending for the people who move, indexed |
| Tax on pay formerly put into premiums, and on pay the phase-in leaves | 292 | 3% | Ordinary income and payroll tax on it |
| **The system's gross cost** | **8,407** | 100% | |

**The federal budget's view.** The new money these sources raise is **$3,794B**: the booked net cost ($4,094B) less the seam ($300B). It is made up of:
- the employer contribution's net yield, $1,482B. At the full rate it would be $1,511B, after lowering other tax by $686B, because those premiums never become taxable pay; the phase-in costs $28B ($41B less the $13B of tax on the pay it leaves);
- households, $1,967B: $2,090B collected less the $123B credit;
- the states' extra, $344B.

### 2.3 Year by year: how each year is paid (package A, $B)

| FY | Gross cost | Federal general revenue committed | Health payroll contribution | States | Employers | Households, net of the credit | Tax on former pre-tax premiums | Credit paid back | Household rate |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2030 | 50 | 0 | 0 | 0 | 0 | 50 | 0 | 0 | 0.4% |
| 2031 | 813 | 187 | 0 | 92 | 112 | 408 | 14 | 0 | 2.9% |
| 2032 | 1,169 | 259 | 0 | 127 | 156 | 607 | 20 | 0 | 4.1% |
| 2033 | 1,885 | 371 | 0 | 219 | 503 | 728 | 64 | 0 | 4.8% |
| 2034 | 2,823 | 528 | 0 | 350 | 1,002 | 815 | 127 | 0 | 5.2% |
| 2035 | 5,670 | 1,695 | 357 | 494 | 1,507 | 1,405 | 212 | 56 | 8.9% |
| 2036 | 6,778 | 2,156 | 495 | 553 | 1,699 | 1,630 | 244 | 87 | 10.1% |
| 2037 | 7,147 | 2,285 | 515 | 584 | 1,803 | 1,706 | 256 | 95 | 10.2% |
| 2038 | 7,549 | 2,423 | 536 | 617 | 1,913 | 1,793 | 267 | 104 | 10.4% |
| 2039 | 7,959 | 2,569 | 557 | 652 | 2,031 | 1,870 | 280 | 113 | 10.45% |
| **2040** | **8,407** | **2,724** | **580** | **689** | **2,156** | **1,967** | **292** | **123** | **10.6%** |
| FY2030-39 | 41,842 | 12,472 | 2,461 | 3,687 | 10,726 | 11,012 | 1,485 | 456 | |

The six source columns (from federal general revenue to the tax on former pre-tax premiums) add to the gross cost. The credit is collected in the household rate and paid back, so the households' column is net of it.

How the transition years are paid:
- **Employers start paying as each group moves:** for children's coverage from 2031, then for each third of employer groups in 2033-35. They pay on the premiums they paid for the workers who have moved. From the endpoint they pay the payroll-based contribution; employers with no 2028 coverage pay a tenth of it in 2035, rising a tenth a year (part 2.6). That leaves $46B uncollected in FY2035 (three quarters of a year), $64B in FY2036, falling to $41B in FY2040 and nothing from 2045.
- **The worker transition credit starts with the payroll-based contribution in 2035:** $56B in FY2035 (three quarters of a year), rising with pay to $123B in FY2040.
- **States pay with each Medicaid third.**
- **The 2.9% payroll contribution** goes to the plan from the endpoint. Before then it pays Medicare's hospital claims.
- **The household rate rises with the waves.** It starts near 3% because the early years carry costs that no payer moves with: the restoration, Medicare's upgrades and Medicare at 60.
- **Recommended:** set the rate in law as steps that follow this path (about 3% from 2031, 5% from 2033, 9% at the endpoint, then set each year to balance the fund), with the FY2030 restoration ($50B) on the general fund. (The table charges households that $50B, 0.4%, so the years add up; on the recommended path it moves to the general fund and the contribution starts in 2031.)
- **The catch:** a household whose own coverage hasn't moved yet (for example, a childless worker with job coverage in 2031-34) pays the contribution and its own premium share for two to four years. Part 9, question 9.
- **Growth.** After full adoption the household rate drifts up about 0.1 to 0.15 point a year, because the plan's cost grows at CBO's health rate (about 5.7% a year), faster than incomes. Design memo D2 addresses this.
- **After FY2040.** The phase-in ends in 2044, and the credit steps down over 2045-48 and ends in 2049. Once both stop costing money, about 0.8 point comes off the rate, on FY2040's economy (part 4.3, "The long run").

### 2.4 The top end, and why it can't carry much more

- **The stack before health.** With the plan's decided and booked measures, the combined top federal rate on wages is about **63% before health**:
  - 39.6% income tax (G9);
  - 12.4% Social Security above $250,000 (SS-1);
  - 5% Medicare (H1b), which includes today's 2.9%;
  - the booked 4 + 2 income points.

  The handover notes' 50.6% left out SS-1. Package A adds the 10.6% household contribution, for **73.6%**. The capped employer contribution adds nothing at the top.
- **The evidence.**
  - Diamond and Saez's revenue-maximizing top rate is about 73%, counting federal, state, payroll and sales taxes (`legacy/domains/domain-revenue.md`, "Combined top rates").
  - Reported income responds to tax rates most at the top: Gruber and Saez measured a taxable-income elasticity of 0.57 above $100,000 in 1992 dollars [EV-CAR-720]. Saez, Slemrod and Giertz's survey (2012; not yet in the register) puts the range at about 0.12-0.4. The check below runs 0.12, 0.25, 0.4 and the registered 0.57.
- **The stacking check** (`stacking_check()`). Suppose the elasticity is 0.25. Then the top 1%'s income shrinks as the rate rises, and the taxes already on it shrink with it. Counting both, the top 1% yields about **44%** of its new charge under package A.
  - That costs about $68B, or 0.35 point on the household rate. The fourth fifth falls to about +$300 (2026 dollars).
  - An uncapped employer contribution, on HI's base, would add 11.9 points at the top. The top 1% would then yield only about 21%, and the household rate would need about 12.4%.
  - **The stack is a plan-wide question for stage G.**

### 2.5 Avoidance, placed where it happens

The budget model's income-contribution yields carry a 20% allowance for avoidance, on top of JCT's own behavioral response. The household tables put all of it on the top fifth, shared in proportion to the charge, for three reasons:
- the base is taxable income counting only the standard deduction, so itemized deductions can't shrink it;
- withheld wages are misreported at about 1%, against 55% for income nobody reports [EV-CAR-719];
- measured responses below the top are small [EV-CAR-720].

So every household below the top fifth is charged its full statutory amount: the rate times its base. Part 5 shows the range: Gruber and Saez's elasticities applied to every fifth, and the first draft's even spread.

### 2.6 The employer contribution: mandatory, and built not to cut pay

Espen, November 15: "I think the employer contribution has to be designed so it's mandatory and also can't reduce worker pay, somehow. Maybe a slower phase in for those folks makes sense or something else." Five rules do this. The end of this part sets out what the law can and can't guarantee, and part 2.7 adds the credit for the workers most exposed.

**1. Mandatory, with nothing to opt out of.**
- It is a tax on the employer, like the employer's half of payroll tax. Employers deposit it with their payroll taxes and report it on the forms they already file: Form 941 (Form 943 for farms, Form 944 for the smallest employers, Schedule H for household employers, Form CT-1 for railroads). Each worker's amount goes in a new box on the W-2.
- The self-employed pay the same rate on the same band through SECA, on Schedule SE. So calling a worker a contractor saves nothing.
- **No small-firm exemption.** Warren exempted firms under 50 workers that didn't offer coverage. The Tax Policy Center's Burman argued that this puts a cliff at the 50th worker [EV-CAR-735]. Here the low-pay line and the phase-in protect small, low-paying employers without a cliff.
- **Burden:** one more line on returns employers already file, collected by the IRS with its existing deposit rules and penalties. No new agency.

**2. A slower start for employers that offered no coverage.**
- **The test:** the employer reported no group health coverage for 2028. The IRS already holds these records: Forms 1095-C from larger employers, Forms 1095-B from insurers (which name the sponsoring employer), and box 12 DD on the W-2. 2028 is the last full year before the law, so an employer can't qualify by dropping coverage after the law passes. (The handoff proposed 2029; 2028 closes that gap.)
- **The schedule:** a tenth of the full rate in calendar 2035, rising by a tenth each year, full from 2044.
- **Why that speed:** each year's step is 1.93% of pay in the band. For a $45,000 worker that is about $480, or 1.1% of pay, rising to about 1.7% of pay at the wage base. Pay rose 3.7% in 2026 [EV-CAR-722], and the model's path is about 3.2% a year. So even if every step came out of pay, pay could still rise in dollars every year. After prices (about 2.3% a year), it would be roughly flat for lower-paid workers through the decade and would fall slightly, by under 1% a year, for the best paid.
- **Who it covers:** KFF finds 92% of workers are at firms that offer coverage [EV-CAR-295]. KFF doesn't give the other 8%'s pay. The model assumes they look like the CPS's workers in households without job coverage, who earn about 56% of the average worker's pay in the band. On that assumption they earn about 4.5% of band pay.
- **Anti-gaming:** status is judged across a controlled group of businesses, as the tax code already does for benefit plans, and a successor keeps its predecessor's status, as state unemployment insurance does for experience ratings. Employers formed after the law pay the full rate: they set pay in the new system.
- **Cost:** $46B in FY2035 (three quarters of a year) and $64B in FY2036, falling to $41B in FY2040 ($28B after the tax on the pay it leaves, 0.14 point) and nothing from 2045.
- **Model note:** the CPS doesn't say whether a worker's employer offered coverage. The model draws the 4.5% from workers in households with no job coverage, by a fixed random draw.

**3. Pay rates can't be cut.**
- An employer may not lower the base pay rate of anyone it employed when its contribution began, through 2044, unless the job changes or the worker asks for fewer hours.
- **Enforcement:** the Labor Department's Wage and Hour Division, with remedies like the minimum-wage law's: back pay plus an equal amount in damages. To find cases it screens the quarterly wage records employers already send to state unemployment insurance, and the W-2s, for continuing workers whose pay fell. Workers can also complain.
- **Its limit:** it protects incumbents' pay rates in dollars. It doesn't protect raises, hours or the starting pay of new hires.

**4. Savings must reach pay.**
- Employers that used to spend more on premiums than they now pay in contribution save money. For three years from the January 2035 endpoint, when the payroll-based contribution starts (through 2037), they must raise the pay of the workers they covered by at least the difference, per worker: their 2028 premium cost (grown with health costs) less the new contribution on that worker's pay. They certify it once a year with the fourth-quarter Form 941, and it is checked by audit.
- **Sizes, in FY2040 terms (before tax):** about $771B of pay rises where former employer premiums exceed the contribution charged on the pay, against about $730B of contribution above former premiums where the reverse is true. For the second group, rule 3 stops pay cuts, so the difference can only come out of future raises. The two differ by the $41B phase-in. These sizes net premiums against contributions household by household; the model can't see employers, so they are a proxy for the employer-by-employer amounts.
- The household tables already assume the savings reach pay, so this rule costs nothing in the arithmetic. It makes that assumption more likely to hold. Urban's review of the evidence agrees that employers' savings pass back into wages, but not completely and not quickly (Gruber 2000, as cited in [SRC-3223, discussion]).

**5. Union contracts.**
- **Warren's provision:** employers with bargained coverage could cut their contribution down to the national average per worker if they passed the savings to workers "in the form of increased wages, pensions, or other collectively-bargained benefits," and newly bargained contracts could do the same, as an incentive to organize [EV-CAR-726; SRC-3356, read November 15].
- **What carries over:** savings under a contract go to its members, in whatever form they bargain: wages, pensions or other benefits. Either side can reopen the contract's health article within 12 months of the employer's first contribution. Until a new agreement, rule 4 applies and the savings are paid as wages. Employers' hourly payments into multiemployer health funds are part of that bargaining.
- **What doesn't:** a lower rate for union employers. Here the rate is uniform on pay, so there is no employer-specific amount to reduce, and a reduction would lose revenue. Whether the plan should encourage organizing belongs to the work flagship (stage F).

**What the law can and can't guarantee.**
- **It can guarantee:** that every employer pays; that incumbents' pay rates don't fall in dollars through 2044; that savings go into pay for three years; and a phase-in slow enough for normal raises to absorb.
- **It can't set** the raises employers would otherwise have given, or hours, hiring, new hires' pay or prices. Over time most of a payroll cost lands on pay:
  - when premiums rise 10%, covered workers' wages fall 2.3% (Baicker and Chandra [EV-CAR-296]);
  - total compensation falls $0.52 for each dollar of higher premiums, mostly through workers' premium shares (Anand [EV-CAR-299]). Under the plan there are no premium shares, so the adjustment has to come through pay;
  - CRFB expected Warren's contribution to be borne by workers through lower wages [EV-CAR-741].
- **So the memo assumes,** as CBO does, that in the long run total pay is fixed and the contribution comes out of it. The household tables are built that way.

**If pay doesn't behave as assumed** (FY2040, package A; households in 2026 dollars):

| Case | Household rate | Q1 | Q2 | Q3 | Q4 | Bottom-four households losing cash (by more than 5%) |
| --- | --- | --- | --- | --- | --- | --- |
| As assumed: the contribution comes out of pay, and savings go into pay | 10.6% | +5,062 | +7,837 | +7,164 | +782 | 26.9M (6.2M) |
| Pay holds where the contribution is above former premiums; owners bear the $730B | 10.2% | +5,104 | +8,361 | +7,984 | +2,197 | 20.8M (2.4M) |
| Employers that save keep half of it ($386B) | 10.8% | +4,409 | +6,198 | +5,168 | −259 | 29.1M (6.0M) |

**What the plan does about it:**
- The worker transition credit (2.7) protects the workers most exposed, whatever pay does.
- **Published counts each year,** from W-2s and state wage records: pay growth for continuing workers at phase-in employers, at employers that saved and at employers that now pay more, against all workers.
- **A review trigger:** if pay at saving employers rises by less than half their saving, or pay at phase-in employers falls behind other workers' by more than a year's step, Treasury and Labor report to Congress with options: extend rule 4, slow the phase-in, or extend the credit.
- This follows the design lens: published counts with a review trigger, not policing up front (`DEC-2026-11-09-13`).
- **Burden:** rules 3 and 4 are new duties on employers, for ten years and three years. They rest on records employers already file. Small employers that offered no coverage face only rule 3.

**Considered and not recommended:** moving each employer gradually from its own 2028 premium cost to the full rate, as Warren's plan did. It would spread the change for employers that now pay more. But it needs each employer's 2028 cost, which only larger employers report on the W-2, and it makes the rate employer-specific for a decade. Rule 3 plus normal raises does the same job more simply.

### 2.7 The fix for households that lose cash: a worker transition credit

- **Who qualifies (one plain test, from records the government holds):** people who had earnings in 2028 (a W-2 or Schedule SE) and no job coverage, no individual-market plan and no Medicare that year (Forms 1095-A, 1095-B and 1095-C, and Medicare's enrollment). That means people who were uninsured, on Medicaid or on other public coverage. No application: the IRS knows who qualifies.
- **How much:** the employer contribution charged on their pay (the new W-2 box, or Schedule SE), **in full**. It phases out with the household's AGI between **$60,000 and $120,000** single ($120,000 and $240,000 for couples), in 2026 dollars, price-indexed like the other lines.
- **How it is paid:** a refundable credit on the income tax return, delivered through the year by lower withholding, so it arrives with each paycheck.
- **When:** from the January 2035 endpoint, in full through 2044 (the phase-in decade), then a fifth less each year (80% in 2045, down to 20% in 2048), with none from 2049.
- **Cost:** $56B in FY2035, $123B in FY2040 (0.6 point on the household rate), $456B over FY2030-39.
- **Why these people:**
  - Their employer paid nothing for their health care, so the contribution comes out of their pay with nothing behind it.
  - People who bought their own plan, or paid Medicare's premiums, stop paying for it, so they already gain. The self-employed example in 4.2 is +$3,700 without the credit, so the test leaves them out. The cross-check found about $25B of an earlier version going to households with Medicare; leaving Medicare out saves $22B (0.1 point) and adds about 0.6 million households that lose a little.
- **Why transitional:** in the long run, two workers on the same pay pay the same, whatever coverage they had in 2028. The credit gives the people who start with nothing from an employer the same slow start the phase-in gives employers. The long run is set out honestly in 4.3.
- **Burden:** none for workers. The IRS works out who qualifies from its own records, and employers report the contribution on the W-2 they file anyway.
- **Limits of the model:** the CPS can't tie coverage to each worker, so the model applies the test to tax units, which approximates who qualifies. People who start work after 2028 don't qualify; they take jobs whose pay is already set in the new system.
- **The alternatives are priced in 4.3:** a credit for every worker, a credit at 75%, a narrower phase-out, a higher low-pay line instead, and a permanent credit for low-paid workers.

## Part 3. The packages

*Superseded: the packages are re-priced on the corrected cost, against the take-home test, in `health-cost-review.md`, part 2 (recommended there: package E).*

All four packages cover the FY2040 gross cost of $8,407B exactly. They share:
- the federal general revenue committed ($2,724B);
- the 2.9% payroll contribution;
- the states' payment (100%, $689B);
- the employer base, the employer phase-in (2.6) and the worker transition credit (2.7).

They differ in how households and employers make up the rest.

Households in 2026 dollars:

| | **A. Contributions sized to the system (recommended)** | B. Household 5.5%, with a rebated VAT | C. Household 5.5%, larger employer contribution | D. Household 5.5%, with a top tier |
| --- | --- | --- | --- | --- |
| Household contribution on taxable income | **10.6%** | 5.5% | 5.5% | 5.5% |
| Second tier on AGI above $100K/$200K (2025 dollars) | — | — | — | 15.1 points |
| Value-added tax (a quarter rebated per person) | — | 12.8% | — | — |
| Employer contribution in the band (share of all pay) | 19.3% (11.9%) | 19.3% (11.9%) | 33.6% (20.7%) | 19.3% (11.9%) |
| Health payroll contribution | 2.9% of all pay | 2.9% | 2.9% | 2.9% |
| Top federal rate on wages | 73.6% | 68.5% | 68.5% | 83.6% |
| **Net per household, FY2040: Q1 / Q2 / Q3 / Q4** | **+5,062 / +7,837 / +7,164 / +782** | +3,686 / +6,172 / +6,230 / +1,567 | +5,149 / +8,269 / +7,806 / +905 | +5,194 / +9,086 / +10,633 / +6,718 |
| Q5 / top 1% | −17,150 / −97,247 | −13,961 / −75,944 | −18,433 / −69,584 | −27,935 / −315,829 |
| Bottom-four households that lose (millions, of about 121) | 26.9 | 35.0 | 21.8 | 11.6 (on paper) |
| … losing more than 5% of their income | 6.2 | 9.0 | 7.4 | 1.6 (on paper) |
| New collection machinery | none | a federal VAT | none | none |
| On the evidence | holds; the top 1% yields about 44% of its new charge | holds; hardest on the bottom two fifths | holds; workers bear it through pay | **doesn't hold**: the top 1% yields about 25% of its new charge (part 2.4) |

**Why A:**
- **Health care as a right:** no premiums, no deductibles, care free at the point of use except small capped copays above 200% of poverty.
- **The single payer's savings are in the cost** (part 1).
- **The most affordable for the bottom three fifths** of the three credible packages (A, B, C).
- **Existing machinery only:** income tax withholding and the payroll tax system (`DEC-2026-11-13-08`).
- **It doesn't meet a 5-6% statutory household rate.** In shares of AGI, the second fifth pays about 5.6% and the middle fifth about 7.6%.

**What 5-6% costs:**
- **B:**
  - a federal VAT of about 13% on top of state sales taxes;
  - the bottom three fifths lose $900-1,700 a year against A (2026 dollars), and about 8 million more bottom-four households lose;
  - it needs a new federal collection system;
  - at a 6% household rate the VAT is 11.6%; at 5%, 14.1%.
- **C:**
  - employers pay about 1.7 times what they would otherwise have spent, because the larger employer contribution also pays for the phase-in and the credit;
  - in the long run workers bear it through pay, so it is a worker payroll tax in all but name;
  - it is a big jump in labor cost for employers that offered no coverage.
- **D:**
  - it looks best on paper and is the least likely to deliver;
  - at about 84% on top wages, and about 99% if the top tier lost 60% to avoidance, most of it wouldn't be collected.

## Part 4. Households

### 4.1 Package A by fifth, a table to multiply (FY2040, 2026 dollars per household a year)

| | Q1 | Q2 | Q3 | Q4 | Q5 | Top 1% |
| --- | --- | --- | --- | --- | --- | --- |
| AGI (before the plan) | 11,464 | 46,387 | 95,746 | 160,660 | 381,713 | 1,317,326 |
| Taxable income, including the pay formerly put into premiums (the base) | 2,580 | 24,432 | 68,657 | 133,708 | 357,767 | 1,309,243 |
| × the household rate | 10.61% | 10.61% | 10.61% | 10.61% | 10.61% | 10.61% |
| **= household contribution charged** | **−274** | **−2,593** | **−7,286** | **−14,190** | **−37,969** | **−138,948** |
| … as a share of AGI | 2.4% | 5.6% | 7.6% | 8.8% | 9.9% | 10.5% |
| Less what avoidance keeps from being collected (top fifth only) | +0 | +0 | +0 | +0 | +12,098 | +44,745 |
| Premiums and out-of-pocket costs they stop paying | +3,362 | +6,895 | +11,738 | +16,182 | +18,804 | +15,955 |
| Employer premiums that would have gone to coverage, now pay | +2,244 | +6,795 | +11,781 | +15,228 | +16,731 | +16,516 |
| Tax on former premiums, both shares, now paid as pay | −208 | −2,158 | −5,197 | −7,378 | −8,259 | −11,600 |
| Employer health contribution, borne through pay | −422 | −2,901 | −7,343 | −14,465 | −27,647 | −35,535 |
| Less the tax on the pay the contribution takes instead | +131 | +906 | +2,294 | +4,518 | +8,637 | +11,100 |
| The phase-in, less tax on the pay it leaves | +21 | +88 | +139 | +176 | +259 | +447 |
| Worker transition credit | +208 | +805 | +1,038 | +710 | +198 | +73 |
| **Net** | **+5,062** | **+7,837** | **+7,164** | **+782** | **−17,150** | **−97,247** |
| … FY2040 dollars | +6,970 | +10,790 | +9,864 | +1,077 | −23,612 | −133,889 |
| Net as a share of AGI | +44.2% | +16.9% | +7.5% | +0.5% | −4.5% | −7.4% |
| D3 measure: expanded income | 24,429 | 66,562 | 113,153 | 178,379 | 407,875 | 1,362,468 |
| Net as a share of expanded income | +20.7% | +11.8% | +6.3% | +0.4% | −4.2% | −7.1% |

How to read it:
- **Multiply down the first rows:** the base times 10.61% gives the charge, and the charge over AGI gives the share of income. For the middle fifth: 10.61% × $68,657 = $7,286, which is 7.6% of its $95,746 AGI.
- **The base** is taxable income as the budget model's yield implies it, including the pay workers used to put into premiums before tax, which becomes taxable once premiums end. It is a little above taxable income before the plan.
- **The last two rows** are D3's fairness measure, expanded income, which also counts untaxed Social Security and benefits and the employer's payroll tax. It is used only for the fairness test and for the "more than 5% of income" counts in 4.3, and it is labelled wherever it appears. The poorest fifth's AGI is small because most of its income isn't taxed, so its gain looks very large against AGI.

The 2.9% payroll contribution is not a row: households pay it today and keep paying it.

How the table is built:
- **Households:** about 151 million in FY2040, ranked by size-adjusted income, with equal numbers in each fifth.
- **Spreading rows across fifths:** each row uses one of the household model's measured keys (`models/tools/household/keys.csv`): `health_hh`, `employer_cov`, `exclusion_end`, the band of pay between $20,000 and the wage base, and taxable income. The phase-in and the credit use keys built from the 2029 households themselves (`no_offer()`, `credit_key()`).
- **Why the credit reaches the top fifth at all:** a household can hold more than one tax unit, such as a grown child with a low income and no coverage, and the credit follows the tax unit's own income.
- **Employer rows:** they follow CBO in assuming total pay is fixed. Premiums an employer no longer pays would become pay, and the contribution comes out of that pay instead. So in total those rows nearly cancel, but not within a fifth: premiums follow coverage, while the contribution follows pay.
- **Cash only:** the table doesn't count the value of coverage to people who are uninsured now.

### 4.2 Worked examples (FY2040, 2026 dollars)

Each example is a household with this income in 2026 dollars, in FY2040, at FY2040's rates. Every amount is in 2026 dollars; the last column also gives FY2040's own dollars.
- **Health costs:** KFF's 2026 premiums (single $9,804, the worker paying $1,672; family $28,303, the worker paying $7,471 [EV-CAR-722, EV-CAR-111]) and the coverage model's out-of-pocket costs, copays and $3,500 Medicare premium. They grow about 4.8% a year per person (CMS's 5.4% for total national health spending [EV-CAR-056], less population growth of about 0.5% a year), against prices of about 2.3% a year. So by FY2040 they are about 1.41 times today's in 2026 dollars.
- **Lines:** the $20,000 low-pay line, the credit's $60,000/$120,000 and the standard deduction ($16,100 single, $32,200 couple, plus $1,650 for each spouse 65 or over) are all price-indexed, so they keep their 2026 values here. The wage base grows with average pay, so it is about $208,000 here.
- **The household contribution:** 10.61% of taxable income, which is AGI after the plan (now including the pay change and the former pre-tax premium share) less the standard deduction.
- **Tax on pay that changes:** the federal bracket plus both halves of the remaining payroll taxes.
- **The employer rate:** 19.3% on actual pay in the band. If the budget model's payroll point is low (part 8), the rate on actual pay would be about 16-17%, and every employer amount here would be about a sixth smaller. The fifth tables and loser counts don't depend on this: they spread the contribution's total.

Package A:

| Household | Stops paying (premiums + out of pocket − copays) | Employer: would have spent → pays | Pay change, then tax on it | Tax on former pre-tax premium | Household contribution: rate × (AGI − deduction) = charge (share of AGI) | Worker transition credit | **Net a year** (FY2040 dollars) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Single worker, $45,000, single job coverage | 2,353 + 2,272 − 500 = **4,125** | 11,445 → 19.3% × 25,000 = 4,828 | +6,617, −1,806 | −642 | 10.61% × (53,970 − 16,100) = −4,019 (7.4%) | — | **+4,274 (+9.5%)** (+5,885) |
| Single worker, $45,000, employer offers no coverage, uninsured today | 0 + 2,958 − 500 = **2,458** | 0 → 2,776 (57.5% of 4,828, the phase-in in FY2040) | −2,776, +758 | 0 | 10.61% × (42,224 − 16,100) = −2,772 (6.6%) | +2,776 | **+443 (+1.0%)** (+611), and now covered |
| Family of four, $90,000, family job coverage | 10,515 + 9,088 − 2,000 = **17,604** | 29,320 → 19.3% × 70,000 = 13,519 | +15,800, −4,314 | −2,871 | 10.61% × (116,315 − 32,200) = −8,927 (7.7%) | — | **+17,293 (+19.2%)** (+23,809) |
| Family of four, $160,000, family job coverage | **17,604** | 29,320 → 19.3% × 140,000 = 27,039 | +2,281, −851 | −3,922 | 10.61% × (172,796 − 32,200) = −14,921 (8.6%) | — | **+191 (+0.1%)** (+262) |
| Retired couple on Medicare, $60,000 (Social Security $36,000 and pension $24,000; AGI $33,000) | 7,420 + 7,771 − 1,000 = **14,191** | — | — | — | AGI below the deduction of 35,500: 0 | — | **+14,191 (+23.7%)** (+19,538) |
| Retired couple on Medicare, $110,000 (AGI $102,500) | **14,191** | — | — | — | 10.61% × (102,500 − 35,500) = −7,111 (6.9%) | — | **+7,080 (+6.4%)** (+9,748) |
| Self-employed single, $70,000 net, buys an individual-market plan | 12,474 + 5,547 − 500 = **17,521** | pays the employer contribution: 19.3% × (92.35% × 70,000 − 20,000) = −8,622 | — | — | 10.61% × (65,000 − 16,100) = −5,190 (8.0%) | — (had a plan of their own) | **+3,709 (+5.3%)** (+5,106) |

**The uninsured worker, before and after the fix, and in the long run:**
- **Before the fix:** the full 4,828 comes out of pay, with 1,318 back in tax, and the household contribution is 9.84% × (40,172 − 16,100) = 2,369. Net **−3,422 (−7.6%)**.
- **With the fix, FY2040:** **+443 (+1.0%)**. If the employer did offer coverage but this worker wasn't on it, the contribution is the full 4,828, the credit returns all of it, and the net is about +1,200.
- **In the long run** (after the phase-in ends in 2044 and the credit in 2049): about **−$3,400 a year** on FY2040's economy, against a world where they would still be uninsured. They then pay about $7,200 a year in the two contributions: much the same as other workers on that pay, and less than the $16,100 that goes to health care for a $45,000 worker with job coverage under today's system (the employer's and the worker's premiums and the out-of-pocket costs). Part 4.3 sets out the choice.

**Two example assumptions to know** (the second cross-check):
- The retired couple at $60,000 is given $9,000 of taxable Social Security. Section 86's thresholds aren't indexed, so by FY2040 about $12,900 would be taxable. That puts AGI near $36,900, a contribution of about $150, and a net of about +14,040.
- The self-employed example leaves out two effects. When premiums end, the self-employed health insurance deduction ends with them, adding about $12,500 to AGI (about −$2,800 in tax and contribution). Against that, a deduction for the employer contribution would be worth about +$1,950 (part 9, question 11). Net, the example is nearer +$2,800 than +$3,700.

**On the alternative base** (AGI above $20,500/$41,000 in 2026 dollars, at 11.16%), the same households come out within about $500 of these figures. For example, the uninsured worker is +797 and the family at $160,000 is +419.

The same households under the other packages (2026 dollars):

| Household | B | C | D |
| --- | --- | --- | --- |
| Single worker, job coverage | +1,410 | +3,807 | +6,211 |
| Uninsured worker | −3,022 | +2,454 | +1,779 |
| Family at $90,000 | +13,910 | +14,862 | +21,594 |
| Family at $160,000 | −6,321 | −4,081 | +7,379 |
| Retired couple at $60,000 | +8,237 | +14,191 | +14,191 |
| Retired couple at $110,000 | −120 | +10,506 | +10,506 |
| Self-employed | −1,184 | −180 | +6,209 |

D's figures rest on a top tier the evidence says wouldn't be collected.

### 4.3 Affordable at every income? Who loses, and how many (package A)

How this is counted (`micro()`): each fifth's total is spread over its own households in proportion to each one's base (its coverage on the CPS, its pay in the band, its taxable income). The fifths' averages are therefore exactly those in 4.1.

**Before and after the fix** (millions of FY2040 households). "Losing more than 5% of income" uses D3's expanded income, the fairness test's measure, because AGI leaves out most of the poorest households' income:

| | Q1 | Q2 | Q3 | Q4 | **Bottom four** | Q5 |
| --- | --- | --- | --- | --- | --- | --- |
| Paying more than they save, before the fix | 2.2 | 5.7 | 7.8 | 15.0 | **30.7** | 24.4 |
| … losing more than 5% of their income | 0.7 | 3.0 | 3.2 | 5.5 | **12.4** | 11.6 |
| **Paying more than they save, with the fix (package A)** | **0.9** | **3.4** | **6.8** | **15.8** | **26.9** | 25.0 |
| **… losing more than 5% of their income** | **0.0** | **0.1** | **0.6** | **5.4** | **6.2** | 12.6 |

- **A correction.** The merged memo put the over-5% count at 16.1 million for the bottom four. That test compared FY2040 dollars with 2029 incomes, which are about 30% smaller. On FY2040 incomes the merged package's count is 11.7 million (11.8 million with the low-pay line now set in 2026 dollars). The counts of households that lose at all were right.
- **What the fix does:**
  - In the bottom three fifths, households losing more than 5% fall from **6.9 million to 0.75 million**, and households losing at all from 15.7 million to 11.1 million.
  - The median loss among bottom-four losers falls from about $4,400 to about $3,400 a year.
  - On the counts, the credit does almost all the work. The phase-in mainly keeps pay from falling at employers that never offered coverage, including for their workers above the credit's income range, and gives those employers time.
- **Who still loses** (bottom four, with the fix):
  - about 59% have job coverage that cost little relative to their pay: mostly single workers on good pay. A premium is the same for everyone; the plan's contributions follow pay;
  - about 37% are working households with no job coverage, mostly above the credit's income range;
  - about 9% are Medicare households with income well above the deduction.
  - (The groups overlap, for example a Medicare enrollee living with a covered worker, so the shares add to more than 100%.)
- **The fourth fifth is where affordability is thinnest:** half of it pays more, and the fix doesn't change that. The rate rise that pays for the credit adds about 0.8 million losers there. Design memos D1 and D2 (part 6) bring the bottom-four count to **20.8 million** (3.5 million losing more than 5%) and lift the fourth fifth to about +$3,240.
- **The low-pay line protects the poorest.** Without it (the contribution at 14.3% on all pay up to the wage base), the poorest fifth's losers rise from 0.9 million to 4.0 million, and the bottom-four count to 33.5 million. That variant keeps the credit sized on the band, so it overstates the line's effect somewhat; a credit on all pay up to the wage base would narrow the gap.

**The fix's design, against the alternatives** (FY2040, package A; each re-solves the household rate; the fourth fifth's average in 2026 dollars):

| Design | Household rate | Cost ($B) | Bottom-four losers (M) | … over 5% (M) | Bottom three fifths over 5% (M) | Fourth fifth's average |
| --- | --- | --- | --- | --- | --- | --- |
| None | 9.84% | 0 | 30.7 | 12.4 | 6.9 | +926 |
| Phase-in only | 9.99% | 28 | 30.6 | 11.9 | 6.4 | +909 |
| **Phase-in and the transition credit (recommended)** | **10.61%** | **152** | **26.9** | **6.2** | **0.75** | **+782** |
| The same credit at 75% of the contribution | 10.46% | 121 | 28.6 | 6.9 | 1.5 | +813 |
| The credit phased out between $50,000 and $100,000 | 10.51% | 132 | 26.9 | 6.8 | 1.2 | +686 |
| The credit for every worker, not only those without coverage in 2028 | 13.97% | 813 | 23.1 | 6.8 | 1.7 | +2,996 |
| The same, at half the contribution | 11.98% | 421 | 26.9 | 9.1 | 4.1 | +1,952 |
| No credit; the low-pay line raised to $30,000 (the employer rate becomes 22.8% in the band) | 9.99% | 28 | 28.6 | 10.5 | 4.9 | +1,012 |
| Recommended, on the alternative base (AGI above $20,500/$41,000) | 11.16% | 152 | 25.2 | 5.9 | 0.7 | +983 |

What the comparison shows:
- **Targeting is what makes it work.** A credit for every worker costs more than five times as much. It lifts the fourth fifth's average, but the rate rise to pay for it leaves slightly more households losing more than 5%.
- **At 75%** the credit roughly matches the worker's loss after tax for a typical worker, but it leaves about twice as many in the bottom three fifths losing over 5%. In full, it is simpler to explain: you get back what was charged on your pay.
- **A higher low-pay line** helps everyone's lowest pay, including people who already gain, and moves the contribution onto pay above $30,000. It does about a third as much for the households losing more than 5%.
- **The alternative base** protects a little more (1.7 million fewer losers) at 0.55 point more on the rate. The standard deduction sits a little below its line, so taxable income reaches slightly further down.

**The long run** (after the phase-in ends in 2044 and the credit in 2049):
- Priced on FY2040's economy, the long run is the "None" row: a 9.84% rate, and 30.7 million bottom-four households paying more than they would under today's law, 12.4 million by more than 5%.
- By then the comparison means less. It sets someone's health contributions against a world in which they would still be uninsured, or on Medicaid at no cost. Workers on the same pay pay much the same, and less than today's premiums take out of pay for workers with job coverage (the $45,000 example in 4.2).
- **The alternative is a permanent credit for every low-paid worker** (the contribution on their pay, phased out between $30,000 and $60,000). It costs about $169B (0.85 point), more than the transition credit, and does less: 28.4 million losers and 10.6 million over 5%, because most of it goes to workers who already gain. **Recommended: keep the credit transitional** (part 9, question 7).

**These counts are rough.** The CPS under-reports Medicaid, and the model gives every person in a coverage group that group's average cost. Real premiums and medical bills vary far more, so the true spread is wider in both directions.

## Part 5. What changes the numbers: sensitivities on package A (FY2040)

Households in 2026 dollars:

| Case | Household rate | Q1 | Q2 | Q3 | Q4 | Q5 | Top 1% |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **A as recommended (taxable-income base, with the fix)** | 10.61% | +5,062 | +7,837 | +7,164 | +782 | −17,150 | −97,247 |
| A on AGI above $20,500/$41,000 (the alternative base) | 11.16% | +5,116 | +8,149 | +7,560 | +983 | −18,114 | −102,610 |
| A before the fix (taxable-income base) | 9.84% | +4,853 | +7,132 | +6,515 | +926 | −15,731 | −90,934 |
| A as merged in #385 (line base, no fix; the low-pay line now in 2026 dollars) | 10.35% | +4,903 | +7,422 | +6,882 | +1,113 | −16,626 | −95,908 |
| With design memos D1 and D2 | 8.77% | +5,110 | +8,286 | +8,426 | +3,240 | −12,669 | −80,931 |
| Savings booked (administration 3%, drugs 23% lower) | 9.35% | +5,094 | +8,145 | +8,032 | +2,471 | −14,072 | −86,037 |
| The seam not fixed (the cautious reading) | 12.13% | +5,023 | +7,465 | +6,119 | −1,253 | −20,860 | −110,756 |
| The 2.9% folded into the employer contribution (workers pay no health payroll tax; employer 24.0%) | 11.16% | +5,186 | +7,901 | +6,782 | −468 | −18,302 | −78,080 |
| The 2.9% repealed and its money split between the two contributions | 12.22% | +5,215 | +8,026 | +7,026 | +31 | −17,225 | −82,751 |
| Employer contribution with no low-pay line (14.3% up to the wage base) | 10.61% | +4,595 | +6,919 | +6,377 | +794 | −14,990 | −93,718 |
| Employer contribution on all pay, HI's base (11.9%) | 10.61% | +4,702 | +7,320 | +7,180 | +2,128 | −17,634 | −159,911 |
| Employers at 65% of what they'd otherwise spend (the first draft's share) | 13.03% | +5,021 | +7,632 | +6,862 | +724 | −16,544 | −110,314 |
| The first draft's package on the corrected method (65%, 80%, no seam fix, no fix) | 14.75% | +4,594 | +6,296 | +4,924 | −1,278 | −21,351 | −166,657 |
| States at 80% / 50% / 0% | 11.31% / 12.36% / 14.11% | +5,044 / +5,017 / +4,972 | +7,666 / +7,410 / +6,983 | +6,684 / +5,965 / +4,765 | −153 / −1,555 / −3,892 | | |
| Same as all pay, after the stacking check (elasticity 0.25) | 12.36% | +4,657 | +6,894 | +5,981 | −206 | −21,888 | −175,400 |
| A after the stacking check (elasticity 0.25 / 0.4 / 0.57, the registered figure) | 10.96% / 11.42% / 11.91% | +5,053 / +5,041 / +5,028 | +7,752 / +7,639 / +7,519 | +6,926 / +6,610 / +6,272 | +318 / −296 / −957 | | |
| Avoidance spread "elastic" / "even" | 10.61% | +5,085 / +5,113 | +8,052 / +8,321 | +7,776 / +8,540 | +1,522 / +3,504 | | |
| Top 1% at its IRS share of the base (29%, against the CPS's 12%) | 10.61% | +5,113 | +8,318 | +8,530 | +3,484 | −21,750 | −310,039 |
| Pay holds where the contribution is above former premiums (owners bear it; part 2.6) | 10.20% | +5,104 | +8,361 | +7,984 | +2,197 | −19,949 | −219,164 |
| Employers that save keep half their saving (part 2.6) | 10.83% | +4,409 | +6,198 | +5,168 | −259 | −11,819 | −26,145 |

What the table shows:
- **Pass-through.** At 100%, employers as a group keep no net saving. But some employers save and others pay more (part 2.6). If those that save kept half of it, the fourth fifth would fall to about −$260 and 2.2 million more bottom-four households would lose. That is what rule 4 and the review trigger are for. In the first draft's package, the aggregate check alone (employers passing on half [EV-CAR-299]) put the fourth fifth at about −$2,700.
- **The fourth fifth** stays positive except in these cases: the cautious seam reading, states at 80% or less, the 2.9% folded into the employer contribution, the first draft's shares, employers keeping half their savings, and top-end elasticities of 0.4 or more.
- **The rest of the plan.** Scenario Q, the rest of the plan without health, gives the fourth fifth +$552 in FY2040 dollars (`models/tools/household/results.md`, section 8).

## Part 6. Design memos: changes to the decided design, for Espen to weigh

Espen, November 15: "it's ok to reopen parts of the design if compelling evidence suggests we should." Each memo keeps the decided design as the baseline and prices the change on the corrected model in FY2040. A point of the household rate is about $197B.

**D1. Administration.**
- **Options:**
  - A: 5%, the decided working figure;
  - B: book 4%, with 3% as the specification's target;
  - C: book 3%.
- **Effect:** B −$92B (0.5 point); C −$181B (0.9 point).
- **Evidence:**
  - Traditional Medicare's administration was 1.4% of its spending in 2017 [EV-CAR-217].
  - Warren's plan assumed 2.3%. Urban's researchers called that too low and 6% more reasonable [EV-CAR-742].
  - Urban's 2019 single-payer estimates used 6%, and judged 3% "insufficient" for fraud prevention, care management and monitoring quality and access; at 3% their "lite" variant's national spending fell by $77B (2020) [SRC-3223, table 14]. That supports booking 4% and treating 3% as a target to earn, not to assume.
- **Quality and access:** little risk at 4%. At 3%, the budgets for payment integrity and member services would need protecting.
- **Recommendation: B.**

**D2. A national health budget.**
- **Options:**
  - A: no budget; growth follows CBO's health path, about 5.7% a year;
  - B: from 2037, hold the plan's spending growth to nominal GDP growth plus 1 point, with a review trigger and an automatic report to Congress if it's missed;
  - C: hold growth to GDP growth.
- **Effect in FY2040:** B −$270B (1.4 points); C −$590B (3.0 points). The effect grows every year after.
- **Evidence:**
  - Warren's plan counted $1.1 trillion over ten years from slower cost growth [EV-CAR-724]; Urban's John Holahan said getting health spending growth down to GDP growth is not something the country has ever done [EV-CAR-742].
  - Urban's researchers note that this has never been done in the US [EV-CAR-742].
  - B leaves room above GDP for an older population and new treatments.
- **Quality and access:** if growth runs hot, a budget squeezes payment rates or volume. The review trigger is the guard against that.
- **Recommendation: B.** The specification would set the mechanism: global hospital budgets and an update rule for fees. This is the largest affordability lever after the payment rate, and it is the long-run answer to the household rate's drift.

**D3. The payment rate** (decided: about 1.15 times Medicare, with a hospital glide to 2036).
- **Options:** A: 1.15; B: 1.10; C: 1.05.
- **Effect:** B −$341B (1.7 points); C −$681B (3.5 points). The rate is the largest single driver of cost (care `6-cost.md`, part 6).
- **Evidence:**
  - Warren's plan paid hospitals 110% of Medicare; Urban assumed 115% [EV-CAR-732]. In Urban's sensitivity, hospitals at 140% added $127B a year to its "lite" variant (2020) [SRC-3223, table 14]. Urban also notes that lower rates need a long phase-in, which raises costs in the transition; the decided glide to 2036 does that.
  - The decided glide protects hospitals moving down from commercial prices of about 2.1 times Medicare (memo 5 B).
- **Quality and access:** rural and safety-net hospitals are the most exposed.
- **Recommendation: A**, revisited when the glide ends in 2036, with data on hospital margins. The evidence doesn't yet compel a change.

**D4. Copays** (decided: small capped copays above 200% of poverty, memo 4 C).
- **Options:** A: as decided; B: none at all, as S. 1506 has.
- **Effect:** B +$251B (1.3 points).
- **Recommendation: A.** The copays are small, capped and waived below 200% of poverty. Removing them would raise the rate for everyone.

**Package A with D1 B and D2 B:** a household rate of **8.8%**, the fourth fifth at +$3,240 (2026 dollars), and 20.8 million bottom-four households losing cash (3.5 million by more than 5%).

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
| Employers | Paper: 7.5% of payroll, the first $2 million exempt. In the transition, per enrolling worker, the higher of 75% of premiums or the 7.5% | Nothing | 98% of each employer's prior per-worker spending, converging to the national average. Firms under 50 workers that don't offer coverage are exempt [EV-CAR-725, EV-CAR-726] | What employers as a whole would otherwise spend, as a contribution on pay between a $20,000 line and the wage base. Mandatory for all, through Form 941 and SECA; phased in over 2035-44 for employers with no 2028 coverage; pay rates protected; savings passed into pay (part 2.6) |
| States | Eligibility no stricter than January 2025's; a floor on institutional long-term care spending (sec. 204) | No maintenance of effort; long-term care moves into the program | A maintenance of effort of about $6T: Medicaid and CHIP, and state employee premiums [EV-CAR-727] | 100% of former Medicaid spending outside long-term care, indexed |
| Households | Paper: 4% above about $29,000 for a family of four | Nothing | "No new middle-class taxes": higher take-home pay is taxed under current law [EV-CAR-728] | 10.6% of taxable income, with a transition credit for workers who had no coverage in 2028 |
| Top-end and other revenue | Paper: about $4.6T (rates to 52%, a 1% wealth tax, the estate tax and more) | None | Financial transactions tax, wealth and capital-gains taxes, corporate changes, the tax gap, immigration reform, ending overseas war funds [EV-CAR-729, EV-CAR-730] | None for health: the plan's top-end taxes fund its other flagships |
| HI payroll tax | Not mentioned | Not mentioned | Kept | Kept at 2.9% as the plan's own contribution; into the plan's fund from 2035 |
| Cost assumptions | — | — | Administration 2.3%, hospitals at 110% of Medicare [EV-CAR-744]; $1.1T from slower cost growth [EV-CAR-724] | Administration 5% (D1: 4%); 1.15 times Medicare; CBO's growth (D2: GDP + 1) |
| What reviewers found | CRFB and TPC qualify the paper's figures [EV-CAR-714 to EV-CAR-716] | — | CRFB: the direct offsets about right, the extra revenue well short; +$6.1T to deficits, range −$1.2T to +$11.2T [EV-CAR-737 to EV-CAR-741]. TPC: the employer charge works like a head tax and penalizes hiring the 50th worker [EV-CAR-735]; the stacked top taxes could pass 100% [EV-CAR-736] | Part 8's cross-check; part 2.4's stack |

What this plan takes, and what it does differently:
- **From Warren:**
  - the order: cost first, then financing;
  - an employer contribution set against what employers would otherwise spend;
  - a maintenance of effort for the states.
- **Unlike Warren:**
  - The employer contribution is on pay, not a charge per worker. TPC found the per-worker charge works like a head tax [EV-CAR-735]. Here the low-pay line, rather than a small-firm exemption, protects low-paid workers, and a ten-year phase-in replaces the exemption for employers that never offered coverage.
  - Union contracts keep Warren's choice of how savings reach members (wages, pensions or other benefits), but not a lower rate for union employers (part 2.6, rule 5).
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
- the per-point yield on the old base: $180.2B. The merged memo's $187B (now $197B on taxable income) adds the pay formerly put into premiums before tax, which is now income (the second fix below);
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

**The agent review of #385 (November 15)** confirmed the arithmetic. It also found that the worked examples grew per-person health costs at the total national rate (5.4%), which includes population growth. They now use per-person growth, about 4.8%; the family at $90,000 moves from about +$15,800 to +$13,900. The fifth tables were not affected.

**The second cross-check (#386, November 15).** A fresh agent re-derived the fix's figures by its own route, from the household records, without the new functions.
- **What it confirmed:**
  - the phase-in's FY2040 share not yet charged (0.425) and its cost;
  - the credit's cost, and that it refunds exactly the contribution each qualifying household is charged;
  - the re-solved household rate;
  - the loser counts before and after, including the over-5% correction: on 2029 incomes the merged count is 16.1 million, on FY2040 incomes 11.7 million;
  - the worked examples;
  - the employer split's identity;
  - that the year path's sources add to the gross cost.

**What it found, and what was done:**

| Finding | Size | Done |
| --- | --- | --- |
| The low-pay-line alternative's rate was rescaled twice (27.5%) | The rate is 22.8%, not 27.5%; the counts are unaffected | Fixed in `line_variant()` and 4.3 |
| About 17% of the credit went to households with a Medicare enrollee, who already gain when Medicare's premiums end | About $25B | The test now leaves out Medicare: −$22B, 0.1 point, and about 0.6 million more households that lose a little |
| The no-offer share counted only earners with pay in the band; KFF's 8% is of all workers | 5.0% of band pay against 4.5% | Fixed: all earners |
| FY2035's phase-in had no three-quarter-year factor, though the credit did | About $11B in FY2035 | Fixed |
| The credit's end date was off by one between parts | — | Aligned: in full through 2044, a fifth less each year, none from 2049 |
| The pass-through rule's three years should start at the 2035 endpoint, not when each wave moves | — | Fixed |
| The employer split nets premiums against contributions by household, not by employer | — | Labelled as a proxy (2.6, rule 4) |
| "The other 8% are lower paid" isn't in KFF's evidence | — | Stated as the model's assumption (2.6) |
| The quotation of Warren's union provision isn't in EV-CAR-726's registered anchor | — | Quoted from SRC-3356, re-read at the source November 15; adding it to the entry's anchor is left for the evidence registry |
| "Burman showed"; the evidence says he argued | — | Fixed |
| The no-low-pay-line variant keeps a credit sized on the band, so it overstates the line's protection with the fix in place | Small | Noted in 4.3 |
| The examples use the statutory rate on actual pay, while the fifth tables spread the aggregate, which is about a quarter lower per dollar of CPS pay (the payroll point, below) | About a third in an example's credit and employer row | Noted in 4.2; to settle in the booking PR |

**After the cross-check,** at Espen's direction, the household base became taxable income, and the household figures moved to 2026 dollars. The design's lines were set in 2026 dollars, which moves the employer rate from 19.5% to 19.3%. All the figures in this memo are from the run after these changes. A second fresh agent then re-derived the taxable-income yield and the rate (10.613%), the 2026-dollar fifth tables, every worked example and part 10's gap, and confirmed them. It found the household base's ratio is taken on 2029 incomes (on FY2040's real incomes it would put the rate about 0.05 point higher, at about 10.66%), two example assumptions (below, in 4.2) and some wording, all fixed.

**The top three remaining risks to accuracy:**
1. the payroll point;
2. the use of CBO's growth in net federal health subsidies, about 5.7% a year after 2036, as the plan's growth path;
3. the household model's coverage averages (part 4.3).

## Part 9. Questions for Espen

*Questions 1, 2, 12 and 17 are superseded by `health-cost-review.md`, part 4.*

Each question is decided on its own; none is adopted by silence.

1. **The package:** A (recommended), B, C or D?
2. **"Mid single digits":** did you mean the household rate, or what a typical household pays of its income? **Recommendation: judge it by what households pay.** Under A the second fifth pays about 5.6% of its AGI and the middle fifth about 7.6%, and workers' health payroll contribution is 1.45%. A 5-6% rate on taxable income needs about $1T a year from a VAT or a larger employer contribution, and costs the bottom three fifths more.
3. **The employer contribution's size:** what employers as a whole would otherwise have spent on premiums (recommended), or less (65%, as in the first draft)?
4. **The employer contribution's base:**
   - pay between a $20,000 low-pay line and the wage base, 19.3% (recommended);
   - pay up to the wage base with no line, about 14.3%;
   - all pay, about 11.9%.
5. **The household contribution's base (your suggestion):**
   - **a. Taxable income,** "10.6% of the taxable income on your tax return," with no separate line (**recommended**).
   - **b. Or AGI above $20,500/$41,000,** as merged: 11.2%. It protects a little more (1.7 million fewer bottom-four households losing cash) for a slightly harder-to-explain base.
   - **c. Itemized deductions and the 20% business-income deduction should not count** (**recommended**). Count only the standard deduction, so the base is AGI less the standard deduction for everyone. Counting them would shrink the base mostly at the top, and the model can't price that because the household data don't show them. The fix is one line on the return: "AGI minus your standard deduction," even for people who itemize.
6. **The employer contribution, mandatory and pay-protected (part 2.6).** Each rule can be decided on its own; all five are recommended:
   - **a. Mandatory for every employer,** paid with payroll taxes on Form 941 and by the self-employed through SECA, with no small-firm exemption.
   - **b. The phase-in** for employers that reported no coverage for 2028: a tenth of the rate in 2035, rising a tenth a year, full in 2044. It costs $28B in FY2040 and nothing from 2045. The alternative is no phase-in.
   - **c. No cuts in pay rates** through 2044 for workers employed when their employer's contribution began, enforced by the Labor Department.
   - **d. Savings into pay:** for three years from 2035, employers that save must pass the per-worker difference into the pay of the workers they covered.
   - **e. Union contracts:** savings go to members in whatever form they bargain, with a reopener within 12 months. No lower rate for union employers; whether to encourage organizing goes to the work flagship.
7. **The fix for households that lose cash (parts 2.7 and 4.3):**
   - **a. The worker transition credit as designed** (**recommended**): the contribution on the pay of people who had earnings in 2028 and no job coverage, plan of their own or Medicare that year, in full, phased out between $60,000 and $120,000 ($120,000 and $240,000 for couples). It costs $123B in FY2040 (0.6 point). With the phase-in, it cuts bottom-four households losing more than 5% of income from 12.4 million to 6.2 million.
   - The alternatives, priced in 4.3: the credit at 75% (0.15 point cheaper, less protection); a credit for every worker (3.4 points more, no better on the over-5% count); the low-pay line at $30,000 instead (cheaper, about a third of the protection); or no credit.
   - **b. How long:** transitional, in full through 2044 and none from 2049 (**recommended**), or a permanent credit for all low-paid workers? The permanent one costs more ($169B) and protects fewer of the households that lose.
8. **The 2.9% payroll contribution:**
   - keep it as the plan's own contribution on all pay (recommended);
   - fold it into the employer contribution, so workers pay no payroll tax for health. This costs about $108B of other tax, and the fourth fifth turns slightly negative.
9. **The household contribution in the transition:** steps that follow the waves (about 3% from 2031, 5% from 2033, 9% at the endpoint), with no credit for premiums still paid (recommended)? The alternatives:
   - a credit for premiums still paid: fairer, but FY2031-34 revenue falls by roughly $0.9T, and the early rate about doubles for everyone else;
   - a start in 2035, borrowing about $2.6T over FY2030-34.
10. **The states at 100%** of their former Medicaid spending for the people who move, indexed (recommended), or 80%, 50% (booked) or 0%?
11. **The self-employed** pay the employer contribution on net earnings, in the same band, as SECA does (recommended)? At booking, deduct that contribution from their income base, as an employee's comes out of pay before tax. The worked example doesn't yet deduct it, so it slightly overstates their household contribution.
12. **D1, administration:** book 4%, with a 3% target (recommended)?
13. **D2, a national health budget:** hold growth to GDP plus 1 point from 2037 (recommended)?
14. **D3 and D4:** keep the 1.15 payment rate and the small copays (recommended)?
15. **The Medicare seam:** rebook HLT-7 on CBO's Medicare figure in the booking PR: −$0.30T in FY2040, −$1.28T over FY2030-39 (recommended)?
16. **Counting and the fund:** count health's contributions outside D3's revenue-mix test, as replacements for premiums, and pay them into the plan's fund, with the general fund covering any shortfall (recommended)? The credit would be paid from the same fund, as a refund of the contribution.
17. **The physician rate correction (part 1.2b):** at booking, price physician and other non-hospital claims at Medicare's fee schedule plus the add-ons, as the decided design says, instead of the hospital target: about −$0.28T in FY2040 and about 1.4 points off the household rate (recommended)?

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
- **The plan-wide gap after the recommended health package** (case `mixed`, nominal $B; project arithmetic: the booked plan-wide gap less health's booked need, year by year, because package A, with its phase-in and credit, covers health's own need in every year):

  | | FY2040 | FY2030-39 |
  | --- | --- | --- |
  | Checkpoint part C (old part B's package) | about 70 | about 1,890 |
  | **Recomputed on package A** | **70** | **1,885** |
  | … with the FY2030 restoration on the general fund, as part 2.3 recommends | 70 | 1,935 |

  - **Why it barely moves:** both packages cover health's need in full, so what remains is the rest of the plan. The phase-in and the credit are paid inside the household rate, year by year, not left to the gap.
  - **The decade figure** runs at roughly $0.13T to $0.26T a year from FY2031. It matters for the debt guardrail, not the FY2040 test.
  - **With the seam rebooked,** health's own FY2040 net cost is $3,794B, so the plan-wide FY2040 gap before health's financing would be about $3.86T.
  - **Checkpoint part C's stage G items:** none of the dossiers' items change. On the menu:
    - item 3 (start the household contribution with wave 1 in 2031) is now part of the recommended path (part 2.3);
    - item 4 (the administration and drug savings) is now design memos D1 and D2;
    - item 1 (one more point above $100,000/$200,000) would now stack on a top rate of about 73.6%, so on the stacking check it would raise less than its $67B.
- **A booking PR (tier 3), after Espen answers,** would:
  - rebase HLT-7 on CBO's Medicare figure;
  - price physician and other non-hospital claims at the decided rate (part 1.2b), with the coverage model's own single-payer run;
  - book the employer contribution's row, net of the tax it displaces;
  - book the states' share (HLT-7.17);
  - book the household contribution's rows and path, and `scenarios.json`;
  - book the phase-in (a lower employer row through FY2044) and the worker transition credit (an outlay row, FY2035-49), as Espen decides them;
  - price the transition choices;
  - settle the payroll point;
  - book any design memo Espen adopts.

## Method and sources

- **Code:** `models/tools/health_financing.py`: `coverage`, `seam`, `physician_rate`, `need_path`, `replaced_path`, `system_view`, `payers`, `payer_path`, `flow_path`, `package`, `package_path`, `micro`, `stacking_check`, `design_levers`, `growth_hold`, `examples`; for the fix and the employer protections, `no_offer`, `phase_left`, `credit_key`, `line_variant`, `employer_split`, `pay_holds_check`, `savings_kept_check`. Tests: `models/bookings/test_health_financing.py`.
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
  - Anand on pass-through [EV-CAR-299]; Baicker and Chandra on premiums and wages [EV-CAR-296];
  - KFF's 2026 offer rates [EV-CAR-295];
  - Vermont [EV-CAR-244, EV-CAR-245];
  - the bills and the options paper [EV-CAR-272 to EV-CAR-292, EV-CAR-713 to EV-CAR-716];
  - Warren's plan and its reviews [EV-CAR-723 to EV-CAR-744]; Warren's union provision re-read at its source (SRC-3356, through an Exa fetch, November 15);
  - Urban's 2019 comparison of reforms [SRC-3223], read November 15 for its single-payer variants, sensitivities and pass-back discussion. It models no financing. Its copyright page permits reproduction with attribution, but the library saves only government works and Creative Commons texts, so it stays a citation row.
- **Legacy work,** weighed as evidence, not as defaults (`DEC-2026-11-13-15`):
  - `legacy/domains/domain-revenue.md`;
  - `legacy/sources/revenue-channels-and-full-menu.md`;
  - `legacy/sources/revenue-counted-reconciliation.md`;
  - `legacy/domains/domain-health.md`.
- **The handover notes** (`notes/health-financing-findings-2026-11-15.md`):
  - confirmed: the corrected method, the avoidance evidence, the seam's size, and HX covering both shares;
  - corrected: the top rate (SS-1 left out), HX's alignment with the booking, and federal coverage in the employer money.
