# Carbon model

`cfd-model.js` is Espen's Carbon Dividend Model (v3.4), built in an earlier project for a different design (a $40 fee rising $8 a year, wider coverage, a 90% dividend). Its design notes, sources, checks and version history are in `legacy/sources/climate-carbon-dividend-model-notes.md`; the research baseline it started from is `legacy/sources/climate-carbon-fee-research-baseline-2026-10.md`, and the parked border-adjustment notes are `legacy/sources/climate-border-adjustment-model-notes.md`.

Files:
- `cfd-model.js`: the model (pure JavaScript, no dependencies). `CFD.simulate(policy, world, pricePath)` returns year rows 2025-2050 in 2025 dollars.
- `cfd-tests.js`: 53 regression checks (45 original, 8 for the Project 2050 options) (`node cfd-tests.js`); `run-all.sh` runs them before every rebuild.
- `cfd-households.js` and `cfd-cex-2024.json`: the household module on BLS Consumer Expenditure Survey 2024 tables.
- `p2050-run.js`: Project 2050's driver. It reads the cases `models/tools/carbon-model.py` writes and prints the results as JSON.

Changes made for Project 2050 (Oct 21, 2026), none of which alter the model's own default runs:
- Policy options `roadExempt`, `roadPath` and `othRoad`: gasoline and diesel can be held outside the fee and priced by their own per-gallon tax (D7, with Moving America's fuel steps as the path). Receipts then exclude road fuels.
- Rows carry `feeGasoline` (zero when road fuels are exempt), and the household module uses it, so an exempt road fuel is not counted as a fee cost.
- Policy options `ces` (CLI-3: `{ start, target, year }`; a tradable-credit Clean Energy Standard modeled as a credit price on fossil MWh that moves each year toward the level meeting a straight path to the target, capped at the alternative compliance payment `cesAcp`), `gridStatute` (CLI-6: extra transmission growth `gsTx` and usable wind and solar share `gsCurt`) and `weatherize` (CLI-5: Weatherization heat pumps in `wxHomes` million homes a year). All three magnitudes are assumptions, set in `models/data/inputs/carbon-parameters.csv`. Rows carry `cleanShare`, `cesPrice`, `cesTarget` and `cesAcp` (payments, $bn).
- Eight added checks in `cfd-tests.js` cover these options.
- Settings added Oct 26, 2026 for `models/tools/climate-portfolio/`, all defaulting to earlier behavior so every earlier output is unchanged: `crTruckCost` and `crHpCost` (average 45W and 25C credit per sale, formerly hard-coded at $20,000 and $3,000); `crVehYears` (vehicle credits' own term; null uses `crYears`); `crPowerTrigger` (power-credit phase-out trigger, formerly hard-coded at 383 Mt); `zevPath` and `zevTrkPath` (optional statutory zero-emission sales schedules, `{year: share}`); `ces.target2`/`ces.year2` (an optional second clean-power step); and a reported `credInd` row field (an estimate of industrial support cost, not added to `credits`).
