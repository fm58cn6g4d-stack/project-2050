# Child-poverty source-year CPS baseline: empirical integration

October 24, 2026. Source branch claude/pensive-mendel-g1lwl5 at 4133d157f5d0ab410b19af6212424b67916c09ab. No adopted policy, target-year population or fiscal parameter changes.

The official 2026 CPS ASEC archive was downloaded and executed against the rebuilt tool's poverty and replicate-variance routines. This clears a source-year measurement milestone. It does not establish a 2030/2034 policy baseline or a Project 2050 poverty effect.

## Data and reproducibility

Official landing page: https://www.census.gov/data/datasets/2026/demo/cps/cps-asec-2026.html

Official archive: https://www2.census.gov/programs-surveys/cps/datasets/2026/march/asecpub26csv.zip

Archive SHA-256: fe819d0d2fc4470c282e76c247b8aa8b6054811619730307e9f2fe6186707d93

The archive contains household, family and person CSVs plus asec_csv_repwgt_2026.csv. The person records carry FILEDATE 72726. Survey year is 2026; income/resource reference year is 2025. Large raw public-use files remain outside Git; the official URL and hash identify the exact input.

Run from the repository root:
```bash
python3 index/tools/child-poverty/cps_baseline.py --archive /path/to/asecpub26csv.zip --output /path/to/cps-2026-baseline.json
```

The adapter reads pppub26.csv and the included replicate-weight CSV directly from the archive. Join keys are PH_SEQ / h_seq and PPPOS, not row order or P_SEQ. MARSUPWT has two implied decimals and is divided by 100; pwwgt0 and pwwgt1–160 already contain decimal weights. The precise pwwgt0 estimate centers SDR sampling variance; rounded MARSUPWT point estimates are also reported. No SSN/ITIN, tax-claimant, service or receipt assignments are invented.

Documentation: [2026 dictionary](https://www2.census.gov/programs-surveys/cps/datasets/2026/march/asec2026_ddl_pub_full.pdf), [person layout](https://www2.census.gov/programs-surveys/cps/datasets/2026/march/persfmt.txt), [SPM methods and public-use replication checks](https://www2.census.gov/programs-surveys/supplemental-poverty-measure/datasets/spm/readme.pdf).

## Results

| Check or measure | Observed result |
| --- | --- |
| Person records / replicate records | 134,729 / 134,729 |
| Complete one-to-one keyed join | Yes |
| Nonpositive-threshold exclusions | 0 |
| Calculated SPM status versus supplied SPM_POOR | 0 disagreements |
| All-age unweighted poor | 16,941; matches Census README |
| All-age weighted poor | 44,390,216.71; rounds to Census README's 44,390 thousand |
| Weighted child population | 72,082,589.85 |
| Weighted poor children | 9,652,806.50 |
| Child SPM poverty | 13.3913%; reproduces the published 13.4% rounding |
| Child deep poverty, below 50% of threshold | 3.4447% |
| Children below 150% of threshold, including poor children | 32.5302% |
| Child-poverty sampling SE | 0.3425 percentage points |
| Normal-approximation 95% sampling interval | 12.7200%–14.0626% |

Full results are in index/tools/child-poverty/empirical/cps-2026-baseline.json. Child-gap dollar totals repeat the family gap for each child and are not budget costs.

The script fails on duplicate or unmatched join keys, supplied-status disagreement, the named all-age public-use replication-check failure, or failure to reproduce the declared rounded child benchmark (13.35% to less than 13.45%). It does not adjust weights to make the checks pass. Public-use and internal-file estimates are distinct; the public-use count identity and rounded published child-rate check are reported separately.

## Integration boundaries and next assignment

This empirical adapter deliberately evaluates source-year resource/threshold identities without requiring an unresolved tax-unit or policy overlay. It is additional evidence for the actual poverty/SDR routines, not proof that the generic policy preprocessor's tax/claimant construction is nationally validated. All 160 replicate columns are used. Sampling intervals exclude model, underreporting and policy-parameter uncertainty.

The source-year data can now support development of the 2030/2034 current-law counterfactual, with explicit population controls, taxes/transfers and threshold paths. Tax claimant/dependent reconciliation and identification assumptions, program delivery, administrative-underreporting alignment and behavioral sensitivities remain open. Actual child-care expense caps and scarce housing awards must still be audited when policy deltas are attached. Other project household taxes/transfers remain necessary before any whole-package claim.

The 62 existing logic tests remain the regression suite. The new empirical execution adds keyed-join, published-status and external-count/rounded-rate checks. The fiscal and incidence input tables, adopted benefit rules and common generator scripts are unchanged.

