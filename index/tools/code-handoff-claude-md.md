# Project 2050: standing instructions for Claude Code

Read this first, every session. Written in chat on Oct 19, 2026, from the live Governing Decisions doc (rev 113).

## Who you work for
Espen Swanson. Not a programmer. Write in plain language. Run commands yourself rather than asking them to. Report in 10 lines or fewer: what you did, what you found, what needs their decision.

## What Code is for here
Mechanical, computational and file-heavy jobs on the Project 2050 files: parsing, checking, regenerating, modeling. Policy judgment stays in chat. When a job needs a judgment call (which of two numbers is right, whether to depart from a decision), stop and write it up as options with their effects. Do not decide.

## Where the files are
The Project "Project 2050" on claude.ai. If this session has the Projects tool (project_info, project_read, project_write), use it. project_read writes large files to a local path; read them from there. Mirror the project's folders in ./project-2050/ so paths match. Folder = role: governing/, domains/, index/, sources/, frameworks/, staging/, archive/.
Do not open archive/ (ideas only; large war-game HTML and JSX).

## Authority (higher overrides lower)
1. governing/project-2050-governing-decisions.md. The live Claude Doc wins if they differ and you can read it: https://claude.ai/code/artifact/817382ad-9f54-4875-b887-3eb601724c40
2. domains/ canonical files: domain-revenue, -health, -family, -social-security, -democracy, -courts, -executive-power, -integrity, -capacity; transportation-moving-america-act-2031-draft-2.md and public-safety-safe-everywhere.md until converted. Source tables behind them: sources/health-go-big-bill-detail-and-financing.md, sources/revenue-channels-and-full-menu.md. Where a file predates a decision, the decision wins.
3. index/: generated files. Never hand-edit; regenerate.
4. frameworks/: reasoning only.
5. staging/unified-reform-inventory-current.md: domains without a file yet.
6. archive/ ideas- and wargame- files: never current sources.
7. sources/ outside inputs.
8. archive/superseded-: ignore.

## Decisions in force (Oct 19, 2026)
- D1 Plan for 52-54 Senate seats; 56+ is upside. Every item gets a survival tag at 51: ✔ survives (reconciliation, state, executive, House-only); ◐ needs a D2 majority-precedent path; ✖ needs 60, 67 or Republican votes. Democratic president Jan 2029 to at least Jan 2037; House possibly lost in 2030; electoral and civil-rights package must pass by mid-2030; House size (DEM10) and STV (DEM11) move to 2033 with a one-off 2034 redraw; no 2033 queue for anything else. The 2026-28 permitting deal is stipulated as enacted.
- D2 Senate rules: OPEN. Modeling basis: F (graduated cloture) primary, C alternate, G failure case, E upper bound.
- D3 No $400K pledge. Test: every income group below the top comes out ahead on net from combined taxes, fees and benefits; new general-fund revenue comes mostly from the top 1% and corporations. Needs an incidence model.
- D4 Permanent programs fully paid for over ten years from any source. Dedicated funds (Social Security, Medicare HI, Highway Trust Fund) kept whole, read on a 75-year window for the social-insurance funds. Borrowing only for time-limited capital (Moving America's renewal top-ups and capital lines count, ~$0.30T). Byrd rule unchanged.
- D5 Three reconciliation vehicles: R1 FY2029, R2 FY2030, R3 FY2031. R1 moves to R2 if the slot is lost. Social Security and rules-only items go to the regular floor.
- D6 Go-big health bill canonical; Medicare buy-in (60 or 55) is a separately scored add-on; dental scored separately but kept in.
- D7 Gasoline and diesel taxed only through Moving America's fuel-tax steps. Economy-wide fee and dividend covers the rest: $1.35-1.6T gross = REV-C1 $1.20-1.35T plus REV-C2 $0.15-0.25T; about 80% of REV-C1 rebated, 20% to transition.
- D8 Social Security: solvency first, targeted increase, regular-order bill in spring 2030. Closes about 65-72% of the 4.42% gap after the 15% avoidance haircut (70-77% before it); 86-92% with SS-5, the recommended closer (closer still to choose).
- D9 Direction, not a cap: about $0.6T agency-rebuild line, roughly flat real defense, both provisional.

## Design rules
Reciprocity. Durable instruments (mandatory spending, auto-enrollment, statute, no sunsets on permanent programs; a trust fund only with a natural revenue stream). Legibility. Pairing structural reform with material benefits. Supply with demand. Capacity first. Write for this Court. One version per policy. Every number has a basis.

## Working rules
- Propose changes as options with their effects; never silently rewrite a canonical file.
- A second version of a policy gets flagged and folded into the domain file as an option.
- Tag every number sourced, scaled or estimated, with its window (default ten years, 2030-39, trillions).
- Name policies by domain-file IDs (REV-, HLT-, FAM-, SS-, CAP-, CRT- and so on).
- Look up anything that describes the world now before stating it.

## Guardrails for Code
- READ-ONLY: governing/, domains/, sources/, frameworks/, staging/, archive/. Never edit or push to them. Problems go in a report: file, line, what is wrong, proposed fix as an option.
- WRITABLE: index/tools/ (scripts, reports, code-log.md). The generated ledger (index/2029-trifecta-master-ledger.md) only by running the generator, only after you have shown what will change and Espen says go.
- Do not change numbers inside the script tables (ledger-build.py) to match a domain file. Produce a difference table and ask.
- One job at a time. No parallel subagents. Estimate before any long run. Stop at the end of each job and wait for a go.
- Before pushing a file that already exists in the project, re-read it and confirm it has not changed since you pulled it. If it has, stop and say so.
- End of every session: append an entry to index/tools/code-log.md (date, what ran, what changed, open flags, how to rerun), push changed files with project_write using local_path, and list exactly what was pushed.

## Jobs, in order
**Job 0, setup and reproduce.** Pull the files. Copy index/tools/*.py to a work folder, renaming incidence-model.py to incidence.py and incidence-years.py to years.py (the scripts import each other under those names; do not edit the originals). Run the readme's five steps. Confirm the saved state reproduces: base $6.37T, general-fund gap $3.69T, about $0.05T after every option. Report any mismatch.

**Job 1, linter** (index/tools/lint-project.py, output index/tools/lint-report.md, sorted by severity). Checks:
- every figure in domains/ carries a basis tag and window; flag candidates, since a heuristic will be noisy
- every item carries a survival tag
- IDs are unique, follow domain-first naming, and every cited ID exists; no old democracy IDs D0-D13
- stale phrases: "2033 queue", the $400K pledge as binding, G4 in the base, Medicare at 60 in the base package, claude/ paths, Beyond Health Care cited as current, "70-77%" outside a before-haircut context
- a policy defined twice, or near-duplicate titles across files
- file names kebab-case, files in the right role folder
- headline numbers ($10.06T claims, $6.37T base, $3.69T gap, 166/163 floor days, D7 split, D8 percentages) match the generated ledger everywhere they appear
- arithmetic: base rows sum to 5.71 / 6.37 / 7.12; REV-C1 plus REV-C2 equals D7's range; the D8 package sums to its stated share of 4.42%; channel totals tie to the register

**Job 2, reconcile.** For every register and revenue row in ledger-build.py, compare its number, basis and window with the matching domain-file row. Output a difference table. Change nothing.

**Job 3, one-command rebuild.** A single run-all script that does the readme's five steps in a work folder, writes the new ledger to a staging path, and diffs it against the current ledger. Make incidence read its totals from ledger.json instead of hand-keyed ROWS, or at least check ROWS against ledger.json and warn. Show the diff before anything is pushed to index/.

**Job 4, incidence v2. Ask first; this is the expensive one.** Add D3's pass/fail to the output: Q1-Q4 each positive on net at 2034 and 2039, and top 1% plus corporations bearing more than half of new general-fund revenue. Show the fourth quintile's sensitivity to the open levers (C19 exclusion cap, C20 surtax, dividend share above 80%). Keep every distribution key labeled as an estimate with its source pattern.

## Known issues found Oct 19 (do not rediscover; report them as lint findings)
1. The generated ledger is internally inconsistent on D8: the changes table says 65-72% but the channels table, F5 note and one conflicts row still say 70-77%. The figures live in ledger-build.py (F5 note, CONFLICTS) and ledger-make-md.py.
2. The incidence scripts hand-import the ledger's totals, and the two incidence files import each other under working names.
3. The saved project instructions are stale against the live doc: they omit D4's two readings and give D8 as 70-77%. Espen's housekeeping item, not yours.
4. D9: the project copy of the governing doc extends the agency list (CMS, OPM, EAC, FEC, integrity units); the live doc (rev 113) still lists nine agencies. Ledger A1 lists nine. Flag, do not resolve.
