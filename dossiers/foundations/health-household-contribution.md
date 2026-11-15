# The household health contribution: the unified design, priced across rates

Role: the stage E memo that rebuilds the household contribution Espen chose on November 15 and prices it across a range of rates, so Espen can pick the final rate on reviewed numbers. It replaces package E's household tier ("4% of AGI above $100K/$200K") in `health-cost-review.md` (parts 2.3 and 4) and the lead's exploratory variants (`notes/variants-2026-11-15/README.md`, which priced X3 by monkeypatching). Everything else in package E stands as Espen approved it.

Status: **for Espen's choice of rate, November 15, 2026.** It books nothing and changes no adopted input. Code: `models/tools/health_cost_review.py`, part 3 (`python3 models/tools/health_cost_review.py --part3 --md`). Tests: `models/tools/test_health_cost_review.py`, class `Unified`.

Units are as in `health-cost-review.md`: households in 2026 dollars, budget totals in FY2040 nominal $B (case `mixed`), and "today" means today's law grown to FY2040.

## In plain terms

- **Espen asked:** one health contribution in place of the worker's Medicare tax, with 85-90% of workers (or more) coming out ahead.
- **What meets that:** a base rate of **2.5% or less**, with the surcharge at about 6 points (5, plus about 1 to keep H1b's booked revenue). At 2.5%, 86% of workers come out ahead. At 2.25%, 89% do, and at 2.0%, 91%.
- **What it costs the rest of the plan:** a lower rate means health takes more of the revenue already booked for the other flagships. The plan-wide FY2040 gap is **$527B at 2.5%**, **$583B at 2.25%** and **$638B at 2.0%**. Package E as approved left $649B.
- **Recommendation: 2.25%, with a 5-point surcharge, and the exemption phased in at one steady rate up to 250% of poverty.** That puts 88.7% of workers ahead, the middle of Espen's range, with a margin for the model's uncertainty. It costs $56B a year more than 2.5%. At 2.5% the result (85.9%) sits less than a point above the 85% floor, so one uncertain assumption could tip it under.
- **Almost every retiree and non-worker comes out ahead (about 98.5-98.6%),** because the plan ends Medicare premiums and medical bills. The few who don't have high incomes.
- **Two things to fix before booking:**
  - The 2 points already booked on income above $20K/$40K for the other flagships would pull the result down to about 70% at 2.25%. Stage G should drop that charge or fold it into this one.
  - H1b's wage half ($43.5B) has to be restated, because folding Medicare's worker tax in takes away its base. Every figure here folds it into the surcharge (section 7).

## 1. The design as built

Espen's shape (November 15): "Shape is right and I'd really like 85-90% of workers to come out ahead (or more)".

- **One health contribution.** It replaces the worker's 1.45% Medicare tax (HI), the 0.9% Additional Medicare Tax, and the worker's HI on former premiums. Employers keep their 1.45%. It is withheld from pay for wages and paid on the return for other income.
- **A base rate R** on all AGI.
- **A surcharge S** (5 points as the starting case; priced here at 5.96, with H1b's wage half folded in, section 7) on AGI above $205,400 single and $256,750 joint. These are 2026 dollars, indexed as `LINE_HIGH` is.
- **A low-income exemption:** nothing at or below 138% of poverty for the tax unit's size, rising to the full rate at 200%, with no cliff.
- **Everything else is package E:** cost case "design" (D1, D2, D5 at 25%), the five new streams, the small-employer allowance, the worker transition credit, and health's first call on booked revenue. Booked revenue closes whatever the contribution leaves.

**How it is built** (`unified_package`):
- It starts from package F, which has no household contribution: what's left is the remainder booked revenue would have to close.
- It adds what the fold-in stops collecting (section 6, including H1b's wage half) and subtracts the contribution's yield, so a surcharge that wins H1b back must be priced in, not assumed. Booked revenue taken = F's remainder + the fold-in's lost revenue − the contribution's yield.
- The yield is package E's budget-model yield per point, scaled by the household model's base, with the 20% avoidance allowance placed in the top fifth. This is the variants' method.
- The contribution gets its own quintile key, and nothing in the models is swapped or patched.
- The rebuild reproduces the lead's X3 exactly on X3's own conventions ($308.1B taken with H1b kept whole, 78.7% of workers ahead, 98.6% below 200% of poverty, test household T at $3,514). The test `test_reproduces_x3` checks this.
- The figures below differ from X3 in three ways: the better-supported worker HI figure (section 6, +$36.6B taken at every rate); Medicare Part B's premium counted in today's cost (about +0.6 points on the pass rate); and the surcharge at 5.96 rather than 5 (about −0.4 points on the pass rate, the same booked revenue).

**The take-home test** (`take_home_micro`) now counts the worker's HI and the 0.9% in today's visible cost. It counts them in the plan's cost too, unless the contribution replaces them. So package E's result is unchanged by this, and the unified design is compared like with like. Medicare Part B's standard premium ($202.90 a month in 2026, grown as other premiums) is added to today's cost for Medicare enrollees. That is a working assumption: the CPS's premiums leave Part B out.

## 2. The rate table (FY2040; S = 5.96, H1b folded in, unless shown)

✓ marks a rate that meets Espen's target of 85% or more of workers ahead.

| R | Workers ahead | Workers below 200% of poverty ahead | Retirees and non-workers ahead | Workers ahead with the booked 2 points | Bottom-four households losing cash (M) | T: today → plan | Booked revenue taken ($B) | Plan-wide FY2040 gap ($B) | Top rate on wages |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Package E (for reference: 4 points above $100K/$200K, HI kept) | 90.8% | 100.0% | 99.4% | 77.3% | 1.6 | 6,692 → 2,385 | 579 | 649 | 67.0% |
| 2.00% ✓ | 90.9% | 100.0% | 98.7% | 72.9% | 2.0 | 6,692 → 2,786 | 568 | 638 | 67.4% |
| 2.25% ✓ | 88.4% | 100.0% | 98.6% | 69.7% | 2.4 | 6,692 → 2,968 | 513 | 583 | 67.7% |
| 2.50% ✓ | 85.6% | 99.7% | 98.5% | 66.8% | 3.0 | 6,692 → 3,150 | 457 | 527 | 67.9% |
| 2.75% | 82.3% | 99.6% | 98.4% | 63.5% | 3.5 | 6,692 → 3,332 | 401 | 471 | 68.2% |
| 3.00% | 78.9% | 98.6% | 98.2% | 60.8% | 4.0 | 6,692 → 3,514 | 345 | 415 | 68.4% |
| 3.25% | 75.6% | 98.3% | 97.9% | 58.4% | 4.5 | 6,692 → 3,696 | 289 | 359 | 68.7% |
| 3.50% | 72.5% | 98.0% | 97.8% | 56.0% | 5.2 | 6,692 → 3,878 | 233 | 303 | 68.9% |
| 2.25% with S = 4.96 (4, plus H1b) ✓ | 88.9% | 100.0% | — | 69.9% | 2.4 | 6,692 → 2,968 | 558 | 628 | 66.7% |
| 2.50% with S = 4.96 ✓ | 86.1% | 99.7% | — | 67.0% | 3.0 | 6,692 → 3,150 | 502 | 572 | 66.9% |
| **Recommended: 2.25%, steady-rate exemption to 250%** ✓ | **88.7%** | 100.0% | 98.6% | 70.1% | 2.4 | 6,692 → 2,968 | **516** | **586** | 67.7% |
| 2.5%, steady-rate exemption to 250% ✓ | 85.9% | 100.0% | 98.5% | 67.2% | 2.9 | 6,692 → 3,150 | 460 | 530 | 67.9% |

If H1b's wage half were not restated (S = 5), the contribution would raise $43.5B less: at 2.5%, $500B taken instead of $457B.

**Reading the table:**
- **The range that meets 85-90%+ is R = 2.0% to 2.5%.** The gap runs from $638B at 2.0% to $527B at 2.5%. At 2.5% the margin over 85% is under a point.
- **Each quarter-point of R** moves about 3.3 points of workers and about $56B of booked revenue.
- **One point less of S** adds about half a point of workers and costs about $45B. It is a poor trade: the surcharge falls almost entirely on households who would not pass the test anyway.
- **Who passes, by coverage, at 2.25% as recommended:**
  - workers with job coverage today: 86.9%;
  - workers on Medicaid: 83.2% (80.3% with the drafted exemption);
  - uninsured workers: 96.3%;
  - workers with their own plan: 97.8%.
- **Who passes, by income, at 2.5%:**
  - below $100K of AGI: 95-100%;
  - $100K-$200K: about 87-88%;
  - above $200K: 50%, where the surcharge bites.
- **The top federal rate on wages** (statutory, both halves) is 67.7% at 2.25% with H1b folded into S (section 7), against package E's 67.0% and 63.0% before health.

## 3. Per-household figures, like for like

Package E's $1,371 for test household T (a single worker at $72,000 with job coverage) left out the $1,014 of Medicare tax T still pays under E. This memo counts HI on both sides:

| Test household T (2026 dollars a year) | Today, grown to FY2040 | Plan |
| --- | --- | --- |
| Package E (HI kept) | 6,692 (5,679 + 1,014 HI) | 2,385 (1,371 + 1,014 HI) |
| Unified at 2.25% | 6,692 | 2,968: a contribution of $1,639, copays of $498, and $830 of tax on the pay that used to go to premiums |
| Unified at 2.5% | 6,692 | 3,150 |

Net per household by fifth, FY2040, in 2026 dollars (everything health changes, including employer premiums becoming pay, which is why these are larger than the visible-cost test):

| | Q1 | Q2 | Q3 | Q4 | Q5 | Top 1% |
| --- | --- | --- | --- | --- | --- | --- |
| Package E | +4,819 | +9,453 | +12,949 | +12,947 | −7,069 | −212,130 |
| Unified at 2.25% (recommended) | +4,903 | +9,199 | +12,074 | +11,665 | −6,261 | −234,211 |
| Unified at 2.5% (steady rate to 250%) | +4,896 | +9,107 | +11,845 | +11,271 | −6,872 | −237,446 |

(`health-cost-review.md`'s per-fifth nets were in FY2040 nominal dollars, about 1.377 times these.)

## 4. Retirees and non-workers on the all-AGI base

The 78.7% figure in the variants counted only workers. The same test run on everyone else: 69.1 million tax units, half of them on Medicare, a fifth on Medicaid.
- **About 98.5% come out ahead** at any rate in the range: 98.6% at 2.25% and 98.5% at 2.5%. On Medicare: about 98.7%. Below 200% of poverty: 100%.
- **Why:** the plan ends Medicare's premiums and most medical bills, which cost a retiree far more than a contribution of 2-2.5% of AGI. AGI counts only part of Social Security.
- **Who doesn't come out ahead:** almost all of them have AGI above $200,000, where the pass rate is about 67-69%.
- **The one assumption that matters here:** if the CPS's premiums already include Part B, the pass rate falls to about 96.3% at 2.5%. It still comfortably passes.

## 5. The exemption's marginal rate, and how to deliver it

**The marginal rate.** In its band, the drafted phase-in (charge = R × AGI × the share of the way from 138% to 200%) adds R × (2x − 1.38) / 0.62 points for each extra dollar, where x is income as a multiple of poverty.
- **At R = 3%** that is 6.7% at the bottom of the band, rising to 12.7% at the top.
- **At R = 2.5%** it is 5.6% rising to 10.6%; at 2.25%, 5.0% rising to 9.5%.
- **It stacks on the EITC.** A single parent of two children between 138% and 200% of poverty (about $36,800 to $53,300 for a family of three) is also in the EITC's 21% phase-out, plus 6.2% Social Security tax and 10-12% income tax. The drafted exemption takes that parent's combined rate to roughly 45-50%, before SNAP.

**Gentler designs, priced at R = 2.5% (S = 5.96):**

| Exemption | Workers ahead | Below 200% of poverty | Exemption's cost ($B) | Its own marginal rate (points) | Booked revenue taken ($B) | Gap ($B) |
| --- | --- | --- | --- | --- | --- | --- |
| 138% to 200%, as drafted | 85.6% | 99.7% | 15.8 | 5.6 rising to 10.6 | 457 | 527 |
| 138% to 250% | 86.1% | 100.0% | 22.0 | 3.1 rising to 8.1 | 463 | 533 |
| 138% to 300% | 86.5% | 100.0% | 28.9 | 2.1 rising to 7.1 | 470 | 540 |
| One steady rate, 138% to 200% | 85.6% | 99.7% | 15.0 | 8.1 throughout | 456 | 526 |
| **One steady rate, 138% to 250%** | 85.9% | 100.0% | 19.4 | **5.6 throughout** | 460 | 530 |

"One steady rate" charges a fixed share of each dollar above 138% of poverty until the charge reaches R × AGI, which happens exactly at the top of the band. There is still no cliff.

**Recommended: one steady rate to 250%.** It halves the worst marginal rate (10.6 down to 5.6 points at R = 2.5%, and 5.0 at 2.25%) for about $4B a year. A single rate is also easier to explain and to build into withholding tables than a curve. Phasing in to 300% buys little more for $13B.

**Delivery, against "guide, don't police" (`DEC-2026-11-09-13`).** The draft has workers claim the exemption on the W-4 and reconcile at year end, like the premium tax credit. That has real costs:
- a new claim each worker must know to make;
- household size and income estimated in advance;
- repayments at tax time when income turns out higher.

These fall hardest on low-wage workers with changing hours, and the premium tax credit's own reconciliation is a known source of surprise bills.

**The simplest delivery needs no claim:**
1. Build the exemption into the employer withholding tables, as the standard deduction already is. Withholding starts above 138% of poverty for one person, annualized per pay period, at the steady rate.
2. Use the W-4's existing dependents step for larger households. No new form or field is needed.
3. Settle on the ordinary return, where income and household size are already known.

Under-withholding is small by design, since the band rate is at most about 5.6 points. Anyone who doesn't file and is below the filing threshold owes nothing.

## 6. Reconciling the lost revenue

**Worker HI: $326B, not $290B or $343B.** FY2040, nominal.
- **$290B** is half of `health_financing.py`'s 2.9% on the budget model's payroll point: $135B a point in 2030, growing 4% a year (`assumptions.json`, the education fund's figure).
- **$343B** is the household model's earnings, grown with GDP per household.
- **$326B** comes from CBO's own payroll, the better-supported measure. CBO's 2026 long-term projections (SRC-3813, table 2) give Social Security taxable payroll of $18.19T in 2039 and $18.85T in 2040: $18.68T for FY2040. HI taxes all covered earnings, of which taxable payroll is about 83% (`CAP_SHARE`). That gives $22.5T, and 1.45% of it is $326B.

The budget model's $135B a point for 2030 is within 3% of CBO's *capped* taxable payroll for that year ($13.16T, so $131.6B a point), so it looks like a capped figure that `health_financing.py` reads as all pay. On all covered earnings the point would be about $158B. So the $290B figure is about 11% low as a measure of HI. Items priced on a capped base would be slightly overstated, not understated, and items on all pay understated: a stage G check, not this memo's. The household model's $343B grows earnings with GDP, a bit faster than CBO grows payroll. **This memo uses $326B,** which adds $36.6B of booked revenue taken at every rate against the variants. The tool keeps all three bases (`worker_hi_bn`). At 2.5%, $290B would mean $420B taken and $343B would mean $473B.

**The 0.9% Additional Medicare Tax: $53.5B, a working figure, probably low.**
- **Basis:** the household model's earnings above $200,000/$250,000, which are not indexed, grown with GDP per household.
- **Why probably low:** the CPS top-codes high earnings. The top 1% has about 9% of wages in the CPS against 12% on the legacy key. Scaling for that puts it nearer $70B.
- **If it is higher,** booked revenue taken rises by the same amount.

**Worker HI on former pre-tax premiums: $16.1B** (1.45% of HX's kept base). With H1b's wage half ($43.5B, section 7) the fold-in stops collecting **$439B**, and the surcharge's extra 0.96 points win the H1b part back.

## 7. H1b restated

H1b, the booked rise in Medicare and investment-income tax to 5% above $400K, raises $62.7B on the audit lines.
- **About 69% of it is the wage half,** taking wages above $400K over AGI above $400K on the household model: **$43.5B**.
- That half rests on the worker's HI and the 0.9%, which the fold-in repeals, so it loses its base. The investment half stays as a 5% investment-income tax.
- The tool counts the wage half as lost revenue, and section 2's table wins it back by folding it into S. The two ways to restate it, with the same 20% avoidance allowance:

| | Points needed | The top federal rate on wages at R = 2.25% (S = 5) |
| --- | --- | --- |
| Its own step: points on AGI above $400K within the contribution | 1.8 | 68.5% |
| Folded into S: the surcharge rises from 5 to about 6 points | 1.0 | 67.7% |

**Recommended: fold it into S** (6 points above $205,400/$256,750). It is one fewer step, it has a lower top rate, and it raises the same money.
- The own step needs more than H1b's 1.2 points because it applies to all AGI above $400K after the avoidance allowance.
- The plan's top rate before health was 63.0%, and package E's 67.0%.

**Sensitivity to the 20% avoidance allowance:**

| Allowance | H1b's own yield ($B) | Its wage half ($B) | Own step (points) | Into S (points) | Booked revenue taken at R = 2.5% ($B) |
| --- | --- | --- | --- | --- | --- |
| 10% | 70.6 | 48.9 | 1.6 | 0.85 | 353 |
| 20% (central) | 62.7 | 43.5 | 1.8 | 0.96 | 457 |
| 30% | 54.9 | 38.0 | 2.1 | 1.10 | 560 |
| 40% | 47.0 | 32.6 | 2.4 | 1.28 | 664 |

The last column holds S at 5.96. The allowance matters more for the contribution itself than for H1b: each 10 points moves booked revenue taken by about $104B. The project's 20% was set for high-income tiers. On a broad base withheld from wages, avoidance is likely smaller, so the gap here may be overstated. Stage G should set the allowance by tier.

## 8. The booked 2 points (an item for stage G)

The other flagships' booked charge of 2 points on AGI above $20K/$40K is not part of health. It is on top of the plan, so it is shown separately.
- **Adding it to the take-home test cuts the share of workers ahead by about 19 points:** 88.7% to 70.1% at 2.25% as recommended, and 85.9% to 67.2% at 2.5%. Package E falls from 90.8% to 77.3%.
- **No rate in this range meets 85% with it in place.**
- **For stage G:** drop that charge or fold it into the unified contribution. Folded in, its revenue would come from the same base the health contribution already taxes.

## 9. Recommendation for Espen

**R = 2.25%, S = 5.96 (Espen's 5, plus 0.96 to fold in H1b's wage half), and the exemption phased in at one steady rate from 138% to 250% of poverty, with no W-4 claim.**
- It puts 88.7% of workers ahead (100% below 200% of poverty) and about 98.6% of retirees and non-workers.
- It takes about $516B of booked revenue and leaves a plan-wide FY2040 gap of about $586B. That is about $63B less than package E as approved, and it gives package E's results with one contribution in place of two.

**If Espen prefers a smaller gap:** 2.5% still meets the floor (85.9%) and saves about $56B a year. But it leaves under a point of margin: the Part B assumption alone moves the result by about half a point.

**If Espen wants "or more":** 2.0% reaches about 91% and costs about $55B a year more than 2.25%.

## Method and caveats

- **Same method as the variants:** FY2040, package E's cost case and streams, the 20% avoidance allowance all in the top fifth, and the top 1%'s share scaled from the legacy key's 55% (a judgement call).
- **The exemption and lines** are applied to the 2029 tax units' AGI grown to FY2040 in 2026 dollars. Poverty is the tax unit's size on the 2025 guidelines, as `fpl200()`.
- **Employer premiums that become pay** aren't added to the contribution's base. In total they are roughly offset by the employer contribution that replaces them; household by household this is a small understatement of the contribution.
- **The bottom-four loser counts** differ slightly from the variants' (4.0M against 4.5M at 3%), because the contribution's key is now built on FY2040 incomes rather than 2029 ones.
- **Not an official score:** this is project arithmetic on the project's own models.
