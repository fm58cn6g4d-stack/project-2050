# Household model: changelog

Role: the version history of `MOD-household`, newest first, one entry per version under the rule in `models/schema/README.md` ("Versions"). Each entry says how far the headline results moved. Status: current.

## 0.3.0 (2026-11-25)

The ledger snapshot (`snapshot/ledger.json`) updated for stage G step 11's rebooking of IMM-1 (I1 A, `DEC-2026-11-25-27`: the status line on CBO's on-budget figure for H.R. 6, the ledger midpoint from $0.169T to $0.179T). No code or interface change.
- Results: the ledger's gap figures in `results.json` move by $0.01T (`gap_mid` 7.66 to 7.67, `gap_after_accepted` 3.15 to 3.16). No household, poverty, take-home or D3 figure moved.

## 0.2.0 (2026-11-25)

Step H3 of stage H: the model brought to the toolkit standard.

- **Interface:** `results.json` and `results.md` carry the toolkit's results header (model ID, version, status, commit, the hashes of every code and input file, units, price basis, year type, baseline vintage, scoring convention, scenarios, uncertainty, and the "not an official score or a benefit determination" line), stamped by `models/runlog.py`. `run.py` takes `--ledger` as an option (it was required), starts from `snapshot/ledger.json` when `build/ledger.json` is absent, and has `--record` and `--update-snapshot`. A minor version because the results file's shape changed (before 1.0.0, a results or interface change takes a minor version).
- **New:** `parameters.csv`, the model's current-law inputs (income tax, credits, payroll tax, SNAP, the poverty guideline), the SNAP work-rule calibration's inputs and the CBO-convention check's working values, on `models/schema/parameters.py`; `params.py`, `snap2025.py` and `conventions.py` read them (the 2025 law dictionary built from the file equals the old literal, checked). The card's evidence table is generated from it.
- **New:** `snapshot/ledger.json`; `fetch_cps.py` (downloads the CPS archive and checks its SHA-256); a validation table written by the test code (23 benchmarks, 9 pass and 14 miss, most of the misses the TPC denominator gap); a known-issues list; this changelog.
- **Changed (data boundary):** `intervals.py` no longer imports `health_cost_review.py` or `health_financing.py`: it reads their per-unit take-home results from `take-home-flags.csv.gz` (`take-home-flags.md`). Rerun on the Census archive, it gives the committed `intervals.json`'s `take_home` block exactly. `intervals.json` itself is not refreshed (its D3 block predates the settlement; Known issues).
- **Seeds:** none to fix. Nothing in the model draws random numbers (the intervals are successive difference replication); a test checks that no module imports `random`.
- **Results:** no figure moved. Every key outside `header` in `results.json` is identical to 0.1.0's (checked, and `results.md` differs from it in its header block only). The model code hashes changed (`params.py`, `snap2025.py`, `conventions.py`, `run.py`, `provisions.py`, `intervals.py`), and the inputs list now names `parameters.csv`, `take-home-flags.csv.gz` and the ledger snapshot.

## 0.1.0 (2026-11-24)

- The model as it stood at the financing settlement (#480), versioned retroactively in step H3 (it had no version and no results header). It is maintenance step M3's work (parts 1 and 2: the 2029 baseline, the provision interface, the D3 report, the secure floor's INC-1 to INC-5, the typical families, the 65-cent ceiling check, the replicate-weight intervals and the CBO-convention check) plus the stage G changes to its keys, rules and D3 scenarios (Q-H7 on 2026-11-20 and Q-G on 2026-11-24).
- The run-log rows from `RUN-household-2026-11-18-a` to `RUN-household-2026-11-24-a` in `models/runs.csv` are runs at the commits that changed `results.json`, back-filled and labeled 0.1.0 although the keys, rules and D3 scenarios changed between them: one version for the whole span, because the project did not number versions then. The hand-written runs a to g of 2026-11-13 and 2026-11-16 are in the card.
