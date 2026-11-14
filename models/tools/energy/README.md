# Energy and climate model (M4)

Role: the home of `MOD-energy`, the core energy and climate model of `charter/PLAN.md` 3.4 (emissions, prices, bills, dividends; flagship 4, clean power). Status: **working** (part 2 of step M4, `DEC-2026-11-13-09`): the model runs clean power's decided set; `MODEL-CARD.md` says what it answers, its evidence, benchmarks and limits.

| File | What |
| --- | --- |
| `survey.md` | Part 1: the validated energy and climate policy models used for U.S. policy analysis, what each can teach this model, and the recommended design |
| `MODEL-CARD.md` | What the model answers and cannot, its evidence map, mechanisms, benchmarks, limits and interfaces |
| `run.py` | One command: runs every scenario and benchmark and writes `results.json` and `results.md` (generated; do not edit) |
| `model.py`, `engine.js`, `data.py` | Scenarios and accounts; the driver for the engine (`models/tools/carbon/cfd-model.js`); the data layer |
| `assumptions.csv` | This model's labeled working assumptions, with ranges; adopted inputs stay in `models/data/inputs/` |
| `test_energy.py` | Tests, run by `run-all.sh` before every rebuild |

- Sources: **source IDs numbered 5000 to 5099 are reserved for this model** (this README, November 13, 2026; `library/reserved-blocks.csv`).
- Starting material: `models/tools/carbon/` (Espen's Carbon Dividend Model v3.4), `models/tools/carbon-model.py`, `models/tools/climate-portfolio/`, and the legacy notes they cite.
