# Climate and grid portfolio allocation

**Status: claimed, in progress (scope stub).** Claude Code, October 26, 2026. Source base: `main` at `77f8a5e551367a52319e5323e8a33789894ebc67` (merge of PR #25). Task branch `claude/climate-portfolio`; draft PR is the visible claim. No policy, input or generated output is changed by this stub.

## Task

The queue's next substantive item and the October 26 approval: keep the clean-energy credit budget while comparing grid delivery, adaptation, workforce, procurement and marginal credits on one common cost/emissions baseline, with household bill effects and liabilities, to support an allocation decision. Do not bank unscored savings, do not turn modeled abatement into a pay-for, and do not start a general rewrite.

## Owned paths

- `sources/climate-portfolio-*.md` and `sources/climate-portfolio-*.csv`
- `index/tools/climate-portfolio/`

Read-only for this task: the carbon model (`index/tools/carbon/`, `index/tools/carbon-model.py`, `index/data/inputs/carbon-parameters.csv`), the strategic-review climate screens, the climate/revenue/transportation domains, and the shared fiscal model. Codex owns `index/tools/recovery-budget/`, shared fiscal inputs and outputs, `recovery-adoption.json` and common generated outputs (PR #24 open); this task returns proposed input deltas instead of editing them.

## Planned deliverables

1. Inventory of every climate row (CLI-1 to CLI-13, CLI-4E, REV-C1/C2/C3, the Climate Dividend, Moving America fuel-tax interaction, climate agencies from the capacity review, D7), separated into decided, accepted-for-development and option rows.
2. One common baseline on the existing carbon model: cost (budget authority vs outlays; time-limited vs permanent under D4-B), tons avoided by 2035 and 2050, cost per ton, household bill effects, liabilities (Judgment Fund contracts, loan guarantees, balance-sheet lending), delivery bottlenecks and durability under a hostile trifecta.
3. Portfolio comparison within stated envelopes against the 2050 net-zero benchmark and the 2035 NDC range. Missing prices stay unknown.
4. This recommendation, a source-backed component CSV (`sources/climate-portfolio-components.csv`), a reproducible script, proposed input deltas for Codex, and decisions for Espen.
