# Contribution and protection: initial screen

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
