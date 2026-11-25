# Health coverage model: changelog

Role: the version history of `MOD-health-coverage`, newest first, one entry per version under the rule in `models/schema/README.md` ("Versions"). Each entry says how far the headline results moved. Status: current.

## 0.3.0 (2026-11-25)

- **Interface:** `inputs.csv` is on the toolkit's parameter schema (`models/schema/parameters.py`): the column `evidence_id_or_basis` is now `source`, there is a new `year` column (the year each value is for: `2032`, `FY2025-FY2034`, `none` for a ratio), and the year or span that was written into some units (`$ billion, 2024`) moved from `unit` to `year`. No row, value, range or kind changed. The card's evidence table is generated from the file.
- **Status:** `exploratory` is now `working` (the care dossier's flagship 2 figures rest on the model; it has tests and a validation table). Neither "preview" nor "released": memo H1 is undecided.
- **Validation:** the benchmarks are `models/schema/validation.py` records in `test_model.py`, which writes the card's validation table and fails when it is stale. The three misses (BM-1a, BM-1b, BM-3b) are kept. The table counts BM-2 and BM-3a as in-sample, so the card now reads "7 independent: 4 pass, 3 miss" where it read "6 of 9 pass".
- **Fix (text):** the explanations of BM-1a and BM-1b said the low single-payer corner is outside CBO's range; it is inside, and only the high corner misses. The card is on the template; it lists the 78 assumptions that no register entry measures, and has a known-issues list.
- **Results:** no figure moved. Every key outside `header` in `results.json` is identical to 0.2.0's (checked); `results.md` changed in its header block only (version, status, input hash, and "Exploratory analysis" reads "Analysis"). Inputs: `inputs.csv` `a394a7a04284` (was `71db5175ffbc`), `scenarios.csv` unchanged.

## 0.2.0 (2026-11-25)

- **Interface:** `results.json` carries the toolkit's results header (`header`: model ID, version, status, commit, code and input hashes, units, price basis, year type, baseline vintage, scoring convention, the scenarios it holds, an uncertainty statement, and the "not an official score or a benefit determination" line), stamped by `models/runlog.py`; `results.md` opens with the same block. The old top-level `model`, `version`, `status` and `run_log` keys are gone (the header holds them); `run_log`'s evidence-register note is now the top-level `evidence_register`. A minor version because the file's shape changed (before 1.0.0, a results or interface change takes a minor version).
- **New:** `--record` stamps the commit and appends a `RUN-` row to `models/runs.csv`.
- **Fix:** `model.py` with no `--out` no longer empties `MODEL-CARD.md` (it opened the card for writing before reading it).
- **Results:** no figure moved. Every key under `results`, `fy2030_39`, `benchmarks`, `uncertainty`, `baseline_checks`, `growth` and `staged_path_to_single_payer` is identical to 0.1.0's; inputs unchanged (`inputs.csv` `71db5175ffbc`, `scenarios.csv` `92cf583c7b79`).

## 0.1.0 (2026-11-10)

- First version (care dossier, stage D): 13 scenarios; 9 benchmarks, 6 pass and 3 miss (BM-1a, BM-1b, BM-3b).
