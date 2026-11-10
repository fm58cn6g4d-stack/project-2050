# Transportation: what would change our minds

Role: section 8 of the transportation dossier. For each major choice (`DEC-2026-11-10-08`) it gives the main uncertainty, the finding that would change it with a threshold, who sees it and when, and the fallback. Status: draft (stage C, step 7, PR 3).

How triggers work: under the design lens (`DEC-2026-11-09-13`), a trigger starts a published review, not an automatic cut. The review has a deadline, and the agency that owns the program reports to Congress with a recommendation. A few hard stops are listed at the end. None of them takes service away from riders already using it.

## By choice

| Choice | Main uncertainty | What would change it (threshold) | Who sees it, when | Fallback |
| --- | --- | --- | --- | --- |
| **Fuel-tax steps** (memo 1) | Drivers respond more than the model's zero assumption; the legacy design guessed 2-3% of fuel receipts [EV-MOV-228] | Receipts more than 5% below the model for two years after a step, net of pauses | Treasury and CBO's yearly report (division A sec. 108), from FY2031 | Hold the step size; draw on the capped $25B backstop [EV-MOV-219]; the settlement decides on general-fund cover. Not 2-cent steps, which cost coverage permanently [EV-MOV-203] |
| **Price pause** | Price shocks defer many steps | Three or more pauses by FY2036 | Same report | Resume deferred steps as written. The capped $25B backstop covers part of the shortfall in between (three pauses delay about $53.3B [EV-MOV-219]); the rest, about $28B, falls on expansion programs first under sec. 108(c)(2), never on sec. 105 or 106(e) money or executed agreements, unless the settlement covers it |
| **Fossil premium** (FY2040-44) | The premium shrinks its own base faster than modelled; its receipts are an upper bound [EV-MOV-206] | Electric cars above 40% of new sales by 2036, or the premium projected to raise less than half its modelled receipts | The 2036 report before the successor bill | Keep the premium as a signal but stop crediting it to the general-fund draw; or start it later. The successor bill decides |
| **Clean-vehicle charge** | Collection costs above the 10% ceiling at the start [EV-MOV-120] [EV-MOV-118] | Cost above 10% two years after start | GAO's three-year review (sec. 111), first report 2033 | Treasury collects through more state agreements; the ceiling is not raised without a review. If cost stays above the ceiling, the successor bill can offer a flat annual federal fee by vehicle class, collected at registration, as Oregon's 2025 law does beside its per-mile charge [EV-MOV-117]. It costs far less to collect: at 10% of the charge's $14.5B over FY2032-36 (MOV-29.03), collection could cost up to $1.45B. Memo 1's decision stands; this is the cheaper fallback |
| **Weight-distance charge** (memo 2) | Evasion at Oregon's 5-11% [EV-MOV-122] | Measured evasion above 10% | GAO's review; Treasury audits | Raise the audit rate within the collection ceiling. Not a fall-back to a flat tax |
| **Size and split** (memo 3) | Construction costs eat the program's buying power, as in FY2021-25 [EV-MOV-008] | Highway construction costs rising more than 20% faster than general inflation over three years (FHWA's index [EV-MOV-132]) | FHWA, yearly | The settlement may re-index program levels (A-5 kept them nominal), or pare by the fallback tiers below |
| **Interstate renewal** | The program is short of the National Academies' need [EV-MOV-010] | Interstate pavement or bridge condition worsening for two years | FHWA's condition data, yearly | Memo 3's option B (full money from FY2032), for the settlement |
| **Transit operating help** (memo 4) | The tier holds service but agencies shift capital money to operations or costs grow | Preventive-maintenance shares or cost per service hour moving sharply in the published reports; areas covering more than a fifth of riders below the service floor | FTA's yearly published report | An FTA review of the outlier areas, then a recommendation to Congress. The legacy conditions (a hard cap on preventive-maintenance shifting, a cost review) are the fallback if reviews fail twice |
| **Conditions on states** (memo 5) | Publishing condition trends doesn't move states toward repair | Poor-condition shares rising for two years in more than ten states | FHWA's review of each state | The legacy preservation shift and lifecycle gate (memo 5, option A), by law in the successor bill |
| **Passenger rail** (memo 6) | Corridors are not ready, and an administration slows the pipeline [EV-MOV-109] [EV-MOV-225] | Less than half of Tier 1 money obligated by FY2034 | FRA's yearly report; the readiness reserve's certification | Unobligated Tier 1 money stays for the corridor that clears first; the reserve shrinks; the successor bill resizes. Gates are never waived |
| **Charging Gap Program** | Auctions and uptime payments untested at federal scale [EV-MOV-216] | Fewer than half of first-round awards energized in 24 months | FHWA's gap map updates | Re-offer lapsed awards (the lapse rule); if the method fails twice, return the money to states' formula programs |
| **The baseline** (point 1) | No multi-year law by the end of 2028 | That fact on December 31, 2028 | Congress's record | The contingency authorization (MOV-31.90) on regular order in 2029-30 |

## Political and legal events

- **No 2028 extension.** Fund credits stop after September 30, 2028 [EV-MOV-004] and rates fall to 4.3 cents [EV-MOV-016]. The 2029 act then carries the extension's terms too. This is the largest risk the model does not cover.
- **Reconciliation lost in 2029-30** (a Republican House). The two acts cannot pass (`dossiers/scenario/house-stress-test-2029.md`). Revenue and top-ups then need a regular-order bill with 60 votes, and the fallback tiers apply.
- **The 2030 act slips past R3.** Package two and the FY2035-36 top-ups move to the 2031 bill, which needs 60 votes. The 2029 act's money is unaffected.
- **Court challenges** to the per-mile charges' privacy rules or to tolling rebuilt Interstate segments. Neither is a design fork; the design's privacy rules are stricter than current law for tax return information.

## The fallback tiers

If the bill must shrink, it shrinks in three rounds that cut construction and expansion first and leave the structural provisions alone (`legacy/domains/transportation-moving-america-act-2031-draft-2.md`, "Fallback tiers"):

| Round | Bill | Average draw FY2032-36 |
| --- | --- | --- |
| As decided | $936.57B | 0.180% |
| First | $865.02B | 0.147% [EV-MOV-226] |
| Second | $804.30B | 0.119% [EV-MOV-227] |
| Third | $739.25B | 0.089% [EV-MOV-227] |

These survive every round: the fund and its revenue, contract authority within receipts, continuation, the location-data bar, the Interstate program as a program, the safety rules, the transit operating tier's protective conditions and the rail gates.

## Hard stops

These end a payment, not anyone's service:
- **A recipient that certifies falsely** (maintenance of effort, the service floor, a gate) repays and is barred from the next year's award.
- **A per-mile charge reading that includes location data** must be destroyed, and the disclosure is actionable (sec. 111).
- **A Tier 1 project that fails a tranche gate** gets no further tranche until it cures.

## When the evidence arrives

| When | What | Informs |
| --- | --- | --- |
| Each year, from FY2031 | Treasury and DOT account report (sec. 108) | Steps, pauses, the backstop |
| Each year | FHWA condition data; NTD service and cost; FRA obligation reports | Memos 3-6 |
| 2027 | NHTSA's final 2025 death count (FARS) | Safety baseline |
| 2027-28 | CBO's next Highway Trust Fund baselines | The 2028 extension's transfer |
| March 31, 2030 | The highway cost allocation study | The weight-distance schedule (2030 act) |
| 2033, then every three years | GAO's review of the per-mile charges | Collection cost, evasion, privacy |
| 2036 | The account report before the successor bill | The premium, the split, re-indexing |
