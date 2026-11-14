# Energy and climate model: model card

Role: the model card of `MOD-energy`, the core energy and climate model of `charter/PLAN.md` 3.4 (emissions, prices, bills, dividends; flagship 4). Status: **working**. The model runs clean power's decided set (`DEC-2026-11-13-06`, `-07`) and passes the benchmarks its status rests on: DA-1, DA-2, BL-1, PR-1 and BK-1. One benchmark fails and one is not yet built; both are explained below. Owner: Claude Code (the M4 worker session), reporting to the lead. Its design is `survey.md`, section 4. Generated results are in [`results.md`](results.md) and `results.json`. Never quote a figure from this card that `results.md` no longer shows.

## What it answers, and what it cannot

It answers, year by year from 2025 to 2050, against the January 2029 current law (`DEC-2026-10-29-01`):
- **emissions:** energy CO2 by sector (power, transport, industry, buildings), industrial process CO2 and N2O, methane, fluorinated gases and net greenhouse gases, against 2005 and against the 2029 baseline;
- **receipts:** the carbon price on power plants and large industry (memo 1 B), process emissions, the border adjustment, the methane fee, and the clean electricity standard's capped payments, each with the adopted 24.4% income and payroll tax offset (`DEC-2026-11-12-08`);
- **outlays:** the 80/20 split into the Climate Dividend and the transition share, the dividend per adult, and the engine's estimate of the credits' cost (a cross-check, not a score);
- **prices and households:** the national average retail electricity price, and the carbon channel's cost and dividend by income fifth;
- **layers and options:** the decided set built up one measure at a time, the options memo 1 weighed (A, C, D), a repeal test and sensitivities (industry coverage, the builder's strength, the permitting package);
- **for clean power's re-review** (`DEC-2026-11-13-12`): `results.md` answers the list in #346 point by point, including the coal and gas fleets' wind-down for the transition guarantee's count of closures. The guarantee itself (CLI-11, with tribal governments' lost revenue, `DEC-2026-11-13-11`) is priced by the dossier, not here;
- **for the booking step:** every receipt and outlay by fiscal year under provision IDs (`results.json`, `provisions`).

It cannot answer, by design (`survey.md`, 4.5):
- **regional, hourly or least-cost power questions** (ReEDS, IPM or RIO answer those): one national market with a sourced build pipeline;
- **macroeconomic, GDP or jobs effects:** the budget model is not dynamic, and the offset is the convention for the tax interaction;
- **fuel market prices:** fuel prices are inputs, as in the Energy Policy Simulator;
- **land use and forests** beyond the inventory's sink held at its recent level; CLI-13 stays as booked;
- **leakage** beyond the border adjustment's small trade response;
- **health effects** beyond the carbon model's own power-plant figure (not reported here yet);
- **bills by region:** the engine is one national market (#346's item 3);
- **official scores or individual benefits** (`charter/PLAN.md` 3.4).

## How it is built

| Layer | File | What it does |
| --- | --- | --- |
| Engine | `engine/cfd-model.js`: a copy of Espen's Carbon Dividend Model v3.4 (`models/tools/carbon/`) with M4's options; `engine/cfd-tests.js` holds its regression checks | Power dispatch and build, vehicle cohorts, heating turnover, industrial abatement, methane, fluorinated gases, the border adjustment; 2025 dollars |
| Driver | `engine.js` | Runs the cases and returns every row field the accounts need, households against any base case, and the Monte Carlo |
| Scenarios and accounts | `model.py` | The layers, options and sensitivities; nominal accounts by year |
| Data | `data.py` | AEO2026, EIA and NOAA series read from the library's saved texts |
| Results and benchmarks | `run.py` | One command: `python3 models/tools/energy/run.py` writes `results.json` and `results.md` |
| Tests | `test_energy.py` | Identities, boundary cases, data traced to source, driver equivalence, the status benchmarks |

**Why a copy, and what M4 added to it.** The legacy carbon model stays as it is: its exports record the engine file's hash, and one of them is pinned in an adopted input (`models/data/inputs/climate-adoption.json`), so editing it would be a tier-3 change for no change in any figure. The energy model runs its own copy. Every option added defaults to the original behavior, and `test_energy.py` checks that the copy with defaults gives the original's rows exactly on four designs; BK-1 reproduces the legacy run's receipts. When the legacy suite is retired (`models/README.md`), its readers can move to this engine.
- `sectorPrice`, memo 1 B's coverage. The share of the fee each sector's fuel pays directly: buildings 0, non-road transport 0, industry at its covered share.
- `heatStd`, the clean-heat standard (CLI-4H.01). A soft floor on heat pumps' share of heating-equipment sales, like the vehicle standards.
- `retailNetCredits`. Nets the power credits out of the cost passed to retail prices. Without it the engine charged ratepayers the full capital cost of credited plants, and restoring credits appeared to raise prices (BI-1 caught this).
- `retailAcp`. Adds the clean standard's capped payments, which suppliers pay to Treasury, to the cost passed to retail prices. Credit trades between plants net out inside the sector either way. Clean power's re-review found the gap (R-2, `dossiers/clean-power/review-m4.md`).
- `feeHeat` on each row, so the household module charges home heating only when buildings are priced.

## Evidence map

| Input | Value or source | Kind |
| --- | --- | --- |
| Price path | REV-C1A.01: $25 in 2030, $150 by 2037, then 5% a year (`carbon-parameters.csv`) | Decision (adopted input) |
| Coverage | Power plants (40 CFR part 75) and industrial facilities at or above 25,000 t CO2e (REV-C1G.01); homes, commercial buildings, road and non-road transport fuel not charged (REV-C1G.02) | Decision |
| Industry's covered share | 80% (70-90%), applied as a blended price signal | **Labeled assumption** (`assumptions.csv`, `ind_cover`); no count of covered combustion CO2 is in the evidence yet |
| Clean electricity standard | 80% by 2035, 100% by 2040; payment cap $40/MWh (2025 dollars) | Decision (CLI-3A.01); cap a working choice (CLI-3A.02) |
| Clean-heat standard | 60% of sales in 2032, +5 points a year | Decision (point 9); shares a working choice (CLI-4H.01) |
| Credits | The engine's restored set; household credits full through 2034, vehicle credits through 2032, then stepping down | Decision (memo 2 B); terms are working choices (CLI-1A.02). The engine's power credits stop at its emissions trigger rather than stepping to 60%, an approximation |
| Methane fee | $1,200 to $1,500 a ton from 2030, certified-facility exemption | Decision (point 3; `carbon-parameters.csv`) |
| Moving America's fuel steps | Road fuels priced by the gallon (MOV-29), from the transportation model | Decision (transportation dossier) |
| Offset | 24.4% (`excise-offset.csv`) | Decision (`DEC-2026-11-12-08`); CBO 21-25% (SRC-2453); JCT 25% historically (SRC-5005) |
| Dividend | 80% of combustion receipts, equal per adult; adults 77% of CBO's population | Decision (CLI-2A.04); share a convention (`assumptions.csv`) |
| Permitting package | Not assumed; a sensitivity with it enacted in 2027 | Working choice (`dossiers/clean-power/3-design.md`) |
| The standby builder of last resort | The engine's federal grid program at half strength (25-100%) | Decision (memo 4 B as decided, `DEC-2026-11-13-10`); strength a **labeled assumption** (`assumptions.csv`, `grid_standby_scale`): it builds only where others fail, so less than a builder everywhere |
| 2025 starting point | EIA energy CO2 by sector (SRC-5004) | Data |
| Baseline benchmark | AEO2026 combination case (SRC-5049; main case SRC-5050) | Analysis (EIA, second Trump administration; checked against Rhodium and the 2026 review) |
| 2005 base | EPA net 6,536 Mt (SRC-4460); EIA energy 5,999 Mt | Data |
| Weather | NOAA degree days (SRC-5047, SRC-5048) | Data |
| The Energy Policy Simulator's two pathways | Total CO2e including land use, 2025-2050, from version 4.0.7's web tool, Current Policies and US Climate Action, run by Espen (`models/data/energy/eps-us-4.0.7-runs-2026-11-13.csv`) | Analysis (Energy Innovation's model and scenarios; an advocate's package, SRC-5044) |
| The engine's behavioral inputs | 37 uncertain inputs with ranges, each sourced or assumed in the carbon model's notes (SRC-0077) | Mixed, as documented there |

## Mechanisms and their basis

- **Stock turnover and technology choice.** The engine has vehicle cohorts, heating stock and a power fleet. New purchases are split by logit choice on cost, with standards as soft floors (SRC-0077). The Energy Policy Simulator works the same way: vintaged stocks, logit choice calibrated to historical sales (SRC-5012, SRC-5014). The methods are re-implemented in our own code, and no GPL code is used (SRC-5016, SRC-5021).
- **A carbon price by sector, on each fuel's CO2 and on process emissions.** This follows the Energy Policy Simulator's carbon tax, which is set by sector and can cover or exempt process emissions and non-CO2 gases. Its design switches include a border adjustment and export rebates (SRC-5015, SRC-5021).
- **Retail prices.** The change in the power sector's average cost is passed through in full, net of credits: the cost-of-service treatment of regulated utilities. NEMS uses it for regulated regions (survey.md, 2.2) and the Energy Policy Simulator offers it as a rate pathway (SRC-5011).
- **A baseline from outside, checked.** The Energy Policy Simulator takes its baseline from other studies (SRC-5012). This model keeps the engine's calibrated baseline and checks it against AEO2026's combination case (BL-1). The two are within 5% through 2040. Recalibrating the engine would have moved booked legacy figures for no gain inside the budget window.
- **Benchmarks that explain differences.** In the Energy Policy Simulator's words, results "need not match other models", but the reason for a difference should be understood (SRC-5043). En-ROADS's practice of scoring a whole path's closeness with SMAPE is used for EM-1 (SRC-5045).

## Benchmarks

`results.md`, "Benchmarks", has every row and why each difference arises. In short:
- **The status rests on DA-1, DA-2, BL-1, PR-1 and BK-1, and all pass.** DA-1 and DA-2 are in-sample (the engine is calibrated to those figures). BL-1 tracks AEO2026 through 2040, and the 2050 gap is explained. PR-1 is inside EMF 37's per-dollar range, in its lower half. BK-1 reproduces the legacy run.
- **PR-2 fails.** Receipts on CBO's price path run about 26% above CBO's $919 billion in every year. The engine cuts emissions slowly in its first decade, so its tax base stays high. The ledger already sets REV-C1 below the model for this reason. A booking should take the model's receipts as the high side of a range, not as a point.
- **HI-1 is not built.** The history run needs the engine to start in 2015.
- **Against the Energy Policy Simulator, run by Espen (November 13, 2026):** BL-3 passes. Current policy cuts net greenhouse gases 13% from 2025 to 2035 here, and 10% in the simulator's Current Policies pathway. PK-1 is reported, not tested: the simulator's US Climate Action package cuts 43% by 2035 against the decided set's 29%. It is a far wider package with no carbon price: more industrial, building, land and carbon-removal measures. The gap shows what such measures would have to add toward point 1's goal.
- **Reported, not pass or fail:**
  - CR-1, the credits' effect against the IRA comparisons. The comparison is not like for like, and the reason is stated.
  - EM-1, the closeness score.
- **Passed in direction or shape:** BI-1, the credits' effect on prices, and DI-1, who comes out ahead.
- **BK-2 passes.** It checks memo 1's proportional arithmetic against a run.

## Limits

- **One national power market, no hours or regions.** The clean standard's feasibility rests on the engine's grid-access limit, not on a regional build (SRC-0077, v2.4).
- **Structural uncertainty is larger than the Monte Carlo bands.** The bands vary inputs only. Published models differ by more for the same policy.
- **Industry's covered share is assumed.** The memo 1 B coverage applies it as one blended price, not facility by facility. The `ind_lo` and `ind_hi` rows show its range.
- **The power credits stop at the engine's emissions trigger** rather than following CLI-1A.02's 60% step. The credit cost is the engine's estimate and runs above the booked CLI-1 (`results.md`, "For the budget model's booking step"). It is a cross-check, not a score.
- **Calendar years are booked as fiscal years,** as the ledger books these rows. PR-2 applies CBO's fiscal-year timing for its own comparison only.
- **The engine's 2025 calibration is not weather-normalized.** NOAA's degree days put 2025 within a few percent of normal (results.md).
- **The social-cost table is a labeled side table on EPA's 2023 estimates.** It is not federal guidance: OMB M-25-27 tells agencies not to monetize greenhouse gas effects (SRC-5007). Temperature is converted for CO2 only.

## Interfaces

- **Budget model.** `results.json` → `provisions` gives each receipt and outlay by fiscal year, under the provision IDs of `dossiers/clean-power/4-specification.md`, beside the ledger's booked midpoint. The booking step after clean power's milestone review reads it. This model changes no ledger row.
- **Household model.** The carbon channel by income fifth comes from the carbon model's survey-based module. Passing the price through the household model's incidence keys for the D3 test is part of the booking step.
- **Clean power's dossier tools.** `dossiers/clean-power/tools/coverage_read.py` and `clean_power_path.py` stand in for this model's coverage run. They can read `results.json` instead.
- **The climate pricing export's 25% offset** (#289) is rebuilt in a separate tier-3 PR, because its file's hash is pinned in `models/data/inputs/climate-adoption.json`.

## Run log

`results.md` and `results.json` record the first 16 hex digits of the SHA-256 of every input file: the engine, the driver, this model's code and assumptions, the adopted inputs and the saved data. The same inputs give the same outputs, so the rebuild's drift check ties every published figure to its inputs.
