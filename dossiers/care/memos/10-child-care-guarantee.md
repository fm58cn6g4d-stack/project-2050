# Memo 10: What families of children under 5 are guaranteed

Role: decision memo for Espen, fork 10 of the care dossier (part C, child care and pre-K; `../3c-design-child-care.md`). Status: **for Espen, not decided.** Sources are named in plain text; bracketed tags point to the evidence register (`../evidence.json`). Costs marked "judgment" are this dossier's working assumptions, not official scores; their basis is in `../3c-design-child-care.md`, "What the options cost".

**This memo decides what a family with a child from birth to kindergarten can count on for paid child care, and what it pays.** Pre-K for 3s and 4s is memo 11. How fast it starts is memo 12. Who runs it is memo 13.

## The question

- **Today.** Full-day care for one child costs 8.9% to 16.0% of median family income (Department of Labor, 2024) [EV-CAR-514]. Federal help reaches 16 percent of eligible children (ASPE, 2026) [EV-CAR-507].
- **By 2029.** The 2024 rule's 7% copayment cap is rescinded (HHS, 2026) [EV-CAR-510]. The 2025 law's tax changes help families who owe income tax [EV-CAR-502] [EV-CAR-503].
- **The question.** Should the plan grow today's rationed programs, guarantee that no family pays more than a set share of income, or make care free or nearly free for everyone?
- **The legacy design.** FAM-2 phases toward a 7% of income cap (`legacy/domains/domain-family.md`). It is a working choice, weighed here as an option (`DEC-2026-10-30-02`).

## What the evidence says, in five lines

1. Cheap care raises mothers' employment where price holds them back: strongly in Quebec (Baker, Gruber and Milligan, Journal of Political Economy, 2008; Lefebvre and Merrigan, 2008; quasi-experimental) [EV-CAR-530] [EV-CAR-532], barely in Norway (Havnes and Mogstad, 2011) [EV-CAR-544].
2. Children gain from good care (Norway) [EV-CAR-543] and can lose from fast expansion into fair-quality care (Quebec) [EV-CAR-531] [EV-CAR-536].
3. Cutting prices before building supply produces waitlists (Canada's Auditor General, 2025; C.D. Howe, 2026; quasi-official data) [EV-CAR-538] [EV-CAR-539].
4. More block-grant money without more children served: appropriations more than tripled after 2015 while the count stayed near 1.3-1.4 million (CRS, 2024) [EV-CAR-508].
5. U.S. legislative consensus on the left is a 7% cap with free care for lower incomes (Child Care for Working Families Act, 2025; Build Back Better, 2021) [EV-CAR-580] [EV-CAR-587]. The bipartisan route is tax credits [EV-CAR-583] [EV-CAR-584].

## The options

**A. Grow the block grant and make the dependent care credit refundable (the bipartisan route).**
- *What it is:*
  - CCDBG roughly triples, to about $26 billion.
  - Point 1 puts the 2024 protections in law.
  - The dependent care credit becomes refundable, as in the bipartisan PACE Act [EV-CAR-584].
  - States still set eligibility and waiting lists.
  - Paired with universal pre-K (memo 11), this is the legacy FAM-2C.
- *Where tried:* every state's subsidy program today; the 2014 reauthorization [EV-CAR-585].
- *For people:* a single mother earning $30,000 in a state that funds her gets care for a $50-a-month copay. Her neighbor in the next income bracket, or on the waiting list, gets a tax refund of a few hundred dollars.
- *Cost:* about $25 billion a year more at maturity (range $15-35 billion; judgment).
- *Evidence strength:* program evaluation and descriptive data. More money has bought higher rates more than more children [EV-CAR-508].
- *Political risk:* the lowest. Republicans have backed CCDBG increases and the Britt-Kaine credits [EV-CAR-583]. It would not be felt by most families, so it wins few votes either.
- *Burden:* states' income and activity checks stay. Waiting lists stay.

**B. A capped-cost guarantee: free at or below 85% of state median income, never more than 7% of income above it, with no upper limit (recommended).**
- *What it is:*
  - Every child under 5 whose family wants paid care is entitled to it.
  - Families at or below 85% of state median income pay nothing.
  - Above that, copays rise to a 7% maximum above 150%, as in the 2025 Child Care for Working Families Act [EV-CAR-580].
  - There is no upper income limit and no activity test (point 2).
  - Income is checked once a year (point 3).
  - Providers are paid by enrollment at cost-of-care rates (memo 12).
  - This is the end state of the legacy FAM-2A.
- *Where tried:* Washington State's 7% cap (2021, now paused) [EV-CAR-549]; the 2024 federal rule, now rescinded [EV-CAR-510]; DoD's income-based fees [EV-CAR-551]; Build Back Better's House-passed design.
- *For people (illustrative):*
  - *Two parents earning $70,000 in Ohio:* they pay nothing for their toddler instead of about $10,000 a year.
  - *A family earning $180,000:* it pays no more than about $12,600 for two children.
- *Cost:* about $85 billion a year of new federal money at maturity (2033), range $50-145 billion (judgment). About $110 billion in FY2040. The arithmetic: about $118 billion of gross care, less copays and today's block grant, at a 90% federal share, plus administration (`../3c-design-child-care.md`, "What the options cost").
  - *States' share (step 8, `DEC-2026-11-11-05`):* at the recommended 90% for three years, then 80%, about $74 billion a year at maturity and $97 billion in FY2040, with states paying about $20 billion a year. The options (90%, 80%, 75%) and the risk that states decline are in `../3c-design-child-care.md`, "States' share".
  - *How it compares.* CBO put Build Back Better's six-year child care and pre-K at $381 billion and $752 billion if permanent, with a third of children in non-participating states (CBO via CRFB) [EV-CAR-587]. Scaled to full participation and the 2030s, that is about $150-200 billion a year for child care and pre-K together. This option plus memo 11 A is about $145 billion, at the bottom of that range, because families above 85% of state median income pay copays.
  - *Wages.* Part D's wage floor at parity would add about $45 billion.
- *Evidence strength:* international practice and program evaluation for capped fees (DoD, Washington). The employment and child effects are quasi-experimental and depend on quality and supply (lines 1-3).
- *Political risk:*
  - The cost is large. BBB's version died with a senator's objection to the bill's size and its temporary programs [EV-CAR-589].
  - Critics argue the benefits reach relatively high-income families (Niskanen Center, 2023) [EV-CAR-590].
  - A cap can raise prices if supply does not grow.
  - "No activity test" will be attacked (point 2).
- *Burden:* one income statement a year. Nothing for families at or below 85%.

**C. Universal low flat fee or free care, with no income test (Quebec, Canada, New Mexico).**
- *What it is:* every child in licensed care pays a flat low fee (about $10 a day) or nothing. Provinces and states fund the slots.
- *Where tried:*
  - *Quebec since 1997* [EV-CAR-530]. Big employment gains; quality and child outcome problems [EV-CAR-531] [EV-CAR-535].
  - *Canada since 2021* [EV-CAR-537]. Fees cut fast; spaces short, waitlists up [EV-CAR-538] [EV-CAR-539] [EV-CAR-540].
  - *New Mexico since November 2025.* Too new to evaluate, with its cost disputed [EV-CAR-547].
- *For people:* everyone pays the same small fee, the simplest offer to explain. The family earning $180,000 saves $25,000 a year, more than the family at 85% saves under B.
- *Cost:* about $115 billion a year at maturity (range $75-185 billion; judgment). It is about $30 billion more than B, mostly copayments forgone by families above 85% of state median income and more use by higher-income families. New Mexico's fiscal staff warn of the same take-up risk [EV-CAR-547].
- *Evidence strength:* international practice and quasi-experimental studies, positive for employment and mixed for children.
- *Political risk:* the most popular offer and the hardest to fund. Demand outruns supply first here, and rationing by waitlist is the visible failure.
- *Burden:* none on families.

## Consequences at a glance

| | A. Block grant and credit | **B. Capped-cost guarantee** | C. Universal flat fee or free |
| --- | --- | --- | --- |
| Who is guaranteed care | No one; states ration | Every child under 5 | Every child under 5 |
| What a family at 85% of state median income pays | A state copay, if served | Nothing | A flat fee or nothing |
| What a family at 200% pays | Market price, less a credit | At most 7% of income | A flat fee or nothing |
| New federal cost, maturity (2033) | about $25 billion | about $85 billion | about $115 billion |
| FY2040 | about $30 billion | about $110 billion | about $150 billion |
| Supply pressure | Low | High | Highest |
| Paperwork | State eligibility and activity checks | One statement a year | None |
| Political base | Bipartisan, low salience | Democratic bills since 2017; BBB | Most popular, least proven at U.S. scale |

**Fiscal rule** (`DEC-2026-11-10-05`): B and C reach many of the same families at different cost, so the choice is partly about money and comes to you. The cost is reported to the financing settlement; nothing is trimmed here.

## Recommendation: B

- **It guarantees care to every family without paying the most for the families who need it least.** Families at or below 85% of state median income get what C gives them. Above that, copays keep the cost about $30 billion a year below C.
- **It is the tested U.S. design.** The 7% cap runs through the CCWFA, BBB, Washington and the 2024 rule [EV-CAR-580] [EV-CAR-549] [EV-CAR-510]. The DoD system shows sliding fees and good care can coexist [EV-CAR-551].
- **It follows the design lens.**
  - It drops what makes today's subsidies hard to use: the activity test (point 2), the waiting list and the mid-year checks (point 3).
  - The one remaining test is a yearly income statement, read from the tax record or the family's word.
- **Its evidence strength is moderate.** The employment gain is quasi-experimental and depends on how many parents price holds back. Children's gains depend on quality, which memos 11 and 12 and part D carry. The cost range is wide because take-up is uncertain.
- **If you prefer universality,** C costs about $30 billion a year more and removes the last form. **If you want the smallest step,** A is the fallback, but it leaves most families where they are.

**What would change this:**
- New Mexico's first evaluation shows a universal design's take-up near B's (C's extra cost would then be smaller);
- the financing settlement cannot carry B (A's block grant, with B's design for the lowest-income tier, as a fallback);
- part D finds the workforce cannot grow fast enough for B by 2032 (memo 12's later date).

## If you decide

- **What section 4 writes.**
  - *Under B or C:* a new mandatory child care title in the 2029 reconciliation bill (the working vehicle), with the payment rules of memo 12.
  - *Under A:* CCDBG amendments and appropriations, and the credit's refundability through the secure floor.
- **What section 6 prices.** The choice, with memo 12's phasing, on fiscal years.
- **The agenda.**
  - FAM-2A carries B's design.
  - FAM-2F (new) carries A.
  - FAM-2E (new) carries C.

## Questions for you

1. A, B (recommended) or C?
2. Under B, is 85% of state median income the right free line? It is the CCWFA's line. The legacy used 75%; a lower line costs less and charges more families.
