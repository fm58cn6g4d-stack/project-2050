# Project 2050: progress board

Role: the live status of the plan (`charter/PLAN.md`, section 6): who is working, what is in motion, where each dossier stands, what comes next, known gaps and open questions for Espen. Only the lead edits it, folding in the "For the board" notes from workers' PRs (`DEC-2026-11-12-03`). Status: current. It holds no history: finished work is in Git and the PRs, decisions are in `charter/decisions.md`, and rules are in `charter/STANDARDS.md`.

Updated November 12, 2026 (about 22:20 UTC) by the lead, session_01UQzgBwNea5uYV7BMBRB3Ha.

## Standing sessions

| Role | Session | Title | Since |
| --- | --- | --- | --- |
| Lead | `session_01UQzgBwNea5uYV7BMBRB3Ha` | Project 2050: lead | November 12, about 22:01 UTC |
| Reviewer | `session_01UQzgBxJre9xhzNQVtr5prW` | Project 2050: reviewer | November 12, about 17:48 UTC; woken every three hours at :32 by the scheduled task `trig_018vXM1DzQgYoSdYohwgxr72` (older reviewer tasks are disabled) |
| Strategy | `session_01UQzgBuA3EdnR7Dx4kUq1un` | Project 2050: strategy and systems | October 27 |

**Former standing sessions** (the most recent; earlier ones are in this file's Git history):
- Lead `session_01UQzgBuYpTa4haagP5TUTko`: the charter audit (#290, #291), the board rewrite and restart plan, 0o/0p/0q recorded, secure floor S4 to its booking (#304), immigration I4 and its review, budget inputs #289 and #297; November 12.
- Lead `session_01UQzgBtrMsAhWpEyfRAzn6W`: the care booking and paid-leave ceiling merges (#265, #266), the process rules `DEC-2026-11-12-01` to `-05`, the budget model's B6 remainder (#272 to #282), question 0q; November 12.
- Reviewer `session_01UQzgBufZFsrJoyrRZhNoe2`: PRs #265 to #283; November 12.
- Lead `session_01UQzgBtThMM4483EL9swRwN`: the overnight relay; care parts B-D to L3; the secure floor's S1-S3; immigration I1-I3; November 12.
- Reviewer `session_01UQzgBwfcHa4zjG9SpjSeAf`: PRs #257 to #268; November 12.

## In motion

- **Open PRs:**
  - #309, Espen's answer on Social Security's cap, one new decision entry (tier 3; the lead). Waiting on the reviewer, then Espen's label (ping them).
  - #307, immigration: Espen's answers written in (routine; author the immigration worker). Waiting on the reviewer.
  - This board PR.
- **Workers (report to the lead):**
  - Immigration milestone review and fix steps 1-4, `session_01UQzgBtaHE8nkT9Znw8gZVp` (#303, #305, both merged; about 315,000 tokens). Sent a `handoff` naming the new lead; asked for its `done` and it will take the immigration booking (brief sent once #304 merged). Its #307 (routine, open) writes Espen's three answers into the dossier and reprices: the decided set is about +$0.17T over FY2030-39 and +$27.7B in FY2040. It also finds care's base overstated by about $430B over FY2030-39 under option C, which goes to a health booking correction.
  - Secure floor fix session `session_01UQzgBwAwdHFG8ArnCwHdrQ`: done (#298, #301).
  - I4 author `session_01UQzgBufjvZ5c5m2JNm9iBZ`: done (#294, #299).
  - The outgoing lead, `session_01UQzgBuYpTa4haagP5TUTko`: stepped back; its PRs are handed over.
- **Espen's answers still to record as DEC entries** (in the immigration booking PR, tier 3; quote Espen):
  - "both as recommended" on the review's two questions (from-abroad applications, limited; the signing-day cutoff kept and stated plainly).
  - Health coverage for people without status: **C**. The single plan covers people with registered status or any lawful status, including lawful temporary workers. People with no status get emergency care only, as today. Priced net of the Emergency Medicaid and uncompensated care already paid for those who gain coverage. This amends `DEC-2026-11-12-07` memo 6 C for health only. Espen: "i think it has to be C, with the proper net cost fixes for current care outlays". A later look at coverage for farmworkers, contractors, transient and seasonal workers is noted for section 8.
- **A check for Espen, from #307:** the long-term care benefit (IMM-1.23) stays "every resident", since the option C amendment was for health coverage only. Is that the intent?
- **Social Security's cap:** Espen answered "keep the one-point cap"; recorded in #309.
- **Lead check-in:** `trig_01S1Wi1m3GphpoGYxPDe6ZJ4` (`send_later`, November 13, 01:03 UTC), re-armed every three hours. The outgoing lead's `trig_018c9dsspfuh2UnHeFTE5hWQ` is disabled.
- **Codex** access to the repository is suspended by Espen for now (out of credits); don't reach it with PR comments until it is restored.
- **Espen's usage:** a weekly-limit reset was used on November 12; the allowance must last until Monday at 2 am Eastern. Keep to three working sessions, lighter models for mechanical work, and follow-ups in the session that holds the context.

## Next, in order

1. #309 approved and labeled.
2. The immigration booking (tier 3, option C's health coverage repriced in section 6, with the DEC entries above, CRT-5's re-score note, and C-6's `.github/` change to run the immigration test, also tier 3); then the reviewer's L3 re-check.
3. **Maintenance at the stage D/E boundary**, before clean power:
   - **M1, dossier tidy-up** (Most capable): out-of-date status lines in every dossier README and review file (see "Known gaps"); care's one map; transportation's `6-cost.md` refreshed to #289 and #297's figures.
   - **M2, library and housing mechanics** (Standard): `library/build_catalog.py` respects reserved ID blocks; one home for CRS R48552; catalog anchors for D and E evidence entries; `packages.py`'s stale housing label.
   - **M3, the household model rebuild, with the legacy outputs:** `models/tools/household/` from the legacy incidence model and the child-poverty microsimulation, with a model card and benchmarks (Census poverty figures, the Tax Policy Center). Move the legacy suite's reports out of `legacy/` as it replaces them. Most capable, about two or three sessions. The secure floor's 65-cent ceiling, the checkpoint's revenue options and stage G's fairness test need it. Also give INC-1 to INC-5 incidence keys (#304's open item).
4. **Settlement checkpoint memo for Espen** (end of stage E): the plan-wide gap, the revenue options the legacy work holds, and which flagships drive the cost.
5. Clean power (flagship 4).

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
| Immigration (`dossiers/immigration/`, flagship 6) | L2 | Sections 1-9, memos 1-7 and the first immigration model (`tools/immigration_model.py`), decided (`DEC-2026-11-12-07`, `-12`); milestone review: L2 pass (#303); fix steps 1-4 done (#305): about +$0.41T over FY2030-39 and +$56.5B in FY2040, or about +$0.17T and +$27.7B with option C once #307 merges; not booked | The booking, then the reviewer's L3 re-check |
| Clean power (flagship 4) | L1 | Not started | Stage E, after a slot frees |
| Work (flagship 5), democratic renewal, fair financing | L1 | Not started (stages F and G) | — |
| Rural delivery note (`dossiers/foundations/rural-delivery.md`) | — | Done (#171); applied project-wide by `DEC-2026-11-09-26` | Each dossier reads it for section 5 |

## Federal budget model (`models/tools/budget/`)

- **Done:** B1 conventions and assumptions; B2 data layer; B3 provision library; B5 viewer; B6 integration; B7 Espen's counting choices (`DEC-2026-11-08-03` to `-07`, `DEC-2026-11-12-08`). The workflow is `WORKFLOW.md` (#104).
- **B4 benchmarks:** Espen answered 0r: a light research pass on historical spend-out averages, an evidence-backed placeholder in the model, and B4 closed with PS-4b reported as not fully validated (`DEC-2026-11-12-11`, #297). `MODEL-CARD.md` lists what is validated, bounded and not yet validated.
- **Plan-wide FY2040 general-fund primary balance** (case `mixed`, after #304): about $4,230B short.
- Budget-model workers report to the lead.

## Known gaps

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
