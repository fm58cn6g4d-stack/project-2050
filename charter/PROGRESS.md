# Project 2050: progress board

Role: the live status of the plan (`charter/PLAN.md`, section 6): who is working, what is in motion, where each dossier stands, what comes next, known gaps and open questions for Espen. Only the lead edits it, folding in the "For the board" notes from workers' PRs (`DEC-2026-11-12-03`). Status: current. It holds no history: finished work is in Git and the PRs, decisions are in `charter/decisions.md`, and rules are in `charter/STANDARDS.md`.

Updated November 13, 2026 (about 23:10 UTC) by the outgoing lead, session_01UQzgBuU8feeYuYt6o6GeGK, for the lead handoff.

## Standing sessions

| Role | Session | Title | Since |
| --- | --- | --- | --- |
| Lead | `session_01UQzgBuU8feeYuYt6o6GeGK` | Project 2050: lead | November 13, about 06:00 UTC |
| Reviewer | `session_01UQzgBxNwxtd5koUq9phZwU` | Project 2050: reviewer | November 13, about 12:09 UTC; woken every three hours at :32 by the scheduled task `trig_019mwEJpZ4HeKBduzE2dM1ae` (older reviewer tasks are disabled) |
| Strategy | `session_01UQzgBuA3EdnR7Dx4kUq1un` | Project 2050: strategy and systems | October 27 |

**Former standing sessions** (the most recent; earlier ones are in this file's Git history):
- Lead `session_01UQzgBwNea5uYV7BMBRB3Ha`: the secure floor and immigration bookings to L3 (#304, #310), Espen's decisions DEC-2026-11-12-16 to -19 and DEC-2026-11-13-01 to -02, the care base under option C (#313), the reviewer handover, M2 (#312), clean power E-C1 (#315, #317), M3 parts 1-2 (#318 to #321); November 12 to 13.
- Reviewer `session_01UQzgBx3GY2ubHn3v5pRWdb`: PRs #323 to #331; November 13 (handed over at about 586,000 tokens).
- Reviewer `session_01UQzgBw6mqUQnF5hz7WbpQH`: PRs #314 to #322; November 13 (handed over at about 712,000 tokens).
- Reviewer `session_01UQzgBxJre9xhzNQVtr5prW`: PRs #284 to #313; November 12 to 13.
- Lead `session_01UQzgBuYpTa4haagP5TUTko`: the charter audit (#290, #291), the board rewrite and restart plan, 0o/0p/0q recorded, secure floor S4 to its booking (#304), immigration I4 and its review, budget inputs #289 and #297; November 12.
- Lead `session_01UQzgBtrMsAhWpEyfRAzn6W`: the care booking and paid-leave ceiling merges (#265, #266), the process rules `DEC-2026-11-12-01` to `-05`, the budget model's B6 remainder (#272 to #282), question 0q; November 12.

## In motion

**Lead handoff (November 13, about 23:10 UTC)** from `session_01UQzgBuU8feeYuYt6o6GeGK` (context past 612,000 tokens) to the new lead named in the Standing sessions table once it confirms.

- **Open PRs:**
  - #335, Espen's November 13 round, `DEC-2026-11-13-04` to `-08` (tier 3; author the outgoing lead; `charter/decisions.md` and one line in `charter/STANDARDS.md`'s design lens). Approved at `ececa9f`, current with main; **Espen was asked for the label at about 23:05 UTC.** The reviewer's optional note: DEC-06's "except 14" means the decision document's item 14 (memo 7), not point 14; a bracket would clarify, but a push needs a re-review, so it was left. The new lead owns #335 from now on.
  - The M4A financing follow-up (routine; author `session_01UQzgBtSzgtGkdukhQoJaNv`, branch `claude/m4a-financing-followup`): the reviewer's two wording notes on #334. No figures change.
- **Merged today:** #330 (D, `DEC-2026-11-13-03`, Espen's label), #332, #333 (the secure floor's status lines after D), #334 (the Medicare for All financing side-by-side, section 6 of `dossiers/foundations/checkpoint-financing.md`).
- **Workers (report to the lead):**
  - E-C2, clean power sections 4-9, `session_01UQzgBwvZTryixNAc6pThNU` (Most capable, started about 23:03 UTC), branch `claude/clean-power-e-c2`. It reads the decisions from #335's branch until #335 merges; it also moves the decided rows to L2 and fixes the library's "crs r44593" two homes. Then: the milestone review, its fixes, the booking.
  - The rebookings, `session_01UQzgBv5F38Tpd5UjbR3xCf` (Most capable, started about 23:03 UTC), branch `claude/rebook-inc4-imm6`: INC-4 rescoped (`DEC-2026-11-13-04`: only care neither the under-5 guarantee nor the school-age block grant pays) and immigration memo 6's health factor at 0.67 (`DEC-2026-11-13-05`, about −$26B over FY2030-39). Tier 3; it needs Espen's label after #335 merges. It touches no `charter/` file, so it won't conflict with #335.
  - The M4A worker `session_01UQzgBtSzgtGkdukhQoJaNv` holds its follow-up PR.
  - Reviewer: see Standing sessions.
  - Done, Espen may archive: D `session_01UQzgBtQcZhNsuZ4WPD35B5`; secure floor status `session_01UQzgBtrghrWBbFGS3ZaJNo`; and every session the board listed as done before.
- **The decision document** (a Claude Doc; the doc id is 881ecff6-a8f3-448b-89c5-ed3312e423ce and the artifact link is https://claude.ai/artifact/HouYTVFgnhsepKsZzoopxD; body node 83add86c-21a5): items 1-30, all answered. Item 1 (#330) is merged. Items 2-28 are in #335. Items 29-30 needed no decision. Espen comments there, and the lead answers in the doc's own threads with the Claude Docs connector.
- **Espen's direction today** (`DEC-2026-11-13-08`, in #335): use existing machinery and systems first, and simplify where a system or design is more complex and costly to administer than its purpose needs. Apply it in every brief and review.
- **Waiting on Espen:** #335's label; then the rebooking PR's label once it is reviewed and current. Nothing else is open for decision.
- **Small items for later:**
  - The secure floor README table's rows 1-2 still say "Draft (S2)" (#333 left them).
  - HOU-1, HOU-2 and HOU-3 are parent rows with no provisions, left at L2 (#329). The lead settles them with their children.
  - E-Verify's Social Security funds line is written up in #328 for a tier-3 change to the funds model.
  - M3's later items: replicate-weight intervals, the CBO-convention check, moving the budget readers to the measured keys.
  - The tier-3 cleanups from the legacy move: `merge-policy.json`, `scenarios.json`'s role text, `models/data/inputs/readme.md:43`.
- **Lead check-in:** `trig_01GVpVXmkRjHBDk6wp48qX5X` (`send_later`, about 00:17 UTC) is the outgoing lead's. The new lead recreates its own and disables this one; never delete it.
- **Labels and decision-log conflicts:** two tier-3 PRs that both add rows to `charter/decisions.md` conflict when the first merges, and the gate drops `espen-approved` from the second when that conflict is resolved. Ask Espen to label such PRs one at a time.
- **Gate note:** a routine PR can sit "ready, merging now" while main moves under it. GitHub's branch update (or a merge of main) un-sticks it; the approval carries over (#329, November 13).
- **Codex** access stays suspended; don't reach it with PR comments.
- **Espen's usage:** keep to three sessions, with lighter models for mechanical work.

## Next, in order

1. #335's label; the rebookings' label; E-C2 (sections 4-9), then clean power's milestone review and booking.
2. **Clean power (flagship 4, stage E's other flagship)**: E-C1 done (#315, #317); Espen's memo answers, then E-C2 (sections 4-9), the milestone review and the booking.
3. **Maintenance, alongside clean power:**
   - **M1** done (#326); follow-up #329 open. Left: the secure floor's lines after #330; HOU-1, HOU-2 and HOU-3 are parent rows with no provisions of their own, left at L2 (#329), for the lead to settle with their children; the library's "crs r44593" two homes (SRC-1942 and SRC-4465, clean power's row), for clean power's next step.
   - **M3, the household model:** parts 1-2 done (#318 to #322, #327). Left for a later Most capable session: replicate-weight intervals; the CBO-convention check; moving the budget model's readers to the measured keys; the model card's note that the fixture's exact reproduction holds as of `e897ac6`. INC-4's booking goes to Espen (above).
   - **Immigration:** the review's small items done (#328). Left: E-Verify's Social Security funds line (about −$42B over FY2030-39), written up in #328's "For the board" for a tier-3 change to the funds model; memo 6's health factor goes to Espen (above). The vote model's two-bill split stays paused with vote modeling (`charter/PLAN.md` 5).
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
| Secure floor (`dossiers/secure-floor/`, flagship 1) | L3 (alternatives and options at L1-L2) | Sections 1-9 and memos 1-7, decided (`DEC-2026-11-12-06`, `-09`, `-13` to `-15`); review #298, fixes #301; booked (#304, which was also the L3 re-check): about $2.53T over FY2030-39 and $292B in FY2040 | #330 (D, waits on Espen's label); SS-8's budget treatment (research); INC-1 to INC-5 are in the D3 test (#320) |
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
  - INC-1 to INC-5 are now in the D3 household test (#320).
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
