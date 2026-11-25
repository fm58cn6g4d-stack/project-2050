# Immigration model: changelog

Role: the version history of `MOD-immigration`, newest first, one entry per version under the rule in `models/schema/README.md` ("Versions"). Each entry says how far the headline results moved. Status: current.

## 0.1.0 (2026-11-25)

- **First version as a toolkit model** (stage H step H6). The immigration dossier's first model (`dossiers/immigration/tools/immigration_model.py` and `immigration_path.py`, board row I4, November 12) moved here; the dossier keeps thin wrappers at the old paths, so section 6, care's `status_rule.py`, the booking and the dossier's test run this code unchanged.
- **Interface:** inputs moved from the code into `parameters.csv` and `plan.csv` on the parameter schema (every value, low and high exactly as before; the filing shape and memo 1's yearly profile are rows by year; the plan's commitments, the 30,000 cap, the six years to clear and filing's opening, are `plan.csv`); `immigration_run.py` with `--out`, `--scenario`, `--print` and `--record`; `results.json` on the results schema.
- **New:** the labor-market module (`immigration_labor.py`, `labor.csv`), not booked; coded benchmarks against CRS (R47637 replayed through `court_path`), DHS (ICE custody, the asylum corps), CBO (H.R. 6, the farm bill, and the labor module's off-budget tax) and ITEP and Pope for the labor module; `court_path` takes keyword overrides (defaults unchanged) and `crs_replay` uses them.
- **Fix (printout):** "at 800 judges: FYNone" now reads "at 800 judges: not by FY2045".
- **Results:** no booked figure moved. Every line of `lines()`, `uscis()`, `eoir()`, `term_increment()`, `care_base_correction()` and the other modules is identical to the dossier tool's in all three scenarios (checked function by function); section 6's total stays +$149.0 billion over FY2030-39 and +$22.5 billion in FY2040; the booking's printout and care's `status_rule.py` are unchanged.
