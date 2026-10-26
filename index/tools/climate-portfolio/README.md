# Climate portfolio comparison

Compares climate instruments on one common baseline: the carbon model's decided package (case `full`, written by `index/tools/carbon-model.py`), changed one named lever or combination at a time. Results feed [the allocation recommendation](../../../sources/climate-portfolio-allocation.md). It never writes canonical inputs or shared generated outputs.

Files:
- `assumptions.json`: the cases, benchmark range, bill and inflation settings, and the external cost assumptions (all planning assumptions, labeled).
- `run.js`: a driver for `../carbon/cfd-model.js` that allows per-case world overrides and keeps the power-side outlay and retail price fields.
- `portfolio.py`: builds the cases, runs the model, computes emissions against the benchmarks, outlay differences, cost per ton, REV-C1 and dividend interactions, and bills; writes `build/climate-portfolio/` and, with `--write`, `sources/climate-portfolio-model-results.{md,json}`.
- `test_portfolio.py`: reproduction and accounting checks.

Run from the repository root (needs Python 3 and node):

```
bash index/tools/run-all.sh                               # writes build/carbon-config.json
python3 index/tools/climate-portfolio/portfolio.py --write
python3 index/tools/climate-portfolio/test_portfolio.py
```

The two carbon-model settings `crTruckCost` and `crHpCost` (average 45W and 25C credit per sale) let a case remove a credit's cost along with its effect; their defaults reproduce the earlier hard-coded values, so the carbon model's own outputs are unchanged. The model books no cost for industrial support, so those cases are marked unpriced. Output hashes for every source file are listed at the end of the generated report.
