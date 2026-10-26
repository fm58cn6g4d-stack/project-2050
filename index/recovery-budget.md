# Recovery and Solvency budget: exploratory results

> **Climate scope:** This capacity/fund reference retains the historical carbon schedule. Merged PR #26 is evaluated in the separate [climate financing comparison](../sources/climate-recovery-financing-comparison.md); these totals are not the fully integrated current climate agenda.

> **Approval implemented:** Espen selected the recommended architecture and working spending changes; [adopted inputs](data/inputs/recovery-adoption.json) feed this model. The preferred architecture is the mixed reserve-corridor case. Its illustrative tax rates, credit and grant parameters remain unselected, and no complete financing schedule is adopted. Read [the assessment](../sources/recovery-and-solvency-budget.md) and [method/source notes](tools/recovery-budget/README.md). Nominal dollars; FY2030–39 window. Existing federal revenue/spending/debt are included; gross-flow, state/local and annual account reconciliation remain incomplete. No D3/D4 or all-fund solvency certification.

| Case | Debt/GDP 2039 | Debt/GDP 2056 | Deficit/GDP 2056 | Stable debt ratio 2045–56? | Broad-income rate needed, total points |
| --- | ---: | ---: | ---: | --- | ---: |
| mixed | 119.4% | 115.3% | 3.76% | True | 1.58 |
| larger_payroll | 119.0% | 113.6% | 3.59% | True | 1.28 |
| mixed_downside | 124.9% | 137.6% | 5.59% | False | 5.35 |
| mixed_all_debt_rate_plus1 | 130.9% | 151.7% | 6.60% | False | 5.37 |
| mixed_no_macro_translation | 119.2% | 113.9% | 3.61% | True | — |
| mixed_leave_admin_high | 119.5% | 115.6% | 3.79% | True | — |
| mixed_ssa_medicare_all_hi | 119.4% | 115.3% | 3.77% | True | — |
| mixed_ssa_medicare_all_smi | 119.4% | 115.3% | 3.76% | True | — |
| mixed_reserve_corridor | 119.4% | 115.3% | 3.76% | True | — |
| mixed_corridor_downside | 124.9% | 137.6% | 5.59% | False | — |
| mixed_legacy_education_floor | 119.4% | 115.5% | 3.77% | True | — |
| mixed_larger_credit | 123.8% | 119.9% | 3.88% | True | — |

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
| 2030 | 6534 | 7364 | 7355 | 9655 | 1457 | 2299 | 109.6% |
| 2035 | 7898 | 8732 | 10217 | 12509 | 2006 | 2292 | 116.7% |
| 2039 | 9294 | 10409 | 12324 | 14813 | 2413 | 2489 | 119.4% |
| 2045 | 11831 | 13205 | 16062 | 18545 | 3036 | 2483 | 118.0% |
| 2056 | 17910 | 20097 | 24149 | 27752 | 4398 | 3602 | 115.3% |

Totals above are $B, not $T. The audit CSV exposes every increment and matched gross-up. Internal fund grants do not appear as new external resources.

| Household diagnostic, FY2039 annual net $/household | Q1 | Q2 | Q3 | Q4 | Q5 |
| --- | ---: | ---: | ---: | ---: | ---: |
| mixed | 15,927 | 12,910 | 6,662 | -2,906 | -77,221 |
| larger_payroll | 15,748 | 12,260 | 5,333 | -4,517 | -73,992 |
| mixed_larger_credit | 18,222 | 15,647 | 9,825 | -601 | -86,820 |

These are approximate quintile averages including modeled benefits, not a D3 certification or guarantees for individual households. See the assumptions and limits in the assessment.

| Fund, mixed case | Result |
| --- | --- |
| Education | Depletion: None; terminal reserve/outlays 19.53; rising: True |
| Combined OASDI | Depletion: None; conservative model solvency: False; actuarial balance +0.50% payroll |
| HI | Depletion: None; terminal reserve/cost 6.83; rising: True |
| Leave, high take-up | Loan repaid 2058; terminal loan $0.0B |

Combined OASDI has no modeled depletion through 2100; its reserve/cost ratio moves from 364.0% in 2095 to 363.1% in 2100. The final-period decline is 0.85 percentage points: the unchanged maximum-decline test of 0.5 points fails. Sustainability also requires no depletion and a terminal ratio of at least 100%. Actuarial balance: +0.495% of payroll. SSA administration is charged to OASDI in this case.

OASI/DI legal separation, the HI annual-data calibration, HTF beyond 2046, and long-run category/cash mappings remain unresolved. A positive balance in one fund cannot fund a second account without legislation.
