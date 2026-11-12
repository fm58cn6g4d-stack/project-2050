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
- **Sources and evidence** (`DEC-2026-10-28-07`). Any credible source may be used, government or not; its rights decide how it enters the library (`library/README.md`). Every evidence entry says whether it is data (a measured fact) or analysis (an interpretation: causes, effects, projections, models). Grade by the kind of evidence, not the publisher: an agency's causal account is analysis. Record who published an analysis, when and with what stake; check a report's headline against its own numbers; and rely on an analysis only once an independent publisher supports or qualifies it, presenting both views where one contests it. Executive-branch sources (agencies, the White House Council of Economic Advisers, OMB, executive orders) carry the administration that produced them. Their analysis gets skepticism in proportion to the administration's record of politicized analysis: most for the second Trump administration (2025 on), which has staffed for loyalty first, then the first Trump administration, with Obama- and Biden-era analysis checked as usual, and more where warranted (`DEC-2026-10-30-01`). The registry checker checks each entry's data-or-analysis label, its grade and its corroboration links; the rest of the method is in `dossiers/TEMPLATE.md`.
- **Web search.** When Firecrawl is unavailable or out of credits, switch to Exa or another web search and fetch tool and carry on; don't stop or wait for Firecrawl. Espen is not buying more Firecrawl usage (`DEC-2026-11-12-02`).
- Espen's Google Drive is not a project source; do not search it for project work.

**Session routine.**
1. Read this page and `charter/PROGRESS.md`. Check open PRs.
2. Claim one step: the lead names it in your brief. Open your PR early, as a draft if the step is long, with the step in its title.
3. Read that dossier's files and the evidence it needs.
4. Do the step. One dossier step per session.
5. Run the checks.
6. Write the board update in your PR description, under "For the board": done, next, and open questions for Espen. Only the lead edits `charter/PROGRESS.md`, folding these in a few times a day; a worker edits it only when no lead is live (`DEC-2026-11-12-03`).
7. Open one coherent PR and mark it ready when done.

**Choosing the model for the work.** Use the lightest model that can do the step well, and the strongest where care and judgment matter: errors in large, interconnected datasets propagate, so mistakes there cost more than the tokens saved.

| Tier | Use for | Examples |
| --- | --- | --- |
| **Light** (Haiku-class) | Mechanical work with a clear spec and automatic checks | File moves and link updates; regenerating outputs; running checks; formatting; updating the board; gathering `library/` catalog facts by script; extracting text from originals |
| **Standard** (Sonnet-class) | Structured work needing some judgment within a settled design | Cataloguing (status, aliases, rights); drafting evidence entries; model code and tests to a written spec; dossier sections from existing evidence; checklist reviews |
| **Most capable** (Opus-class) | Strategy, design, synthesis, and work where an error would spread | Design choices and decision memos; dossier problem, design and specification sections; reconciling conflicting evidence; model design and integrating the household, health and budget models; adversarial milestone reviews; legal and constitutional analysis; public briefs |

- Every step on `charter/PROGRESS.md` names its tier.
- A lighter model that meets ambiguity stops and leaves a note in its PR for a stronger session, and tells its report-back address; it doesn't guess.
- Strong sessions delegate mechanical subtasks to lighter subagents where the tools allow, and check the results.
- When unsure, go one tier up. The same tiers apply to other vendors' agents, by capability.

**Merge categories.** The merge gate (`.github/merge-policy.json`, details in `legacy/governing/project-collaboration.md`) applies them.
- **Routine** (gate tiers 1–2): research, evidence, library, models, dossier drafts, the board, and public pages that change no commitment. These merge once checks pass and another agent has reviewed the current head.
- **Decisions** (tier 3): the charter, the flagship list, adopted model inputs (`models/data/inputs/`), design choices at real forks, new or removed programs, the merge rules and entry files (`.github/`, `AGENTS.md`, `CLAUDE.md`, `GEMINI.md`), and anything labeled `needs-espen`. These merge only after Espen adds `espen-approved` themselves. Agents never apply `espen-approved` or `espen-override` and never enable auto-merge on a tier-3 PR.
- Keep routine and decision changes in separate PRs.
- Every PR description carries `Agent-Author: <claude-code|codex|gemini> <session id>`. A reviewing agent reads the diff at the head and comments `Agent-Review: approve` (or `changes-requested`), `Reviewed-Head: <full SHA>` and `Reviewer: <agent> <session id>`.

**Milestone review.** A second agent reviews each dossier against the checklist at L2 and again at L3, trying to break it: weak evidence, missing populations, optimistic assumptions, cheaper alternatives. At each stage boundary Espen holds a short strategic review.

**Design lens: guide, don't police.** Prefer designs that are simple for the people served and for the agencies running them. Each eligibility test, document, deadline, cap or quota has to earn its place against the burden it adds, because such burdens fall hardest on the people in the worst situations and they raise running costs. Prefer one plain test, self-attestation and records the government already holds, local judgment based on need, and published counts with a review trigger, over strict structures enforced up front. Accept that not every group will be served in exactly the share the design projects; correct with monitoring, not with more rules. Recommendations say what each requirement costs in burden, as well as what it buys. (`DEC-2026-11-09-13`)

**Fiscal rule in dossiers: report, don't gate.** Each dossier prices everything honestly and reports its fiscal-rule effect: yearly cost, permanent cost from FY2040, and its share of the plan-wide margin. It passes that to the financing settlement, the one place where the plan is balanced, plan-wide, once more of it is specified. A dossier's own gap in a test year is not a defect to fix and is not put to Espen by itself. A cost goes to Espen when the choice is mainly about money: designs that reach the same people at very different cost, or a cost well above comparable programs. The budget model keeps a running plan-wide total so drift stays visible. (`DEC-2026-11-10-05`)

**What needs an answer now.** Specify what government commits to do; don't try to predict everything that follows from it. Before extending a research or specification task, ask: what decision would a different answer change? Treat each question one of four ways. *Decide now* when the answer defines the commitment (eligibility, benefit, authority, agency, rights); real forks stay Espen's. *Use a working assumption* when a number is needed for budgeting or comparison, with its basis, range and the cost of being wrong. *Leave it open* when several outcomes are reasonable and none changes today's choice; record the alternatives and what finding would make it matter. *Study it in implementation* when pilots or administrative experience will answer it better than desk research, without a new reporting burden. An uncertainty belongs on the critical path only when a plausible answer would change the choice, undermine the commitment, or expose a legal or delivery obstacle. Reviewers treat unsupported claims stated as settled, inconsistent commitments, decision-changing omissions and missing delivery mechanisms as defects; a clearly bounded uncertainty is not one. A reviewer who asks for more investigation says which decision it would inform and whether it blocks that decision now. (`DEC-2026-11-10-07`)

**Decision memos.** At each real fork Espen gets two to four options, a recommendation and the consequences of each, in the dossier's design section, with a `DEC-` entry in `charter/decisions.md` once decided. Approval is per decision, never as a package.

**Sessions and handoffs.** A Claude Code session starts another session only to take a ready board step, to run independent work in parallel, to run a large batch at a better-suited tier, or for an independent review. It never starts one for a small subtask, for work a live session already holds, or for a step that waits on Espen. At most three Claude sessions work at once. Each new session gets a standalone brief and reports back when its PR is ready. Messages between sessions only alert another session to work: whatever the other session must know goes in the PR, on the board or in the dossier. Reach Codex with a PR comment. The mechanics are in `.claude/skills/sessions/SKILL.md`.

**Roles.** Claude leads the dossiers, the federal budget model with its shared fiscal inputs (`DEC-2026-11-08-02`) and fair financing, the financing settlement (`DEC-2026-11-11-07`); changing adopted inputs in `models/data/inputs/` stays Espen's decision. Codex review is not required for the budget model or the financing settlement: they merge on the Claude reviewer's review, like other work (`DEC-2026-11-12-01`). At most two dossiers are active at once.
