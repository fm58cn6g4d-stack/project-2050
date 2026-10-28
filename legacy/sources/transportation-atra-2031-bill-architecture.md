# American Transit Renewal Act of 2031 — Full Bill Architecture

> **Filed Oct 20, 2026** from the Surface Transportation claude.ai Project (ATRA doc, artifact 6eded0d5). Project paths are rewritten to their repo locations; the model scripts are in `index/tools/transportation/`. Where this file differs from `domains/transportation-moving-america-act-2031-draft-2.md` (Draft 2, canonical for MOV-), Draft 2 governs.


Oct 4, 2026 · @espen

**Calendar and name, decided October 12.** This Act is now division C of the Moving America Act of 2031. The 2031 bill covers FY2032-36, and BUILD America 250-Plus runs through FY2031. The canonical authorization table and the fiscal chart are restated. Other figures in this document reading FY2031-35 are superseded by `sources/transportation-calendar-fy2032-36.md` in the project, and by the fiscal model run with `BILL_START = 2032`. The program amounts are unchanged in nominal terms, one year later. The headline differences:

- **The draw:** FY2032-36 averages 0.174% (peak 0.177%), not 0.185%.
- **CBO basis:** 0.193-0.203% in FY2032-36, under the benchmark.
- **The FY2031 cliff:** 250-Plus's last year is a cliff that the 2030 reconciliation package should bridge.
- **The 250-Plus transfer:** stays at $108.0B through FY2030; nothing in 250-Plus is sized to the later program.

## What changed from the handoff

Twelve premises in the prompt and the split framework did not survive verification, and four of them change the architecture rather than the wording.

| # | The handoff said | This version does | Why |
| --- | --- | --- | --- |
| 1 | The Highway Trust Fund goes insolvent in FY2028 | Treats FY2027 as transit's cliff and FY2028 as the highway account's | CBO's June 2026 baseline exhausts the transit account during FY2027, with a $2.9B shortfall by year-end; CBO's September 30 estimate of H.R. 8870 puts it at $3.1B, rising to $48.2B by the end of FY2031. The highway account follows in FY2028. Transit goes over first |
| 2 | A repair backlog "in the neighborhood of $180B" | Sizes the amortization schedule on $127.8B | DOT's 25th Conditions and Performance report puts the backlog at $127.8B in 2025 dollars, on 2018 data. It reaches $180B only in nominal dollars around 2039 |
| 3 | Transit takes 60% of a $279.6B combined envelope, $167.8B | Builds a dollar floor of $224.42B and reports the split as an outcome | The bottom-up floor is $189.42B before any operating tier. The envelope cannot hold a transit floor and ARCA at once: together they are 1.56 times it at the House bill's highway levels |
| 4 | The section 5307 operating bar is the hinge of the package | Amends 5307, and treats 26 U.S.C. 9503(e)(3) as the real hinge | The bar is already porous: preventive maintenance has counted as capital since 1998, and the federal share of operating cost was 17% in 2024. The Mass Transit Account itself is limited by the tax code to "capital or capital related expenditures" |
| 5 | SEC. 101(d) makes transit the beneficiary of the rail account | Writes transit's share into SEC. 101 | As drafted, 101(d) floors the transit account at about $7.5B in FY2031, rising to about $10B in FY2041-45. By FY2041-45 rail is 105% covered by dedicated revenue, highways 75% and transit 16% |
| 6 | ARCA fits under the 0.192% rule at 0.099% of GDP in FY2031-35 | Re-runs the rule with all three modes in it | Counting highways, baseline transit and rail together, ARCA alone runs at 0.130% on the base case. The 0.099% row reproduces only by leaving highway and transit general-fund appropriations out of a test whose cap counts them |
| 7 | The cap is 0.192% of GDP | Uses 0.206% for an all-in test | The 0.192% leaves out $4.3B of annual general-fund appropriations that existed in FY2026. A test that counts them on one side must count them on the other |
| 8 | A 2.4 cent per-mile fee replaces all current trust fund revenue, about $44B | Keeps the anchor, flags it | Checked, and the anchor is wrong. FHWA counts 3.32 trillion vehicle-miles in 2025, so 2.4 cents grosses about $80B. That matches trust fund outlays, not receipts; receipts are replaced at about 1.4 cents. ARCA's revenue rows are built on the $44B figure and understate the fee's yield by about 40% |
| 9 | The 2026 bill is conventional, "nothing structural" for transit | Builds on what H.R. 8870 actually does | It opens operating eligibility three ways (a state block grant, a 125-bus rule, security costs), drops the Low-No and rail vehicle replacement programs, and conditions formula money on fare-evasion penalties |
| 10 | The FY2028 revenue bill creates the rail account | Plans 2028 as a defensive patch | The Secretary's July 22, 2026 letter to the Senate committees recommends eliminating the Mass Transit Account outright |
| 11 | Operating gaps and repair backlog are separate claims | Treats them as one | Agencies are closing operating gaps with capital money: SEPTA with $394M of state capital funds, Pittsburgh with $44.8M, Pennsylvania by flexing $153M of federal highway funds. A closed bar converts an operating gap into backlog |
| 12 | Section 5337's formula is sound as written | Repairs a stale cross-reference | 5337(c) and (d) still apportion "the amount authorized or made available under section 5338(a)(2)(K)". IIJA moved that money to subparagraph (L) |

The diagnosis in the split framework survives: transit's claim is a flow and rail's is a stock, and the floor should be written in dollars. What does not survive is the idea that a parity share can discipline the two packages. The binding constraint is the general-fund rule, and it binds.

## The real baseline

Federal transit money in FY2026 is $14.642B of contract authority plus about $3.3B for Capital Investment Grants, and the trust fund account behind the first number collects $5.7B a year against $17B of outlays.

### What current law provides

| Program | Section | FY2026 | Instrument |
| --- | --- | --- | --- |
| Urbanized area formula | 5307 | $7.026B | Contract authority, Mass Transit Account |
| State of good repair | 5337 | $3.850B, of which $300M competitive railcar replacement | Contract authority |
| Buses and bus facilities | 5339 | $1.153B | Contract authority |
| Rural area formula | 5311 | $0.960B | Contract authority |
| Growing and high-density states | 5340 | $0.812B | Contract authority |
| Seniors and people with disabilities | 5310 | $0.407B | Contract authority |
| Planning, research, administration, other | 5305, 5312, 5314, 5334, 5335 | $0.434B | Contract authority |
| **Total, 5338(a)** |  | **$14.642B** |  |
| Capital Investment Grants | 5309 | $3.0B authorized; $1.6B advance appropriation plus annual appropriations | General fund |

IIJA authorized and appropriated $108B over FY2022-26, about $21.6B a year: 65% contract authority, 20% advance appropriations and 16% subject to appropriation. The advance appropriations lapsed on September 30, 2026. ([CRS R48644](https://www.congress.gov/crs-product/R48644); 49 U.S.C. 5338)

### The account behind it

The Mass Transit Account receives 2.86 cents of each gallon taxed under 26 U.S.C. 9503(e)(2). CBO projects receipts of $5.7B in FY2027 plus $1.2B flexed from the highway account, against outlays of $18.1B. The gap is $10.7B a year over FY2027-31 and the cumulative shortfall reaches $96.5B by FY2036. Congress has transferred $60.3B of general revenue into the account since 2008, $28B of it in IIJA. The authority to deposit the taxes at all expires October 1, 2028. ([CBO, June 2026 baseline](https://www.cbo.gov/system/files/2026-06/51300-2026-06-highwaytrustfund.pdf); 26 U.S.C. 9503(b), (e), (f))

### Operating money, and what the relief acts changed

The three COVID relief acts provided $69.5B: $25B in the CARES Act, $14B in the December 2020 appropriations act and $30.5B in the American Rescue Plan. They were available for operating costs in every urbanized area, the broadest operating eligibility large systems have had since FY1998.

The effect shows in the shares. The federal government covered 8% of transit operating cost in 2019 and 17% in 2024. Fare revenue fell from $20.2B to $11.8B over the same years in 2025 dollars, and ridership in late 2025 stood at 81% of its 2019 level. The relief money is spent. The fare gap of $8.4B a year is not.

### The statutory map

I read each of these in the current U.S. Code rather than relying on the list in the prompt.

| Provision | What it says | Where the package touches it |
| --- | --- | --- |
| 49 U.S.C. 5307(a)(1)(D) | Operating grants in urbanized areas under 200,000 | Unchanged |
| 5307(a)(2)-(3) | In areas of 200,000 or more: operating grants only for systems with 100 or fewer peak buses, "excluding rail fixed guideway", capped at 75% or 50% of the attributable apportionment | Title II replaces the bus-count test with a service operating tier |
| 5307(d)(2) | Operating grants "may not exceed 50 percent of the net project cost" | Kept for the new tier |
| 5302(4)(E) | "Preventive maintenance" is a capital project | Kept, with a ceiling tied to prior use |
| 5309(l)(1)(B)(ii) | A full funding grant agreement may not carry more than 60% from section 5309 | Title IV |
| 5309(q) | Joint public transportation and intercity passenger rail projects are already eligible, for the transit share of cost | Title VI and the ARCA crosswalk |
| 5326 | Asset management plans, targets and reports. No consequence for missing a target | Title III adds one |
| 5337(c)-(d) | Formula for repair money; cross-reference to 5338(a)(2)(K) is stale | Title III |
| 5333(b) | Labor protective arrangements are a condition of assistance under 5307-5312, 5337 and 5338(b) | Applies to the new tier without amendment |
| 5323(j)(2)(C) | Rolling stock: more than 70% domestic content and final assembly in the United States | Title VII and the crosswalk |
| 26 U.S.C. 9503(e)(3) | Account available "for making capital or capital related expenditures" | Title I strikes the limitation |

Not read in this pass: 5303-5305, 5310, 5311, 5324, 5329, 5339, 5340 and the CFR parts. The package's amendments to those are described, not drafted.

## The December 2026 compromise: BUILD America 250-Plus

The transit title of the assumed lame-duck deal authorizes $102.8B over FY2027-31 and delivers about $99.8B, or $20.0B a year. That is 8% below IIJA in nominal dollars and 18% below it in real terms. This section constructs the deal the same way the ARCA document does; it is a forecast, not enacted law.

| Line | H.R. 8870 as reported | 250-Plus, FY2027-31 | Of which guaranteed | Delivered |
| --- | --- | --- | --- | --- |
| Mass Transit Account contract authority | $87.6B | $87.6B | $87.6B | $87.6B |
| Capital Investment Grants | $15.0B, subject to appropriation | $15.0B | $5.0B | $12.0B |
| WMATA grants | $0.15B in FY2031, subject to appropriation | $0.15B | none | $0.15B |
| **Total** | **$102.8B** | **$102.8B** | **$92.6B (90%)** | **$99.8B** |

The contract authority runs $16.9B, $17.2B, $17.5B, $17.8B and $18.2B by year, $87.6B in all. I assume Senate Democrats buy a $5B guarantee for Capital Investment Grants with the same capital they spend on the rail guarantee, and that the remaining $10B is appropriated at the 70% rate ARCA applies to competitive programs. [[WMATA's $150M is for FY2031 only, per CBO's September 30 estimate. (Mass Transit, June 2, 2026; CBO cost estimates, summer and September 30, 2026](https://www.masstransitmag.com/management/article/55381249/house-ti-committee-approves-build-america-250-act-for-surface-transportation-reauthorization)](https://www.cbo.gov/publication/62817))

Transit's position differs from rail's in one respect that matters for everything after. Rail's baseline is 30% guaranteed. Transit's is 90% guaranteed, because formula money rides on contract authority. The guarantee is only as good as the account, and the account is empty in FY2027.

### What the House bill already does

- **Operating eligibility, three ways.** Systems running 101 to 125 peak buses may use up to 25% of their apportionment for operations (section 3005). A voluntary state block grant makes formula money "broadly eligible", operating costs included, outside areas above 3.5 million people (section 3006). Up to 1.5% of formula funds may pay for security operations (section 3012).
- **Capital Investment Grants.** Small Starts become "Streamlined Starts" with a $1B cost ceiling and a $500M federal ceiling. Projects need 30% design before entering project development. The expedited-delivery pilot's federal share rises from 25% to 40% (section 3007).
- **Repair.** The state of good repair program averages $4.7B a year, up from $4.3B, and loses its $300M competitive railcar replacement program (section 3022).
- **Buses.** No dedicated Low-No funding. From FY2029 the federal share is capped against a five-year average bus price, falling to 70% by FY2031 (section 3013).
- **Conditions.** From FY2028 the Secretary withholds 10% of urbanized formula funds where fare evasion is not an offense. At least 3% of formula funds go to accessibility and $400M a year to All Stations Accessibility.
- **Rail flex.** States may use a portion of highway formula dollars for rail equipment, stations and state-supported routes. This is the highway-flex-to-rail provision I would otherwise have proposed adding.

### What I would add to this vehicle, and nothing more

Three provisions are small enough to ride a bipartisan bill and each sets up a later title.

1. **A reporting line for capital money used on operations.** Each recipient reports annually the amount of federal and state capital funds applied to operating costs or preventive maintenance. It costs nothing and creates the record Title III depends on.
2. **A general-fund transfer sized to** CBO's shortfall. CBO's September 30 estimate of the bill puts the transit account's cumulative shortfall at $36.8B by the end of FY2030 and $48.2B by FY2031, and the highway account's at $71.2B and $99.5B. A transfer of $108.0B to both accounts through FY2030 carries the guarantee to the 2031 bill without counting on per-mile receipts that do not yet exist, and reconciliation cannot make one later. A transit-only transfer leaves the highway account dry in FY2028, which is the quickest way to lose the highway votes the deal needs.
3. **Restoring the 5337(f) railcar replacement program.** Its repeal saves $1.5B and lands on the oldest fleets. This is the trade most likely to be available for the fare-evasion condition.

### What it does not do

No operating program for the systems that carry most riders. No schedule for the repair backlog. No revenue: the electric-vehicle fee in section 1129 runs through FY2036 and is not credited to the trust fund; CBO counts it as general revenue, $16.8B gross and $12.4B net. No fix for an account that runs dry in the bill's first year.

## The 2027-28 positioning window

Nothing passes in this window, and the job is to keep the Mass Transit Account alive through September 30, 2028 while building the record for 2029. The window is defensive first and preparatory second.

### The forcing event, read from transit's side

ARCA treats the 2028 expiration of the fuel taxes as the moment a rail account gets created. From the transit account's side the same date is a threat. The administration's stated position is to eliminate the account and send its 2.86 cents to highways, and a Democratic House facing a Republican president cannot enact a per-mile fee in 2028.

The realistic 2028 outcome is a two-year extension of the existing taxes with a general-fund patch. That is what Congress has done at every prior deadline. So the three demands for 2028 are narrow:

1. **Extend 26 U.S.C. 9503(b) and (e) as they are.** No change to the 2.86 cents and no merger of the accounts.
2. **Size the patch to both accounts' contract authority through FY2030.** On CBO's baseline that is about $61B for highways and $35B for transit.
3. **Commission the per-mile fee's design.** A Treasury and DOT report on collection, privacy and rural incidence, due in 2029, so the reconciliation bill legislates against a study instead of a slogan.

The revenue structure and the new accounts move in the 2029-30 reconciliation, where a revenue measure needs 51 votes and where ARCA already places its aviation fee and rail diesel tax. ARCA's document has the rail account created in both places. This one puts it in reconciliation.

### What the window produces

| Product | Committee | What it sets up |
| --- | --- | --- |
| Transit Operating Stability Act (marker bill) | House T\&I; Senate Banking | The Title II service operating tier, with its conditions already drafted and scored |
| Transit Asset Renewal Act (marker bill) | House T\&I; Senate Banking | The Title III amortization schedule and the section 5326 consequence |
| Surface Transportation Trust Fund Act (marker bill) | Ways and Means; Finance | Title I's three accounts and the incremental-share rule |
| CBO request: per-mile fee at 0.6, 0.8 and 1.0 cents | Budget; Finance | A score for the one number the fiscal test is most sensitive to |
| GAO request: capital funds applied to operations since 2020 | T\&I; Banking | The evidence that a closed operating bar becomes repair backlog |
| GAO request: FTA staffing against Capital Investment Grant workload | Appropriations | FTA fell from 781 staff in FY2024 to 552 in FY2026; the pipeline behind it holds 47 projects |
| Hearings: the 2027 exhaustion of the transit account | T\&I; Banking | A record that the December 2026 transfer was undersized, if it was |

Senate jurisdiction is the detail that shapes all of this. Transit is the Banking Committee's, not Commerce's or EPW's, so a transit title and a rail title reach the same bill through different rooms. The marker bills should be introduced as a pair with ARCA's so the conference sees one passenger package.

## The 2029-30 reconciliation window

Reconciliation can carry $32.0B of transit money and the whole revenue structure, and transit is a better fit for it than rail. Transit's largest needs are fast-spending: operating grants outlay within the year and repair money within three or four.

### The Byrd test, applied to transit

| Instrument | Status | Why |
| --- | --- | --- |
| Mandatory general-fund grants "to carry out section 5307" or 5337 | Available | Direct spending. The American Rescue Plan put $30.5B into transit this way in 2021 |
| Operating eligibility on that money | Available | A term or condition "under which mandatory outlays are made", attached to the new money only |
| Maintenance-of-effort and service conditions on the same money | Available | Same reasoning |
| Per-mile fee, electric-vehicle fee, indexed fuel taxes deposited to the trust fund | Available | Revenue provisions; the 1990 reconciliation is the precedent |
| Creating the accounts and setting their shares of receipts | Available, with care | It directs where receipts are credited. It should travel inside the revenue title, not as a freestanding provision |
| Striking "capital or capital related" from 26 U.S.C. 9503(e)(3) | Doubtful | No budgetary effect of its own. It belongs in the 2031 bill; reconciliation works around it by using general-fund grants |
| General-fund transfer into the transit account | Barred | Intragovernmental transfer |
| New contract authority under an obligation limitation | Barred | Outlays score to appropriations acts |
| Amending 5307, 5309, 5326 or 5337 | Barred | Policy with incidental budgetary effect |
| Capital Investment Grants for projects not yet under agreement | Available with deadlines | Direct spending like any other grant. An obligation deadline and an expenditure deadline on the money keep outlays inside the budget window; without them a slow project spends past it and the provision is exposed. The binding limit is which projects can sign and spend by the deadlines, not the rule |

### The package

| Provision | FY2029 | FY2030 | Total | Why it clears |
| --- | --- | --- | --- | --- |
| Operating transition grants | $4.0B | $5.0B | $9.0B | Outlays within the year. Conditions: state and local operating support held at its three-year average; service hours held at 95% of the base year |
| State of good repair, shovel-ready backlog | $4.0B | $6.0B | $10.0B | Projects already in asset management plans |
| Bus and railcar replacement orders | $3.0B | $1.0B | $4.0B | Firm orders with delivery schedules |
| Station accessibility |  | $3.0B | $3.0B | Small discrete projects |
| Capital Investment Grants, executed agreements only |  | $3.0B | $3.0B | Pays down commitments already scheduled |
| Credit subsidy: transit and joint development | $1.0B | $1.0B | $2.0B | Scores at obligation |
| Workforce and FTA capacity |  | $1.0B | $1.0B | Grants and salaries |
| **Total** | **$12.0B** | **$20.0B** | **$32.0B** |  |

The package is back-loaded on purpose. FY2029-30 is where the general-fund test is tightest, because rail's $48.5B and the trust fund patch land before the per-mile fee has grown. On the base case, with the fee starting at 1.0 cent, the combined draw is 0.194% of GDP across FY2029-30, peaking at 0.197% in FY2030, under the 0.206% benchmark. A 0.6-cent start puts FY2030 at 0.228%.

### What it hands the 2031 bill

- **A funded bridge for operations.** Two years of transition grants carry large systems from the end of state stopgaps to the Title II tier, with the conditions already in force.
- **The revenue fight finished.** The per-mile fee, the indexed fuel taxes and the three accounts exist before the reauthorization is written.
- **A head start on the backlog.** $10B retires about 7% of it before the schedule begins.

One overlap with ARCA needs settling. Rail's reconciliation package carries $3.0B for "station access and ADA backlog", and this one carries $3.0B for station accessibility. They are different stations: Amtrak-served in one, rail transit and commuter rail in the other. The bill text should say so.

## The FY2027-31 baseline, modeled

Seven projects costing more than $1B open by FY2031, and no amount of new money changes that number. The capital pipeline and the operating crisis run on different clocks, and the baseline has to be read on both.

### Where the capital pipeline stands

FTA's dashboard of September 11, 2026 lists 47 projects seeking Capital Investment Grants. Their combined cost is about $78.6B, and the 39 with a stated request seek $28.2B. ([FTA CIG Dashboard](https://www.transit.dot.gov/funding/grants/grant-programs/capital-investments/capital-investment-grant-cig-dashboard))

| Group | Projects | Total cost | CIG requested | Examples |
| --- | --- | --- | --- | --- |
| New Starts and Core Capacity | 17 | $72.2B | $25.5B | BART Silicon Valley Phase II ($12.7B), Southeast Gateway ($10.6B), The Portal ($8.3B), Austin Light Rail ($8.2B) |
| Small Starts | 30 | $6.4B | $2.7B | Bus rapid transit in Columbus, Raleigh, Cincinnati, Portland, Atlanta |
| Under construction with a signed agreement | 8 | $45.8B | $12.3B | Second Avenue Subway Phase 2, Red Line Extension, Purple Line |
| Outside the federal pipeline | 9 | $98.3B | none yet | Sepulveda, Interborough Express, Ballard and West Seattle, Baltimore Red Line, Link21 |

The last two groups are from my own knowledge of sponsor plans at mid-2026 and were not re-verified in this pass. Costs for the fourth group are sponsor estimates and soft.

Three facts shape what follows. The four largest pipeline projects hold $17.7B of the $28.2B requested, so the program's five-year appropriation is spoken for by a handful of grants. None of the 17 larger projects reports its non-federal match as committed. And FTA has lost 29% of its staff since FY2024, which bears hardest on exactly this program.

### Three phases, FY2027-31

| Phase | Period | What governs |
| --- | --- | --- |
| Lame-duck enactment | December 2026 | 250-Plus passes. Contract authority flows; Capital Investment Grants get $5B guaranteed |
| Divided government | FY2027-28 | Formula money moves because it must. Discretionary grants slow: the dashboard's estimated grant dates slip one to two years in this model |
| Restoration | FY2029-31 | Reconciliation money and a re-staffed FTA clear the grant queue. This is when the 2027-dated agreements actually sign |

### What opens by FY2031, and why it does not move

| Measure | End FY2028 | End FY2031 | End FY2036 |
| --- | --- | --- | --- |
| Projects in service, of 64 tracked | 3 | 39 | 53 |
| Of which over $1B | 3 | 7 | 16 |
| Projects under construction | 32 | 15 | 10 |

The seven large openings are the Purple Line, the D Line subway sections, the Minneapolis Green and Blue Line extensions, the Red Line Extension in Chicago, Honolulu's final segment and FrontRunner's double-tracking. Five of the seven hold agreements signed before this package exists. East San Fernando Valley light rail follows in December 2031, which is FY2032.

Moving every pipeline grant two years earlier raises total openings by FY2031 from 40 to 45. All five additions are bus rapid transit lines under $400M. The count of large projects stays at eight. Money cannot shorten a tunnel that is already being bored, which is the same finding as the rail corridor grid and for the same reason.

### The systems, on a faster clock

| System | The gap | How it is being covered | Until |
| --- | --- | --- | --- |
| MTA New York | Reported $160M, $243M and $306M for 2027-29; $700M a year of one-time money ends in 2029 | One-time reimbursements and fees | 2028 |
| SEPTA | $213M structural | $394M of state capital funds applied to operations | FY2027 |
| Pittsburgh Regional Transit | $100M-plus | $44.8M of capital funds, $15.4M of reserves | FY2027 |
| BART | $350-400M a year | Regional sales tax on the November 2026 ballot | Unresolved |
| SFMTA | $307M, growing to $430M by 2030 | Same measure | Unresolved |
| NJ Transit | Not stated; $3.5B budget | $765.6M corporate transit fee, $302M state subsidy | Fee-dependent |
| Chicago (CTA, Metra, Pace) | $202M to $730M, depending on the estimate | $1.5B state package, October 2025 | Resolved |
| WMATA | Capital, not operating | $460M a year of new regional capital funding from FY2028 | Resolved if enacted |
| TriMet, Cleveland, Milwaukee | Service cuts announced or pending | Cuts and county stopgaps | Unresolved |

Sources: [Citizens Budget Commission](https://cbcny.org/research/mta-operating-budget-outlook-short-term-stability-long-term-risks), [SSTI](https://ssti.us/2025/11/11/transit-agencies-are-averting-the-fiscal-cliff-but-still-need-long-term-funding-solutions/), [WESA](https://www.wesanews.org/development-transportation/2026-05-29/pittsburgh-regional-transit-budget-no-fare-hikes-service-cuts), [Mercury News](https://www.mercurynews.com/2026/09/20/the-bay-area-faces-a-transit-reckoning-will-voters-pay-to-keep-it-running/), [SFMTA](https://www.sfmta.com/bridging-our-budget-gap-save-muni), [New Jersey Monitor](https://newjerseymonitor.com/2026/07/16/nj-transit-approves-3-5-billion-budget/), [DMVMoves](https://dmvmoves.org/cog-and-metro-boards-endorse-plan-to-provide-460m-to-modernize-metro-transform-regional-transit/). The Bay Area, Pittsburgh and New Jersey figures are from search excerpts, not full reads.

The list in the prompt needs two corrections. Chicago and Washington have largely been handled by their states. The unresolved cases are Pennsylvania's two systems and the Bay Area. And the two systems covering operations with capital funds are the clearest evidence for Title III: their gap will reappear as backlog.

## What the baseline leaves undone

Costing the work bottom-up gives a federal need of about $817B over FY2031-45 and a five-year program of $224.42B. Three-quarters of the five-year figure is renewal, and none of the renewal can be deferred without a service consequence.

| Category | Federal need, FY2031-45 | The Act, FY2031-35 | Basis |
| --- | --- | --- | --- |
| Urbanized formula, capital | \~$196B | $54.10B | About $9.3B in FY2031 under 250-Plus (my apportionment of its contract authority), raised to $10.0B and grown 3.9% a year |
| State of good repair formula | \~$101B | $28.00B | The $4.7B a year in H.R. 8870, grown; covers normal replacement |
| Backlog retirement | \~$108B | $31.53B | $127.8B backlog in 2025 dollars retired over 20 years; federal share 80% of each year's installment |
| Service operating assistance | \~$135B | $35.00B | $6.0B in FY2031, which holds the federal share of operating cost near its 2024 level of 17% |
| Capital Investment Grants | \~$110B | $27.50B | $28.2B already requested, plus about 45% of $98.3B in projects not yet in the pipeline |
| Buses and bus facilities | \~$50B | $14.00B | $2.0B a year in H.R. 8870, plus the zero-emission increment it dropped |
| Rural, tribal, seniors and disabilities | \~$38B | $10.70B | H.R. 8870 levels plus an 80% operating share in rural areas |
| Station accessibility | \~$17B | $5.00B | $400M a year in H.R. 8870, raised to $1.0B with a completion date |
| Joint transit-rail facilities | \~$18B | $6.00B | Transit's share of the terminals ARCA funds in section 310 |
| Workforce, resilience, ferries, relief, planning, FTA | \~$44B | $12.59B | Itemized in the authorization table |
| **Total** | **\~$817B** | **$224.42B** |  |

### Is the repair number right?

DOT's report gives three ways to clear the backlog over twenty years. Each needs $23.7B to $25.6B a year of preservation spending in 2025 dollars, against $17.0B actually spent. The difference is $6.7B to $8.6B a year from all levels of government. The schedule here supplies $6.4B a year in 2025 dollars, of which the federal share is $5.1B. It is at the low end of DOT's range because I size it on the backlog alone and leave normal replacement to the formula.

The backlog figure rests on 2018 data. I hold it flat in real terms to FY2031, which is roughly what DOT's sustain-current-spending scenario shows. If the operating crisis has pushed it higher, the schedule is light.

### How it compares

| Comparison | Annual rate | The Act as a multiple |
| --- | --- | --- |
| 250-Plus, delivered | $20.0B | 2.2x |
| IIJA, nominal | $21.6B | 2.1x |
| IIJA, in FY2031 dollars | \~$25.7B | 1.7x |
| Stronger Communities Through Better Transit Act, operating only | $20.0B | The Act's operating tier is 35% of it |

The honest multiple is 1.7. Of the increase over IIJA in real terms, more than a third is the operating tier and a third is backlog retirement. The Act is a renewal bill with an expansion program attached, which is the opposite of ARCA's shape and the reason the two do not compete for the same kind of dollar.

## The Act at a glance

The American Transit Renewal Act is a seven-title, $224.42B five-year authorization enacted as the public transportation title of the 2031 surface transportation reauthorization. It is preceded by $32.0B of mandatory appropriations in the 2029-30 reconciliation packages, which makes the federal commitment across FY2029-35 $256.42B.

| Title | Subject | FY2031-35 |
| --- | --- | --- |
| I | Surface Transportation Trust Fund: three accounts, shares of new revenue, the renewal-first rule, the general-fund rule | revenue title, shared with ARCA |
| II | Service operating assistance | $35.00B |
| III | State of good repair: formula, backlog retirement schedule, asset management enforcement, resilience | $63.03B |
| IV | Capital Investment Grants | $27.50B |
| V | Labor and workforce | $2.85B |
| VI | Formula capital, buses, rural, accessibility, joint facilities, ferries, emergency relief | $91.30B |
| VII | Delivery, cost discipline, FTA capacity, planning and research | $4.74B |
|  | **Total** | **$224.42B** |
|  | Preceding it: 2029-30 reconciliation | $32.00B |

By year the authorization runs $40.70B, $42.89B, $45.09B, $47.04B and $48.70B.

### Two kinds of money, on purpose

**Renewal, $190.92B.** Everything a system needs to keep running what it has: formula capital, repair, the operating tier, buses, rural service, accessibility. It is contract authority from the Mass Transit Account and has first call on dedicated revenue.

**Expansion, $33.50B.** Capital Investment Grants and joint facilities. It is a mandatory general-fund appropriation, sits outside the trust fund, and is the first thing reduced if the general-fund rule is breached.

This is the flow-and-stock distinction from the split framework, moved from between the modes to inside each of them. Rail has renewal too, and transit has expansion.

### The guarantee, stated precisely

**Contract authority for renewal.** It survives a stopgap, as transit formula money always has. What changes is the account behind it, which Title I refills with a share of new revenue.

**Continuation at the final-year level.** If the FY2036 reauthorization fails, renewal contract authority continues at its FY2035 amount, indexed. CBO's baseline already assumes this of expiring contract authority, so the provision makes law of a scoring convention.

**Mandatory money for expansion, with full obligation at signing.** A full funding grant agreement obligates the whole federal share when it is executed. Today 49 U.S.C. 5338(d)(2) makes a general-fund grant an obligation "only to the extent that amounts are appropriated", which is why a project sponsor carries appropriations risk for a decade.

**A solvency trigger that protects renewal.** If the account's projected balance falls short, expansion is reduced first and renewal last. ARCA's section 108 reduces everything proportionally.

## The fiscal envelope, and the trust fund architecture

Rebased October 12 on two corrections, and the answer holds with room to spare. The per-mile fee is now priced on vehicle-miles, not on ARCA's anchor, and highways are carried at the levels in H.R. 8870 rather than ARCA's flat FY2026 figure. On that base ARCA and this Act together draw 0.194% of GDP in FY2029-30 and 0.185% in FY2031-35, under the 0.206% cap in every year, if the fee starts at 1.0 cent. A 0.6-cent start still breaches the cap, now because of the higher highway levels rather than a thin fee. Everything here comes from `transit_fiscal_model.py`; nothing is computed by hand.

Checked October 12 against CBO's September 30 estimate of H.R. 8870. The model's current-law trust fund receipts match CBO's to the decimal ($49.1B in FY2029), the EV fee runs on CBO's collections, WMATA's grant is $150M in FY2031 only, and NHTSA and FMCSA, about $2.2B a year from the Highway Account, are now in the highway line. The 0.206% cap is this project's benchmark, not a CBO or statutory limit: it restates ARCA's own rule, the FY2026 general-fund draw on surface programs, and it counts transfers. Exceeding it is a choice, not a violation. The figure that binds in practice is CBO's score, which nets new excise receipts by about a quarter for lost income and payroll taxes: 0.204% to 0.214% in FY2031-35 and 0.219% in FY2030. The reconciliation instructions have to be sized to that.

### The parity envelope cannot hold both packages

| Operating scenario | Transit, FY2031-35 | Rail (ARCA) | Combined | Multiple of the $306.1B envelope | Split, transit / rail |
| --- | --- | --- | --- | --- | --- |
| A: bar kept | $189.42B | $254.03B | $443.45B | 1.45x | 43 / 57 |
| B: conditional tier (the drafted bill) | $224.42B | $254.03B | $478.45B | 1.56x | 47 / 53 |
| C: broad eligibility | $259.42B | $254.03B | $513.45B | 1.68x | 51 / 49 |

The envelope is 75% of highway funding, and at H.R. 8870's highway levels it is $306.1B over FY2031-35. The split framework hoped a need-based transit floor would land near 60% of it, $183.6B. It lands at $189.42B before any operating money. If rail were the residual inside the envelope, rail would receive $81.6B and ARCA would be 3.1 times its share. That is not a ratio anyone can defend, so the ratio is the wrong instrument.

Rail plus transit already exceeds highway funding in this plan: 1.17 times in FY2031-35, 1.05 in FY2036-40 and 1.08 in FY2041-45. Parity by 2045 is met fourteen years early. As a target it constrains nothing.

### The rule that does bind

ARCA's discipline rule holds the combined general-fund draw to its IIJA-era peak, 0.192% of GDP. Two adjustments make it a fair test of three modes at once. The cap rises to 0.206%, because the 0.192% omits $4.3B of annual appropriations that the FY2026 program also drew. And the draw counts every program against every dedicated dollar: highways, transit and rail, baseline and new.

| Base case: fee from 1.0 cent on vehicle-miles, House highway levels | FY2029-30 | FY2031-35 | FY2036-40 | FY2041-45 |
| --- | --- | --- | --- | --- |
| ARCA alone, transit at its baseline | 0.149% | 0.130% | 0.072% | 0.068% |
| ARCA plus the Act, scenario A | 0.194% | 0.169% | 0.113% | 0.109% |
| ARCA plus the Act, scenario B | 0.194% | 0.185% | 0.130% | 0.127% |
| ARCA plus the Act, scenario C | 0.194% | 0.202% | 0.148% | 0.144% |

Period averages; the cap is 0.206%. Scenario B peaks at 0.197% in FY2030 and 0.189% in FY2033. The room left under the cap is $3.1B in FY2030 and $6.9B to $11.2B a year in FY2031-35. ARCA's own table reports 0.105% and 0.099% for the first two periods; the model reproduces those figures by ARCA's method, which leaves out the general-fund appropriations its cap counts (see the verification pass).

Two inputs decide the result, and they pull in opposite directions. Pricing the fee on vehicle-miles adds about $10B a year in FY2031-35. Carrying highways at the House bill's levels takes about $8B a year back. The table shows scenario B under each pairing.

| Scenario B, peak year | Fee from 0.6 cents | Fee from 0.8 cents | Fee from 1.0 cent |
| --- | --- | --- | --- |
| Vehicle-miles yield, House highway levels (base case) | 0.228%, over | 0.213%, over | 0.197% |
| Vehicle-miles yield, ARCA's highway levels | 0.209%, over | 0.193% | 0.178% |
| ARCA's yield anchor, House highway levels | 0.250%, over | 0.240%, over | 0.230%, over |
| ARCA's yield anchor, ARCA's highway levels | 0.230%, over | 0.220%, over | 0.211%, over |

Starting the fee at 1.0 cent in FY2029 and stepping 0.2 cents a year reaches 3.6 cents in FY2042 instead of FY2044, and the fuel taxes are displaced over the same fourteen years. The extra 0.4 cents is about $48 a year for a vehicle driven 12,000 miles. A 0.8-cent start misses by $2.7B over FY2029-30.

&#91;embedded content: transit\_fiscal\_model.py, architecture C, scenario B · FY2027-45 · all-in accounting\]

The tightest years are FY2029-30, when both reconciliation packages land before the fee has grown. After FY2035 the draw falls to about 0.13% of GDP and stays there.

### Three architectures

Total general-fund need is the same under any account structure. What the structure decides is which mode holds dedicated money and which lives on annual appropriations.

| Share of each program covered by dedicated revenue, FY2041-45 | Highways | Transit | Rail |
| --- | --- | --- | --- |
| A. Standalone rail trust fund, as ARCA first drafted it | 100% | 28% | 33% |
| B. Rail account at 8% rising to 28% of the fund, as ARCA's SEC. 101 now reads | 75% | 16% | 105% |
| C. Floors, then shares of new revenue: 35% highways, 50% transit, 15% rail | 74% | 58% | 50% |

Scenario B, base case. Architecture A strands $4.1B of highway-account surplus over FY2041-45. Architecture B makes intercity rail the only self-financing mode in the federal program, on road-user money, while the transit account that carries eight billion trips a year is 16% funded. That is not a structure a transit caucus votes for, and SEC. 101(d) does not prevent it.

### Four choices

**Choice 1. One fund, three accounts, and a renewal-first rule inside each.** The Mass Transit Account keeps its name. Dedicated revenue pays for renewal before expansion in every account.

**Choice 2. Shares are written on new revenue only.** Each existing account keeps its FY2028 receipts, indexed. Receipts above those floors divide 35% to highways, 50% to transit and 15% to rail. The percentages come from a rule: they bring the three renewal programs toward the same coverage ratio, and each reauthorization resets them by that rule. The model's unrounded answer for scenario B is 34 / 54 / 12. The drafted shares give highways one point, because drivers pay the fee, and rail three, because rail's coverage is lowest in the 2030s. On renewal programs alone they reach 74% for highways, 69% for transit and 78% for rail in FY2041-45. The transit gap is left as drafted: the EV fee and its place in the system are due for a larger redesign, which will move these numbers more than a point of share would. The earlier 30 / 50 / 20 gave rail 87% while highways sat at 71%.

**Choice 3. General-fund money stays out of the fund.** Expansion programs in both bills are mandatory general-fund appropriations, capped by the rule. ARCA's $132B transfer into a rail trust fund disappears as a transfer. The same dollars appear as direct spending for sections 303, 310, 311 and 312, which is reconciliation-eligible within the budget window and honest about what a user-fee fund is.

**Choice 4. The fee starts at a cent, and the rule has an order of operations.** If the draw is projected above 0.206%, the Secretary reduces expansion obligations in both bills proportionally, never renewal. On the base case the trigger fires in no year. It is insurance against the revenue risks below: on the 0.6-cent schedule it would take $14.3B out of FY2029-30 and $8.9B out of FY2031-35. The room it leaves is large enough to release ARCA's $25B readiness reserve over FY2031-35 and still keep $1.9B to $6.2B a year under the cap.

### What breaks this

- **Who pays the fee.** The base case charges every vehicle. A light-duty-only fee raises scenario B's peak to 0.209% in FY2030 and 0.205% in FY2031-35: over the cap in FY2030 and at it after.
- **Collection cost.** I take 10% off the gross. At the 13% top of ARCA's range the peaks are 0.201% and 0.193%. A light-duty-only fee at 13% is over it, 0.212% in FY2030.
- **Highway levels.** The base case carries H.R. 8870's $72.9B to $77.6B a year, FY2027-31: a $372.4B obligation limitation plus about $3.2B of exempt funds, as introduced. Growth after FY2031 is 2.5% a year.
- **Fuel-tax displacement.** I assume the fee replaces the fuel taxes linearly as it ramps up. On ARCA's yield and schedule that reproduces ARCA's rail revenue rows within 4% from FY2031, and 9% in FY2029-30.
- **Vehicle-miles.** The base grows 0.5% a year from FHWA's 3.32 trillion in 2025. A flat base costs about $3B a year by FY2035.

## Title I — Surface Transportation Trust Fund

Title I is one title shared by both bills. It replaces the two SEC. 101 texts now sitting in the ARCA document with a single fund, three accounts and a rule for dividing new revenue. It would be reported by Ways and Means and Finance and merged in conference, as ARCA already plans for its revenue title.

### Section-by-section

| Section | Provision | Change from ARCA as drafted |
| --- | --- | --- |
| 101 | Fund, accounts, base amounts, shares of new revenue, renewal-first rule | Replaces the 8 / 15 / 22 / 28% rail share of all receipts with 35 / 50 / 15 shares of new receipts |
| 102 | Per-mile fee: 1.0 cent in FY2029, plus 0.2 cents a year to 3.6 cents in FY2042 | Starts 0.4 cents higher and finishes two years sooner |
| 103 | Fuel taxes retained and indexed; electric-vehicle fee at $130 and $35, rising $5 a year to $200 | Unchanged |
| 104 | Aviation segment surcharge and rail diesel tax, credited to the rail account | Unchanged; kept out of the three-way split because they are rail-specific |
| 105 | General-fund programs: mandatory appropriations for expansion in both bills | Replaces ARCA's general-fund transfer into the fund |
| 106 | Contract authority and contingent commitments | Extended to the transit account; the readiness reserve becomes subject to section 108 |
| 107 | Continuation of renewal authority absent reauthorization | Replaces the $12B rail-only floor with continuation of each account's renewal programs at FY2035 levels |
| 108 | Solvency and general-fund discipline: expansion reduced first | Replaces proportional reduction; the trigger moves from 0.2% to 0.206% measured all-in |
| 109 | Joint facilities | Replaces the bar on using rail money for chapter 53 purposes |

### Drafted text: sections 101, 108 and 109

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
  (1) 35 percent shall be credited to the Highway Account;
  (2) 50 percent shall be credited to the Mass Transit Account; and
  (3) 15 percent shall be credited to the Intercity Passenger Rail Account.

(e) RAIL-SPECIFIC RECEIPTS.—Taxes received under sections 4283 and
4041(a)(1)(C)(iii) shall be credited to the Intercity Passenger Rail Account
and shall not be taken into account under subsection (c) or (d).

(f) RENEWAL FIRST.—Amounts in an account shall be available for the
expansion programs of that account only to the extent they exceed the amounts
made available for that fiscal year for its renewal programs. For purposes of
this Act—
  (1) the renewal programs of the Mass Transit Account are those under
  sections 5305, 5307, 5310, 5311, 5312, 5314, 5324, 5326, 5329, 5337, 5339
  and 5340 of title 49, United States Code;
  (2) the renewal programs of the Intercity Passenger Rail Account are those
  under titles II, IV through VII and X of the American Rail Competitiveness
  Act and sections 302, 304, 305 and 306 of that Act; and
  (3) the expansion programs are those under section 5309 of title 49,
  section 606 of this Act, and sections 303, 310, 311 and 312 of the American
  Rail Competitiveness Act.

(g) MASS TRANSIT ACCOUNT EXPENDITURES.—Section 9503(e)(3) of such Code is
amended by striking "capital or capital related expenditures (including
capital expenditures for new projects)" and inserting "expenditures
authorized under chapter 53 of title 49, United States Code".

(h) RESETTING THE SHARES.—Not later than 18 months before the expiration of
each authorization, the Secretary of the Treasury and the Secretary of
Transportation shall report to the Committees the percentages under
subsection (d) that would result in dedicated receipts covering an equal
share of the renewal programs of each account over the following 10 fiscal
years.

SEC. 108. SOLVENCY AND GENERAL FUND DISCIPLINE.

(a) REPORT.—The Secretary and the Director of the Congressional Budget
Office shall jointly report each year the amount by which obligations for
all programs of the three accounts and for programs under section 105 are
projected to exceed receipts credited to the Fund, as a percentage of gross
domestic product.

(b) TRIGGER.—If that percentage is projected to exceed 0.206 percent for a
fiscal year, the Secretary shall reduce amounts available for obligation for
that fiscal year for the expansion programs described in section 101(f)(3),
in proportion to the amounts otherwise available for each, by the amount of
the excess.

(c) RENEWAL PROTECTED.—No reduction under this section or by reason of a
projected shortfall in an account shall be made to a renewal program until
amounts available for the expansion programs of that account have been
reduced to zero.

(d) EXECUTED AGREEMENTS.—A reduction under this section shall not apply to
an amount obligated under a full funding grant agreement or a contingent
commitment executed before the date of the report.

SEC. 109. JOINT FACILITIES.

Amounts in the Mass Transit Account and the Intercity Passenger Rail Account
may be obligated for a facility used by both public transportation and
intercity passenger rail transportation, each in proportion to—
  (1) for the rehabilitation or replacement of an existing facility, the
  share of train movements at the facility in the most recent fiscal year
  made by the services that account supports; and
  (2) for an expansion of the capacity of a facility, the share of the
  additional train movements the project is projected to make possible
  that will be made by those services,
as determined by the Secretary using the method of section 5309(q)(4) of
title 49, United States Code.
```

Section numbers in the Internal Revenue Code are carried from ARCA's draft and would be conformed by the Finance Committee.

Three drafting points carry the weight. Subsection 101(c) replaces ARCA's 101(d): it is the same protection for the two existing accounts, stated as a credit that comes first instead of a floor that is checked afterwards. Subsection 101(g) is the amendment the operating tier cannot work without. And 108(d) is what lets a contractor believe an executed agreement: the trigger falls on unobligated expansion money, never on a signed commitment.

### What the shares produce

| Dedicated revenue as a share of each program, scenario B, base case | Highways | Transit | Rail |
| --- | --- | --- | --- |
| FY2029-30 | 71% | 62% | 13% |
| FY2031-35 | 75% | 63% | 26% |
| FY2036-40 | 78% | 65% | 47% |
| FY2041-45 | 77% | 60% | 50% |

No account reaches 100%. That is the honest result of accounts that collect about $141B a year in FY2041-45, rail-specific taxes included, against $220B of programs. The gaps are mostly expansion, which the bills fund from the general fund on purpose: on renewal programs alone coverage is 74% for highways, 69% for transit and 78% for rail. ARCA's claim that rail becomes fully self-financing by FY2041-45 was true only because rail took 28% of a fund whose other two accounts were short.

## Title II — Operating assistance ($35.00B)

Title II opens federal operating assistance to large urbanized areas, permanently, as a separate formula tier with four conditions. It costs $6.0B in FY2031 rising to $8.0B, and it is the largest operating program the general-fund rule tolerates alongside ARCA.

### The answer to the design question

| Option | Verdict | Why |
| --- | --- | --- |
| Keep the bar | No | It has not kept federal money out of operations. It has routed that money through preventive maintenance and, lately, through capital funds diverted to payroll |
| Lift the bar inside the existing formula | No | Every operating dollar would come out of a capital apportionment. That is the outcome the bar's authors feared, and they were right to |
| Time-limited relief | No, except as the 2029-30 bridge | The fare gap is structural: $8.4B a year in 2025 dollars, six years after the pandemic |
| A fare-recovery or ridership condition | No | It pays most to the systems that need least and cuts aid as ridership falls, which is when service cuts do the most damage |
| **A separate formula tier with maintenance of effort, a service floor and an asset condition** | **Yes** | New money that cannot erode capital, cannot replace state and local support, and cannot be collected while assets decay |

### Drafted text: section 201

```
SEC. 201. SERVICE OPERATING ASSISTANCE.

(a) IN GENERAL.—Section 5307 of title 49, United States Code, is amended by
adding at the end the following:

  "(i) SERVICE OPERATING ASSISTANCE.—
    "(1) GRANTS.—The Secretary shall make grants under this subsection to
    designated recipients in urbanized areas with a population of not fewer
    than 200,000 individuals to finance the operating costs of equipment and
    facilities for use in public transportation, including rail fixed
    guideway public transportation.
    "(2) APPORTIONMENT.—Amounts made available under section 5338(a)(2)(P)
    shall be apportioned among such urbanized areas as follows:
      "(A) 50 percent in the ratio of vehicle revenue hours;
      "(B) 30 percent in the ratio of unlinked passenger trips; and
      "(C) 20 percent in the ratio of low-income individuals residing in
      the urbanized area,
    except that no urbanized area shall be apportioned more than 25 percent
    of the operating costs of public transportation in the area, less fare
    revenues, in the most recent year for which data are reported under
    section 5335, and any amount not apportioned by reason of that limit
    shall be apportioned among the other urbanized areas under this
    paragraph.
    "(3) GOVERNMENT SHARE.—Subsection (d)(2) applies to a grant under this
    subsection.
    "(4) CONDITIONS.—A recipient may receive a grant under this subsection
    for a fiscal year only if the recipient certifies, and the Secretary
    accepts, that—
      "(A) the aggregate amount of State and local financial support for
      the operating costs of public transportation in the urbanized area,
      other than revenues from providing public transportation, will be not
      less than the average of such support for the 3 preceding fiscal
      years, increased by the percentage change in the Consumer Price Index
      for All Urban Consumers;
      "(B) vehicle revenue hours will be not less than 95 percent of the
      average for fiscal years 2028 through 2030;
      "(C) the recipient is not subject to a direction under section
      5326(e)(3); and
      "(D) the share of amounts apportioned under subsection (a)(1) and
      section 5337 that the recipient applies to preventive maintenance
      will not exceed the average share so applied in fiscal years 2027
      through 2029.
    "(5) COST REVIEW.—A recipient whose operating cost per vehicle revenue
    hour has increased, over 3 consecutive fiscal years, at an annual rate
    more than 1.5 percentage points above the Employment Cost Index for
    State and local government workers shall submit to the Secretary, and
    publish, a plan identifying the causes. Operating costs in excess of
    that rate shall not be included in net project cost for the following
    fiscal year unless the Secretary finds the increase attributable to an
    expansion of service.
    "(6) ELECTION.—A public transportation system eligible under subsection
    (a)(2) may receive assistance under that subsection or this one, but
    not both, for a fiscal year.
    "(7) PUBLICATION.—The Secretary shall publish annually, for each
    recipient, the amounts under paragraph (4)(A), the vehicle revenue hours
    under paragraph (4)(B), and operating cost per vehicle revenue hour by
    mode.".

(b) AUTHORIZATION.—Section 5338(a)(2) of such title is amended by adding at
the end the following:
  "(P) $6,000,000,000 for fiscal year 2031, $6,500,000,000 for fiscal year
  2032, $7,000,000,000 for fiscal year 2033, $7,500,000,000 for fiscal year
  2034, and $8,000,000,000 for fiscal year 2035 shall be available to carry
  out section 5307(i);".
```

The existing 100-bus rule in 5307(a)(2) stays. Small operators in large areas keep the flexibility they have, and H.R. 8870's 125-bus extension is carried.

### What each condition is for

- **Maintenance of effort, (4)(A).** The standing objection to federal operating aid is that states withdraw a dollar for each one that arrives. The text borrows its form from 49 U.S.C. 5323(e)(2), which already conditions bond-proceeds match on a three-year look-back.
- **Service floor, (4)(B).** The grant buys service, so it lapses if service is cut. The base years are before the tier exists, so it cannot be gamed by cutting first.
- **Asset condition, (4)(C) and (D).** A recipient under a Title III direction is ineligible, and the preventive maintenance share is frozen. Operating aid cannot be stacked on top of capital diversion.
- **Cost review, (5).** This answers the 1970s record directly. The benchmark is a wage index plus 1.5 points, so market wage growth is not penalized and growth beyond it is.

### The counterargument, taken seriously

The bar was not an accident. Federal operating aid in the 1970s and early 1980s coincided with rising unit costs, mostly wages and benefits, and with service extended onto weak routes. Charles Lave's 1994 account of declining transit productivity is the standard citation, and CRS repeats it in 2026. TEA-21 ended large-area operating aid in FY1998 and widened the definition of capital to soften the change.

Two things have changed since. The bar has been tested for 28 years, and it did not hold: the federal share of operating cost doubled to 17% by 2024, and agencies are now paying operators out of capital funds. And the tier here is not the 1970s program. That program had no maintenance of effort, no service floor and no cost benchmark. If the conditions fail, the evidence will be in the paragraph (7) publication within three years, and the FY2036 reauthorization can act on it.

### What it does to the split

The tier moves the FY2031-35 split from 43 / 57 to 47 / 53 and adds $7B a year to the general-fund test. On the base case even doubling it, as scenario C does, reaches the cap, 0.206% in FY2033, and uses all of the margin that protects against revenue risk. The drafted size stays at $6.0B rising to $8.0B.

### Where the money goes

I ran paragraph (2) against the 2024 National Transit Database and the Census Bureau's 2019-23 poverty counts for the 183 urbanized areas of 200,000 or more. Each reporting agency is assigned to its primary urbanized area, which is an approximation; FTA splits multi-area reporters. Net operating cost is operating expense less fares, $50.6B nationally in 2024.

| Urbanized area, FY2031 at $6.0B | Apportionment | Share of the tier | Share of national net operating cost | Apportionment as share of the area's net operating cost |
| --- | --- | --- | --- | --- |
| New York--Jersey City--Newark | $1,662M | 27.7% | 27.7% | 11.9% |
| Los Angeles--Long Beach--Anaheim | $394M | 6.6% | 7.5% | 10.4% |
| Chicago | $316M | 5.3% | 5.8% | 10.8% |
| Washington--Arlington | $249M | 4.1% | 6.3% | 7.8% |
| San Francisco--Oakland | $196M | 3.3% | 5.5% | 7.1% |
| Philadelphia | $181M | 3.0% | 2.9% | 12.4% |
| Boston | $163M | 2.7% | 3.6% | 8.9% |
| Miami--Fort Lauderdale | $154M | 2.6% | 2.0% | 15.0% |
| Seattle--Tacoma | $140M | 2.3% | 4.0% | 7.0% |
| Houston | $123M | 2.0% | 1.6% | 15.6% |

The tier pays about 11.9% of net operating cost nationally. New York receives exactly its share of national net operating cost, so the ridership factor is not the windfall the Senate fight assumes. The nine areas over five million people take 54.5% of the tier against 56.6% of net cost. The 138 areas under one million take 14.9% against 10.0%, which is what the low-income factor is for.

The run changed the text. As first drafted, paragraph (2) guaranteed each State's areas 0.5% of the tier. That floor moved $344M a year to 18 States, and it would have paid Boise $30M against a reported net operating cost of $1M and Nashua $30M against $4M. Money a recipient cannot match at 50% is money it cannot spend. The floor is replaced by a ceiling: no area receives more than 25% of its net operating cost, with the excess reapportioned. The ceiling binds in 69 areas, all of them small, and costs New York nothing.

$6.0B is anchored on a share, not on a sum of agency gaps, because the gaps move every budget season. The run supports the anchor: transit's fare revenue in these areas fell $4.9B between 2019 and 2024 in nominal dollars, and the tier replaces about that much. The run's code and data are in the project as `transit_apportionment.py`.

## Title III — State of good repair ($63.03B)

Title III puts the repair backlog on a twenty-year schedule and gives section 5326 its first consequence. A legislated schedule is the right instrument, because the backlog is the one transit need with a published number, a published asset list and no deadline.

| Section | Program | FY2031-35 | Federal share |
| --- | --- | --- | --- |
| 301 | State of good repair formula, including $300M a year of restored railcar replacement grants | $28.00B | 80% |
| 302 | Backlog retirement schedule | $31.53B | 80% |
| 303 | Asset management enforcement and FTA capacity | $0.50B | 100% |
| 304 | Transit resilience | $3.00B | 80% |

### The schedule

| Fiscal year | Installment, all sources | Federal share | Backlog remaining, 2025 dollars |
| --- | --- | --- | --- |
| 2031 | $7.41B | $5.93B | $121.4B |
| 2035 | $8.18B | $6.54B | $95.8B |
| 2040 | $9.25B | $7.40B | $63.9B |
| 2045 | $10.47B | $8.38B | $32.0B |
| 2050 | $11.85B | $9.48B | zero |

Each installment is one-twentieth of $127.8B, indexed. The authorization for section 302 is set slightly above the federal share in each year, $6.00B against $5.93B in FY2031, to cover assets that enter the backlog after the baseline is struck.

Twenty years is DOT's own horizon. A shorter period would outrun the supply chain: railcar and signal work is constrained by a handful of suppliers, and the reconciliation package already advances $10B of it.

### Drafted text: sections 301 to 303

```
SEC. 301. STATE OF GOOD REPAIR FORMULA.

Section 5337 of title 49, United States Code, is amended—
  (1) in subsections (c)(1) and (d)(2), by striking "section
  5338(a)(2)(K)" and inserting "section 5338(a)(2)(L)"; and
  (2) by restoring subsection (f), as in effect on September 30, 2026.

SEC. 302. BACKLOG RETIREMENT SCHEDULE.

Section 5337 of such title is further amended by adding at the end:

  "(g) BACKLOG RETIREMENT.—
    "(1) BASELINE.—Not later than 1 year after the date of enactment of
    this subsection, the Secretary shall publish, for each recipient, the
    cost in constant dollars of replacing or rehabilitating the capital
    assets of the recipient that were not in a state of good repair on
    September 30, 2030, as shown in the transit asset management plan of
    the recipient (in this subsection referred to as the 'baseline
    backlog').
    "(2) APPORTIONMENT.—Amounts made available under section 5338(a)(2)(Q)
    shall be apportioned among recipients in the ratio of their baseline
    backlogs.
    "(3) INSTALLMENT.—In each of the 20 fiscal years beginning with fiscal
    year 2031, a recipient shall obligate, from all sources, for assets in
    its baseline backlog an amount not less than one-twentieth of its
    baseline backlog, adjusted for inflation.
    "(4) USE.—Amounts apportioned under this subsection may be used only
    for assets in the baseline backlog and may not be used for preventive
    maintenance.
    "(5) MAINTENANCE OF EFFORT.—A recipient may receive an apportionment
    under this subsection only if State and local financial support for
    capital projects of the recipient will be not less than the average
    for the 3 preceding fiscal years.
    "(6) GOVERNMENT SHARE.—Subsection (e) applies.
    "(7) REPORT.—The Secretary shall publish annually, for each recipient,
    the baseline backlog remaining.".

SEC. 303. ASSET MANAGEMENT ACCOUNTABILITY.

Section 5326 of such title is amended by adding at the end:

  "(e) ACCOUNTABILITY.—
    "(1) DETERMINATION.—The Secretary shall determine each fiscal year, for
    each recipient operating a fixed guideway, whether the cost in constant
    dollars of the recipient's assets not in a state of good repair
    increased during the preceding fiscal year.
    "(2) PLAN.—A recipient for which the Secretary makes that determination
    for 2 consecutive fiscal years shall submit and publish, within 180
    days, a corrective investment plan.
    "(3) DIRECTION.—If the Secretary makes that determination for a third
    consecutive fiscal year, the Secretary shall direct that not less than
    25 percent of the amounts apportioned to the recipient under section
    5307(a)(1) be obligated only for projects in the investment
    prioritization of the recipient's transit asset management plan, until
    the Secretary determines that the cost described in paragraph (1) has
    decreased for a fiscal year.
    "(4) NO REDUCTION.—Nothing in this subsection authorizes the Secretary
    to withhold or reduce an apportionment.
    "(5) CAPITAL FUNDS APPLIED TO OPERATIONS.—Each recipient shall report
    annually, and the Secretary shall publish, the amount of Federal, State
    and local capital funds applied to operating costs or to preventive
    maintenance.".
```

### Why the consequence is a direction and not a penalty

Withholding money from an agency that is deferring maintenance makes it defer more. Paragraph (3) redirects the agency's own apportionment toward its own priority list and takes nothing away. Paragraph (4) says so in terms, because the 2026 House bill and the Secretary's July letter both reach for withholding as the tool of first resort.

The direction also links to Title II. An agency under direction loses eligibility for the operating tier, so the two titles close on each other: operating aid is available to agencies that keep their assets, and the repair schedule is funded for agencies that keep their local effort.

### What the schedule cannot see

The baseline is each agency's own asset management plan. Those plans vary in quality, and an agency with a thin inventory reports a small backlog. Section 303's $0.50B pays for FTA to audit baselines before the first apportionment. The Northeast Corridor's commuter-territory assets are a second gap: they sit in both this backlog and the NEC Commission's, and section 109 is where that double claim gets settled.

## Title IV — Capital Investment Grants ($27.50B)

Title IV changes what a grant agreement is worth more than it changes how projects are rated. The throttle on new fixed-guideway capacity is that a sponsor signs for a decade of construction against money Congress appropriates one year at a time.

### What changes

| Section | Provision | Current law |
| --- | --- | --- |
| 401(a) | $27.50B of mandatory appropriations over five years, available until expended | $3.0B a year authorized, subject to appropriation (5338(b)) |
| 401(b) | A full funding grant agreement obligates the whole federal share at signing | A general-fund grant binds the government "only to the extent that amounts are appropriated" (5338(d)(2)) |
| 402 | Warrants become the default: a project seeking 50% or less from section 5309 is justified by published thresholds, without a bespoke rating | Warrants "to the maximum extent practicable" (5309(g)(3)) |
| 403 | Local financial commitment is stated in ARCA's five match categories, A through E, with categories C and D capped at 40% | "Stable and dependable" sources, judged case by case |
| 404 | FTA decides engineering entry, letters of no prejudice and grant agreements within 120 days of a complete submission, or publishes why not | No clock |
| 405 | Projects with a federal share above $1B take ARCA's tranche gates and its cure and termination rules | None |
| 406 | Joint projects under 5309(q) file one application and one finance plan with ARCA's section 302 or 303 | Two programs, two reviews |
| 407 | Projects over $1B report standardized unit costs and take an independent cost review at 30% design | None |

Carried from H.R. 8870 without change: Streamlined Starts up to $1B, 30% design before project development, the transit-oriented development rating credit, guidance updated every two years.

Not changed: the 60% ceiling on the section 5309 share in 5309(l)(1)(B)(ii). The dashboard shows sponsors requesting 40% to 49% on the largest projects. Raising the ceiling would buy fewer projects with the same money, and the pipeline already asks for more than the program holds.

### Drafted text: section 401

```
SEC. 401. CAPITAL INVESTMENT GRANTS.

(a) APPROPRIATION.—Out of any money in the Treasury not otherwise
appropriated, there is appropriated to carry out section 5309 of title 49,
United States Code, to remain available until expended—
  (1) $4,500,000,000 for fiscal year 2031;
  (2) $5,000,000,000 for fiscal year 2032;
  (3) $5,500,000,000 for fiscal year 2033;
  (4) $6,000,000,000 for fiscal year 2034; and
  (5) $6,500,000,000 for fiscal year 2035.

(b) FULL OBLIGATION.—Section 5338(d)(2) of such title is amended to read as
follows:
  "(2) GRANTS FINANCED FROM GENERAL FUND.—A full funding grant agreement or
  small start grant agreement financed with amounts appropriated by section
  401(a) of the American Transit Renewal Act of 2031 is a contractual
  obligation of the Government to pay the Government share stated in the
  agreement, and the Secretary shall obligate that share in full on the
  date the agreement is executed.".

(c) CONTINGENT COMMITMENTS.—The total of amounts obligated under subsection
(b) and committed under section 5309(k)(2) of such title for fiscal years
after 2035 may not exceed 60 percent of the amount appropriated for fiscal
year 2035, multiplied by the number of such fiscal years, through fiscal
year 2045.
```

### Why this, and not a new rating system

The rating process is slow, but the dashboard says the binding problem is elsewhere. Of 17 New Starts and Core Capacity projects, 10 already hold ratings of medium or better. None has its match committed, and the largest four are waiting on grant dates in 2027 that depend on appropriations nobody has made. A project that could sign once and build is a different credit than one that returns to Congress every year.

Section 405 matters because it works in both directions. The gates discipline a sponsor whose costs run. ARCA's sections 401(d) through (f) and 407 also bind the department: a decision deadline, a cure period, a published factual basis and judicial review before any termination. The department held payments to the Second Avenue Subway from October 2025 and released them on April 16, 2026, only after the MTA sued. A federal judge ordered about $2B for Chicago's Red Line projects unfrozen in March 2026. Transit megaprojects need the same protection ARCA writes for rail corridors.

### The permitting control test

ARCA's document works through why formula money with State project selection escapes the "predominant federal control" test in the 2026 permitting law and why gated discretionary money does not. Transit sits on both sides of that line.

- **Formula programs ride the carve-out.** Sections 5307, 5337 and the new 5337(g) are apportioned by formula and programmed locally. That covers the entire renewal program, including backlog retirement.
- **Capital Investment Grants do not.** A rated project with a federal grant agreement is federal control by design, and Title IV adds gates that confirm it. These projects take the full two-year review.
- **The right-of-way exemption already covers transit.** MAP-21 section 1316 reaches transit work in existing operational right-of-way. ARCA's section 901 extends it to FRA projects; nothing is needed here.

H.R. 8870 would also let large transit agencies assume responsibility for categorical exclusions. That stays.

## Title V — Labor and workforce ($2.85B)

Title V leaves section 5333(b) exactly as it is and spends $2.85B on the constraint that actually limits service: there are not enough operators and mechanics. The operating tier buys nothing if the vehicles have no drivers.

### Section 5333(b), stated plainly

The labor protective arrangements formerly in section 13(c) are a condition of assistance under sections 5307 through 5312 and 5337. The new operating tier is section 5307(i) and the backlog schedule is section 5337(g), so both are covered without a word of amendment. I have drafted around nothing.

| Question | Answer in this bill |
| --- | --- |
| Does the operating tier need a new Department of Labor certification each year? | No. 5333(b)(4) already provides certification "without referral" for grants that "do not materially revise or amend existing assistance agreements". Section 502 confirms that a recurring formula grant under 5307(i) or 5337(g) qualifies |
| Does the bill require or reward contracting out? | No. Private operators asked the House for a contracting test in grant ratings. It is not here |
| Does the bill restrict contracting out? | No. 5333(b)(5) continues to govern the replacement of one contractor by another |
| Does the maintenance-of-effort rule freeze labor costs? | No. The cost review in 5307(i)(5) is indexed to public-sector wage growth plus 1.5 points |
| What about commuter rail employees? | They bargain under the Railway Labor Act, and 5333(b) arrangements still attach to the grant. ARCA's section 503 carries their agreements through any Amtrak reorganization; section 109 joint facilities should carry the same clause for commuter operators |

### The shortage

APTA reports that 42.7% of the transit workforce is 55 or older, and its survey found 96% of responding agencies short of staff, with operators and mechanics the hardest positions to fill. Both figures come from search excerpts of APTA material that I did not open in full. ([APTA, workforce issues](https://www.apta.com/industry-issues/workforce-issues/))

### What the money does

| Section | Provision | FY2031-35 |
| --- | --- | --- |
| 501 | Registered apprenticeships for bus and rail operators, vehicle mechanics, signal and power maintainers, run jointly by labor and management | $1.60B |
| 503 | Frontline training set-aside: 1% of each recipient's 5307 and 5337 apportionment, matched from this title | $0.75B |
| 504 | Operator safety: enclosed workstations on new buses, as in H.R. 8870 section 3102, plus retrofit grants for the existing fleet | $0.40B |
| 505 | Transit Workforce Development Center, made permanent | $0.10B |

Section 506 carries no money. Before federal funds pay for automated revenue service, FTA must issue minimum safety standards covering operator presence. That is the Transportation Trades Department's position, and it costs less to settle in statute than in a decade of grant-by-grant disputes.

### Where labor and the fiscal design meet

The service floor in Title II is a labor provision in effect. It bars an agency from taking operating money while cutting service hours, which is the same as barring layoffs financed by federal aid. And the renewal-first rule in Title I puts the programs that pay for existing jobs ahead of the programs that build new lines. The unions' interest and the fiscal rule point the same way, which is unusual enough to say.

## Title VI — Formula capital, buses, rural service, accessibility and joint facilities ($91.30B)

Title VI is the base of the program and the part every member's district sees. Most of it extends current formula programs at higher levels; two sections are new.

| Section | Program | FY2031-35 | What changes |
| --- | --- | --- | --- |
| 601 | Urbanized area formula, capital (5307, 5340) | $54.10B | Level only. $10.0B in FY2031 against about $9.3B under 250-Plus |
| 602 | Buses and bus facilities (5339) | $14.00B | Restores a zero-emission increment as a cost share, not a mandate |
| 603 | Rural, tribal and intercity bus (5311) | $7.50B | Rural operating share raised from 50% to 80% |
| 604 | Seniors and people with disabilities (5310) | $3.20B | Level only |
| 605 | All Stations Accessibility | $5.00B | $1.0B a year and a completion date |
| 606 | Joint transit-rail facilities and station access | $6.00B | New |
| 607 | Ferries | $1.00B | H.R. 8870's consolidated program, carried |
| 608 | Emergency relief, quick release (5324) | $0.50B | New standing authorization from the transit account |

### Section 602: buses

H.R. 8870 drops dedicated Low-No funding and, from FY2029, caps the federal share against a five-year average bus price. Three domestic manufacturers remain of the ten that built more than 100 buses a year a decade ago. A price cap on the buyer does not fix a supplier base that thin.

Section 602 keeps propulsion neutral, as the House bill does. It adds a 90% federal share for the incremental cost of a zero-emission bus and its charging equipment over a comparable diesel bus, which pays for the difference without directing the choice. It also authorizes pooled multi-agency orders against a standard specification, the same instrument ARCA's section 1201 uses for railcars.

### Section 605: accessibility with a date

ARCA's section 205 gives Amtrak stations a hard FY2036 accessibility deadline. Section 605 gives legacy rail transit stations FY2045, with an annual list by name of stations not yet accessible. The inventory is large: FTA counted about 965 of 3,447 rail transit stations, 28%, as not accessible in 2021. The costs are larger than the line. CTA puts 42 stations at $2.1B, SEPTA its whole system at $2.4B, and the MTA's settlement commits it to 95% of its inaccessible stations by 2055 at a cost its accessibility chief has put near $35B. $1.0B a year cannot finish the job by FY2045; it is a federal share, matched, and the bill requires FTA to publish a national count and cost within a year so that the FY2036 bill can size the rest.

### Section 606: joint facilities

This is the pressure-relief provision from the split framework, aimed at a better target than station access alone. ARCA's section 310 funds five terminals at $20.20B, and commuter and transit trains are most of the movements at four of them.

| Terminal in ARCA section 310 | ARCA share | Commuter and transit use | Basis |
| --- | --- | --- | --- |
| Chicago Union Station and CREATE | $9.0B | Metra about 130,000 weekday riders against Amtrak's 9,000; 79% of train movements | Station fact sheet, 2019 |
| New York Penn and Sunnyside | $4.0B | Long Island Rail Road and NJ Transit about 92% of riders | Secondary counts; NJ Transit figures conflict |
| Washington Union Station | $3.5B | MARC and VRE about 45,000 weekday riders against Amtrak's 16,500 | Commuter count is a 2008 baseline; unverified share |
| Los Angeles Union Station | $0.7B | Metrolink and Metro rail about 20,000 weekday boardings against Amtrak's 2,900 | Secondary, FY2026 |
| Atlanta | $3.0B | No intercity terminal exists; a relocation study has three downtown sites | Atlanta Regional Commission, November 2025 |

The 30% placeholder was wrong by any measure of use. Commuter trains carry 79% of the movements at Chicago and roughly 85 to 94% of the riders at the four existing terminals. Attributing ARCA's $17.2B of existing-terminal work by average use would put $13B to $15B on the transit account, which turns ARCA's terminal program into a commuter program paid for by transit. The fix is a rule, not a bigger number. SEC. 109 now attributes renewal of an existing facility by each service's share of train movements, and capacity expansion by the train movements each service gains from the project. Intercity-driven expansion stays on the rail account; repair of a commuter-dominated concourse falls mostly on transit. $6.0B stays as a planning figure until the terminal projects are scoped; at that point it should be set project by project.

Section 606 is expansion money: general-fund, outside the trust fund, and first in line under the trigger.

### Section 608: emergency relief

FTA's emergency relief program has no standing money, so transit agencies wait on FEMA after a disaster while highway agencies draw on a trust fund authorization within days. $100M a year from the transit account gives FTA the same quick-release authority.

## Title VII — Delivery, cost discipline and FTA capacity ($4.74B)

Title VII rebuilds the agency that administers everything above and borrows ARCA's cost-discipline sections rather than inventing parallel ones.

| Section | Provision | FY2031-35 |
| --- | --- | --- |
| 701 | Metropolitan and statewide planning (5305) | $1.55B |
| 702 | FTA administration and oversight: restores staffing to at least 800 | $1.05B |
| 703 | Safety oversight (5329) and the National Transit Database | $0.55B |
| 704 | Research, technical assistance and bus testing | $0.80B |
| 705 | Cost benchmarking, standard designs and owner-side engineering capacity | $0.79B |

### Section 702: capacity

FTA had 781 staff in FY2024 and 552 in FY2026, and the FY2027 request is 547. This Act roughly doubles the money the agency moves and adds a backlog baseline to audit, a maintenance-of-effort test to verify and a 120-day clock on grant decisions. None of that works at 552.

### Section 705: cost

American transit construction costs are among the highest in the world. The Transit Costs Project attributes that to overbuilt stations, non-standard design, thin in-house staff and procurement that prices risk onto contractors. ARCA's sections 705 through 709 answer the same findings for rail: a public unit-cost database, reference designs, grants for owner-side engineers, alternative delivery as of right, and utility relocation deadlines.

Section 705 applies those five sections to projects under chapter 53 by cross-reference and funds FTA's part. One database, one set of reference designs for stations and platforms, one utility rule. A transit agency and a state rail authority building in the same city should not face two regimes.

### Buy America, where the two bills collide

| Buyer | Rule | Source |
| --- | --- | --- |
| Transit agency with FTA money | More than 70% domestic content, final assembly in the United States | 49 U.S.C. 5323(j)(2)(C) |
| State or Amtrak with FRA money | 100% of manufactured-product components | 49 U.S.C. 22905(a), as ARCA describes it |
| Amtrak, own purchases | More than 50% domestic content | 49 U.S.C. 24305(f), as ARCA describes it |

ARCA's section 704 moves rail to 75% and its section 1201 says the equipment pool should face one standard. A commuter railcar bought through the pool with both FTA and FRA money would face two. Section 706 sets the pool's standard for any jointly funded order and leaves 5323(j) alone for everything else.

I read 5323(j) in this pass. The two rail provisions are quoted from the ARCA document and were not re-read.

### Sections 711-716: conforming amendments across chapter 53

I read sections 5303, 5304, 5305, 5310, 5311, 5324, 5329, 5338, 5339 and 5340 as they stand in September 2026. Four of them need amendment for the new tiers to work, and two carry stale cross-references from IIJA's renumbering of 5338(a)(2). None of these sections costs money.

```
SEC. 711. PLANNING TARGETS.

(a) METROPOLITAN.—Section 5303(h)(2)(B)(ii) of title 49, United States Code,
is amended by striking "sections 5326(c) and 5329(d)" and inserting
"sections 5307(i)(4), 5326(c), 5329(d), and 5337(g)".

(b) STATEWIDE.—Section 5304(d)(2)(B)(ii) of such title is amended by
striking "sections 5326(c) and 5329(d)" and inserting "sections 5326(c),
5329(d), and 5337(g)".

SEC. 712. RURAL OPERATING SHARE.

Section 5311(g)(2)(A) of such title is amended by striking "50 percent" and
inserting "80 percent".

SEC. 713. EMERGENCIES.

Section 5324 of such title is amended by adding at the end the following:
  "(g) OPERATING ASSISTANCE CONDITIONS.—For a fiscal year in which an
  emergency described in subsection (a)(2) affects an urbanized area, the
  Secretary may waive, for a recipient in that area, the requirements of
  subparagraphs (A) and (B) of section 5307(i)(4), to the extent the
  Secretary finds that the emergency prevents compliance.".

SEC. 714. SAFETY ENFORCEMENT.

Section 5329(g)(2) of such title is amended by adding at the end the
following:
  "(C) OPERATING ASSISTANCE.—The Secretary may withhold amounts apportioned
  under section 5307(i) under paragraph (1)(E) only after requiring the use
  of funds under paragraph (1)(D) for not less than 1 fiscal year.".

SEC. 715. TECHNICAL CORRECTIONS.

(a) Section 5337 of such title is amended in subsections (c)(1) and (d)(2)
by striking "section 5338(a)(2)(K)" each place it appears and inserting
"section 5338(a)(2)(L)".

(b) Section 5339(a)(5) of such title is amended by striking
"section 5338(a)(2)(L)" and inserting "section 5338(a)(2)(M)".

(c) Section 5340(b) of such title is amended by striking
"section 5338(b)(2)(N)" and inserting "section 5338(a)(2)(O)".

SEC. 716. OVERSIGHT.

Section 5338(c)(1)(B) of such title is amended by inserting "(other than
subsection (i))" after "section 5307".
```

Section 711 puts the backlog schedule and the service floor into the performance targets that metropolitan and state plans already track. Section 712 is the rural half of the operating answer: rural systems have always had operating eligibility, at a 50% share that small counties cannot match. Section 713 keeps a hurricane from costing an agency its operating grant through the service floor. Section 714 keeps safety enforcement intact but makes the operating tier the last thing withheld, so a safety finding does not become a service cut. Section 716 keeps FTA's 0.75% oversight takedown off the operating tier, up to $45M a year that FTA could otherwise take out of service.

Two provisions need no amendment and are left alone on purpose. Section 5329(d)(4)(B) already requires a large-area recipient to spend 0.75% of its section 5307 money on safety; it reaches the operating tier, and it should, because operator assaults are an operating problem. Section 5310's operating share is already 50% and its program is untouched.

One gap remains: H.R. 8870's own renumbering of 5338(a)(2). If the 2026 bill adds or strikes subparagraphs, every letter in this Act's cross-references moves. The drafting rule is to cite 5338(a)(2) by program in the 2031 bill, not by letter.

## The full authorization table

Every line, every year, in billions of dollars. This is the canonical table: the fiscal model reads it, and where any figure elsewhere in this document conflicts with it, this one governs.

| Section | Program | Kind | Source | FY32 | FY33 | FY34 | FY35 | FY36 | Total |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 201 | Service operating assistance, 5307(i) | Renewal | Transit account | 6.00 | 6.50 | 7.00 | 7.50 | 8.00 | 35.00 |
| 301 | State of good repair formula, 5337 | Renewal | Transit account | 5.20 | 5.40 | 5.60 | 5.80 | 6.00 | 28.00 |
| 302 | Backlog retirement schedule, 5337(g) | Renewal | Transit account | 6.00 | 6.15 | 6.30 | 6.46 | 6.62 | 31.53 |
| 303 | Asset management enforcement, 5326 | Renewal | Transit account | 0.10 | 0.10 | 0.10 | 0.10 | 0.10 | 0.50 |
| 304 | Transit resilience | Renewal | Transit account | 0.60 | 0.60 | 0.60 | 0.60 | 0.60 | 3.00 |
| 401 | Capital Investment Grants, 5309 | Expansion | General fund | 4.50 | 5.00 | 5.50 | 6.00 | 6.50 | 27.50 |
| 501-505 | Workforce | Renewal | Transit account | 0.50 | 0.55 | 0.60 | 0.60 | 0.60 | 2.85 |
| 601 | Urbanized area formula, capital, 5307 and 5340 | Renewal | Transit account | 10.00 | 10.40 | 10.80 | 11.20 | 11.70 | 54.10 |
| 602 | Buses and bus facilities, 5339 | Renewal | Transit account | 2.60 | 2.70 | 2.80 | 2.90 | 3.00 | 14.00 |
| 603 | Rural, tribal and intercity bus, 5311 | Renewal | Transit account | 1.40 | 1.45 | 1.50 | 1.55 | 1.60 | 7.50 |
| 604 | Seniors and people with disabilities, 5310 | Renewal | Transit account | 0.60 | 0.62 | 0.64 | 0.66 | 0.68 | 3.20 |
| 605 | All Stations Accessibility | Renewal | Transit account | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 5.00 |
| 606 | Joint transit-rail facilities and station access | Expansion | General fund | 1.00 | 1.20 | 1.40 | 1.40 | 1.00 | 6.00 |
| 607 | Ferries | Renewal | Transit account | 0.20 | 0.20 | 0.20 | 0.20 | 0.20 | 1.00 |
| 608 | Emergency relief, quick release, 5324 | Renewal | Transit account | 0.10 | 0.10 | 0.10 | 0.10 | 0.10 | 0.50 |
| 701-705 | Planning, FTA capacity, safety, research, delivery | Renewal | Transit account | 0.90 | 0.92 | 0.95 | 0.97 | 1.00 | 4.74 |
|  | **Total** |  |  | **40.70** | **42.89** | **45.09** | **47.04** | **48.70** | **224.42** |
|  | Renewal |  | Transit account | 35.20 | 36.69 | 38.19 | 39.64 | 41.20 | 190.92 |
|  | Expansion |  | General fund | 5.50 | 6.20 | 6.90 | 7.40 | 7.50 | 33.50 |

### Against the baseline

| Category | 250-Plus, per year | The Act, per year | Change |
| --- | --- | --- | --- |
| Formula and other contract authority, excluding repair | \~$12.8B | $18.6B | +45% |
| State of good repair | \~$4.7B | $12.6B | +168% |
| Operating assistance for large areas | none | $7.0B | new |
| Capital Investment Grants, delivered | $2.4B | $5.5B | +129% |
| Joint facilities | none | $1.2B | new |
| **Total** | **$20.0B** | **$44.9B** | **+124%** |

The shape matters as much as the size. Formula capital rises a little faster than cost. The money that changes what agencies can do is in repair and operations, which between them take $14.9B of the $24.9B annual increase.

## The split recommendation

My number is no percentage at all: a transit renewal floor of $190.92B in statute for FY2031-35, with expansion in both bills as the residual. The split that results is 47 / 53 transit to rail in FY2031-35, moving to 56 / 44 and then 57 / 43.

| Period | Transit | Rail | Split, transit / rail | Rail + transit, as a multiple of highways |
| --- | --- | --- | --- | --- |
| FY2027-28, 250-Plus | $39.1B | $21.5B | 65 / 35 | 0.47 |
| FY2029-30, with reconciliation | $72.4B | $73.3B | 50 / 50 | 1.07 |
| FY2031-35, the two bills | $224.4B | $254.0B | 47 / 53 | 1.28 |
| FY2036-40 | $271.4B | $214.3B | 56 / 44 | 1.15 |
| FY2041-45 | $321.2B | $242.4B | 57 / 43 | 1.18 |

### What the handoff got right and wrong

**Right: the shape.** Rail's share rises and then falls. It peaks in the build-out period and settles near the 60 / 40 that IIJA showed. The framework predicted that from first principles, and the bottom-up numbers agree.

**Right: the floor belongs to transit.** Renewal cannot be deferred, and 85% of this Act is renewal.

**Wrong: that the floor fits inside a parity envelope.** The envelope for FY2031-35 is $306.1B at the House bill's highway levels. Transit's floor plus ARCA is $478.5B. A 60 / 40 division of the envelope gives transit about $183.6B, which is $5.8B less than the Act costs with no operating tier at all.

**Wrong: that rail as a whole is the residual.** ARCA is 37% expansion and 63% renewal by the definitions in section 101(f): $93.2B for sections 303, 310, 311 and 312, and $160.8B for the Northeast Corridor, operations, fleet, formula corridor capital, safety and the rest. Amtrak's operating grant is no more deferrable than a bus system's. The residual claimant is expansion, in both modes.

### What it does to ARCA's 2.27 ratio

It retires it. The ratio compares ARCA to rail's share of an envelope, and on these numbers rail's share of the envelope would be $81.6B, making ARCA 3.1 times its allotment. No bill survives that sentence in a hearing, and the sentence is an artifact of the envelope, not a fact about the bill.

The test that replaces it has three parts, and each can be read off the model.

1. **Is renewal in both modes covered?** Yes: $190.9B for transit and $160.8B for rail.
2. **Does the combined draw stay under 0.206% of GDP?** Yes, on the base case: 0.185% in FY2031-35 with a 1.0-cent start, peaking at 0.189%. A 0.6-cent start breaches the cap at the House bill's highway levels, by $14.3B in FY2029-30.
3. **If not, what gives?** Expansion, proportionally: transit holds 26% of the combined expansion total and rail 74%, so a $16B reduction falls about $4B on Capital Investment Grants and joint facilities and $12B on ARCA's Tier 1, terminal and long-distance programs.

### What this asks ARCA to change

- Replace the rail share of all fund receipts (8% rising to 28%) with 15% of new receipts. Rail's dedicated coverage of its whole program in FY2041-45 falls from 105% to 50%, and of its renewal programs to 78%.
- Drop the claim that the program becomes self-financing. No surface account does.
- Re-run the affordability table with highways and transit in it. On this model's base case ARCA alone runs at 0.130% of GDP in FY2031-35, not 0.099%.
- Put section 106(e)'s $25B readiness reserve expressly under the trigger. On the base case it fits in FY2031-35, released evenly, with $1.9B to $6.2B a year to spare.
- Keep parity as a statement of policy and stop using it as a constraint.

## Crosswalk with ARCA

The two bills touch in sixteen places. Five need a change to ARCA's text, and the rest are provisions one bill can borrow from the other.

| # | Where they touch | ARCA says | This Act says | Resolution |
| --- | --- | --- | --- | --- |
| 1 | Fund structure | Two SEC. 101 texts: a standalone rail trust fund and a rail account in a reformed fund | One fund, three accounts | Adopt the shared Title I; delete the standalone text |
| 2 | Rail's share | 8 / 15 / 22 / 28% of all receipts | 15% of receipts above the two base amounts | **ARCA changes** |
| 3 | Protection of existing accounts | 101(d): not less than FY2028 amounts, indexed | 101(c): the same amounts, credited first | Same substance, firmer drafting |
| 4 | Per-mile fee | 0.6 cents in FY2029 to 3.6 cents in FY2044 | 1.0 cent in FY2029 to 3.6 cents in FY2042 | **ARCA changes**; at House highway levels 0.6 cents breaches the cap |
| 5 | General-fund money | $132B transfer into the rail fund (section 105) | Mandatory appropriations to expansion programs, outside the fund | **ARCA changes** |
| 6 | Failed reauthorization | Section 107: $12B a year to rail, indexed | Renewal programs in every account continue at FY2035 levels | **ARCA changes**; rail's renewal programs are $34.4B in FY2035, so rail does better |
| 7 | Solvency | Section 108: proportional reduction | Expansion first, renewal last, executed agreements protected | **ARCA changes** |
| 8 | Anti-diversion | Section 109 and the older 9512(d): no rail money for chapter 53 purposes | Section 109: joint facilities funded from both accounts by use | Replace |
| 9 | Terminals | Section 310, $20.20B | Section 606, $6.00B for transit's share | Joint claim; shares computed under 5309(q)(4) |
| 10 | Station accessibility in reconciliation | $3.0B, "station access and ADA backlog" | $3.0B, rail transit and commuter stations | Name the station classes in each |
| 11 | Northeast Corridor access charges | Section 1103 adds a repair component to charges eight commuter authorities pay | Operating tier and backlog schedule | The added charge is an eligible backlog cost under 5337(g) where the asset is in the baseline |
| 12 | Match status | Section 403, categories A through E | Section 403 here adopts it for Capital Investment Grants | Borrowed |
| 13 | Gates and termination | Sections 401 and 407 | Section 405 applies them to grants over $1B | Borrowed |
| 14 | Cost discipline | Sections 705 through 709 | Section 705 cross-references them | Borrowed |
| 15 | Equipment and Buy America | Section 1201 pool; section 704 at 75% | Section 706: pool standard governs joint orders | One standard for jointly funded equipment |
| 16 | Through-ticketing | Section 604: common interface including transit agencies | No separate provision | Transit agencies' interface costs are eligible under section 601 |

### Statutes both bills amend

| Statute | ARCA | This Act | Conflict? |
| --- | --- | --- | --- |
| 26 U.S.C. 9503 | Redesignates the fund; adds the rail account | Same, plus strikes the capital limitation in (e)(3) | No, if drafted once |
| 49 U.S.C. 5309(q) | Not touched | Used as the cost-attribution rule for joint facilities | No |
| 49 U.S.C. 5302(15) | Not touched | Not touched. It excludes Amtrak service from "public transportation", which keeps the two programs' eligibility separate | No |
| 49 U.S.C. 24905(c) | Section 1103 extends the cost allocation policy | Row 11 above | Needs one sentence in each bill |

### ARCA items this work could not reproduce

These are for the rail side's own audit. Each is stated in the section where it arose.

1. The affordability row for FY2031-35, 0.099% of GDP. Reproduced since by ARCA's own method; counted all-in, this model's base case gives 0.130% for ARCA alone.
2. The statement that the trust fund's own general-fund need falls to zero around FY2035. On ARCA's revenue rows the fund collects about $82B that year, against $78B for highways and about $23B for baseline transit.
3. The anchor that a 2.4 cent per-mile fee raises about $44B. Wrong: it grosses about $80B; the base case now prices the fee on vehicle-miles.
4. The date the rail account is created: the fiscal-envelope section says 2028, the reconciliation section says 2030.
5. The known open items: the cash-flow model still on $185.43B, and section 106(e)'s text.

## Phasing, and what gets built

The Act's first effects are operating and repair effects, visible within a year of enactment. Its capital effects arrive in the late 2030s, on projects that enter the pipeline under it.

| Period | What happens |
| --- | --- |
| December 2026 | 250-Plus enacted. The transit account needs a transfer in the same bill or runs dry during FY2027 |
| FY2027-28 | Formula money flows; discretionary grants slow. Pennsylvania's stopgaps expire in FY2027 and the Bay Area's fate turns on a November 2026 ballot. Marker bills and the GAO and CBO requests are filed |
| FY2028 | Fuel taxes extended as they are, with a patch through FY2030. The transit account survives |
| FY2029 | First reconciliation package: $12.0B for transit, including $4.0B of operating transition grants with maintenance of effort attached. Per-mile fee begins at 1.0 cent; the three accounts are created |
| FY2030 | Second package: $20.0B. The grant agreements dated 2027 on FTA's dashboard sign in this window |
| FY2031 | Enactment. The operating tier and the backlog apportionment flow in the first year because both are formulas. FTA publishes backlog baselines within twelve months |
| FY2031-33 | Projects outside today's pipeline enter project development: Interborough Express, West Seattle, the Red-Blue Connector, Red and Purple Modernization Phase 2 |
| FY2032-36 | Nine projects over $1B open, all from today's pipeline: East San Fernando Valley, Second Avenue Subway Phase 2, Austin, the WMATA and MBTA core capacity programs, The Portal, Southeast Gateway, Tacoma Dome, the Columbia River crossing |
| FY2035-36 | Reauthorization. A quarter of the backlog is retired. The first three years of section 5307(i)(7) data show whether the operating conditions held |
| FY2037-45 | The projects this Act started open: Interborough Express and West Seattle in 2037-38, Baltimore's Red Line in 2040, Ballard in 2042, Sepulveda in 2043. The backlog is three-quarters retired by FY2045 |

### What the Act buys, by 2045

| Measure | 2026 | 2045 under the Act |
| --- | --- | --- |
| Repair backlog, 2025 dollars | $127.8B | $32.0B |
| Tracked capital projects in service, of 64 | 0 | 63 |
| Of which over $1B | 0 | 25 |
| Federal share of large-system operating cost | 17% in 2024, falling as relief money ends | Held near 17% by statute |
| Mass Transit Account covered by dedicated revenue | 36% | 58% |
| Legacy rail stations with a statutory accessibility date | none | all, by FY2045 |

### What still does not get built

- **Link21.** A second transbay crossing shared with intercity rail clears planning in this window and opens around 2050. It is the one project here that belongs equally to ARCA's second generation.
- **Second Avenue Subway beyond 125th Street, a Roosevelt Boulevard subway, a new downtown Washington line.** None has an environmental document, and no authorization in 2031 produces one in time.
- **Bus networks.** The Act funds vehicles, facilities and operations. Street space is a local decision the bill cannot make.

The summary is the mirror image of ARCA's. ARCA finishes a first generation of new railroad and starts a second. This Act stops an existing network from shrinking, retires three-quarters of what it owes itself, and opens about two dozen large projects, most of which were already designed.

## The next decade: the FY2036 reauthorization

The second bill is larger than the first, $592.5B over ten years, and that is the opposite of ARCA's second decade. Rail's program shrinks in real terms once its first generation is built. Transit's does not, because a renewal program has no completion date.

| Line | FY2036-40 | FY2041-45 |
| --- | --- | --- |
| Renewal: formula capital, repair, backlog schedule, buses, rural, accessibility, workforce | $183.2B | $215.6B |
| Operating tier | $45.1B | $54.8B |
| Expansion: Capital Investment Grants and joint facilities | $43.1B | $50.8B |
| **Total** | **$271.4B** | **$321.2B** |

These extend the FY2035 lines by rule: renewal at 3.5% a year, the operating tier at 4%, backlog installments at inflation, Capital Investment Grants at 5% to FY2040 and inflation after.

### What the FY2036 bill inherits

| Inherited | Consequence |
| --- | --- |
| Five years of published operating data under 5307(i)(7) | The operating tier is argued on evidence. If state support fell or unit costs ran, the bill tightens it; if not, the tier stops being controversial |
| A backlog baseline for every rail system, a quarter retired | The schedule either held or the section 5326 directions show who fell behind |
| A transit account at about half coverage | The argument is over the share of new revenue, reset by the equal-coverage rule in section 101(h) |
| Eight megaprojects open and nine more under construction | Capital Investment Grants are judged on delivered cost, with unit costs in a public database |
| Mandatory appropriations for expansion that end in FY2035 | The largest exposure. Renewal continues by law if the bill fails; expansion does not |

### Three questions the second bill has to answer

**Does the operating tier grow with service or with cost?** The first bill grows it 4% a year regardless. By 2036 there is enough data to tie growth to service hours delivered.

**What happens when the backlog baseline is retired?** The schedule ends in FY2050. Assets that enter the backlog after 2030 are not in it. The FY2036 bill should set a second baseline, or fold retirement into a formula sized to keep the backlog at zero.

**Who pays for commuter rail on the Northeast Corridor?** ARCA's second decade sets a $4B a year renewal ramp for the corridor. Commuter authorities run most of the trains on it. Section 109 gives a rule for joint facilities; the second bill has to apply it to the largest joint facility in the country.

### Three things a 2031 bill cannot plan for

- **Automated vehicles.** Cheap automated ride service takes the trips that low-frequency bus routes serve. Frequent trunk service is least exposed, and the operating tier's service-hour formula rewards it.
- **Remote work.** Commuter rail ridership is at 77% of 2019. If it stays there the case for peak-capacity projects weakens and the case for all-day service strengthens.
- **Climate damage.** Section 304 is $3.0B against an exposure nobody has priced. ARCA's document found the same gap on the Northeast Corridor.

## Political path and fallback tiers

The Act clears five committees, and the shared revenue title is the one that decides whether either bill has money behind it.

| Committee | What it reports |
| --- | --- |
| House Transportation and Infrastructure | Titles II through VII |
| Senate Banking, Housing, and Urban Affairs | Titles II through VII. Transit is this committee's, not EPW's or Commerce's |
| House Ways and Means; Senate Finance | Title I, shared with ARCA |
| Appropriations, both chambers | The obligation limitation on renewal; nothing on expansion, which is mandatory |
| Budget, both chambers | The 2029-30 reconciliation instructions |

The practical consequence matches ARCA's. Title I should be drafted, scored and shopped to Finance and Ways and Means first, as one product for both bills. A transit title and a rail title that arrive asking for the same new revenue separately will be played against each other.

### The coalition, by what each bloc is buying

| Bloc | What the Act gives them | Provision |
| --- | --- | --- |
| Large-system delegations: New York, New Jersey, Illinois, Pennsylvania, Massachusetts, California, the Washington region | Operating money by formula, and the backlog on a schedule | 201, 302 |
| Small-urban and rural members | An 80% rural operating share, an operating-tier ceiling that keeps small areas' grants spendable, bus money | 603, 201, 602 |
| Sun Belt growth regions | Capital Investment Grants that obligate in full at signing | 401 |
| Highway interests | 35% of new revenue on top of an indexed base, and a highway account that is three-quarters covered instead of insolvent | Title I |
| Transit labor | The service floor, apprenticeships, operator protection, no contracting mandate | 201, Title V |
| Fiscal conservatives | Maintenance of effort, a cost benchmark, a published backlog, a general-fund trigger with an order of operations | 201, 303, 108 |
| Appropriators | An obligation limitation on $190.9B of renewal | Title I |
| Disability advocates | A completion date for station accessibility | 605 |

The hard vote is the highway bloc's. Thirty-five percent of new revenue is less than the 88% of legacy receipts highways hold today, and the answer has to be that 88% of an account that is $221B short through FY2036 is worth less than 35% of one that is solvent.

### What is tradeable

| Tradeable | Range | Notes |
| --- | --- | --- |
| Size of the operating tier | $4B to $8B a year | The largest dial after the fee. $6B rising to $8B is drafted |
| Per-mile starting rate | 0.6 to 1.0 cent | Each 0.2 cents is worth about 0.012 points of GDP in FY2031-35; 0.6 and 0.8 cents breach the cap in FY2030 |
| Incremental shares | Highways 23% to 40% | 35 / 50 / 15 is drafted; the equal-coverage answer is 34 / 54 / 12; the transit gap waits for the EV redesign |
| Backlog period | 20 to 30 years | Thirty years saves $10.5B in FY2031-35 and leaves a third of the backlog standing in 2050 |
| Fare-evasion and security conditions from H.R. 8870 | Keep or drop | Worth trading for the maintenance-of-effort rule, which matters more |

Four provisions should not be traded: the amendment to 26 U.S.C. 9503(e)(3), transit's written share in section 101(d), the conditions in 5307(i)(4), and full obligation under 5338(d)(2). Without them the bill is 250-Plus with larger numbers and an empty account.

### Fallback tiers

| Round | Cuts | Program after |
| --- | --- | --- |
| First, -$30.0B | Operating tier flat at $4.0B a year ($20.0B); Capital Investment Grants to $20.0B; joint facilities to $3.0B; buses to $11.5B; resilience to $1.0B | **$194.4B** |
| Second, -$30.0B | Backlog retirement on a 30-year schedule ($21.0B); formula capital to $46.1B; operating tier to $15.0B; Capital Investment Grants to $15.0B; accessibility to $3.5B | **$164.4B** |
| Third, -$34.4B | Operating tier three years only ($9.0B); backlog to $15.0B; formula capital to $38.0B; repair formula to $24.0B; Capital Investment Grants to $12.5B; buses to $9.0B; other lines down $5.3B | **$130.0B** |

The third round is $26.0B a year, which is IIJA in FY2031 dollars with a three-year operating bridge and a slow backlog schedule. It is a defensible bill. It is not the bill this document argues for, and the difference is whether the federal government treats keeping transit running as its problem or as the states'.

## Assumptions, sensitivities and open items

Three assumptions decide whether the conclusions hold; the rest move numbers without changing them.

### The conclusions are sensitive to these

| Assumption | What I assumed | What changes if it is wrong |
| --- | --- | --- |
| Per-mile fee yield | Rate times FHWA vehicle-miles, all vehicles, 10% collection cost | The base case since October 12. On ARCA's anchor, about 40% lower, nothing fits at House highway levels. A light-duty-only fee at 13% collection cost puts FY2030 at the cap, 0.206% |
| Fuel-tax displacement | Linear, complete when the fee reaches 3.6 cents in FY2042 | If fuel taxes are kept alongside the fee, fund receipts in the 2040s are about 60% higher |
| Size of the operating tier | $6.0B in FY2031, anchored on the 2024 federal share | At $12B (scenario C) the base case reaches the cap, 0.206% in FY2033. At zero (scenario A) it peaks at 0.197% in FY2030; on ARCA's old revenue line the Act fit in FY2031-35, peaking at 0.202%, though FY2029-30 is still over |
| Highway levels | H.R. 8870 as introduced: $72.9B to $77.6B a year, FY2027-31 | At ARCA's flat-real $62.657B the base case falls to 0.173% in FY2029-30 and 0.168% in FY2031-35, and a 0.6-cent start misses narrowly, 0.209% in FY2030. The higher House levels are why the fee still has to start at a cent |

### These move numbers, not conclusions

- The 250-Plus transit deal: contract authority as reported, $5B of Capital Investment Grants guaranteed.
- The backlog held flat in real terms from 2018 data to FY2031.
- An 80% federal share of backlog installments.
- GDP growth of 4.1% nominal, backed out of ARCA's own percentage rows.
- Out-year growth rates for FY2036-45.
- Grant slippage of one to two years in FY2027-28.

### Open items

- [x] Run the section 5307(i) apportionment against National Transit Database data, by urbanized area and by state
- [x] Verify H.R. 8870's highway total against the bill text
- [x] Read 49 U.S.C. 5303-5305, 5310, 5311, 5324, 5329, 5339 and 5340 and draft the conforming amendments (sections 711-716)
- [x] Confirm the American Rescue Plan section number and the terms of its operating eligibility
- [x] Verify opening dates and costs for the 17 projects I entered from memory
- [x] Compute use shares at the five ARCA terminals to replace the 30% placeholder in section 606
- [x] Get a count and cost of inaccessible legacy rail stations for section 605
- [x] Reconcile this model with ARCA's affordability table, row by row
- [x] Check the October 2025 payment hold on New York projects before citing it
- [ ] Decide whether ARCA's section 107 floor survives as a rail-only provision
- [ ] Read the implementing regulations (49 CFR parts 625, 630 and 673) against Titles II and III
- [ ] Get FTA to publish a national cost for making legacy rail stations accessible; only system figures exist
- [ ] Scope the five terminal projects and set section 606 project by project under the new SEC. 109 rule
- [ ] Rerun the apportionment with FTA's own multi-area splits instead of primary-area assignment
- [ ] Check H.R. 8870's section 3023 figures against the enrolled text once it is reachable

### Verification pass, October 5, 2026

The pass covered the 17 projects entered from memory, the three ARCA figures the model could not reproduce, and the facts cited without a source. One result changes a headline finding.

**The per-mile anchor is wrong, and correcting it removes the breach.** ARCA says 2.4 cents a mile replaces all current trust fund revenue, about $44B. FHWA counts 3,323.8 billion vehicle-miles in 2025, so 2.4 cents grosses about $80B. Eno reports the same: 2.4 cents raises about $78B, the full annual outlays of the highway and transit programs. Receipts are replaced at about 1.4 cents. The model's base case keeps ARCA's anchor so both bills are tested on one revenue line. On the physical base, with 10% taken off for collection cost:

| Case, 0.6-cent start | FY2029-30 | FY2031-35 | Cap |
| --- | --- | --- | --- |
| ARCA's revenue line | 0.219%, peak 0.224% | 0.213%, peak 0.218% | 0.206% |
| Physical base | 0.199%, peak 0.203% | 0.185%, peak 0.191% | 0.206% |
| Physical base, operating tier doubled | 0.199%, peak 0.203% | 0.202%, peak 0.207% | 0.206% |

On ARCA's highway levels the vehicle-miles yield lets a 0.6-cent schedule carry both bills. On the House bill's highway levels, which the 2026 law sets, it does not; the October 12 rebase in the fiscal envelope section adopts both corrections and keeps the 1.0-cent start. Two assumptions sit under the new rows and both are mine: the fee applies to all vehicles, and the schedule is in nominal cents.

**ARCA's affordability rows reproduce, by a method that does not match its cap.** The 0.105%, 0.099%, 0.019% and 0.001% rows equal rail's general-fund draw plus the CBO baseline trust fund shortfall, less the highway and transit share of new per-mile and vehicle-fee receipts. The model returns 0.110%, 0.097%, 0.019% and 0.002% on that method. Three choices are buried in it:

- Highways and transit are frozen at CBO baseline outlays for 15 years.
- Fuel taxes are not displaced in this calculation, though they are displaced in the rows that give rail its dedicated revenue. That is the only way the trust fund's own need reaches zero around FY2035. With displacement applied consistently it stays at $14B to $29B a year through FY2045.
- The cap's numerator includes $36.8B of advance appropriations for every mode. The test counts no continuing general-fund appropriations for highways or transit.

**Pipeline corrections.** The grid and map carry these.

| Project | Was | Now |
| --- | --- | --- |
| Second Avenue Subway Phase 2 | $7.70B | $6.97B budget; the agreement baseline is $7.7B |
| Red Line Extension | Construction from 2025 | Groundbreaking April 24, 2026 |
| D Line subway | Sections 2 and 3 in 2027 | Confirmed; Section 1 opened May 8, 2026 |
| Purple Line | Opens FY2027 | Target December 30, 2027, which is FY2028 |
| East San Fernando Valley | Opens FY2031 | December 2031, which is FY2032 |
| Green Line Extension, Minneapolis | Opens 2027 | Confirmed: June 12, 2027, at $2.86B |
| IndyGo Blue Line | Opens FY2028 | Late 2028, which is FY2029 |
| West Seattle Link | $7.0B, 4.1 miles, four stations | $4.9-5.3B in 2025 dollars, 3.9 miles, three stations; Sound Transit's opening is now 2035 |
| Ballard Link | $11.5B | $20.1-22.6B in 2025 dollars; funded only to Seattle Center; opening 2042 |
| Charlotte Red Line | $2.0B | $1.26B; sales tax passed November 2025 |
| Baltimore Red Line | Light rail | Mode reopened April 2026; decision due early 2027; $4.7-9.0B if light rail |
| Sepulveda | Heavy rail, $24.0B | Confirmed at $24.2B in 2023 dollars; preferred alternative adopted January 22, 2026 |
| Link21 | $29B | $18-30B in 2023 dollars for the crossing; standard gauge adopted June 2025; its federal path is FRA Corridor ID, not Capital Investment Grants |

None of the nine projects outside the pipeline has entered it. Link21 belongs in the crosswalk as a rail-side project that section 109 would let transit money join.

**Facts confirmed.** The American Rescue Plan's section 3401 appropriated $30.46B from the general fund, available until September 30, 2024, at a 100% federal share and open to operating costs. Its $250M for Small Starts reached projects still in project development, which is the precedent for the Byrd table's Capital Investment Grants row. H.R. 8870's transit contract authority is $87.6B, not the $87.4B an earlier pass produced by summing rounded years.

Sources: [FHWA Traffic Volume Trends, December 2025](https://www.fhwa.dot.gov/policyinformation/travel_monitoring/25dectvt/); [Eno, Closing the Trust Fund Gap](https://enotrans.org/wp-content/uploads/2026/03/Part-5-Closing-the-Trust-Fund-Gap-by-Increasing-Federal-Revenues.pdf); [CBO trust fund baseline, June 2026](https://www.cbo.gov/system/files/2026-06/51300-2026-06-highwaytrustfund.pdf); CBO cost estimate for H.R. 8870, September 30, 2026; [49 U.S.C. 5301 note](https://uscode.house.gov/view.xhtml?edition=prelim&num=0&req=granuleid%3AUSC-prelim-title49-section5301); [Governor Hochul on Second Avenue Subway](https://www.governor.ny.gov/news/governor-hochul-celebrates-groundbreaking-major-construction-stage-second-avenue-subway-phase); [ABC7 on the restored funds](https://abc7ny.com/post/nycs-second-avenue-subway-project-mta-heads-court-60m-withheld-funds-trump-administration/18897991/); [CBS Chicago on the Red Line Extension](https://www.cbsnews.com/chicago/news/cta-red-line-extension-groundbreaking/); [Sound Transit cost memo](https://www.soundtransit.org/st_sharepoint/download/sites/PRDA/FinalRecords/2025/Memo%20-%20Updated%20ST3%20Capital%20Project%20Cost%20Estimates%2009-11-2025_updated.pdf); [The Urbanist on West Seattle](https://www.theurbanist.org/west-seattle-link-date-slips-to-2035-as-sound-transit-greproperty-acquisitions/); [Maryland MTA on the Red Line](https://www.mta.maryland.gov/articles/538); [LA Metro board report on Sepulveda](https://boardagendas.metro.net/board-report/2025-1062/); [BART on Link21](https://www.bart.gov/news/articles/2025/news20250612-1).

### Second pass and rebase, October 12, 2026

**Rebase.** The base case now prices the per-mile fee on vehicle-miles and carries highways at H.R. 8870's levels. The 1.0-cent start survives, for a different reason than before: on ARCA's flat highway figure 0.6 cents would now pass, but the House bill sets highways about $8B a year higher. The trigger does not fire, and ARCA's $25B readiness reserve now fits under the cap. The incremental shares move from 30 / 50 / 20 to 35 / 50 / 15. Restated on the vehicle-miles yield with ARCA's own shares and schedule, ARCA's rail revenue rows rise by 21%, 13%, 9% and 5% in the four periods.

**Apportionment run.** Done against NTD 2024 and ACS 2019-23 data; results and the redrafted ceiling are in Title II.

**Chapter 53.** Sections 5303, 5304, 5305, 5310, 5311, 5324, 5329, 5338, 5339 and 5340 read; conforming amendments drafted as sections 711-716 in Title VII. Two more stale cross-references found, in 5339(a)(5) and 5340(b).

**Remaining verifications.**

| Item | Finding | Status |
| --- | --- | --- |
| H.R. 8870 transit contract authority | $16.868B, $17.205B, $17.527B, $17.835B, $18.157B; $87.592B in all. 5307: $7.75B rising to $8.26B. 5337: $4.64B to $4.66B. 5339: $1.70B to $2.30B | Matches APTA's funding table and a quotation of section 3023; the bill text itself was not reachable |
| Red Line Extension opening | 2030, as reported at the April 2026 groundbreaking | No CTA or FTA statement found |
| Honolulu, Skyline to Civic Center | Official budget $10.08B; target March 31, 2031; FTA's consultant projects April 2032 | Grid keeps FY2031 and flags the slip |
| IndyGo Blue Line | $370M to $390M, a 2023 figure; federal grant $149.9M plus $22M of RAISE | Cost stale |
| Red-Blue Connector | About $850M, the 2021 estimate; no newer figure | Unverified |
| Red and Purple Modernization, next phases | No estimate published; a planning study is due in 2026 | Grid figure is a placeholder |
| Joint terminals | Commuter use 79% of train movements at Chicago and about 85 to 94% of riders at the four existing terminals; no Atlanta terminal exists | Section 606 and SEC. 109 redrafted |
| Inaccessible stations | About 965 of 3,447 rail transit stations, 28%, in 2021; no national cost estimate | Section 605 revised |

Sources: [APTA, H.R. 8870 funding table](https://www.apta.com/wp-content/uploads/2026/06/HR-8870-BUILD-America-250-Draft-Funding-Table-Public-Transit-05222026.pdf); [NTD time series, data.transportation.gov](https://data.transportation.gov/d/ectq-t3k3); [Census table C17002](https://data.census.gov/table/ACSDT5Y2023.C17002); [Civil Beat on Honolulu's schedule](https://www.civilbeat.org/2026/07/another-delay-for-honolulu-rail-the-timeline-appears-to-be-slipping-again/); [Civil Beat on Honolulu's cost](https://www.civilbeat.org/2026/08/cost-of-honolulu-rail-line-may-be-climbing-again/); [WTTW on the Red Line Extension](https://news.wttw.com/2026/04/24/cta-kicks-construction-long-awaited-57b-red-line-extension-far-south-side); [Chicago Union Station fact sheet](https://chicagounionstation.com/uploads/documents/CUS-Fact-Sheet-2019.pdf); [Atlanta Regional Commission station study](https://cdn.atlantaregional.org/wp-content/uploads/20251107-tcc-amtrak-station-plan-update.pdf); [Stateline on station accessibility](https://stateline.org/2021/12/07/no-more-stairs-cash-influx-to-make-transit-more-accessible/).

### What the audit pass caught

The audit ran after the first full draft and before this version.

| Finding | Correction |
| --- | --- |
| An earlier chat message said SEC. 101 would leave transit about $30B a year in FY2041-45. That figure treated all of rail's dedicated revenue as its share of the fund | Rail's aviation and diesel taxes are separate. The fund is about $118B a year, not $175B, and transit's guaranteed amount is about $10B |
| Trigger reduction stated as $23B in one section and $16B in another | $15.9B, from the model; both sections now agree. Superseded by the October 12 rebase, under which the trigger does not fire |
| Repair and operations said to take $19.6B of the annual increase | $14.9B |
| Rail's FY2035 renewal programs stated as $30.6B | $34.4B, from ARCA's canonical table less sections 303, 310, 311 and 312 |
| Thirteen of 17 large pipeline projects said to hold a rating | Ten |
| "A third less headroom" for ARCA | About half: 0.048 points against a reported 0.093 |
| Unrounded incremental shares given as 23 / 63 / 15, summing to 101 | 22 / 63 / 15 |
| First revenue calibration overstated ARCA's FY2031-35 rail revenue by 10.5% | Displacement now starts in FY2029; the model is within 3.2% |
| Reconciliation package drafted at $36B breached the cap in FY2029 | Resized to $32B and back-loaded |
| FY2036-45 line items in the second-decade table did not sum to the model | Recomputed from the model |

## Sources

**Read in full**

- [CRS R48644, Surface Transportation Reauthorization: Public Transportation, updated September 2, 2026](https://www.congress.gov/crs-product/R48644): funding history, the backlog and DOT's scenarios, federal operating shares, fare revenue, H.R. 8870's transit provisions, the Secretary's July 22, 2026 letter
- [CBO, Highway Trust Fund Accounts, June 2026 baseline](https://www.cbo.gov/system/files/2026-06/51300-2026-06-highwaytrustfund.pdf): receipts, outlays and shortfalls by account
- [FTA, Capital Investment Grants Dashboard, September 11, 2026](https://www.transit.dot.gov/sites/fta.dot.gov/files/2026-09/CIG-Public-Dashboard-09-11-2026.pdf): all 47 pipeline projects
- [Mass Transit, House T&I Committee approves BUILD America 250 Act, June 2, 2026](https://www.masstransitmag.com/management/article/55381249/house-ti-committee-approves-build-america-250-act-for-surface-transportation-reauthorization): contract authority by year
- [SSTI, Transit agencies are averting the fiscal cliff, November 11, 2025](https://ssti.us/2025/11/11/transit-agencies-are-averting-the-fiscal-cliff-but-still-need-long-term-funding-solutions/): Pennsylvania and Illinois stopgaps
- United States Code, current text: [49 U.S.C. 5302](https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title49-section5302&num=0&edition=prelim), [5307](https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title49-section5307&num=0&edition=prelim), [5323](https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title49-section5323&num=0&edition=prelim), [5326](https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title49-section5326&num=0&edition=prelim), [5333](https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title49-section5333&num=0&edition=prelim), [5337](https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title49-section5337&num=0&edition=prelim), [5338](https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title49-section5338&num=0&edition=prelim) and [26 U.S.C. 9503](https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section9503&num=0&edition=prelim)
- [49 U.S.C. 5309](https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title49-section5309&num=0&edition=prelim): definitions, subsections (g), (l) and (q) only
- [ARCA bill architecture document](https://claude.ai/code/artifact/518f3bb4-2063-42e2-9b4b-1936f8d19ca8), the corridor pipeline grid and the network map

**Search excerpts only, not opened in full**

- [CBO cost estimate, H.R. 8870](https://www.cbo.gov/publication/62817)
- [Holland & Knight, A Closer Look at the BUILD America 250 Act](https://www.hklaw.com/en/insights/publications/2026/05/a-closer-look-at-the-build-america-250-act): the $376B highway figure
- [Citizens Budget Commission, MTA Operating Budget Outlook](https://cbcny.org/research/mta-operating-budget-outlook-short-term-stability-long-term-risks)
- [Mercury News, September 20, 2026](https://www.mercurynews.com/2026/09/20/the-bay-area-faces-a-transit-reckoning-will-voters-pay-to-keep-it-running/); [SFMTA](https://www.sfmta.com/bridging-our-budget-gap-save-muni)
- [New Jersey Monitor, July 16, 2026](https://newjerseymonitor.com/2026/07/16/nj-transit-approves-3-5-billion-budget/)
- [WESA, May 29, 2026](https://www.wesanews.org/development-transportation/2026-05-29/pittsburgh-regional-transit-budget-no-fare-hikes-service-cuts)
- [DMVMoves](https://dmvmoves.org/cog-and-metro-boards-endorse-plan-to-provide-460m-to-modernize-metro-transform-regional-transit/)
- [APTA, Workforce Issues](https://www.apta.com/industry-issues/workforce-issues/)

**From my own knowledge, labeled where used**

Still unverified after the October 5 pass: the Red Line Extension's 2030 opening; Honolulu's cost and its March 2031 date, which the agency says is slipping; IndyGo's cost; the Red-Blue Connector's cost, a 2021 estimate; any cost for the next phases of Red and Purple Modernization, for which CTA has published none; the transit operators at ARCA's terminals; and H.R. 8870's year-by-year transit contract authority against the bill text.

**Modeled, not sourced**

Every projection past FY2026, the 250-Plus transit deal, grant slippage, the authorization levels, and the general-fund test. All of it is in `transit_fiscal_model.py`, which prints its assumptions and can be re-run with any of them changed.
