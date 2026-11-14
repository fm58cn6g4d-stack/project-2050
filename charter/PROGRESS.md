# Project 2050: progress board

Role: the live status of the plan (`charter/PLAN.md`, section 6): who is working, what is in motion, where each dossier stands, what comes next, known gaps and open questions for Espen. Only the lead edits it, folding in the "For the board" notes from workers' PRs (`DEC-2026-11-12-03`). Status: current. It holds no history: finished work is in Git and the PRs, decisions are in `charter/decisions.md`, and rules are in `charter/STANDARDS.md`.

Updated November 14, 2026 (about 23:55 UTC) by the outgoing lead, session_01UQzgBtP7WyFvcizv9UvvFk, for the lead handoff.

## Standing sessions

| Role | Session | Title | Since |
| --- | --- | --- | --- |
| Lead | `session_01UQzgBtP7WyFvcizv9UvvFk` (handing over; the new lead adds itself) | Project 2050: lead | November 14, about 14:43 UTC |
| Reviewer | `session_01UQzgBvCR9T87TyoLdLaXdq` | Project 2050: reviewer | November 14, about 14:45 UTC; woken every three hours at :32 by the scheduled task `trig_01CDJ4kLC3BXeLKRtBxHcMit` (older reviewer tasks are disabled) |
| Strategy | `session_01UQzgBuA3EdnR7Dx4kUq1un` | Project 2050: strategy and systems | October 27 |

**Former standing sessions** (the most recent; earlier ones are in this file's Git history):
- Lead `session_01UQzgBtP7WyFvcizv9UvvFk`: the reviewer handover; the merge queue through #362, #372, #374 to #377 (clean power booked and paused: `DEC-2026-11-14-02`, `-03`, memo 8 D); the process rules `DEC-2026-11-14-04`, `-05` (#376); the stage-order line (#379) and the checkpoint-order decision (#380); the financing checkpoint memo started (#378); November 14.
- Lead `session_01UQzgBuP5ZGwT3KENpUcuNd`: the handoff and #335 merged; E-C2, the rebookings, M4 (energy and climate model, two sessions), clean power's milestone review, re-review on MOD-energy and booking at L3 (#359); Espen's decisions `DEC-2026-11-13-09` to `-15` and memo 8 D (#371); the one-at-a-time merge queue; the handoff (#373); November 13 to 14.
- Reviewer `session_01UQzgBxNwxtd5koUq9phZwU`: PRs #332 to #373, finishing with #362; November 13 to 14 (handed over at about 576,000 tokens; its task `trig_019mwEJpZ4HeKBduzE2dM1ae` is disabled).
- Lead `session_01UQzgBuU8feeYuYt6o6GeGK`: the overnight relay of November 13 (#320 to #334: M3 part 2 finished, M1, the stage E checkpoint memo, immigration's small items, option D), the decision document and Espen's November 13 round (#335, DEC-2026-11-13-04 to -08), two reviewer handovers, E-C2 and the rebookings started; November 13.
- Lead `session_01UQzgBwNea5uYV7BMBRB3Ha`: the secure floor and immigration bookings to L3 (#304, #310), Espen's decisions DEC-2026-11-12-16 to -19 and DEC-2026-11-13-01 to -02, the care base under option C (#313), the reviewer handover, M2 (#312), clean power E-C1 (#315, #317), M3 parts 1-2 (#318 to #321); November 12 to 13.
- Reviewer `session_01UQzgBx3GY2ubHn3v5pRWdb`: PRs #323 to #331; November 13 (handed over at about 586,000 tokens).
- Reviewer `session_01UQzgBw6mqUQnF5hz7WbpQH`: PRs #314 to #322; November 13 (handed over at about 712,000 tokens).
- Reviewer `session_01UQzgBxJre9xhzNQVtr5prW`: PRs #284 to #313; November 12 to 13.
- Lead `session_01UQzgBuYpTa4haagP5TUTko`: the charter audit (#290, #291), the board rewrite and restart plan, 0o/0p/0q recorded, secure floor S4 to its booking (#304), immigration I4 and its review, budget inputs #289 and #297; November 12.
- Lead `session_01UQzgBtrMsAhWpEyfRAzn6W`: the care booking and paid-leave ceiling merges (#265, #266), the process rules `DEC-2026-11-12-01` to `-05`, the budget model's B6 remainder (#272 to #282), question 0q; November 12.

## In motion

**Lead handoff (November 14, about 23:55 UTC)** from `session_01UQzgBtP7WyFvcizv9UvvFk` (context about 560,000 tokens; lineage depth 6, so Espen starts the new lead: "You are the new Project 2050 lead: follow the handoff in charter/PROGRESS.md and .claude/skills/sessions/SKILL.md."). The strategy session is at about 614,000 tokens and near its weekly limit, so it should not start the new lead.
1. **Open PRs and what each waits on:**
   - #378, the financing checkpoint memo (routine), author `session_01UQzgBx2V9SaMWW9KWZrcyX` (Most capable, about 360,000 tokens, report-back to the lead): the reviewer's requested fix (B1's federal-cost reconciliation) is made and approved at `fa48c36`; it merges on its own. Once it merges, put its seven questions to Espen (memos F1 to F3 and part B4's four points, listed in #378's "For the board"), plainly and numbered, with the recommendation for each.
   - #380, the decision row #380 adds (the checkpoint and settlement order) and the PLAN 6 stage G row (tier 3, the lead's; the new lead owns it): approved and current; waits only on Espen's label.
2. **After Espen answers the memos:** record the answers as `DEC-` rows and book them in one tier-3 PR (the employer contribution's row and HX's reduction, the states' share, the contribution rows, `scenarios.json`; #378 lists them). Then Espen's stage E boundary review, then stage F.
3. **Scheduled check-ins:** the lead's `send_later` safety net, latest `trig_01KnwzZNsbqeQpZadZY8x1s2` (about 02:52 UTC November 15). The new lead sets its own and disables any left pending (never delete). The reviewer's task is `trig_01CDJ4kLC3BXeLKRtBxHcMit` (every three hours at :32).
4. **Nothing else is in flight outside the repository.** Clean power and MOD-energy are paused (parked items below). Every finished worker is archived.

- **Where we are in the plan (`charter/PLAN.md` section 6), for every lead:** stages A to D are done, and stage E (clean power and immigration) is booked. **Stage E's last step, the financing checkpoint memo, is in progress.** Then: Espen's stage-boundary review; stage F (work, democratic renewal); then stage G, the full financing settlement. Espen, November 14: the checkpoint is "a bit of a more substantial checkpoint", aiming to settle Medicare for All's financing, "and then do a deep dive full audit settlement (some parts again) after stage F completes." So the checkpoint does not replace stage G: stage G re-audits the whole plan, including what the checkpoint settled, once stage F's costs are in. Keep this line current as the stages move.
- **Clean power and MOD-energy are wrapping up for now** (Espen, November 14: "I want to move toward wrapping up clean power and climate model for now, but ofc willing to reopen later"; only planned steps and fixes). Merged today: #362 (design test, memo 9's record, transmission evidence EV-CLP-733 to 759, CLI-10.03's siting fix), #372 (`DEC-2026-11-14-02`: all of the standard's payments are general-fund receipts, no grid account; `DEC-2026-11-14-03`: the eastern transmission corporation gets eminent domain on TVA's model), #374 (memo 8 marked decided; PR-3, the revenue convention against Treasury's). As booked: clean power about $1,730.9B over FY2030-39 and $82.0B in FY2040; **plan-wide FY2040 gap $4,162.4B short (7.68% of GDP)**.
- **Merge queue** (`DEC-2026-11-14-04`): workers push only when the lead says it is their turn. Merged since the last board update: #375 (board), #376 (`DEC-2026-11-14-04`, `-05`), #377 (memo 8 D booked as CLI-4R, about $2.6B over FY2030-39 and $1.6B in FY2040; `pricing.py`'s labels at 24.4%; clean power about $1,733.5B and $83.6B; **plan-wide FY2040 gap $4,164.0B short**). Now: #378 (memo; approved at `fa48c36`, merging), #380 (label), this handoff board PR.
- **In progress: the financing checkpoint memo** (`dossiers/foundations/checkpoint-financing.md`, first draft #325, Medicare for All side-by-side #334, #336), session `session_01UQzgBx2V9SaMWW9KWZrcyX` (Most capable, started 23:22 UTC November 14), branch `claude/financing-checkpoint`, report-back to the lead. Espen, November 14: "in the financing memo I want particular attention paid to a holistic look at making Medicare for all affordable. In theory, it should come out cheaper for the country, but that also means it needs to be affordable for the government. Ofc analyze the full set of project components planned for the financing memo, I just ideally want to solve that piece in that step if we can." So the memo covers its planned scope (the plan-wide gap, the legacy revenue options, which flagships drive the cost) and works out how national health spending now paid by households and employers becomes affordable public financing, with options and a recommendation.
- **Parked with clean power, for a later reopening:** the ranked list of new MOD-energy capabilities (Espen: "continue refining itself and building more utility by being able to analyze more aspects of climate policy"); design-test finding 6 (on the model the standard's cap could be $20 with the same carbon cut; revisit at the next model version); HI-1, the 2015-25 power history check, misses narrowly (5.7% against 5%; damped coal switching tested and not adopted), so MOD-energy stays "working"; CLI-10.03's reach to state-owned land (*United States v. Carmack*) is marked "to confirm in drafting"; Espen's question on the eastern corporation is decided (`-03`). A snapshot page of MOD-energy's predictions: https://claude.ai/artifact/HtUiL7sspMPqMT8oG33DYp (not a source of record).
- **Workers (report to the lead):** the financing checkpoint session above. Reviewer: see Standing sessions. Every finished session through #377 is archived (November 14).
- **Gate note (Espen, November 14):** a `changes-requested` verdict is cleared only by a later approval under the same `Reviewer:` ID; at a reviewer handover the new reviewer may copy the old ID (`DEC-2026-11-14-05`). A routine PR can also sit "ready, merging now" while main moves; a branch update un-sticks it.
- **Waiting on Espen:** #380's label. Then the checkpoint memo's seven questions, from #378's corrected text, once it merges. Small open item: tighten the CLI-4R test to assert the ledger's booked $3.0B sum at its next touch (#377's reviewer).
- **The decision document** (a Claude Doc; doc id 881ecff6-a8f3-448b-89c5-ed3312e423ce; artifact https://claude.ai/artifact/HouYTVFgnhsepKsZzoopxD; body node 83add86c-21a5): items 1-30, all answered. Espen comments there, and the lead answers in the doc's own threads with the Claude Docs connector.
- **Small items for later:** `immigration_booking.py`'s non-JSON printout fails with `KeyError: 'CAP-7S'` on main (`--json` and the tests are fine); `agenda/agenda.csv`'s INC-4 title and `dossiers/secure-floor/3-design.md` point 7 still describe INC-4's old scope (`DEC-2026-11-13-04`); a guard in `library/build_catalog.py` against shallow-clone rewrites of catalog-facts.csv; the secure floor README rows 1-2; HOU-1 to HOU-3; E-Verify's funds line; M3's later items; the legacy-move tier-3 cleanups; DEC-06's "except 14" means the decision document's item 14 (memo 7), to clarify at a later `charter/decisions.md` touch.
- **Lead check-in:** a `send_later` safety net every three hours (latest `trig_016uXBS17jBCeWSrnBfEerwe`, about 23:50 UTC November 14); each check-in sets the next.
- **Codex** stays suspended. **Espen's usage:** keep to three working sessions, efficient briefs.

## Next, in order

1. **Clean power** is booked and paused at L3 (#359, #372, #377), to reopen later (parked items in In motion).
2. **The settlement checkpoint memo** (item 4, in progress), with Espen's Medicare for All affordability direction (In motion); then Espen's options, then Espen's stage E boundary review, then stage F.
3. **Maintenance, later:**
   - **M1** done (#326, follow-up #329; the secure floor's lines after D in #333; the "crs r44593" two homes in #338). Left: HOU-1, HOU-2 and HOU-3 are parent rows with no provisions of their own, left at L2 (#329), for the lead to settle with their children.
   - **M3, the household model:** parts 1-2 done (#318 to #322, #327). Left for a later Most capable session: replicate-weight intervals; the CBO-convention check; moving the budget model's readers to the measured keys; the model card's note that the fixture's exact reproduction holds as of `e897ac6`. INC-4 is rebooked at about $0.5B a year on the household model's measure (#339, `DEC-2026-11-13-04`).
   - **Immigration:** the review's small items done (#328). Left: E-Verify's Social Security funds line (about −$42B over FY2030-39), written up in #328's "For the board" for a tier-3 change to the funds model; memo 6's health factor is rebooked at 0.67 (#339, `DEC-2026-11-13-05`). The vote model's two-bill split stays paused with vote modeling (`charter/PLAN.md` 5).
4. **Settlement checkpoint memo for Espen** at the end of stage E (first draft merged, #325, `dossiers/foundations/checkpoint-financing.md`; clean power is booked): the plan-wide gap, the revenue options the legacy work holds, and which flagships drive the cost.

**The financing settlement** (stage G, `charter/PLAN.md` section 6): after stage F completes, a deep-dive full audit of the whole plan's financing, re-checking what the stage E checkpoint settled (Espen, November 14); once the first wave's designs are specified; re-run as later waves add cost, at each new CBO baseline, and before 2028.

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
| Clean power (`dossiers/clean-power/`, flagship 4) | L3 (booked) | Sections 1-9 and memos 1-9, decided (#335; `DEC-2026-11-13-10` to `-14`; `DEC-2026-11-14-01` to `-03`); milestone review and fixes (#344, #346); re-review on MOD-energy (#349, #351, #354); booked (#359, #372): about $1,730.9B over FY2030-39 and $82.0B in FY2040 | The wrap-up PR (memo 8 D's booking); then paused (parked items in In motion) |
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
