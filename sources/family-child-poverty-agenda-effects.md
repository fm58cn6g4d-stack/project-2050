# Child poverty under Project 2050: completed conditional agenda analysis

> Historical pre-adoption experiment: FAM-1A and 400,000 new voucher awards. Espen subsequently adopted FAM-1D/AFA and one million awards. Use [current selected-package comparisons](family-comparison-model-checks.md) and the [adoption bridge](family-adoption-architecture-bridge.md) for current policy; the results below retain their original assumptions.

October 24, 2026. Source branch claude/pensive-mendel-g1lwl5 at df2911d1ae101d6dd73a3c694c8c6874a07433af. This report records a completed static scenario analysis, not a forecast of the poverty rate in 2030 or 2034 and not a change to adopted policy.

The modeled package materially reduces child poverty and deep poverty. FAM-1A supplies most of the early reduction; mature food assistance and scarce housing assistance add to it. Full modeled receipt still leaves substantial poverty. Better delivery matters, but the tested delivery improvements alone do not eliminate the remaining gap.

## Main results

The observed source-year child SPM baseline is 13.39%. Ages and family relationships come from the 2026 CPS ASEC; resources refer to 2025. The 2030/2034 labels select policy phasing, price conventions and optional demographic growth ratios, with source-year net resources held in 2025 purchasing power. Future tax/transfer law is not comprehensively forecast. Counts use the CPS-anchored population scenarios rather than CBO's absolute Social Security-area totals.

| Phasing year | Conditional delivery case | Same-scenario baseline | After modeled policies | Deep poverty after | Net fewer poor children |
| --- | --- | ---: | ---: | ---: | ---: |
| 2030 | Stressed | 13.39% | 11.08% | 2.57% | 1.60 million |
| 2030 | Moderate | 13.39% | 10.61% | 2.40% | 1.92 million |
| 2030 | Enhanced | 13.39% | 10.36% | 2.32% | 2.10 million |
| 2030 | Full | 13.39% | 10.17% | 2.27% | 2.23 million |
| 2034 | Stressed | 13.40% | 10.80% | 2.47% | 1.74 million |
| 2034 | Moderate | 13.40% | 10.29% | 2.28% | 2.08 million |
| 2034 | Enhanced | 13.40% | 10.03% | 2.19% | 2.25 million |
| 2034 | Full | 13.40% | 9.87% | 2.13% | 2.36 million |

Stressed, moderate, enhanced and full are analyst assumptions, not measured program-performance estimates, forecast percentiles or confidence bounds. Moderate assumes a 95% conditional coverage share, 95% annual receipt of the incremental CTC, 50%/75% usable care access and 60%/85% pre-K access in 2030/2034, 90% food receipt and 65% voucher lease-up. Full means complete modeled coverage/receipt/access within income rules, the stated food calendar and the voucher award cap; it does not give every eligible renter a voucher. Conditional coverage is an aggregate family-level research convention, not imputed SSN/ITIN status. The main construction leaves the 327 children without a positive Census claimant pointer without a new credit; their proxy inclusion is a separate sensitivity.

The main dollar convention sets the $3,600/$3,000 child credit in 2030 nominal dollars and indexes it thereafter. A coequal sensitivity indexes those amounts from 2025. Neither convention is silently adopted as a legal drafting decision. First-stage increase thresholds follow the 2021 filing-status levels; the retained credit uses the recorded CBO parameter vintage. The age-17 layer is separately branched. Interview ages proxy for tax-year ages because exact birthdays are unavailable; the Census claimant pointer is not proof of legal qualifying-child status. Actual source-year credits remain in baseline resources. Receipt applies to the net expansion, preserving baseline credits; this is the explicit increment-only convention, not a model of replacement, reconciliation or repayment losses. Source nonrefundable CTC includes ODC; the main offset subtracts the entire observed combined amount before computing an increment, while the ODC sensitivity retains the maximum possible adult-dependent portion.

## How the channels interact

Each row recomputes poverty jointly after adding the next channel to the same families. These are order-dependent cumulative comparisons, not independent effects to add together.

| Year | Cumulative policy channels, moderate delivery | Child poverty | Deep poverty |
| --- | --- | ---: | ---: |
| 2030 | CTC | 10.85% | 2.45% |
| 2030 | CTC + care/pre-K | 10.71% | 2.43% |
| 2030 | + school/summer food | 10.60% | 2.41% |
| 2030 | + scarce vouchers | 10.57% | 2.40% |
| 2030 | + employee leave contribution | 10.61% | 2.40% |
| 2034 | CTC | 10.86% | 2.45% |
| 2034 | CTC + care/pre-K | 10.70% | 2.40% |
| 2034 | + school/summer food | 10.36% | 2.32% |
| 2034 | + scarce vouchers | 10.23% | 2.28% |
| 2034 | + employee leave contribution | 10.29% | 2.28% |

FAM-2A reduces the actual capped work/care deduction. Pre-K and care share the same expense pool, so one saved dollar cannot be counted twice. Monetary gains are limited for families reporting no paid care, even when access to a new service could improve their lives or employment. Care eligibility uses state weighted medians for four-person CPS SPM units and an explicit size adjustment; these are proxies rather than administrative state median income determinations. Usable services and the pre-K share of paid expenses are assumptions varied in the results.

Food gains are net of baseline lunch and Summer EBT values. The empirical modal annual free-lunch value is $861 per school-age child in the source data. School-age counts proxy for enrollment. The main 2030 case credits 80/179 of annual school-lunch gains and no Summer EBT increase, consistent with a conservative fall-2030 launch convention; a full-year food case is also reported. Three summer months, the $60 monthly policy amount and a source-year 185%-FPG/direct-certification eligibility proxy determine the mature summer increment. Existing summer payments are deducted before adding the new amount. Some summer EBT is embedded in school-lunch values and some may be reported with SNAP. Breakfast is beneficial but receives no value under the Census SPM method, so no breakfast dollars are inserted here.

HOU-4A awards are capped at 100,000 households in 2030 and 400,000 in 2034. Allocation includes adult-only households and separates award from lease-up. The code integrates discrete recipient/nonrecipient poverty outcomes; it does not spread an average subsidy across every renter. The income/waitlist proxy and housing-need cap remain uncertain, and no construction capital becomes family cash. HOU-1 has no automatic primary cash value because its household-cash/construction split is unsized; the explicit temporary-cash sensitivity expires after 2031.

The employee paid-leave contribution is included as a cost-side stress at 0.3% of wage income. Leave benefits are not assigned without an observed leave event. The higher employee rate and full employer wage incidence are separately varied. This is a conservative cost-side inclusion, not a net evaluation of paid leave.

## Uncertainty and broader agenda channels

| One-at-a-time change from moderate case | 2030 child poverty | 2034 child poverty |
| --- | ---: | ---: |
| Index benefits from 2025 instead of 2030 | 10.10% | 9.69% |
| Baseline resources lower by 5% of threshold | 12.32% | 11.88% |
| Baseline resources higher by 5% of threshold | 9.13% | 8.75% |
| Same coverage gap concentrated in lowest-resource quarter | 11.01% | 10.67% |
| Retain maximum possible adult-dependent ODC | 10.59% | 10.24% |
| Employer leave contribution fully borne in wages | 10.72% | 10.33% |
| Add adult climate dividend and consumer-cost proxy | 10.52% | 10.12% |
| Add carbon proxy and 15% reduction in actual MOOP | 10.23% | 9.84% |
| Add carbon proxy and 30% reduction in actual MOOP | 9.97% | 9.56% |
| Assume $10B temporary household cash, separate from construction | 10.37% | 10.29% |

The resource-adequacy cases shift each unit's baseline resources by plus or minus 5% of its SPM threshold. Their baselines change as well; the displayed after-policy rates are not measured against an unchanged 13.4% baseline. They are stresses, not economic predictions. Coverage concentration puts the same total gap in the lowest-resource quarter, without assigning legal status to observed families. The full result file also varies SMI, pre-K expense allocation, age 17, unresolved claimants, food timing, population weighting and the automatic leave contribution ceiling.

The carbon extension takes both sides of CLI-2A/REV-C1 from the existing project carbon model: adult-only dividends and consumer-price costs. Source-year household income quintiles and a carbon-price scaling rule provide a reduced-form proxy; these are not observed household energy bills. Health cases reduce actual SPM medical out-of-pocket expenses by 15% or 30%; those percentages are sensitivities, not calibrated estimates of the health bill's effects. Joint carbon/health cases are recomputed rather than obtained by adding separate poverty reductions.

The main estimate covers the child-policy channels above. It is not the entire Project 2050 household effect: health coverage and quality, leave benefits, wage and employment changes, other taxes and transfers, public services, housing supply, inflation and long-run child development remain outside the quantified headline. The existing household-incidence and fiscal generators remain the D3/D4 checks. No SPM resource gain or child-weighted poverty gap is presented as a federal budget cost or social value.

All 160 replicate weights are retained, and paired policy changes use the same replicate weights as their baseline. For moderate delivery, the conditional 95% sampling intervals for the poverty-rate reduction are 2.47–3.09 points in 2030 and 2.78–3.44 points in 2034. Sampling intervals exclude uncertainty in legal rules, receipt, proxies, allocation and future conditions. The wider scenario and sensitivity comparisons must be read alongside them. No employment response is credited in the primary runs.

## Who remains poor

In the moderate 2034 case, about 6.87 million children remain poor and 1.52 million remain deeply poor. About 6.59 million would remain poor even with full modeled coverage and receipt at the same benefit levels and scarce-voucher limits. The difference is a scenario comparison, not a causal attribution: fixed exclusions, proxy choices and unmodeled channels also remain in that full case.

| Overlapping family characteristic, 2034 moderate | Poverty rate within group | Share of remaining poor children |
| --- | ---: | ---: |
| No positive earnings | 62.66% | 27.04% |
| Positive earnings | 7.86% | 72.96% |
| Multiple/no adults | 8.26% | 68.68% |
| One adult | 22.25% | 31.32% |
| Owner/other | 5.38% | 35.14% |
| Renter | 20.36% | 64.86% |
| Asian non-Hispanic head | 9.44% | 3.33% |
| Black non-Hispanic head | 15.70% | 21.56% |
| Hispanic head | 16.81% | 39.20% |
| Other non-Hispanic head | 8.86% | 6.10% |
| White non-Hispanic head | 5.99% | 29.80% |

These rows overlap across categories and must not be added. Race/ethnicity refers to the SPM unit head, not the child's own identity. No subgroup below 30 sample children is published as a rate. Low-earnings families have the highest risk, but most remaining poor children live in units with positive earnings. Renters also account for a disproportionate share. Those patterns argue for examining income adequacy, reliable work, housing and health costs alongside delivery, rather than interpreting the residual as a single eligibility or employment problem.

## Verification, sources and reproduction

The source baseline reproduces the previously verified 13.3913% child SPM rate. All person/replicate keys match. Source-year SPM resources and refundable tax amounts reconcile as recorded in the preceding audit. The matched element-removal comparator finds that EITC plus refundable ACTC lifts 6.14 million people, including 3.25 million children, out of poverty in the public-use data. Census publishes rounded internal-file figures of 6.1 million and 3.3 million. Both pass predeclared public-use/internal tolerances; no weights or benefits were adjusted to pass them. This validates source-year accounting, not the Project's assumed delivery or future effects.

The suite passes 102 tests, including nonlinear receipt-mixture, household award-cap, shared-care, claimant-link, credit-boundary and temporary-aid checks. The empirical checker additionally verifies all eight main cases, 42 sensitivities, population/count identities, paired changes, stage monotonicity and the end of temporary aid. An average income gain is never substituted for the recipient/nonrecipient poverty mixture.

Run from the repository root:

```bash
python3 index/tools/child-poverty/run_validation.py
python3 index/tools/child-poverty/agenda_analysis.py --archive /path/to/asecpub26csv.zip --output index/tools/child-poverty/empirical/agenda-results.json
python3 index/tools/child-poverty/check_agenda_results.py --results index/tools/child-poverty/empirical/agenda-results.json
python3 index/tools/child-poverty/report_agenda.py --results index/tools/child-poverty/empirical/agenda-results.json --markdown sources/family-child-poverty-agenda-effects.md --html index/child-poverty-agenda-analysis.html
```

The assumptions file names every research convention and its basis. The result file records the official archive hash, assumptions hash and official input-subset hashes. The package manifest supplies code/output integrity hashes. The source data remain outside Git; the official archive URL is recorded in the baseline report.

Primary references: [Census 2025 poverty report](https://www2.census.gov/library/publications/2026/demo/p60-290.pdf), [Census SPM technical documentation](https://www2.census.gov/programs-surveys/supplemental-poverty-measure/datasets/spm/spm_techdoc.pdf), [2026 ASEC dictionary](https://www2.census.gov/programs-surveys/cps/datasets/2026/march/asec2026_ddl_pub_full.pdf), [2025 HHS poverty guidelines](https://public-inspection.federalregister.gov/2025-01377.pdf), and [CBO official machine-readable data](https://www.cbo.gov/data/budget-economic-data). Project policy authority is the governing document and canonical FAM, EDU and HOU files; the carbon extension uses index/climate-carbon-model.md.

The four child-poverty report exports were available locally. The attached bibliography again returned no readable content, and its saved-file download failed; it was not treated as evidence. The analysis implements Espen's direction to complete bounded agenda scenarios without overbuilding a speculative target-year current-law forecast. It adopts no new policy, eligibility rule or poverty target.
