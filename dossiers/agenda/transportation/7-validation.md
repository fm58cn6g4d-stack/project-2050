# Transportation: validation

Role: section 7 of the transportation dossier: the decided design checked against outside figures, what the models miss, how it lands with the rest of the plan and for whom, the strongest objections and the signs of failure. Status: draft (stage C, step 7, PR 3), on `DEC-2026-11-10-08`. Model figures are the plan's own (grade D).

Outcomes checked: OUT-05 (emissions and a prepared country), OUT-11 (the fiscal and fairness tests) and OUT-12, the transportation outcome added with the decision (safe, affordable travel).

## 1. Against outside figures

| Check | The plan | Outside figure | Verdict |
| --- | --- | --- | --- |
| The trust fund gap the plan must fill | Top-ups of $209.74B and $57.33B for FY2032-36, plus new revenue from FY2030 [EV-MOV-200] | CBO: cumulative shortfalls of $86.0B (highway) and $45.2B (transit) by the end of FY2031 under current law, more under H.R. 8870 [EV-MOV-015] | **Holds.** The plan fills the gap with revenue first, and the 2028 extension's transfer covers FY2029-31. The transfer is not yet sized (section 6) |
| Highway and bridge repair | Repair-first rules, the Interstate and Bridge Renewal program at $30.77B over FY2032-36 [EV-MOV-212] | FHWA: $151.1B a year from all governments for all cost-beneficial work, against $115.1B spent [EV-MOV-005] | **Partly.** The plan narrows the gap but does not close it; most of the gap is state and local |
| The Interstate | Interstate and Bridge Renewal, $30.77B over FY2032-36, its new money ramping up from zero [EV-MOV-212] | National Academies: $45-70B a year of combined spending needed, against $20-25B [EV-MOV-010] | **Short.** The plan's new money is a fraction of the gap. Memo 3's option B (start at full size in FY2032) is the settlement's lever |
| Transit repair | A 20-year schedule that retires the backlog | Conditions and Performance: $20.3B a year needed to reach good repair, against $13.5B spent; backlog $101B in 2018 [EV-MOV-104], $127.8B in 2025 dollars [EV-MOV-105] | **Holds on 2018 data.** The backlog has not been re-estimated since; a new count could be higher |
| Transit operations | $6.0B rising to $8.0B a year, 11.9% of national net operating cost in its first year [EV-MOV-220] | From 2019 to 2025, in nominal dollars: fares down $4.1B and operating expenses up $19.4B, so net operating cost (expenses less fares) up about $23.5B [EV-MOV-100]. The federal share of operating cost rose from 8% to 17% with pandemic relief [EV-MOV-103]; on about $70B of expenses, the nine points now ending are roughly $6B a year. All by this dossier's arithmetic | **Partly.** The tier exceeds the national fare loss and about replaces the expiring relief, but it covers only about a quarter of the growth in net operating cost. It is apportioned by service, trips and low-income residents, so it will not match each system's gap |
| Passenger rail readiness | $254.03B, with gates and a reserve [EV-MOV-222] | Three to five corridors with a finished environmental record by 2031, by the legacy design's own count [EV-MOV-225]; FRA staff down 22% and every corridor under review [EV-MOV-109] | **At risk.** Money will wait at the gates. The design accepts that and caps the damage, but early years may obligate far less than authorized |
| Charging | The Charging Gap Program, $2.63B of formula money [EV-MOV-216] | NEVI obligated about $526 million in its first years before suspension [EV-MOV-014] | **Untested.** The auction method has no federal track record (section 8) |
| Per-mile charges | Odometer-only, 10% collection ceiling | Utah projects 14.2% of revenue at small scale [EV-MOV-120]; Oregon staff expect high early costs [EV-MOV-118] | **At risk in early years.** At national scale costs should fall; GAO's review is the check |

## 2. What the models miss

- **Demand response.**
  - The transportation model has none, so higher fuel taxes and the premium are assumed not to reduce driving or speed the shift to electric cars [EV-MOV-206]. Both effects would lower receipts, which makes the steps' and the premium's revenue upper bounds. The legacy design put the steps' effect at probably 2-3% of fuel receipts [EV-MOV-228]; a trust-fund cash-flow model and a CBO score are both needed before the acts are scored.
  - It also misses the other side: induced demand from new lanes [EV-MOV-114], which the lower federal share for new lanes addresses only in part.
- **Construction cost.**
  - Program levels are nominal and not re-indexed (A-5, kept as a working choice). Construction costs rose 63% from FY2021 to FY2025 [EV-MOV-008] and fell back only part way after 2024 [EV-MOV-132].
  - A repeat would buy less repair than planned. Section 8 makes it a trigger.
- **The baseline.** The model assumes H.R. 8870 or an equivalent funds FY2027-31 at about current levels. Under the lapse case (`3-design.md`, case 3), FY2029-31 program levels and the transfer change.
- **CBO scoring.** The model approximates CBO's basis (the 25% offset); it is not a CBO score. Each act needs its own score before enactment.
- **GDP.** The model's GDP path is backed out of the legacy rail design's 2026 figure and grown at 4.1%, not taken from CBO's baseline. Shares of GDP are approximate to a few thousandths of a point.

## 3. How it lands with the rest of the plan

- **Housing.** HOU-6's zoning reward keeps a condition on new transportation money (`dossiers/home/3-design.md`, memo 4). Section 4 places it on the 2031 bill's new and incremental money only, never on the renewal base, transit operations or safety (MOV-31.91, a working choice). Housing owns its terms.
- **Clean power (OUT-05).** The clean-vehicle charge must not undercut the shift to electric cars. At a 40-mpg rate an electric car pays $141 a year in FY2036 against $225 for a 25-mpg gas car [EV-MOV-204] [EV-MOV-201], and never pays the premium. The climate model should read the charge as a small cost per mile, not a penalty.
- **Fair financing (D3).**
  - For a 25-mpg car driven 12,000 miles, federal fuel tax rises from $88 to $225 a year by FY2036 [EV-MOV-201]. That is an added $137, or about 0.3% of a $40,000 income and 0.1% of a $100,000 income, by this dossier's arithmetic.
  - After FY2036 it keeps rising, with indexing and the decided fossil premium (phased in over FY2040-44): about $317 a year in FY2040, $406 in FY2044 and $427 in FY2046 in nominal dollars [EV-MOV-229]. In 2029 dollars that is about $189 in FY2036, $242 in FY2040 and $280 from FY2044 on. These are the plan's model (`Revenue.gr(t)` in `moving_america.py`, deflated at the model's 2.5% inflation; run November 10, 2026; grade D), and they hold the car's 12,000 miles fixed, since the model has no demand response [EV-MOV-206]. A clean car pays $221 in FY2046 and never pays the premium [EV-MOV-229].
  - The household model does not yet carry fuel taxes; the settlement should add them before it runs the fairness test.
- **The secure floor.** Lower-income households spend a larger share on transportation [EV-MOV-013]. The fuel-tax steps are where the plan asks most of them in this dossier. No transportation benefit offsets it directly, so the floor and the settlement have to.

## 4. Reach: for whom

- **People without a car.** Transit's operating tier and the service floor reach them most. The count of households without a car is not in the register; Census ACS table B08201 would supply it.
- **Rural places.** Formula money reaches rural roads through states, and the Charging Gap Program reserves 30% for rural sites. The rail program's regional commissions let places without a willing state DOT sponsor corridors.
- **Pedestrians and local streets.** They gain from the Safe System changes (the planning share and proven countermeasures [EV-MOV-126] [EV-MOV-127]). Local governments own about three-quarters of road miles [EV-MOV-012], and the higher local suballocation (60%) moves money toward them.
- **Riders who depend on paratransit.** Disabled riders using ADA complementary paratransit are not named in memo 4, and paratransit is the fastest-growing and costliest service per trip for many agencies. The service floor counts vehicle revenue hours, so an agency could meet it while cutting fixed-route coverage, which shrinks the paratransit service area tied to it. No new condition is added (the design lens); FTA's published report adds each area's paratransit trips and service area, so a shrinking area shows (MOV-31.40). Paratransit's share of operating cost is something to study in implementation, from the NTD.
- **Tribal nations.** Section 4 provides for them: a 3% tribal set-aside in the bridge formula program (MOV-31.21), the federal lands and tribal programs carried in sec. 1101 (MOV-31.20), tribal transit within the rural formula (5311, MOV-31.46), and tribal governments exempt from the clean-vehicle charge (MOV-29.03). Section 1 has no tribal road or safety figure; no choice turns on one now.
- **Truckers and small carriers.** They pay by weight and miles. Owner-operators of the heaviest interstate trucks pay most, on the IFTA records they already file; intrastate carriers report once a year (section 5).

## 5. Objections answered

1. **"Gas taxes hit working families hardest."**
   - True of any fuel tax. The steps are small (3 cents a year), pause when prices spike, and pay for repair that drivers already pay for in vehicle damage.
   - Polls show 74-75% support when the money is dedicated to maintenance [EV-MOV-129] [EV-MOV-134].
   - The fairness test is run plan-wide.
2. **"A per-mile charge means tracking where I drive."** It doesn't: the charge reads the odometer only, readings are tax return information from the first day, and the 2031 bill bars location data and destroys readings after three years (division A sec. 111).
3. **"Trucking already pays its share."** The heavy-vehicle use tax is flat at $550 and unindexed since 1984 [EV-MOV-209]. A weight-distance charge prices the damage, as Oregon's does [EV-MOV-121].
4. **"Federal money for transit operations rewards waste."**
   - The tier pays a capped share (no area above 25% of net cost).
   - It requires states and cities to keep their own support, and it publishes cost per service hour every year (memo 4).
   - The pre-1998 experience is the legacy design's argument, not an evaluation in the register.
5. **"High-speed rail is a boondoggle."**
   - European lines show the risk: overruns and some lines with too few riders [EV-MOV-130].
   - The design pays by stage, after independent review, caps any one corridor at $14B and requires committed local money [EV-MOV-224].
6. **"Washington shouldn't tell states how to spend highway money."** The decided design (memo 5, B) asks states to publish, not to obtain approval. The one financial lever is a lower federal share for new lanes, and the evidence that new lanes fill with new traffic supports it [EV-MOV-114] [EV-MOV-115].
7. **"Just pay for roads from the general fund."** Indexing alone would raise the general-fund draw from 0.180% to 0.267% of GDP [EV-MOV-203], with users paying a shrinking share of what they use.

## 6. Signs of failure

- **Collection.** The clean-vehicle or weight-distance charge costs more than 10% to collect two years after start (GAO's review).
- **Pauses.** Price pauses defer three or more steps. The $25B backstop is drawn and exhausted (three pauses delay about $53.3B [EV-MOV-219]), and the remaining shortfall falls on expansion programs under sec. 108(c)(2).
- **Transit service.** Areas covering more than a fifth of riders fall below the service floor.
- **Rail.** Less than half of Tier 1 money is obligated by FY2034.
- **Repair.** Poor-condition pavement or bridge shares rise for two years in more than ten states despite the repair reports.
- **Costs.** Construction costs rise more than 20% faster than general inflation over three years.

Section 8 turns these into triggers with reviews.

## Questions for Espen

None new. The open items are for the settlement and the budget model:
- the household fuel-tax burden;
- the FY2040 booking.
