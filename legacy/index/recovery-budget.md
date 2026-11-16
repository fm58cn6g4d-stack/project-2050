# Recovery and Solvency budget: exploratory results

> **Climate scope:** Includes decided domestic Package A, conservative credit savings, O5 and CLI-7C expected cost. The $75–150B contingent reinsurance liability is disclosed, not scored. International purchases and removal purchases are excluded. Annual 2030–50 export flows are extended at constant real 2050 levels to 2056; this is a transparent proxy, not a long-term emissions forecast. See [integration accounting](../sources/climate-ledger-integration.md).

> **Approval implemented:** Espen selected the recommended architecture and working spending changes; [adopted inputs](data/inputs/recovery-adoption.json) feed this model. The preferred architecture is the mixed reserve-corridor case. Its illustrative tax rates, credit and grant parameters remain unselected, and no complete financing schedule is adopted. Read [the assessment](../sources/recovery-and-solvency-budget.md) and [method/source notes](tools/recovery-budget/README.md). Nominal dollars; FY2030–39 window. Existing federal revenue/spending/debt are included; gross-flow, state/local and annual account reconciliation remain incomplete. No D3/D4 or all-fund solvency certification.

| Case | Debt/GDP 2039 | Debt/GDP 2056 | Deficit/GDP 2056 | Stable debt ratio 2045–56? | Broad-income rate needed, total points |
| --- | ---: | ---: | ---: | --- | ---: |
| mixed | 123.8% | 161.7% | 8.14% | False | 9.26 |
| larger_payroll | 124.4% | 164.8% | 8.38% | False | 9.64 |
| mixed_downside | 129.2% | 180.8% | 9.68% | False | 14.93 |
| mixed_all_debt_rate_plus1 | 131.4% | 195.9% | 11.27% | False | 12.76 |
| mixed_no_macro_translation | 123.7% | 160.7% | 8.03% | False | — |
| mixed_leave_admin_high | 123.9% | 162.0% | 8.16% | False | — |
| mixed_ssa_medicare_all_hi | 123.8% | 161.7% | 8.14% | False | — |
| mixed_ssa_medicare_all_smi | 123.8% | 161.7% | 8.14% | False | — |
| mixed_reserve_corridor | 123.8% | 161.7% | 8.14% | False | — |
| mixed_corridor_downside | 129.2% | 180.8% | 9.68% | False | — |
| mixed_legacy_education_floor | 123.9% | 161.8% | 8.15% | False | — |
| mixed_larger_credit | 128.2% | 166.2% | 8.26% | False | — |

The last column is the total broad-tier rate required under this static tax-yield proxy, replacing the proposed two-point broad tier, with the high tier unchanged. It is not a tax score.

| Education component | Full fund $T | Current law moved $T | Increment vs current law $T | Old agenda moved $T | Change vs old agenda $T |
| --- | ---: | ---: | ---: | ---: | ---: |
| meals | 0.707 | 0.432 | 0.274 | 0.270 | 0.004 |
| idea | 0.513 | 0.184 | 0.329 | 0.250 | 0.079 |
| care | 1.484 | 0.000 | 1.484 | 1.484 | 0.000 |
| title_i | 0.361 | 0.238 | 0.123 | 0.080 | 0.043 |
| teacher | 0.076 | 0.000 | 0.076 | 0.000 | 0.076 |
| para_mental | 0.096 | 0.000 | 0.096 | 0.000 | 0.096 |
| pipeline | 0.034 | 0.000 | 0.034 | 0.030 | 0.004 |
| TOTAL | 3.270 | 0.854 | 2.416 | 2.114 | 0.302 |

| Fixed-grant comparison, FY | Current-law revenue | Current-law primary spending | Total revenue | Total spending | Net interest | Deficit | Debt/GDP |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 2029 | 6261 | 7015 | 6261 | 8405 | 1345 | 2144 | 107.5% |
| 2030 | 6534 | 7364 | 7640 | 9591 | 1450 | 1950 | 108.7% |
| 2035 | 7898 | 8732 | 12400 | 15087 | 1940 | 2687 | 113.3% |
| 2039 | 9294 | 10409 | 14979 | 18559 | 2483 | 3579 | 123.8% |
| 2045 | 11831 | 13205 | 19497 | 23880 | 3459 | 4384 | 135.5% |
| 2056 | 17910 | 20097 | 29511 | 37302 | 6126 | 7791 | 161.7% |

Totals above are $B, not $T. The audit CSV exposes every increment and matched gross-up. Internal fund grants do not appear as new external resources.

| Household diagnostic, FY2039 annual net $/household | Q1 | Q2 | Q3 | Q4 | Q5 |
| --- | ---: | ---: | ---: | ---: | ---: |
| mixed | 12,256 | 8,641 | 3,565 | -4,199 | -76,760 |
| larger_payroll | 12,132 | 8,270 | 2,906 | -4,887 | -72,665 |
| mixed_larger_credit | 14,551 | 11,377 | 6,728 | -1,894 | -86,359 |

These are approximate quintile averages including modeled benefits, not a D3 certification or guarantees for individual households. See the assumptions and limits in the assessment.

| Fund, mixed case | Result |
| --- | --- |
| Education | Depletion: 2035; terminal reserve/outlays -2.59; rising: True |
| Combined OASDI | Depletion: 2093; conservative model solvency: False; actuarial balance -0.31% payroll |
| HI | Depletion: 2038; terminal reserve/cost -4.60; rising: False |
| Leave, high take-up | No Treasury loan (peak $0.0B); terminal loan $0.0B |

Combined OASDI has modeled depletion in 2093; its reserve/cost ratio moves from -10.9% in 2095 to -58.0% in 2100. The final-period decline is 47.17 percentage points: the unchanged maximum-decline test of 0.5 points fails. Sustainability also requires no depletion and a terminal ratio of at least 100%. Actuarial balance: -0.311% of payroll. SSA administration is charged to OASDI in this case.

OASI/DI legal separation, the HI annual-data calibration, HTF beyond 2046, and long-run category/cash mappings remain unresolved. A positive balance in one fund cannot fund a second account without legislation.
