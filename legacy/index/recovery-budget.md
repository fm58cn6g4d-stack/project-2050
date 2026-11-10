# Recovery and Solvency budget: exploratory results

> **Climate scope:** Includes decided domestic Package A, conservative credit savings, O5 and CLI-7C expected cost. The $75–150B contingent reinsurance liability is disclosed, not scored. International purchases and removal purchases are excluded. Annual 2030–50 export flows are extended at constant real 2050 levels to 2056; this is a transparent proxy, not a long-term emissions forecast. See [integration accounting](../sources/climate-ledger-integration.md).

> **Approval implemented:** Espen selected the recommended architecture and working spending changes; [adopted inputs](data/inputs/recovery-adoption.json) feed this model. The preferred architecture is the mixed reserve-corridor case. Its illustrative tax rates, credit and grant parameters remain unselected, and no complete financing schedule is adopted. Read [the assessment](../sources/recovery-and-solvency-budget.md) and [method/source notes](tools/recovery-budget/README.md). Nominal dollars; FY2030–39 window. Existing federal revenue/spending/debt are included; gross-flow, state/local and annual account reconciliation remain incomplete. No D3/D4 or all-fund solvency certification.

| Case | Debt/GDP 2039 | Debt/GDP 2056 | Deficit/GDP 2056 | Stable debt ratio 2045–56? | Broad-income rate needed, total points |
| --- | ---: | ---: | ---: | --- | ---: |
| mixed | 120.5% | 119.1% | 4.05% | False | 2.02 |
| larger_payroll | 120.1% | 117.4% | 3.88% | True | 1.72 |
| mixed_downside | 126.0% | 141.4% | 5.88% | False | 5.93 |
| mixed_all_debt_rate_plus1 | 128.3% | 149.8% | 6.63% | False | 5.58 |
| mixed_no_macro_translation | 120.3% | 117.7% | 3.90% | True | — |
| mixed_leave_admin_high | 120.6% | 119.4% | 4.08% | False | — |
| mixed_ssa_medicare_all_hi | 120.5% | 119.1% | 4.05% | False | — |
| mixed_ssa_medicare_all_smi | 120.5% | 119.1% | 4.05% | False | — |
| mixed_reserve_corridor | 120.5% | 119.1% | 4.05% | False | — |
| mixed_corridor_downside | 126.0% | 141.4% | 5.88% | False | — |
| mixed_legacy_education_floor | 120.5% | 119.3% | 4.06% | False | — |
| mixed_larger_credit | 124.9% | 123.7% | 4.17% | True | — |

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
| 2030 | 6534 | 7364 | 7370 | 9710 | 1458 | 2340 | 109.7% |
| 2035 | 7898 | 8732 | 10227 | 12553 | 2016 | 2327 | 117.3% |
| 2039 | 9294 | 10409 | 12317 | 14912 | 2433 | 2596 | 120.5% |
| 2045 | 11831 | 13205 | 16049 | 18677 | 3087 | 2628 | 120.0% |
| 2056 | 17910 | 20097 | 24133 | 28012 | 4541 | 3879 | 119.1% |

Totals above are $B, not $T. The audit CSV exposes every increment and matched gross-up. Internal fund grants do not appear as new external resources.

| Household diagnostic, FY2039 annual net $/household | Q1 | Q2 | Q3 | Q4 | Q5 |
| --- | ---: | ---: | ---: | ---: | ---: |
| mixed | 16,957 | 13,343 | 6,686 | -3,000 | -77,416 |
| larger_payroll | 16,777 | 12,693 | 5,356 | -4,611 | -74,187 |
| mixed_larger_credit | 19,252 | 16,079 | 9,849 | -695 | -87,015 |

These are approximate quintile averages including modeled benefits, not a D3 certification or guarantees for individual households. See the assumptions and limits in the assessment.

| Fund, mixed case | Result |
| --- | --- |
| Education | Depletion: None; terminal reserve/outlays 19.53; rising: True |
| Combined OASDI | Depletion: None; conservative model solvency: False; actuarial balance +0.50% payroll |
| HI | Depletion: None; terminal reserve/cost 6.83; rising: True |
| Leave, high take-up | Loan repaid 2058; terminal loan $0.0B |

Combined OASDI has no modeled depletion through 2100; its reserve/cost ratio moves from 364.0% in 2095 to 363.1% in 2100. The final-period decline is 0.85 percentage points: the unchanged maximum-decline test of 0.5 points fails. Sustainability also requires no depletion and a terminal ratio of at least 100%. Actuarial balance: +0.495% of payroll. SSA administration is charged to OASDI in this case.

OASI/DI legal separation, the HI annual-data calibration, HTF beyond 2046, and long-run category/cash mappings remain unresolved. A positive balance in one fund cannot fund a second account without legislation.
