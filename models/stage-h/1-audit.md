# Stage H, step 1: the toolkit and front door audit and plan

Role: the first step of stage H, "Release the core models as a professional toolkit, and rebuild the illustrated vision" (`charter/PLAN.md` section 6; the toolkit standard in 3.4; the front door in 3.5). Part 1 scores every core model against the toolkit standard, part 2 audits the public front door, and part 3 proposes the rest of stage H. The decision memos for Espen are in `memos/` (H1 to H5; memo numbers are not step numbers) (index: `memos/README.md`). Status: **audit, November 25, 2026; read-only.** A first deliverable, the front door's outline, is `2-front-door-outline.md`; part 3.5 records what a professional-practice review changed. It changes no model, input or public page and decides nothing. Settled and not reopened here: the flagship list (`DEC-2026-11-20-03`, `DEC-2026-11-24-11`), stage G's close (`DEC-2026-11-24-10`), and the rule that the toolkit never claims official scores (PLAN 3.4). The fiscal path's revision (G15's redraft, G19's re-check, CLI-1's cost tail; `DEC-2026-11-25-01` to `-11` (batch 3, #487)) is a separate step; this file touches nothing in `dossiers/foundations/fair-financing/` or the fiscal scripts.

How it was done: a rerun of `bash models/tools/run-all.sh` on main at `f303483` (after #486), each model's own entry point and tests run on their own, and three Standard-tier helper audits (household, health and budget; energy, immigration, transportation and housing; the loose scripts) whose findings were spot-checked against the files. Scores: **Present** (meets the part), **Partial** (some of it), **Missing**. Gap sizes: **small** (under an hour), **medium** (about a session), **large** (more than a session).

## In plain terms

1. **Everything runs.** `run-all.sh` finishes cleanly and reproduces every committed output exactly; each model's own tests pass. One side check fails: the climate portfolio's international report still names its pre-reset path (part 1.8).
2. **Three models are close to the standard** (household, health coverage, energy and climate): each has a model card, benchmarks, tests and one command. What they lack is mostly bookkeeping: an up-to-date, machine-written run log and a few card details.
3. **The federal budget model is the biggest gap that matters.** It has strong benchmarks and tests, but no single command of its own (it runs only inside `run-all.sh`), no evidence map, no named owner and no run log. Its code is spread across about a dozen loose scripts tangled with the dossiers' booking scripts.
4. **Immigration and transportation work but have no model cards or run logs**, and **there is no housing model at all.**
5. **Nothing in the repository says how it may be reused:** there is no license file. That and "what released means" are Espen's choices (memos H1 and H2).
6. **The front door is a month out of date.** It is pinned to October 25 evidence, cites the old domain files rather than the dossiers, shows a public option where the plan now has a single health plan, has no immigration scene, and says no financing plan has been chosen, although the settlement is booked. It can't even be rebuilt from a normal clone, because its pinned commit is no longer fetched. It needs rebuilding from the dossiers' public cases (section 9), not patching.
7. **The proposed stage H is eleven steps** (one a small tier-3 license PR), toolkit first, with the front door's content work able to start in parallel and its visual design done in Figma. That is above PLAN's 5-8 sessions; part 3 says where it could shrink.

## Part 1. The toolkit audit

### 1.1 Scorecard

| Core model | Card | Benchmarks | Interface | Tests | Run log | Overall |
| --- | --- | --- | --- | --- | --- | --- |
| Household (`MOD-household`) | Present | Present | Partial | Present | Partial | Near the standard |
| Health coverage (`MOD-health-coverage`) | Present | Partial | Present | Present | Partial | Near the standard |
| Federal budget (no MOD- ID) | Partial | Present | Partial | Present | Missing | Largest gap among the models in use |
| Energy and climate (`MOD-energy`) | Present | Present | Partial | Present | Present | Nearest the standard |
| Housing | Missing | Missing | Missing | Missing | Missing | No model exists |
| Immigration (first version) | Partial | Partial | Partial | Partial | Missing | A dossier tool, not yet a model |
| Transportation (Moving America) | Partial | Partial | Present | Present | Missing | Works; undocumented as a model |

**Across all models:**
- **No license** at the root or in any model folder (memo H2).
- **No dependency manifest**, but none is needed beyond the interpreter: every model is Python standard library only, plus Node.js (no packages) for the carbon engine.
- **No version numbers** except health coverage's `VERSION = '0.1.0'` (`models/tools/health-coverage/model.py:17`); no changelog anywhere.
- **No register of model IDs.** `MOD-household`, `MOD-energy` and `MOD-health-coverage` are self-declared in their cards; PLAN section 4 gives `MOD-household` and `RUN-household-2026-11-02-a` only as examples, and `models/registry/check.py` checks no `MOD-` or `RUN-` IDs.
- **Owners are session labels** ("Claude Code (the M3 worker sessions)"), not a role a reader can contact.

### 1.2 Household model (`models/tools/household/`)

| Part | Score | Evidence | Gap | Size |
| --- | --- | --- | --- | --- |
| Model card | Present | `MODEL-CARD.md`: status **working** and owner (line 3); "What it answers, and what it cannot"; data; assumptions A-1 to A-10 with basis and range; rules modeled; limits; status and next steps | The evidence map is prose (EV-/SRC- IDs and P.L. 119-21 sections in the data and rules sections), not an input-by-input table like health coverage's `inputs.csv`; the research basis for each mechanism is thin | small |
| Benchmarks | Present | The card's benchmarks table: Census P60-290 (SRC-3602), TPC T26-0045, CBO 61911, IRS SOI, the Census tax model, each with a cause; JCT marked "not used" with a reason; `results.md` sections 9-10 (intervals, the CBO-convention check) | IRS SOI is cited, not run (its `.xls` can't be read by `fetch_public.py`); TPC's 1.5-3.7-point rate gaps are explained, not closed | small |
| Interface | Partial | `python3 models/tools/household/run.py --ledger build/ledger.json --out DIR`; the CPS extract is committed in `models/data/household/` | Needs `build/ledger.json` from `run-all.sh`, so it does not run from a clean checkout; no input/output schema beyond the card | small to medium |
| Tests | Present | `test_household.py`: 32 tests (hand-checked taxes, the SPM identity against Census's published rates, household accounting, typical families, replicate weights, the CBO convention) | The legacy-reproduction test is skipped (its fixture is from `e897ac6`) | small |
| Run log | Partial | The card's run-log table, `RUN-household-2026-11-13-a` to `RUN-household-2026-11-16-g`, each with version, inputs and provisions | Hand-written and stops at November 16, although the D3 report has been rerun since (the settlement, #480); `results.json` carries no commit or input hash | medium |

- **Ran:** `run.py` in 29 s, `results.json` identical to the committed copy; `test_household.py` OK (32 tests, 1 skipped).
- **`models/tools/child-poverty/`** is the older child-poverty microsimulation that the household model partly replaces; its agenda cases are on the household card's "still to do" list. Its own validation (`run_validation.py`, 117 tests, run by `run-checks.sh`) passes, but **it rewrites tracked files** in `child-poverty/diagnostics/` each time it runs. The released toolkit either folds the remaining agenda cases into the household model and retires it, or writes those diagnostics to `build/`.
- The budget model's readers still use the legacy typed keys (`incidence.json`), not the household model's measured keys (board, small items: M3's fourth item).

### 1.3 Health coverage model (`models/tools/health-coverage/`)

| Part | Score | Evidence | Gap | Size |
| --- | --- | --- | --- | --- |
| Model card | Present | `MODEL-CARD.md`: status **exploratory**, owner (line 3); answers and can't; evidence map; mechanisms and research basis; judgment calls; limits. `inputs.csv`: 181 inputs, 103 traced to evidence and 78 labeled assumptions with low and high values | "Evidence still needed" lists untraced inputs (ACA percentage tables, Part B/D premiums, MEPS); "First version, 2026-11-10" and "exploratory" undersell a model flagship 2 now rests on, or the status is right and the dossier leans on it harder than it should: the card's next edit says which | small |
| Benchmarks | Partial | BM-1a to BM-6b against CBO, Urban and RAND, with "Differences explained" | 3 of 9 miss (BM-1a, BM-1b, BM-3b: restoration's federal cost runs above CBO's); BM-2 and BM-3a are in-sample by construction; BM-5's target is marked "unverified"; no JCT, SSA or TPC comparison | medium |
| Interface | Present | `python3 models/tools/health-coverage/model.py [--out DIR]`; `inputs.csv`, `scenarios.csv` in; `results.json`, `results.md` out; standalone | No column schema for the CSVs | small |
| Tests | Present | `test_model.py`: 23 tests (identities, boundaries, benchmarks, drift against committed results) | — | — |
| Run log | Partial | `results.json`'s `run_log`: `model_version` 0.1.0, 12-character hashes of `inputs.csv` and `scenarios.csv`, `as_of` 2026-11-10 | No git commit; nothing links a dossier figure to the run it came from | small to medium |

- **Ran:** `model.py --out` ("13 scenarios, 6/9 benchmarks pass"), results byte-identical; `test_model.py` OK.
- **Not part of the model:** `models/tools/health/decision_analysis.py` (a bounded decision check; its 9 tests pass in `run-checks.sh`), and the loose `health_booking.py`, `health_cost_review.py`, `health_financing.py` (part 1.9).

### 1.4 Federal budget model (`models/tools/budget/` and the loose scripts)

The model, per `MODEL-CARD.md` "What the model is", is `budget/` (data layer, provision library, benchmarks, viewer) plus `fiscal-model.py`, `fiscal-data.py`, `fiscal-profiles.py`, `funds-model.py`, `inputs.py`, `scenarios.py` and `ledger-build.py`. `recovery-budget/` is a separate exploratory total-budget model that imports the settlement's booking script.

| Part | Score | Evidence | Gap | Size |
| --- | --- | --- | --- | --- |
| Model card | Partial | `MODEL-CARD.md`: what it is, what it is for and not for, known limits and errors, an inputs table; assumptions in `models/data/budget/assumptions.csv` (18 `ASM-` rows with source and who decided) | **No evidence map**: the card has no `EV-` IDs and its `SRC-` IDs sit only in `test_benchmarks.py` and `benchmarks.md`. **No owner**: the inputs table still says "Codex maintains the fiscal model today; PR #106 proposes moving it to Claude", although Claude has led it since `DEC-2026-11-08-02`. Status reads "current", not exploratory, working or released. No `MOD-` ID. Mechanisms are only in `CONVENTIONS.md` | medium |
| Benchmarks | Present | `benchmarks.md` and `.json`: 20 benchmarks (18 pass, 1 bounded, 1 fail) against CBO's baseline, JCT, CBO's rules of thumb, the Trustees and SSA's actuaries; B4 closed with PS-4b reported as not fully validated (`DEC-2026-11-12-11`) | PS-4b fails, PS-4a is bounded (+18 points); some are in-sample; no Treasury comparison (`models/tools/treasury-data/` was blocked by HTTP 403) | small to medium |
| Interface | Partial | Its only one-command form is `bash models/tools/run-all.sh`, which rebuilds the whole suite into `build/`; pieces take arguments (`fiscal-model.py --baseline`, `fiscal-data.py --cache --out`) | No standalone entry point; `fiscal-model.py` writes beside itself, so it runs only from a copy in `build/`; scenarios and outputs are described only in `models/tools/readme.md` and the card | large |
| Tests | Present | `test_data.py` (the baseline rebuilt cell for cell), `test_provisions.py` (the library equals `fiscal-model.py` row by row), `test_benchmarks.py` (identities ID-1 to ID-5 to 1e-6 $B, published scores, trust funds), `test_fiscal_components.py`, `test_ledger_rounding.py`, `test_funds_model.py` | They need `build/` from a run-all | small |
| Run log | Missing | — | Nothing links a published figure (a booking, the settlement's 117.8%) to a model version, inputs and provision versions; `provisions.csv` has no version stamp; the drift check in `run-checks.sh` only compares regenerated outputs with committed ones | medium |

- **Ran:** `test_data.py` OK, `test_provisions.py` OK, `recovery-budget/test_model.py` OK (18 tests), all inside the rerun of `run-all.sh`.
- **The release boundary is not clean.** `recovery-budget/model.py` imports `settlement_booking.py`, which imports `care_booking.py`, `health_booking.py` and `financing-protection/packages.py`; `household/` imports `health_cost_review.py`, `health_financing.py` and `health_booking.py`. The released budget model has to load the plan's bookings as data (the ledger and provision tables it already reads), not import the scripts that wrote them.
- **Timing.** Stage G step 9, now running, revises the fiscal path in `dossiers/foundations/fair-financing/` and the fiscal scripts (`fiscal_path.py`, `fiscal_dynamic.py`, CLI-1's cost tail), then brings Espen batch 4 (the redrafted G15 and G19's mix). The budget model's release step (part 3, H4) builds on step 9's merged changes and writes none of those files before then.

### 1.5 Energy and climate model (`models/tools/energy/`, with `carbon/` and `climate-portfolio/`)

One model and two older relatives, not three peers. `energy/` is `MOD-energy`; its `engine/cfd-model.js` is a modified copy of `carbon/cfd-model.js` (Espen's Carbon Dividend Model, v3.4). `carbon/` with `carbon-model.py` is the older run that still feeds the ledger (run-all step 6b), and `climate-portfolio/` is a research driver on the carbon engine (the 13,824-package search) that reads `build/carbon-config.json`. `climate-integration.py` and its report read the portfolio's export, guarded by a SHA-256 pin in `models/data/inputs/climate-adoption.json`. The energy card says the carbon run and the portfolio have not moved onto `energy/`.

| Part | Score | Evidence | Gap | Size |
| --- | --- | --- | --- | --- |
| Model card | Present | `energy/MODEL-CARD.md`: status **working**, owner, answers and can't, evidence map (CLI- and REV- IDs; labeled assumptions with ranges in `assumptions.csv`), mechanisms and basis, limits | `carbon/` and `climate-portfolio/` have READMEs, not cards (no status, owner or can't-answer) | small |
| Benchmarks | Present | The card and `results.md`: EIA, CBO, EPS, Treasury, EMF 37, with reasons for each difference; in this run DA-1, DA-2, BL-1 to 3, PR-1, BI-1, BK-1, BK-2, DI-1 pass | PR-2 and HI-1 fail (HI-1 by 5.7% against 5%, parked with clean power, board "In motion") | small to medium |
| Interface | Partial | `python3 models/tools/energy/run.py [--out DIR]`, standalone (Node.js, no packages); `menu.py` and `results.json` document provisions by fiscal year | The portfolio and `carbon-model.py` need `run-all.sh` first; two copies of the engine to keep in step | medium |
| Tests | Present | `energy/test_energy.py`; both engines' `cfd-tests.js` (53 checks in `carbon/`); `climate-portfolio/test_portfolio.py`, `test_packages.py`, `test_international.py`; `test_climate_integration.py` | `test_international.py` fails (below) | small |
| Run log | Present | `results.md` and `results.json` record a hash of every input file; the card has a run-log section | Hashes but no git commit or model version; the portfolio's and carbon run's outputs carry none | small |

- **Ran:** `test_energy.py` all passed; `run.py --out` byte-identical to the committed `results.json`; both `cfd-tests.js` pass; `test_portfolio.py` and `test_packages.py` pass.
- **Fails: `python3 models/tools/climate-portfolio/test_international.py`** ("committed report matches the build"). `legacy/sources/climate-portfolio-international-pricing.md` line 3 still says it was generated by `index/tools/climate-portfolio/international.py`; the build now writes `models/tools/...`. A stale generated file from the October 28 move, not a model error. Neither `run-all.sh` nor `run-checks.sh` runs this test, which is why it went unnoticed. Fix: regenerate the file and add the test to `run-checks.sh` (H2).

### 1.6 Housing model

**Missing.** No `MOD-housing`, no code in `models/tools/` and no `dossiers/home/tools/`. (`dossiers/scenario/tools/house_model.py` is the 2028 House seats model.) PLAN 3.4 calls it "New, small and evidence-based"; stage C closed housing at L2-L3 without one. What exists is priced by hand: `dossiers/home/6-cost.md` (about $0.81 trillion over FY2030-39), `7-validation.md` (benchmarks against CBO, Urban, CBPP, USDA, IRS and HUD), `evidence.json` and `provisions.json`, and the HOU- rows in `models/data/budget/provisions.csv` that the budget model books. Every part of the standard is missing; a first model of assistance reach, rents and supply is **large**. Whether it is built in stage H is memo H5.

### 1.7 Immigration model (`dossiers/immigration/tools/`)

| Part | Score | Evidence | Gap | Size |
| --- | --- | --- | --- | --- |
| Model card | Partial | `immigration_model.py` docstring (lines 1-26): role, status "draft (board row I4)", four modules, "labor-market effects are not modeled"; an `INPUTS` table of central, low and high values, each citing EV-IMM- or "assumption: ..."; `7-validation.md` section 2 lists what is missing | No card file, `MOD-` ID or owner; no can't-answer list or research basis | medium |
| Benchmarks | Partial | `7-validation.md` section 1, in prose: the asylum corps against DHS (EV-IMM-302), judges against CRS (EV-IMM-642), status against CBO's 2021 score (EV-IMM-600, -604, -611) | No coded benchmarks; status's fiscal effect is CBO's score scaled, not modeled | medium to large |
| Interface | Partial | `python3 dossiers/immigration/tools/immigration_model.py` and `immigration_path.py` run standalone and print cases | No arguments, no file output, no scenarios; imports `dossiers/care/tools/health_path.py` | medium |
| Tests | Partial | `test_immigration_model.py`: 8 tests (every input traces; modules behave; `6-cost.md` quotes the tool's figures); run by `run-checks.sh` | No identities or reproduction of published results | small |
| Run log | Missing | Output is pasted into `6-cost.md` by hand | — | small to medium |

- **Ran:** the tests pass (8, 0.07 s). The central printout reads "at 800 judges: FYNone" where it means the backlog never clears, a printout fix.
- PLAN 3.4 puts "the full model, with a model card, in stage H"; labor-market effects are its largest missing module. The full model moves to `models/tools/immigration/`, and the dossier's `tools/` keeps a thin wrapper so `6-cost.md`'s test still passes.

### 1.8 Transportation model (`models/tools/transportation/`)

| Part | Score | Evidence | Gap | Size |
| --- | --- | --- | --- | --- |
| Model card | Partial | `readme.md` (running, files, known points); `moving_america.py`'s docstring (units; S sourced, R from ARCA, A assumption tags; "What is NOT here") | No card, `MOD-` ID, status or owner; no evidence IDs (inputs cite CBO series by name) | medium |
| Benchmarks | Partial | CBO series embedded as inputs; `golden/legacy-final-v3.txt` reproduces the legacy stack | It reproduces the project's own Draft 2; it compares nothing to an independent estimate (CBO's Highway Trust Fund projections, FTA's apportionments) | medium |
| Interface | Present | `python3 models/tools/transportation/report.py [--json OUT]`, standalone, standard library | Helper scripts write into the current folder; rail and scoring tables typed in by hand | small |
| Tests | Present | `test_moving_america.py`: Draft 2's protected figures and a line-for-line match with `golden/report.txt` (run-all step 0) | No identities or boundary cases | small to medium |
| Run log | Missing | `--json` output carries no version or hash | — | small |

### 1.9 The loose scripts in `models/tools/`

About sixty files sit directly in `models/tools/`. Which model each belongs to, and whether it ships:

| Group | Files | Belongs to | In the released toolkit? |
| --- | --- | --- | --- |
| The budget model's engine | `fiscal-model.py`, `fiscal-data.py`, `fiscal-profiles.py`, `inputs.py`, `scenarios.py`, `ledger-build.py`, `funds-model.py`, `climate-integration.py`, `window.py`; tests `test_fiscal_components.py`, `test_ledger_rounding.py`, `test_funds_model.py`, `test_climate_integration.py` | Budget (the climate reader is the energy model's interface to it) | **Yes**: moved into or wrapped by `models/tools/budget/` (H4) |
| The fiscal path analyses | `fiscal_path.py`, `fiscal_dynamic.py` (and its two `.json` files), `fiscal_frontier.py`, `test_fiscal_path.py` | Budget (stage G step 8) | Later: they are analyses on the budget model, and the fiscal path revision changes them; they can ship as the budget model's "debt paths" scenarios once that revision merges and the dynamic layer's red-team status is on its card |
| Dossier bookings and their checks | `care_booking.py`, `health_booking.py` (and `health_before_booking.json`), `clean_power_booking.py`, `immigration_booking.py`, `secure_floor_booking.py`, `work_booking.py`, `democratic_renewal_booking.py`, `settlement_booking.py`; the `test_fiscal_*.py` files (care, health, clean power, immigration, secure floor, work, democratic renewal, counting, MR6, health financing) and `test_settlement_booking.py` | The plan, booked on the budget model | **No.** They pin each dossier's booked figures and stay in the project's checks; they move together to `models/bookings/` so the released folders hold only models |
| Dossier cost tools and one-off analyses | `capacity-funding.py` (and test), `democratic_renewal_cost.py`, `democratic_renewal_pace.py`, `test_democratic_renewal.py`, `health_financing.py`, `health_cost_review.py`, `program_inventory.py`, `family-financing.py` (and test); folders `financing-protection/`, `capacity-review/`, `health/`, `strategic-review/` | Dossiers and stage G | **No**; move with the bookings. `health_cost_review.py` and `health_financing.py` are imported by `household/`, which has to stop importing them first (H3) |
| Superseded or paused | `ledger-paths.py`, `votes-model.py`, `test_calendar.py` and `calendar/` (paused, PLAN 3.4); `fiscal-recovery/` (its README says the recovery budget supersedes it); `recovery-budget/` (exploratory) | — | **No** |
| Infrastructure | `run-all.sh`, `check-project.py`, `dashboard-data.py`, `ledger-make-md.py`, `fiscal-make-md.py`, `climate-integration-report.py`, `carbon-model.py`, `migrate_paths.py`, `readme.md`, `roadmap.md`, `treasury-data/`, `public-product/` | — | No (`carbon-model.py` retires once the ledger reads `energy/`) |

**Not run anywhere** (neither `run-all.sh` nor `run-checks.sh`): `test_health_financing.py`, `test_health_cost_review.py` (about 3 minutes), `financing-protection/test_*.py`, `climate-portfolio/test_international.py`, `calendar/evidence-check.py`, `program_inventory.py`, `migrate_paths.py`, `treasury-data/`. `roadmap.md` still lists the retired `incidence-*.py` scripts.

### 1.10 One command, and what fails

- `bash models/tools/run-all.sh` on `f303483`: exit 0; every one of its 43 generated files **unchanged** against the committed copy.
- It reports, without failing: the public story's two drifted claims (`q4`, `downside`; part 2), and 493 evidence-register warnings (contested or uncorroborated analysis, and re-checks past due in clean power's register, EV-CLP-001 to -259); these are the register's routine flags, not model failures.
- Each model's own entry point and tests pass, as listed above. **The two failures:** `climate-portfolio/test_international.py` (a stale generated file, 1.5) and the front door builder (`public-product/build.py --check` and `test_build.py` stop with `git show 3594c784...: exit status 128`, because the pinned commit is not in a 50-commit clone; part 2).

## Part 2. The front door audit

### 2.1 What exists

| Piece | Built by | Pinned to | State |
| --- | --- | --- | --- |
| The front door, "A day in a possible 2050" (`public/site/index.html`), its analysis companion (`analysis.html`), three design treatments (`directions.html`), `public-map.json`, `manifest.json` | `models/tools/public-product/build.py` from `content.json`, `site.html`, `style.css`, `community.svg`, `interaction.js` | `3594c784`, October 25 (Codex, PR #19) | Working edition, never deployed (`manifest.json`: `working_public_edition_not_deployed`) |
| The story page, seven illustrated essays (`public/site/story.html`), its claim register (`story-claims.html`, `.json`) | `public-product/story/build_story.py` from `essays.json` (79 claims), `art/`, `story.css` | `650cadec`, October 27 (PR #39) | Working edition, never deployed; two claims drifted |
| Review screenshots (`public/site/review-*.png`) | By hand from the browser checks | — | Show the October editions |

**What is good and worth keeping:** a static, offline, script-light page under 200 KB with no outside requests; stable policy IDs behind plain names; a claim register in which every figure traces to an exact repository passage and the build fails on an untraced number; a "what this essay does not claim" box; browser checks at 320-1440 px, keyboard and no-JavaScript paths; colors checked to WCAG AA. That machinery is the right base. The content is what is stale.

### 2.2 What is stale against the specified flagships

**The front door (`content.json`, `build.py`):**
1. **Its evidence is the old tree.** Every source is a legacy domain file under its October names (`domains/domain-family.md`, `domains/domain-health.md` and so on, now `legacy/domains/`); none is a dossier. Its 36 policies carry pre-dossier IDs and options (FAM-1D, HOU-4A, HLT-1 to HLT-4, CLI-1 to 8, LAB-, AI-, DEM-, INT-, CAP-7, EDU-1 to 5, MOV-31).
2. **Health shows the wrong design.** It lists "A public health-insurance option" (HLT-3) as a selected design. Care's L3 design is the single plan (HLT-1, 2, 4, 6, 7, 8 booked); HLT-3 is an alternative at L2 (`dossiers/care/README.md`).
3. **Flagship 6 is missing.** No stop or policy covers immigration; it appears only as one of seven themes. The secure floor (flagship 1) is folded into "At home" rather than standing as a flagship, and fair financing appears only in the companion.
4. **The money is wrong.** `build.py` reads FY2040's general-fund primary gap from the long-term model's DEC scenario (`fiscal-paths.csv`), not the budget model's case `mixed` that the plan books, and the companion says "Financing strategy remains under holistic redesign; none of the three recent financing illustrations has been selected" (`build.py` line 181). The settlement has been booked since #480: every year FY2040-56 closes on the general fund, with the health contribution at 3.80% from 2035.
5. **Education stands as a selected design** (EDU-1 to 5), though education is a wave-two topic (stage I) not yet specified; `public/README.md`'s own note says the edition's fiscal headline predates the EDU-9B result.
6. **It cannot be rebuilt or checked from a normal clone:** the pinned commit `3594c784` is outside a 50-commit history, so `build.py --check` and `test_build.py` fail; `run-checks.sh` skips them by design.
7. Its README (`models/tools/public-product/README.md`) links to `../../../sources/...` and `../../public-2050/...`, paths that no longer exist.

**The story page (`essays.json`):**
1. Pinned to October 27, the day before the reset: before any dossier existed. Its 79 claims cite the legacy tree, including the recovery budget's old tables.
2. **Two claims already fail** against main: `q4` and `downside` cite rows of `index/recovery-budget.md` that no longer exist (run-all step 8d; board "Known gaps", "Public pages").
3. Its essay "Paying for it honestly" predates the settlement and the fiscal path review.

**Against the fiscal path review (#483 to #485) and batch 3 (`DEC-2026-11-25-01` to `-11`, #487):**
- The settlement's debt figures (117.8% of GDP in FY2040, 133.1% in FY2056) are booked, but **G15 is decided as "B, made more aggressive" and is provisional until the revision step redrafts it and Espen confirms** (`DEC-2026-11-25-01`). G19's mix is re-checked in the same step, and a VAT or other broad measure is now allowed after the plan's first years. The debt limit's repeal (G21 A, `DEC-2026-11-25-07`) comes with a direction to say so publicly before 2029.
- So the front door can say now: the plan is paid for on the general fund in every year from FY2040 on the project's estimates; health's financing; who comes out ahead (D3, now tested in FY2040 and FY2050 too, `DEC-2026-11-25-08`); no dynamic saving counted up front (`-11`); the debt-limit position. It should **not** state a debt path, the take-home share or the later revenue steps until the revision step has merged and Espen has confirmed G15. The content step (H8) runs its money section last for that reason.

### 2.3 What the "day in 2050" has to show

PLAN 3.5: the front door "is rebuilt on the specified flagships", and every public piece is built from its dossier, never ahead of it. Concretely:
- **One day, eight scenes, every flagship and foundation:** the secure floor (1), care (2: health and long-term care, child care), housing (3), clean power (4), work (5), immigration (6), democratic renewal and fair financing; transportation can join as wave two's converted dossier. Each scene is fiction and labeled so.
- **Each scene names what made the difference** in plain words, with the provision behind it and **when it begins**: the section 9 rule that a promise holds from the date its provision takes effect (`dossiers/TEMPLATE.md`, "Section 9 only from sections 1 to 8"). A 2050 scene can show a 2035 protection only if the law starts it by then.
- **Every number from a dossier's sections 1-8**, through a claim register like the story page's, with "about" and the conditions; model results as "our analysis", never official scores.
- **The money told honestly:** what is paid for and how, who pays, who comes out ahead, and what is still to be decided (part 2.2).
- **Hard questions with honest answers**, from each section 9's hard-questions list.
- **A route into the depth:** each scene links to its flagship brief (section 9), the dossier and the toolkit model it rests on; the analysis companion becomes the toolkit's front page for professionals.
- Plain language for a general reader, in the persuasive, forthright and optimistic voice Espen set; fast on a phone; accessible.

Every flagship except fair financing has a reviewed section 9 to build from: `dossiers/secure-floor/9-public-case.md`, `care/9-public-case.md` and `9bcd-public-case.md`, `home/9-public-case.md`, `clean-power/9-public-case.md`, `work/9-public-case.md`, `immigration/9-public-case.md`, `foundations/democratic-renewal/9-public-case.md`, `agenda/transportation/9-public-case.md`. Fair financing has none yet; its public case is written after the revision step. Some section 9s predate the settlement: work's can't-say list still says the plan-wide settlement "has not yet run" (`dossiers/work/9-public-case.md`, line 124), and its money lines were written before #480. H8 re-reads every money line against `dossiers/foundations/fair-financing/2-settlement.md` rather than copying it, and lists any section 9 that needs a touch. The research briefs and organizing kits PLAN 3.5 also asks for do not exist outside these section 9s; this plan builds the front door and leaves the kits to a later step (memo H4).

## Part 3. The stage H plan

### 3.1 Steps

Step H1 is this audit. H2 is split: H2a (tier 2) sets the frame, H2b (tier 3) adds the license and the `.github/` wiring, because those need Espen's label (`charter/STANDARDS.md`, "Merge categories"). Toolkit steps come first. Each is one PR-sized session. "Writes" lists the files a step owns, which decides what can run in parallel.

| Step | Work | Tier | Inputs | Outputs (writes) | Acceptance check |
| --- | --- | --- | --- | --- | --- |
| **H2a. The toolkit's common frame** | Sets the conventions every model follows (part 3.5): (1) a card template with the standard's seven elements; (2) a **parameter-file schema** (each input: value, unit, effective year, evidence ID or source URL, and a range for assumptions), from which each card's evidence table is generated; (3) a **results schema** with a fixed header (model ID, version, commit, input hashes, units, price basis, year type, baseline vintage, scoring convention) and the line "not an official score or a benefit determination" stamped in by the run-log helper (`models/runlog.py`), which also appends a `RUN-` row to `models/runs.csv`; (4) a **validation-table convention** (target, source and vintage, model figure, difference, tolerance set in advance, pass or miss, explanation), generated by test code; (5) a **versioning rule** (major: results or interface change; minor: new scenario or parameter; patch: no change in results) with a `CHANGELOG.md` per model and a check that a changed results file without a version bump and changelog line fails; (6) the register of model IDs (`models/toolkit.csv`) with each release criterion's pass or fail (memo H1); (7) housekeeping: regenerate the stale international report and add `test_international.py`, `test_health_financing.py` and `financing-protection/test_*.py` to `run-checks.sh` (the slow one behind a flag), and make child-poverty's validation write to `build/` | Most capable (it sets the interface every model follows) | This audit; memos H1, H2 | `models/MODEL-CARD-TEMPLATE.md`, `models/schema/` (parameter and results schemas), `models/runlog.py` and its test, `models/toolkit.csv`, `models/registry/` (the `RUN-` and schema checks) | The helper's and schemas' tests pass; the checks run in `run-checks.sh`; `test_international.py` passes |
| **H2b. The license and the checks wiring (tier 3)** | The license files as memo H2 decides, a line in each model card, `CITATION.cff`; the `run-checks.sh` additions from H2a (the new tests and checks) | Light (mechanical, to a decided spec) | Memo H2 answered; H2a merged | `LICENSE`, `LICENSE-docs`, `CITATION.cff`, `.github/scripts/run-checks.sh` | Checks pass; merged only with Espen's label |
| **H3. Household and health coverage to the standard** | Household: its inputs moved into a parameter file on H2's schema, the card's evidence table generated from it; `run.py` able to start from a committed ledger snapshot when `build/` is absent; a fetch script that downloads the CPS archive and checks its hash; fixed seeds for the intervals; stop importing `health_cost_review.py` and `health_financing.py` (read their outputs as data); results on H2's schema, run log back-filled from the November 16 runs to the settlement. Health coverage: `inputs.csv` mapped onto the parameter schema; the card's status and date; the untraced inputs traced or listed; the three benchmark misses kept, in the validation table; both models get a changelog and a known-issues list | Standard | H2 | `models/tools/household/`, `models/tools/health-coverage/` | A fresh-clone job runs each model's one command and tests; results unchanged; each card passes H2's criteria |
| **H4. The federal budget model released** | One command (`python3 models/tools/budget/run.py --reform FILE --out DIR`) that builds the baseline, ledger, paths and funds into `DIR` without `run-all.sh`. **Current law is the default**; the plan (case `mixed`) ships as one example reform file and a published CBO option (from its *Options for Reducing the Deficit*) as a neutral second, so the tool reads as general, not as the plan's calculator. The engine scripts move into `budget/` with thin shims at the old paths so `run-all.sh` and the bookings keep working; the bookings and dossier tools move to `models/bookings/`; the card gets its evidence map, owner role, `MOD-budget` ID and status; parameters, results and validation tables on H2's schemas | Most capable (errors here spread to every dossier) | H2; **stage G step 9 merged** (its revised `fiscal_path.py`, `fiscal_dynamic.py`, CLI-1 tail and settlement tests are H4's starting point) | `models/tools/budget/`, shims at the old paths, `models/bookings/`, `run-all.sh` (paths only) | `run-all.sh` reproduces every committed output unchanged; `budget/run.py` from a fresh clone with the plan's reform file reproduces `fiscal-paths.csv`'s case `mixed` exactly; the card passes H2's criteria |
| **H5. Energy and climate, and transportation, to the standard** | Energy: re-point `carbon-model.py` and the portfolio at `energy/`'s engine and retire the duplicate, or record why both stay; one umbrella card for the family; parameters on H2's schema; **the Carbon Dividend Model's license settled with Espen** (memo H2: `MOD-energy` can't be released on an unlicensed engine). Transportation: a card (`MOD-transportation`), evidence IDs for its inputs, one independent benchmark (CBO's Highway Trust Fund projections), results on H2's schema | Standard | H2; memo H2's answer on the engine | `models/tools/energy/`, `carbon/`, `climate-portfolio/`, `carbon-model.py`, `models/tools/transportation/` | `run-all.sh` unchanged outputs; both cards pass H2's criteria |
| **H6. The immigration model, full version** | Move to `models/tools/immigration/` (`MOD-immigration`) with a card, arguments, JSON output and scenarios; coded benchmarks against CBO, CRS and DHS; the labor-market module PLAN names, with its evidence and limits; the "FYNone" printout fixed; the dossier's `tools/` becomes a wrapper | Most capable (a new mechanism and its evidence) | H2; `dossiers/immigration/` sections 6 and 7 | `models/tools/immigration/`, `dossiers/immigration/tools/` (wrapper only) | `6-cost.md`'s figures reproduce exactly; the labor module's results sit beside them, unbooked; the card ticks every element |
| **H7. The housing model** (only if memo H5 says build it now) | A small model of assistance reach, rents and supply from `dossiers/home/` sections 1-7 and its evidence register; reproduces `6-cost.md`'s cost | Most capable | H2; memo H5 | `models/tools/housing/` | It reproduces `6-cost.md`; benchmarks against CBO and HUD; card complete |
| **H8. The front door's content** | From the outline in `2-front-door-outline.md`: a content file built from the section 9s (the day's scenes, each scene's provisions and start dates, the hard questions) and a claim register on the story page's machinery (every figure traced to a dossier passage); the money section written last, after stage G step 9 and Espen's batch 4; a generated docs page per model (card, parameter table, validation table, changelog, how to run) built from H2's files so it can't drift; the builder pinned to a commit that a normal clone holds, with a drift report in `run-checks.sh` | Most capable (public claims) | The section 9s; memo H4; H2's files | `models/tools/public-product/` (new content and builder), `public/README.md` | Every claim traces; `--check` and the tests pass from a fresh clone; a reviewer's claims read finds no claim ahead of its dossier |
| **H9. The visual design, in Figma** | Create the project's Figma file; a style frame (type, color tokens light and dark, illustration direction) and three directions for Espen to choose from; then the chosen direction as phone and desktop frames for the day's scenes, the scene detail, the money section and the toolkit page; illustration briefs per scene | Most capable (design) | H8's scene list and copy; memo H4 | A Figma file (link on the board); `public/design/` with exported tokens and the frame list | Espen picks a direction; the frames cover every page H10 builds; text and color pairs at WCAG AA |
| **H10. The site built from the design** | Build the pages from H8's content and H9's frames; original illustrations to the briefs; browser checks at 320-1440 px, keyboard, no-JavaScript, reduced motion; retire the October edition's pages | Most capable (or Standard to a finished design) | H8, H9 | `public/site/`, `models/tools/public-product/` | The browser checks pass; every claim traces; screenshots match the frames |
| **H11. Release** | The reviewer's milestone review of the toolkit and site (claims, limits, the never-official-scores line); a short `CONTRIBUTING.md` and issue templates (a bug, a benchmark discrepancy) that say plainly that agents maintain the project, answers come through GitHub only, and there is no support promise; the first tagged release with release notes, golden output hashes and a toolkit-only archive attached; optionally a minimal `pyproject.toml` so `pip install` from the tag works (memo H3); publication as memo H3 decides; Espen's approval for anything that goes public | Most capable | All above; memos H1 to H3 | Release notes, tag, `CONTRIBUTING.md`, `.github/` templates and publishing workflow (tier 3) | The reviewer approves; Espen approves publication; the published pages and archive match the tagged commit |

### 3.2 Order and parallel work

- **First:** H2a, alone (every other toolkit step uses its template and helper; "H2" in the other rows means H2a). H2b, the tier-3 license and checks PR, follows as soon as memo H2 is answered and runs alongside the model steps.
- **Then in parallel, up to the three-session limit:** H3, H5 and H6 write different folders. H8 can start alongside them on everything but its money section: it writes only `models/tools/public-product/`.
- **H4 waits for stage G step 9** (it moves the scripts step 9 edits, and starts from step 9's versions); it then runs alongside whichever of H3, H5 and H6 remain.
- **H9 after H8's scene list** (it can start on the style frame and directions while H8 finishes); **H10 after H9**; **H11 last.**
- H7 runs whenever memo H5 places it; it writes only `models/tools/housing/`.
- **Count:** eleven steps (twelve with H7), H2b being a small Light session, against PLAN's 5-8. To shrink: fold H5 into H3 (one Standard session, two models each), or defer H6's labor module and H7 to stage I. The parts that can't shrink are H2, H4 and the front door's three steps.

### 3.3 The Figma work

The Figma connector is on. This step creates no file; H9 does, once H8 has the scene list. H9's file holds: (1) a style frame with type, color tokens (light and dark) and spacing; (2) three directions on one scene, for Espen's choice, the way the October edition offered three treatments; (3) the chosen direction across the day, the scene detail, the money section and the toolkit page, phone and desktop; (4) an illustration brief per scene. Tokens are exported into `public/design/` so the site's CSS reads them and the repository stays the source of truth. The illustrations are original work, as the story page's are.

### 3.4 Where the toolkit and the site would live

This is Espen's choice (memo H3). The lead recommends keeping the site's code in this repository for now, and Espen has turned off the Lovable, Wix and AnimatedWebs connectors; every option below keeps the code here. The options:
- **The toolkit:** tagged releases of this repository (the `models/` folders, with the register and cards), or its own repository fed from this one.
- **The site:** GitHub Pages built from `public/site/` by a GitHub Action; a claude.ai artifact (private by default, for review copies, not a public home); or a static host such as Cloudflare Pages (the October blueprint's recommendation, `legacy/sources/public-product-blueprint.md`, "Hosting and release maintenance"), which needs an account Espen creates.

### 3.5 What the professional-practice review changed

Espen asked (November 25) that tough analytical and toolkit-design work may consult a Fable model. A Fable subagent read this plan, memos H1 to H3 and two model cards, and critiqued them against how CBO, JCT, the Tax Policy Center, PolicyEngine, the Penn Wharton Budget Model and the Policy Simulation Library (Tax-Calculator, OG-USA) package and release models. It worked from its own knowledge, without web searches. What changed:
- **Parameters as data** (H2a, H3 to H6): each model's inputs move into a parameter file with value, unit, effective year, evidence ID and range, and the card's evidence table is generated from it, as PolicyEngine's and Tax-Calculator's parameter files are. This replaces hand-written evidence tables.
- **A results schema and a mechanical disclaimer** (H2): every results file carries the same header, and the run-log helper stamps "not an official score or a benefit determination" into it, not only onto cards.
- **A versioning rule and changelogs** (H2): semantic versions per model, a changelog line stating how much a headline result moved, and a check that fails a results change without either.
- **A validation-table convention** (H2) with tolerances set in advance and the baseline vintage stated, as CBO's and JCT's methods papers do.
- **The plan separated from the models** (H4): current law is the default run; the plan is one example reform beside a neutral CBO option.
- **Reproducibility finished** (H3, H11): fresh-clone jobs, a CPS fetch script with a hash, fixed seeds, golden hashes on the release.
- **Per-model docs pages** (H8), a contributor note and issue templates (H11).
- **Memos:** H1's recommended option is now a published checklist with a labeled preview tier for "working" models; H2 notes the field's norms (CC0 for parameter files) and that the Carbon Dividend Model's license gates `MOD-energy`'s release; H3 adds `pip install` from a tagged release as a packaging choice inside option A.
- **Kept as sound:** the honest scorecard; reproducing committed outputs exactly as each refactor's test; the shims; bookings out of the released folders; standard library only; one repository as the source of truth; outside review as a later upgrade; H2 first and step 9 gating H4; no hosted API now.

## Questions for Espen

Memos H1 to H5, each decided on its own (`memos/README.md`):
1. **H1:** what "released" means for a model.
2. **H2:** the license for the code and the writing.
3. **H3:** where the toolkit and site live, and in what form.
4. **H4:** the front door's scope.
5. **H5:** whether the housing model is built in stage H.
