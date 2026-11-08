# Project 2050: progress board

Role: the live status of the plan (`charter/PLAN.md`, section 6). Every session updates it before opening its PR. Status: current. It replaces `legacy/sources/project-work-queue.md` as the place to claim work.

Updated November 8, 2026 by Claude Code (stage B, step 1).

## Standing sessions

Who holds each long-running role (`.claude/skills/sessions/SKILL.md`, "Roles" and "Handing over a standing role"). Espen talks to the lead for day-to-day work.

| Role | Session | Title | Since |
| --- | --- | --- | --- |
| Lead | `session_01UQzgBx6gAsCr9hXdHVxrQy` | Project 2050: lead | October 28 (began as the stage A reset session) |
| Reviewer | `session_01UQzgBx8fyTLVyi9sHKfawa` | Project 2050: reviewer | October 29; woken by the reviewer scheduled task. The former reviewer was `session_01QHgvhVvafmiGMqU7Vewnst` (October 26 to 29) |
| Strategy | `session_01UQzgBuA3EdnR7Dx4kUq1un` | Project 2050: strategy and systems | October 27 |

## Now

| Stage | Step | Tier | Status | Owner | Where |
| --- | --- | --- | --- | --- | --- |
| A. Reset | 1. Clean tree, `legacy/`, models and checks migrated, standards, board, decision log, entry files | Most capable (moves and path rewrites: Light) | Done | Claude Code | PR #46, merged |
| A. Reset | 2. `agenda/agenda.csv` from the legacy domain files and options register | Standard to extract; Most capable for levels and status | Done | Claude Code | PR #47, merged |
| A. Reset | 3. `library/catalog.csv` and the generated name index | Light for file facts; Standard for status, aliases and rights | Done | Claude Code | PR #48, merged |
| A. Reset | 4. Registry checker, generalized from the story builder's checks | Most capable | Done | Claude Code | PR #49, merged |
| A. Reset | 5. `charter/outcomes.md` draft, for Espen's approval | Most capable | Done: approved by Espen | Claude Code | PR #50, merged |
| B. Post-election update | 1. Rebaseline the political planning scenario: results record by certainty, analysis review, 2027-28 framework with open questions, what it means for the 2029 plan | Most capable | Done: `dossiers/scenario/` (results record, analysis review, 2027-28 framework with 12 questions, flags for D1-D9 and the stage order); SRC-0440 to 0554 | Claude Code (session_01UQzgBuqtNbQNRi98DUinu5) | PR #78, merged
| B. Post-election update | 2. Follow-up for Espen: Alaska Senate rechecked; governor count; the 2028 Senate map and a scenario estimate of the 2029 Senate (`5-senate-2028.md`); a proposed D1 update in a separate tier-3 PR | Most capable | In review | Claude Code (session_01UQzgBuqtNbQNRi98DUinu5) | Branch `claude/stage-b-followup`; D1 on `claude/d1-rebaseline` |
| B. Post-election update | 3. 2027-28 and 2028: the 2027 off-cycle races; the governing playbook as options (federal levers, governors, courts and defiance risks); 2028 scenarios with drivers; how the 2026 result compounds for the 2029 plan and to 2050; two rounds of stress tests | Most capable | Done: `dossiers/scenario/2027-races.md`, `2027-28-playbook.md`, `2028-outlook.md`, `compounding-2029-2050.md`, `2027-28-stress-tests.md`; SRC-0800 to 0989 (citation rows). The 2028 Senate stays in `5-senate-2028.md` | Claude Code (session_01UQzgBxGYju6momc4d3CoJd) | PRs #81 and #83, merged |
| B. Post-election update | 3b. Round 2 for the lead: a Republican-presidency branch; the pre-build pipeline by flagship; redistricting through 2032 (2028 redraws, DEM-2's worth, the 2031 pens ranked); the defense lock-in arithmetic; a third round of stress tests | Most capable | In review: `dossiers/scenario/2028-republican-branch.md`, `compounding-prebuild.md`, `compounding-redistricting.md`, `compounding-defense.md` (script `tools/compounding-defense.py`); SRC-1001 to 1050 | Claude Code (session_01UQzgBxGYju6momc4d3CoJd) | Branch `claude/scenario-2027-28-r2` |
| B. Post-election update | 3c. Round 3 for the lead: decision memo on the defense baseline and DEM-2's severability; a state-by-state 2028 presidential model sharing the Senate model's swing | Most capable | In review: `dossiers/scenario/memo-defense-baseline-and-dem2.md` (PR #89 merged into its stacked base, carried to main on `claude/dem2-value-order` with the 2031-pens update); `presidential-model-2028.md` on `claude/presidential-2028` (PR #87, stacked on #84) | Claude Code (session_01UQzgBxGYju6momc4d3CoJd) | Branch `claude/scenario-memo` |
| C. First dossiers | 1. Dossier template; housing section 1, the problem, with its evidence register | Most capable (text extraction: Light) | Done | Claude Code | PR #53, merged |
| C. First dossiers | 1b. Sources and evidence method: non-government sources (open-licensed texts, citation rows for licensed works); data versus analysis; analysis corroborated by independent publishers | Most capable | Done | Claude Code | PR #54, merged |
| C. First dossiers | 2. Housing: refresh rent burden with the 2025 ACS (released Oct 29); subgroup breakdowns from the HUD report | Standard | In review: HUD subgroup breakdowns (EV-HOU-030 to 034) drafted; 2025 ACS refresh: EV-HOU-038 to 044, section 1 updated, shared-rules fixes (PR #62 notes) | Claude Code (session_01UQzgBvYjGdPE5ZxakSiAHf) | Branch `claude/acs-2025-refresh` |
| C. First dossiers | 3. Housing section 2, what works | Most capable | Done: `dossiers/home/2-what-works.md`, EV-HOU-050 to 184, and EV-HOU-190 and 191 from HUD's *Picture of Subsidized Households* 2023 (Espen's upload); causes, programs and experience abroad | Claude Code (session_01UQzgBwQoJg2sZm4YbUgNaQ) | PR #58, merged; follow-up PR open |
| C. First dossiers | 4. Housing section 3, design choices, with decision memos for Espen | Most capable | In review: `dossiers/home/3-design.md` with seven memos in `dossiers/home/memos/`, EV-HOU-185 to 189. Waits on Espen's decisions before section 4 | Claude Code (session_01UQzgBuhoTGv4SfXLxQf4ZT) | Branch `claude/stage-c-housing-4` |
| C. First dossiers | 4r. Housing: rebaseline section 3 and the memos on the ROAD to Housing Act (Public Law 119-101): provision map, evidence, fork-by-fork changes | Most capable | Done: `dossiers/home/road-act.md`; EV-HOU-200 to 251 from the enacted text and a HUD Inspector General audit (grade A) and CRS R49354, R48732, R48849 (grade C); smaller choice 2 now answers whether voucher refusal is already illegal; fork 4 options and recommendation revised (memo 4); HOU-7 becomes a yes-or-no (point 8, HOU-7B recommended); other forks wording only; shared-rules notes on 1437a | Claude Code (session_01UQzgBtDfz7sX8TE79NK7t2) | PR #68, merged |
| C. First dossiers | 4b. Housing: refresh section 3 and the memos under `DEC-2026-10-30-02` (HOU-4A, HOU-4D, HOU-3C as working choices, weighed as options); 2029 baseline; administration named on executive-branch evidence | Most capable | In review: forks 1, 2, 3 (new part 3, HOU-3C) and 8 re-run with "keep the legacy design" as an explicit option; memos 1, 2, 3, 8 rewritten; context notes in `evidence.json` | Claude Code (session_01UQzgBu67MWo6dPaJU4jBTk) | Branch `claude/housing-design-refresh` |
| C. First dossiers | 4c. Housing: point 5 of "Recommended without a memo" worked out rule by rule (emergency-aid rules: eligibility, risk screen, caps, self-attestation and checks, landlord applications, error measurement, grantee network, data standard), within memo 6's options | Most capable | In review: `dossiers/home/point-5-emergency-aid-rules.md`; text versions SRC-0990 to 0995, citation rows SRC-1060 to 1069 | Claude Code (session_01UQzgBxGYju6momc4d3CoJd) | Branch `claude/emergency-aid-rules` |
| C. First dossiers | 5. Housing sections 4-6: specification, delivery, cost (with Codex on the budget model) | Most capable | Later: starts once Espen decides the section 3 memos | Claude Code, Codex | — |
| C. First dossiers | 6. Housing sections 7-9; L2/L3 milestone review | Most capable | Later | Claude Code; reviewer | — |
| C. First dossiers | 7. Transportation converted as the reference dossier; template fixes | Standard to convert; Most capable for gaps | Later | Claude Code | — |

## Open PRs

- Stage B step 2: Alaska and governor rechecks and the 2028 Senate map (`claude/stage-b-followup`).
- Stage B: proposed D1 update, tier 3, waits for Espen (`claude/d1-rebaseline`).
- Stage B step 3b: round 2 scenario files (`claude/scenario-2027-28-r2`).

- Stage C step 4b: housing section 3 refresh under `DEC-2026-10-30-02` (`claude/housing-design-refresh`).

- Stage C step 4: housing section 3, design choices (`claude/stage-c-housing-4`).
- Stage C step 2: 2025 ACS refresh and shared-rules fixes (`claude/acs-2025-refresh`).

## Done (recent)

| Item | Result |
| --- | --- |
| Stage C step 3, housing section 2, what works (PR #58, merged) | `dossiers/home/2-what-works.md`: causes weighed from independent research, programs at home and abroad, EV-HOU-050 to 184; eight forks left for section 3 |
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
- **Blocked sources.** HUD, CBO and GAO block automated downloads from agent sessions; Census, the Federal Reserve, EveryCRSReport and congress.gov's CRS files do not; the GovQuery connector finds CRS and GAO reports by topic. The Congress.gov API names each CRS report's current version (EveryCRSReport can lag), and congress.gov's CRS PDFs download. Sessions read API keys from the environment variables `API_CENSUS_KEY` (Census Data API) and `API_DATA_GOV_KEY` (the Congress.gov and GovInfo APIs). Both are set in the cloud environment settings and never written into the repository; a recorded query address leaves the key out. Blocked documents come in through Espen's uploads; `library/fetch_public.py --file` saves an uploaded public document as text under its official address.
- **Legacy outputs.** The legacy model suite still regenerates its reports in `legacy/index/` and `legacy/sources/` (`models/README.md`). They move into `models/` as each core model is rebuilt.
- **Story claims after PR #45.** Two essay claims (`q4`, `downside`) cite figures that PR #45 changed (fourth-quintile −$2,906 is now −$3,054). The page stays pinned to its evidence commit; an editor should reread and advance the pin. `run-all.sh` reports it on every run.
- **Catalog facts.** `catalog-facts.csv` dates depend on the clone's history depth, so the file is refreshed, never checked.
- **Front-door edition.** `public/site/index.html` is pinned to an older evidence commit and is rebuilt in stage H.

- **Standards wording.** The data-versus-analysis and corroboration rule Espen asked for on October 28 is in `dossiers/TEMPLATE.md` and the checker. It also belongs in `charter/STANDARDS.md`, which is tier 3: proposed for the next charter PR, with Espen's stage A sign-off for `charter/decisions.md`.

## Questions for Espen

0b. **Two choices in `dossiers/scenario/memo-defense-baseline-and-dem2.md`**, one at a time: (a) count defense against CBO's baseline (A), a fixed flat-real reference (B), or CBO's baseline with a disclosed line (C, recommended; work by Codex after Espen decides); (b) DEM-2 as one provision (A), one severable bill in order ban, criteria, commissions (B), two bills (C), or legacy DEM-2E, criteria with a court backstop and commissions as a voluntary safe harbor (D, recommended, with Title II, the criteria, written to survive on its own, since it carries nearly all of the 2032 House value).

0a. **Stage B step 3, 2027-28 and 2028** (`dossiers/scenario/2027-28-stress-tests.md`, "Next questions"; options, none urgent before the lame duck ends):
   - protect the FY2029 reconciliation slot by using only FY2027 and FY2028 resolutions in 2027-28;
   - which 2027-28 deals are worth their lock-in (a time-limited ACA extension, drug pricing on Trump's design, a $15 minimum wage, a Social Security donut, defense parity);
   - decide the FY2028 defense path before summer 2027, since it sets NSC-1A's base (about $0.1-0.4 trillion over 2030-39);
   - a position on 2027 mid-decade redraws, given DEM-2's planned ban;
   - whether to write a branch for a Republican presidency in 2029.

0. **Stage B, the post-election update** (`dossiers/scenario/3-framework-2027-28.md`, section 7; none urgent before the lame duck ends). The five that matter most:
   - what 2027-28 is for: laws now, a clear record, a plan ready for 2029, a protected 2028 election, or a mix;
   - when an early deal is worth locking in a design before its dossier decides it;
   - whether to rebaseline D1 (52-54 seats) now that 2026 produced 55-56, or after a 2028 map analysis;
   - whether any Senate rules change happens in 2027 or waits for 2029 (D2);
   - what 2027-28 appropriations should do to the FY2029 defense base that NSC-1A holds flat.

1. **Seven housing design decisions**, one short memo each in `dossiers/home/memos/`, decided one at a time:
   - `1-help-or-homes.md`: where new rental help goes in tight and loose markets;
   - `2-how-broad.md`: how broad the rental guarantee is;
   - `3-production.md`, in two parts: tax credits and lasting affordability; the federal builder of last resort (HOU-9A, 9B or 9C);
   - `4-zoning.md`: what the zoning reward pays for; revised October 29 for the ROAD to Housing Act, which already has a growth reward fund and a CDBG reallocation (the recommendation now builds on them);
   - `5-homelessness.md`: Housing First and a recovery-housing option;
   - `6-prevention.md`: a standing emergency-rent fund or a one-time package;
   - `8-who-first.md`: who the guarantee reaches first.
   `dossiers/home/3-design.md` also asks a yes or no on fork 7 and on eight narrower points ("Recommended without a memo"); none is adopted until Espen agrees. Point 8 is now the investor limit: leave the ROAD to Housing Act's limit as enacted until the 2037 reports (HOU-7B, recommended), or remove its 2042 sunset now (HOU-7).
2. Optional uploads for housing section 2: HUD's Family Options Study reports and *A Picture of Subsidized Households*, and CBO's analysis of the 2023 immigration surge (publication 61464). They would replace secondary summaries (`dossiers/home/2-what-works.md`, "Evidence still needed").
3. Optional: upload HUD's *2025 Annual Homelessness Assessment Report*, Part 1 (May 2026), to raise the 2025 homelessness figures from grade C to A. *Worst Case Housing Needs 2025* and the 2024 homelessness report arrived October 28 and are in the library.
