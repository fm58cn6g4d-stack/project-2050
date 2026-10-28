# Project 2050: progress board

Role: the live status of the plan (`charter/PLAN.md`, section 6). Every session updates it before opening its PR. Status: current. It replaces `legacy/sources/project-work-queue.md` as the place to claim work.

Updated October 28, 2026 by Claude Code (stage A, step 4).

## Now

| Stage | Step | Tier | Status | Owner | Where |
| --- | --- | --- | --- | --- | --- |
| A. Reset | 1. Clean tree, `legacy/`, models and checks migrated, standards, board, decision log, entry files | Most capable (moves and path rewrites: Light) | Done | Claude Code | PR #46, merged |
| A. Reset | 2. `agenda/agenda.csv` from the legacy domain files and options register | Standard to extract; Most capable for levels and status | In review | Claude Code | PR #47 |
| A. Reset | 3. `library/catalog.csv` and the generated name index | Light for file facts; Standard for status, aliases and rights | In review | Claude Code | PR #48 |
| A. Reset | 4. Registry checker, generalized from the story builder's checks | Most capable | In review | Claude Code | Branch `claude/stage-a-registry` (after #47 and #48) |
| A. Reset | 5. `charter/outcomes.md` draft, for Espen's approval | Most capable | Next | Claude Code | — |
| B. Post-election update | Rebaseline the political planning scenario | Most capable | Starts after the November 3 results | — | — |

## Open PRs

PR #47 (agenda), PR #48 (catalog) and the registry checker (step 4). Routine PRs merge on review by the scheduled Claude reviewer session; tier-3 PRs wait for Espen.

## Done (recent)

| Item | Result |
| --- | --- |
| Stage A step 1, the reset (PR #46) | Merged: clean tree, `legacy/`, migrated models and checks, standards, board |
| Stage A step 4, the registry checker (in review) | `models/registry/check.py` checks the agenda, the library catalog, charter IDs, evidence registers and provisions, and every SRC-, EV-, OUT- and DEC- reference; it runs in every PR as `run-all.sh` step 8e. The story builder now uses the same claim rules (`models/registry/claims.py`) |
| Stage A step 3, the library catalog (in review) | 286 documents in `library/catalog.csv` with `SRC-` IDs; generated file facts; `library/name-index.md` resolves 856 names, including Bill Book, the map, the go-big and revenue tabs, staging rows and the durability session. One intake PDF needs a rights check |
| Stage A step 2, the agenda (in review) | 499 items in `agenda/agenda.csv`: 32 decided, 267 chosen, 54 options, 128 alternatives, 18 held, declined, pointer or retired. None is L3 yet |
| Restructuring plan | Adopted by Espen October 28 (`charter/PLAN.md`, `DEC-2026-10-28-01`) |
| Research intake, October 28 | Filed in `library/intake/2026-10-28/` with checksums |
| PR #39, public story page with seven essays and a claim register | Merged at `eceb44a`. The old queue still called it "ready for approval"; it is done |
| PR #45 (Codex), decided climate Package A, O5 and CLI-7C integrated into the fiscal models | Merged at `3a0a4b0` after Claude Code review and Espen's approval. DEC 2056 debt 155.7% to 156.4% of GDP; mixed Q4 FY2039 −$2,906 to −$3,054; D3 still unresolved |
| PR #44, climate export reconciliation and JSON drift checks | Merged at `ffe461d` |

## Known gaps

- **Review capacity.** Codex is out of review credits. The scheduled Claude reviewer session (a separate Claude Code session, which counts as another agent) reviews routine PRs on request. Espen's `espen-approved` stands in for an agent review only on tier 3, so a routine PR Espen wants to approve directly also needs `needs-espen`.
- **Legacy outputs.** The legacy model suite still regenerates its reports in `legacy/index/` and `legacy/sources/` (`models/README.md`). They move into `models/` as each core model is rebuilt.
- **Story claims after PR #45.** Two essay claims (`q4`, `downside`) cite figures that PR #45 changed (fourth-quintile −$2,906 is now −$3,054). The page stays pinned to its evidence commit; an editor should reread and advance the pin. `run-all.sh` reports it on every run.
- **Front-door edition.** `public/site/index.html` is pinned to an older evidence commit and is rebuilt in stage H.

## Questions for Espen

1. `library/intake/2026-10-28/old-sessions/Claude climate carbon permitting/permitting-reform-summary-1.pdf`: who published it? If it is licensed, it should come out of the public repository.
