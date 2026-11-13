# Transportation: delivery

Role: section 5 of the transportation dossier. It says who runs each provision of section 4 (`4-specification.md`, `provisions.json`), what capacity that takes, on what timeline, what states do, what remedies hold when delivery fails, and what the statute must say so a reluctant agency cannot stall it. Status: reviewed at L3 (`review-milestone.md`; closed in stage C, see the README), written on the decisions in `DEC-2026-11-10-08`. It converts the legacy design's delivery content (Draft 2's divisions A, E and F) and adds only what the decisions changed.

## 1. Who runs what

| Agency | Runs | Provisions |
| --- | --- | --- |
| **Treasury (IRS)** | Fuel taxes, steps and the price pause; the clean-vehicle per-mile charge (with states, at registration); the weight-distance charge (through the fuel-tax filings carriers already make); rail diesel; account receipts and projections | MOV-29, MOV-30; division A secs. 102-104, 108, 110, 111 |
| **FHWA** | Formula highway programs; Interstate and Bridge Renewal; fix-it-first reports and reviews; Safe System; resilience and freight set-asides; the Charging Gap Program's gap map and auctions | Division B |
| **FTA** | Formula and repair programs; the operating tier and its published reports; Capital Investment Grants | Division C |
| **FRA** | Corridor development; Tier 1 gates and the readiness reserve; terminals; regional commissions; the national fleet | Division D |
| **The Secretary of Transportation** | Certifies Tier 1 readiness for the reserve; sets joint-facility shares; publishes the yearly account report with Treasury | Division A secs. 106, 108, 109 |
| **GAO** | Reviews the per-mile charges' collection cost, evasion and privacy every three years | Division A sec. 111 |
| **States** | Collect the clean-vehicle charge at registration under agreements; choose and build formula projects; publish condition trends and lifecycle analyses; may toll rebuilt Interstate segments; sponsor rail corridors through commissions | Divisions A, B, D |
| **Transit agencies** | Certify maintenance of effort and the service floor; publish preventive-maintenance and cost reports | Division C |

## 2. Timeline

Dates follow the scenario calendar (`dossiers/scenario/`): R1, the plan's first budget bill, targets February to March 2029; R3 passes in summer 2030.

| When | What | Notes |
| --- | --- | --- |
| 2027-28 (exception) | The 2028 extension (MOV-28.01): rates and fund credits to September 30, 2029; heavy-vehicle use tax to September 30, 2030; a transfer keeping both accounts solvent through FY2031 | Needs 60 votes under divided government. Without it, credits stop after September 30, 2028 [EV-MOV-004] |
| By November 2028 (preparation) | Text and CBO scores for MOV-29 ready; Treasury and DOT design the registration-based collection with states that already run road usage charges | Oregon and Utah are the partners [EV-MOV-116] [EV-MOV-119] |
| Early 2029 | The 2029 act (MOV-29, on R1) | If no multi-year authorization is law by December 31, 2028, the contingency authorization (MOV-31.90) moves on regular order in 2029-30 |
| October 1, 2029 | Fuel taxes indexed; the first 3-cent step | |
| March 31, 2030 | The highway cost allocation study, which sets the weight-distance schedule | Feeds the 2030 act |
| Summer 2030 | The 2030 act (MOV-30, on R3) | |
| October 1, 2030 | Clean-vehicle charge, weight-distance charge and rail diesel (first rates) begin; the EV fee and use tax end | A year after enactment, so collection can be built |
| October 1, 2031 | Aviation surcharge and full rail diesel rates; the Moving America Act of 2031 takes effect (FY2032) | |
| FY2032-36 | The 2031 bill's programs; top-ups obligated by 2036-37 and spent by 2038-39 | The packages obligate over FY2029-31 [EV-MOV-217] |
| FY2037 | Account shares move to 45 / 40 / 15 | |
| FY2040-44 | The fossil transition premium, five 2-cent steps | |

## 3. Capacity

- **Treasury.** The per-mile charges are a new kind of excise.
  - The design keeps them on records that exist: odometer readings at state registration, and quarterly filings carriers make under the fuel-tax agreement (IFTA).
  - Trucks that run only inside one state file no IFTA return. Those of 55,000 lb or more already file the annual heavy-vehicle use tax return (26 U.S.C. 4481) [EV-MOV-209], which the charge replaces; those between 26,000 and 55,000 lb file nothing federal today. Working choice for the 2030 act's drafting: intrastate carriers report odometer miles once a year on that annual return, with the declared weight their state registration already records, instead of quarterly. It is still a new line on a return for the lighter group, the one added burden; the IFTA route is unchanged for interstate carriers (MOV-30.01).
  - It provides implementation money ($750 million through FY2033 in Draft 2) and a 10% ceiling on collection cost.
  - The working assumption is that collection costs start high and fall. Oregon and Utah's experience puts the range at about 11% to 14% of revenue at small scale [EV-MOV-118] [EV-MOV-120], so the ceiling may bind in the early years. That is something to study in implementation, with GAO's three-year review as the check.
- **Audits.** Weight-mile taxes are evaded at an estimated 5% to 11% [EV-MOV-122]. Working assumption: an audit program sized to bring evasion toward the low end, paid within the collection ceiling. Its exact rate is left to Treasury rule.
- **FRA and FTA staff.** FRA's staff is down 22% [EV-MOV-109], and the plan triples its rail program. The legacy design paid for delivery capacity in division E ($0.50B of owner-side engineering grants) and for FTA capacity in package two ($1.00B). Working assumption: those amounts stand. Whether they are enough is a question to study in the first two years; it does not change a design choice. FTA's own staffing counts are not yet in the register.
- **States.** Formula money keeps flowing through state DOTs as today. The new duties are:
  - registration-based collection;
  - two published reports (memo 5);
  - the set-asides.

  The reports replace two review processes the legacy design would have added (`4-specification.md`, "What the decisions changed").
- **Transit agencies.** They certify two conditions (maintenance of effort and the service floor) and publish two figures each year (memo 4). Agencies already report the underlying data to the National Transit Database.
- **Workforce.** Construction, transit operations and rail manufacturing share a labor pool with housing and clean power (`dossiers/shared-rules.md`, rule 8). Section 7 flags the overlap; no transportation-specific rule.

## 4. Getting money to projects

The legacy design's answers to slow grants [EV-MOV-009], kept as chosen:
- **Agreement deadline.** A grant agreement within 180 days of selection, or the Secretary reports why.
- **Flexibility.** Pre-award authority, and scope changes within 10% without reselection.
- **Full obligation.** Capital Investment Grants obligated in full at signing.
- **Protected agreements.** Executed agreements are protected by a decision deadline, a cure period, a published basis and judicial review before termination (division E sec. 104; division D's anti-pretext rules).
- **Paying for performance.** Charging Gap awards lapse if a site is not energized within 24 months, and half the payment waits on five years of uptime.

## 5. What the statute must say for a reluctant agency

The record since 2025 shows why money and dates have to be self-executing:
- the federal charging program was suspended and part rescinded [EV-MOV-014];
- FRA is reviewing every corridor in its pipeline [EV-MOV-109];
- one new capital grant agreement was signed in transit in nearly two years [EV-MOV-112].

So the design:
- provides contract authority and appropriations that are available until spent;
- sets apportionment formulas in statute, not by rule;
- sets gate tests that are objective and published (division D sec. 401);
- adds deadlines with reporting duties, and judicial review before termination;
- continues renewal programs at FY2036 levels, adjusted for inflation, if the 2031 bill lapses (division A sec. 107).

None of this stops an administration from slowing work it opposes. It does make delay visible and contestable.

## 6. Remedies

- **Taxpayers.** Per-mile charge readings are tax return information, with the Internal Revenue Code's remedies for disclosure, from the charge's first day. From the charge's start on October 1, 2030, the 2029 act defines it by odometer readings only and the readings are tax return information; the bar on collecting location data, the three-year deletion and the private right of action are in the 2031 bill and apply from October 1, 2031 (sec. 111, MOV-31.11). Draft 2 suggests a standalone privacy bill before October 1, 2030 to close that year. That is Draft 2's suggestion, not a plan commitment: no provision, vehicle or agenda row carries it (a question for Espen on the board).
- **States and sponsors.** Executed agreements can be terminated only after notice, a cure period and judicial review (section 4 above).
- **Riders.** The service floor is a grant condition. An area that drops below 95% of its FY2028-30 service hours loses the operating tier for that year.
- **The public.** Each state's condition trend, each large lane-adding project's lifecycle analysis, and each transit area's preventive-maintenance share and cost per service hour are published every year. FHWA and FTA review the outliers (memos 4 and 5).

## 7. Where a state refuses

- **Formula money** still flows. State collection of the clean-vehicle charge is by agreement, at a state's request. Where a state does not sign one, owners submit a verified odometer reading and pay Treasury once a year (the drafted 26 U.S.C. 4492(a) and 4493(a)-(b) in Draft 2). That is more burden for those owners, which is why Treasury and DOT design the state agreements first (timeline, "By November 2028").
- **Rail.** A state that will not sponsor a corridor can be bypassed: cities, compacts and regional commissions can sponsor corridors (division D). Today's program effectively requires a state DOT, because matching shares and sponsorship sit with states.
- **Tolling.** A state that does not toll a rebuilt Interstate segment gives up that revenue but loses no federal money.

## 8. Lessons the design draws on

| Lesson | Source | In the design |
| --- | --- | --- |
| A federal charging program run through 50 state plans and highway procedures stalled | NEVI [EV-MOV-014] | National auctions, payment for uptime, a lapse rule |
| Grants change and stall between selection and signing | GAO [EV-MOV-009] | Agreement deadline; scope flexibility |
| Weight-mile taxes cost about 11% to collect and are evaded at 5-11% | Oregon [EV-MOV-118] [EV-MOV-122] | Use existing filings; audits within the collection ceiling |
| Per-mile charges cost more to collect at small scale | Utah, Oregon [EV-MOV-120] [EV-MOV-118] | Registration-based odometer reading; a ceiling reviewed by GAO |
| Relief money filled transit's fare gap only for a time | CRS, GAO [EV-MOV-103] [EV-MOV-128] | A standing operating tier with maintenance of effort |

## Questions this section leaves open

None is for Espen now. They are things to study in implementation:
- the audit rate for the weight-distance charge;
- whether the collection-cost ceiling binds in the first years;
- whether FRA's and FTA's delivery capacity grants are enough.
