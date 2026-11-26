# Federal budget model: changelog

Role: the version history of `MOD-budget` (`models/schema/README.md`, "Versions"), newest first. Status: current.

## 0.4.0 (2026-11-25)

Stage G step 11: the health fund booked as its own account (`DEC-2026-11-25-28`, `-30` to `-32`) and IMM-1 rebooked (I1 A, `-27`).
- **Interface:** the engine (`recovery-budget/model.py`) has a `health_fund()` account. Each case's rows add `health_fund_sources_bn`, `health_fund_spending_bn`, `health_fund_gf_transfer_bn` and `health_fund_reserve_bn`, and each case adds `health_fund`. The general fund's gap counts only the transfer to the fund. The settlement's S06 takes a rate path (`settlement.json`), and the funds model a third `direct` Social Security line, IMM-1-SS.
- **Results:** the plan's debt in FY2056 is 129.3% of GDP, down from 131.5% in 0.3.0: 2.0 points from the fund's rule and 0.1 from IMM-1. FY2040 stays 117.8%. The plan's general-fund gap moves in FY2030-35 with the fund holding its early surplus; unified figures don't. Current law and the CBO option didn't move: their headers change only in the hashes of the changed inputs.

## 0.3.0 (2026-11-25)

The plan's figures moved with CLI-1's step-down after FY2039 (memo G25; #493's `fiscal-after.csv` row): a new input, no change to the code or the interface.
- Results: the plan (`results/plan.json`) has debt at 131.5% of GDP in FY2056, 1.6 points below 0.2.0's 133.1%; FY2040 stays 117.8%. Current law and the CBO option did not move; their headers change only in the hash of `fiscal-after.csv`.

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
