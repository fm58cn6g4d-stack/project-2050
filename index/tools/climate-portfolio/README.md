# Climate portfolio comparison

Compares climate instruments on one common baseline: the carbon model's decided package (case `full`, written by `index/tools/carbon-model.py`), changed one named lever or combination at a time. Results feed [the allocation recommendation](../../../sources/climate-portfolio-allocation.md). It never writes canonical inputs or shared generated outputs.

Files:
- `assumptions.json`: the cases, benchmark range, bill and inflation settings, and the external cost assumptions (all planning assumptions, labeled).
- `run.js`: a driver for `../carbon/cfd-model.js` that allows per-case world overrides and keeps the power-side outlay and retail price fields.
- `portfolio.py`: builds the cases, runs the model, computes emissions against the benchmarks, outlay differences, cost per ton, REV-C1 and dividend interactions, and bills; writes `build/climate-portfolio/` and, with `--write`, `sources/climate-portfolio-model-results.{md,json}`.
- `test_portfolio.py`: reproduction and accounting checks.
- `packages.json` and `packages.py`: every combination of the ten levers (4,608 packages); best package per budget and bill cap, the cost/abatement frontier, layering inside the recommended package, weak-delivery and 2037-repeal stress tests, ambition diagnostics and the off-model CLI-13 estimates. Writes `sources/climate-portfolio-packages.{md,json}`.
- `pricing.json` and `pricing.py`: grid financing windows (grants, direct loans, capacity contracts), the credit redesign in ledger terms, LMI bill protection, the disaster preparedness and response package, and the whole-package budget by D4 class. Writes `sources/climate-portfolio-pricing.{md,json}` and `sources/climate-portfolio-disaster-components.csv`.
- `test_packages.py`: checks for the search and pricing.

Run from the repository root (needs Python 3 and node):

```
bash index/tools/run-all.sh                               # writes build/carbon-config.json
python3 index/tools/climate-portfolio/portfolio.py --write
python3 index/tools/climate-portfolio/test_portfolio.py
python3 index/tools/climate-portfolio/packages.py --write
python3 index/tools/climate-portfolio/pricing.py --write
python3 index/tools/climate-portfolio/test_packages.py
```

Carbon-model settings added for this work, all off or at their earlier values by default (the carbon model's own outputs are unchanged): `crTruckCost` and `crHpCost` (credit cost per sale), `crVehYears` (vehicle credits' own term), `crPowerTrigger` (power-credit phase-out, Mt), `zevPath`/`zevTrkPath` (statutory zero-emission sales schedules), `ces.target2`/`ces.year2` (a second clean-power step), and a reported `credInd` row (industrial support cost estimate, not added to `credits`). Output hashes for every source file are listed at the end of the generated report.
