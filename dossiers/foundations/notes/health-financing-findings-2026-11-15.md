# Health financing: findings for the fresh start

Role: handover note from the stopped revision of the stage E checkpoint memo (`../checkpoint-financing.md`, #378). It is written for the session that starts the single health plan's pricing and financing again. Status: **notes, November 15, 2026; not a decision and not a source of record.** Every figure is project arithmetic on the project's exploratory models, not an official score. The memo and `models/tools/health_financing.py` are unchanged on this branch. The revised code is in this branch's commit `6b32a83`, which ran and passed its tests; the next commit takes it back out so this PR changes notes, evidence and library only.

## 1. The household figures: what was wrong, and the corrected numbers

- **The error.** The memo's tables (part B3, F1 to F3) charge the income contribution as `rate × the budget model's per-point yield`. That yield already carries the budget model's 20% avoidance allowance (`models/tools/recovery-budget/assumptions.json`, `tax.additional_yield_haircut`). `per_household()` then spreads it over every household in proportion to its base. So every withheld wage earner was charged 80% of what the law would charge.
- **Income measures.** The memo's "average incomes" ($34K, $92K, $156K, $246K, $562K, top 1% $1.88M) are expanded income (`household/budget.py:123`: cash income plus the employer's payroll tax), grown to FY2040 by nominal GDP per household. The contribution's base is AGI above $20,000/$40,000. On the same growth, per household in FY2040:

| | Q1 | Q2 | Q3 | Q4 | Q5 | Top 1% |
| --- | --- | --- | --- | --- | --- | --- |
| Expanded income | 33,634 | 91,643 | 155,789 | 245,592 | 561,562 | 1,875,845 |
| AGI | 15,783 | 63,866 | 131,823 | 221,196 | 525,542 | 1,813,694 |
| AGI above the line (CPS, grown) | 2,454 | 25,568 | 78,599 | 162,784 | 465,013 | 1,754,908 |
| AGI above the line (as the budget model's yield implies it) | 2,490 | 25,939 | 79,743 | 165,123 | 471,802 | 1,778,855 |

  The base the yield implies is $22.53T in FY2040; the CPS-grown base is $22.21T (1.4% lower). Use the implied base so that rate × base = charge.
- **Corrected result for the memo's package** (F1 A, F2 A, F3 B; 15.68% on the broad base). The statutory charge is $3,533B; avoidance keeps $707B from being collected; $2,827B is collected. The middle fifth's charge is 15.68% × $79,743 = **$12,507** (the memo shows $10,005). With the shortfall placed on the top fifth (section 2), net per household: Q1 +6,634, Q2 +9,890, **Q3 +8,576** (memo +11,077), **Q4 −259** (memo +4,921), Q5 −30,978, top 1% −245,733. The lead's rough re-estimate (+$8,700; about break-even) is confirmed.
- **Downstream claims that change** if that package is kept: "In plain terms" 7, B3's tables and the "middle fifth pays 6.4%" line (it is 8.0% of expanded income), B3's "beside the rest of the plan" (Q4 is then about +$300 with scenario Q's +$552), B4, D3's household test (Q4 no longer passes on average), and every F1 to F3 household row.

## 2. Where the avoidance shortfall falls: evidence

The contribution's base is AGI, so itemized deductions cannot shrink it. That leaves reporting and real responses.
- **Withheld wages are hardly misreported.** The IRS estimates net misreporting at 1% of income with substantial information reporting and withholding (wages), 6% with reporting but no withholding, and 55% with little or no reporting (sole proprietors), tax years 2014-16 [EV-CAR-719] (IRS Publication 1415, SRC-3396, saved as text).
- **Measured responses concentrate at the top.** Gruber and Saez: taxable-income elasticity 0.57 above $100,000 (1992 dollars, about $320,000 in FY2040), against 0.18 for $10,000-50,000 and 0.11 for $50,000-100,000; for broad income the estimates below $100,000 are negative but insignificant [EV-CAR-720] (SRC-3397, cited). Saez, Slemrod and Giertz (*JEL* 50(1), 2012) review the literature: about 0.12 to 0.4 overall, the response concentrated in the top 1%. That review is not yet in the register.
- **The budget model's yields are CBO/JCT option 60938's**, which already include JCT's conventional behavioural response. The 20% is an extra allowance on top.
- **Working assumption used:** the whole shortfall falls on the top fifth (Q1 to Q4 none), shared within it in proportion to the charge, so the top 1% takes 18.9%. **Range:**
  - "elastic": Gruber and Saez's taxable-income elasticities on every quintile (Q1-Q3 0.18, Q4 0.11, Q5 0.57), the upper bound for the middle. The memo's package then gives Q3 +9,670 and Q4 +1,126.
  - "even": the first draft's method, Q3 +11,077 and Q4 +4,921; not supported by the evidence.
- **Rough check:** an extra 16 points on top-fifth income, at elasticity 0.3 to 0.57 against marginal rates near 50-60%, loses about 25-70% of the static yield there. So 20% overall, all of it at the top, is plausible, and possibly low at the very top.

## 3. Top-coding

The CPS gives the top 1% 11.9% of the broad base. IRS data, tax year 2022: the top 1% of returns had 22.4% of $14.75T of AGI [EV-CAR-721] (Tax Foundation restating IRS SOI, SRC-3398). After the lines, which fall mostly below the top half, that is about **29% of the base** (approximate). The household model's own convention fixes the top 1% only where `keys.csv` says so (the surtax key keeps the legacy 55% against the CPS's 28%).

Sensitivity: re-key the broad charge with the top 1% at 29% and the other households scaled down in proportion. On the memo's package that gives Q3 +10,999 and Q4 +4,759 (against +8,576 and −259). This is large enough to matter for D3, but it rests on tax units rather than households and on an approximate base. Settle a household-ranked top-1% base share (SOI, CBO's distribution data, or TPC) before relying on it.

## 4. The lower-rate package (item 2), as far as it got

The packages, FY2040; net per household; the second tier is on AGI above $100,000/$200,000, per point $66.9B collected:

| Package | Employers | States | Household side | Q1 | Q2 | Q3 | Q4 | Q5 | Top 1% | Top rate on wages |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Memo's (corrected) | 65%, 7.7% payroll | 80% | 15.68% | +6,634 | +9,890 | +8,576 | −259 | −30,978 | −245,733 | 66.3% |
| Employers and states 100%, one rate | 100%, 11.9% payroll | 100% | 11.75% | +6,393 | +9,603 | +9,093 | +1,761 | −28,426 | −243,180 | 62.4% |
| Same, two tiers | 100% | 100% | 10.0% + 4.7 | +6,437 | +10,056 | +10,466 | +4,254 | −32,788 | −335,401 | 65.3% |
| Two tiers, states at 80% | 100% | 80% | 10.8% + 4.7 | +6,418 | +9,857 | +9,856 | +2,990 | −35,259 | −344,718 | 66.1% |

Notes on the table:
- The top rate stacks the health contribution's points on 39.6% (G9), 5% Medicare and investment tax (H1b) and the booked 4 + 2 points. It is project arithmetic.
- **Savings booked as a sensitivity** (administration 3%, drugs 23% below today: −$256B in FY2040). The two-tier package's first tier falls to 8.6% and Q4 rises to +6,604. With savings, the one-rate package is at 10.3%.
- **Top avoidance at 60% on the second tier** (instead of 20%): the first tier rises to 10.9% and Q4 falls to +2,814.
- **Half pass-through** (Anand, $0.52 per $1 [EV-CAR-299]). At 100% employer contributions nothing depends on pass-through, because employers keep no net saving. At the memo's 65%, employers keep $415B: the federal side loses about $95B (0.53 points), and Q4 falls to −2,306, Q3 to +6,876.
- **A package where every fifth below the top comes out ahead exists**: employers at 100%, states at 100%, any second tier from 0 to 31 points. With the memo's 65% and 80%, Q4 turns positive only with a second tier (1 point: +272; 4.7 points: +2,235, first tier 13.9%).

**Espen's 5-6% ceiling** (the lead's addition; first-tier rate) **is not met by these levers alone.**
- At employers 100% and states 100%, the second tier has to reach about 16 to 18 points for a 5-6% first tier: about 19 points gives 4.7%, 16 points gives 5.8%. The top rate on wages would then be about 72-74%, at or above the Diamond-Saez revenue-maximizing 73% the legacy menu cites (`legacy/sources/revenue-channels-and-full-menu.md`). The 20% avoidance allowance would not hold at that rate.
- Adding the $256B of savings lowers the first tier by about 1.4 points.
- Getting to 5-6% with a plausible top rate needs another broad base: a VAT with a rebate (F1 C's half), a worker payroll piece, or new general revenue. The top-end taxes the Sanders options paper used are already booked for the rest of the plan (part B5, part E), so general revenue for health means new taxes beyond those.
- Plain wording for Espen: F1 A is an income-based contribution on all income above the line, collected with the income tax (wages, pensions, investment income). It is not a payroll tax. F1 B is a payroll tax on earnings only.

## 5. The full accounting (item 3) and the B1 seam

National health spending by who pays, 2032 full scale (coverage model, decided variant), $ billion. Both columns add to national spending (8,276 and 7,785):

| Payer | Today | The plan, before new financing | Change |
| --- | --- | --- | --- |
| Federal: Medicare net, Medicaid federal, premium credits / plan outlays net of the states' payment, plus Medicaid long-term care's federal part | 2,390 | 5,782 | +3,392 |
| States: Medicaid's non-federal part / the states' 50% payment, plus long-term care | 614 | 389 | −225 |
| Employers: premiums | 1,547 | 0 | −1,547 |
| Households: premiums and out of pocket / copays and outside-plan out of pocket | 1,738 | 191 | −1,547 |
| Spending on the four lines with no payer named in the model | 389 | 0 | −389 |
| Other health spending (VA, DoD, public health, research and so on), less care for the uninsured that others pay for today | 1,598 | 1,423 | −174 |
| **National health spending** | **8,276** | **7,785** | **−491** |

FY2040 on the booking's path (×1.533): today 12,688, plan 11,936.

**The first draft's "missing term" (565) is 389 unassigned plus 174 of others' uncompensated care.** The unassigned 389, line by line:
- **Model seam: 172.**
  - CMS's Medicare figure (2,024, its pre-2025-law projection grown 7.7% a year) is 157 above CBO's February 2026 mandatory outlays of $1,867B [EV-CAR-718] (SRC-3395, CBO's workbook saved as text).
  - CBO's net Medicare (1,867 − 340 = 1,526) is 15 above its subsidy table's 1,511.
  - Priced through the plan (1.056 per Medicare dollar), the seam overstates the booked federal cost by about **$181B in 2032, about $0.28T in FY2040**. It is not rebooked. A rebase of the coverage model's Medicare line to CBO's gross would fix it; that is a model change.
- **Real spending with a real payer: 217.**
  - Medicare's receipts not counted, 93: CBO's $340B of premiums and other receipts, less the $248B of household premiums the model counts at $3,500 a person (Medigap included). So households and states (the Part D clawback) stop paying more than modeled.
  - Private premiums for people counted twice, 88: CBO's 189.2M private enrollees against 182.4M after the model's overlap removal. Their employers and workers pay too.
  - Other private premiums, 20; other out of pocket, 16.
- **Others' uncompensated care, 174**, is real: hospitals, state and local programs and philanthropy pay for it today.

The identity: new federal spending 3,392 = households 1,547 + employers 1,547 + states 225 + unassigned 389 + others' care 174 − saving 491.

**Answer to Espen's question** (one sentence): Yes for the country: public revenue plus what people still pay privately is about $0.75 trillion (6%) less than today's total in FY2040. But the new public money (about $5.06 trillion, $0.97 trillion of it returning as tax on former premiums that become pay) is about equal to what households, employers and states stop paying ($5.09 trillion), not less, because it also takes over about $0.86 trillion that other payers fund today; about $0.26 trillion of that is a model seam that overstates the federal cost.

**Why households' contribution exceeds what they stop paying.** The contribution is $2.83T; households stop paying $2.37T. The employer side collects only 65% of former employer premiums ($1.54T). The other 35% ($0.83T) becomes pay at full pass-through, and the plan taxes it (HX net of the lost tax, about $0.56T). The household contribution then covers what is left. In total, households come out about −$0.19T in FY2040 at the memo's package; the bottom four fifths gain and the top fifth pays. At employers 100%, nothing becomes pay, so the household contribution falls to $2.12T, below the $2.37T they stop paying.

## 6. HX: does it cover both premium shares?

`sub_esi` ($680B in 2032; EV-CAR-052) is JCT's "tax value of the exclusion of employment-based health insurance from federal income and payroll taxes", "but not ... Medicare wraparound coverage for former employees" (CBO, SRC-3000, table note d).
- The exclusion is the whole premium's: the employer's share, and the worker's share paid pre-tax through cafeteria plans. So HX covers both shares for income and payroll tax. Its rate against total premiums is 0.31 (680/2,177).
- The household rows put all of HX against "employer premiums that become pay" ($2.37T, the employer's share only). That makes it look like 44% of the pay rise; the worker's share shows up as premiums they stop paying.
- Gaps, each small:
  - the retiree wraparound exclusion is not in HX;
  - the booking's federal-coverage correction lowers HX by 50/680 (FEHB, TRICARE and the VA in the employer cell; `health_booking.py`, `FEDCOV_REVENUE_2032`), so the booked HX is $966B. The household rows use $1,043B, which charges households about $77B (about $500 a household) of tax the booking does not collect. Align them in the fresh start.
- When employers keep paying a share, HX falls by the exclusion's rate on that share (`employer_rows`, "less tax on pay that no longer rises"): $482B at 65% and $741B at 100%.

## 7. Code changes made in `6b32a83` (for reuse)

- `income_rows()`: each income contribution becomes two rows: the statutory charge (collected ÷ 0.8, on the base's key) and the avoidance credit (on an avoidance key).
- `avoidance_key()` with `AVOID_WEIGHTS` (central, elastic, even), plus a second-tier key `income_high` (AGI above $100,000/$200,000 indexed; the top 1% at keys.csv's surtax 55%).
- `keys()` also returns AGI and the base by quintile.
- `package()` builds any employer, state, household and savings combination. `memo_options()` builds F1 A to D, F2 and F3 around a chosen recommendation. `packages()` builds the four packages plus sensitivities, and `first_tier_search()` scans second-tier rates.
- `passthrough_check()`, `topcode_check()`, and a combined top rate on wages.
- `reconciliation()`: the payer table and the seam split above.
- Tests:
  - every package closes the need;
  - charge − avoidance = collected, and rate × base = charge;
  - central avoidance falls on Q5 only;
  - the lead's +$8,700 and break-even;
  - the reconciliation adds to national spending both ways, the identity holds, and 389 + 174 ≈ 565.
- Not done:
  - HX's $77B alignment;
  - the Medicare rebase;
  - a household-ranked top-1% base;
  - adding Saez, Slemrod and Giertz to the register;
  - the 5-6% ceiling worked as an option;
  - HX shown in every option's table (it is the third relief row in every package's `detail`).

## Sources added on this branch

- SRC-3395, the text of CBO's February 2026 projections workbook (SRC-1142);
- SRC-3396, IRS Publication 1415;
- SRC-3397, Gruber and Saez (cited);
- SRC-3398, Tax Foundation on IRS SOI 2022 (cited);
- evidence entries EV-CAR-718 to EV-CAR-721 in `dossiers/care/evidence.json`.
