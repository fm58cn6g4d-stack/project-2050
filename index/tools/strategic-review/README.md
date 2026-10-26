# Strategic-review experiments

Exploratory research for the October 25, 2026 independent review. Source main:
`beeba090020b7916f8ed08bcff36161fb70d1e69`. Those original experiments did not change adopted policy or numerical inputs. The later [fiscal-recovery package](../fiscal-recovery/README.md) records Espen's full EDU-9B adoption and supplies an integrated bridge; the original arithmetic here remains a pre-education comparison.

From the repository root, with Python 3.9+ and Node.js for the existing suite:

```bash
bash index/tools/run-all.sh
python3 index/tools/strategic-review/analyze.py
python3 index/tools/strategic-review/test_analysis.py
```

The first command builds the existing suite in `build/` without writing committed
baseline outputs. The second writes only `sources/strategic-review-arithmetic.md`
and `.json`; `--output /tmp/review-check` writes a separate comparison copy.
`assumptions.json` is the authored scenario record. The new tool imports the
existing fiscal `row_path` function and its authored profiles and reads rebuilt
DEC/ledger results. It does not modify them or claim to rescore a tax.

The experiments examine simultaneous low cases for HLT-6's **general-fund** share,
G8 and C39, then selected revenue illustrations. They do not recalculate HI, debt,
interest or incidence. Maturity-only pass is not D4 compliance. No probability is
assigned to the joint downside. Existing GX stays unchanged and no additional
generic avoidance or macro-feedback loss is added.

The housing calculation concerns two million **additional** awards after the
adopted million, with an explicit ramp, price basis and administration allowance.
It is not full-entitlement costing or a new poverty simulation. Care examples are
constant-2026-dollar unit arithmetic, never inserted into nominal fiscal paths.
The net-0.5%-GDP case names a funding requirement, not a chosen instrument; any
rebate/compensation has to be paid before achieving that net yield.

Generated JSON contains SHA-256 hashes of source code, assumptions, rebuilt
intermediates and relevant inputs. `MANIFEST.sha256` covers this research package;
verify from repository root with:

```bash
sha256sum -c index/tools/strategic-review/MANIFEST.sha256
```

Validation for this review: the common dry rebuild reproduced all 21 compared
products unchanged; focused checks independently verify baseline identity,
published financing comparison, ten-year loss calibration, housing exposure,
monotonic stress response and separation of care units. A second generation into
`/tmp` is compared byte for byte. Existing consistency findings remain unchanged.
Raw CPS data, current tax-law rescoring and external specialist review are outside
this bounded analysis.

## October 26: financing redesign and participation follow-up

Espen directed a wholesale financing review with participation support, institutional
responsibility, delivery remedies and a modeled climate comparison. After the common
dry rebuild above:

```bash
python3 index/tools/strategic-review/redesign.py
python3 index/tools/strategic-review/test_redesign.py
```

This writes only `sources/fiscal-redesign-first-results.md` and `.json`; use
`--output /tmp/redesign-check` for a separate deterministic comparison. Read the
results with `sources/fiscal-redesign-and-participation-2026-10-26.md`.
`redesign-assumptions.json` identifies the authored margin, service allowance,
replacement rows and stress cases. Eighteen fiscal cases solve for net revenue
requirements, not tax rates. Incremental debt/interest calculations retain existing
fund paths and do not certify D3, all D4 conditions or long-run fund solvency.

Ten climate cases call the existing Node driver with temporary configurations.
Full configurations and annual results are saved; no baseline configuration is
changed. Grid cost and delivery sensitivities are assumptions, and the `credits`
accumulator includes selected program costs but is not a full fiscal or social-cost
score. Credits-off is a diagnostic of the entire modeled bundle. New tests compare
the selected cases with stored outputs and check tax replacement, maturity margins,
outyear-versus-window stress, cost-only effects and non-additive climate results.
The package manifest covers both passes, excluding the manifest itself.
