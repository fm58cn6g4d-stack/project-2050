# Recovery and Solvency budget: exploratory results

> **Approval implemented:** Espen selected the recommended architecture and working spending changes; [adopted inputs](data/inputs/recovery-adoption.json) feed this model. The preferred architecture is the mixed reserve-corridor case. Its illustrative tax rates, credit and grant parameters remain unselected, and no complete financing schedule is adopted. Read [the assessment](../sources/recovery-and-solvency-budget.md) and [method/source notes](tools/recovery-budget/README.md). Nominal dollars; FY2030–39 window. Existing federal revenue/spending/debt are included; gross-flow, state/local and annual account reconciliation remain incomplete. No D3/D4 or all-fund solvency certification.

| Case | Debt/GDP 2039 | Debt/GDP 2056 | Deficit/GDP 2056 | Stable debt ratio 2045–56? | Broad-income rate needed, total points |
| --- | ---: | ---: | ---: | --- | ---: |
| mixed | 119.5% | 114.4% | 3.67% | True | 1.40 |
| larger_payroll | 119.2% | 112.6% | 3.50% | True | 1.10 |
| mixed_downside | 125.1% | 136.6% | 5.49% | False | 5.11 |
| mixed_all_debt_rate_plus1 | 131.1% | 150.6% | 6.49% | False | 5.20 |
| mixed_no_macro_translation | 119.3% | 112.9% | 3.51% | True | — |
| mixed_reserve_corridor | 119.5% | 114.4% | 3.67% | True | — |
| mixed_corridor_downside | 125.1% | 136.6% | 5.49% | False | — |
| mixed_legacy_education_floor | 119.6% | 114.5% | 3.68% | True | — |
| mixed_larger_credit | 123.9% | 118.9% | 3.79% | True | — |

The last column is the total broad-tier rate required under this static tax-yield proxy, replacing the proposed two-point broad tier, with the high tier unchanged. It is not a tax score.

| Education component | Full fund $T | Current law moved $T | Increment vs current law $T | Old agenda moved $T | Change vs old agenda $T |
| --- | ---: | ---: | ---: | ---: | ---: |
| meals | 0.707 | 0.432 | 0.274 | 0.270 | 0.004 |
| idea | 0.513 | 0.184 | 0.329 | 0.250 | 0.079 |
| care | 0.786 | 0.000 | 0.786 | 0.600 | 0.186 |
| title_i | 0.361 | 0.238 | 0.123 | 0.080 | 0.043 |
| teacher | 0.076 | 0.000 | 0.076 | 0.000 | 0.076 |
| para_mental | 0.096 | 0.000 | 0.096 | 0.000 | 0.096 |
| pipeline | 0.034 | 0.000 | 0.034 | 0.030 | 0.004 |
| TOTAL | 2.572 | 0.854 | 1.718 | 1.230 | 0.488 |

| Fixed-grant comparison, FY | Current-law revenue | Current-law primary spending | Total revenue | Total spending | Net interest | Deficit | Debt/GDP |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 2029 | 6261 | 7015 | 6261 | 8410 | 1345 | 2149 | 107.5% |
| 2030 | 6534 | 7364 | 7357 | 9671 | 1457 | 2314 | 109.7% |
| 2035 | 7898 | 8732 | 10173 | 12472 | 2012 | 2299 | 117.0% |
| 2039 | 9294 | 10409 | 12261 | 14727 | 2416 | 2466 | 119.5% |
| 2045 | 11831 | 13205 | 15995 | 18431 | 3031 | 2436 | 117.7% |
| 2056 | 17910 | 20097 | 24078 | 27586 | 4362 | 3508 | 114.4% |

Totals above are $B, not $T. The audit CSV exposes every increment and matched gross-up. Internal fund grants do not appear as new external resources.

| Household diagnostic, FY2039 annual net $/household | Q1 | Q2 | Q3 | Q4 | Q5 |
| --- | ---: | ---: | ---: | ---: | ---: |
| mixed | 15,741 | 12,820 | 6,747 | -2,697 | -76,872 |
| larger_payroll | 15,561 | 12,170 | 5,418 | -4,307 | -73,644 |
| mixed_larger_credit | 18,036 | 15,557 | 9,911 | -392 | -86,471 |

These are approximate quintile averages including modeled benefits, not a D3 certification or guarantees for individual households. See the assumptions and limits in the assessment.

| Fund, mixed case | Result |
| --- | --- |
| Education | Depletion: None; terminal reserve/outlays 19.53; rising: True |
| Combined OASDI | Depletion: None; conservative model solvency: True; actuarial balance +0.50% payroll |
| HI | Depletion: None; terminal reserve/cost 6.88; rising: True |
| Leave, high take-up | Loan repaid 2048; terminal loan $0.0B |

OASI/DI legal separation, the HI annual-data calibration, HTF beyond 2046, and long-run category/cash mappings remain unresolved. A positive balance in one fund cannot fund a second account without legislation.
