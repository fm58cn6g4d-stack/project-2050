# Project 2050: standards

Role: the one page every agent session reads first, with `charter/PROGRESS.md`. Status: current (stage A, October 28, 2026). The plan it serves is `charter/PLAN.md`.

**Who decides.** Espen Swanson owns the project and uses they/them pronouns. Espen decides goals, the flagship list, design choices at real forks and anything that changes what the project commits to. Agents decide project elements in service of those goals and record why. Agents never contact other people on Espen's behalf. Espen is not a programmer: write to them plainly and briefly, and run commands yourself.

**Time frame.** The project is written now, from the data, research and law available today, but it recommends a governing plan that begins in January 2029. Everything is aimed at a strategy ready to carry out from 2029 on. Two narrow exceptions are labeled as such: what to attempt under divided government in 2027-28, and the preparation needed between now and January 2029. So state the current-law baseline as it will stand in 2029, counting enacted laws with later effective dates and scheduled expirations; date recommendations from 2029 on; and treat earlier dates as preparation, not launch. (`DEC-2026-10-29-01`)

**Where things live.** Anything outside these folders is not current work.

| Folder | Holds |
| --- | --- |
| `charter/` | Plan, these standards, progress board, outcomes record, decision log |
| `dossiers/` | One folder per flagship, foundation and started agenda topic (plan 3.3) |
| `agenda/` | `agenda.csv`: every policy and option ID, with level and status |
| `library/` | Originals and text versions, the catalog and the generated name index |
| `models/` | Model code (`models/tools/`), data (`models/data/`), model cards, the registry checker |
| `public/` | The site (`public/site/`), briefs and organizing material |
| `legacy/` | The tree as of October 28, 2026. Read-only: cite it, never extend it |

The legacy model suite still writes its generated reports into `legacy/index/` and `legacy/sources/` until each core model is rebuilt in `models/` (`models/README.md` lists them). Those regenerated outputs are the only routine changes inside `legacy/`.

**How agents work.** The repository is the only memory; every session can start cold.
- Keep files small and self-describing: role and status at the top, no dated history in canonical files (history goes in the decision log or Git).
- Cross-reference by stable ID (`SRC-0001`, `EV-HOU-001`, `HOU-4A`, `HOU-4A.01`, `DEC-2026-10-28-01`, `OUT-01`, `MOD-household`); plan section 4 lists them all. One canonical home per fact. Generated indexes are rebuilt by script, never hand-edited.
- Rely on checks, not memory: `bash .github/scripts/run-checks.sh` runs the full rebuild, drift check and tests.
- Licensed or paywalled material is cited and briefly quoted, never committed: the repository is public.
- **Sources and evidence** (`DEC-2026-10-28-07`). Any credible source may be used, government or not; its rights decide how it enters the library (`library/README.md`). Every evidence entry says whether it is data (a measured fact) or analysis (an interpretation: causes, effects, projections, models). Grade by the kind of evidence, not the publisher: an agency's causal account is analysis. Record who published an analysis, when and with what stake; check a report's headline against its own numbers; and rely on an analysis only once an independent publisher supports or qualifies it, presenting both views where one contests it. The registry checker checks each entry's data-or-analysis label, its grade and its corroboration links; the rest of the method is in `dossiers/TEMPLATE.md`.
- Espen's Google Drive is not a project source; do not search it for project work.

**Session routine.**
1. Read this page and `charter/PROGRESS.md`. Check open PRs.
2. Claim one step on the board (in your PR, opened early as a draft if the step is long).
3. Read that dossier's files and the evidence it needs.
4. Do the step. One dossier step per session.
5. Run the checks.
6. Update the board: done, next, and open questions for Espen.
7. Open one coherent PR and mark it ready when done.

**Choosing the model for the work.** Use the lightest model that can do the step well, and the strongest where care and judgment matter: errors in large, interconnected datasets propagate, so mistakes there cost more than the tokens saved.

| Tier | Use for | Examples |
| --- | --- | --- |
| **Light** (Haiku-class) | Mechanical work with a clear spec and automatic checks | File moves and link updates; regenerating outputs; running checks; formatting; updating the board; gathering `library/` catalog facts by script; extracting text from originals |
| **Standard** (Sonnet-class) | Structured work needing some judgment within a settled design | Cataloguing (status, aliases, rights); drafting evidence entries; model code and tests to a written spec; dossier sections from existing evidence; checklist reviews |
| **Most capable** (Opus-class) | Strategy, design, synthesis, and work where an error would spread | Design choices and decision memos; dossier problem, design and specification sections; reconciling conflicting evidence; model design and integrating the household, health and budget models; adversarial milestone reviews; legal and constitutional analysis; public briefs |

- Every step on `charter/PROGRESS.md` names its tier.
- A lighter model that meets ambiguity stops and leaves a note on the board for a stronger session; it doesn't guess.
- Strong sessions delegate mechanical subtasks to lighter subagents where the tools allow, and check the results.
- When unsure, go one tier up. The same tiers apply to other vendors' agents, by capability.

**Merge categories.** The merge gate (`.github/merge-policy.json`, details in `legacy/governing/project-collaboration.md`) applies them.
- **Routine** (gate tiers 1–2): research, evidence, library, models, dossier drafts, the board, and public pages that change no commitment. These merge once checks pass and another agent has reviewed the current head.
- **Decisions** (tier 3): the charter, the flagship list, adopted model inputs (`models/data/inputs/`), design choices at real forks, new or removed programs, the merge rules and entry files (`.github/`, `AGENTS.md`, `CLAUDE.md`, `GEMINI.md`), and anything labeled `needs-espen`. These merge only after Espen adds `espen-approved` themselves. Agents never apply `espen-approved` or `espen-override` and never enable auto-merge on a tier-3 PR.
- Keep routine and decision changes in separate PRs.
- Every PR description carries `Agent-Author: <claude-code|codex|gemini> <session id>`. A reviewing agent reads the diff at the head and comments `Agent-Review: approve` (or `changes-requested`), `Reviewed-Head: <full SHA>` and `Reviewer: <agent> <session id>`.

**Milestone review.** A second agent reviews each dossier against the checklist at L2 and again at L3, trying to break it: weak evidence, missing populations, optimistic assumptions, cheaper alternatives. At each stage boundary Espen holds a short strategic review.

**Decision memos.** At each real fork Espen gets two to four options, a recommendation and the consequences of each, in the dossier's design section, with a `DEC-` entry in `charter/decisions.md` once decided. Approval is per decision, never as a package.

**Sessions and handoffs.** A Claude Code session starts another session only to take a ready board step, to run independent work in parallel, to run a large batch at a better-suited tier, or for an independent review. It never starts one for a small subtask, for work a live session already holds, or for a step that waits on Espen. At most three Claude sessions work at once. Each new session gets a standalone brief and reports back when its PR is ready. Messages between sessions only alert another session to work: whatever the other session must know goes in the PR, on the board or in the dossier. Reach Codex with a PR comment. The mechanics are in `.claude/skills/sessions/SKILL.md`.

**Roles.** Codex leads the federal budget model and fair financing. Claude leads the dossiers. Each reviews the other's work at milestones. At most two dossiers are active at once.
