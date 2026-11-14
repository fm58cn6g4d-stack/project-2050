# Energy and climate model: survey of trusted models (M4, part 1)

Role: part 1 of step M4 (`DEC-2026-11-13-09`). It surveys the validated energy and climate policy models that are widely used for U.S. policy analysis, says what each can teach `MOD-energy`, and ends with the recommended design of `models/tools/energy/`. Status: draft for review, November 13, 2026. Part 2 builds the model to section 4's design unless the lead or the reviewer stops it.

Sources are cited by `SRC-` ID (`library/catalog.csv`). Each model's documentation is analysis by a publisher with a stake, and the stake is named. Analysis by the second Trump administration's agencies (2025 on) is flagged and weighed with extra skepticism (`DEC-2026-10-30-01`). Section 2.1 rests on the simulator's public documentation and on files Espen uploaded on November 13: the model's Read Me [SRC-5043], the Climate Ambition scenario guide [SRC-5044], the En-ROADS technical reference [SRC-5045] and the C-ROADS paper [SRC-5046]. None of the uploads carries an open license, so they stay out of the repository; only citation rows and short quotations come in.

## 1. What the model has to answer

Clean power's decided set (`DEC-2026-11-13-06`, `-07`; `dossiers/clean-power/3-design.md` and memos) needs, year by year from 2029 to 2050, and against the January 2029 current-law baseline (`charter/STANDARDS.md`, "Time frame"):
- **emissions:** energy CO2 by sector, process CO2, methane and the other gases, against 2005 and against the 2029 baseline (point 1's goals);
- **receipts:** the carbon price on power plants and large industry with the border adjustment (memo 1 B), the methane fee (point 3), the clean electricity standard's capped payments (memo 3 B), and the income and payroll tax offset on each (24.4%, `DEC-2026-11-12-08`);
- **outlays:** the credits as they step down (memo 2 B), and the 80/20 split of the price into the Climate Dividend and the transition share (points 5-6);
- **prices and bills:** retail electricity and fuel prices, and household bills and dividends by income (memo 5 B and the D3 test);
- **the rebuilt pricing export:** the climate pricing export's 25% offset replaced by the adopted rate (board "Known gaps", #289).

These are the questions of a fiscal and distributional model with a physical core, not of an energy-system optimizer. That shapes what follows (`DEC-2026-11-13-08`: use existing machinery and simplify).

## 2. The models

### 2.1 Energy Policy Simulator (EPS), U.S. edition, Energy Innovation

- **What it answers.** The emissions, fuel use, costs, cash flows by actor, jobs, GDP and health effects of a chosen package of policy levers against a business-as-usual path, economy-wide and by state [SRC-5011] [SRC-5012].
- **Structure.** A system dynamics model in Vensim, single region (with state editions), annual steps to 2050; version 4.0.7, October 1, 2026 [SRC-5011]. Its calculation order is fuels and prices, then the demand sectors (transportation, buildings, industry including agriculture), then electricity, district heat and hydrogen supply, then land use, then totals, health and cash flows [SRC-5012].
- **Mechanisms.**
  - *It does not build its own baseline.* "The EPS does not construct a future business-as-usual (BAU) or reference scenario. Instead, it uses a BAU scenario … as input data", except in electricity and transportation, where the BAU passes through the decision logic [SRC-5012]. Its BAU comes mainly from EIA's AEO (transport rebased to AEO2026 in version 4.0.6) [SRC-5011].
  - *Stock turnover.* Vehicles and building components are vintaged stocks, so "an efficiency improvement in an early year will result in fuel savings in all subsequent years, until the improved vehicle/building component/etc. is retired"; industry has no fleet stock and phases reductions in with costs [SRC-5012].
  - *Vehicle choice.* A logit on cost per mile (upfront cost, discounted operating cost and a shadow cost for EV barriers), with shareweights calibrated to historical sales, then state sales minimums [SRC-5014].
  - *Electricity.* Not a linear program: 24 plant types with vintages, six seasonal 24-hour timeslices, capacity built when profitable or needed for reliability, multi-stage dispatch giving hourly prices; recent versions add effective load-carrying capability, soft and hard build caps, a combined renewable or clean standard with a credit price, data-center load and a cost-of-service retail rate pathway alongside market rates [SRC-5013] [SRC-5011].
  - *Prices.* Fuel prices are inputs; the model "does not endogenously update the price of non-electricity fuels in response to supply and demand changes" [SRC-5017].
  - *Carbon price.* Set by sector, applied to each fuel's CO2e content; if industry is priced, its process emissions are too unless excluded; revenue can be left to government, netted against package cost, or routed through the input-output model to spending, deficits, household taxes (including a climate dividend), payroll or corporate taxes [SRC-5015] [SRC-5019]. The model's distribution files (Espen's upload) show the design switches the carbon price carries: a border adjustment that can be turned off, a rebate of the tax on exported products, exemptions for non-CO2 gases and for each industry's process emissions, and a separate allocation of carbon tax revenue [SRC-5021]. These are the same choices memo 1 B makes, so the model needs each as a switch too.
  - *Outputs beyond emissions.* Cash flows by actor (government, industry, consumers, energy industries); jobs and GDP from a BEA-based input-output model [SRC-5019]; premature deaths from reduced-form incidence-per-ton factors for fine particles only, which its documentation calls possibly conservative [SRC-5018].
- **Validation.** EPS was one of six economy-wide models in the nine-model comparison of the Inflation Reduction Act (Bistline et al. 2023) [SRC-5022], in the EMF 37 net-zero study [SRC-5024], and in the 2026 review of the IRA and the One Big Beautiful Bill Act (P.L. 119-21) [SRC-4479]. Its developers cite review by national laboratories and universities, with the note that listing a reviewer "does not imply endorsement" [SRC-5011]; that is invited expert review, not a published validation. No back-cast of past outcomes was found. Intercomparisons compare models with each other, not with outcomes.
- **Publisher and stake.** Energy Innovation Policy and Technology, a San Francisco firm whose mission is "to mitigate climate change by promoting the most effective and equitable energy policies"; it builds "Climate Ambition" packages of the policies it favors and publishes analyses of them with its own model [SRC-5011] [SRC-5020]. Records describe it as an LLC; funders are not disclosed on the pages read. Its July 2026 analysis of federal policy changes since January 2025 ($460 more per household for energy in 2035) is the developers' own run, not peer reviewed [SRC-5020].
- **License and openness.** The model is "released under the GNU General Public License version 3 (GPLv3) or any later version"; Vensim is not covered [SRC-5016] [SRC-5021]. Its input data are public sources, shipped with citations. The documentation text carries no open license.
- **The Climate Ambition scenario** (July 2026), Energy Innovation's illustrative federal-and-state package with "federal policies begin phasing in in 2029", is the nearest published package to clean power's set: it restores the IRA's clean electricity, manufacturing, vehicle, hydrogen and capture credits and extends them through 2050, with a 100% clean energy standard and "a target of 80% clean by 2035", methane fees and rules, building and vehicle standards, and carbon removal; it has no carbon price [SRC-5044]. The guide gives settings, not results.
- **The developers' own view of calibration.** The Read Me says to compare outputs with other models of the same region, and: "the EPS results need not match other models. But significantly different results can sometimes indicate an issue with input data or other assumptions. At a minimum, it is useful to understand why the EPS produces results that differ" [SRC-5043]. That is the benchmark standard this model adopts (section 3). It works internally in 2012 dollars, grams and Btu.
- **What Project 2050 can use.** Methods, not code: porting EPS code would make our model a derivative work under the GPL (lead's note, November 13). We re-implement in our own code and cite each borrowed method to the EPS documentation in the model card. The methods worth taking (section 4): an external baseline from AEO; vintaged stocks; logit technology choice calibrated to historical sales; a carbon price by sector on CO2e content with process emissions; cash flows by actor; a clean standard with a clearing credit price; a cost-of-service retail rate; health by incidence per ton. Its OBBBA-era results are a benchmark (section 3), and the Climate Ambition package, if Energy Innovation publishes its results or part 2 can run the public web tool on it, is the only outside run close to the decided set.

### 2.2 EIA's National Energy Modeling System (NEMS) and the Annual Energy Outlook

- **What it answers.** EIA's projections of U.S. energy supply, demand, prices and energy CO2 to 2050 under current law, with side cases [SRC-5028].
- **Structure.** Thirteen-plus modules solved to an annual market equilibrium: demand (residential, commercial, industrial, transportation), conversion (electricity, liquid fuels, hydrogen), supply (oil, gas, coal, renewables) and a macro module from S&P Global [SRC-5028]. Demand modules vintage equipment stocks and choose equipment on capital and operating cost; short-run price elasticities are small (EIA's residential documentation gave −0.15 for fuels and −0.30 for electricity in AEO2022). The electricity module plans capacity and dispatches with linear programs and sets retail prices by cost of service in regulated regions and by marginal cost plus capacity and wires charges in competitive ones.
- **Validation.** EIA's own retrospective reviews are the only systematic comparison of a U.S. energy model with outcomes. The September 2022 edition, covering AEO1994 to AEO2022, put the average absolute error of total energy CO2 projections at 14.6%, overestimated 79.8% of the time; the gas price to power plants at 46.9% [SRC-5002]. The March 2026 edition dropped the error table for a data file [SRC-5003]. Reference cases hold law fixed, so these errors combine forecasting error with later changes in policy. NEMS also took part in EMF 32 [SRC-5009] and, as Rhodium's and DOE's variants, in EMF 37 and the IRA comparisons [SRC-5025] [SRC-5022].
- **Publisher and stake.** EIA, the statistical agency of the Department of Energy, independent by statute. AEO2026 (April 8, 2026) is the first to include P.L. 119-21, with some provisions left out for want of guidance or model detail [SRC-5000]; it renamed the reference case the "Counterfactual Baseline" because it was misread as EIA's preferred case, and its administrator's foreword is promotional in tone. It is second-Trump-administration analysis; its data series are weighed as data.
- **Which AEO2026 case fits the 2029 baseline.** The Counterfactual Baseline keeps EPA's 2024 power plant rule (its partial repeal came after the cutoff) and EPA's 2024 vehicle rules, which have since been rescinded; the **Alternative Electricity–Alternative Transportation Combination case** drops both [SRC-5001]. That combination case is the nearest public projection to the January 2029 law (see the inherited baseline in `dossiers/clean-power/3-design.md`).
- **License and openness.** Public domain; the NEMS code is on GitHub (EIA says Apache 2.0), but running it needs commercial solvers and about 11 hours a run [SRC-5028].
- **What Project 2050 can use.** AEO2026's tables as the baseline's input data (EPS's approach), its prices, and its sector CO2; the retrospective's 14.6% as an honest floor on how uncertain any baseline is.

### 2.3 NREL's ReEDS and the Standard Scenarios (now the National Laboratory of the Rockies)

- **What it answers.** Least-cost capacity expansion and dispatch of the contiguous U.S. power sector to 2050, with transmission, regional resource supply curves and reliability [SRC-5029].
- **Structure.** A linear program over 134 balancing areas with representative and stress periods; costs from the Annual Technology Baseline [SRC-5029]. Cambium, built from it, gives hourly marginal emission rates.
- **Validation.** No comparison with outcomes was found. It took part in EMF 32 coupled to MIT's USREP and in the IRA power-sector comparison [SRC-5023].
- **Publisher and stake.** A DOE national laboratory, renamed by DOE on December 1, 2025; its mission statement changed with the administration. The latest Standard Scenarios (December 2024) predate P.L. 119-21 [SRC-5030].
- **License and openness.** Code BSD-3-Clause (needs GAMS and a commercial solver); reports state no license, so they are cited, not saved.
- **What Project 2050 can use.** Cost and build-rate data (ATB, already partly in the carbon model) and, for benchmarking the power sector, the Standard Scenarios' clean-standard runs, with the caveat that they assume the IRA.

### 2.4 GCAM and GCAM-USA (PNNL, Joint Global Change Research Institute)

- **What it answers.** Long-run energy, land, water and emissions paths for 32 world regions, with the 50 states and DC in GCAM-USA [SRC-5033].
- **Structure.** Dynamic-recursive partial equilibrium in five-year steps with vintaged capital and logit market shares; a macro module since version 9.0; version 9.1, June 2, 2026 [SRC-5033].
- **Validation.** Published hindcasts are mixed: a buildings hindcast from 1990 to 2010 slightly overestimated heating demand and missed plug-load growth; a land-use hindcast missed biofuels because it "did not anticipate biofuels policies". It took part in the IRA comparison and the 2026 review [SRC-5022] [SRC-4479].
- **Publisher and stake.** A DOE laboratory community model, open to all users; the University of Maryland runs a variant for its subnational climate work.
- **License.** ECL-2.0 (Apache-derived).
- **What Project 2050 can use.** Little directly: five-year steps and global scope are wrong for a budget model. A benchmark through the 2026 review's OBBBA rows.

### 2.5 REPEAT Project (Princeton ZERO Lab and Evolved Energy Research)

- **What it answers.** Rapid evaluation of federal energy and climate bills as they move: emissions, energy spending, investment, jobs and air pollution, downscaled to states [SRC-4478].
- **Structure.** Evolved Energy Research's EnergyPATHWAYS (demand-side stock rollover) feeding RIO, a linear program that co-optimizes supply investment and hourly operation across 27 zones; RIO has "no income effect, no price-induced change in service demand, and no macroeconomic feedback" [SRC-5041].
- **Validation.** In the 2023 IRA comparison (RIO-REPEAT gave the largest IRA effect of the six economy-wide models: 53% below 2005 in 2035 against 37% without the act) [SRC-5022] [SRC-4479]. Its reports say they are not peer reviewed [SRC-4478].
- **Publisher and stake.** A Princeton lab and a private consultancy, funded by the Hewlett Foundation, publishing quickly on live bills.
- **License and openness.** EnergyPATHWAYS is MIT-licensed; RIO's code is not public. The OBBB report says "All data and graphics in this report are available under CC BY license" (version unstated) [SRC-4478].
- **What Project 2050 can use.** Its OBBB results as a benchmark for the credits layer: about 190 Mt more emissions in 2030 and 470 Mt in 2035, and about $165 and $280 more per household per year in energy spending, against executive repeal alone [SRC-4478]. Its transmission-limited build rates are already in the carbon model's pipeline (`legacy/sources/climate-carbon-dividend-model-notes.md`, v2.4).

### 2.6 Rhodium Group: RHG-NEMS and Taking Stock

- **What it answers.** An annual current-policy emissions outlook with a range of scenarios, quick analyses of enacted laws, and preliminary emissions for the past year each January [SRC-4475] [SRC-4473].
- **Structure.** Rhodium's own modified copy of NEMS, extended to all gases and land use; the modifications are not published [SRC-4474] [SRC-4476].
- **Validation.** In EMF 32, the IRA comparison and the 2026 review [SRC-5022] [SRC-4479]. Its January estimates are later replaced by EPA's inventory; no published back-test of them was found.
- **Publisher and stake.** A for-profit research firm serving governments, investors and philanthropies; it states its ranges "represent distinct emissions pathways rather than confidence intervals".
- **License.** All rights reserved; cited only.
- **What Project 2050 can use.** The current-policy range as the baseline's main independent benchmark: Taking Stock 2025, after P.L. 119-21, 26-35% below 2005 in 2035 [SRC-4474] [EV-CLP-112]; its OBBBA analysis, 27-44% in 2035 and household bills $78-192 higher [SRC-4477] [EV-CLP-113]; Taking Stock 2026 [SRC-4475].

### 2.7 EPA's Integrated Planning Model (IPM) and the social cost of greenhouse gases

- **IPM: what it answers.** Least-cost capacity expansion, dispatch and pollution controls for the power sector in 67 U.S. regions; EPA's tool for power plant rules [SRC-5008].
- **Structure.** A linear program; demand fixed between baseline and policy cases [SRC-5010]. A separate EPA workbook (2019) turns its results into retail prices.
- **Validation.** No comparison with outcomes found; an IPM run by NRDC was in the IRA power-sector comparison [SRC-5023].
- **Publisher and stake.** ICF's proprietary model, run for EPA; EPA publishes inputs, run files and documentation. The 2025 Reference Case (February 2026) adds P.L. 119-21 and large data-center loads, with phrasing about "Super Intelligence applications" [SRC-5008]; the September 2026 analysis for the partial repeal of the power plant standards does not value climate effects [SRC-5010]. Resources for the Future finds forgone climate benefits outweigh its cost savings by about $1.5 trillion through 2050, and the center-right American Action Forum notes its savings grew by an order of magnitude from proposal to final while health and climate costs were dropped [SRC-5031] [SRC-5032]. Second-Trump-administration analysis: used only as a data point on what the administration assumes.
- **Social cost of greenhouse gases.** EPA's 2023 report, after external peer review, put the 2020 social cost at $190 a ton of CO2, $1,600 a ton of methane and $54,000 a ton of N2O at a 2% discount rate (2020 dollars) [SRC-5006]. Executive Order 14154 disbanded the interagency group and withdrew its estimates [SRC-4732]; OMB told agencies they "should not monetize the impacts from such emissions" [SRC-5007]. RFF's GIVE model (MIT license) is one of the 2023 report's three damage modules, so the two are not independent.
- **What Project 2050 can use.** IPM: nothing directly. The social cost: the 2023 values as a labeled valuation of avoided emissions, reported beside tons, not booked.

### 2.8 Carbon-tax models: RFF, the Tax Policy Center, CBO, JCT and Treasury

- **RFF's E3 model** (Goulder and Hafstead): a computable general equilibrium model of the U.S. with 35 industries and a detailed tax system, behind RFF's Carbon Pricing Calculator; in EMF 32; its calculator covers energy CO2 only, on an AEO2019 baseline [SRC-5034]. Its household work finds an equal rebate leaves every quintile but the top better off [SRC-4620]. Nonprofit, takes no positions on bills; content CC BY-NC-ND 4.0, which forbids derivatives, so it is cited.
- **Tax Policy Center** (Rosenberg, Toder and Lu, 2018): microsimulation on Rhodium's NEMS prices; at about $50 a ton, burdens of 2.1% of pretax income in the bottom quintile and 1.1% in the top; a per-adult rebate more than offsets the burden for low and middle incomes [SRC-5035].
- **CBO and JCT.** CBO's December 2024 option: $25 a ton rising 5% a year above inflation raises $919 billion over 2025-34, net of the income and payroll tax offset [SRC-5036]. The offset: JCT "historically … assumed an income and payroll tax offset of 25 percent" [SRC-5005]; CBO puts it at 21-25% in recent years [SRC-2453]; Espen adopted 24.4% (`DEC-2026-11-12-08`). CBO's 2013 report on a carbon tax remains its full treatment [SRC-4621].
- **Treasury's Office of Tax Analysis** (2017): a carbon tax distributed to sources of income, less regressive than TPC's and CBO's, with a per-person rebate raising the poorest decile's after-tax income by almost 9% [SRC-4615].
- **Validation.** These are accounting and incidence models; their checks are against each other. Ex post, prices have cut covered emissions modestly (`dossiers/clean-power/2-what-works.md`).
- **What Project 2050 can use.** The conventions, not new numbers: gross receipts less the adopted offset; the dividend as a per-adult transfer; incidence through prices of consumption and sources of income (the household model already holds both keys). CBO's option is a revenue benchmark on its own price path.

### 2.9 Model intercomparisons: EMF 32, EMF 37 and the IRA comparisons

- **EMF 32** (Stanford Energy Modeling Forum, 11 teams, 2018): carbon taxes of $25 or $50 from 2020 rising 1% or 5% [SRC-5009]; "the vast majority of the reductions occurring in the electricity sector", and "beyond 2030 … model uncertainties are too large to make quantitative results useful" [SRC-5026]; a $50 tax rising 5% cut CO2 26-47% below 2005 by 2030, with first-year revenue about $200 billion at $50 (summary by a steering committee member) [SRC-5027]. Its baseline (AEO2016) is stale; its range across models is the useful part.
- **EMF 37** (16 teams, 2023-25): net-zero CO2 paths; reference-case CO2 change 2020-2050 "from a 15% increase to a 56% decrease" [SRC-5025]; and the synthesis: "each dollar per metric ton carbon price leads to a 0.06 % to 0.31 % reduction in economy-wide CO2 emissions" [SRC-5024]. That per-dollar range is the single most useful benchmark for a carbon price's effect.
- **IRA comparisons**: nine models put the IRA at 43-48% below 2005 by 2035 [SRC-5022]; eleven put power CO2 47-83% below 2005 in 2030 [SRC-5023]; the 2026 review puts the IRA at 39-48% in 2035, no IRA at 27-35%, and P.L. 119-21 at 31-37% [SRC-4479] [EV-CLP-115]. The review's authors are largely the modeling teams it reviews.

### 2.10 Climate response: FaIR, MAGICC and the carbon budget

- **FaIR** (Apache-2.0) and **MAGICC7** (free after registration; binary CC BY 4.0, probabilistic parameters CC BY-NC 4.0) are the reduced-complexity models IPCC's Working Group III used to classify scenarios [SRC-5038] [SRC-5039].
- **Is a temperature step needed?** Not for any decision in the clean power set. For context, IPCC's best estimate is 0.45°C per 1,000 billion tons of cumulative CO2 (likely 0.27-0.63) [SRC-5037], so a billion tons avoided is about 0.0005°C. That is enough to report a single country's CO2 change to first order; it does not cover methane or timing, which would need FaIR. Recommendation: report cumulative tons and the TCRE conversion with its range; add FaIR only if a public brief needs methane's warming in degrees.

### 2.11 Others the research turned up

- **EPA's greenhouse gas inventory** is the data the goals are measured on, and it has stopped: EPA did not publish the 1990-2023 or 1990-2024 inventories (`EV-CLP-103`); the 1990-2023 report surfaced through a FOIA request [SRC-4460] [SRC-4480]; the University of Maryland published an unofficial 1990-2024 inventory by EPA's methods in April 2026 [SRC-5040]. EIA's energy CO2 series continues: 4,904 Mt in 2025, up 2% [SRC-5004].
- **Climate Interactive's En-ROADS and C-ROADS** (Climate Interactive with MIT Sloan and Ventana Systems): globally aggregated system dynamics models in Vensim that return results in seconds, built for group exercises and "not intended as a tool for prediction"; a single world region, so they cannot give U.S. answers [SRC-5045] [SRC-5046]. Not used for numbers. Their testing practice is worth copying: En-ROADS starts from measured 1990 values and publishes its runs against measured history for energy, emissions and temperature; and it reproduces other models' scenarios by setting its own levers to match, then reports how close it comes with R² and the symmetric mean absolute percentage error [SRC-5045]. C-ROADS was built the same way, to replicate the large models' results transparently for negotiators [SRC-5046].
- **MIT CEEPR** used the EPS to find P.L. 119-21 keeps about two-thirds of the IRA's emissions cuts through 2035 [SRC-5042]: a third-party use, not independent of the model.
- **Espen's Carbon Dividend Model v3.4** (`models/tools/carbon/`, SRC-0077, SRC-0056) belongs on this list too. It is a structural model of the same kind as the EPS: a dispatch stack with a sourced build pipeline, vehicle cohorts with logit choice, heating turnover, industrial abatement, methane and fluorinated gases, a border model, a household module on the Consumer Expenditure Survey, 53 regression checks and 120-draw uncertainty bands. Its own validation found it responds more slowly than NEMS, REGEN and E3 in the first decade, mostly from financing cost and build speed (SRC-0077, v2.3). It was calibrated before P.L. 119-21's final shape and assumes the permitting deal in every case, which the clean power dossier no longer does.

## 3. What the survey says about benchmarks

Comparable runs exist for the baseline and for single instruments, not for clean power's package. The model card should benchmark:

| ID | Quantity | Benchmark | Why comparable |
| --- | --- | --- | --- |
| DA-1 | Energy CO2 by sector, 2025 | EIA, 4,904 Mt (revised to 4,916) [SRC-5004] | Measured data |
| DA-2 | Gross and net GHG by gas and source, 2023 | EPA inventory [SRC-4460]; UMD for 2024 [SRC-5040] | Measured data, inventory method |
| BL-1 | Energy CO2 path to 2050, no new policy | AEO2026 combination case [SRC-5001] | Same law, apart from the permitting package |
| BL-2 | GHG below 2005 in 2035, current policy | Rhodium 26-35% [SRC-4474]; the 2026 review's OBBBA rows 31-37% [SRC-4479] | Post-OBBBA current policy |
| PR-1 | Response to a carbon price | EMF 37: 0.06-0.31% per dollar a ton [SRC-5024]; EMF 32's range [SRC-5027] | A price alone, many models |
| PR-2 | Receipts on CBO's path | $919B net over 2025-34 at $25 rising 5% [SRC-5036] | Same price path and offset convention |
| CR-1 | Restoring the credits | The 2026 review's gap between IRA and OBBBA (about 8-11 points in 2035) [SRC-4479]; REPEAT's 470 Mt in 2035 [SRC-4478] | The credits layer alone |
| BI-1 | Household energy bills from the credits' repeal | Rhodium $78-192, REPEAT about $280, Energy Innovation $460 per household in 2035 [SRC-4477] [SRC-4478] [SRC-5020] | Same law change, opposite sign |
| DI-1 | Incidence of a carbon price with a per-adult rebate | Treasury, TPC, RFF: bottom quintiles ahead, top behind [SRC-4615] [SRC-5035] [SRC-4620] | Shape, not level |
| BK-1 | Legacy carbon model on the legacy design | `legacy/index/climate-carbon-model.md` (SRC-0056) | Reproduces the inherited numbers before changing them |

Two tests follow En-ROADS's practice [SRC-5045]: **HI-1**, a history run (the engine started from 2015's measured values with that year's policies and run to 2025, against EIA's measured energy CO2 by sector, with each year's actual degree days so weather is not mistaken for model error); and **EM-1**, emulation (the engine set to each benchmark's price path or policy and scored against its published path with SMAPE, so closeness is one comparable number across benchmarks).

EPS, REPEAT and Rhodium have no published run of clean power's set (power and industry priced, buildings and road fuels not, an 80%/100% standard and stepped-down credits), so they serve through the rows above, not as a package benchmark. Energy Innovation's Climate Ambition scenario includes an 80%-by-2035, 100%-by-2040 clean standard, but its guide publishes settings, not results [SRC-5044]; a run of it in the EPS web tool would be the one package-level comparison, and part 2 will try it.

## 4. Recommendation: the design of `models/tools/energy/`

**In one line:** an EPS-style policy simulator built around Espen's carbon model: the AEO2026 combination case as its outside baseline, the carbon model's tested sector engine for responses, and a new Python layer for the policy accounting, bills, distribution, benchmarks and the budget model's interface.

**Why not something larger.** The decisions need receipts, outlays, bills by income and emissions against a baseline, each within a range. A capacity-expansion optimizer (ReEDS, IPM, RIO) would answer finer power-sector questions none of the memos asks, at the cost of commercial solvers and runs no one could check. The intercomparisons show that model structure moves results more than any one model's detail: 34-80% for the same net-zero target in EMF 37 [SRC-5025], 26-47% for the same tax in EMF 32 [SRC-5027]. So the model should be simple, its baseline taken from a public source, and its uncertainty shown as the spread across published models.

**Why not a new model from scratch.** The carbon model already has what the EPS has in transportation, buildings, industry and electricity, calibrated to EIA's 2025 figures, with 53 regression checks. Rebuilding it would spend the step reproducing what exists. What it lacks is what the toolkit standard asks for: an external baseline, the decided set's coverage, a fiscal layer that matches the budget model's conventions, benchmarks with explanations and a run log.

### 4.1 Layers

1. **Baseline (input data, the EPS method).** Fuel use, prices and energy CO2 by sector from AEO2026's Alternative Electricity–Alternative Transportation Combination case (public domain, saved with `fetch_public.py`), adjusted for what it leaves out: the provisions of P.L. 119-21 that NEMS omits (its Table 1) [SRC-5000], and the January 2029 law's later dates. Non-energy gases from EPA's 1990-2023 inventory [SRC-4460], carried forward by source. The 2025 starting year is weather-normalized with NOAA's heating and cooling degree days [SRC-5047] [SRC-5048], because a cold or hot year moves building and power emissions (EIA attributes part of 2025's 2% rise to a colder winter [SRC-5004]); AEO projects normal weather, so the baseline starts from a normal-weather 2025. The engine is recalibrated so its no-policy path tracks this baseline (BL-1), not its own internal assumptions.
2. **Engine (the carbon model).** `models/tools/carbon/cfd-model.js`, run unchanged for its own design and extended only with options (the way Project 2050's earlier changes were made, each defaulting to the old behavior). It is Espen's own code, not GPL code. New options: memo 1 B's coverage (fuel to power plants and large industrial facilities, with their process CO2; no direct charge on residential and commercial fuel or road fuel); the permitting package as a switch (off in the baseline); the credit set's step-down schedule (memo 2 B); and the clean standard's second step (100% by 2040, already an option).
3. **Policy accounting (new, Python).** Year-by-year, in nominal dollars for the budget model:
   - receipts by instrument (carbon price, border adjustment, methane fee, the standard's capped payments), each with the 24.4% offset (`DEC-2026-11-12-08`), replacing the pricing export's 25%;
   - the 80/20 split, the Climate Dividend per adult and its cost on the dividend account;
   - the credits' outlays by year as they step down;
   - cash flows by actor (government, households, power producers, industry), the EPS's accounting convention.
4. **Prices and bills (new).** Retail electricity price by cost of service: the change in the generation cost per MWh (fuel, carbon price, standard credits, new build) passed through to the average residential price (EIA, SRC-4400), as the EPS's cost-of-service pathway and NEMS's regulated regions do. Household bills and the dividend by income: the carbon model's Consumer Expenditure Survey groups now; the household model (`models/tools/household/`) through its incidence keys for the D3 test.
5. **Outputs.** Emissions by sector and gas against 2005 and the 2029 baseline; receipts and outlays for the budget model's provision library; bills and dividends by quintile; avoided tons valued at EPA's 2023 social cost as a labeled side table; cumulative CO2 converted to temperature with the TCRE range; health from avoided power-plant generation by EPA's benefit-per-kWh, as the carbon model already reports (labeled, power plants only).
6. **Uncertainty.** The carbon model's Monte Carlo for input uncertainty, and the benchmarks' model spread for structural uncertainty, reported side by side.

### 4.2 Data sources

| Need | Source | Rights |
| --- | --- | --- |
| Baseline fuel use, prices, energy CO2 | EIA AEO2026, combination case, tables 2, 3, 8, 18 | Public domain |
| 2025 calibration | EIA energy CO2 2025 [SRC-5004]; Monthly Energy Review; Electric Power Monthly prices [SRC-4400] | Public domain |
| Non-CO2 and process emissions | EPA inventory 1990-2023 [SRC-4460]; UMD 1990-2024 as a check [SRC-5040] | Public domain; cited |
| Technology costs, build rates | NLR Annual Technology Baseline [SRC-4711]; LBNL queue [SRC-4410] (already in the carbon model) | Cited |
| Household spending | BLS Consumer Expenditure Survey 2024 (in the carbon model); EIA RECS 2020 [SRC-1935]; the household model's CPS | Public domain |
| Weather (heating and cooling degree days) | NOAA Climate at a Glance, contiguous U.S., 1895-2026 [SRC-5047] [SRC-5048] (Espen's upload, checked against the live series) | Public domain |
| Offset rate | `DEC-2026-11-12-08` (24.4%); CBO [SRC-2453]; JCT [SRC-5005] | Public domain |
| Valuation | EPA 2023 social cost [SRC-5006] | Public domain |

### 4.3 Benchmarks

Section 3's table, with HI-1 and EM-1. The status stays "working" until DA-1, DA-2, BL-1, PR-1 and BK-1 pass within stated tolerances and the others are reported with their differences explained, in the EPS Read Me's spirit: a result need not match, but every difference is understood [SRC-5043].

### 4.4 Interface

One command, `python3 models/tools/energy/run.py`, writes `results.json` and `results.md` for named scenarios (the 2029 baseline, the decided set, each layer added in turn, and the options memo 1 weighed), with a run log of model version, inputs and the engine's commit. The budget model reads the receipts and outlays through its provision library; the household model reads the carbon channel by group. Clean power's dossier tools already stand in for parts of this: `dossiers/clean-power/tools/coverage_read.py` reads memo 1 B's receipts from the carbon model's sector split, noting the model "has no switch for leaving buildings and non-road transport out", and `clean_power_path.py` does section 6's arithmetic against the booked rows with labeled working assumptions; `provisions.json` holds the provision IDs. Part 2 supplies the missing switch and publishes results those tools (owned by the clean power sessions) can read instead, keyed to the same provision IDs. Tests (accounting identities, boundary cases such as a zero price, and reproduction of the legacy run) join `bash .github/scripts/run-checks.sh`. Changing `models/data/inputs/carbon-parameters.csv` is Espen's decision: any proposed change goes in a separate tier-3 PR.

### 4.5 What it deliberately leaves out

- **Regional and hourly power detail, transmission flows and least-cost optimization** (ReEDS, IPM, RIO): one national market with a sourced build pipeline, as now. The standard's feasibility is judged against the benchmarks' build rates, not optimized.
- **Macroeconomic, GDP and jobs effects** (the EPS's input-output model, E3's general equilibrium): the budget model is not dynamic, and the offset is the convention for the tax interaction. Memo 7's worker counts come from the dossier's evidence.
- **Endogenous fuel prices and international markets.** Fuel prices are AEO inputs, as in the EPS; LNG exports and world oil are outside.
- **Land use and forests** beyond the inventory's sink held at its recent level; CLI-13 stays as booked.
- **Leakage beyond the border model's trade elasticity**, and the detailed border model the legacy notes park (SRC-0076).
- **A full health model:** power plants only, by benefit per kWh; no ozone, no other sectors.
- **Temperature beyond the TCRE conversion**, unless a public brief needs methane in degrees.

## 5. Open items

- **Espen's uploads** (the EPS Read Me, Climate Ambition guide and scenario and lever files, the En-ROADS reference, the C-ROADS paper and NOAA's degree days) are read and cited; the EPS files are GPL-3.0 and the documents carry no open license, so none is committed. NOAA's series are public domain and saved from NOAA's own address. Part 2 cites each borrowed EPS method to the online documentation pages, which the catalog lists.
- AEO2026's combination-case tables and its Table 1 of omitted P.L. 119-21 provisions are saved and read in part 2's first step.
- The permitting package's fate after November 16 sets whether the baseline's switch is on.
