# Health coverage model: changelog

Role: the version history of `MOD-health-coverage`, newest first, one entry per version under the rule in `models/schema/README.md` ("Versions"). Each entry says how far the headline results moved. Status: current.

## 0.2.0 (2026-11-25)

- **Interface:** `results.json` carries the toolkit's results header (`header`: model ID, version, commit, code and input hashes, units, price basis, year type, baseline vintage, scoring convention, and the "not an official score or a benefit determination" line), stamped by `models/runlog.py`; `results.md` opens with the same block. The old top-level `model`, `version`, `status` and `run_log` keys are gone (the header holds them); `run_log`'s evidence-register note is now the top-level `evidence_register`. A minor version because the file's shape changed (before 1.0.0, a results or interface change takes a minor version).
- **New:** `--record` stamps the commit and appends a `RUN-` row to `models/runs.csv`.
- **Fix:** `model.py` with no `--out` no longer empties `MODEL-CARD.md` (it opened the card for writing before reading it).
- **Results:** no figure moved. Every key under `results`, `fy2030_39`, `benchmarks`, `uncertainty`, `baseline_checks`, `growth` and `staged_path_to_single_payer` is identical to 0.1.0's; inputs unchanged (`inputs.csv` `71db5175ffbc`, `scenarios.csv` `92cf583c7b79`).

## 0.1.0 (2026-11-10)

- First version (care dossier, stage D): 13 scenarios; 9 benchmarks, 6 pass and 3 miss (BM-1a, BM-1b, BM-3b).
