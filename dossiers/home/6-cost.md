# A home you can keep: cost

Role: section 6 of the housing dossier. It prices each provision of section 4 (`4-specification.md`, `provisions.json`) on the delivery timeline of section 5 (`5-delivery.md`, PR #137), with budget authority, outlays, revenue effects and a low, central and high figure, and tests the result against the fiscal rule (D4-B) with the budget model's own figures. Status: draft (stage C, step 5). It changes no ledger figure, adopted input or model code: every change it implies is a proposal, listed in section 5 below, for Espen and the lead (tier 3). The tax credits are option D, which Espen chose (`DEC-2026-11-09-08`; HOU-2D). It carries Espen's cost decision (`DEC-2026-11-09-09`: housing's FY2040 gap goes to the financing settlement, and the last capital is awarded so it is spent by 2039) and prices the November 9 design decisions that cost money (`-10`): the duty to house, the wider services backstop, fair housing testing money, the R1 readiness money and the tribal set-asides. It also prices stage 2's wider entry (`DEC-2026-11-09-12`) from the count in `research-doubled-up.md` (section 2.7).

## How to read this section

- **Counting rules.** The project's budget conventions (`models/tools/budget/CONVENTIONS.md`). Amounts are nominal dollars by federal fiscal year (FY), as deficit effects: a cost is positive. The common window is FY2030-39 (`ASM-WINDOW`), with FY2029 shown as its own line. Each bill is also read over its own CBO window (budget choice 3). For R2, under the FY2030 budget resolution, that window is FY2030-39, the same as the plan's. "At maturity" means FY2040 and after, where the D4-B maturity test reads (`ASM-MATURITY`). Each provision is measured as an increment over the adopted baseline (`ASM-INCREMENT`). Interest on the added borrowing is left out of each provision's cost, as in a CBO score; the debt tests in section 3 include it (`CONVENTIONS.md`, section 10).
- **Low, central and high.** The central figure is the one the tests use: midpoints decide, with a cautious reading beside them (budget choice 2, `ASM-CALIB-MID`). Low and high move every judgment input in the same direction, so they bracket the result rather than give a probability.
- **What is model output and what is this section's arithmetic.** The model's figures are quoted from its generated files: `legacy/index/fiscal-long-term-model.md` (the fiscal model's D4 tests, scenario DEC), `models/data/recovery-budget-paths.csv` (the Recovery and Solvency budget, which carries the adopted spending allocations; `ASM-REC-EXPLORATORY`), and the provision library's paths for the housing rows (`models/tools/budget/provisions.py`). The provision-level figures are this section's arithmetic. They are an estimate, not a score: the inputs are listed in section 1.1 and every judgment is marked. Section 3 lays this arithmetic over the model's published paths; that is not a model run, and the model stays canonical until a tier-3 PR changes its inputs.
- **Validation status.** The budget model's benchmarks have not all passed (`models/tools/budget/MODEL-CARD.md`, milestone status). The D4 readings rest on the accounting identities and the interest arithmetic, which do pass, and on the ledger's midpoints, which no benchmark tests. Year-by-year budget authority for discretionary rows is rough (PS-4a and PS-4b fail); this section's housing rows are mandatory, but the spend-out of its capital grants is this section's judgment, not CBO's rate.

## In brief

1. **The housing plan costs about $0.78 trillion over FY2030-39** (central; range about $0.59-1.10 trillion) and about $96 billion a year of permanent cost in FY2040. The steps below build up to it, from $0.65 trillion for the first draft's design: **the housing plan before the addendum costs about $0.65 trillion over FY2030-39** (range about $0.51-0.90 trillion), with the tax credits Espen chose (option D) and stage 2's wider entry. That is about $0.06 trillion below what the budget model now books for housing: $0.71 trillion, the ledger's $0.56 trillion plus the $0.147 trillion of HOU-4D and the housing-agency fee allowance that the recovery budget adds. The window falls because the new awards lease up over months rather than at once, the one-time $85 billion package (HOU-1A) is replaced by a smaller start and a standing fund, stage 2 starts in 2034 rather than 2030, and the credits are narrower than the legacy package. Three things raise it from the earlier draft's $0.61 trillion: the capital is now spent inside the window (`DEC-2026-11-09-09`), the November 9 decisions add the duty to house, the wider services backstop and testing money (`-10`), and stage 2 now admits families with no home of their own (`-12`; about $17 billion over FY2037-39). **Memos 9 and 10 (`DEC-2026-11-09-19`, `-20`) add about $57 billion (section 2.8), for about $0.71 trillion in all (about $0.54-0.99 trillion):** down payment help for first-time buyers (about $28 billion, time-limited), FHA's premium cut (about $25 billion) and manufactured-home community grants (about $3.5 billion). The other new provisions cost nothing or sit inside HOU-3C's amounts. **Memos 11 and 12 (`DEC-2026-11-09-21`, `-22`) add about $61 billion (section 2.9), for about $0.77 trillion in all (about $0.58-1.08 trillion):** the home repair fund (about $37 billion, time-limited), the property-tax match for older owners (about $20 billion as states join, permanent) and about $4 billion of legal help, service coordinators and home-sharing grants. **The ROAD to Housing funding map (section 2.10, `road-funding.md`) adds no R2 money:** the plan already funds the Act's three largest channels, and the FY2029 bridge of about $0.87 billion counts inside them. **Memo 13, the rural channel (`DEC-2026-11-10-02`), adds about $14.5 billion (section 2.11), for about $0.78 trillion in all:** USDA field staff and systems, Section 502 at scale, a rural rental preservation fund with vouchers, and self-help and farmworker housing; the rural repair door sits inside the repair fund.
2. **At maturity it costs more than the model books.** In FY2040 the plan's permanent housing lines cost about $96 billion with every addendum (the $90 billion below is the plan before memos 9-13; 0.18% of GDP), against the $65 billion the model carries. The $79 billion and $90 billion in this paragraph include the credits; the table in section 2 counts spending only. Stage 3 for disabled renters (about $9 billion in FY2040, $14 billion by FY2042), stage 2's wider entry (about $8 billion), the standing emergency fund (about $6 billion), and stage 2 at its true timing make up most of the difference. The $90 billion is the $79 billion Espen accepted for now (`DEC-2026-11-09-09`, on option B's credits) plus about $1 billion for option D's credits, about $1 billion for the duty to house and about $8 billion for the wider entry. FHA's premium cut (HOU-10.02) adds about $3 billion a year from FY2040, so the permanent lines come to about $93 billion. The property-tax match for older owners (HOU-13.01), legal help (HOU-13.02) and service coordinators (HOU-13.03) add about $3.5 billion more, for about $96 billion. Memo 13's staff and rural vouchers add about $0.4 billion (section 2.11). With the last capital awarded earlier, capital still being spent after FY2039 adds about $8 billion in FY2040, down from about $16 billion, about $2 billion in FY2041 and nothing after.
3. **Fit with the fiscal rule.**
   - The fiscal model's decided program (scenario DEC) already fails the maturity test by 0.13% of GDP in FY2040, before HOU-4D or any of this section's new costs.
   - The adopted recovery architecture passes it with a margin of $4.5 billion in FY2040, and only that year is tight.
   - Swapped into it, this section's central housing costs use up that margin. FY2040 then fails by about $20 billion counting the permanent lines alone, or $28 billion with the capital tail. With memos 9 and 10, about $23 billion and $31 billion (section 2.8). With memos 11 and 12 as well, about $26 billion and $36 billion: the property-tax match adds about $3 billion a year of permanent cost (section 2.9). With memo 13, about $26.4 billion and $37 billion (section 2.11). From FY2041 the test passes again, by about $20 billion before the addendum (about $12 billion after it, about $11 billion with memo 13), and by more each year after.
   - The high case fails FY2040 and FY2041, and on this section's rough arithmetic FY2042 too. The low case passes.
   - So housing's new permanent costs are not yet paid for in FY2040. Espen decided that this gap goes to the financing settlement and that housing is not trimmed yet, and that slight overshoots in FY2040 are acceptable at this stage of design (`DEC-2026-11-09-09`; questions 1 and 5).
   - Stage 2's wider entry under `DEC-2026-11-09-12` is in these totals (section 2.7): about 0.4 million more eligible families (0.23-0.75 million), about $17 billion over FY2030-39 (8-54) and $8 billion in FY2040 (3-24). It accounts for about $8 billion of the FY2040 gap.
4. **Lease-up is the softest input** (section 1.4). The central 90% leased is the cautious case for the fiscal rule. At 75% the plan costs about $0.60 trillion and houses about 2.2 million households in FY2042 rather than 2.7 million. At 57%, 2022's national search success rate, it costs about $0.56 trillion and houses about 1.7 million. These readings include stage 2's wider entry (section 2.7). From 2037 the duty to house lifts stage 2's share above these readings.
5. **Stage 3 checks out at the lead's rough figure.** On HUD's 2023 counts, about 0.5-0.8 million households qualify if the stage covers people under 62 with severe housing problems. Fully enrolled, they cost about $14 billion a year in FY2042 dollars (range $8-26 billion). If stage 3 also covers disabled people 62 and over, the count could roughly double, and it is unpriced.

## 1. Each provision's cost

### 1.1 Inputs common to the rental help lines

| Input | Central | Low | High | Basis |
| --- | --- | --- | --- | --- |
| Rent subsidy per leased household, FY2030 | $17,000 | $15,500 | $18,500 | HUD's 2023 spending per voucher unit, $1068 a month (about $12,800 a year) [EV-HOU-370], grown at 4% a year to 2030. That lands within 1% of the legacy planning figure ($15,200 in FY2026, growing 3%; `legacy/domains/domain-housing.md`, HOU-4A). The range is judgment: price growth of 2.3% to 5% a year from 2023. The account grew 34% in four years to FY2023 [EV-HOU-187] |
| Growth after 2030 | 3% a year | 2.3% (CPI, `ASM-CPI-PATH`) | 4% | Legacy planning input; range is judgment |
| Share of awards leased at steady state | 90% | 84% | 98% | National vouchers run 84% occupied [EV-HOU-370]. Section 5's full fees, search help, over-issue and reallocation should do better (judgment) |
| Time from award to lease | 6 months | 9 | 3 | Emergency Housing Vouchers took 77 days from issuance to lease [EV-HOU-344], but only 67% were leased after almost two years [EV-HOU-345]. The central figure is judgment |
| Housing agency fees | 8.1% of the subsidy, plus a $750 issuance fee per award | 7%, $500 | 10%, $1,000 | The legacy fee allowance ($12.2 billion on $150 billion; `recovery-adoption.json`, `housing_admin_basis`). Section 5 requires fees in full, never prorated; HUD now prorates regular fees at 85% [EV-HOU-343]. If the legacy 8.1% reflects prorated fees, full fees are about 9.5%, inside the high case. The issuance fee is judgment |
| Search help (HOU-4.07) | $2,000 per new award and per reissue (10% of leased households a year) | $1,000 | $3,500 | Judgment, pending the design research section 4 still owes. Includes section 5's landlord damage and vacancy fund |
| Award timing | R2 signed about January 14, 2030; first awards from April 2030; 250,000 in each of FY2030-33 | | | Section 5's calendar: the two middle central runs finish R2 on October 30, 2029 and January 14, 2030. This section takes the later one, the cautious choice for 2030's lease-up. If R2 is signed on October 30, 2029, awards start about January 2030: that adds about $0.5 billion to HOU-4A's window cost and changes nothing from FY2034 on |

### 1.2 The table

FY2030-39 outlays in billions, central (low-high). "BA" is budget authority. FY2040 is the first year of the maturity test. "Kind" is how the money is enacted (section 4's vehicles).

| Provision | Kind and vehicle | BA, FY2030-39 | Outlays FY2030-39 | FY2040 | At maturity | Source |
| --- | --- | --- | --- | --- | --- | --- |
| HOU-4A.01-.02 One million awards, with full fees | Mandatory, R2 | About equal to outlays, plus each award year's unspent first-year money, which stays available until spent | 147 (116-194): rent 136, fees 12 | 22 (18-30) | Permanent; grows with rents. 900,000 households leased from FY2034 | Section 1.1 |
| HOU-4.07 Search help, all new awards and moves | Mandatory, R2, as a per-award fee beside the agency fee | Equal to outlays | 8 (3-17) | 1 | Permanent, about $0.6-1 billion a year | Section 1.1 |
| HOU-4D.01 Stage 2 guarantee, 2034 on | Mandatory, R2; a right from 2037 | Equal to outlays ("such sums" once it is a right) | 81 (44-142) | 23 (12-44) | Permanent. About 920,000 families leased (590,000-1,470,000) | Section 1.3 |
| HOU-4D.01 Duty to house: placements when a search fails, 2037 on (`DEC-2026-11-09-10`) | Mandatory, R2; inside the right | Equal to outlays | 3 (1-5), FY2037-39 | 1 (0.5-2) | Permanent; grows with stage 2 | Judgment (section 2.5): placements lift stage 2's leased share from 90% to about 95% (93-98%), at the same subsidy and fees. Placement homes may cost more than an average voucher; that is unpriced |
| HOU-4D.01 Stage 2's wider entry: families with children with no home of their own, 2034 on (`DEC-2026-11-09-12`) | Mandatory, R2; inside the right | Equal to outlays | 17 (8-54), FY2037-39 | 8 (3-24) | Permanent. About 310,000 more families leased (135,000-735,000) | Section 2.7: rent and fees, the duty to house, search help and the higher payment standards for the added families |
| HOU-4.08 Stage 3, disabled renters, 2038 on | Mandatory, R2 (effective 2038) | Equal to outlays | 5 (2-13), FY2038-39 only | 9 (5-18) | Permanent. About $14 billion in FY2042 (8-26) when fully enrolled | Section 2.1 |
| HOU-1D.04 One-time start, 2030-31 | Mandatory, R2, one-time | 15 (10-25) in FY2030 | 15 (10-25), spent FY2030-32 | 0 | None | Section 2.2 |
| HOU-1D.01-.03 Standing emergency fund | Mandatory, R2; a capped yearly amount, indexed | 5 a year from FY2031, indexed: 49 (30-79) | 49 (29-78) | 6 (4-10) | Permanent | Section 2.2 |
| HOU-3C.01 State revolving fund grants | Mandatory, R2; borrowed inside the envelope (C21) | 72, awarded FY2030-37 (`DEC-2026-11-09-09`) | 70 | 2 | Time-limited; about $2 billion spent in FY2040, none after | Legacy amounts; section 4's re-timed schedule; spend-out is this section's judgment: 15%, 35%, 30%, 20% over four years |
| HOU-3C.02 Construction loans, $300 billion | Credit subsidy, R2 (Federal Credit Reform Act) | Subsidy BA at commitment: about 15 at a 5% rate; commitments end FY2038 (`DEC-2026-11-09-09`) | 14 | 0.4 | Time-limited | Legacy: subsidy rate 2-10%, central 5%; needs CBO's rate. Disbursed over three years, 40%, 40%, 20% (judgment) |
| HOU-5.01 Public housing repair | Mandatory, R2; borrowed inside the envelope (C31) | 58 (about $7.25 billion a year more than FY2026, FY2030-37; `DEC-2026-11-09-09`) | 57 | 1.5 | Time-limited; about $1.5 billion spent in FY2040, none after | Legacy amount; section 4's re-timed schedule; spend-out judgment |
| HOU-6.01 Zoning reward (Innovation Fund) | Mandatory, R2 | 30 | 25 | 3 | Time-limited as priced (question 6); about $2 billion more in FY2041 | Legacy amount; awards follow finished homes, so spending lags and cannot be moved earlier (judgment) |
| HOU-8.01 Social housing pilot, equity | Mandatory, R2 | 10 | 9 | 1 | Time-limited | Legacy |
| HOU-9A.01 Small federal builder, capital | Mandatory, R2 (capital); regular bill (the corporation) | 5 (2-20) | 5 | 0 | Time-limited capital; its loans repay | Placeholder, judgment: the legacy file leaves it unscored |
| HOU-4.10 Recovery housing, 2030-34 | Mandatory, R2, time-limited | 1.5 | 1.5 | 0 | Appropriations after 2034 if renewed | Placeholder, judgment; no evidence on per-place cost in the register |
| HOU-4.12 HUD services backstop | Mandatory, R2, 2030-39; appropriations after | 6 | 6 | 1 | Permanent at about $0.7 billion as priced, but as appropriations | Placeholder, judgment (section 2.3); includes peer-specialist training and navigator shortfall money (section 5, 2.6) |
| HOU-4.12 Wider backstop through 2035, for tenants whose state Medicaid does not cover the services (`DEC-2026-11-09-10`) | Mandatory, R2, 2030-35 | 6 (3-12) | 6 (3-12) | 0 | Ends 2035 | Placeholder, judgment (section 2.3): $1 billion a year (0.5-2) |
| HOU-4.06 Fair housing testing and enforcement grants, 2030-34 (`DEC-2026-11-09-10`; amount `DEC-2026-11-09-17`) | Mandatory, R2 | 0.5 | 0.5 | 0 | Ends 2034 | Decided: $100 million a year; the program's current appropriation is not in the register |
| Payment standards up to 120% where lease-up is low (section 5, 2.2) | Inside HOU-4A, HOU-4D and HOU-4.08 | Equal to outlays | 7 (2-20) | 2 (0.4-5) | Permanent | Judgment: about a quarter of awards in low lease-up markets, with payment limits about 10% higher there, raise the rent subsidy by about 3% overall (1-6%). The subsidy rises more than the limit, because the tenant's share is fixed by income |
| Inspector general set-aside for audits of the new programs (section 5, section 7) | Mandatory, R2 | $50 million a year, indexed | 0.6 (0.3-1.1) | 0.1 | Permanent | Judgment |
| Federal administration, systems and evaluation set-aside (section 5, 2.1) | Mandatory, R2, available until spent | 0.5% of housing's program outlays | 2 (1-7) | 0.4 | Permanent | Judgment: priced as added money, not carved out of the programs (range 0.25-1%) |
| HOU-10.01 Down payment help for first-time buyers, 2030-39 (`DEC-2026-11-09-19`) | Mandatory, R2, time-limited | 28.5: $1.5 billion in FY2030, then $3 billion a year | 28 (19-47) | 0.15 | Ends FY2039 | Section 2.8 |
| HOU-10.02 FHA's annual premium on purchase loans to 0.30% (`DEC-2026-11-09-19`) | Credit subsidy (Federal Credit Reform Act); R2 or regular bill | Subsidy at endorsement, cohort by cohort | 25 (15-35) | 3 (2-4) | Permanent; grows with FHA's purchase volume | Section 2.8; needs CBO's score |
| HOU-3C.05 Homes to buy inside HOU-3C (`DEC-2026-11-09-19`) | Inside HOU-3C.01 and .02 | — | 0 | 0 | — | Section 2.8: up to $30 billion of the $300 billion of commitments; no added cost |
| HOU-11.01 Manufactured-home community grants (PRICE), 2030-39 (`DEC-2026-11-09-20`) | Mandatory, R2, time-limited | 3.3: $350 million a year in FY2030-38 and $150 million in FY2039, plus $0.2 billion in FY2029 appropriations, $3.5 billion in all (`DEC-2026-11-10-01`) | 3.5 (2-5) | 0.3 | Ends FY2039 | Section 2.8; amount decided by Espen, `DEC-2026-11-09-24`. The companies' chattel purchases are unpriced |
| HOU-12.01 Home repair fund, with HOU-12.02 to .04 inside it, 2030-39 (`DEC-2026-11-09-21`, `-22`) | Mandatory, R2, time-limited | 37.7: $2 billion in FY2030, $4 billion a year in FY2031-38, $3.7 billion in FY2039 (amounts decided, `DEC-2026-11-09-25`, amended by `DEC-2026-11-10-01`); plus $0.3 billion through the repair pilot in FY2029 appropriations, $38 billion in all | 37 (25-54) | 1.2 (tail) | Ends FY2039 | Section 2.9 |
| HOU-13.01 Property-tax match for older owners (`DEC-2026-11-09-22`) | Mandatory, R2, permanent | Equal to outlays | 20.5 (8-35) | 3.1 (1.2-5.2) | Permanent; grows with property taxes | Section 2.9 |
| HOU-13.02 to .04 Equity protection, service coordinators, home-sharing grants (`DEC-2026-11-09-22`) | Mandatory, R2 | Equal to outlays | 3.6 (2-5) | 0.35 | Legal help and coordinators permanent; home sharing ends FY2039 | Section 2.9 |
| HOU-3C.06 Older and disabled renters' homes inside HOU-3C (`DEC-2026-11-09-22`) | Inside HOU-3C.01 and .02 | — | 0 | 0 | — | Section 2.9 |
| HOU-14.01 Rural Development's staff and one loan system, 2030-39 (`DEC-2026-11-10-02`) | Mandatory, R2, time-limited; appropriations from FY2040 | Equal to outlays | 3.5 (2.5-5) | 0.35 | Staff permanent if kept, as appropriations | Section 2.11 |
| HOU-14.02 Section 502 at scale, broader limits (`DEC-2026-11-10-02`) | Credit subsidy, R2 | Subsidy BA with each year's loan level, FY2030-39 | 3.5 (2.5-5.5) | 0.1 | Ends FY2039 | Section 2.11 |
| HOU-14.03 Rural rental preservation fund and vouchers (`DEC-2026-11-10-02`) | Mandatory, R2 (fund); appropriations (vouchers) | 5 for the fund, plus vouchers | 5.2 (3.3-8.6) | 0.46 | Fund ends FY2039; vouchers about $0.06 billion a year, permanent | Section 2.11 |
| HOU-14.04 Self-help and farmworker housing (`DEC-2026-11-10-02`) | Mandatory, R2, time-limited | 2.5 | 2.3 (1.5-3.5) | 0.2 | Ends FY2039 | Section 2.11 |
| Interest on late first payments to landlords (section 5, 2.3) | Inside HOU-4.07 | — | Under 0.1 | — | — | Judgment: a penalty that costs only if HUD or agencies pay late; not in the totals |
| **Spending, total** | | | **661 (487-957)** | **90 with the capital tail; 79 permanent** | | |
| HOU-2D.01-.04 Tax credits, option D (`DEC-2026-11-09-08`; bond-deal boost `DEC-2026-11-09-18`) | Revenue, R2 | None (a revenue loss) | 123 (102-144) | about 16 (13-24) | Permanent for the low-income credit; the trial credits are claimed to about 2048 | Section 4 of this file |
| **Housing, total** | | | **784 (589-1,101)** | **106 (70-178)** | | |

**Provisions with no cost of their own.** HOU-4.01 to HOU-4.05, HOU-4.06's protection itself, HOU-4.09, HOU-4.11, HOU-4.13, HOU-5.02, HOU-6.02, HOU-7B.01, HOU-3C.03, HOU-3C.04 and HOU-2D.04 are rules, conditions, set-asides or regular-bill items. Their costs, if any, sit in the rows above. HOU-4.05's neighborhood payment limits change the cost per award, and the register has no national estimate of by how much (section 4).

**Revenue effects.** HOU-2D is the only revenue line. The construction loans' repayments and interest are inside their subsidy cost under credit reform (legacy file). No offsetting savings are counted anywhere: not shelter or Medicaid savings from Housing First, which the National Academies advise not to expect except perhaps among the heaviest users [EV-HOU-315] [EV-HOU-318], and not lower spending on homelessness programs. That is CBO's practice for savings outside the bill's own accounts, and the cautious choice.

**FY2029, disclosed.** Espen adopted section 5's readiness tranche in R1 (`DEC-2026-11-09-10`; HOU-4.02, item 7). It is a FY2029 line of $0.75 billion (`DEC-2026-11-09-14`) in R1's own window, FY2029-38, outside the FY2030-39 totals above. HUD's other readiness work in 2029 runs on appropriations and the agency rebuild surge (CAP-7S; section 5).

### 1.3 How the rental help lines are built

- **HOU-4A.** 250,000 awards a year, issued evenly from April 2030 (FY2030) and through FY2031-33. Each award leases after the lag, at the steady-state share, and costs the subsidy plus fees.
  - Over the window that is 6.7 million household-years leased (central), against 8.0 million if every award leased the day it was issued.
  - On that no-lag assumption, this section's subsidy gives about $160 billion of rent help, near the legacy $150 billion. The lease-up lag and the 90% leased share take about $24 billion off, leaving $136 billion. Fees are about the legacy allowance ($11.7 billion against $12.2 billion). Search help ($3.6 billion for these awards) is a separate line.
  - So the central figure, $147 billion with fees, is about $15 billion below the legacy $162.2 billion, mostly because the legacy figure pays for every award from its first day.
- **HOU-4D.** Enrollment opens in FY2034 at up to 300,000 families a year. In FY2037 every remaining family that applies enrolls. The group is HUD's 1.717 million extremely low-income families with children with worst case needs in 2023 [EV-HOU-186], less the families the first million reach. Memo 2's split puts that remainder at about 1.2 million, which this section takes as central (1.0-1.5 million). Of them, 85% apply (70-100%; judgment: no take-up evidence for a housing right is in the register). After 2037 the count is held flat, new eligible families replacing those who leave, as memo 2 assumed.
  - Central: about $81 billion through FY2039 and $22 billion in FY2039. Memo 2's arithmetic gave $114 billion at full sign-up, or $123 billion with fees, and about $27 billion a year by 2039. The central case is lower because it counts take-up, the lease-up lag and the leased share; the high case, at full sign-up, is $142 billion.
  - **The $135 billion envelope fits the window but books the wrong years.** The recovery budget spreads it from FY2030 on a four-year ramp (`models/tools/recovery-budget/model.py`, `housing_extra`). So it carries about $35 billion in FY2030-33, before stage 2 opens, and $18.9 billion in FY2040, against $22.7 billion here. The window cost is overstated and the maturity cost understated. Section 5 lists the fix.
- **Stage 2's exit rule** (families keep help while under 80% of area median income, `DEC-2026-11-09-11`) is inside the flat-count assumption. The register has no exit data to price it.

### 1.4 Lease-up sensitivity: cost and households housed

The leased share is the rental help lines' weakest input. National vouchers run 84% occupied [EV-HOU-370]. Emergency Housing Vouchers reached 67% after about two years [EV-HOU-345]. Section 7 (PR #139) cites a national search success rate of 57% in 2022, from the NYU Furman Center. It also cites the Urban Institute's warning, made at a 61% success rate, that success "would likely fall" as more households search. The table moves only the leased share; every other input stays central. It covers the rental help lines: HOU-4A, HOU-4D and HOU-4.08, with fees, search help and the higher payment standards.

| Leased share at steady state | Rental help, FY2030-39 | Rental help, FY2040 | Households housed: first million (FY2034) | Stage 2 (FY2039) | Stage 3 (FY2042) | All three (FY2042) |
| --- | --- | --- | --- | --- | --- | --- |
| 57% | $160 billion | $36 billion | 570,000 | 580,000 | 340,000 | 1.49 million |
| 75% | $208 billion | $47 billion | 750,000 | 765,000 | 450,000 | 1.97 million |
| **90% (central)** | **$248 billion** | **$57 billion** | **900,000** | **920,000** | **540,000** | **2.36 million** |

The table leaves out the duty to house (section 2.5) and stage 2's wider entry (section 2.7); the readings below add the wider entry, scaled to each leased share (about $7 billion in FY2040 at 75%, $5-6 billion at 57%, and 255,000 and 195,000 families housed in FY2042). Under the duty to house, a stage 2 family whose search fails after 2037 is offered a placement, so at low lease-up the rows understate stage 2's cost and reach from FY2037 (judgment).

**What each case means for the headline** (option D, with the re-timed capital and stage 2's wider entry; this section's arithmetic):
- **At 75%:** housing costs about $0.60 trillion over the window and $87 billion in FY2040. The permanent lines then fail FY2040 by about $9 billion; with the capital tail, by about $17 billion. About 440,000 fewer households are housed in FY2042.
- **At 57%:** about $0.56 trillion and $74 billion. The permanent lines pass FY2040 by about $4 billion, but with the tail FY2040 fails by about $4 billion. About 990,000 fewer households are housed in FY2042.

**Why the central figure stays at 90%.** Two reasons; neither is a forecast that the plan will reach 90%.
- **It is the cautious case for the fiscal rule.** Cost rises with lease-up, so the test should be passed at the lease-up the plan is built to reach, not at a shortfall that would also mean the plan failed people.
- **It is what the statute's design aims at.** Fees are paid in full, search help comes with every award, agencies may issue more vouchers than awards, unused awards move to other agencies, and source-of-income protection applies (section 5, 2.2 and 2.3).

**The 57% figure is a lower bound, not a steady state.** It is the share of searches that succeed. A voucher whose search fails goes back to be reissued, so the leased share of awards over time sits above one-shot search success. The national 84% occupancy shows the gap.

**For reach, read the 75% row beside the central one.** Section 7 rates lease-up at risk, and the first awards land in tight markets. Until the plan's own data show otherwise, households housed should be reported as a range: about 2.2-2.7 million across the three stages in FY2042, with stage 2's wider entry. Lower lease-up is not a saving. The money stays available until spent, so unleased awards are help not delivered, and from 2037 the duty to house requires a placement for a stage 2 family whose search fails (HOU-4D.01, `DEC-2026-11-09-10`). Section 7 sets a warning line: below 70% leased at 18 months nationally. No decision changes here.

## 2. The new costs the decisions add

### 2.1 Stage 3: disabled extremely low-income renters, from 2038

**Who.** HUD's 2023 count gives 1.162 million very low-income renter households with someone younger than 62 with a disability and worst case needs. Of them, 345,000 are families with children, 57,000 older-adult households, 175,000 other families and 585,000 other single-person or nonfamily households [EV-HOU-371].
- The families with children fall in stage 2 if they are extremely low income. That leaves about 817,000 households (this section's arithmetic).
- HUD does not split them by extremely low and very low income. Across all renters, extremely low-income households are 68.6% of worst case needs [EV-HOU-185]. A person living alone on SSI had $914 a month in 2023 [EV-HOU-372], under the extremely low-income line almost everywhere, so the share among disabled households is likely higher (judgment).
- At a 69-85% share that is about 560,000-690,000 households. With 85-100% applying, and room for growth or a broader test, the central count is 600,000 (450,000-800,000).
- That matches the lead's rough range of 0.5-0.8 million.

**Cost.** Enrollment over 2038-40, a third a year (judgment; section 4 leaves the pace to the care flagship and this section), at the same subsidy, fees and lease-up as the other awards.
- FY2038-39: about $5 billion (2-13), inside the window and outside the $135 billion, as memo 2's condition requires.
- FY2040: $9 billion (5-18).
- Fully enrolled: about 540,000 households leased, about $14 billion in FY2042 (8-26) and $15.5 billion in FY2045.
- **Check of the lead's estimate.** "$12-19 billion a year at maturity" holds. At FY2042 rents, with fees, 0.5-0.8 million households leased would cost about $13-21 billion; with 90% of them leased, as section 1.1 assumes, about $12-19 billion. The central case, $14 billion, is inside both.

**What the count leaves out, unpriced.**
- **Disabled people 62 and over.** HUD's report counts disability only under 62 [EV-HOU-371]. Section 4 says older renters who are *not* disabled have no funded route, which implies older disabled renters are in stage 3. There are 1.749 million older extremely low-income worst-case households [EV-HOU-186]. Two-thirds of older voucher holders report a disability (HUD's 2023 voucher data, not in the register), so the older disabled group could be as large as the under-62 group or larger. The register has no count, so it is unpriced (question 2).
- **The severe-problems test.** This section assumes stage 3 uses stage 2's test: unassisted, with severe problems. Without it, all unassisted extremely low-income disabled renters would qualify, a larger and uncounted group.
- **Services.** Stage 3's home and community-based services are the care flagship's (shared rule 7); see section 2.3. The accessible homes come from HOU-3C's existing money (HOU-3C.03), at no added cost in this section.

**Financing.** Stage 3 is a permanent claim from FY2038, so under D4 it must be paid for from FY2040 (section 4, HOU-4.08). Section 3 shows it is the largest single reason housing's FY2040 cost exceeds the model's.

### 2.2 The emergency fund (HOU-1D)

**Form.** Section 4 leaves the amount to this section. A standing fund that paid every eligible crisis would be open-ended: 23% of renters fell behind on rent at some point in 2025 [EV-HOU-008], and landlords filed 1.23 million eviction cases in 2025 in the places Eviction Lab tracks, only part of the country [EV-HOU-077]. So this section prices it as a **capped yearly amount, set in the statute and indexed to prices**, paid through the grantee network by need formula. Mandatory money of a fixed size, not an entitlement, is how the 2021-22 program and Emergency Housing Vouchers were funded [EV-HOU-150] [EV-HOU-188].

**Size (judgment, central $5 billion a year from FY2031; range $3-8 billion).**
- At about $3,500 per household, with legal help and administration, $5 billion serves roughly 1.4 million households a year. That is about the scale of the tracked eviction filings and a small share of renters who fall behind.
- The per-household figure is judgment. It sits between the Santa Clara trial's average of about $2,000 [EV-HOU-109] and the cap of four months' Fair Market Rent (HOU-1D.01).
- Targeting decides value: in Chicago, preventing one case of homelessness cost about $10,300, and less with better targeting [EV-HOU-108].
- **The annual cap** (`DEC-2026-11-09-17`): four months of Fair Market Rent per household in any 12 months, usable across any number of crises, replacing one episode a year capped at four months. The most one household can receive in a year is unchanged, so the fund's priced range ($3-8 billion a year, a fixed yearly amount) does not move. What can change is the split: a household with a second crisis can now draw the rest of its cap, which raises the average per household and lowers the count served. If one in ten paid households returns within the year for about $1,500 more (judgment), the average rises to about $3,650 and $5 billion serves about 1.37 million households rather than 1.4 million. The repeat-use count HOU-1D.01 publishes will show the real split.

**The one-time start (HOU-1D.04): central $15 billion over 2030-31 (range $10-25 billion).** It is smaller than the $85 billion of HOU-1A, and rent help only. The binding limit is what a network built in 2030 can pay out well. The 2021 program spent about 6% of its first $25 billion in five months, and paid 2% of households twice [EV-HOU-150]. Section 5 has the network named in 2030. Outlays are spread over FY2030-32 (30%, 50%, 20%; judgment).

**Against the ledger.** The ledger's housing title carries HOU-1A at $85 billion (section 4). HOU-1D costs $64 billion over the window: $15 billion one-time and $49 billion standing. So the window falls about $21 billion. But the standing fund adds about $6 billion a year at maturity, where HOU-1A added nothing.

### 2.3 Supportive-housing services: what is housing's and what is care's

| Cost | Whose | Where it is counted | Priced here? |
| --- | --- | --- | --- |
| Rent for supportive-housing tenants | Housing | HOU-4A stage 1 awards (HOU-4.11, item 4) | Yes, inside HOU-4A |
| Tenancy-sustaining services, housing navigation, assertive community treatment for Medicaid enrollees | Care (HLT-4, Medicaid home and community-based services) | The care flagship's HLT-4 row, with Medicaid restored by HLT-1 | No: counting it here would count it twice |
| Medicines for opioid use disorder and other treatment | Care and health coverage (HLT-1, HLT-4) | Health rows | No |
| Stage 3's home and community-based services | Care (HLT-4) | Health rows | No |
| The same services for tenants without Medicaid | Housing (HOU-4.12 backstop) | This section | Placeholder |
| The same services, through 2035, for tenants whose state Medicaid program does not cover them | Housing (HOU-4.12, `DEC-2026-11-09-10`) | This section | Placeholder |
| Peer training, wage floors and caseload limits on the HUD backstop | Housing | Inside HOU-4.12 | Placeholder |
| VA case managers for HUD-VASH | VA, care flagship (section 5, 2.6) | Not housing | No |

**The backstop is a placeholder.** It is priced at $0.5 billion in FY2030, growing 3% a year: about $6 billion over the window and $0.7 billion in FY2040 (judgment). The register has neither the per-tenant service cost nor the count of supportive-housing tenants without Medicaid (section 4, "Evidence still needed").
- In Denver, savings elsewhere offset about half the yearly cost per person, $6,876 [EV-HOU-318]. That gives the scale, not the split.
- Espen adopted section 5's extension of the backstop, through 2035, to tenants whose state Medicaid program does not cover the services (`DEC-2026-11-09-10`). It is priced as a placeholder of $1 billion a year over FY2030-35 (range $0.5-2 billion), about $6 billion in all (judgment). The real cost depends on how many states leave these services out of HLT-4's benefit; it could be several times more.

**The rule against double counting.** HLT-4's row prices the Medicaid services. This dossier prices only the backstop, for people HLT-4 does not reach. When HLT-4 is costed, its documentation should say whether it includes tenancy supports and assertive community treatment, as section 4 asks (HOU-4.12, item 1). If it does not, the gap stays with care, not housing.

### 2.4 Full housing agency fees and administration

- **Fees in full, never prorated, with an issuance fee** (section 5, 2.2) are inside HOU-4A, HOU-4D and HOU-4.08: about $12 billion, $7 billion and $1 billion over the window. That is 8.1% of the subsidy plus $750 an award.
- If "in full" means the unprorated rate and the legacy allowance was set at prorated rates, the fee is about 9.5%. That adds about $2.5 billion over the window and $0.7 billion a year at maturity (this section's arithmetic; inside the high case).
- **HUD's own staff** are in the agency rebuild (CAP-7S) and the sustained increase (CAP-7), not here (section 4, HOU-4A.02). CAP-7 is a legacy working choice whose agency shares are not yet set, so HUD's staffing after the surge has no settled line (section 5, 2.1).
- Section 5's set-aside of each new mandatory program for federal administration, systems and evaluation is priced as added money: 0.5% of housing's program outlays, about $2.4 billion over the window (judgment; section 1.2). If it is carved out of the programs instead, it adds nothing and buys slightly less help.

### 2.5 The guarantee from 2037

Stage 2 becomes a right in 2037: every eligible family that applies gets help (HOU-4D.01). That turns its cost from a capped envelope into an estimate.
- **The year it becomes a right.** FY2037 enrollments take stage 2 from about 900,000 families awarded to the full group, about 1.02 million in the central case. Its cost rises from $12 billion in FY2036 to $18 billion in FY2037 and $22 billion by FY2039 (central).
- **The duty to house** (`DEC-2026-11-09-10`; HOU-4D.01). A family whose search fails is offered an attached home or a reissued voucher with a higher payment standard. This section prices it as lifting stage 2's leased share from 90% to about 95% from FY2037 (93-98%; judgment), at the same subsidy and fees: about $3 billion over FY2037-39 (1-5) and $1.3 billion in FY2040 (0.5-2), growing with stage 2. If placement homes cost more than an average voucher, as attached homes in tight markets may, the cost is higher; the register has no evidence on it.
- **Remedies.** Espen adopted the private right of action, with attorney's fees, and deemed approval (`DEC-2026-11-09-10`; section 5, 6.3). Neither is separately priced. Deemed approval pays some families before checks, and its error cost is unknown; fees fall on agencies that lose suits.
- **The risk.** The high case, $44 billion in FY2040, is about twice the central one. Full sign-up, a larger group and faster rent growth drive it, and none of them is in the government's control once help is a right. That is what memo 2 warned: "the $135 billion becomes an estimate, not a cap."

### 2.6 Tribal set-asides

Espen decided that tribal housing gets dedicated set-asides (`DEC-2026-11-09-10`; HOU-4.13). They are shares of amounts already priced, so they add nothing to the totals. At the shares Espen decided (`DEC-2026-11-09-16`), about $14 billion of the FY2030-39 money goes through tribes (this section's arithmetic, central):
- 3% of the emergency fund and its start: about $1.9 billion of $64 billion;
- 3% of the new-award money (HOU-4A, HOU-4D with the duty to house and the wider entry, HOU-4.08, with fees, search help and higher payment standards): about $8 billion of $268 billion;
- 5% of the revolving-fund grants: about $3.6 billion of $72 billion.

Whether a dollar buys more or less help through tribes than elsewhere is unknown: the form follows each tribe's plan, and repair and building cost more per household than rent help. Restoring resources sufficient for tribes to care for their people may need more than these shares. HOU-4.13's proposed need report would price that, and any added money is a later decision.

### 2.7 Stage 2's wider entry: families with no home of their own (`DEC-2026-11-09-12`)

Espen decided that from 2034 stage 2 also admits extremely low-income families with children who have no home of their own, doubled up or homeless (HOU-4D.01). They were outside the 1.717 million [EV-HOU-186], because they are not renter households [EV-HOU-432].

**Count** (`research-doubled-up.md`, section 7; grade D):
- a one-time stock of doubled-up families of about 0.3 million at the 2034 opening (0.15-0.55 million), net of those stage 1 houses first;
- a flow of about 0.1 million homeless families a year (0.08-0.2 million). Under section 1.3's convention, stage 2's count is held flat after 2037, new families replacing those who leave. The flow is priced the same way: it adds one year's flow, about 0.1 million, to the standing count (judgment). Most families who become homeless come from groups already counted, doubled up or rent-burdened [EV-HOU-427] [EV-HOU-428], so later years mostly replace exits. The high case's 0.2 million allows for longer stays.
- In all: about 0.4 million more eligible families (0.23-0.75 million), against the 1.2 million (1.0-1.5 million) section 1.3 prices.

**Cost.** The same inputs as stage 2 throughout:
- 85% apply (70-100%) and 90% lease (84-98%), at stage 2's cost per leased household with fees: about $25,000 in FY2040 (central).
- Enrollment is capped at 300,000 a year in FY2034-36. In the central and high cases the cap already binds, so the added families enroll in FY2037, when the right begins. In the low case they fit under the cap and enroll in FY2036.
- The duty to house, search help ($2,000 an award) and the higher payment standards scale with them.

| | Central | Low | High |
| --- | --- | --- | --- |
| Added families eligible | 400,000 | 230,000 | 750,000 |
| Leased (FY2040) | 306,000 | 135,000 | 735,000 |
| FY2030-39 outlays | $17 billion (FY2037 $1 billion, FY2038 $7 billion, FY2039 $8 billion) | $8 billion | $54 billion |
| FY2040 | $8 billion | $3 billion | $24 billion |

This section's arithmetic, rounded. The central window cost is rent and fees $14.6 billion, the duty to house $1.0 billion, search help $0.7 billion and the higher payment standards $0.4 billion. Need-based intake may enroll these families before 2037 in place of others, which leaves each year's total unchanged under the cap.

**What it means.**
- The wider entry is about 30% of stage 2's central count. It is a right from 2037, so like the rest of stage 2 it is an estimate, not a cap.
- It accounts for about $8 billion of FY2040's maturity gap (section 3.3).
- It replaces part of section 7's "count risk" (families forming households once help is a right), so the two should not be added.

### 2.8 Homeownership and broad supply (memos 9 and 10)

Espen chose memo 9's parts 1 C (with a higher income limit and plain stacking), 2 B and 3 C, and memo 10's four B options (`DEC-2026-11-09-19`, `-20`). The research note's draft numbers (`research-ownership-supply.md`, section 5) are the starting point; every input here is this section's judgment unless it cites the register.

| Provision | FY2030-39, central (low-high) | FY2040 | How it is built |
| --- | --- | --- | --- |
| HOU-10.01 Down payment help | 28 (19-47) | 0.15 (tail) | $1.5 billion of budget authority in FY2030 while states start, then $3 billion a year to FY2039; paid at closing, so nearly all spends in the year, with about 5% spilling into the next. Low and high are memo 9's $20-50 billion. About 1.4 million buyers at an average of about $20,000 [EV-HOU-525]. **Espen's higher income limit (140%, 160% in high-cost areas) does not change the cost**: the money is a fixed yearly amount, so more eligible buyers means the money is rationed sooner, first-generation buyers first. It lowers the share of buyers who would not otherwise have bought, since buyers at 120-140% of area median income are less often short of cash (judgment): about 0.17-0.26 million lasting added owners rather than the memo's 0.19-0.28 million |
| HOU-10.02 FHA premium cut | 25 (15-35) | 3 (2-4) | 0.25 points of premium on about $200 billion of new purchase loans a year (about 650,000 loans [EV-HOU-552]), counted under credit reform as each year's cohort's lost premiums over its life, at about $2.5-3 billion a cohort (judgment; average loan life of about six years). The memo's $15-25 billion counted cash premiums forgone in the window; credit-reform scoring pulls each cohort's later years forward, so the score is higher. Permanent: about $3 billion a year in FY2040, growing with FHA's volume. CBO's score decides |
| HOU-3C.05 Homes to buy | 0 | 0 | Up to $30 billion of HOU-3C.02's commitments and part of HOU-3C.01's grants; no added budget authority. Short construction loans may carry a lower subsidy rate than the rental loans, which would lower HOU-3C.02's score a little (needs CBO) |
| HOU-11.01 Community grants (PRICE) | 3.5 (2-5) | 0.3 | $350 million a year (decided by Espen, `DEC-2026-11-09-24`), spent over two years; FY2039 is $150 million and $200 million comes first as a FY2029 bridge in appropriations (`DEC-2026-11-10-01`, section 2.10). The Fannie Mae and Freddie Mac chattel purchases add credit risk that CBO counts on budget [EV-HOU-556]; unpriced |
| HOU-11.02 Federal land sales | Not counted | — | Receipts, possibly about $15 billion over a decade on AEI's estimate [EV-HOU-583], with up to half kept for local water and roads (decided by Espen, `DEC-2026-11-09-24`). Asset-sale receipts are usually left out of budget-enforcement scoring (judgment), so this section counts none |
| HOU-11.03 Infill exclusion; HOU-6.01's wider list | 0 | 0 | No money |
| **Total** | **57 (36-87)** | **3.5 (2.3-4.8)**, of which 3 permanent | |

- **Fiscal rule.** HOU-10.01 and HOU-11.01 are time-limited and end in FY2039, so they add only a small tail to FY2040. HOU-10.02 is permanent: it adds about $3 billion a year to FY2040's gap. On the central figures, FY2040 now fails by about $23 billion counting permanent lines alone, or about $31 billion with the tails (section 3.3). FY2041 still passes, by about $16 billion.
- **The envelope.** HOU-10.01 and HOU-11.01 qualify as time-limited investments. Borrowing for them inside the envelope (about $0.03 trillion of the $0.30 trillion left) would lower the general-fund claim in the window by that much and leave the maturity test unchanged (section 5, item 12).
- **Who it reaches.** HOU-10.01's higher income limit and HOU-10.02 reach the third and fourth income fifths, the groups D3 watches (`3-design.md`, fork 3); the incidence model should check them (section 7).

### 2.9 Repair and aging in place (memos 11 and 12)

Espen chose every recommended part of memos 11 and 12 (`DEC-2026-11-09-21`, `-22`). The research note's draft numbers (`research-repair-aging.md`, section 11) are the starting point; the amounts are section 4's, decided by Espen as proposed (`DEC-2026-11-09-25`; question 10), and every input here is this section's judgment unless it cites the register.

| Provision | FY2030-39, central (low-high) | FY2040 | How it is built |
| --- | --- | --- | --- |
| HOU-12.01 Home repair fund, with HOU-12.02 to .04 inside it | 37 (25-54) | 1.2 (0.8-1.6), tail only | $2 billion of budget authority in FY2030 while grantees start, then $4 billion a year to FY2038 and $3.7 billion in FY2039, with $0.3 billion first as a FY2029 bridge through the ROAD repair pilot (`DEC-2026-11-10-01`, section 2.10), $38 billion in all; about 70% spent in the year awarded and 30% the next, so about $1.2 billion spills into FY2040. About 220,000-330,000 homes a year at $12,000-18,000 each with administration, from Philadelphia's and Detroit's costs [EV-HOU-647] [EV-HOU-660]. Low and high are the research note's $25-55 billion. Renter repairs (about $0.5-1 billion a year), readiness repairs for clean power (about $0.25-0.75 billion once CLI-5W runs) and the older-adult track (about $0.3-1.6 billion) are uses of the same money, not additions |
| HOU-13.01 Property-tax match for older owners | 20.5 (8-35) | 3.1 (1.2-5.2), permanent | Half of state relief above 3% of income for owners 65 or over and disabled owners up to 80% of area median income, only above each state's 2028 effort. States join as they change their laws: about $0.5 billion in FY2031, $1.5 billion in FY2032, $2 billion in FY2033, $2.5 billion in FY2034, then growing about 4% a year with property taxes [EV-HOU-670]. At maturity about 2-4 million older owners at $500-1,000 each of federal share (judgment) |
| HOU-13.02 Equity protection | 2 (1-3) | 0.2, permanent | $200 million a year of legal-aid grants from FY2030; about 20,000 titles a year at about $9,200 [EV-HOU-684] plus foreclosure defense. The reverse-mortgage rules carry no scored cost while FHA's reverse-mortgage book stays well capitalized [EV-HOU-679] |
| HOU-13.03 Service coordinators | 1.35 (0.9-1.8) | 0.15, permanent | $150 million a year from FY2031, about 1,800 more coordinators at HUD's cost per grant [EV-HOU-672] |
| HOU-13.04 Home-sharing grants | 0.27 (0.15-0.45) | 0 | $30 million a year, FY2031-39; ends FY2039 |
| HOU-3C.06 Older and disabled renters' homes | 0 | 0 | A share of HOU-3C's existing amounts |
| **Total** | **61 (35-94)** | **4.7 (2.2-7.3)**, of which 3.5 (1.4-5.7) permanent | |

- **Fiscal rule: the property-tax match is the addendum's main permanent cost, and it widens the FY2040 gap.** The repair fund and home-sharing grants are time-limited and end in FY2039, leaving only the repair fund's tail in FY2040. The property-tax match, legal help and coordinators are permanent: about $3.5 billion a year in FY2040, of which about $3.1 billion is the tax match, rising about 4% a year after. On the central figures, FY2040 now fails by about $26 billion counting permanent lines alone (up from about $23 billion), or about $36 billion with the tails (up from about $31 billion) (section 3.3). FY2041 still passes, by about $12 billion (down from about $16 billion), and FY2042 by about $60 billion. The match goes to the financing settlement with the rest of housing's FY2040 gap (`DEC-2026-11-09-09`); if it must be trimmed, a lower match rate or a later start are the levers, not a stricter test for older owners.
- **The envelope.** The repair fund qualifies as a time-limited investment, like HOU-3C.01 and HOU-5.01. Borrowing for it inside the envelope (about $0.037 trillion of the roughly $0.27 trillion left after memos 9 and 10) would lower the general-fund claim in the window by that much and leave the maturity test unchanged (section 5, item 13).
- **Who it reaches.** The repair fund reaches low-income owners, most of whom the rental help never touches; the tax match and legal help reach older owners up to 80% of area median income. Neither has a phase-out that stacks with the rental help's (`7-validation.md`, 3.7).

### 2.10 Funding the ROAD to Housing Act (board row 6a)

The funding map is `road-funding.md`. Nothing in the ROAD to Housing Act is funded in FY2027: the continuing resolution runs to December 11, 2026 and bars new starts [EV-HOU-750] [EV-HOU-751], and the House committee's THUD bill has no ROAD line [EV-HOU-754]. The plan already funds the three largest ROAD channels from FY2030: the Innovation Fund through HOU-6.01, the whole-home repair pilot's successor HOU-12.01, and PRICE through HOU-11.01. So the map adds no R2 money. Espen decided them as recommended on November 10, 2026 (`DEC-2026-11-10-01`; question 11).

| Item | Money | Effect on this section's totals |
| --- | --- | --- |
| 2027-28 asks for the ROAD programs (`road-funding.md`, 2.3) | About $0.51 billion in FY2027 and $0.62 billion in FY2028 | None: 2027-28 law, outside the plan's window. Under the "total" rule below, a win lowers the plan's cost |
| The "total" rule: HOU-6.01, HOU-12.01 and HOU-11.01 are total program levels, counting any ROAD money appropriated before or beside them | — | None against the adopted baseline (CBO, February 2026, which carries no ROAD money). If a later baseline carries a 2027-29 appropriation forward, the plan's cost falls: for the Innovation Fund at $200 million a year, about $2 billion over FY2030-39 |
| FY2029 bridge in FY2029 appropriations, **option A (decided, `DEC-2026-11-10-01`)**: inside the plan's money | About $0.87 billion of budget authority in FY2029: $270 million in HOU-6.01's channel (Innovation Fund, planning grants, pattern books, single-stair grants), $300 million in HOU-12.01's (the repair pilot), $200 million in HOU-11.01's (PRICE), $100 million in HOU-3C.01's (RESIDE). Each program's R2 budget authority falls by the same amount, from its last years | Total budget authority unchanged, but spending moves earlier: FY2030-39 outlays about +$0.4 billion (0.3-0.8), since the bridge spends in FY2030-32 while the cut years would have spent partly after FY2039; FY2040-42 tails about −$0.4 billion (about −$0.3 billion in FY2040). Housing still about $0.77 trillion. Amends decided FY2039 amounts: HOU-12.01 from $4 billion to $3.7 billion (`DEC-2026-11-09-25`), HOU-11.01 from $350 million to $150 million (`-24`) |
| FY2029 bridge, **option B**: on top | The same $0.87 billion, added | FY2030-39 about +$0.8 billion (housing still about $0.77 trillion); FY2029 about +$0.04 billion; FY2040 unchanged |
| HOME, if the House's FY2027 cut to $500 million stuck (`road-funding.md`, 2.1) | Restoring $1.25 billion is about $0.75 billion a year | None against the adopted baseline, which carries FY2026's level. Against a rebased baseline it is new money of about $7.5 billion over FY2030-39 and about $0.9 billion a year in FY2040: then the FY2040 gap would widen by about $1 billion (budget choice 0c decides which baseline) |

**FY2040 gap.** The permanent lines are unchanged under either option: about $26 billion (section 2.9). With the tails it stays about $36 billion; option A trims about $0.3 billion off FY2040's tail. The bridge money is time-limited and spends out by about FY2032.

**A cut to the capital grants' base would shrink HOU-5.01's repairs.** HOU-5.01 adds about $7.25 billion a year above FY2026's $3.2 billion of public housing capital grants. A lasting cut like the House's $2.29 billion [EV-HOU-753] would leave the plan repairing less than decided unless HOU-5.01 rose by about $0.9 billion a year; this section does not price that, since the FY2027 level is not yet law.

### 2.11 The rural channel (memo 13)

Espen chose every recommended part of memo 13 (`DEC-2026-11-10-02`), with the amounts the memo proposed. The memo's draft numbers (`memos/13-rural.md`, "Rough cost of the recommendations") are the starting point; every input here is this section's judgment unless it cites the register.

| Provision | FY2030-39, central (low-high) | FY2040 | How it is built |
| --- | --- | --- | --- |
| HOU-14.01 Field staff and one loan system | 3.5 (2.5-5) | 0.35, permanent if kept | About 2,000 more staff at about $150,000 each with benefits and offices: $0.1 billion in FY2030, $0.2 billion in FY2031, then $0.3 billion a year; the system at about $0.15 billion a year over FY2030-34 (rural delivery note, section 4.1). From FY2040 the staff are a regular Agriculture appropriation, counted here as a permanent claim, growing with pay |
| HOU-14.02 Section 502 at scale, broader limits | 3.5 (2.5-5.5) | 0.1, tail | Direct loan levels above FY2026's $1 billion [EV-HOU-781]: +$0.5 billion in FY2030, +$1.5 billion in FY2031, +$2.5 billion in FY2032, +$3 billion a year in FY2033-39, about $25.5 billion more lending, at OMB's FY2026 subsidy rate of about 13% (rural delivery note, section 1.2): about $3.3 billion. Direct loans to 100% of area median income add about $0.2 billion, since higher-income borrowers take little payment help. Guaranteed loans to 140%/160% earn more in fees than they cost; counted as zero. A higher delinquency re-estimate is the main risk [EV-HOU-701] |
| HOU-14.03 Rural rental homes | 5.2 (3.3-8.6) | 0.46, of which 0.06 permanent | Preservation fund $0.5 billion a year, $5 billion of budget authority, spent over about three years: about $4.6 billion in the window and $0.4 billion in FY2040. Rural vouchers about $0.06 billion a year, permanent (`road-funding.md`'s placeholder). Continued rental assistance costs about $7,700 a unit a year [EV-HOU-773] but stays inside the baseline, which carries today's level forward; it costs more only if the appropriation would otherwise fall |
| HOU-14.04 Self-help and farmworker housing | 2.3 (1.5-3.5) | 0.2, tail | About $0.25 billion a year more than FY2026's levels [EV-HOU-756], $2.5 billion of budget authority, about 90% spent in the window |
| HOU-12.01's rural door; HOU-10.01's link; HOU-14.05; HOU-14.06 | 0 | 0 | About a sixth of HOU-12.01's $38 billion routed through USDA (no added money); rules and a map |
| **Total** | **14.5 (10-21)** | **1.1, of which 0.4 permanent** | |

- **Fiscal rule.** The fund, the loan levels and the self-help and farmworker money end in FY2039, leaving tails of about $0.7 billion in FY2040. The staff, if kept, and the vouchers are permanent: about $0.4 billion a year in FY2040. On the central figures FY2040 now fails by about $26.4 billion counting permanent lines alone (up from about $26 billion), or about $37 billion with the tails (up from about $36 billion). FY2041 still passes, by about $11 billion. The gap goes to the financing settlement with the rest of housing's (`DEC-2026-11-09-09`); the staff are the lever if it must shrink, not the rules that let people in.
- **The envelope.** HOU-14.01's systems money, HOU-14.03's fund and HOU-14.04 qualify as time-limited investment. Borrowing for them inside the envelope (about $0.01 trillion) would lower the general-fund claim in the window and leave the maturity test unchanged.
- **Who it reaches.** Low- and moderate-income rural owners, buyers and renters, many in places HUD's grantees reach thinly. The repair door changes no one's terms, only where they apply. HOU-14.05's published count is the check that the single test leaves no one behind (Espen's condition).

## 3. Fit with the fiscal rule

### 3.1 The rule

D4-B has three parts (`ASM-MATURITY`, `ASM-ENVELOPE`, `ASM-GUARDRAILS`; Decision Brief 2):
- **Maturity.** Permanent programs are paid for: the general fund's primary balance from the program must be at or below zero in FY2040 and every later year to 2056.
- **Envelope.** Time-limited investments may be borrowed for inside 0.5% of GDP to 2034, tapering to zero by 2040.
- **Guardrails.** Total debt and net interest stay below the baseline.

### 3.2 What the model says today

| Reading | Result | Housing inside it | Source |
| --- | --- | --- | --- |
| Fiscal model, decided program (DEC): maturity | **Fails**: general fund 0.13% of GDP short in FY2040 (about $72 billion) and in its worst year | HOU-1 only ($0.56 trillion over the window; $44.7 billion in FY2040). No HOU-4D, no fee allowance | `legacy/index/fiscal-long-term-model.md`, "D4 tests" |
| Fiscal model, DEC: envelope | $1.60 trillion of room over 2030-39; $1.30 trillion held by accepted borrowing lines; $0.30 trillion left | C21 (HOU-3C's state grants, $0.06 trillion) and C31 (HOU-5's repair, $0.06 trillion) | Same; `models/data/inputs/ledger-cuts.csv` |
| Fiscal model, DEC: guardrails | Pass: total debt 2.8, 11.6 and 23.8 points below the baseline in 2035, 2045 and 2056; net interest below the baseline | As above | Same |
| Recovery budget, mixed case (the adopted architecture; its tax rates exploratory) | **Passes** the maturity test, by $4.5 billion in FY2040, $49.6 billion in FY2041 and $96.7 billion in FY2042; the margin widens every year to 2056 | HOU-1's two components, HOU-4D's $135 billion and the $12.2 billion fee allowance: $65.2 billion in FY2040 | `models/data/recovery-budget-paths.csv`, case `mixed`, `agenda_gf_primary_bn`; `ASM-REC-EXPLORATORY` |

The two readings differ because the recovery budget adds the adopted architecture's new revenue and spending changes. Its tax schedule is exploratory and no financing is adopted. Neither model certifies D4 (`legacy/index/recovery-budget.md`).

### 3.3 This section's housing costs in the rule

Replace the model's housing paths with this section's, and leave everything else as the model has it.

| FY | Model's housing | This section, central (option D) | Difference | Recovery budget's general-fund balance, adjusted | Test |
| --- | --- | --- | --- | --- | --- |
| 2039 | 88.9 | 96.9 | +8.0 | 145.3 (inside the envelope years) | Not a maturity year |
| 2040 | 65.2 | 97.3 (89.6 permanent) | +32.1 (+24.4) | **+27.5 (+19.8 permanent only)**, 0.05% (0.04%) of GDP | **Fails** |
| 2041 | 67.5 | 97.6 | +30.1 | −19.5 | Passes |
| 2042 | 69.8 | 99.1 | +29.3 | −67.4 | Passes |
| 2045 | 77.2 | 108.1 | +30.9 | −191.0 | Passes |
| 2056 | 110.8 | 149.0 | +38.2 | −460.3 | Passes |

Billions. The adjusted balance is the recovery budget's FY figure plus the difference; negative passes. The table is before memos 9 and 10: their central figures add about $3.5 billion in FY2040 ($3 billion permanent), about $3.1 billion in FY2041 and about $3.3 billion in FY2042 (section 2.8), so FY2040 fails by about $31 billion (about $23 billion permanent only), and FY2041 and FY2042 still pass, at about −$16 billion and −$64 billion. Memos 11 and 12 add about $4.7 billion in FY2040 ($3.5 billion permanent), about $3.6 billion in FY2041 and about $3.7 billion in FY2042 (section 2.9), so FY2040 fails by about $36 billion (about $26 billion permanent only), and FY2041 and FY2042 still pass, at about −$12 billion and −$60 billion. Memo 13 adds about $1.1 billion in FY2040 ($0.4 billion permanent) and about $0.5 billion in FY2041 and FY2042 (section 2.11), so FY2040 fails by about $37 billion (about $26.4 billion permanent only), and FY2041 and FY2042 still pass, at about −$11 billion and −$59 billion. Stage 2's wider entry under `DEC-2026-11-09-12` is included (section 2.7): about $8 billion in FY2039-40, growing about 3% a year, $13 billion by FY2056.
- **Low case:** FY2040 passes, at about −$6 billion (the wider entry's low case adds about $3 billion).
- **High case:** FY2040 fails by about $95 billion (0.19% of GDP) and FY2041 by about $54 billion, with the wider entry's high case ($24 billion in FY2040) included. Before it, the high case passed from FY2042; it now likely fails FY2042 by about $10 billion and passes from FY2043 (this section's rough arithmetic; the model run should confirm it, section 5, item 8).
- **Against the fiscal model's DEC,** which carries no HOU-4D, this section's housing adds about $52 billion in FY2040. That widens DEC's shortfall from 0.13% to about 0.24% of GDP.
- **What changed from the earlier draft** (option B, capital spent to FY2042): option D adds about $1 billion a year through 2047; the duty to house adds about $1-1.4 billion a year from FY2037, growing with stage 2; re-timing the capital (`DEC-2026-11-09-09`) moves about $18 billion of outlays into FY2032-38, and takes about $5 billion off FY2039, $8.6 billion off FY2040, $7 billion off FY2041 and $3 billion off FY2042; stage 2's wider entry (`DEC-2026-11-09-12`) adds about $1 billion in FY2037, $7 billion in FY2038 and $8 billion a year from FY2039. The wider services backstop and the testing money end before FY2036 and do not touch these years.

**What this means.**
1. **Housing's new permanent claims are not yet financed in FY2040.** Stage 3, the standing fund, stage 2 at its true timing and its wider entry, option D's credits and the duty to house add about $24 billion a year at maturity to what the model carries. FY2040 is the one year with no margin to absorb it. From FY2041 the adopted architecture's margin covers housing's central costs, and its high case from about FY2043. **Espen decided** that the gap goes to the financing settlement and that housing is not trimmed yet (`DEC-2026-11-09-09`), so question 1's fallback, a slower stage 3, is not used.
2. **The capital tail is mostly gone.** With the last grants and repair money awarded by FY2037 and the last loans committed by FY2038 (`DEC-2026-11-09-09`; section 4, HOU-3C.01, HOU-3C.02, HOU-5.01), about $8 billion of capital still spends in FY2040: about $4 billion from the last 20% of FY2037's grants and repair money and the loans' last disbursements, and about $4 billion from the zoning reward, which pays for finished homes and so cannot be moved earlier, and the social housing pilot's last equity. About $2 billion of the zoning reward falls in FY2041. Espen accepted slight FY2040 overshoots at this stage of design (`DEC-2026-11-09-09`). Ruling that a time-limited line's tail counts as time-limited (question 5's alternative) would remove the rest; it is not needed now.
3. **The guardrails are not at risk from housing.** Before interest, this section's central costs sum to about $0.1 trillion less than the model's through 2035, about $0.07 trillion more through 2045, and about $0.5 trillion more through 2056: about 0.5% of 2056 GDP. The high case is about 2.5% of 2056 GDP more, perhaps three points of debt with interest (this section's arithmetic, rounded, not run). The DEC guardrails pass by 2.8, 11.6 and 23.8 points in 2035, 2045 and 2056, and housing's high case lowers debt through 2035.
4. **The Byrd rule.** R2's permanent housing lines raise deficits after the window. Reconciliation strikes a provision that adds to deficits beyond the resolution's window (`CONVENTIONS.md`, section 5), unless other provisions in its title offset it in those years. So R2 needs the offsets for stage 2, stage 3, the standing fund and the credits in the same bill, or the lines must sunset. This is the per-bill test budget choice 3 asks for, and B3 has not built it (`models/tools/roadmap.md`).

### 3.4 Within the envelope

Housing uses $0.12 trillion of the envelope through C21 and C31, unchanged by this section. Re-timing the capital (`DEC-2026-11-09-09`) keeps those totals and moves their last outlays from FY2040-42 into FY2032-39, inside the envelope years, while the envelope tapers toward zero by 2040; the year-by-year room is the model's check (section 5, item 8). Of the $0.30 trillion left, housing could ask for HOU-8's equity grant and HOU-9A's capital (about $0.014 trillion, time-limited capital). That would lower the general-fund window claim by that much and leave the maturity test unchanged. The emergency fund's start and the vouchers are not investment, so they stay general-fund claims.

## 4. The tax credits: option D

Espen chose option D (`DEC-2026-11-09-08`); section 4 writes it as HOU-2D.01 to .04. The figures are memo 3's research (`memo-3-part1-research.md`; `memos/3-production.md`). None is a JCT score.

| Piece | What it is | FY2030-39 revenue loss | FY2040 |
| --- | --- | --- | --- |
| HOU-2D.01 Low-income credit increase with the deep-income boost | Permanent | About $0.10 trillion ($0.08-0.12; legacy estimate HOU-2B) | About $15 billion (12-22) |
| HOU-2D.01, bond-deal boost for poorest-renter buildings (`DEC-2026-11-09-18`) | Permanent; AHCIA section 308 for bond-financed buildings using the deep-income boost | About $1 billion ($0.4-1.6; memo 3b's step table) | About $0.2 billion (0.1-0.4) |
| HOU-2D.02 Middle-income credit | Tight markets only, 2030-34 awards, a trial with lottery evaluation | About $7 billion, with claims running to about 2048 | About $1 billion |
| HOU-2D.03 Neighborhood homes credit | 2030-34, with evaluation | About $15 billion over five years [EV-HOU-269] [EV-HOU-270] | Small |
| HOU-2D.04 Permanent affordability | A condition on the credits | None directly; lowers credit pricing somewhat | — |
| **Total** | | **About $0.12 trillion ($0.10-0.14)** | **About $16 billion (13-24)** |

The bond-deal boost does not move the rounded totals: it adds about $1 billion to the window ($122 billion to $123 billion; range $102-144 billion) and about $0.2 billion to FY2040 (this section's arithmetic from memo 3b: nine cohorts of awards are being claimed in FY2040, at about $11-45 million a year each). The FY2040 gap stays at about $26.4 billion ($37 billion with the capital tail).

- **After 2040.** The low-income credit is permanent and grows with its claims; the trial credits stop adding cost by about 2048.
- **Against the ledger's $0.15 trillion (HOU-2A):** about −$0.03 trillion.

**The credits' FY2040 cost is the least certain figure in this section.** Each year's low-income credits are claimed over ten years once a building is in service. So a permanent allocation increase keeps building in cost for a decade before it levels off.
- This section spreads the legacy window estimate on a three-year ramp, which gives about $15 billion in FY2040.
- If claims instead build year by year from 2031, the same $0.10 trillion window total implies about $22 billion in FY2040 (this section's arithmetic).
- Neither is a score. The 2025 tax law's 12% increase scored at $15.7 billion over ten years [EV-HOU-261], which shows the scale of one such change. A JCT score of the chosen option is needed before the maturity test can rely on it.

## 5. Changes this section proposes for the ledger and the models (for Espen and the lead; tier 3)

None is made here. Each moves figures, so each is an adopted-input change for its own PR (`models/tools/budget/WORKFLOW.md`, B6).

1. **Replace HOU-1's two components** (`fiscal-components.csv`: the legacy title at $0.47 trillion with 55% continuing, and the voucher increment at $0.09 trillion) with provision-level components or `split` rows, one per line of the table in section 1.2. Each gets its own continuing share:
   - permanent: HOU-4A, HOU-4.07, HOU-4D with the duty to house, HOU-4.08, HOU-1D's standing fund, HOU-2D.01, and HOU-4.12's base backstop (as appropriations after 2039);
   - time-limited: HOU-1D.04, HOU-3C, HOU-5, HOU-6.01, HOU-8, HOU-9A, HOU-4.10, HOU-4.12's wider backstop (FY2030-35), HOU-4.06's testing money (FY2030-34) and HOU-2D.02 and .03 (claims to about 2048).

   The title's single 55% continuation (`ASM-PROF-TIMELIMITED`, `ASM-PROF-COMPONENTS`) mixes one-time and permanent pieces.
2. **Retime HOU-4D** (`housing_extra_tn` in `recovery-adoption.json`, read by the recovery budget with a 2030 start and four-year ramp). Start it in FY2034, rising to the full group in FY2037. Central $0.081 trillion over the window, $22.7 billion in FY2040; with the wider entry (section 2.7), $0.096 trillion and about $30 billion (the duty to house, search help and higher payment standards for the added families are in their own lines).
3. **Fold the fee allowance** (`housing_base_admin_tn`, $0.0122 trillion) into the HOU-4A component, at fees in full plus an issuance fee. Add HOU-4.07's search help as its own line.
4. **Add stage 3 (HOU-4.08)** as a permanent mandatory row from FY2038: central $0.005 trillion over the window and about $14 billion a year from FY2042, outside the $135 billion.
5. **Replace HOU-1A's $0.085 trillion** with HOU-1D:
   - a one-time $0.015 trillion over FY2030-32;
   - a standing fund of $5 billion a year from FY2031, indexed to prices, permanent.
6. **Book HOU-2D** (option D, `DEC-2026-11-09-08`) as its own revenue row: $0.12 trillion over the window, with a claims-based continuing profile, pending JCT.
7. **Splits** (`provision-splits.csv`, empty today):
   - HOU-4.12: mandatory in R2 for FY2030-39, appropriations after;
   - HOU-4.10: mandatory for 2030-34, appropriations if renewed;
   - HOU-6.01: R2 money, with the eligibility rules in the regular bill at no cost.
8. **Capital spend-out, on the re-timed schedules** (`DEC-2026-11-09-09`; section 4). Record budget authority and outlays separately for HOU-3C.01, HOU-3C.02, HOU-5.01 and HOU-6.01: grants awarded FY2030-37 ($72 billion of budget authority, $70 billion of window outlays), loans committed FY2030-38, repair money awarded FY2030-37 ($58 billion and $57 billion), the zoning reward as before ($30 billion and $25 billion). Then rerun the FY2040-42 tests, the high case and the envelope's year-by-year room.
9. **Provision specs** (`provisions.csv`): the housing components' `budget_authority` is `unknown` today. For the rental help lines it would be `outlays`; for the capital lines, provided in full on enactment with spend-out.
10. **Byrd check.** When B3 builds the per-bill window test, run R2's housing title through it (section 3.3, item 4).
11. **Add R1's readiness tranche** (HOU-4.02, item 7) as a FY2029 mandatory row in R1: about $0.75 billion, time-limited.
12. **Add memos 9 and 10** (section 2.8): HOU-10.01 (about $0.028 trillion over the window) and HOU-11.01's grants (about $0.0035 trillion) as time-limited mandatory rows, proposed to borrow inside the D4-B envelope; HOU-10.02 as a permanent credit-subsidy row (about $0.025 trillion, about $3 billion in FY2040), pending CBO's score.
13. **Add memos 11 and 12** (section 2.9): HOU-12.01 (about $0.037 trillion over the window) and HOU-13.04 (about $0.0003 trillion) as time-limited mandatory rows, HOU-12.01 proposed to borrow inside the D4-B envelope; HOU-13.01 (about $0.02 trillion, about $3.1 billion in FY2040), HOU-13.02 and HOU-13.03 (about $0.0034 trillion together, about $0.35 billion in FY2040) as permanent mandatory rows.

The net effect on the headline (central, option D, with the wider entry): about −$0.06 trillion over FY2030-39, about +$24 billion a year in FY2040 for the permanent lines, and about +$32 billion in FY2040 with the capital tail. Memos 9 and 10 (item 12) add about +$0.057 trillion over FY2030-39 and about +$3 billion a year in FY2040 (permanent), about +$3.5 billion with their tails. Memos 11 and 12 (item 13) add about +$0.061 trillion over FY2030-39 and about +$3.5 billion a year in FY2040 (permanent), about +$4.7 billion with the repair fund's tail.

## 6. What is still unpriced

- **The tax credits' JCT score** and their FY2040 run rate (section 4).
- **Memos 9 and 10** (section 2.8): CBO's credit-reform score for FHA's premium cut; the companies' risk on chattel loans; federal land receipts; and any change in the construction loans' subsidy rate for short loans to builders of homes for sale.
- **Memos 11 and 12** (section 2.9): how fast states join the property-tax match and how much relief they already give older owners (the maintenance-of-effort base); contractor capacity for the repair fund, which Pennsylvania's counties found scarce [EV-HOU-655]; and any Medicare or Medicaid savings from the older-adult track, not counted [EV-HOU-687] [EV-HOU-688].
- **Stage 3 for disabled people 62 and over,** and stage 3 without a severe-problems test (section 2.1).
- **Supportive-housing services:** the per-tenant cost and the count of tenants without Medicaid behind the HOU-4.12 placeholder, and the true cost of its extension through 2035 to states that do not cover the services (section 2.3; placeholder).
- **HOU-9A's builder:** capital, operating cost and loan subsidy (placeholder).
- **HOU-4.10's recovery housing:** grants per place (placeholder).
- **Search help's design and cost** (HOU-4.07): the research section 4 still owes.
- **Neighborhood payment limits** (HOU-4.05): their effect on cost per award.
- **Attached awards** (HOU-4.04): whether they cost more or less than tenant-based ones. The register has no evaluation.
- **Rent offsets from other flagships' benefits** (shared rule 1): new income outside the tax code raises tenants' rent and lowers housing's cost by up to 30 cents a dollar. That is the household model's work.
- **The remaining capital tail** (about $8 billion in FY2040), which rests on this section's spend-out judgment, and CBO's subsidy rate for the construction loans.
- **Section 5's items Espen adopted** (`DEC-2026-11-09-10`): the R1 readiness tranche ($0.75 billion) and the testing grants ($100 million a year) are set (`DEC-2026-11-09-14`, `-17`); the cost of deemed approval's payments before checks and the attorney's fees for successful private suits under the 2037 guarantee, the right to return and the Housing First lease protection are unpriced.
- **The duty to house's placement homes,** if they cost more than an average voucher (section 2.5).
- **Tribal need:** what restoring resources sufficient for tribes to care for their people would cost beyond the set-asides (section 2.6; HOU-4.13's 2032 need report).
- **Stage 2's wider entry: its count** (section 2.7) rests on an assumed 1.5-2 students per family and on how long homeless families stay in stage 2. An ACS microdata run would replace the first (`research-doubled-up.md`).
- **Inflow and outflow in stage 2** after 2037. The count is held flat, and the exit rule's effect is unmeasured.

## Questions for Espen

Each is yes or no, and none is adopted until you answer. Questions 1 and 5 are now decided (`DEC-2026-11-09-09`); they stay here so their numbers can be traced. "Housing's FY2040 gap" means the shortfall in the fiscal rule's maturity test in FY2040, on the budget model's adopted architecture.

1. **Should housing's FY2040 gap go to the financing settlement rather than be closed by trimming housing?** On the central figures housing is about $9 billion short in FY2040 counting permanent programs only, or $25 billion with the capital tail. From FY2041 the adopted architecture's margin covers it. The alternative is to slow something in housing: stage 3's enrollment over 2038-41 instead of 2038-40 would save about $3 billion in FY2040 (this section's arithmetic). Recommendation: yes, send it to the settlement, with the slower stage 3 as the fallback. **Decided (`DEC-2026-11-09-09`): yes; housing is not trimmed yet, so the fallback is not used.** On this revision's figures, with stage 2's wider entry, the gap was about $20 billion, or $28 billion with the capital tail (section 3.3); with every addendum it is $26.4 billion and $37 billion.
2. **Does stage 3 include disabled renters 62 and over?** Section 4 implies it does. HUD's worst case needs report (2025) counts disability only under 62. The older group could be as large again, unpriced. Recommendation: decide with the care flagship; until then, price stage 3 for people under 62 and say so.
3. **Should stage 3 use stage 2's test: unassisted, with severe housing problems?** This section assumes yes. Without it, the eligible group is larger and uncounted. Recommendation: yes. Under the design lens (`DEC-2026-11-09-13`) the test should be shown the plain way, by the household's own statement of rent and conditions, checked after award, so it bounds the cost without adding paperwork.
4. **Should the standing emergency fund be a capped yearly amount of about $5 billion, indexed to prices, with a one-time start of about $15 billion in 2030-31?** Both sizes rest on judgment: the Santa Clara trial (Phillips and Sullivan) [EV-HOU-109], the 2021-22 program's start-up record (Congressional Research Service, 2023) [EV-HOU-150], and Eviction Lab's filing counts (2025) [EV-HOU-077]. An open-ended fund that paid every eligible crisis has no reliable cost. Recommendation: yes.
5. **Should the last two years of construction and repair money be awarded earlier, so it is spent by FY2039?** The amounts stay as you decided. Otherwise about $16 billion of capital spending falls in FY2040, the first year the rule tests, after the borrowing envelope closes. Recommendation: yes. **Decided (`DEC-2026-11-09-09`): yes; the last capital is awarded so it is spent by 2039, and slight FY2040 overshoots are acceptable at this stage.** Section 4 moves the grants' and repair money's last awards to FY2037 and the loans' last commitments to FY2038; about $8 billion of capital still spends in FY2040 (section 3.3).
6. **Does the zoning reward (HOU-6.01) end with the FY2030-39 money?** Section 4 removes the Innovation Fund's 2033 end date but sets no money after 2039. Continuing at the same scale would be about $3 billion a year at maturity. Recommendation: yes, it ends unless renewed on its results.
7. **Should the central estimate for stage 2 assume 85% of eligible families apply, rather than memo 2's full sign-up?** The rule's tests use the central figure. Full sign-up is the high case: about $142 billion through 2039 rather than $81 billion. No evidence on take-up of a housing right is in the register. Recommendation: yes, with full sign-up reported as the cautious reading (budget choice 2).
8. **Should "fees in full" mean HUD's unprorated rate?** HUD now pays agencies 85% of their fees (HUD's 2026 fee notice) [EV-HOU-343]. The unprorated rate costs about $2.5 billion more over the window than the legacy allowance. Recommendation: yes.

9. **The parameters memos 9 and 10 left open** (`DEC-2026-11-09-19`, `-20`; section 4, HOU-10 and HOU-11), **decided by Espen, November 9, 2026** ("yes to all four as recommended", and counseling as point 5; `DEC-2026-11-09-24`):
   - *Down payment help's income limit:* 140% of area median income, and 160% in high-cost areas (places where FHA's loan limit is above its floor). The 160% is above the 135-150% range you named; 150% keeps every limit inside it. 140% is the limit the plan's neighborhood homes credit already uses for buyers, so the two buyer programs share one number. 135% or 150% would move the cost not at all (the money is a fixed yearly amount) but would change how quickly it runs out and how many buyers are drawn in who could not otherwise buy.
   - *FHA's safety line:* the cut holds while the insurance fund's capital ratio stays at or above 3%, one point above the legal 2%; it was 11.47% in fiscal 2025 (HUD, 2025) [EV-HOU-552].
   - *Counseling for down payment help:* offered free to every buyer, not required by federal rule, since a required course adds a step before closing and the evidence ties lower default to the agency's whole package (Hembre, Moulton and Record, 2021) [EV-HOU-537]. **Decided by Espen** (November 9, 2026): "yes unless 'counseling' just means a part of the normal loan process, which might be the case"; counseling that is part of an agency's or lender's normal process stays.
   - *Manufactured-home community grants:* $350 million a year for FY2030-39 (FY2039 later lowered to $150 million for the FY2029 bridge, `DEC-2026-11-10-01`).
   - *Federal land proceeds:* up to half for water, sewer and roads for the new homes, the rest to the Treasury.

10. **The amounts memos 11 and 12 left open** (`DEC-2026-11-09-21`, `-22`; section 4, HOU-12 and HOU-13), **decided by Espen, November 9, 2026, as proposed** ("yes to all six as recommended"; the 3% floor kept: "keep 3%"; `DEC-2026-11-09-25`):
   - *The repair fund's size:* $2 billion in FY2030, then $4 billion a year to FY2039 (FY2039 later lowered to $3.7 billion for the FY2029 bridge, `DEC-2026-11-10-01`), about $38 billion, the middle of memo 11's range. More reaches more of the need (lower-income owners alone need about $74.6 billion of repairs [EV-HOU-602]) but runs into contractor shortages.
   - *Per-home limits:* up to $25,000 a home, plus $15,000 for lead or accessibility work; for landlords, up to $25,000 a unit for owners of up to 20 units.
   - *Tribal share of the repair fund:* 5%, as for the construction grants (HOU-4.13).
   - *Relocation help:* moving costs and up to three months' rent where a city orders tenants out of an unsafe home.
   - *The property-tax match:* half of state relief above 3% of income, from FY2031, only above each state's 2028 effort. The 3% floor is below the 4-6% memo 12 gave as an example; a 5% floor would cut the match's cost by roughly a third (judgment) and leave states free to start relief lower on their own money. A lower threshold or a higher match rate costs more and adds to the FY2040 gap; dropping the maintenance-of-effort rule lets states swap federal money for their own.
   - *Legal help:* $200 million a year. *Service coordinators:* $150 million a year more. *Home sharing:* $30 million a year, FY2031-39.

11. **Funding the ROAD to Housing Act** (section 2.10; `road-funding.md`). **Decided by Espen, November 10, 2026: "yes to all four as recommended"** (`DEC-2026-11-10-01`), including option A for the bridge:
   - *The "total" rule:* HOU-6.01, HOU-12.01 and HOU-11.01 are total program levels that include any ROAD money Congress appropriates first, so a 2027-28 win lowers the plan's cost rather than adding to it. Recommendation: yes.
   - *The FY2029 bridge:* about $0.87 billion in FY2029 appropriations for the Innovation Fund and its small grants, the repair pilot, PRICE and RESIDE, counted inside HOU-6.01, HOU-12.01, HOU-11.01 and HOU-3C.01 (option A: about +$0.4 billion over FY2030-39 as spending moves earlier, and about −$0.4 billion of FY2040-42 tails), not added on top (option B: about +$0.8 billion over FY2030-39). Recommendation: A. Neither moves the permanent-line FY2040 gap. A yes to A lowers HOU-12.01's decided FY2039 amount to $3.7 billion and HOU-11.01's to $150 million, so it amends `DEC-2026-11-09-25` and `-24` and needs its own `DEC-` entry (tier 3).

12. **The rural channel's amounts** (memo 13; section 2.11; section 4, HOU-14). **Decided by Espen, November 10, 2026, as recommended** (`DEC-2026-11-10-02`): Rural Development rebuilt to about 5,000 staff (about $0.4 billion a year); direct Section 502 loans grown about six-fold and opened to 100% of area median income, guaranteed loans to 140% and 160%; about a sixth of the repair fund through USDA, with no new money; a $0.5 billion a year preservation fund with rent help after every mortgage; self-help at about $100 million and farmworker housing at about $200 million a year; one rural test up to 35,000 people, "carefully implemented to improve systems and delivery without leaving people behind". The sixth and the yearly paths are this section's judgment.

## Evidence still needed

- A JCT score of option D's credits (HOU-2D).
- A count of tribal homes needing repair or replacement, to size HOU-4.13's set-asides from need.
- The number of extremely low-income renters with disabilities, by age, from the American Housing Survey or the American Community Survey (HUD tabulation or a custom run).
- Per-tenant service costs in supportive housing, and the share of tenants without Medicaid (research note's gap).
- HUD's housing agency fee rates in dollars and the national proration history, to settle the fee rate.
- Take-up of an entitlement to rental help: France's housing allowance [EV-HOU-156] is the nearest case in the register, but it is not a take-up estimate.
- CBO's credit subsidy rate for HUD-FFB risk-share lending.
- The year-by-year spend-out of HUD capital grants (HOME, the Capital Fund) from CBO's account-level projections, to replace this section's judgment.
