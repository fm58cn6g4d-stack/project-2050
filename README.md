# Project 2050

A coherent, internally consistent set of policy options for a 2029-30 Democratic trifecta and the decades after: domain-by-domain policy files, the decisions that govern them, and the models that keep the numbers honest (a ten-year ledger, a household incidence test, and a long-term all-of-government fiscal model).

Start with `CLAUDE.md` (the rules any assistant should follow here) and `governing/project-2050-governing-decisions.md` (the decisions).

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

## Using another chat assistant (for example HopGPT) with these files
Chat tools usually take uploaded files rather than a repo. Download the repo as a zip (GitHub: Code → Download ZIP), then upload only what the task needs. Always include `CLAUDE.md` and `governing/project-2050-governing-decisions.md`, then add:

| Task | Also upload |
| --- | --- |
| Decision Brief 2 (trims, scope, fiscal rule) | `index/fiscal-long-term-model.md`, `index/options-register.md`, `domains/domain-revenue.md`, `index/2029-trifecta-master-ledger.md`, `governing/decision-brief-01-senate-rules-and-gap.md` |
| Work inside one domain | that `domains/domain-*.md` file, `index/options-register.md`, and any `sources/` file it cites |
| Revenue or incidence questions | `domains/domain-revenue.md`, `index/revenue-household-incidence-model.md`, `sources/revenue-channels-and-full-menu.md` |
| Social Security | `domains/domain-social-security.md`, `domains/domain-revenue.md` |

Ask the assistant to return changes as options with their effects (the working rule), then bring the result back here, edit the files, and rerun `run-all.sh` if any number changed. Generated files in `index/` should only change by rerunning the scripts.
