# Memo F1: How households pay in place of premiums

Role: decision memo for Espen, fork 1 of the financing checkpoint's health batch (`README.md`; `../checkpoint-financing.md`, part B). Status: **for decision, November 14, 2026**. Figures are FY2040, from `models/tools/health_financing.py` (project arithmetic, not an official score), with memo F2 at A and memo F3 at B.

## The question

When the plan is complete, households stop paying about **$2.37 trillion** a year in premiums and out-of-pocket costs (FY2040). After the employer contribution (F2) and the states' share (F3), about **$2.83 trillion** of the plan's cost is left for households to carry in some other form. The question is which form. The design rejected income-checked public premiums (care memo 3, C) because every premium needs enrollment-linked income checks. Each option here is a tax collected through existing systems, with no link between paying and being covered.

## The options

**A. An income-based health contribution (recommended).** A rate on income above $20,000 single or $40,000 joint (the budget model's broad tier, price-indexed), collected with the income tax: withholding for wages and estimated payments for other income. It reaches about **15.7%** in FY2040 and phases in with the waves (part B4, point 3).
- *Gap:* −$2,827B in FY2040, closing health with F2 and F3.
- *Households (D3), net a year:* Q1 **+$6,712**, Q2 **+$10,703**, Q3 **+$11,077**, Q4 **+$4,921**; Q5 −$39,551; top 1% −$278,055. The middle fifth pays about 6.4% of its income and stops paying about 10.4% of it in premiums and out-of-pocket costs.
- *Administrative burden:* low. It is a rate on the existing return, with new withholding tables and no new filing, enrollment or income check. It reaches retirement and investment income as well as pay.
- *Political risk:* high visibility. "A 15.7% health contribution" is the largest single tax in the plan, although for most households it is smaller than the premiums it ends. Vermont's plan stopped when its full tax became visible [EV-CAR-245]. On top of the booked measures, the top rate on wages passes 60%, and avoidance at the top may exceed the budget model's 20% allowance.
- *Legal risk:* low (Congress's taxing power).

**B. A worker payroll contribution on all earnings.** About **14.1%** of wages and self-employment earnings, no cap, withheld beside Social Security and Medicare taxes.
- *Gap:* −$2,827B.
- *Households:* Q1 +$5,349, Q2 +$7,489, Q3 +$8,114, Q4 +$3,484; Q5 −$30,575; top 1% −$279,231.
- *Administrative burden:* lowest (W-2 and quarterly deposits already exist).
- *Political risk:* the rate is on work only. Retirees stop paying Medicare premiums and pay nothing in, so working families in the fourth fifth carry more. With the employer's 7.7% (F2), payroll levies rise about 22 points.
- *Legal risk:* low.

**C. Half an income contribution, half a value-added tax with a per-person rebate.** About 7.8% on income above the line, plus a broad VAT of about 13.5% that pays back a quarter of its yield as an equal amount per person.
- *Gap:* −$2,827B.
- *Households:* Q1 +$3,631, Q2 +$6,471, Q3 +$7,419, Q4 +$3,706; Q5 −$27,366; top 1% −$210,703.
- *Administrative burden:* high. A VAT is a new federal collection system beside 45 states' sales taxes, with registration for millions of businesses, and the rebate needs a payment channel.
- *Political risk:* a new kind of tax, and prices rise once.
- *Legal risk:* low.

## Recommendation

**A.** It leaves every fifth below the top better off than B or C, it reaches all income, not only pay, and it uses the return households already file. Its risk is political: the rate is large and visible. The public case should always show a family's premiums and deductibles ending beside its contribution.

**What would change this:**
- a decision that no tax may be called a health contribution, in which case B comes next;
- a stage G finding that avoidance at the top is much larger than allowed for, in which case a lower first tier with more at the top (part D, stage G question 1).

## Question for you

Which household side: A (recommended), B or C?
