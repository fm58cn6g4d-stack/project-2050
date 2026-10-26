# Recovery and Solvency budget: exploratory results

> **Approval implemented:** Espen selected the recommended architecture and working spending changes; [adopted inputs](data/inputs/recovery-adoption.json) feed this model. The preferred architecture is the mixed reserve-corridor case. Its illustrative tax rates, credit and grant parameters remain unselected, and no complete financing schedule is adopted. Read [the assessment](../sources/recovery-and-solvency-budget.md) and [method/source notes](tools/recovery-budget/README.md). Nominal dollars; FY2030–39 window. Existing federal revenue/spending/debt are included; gross-flow, state/local and annual account reconciliation remain incomplete. No D3/D4 or all-fund solvency certification.

| Case | Debt/GDP 2039 | Debt/GDP 2056 | Deficit/GDP 2056 | Stable debt ratio 2045–56? | Broad-income rate needed, total points |
| --- | ---: | ---: | ---: | --- | ---: |
| mixed | 119.3% | 114.7% | 3.71% | True | 1.48 |
| larger_payroll | 119.0% | 113.0% | 3.54% | True | 1.18 |
| mixed_downside | 124.9% | 136.9% | 5.53% | False | 5.21 |
| mixed_all_debt_rate_plus1 | 130.9% | 151.0% | 6.53% | False | 5.27 |
| mixed_no_macro_translation | 119.2% | 113.3% | 3.55% | True | — |
| mixed_leave_admin_high | 119.4% | 115.0% | 3.73% | True | — |
| mixed_ssa_medicare_all_hi | 119.3% | 114.7% | 3.71% | True | — |
| mixed_ssa_medicare_all_smi | 119.3% | 114.7% | 3.71% | True | — |
| mixed_reserve_corridor | 119.3% | 114.7% | 3.71% | True | — |
| mixed_corridor_downside | 124.9% | 136.9% | 5.53% | False | — |
| mixed_legacy_education_floor | 119.4% | 114.8% | 3.72% | True | — |
| mixed_larger_credit | 123.7% | 119.2% | 3.83% | True | — |

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
| 2029 | 6261 | 7015 | 6261 | 8405 | 1345 | 2144 | 107.5% |
| 2030 | 6534 | 7364 | 7357 | 9659 | 1457 | 2302 | 109.6% |
| 2035 | 7898 | 8732 | 10173 | 12462 | 2007 | 2289 | 116.7% |
| 2039 | 9294 | 10409 | 12261 | 14740 | 2412 | 2479 | 119.3% |
| 2045 | 11831 | 13205 | 15996 | 18451 | 3030 | 2455 | 117.7% |
| 2056 | 17910 | 20097 | 24078 | 27625 | 4374 | 3546 | 114.7% |

Totals above are $B, not $T. The audit CSV exposes every increment and matched gross-up. Internal fund grants do not appear as new external resources.

| Household diagnostic, FY2039 annual net $/household | Q1 | Q2 | Q3 | Q4 | Q5 |
| --- | ---: | ---: | ---: | ---: | ---: |
| mixed | 15,739 | 12,818 | 6,746 | -2,698 | -76,873 |
| larger_payroll | 15,560 | 12,168 | 5,416 | -4,308 | -73,645 |
| mixed_larger_credit | 18,034 | 15,555 | 9,909 | -393 | -86,472 |

These are approximate quintile averages including modeled benefits, not a D3 certification or guarantees for individual households. See the assumptions and limits in the assessment.

| Fund, mixed case | Result |
| --- | --- |
| Education | Depletion: None; terminal reserve/outlays 19.53; rising: True |
| Combined OASDI | Depletion: None; conservative model solvency: False; actuarial balance +0.50% payroll |
| HI | Depletion: None; terminal reserve/cost 6.83; rising: True |
| Leave, high take-up | Loan repaid 2058; terminal loan $0.0B |

OASI/DI legal separation, the HI annual-data calibration, HTF beyond 2046, and long-run category/cash mappings remain unresolved. A positive balance in one fund cannot fund a second account without legislation.
