# Federal budget model: changelog

Role: the version history of `MOD-budget` (`models/schema/README.md`, "Versions"), newest first. Status: current.

## 0.2.0 (2026-11-25)

Stage H step H4: the model released to the toolkit standard (not marked "released": memo H1 is undecided).
- One command, `run.py --reform FILE --out DIR`, from a fresh clone: the baseline, ledger, paths and funds into DIR, then the reform against current law. Current law is the default; `reforms/` ships current law, a neutral CBO option (Mandatory Spending Option 2, SRC-1855) and the plan as booked (case `mixed`).
- The engine (`fiscal-model.py`, `fiscal-data.py`, `fiscal-profiles.py`, `ledger-build.py`, `funds-model.py`, `climate-integration.py`, `window.py` and four tests) moved to `engine/`, with shims at the old paths; `fiscal-model.py` takes `--out-dir`. The plan's bookings and dossier tools moved to `models/bookings/`.
- The card on `models/MODEL-CARD-TEMPLATE.md`: evidence map from `parameters.csv`, the owner role, `MOD-budget`, status working, the validation-convention table, known issues.
- Results on the toolkit's schema: `results/*.json` with the header.
- Results: no figure moved. `run-all.sh` reproduces every committed figure; only the source hashes in `recovery-budget.json` and `fiscal-recovery-model.json` changed, because the engine files they hash moved.

## 0.1.0 (2026-11-12)

The budget model as built in pieces B1 to B6 (`WORKFLOW.md`): the data layer, the provision library, the benchmarks (B4 milestone met by `DEC-2026-11-12-11`), the viewer. No results header; versioned here for the first time.
- Results: the reference figures before step H4.
