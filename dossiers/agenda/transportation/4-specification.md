# Moving America: specification

Role: section 4 of the transportation dossier. It writes the Moving America design as provisions: what each does, its parameters, who pays and who receives, the vehicle, the agency, how it changes current law, and the evidence it rests on. Provision IDs and their fields are in `provisions.json` (82 provisions). Status: draft (stage C, step 7, PR 3). Espen decided every memo (1 to 6) and all eight points in `3-design.md` as recommended (`DEC-2026-11-10-08`), so every provision is decided unless its status says `chosen (drafting detail)`: pure drafting detail that no memo or point weighed. Where Draft 2 and the decisions differ, the decisions govern and the provision says so ("What the decisions changed" below). Costs: each provision's `cost_source` points to `6-cost.md` (PR 3, in progress) and gives the model figure where Draft 2 has one. Draft 2's figures are the project's estimates (grade D), not a JCT or CBO score [EV-MOV-200].

## How to read this section

- **Status of each provision.** *Decided* means Espen decided the design in `DEC-2026-11-10-08` (a memo option or a point). *Chosen (drafting detail)* means it is carried from the legacy bill as a working choice that no memo or point weighed (`DEC-2026-10-30-02`). Nothing here is pending or open for Espen; parameters that rest on judgment say so, and "a working choice" marks one this section sets so the draft is complete.
- **The drafting base.** The legacy bill (`legacy/domains/transportation-moving-america-act-2031-draft-2.md`, "Draft 2") governs where its sources disagree. Draft 2 drafts the statutory text of division A in full, divisions B to D in part (division B's title I is H.R. 8870's, by reference; division C titles II and III and secs. 401, 606, 706, 717; division D title I and sec. 303) and specifies the rest. The drafted text, and the American Transit Renewal Act (ATRA) and American Rail Competitiveness Act (ARCA) it merged, are the drafting base by reference for the later L4 work. This section states the parameters that matter, not the text.
- **Four vehicles, each carrying only what it can legally carry.** Reconciliation carries revenue and general-fund grants "to carry out" existing programs, with obligation and expenditure deadlines; it cannot carry contract authority, a transfer into a trust fund, or program design (Byrd rule). So revenue and the money that must not wait are in the two reconciliation acts; programs, contract authority within receipts, expansion appropriations, shares from FY2037, continuation, the solvency backstop and privacy are in the 60-vote 2031 bill.
- **Dates.** Calendar and fiscal years are the plan's targets. The plan begins in January 2029 (`DEC-2026-10-29-01`); the 2028 extension is a labeled 2027-28 exception. Amounts are nominal and were not re-indexed when the calendar moved a year (A-5). "FY2032-36" is the bill's window; the next bill is FY2037-41.
- **The baseline in 2029** is not settled (`3-design.md`). Three cases are plausible: (1) a five-year law through FY2031, as Draft 2 assumed (H.R. 8870, "this project's forecast, not law"); (2) short extensions through 2028; (3) a lapse on Oct 1, 2028. The two reconciliation acts work in every case; the 2031 bill's timing does not, which is why MOV-31.90 writes the contingency.
- **Shared rules** (privacy, verification) are in one place: "Shared rules kept in one place" below and MOV-31.11.
- **Evidence.** The last column of each table lists the evidence IDs the provision's parameters rest on. Most parameters are the legacy design's own choices and arithmetic, so their evidence is the project-estimate entries (EV-MOV-200 to 226). Where a parameter is a drafting detail with no entry, the column says so.

## The four vehicles

| Vehicle | Votes | When | What it carries | Money |
| --- | --- | --- | --- | --- |
| 2028 extension (MOV-28), a 2027-28 exception | 60 | by Sept 30, 2028 | Fuel taxes and fund credits extended one year, to Sept 30, 2029; heavy-vehicle use tax to Sept 30, 2030; a general-fund transfer that keeps both accounts solvent through FY2031 | Transfer not yet sized |
| 2029 reconciliation act (MOV-29, vehicle R1) | 51 | 2029; passes partway through FY2029; fuel rates from Oct 1, 2029 | Creates the three-account fund; fuel taxes permanent, indexed and stepped; clean-vehicle per-mile charge and permanent truck excises; EV fee as a one-year bridge; package one; renewal top-ups for FY2032-34 and FY2035 highway and transit | $47.0B package, $209.74B top-ups; net deficit reduction about $33.3B |
| 2030 reconciliation act (MOV-30, vehicle R3) | 51 | 2030, before the midterms; rates from Oct 1, 2030 and Oct 1, 2031 | Weight-distance charge replacing the heavy-vehicle use tax; rail diesel tax; aviation surcharge; package two; renewal top-ups for FY2035 rail and FY2036 | $33.5B package, $57.33B top-ups; net deficit reduction about $4.2B |
| Moving America Act of 2031 (MOV-31) | 60 | effective Oct 1, 2031 | Divisions A-F: programs, contract authority within receipts, expansion appropriations, shares from FY2037, continuation, solvency backstop, privacy | $936.57B authorized |

R1 and R3 are the plan's reconciliation labels (housing rides R2, `dossiers/home/4-specification.md`). Both budget resolutions instruct Ways and Means and Finance as well as the program committees, and the instruction is sized to the net score. Divisions: A Surface Transportation Trust Fund and Revenue (Ways and Means; Finance); B Federal-Aid Highways and Highway Safety; C public transportation (ATRA); D intercity passenger rail (ARCA); E Research, Data and Project Delivery; F Budget Discipline and General Provisions. The plan's size as chosen is $936.57B over FY2032-36, with dedicated receipts of $545.84B and the general fund paying $390.73B, or 0.180% of GDP a year, falling to 0.026% by FY2042-46 [EV-MOV-200].

## The 2028 extension (MOV-28)

One provision. It keeps 2029's forcing event (an expiring tax base to reform, not merely rates to raise) and buys time for the cash-flow model that sizes the transfer.

| ID | Provision | Key parameters | Agency | Evidence |
| --- | --- | --- | --- | --- |
| MOV-28.01 | The 2028 extension: rates and fund credits for one more year, with a transfer keeping both accounts solvent through FY2031 (a 2027-28 exception) | Rates and fund credits to Sept 30, 2029; use tax to Sept 30, 2030; general-fund transfer through FY2031 (not yet sized); no change to the 2.86-cent Mass Transit rate; no merger | Treasury (IRS); DOT (the fund's accounts) | EV-MOV-001, EV-MOV-002, EV-MOV-004, EV-MOV-015, EV-MOV-016, EV-MOV-131 |

## The 2029 reconciliation act (MOV-29, vehicle R1)

Revenue first (MR1 to MR3), then the fund, then the money. A 25-mpg car's federal fuel tax goes from $88 a year to $142 in FY2032 and $225 in FY2036 [EV-MOV-201]; an electric car pays $77 a year in FY2031 and $141 in FY2036 [EV-MOV-204]. The fund's shares of new revenue are 35 / 50 / 15 through FY2036 in this act; 45 / 40 / 15 from FY2037 is in the 2031 bill (MOV-31.01), and the act does not carry it.

| ID | Provision | Key parameters | Agency | Evidence |
| --- | --- | --- | --- | --- |
| MOV-29.01 | Fuel taxes permanent and indexed, with ten 3-cent Fix-It-First steps and a gas-price pause (MR1; 2029 act) | Permanent; CPI-indexed from FY2030; ten steps of 3 cents (2029 dollars), one each Oct 1 from 2029; pause if gasoline over $4.00 (indexed) or up over 20%; a deferred step is not forfeited | Treasury (IRS); DOT | EV-MOV-016, EV-MOV-123, EV-MOV-124, EV-MOV-129, EV-MOV-134, EV-MOV-200, EV-MOV-201, EV-MOV-202, EV-MOV-203, EV-MOV-219 |
| MOV-29.02 | The fossil transition premium, FY2040-44 (A-28; MR1; enacted in 2029, scores nothing inside either window) | After the ten steps: five more steps of 2 cents (2029 dollars), FY2040-44, same pause; clean vehicles never pay; receipts follow remaining general-fund need | Treasury (IRS); DOT | EV-MOV-016, EV-MOV-200, EV-MOV-206, EV-MOV-211 |
| MOV-29.03 | The clean-vehicle per-mile charge, odometer base only (MR2; A-11; 2029 act, starts Oct 1, 2030) | Electric and fuel-cell vehicles pay the gasoline road-use rate / 40 per mile (cars), 30% of that for plug-ins, diesel rate / 6.5 for heavier; odometer readings only; no tax before Oct 1, 2030; 10% cost ceiling | Treasury (IRS); States by agreement; DOT (cost allocation study) | EV-MOV-116, EV-MOV-117, EV-MOV-119, EV-MOV-120, EV-MOV-204, EV-MOV-205 |
| MOV-29.04 | Truck and tire excises permanent, 4% for zero-emission trucks; the EV fee as a one-year bridge (MR3; 2029 act) | 12% retail truck excise and tire tax permanent; 4% for zero-emission chassis, body and tractor sold after Sept 30, 2029; EV fee into the fund for FY2030 only | Treasury (IRS); DOT | EV-MOV-001, EV-MOV-016, EV-MOV-204 |
| MOV-29.05 | The three-account fund and its shares of new revenue: 35 / 50 / 15 (2029 act); 45 / 40 / 15 from FY2037 is in the 2031 bill (MOV-31.01) | Surface Transportation Trust Fund with Highway, Mass Transit and Intercity Passenger Rail Accounts; FY2028 base indexed and credited first; new revenue 35 / 50 / 15 through FY2036; renewal first | Treasury; DOT | EV-MOV-004, EV-MOV-131, EV-MOV-200, EV-MOV-211 |
| MOV-29.06 | Package one, rail: $35.00B (2029 act) | RRIF subsidy $6.00B; zero-emission rail $9.00B; state-of-good-repair backlog $8.00B; long-distance fleet $5.50B; Corridor ID $3.50B; station access and ADA $3.00B | DOT (FRA, Amtrak grants); Treasury for credit | EV-MOV-106, EV-MOV-107, EV-MOV-108, EV-MOV-110, EV-MOV-217, EV-MOV-222 |
| MOV-29.07 | Package one, transit: $12.00B (2029 act) | Operating transition grants $4.00B; shovel-ready backlog $4.00B; bus and railcar replacement $3.00B; TIFIA subsidy $1.00B | DOT (FTA) | EV-MOV-002, EV-MOV-100, EV-MOV-103, EV-MOV-104, EV-MOV-105, EV-MOV-128 |
| MOV-29.08 | Renewal top-ups for FY2032-34, plus FY2035 highway and transit: $209.74B, with their deadlines (A-14, A-15; 2029 act) | General-fund appropriations to formula programs; highway FY2032-35 $112.94B, transit FY2032-35 $36.69B, rail FY2032-34 $60.11B; obligated by Sept 30, 2036, spent by Sept 30, 2038 | DOT (FHWA, FTA, FRA); Amtrak | EV-MOV-002, EV-MOV-015, EV-MOV-131, EV-MOV-200, EV-MOV-218 |
| MOV-29.09 | The obligation ramp for both packages over FY2029-31 (A-16) | Rail $6.0B / 17.0 / 25.5 and transit $4.0B / 13.0 / 15.0 across both packages (FY2029 / 2030 / 2031); every package line obligated by Sept 30, 2031 | DOT (FTA, FRA) | EV-MOV-001, EV-MOV-217, EV-MOV-200 |
| MOV-29.10 | Scoring convention for the new excises: the 25% income and payroll tax offset (MR6) | Net revenue = gross less a 25% income and payroll tax offset: +$290.0B net of +$386.7B gross (2029 act); +$95.0B net of +$126.7B (2030 act) | JCT, CBO (scoring); Treasury | EV-MOV-200, EV-MOV-218 |

## The 2030 reconciliation act (MOV-30, vehicle R3)

The heaviest vehicles and the railroads and airlines begin to pay. Rail diesel and the aviation surcharge are rail's only dedicated receipts outside the split, $36.2B in FY2032-36 [EV-MOV-208]. The weight-distance charge replaces a use tax that has been flat at $550 and unindexed since 1984 [EV-MOV-209].

| ID | Provision | Key parameters | Agency | Evidence |
| --- | --- | --- | --- | --- |
| MOV-30.01 | A weight-distance charge for trucks over 26,000 lb, replacing the heavy-vehicle use tax (MR4; A-12; 2030 act, starts Oct 1, 2030) | Per mile on U.S. public highways: 0.8 cent to 3.4 cents plus 0.4 cent per 2,000 lb over 80,000; about a 3-cent average on Class 7-8 miles; from IFTA records interstate carriers already file; intrastate carriers once a year on the annual return that replaces the use tax (section 5) | Treasury (IRS); States (IFTA agreements) | EV-MOV-118, EV-MOV-121, EV-MOV-122, EV-MOV-207, EV-MOV-209 |
| MOV-30.02 | Rail diesel tax by Surface Transportation Board class (MR5; A-13; 2030 act) | Class I / Class II: 10 / 5 cents from Oct 1, 2030, 15 / 7.5 cents from Oct 1, 2031; zero for Class III and for intercity or commuter passenger trains; credited to the Rail Account | Treasury (IRS); Surface Transportation Board (class) | EV-MOV-208, EV-MOV-222 |
| MOV-30.03 | The aviation segment surcharge: $4 in FY2032 rising to $16 (MR5; A-13; 2030 act) | Per domestic segment beginning after Sept 30, 2031: $4 in FY2032, +$2 a year to $12 in FY2036, then +$0.40 a year, capped at $16; credited to the Rail Account; the corridor surcharge is dropped | Treasury (IRS) | EV-MOV-208 |
| MOV-30.04 | Package two, rail: $13.50B (2030 act) | RRIF second tranche $4.00B; grade crossing elimination $4.00B; electrification second tranche $3.00B; workforce and domestic supplier base $2.50B | DOT (FRA); Treasury for credit | EV-MOV-106, EV-MOV-110, EV-MOV-217, EV-MOV-222 |
| MOV-30.05 | Package two, transit: $20.00B (2030 act) | Operating transition $5.00B; state of good repair $6.00B; bus replacement $1.00B; station accessibility $3.00B; CIG $3.00B; TIFIA $1.00B; workforce and FTA capacity $1.00B | DOT (FTA) | EV-MOV-100, EV-MOV-103, EV-MOV-112, EV-MOV-113, EV-MOV-128 |
| MOV-30.06 | Renewal top-ups for FY2035 rail and FY2036: $57.33B, with their deadlines (A-14, A-15; 2030 act) | General-fund appropriations to formula programs; FY2036 highway $26.99B and rail $13.69B, FY2035 rail $16.65B; obligated by Sept 30, 2037, spent by Sept 30, 2039 | DOT (FHWA, FRA); Amtrak | EV-MOV-200, EV-MOV-218 |

## The Moving America Act of 2031 (MOV-31)

The bill authorizes $936.57B across divisions B to D: $812.87B of renewal and $123.70B of expansion; by division $461.12B (B), $221.42B (C) and $254.03B (D), plus about $1.0B of division E [EV-MOV-200]. It takes effect Oct 1, 2031 (MOV-31.89). Under baseline cases 2 and 3 it is the renewal of the contingency authorization (MOV-31.90).

### Division A: Surface Transportation Trust Fund and Revenue (MOV-31.01 to MOV-31.11)

Secs. 102 to 104 are enacted by the reconciliation acts (MOV-29 and MOV-30). The 2031 bill **cross-refers** to them (MOV-31.02 to MOV-31.04): it prints no second tax and re-enacts no rate, and adds what reconciliation cannot carry (privacy, State coordination). Sec. 101 is the same: the 2031 bill cross-refers to the act's text and adds the FY2037 shares, the 9503(e)(3) amendment and the reset report (MOV-31.01). Draft 2 does not say which of restating or cross-referring it means; cross-referring avoids two texts of one tax and is a working choice.

| ID | Provision | Key parameters | Agency | Evidence |
| --- | --- | --- | --- | --- |
| MOV-31.01 | Division A sec. 101: the fund and shares restated, with the FY2037 shares 45 / 40 / 15 added (cross-refers to MOV-29.05) | Restates the 2029 act's fund (cross-reference, no new tax); adds 45 / 40 / 15 from FY2037 unless a later Act provides otherwise, the 9503(e)(3) fix, and the 18-month reset report | Treasury; DOT | EV-MOV-004, EV-MOV-200, EV-MOV-211 |
| MOV-31.02 | Division A sec. 102: the clean-vehicle road user charge (cross-reference to MOV-29.03) | Revenue already law from the 2029 act; the 2031 bill cross-refers and adds only sec. 111's privacy rules and the sec. 1108 coordination with State registration | Treasury; States | EV-MOV-204 |
| MOV-31.03 | Division A sec. 103: fuel taxes, steps, the premium and the EV-fee bridge (cross-reference to MOV-29.01, .02, .04) | Revenue already law from the 2029 act ($426.7B FY2032-36); cross-reference only | Treasury; DOT | EV-MOV-200 |
| MOV-31.04 | Division A sec. 104: truck and rail taxes (cross-reference to MOV-29.04, MOV-30.01 to .03) | Excises law from the 2029 act; weight-distance charge, rail diesel and aviation surcharge law from the 2030 act ($35.8B + $36.2B FY2032-36); cross-reference only | Treasury | EV-MOV-208, EV-MOV-209 |
| MOV-31.05 | Division A sec. 105: mandatory appropriations for expansion, $123.70B | CIG $27.50B; sec. 606 $3.00B; sec. 303 $55.00B; sec. 310 $20.20B; sec. 311 $6.00B; sec. 312 $12.00B = $123.70B, FY2032-36, available until expended | DOT (FTA, FRA) | EV-MOV-112, EV-MOV-200, EV-MOV-222, EV-MOV-224 |
| MOV-31.06 | Division A sec. 106: contract authority, contingent commitments, and the readiness reserve of up to $25.00B | Divisions B-D available on enactment or Oct 1, until expended; limitation below 90% cuts expansion first; commitments to FY2046 at most 60% a year; reserve up to $25.00B released at gates | DOT; Treasury | EV-MOV-222, EV-MOV-224, EV-MOV-225, EV-MOV-200 |
| MOV-31.07 | Division A sec. 107: continuation of renewal programs if the authorizations lapse | Renewal programs continue at FY2036 levels adjusted for inflation; expansion excluded; direct spending; $34.44B of rail renewal in FY2036 | DOT | EV-MOV-001, EV-MOV-131, EV-MOV-222 |
| MOV-31.08 | Division A sec. 108: the annual report and the capped $25B solvency backstop; the 0.206% benchmark is a published comparison, not a trigger (memo 3) | Annual joint Treasury-CBO report with the 0.206% comparison (no trigger); backstop restores 25% of next year's obligations, at most $25B in total for FY2032-36 | Treasury; CBO; DOT | EV-MOV-200, EV-MOV-213, EV-MOV-219 |
| MOV-31.09 | Division A sec. 109: joint facilities, attributed by train movements | Mass Transit, Rail and sec. 310 amounts attributed by share of train movements (method of 49 U.S.C. 5309(q)(4)); sec. 310 pays only the intercity share | DOT (FTA, FRA) | EV-MOV-222 |
| MOV-31.10 | Division A sec. 110: contract authority within receipts; coordination with the top-ups ($267.07B) | Each account's authority capped at projected receipts plus unobligated balance; top-ups of $209.74B (2029 act) and $57.33B (2030 act) distributed among programs; a general-fund fallback if the top-ups are not enacted | Treasury; DOT | EV-MOV-002, EV-MOV-200, EV-MOV-218 |
| MOV-31.11 | Division A sec. 111: privacy and administration of the road user charges (odometer only) | No location, route, time or manner data; no device; readings are return information (6103), never sold, destroyed within 3 years; remedies under 7431; GAO review by Sept 30, 2033 and every 3 years | Treasury (IRS); States; GAO | EV-MOV-116, EV-MOV-117, EV-MOV-119, EV-MOV-120, EV-MOV-204 |

### Division B: Federal-Aid Highways and Highway Safety (MOV-31.20 to MOV-31.39)

$461.12B: $418.28B FHWA (H.R. 8870 title I continued at 2.5% a year), $30.77B Interstate and Bridge Renewal and $12.07B NHTSA and FMCSA, plus $17.24B of general-fund grants subject to appropriation (sec. 1112) outside the total. Ten sections are drafted (1101, 1104, 1105, 1106, 1109, 1110, 1112, 1113, 1114, 1116) and the rest are specified; the specified ones are grouped below. Memo 5 changed sec. 1106 and memo 3 changed sec. 1112.

| ID | Provision | Key parameters | Agency | Evidence |
| --- | --- | --- | --- | --- |
| MOV-31.20 | Division B sec. 1101: highway authorizations, $418.28B (H.R. 8870 title I continued at 2.5% a year) | FHWA programs $79.58B / 81.57 / 83.60 / 85.69 / 87.84 = $418.28B, FY2032-36; limitation $80.971B in FY2032 rising to $97.377B; the rest of title I (about $40.6B) continues | DOT (FHWA) | EV-MOV-001, EV-MOV-003, EV-MOV-005, EV-MOV-008, EV-MOV-132, EV-MOV-133, EV-MOV-200 |
| MOV-31.21 | Division B secs. 1102 and 1103: apportioned formula programs and the bridge formula program (specified, not drafted) | Formula programs at H.R. 8870 shares: about $325.5B, within sec. 1101 after the sec. 1116 set-aside; bridge formula on contract authority about $49.6B, $75M State floor | DOT (FHWA) | EV-MOV-005, EV-MOV-006, EV-MOV-018 |
| MOV-31.22 | Division B sec. 1104: Interstate and Bridge Renewal, $30.77B (A-23) | Converted bridge program $10.77B plus new money $0 / 2 / 4 / 6 / 8B = $30.77B; 80% formula, 20% large projects over $500M; federal share 90%; tolling allowed on reconstructed segments | DOT (FHWA) | EV-MOV-006, EV-MOV-010, EV-MOV-018, EV-MOV-212 |
| MOV-31.23 | Division B sec. 1105: renewal classification | Every Highway Account program, sec. 1104 included, is a renewal program for secs. 101(f), 107 and 108 | DOT (FHWA) | EV-MOV-200 |
| MOV-31.24 | Division B sec. 1106: fix-it-first as published reports and a review, with the lower federal share for new lanes (memo 5 option B) | 70% federal share (Interstate 80%) for new general-purpose lanes kept; condition trends and lifecycle analyses (projects $100M or more) published; FHWA reviews a state whose condition falls two years in a row and agrees a repair plan | DOT (FHWA) | EV-MOV-017, EV-MOV-114, EV-MOV-115, EV-MOV-214 |
| MOV-31.25 | Division B sec. 1109: Safe System (A-25) | SS4A planning reservation 15%; HSIP limited to proven countermeasures where targets regress; State with vulnerable-user deaths of 15% or more spends at least that share of HSIP on them | DOT (FHWA, NHTSA) | EV-MOV-007, EV-MOV-126, EV-MOV-127 |
| MOV-31.26 | Division B sec. 1110: resilience, carbon reduction and clean fuels set-asides (A-26) | 4% of NHPP for resilience (about $1.4B a year); Carbon Reduction Program restored as 2% of each State's formula money; CMAQ alternative-fuel minimum held at 10% | DOT (FHWA) | EV-MOV-011, EV-MOV-215 |
| MOV-31.27 | Division B sec. 1112: general-fund grants for multimodal freight and National Infrastructure Grants, $17.24B, reported and not counted against a benchmark (memo 3) | Authorized to be appropriated: $1.23B (23 U.S.C. 117) and $2.05B (sec. [7105]) in FY2032, each grown 2.5% a year = $17.24B, subject to appropriation; reported, not counted against 0.206% | DOT (FHWA, Office of the Secretary) | EV-MOV-001, EV-MOV-213 |
| MOV-31.28 | Division B sec. 1113: truck parking | 15% of each State's freight formula apportionment for truck parking unless it certifies that needs on the national freight network are met; about $0.28B a year on top of $0.15B competitive | DOT (FHWA, FMCSA) | EV-MOV-215 |
| MOV-31.29 | Division B sec. 1114: truck size and weight; the 91,000-lb pilot ends in 2031 | H.R. 8870's 91,000-lb pilot ends Sept 30, 2031 and is not extended; Secretary's report by Sept 30, 2033, including the rate that would recover cost | DOT (FHWA) | EV-MOV-209 |
| MOV-31.30 | Division B sec. 1116: the Charging Gap Program replaces NEVI (A-27) | $0.5B in FY2032 growing 2.5% a year = $2.63B from formula money; national reverse auctions on a published gap map; half paid at energization, half over 5 years for 97% uptime; 24 months to energize | DOT (FHWA, Joint Office) | EV-MOV-014, EV-MOV-216 |
| MOV-31.31 | Division B secs. 1107, 1108 and 1111: multimodal flexibility, State coordination of the road user charge, delivery and unit-cost reporting (specified) | STBG and CMAQ may pay for transit and intercity rail capital and a State's share of a joint facility; one registration transaction for State and federal charge; unit costs for projects over $100M | DOT (FHWA) | none (drafting detail) |
| MOV-31.32 | Division B sec. 1115: local access and suballocation (A-25) | STBG suballocation by population raised from 55% to 60%; 1% of the amount for rural planning organizations; consolidated pilot 30% not 25%; metropolitan planning organizations keep direct-recipient option | DOT (FHWA) | EV-MOV-012 |
| MOV-31.33 | Division B secs. 1201 and 1301: NHTSA and FMCSA at H.R. 8870 levels, grown, $12.07B | NHTSA and FMCSA $2.29B / 2.35 / 2.42 / 2.48 / 2.53 = $12.07B (roughly $6.4B NHTSA and $5.7B FMCSA); programs carried forward | DOT (NHTSA, FMCSA) | EV-MOV-007 |

### Division C: Public Transportation (MOV-31.40 to MOV-31.59)

$221.42B: $190.92B of renewal from the Mass Transit Account and $30.50B of expansion (CIG $27.50B, sec. 606 $3.00B) [EV-MOV-200]. By title: II operating tier $35.00B; III state of good repair $63.03B; IV CIG $27.50B; V workforce $2.85B; VI formula capital $88.30B (of which sec. 606 is $3.00B); VII delivery and authorizations $4.74B. Memo 4 changed title II. Specified, not drafted: secs. 402-407, 501-506, 601-605, 607-608 and 701-705.

| ID | Provision | Key parameters | Agency | Evidence |
| --- | --- | --- | --- | --- |
| MOV-31.40 | Division C title II: transit operating help, the new 5307(i) tier, $35.00B (memo 4 option D) | $6.0B rising to $8.0B a year for areas of 200,000 or more; 50% revenue hours, 30% trips, 20% low-income residents; capped at 25% of net operating cost; conditions: maintenance of effort, 95% service floor, no outstanding 5326(e) direction; two accounting tests become published reports, which also give paratransit trips and service area | DOT (FTA) | EV-MOV-100, EV-MOV-101, EV-MOV-102, EV-MOV-103, EV-MOV-128, EV-MOV-210, EV-MOV-220, EV-MOV-221 |
| MOV-31.41 | Division C title III: state of good repair formula, asset management enforcement and transit resilience ($31.50B) | 5337 formula $28.00B (80% federal share); 5326(e) asset management $0.50B at 100%; transit resilience $3.00B at 80%; four date corrections | DOT (FTA) | EV-MOV-104, EV-MOV-105, EV-MOV-200 |
| MOV-31.42 | Division C sec. 302: the 5337(g) backlog retirement schedule, $31.53B over a 20-year schedule | $6.00B / 6.15 / 6.30 / 6.46 / 6.62 = $31.53B; each recipient obligates at least 1/20 of its baseline backlog a year from FY2032; retired in FY2051; 80% federal share | DOT (FTA) | EV-MOV-104, EV-MOV-105 |
| MOV-31.43 | Division C title IV sec. 401: Capital Investment Grants, $27.50B, obligated in full at signing | $4.5B / 5.0 / 5.5 / 6.0 / 6.5 = $27.50B from sec. 105(a)(1); a full funding grant agreement obligates the whole federal share when signed; commitments to FY2046 at most 60% of the FY2036 amount a year | DOT (FTA) | EV-MOV-112, EV-MOV-113, EV-MOV-200 |
| MOV-31.44 | Division C secs. 402-407: CIG delivery reforms (specified, not drafted) | Warrants as default; match categories A-E (C and D capped at 40%); FTA decides in 120 days; gates for projects over $1B; one application for joint projects; unit-cost review | DOT (FTA) | EV-MOV-112, EV-MOV-113 |
| MOV-31.45 | Division C title V: labor and workforce, $2.85B (specified, not drafted) | Apprenticeships $1.60B; frontline training set-aside 1% of 5307 and 5337 apportionments $0.75B; operator safety $0.40B; Workforce Development Center $0.10B; 5333(b) unchanged | DOT (FTA); Labor | none (drafting detail) |
| MOV-31.46 | Division C title VI: formula capital, buses, rural, seniors and disabilities, accessibility, ferries and emergency relief, $85.30B | Urbanized formula 5307/5340 $54.10B; buses 5339 $14.00B; rural 5311 $7.50B; seniors and disabilities 5310 $3.20B; All Stations Accessibility $5.00B; ferries $1.00B; emergency relief $0.50B | DOT (FTA) | EV-MOV-104, EV-MOV-200 |
| MOV-31.47 | Division C sec. 606: joint facilities outside the five sec. 310 nodes, $3.00B (A-6) | $0.60B a year from sec. 105(a)(2); pays only the transit-attributed share (sec. 109(a)), at most 80% of that share; one combined application with division D | DOT (FTA, FRA) | EV-MOV-222 |
| MOV-31.48 | Division C title VII secs. 701-705: planning, FTA capacity, safety, research and delivery, $4.74B | Planning $1.55B; FTA administration and staffing $1.05B; safety oversight and NTD $0.55B; research, technical assistance and bus testing $0.80B; cost benchmarking and owner-side engineering $0.79B | DOT (FTA) | EV-MOV-125 |
| MOV-31.49 | Division C sec. 706: Buy America for jointly funded rolling stock | Division D sec. 1201's domestic content and final assembly apply in lieu of 5323(j)(2)(C) | DOT (FTA, FRA) | none (drafting detail) |
| MOV-31.50 | Division C sec. 717: the transit authorizations by program name, $190.92B | Rewrites 5338(a)(2) whole, FY2032-36, from the Mass Transit Account: $190.92B renewal; cites programs by name; subject to sec. 110(a) | DOT (FTA) | EV-MOV-001, EV-MOV-200 |

### Division D: Intercity Passenger Rail (MOV-31.60 to MOV-31.79)

$254.03B plus up to $25.00B of readiness reserve, contingent: $160.83B of renewal from the Rail Account and $93.20B of expansion (secs. 303, 310, 311, 312) [EV-MOV-222]. By title: II core network $59.95B; III corridor development $160.45B ($67.25B renewal, $93.20B expansion); IV to XIII $33.63B [EV-MOV-223]. Sec. 303 (the Tier 1 program), sec. 310 (terminals) and sec. 401 (the tranche gates) are provisions of their own because they carry the most money and the most risk. Memo 6 kept the design as chosen: dollars-capped corridors, a reserve released at gates, one terminal program.

| ID | Provision | Key parameters | Agency | Evidence |
| --- | --- | --- | --- | --- |
| MOV-31.60 | Division D title I: the Intercity Passenger Rail Account and its subaccounts | Rail Account is the source of contract authority; subaccounts Core Network, Corridor Development, High-Speed Rail, Credit, Commission; no separate trust fund; the corridor surcharge is dropped | DOT (FRA); Treasury | EV-MOV-208, EV-MOV-222, EV-MOV-223 |
| MOV-31.61 | Division D title II: the core network, $59.95B | NEC base grant $10.00B; NEC Capital Program $17.00B; National Network operating $11.00B; long-distance preservation $4.70B; National Fleet Program $13.10B; stations and ADA $4.15B | DOT (FRA); Amtrak | EV-MOV-106, EV-MOV-107, EV-MOV-223 |
| MOV-31.62 | Division D title III renewal sections: Corridor ID, intercity capital for Tier 2-3, CRISI, grade crossings and safety ($67.25B) | Corridor ID $2.50B; Tier 2-3 capital $38.00B (45% formula, 55% competitive); CRISI $12.50B; grade crossings $12.50B; safety implementation $1.75B | DOT (FRA) | EV-MOV-108, EV-MOV-109, EV-MOV-225 |
| MOV-31.63 | Division D sec. 303: the National High-Speed Rail Program (Tier 1), $55.00B, with the $14.0B corridor cap (A-21) | $55.00B FY2032-36 (6.0 / 9.0 / 11.0 / 13.5 / 15.5); federal share at most 50%; no project under $1B; at most $14.0B a corridor ($19.25B with the reserve); entry gates | DOT (FRA) | EV-MOV-108, EV-MOV-130, EV-MOV-222, EV-MOV-224, EV-MOV-225 |
| MOV-31.64 | Division D sec. 310: terminals of national significance, $20.20B for five nodes (A-6) | Chicago Union Station and CREATE $9.0B; New York Penn and Sunnyside $4.0B; Washington Union Station $3.5B; Los Angeles Union Station $0.7B; Atlanta $3.0B = $20.20B; pays only the intercity share | DOT (FRA, FTA) | EV-MOV-222 |
| MOV-31.65 | Division D secs. 311 and 312: federally initiated corridors ($6.00B) and long-distance network implementation ($12.00B) | Sec. 311 $6.00B (at most 14 designations in FY2032-36; 100% federal through preliminary engineering and environmental review); sec. 312 $12.00B first tranche for five long-distance options | DOT (FRA) | EV-MOV-109, EV-MOV-110, EV-MOV-111, EV-MOV-222 |
| MOV-31.66 | Division D sec. 401: tranche gates for the larger rail projects | Four tranches of at most 25% each for projects with a federal share over $300M; tranches 2-4 need independent certification; gates on match, rolling stock, forecasts, cost and schedule; 90-day decision | DOT (FRA) | EV-MOV-130, EV-MOV-225 |
| MOV-31.67 | Division D title IV secs. 402-407: independent review, match rules, variance reporting, cure and funding certainty ($1.33B) | Office of Rail Project Delivery; independent reviewers; match categories A-E (C and D together at most 40%); quarterly posting for projects over $300M; deobligated money to the competitive pool; executed agreements protected | DOT (FRA) | EV-MOV-009, EV-MOV-130 |
| MOV-31.68 | Division D title V: regional corridor commissions, $1.00B, and labor continuity | Five commissions at $40M a year each = $1.00B (Northeast, Southeast, Cascadia, Midwest Hub, Texas Triangle); advance consent to interstate rail compacts; collective bargaining continues through any Amtrak reorganization | DOT (FRA) | EV-MOV-109 |
| MOV-31.69 | Division D title VI: access, operations and ticketing, $0.85B | Preference enforcement (delay presumed when on-time performance is under 80% for two quarters; $25,000 a day; 240-day decision) $0.125B; access covenants and dispatching grants $0.64B; on-time standards $0.085B | DOT (FRA); Surface Transportation Board | none (drafting detail) |
| MOV-31.70 | Division D title VII: industrial base, workforce and project delivery, $3.95B | Rolling-stock manufacturing capacity grants $1.75B; workforce $1.75B; Buy America transition assistance $0.45B; standard specifications, cost benchmarking, standard designs, delivery methods and utility relocation within the total | DOT (FRA) | EV-MOV-125, EV-MOV-130 |
| MOV-31.71 | Division D title VIII: credit, $5.00B | $1.00B a year: credit risk premium for public borrowers (ARCA $3.3B), interest-rate buy-down (ARCA $1.25B); 75-year terms; 180-day decision; master credit agreements | DOT (FRA, Build America Bureau) | EV-MOV-222 |
| MOV-31.72 | Division D title IX: permitting parity, $0.50B | Endangered Species Act and categorical exclusion parity for work within existing operating rail right-of-way; Section 4(f) alignment; Coast Guard and Corps clocks; judicial review parity; $0.3B national programmatic review | DOT (FRA); Interior; Army Corps; Coast Guard | EV-MOV-225 |
| MOV-31.73 | Division D title X: operating support for state-supported corridors, $8.00B | $0.80B / 1.20 / 1.60 / 2.00 / 2.40 = $8.00B contract authority from the Rail Account (renewal); 6-year grants become 10 with one 5-year renewal; federal share 90% falling to 50% | DOT (FRA) | EV-MOV-106, EV-MOV-107 |
| MOV-31.74 | Division D title XI: access, competition and structure, $1.50B | Designated corridor operators share Amtrak's access rights; a competitive operator pilot raised to eight routes; NEC cost allocation extended to funded corridors; dedicated passenger track presumptive for Tier 1 and 2; vertical separation not pursued | DOT (FRA); Surface Transportation Board | none (drafting detail) |
| MOV-31.75 | Division D title XII: the National Passenger Rail Equipment Pool, $8.50B | $8.00B pool plus $0.50B FRA testing and certification; at most six equipment families; leases by useful life; Tier III rule within 18 months | DOT (FRA) | none (drafting detail) |
| MOV-31.76 | Division D title XIII: the night network, $3.00B | $0.40B / 0.60 / 0.70 / 0.70 / 0.60 = $3.00B; one ticket (no new money); station value capture (authority); an airline bargain (authority) | DOT (FRA) | none (drafting detail) |

### Division E: Research, Data and Project Delivery (MOV-31.80 to MOV-31.84)

About $1.0B, specified, outside the fiscal model and outside the $936.57B: secs. 101 and 107 $0.25B, sec. 102 $0.15B, sec. 103 $0.10B, sec. 106 $0.50B; secs. 104 and 105 are policy.

| ID | Provision | Key parameters | Agency | Evidence |
| --- | --- | --- | --- | --- |
| MOV-31.80 | Division E secs. 101 and 107: the national intercity travel forecast and multi-area apportionment data ($0.25B) | Forecast of intercity passenger travel, all modes, every five years $0.10B; BTS and National Transit Database multi-area apportionment data published with each apportionment $0.15B | DOT (BTS, FTA) | none (drafting detail) |
| MOV-31.81 | Division E sec. 102: one public unit-cost database for projects over $100M ($0.15B) | Highway, transit and rail projects over $100M report unit costs to one database fed by div. B secs. 1106(d) and 1111, div. C sec. 705 and div. D sec. 705 | DOT | EV-MOV-125 |
| MOV-31.82 | Division E sec. 103: evaluation of the road user charges ($0.10B) | Yearly report to the tax committees on collection cost, evasion, privacy compliance and rural and income incidence of the 4491 and 4495 charges; complements GAO's review under 4494(d) | DOT; Treasury; GAO | EV-MOV-118, EV-MOV-120, EV-MOV-122 |
| MOV-31.83 | Division E secs. 104 and 105: the grant pipeline and permitting parity (policy) | Agreement executed within 180 days of selection or the Secretary reports why; pre-award authority; scope changes within 10% without reselection; executed agreements protected; Coast Guard and Corps 408 clocks for transit and highway bridges | DOT (all modes) | EV-MOV-009 |
| MOV-31.84 | Division E sec. 106: owner-side engineering and delivery capacity grants ($0.50B) | Grants to State DOTs and transit agencies to hire owner-side engineers, matching division D sec. 707 | DOT | EV-MOV-125 |

### Division F: Budget Discipline and General Provisions (MOV-31.85 to MOV-31.89)

No money; specified.

| ID | Provision | Key parameters | Agency | Evidence |
| --- | --- | --- | --- | --- |
| MOV-31.85 | Division F sec. 101: cross-references cite programs by name, not by letter | References to 49 U.S.C. 5338(a) and 23 U.S.C. 104 cite programs by name so a later relettering cannot misdirect money | DOT; Office of Legislative Counsel | none (drafting detail) |
| MOV-31.86 | Division F sec. 104: reconciliation money counts toward a program's FY2032-36 baseline only where obligated | Money obligated in FY2029-31 counts toward a program's FY2032-36 baseline only where obligated; top-ups are not double counted in the sec. 108 report | DOT; Treasury | EV-MOV-217 |
| MOV-31.87 | Division F sec. 102: Buy America for jointly funded rolling stock | The equipment pool's standard (division D sec. 1201; division C sec. 706) applies to jointly funded rolling stock; each mode's own rule elsewhere | DOT (FTA, FRA) | none (drafting detail) |
| MOV-31.88 | Division F sec. 103: labor protections carried through any Amtrak reorganization and to joint facilities | 49 U.S.C. 5333(b) and Railway Labor Act protections carried through any Amtrak reorganization and to joint facilities under division A sec. 109 | DOT; Labor | none (drafting detail) |
| MOV-31.89 | Division F sec. 105: effective date Oct 1, 2031, and continuation if the bill lapses | Effective Oct 1, 2031, the first day of FY2032 and the day the Corridor ID new-selection sunset falls; division A sec. 107 continuation applies if the bill lapses | DOT | EV-MOV-001 |

### The contingency authorization (MOV-31.90)

Point 1 of `3-design.md`, decided as recommended. It is the one provision that exists because of the baseline, not because Draft 2 has it.

| ID | Provision | Key parameters | Agency | Evidence |
| --- | --- | --- | --- | --- |
| MOV-31.90 | The contingency authorization: if no multi-year surface transportation law is in place by Dec 31, 2028, a regular-order authorization in 2029-30, with highway title I drafted in full | Triggered if no multi-year authorization is law by Dec 31, 2028; enacted in 2029-30 covering the years to FY2031; highway title I drafted in full, not by reference to H.R. 8870; the 2031 bill becomes its renewal | DOT | EV-MOV-001, EV-MOV-003, EV-MOV-016, EV-MOV-131 |

### Housing's condition on new money (MOV-31.91)

| ID | Provision | Key parameters | Agency | Evidence |
| --- | --- | --- | --- | --- |
| MOV-31.91 | Housing's zoning condition on new transportation money (HOU-6.02) | Applies to the bill's new and incremental money: division A sec. 105's expansion appropriations ($123.70B) and sec. 1104's new money; never the renewal formula base, the operating tier or safety money (a working choice). The share and the reforms are housing's (`dossiers/home/4-specification.md`, HOU-6.02, decided by `DEC-2026-11-09-04`) | DOT with HUD | None (a condition, no cost) |

## What the decisions changed

`DEC-2026-11-10-08` decided memos 1 to 6 and points 1 to 8 as recommended. Of these, three memos change Draft 2's text and one point adds a provision; the rest keep the legacy design as chosen. The older `DEC-2026-11-10-05` already retired the 0.206% benchmark as a design rule.

| Decision | Draft 2 said | Now | Where |
| --- | --- | --- | --- |
| Memo 3 (A): size and split | Sec. 108(b): if the projected draw exceeds 0.206% of GDP, the Secretary reports reductions or deferrals within 60 days. A-18: sec. 1112's $17.24B counts against the benchmark | Sec. 108 keeps the annual joint report and the capped $25B solvency backstop (FY2032-36). The 0.206% is a published comparison, not a trigger. Sec. 1112's grants are reported in the sec. 108(a) report and not counted against a benchmark (A-4, A-17 and A-18 superseded). Size ($936.57B), split (35 / 50 / 15, then 45 / 40 / 15) and Interstate and Bridge Renewal's new money ($0 / 2 / 4 / 6 / 8B) are unchanged; resizing by need (memo 3 B) is left to the financing settlement | MOV-31.08, MOV-31.27, MOV-31.22, MOV-29.05, MOV-31.01 |
| Memo 4 (D): transit operating help | Sec. 5307(i) with five conditions: maintenance of effort, a 95% service floor, no outstanding 5326(e) direction, a cap on the preventive-maintenance share, and a cost review (cost per vehicle revenue hour more than 1.5 points above the wage index for 3 years) | $35.00B kept, with the apportionment (50 / 30 / 20) and the 25% ceiling. Conditions (A) maintenance of effort, (B) the 95% service floor and (C) no 5326(e) direction stay. Conditions (D) and (5) become an annual published report of preventive-maintenance spending and cost per vehicle revenue hour, with an FTA review where an area's figures move sharply: a review trigger set by FTA rule (a working choice) | MOV-31.40, MOV-31.41 |
| Memo 5 (B): conditions on states | Sec. 1106: a preservation shift (50% of NHPP rising to 80%) after two failed determinations; a lifecycle certification for lane-adding projects of $100M or more; a 10-point lower federal share for new lanes | The lower share stays (70%, 80% on the Interstate). The preservation shift becomes each State's published condition trend; the lifecycle test becomes a published lifecycle analysis of each lane-adding project of $100M or more. FHWA reviews a State whose condition falls for two consecutive years and agrees a repair plan. Secs. 1109 and 1115 (A-25) stay as chosen | MOV-31.24, MOV-31.25, MOV-31.32 |
| Point 1 | (not in Draft 2) | If no multi-year authorization is law by Dec 31, 2028, a regular-order authorization in 2029-30 for the years to FY2031, with highway title I drafted in full, and the 2031 bill becomes its renewal | MOV-31.90, MOV-31.20 |
| Memos 1, 2, 6; points 2 to 8 | The legacy design | Kept as chosen: A-9 (the extension), A-10, A-11, A-28, A-12, A-13, A-6, A-21, A-22, A-14 to A-16, A-19, A-20, A-26, A-27, A-1, A-2 | the provisions named in the table above and in section 8 |

## Design lens

`DEC-2026-11-09-13` (guide, don't police): each test, filing, deadline or cap should earn its place against the burden it adds. Here the lens changes two designs and confirms two.

**Simplifications**

1. *The clean-vehicle charge reads the odometer and nothing else* (MOV-29.03, MOV-31.11). One plain test using records the government already holds at registration or inspection. It buys privacy and political support (74% backed a dedicated 10-cent maintenance increase in the Mineta Transportation Institute's 2024 survey [EV-MOV-129]; Draft 2 reads mileage fees as drawing weaker support). It costs: miles driven abroad or on private land are taxed; fraud is handled by audit, not a device; and collection cost is allowed up to 10% of collections, which is not trivial (Utah projects its program will spend 14.2% of its revenue [EV-MOV-120]).
2. *The weight-distance charge uses the mileage records carriers already file each quarter* (MOV-30.01). For interstate carriers, no new filing. Intrastate trucks file no IFTA return; they report odometer miles once a year on the annual return that replaces the heavy-vehicle use tax, which is a new line for trucks of 55,000 lb or more and a new filing for those between 26,000 and 55,000 lb (section 5). It buys low burden; it costs a collection cost near Oregon's 11% of revenue and evasion of roughly 5-11% [EV-MOV-118] [EV-MOV-122], which the yearly evaluation in MOV-31.82 reports.
3. *Memo 4: two accounting tests become one published report* (MOV-31.40). It removes two tests an agency tracked and certified each year; it gives up a hard stop on shifting capital money to operations and on cost growth, and it rests on judgment (no study of the 1998 capital-only rule's conditions is in the register).
4. *Memo 5: a preservation shift and a lifecycle gate become published reports and a review trigger* (MOV-31.24). It removes a federal approval step on large projects; it gives up a binding requirement to spend on repair first. The lower federal share for new lanes stays because it works through the money and needs no review; driving rises about one-for-one with new Interstate lane-kilometers [EV-MOV-114].

**Burdens kept, because they earn their place**

- *Maintenance of effort and the 95% service floor* (MOV-31.40): they stop federal money replacing State money and make it reach riders. Cost: two numbers each recipient reports.
- *The 5326(e) direction* (MOV-31.41): operating help should not reward a system that lets its assets decay. Cost: a corrective plan after two bad years.
- *Entry gates, tranche gates and the dollars cap on Tier 1 corridors* (MOV-31.63, MOV-31.66): high-speed rail is the largest new commitment in a country with high construction costs and a thin pipeline (three to five corridors ready at enactment [EV-MOV-225]). The gates are objective, scheduled and public, so they also protect a project from a pretext termination.
- *Uptime holdback and the 24-month lapse in the Charging Gap Program* (MOV-31.30): what should make it faster than NEVI, which obligated about $526M of its $5B by early 2025 [EV-MOV-014]. It is untested at federal scale [EV-MOV-216], so it is a thing to study in implementation.
- *The 1/20-a-year backlog obligation* (MOV-31.42): a 20-year schedule that retires the backlog. Cost: a recipient must find its share from all sources each year.
- *Annual State reporting of obligations by purpose* (MOV-31.24) and the unit-cost database (MOV-31.81): reporting, with no penalty.

## Shared rules kept in one place

Transportation has no income-tested benefit, so it relies on few of `dossiers/shared-rules.md`'s rules (`3-design.md`).

- **Rule 5, who verifies, pays and answers for mistakes.** The per-mile charges are taxes administered by the Treasury; States may collect the clean-vehicle charge at registration under agreements that remit not less than 99% within 60 days. **Privacy is sec. 111 (MOV-31.11) and every road user charge cites it:** no location, route, time or manner data and no device; readings are return information under 26 U.S.C. 6103, may not be sold, and are destroyed within 3 years; remedies under 7431; a GAO review by Sept 30, 2033 and every 3 years. **Verification** is by audit and by the records already held (registration, inspection, IFTA returns), with the yearly evaluation in MOV-31.82. The bar on location data and the retention rules cannot ride reconciliation, so they begin with the 2031 bill; readings are return information from the first day anyway.
- **Rule 8, workforce.** Construction, transit operations and rail manufacturing draw on the same workforce as housing and clean power. No transportation-specific rule; division C title V and division D title VII fund apprenticeships and capacity, and the dossier's delivery section (section 5) states the capacity need.
- **Fairness (D3, owned by the financing settlement).** Fuel taxes take a larger share of income from lower-income households. The plan-wide test is settled policy (`DEC-2026-10-30-02`); the household model checks it. Memo 1 shows the household cost.

## Consistency check

Every amount below must agree across this file, `provisions.json` and the agenda. Source: Draft 2's canonical authorization table, which governs where any other figure disagrees. The agenda rows carry names only and no amounts; MOV-29's row says "FY2032-35 renewal top-ups" and MOV-30's "FY2035-36 top-ups", which is the same split by mode as MOV-29.08 and MOV-30.06 (FY2035 highway and transit in the 2029 act, FY2035 rail in the 2030 act); those rows are not edited here.

| Amount | What it is | Where it appears | Check |
| --- | --- | --- | --- |
| $936.57B | Authorized FY2032-36, divisions B-D | vehicles table; MOV-31 overview; MOV-31.20 to MOV-31.76; `3-design.md` | 461.12 + 221.42 + 254.03 = 936.57; 812.87 renewal + 123.70 expansion |
| $461.12B / $221.42B / $254.03B | Divisions B / C / D | MOV-31 overview; MOV-31.20 to .33, .40 to .50, .60 to .76 | B: 418.28 + 30.77 + 12.07; C: 190.92 + 30.50; D: 160.83 + 93.20 |
| $812.87B / $123.70B | Renewal / expansion | MOV-31.05, MOV-31.10 | expansion 27.50 + 3.00 + 55.00 + 20.20 + 6.00 + 12.00 = 123.70 (the general-fund draw table shows $123.66B: transit receipts cover $0.04B of CIG in FY2036; $123.70B governs) |
| $545.84B | Dedicated receipts FY2032-36 | vehicles table; MOV-29.05 | highways 321.19 + transit 154.27 + rail 70.38 |
| $390.73B | General fund FY2032-36 | vehicles table; MOV-29.08, MOV-30.06, MOV-31.05 | 139.93 + 67.15 + 183.65; also 123.66 expansion + 267.07 top-ups |
| $267.07B | Renewal top-ups FY2032-36 | MOV-29.08, MOV-30.06, MOV-31.10 | $209.74B (2029 act) + $57.33B (2030 act); highways 139.93, transit 36.69, rail 90.45 |
| $209.74B / $57.33B | Top-ups by act | MOV-29.08 / MOV-30.06 | 2029 act: highway 112.94 + transit 36.69 + rail 60.11; 2030 act: rail 30.34 + highway 26.99 |
| Obligated by Sept 30, 2036, spent by Sept 30, 2038 / by Sept 30, 2037, spent by Sept 30, 2039 | Top-up deadlines | MOV-29.08 / MOV-30.06 | 2029 act / 2030 act |
| $47.0B / $33.5B | Packages one and two | vehicles table; MOV-29.06, .07, MOV-30.04, .05 | rail 35.00 + transit 12.00; rail 13.50 + transit 20.00; both $80.50B |
| $256.74B / $90.83B | Total spending by act | MOV-29.10 | 47.00 + 209.74; 33.50 + 57.33 |
| +$33.3B / +$4.2B | Net deficit reduction by act (project estimate) | vehicles table; MOV-29.10 | net revenue 290.0 less 256.74; 95.0 less 90.83 |
| $6.0B / 17.0 / 25.5 and $4.0B / 13.0 / 15.0 | Rail and transit obligations FY2029 / 30 / 31, both packages | MOV-29.09 | 35.00 + 13.50 = 48.5; 12.00 + 20.00 = 32.0 |
| $35.00B | Transit operating tier, 5307(i) | MOV-31.40, MOV-31.50 | 6.0 + 6.5 + 7.0 + 7.5 + 8.0 |
| $25B | Capped solvency backstop FY2032-36 | MOV-31.08 | the cap is the aggregate across FY2032-36 |
| $55.00B | Tier 1 program, sec. 303 | MOV-31.05, MOV-31.63 | 14.00 + 12.00 + 7.00 + 6.50 + 7.50 + 8.00; by year 6.0 + 9.0 + 11.0 + 13.5 + 15.5 |
| $14.0B / $19.25B | Corridor cap / with the reserve (35% of $55B) | MOV-31.06, MOV-31.63 | a corridor at the cap may draw $5.25B from the reserve |
| $25.00B | Readiness reserve, up to, contingent | MOV-31.06, MOV-31.63, MOV-31 overview | illustrated 0 / 0 / 5 / 8 / 12 |
| $20.20B | Terminals, sec. 310 | MOV-31.05, MOV-31.64 | 9.0 + 4.0 + 3.5 + 0.7 + 3.0; existing four $17.2B, transit share $13.96B |
| $30.77B | Interstate and Bridge Renewal, sec. 1104 | MOV-31.22 | 10.77 converted + 20.00 new (the authorization text sums to $30.776B; the table governs) |
| $17.24B | Sec. 1112 grants, outside the total | MOV-31.27 | 1.23 + 2.05 in FY2032, grown 2.5% a year |
| $2.63B | Charging Gap Program, inside formula money | MOV-31.30 | 0.5 in FY2032, grown 2.5% a year |
| $31.53B / $63.03B | Backlog schedule / title III | MOV-31.41, MOV-31.42 | 28.00 + 31.53 + 0.50 + 3.00 = 63.03 |
| $190.92B | Division C renewal, sec. 717 | MOV-31.50 | sum of the 717 lines; plus $30.50B expansion = $221.42B |
| $1.0B | Division E | MOV-31 overview; MOV-31.80 to .84 | 0.25 + 0.15 + 0.10 + 0.50 = 1.00 |
| 0.180% / 0.200% / 0.026% | Average draw FY2032-36 / its peak in FY2032 / FY2042-46 | vehicles table; MOV-31.08 | with sec. 1112, the FY2032 all-in peak is 0.208% |

## Evidence still needed, and where the draft chose between figures

Only items that would change a choice now (`charter/STANDARDS.md`, "What needs an answer now"); the rest is study in implementation.

- **Sizing the 2028 transfer** needs the trust-fund cash-flow model (balances and outlay timing); it is not built (MOV-28.01).
- **H.R. 8870's enacted text** governs division B's title I; Draft 2 forecast it as enacted and called that a forecast, not law (MOV-31.20, MOV-31.90).
- **The baseline shares in 23 U.S.C. 120** (80% and 90%) behind "70%, 80% on the Interstate" are assumed, not stated in Draft 2 (MOV-31.24).
- **FTA's and FHWA's review triggers** (what "moves sharply" and "falls" mean) are set by rule; each is a working choice (MOV-31.40, MOV-31.24).
- **Which Buy America standard governs** a jointly funded fleet (50%, 70%, 75% or 100%) must be stated in sec. 1201 (MOV-31.49).
- **Where Draft 2 disagrees with itself** the governing figure is used and the alternative is in the provision's `parameters`: the expansion total ($123.70B, not $123.66B); sec. 1104's authorization text ($30.776B) against its table ($30.77B); sec. 1112's $1.23B and $2.05B against the rounded $1.2B and $2.0B; Tier 1's table against the ARCA-era increments in prose; the use tax's extension to Sept 30, 2030 (in the text, not in the vehicle table); whether sec. 101(g) rides in the 2029 or the 2031 vehicle (the Byrd table puts it in 2031); the bridge formula's $9.0B or $9.2B a year (unresolved; the enacted text decides); and the 48.4-cent / 45.3-cent comparison with the 1993 rate against looser prose.
- **Facts Draft 2 states without a source** (the $127.8B backlog's original, FTA's 781 and 552 staff, the National Transit Database shares behind the operating tier, the terminal ridership proxies) are used as the legacy design's figures and are marked in the provision text where they matter.
