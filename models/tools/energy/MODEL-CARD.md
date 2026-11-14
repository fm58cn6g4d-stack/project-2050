# Energy and climate model: model card

Role: the model card of `MOD-energy`, the core energy and climate model of `charter/PLAN.md` 3.4 (emissions, prices, bills, dividends; flagship 4). Status: **working**. The model runs clean power's decided set (`DEC-2026-11-13-06`, `-07`) and passes the benchmarks its status rests on: DA-1, DA-2, BL-1, PR-1 and BK-1. Two benchmarks fail, PR-2 and HI-1; both are explained below. Owner: Claude Code (the M4 worker session), reporting to the lead. Its design is `survey.md`, section 4. Generated results are in [`results.md`](results.md) and `results.json`. Never quote a figure from this card that `results.md` no longer shows.

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
- `retailAcp`. Adds the clean standard's capped payments, which suppliers pay to Treasury, to the cost passed to retail prices. Credit trades between plants net out inside the sector either way. Clean power's re-review found the gap (R-2, `dossiers/clean-power/review-m4.md`); it estimated about two-thirds of a cent by 2040 and the fix gives about half a cent.
- `retro`. Carbon capture retrofitted to existing coal and combined-cycle plants (off by default; the energy model reads it from `assumptions.csv`, `ccs_retrofit_*`, with `ccs_retrofit_scale` as the switch). Each year from `start`, owners start retrofits where the expected carbon price, or 45Q while it lasts, covers the annualized cost; coal first, up to the eligible coal, then combined cycles, at most `rate` GW a year and `cap` GW in all (both times the scale). A retrofit comes online `lead` years later, derated, with a heat-rate penalty, and captures the set share of its CO2. Each captured ton earns the larger of the carbon price avoided and 45Q (not both, as for the engine's new capture plants), and 45Q is booked as a credit outlay for 12 years when construction started before the credit's deadline. Costs and performance are EPA's (IPM Table 6-2, SRC-5067); capture in operation, lead time and limits are labeled assumptions drawn from EPA's 2026 partial repeal (SRC-5069) and CRS (SRC-5068).
- `crPowSched`. The power credits step down on the dates fixed in statute (CLI-1A.02) instead of ending at the engine's emissions trigger. `crPhase`, used only without a schedule, phases them out over three years after the trigger as the IRA provides (26 U.S.C. 45Y(d)(3)), not in one year; the one-year cliff had put a 0.9-cent jump into the retail price in a single year.
- `q45Stack`. Off by default: a stored ton earns the carbon price avoided or 45Q, whichever is larger, for new gas plants with capture, industrial capture and retrofits alike. On, it earns both, as current law allows unless the price's statute nets 45Q out (memo 8). `q45Other` reports 45Q on stored tons outside retrofits; the ledger books current-law 45Q outside this model.
- `coalDamp` (off). Coal and gas generation move only part of the way in a period from the dispatch at last period's prices toward this period's (partial adjustment). Tested against HI-1 and HI-2 and not adopted (see Benchmarks).
- Retrofits and retirement. A coal unit with a retrofit under way is not retired if the retrofit will meet the power plant standard (capture of at least 90%, memo 8's CLI-4R.01); below that, under the standard, no coal retrofit starts and any built retire by 2040.
- `peakFactor`. The ratio of peak to average load in dispatch (default 1.5). The monthly history (HI-2) sets each month's so its peak is no higher than the year's; at 1.5 every July and August ran short of capacity.
- `feeHeat` on each row, so the household module charges home heating only when buildings are priced.

## Evidence map

| Input | Value or source | Kind |
| --- | --- | --- |
| Price path | REV-C1A.01: $25 in 2030, $150 by 2037, then 5% a year (`carbon-parameters.csv`) | Decision (adopted input) |
| Coverage | Power plants (40 CFR part 75) and industrial facilities at or above 25,000 t CO2e (REV-C1G.01); homes, commercial buildings, road and non-road transport fuel not charged (REV-C1G.02) | Decision |
| Industry's covered share | 80% (70-90%), applied as a blended price signal | **Labeled assumption** (`assumptions.csv`, `ind_cover`); no count of covered combustion CO2 is in the evidence yet |
| Clean electricity standard | 80% by 2035, 100% by 2040; payment cap $40/MWh (2025 dollars) | Decision (CLI-3A.01); cap a working choice (CLI-3A.02) |
| Clean-heat standard | 60% of sales in 2032, +5 points a year | Decision (point 9); shares a working choice (CLI-4H.01) |
| Credits | The engine's restored set; household credits full through 2034, vehicle credits through 2032, then stepping down | Decision (memo 2 B); terms are working choices (CLI-1A.02). Power credits follow CLI-1A.02's step-down (`crPowSched`): wind, solar and transmission full through 2034, 60% through 2037, storage full through 2039 (`assumptions.csv`) |
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
| The Energy Policy Simulator run on the plan's settings | Total CO2e including land use, 2025-2050, version 4.0.7, two runs by Espen: the carbon price alone and the decided set as the sliders allow (`models/data/energy/eps-us-4.0.7-runs-2026-11-13-p2050.csv`; the header lists each run's settings) | Analysis (Energy Innovation's model, our settings) |
| The Energy Policy Simulator's generation by type | Current Policies and runs 1 and 2, 2025-2050, by Espen (`models/data/energy/eps-us-4.0.7-generation-2026-11-13.csv`) | Analysis (Energy Innovation's model, our settings) |
| Power-sector history by month, 2019-2024 | EIA Monthly Energy Review generation, fuel costs and coal stocks (SRC-5064 to SRC-5066) and power CO2 (SRC-5057) | Data |
| Power-sector history, 2015-2025 | EIA Electric Power Annual generation, capacity and fuel costs, and Monthly Energy Review power CO2 (SRC-5052 to SRC-5057) | Data |
| Carbon-capture retrofits | EPA IPM Table 6-2 costs and performance (SRC-5067); EPA's 2026 partial repeal of the Carbon Pollution Standards for Boundary Dam 3's record, the seven-year lead time and the 40 GW considered (SRC-5069); CRS on storage permits (SRC-5068); 45Q (SRC-5070) | Data, with labeled assumptions for capture in operation, lead time and limits |
| Regional fuel price spread | EIA Electric Power Monthly delivered coal and gas prices and receipts by state, January-August 2025 (SRC-5058 to SRC-5061), times a calibrated 1.5 | Data, with a labeled calibration |
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
- **HI-1 fails (power sector, 2015-2025), narrowly, after a fix that halved the gap.** Fed each year's measured fleet, generation and fuel prices, the engine's power dispatch first missed measured coal and gas CO2 by 9% on average: with one national fuel price it switched the whole fleet between coal and gas at once. The dispatch now splits each block of plants by the spread of delivered fuel prices EIA measures across states (29% of the average for coal, 20% for gas), widened 1.5 times (`assumptions.csv`, `fuel_spread_mult`, a labeled calibration), with the engine recalibrated to its own 2025 targets (DA-1 still passes). The gap is now 5.7% over all eleven years (4.3% leaving out 2021-22), against a 5% tolerance. An earlier version left 2021-22 out for the coal shortage; HI-2 showed that was not justified, so every year is scored.
- **Damped switching, tested and not adopted.** Moving 60% of the way each period narrows HI-1 to 5.2% (still a fail) and HI-2 to 6.9%, but only where gas is cheap; where gas is dear (mostly 2021-22, when coal was also short) the gap barely moves. It would also lower the engine's short-run response of coal-and-gas CO2 to the gas price from about 0.26 to 0.16, and the published estimates must be checked before going that way. `results.md`, HI-1, has the figures.
- **HI-2 (monthly, 2019-2024), reported.** Each month's peak is now held to the year's (`peakFactor`), which removes the capacity shortfalls the engine showed every July and August; summer coal falls a little further below measured, so the gap is slightly wider (8.3% average). Month by month, the gap follows the gas-to-coal price ratio: the engine runs about 12% too little coal-and-gas CO2 when gas is cheap and about 8% too much when gas is dear, and the price ratio explains 89% of the monthly gap. The coal stockpile adds nothing once prices are counted. So the engine's coal-gas switching is still too strong in both directions. One candidate cause, coal bought under take-or-pay contracts, improved the fit in a test but needed an implausible running cost for coal; it waits on evidence about contract terms. The full-engine history (vehicles, buildings and building decisions from 2015) is still to be built.
- **EP-3 (Espen's EPS generation by type, November 13, 2026), reported.** Both models start 2030 with about the same coal under current policies (about 530 TWh), so EP-1's difference is the response. With the price, this engine cuts coal 88% in the first year and EPS 51%: the engine's first-year switching is likely too strong (HI-1, HI-2). By 2035 both add about the same wind and solar; EPS cuts further because it fits carbon capture to existing coal and gas plants (about 760 TWh in 2035). Run on EPS's retrofit terms as read from its code, unverified until checked against Espen's uploaded EPS documentation (95% capture, no capacity lost, one year to build, every plant eligible), this engine's retrofitted plants make about the same (768 TWh) and its 2035 cut overshoots EPS's: those terms explain the 2035 gap. On EPA's costs and the capture achieved so far, no retrofit pays under the plan's price before coal retires (see "Carbon-capture retrofits" below and in `results.md`). *(This note was dropped by mistake in #360 and is restored here.)*
- **Fast in power, slow elsewhere.** PR-2 says the engine cuts slowly in its first decade, and EP-1 that it cuts more than EPS by 2030; both hold, by sector. With the price alone in 2030, power plants make about 390 Mt of the engine's roughly 440 Mt energy cut; transport and industry make about 45 Mt between them. Most taxed emissions are outside power, so receipts stay high (PR-2), while the power response is quick. That power response is likely still too strong in the first years: from 2020 to 2021, as gas prices doubled, measured coal power rose 16% while the engine's roughly doubled, and annual data cannot separate fleet behavior from the coal shortage.
- **EP-1 and EP-2 (Espen's EPS runs of the plan's settings, November 13, 2026), reported.** With the same carbon price, the two models cut about the same amount over 2030-2050 but on different curves. This engine cuts more by 2030 (coal-to-gas switching in power, likely still too quick); the simulator's cut comes mostly in 2031-2035, as plants retire and new ones are built, and then levels off, while this engine's keeps growing. The package run shows the same pattern: the simulator's cut is larger through 2040 and this engine's larger by 2050. The settings could not be matched exactly; `results.md` lists the differences.
- **Against the Energy Policy Simulator, run by Espen (November 13, 2026):** BL-3 passes. Current policy cuts net greenhouse gases 13% from 2025 to 2035 here, and 10% in the simulator's Current Policies pathway. PK-1 is reported, not tested: the simulator's US Climate Action package cuts 43% by 2035 against the decided set's 29%. It is a far wider package with no carbon price: more industrial, building, land and carbon-removal measures. The gap shows what such measures would have to add toward point 1's goal.
- **Reported, not pass or fail:**
  - CR-1, the credits' effect against the IRA comparisons. The comparison is not like for like, and the reason is stated.
  - EM-1, the closeness score.
- **Passed in direction or shape:** BI-1, the credits' effect on prices, and DI-1, who comes out ahead.
- **BK-2 passes.** It checks memo 1's proportional arithmetic against a run.

## Limits

- **Carbon-capture retrofits are a sensitivity, not part of the plan's runs.** The option is in the engine and its inputs are sourced, but the decided set runs without it (`ccs_retrofit_scale` 0) until the clean power dossier adopts a retrofit policy. At the research-based limits (scale 1) none pays under the plan's price: on EPA's costs and 75% capture in operation, a coal retrofit pays only above about $140 a ton expected, after the power plant standards retire unabated coal in 2040. At design capture (90%) and twice the limits, about 30 GW of combined cycles are retrofitted by 2050. If 45Q stacks on the price (`q45Stack`), retrofits start from 2031: at 90% capture and twice the limits, about 6 GW of coal and 13 GW of combined cycles are online by 2040. The owner's decision still compares a retrofit with running unabated, not with the forced retirement the standard imposes, which would favor coal retrofits a little more.
- **One national power market, no hours or regions.** Fuel prices now vary by plant (HI-1), but there is still one grid: no transmission limits between regions, no hours. The clean standard's feasibility rests on the engine's grid-access limit, not on a regional build (SRC-0077, v2.4).
- **Structural uncertainty is larger than the Monte Carlo bands.** The bands vary inputs only. Published models differ by more for the same policy.
- **Industry's covered share is assumed.** The memo 1 B coverage applies it as one blended price, not facility by facility. The `ind_lo` and `ind_hi` rows show its range.
- **The credit cost is the engine's estimate.** The power credits now follow CLI-1A.02's step-down (until November 14, 2026 they stopped at the engine's emissions trigger, the gap clean power's re-review noted in R-6). The cost still runs above the booked CLI-1 (`results.md`, "For the budget model's booking step"). It is a cross-check, not a score.
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
