# Project 2050

A coherent, internally consistent set of policy options for a 2029-30 Democratic trifecta and the decades after: domain-by-domain policy files, the decisions that govern them, and the models that keep the numbers honest (a ten-year ledger, a household incidence test, and a long-term all-of-government fiscal model).

Start with `governing/project-2050-governing-decisions.md` (the authoritative decisions), then `governing/project-instructions.md` (shared working rules). `AGENTS.md`, `CLAUDE.md` and `GEMINI.md` are thin entry points for agents using this repository.

## Folders
| Folder | Role |
| --- | --- |
| `governing/` | Decisions D1-D9, design rules, decision briefs. Highest authority. |
| `domains/` | One canonical file per domain, with stable IDs (REV-, HLT-, FAM-, ...). |
| `index/` | Generated ledger and models (`index/tools/` scripts, `index/data/` data). Regenerate, don't hand-edit. `options-register.md` is the hand-written list of every option. |
| `frameworks/` | Reasoning frameworks; not current policy. |
| `sources/` | Outside inputs and source tables. |
| `staging/`, `archive/` | History and ideas only. |

## Rebuilding the numbers
```
bash index/tools/run-all.sh          # rebuild into build/ and show what changed
bash index/tools/run-all.sh --write  # copy the rebuilt files into index/
```
Needs only Python 3 (standard library).

## Using Claude, ChatGPT/Codex, Gemini or another assistant
Use a repository connection when available, or download the intended branch as a ZIP (GitHub: Code → Download ZIP) and upload only what the task needs. Always include `governing/project-instructions.md` and `governing/project-2050-governing-decisions.md`, and record their branch and commit. External copies are working copies; a connection or upload does not guarantee automatic synchronization. Then add:

| Task | Also upload |
| --- | --- |
| Decision Brief 2 (trims, scope, fiscal rule) | `index/fiscal-long-term-model.md`, `index/options-register.md`, `domains/domain-revenue.md`, `index/2029-trifecta-master-ledger.md`, `governing/decision-brief-01-senate-rules-and-gap.md` |
| Work inside one domain | that `domains/domain-*.md` file, `index/options-register.md`, and any `sources/` file it cites |
| Revenue or incidence questions | `domains/domain-revenue.md`, `index/revenue-household-incidence-model.md`, `sources/revenue-channels-and-full-menu.md` |
| Social Security | `domains/domain-social-security.md`, `domains/domain-revenue.md` |

Ask the assistant to return changes as options with their effects (the working rule), then bring the result back here, edit the files, and rerun `run-all.sh` if any number changed. Generated files in `index/` should only change by rerunning the scripts.

## Scenario calendar integration

`index/calendar-scenarios.md` and `index/calendar-scenario-explorer.html` are the current scenario presentation; `index/calendar-delivery-opportunities.md` keeps possible felt effects separate. Inputs: `index/data/inputs/calendar-scenarios.json` and the live bill inventory; milestone evidence: `sources/calendar-delivery-milestones.csv`; runner/tests: `index/tools/calendar/`. `run-all.sh` regenerates them and dashboard/calendar.json. The 172/163 display is legacy provenance. New numeric ranges are illustrative; vote parameters and fiscal/benefit profiles are unchanged. See `sources/calendar-model-review-and-integration.md` for review findings and limits.
