# Memo G3: A broad source for the rest

**Decided:** no VAT: cuts first, option E (a larger health contribution) as the fallback; G3b on the ten-year window, `DEC-2026-11-20-07`. Booked in stage G step 7 (`../2-settlement.md`, `models/data/inputs/settlement.json`). The memo below is the record of the choice as put to Espen; its figures are the draft's.


Role: decision memo for Espen, fork 3 of stage G's batch ([`README.md`](README.md); [`../2-settlement.md`](../2-settlement.md) parts 2, 3 and 5). Status: **provisional, drafted on the recommendation, November 20, 2026; revised for the milestone review (#470: B-1, B-2, B-3, F-5, F-6). This is a new fork:** the audit's list didn't have it, because the audit didn't know how much would be left after the other choices. Not decided, not booked. Nominal $B on case `mixed`, priced by `models/tools/financing-protection/packages.py`. Project arithmetic on exploratory models, not official scores.

## The question

After health takes its share of the top-end and corporate rows, and after the corrections, the cap (memo G4), the education fund (G7), memo G1's option A and memo G2's option C, the plan is still **$263B short in FY2040 (0.49% of GDP), rising to $731B (0.76% of GDP) in FY2056.**

The top end can't close it. The combined top rate on wages is already 68-73%, and the charge on the wealthiest holders' capital income passes 100% before the cap (stack note). The evidence suggests more rate there would raise little (`../../notes/stack-2026-11-16.md` part 3). Taxing employers more conflicts with your direction to spare them (`DEC-2026-11-15-03`). That leaves a broad base, or cuts on the scale of memo G1's option D.

The question: which broad base, if any?

## How a VAT works, and what it would raise

- **The mechanism.** Each business pays a percentage of its sales less what it bought from other businesses. The tax builds up through the chain and lands on what households finally buy.
- **Where it exists.** Every rich democracy except the United States has one. The OECD average standard rate is about 19%. Canada's federal rate is 5% and Japan's is 10%.
- **CBO's estimate.** CBO prices a 5% broad-base VAT at about $3.4T over 2025-34. The legacy menu re-windows it as $3.5T over 2026-35 (`legacy/sources/revenue-channels-and-full-menu.md`, line 112), about $105B a point in FY2040, net of the income and payroll taxes it displaces.
- **The plan's own effect on the base.** CBO's broad base leaves out care that Medicare and Medicaid pay for, but **includes privately paid health care** (CBO budget option 56872). From 2035 the plan pays for that care, so it leaves the taxable base. Without it the base is about 14% smaller: **about $90B a point** (working assumption, range 12-16%; the review's B-2).
- **What it costs households in FY2040, per point:** about $370 in the bottom fifth, $570 in the second, $780 in the middle, $980 in the fourth and $1,390 in the top fifth. That is the gross tax, D3's consumption key.
- **The price convention** (the review's B-1). CBO scores a VAT holding nominal incomes fixed: it shows up as lower pay and profits, not higher prices. The package is scored that way. In practice the Federal Reserve would probably let prices rise once by about the rate.
  - If it does, Social Security, SSI and other indexed benefits rise with prices, which protects retirees and others who live on them.
  - That costs the budget about $120B a year in FY2040 at this package's rate (a risk row in `../2-settlement.md` part 5).
  - It also worsens Social Security's 75-year balance, unless the trust funds' hold-harmless covers the cost-of-living increase as well as the payroll offset.
  - Fixed private pensions and savings get no such protection.
- **The hold-harmless:** a statutory transfer from VAT receipts to the trust funds, equal to their share of the payroll-tax offset, as in the 2011-12 payroll-tax holiday. So Social Security doesn't move on CBO's convention.

## The options

| | What | Rate needed, FY2035 → FY2051 | Households, FY2040, the tax alone (bottom / middle / fourth fifth, $ a year) | Workers ahead, VAT counted | Revenue-mix test (decade / FY2040 / FY2056) |
| --- | --- | --- | --- | --- | --- |
| **A (recommended)** | A broad VAT from the January 2035 endpoint, no rebate | **2.95% → 4.6%** | about −1,090 / −2,300 / −2,900 | **57.8%** | 61% / 54% / 50% |
| B | The same VAT with a rebate: either $350 an adult, or the $300 credit kept as the rebate (memo G1 C) | about 1.1 points more; with the credit kept, 4.1% → 5.6% | about −940 / −2,450 / −3,260 at 4.05% with a $350 rebate | not run | 59% / 52% / 48% (credit kept) |
| C | A targeted VAT credit through the channels the government already runs: SSI, SNAP, the child benefit and the childless EITC | about 0.35 points more (rough) | the bottom fifth's VAT about offset on average | not run | about as A |
| D | The VAT from FY2033 instead of 2035 | 2.95% from FY2033 | as A, two years earlier | 57.8% in FY2040 | 59% / 54% / 50% |
| E | **No VAT:** the health contribution carries the rest, its base rate at about 4.45% in FY2040 and rising with memo G8's steps | 0% | about −30 / −1,020 / −1,770 (the contribution beyond G2 C's 3.25%) | **60.8%** | 65% / 61% / 58% |
| F | No broad tax: cuts instead | — | Whole programs end (memo G1, D) | 76.2% (G2 C's) | — |

**A, a VAT from the endpoint, no rebate (recommended).**
- *Rate:* 2.95% from January 2035, the same day the single plan's savings reach every household. Then 3.6% from FY2041, 3.85% from FY2044 and 4.6% from FY2051. The steps are memo G8's.
- *Households:* a VAT takes a larger share of income from lower-income households, because they spend more of what they have. **Every fifth below the top still comes out ahead on D3:** on the FY2030-39 average (Q1 +$14,308, Q2 +$12,171, Q3 +$10,440, Q4 +$4,553) and in every year from FY2033 to FY2039. The fourth fifth's thinnest year is +$2,001, in FY2033.
- *Exemptions:* none by product: one rate on a broad base, the simplest to run and the hardest to avoid. Small businesses under about $100,000 of sales stay out, which also spares them (`DEC-2026-11-15-03`).
- *Burden:* high at the start. It is a new federal collection system alongside 45 states' sales taxes, with registration for millions of businesses. FY2030-34 is for building it. The IRS's systems and the states' sales-tax registrations are the starting point (design lens: existing machinery first).
- *Political risk:* high. It is a new kind of federal tax, and "a national sales tax" is an easy attack.
- *Legal risk:* low (Congress's taxing power).

**B, with a rebate.**
- A $350 rebate for every adult costs about $98B a year, a little more than a VAT point.
- It protects the poorest in cash, but pays the same to a millionaire, and needs a payment to every adult, including people who don't file.
- **The $300 credit that memo G1 ends is close to this rebate,** and it already has a payment channel. Keeping it (memo G1 C) puts the VAT at 4.1% stepping to 5.6%. The review's F-5 asked that the two be read side by side: G1 A with G3 A is a VAT with no offset, and keeping the credit is close to G3 B.

**C, a targeted credit through existing programs.**
- A credit roughly equal to the bottom fifth's average VAT, paid with SSI, SNAP, the child benefit and the childless EITC, costs about $30-35B a year at this package's rate. That is about 0.35 VAT points, a rough figure, not run on the screens.
- It reaches the bottom fifth without a new channel (`DEC-2026-11-13-08`) and without paying the top.
- It misses low-income people outside those programs. Under reading (a), Social Security and SSI already rise with prices, so that part is automatic.

**D, start in FY2033.**
- The first draft had this. It changes nothing from FY2040 and raises about $420B more over FY2033-34.
- But it puts the fourth fifth behind on D3 in FY2033 (−$235) and only just ahead in FY2034 (+$970), before health's savings arrive (the review's B-4). Not recommended.

**E, no VAT: a larger health contribution instead.**
- *Rate:* about 4.45% of AGI in FY2040, with its exemption below 250% of poverty, rising to cover health's growth. It is priced for FY2040 only; the later steps aren't modelled.
- *With everything counted it is the best for households:* 60.8% of workers ahead, 98.2% below 200% of poverty, and 96.9% of retirees. No new collection system is needed.
- *But:* on the health-only test as decided it is 60.8%, far below your 85%. And "a 4.45% health contribution, rising" is the most visible tax in the plan; Vermont's plan stopped when its full tax became visible [EV-CAR-245].
- *Its revenue-mix test is high partly because of labels:* a larger health contribution is left out of the test as a premium replacement (`DEC-2026-11-15-29`), although beyond 3.25% it pays for more than premiums.

**F, cuts instead.** See memo G1, option D: $263B in FY2040, rising to $731B, from the plan's own programs.

## The revenue-mix test

A VAT falls on everyone who buys things, so it lowers the share of the plan's new general-fund revenue that the top 1% and corporations bear (`../2-settlement.md` part 3). The test is decided on the FY2030-39 window; the rule is more than half.

| Package | FY2030-39 | FY2040 | FY2056 |
| --- | --- | --- | --- |
| As booked | 64% | 57% | 52% |
| **A, as recommended (with G2 C)** | **61%** | **54%** | **50%** |
| A with G2 A (the first draft) | 57% | 50% | 46% |
| A with G1 B | 63% | 58% | 52% |
| E | 65% | 61% | 58% |

## Recommendation

**A, a broad VAT from the January 2035 endpoint, at about 2.95% and stepping with health's growth, with memo G2's fold.**
- Together they raise the money with the smallest VAT that keeps the decided take-home test above three-quarters (76.2%).
- They keep the revenue-mix test passing, spare employers, and leave every fifth below the top ahead on average.

**What would change this:**
- If the bottom fifth's cash matters more than a little more VAT, add **C**, a targeted credit through existing programs (about 0.35 points).
- If a new kind of tax is a step too far, **E** carries it on the health contribution. It is better for households with everything counted, but it is very visible, and it moves the health-only test far from your target.

## Questions for you

**G3.1.** Close what is left with a broad VAT from the January 2035 endpoint, at about 2.95% and stepping with health's growth (A, recommended)? Or a VAT with a rebate (B), a VAT with a targeted credit through existing programs (C), the VAT from FY2033 (D), no VAT and a larger health contribution (E), or cuts (F)?

**G3.2.** D3's revenue-mix test passes on its ten-year window with A (61%), and holds about half in the mature years (54% in FY2040, 50% in FY2056). Accept that the test is read on its decided ten-year window, with the mature-year share reported every year (recommended)? Or require more than half in every mature year too, which needs G1 B, or E?
