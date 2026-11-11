# Memo 14: How care workers' pay is set in home care and nursing homes

Role: decision memo for Espen, fork 14 of the care dossier (part D, the care workforce; `../3d-design-workforce.md`). Status: **for Espen, not decided.** Sources are named in plain text; bracketed tags point to the evidence register (`../evidence.json`). Costs marked "judgment" are this dossier's working assumptions, not official scores; their basis is in `../3d-design-workforce.md`, "What the options cost", and `../tools/workforce_demand.py`.

**This memo decides whether, how and at what level the federal government sets the pay of the people who give care that public money pays for at home and in nursing homes.** It covers home health and personal care aides, paid family caregivers, nursing assistants and other direct care staff, under Medicaid in 2030-34 and under the single plan's home care benefit from 2035 (part B, memo 6). Early educators are memo 15; nursing home staffing levels are memo 16.

## The question

- **Today.**
  - *Pay:* about 5.4 million direct care workers earn a median of $17.36 an hour, $16.77 in home care (PHI, 2025) [EV-CAR-613].
  - *Hardship:* nearly half rely on public assistance [EV-CAR-613].
  - *Rates:* Medicaid pays most of the bill [EV-CAR-404], and more than half of reporting states paid personal care agencies less than $20 an hour, out of which the wage comes (KFF survey, 2025) [EV-CAR-627].
- **By 2029.**
  - *The pay rule:* the 2024 rule that 80% of home care payments go to workers' pay starts only in July 2030, and the administration plans to rescind or revise it (CMS, 2024 and 2025) [EV-CAR-419] [EV-CAR-420].
  - *Wage law:* the Labor Department has proposed restoring home care's exemption from minimum wage and overtime (2025) [EV-CAR-616].
  - *Federal standard:* none.
- **Why it matters for the plan.** Parts B and C would need about 3.6 million more paid care workers at maturity, between 1.2 and 9.9 million (project arithmetic, on part B's revised figures; `../1d-problem-workforce.md`, part 5). Their costs assume today's wages. A benefit nobody can be hired to deliver turns into a waiting list.
- **The legacy design.** Federal standards boards for home care (LAB-3, the work flagship's), with a Medicaid pass-through. It is a working choice, weighed here (`DEC-2026-10-30-02`).

## What the evidence says, in five lines

1. **Higher pay keeps workers and improves care.** A ten percent higher minimum wage cut nursing home separations, and would prevent at least 15,000 deaths (Ruffini, Washington Center for Equitable Growth working paper, 2020; quasi-experimental) [EV-CAR-624]. In San Francisco, home care retention rose from 39 to 74 percent after raises (Howes, Industrial Relations, 2005; program evaluation) [EV-CAR-625].
2. **Temporary money buys temporary raises.** Most of ARPA's home care raises were not sustained, except where a legislature wrote them in, as Colorado did, from $12.41 to nearly $18 (MACPAC, 2026) [EV-CAR-628].
3. **A share-of-payment rule has never been tried** (CMS, 2024) [EV-CAR-419]. It controls how a rate is split, not how big it is.
4. **States that set floors fund them in the rate.** Minnesota's nursing home board set $22.50 for nursing assistants once Medicaid approved the rate to pay for it (Minnesota Department of Labor and Industry, 2026) [EV-CAR-618]. Washington bargains with its home care workers as their public employer, at $22.52-23.68 (Washington law; SEIU 775, 2025) [EV-CAR-620] [EV-CAR-621].
5. **No US bill sets a care wage number.** Better Care Better Jobs (2023) and the HCBS Access Act (2026) ask states to pass rate increases through to workers and to cooperate with unions [EV-CAR-617] [EV-CAR-639]. Medicare for All counts wages and bargaining in hospitals' budgets but sets no home care floor [EV-CAR-637].

## Part 1: how pay is set

**A. A pass-through of rate increases, with the 80% share in statute.**
- *What it is:* the Better Care Better Jobs route. The federal government raises its home care match, states must pass increases through to workers at least proportionately [EV-CAR-617], and the 2024 rule's 80% compensation share goes into statute [EV-CAR-419]. No wage number.
- *Where tried:* ARPA's one-year match increase (2021-22) [EV-CAR-425]; the 80% rule, never in force.
- *For workers:* an aide's pay rises when their state raises rates, and not otherwise. In a state paying agencies $18 an hour, 80% is $14.40 for wages, payroll taxes and benefits together.
- *Cost:* about $0-10 billion a year in 2035 beyond what parts B and C already priced (judgment: it moves money only if rates rise).
- *Evidence strength:* program evaluation for the pass-through (modest, temporary effects); none for the 80% share.
- *Political risk:* low among Democrats, who backed these bills. Agencies oppose the 80% share as unworkable for small providers. The rule's own exceptions for small providers concede it [EV-CAR-636].
- *Burden:* agencies report how they spend payments, which states already collect for the 2024 rule.

**B. A federal care wage floor that the payer funds in its rates, with the 80% share as its check, and states free to go higher (recommended).**
- *What it is:*
  - *The floor:* a minimum hourly wage for every worker giving publicly paid home care or nursing home care, set in the 2029 law, indexed to average wages each year and higher where a state or local minimum is higher (part 2 sets the level).
  - *Who pays:* the payer funds it. From 2030 Medicaid rates must cover the floor, with the federal government paying 90% of the added cost. From 2035 the single plan's home care rates include it.
  - *The check:* the 80% share applies as a check that money reaches workers, not as the main tool. States keep the small-provider option [EV-CAR-636].
  - *Above the floor:* states may set higher wages by a standards board (Minnesota) or by bargaining (Washington), and those are allowable costs (point 3).
  - *Family caregivers:* paid relatives get the floor (point 1).
- *Where tried:* Minnesota's nursing home board [EV-CAR-618]; Colorado's legislated base wage [EV-CAR-628]; California's health care minimum wage, which reaches home health agencies and holds free-standing nursing homes out until a spending rule exists (California Department of Industrial Relations) [EV-CAR-619]. Nevada's board recommended a $25 rate and a $15 floor (2022) [EV-CAR-622]. No national program.
- *For workers (illustrative):* at $20 an hour, a full-time aide earns about $41,600 a year, against about $34,900 at today's home care median. A paid daughter caring for her father is paid the same.
- *Cost:* at $20, about $47 billion in 2035 (range $25-95 billion), about $0.35 trillion over FY2030-39 and about $62 billion in FY2040 (judgment; part 2 gives the other levels).
  - *Where it comes from:* about 12% more payroll on about $617 billion of publicly paid home care in 2035 (today's Medicaid home care grown, plus the part of memo 6 B's new money that buys new hours, as part B revised it), plus $2-4 billion in nursing homes.
  - *How it compares:* LeadingAge's model put a living wage for all direct care workers at $9.4 billion in 2022 (LeadingAge LTSS Center, 2020) [EV-CAR-626]. Grown to 2035 and doubled for memo 6 B's added hours, it is the same order of magnitude, though it covers all direct care at a different wage level. CBO's score of Build Back Better's home care money, a match increase with conditions, was about $150 billion over ten years (KFF's report of CBO, 2021) [EV-CAR-447], between A and B.
- *Evidence strength:* quasi-experimental and program evaluation for pay's effect on retention and quality (lines 1 and 4). The floor's design is state practice, not evaluated. The level is judgment.
- *Political risk:*
  - *Cost:* the cost is new federal spending tied to the single plan's financing.
  - *States:* they object to a federal wage condition in Medicaid. The 90% federal payment in the bridge answers the cost, not the principle.
  - *Agencies:* they back a floor only if rates follow; the law writes the rate rule with the floor.
  - *Opponents:* they call it a federal wage mandate. It is a condition on federal money, like Davis-Bacon's prevailing wage on federal construction (not in register).
  - *Legislative route:* it can ride a reconciliation bill, because it sets how federal money is spent.
- *Burden:* providers show payroll at or above the floor from records they already keep (point 4). Workers do nothing.

**C. State-level bargaining in every state, with the state as employer of record.**
- *What it is:*
  - *Bargaining:* every state recognizes a statewide unit of publicly paid home care workers and bargains wages and benefits with it, as Washington does with individual providers [EV-CAR-620]. The federal payer funds the agreements.
  - *Agency workers:* they would need sectoral bargaining across private employers, the legacy LAB-3B, which has no US statutory precedent.
- *Where tried:* Washington since 2001, and its 2025-27 agreement [EV-CAR-621]; California's IHSS county public authorities (not in register).
- *For workers:* the highest wages where unions are strong, and a voice in training and scheduling. In states without a union, nothing until one forms.
- *Cost:* up to about $130-150 billion a year at maturity if wages reached Washington's level everywhere, about 35-40% above today's national home care median, and less where bargaining lags (judgment).
- *Evidence strength:* program evaluation (San Francisco) [EV-CAR-625]; no national test.
- *Political risk:* the highest.
  - *Legal:* the Supreme Court bars requiring agency fees from these workers (Harris v. Quinn, 2014) [EV-CAR-623], so units depend on voluntary membership.
  - *Opponents:* right-to-work groups and most Republican states would fight it.
  - *Legislative route:* it likely needs the labor bill (LAB-1), not reconciliation.
- *Burden:* states run bargaining; workers choose whether to join.

**D. No care-specific floor (current law, with the general minimum wage).**
- *What it is:* care pay follows the general minimum wage, which the work flagship's LAB-4 would raise to $17 and then two-thirds of the median (`legacy/domains/domain-labor.md`), and the market.
- *For workers:* LAB-4's $17 is near today's home care median [EV-CAR-613], so most aides would see little change.
- *Cost:* none here.
- *Political risk:* none new; but parts B and C's benefits then meet the supply limit.

## Part 2: the level, if B

All in 2026 dollars, indexed to average wage growth from 2027, and never below a higher state or local minimum. The medians compared are 2024 and 2025 figures, so wage growth to 2026 narrows each gap a little.

| Level | Against today's medians | Payroll added (judgment) | 2035 ($ billion) | FY2030-39 ($ trillion) | FY2040 ($ billion) |
| --- | --- | --- | --- | --- | --- |
| A. $18 | Just above the 2024 home care median of $16.77 [EV-CAR-613] | about 5% | about 20 | about 0.14 | about 25 |
| **B. $20 (recommended)** | About 19% above the 2024 home care median; about the 2025 nursing assistant median, $42,260 a year [EV-CAR-609] | about 12% (8-18%) | **about 47 (25-95)** | **about 0.35** | **about 62** |
| C. $22.50 | Minnesota's nursing assistant floor [EV-CAR-618]; near Washington's bargained start [EV-CAR-621] | about 25% | about 98 | about 0.72 | about 127 |

- **Why $20.** It lifts most home care workers to about what nursing assistants already earn, so home care stops losing workers to nursing homes and hospitals for the same work.
- **What it costs as a share.** About 12% of home care payroll.
- **Why not C.** $22.50 doubles the cost. It is the level where Minnesota's board and Washington's bargaining landed, in two high-cost states, and the floor already lets states go higher.
- **Under part B's memo 6 A** (stronger Medicaid rather than a new benefit), the base is smaller: B at $20 costs about $22 billion a year in 2035, and states pay about 47% unless the federal government pays the floor's added cost (judgment).

## Consequences at a glance

| | A. Pass-through | **B. Floor funded in rates** | C. Bargaining everywhere | D. No floor |
| --- | --- | --- | --- | --- |
| Is a wage guaranteed? | No | Yes, nationally | Where workers organize | No |
| Typical home care wage, 2035 (2026 dollars) | today's, plus rate increases | at least $20 | $22-24 where bargained | today's, or LAB-4's $17 |
| New federal cost, 2035 | about $0-10 billion | about $47 billion (at $20) | up to about $130-150 billion | 0 |
| FY2040 | about $5-10 billion | about $62 billion | about $170-195 billion | 0 |
| Evidence for the mechanism | Program evaluation, temporary effects | State practice; pay's effect quasi-experimental | One state's program | — |
| Legislative route | Reconciliation | Reconciliation | Likely the labor bill | — |
| Risk to parts B and C's supply | High | Moderate | Uneven by state | Highest |

**Fiscal rule** (`DEC-2026-11-10-05`): the level is mainly about money, so it comes to you. The cost is reported to the financing settlement; nothing is trimmed here.

## Recommendation: part 1 B, part 2 B ($20)

- **It is the only option that guarantees the wage**, and pay is the lever with the strongest evidence [EV-CAR-624] [EV-CAR-625].
- **It fixes the failure of every earlier attempt.** ARPA's money was temporary [EV-CAR-628], and the 2024 rules set duties without paying for them [EV-CAR-601]. Here the floor is permanent and the payer funds it in the same law.
- **It keeps what works in the bills.** The pass-through and the 80% share stay as checks [EV-CAR-617] [EV-CAR-639], and states that bargain or run boards can go higher.
- **It follows the design lens.** One number, indexed, checked from payroll records already kept; nothing asked of workers or families.
- **Evidence strength: moderate.** The effect of pay is well supported. The level is judgment, and the cost range is wide because part B's new-user count is uncertain.

**What would change this:**
- an evaluation of Minnesota's board or a pass-through showing raises without retention gains (toward A);
- the financing settlement cannot carry $20 (part 2 A, with the floor rising later);
- the work flagship adopts LAB-3 boards that cover home care nationally (B's floor stays as the minimum under them).

## If you decide

- **What section 4 writes.**
  - *Under B:* the floor, its index and the rate rule in the 2029 reconciliation bill: in Medicaid from 2030 with 90% federal payment of the added cost, and in the single plan's home care benefit from 2035. Also the 80% share as its check, family caregivers at the floor (point 1) and state standards above it allowable (point 3).
  - *Under A:* the match increase and the share.
  - *Under C:* a bargaining title for the labor bill, proposed to the work flagship.
- **What section 6 prices.** The chosen level on fiscal years, checked against HLT-4's booked care workforce money so nothing is counted twice.
- **Parts B and C.** Their benefits are priced with this line beside them, not inside.
- **The agenda.** HLT-10 (new, `option`, L1) carries B.

## Questions for you

1. How pay is set: A, B (recommended), C or D?
2. Under B, the level: $18, $20 (recommended) or $22.50, in 2026 dollars, indexed?
