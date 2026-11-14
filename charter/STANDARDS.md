# Project 2050: standards

Role: the rules every agent session follows. Read this page first, then `charter/PROGRESS.md`. Status: current. The plan it serves is `charter/PLAN.md`; decisions are in `charter/decisions.md`; how sessions start, hand over and message each other is in `.claude/skills/sessions/SKILL.md`.

## Who decides

- Espen Swanson owns the project and uses they/them pronouns.
- **Espen decides:** goals, the flagship list, design choices at real forks, and anything that changes what the project commits to.
- **Agents decide:** project elements in service of those goals, and record why.
- Agents never contact other people on Espen's behalf.

## Working with Espen

- Espen is not a programmer. Write plainly and briefly, and run commands yourself.
- Give short updates with numbered, one-line asks.
- Espen answers in the lead session. The lead records each answer as a `DEC-` entry in `charter/decisions.md`, with Espen's own words, in one tier-3 PR per round of answers. Each item is still decided on its own (see "Decision memos").
- If Espen is messaging about Project 2050 after 12:30 am Eastern, tell them to go to bed (Espen, November 11).

## Time frame

The project is written now, from today's data, research and law, but it recommends a governing plan that begins in January 2029 (`DEC-2026-10-29-01`).
- State the current-law baseline as it will stand in 2029, counting enacted laws with later effective dates and scheduled expirations.
- Date recommendations from 2029 on.
- Two narrow exceptions are labeled as such: what to attempt under divided government in 2027-28, and preparation between now and January 2029.

## Where things live

Anything outside these folders is not current work.

| Folder | Holds |
| --- | --- |
| `charter/` | Plan, these standards, progress board, outcomes record, decision log |
| `dossiers/` | One folder per flagship, foundation and started agenda topic (plan 3.3) |
| `agenda/` | `agenda.csv`: every policy and option ID, with level and status |
| `library/` | Originals and text versions, the catalog and the generated name index |
| `models/` | Model code (`models/tools/`), data (`models/data/`), model cards, the registry checker |
| `public/` | The site (`public/site/`), briefs and organizing material |
| `legacy/` | The tree as of October 28, 2026. Read-only: cite it, never extend it |

The legacy model suite still writes its generated reports into `legacy/index/` and `legacy/sources/` until each core model is rebuilt in `models/` (`models/README.md`). Those regenerated outputs are the only routine changes inside `legacy/`.

## How agents work

- **The repository is the only memory.** Every session can start cold.
- **Small, self-describing files.** Each file opens with its role and status. Canonical files carry no dated history: decisions and their reasons go in `charter/decisions.md`, and everything else is in Git.
- **Stable IDs, one home per fact.** Cross-reference by ID (`SRC-0001`, `EV-HOU-001`, `HOU-4A`, `HOU-4A.01`, `DEC-2026-10-28-01`, `OUT-01`, `MOD-household`); plan section 4 lists them all. Generated indexes are rebuilt by script, never hand-edited.
- **Checks, not memory.** `bash .github/scripts/run-checks.sh` runs the full rebuild, drift check and tests. It compares against committed files, so commit before you run it.
- **Licensed or paywalled material** is cited and briefly quoted, never committed: the repository is public.
- **Sources and evidence** (`DEC-2026-10-28-07`):
  - Any credible source may be used, government or not; its rights decide how it enters the library (`library/README.md`).
  - Every evidence entry says whether it is data (a measured fact) or analysis (an interpretation: causes, effects, projections, models). Grade by the kind of evidence, not the publisher: an agency's causal account is analysis.
  - For an analysis, record who published it, when and with what stake. Check a report's headline against its own numbers. Rely on an analysis only once an independent publisher supports or qualifies it, and present both views where one contests it.
  - Executive-branch analysis (agencies, the White House Council of Economic Advisers, OMB, executive orders) gets skepticism in proportion to the administration's record of politicized analysis: most for the second Trump administration (2025 on), then the first; Obama- and Biden-era analysis is checked as usual, and more where warranted (`DEC-2026-10-30-01`).
  - The registry checker checks each entry's data-or-analysis label, grade and corroboration links. The rest of the method is in `dossiers/TEMPLATE.md`.
- **Use what exists first.** Search `legacy/` (domains, sources) and `models/tools/` before new research, and restate legacy figures with their IDs.
- **Use all the information at hand, as evidence, not as a default** (`DEC-2026-11-13-15`). The legacy work, the library, other dossiers and model results are sources to weigh with new research; their conclusions carry no presumption. Each research pass and decision memo opens with "Already in the repository": what the repository already holds on the question, by ID, and where new evidence confirms, qualifies or overturns it. Check again before each new research pass, not only at the start of a step.
- **Web search.** When Firecrawl is unavailable or out of credits, switch to Exa or another search and fetch tool and carry on (`DEC-2026-11-12-02`).
- **Sources you can't download directly.**
  - HUD, CBO and GAO block automated downloads. Census, the Federal Reserve, EveryCRSReport and congress.gov's CRS files do not. The GovQuery connector finds CRS and GAO reports by topic; the Congress.gov API names each CRS report's current version.
  - CBO: fetch through a search or fetch tool such as Exa (`DEC-2026-11-08-10`). HUD and GAO: Espen uploads them.
  - API keys come from the environment variables `API_CENSUS_KEY` (Census Data API) and `API_DATA_GOV_KEY` (Congress.gov and GovInfo). Never write a key into the repository; a recorded query address leaves it out.
  - Save a public document as text under its official address with `library/fetch_public.py --file`.
- Espen's Google Drive is not a project source; don't search it for project work.

## Session routine

1. Read this page and `charter/PROGRESS.md`. Check open PRs.
2. Take the one step the lead names in your brief. Open your PR early, as a draft if the step is long, with the step in its title.
3. Read that dossier's files and the evidence it needs.
4. Do the step. One dossier step per session.
5. Run the checks.
6. Write the board update in your PR description under "For the board": done, next, and open questions for Espen. Only the lead edits `charter/PROGRESS.md`; a worker edits it only when no lead is live (`DEC-2026-11-12-03`).
7. Open one coherent PR and mark it ready when done.

## Choosing the model

Use the lightest model that can do the step well, and the strongest where care and judgment matter: errors in large, interconnected datasets propagate, so mistakes there cost more than the tokens saved.

| Tier | Use for | Examples |
| --- | --- | --- |
| **Light** (Haiku-class) | Mechanical work with a clear spec and automatic checks | File moves and link updates; regenerating outputs; running checks; formatting; gathering `library/` catalog facts by script; extracting text from originals |
| **Standard** (Sonnet-class) | Structured work needing some judgment within a settled design | Cataloguing (status, aliases, rights); drafting evidence entries; model code and tests to a written spec; dossier sections from existing evidence; checklist reviews |
| **Most capable** (Opus-class) | Strategy, design, synthesis, and work where an error would spread | Design choices and decision memos; dossier problem, design and specification sections; reconciling conflicting evidence; model design and integrating the household, health and budget models; adversarial milestone reviews; legal and constitutional analysis; public briefs; the progress board |

- Every step on `charter/PROGRESS.md` names its tier.
- A lighter model that meets ambiguity stops, leaves a note in its PR for a stronger session and tells its report-back address. It doesn't guess.
- Strong sessions delegate mechanical subtasks to lighter subagents where the tools allow, and check the results.
- When unsure, go one tier up. The same tiers apply to other vendors' agents, by capability.

## Merge categories

The merge gate (`.github/merge-policy.json`; details in `legacy/governing/project-collaboration.md`) applies them.
- **Routine** (gate tiers 1-2): research, evidence, library, models, dossier drafts, the board, and public pages that change no commitment. These merge once checks pass and another agent has reviewed the current head.
- **Decisions** (tier 3): the charter, the flagship list, adopted model inputs (`models/data/inputs/`), design choices at real forks, new or removed programs, the merge rules and entry files (`.github/`, `AGENTS.md`, `CLAUDE.md`, `GEMINI.md`), and anything labeled `needs-espen`. These merge only after Espen adds `espen-approved` themselves.
- Agents never apply `espen-approved` or `espen-override`, and never enable auto-merge on a tier-3 PR.
- Keep routine and decision changes in separate PRs.
- Ask Espen for `espen-approved` only when the PR's head is final, current with main and approved by the reviewer. A push with new content drops the label; a merge of main does not (`DEC-2026-11-12-04`).
- Every PR description carries `Agent-Author: <claude-code|codex|gemini> <session id>`. A reviewing agent reads the diff at the head and comments `Agent-Review: approve` (or `changes-requested`), `Reviewed-Head: <full SHA>` and `Reviewer: <agent> <session id>`.

## Milestone review

- A second agent reviews each dossier against the checklist at L2 and again at L3, trying to break it: weak evidence, missing populations, optimistic assumptions, cheaper alternatives.
- The L3 re-check is done by a fresh or the standing reviewer on the close-out PR itself.
- Book a dossier in the budget model only after its milestone review's fixes, so it is booked once.
- At each stage boundary Espen holds a short strategic review.

## Design lens: guide, don't police

Prefer designs that are simple for the people served and for the agencies running them (`DEC-2026-11-09-13`).
- Each eligibility test, document, deadline, cap or quota has to earn its place against the burden it adds, because such burdens fall hardest on the people in the worst situations and they raise running costs.
- Prefer one plain test, self-attestation and records the government already holds, local judgment based on need, and published counts with a review trigger, over strict structures enforced up front.
- Accept that not every group will be served in exactly the share the design projects; correct with monitoring, not with more rules.
- Recommendations say what each requirement costs in burden, as well as what it buys.
- Use existing machinery first: deliver through the agencies, programs, records and payment systems that already exist wherever they can do the job, and simplify where an existing system or a proposed design is more complex and costly to administer than its purpose needs (`DEC-2026-11-13-08`).

## Fiscal rule in dossiers: report, don't gate

(`DEC-2026-11-10-05`)
- Each dossier prices everything honestly and reports its fiscal-rule effect: yearly cost, permanent cost from FY2040, and its share of the plan-wide margin.
- It passes that to the financing settlement, the one place where the plan is balanced, plan-wide.
- A dossier's own gap in a test year is not a defect to fix and is not put to Espen by itself.
- A cost goes to Espen when the choice is mainly about money: designs that reach the same people at very different cost, or a cost well above comparable programs.
- The budget model keeps a running plan-wide total so drift stays visible.

## What needs an answer now

Specify what government commits to do; don't try to predict everything that follows from it (`DEC-2026-11-10-07`). Before extending a research or specification task, ask what decision a different answer would change. Treat each question one of four ways:
- **Decide now** when the answer defines the commitment (eligibility, benefit, authority, agency, rights). Real forks stay Espen's.
- **Use a working assumption** when a number is needed for budgeting or comparison, with its basis, range and the cost of being wrong.
- **Leave it open** when several outcomes are reasonable and none changes today's choice. Record the alternatives and what finding would make it matter.
- **Study it in implementation** when pilots or administrative experience will answer it better than desk research, without a new reporting burden.

An uncertainty belongs on the critical path only when a plausible answer would change the choice, undermine the commitment, or expose a legal or delivery obstacle. Reviewers treat these as defects: unsupported claims stated as settled, inconsistent commitments, decision-changing omissions, and missing delivery mechanisms. A clearly bounded uncertainty is not one. A reviewer who asks for more investigation says which decision it would inform and whether it blocks that decision now.

## Decision memos

- At each real fork Espen gets two to four options, a recommendation and the consequences of each, in the dossier's design section. What a good memo set has is in `dossiers/TEMPLATE.md`, "Decision memos in one batch".
- Approval is per decision, never as a package: Espen may answer a whole batch at once, but each memo and point is decided on its own.
- Once decided, it gets a `DEC-` entry in `charter/decisions.md`.

## Sessions and handoffs

- A Claude Code session starts another session only to take a ready board step, to run independent work in parallel, to run a large batch at a better-suited tier, or for an independent review.
- It never starts one for a small subtask, for work a live session already holds, or for a step that waits on Espen.
- At most three Claude sessions work at once.
- Each new session gets a standalone brief and reports back when its PR is ready.
- Messages between sessions only alert another session to work: whatever it must know goes in the PR, on the board or in the dossier.
- Reach Codex with a PR comment, when its access to the repository is on (the board says when it is suspended).
- The mechanics are in `.claude/skills/sessions/SKILL.md`.

## Roles

- Claude leads the dossiers, the federal budget model with its shared fiscal inputs (`DEC-2026-11-08-02`), and fair financing, the financing settlement (`DEC-2026-11-11-07`). Changing adopted inputs in `models/data/inputs/` stays Espen's decision.
- Codex review is not required for the budget model or the financing settlement: they merge on the Claude reviewer's review, like other work (`DEC-2026-11-12-01`).
- At most two dossiers are active at once.
