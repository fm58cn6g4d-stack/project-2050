# Recovery and Solvency budget: exploratory results

> **Climate scope:** Includes decided domestic Package A, conservative credit savings, O5 and CLI-7C expected cost. The $75–150B contingent reinsurance liability is disclosed, not scored. International purchases and removal purchases are excluded. Annual 2030–50 export flows are extended at constant real 2050 levels to 2056; this is a transparent proxy, not a long-term emissions forecast. See [integration accounting](../sources/climate-ledger-integration.md).

> **Approval implemented:** Espen selected the recommended architecture and working spending changes; [adopted inputs](data/inputs/recovery-adoption.json) feed this model. The preferred architecture is the mixed reserve-corridor case. Its illustrative tax rates, credit and grant parameters remain unselected, and no complete financing schedule is adopted. Read [the assessment](../sources/recovery-and-solvency-budget.md) and [method/source notes](tools/recovery-budget/README.md). Nominal dollars; FY2030–39 window. Existing federal revenue/spending/debt are included; gross-flow, state/local and annual account reconciliation remain incomplete. No D3/D4 or all-fund solvency certification.

| Case | Debt/GDP 2039 | Debt/GDP 2056 | Deficit/GDP 2056 | Stable debt ratio 2045–56? | Broad-income rate needed, total points |
| --- | ---: | ---: | ---: | --- | ---: |
| mixed | 166.8% | 330.4% | 21.91% | False | 31.31 |
| larger_payroll | 167.5% | 333.5% | 22.15% | False | 31.69 |
| mixed_downside | 172.0% | 348.6% | 23.37% | False | 44.19 |
| mixed_all_debt_rate_plus1 | 176.1% | 385.3% | 27.56% | False | 35.77 |
| mixed_no_macro_translation | 166.7% | 329.1% | 21.76% | False | — |
| mixed_leave_admin_high | 166.9% | 330.7% | 21.93% | False | — |
| mixed_ssa_medicare_all_hi | 166.8% | 330.4% | 21.91% | False | — |
| mixed_ssa_medicare_all_smi | 166.8% | 330.4% | 21.90% | False | — |
| mixed_reserve_corridor | 166.8% | 330.4% | 21.91% | False | — |
| mixed_corridor_downside | 172.0% | 348.6% | 23.37% | False | — |
| mixed_legacy_education_floor | 166.9% | 330.6% | 21.92% | False | — |
| mixed_larger_credit | 171.2% | 334.9% | 22.03% | False | — |

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
| 2030 | 6534 | 7364 | 7370 | 9551 | 1455 | 2181 | 109.3% |
| 2035 | 7898 | 8732 | 10964 | 16473 | 2218 | 5509 | 132.5% |
| 2039 | 9294 | 10409 | 13304 | 20820 | 3300 | 7516 | 166.8% |
| 2045 | 11831 | 13205 | 17404 | 28074 | 5524 | 10670 | 218.6% |
| 2056 | 17910 | 20097 | 26334 | 47295 | 12461 | 20961 | 330.4% |

Totals above are $B, not $T. The audit CSV exposes every increment and matched gross-up. Internal fund grants do not appear as new external resources.

| Household diagnostic, FY2039 annual net $/household | Q1 | Q2 | Q3 | Q4 | Q5 |
| --- | ---: | ---: | ---: | ---: | ---: |
| mixed | 10,032 | 6,111 | 856 | -6,955 | -79,672 |
| larger_payroll | 9,908 | 5,740 | 197 | -7,643 | -75,577 |
| mixed_larger_credit | 12,327 | 8,847 | 4,019 | -4,650 | -89,271 |

These are approximate quintile averages including modeled benefits, not a D3 certification or guarantees for individual households. See the assumptions and limits in the assessment.

| Fund, mixed case | Result |
| --- | --- |
| Education | Depletion: None; terminal reserve/outlays 19.53; rising: True |
| Combined OASDI | Depletion: None; conservative model solvency: False; actuarial balance +0.50% payroll |
| HI | Depletion: 2047; terminal reserve/cost -0.92; rising: True |
| Leave, high take-up | Loan repaid 2058; terminal loan $0.0B |

Combined OASDI has no modeled depletion through 2100; its reserve/cost ratio moves from 364.0% in 2095 to 363.1% in 2100. The final-period decline is 0.85 percentage points: the unchanged maximum-decline test of 0.5 points fails. Sustainability also requires no depletion and a terminal ratio of at least 100%. Actuarial balance: +0.495% of payroll. SSA administration is charged to OASDI in this case.

OASI/DI legal separation, the HI annual-data calibration, HTF beyond 2046, and long-run category/cash mappings remain unresolved. A positive balance in one fund cannot fund a second account without legislation.
