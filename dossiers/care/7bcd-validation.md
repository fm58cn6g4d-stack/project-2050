# Care you can count on, parts B-D (long-term care, child care and pre-K, the care workforce): validation

Role: section 7 of the care dossier for parts B, C and D: how the cost in sections 4-6 compares with outside estimates, what the arithmetic misses, who the design reaches and what households pay, the strongest objections, and the signs of failure. Status: draft (stage D, board row D-9, PR 2), on `DEC-2026-11-11-02` to `-06`. Figures marked "project arithmetic" come from `tools/care_repricing.py` and `tools/care_bcd_path.py`; there is no exploratory model for parts B-D, as health has, so every comparison here is between working assumptions and outside figures, not a model run.

## 1. Against outside figures

| Check | Our figure | Outside figure | Reading |
| --- | --- | --- | --- |
| The home benefit (memo 6 B) in 2035, first full year | About $300 billion (range $130-655 billion), before options 2 and 4 | **Urban Institute, 2020** (Favreault), home care for everyone at two activities, no cost sharing, up to $150 a day: $355 billion higher in 2020 for 10.0 million people averaging $40,900, which the author calls "highly speculative" [EV-CAR-483]; adjusted to this design and the three-activity line, about $390-560 billion (3b) | **Below Urban.** Three design choices account for most of the gap: set tier budgets rather than a daily cap, memo 4 C's capped copays, and slower take-up in the first year. If Urban is closer, the benefit costs about $560 billion in 2035, which is why the range runs high (section 6, part 6) |
| The same | About $300 billion | **CBO, December 2020**, option 5 against option 4: all long-term care from one limitation, no cost sharing, federal subsidies $599 billion higher in 2030, about two-fifths replacing state and out-of-pocket spending [EV-CAR-452] [EV-CAR-453]; adjusted, about $280-320 billion (3b) | **Inside the range.** CBO's design is broader (one limitation) and includes institutions, which the adjustment removes; an illustrative option, not a bill score |
| Catastrophic insurance for comparison (memo 6 C, not chosen) | — | **The WISH Act's actuaries**: a 65-and-over cash benefit after a one-to-five-year wait at a 1.7-2.2% payroll tax over 75 years (Milliman for ASPE, 2025; Oliver Wyman, GCG and ARC, 2026) [EV-CAR-454] [EV-CAR-455], reported as about $200 billion at 1.7% [EV-CAR-456] | **The chosen design costs more**, as expected: it covers all ages and the front end, with no waiting period. The actuaries' figure is a floor for any universal insurance, not a check on this one |
| The bridge (point 1) | About $122 billion over FY2030-35 (6 points in FY2030-31, up to 10 from FY2032) | **Build Back Better's** 6-point home care match increase with conditions: about $150 billion over ten years (CBO, as KFF reports it) [EV-CAR-447] | **Consistent.** Scaled to 10 points and the 2030s, about $35 billion a year, against the bridge's $14-15 billion in FY2030-31 and $27-30 billion in FY2032-34; the bridge is temporary and partly paid for progress |
| Child care and pre-K at maturity | About $145 billion a year at the original shares (10 B plus 11 A); $131 billion at the decided shares (child care $74 billion, pre-K $57 billion, 2033) | **CBO on Build Back Better** (via CRFB): $381 billion over six years for the pair, $752 billion over ten if permanent, with a third or more of children in states that would not take part [EV-CAR-587]; **Penn Wharton**, the same scale [EV-CAR-588]; scaled to full participation and 2030s prices, about $150-200 billion a year (3c) | **At or below the bottom of the range**, mainly because families above 85% of state median income pay copays and rates are at today's wages. With early educators' parity (about $53 billion in FY2040) the pair is about $229 billion in FY2040, inside the range |
| The same | — | **The National Academies**: at least $140 billion a year from all sources in 2018 dollars for a high-quality birth-to-five system, public money up by as much as $53 billion a year [EV-CAR-567] | **Comparable in gross cost**, grown to the 2030s and with parity; this design's federal cost is higher because it makes care free for most families |
| The same | — | **PERI** on the Child Care for Working Families Act: about $60 billion a year, method not given [EV-CAR-591] | **Not relied on**: low against CBO's scores of similar designs |
| The wage floor, home care | About $39 billion in home care in 2035, plus $2-4 billion in nursing homes | **LeadingAge**: $9.4 billion in 2022 to lift all direct care workers to a living wage [EV-CAR-626]; about $19 billion grown to 2035 on today's workforce, about $33 billion on the larger 2035 base | **Order of magnitude only.** LeadingAge's figure covers all direct care (private pay included) at its own wage level, not $20 |
| Nursing home staffing | About $5-7 billion a year from 2035; $0.04 trillion over FY2030-39 | **CMS** (Biden administration): $43.0 billion over ten years for the 2024 standards [EV-CAR-601]; the **repeal** (second Trump administration): $55.1 billion [EV-CAR-603], shown as that administration's view | **Below CMS's ten-year figure**, because memo 16 C phases the total in by 2035 and sets no aide minimum; from 2035 the yearly cost is about CMS's average |
| Early educators' parity | About $53 billion in FY2040 at the child care share; $0.26 trillion over FY2030-39 on fiscal years | No independent model in the register (3d, "Evidence still needed") | **Unchecked.** Part C's judgment; section 6 corrected the path. An outside estimate is the most useful missing check |

**What the benchmarks do not test.** None is an estimate of this design. Each is adjusted by project arithmetic, and the two long-term care models differ by about a factor of two. The comparisons show the central figures are in the outside range, not that they are right. Take-up of a universal home benefit and of free child care are the two numbers no US experience pins down.

## 2. What the arithmetic misses

| Missing | Direction | Size or note | What would answer it |
| --- | --- | --- | --- |
| Behavior of families now caring unpaid | Higher cost if more families shift to paid care | Cash and Counseling found paid hours rose when relatives could be paid, but total care hours did not [EV-CAR-486]; the new-user line includes it only through its range | The national evaluation (HLT-4.06); the first years' claims |
| Supply limits | Lower cost early, longer waits | CBO assumed supply would meet the added demand [EV-CAR-452]; if hiring falls short, spending is lower and waits longer. About 2.8 million recruits for long-term care on the three-activity line (range 0.9-8.8 million) (3d) | Workforce counts (HLT-10.05) |
| Room and board shifting | Higher cost | Nursing homes could move costs into room and board; the rate rule (HLT-9.08) is the guard | Cost reports by payer |
| Mothers' employment and taxes | Lower net cost | Not counted, as in CBO's scores; Quebec's evidence puts the long-run recapture at 75-117% [EV-CAR-534], Norway's much less [EV-CAR-544] | The evaluation (FAM-2.11) |
| Turnover, public assistance, quality | Lower net cost | About half of direct care workers rely on public assistance [EV-CAR-613]; not counted | Workforce counts |
| The population over 85 | Higher cost after 2040 | Nearly doubles by 2040 [EV-CAR-403]; inside the 5.5% growth, but costs keep rising past FY2040 | — |
| Fraud in personal care | Higher cost | Personal care cases were 38% of Medicaid fraud units' indictments in FY2012-15 [EV-CAR-463]; fiscal agents' payroll records are the check | Fiscal agents' audits |
| Households' cost by income | — | No household model covers care (below) | A care module in the household model |

## 3. How it lands with the rest of the plan

- **Health.** The benefit starts on health's endpoint, so people move once; Medicaid long-term care stays in Medicaid until then, as health's booking assumes (D-4c). Health's FY2040 net cost is $4,243 billion as booked (`6-cost.md`, part 5); parts B-D add about $580 billion net of what is already booked (`6bcd-cost.md`, part 5).
- **The plan-wide balance.** About $3,750 billion short in FY2040 as booked; about $4,243-4,403 billion short with parts B-D. The financing settlement balances it (`DEC-2026-11-10-05`); after `DEC-2026-11-11-07` that settlement is Claude's to design.
- **Housing.** HOU-4.12's tenancy services and HOU-12.04's CAPABLE visits move to care on schedule (section 4, "The seams with housing"); housing ignores child care's value in rent (`DEC-2026-11-10-03`), so the guarantee adds no counted income.
- **The secure floor.** Paid leave (FAM-3) shortens the months infants need care; the child care cap is a phase-out to stack with the floor's (shared rule 2); the floor owns SSI's own asset limit and any caregiver credit in Social Security.
- **Education.** Pre-K's hiring peak (2031-33) needs EDU-4's pipeline; the EDU-9B fund now carries child care's legacy row in the budget model, which a booking must reconcile (`6bcd-cost.md`, part 5, item 5).

## 4. Reach: for whom

**Who it reaches, at full scale (central; 3b, 3c).**
- *Long-term care:* about 12 million people using home care in 2037 (today's 7.8 million Medicaid users [EV-CAR-407] [EV-CAR-408] and about 3.9 million new users), of every age; nursing-home residents' care part paid without an asset test. People at two activities whose state does not use the Medicaid option are not reached.
- *Child care:* every child under 5 whose family wants paid care, about 4.5 million full-time equivalents under 3 (range 3.5-6.0 million) and wraparound care for about 3.1 million; free for families at or below 85% of state median income, about half of families with young children (memo 12's judgment).
- *Pre-K:* about 5.2 million 3- and 4-year-olds.
- *Workers:* most home care aides (the 2024 median is $16.77 an hour [EV-CAR-613]) and child care staff (median $16.82 [EV-CAR-516]) get a raise to the floor.

**Household cost by income.** No household model in `models/` covers care: `models/tools/incidence-model.py` spreads the legacy FAM-2 and HLT-4 rows over income quintiles with fixed keys and has no copay or income-line logic, and the child poverty model applies the legacy 75% line, not the decided 85% (`models/tools/child-poverty/model.py`). So this section shows two things: the incidence model's keys applied to the decided cost, and the decided rules applied to typical cases.

*The decided cost on the incidence model's keys, FY2040, per household per year* (project arithmetic: 140 million households, a fifth in each quintile; the keys are the legacy model's judgment):

| Income quintile | Child care, pre-K and early educators' pay (key `childcare`: 28/30/24/13/5%) | Long-term care and its workforce (key `medicaid_ltc`: 50/25/14/7/4%) |
| --- | --- | --- |
| Lowest fifth | about $2,290 | about $8,930 |
| Second | about $2,450 | about $4,460 |
| Middle | about $1,960 | about $2,500 |
| Fourth | about $1,060 | about $1,250 |
| Top fifth | about $410 | about $710 |

- These are averages over all households in each fifth, not over users. The long-term care key is Medicaid's distribution; a benefit with no asset test reaches higher quintiles more than Medicaid does, so it understates the middle and upper fifths' share. Who pays the taxes is the settlement's (D3).

*The decided rules on typical cases* (project arithmetic on the cited prices):
- **A family with one toddler** in a market where full-time care costs the national average, $13,184 in 2025 (Child Care Aware) [EV-CAR-515]: at or below 85% of state median income it pays nothing; at 120% it pays at most about 3.8% of income (the straight line from 0% at 85% to 7% at 150%, FAM-2.01); at 150% or above, at most 7% of income. A family paying the full price today at 150% of median income pays less under the cap wherever 7% of its income is below the price.
- **An older adult needing help at home** with three activities: no asset test and no estate recovery; the plan's copays only above 200% of poverty, capped at $1,000 a year (HLT-7.06), against a lifetime average of $137,800 in paid long-term care, almost 59% of it paid out of pocket today, with almost two in ten spending at least $100,000 (ASPE) [EV-CAR-401].
- **A nursing-home resident** at $114,975 a year (CareScout, 2025) [EV-CAR-437]: the plan pays the care part (60-70%, judgment); the resident pays room and board (about $34,000-46,000) from income, keeping the protected allowance, and up to 20% of the care part from income left after that. If her income does not cover room and board, Medicaid pays the rest, income-tested only, with no savings test (HLT-4.08, memo 8 C), so from 2035 savings and the home are never spent down; a spouse at home keeps the income they need. (In 2030-34, before the benefit, Medicaid's savings limit rises to $10,000, HLT-4.04.)

**Who gains first.**
- From January 2030: Medicaid home care workers (the floor); people facing estate recovery or the $2,000 asset limit; states taking the bridge.
- From the 2030-31 school year: families at or below 85% of state median income; 4-year-olds; child care staff (the floor).
- From 2031: nursing-home residents (registered nurse staffing).
- From July 2032: every family with a child under 5 (the 7% cap).
- From January 2035: everyone needing long-term care, phased by need to 2037.

**Outcomes it serves:**
- **OUT-03** (care people can count on): long-term care without spend-down; child care and pre-K for every child; care workers paid enough to stay.
- **OUT-02** (planning beyond the next paycheck): the end of the long-term care spend-down from 2035 (no asset test for the benefit or for room-and-board help) and of most child care bills.
- **OUT-08** (time and practical freedom): family caregivers' respite and pay; parents' time to work.
- **OUT-01** (child poverty): free care for families below 85% of state median income.

## 5. Objections answered

**"After Medicare for All, the country can't afford this too."** Parts B-D add about $580 billion in FY2040 net of what the budget model already books, about 1.1% of GDP, on top of health's shift from premiums to taxes. Much of it replaces what families now pay out of pocket for long-term care and child care, or give in unpaid care [EV-CAR-401] [EV-CAR-436] [EV-CAR-514]. The cost was cut about a fifth after Espen's direction (memo 17), with every protection kept. Whether it is affordable is the financing settlement's test, plan-wide; the dossier reports it honestly rather than trimming it (`DEC-2026-11-10-05`).

**"CLASS failed; long-term care insurance always does."** CLASS was voluntary and premium-funded, and was repealed in 2013 [EV-CAR-476]; this benefit is universal and part of the single plan, as in Germany, Japan and the Netherlands (3b).

**"Paying relatives invites fraud and pays for what families did for free."** Self-direction with paid relatives is already allowed in 44 states in at least one waiver [EV-CAR-439], in red and blue states [EV-CAR-493]; memo 9 E keeps today's state rules, adds a national evaluation before any national right, and pays through public fiscal agents whose payroll records are the check on fraud [EV-CAR-463].

**"Free care at home will flood the system."** The line is three activities, the strictest of the common lines (WA Cares uses it [EV-CAR-497]); new users are phased in over 2035-36; budgets are set by tier. Woodwork demand is the cost risk the range carries.

**"Paying for child care for parents who don't work."** Most families with young children have every parent at work [EV-CAR-518]; an activity test mainly catches job-seekers and students, and costs paperwork when jobs change.

**"Federal wage mandates kill jobs."** The floor is a condition on public money that pays the floor's added cost in its rates, so providers are not left to absorb it; pay is the lever with the best evidence on retention [EV-CAR-624] [EV-CAR-625].

**"States will just decline."** A state that declines child care or pre-K still owes its share, and HHS runs the program there; declining saves it nothing. The instrument is untested in court, which section 8 names.

## 6. Signs of failure

Published counts, each with what it would trigger (none is a gate; `DEC-2026-11-09-13`):
- New users in 2035-36 run well above 5.6 million or below 2.8 million (the range): revisit the tier amounts (HLT-9.03) or the phase-in (section 8).
- Time from request to services rises after 2035 in the access reports (HLT-4.05): a supply shortfall; part D's floor or training first.
- Home care turnover does not fall after the floor (HLT-10.05): the floor's level or design (memo 14's trigger).
- Room-and-board charges rise faster than costs in cost reports: tighten the rate rule.
- Child care slots for infants fall where pre-K grows (New York City's pattern [EV-CAR-569]): speed the salary scale or the operating grants.
- A pre-registered pre-K evaluation shows Tennessee-like results [EV-CAR-559]: curriculum and coaching standards (FAM-2.02), not the program's existence.
- States challenge their payments in court: the hold-harmless and its cost (section 6, part 6).
- Nursing homes claim shortage-area exemptions in large numbers after 2031: slow the total's phase-in (memo 16's trigger).
