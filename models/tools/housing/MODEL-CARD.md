# Housing model: model card

Role: the model card of `MOD-housing`, which rebuilds the housing flagship's cost (`dossiers/home/6-cost.md`) from its inputs and adds how many households the rent awards reach and what they may do to rents where supply is short, for the dossier, the budget model's housing rows and readers who want to check them (`charter/PLAN.md` 3.4; memo H5 A, `DEC-2026-11-25-22`). Status: **exploratory** (set 2026-11-25, step H7: new, with tests and validation tables; the booked housing figures do not rest on it, and it stays below "working" until the reviewer has tried to break it). Owner: the Project 2050 lead session (Claude Code), through GitHub issues on this repository. Version: 0.1.0, see `CHANGELOG.md`. License: as decided in `DEC-2026-11-25-33` (code Apache 2.0, writing CC BY 4.0, parameter and data files CC0); the license files arrive with step H2b. Every output of this model is analysis of the evidence, not an official score or a benefit determination; its results files carry that line in their header.

## What it answers

For FY2030-45 (federal fiscal years; FY2030-39 is the window, FY2040 the first year of the maturity test), in nominal dollars, a cost positive, against current law as it will stand in January 2029 and the adopted baseline (CBO, February 2026):
- **The federal cost of each provision in `6-cost.md` section 1.2**, line by line, and the totals: about **$0.81 trillion over FY2030-39** (model $807 billion; low $602 billion, high $1,157 billion) and about **$121 billion in FY2040**. 26 of the 35 lines are built from their inputs; 9 are taken as published (`published.csv`) because the dossier states no build that can be rerun (the zoning reward's lag, the federal builder, FHA's credit-reform score, the tax credits, and five small lines).
- **The cost at another lease-up rate** (`--leased`), which reruns every rental line: section 1.4's table and headline readings (about $0.76 trillion at 75%, $0.70 trillion at 57%).
- **How many households the rent awards reach**, by stage and year (about 0.9 million from the first million by FY2034; about 3.4 million by FY2040 and 3.6 million by FY2042 before the financing settlement capped stage 2), and **by income band where HUD's counts allow**: stages 2 and 3 are extremely low income by rule, and together reach about 46% of the 5.8 million extremely low-income renter households with worst case needs. Also the emergency fund's households a year, the repair fund's homes and the down payment help's buyers.
- **Rents where supply is short**: how much of the added rent subsidy landlords could capture as higher rents in tight and other markets, and the rent unassisted low-income renters could pay, as ranges from the register (`rents`). They are never added to the cost.
- **Supply only as a range from the evidence** (`rents.supply_range`): the homes the plan pays for directly (the decided target, 0.8-1.9 million) and the net homes that adds to the stock (0 to about 0.65 million). Not a forecast.

## What it cannot answer

- **It does not score anything officially.** The rental lines are the dossier's arithmetic rebuilt; the credit lines (HOU-3C.02, HOU-10.02, HOU-14.02) are not CBO credit-reform scores, and the tax credits (HOU-2D) are not a JCT score.
- **It does not forecast rents or housing supply.** The rent readings are bounded transfers on the added subsidy, not a path of market rents; supply is the evidence's range, with no year path.
- **It does not model behavior** beyond the dossier's fixed shares: take-up, lease-up and household formation are inputs, not responses. When help becomes a right in 2037, families now doubled up may form households and apply (7-validation.md 1.3's count risk); only the wider entry's count covers part of that.
- **It does not price the financing settlement's restatement** (`DEC-2026-11-24-09`, S11: stage 2 a capped program, about 810,000 families in FY2040, the duty to house dropped). The budget model books that; this model prices the design as 6-cost.md does.
- **It does not determine anyone's eligibility.** Who qualifies for which stage is the dossier's rule (`4-specification.md`, HOU-4.03), not a model output.
- **It does not count offsetting savings** (shelter, Medicaid) or interest on the added borrowing, as a CBO score does not.
- It never produces an official score or an individual benefit determination.

## Evidence map

Generated from the parameter files by `python3 models/tools/housing/test_housing.py --write-card`. Write nothing by hand between the markers.

<!-- generated:parameters:start -->
**`parameters.csv`** (the judgment inputs of the rental help lines, the stages' counts and the indexation rates). 22 inputs: 1 traced to evidence, 0 policy parameters, 0 calibrated to a benchmark, 21 labeled assumptions with a tested range.

| ID | Value | Unit | Year | Kind | Source or basis | Range |
| --- | --- | --- | --- | --- | --- | --- |
| `subsidy_fy2030` Rent subsidy per leased household | 17000 | $ per leased household-year | FY2030 | assumption | 6-cost.md 1.1: HUD's 2023 spending per voucher unit, $1068 a month (EV-HOU-370), grown 4% a year to 2030; range is price growth of 2.3% to 5% a year from 2023 (EV-HOU-187) | 15500 to 18500 |
| `subsidy_growth` Growth of the subsidy after FY2030 | 0.03 | share a year | FY2031-FY2045 | assumption | 6-cost.md 1.1: legacy planning input (legacy/domains/domain-housing.md HOU-4A); low is CPI (ASM-CPI-PATH) | 0.023 to 0.04 |
| `leased_share` Share of awards leased at steady state | 0.9 | share | none | assumption | 6-cost.md 1.1 and 1.4: national vouchers 84% occupied (EV-HOU-370); section 5's fees, search help, over-issue and reallocation should do better (judgment); EHV 67% after two years (EV-HOU-345) | 0.84 to 0.98 |
| `lag_months` Time from award to lease | 6 | months | none | assumption | 6-cost.md 1.1: EHV took 77 days from issuance to lease (EV-HOU-344); central is judgment | 3 to 9 |
| `fee_rate` Housing agency fees | 0.081 | share of subsidy | none | assumption | 6-cost.md 1.1: the legacy fee allowance ($12.2B on $150B), working assumption; 9.5% if it was set at prorated rates (EV-HOU-343) | 0.07 to 0.1 |
| `issuance_fee` Issuance fee per new award | 750 | $ per award | none | assumption | 6-cost.md 1.1: judgment | 500 to 1000 |
| `search_help` Search help (HOU-4.07) | 2000 | $ per award or reissue | FY2030 | assumption | 6-cost.md 1.1: judgment, pending section 4's design research; includes the landlord damage and vacancy fund; grows with the subsidy | 1000 to 3500 |
| `reissue_rate` Reissues a year | 0.1 | share of leased households a year | none | assumption | 6-cost.md 1.1: judgment (not varied in the dossier's low and high) |  |
| `payment_standard_uplift` Payment standards up to 120% where lease-up is low | 0.03 | share of rent subsidy | none | assumption | 6-cost.md 1.2: about a quarter of awards in low lease-up markets with limits about 10% higher raise the subsidy about 3% overall (judgment) | 0.01 to 0.06 |
| `stage2_pool_m` Stage 2's first count (memo 2) | 1.2 | million families | 2034 | assumption | 6-cost.md 1.3: HUD's 1.717 million ELI families with children with worst case needs (EV-HOU-186) less the families the first million reaches, memo 2's split | 1.0 to 1.5 |
| `stage2_takeup` Stage 2 families who apply | 0.85 | share | none | assumption | 6-cost.md 1.3; DEC-2026-11-10-03 (question 7: 85% central, full sign-up the cautious reading); no take-up evidence for a housing right in the register | 0.7 to 1.0 |
| `duty_leased_share` Stage 2's leased share under the duty to house | 0.95 | share | FY2037-FY2045 | assumption | 6-cost.md 2.5: placements lift stage 2's leased share from 90% to about 95% from FY2037 (judgment) | 0.93 to 0.98 |
| `wider_pool_m` Stage 2's wider entry: families with no home of their own | 0.4 | million families | 2034 | assumption | 6-cost.md 2.7; research-doubled-up.md section 7 (grade D): a doubled-up stock of about 0.3 million and one year's flow of about 0.1 million homeless families (EV-HOU-427) | 0.23 to 0.75 |
| `stage2_restated_total_m` Stage 2 restated: the whole count | 1.6 | million families | 2034 | assumption | 6-cost.md 2.12: about 1.6 million of the 1.717 million (EV-HOU-186) remain once stage 1, uncapped, takes the first million (1.4-1.8 million); the line prices the families above memo 2's first count (stage2_pool_m) | 1.4 to 1.8 |
| `added_search_award_only` Search help for stage 2's added families | 2000 | $ per award | none | assumption | 6-cost.md 2.7: search help for the wider entry and the restated count, about $0.7 billion on the central count (awards only, not grown; judgment) | 1000 to 3500 |
| `stage3_under62_m` Stage 3 under 62: households applying | 0.6 | million households | 2038 | assumption | 6-cost.md 2.1: HUD's 1.162 million very low-income renter households with a disabled member under 62 and worst case needs (EV-HOU-371), less 345,000 families with children, at a 69-85% ELI share (EV-HOU-185) and 85-100% applying | 0.45 to 0.8 |
| `stage3_older_eligible_m` Stage 3's disabled renters 62 and over: eligible | 0.77 | million households | 2038 | assumption | 6-cost.md 2.12: 1.749 million older ELI worst-case households (EV-HOU-186) at a 47% disability share (35-67%; EV-HOU-786), less 57,000 counted under 62 (EV-HOU-371) | 0.55 to 1.1 |
| `stage3_older_takeup` Stage 3's older group who apply | 0.85 | share | none | assumption | 6-cost.md 2.12: the convention Espen set for stage 2 (DEC-2026-11-10-03) | 0.7 to 1.0 |
| `stage3_older_cost_ratio` Older group's cost per household against the under-62 group's | 0.9 | ratio | none | assumption | 6-cost.md 2.12: older renters' incomes are mostly above SSI's (EV-HOU-372), so their rent share is higher (judgment) | 0.85 to 1.0 |
| `standing_fund_growth` Emergency fund indexation | 0.023 | share a year | none | assumption | 6-cost.md 2.2: indexed to prices (ASM-CPI-PATH) |  |
| `property_tax_growth` Property-tax growth | 0.04 | share a year | none | evidence | EV-HOU-670 (6-cost.md 2.9: the match grows about 4% a year with property taxes) |  |
| `backstop_growth` HUD services backstop growth | 0.03 | share a year | none | assumption | 6-cost.md 2.3: placeholder (judgment) |  |

**`plan.csv`** (the plan's decided amounts and schedules, held fixed across the cases). 74 inputs: 0 traced to evidence, 74 policy parameters, 0 calibrated to a benchmark, 0 labeled assumptions with a tested range.

| ID | Value | Unit | Year | Kind | Source or basis | Range |
| --- | --- | --- | --- | --- | --- | --- |
| `awards_4a_per_year` HOU-4A.01: new awards a year | 250000 | awards | FY2030-FY2033 | policy | DEC-2026-11-09-01 (memos 1 and 2 keep the count and pace); DEC-2026-11-09-06 |  |
| `awards_4a_first_month` HOU-4A: first awards (month 6 of FY2030 = April 2030) | 6 | months after October 1 2029 | FY2030 | policy | DEC-2026-11-09-10 (R1 readiness); 6-cost.md 1.1: R2 signed about January 14 2030, first awards from April 2030 (5-delivery.md's later central run) |  |
| `stage2_cap_per_year` HOU-4D.01: enrollment cap | 300000 | families | FY2034-FY2036 | policy | DEC-2026-11-09-01 (memo 2 B: up to 300,000 a year from 2034, complete in 2037) |  |
| `stage2_right_fy` HOU-4D.01: the year stage 2 becomes a right | 2037 | fiscal year | none | policy | DEC-2026-11-09-01; DEC-2026-11-09-10 (the right and its duty to house) |  |
| `stage3_first_fy` HOU-4.08: stage 3 opens; enrolled a third a year over FY2038-40 | 2038 | fiscal year | none | policy | DEC-2026-11-09-06; DEC-2026-11-10-03 (stage 3 from 2038, disabled renters of every age) |  |
| `emergency_start_ba` HOU-1D.04: one-time start | 15 | $ billion | FY2030 | policy | DEC-2026-11-10-03 (question 4: about $15 billion one-time start) |  |
| `emergency_start_spend` HOU-1D.04: share spent | 0.3 | share | FY2030 | policy | DEC-2026-11-10-03; 6-cost.md 2.2 (spend-out 30%, 50%, 20%: judgment) |  |
| `emergency_start_spend` HOU-1D.04: share spent | 0.5 | share | FY2031 | policy | DEC-2026-11-10-03; 6-cost.md 2.2 (spend-out 30%, 50%, 20%: judgment) |  |
| `emergency_start_spend` HOU-1D.04: share spent | 0.2 | share | FY2032 | policy | DEC-2026-11-10-03; 6-cost.md 2.2 (spend-out 30%, 50%, 20%: judgment) |  |
| `standing_fund_ba` HOU-1D.01-.03: standing fund, first year | 5 | $ billion a year | FY2031 | policy | DEC-2026-11-10-03 (question 4: about $5 billion a year from FY2031, indexed to prices) |  |
| `revolving_grants_ba` HOU-3C.01: state revolving fund grants, awarded evenly | 72 | $ billion | FY2030-FY2037 | policy | DEC-2026-11-09-09 (awarded FY2030-37) |  |
| `public_housing_ba` HOU-5.01: public housing repair, awarded evenly | 58 | $ billion | FY2030-FY2037 | policy | DEC-2026-11-09-09 (about $7.25 billion a year more than FY2026, FY2030-37) |  |
| `capital_spend_y0` HOU-3C.01 and HOU-5.01: share spent in year 0 after award | 0.15 | share | none | policy | DEC-2026-11-09-09 (award schedule); 6-cost.md 1.2 (spend-out 15%, 35%, 30%, 20%: judgment) |  |
| `capital_spend_y1` HOU-3C.01 and HOU-5.01: share spent in year 1 after award | 0.35 | share | none | policy | DEC-2026-11-09-09 (award schedule); 6-cost.md 1.2 (spend-out 15%, 35%, 30%, 20%: judgment) |  |
| `capital_spend_y2` HOU-3C.01 and HOU-5.01: share spent in year 2 after award | 0.3 | share | none | policy | DEC-2026-11-09-09 (award schedule); 6-cost.md 1.2 (spend-out 15%, 35%, 30%, 20%: judgment) |  |
| `capital_spend_y3` HOU-3C.01 and HOU-5.01: share spent in year 3 after award | 0.2 | share | none | policy | DEC-2026-11-09-09 (award schedule); 6-cost.md 1.2 (spend-out 15%, 35%, 30%, 20%: judgment) |  |
| `loan_commitments` HOU-3C.02: construction loan commitments, evenly | 300 | $ billion | FY2030-FY2038 | policy | DEC-2026-11-09-09 (commitments end FY2038) |  |
| `loan_disburse_y0` HOU-3C.02: share disbursed in year 0 | 0.4 | share | none | policy | DEC-2026-11-09-09; 6-cost.md 1.2 (disbursed 40%, 40%, 20%: judgment) |  |
| `loan_disburse_y1` HOU-3C.02: share disbursed in year 1 | 0.4 | share | none | policy | DEC-2026-11-09-09; 6-cost.md 1.2 (disbursed 40%, 40%, 20%: judgment) |  |
| `loan_disburse_y2` HOU-3C.02: share disbursed in year 2 | 0.2 | share | none | policy | DEC-2026-11-09-09; 6-cost.md 1.2 (disbursed 40%, 40%, 20%: judgment) |  |
| `recovery_housing` HOU-4.10: recovery housing | 0.3 | $ billion a year | FY2030-FY2034 | policy | DEC-2026-11-09-05 (memo 5 B); 6-cost.md 1.2 ($1.5 billion over 2030-34, placeholder) |  |
| `services_backstop` HOU-4.12: HUD services backstop, first year | 0.5 | $ billion | FY2030 | policy | DEC-2026-11-09-10; 6-cost.md 2.3 (placeholder: $0.5 billion in FY2030, growing 3%) |  |
| `wider_backstop` HOU-4.12: wider backstop through 2035 | 1.0 | $ billion a year | FY2030-FY2035 | policy | DEC-2026-11-09-10; 6-cost.md 2.3 (placeholder, range $0.5-2 billion) |  |
| `testing_grants` HOU-4.06: fair housing testing grants | 0.1 | $ billion a year | FY2030-FY2034 | policy | DEC-2026-11-09-17 ($100 million a year) |  |
| `ig_set_aside` Inspector general set-aside, first year | 0.05 | $ billion a year | FY2030 | policy | DEC-2026-11-09-10; 6-cost.md 1.2 ($50 million a year, indexed: judgment) |  |
| `down_payment_ba` HOU-10.01: down payment help, FY2030 | 1.5 | $ billion | FY2030 | policy | DEC-2026-11-09-19; DEC-2026-11-10-03 |  |
| `down_payment_ba` HOU-10.01: down payment help, FY2031-39 | 3.0 | $ billion a year | FY2031-FY2039 | policy | DEC-2026-11-09-19; DEC-2026-11-10-03 |  |
| `down_payment_spill` HOU-10.01: share spent the next year | 0.05 | share | none | policy | DEC-2026-11-09-19; 6-cost.md 2.8 (paid at closing, about 5% spills into the next year: judgment) |  |
| `repair_fund_ba` HOU-12.01: home repair fund | 2.0 | $ billion | FY2030 | policy | DEC-2026-11-09-25; DEC-2026-11-10-01 (FY2039 cut to $3.7 billion by the FY2029 bridge) |  |
| `repair_fund_ba` HOU-12.01: home repair fund | 4.0 | $ billion | FY2031 | policy | DEC-2026-11-09-25; DEC-2026-11-10-01 (FY2039 cut to $3.7 billion by the FY2029 bridge) |  |
| `repair_fund_ba` HOU-12.01: home repair fund | 4.0 | $ billion | FY2032 | policy | DEC-2026-11-09-25; DEC-2026-11-10-01 (FY2039 cut to $3.7 billion by the FY2029 bridge) |  |
| `repair_fund_ba` HOU-12.01: home repair fund | 4.0 | $ billion | FY2033 | policy | DEC-2026-11-09-25; DEC-2026-11-10-01 (FY2039 cut to $3.7 billion by the FY2029 bridge) |  |
| `repair_fund_ba` HOU-12.01: home repair fund | 4.0 | $ billion | FY2034 | policy | DEC-2026-11-09-25; DEC-2026-11-10-01 (FY2039 cut to $3.7 billion by the FY2029 bridge) |  |
| `repair_fund_ba` HOU-12.01: home repair fund | 4.0 | $ billion | FY2035 | policy | DEC-2026-11-09-25; DEC-2026-11-10-01 (FY2039 cut to $3.7 billion by the FY2029 bridge) |  |
| `repair_fund_ba` HOU-12.01: home repair fund | 4.0 | $ billion | FY2036 | policy | DEC-2026-11-09-25; DEC-2026-11-10-01 (FY2039 cut to $3.7 billion by the FY2029 bridge) |  |
| `repair_fund_ba` HOU-12.01: home repair fund | 4.0 | $ billion | FY2037 | policy | DEC-2026-11-09-25; DEC-2026-11-10-01 (FY2039 cut to $3.7 billion by the FY2029 bridge) |  |
| `repair_fund_ba` HOU-12.01: home repair fund | 4.0 | $ billion | FY2038 | policy | DEC-2026-11-09-25; DEC-2026-11-10-01 (FY2039 cut to $3.7 billion by the FY2029 bridge) |  |
| `repair_fund_ba` HOU-12.01: home repair fund | 3.7 | $ billion | FY2039 | policy | DEC-2026-11-09-25; DEC-2026-11-10-01 (FY2039 cut to $3.7 billion by the FY2029 bridge) |  |
| `repair_fund_spill` HOU-12.01: share spent the next year | 0.3 | share | none | policy | DEC-2026-11-09-25; 6-cost.md 2.9 (about 70% spent in the year awarded, 30% the next: judgment) |  |
| `property_tax_match` HOU-13.01: property-tax match as states join; grows with property taxes after FY2034 | 0.5 | $ billion | FY2031 | policy | DEC-2026-11-09-22; 6-cost.md 2.9 (states join as they change their laws: judgment) |  |
| `property_tax_match` HOU-13.01: property-tax match as states join; grows with property taxes after FY2034 | 1.5 | $ billion | FY2032 | policy | DEC-2026-11-09-22; 6-cost.md 2.9 (states join as they change their laws: judgment) |  |
| `property_tax_match` HOU-13.01: property-tax match as states join; grows with property taxes after FY2034 | 2.0 | $ billion | FY2033 | policy | DEC-2026-11-09-22; 6-cost.md 2.9 (states join as they change their laws: judgment) |  |
| `property_tax_match` HOU-13.01: property-tax match as states join; grows with property taxes after FY2034 | 2.5 | $ billion | FY2034 | policy | DEC-2026-11-09-22; 6-cost.md 2.9 (states join as they change their laws: judgment) |  |
| `legal_help` HOU-13.02: equity protection | 0.2 | $ billion a year | FY2030-FY2045 | policy | DEC-2026-11-09-25 ($200 million a year from FY2030) |  |
| `service_coordinators` HOU-13.03: service coordinators | 0.15 | $ billion a year | FY2031-FY2045 | policy | DEC-2026-11-09-25 ($150 million a year from FY2031) |  |
| `home_sharing` HOU-13.04: home-sharing grants | 0.03 | $ billion a year | FY2031-FY2039 | policy | DEC-2026-11-09-25 ($30 million a year, FY2031-39) |  |
| `rural_staff` HOU-14.01: field staff | 0.1 | $ billion | FY2030 | policy | DEC-2026-11-10-02; 6-cost.md 2.11 (about 2,000 more staff at about $150,000 each) |  |
| `rural_staff` HOU-14.01: field staff | 0.2 | $ billion | FY2031 | policy | DEC-2026-11-10-02; 6-cost.md 2.11 (about 2,000 more staff at about $150,000 each) |  |
| `rural_staff` HOU-14.01: field staff | 0.3 | $ billion | FY2032 | policy | DEC-2026-11-10-02; 6-cost.md 2.11 (about 2,000 more staff at about $150,000 each) |  |
| `rural_staff` HOU-14.01: field staff | 0.3 | $ billion | FY2033 | policy | DEC-2026-11-10-02; 6-cost.md 2.11 (about 2,000 more staff at about $150,000 each) |  |
| `rural_staff` HOU-14.01: field staff | 0.3 | $ billion | FY2034 | policy | DEC-2026-11-10-02; 6-cost.md 2.11 (about 2,000 more staff at about $150,000 each) |  |
| `rural_staff` HOU-14.01: field staff | 0.3 | $ billion | FY2035 | policy | DEC-2026-11-10-02; 6-cost.md 2.11 (about 2,000 more staff at about $150,000 each) |  |
| `rural_staff` HOU-14.01: field staff | 0.3 | $ billion | FY2036 | policy | DEC-2026-11-10-02; 6-cost.md 2.11 (about 2,000 more staff at about $150,000 each) |  |
| `rural_staff` HOU-14.01: field staff | 0.3 | $ billion | FY2037 | policy | DEC-2026-11-10-02; 6-cost.md 2.11 (about 2,000 more staff at about $150,000 each) |  |
| `rural_staff` HOU-14.01: field staff | 0.3 | $ billion | FY2038 | policy | DEC-2026-11-10-02; 6-cost.md 2.11 (about 2,000 more staff at about $150,000 each) |  |
| `rural_staff` HOU-14.01: field staff | 0.3 | $ billion | FY2039 | policy | DEC-2026-11-10-02; 6-cost.md 2.11 (about 2,000 more staff at about $150,000 each) |  |
| `rural_system` HOU-14.01: one loan system | 0.15 | $ billion a year | FY2030-FY2034 | policy | DEC-2026-11-10-02; 6-cost.md 2.11 |  |
| `section502_added_lending` HOU-14.02: added direct loan level | 0.5 | $ billion | FY2030 | policy | DEC-2026-11-10-02; EV-HOU-781 (above FY2026's $1 billion) |  |
| `section502_added_lending` HOU-14.02: added direct loan level | 1.5 | $ billion | FY2031 | policy | DEC-2026-11-10-02; EV-HOU-781 (above FY2026's $1 billion) |  |
| `section502_added_lending` HOU-14.02: added direct loan level | 2.5 | $ billion | FY2032 | policy | DEC-2026-11-10-02; EV-HOU-781 (above FY2026's $1 billion) |  |
| `section502_added_lending` HOU-14.02: added direct loan level | 3.0 | $ billion | FY2033 | policy | DEC-2026-11-10-02; EV-HOU-781 (above FY2026's $1 billion) |  |
| `section502_added_lending` HOU-14.02: added direct loan level | 3.0 | $ billion | FY2034 | policy | DEC-2026-11-10-02; EV-HOU-781 (above FY2026's $1 billion) |  |
| `section502_added_lending` HOU-14.02: added direct loan level | 3.0 | $ billion | FY2035 | policy | DEC-2026-11-10-02; EV-HOU-781 (above FY2026's $1 billion) |  |
| `section502_added_lending` HOU-14.02: added direct loan level | 3.0 | $ billion | FY2036 | policy | DEC-2026-11-10-02; EV-HOU-781 (above FY2026's $1 billion) |  |
| `section502_added_lending` HOU-14.02: added direct loan level | 3.0 | $ billion | FY2037 | policy | DEC-2026-11-10-02; EV-HOU-781 (above FY2026's $1 billion) |  |
| `section502_added_lending` HOU-14.02: added direct loan level | 3.0 | $ billion | FY2038 | policy | DEC-2026-11-10-02; EV-HOU-781 (above FY2026's $1 billion) |  |
| `section502_added_lending` HOU-14.02: added direct loan level | 3.0 | $ billion | FY2039 | policy | DEC-2026-11-10-02; EV-HOU-781 (above FY2026's $1 billion) |  |
| `section502_subsidy_rate` HOU-14.02: subsidy rate | 0.13 | share | FY2026 | policy | DEC-2026-11-10-02; 6-cost.md 2.11 (OMB's FY2026 rate, rural delivery note 1.2) |  |
| `section502_to_100_ami` HOU-14.02: the wider limit | 0.2 | $ billion | FY2030-FY2039 | policy | DEC-2026-11-10-02; 6-cost.md 2.11 (direct loans to 100% of area median income add about $0.2 billion) |  |
| `rural_preservation_ba` HOU-14.03: preservation fund | 0.5 | $ billion a year | FY2030-FY2039 | policy | DEC-2026-11-10-02; 6-cost.md 2.11 |  |
| `rural_preservation_spend_y0` HOU-14.03: share spent in year 0 | 0.4 | share | none | policy | DEC-2026-11-10-02; 6-cost.md 2.11 (spent over about three years: this model reads it as 40%, 40%, 20%, which gives the section's $4.6 billion in the window) |  |
| `rural_preservation_spend_y1` HOU-14.03: share spent in year 1 | 0.4 | share | none | policy | DEC-2026-11-10-02; 6-cost.md 2.11 (spent over about three years: this model reads it as 40%, 40%, 20%, which gives the section's $4.6 billion in the window) |  |
| `rural_preservation_spend_y2` HOU-14.03: share spent in year 2 | 0.2 | share | none | policy | DEC-2026-11-10-02; 6-cost.md 2.11 (spent over about three years: this model reads it as 40%, 40%, 20%, which gives the section's $4.6 billion in the window) |  |
| `rural_vouchers` HOU-14.03: rural vouchers | 0.06 | $ billion a year | FY2030-FY2045 | policy | DEC-2026-11-10-02; 6-cost.md 2.11 (road-funding.md's placeholder) |  |

**`published.csv`** (lines taken as 6-cost.md publishes them, because it states no build this model can rerun). 21 inputs: 0 traced to evidence, 0 policy parameters, 0 calibrated to a benchmark, 21 labeled assumptions with a tested range.

| ID | Value | Unit | Year | Kind | Source or basis | Range |
| --- | --- | --- | --- | --- | --- | --- |
| `zoning_reward` HOU-6.01 zoning reward (Innovation Fund) | 25 | $ billion | FY2030-FY2039 | assumption | 6-cost.md 1.2: legacy amount ($30 billion of budget authority); awards follow finished homes, so spending lags (judgment); DEC-2026-11-09-04 |  |
| `zoning_reward` HOU-6.01 zoning reward, FY2040 tail | 3 | $ billion | FY2040 | assumption | 6-cost.md 1.2 and 3.3: about $3 billion in FY2040 |  |
| `zoning_reward` HOU-6.01 zoning reward, FY2041 tail | 2 | $ billion | FY2041 | assumption | 6-cost.md 1.2: about $2 billion more in FY2041 |  |
| `social_housing_pilot` HOU-8.01 social housing pilot, equity | 9 | $ billion | FY2030-FY2039 | assumption | 6-cost.md 1.2: legacy ($10 billion of equity); DEC-2026-11-10-04 |  |
| `social_housing_pilot` HOU-8.01, FY2040 tail | 1 | $ billion | FY2040 | assumption | 6-cost.md 1.2 |  |
| `federal_builder` HOU-9A.01 small federal builder, capital | 5 | $ billion | FY2030-FY2039 | assumption | 6-cost.md 1.2: placeholder, judgment (the legacy file leaves it unscored); DEC-2026-11-09-03 | 2 to 20 |
| `federal_builder` HOU-9A.01, FY2040 | 0 | $ billion | FY2040 | assumption | 6-cost.md 1.2 |  |
| `federal_admin` Federal administration, systems and evaluation set-aside | 2 | $ billion | FY2030-FY2039 | assumption | 6-cost.md 1.2: 0.5% of housing's program outlays (range 0.25-1%), judgment; section 2.4 says about $2.4 billion, the table and the booking $2 billion (fiscal-components.csv 0.002) | 1 to 7 |
| `federal_admin` Federal administration set-aside, FY2040 | 0.4 | $ billion | FY2040 | assumption | 6-cost.md 1.2 | 0.2 to 0.8 |
| `fha_premium_cut` HOU-10.02 FHA premium cut, loans endorsed through FY2039 | 25 | $ billion | FY2030-FY2039 | assumption | 6-cost.md 2.8: 0.25 points on about $200 billion of purchase loans a year (EV-HOU-552), each cohort's lost premiums at $2.5-3 billion under credit reform (judgment); needs CBO's score; DEC-2026-11-10-03 | 15 to 35 |
| `fha_premium_cut` HOU-10.02, FY2040 | 0 | $ billion | FY2040 | assumption | 6-cost.md 2.12: ends with FY2039's loans |  |
| `manufactured_home_grants` HOU-11.01 manufactured-home community grants | 3.5 | $ billion | FY2030-FY2039 | assumption | 6-cost.md 1.2 and 2.8: $350 million a year (DEC-2026-11-09-24), $3.5 billion in all with the FY2029 bridge (DEC-2026-11-10-01); the section's own spend-out would give about $3.2-3.4 billion in the window | 2 to 5 |
| `manufactured_home_grants` HOU-11.01, FY2040 tail | 0.3 | $ billion | FY2040 | assumption | 6-cost.md 1.2 | 0.2 to 0.4 |
| `self_help_farmworker` HOU-14.04 self-help and farmworker housing | 2.3 | $ billion | FY2030-FY2039 | assumption | 6-cost.md 2.11: about $0.25 billion a year more than FY2026 (EV-HOU-756), $2.5 billion of budget authority, about 90% spent in the window; DEC-2026-11-10-02 | 1.5 to 3.5 |
| `self_help_farmworker` HOU-14.04, FY2040 tail | 0.2 | $ billion | FY2040 | assumption | 6-cost.md 2.11 | 0.1 to 0.3 |
| `section502_fy2040_tail` HOU-14.02 Section 502, FY2040 tail | 0.1 | $ billion | FY2040 | assumption | 6-cost.md 2.11 |  |
| `rural_staff_fy2040` HOU-14.01 staff, FY2040 | 0.35 | $ billion | FY2040 | assumption | 6-cost.md 2.11: the staff as a regular appropriation from FY2040, growing with pay | 0.3 to 0.4 |
| `low_income_credit` HOU-2D.01 low-income credit increase (revenue loss) | 101.3 | $ billion | FY2030-FY2039 | assumption | 6-cost.md 4: about $0.10 trillion ($0.08-0.12; legacy HOU-2B) plus about $1 billion for the bond-deal boost (DEC-2026-11-09-18); fiscal-components.csv books 0.1013; not a JCT score; DEC-2026-11-09-08 | 82 to 121 |
| `low_income_credit` HOU-2D.01, FY2040 | 15.2 | $ billion | FY2040 | assumption | 6-cost.md 4: about $15 billion (12-22) plus about $0.2 billion for the boost | 12.2 to 22.2 |
| `trial_credits` HOU-2D.02-.03 trial credits (revenue loss) | 22 | $ billion | FY2030-FY2039 | assumption | 6-cost.md 4: the middle-income credit about $7 billion and the neighborhood homes credit about $15 billion (EV-HOU-269, EV-HOU-270); not a JCT score | 20 to 23 |
| `trial_credits` HOU-2D.02-.03, FY2040 | 1 | $ billion | FY2040 | assumption | 6-cost.md 4: about $1 billion, and small | 0.8 to 1.8 |

**`market.csv`** (the reach, rent and supply evidence). 25 inputs: 17 traced to evidence, 2 policy parameters, 0 calibrated to a benchmark, 6 labeled assumptions with a tested range.

| ID | Value | Unit | Year | Kind | Source or basis | Range |
| --- | --- | --- | --- | --- | --- | --- |
| `tight_share` Share of the plan's added rent subsidy spent in tight (inelastic) markets | 0.4 | share of added rent subsidy | none | assumption | judgment: the register has no share of voucher spending in supply-constrained markets. Lease-up is lower where vacancies are few (EV-HOU-092); the first awards land in tight markets (6-cost.md 1.4); extremely low-income need is concentrated where rents are high (EV-HOU-018). Range swept | 0.25 to 0.6 |
| `pass_through_tight` Landlord capture: share of each added subsidy dollar that becomes higher rent for the households helped (tight markets) | 0.39 | share of subsidy | none | assumption | the register's range for markets where supply cannot respond: 0 (no overall rent rise from more vouchers, EV-HOU-096; Finland's upper bound 0.2, EV-HOU-158) to 0.78 (France, EV-HOU-156); the UK's 0.6-0.67 (EV-HOU-155) inside it. Central is the midpoint, the project's convention (ASM-CALIB-MID), not a finding: 7-validation.md 5.1 says both views stand | 0 to 0.78 |
| `pass_through_elastic` Landlord capture in other markets | 0.1 | share of subsidy | none | assumption | 0 where supply responds (EV-HOU-096) to Finland's upper bound of 0.2 where allowances follow set limits (EV-HOU-158); midpoint by convention (ASM-CALIB-MID) | 0 to 0.2 |
| `spillover_ratio_tight_high` High end of the rent paid by unassisted low-income renters per added subsidy dollar (tight markets) | 1.41 | $ of rent per $ of subsidy | none | evidence | EV-HOU-397 (Susin 2002: $8.2 billion more rent paid by unsubsidized poor households against $5.8 billion of subsidy, 90 largest metros, 1974-93 data, contested); 8.2 / 5.8 |  |
| `spillover_pct_tight_high` The high end of the rent rise for unassisted poor renters | 0.16 | share of rent | none | evidence | EV-HOU-397 (Susin 2002: vouchers raised rents for unsubsidized poor households 16% on average in the 90 largest metros) |  |
| `stock_rent_elasticity` Local rent effect of added housing stock | -0.1 | % rent per % stock | none | evidence | EV-HOU-133 (Li 2022: within 500 feet of new high-rises in New York City, each 10% more housing lowers rents 1%) |  |
| `net_add_per_subsidized_low` Net homes added per subsidized home: low | 0.33 | homes per subsidized home | none | evidence | EV-HOU-114 (one subsidized unit adds a third to a half of a unit to the stock) |  |
| `net_add_per_subsidized_high` Net homes added per subsidized home: high | 0.5 | homes per subsidized home | none | evidence | EV-HOU-114 |  |
| `direct_homes_m` Homes the plan pays for directly (target) | 1.3 | million homes | FY2030-FY2039 | policy | DEC-2026-11-09-17 (the published target: about 1.3 million homes the plan pays for directly, credits included; 4-specification.md HOU-3C.04) | 0.8 to 1.9 |
| `construction_homes_m` Of which the construction money's homes | 0.9 | million homes | FY2030-FY2039 | policy | DEC-2026-11-09-17; 7-validation.md 1.4: the construction money's share of the target | 0.6 to 1.3 |
| `shortage_eli_m` Shortage for the poorest renters | 7.1 | million homes | 2025 | evidence | EV-HOU-018 (NLIHC: shortage of rental homes affordable and available to extremely low-income renters) |  |
| `shortage_national_low_m` National shortage: low | 4 | million homes | 2024 | evidence | EV-HOU-017 (commonly cited national shortage: 4-5 million; methods differ) |  |
| `shortage_national_high_m` National shortage: high | 5 | million homes | 2024 | evidence | EV-HOU-017 |  |
| `eli_renters_m` Extremely low-income renter households | 12.018 | million households | 2023 | evidence | EV-HOU-186 (HUD Worst Case Housing Needs 2025) |  |
| `eli_worst_case_m` ELI renter households with worst case needs (unassisted with severe problems) | 5.809 | million households | 2023 | evidence | EV-HOU-186 |  |
| `eli_families_worst_case_m` ELI families with children with worst case needs | 1.717 | million households | 2023 | evidence | EV-HOU-186 |  |
| `eli_older_worst_case_m` ELI older-adult households with worst case needs | 1.749 | million households | 2023 | evidence | EV-HOU-186 |  |
| `vli_disabled_worst_case_m` Very low-income renter households with a disabled member under 62 and worst case needs | 1.162 | million households | 2023 | evidence | EV-HOU-371 |  |
| `eli_share_of_worst_case` ELI share of all worst case needs | 0.686 | share | 2023 | evidence | EV-HOU-185 (ELI households are 68.6% of all worst case needs) |  |
| `voucher_households_m` Existing voucher households | 2.404 | million households | 2023 | evidence | EV-HOU-370 (Housing Choice Voucher households at the end of 2023) |  |
| `homeless_night_2025` People homeless on a night in 2025 | 745652 | people | 2025 | evidence | EV-HOU-014 (HUD point-in-time count) |  |
| `shelter_users_fy2022` People who used shelter over a year | 1388000 | people | FY2022 | evidence | EV-HOU-427 (people who used shelter over FY2022) |  |
| `emergency_cost_per_household` Emergency fund: cost per household helped | 3500 | $ per household | none | assumption | 6-cost.md 2.2: judgment, between the Santa Clara trial's about $2,000 (EV-HOU-109) and four months' Fair Market Rent | 2000 to 5000 |
| `repair_cost_per_home` Repair fund: cost per home | 15000 | $ per home | none | assumption | 6-cost.md 2.9: $12,000-18,000 each with administration, from Philadelphia's and Detroit's costs (EV-HOU-647, EV-HOU-660) | 12000 to 18000 |
| `buyer_help_average` Down payment help: average per buyer | 25000 | $ per buyer | none | assumption | 6-cost.md 2.12: an average of about $24,000-26,000 under the cap (DEC-2026-11-10-03) | 24000 to 26000 |
<!-- generated:parameters:end -->

Evidence still needed (each now an assumption with a range): take-up of a housing right (no U.S. precedent in the register; France's allowance, EV-HOU-156, is not a take-up estimate); CBO's credit subsidy rate for HOU-3C.02's loans and a CBO score of FHA's premium cut; a JCT score of option D's credits; CBO's spend-out rates for HUD capital grants; HUD's fee rates in dollars; the share of voucher spending in supply-constrained markets (`tight_share`); rent pass-through from a recent large voucher expansion, such as Emergency Housing Vouchers by market (7-validation.md, "Evidence still needed").

## Mechanisms and their research basis

- **Rental help, month by month** (HOU-4A, HOU-4D, HOU-4.08). Awards are issued evenly over each year's months on the decided schedule: 250,000 a year from April 2030 through FY2033 (`DEC-2026-11-09-01`); stage 2 at up to 300,000 a year from FY2034, every remaining applicant in FY2037 when it becomes a right; stage 3 a third a year over FY2038-40 (`DEC-2026-11-10-03`). Each award leases after the lag (6 months; EHV took 77 days, EV-HOU-344) at the steady-state share (90%; national occupancy 84%, EV-HOU-370; EHV 67% after two years, EV-HOU-345) and costs the subsidy ($17,000 in FY2030 from HUD's 2023 $1,068 a month, EV-HOU-370, growing 3%) plus fees (8.1% and $750 an award, the legacy allowance; EV-HOU-343). Search help is $2,000 an award and a reissue for 10% of leased households a year, growing with the subsidy. Stage 2's pools come from HUD's 1.717 million ELI families with worst case needs (EV-HOU-186) at 85% applying (`DEC-2026-11-10-03`); stage 3's from HUD's disability counts (EV-HOU-371, EV-HOU-786). The duty to house lifts stage 2's leasing by 5.6% from FY2037 (95% against 90%; judgment), capped so no line leases more than its awards (which, in the high case, leaves the duty only 2 points: see Limits). The higher payment standards add 3% to the rent subsidy (judgment).
- **Budget authority times spend-out** for the capital, emergency, owner and rural lines, on the decided amounts and award schedules (`DEC-2026-11-09-09`, `-25`, `DEC-2026-11-10-01`, `-02`); every spend-out rate is 6-cost.md's judgment, not CBO's.
- **Low and high** move every judgment input in the same direction (6-cost.md, "Low, central and high"); a longer lag lowers cost, so the low case takes 9 months. Lines built from decided amounts held fixed take 6-cost.md's own ranges, as ratios to its central applied to the model's central.
- **Reach** is the leased households at the end of each fiscal year, and the other programs' money divided by their cost per household (6-cost.md 2.2, 2.9, 2.12).
- **Rents: a pass-through reading, not an elasticity model** (the register has no supply or demand elasticities by market). Landlord capture = added rent subsidy in tight markets × a pass-through share from 0 (no overall rent rise from more vouchers, Eriksen and Ross, EV-HOU-096; Finland's upper bound of 0.2, EV-HOU-158) to 0.78 (France, EV-HOU-156), with the UK's 0.6-0.67 inside it (EV-HOU-155); 0 to 0.2 elsewhere. The central is the range's midpoint by the project's convention (`ASM-CALIB-MID`), not a finding. Spillover to unassisted renters in tight markets runs from 0 (EV-HOU-096) to Susin's ratio of $8.2 billion of their rent to $5.8 billion of subsidy, 1.41 (EV-HOU-397, 1974-93 data, contested), with no central: the evidence is split (7-validation.md 5.1). The share of the added subsidy in tight markets is a labeled judgment, 40% (25-60%), swept. The design's features enter as directions only: neighborhood payment limits lower capture (EV-HOU-095), the 120% payment standards raise it in the same markets, attached homes lower it by the net homes they add (EV-HOU-114, EV-HOU-115, EV-HOU-133). Method checked with a fable subagent; its citations were verified against the register.
- **Supply as a range**: the decided target of homes the plan pays for (`DEC-2026-11-09-17`) times the net homes a subsidized home adds, 0 (EV-HOU-115) to a half (EV-HOU-114).

## Limits

- **The rental lines rest on two soft inputs:** the 90% leased share (EHV reached 67%; BM-HUD-3 misses) and the subsidy's growth, whose risk is upward (BM-CBO-2 and BM-CBO-3 miss low). Section 1.4's sweep is the honest reading of the first: lower lease-up is help not delivered, not a saving.
- **Nine lines are taken as published**, about $195 billion of the window, including the tax credits ($123 billion) and FHA's premium cut ($25 billion). The model checks nothing about them beyond their sum.
- **Even issuance within a year** and a fixed lag are simplifications; they reproduce the dossier, whose own convention they are.
- **The rent readings apply average, historical ratios to a program about two and a half times today's** (3.6 million added on 2.4 million, EV-HOU-370), far outside the studies' samples; the tight-market share is invented and labeled so. Readings in dollars cannot be turned into rents per household without counts the register lacks.
- **The pools are 2023 counts** (HUD, Worst Case Housing Needs 2025) held flat after 2037, as the dossier assumes; stage 2's exit rule is unpriced.
- **Two lines differ from 6-cost.md's table by its own rounding** (HOU-3C.02 and HOU-13.01, below), so the model's total is $807.2 billion against the table's $806 billion; the booked figures stay as booked.
- **The high case's published total ($1,139 billion) is below the sum of its own line highs ($1,157 billion).** The model's total ($1,157 billion) is close to the lines' sum, but line by line it differs from the published highs by up to $2.7 billion in both directions (REP-HIGH lists them), so the agreement partly rests on offsets.
- **The duty to house's own range is not in order** (low $1.2 billion, central $3.4 billion, high $2.3 billion; 6-cost.md: 1-5). In the high case awards already lease at 98%, so the duty can add only the last 2 points; 6-cost.md's $5 billion would need stage 2 to lease more than 100% of its awards. Stage 2 with its duty runs in order ($48.5, 84.2 and 144.3 billion), and the tests check that and every other line.
- **FY2040 is checked as a total, not line by line.** The small lines' FY2040 tails differ from 6-cost.md's by up to about $0.1 billion each (HOU-14.03: $0.36 billion against $0.46 billion, since the section's "about three years" spend-out is read as 40%, 40%, 20% to match its window figure).
- Baseline vintage: CBO, February 2026 (`ASM-INCREMENT`); subsidy base HUD 2023; pools HUD 2023.

## Validation

Generated by the model's test code (`test_housing.py`, on `models/schema/validation.py`). Tolerances were set in this version's test code when the benchmarks were written; the model's figures were roughly known then, so they are not blind.

<!-- generated:validation:start -->
**Reproduction of `dossiers/home/6-cost.md` and the booking** (in-sample by construction: they check the rebuild, not accuracy). 42 benchmarks. 0 independent: 0 pass, 0 miss. 42 in-sample by construction (they check arithmetic, not accuracy): 40 pass.

| ID | Quantity | Target | Source and vintage | Model | Difference | Tolerance (set in advance) | Result | Explanation |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| REP-HOU-4A | HOU-4A.01-.02 One million awards, with full fees, FY2030-39 | 147 $ billion | 6-cost.md 1.2; the dossier, central | 147 | 0.37 (+0.2%) | 0.50 $ billion; the table's own rounding (half its last digit) | pass (in-sample) | the dossier's arithmetic, rebuilt from its inputs |
| REP-HOU-4.07 | HOU-4.07 Search help, FY2030-39 | 8.00 $ billion | 6-cost.md 1.2; the dossier, central | 8.03 | 0.025 (+0.3%) | 0.50 $ billion; the table's own rounding (half its last digit) | pass (in-sample) | the dossier's arithmetic, rebuilt from its inputs |
| REP-HOU-4D | HOU-4D.01 Stage 2 guarantee, 2034 on, FY2030-39 | 81.0 $ billion | 6-cost.md 1.2; the dossier, central | 80.8 | -0.19 (-0.2%) | 0.50 $ billion; the table's own rounding (half its last digit) | pass (in-sample) | the dossier's arithmetic, rebuilt from its inputs |
| REP-HOU-4D-DUTY | HOU-4D.01 Duty to house, 2037 on, FY2030-39 | 3.00 $ billion | 6-cost.md 1.2; the dossier, central | 3.40 | 0.40 (+13.4%) | 0.50 $ billion; the table's own rounding (half its last digit) | pass (in-sample) | the duty to house's high falls below its central: in the high case awards already lease at 98%, so the duty can add only the last 2 points; 6-cost.md's high of $5 billion would need stage 2 to lease more than 100% of its awards. Stage 2 with the duty runs $48.5, 84.2 and 144.3 billion |
| REP-HOU-4D-WIDER | HOU-4D.01 Stage 2's wider entry, FY2030-39 | 17.0 $ billion | 6-cost.md 1.2; the dossier, central | 16.9 | -0.097 (-0.6%) | 0.50 $ billion; the table's own rounding (half its last digit) | pass (in-sample) | the dossier's arithmetic, rebuilt from its inputs |
| REP-HOU-4D-RESTATED | HOU-4D.01 Stage 2 restated (stage 1 uncapped), FY2030-39 | 17.0 $ billion | 6-cost.md 1.2; the dossier, central | 16.9 | -0.097 (-0.6%) | 0.50 $ billion; the table's own rounding (half its last digit) | pass (in-sample) | the dossier's arithmetic, rebuilt from its inputs |
| REP-HOU-4.08-U62 | HOU-4.08 Stage 3, disabled renters under 62, FY2030-39 | 5.00 $ billion | 6-cost.md 1.2; the dossier, central | 5.41 | 0.41 (+8.1%) | 0.50 $ billion; the table's own rounding (half its last digit) | pass (in-sample) | the dossier's arithmetic, rebuilt from its inputs |
| REP-HOU-4.08-62UP | HOU-4.08 Stage 3's disabled renters 62 and over, FY2030-39 | 5.00 $ billion | 6-cost.md 1.2; the dossier, central | 5.31 | 0.31 (+6.2%) | 0.50 $ billion; the table's own rounding (half its last digit) | pass (in-sample) | the dossier's arithmetic, rebuilt from its inputs |
| REP-HOU-1D.04 | HOU-1D.04 One-time start, FY2030-39 | 15.0 $ billion | 6-cost.md 1.2; the dossier, central | 15.0 | 0.000 (+0.0%) | 0.50 $ billion; the table's own rounding (half its last digit) | pass (in-sample) | the dossier's arithmetic, rebuilt from its inputs |
| REP-HOU-1D.01 | HOU-1D.01-.03 Standing emergency fund, FY2030-39 | 49.0 $ billion | 6-cost.md 1.2; the dossier, central | 49.4 | 0.37 (+0.8%) | 0.50 $ billion; the table's own rounding (half its last digit) | pass (in-sample) | the dossier's arithmetic, rebuilt from its inputs |
| REP-HOU-3C.01 | HOU-3C.01 State revolving fund grants, FY2030-39 | 70.0 $ billion | 6-cost.md 1.2; the dossier, central | 70.2 | 0.20 (+0.3%) | 0.50 $ billion; the table's own rounding (half its last digit) | pass (in-sample) | the dossier's arithmetic, rebuilt from its inputs |
| REP-HOU-3C.02 | HOU-3C.02 Construction loans (subsidy), FY2030-39 | 14.0 $ billion | 6-cost.md 1.2; the dossier, central | 14.7 | 0.67 (+4.8%) | 0.50 $ billion; the table's own rounding (half its last digit) | **miss** (in-sample) | 6-cost.md's own inputs give $14.7 billion: $15 billion of subsidy at 5% on $300 billion committed evenly FY2030-38, less the 20% of FY2038's disbursed in FY2040 ($0.3 billion, the table's 0.4). Section 3.5 prints 14.6; the table rounds it to 14. The booking carries 14 (fiscal-components.csv 0.014). |
| REP-HOU-5.01 | HOU-5.01 Public housing repair, FY2030-39 | 57.0 $ billion | 6-cost.md 1.2; the dossier, central | 56.5 | -0.45 (-0.8%) | 0.50 $ billion; the table's own rounding (half its last digit) | pass (in-sample) | the dossier's arithmetic, rebuilt from its inputs |
| REP-HOU-4.10 | HOU-4.10 Recovery housing, FY2030-39 | 1.50 $ billion | 6-cost.md 1.2; the dossier, central | 1.50 | 0.000 (+0.0%) | 0.050 $ billion; the table's own rounding (half its last digit) | pass (in-sample) | the dossier's arithmetic, rebuilt from its inputs |
| REP-HOU-4.12 | HOU-4.12 HUD services backstop, FY2030-39 | 6.00 $ billion | 6-cost.md 1.2; the dossier, central | 5.73 | -0.27 (-4.5%) | 0.50 $ billion; the table's own rounding (half its last digit) | pass (in-sample) | the dossier's arithmetic, rebuilt from its inputs |
| REP-HOU-4.12-WIDER | HOU-4.12 Wider backstop through 2035, FY2030-39 | 6.00 $ billion | 6-cost.md 1.2; the dossier, central | 6.00 | 0.000 (+0.0%) | 0.50 $ billion; the table's own rounding (half its last digit) | pass (in-sample) | the dossier's arithmetic, rebuilt from its inputs |
| REP-HOU-4.06 | HOU-4.06 Fair housing testing grants, FY2030-39 | 0.50 $ billion | 6-cost.md 1.2; the dossier, central | 0.50 | 0.000 (+0.0%) | 0.050 $ billion; the table's own rounding (half its last digit) | pass (in-sample) | the dossier's arithmetic, rebuilt from its inputs |
| REP-PAYSTD | Payment standards up to 120%, FY2030-39 | 7.00 $ billion | 6-cost.md 1.2; the dossier, central | 6.57 | -0.43 (-6.1%) | 0.50 $ billion; the table's own rounding (half its last digit) | pass (in-sample) | the dossier's arithmetic, rebuilt from its inputs |
| REP-IG | Inspector general set-aside, FY2030-39 | 0.60 $ billion | 6-cost.md 1.2; the dossier, central | 0.56 | -0.045 (-7.5%) | 0.050 $ billion; the table's own rounding (half its last digit) | pass (in-sample) | the dossier's arithmetic, rebuilt from its inputs |
| REP-HOU-10.01 | HOU-10.01 Down payment help, FY2030-39 | 28.0 $ billion | 6-cost.md 1.2; the dossier, central | 28.4 | 0.35 (+1.3%) | 0.50 $ billion; the table's own rounding (half its last digit) | pass (in-sample) | the dossier's arithmetic, rebuilt from its inputs |
| REP-HOU-12.01 | HOU-12.01 Home repair fund, FY2030-39 | 37.0 $ billion | 6-cost.md 1.2; the dossier, central | 36.6 | -0.41 (-1.1%) | 0.50 $ billion; the table's own rounding (half its last digit) | pass (in-sample) | the dossier's arithmetic, rebuilt from its inputs |
| REP-HOU-13.01 | HOU-13.01 Property-tax match, FY2030-39 | 20.5 $ billion | 6-cost.md 1.2; the dossier, central | 20.6 | 0.082 (+0.4%) | 0.050 $ billion; the table's own rounding (half its last digit) | **miss** (in-sample) | Section 2.9's own schedule ($0.5, 1.5, 2 and 2.5 billion in FY2031-34, then 4% a year) sums to $20.58 billion; the table prints 20.5 and the booking 0.0205. |
| REP-HOU-13.02 | HOU-13.02-.04 Equity, coordinators, home sharing, FY2030-39 | 3.60 $ billion | 6-cost.md 1.2; the dossier, central | 3.62 | 0.020 (+0.6%) | 0.050 $ billion; the table's own rounding (half its last digit) | pass (in-sample) | the dossier's arithmetic, rebuilt from its inputs |
| REP-HOU-14.01 | HOU-14.01 Rural Development staff and system, FY2030-39 | 3.50 $ billion | 6-cost.md 1.2; the dossier, central | 3.45 | -0.050 (-1.4%) | 0.050 $ billion; the table's own rounding (half its last digit) | pass (in-sample) | the dossier's arithmetic, rebuilt from its inputs |
| REP-HOU-14.02 | HOU-14.02 Section 502 at scale, FY2030-39 | 3.50 $ billion | 6-cost.md 1.2; the dossier, central | 3.52 | 0.015 (+0.4%) | 0.050 $ billion; the table's own rounding (half its last digit) | pass (in-sample) | the dossier's arithmetic, rebuilt from its inputs |
| REP-HOU-14.03 | HOU-14.03 Rural rental fund and vouchers, FY2030-39 | 5.20 $ billion | 6-cost.md 1.2; the dossier, central | 5.20 | 0.000 (+0.0%) | 0.050 $ billion; the table's own rounding (half its last digit) | pass (in-sample) | the dossier's arithmetic, rebuilt from its inputs |
| REP-TOTAL | Housing, total, FY2030-39 (spending and credits) | 806 $ billion | 6-cost.md 1.2 and In brief ($0.81 trillion); the dossier, central | 807 | 1.18 (+0.1%) | 1.50 $ billion; the published total is the sum of 33 lines each rounded to $1 billion or $0.1 billion (0.2%) | pass (in-sample) | the model sums unrounded lines; the table's lines sum to 805.7. The two known differences above add $0.7 billion and $0.1 billion; the rest is the other lines' rounding |
| REP-SPEND | Spending, total, FY2030-39 | 683 $ billion | 6-cost.md 1.2; the dossier, central | 684 | 0.88 (+0.1%) | 1.50 $ billion; as REP-TOTAL | pass (in-sample) | as REP-TOTAL |
| REP-FY2040 | Housing, FY2040 (with the capital tail) | 120 $ billion | 6-cost.md 1.2; 3.2 (the model booked $120.5 billion); the dossier and the budget model | 121 | 0.82 (+0.7%) | 1.50 $ billion; the table's rounding to $1 billion and the booking's fit | pass (in-sample) | the lines taken as published carry their FY2040 figures as printed |
| REP-LOW | Housing, low case, FY2030-39 | 602 $ billion | 6-cost.md 1.2; the dossier, low | 602 | -0.47 (-0.1%) | 2%; the low case moves every judgment input together; 2% allows for the lag and count rounding | pass (in-sample) | rental lines rebuilt at every input's low; lines built from decided amounts take the published ranges as ratios to the central |
| REP-HIGH | Housing, high case, FY2030-39 | 1,139 $ billion | 6-cost.md 1.2; the dossier, high | 1,157 | 17.9 (+1.6%) | 2%; as REP-LOW | pass (in-sample) | 6-cost.md's high total is below the sum of its own line highs (1157). The model's lines differ from the published highs by up to $2.7 billion each, in both directions: search help +1.9, the older stage 3 group +1.3, the wider entry +0.4, HOU-4A -0.5, stage 3 under 62 -0.4 and the duty to house -2.7 (see REP-HOU-4D-DUTY), so the total's pass partly rests on offsets |
| REP-LEASE-0.57-W | Rental help at 57% leased, FY2030-39 | 160 $ billion | 6-cost.md 1.4; the dossier | 160 | -0.22 (-0.1%) | 1.00 $ billion; the table rounds to $1 billion | pass (in-sample) | HOU-4A, HOU-4D's first count and stage 3 under 62, with fees, search help and the higher payment standards |
| REP-LEASE-0.57-40 | Rental help at 57% leased, FY2040 | 36.0 $ billion | 6-cost.md 1.4; the dossier | 36.2 | 0.19 (+0.5%) | 1.00 $ billion; as above | pass (in-sample) | as above |
| REP-LEASE-0.57-HH | Households housed by those three lines at 57% leased, FY2042 | 1.49 million households | 6-cost.md 1.4; the dossier | 1.49 | 0.003 (+0.2%) | 0.010 million households; the table rounds to 10,000 | pass (in-sample) | leased at the end of FY2042 |
| REP-LEASE-0.75-W | Rental help at 75% leased, FY2030-39 | 208 $ billion | 6-cost.md 1.4; the dossier | 208 | -0.075 (-0.0%) | 1.00 $ billion; the table rounds to $1 billion | pass (in-sample) | HOU-4A, HOU-4D's first count and stage 3 under 62, with fees, search help and the higher payment standards |
| REP-LEASE-0.75-40 | Rental help at 75% leased, FY2040 | 47.0 $ billion | 6-cost.md 1.4; the dossier | 47.4 | 0.41 (+0.9%) | 1.00 $ billion; as above | pass (in-sample) | as above |
| REP-LEASE-0.75-HH | Households housed by those three lines at 75% leased, FY2042 | 1.97 million households | 6-cost.md 1.4; the dossier | 1.97 | -0.005 (-0.3%) | 0.010 million households; the table rounds to 10,000 | pass (in-sample) | leased at the end of FY2042 |
| REP-LEASE-0.90-W | Rental help at 90% leased, FY2030-39 | 248 $ billion | 6-cost.md 1.4; the dossier | 248 | 0.047 (+0.0%) | 1.00 $ billion; the table rounds to $1 billion | pass (in-sample) | HOU-4A, HOU-4D's first count and stage 3 under 62, with fees, search help and the higher payment standards |
| REP-LEASE-0.90-40 | Rental help at 90% leased, FY2040 | 57.0 $ billion | 6-cost.md 1.4; the dossier | 56.7 | -0.25 (-0.4%) | 1.00 $ billion; as above | pass (in-sample) | as above |
| REP-LEASE-0.90-HH | Households housed by those three lines at 90% leased, FY2042 | 2.36 million households | 6-cost.md 1.4; the dossier | 2.36 | -0.002 (-0.1%) | 0.010 million households; the table rounds to 10,000 | pass (in-sample) | leased at the end of FY2042 |
| REP-REACH-ALL | Households housed in FY2042, all three stages with the added counts, 90% leased | 3.60 million households | 6-cost.md 1.4 and 2.12 (3.0-3.6 million); the dossier | 3.56 | -0.041 (-1.1%) | 0.050 million households; printed to 0.1 million | pass (in-sample) | before the financing settlement capped stage 2 (DEC-2026-11-24-09) |
| REP-BOOK-HOU1 | HOU-1 as booked: the 31 components (the duty to house removed by the settlement) | 688 $ billion | models/data/inputs/fiscal-components.csv (HOU-1); DEC-2026-11-24-09; the budget model, as booked | 689 | 1.16 (+0.2%) | 1.50 $ billion; the components carry 6-cost.md's rounded figures | pass (in-sample) | the model's same 31 lines; the booking takes the table's rounded figures |

**Benchmarks against CBO, HUD and the Urban Institute.** 9 benchmarks. 6 independent: 2 pass, 4 miss. 3 in-sample by construction (they check arithmetic, not accuracy): 3 pass.

| ID | Quantity | Target | Source and vintage | Model | Difference | Tolerance (set in advance) | Result | Explanation |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BM-CBO-1 | Cost per assisted household-year with fees, 2020 dollars: CBO's vouchers for all ELI households | 11,717 $ a household-year | EV-HOU-390; CBO budget option, 2015: $290 billion over 2016-25 for 4.5 million more households, phased in over ten years (5.5 household-years each if even; 7-validation.md 1.1) | 12,415 | 698 (+6.0%) | 25%; two vintages a decade apart, a different population (every ELI household) and an assumed even phase-in: a gap beyond a quarter would mean the subsidy is out of line | pass | the model's FY2030 cost per leased household with fees, taken back to 2020 along 6-cost.md 1.1's 4% path |
| BM-CBO-2 | Federal spending per voucher household, 2019 dollars | 9,400 $ a household-year | EV-HOU-391; CBO budget option, December 2018 (for 2019) | 11,937 | 2,537 (+27.0%) | 25%; as BM-CBO-1 | **miss** | a miss: HUD's own 2023 figure ($12,816, EV-HOU-370) is already 36% above CBO's 2019 one, and the account grew 34% in FY2019-23 (EV-HOU-187), much faster than the 4% path the model is taken back along; the plan's households are also poorer than the average voucher household (7-validation.md 1.1). It supports the dossier's verdict: the risk is upward |
| BM-CBO-3 | Cost per added voucher household-year, 2020 dollars: CBO's 10% voucher increase | 9,000 $ a household-year | EV-HOU-390; CBO budget option, 2015: about 200,000 more households for $18 billion over ten years | 12,415 | 3,415 (+37.9%) | 25%; as BM-CBO-1 | **miss** | a miss: CBO priced added vouchers at the existing program's 2015 mix and costs; per-voucher costs rose much faster after 2019 (EV-HOU-187), and the plan pays full fees, an issuance fee and higher payment standards for poorer households |
| BM-HUD-1 | Rent subsidy per leased household, 2023 | 12,816 $ a household-year | EV-HOU-370; HUD, Picture of Subsidized Households, end of 2023 | 12,919 | 103 (+0.8%) | 2%; the subsidy input was grown from this figure, so only arithmetic is checked | pass (in-sample) | in-sample by construction: 6-cost.md 1.1 grows HUD's 2023 figure 4% a year to $17,000 in FY2030 |
| BM-HUD-2 | Share of awards leased, steady state | 0.84 share | EV-HOU-370; HUD, end of 2023: units occupied of units authorized | 0.90 | 0.060 (+7.1%) | 0.10 share; ten points: occupancy is held down by funding as well as by search, so it is a loose floor for the plan's measure | pass | the model's 90% is above it by six points; the measures differ (7-validation.md 1.2) |
| BM-HUD-3 | Share of awards leased, measured the plan's way (with reissue) | 0.67 share | EV-HOU-345; HUD, Emergency Housing Vouchers, February 2023 (about two years after award) | 0.90 | 0.23 (+34.3%) | 0.10 share; ten points: the only precedent measured as the plan measures, at full fees and with waivers | **miss** | a miss, and the reason section 1.4's sensitivity exists: the dossier rates lease-up at risk (7-validation.md 1.2). `--leased 0.75` and `--leased 0.57` rerun every rental line; at 67% the first million houses about 670,000 |
| BM-HUD-4 | Stage 2's renter families: HUD's ELI families with children with worst case needs, less those stage 1 houses | 1.40 to 1.80 million families | EV-HOU-186; HUD, Worst Case Housing Needs 2025 (2023 data): 1.717 million | 1.60 | 0.000 (+0.0%) | inside the range; the dossier's own range around HUD's count | pass (in-sample) | in-sample: the restated count is built from HUD's 1.717 million (6-cost.md 2.12) |
| BM-HUD-5 | Stage 3 under 62: households applying | 0.56 to 0.69 million households | EV-HOU-371; EV-HOU-185; HUD, Worst Case Housing Needs 2025: 1.162 million VLI renter households with a disabled member under 62 and worst case needs, less 345,000 families with children, at a 68.6-85% ELI share | 0.60 | 0.000 (+0.0%) | inside the range or within 0.050; the 85-100% take-up and room for growth that 6-cost.md 2.1 adds | pass (in-sample) | in-sample: 6-cost.md 2.1 builds the 600,000 from these counts |
| BM-URB-1 | Average subsidy of a new voucher, 2022 dollars, per month | 765 $ a month | EV-HOU-392; Urban Institute, 2023 (full funding of vouchers) | 1,035 | 270 (+35.3%) | 25%; as BM-CBO-1 | **miss** | a miss: Urban's new vouchers reach every household under 50% of area median income, who pay more of their rent; the plan's go to homeless households and the poorest families and disabled renters (7-validation.md 1.1) |
<!-- generated:validation:end -->

**Differences explained.**
- *Reproduction.* Every built line matches 6-cost.md 1.2 to the table's own rounding except HOU-3C.02 and HOU-13.01, where the table rounds differently from the section's own build (explanations in the table). The lease-up table of section 1.4 and the households housed reproduce exactly. The booking (`fiscal-components.csv`, HOU-1 and `recovery-adoption.json`, HOU-4D) matches the model's lines within its rounding.
- *Benchmarks.* The three cost-per-household misses (BM-CBO-2, BM-CBO-3, BM-URB-1) all run the same way: older or broader estimates sit 27-38% below the plan's cost per household, which supports 7-validation.md's verdict that the subsidy's risk is upward, not that it is too high. BM-HUD-3 is the lease-up risk the dossier already names.
- *Benchmarks that could not be sourced:* no CBO credit subsidy rate for HOU-3C.02's loans or score of FHA's premium cut, no JCT score of the credits (the 2025 law's 12% increase, EV-HOU-261, is a different change), no CBO spend-out rates for HUD capital grants, and no independent estimate of rent pass-through for a U.S. expansion of this size. Each is in "Evidence still needed".

## Known issues

- The rent readings' tight-market share and central pass-through are judgments; the readings should not be quoted without their ranges (this card; `results.json`, `rents`).
- No fresh-clone job has run the one command yet (step H2b).
- The financing settlement's restatement of stage 2 (`DEC-2026-11-24-09`) is not a scenario here; to add it is a minor version (board, H7 follow-up).
- The reviewer has not yet tried to break the model (release criterion `rc_review`).

## How to run

Standard library only; every input is committed beside the code.

```bash
python3 models/tools/housing/housing_run.py [--out DIR] [--scenario central|low|high] [--leased SHARE] [--print] [--record]
python3 models/tools/housing/test_housing.py
python3 models/tools/housing/test_housing.py --write-card      # regenerate the card's two blocks
```

The results file (`results.json`, on the toolkit's results schema) holds `cost` (each case's lines and totals), `reproduction` (6-cost.md 1.2 against the model), `lease_up` (section 1.4), `reach` and `rents` (with `supply_range`). `--leased` reruns every rental line at another steady-state leased share; `--record` stamps the commit and appends a `RUN-housing-` row to `models/runs.csv`.

## Run log

Recorded runs are rows of `models/runs.csv` with `model_id` `MOD-housing` (`RUN-housing-<date>-<letter>`), written by `models/runlog.py` when the model runs with `--record`. A dossier quoting a figure cites the run ID.
