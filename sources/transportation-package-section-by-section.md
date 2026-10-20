# Surface Transportation Package, 2026-2036 — Section-by-Section

> **Filed Oct 20, 2026** from the Surface Transportation claude.ai Project (package section-by-section, artifact fb14029c). Project paths are rewritten to their repo locations; the model scripts are in `index/tools/transportation/`. Where this file differs from `domains/transportation-moving-america-act-2031-draft-2.md` (Draft 2, canonical for MOV-), Draft 2 governs.


Oct 12, 2026 · @espen

## How to read this

Four vehicles carry the program, and only the last is a full reauthorization. The 2026 bill sets the baseline, the two reconciliation packages pre-fund what spends fast and create the revenue, and the 2031 bill folds the rail program (ARCA) and the transit program (the American Transit Renewal Act, ATRA) into one surface transportation reauthorization with a shared trust fund title.

**Calendar and name, decided October 12.** The 2031 bill covers FY2032-36 and its working title is the Moving America Act of 2031. BUILD America 250-Plus runs through FY2031, so no year is authorized twice. The framework tables and headline figures below are restated; any figure still reading FY2031-35 is superseded by `sources/transportation-calendar-fy2032-36.md` in the project. Program tables keep their nominal amounts one year later, a \~2.5% real reduction that is flagged there.

| Vehicle | When | What it carries | Federal dollars |
| --- | --- | --- | --- |
| BUILD America 250-Plus | December 2026, lame duck | H.R. 8870 as reported, plus a Senate trade for partial guarantees | Rail \~$73B authorized, \~$60B delivered; transit $102.8B authorized, \~$99.8B delivered; highways \~$375.5B, FY2027-31 |
| 2029 reconciliation | FY2029 | Rail $35.0B, transit $12.0B, the per-mile fee and the three-account fund | $47.0B |
| 2030 reconciliation | FY2030 | Rail $13.5B, transit $20.0B, aviation fee and rail diesel tax | $33.5B |
| Moving America Act of 2031 | FY2032-36 | Divisions A-F: revenue, highways and safety, transit (ATRA), rail (ARCA), research and delivery, budget rules | $908.8B across FHWA, NHTSA, FMCSA, FTA and FRA lines |

Three kinds of material are mixed here, and each section says which it is. ATRA and ARCA are designed and partly drafted in the two bill architecture docs; their sections below are summaries of those docs as rebased on October 12. The 2026 and reconciliation sections restate the forecasts those docs built. Division B (highways and safety) and most of Division E were not designed in this project; their sections are a proposed framework, sized from the fiscal model's highway line, and are marked as such.

All figures are budget authority in nominal dollars unless a row says otherwise. The rail numbers are ARCA's canonical table; the transit numbers are ATRA's; the revenue and general-fund figures come from `transit_fiscal_model.py` on its October 12 base case, checked against CBO's September 30, 2026 cost estimate of H.R. 8870.

## BUILD America 250-Plus (December 2026)

The baseline is H.R. 8870 as reported 62-2 in May 2026, enacted in the lame duck with one Senate trade: partial guarantees for rail and for Capital Investment Grants in exchange for the House's accountability and cost-share riders. It is a forecast, not law. It funds FY2027-31 at roughly IIJA levels in nominal terms and leaves the trust fund insolvent.

### Highways and the trust fund (as introduced)

| Section | Provision | FY2027-31 |
| --- | --- | --- |
| 1101 | Federal-aid highway formula programs: NHPP, STBG, metropolitan planning, HSIP, CMAQ, freight | $293.9B ($56.9B rising to $60.9B) |
| 1101 | Bridge formula program | \~$46B ($9.2B a year) |
| 1102 | Obligation limitation, plus \~$0.64B a year exempt | $372.4B limitation; \~$375.5B FHWA total |
| 1129 | Electric-vehicle and plug-in hybrid registration fee, $130 and $35, escalating, through FY2036; receipts go to the general fund, not the trust fund (CBO: $16.8B gross, $12.4B net of the income-tax offset, FY2026-36) | revenue |
| — | Headline total | $579.3B (CBO): $470.7B under obligation limitations, $108.6B in other authorizations |

Not in the bill: an extension of the fuel taxes that expire September 30, 2028, or a transfer large enough to carry the transit account through FY2027. CBO's September 30 estimate of the bill exhausts the transit account in FY2027 and the highway account in FY2028. Cumulative shortfalls at the end of FY2031 are $99.5B (highway) and $48.2B (transit), against $86.0B and $45.2B in the baseline, and that assumes the expiring fuel taxes continue. The bill also authorizes $26B of general-fund grants outside the trust fund, subject to appropriation: Bridge Investment Program $10B and multimodal freight $6B (sec. 1101), and National Infrastructure Grants $10B (sec. 7105).

### Public transportation (as projected in theorized Senate deal)

| Section | Provision | FY2027-31 | Guaranteed in 250-Plus |
| --- | --- | --- | --- |
| 3023 | Mass Transit Account contract authority: $16.868B, $17.205B, $17.527B, $17.835B, $18.157B | $87.6B | All |
| 3023 | Of which 5307/5336 urbanized area formula | $7.75B rising to $8.26B a year | All |
| 3022 | State of good repair (5337); repeals the 5337(f) railcar program | $4.64B to $4.66B a year | All |
| 3023 | Buses (5339) | $1.70B to $2.30B a year | All |
| 3007 | Capital Investment Grants, with Streamlined Starts up to $1B and $500M grants | $15.0B authorized | $5.0B (the Senate trade); the rest delivered at \~70% |
| — | WMATA grants (sec. 3109), FY2031 only | $0.15B | None |
| 3005 | Operating use for systems with 101-125 peak buses, up to 25% | policy | — |
| 3006 | Voluntary state block grant, formula money broadly eligible outside areas over 3.5M | policy | — |
| 3012 | Security operations up to 1.5% of formula funds; fare-evasion withholding | policy | — |
| 3013 | Bus federal share capped against a five-year average price | policy | — |

Total transit: $102.8B authorized, about $99.8B delivered, roughly 8% below IIJA in nominal dollars and 18% below in real terms. Three small additions are proposed for the vehicle: annual reporting of capital funds used on operations, a general-fund transfer into both accounts sized to CBO's cumulative shortfall through FY2030 ($71.2B highway, $36.8B transit, $108.0B in all, near IIJA's $118B; not grown to cover FY2031, because a 2026 Congress patches to the cash in front of it and nothing in 250-Plus is sized to the later program), because reconciliation cannot make one and the highway account runs dry in FY2028, and restoring the 5337(f) railcar program ($1.5B) as the trade for the fare-evasion condition.

### Passenger rail&#32;

| Program | H.R. 8870 as written: authorized, none guaranteed | 250-Plus: authorized | 250-Plus: of which guaranteed (Senate trade) | Delivered (assumed rate on the unguaranteed rest) |
| --- | --- | --- | --- | --- |
| Amtrak Northeast Corridor | $10.4B | $11.5B | $6.0B | 90% of the rest |
| Amtrak National Network | $20.7B | $22.0B | $10.0B | 90% of the rest |
| National Intercity Passenger Railroad Partnership Program | $18.5B | $24.0B | $6.0B | 65% of the rest |
| CRISI | $9.1B | $10.0B | — | 70% |
| Railroad crossing elimination | $3.65B | $5.0B | — | 50% |
| Corridor ID and planning | not stated | $0.75B | — | 80% |
| Interstate compacts; Restoration and Enhancement | folded in | $50M and $500M set-asides | — | — |
| Total | \~$62.4B | \~$73.3B | $22.0B (30%) | \~$60B |

**What changes between the bill and the deal.** H.R. 8870 as written guarantees nothing for passenger rail. Every line is an authorization of appropriations, about $62.4B in all (CBO: Amtrak grants $31.1B, rail infrastructure grants $27.6B, crossing elimination $3.65B), and annual appropriations decide how much is spent. 250-Plus, the forecast enacted version, raises the authorizations to about $73.3B. The Senate trade then turns $22.0B of that, 30%, into guaranteed money: $6.0B for the Northeast Corridor, $10.0B for the National Network and $6.0B for the Partnership Program. CRISI, crossing elimination and Corridor ID stay wholly subject to appropriation. The delivered column applies ARCA's assumed rates to the unguaranteed remainder only. Transit runs the other way. Its $87.6B of contract authority is guaranteed in H.R. 8870 as written, and the deal adds only the $5.0B of Capital Investment Grants it guarantees out of $15.0B authorized.

Riders carried as the House wrote them: Railway Safety Act provisions, station modernization authority, declining federal shares and business plans in the partnership program, an Amtrak mission rewrite toward financial performance, board transparency. No structural concession is sought. Corridor ID's new-selection sunset (October 1, 2031) is left alone: Division D makes the program permanent, and if the 2031 bill slips, the short-term extension act carries the date forward.

### Paired bipartisan permitting law

The American Affordability and Jobs Act (introduced September 30, 2026) is assumed to pass in the same lame duck: two-year EIS and one-year EA deadlines, a 150-day filing window, remand instead of vacatur, ten-year programmatic reviews, a narrowed section 106. It leaves rail without ESA right-of-way parity, leaves section 4(f), Coast Guard bridge permits and Corps 408 review untouched, and does not protect executed grant agreements. The 2031 bill closes those gaps in Division E.

## 2029-30 reconciliation: rail and transit titles

Two packages put $80.5B of transportation money and the whole revenue structure in place before the 2031 bill is written. Every spending line is a mandatory appropriation "to carry out" an existing authority, available until a stated deadline, so it clears the Byrd rule: fund the program, do not amend it. Conditions ride on the new money only.

### What the Byrd rule allows

| Instrument | Status | Basis |
| --- | --- | --- |
| Mandatory general-fund grants to carry out an existing section | Available | Direct spending; the American Rescue Plan put $30.46B into transit this way |
| Conditions on that money: operating eligibility, maintenance of effort, service floors, 100% federal share for small sponsors | Available | Terms "under which mandatory outlays are made" |
| Per-mile fee, EV fee, indexed fuel taxes, aviation fee, rail diesel tax deposited to a trust fund | Available | Revenue; the 1990 motor-fuel precedent |
| Creating the accounts and setting their shares of receipts | Available, inside the revenue title | It directs where receipts are credited |
| Credit subsidy (RRIF, TIFIA) | Available | Scores at obligation |
| Capital grants for projects not yet under agreement, including Capital Investment Grants | Available with obligation and expenditure deadlines | Deadlines keep outlays inside the window; without them, barred in practice |
| General-fund transfer into the trust fund | Barred | Intragovernmental; binds the 2031 bill, not this one |
| Contract authority under an obligation limitation | Barred | Outlays score to appropriations |
| Amending program design: 5307, 5309, 5326, 5337, CRISI, 25101 ceilings | Barred | Policy with incidental budgetary effect |

### Package one (FY2029)

| Title and line | Authority carried out | Amount | Condition |
| --- | --- | --- | --- |
| Rail: RRIF credit risk premium subsidy | 49 U.S.C. 22402 | $6.00B | Supports $35-50B of lending |
| Rail: zero-emission rail, electrification and trainsets | 22907, 24911 | $9.00B | Discrete segments and firm orders |
| Rail: state-of-good-repair backlog, NEC and national | 24911, Amtrak grants | $8.00B | Documented, designed work |
| Rail: Amtrak long-distance fleet replacement | Amtrak grants | $5.50B | Firm delivery schedule |
| Rail: Corridor ID planning and design | 25101 | $3.50B | 100% federal share below a sponsor capacity threshold |
| Rail: Amtrak station access and ADA | Amtrak grants | $3.00B | Amtrak-served stations only |
| Transit: operating transition grants | 5307 | $4.00B | State and local support held at its 3-year average; service hours at 95% of base |
| Transit: state of good repair, shovel-ready backlog | 5337 | $4.00B | Projects in asset management plans |
| Transit: bus and railcar replacement orders | 5339, 5337 | $3.00B | Firm orders |
| Transit: credit subsidy, transit and joint development | TIFIA | $1.00B | Scores at obligation |
| Revenue: per-mile fee at 1.0 cent; fuel taxes extended and indexed; EV fee; Surface Transportation Trust Fund with three accounts | 26 U.S.C. 9503 | receipts | Accounts created inside the revenue title |
| Total budget authority |  | $47.00B |  |

### Package two (FY2030)

| Title and line | Authority carried out | Amount | Condition |
| --- | --- | --- | --- |
| Rail: RRIF credit risk premium, second tranche | 22402 | $4.00B | As above |
| Rail: grade crossing elimination | 22909 | $4.00B | Discrete, locally delivered |
| Rail: electrification, second tranche | 24911 | $3.00B | As above |
| Rail: workforce and domestic supplier base | 22907 | $2.50B | Grants and cooperative agreements |
| Transit: operating transition grants | 5307 | $5.00B | As in package one |
| Transit: state of good repair | 5337 | $6.00B | As above |
| Transit: bus replacement | 5339 | $1.00B | Firm orders |
| Transit: station accessibility | 5337, ASAP | $3.00B | Rail transit and commuter stations only |
| Transit: Capital Investment Grants | 5309 | $3.00B | Executed agreements, plus projects that sign by the obligation deadline |
| Transit: credit subsidy | TIFIA | $1.00B | Scores at obligation |
| Transit: workforce and FTA capacity | 5314, admin | $1.00B | Grants and salaries |
| Revenue: aviation segment fee and rail diesel tax (10 and 5 cents), deposited to the rail account | 26 U.S.C. | receipts | 1990 precedent |
| Total budget authority |  | $33.50B |  |

Rail $48.5B and transit $32.0B are back-loaded so the general-fund test holds: on the base case the combined draw is 0.194% of GDP across FY2029-30, peaking at 0.197% in FY2030, against the project's 0.206% benchmark. Both reconciliation instructions should go to Finance and Ways and Means as well as to Commerce, Banking and EPW, because the revenue lines are the point.

## Moving America Act of 2031: the framework

One bill, six divisions, $908.8B over FY2032-36 for highways, highway safety, transit and passenger rail. ARCA and ATRA keep their names as short titles of Divisions D and C. Division A is the shared revenue title both architecture docs already assume, reported by Ways and Means and Finance and merged in conference.

| Division | Short title | Committees | FY2032-36 | Status in this project |
| --- | --- | --- | --- | --- |
| A | Surface Transportation Trust Fund and Revenue Act | Ways and Means; Finance | revenue; transfers | Designed (ATRA Title I, ARCA Title I) |
| B | Federal-Aid Highways and Highway Safety | T\&I; EPW, Commerce | $430.4B: FHWA $418.3B, NHTSA and FMCSA $12.1B | Proposed framework, sized from the model |
| C | American Transit Renewal Act | T\&I; Banking | $224.42B | Designed; Titles I-IV and VII drafted in part |
| D | American Rail Competitiveness Act | T\&I; Commerce | $254.03B, plus up to $25B readiness reserve | Designed; Titles I, IV and X-XII drafted in part |
| E | Research, Data and Project Delivery | T\&I; Commerce, EPW, Science | \~$1.0B proposed, outside the model | Partly designed (ARCA Titles VII and IX, ATRA Title VII) |
| F | Budget Discipline and General Provisions | all | none | Designed (ATRA SEC. 108) |

### By year

| FY | Highways (FHWA, NHTSA, FMCSA) | Transit | Rail | Total |
| --- | --- | --- | --- | --- |
| 2032 | $81.87B | $40.70B | $39.95B | $162.52B |
| 2033 | $83.92B | $42.89B | $47.29B | $174.10B |
| 2034 | $86.02B | $45.09B | $52.07B | $183.18B |
| 2035 | $88.17B | $47.04B | $56.13B | $191.34B |
| 2036 | $90.37B | $48.70B | $58.59B | $197.66B |
| Total | $430.35B | $224.42B | $254.03B | $908.80B |

Highways continue H.R. 8870's FY2031 level (250-Plus's last year) at 2.5% a year from FY2032; NHTSA and FMCSA ($12.07B) are the remainder of CBO's obligation limitation after FHWA and FTA, grown the same way. Transit and rail keep the nominal amounts drafted for FY2031-35, one year later. That is a placeholder for Division B's own sizing, which this project has not done.

### How it is paid for

Dedicated receipts cover $531.7B of the $908.8B: the reformed fund collects $495.5B and rail's aviation and diesel taxes $36.2B. The rest, $377.1B, is general fund, in two forms. Expansion in both bills, $126.7B, is mandatory appropriations (ATRA section 401, 606; ARCA sections 303, 310, 311, 312). The renewal shortfall in each account, $250.4B, is a transfer into the fund, as IIJA's $118B transfer was: about $114.1B to highways (NHTSA and FMCSA included), $43.7B to transit and $92.6B to rail. That transfer is not in either architecture doc as a separate section and is added here as Division A section 110.

The general-fund test holds the draw for all three modes under 0.206% of GDP. That figure is this project's benchmark, not a CBO or statutory limit: ARCA set 0.192%, the FY2026 general-fund draw on surface programs, as its own discipline rule, and the fiscal model restates it at 0.206% to count annual appropriations the same way. Congress's binding constraints are elsewhere, in the budget resolution's reconciliation instructions, PAYGO and the Byrd rule. On the base case the draw runs 0.169% to 0.177% a year in FY2032-36, with $12.4B to $16.6B a year of room, and ARCA's $25B readiness reserve fits at $5B a year with $7.4B to spare in the tightest year. The tight years are now before the bill: FY2030 at 0.197%. FY2031, 250-Plus's last year, falls to 0.081%, which is a cliff in rail and transit funding that the 2030 reconciliation package should bridge.

Exceeding the benchmark is acceptable; the cost of doing so should be stated. The test counts transfers. CBO scores a new excise net of about a quarter for lost income and payroll taxes (its EV fee nets $12.4B of $16.8B), so on CBO's basis the per-mile fee and indexing add $56.3B over FY2032-36 and the package runs 0.193% to 0.203%, still under the benchmark, and 0.219% in FY2030. That is the figure the reconciliation instructions will have to accommodate. The model's receipts match CBO's: current-law trust fund receipts of $49.1B in FY2029 reproduce its Table 6 to the decimal.

## Division A: Trust fund and revenue

Division A turns the Highway Trust Fund into a Surface Transportation Trust Fund with three accounts and writes a rule for dividing the money the per-mile fee adds. It replaces both SEC. 101 texts in the ARCA and ATRA docs. The reconciliation packages created the accounts and the fee; this division sets their permanent terms.

| Section | Provision | Source and change |
| --- | --- | --- |
| 101 | Surface Transportation Trust Fund: 26 U.S.C. 9503 redesignated; Highway, Mass Transit and Intercity Passenger Rail Accounts. Highway and transit accounts first credited with FY2028 receipts, CPI-indexed; receipts above those base amounts split 35% highways, 50% transit, 15% rail; renewal programs paid before expansion in each account; 9503(e)(3) amended so the transit account pays for any chapter 53 purpose; shares reset each reauthorization by an equal-coverage report | ATRA SEC. 101 (drafted). Replaces ARCA's 8 / 15 / 22 / 28% rail share of all receipts. ARCA's five rail accounts become subaccounts of the rail account |
| 102 | Per-mile road user charge: 1.0 cent in FY2029, plus 0.2 cents a year to 3.6 cents in FY2042, on all vehicle-miles; fuel taxes phased down over the same period | ATRA SEC. 102. ARCA drafted 0.6 cents rising to FY2044; at House highway levels that schedule breaches the general-fund cap |
| 103 | Fuel taxes retained and indexed; electric-vehicle and plug-in hybrid fee at $130 and $35, rising $5 a year to $200; the H.R. 8870 fee's FY2036 expiry struck and its receipts credited to the fund (H.R. 8870 leaves them in the general fund; the 2029 package moves them) | ATRA SEC. 103; ARCA Choice 2 |
| 104 | Aviation segment fee, $4 in FY2032 stepping to $12 by FY2036 and capped at $16 by FY2046; rail diesel tax at 15 and 7.5 cents per gallon from FY2032 (10 and 5 cents in FY2030-31); corridor surcharge of $12 on city pairs with a funded corridor; all credited to the rail account outside the three-way split | ARCA SECS. 102-104 |
| 105 | General-fund programs: mandatory appropriations for expansion (ARCA sections 303, 310, 311, 312; ATRA sections 401 and 606), $126.7B over FY2032-36 | ATRA SEC. 105. Replaces ARCA's $132B general-fund transfer into the rail fund |
| 106 | Contract authority on enactment for every account; contingent commitments to FY2046 capped at 60% of a year's authorization; ARCA's $25B readiness reserve subject to section 108 | ARCA SEC. 106, extended to transit |
| 107 | Continuation of each account's renewal programs at FY2036 levels if reauthorization lapses | ATRA SEC. 107. Replaces ARCA's $12B rail-only floor |
| 108 | General-fund discipline: Secretary and CBO report the all-in draw yearly; above 0.206% of GDP, expansion is reduced first, renewal last; executed agreements exempt | ATRA SEC. 108 (drafted). Replaces ARCA's proportional reduction |
| 109 | Joint facilities: transit and rail accounts both pay for shared facilities, renewal by share of train movements, expansion by share of added train movements | ATRA SEC. 109 (drafted, revised October 12). Replaces ARCA's bar on chapter 53 uses |
| 110 | Transfers to the accounts equal to each account's projected renewal shortfall: about $114.1B highways (NHTSA and FMCSA included), $43.7B transit, $92.6B rail over FY2032-36 | New in this framework; the IIJA transfer precedent. Not reconciliation-eligible, so it rides here |
| 111 | Per-mile fee administration: Treasury collection, a privacy rule barring location data, a state collection-agreement option, 10% cost allowance | New. The architecture docs assume collection but do not draft it |

Section 111 is the one most likely to decide whether section 102 survives. The fee's political risk is surveillance, not price: about $48 a year more than ARCA's schedule for a car driven 12,000 miles. The section should say in terms that odometer reads, not location, are the base.

## Division B: Federal-aid highways and highway safety (proposed framework)

This division was not designed in the project. What follows is a framework that fits the rest of the bill: H.R. 8870's program structure carried forward at 2.5% a year, $418.3B over FY2032-36, with the few changes the shared trust fund requires. The sub-allocations are proposals, not model outputs.

| Section | Provision | FY2032-36 | Basis |
| --- | --- | --- | --- |
| 1101 | Authorizations and obligation limitation, FY2032-36, from the Highway Account | $418.3B FHWA total | Model's highway line: H.R. 8870 FY2031 level, +2.5% a year from FY2032 |
| 1102 | Apportioned formula programs: NHPP, STBG, HSIP, CMAQ, freight, metropolitan planning, at H.R. 8870 shares | \~$328.1B | H.R. 8870 sec. 1101(a)(1), $60.9B in FY2031, grown |
| 1103 | Bridge formula program | \~$49.6B | H.R. 8870, $9.2B a year, grown |
| 1104 | Federal lands and tribal programs, emergency relief, TIFIA, administration and discretionary capacity grants | \~$40.6B | Residual of the FHWA total |
| 1105 | Renewal programs of the Highway Account defined for Division A section 101(f): apportioned formula programs and bridge; discretionary capacity grants are expansion | policy | Needed: ATRA's SEC. 101(f) defines transit and rail renewal but not highway renewal |
| 1106 | Fix-it-first: a State whose NHPP pavement or bridge condition falls below its own target for two reporting periods applies a rising share of NHPP to preservation before new capacity | policy | Parallel to ATRA's 5326(e) direction, without withholding |
| 1107 | Transit and rail flexibility kept: STBG and CMAQ transfers to chapter 53 and to intercity rail capital as of right; a State may use STBG for its share of a joint facility under Division A section 109 | policy | Continues 23 U.S.C. 104(f) and 133 |
| 1108 | Per-mile fee coordination: States may collect the Division A section 102 charge alongside a state road user charge under one account, with Treasury reimbursement of collection cost | policy | Ties to Division A section 111 |
| 1109 | Vulnerable road user safety: HSIP set-aside when pedestrian and cyclist deaths exceed 15% of a State's fatalities, continued and indexed | policy | Continues IIJA's special rule |
| 1110 | Resilience: PROTECT formula continued as a set-aside within NHPP, coordinated with ATRA's transit resilience line | within 1102 | Continues IIJA |
| 1111 | Unit cost and delivery reporting for highway projects over $100M, into the same public database as transit and rail | policy | Mirrors ARCA section 705 and ATRA section 705 |
| 1112 | General-fund grants carried from H.R. 8870, subject to appropriation: Bridge Investment Program ($2B a year), multimodal freight ($1.2B), National Infrastructure Grants ($2B, sec. 7105) | \~$28.0B authorized FY2032-36 | Outside the fund and the model. If fully appropriated, $5.2B a year would take most of the FY2032 room; fold the bridge money into the formula program or count these under the cap |
| 1201 | NHTSA highway safety programs, section 402 grants, and vehicle safety | \~$12.1B with FMCSA: H.R. 8870 levels ($2.0-2.2B a year in FY2027-31, CBO's $470.7B limitation less FHWA and FTA), grown 2.5% | — |
| 1301 | FMCSA motor carrier safety assistance and operations | in the 1201 figure | — |

The political center of this division is section 1101's number, not its policy. Highways hold 88% of today's fuel tax receipts and receive 35% of the new money in Division A; the argument that carries the highway bloc is a solvent account covering three-quarters of its program, against an insolvent one covering none of the growth. A full design pass on this division should start from the H.R. 8870 conference text, which this project has only read in summary.

## Division C: Public transportation (American Transit Renewal Act)

ATRA is $224.42B over FY2032-36: $190.92B of renewal from the Mass Transit Account and $33.50B of expansion as mandatory general-fund money. Its Title I moves to Division A; section numbers below keep ATRA's numbering so they trace to the architecture doc. By year: $40.70B, $42.89B, $45.09B, $47.04B, $48.70B.

### Title II: Operating assistance ($35.00B)

| Section | Provision | FY2032-36 |
| --- | --- | --- |
| 201 | New 49 U.S.C. 5307(i): formula operating grants to urbanized areas of 200,000 or more, rail included. Apportioned 50% vehicle revenue hours, 30% unlinked trips, 20% low-income residents; no area above 25% of its net operating cost, excess reapportioned. 50% federal share. Conditions: state and local support at its 3-year average, CPI-indexed; service hours at 95% of FY2028-30; not under a 5326(e) direction; preventive-maintenance share frozen. Cost review above the state-local wage index plus 1.5 points. Annual publication. New 5338(a)(2)(P): $6.0B rising to $8.0B | $35.00B |

On 2024 data the first-year tier pays about 11.9% of net operating cost nationally; New York's 27.7% share equals its share of that cost.

### Title III: State of good repair ($63.03B)

| Section | Provision | FY2032-36 |
| --- | --- | --- |
| 301 | State of good repair formula (5337), including $300M a year of restored railcar replacement grants; 80% federal | $28.00B |
| 302 | New 5337(g): the $127.8B backlog (2025 dollars) retired in 20 installments from FY2032, apportioned by each agency's audited baseline; 80% federal | $31.53B |
| 303 | Asset management enforcement: new 5326(e) directs an agency that misses its targets to apply its own apportionment to its own priority list; no withholding. FTA baseline audits | $0.50B |
| 304 | Transit resilience | $3.00B |

### Title IV: Capital Investment Grants ($27.50B)

| Section | Provision | FY2032-36 |
| --- | --- | --- |
| 401 | Mandatory appropriations available until expended; a full funding grant agreement obligates the whole federal share at signing, ending 5338(d)(2)'s "only to the extent that amounts are appropriated" | $27.50B |
| 402 | Warrants by default for projects seeking 50% or less from 5309 | policy |
| 403 | Local commitment in ARCA's five match categories; categories C and D capped at 40% | policy |
| 404 | 120-day decision clock on engineering entry, letters of no prejudice and agreements | policy |
| 405 | ARCA's tranche gates and cure-and-termination rules for federal shares over $1B, binding the department as well as the sponsor | policy |
| 406 | One application and one finance plan for joint projects under 5309(q) and ARCA sections 302-303 | policy |
| 407 | Standardized unit costs and an independent cost review at 30% design for projects over $1B | policy |

Carried from H.R. 8870: Streamlined Starts, 30% design before project development, the transit-oriented development rating credit.

### Title V: Labor and workforce ($2.85B)

| Section | Provision | FY2032-36 |
| --- | --- | --- |
| 501 | Registered apprenticeships for operators, mechanics, signal and power maintainers, joint labor-management | $1.60B |
| 502 | Confirms 5333(b) certification "without referral" for recurring 5307(i) and 5337(g) grants | policy |
| 503 | Frontline training set-aside, 1% of each recipient's 5307 and 5337 apportionment, matched | $0.75B |
| 504 | Operator safety: enclosed workstations on new buses, retrofit grants | $0.40B |
| 505 | Transit Workforce Development Center made permanent | $0.10B |
| 506 | Minimum safety standards, including operator presence, before federal funds pay for automated revenue service | policy |

### Title VI: Formula capital, buses, rural, accessibility, joint facilities ($91.30B)

| Section | Provision | FY2032-36 |
| --- | --- | --- |
| 601 | Urbanized area formula, capital (5307, 5340) | $54.10B |
| 602 | Buses (5339): propulsion-neutral; 90% federal share of the zero-emission increment; pooled multi-agency orders | $14.00B |
| 603 | Rural, tribal and intercity bus (5311); rural operating share to 80% (section 712) | $7.50B |
| 604 | Seniors and people with disabilities (5310) | $3.20B |
| 605 | All Stations Accessibility: $1.0B a year, FY2045 completion target, annual list by name, national count and cost published within a year | $5.00B |
| 606 | Joint transit-rail facilities and station access, attributed under Division A section 109; general fund, first under the trigger | $6.00B |
| 607 | Ferries, H.R. 8870's consolidated program | $1.00B |
| 608 | Emergency relief quick release (5324), standing authorization | $0.50B |

### Title VII: Delivery, cost discipline and FTA capacity ($4.74B)

| Section | Provision | FY2032-36 |
| --- | --- | --- |
| 701 | Metropolitan and statewide planning (5305) | $1.55B |
| 702 | FTA administration and oversight; staffing restored to at least 800 | $1.05B |
| 703 | Safety oversight (5329) and the National Transit Database | $0.55B |
| 704 | Research, technical assistance and bus testing | $0.80B |
| 705 | Cost benchmarking, standard designs and owner-side engineering capacity, shared with ARCA section 705 | $0.79B |
| 711 | Planning targets: 5303 and 5304 add the service floor and the backlog schedule | policy |
| 712 | Rural operating share 50% to 80% (5311(g)(2)(A)) | policy |
| 713 | Emergency waiver of the 5307(i) service and effort conditions (5324(g)) | policy |
| 714 | Safety withholding reaches 5307(i) money only after a year of directed use (5329(g)(2)(C)) | policy |
| 715 | Stale cross-references in 5337, 5339(a)(5) and 5340(b) corrected | policy |
| 716 | FTA's 0.75% oversight takedown excludes 5307(i) (5338(c)(1)(B)) | policy |

## Division D: Passenger rail (American Rail Competitiveness Act)

ARCA is $254.03B over FY2032-36 ($39.95B, $47.29B, $52.07B, $56.13B, $58.59B), plus up to $25B of readiness reserve released on gate clearance. Its Title I moves to Division A with four changes: rail takes 15% of new fund receipts instead of 8-28% of all receipts, the $132B transfer becomes a renewal transfer plus mandatory appropriations, the $12B rail floor becomes continuation of every account, and the solvency trigger cuts expansion first. Amounts below are ARCA's canonical table.

### Title II: Core network ($59.95B)

| Section | Provision | FY2032-36 |
| --- | --- | --- |
| 201(a) | Amtrak Northeast Corridor base grant: operations, normalized replacement, corridor repair; 100% federal | $10.00B |
| 201(b) | NEC Capital Program: Hudson Tunnel, B&P, Susquehanna, Connecticut River, Sawtooth, Penn Station; 80% federal, the rest allocated under the NEC Commission's cost policy | $17.00B |
| 202 | National Network operating grant: daily service restored, new corridors' operating cost; route-level reporting; missing a financial target is not by itself grounds for discontinuance | $11.00B |
| 203 | Long-distance preservation and renewal: overhaul and life extension, stations, host capacity, daily service | $4.70B |
| 204 | National Fleet Program: single-level long-distance fleet ($7.50B), NEC and high-speed trainsets, locomotives, maintenance facilities | $13.10B |
| 205 | Stations and ADA: hard FY2036 deadline, annual certification by name; small-station program; New Orleans, Dallas, Denver hubs | $4.15B |

### Title III: Corridor development ($160.45B)

| Section | Provision | FY2032-36 |
| --- | --- | --- |
| 301 | Corridor ID made permanent, three funded steps | $2.50B |
| 302 | Intercity capital, Tier 2 and 3: 45% formula to the five commissions and States, 55% competitive | $38.00B |
| 303 | National High-Speed Rail Program, Tier 1: 50% federal, $1B minimum, gated entry (record of decision, rolling stock strategy, certified ridership, committed match); general fund; first call on the reserve | $55.00B |
| 304 | CRISI, with 25% rural and short-line safety set-asides | $12.50B |
| 305 | Grade crossings: half formula by crossings weighted by collisions, half competitive | $12.50B |
| 306 | Safety implementation | $1.75B |
| 310 | Terminals and junctions of national significance: Chicago, New York Penn and Sunnyside, Washington Union, Los Angeles Union, Atlanta; transit share paid by ATRA section 606 under Division A section 109 | $20.20B |
| 311 | Federally initiated corridors, starting with Palmdale-Los Angeles and the high-speed trunks no State will propose | $6.00B |
| 312 | Long-distance network implementation: first tranche of FRA's five highest-rated route options | $12.00B |
| 313 | Strikes the 750-mile ceiling and the "formerly operated by Amtrak" limb of 25101(h) | policy |

### Titles IV-IX: Accountability, institutions, access, industry, credit, permitting ($12.63B)

| Section | Provision | FY2032-36 |
| --- | --- | --- |
| 401-406 | Tranche gates at 25, 50 and 75% of federal capital; Office of Rail Project Delivery and independent reviewers; match status taxonomy and two-sided contingent commitments; public variance reporting; cure, termination and reallocation; identical rules for non-Amtrak operators | $1.33B |
| 407 | Funding certainty: decision deadline, cure period, published factual basis and judicial review before terminating an executed agreement | policy |
| 501 | Five regional corridor commissions on the NEC Commission model: Northeast, Southeast, Cascadia, Midwest Hub, and a fifth | $1.00B |
| 503 | Amtrak structure neutrality: rules that hold under any reorganization, open access if NEC infrastructure is separated | policy |
| 601 | Preference enforcement: burden shift, civil penalties, 240-day decisions, private right of action | $0.125B |
| 602 | Capacity-for-access covenants on federally funded host projects, 30 years | $0.64B |
| 603 | On-time standard 80%, 85% for assisted routes after FY2034; certified delay reporting | $0.085B |
| 604 | Interoperable ticketing and scheduling, open API, through-ticketing with transit | included |
| 701-704 | Rolling stock supplier grants tied to committed orders; standard specification and pooled procurement; craft apprenticeships and owner capacity; Buy America at 75% with final assembly | $3.95B (with 705-709) |
| 705-709 | Unit-cost disclosure, standard designs, $600M for owner-side engineers, progressive design-build and alliance contracting, utility relocation deadlines | within $3.95B |
| 801 | Credit: RRIF ceiling to $150B (H.R. 8870 raises it from $35B to $50B); $3.3B credit risk premium for public borrowers; $1.25B interest buy-down; longer terms | $5.00B |
| 901-907 | Permitting parity: ESA right-of-way exemption, statutory categorical exclusion in existing right-of-way, 4(f) alignment, Coast Guard and Corps 408 clocks, judicial review parity, $300M national programmatic review, $200M review staff | $0.50B |

### Titles X-XIII: Operating support, competition, fleet, night trains ($21.00B)

| Section | Provision | FY2032-36 |
| --- | --- | --- |
| 1001 | Strikes 22908(e)(2) so operating assistance can be used; permanent 50% floor for interstate routes; one State's withdrawal does not end service | $8.00B (title) |
| 1002 | State cost allocation States can audit | within Title X |
| 1003 | Advance consent to interstate rail compacts meeting stated conditions | within Title X |
| 1101 | Operator-neutral access: a State- or compact-selected operator gets Amtrak's access, preference and remedies | $1.50B (title) |
| 1102 | Competitive service pilot reopened: eight routes of any length, no advance host consent | within Title XI |
| 1103 | Access charges on the NEC Commission's cost allocation model, STB backstop | within Title XI |
| 1104 | Dedicated passenger track presumed above a density threshold for Tier 1 and 2 | within Title XI |
| 1201-1204 | Public equipment pool with performance specifications, Tier III completion, FRA certification capacity, lease that follows the asset | $8.50B |
| 1301 | Night network: overnight services on 500-1,200 mile city pairs | $3.00B |
| — | One ticket (in Title VI), station value capture and the airline slot bargain: authority only | none |

## Divisions E and F, and the bill whole

Division E collects what all three modes share; most of it is policy and the money is small. Division F holds the general provisions. Both are proposed here except where a section cites an architecture doc.

### Division E: Research, data and project delivery (proposed, \~$1.0B outside the model)

| Section | Provision | FY2032-36 |
| --- | --- | --- |
| 101 | National intercity passenger travel forecast, all modes, every five years; no federal forecast of the trip exists today | $0.10B |
| 102 | One public unit-cost database for highway, transit and rail projects over $100M, fed by Division B section 1111, ATRA section 705 and ARCA section 705 | $0.15B |
| 103 | Per-mile charge evaluation: collection cost, evasion, privacy compliance and equity, reported yearly to the tax committees | $0.10B |
| 104 | Executed grant agreements protected across all modes: decision deadline, cure period, published basis and judicial review before termination (ARCA section 407, extended); closes the gap the 2026 permitting law left | policy |
| 105 | Permitting parity across modes: ARCA sections 901-905 for rail, plus the same Coast Guard and Corps 408 clocks for transit and highway bridges | policy |
| 106 | Owner-side engineering and delivery capacity grants to State DOTs and transit agencies, matching ARCA section 707 | $0.50B |
| 107 | Bureau of Transportation Statistics and the National Transit Database: multi-area apportionment data published with each apportionment | $0.15B |

### Division F: Budget discipline and general provisions

| Section | Provision |
| --- | --- |
| 101 | Cross-references to 49 U.S.C. 5338(a)(2) and 23 U.S.C. 104 cite programs by name, not by subparagraph letter, so a relettering in any later bill cannot misdirect money |
| 102 | Buy America for jointly funded rolling stock: the equipment pool's standard (ARCA section 1201, ATRA section 706); each mode's own rule elsewhere |
| 103 | Labor: 49 U.S.C. 5333(b) and the Railway Labor Act protections carried through any Amtrak reorganization and to joint facilities |
| 104 | Reconciliation money from 2029-30 counted toward each program's FY2032-36 baseline only where obligated; no double counting in the general-fund report |
| 105 | Effective date October 1, 2030; continuation under Division A section 107 if the bill lapses |

### Authorization summary, FY2032-36

| Division and title | Amount | Kind |
| --- | --- | --- |
| B: Highways and highway safety | $430.35B | Renewal, Highway Account |
| C-II: Transit operating assistance | $35.00B | Renewal |
| C-III: Transit state of good repair | $63.03B | Renewal |
| C-IV: Capital Investment Grants | $27.50B | Expansion, general fund |
| C-V, VI, VII: Workforce, formula capital, delivery | $98.89B | Renewal, except section 606 ($6.00B) |
| D-II: Rail core network | $59.95B | Renewal |
| D-III: Rail corridor development | $160.45B | Sections 303, 310, 311, 312 ($93.20B) expansion; the rest renewal |
| D-IV to XIII: Accountability through night trains | $33.63B | Renewal |
| E: Research, data and delivery | \~$1.00B | Proposed; outside the model |
| Total | \~$909.8B |  |
| Contingent: ARCA readiness reserve | up to $25.00B | Expansion, under the trigger |

## Settled, assumed, and still to draft

The transit and rail divisions are designed to section level and partly drafted; the revenue division is designed and partly drafted; the highway division is a sized placeholder. Six inconsistencies between the source docs need settling before any of this goes to legislative counsel.

### Inconsistencies to resolve

| Item | Where | Resolution proposed |
| --- | --- | --- |
| ARCA's Title I still describes the standalone fund, 8-28% rail share, $132B transfer and proportional trigger | ARCA doc | Rewrite ARCA Title I to point to Division A; the October 12 rebase has not been applied to the ARCA doc |
| Aviation fee schedule: ARCA's reconciliation section raises a fee "$4 to $9" in 2030 and steps it to $12; its envelope section starts a surcharge at $4 in FY2031 | ARCA doc | Pick one schedule; the fiscal model uses $4 in FY2032 rising to $12 in FY2036 |
| ARCA's title tables give 203 at $5.90B, 205 at $6.65B and 303 at $40.00B; the canonical table gives $4.70B, $4.15B and $55.00B | ARCA doc | The canonical table governs; correct the title tables |
| ARCA's Byrd table bars greenfield capital "in practice"; ATRA's now allows capital with obligation and expenditure deadlines | Both docs | Use the deadline rule in both |
| ATRA's 250-Plus table shows $103.2B total transit on the older $87.4B figure | ATRA doc | $87.6B contract authority; WMATA $0.15B in FY2031 only (CBO); $102.8B total, \~$99.8B delivered |
| Highway renewal programs are undefined for the renewal-first rule | ATRA SEC. 101(f) | Division B section 1105 |

### New in this framework, not in either architecture doc

- Division A section 110, the renewal-shortfall transfers ($250.4B over FY2032-36).
- Division A section 111, per-mile fee administration and the location-data bar.
- All of Division B beyond its total, and Division E sections 101-103, 106 and 107.
- Division F sections 101 and 104.

### Still to draft

- [ ] Division A sections 102-104, 106, 107, 110, 111 in statutory text (101, 108 and 109 are drafted)
- [ ] Division B from the H.R. 8870 conference text, including NHTSA and FMCSA levels
- [ ] ATRA sections 302 (5337(g)) and 303 (5326(e)) are drafted; 401-407, 501-506, 601-608 and 701-705 are not
- [ ] ARCA sections 302's formula, 310's project list under the new joint-facility rule, and Titles V-IX text
- [ ] A CBO-style score of Divisions A and B; the general-fund test above is this project's model, not CBO's; the 0.206% benchmark is the project's own and may be exceeded, but the reconciliation instructions must be sized to CBO's net-of-offset score (about 0.025% of GDP above the transfer measure)

### Sources

The two architecture docs: [American Transit Renewal Act of 2031](https://claude.ai/code/artifact/6eded0d5-40fc-433a-b940-8d8ca015f581) and [American Rail Competitiveness Act of 2031](https://claude.ai/artifact/518f3bb4-2063-42e2-9b4b-1936f8d19ca8); the project's `transit_fiscal_model.py` and `transit-package-status.md`; [H.R. 8870 text](https://www.congress.gov/119/bills/hr8870/BILLS-119hr8870ih.htm); [APTA's H.R. 8870 funding table](https://www.apta.com/wp-content/uploads/2026/06/HR-8870-BUILD-America-250-Draft-Funding-Table-Public-Transit-05222026.pdf); [Holland & Knight on the BUILD America 250 Act](https://www.hklaw.com/en/insights/publications/2026/05/a-closer-look-at-the-build-america-250-act); [CBO trust fund baseline, June 2026](https://www.cbo.gov/system/files/2026-06/51300-2026-06-highwaytrustfund.pdf); CBO cost estimate for H.R. 8870 as ordered reported, September 30, 2026.
