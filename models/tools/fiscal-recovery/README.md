# Fiscal recovery and education adoption bridge

> Historical first-pass calculation. The [Recovery and Solvency supplement](../recovery-budget/README.md) supersedes the pooled education residual and separate-fund fiscal comparisons with component reconciliation and consolidated flows. Retained inputs/results preserve this experiment; the arithmetic tests below do not independently verify its $0.77T current-law assumption.

Source main `beeba090020b7916f8ed08bcff36161fb70d1e69`; comparison review
`b94507d552e504a7f0c0f0c4ef16368d946557d6`. Full EDU-9B benefit scope and
payroll institution are adopted. Financing schedules are conditional recommendations.
Read `sources/fiscal-recovery-and-education-redesign.md`.

## Run

Python 3.9+ and Node.js for the existing common suite; no third-party Python package.
From repository root:

```bash
bash index/tools/run-all.sh --write
python3 -W ignore::ResourceWarning index/tools/fiscal-recovery/test_model.py
python3 index/tools/fiscal-recovery/model.py --output-dir /tmp/recovery-check
sha256sum -c index/tools/fiscal-recovery/MANIFEST.sha256
```

The common runner now generates the original comparison and the education supplement.
A dry run without `--write` writes only `build/` and compares committed products.
Standalone `model.py` requires that common build and defaults to the three committed
outputs: `index/fiscal-recovery-model.md`, `index/data/fiscal-recovery-model.json`,
`sources/fiscal-recovery-inventory.csv`. `--output-dir` changes all three destinations.
Original fiscal CSV, ledger numeric inputs and incidence inputs remain the
pre-education comparison, **not complete new-policy totals**. Generator-owned notices
state this. Keeping an explicit bridge avoids turning an unselected contribution rate
into adopted policy. The public edition remains on its prior source pin.

`index/data/inputs/education-adoption.json` records selected scope and source cost
assumptions. `assumptions.json` contains working financing, stress and recovery choices.
No estate revenue is counted again; no high-end tax haircut is reclaimed. No borrowing
row or dynamic revenue is a pay-for. Exact filing/self-employment rules, appropriation
crosswalk, federal/state matching and statutory indexing require further work.

## Accounting and horizons

All fiscal flows are nominal $B/year; window totals are $T, FY2030–39. For each year:

- Full fund outlays = old agenda transfer + absorbed current-law spending + new benefits.
- General-fund delta = − old transfer − current-law absorption + fund grants + tax offset
  + household-protection reserve.
- Unified delta = new benefits − payroll receipts + tax offset + protection reserve.
- Unified delta − GF delta = fund outlays − payroll receipts − fund grants.

Positive deltas worsen balances. Permanent grants and transition grants are both GF
expenses; they cancel on consolidation. Reserve interest is an internal Treasury
transfer, not new unified revenue. Negative reserve values are unmet financing,
not an assumed legal authority to spend. The model isolates fund-engine import side
effects in a temporary directory. Tests preserve all original CSV inputs.

The mixed reference phases 1.4 points over 2031–35, adds a permanent 30% GF share and
fills the additional early shortfall through 2034. A 2-point comparator has transition
grants but no continuing share. The 12.5% offset and 20% protection reserve are
unscored allowances. Incidence adds only the new benefit increment, allocated using
the old education option's .24/.39 childcare/education proportions, and the full
worker burden of both tax halves. It never allocates an unidentified rebate.

Education has 75 years (2030–2104), with source anchors through 2049 and authored
extrapolations thereafter. A positive terminal balance is not sustainable solvency
if the reserve ratio declines. Care-share-floor alternatives apply the same share to
the combined care line: an explicit sensitivity pending component reconciliation.

Existing fiscal debt arithmetic runs through 2056. Additional net-resource requirements
are NOT tax rates or scored receipts. The whole-government solve phases resources over
2035–44 and requires nonincreasing debt/GDP in every year 2045–56. It includes the
agenda requirement; do not add them. SS/HI/leave alternatives are separate diagnostics,
not an unreconciled second set of receipts inside the unified paths. The program-rate
stress is incremental, not a shock to all federal debt. No new growth/inflation model.

SSA-based SS/HI paths run 2026–2100; leave to 2060; transportation ends in 2046. The SS
solver retains the old engine's conservative one-year terminal reserve and near-stable
last-six-year ratio test. Its 0.34-point interaction deduction is an annual authored
approximation informed by the repository's joint-versus-separate SSA comparison.
HI has a known calibration difference; neither is an official joint actuarial score.

## Inventory, provenance and validation

The CSV preserves every 59 bill, 58 revenue, 22 option/cut and nine dynamic input rows.
Amounts are recorded window estimates; `model:...` entries are model references, not
zeros. Source notes preserve window exceptions. Rows overlap: do not sum the inventory.
New education costs and payroll scenarios live in the bridge and JSON, not an additional
legacy bill row that would also be counted by the original pipeline.

JSON includes source hashes for code, numerical inputs, comparison intermediates and
the source education report. The package manifest also covers authored text and tests,
excluding itself. Verify both the manifest and deterministic regeneration. Ten focused
tests check transfer conservation, new costs, early grants, no estate reuse, tax deferral,
state costs, reserve/timing failures, incidence, debt stabilization and input preservation.
Inherited ResourceWarnings from the legacy import code are not new data failures.

Earlier strategic experiments remain on their original numerical comparison. Their
JSON hashes describe that generation; do not relabel those as a new-policy score.
The repository manifest is refreshed for amended shared status text. No raw private
microdata, official joint tax score, actuarial package score or delivery certification
is bundled.

Validation in this pass: common rebuild completed, all ten new tests and thirteen prior
strategic-review tests passed, and all three new outputs reproduced byte for byte.
The common checker retains its prior unresolved findings and identifies the expected
ED1 difference between the preserved $2.1T historical row and new conditional financing.
Neither that finding nor a successful run establishes a D3/D4 pass.
