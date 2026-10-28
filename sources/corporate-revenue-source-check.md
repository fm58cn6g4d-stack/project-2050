# Corporate revenue: what the primary estimates actually support

Codex research, October 27, 2026. Repository baseline: main `b1aba10e8ad69d8ce9c8899a2e511dd1bb5b2a56`. Primary documents accessed October 27. This is a source and scope check, **not a current-law joint score**. Adopted inputs and baseline outputs remain intact.

The corporate revenue agenda remains a persuasive place to begin financing. Its counted dollars, however, need a better foundation before they can define the spending envelope. Three base rows—G1, G5 and G7—already contribute $2.46T over FY2030–39. The sources below substantiate earlier proposals, not that combined later-window yield.

## Verified estimates and the project mapping

All primary-source amounts below are nominal billions over **FY2025–34**, not FY2030–39. Treasury estimates are from March 11, 2024; CBO's December 12, 2024 options attribute their estimates to JCT staff.

| Project row and counted amount | Verified primary estimate | What must be reconciled |
| --- | --- | --- |
| G1: corporate rate 21% → 28%; $1,650B | Treasury: $1,349.941B for 28%. Separately, CBO/JCT: $135.7B for 21% → 22% | Different proposals and estimation contexts. The ledger's combined Treasury/CBO attribution does not specify which annual series supports $1,650B |
| G5: buyback tax to 4% and corporate minimum to 21%; $400B | Treasury: $165.966B for repurchase-tax increase **and loophole changes**, plus $137.429B for the minimum-tax increase; $303.395B combined | Separate instruments and bases; preserve the loophole scope. Raising the regular corporate rate can reduce incremental minimum-tax receipts |
| G7: foreign income at the full corporate rate; $410B | CBO/JCT: $340.0B | The option starts January 2025 and changes the tangible-assets exemption, reduced GILTI rate and foreign-tax-credit limitation together. It is not simply a rate-only estimate to add unchanged beside G1 |
| TS2, inside C38: large-firm foreign-derived deduction repeal; $190B before the package haircut | Treasury: $157.993B gross repeal revenue; equal negative R&D-support line; net subtotal zero | Project TS2 is a different design, including a small-business exception. Gross repeal revenue is not Treasury's net package yield |

Primary references: [Treasury revenue tables, first page](https://home.treasury.gov/system/files/131/General-Explanations-FY2025-Table.pdf#page=1); [Treasury explanations, printed pp. 2–5 and 37](https://home.treasury.gov/system/files/131/General-Explanations-FY2025.pdf); [CBO corporate-rate option](https://www.cbo.gov/budget-options/60956); [CBO foreign-income option](https://www.cbo.gov/budget-options/60960). Treasury's table note cautions that display order need not be estimation order; do not infer standalone additivity from adjacent rows.

Repository mapping: [revenue inputs](../index/data/inputs/ledger-revenue.csv), [revenue domain, sprint design and prior reasoning](../domains/domain-revenue.md), and [counted-revenue reconciliation](revenue-counted-reconciliation.md). C38 already includes TS2; this is not additional revenue.

## A useful discrepancy, not a replacement score

Pure arithmetic illustrates why the G1 source choice matters. Seven times CBO's one-point estimate is $949.9B in its original window. Multiplying that by 1.25 gives $1,187.375B; multiplying Treasury's seven-point estimate by the same factor gives $1,687.426B. The latter is much nearer the project's $1,650B.

**Neither calculation is a valid new score.** The 1.25 multiplier is used here only to expose the difference, borrowing the rough later-window convention described for the sprint. It is not an established G1 transformation, a macroeconomic forecast, or evidence that the lower result is correct. Nonlinear behavior, interactions, start dates and estimation baselines must be reconciled before choosing between estimates. Do not book the roughly $500B difference between these arithmetic illustrations as either a saving or a revenue shortfall.

Likewise, $340B × 1.2 = $408B is close to G7's $410B, and $303.395B × 1.25 = $379.244B is near G5's $400B. Those similarities are provenance leads, not proof of how the old workbook produced its figures. The original annual transformations remain unverified.

## The baseline has changed

The [IRS Form 8993 instructions, revision December 2025](https://www.irs.gov/instructions/i8993), identify Public Law 119-21 changes to deduction-eligible income and state that the deduction percentages become 33.34% and 40% after 2025. Treasury's older FDII explanation instead assumed a scheduled 21.875% deduction after 2025. A later-year multiplier cannot repair that legal-baseline difference.

This check does not exhaust the subsequent international-tax changes or authenticate a comprehensive October 2026 legal baseline. It establishes that re-scoring must begin with the current rules and a precise proposed departure from them, rather than simply shifting the old score five years.

The TS2 gross/net distinction is not evidence of an existing project double count. Project 2050 may choose to retain repeal receipts for other public purposes instead of adopting Treasury's linked R&D support. Its present design should be evaluated on that basis. If a new R&D replacement is proposed, price it explicitly and reconcile it with existing research/industrial commitments; neither silently import Treasury's cost nor promise the gross receipts twice.

## Recommended next analytical decision

Retain the adopted revenue inputs as the comparison case, but stop treating their low legal-risk labels as certification of yield. Build one corporate package in this order:

1. Specify the regular rate, international taxable base and foreign-tax-credit rules together. Resolve whether G7's “full rate” means the proposed 28% rate and identify how each element differs from current law.
2. Calculate the minimum-tax increment after that regular-tax package. Keep the buyback excise separate, with its netting and anti-avoidance scope stated.
3. Add corporate base measures from C38, including TS1–TS5, as conditional increments; separate any mixed corporate/noncorporate coverage rather than assigning all C38 receipts to corporations.
4. Publish annual FY2030–39 and mature-year paths, distinguishing reproduced official historical estimates from independently authored translations and interaction assumptions. Test lower collection and avoidance without substituting an unexplained uniform haircut for a joint score.

That work may support more or less revenue than currently counted. The present evidence does not justify choosing either result, adopting a new tax schedule, or downsizing programs. Espen retains the final spending choice.

## Verification limits

The web research tool opened the primary Treasury PDFs and CBO/IRS pages; figures were checked against their tables/text. A direct shell download of the Treasury PDF returned HTTP 403, so no local PDF snapshot or download hash is claimed. The web tool's initial CBO index clicks resolved to unrelated options; the final direct option URLs above were separately opened and their titles and tables verified. No current-law microsimulation, taxpayer-level interaction model or independently scored replacement package was produced.
