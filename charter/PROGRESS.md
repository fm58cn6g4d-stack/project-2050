# Project 2050: progress board

Role: the live status of the plan (`charter/PLAN.md`, section 6): who is working, what is in motion, where each dossier stands, what comes next, known gaps and open questions for Espen. Only the lead edits it, folding in the "For the board" notes from workers' PRs (`DEC-2026-11-12-03`). Status: current. It holds no history: finished work is in Git and the PRs, decisions are in `charter/decisions.md`, and rules are in `charter/STANDARDS.md`.

Updated November 13, 2026 (about 06:05 UTC) by the lead, session_01UQzgBuU8feeYuYt6o6GeGK.

## Standing sessions

| Role | Session | Title | Since |
| --- | --- | --- | --- |
| Lead | `session_01UQzgBuU8feeYuYt6o6GeGK` | Project 2050: lead | November 13, about 06:00 UTC |
| Reviewer | `session_01UQzgBx3GY2ubHn3v5pRWdb` | Project 2050: reviewer | November 13, about 06:00 UTC; woken every three hours at :32 by the scheduled task `trig_01HM2PZzezuaA4AA2ThDMR8P` (older reviewer tasks are disabled) |
| Strategy | `session_01UQzgBuA3EdnR7Dx4kUq1un` | Project 2050: strategy and systems | October 27 |

**Former standing sessions** (the most recent; earlier ones are in this file's Git history):
- Lead `session_01UQzgBwNea5uYV7BMBRB3Ha`: the secure floor and immigration bookings to L3 (#304, #310), Espen's decisions DEC-2026-11-12-16 to -19 and DEC-2026-11-13-01 to -02, the care base under option C (#313), the reviewer handover, M2 (#312), clean power E-C1 (#315, #317), M3 parts 1-2 (#318 to #321); November 12 to 13.
- Reviewer `session_01UQzgBw6mqUQnF5hz7WbpQH`: PRs #314 to #322; November 13 (handed over at about 712,000 tokens).
- Reviewer `session_01UQzgBxJre9xhzNQVtr5prW`: PRs #284 to #313; November 12 to 13.
- Lead `session_01UQzgBuYpTa4haagP5TUTko`: the charter audit (#290, #291), the board rewrite and restart plan, 0o/0p/0q recorded, secure floor S4 to its booking (#304), immigration I4 and its review, budget inputs #289 and #297; November 12.
- Lead `session_01UQzgBtrMsAhWpEyfRAzn6W`: the care booking and paid-leave ceiling merges (#265, #266), the process rules `DEC-2026-11-12-01` to `-05`, the budget model's B6 remainder (#272 to #282), question 0q; November 12.

## In motion

- **Open PRs:**
  - #320, the secure floor's INC-1 to INC-5 rows in `models/data/inputs/incidence-rows.csv` (tier 3; the M3 part 2 worker). Re-approved at `f4fe603` by both reviewers; **Espen labeled it** about 06:09 UTC; the worker merged main again (`010b2e5`), which keeps the label and approvals, so it merges on the gate.
  - This board PR.
- **Merged since the handoff:** #316 (`DEC-2026-11-13-02`, November 13, 05:53 UTC); #322; #323, the handoff note.
- **Workers (report to the lead):**
  - M3 part 2, `session_01UQzgBvcq5CFU3aHTEQs51E` (Most capable). Queue, in order: #320's main merge; the legacy-reports move (`d3.py` replaces `incidence-*.py`, branch `claude/m3-part2-legacy-move`, opens after #320); then **Espen's answer D on the 65-cent ceiling** ("go with D on the 65-cent ceiling", November 13): SNAP's earned-income deduction from 20% to 45%, up to about $32B a year, as one tier-3 PR with its `DEC-` entry (the next 11-13 ID), the provision in the secure floor's specification, its booking and the re-run check. #316 has merged, so it no longer waits on a decision-log conflict. Lead's answers already given: INC-1.02 read so no family loses the EITC; INC-4's $0.3B-measured against $4.5B-booked gap gets a reconciliation note, not a booking change; the housing key's central case is the CPS spread (93% in Q1), the legacy 60% a sensitivity.
  - M1, the dossier tidy-up, `session_01UQzgBtAeRDYo4gqoiVQ76i` (Most capable, started about 06:01 UTC), branch `claude/m1-dossier-tidy`: dossier status lines and review headers, care's one status table, care `6-cost.md` part 5 and transportation `6-cost.md` refreshed, the library's "crs r44593" two-homes nit. It stays out of `dossiers/secure-floor/` while D is open, and lists those stale lines for the board.
  - Stage E checkpoint memo, first draft, `session_01UQzgBxH31r4ahuzdcCUEwy` (Most capable, started about 06:05 UTC): the one-sheet in "Next", item 4, drafted now with clean power marked pending, as `dossiers/foundations/checkpoint-financing.md` (branch `claude/g0-financing-scope` or `claude/stage-e-checkpoint-memo`). It covers the plan-wide gap, which flagships drive it, the inputs still moving, the revenue options the legacy work holds, and the questions stage G will ask. It is not the settlement: stage G stays paused until the designs are fixed. Espen, November 13: "begin the financing settlement work overnight, too ... at least have the research and options and such scoped out", then "not the full settlement, the check-in partial/one-sheet/high-level financing analysis" and "not full stage G, we talked about this earlier".
  - Reviewer: see Standing sessions.
  - Next when a slot frees: immigration's small items (Standard or Most capable; "Next", item 3).
  - Done, Espen may archive: clean power E-C1 `session_01UQzgBvGHoWGmLZJ179V9R7` (#315, #317); M3 part 1 `session_01UQzgBwdLcHcwAfDxTeXZaS` (#318, #319); care base `session_01UQzgBskUP5ct6NJr6zMve5` (#313); former reviewers `session_01UQzgBxJre9xhzNQVtr5prW` and `session_01UQzgBw6mqUQnF5hz7WbpQH`; former lead `session_01UQzgBwNea5uYV7BMBRB3Ha` (no open PRs once #323 merged).
- **Waiting on Espen:**
  - **Clean power's memo batch** (#317, merged; `dossiers/clean-power/memos/README.md`): memos 1-7 (eleven decisions) and points 1-14, each recommended. Put to Espen on November 13 with a table; no answer yet. On the answers: one tier-3 DEC PR, then E-C2 (sections 4-9) in a fresh Most capable session.
  - The D PR's label, once it is open, reviewed and current (#320 is labeled).
- **Espen's instruction for the night** (November 13, about 06:00 UTC): "pls keep things moving over night, and make progress wherever you can, then prepare clear summaries and decision docs for me tmw". So: up to three sessions on ready steps (M3 part 2, M1, the checkpoint memo draft; then immigration's small items; E-C2 waits on the memo answers), and by Espen's morning (Eastern) one plain summary of the night and one decision document covering the clean power memo batch, the labels waiting and anything new, every item numbered with its recommendation and cost.
- **Small tier-3 cleanups for later (from the legacy move):** `.github/merge-policy.json` still lists `legacy/index/revenue-household-incidence-model.md` as a generated output (harmless; drop it later); `models/data/inputs/scenarios.json`'s "role" text names `incidence-model.py` (should name `models/tools/household/d3.py`). The child-poverty validation suite stays in `run-checks.sh` until the household model ports its 8 agenda cases.
- **Lead check-in:** `trig_01Q9afGUKy8hTHcdsTpJX5FT` (`send_later`, 09:01 UTC), re-armed every three hours. The outgoing lead's `trig_01PgFK2nZnrqDchtrJ9VG2bj` and the old reviewer task `trig_01QHkurHcrA7npaVk277NyeR` are disabled, not deleted.
- **Labels and decision-log conflicts:** two tier-3 PRs that both add rows to `charter/decisions.md` conflict when the first merges, and the gate drops `espen-approved` from the second when that conflict is resolved (#310, November 13). Ask Espen to label such PRs one at a time, the next only after the first merges and the second is updated.
- **Codex** access to the repository is suspended by Espen for now (out of credits); don't reach it with PR comments until it is restored.
- **Espen's usage:** a weekly-limit reset was used on November 12 and lasts until Monday at 2 am Eastern; about 12% was used by Thursday night, November 12. Keep to three sessions, with lighter models for mechanical work.

## Next, in order

1. #320 current, re-approved and labeled; the legacy-reports move; the 65-cent fix (D).
2. **Clean power (flagship 4, stage E's other flagship)**: E-C1 done (#315, #317); Espen's memo answers, then E-C2 (sections 4-9), the milestone review and the booking.
3. **Maintenance, alongside clean power:**
   - **M1, dossier tidy-up** (Most capable): out-of-date status lines in every dossier README and review file (see "Known gaps"); care's one map; transportation's `6-cost.md` refreshed to #289 and #297's figures. Also: care's `6-cost.md` part 5 table still shows #230's totals; immigration's README and status lines (L3); the board's own `M2` notes.
   - **M3, the household model rebuild** (part 1 done, #318 and #319; part 2 in progress, see above), **with the legacy outputs:** `models/tools/household/` from the legacy incidence model and the child-poverty microsimulation, with a model card and benchmarks (Census poverty figures, the Tax Policy Center). Move the legacy suite's reports out of `legacy/` as it replaces them. Most capable, about two or three sessions. The secure floor's 65-cent ceiling, the checkpoint's revenue options and stage G's fairness test need it. Also give INC-1 to INC-5 incidence keys (#304's open item).
   - Immigration's open items (small): the vote model's two-bill split for IMM-1 (memo 7 part 3); a Social Security funds line for E-Verify's −$42B; spot checks W-1, W-3 and C-5 from the milestone review.
4. **Settlement checkpoint memo for Espen** at the end of stage E (first draft in progress now, finished after clean power is booked): the plan-wide gap, the revenue options the legacy work holds, and which flagships drive the cost.

**The financing settlement** (stage G, `charter/PLAN.md` section 6): once the first wave's designs are specified; re-run as later waves add cost, at each new CBO baseline, and before 2028.

## Where each dossier stands

| Dossier | Level | Where it stands | Next |
| --- | --- | --- | --- |
| Political scenario (`dossiers/scenario/`, stage B) | — | Done (#78 to #101). Its 2027-28 questions are open, not urgent (questions below) | None scheduled; its README's file list is out of date |
| Housing (`dossiers/home/`, flagship 3) | L2, with the provisions the review passed at L3 | Sections 1-9, memos 1-13; milestone review passed (#182, re-check #194); booked (#193); closed in stage C (`DEC-2026-11-10-14`) | Priority pieces to L4 later; deferred items under "Known gaps" |
| Transportation (`dossiers/agenda/transportation/`, wave two) | L3 | Sections 1-9; review passed (#207, #213, #214); booked (MR6 #209; timing #289); closed in stage C | Refresh `6-cost.md` to #289's figures (the 24.4% offset, the FY2040 draw) when next opened; settlement items in its README |
| Health (`dossiers/care/`, flagship 2, part A) | L3 | Sections 1-9, memos 1-5; review passed (#224 to #229); booked (#230, #237, #279) | None; the README's status table is out of date |
| Care parts B-D (`dossiers/care/`, flagship 2) | L3 (FAM-2A to 2F at L2) | Sections 1b-9bcd, memos 6-17; review passed (#260, #263); booked (#265) | None; the README's status table is out of date |
| Secure floor (`dossiers/secure-floor/`, flagship 1) | L3 (alternatives and options at L1-L2) | Sections 1-9 and memos 1-7, decided (`DEC-2026-11-12-06`, `-09`, `-13` to `-15`); review #298, fixes #301; booked (#304, which was also the L3 re-check): about $2.53T over FY2030-39 and $292B in FY2040 | Incidence keys for INC-1 to INC-5 (M3); SS-8's budget treatment (research) |
| Immigration (`dossiers/immigration/`, flagship 6) | L3 (alternatives at L2) | Sections 1-9, memos 1-7 and the first immigration model (`tools/immigration_model.py`), decided (`DEC-2026-11-12-07`, `-12`, `-17` to `-19`); milestone review #303, fixes #305 and #307; booked (#310, which was also the L3 re-check): about +$175B over FY2030-39 and +$28.8B in FY2040 | IMM-1.23's long-term care text follows option C (the care base correction); the open items in "Next" |
| Clean power (`dossiers/clean-power/`, flagship 4) | L1 | Sections 1-3 and memos 1-7 drafted (#315, #317); about +$0.11T against the booked legacy climate rows, about $1.9T over FY2030-39 and $156B in FY2040 for the recommended set | Espen's memo answers, then E-C2 |
| Work (flagship 5), democratic renewal, fair financing | L1 | Not started (stages F and G) | — |
| Rural delivery note (`dossiers/foundations/rural-delivery.md`) | — | Done (#171); applied project-wide by `DEC-2026-11-09-26` | Each dossier reads it for section 5 |

## Federal budget model (`models/tools/budget/`)

- **Done:** B1 conventions and assumptions; B2 data layer; B3 provision library; B5 viewer; B6 integration; B7 Espen's counting choices (`DEC-2026-11-08-03` to `-07`, `DEC-2026-11-12-08`). The workflow is `WORKFLOW.md` (#104).
- **B4 benchmarks:** Espen answered 0r: a light research pass on historical spend-out averages, an evidence-backed placeholder in the model, and B4 closed with PS-4b reported as not fully validated (`DEC-2026-11-12-11`, #297). `MODEL-CARD.md` lists what is validated, bounded and not yet validated.
- **Plan-wide FY2040 general-fund primary balance** (case `mixed`, after #313): about $4,239B short (7.83% of GDP).
- Budget-model workers report to the lead.

## Known gaps

- **Immigration (from #313):** `dossiers/immigration/3-design.md`'s proposed shared-rule-3 note needs its first sentence changed (long-term care now narrows too) before it goes into `dossiers/shared-rules.md`.
- **Secure floor (from S4, #287):**
  - SS-8, the trust funds' stock investment, is booked at zero: how the budget records the purchases (outlays, financing, or returns above Treasury's rate) needs a check of CBO's and OMB's treatment; the Railroad Retirement trust is the nearest precedent.
  - INC-1 to INC-5 have no incidence keys, so they are not in the D3 household test (M3).
  - Nit: `tools/afa_floor.py`'s docstring should cite sec. 1(f)(6), not 1(f)(4).
- **Budget model:**
  - The climate pricing export (`legacy/sources/climate-portfolio-pricing.json`) still uses a 25% offset; CXP's booking differs from it by about $0.6 billion over FY2030-39 until the export is rebuilt (#289).
  - Held nits: a missing period after "HLT-3's slot" in HLT-7's ledger note (tier 3); "-0.00 points" on the dedicated-funds page.
- **For the financing settlement:** with child care and pre-K inside the education fund (EDU-9B), its reserve goes negative in 2035 at the 1.4-point rate (about 1.7 points keeps it solvent); R1's child benefit adds about $2.3 trillion in the ten years after its window (the Byrd rule).
- **Housing, deferred** (fix step 7, #193):
  - the HOU-2D tax credits are booked as parts of HOU-1, so they show as outlays; their own revenue row is a tier-3 change;
  - `models/tools/financing-protection/packages.py`'s screen "additional housing 135 to 100" predates HOU-4D's $115 billion; it stays as a historical screen until the financing settlement rebuilds the screens (#312);
  - 11 headline figures quoted in read-only legacy files no longer match the model (`legacy/index/check-report.md`); legacy is cited, never edited.
- **Library:**
  - Reserved source blocks live in `library/reserved-blocks.csv`; a new dossier adds its row there (#312).
  - `catalog-facts.csv` dates depend on the clone's history depth, so the file is refreshed, never checked.
- **Out-of-date status lines in dossier files:** the transportation README ("in progress, step 7"); the care README's tables; housing's `review-milestone.md` ("L3 not yet"); the immigration README (0p "with Espen"); the scenario README's file list. Step M1 fixes them.
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
