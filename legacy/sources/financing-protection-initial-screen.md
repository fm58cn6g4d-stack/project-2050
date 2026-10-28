# Contribution and protection: initial screen

**Historical screen:** numerical cases below predate PRs #23/#25 and their leave/SSA administration costs. Use the [updated spending comparisons](spending-package-comparisons.md) and current integrated budget for new decisions.

Start with the [revenue-rebalancing decision plan](revenue-rebalancing-and-sustainable-agenda.md) for the current direction and reading map.

October 26. Exploratory first step after PR #22 integration; no tax schedule selected. Source main aa8552d, with the capacity-integration changes. Reproduce after the common build with `python3 index/tools/financing-protection/screen.py`; [JSON results](financing-protection-screen.json). The [recovery method](../index/tools/recovery-budget/README.md) and its source references apply. This screen introduces no new external evidence.

The first finding is that raising the universal credit alone is a costly and incomplete answer. Removing the broad income contribution helps Q4 but weakens the debt path. Raising the so-called high-income contribution can also reach Q4: its threshold is $100,000 single/$200,000 joint in 2025 dollars, not a millionaires-only tax. The inherited distribution keys are rough; these are diagnostics rather than household guarantees.

All cases retain the illustrative 1.4-point education contribution, 30% public share, two-point later Social Security closer, HI support and education reserve corridor. Those illustrative financing parameters remain unselected. All use the integrated $250B IRS receipt-risk allowance and $12.2B voucher administration correction.

| Annual adult credit, 2030 dollars | Upper income tier points | Broad tier points | Debt/GDP 2056 | Q4 annual net, 2039 dollars |
| --- | --- | --- | --- | --- |
| $300 | 4 | 2 | 114.4% | −$2,697 |
| $1,500 | 10 | 2 | 118.9% | −$392 |
| $1,500 | 10 | 0 | 131.4% | +$1,097 |
| $2,400 | 10 | 2 | 136.1% | +$1,959 |
| $1,500 | 14 | 2 | 106.6% | −$944 |
| $2,400 | 14 | 0 | 136.3% | +$2,895 |

Do not read a debt endpoint as D4 stability, or a positive quintile average as D3. These household results include imputed service benefits and assumed health savings; they do not establish immediate disposable-income protection. The screen records 2030/2035 results too, but does not resolve FY2029 cash. Benefit receipt, disability, retirement, family structure and within-quintile losses remain unobserved in this approximation. Wage pass-through, employer payroll offsets and joint tax interactions require better evidence. No additional distributional benefit is credited for PHA administration spending.

**Direction for the settlement.** Develop a refundable contribution credit with a universal nonworker base and an additional worker contribution offset, rather than increasing a universal amount until one average turns positive. Test smooth phaseouts and higher upper-tier thresholds together; a phaseout is itself a marginal tax and must be priced. Include self-employment, retirees and disabled adults explicitly. Avoid paying twice for the same contribution through fund-side protection reserves and GF credits. Annual cash before imputed services and household losses must be visible alongside fund solvency and debt. A tax holiday financed by an unspecified future tax is not a funded solution.

The next calculation needs current-law household tax/benefit data and an explicit entitlement formula, not additional precision from these quintile keys. Build household cells by income, work status, age/disability and children; reconcile the population and tax bases to the federal totals; test employer wage incidence and health savings separately. Retain the present six cases as reproducible comparators. This is the beginning of the assigned financing work, not a completed microsimulation or a recommendation to adopt one of the table's schedules.

## Revenue-first revision following Espen's direction

The assignment now starts with a defensible revenue envelope and compares spending packages within it. Espen retains the final decision on strategic spending reductions. The earlier six cases are comparisons, not the organizing framework for this work.

Two additional diagnostics remove the new broad income contribution; the first also removes the additional upper income contribution. Both retain corporate/high-wealth reforms already carried by the model, its illustrative dedicated payroll financing, and the $300 adult credit:

| Additional upper income points | Additional broad points | Debt/GDP 2056 | Debt nonincreasing throughout 2045–56? | Q4 net in 2039 |
| --- | --- | --- | --- | --- |
| 0 | 0 | 139.1% | No | −$656 |
| 4 | 0 | 126.8% | No | −$1,208 |

The model already includes G1's corporate rate restoration, G5's minimum/buyback taxes, G7's foreign-income reform, G9's reversal of high-income tax relief, G6's gains-at-death reform and G11's billionaire taxation, with its existing overlap allowances. Their gross historical approximately $6.37T package is not a fresh pot available on top of the model. The new IRS allowance also reduces its usable receipts. Dedicated Social Security/HI receipts cannot fund unrelated programs without compromising those accounts. These comparisons are not a claim that the wealthy/corporate envelope has been exhausted: its source vintages, alternatives and interactions need fresh evaluation.

**Recommended analytical structure.** Establish three explicitly priced revenue cases: a durable core of corporate, high-income and capital-income reform; an expanded progressive case with incremental receipts measured against that core; and an adverse-yield case including avoidance, litigation and timing. Distinguish statutory threshold effects on upper-middle-income households from taxes on very large fortunes. Treat payroll contributions and their protection separately, with a consolidated total so that earmarking cannot hide costs. Do not score a corporate increase as burden-free for workers merely because corporations remit it.

For each case reserve financing for existing-government stability and trust-fund solvency, early recovery/protection, and delivery risk before allocating additional program expansions. Present annual receipts, permanent primary spending capacity, debt and interest alongside the ten-year total. Compare a protected essential-services package, a broader sustainable package, and the current proposed agenda with its financing gap visible. For each reduction identify lost coverage/service, distribution, delivery effects and whether it truly reduces permanent costs or merely postpones cash.

PR #23's proposed $200B finite capacity reduction is a candidate for that comparison, not adopted savings. A finite reduction cannot by itself close a permanent operating gap. Its allocation range and recurring unpriced functions need reconciliation before treating the proposed ceiling as sufficient. Likewise, moving NOAA satellites or foreign assistance out of the capacity category does not save money if the project still intends to fund them elsewhere.

The next substantive evidence pass will reconcile revenue provisions against current law and identify incremental alternatives without double counting, then price household protection and spending packages against those bounded receipts. The prior credit screen remains useful for revealing weaknesses; it no longer sets the fiscal objective.
