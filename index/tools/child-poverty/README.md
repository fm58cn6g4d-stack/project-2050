# Child-poverty microsimulation — reconstructed research tool

October 24, 2026. **Logic tested on artificial data; observed CPS source-year baseline verified with all 160 replicate weights; no national Project 2050 policy estimate.** Integration source is `claude/pensive-mendel-g1lwl5` at `4133d157f5d0ab410b19af6212424b67916c09ab` (reconstruction merged through PR #10; original reconstruction source: `14feb987a7d8aec416ba5bacc50880187a756383`). This changes no adopted policy, fiscal input or existing generated output.

This rebuild uses the four local research-report exports, the three preliminary notes, the canonical rule sheet and the surviving GitHub prototype. It does **not** claim to recover the missing ZIP byte for byte. `recovered/model-upstream-8a8f4b.py` preserves the exact surviving source; its SHA-256 is `702c8e45badb933eb59851718a57dfaed7f0164e09a0961c7bdc1b9d88334bb9`.

## Reproduce the verification

Python 3.9 or later, standard library only; verified here with Python 3.12.14. From the repository root:

```bash
python3 index/tools/child-poverty/run_validation.py
```

The runner works from other working directories too. It executes 83 unit/regression tests, demonstrates the original mixed-sibling attribution defect against the exact recovered source, exercises a raw CSV-in-ZIP preprocessing/baseline pipeline and the model CLI, and generates 24 artificial scenario rows: two years × three identification branches × four receipt scenarios. It writes `diagnostics/`, including test results, JSON ledgers, CSV tables and hashes. Everything in `synthetic/` and `diagnostics/` is artificial. Official-data executions are separately recorded in `empirical/`.

The `synthetic/` JSON fixtures are inspectable and reproducible with `python3 index/tools/child-poverty/fixtures.py`. Test receipt/index/reference values are **not** production tax parameters. A full-receipt case does not create a care slot or award a voucher. Enhanced delivery may explicitly add a service that was unavailable under the supplied baseline supply assumptions.

## Run a prepared research case

```bash
python3 index/tools/child-poverty/model.py \
  --data index/tools/child-poverty/synthetic/population.json \
  --policy index/tools/child-poverty/synthetic/policy-2030.json \
  --output build/child-poverty/synthetic-2030.json
```

The replacement input contract is versioned JSON (`schema_version: 2`), documented in [schema.md](schema.md). This deliberately replaces v1's three CSVs rather than silently interpreting old files with new semantics. The recovered v1 script still runs with its own original contract for comparison.

The engine jointly calculates current law, statutory full available receipt, delivered receipt and enhanced delivery for 2030 and 2034. Each runs under three **research** identification branches: claimant/spouse SSN condition with child SSN; adult ITIN with child SSN; and adult/child ITIN inclusion. These are incomplete legal branches, not an assertion that every statutory or territorial rule has been settled.

The amount layer preserves FAM-1A's $3,600 under six and $3,000 ages 6–17, fully refundable. Indexing, retained credit, phaseout threshold indexing, age-17 treatment and receipt basis must be supplied explicitly. The provisional two-stage phaseout is not a complete tax calculator. Current-law CTC is imported from a separately audited baseline; the engine does not substitute the statutory maximum for each family's actual credit.

`replace_credit` subtracts the current-law credit already present in SPM resources and adds the received proposed award; it can show a loss. `increment_only` preserves the baseline credit and delivers only the increment, as v1 did. The latter is an explicit sensitivity convention and refuses statutory losers. Neither convention silently decides the permanent advance-payment/reconciliation architecture.

Monthly fractions describe the year cash arrives, including late catch-up payments. Annual receipt and on-time months are separate. Neither is a model of food insecurity, eviction or monthly poverty.

## Prepare a source-year baseline

The official 2026 ASEC archive (income year 2025) has now been executed using the actual poverty and SDR routines. See [the empirical integration report](../../../sources/family-child-poverty-cps-baseline.md) for input URL/hash, field scaling, checks and limitations; results are in [empirical/cps-2026-baseline.json](empirical/cps-2026-baseline.json). Reproduce from the repository root:

```bash
python3 index/tools/child-poverty/cps_baseline.py \
  --archive /path/to/asecpub26csv.zip --output /path/to/cps-2026-baseline.json
```

This source-specific adapter measures existing SPM resources without inventing missing tax or identification assignments. Its successful join and calibration do not validate the generic policy preprocessor's claimant/tax construction. For a separately reviewed policy-ready input, use the generic pipeline below.

```bash
python3 index/tools/child-poverty/preprocess.py \
  --raw /path/to/cps-person.csv --mapping /path/to/reviewed-field-map.json \
  --replicates /path/to/replicate-weights.csv --output /path/to/source-year.json
python3 index/tools/child-poverty/model.py \
  --data /path/to/source-year.json --baseline-only --output /path/to/baseline.json
python3 index/tools/child-poverty/calibrate.py \
  --data /path/to/source-year.json --benchmark /path/to/reviewed-benchmark.json \
  --output /path/to/comparison.json
```

ZIP inputs are supported. Specify `--member` when more than one CSV is present. Separate replicate files join by explicit household/person keys; ambiguous or incomplete joins fail. `SPM_ID` is preserved as a string, and `TAX_ID` is household-namespaced. Missing tax links and legal identification remain missing; citizenship is never converted to an SSN/ITIN class. Repeated SPM resources/thresholds/weights must agree. Tax units spanning SPM units fail pending an audited allocation.

The production templates intentionally contain nulls. Verify the exact file vintage, weight scaling, replicate column names and unit fields against its documentation. **Do not treat `SPM_CHILDCAREXPNS` as a capped deduction:** Census labels it uncapped; the combined capped field is `SPM_CAPWKCCXPNS`. Person estimates use `MARSUPWT`, not `SPM_WEIGHT`. Retain a named public-use baseline separately from administrative-underreporting adjustments.

Policy overlays add reviewed claimant/dependent assignments, actual current-law tax amounts, identification assumptions and delivery/service inputs. They cannot overwrite the source-year resource/threshold/weight fields. Project the source-year baseline before attaching target-year policy/service overlays. `project.py` imports a complete, externally audited target-year replacement/reweighting ledger and checks population controls. It supplies no invented inflation path, tax projection, cohort aging or demographic weights. Non-synthetic policy runs require the correct target-year/dollar-year and input-review references.

## Target-year preparation

The [target-year preparation report](../../../sources/family-child-poverty-target-year-preparation.md) records the exact source-year tax/SPM reconciliation, separate own-return and dependent-claimant links, official CBO calendar-year and CTC parameter extracts, and two demographic sensitivities. Reproduce the empirical audit and optional claimant crosswalk with:

```bash
python3 index/tools/child-poverty/cps_projection.py \
  --archive /path/to/asecpub26csv.zip \
  --output build/child-poverty/cps-target-year-preparation.json \
  --crosswalk-output build/child-poverty/cps-claimant-crosswalk.csv
```

`current_law_ctc.py` calculates conditional Schedule-8812 arithmetic from reviewed qualifying-dependent counts, earned income, MAGI and Worksheet A limits. It uses CBO's February 2026 parameters; it does not recompute total tax liability or infer eligibility from CPS citizenship/age. Its combined CTC/ODC result must not be imported as CTC alone. Census `CTC_CRD` also combines CTC and ODC, and `SPM_FEDTAX` already includes refundable credits. Census dependent pointers and a dependent's own `TAX_ID` can identify different returns.

The demographic sensitivity holds real resources and within-cell poverty fixed while applying CBO Social Security-area age/sex growth ratios to the CPS sample. It does not use CBO's absolute totals as CPS controls. Its outputs have `policy_ready: false`; they are not policy-engine inputs or complete 2030/2034 current-law forecasts. Income, tax/transfer, threshold, expense and delivery projections remain to be jointly reviewed and supplied.

## Accounting and interpretation

Resources equal current-law resources + CTC replacement/increment + SPM-countable emergency aid + reductions in actual capped expenses + incremental SPM-valued food/housing assistance. Pre-K and care share one expense pool, and their combined SPM gain cannot exceed the corresponding deduction reduction. This assumes unchanged work expenses and earnings cap; a behavioral scenario requires their recomputation.

Meals and Summer EBT enter net of baseline benefits, at SPM value. Voucher effects require an award and lease-up; weighted household awards cannot exceed the adopted cumulative 100,000-per-year phase-in to 400,000. The externally supplied incremental housing cap must already account for baseline assistance. HOU-1 emergency-aid effects require an award and expire after 2031. No construction, loan authority, capacity appropriation or program budget becomes immediate family cash.

Outputs include person-weighted child poverty, deep poverty, below-150% and near-only rates/counts; child-weighted and separately unit-weighted poverty gaps; subgroups with small-cell warnings/rate suppression; payment reliability; unit resource ledgers; and overlapping residual flags. The mutually exclusive ordered attribution partitions **delivered-poor children only**. Legal exclusion is child-specific; resource inadequacy and most service shortages are shared SPM-unit conditions. These are descriptive flags, not a causal decomposition.

The SDR routine recomputes estimates under every supplied replicate weight using `4/R × sum((replicate estimate − full-sample estimate)²)`. It also computes paired policy changes with the same weights. Its intervals cover sampling uncertainty only. The synthetic two-replicate example tests the formula; an actual CPS run requires all 160. National all-child intervals are implemented; subgroup-specific intervals and uncertainty in unit-level fiscal/resource totals are not yet supplied.

Child-weighted gaps repeat a unit's shortfall for each child. They are not a supplement's budget cost. Unit-weighted resource deltas are not federal outlays, scored revenue or social value. The focused model omits other Project taxes/transfers and cannot certify D3 or D4.

## Outstanding publication requirements

Source-year CPS measurement and 160-replicate calibration are complete for the recorded archive. Outstanding: reviewed post-2025 current-law taxes and claimant/SPM identities; 2030/2034 projection and controls; legal eligibility/phaseout/reconciliation review; calibrated payment, usable-care, summer-meal and voucher delivery; administrative-alignment sensitivities; supported employment cases with joint tax/transfer recomputation; a matched external comparator; and whole-package interactions. No Project policy poverty percentage, eradication claim, permanent-policy cost or new policy selection follows from the source-year baseline or artificial tests.

See `sources/family-child-poverty-rebuild-findings-and-integration.md` for recovery findings, policy decisions needed and the staged integration plan. `run-all.sh` is intentionally unchanged: national runs must remain separate from the existing fiscal and quintile tools until the empirical inputs are validated.

Create a reproducible standalone bundle with `python3 index/tools/child-poverty/package.py --out /path/to/rebuilt-model.zip`. The ZIP includes tests, diagnostics, provenance and a SHA-256 manifest.
