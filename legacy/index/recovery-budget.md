# Recovery and Solvency budget: exploratory results

> **Climate scope:** Includes decided domestic Package A, conservative credit savings, O5 and CLI-7C expected cost. The $75–150B contingent reinsurance liability is disclosed, not scored. International purchases and removal purchases are excluded. Annual 2030–50 export flows are extended at constant real 2050 levels to 2056; this is a transparent proxy, not a long-term emissions forecast. See [integration accounting](../sources/climate-ledger-integration.md).

> **Approval implemented:** Espen selected the recommended architecture and working spending changes; [adopted inputs](data/inputs/recovery-adoption.json) feed this model. The preferred architecture is the mixed reserve-corridor case. Its illustrative tax rates, credit and grant parameters remain unselected, and no complete financing schedule is adopted. Read [the assessment](../sources/recovery-and-solvency-budget.md) and [method/source notes](tools/recovery-budget/README.md). Nominal dollars; FY2030–39 window. Existing federal revenue/spending/debt are included; gross-flow, state/local and annual account reconciliation remain incomplete. No D3/D4 or all-fund solvency certification.

| Case | Debt/GDP 2039 | Debt/GDP 2056 | Deficit/GDP 2056 | Stable debt ratio 2045–56? | Broad-income rate needed, total points |
| --- | ---: | ---: | ---: | --- | ---: |
| mixed | 124.8% | 162.5% | 8.15% | False | 9.21 |
| larger_payroll | 125.4% | 165.6% | 8.39% | False | 9.59 |
| mixed_downside | 130.1% | 181.7% | 9.69% | False | 14.86 |
| mixed_all_debt_rate_plus1 | 132.5% | 197.0% | 11.30% | False | 12.75 |
| mixed_no_macro_translation | 124.6% | 161.5% | 8.04% | False | — |
| mixed_leave_admin_high | 124.9% | 162.8% | 8.17% | False | — |
| mixed_ssa_medicare_all_hi | 124.8% | 162.5% | 8.15% | False | — |
| mixed_ssa_medicare_all_smi | 124.8% | 162.5% | 8.15% | False | — |
| mixed_reserve_corridor | 124.8% | 162.5% | 8.15% | False | — |
| mixed_corridor_downside | 130.1% | 181.7% | 9.69% | False | — |
| mixed_legacy_education_floor | 124.9% | 162.7% | 8.16% | False | — |
| mixed_larger_credit | 129.2% | 167.0% | 8.27% | False | — |

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
| 2030 | 6534 | 7364 | 7599 | 9588 | 1451 | 1989 | 108.8% |
| 2035 | 7898 | 8732 | 12384 | 15108 | 1953 | 2724 | 114.1% |
| 2039 | 9294 | 10409 | 14976 | 18601 | 2503 | 3625 | 124.8% |
| 2045 | 11831 | 13205 | 19544 | 23938 | 3487 | 4394 | 136.5% |
| 2056 | 17910 | 20097 | 29582 | 37382 | 6159 | 7800 | 162.5% |

Totals above are $B, not $T. The audit CSV exposes every increment and matched gross-up. Internal fund grants do not appear as new external resources.

| Household diagnostic, FY2039 annual net $/household | Q1 | Q2 | Q3 | Q4 | Q5 |
| --- | ---: | ---: | ---: | ---: | ---: |
| mixed | 12,234 | 8,626 | 3,567 | -4,182 | -76,745 |
| larger_payroll | 12,111 | 8,255 | 2,909 | -4,870 | -72,650 |
| mixed_larger_credit | 14,529 | 11,362 | 6,731 | -1,877 | -86,344 |

These are approximate quintile averages including modeled benefits, not a D3 certification or guarantees for individual households. See the assumptions and limits in the assessment.

| Fund, mixed case | Result |
| --- | --- |
| Education | Depletion: 2035; terminal reserve/outlays -2.59; rising: True |
| Combined OASDI | Depletion: 2093; conservative model solvency: False; actuarial balance -0.31% payroll |
| HI | Depletion: 2038; terminal reserve/cost -4.60; rising: False |
| Leave, high take-up | No Treasury loan (peak $0.0B); terminal loan $0.0B |

Combined OASDI has modeled depletion in 2093; its reserve/cost ratio moves from -10.9% in 2095 to -58.0% in 2100. The final-period decline is 47.17 percentage points: the unchanged maximum-decline test of 0.5 points fails. Sustainability also requires no depletion and a terminal ratio of at least 100%. Actuarial balance: -0.311% of payroll. SSA administration is charged to OASDI in this case.

OASI/DI legal separation, the HI annual-data calibration, HTF beyond 2046, and long-run category/cash mappings remain unresolved. A positive balance in one fund cannot fund a second account without legislation.
