# Project 2050: progress board

Role: the live status of the plan (`charter/PLAN.md`, section 6): who is working, what is in motion, where each dossier stands, what comes next, known gaps and open questions for Espen. Only the lead edits it, folding in the "For the board" notes from workers' PRs (`DEC-2026-11-12-03`). Status: current. It holds no history: finished work is in Git and the PRs, decisions are in `charter/decisions.md`, and rules are in `charter/STANDARDS.md`.

Updated November 14, 2026 (about 08:40 UTC) by the outgoing lead, session_01UQzgBuP5ZGwT3KENpUcuNd, for the lead handoff.

## Standing sessions

| Role | Session | Title | Since |
| --- | --- | --- | --- |
| Lead | `session_01UQzgBuP5ZGwT3KENpUcuNd` (handing over; the new lead adds itself) | Project 2050: lead | November 13, about 23:16 UTC |
| Reviewer | `session_01UQzgBxNwxtd5koUq9phZwU` | Project 2050: reviewer | November 13, about 12:09 UTC; woken every three hours at :32 by the scheduled task `trig_019mwEJpZ4HeKBduzE2dM1ae` (older reviewer tasks are disabled) |
| Strategy | `session_01UQzgBuA3EdnR7Dx4kUq1un` | Project 2050: strategy and systems | October 27 |

**Former standing sessions** (the most recent; earlier ones are in this file's Git history):
- Lead `session_01UQzgBuP5ZGwT3KENpUcuNd`: the handoff and #335 merged; E-C2, the rebookings, M4 (energy and climate model, two sessions), clean power's milestone review, re-review on MOD-energy and booking at L3 (#359); Espen's decisions `DEC-2026-11-13-09` to `-15` and `DEC-2026-11-14-01`; the one-at-a-time merge queue; November 13 to 14.
- Lead `session_01UQzgBuU8feeYuYt6o6GeGK`: the overnight relay of November 13 (#320 to #334: M3 part 2 finished, M1, the stage E checkpoint memo, immigration's small items, option D), the decision document and Espen's November 13 round (#335, DEC-2026-11-13-04 to -08), two reviewer handovers, E-C2 and the rebookings started; November 13.
- Lead `session_01UQzgBwNea5uYV7BMBRB3Ha`: the secure floor and immigration bookings to L3 (#304, #310), Espen's decisions DEC-2026-11-12-16 to -19 and DEC-2026-11-13-01 to -02, the care base under option C (#313), the reviewer handover, M2 (#312), clean power E-C1 (#315, #317), M3 parts 1-2 (#318 to #321); November 12 to 13.
- Reviewer `session_01UQzgBx3GY2ubHn3v5pRWdb`: PRs #323 to #331; November 13 (handed over at about 586,000 tokens).
- Reviewer `session_01UQzgBw6mqUQnF5hz7WbpQH`: PRs #314 to #322; November 13 (handed over at about 712,000 tokens).
- Reviewer `session_01UQzgBxJre9xhzNQVtr5prW`: PRs #284 to #313; November 12 to 13.
- Lead `session_01UQzgBuYpTa4haagP5TUTko`: the charter audit (#290, #291), the board rewrite and restart plan, 0o/0p/0q recorded, secure floor S4 to its booking (#304), immigration I4 and its review, budget inputs #289 and #297; November 12.
- Lead `session_01UQzgBtrMsAhWpEyfRAzn6W`: the care booking and paid-leave ceiling merges (#265, #266), the process rules `DEC-2026-11-12-01` to `-05`, the budget model's B6 remainder (#272 to #282), question 0q; November 12.

## In motion

**Lead handoff (November 14, about 08:40 UTC)** from `session_01UQzgBuP5ZGwT3KENpUcuNd` (context about 705,000 tokens, past the 600,000 line) to a new lead. Its lineage depth is 5, so Espen (or the strategy session) starts the new lead with the one-line prompt: "You are the new Project 2050 lead: follow the handoff in charter/PROGRESS.md and .claude/skills/sessions/SKILL.md."

- **Merge queue (Espen, November 14: move open PRs through one by one).** Workers were told to push nothing until the lead says it is their turn; they commit locally. Order:
  1. #371 (tier 3, `DEC-2026-11-14-01`, carbon capture retrofits, memo 8 D; author the outgoing lead; the new lead owns it). Approved at `2020eac`, current with main `afd65e6`; **waits only on Espen's label**. Nothing else may move main until it merges.
  2. #362 (routine; clean power design test and memo 9's decided record; owner `session_01UQzgBwjJYCNKoAtuv3JaqD`). Conflicts with main; changes requested (catalog-facts.csv rewritten by a shallow clone; memo 9 fixes). The worker resolves locally and pushes when told.
  3. #372 (tier 3; the grid-account booking of memo 9 B; same worker). Changes requested (README status lines). **Before asking Espen for its label, tell Espen plainly** (the reviewer's note): as sized to ready-to-build projects, about $158B over FY2030-39 and $41B in FY2040 of the standard's payments stay as general-fund receipts and little grid is funded beyond CLI-10; the households' $163B top-up is gone; the "up to 1.4 Gt and 0.5 cents" is not bought on this sizing. Clean power falls to about $1.74T and $83B; the plan-wide FY2040 gap to about $4,163.0B. Espen may want to revisit the split.
  4. M4's branches (owner `session_01UQzgBsvbaeg7scCg7HJbVB`): `claude/m4-followups` (memo 8 marked decided, citing `DEC-2026-11-14-01`; needs #371 merged) and `claude/m4-pr3` (local; a second receipts benchmark against Treasury OTA, passes).
  After each merge: update the next PR's branch once (GitHub's update or a merge of main), then let it merge. Two tier-3 PRs that both add `charter/decisions.md` rows conflict: resolve by keeping both rows in order, then the reviewer re-approves.
- **Workers (report to the lead):**
  - Clean power part 2, `session_01UQzgBwjJYCNKoAtuv3JaqD` (Most capable; started 04:50 UTC): memo 9's decided record; a "how transmission actually gets built" section built on the legacy work (domain-climate, SRC-0155/0156/4532, legacy CLI-5, CLI-6D, CLI-10), cited by ID, plus 2026 data and BAAJA's manager's amendment; the CLI-10.03 siting fix (FPA 216 needs a DOE corridor; DOE cancelled all three on August 12, 2026); evidence updates; then #372.
  - M4 part 2, `session_01UQzgBsvbaeg7scCg7HJbVB` (Most capable; started 04:33 UTC, taking over from `session_01UQzgBtLC9XG5ZhhwqzJVwW`): memo 8 follow-up; PR-3; then a ranked list of new model capabilities, each saying what it implies for clean power (Espen: "continue refining itself and building more utility by being able to analyze more aspects of climate policy"; "incorporate its findings into the clean power dossier ... to back up, interrogate, and design the best climate policy package we can").
  - Reviewer: `session_01UQzgBxNwxtd5koUq9phZwU`, **context about 520,000 tokens: hand it over first** (the new lead starts the successor; schedule from `trig_019mwEJpZ4HeKBduzE2dM1ae`).
  - Done, Espen may archive: the first M4 session `session_01UQzgBtLC9XG5ZhhwqzJVwW` (#342 to #361, #364 handed over); clean power's review, booking and design-test session `session_01UQzgButU9bQRw8o2Tq3QvS` (#344, #346, #349, #351, #354, #359); E-C2, the rebookings, M4A, D and secure floor status sessions; former lead `session_01UQzgBuU8feeYuYt6o6GeGK`.
- **Merged since the last board update:** #357 to #361, #363 to #370 (among them: clean power booked at L3, #359, on option A for the standard's payments offset; `DEC-2026-11-13-14`, memo 9 B with the grid account sized to ready-to-build projects; `DEC-2026-11-13-15`, use all information as evidence, not as a default; M4's CCS retrofit option, design menu and history checks). Plan-wide FY2040 gap: $4,203.9B short after #359.
- **MOD-energy status:** working. HI-1 (2015-25 power history) fails narrowly, 5.7% against 5%: coal-gas switching too strong, so near-term power cuts and early receipts lean high (disclosed in the booking). A damped coal response is the planned fix. A snapshot page for Espen: https://claude.ai/artifact/HtUiL7sspMPqMT8oG33DYp (not a source of record).
- **Espen's process notes, November 14:** (1) run one merge queue; workers push only when told. Write this into `.claude/skills/sessions/SKILL.md` in the next tier-3 batch. (2) Use all information as evidence, not as a default (`DEC-2026-11-13-15`, in STANDARDS and the skill); no extra section on each document.
- **Waiting on Espen:** #371's label; then #372's label after Espen sees the receipts point above.
- **Small items for later:** a guard in `library/build_catalog.py` against shallow-clone rewrites of catalog-facts.csv; the secure floor README rows 1-2; HOU-1 to HOU-3; E-Verify's funds line; M3's later items; the legacy-move tier-3 cleanups; "CX, 25%" labels in climate-portfolio `pricing.py`; booking D's small cost with #372's change.
- **Next after the queue:** the settlement checkpoint memo (`dossiers/foundations/checkpoint-financing.md`), now that clean power is booked.
- **Lead check-in:** the outgoing lead's `send_later` check-ins are disabled at handoff; the new lead sets its own.
- **Codex** stays suspended. **Espen's usage:** keep to three working sessions, efficient briefs.

## Next, in order

1. Clean power's booking (tier 3, in progress; the L3 close-out), then Espen's label; then the settlement checkpoint memo (item 4).
2. **Clean power (flagship 4, stage E's other flagship)**: E-C1 done (#315, #317); memos decided (#335, `DEC-2026-11-13-06`, `-07`); E-C2 done (#338, #341: sections 4-9 at L2; about $1.85T over FY2030-39 and $147B in FY2040); milestone review and fixes done (#344, #346), re-reviewed on MOD-energy (#349, #351, #354); the booking in progress.
3. **Maintenance, alongside clean power:**
   - **M1** done (#326, follow-up #329; the secure floor's lines after D in #333; the "crs r44593" two homes in #338). Left: HOU-1, HOU-2 and HOU-3 are parent rows with no provisions of their own, left at L2 (#329), for the lead to settle with their children.
   - **M3, the household model:** parts 1-2 done (#318 to #322, #327). Left for a later Most capable session: replicate-weight intervals; the CBO-convention check; moving the budget model's readers to the measured keys; the model card's note that the fixture's exact reproduction holds as of `e897ac6`. INC-4 is rebooked at about $0.5B a year on the household model's measure (#339, `DEC-2026-11-13-04`).
   - **Immigration:** the review's small items done (#328). Left: E-Verify's Social Security funds line (about −$42B over FY2030-39), written up in #328's "For the board" for a tier-3 change to the funds model; memo 6's health factor is rebooked at 0.67 (#339, `DEC-2026-11-13-05`). The vote model's two-bill split stays paused with vote modeling (`charter/PLAN.md` 5).
4. **Settlement checkpoint memo for Espen** at the end of stage E (first draft merged, #325, `dossiers/foundations/checkpoint-financing.md`; finished after clean power is booked): the plan-wide gap, the revenue options the legacy work holds, and which flagships drive the cost.

**The financing settlement** (stage G, `charter/PLAN.md` section 6): once the first wave's designs are specified; re-run as later waves add cost, at each new CBO baseline, and before 2028.

## Where each dossier stands

| Dossier | Level | Where it stands | Next |
| --- | --- | --- | --- |
| Political scenario (`dossiers/scenario/`, stage B) | — | Done (#78 to #101). Its 2027-28 questions are open, not urgent (questions below) | None scheduled; its README's file list is out of date |
| Housing (`dossiers/home/`, flagship 3) | L2, with the provisions the review passed at L3 | Sections 1-9, memos 1-13; milestone review passed (#182, re-check #194); booked (#193); closed in stage C (`DEC-2026-11-10-14`) | Priority pieces to L4 later; deferred items under "Known gaps" |
| Transportation (`dossiers/agenda/transportation/`, wave two) | L3 | Sections 1-9; review passed (#207, #213, #214); booked (MR6 #209; timing #289); closed in stage C | Refresh `6-cost.md` to #289's figures (the 24.4% offset, the FY2040 draw) when next opened; settlement items in its README |
| Health (`dossiers/care/`, flagship 2, part A) | L3 | Sections 1-9, memos 1-5; review passed (#224 to #229); booked (#230, #237, #279) | None (README map fixed, #326) |
| Care parts B-D (`dossiers/care/`, flagship 2) | L3 (FAM-2A to 2F at L2) | Sections 1b-9bcd, memos 6-17; review passed (#260, #263); booked (#265) | None (README map fixed, #326) |
| Secure floor (`dossiers/secure-floor/`, flagship 1) | L3 (alternatives and options at L1-L2) | Sections 1-9 and memos 1-7, decided (`DEC-2026-11-12-06`, `-09`, `-13` to `-15`); review #298, fixes #301; booked (#304, which was also the L3 re-check), then D (#330) and INC-4 rescoped (#339): about $2.59T over FY2030-39 and $298B in FY2040 | SS-8's budget treatment (research); INC-1 to INC-5 are in the D3 test (#320) |
| Immigration (`dossiers/immigration/`, flagship 6) | L3 (alternatives at L2) | Sections 1-9, memos 1-7 and the first immigration model (`tools/immigration_model.py`), decided (`DEC-2026-11-12-07`, `-12`, `-17` to `-19`); milestone review #303, fixes #305 and #307; booked (#310, which was also the L3 re-check), memo 6's health factor at 0.67 (#339): about +$149B over FY2030-39 and +$22.5B in FY2040 | IMM-1.23's long-term care text follows option C (the care base correction); the open items in "Next" |
| Clean power (`dossiers/clean-power/`, flagship 4) | L2 (L3 on booking) | Sections 1-9 and memos 1-7, decided (#335, `DEC-2026-11-13-10` to `-13`); milestone review and fixes (#344, #346); re-review on MOD-energy (#349, #351, #354): the decided set about $1,854B over FY2030-39 and $113B in FY2040 (−$51.6B against the booked legacy rows), not yet booked | The booking (tier 3, in progress) |
| Work (flagship 5), democratic renewal, fair financing | L1 | Not started (stages F and G) | — |
| Rural delivery note (`dossiers/foundations/rural-delivery.md`) | — | Done (#171); applied project-wide by `DEC-2026-11-09-26` | Each dossier reads it for section 5 |

## Federal budget model (`models/tools/budget/`)

- **Done:** B1 conventions and assumptions; B2 data layer; B3 provision library; B5 viewer; B6 integration; B7 Espen's counting choices (`DEC-2026-11-08-03` to `-07`, `DEC-2026-11-12-08`). The workflow is `WORKFLOW.md` (#104).
- **B4 benchmarks:** Espen answered 0r: a light research pass on historical spend-out averages, an evidence-backed placeholder in the model, and B4 closed with PS-4b reported as not fully validated (`DEC-2026-11-12-11`, #297). `MODEL-CARD.md` lists what is validated, bounded and not yet validated.
- **Plan-wide FY2040 general-fund primary balance** (case `mixed`, after #339): about $4,245.4B short (7.84% of GDP).
- Budget-model workers report to the lead.

## Known gaps

- **Immigration (from #313):** `dossiers/immigration/3-design.md`'s proposed shared-rule-3 note needs its first sentence changed (long-term care now narrows too) before it goes into `dossiers/shared-rules.md`.
- **Secure floor (from S4, #287):**
  - SS-8, the trust funds' stock investment, is booked at zero: how the budget records the purchases (outlays, financing, or returns above Treasury's rate) needs a check of CBO's and OMB's treatment; the Railroad Retirement trust is the nearest precedent.
  - INC-1 to INC-5 are now in the D3 household test (#320).
  - Nit: `tools/afa_floor.py`'s docstring should cite sec. 1(f)(6), not 1(f)(4).
- **Budget model:**
  - Held nits: a missing period after "HLT-3's slot" in HLT-7's ledger note (tier 3); "-0.00 points" on the dedicated-funds page.
- **For the financing settlement:** with child care and pre-K inside the education fund (EDU-9B), its reserve goes negative in 2035 at the 1.4-point rate (about 1.7 points keeps it solvent); R1's child benefit adds about $2.3 trillion in the ten years after its window (the Byrd rule).
- **Housing, deferred** (fix step 7, #193):
  - the HOU-2D tax credits are booked as parts of HOU-1, so they show as outlays; their own revenue row is a tier-3 change;
  - `models/tools/financing-protection/packages.py`'s screen "additional housing 135 to 100" predates HOU-4D's $115 billion; it stays as a historical screen until the financing settlement rebuilds the screens (#312);
  - 11 headline figures quoted in read-only legacy files no longer match the model (`legacy/index/check-report.md`); legacy is cited, never edited.
- **Library:**
  - Reserved source blocks live in `library/reserved-blocks.csv`; a new dossier adds its row there (#312).
  - `catalog-facts.csv` dates depend on the clone's history depth, so the file is refreshed, never checked.
- **Out-of-date status lines in dossier files:** fixed by #326 except the secure floor's (after #330) and clean power's (after its memo answers).
- **Public pages:** two story claims (`q4`, `downside`) cite figures that PR #45 changed; the page stays pinned to its evidence commit until an editor rereads it. `public/site/index.html` is pinned to an older commit and is rebuilt in stage H.
- **Legacy outputs:** the legacy suite still writes reports into `legacy/index/` and `legacy/sources/` until each core model is rebuilt (`models/README.md`).

## Directions for later stages

- **Education (EDU-5):** address college students' costs, including those the dropped $500 other-dependents credit covered (`DEC-2026-11-12-09`).
- **Democratic renewal:** DEM-2's structure (one provision, a severable bill, two bills, or the legacy DEM-2E; `dossiers/scenario/memo-defense-baseline-and-dem2.md`, choice b) goes to that dossier's memo set.
- **Transportation, fuel taxes may be revisited** (`DEC-2026-11-10-14`): when transportation is next opened, or the financing settlement weighs user fees against general revenue, weigh a smaller or later fuel-tax path, more general-fund support, or the per-mile and weight-distance charges carrying more, with the cost of each.
- **Health, Medicare "Part E" as an alternative to weigh later** (Espen, November 11: "worth noting this slight alternative for consideration later"): Jacob Hacker's design as Robert Kuttner describes it (The American Prospect, October 2026), where employers either offer plans meeting Medicare's standards or pay into Medicare, indefinitely, instead of a firm 2035 endpoint.
- **Stage H (public site):** ask Espen to turn the Figma connector back on first.

## Questions for Espen

0a. **Stage B's 2027-28 questions** (not urgent before the lame duck ends; `dossiers/scenario/3-framework-2027-28.md`, section 7, and `2027-28-stress-tests.md`, "Next questions"): what 2027-28 is for; when an early deal is worth locking in a design; whether a Senate rules change happens in 2027 or waits for 2029 (D2); the FY2028 defense path before summer 2027 (it sets NSC-1A's base); protecting the FY2029 reconciliation slot; a position on 2027 mid-decade redraws.

Optional: HUD's *2025 Annual Homelessness Assessment Report*, Part 1 (May 2026), would raise housing's 2025 homelessness figures from grade C to A.
