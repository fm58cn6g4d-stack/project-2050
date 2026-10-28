# Child-poverty target-year preparation: tax links, parameters and projection limits

October 24, 2026. Technical research addition based on claude/pensive-mendel-g1lwl5 at bef6a77624e76bdee28ad2ce7888872127ac3984. No change to adopted policy or fiscal inputs.

The verified CPS baseline now has a reproducible audit of its tax and claimant links, official 2030/2034 tax parameters, a bounded current-law credit worksheet, and two demographic sensitivity runs. This advances the target-year baseline but does not complete it. A national current-law poverty forecast requires recomputing income, taxes, transfers, expenses and thresholds together. Applying one inflation factor to net resources would conceal those interactions.

## What the data establish

The 2026 ASEC archive contains 134,729 people, including 31,444 children, in 55,401 SPM units and 72,979 household-namespaced Census tax-unit keys. Every repeated SPM component agrees within its unit. The documented resource identity reproduces every unit's resources exactly. Summed person-level ACTC, EITC and after-credit federal taxes each equal their SPM-unit counterpart exactly. No tax unit spans two SPM units.

These checks establish accounting consistency within the Census public-use tax model; they do not independently validate its behavioral, reporting or legal assumptions.

Two distinctions matter for the policy overlay. First, Census's CTC_CRD combines the nonrefundable child credit and credit for other dependents. It cannot be imported wholesale as the child credit that a reform replaces. Second, SPM_FEDTAX already incorporates refundable credits. Adding ACTC or EITC to resources again would count them twice. The [Census dictionary](https://www2.census.gov/programs-surveys/cps/datasets/2026/march/asec2026_ddl_pub_full.pdf) and [SPM README](https://www2.census.gov/programs-surveys/supplemental-poverty-measure/datasets/spm/readme.pdf) document these fields.

DEP_STAT is a household line-number pointer to the filer claiming a dependent. All 36,346 positive pointers resolve. Of these dependents, 171 have a different own-return TAX_ID from their claimant; 141 are children. This can occur when a dependent files a separate return. The adapter therefore exports separate own-return and claimant-return fields. It does not overwrite one with the other. Another 327 children have no positive claimant pointer; their claimant remains unresolved. These are unweighted record counts, not national eligibility estimates. Observed pointers do not prove statutory support, residence, tax-year age or SSN/ITIN eligibility.

## Official target-year inputs

[CBO identifies US-CBO/cbo-data as its official machine-readable repository](https://www.cbo.gov/data/budget-economic-data). The committed extracts preserve selected source rows, with immutable full-source Git blob hashes and subset SHA-256 hashes. Economic inputs use calendar years rather than the project's existing fiscal-year series.

| CBO February 2026 parameter vintage | 2025 | 2030 | 2034 |
| --- | ---: | ---: | ---: |
| Maximum CTC per qualifying child | $2,200 | $2,400 | $2,600 |
| Maximum refundable ACTC per qualifying child | $1,700 | $1,900 | $2,100 |
| Credit per eligible other dependent | $500 | $500 | $500 |
| ACTC earned-income threshold | $2,500 | $2,500 | $2,500 |
| ACTC phase-in rate above threshold | 15% | 15% | 15% |

These are sourced parameters in a named forecast vintage. Future indexed amounts are CBO projections, not future IRS announcements. The retrieved [2025 IRS Schedule 8812](https://www.irs.gov/pub/irs-pdf/f1040s8.pdf) supplies the worksheet structure: joint versus other filing-status thresholds, the next-$1,000 phaseout step, a nonrefundable credit limit, earned-income refundability, and the alternative payroll route for certain families with three or more qualifying children.

current_law_ctc.py implements that conditional arithmetic using supplied reviewed eligibility and Worksheet A limits. It refuses missing reviews and unsupported special-return cases. The three-child payroll alternative requires its own reviewed inputs when relevant. It keeps CTC and ODC combined where the form combines them and returns no CTC-only allocation. It does not calculate total federal liability, state taxes, MAGI, legal eligibility or filing behavior. It cannot by itself populate the policy model's current_law_ctc field. The treatment of existing ODC, including age-17 dependents, still requires an explicit policy/tax allocation.

Calendar-year index ratios from 2025 are also recorded: CPI-U rises by factors of 1.1301 and 1.2357 in 2030/2034, while the wage/salary ECI rises by 1.1696 and 1.3137. These help prepare component-specific aging. They are not applied to net SPM resources. Medical expenses have a separate index; the annual-average chained CPI series is not the statutory tax-indexing window. CPI-U alone does not forecast SPM thresholds.

## What the sensitivity runs mean

The two runs apply CBO's single-age/sex child-population growth ratios from 2026 to 2030/2034 to the observed CPS cells. The base year is 2026 because ages are observed in the 2026 survey, while resources refer to 2025. Ages, household composition and real resources remain unchanged. New births and future families are represented only through reweighting observed age cells; no child's age is mechanically advanced.

CBO's Social Security-area population includes people outside the CPS universe. Its absolute totals are therefore not used as CPS controls. The resulting CPS-anchored child counts are approximately 69.17 million and 66.75 million. Poverty rates remain near 13.4% because within-cell resource distributions are deliberately frozen. These figures are labeled demographic sensitivities throughout; they are not current-law forecasts, predictions of policy effects or evidence that future poverty is unchanged.

All 160 replicate weights receive the same fixed external age/sex multiplier as each corresponding base weight. The resulting sampling intervals are conditional on those multipliers. They omit demographic forecast, model and parameter uncertainty. Each of 36 cells is checked against its CPS-anchored ratio target. These output objects are not schema-version-2 policy inputs and cannot be passed directly to the policy engine.

## Reproduce and integrate

From the repository root:

```bash
python3 index/tools/child-poverty/run_validation.py --out build/child-poverty/validation
python3 index/tools/child-poverty/cps_projection.py \
  --archive /path/to/asecpub26csv.zip \
  --output build/child-poverty/cps-target-year-preparation.json \
  --crosswalk-output build/child-poverty/cps-claimant-crosswalk.csv
```

The suite now passes 83 tests, including 21 new credit-boundary, claimant-link and population-accounting checks. The legacy regression, raw ZIP pipeline, policy CLI and 24 artificial scenario rows also pass. The empirical command has been executed on the archived official data; committed results are in index/tools/child-poverty/empirical/cps-target-year-preparation.json.

The next substantive task is a jointly recomputed current-law baseline. It needs an audited claimant/credit crosswalk, source-year tax-model comparison, component income aging, target-year federal and state tax/transfer calculations, SPM threshold and expense paths, and CPS-universe controls with corresponding replicate treatment. Only after that baseline passes should the delivery and policy overlays be attached. Program receipt rates, usable care, meal access and housing awards remain inputs to be estimated, rather than values inferred from appropriations.

The attached bibliography returned no readable text, and its saved-file transfer failed. It was not used as evidence. This step relies on the child-poverty reports already reviewed and the official records linked above. Project governing rules, benefit amounts, fiscal and incidence tables, and common generators are unchanged.

