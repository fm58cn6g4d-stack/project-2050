# Clean power: the decided package tested on the energy model

Role: the design-improvement step Espen asked for after the booking: use the energy model (MOD-energy, `models/tools/energy/`) alongside the dossier's independent external research to "back up, interrogate, and design the best climate policy package we can". Status: second pass, on the model's committed runs (`results.json`, main at `37ee069`, after #365's named runs). The model is M4's; this file runs nothing new into it. Any change to a decided item goes to Espen as a decision memo: memo 9 so far, decided B (`DEC-2026-11-13-14`).

## The runs, side by side

Energy CO2 below 2005 (2035, 2040); clean share of generation; national retail price (2025 cents a kWh); nominal $ billion over FY2030-39. Cumulative energy CO2 2030-50 against the decided set, Mt, summed year by year from the engine's annual rows (project arithmetic; `results.json` keeps only 2030, 2035, 2040 and 2050, so the yearly rows come from re-running the committed configuration unchanged, which reproduces `results.json`).

| Run | CO2 2035 | CO2 2040 | Clean 2040 | Price 2040 | Credits FY2030-39 | Standard's payments | Cumulative CO2 vs decided |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2029 current law | 27.4% | 30.7% | 60% | 14.7 | 0 | 0 | +24,173 |
| **The decided set** | **40.8%** | **51.8%** | **87%** | **16.1** | **1,037** | **163** | — |
| Builder everywhere (memo 4 A, full strength, `bld_hi`) | 41.9% | 53.6% | 92% | 15.5 | 1,172 | 93 | −1,433 |
| Builder at 75% (`bld_75`) | 41.3% | 52.8% | 90% | 15.8 | 1,105 | 128 | −749 |
| Standby builder at 25% (`bld_lo`) | 40.3% | 50.6% | 85% | 16.3 | 967 | 199 | +812 |
| Decided set with the permitting package | 42.4% | 54.5% | 94% | 15.6 | 1,125 | 74 | −2,198 |
| Standard's cap at $20 (`ces_cap20`) | 40.8% | 51.7% | 87% | 15.8 | 1,036 | 85 | +55 |
| Standard's cap at $60 (`ces_cap60`) | 40.8% | 51.8% | 88% | 16.3 | 1,037 | 229 | −82 |
| Economy-wide price (memo 1 A) | 41.5% | 52.8% | 87% | 16.1 | 1,041 | 175 | −1,356 |
| Price repealed from 2033 (durability) | 36.7% | 47.2% | 83% | 15.3 | 986 | 253 | +5,657 |

The yearly sum replaces the first pass's trapezoid over four years, which gave −1,458, −2,159, +864, −1,258 and +5,395 for the same runs; no conclusion changes.

**The standard's own layer** (80% by 2035, 100% by 2040, added on top of the credits) moves energy CO2 from 39.1% to 39.0% below 2005 in 2035: on the model it slightly *raises* 2035 emissions, then cuts about 315 Mt over 2030-50, mostly after 2035, while suppliers pay about $193 billion over FY2030-39 at that layer and the 2040 price rises from 15.7 to 16.3 cents (`results.md`, the layered tables). The engine does not report why; a likely reason is that while the grid binds, the standard's credit for captured gas and its effect on dispatch move fossil output at the margin before new wind and solar can connect. It strengthens point 2 below.

## What the runs say

1. **The grid is the binding lever, as the dossier's evidence says.** Every run that adds grid access cuts more than any price or standard change: the full-strength builder about 1.4 Gt over 2030-50 and the permitting package about 2.2 Gt, both with lower bills. The external evidence agrees: transmission must roughly double its growth rate [EV-CLP-400]; the typical project built in 2025 waited about 61 months to connect [{LBNL}] and 13% of requests are built [EV-CLP-408]; about 435 miles of 345 kV and above were built in 2025 [{GS}]. The engine's own note: grid access, not price, limits wind and solar (SRC-0077).
2. **When the grid binds, the standard is mostly a fee.** Its payments ($163 billion on the decided set) are large and its added cut small, because suppliers cannot connect the clean power the standard asks for. The cap's level barely moves carbon: $20, $40 or $60 all give 41% in 2035, within 0.1 points in 2040, and within about 0.1 Gt over 2030-50, while payments run $85, $163 or $229 billion and the 2040 price 15.8, 16.1 or 16.3 cents. The payments fall as the grid grows: to $93 billion with the full builder and $74 billion with permitting. That pointed at using the payments to build the grid that ends them: **memo 9**, decided B.
3. **More builder helps, with steadily smaller returns per dollar on the model.** From the decided half-strength builder, 75% adds about $68 billion of credits for about 0.75 Gt; full strength adds about $135 billion for about 1.43 Gt: about **$90-95 a ton** either way (project arithmetic on nominal dollars and undiscounted tons), against EPA's 2023 social cost of carbon of $230 a ton in 2030 (2020 dollars; SRC-5006). Bills are up to 0.5 cents a kWh lower in 2040. These are upper bounds: see "What the engine assumes about the builder" below.
4. **The economy-wide price (memo 1 A, not chosen)** cuts about 1.36 Gt more over 2030-50, mostly after 2035, with about $840 billion more receipts and a heating charge on households. Espen chose B (`DEC-2026-11-13-06`); nothing here reopens it.
5. **The methane fee is the cheapest tonne in the set:** it lifts net greenhouse gases from 41.0% to 42.8% below 2005 in 2035 and raises money (about $22 billion). Kept as decided.
6. **The standard's cap could be lower without losing carbon, on the model.** A $20 cap gives the same cut, a lower 2040 price (15.8 cents) and $78 billion less in payments. Under memo 9 B the payments now fund the grid account, and the research below finds money is rarely what binds, so a lower cap would mostly reduce receipts. Not put to Espen: the cap was decided in memo 3, the model's standard is crude (one national credit, no banking), and the cap also guards against shortfalls the model can't see. Recorded as a finding to revisit at the next model version.

## What the engine assumes about the builder

The builder is the engine's federal grid program at a fraction of full strength (`assumptions.csv`, `grid_standby_scale`, 0.5, range 0.25-1.0; `engine/cfd-model.js` line 43: +0.8 points a year of transmission growth, +15 GW a year of reconductoring access and $12 billion a year at full strength). Five features make every builder run an upper bound:
- **It ramps to full effect by 2032** (line 460: a three-year ramp from 2030), faster than any real builder could site a line.
- **It adds linearly on top of permitting** (lines 461 and 464: its transmission growth and access are summed with the permitting package's, with no overlap), so the builder-plus-permitting gain is overstated.
- **It credits all 15 GW a year of reconductoring to the builder** (line 464), though most reconductoring would be done by incumbent utilities on their own systems once paid for.
- **It has no trigger and no supply limit:** it builds everywhere every year, not only where the one-year trigger is met, and never waits on transformers, crews or siting.
- **Its $12 billion a year is booked as a federal cost** (line 515, counted in the credits), though under CLI-10.02 and CLI-10.03 the builder's capital is borrowed and repaid through rates.

So `bld_hi`'s −1.43 Gt is the most a builder could add on this engine, not a forecast. M4 has been asked for a run with the builder at full strength together with the permitting package, to bound the overlap.

## How transmission actually gets built

The research (sources re-pulled November 14; registered as evidence) says money is rarely the binding input. Siting authority, cost allocation, equipment and lead time are.

- **The record is slow and getting slower.** About 435 miles of 345 kV and above were built in 2025 [{GS}] (the same firm's congestion report says 411), against 888 in 2024 and an average of 1,781 a year in 2010-14 [EV-CLP-051]. Interregional lines have come almost to a stop: no project has come from FERC Order 1000's interregional process since 2011 [{ROSNER}]. Projects built in 2025 waited about 61 months in interconnection queues [{LBNL}].
- **Regional plans are funded; execution binds.** MISO's Tranche 2.1 ($21.8 billion, 2032-34), SPP's 2025 plan ($8.6 billion, including about 949 miles of 765 kV), PJM's 2025 plan ($11.8 billion) and ERCOT's 765 kV build (about $33 billion) are approved and paid for through rates [{PLANS}]. Over 10,000 miles of 500 kV and above are planned by 2034, most of it in 2030-34 [{PLANS}]. In these regions a federal builder would duplicate, and compete for the same transformers and crews.
- **Equipment is short.** Power transformers run about 30% short of demand, with lead times around 128 weeks and about 80% imported [{XFMR}]; a September 2026 estimate puts North America and Europe's 2025 deficit at 38% [{XFMR2}].
- **Federal money has been offered and mostly not used.** WAPA's Transmission Infrastructure Program has $3.25 billion of borrowing authority and has financed two lines in seventeen years (the Montana-Alberta Tie Line in 2013 and ED5-Palo Verde in 2015), with about $76 million outstanding [{WAPA}]. DOE's Transmission Facilitation Program is nearly fully obligated; the 2025 reconciliation law (OBBBA) rescinded the unobligated IRA §50151 lending, about $389 million of §50152's siting grants, and §50153 [{OBBBA}].
- **Federal siting has no working path under current law.** FPA section 216's backstop permit, and its eminent domain (216(e)), apply only inside a DOE national-interest corridor (SRC-4771). DOE cancelled all three remaining corridors on August 12, 2026, citing in part a "lack of expressed developer interest in seeking FERC backstop siting authority" [{NIETC}] (second Trump administration; the cancellation is a fact, the reason its view).
- **Merchant lines show the time it takes.** SunZia took about 17 years to permit and was energized in 2026 [{SUNZIA}]; the Champlain Hudson Power Express (339 miles) entered service in May 2026 under a New York contract [{CHPE}]; Grain Belt Express lost its DOE guarantee in 2025 [EV-CLP-435], won 6-0 at the Illinois Supreme Court in January 2026, and has a federal permitting target of January 2027 [{GRAIN}].
- **Public power already owns a large share.** The power marketing administrations and TVA own about 14% of US transmission [{PMA}]; Bonneville's own portfolio, about $8 billion and 10 GW, is mostly rebuilds and reconductoring.
- **The pending permitting bill is the biggest lever.** BAAJA (S.5653; the Capito substitute, SA 6883 to H.R. 2347) passed procedural votes of 73-25 and 62-21 on November 9 and 10, with cloture ripening November 16; the dossier's sources put passage at about 22-27% (SRC-0155, SRC-0156). Its §2101 would drop the corridor requirement and have FERC permit lines of 230 kV and up after the state has had one year [{BAAJA}]. On the September 30 text, Rhodium finds interregional build of 1.9-2.6 TW-miles a year against 0.7 and up to 1.5 Gt less CO2 [{RHODIUM}]; RFF finds about 30% more transmission by 2041 and about 1.8 Gt less [{RFF}]; SRC-0155 puts transmission at 30-40% of its 2035 potential without the bill and 85-95% with it. The substitute preserves utilities' right of first refusal and exempts non-RTO utilities from §2106's planning duties [EV-CLP-263].

**Where a builder adds, and where it duplicates.** A federal builder of last resort adds most on cross-seam and interregional lines (DOE's July 2026 draft needs study values ERCOT ties at $31-48/MWh and SPP-WestConnect at $18-33/MWh [{NEEDS}]), in the non-RTO Southeast and West, on the public power systems' own lines (reconductoring), and as anchor offtaker for stranded merchant lines. It duplicates in the RTO regions and ERCOT, where $70 billion and more is approved and execution binds; there it competes for transformers and crews, and Treasury-rate financing could make "last resort" the default. That is why memo 9's account pays first for reconductoring, risk cover, equipment and siting grants, and only for ready-to-build work, and why the trigger and competitive-cost test stay.

## Limits

- The builder is a labeled assumption with the five generous features above. How fast a real builder can site lines is the open question [EV-CLP-435] [EV-CLP-437].
- Two of the model's benchmarks fail (HI-1, PR-2; `6-cost.md`, part 6, 1a): its near-term power cuts and early receipts lean high. The grid lever acts on wind and solar access rather than coal-to-gas switching, so the comparison between runs is less exposed than the levels.
- The household split of memo 9's options is not modeled: the household module reads the price, not where the payments go.
- M4's open #366 changes the engine; these figures are on main at `37ee069` and are refreshed if it moves them.

## Next

- The booking change for memo 9 B (tier 3, separate PR): CLI-3A's pay-out becomes grid-account outlays sized to ready-to-build need, with the rest kept as receipts.
- M4: a run with the builder at full strength plus permitting, to bound the overlap.
- CLI-10.03's siting text is corrected in `4-specification.md` (see the PR).
