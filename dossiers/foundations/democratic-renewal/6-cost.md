# Democratic renewal: cost

Role: section 6 of the democratic renewal foundation. It prices every provision of `4-specification.md` and `5-delivery.md` on federal fiscal years against the January 2029 law, sets each beside what the budget model books, and reports the fiscal-rule figures to the financing settlement (`charter/STANDARDS.md`, "Fiscal rule in dossiers: report, don't gate"; `DEC-2026-11-10-05`). Status: **draft** (stage F, step 6), on `DEC-2026-11-17-40` to `-99`, with the provisional items of sections 4 and 5 priced on their recommendations (part 7). **Nothing is booked here** and no adopted input changes: booking follows the milestone review (`charter/STANDARDS.md`, "Milestone review"), and part 9 lists what a booking would change. Every figure is project arithmetic or a restated outside score, not an official score.

## Counting rules

- **Conventions.** Federal cost, nominal $ billion by federal fiscal year (FY y runs from October of y−1), a cost positive, **on the general fund** unless a line says otherwise, against the January 2029 law.
- **The booked basis.** The budget model's central case, `mixed`, read from its audit lines (`legacy/sources/recovery-budget-audit.csv`) on main after #402, not rebuilt. CAP-7S and CAP-7 are booked at Espen's October 26 sizes through the model's line "Smaller capacity and AI authorizations", which scales the ledger rows ($560 billion and $456 billion) to $98.0 billion and $279.2 billion (`models/tools/budget/note-cap7-sizes.md`). This section quotes the scaled figures as the booked ones.
- **The plan-wide gap** is the general-fund primary balance of the whole plan in FY2040, case `mixed`: **$602.7 billion short** (1.11% of GDP; `models/data/recovery-budget-paths.csv`, `agenda_gf_primary_bn`, after #402; the board rounds it to $603 billion). Each share below is of that figure, on the same basis (additive on the primary balance before interest). It moves whenever another dossier is booked.
- **The draft scenario.** `models/tools/democratic_renewal_cost.py` lays the booked rows and the unbooked lines on fiscal years, so this section and a later booking read the same numbers (run it with no flag for the tables, `--check` for its self-checks). It reads the audit lines and writes nothing.
- **Spending, revenue and contingent money stay apart** (`dossiers/TEMPLATE.md`, "One basis for each fiscal figure", "Say what a model figure leaves out"). Revenue effects (the 1043 deferral, the IRS's enforcement yield) have their own lines. A reserve released only when its gates clear is shown from zero to its cap, never added to firm money. An authorization subject to appropriation is labeled so.
- **Ranges** run each line's low and high inputs together: a bound, not a probability interval.
- **What each input is** (commitment, working assumption, open question, study in implementation) is in part 10.

## 1. What is booked today, and what this foundation's provisions need

### 1.1 The booked rows

Nine ledger rows carry this foundation's provisions. On the booked basis, by fiscal year:

| Row | What it carries (section 4) | 2030 | 2031 | 2032 | 2033 | 2034 | 2035 | 2036 | 2037 | 2038 | 2039 | **FY2030-39** | **FY2040** |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DEM-1 | The democracy act's Divisions A to E: the floor, the Voting Rights titles, DEM-2, the match (INT-5), DISCLOSE and the rest of Division D, the riders | 0.8 | 0.9 | 0.9 | 0.9 | 1.0 | 1.0 | 1.0 | 1.1 | 1.1 | 1.1 | **10.0** | **1.22** |
| DEM-11 | Election administration: the block grant and the equipment fund (DEM-11.01, 11.02), the voter card inside | 1.8 | 1.8 | 1.9 | 1.9 | 2.0 | 2.0 | 2.1 | 2.1 | 2.2 | 2.2 | **20.0** | **2.26** |
| DEM-16 | Civic education grants (DEM-16.01) | 0.8 | 0.9 | 0.9 | 0.9 | 1.0 | 1.0 | 1.0 | 1.1 | 1.1 | 1.1 | **10.0** | **1.22** |
| DEM-17 | The libraries and public space capital fund (DEM-17.01), closed after FY2036 | 3.8 | 4.0 | 4.1 | 4.3 | 4.4 | 4.6 | 4.8 | — | — | — | **30.0** | **0** |
| DEM-3 | A larger House, from 2033 (DEM-3.01, a direction) | — | — | — | 1.3 | 1.3 | 1.4 | 1.4 | 1.5 | 1.5 | 1.6 | **10.0** | **1.65** |
| CRT-P1 | The court bills: judgeships, integrity, terms (CRT-1 to CRT-15) | 0.3 | 0.6 | 1.0 | 1.0 | 1.1 | 1.1 | 1.1 | 1.2 | 1.2 | 1.3 | **10.0** | **1.33** |
| CAP-8 | Congress's capacity (CAP-1 to CAP-6, CAP-14, CAP-15) and the civil service (CAP-8, CAP-9, CAP-12) | 1.8 | 3.6 | 3.8 | 3.9 | 4.1 | 4.2 | 4.4 | 4.6 | 4.7 | 4.9 | **40.0** | **5.09** |
| CAP-7S | The surge (CAP-7S.01, 7S.02), plus $5 billion advanced into FY2029 | 11.4 | 19.6 | 21.2 | 19.6 | 16.3 | 9.8 | — | — | — | — | **98.0** | **0** |
| CAP-7 | The sustained increase (CAP-7.01) | 8.6 | 17.8 | 27.7 | 28.7 | 29.8 | 30.9 | 32.1 | 33.3 | 34.5 | 35.8 | **279.2** | **37.20** |
| **All nine** | | **29.4** | **49.2** | **61.5** | **62.6** | **60.9** | **56.1** | **48.0** | **44.8** | **46.5** | **48.2** | **507.2** | **49.98** |

(Rows are rounded; totals are the model's. The FY2029 advance of $5 billion is the model's separate line, netted in FY2030, so the surge's lifetime cash is unchanged. INT-1, DEM-4, DEM-5 and DEM-6 are booked at zero.)

### 1.2 Each provision against its row

| Provisions | What they cost, FY2030-39 | FY2040 | Basis | Booked in | Against the booking |
| --- | --- | --- | --- | --- | --- |
| **The voting floor** (DEM-1.01 to 1.14, DEM-12.01, DEM-13.01; DEM-1F.01) | Rules on states, carried by DEM-11's money; federal cost near zero beyond it. DEM-13.01's paid time falls on employers | — | CBO: the 2022 Freedom to Vote: John R. Lewis Act, which joined this floor and the preclearance title, reduced the deficit by $131 million over 2022-2031 [EV-DEM-322]; the 2019 For the People Act's implementing costs were $2.4 billion over 2019-2024, $750 million of it election security grants [EV-DEM-320] | DEM-1, DEM-11 | Inside |
| **DEM-11.01 and 11.02**, the block grant (about $1.7-1.9 billion a year) and the equipment fund (about $100-300 million a year) | About **$20 billion** (working total; range about $10-40 billion, as $1-4 billion a year) | **$2.26 billion** | `DEC-2026-11-17-41`, `-94`; Stewart's replacement cost of $1-3 billion over a ten-year equipment life (`SRC-5386`, p. 6); federal election money since 2003 has been one-time: over $1 billion of security grants since 2018 [EV-DEM-171], $45 million in FY2026 [EV-DEM-017] | DEM-11 | Equal; the split inside it is a working figure until a county cost study replaces it |
| DEM-1.07, the free voter card | Well under $0.1 billion a year (judgment) | — | Mailing from records to every registrant over two cycles | DEM-11 | Inside |
| DEM-11.03, the records match's one-time build | About $0.2-0.5 billion once (judgment) | 0 | States reported about $249,000 on average to build online registration [EV-DEM-166] | CAP-13, inside CAP-7S | Inside the surge's state and local line |
| DEM-1.15, the EAC rebuilt | About $0.4 billion of staff [EV-DEM-329] | — | The EAC had $58.9 million in FY2026 [EV-DEM-347] | CAP-7, CAP-7S (part G's "FEC, EAC and the integrity units") | Inside |
| DEM-1.16 to 1.19, the Voting Rights titles; DEM-2.01 to 2.06, redistricting; DEM-4.01, the state option | About zero: DOJ's Civil Rights Division and the courts within their bases | — | No CBO score of the John Lewis bill alone exists [EV-DEM-323]; its preclearance title was in the 2022 score above | DEM-1 | Inside |
| DEM-2.05, commission start-up grants | Small; legacy "up to $0.01 trillion" (`domain-democracy.md`:110, estimate) | — | Few states will choose a commission in one cycle | DEM-1 | Inside DEM-1's range |
| **INT-5.01, the 6:1 match** | About **$6 billion** (range $4-12 billion) | About $0.6-1.2 billion | Part 2; CBO's H.R. 1 (2021) score scaled [EV-DEM-355] | DEM-1 ($10 billion, range to $40 billion) | Inside |
| INT-2.01, INT-6.01, INT-7.01, INT-8.01, INT-16.01, INT-14.03 (the FEC's duties) | FEC staff about $0.5 billion [EV-DEM-329] | — | The FEC had $80.9 million in FY2026 [EV-DEM-347] | CAP-7, CAP-7S | Inside |
| INT-15.01, shareholder authorization | About zero on the general fund | — | The SEC's staff are fee-funded (legacy, `capacity-recovery-components.csv`:136) | — | Not a general-fund cost |
| **The stock ban** (INT-1.01 to 1.06), with CAP-1.01 and CAP-14.01 in the same act | Near zero of spending; **revenue −$0.003 billion** (the 1043 deferral) | — | CBO: the ETHICS Act lowered revenue by $3 million over 2024-2034 and cost zero to $500,000 of appropriations [EV-DEM-325]; the Stop Insider Trading Act under $500,000 [EV-DEM-326]. OGE's staff are in the integrity line (about $2.1 billion) [EV-DEM-329]. Penalties (INT-1.04) are not counted as receipts: their purpose is compliance | INT-1 ($0); the integrity line in CAP-7 | Inside; the revenue effect is its own line, too small to book |
| INT-3, 4, 9, 10, 11, 12.02, 13, 14.01, 14.02 (the other ethics rules) | About zero beyond the integrity line | — | FinCEN's and the FARA unit's staff [EV-DEM-329] | CAP-7, CAP-7S | Inside |
| **DEM-16.01**, civic education; DEM-18.01, three national assemblies | About $10 billion (legacy, `domain-democracy.md`:261); the three pilots about $10-20 million once (judgment: 100 to 150 paid members over several weekends, facilitators, a published evaluation) | About $1.2 billion | Legacy estimate | DEM-16 | Inside |
| DEM-17.01, the capital fund | About $30 billion (range $20-50 billion), closed after FY2036 | 0 | Legacy, `domain-democracy.md`:267, estimate | DEM-17 (R3, borrowed under C32) | Equal |
| **DEM-17.02, the permanent library line** | **About $7.8 billion** (range $5.2-10.5 billion) | **About $0.9 billion** (range $0.6-1.2 billion) | Part 3 | — | **Unbooked** |
| DEM-3.01, the 2031 House review; DEM-4.02, DEM-9.01, DEM-8.02, the 2033 decisions | About $10 billion for member offices if the House grows from 2033 (legacy), plus a chamber build of plausibly $10-30 billion, unscored (legacy, `domain-democracy.md`:132) | About $1.7 billion | Legacy estimates | DEM-3 | The build is not in the row (part 4) |
| DEM-5.01, DEM-6.01, DEM-7.01, statehood and status | None in the window; Puerto Rico statehood's Medicaid, SNAP and tax effects are scored by CBO before the vote (DEM-6.01) | — | — | DEM-5, DEM-6 at zero | Part 4 |
| DEM-8.01, 10.01, 19.01, 20.01, INT-17.01, CRT-19.01 (state tracks) | None federally | — | Campaigns, not federal duties | — | — |
| **CRT-1.01, 71 judgeships**; CRT-13.01 | About **$0.4-0.6 billion** | About $0.08 billion | CBO: the JUDGES Act of 2024, 66 seats, $98 million of direct spending and $251 million subject to appropriation over 2024-2034 [EV-DEM-324]; per seat about $1.0-1.1 million a year on CBO's figures [EV-DEM-357], in three tranches (2030, 2033, 2035) | CRT-P1 | Inside, with room (part 4) |
| CRT-2.01 to 2.03, INT-12.01, CRT-3, 4, 6, 7, 11 (court integrity); CRT-15 (terms) | A few million dollars a year; the inspector general most of it | About $0.01 billion | CBO: S. 359 (2023) $5 million over 2023-2028, about $1 million for the code and disclosure [EV-DEM-327]; no score of a term statute exists | CRT-P1 | Inside |
| CRT-8.01, CRT-9.01, CRT-10.01, 10.02, CRT-17.01, CRT-18.01 (drafting rules, remedies, penalties, norms) | About zero | — | Drafting and forum rules | — | — |
| **CRT-5.01 to 5.08, the immigration court**: the judges and counsel | In IMM-1: the judge teams about $13.2 billion and counsel about $9.2 billion over FY2030-39 (`dossiers/immigration/6-cost.md`, part 1; CRT-P1's ledger note) | — | The immigration model | IMM-1 | Booked there |
| **CRT-5.09, the court's structure** | **About $6.9 billion** (range $3.2-9.7 billion) | **About $0.95 billion** (range $0.4-1.3 billion) | Part 3 | — | **Unbooked** (part 4: CRT-P1 has room) |
| **CRT-5.06, the judges' split** | **About −$4.3 billion over FY2036-39** (range −$3.5 to −$5.0 billion) | **About −$0.9 billion** | Part 5 | IMM-1 | A later tier-3 rebooking |
| **CRT-20.01, civil legal aid** | **About $4.6 billion** (range $2.3-8.5 billion) | **About $0.7 billion** (range $0.3-1.2 billion) | Part 3 | — | **Unbooked**; sized here for the first time |
| **CAP-7S.01, 7S.02, CAP-7.01 to 7.05, CAP-11.01, CAP-12.01, CAP-13.01** | The allocation, $54.8 billion of surge and $249.5 billion sustained ($32.5 billion in FY2040); the contingency the rest | | Part G [EV-DEM-328] [EV-DEM-329] [EV-DEM-330] | CAP-7S, CAP-7 | Part 1.3 |
| CAP-19.01 to 19.06, shared rule 5 | Inside part G's lines (OMB, the digital service corps, CAP-13's data agreements) | — | Agencies attribute about 73% of FY2021-24 overpayments to not using data they held [EV-DEM-291]; no saving is counted | CAP-7, CAP-7S | Inside |
| CAP-4.01, payments in a lapse | About zero expected; direct spending in a lapse year under CBO's convention [EV-DEM-315], repaid by the later appropriation | — | Part 6 | — | Not booked, correctly |
| CAP-8.01, CAP-9.01, the civil service | Small; MSPB's fast-track appeals unsized (MSPB had $51.5 million in FY2026 [EV-DEM-347]) | — | Study in implementation (part 1.3) | CAP-8 | Inside; MSPB a claim on the contingency |
| **CAP-1.01**, staff at real 1979 levels; CAP-14.01; CAP-2.01, OTA; CAP-3.01, CRS, GAO, CBO; CAP-15.01; CAP-17.01 | About $30-50 billion together (legacy: CAP-1 $0.02 trillion, about $1.5-3 billion a year; OTA under $0.01 trillion; the support agencies about $0.01 trillion; `domain-capacity.md`:61, :67, :75); the housing allowance about $10-15 million a year (judgment: about 500 members at a one-bedroom fair market rent) | About $4-5 billion | Legacy estimates; staffing counts not yet on one method (Evidence still needed) | CAP-8 ($40 billion, with the civil service's $0.01 trillion) | At or a little above the row (part 4) |
| **CAP-6.01, statute tracking** | **About $0.09 billion** (range $0.05-0.13 billion) | **About $0.01 billion** | $8 million a year (range $5-12 million), indexed; the Law Revision Counsel had $3.9 million [EV-DEM-339] and asked for $5.048 million for FY2025 [EV-DEM-340] | — (inside the legacy "about $0.00") | **Unbooked**, too small to move a total |
| CAP-5.01, CAP-16.01, CAP-18.01 (rules and preparation) | None | — | Chamber rules; outside government | — | — |
| CAP-10 (a direction) | In the international and education dossiers' lines | — | — | Theirs | — |

### 1.3 CAP-7S and CAP-7: booked, allocated, contingent

The booked rows hold more than part G's bottom-up allocation. Memo 10 part 1 B (`DEC-2026-11-17-58`) names the difference a delivery contingency, released by OMB only against a published written need (CAP-7S.02). So the booked figure is part firm and part contingent:

| | Surge (FY2029-35) | Sustained, FY2030-39 | FY2040 | Firm or contingent |
| --- | --- | --- | --- | --- |
| Booked (case `mixed`) | **$98.0 billion** (plus the $5 billion FY2029 advance, inside the lifetime) | **$279.2 billion** | **$37.2 billion** | — |
| Part G's allocation (CAP-7S.01, CAP-7.01) | $54.8 billion | $249.5 billion | $32.5 billion | Firm once appropriated, released against hiring paths (CAP-7.02) |
| **Memo 10's delivery contingency** (CAP-7S.02) | **$0 to $43.2 billion** | **$0 to $29.7 billion** | **$0 to $4.7 billion** | **Contingent**: released only against a published need, for enacted programs |
| #404's residual (stage G's options A to C) | $0 (A) to $7.0 billion (C) | $0 (A) to $20.8 billion (C) | $0 to $2.8 billion | **Not booked**; option B is about $3.5 billion and $20.6 billion. Under memo 10, A is enough: the allocation fits inside the booked figures |
| The legacy review's high case, for scale | $103.3 billion | $355.1 billion | — | The contingency covers the surge's high case without being spent by default [EV-DEM-328] |

- **The contingency is neither new money nor a saving.** It is inside the booked $98.0 billion and $279.2 billion. If none of it is released, outlays fall short of the booking by up to $72.9 billion over FY2030-39 and $4.7 billion in FY2040. This section does not count that as a saving: the booking is a ceiling a delivery failure would call on.
- **Its first known claims** (`5-delivery.md`, part 3.3), on the sustained side:
  - *Work:* FMCS about $0.1-0.2 billion (`work/4-specification.md`, part F); OSHA at the high end, up to about 400 more staff than part G's 700 (judgment: about $0.6-0.9 billion over the decade, at part G's Labor line of $4.6 billion for about 2,000 added staff [EV-DEM-329] [EV-DEM-331], ramped); the Office of Apprenticeship's staff once Labor's plan sizes them; the FLRA, small. About **$0.7-1.1 billion** in all so far, about 2.5-3.5% of the sustained contingency. The NLRB's $1.0-1.4 billion fits inside part G's $1.9 billion row and claims nothing.
  - *This foundation:* MSPB's fast-track appeals (CAP-9.01), after the first year's count; small.
  - *Care:* ACF's fallback staff, inside ACF's row first.
  - *Rural Development:* only if HOU-14.01's rebuild falls behind the front-door load.
- **A second, separate contingency is booked.** The budget model also carries Espen's October 26 "delivery contingency" of **$100 billion over FY2030-39 ($14.0 billion in FY2040)**, an "explicit allowance for unpriced health/delivery obligations; not added again within agency allocations" (`legacy/governing/project-2050-governing-decisions.md`:444; `recovery-adoption.json`, `delivery_contingency_tn` 0.1). It is not one of this foundation's rows, and memo 10 did not count it. The two answer overlapping risks: a delivery failure the agencies' lines do not cover. Together they hold up to about **$173 billion** over FY2030-39 and about **$19 billion** in FY2040 that no enacted program has yet claimed. **For stage G:** decide whether both are needed; if both stay, give each a written lane (memo 10's for agency delivery of enacted programs, the October 26 allowance for unpriced program obligations, health first), so one need is not claimed twice. This is reported, not changed.
- **SSA's line is gross; the booking already nets the OASDI share.** Part G's SSA line ($3.9 billion of surge, $31.0 billion sustained) is gross [EV-DEM-329]. The budget model already moves SSA's OASDI share of its administrative increase to the trust fund ("SSA OASDI capacity reclassification", **−$15.0 billion over FY2030-39 and −$1.7 billion in FY2040** on the general fund), on SSA's FY2026 administrative outlays: OASDI about 44%, Medicare about 25% (half of it HI, a working split) and SSI about 31% (`recovery-adoption.json`, `administration`). On those shares the trust funds would carry about 56% of part G's SSA line, about $17 billion of the $31.0 billion. The model's own SSA account is an incremental-workload proxy, so the two are close but not the same measure. A measured split stays Evidence still needed; the working split is the model's.
- **The IRS line carries a revenue effect booked elsewhere.** Part G gives the IRS $8.8 billion of surge and $94.2 billion sustained. Its enforcement yield is booked as revenue row G8 ($400 billion over FY2030-39, $54.8 billion in FY2040), less the model's "IRS yield allowance with smaller capacity budget" ($250 billion and $34.2 billion): a net **gain of about $150 billion and $20.5 billion**, on its own revenue line, never netted into CAP-7. The yield depends on the IRS hiring its path; in 2023 the IRS lost more revenue agents than it hired with the money in hand [EV-DEM-277]. A slow path delays the yield more than it saves outlays.

## 2. The match (INT-5.01)

The match is decided (memo 4 part 1 B, `-46`): 6:1 on in-state gifts up to $200, for House and Senate candidates who opt in, no spending cap, a payment ceiling set from the previous two cycles' spending in comparable races, paid from a fund the FEC administers out of general revenue (INT-5B). Its cost is a working assumption, checked here against the one outside score.

- **The outside score.** CBO estimated in March 2021 that H.R. 1's match, for House candidates only, up to $6 for every $1 from donors giving $200 or less, would cost about **$620 million for the 2028 election and about $850 million for the 2030 election**, about $1.6 billion over 2021-2031 (CBO, 2021) [EV-DEM-355]. That bill's match was not limited to in-state gifts.
- **Scaling it to this design** (project arithmetic, working assumption):
  - *Senate candidates added:* the cost rises by half to the whole of the House cost (judgment; Senate races raise less in small gifts per candidate but are statewide);
  - *in-state gifts only:* a share of 0.6 to 0.9 of small gifts is matched (judgment; out-of-state small giving is concentrated in a few national races);
  - so the 2030-cycle equivalent is about **$0.8-1.5 billion a cycle**, growing about 10% a cycle as participation and the ceilings rise.
  - *First matched cycle 2032:* the act is enacted by spring 2030 at the latest, and the FEC needs the fund, the qualifying rules and the payment system in place first, as CBO's own estimate assumed some years' lead.
- **Over FY2030-39:** four cycles (2032 to 2038), about **$6 billion (range $4-8 billion)**; with ceilings and participation at the high end, up to about $12 billion. **FY2040:** about $0.6-1.2 billion a year, averaged over the 2040 cycle.
- **Against the booking.** DEM-1 books $10.0 billion (range to $40 billion) for the democracy act, the match its only material cost. The central estimate fits inside it with room for DEM-2.05's commission grants; **the legacy high of $30 billion is not supported** by CBO's scale. A booking could narrow DEM-1's range to about $0.004-0.015 trillion; it need not change the midpoint.
- **Studied in implementation:** the first two cycles' participation and payments, published by the FEC, replace the scaling.

## 3. The unbooked lines, priced

Each is a permanent or multi-year line that sections 3 to 5 sent to stage G unbooked. The draft scenario lays them on fiscal years.

| Line | 2030 | 2031 | 2032 | 2033 | 2034 | 2035 | 2036 | 2037 | 2038 | 2039 | **FY2030-39** | **FY2040** | Range FY2030-39 | Range FY2040 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DEM-17.02, the permanent library line | 0.38 | 0.77 | 0.78 | 0.80 | 0.81 | 0.83 | 0.84 | 0.86 | 0.88 | 0.90 | **7.8** | **0.91** | 5.2 to 10.5 | 0.61 to 1.22 |
| CRT-5.09, the immigration court's structure | 0.05 | 0.15 | 0.75 | 0.77 | 0.80 | 0.82 | 0.84 | 0.87 | 0.90 | 0.92 | **6.9** | **0.95** | 3.2 to 9.7 | 0.44 to 1.33 |
| CRT-20.01, civil legal aid through LSC | 0.10 | 0.20 | 0.30 | 0.40 | 0.50 | 0.60 | 0.61 | 0.62 | 0.64 | 0.65 | **4.6** | **0.66** | 2.3 to 8.5 | 0.33 to 1.21 |
| CAP-6.01, statute tracking | 0.01 | 0.01 | 0.01 | 0.01 | 0.01 | 0.01 | 0.01 | 0.01 | 0.01 | 0.01 | **0.09** | **0.01** | 0.05 to 0.13 | 0.01 to 0.01 |
| **Unbooked, all** | **0.54** | **1.13** | **1.84** | **1.98** | **2.12** | **2.26** | **2.30** | **2.36** | **2.43** | **2.48** | **19.4** | **2.54** | **10.8 to 28.8** | **1.4 to 3.8** |

(Rows are rounded; totals are the scenario's sums.)

**Section 4's restatement, checked.** Section 4 put the three lines it could size (the library line, the court's structure, statute tracking) at "about $8-20 billion over FY2030-39 and about $1-2 billion in FY2040, plus legal aid once sized". On the paths above the same three are **about $14.8 billion (range $8.5-20.3 billion) and $1.9 billion (range $1.1-2.6 billion)**, so the check holds; the library line's first year is at half while its formula starts. With legal aid sized, **all four are about $19.4 billion (range $10.8-28.8 billion) and $2.5 billion in FY2040 (range $1.4-3.8 billion)**.

- **DEM-17.02, the library line** (`-99`, k). About $0.75 billion a year (range $0.5-1 billion, judgment) in FY2030 dollars, half in FY2030 as the formula starts, then indexed at 2%: about 2.8 to 5.6 times IMLS's $180.0 million of Grants to States in FY2024 [EV-DEM-338]. It is a permanent authorization paid by annual appropriation (Labor-HHS), so a booked figure would be the expected outlay at the authorized level, not an entitlement. **Unbooked; permanent, so paid for at maturity.** The size is a working assumption with no outside benchmark beyond today's line.
- **CRT-5.09, the court's structure** (memo 9 part 1 A′). A transition office in the Administrative Office in FY2030-31 (about $0.05-0.3 billion a year), then from FY2032, when the court takes over on October 1, 2031 (working), the court office (records, interpreters, space, filing, judicial education), the appellate panels and the restored federal-court review, at about $0.75 billion a year (range $0.35-1.05 billion), grown 3%. It is the structure only: **the judge teams and counsel are in IMM-1** (`dossiers/immigration/6-cost.md`, part 1), and EOIR's existing appropriation for adjudication moves with the court, so only the increment counts. EOIR received $790.0 million in FY2026 and the administration requests $889.0 million for FY2027 (CRS, 2026) [EV-DEM-354]; that base, and its growth with the judge corps, stays in the baseline and in IMM-1, and the structure line is the court's cost above it. Benchmarks: the Administrative Office's own appropriation was $107.0 million in FY2026 [EV-DEM-347]; EOIR's FY2024 request put court costs such as space buildout at 39% of a new judge team's cost and interpretation at 9% [EV-IMM-644], which IMM-1's team cost already carries. The immigration milestone review's re-score without the judges and counsel put the structure on the order of $3-10 billion (`dossiers/immigration/review-milestone.md`:186-195; `ledger-bills.csv`, CRT-P1's note). No CBO or judiciary estimate exists (Evidence still needed). **Unbooked;** part 4 shows CRT-P1's booked row has room for it.
- **CRT-20.01, civil legal aid** (memo 9 part 3 B). Memo 9 asked this section to size the schedule against provider capacity. Today: LSC received $580.0 million in FY2023, $560.0 million in FY2024 and FY2025, and $540.0 million in FY2026 (CRS, 2026) [EV-DEM-352], and its grantees work from over 900 offices in every state and territory (LSC) [EV-DEM-358]. The administration's FY2027 request is $21.0 million, for an orderly closure (second Trump administration, 2026) [EV-DEM-352] [EV-DEM-353]. **The cost depends on the January 2029 baseline:** priced here against LSC continuing at about its FY2026 level; if LSC is closed or cut before 2029, restoring it first adds about $0.55 billion a year (about $5.5 billion over FY2030-39) before the schedule below begins (open question, settled by the FY2027 and FY2028 appropriations). The working schedule: LSC's appropriation rises in six equal steps to **about $0.6 billion a year above its FY2029 level by FY2035** (range $0.3-1.1 billion), then is indexed at 2%, each step released as grantees report hiring against their plans. LSC funded about 4,591 attorneys in 812 offices in 2015, the latest count in the register [EV-DEM-349]. Growth faster than providers can hire is the failure to avoid: New York's eviction right outran its lawyers, with representation falling to 30% by March 2025 [EV-DEM-243]. Low-income Americans get no or not enough help for 92% of their substantial civil legal problems (LSC's survey; it has a stake) [EV-DEM-240]. **Unbooked, and an appropriation each year, so contingent on each step's release:** the central figure is the expected outlay if grantees hire on the path; a slow path delays it.
- **CAP-6.01, statute tracking** (`-99`, t). About $8 million a year (range $5-12 million), indexed: 20 to 40 lawyers and analysts plus $1-2 million of data and software, against the Law Revision Counsel's $3.9 million [EV-DEM-339]. **Unbooked**, and too small to change any total; it can ride CAP-8's row at booking.

## 4. Where the booked rows and the specification differ

- **CRT-P1 has room for the court's structure.** The row books **$10.0 billion over FY2030-39 and $1.33 billion in FY2040** for the court bills. Section 4's contents cost far less: the judgeships about $0.4-0.6 billion [EV-DEM-324] [EV-DEM-357], the integrity act's inspector general and publication duties a few million dollars a year [EV-DEM-327], the terms statute about zero. That is **about $0.5-0.7 billion over FY2030-39 and about $0.09 billion in FY2040**, leaving about **$9.3-9.5 billion and $1.24 billion** the row's contents do not use. The legacy row was sized when it carried more of the court program: its note says CRT-5's legacy figure included the judge corps and counsel, now in IMM-1. The court's structure, about $6.9 billion (range $3.2-9.7 billion) and $0.95 billion, fits inside that room. **For the booking step,** two readings: (a) re-label CRT-P1 to carry CRT-5.09 as well, adding nothing; or (b) cut CRT-P1 to its contents and book CRT-5.09 as its own row. Either way the net change is about **−$2.5 billion over FY2030-39 (range −$6.3 to +$0.4 billion) and about −$0.3 billion in FY2040**, so **the unbooked court structure does not add to the plan-wide gap at the central estimate.** This section reports it and does not rebook.
- **DEM-1 carries the match and little else** (part 2).
- **CAP-8 is at or a little below its contents' high end.** The legacy estimates for Congress's capacity (CAP-1 to CAP-3, CAP-14, CAP-15: about $0.03-0.04 trillion) plus the civil service ($0.01 trillion) sum to the row's $0.04 trillion at the low end and up to about $0.05 trillion if CAP-1 reaches $3 billion a year. CAP-1.01's "real, not nominal, 1979 levels" (`-89`) is the swing item; a count of 1979 staff and pay on one method would settle it (Evidence still needed).
- **DEM-3's row does not hold the chamber build.** It books member offices for a larger House from 2033. The Architect of the Capitol's build, plausibly $10-30 billion (legacy, unscored), is outside it. The 2031 review (DEM-3.01) decides the size, and the democracy act directs the Architect's report by 2030, which is the cost study. Not added here: the size is a direction, and the build is capital to be priced when the report exists (open question).
- **DEM-6's row is zero, correctly for the window.** Puerto Rico statehood's fiscal effect (full Medicaid and SNAP, federal tax) begins only after a vote and admission, and CBO scores it first (DEM-6.01). If statehood were enacted in the window, it would be a large separate line for that bill.

## 5. IMM-1's effect from memo 9 part 2 (not booked)

Memo 9 part 2, as Espen changed it (`DEC-2026-11-17-56`; CRT-5.06), puts about 200 of the about 920 added judges on regular 14-year terms and the rest on temporary terms that end when the backlog clears. Against IMM-1's booked judge teams, which keep every added judge until attrition:

| | FY2036-39 | FY2040 | Basis |
| --- | --- | --- | --- |
| Every added judge on a temporary term (memo 9 part 2 B as recommended) | −$5.5 billion | −$1.1 billion | `immigration_model.term_increment`: −$5.55 billion and −$1.06 billion |
| **As decided: about 720 of 920 temporary** | **about −$4.3 billion** (range −$3.5 to −$5.0 billion) | **about −$0.9 billion** (range −$0.7 to −$1.05 billion) | About 78% of the all-temporary saving (project arithmetic, working assumption) |

- It is **a later tier-3 rebooking of IMM-1**, not booked here: IMM-1's judge-team component falls by these amounts. The scenario's yearly shape (rising from FY2036 as the backlog clears) is illustrative; only the totals come from the immigration model.
- **Share of the gap:** about −0.15% of the FY2040 plan-wide gap.
- The corps is reset in 2033 from receipts after legalization (CRT-5.06), so the rebooking should wait for that reset or be revised at it.

## 6. Benchmarks against outside scores

| Provision | Outside score | What it says | Fit |
| --- | --- | --- | --- |
| The voting floor with the Voting Rights titles | CBO and JCT, Freedom to Vote: John R. Lewis Act, House-passed January 2022 [EV-DEM-322] | −$131 million net over 2022-2031; revenue +$3.1 billion | The floor's own federal cost is small; DEM-11's recurring grant is the plan's addition, which that bill did not carry |
| The 2019 For the People Act (H.R. 1) | CBO, March 2019 [EV-DEM-320] | $2.6 billion authorized and $2.4 billion of costs over 2019-2024, $750 million of it election security grants; public financing not scored | One-time grants; DEM-11 is recurring by decision (`-94`) |
| The 2021 For the People Act (H.R. 1 and S. 1) | CBO's 2021 score, as the National Taxpayers Union Foundation reports it [EV-DEM-321] | $2.2 billion of direct spending and $3.2 billion of fines and revenue over ten years, net −$999 million; NTUF counts at least $5.4 billion more that CBO did not score | The match was financed by a fines surcharge there; here by general revenue (INT-5B) |
| Election administration's need | Institute for Responsive Government and the Project for Election Infrastructure (advocates for federal election funding; no method published) [EV-DEM-356] | More than $50 billion over ten years; an average federal election year costs $4-6 billion | DEM-11's $20 billion is about two-fifths of the advocates' figure; it is a federal share of running costs, not the whole need. One source's view, from a publisher with a stake |
| The EAC's grants | EAC [EV-DEM-171]; appropriations [EV-DEM-017] | Over $1 billion of HAVA security grants since 2018; $45 million in FY2026 | DEM-11's $2 billion a year is about 40 times FY2026's grant: the recurring need, not a one-time top-up |
| The stock ban | CBO, ETHICS Act (2024) [EV-DEM-325]; Stop Insider Trading Act (2026) [EV-DEM-326] | −$3 million of revenue over 2024-2034; under $500,000 of administration | INT-1 at zero holds |
| Judgeships | CBO, JUDGES Act of 2024 [EV-DEM-324] | $349 million over 2024-2034 for 66 seats | About $0.4-0.6 billion for 71 seats over FY2030-39 |
| A new district judgeship | CBO, JUDGES Act of 2024, on the Administrative Office's figures [EV-DEM-357] | $275,000 a judge in 2025 rising to $340,000 by 2034; a new court about $750,000 in its first year and about $700,000 a year after | About $1.0-1.1 million a seat-year: about $0.5-0.6 billion over FY2030-39 for 71 seats in three tranches, a little above the scaled 2024 total |
| Court ethics and the inspector general | CBO, S. 359 (2023) [EV-DEM-327] | $5 million over 2023-2028 | A few million dollars a year |
| Funding lapses | CRS on CBO's treatment of automatic continuing resolutions [EV-DEM-315] | Scored as new direct spending | CAP-4.01 continues three kinds of payment only; its score is the lapse year's continued payments, which the later appropriation repays |
| The bases of this foundation's bodies | CRS's FY2026 tables [EV-DEM-347] | EAC $58.9 million, FEC $80.9 million, OGE $23.0 million, MSPB $51.5 million, AO $107.0 million | The rebuild's regulator and integrity lines (about $3.0 billion over the decade) are several times today's bases: the restoration part G sized |
| Legal aid | CRS's appropriations tables [EV-DEM-352] | LSC $540.0 million in FY2026; $21.0 million requested for FY2027, for closure [EV-DEM-353] | The schedule roughly doubles LSC by FY2035 if LSC continues; restoring a closed LSC would come first |

No outside score exists for the Voting Rights titles alone [EV-DEM-323], a term statute for the Justices, the immigration court's structure, the library line, or the agency rebuild as designed (the legacy second-round review is the project's own, grade D [EV-DEM-328]).

## 7. The provisional items, priced on their recommendations

Each is drafted on the recommendation, marked provisional under the overnight relay and listed for Espen in the PR's "For the board". **None is a choice mainly about money**, so none goes to Espen as a cost question (`charter/STANDARDS.md`, "Fiscal rule in dossiers").

| Item | Recommendation | Cost on the recommendation | Cost on the alternative |
| --- | --- | --- | --- |
| **INT-1.01**, self-directed retirement accounts (section 4, question 1) | New purchases of individual stocks in a self-directed account count under the ban; existing holdings and plan-managed accounts never | **About zero.** A sale inside an IRA is not taxed, so the 1043 deferral is not engaged; the ethics offices read the same filings | About zero |
| **Fix 1, CAP-7.02's start rule** (section 5, part 8) | A program whose agency is behind follows its own statute: it starts later where the statute lets it; where the statute fixes the date, the date holds and the corrective plan, the contingency and the flagship's backstop come first. **This amends a sentence of decided memo 10 B** ("A program whose agency is behind starts later; it does not shrink", `memos/10-capacity-size-and-pace.md`:50), which Espen chose | **No change to any total.** It can bring forward a claim on the contingency (part 1.3) for care's and housing's fixed dates, within the contingency's cap | Memo 10 B as written: a late agency delays every program, which defers outlays (a timing effect, not a saving) but breaks care's and housing's statutes |
| **Fix 2, CRT-5.03's interim appointments** | Unscreened sitting judges continue up to two years at the transfer | **Zero:** the judges are already paid in IMM-1; it avoids a gap in the corps that would add to the backlog | A gap would push the backlog's clearance, and IMM-1's judge years, later |
| **Fix 3, DEM-1.13's enforcement** | The Attorney General, or a voter after notice and a period to correct, may sue | **About zero** federally: DOJ's Civil Rights Division within its base; fee awards to prevailing voters would fall on states that do not comply. The National Voter Registration Act's model, which fix 3 copies, gives 90 days after written notice to correct, 20 days within 120 days of a federal election, and no notice within 30 days of one (52 U.S.C. 20510(b)) [EV-DEM-351]. | None; an unenforced mandate |
| **Fix 4, the 60-day payment clock** (DEM-11.01, CAP-13.01) | Formula money paid within 60 days, enforceable by the recipient | **Zero** on the totals; outlays land earlier within each fiscal year, not in a different one | Payments an unwilling administration could slow |
| **The floor's effective dates** (section 5, question 2) | Barrier-removing rules for any federal election 180 days after enactment; systems rules by the 2032 general election | **No change:** DEM-11's grant starts in FY2030 either way, and the records build (DEM-11.03, about $0.2-0.5 billion) falls in FY2030-31 inside CAP-13 | Every rule for 2030 would pull the records build and the voter card's mailing into FY2030 inside the same lines: a higher risk of failed launches, not a higher total |

## 8. The fiscal-rule report

One basis throughout: federal fiscal years, $ billion, a cost positive, on the general fund, against the budget model's booking (case `mixed`, on main after #402).

| Measure | FY2030-39 | FY2040 (permanent) | Share of the FY2040 plan-wide gap ($602.7 billion) |
| --- | --- | --- | --- |
| **Booked rows that carry this foundation** (part 1.1) | **$507.2 billion** | **$50.0 billion** (0.092% of GDP) | **8.3%** |
| *of which* firm (all but memo 10's contingency) | $434.3 billion | $45.3 billion | 7.5% |
| *of which* memo 10's delivery contingency, inside the booking | $0 to $72.9 billion | $0 to $4.7 billion | 0 to 0.8% |
| **Unbooked lines** (part 3), for stage G | **about +$19.4 billion** (range +$10.8 to +$28.8 billion) | **about +$2.5 billion** (range +$1.4 to +$3.8 billion) | **about 0.42%** (range 0.23-0.63%) |
| *of which* the court's structure, which fits inside CRT-P1's booked row (part 4) | about +$6.9 billion | about +$0.95 billion | about 0.16% |
| **Unbooked, net of CRT-P1's room** | **about +$12.5 billion** | **about +$1.6 billion** | **about 0.26%** |
| Revenue effect: the 1043 deferral (INT-1.03) | about +$0.003 billion | about zero | about zero |
| Later tier 3: IMM-1 lowered for the judges' split (part 5) | about −$4.3 billion (FY2036-39) | about −$0.9 billion | about −0.15% |
| Not booked, stage G's choice: #404's residual | $0 to $27.8 billion | $0 to $2.8 billion | 0 to 0.46% |
| For reference, booked elsewhere: the October 26 delivery contingency (not this foundation's row) | $100.0 billion | $14.0 billion | 2.3% |
| For reference, booked elsewhere: IRS enforcement revenue net of its allowance (G8) | about −$150 billion (a gain) | about −$20.5 billion | about −3.4% |

- **The yearly cost** of the booked rows peaks with the surge, at about $63 billion in FY2033 (part 1.1), and settles near $45-50 billion a year from FY2036. The unbooked lines add about $0.5 billion in FY2030, rising to about $2.5 billion a year by FY2039.
- **Permanent cost from FY2040:** about **$50 billion a year** booked (CAP-7's $37.2 billion the largest), plus about $2.5 billion a year unbooked ($1.6 billion net of CRT-P1's room), rising with prices; the surge and the capital fund have ended.
- **Share of the plan-wide margin:** this foundation's booked rows are about 8.3% of the FY2040 gap, almost all of it the agency rebuild every flagship relies on. The unbooked lines would add about 0.4%, or about 0.3% net of CRT-P1's room; the IMM-1 rebooking would take about 0.15% off.
- **Report, don't gate** (`DEC-2026-11-10-05`). None of these is a defect to fix here. The one question mainly about money, whether the plan needs both delivery contingencies (part 1.3), is stage G's.

## 9. What a booking would change (proposed, not made)

Tier 3, after the milestone review. This PR changes nothing in `models/data/inputs/`.
1. **New rows** in `ledger-bills.csv` for DEM-17.02 (about $0.008 trillion, range $0.005-0.010 trillion, CPI-indexed, permanent) and CRT-20.01 (about $0.005 trillion, range $0.002-0.008 trillion, stepped to FY2035, then indexed), with year shapes from `models/tools/democratic_renewal_cost.py`.
2. **CRT-P1** re-labeled to carry CRT-5.09, or cut to its contents with CRT-5.09 as its own row (part 4); either way about the same net. The row's note and `ledger-conflicts.csv` line 28 ("CRT-5 is unscored") updated to cite this section.
3. **CAP-6.01** inside CAP-8's row, with no change in amount.
4. **IMM-1's judge-team component** lowered by about $4.3 billion over FY2036-39 and $0.9 billion in FY2040 (part 5), with the 2033 reset noted.
5. **CAP-7S and CAP-7:** no change in size. Their ledger notes still describe $0.60 trillion and 0.12% of GDP; bringing the rows to the booked sizes and dropping the CAP part of the scaling line is the clean-up `note-cap7-sizes.md` names, best done with stage G's choice on #404's residual. CAP-7S.02's contingency is recorded in the rows' notes as inside the booking, not added.
6. **For stage G, not a row:** the two delivery contingencies (part 1.3); INT-5B's payer, and DEM-1's range narrowed to the match's (part 2); LSC's January 2029 baseline (part 3); the House chamber build once the Architect reports (part 4).

## 10. What each figure is

| Input | Treatment (`DEC-2026-11-10-07`) |
| --- | --- |
| What each provision commits to; the allocation of CAP-7S and CAP-7 by part G's table; the contingency's release rule; the match's design (6:1, $200, in-state, no spending cap); DEM-11's form (block grant plus equipment fund) | Commitments (decided) |
| DEM-11 at about $2 billion a year (range $1-4 billion) and its split | Working assumption; a county cost study replaces it (study in implementation) |
| The match's cost | Working assumption (part 2); the first two cycles' participation answers it (study in implementation) |
| The library line's size ($0.5-1 billion a year) | Working assumption on Espen's direction (`-99`, k) |
| The court's structure ($3.2-9.7 billion) and its timing from October 1, 2031 | Working assumptions (judgment on the immigration review's re-score); an estimate from the judiciary or CBO is Evidence still needed |
| Legal aid's schedule (+$0.3-1.1 billion a year by FY2035) | Working assumption; each step's release is a study in implementation, on grantees' hiring reports |
| Statute tracking ($5-12 million a year) | Working assumption on the Law Revision Counsel's budget |
| The judges' split against IMM-1 (−$3.5 to −$5.0 billion) | Working assumption (project arithmetic on the immigration model); reset in 2033 |
| CRT-P1's room and the two readings at booking | Open question, for the booking step |
| Congress's capacity (CAP-1 to CAP-3) at $0.03-0.05 trillion | Working assumption on legacy estimates; staffing counts on one method are Evidence still needed |
| SSA's trust-fund split | Working assumption (the model's FY2026 outlay shares); a measured split is Evidence still needed |
| How much of memo 10's contingency is released | Study in implementation (OMB's published releases, GAO's yearly audit, CAP-7.05) |
| Whether both delivery contingencies are needed | Open question, for stage G |
| #404's residual (options A to C) | Open question, for stage G |
| MSPB's fast-track load | Study in implementation |
| The House chamber build | Open question until the Architect's 2030 report |

## Evidence still needed

- An estimate of the immigration court's structure from the judiciary or CBO (CRT-5.09).
- A county or state study of election costs per registered voter (DEM-11).
- LSC's current grantee and attorney counts (the register's latest is 2015 [EV-DEM-349]) and the January 2029 baseline for LSC (CRT-20.01).
- FEC data on small (unitemized) gifts to House and Senate candidates by state of the donor, to replace the match's scaling (INT-5.01).
- CBO's H.R. 1 (2021) and JUDGES Act (2024) estimates saved as texts (cbo.gov blocks downloads; read through a search tool) [EV-DEM-355] [EV-DEM-357].
- Congressional staffing in 1979 and today, and pay, on one method (CAP-1.01, CAP-3.01).
- SSA's measured administrative split by trust fund (CAP-7.01).
- CBO's full estimates of the 2019 and 2021 For the People Acts and of S. 1498 (cbo.gov blocks downloads).
