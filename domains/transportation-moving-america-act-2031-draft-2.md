# Moving America Act of 2031 — Unified Bill (Draft 2)

Oct 12, 2026 · @espen

## The bill at a glance

The Moving America Act of 2031 authorizes **$936.57B** over FY2032-36 for highways, highway safety, public transportation and intercity passenger rail. Users pay for repair and the nation pays to build. Dedicated receipts cover **$545.84B**, and the general fund pays **$390.73B**, or **0.180% of GDP** a year. By FY2042-46 the draw falls to 0.026%. User fees then cover 95% of highway renewal and all of transit's and rail's, and from FY2040 a fossil transition premium on gasoline and diesel, which clean vehicles never pay, retires most of the remaining general fund.

This draft replaces the October 12 merge doc, which is kept as an archive. It merges the ARCA and ATRA architecture docs, the package section-by-section, the final revenue plan, and the division B redesign. Where this doc and any source disagree, this doc governs.

| Div. | Short title | Committees (House; Senate) | FY2032-36 | Drafting status |
| --- | --- | --- | --- | --- |
| A | Surface Transportation Trust Fund and Revenue | Ways and Means; Finance | Revenue; $123.70B expansion appropriations (sec. 105); top-up coordination (sec. 110) | All eleven sections drafted |
| B | Federal-Aid Highways and Highway Safety | T\&I; EPW, Commerce | $461.12B, plus $17.24B of general-fund grants subject to appropriation | Hybrid: H.R. 8870 title I by reference; ten sections drafted, eight specified |
| C | American Transit Renewal Act | T\&I; Banking | $221.42B | Titles II-III and secs. 401, 606, 706, 717 drafted; rest specified |
| D | American Rail Competitiveness Act | T\&I; Commerce | $254.03B, plus up to $25.00B readiness reserve, contingent | Title I and sec. 303 drafted here; ARCA drafts the rest |
| E | Research, Data and Project Delivery | T&I, Science; Commerce, EPW | about $1.0B | Specified |
| F | Budget Discipline and General Provisions | All | none | Specified |
|  | **Total, divisions B-D** |  | **$936.57B**: $812.87B renewal, $123.70B expansion |  |

### Four vehicles, one design

The bill is the last of four laws. Each carries only what it can legally carry.

| Vehicle | Votes | What it carries | Money |
| --- | --- | --- | --- |
| 2028 extension, by Sept 30, 2028 | 60 | Fuel taxes and fund credits extended one year, to Sept 30, 2029; a general-fund transfer that keeps both accounts solvent through FY2031 | Transfer not yet sized |
| 2029 reconciliation act | 51 | Creates the three-account fund; fuel taxes permanent, indexed and stepped from Oct 1, 2029; clean-vehicle per-mile charge and permanent truck excises; EV fee as a one-year bridge; package one; renewal top-ups for FY2032-35 | $47.0B package, $209.74B top-ups; net deficit reduction about $33.3B |
| 2030 reconciliation act | 51 | Weight-distance charge replacing the heavy-vehicle use tax; rail diesel tax; aviation surcharge; package two; renewal top-ups for FY2035-36 | $33.5B package, $57.33B top-ups; net deficit reduction about $4.2B |
| Moving America Act of 2031 | 60 | Divisions A-F: programs, contract authority within receipts, expansion appropriations, shares from FY2037, continuation, solvency backstop, privacy | $936.57B authorized |

**Calendar.** BUILD America 250-Plus (H.R. 8870, forecast as enacted) authorizes FY2027-31. This bill authorizes FY2032-36, and the next one FY2037-41. Amounts are nominal and were not re-indexed when the calendar moved a year **\[A-5\]**.

**How to read it.** A bold tag such as **\[A-12\]** marks a call listed under "Decisions and assumptions". Every figure comes from `index/tools/transportation/moving_america.py` (printed by `report.py`). Since Oct 20, 2026 it folds in the old overlay stack (`transit_fiscal_model.py` through `final_v3.py`, kept in `legacy/`) and reproduces its output line for line. The model counts budget authority by fiscal year, not outlays.

## Decisions and assumptions

Twenty-eight calls carry the bill. Seven were decided by Espen and are recorded so the alternative stays visible. The other twenty-one were made in drafting and are open for review. The numbering is new; "Was" gives the tag in the archived doc. Two old calls are retired: the FY2028 forcing event (replaced by A-9) and the Mass Transit Account carry-forward (sec. 110(a) now counts any balance automatically).

The calls most likely to change the bill's shape are A-9 (the 2028 extension), A-10 (the fuel-tax steps), A-23 (Interstate and Bridge Renewal) and A-28 (the fossil transition premium).

### Decided

| # | Was | Call | Alternative | What moves if overturned |
| --- | --- | --- | --- | --- |
| **A-1** | A-2 | Division letters A-F | Transit as B, or highways split from safety | Cross-references only |
| **A-2** | A-3 | Highway division is hybrid: H.R. 8870 title I by reference, plus drafted policy sections. All of division B is renewal except sec. 1112 | Draft title I in full, or class capacity grants as expansion | Each 5% of the highway program classed as expansion lowers highways' equal-coverage share about 3 points |
| **A-3** | A-4 | Transit operating tier: scenario B, $35.00B | Scenario C, $70.00B; or A, none | C: draw 0.196% avg, all-in peak 0.223%. A: 0.164%, all-in 0.193% |
| **A-4** | A-7 | 0.206% of GDP is a benchmark, not a cap. What binds is the reconciliation instructions, PAYGO and the Byrd rule | Treat it as a hard cap | FY2029-31 exceed it (0.225% in FY2030) and would have to shrink |
| **A-5** | A-16 | Nominal levels not re-indexed when the calendar moved a year | Multiply every line by 1.025 | Draw up about 0.004 points |
| **A-6** | A-6 | Joint terminals: div. D sec. 310 ($20.20B) is the single program for the five nodes; div. C sec. 606 retargeted elsewhere and cut to $3.00B | Split project by project | Up to $13.96B of terminal renewal falls to commuter operators' formula money (see division D) |
| **A-7** | A-5 | Incremental shares 35 / 50 / 15 through FY2036 | The equal-coverage solve, 50.5 / 37.6 / 12.0 | See A-8 |

### Open: revenue and the vehicles

| # | Was | Call | Alternative | What moves if overturned |
| --- | --- | --- | --- | --- |
| **A-8** | A-5 | Shares move to **45 / 40 / 15 from FY2037**, written into the 2031 bill | Keep 35 / 50 / 15 permanently | Kept, before the fossil premium: transit piles up $5.9B it cannot spend while highway renewal coverage sits at 80% in FY2042-46. With the move: 89 / 96 / 104, nothing stranded. The split does not change the total general-fund draw; it decides which account reaches self-sufficiency |
| **A-9** | A-20 | **No new revenue in FY2029.** A clean 2028 extension carries current rates and fund credits to Sept 30, 2029, plus a transfer keeping both accounts solvent through FY2031. New rates start Oct 1, 2029 (fuel), Oct 1, 2030 (per-mile, trucks, rail diesel) and Oct 1, 2031 (aviation) | Earlier starts, as in the retired designs | Without the extension, credits stop Oct 1, 2028 and FY2029 is a cash crisis. If the extension runs past FY2029, the forcing event for the 2029 act is lost, though reconciliation can still raise rates. Not modelled |
| **A-10** | A-19 | **Fuel taxes permanent and CPI-indexed from FY2030, plus ten Fix-It-First steps of 3¢** (2029 dollars), one a year, deferred (not forfeited) in any year gasoline averages over $4.00 indexed or rose over 20% | Indexing only; 2¢ steps; front-loaded increases | Indexing only: draw 0.267%, renewal coverage FY2042-46 62 / 42 / 75. 2¢ steps: 0.209%, 85 / 88 / 111. Three pauses: 0.204%, recovered later |
| **A-11** | A-10, A-19 | **Clean vehicles pay per mile at parity** with the road-use rate: the gasoline road-use rate ÷ 40 mpg for cars, the diesel road-use rate ÷ 6.5 for trucks, 30% of the car rate for plug-in hybrids. Parity is with what an efficient gas car would pay to keep roads funded in a fossil-dependent world, never with the fossil premium, so no clean car pays more per mile than a 40-mpg hybrid. Odometer only, location data barred, 10% collection-cost ceiling | Peg to 25 mpg, plug-ins at 50%; a flat fee; per-mile on all vehicles | A car pays 0.64¢ a mile in FY2031 ($77 a year at 12,000 miles), 1.17¢ in FY2036 ($141, the same as a 40-mpg hybrid) and 1.84¢ in FY2046 ($221, against $267 for the hybrid and $427 for a 25-mpg car). A plug-in driven 40% on electricity pays about $126 in FY2036. Pegging to 25 mpg with plug-ins at 50% would raise about $5.7B more in FY2032-36 |
| **A-12** | new | **Trucks over 26,000 lb pay a weight-distance charge** (3¢ average on Class 7-8 miles) in place of the heavy-vehicle use tax. Truck and tire excises made permanent, 4% for zero-emission trucks | A diesel increase alone; keep the use tax | At a 2¢ average: draw 0.185% avg, all-in peak 0.213% |
| **A-13** | A-18, A-22 | **Rail taxes:** rail diesel 15¢ / 7.5¢ keyed to Surface Transportation Board class, short lines exempt; aviation surcharge $4 → $16; the corridor competitiveness surcharge is dropped | A flat diesel rate; keep the surcharge | Rail's only dedicated receipts outside the split, $36.2B in FY2032-36. Without them rail coverage roughly halves. The surcharge was about $1B with its own machinery and an airline fight |
| **A-14** | A-21 | **Three money paths.** Contract authority from each account is capped at its receipts (div. A sec. 110(a)). Renewal top-ups are general-fund appropriations to programs in the 2029 and 2030 acts, since reconciliation cannot transfer into a trust fund. Expansion is appropriated in the 2031 bill (sec. 105) | General-fund transfers into the fund in the 2031 bill | No figure moves; it decides which vote carries the money. Sec. 110(c) keeps the transfer as a fallback |
| **A-15** | new | **Top-up placement:** the 2029 act carries FY2032-34 plus FY2035 highway and transit ($209.74B); the 2030 act carries FY2035 rail and FY2036 ($57.33B) | Split by fiscal year (FY2032-34 / FY2035-36) | By fiscal year the 2030 act would add about $27.5B to deficits and fail the Byrd out-year test without offsets. As placed, both acts reduce deficits |
| **A-16** | A-8 | **Reconciliation money obligates over FY2029-31,** ramping with mid-year enactment: rail $6.0B / 17.0 / 25.5, transit $4.0B / 13.0 / 15.0 | Obligate each package in its enactment year | Enactment-year timing puts $35B of rail obligations into a half-year and leaves rail at $13.3B in FY2031, a $26.7B cliff into FY2032 |
| **A-17** | A-13 | **Sec. 108: report and recommend at 0.206%, plus a capped solvency backstop** ($25B over FY2032-36) for accounts that run short when steps pause | A hard GDP trigger | A trigger buys no CBO credit unless projected to fire. Three pauses cost about $53.3B of FY2032-36 receipts |
| **A-18** | A-11 | **Sec. 1112's general-fund grants count against the benchmark** ($17.24B) | Leave them out, since they are subject to appropriation | Counted, FY2032 reaches 0.208%, 0.002 points over |

### Open: programs

| # | Was | Call | Alternative | What moves if overturned |
| --- | --- | --- | --- | --- |
| **A-19** | A-15 | **One renewal definition** for all three accounts (div. A sec. 101(f)); continuation and solvency cross-refer to it | ARCA's narrower list (secs. 201-205) | Rail continuation would carry $12.62B in FY2036, not $34.44B |
| **A-20** | A-17 | **Drafted dates shift one year, except the 5307(i)(4) base years** (service hours FY2028-30, preventive maintenance FY2027-29) | Shift the base years too | Shifting adds FY2031, the year with the most reconciliation operating money, to the service floor |
| **A-21** | A-12 | **Tier 1 corridor cap fixed in dollars:** $14.0B under sec. 303, $19.25B with the reserve | A percentage cap | A percentage loosens exactly when the program grows |
| **A-22** | A-14 | **Readiness reserve illustrated at $0 / 0 / 5 / 8 / 12B** | ARCA's 0 / 5 / 7 / 7 / 6 | Presentation only; release follows gate clearance. Back-loading keeps the reserve out of FY2032-33, the tight years |
| **A-23** | new | **Interstate and Bridge Renewal (div. B sec. 1104):** H.R. 8870's competitive bridge program ($2B a year, subject to appropriation) becomes contract authority, plus new money of $0 / 2 / 4 / 6 / 8B. 80% formula, 20% large projects. Tolling allowed on reconstructed segments | Keep the bridge program competitive and appropriated; size it larger | $30.77B over FY2032-36. Each $2B a year more adds about 0.005 points to the draw. New money starts at zero because FY2032 has no room |
| **A-24** | new | **Fix-it-first with teeth (sec. 1106):** States below their condition targets shift NHPP to preservation; a lifecycle test for projects over $100M adding lanes; federal share 70% (Interstate 80%) for new general-purpose lanes | H.R. 8870's biennial review only | No federal cost. State DOTs and ARTBA will resist strings on formula money; the share cut is the tradeable part |
| **A-25** | new | **Safe System and local access (secs. 1109, 1115):** SS4A planning share 15%; HSIP limited to proven countermeasures where targets regress; STBG suballocation 60% | H.R. 8870 (5% planning share, report only, 55%) | No federal cost |
| **A-26** | new | **Resilience, clean fuels, freight (secs. 1110, 1113, 1114):** 4% NHPP resilience set-aside; the Carbon Reduction Program restored as 2% of each State's formula money; CMAQ alternative-fuel set-aside held at 10%; 91,000-lb pilot ends Sept 30, 2031; 15% of freight formula to truck parking | Restore CRP as new money; leave CRP repealed; keep the pilot | All within the top line, but the set-asides take about $2.6B a year of formula money out of State discretion. CRP as new money would add about $1.3B a year |
| **A-27** | new | **Charging Gap Program replaces NEVI (div. B sec. 1116):** $0.5B a year from formula money, rising 2.5%; national reverse auctions on a published gap map; half paid at energization, half over five years for uptime; 24 months to energize or the award lapses; 40% for medium and heavy trucks, 30% rural; unspent NEVI balances folded in | Restore NEVI as a State formula program; or no charging program | $2.63B over FY2032-36, no new federal money. Auction-and-performance payment is untested at federal scale for charging; the lapse rule and the uptime holdback are what make it faster than NEVI |
| **A-28** | new | **Fossil transition premium (div. A sec. 103):** after the ten Fix-It-First steps, gasoline and diesel take five more steps of 2¢ (2029 dollars), FY2040-44, under the same price pause. Clean vehicles never pay it. Receipts go to the accounts in proportion to their remaining general-fund need. Enacted in the 2029 act, so it scores nothing inside either reconciliation window | No premium; or a larger, open-ended one | No change in FY2032-36. Without it, FY2042-46 draws 0.065% instead of 0.026% and renewal coverage is 89 / 96 / 104 instead of 95 / 109 / 135. The FY2042-46 receipts ($124.8B) are an upper bound, since the model has no demand response. Credited by the regular split it strands nothing in the base case, but it stranded $28.9B in transit under a 25-mpg peg; crediting by need is the insurance |

## The fiscal architecture

Dedicated revenue pays $545.84B of the $936.57B, and the general fund pays $390.73B: **0.180% of GDP a year, peaking at 0.200% in FY2032**. The draw falls to 0.067% in FY2037-41 and 0.026% in FY2042-46, about $17.1B a year, mostly for new rail lines. Transit's renewal programs become self-sufficient in FY2036 and rail's in FY2040; highway renewal reaches 95% coverage in FY2042-46. The fossil transition premium, from FY2040, does most of the late work.

### The design

- **Users pay for repair; the nation pays to build.** Dedicated receipts fund renewal: roads, bridges, transit and rail kept in good repair. Expansion (CIG, Tier 1 high-speed rail, terminals, new corridors) is a general-fund national investment.
- **Fossil fuel pays more over time; clean vehicles pay for road use.** Clean vehicles pay per mile at parity with the road-use part of the fuel tax, what an efficient 40-mpg gas car would pay to keep roads funded in a fossil-dependent world. From FY2040, gasoline and diesel also pay a fossil transition premium that clean vehicles never pay **\[A-28\]**.
- **One fund, three accounts.** The Highway and Mass Transit Accounts are credited their FY2028 receipts first, CPI-indexed. Receipts above those floors split **35 / 50 / 15** through FY2036 **\[A-7\]** and **45 / 40 / 15** from FY2037 **\[A-8\]**. Rail's own taxes go to the rail account, and premium receipts go wherever the general fund is still paying.
- **Revenue in five parts:**
  1. fuel taxes made permanent, indexed, and raised 3¢ a year for ten years with a gas-price pause **\[A-10\]**;
  2. clean vehicles pay per mile at the road-use rate **\[A-11\]**;
  3. trucks over 26,000 lb pay a weight-distance charge in place of the 1982 use tax **\[A-12\]**;
  4. rail's own diesel and aviation taxes **\[A-13\]**;
  5. from FY2040, a fossil transition premium on gasoline and diesel, 2¢ a year for five years **\[A-28\]**.
- **Three money paths, each in the vehicle that can carry it** **\[A-14\]**: the fund pays contract authority within its receipts; reconciliation appropriates renewal top-ups to programs; the 2031 bill appropriates expansion.

### Why this revenue design

The earlier design charged every vehicle per mile while fuel taxes phased out. It is retired for three reasons:

- **It hid a large increase.** For a 25-mpg car it was the equivalent of about 24¢ a gallon more in its first year, rising to about 90¢ by FY2042. In the Mineta Transportation Institute's 2024 survey, 74% backed a 10¢ gas-tax increase dedicated to maintenance; mileage fees draw weaker support.
- **It charged an 80,000-lb truck the same per mile as a sedan.**
- **It could not have started when assumed.** It credited per-mile revenue from FY2029, which no collection system could deliver **\[A-9\]**.

The replacement asks less of car drivers in every year through FY2036, and more of the heaviest trucks. Each remaining piece earns its complexity:

| Piece | Why it stays |
| --- | --- |
| Fix-It-First steps, 3¢ a year for ten years | The revenue engine. Indexing alone leaves FY2032-36 at 0.267% and renewal coverage at 62 / 42 / 75 |
| Gas-price pause | The political price of the steps after the 2022-26 price shocks. Paused steps resume, so long-run revenue is unchanged |
| Clean-vehicle charge at the road-use rate | Without it, the fastest-growing part of the fleet pays nothing once the EV fee ends. Tying it to the road-use rate leaves one number to argue about and keeps the premium off clean vehicles |
| Weight-distance charge | Fuel taxes cannot price axle weight, and the use tax has been flat, capped at $550 and unindexed since 1982. It replaces the use tax rather than adding a layer |
| Rail diesel and aviation taxes | Rail's only dedicated receipts outside the split |
| Share change in FY2037 | Without it, transit strands $5.9B while highway renewal sits at 80% |
| Fossil transition premium, FY2040-44 | The long-run signal: from 2040, fossil fuel pays more than road use costs and clean vehicles do not. It also retires most of the FY2042-46 general-fund draw |

### Dedicated revenue by source ($B)

| FY | Gasoline | Diesel | Other fund taxes | EV fee | Clean-car per-mile | Clean-truck per-mile | Weight-distance | Rail taxes | Fossil premium | **Total** |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2029 | 27.1 | 14.6 | 7.5 | — | — | — | — | — | — | **49.3** |
| 2030 | 32.6 | 16.8 | 7.6 | 1.2 | — | — | — | — | — | **58.2** |
| 2031 | 38.5 | 19.1 | 6.3 | — | 0.7 | 0.3 | 6.4 | 0.4 | — | **71.6** |
| 2032 | 44.7 | 21.4 | 6.4 | — | 1.0 | 0.5 | 6.6 | 3.7 | — | **84.3** |
| 2033 | 51.3 | 23.8 | 6.4 | — | 1.3 | 0.8 | 6.9 | 5.4 | — | **96.0** |
| 2034 | 58.4 | 26.4 | 6.5 | — | 1.6 | 1.1 | 7.2 | 7.2 | — | **108.4** |
| 2035 | 65.9 | 29.0 | 6.6 | — | 2.0 | 1.5 | 7.4 | 9.0 | — | **121.5** |
| 2036 | 73.9 | 31.8 | 6.7 | — | 2.6 | 2.0 | 7.7 | 10.9 | — | **135.6** |
| **FY2032-36** | 294.2 | 132.5 | 32.6 | — | 8.5 | 6.0 | 35.8 | 36.2 | — | **545.8** |
| FY2037-41 | 462.8 | 180.7 | 33.0 | — | 23.9 | 24.0 | 43.6 | 63.7 | 16.3 | **848.0** |
| FY2042-46 | 525.8 | 178.3 | 31.4 | — | 43.5 | 51.0 | 53.2 | 80.9 | 124.8 | **1,088.9** |

- FY2029 is current-law rates, carried by the 2028 extension **\[A-9\]**.
- "Other fund taxes" are the truck sales and tire taxes, net of the 4% zero-emission rate, plus the use tax until it ends Sept 30, 2030.
- For a 25-mpg car driven 12,000 miles, federal fuel tax goes from $88 today to $105 in FY2030, $142 in FY2032 and $225 in FY2036.
- With no pauses, gasoline reaches 62.0¢ nominal in FY2039, the last step: 48.4¢ in 2029 dollars, against 45.3¢ for the 1993 rate in 2029 dollars.

### How FY2032-36 is paid for ($B)

|  | Highways | Transit | Rail | Total |
| --- | --- | --- | --- | --- |
| Program | 461.12 | 221.42 | 254.03 | **936.57** |
| Dedicated receipts | 321.19 | 154.27 | 70.38 | **545.84** |
| General fund | 139.93 | 67.15 | 183.65 | **390.73** |
| — expansion, div. A sec. 105 (2031 bill) | — | 30.46 | 93.20 | 123.66 |
| — renewal top-ups, 2029 and 2030 acts **\[A-14\]** | 139.93 | 36.69 | 90.45 | 267.07 |
| Whole-program coverage | 70% | 70% | 28% | 58% |
| Renewal coverage | 70% | 81% | 44% |  |

Transit draws $30.46B of general-fund expansion, not the full $30.50B authorized, because in FY2036 its own receipts start covering part of CIG. The highway top-up is the largest, $28.55B in FY2032 easing to $26.99B in FY2036, because the Interstate and Bridge Renewal program adds need about as fast as the steps add receipts **\[A-23\]**.

### The draw, by period

| Period | Draw, avg / peak (year) | Peak with sec. 1112 **\[A-18\]** | CBO net basis, peak | Whole-program coverage, hwy / transit / rail |
| --- | --- | --- | --- | --- |
| FY2027-28 (250-Plus) | 0.171% / 0.173% (2027) | 0.189% | 0.173% | 55 / 36 / 0 |
| FY2029-31 (250-Plus + reconciliation) | 0.212% / 0.225% (2030) | 0.239% | 0.231% | 60 / 38 / 5 |
| **FY2032-36 (this bill)** | **0.180% / 0.200% (2032)** | **0.208%** | **0.220%** | **70 / 70 / 28** |
| FY2037-41 | 0.067% / 0.100% (2037) | 0.108% | 0.143% | 89 / 85 / 64 |
| FY2042-46 | 0.026% / 0.041% (2042) | 0.048% | 0.098% | 95 / 93 / 86 |

FY2029-31 runs over the benchmark under any design: it carries 250-Plus's own shortfall plus the reconciliation money, before most new rates start. That is accepted **\[A-4\]**. The CBO basis nets out the 25% income and payroll tax offset on new excise receipts. Renewal coverage in FY2042-46 is 95 / 109 / 135.

### Room under the benchmark, FY2032-36 ($B a year)

|  | FY2032 | FY2033 | FY2034 | FY2035 | FY2036 |
| --- | --- | --- | --- | --- | --- |
| Room, base case | 2.50 | 4.14 | 9.12 | 15.74 | 24.85 |
| Less sec. 1112 grants **\[A-18\]** | −0.78 | 0.77 | 5.68 | 12.21 | 21.23 |
| Less the readiness reserve at 0 / 0 / 5 / 8 / 12 **\[A-22\]** | **−0.78** | 0.77 | 0.68 | 4.21 | 9.23 |

FY2032 is the tight year: with everything counted the draw is 0.208%, 0.002 points over the benchmark, which A-4 accepts. That is why the Interstate and Bridge Renewal program's new money starts at zero and builds $2B a year.

### What breaks this

| Change | Draw FY2032-36, avg / peak | All-in peak | Draw FY2042-46, avg | Renewal coverage FY2042-46 |
| --- | --- | --- | --- | --- |
| **Base case** | 0.180% / 0.200% | 0.208% | 0.026% | 95 / 109 / 135 |
| Three pauses (FY2032, 2035, 2038), resumed later | 0.204% / 0.217% | 0.231% | 0.026% | 95 / 109 / 135 |
| Steps of 2¢, not 3¢ | 0.209% / 0.219% | 0.233% | 0.076% | 85 / 88 / 111 |
| Weight-distance at a 2¢ average | 0.185% / 0.205% | 0.213% | 0.032% | 94 / 107 / 132 |
| Indexing only, no steps | 0.267% / 0.274% | 0.306% | 0.174% | 62 / 42 / 75 |
| No fossil premium **\[A-28\]** | 0.180% / 0.200% | 0.208% | 0.065% | 89 / 96 / 104 |
| Clean cars pegged to 25 mpg, plug-ins at 50% **\[A-11\]** | 0.177% / 0.198% | 0.206% | 0.017% | 97 / 113 / 141 |
| Operating tier doubled, scenario C **\[A-3\]** | 0.196% / 0.215% | 0.223% | 0.043% | 94 / 97 / 129 |
| No operating tier, scenario A | 0.164% / 0.185% | 0.193% | 0.010% | 98 / 122 / 146 |
| No 2028 extension **\[A-9\]** | not modelled | — | — | — |

The steps are the load-bearing piece. Pauses only delay them; smaller steps, or none, cost real coverage. In FY2042-46 dedicated receipts run about $217.8B a year against $234.9B of programs, and the general-fund draw falls from $78.1B a year in FY2032-36 to $17.1B, mostly rail expansion. The premium's receipts ($124.8B in FY2042-46) are an upper bound: the model has no demand response, and a premium meant to move drivers off fossil fuel shrinks its own base.

**Not modelled:** a trust-fund cash-flow model (balances and outlay timing), a CBO or JCT score, and fuel demand response to the steps, probably 2-3% of fuel receipts. All three are needed before the bill is scored.

## The vehicles: 2028 extension, 2029 and 2030 reconciliation acts

Most of the money and all of the revenue are law before the 2031 bill arrives. The 2029 act enacts the revenue structure and $256.74B of spending; the 2030 act adds the truck and rail taxes and $90.83B more. Both reduce deficits over their windows, about $33.3B and $4.2B. Every spending line is a general-fund appropriation "to carry out" an existing program, with obligation and expenditure deadlines, so it clears the Byrd rule. Conditions ride on the new money only.

### The 2028 extension

Current law ends fund credits for taxes received after Sept 30, 2028 and drops the fuel rates to 4.3¢. The design needs one clean 60-vote extension before then **\[A-9\]**:

1. Extend 26 U.S.C. 9503(b) and (e) and the expiring rates for one year, to Sept 30, 2029, with no change to the Mass Transit Account's 2.86¢ and no merger of the accounts.
2. Carry a general-fund transfer that keeps both accounts solvent through FY2031. Reconciliation cannot make that transfer later, and 250-Plus's $108.0B covers only CBO's shortfall through FY2030.
3. Extend the heavy-vehicle use tax to Sept 30, 2030, so it runs until the weight-distance charge starts.

A one-year extension keeps the forcing event: the 2029 act has an expiring tax base to reform, not merely rates to raise.

### What the Byrd rule allows

| Instrument | Status | Basis |
| --- | --- | --- |
| General-fund grants to carry out an existing program (5307, 5337, 5309, 24911, Amtrak grants, title 23 formula programs) | Available | Direct spending; the American Rescue Plan put $30.46B into transit this way |
| The same, for future fiscal years (the FY2032-36 renewal top-ups) | Available, with deadlines inside the window | Direct spending; the out-year test runs title by title, so each spending title needs its own expenditure deadline |
| Conditions on that money: operating eligibility, maintenance of effort, service floors, preservation-only use | Available | Terms "under which mandatory outlays are made" |
| Fuel-tax rates, indexing and steps; the clean-vehicle and weight-distance charges defined by odometer and distance records; truck excises; rail diesel; aviation surcharge, all credited to the fund | Available | Revenue; the 1990 motor-fuel precedent |
| Creating the accounts and setting their shares of receipts | Available, inside the revenue title | It directs where receipts are credited |
| Credit subsidy (RRIF, TIFIA) | Available, and the cleanest | FCRA scores the subsidy at obligation |
| Capital grants for projects not yet under agreement, CIG and greenfield rail included | Available with deadlines | ARP sec. 3401 precedent |
| General-fund transfer into the trust fund | Barred | Intragovernmental, no budgetary effect. This is why top-ups go to programs, and why the transfer survives only as the 2031 bill's fallback (div. A sec. 110(c)) |
| Contract authority under an obligation limitation | Barred | Outlays score to appropriations |
| Location-data bar, retention limits, private right of action; striking "capital" from 9503(e)(3) | Doubtful or barred | No budgetary effect of their own; they ride in the 2031 bill (div. A secs. 101(g), 111) |
| Amending program design, preference enforcement, Amtrak reorganization, permitting | Barred | Policy with merely incidental budgetary effect |

### The packages

| Package and line | Authority | Amount | Condition |
| --- | --- | --- | --- |
| **One (2029 act): rail** |  | **$35.00B** |  |
| RRIF credit risk premium subsidy | 49 U.S.C. 22402 | $6.00B | Supports $35-50B of lending |
| Zero-emission rail: electrification and trainsets | 22907, 24911 | $9.00B | Discrete segments, firm orders |
| State-of-good-repair backlog, NEC and national | 24911, Amtrak grants | $8.00B | Documented, designed work |
| Amtrak long-distance fleet replacement | Amtrak grants | $5.50B | Firm delivery schedule |
| Corridor ID planning and design | 25101 | $3.50B | 100% federal share below a sponsor-capacity threshold |
| Station access and ADA | Amtrak grants | $3.00B | Amtrak-served stations only |
| **One (2029 act): transit** |  | **$12.00B** |  |
| Operating transition grants | 5307 | $4.00B | Support held at 3-year average; service hours at least 95% of base |
| State of good repair, shovel-ready backlog | 5337 | $4.00B | Projects in asset management plans |
| Bus and railcar replacement | 5339, 5337 | $3.00B | Firm orders |
| Credit subsidy, transit and joint development | TIFIA | $1.00B | Scores at obligation |
| **One (2029 act): revenue** | 26 U.S.C. 9503; new ch. 36 subch. E | receipts | Three-account fund created; fuel taxes permanent, indexed and stepped from Oct 1, 2029; clean-vehicle charge from Oct 1, 2030; truck and tire excises permanent, 4% for zero-emission trucks; EV fee into the fund for FY2030, then ended |
| **Two (2030 act): rail** |  | **$13.50B** |  |
| RRIF credit risk premium, second tranche | 22402 | $4.00B | As above |
| Grade crossing elimination | 22909 | $4.00B | Discrete, locally delivered |
| Electrification, second tranche | 24911 | $3.00B | As above |
| Workforce and domestic supplier base | 22907 | $2.50B | Grants and cooperative agreements |
| **Two (2030 act): transit** |  | **$20.00B** |  |
| Operating transition grants | 5307 | $5.00B | As in package one |
| State of good repair | 5337 | $6.00B | As above |
| Bus replacement | 5339 | $1.00B | Firm orders |
| Station accessibility | 5337, ASAP | $3.00B | Rail transit and commuter stations only |
| Capital Investment Grants | 5309 | $3.00B | Executed agreements plus projects that sign by the deadline |
| Credit subsidy | TIFIA | $1.00B | Scores at obligation |
| Workforce and FTA capacity | 5314, admin | $1.00B | Grants and salaries |
| **Two (2030 act): revenue** | 26 U.S.C. 4495, 4481, 4041(a)(1)(C)(ii), 4283 | receipts | Weight-distance charge from Oct 1, 2030, replacing the use tax; rail diesel 10¢ / 5¢ from Oct 1, 2030 and 15¢ / 7.5¢ from Oct 1, 2031; aviation surcharge $4 from FY2032; rail taxes to the rail account |
| **Total packages** |  | **$80.50B** | One $47.00B, two $33.50B |

The two station lines do not overlap: package one covers Amtrak-served stations, package two rail transit and commuter stations.

### When the package money obligates **\[A-16\]**

The 2029 act will pass partway through FY2029, so little can obligate that year. The schedule ramps into FY2031, so the step into FY2032 is a ramp, not a cliff.

| $B obligated | FY2029 | FY2030 | FY2031 | Total |
| --- | --- | --- | --- | --- |
| Rail, package one | 6.0 | 13.0 | 16.0 | 35.0 |
| Rail, package two | — | 4.0 | 9.5 | 13.5 |
| Transit, package one | 4.0 | 4.0 | 4.0 | 12.0 |
| Transit, package two | — | 9.0 | 11.0 | 20.0 |
| **Rail program incl. 250-Plus** | 17.90 | 29.90 | 38.80 | FY2032: 39.95 |
| **Transit program incl. 250-Plus** | 23.93 | 33.24 | 35.71 | FY2032: 40.30 |
| Draw, % of GDP | 0.194% | 0.225% | 0.215% |  |
| Draw, CBO net basis | 0.194% | 0.231% | 0.229% |  |

Every package line must be obligated by **Sept 30, 2031**, and capital lines expended by Sept 30, 2036. Credit subsidy lines need no expenditure deadline.

### Renewal top-ups **\[A-14, A-15\]**

The renewal shortfall that dedicated receipts cannot yet cover reaches programs directly. The top-ups fall every year because receipts rise every year; transit's reaches zero in FY2036.

| $B | FY2032 | FY2033 | FY2034 | FY2035 | FY2036 | Total |
| --- | --- | --- | --- | --- | --- | --- |
| Highways (title 23 formula programs) | 28.55 | 28.47 | 28.20 | 27.72 | 26.99 | 139.93 |
| Transit (5307, 5337, 5339, 5311) | 14.04 | 11.01 | 7.68 | 3.96 | 0.00 | 36.69 |
| Rail (Amtrak grants, 24911, 22907, 22909) | 20.60 | 20.44 | 19.07 | 16.65 | 13.69 | 90.45 |
| **Total** | **63.19** | **59.92** | **54.95** | **48.33** | **40.68** | **267.07** |
| Enacted in | 2029 act | 2029 act | 2029 act | 2029 act: highways and transit, $31.68B. 2030 act: rail, $16.65B | 2030 act |  |

The 2029 act carries **$209.74B** and the 2030 act **$57.33B**. Highway top-ups are limited to preservation, rehabilitation and reconstruction: fix-it-first in practice, and the work that spends fastest. The 2029 act's money must be obligated by Sept 30, 2036 and spent by Sept 30, 2038; the 2030 act's by Sept 30, 2037 and Sept 30, 2039.

Locking the top-ups in 2029-30 has two payoffs. The 60-vote bill then carries only the expansion appropriations. And renewal funding survives even if the 2031 bill stalls or the 2030 midterms end the trifecta, because the money flows to existing formula programs either way.

### Score by act ($B over each window)

|  | 2029 act, FY2029-38 | 2030 act, FY2030-39 |
| --- | --- | --- |
| Fuel taxes: indexing and steps | +380.4 | — |
| Zero-emission truck excise at 4% | −8.4 | — |
| EV fee ended after FY2030 | −14.7 | — |
| Clean-car per-mile charge | +16.5 | — |
| Clean-truck per-mile charge | +12.9 | — |
| Weight-distance charge | — | +67.3 |
| Use tax repealed | — | −13.9 |
| Rail diesel and aviation surcharge | — | +73.3 |
| **Revenue, gross** | **+386.7** | **+126.7** |
| **Revenue, net of the 25% income and payroll offset** | **+290.0** | **+95.0** |
| Package | −47.00 | −33.50 |
| Renewal top-ups | −209.74 | −57.33 |
| **Net deficit reduction** | **about +33.3** | **about +4.2** |

The fossil transition premium, also enacted in the 2029 act, starts in FY2040, outside both windows, so it scores nothing here. The baseline follows CBO's convention: expiring trust-fund excises continue at current rates, and the 250-Plus EV fee runs to the general fund through FY2036. Spending is budget authority; with the deadlines above it all outlays inside each window. These are this project's estimates, not a JCT or CBO score.

### The instructions

Both budget resolutions instruct Ways and Means and Finance as well as T&I, Commerce, Banking and EPW, because the revenue lines are the point. Each instruction is sized to the net score above. Rail's credit subsidy is the most efficient line in either package: at quoted risk premiums, $10B supports $60-80B of face-value lending.

## Division A — Surface Transportation Trust Fund and Revenue

Division A turns the Highway Trust Fund into a three-account Surface Transportation Trust Fund and sets the revenue that fills it. Most of it is law before the 2031 bill: the 2029 act creates the fund and enacts secs. 102, 103 and 104(c); the 2030 act enacts the rest of sec. 104. The 2031 bill restates those sections in final form, adds the FY2037 shares, and carries what reconciliation cannot: contract authority, expansion appropriations, continuation, reporting, the solvency backstop and the privacy statute. Each section reads as it will once all three acts are law; counsel converts the earlier enactments into amendments "to read as follows". Finance will conform Code section numbers.

| Sec. | Provision | Statute | Enacted in | FY2032-36 |
| --- | --- | --- | --- | --- |
| 101 | Fund, accounts, base amounts, shares (35 / 50 / 15; 45 / 40 / 15 from FY2037), renewal and expansion defined | 26 U.S.C. 9503 | 2029 act; FY2037 shares 2031 bill | — |
| 102 | Clean-vehicle road user charge at parity | new 26 U.S.C. 4491-4493 | 2029 act, effective Oct 1, 2030 | $14.5B |
| 103 | Fuel taxes permanent and indexed; Fix-It-First steps with a price pause; fossil transition premium from FY2040; EV fee bridge; permanent fund credits | 26 U.S.C. 4081, 9503; 250-Plus sec. 1129 | 2029 act, effective Oct 1, 2029 | $426.7B (all fuel tax) |
| 104 | Weight-distance charge replacing the use tax; truck and tire excises permanent (4% for zero-emission trucks); aviation surcharge; rail diesel | 26 U.S.C. 4495, 4481, 4051, 4071, 4283, 4041, 9503 | Excises 2029 act; the rest 2030 act | $35.8B + $36.2B rail |
| 105 | Mandatory appropriations for expansion | Freestanding | 2031 bill | $123.70B |
| 106 | Contract authority, contingent commitments, readiness reserve | Freestanding | 2031 bill | up to $25.00B, contingent |
| 107 | Continuation on lapse | Freestanding | 2031 bill | — |
| 108 | Reporting, recommendation, solvency backstop | Freestanding; 9503(d) | 2031 bill | contingent, capped at $25B |
| 109 | Joint facilities | 49 U.S.C. 5309(q)(4) | 2031 bill | — |
| 110 | Contract authority within receipts; coordination with the reconciliation top-ups | Freestanding | Top-ups 2029 and 2030 acts; coordination 2031 bill | $267.07B top-ups |
| 111 | Privacy and administration of the road user charges | new 26 U.S.C. 4494; 4492-4493 | 2031 bill | — |

### Sec. 101. Surface Transportation Trust Fund

One renewal definition serves all three accounts **\[A-19\]**; sec. 1112 sits outside both classes **\[A-18\]**. The rail diesel tax is the train rate in 4041(a)(1)(C)(ii) (clause (iii) is buses), and 4283, repealed in 1990, is re-used by sec. 104. Subsection (d)(1) is the 2029 act's text; (d)(2) is added by the 2031 bill **\[A-8\]**.

```
SEC. 101. SURFACE TRANSPORTATION TRUST FUND.

(a) REDESIGNATION.—Section 9503 of the Internal Revenue Code of 1986 is
amended by striking "Highway Trust Fund" each place it appears and inserting
"Surface Transportation Trust Fund".

(b) ACCOUNTS.—The Fund shall consist of a Highway Account, the Mass Transit
Account established by section 9503(e), and an Intercity Passenger Rail
Account.

(c) BASE AMOUNTS.—For fiscal year 2029 and each fiscal year thereafter there
shall be credited to the Highway Account and to the Mass Transit Account,
before any amount is credited under subsection (d), an amount equal to the
amount credited to that account for fiscal year 2028, increased by the
percentage change in the Consumer Price Index for All Urban Consumers since
fiscal year 2028. If receipts are less than the sum of the two base amounts,
each account shall be credited in proportion to its base amount.

(d) NEW REVENUE.—Of amounts credited to the Fund for a fiscal year in excess
of the base amounts under subsection (c)—
  (1) for fiscal years 2029 through 2036, 35 percent shall be credited to
  the Highway Account, 50 percent to the Mass Transit Account, and 15
  percent to the Intercity Passenger Rail Account; and
  (2) for fiscal year 2037 and each fiscal year thereafter, 45 percent shall
  be credited to the Highway Account, 40 percent to the Mass Transit
  Account, and 15 percent to the Intercity Passenger Rail Account, unless
  a later Act provides otherwise after the report under subsection (i).

(e) RAIL-SPECIFIC RECEIPTS.—Taxes received under section 4283 of such Code
(as added by section 104 of this division), and under section
4041(a)(1)(C)(ii) of such Code to the extent attributable to the rates in
subclauses (IV) and (V) thereof, shall be credited to the Intercity Passenger
Rail Account and shall not be taken into account under subsection (c) or (d).

(f) RENEWAL AND EXPANSION.—
  (1) RENEWAL FIRST.—Amounts in an account shall be available for the
  expansion programs of that account only to the extent they exceed the
  amounts made available for that fiscal year for its renewal programs.
  (2) EXPANSION PROGRAMS.—For purposes of divisions A through D, the
  expansion programs are—
    (A) the program carried out with amounts appropriated by section
    105(a)(1) of this division under section 5309 of title 49, United States
    Code;
    (B) section 606 of division C;
    (C) sections 303, 310, 311 and 312 of division D; and
    (D) the readiness reserve under section 106(e) of this division.
  (3) RENEWAL PROGRAMS.—For purposes of divisions A through D, the renewal
  programs are—
    (A) of the Highway Account, every program for which amounts are made
    available from that Account by division B or by title 23, United States
    Code, including the programs of the National Highway Traffic Safety
    Administration and the Federal Motor Carrier Safety Administration;
    (B) of the Mass Transit Account, every program under chapter 53 of title
    49, United States Code, and under division C, other than an expansion
    program; and
    (C) of the Intercity Passenger Rail Account, every program under
    division D other than an expansion program.
  (4) EXCLUSION.—Section 1112 of division B is neither a renewal program nor
  an expansion program of any account.

(g) MASS TRANSIT ACCOUNT EXPENDITURES.—Section 9503(e)(3) of such Code is
amended by striking "capital or capital related expenditures (including
capital expenditures for new projects)" and inserting "expenditures
authorized under chapter 53 of title 49, United States Code".

(h) SUBACCOUNTS.—The subaccounts established by section 101(b) of division D
shall be maintained within the Intercity Passenger Rail Account.

(i) RESETTING THE SHARES.—Not later than 18 months before the expiration of
each authorization of appropriations from the Fund, the Secretary of the
Treasury and the Secretary of Transportation shall report to the Committees
the percentages under subsection (d) that would result in dedicated receipts
covering an equal share of the renewal programs of each account over the
following 10 fiscal years, and whether further steps under section
4081(a)(2)(E)(iv) of such Code should be taken.

(j) PARITY.—It is the policy of the United States that Federal assistance
for intercity passenger rail and public transportation, combined, shall
equal Federal assistance for highways by fiscal year 2045.

(k) COMMITTEES.—In this division, the term "Committees" means the Committee
on Ways and Means and the Committee on Transportation and Infrastructure of
the House of Representatives and the Committee on Finance, the Committee on
Environment and Public Works, the Committee on Banking, Housing, and Urban
Affairs, and the Committee on Commerce, Science, and Transportation of the
Senate.

(l) FOSSIL TRANSITION RECEIPTS.—Receipts attributable to the fossil
transition amount under section 4081(a)(2)(E)(iv) of such Code shall not
be taken into account under subsection (c) or (d), and shall be credited
among the accounts in proportion to the amounts by which obligations for
each account's programs are projected, in the most recent report under
section 108(a), to exceed its other receipts for the fiscal year or, if no
account is so projected, under subsection (d).

(m) POLICY.—It is the policy of the United States to reduce the dependence
of surface transportation on fossil fuels. Clean vehicles shall pay for
their use of the roads at the road-use rate, and shall not bear the fossil
transition amount.
```

### Sec. 102. Clean-vehicle road user charge

Electric and fuel-cell vehicles pay per mile at a rate written as parity with the road-use part of the fuel tax **\[A-11\]**. A car pays the gasoline road-use rate divided by 40 mpg, the fuel economy of an efficient hybrid (0.64¢ a mile in FY2031, 1.17¢ in FY2036, 1.84¢ in FY2046); a truck pays the diesel road-use rate divided by 6.5 mpg. The road-use rate is the base rate, the Fix-It-First steps and indexing: what gas cars would pay to keep roads funded in a fossil-dependent world. It never includes the fossil transition premium, so no clean car pays more per mile than a 40-mpg hybrid, and from FY2040 it pays less; the gap is the point. Plug-in hybrids pay 30%, because they also pay fuel tax on the gasoline they burn; a plug-in driven 40% on electricity pays about $126 in FY2036, a little under a clean car or a 40-mpg hybrid. The base is two odometer readings, which defines the amount owed and so can ride reconciliation; the location-data bar and remedies are in sec. 111. The charge starts Oct 1, 2030, a year after enactment, to give Treasury and the States time to build collection **\[A-9\]**.

```
SEC. 102. CLEAN VEHICLE ROAD USER CHARGE.

(a) IN GENERAL.—Chapter 36 of the Internal Revenue Code of 1986 is amended by
adding at the end the following:

  "Subchapter E—Road User Charges

  "SEC. 4491. CLEAN VEHICLE ROAD USER CHARGE.
  "(a) IMPOSITION.—There is hereby imposed on the use of any covered vehicle
  registered in any State a tax equal to the rate determined under
  subsection (b) multiplied by the miles traveled by the vehicle during the
  taxable period, as determined under section 4492.
  "(b) RATE.—The rate for a taxable period ending in a fiscal year is—
    "(1) for a covered vehicle with a gross vehicle weight rating of 26,000
    pounds or less, the road-use rate for gasoline under section 4081(a)(2)(E)(v)
    on October 1 of that fiscal year, divided by 40, per mile;
    "(2) for such a vehicle that is a plug-in hybrid, 30 percent of the rate
    under paragraph (1); and
    "(3) for any other covered vehicle, the road-use rate for diesel fuel under
    section 4081(a)(2)(E)(v) on October 1 of that fiscal year, divided by
    6.5, per mile.
  "(c) COVERED VEHICLE.—The term 'covered vehicle' means a highway motor
  vehicle propelled in whole or in part by an electric motor drawing current
  from a battery recharged from an external source or from a fuel cell.
  "(d) LIABILITY; EXEMPTIONS.—The tax is payable by the person in whose name
  the vehicle is registered at the end of the taxable period. No tax shall be
  imposed on a vehicle owned by the United States, a State or political
  subdivision, or an Indian tribal government, or used to provide public
  transportation.
  "(e) PERIOD.—No tax shall be imposed on miles traveled before October 1,
  2030.

  "SEC. 4492. MILES TRAVELED.
  "(a) ODOMETER ONLY.—Miles traveled during a taxable period are the
  difference between two readings of the vehicle's odometer, taken at
  registration, registration renewal, or inspection, or submitted by the
  registered owner and verified as the Secretary prescribes. The taxable
  period is the period between successive readings, but not more than 15
  months.

  "SEC. 4493. COLLECTION.
  "(a) IN GENERAL.—The tax is payable annually.
  "(b) STATE AGREEMENTS.—The Secretary shall enter into an agreement with any
  State that requests it, under which the State collects the tax at
  registration or renewal and remits not less than 99 percent of
  collections within 60 days.
  "(c) COST ALLOWANCE.—Not more than 10 percent of amounts collected under
  this subchapter in a fiscal year may be used for costs of collection,
  including payments to States, and amounts so used are not credited to the
  Fund.".

(b) CREDIT TO FUND.—Section 9503(b)(1) of such Code is amended by adding at the
end "(F) section 4491 (relating to clean vehicle road user charge).".

(c) IMPLEMENTATION.—There is appropriated to the Secretary of the Treasury, out
of any money in the Treasury not otherwise appropriated, $750,000,000, to
remain available until September 30, 2033, for systems to administer
subchapter E of chapter 36 of such Code, including agreements with States;
and to the Secretary of Transportation $25,000,000 for a highway cost
allocation study, by vehicle class, weight, and axle configuration, to be
transmitted to the Committee on Ways and Means and the Committee on Finance
not later than March 31, 2030.
```

### Sec. 103. Fuel taxes, the Fix-It-First steps, and the EV-fee bridge

Fuel taxes are made permanent and indexed from Oct 1, 2029, and rise 3¢ a year for ten years in 2029 dollars **\[A-10\]**. A step is deferred in any year gasoline is expensive or spiking, and taken the first year it isn't, so a pause delays revenue rather than losing it. Gasoline reaches about 48¢ in 2029 dollars when the steps finish, about where the 1993 rate stands in today's money. Then, from FY2040, five steps of 2¢ add a fossil transition premium. The road-use rate stays where repair needs it, clean vehicles pay only that, and fossil fuel pays more. The step revenue needs no earmark: sec. 101(f)'s renewal-first rule spends dedicated money on repair before anything else.

Permanent credits and expenditure authority mean continuation under sec. 107 can never be stranded by a lapse, and they end the recurring expiration fight. The expiring base is used once, to pass this **\[A-9\]**. The 250-Plus EV fee runs one more year, into the fund, and ends when sec. 102 begins.

```
SEC. 103. FUEL TAXES; FIX-IT-FIRST ADJUSTMENT; ELECTRIC VEHICLE FEE.

(a) PERMANENCE.—Section 4081(d) of the Internal Revenue Code of 1986 is
amended by striking paragraph (1).

(b) ADJUSTMENT.—Section 4081(a)(2) of such Code is amended by adding at the
end the following:
  "(E) ADJUSTMENT AFTER FISCAL YEAR 2029.—
    "(i) IN GENERAL.—For any removal, entry, or sale in a fiscal year beginning
    after September 30, 2029, each rate in clauses (i) and (iii) of
    subparagraph (A) shall be the rate in that clause, plus the Fix-It-First
    amount and the fossil transition amount for the fiscal year, multiplied by 1 plus the cost-of-living
    adjustment for the fiscal year, rounded to the nearest 0.1 cent, but
    not less than the rate for the preceding fiscal year.
    "(ii) FIX-IT-FIRST AMOUNT.—The Fix-It-First amount for a fiscal year is
    3 cents multiplied by the number of steps taken as of the first day of
    the fiscal year, not exceeding 10. One step is taken on October 1, 2029,
    and one on October 1 of each fiscal year thereafter until 10 steps have
    been taken, except as provided in clause (iii).
    "(iii) PRICE PAUSE.—No step under clause (ii) or (iv) shall be taken on October 1 of any
    year if,
    for the 12-month period ending on the preceding June 30, the average
    retail price of regular gasoline in the United States, as published by
    the Energy Information Administration—
      "(I) exceeded $4.00 per gallon, multiplied by 1 plus the cost-of-living
      adjustment for the fiscal year beginning on that October 1; or
      "(II) exceeded such average for the preceding 12-month period by more
      than 20 percent.
    A step not taken by reason of this clause shall be taken on the first
    October 1 on which neither subclause applies, and not more than one
    step shall be taken on any October 1.
    "(iv) FOSSIL TRANSITION AMOUNT.—The fossil transition amount for a
    fiscal year is 2 cents multiplied by the number of transition steps
    taken as of the first day of the fiscal year, not exceeding 5. A
    transition step is taken on each October 1 that is not earlier than
    October 1, 2039, and after all steps under clause (ii) have been taken,
    until 5 transition steps have been taken, except as provided in clause
    (iii).
    "(v) ROAD-USE RATE.—The road-use rate for gasoline, and for diesel
    fuel, for a fiscal year is the rate for that fuel determined under
    clause (i) without regard to the fossil transition amount.
    "(vi) COST-OF-LIVING ADJUSTMENT.—The cost-of-living adjustment for a
    fiscal year is the percentage, if any, by which the Consumer Price Index
    for All Urban Consumers for the 12-month period ending on the June 30
    preceding the fiscal year exceeds that index for the 12-month period
    ending on June 30, 2028.".

(c) OTHER FUELS.—Rates of tax under section 4041 determined by reference to
section 4081(a)(2)(A) shall be determined by reference to that section as
adjusted under subparagraph (E).

(d) PERMANENT CREDITS AND EXPENDITURE AUTHORITY.—Section 9503 of such Code is
amended—
  (1) in subsection (b)(1), by striking "before October 1, 2028";
  (2) in subsection (b)(2), by striking "after September 30, 2028, and before
  July 1, 2029, and which are attributable to liability for tax incurred
  before October 1, 2028" and inserting "after September 30, 2028"; and
  (3) in subsections (c)(1) and (e)(3), by striking the date before which
  expenditures may be made, so that expenditure authority does not lapse,
  and by inserting a reference to divisions A through D of the Moving
  America Act of 2031.

(e) ELECTRIC VEHICLE FEE.—Section 1129 of the [BUILD America 250-Plus Act] is
amended—
  (1) by requiring that amounts remitted by States for registration periods
  beginning after September 30, 2029, be deposited in the Surface
  Transportation Trust Fund; and
  (2) by providing that no fee shall be imposed for any registration period
  beginning after September 30, 2030, on a vehicle subject to tax under
  section 4491 of the Internal Revenue Code of 1986.

(f) EFFECTIVE DATE.—Subsections (a) through (c) apply to removals, entries, and
sales after September 30, 2029.
```

Subsection (d)'s dates assume the 2028 extension carries credits only to Sept 30, 2029; if it runs longer, the struck text changes but the effect does not.

### Sec. 104. Truck and rail taxes

The weight-distance charge prices what fuel cannot: pavement wear rises roughly with the fourth power of axle load, while fuel use barely rises with weight **\[A-12\]**. It replaces the heavy-vehicle use tax, flat and capped at $550 since 1982, so trucks carry one more charge, not two. Mileage comes from the IFTA distance records carriers already file quarterly, and declared weight from the return.

The rates are calibrated to a 3¢ average across Class 7-8 miles, about $6.4B in FY2031. The 2030 act sets the final schedule from the cost-allocation study ordered by sec. 102(c). Clean trucks pay this charge and the sec. 4491(b)(3) rate, because damage comes from weight, not fuel; the 4% excise on zero-emission trucks carries the purchase incentive instead.

The 12% retail truck excise and the tire tax would otherwise end Sept 30, 2028 (26 U.S.C. 4051(c), 4071(d)). The rail diesel tax uses 4041(a)(1)(C)(ii), the train rate that has been zero since 2007, and 9503(b)(4)(C) must be amended or the receipts land in the general fund. The Code has no railroad-class concept, so the rates key to the Surface Transportation Board's classification **\[A-13\]**.

```
SEC. 104. TRUCK AND RAIL TAXES.

(a) WEIGHT-DISTANCE CHARGE.—Subchapter E of chapter 36 of the Internal Revenue
Code of 1986 is amended by adding at the end the following:

  "SEC. 4495. WEIGHT-DISTANCE CHARGE.
  "(a) IMPOSITION.—There is hereby imposed on the use of any highway motor
  vehicle with a declared combined gross weight of more than 26,000 pounds a
  tax equal to the rate determined under subsection (b) multiplied by the
  miles the vehicle travels on public highways in the United States during
  the taxable period.
  "(b) RATES.—
    "(1) IN GENERAL.—The rate per mile for fiscal year 2031 is—
      "(A) 0.8 cent, for a declared weight of not more than 33,000 pounds;
      "(B) 1.6 cents, for more than 33,000 but not more than 55,000 pounds;
      "(C) 2.6 cents, for more than 55,000 but not more than 70,000 pounds;
      "(D) 3.4 cents, for more than 70,000 but not more than 80,000 pounds;
      and
      "(E) 3.4 cents plus 0.4 cent for each 2,000 pounds or fraction thereof
      by which the declared weight exceeds 80,000 pounds.
    "(2) AXLES.—For a vehicle with a declared weight over 55,000 pounds
    operating on fewer than 5 axles, the rate is 125 percent of the rate
    under paragraph (1).
    "(3) INDEXING.—For any later fiscal year, each rate is multiplied by 1
    plus the cost-of-living adjustment under section 4081(a)(2)(E)(vi) for
    that fiscal year, divided by 1 plus that adjustment for fiscal year 2031.
  "(c) MILES AND WEIGHT.—Miles are determined from the distance records the
  operator maintains under the International Fuel Tax Agreement or, for a
  vehicle not subject to that agreement, from odometer readings. Declared
  weight is the weight declared on the return under subsection (e).
  "(d) CLEAN VEHICLES.—The tax applies in addition to the tax under section
  4491(b)(3).
  "(e) RETURNS.—The tax is reported and paid quarterly, as the Secretary
  prescribes. The Secretary may enter into agreements under which States
  that administer the International Fuel Tax Agreement collect and remit it.
  "(f) PERIOD.—No tax shall be imposed on miles traveled before October 1,
  2030.".

(b) USE TAX.—Section 4481(f) of such Code is amended by striking "October 1,
2029" and inserting "October 1, 2030", and section 4481 shall not apply to
use after September 30, 2030.

(c) RETAIL TRUCK AND TIRE EXCISES.—Sections 4051(c) and 4071(d) of such Code
are repealed, and section 4051(a) is amended by adding at the end:
  "(6) ZERO-EMISSION VEHICLES.—In the case of a chassis, body, or tractor sold
  after September 30, 2029, for use in a vehicle propelled solely by an
  electric motor drawing current from a battery or fuel cell, paragraph (1)
  shall be applied by substituting '4 percent' for '12 percent'.".

(d) AVIATION SEGMENT SURCHARGE.—Subchapter C of chapter 33 of such Code is
amended by inserting after section 4282 the following:
  "SEC. 4283. INTERCITY PASSENGER RAIL SEGMENT SURCHARGE.
  "(a) IN GENERAL.—There is hereby imposed, in addition to the tax under
  section 4261(b), a tax on each domestic segment of taxable transportation
  (as defined in section 4262) beginning after September 30, 2031, of—
    "(1) $4 for a segment beginning in fiscal year 2032;
    "(2) for a segment beginning in fiscal year 2033, 2034, 2035, or 2036,
    the amount for the preceding fiscal year plus $2; and
    "(3) for a segment beginning in a later fiscal year, the amount for the
    preceding fiscal year plus $0.40, but not more than $16.
  "(b) COLLECTION.—The tax is paid and collected in the same manner as the
  tax under section 4261(b).".

(e) RAIL DIESEL FUEL.—Section 4041(a)(1)(C)(ii) of such Code is amended by
striking subclause (III) and inserting:
    "(III) 0 after December 31, 2006, and before October 1, 2030,
    "(IV) after September 30, 2030, and before October 1, 2031, 10 cents per
    gallon for a Class I railroad and 5 cents per gallon for a Class II
    railroad, and
    "(V) after September 30, 2031, 15 cents per gallon for a Class I railroad
    and 7.5 cents per gallon for a Class II railroad.
  For purposes of subclauses (IV) and (V), the class of a railroad is that
  assigned by the Surface Transportation Board, and the rate is zero for
  fuel used by a Class III railroad or in a train providing intercity
  passenger or commuter rail passenger transportation.

(f) TRUST FUND.—Section 9503 of such Code is amended—
  (1) in subsection (b)(1), by adding at the end "(G) section 4495 (relating
  to weight-distance charge)."; and
  (2) in subsection (b)(4)(C), by inserting "(other than to the extent
  attributable to the rates in section 4041(a)(1)(C)(ii)(IV) and (V))" after
  "fuel used in a train".
```

Two Code checks remain: that 9502(b) does not send the new 4283 tax to the Airport and Airway Trust Fund, and a conforming rule so train fuel removed at a terminal (taxed under 4081, refunded under 6427(l)) bears the class rate.

### Sec. 105. Mandatory appropriations for expansion

One appropriation for all expansion, so ATRA's sec. 401(a) and ARCA's sec. 105 do not appropriate the same money twice. Totals: CIG $27.50B, sec. 606 $3.00B **\[A-6\]**, sec. 303 $55.00B, sec. 310 $20.20B, sec. 311 $6.00B, sec. 312 $12.00B; **$123.70B**, checked in code.

```
SEC. 105. MANDATORY APPROPRIATIONS FOR EXPANSION.

(a) APPROPRIATIONS.—Out of any money in the Treasury not otherwise
appropriated, there are appropriated, to remain available until expended—
  (1) to carry out section 5309 of title 49, United States Code,
  $4,500,000,000 for fiscal year 2032, $5,000,000,000 for fiscal year 2033,
  $5,500,000,000 for fiscal year 2034, $6,000,000,000 for fiscal year 2035,
  and $6,500,000,000 for fiscal year 2036;
  (2) to carry out section 606 of division C, $600,000,000 for each of fiscal
  years 2032 through 2036;
  (3) to carry out section 303 of division D, $6,000,000,000 for fiscal year
  2032, $9,000,000,000 for fiscal year 2033, $11,000,000,000 for fiscal year
  2034, $13,500,000,000 for fiscal year 2035, and $15,500,000,000 for fiscal
  year 2036;
  (4) to carry out section 310 of division D, $2,500,000,000 for fiscal year
  2032, $3,700,000,000 for fiscal year 2033, $4,500,000,000 for fiscal year
  2034, $4,800,000,000 for fiscal year 2035, and $4,700,000,000 for fiscal
  year 2036;
  (5) to carry out section 311 of division D, $1,600,000,000 for fiscal year
  2032, $1,400,000,000 for fiscal year 2033, $1,100,000,000 for fiscal year
  2034, and $950,000,000 for each of fiscal years 2035 and 2036; and
  (6) to carry out section 312 of division D, $1,500,000,000 for fiscal year
  2032, $2,000,000,000 for fiscal year 2033, $2,500,000,000 for fiscal year
  2034, and $3,000,000,000 for each of fiscal years 2035 and 2036.

(b) FULL OBLIGATION.—A grant agreement financed with amounts appropriated by
subsection (a) is a contractual obligation of the United States to pay the
Government share stated in it, and the Secretary shall obligate that share in
full on the date the agreement is executed. Section 5338(d)(2) of title 49,
United States Code, as amended by section 401(b) of division C, applies to
paragraph (1).

(c) NOT FROM THE FUND.—Amounts appropriated by this section are not derived
from the Surface Transportation Trust Fund.
```

### Sec. 106. Contract authority, contingent commitments, readiness reserve

ARCA's sec. 106, extended to all three accounts. The readiness reserve is a contingent general-fund appropriation, not contract authority against an account that is already short, and 106(e) carries the combined per-corridor cap **\[A-21\]**.

```
SEC. 106. CONTRACT AUTHORITY; CONTINGENT COMMITMENTS; READINESS RESERVE.

(a) IN GENERAL.—Amounts made available from the Surface Transportation Trust
Fund by divisions B, C and D shall be available for obligation on the date of
enactment of this Act, or on October 1 of the fiscal year for which they are
made available if later, and shall remain available until expended. Such
amounts shall be treated as authority described in section 1341(a)(1) of
title 31, United States Code, and approval of a project financed with them is
a contractual obligation of the United States to pay the Federal share.

(b) OBLIGATION LIMITATION.—Obligations of amounts made available from an
account in any fiscal year may not exceed the limitation set forth for that
account for that fiscal year in an appropriations Act. A limitation set below
90 percent of the amount made available for an account for that fiscal year
shall be applied first to reduce obligations for the expansion programs of
that account, and to its renewal programs only after obligations for those
expansion programs have been reduced to zero.

(c) CONTINGENT COMMITMENTS.—
  (1) The Secretary may enter into an agreement committing amounts to be made
  available in a fiscal year not later than fiscal year 2046.
  (2) The aggregate of commitments under paragraph (1) against the amounts of
  any single fiscal year for any program may not exceed 60 percent of the
  amount made available for that program for that fiscal year.
  (3) An agreement under this subsection shall state the amount committed by
  fiscal year, the conditions on which each installment depends, and the
  non-Federal commitments on which the Federal commitment is contingent.

(d) EFFECT OF LAPSE IN APPROPRIATIONS.—A lapse in, or failure to enact, an
appropriations Act does not reduce, rescind, or otherwise affect amounts made
available under divisions B, C and D or obligations incurred against them.

(e) READINESS RESERVE.—
  (1) Out of any money in the Treasury not otherwise appropriated, there is
  appropriated to carry out section 303 of division D not more than
  $25,000,000,000, which shall become available for obligation only upon a
  certification by the Secretary that a project has satisfied the entry
  requirements of that section, that its design is complete to not less than
  30 percent for each Tier 1 element, and that amounts otherwise available
  under that section for that fiscal year are fully obligated.
  (2) The total of amounts obligated for any one corridor under this
  subsection and section 303 of division D may not exceed $19,250,000,000.
  (3) Amounts under this subsection that have not become available for
  obligation on September 30, 2036, shall lapse.
  (4) Amounts under this subsection are an expansion program and are reduced
  under section 108 before any other program.
```

### Sec. 107. Continuation on lapse

ARCA's text, cross-referring to the single renewal definition in sec. 101(f) **\[A-19\]**. On lapse it carries $34.44B of rail renewal in FY2036.

```
SEC. 107. CONTINUATION ON LAPSE.

(a) IN GENERAL.—If authorizations under divisions B, C and D expire without
reauthorization, the Secretary shall continue to apportion and obligate, from
each account of the Surface Transportation Trust Fund, amounts for the
renewal programs of that account at the levels made available for fiscal
year 2036, adjusted for inflation.

(b) RENEWAL PROGRAMS.—In this section, the renewal programs of an account are
those described in section 101(f)(3).

(c) EXPANSION PROGRAMS EXCLUDED.—No amount is available under this section
for an expansion program described in section 101(f)(2).

(d) RULE OF CONSTRUCTION.—Amounts made available under this section
constitute direct spending, and their obligation does not require an annual
appropriation or an obligation limitation.
```

### Sec. 108. Reporting, recommendation and account solvency

The 0.206% benchmark is reported, not enforced **\[A-17\]**. Subsection (c) exists for one reason: a price pause delays steps, and an account can run short before receipts catch up. Three pauses would cost about $53.3B of FY2032-36 receipts; the backstop is capped at $25B, and CBO scores its expected cost. Cuts come only after it is exhausted, and never to sec. 105 money. The report counts sec. 1112 **\[A-18\]** and the reserve.

```
SEC. 108. GENERAL FUND REPORTING AND ACCOUNT SOLVENCY.

(a) REPORT.—The Secretary and the Director of the Congressional Budget
Office shall jointly report to the Committees each year, for the current and
each of the following 5 fiscal years, the amount by which obligations for the
programs of the three accounts, for programs under sections 105, 106(e) and
110(b), and appropriations for programs under section 1112 of division B, are
projected to exceed receipts credited to the Fund, as a percentage of gross
domestic product, stated both on that basis and net of the reduction in
income and payroll tax receipts estimated to result from taxes credited to
the Fund. The report shall state any step deferred under section
4081(a)(2)(E)(iii) of the Internal Revenue Code of 1986 and its effect.

(b) RECOMMENDATION.—If the percentage under subsection (a) is projected to
exceed 0.206 percent for a fiscal year, the Secretary shall, within 60 days,
transmit to the Committees a report identifying reductions or deferrals in
obligations for expansion programs, beginning with section 106(e), and
receipts, that would reduce the percentage to 0.206 percent.

(c) SOLVENCY BACKSTOP.—
  (1) TRANSFER.—If the Secretary of the Treasury projects that the unexpended
  balance of an account at the end of a fiscal year will be less than 25
  percent of the obligations from that account projected for the following
  fiscal year, there is appropriated to that account, out of money in the
  Treasury not otherwise appropriated, the amount necessary to restore the
  balance to 25 percent, not to exceed $25,000,000,000 in the aggregate for
  fiscal years 2032 through 2036.
  (2) REDUCTION.—Only after amounts under paragraph (1) are exhausted, any
  reduction in amounts available from an account, including under section
  9503(d) of such Code, shall be made first to its expansion programs, if
  any, and to its renewal programs only after those are reduced to zero.
  Amounts under sections 105 and 106(e) are not reduced by reason of a
  shortfall in an account.

(d) EXECUTED AGREEMENTS.—No reduction or deferral shall apply to an amount
obligated under a full funding grant agreement, a grant agreement under
section 105(b), or a contingent commitment executed before the date of the
report.
```

### Sec. 109. Joint facilities

ATRA's train-movement rule. Subsection (b) makes it govern sec. 310 projects **\[A-6\]**: sec. 310 pays the rail share, and the transit share comes from the Mass Transit Account and chapter 53. Subsection (c) allows ridership shares where movement counts are unavailable.

```
SEC. 109. JOINT FACILITIES.

(a) ATTRIBUTION.—Amounts in the Mass Transit Account and the Intercity
Passenger Rail Account, and amounts made available for section 310 of
division D, may be obligated for a facility used by both public
transportation and intercity passenger rail transportation, each in
proportion to—
  (1) for the rehabilitation or replacement of an existing facility, the
  share of train movements at the facility in the most recent fiscal year
  made by the services that source supports; and
  (2) for an expansion of the capacity of a facility, the share of the
  additional train movements the project is projected to make possible that
  will be made by those services,
as determined by the Secretary using the method of section 5309(q)(4) of
title 49, United States Code.

(b) TERMINALS OF NATIONAL SIGNIFICANCE.—For a project under section 310 of
division D, amounts made available for that section shall pay only the share
attributed to intercity passenger rail under subsection (a). The share
attributed to public transportation is eligible under sections 5307, 5309(q)
and 5337 of title 49, United States Code, and under section 1107 of
division B.

(c) DATA.—Where train movements for the most recent fiscal year are not
reported, the Secretary may use scheduled movements or, for an existing
facility, the shares of weekday boardings, and shall publish the basis of
each determination.
```

### Sec. 110. Contract authority within receipts; renewal top-ups

Each account's contract authority is capped at its own receipts plus its balance, so the fund is solvent by construction **\[A-14\]**. Any balance the Mass Transit Account carries into FY2032 counts automatically. The renewal shortfall is met by the reconciliation top-ups shown under "The vehicles": $209.74B in the 2029 act and $57.33B in the 2030 act. Subsection (b) points them at division B-D programs; highway top-ups restore each program's reduction in proportion and stay limited to repair. Subsection (c) is the fallback if reconciliation never delivers. It is the old general-fund transfer, kept as insurance, and costs nothing if the top-ups are enacted.

```
SEC. 110. CONTRACT AUTHORITY WITHIN RECEIPTS; RENEWAL TOP-UPS.

(a) CONTRACT AUTHORITY WITHIN RECEIPTS.—The amounts made available from an
account of the Fund by divisions B, C and D for a fiscal year shall not
exceed the receipts the Secretary of the Treasury projects will be credited
to that account for that fiscal year, plus its unobligated balance at the
beginning of that fiscal year. The Secretary shall reduce such amounts
proportionately within each division to the extent necessary.

(b) TOP-UPS.—Amounts appropriated for fiscal years 2032 through 2036 by
section [__] of [the 2029 reconciliation Act] and section [__] of [the 2030
reconciliation Act]—
  (1) for Federal-aid highway programs under title 23, United States Code,
  shall be distributed among the programs of division B in proportion to
  the reductions made under subsection (a) for that fiscal year, and may be
  obligated only for the preservation, rehabilitation, reconstruction, or
  replacement of existing highways, bridges, and tunnels; and
  (2) to carry out a program under chapter 53 of title 49, United States
  Code, or for a grant to the National Railroad Passenger Corporation or
  under section 22907, 22909, or 24911 of such title, shall be available for
  the corresponding program under division C or D,
in addition to amounts made available from the Fund, and subject to the
requirements of those divisions and to the deadlines in those Acts.

(c) FALLBACK.—For any fiscal year for which no amount has been appropriated as
described in subsection (b) for an account's renewal programs as of October
1 of that fiscal year, there is appropriated to that account, out of money in
the Treasury not otherwise appropriated, the amount set forth for that
account and fiscal year in the table in the report accompanying this Act,
and subsection (a) shall be applied by adding that amount to receipts.
```

### Sec. 111. Privacy and administration

The charge's political risk is surveillance, not price. Reconciliation can define the base as two odometer readings, because that sets the amount owed. A bar on collecting other data, retention limits and a private right of action have no budgetary effect, so they ride here **\[A-11\]**. Readings are return information under 26 U.S.C. 6103 from the first day of the charge, so the gap before this bill is narrow; a standalone privacy bill before Oct 1, 2030 would close it. Protection covers truck distance records under 4495 as well.

```
SEC. 111. ROAD USER CHARGE PRIVACY AND ADMINISTRATION.

(a) NO OTHER INFORMATION.—Section 4492 of the Internal Revenue Code of 1986
is amended by adding at the end:
  "(b) NO OTHER INFORMATION.—No information about the location, route, time,
  or manner of a vehicle's travel may be collected, required, received, or
  retained for purposes of this subchapter, whether offered by the taxpayer
  or any other person, except the per-jurisdiction distance records
  described in section 4495(c), and no device may be required to be
  installed in any vehicle.".

(b) PRIVACY.—Subchapter E of chapter 36 of such Code is amended by inserting
after section 4493 the following:
  "SEC. 4494. PRIVACY.
  "(a) RETURN INFORMATION.—Odometer readings, distance records, and any other
  information obtained under this subchapter are return information for
  purposes of section 6103, may not be disclosed for any purpose other than
  administration of this title, and may not be sold.
  "(b) RETENTION.—Readings and records shall be destroyed not later than 3
  years after the end of the taxable period to which they relate, unless
  needed for a pending examination or proceeding.
  "(c) REMEDIES.—Section 7431 applies to any collection, retention, or
  disclosure in violation of section 4492(b) or this section, by an officer
  or employee of the United States or of a State, or a contractor of either.
  "(d) REVIEW.—The Comptroller General shall report to the Committee on Ways
  and Means and the Committee on Finance on collection costs, evasion, and
  compliance with this section not later than September 30, 2033, and every
  3 years thereafter.".
```

Odometer-only has known costs, accepted deliberately: miles driven abroad or on private land are taxed; fraud enforcement rests on audit and 49 U.S.C. 32703, not telemetry; and the 10% cost allowance is a ceiling, reviewed by GAO. Sec. 4494(a) bars non-tax disclosure outright, stricter than 6103(i)(1)'s court-order route; that is the warrant line the privacy pitch needs.

## Division B — Federal-Aid Highways and Highway Safety

Division B authorizes **$461.12B** over FY2032-36: $418.28B of FHWA programs continuing H.R. 8870's title I at 2.5% a year, **$30.77B for a new Interstate and Bridge Renewal program**, and $12.07B for NHTSA and FMCSA. Another $17.24B of general-fund grants is authorized subject to appropriation. All of it is renewal except sec. 1112 **\[A-2\]**.

The design keeps what H.R. 8870 does well: about 90% formula money, a larger STBG share, bridges moved onto contract authority, faster environmental review. It fixes what H.R. 8870 and the IIJA both left undone. Nothing funds the Interstate rebuild, repair has no teeth, safety money shrinks with no consequence for rising deaths, and resilience and clean fuels lost their formula money.

### What the baseline leaves undone

| Problem | Evidence | Response |
| --- | --- | --- |
| No program rebuilds the Interstate | TRB Special Report 329: $45-70B a year needed over 20 years, against $20-25B spent. Neither the IIJA nor H.R. 8870 dedicates money to it | Sec. 1104, Interstate and Bridge Renewal, with tolling of rebuilt segments allowed **\[A-23\]** |
| Large bridges depend on appropriators | H.R. 8870 leaves the competitive bridge program at $2B a year subject to appropriation; the 2025 inventory counts 41,677 poor bridges (6.7%) | The bridge program becomes contract authority inside sec. 1104, with a large-project tier |
| Repair has no teeth | Poor federal-aid pavement fell only from 19% (2018) to about 16.5% (2024); 112,957 lane-miles added in 2018-24 cost about $5.3B a year to maintain; H.R. 8870 loosened asset-plan review to every two years | Sec. 1106: a preservation requirement for States missing targets, a lifecycle test, a lower federal share for new general-purpose lanes **\[A-24\]** |
| Safety money shrinks with no consequence | 36,640 deaths in 2025, down 6.7% but well above the early-2010s level; H.R. 8870 cuts SS4A's path and its planning share to 5%, and only reports regressive targets | Sec. 1109: Safe System conditions, a 15% planning share, consequences for regressive targets **\[A-25\]** |
| Locals lack direct access | Local governments own about 80% of roads and see over half of traffic deaths (NACTO) | Secs. 1109 and 1115: direct SS4A eligibility kept, STBG suballocation to 60% |
| Resilience and clean-fuel money cut | H.R. 8870 repeals the PROTECT formula ($7.3B under the IIJA), phases the CMAQ alternative-fuel set-aside from 10% to 7%, and repeals the Carbon Reduction Program and NEVI | Sec. 1110: a 4% NHPP resilience set-aside, carbon reduction restored inside formula money, the CMAQ set-aside held at 10%. Sec. 1116: a charging program that pays only for working chargers **\[A-26\]** |
| Truck parking and truck weight | One parking space for every 11 truck drivers (ATRI); the 91,000-lb pilot passed T&I 35-29 over county, safety and trucking opposition | Secs. 1113 and 1114: 15% of freight formula money to parking; the pilot ends; the weight-distance charge prices weight **\[A-26\]** |
| Grants stall between award and agreement | GAO: 23% of surveyed IIJA awardees had no signed agreement; 31 of 32 FY2019 projects changed before signing | Division E sec. 104: a 180-day agreement clock and protection of executed agreements |
| Buying power | Highway construction costs rose 63% from FY2021 to FY2025; BTS puts the IIJA's lost buying power at 34% | 2.5% annual growth plus the renewal top-ups; not fully restored |

### Sections

| Sec. | Provision | FY2032-36 | Status |
| --- | --- | --- | --- |
| 1101 | H.R. 8870 title I continued at 2.5% a year; obligation limitation | $418.28B FHWA | Drafted |
| 1102 | Apportioned formula programs at H.R. 8870 shares (NHPP, STBG at 31%, HSIP, CMAQ, freight, planning) | about $325.5B, within 1101, after the sec. 1116 set-aside | Specified |
| 1103 | Bridge formula program on contract authority, $75M State floor, 20% off-system | about $49.6B, within 1101 | Specified |
| 1104 | Interstate and Bridge Renewal | $30.77B | Drafted |
| 1105 | Renewal classification | — | Drafted |
| 1106 | Fix-it-first | policy | Drafted |
| 1107 | Multimodal flexibility | policy | Specified |
| 1108 | Road user charge coordination with the States | policy | Specified |
| 1109 | Safe System | within 1101 | Drafted |
| 1110 | Resilience, carbon reduction and clean fuels | within 1102 | Drafted |
| 1111 | Delivery and unit-cost reporting | policy | Specified |
| 1112 | General-fund grants: multimodal freight and National Infrastructure Grants | $17.24B, subject to appropriation | Drafted |
| 1113 | Truck parking | within 1102 | Drafted |
| 1114 | Truck size and weight | policy | Drafted |
| 1115 | Local access and suballocation | policy | Specified |
| 1116 | Charging Gap Program, replacing NEVI | $2.63B, within 1101 | Drafted |
| 1201, 1301 | NHTSA and FMCSA at H.R. 8870 levels, grown | $12.07B | Specified |

The rest of title I, about $40.6B (STAG, SS4A, PROTECT grants, federal lands and tribal, emergency relief, TIFIA, administration), continues under sec. 1101.

### Sec. 1101. Authorizations

The limitation is the FHWA total less the exempt amount, plus sec. 1104.

```
SEC. 1101. HIGHWAY AUTHORIZATIONS.

(a) CONTINUATION.—Except as otherwise provided in this division, title I of
the [BUILD America 250-Plus Act], and the amendments made by that title,
shall apply for each of fiscal years 2032 through 2036, and each amount
authorized by that title for fiscal year 2031 to be appropriated out of the
Highway Account shall be authorized for each such fiscal year in an amount
equal to the fiscal year 2031 amount increased by 2.5 percent for each fiscal
year after fiscal year 2031.

(b) OBLIGATION LIMITATION.—The total of all obligations from amounts made
available from the Highway Account by this division for Federal-aid highway
and highway safety construction programs, including section 1104, shall not
exceed—
  (1) $80,971,000,000 for fiscal year 2032;
  (2) $84,995,000,000 for fiscal year 2033;
  (3) $89,070,000,000 for fiscal year 2034;
  (4) $93,197,000,000 for fiscal year 2035; and
  (5) $97,377,000,000 for fiscal year 2036.

(c) EXEMPT AMOUNTS.—Amounts exempt from the limitation under section 1102 of
the [BUILD America 250-Plus Act] for fiscal year 2031 shall be exempt in the
same amounts, increased by 2.5 percent for each fiscal year after fiscal year
2031.
```

### Sec. 1104. Interstate and Bridge Renewal

The Interstate is 70 years old and has no program of its own. Sec. 1104 creates one **\[A-23\]**. It starts from H.R. 8870's competitive bridge program, $2B a year subject to appropriation, and turns it into contract authority. New money is added at $0 / 2 / 4 / 6 / 8B, back-loaded because FY2032 has no room under the benchmark, and continues at the FY2036 level plus 2.5% a year.

| $B | FY2032 | FY2033 | FY2034 | FY2035 | FY2036 | Total |
| --- | --- | --- | --- | --- | --- | --- |
| Bridge program, converted | 2.05 | 2.10 | 2.15 | 2.21 | 2.26 | 10.77 |
| New money | 0.00 | 2.00 | 4.00 | 6.00 | 8.00 | 20.00 |
| **Sec. 1104** | **2.05** | **4.10** | **6.15** | **8.21** | **10.26** | **30.77** |

Eighty percent goes out by formula on Interstate lane-miles, Interstate travel and the deck area of NHS bridges in poor or fair condition. Twenty percent funds projects over $500M on multiyear agreements, because no State's formula share can carry a $3B river crossing. The program buys reconstruction, not general-purpose lanes. A State may toll a rebuilt segment, as TRB recommended, with revenue kept in the corridor.

```
SEC. 1104. INTERSTATE AND BRIDGE RENEWAL PROGRAM.

(a) IN GENERAL.—Chapter 1 of title 23, United States Code, is amended by
adding at the end the following:

"§ [178]. Interstate and bridge renewal program

  "(a) PURPOSE.—The purpose of this section is to reconstruct the Interstate
  System, and the bridges of the National Highway System, as they reach the
  end of their service lives.
  "(b) APPORTIONMENT.—Of the amount made available for a fiscal year, less
  the set-aside under subsection (e), the Secretary shall apportion to each
  State with Interstate System mileage—
    "(1) 50 percent in the ratio that Interstate lane-miles in the State bear
    to such lane-miles in all States;
    "(2) 25 percent in the ratio that vehicle-miles traveled on the
    Interstate System in the State bear to such miles in all States; and
    "(3) 25 percent in the ratio that the deck area of bridges on the
    National Highway System classified as in poor or fair condition in the
    State bears to such area in all States,
  except that each such State shall receive not less than 0.5 percent.
  "(c) ELIGIBLE PROJECTS.—Amounts under this section may be obligated only
  for—
    "(1) reconstruction, rehabilitation, or replacement of Interstate System
    pavements, bridges, tunnels, and interchanges that have reached, or will
    within 10 years reach, the end of their design service lives;
    "(2) replacement or rehabilitation of a bridge on the National Highway
    System classified as in poor or fair condition;
    "(3) resilience and safety improvements carried out as part of a project
    under paragraph (1) or (2); and
    "(4) tolling equipment for a facility tolled under subsection (h).
  "(d) CAPACITY.—No amount under this section may be obligated for the
  portion of a project that adds a general-purpose through lane. A lane added
  as part of a project under subsection (c) is eligible only if it is an
  auxiliary lane between adjacent interchanges or a lane on which the State
  charges a toll that varies with demand.
  "(e) LARGE PROJECTS.—The Secretary shall set aside 20 percent of the amount
  made available for each fiscal year for competitive grants for projects
  under subsection (c) with a total cost of not less than $500,000,000. A
  grant may be made by a multiyear agreement under section 106(c) of division
  A of the Moving America Act of 2031, and may not exceed 50 percent of the
  project cost. A project selected under the bridge investment program before
  October 1, 2031, is eligible under this subsection.
  "(f) RENEWAL PLAN.—A State may obligate amounts apportioned under
  subsection (b) only after it includes in its asset management plan under
  section 119(e) an Interstate renewal plan that identifies, for each
  segment, the expected year of reconstruction and its estimated cost over
  20 years.
  "(g) FEDERAL SHARE.—The Federal share of a project under this section is
  90 percent.
  "(h) TOLLING.—Notwithstanding section 301, a State may impose a toll on a
  segment of the Interstate System reconstructed with amounts under this
  section, if—
    "(1) the toll takes effect only after the reconstruction contract for
    the segment is awarded;
    "(2) toll revenues are used only for the facility, other highways in the
    corridor, and public transportation serving the corridor;
    "(3) the State provides a discount or credit for low-income residents
    and frequent local users; and
    "(4) the State has held a public hearing on the toll and its rates.
  "(i) AUTHORIZATION.—There shall be available from the Highway Account of
  the Surface Transportation Trust Fund to carry out this section
  $2,050,000,000 for fiscal year 2032, $4,101,000,000 for fiscal year 2033,
  $6,154,000,000 for fiscal year 2034, $8,208,000,000 for fiscal year 2035,
  and $10,263,000,000 for fiscal year 2036.".

(b) BRIDGE INVESTMENT PROGRAM.—No amount is authorized to be appropriated out
of the general fund for the competitive bridge program under title I of the
[BUILD America 250-Plus Act] for any fiscal year after fiscal year 2031.
```

The section number is a placeholder until 250-Plus's additions to chapter 1 are known. The apportionment needs a data run on lane-miles, Interstate travel and NBI deck area before any State table is published.

### Sec. 1105. Renewal classification

```
SEC. 1105. RENEWAL PROGRAMS OF THE HIGHWAY ACCOUNT.

For purposes of sections 101(f), 107 and 108 of division A, every program
for which amounts are made available from the Highway Account by this
division or by title 23, United States Code, including section 1104, is a
renewal program.
```

### Sec. 1106. Fix-it-first

Three tools, none of which costs federal money **\[A-24\]**. A State that keeps missing its own pavement and bridge targets must put a rising share of NHPP into repair, and may not lower its targets below its actual condition. A State adding general-purpose lanes on a project over $100M must show it can maintain them for 20 years and publish how its last forecasts turned out. And the federal share for the added-lane portion drops 10 points, so expansion costs a State more of its own money than repair does. The INVEST Act-style amendment failed by voice vote at the H.R. 8870 markup; this version is narrower, aimed at outcomes rather than project lists.

```
SEC. 1106. FIX-IT-FIRST.

(a) PRESERVATION REQUIREMENT.—Section 119 of title 23, United States Code, is
amended by adding at the end the following:
  "(k) FIX-IT-FIRST.—
    "(1) If, in two consecutive biennial determinations under section
    150(e), the condition of pavements or bridges on the National Highway
    System in a State has neither met nor made significant progress toward
    the targets the State set under section 150(d), the State shall obligate,
    in the following fiscal year, not less than 50 percent of the amount
    apportioned to it under this section for the preservation,
    rehabilitation, reconstruction, or replacement of National Highway
    System pavements and bridges in poor or fair condition.
    "(2) The percentage under paragraph (1) increases by 10 percentage
    points for each further consecutive determination, to not more than 80
    percent, and ceases to apply after a determination that the targets are
    met.
    "(3) A State's targets for the condition of pavements and bridges may not
    be lower than the condition it reported in the preceding determination.".

(b) LIFECYCLE TEST.—Section 106 of such title is amended by adding at the end
the following:
  "(k) ADDED LANE-MILES.—The Secretary may not authorize Federal funds under
  this title for a project with an estimated total cost of $100,000,000 or
  more that adds general-purpose through lane-miles unless the State
  certifies, and its asset management plan shows, that—
    "(1) the State has identified funding to maintain the added lane-miles
    in good condition for 20 years; and
    "(2) the State has published the project's traffic forecast together
    with the forecasts and observed outcomes of its three most recent
    comparable projects.".

(c) FEDERAL SHARE.—Section 120 of such title is amended by adding at the end
the following:
  "(l) ADDED GENERAL-PURPOSE LANES.—The Federal share of the cost of the
  portion of a project that adds a general-purpose through lane shall be 10
  percentage points less than the share that would otherwise apply under
  this section.".

(d) REPORTING.—Each State shall report annually, in the database under
section 102 of division E, the share of its obligations under title 23 for
preservation and reconstruction, safety, added capacity, and other purposes.
```

### Sec. 1109. Safe System

SS4A stays on contract authority at H.R. 8870's levels, grown, with direct eligibility for cities, counties, MPOs and tribes **\[A-25\]**. The planning share is 15%, between H.R. 8870's 5% and the IIJA's 40%, because most small places still lack a plan. Where a State's targets regress, HSIP money is limited to proven countermeasures. The vulnerable-road-user rule scales with the State's actual share of deaths; pedestrians alone were 6,529 of 36,640 deaths in 2025.

```
SEC. 1109. SAFE SYSTEM.

(a) SAFE STREETS AND ROADS FOR ALL.—The program under section [1119] of the
[BUILD America 250-Plus Act] is amended—
  (1) by striking the percentage reserved for planning grants and inserting
  "15 percent"; and
  (2) by requiring, as a condition of an implementation grant, a
  comprehensive safety action plan that adopts a Safe System approach and a
  goal of eliminating roadway fatalities and serious injuries by a stated
  date.

(b) REGRESSIVE TARGETS.—Section 148(i) of title 23, United States Code, is
amended by adding at the end the following:
  "(4) REGRESSIVE TARGETS.—If a State's target under section 150(d) for the
  number or rate of fatalities or serious injuries for a year exceeds the
  State's average for the most recent 5-year period, or the State has
  neither met nor made significant progress toward those targets for 2
  consecutive years, the State may obligate amounts apportioned under this
  section for the following fiscal year only for projects using
  countermeasures the Secretary has designated as proven safety
  countermeasures.".

(c) SPEED MANAGEMENT.—Section 148(a)(4)(B) of such title is amended by adding
at the end: "speed management, including the setting of speed limits by a
Safe System method;".

(d) VULNERABLE ROAD USERS.—Section 148(l) of such title is amended so that a
State in which vulnerable road user fatalities are not less than 15 percent
of total fatalities shall obligate, for vulnerable road user safety, not
less than the percentage of its apportionment under this section that
equals that share.
```

### Sec. 1110. Resilience, carbon reduction and clean fuels

Three set-asides inside existing formula money, none of it new federal spending **\[A-26\]**. A 4% NHPP set-aside, about $1.4B a year, replaces most of the repealed PROTECT formula. The Carbon Reduction Program returns as 2% of each State's formula apportionment, about $1.24B a year against the IIJA's $1.34B in FY2026, with 65% suballocated by population as before. The CMAQ alternative-fuel set-aside stays at 10% instead of falling to 7%. NEVI's successor is sec. 1116.

```
SEC. 1110. RESILIENCE, CARBON REDUCTION, AND CLEAN FUELS.

(a) RESILIENCE.—Section 119 of title 23, United States Code, is amended by
adding at the end the following:
  "(l) RESILIENCE.—Of the amount apportioned to a State under this section
  for a fiscal year, not less than 4 percent shall be obligated for
  activities eligible under section 176. The Federal share of such an
  activity carried out under a resilience improvement plan of the State is
  90 percent.".

(b) CARBON REDUCTION.—Section 175 of such title, as in effect on September
30, 2026, is restored, except that—
  (1) the amount set aside for a State for a fiscal year shall be 2 percent
  of the total amount apportioned to the State under section 104(b) for
  that fiscal year, taken proportionally from the State's other
  apportionments; and
  (2) an electric vehicle charging project carried out with such amounts
  shall meet the standards under section [179](f).

(c) ALTERNATIVE FUELING.—The minimum percentage of the amount apportioned
under section 149 of such title that a State is required to obligate for
alternative fueling infrastructure shall be 10 percent for each of fiscal
years 2032 through 2036.
```

### Sec. 1112. General-fund grants

Only multimodal freight grants ($1.2B) and National Infrastructure Grants ($2.0B) stay on the general fund, grown 2.5%: **$17.24B** over FY2032-36, counted against the benchmark **\[A-18\]**. The bridge program has moved into sec. 1104.

```
SEC. 1112. GENERAL FUND GRANTS.

(a) AUTHORIZATIONS.—There are authorized to be appropriated out of the general
fund of the Treasury—
  (1) for grants under section 117 of title 23, United States Code,
  $1,230,000,000 for fiscal year 2032; and
  (2) for grants under section [7105] of the [BUILD America 250-Plus Act],
  $2,050,000,000 for fiscal year 2032,
and for each of fiscal years 2033 through 2036, each such amount for the
preceding fiscal year increased by 2.5 percent.

(b) NO OTHER AMOUNTS.—No other amount authorized to be appropriated out of
the general fund by title I or section [7105] of that Act for fiscal year
2031 is authorized for any later fiscal year.

(c) REPORTING.—Amounts appropriated under this section are counted under
section 108(a) of division A.
```

### Sec. 1113. Truck parking

Fifteen percent of each State's freight formula money goes to truck parking until the State shows its need is met, about $0.28B a year on top of H.R. 8870's $0.15B of competitive grants. That roughly triples federal parking money without a new program.

```
SEC. 1113. TRUCK PARKING.

Section 167 of title 23, United States Code, is amended by adding at the end
the following:
  "(n) TRUCK PARKING.—A State shall obligate not less than 15 percent of the
  amount apportioned to it under this section for a fiscal year for projects
  that add or improve commercial motor vehicle parking, unless the State
  certifies, on the basis of the most recent national truck parking survey
  under section 1401(c) of MAP-21, that its parking needs on the National
  Highway Freight Network are met.".
```

### Sec. 1114. Truck size and weight

The 91,000-lb pilot ends with 250-Plus and is not extended **\[A-26\]**. Counties, the Coalition Against Bigger Trucks (owner-operators, the Teamsters, railroads and safety groups) and Sen. Wicker opposed it. The question can return once the weight-distance charge makes heavier trucks pay their way: sec. 4495 already charges 0.4¢ a mile for each 2,000 lb over 80,000.

```
SEC. 1114. TRUCK SIZE AND WEIGHT.

(a) PILOT.—The pilot program under section [1302] of the [BUILD America
250-Plus Act] permitting the operation of vehicles weighing up to 91,000
pounds on the Interstate System shall terminate on September 30, 2031.

(b) REPORT.—Not later than September 30, 2033, the Secretary shall report to
the Committees, using data from that pilot, on the pavement, bridge, and
safety effects of vehicles over 80,000 pounds, and on the rate under section
4495(b)(1)(E) of the Internal Revenue Code of 1986 that would recover their
cost.
```

### Sec. 1116. Charging Gap Program

NEVI's money was real but slow. It gave $5B to 50 State plans, ran private charging sites through federal-aid highway procedures, set station spacing by rule rather than by need, and paid only by reimbursement. About $526M was obligated by early 2025. FHWA then suspended the program, and $503.8M was rescinded in January 2026. By mid-2026 about 4,000 ports at 990 sites were under contract, with roughly $4B unspent. Sec. 1116 replaces it with a program built to close gaps fast and pay only for chargers that work **\[A-27\]**.

| What slowed NEVI | What sec. 1116 does instead |
| --- | --- |
| 50 State plans, each approved before money moved | One national program run by DOT. A State may run the auction for its own gaps, on the same terms |
| Spacing rules (every 50 miles, within a mile of the corridor) required a full corridor build-out before anything else | A published gap map. Money goes only where the market has not built |
| Federal-aid highway procedures applied to private sites | Not a federal-aid highway project. A statutory categorical exclusion on private or disturbed land. Prevailing wages and Buy America still apply |
| Grants negotiated site by site and paid by reimbursement | Reverse auctions on a standard agreement, awarded within 60 days. Half paid within 30 days of energization, half over five years for meeting the uptime standard |
| Utility interconnection, usually the longest wait | Utility make-ready and on-site storage are eligible costs, and utilities may bid. A 24-month deadline to energize, with one 12-month extension for documented utility delay |
| Built for cars on Interstates | At least 40% for medium and heavy trucks at freight sites, ports and truck parking; at least 30% rural |

It is funded at $0.5B in FY2032, rising 2.5% a year ($2.63B over FY2032-36), set aside from formula money before apportionment. NEVI balances still unobligated on Oct 1, 2031 can be used by the State under these terms for one year, then go to the national auction. Whatever remains of the roughly $4B unspent in mid-2026 moves onto the faster track, so the first years can run well above the new money's level.

```
SEC. 1116. CHARGING GAP PROGRAM.

(a) IN GENERAL.—Chapter 1 of title 23, United States Code, is amended by
adding at the end the following:

"§ [179]. Charging gap program

  "(a) GAP MAP.—Not later than 180 days after the date of enactment of the
  Moving America Act of 2031, and annually thereafter, the Secretary, in
  consultation with the Secretary of Energy, shall publish a map
  identifying—
    "(1) segments of the National Highway System more than 50 miles of
    travel from a public charging site that meets subsection (f); and
    "(2) locations on the National Highway Freight Network, at ports, and at
    truck parking facilities where charging for medium- and heavy-duty
    vehicles is needed and not available.
  "(b) AWARDS BY AUCTION.—Not less than twice each fiscal year, the
  Secretary shall award amounts under this section by competitive auction
  for gaps on the map. Any person, including a private entity, a State,
  local, or tribal government, or an electric utility, may bid. A bid shall
  state the Federal amount requested to energize, by a stated date, a site
  in a gap that meets subsection (f). The Secretary shall select the bids
  that close the most gap at the lowest Federal cost and announce awards
  not later than 60 days after an auction closes.
  "(c) AGREEMENT AND PAYMENT.—
    "(1) An award shall be made by a standard agreement published before
    the auction, without further negotiation.
    "(2) The Secretary shall pay 50 percent of an award not later than 30
    days after the site is energized and reporting data under subsection
    (f)(4), and the remainder in equal annual installments over 5 years,
    each conditioned on the site meeting subsection (f)(5) for the
    preceding year.
    "(3) An award for a site not energized within 24 months after the award
    shall lapse, and the amount shall be offered at the next auction. The
    Secretary may extend the period once, by not more than 12 months, on a
    showing that the delay results from utility interconnection.
  "(d) LIMITS.—An award may not exceed 80 percent of the documented cost of
  the site, including utility make-ready and on-site energy storage. Of the
  amounts awarded each fiscal year, not less than 40 percent shall be for
  sites under subsection (a)(2), and not less than 30 percent for sites in
  rural areas.
  "(e) PROCEDURES.—
    "(1) A project under this section located on private property or on
    previously disturbed land is a categorical exclusion under the National
    Environmental Policy Act of 1969, and is not a project on a Federal-aid
    highway for purposes of this title, except sections 113 and 313.
    "(2) A State may elect, not later than 90 days before an auction, to
    conduct the auction for the gaps in that State, using the map, standard
    agreement, payment schedule, and limits of this section.
  "(f) STANDARDS.—A site funded under this section shall—
    "(1) provide not less than 4 ports of not less than 150 kilowatts each
    for light-duty vehicles or, at a site under subsection (a)(2), not less
    than 2 ports of not less than 1 megawatt each;
    "(2) accept payment by contactless card without a membership;
    "(3) use the connector standards the Secretary designates, including
    SAE J3400;
    "(4) report availability, price, and uptime in real time through an
    open data feed; and
    "(5) maintain uptime of not less than 97 percent.
  "(g) REPORTING.—The Secretary shall publish, for each auction and site,
  the Federal cost per port, the time from award to energization, and
  uptime.
  "(h) FUNDING.—Before apportioning amounts under section 104(b) for a
  fiscal year, the Secretary shall set aside to carry out this section
  $500,000,000 for fiscal year 2032, increased by 2.5 percent for each later
  fiscal year.".

(b) NEVI BALANCES.—Amounts made available for the National Electric Vehicle
Infrastructure Formula Program that are unobligated on October 1, 2031, may
be obligated by the State under section [179] of title 23, United States
Code, until September 30, 2032, and thereafter shall be available to the
Secretary for auctions under that section.
```

### Specified, not drafted

- **Sec. 1102, formula programs.** H.R. 8870's shares carry forward: NHPP, STBG at 31%, HSIP, CMAQ with its cost-effectiveness table, freight, and metropolitan planning at a 90% federal share. Transportation Alternatives money may be transferred out only if unobligated after three years.
- **Sec. 1103, bridges.** The bridge formula stays on contract authority with a $75M State floor, 20% off-system, a 3% tribal set-aside and the 25% local competition at a 95% federal share. Sources differ on $9.0B or $9.2B a year; the enacted text decides.
- **Sec. 1107, multimodal flexibility.** STBG and CMAQ flex to chapter 53 and intercity rail capital as of right, and STBG can pay a State's share of a joint facility under div. A sec. 109.
- **Sec. 1108, road user charge coordination.** A State may collect the sec. 4491 charge and its own road usage charge in one registration transaction under 26 U.S.C. 4493(b). The 250-Plus EV fee's 125% withholding penalty lapses with the fee. FHWA's per-mile pilot continues, testing truck distance reporting under 4495.
- **Sec. 1111, delivery reporting.** Unit costs for projects over $100M and the work-type shares under sec. 1106(d) go into the division E database.
- **Sec. 1115, local access.** STBG suballocation by population rises from 55% to 60%. One percent of the amount for areas under 50,000 funds rural transportation planning organizations where designated. H.R. 8870's consolidated funding pilot must suballocate 30%, not 25%. MPOs keep the option to be direct recipients.
- **Secs. 1201 and 1301, NHTSA and FMCSA.** H.R. 8870 levels grown 2.5%: $12.07B together, roughly $6.4B NHTSA and $5.7B FMCSA on H.R. 8870's five-year proportions. The sec. 402 and 405 merger with its speed priority, the automated-truck safety case and the lease-purchase rule carry forward.

### Kept from H.R. 8870 as enacted

STAG ($2.4B a year, grown), the PROTECT grant program ($0.5B), wildlife crossings, federal lands and tribal programs, emergency relief with resilience eligibility, the project delivery subtitle (categorical exclusion thresholds of $12M and $70M, a single lead agency, page and time limits), bridge inspection reviews and Buy America. Division B's top-line and these programs need checking against the enacted text, not the reported bill.

## Division C — Public Transportation (American Transit Renewal Act)

Division C authorizes **$221.42B** over FY2032-36: $190.92B of renewal from the Mass Transit Account and $30.50B of expansion from division A sec. 105. It does three things 250-Plus does not: a conditional operating tier for large systems **\[A-3\]**, a 20-year schedule that retires the $127.8B repair backlog, and CIG grants obligated in full at signing. ATRA's title I is now division A. Transit's renewal programs become self-sufficient in FY2036, when its top-up reaches zero.

| Title | Subject | FY2032-36 | Kind |
| --- | --- | --- | --- |
| II | Service operating assistance, new 5307(i) | $35.00B | Renewal |
| III | State of good repair: 5337 formula, 5337(g) backlog schedule, 5326(e) enforcement, resilience | $63.03B | Renewal |
| IV | Capital Investment Grants (5309), plus delivery reforms in secs. 402-407 | $27.50B | Expansion, div. A sec. 105(a)(1) |
| V | Labor and workforce | $2.85B | Renewal |
| VI | Formula capital, buses, rural, seniors and disabilities, accessibility, ferries, emergency relief, joint facilities | $88.30B | Renewal, except sec. 606 ($3.00B, expansion) **\[A-6\]** |
| VII | Planning, FTA capacity, safety, research, delivery; Buy America; authorizations | $4.74B | Renewal |
|  | **Total** | **$221.42B** | $40.30B / 42.29 / 44.29 / 46.24 / 48.30 by year |

### Title II: the operating tier, scenario B

The new 5307(i) runs $6.0B rising to $8.0B a year for urbanized areas of 200,000 or more. Funds are apportioned 50% on vehicle revenue hours, 30% on trips and 20% on low-income residents, and each area is capped at 25% of its net operating cost. Grants are conditioned on maintenance of effort, a 95% service floor, no outstanding 5326(e) direction, and a cap on preventive-maintenance shifting **\[A-3\]**. On 2024 NTD data the first-year tier is 11.9% of national net operating cost. New York's share (27.7%) equals its share of that cost; the ceiling binds in 69 small areas and costs New York nothing.

Sec. 201(a), the new 5307(i), stands as ATRA drafted it. Its base years stay FY2028-30 for service hours and FY2027-29 for preventive maintenance **\[A-20\]**. Sec. 201(b)'s amounts are replaced by sec. 717.

### Title III: the 5337(g) dates

Secs. 301-303 stand as ATRA drafted them, with four corrections:

- In new 5337(g)(1), "September 30, 2030" becomes "September 30, 2031" **\[A-20\]**.
- In 5337(g)(3), "beginning with fiscal year 2031" becomes "beginning with fiscal year 2032". The backlog is retired in FY2051.
- Sec. 301(1) is struck, because sec. 715(a) makes the same 5338(a)(2)(K) → (L) amendment.
- 5337(g)(2)'s reference to "section 5338(a)(2)(Q)" becomes "section 717 for the backlog retirement program", per division F sec. 101's rule against citing by letter.

### Title IV: Capital Investment Grants

```
SEC. 401. CAPITAL INVESTMENT GRANTS.

(a) FUNDING.—Amounts appropriated by section 105(a)(1) of division A shall be
available to carry out section 5309 of title 49, United States Code.

(b) FULL OBLIGATION.—Section 5338(d)(2) of such title is amended to read as
follows:
  "(2) GRANTS FINANCED FROM GENERAL FUND.—A full funding grant agreement or
  small start grant agreement financed with amounts appropriated by section
  105(a)(1) of division A of the Moving America Act of 2031 is a contractual
  obligation of the Government to pay the Government share stated in the
  agreement, and the Secretary shall obligate that share in full on the
  date the agreement is executed.".

(c) CONTINGENT COMMITMENTS.—The total of amounts obligated under section
5338(d)(2) of such title and committed under section 5309(k)(2) of such title
for fiscal years after 2036 may not exceed 60 percent of the amount
appropriated for fiscal year 2036, multiplied by the number of such fiscal
years, through fiscal year 2046.
```

Subsection (a) no longer appropriates; division A sec. 105 does, once. Secs. 402-407 are specified, not drafted: warrants as the default, match categories, a 120-day clock, tranche gates, one application for 5309(q) joint projects, and unit-cost review.

### Title VI: sec. 606, joint facilities outside the five terminals

Sec. 606 funds joint transit and intercity rail facilities outside the five sec. 310 nodes **\[A-6\]**: Denver Union Station, Seattle King Street, Portland Union Station and stations like them, at $0.60B a year.

```
SEC. 606. JOINT FACILITIES.

(a) GRANTS.—The Secretary may make grants from amounts appropriated by
section 105(a)(2) of division A for capital projects at facilities used by
both public transportation and intercity passenger rail transportation,
other than a facility for which a project is funded under section 310 of
division D.

(b) SHARE.—A grant under this section may pay only the share of the project
attributed to public transportation under section 109(a) of division A, at
a Federal share of not more than 80 percent of that share.

(c) COORDINATION.—An application under this section and an application for
the intercity share under division D shall be made and reviewed as one
application.
```

### Title VII: Buy America and the authorizations

Secs. 711-716 stand as drafted. Sec. 717 replaces every scattered 5338(a)(2) amount in the ATRA draft and cites programs by name, not letter (division F sec. 101). Because it rewrites 5338(a)(2) whole, sec. 715's cross-reference fixes must be conformed to its paragraph numbers.

```
SEC. 706. BUY AMERICA FOR JOINTLY FUNDED ROLLING STOCK.

For rolling stock procured through the national equipment pool under section
1201 of division D with amounts made available under both chapter 53 of
title 49, United States Code, and division D, the domestic content and final
assembly requirements of section 1201 of division D shall apply in lieu of
section 5323(j)(2)(C) of such title. Section 5323(j) is otherwise
unaffected.

SEC. 717. AUTHORIZATIONS FROM THE MASS TRANSIT ACCOUNT.

(a) IN GENERAL.—Section 5338(a)(2) of title 49, United States Code, is amended
to read as follows: "(2) There shall be available from the Mass Transit
Account of the Surface Transportation Trust Fund, to carry out each program
named below, the following amounts (in millions of dollars) for fiscal years
2032, 2033, 2034, 2035 and 2036 respectively:
  (1) service operating assistance, section 5307(i): 6,000; 6,500; 7,000;
  7,500; 8,000;
  (2) urbanized area formula grants, sections 5307 and 5340: 10,000; 10,400;
  10,800; 11,200; 11,700;
  (3) state of good repair formula, section 5337(c) and (d): 5,200; 5,400;
  5,600; 5,800; 6,000;
  (4) backlog retirement, section 5337(g): 6,000; 6,150; 6,300; 6,460;
  6,620;
  (5) asset management accountability, section 5326: 100 for each year;
  (6) transit resilience, section 304 of this division: 600 for each year;
  (7) workforce, title V of this division: 500; 550; 600; 600; 600;
  (8) buses and bus facilities, section 5339: 2,600; 2,700; 2,800; 2,900;
  3,000;
  (9) formula grants for rural areas, section 5311: 1,400; 1,450; 1,500;
  1,550; 1,600;
  (10) enhanced mobility of seniors and individuals with disabilities,
  section 5310: 600; 620; 640; 660; 680;
  (11) All Stations Accessibility, section 605 of this division: 1,000 for
  each year;
  (12) ferries, section 607 of this division: 200 for each year;
  (13) emergency relief, section 5324: 100 for each year; and
  (14) planning, administration, safety oversight, research and delivery,
  sections 5303, 5304, 5305, 5312, 5314, 5329 and 5334 and title VII of
  this division: 900; 920; 950; 970; 1,000.".

(b) TOTAL.—The amounts in subsection (a) total $190,920,000,000.
```

The $190.92B is the renewal total, checked in code. With $27.50B of CIG and $3.00B of sec. 606 from division A sec. 105, the division is $221.42B. Amounts in sec. 717 are subject to division A sec. 110(a); any reduction is restored by the transit top-ups.

### Shared provisions with division D

- **Station accessibility in reconciliation:** each package line names its class, Amtrak-served or rail transit and commuter, so there is no double count.
- **NEC access charges:** ARCA sec. 1103's repair component is an eligible 5337(g) backlog cost where the asset is in the baseline. One sentence goes in each division, plus 49 U.S.C. 24905(c).
- **49 U.S.C. 5302(15)** is untouched: it excludes Amtrak service from "public transportation" and keeps the two programs' eligibility separate.

## Division D — Intercity Passenger Rail (American Rail Competitiveness Act)

Division D authorizes **$254.03B** over FY2032-36, plus up to $25.00B of readiness reserve, contingent. Of the total, $160.83B is renewal from the Intercity Passenger Rail Account and $93.20B is expansion from division A sec. 105 (secs. 303, 310, 311, 312). By year: $39.95B / 47.29 / 52.07 / 56.13 / 58.59. Dedicated receipts cover 44% of rail renewal in FY2032-36 and 135% by FY2042-46, when the fossil premium also pays toward expansion; renewal is self-sufficient from FY2040. Its thirteen titles stand as ARCA rev 354 has them, with the changes recorded here.

| Title | Subject | FY2032-36 | Kind |
| --- | --- | --- | --- |
| I | The rail account, subaccounts, cross-references to division A | — | — |
| II | Core network: NEC base and capital, National Network, long-distance, national fleet, stations and ADA | $59.95B | Renewal |
| III | Corridor development: 301-306 renewal; 303, 310, 311, 312 expansion | $160.45B | $67.25B renewal, $93.20B expansion |
| IV-XIII | Accountability, commissions, access, industrial base, credit, permitting, operating support, competition, fleet pool, night network | $33.63B | Renewal **\[A-19\]** |
|  | **Total** | **$254.03B** |  |
| Div. A 106(e) | Readiness reserve, illustrated $0 / 0 / 5 / 8 / 12B | up to $25.00B | Expansion, contingent **\[A-22\]** |

### Title I

ARCA's revenue sections now live in division A sec. 104, its expansion appropriations in sec. 105, and its secs. 106-109 in division A. The corridor surcharge is dropped **\[A-13\]**, so the Commission Subaccount is funded from title V's authorization alone. Title I keeps one section:

```
SEC. 101. RAIL ACCOUNT; CONTRACT AUTHORITY.

(a) SOURCE OF AUTHORITY.—The Intercity Passenger Rail Account established by
section 101 of division A is the source of contract authority under this
division. No separate trust fund is established by this division.

(b) SUBACCOUNTS.—Within that Account there are established a Core Network
Subaccount, a Corridor Development Subaccount, a High-Speed Rail Subaccount,
a Credit Subaccount, and a Commission Subaccount.

(c) EXPENDITURES.—Amounts in the Account are available, without further
appropriation, to carry out titles II through XIII of this division, other
than sections 303, 310, 311 and 312.

(d) RULE OF CONSTRUCTION.—Nothing in this division limits the availability
of amounts in the Mass Transit Account for a joint facility under section 109
of division A.
```

### Sec. 303 and the Tier 1 allocation at $55.00B

**\[A-21\]** ARCA's own table of increments meant the program's growth from $40B to $55B for Palmdale-Los Angeles and Phoenix-Las Vegas. $7.0B goes to those two lines: $2.0B to California and $5.0B to Brightline West. California rises less than the full Palmdale-LA cost, because it is still gated on the sec. 401 remediation conditions. $8.0B stays unallocated for whichever corridor clears its gates first, a sixth included. Dallas-Houston stays at the $14.0B cap, and Texas keeps the largest single allocation.

| Corridor | Allocation | Status at enactment |
| --- | --- | --- |
| Dallas-Houston | $14.00B | Greenfield; no legacy alignment; at the cap |
| California: Merced-Bakersfield, Bakersfield-Palmdale, Palmdale-Los Angeles design and early works | $12.00B | Gated on the sec. 401 remediation conditions |
| Seattle-Portland | $7.00B | Service Development Plan completes 2028; later start |
| Charlotte-Atlanta | $6.50B | Extends the Southeast Corridor's cleared work north |
| Brightline West: Los Angeles Union and Phoenix extensions, Phoenix-Las Vegas | $7.50B | Private-led; federal share on public segments only |
| Unallocated: the first corridor to clear its gates | $8.00B | Released in the 2034-36 readiness window |
| **Total** | **$55.00B** |  |

```
SEC. 303. NATIONAL HIGH-SPEED RAIL PROGRAM.

(a) IN GENERAL.—The Secretary shall make grants for the construction of
Tier 1 high-speed intercity passenger rail corridors from amounts
appropriated by section 105(a)(3) of division A.

(b) ELIGIBLE APPLICANTS.—A State, an interstate compact, a regional corridor
commission established under title V, Amtrak, or a private operator may
apply, on identical terms.

(c) ENTRY.—No amount may be obligated for a project under this section until
the applicant has—
  (1) a record of decision under the National Environmental Policy Act of
  1969, or an executed programmatic agreement, covering the segment;
  (2) an executed rolling stock procurement, or a procurement strategy with a
  firm solicitation date;
  (3) ridership and revenue projections certified by an independent reviewer
  under section 402; and
  (4) a non-Federal share committed at a legal status stated under section
  403.

(d) TERMS.—The Federal share of a project may not exceed 50 percent. No
project with a total cost of less than $1,000,000,000 is eligible.

(e) CORRIDOR LIMIT.—Not more than $14,000,000,000 of amounts appropriated by
section 105(a)(3) of division A for fiscal years 2032 through 2036 may be
obligated for any one corridor. Section 106(e)(2) of division A limits the
total under this section and that section combined.
```

With the combined cap at $19.25B (35% of $55B, written in dollars), a corridor at the sec. 303 cap can still draw $5.25B from the reserve if it clears first.

### Sec. 310: the five terminals

**\[A-6\]** Sec. 310 ($20.20B) is the single program for the five nodes, and division A sec. 109 attributes each project between the modes.

| Node | Sec. 310 | Transit use | Transit share of renewal under sec. 109 |
| --- | --- | --- | --- |
| Chicago Union Station and CREATE | $9.0B | Commuter trains are 79% of movements | $7.11B |
| New York Penn and Sunnyside | $4.0B | LIRR and NJ Transit about 92% of riders | $3.68B |
| Washington Union Station | $3.5B | MARC and VRE about 45,000 of 61,500 weekday riders (73%); 2008 baseline, unverified | $2.56B |
| Los Angeles Union Station | $0.7B | Metrolink and Metro about 20,000 of 22,900 boardings (87%) | $0.61B |
| Atlanta | $3.0B | No intercity terminal exists | none to compute |
| **Existing four** | **$17.2B** |  | **$13.96B** if all of it is renewal |

Only Chicago's share is a movement count; the other three are ridership proxies under sec. 109(c). Expansion is attributed by added movements, which skews intercity at Chicago, Washington and Atlanta, so the true transit share lies between roughly $3B and $14B.

**What this does not settle.** Sec. 310 pays only the intercity share. The transit share has no dedicated program; it falls to commuter operators' 5307 and 5337 money, and $13.96B is 23.5% of all five-year 5337 formula and backlog money nationwide. Terminal renewal will move at the pace the transit side can be financed. Washington has no current design after its $8.8B expansion was cancelled in July 2026, and Atlanta is an access negotiation with Norfolk Southern before it is a construction project.

### Changes to ARCA's text

| Where | ARCA | This bill |
| --- | --- | --- |
| Canonical table | FY31-35 headers; reserve 0 / 5 / 7 / 7 / 6 | FY32-36; reserve 0 / 0 / 5 / 8 / 12 **\[A-22\]** |
| Secs. 102-104 | Aviation surcharge, corridor surcharge, rail diesel | Division A sec. 104; corridor surcharge dropped **\[A-13\]** |
| Sec. 311(e) | "fiscal years 2031 through 2035" | "fiscal years 2032 through 2036" |
| Sec. 601(b) | "Intercity Passenger Rail Trust Fund … Commission Account subaccount" | "Intercity Passenger Rail Account … Commission Subaccount under section 101(b)" |
| Secs. 503(c), 601(d) | "title II / title III of the American Rail Competitiveness Act" | "title II / title III of this division" |
| Title X | "mandatory, not contract authority" | Contract authority from the rail account, a renewal program **\[A-19\]** |
| Continuation | Rail renewal = secs. 201-205 | Division A sec. 101(f)(3) **\[A-19\]** |
| Short title | "Surface Transportation Reauthorization Act of 2031" | "Moving America Act of 2031" |
| Section-by-section rows 102, 106, 107 | $4 in 2031 → $12 in 2035; FY2045; FY2035 | $4 in FY2032 → $12 in FY2036; FY2046; FY2036 |

Two items remain open. Sec. 707's "$600M in grants" sits outside title VII's $3.95B, either an unfunded line or a double count. ARCA's "against the baseline" tables are still on its superseded $185.43B base. Neither moves a canonical total.

## Divisions E and F — Delivery, data and general provisions

Division E collects what all three modes share, about **$1.0B**, outside the fiscal model: data, a per-mile evaluation, delivery capacity, and the grant pipeline fixes GAO's findings call for. Division F carries no money. Both are specified, not drafted.

### Division E: Research, Data and Project Delivery

| Sec. | Provision | FY2032-36 |
| --- | --- | --- |
| 101 | National intercity passenger travel forecast, all modes, every five years | $0.10B |
| 102 | One public unit-cost database for highway, transit and rail projects over $100M, fed by div. B secs. 1106(d) and 1111, div. C sec. 705, div. D sec. 705 | $0.15B |
| 103 | Road user charge evaluation: collection cost, evasion, privacy compliance and rural and income incidence of the sec. 4491 and 4495 charges, reported yearly to the tax committees; complements GAO's review under 26 U.S.C. 4494(d) | $0.10B |
| 104 | **Grant pipeline**, all modes: an agreement executed within 180 days of selection or the Secretary reports why; pre-award authority for costs after selection; scope changes within 10% without reselection; executed agreements protected by a decision deadline, cure period, published basis and judicial review before termination (div. D sec. 407, extended) | policy |
| 105 | Permitting parity: div. D secs. 901-905 for rail, plus Coast Guard and Corps 408 clocks for transit and highway bridges | policy |
| 106 | Owner-side engineering and delivery capacity grants to State DOTs and transit agencies, matching div. D sec. 707 | $0.50B |
| 107 | BTS and the National Transit Database: multi-area apportionment data published with each apportionment | $0.15B |
|  | **Total** | **$1.00B** |

Sec. 104 answers GAO-25-107166: as of April 2025, 23% of surveyed IIJA discretionary awardees had no signed agreement, and 31 of 32 FY2019 BUILD and RAISE projects changed between selection and signing. Division E is not in the $936.57B. From the general fund it adds about $0.2B a year to the draw, which takes FY2032's all-in figure to about 0.2085%, a little further over the benchmark **\[A-4\]**.

### Division F: Budget Discipline and General Provisions

| Sec. | Provision |
| --- | --- |
| 101 | Cross-references to 49 U.S.C. 5338(a) and 23 U.S.C. 104 cite programs by name, not subparagraph letter, so a relettering in any later bill cannot misdirect money. Div. C sec. 717 is written that way |
| 102 | Buy America for jointly funded rolling stock: the equipment pool's standard (div. D sec. 1201, div. C sec. 706); each mode's own rule elsewhere |
| 103 | Labor: 49 U.S.C. 5333(b) and Railway Labor Act protections carried through any Amtrak reorganization and to joint facilities under div. A sec. 109 |
| 104 | Reconciliation money obligated in FY2029-31 counts toward a program's FY2032-36 baseline only where obligated, and top-ups are not double-counted in the div. A sec. 108 report **\[A-16\]** |
| 105 | Effective date October 1, 2031, the first day of FY2032 and the day the Corridor ID new-selection sunset falls; continuation under div. A sec. 107 if the bill lapses **\[A-20\]** |

## Canonical authorization table, FY2032-36

This table governs every authorization figure in the bill: **$936.57B** across divisions B-D, $812.87B of renewal from the three accounts and $123.70B of expansion from the general fund. Every row was generated from the model's arrays and checked in code. Where any other figure disagrees, this table wins. Amounts are $B; R is renewal, X expansion.

| Div. | Sec. | Program | R/X | Source | FY32 | FY33 | FY34 | FY35 | FY36 | Total |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| B | 1101 | FHWA programs (H.R. 8870 title I continued) | R | Highway Acct | 79.58 | 81.57 | 83.60 | 85.69 | 87.84 | 418.28 |
| B | 1104 | Interstate and Bridge Renewal **\[A-23\]** | R | Highway Acct | 2.05 | 4.10 | 6.15 | 8.21 | 10.26 | 30.77 |
| B | 1201, 1301 | NHTSA and FMCSA | R | Highway Acct | 2.29 | 2.35 | 2.42 | 2.48 | 2.53 | 12.07 |
| **B** |  | **Division B total** |  |  | **83.92** | **88.02** | **92.17** | **96.38** | **100.63** | **461.12** |
| C | 201 | Service operating assistance, 5307(i) | R | Transit Acct | 6.00 | 6.50 | 7.00 | 7.50 | 8.00 | 35.00 |
| C | 301 | State of good repair formula, 5337 | R | Transit Acct | 5.20 | 5.40 | 5.60 | 5.80 | 6.00 | 28.00 |
| C | 302 | Backlog retirement, 5337(g) | R | Transit Acct | 6.00 | 6.15 | 6.30 | 6.46 | 6.62 | 31.53 |
| C | 303 | Asset management, 5326(e) | R | Transit Acct | 0.10 | 0.10 | 0.10 | 0.10 | 0.10 | 0.50 |
| C | 304 | Transit resilience | R | Transit Acct | 0.60 | 0.60 | 0.60 | 0.60 | 0.60 | 3.00 |
| C | 401 | Capital Investment Grants, 5309 | X | GF (A-105) | 4.50 | 5.00 | 5.50 | 6.00 | 6.50 | 27.50 |
| C | 501 | Workforce (501-506) | R | Transit Acct | 0.50 | 0.55 | 0.60 | 0.60 | 0.60 | 2.85 |
| C | 601 | Urbanized area formula, 5307/5340 | R | Transit Acct | 10.00 | 10.40 | 10.80 | 11.20 | 11.70 | 54.10 |
| C | 602 | Buses and bus facilities, 5339 | R | Transit Acct | 2.60 | 2.70 | 2.80 | 2.90 | 3.00 | 14.00 |
| C | 603 | Rural, tribal, intercity bus, 5311 | R | Transit Acct | 1.40 | 1.45 | 1.50 | 1.55 | 1.60 | 7.50 |
| C | 604 | Seniors and disabilities, 5310 | R | Transit Acct | 0.60 | 0.62 | 0.64 | 0.66 | 0.68 | 3.20 |
| C | 605 | All Stations Accessibility | R | Transit Acct | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 5.00 |
| C | 606 | Joint facilities outside the sec. 310 nodes **\[A-6\]** | X | GF (A-105) | 0.60 | 0.60 | 0.60 | 0.60 | 0.60 | 3.00 |
| C | 607 | Ferries | R | Transit Acct | 0.20 | 0.20 | 0.20 | 0.20 | 0.20 | 1.00 |
| C | 608 | Emergency relief, 5324 | R | Transit Acct | 0.10 | 0.10 | 0.10 | 0.10 | 0.10 | 0.50 |
| C | 701 | Planning, FTA capacity, safety, research (701-705) | R | Transit Acct | 0.90 | 0.92 | 0.95 | 0.97 | 1.00 | 4.74 |
| **C** |  | **Division C total** |  |  | **40.30** | **42.29** | **44.29** | **46.24** | **48.30** | **221.42** |
| D | 201(a) | Amtrak NEC base grant | R | Rail Acct | 2.00 | 2.00 | 2.00 | 2.00 | 2.00 | 10.00 |
| D | 201(b) | NEC Capital Program | R | Rail Acct | 3.00 | 3.30 | 3.50 | 3.55 | 3.65 | 17.00 |
| D | 202 | National Network operating | R | Rail Acct | 2.20 | 2.20 | 2.20 | 2.20 | 2.20 | 11.00 |
| D | 203 | Long-distance preservation | R | Rail Acct | 0.90 | 0.92 | 0.95 | 0.96 | 0.97 | 4.70 |
| D | 204 | National Fleet Program | R | Rail Acct | 1.90 | 2.35 | 2.80 | 3.05 | 3.00 | 13.10 |
| D | 205 | Stations and ADA | R | Rail Acct | 0.75 | 0.85 | 0.90 | 0.85 | 0.80 | 4.15 |
| D | 301 | Corridor ID and Service Development | R | Rail Acct | 0.50 | 0.50 | 0.50 | 0.50 | 0.50 | 2.50 |
| D | 302 | Intercity capital, Tier 2-3 | R | Rail Acct | 6.20 | 7.20 | 7.80 | 8.20 | 8.60 | 38.00 |
| D | 303 | National High-Speed Rail (Tier 1) | X | GF (A-105) | 6.00 | 9.00 | 11.00 | 13.50 | 15.50 | 55.00 |
| D | 304 | CRISI | R | Rail Acct | 2.50 | 2.50 | 2.50 | 2.50 | 2.50 | 12.50 |
| D | 305 | Grade crossing elimination | R | Rail Acct | 2.50 | 2.50 | 2.50 | 2.50 | 2.50 | 12.50 |
| D | 306 | Safety implementation | R | Rail Acct | 0.40 | 0.40 | 0.35 | 0.30 | 0.30 | 1.75 |
| D | 310 | Terminals of national significance | X | GF (A-105) | 2.50 | 3.70 | 4.50 | 4.80 | 4.70 | 20.20 |
| D | 311 | Federally initiated corridors | X | GF (A-105) | 1.60 | 1.40 | 1.10 | 0.95 | 0.95 | 6.00 |
| D | 312 | Long-distance network implementation | X | GF (A-105) | 1.50 | 2.00 | 2.50 | 3.00 | 3.00 | 12.00 |
| D | IV | Accountability and review | R | Rail Acct | 0.25 | 0.27 | 0.27 | 0.27 | 0.27 | 1.33 |
| D | V | Regional commissions | R | Rail Acct | 0.20 | 0.20 | 0.20 | 0.20 | 0.20 | 1.00 |
| D | VI | Access, operations, ticketing | R | Rail Acct | 0.15 | 0.20 | 0.20 | 0.15 | 0.15 | 0.85 |
| D | VII | Industrial base, workforce, delivery | R | Rail Acct | 0.90 | 0.90 | 0.80 | 0.70 | 0.65 | 3.95 |
| D | VIII | Credit | R | Rail Acct | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 5.00 |
| D | IX | Permitting parity | R | Rail Acct | 0.10 | 0.10 | 0.10 | 0.10 | 0.10 | 0.50 |
| D | X | Operating support **\[A-19\]** | R | Rail Acct | 0.80 | 1.20 | 1.60 | 2.00 | 2.40 | 8.00 |
| D | XI | Access, competition, structure | R | Rail Acct | 0.40 | 0.30 | 0.30 | 0.25 | 0.25 | 1.50 |
| D | XII | National fleet pool | R | Rail Acct | 1.30 | 1.70 | 1.80 | 1.90 | 1.80 | 8.50 |
| D | XIII | Night network | R | Rail Acct | 0.40 | 0.60 | 0.70 | 0.70 | 0.60 | 3.00 |
| **D** |  | **Division D total** |  |  | **39.95** | **47.29** | **52.07** | **56.13** | **58.59** | **254.03** |
|  |  | **Total, divisions B-D** |  |  | **164.17** | **177.60** | **188.53** | **198.75** | **207.52** | **936.57** |
|  |  | of which renewal | R |  | 147.47 | 155.90 | 163.33 | 169.90 | 176.27 | 812.87 |
|  |  | of which expansion (div. A sec. 105) | X |  | 16.70 | 21.70 | 25.20 | 28.85 | 31.25 | 123.70 |

Renewal is paid by dedicated receipts ($545.84B) and the reconciliation top-ups ($267.07B); in FY2036 transit receipts also cover $0.04B of CIG. The NHTSA and FMCSA row is rounded so each year's division B total matches the model. Three things sit outside the table:

- up to **$25.00B** of readiness reserve (div. A sec. 106(e)), illustrated at 0 / 0 / 5 / 8 / 12 **\[A-22\]**;
- **$17.24B** of division B sec. 1112 general-fund grants, subject to appropriation **\[A-18\]**;
- about **$1.0B** of division E.

## The 250-Plus baseline and the FY2029-31 bridge

BUILD America 250-Plus funds FY2027-31 at roughly IIJA levels in nominal terms and leaves the trust fund insolvent. It is this project's forecast, not law: H.R. 8870 as reported 62-2 on May 22, 2026, assumed enacted after the current extension (to Dec 11, 2026) with one Senate trade, partial guarantees for rail and CIG in exchange for the House's accountability and cost-share riders. FY2031 is its final year for every mode: highways $77.64B FHWA plus $2.24B safety, transit $20.71B, rail $13.3B.

### The 2026-bill discipline rule

**Nothing in 250-Plus is sized to anything in this document.** Lawmakers in December 2026 do not have the FY2032-46 program in front of them. Three consequences:

1. **H.R. 8870 as written contains no general-fund transfer.** It authorizes contract authority against accounts CBO projects will run dry (transit in FY2027, highways in FY2028). The model's FY2027-31 general-fund column is an inference about what Congress must do later, not a provision of any bill.
2. **The proposed transfer stays at $108.0B:** $71.2B highway plus $36.8B transit, CBO's shortfall through FY2030. A 2026 Congress patches to the cash in front of it, as it did repeatedly from 2008 to 2014.
3. **FY2031 solvency is the 2028 extension's job, not 250-Plus's** **\[A-9\]**. If both accounts are not solvent on Oct 1, 2031, division A sec. 101(c)'s FY2028 floors are credited against receipts already spoken for. That risk is real and unmodelled until the cash-flow model exists.

### What 250-Plus does, by mode

| Mode | H.R. 8870 as written | Guaranteed | Delivered (forecast) |
| --- | --- | --- | --- |
| Highways (FHWA) | $375.5B: $372.4B limitation + about $3.2B exempt; $72.9B (FY2027) → $77.6B (FY2031) | contract authority | same |
| Highways: general-fund grants | $26B: competitive bridge program $10B, multimodal freight $6B, National Infrastructure Grants $10B | none | subject to appropriation |
| Transit | $87.6B contract authority + $15.0B CIG + $0.15B WMATA (FY2031) | $92.6B (90%), with $5.0B CIG in the Senate trade | about $99.8B |
| Passenger rail | about $62.4B, all subject to appropriation | $22.0B (30%): NEC $6.0B, National Network $10.0B, Partnership $6.0B | about $59.6B |

CBO's estimate for H.R. 8870 (Sept 30, 2026) totals $579.3B of authorizations and exhausts the transit account in FY2027 and the highway account in FY2028. Cumulative shortfalls at end-FY2031 are $99.5B highway and $48.2B transit, assuming the expiring fuel taxes continue. The bill sends its EV fee ($16.8B gross, $12.4B net, FY2026-36) to the general fund. Transit delivery is 8% below the IIJA in nominal terms and 18% below in real terms.

**What H.R. 8870 already does for transit:** operating eligibility up to 25% for systems with 101-125 peak buses (sec. 3005); a voluntary State block grant outside areas over 3.5 million (sec. 3006); 1.5% for security operations (sec. 3012); Streamlined Starts with a $1B ceiling (sec. 3007); repeal of the 5337(f) railcar program (sec. 3022); a bus federal-share cap (sec. 3013); and, from FY2028, 10% withholding where fare evasion is not an offense.

**Rail riders carried as written:** Railway Safety Act provisions, station modernization authority, declining federal shares in the Partnership program, an Amtrak mission rewrite toward financial performance, and RRIF's ceiling raised from $35B to $50B with Amtrak and compacts eligible. The Corridor ID new-selection sunset (Oct 1, 2031) falls on this bill's first day, and division D makes the program permanent.

**Three small additions proposed for the 250-Plus vehicle:** annual reporting of capital funds used on operations; the $108.0B two-account transfer; and restoring the 5337(f) railcar program ($1.5B) as the trade for the fare-evasion condition. The paired American Affordability and Jobs Act is assumed to pass the same lame duck, with two-year EIS deadlines and remand instead of vacatur; division E closes the gaps it leaves.

### FY2029-32 by mode ($B)

The reconciliation schedule turns what was a cliff into a ramp **\[A-16\]**.

|  | FY2029 | FY2030 | FY2031 | FY2032 |
| --- | --- | --- | --- | --- |
| Highways and safety | 77.16 | 78.49 | 79.88 | 83.92 |
| Transit, with the schedule | 23.93 | 33.24 | 35.71 | 40.30 |
| Rail, with the schedule | 17.90 | 29.90 | 38.80 | 39.95 |
| Rail, each package obligated in its enactment year | 46.90 | 26.40 | 13.30 | 39.95 |
| Draw, % of GDP | 0.194% | 0.225% | 0.215% | 0.200% |
| Room under the benchmark | 4.03 | −7.06 | −3.70 | 2.50 |

FY2030-31 run over the benchmark by $7.1B and $3.7B. That is 250-Plus's own shortfall plus the reconciliation money arriving before most new rates do, and it is accepted **\[A-4\]**. Transit FY2031 includes 250-Plus's $20.71B: $18.16B contract authority, $2.40B CIG delivered and $0.15B WMATA.

## Political path

The bill passes in four moves, and each later move is easier because the earlier one happened:

1. **2028:** a one-year extension that keeps the expiring base as a forcing event and carries the FY2031 transfer.
2. **2029:** the revenue structure and most of the money, by reconciliation.
3. **2030:** the truck and rail taxes and the rest of the top-ups, by reconciliation, before the midterms.
4. **2031:** the authorization, reforming what reconciliation already did rather than inventing it, with almost no new general fund beyond expansion.

### Committees

| Vehicle or division | House | Senate |
| --- | --- | --- |
| 2028 extension | Ways and Means; T&I | Finance; EPW, Commerce, Banking |
| 2029 and 2030 instructions | Budget, to Ways and Means and T&I | Budget, to Finance, EPW, Commerce and Banking |
| A: trust fund and revenue | Ways and Means | Finance |
| B: highways and safety | T&I | EPW; Commerce for NHTSA and FMCSA |
| C: public transportation | T&I | Banking |
| D: intercity passenger rail | T&I | Commerce |
| E: delivery and data | T\&I; Science | Commerce, EPW |
| Obligation limitations on renewal | Appropriations | Appropriations |

Senate EPW carries the surface bill, and the four Senate reports merge in conference. Appropriators get real obligation limitations on $812.87B of renewal and nothing on expansion, which is mandatory.

### 2027-28: the positioning window

Nothing big passes in this window. The job is to win the 2028 extension on the right terms and build the record:

- **The extension:** one year, current rates, the transfer through FY2031, the use tax to Sept 30, 2030, and no merger of the accounts. The Secretary's July 2026 letter proposes eliminating the Mass Transit Account; Graves and Larsen rejected it, and the extension should too.
- **The record:** CBO scores of the steps and the clean-vehicle charge; a Treasury-DOT design for collecting sec. 4491 at State registration, with States that already run road usage charges as partners; GAO work on capital used for operations and on FTA staffing (781 in FY2024, 552 in FY2026).
- **Marker bills** on transit operating stability, asset renewal, the trust fund, Interstate renewal, and ARCA's own.

### Coalition

| Bloc | What the bill gives them | Provision |
| --- | --- | --- |
| Highway builders and State DOTs | About 90% formula money kept; the first Interstate renewal program; highway renewal fully funded through FY2036 by receipts plus top-ups; 45% of new revenue from FY2037 | B 1101, 1104; A 101(d), 110 |
| Counties and cities | Direct SS4A access with a 15% planning share; STBG suballocation at 60%; 20% off-system bridge money; the heavier-truck pilot ended | B 1103, 1109, 1114, 1115 |
| Safety advocates | Safe System conditions, consequences for regressive targets, speed management, a vulnerable-road-user rule that scales with deaths | B 1109 |
| Owner-operators, the Teamsters, safety and rail groups against bigger trucks | The 91,000-lb pilot ends; truck parking money roughly triples; light trucks pay far less per mile than heavy ones | B 1113, 1114; A 104 |
| Environmental and resilience groups | A fossil transition premium clean vehicles never pay, resilience set-aside, carbon reduction restored, a charging program that pays only for working chargers, CMAQ alternative-fuel money held at 10%, a 4% excise for zero-emission trucks | B 1110, 1116; A 104(c) |
| Northeast delegation | The NEC backlog funded with a guarantee; commuter-rail operating money | D 201 ($27.00B); C 201 |
| Large-system delegations | Operating money by formula and the backlog on a schedule | C 201 ($35.00B), 302 ($31.53B) |
| Rural and long-distance States | Long-distance preservation and new routes; an 80% rural operating share; the Interstate formula's lane-mile weighting | D 203, 312; C 603; B 1104 |
| Southeast, Texas, Midwest and Cascadia | Commissions and the Tier 1 pipeline: Charlotte-Atlanta $6.50B, Dallas-Houston $14.00B at the cap, Seattle-Portland $7.00B | D 302, 303, 501 **\[A-21\]** |
| Sun Belt growth regions | CIG obligated in full at signing | C 401; A 105(b) |
| Fiscal conservatives | Both reconciliation acts reduce deficits; contract authority within receipts; fix-it-first; statutory gates and a dollar cap per corridor | A 108, 110; B 1106; D title IV |
| Privacy hawks of both parties | Odometer only, a statutory bar on location data, return-information protection | A 111 **\[A-11\]** |
| Labor | Service floor, apprenticeships, 5333(b) and Railway Labor Act protections | C 201, title V; F 103 |
| Freight railroads | Capital and compensation; diesel at 15¢ for Class I, short lines exempt | D 602; A 104 **\[A-13\]** |
| Disability advocates | A completion date for station accessibility and an ADA deadline | C 605; D 205 |

### The hard votes

**The steps.** A federal fuel-tax increase every year for ten years, after the 2022-26 price shocks. For a 25-mpg car driven 12,000 miles, federal fuel tax goes from $88 a year to $142 in FY2032 and $225 in FY2036. The case: every cent goes to repair first, the pause stops a step whenever prices spike, and in 2029 dollars the rate ends near where 1993 left it. Seventy-four percent backed a 10¢ maintenance increase in MTI's 2024 survey. The fossil transition premium comes a decade later and is smaller, 2¢ a year for five years, and is argued as what it is: from 2040, fossil fuel pays more than road use costs, and clean vehicles do not.

**Highways' share.** Highways get 35% of new revenue through FY2036, against the 88% of legacy receipts they hold today. The answer: the FY2028 base is protected and indexed, the top-ups fill highway renewal in full, the Interstate gets its own program, and the share rises to 45% in FY2037.

**Trucks.** At 3.4¢ a mile, an 80,000-lb tractor running 100,000 miles pays about $3,400 a year in weight-distance charge in place of the $550 use tax, plus the diesel steps. The case is the cost-allocation study the 2029 act orders: heavy trucks do most of the pavement damage, and the charge is the condition for ever raising weight limits.

### What is tradeable and what is not

| Dial | Range | Drafted, and the cost of moving it |
| --- | --- | --- |
| Fuel-tax step | 2-3¢ | 3¢. At 2¢, renewal coverage in FY2042-46 falls to 85 / 88 / 111 |
| Price pause | $3.50-4.50; 15-25% | $4.00 indexed or 20%. Lower thresholds pause more often; revenue returns later |
| Weight-distance average | 2-3.5¢ | 3¢. At 2¢ the draw rises about 0.005 points |
| Parity benchmark | 25-40 mpg | 40 mpg, an efficient hybrid. At 25, about $5.7B more in FY2032-36 |
| Interstate and Bridge Renewal new money | $0-12B a year by FY2036 | 0 / 2 / 4 / 6 / 8. Each $2B a year adds about 0.005 points |
| Added-lane federal share cut | 0-10 points | 10 points |
| Charging Gap Program | $0.25-1B a year | $0.5B rising 2.5%, plus unspent NEVI balances; 40% freight, 30% rural |
| Fossil transition premium | 0-3¢ a step; 3-10 steps; start FY2037-42 | Five 2¢ steps from FY2040. Without it, FY2042-46 draws 0.065% instead of 0.026% |
| Interstate tolling | rebuilt segments, or pilot slots only | Rebuilt segments |
| Operating tier | $4-8B a year | $6B rising to $8B **\[A-3\]** |
| Backlog period | 20-30 years | 20 years; 30 saves about $10.5B over the bill |
| Aviation surcharge | $4-16 | $4 → $12 → $16 cap |
| Rail diesel | 4.3-24.4¢ | 15¢ / 7.5¢ |
| Tier 1 size | $4-55B | $55B; see fallback tiers |
| H.R. 8870 fare-evasion and security conditions | keep or drop | Worth trading for maintenance of effort |

**Not tradeable.** Without these the bill is 250-Plus with larger numbers and an empty fund:

- **Division A:** renewal-first and the 9503(e)(3) fix (101(f), (g)), transit's written share (101(d)), permanent credits (103(d)), contract authority within receipts (110(a)), continuation (107), and the location-data bar (111).
- **Division B:** sec. 1104's bar on general-purpose lanes and its renewal plan; sec. 1106(a)(3)'s bar on condition targets below actual condition.
- **Division C:** the 5307(i)(4) conditions and full obligation under 5338(d)(2).
- **Division D:** the title IV gates, the sec. 403 match taxonomy, and the sec. 602 covenants.

## Fallback tiers

If the bill has to shrink, it shrinks in three rounds that cut construction and expansion first and leave the structural provisions alone, ending at **$739.25B** with the draw at 0.089% of GDP. Each cut comes off the general-fund draw dollar for dollar, because every mode draws general fund in every year. Transit's rounds are ATRA's; rail's were rebuilt on the canonical lines and are not yet reviewed. Two highway options can pair with any round.

| Round | Highways and safety | Transit | Rail | Bill | Draw, FY2032-36 avg |
| --- | --- | --- | --- | --- | --- |
| The bill | $461.12B | $221.42B | $254.03B | **$936.57B** | 0.180% |
| First | — | −$27.00B → $194.42B | −$44.55B → $209.48B | **$865.02B** | 0.147% |
| Second | — | −$30.02B → $164.40B | −$30.70B → $178.78B | **$804.30B** | 0.119% |
| Third | — | −$34.40B → $130.00B | −$30.65B → $148.13B | **$739.25B** | 0.089% |
| Highway option 1: FHWA and safety flat at FY2031 nominal | −$30.97B | — | — | any round | −0.014 points |
| Highway option 2: no new Interstate and Bridge Renewal money | −$20.00B | — | — | any round | −0.009 points |

### What each round cuts

**Transit:**

- **First:** operating tier flat at $4.0B a year ($20.0B); CIG to $20.0B; buses to $11.5B; resilience to $1.0B.
- **Second:** backlog on a 30-year schedule ($21.0B); formula capital to $46.1B; operating tier to $15.0B; CIG to $15.0B; accessibility to $3.5B.
- **Third:** operating tier for three years only ($9.0B); backlog to $15.0B; formula capital to $38.0B; repair formula to $24.0B; CIG to $12.5B; buses to $9.0B; other lines down $5.3B. That is the IIJA in FY2031 dollars with a three-year operating bridge.

**Rail:**

- **First:** sec. 303 to $22.0B (two greenfield corridors and California); crossings to $8.0B; fleet to $11.0B; NEC Capital Program to $14.0B; title VII to $2.0B; readiness reserve to $10B.
- **Second:** sec. 302 to $28.0B; sec. 303 to $12.0B; CRISI to $10.0B; long-distance to $4.5B; fleet to $9.0B; sec. 312 to $6.0B; reserve to zero.
- **Third:** NEC Capital Program to $10.0B; sec. 302 to $20.0B; sec. 303 to $4.0B; National Network operating to $10.0B; crossings to $4.0B; stations to $3.5B; sec. 311 to $1.0B.

Any round that cuts sec. 303 below $40B should cut the $14.0B corridor cap with it; under the first round it would let one corridor take 64% of the program **\[A-21\]**.

**Highways:** option 1 holds FHWA and safety at $77.64B and $2.24B instead of growing them 2.5% a year, a 7.2% real cut over five years. Option 2 keeps the converted bridge program in sec. 1104 but adds no new money. Neither touches the fix-it-first or safety provisions.

### What survives every round

- Division A in full: the fund, the revenue, the shares, contract authority within receipts, continuation, the report, the location-data bar.
- Division B's sec. 1104 as a program, sec. 1106 and sec. 1109.
- Division C's 5307(i) conditions and full obligation under 5338(d)(2), whatever the tier's size.
- Division D's title IV gates and sec. 403 match taxonomy ($1.33B), title V commissions ($1.0B), title VI access and preference enforcement ($0.85B), and the sec. 205 ADA reserve with its FY2036 deadline ($2.5B): about $5.7B.

## Open items

Four things stand between this draft and a bill that can be scored: the 2028 extension's terms, a cash-flow model, a score of both reconciliation acts, and checking divisions A and B against H.R. 8870 as enacted. Everything else is drafting or verification that does not move a total.

### Before the bill can be scored

- [ ] **Size the 2028 extension's transfer** so both accounts are solvent through FY2031, and model the case where the extension slips or runs longer than a year **\[A-9\]**. It is the largest unmodelled risk.
- [ ] **Build the trust-fund cash-flow model:** three accounts, outlay timing, the sec. 110(a) cap, the top-ups and the sec. 108(c) backstop. It decides whether the FY2028 floors are real money on Oct 1, 2031.
- [ ] **Score both reconciliation acts and division A** on CBO and JCT conventions, including fuel demand response to the steps (probably 2-3% of fuel receipts) and to the fossil premium, whose FY2042-46 receipts ($124.8B) are an upper bound. The estimates here are budget authority from this project's model.
- [x] **Fold the overlays into the model.** Done Oct 20, 2026: `moving_america.py` is one model with no patching, checked line for line against the old `final_v3.py` output. One open point: the A-7 equal-coverage solve (50.5/37.6/12.0) came from the old script's 25-mpg / PHEV-50% sensitivity path; on the governing design it is 50.0/38.2/11.8.

### Revenue and Code

- [ ] Confirm 26 U.S.C. 9502(b) does not send the new 4283 tax to the Airport and Airway Trust Fund.
- [ ] Draft the 4081 / 6427(l) conforming rule so train fuel removed at a terminal bears the class rate.
- [ ] Set the weight-distance schedule from the cost-allocation study due March 31, 2030, in time for the 2030 act.
- [ ] Design IFTA collection agreements for sec. 4495 and State registration agreements for sec. 4491.
- [ ] Re-date sec. 103(d) once the 2028 extension's dates are known.

### Drafting

- [ ] **Division B against H.R. 8870 as enacted:** program shares and top-line, the bridge formula ($9.0B or $9.2B), the INFRA general-fund level ($1.2B or $2B), whether sec. 7105 is titled National Infrastructure Grants, the 91,000-lb pilot's enacted form, the NHTSA / FMCSA split, chapter 1's section numbering for sec. 1104, and the sec. 1129 EV-fee text amended by div. A sec. 103(e).
- [ ] **Sec. 1104's apportionment data run:** Interstate lane-miles, Interstate travel and NBI deck area by State.
- [ ] **Sec. 1116's gap map and first auction:** station data from DOE's Alternative Fuels Data Center, freight-site demand, the standard agreement, and how much NEVI money remains unobligated in 2031.
- [ ] **The reconciliation spending titles:** top-up lines by program, with the deadlines in "The vehicles".
- [ ] **Division B specified sections:** 1102, 1103, 1107, 1108, 1111, 1115, 1201 and 1301.
- [ ] **Division C:** secs. 402-407, 501-506, 601-605, 607-608 and 701-705. Read 49 CFR parts 625, 630 and 673 against titles II and III.
- [ ] **Division D:** titles V-IX text, sec. 302's formula, and sec. 310's project list under the sec. 109 rule. Sec. 707's $600M must be funded or dropped.
- [ ] **The rail Buy America cites** (49 U.S.C. 22905(a), 24305(f)) were quoted from ARCA and not re-read.

### Facts to verify

- [ ] Washington Union Station's commuter figures (2008 baseline) and a replacement design after the July 2026 cancellation.
- [ ] How the $3-14B transit share at the five terminals is financed **\[A-6\]**.
- [ ] An FTA national cost for legacy rail-station accessibility (sec. 605). Only system figures exist: MTA about $35B, SEPTA $2.4B, CTA $2.1B.
- [ ] Rerun the 5307(i) apportionment with FTA's multi-area splits.
- [ ] ATRA's unverified pipeline facts: Red Line Extension 2030 opening; Honolulu's $10.08B and opening date; IndyGo cost; Red-Blue Connector; RPM next phases.
- [ ] Check the working title "Moving America Act" for conflicts before public use.

### Review

- [ ] An independent review of the division B design, especially secs. 1104 and 1106, with State DOT and county input.
- [ ] The rebuilt rail fallback rounds.
- [ ] Mark the source docs (ARCA, ATRA, the package doc and the archived merge doc) as superseded by this draft.

## Sources

**Merged from:**

- [Moving America Act of 2031 — Unified Bill Architecture](https://claude.ai/code/artifact/6aae1b34-e426-48b0-8d3e-85b483b00918) (archived merge doc, rev 122)
- [American Rail Competitiveness Act of 2031 — Full Bill Architecture](https://claude.ai/code/artifact/518f3bb4-2063-42e2-9b4b-1936f8d19ca8) (rev 354; repo copy `sources/transportation-arca-2031-bill-architecture.md`)
- [American Transit Renewal Act of 2031 — Full Bill Architecture](https://claude.ai/code/artifact/6eded0d5-40fc-433a-b940-8d8ca015f581) (rev 161; repo copy `sources/transportation-atra-2031-bill-architecture.md`)
- [Surface Transportation Package — Section-by-Section](https://claude.ai/code/artifact/fb14029c-152b-4727-9ae3-b2f055c8b6f7) (rev 119; repo copy `sources/transportation-package-section-by-section.md`)

**Project files:** `index/tools/transportation/moving_america.py` and `report.py` (every figure here), with the old overlay stack in `index/tools/transportation/legacy/`, plus `sources/transportation-calendar-fy2032-36.md`.

**Statute:**

- [26 U.S.C. 4041](https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section4041): the train rate is (a)(1)(C)(ii), zero since 2007; (iii) is buses.
- [26 U.S.C. 4283](https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section4283): repealed in 1990, so the number is free.
- [26 U.S.C. 9503](https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section9503): fund credits end for taxes received after Sept 30, 2028; (b)(4)(C) excludes train fuel; (e)(3) carries the capital-only language.
- 26 U.S.C. 4081(d), 4051(c), 4071(d) and 4481(f): the fuel-rate drop after Sept 30, 2028, the truck and tire excise end dates, and the use tax's Oct 1, 2029 end.
- [49 U.S.C. 5338](https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title49-section5338): current lettering of 5338(a)(2).

**H.R. 8870 and the baseline:**

- [H.R. 8870 text as introduced](https://www.congress.gov/119/bills/hr8870/BILLS-119hr8870ih.htm)
- [T&I section-by-section, as reported (ANS)](https://transportation.house.gov/UploadedFiles/ANS_BUILD_America_250_Section_by_Section.pdf) and [as introduced](https://transportation.house.gov/uploadedfiles/build_america_250_act_section_by_section.pdf)
- [CBO cost estimate for H.R. 8870, Sept 30, 2026](https://www.cbo.gov/system/files/2026-09/hr8870..pdf)
- [CBO Highway Trust Fund baseline, June 2026](https://www.cbo.gov/system/files/2026-06/51300-2026-06-highwaytrustfund.pdf)
- [APTA's H.R. 8870 funding table](https://www.apta.com/wp-content/uploads/2026/06/HR-8870-BUILD-America-250-Draft-Funding-Table-Public-Transit-05222026.pdf)
- Holland & Knight: [a closer look at the BUILD America 250 Act](https://www.hklaw.com/en/insights/publications/2026/05/a-closer-look-at-the-build-america-250-act), [the House reauthorization](https://www.hklaw.com/en/insights/publications/2026/05/build-america-250-act-house-surface-transportation-reauthorization), [Secretary Duffy's July letter](https://www.hklaw.com/en/insights/publications/2026/07/dot-secretary-duffy-reiterates-surface-transportation-reauthorization)
- [Surface transportation programs extended to December 2026](https://www.masstransitmag.com/management/article/55403068/surface-transportation-programs-extended-to-december-2026)
- [DOT IIJA authorization table](https://www.transportation.gov/sites/dot.gov/files/2022-01/DOT_Infrastructure_Investment_and_Jobs_Act_Authorization_Table_%28IIJA%29.pdf)

**Stakeholder analyses of H.R. 8870:**

- [AASHTO Journal](https://aashtojournal.transportation.org/?p=40502); [ARTBA first look](https://www.artba.org/news/artbas-first-look-house-surface-transportation-reauthorization-proposal/); [ACEC summary](https://www.acec.org/wp-content/uploads/2026/06/BUILD-America-250-Act-summary.pdf)
- [NACo legislative analysis](https://www.naco.org/resource/naco-legislative-analysis-build-america-250-act); [NLC](https://www.nlc.org/article/2026/05/20/congress-next-transportation-bill-builds-toward-local-priorities/); [AMPO summary](https://ampo.org/wp-content/uploads/2026/06/BA250_AMPO_SUMMARY_SLIDEDECK.pdf); [NACTO and Climate Mayors letter](https://nacto.org/latest/letter-build-america-250-needs-stronger-support-for-cities-say-mayors-and-city-transportation-officials/)
- [Eno Center webinar slides](https://enotrans.org/wp-content/uploads/2026/05/BUILD-America-250-webinar-slides.pdf)
- T4America: [ten things to know](https://t4america.org/2026/05/22/ten-things-to-know-about-the-build-acts-failure-to-produce-better-outcomes/) and [fix-it-first](https://t4america.org/2026/07/14/fix-it-first-was-common-sense-in-2020-invest-act-now-congress-calls-it-radical/); [Taxpayers for Common Sense, Repair Priorities 2026](https://www.taxpayer.net/wp-content/uploads/2026/04/Repair-Priorities-2026_4.29.pdf)
- [GHSA](https://www.ghsa.org/news/BUILD_for_Americas_250); [UCS](https://blog.ucs.org/?p=97411); [SELC](https://www.selc.org/?p=42456); [The Trucker on the 91,000-lb pilot](https://www.thetrucker.com/trucking-news/truckload-authority/the-build-america-250-act-growing-momentum-for-higher-truck-weight-limits)

**Conditions, costs and delivery:**

- [FHWA Conditions and Performance, 25th edition](https://www.fhwa.dot.gov/policy/25cpr)
- [TRB Special Report 329, Renewing the National Commitment to the Interstate Highway System](https://nap.nationalacademies.org/26472)
- [ARTBA 2025 bridge report](https://artbabridgereport.org/reports/2025-ARTBA-Bridge-Report.pdf)
- NHTSA early estimates: [2024](https://crashstats.nhtsa.dot.gov/Api/Public/ViewPublication/813800), [2025](https://crashstats.nhtsa.dot.gov/Api/Public/ViewPublication/813829)
- [GAO-25-107166 on IIJA funding and grant agreements](https://files.gao.gov/reports/GAO-25-107166/index.html)
- [BTS, IIJA buying power](https://www.bts.gov/sites/bts.dot.gov/files/2026-07/IIJA%20Buying%20Power.pdf)
- [Atlas Public Policy, NEVI status, July 2026](https://atlaspolicy.com/wp-content/uploads/2026/07/NEVI-Status-Update-Fact-Sheet.pdf)
- [Mineta Transportation Institute, What Do Americans Think About Federal Tax Options to Support Transportation? (2024)](https://transweb.sjsu.edu/node/4576)
