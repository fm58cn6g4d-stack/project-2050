# Version 2 input contract

All amounts are annual dollars of `metadata.dollar_year`. JSON numbers must be finite. Identifiers are strings, booleans are actual JSON booleans, and missing assumptions are errors rather than full-receipt defaults. Raw column mappings and policy overlays are distinct.

| Object | Required fields | Meaning |
| --- | --- | --- |
| Root | `schema_version: 2`, `metadata`, `units`, `taxes`, `people` | Arrays of unique ID records |
| Metadata | `kind`, `source_vintage`, `resource_year`, `dollar_year`, `baseline_description`, `weight_basis` | Kind is synthetic, source_year or projected. Non-synthetic policy runs also require references for target-year baseline, tax crosswalk and service valuation review. |
| SPM unit, baseline | `spm_unit_id`, `resources`, `threshold`, `unit_weight` | Existing net SPM resources and threshold, not pretax cash; a baseline-only run needs only these. |
| Person, baseline | `person_id`, `spm_unit_id`, `age`, `person_weight` | Person weights are used for child estimates. Optional `replicate_weights` must have identical dimensions across all people: zero or 160 for real CPS. |
| Person, policy | `tax_unit_id`, `child_id`, `qualifying_child` | Required for children under 18. Child ID is ssn/itin/other; the non-ID qualifying-child flag covers independently reviewed residency/dependency/etc. rules. It does not derive those rules. |
| Tax unit, policy | `tax_unit_id`, `spm_unit_id`, `agi`, `filing_status`, `claimant_ids`, `current_law_ctc`, `receipt`, `on_time_months` | Filing status joint/head/other; one claimant ID for nonjoint, two for joint. Current-law CTC includes the actual CTC/ACTC already reflected in baseline resources, without ODC or duplicated joint-return amounts. |
| Receipt | `delivered` and `enhanced`: arrays of 12 fractions | Each is a fraction of the annual award received that month; total ≤1. A late payment can be >1/12. Full receipt uses 1/12 per month; `on_time_months` is separately observed/assumed, 0–12. |
| SPM unit, care | `childcare_expense`, `work_expense`, `work_care_deduction`, `care_family_income`, `state_median_income`, `care_need_eligible` | Expenses before and after the combined earnings cap. Care income is the applicable care-family income, not automatically tax AGI or SPM cash. State median must be family-size-adjusted and positive where relevant. |
| SPM unit, pre-K | `prek_eligible`, `prek_spm_reduction` | Field name retained as a concise input label: it is the potential reduction in paid care expenses **before** recomputing the combined SPM cap. It is not added as cash. Eligibility needs a child aged 3 or 4. |
| SPM unit, food | `school_meal_spm_delta`, `summer_ebt_spm_delta` | Potential incremental SPM value net of current-law benefits, under explicitly reviewed timing/coverage assumptions. |
| SPM unit, housing | `voucher_eligible`, `voucher_awarded`, `voucher_spm_delta`, `housing_increment_cap`, `emergency_aid_eligible`, `emergency_aid_awarded`, `emergency_aid_spm_delta` | Award, lease-up and capped incremental value are separate. HOU-1 is temporary. Housing costs and new construction are not these delta fields. |
| SPM unit, access | `delivery.full_receipt`, `delivery.delivered`, `delivery.enhanced` | Each supplies six booleans: care, prek, school_meal, summer_ebt, voucher, emergency_aid. Care/pre-K mean usable access; voucher means successful lease-up given award. Full available receipt must include each delivered service; enhanced may add explicitly modeled access. |
| Person, optional | `subgroups` | family_structure, earnings_band, disability, identification, race_ethnicity, geography, tenure. Missing categories display not_recorded; age group and SPM unit size are calculated. |

The minimum policy record requires `year` (2030 or 2034), `policy_status: research_only`, positive `policy_index` and `phaseout_threshold_index`, `reference_under17`, `reference_age17`, `age17_layer` (expansion_only/retained_reference), `receipt_basis` (replace_credit/increment_only), `min_cell` and documented parameter provenance. Real subgroup tables require a minimum cell of at least 30.

`templates/` are unresolved production forms. `synthetic/` are artificial worked examples. Neither constitutes a calibrated population or a reviewed statutory rule sheet.

## Care arithmetic

Let C be uncapped paid care, W uncapped work expense, D the combined SPM deduction already in baseline resources, P actual pre-K savings and A additional care savings. Under a fixed earnings cap and work expense:

`new deduction = min(D, W + C − P − A)`

`SPM expense gain = D − new deduction`

Pre-K is applied first for component reporting; care applies to the remaining paid-care expense and the applicable income cap. The total result is joint. Different operational interpretations of the family copayment or preschool/wraparound cost need new explicit parameters and review.

## Preprocessing and projection boundaries

The field-map constructor preserves source-year Census SPM totals, exact SPM IDs, household-namespaced tax IDs, person weights and keyed replicate weights. Tax observations are retained, not automatically summed into a return. Unassigned tax children need an audited overlay, including explicit additional nonfiler/kinship units if appropriate.

The projection adapter requires every existing unit/person/tax ID in an externally prepared replacement ledger, new base and replicate weights, AGI and actual current-law credit, source references and population controls. It leaves observed ages and family structure fixed; it is a reweighted cross-section adapter, not a cohort demographic model. Births, new families or alternative demographic constructions require a complete new population file.

An audited policy overlay may provide a `reviews` object with nonempty `tax_unit_crosswalk_review` and `service_valuation_review` reference strings. These are analyst-supplied review citations, not a certification performed by the constructor. Baseline totals remain protected.

The 2026 CPS audit confirms that `DEP_STAT` points to the claiming filer's `A_LINENO`. A dependent's own `TAX_ID` can differ from that claimant's tax unit. The optional `cps_projection.py --crosswalk-output` CSV preserves both, leaves missing claimant pointers unresolved and does not establish legal eligibility. `CTC_CRD` combines nonrefundable CTC and ODC; it cannot be imported as CTC alone. Refundable credits are already incorporated in `SPM_FEDTAX` and must not be added a second time.

The separate `current_law_ctc.calculate` worksheet accepts reviewed qualifying-child/other-dependent counts, MAGI, earned income and a credit-limit worksheet result. It reports combined nonrefundable CTC/ODC and ACTC, with no inferred CTC-only allocation. Its parameters and method are documented in `sources/family-child-poverty-target-year-preparation.md`. The demographic sensitivity output is deliberately outside this population schema and sets `policy_ready: false`; age/sex reweighting alone cannot supply target-year net resources or current-law taxes.
