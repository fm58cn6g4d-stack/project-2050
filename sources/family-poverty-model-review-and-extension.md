# Poverty model review: scope, alternatives and later years

October 24, 2026 · Research and software update in PR #18. Source main: `31d2e584d790c6dc6e3c243e1643b1ab3a8d050e`; continues reviewed research branch head `3da255b51ba654833d29bd611d5db7c692b3eb06`. Espen approved delivery improvement as necessary in every design, a FAM-1A/FAM-1D comparison including an American Family Act analogue, and wider rental-assistance exploration. These are development directions, not adoption of an expansion, eligibility rule, indexing anchor or financing amount.

## Is something wrong with the model?

**The first problem is interpreting a partial, static experiment as an estimate of the whole agenda.** The published report discloses the distinction, but a headline about “Project 2050 poverty” can still invite it. The evidence currently supports a narrower claim: selected modeled child-policy channels reduce poverty against source-year resources under specified assumptions. It does not establish how close the full agenda comes to the charter's ambition.

A targeted inspection of credit arithmetic, source-credit offsets, expense caps, discrete receipt, household voucher allocation and aggregation did not identify a demonstrated computational defect that explains the modest headline. The original 102 tests and the stored eight-case/42-sensitivity checks still pass; 13 new extension tests also pass. Those checks are not an independent validation of every source assumption. A fresh national re-execution and inspection of household contribution distributions is still needed before claiming that the substantive result is validated independently. New national alternative results are not available in this update.

| Feature inspected | Why the result can be modest | Assessment and treatment |
| --- | --- | --- |
| Existing source-year credits remain in baseline | The new credit is an increment over credits families already receive, not the whole statutory award added to income. | Correct anti-double-counting principle. Frozen source-year taxes are an explicit comparison convention, not an audited future-law baseline. A stronger comparator should reconcile the exact award, source credit and resources for the same families. |
| $3,600/$3,000 treated as 2030 face values in the main case | Five years of inflation reduce their purchasing power relative to a 2025 anchor. The existing alternate anchor lowers moderate 2034 poverty from 10.29% to 9.69%. | A consequential unresolved policy/price convention, not a reason to select the more favorable result. Both branches remain visible. |
| Moderate credit coverage 95% and conditional receipt 95% | Their product is 90.25% in the outcome mixture. It is an assumption, not measured take-up or an identification-status model. | Test the assumptions, including concentration among poorer families. Full modeled coverage/receipt still retains claimant proxies and scarce housing. No citizenship-to-SSN/ITIN imputation. |
| Care/pre-K valued through actual paid expenses and capped SPM deductions | A family with no recorded paid care can gain access and time without receiving a measured cash gain. | Appropriate for the expense channel. Incomplete for employment, quality, child development and broader freedom; do not turn service budgets into cash. |
| Vouchers limited to 400,000 new household awards | Awards include adult-only households and are distinct from successful leases. | Reflects the selected scale and an uncertain allocation proxy. It cannot test an entitlement without changing the scenario explicitly. |
| Leave contributions included, leave benefits omitted | A cost-only stress slightly worsens the headline. | Not a net evaluation of leave insurance; add benefits only against supported leave events and replacement rules. |
| Frozen earnings, expenses, thresholds and other baseline resources | No gains from wage policy, changed employment, housing supply or accumulated childhood benefits appear automatically. | Keeps the current experiment tractable. It is insufficient for a long-term whole-agenda claim. Broadening it should use distinct causal channels with overlap controls. |

The source-year EITC/ACTC removal comparator validates an accounting operation, not the entire Project benefit simulation. Replicate-weight intervals measure sampling uncertainty conditional on assumptions. Passing either does not settle eligibility, tax construction, future receipt or benefit valuation.

## What has been added to the toolkit

The separate [comparison adapter](../index/tools/child-poverty/comparison_analysis.py) reuses the existing archive parser, household/service preparation, receipt mixture, aggregation and all 160 replicate weights. It leaves the published model, assumptions and results unchanged. [Generated checks](family-comparison-model-checks.md) and their [JSON](family-comparison-model-checks.json) distinguish executed references from unexecuted national comparisons.

The runnable matrix compares:

- Adopted FAM-1A, preserving the original result as a reproduction gate.
- FAM-1D represented by AFA face amounts anchored to 2030, to separate benefit size from purchasing-power assumptions.
- An AFA annual-exposure analogue preserving those face amounts in 2025 purchasing power, plus a version without the newborn bonus.
- Moderate, enhanced and full delivery for each design. Improved delivery is part of every design comparison, not an optional substitute for adequate benefits.
- One million voucher awards and full coverage of the model's proxy-eligible renter pool, under enhanced delivery, both separately and jointly with the AFA analogue. These are exploratory reach boundaries, not selected HOU-4C eligibility, phase-ins or proof that landlords/units exist.

**FAM-1D is already the repository's AFA option.** These price/newborn branches distinguish interpretations of that option; they are not three different policy packages to add together. Effects are recomputed jointly when microdata are supplied. Expected awards and leases are separate. Every new federal cost stays null: a source-year SPM gain, household award or poverty gap is not a budget score.

The alternative tax calculation allows negative increments. A high-income family whose credit falls cannot have that loss silently erased by the original FAM-1A increment-only convention. This is a capability needed for the alternative, not a correction to the previously stated FAM-1A scenario. Source nonrefundable CTC still combines adult-dependent credit; the adapter retains the same conservative combined offset for comparability, so a separate ODC allocation remains unresolved. The output is not a complete AFA distributional or D3 analysis.

## American Family Act: source-to-model boundary

Primary text inspected: [H.R.2763, introduced](https://www.govinfo.gov/content/pkg/BILLS-119hr2763ih/html/BILLS-119hr2763ih.htm), §2, proposed §24A(b)–(e), and the corresponding [S.1393](https://www.govinfo.gov/content/pkg/BILLS-119s1393is/html/BILLS-119s1393is.htm). Both are 119th-Congress proposals introduced April 9, 2025; they are not current law. Their substantial initial sponsor lists support treating this as an important live alternative. No fresh exact cosponsor census or vote prediction is claimed.

The proposed monthly base is $300 for ages six through seventeen and 120% for children under six, with an 800% multiplier replacing that percentage in the first month of life. Thus the unindexed full-year exposure analogue is $3,600, $4,320, or $6,360 for an infant with eleven ordinary months plus the first-month payment. The text also specifies initial/secondary income thresholds, inflation/rounding, monthly residence/care/tie-breaker rules, refundability, identification and advance-payment/reconciliation machinery.

The adapter **does not simulate that entire statute**. Interview ages do not provide birth month, calendar-year exposure or monthly household changes. The $6,360 age-zero branch is a full-year exposure convention, not an exact award to every surveyed infant; the no-bonus case brackets that mechanism without claiming to bound all age/timing errors. The annual analogue scales thresholds with an explicit price factor rather than reconstructing the statute's different CPI base years, lag and rounding. It maps the existing `other` filing category to a single taxpayer; separate-return distinctions, MAGI exclusions, prior-year income elections, broader specified-child definitions, Puerto Rico, adult-dependent credits and protected reconciliation require further work. All qualifying-child and identification inputs remain conditional.

The text asks for taxpayer identification numbers; that should not be silently replaced by a work-authorized-SSN-only rule. Nor does an ID provision establish residence or every other eligibility condition. A legal branch must be specified separately from observed survey citizenship; the present data do not support a national count of each SSN/ITIN branch. The comparison can test conditional coverage, but cannot declare those eligibility choices resolved or selected.

## More components: yes, in a controlled order

| Addition | Required input and overlap control | Current status |
| --- | --- | --- |
| Health's effect on family expenses | Calibrated changes to actual medical out-of-pocket deductions by household, including premiums and payer coordination; no duplication of existing expense savings | High priority after the health work. Adapter accepts reviewed savings capped at source MOOP; no invented universal percentage supplied. Existing 15%/30% sensitivities remain stresses. |
| Other tax/transfer and wage policies | Net household resources after taxes, contribution burdens, benefit interactions and earnings responses, with a named baseline and source | A reviewed net-amount input is supported. No direct conversion of quintile averages or gross wage increases into every child's resources. |
| Paid-leave benefits | Supported qualifying events, replacement, receipt, contributions and interaction with existing state/employer coverage | Reviewed net benefit input supported; no blanket annual entitlement credited to every family. |
| Wider housing assistance | Eligibility, allocation, phased awards, successful lease-up and SPM valuation; coordinate with supply and existing subsidy | Exploratory award-cap comparisons implemented. National effects and actual cost require the verified archive and further specification. |
| Care, housing supply and long-run childhood effects | Separate evidence for availability, net employment/resources, rents, quality and later outcomes; recompute affected taxes/benefits | Keep as distinct pathways and non-SPM outcomes until evidence supports quantification. No automatic multiplier or dynamic revenue. |

The overlay input requires a unit identifier, named component, finite net 2025-dollar amount, source/review reference and explicit baseline reconciliation. Duplicate unit/component entries, unsupported construction-as-cash inputs, unknown units and medical savings above actual deductions are rejected. These checks enforce a contract; they do not establish the validity of a supplied estimate. No household microdata or unreviewed overlays are committed.

## Extending beyond 2034 intelligently

The immediate extension covers **2040 and 2050** as conditional policy-maturity references. It does not extrapolate a poverty-rate trend. With the 2034 population mix, real resources, real policy rules and delivery unchanged, moderate remains 10.29%, enhanced 10.03% and full 9.87% at both dates. Those repeated values are generated from the existing result, not independently simulated future observations. They make a useful point: waiting longer produces no improvement in a static model without an explicit mechanism.

A verified-archive run can also evaluate reviewed year-specific delivery stages and resource stresses, using the same 2034 valuation/population reference. For example, an enhanced-delivery 2040 case differs because delivery was changed, not because the date itself predicts it. A resource shift expressed as a share of the poverty threshold is an adequacy stress, not a wage/employment forecast. The adapter requires a named review for each such path. It deliberately does not extrapolate the existing short CBO extracts, age today's children into 2050, or project future child counts from a fixed sample.

A subsequent evidence-backed extension could add refreshed age/sex population weights, supported net earnings/expense paths and non-SPM care/housing outcomes. Each should be reported against its own same-scenario baseline. Childhood effects on adult opportunity belong in a cohort analysis; they cannot be inferred by relabeling today's children as the future child population. This is a staged improvement to the existing toolkit, not a new integrated 2050 engine prerequisite.

## Execution, limits and next action

Executed: all 115 model/extension unit tests; existing eight-case/42-sensitivity checker; old published Markdown/HTML reproduction; new generator and byte-identical reproduction; local link, source-hash and whitespace checks. The original 102-test suite remains part of the total. Test cases for alternative schedules, negative credit increments, newborn exposure, joint housing/delivery, overlay bounds and later-year labeling use artificial microdata and are never published as national estimates. Existing policy/fiscal/incidence inputs are unchanged.

Fresh national comparisons are **blocked**, not completed. The official [Census archive](https://www2.census.gov/programs-surveys/cps/datasets/2026/march/asecpub26csv.zip) is not local; the workspace proxy returned HTTP 403, and `www2.census.gov` is absent from the configured destination list. The cloud-runtime networking instructions prohibit bypassing that restriction. The web research tool can inspect official pages and bill text but has not delivered the archive bytes to the execution workspace. No alternate source or constructed microdata has been passed off as the verified file. Expected SHA-256 is `fe819d0d2fc4470c282e76c247b8aa8b6054811619730307e9f2fe6186707d93`.

Reproduce the available checks with:

```bash
python3 -m unittest discover -s index/tools/child-poverty -p 'test_*.py'
python3 index/tools/child-poverty/comparison_analysis.py
```

After the official archive becomes accessible:

```bash
python3 index/tools/child-poverty/comparison_analysis.py --archive /path/to/asecpub26csv.zip
```

The runner verifies its hash, checks the source-year comparator and requires exact reproduction of the legacy moderate 2034 poverty rate before accepting the new national matrix. `--overlays` accepts the reviewed component ledger described above; `--paths` accepts an array of `{year, delivery, resource_shift, review}` records for 2034/2040/2050. Neither supplies missing evidence automatically. Outputs are generator-owned Markdown/JSON; regenerate through the script. Federal costs remain unpriced even after a successful poverty run.

**Next concrete action:** obtain permitted access to the official archive and execute the national matrix; inspect the credit/service contribution distributions and alternative results before recommending any benefit adoption. Until then, the policy comparison remains prepared and tested, with the existing evidence and static later-year references available. No merge, outside contact or other workstream is authorized by this update.
