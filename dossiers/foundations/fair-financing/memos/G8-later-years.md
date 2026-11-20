# Memo G8: Keeping the later years closed

Role: decision memo for Espen, fork 8 of stage G's batch ([`README.md`](README.md); [`../2-settlement.md`](../2-settlement.md) part 3; `../1-audit.md` part C, item 3). Status: **provisional, drafted on the recommendation, November 20, 2026. This is a new fork, not on the audit's list.** Not decided, not booked. Nominal $B and shares of GDP on case `mixed`, priced by `models/tools/financing-protection/packages.py`.

## The question

The fiscal rule tests the general fund in FY2040 **and every later year**. A package that balances FY2040 doesn't stay balanced on its own, because two of the plan's costs grow faster than the economy:
- **The single plan grows at GDP plus 1 point** under D2's national health budget (`DEC-2026-11-15-08`). In the model, health's spending rises from 6.5% of GDP in FY2040 to 7.5% in FY2056.
- **Long-term care grows about 5.5% a year,** as the population ages.

Health's own revenue (the contributions, the employer contribution, the tax on former premiums) grows about with the economy. So without a further step, the gap reopens by about 0.02% of GDP a year after FY2040: about **0.27% of GDP by FY2056, $263B in that year** on memo G3's package. Part of that is memo G2's fold, which doesn't grow to the 2 points' full rate as they would have from FY2044.

The question: how to keep the later years closed.

## The options

| | What | VAT path (memo G3, A) | Cost to households early | Certainty |
| --- | --- | --- | --- | --- |
| **A (recommended)** | **Steps set in law now,** each one able to be delayed by the plan's fund trustees if it isn't needed | 2.95% from the January 2035 endpoint; 3.6% from FY2041; 3.85% from FY2044; 4.6% from FY2051 | Lowest | High: the package closes every year to FY2056 on paper |
| B | One rate from the start, high enough for FY2056 | 4.6% from 2035 | About $1,600 a year more for a fourth-fifth household from 2035; surpluses until about 2050 | High |
| C | No steps in law: each Congress closes the gap when it appears | 2.95% throughout | Lowest | Low: the rule fails from about FY2041 |
| D | Slow health's growth instead: D2 at GDP plus 0.5 from FY2045 | Lower steps (not priced) | Lowest | It reopens a decided health design, so it is listed only for completeness |
| E | A, with a margin of 0.1% of GDP every year (the review's F-2) | 3.55% from 2035; 4.2% from FY2041; 4.45% from FY2044; 5.2% from FY2051 | About $590 a year more for a fourth-fifth household in FY2040 | Higher: about $55-100B a year of room for a yield shortfall |

**A, steps in law (recommended).**
- *How it works:* the plan's fund trustees publish, every year, health's and long-term care's growth against GDP. A scheduled step takes effect on its date unless the trustees certify that the gap it closes hasn't appeared. Congress can always replace a step with something else of the same size.
- *Why:* budget scorers and markets see a funded plan. Households pay only as the costs arrive. And the trustees' review can delay a step that isn't needed (design lens: published counts with a review trigger).
- *Check:* on the central estimate, A keeps every year from FY2040 to FY2056 closed. The worst year is FY2043, at 0.00% of GDP.
- *A cost of every step:* each one is broad revenue, so the revenue-mix test's share falls as the steps arrive: 54% in FY2040 and 50% in FY2056 (memo G3, point G3.2).
- *Its margin is thin:* about $3-7B a year. Any shortfall in yield breaks the rule, and the yield risks have no backstop (memo G5). E buys room.
- *Legal footing* (the review's F-7): Congress sets the rates, the dates and the trigger, and the trustees find a fact. That is contingent legislation of the kind upheld in *Field v. Clark* (1892) and *J.W. Hampton v. United States* (1928). The statute should say a step takes effect by default if a finding is challenged. Step 7 writes it into the settlement's specification.

**B, one rate from the start.** It is simpler, but it collects up to 1.65 points more than needed in the 2030s and 2040s, from households, years before the costs arrive.

**E, a margin.** It costs about 0.6 VAT points from the start, and keeps about 0.1% of GDP in hand each year against the yield risks.

**C, leave it to later Congresses.** That is how the gap becomes a cut to health, which is what you asked the plan to avoid.

**D, tighten D2.** It would hold the plan's spending closer to the economy's growth. But health's design, and D2 with it, is settled. Health comes first.

## Recommendation

**A.** Scheduled steps in law, which the trustees can delay when the costs don't arrive. If you weigh the yield risks heavily, add E's margin.

## Question for you

**G8.** Keep the later years closed with scheduled VAT steps set in law now, which the plan's fund trustees can delay if a step isn't needed (A, recommended)? Or one higher rate from the start (B), no steps (C), or A with a margin of 0.1% of GDP (E)?
