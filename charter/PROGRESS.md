# Project 2050: progress board

Role: the live status of the plan (`charter/PLAN.md`, section 6). Every session updates it before opening its PR. Status: current. It replaces `legacy/sources/project-work-queue.md` as the place to claim work.

Updated October 28, 2026 by Claude Code (stage A, PR 1).

## Now

| Stage | Step | Tier | Status | Owner | Where |
| --- | --- | --- | --- | --- | --- |
| A. Reset | 1. Clean tree, `legacy/`, models and checks migrated, standards, board, decision log, entry files | Most capable (moves and path rewrites: Light) | In review: needs Espen's approval (tier 3) | Claude Code | PR #46 (branch `claude/stage-a-reset`) |
| A. Reset | 2. `agenda/agenda.csv` from the legacy domain files and options register | Standard to extract; Most capable for levels and status | Next | Claude Code | — |
| A. Reset | 3. `library/catalog.csv` and the generated name index | Light for file facts; Standard for status, aliases and rights | Waiting on step 1 | Claude Code | — |
| A. Reset | 4. Registry checker, generalized from the story builder's checks | Most capable | Waiting on step 1 | Claude Code | — |
| A. Reset | 5. `charter/outcomes.md` draft, for Espen's approval | Most capable | Waiting for Espen (tier 3) | Claude Code | Branch `claude/stage-a-outcomes` |
| B. Post-election update | Rebaseline the political planning scenario | Most capable | Starts after the November 3 results | — | — |

## Open PRs

None besides the reset (PR #46).

## Done (recent)

| Item | Result |
| --- | --- |
| Restructuring plan | Adopted by Espen October 28 (`charter/PLAN.md`, `DEC-2026-10-28-01`) |
| Research intake, October 28 | Filed in `library/intake/2026-10-28/` with checksums |
| PR #39, public story page with seven essays and a claim register | Merged at `eceb44a`. The old queue still called it "ready for approval"; it is done |
| PR #45 (Codex), decided climate Package A, O5 and CLI-7C integrated into the fiscal models | Merged at `3a0a4b0` after Claude Code review and Espen's approval. DEC 2056 debt 155.7% to 156.4% of GDP; mixed Q4 FY2039 −$2,906 to −$3,054; D3 still unresolved |
| PR #44, climate export reconciliation and JSON drift checks | Merged at `ffe461d` |

## Known gaps

- **Review capacity.** Codex is out of review credits, so routine PRs lack the second-agent review the gate needs. Until that returns: small PRs, and Espen approves directly (Espen may also add `espen-override`).
- **Legacy outputs.** The legacy model suite still regenerates its reports in `legacy/index/` and `legacy/sources/` (`models/README.md`). They move into `models/` as each core model is rebuilt.
- **Front-door edition.** `public/site/index.html` is pinned to an older evidence commit and is rebuilt in stage H.

## Questions for Espen

1. Approve the reset, PR #46 (add `espen-approved`).
