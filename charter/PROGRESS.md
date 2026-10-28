# Project 2050: progress board

Role: the live status of the plan (`charter/PLAN.md`, section 6). Every session updates it before opening its PR. Status: current. It replaces `legacy/sources/project-work-queue.md` as the place to claim work.

Updated October 28, 2026 by Claude Code (stage C: sources and evidence method).

## Now

| Stage | Step | Tier | Status | Owner | Where |
| --- | --- | --- | --- | --- | --- |
| A. Reset | 1. Clean tree, `legacy/`, models and checks migrated, standards, board, decision log, entry files | Most capable (moves and path rewrites: Light) | Done | Claude Code | PR #46, merged |
| A. Reset | 2. `agenda/agenda.csv` from the legacy domain files and options register | Standard to extract; Most capable for levels and status | Done | Claude Code | PR #47, merged |
| A. Reset | 3. `library/catalog.csv` and the generated name index | Light for file facts; Standard for status, aliases and rights | Done | Claude Code | PR #48, merged |
| A. Reset | 4. Registry checker, generalized from the story builder's checks | Most capable | Done | Claude Code | PR #49, merged |
| A. Reset | 5. `charter/outcomes.md` draft, for Espen's approval | Most capable | Done: approved by Espen | Claude Code | PR #50, merged |
| B. Post-election update | Rebaseline the political planning scenario | Most capable | Starts after the November 3 results | — | — |
| C. First dossiers | 1. Dossier template; housing section 1, the problem, with its evidence register | Most capable (text extraction: Light) | Done | Claude Code | PR #53, merged |
| C. First dossiers | 1b. Sources and evidence method: non-government sources (open-licensed texts, citation rows for licensed works); data versus analysis; analysis corroborated by independent publishers | Most capable | In review | Claude Code | Branch `claude/library-citations` |
| C. First dossiers | 2. Housing: refresh rent burden with the 2025 ACS (released Oct 29); subgroup breakdowns from the HUD report | Standard | In progress: HUD subgroup breakdowns (EV-HOU-030 to 034) drafted; ACS refresh after the October 29 release | Claude Code | Branch `claude/stage-c-housing-2` (after PR #54) |
| C. First dossiers | 3. Housing section 2, what works | Most capable | Waiting on step 2 | Claude Code | — |
| C. First dossiers | 4. Housing section 3, design choices, with decision memos for Espen | Most capable | Waiting on step 3 | Claude Code | — |
| C. First dossiers | 5. Housing sections 4-6: specification, delivery, cost (with Codex on the budget model) | Most capable | Later | Claude Code, Codex | — |
| C. First dossiers | 6. Housing sections 7-9; L2/L3 milestone review | Most capable | Later | Claude Code; reviewer | — |
| C. First dossiers | 7. Transportation converted as the reference dossier; template fixes | Standard to convert; Most capable for gaps | Later | Claude Code | — |

## Open PRs

The stage C sources and evidence method PR (`claude/library-citations`).

## Done (recent)

| Item | Result |
| --- | --- |
| Stage C step 1, the housing problem section (PR #53, merged) | Dossier template; `dossiers/home/1-problem.md` with EV-HOU-001 to 028 (Census, Federal Reserve and HUD at grade A; CRS summaries and agency cause narratives at C). Espen uploaded HUD's *Worst Case Housing Needs 2025* and *2024 AHAR*. Approved by the Claude reviewer and Codex |
| Stage A, complete | Espen reviewed stage A and the outcomes record (PR #50) on October 28 and started stage C |
| Stage A step 1, the reset (PR #46) | Merged: clean tree, `legacy/`, migrated models and checks, standards, board |
| Catalog follow-up: one home per name (PR #51, merged; staging rows fixed after) | 16 original uploads marked `copy_of` their working copies in `legacy/`; two generic titles renamed; the catalog check now fails if any title or alias leads to two homes |
| Stage A step 4, the registry checker (PR #49, merged) | `models/registry/check.py` checks the agenda, the library catalog, charter IDs, evidence registers and provisions, and every SRC-, EV-, OUT- and DEC- reference; it runs in every PR as `run-all.sh` step 8e. The story builder now uses the same claim rules (`models/registry/claims.py`) |
| Stage A step 3, the library catalog (PR #48, merged) | 286 documents in `library/catalog.csv` with `SRC-` IDs; generated file facts; `library/name-index.md` resolves 856 names, including Bill Book, the map, the go-big and revenue tabs, staging rows and the durability session. The one PDF flagged for rights is the Senate Energy and Natural Resources Committee's public one-pager (reviewer, PR #48) |
| Stage A step 2, the agenda (PR #47, merged) | 499 items in `agenda/agenda.csv`: 38 decided, 266 chosen, 58 options, 118 alternatives, 19 held, declined, pointer or retired. None is L3 yet |
| Restructuring plan | Adopted by Espen October 28 (`charter/PLAN.md`, `DEC-2026-10-28-01`) |
| Research intake, October 28 | Filed in `library/intake/2026-10-28/` with checksums |
| PR #39, public story page with seven essays and a claim register | Merged at `eceb44a`. The old queue still called it "ready for approval"; it is done |
| PR #45 (Codex), decided climate Package A, O5 and CLI-7C integrated into the fiscal models | Merged at `3a0a4b0` after Claude Code review and Espen's approval. DEC 2056 debt 155.7% to 156.4% of GDP; mixed Q4 FY2039 −$2,906 to −$3,054; D3 still unresolved |
| PR #44, climate export reconciliation and JSON drift checks | Merged at `ffe461d` |

## Known gaps

- **Review capacity.** Codex reviews again (PR #50). The scheduled Claude reviewer session also reviews routine PRs on request. Espen's `espen-approved` stands in for an agent review only on tier 3.
- **Blocked sources.** HUD, CBO and GAO block automated downloads from agent sessions; Census, the Federal Reserve, EveryCRSReport and congress.gov's CRS files do not; the GovQuery connector finds CRS and GAO reports by topic. The Congress.gov API names each CRS report's current version (EveryCRSReport can lag), and congress.gov's CRS PDFs download. The API needs an api.data.gov key, which Espen gives a session directly; it is never committed or written into the repository. Blocked documents come in through Espen's uploads; `library/fetch_public.py --file` saves an uploaded public document as text under its official address. Espen's Google Drive is not a project source: do not search it.
- **Legacy outputs.** The legacy model suite still regenerates its reports in `legacy/index/` and `legacy/sources/` (`models/README.md`). They move into `models/` as each core model is rebuilt.
- **Story claims after PR #45.** Two essay claims (`q4`, `downside`) cite figures that PR #45 changed (fourth-quintile −$2,906 is now −$3,054). The page stays pinned to its evidence commit; an editor should reread and advance the pin. `run-all.sh` reports it on every run.
- **Catalog facts.** `catalog-facts.csv` dates depend on the clone's history depth, so the file is refreshed, never checked.
- **Front-door edition.** `public/site/index.html` is pinned to an older evidence commit and is rebuilt in stage H.

- **Standards wording.** The data-versus-analysis and corroboration rule Espen asked for on October 28 is in `dossiers/TEMPLATE.md` and the checker. It also belongs in `charter/STANDARDS.md`, which is tier 3: proposed for the next charter PR, with Espen's stage A sign-off for `charter/decisions.md`.

## Questions for Espen

1. Optional: upload HUD's *2025 Annual Homelessness Assessment Report*, Part 1 (May 2026), to raise the 2025 homelessness figures from grade C to A. *Worst Case Housing Needs 2025* and the 2024 homelessness report arrived October 28 and are in the library.
