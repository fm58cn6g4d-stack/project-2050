# Climate portfolio comparison

Compares climate instruments on one common baseline: the carbon model's decided package (case `full`, written by `index/tools/carbon-model.py`), changed one named lever or combination at a time. Results feed [the allocation recommendation](../../../sources/climate-portfolio-allocation.md). It never writes canonical inputs or shared generated outputs.

Files:
- `assumptions.json`: the cases, benchmark range, bill and inflation settings, and the external cost assumptions (all planning assumptions, labeled).
- `run.js`: a driver for `../carbon/cfd-model.js` that allows per-case world overrides and keeps the power-side outlay and retail price fields.
- `portfolio.py`: builds the cases, runs the model, computes emissions against the benchmarks, outlay differences, cost per ton, REV-C1 and dividend interactions, and bills; writes `build/climate-portfolio/` and, with `--write`, `sources/climate-portfolio-model-results.{md,json}`.
- `test_portfolio.py`: reproduction and accounting checks.
- `packages.json` and `packages.py`: every combination of the eleven levers (13,824 packages); best package per budget and bill cap, the cost/abatement frontier, layering inside the recommended package, weak-delivery and 2037-repeal stress tests, ambition diagnostics and the off-model CLI-13 estimates. Writes `sources/climate-portfolio-packages.{md,json}`; the committed JSON omits the per-package rows (about 15 MB), which stay in `build/climate-portfolio/`.
- `pricing.json` and `pricing.py`: grid financing windows (grants, direct loans, capacity contracts), the credit redesign in ledger terms, LMI bill protection, the disaster preparedness and response package, the whole-package budget by D4 class, and the payment options (O1-O5) with their general-fund and dividend effects. Writes `sources/climate-portfolio-pricing.{md,json}` and `sources/climate-portfolio-disaster-components.csv`.
- `test_packages.py`: checks for the search and pricing.
- `international.json`, `international.py` and `test_international.py`: verified international mitigation, loss-and-damage and adaptation finance against the 2035 gap left after Package A. Writes `sources/climate-portfolio-international-pricing.{md,json}`.

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

## Annual payment export for recovery integration

The pricing JSON exposes each component's `budget.items[].path_bn[case][year]` and each payment option's `budget.payment[option].cases[case].annual[year]`, for 2030–50. Values are nominal billions of dollars; year keys are strings. These are **increments against the decided $150 carbon-price package**, not total government accounts. Source hashes remain in the output. No post-2050 extension is supplied.

Annual payment records separate added combustion/process receipts, CX cost, general-fund items excluding CX, channel uses and allocation, channel shortfall/surplus, direct GF receipts, process-dividend diversion, dividend change, GF net cost and D4-B net cost. Positive costs increase the deficit; negative costs are savings. Receipt changes and dividend changes can be negative. The dividend is the package increment, not the total Climate Dividend. `dividend_vs_d7_bn` isolates the payment-rule change from the existing 80/20 treatment of that increment.

For O5, GF net cost equals GF items excluding CX + CX + channel uses + dividend − added receipts. D4-B cost is separate: add it once for the whole-package deficit increment. Component paths are the decomposition, not extra costs to add on top of these totals. The $150 step's existing transition share is never new financing here. CLI-7C's expected net cost is the `reinsurance` component; contingent exposure stays separately disclosed in `disaster.rows`, not added to expected expenditure.

This export preserves the existing pricing calculations. It does not integrate the package into the canonical ledger/recovery model, price international purchases, certify D3/D4, or select strategic spending reductions.
