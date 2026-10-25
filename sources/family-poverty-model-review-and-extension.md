# Poverty model review: scope, alternatives and later years

> **October 24 adoption update:** Espen has now selected FAM-1D/AFA plus one million total new voucher awards; broader renter assistance remains an optional add-on to explore. The earlier review/comparison language below records the pre-adoption assessment. Use the [current adoption and architecture bridge](family-adoption-architecture-bridge.md) and [selected-package model results](family-comparison-model-checks.md) for current scope, funding gaps and next work.
October 24, 2026 · Research and software update in PR #18. Source main: `31d2e584d790c6dc6e3c243e1643b1ab3a8d050e`; continues reviewed research branch head `3da255b51ba654833d29bd611d5db7c692b3eb06`. Espen approved delivery improvement as necessary in every design, a FAM-1A/FAM-1D comparison including an American Family Act analogue, and wider rental-assistance exploration. These are development directions, not adoption of an expansion, eligibility rule, indexing anchor or financing amount.

## Is something wrong with the model?

**The first problem is interpreting a partial, static experiment as an estimate of the whole agenda.** The published report discloses the distinction, but a headline about “Project 2050 poverty” can still invite it. The evidence currently supports a narrower claim: selected modeled child-policy channels reduce poverty against source-year resources under specified assumptions. It does not establish how close the full agenda comes to the charter's ambition.

A targeted inspection of credit arithmetic, source-credit offsets, expense caps, discrete receipt, household voucher allocation and aggregation did not identify a demonstrated computational defect that explains the modest headline. The original 102 tests and the stored eight-case/42-sensitivity checks still pass; 15 extension tests also pass. Those checks are not an independent validation of every source assumption. User-supplied Census members subsequently enabled national re-execution of the comparison matrix and exact reproduction of the original moderate result. This is a stronger computational/source check, not independent validation of all eligibility or behavioral assumptions. Further distributional inspection and calibration remain useful; the executed conditional comparisons are in the generated report.

| Feature inspected | Why the result can be modest | Assessment and treatment |
| --- | --- | --- |
| Existing source-year credits remain in baseline | The new credit is an increment over credits families already receive, not the whole statutory award added to income. | Correct anti-double-counting principle. Frozen source-year taxes are an explicit comparison convention, not an audited future-law baseline. A stronger comparator should reconcile the exact award, source credit and resources for the same families. |
| $3,600/$3,000 treated as 2030 face values in the main case | Five years of inflation reduce their purchasing power relative to a 2025 anchor. The existing alternate anchor lowers moderate 2034 poverty from 10.29% to 9.69%. | A consequential unresolved policy/price convention, not a reason to select the more favorable result. Both branches remain visible. |
| Moderate credit coverage 95% and conditional receipt 95% | Their product is 90.25% in the outcome mixture. It is an assumption, not measured take-up or an identification-status model. | Test the assumptions, including concentration among poorer families. Full modeled coverage/receipt still retains claimant proxies and scarce housing. No citizenship-to-SSN/ITIN imputation. |
| Care/pre-K valued through actual paid expenses and capped SPM deductions | A family with no recorded paid care can gain access and time without receiving a measured cash gain. | Appropriate for the expense channel. Incomplete for employment, quality, child development and broader freedom; do not turn service budgets into cash. |
| Vouchers limited to 400,000 new household awards | Awards include adult-only households and are distinct from successful leases. | Reflects the selected scale and an uncertain allocation proxy. It cannot test an entitlement without changing the scenario explicitly. |
| Leave contributions included, leave benefits omitted | A cost-only stress slightly worsens the headline. | Not a net evaluation of leave insurance; add benefits only against supported leave events and replacement rules. |
| Frozen earnings, expenses, thresholds and other baseline resources | No gains from wage policy, changed employment, housing supply or accumulated childhood benefits appear automatically. | Keeps the current experiment tractable. It is insufficient for a long-term whole-agenda claim. Broadening it should use distinct causal channels with overlap controls. |

The new contribution check also confirms that the adopted credit is reaching the bottom in the calculation: source-deep-poor children's units have an average additional statutory credit of about $6,574 in 2025 dollars before receipt assumptions, compared with about $527 of existing unit credit. These are **child-weighted household/unit amounts**, not $6,574 for each child or a fiscal total. About 95% of children in that group have a positive modeled increment. This does not identify every exclusion or establish adequacy; it argues against an explanation in which the credit generally never enters deeply poor families' modeled resources.

The source-year EITC/ACTC removal comparator validates an accounting operation, not the entire Project benefit simulation. Replicate-weight intervals measure sampling uncertainty conditional on assumptions. Passing either does not settle eligibility, tax construction, future receipt or benefit valuation.

## Executed national comparison: what changes the outcome

With the uploaded members, the selected comparison matrix now executes on the actual CPS source sample. All figures remain conditional static comparisons using 2034 valuation/population conventions, not forecasts or an exact monthly AFA score. The source-year baseline is about 13.4% child poverty.

| Design and delivery | Child poverty | Deep poverty | Main interpretation |
| --- | ---: | ---: | --- |
| Previous package, moderate delivery, 400,000 new voucher awards | 10.29% | 2.28% | Exact reproduction of the published calculation |
| AFA analogue with 2030 face amounts, moderate delivery | 9.34% | 2.13% | Larger credit plus stated alternative schedule; not benefit-size-only identification |
| AFA analogue preserving 2025 real face amounts, moderate delivery | 8.89% | 2.03% | About 931,000 fewer poor children than the adopted moderate case; price convention remains a research branch |
| Same real-value AFA analogue, enhanced delivery, one million voucher awards | 8.34% | 1.85% | A bounded wider-reach joint comparison; 850,000 expected leases under the scenario |
| Same real-value AFA analogue, enhanced delivery, all proxy-eligible renter households awarded | 6.32% | 1.16% | Exploratory reach boundary: about 6.76m awards and 5.74m expected leases, not an implementable or priced entitlement |

The broader housing boundary retains income/eligibility and valuation proxies, the assumed lease-up rate, existing housing assistance and source-year resources. It assumes enough feasible leases at that scale without demonstrating supply, landlord participation or rent effects. It is a useful signal that benefit reach can materially change the result, not evidence that the entitlement can immediately be delivered at a known price. Compared at the same enhanced delivery, adopted-credit/wider-housing is 7.52% versus 6.32% for the joint AFA case. Comparing the latter with the moderate adopted case also changes delivery, so it is not a clean isolated housing or credit effect.

**Recommendation:** take the AFA and a specified wider rental-assistance path seriously as alternatives worth costing. The national exercise strengthens the case for examining adequacy and reach alongside delivery. It does not justify adopting the broadest boundary, summing separate percentage reductions, or claiming that 6.32% is the entire agenda's expected outcome. No new calibrated health, wage or leave gains are credited. The generated JSON also includes child-weighted credit contribution diagnostics by source-resource group; these are unit credit amounts shared by children, not per-child statutory awards or federal costs.

## What has been added to the toolkit

The separate [comparison adapter](../index/tools/child-poverty/comparison_analysis.py) reuses the existing archive parser, household/service preparation, receipt mixture, aggregation and all 160 replicate weights. It leaves the published model, assumptions and results unchanged. [Generated checks](family-comparison-model-checks.md) and their [JSON](family-comparison-model-checks.json) distinguish executed references from unexecuted national comparisons.

The runnable matrix compares:

- Historical FAM-1A, preserving the original result as a reproduction gate.
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

The uploaded-member run also evaluates the [explicit later-year scenario inputs](family-later-year-scenario-paths.json): moderate 2034, enhanced 2040 and full modeled receipt in 2050, plus favorable/adverse 2050 resource stresses, all using the same 2034 valuation/population reference. An enhanced-delivery 2040 case differs because delivery was changed, not because the date itself predicts it. Adopted-credit and AFA cases share each path; changed resource baselines are reported separately in the JSON. A resource shift expressed as a share of the poverty threshold is an adequacy stress, not a wage/employment forecast. The adapter requires a named review for each such path. It deliberately does not extrapolate the existing short CBO extracts, age today's children into 2050, or project future child counts from a fixed sample.

| Conditional path, same real baseline | Adopted credit | Real-value AFA analogue |
| --- | ---: | ---: |
| 2034 moderate delivery reference | 10.29% | 8.89% |
| 2040 enhanced-delivery illustration | 10.03% | 8.55% |
| 2050 full modeled receipt/access illustration | 9.87% | 8.33% |

These dates label **assumed stages**, not promised dates or projected poverty. The 2050 adverse resource stress raises the same-scenario baseline to 15.35%, producing 11.42% with the adopted credit or 9.71% with AFA. The favorable stress lowers the baseline to 11.66%, producing 8.33% or 7.12%, respectively. Neither stress credits an estimated economic effect to policy. The large differences make the surrounding resource path important to future analysis; they do not establish which future is likely.

A subsequent evidence-backed extension could add refreshed age/sex population weights, supported net earnings/expense paths and non-SPM care/housing outcomes. Each should be reported against its own same-scenario baseline. Childhood effects on adult opportunity belong in a cohort analysis; they cannot be inferred by relabeling today's children as the future child population. This is a staged improvement to the existing toolkit, not a new integrated 2050 engine prerequisite.

## Execution, limits and next action

Executed: all 117 model/extension unit tests; existing eight-case/42-sensitivity checker; legacy report reproduction; two national matrix executions with all sixteen case records identical; ten later-year cases; complete source-year baseline comparison (only container hash differs); all three adopted 2034 references; award/lease, poverty/count, null-cost and generator-render/source-hash gates; common rebuild and local link/whitespace checks. The original 102-test suite remains part of the total. Test cases for alternative schedules, negative credit increments, newborn exposure, joint housing/delivery, overlay bounds and later-year labeling use artificial microdata and are never published as national estimates. Existing policy/fiscal/incidence inputs are unchanged.

**The data-access block is resolved.** Espen supplied all four Census CSVs, with compressed person data and four split parts of the replicate-weight ZIP. The parts were concatenated in filename order and ZIP integrity checked. Person and weight files each contain 134,729 records; there are 31,444 children and all 160 replicate weights plus the base weight. The parser's complete joins and source-year credit-removal comparator passed. The complete source-year baseline JSON reproduced every field except the necessarily different container hash, and all three adopted 2034 delivery results reproduced. All sixteen national comparisons repeated identically on a second run.

The [upload manifest](family-census-upload-manifest.json) records exact member byte counts/hashes. The source URL remains the official [Census archive](https://www2.census.gov/programs-surveys/cps/datasets/2026/march/asecpub26csv.zip), whose original expected SHA-256 is `fe819d0d2fc4470c282e76c247b8aa8b6054811619730307e9f2fe6186707d93`. That original ZIP was not obtained: the local archive is a new container for the uploaded CSVs and has its own hash. The adapter verifies every manifested member and records this distinction explicitly, rather than suppressing the original-archive hash gate. This establishes uploaded-byte integrity plus equivalence on the checked source/model results, not independent byte identity to the inaccessible original archive. Raw CSVs, ZIPs and individual records stay outside GitHub.

Reproduce the available checks with:

```bash
python3 -m unittest discover -s index/tools/child-poverty -p 'test_*.py'
python3 index/tools/child-poverty/comparison_analysis.py
```

For the official original archive:

```bash
python3 index/tools/child-poverty/comparison_analysis.py --archive /path/to/asecpub26csv.zip --paths sources/family-later-year-scenario-paths.json
```

For the uploaded members, pass `--source-manifest sources/family-census-upload-manifest.json` with a local ZIP containing the named CSVs. The runner verifies the original archive hash or every manifested member, checks the source-year comparator and requires exact reproduction of the legacy moderate 2034 poverty rate before accepting the new national matrix. `--overlays` accepts the reviewed component ledger described above; `--paths` accepts an array of `{year, delivery, resource_shift, review}` records for 2034/2040/2050. Neither supplies missing evidence automatically. Outputs are generator-owned Markdown/JSON; regenerate through the script. Federal costs remain unpriced even after a successful poverty run.

**Next concrete action:** review the executed credit/housing comparisons and their financing/evidence limits before choosing any benefit change. New calibrated health, earnings or leave inputs and a real marginal budget remain unresolved. No policy adoption, merge, outside contact or other workstream follows from a successful poverty run.
