# Models

Role: the project's models, their data and checks. Status: the legacy model suite, moved here unchanged in behavior on October 28, 2026; the core models of `charter/PLAN.md` 3.4 (household, health coverage, federal budget, energy and climate, housing, immigration, transportation) are built from it in stages C–H, each with a model card, benchmarks, tests and a run log.

| Path | Holds |
| --- | --- |
| `tools/` | Model code. `tools/readme.md` explains each step; `tools/run-all.sh` rebuilds the common suite (`--write` to update outputs) |
| `data/` | Model data: adopted inputs in `data/inputs/` (changing them is a decision for Espen), CBO extracts, generated JSON/CSV and dashboard files |

**Legacy outputs.** Until each core model replaces its part of the suite, the suite still writes its reports where they lived before: `legacy/index/` (ledger, incidence, fiscal, funds, carbon, calendar, votes, recovery budget, consistency report) and the generated companions in `legacy/sources/` (recovery audit and inventory, education reconciliation, climate portfolio, child poverty, health, strategic review, financing screens). `.github/merge-policy.json` lists the ones the gate treats as model outputs. These are the only routine changes inside `legacy/`.

**Old paths.** Cited paths in pinned evidence (the public story and front door) keep their October 28 names; the builders map `index/tools/` to `models/tools/`, `index/data/` to `models/data/`, `index/public-2050/` to `public/site/` and everything else to `legacy/`.

Run every check from the repository root: `bash .github/scripts/run-checks.sh`.
