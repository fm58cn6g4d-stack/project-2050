# Memo G3: A broad source for the rest: a value-added tax

Role: decision memo for Espen, fork 3 of stage G's batch ([`README.md`](README.md); [`../2-settlement.md`](../2-settlement.md) parts 2 and 3). Status: **provisional, drafted on the recommendation, November 20, 2026. This is a new fork: the audit's list did not have it, because the audit did not know how much would be left after the other choices.** Not decided, not booked. Nominal $B on case `mixed`, priced by `models/tools/financing-protection/packages.py`. Project arithmetic on exploratory models, not official scores.

## The question

After health takes its share of the top-end and corporate rows, and after the corrections, the cap (memo G4), the education fund (G7), memo G1's option A and memo G2's option A, the plan is still **$487B short in FY2040 (0.90% of GDP), rising to $1,160B (1.21% of GDP) in FY2056.**

The top end can't close it. The combined top rate on wages is already 68-73%, and the charge on the wealthiest holders' capital income passes 100% before the cap (stack note). The evidence suggests more rate there would raise little (`../../notes/stack-2026-11-16.md` part 3). Taxing employers more conflicts with your direction to spare them (`DEC-2026-11-15-03`). That leaves a broad base, or cuts on the scale of memo G1's option D.

The question: which broad base, if any?

## The options

| | What | Rate needed | Households, FY2040, $ a year (bottom / middle / fourth fifth), the tax alone | Take-home test |
| --- | --- | --- | --- | --- |
| **A (recommended)** | A broad **value-added tax**, collected from health's January 2035 endpoint, no rebate | **4.75%**, stepping to 6.3% by FY2051 (memo G8) | about −2,030 / −4,300 / −5,430 at 4.75% | Unchanged (88.7%) |
| B | The same VAT with a refundable rebate of $350 an adult | about 5.7% | about −1,890 / −4,440 / −5,760 | Unchanged |
| C | A broad income contribution instead (memo G2's 2 points kept, plus about 2.6 more points above $20,000/$40,000) | about 4.6 points of AGI above the line | about −120 / −3,120 / −6,280 | Below 70.1% of workers ahead (not priced) |
| D | No broad tax: cuts instead | — | Whole programs end (memo G1, D) | 88.7% |

**How a VAT works.** Each business pays a percentage of its sales less what it bought from other businesses, so the tax builds up through the chain and lands on what households finally buy. Every rich democracy except the United States has one. The OECD average standard rate is about 19%; Canada's federal rate is 5% and Japan's is 10%. CBO prices a 5% broad-based VAT at about $3.5T over 2026-35 (`legacy/sources/revenue-channels-and-full-menu.md`, line 112). That is about **$105B a point in FY2040**, net of the income and payroll taxes it displaces (CBO's convention). The trust funds are held harmless for their share, as they were for the 2011-12 payroll-tax holiday.

**A, a VAT with no rebate (recommended).**
- *Rate:* 4.75% from January 2035, the same day the single plan's savings reach every household; 5.25% from FY2041, 5.6% from FY2044 and 6.3% from FY2051. The steps are memo G8's. An earlier start (FY2033) would put the fourth fifth behind on D3 in FY2033-34, before health's savings arrive.
- *Households:* a VAT takes a larger share of income from lower-income households, because they spend more of what they have. In FY2040 the 4.75% costs about $2,030 a year in the bottom fifth, $4,300 in the middle and $5,430 in the fourth. Against the plan's whole package, **every fifth below the top still comes out ahead on D3**: Q1 +$13,896, Q2 +$11,669, Q3 +$9,935, Q4 +$4,102 a household a year on the FY2030-39 average.
  - The fourth fifth is ahead in every year: +$2,001 in FY2033 (its thinnest year, before the VAT), +$4,861 in FY2035 (the VAT's first year) and +$9,653 in FY2039 (`../2-settlement.md` part 3).
  - Within each fifth, some households come out behind. The secure floor's benefits and the health contribution's exemption are the protection for the lowest incomes. A flat rebate is the poorly targeted alternative (B).
- *Exemptions:* none by product: one rate on a broad base, which is simplest to run and hardest to avoid. Small businesses under about $100,000 of sales stay out, which also spares them (`DEC-2026-11-15-03`).
- *Burden:* high at the start. It is a new federal collection system alongside 45 states' sales taxes, with registration for millions of businesses. FY2030-34 is for building it. The IRS's own systems and the states' sales-tax registrations are the starting point (design lens: existing machinery first). Prices rise once by about the rate, then inflation returns to normal.
- *Political risk:* high. It is a new kind of federal tax, and "a national sales tax" is an easy attack.
- *Legal risk:* low (Congress's taxing power).

**B, with a $350 rebate for each adult.** It costs about $95B a year, so the rate needs about 0.9 points more. It protects the poorest households in cash, but it pays the same $350 to a millionaire, and it needs a payment channel to every adult, including people who don't file.

**C, a broad income contribution instead.** It is more progressive than a VAT and uses the existing return. But it falls on pay, like the health contribution, and the take-home test would collapse: with the 2 points alone it is 70.1% of workers ahead, and each further point lowers it (not priced here). It also charges the fourth fifth more than the VAT does.

**D, cuts instead.** See memo G1, option D: roughly all of child care, pre-K and the child benefit, and still growing.

## The revenue-mix test

A VAT falls on everyone who buys things, so it lowers the share of the plan's new general-fund revenue that the top 1% and corporations bear (`../2-settlement.md` part 3):

| Package | FY2030-39 | FY2040 | FY2056 |
| --- | --- | --- | --- |
| As booked | 64% | 57% | 52% |
| **A, as recommended** | **57%** | **50%** | **46%** |
| With G1 B | 60% | 52% | 48% |
| With G2 C | 60% | 54% | 50% |
| With G1 B and G2 C | 63% | 57% | 52% |

The test is decided on the FY2030-39 window, where A passes. In the mature years the share falls to about half and below. This is a consequence to weigh (point G3.2), not a reason the package fails the test as written.

## Recommendation

**A, a broad VAT from the January 2035 endpoint, stepping with health's growth.** It is the only base large enough to close the gap that keeps your take-home test, spares employers and leaves every fifth below the top ahead on average.

**What would change this:**
- If the bottom fifth's cash matters more than the rebate's cost and burden, then **B**.
- If you would rather not have a new kind of tax at all, then memo G2's option C, folding the 2 points into the health contribution, roughly halves the VAT needed (2.75% stepping to 4.0%).

## Question for you

**G3.1.** Close what is left with a broad value-added tax, collected from the January 2035 endpoint at about 4.75% and stepping with health's growth (A, recommended)? Or a VAT with a $350 rebate for each adult (B), a broad income contribution instead (C), or cuts instead (D)?

**G3.2.** D3's revenue-mix test (the top 1% and corporations bear more than half of new general-fund revenue) passes on its window with the VAT: 57% over FY2030-39. But it falls to 50% in FY2040 and 46% in FY2056, because a VAT falls broadly. Accept that the test is read on its decided ten-year window (recommended, with the mature-year share reported every year)? Or require it in mature years too, which needs G2 C or G1 B or both (G1 B and G2 C together: 63%, 57% and 52%)?
