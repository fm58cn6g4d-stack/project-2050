# Child-poverty microsimulation v1 — research prototype

**Status:** unvalidated prototype; no Project 2050 child-poverty estimate has been produced. This folder is intentionally separate from the existing quintile incidence model and `run-all.sh`. It does not change canonical policy, fiscal inputs, generated outputs or the approved decisions.

## Purpose and inputs

Run `model.py` against three **analyst-prepared, de-identified** CSV tables. The engine requires a separately constructed post-2025-law CPS ASEC/SPM baseline, including survey calibration/aging to 2030 or 2034, SPM unit composition and threshold by geography/tenure, tax-unit reconciliation, current-law tax/credit estimates, underreporting corrections, and survey weights. It **cannot** ingest raw CPS ASEC files directly or derive these fields itself. Obtain a licensed microdata workflow or use public CPS ASEC with documented access and reproducible preprocessing; do not publish estimates until that pipeline exists.

Required fields:

- `units.csv`: `spm_unit_id,weight,spm_threshold,spm_resources,spm_care_expense,care_family_income,state_median_income,care_slot,care_delivered,care_enhanced,prek_spm_delta,prek_delivered,prek_enhanced,school_meal_spm_delta,school_meal_delivered,school_meal_enhanced,summer_ebt_spm_delta,summer_ebt_delivered,summer_ebt_enhanced,voucher_awarded,voucher_spm_delta,voucher_leaseup_delivered,voucher_leaseup_enhanced,emergency_aid_spm_delta,emergency_aid_delivered,emergency_aid_enhanced`.
- `taxes.csv`: `tax_unit_id,spm_unit_id,agi,filing_status,adult_id,current_law_ctc,months_delivered,months_enhanced`. Filing status: `joint`, `head`, `other`; identification: `ssn`, `itin`, `other`. CTC months 0–12.
- `people.csv`: `person_id,spm_unit_id,tax_unit_id,age,child_id`; optional subgroup fields: `family_structure,earnings_band,disability,identification,race_ethnicity,geography,tenure`. Every child must map to a tax unit within its SPM unit. Children are people under 18. Subgroups missing from the extract display as `not_recorded`.

All dollar amounts are **annual dollars of the target year**. `spm_resources` is the *current-law* SPM unit's resources **after** taxes/credits, noncash benefits and SPM expenses. `current_law_ctc` is the current-law credit already included in those resources. All `*_spm_delta` fields must be *incremental changes to SPM resources*, not program spending, face-value benefits or household consumption; their calculation must be documented externally and checked for overlap. `weight` is the SPM unit's household weight; it is replicated once per child for child headcounts. Voucher award and lease-up are separate. Construction and capacity grants must not be counted as immediate cash.

## Example invocation

```bash
python3 models/tools/child-poverty/model.py \
  --units /path/to/units.csv --taxes /path/to/taxes.csv \
  --people /path/to/people.csv --year 2030 \
  --vintage 'CPS ASEC 2026, analyst extract v1 aged to 2030' \
  --policy-index 1.0 --reference-under17 2200 --reference-age17 2200 \
  --output /path/to/results.json
```

**The reference and index numbers in this command are illustrations only**, not validated statutory parameters for 2030. The operator must specify the dollar base year, index factor and first-phaseout reference from an independently reviewed legal/tax specification. The two-stage phaseout implementation is explicitly provisional. Do not use the example invocation to claim a rate or fiscal score.

## Scenarios and outputs

The engine jointly evaluates `current_law`, `full_receipt`, `delivered`, `enhanced` under three **research-only** identification branches: `ssn_only`, `adult_itin`, `adult_and_child_itin`. They are sensitivity branches, not adopted eligibility. `full_receipt` sets receipt to 100% **for eligible persons and recorded service slots/awards only**; it cannot make a legally excluded child eligible, invent a care slot or award a voucher. Delivered/enhanced receipt months and service flags are supplied by the analyst, not generated from a uniform take-up rate.

The model reports child SPM poverty, deep poverty, below-150%-of-threshold, child-weighted poverty-gap dollars, a distinct SPM-unit-weighted gap, subgroup tables, and overlap/ordered mechanism flags. The child-weighted gap repeats the same SPM unit shortfall for each child; **do not present it as a budgetary cost or add it to the unit-weighted gap**. Mechanism attribution is descriptive and overlaps; ordered counts depend on ordering.

## Critical limitations before a published estimate

1. **Tax calculation** is provisional. It does not resolve the 2025-law eligibility rules, 17-year-old reference, residency, phaseout interactions, family splitting, custody, nonfilers, or recapture. It treats the policy credit as a positive increment over a supplied current-law CTC. That cannot identify losers or reconcile complex tax-unit changes. Tax units crossing SPM units are rejected.
2. **FAM-2A** is represented through a simplified 7%-cap / under-75%-of-state-median-income calculation, usable slots and a separate pre-K delta. Care expenses are capped only when a slot is flagged. Analysts must separately model supply, age, hours, quality, disability access, state/Tribal participation, and care-induced employment responses.
3. **EDU-3A** meal and summer EBT SPM effects are *externally prepared*, not equivalent to the face value of meals or the full `$60` benefit. School-year timing, summer eligibility and SPM valuation require independent computation.
4. **HOU-1A / HOU-4A** are externally assigned and SPM-valued. The engine does not allocate the 400,000 incremental vouchers, select households, model waitlists, fair-market rents, or enforce the aggregate 2030–33 phase-in. These must be constructed and checked before any national estimate.
5. **Whole-package incidence** is absent: other taxes, transfers, climate dividends, health costs and interactions are not simulated. A focused child-policy effect is not the total Project 2050 effect. No behavioral responses, uncertainty bands, replicate-weight standard errors, monthly hardship or calibrated national receipt model yet.
6. **Residual mechanism flags** are indicative. Legal exclusion flags every child in an ineligible identification branch regardless of whether a current-law benefit is available. Resource inadequacy is tested against a full-receipt counterfactual; flags are not necessarily mutually exclusive or causal explanations. Service flags are limited to provided fields.

## Minimum next validation gates

- Build and publish the public-data ETL/weighting/tax/SPM crosswalk and source vintage, then reproduce a published current-law child SPM benchmark within an explained tolerance.
- Independently review statutory FAM-1A eligibility, phaseouts, indexing and reconciliation; resolve FAM-2A provenance and EDU-3A reimbursement/valuation questions.
- Verify no duplicate counting of CTC, child care, meals, vouchers, emergency aid or other package transfers; audit service reach and fiscal volumes by year.
- Run synthetic unit tests, weighted identities, phaseout edge cases, and 2030/2034 outputs; add CPS replicate-weight confidence intervals and sensitivity bands before publishing any poverty rate.
- Compare alternatives (FAM-1D, HOU-4C, enhanced delivery) as **proposals**, with incremental cost and D3/D4 constraints, only after baseline validation.

**Authority:** `legacy/governing/project-2050-governing-decisions.md`; `legacy/governing/project-instructions.md`; `legacy/sources/family-child-poverty-model-brief.md`; `legacy/domains/domain-family.md`, `domain-education.md`, `domain-housing.md`. Source branch `claude/pensive-mendel-g1lwl5`, commit `14feb987a7d8aec416ba5bacc50880187a756383`. This prototype branch does not supersede it.

