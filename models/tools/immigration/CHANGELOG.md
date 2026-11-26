# Immigration model: changelog

Role: the version history of `MOD-immigration`, newest first, one entry per version under the rule in `models/schema/README.md` ("Versions"). Each entry says how far the headline results moved. Status: current.

## 0.2.0 (2026-11-25)

- **Change (I1 A, `DEC-2026-11-25-27`; the booking rule, `-28`):** the status line (`status_fiscal`) scales CBO's on-budget deficit figure for H.R. 6, $42.48 billion (EV-IMM-669, read from the PDF), instead of the unified $35.33 billion; a new `status_offbudget()` scales CBO's off-budget figure (−$7.15 billion: payroll tax less added Social Security benefits) the same way, with no health netting, for the booking's Social Security line (IMM-1-SS). Parameters: `hr6_deficit_bn` replaced by `hr6_onbudget_deficit_bn` and `hr6_offbudget_deficit_bn`. BM-CBO-1 and BM-CBO-3 read the on-budget figure. The results file adds `path.status_off_budget` (an interface addition).
- **Results:** memo 1's line rises from $50.5 billion to $60.8 billion over FY2030-39 (central; low $67.1 billion, high $55.0 billion) and from $10.1 billion to $12.2 billion in FY2040; section 6's general-fund total from +$149.0 billion to +$159.2 billion over FY2030-39 and from +$22.5 billion to +$24.6 billion in FY2040. Social Security's funds gain $22.2 billion over FY2030-39 and $4.4 billion in FY2040. No other line moved.

## 0.1.0 (2026-11-25)

- **First version as a toolkit model** (stage H step H6). The immigration dossier's first model (`dossiers/immigration/tools/immigration_model.py` and `immigration_path.py`, board row I4, November 12) moved here; the dossier keeps thin wrappers at the old paths, so section 6, care's `status_rule.py`, the booking and the dossier's test run this code unchanged.
- **Interface:** inputs moved from the code into `parameters.csv` and `plan.csv` on the parameter schema (every value, low and high exactly as before; the filing shape and memo 1's yearly profile are rows by year; the plan's commitments, the 30,000 cap, the six years to clear and filing's opening, are `plan.csv`); `immigration_run.py` with `--out`, `--scenario`, `--print` and `--record`; `results.json` on the results schema.
- **New:** the labor-market module (`immigration_labor.py`, `labor.csv`), not booked; coded benchmarks against CRS (R47637 replayed through `court_path`), DHS (ICE custody, the asylum corps), CBO (H.R. 6, the farm bill, and the labor module's off-budget tax) and ITEP and Pope for the labor module; `court_path` takes keyword overrides (defaults unchanged) and `crs_replay` uses them.
- **Fix (printout):** "at 800 judges: FYNone" now reads "at 800 judges: not by FY2045".
- **Results:** no booked figure moved. Every line of `lines()`, `uscis()`, `eoir()`, `term_increment()`, `care_base_correction()` and the other modules is identical to the dossier tool's in all three scenarios (checked function by function); section 6's total stays +$149.0 billion over FY2030-39 and +$22.5 billion in FY2040; the booking's printout and care's `status_rule.py` are unchanged.
