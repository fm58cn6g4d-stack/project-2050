# Carbon model

`cfd-model.js` is Espen's Carbon Dividend Model (v3.4), built in an earlier project for a different design (a $40 fee rising $8 a year, wider coverage, a 90% dividend). Its design notes, sources, checks and version history are in `sources/climate-carbon-dividend-model-notes.md`; the research baseline it started from is `sources/climate-carbon-fee-research-baseline-2026-10.md`, and the parked border-adjustment notes are `sources/climate-border-adjustment-model-notes.md`.

Files:
- `cfd-model.js`: the model (pure JavaScript, no dependencies). `CFD.simulate(policy, world, pricePath)` returns year rows 2025-2050 in 2025 dollars.
- `cfd-tests.js`: 45 regression checks (`node cfd-tests.js`); `run-all.sh` runs them before every rebuild.
- `cfd-households.js` and `cfd-cex-2024.json`: the household module on BLS Consumer Expenditure Survey 2024 tables.
- `p2050-run.js`: Project 2050's driver. It reads the cases `index/tools/carbon-model.py` writes and prints the results as JSON.

Changes made for Project 2050 (Oct 21, 2026), none of which alter the model's own default runs:
- Policy options `roadExempt`, `roadPath` and `othRoad`: gasoline and diesel can be held outside the fee and priced by their own per-gallon tax (D7, with Moving America's fuel steps as the path). Receipts then exclude road fuels.
- Rows carry `feeGasoline` (zero when road fuels are exempt), and the household module uses it, so an exempt road fuel is not counted as a fee cost.
