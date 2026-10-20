# Transportation model (Moving America Act of 2031)

These scripts produce every figure in `domains/transportation-moving-america-act-2031-draft-2.md` (Draft 2, MOV-). Since Oct 20, 2026 they are one model, `moving_america.py`, and `run-all.sh` runs it: the ledger rows MOV-29, MOV-30, MOV-31 and MR1-MR6 in `ledger-build.py` now come from the model instead of being typed in.

## Running
From the repo root, Python 3.10 or later, standard library only:

```
python3 index/tools/transportation/report.py                  # Draft 2's governing printout
python3 index/tools/transportation/test_moving_america.py     # check Draft 2's figures still come out
python3 index/tools/transportation/report.py --json out.json  # the figures the ledger reads
```

`bash index/tools/run-all.sh` runs the test first and stops if a figure moved, then writes `build/moving-america.json`, which `ledger-build.py` reads.

## If a figure moves
A moved figure is a proposal for Espen, not a fix. Once agreed: update Draft 2, update `golden/final_v3.txt` (the saved printout) and `PROTECTED` in the test, then run `bash index/tools/run-all.sh --write` so the ledger and everything downstream follow.

## Files
| File | What it does |
| --- | --- |
| `moving_america.py` | The model: programs (highway, transit, rail), trust-fund receipts by source, the general-fund draw, top-ups and expansion, the 2029 and 2030 act scores, sensitivities, and `ledger_rows()` for the ledger. A `Design` holds the revenue choices (fuel steps, clean-car peg, PHEV share, shares by mode); `Model(Design(...))` runs any variant without patching other modules. |
| `report.py` | Prints every figure Draft 2 carries, in the old `final_v3.py` layout; `--json` writes the ledger figures. |
| `test_moving_america.py` | Draft 2's protected figures plus a line-for-line match against `golden/final_v3.txt`; `--legacy` also reruns the old stack (Python 3.12+). |
| `golden/final_v3.txt` | The printout of the old governing script, saved Oct 20, 2026. |
| `legacy/` | The old overlay stack (`transit_fiscal_model.py` plus overlays through `final_v3.py`, and the superseded `rev_variant*.py`), kept runnable for comparison. Each overlay patched the base model at import, so results depended on import order; `moving_america.py` replaces it. Don't edit. |
| `transit_apportionment.py` + `ntd_uza_2024.py` | Sec. 5307(i) operating-tier apportionment on NTD 2024 data (writes `apportion_fy2031.json` into the current folder). |
| `transit_pipeline_data.py` | Transit delivery pipeline (64 projects) behind the grid and map (writes `pipeline.json` into the current folder). |

Run the two supporting scripts from `build/` or a scratch folder so their output is not committed.

## Known points
- **Typed inputs.** Rail expansion by year (`RAIL_EXPANSION`, $93.20B) is typed from Draft 2's table, as it was in the old stack. So are the 2029 and 2030 act score lines other than the clean-car charge (`SCORE_2029`, `SCORE_2030`), which came from the old `funding_stack.py` run. Division E's ~$1B is set in `ledger-build.py` (`DIV_E`).
- **Share solve.** Draft 2's "equal-coverage solve 50.5/37.6/12.0" (A-7) came from the old script running the solve after its sensitivity loop, on the 25-mpg / PHEV-50% revenue path. The printout keeps that value so it matches Draft 2. On the governing design the solve is 50.0/38.2/11.8 (`report.governing_share_solve()`). Whether to restate A-7 is Espen's call.
- **Two expansion figures.** $123.70B is the expansion appropriated (sec. 105, MOV-31); $123.66B is what the general fund pays for it, because FY2036 transit receipts cover $0.04B of CIG.
- **Rounding.** The ledger takes Draft 2's figures at the precision Draft 2 prints ($0.01B for amounts, $0.1B for scores); MR6, the 25% offset, is printed net minus printed gross.

## Related files
- Decision record for the FY2032-36 calendar: `sources/transportation-calendar-fy2032-36.md`.
- Status at the merge: `sources/transportation-merge-status-oct12.md`; earlier state in the other `sources/transportation-*` files.
- The ARCA, ATRA and section-by-section docs: `sources/transportation-*-bill-architecture.md` and `sources/transportation-package-section-by-section.md`. Draft 2 governs where they differ.
