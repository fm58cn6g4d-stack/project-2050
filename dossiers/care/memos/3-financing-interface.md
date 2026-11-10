# Memo 3: How money flows into the health system

Role: decision memo for Espen, fork 3 of the health design (`../3-design.md`). Status: for Espen's decision. Sources are named in plain text; bracketed tags point to the evidence register (`../evidence.json`); "the coverage model" is this project's exploratory analysis (`models/tools/health-coverage/results.md`).

**This memo decides the plumbing, not the taxes.** Which taxes pay for the plan, and who bears them, is the financing settlement's job (`charter/PLAN.md` 3.1; `DEC-2026-11-10-05`: dossiers report their cost, the settlement balances the plan). What the health design must decide now is which existing money streams stay, which end, and what the new revenue must fill, because that sets the size of the gap the settlement closes.

## The money today, and the amount to be financed

- In 2024, private insurance paid $1,644.6 billion of national health spending, Medicare $1,118.0 billion, Medicaid $931.7 billion, and people $556.6 billion out of pocket (CMS, 2025) [EV-CAR-121].
- Under single-payer (memo 1, C) in 2032, the coverage model finds the federal government would carry about $3.3 trillion more a year, while households stop paying about $1.7 trillion in premiums and out-of-pocket costs and employers about $1.5 trillion in premiums. The total flowing through the system changes little; who pays it changes completely.
- Under the public option (A) or the staged path in its early years (B), the amount is about $240-260 billion a year in 2032 (the coverage model).

## The options

**A. New dedicated revenue only.** Every existing private flow ends when people move; the gap is filled by taxes the settlement chooses, into a single health trust fund.
- *For:* simplest to explain; one fund.
- *Against:* the largest new tax, about $3.3 trillion a year at full scale, with no credit for money states and employers already spend. Vermont's plan stopped when its full tax became visible (VTDigger, 2014; State of Vermont, 2014) [EV-CAR-245] [EV-CAR-244].

**B. Keep the existing public streams and replace premiums with contributions (recommended).**
- *Medicare's streams stay:* the payroll tax for hospital insurance, the premiums and general revenue that fund doctors' and drug coverage, all folded into one fund. Under a staged path, the hospital trust fund is kept whole as the legacy design required (D4; `legacy/domains/domain-health.md`).
- *States pay a fixed maintenance of effort* equal to their current share of Medicaid spending for the people who move, growing with a set index. In the coverage model, states keeping half their current spending lowers the federal cost by about $300 billion a year at full scale.
- *Employers' premiums become a contribution* while their workers move (memo 2, point 4), then a broad payroll contribution the settlement sets. Employers already pay about $1.5 trillion a year in premiums in 2032 (the coverage model).
- *New revenue fills the rest,* chosen by the financing settlement under D3 (households below the top come out ahead).
- *For:* the new tax is far smaller than A's because existing money keeps flowing; households see premiums and deductibles end while the employer contribution is a known, capped amount.
- *Against:* more streams to administer; states and employers argue the size of their share.

**C. Income-related public premiums.** People pay a premium to the public plan scaled to income (Vermont's design capped it at 9.5% of income; State of Vermont, 2014) [EV-CAR-244], plus employer and new revenue.
- *For:* keeps a visible link between coverage and payment; lowers the new tax.
- *Against:* every premium needs income checks and collection, the kind of step that drops eligible people (Shepard and Wagner, American Economic Review, 2025) [EV-CAR-206]; it works against the design lens.

## Recommendation

**B.** It keeps the money already in the system, leaves the settlement the smallest gap to fill, and asks nothing of people at the point of care. Under a public option (memo 1, A) only its first part applies: the hospital trust fund kept whole, and the restoration and public plan paid from the general fund.

**Fiscal rule.** The coverage model reports the amount to be financed for each option (2032 and FY2030-39) and section 6 will report the FY2040 permanent cost. Nothing is trimmed to fit (`DEC-2026-11-10-05`).

**What would change this:** if the financing settlement concludes that a single broad tax is fairer than an employer contribution, B's employer part becomes A's; the state part stays.

## Questions for you

1. Which plumbing: A, B (recommended) or C?
2. Should states pay a fixed maintenance of effort (recommended), and at about their current share?
