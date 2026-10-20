# Project 2050: standing instructions for Claude (and any other model)

Read this first, every session. Updated Oct 20, 2026, when the project moved from the claude.ai Project into this repo.

## What this is
Project 2050 designs a coherent, internally consistent set of policy options for a 2029-30 Democratic trifecta and the decades after. The owner is Espen Swanson. Espen is not a programmer: write in plain language, run commands yourself rather than asking Espen to, and report briefly (what you did, what you found, what needs Espen's decision).

## Where things live
- **This repo is the working home of the files.** Folder = role (authority descending; a higher role overrides a lower one):
  1. `governing/` — `project-2050-governing-decisions.md` (the decisions and design rules) and the decision briefs. The live Claude Doc version of the governing doc (https://claude.ai/code/artifact/817382ad-9f54-4875-b887-3eb601724c40) wins if they differ; keep the repo copy in sync with it.
  2. `domains/` — one canonical file per domain, each with stable IDs: domain-revenue (REV-), -health (HLT-), -family (FAM-), -social-security (SS-), -democracy (DEM-), -courts (CRT-), -executive-power (EXE-), -integrity (INT-), -capacity (CAP-), -climate (CLI-), -housing (HOU-), -labor (LAB-), -competition (COM-), -immigration (IMM-), -rights (RTS-), -public-safety (SAF-), -ai (AI-), -national-security (NSC-), -amendments (AMD-), -education (EDU-). Canonical until converted: `transportation-moving-america-act-2031-draft-2.md` (MOV-); its model scripts are in `index/tools/transportation/` and its source docs (ARCA, ATRA, the section-by-section, the calendar decision, session status) are `sources/transportation-*`. `public-safety-safe-everywhere.md` is the evidence base behind domain-public-safety, not canonical. Where a file predates a decision, the decision wins.
  3. `index/` — generated files (the master ledger, the household incidence model, the long-term fiscal model, `index/data/`). **Never hand-edit them; regenerate** with `bash index/tools/run-all.sh` (dry run with a diff) and `--write` to update. Hand-written exceptions: `index/options-register.md` (every option once, with exclusive groups and overlaps — check it before proposing or summing options) and `index/revenue-assignment-audit.md`.
  4. `frameworks/` — reasoning only, not current policy (radical-means-moderate-ends, instruments-and-consequences, the Talarico stress test).
  5. `staging/` — the old reform inventory; rows are pointers to domain files now.
  6. `archive/` — ideas only, never current sources. Four large archive files (the superseded Beyond Health Care agenda and three war-game HTML pages) were not copied from the claude.ai Project; they are ideas only.
  7. `sources/` — outside inputs and source tables behind the domain files.
- **Live pages on claude.ai** (edit through Claude on claude.ai, not from here): the governing doc above; Decision Brief 1 (https://claude.ai/artifact/STTq2kjhUfzJUYJUy8VafV); "Senate Rules Reform: Options" (https://claude.ai/code/artifact/0f226c46-5ce8-4bec-9a54-c5fd7e7a5629); the ledger dashboard (https://claude.ai/artifact/RDuHM7DqCwvLUtVaB4ANMs).
- **The claude.ai Project "Project 2050"** holds a copy of these files from before the move. Don't let the two drift: after a session that changes files here, either push the changed files to the Project too or say plainly that the Project is now behind.

## Current decisions (Oct 20, 2026; the governing doc has the full text)
- **D1 Scenario:** plan for 52-54 Senate seats; 56+ is upside. Democratic president Jan 2029 to at least Jan 2037; Democratic Senate through 2036 if 52+ after 2026; House possibly lost in 2030, regained 2033-36 if DEM-1 is in force before the 2031 redistricting. DEM-1 must pass by mid-2030 (DEM-1F adopted: after R1, by spring 2030). DEM-3, DEM-4, DEM-9 move together to 2033 with a one-off 2034 redraw. Must pass in the first trifecta: HLT-3, CLI-6/CLI-7, IMM-1, AI-1/AI-4. The 2026-28 permitting deal is stipulated as enacted. Tag every item for survival at 51: ✔ survives (reconciliation, state, executive, House-only); ◐ needs a D2 majority-precedent path; ✖ needs 60, 67 or Republican votes.
- **D2 Senate rules: DECIDED** — F (graduated cloture: 60, 57, 54, then a majority, about a day apart) with guaranteed minority amendments and equal time, adopted week one of 2029; C (talking filibuster, 15-day backstop) is the opening offer; G (democracy carve-out) the written fallback. Reconciliation as now.
- **D3 Taxes:** no $400K pledge. Every income group below the top comes out ahead on net from combined taxes, fees and benefits; new general-fund revenue mostly from the top 1% and corporations. Middle-reaching options are checked in the incidence model before they are final.
- **D4 Fiscal rule:** permanent programs fully paid for over ten years; Social Security, Medicare HI and the Highway Trust Fund kept whole (75-year window for the social-insurance funds); no new trust fund just to hold a pay-for; borrowing only for time-limited capital (incl. Moving America's capital lines and time-limited climate capital); Byrd rule unchanged. **A broader loosening toward a long-term fiscal-arc rule is directed; options D4-B and D4-C are in the governing doc, parameters pending.** The long-term model (`index/fiscal-long-term-model.md`) finds D4-B's total-debt guardrails fail in every scenario, so they must be restated relative to the baseline or paired with a sustainability layer of about 1.5-2% of GDP.
- **D5:** three reconciliation vehicles, R1 FY2029, R2 FY2030, R3 FY2031. Social Security and rules-only items go to the regular floor.
- **D6:** the go-big health bill is canonical; the Medicare buy-in is a separately scored add-on; dental is scored separately but kept in.
- **D7 Carbon:** gasoline and diesel taxed only through Moving America's fuel-tax steps; economy-wide fee and dividend for the rest: REV-C1 $25/t in 2030 rising to ~$100 by 2037 (~$1.35T), border adjustment REV-C2 (~$0.20T); ~80% rebated.
- **D8 Social Security:** solvency first with a targeted increase, regular-order bill in spring 2030; closes ~65-72% of the 4.42% gap after the avoidance haircut (86-92% with SS-5, the recommended closer, not yet chosen).
- **D9 Discretionary:** a direction, not a cap: ~$0.6T agency-rebuild line (CAP-7), roughly flat real defense (NSC-1 base open).

**State (regenerate rather than quote if a domain file changed):** general-fund claims ~$10.48T against a $6.37T base, a $4.11T gap; ~$1.46T on the planning basis (Package B: C18, C35, C19b, C20, plus borrowing readings C21, C30, C31, C32, C37); ~−$0.12T with the sprint package C38 and the program trims; 170 Senate floor days under F against 163.

## Design rules
Reciprocity (only rules we'd accept in the minority). Durable instruments: mandatory spending, auto-enrollment, statute, no sunsets on permanent programs; a trust fund only where a permanent benefit has a natural revenue stream. Legibility. Pairing structural reform with material benefits. Supply with demand. Capacity first. Write for this Court. One version per policy. Every number has a basis. Payments do not stop: every recurring payment carries standing disbursement authority that survives a shutdown.

## Working rules
- Propose changes as options with their effects; don't silently rewrite a canonical file. Decisions are Espen's.
- A second version of a policy gets flagged and folded into its domain file as an option.
- Tag every number as sourced, scaled, estimated or proposal, with its window (default ten years, 2030-39, in trillions).
- Look up anything that describes the world now before stating it.
- Name policies by their domain-file IDs.
- After a domain file changes a number, update the script tables in `index/tools/` (ledger-build.py, incidence-model.py, fiscal-profiles.py as relevant) and regenerate; never edit generated files by hand.
- Filing: new docs go straight into their role folder, lowercase kebab-case, domain first.

## Tools
`index/tools/readme.md` explains each script. Quick version:
- `bash index/tools/run-all.sh` — rebuild everything in `build/` and diff against `index/`; `--write` to update; `--fetch` to re-download CBO's data (github.com/US-CBO/cbo-data).
- Ledger tables (bills, revenue, options, conflicts, dynamic sensitivity) live in `ledger-build.py`; incidence rows in `incidence-model.py` (hand-keyed — check against `build/ledger.json`); long-term year profiles in `fiscal-profiles.py`; fiscal scenarios in `fiscal-model.py`.
- Transportation model: `index/tools/transportation/` (run `final_v3.py`; see its readme). Not part of run-all.sh; MOV- and MR rows in ledger-build.py are keyed by hand from Draft 2.
- Sprint revenue rows use the prefix TS (TS1-TS12, TSX) so the old tariff row T1 keeps its ID; high-pay options are HP1-HP3.

## Git
Commit with a short plain message describing what changed and why. Don't rewrite history. Work on a branch for anything large and say so.

## Open queue (Oct 20)
1. Decision Brief 2: program trims and scope (C5, C17, C33, C34, C36, LAB-9, CAP-7, NSC-1), the D4 choice (relative guardrails vs. a sustainability layer; envelope 0.25/0.5/0.75% of GDP; Judgment Fund contingent liabilities), and alternatives (REV-TS12, SC1, REV-HP1-HP3).
2. Fresh post-2025-law scores for REV-TS1-TS3 and a joint TS1/G1 score.
3. A 75-year Social Security trust-fund module (D8, SS-5) and the SS-10 67-vote comparison.
4. D1 re-baseline after the Nov 3 election.
5. Revenue strategy session on payroll raisers (EDU-9B note); a fiscal tab on the dashboard; non-tax high-pay companions in domain-competition.md; a synthesis plan document.
