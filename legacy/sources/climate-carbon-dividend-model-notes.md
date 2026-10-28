# Carbon Dividend Act of 2029: policy spec and model notes (v2, structural model)

Companion to the published page "Carbon Dividend Model". Source: `claude/cfd-model.js` (pure JS, no dependencies). `CFD.run(policy, levers)` returns `{pol, base}` year rows 2025-2050; `CFD.monteCarlo(policy, levers, N, seed)` returns N paired runs; `CFD.simulate(policy, world, pricePath)` is the core. Run with node; no rebuild needed. v1 was an emulator fitted to published runs and is superseded.

## Policy as drafted (model defaults)

- Fee: $40/t CO2e in 2030 (2025$), +$8/yr real ($80 in 2035, $200 in 2050).
- Ratchet: energy CO2 targets 35% below 2005 by 2035, 55% by 2050; extra +$4 step after a missed year. Targets set where the model says the fee alone delivers.
- Coverage: fossil CO2 (upstream); industrial process CO2 and N2O (~345 Mt); methane from oil/gas, coal mines, landfills (~380 Mt); HFC allowances at 20% of the rate; border charge on embodied carbon of EITE imports with export rebates. Optional: international bunker fuels (83 Mt). Excluded: agriculture (~585 Mt).
- Dividend: 90% of net receipts (after 25% offset), adult 1 / under-19 0.5 share, monthly, labeled, paid before the fee starts, untaxed. 10% to a Transition and Hardship Account.
- No EPA pause; state programs continue; 45Q stays, storage refund reduced by 45Q claimed.

## Model structure

- Power: 8 dispatch tranches (coal x3, gas CC x3, CT x2) plus gas CCS, stacked by running cost on a 40-block linear residual load-duration curve net of nuclear, hydro, wind, solar; curtailment above ~42-55% VRE share. Investment: logit over value-adjusted levelized cost for new energy, plus displacement builds when new wind/solar/CCS beats running fossil cost, subject to GW/yr limits; firm capacity shortfall filled by CT or storage. Coal retires on going-forward cost vs cheapest replacement.
- Light-duty vehicles: 36 age cohorts, logistic survival, EV share logit on price premium (battery cost), fuel savings over a payback period, and a network term on EV stock share. VMT and new-car mpg elasticities.
- Trucks: sales-share logit on cost per mile, 14-year turnover. Aviation and other: price elasticity.
- Buildings: 1/18 of fossil heating replaced per year; heat pump share logit on lifetime cost; short-run elasticity.
- Industry: efficiency elasticity; low-temperature heat electrification when heat pump beats boiler; CCS by source (NETL costs + T&S) when max(fee, 45Q) exceeds cost; refining tied to fuel demand.
- Non-CO2: EPA 2014 US abatement curves; coal mine methane tied to coal output; HFCs follow AIM Act cap.
- Feedbacks: electrification load into power demand; power cost into retail price.
- Expectations: investors use the 10-year average of the statutory schedule from 2029.
- Monte Carlo: 37 inputs, triangular ranges, 120 draws, 10th-90th percentile bands.

## Checks

- 2025 calibration: energy CO2 4,900 (EIA 4,904); power 1,485; coal 749 TWh (753); gas 1,820 (1,816); EV share 7.8%.
- No-policy path: power -34% 2025-2040 (Rhodium -24 to -48); transport -13% (-12 to -22); industry +1%; energy CO2 -22% by 2050 (EIA -11 to -38). Wind/solar build floor is calibrated to land here.
- Against published fee studies (their fee path, energy CO2 vs reference): NEMS $15: -5.2% in 2030 (published -12.1), -11.9% in 2050 (-16.7); NEMS $35: -9.6% (-16.7), -24.8% (-21.6); REGEN 2035: -7.1% (-25.5); E3: -10.2% in 2030 (-31), -14.0% in 2035 (-38). The model is less responsive in the first decade than all three.

## Default results (central world)

| Year | Fee | Energy CO2 below 2005 | No policy | Gross revenue | Dividend per adult |
|---|---|---|---|---|---|
| 2030 | $40 | 28% | 23% | $198bn | $422 |
| 2035 | $80 | 36% (34-38) | 28% | $351bn | $739 ($721-765) |
| 2040 | $120 | 45% | 32% | $461bn | $967 |
| 2050 | $200 | 54% (52-57) | 36% | $643bn | $1,336 |

2030-39 gross revenue $3.30tn, ~13% from sources other than fuel CO2. 19 Gt CO2e avoided by 2050. Net GHG 57% below 2005 in 2050 (no policy 37%). Coal generation zero by 2035; EV sales share 43% in 2050 vs 37% without the fee. Ratchet fires at least once in about half of Monte Carlo runs.

## Known limits / next steps

- One national power market; no regions, transmission or hourly weather.
- Bands are parametric only; structural uncertainty is larger (see comparison above).
- No macro; static household footprints; no hydrogen, long-duration storage, advanced nuclear or DAC.
- Assumed inputs to replace with sourced data: border trade embodied emissions (only steel 38 Mt is sourced), behavioral parameters, build limits, gas CC/CT split, industrial subsector shares, 2005 energy CO2, pre-2025 EV shares.
- Candidate upgrades: regional power (3-5 zones), AEO2026 tables, sourced EITE trade flows, complementary policies (vehicle standards, rebates from the 10%), agriculture module.

## v2.1: companion measures (added 2 Oct 2026)

- `permitYear` (policy option): permitting reform enacted that year, phased in over 4 years. If before 2029 it also applies to the no-policy path. Page default is 2027, modeled on the Bipartisan American Affordability and Jobs Act of 2026 (released 30 Sept 2026; Senate vote expected after the midterms; not yet law). Effects: wind/solar build limit +60% (Princeton REPEAT, unconstrained vs 1%/yr transmission); value-deflation slope -25%, curtailment threshold +5 points, build floor +25%, CCS build +50% (all assumed). Fossil provisions not modeled.
- `credits` (policy option, default off): 2029 climate bill restoring IRA credits from 2030. 30% ITC for solar and storage, $31/MWh wind PTC for 10 years, until power CO2 is at or below 383 Mt; for 10 years: $7,500 EV credit (eroding with inflation, 85% take-up), $0.08/mile truck credit, $2,000 heat pump credit, $15/kWh battery cost pass-through from 45X. Treasury cost is tracked in `credits` ($bn/yr).
- Current-law storage ITC through 2035 added to all runs.

Results with permitting passed by 2027 (page default), central world:

| Case | Energy CO2 below 2005, 2035 | 2050 | Dividend per adult 2035 | Credit cost 2030-39 |
|---|---|---|---|---|
| No policy | 28% | 39% | - | - |
| Fee | 41% (38-43) | 58% (55-60) | $693 | - |
| Fee + restored credits | 44% | 59% | $665 | $0.90tn |
| Fee, no permitting reform | 36% | 55% | $739 | - |
| Credits + permitting, no fee | 32% | 46% | - | $0.65tn |

Permitting reform avoids 1.8 Gt by 2050 with no other policy, 3.8 Gt on top of restored credits, and 4.8 Gt on top of the fee. RMI's 6.5 Gt for the 2024 bill's transmission provisions assumed the IRA credits in force, so 3.8 Gt is the like-for-like figure. Permitting reform is a complement: its value depends on how much clean build the other policies make economic. Credits lift the EV share of sales in 2035 from 24% to 36% but add only about 3 points to 2035 energy CO2 reductions.

## v2.2: EV feedback, broader credits, vehicle standards (2 Oct 2026)

- EV choice now includes a sales-share feedback (`evNetSales` 0.45, from Li, Tong, Xing and Zhou 2017: feedback explains ~40% of the tax credit's sales effect) alongside the stock-share term (`evNet` recalibrated to 0.42 so the no-policy path is unchanged: 29% of sales in 2040, 37% in 2050). The path is tipping-sensitive: evNet 0.5 gives 47% by 2050, 0.3 gives 25%.
- Restored credits broadened: effective ITC 38% and PTC $34 (adders, assumed), used-EV credit ($1,000 effective), charging credit as a lasting boost to EV utility (+0.03 logit per credit year), heat pump support $3,000 average, industrial credits (15% off capture and low-temperature electrification cost). Consumer credits run 10 years then 75%/50%.
- `standards` option: EPA vehicle rules as a floor on EV sales share (25% 2032, 50% 2037, 67% from 2040; trucks 30% by 2037). No compliance cost modeled.

Results (permitting by 2027, central):

| Case | EV share of sales 2035 / 2040 / 2050 | Energy CO2 below 2005, 2035 / 2050 | Credit cost 2030-39 |
|---|---|---|---|
| No policy | 22 / 29 / 37 | 28 / 39 | - |
| Fee | 25 / 34 / 44 | 41 / 58 | - |
| Credits only | 45 / 58 / 54 | 33 / 48 | $0.95tn |
| Fee + credits | 49 / 62 / 60 | 45 / 61 | $1.16tn |
| Fee + credits + standards | 49 / 67 / 67 | 45 / 62 | $1.16tn |

Finding: fee and credits overlap in power (the fee already saturates wind/solar build), so the credits' marginal value alongside the fee is in vehicles and heating. Fuel price alone moves EV share slowly, consistent with the EU (17.4% BEV share in 2025 despite much higher fuel taxes).

## v2.3: investment rule, validation, new outputs (3 Oct 2026)

- Wind/solar/CCS displacement builds now compare against each running fossil tranche (coal first) and close `dispSpeed` (0.3) of the displaceable energy per year, still capped by GW/yr limits. Replaces the earlier rule based on the average running cost.
- Sourced inputs updated: storage 43.6 GW at end-2025 (EIA); gas combined cycle ~290 GW (EIA); 2005 energy CO2 5,999 Mt (EIA: 2023 was 20% below 2005). Border trade figures are still placeholders.
- Validation: under "2022 conditions" (fcr 6.5%, build limits 90/35 GW, dispSpeed 0.5) the model gives -9.8% / -11.6% for NEMS $15 in 2030 / 2050 (published -12.1 / -16.7) and -13.8% / -21.2% for NEMS $35 (published -16.7 / -21.6). REGEN 2035: -13.7% vs -25.5%. So most of the gap with EIA's model is financing cost and build speed.
- Page adds a layer-by-layer table (current law, + permitting, + fee, + credits, + standards, with Treasury cost per added ton for credits) and a 2030-39 budget table.

Central results now (permitting by 2027): no policy 29% / 39% below 2005 in 2035 / 2050; fee 40% / 56%; fee + credits 42% / 60%. Dividend per adult $699 in 2035. Gross revenue 2030-39 $3.14tn, 14% from sources other than fuel CO2.

## v2.4: sourced build pipeline (3 Oct 2026)

Fixed annual build caps for wind and solar are replaced by a pipeline. Each year's build = min(what investors want, mature projects, industry capacity, grid access).

- Mature projects: stock of projects with interconnection agreements (LBNL Queued Up 2025: 408 GW; solar 68%, wind 19% of the queue), released over `icTime` 4 years (LBNL median request-to-operation), less `attr` 33% siting cancellations (LBNL developer survey). Refilled by new starts in proportion to what investors want.
- Industry capacity: starts at 45 GW/yr solar (EIA planned 2026: 43.4) and 12 GW/yr wind; grows 25% / 15% a year when over 85% used, shrinks 5% when under 60%.
- Grid access (wind + solar GW/yr) = gridBase 24 + 26 x transmission growth (%/yr) + 0.5 x retiring coal GW. The 26 GW per point comes from Princeton REPEAT (1% -> 36 GW/yr, 1.5% -> 49) and is consistent with DOE's Needs Study (+64% within-region transmission by 2035 for a high-clean case). gridBase is calibrated so 2026 matches EIA planned additions. Scarce grid access is shared by delivered energy.
- Transmission growth: 1%/yr base (Grid Strategies: 345kV+ miles fell from 1,781/yr in 2010-14 to 536/yr in 2020-23, 888 in 2024). Policy effects, all assumed magnitudes: permitting reform +1.0 point (back to the ~2% long-run average), credit bill with transmission ITC +0.3, fee +0.15; first-order lag 25%/yr.
- Permitting reform also cuts icTime by 1.5 years and cancellations by 5 points.
- Gas turbines: US additions capped at 12 GW/yr rising to 34 by 2031 (GE Vernova: 20 -> 30 GW/yr by 2030, sold out through 2030; US share assumed). Firm-capacity shortfalls beyond that go to storage.
- Standards toggle now also covers power plants: unabated coal out by 2040, new baseload gas needs capture from 2033.

Findings (central, permitting by 2027): with the fee, investors want 130-160 GW/yr of wind and solar from 2030; grid access allows 75-80. Grid access, not price, is the binding limit. Results: no policy 30% / 40% below 2005 in 2035 / 2050; fee 38% / 56% (10th-90th: 36-39 / 53-58); fee without permitting reform 36% / 52%; fee + credits 39% / 59%. Dividend per adult $724 in 2035. Ratchet fires in about a third of uncertain runs.

Validation under "2022 conditions" (cheap financing, no pipeline limits): NEMS $15: -11.3% in 2030 (published -12.1); NEMS $35: -18.4% in 2030 (-16.7), -21.4% in 2050 (-21.6). REGEN 2035: -13.5% (-25.5).

## v2.5: firm low-carbon build fix, nuclear, advanced hydro, grid program (3 Oct 2026)

- Bug fix: gas with capture was being allocated a share of new builds by cost alone, so wind and solar "won" that share even when the grid could not connect them. Firm options (gas CC, gas CCS, nuclear) now also compete for the wind and solar energy left unbuilt by the grid limit. With the fee, gas CCS reaches ~70 GW by 2040 (was ~4).
- Firm option ramps: CCS from 2032 at 2 GW/yr, nuclear from 2033 at 1 GW/yr, each +25%/yr when fully used; nuclear capped at 15 GW/yr (DOE Liftoff: 13 GW/yr by 2041). Reactor cost $13,000/kW falling 8% per doubling to a $6,800 floor. Current-law nuclear credit through 2035 included in all runs.
- `grid` option (federal grid build-out program): transmission growth +0.8 points, +15 GW/yr grid access from reconductoring, $12bn/yr for 2030-39. All assumed magnitudes; direction from Berkeley/GridLab.
- `nuclear` option (advanced nuclear, fusion and hydro program): 40% reactor ITC, 1.5-point lower financing rate, +8 points industry growth; $2bn/yr fusion R&D (no fusion power modeled); conduit hydro 1.41 GW (ORNL) built 2031-40; wave from 0.03 GW/yr growing 35%/yr, capped at 8 GW.
- Transmission investment credit in the credits bill now costed at $9bn/yr (assumed).

Central results (permitting by 2027): fee 39% / 57% below 2005 in 2035 / 2050 (10th-90th: 38-41 / 55-59), dividend $716 per adult in 2035. Fee + credits 40% / 60%. + grid program 42% / 60%. + nuclear program 42% / 62% (new nuclear ~80 GW by 2050, power CO2 68 Mt). + EPA standards 42% / 63%. Credits and programs cost ~$1.37tn over 2030-39 for the full package.

## v2.6: storage-credit timing, health benefit, who-pays, sensitivity, tests (3 Oct 2026)

- Fix: 45Q now follows its statutory schedule (plants online by ~2035 under current law, credit paid 12 years; extended ten years under the credits bill). No-policy gas with capture plateaus near 9 GW instead of growing to 36.
- Health co-benefit (page only): avoided coal and gas generation valued with EPA's 2024 benefit-per-kWh, using the Midwest figure (~8.5 c/kWh) for coal and California (~1 c/kWh) for gas as proxies. $0.53tn through 2050 for the fee case. Power plants only.
- New page outputs: what the average person pays by channel (driving, heating, electricity, everything else) against the dividend; one-at-a-time sensitivity table (top ten inputs for the selected case).
- `claude/cfd-tests.js`: 28 regression checks (2025 calibration, baseline within published ranges, accounting identities, expected policy behaviour). Run with `node cfd-tests.js` next to `cfd-model.js`.
- Tried and abandoned: a household module by income, region and rural/urban from the BLS Consumer Expenditure Survey. The tables could not be retrieved reliably, so nothing was built on them.

Central results unchanged for policy cases: fee 39% / 57% below 2005 in 2035 / 2050; dividend $716 per adult in 2035. No policy: 29% / 40%.

## v2.7: household module from BLS data, EIA comparison (4 Oct 2026)

- `claude/cfd-households.js` + `claude/cfd-cex-2024.json`: household module built on the BLS Consumer Expenditure Survey tables Espen supplied (2024 income deciles, quintiles, region, type of area; 2023-24 region by income). For each group: fee cost through gasoline, heating fuel and electricity (group spending x fee-driven price change x national fuel-use index), the remainder allocated by other spending, and a dividend of one share per adult and half per child. Replaces the 2012-14 footprint deciles on the page.
- Central fee case, 2035, per household: lowest income tenth +$298, fifth tenth +$30, highest tenth -$1,530; average -$212 (the 10% transition account and administration). Northeast -$286, Midwest -$153, South -$54, West -$319. Rural -$116 vs all urban -$165: rural households pay more for gasoline but are larger, so get more dividend.
- Limits: group means only (no share-who-gain); groups cut fuel use at the national rate; fuel oil/propane at an assumed 2.5 kg CO2 per dollar.
- Industry no-policy growth raised to 0.6%/yr (EIA AEO2026 Table 18 shows 0.7%/yr for industrial direct CO2).
- New check: standards on, fee off, against EIA AEO2026's central case (which keeps the EPA rules). Change from 2025, model vs EIA: 2040 power -46% vs -56%, transport -22% vs -26%, industry +6% vs +10%, buildings -9% vs -8%, total -22% vs -25%; 2050 total -30% vs -22%.
- Central results now: fee 38% / 55% below 2005 in 2035 / 2050 (10th-90th 37-40 / 54-57); no policy 28% / 38%; dividend $722 per adult in 2035.
- Still a placeholder: border-adjustment trade figures. The LBNL paper supplied covers computers, vehicles, machinery, pharmaceuticals and plastics, not the covered basic materials. Needed: EPA import emission factors (GLORIA, 2022) plus import and export values by commodity.

## v2.8: sourced border adjustment (4 Oct 2026)

- Border-trade placeholders replaced using files Espen supplied: BEA supply-use tables (2017 detail commodities scaled to 2022 by summary-sector trade growth), EPA Supply Chain GHG Emission Factors v1.3 (U.S. kg CO2e per 2022 dollar, by product), and EPA import emission factors from GLORIA (2022, summary sectors). Script: `border.py` logic summarised here.
- Covered products: iron and steel, steel products, alumina and primary aluminum, aluminum products, cement, lime and gypsum, glass, fertilizer, petrochemicals, other basic inorganic and organic chemicals, plastics and resins, pulp, paper, paperboard, refined petroleum products.
- Result: covered imports $313bn carrying 226 Mt CO2e at U.S. intensity, 410 Mt at EPA's foreign intensity (foreign/U.S. ratio capped at 2; raw ratios were 1.9 for primary metals, 1.7 chemicals, 1.6 paper, but 7.3 for nonmetallic minerals and 5.3 for petroleum products, which look like price-basis artefacts). Covered exports $371bn carrying 211 Mt. Model central: imports 320 Mt (range 226-410), exports 211 Mt (170-230). Largest import lines: steel 79 Mt, basic organic chemicals 96, refined products 46, plastics 38, aluminum 33. Refined products are a net export (rebate exceeds charge).
- Export rebates now shrink with U.S. industrial emissions. Origin-price credit (15%) is still assumed.
- Border revenue: $5.7bn in 2035 (10th-90th: $2.4-9.5bn), $55bn over 2030-39. Was $2.8bn in 2035 on the placeholders. Small against $345bn total, so headline results barely move: fee 38% / 55% below 2005 in 2035 / 2050, dividend $728 per adult in 2035.

## v2.9: border intensity ratios by product (4 Oct 2026)

- Dropped the uniform rule (EPA per-dollar import factor over U.S. factor, floored at 1 and capped at 2). It patched an artefact (a broad foreign sector compared with specific U.S. products), ignored that chemistry fixes emissions for cement and refining, and wrongly ruled out imports cleaner than U.S. output.
- Replaced with an ASSUMED foreign/U.S. ratio per product (low, central, high), set by judgment, not measured: steel mills 1.1/1.5/2.0; steel products 1.1/1.4/1.9; primary aluminum 0.6/0.9/1.4; aluminum products 0.9/1.2/1.7; cement, lime 0.95/1.1/1.3; glass 1.0/1.2/1.5; fertilizer and other chemicals, plastics 1.0/1.3/1.7; petrochemicals 1.0/1.2/1.6; pulp and paper 0.8/1.0/1.4; refined products 0.95/1.1/1.3.
- Result: covered imports carry 284 Mt CO2e (219 to 374); was 320 (226 to 410). Exports unchanged at 211 Mt.
- Border revenue: $3.3bn in 2035, $32bn over 2030-39 (was $5.7bn and $55bn). Net border revenue is small because export rebates nearly offset import charges. Headlines unchanged: dividend $723 per adult in 2035.
- A detailed border model is parked: see `claude/cbam-spinoff-notes.md`.

## v3.0: measures no longer go dead when stacked (4 Oct 2026)

Espen noticed that with every measure on and a high fee, the last measures listed added nothing (vehicle standards on or off did not move EV sales). Causes found and fixed:

- **Standards were hard floors** (`max(standard, market)`), so whichever was larger hid the other. Now a soft floor: `std + s*ln(1+exp((mkt-std)/s))`, s = `stdSoft` 0.06 (ASSUMED; stands in for carmakers differing in how close each is to the rule). The rule also makes new gasoline cars 1%/yr more efficient 2032-40 (`stdMpg`, ASSUMED). Same soft floor for trucks.
- **Bug: firm plants could not replace running gas on their own economics.** `dC` was computed and never used, so gas with capture and nuclear only got the wind and solar energy the grid could not connect. More grid access therefore meant fewer firm plants and higher 2050 power emissions. Fixed: firm plants displace running fossil tranches, costed at the hours that tranche actually runs (screening curve), so they do not replace peakers.
- Without that screening the fix overbuilt nuclear until fossil generation and the wholesale price hit zero by 2050. A hard 90% limit on wind and solar was tried and dropped as another arbitrary wall.
- **Grid program** now also raises the wind and solar share at which output starts being wasted (`gpCurt` 0.05, ASSUMED, phased 2031-37), as permitting reform already did.
- **Industry had no abatement beyond low-temperature heat and refinery capture**, a ceiling at high fees. Added high-temperature heat: `htShare` 0.45 of other industrial fuel use (Energy Innovation: 56% of process heat is above 200C), up to 80% abatable, adoption centred on `htCost` $150/t (Columbia CGEP: capture retrofits ~$60/t, blue hydrogen ~$120, green ~$370), at half the capture adoption rate.
- **Aviation had only a demand response.** Added low-carbon jet fuel: up to 10% at ~$220/t (ICCT, waste oils), up to a further 50% at ~$400/t (RFF, ethanol-to-jet $142-478/t).
- Ladder table gains a column: tons each companion measure avoids when it is the only thing added to the fee, beside its contribution in stacking order.
- Tests: 14 new checks that with everything on, at default and high fee, removing any one measure raises emissions, standards still raise EV sales, and some gas generation remains. 42 checks, all pass.

What is real, not a bug, and left alone: overlap between measures aimed at the same job; credits expiring around 2040, which stalls EV sales for a decade; EV buyers' weak response to fuel price (the price coefficient matches the literature elasticity of about -2 to -3); peaking gas plants with no clean fuel option, so power does not reach zero.

Central results (permitting by 2027): no policy 29% / 38% below 2005 in 2035 / 2050; fee 38% / 57% (was 55%); + credits 40 / 61; + grid 42 / 62; + nuclear 42 / 63; + standards 42 / 65. EV share of sales 2050: fee 44%, with credits 61%, with standards 69%. Dividend $721 per adult in 2035. Gross revenue 2030-39 $3.22tn.

Possible next steps: a clean fuel for peaking plants (hydrogen or long-duration storage); a vehicle rule that keeps tightening after 2040; compliance cost of standards.

## v3.1: tightening vehicle rules, long-duration storage, hydrogen, longer batteries (4 Oct 2026)

- **Vehicle rules keep tightening** (Espen's decision): cars 67% in 2040 rising to 100% of sales by 2050; trucks 30% in 2037 rising to 65% by 2050. Still a soft floor.
- **Batteries**: cost path already matched NREL 2025 mid (4-hour system $334/kWh in 2024, $178 in 2050). New: batteries lengthen from 4 to 8 hours by 2045 (`storDurEnd`, ASSUMED, range 4-12). Longer duration raises the wind and solar share before output is wasted, raises peak credit (0.6 to 0.8), and raises cost per kW (power equipment is 28% of a 4-hour system, NREL).
- **Long-duration storage** (`ldes`): a dispatch tranche with no emissions, energy-limited to wasted wind and solar output times round-trip efficiency (45% rising to 57%). Built where it beats a running gas tranche at that tranche's hours. Capex $2,200/kW falling to $1,500 by 2035 (DOE Liftoff: $1,900-2,500 today, $1,100 target; ASSUMED partly met; range 1,100-2,200). Supply 1 GW/yr in 2030, +30%/yr when fully used, max 15 (DOE: 3 GW/yr by 2030, 10-15 by 2035).
- **Hydrogen** (`h2`): after dispatch, gas plants swap to hydrogen where cheaper including the fee, up to supply (1 Mt in 2032 to 15 Mt in 2050, ASSUMED; range for 2050: 5-30). Price $5/kg in 2030 to $2.50 in 2050 (ASSUMED within IEA, ICCT, BNEF ranges; 2050 range 1.5-4.5). Restored credits take $3/kg off through 2040, phasing out by 2045; cost booked to the Treasury. Produced off-grid: no electricity demand in the model.
- Results (permitting by 2027), below 2005 in 2035 / 2050: no policy 29 / 40; fee 38 / 59; + credits 41 / 63; + grid 42 / 64; + nuclear 42 / 64; + standards 42 / 67. Fee case 2050: 62 TWh from long-duration storage (32 GW), 28 TWh from hydrogen. With credits, hydrogen reaches 136 TWh in 2040 then falls back when the credit ends. EV sales with standards: 69% in 2040, 99% in 2050. At $400/t with everything on, power emissions fall to about 2 Mt in 2050.
- Known weak points: long-duration storage arrives only in the 2040s because it may charge only from wasted output; hydrogen price and supply are assumed paths; hydrogen burned with credits flips back to gas when the credit ends.
- Tests: 45 checks, all pass.

## v3.2: 8-hour batteries the norm by 2040 (4 Oct 2026)

- Espen's view: new battery technology of 8 hours or more will dominate new grid installations by 2040. New batteries now lengthen from 4 hours to 8 by 2038 (`storDur38`, range 5-10) and to 10 by 2050 (`storDurEnd`, range 8-14). Was 8 by 2045. Cost still follows NREL's lithium-ion path; no extra saving from new chemistries.
- Effect is small: fee case 38.4% / 59.2% below 2005 in 2035 / 2050 (was 38.3 / 59.1); no policy 2050 40.6% (was 39.6). Reasons: wind and solar building is limited by grid access, not by wasted output, through the 2030s; and longer batteries leave less wasted output for long-duration storage to charge from (24 GW in 2050, was 32).

## v3.3: cheaper new battery chemistries (4 Oct 2026)

- Espen's view: the 8-hour-plus batteries will be new chemistries cheaper than lithium-ion. `storChem` 0.30: the energy part of a battery is 30% cheaper than NREL's lithium-ion path by 2040, phased in from 2030 (IEA: sodium-ion can cost 30% less than LFP; a 2025 bottom-up study in the Journal of Energy Storage finds only 3% by 2035; range 0.03-0.45). Developers spend the same and get more storage (attach rate scales with the saving).
- Results, below 2005 in 2035 / 2050: no policy 29 / 42 (2050 was 40.6); fee 38 / 59.4; everything on 42.5 / 67.6. Fee case 2050 power emissions 93 Mt (was 109); batteries 725 GW. Cheaper storage trims nuclear under the full package (117 GW in 2050, was 123); test threshold lowered to 110.
- "Crowding out": long-duration storage in this model charges only from wind and solar output that would otherwise be wasted. Longer batteries use that output first, leaving less for it.

## v3.4: old batteries replaced by longer ones (4 Oct 2026)

- Gap Espen spotted: longer batteries only applied to new additions; the 4-hour fleet stayed forever. Now one-eighteenth of the fleet wears out each year (18-year life, ASSUMED) and is replaced at the duration then on sale. Average fleet duration in the fee case: 5.2 hours in 2035, 8.4 in 2050 (was 7.2).
- Replacement spending is not charged to electricity prices (the model does not charge replacement for any plant type).
- Results: no policy 2050 43.0% below 2005 (was 42.1); fee 59.5 (was 59.4); fee-case power emissions in 2050 86 Mt (was 93).
