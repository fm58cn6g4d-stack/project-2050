# Project 2050: progress board

Role: the live status of the plan (`charter/PLAN.md`, section 6). Every session updates it before opening its PR. Status: current. It replaces `legacy/sources/project-work-queue.md` as the place to claim work.

Updated October 28, 2026 by Claude Code (stage A, PR 1).

## Now

| Stage | Step | Status | Owner | Where |
| --- | --- | --- | --- | --- |
| A. Reset | 1. Clean tree, `legacy/`, models and checks migrated, standards, board, decision log, entry files | In review: needs Espen's approval (tier 3) | Claude Code | PR #46 (branch `claude/stage-a-reset`) |
| A. Reset | 2. `agenda/agenda.csv` from the legacy domain files and options register | Next | Claude Code | — |
| A. Reset | 3. `library/catalog.csv` and the generated name index | Waiting on step 1 | Claude Code | — |
| A. Reset | 4. Registry checker, generalized from the story builder's checks | Waiting on step 1 | Claude Code | — |
| A. Reset | 5. `charter/outcomes.md` draft, for Espen's approval | Waiting on step 1 | Claude Code | — |
| B. Post-election update | Rebaseline the political planning scenario | Starts after the November 3 results | — | — |

## Open PRs

| PR | What | State |
| --- | --- | --- |
| #45 (Codex) | Integrate the decided climate Package A, O5 and CLI-7C into the fiscal models | Tier 3, waiting on Espen. Merge it before the reset PR; the reset is rebuilt on top of it so Codex's changes follow the moved files |

## Done (recent)

| Item | Result |
| --- | --- |
| Restructuring plan | Adopted by Espen October 28 (`charter/PLAN.md`, `DEC-2026-10-28-01`) |
| Research intake, October 28 | Filed in `library/intake/2026-10-28/` with checksums |
| PR #39, public story page with seven essays and a claim register | Merged at `eceb44a`. The old queue still called it "ready for approval"; it is done |
| PR #44, climate export reconciliation and JSON drift checks | Merged at `ffe461d` |

## Known gaps

- **Review capacity.** Codex is out of review credits, so routine PRs lack the second-agent review the gate needs. Until that returns: small PRs, and Espen approves directly (Espen may also add `espen-override`).
- **Legacy outputs.** The legacy model suite still regenerates its reports in `legacy/index/` and `legacy/sources/` (`models/README.md`). They move into `models/` as each core model is rebuilt.
- **Front-door edition.** `public/site/index.html` is pinned to an older evidence commit and is rebuilt in stage H.

## Questions for Espen

1. Approve the reset, PR #46 (add `espen-approved`), after PR #45 if you approve that one too.
