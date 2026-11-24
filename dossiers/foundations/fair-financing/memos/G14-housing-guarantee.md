# Memo G14: The housing guarantee

**Decided:** C, `DEC-2026-11-24-09`; booked in step 7, shaped on stage 2's enrollment (−$40.7B over FY2037-39, not −$44.0B). Booked in stage G step 7 (`../2-settlement.md`, `models/data/inputs/settlement.json`). The memo below is the record of the choice as put to Espen; its figures are the draft's.


Role: decision memo for Espen, fork 14 of stage G, from step 4b's whole-budget scan ([`../3-budget-scan.md`](../3-budget-scan.md) part C, item C10). It answers your question of November 20. Status: **provisional, drafted on the recommendation, November 20, 2026. A new fork.** Not decided, not booked. Nominal $B on case `mixed`, priced by `models/tools/financing-protection/budget_scan.py` from the housing dossier's own figures (`dossiers/home/6-cost.md`). Project arithmetic on exploratory models, not official scores.

## The question

You asked on November 20: "it might make sense to cut back some of the new housing spending, potentially by dropping the full housing guarantee. I think housing should still get significant investment, and direct housing payment assistance should still be expanded compared to the baseline, but a guarantee might be too ambitious for now (could be a 2040s goal?)".

You decided the housing plan in three stages (`DEC-2026-11-09-10`, `-12`):
- **Stage 1:** a million new rent-help awards from 2030 (HOU-4A), first for people with no home of their own, homeless or doubled up. About $22B in FY2040.
- **Stage 2:** help for every extremely low-income family with children in serious need. It opens in 2034, capped at 300,000 new families a year, and **becomes a right in 2037** (HOU-4D.01). With the right come:
  - a **duty to house** (a home is found when a family's search fails);
  - a **wider entry** for families with children who have no home of their own.
- **Stage 3:** disabled renters, from 2038 (HOU-4.08).

Stage 2 is **$39.5B in FY2040 and $69.8B in FY2056.** It reaches about **1.53 million families** in FY2040:
- about 920,000 in the core group;
- about 306,000 from the wider entry;
- about 300,000 more once stage 1 takes the first million.

Because it is a right, its cost is an estimate, not a cap. The housing dossier's high case is about twice the central one. Health comes first, and other flagships may give way in the settlement (`DEC-2026-11-15-04`), so this is a money choice about a decided design.

## The options

| | What | FY2040 | FY2056 | FY2030-39 | Stage 2 families housed, FY2040 | Fallback rate (with G10 C, G11, G12) |
| --- | --- | --- | --- | --- | --- | --- |
| A | As booked: a right from 2037 | 0 | 0 | 0 | about 1.53 million | 3.95% |
| B | Drop stage 2: no right, no duty to house, no wider entry. Stage 1, stage 3 and the rest of housing stay. A 2040s target with a review | −39.5 | −69.8 | −115.0 | none | 3.75% |
| **C (recommended)** | **Keep stage 2 as a capped program, not a right.** It is held at its pre-right size (about 900,000 awards, about 810,000 families housed), with no duty to house. Wider-entry families come in within the cap by need. A 2040s target with a review | **−18.6** | **−32.8** | **−44.0** | **about 810,000** | **3.85%** |
| D | Defer the right to 2045, capped as C until then | −18.6 | 0 | −44.0 | about 810,000 until 2045, then about 1.53 million | 3.85% |

The fallback rate is the health contribution's base rate that closes every year from FY2040 to FY2056 (memo G10).

**A, as booked.** About 1.53 million more families housed by FY2040. It costs about 0.1 points more on the health contribution than C (3.95% against 3.85%).

**B, drop stage 2.**
- *What stays:* stage 1's million awards, which go first to homeless and doubled-up families, plus stage 3, the emergency fund, the building and repair programs, and the rural channel.
- *What goes:* help for about 1.5 million families with children in serious need.
- It saves the most, $39.5B in FY2040. But direct rent help then grows only by stage 1's million, which is less than "expanded compared to the baseline" seems to mean for families with children.

**C, a capped program (recommended).**
- *What it is:* stage 2 runs as it would before 2037, a program with a yearly cap, published counts and a review trigger (the design lens, `DEC-2026-11-09-13`). It never becomes a right.
- *Families reached:* about 810,000 families housed in FY2040. That is about 720,000 fewer than the right would house; they wait instead.
- *What is lost for homeless and doubled-up families:*
  - Stage 1's first claim on a million awards stays.
  - The wider entry stays, but within the cap. Families with no home of their own compete by need, not by right.
  - The duty to house goes. A family whose search fails gets search help and a higher payment standard, not a home.
- *Delivery:* nothing new to build. Stage 2's machinery for 2034-36 continues.
- *The 2040s goal:* the statute names a target, a right for the full group, and a review in 2041 on the program's own data. Making it a right then is a later Congress's vote, not automatic.
- *The range:* the saving depends on the cap's size. At a cap reaching 0.45 to 0.65 of the right's families, it is −$14B to −$22B in FY2040.

**D, defer the right to 2045.** The same as C until 2045, then the right returns, so it saves nothing in the long run (FY2056: 0). The fallback rate is still 3.85%, because the tightest years are in the early 2040s and the defense path's later surplus absorbs the right's return. It commits a later Congress to the cost now, which is what makes it a promise. If the 2040s goal should be firm, D is the way to write it.

## Recommendation

**C.**
- It keeps what you said should stay: significant investment, and direct rent help expanded well beyond today's (stage 1 plus about 810,000 stage 2 families).
- It drops the part with an open-ended cost: the right and the duty to house.
- It saves about $19B in FY2040 and $33B in FY2056, and brings the fallback rate from 3.95% to 3.85%.
- The right becomes a 2040s goal, with a review on real data.

**What would change this:**
- **If the money matters more than the families stage 2 reaches,** then B. It saves about $21B more in FY2040 and brings the fallback rate to 3.75%.
- **If the 2040s goal should be a promise in law,** then D.

## Question for you

**G14.** Keep housing's stage 2 as a capped program, not a right, with the right as a 2040s goal and a review (C, recommended)? Or drop stage 2 with a 2040s target (B), defer the right to 2045 (D), or keep it as booked (A)?
