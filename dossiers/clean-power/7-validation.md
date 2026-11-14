# Clean, affordable power and a prepared country: validation

Role: section 7 of the clean power dossier: how the costs and results in sections 4-6 compare with outside figures, what the models and arithmetic miss, how the decided set lands with the rest of the plan, who it reaches and what households pay, what it does to emissions, the strongest objections, and the signs of failure. Status: reviewed (L2), with the milestone review's fixes and the re-review on the energy model (`review-m4.md`); L3 after the booking; on `DEC-2026-11-13-06` and `DEC-2026-11-13-07`. "The carbon model read" is `tools/coverage_read.py`; "project arithmetic" is `tools/clean_power_path.py`. Outcome it serves: OUT-05 (net emissions, household energy burden, disaster and uninsured losses, employment in transition regions; section 1).

## 1. Against outside figures

| Line | This dossier | Outside figure | Reading |
| --- | --- | --- | --- |
| Carbon price receipts (memo 1 B) | About $1.20 trillion over FY2030-39 on the booked basis; power and industry 63% of the fee's base on the carbon model [EV-CLP-714] | No outside score of a U.S. price on power and industry on this path is in the register. Canada's industrial price was expected to deliver 23-48% of its cuts against 8-14% for the consumer charge (Canadian Climate Institute, reported by CBC) [EV-CLP-318]; the EU's system on power and industry cut those sectors 50% since 2005 [EV-CLP-322] | The covered sectors carry most of a price's effect abroad; the receipts are the legacy model's, which responds slowly, so they lean high [EV-CLP-705] |
| Emission cuts from a price | On the energy model the price alone (memo 1 B, with process emissions) moves energy CO2 from 28% to 37% below 2005 in 2035 (part 5) | 5-15% in British Columbia (Murray and Rivers) [EV-CLP-302], contested as smaller outside transport (Pretis) [EV-CLP-303]; about 10% at EU-regulated plants (Dechezleprêtre and others) [EV-CLP-334]; 4-6% for a $40 tax across Europe (Metcalf and Stock) [EV-CLP-337] | A price does part of the work; the standards and credits do the rest, as the design intends |
| The dividend's distribution | On the carbon channel in 2035, the bottom two-fifths about $81-97 a household ahead under B, the middle fifth about even (part 4; the energy model) | Treasury's 2017 model: a per-person rebate raises the poorest decile's after-tax income almost 9% [EV-CLP-353]; about 70% of households better off with an equal dividend [EV-CLP-356]; Canada's PBO found households ahead on the fiscal count [EV-CLP-313] and slightly behind with wider economic effects [EV-CLP-314] | Same direction and shape (the energy model's DI-1 benchmark) |
| Credits | $0.757 trillion booked | JCT's 2022 score, $271 billion over FY2022-31 [EV-CLP-200]; CBO 2024, about $800 billion over 2025-34 [EV-CLP-201]; Penn Wharton, $1,045 billion over FY2023-32 [EV-CLP-203]; the 2025 repeal's savings, about $543 billion [EV-CLP-214] | The booking sits inside the outside range for a set that steps down; the cost risk (`6-cost.md`, part 2) is real, and the trigger (CLI-1A.03) is the answer |
| The standard | 80% clean by 2035, 100% by 2040 | The energy model (MOD-energy) reaches 73% in 2035, 87% in 2040 and 92% in 2045, because grid access, not price, is the limit; the legacy carbon model, which assumes the permitting package, reached 75% in 2035 [EV-CLP-708] and 91% in 2040; the queue's 55 months and 13% completion [EV-CLP-409] [EV-CLP-408] | Both targets are missed on the project's models, the 2040 one by about 13 points. The capped payment (CLI-3A.02) limits what missing them costs bills, but suppliers pay it every year the target is missed: about $41 billion in FY2040, returned through the bill credit (`6-cost.md`, part 2) |
| Grid tranches | $39 billion booked plus about $60 billion | DOE's lending lost about 3% of disbursements [EV-CLP-427]; REPEAT's 2.3% a year of transmission growth needed [EV-CLP-400] | The subsidy ratio is the legacy design's; DOE's record supports a low loss rate on loans |
| Bill credit | About $12 billion a year | LIHEAP's $4 billion reaches about 17% of eligible households [EV-CLP-038]; reach rose to 21-22% only when funding rose [EV-CLP-039] | Reach follows money; tripling reach at three times the money is a linear assumption, not a study (part 2) |
| Disaster package | $0.196 trillion booked | NIBS: $6 per $1 of federal mitigation grants [EV-CLP-610] and $11 per $1 of codes [EV-CLP-611], one institute's model; billion-dollar disasters cost $115-192 billion a year in 2024-25 [EV-CLP-125] [EV-CLP-130] | Small next to the losses; avoided losses are not counted as savings |
| Transition guarantee | About $14 billion over FY2030-39, front-loaded as coal closes by 2035 on the energy model | Canada's task force set 90% for two years and $20,000 for retraining without a cost [EV-CLP-529]; U.S. coal workers lost about 1.6 years of wages [EV-CLP-516] | Bottom-up working assumption only; no outside score |

## 2. What the models and arithmetic miss

- **Buildings unpriced.** The energy model leaves buildings and non-road fuel unpriced as memo 1 B does (`sectorPrice`), with the clean-heat standard in their place; industry's covered share is an assumption, 80% (70-90%), because no count of combustion CO2 above the 25,000-ton threshold is in the evidence. The legacy read (`tools/coverage_read.py`) is kept as a cross-check.
- **The engine's first decade.** Its receipts lean high: on CBO's price path they run 26% above CBO's (the energy model's PR-2 benchmark, a fail), as the legacy engine's did against NEMS, REGEN or E3 [EV-CLP-705]. Treat receipts and the dividend as the high side of a range. In the power sector the bias runs the other way for emissions: its history run misses measured coal and gas CO2 by 5.7% a year on average (HI-1, a fail; tolerance 5%), because it switches from coal to gas too readily, cutting coal 88% in the price's first year where the Energy Policy Simulator cuts 51% (EP-3). So the near-term power cuts are likely overstated; the 2035 figure (about 41%) may be a point or two optimistic (judgment), beyond the 40-42% band, which is a floor on the uncertainty. Disclosed in the booking (`6-cost.md`, part 6, 1a), not adjusted.
- **Every legacy model case assumes the 2026-28 permitting package became law** [EV-CLP-704]. If it fails, a 2029 climate law reaches about half its 2035 potential instead of four-fifths, on the legacy permitting analysis's illustrative estimate [EV-CLP-711]. Memo 4 plans for both cases (CLI-3A.03, .04); the emissions results lean optimistic if it fails.
- **The credits' take-up.** The carbon model counts its own credit set at about twice the booking [EV-CLP-710]. The trigger limits it; nothing models how fast it would bind.
- **The household module is coarse.** It spreads each quintile's indirect cost by non-energy spending and uses 2024 survey tables (`models/tools/carbon/cfd-households.js`); it has no regional split for the rows used here, so a heating-oil household in Maine and an all-electric one in Phoenix look alike.
- **Electricity prices.** On the energy model the decided set's national average retail price is 14.9 cents a kilowatt-hour in 2035 and 16.1 in 2040 (2025 dollars), against 14.3 and 14.7 under current law, about a tenth higher by 2040: the price and the standard raise costs, and the credits and cheaper clean power bring them back down until the power credits step down after 2034 (CLI-1A.02, which the model follows since #356). The price nets the credits out (cost-of-service) and includes the standard's capped payments, which add about 0.6 cents by 2040 (15.7 to 16.3 cents for the standard's layer; the model's fix for `review-m4.md`, R-2, #350). The payments are returned to lower- and moderate-income households through the bill credit.
- **The standard after 2035.** Under the decided path to 100% by 2040, suppliers pay the capped payment on the shortfall every year: about $21-41 billion a year in 2036-40 and $20-36 billion a year to 2050 (the energy model, `results.json`, CLI-3A.02).
- **Regions.** The module is national. Where power comes mostly from coal or oil (West Virginia, Wyoming and Missouri; Hawaii and Puerto Rico, where all-sector prices are already the highest, 35.72 cents a kilowatt-hour in Hawaii [EV-CLP-004]), electricity rises more against the same dividend, so low-income households there may be behind on the carbon channel while the national average is ahead. The bill credit and bill protection reach them first.
- **The guarantee's inputs are judgment.** No count of workers at plants and mines likely to close in 2030-40 is in the register (`4-specification.md`, "Evidence still needed").
- **Automatic LIHEAP enrollment** has no study in the register (memo 5's gap). The first winter's counts answer it.
- **What the plan-wide household model does not yet see.** The D3 test (`models/tools/household/d3.py`) reads the booked climate rows, which still charge home heating; it moves to memo 1 B's distribution at the booking (`6-cost.md`, part 6, step 7).

## 3. How it lands with the rest of the plan

- **The secure floor.** The dividend rides the child benefit's payment file, notice and front doors (FAM-1.09, FAM-1.10, decided by `DEC-2026-11-12-06`), and does not count as income for any program (shared rule 1). It is protected from offset as the child benefit is (CLI-2A.02, a working choice that follows FAM-1.07).
- **Housing.** Home repair's front door to the clean-power programs (HOU-12) is where a low-income owner learns about the credits at the point of sale, Weatherization's heat pumps and the bill credit. The non-wage payments here never raise rent (rule 1).
- **Transportation.** Road fuels stay outside the price (point 2); Moving America's fuel steps price them (MOV-29). The vehicle standards' numbers (CLI-4E.01) and the vehicle credits' step-down (CLI-1A.02) assume Moving America's charging and transit investment.
- **Care.** Displaced workers' health coverage is the single plan's from 2035 (`DEC-2026-11-10-09`); before then, the 2029 restoration (HLT-1) and the marketplace. The guarantee carries no separate health benefit, which is one reason it costs less than the legacy estimate (`6-cost.md`, part 1).
- **Immigration.** Who is paid the dividend follows immigration's table for universal programs (rule 3, `DEC-2026-11-12-07`, memo 6 C). The guarantee follows employment records.
- **Work.** The heat standard (LAB-6) and apprenticeships (LAB-8) stay with work; retraining under CLI-11.03 uses the same eligible provider lists. Oil and gas field workers outside the guarantee are the work flagship's to serve.
- **Fair financing.** The fee's 24.4% offset is a revenue line the settlement sees (CX); memo 1 B lowers it. After FY2039 the transition share's remainder stays in the general fund (`DEC-2026-11-13-13`; `6-cost.md`, part 2).
- **Rural.** USDA's Rural Utilities Service carries co-op lending alongside DOE (`5-delivery.md`, part 6).

## 4. Reach: for whom

**What households pay and get on the carbon channel, 2035, 2025 dollars per household** (the energy model's household module on the decided set, against Moving America's current-law path; `models/tools/energy/results.md`):

| Quintile | Adults | Dividend | Heating | Electricity | Everything else | Net under B |
| --- | --- | --- | --- | --- | --- | --- |
| Lowest 20% | 1.3 | +530 | 0 | −47 | −385 | **+97** |
| Second | 1.7 | +693 | 0 | −62 | −549 | **+81** |
| Middle | 2.0 | +815 | 0 | −67 | −742 | **+6** |
| Fourth | 2.2 | +897 | 0 | −75 | −1,005 | **−184** |
| Highest | 2.4 | +978 | 0 | −88 | −1,714 | **−824** |
| All | 1.8 | +734 | 0 | −68 | −880 | **−214** |

The legacy read (`tools/coverage_read.py`) gave +62, +46, −6, −154 and −654: the energy model's electricity cost is lower because it nets the credits out of retail prices (its BI-1 benchmark). Its electricity column includes the standard's payments (#350). Under B:
- **The bottom two-fifths come out ahead on average, nationally** (about $97 and $81 a year), and the middle fifth about even.
- **The top two-fifths pay more than they get** on the carbon channel, through goods.
- **These are the carbon channel alone.** They include the standard's payments in electricity (part 2, about 0.6 cents a kilowatt-hour by 2040) but leave out the bill credit that returns them (about $12 billion a year to households on SNAP, SSI, FDPIR or LIHEAP). The D3 test with every plan layer is the household model's, at the booking.

**Illustrative households** (2035, on the energy model; nominal dividend):

| Household | Under the decided set |
| --- | --- |
| A retired couple in Ohio heating with gas | No charge on their gas bill. Two Climate Dividend shares, about $820 a year, paid automatically from their Social Security records. Somewhat higher electricity and goods prices. A heat pump credit at the counter if they replace the furnace |
| A single renter in Phoenix, heat in the rent | One share, about $410 a year. If on SNAP, the bill credit goes to them directly (CLI-5H.01), with cooling counted equally |
| A grandmother on SSI in Mississippi | One share, from SSA's records; the bill credit on her summer bill with no form |
| A 57-year-old plant operator in Colstrip, Montana, with a pension | Draws the pension unreduced from the day the plant closes (CLI-11.04); the county's lost property tax replaced in full the first year, then 10 points less each year |
| A 35-year-old coal miner in West Virginia earning $40 an hour | In training: 90% of old pay, with unemployment benefits counted. In a $26-an-hour job: topped up to $36 for each hour worked, for the rest of the two years |
| A homeowner on the Louisiana coast | Premium help sized to income, while the price still shows the risk; the parish gets mitigation money by formula |

**Who still misses out.** Oil and gas field workers whose jobs fall without a facility closing (`4-specification.md`, "Where particular groups fall"); low-income households not on SNAP, SSI or LIHEAP who do not apply for the bill credit; adults outside every record who do not sign up for the dividend.

## 5. Emissions: what the decided set reaches

- **On the energy model (MOD-energy), the decided set reaches about 41% below 2005 in energy CO2 in 2035 and 52% in 2040**, and net greenhouse gases 43% and 66% in 2035 and 2050 (`models/tools/energy/results.md`). Its uncertainty band is 40-42% in 2035, a floor on the real uncertainty: published models differ by more for one policy.
- **Layer by layer** (energy CO2, 2035): current law 28%; the price 37%; the credits 39%; the standards in statute and the clean-heat standard 39-40%; the standby builder 41%; the methane fee adds to net greenhouse gases, not energy CO2. Memo 1 A's economy-wide fee would add almost nothing by 2035 (41%) and 1 point by 2040; the permitting package would add about 1 point in 2035 and 3 in 2040.
- **The earlier judgment** of 40-48% (the legacy models: 42% for the decided legacy package [EV-CLP-704], 48% for Package A [EV-CLP-715]) is replaced: the decided set sits at its low end.
- **Well short of the 2035 target,** 61-66% [EV-CLP-116], as point 1 states plainly. Independent current-policy projections are 26-44% [EV-CLP-112] [EV-CLP-113]. Against the Energy Policy Simulator's current-policies path (run by Espen), the energy model's current law tracks within 3 points; the simulator's far wider US Climate Action package cuts 43% from 2025 to 2035 against the decided set's 30% (the energy model's BL-3 and PK-1).

## 6. Objections answered

| Objection | Answer |
| --- | --- |
| "A carbon tax is a tax on families." | No household is charged directly: the price is on power plants and large industrial facilities (REV-C1G.01), and the dividend comes back to every adult before the price reaches bills (CLI-2A.03). On the carbon channel the bottom two-fifths come out ahead (part 4) |
| "Canada repealed its carbon rebate, so will we." | Canada repealed the consumer charge and kept the price on large emitters [EV-CLP-310] [EV-CLP-312]. The decided design is the part that survived there, and in the EU [EV-CLP-322] |
| "People won't believe they come out ahead." | In Canada 54% of rebate recipients thought they paid more [EV-CLP-321]. Here the payment is named, separate and on a fixed schedule, and there is no line on the gas bill to set against it (memo 1) |
| "The credits will cost far more than scored." | They did under the IRA [EV-CLP-200] [EV-CLP-201]. The step-down is in statute, and the trigger brings it forward if costs run 25% over for two years (CLI-1A.03) |
| "A clean electricity standard raises bills." | Its payment is capped (CLI-3A.02), and what suppliers pay goes back to low- and moderate-income households as bill protection. Clean power is already cheaper than new gas before credits [EV-CLP-456] |
| "Federal power lines will be built over local objection." | The public builder is a standby power: it acts only where no regional builder files within a year of a line's listing, and only at a cost no higher than the best bid; it uses existing siting backstops and no new eminent domain, and builds nothing inside the Texas grid without Texas's agreement (CLI-10.03) |
| "Data centers will raise everyone's bills." | Large new loads pay for the capacity and wires they need, in every market including ERCOT (CLI-6A.03); in PJM, data center load added about $9.3 billion to one year's capacity costs [EV-CLP-024] |
| "Wage insurance pays people to take worse jobs." | It pays only for hours actually worked, toward 90% of the old wage, for two years, capped at twice the median wage; working more never earns more than the old schedule (CLI-11.02). The yearly counts show if top-ups go mostly to very short or very low-paid jobs (CLI-11.05) |
| "Why help coal workers and not others?" | Their losses are large and long: about 1.6 years of wages [EV-CLP-516], with hourly wages down 40% in a UK study [EV-CLP-517]. The guarantee is small, about $12 billion over ten years (`6-cost.md`, part 1), and other workers keep the secure floor and the work flagship's programs |
| "Federal reinsurance puts taxpayers on the hook for hurricanes." | Only above a 1-in-100-year loss, with a $150 billion cap, risk-priced premiums and recoupment, in states that adopt current codes (CLI-7C.01, CLI-8.01). Its $75-150 billion contingent liability is disclosed in every fiscal test [EV-CLP-718] |
| "The plan doesn't reach its own 2035 goal." | True, and it says so (CLI-14.01; part 5). The goal is the national commitment; the inventory duty (CLI-14.02) makes the gap measured, not hidden |

## 7. Signs of failure

Published counts with a review trigger, not gates (`DEC-2026-11-09-13`):
- **The dividend's reach:** the share of adults on any federal record paid each quarter, by state; below 95% in the first full year triggers a review of the matching and front doors.
- **Bills:** EIA's average residential price against its 2029 level (the bill protection sunset's measure, CLI-5L.01); the bill credit's households reached against about half of eligible households.
- **The standard:** each supplier's clean share and payments; a national clean share more than five points behind the path for two years triggers a report on grid access (judgment).
- **The credits:** the trigger (CLI-1A.03) is itself the sign.
- **The grid:** high-voltage miles completed a year against the 2010-14 pace of about 1,781 [EV-CLP-051]; the queue's median time [EV-CLP-409]; the second tranche's milestones.
- **Emissions:** the inventory each April (CLI-14.02), against the working range in part 5.
- **The guarantee:** the yearly counts and their trigger (CLI-11.05).
- **Disasters and insurance:** code adoption against the three-year deadline [EV-CLP-613]; enrollment in the state insurers of last resort [EV-CLP-147] [EV-CLP-148].
