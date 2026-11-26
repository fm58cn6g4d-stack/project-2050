# Household model: model card

Role: the model card of `MOD-household`, the core model that measures taxes, benefits, poverty and distribution for real households (`charter/PLAN.md` 3.4). Status: **working** for the 2029 current-law baseline, the provision interface and the D3 report (with the secure floor's INC-1 to INC-5), the typical families and the 65-cent ceiling check, with 90% sampling intervals from the CPS replicate weights and the CBO-convention check (maintenance step M3; brought to the toolkit standard in step H3, 2026-11-25). It is not marked "preview" or "released": memo H1 is undecided. Owner: the Project 2050 lead session (Claude Code), through GitHub issues on this repository. Version: 0.3.0, see `CHANGELOG.md`. License: the line step H2b adds once memo H2 is answered. Every output of this model is analysis of the evidence, not an official score or a benefit determination; its results files carry that line in their header. Generated results are in [`results.md`](results.md) and `results.json`; never quote a figure from this card that `results.md` no longer shows.

## What it answers

It answers, at the 2029 current-law baseline (`DEC-2026-10-29-01`):
- **each household's budget**: market income, cash benefits, the main noncash benefits, federal income tax after credits, payroll tax and state income tax, for the 137 million households of the CPS (142 million aged to 2029);
- **distribution**: average federal tax rates and any provision's net effect by income quintile and decile, with the top 1% split out, on the D3 convention (below);
- **SPM-style poverty**: rates and counts for all people, children, working-age adults and people 65 and over, and the poverty gap, with the model's own taxes;
- **typical families**: the cents lost from each added dollar of earnings, layer by layer, for the three families the secure floor's 65-cent ceiling names (INC-5.02);
- **provisions**: every booked provision that has an incidence key, distributed by household group, for each scenario in `models/data/inputs/scenarios.json`.

## What it cannot answer

It cannot answer, by design: behavior (work, take-up, migration or marriage responses to a provision); macroeconomic effects; anything below the national level except as a CPS state code; individual benefit determinations or official scores (`charter/PLAN.md` 3.4: "the toolkit never claims to produce official scores or individual benefit determinations"). See "What it does not do".

## Evidence map

Every input is one row of `parameters.csv`, on the toolkit's parameter schema (`models/schema/README.md`); this table is generated from it by `python3 models/schema/parameters.py models/tools/household/parameters.csv --card models/tools/household/MODEL-CARD.md`. It holds current law as the model applies it (income tax, credits, payroll tax, SNAP, the poverty guideline, group `law`), the inputs of the SNAP work-rule calibration (A-8, group `a8_snap`) and the working values of the CBO-convention check (group `cbo_convention`). The statutory URLs are the ones the code's comments cited, listed here and not fetched in step H3. The 2029 values are these 2025 values indexed in `params.py` (`law()`, the column `uprating` names the index); the CBO series that do the indexing are `models/data/cbo/economic_economic_projections_fiscal_2026-02.csv`, an input of every run.

<!-- generated:parameters:start -->
123 inputs: 10 traced to evidence, 112 policy parameters, 0 calibrated to a benchmark, 1 labeled assumptions with a tested range.

| ID | Value | Unit | Year | Kind | Source or basis | Range |
| --- | --- | --- | --- | --- | --- | --- |
| `rates.1` Income tax rates | 0.1 | share | 2025 | policy | https://www.irs.gov/pub/irs-drop/rp-24-40.pdf |  |
| `rates.2` The 2017 act's rates, made permanent | 0.12 | share | 2025 | policy | https://www.irs.gov/pub/irs-drop/rp-24-40.pdf |  |
| `rates.3` The 2017 act's rates, made permanent | 0.22 | share | 2025 | policy | https://www.irs.gov/pub/irs-drop/rp-24-40.pdf |  |
| `rates.4` The 2017 act's rates, made permanent | 0.24 | share | 2025 | policy | https://www.irs.gov/pub/irs-drop/rp-24-40.pdf |  |
| `rates.5` The 2017 act's rates, made permanent | 0.32 | share | 2025 | policy | https://www.irs.gov/pub/irs-drop/rp-24-40.pdf |  |
| `rates.6` The 2017 act's rates, made permanent | 0.35 | share | 2025 | policy | https://www.irs.gov/pub/irs-drop/rp-24-40.pdf |  |
| `rates.7` The 2017 act's rates, made permanent | 0.37 | share | 2025 | policy | https://www.irs.gov/pub/irs-drop/rp-24-40.pdf |  |
| `brackets.joint.1` Rounded down to $50 (joint) or $25 after indexing | 23850 | $ | 2025 | policy | https://www.irs.gov/pub/irs-drop/rp-24-40.pdf |  |
| `brackets.joint.2` Rounded down to $50 (joint) or $25 after indexing | 96950 | $ | 2025 | policy | https://www.irs.gov/pub/irs-drop/rp-24-40.pdf |  |
| `brackets.joint.3` Rounded down to $50 (joint) or $25 after indexing | 206700 | $ | 2025 | policy | https://www.irs.gov/pub/irs-drop/rp-24-40.pdf |  |
| `brackets.joint.4` Rounded down to $50 (joint) or $25 after indexing | 394600 | $ | 2025 | policy | https://www.irs.gov/pub/irs-drop/rp-24-40.pdf |  |
| `brackets.joint.5` Rounded down to $50 (joint) or $25 after indexing | 501050 | $ | 2025 | policy | https://www.irs.gov/pub/irs-drop/rp-24-40.pdf |  |
| `brackets.joint.6` Rounded down to $50 (joint) or $25 after indexing | 751600 | $ | 2025 | policy | https://www.irs.gov/pub/irs-drop/rp-24-40.pdf |  |
| `brackets.single.1` Rounded down to $50 (joint) or $25 after indexing | 11925 | $ | 2025 | policy | https://www.irs.gov/pub/irs-drop/rp-24-40.pdf |  |
| `brackets.single.2` Rounded down to $50 (joint) or $25 after indexing | 48475 | $ | 2025 | policy | https://www.irs.gov/pub/irs-drop/rp-24-40.pdf |  |
| `brackets.single.3` Rounded down to $50 (joint) or $25 after indexing | 103350 | $ | 2025 | policy | https://www.irs.gov/pub/irs-drop/rp-24-40.pdf |  |
| `brackets.single.4` Rounded down to $50 (joint) or $25 after indexing | 197300 | $ | 2025 | policy | https://www.irs.gov/pub/irs-drop/rp-24-40.pdf |  |
| `brackets.single.5` Rounded down to $50 (joint) or $25 after indexing | 250525 | $ | 2025 | policy | https://www.irs.gov/pub/irs-drop/rp-24-40.pdf |  |
| `brackets.single.6` Rounded down to $50 (joint) or $25 after indexing | 626350 | $ | 2025 | policy | https://www.irs.gov/pub/irs-drop/rp-24-40.pdf |  |
| `brackets.hoh.1` Rounded down to $50 (joint) or $25 after indexing | 17000 | $ | 2025 | policy | https://www.irs.gov/pub/irs-drop/rp-24-40.pdf |  |
| `brackets.hoh.2` Rounded down to $50 (joint) or $25 after indexing | 64850 | $ | 2025 | policy | https://www.irs.gov/pub/irs-drop/rp-24-40.pdf |  |
| `brackets.hoh.3` Rounded down to $50 (joint) or $25 after indexing | 103350 | $ | 2025 | policy | https://www.irs.gov/pub/irs-drop/rp-24-40.pdf |  |
| `brackets.hoh.4` Rounded down to $50 (joint) or $25 after indexing | 197300 | $ | 2025 | policy | https://www.irs.gov/pub/irs-drop/rp-24-40.pdf |  |
| `brackets.hoh.5` Rounded down to $50 (joint) or $25 after indexing | 250500 | $ | 2025 | policy | https://www.irs.gov/pub/irs-drop/rp-24-40.pdf |  |
| `brackets.hoh.6` Rounded down to $50 (joint) or $25 after indexing | 626350 | $ | 2025 | policy | https://www.irs.gov/pub/irs-drop/rp-24-40.pdf |  |
| `cg_brackets.joint.1` Rounded as the brackets are | 96700 | $ | 2025 | policy | https://www.irs.gov/pub/irs-drop/rp-24-40.pdf |  |
| `cg_brackets.joint.2` Rounded as the brackets are | 600050 | $ | 2025 | policy | https://www.irs.gov/pub/irs-drop/rp-24-40.pdf |  |
| `cg_brackets.single.1` Rounded as the brackets are | 48350 | $ | 2025 | policy | https://www.irs.gov/pub/irs-drop/rp-24-40.pdf |  |
| `cg_brackets.single.2` Rounded as the brackets are | 533400 | $ | 2025 | policy | https://www.irs.gov/pub/irs-drop/rp-24-40.pdf |  |
| `cg_brackets.hoh.1` Rounded as the brackets are | 64750 | $ | 2025 | policy | https://www.irs.gov/pub/irs-drop/rp-24-40.pdf |  |
| `cg_brackets.hoh.2` Rounded as the brackets are | 566700 | $ | 2025 | policy | https://www.irs.gov/pub/irs-drop/rp-24-40.pdf |  |
| `std.joint` Rounded down to $50 | 31500 | $ | 2025 | policy | https://www.congress.gov/bill/119th-congress/house-bill/1/text |  |
| `std.single` Rounded down to $50 | 15750 | $ | 2025 | policy | https://www.congress.gov/bill/119th-congress/house-bill/1/text |  |
| `std.hoh` Rounded down to $50 | 23625 | $ | 2025 | policy | https://www.congress.gov/bill/119th-congress/house-bill/1/text |  |
| `std_aged.joint` Rounded down to $50 | 1600 | $ | 2025 | policy | https://www.irs.gov/pub/irs-drop/rp-24-40.pdf |  |
| `std_aged.single` Rounded down to $50 | 2000 | $ | 2025 | policy | https://www.irs.gov/pub/irs-drop/rp-24-40.pdf |  |
| `std_aged.hoh` Rounded down to $50 | 2000 | $ | 2025 | policy | https://www.irs.gov/pub/irs-drop/rp-24-40.pdf |  |
| `senior_deduction` Senior deduction, a person 65 or older | 6000 | $ | 2025 | policy | https://www.congress.gov/bill/119th-congress/house-bill/1/text |  |
| `senior_phaseout.joint` | 150000 | $ | 2025 | policy | https://www.congress.gov/bill/119th-congress/house-bill/1/text |  |
| `senior_phaseout.single` | 75000 | $ | 2025 | policy | https://www.congress.gov/bill/119th-congress/house-bill/1/text |  |
| `senior_phaseout.hoh` | 75000 | $ | 2025 | policy | https://www.congress.gov/bill/119th-congress/house-bill/1/text |  |
| `ctc` Child tax credit per child | 2200 | $ | 2025 | policy | https://www.congress.gov/bill/119th-congress/house-bill/1/text |  |
| `ctc_refundable` Refundable part of the child tax credit | 1700 | $ | 2025 | policy | https://www.congress.gov/bill/119th-congress/house-bill/1/text |  |
| `ctc_odc` Credit for other dependents | 500 | $ | 2025 | policy | https://www.congress.gov/bill/119th-congress/house-bill/1/text |  |
| `ctc_earn_floor` Earnings above which the refundable credit builds | 2500 | $ | 2025 | policy | https://www.law.cornell.edu/uscode/text/26/24 |  |
| `ctc_refund_rate` Refundable credit rate on earnings above the floor | 0.15 | share | 2025 | policy | https://www.law.cornell.edu/uscode/text/26/24 |  |
| `ctc_phaseout.joint` Not indexed | 400000 | $ | 2025 | policy | https://www.law.cornell.edu/uscode/text/26/24 |  |
| `ctc_phaseout.single` Not indexed | 200000 | $ | 2025 | policy | https://www.law.cornell.edu/uscode/text/26/24 |  |
| `ctc_phaseout.hoh` Not indexed | 200000 | $ | 2025 | policy | https://www.law.cornell.edu/uscode/text/26/24 |  |
| `ctc_phaseout_rate` Child credit phase-out rate | 0.05 | share | 2025 | policy | https://www.law.cornell.edu/uscode/text/26/24 |  |
| `eitc_rate.1` Earned income credit phase-in rate, by qualifying children 0, 1, 2, 3 or more | 0.0765 | share | 2025 | policy | https://www.irs.gov/pub/irs-drop/rp-24-40.pdf |  |
| `eitc_rate.2` | 0.34 | share | 2025 | policy | https://www.irs.gov/pub/irs-drop/rp-24-40.pdf |  |
| `eitc_rate.3` | 0.4 | share | 2025 | policy | https://www.irs.gov/pub/irs-drop/rp-24-40.pdf |  |
| `eitc_rate.4` | 0.45 | share | 2025 | policy | https://www.irs.gov/pub/irs-drop/rp-24-40.pdf |  |
| `eitc_po_rate.1` Earned income credit phase-out rate, by children | 0.0765 | share | 2025 | policy | https://www.irs.gov/pub/irs-drop/rp-24-40.pdf |  |
| `eitc_po_rate.2` | 0.1598 | share | 2025 | policy | https://www.irs.gov/pub/irs-drop/rp-24-40.pdf |  |
| `eitc_po_rate.3` | 0.2106 | share | 2025 | policy | https://www.irs.gov/pub/irs-drop/rp-24-40.pdf |  |
| `eitc_po_rate.4` | 0.2106 | share | 2025 | policy | https://www.irs.gov/pub/irs-drop/rp-24-40.pdf |  |
| `eitc_earned.1` Earned income amount, by children | 8490 | $ | 2025 | policy | https://www.irs.gov/pub/irs-drop/rp-24-40.pdf |  |
| `eitc_earned.2` Rounded down to $10 | 12730 | $ | 2025 | policy | https://www.irs.gov/pub/irs-drop/rp-24-40.pdf |  |
| `eitc_earned.3` Rounded down to $10 | 17880 | $ | 2025 | policy | https://www.irs.gov/pub/irs-drop/rp-24-40.pdf |  |
| `eitc_earned.4` Rounded down to $10 | 17880 | $ | 2025 | policy | https://www.irs.gov/pub/irs-drop/rp-24-40.pdf |  |
| `eitc_po_start.joint.1` Rounded down to $10 | 17730 | $ | 2025 | policy | https://www.irs.gov/pub/irs-drop/rp-24-40.pdf |  |
| `eitc_po_start.joint.2` Rounded down to $10 | 30470 | $ | 2025 | policy | https://www.irs.gov/pub/irs-drop/rp-24-40.pdf |  |
| `eitc_po_start.joint.3` Rounded down to $10 | 30470 | $ | 2025 | policy | https://www.irs.gov/pub/irs-drop/rp-24-40.pdf |  |
| `eitc_po_start.joint.4` Rounded down to $10 | 30470 | $ | 2025 | policy | https://www.irs.gov/pub/irs-drop/rp-24-40.pdf |  |
| `eitc_po_start.single.1` Rounded down to $10 | 10620 | $ | 2025 | policy | https://www.irs.gov/pub/irs-drop/rp-24-40.pdf |  |
| `eitc_po_start.single.2` Rounded down to $10 | 23350 | $ | 2025 | policy | https://www.irs.gov/pub/irs-drop/rp-24-40.pdf |  |
| `eitc_po_start.single.3` Rounded down to $10 | 23350 | $ | 2025 | policy | https://www.irs.gov/pub/irs-drop/rp-24-40.pdf |  |
| `eitc_po_start.single.4` Rounded down to $10 | 23350 | $ | 2025 | policy | https://www.irs.gov/pub/irs-drop/rp-24-40.pdf |  |
| `eitc_invest_limit` Investment income limit | 11950 | $ | 2025 | policy | https://www.irs.gov/pub/irs-drop/rp-24-40.pdf |  |
| `eitc_childless_ages.1` Childless credit: youngest and oldest age (1 and 2) | 25 | years | 2025 | policy | https://www.law.cornell.edu/uscode/text/26/32 |  |
| `eitc_childless_ages.2` | 64 | years | 2025 | policy | https://www.law.cornell.edu/uscode/text/26/32 |  |
| `ss_rate` Social Security tax rate, each half | 0.062 | share | 2025 | policy | https://www.law.cornell.edu/uscode/text/26/3101 |  |
| `hi_rate` Medicare tax rate, each half | 0.0145 | share | 2025 | policy | https://www.law.cornell.edu/uscode/text/26/3101 |  |
| `ss_wage_base` Social Security wage base | 176100 | $ | 2025 | policy | https://www.ssa.gov/oact/cola/cbb.html |  |
| `addl_hi_rate` Additional Medicare tax rate | 0.009 | share | 2025 | policy | https://www.law.cornell.edu/uscode/text/26/3101 |  |
| `addl_hi_threshold.joint` Not indexed | 250000 | $ | 2025 | policy | https://www.law.cornell.edu/uscode/text/26/3101 |  |
| `addl_hi_threshold.single` Not indexed | 200000 | $ | 2025 | policy | https://www.law.cornell.edu/uscode/text/26/3101 |  |
| `addl_hi_threshold.hoh` Not indexed | 200000 | $ | 2025 | policy | https://www.law.cornell.edu/uscode/text/26/3101 |  |
| `niit_rate` Net investment income tax rate | 0.038 | share | 2025 | policy | https://www.law.cornell.edu/uscode/text/26/1411 |  |
| `niit_threshold.joint` Not indexed | 250000 | $ | 2025 | policy | https://www.law.cornell.edu/uscode/text/26/1411 |  |
| `niit_threshold.single` Not indexed | 200000 | $ | 2025 | policy | https://www.law.cornell.edu/uscode/text/26/1411 |  |
| `niit_threshold.hoh` Not indexed | 200000 | $ | 2025 | policy | https://www.law.cornell.edu/uscode/text/26/1411 |  |
| `ss_base.joint` Not indexed | 32000 | $ | 2025 | policy | https://www.law.cornell.edu/uscode/text/26/86 |  |
| `ss_base.single` Not indexed | 25000 | $ | 2025 | policy | https://www.law.cornell.edu/uscode/text/26/86 |  |
| `ss_base.hoh` Not indexed | 25000 | $ | 2025 | policy | https://www.law.cornell.edu/uscode/text/26/86 |  |
| `ss_adj_base.joint` Not indexed | 44000 | $ | 2025 | policy | https://www.law.cornell.edu/uscode/text/26/86 |  |
| `ss_adj_base.single` Not indexed | 34000 | $ | 2025 | policy | https://www.law.cornell.edu/uscode/text/26/86 |  |
| `ss_adj_base.hoh` Not indexed | 34000 | $ | 2025 | policy | https://www.law.cornell.edu/uscode/text/26/86 |  |
| `fpl.1` HHS poverty guideline, 48 states: one person (1) and each additional person (2) | 15650 | $ | 2025 | policy | https://aspe.hhs.gov/topics/poverty-economic-mobility/poverty-guidelines |  |
| `fpl.2` Rounded to $10 | 5500 | $ | 2025 | policy | https://aspe.hhs.gov/topics/poverty-economic-mobility/poverty-guidelines |  |
| `snap_max.1` SNAP maximum allotment, household size 1 to 8, FY2025 | 292 | $ per month | FY2025 | policy | https://www.fns.usda.gov/snap/allotment/COLA |  |
| `snap_max.2` FY to FY, rounded | 536 | $ per month | FY2025 | policy | https://www.fns.usda.gov/snap/allotment/COLA |  |
| `snap_max.3` FY to FY, rounded | 768 | $ per month | FY2025 | policy | https://www.fns.usda.gov/snap/allotment/COLA |  |
| `snap_max.4` FY to FY, rounded | 975 | $ per month | FY2025 | policy | https://www.fns.usda.gov/snap/allotment/COLA |  |
| `snap_max.5` FY to FY, rounded | 1158 | $ per month | FY2025 | policy | https://www.fns.usda.gov/snap/allotment/COLA |  |
| `snap_max.6` FY to FY, rounded | 1390 | $ per month | FY2025 | policy | https://www.fns.usda.gov/snap/allotment/COLA |  |
| `snap_max.7` FY to FY, rounded | 1536 | $ per month | FY2025 | policy | https://www.fns.usda.gov/snap/allotment/COLA |  |
| `snap_max.8` FY to FY, rounded | 1756 | $ per month | FY2025 | policy | https://www.fns.usda.gov/snap/allotment/COLA |  |
| `snap_std.1` SNAP standard deduction by size (1-3, 4, 5, 6 or more), FY2025 | 204 | $ per month | FY2025 | policy | https://www.fns.usda.gov/snap/allotment/COLA |  |
| `snap_std.2` FY to FY, rounded | 204 | $ per month | FY2025 | policy | https://www.fns.usda.gov/snap/allotment/COLA |  |
| `snap_std.3` FY to FY, rounded | 204 | $ per month | FY2025 | policy | https://www.fns.usda.gov/snap/allotment/COLA |  |
| `snap_std.4` FY to FY, rounded | 217 | $ per month | FY2025 | policy | https://www.fns.usda.gov/snap/allotment/COLA |  |
| `snap_std.5` FY to FY, rounded | 254 | $ per month | FY2025 | policy | https://www.fns.usda.gov/snap/allotment/COLA |  |
| `snap_std.6` FY to FY, rounded | 291 | $ per month | FY2025 | policy | https://www.fns.usda.gov/snap/allotment/COLA |  |
| `snap_earn_ded` SNAP earned income deduction | 0.2 | share | FY2025 | policy | https://www.law.cornell.edu/uscode/text/7/2014 |  |
| `snap_brr` SNAP benefit reduction rate on net income | 0.3 | share | FY2025 | policy | https://www.law.cornell.edu/uscode/text/7/2017 |  |
| `snap_shelter_cap` Excess shelter deduction cap, households without an elderly or disabled member | 712 | $ per month | FY2025 | policy | https://www.fns.usda.gov/snap/allotment/COLA |  |
| `snap_gross_test` SNAP gross income test, share of the poverty guideline | 1.3 | share | FY2025 | policy | https://www.law.cornell.edu/uscode/text/7/2014 |  |
| `snap_min_benefit` SNAP minimum benefit | 23 | $ per month | FY2025 | policy | https://www.fns.usda.gov/snap/allotment/COLA |  |
| `snap.usda_participants` SNAP participants, FY2025 average | 42145499 | persons | FY2025 | evidence | EV-SEC-039 |  |
| `snap.cbo_fewer.abawd_55_64` Sec. 10102: fewer participants, adults 55-64 | 800000 | persons | none | evidence | EV-SEC-036 |  |
| `snap.cbo_fewer.parent_child14` Sec. 10102: fewer participants, parents of a child 14 or older | 300000 | persons | none | evidence | EV-SEC-036 |  |
| `snap.cbo_fewer.total` Sec. 10102: fewer participants, all | 2400000 | persons | none | evidence | EV-SEC-036 |  |
| `snap.energy_cut_monthly` Sec. 10103: energy assistance cut | 100 | $ per month | none | evidence | EV-SEC-038 |  |
| `snap.energy_share` Sec. 10103: share of households affected | 0.03 | share | none | evidence | EV-SEC-038 |  |
| `snap.internet_cut_monthly` Sec. 10104: internet cost cut | 10 | $ per month | none | evidence | EV-SEC-038 |  |
| `snap.internet_share` Sec. 10104: share of households affected | 0.65 | share | none | evidence | EV-SEC-038 |  |
| `snap.first_year` SNAP changes: first year applied | 2026 | year | 2026 | policy | https://www.congress.gov/bill/119th-congress/house-bill/1/text |  |
| `medicare.cost_per_enrollee_2032` Medicare spending per enrollee, 2032 | 20200 | $ per enrollee | 2032 | evidence | EV-CAR-061 |  |
| `medicare.growth_per_person` Health growth per person, 2029 to 2032 | 0.048 | share per year | none | assumption | project judgment: the per-person health growth health_cost_review.py uses; not run across a range, so low and high equal the value |  |
| `esi.worker_share` Worker share of the family premium | 0.264 | share | 2026 | evidence | EV-CAR-111; EV-CAR-112 |  |
<!-- generated:parameters:end -->

Not in the file, and where each is: the reform parameters of the decided plan (the American Family Act credit, the 2021 childless credit, the care credit and guarantee charge, the surtaxes, the plan's layers in `families.py`) are plan design, not current law, and stay in `rules.py` and `families.py`; the labeled assumptions A-1 to A-10 below are structural choices (which CBO series moves which amount), not single numbers; the typed incidence keys and rows are the budget model's adopted inputs (`models/data/inputs/`). Listed in Known issues.

### Data

- **Source:** the Census Bureau's CPS Annual Social and Economic Supplement, 2026 public-use file (income year 2025), `https://www2.census.gov/programs-surveys/cps/datasets/2026/march/asecpub26csv.zip`, SHA-256 `fe819d0d2fc4470c282e76c247b8aa8b6054811619730307e9f2fe6186707d93` (the hash `legacy/sources/family-child-poverty-cps-baseline.md` records). It is a U.S. government work.
- **The committed extract** (`models/data/household/`, 5 MB, built by `extract.py`): 72,979 tax units (Census `TAX_ID` within each household), 55,401 SPM units and 53,344 households. The archive itself (139 MB) is not committed; the extract lets the model and its tests run in the checks.
- **Units:** tax units for taxes (the Census's own assignment of filers, spouses and dependents); SPM units for poverty; households for distribution.
- **Why the CPS and not the legacy cells:** the legacy incidence model's keys are typed estimates "anchored to a published pattern; no row is yet a microsimulation" (its own words). The CPS has every element the D3 test and the SPM need for most keys, and the child-poverty tool had already validated the 2026 file against the Census's published rates. The ACS was not used: it lacks the SPM elements and the Census tax model's figures.
- **Weights:** person weights (`MARSUPWT`) for poverty, household weights (`HSUP_WGT`) for distribution, the head's person weight for tax units.
- **Replicate weights:** the archive's `asec_csv_repwgt_2026.csv` holds the Census's 160 replicate person weights. They are not committed (22 million numbers); `intervals.py` reads them from the archive and commits only its results, `intervals.json`. Each record takes the replicate weights of the person whose weight it already uses: on the file, `HSUP_WGT` is the householder's person weight and `SPM_WEIGHT` the SPM unit head's (checked for every record).

### What it replaces

| Legacy piece | What it did | Now |
| --- | --- | --- |
| `models/tools/incidence-model.py`, `incidence-years.py`, `incidence-make-md.py` → `legacy/index/revenue-household-incidence-model.md` | The D3 net test with typed distribution keys over 140 million households, its year-by-year profiles and its report | **Retired (M3 part 2).** `d3.py` is the engine: its legacy version gives the legacy figures exactly (tested against the last legacy run, `test-data/`) and writes `incidence.json` for the budget model's readers; its model version uses the measured keys. The year profiles are ported (`d3.py`, `series`), and the report's text is `results.md`, sections 5, 6 and 8. The legacy report is the scripts' last output, no longer regenerated |
| `models/tools/child-poverty/` → `legacy/sources/family-child-poverty-*.md`, `legacy/index/child-poverty-agenda-analysis.html` | Child SPM poverty on the CPS ASEC 2026, the agenda's family experiments, replicate-weight uncertainty | The same archive and SPM measurement (`extract.py` checks the same SHA-256), with taxes recomputed, for every age group and aged to 2029. Its replicate-weight intervals are ported and extended to every headline output (`intervals.py`, below); its delivery and identification branches and its eight agenda cases are not yet ported |

## Mechanisms and their research basis

### Rules modeled at the 2029 baseline

All in `params.py` (parameters) and `tax.py` (calculator); 2025 values are the law as enacted, and 2029 values are indexed from them.

- **Income tax:** the 2017 act's brackets, made permanent by P.L. 119-21; the 0/15/20% rates on gains and dividends (all dividends treated as qualified); the standard deduction ($31,500 joint in 2025, P.L. 119-21 sec. 70102) and its additions at 65; taxable Social Security (sec. 86); the net investment income tax.
- **Credits:** the child tax credit ($2,200 in 2025, $2,400 in 2029, refundable up to $1,700 and $1,800, 15% of earnings above $2,500, phased out above $200,000/$400,000), the $500 credit for other dependents, and the earned income credit by number of children (childless workers 25-64).
- **The 2025-2028 items expire before 2029:** the $6,000 senior deduction is applied in 2025 and gone in 2029; the tips, overtime and car-loan deductions are not modeled in either year (the CPS cannot see them).
- **Payroll taxes:** Social Security and Medicare, both halves, the self-employment tax and the additional Medicare tax.
- **Benefits:** Social Security, SSI, TANF, unemployment insurance, veterans' benefits, SNAP, housing assistance, school meals, WIC and energy assistance, as the CPS reports them or the Census imputes them for the SPM. The model does not yet simulate eligibility for them, except SNAP for the typical families. In 2029, P.L. 119-21's SNAP changes are applied to the reported amounts (A-8).
- **Typical families:** SNAP's federal rules (FY2025 parameters uprated: the gross income test at 130% of poverty or a state's broad option up to 200%, the 20% earnings deduction, the standard deduction, an optional excess shelter deduction, 30% of net income); the premium tax credit on the 2010 act's schedule (2026 applicable percentages).

### Assumptions (labeled, with their basis and range)

| ID | Assumption | Basis | Range, and the cost of being wrong |
| --- | --- | --- | --- |
| A-1 | The CPS's 2025 households stand for 2029's: no change in who lives together, works or claims whom | Static aging is the standard first step (CBO's and TPC's models also age a base year) | Demographic change over four years is small next to the keys' uncertainty; a reweighting to CBO's age structure is a part 2 option |
| A-2 | Amounts grow 2025 to 2029 by type, with CBO's February 2026 projections: earnings with wages per payroll job (+15.8%), prices (+10.7%), interest, dividends and rents per household, capital gains with GDP per household; weights grow with CBO's households (+3.6%) | CBO's fiscal-year series (`models/data/cbo/`), standing in for calendar years | Earnings growing faster than the law's indices is what produces bracket creep and EITC erosion in 2029; a slower wage path lowers 2029's poverty rate |
| A-3 | Tax indexing uses CBO's fiscal-year chained CPI-U (FY2028 over FY2024) for the code's twelve months ending August | Gives $2,400 and $1,800 for the 2029 child credit; CBO's own path has $2,400 and $1,900 in 2030 | Off by at most one rounding step in a few amounts |
| A-4 | The Social Security wage base follows CBO's wages per job in place of SSA's average wage index | The two move together | A few hundred dollars on the base |
| A-5 | SPM thresholds grow with CBO's consumer spending per household (+13.6%) | The Census sets the thresholds from five years of spending on food, clothing, shelter and utilities, so they rise with spending, not prices | With prices instead (+10.7%) the 2029 poverty rate would be about 12.6% instead of 13.3% |
| A-6 | Units the Census tax model marks as nonfilers get no refundable credits | Keeps the Census's convention, so the SPM baseline stays calibrated | A full take-up run gives the same 2029 poverty rates to two decimals |
| A-7 | No itemized deductions, AMT or the dependent care, education, saver's and premium credits in the microdata | The CPS has no itemized deductions; the Census's own tax model imputes them | Income tax after credits is about 9% above the Census tax model's in 2025, most of it in the top quintile |
| A-8 | 2029 SNAP is 2025's, uprated, with P.L. 119-21's changes applied (`snap2025.py`). The wider work rule (sec. 10102) removes benefits from adults not disabled who worked under 20 hours a week, with probabilities calibrated so each group's loss matches CBO's participation estimate as a share of USDA's participants (EV-SEC-036, EV-SEC-039). The energy and internet changes (secs. 10103-04) are applied as CBO's expected amounts (EV-SEC-038). The Thrifty Food Plan rule (sec. 10101) needs nothing beyond price uprating. Not applied: the state cost share's state responses (about 300,000 people) and the noncitizen rule (about 90,000), which need behavior or immigration status the model lacks. The law's Medicaid changes stay with the health coverage model | CBO's section estimates (EV-SEC-034 to 038), which the secure floor already uses | The CPS records about $42B of 2025 SNAP against USDA's $95.8B, so the law's poverty effect is understated by about half. The model's cut is 10.1% of benefits, against about 9.8% implied by CBO's sections. CBPP counted 4.7 million fewer participants by March 2026, against CBO's 3 million for 2026 (EV-SEC-040); at that pace the loss would be larger |
| A-9 | The premium credit's 2026 applicable percentages hold in 2029 | The percentages are reindexed yearly; their direction depends on premium growth against income growth | A few tenths of a cent per dollar in the family rates |
| A-10 | State median income for FAM-2.01's charge is the CPS's median cash income of four-person SPM units, nationally ($160,852 in 2029) and in the lowest-income state ($98,693), scaled by HHS's size factors | HHS sets the lines from the ACS; the CPS has every state but small samples (at least 59 four-person units each) | The CPS's SPM-unit median runs above HHS's family median, so the charge may start lower than modeled; it moves the charge's start, not the ceiling's binding point at 100-125% of poverty |

### Distribution conventions

- **D3 convention (the fairness test):** households ranked by expanded cash income (cash income plus the employer's payroll tax) divided by the square root of household size, in quintiles and deciles of **equal numbers of households**, so a per-household average is comparable with the legacy model's. The top 1% is the top 1% of households on the same ranking.
- **Benchmark conventions:** tax units in quintiles of equal numbers of people (the Tax Policy Center's), and CBO's, set against D3 step by step in "The CBO-convention check" below.
- The size adjustment is a model-design choice: an unadjusted ranking puts large families higher than their living standard warrants. It moves households between groups; it changes no booked amount.

### Provision interface

- **Inputs:** the budget model's `ledger.json` (each provision's FY2030-39 amount) and the adopted `incidence-rows.csv`, which books each row as a formula over ledger IDs and splits it across incidence keys (both read only).
- **Keys** (`keys.csv`): for each key, `micro` measures its shares on the 2029 baseline households (a household field, or a rule computed tax unit by tax unit in `rules.py`), and `legacy` keeps the typed key, with the reason.
- **Measured:** 21 keys. In part 1, 14: Earnings and capped earnings; people and adults; FAM-1's child benefit (the American Family Act's credit less today's child and other-dependent credits, household by household); housing assistance; Medicaid and marketplace coverage; Medicare (three keys); employer coverage; Social Security; energy assistance; and C20's surtax base. In part 2, the secure floor's six: INC-1's childless credit (`eitc_childless`, a rule), SNAP's 2025 cuts and SNAP before them (`snap_cut`, `snap`, INC-2), SSI received and SSI's indexed exclusions (`ssi`, `ssi_exclusions`, a rule, INC-3), and the refundable dependent care credit (`cdctc`, a rule, INC-4); then INC-2.02's (`snap_earn`: SNAP households' earnings, each SNAP-receiving SPM unit's capped at 200% of its poverty guideline, since the CPS's annual earnings include months off SNAP). INC-5's forgone rent offsets use housing's key. INC-4's rule measures about $0.3 billion a year of refundability against a $4.5 billion booking; `results.md`, section 6, gives the reasons the CPS may run low and the data that would settle it. INC-1.02 is read as moving no money: no family loses the earned income credit from the shared definition (the lead, on #320).
- **Kept, with the reason in `keys.csv`:** 29 keys, where the CPS cannot see the base: consumption and excises, capital and corporate income, the top-end taxes and the health coverage model's own keys.
- **The top 1%:** for earnings and the surtax, the top 1%'s share is the legacy key's, because the CPS top-codes high incomes. It finds 9% of earnings and 28% of the surtax base in the top 1%, against the legacy 12% and 55%.
- **Outputs:** net dollars per household per year, FY2030-39 average, by group, for every scenario, in the legacy model's arithmetic. They are divided by the model's mid-window household count: the CPS count grown to FY2034-35 with CBO's household growth, 147.1 million against the legacy 140 million.
- **Poverty effects** need a provision as a rule (`rules.py`), not a key. There are five: FAM-1's child benefit, C20's surtax, INC-1's childless credit, INC-3.02's SSI exclusions and INC-4's refundable care credit.
- **The secure floor's rows** (`incidence-rows.csv`, INC1 to INC5 and INC2D, SNAP's earned income deduction at 45% on `snap_earn`; `results.md`, section 6): INC-2 is split on CBO's sections of P.L. 119-21 (43.7% on the households the model cuts, 56.3% on SNAP households before the law); INC-3 on the booking's parts (75.5% on today's SSI recipients, standing in for new eligibles and for the territories, which the CPS does not cover; 24.5% on the exclusions rule). INC-4's rule, rescoped to care no other program pays for (Espen, November 13), nets out both programs: care of children under 5 counts only up to the guarantee's charge, with the CPS's national median income of four-person units standing in for state median income; school-age care counts as reported, since the CPS asks what families paid and leaves out the subsidies they receive, so CCDF's payments for the school-age children it reaches (FAM-2.04, kept at today's reach) are already outside it (Census, SEHSD working paper 2025-11, https://www2.census.gov/library/working-papers/2025/demo/sehsd-wp2025-11.pdf). `run.inc4_sensitivity` reports the measurement with spending scaled up and with CCDF's reach netted again (a lower bound). Its keys were added to `incidence-keys.csv` as measured, rounded, so the legacy arithmetic runs on the same rows.

### Typical families

`families.py` computes, for a single parent of two, a married couple with two (one earner) and a single adult, the cents lost per added dollar of earnings from 50% to 300% of poverty: payroll tax, income tax after credits, SNAP and, as a variant, the premium credit, plus a variant with an excess shelter deduction (a $1,400 monthly rent in 2025 dollars). Medicaid and CHIP are cliffs and are listed apart. The "plan preview" adds FAM-1 and INC-1.01 only. It is not the 65-cent ceiling check, which needs every plan layer and is part 2.

What part 1 already shows, at 2029 law (`results.md`, section 4):
- **Without a shelter deduction:** the single parent and the married couple lose 52.7 cents at 100-125% of poverty (SNAP 24, the earned income credit's phase-out 21, payroll 7.7), as the dossier's arithmetic says. Their combined rate is 39-41 cents at 150-200%, where the credit's phase-out meets the 12% bracket. On the marketplace, that rises to about 55 cents.
- **With rent counted in SNAP's shelter deduction:** SNAP's effective rate is 36 cents, not 24. Each added dollar also shrinks the deduction by 50 cents. The two families then reach 64.7 cents at 100-125% of poverty under current law. **This matters for INC-5.02:** the memo's arithmetic used 24 cents.
- **In the plan preview:** removing today's child credit takes away the credit's offset to the 10% bracket at 100-125% of poverty, so those families reach 62.7 cents before any shelter effect.

**The ceiling check (INC-5.02; `results.md`, section 7)** adds every plan layer (`plan_budget`): paid leave's worker share (0.3%, 0.55% at its ceiling), FAM-1, INC-1.01, SNAP as INC-2 restores it with INC-2.02's earned income deduction at 45% (`DEC-2026-11-13-03`), the premium credit in 2030-34 only, and child care's charge (FAM-2.01) net of INC-4's refundable credit. State median income, which sets the charge's lines, is the CPS's median for four-person SPM units: nationally and in the lowest-income state (assumption A-10). **Result:** met in every case but one. From 2035, 55.5 cents for families with children without the shelter deduction, 55.5 (single parent) and 63.8 (married couple) with it, 49.8 for the single adult; in 2030-34 on the marketplace, 57.6 without the deduction. The one case above the ceiling is the married couple on the marketplace in 2030-34 with the rent, 65.9 at 125% of poverty, monitored under INC-5.02's rule, not fixed. Before INC-2.02 (the deduction at 20%), families with children with the deduction reached 75.0 from 2035 and 77.1 in 2030-34; `results.md` shows both.

### Reconciliation with the legacy incidence model

Scenario Q (the decided package), net dollars per household per year, FY2030-39 (`results.md`, section 5, with the reconciliation table that moves from the legacy setup to the model's one key at a time; the figures change with every booking, so read them there):
- **The D3 result does not change:** on both versions the fourth quintile comes out behind on scenario Q and ahead on the base package alone (scenario A). The model's figures for the fourth quintile are smaller in size than the legacy model's.
- **What moves the fourth quintile:** the household count (147.1 million against 140 million), the earnings keys (the CPS puts 54% of earnings in the top quintile, against the typed 46%, so payroll-based costs fall less on the fourth), FAM-1's key, partly offset by the housing key (the CPS puts today's housing assistance 93% in the first quintile, against the typed 60%).
- **Housing's key** is a model-design choice, which the lead settled on #318: the CPS-measured spread is the central case, and the legacy key is a stated sensitivity in `results.md`. If the housing dossier expects new awards to reach higher up than today's assistance, the sensitivity is the reading to use.
- **Sampling error does not change the verdict:** in every scenario the fourth quintile's sign holds at 90% (`results.md`, section 9). **Nor does CBO's grouping,** though equal numbers of people make Q's fourth-quintile shortfall about $190 a household larger (section 10).
- **What's still open:** the remaining typed keys (capital, consumption and the top-end taxes) dominate the costs, so the measured keys change the picture at the margin, not at the core. Replacing them needs tax data (TPC or CBO tables by key), part 2.

## Limits

- **No behavior:** take-up, work, avoidance and macro effects are out. New benefits are paid at full take-up; current-law credits follow the Census's filing status.
- **Benefits are reported or imputed, not simulated.** CPS under-reporting of SNAP, TANF and SSI is not corrected (the Urban Institute's TRIM3 does this; not available here).
- **No itemized deductions, AMT, or the dependent care, education and premium credits** in the microdata (A-7).
- **The top of the distribution is thin:** the CPS top-codes income and misses most capital gains, so top-1% results come from the legacy keys where it matters (`keys.csv`).
- **No health coverage values:** coverage enters only as counts for keys. The health coverage model owns premiums and out-of-pocket costs.
- **Year-by-year paths are shapes:** the phase-in profiles spread each row's ten-year total (`d3.py`, `series`); they are not scored annual paths.
- **Intervals are for sampling error only** (`intervals.py`): under-reporting, top-coding and the model's assumptions are larger for most outputs and are not in them.

## Validation

Written by the test code (`test_household.py`, on `models/schema/validation.py`); `python3 models/tools/household/test_household.py --write-validation` rewrites this block from the committed `results.json`, and the test fails if it is stale. The tolerances are fixed in the test code, with their basis, before the model's figure is read. Most of the misses are the same gap: the CPS has less income than the sources it is set against (the explanation column). They are reported, not tuned away.

<!-- generated:validation:start -->
23 benchmarks. 23 independent: 9 pass, 14 miss.

| ID | Quantity | Target | Source and vintage | Model | Difference | Tolerance (set in advance) | Result | Explanation |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| HH-P-all | SPM poverty rate, 2025, the model's own taxes: all people | 13.1 percent | SRC-3602; Census P60-290, table 8 (2025) | 13.2 | 0.050 (+0.4%) | 0.31 percent; the 90% sampling half-interval of the model's own rate (intervals.json), which matches the Census's published margin (about 0.3 points for all people, 0.6 for children) | pass | The model rebuilds the Census's resources from its elements exactly with Census taxes (tested); with its own taxes the difference is its slightly higher income tax (no itemized deductions, A-7). |
| HH-P-children | SPM poverty rate, 2025, the model's own taxes: children | 13.4 percent | SRC-3602; Census P60-290, table 8 (2025) | 13.4 | 0.050 (+0.4%) | 0.56 percent; the 90% sampling half-interval of the model's own rate (intervals.json), which matches the Census's published margin (about 0.3 points for all people, 0.6 for children) | pass | The model rebuilds the Census's resources from its elements exactly with Census taxes (tested); with its own taxes the difference is its slightly higher income tax (no itemized deductions, A-7). |
| HH-P-18_64 | SPM poverty rate, 2025, the model's own taxes: adults 18-64 | 12.3 percent | SRC-3602; Census P60-290, table 8 (2025) | 12.3 | 0.020 (+0.2%) | 0.34 percent; the 90% sampling half-interval of the model's own rate (intervals.json), which matches the Census's published margin (about 0.3 points for all people, 0.6 for children) | pass | The model rebuilds the Census's resources from its elements exactly with Census taxes (tested); with its own taxes the difference is its slightly higher income tax (no itemized deductions, A-7). |
| HH-P-65_plus | SPM poverty rate, 2025, the model's own taxes: people 65 and over | 15.4 percent | SRC-3602; Census P60-290, table 8 (2025) | 15.4 | -0.020 (-0.1%) | 0.52 percent; the 90% sampling half-interval of the model's own rate (intervals.json), which matches the Census's published margin (about 0.3 points for all people, 0.6 for children) | pass | The model rebuilds the Census's resources from its elements exactly with Census taxes (tested); with its own taxes the difference is its slightly higher income tax (no itemized deductions, A-7). |
| HH-T-eitc | Earned income credit, 2025 law | 40.5 $ billion | SRC-3600; Census tax model on the same CPS records | 41.0 | 0.50 (+1.2%) | 5%; the model applies the Census tax model's rules to the same records, so it should land within a few percent; 5%, a round band | pass | Follows the Census on the same records. |
| HH-T-ctc | Child and other-dependent credits, refundable and not, 2025 law | 119 $ billion | SRC-3600; Census tax model on the same CPS records | 120 | 0.90 (+0.8%) | 5%; the model applies the Census tax model's rules to the same records, so it should land within a few percent; 5%, a round band | pass | Follows the Census on the same records. |
| HH-T-agi | Adjusted gross income, 2025 | 16,169 $ billion | SRC-3600; Census tax model on the same CPS records | 16,026 | -143 (-0.9%) | 5%; the model applies the Census tax model's rules to the same records, so it should land within a few percent; 5%, a round band | pass | About 1 percent below. |
| HH-T-tax | Income tax after credits, 2025 law | 1,929 $ billion | SRC-3600; Census tax model on the same CPS records | 2,097 | 168 (+8.7%) | 5%; the model applies the Census tax model's rules to the same records, so it should land within a few percent; 5%, a round band | **miss** | The model's income tax is about 9% above the Census's, most of it in the top quintile: the CPS microdata has no itemized deductions, AMT or the dependent care, education, saver's and premium credits (A-7), which the Census's own model imputes. |
| HH-S-eitc | Earned income credit, 2025 law, against IRS returns | 66.3 $ billion | https://www.irs.gov/pub/irs-soi/23in25ic.xls; https://www.irs.gov/pub/irs-soi/23in33ar.xls; IRS SOI, tax year 2023, all returns (2023 law) | 41.0 | -25.3 (-38.1%) | 10%; 10%: a different tax year and law, and a survey against administrative records | **miss** | The CPS under-reports low and self-employment earnings and family links, and the IRS total includes claims its own compliance studies find improper; the model follows the Census on the same records. Cited, not run: fetch_public.py cannot read the legacy .xls. |
| HH-S-ctc | Child and other-dependent credits, total, 2025 law, against IRS returns | 119 $ billion | https://www.irs.gov/pub/irs-soi/23in25ic.xls; https://www.irs.gov/pub/irs-soi/23in33ar.xls; IRS SOI, tax year 2023 ($2,000 credit) | 120 | 0.75 (+0.6%) | 10%; 10%: a different tax year and credit amount ($2,000 against 2025's $2,200) | pass | About 1% above SOI on a credit that is 10% larger per child; the refundable part is $11B lower (the low-earnings under-reporting again). |
| HH-S-actc | Refundable child credit, 2025 law, against IRS returns | 34.5 $ billion | https://www.irs.gov/pub/irs-soi/23in25ic.xls; https://www.irs.gov/pub/irs-soi/23in33ar.xls; IRS SOI, tax year 2023 | 23.0 | -11.5 (-33.4%) | 10%; 10%: a different tax year and credit amount | **miss** | The CPS under-reports the low earnings that drive the refundable part. |
| HH-TPC-1-i | Average federal income tax rate, 2029, Q1 (tax units, quintiles of equal numbers of people) | -3.66 percent | SRC-4801; TPC T26-0045 (June 2026), current law with P.L. 119-21, percent of expanded cash income | -2.10 | 1.56 (+42.6%) | 1.00 percent; one percentage point, a round band set before the comparison; TPC publishes no error band | **miss** | TPC's expanded cash income adds what the CPS lacks (employer health and retirement contributions, retirement-account earnings, imputed corporate tax, SNAP): TPC's income is $29.0T against the model's $21.9T, so the same dollars sit over a larger denominator. In dollars the model's income tax is lower ($2.68T against $3.15T: the CPS top-codes and misses top incomes and gains) and its payroll tax higher ($2.16T against $1.89T: CPS earnings run above the national accounts' wages). The ordering and the progressivity match |
| HH-TPC-1-p | Average federal payroll tax rate, 2029, Q1 (tax units, quintiles of equal numbers of people) | 6.08 percent | SRC-4801; TPC T26-0045 (June 2026), current law with P.L. 119-21, percent of expanded cash income | 5.70 | -0.38 (-6.2%) | 1.00 percent; one percentage point, a round band set before the comparison; TPC publishes no error band | pass | TPC's expanded cash income adds what the CPS lacks (employer health and retirement contributions, retirement-account earnings, imputed corporate tax, SNAP): TPC's income is $29.0T against the model's $21.9T, so the same dollars sit over a larger denominator. In dollars the model's income tax is lower ($2.68T against $3.15T: the CPS top-codes and misses top incomes and gains) and its payroll tax higher ($2.16T against $1.89T: CPS earnings run above the national accounts' wages). The ordering and the progressivity match |
| HH-TPC-2-i | Average federal income tax rate, 2029, Q2 (tax units, quintiles of equal numbers of people) | -0.070 percent | SRC-4801; TPC T26-0045 (June 2026), current law with P.L. 119-21, percent of expanded cash income | 2.10 | 2.17 (+3100.0%) | 1.00 percent; one percentage point, a round band set before the comparison; TPC publishes no error band | **miss** | TPC's expanded cash income adds what the CPS lacks (employer health and retirement contributions, retirement-account earnings, imputed corporate tax, SNAP): TPC's income is $29.0T against the model's $21.9T, so the same dollars sit over a larger denominator. In dollars the model's income tax is lower ($2.68T against $3.15T: the CPS top-codes and misses top incomes and gains) and its payroll tax higher ($2.16T against $1.89T: CPS earnings run above the national accounts' wages). The ordering and the progressivity match |
| HH-TPC-2-p | Average federal payroll tax rate, 2029, Q2 (tax units, quintiles of equal numbers of people) | 7.70 percent | SRC-4801; TPC T26-0045 (June 2026), current law with P.L. 119-21, percent of expanded cash income | 10.0 | 2.30 (+29.9%) | 1.00 percent; one percentage point, a round band set before the comparison; TPC publishes no error band | **miss** | TPC's expanded cash income adds what the CPS lacks (employer health and retirement contributions, retirement-account earnings, imputed corporate tax, SNAP): TPC's income is $29.0T against the model's $21.9T, so the same dollars sit over a larger denominator. In dollars the model's income tax is lower ($2.68T against $3.15T: the CPS top-codes and misses top incomes and gains) and its payroll tax higher ($2.16T against $1.89T: CPS earnings run above the national accounts' wages). The ordering and the progressivity match |
| HH-TPC-3-i | Average federal income tax rate, 2029, Q3 (tax units, quintiles of equal numbers of people) | 4.52 percent | SRC-4801; TPC T26-0045 (June 2026), current law with P.L. 119-21, percent of expanded cash income | 6.50 | 1.98 (+43.8%) | 1.00 percent; one percentage point, a round band set before the comparison; TPC publishes no error band | **miss** | TPC's expanded cash income adds what the CPS lacks (employer health and retirement contributions, retirement-account earnings, imputed corporate tax, SNAP): TPC's income is $29.0T against the model's $21.9T, so the same dollars sit over a larger denominator. In dollars the model's income tax is lower ($2.68T against $3.15T: the CPS top-codes and misses top incomes and gains) and its payroll tax higher ($2.16T against $1.89T: CPS earnings run above the national accounts' wages). The ordering and the progressivity match |
| HH-TPC-3-p | Average federal payroll tax rate, 2029, Q3 (tax units, quintiles of equal numbers of people) | 7.69 percent | SRC-4801; TPC T26-0045 (June 2026), current law with P.L. 119-21, percent of expanded cash income | 10.7 | 3.01 (+39.1%) | 1.00 percent; one percentage point, a round band set before the comparison; TPC publishes no error band | **miss** | TPC's expanded cash income adds what the CPS lacks (employer health and retirement contributions, retirement-account earnings, imputed corporate tax, SNAP): TPC's income is $29.0T against the model's $21.9T, so the same dollars sit over a larger denominator. In dollars the model's income tax is lower ($2.68T against $3.15T: the CPS top-codes and misses top incomes and gains) and its payroll tax higher ($2.16T against $1.89T: CPS earnings run above the national accounts' wages). The ordering and the progressivity match |
| HH-TPC-4-i | Average federal income tax rate, 2029, Q4 (tax units, quintiles of equal numbers of people) | 7.71 percent | SRC-4801; TPC T26-0045 (June 2026), current law with P.L. 119-21, percent of expanded cash income | 9.80 | 2.09 (+27.1%) | 1.00 percent; one percentage point, a round band set before the comparison; TPC publishes no error band | **miss** | TPC's expanded cash income adds what the CPS lacks (employer health and retirement contributions, retirement-account earnings, imputed corporate tax, SNAP): TPC's income is $29.0T against the model's $21.9T, so the same dollars sit over a larger denominator. In dollars the model's income tax is lower ($2.68T against $3.15T: the CPS top-codes and misses top incomes and gains) and its payroll tax higher ($2.16T against $1.89T: CPS earnings run above the national accounts' wages). The ordering and the progressivity match |
| HH-TPC-4-p | Average federal payroll tax rate, 2029, Q4 (tax units, quintiles of equal numbers of people) | 7.90 percent | SRC-4801; TPC T26-0045 (June 2026), current law with P.L. 119-21, percent of expanded cash income | 11.4 | 3.50 (+44.3%) | 1.00 percent; one percentage point, a round band set before the comparison; TPC publishes no error band | **miss** | TPC's expanded cash income adds what the CPS lacks (employer health and retirement contributions, retirement-account earnings, imputed corporate tax, SNAP): TPC's income is $29.0T against the model's $21.9T, so the same dollars sit over a larger denominator. In dollars the model's income tax is lower ($2.68T against $3.15T: the CPS top-codes and misses top incomes and gains) and its payroll tax higher ($2.16T against $1.89T: CPS earnings run above the national accounts' wages). The ordering and the progressivity match |
| HH-TPC-5-i | Average federal income tax rate, 2029, Q5 (tax units, quintiles of equal numbers of people) | 16.2 percent | SRC-4801; TPC T26-0045 (June 2026), current law with P.L. 119-21, percent of expanded cash income | 18.6 | 2.44 (+15.1%) | 1.00 percent; one percentage point, a round band set before the comparison; TPC publishes no error band | **miss** | TPC's expanded cash income adds what the CPS lacks (employer health and retirement contributions, retirement-account earnings, imputed corporate tax, SNAP): TPC's income is $29.0T against the model's $21.9T, so the same dollars sit over a larger denominator. In dollars the model's income tax is lower ($2.68T against $3.15T: the CPS top-codes and misses top incomes and gains) and its payroll tax higher ($2.16T against $1.89T: CPS earnings run above the national accounts' wages). The ordering and the progressivity match |
| HH-TPC-5-p | Average federal payroll tax rate, 2029, Q5 (tax units, quintiles of equal numbers of people) | 5.52 percent | SRC-4801; TPC T26-0045 (June 2026), current law with P.L. 119-21, percent of expanded cash income | 9.20 | 3.68 (+66.7%) | 1.00 percent; one percentage point, a round band set before the comparison; TPC publishes no error band | **miss** | TPC's expanded cash income adds what the CPS lacks (employer health and retirement contributions, retirement-account earnings, imputed corporate tax, SNAP): TPC's income is $29.0T against the model's $21.9T, so the same dollars sit over a larger denominator. In dollars the model's income tax is lower ($2.68T against $3.15T: the CPS top-codes and misses top incomes and gains) and its payroll tax higher ($2.16T against $1.89T: CPS earnings run above the national accounts' wages). The ordering and the progressivity match |
| HH-TPC-T1-i | Average federal income tax rate, 2029, top 1% (tax units, quintiles of equal numbers of people) | 23.3 percent | SRC-4801; TPC T26-0045 (June 2026), current law with P.L. 119-21, percent of expanded cash income | 28.7 | 5.37 (+23.0%) | 1.00 percent; one percentage point, a round band set before the comparison; TPC publishes no error band | **miss** | TPC's expanded cash income adds what the CPS lacks (employer health and retirement contributions, retirement-account earnings, imputed corporate tax, SNAP): TPC's income is $29.0T against the model's $21.9T, so the same dollars sit over a larger denominator. In dollars the model's income tax is lower ($2.68T against $3.15T: the CPS top-codes and misses top incomes and gains) and its payroll tax higher ($2.16T against $1.89T: CPS earnings run above the national accounts' wages). The ordering and the progressivity match |
| HH-TPC-T1-p | Average federal payroll tax rate, 2029, top 1% (tax units, quintiles of equal numbers of people) | 2.13 percent | SRC-4801; TPC T26-0045 (June 2026), current law with P.L. 119-21, percent of expanded cash income | 5.40 | 3.27 (+153.5%) | 1.00 percent; one percentage point, a round band set before the comparison; TPC publishes no error band | **miss** | TPC's expanded cash income adds what the CPS lacks (employer health and retirement contributions, retirement-account earnings, imputed corporate tax, SNAP): TPC's income is $29.0T against the model's $21.9T, so the same dollars sit over a larger denominator. In dollars the model's income tax is lower ($2.68T against $3.15T: the CPS top-codes and misses top incomes and gains) and its payroll tax higher ($2.16T against $1.89T: CPS earnings run above the national accounts' wages). The ordering and the progressivity match |
<!-- generated:validation:end -->

Sources: Census P60-290 is SRC-3600 (report) and SRC-3602 (table 8). TPC T26-0038 and T26-0045 are SRC-4800 and SRC-4801 (licensed, cited only); CBO 61911 is SRC-4802. IRS SOI's tax year 2023 tables 2.5 and 3.3 are at `irs.gov/pub/irs-soi/23in25ic.xls` and `23in33ar.xls`; `fetch_public.py` cannot read legacy `.xls`, so they are cited until it can.

CBO, *The Distribution of Household Income, 2022* (January 2026), table 9 (SRC-4802): first quintile −10.1% income tax and 9.5% payroll; top 1% 23.9% and 2.0%. Not comparable directly (a different year and law), so it is not a row above; the conventions are compared step by step in "The CBO-convention check" below. JCT: no distribution table under P.L. 119-21 yet (JCX-38-25 says its estimates were not ready); the latest, JCX-26-24, is pre-2025 law. Not used.

### Sampling uncertainty

`intervals.py` recomputes the headline outputs with each of the Census's 160 replicate weights and writes `intervals.json`; `run.py` reports it (`results.md`, section 9). The method is the Census's, successive difference replication: SE = √(4/160 × Σ(estimate_r − estimate_0)²), with the 90% interval at ±1.645 SE.
- **Covered:** SPM poverty (rates by age, counts and the gap, 2025 and 2029); D3 average federal tax rates by quintile and the top 1%; the D3 test's net per household by group in every scenario, with the measured keys, groups, household count and group incomes recomputed in each replicate; and `health_cost_review.take_home_micro`'s pass shares for the recommended 2.25% contribution, the 2.5% alternative and package E.
- **The check on the method:** the 2025 poverty intervals reproduce the Census's published 90% margins (about ±0.3 points for all people, ±0.6 for children).
- **What it shows:** sampling error is small next to the model's other uncertainties. The 2029 poverty rate is 13.3% ±0.3; the take-home test's 88.7% of workers is ±0.3; the D3 test's fourth quintile is ±$50-60 a household, and its sign holds at 90% in every scenario.
- **Held fixed:** each record's computed amounts (taxes, poverty status, a package's charge), and two weight-dependent calibrations, SNAP's work-rule probabilities (A-8) and the state-median stand-in (A-10). The take-home package's rates and lines are also held fixed: the intervals say how many of the country's workers pass a given design.
- **Keeping it current:** `results.md` compares the interval run's centers with each run's own estimates and marks any that have moved by more than half an interval; then rerun `intervals.py` with the archive (about five minutes). The take-home centers are not rechecked by `run.py`, since `health_cost_review.py` is not part of it; rerun `intervals.py` when the recommended design changes.

### The CBO-convention check

`conventions.py` moves the 2029 baseline households from D3's conventions to CBO's (*The Distribution of Household Income, 2022*, SRC-4802) one at a time and reports each step's average tax rates, the households that change quintile and scenario Q's net per household on re-measured keys (`results.md`, section 10).

| Convention | D3 | CBO | Effect, measured |
| --- | --- | --- | --- |
| Unit and size adjustment | Households, square root of size | The same | None |
| Groups | Equal numbers of households | Equal numbers of people | The largest: about 8% of households change quintile; the first quintile holds about 32 million households and the fifth 27 million; Q's fourth quintile about $190 a household further behind |
| Means-tested cash (SSI, TANF); negative incomes | In the ranking income; ranked at the bottom | Out; in no group | Very small |
| Medicare and employers' health premiums | Out: the CPS records neither | In, at average cost | About 21% of households change quintile in all, as retirees and covered workers move up; rates fall in the upper quintiles and rise in the first; Q's fourth quintile hardly moves. Measured at working values (a Medicare enrollee at about $17,550 in 2029, from CBO's 2032 cost per enrollee, EV-CAR-061; employers' premiums at 2.79 times what a job-covered unit reports paying, from KFF's 26.4% worker share, EV-CAR-111, EV-CAR-112) |
| Taxes in the rates | Income and payroll | Also corporate and excise | Not a ranking convention: the D3 test carries those taxes through its keys |
| Data | The CPS | Tax returns merged at the top; transfers corrected | Data, not conventions (see "Benchmarks"): the first quintile's income tax rate is about −4% on CBO's conventions against CBO's −10% for 2022, mostly from the survey's under-reported low earnings and credits |

**What it settles:** D3's verdicts do not depend on the convention, and D3 keeps equal households, since it states and compares results per household. CBO's grouping is reported as a sensitivity where a quintile's result is near zero.

## Known issues

- **The D3 sampling intervals are stale since the settlement.** `intervals.json` was run on 2026-11-20 (commit `d143f10`), before the financing settlement was booked in the ledger (#480). Rerunning `intervals.py` on 2026-11-25 reproduces its poverty, tax-rate and take-home blocks exactly, and moves 34 of its 36 `d3_net_per_household` values by at most $10 a household (the centers) and their standard errors by at most about $0.25. Not refreshed in step H3 because that would change the results (`results.md`, section 9). Refresh: `python3 models/tools/household/fetch_cps.py`, then `intervals.py --archive build/cps/asecpub26csv.zip`.
- **The take-home intervals read frozen flags** (`take-home-flags.csv.gz`, `take-home-flags.md`): per-unit pass flags from the health cost review's test at the recommended design, made on 2026-11-25. They go stale if that design changes. Regenerating them needs the health scripts, which this model no longer imports.
- **Inputs still in code**, not in `parameters.csv`: the decided plan's reform parameters (`rules.py`, `families.py`); the typed estimates behind the CBO-convention check's Medicare growth (`medicare.growth_per_person`, in the file, is a single value with no sensitivity run: its low and high equal it); the structural choices in A-2 to A-5. A reform file for the plan's parameters is a later step.
- **The legacy-reproduction test is skipped** on main: its fixture is the legacy model at `e897ac6`, and `incidence-rows.csv` has changed since.
- **Benefits are reported or imputed, not simulated** (the CPS under-reports SNAP: $42B against USDA's $95.8B, so P.L. 119-21's poverty effect is understated by about half, A-8).
- **The child-poverty tool's eight agenda cases are not ported**, and that tool (`models/tools/child-poverty/`) rewrites tracked files each time its validation runs (audit 1.2).
- **The budget model's readers still use the legacy typed keys** (`incidence.json`), not the measured keys.
- **IRS SOI is cited, not run** (its legacy `.xls` cannot be read by `fetch_public.py`); the SOI rows above are checked by hand against the published tables.
- **Most TPC rows miss** because the denominators differ (TPC's income is $29.0T against $21.9T); no TPC-conforming income is built.
- **The run log before 2026-11-18 is hand-written** (below), and its commits are not in the shallow clone step H3 worked in.
- **A ledger refresh changes the results**: the budget model's ledger is an input, so a new booking moves the household outputs. How the versioning rule treats that is an open question for the lead (`models/schema/README.md`, "Versions").
- **No fresh-clone job has run this model yet** (step H2b wires one); the checks here ran it from a clone with `build/` absent.

Tracked on the stage H board (`charter/PROGRESS.md`) and by `models/toolkit.csv`.

## How to run

From a fresh clone, with no `build/`, one command (standard library only; Python 3.10 or later; `numpy` only for `intervals.py`):

```bash
python3 models/tools/household/run.py [--ledger FILE] [--out DIR] [--record] [--update-snapshot]
python3 models/tools/household/test_household.py               # the tests; --write-validation rewrites the table above
bash models/tools/run-all.sh                                   # builds the ledger first, runs the tests and the model, compares with the committed copies
python3 models/tools/household/fetch_cps.py [--out DIR]        # the Census archive (139 MB), with its SHA-256 checked; only for the two scripts below
python3 models/tools/household/extract.py --archive build/cps/asecpub26csv.zip      # rebuild the extract
python3 models/tools/household/intervals.py --archive build/cps/asecpub26csv.zip    # the intervals (about five minutes; numpy)
```

With no `--ledger`, `run.py` starts from the budget model's `build/ledger.json` when it exists and otherwise from the committed snapshot, `snapshot/ledger.json` (the amounts the model reads from the ledger, taken from main on 2026-11-25). `run.py --update-snapshot` refreshes it from a built ledger; a test fails when the two differ, so the snapshot cannot go stale unnoticed. `--out` defaults to this folder: it overwrites the committed `results.json` and `results.md`, which `run-all.sh` compares byte for byte. `--record` stamps the commit and appends a `RUN-` row to `models/runs.csv`.

The CPS archive itself is not committed; the extract in `models/data/household/` (5 MB) lets the model and its tests run without it. `fetch_cps.py` refuses a file whose SHA-256 is not the recorded one, so a changed or truncated download never reaches the model. No random numbers are drawn anywhere in the model: the intervals are the Census's successive difference replication, which is deterministic, so no seed is needed (a test checks that no module imports `random`).

### Tests

`test_household.py` covers:
- hand-checked tax cases: the brackets, the earned income credit, the refundable child credit, taxable Social Security, the child credit's phase-out rounding and the wage base;
- the 2029 law's values;
- the exact SPM identity and the Census's published rates;
- household accounting: net income equals its parts, and unit and household totals agree;
- equal-household groups and keys that sum to 100%;
- the FAM-1 rule, and the secure floor's: the 2021 childless credit, the care credit's rates and the guarantee's charge, the refundable part, SSI's exclusions, and SNAP's cuts as the key's base;
- P.L. 119-21's SNAP changes: the source year untouched, 2029's losses matching CBO's share, a cut of 8-12% of benefits;
- the typical families, and the ceiling check's layers, charge and verdicts;
- **exact reproduction of the legacy incidence model's last results** in every scenario, while its inputs are unchanged, and year profiles that sum to each row's total. The fixture (`test-data/legacy-incidence-2026-11-13.json`) is the legacy model's run on main at `e897ac6`, so **the exact reproduction holds as of `e897ac6`**: on that commit's inputs and ledger, d3.py's legacy version gives the fixture exactly in every scenario (checked again on November 16, 2026 with this model's current code). Since then `incidence-rows.csv` and `incidence-keys.csv` have changed (from INC-2.02's row on), so on main the test is skipped. It guards the legacy arithmetic, not today's figures;
- the replicate-weight step: the SDR formula, its groups and poverty estimators against the model's own, and the committed `intervals.json` (complete, the 2025 margins near the Census's, and the 2029 poverty and tax-rate centers equal to this model's);
- the CBO-convention check: its step 0 is D3 itself, its equal-people groups hold a fifth of people each, and it leaves the model's groups as they were.
- the frame (step H3): the parameter file meets the schema and builds the law the model used; the card's evidence and validation tables are the generated ones; the snapshot equals the built ledger; the model runs from the snapshot; no module imports the health cost or financing scripts or draws at random; the take-home flags match the extract; the fetch script checks the hash; the committed results carry the header and the current code's hashes.

## Run log

Recorded runs are rows of `models/runs.csv` (`RUN-household-<date>-<letter>`), written by `models/runlog.py`; a dossier quoting a figure cites the run ID. The rows from `RUN-household-2026-11-18-a` to `RUN-household-2026-11-24-a` were back-filled in step H3 from the commits that changed `results.json`, each at its commit's own code and inputs, all labeled version 0.1.0 (`CHANGELOG.md`): their `results_sha256` is that commit's file as committed (it had no header then), so it cannot be checked the way a stamped reference output can (the row's note says so). The results header carries the version, the commit (null in the committed reference outputs) and the hashes of the code and the inputs. The version history is `CHANGELOG.md`.

The runs before the helper existed, kept as they were written (their commits are not in the clone step H3 worked in, so they are not rows of `models/runs.csv`):

| Run | Model version | Inputs | Provisions |
| --- | --- | --- | --- |
| `RUN-household-2026-11-13-a` | #318, merged as `13d4664` (M3 part 1) | CPS ASEC 2026 extract (SHA-256 above); CBO February 2026 economic projections; `incidence-rows.csv`, `incidence-keys.csv`, `scenarios.json` as on main | The ledger as built from main on November 13, 2026 |
| `RUN-household-2026-11-13-b` | The A-8 PR's head (M3 part 2, first piece: SNAP under P.L. 119-21) | As run a, with the SPM extract's four work-rule counts added | As run a; no provision result changes |
| `RUN-household-2026-11-13-c` | #320, merged as `e897ac6` (M3 part 2, INC-1 to INC-5) | As run b, with the extract's child care spending (`SPM_CHILDCAREXPNS`), children under 5 and 5-12, and SSI recipients' detail added (no existing field changes) | As run a, with `incidence-rows.csv` INC1 to INC5 and their keys |
| `RUN-household-2026-11-13-d` | #321, merged as `d204a85` (M3 part 2, the 65-cent ceiling check) | As run b | As run a; results section 7 added, no provision result changes |
| `RUN-household-2026-11-13-e` | #327, merged as `8537e86` (M3 part 2, the legacy reports moved) | As runs c and d | As run c; `d3.py` in place of the legacy scripts; results section 8 added |
| `RUN-household-2026-11-13-f` | The INC-2.02 PR's head (Espen's option D, `DEC-2026-11-13-03`) | As run e, with the household field `snap_earn` (no extract change) | As run e, with the ledger row INC-2B, `incidence-rows.csv` INC2D and its key `snap_earn`; the ceiling check with SNAP's earned income deduction at 45% |
| `RUN-household-2026-11-16-g` | The M3 intervals PR's head (replicate-weight intervals and the CBO-convention check) | As run f, with the archive's replicate weights (`asec_csv_repwgt_2026.csv`, same SHA-256) read by `intervals.py`; working values for Medicare and employers' premiums in `conventions.py` | The ledger as built from main on November 16, 2026 (`e561ca5`); no provision result changes; results sections 9 and 10 added |
