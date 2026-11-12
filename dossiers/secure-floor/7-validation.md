# A secure floor for every household: validation

Role: section 7 of the secure floor dossier: how the costs and results in sections 4-6 compare with outside estimates, what the models and arithmetic miss, who the decided set reaches and what households pay, how it lands with the rest of the plan, the strongest objections, and the signs of failure. Status: reviewed (L2, milestone review `review-milestone.md`, #298; L3 after its fix steps and re-check), on `DEC-2026-11-12-06`. Figures marked "project arithmetic" come from `tools/afa_floor.py`, `tools/secure_floor_path.py` and the legacy child-poverty model re-run in `6-cost.md`, part 3. Outcomes served: OUT-01 (child poverty), OUT-02 (planning beyond the next paycheck), OUT-06 (paid leave access), OUT-08 (time), OUT-11 (the fairness and fiscal tests).

## 1. Against outside figures

| Line | This dossier | Outside figure | Reading |
| --- | --- | --- | --- |
| The child benefit (FAM-1) | About $1.85 trillion over FY2030-39 (range $1.65-2.05), $209 billion in FY2040 | Tax Policy Center, about $1.4 trillion over FY2026-35 against current law [EV-SEC-266], about $1.6-1.7 trillion moved to FY2030-39 (memo 1); PolicyEngine, $2.5 trillion over 2025-34 against a baseline in which the 2017 credit expired [EV-SEC-267]; CBO via the Peterson Foundation, $1.6 trillion over 2022-31 for a permanent 2021 credit [EV-SEC-607]; this dossier's CPS check, about $1.45-1.5 trillion at full take-up with no behavior (`6-cost.md`, part 1) | Within the outside range, toward its upper middle. The difference from the CPS check is the newborn month, reach from records (memo 2) and the file's undercount of income; the booking is not trimmed. A JCT or Treasury score would settle it |
| The floor's value | About $4-6 billion a year | None published | Project arithmetic only; the bill's own text sets the phase-out exactly [EV-SEC-263] |
| The childless earned income credit (INC-1.01) | About $0.145 trillion over FY2030-39 | JCT $135 billion over FY2022-31 [EV-SEC-609]; TPC $135.4 billion over FY2025-34 [EV-SEC-610] | Grown at about 2% a year to the 2030s window; on fiscal years the first year moves out of the window |
| SNAP restored (INC-2.01) | About $0.23 trillion | CBO, almost $187 billion of savings over FY2025-34 for the nutrition subtitle [EV-SEC-035] | The 2030s window has every cut in force; immigrant eligibility (sec. 10108) is inside that figure, counted here and not by immigration |
| SSI's limits (INC-3.01) | About $0.013 trillion | SSA's actuaries, $8.9 billion over 2025-34 [EV-SEC-630] | Grown into the later window |
| Paid leave (FAM-3) | $1.38 trillion of benefits, booked at high take-up | Urban, about 0.46% of taxable earnings for the progressive FAMILY Act [EV-SEC-660]; CBO and JCT $547 billion for the 2019 bill [EV-SEC-344] | The booking is the high case, the one the 1.10% ceiling is built for; the outside figures sit at the legacy range's low and middle |
| Social Security (the 2030 act) | About +3.6 to +3.8% of payroll before the fallback, against a 4.42% gap; at or near balance only with SS-7.01's one point used in full (`6-cost.md`, part 4) | SSA's 2026 single-provision scores for each piece [EV-SEC-447] [EV-SEC-450] [EV-SEC-452] [EV-SEC-445] [EV-SEC-455] | Each piece but SS-8 matches SSA's score; SS-8 is project arithmetic at its 20% share, well below the legacy estimate [EV-SEC-697]; no package score exists [EV-SEC-477] |
| Child poverty | About 9% (range 8-12%) on the 2029 baseline | Columbia's Center on Poverty and Social Policy, the American Family Act alone, 13.3% to 8.8% for 2024 [EV-SEC-268]; the legacy model, 8.73% to 8.09% on 2025 incomes [EV-SEC-692] | Consistent; the outside figure has no housing awards and no 2029 baseline either |

## 2. What the models and arithmetic miss

- **No 2029 current-law baseline.** The child-poverty model is a static model on 2025 incomes (`legacy-research.md`, 0). The 2029 rate is a working assumption (`6-cost.md`, part 3). *Studied with the household model* (`MOD-household`), which must recompute income, taxes and transfers together.
- **No identification branch.** Coverage is a scalar. The decided rule (FAM-1.04) removes the parent test, so the scalar is now the right shape (it stands for delivery, not legal exclusion), but a branch would show who the remaining gaps are.
- **No employment response** in the poverty model; the contested range is applied by hand (`6-cost.md`, part 3).
- **Monthly payment behavior.** The model uses annual exposure; the bill is monthly, with a newborn month and a choice of income years. Timing matters to who is poor in a given year, not to the cost.
- **The phase-out's arithmetic is static.** The floor's value assumes 1% real income growth; it is small either way (`6-cost.md`, part 7).
- **Paid leave's take-up** is a range of legacy cases, not a model of who claims; the household model's D3 test still uses 0.6% and $0.9 trillion (`legacy-research.md`, 3.2).
- **Social Security's package** has no SSA score; the investment's return and its budget treatment are open (`6-cost.md`, part 4).
- **The 65-cent ceiling** is checked by hand on statutory rates (memo 7); the household model's distribution is still to come.

## 3. How it lands with the rest of the plan

- **Housing.** The floor's non-wage payments never raise rent (INC-5.01), so housing's 0-30 cent range narrows to 0 for them; vouchers and the decided child benefit stack without offset. Rent still counts paid leave as wages.
- **Care.** Child care is free at or below 85% of state median income (`DEC-2026-11-11-03`), so the refundable dependent care credit (INC-4.01) pays copays and the care the guarantee does not reach; LAB-10's child care fills only the hours the guarantee misses. The caregiver credit (SS-B4.01) tops up actual earnings and never credits paid care twice. The single plan (`DEC-2026-11-10-09`) ends the premium-credit layer in 2035, which is what brings the single parent under 65 cents.
- **Immigration.** Rule 3 is immigration's (`DEC-2026-11-12-07`): the child's own ID, SNAP's pre-2025 rules, one data firewall that FAM-1.08 honors.
- **Clean power.** The Climate Dividend can join the child benefit's rail (FAM-1.09, proposed).
- **Housing, transportation, clean power.** Apprentice hours on plan-funded construction (LAB-10.05, proposed) give LAB-10's trainees jobs at the end.
- **Financing.** About $0.47 trillion over FY2030-39 and $56 billion in FY2040 more than booked, about 1.3% of the plan-wide FY2040 gap (`6-cost.md`, part 5).
- **Fairness test (D3).** The child benefit's distribution changes: the incidence key (`ctc`) still gives the top quintile 4%, but the decided design pays about 5.4 million families above about $210,000 less than the 2029 law. A booking should update F1's key (`6-cost.md`, part 6).

## 4. Reach: for whom

Illustrative households (2025 dollars for the child benefit, as memo 1; project arithmetic):

| Household | Today (2029 law) | Under the decided set |
| --- | --- | --- |
| Single mother, children 3 and 8, earning $14,000 | About $1,725 a year of child credit [EV-SEC-006] | $660 a month ($7,920 a year) of child benefit [EV-SEC-262]; SNAP without the 2025 cuts; free child care (care) |
| Married couple, two children 6 and up, earning $70,000 | $4,400 a year | $600 a month ($7,200 a year) |
| Married couple, two children 6 and up, earning $250,000 in 2030 | About $5,000 a year (2030 dollars) | About $4,660 a year (2030 dollars): about $340 less, the bill's phase-out, no floor |
| A 22-year-old warehouse worker earning $15,000, no children | Nothing: the credit starts at 25 [EV-SEC-027] | About $1,000 of earned income credit (memo 3) |
| A home health aide earning $2,400 a month, after a birth | No paid leave | About $1,850 a month for twelve weeks, and her job back [EV-SEC-340] |
| A disabled woman on SSI saving for a car | Loses SSI above $2,000 [EV-SEC-042] | Can save up to $10,000 |
| A worker at $60,000 | — | Pays $180 a year for paid leave at 0.6%, up to $330 at the ceiling [EV-SEC-676] |
| A retiring couple in 2033 | A cut of about $16,900 a year if the fund is depleted [EV-SEC-406] | Full benefits on time (SS-11.01) |

**Who the decided child benefit reaches.** Every child with an identification number below about $180,000 (couples) gets the full amount, about 87% of children in the CPS file get at least the 2029 law's credit (project arithmetic: 8.8 million of 67.9 million get less), and the poorest children gain most: in the legacy model, children in deep poverty today get about $527 of credit on average [EV-SEC-675], and every one of them gets the full benefit.

**Who still misses out.** Children without any number (the decided rule does not reach them); families who do not confirm a notice and do not file (reached later by front doors); children in the poorest families with no earner, who remain the largest share of poor children in the legacy model (`legacy-research.md`, 1.6).

## 5. Objections answered

| Objection | Answer |
| --- | --- |
| "It costs too much." | It is the plan's largest family commitment, about $1.85 trillion over ten years, and it is reported, not hidden: the whole floor's net change a booking would make is about 1.3% of the plan-wide FY2040 gap, and the child benefit itself costs slightly less than is already booked (`6-cost.md`, parts 1 and 5). The cheaper design that reaches the poorest children (memo 1 B) was weighed and not chosen; it would add a phase-out where the stack is steepest |
| "Paying parents who don't work will reduce work." | Studies of the 2021 payments find no employment effect (Ananat and others) [EV-SEC-212]; simulations predict 367,000 to 1.5 million parents leaving work (Bastian; Corinth and others) [EV-SEC-219] [EV-SEC-218]. Even the largest leaves child poverty about a fifth lower. Removing an earnings test in California caused very few mothers to leave work [EV-SEC-224] |
| "Why do families earning $250,000 get less than today?" | Espen chose the bill's own phase-out, so the benefit is for working and middle-class families. A couple at $250,000 with two children gets about $340 a year less than the 2029 law in 2030; below about $210,000 no couple gets less, and most families get far more |
| "Monthly payments invite fraud and errors." | The child benefit uses records the government holds and one qualifying-child rule (INC-1.02); the earned income credit's errors are mostly over which child qualifies [EV-SEC-258]; the safe harbor keeps honest mistakes by low-income families from becoming debts |
| "Data matching is a privacy risk." | Each match is authorized for named purposes only, logged and counted, and barred from immigration enforcement (FAM-1.08); Canada's enrollment at birth registration works with consent [EV-SEC-113] |
| "Repealing SNAP's work rules rewards idleness." | The 2025 rules remove about 2.4 million people in an average month (CBO) [EV-SEC-036]; Arkansas's Medicaid work rule cut coverage with no gain in employment [EV-CAR-212] |
| "A paid leave tax on every worker." | $180 a year at $60,000 at the start [EV-SEC-676], for twelve weeks of leave and a job back; the bands pay low earners the most |
| "Putting Social Security in the stock market is risky." | Only part of the reserves, in a passive index under an independent board, and benefits never depend on the market. It closes only a small part of the gap on our estimates; the fallback (SS-7.01) is automatic and expected to do more (`6-cost.md`, part 4) |
| "SSA can't handle it." | SSA has lost staff [EV-SEC-066]; paid leave pays for its own administration from the fund, the IRS carries the child benefit's build, and the start moves if SSA cannot staff it, the program does not shrink (`5-delivery.md`, part 7) |

## 6. Signs of failure

Published counts with a review trigger, not gates (`DEC-2026-11-09-13`):
- **Reach:** the share of children on any federal record who are paid the child benefit, by state and by income; below 95% in the first full year triggers a review of the matching and front doors.
- **Accuracy:** the benefit's improper payment rate against the advance credit's 13.6% [EV-SEC-258]; payee disputes and their time to decision.
- **Poverty:** child SPM poverty each September; above 12% in 2032 (the range's top) triggers a review of the benefit's level and reach.
- **The ceiling:** a typical family type above 65 cents for two years triggers a review (INC-5.02).
- **Paid leave:** claims by earnings band; the fund's reserve and loan against the high case (loan above about $182 billion, the booked peak ($185 billion on the fund's own scale), triggers a review of the rate path).
- **Social Security:** each Trustees report's balance after the act; SS-7.01's trigger.
- **LAB-10:** people served, completions and earnings a year later, against the 400,000-900,000 working range.
