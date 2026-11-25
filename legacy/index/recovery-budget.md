# Recovery and Solvency budget: exploratory results

> **Climate scope:** Includes decided domestic Package A, conservative credit savings, O5 and CLI-7C expected cost. The $75–150B contingent reinsurance liability is disclosed, not scored. International purchases and removal purchases are excluded. Annual 2030–50 export flows are extended at constant real 2050 levels to 2056; this is a transparent proxy, not a long-term emissions forecast. See [integration accounting](../sources/climate-ledger-integration.md).

> **Approval implemented:** Espen selected the recommended architecture and working spending changes; [adopted inputs](data/inputs/recovery-adoption.json) feed this model. The preferred architecture is the mixed reserve-corridor case. Its illustrative tax rates, credit and grant parameters remain unselected, and no complete financing schedule is adopted. Read [the assessment](../sources/recovery-and-solvency-budget.md) and [method/source notes](tools/recovery-budget/README.md). Nominal dollars; FY2030–39 window. Existing federal revenue/spending/debt are included; gross-flow, state/local and annual account reconciliation remain incomplete. No D3/D4 or all-fund solvency certification.

| Case | Debt/GDP 2039 | Debt/GDP 2056 | Deficit/GDP 2056 | Stable debt ratio 2045–56? | Broad-income rate needed, total points |
| --- | ---: | ---: | ---: | --- | ---: |
| mixed | 116.9% | 131.5% | 5.49% | False | 2.79 |
| mixed_before_settlement | 124.8% | 160.8% | 8.00% | False | — |
| larger_payroll | 118.2% | 136.8% | 5.90% | False | 3.43 |
| mixed_downside | 122.1% | 147.7% | 6.75% | False | 6.33 |
| mixed_all_debt_rate_plus1 | 124.3% | 162.3% | 8.18% | False | 6.21 |
| mixed_no_macro_translation | 116.8% | 130.5% | 5.37% | False | — |
| mixed_leave_admin_high | 117.0% | 131.8% | 5.51% | False | — |
| mixed_ssa_medicare_all_hi | 116.9% | 131.5% | 5.49% | False | — |
| mixed_ssa_medicare_all_smi | 116.9% | 131.5% | 5.49% | False | — |
| mixed_reserve_corridor | 116.9% | 131.5% | 5.49% | False | — |
| mixed_corridor_downside | 122.1% | 147.7% | 6.75% | False | — |
| mixed_legacy_education_floor | 117.0% | 131.7% | 5.50% | False | — |
| mixed_larger_credit | 129.2% | 165.4% | 8.12% | False | — |

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
| 2029 | 6261 | 7015 | 6261 | 8364 | 1344 | 2104 | 107.4% |
| 2030 | 6534 | 7364 | 7575 | 9500 | 1448 | 1925 | 108.5% |
| 2035 | 7898 | 8732 | 12670 | 14819 | 1912 | 2149 | 111.1% |
| 2039 | 9294 | 10409 | 15196 | 18086 | 2354 | 2890 | 116.9% |
| 2045 | 11831 | 13205 | 19615 | 22907 | 3118 | 3291 | 121.7% |
| 2056 | 17910 | 20097 | 29728 | 34980 | 4998 | 5251 | 131.5% |

Totals above are $B, not $T. The audit CSV exposes every increment and matched gross-up. Internal fund grants do not appear as new external resources.

| Household diagnostic, FY2039 annual net $/household | Q1 | Q2 | Q3 | Q4 | Q5 |
| --- | ---: | ---: | ---: | ---: | ---: |
| mixed | 11,663 | 8,094 | 3,245 | -3,923 | -74,783 |
| larger_payroll | 11,591 | 7,878 | 2,861 | -4,165 | -69,899 |
| mixed_larger_credit | 14,522 | 11,359 | 6,729 | -1,877 | -86,345 |

These are approximate quintile averages including modeled benefits, not a D3 certification or guarantees for individual households. See the assumptions and limits in the assessment.

| Fund, mixed case | Result |
| --- | --- |
| Education | Depletion: None; terminal reserve/outlays 6.71; rising: True |
| Combined OASDI | Depletion: 2093; conservative model solvency: False; actuarial balance -0.31% payroll |
| HI | Depletion: 2037; terminal reserve/cost -11.35; rising: False |
| Leave, high take-up | No Treasury loan (peak $0.0B); terminal loan $0.0B |

Combined OASDI has modeled depletion in 2093; its reserve/cost ratio moves from -10.9% in 2095 to -58.0% in 2100. The final-period decline is 47.17 percentage points: the unchanged maximum-decline test of 0.5 points fails. Sustainability also requires no depletion and a terminal ratio of at least 100%. Actuarial balance: -0.311% of payroll. SSA administration is charged to OASDI in this case.

OASI/DI legal separation, the HI annual-data calibration, HTF beyond 2046, and long-run category/cash mappings remain unresolved. A positive balance in one fund cannot fund a second account without legislation.
