# Revenue already counted: the starting point for a sustainable envelope

Codex research reconciliation, October 27, 2026. Source: remote `main` at **55a675f825cbf4c783f94a0ec1b3586d623b15e1**, after PRs 24, 35 and 36. This is an accounting finding and recommendation for the next financing analysis, not a new tax score or policy adoption. PR 37 remains outside this source vintage. Its carbon integration changes the offset and baseline; its pending options are not assumed approved here.

The revenue-first strategy should begin by testing the receipts the project already relies on. The mixed recovery model retains **$8.115T** of the general-fund reform receipts and adjustments traced below over FY2030–39. Those receipts already finance existing commitments. They cannot be offered again as the pay-for for a new expansion, and their inclusion does not establish that they form a reliable financing envelope.

The [20-row reconciliation](revenue-counted-reconciliation.csv) traces every general-fund base revenue row, the seven retained DEC revenue options, and the recovery IRS allowance. It records source hashes, source descriptions as written, and the corresponding mixed-case audit amounts. It excludes current-law receipts, dedicated funds, new illustrative income contributions, and spending savings. It is therefore a defined subset of the total-government budget, not total federal revenue or a new fiscal-gap estimate.

## From the old ledger to the recovery model

Nominal $T, FY2030–39; positive means receipts, negative means a receipt reduction.

| Step | Amount | Meaning |
| --- | ---: | --- |
| General-fund base before GX and CX | 6.860 | Existing corporate, high-income, capital and enforcement measures |
| GX overlap and avoidance adjustment | −0.495 | Estimated haircut on four specified rows |
| CX carbon-related income/payroll offset | −0.380 | General-fund cost of dedicated excises at this source vintage |
| General-fund base, unrounded | **5.985** | Displayed as $5.99T in the ledger |
| All accepted DEC revenue options | +3.710 | C18, C35, C19b, C20, C38, C39, C40, C41 and C43 |
| Remove C19b and C20 in the mixed recovery case | −1.330 | Health-exclusion cap and the $100K/$200K income surtax are not carried into this case |
| Recovery IRS receipt-risk allowance | −0.250 | Reduces the $0.400T G8 line to $0.150T net |
| **Traced receipts retained in mixed recovery** | **8.115** | Before other recovery taxes, fund flows and offsets |

The committed audit reproduces **$8.114999T**; the $0.000001T difference is annual-output rounding. Its FY2040 sum for these same rows is **$1,010.694B**, based on the model's authored annual profiles, not an independently scored mature-year yield. Compare like-for-like annual paths before deciding what a recurring benefit can rely on.

The recovery model imports the base rows, then adds the accepted option rows. It skips C19b/C20 in the mixed case; the alternative case phases them from 2033. It separately subtracts the IRS allowance. This is why neither the ledger's `in_base` field nor the list of adopted historical options alone identifies the current recovery financing. See [recovery model](../index/tools/recovery-budget/model.py), [DEC selection](../index/tools/fiscal-model.py), [inputs](../index/data/inputs/ledger-revenue.csv), [options](../index/data/inputs/ledger-cuts.csv), and [audit](recovery-budget-audit.csv).

## What the overlap protection does—and leaves unresolved

**GX is a fixed estimate, not a joint tax model.** Its midpoint is exactly 15% of G11 $0.65T + G6 $0.70T + G9 $1.45T + H1b $0.50T: $0.495T. The [revenue domain](../domains/domain-revenue.md) explains that the interaction between annual gains taxation and gains at death sits inside this allowance. That is a considered precaution, but it does not independently estimate how much revenue remains when all provisions operate together.

The C43 description says its overlap is “inside GX's logic.” The implemented GX amount does not explicitly add C43 to its base, however. C18's bracket and gains changes and C39's deduction-value cap also need a joint score. This is a limitation of the fixed allowance, not evidence that an additional arbitrary haircut of a particular size is correct. Keep the existing deduction until a replacement score reconciles the same bases; do not silently release it to enlarge the envelope.

**C38 already contains the sprint menu.** The eleven TS midpoints sum to $0.985T. Applying the stated 10% package haircut gives $0.8865T, rounded to the counted $0.89T. TS6's $0.10T row is already described as including its own estate-overlap adjustment. Do not apply that adjustment twice, add TS1–TS11 again, or treat the entire $0.985T as available beyond C38. TS12 is outside that package but already counted separately as C39. The source descriptions principally refer to the FY2025 Green Book, translated into a later window; they explicitly acknowledge the pre-2025-law baseline. Reading those descriptions does not verify a current-law score.

**Estate and capital-income reforms have multiple aliases but one revenue base.** E1 is counted through C35 at $0.15T beyond G9's estate-exemption reversal, not at its earlier $0.35T gross estimate. Gains at death are G6, not a second education financing source. G4 is an alternative replaced by G11. SC1 is already C43. A new proposal must show its increment over these counted provisions, including timing and avoidance, rather than quote a gross standalone estimate.

**Dedicated funds do not supply spare general-fund receipts.** H1a belongs to Medicare HI; H1b is the separate general-fund row. OASDI investment/pass-through receipts have their own overlap and response conventions. In the mixed recovery implementation, C35 remains a general-fund receipt and education receives modeled grants and contributions; there is no second estate receipt to add to that fund. Any future reassignment changes the account, not total federal resources. The [recovery method](../index/tools/recovery-budget/README.md) governs those boundaries.

## What this implies for the next revenue cases

I recommend keeping two different questions visible: how much is currently counted, and how much can support durable promises after a joint current-law assessment. The $8.115T answers only the first. It should not be relabeled the “durable core.”

The existing [stress assumptions](../index/tools/recovery-budget/assumptions.json) remove a further $0.84T in the decade from the rows traced here: G8 $0.15T, C39 $0.15T, C38 $0.29T and G9 $0.25T. That is additional to the $0.25T IRS allowance already deducted. The same stress also reduces HLT-6 savings by $0.35T, a spending-side change excluded from this receipt-only reconciliation, and loses half the G11 annual revenue after 2039. These are planning stresses, not probabilities, and they do not test the loss of G11 during the first decade.

The next bounded analytical assignment should price **one joint corporate package**—G1, G5, G7 and the corporate components of C38—against the same post-2025-law baseline, with rate/base interactions and a documented translation into FY2030–39. This cluster is large, central to the public argument, and more useful to settle than another arbitrary broad-income contribution. A parallel question for the subsequent capital-income package is what realizations, death-time taxation and a deferral-charge fallback can reliably collect if annual mark-to-market does not survive. Do not treat the current assumption that the fallback preserves most receipts as a verified replacement score.

For now, retain the counted inputs, reserve any apparent upside, and compare additional alternatives only as net changes to this reconciliation. This leaves Espen's final spending choices open and preserves D3/D4 rather than manufacturing room through duplicate receipts or unsupported scoring precision.

## Evidence and reproducibility

This pass inspected repository evidence and executable routing; it did not retrieve or independently verify the underlying Treasury, CBO or JCT publications. The CSV preserves those source descriptions as leads, not newly authenticated citations. Current-law re-scoring and source-vintage verification remain substantive work.

To reproduce the arithmetic on the pinned source: select `ledger-revenue.csv` rows with `in_base=yes` and `channel=General fund`; add `ledger-cuts.csv` rows C18/C35/C38/C39/C40/C41/C43; subtract `recovery-adoption.json`'s `spending.irs_receipt_risk_tn`. Check each against `sources/recovery-budget-audit.csv` with `case=mixed`, summing `revenue_change_bn / 1000` for 2030–39 and reading the 2040 row separately. Each input amount agrees with its audit total within $0.00001T. No common model or adopted input was changed. This report remains pinned when PR 37 lands; its CX change must be reconciled before using these totals as a live comparison.
