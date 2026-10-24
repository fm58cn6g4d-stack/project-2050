# Child-poverty minimum empirical validation specification

October 24, 2026. Companion to family-child-poverty-rebuild-findings-and-integration.md. This is a research specification, not adopted eligibility, an entitlement or a poverty target.

1. Name the exact CPS ASEC/SPM survey vintage, income reference year, file version, public-use coverage and revision status. Retain the original file hashes and code/mapping versions.
2. Preserve individual person weights and all 160 appropriate replicate weights. Keep SPM unit weights distinct. Verify the actual CSV weight scale; do not infer it from an earlier ASCII layout.
3. Preserve Census SPM_ID as text. Namespace tax IDs by household, audit claimant/dependent allocation and reject unresolved tax units spanning resource-sharing units. Missing identification or nonfiler assignments require an explicit audited treatment.
4. Reproduce a named source-year child-SPM population, poor-child count and rate. Use a predeclared tolerance with a public-use/internal-file rationale. Do not substitute official poverty, the overall SPM rate, or another year. Census reports 2025 child SPM and official+ child rates both rounded to 13.4%, so the value itself does not identify the measure.
5. Preserve a reproducible public-use baseline and separately label any benefit-underreporting/administrative alignment. Do not calibrate away unexplained accounting errors.
6. Build independently reviewed post-2025-law baselines for 2030 and a mature-service comparison such as 2034. Document population controls, demographic assumptions, taxes/transfers, actual current-law credits, SPM thresholds and dollar-year conversions.
7. Specify or branch FAM-1's exact amounts/indexing, phaseout layers, age 17, claimant/spouse/child identification, residency, territory, custody, updating, reconciliation and repayment protection. Receipt and legal coverage are separate.
8. Calibrate annual receipt, month of receipt and on-time payment by subgroup. A catch-up payment may restore annual income without repairing a hardship experienced earlier.
9. Estimate FAM-2 paid-care and pre-K savings jointly, conditional on compatible usable services. Recompute the capped SPM expense deduction; uncapped paid care is not automatically an SPM gain.
10. Value incremental school/summer food net of current-law benefits, by actual enrollment/receipt and covered months. Allocate scarce voucher awards as household awards, check the 2030–33 phase-in and lease-up, and respect SPM housing valuation. Exclude construction authority and unspent capacity money from immediate income.
11. Report person-weighted child poverty, deep poverty, below-150% and near-only rates/counts; child-weighted gaps and separately unit-weighted gaps; subgroup cells and coverage limits; sampling uncertainty and parameter sensitivities. Recompute paired policy differences under the same replicate weights.
12. Report overlapping residual mechanisms and a declared ordered presentation for delivered-poor children. Child-specific exclusion cannot be assigned to eligible siblings. Neither overlapping flags nor separate policy percentages are additive.
13. Recreate at least one external comparator after matching its population, law, policy, receipt and employment assumptions. The National Academies' 2018 baseline is not a 2030 post-2025-law baseline.
14. Keep no-employment-response results separate from supported behavioral cases with joint tax/transfer/expense recomputation. Do not monetize hardship or long-run child development as immediate SPM resources.
15. Before a full-project claim, include other adopted household taxes/transfers, climate dividends and health/work/care interactions. Reconcile fiscal volumes through the existing input tables and generators; no dynamic revenue is inserted into D4.

**Publication status at this checkpoint:** artificial logic tests passed; real-data baseline, projections, legal review, calibrated delivery, external-comparator reproduction and full-package integration remain pending. A completed source-year calibration would be an empirical milestone, not permission to adopt a new policy.
