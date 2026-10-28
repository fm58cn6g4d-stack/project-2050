# Carbon Dividend Model: session brief and source accounting

Oct 27, 2026 · @espen

## Summary

This session built the Carbon Dividend Act of 2029 policy design and a structural simulation model of it (now v3.4), published as the "Carbon Dividend Model" artifact and saved to the Carbon Fee & Dividend project. The model covers a fee that starts at $40/t in 2030 and rises with a ratchet, a 90% household dividend, power, transport, buildings, industry and non-CO2 sectors, a border adjustment, and a BLS-based household module. It passes 45 regression checks.

Central results, with permitting reform passed by 2027, are emissions 38.4% below 2005 in 2035 and 59.5% below in 2050 for the fee alone, and about 42.5% and 67.6% with every package on. The dividend is about $720 per adult in 2035.

On sources: every figure in the model traces to a source listed on the artifact's Sources section, the project docs, or the files you uploaded. Most supporting files are in the project. The raw uploads (BLS, BEA, EPA tables), the border calculation scripts and the page build files live only in the session workspace, which is temporary. The searches this session ran were mostly snippet-level, so several new battery, hydrogen and jet-fuel parameters rest on search summaries rather than full documents. Section 7 lists those weak points.

## What was built

| Step | What it added | Why |
| --- | --- | --- |
| Research baseline | Survey of carbon tax, fee-and-dividend, cap-and-trade and border proposals, and of the modeling on them (RFF, Treasury, CBO, Rhodium, EIA, Brookings); methodological gaps | Starting point; saved as research-baseline-2026-10 |
| Policy design | Carbon Dividend Act of 2029: $40/t in 2030, +$8/yr real, ratchet, 90% dividend, border charge, 10% transition account | Designed for a 2029 Democratic trifecta |
| Structural model | Replaced an emulator with screening-curve power dispatch, vintage vehicle cohorts, industry, buildings and non-CO2 abatement curves | You asked for a real model, with revenue beyond energy |
| Policy toggles | IRA-style credits, permitting reform, clean standards | You asked for toggles; credits initially moved the needle too little |
| Build limits | Project pipeline, industry capacity and grid access cap how fast anything can be built | You asked for sourced build limits and policy effects on build speed |
| Grid, nuclear, hydro | Transmission credit, SMR and fusion incentives, advanced hydro, gas with CCS fix | Your direction to do more on grid and firm power |
| Household module | BLS CEX 2024 spending by decile, quintile, region and area type, so dividends can be compared with fee costs | Distribution of winners and losers |
| Border adjustment | BEA supply-use times EPA emission factors, then per-product intensity ratios (v2.9) | You questioned a uniform 2x foreign intensity cap |
| Dead-lever fix (v3.0) | Soft-floor standards and displacement of running plants, so stacked policies keep adding effect | You found levers going dead when stacked |
| Vehicle rule and storage (v3.1 to 3.4) | Tightening vehicle standards, long-duration storage, hydrogen, battery duration and chemistry paths, fleet replacement | Your direction on batteries, hydrogen and 8 to 10 hour storage |

## Where the model stands

**Policy.** The fee is $40/t CO2e in 2030 and rises $8 a year in real terms. It adds $4 a year after any missed target year, where the targets are 35% below 2005 by 2035 and 55% by 2050, and it freezes at 85%. It covers fossil CO2 upstream, process CO2 and N2O, methane, and HFCs at 20% of the rate, with a border charge and export rebates. Agriculture is excluded. The dividend pays 90% of net receipts after a 25% offset: one share per adult and half a share per child under 19. Ten percent goes to a transition account and 1.5% to administration.

**Structure.** Power dispatch uses a 40-block load duration curve with coal, combined-cycle, turbine and CCS tranches, plus energy-limited long-duration storage and a hydrogen swap-in. Investment follows a logit on value-adjusted cost plus displacement of running plants, capped by project pipeline, industry capacity and grid access. Transport has 36-age car cohorts with an EV choice model and a soft-floor vehicle rule. The model also has trucks, heat pumps, industry (low-temperature electrification, high-temperature heat, CCS), jet fuel switching, EPA non-CO2 abatement curves, an HFC cap, and a 120-draw Monte Carlo.

**Central results** (permitting by 2027), percent below 2005 in 2035 and 2050:

| Case | 2035 | 2050 |
| --- | --- | --- |
| No policy | 28.7 | 43.0 |
| Fee only | 38.4 | 59.5 |
| Fee plus credits | 40.6 | 63.1 |
| Fee, credits and grid | 42.2 | about 64 |
| Everything on | about 42.5 | about 67.6 |

In 2050, EVs are 44% of car sales under the fee alone, 61% with credits and 99% with the vehicle standard. The dividend is about $720 per adult in 2035. Gross revenue for 2030 to 2039 is about $3.2 trillion, of which about 13.5% comes from outside fuels. Border revenue is about $3.3 billion in 2035. Under the fee alone, 2050 has about 70 TWh of long-duration storage and about 25 TWh of hydrogen, and power emissions are 86 Mt.

**Checks.** The model is calibrated to 2025, compared with Rhodium and EIA ranges, back-tested against NEMS, REGEN and E3, and compared with AEO2026 Table 18 for the standards case. It has 45 regression checks, all passing, including a loop that tests every lever for dead zones at default and high fee.

## Research performed

**Caveat on the record.** This session was compacted once. The retained transcript shows 7 web searches and no page fetches, all from the storage, hydrogen and jet-fuel work. The earlier research (policy proposals, EIA, EPA, NREL, permitting, nuclear and so on) is documented only in the artifact's Sources section, the project docs and the code comments, not in a call log. Treat the topic list below as reconstructed from those, not from a search log.

| Topic | Main material | Depth |
| --- | --- | --- |
| Carbon fee and dividend proposals and scoring | C2ES tracker, CCL comparison, Columbia CGEP, RFF, EIA AEO2022 fee cases, Hamilton/NBER, Brookings EMF 32, CBO, Treasury OTA, Tax Foundation, CCL household study, Rhodium | Documents read for the baseline note |
| Border adjustment | RFF briefs on the Clean Competition Act and Foreign Pollution Fee Act; Global Efficiency Intelligence on steel imports | Summaries and briefs |
| Energy and emissions baselines | EIA energy CO2, generation and capacity, STEO, AEO2026; EPA inventory Table 2-1; FHWA VM-1 | Data tables |
| Power, nuclear, hydro, grid | Lazard LCOE 2025, DOE Advanced Nuclear Liftoff, ORNL conduit hydro, LBNL Queued Up and developer survey, Grid Strategies, DOE Transmission Needs Study, Berkeley/GridLab reconductoring, GE Vernova turbine backlog | Mixed; several summary-level |
| Permitting and credits | Senate permitting bill coverage, Princeton REPEAT, Third Way and RMI permitting analysis, Steptoe on repealed credits | Summaries |
| Vehicles | Cox Q4 2025 EV sales, ACEA EU share, BNEF pack price, a peer-reviewed EV feedback paper | Summaries |
| Storage, hydrogen, jet fuel (this stretch) | DOE LDES liftoff, NREL 2025 battery cost projections, ICCT hydrogen 2020, ICCT alternative jet fuels, a ScienceDirect HEFA cost paper | Search snippets only |
| Industry and non-CO2 | Columbia CGEP, Energy Innovation, NETL capture costs, CBO on CCS and 45Q, EPA marginal abatement curves | Summaries |
| Households and population | BLS CEX 2024 (8 files you supplied), CBO population outlook, Fremstad and Paul | Files read in full |
| Embodied carbon in trade | BEA supply-use (4 files), EPA supply-chain factors v1.3, EPA GLORIA import factors, a dataset-page PDF, an LBNL paper | Files you supplied |

The BLS pages fetched by the web tool returned numbers that did not match the real tables, so they were thrown out and you supplied the actual files instead. Direct downloads from eia.gov and bea.gov were blocked by the proxy and were not worked around.

## Sources incorporated

"In the project" means the source's content is carried by a saved project doc or the saved model code. The raw files themselves are in the project only where stated.

| Source | What it feeds | Where it lives |
| --- | --- | --- |
| BLS CEX 2024: deciles, quintiles, region, area type, region by income (8 xlsx) | Household spending by group, fee burden vs dividend | Extracted to cfd-cex-2024.json and cfd-households.js in the project; raw xlsx only in the session workspace |
| EIA AEO2026 Table 18 (CSV) | Industrial trend and the standards-only comparison | Model constants and tests; raw CSV not in project |
| BEA supply-use: Supply\_Summary, Use\_Summary, Supply\_Detail, Use\_SUT\_Detail | Sector output and use for border exposure | Results in border.json (not in project); method in cbam-spinoff-notes |
| EPA supply-chain factors v1.3 (CO2e CSV) | U.S. emission factors per product | Same as BEA row |
| EPA GLORIA import factors | Reference ratios only, after v2.9 | Ratios hard-coded in border.py (not in project); described in cbam-spinoff-notes |
| EIA energy CO2, generation and capacity, STEO Jun26, AEO elec cost performance | Baselines, plant costs, calibration | cfd-model.js and notes; page Sources |
| EPA inventory Table 2-1, 2014 MAC curves, Fast Facts transport, health benefit per kWh, SCC values | Non-CO2 abatement, transport baseline, benefit estimates | cfd-model.js and notes |
| FHWA VM-1 2024 | Vehicle miles and fleet | cfd-model.js |
| Lazard LCOE 2025, DOE Advanced Nuclear Liftoff, ORNL conduit hydro | Plant costs for nuclear, SMR, hydro | cfd-model.js and notes |
| LBNL Queued Up, developer survey, Grid Strategies, DOE Transmission Needs Study, Berkeley/GridLab, GE Vernova backlog, EIA planned additions | Build limits and grid access | cfd-model.js and notes |
| Senate permitting bill coverage, Princeton REPEAT, Third Way/RMI, Steptoe | Permitting and credit toggles | cfd-model.js, notes |
| Cox Q4 2025, ACEA, BNEF $108 pack, Li/Tong/Xing/Zhou | EV demand and feedback | cfd-model.js, tests |
| DOE LDES liftoff, NREL 2025 battery, ICCT hydrogen 2020, ICCT jet fuels | Storage, hydrogen and SAF parameters | cfd-model.js; snippet-level, see section 7 |
| Columbia CGEP, Energy Innovation, NETL, CBO 59832 | Industry abatement and CCS cost | cfd-model.js and notes |
| Rhodium Taking Stock 2026, RFF, EIA AEO2022, Brookings EMF 32, Hamilton/NBER | Validation ranges and design comparison | research-baseline-2026-10, cfd-tests |
| CBO Demographic Outlook, Fremstad and Paul | Population and dividend per head | cfd-households.js, notes |
| C2ES, CCL, Treasury OTA, Tax Foundation, CBO option 60962, CCL household study, RFF CLC and FPFA briefs, Nature Communications meta-analysis | Policy design and background | research-baseline-2026-10 |

## Not incorporated, or outside the project

**Files you uploaded but the model does not use**

| Source | Why not used | What it could add |
| --- | --- | --- |
| LBNL paper (qt2qh8x289) | Covers computers, vehicles, machinery, pharma and plastics, which the model's border products do not include | Intensity ratios if the border list widens |
| EPA supply-chain factors, byGHG CSV | CO2e totals were enough | Gas-by-gas border split |
| BEA Supply\_Sector and Use\_Sector | Detail tables were used instead | Coarser cross-check |
| BLS tables-page PDF | Used only to specify which downloads to request | None |
| EPA GLORIA dataset-page PDF | Descriptive only | Documentation of the import factors |
| EPA GLORIA import factors | Used only to set reference ratios, not as data | A direct per-country, per-product import intensity, the core of a detailed CBAM model |

**Used, but the file or code is not in the project**

| Item | Risk | Fix |
| --- | --- | --- |
| Raw BLS, BEA and EPA files (20 uploads) | Lost when the session workspace is reclaimed; only extracts survive | Keep the originals on your computer |
| border.py and border.json | The per-product ratios and the 284 Mt import figure cannot be rebuilt from the project alone | Save both to the project |
| Page build files (body, ui, css parts, build.py) | The published page cannot be rebuilt or edited from the project | Save to the project |

**Reviewed this session but not used as model inputs**

| Source | Status |
| --- | --- |
| ScienceDirect HEFA jet fuel cost paper | Conflicts with the fossil jet price used ($0.4 to 0.7/L vs $0.75/L); not reconciled |
| EU gasoline tax figure | Cited from memory; not verified |
| Canadian hydro-powered aluminum, about 70% EAF steel share, uniform cement and refining intensity | Assumed in border ratios; no source opened |

Sources a larger build would still need: full-text versions of the NREL, DOE LDES, ICCT and jet-fuel documents (only snippets were seen), an updated hydrogen cost source since the ICCT study dates from 2020, and a gas-fired and coal-fired plant retirement schedule from EIA Form 860 data.

## Unverified claims and weak points

- **Battery cost path.** I said earlier that the model's battery cost path matched NREL's mid case. That holds only to 2035 ($240 vs $243/kWh). By 2050 the model gives about $152/kWh against NREL mid at $178, before the extra chemistry cost cut (`storChem`). The model is more optimistic than NREL by design, following your view on new chemistries, but it is not NREL's path.
- **Snippet-level evidence.** The long-duration storage, hydrogen, jet-fuel and battery-duration parameters were set from search summaries, not full documents.
- **Hydrogen source is old.** The ICCT hydrogen study is from 2020.
- **Jet fuel conflict.** A HEFA cost paper puts biofuel at $0.4 to 0.7/L, below the $0.75/L fossil price in the model; this was not reconciled.
- **Assumed border ratios.** Per-product foreign-to-U.S. intensity ratios are judgment values, with a central import embodied-emissions figure of 284 Mt (range 219 to 374). The Canadian hydro aluminum, 70% EAF steel and uniform cement and refining claims were not sourced, and the EU gasoline tax figure is unchecked.
- **Hydrogen modelling.** Hydrogen is produced off-grid, so it adds no electricity demand, and it switches back to gas when the credit ends.
- **Late storage.** Long-duration storage arrives late in the build because of its start year and ramp.
- **Replacement cost.** The cost of replacing worn-out batteries is not charged to the system.
- **Leftover code.** A `FOOT` variable remains in the code unused.
- **Stale notes.** The top of cfd-model-notes.md still describes v2; only the later version entries (v2.1 to v3.4) are current.
- **Central results are one run.** The ranges come from a 120-draw triangular Monte Carlo with a fixed seed; they show parameter uncertainty, not model-structure uncertainty.

## Project files and next steps

**Saved in the project:** cfd-model.js (v3.4, matches the published page), cfd-tests.js (45 checks), cfd-model-notes.md (current from v2.1 on), cfd-households.js, cfd-cex-2024.json, cbam-spinoff-notes.md, research-baseline-2026-10.md.

**Not saved:** border.py and border.json, the page build files, and the 20 raw uploads.

**Suggested next steps**

1. Save border.py, border.json and the page build files to the project, so the border figures and the published page can be rebuilt.
2. Rewrite the stale top of cfd-model-notes.md as a current v3.4 summary.
3. Open the full documents for NREL, DOE LDES, ICCT hydrogen and the jet-fuel sources, then reconcile the battery cost basis and the jet-fuel conflict.
4. Charge replacement battery cost, and give hydrogen an electricity demand.
5. If you want the detailed CBAM model, start from cbam-spinoff-notes.md and the GLORIA import factors.

Sources (pages opened this session): the artifact's Sources section and the project docs listed above; the web searches in this stretch were snippet-level and none was opened in full.
