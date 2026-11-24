# Memo G13: The backstop without a VAT

**Decided:** A, `DEC-2026-11-24-08`. The backstop text and its figures on the booked package are in `../2-settlement.md` parts 3 and 7.1; the wealth tax's loss there is net of the stack cap ($104.0B and +0.46 points in FY2040, not $139.1B and +0.62). Booked in stage G step 7 (`../2-settlement.md`, `models/data/inputs/settlement.json`). The memo below is the record of the choice as put to Espen; its figures are the draft's.


Role: decision memo for Espen, fork 13 of stage G, from step 4b's whole-budget scan ([`../3-budget-scan.md`](../3-budget-scan.md) part E). Status: **provisional, drafted on the recommendation, November 20, 2026. A redraft that `DEC-2026-11-20-09` asked for.** Not decided, not booked. Nominal $B on case `mixed`, priced by `models/tools/financing-protection/budget_scan.py` on the recommended package (memos G10 to G12 and G14, with the health contribution at 3.85%). Project arithmetic on exploratory models, not official scores.

## The question

You chose memo G5's option B: the plan balances with the national health budget (D2) and the wealth tax (HS2) counted, and enacts a backstop that switches on only if one fails (`DEC-2026-11-20-09`). G5's backstop steps were VAT points. With no VAT (`DEC-2026-11-20-07`), they need another instrument.

If either fails, on the recommended package, the gap would be:

| | FY2040 | FY2056 | In health contribution points, FY2040 / FY2056 |
| --- | --- | --- | --- |
| D2 misses its path | 238.5 | 312.8 | +1.06 / +0.73 |
| The wealth tax is struck down | 139.1 | 73.7 | +0.62 / +0.17 |
| Both | 388.4 | 600.0 | +1.73 / +1.40 |

The later years need fewer points because the package runs a surplus there (about $214B in FY2056, from the defense path), which absorbs part of either loss. On its own, the wealth tax is about $287B in FY2056; the surplus covers most of it.

## The options

| | If D2 misses | If the wealth tax falls | Workers ahead, if both trigger in FY2040 |
| --- | --- | --- | --- |
| **A (recommended)** | The health contribution's base rate steps up, 0.25 points a year, to what closes the overrun (up to about 1.1 points) | Its drafted deferral charge on unrealized gains first; then the contribution's top surcharge tier; the base rate last | about 50% (R about 5.6%); about 56% if D2 alone (R about 4.9%) |
| B | As A | A further defense step, about 12% more below G10's path | as A for D2 |
| C | Named spending cuts: a further defense step and a freeze on nondefense discretionary growth | The same | not run |

**A, health pays for health; the top first, then the base rate (recommended).**
- *D2:* if health spending runs above GDP plus 1 point for two years, the contribution rises. Everyone sees the cost of an overrun in their own contribution. That is the pressure that makes the national health budget hold. It uses the contribution's existing withholding, so nothing new is built.
- *The wealth tax:* the charge on unrealized gains is already drafted as its fallback, and the surcharge falls on high incomes, so the replacement starts at the top.
  - **But be clear about what that buys.** Memo G5 says the deferral charge "mostly reaches the same base" as the mark-to-market tax on billionaires (the ledger's row G11), "so it recovers little". The surcharge tier has little room, with the stack on top wages already at 68-73% (memo G4).
  - **So in practice most of a wealth-tax loss would land on the base rate**, on households above the exemption. The table above prices it that way: +0.62 points in FY2040.
  - B is the option that keeps it off households.
- *Legal footing:* as G5 said, Congress sets the rates, the dates and the trigger, and the trustees find a fact. That is contingent legislation of the kind upheld in *Field v. Clark* (1892) and *J.W. Hampton v. United States* (1928).
- *The cost if it triggers:* with both, the base rate would reach about 5.6%, and about half of workers (50.2%) would come out ahead on health's take-home test.

**B, defense for the wealth tax.**
- It keeps the wealth tax's replacement off households.
- But a further $140B in FY2040 is about 12% more off a defense budget already restructured. That would take defense to about 1.8% of GDP in FY2040, a step G10 doesn't recommend even as a contingency.

**C, cuts for both.** $390B in FY2040 is more than everything the scan found outside health, Social Security and the flagships. Named cuts of that size would reach programs you protected. It is listed so the scale is visible.

## Recommendation

**A.** The health contribution backs up the health budget, and the drafted deferral charge and the top surcharge back up the wealth tax. One instrument for each risk, both already in the plan, each visible to the people it falls on.

**What would change this:** if you'd rather the wealth tax's failure never reach a household's contribution, then B for that part, with its defense cost.

## Question for you

**G13.** Redraft G5's backstop so that, if D2 misses, the health contribution's base rate steps up, and if the wealth tax is struck down, its deferral charge and then the top surcharge tier step in (A, recommended)? Or a defense step for the wealth tax (B), or named cuts for both (C)?
