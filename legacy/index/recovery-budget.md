# Recovery and Solvency budget: exploratory results

> **Climate scope:** Includes decided domestic Package A, conservative credit savings, O5 and CLI-7C expected cost. The $75–150B contingent reinsurance liability is disclosed, not scored. International purchases and removal purchases are excluded. Annual 2030–50 export flows are extended at constant real 2050 levels to 2056; this is a transparent proxy, not a long-term emissions forecast. See [integration accounting](../sources/climate-ledger-integration.md).

> **Approval implemented:** Espen selected the recommended architecture and working spending changes; [adopted inputs](data/inputs/recovery-adoption.json) feed this model. The preferred architecture is the mixed reserve-corridor case. Its illustrative tax rates, credit and grant parameters remain unselected, and no complete financing schedule is adopted. Read [the assessment](../sources/recovery-and-solvency-budget.md) and [method/source notes](tools/recovery-budget/README.md). Nominal dollars; FY2030–39 window. Existing federal revenue/spending/debt are included; gross-flow, state/local and annual account reconciliation remain incomplete. No D3/D4 or all-fund solvency certification.

| Case | Debt/GDP 2039 | Debt/GDP 2056 | Deficit/GDP 2056 | Stable debt ratio 2045–56? | Broad-income rate needed, total points |
| --- | ---: | ---: | ---: | --- | ---: |
| mixed | 167.2% | 338.1% | 22.56% | False | 32.38 |
| larger_payroll | 167.9% | 341.2% | 22.80% | False | 32.75 |
| mixed_downside | 172.6% | 357.3% | 24.09% | False | 45.75 |
| mixed_all_debt_rate_plus1 | 176.4% | 393.8% | 28.31% | False | 36.86 |
| mixed_no_macro_translation | 167.1% | 337.0% | 22.43% | False | — |
| mixed_leave_admin_high | 167.3% | 338.4% | 22.58% | False | — |
| mixed_ssa_medicare_all_hi | 167.2% | 338.1% | 22.56% | False | — |
| mixed_ssa_medicare_all_smi | 167.2% | 338.1% | 22.55% | False | — |
| mixed_reserve_corridor | 167.2% | 338.1% | 22.56% | False | — |
| mixed_corridor_downside | 172.6% | 357.3% | 24.09% | False | — |
| mixed_legacy_education_floor | 167.3% | 338.3% | 22.57% | False | — |
| mixed_larger_credit | 171.6% | 342.6% | 22.68% | False | — |

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
| 2030 | 6534 | 7364 | 7369 | 9615 | 1456 | 2245 | 109.5% |
| 2035 | 7898 | 8732 | 10914 | 16315 | 2211 | 5401 | 132.0% |
| 2039 | 9294 | 10409 | 13140 | 20830 | 3304 | 7690 | 167.2% |
| 2045 | 11831 | 13205 | 17093 | 28129 | 5600 | 11036 | 221.7% |
| 2056 | 17910 | 20097 | 25906 | 47489 | 12751 | 21583 | 338.1% |

Totals above are $B, not $T. The audit CSV exposes every increment and matched gross-up. Internal fund grants do not appear as new external resources.

| Household diagnostic, FY2039 annual net $/household | Q1 | Q2 | Q3 | Q4 | Q5 |
| --- | ---: | ---: | ---: | ---: | ---: |
| mixed | 12,031 | 8,213 | 2,839 | -5,069 | -77,882 |
| larger_payroll | 11,908 | 7,842 | 2,181 | -5,758 | -73,787 |
| mixed_larger_credit | 14,326 | 10,949 | 6,002 | -2,764 | -87,481 |

These are approximate quintile averages including modeled benefits, not a D3 certification or guarantees for individual households. See the assumptions and limits in the assessment.

| Fund, mixed case | Result |
| --- | --- |
| Education | Depletion: 2035; terminal reserve/outlays -2.59; rising: True |
| Combined OASDI | Depletion: 2093; conservative model solvency: False; actuarial balance -0.31% payroll |
| HI | Depletion: 2047; terminal reserve/cost 0.76; rising: True |
| Leave, high take-up | No Treasury loan (peak $0.0B); terminal loan $0.0B |

Combined OASDI has modeled depletion in 2093; its reserve/cost ratio moves from -10.9% in 2095 to -58.0% in 2100. The final-period decline is 47.17 percentage points: the unchanged maximum-decline test of 0.5 points fails. Sustainability also requires no depletion and a terminal ratio of at least 100%. Actuarial balance: -0.311% of payroll. SSA administration is charged to OASDI in this case.

OASI/DI legal separation, the HI annual-data calibration, HTF beyond 2046, and long-run category/cash mappings remain unresolved. A positive balance in one fund cannot fund a second account without legislation.
