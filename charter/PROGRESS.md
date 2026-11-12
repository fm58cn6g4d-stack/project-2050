# Project 2050: progress board

Role: the live status of the plan (`charter/PLAN.md`, section 6): who is working, what is in motion, where each dossier stands, what comes next, known gaps and open questions for Espen. Only the lead edits it, folding in the "For the board" notes from workers' PRs (`DEC-2026-11-12-03`). Status: current. It holds no history: finished work is in Git and the PRs, decisions are in `charter/decisions.md`, and rules are in `charter/STANDARDS.md`.

Updated November 12, 2026 by the lead, session_01UQzgBuYpTa4haagP5TUTko.

## Standing sessions

| Role | Session | Title | Since |
| --- | --- | --- | --- |
| Lead | `session_01UQzgBuYpTa4haagP5TUTko` | Project 2050: lead | November 12, about 17:47 UTC |
| Reviewer | `session_01UQzgBxJre9xhzNQVtr5prW` | Project 2050: reviewer | November 12, about 17:48 UTC; woken every three hours at :32 by the scheduled task `trig_018vXM1DzQgYoSdYohwgxr72` (older reviewer tasks are disabled) |
| Strategy | `session_01UQzgBuA3EdnR7Dx4kUq1un` | Project 2050: strategy and systems | October 27 |

**Former standing sessions** (the most recent; earlier ones are in this file's Git history):
- Lead `session_01UQzgBtrMsAhWpEyfRAzn6W`: the care booking and paid-leave ceiling merges (#265, #266), the process rules `DEC-2026-11-12-01` to `-05`, the budget model's B6 remainder (#272 to #282), question 0q; November 12.
- Reviewer `session_01UQzgBufZFsrJoyrRZhNoe2`: PRs #265 to #283; November 12.
- Lead `session_01UQzgBtThMM4483EL9swRwN`: the overnight relay; care parts B-D to L3; the secure floor's S1-S3; immigration I1-I3; November 12.
- Reviewer `session_01UQzgBwfcHa4zjG9SpjSeAf`: PRs #257 to #268; November 12.

## In motion

- **Open PRs:** this board PR (routine, the lead); the budget-inputs PR for Moving America's FY2037-39 draw and question 0r (tier 3, the lead's subagent, opening soon); the FAM-1.11 follow-up (routine, S4's author, opening soon).
- **Workers (report to the lead):**
  - I4 (immigration sections 4-9), `session_01UQzgBufjvZ5c5m2JNm9iBZ`, Most capable, branch `claude/immigration-i4`: resumed after the audit.
  - S4's author, `session_01UQzgBwnUXwPDDfuRotwQLp`: the FAM-1.11 follow-up only (context near 490,000 tokens; no further work after it).
- **Lead check-in:** `trig_018c9dsspfuh2UnHeFTE5hWQ`, 22:07 UTC, re-armed every three hours.

## Next, in order

1. The FAM-1.11 follow-up and the budget-inputs PR (`DEC-2026-11-12-10` and the 0r decision) merge.
2. The secure floor's L2/L3 milestone review, in a fresh Most capable session, once I4's first PR is in review (to stay within three working sessions); then its fixes, then its booking (tier 3).
3. I4 finishes (two PRs, sections 4-6 then 7-9); then immigration's milestone review and booking.
4. **Maintenance at the stage D/E boundary**, after the secure floor reaches L3 and I4 is in review, before clean power starts:
   - **M1, dossier tidy-up** (Most capable): correct the out-of-date status lines in every dossier README and review file (see "Known gaps"); give the care dossier one map, a README with one status table across health and parts B-D, merging the health and "bcd" section files where they repeat each other; refresh transportation's `6-cost.md` to #289's figures.
   - **M2, library and housing mechanics** (Standard): `library/build_catalog.py` respects reserved ID blocks; one home for CRS R48552; catalog anchors for D and E evidence entries; `packages.py`'s stale housing label. Housing's own policy items stay deferred.
   - **M3, legacy outputs:** move the legacy suite's reports out of `legacy/` as part of rebuilding the household model, which stage G's fairness test needs; not a separate step.
5. **Settlement checkpoint at the end of stage E** (Most capable, one short memo for Espen): the plan-wide gap, the revenue options the legacy work holds, and which flagships drive the cost, so stages F and G are steered with the gap in view.
6. Clean power (flagship 4, stage E's second flagship), after M1-M2.

**The financing settlement** (stage G, `charter/PLAN.md` section 6): the first full settlement comes once the first wave's designs are specified (stages D-F), not after waves two and three. It is re-run when a later wave adds real cost, at each new CBO baseline, and once more before the plan goes public in 2028.

## Where each dossier stands

| Dossier | Level | Where it stands | Next |
| --- | --- | --- | --- |
| Political scenario (`dossiers/scenario/`, stage B) | — | Done (#78 to #101). Its 2027-28 questions are open, not urgent (questions below) | None scheduled; its README's file list is out of date |
| Housing (`dossiers/home/`, flagship 3) | L2, with the provisions the review passed at L3 | Sections 1-9, memos 1-13; milestone review passed (#182, re-check #194); booked (#193); closed in stage C (`DEC-2026-11-10-14`) | Priority pieces to L4 later; deferred items under "Known gaps" |
| Transportation (`dossiers/agenda/transportation/`, wave two) | L3 | Sections 1-9; review passed (#207, #213, #214); booked (MR6 #209; timing #289); closed in stage C | Refresh `6-cost.md` to #289's figures (the 24.4% offset, the FY2040 draw) when next opened; settlement items in its README |
| Health (`dossiers/care/`, flagship 2, part A) | L3 | Sections 1-9, memos 1-5; review passed (#224 to #229); booked (#230, #237, #279) | None; the README's status table is out of date |
| Care parts B-D (`dossiers/care/`, flagship 2) | L3 (FAM-2A to 2F at L2) | Sections 1b-9bcd, memos 6-17; review passed (#260, #263); booked (#265) | None; the README's status table is out of date |
| Secure floor (`dossiers/secure-floor/`, flagship 1) | L2 | Sections 1-9 and memos 1-7, decided (`DEC-2026-11-12-06`, `-09`); about $2.0T of legacy lines booked, about $0.47T over FY2030-39 and $56B in FY2040 not yet booked (`6-cost.md`, part 6) | Next steps 1-2 above |
| Immigration (`dossiers/immigration/`, flagship 6) | L1 | Sections 1-3 and memos 1-7, decided (`DEC-2026-11-12-07`); not booked (a replacement for the IMM-1/E11 row is proposed in `3-design.md`) | I4, sections 4-9 (in progress) |
| Clean power (flagship 4) | L1 | Not started | Stage E, after a slot frees |
| Work (flagship 5), democratic renewal, fair financing | L1 | Not started (stages F and G) | — |
| Rural delivery note (`dossiers/foundations/rural-delivery.md`) | — | Done (#171); applied project-wide by `DEC-2026-11-09-26` | Each dossier reads it for section 5 |

## Federal budget model (`models/tools/budget/`)

- **Done:** B1 conventions and assumptions; B2 data layer; B3 provision library; B5 viewer; B6 integration; B7 Espen's counting choices (`DEC-2026-11-08-03` to `-07`, `DEC-2026-11-12-08`). The workflow is `WORKFLOW.md` (#104).
- **B4 benchmarks:** Espen answered 0r: a light research pass on historical spend-out averages, an evidence-backed placeholder in the model, and B4 closed with PS-4b reported as not fully validated (to be recorded in the budget-inputs PR). `MODEL-CARD.md` lists what is validated, bounded and not yet validated.
- **Plan-wide FY2040 general-fund primary balance** (case `mixed`, after #289): about $4,185B short.
- Budget-model workers report to the lead.

## Known gaps

- **Secure floor (from S4, #287):**
  - The paid-leave fund's Treasury loan: the central case, which counts SSA's administration, peaks at about $182 billion in FY2040 and is repaid in 2058 (`dossiers/secure-floor/6-cost.md`, part 4). An earlier figure of $124 billion repaid by 2048 left administration out.
  - The Social Security booking carries a two-point broad payroll rate from 2035 that the decided design (memo 6 C) has only as a fallback, so it overstates trust-fund revenue. Decide how the trust fund's stock purchases (SS-8) are recorded before booking.
  - Memo 6 counted SS-3 and SS-4 twice; counted once, the package is about +4.0 to +4.6% of payroll against the 4.42% gap.
  - Nit: `tools/afa_floor.py`'s docstring should cite sec. 1(f)(6), not 1(f)(4).
- **Budget model:**
  - The climate pricing export (`legacy/sources/climate-portfolio-pricing.json`) still uses a 25% offset; CXP's booking differs from it by about $0.6 billion over FY2030-39 until the export is rebuilt (#289).
  - Held nits: a missing period after "HLT-3's slot" in HLT-7's ledger note (tier 3); "-0.00 points" on the dedicated-funds page.
- **For the financing settlement:** with child care and pre-K inside the education fund (EDU-9B), its reserve goes negative in 2035 at the 1.4-point rate (about 1.7 points keeps it solvent); R1's child benefit adds about $2.3 trillion in the ten years after its window (the Byrd rule).
- **Housing, deferred** (fix step 7, #193):
  - the HOU-2D tax credits are booked as parts of HOU-1, so they show as outlays; their own revenue row is a tier-3 change;
  - D and E evidence entries need a catalog anchor so the checker can resolve them;
  - `models/tools/financing-protection/packages.py` still labels a screen "additional housing 135 to 100" (HOU-4D is $115 billion);
  - 11 headline figures quoted in read-only legacy files no longer match the model (`legacy/index/check-report.md`); legacy is cited, never edited.
- **Library:**
  - `library/build_catalog.py` assigns the next free `SRC-` number even inside a dossier's reserved block; assign IDs by hand until it is fixed.
  - One name, CRS R48552, leads to two SNAP files (SRC-3610, SRC-3911); it needs one home.
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
