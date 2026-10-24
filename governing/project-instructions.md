# Project 2050: shared project instructions

Read the governing decisions first, then this file, at the start of every session. These working instructions apply to Claude, ChatGPT/Codex, Gemini and other assistants; they do not override policy decisions. Updated Oct 23, 2026 (post-pilot integration draft).

## What this is
Project 2050 designs a coherent, internally consistent set of policy options for a 2029-30 Democratic trifecta and the decades after. The owner is Espen Swanson. Espen is not a programmer: write in plain language, run commands yourself rather than asking Espen to, and report briefly (what you did, what you found, what needs Espen's decision).

## Where things live
- **This repo is the working home of the files.** Folder = role (authority descending; a higher role overrides a lower one):
  1. `governing/` — `project-2050-governing-decisions.md` (the decisions and design rules) and the decision briefs. The approved governing document in GitHub is authoritative. Claude artifacts, Google Docs and exports are working copies. Proposed changes become governing decisions only after Espen approves them and they are incorporated into GitHub; an unmerged proposal does not itself change policy. Flag conflicting copies rather than silently reconciling them.
  2. `domains/` — one canonical file per domain, each with stable IDs: domain-revenue (REV-), -health (HLT-), -family (FAM-), -social-security (SS-), -democracy (DEM-), -courts (CRT-), -executive-power (EXE-), -integrity (INT-), -capacity (CAP-), -climate (CLI-), -housing (HOU-), -labor (LAB-), -competition (COM-), -immigration (IMM-), -rights (RTS-), -public-safety (SAF-), -ai (AI-), -national-security (NSC-), -amendments (AMD-), -education (EDU-). Canonical until converted: `transportation-moving-america-act-2031-draft-2.md` (MOV-); its model scripts are in `index/tools/transportation/` and its source docs (ARCA, ATRA, the section-by-section, the calendar decision, session status) are `sources/transportation-*`. `public-safety-safe-everywhere.md` is the evidence base behind domain-public-safety, not canonical. Where a file predates a decision, the decision wins.
  3. `index/` — generated files (the master ledger, the household incidence model, the long-term fiscal model, `index/data/`). **Never hand-edit them; regenerate** with `bash index/tools/run-all.sh` (dry run with a diff) and `--write` to update. Hand-written exceptions: `index/options-register.md` (every option once, with exclusive groups and overlaps — check it before proposing or summing options) and `index/revenue-assignment-audit.md`.
  4. `frameworks/` — reasoning only, not current policy (radical-means-moderate-ends, instruments-and-consequences, the Talarico stress test).
  5. `staging/` — the old reform inventory; rows are pointers to domain files now.
  6. `archive/` — ideas only, never current sources. Four large archive files (the superseded Beyond Health Care agenda and three war-game HTML pages) were not copied from the claude.ai Project; they are ideas only.
  7. `sources/` — outside inputs and source tables behind the domain files.
- **Live pages on claude.ai** (edit through Claude on claude.ai, not from here): the governing doc above; Decision Brief 1 (https://claude.ai/artifact/STTq2kjhUfzJUYJUy8VafV); "Senate Rules Reform: Options" (https://claude.ai/code/artifact/0f226c46-5ce8-4bec-9a54-c5fd7e7a5629); the ledger dashboard (https://claude.ai/artifact/RDuHM7DqCwvLUtVaB4ANMs).
- **External workspaces and copies:** the claude.ai Project "Project 2050", Google Docs and uploads can support discussion and drafting. Record the GitHub branch and commit used. When GitHub changes, refresh relevant copies or clearly label them as behind; do not assume a connector or upload synchronizes automatically.

## Decisions and design rules
Read `governing/project-2050-governing-decisions.md` in full, including its design rules and project instructions. Use its current decisions, state and open calls instead of maintaining a separate policy summary here. Check `index/check-report.md` and the relevant canonical domain files for the task. The governing document wins if another file disagrees.

## Working rules
- Propose changes as options with their effects; don't silently rewrite a canonical file. Decisions are Espen's.
- A second version of a policy gets flagged and folded into its domain file as an option.
- Tag every number as sourced, scaled, estimated or proposal, with its window (default ten years, 2030-39, in trillions).
- Look up anything that describes the world now before stating it.
- Name policies by their domain-file IDs.
- After a domain file changes a number, update the input tables in `index/data/inputs/` (ledger-*.csv, incidence-*.csv, fiscal-*.csv as relevant) and regenerate; never edit generated files by hand.
- Filing: new docs go straight into their role folder, lowercase kebab-case, domain first.

## Tools
`index/tools/readme.md` explains each script. Quick version:
- `bash index/tools/run-all.sh` — rebuild everything in `build/` and diff against `index/`; `--write` to update; `--fetch` to re-download CBO's data (github.com/US-CBO/cbo-data).
- `index/vote-simulation.md` (run-all) gives the odds the packages and bills pass under each D2 path; its roster (`index/data/inputs/votes-senate.csv`) is the war game's mid-2026 map until the Nov 3 re-baseline.
- `index/dedicated-funds.md` (run-all, `funds-model.py`) tracks the funds outside the general fund year by year: Social Security and HI over 75 years, paid leave, the Highway Trust Fund's accounts, the carbon dividend, EDU-9B. Trustees inputs are `index/data/inputs/funds-*.csv`; refresh them when the 2027 reports come out.
- `index/climate-carbon-model.md` (run-all, `carbon-model.py`) runs Espen's structural carbon model (`index/tools/carbon/`) on D7: emissions to 2050, REV-C1 by year, REV-C2 and a methane fee sized, the road-fuel exemption's cost. The model's own notes are `sources/climate-carbon-dividend-model-notes.md`.
- `index/tools/roadmap.md` lists what the tools answer and what comes next. run-all also writes `index/data/dashboard/`, the ledger dashboard's data; after a run that changes it, upload those files to the dashboard (its datasets point at them).
- `index/check-report.md` (written by run-all) lists documents quoting stale headline figures, unknown IDs, stale phrases, ledger rows that differ from their domain file, and scaled figures re-run. Read it at the start of a session; `index/tools/window.py` restates a figure from another budget window in 2030-39 terms.
- Input tables live in `index/data/inputs/` (CSV; its readme explains each): ledger bills, revenue, options, conflicts and dynamic sensitivity; incidence keys, rows (amounts are formulas over ledger IDs, so they follow the ledger) and phase-ins; long-term year profiles. Scenario lists stay in `incidence-model.py` and `fiscal-model.py`.
- Transportation model: `index/tools/transportation/moving_america.py` (print with `report.py`, check with `test_moving_america.py`; see its readme). run-all.sh runs it first, and the MOV-29/30/31 and MR1-MR6 rows in ledger-build.py come from it. A moved figure is a proposal for Espen.
- Sprint revenue rows use the prefix TS (TS1-TS12, TSX) so the old tariff row T1 keeps its ID; high-pay options are HP1-HP3.

## Git
Commit with a short plain message describing what changed and why. Don't rewrite history. Work on a branch for anything large and say so.

## Working across tools
- Start each task by stating its scope, source branch and commit, expected output, and files it may change. Read relevant files before proposing changes; say when a source is unavailable.
- Give concurrent writing tasks separate branches and, for local agents, separate worktrees or checkouts. Avoid simultaneous edits to the same files. GitHub stores and reviews work; it does not synchronize chat memory.
- Keep research and alternative designs labeled as proposals. Include sources, assumptions, effects on D1-D9, overlaps and decisions needed.
- Finish with a short handoff: what changed or was learned, files and commit/PR, validation, unresolved questions and the next action. State whether work is proposed, approved or merged.
- Open a focused pull request for review when asked to prepare changes. Do not merge merely because a proposal was requested; Espen chooses the decisions and integration step.
- In chat-only tools that do not read repository instruction files automatically, supply this file, the governing document and task-relevant files explicitly. The root entry points are pointers, not a guarantee that every product loads them.

## Model and tool guidance
- Proactively recommend a different model, thinking level or execution tool when the task's complexity, uncertainty, need for independent review, or repository work makes a switch worthwhile. Explain the expected benefit briefly and account for time, cost and usage limits; avoid unnecessary switching. Do not claim a switch happened unless it actually did.
- Keep Claude Chat/Cowork, Claude Code, ChatGPT/Codex and Gemini in view as possible collaborators. Preserve continuity through shared sources and task handoffs rather than assigning permanent roles by brand. Verify current capabilities and access before making specific product recommendations.
- Availability note, recorded Oct 21, 2026: Espen has no Claude compute until Monday, Oct 26 unless they choose to buy credits. Plan work without requiring Claude before then. Espen expects to move some work back to Claude after that date; confirm actual availability when relevant rather than assuming a reset occurred.

## Open queue
The governing document's Next steps and Open calls for Espen, the relevant domain's open items, and `index/tools/roadmap.md` hold the working queue. Prioritize a bounded task with Espen; do not treat a recommendation as an adopted decision.

## Post-pilot source and synchronization note

Read sources/project-2050-research-register.md and sources/post-pilot-integration-handoff.md when a task depends on the October 23 pilots or approved directions. The approved charter governs project purpose, outcomes and workflow; the approved governing decisions govern selected instruments and policy. Research reports, alternatives and family illustrations do not become adopted policy through filing or favorable findings. Retrieve a referenced source when needed; explicitly report missing access.

The October 23 integration updates legislative target windows, protects DEM/SS capacity and regenerates outputs. DEM-1 starts floor consideration by March 2029 latest; R1 delay is not an automatic gate on DEM or other priorities. Seasonal targets are not guessed passage months. Capacity allocations do not demonstrate dated feasibility. Revised legislative timing is not a household-receipt estimate: relevant felt-by-midterm fields remain Unverified. Unknown merger savings, reserve, MOV floor time and FY2029 cash remain explicit. Never hand-edit generated outputs.

Communications restriction: Espen has expressly withheld authorization for CMS records-request emails or any other email. Preparing a packet does not authorize submission. Child-poverty research completion authorizes reading and synthesis, not adopting new eligibility or benefit rules. Keep the new working commit in each handoff; refresh external copies after integration rather than assume automatic synchronization.

## Calendar method update approved October 23

Espen authorized review and project-wide integration of the scenario calendar. Use `index/calendar-scenarios.md`, its generated explorer and `index/calendar-delivery-opportunities.md` for the current analytical presentation. Compare ranges of active floor hours, procedural sitting spans, preparation and bicameral delays, capacity and shared disruptions. The old 172-versus-163 calculation and 15-plus-2 reconciliation allowances remain labeled legacy assumptions, not validated durations, physical limits or an instruction to trim nine days.

D1 scope, D2-F and minority guarantees, D5 vehicles, early R1, DEM's March floor-start and enactment limits, spring SS, health launch dates and second-Congress MOV remain in force. Scenario inputs are illustrative and uncalibrated; integration adopts the method, not numerical forecasts, a merger, a recovery sequence or a new launch date. Report votes, scheduling, legal durability and delivery separately. No legacy capacity filter may silently assign a zero passage probability to a bill. Earlier enactment may create additional pre-midterm delivery opportunities, requiring explicit effective dates, agency resources, reach and remedies before a felt-impact claim. No fiscal, benefit or vote parameter is changed by this method update.
