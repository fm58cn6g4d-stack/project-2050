# Memo G2: The 2 points on income above $20,000/$40,000

**Decided:** C, and G2b both ways, judged with everything counted, `DEC-2026-11-20-06`. Booked in stage G step 7 (`../2-settlement.md`, `models/data/inputs/settlement.json`). The memo below is the record of the choice as put to Espen; its figures are the draft's.


Role: decision memo for Espen, fork 2 of stage G's batch ([`README.md`](README.md); [`../2-settlement.md`](../2-settlement.md) parts 2 and 3; `../1-audit.md` part C, item 7). Status: **provisional, drafted on the recommendation, November 20, 2026; the recommendation changed after the milestone review (#470, B-3), from A to C.** Not decided, not booked. Nominal $B on case `mixed`, priced by `models/tools/financing-protection/packages.py`. The take-home figures are from `take_home_vat.py` (FY2040) on `health_cost_review.py`'s test. Project arithmetic on exploratory models, not official scores.

## The question

The plan books an income contribution of 2 points on AGI above $20,000 single and $40,000 joint. It starts in 2035 and reaches the full 2 points in 2044. It raises **$216.3B in FY2040 and $636.8B in FY2056.**

When you set the health contribution at 2.25% (`DEC-2026-11-15-11`), the 88.7% of workers coming out ahead on the take-home test held "only if stage G drops or folds in the booked 2 points". With them, **70.1%** come out ahead, against your target of 85-90%.

The money the 2 points raise has to come from somewhere. Whatever this memo doesn't raise, memo G3's VAT does. **So each option is shown with the VAT it needs, and the take-home test is shown two ways:** health costs only (the test as decided) and with the VAT counted too.

## The options

| | What | VAT needed, FY2040 → FY2051 | Workers ahead: health costs only | **Workers ahead: VAT counted** | Below 200% of poverty, VAT counted | Retirees on Social Security or SSI, VAT counted |
| --- | --- | --- | --- | --- | --- | --- |
| A | Drop the 2 points | 5.4% → 7.3% | **88.7%** | 55.6% | 79.7% | 97.1% |
| B | Keep them as booked | 3.05% → 3.3% | 70.1% | 53.0% | 89.1% | 97.8% |
| **C (recommended)** | **Fold them into the health contribution:** drop them, and raise its base rate from 2.25% to 3.25% from 2035 (reopens `DEC-2026-11-15-11`) | **2.95% → 4.6%** | 76.2% | **57.8%** | **90.4%** | **97.9%** |
| D | Drop them and raise the base rate to 2.5% (reopens `DEC-2026-11-15-11`) | 4.8% → 6.6% | 85.9% | 56.0% | 82.1% | 97.3% |

The retirees' column is on reading (a): prices rise with the VAT, and so do Social Security and SSI (`../2-settlement.md` part 3). Retirees on private pensions and savings do worse under every option: 79-86% ahead.

**A, drop the 2 points** (the first draft's recommendation).
- *Health costs only:* 88.7% of workers ahead, the middle of your range.
- *With the VAT counted:* 55.6%, and only 79.7% of workers below 200% of poverty. Two VAT points cost a bottom-fifth household about $740 a year in FY2040, against about $30 for the 2 points. A VAT has no exemption for low incomes.
- *VAT:* the largest, 5.4% stepping to 7.3%.
- *Revenue-mix test:* 57% over the decade, 50% in FY2040 and 46% in FY2056 (memo G3).

**B, keep them.** It is the worst on both readings: 70.1% on health costs, and 53.0% with the VAT. The 2 points have no exemption below 250% of poverty, so they reach workers the health contribution spares.

**C, fold them into the health contribution (recommended).**
- *How:* the 2 points end. The health contribution's base rate rises by a point, to 3.25%, from 2035, with its exemption as decided: nothing below 138% of poverty, and one steady rate up to 250%.
- *Money:* about the same as the 2 points in FY2040. From FY2044, when the 2 points would have reached their full rate, it raises less, and memo G8's VAT steps take up the difference.
- *Health costs only:* 76.2% of workers ahead, below your target.
- *With the VAT counted:* the best of the four for every group. 57.8% of workers, 90.4% below 200% of poverty, 64.3% between 250% and 400%, and 97.9% of retirees on Social Security or SSI.
- *D3:* the best for the bottom three fifths (Q1 +$14,308, against +$13,917 under A).
- *Revenue-mix test:* 61% over the decade, 54% in FY2040 and 50% in FY2056.
- *Visibility:* "a 3.25% health contribution", in place of 2.25%.
- *It reopens a decision:* you set the base rate at 2.25% (`DEC-2026-11-15-11`), and C raises it to 3.25%. That decision anticipated this: its 88.7% "holds only if stage G drops or folds in the booked 2 points". But choosing C means setting the rate again.

**D, drop them and set the base rate at 2.5%.**
- *Health costs only:* 85.9%, just inside your range. You chose 2.25% partly for the margin: at 2.5%, "one uncertain assumption" could put the result under 85% (`health-household-contribution.md`).
- *With the VAT counted:* 56.0%. It reopens `DEC-2026-11-15-11`.

**How firm the comparison is.** The VAT-counted figures allocate each household's VAT by its fifth's average, on D3's consumption key, not by its own spending (`../2-settlement.md` part 3). So the small gap between C and A for all workers (57.8% against 55.6%) is within what that rough allocation could move. The large gaps are robust, because they come from the health contribution's exemption, which a VAT doesn't have: workers below 200% of poverty (90.4% against 79.7%), and retirees on private pensions and savings (85.7% against 79.3%).

## Recommendation

**C, fold the 2 points into the health contribution at 3.25%.**
- Your test asks whether households pay less in "money that they perceive to come out of their pocket" (`DEC-2026-11-15-02`). A VAT comes out of the same pockets at the till.
- Once the VAT is counted, C protects low-income workers and retirees on private income far better than A (the robust gaps above), and halves the VAT. On all workers the two are close.
- It doesn't meet your 85% on the health-only test, and nothing that pays for the plan meets 85% once everything is counted.

**What would change this:**
- **If the decided test, health costs only, is what you want the plan judged on, then A.** It is the only option that keeps 85-90% with a margin. Its cost is a VAT nearly twice as large, which falls hardest on the households the test is meant to protect.
- If you would rather not have a VAT at all, memo G3's option E carries the rest on the health contribution instead: about 4.45% in FY2040, and rising.

## Question for you

**G2.** Fold the booked 2 points into the health contribution, raising its base rate to 3.25% from 2035, which reopens `DEC-2026-11-15-11` (C, recommended)? Or drop them and pay with a larger VAT (A), keep them (B), or drop them and set the contribution at 2.5% (D)? And which take-home reading should the plan be judged on: health costs only, as decided, or with the VAT counted?
