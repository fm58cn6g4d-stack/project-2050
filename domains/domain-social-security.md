# Domain file: Social Security (SS)

Canonical. This file applies Governing Decision D8: solvency first, with a targeted increase, as a regular-order bill in spring 2030. Effects on the 75-year actuarial balance are in percent of taxable payroll. Ten-year dollar figures are for 2030-39 in trillions.

## The gap

The 2026 Trustees report puts the 75-year deficit at **4.42% of taxable payroll**. The combined trust funds are depleted in **2034**, when 83% of benefits are payable (revenue tab, citing the 2026 report). The gap is larger than in 2023, when SSA's actuaries scored the Sanders-Warren bill against a 3.42% deficit. Every figure below scaled from that 2023 letter is therefore a share of a smaller gap than today's.

**The OASI fund alone runs out sooner.** Rep. Larson's June 2026 statement on the Warren-Moreno framework describes the 2026 Trustees report as putting OASI depletion "in as little as six years," about 2032 (as reported; not re-checked against the report here). That date, an automatic cut of roughly a fifth to a quarter of retirement benefits landing in or near a presidential election year, is what makes a bipartisan deal plausible in 2029-30 (SS-10).

## Chosen design: the D8 baseline

| ID | Piece | Effect on the 75-year balance | Basis |
| --- | --- | --- | --- |
| SS-1 | 12.4% tax on earnings above $250,000 (unindexed threshold), with a small benefit credit for the new taxes | +2.30 | estimate on SSA's 2026 scores (index/dedicated-funds.md: E2.5's base and E2.14's 2% credit, from 2031); SSA scores the 2027 versions at +2.37 (E2.16) and +2.41 (E2.14) |
| SS-2 | 12.4% Social Security tax on investment income above $400,000, credited to the trust fund | +1.17 before the haircut (from 2031); about +0.99 after it | SSA scores this exact tax from 2028 at +1.22 (F11, 2026 Trustees, sourced); the model moves it to 2031. A 15% stacking haircut is booked on top of SSA's behavioral response because REV-H1b taxes the same income (estimate) |
| SS-3 | Higher minimum benefit: 125% of poverty for 30-year workers, wage-indexed | −0.11 | sourced (SSA B5.2, 2026 Trustees) |
| SS-4 | CPI-E for cost-of-living adjustments (about +0.15 points a year) | −0.33 | sourced (SSA A6, 2026 Trustees) |
| | **Baseline, net** | **about +2.85** after the SS-2 haircut (+3.0 before) | estimate (index/dedicated-funds.md; interactions ignored) |
| | **Share of the 4.42% gap** | **about 64%** (68% before the haircut); depletion moves from 2034 to about 2062 | estimate |

**The baseline does not reach 75-year balance.** A gap of about 1.6% of payroll remains after the stacking haircut, and the trust fund runs down from the 2040s to depletion in about 2062 (estimate, index/dedicated-funds.md, built on SSA's 2026 scores of each provision). The closers below cover the gap.

## Closers (choose at least one)

| ID | Piece | Effect | Basis | Who pays |
| --- | --- | --- | --- | --- |
| SS-5 | Investment-income tax on active S-corporation holders and limited partners, as in Sanders-Warren section 8b | +0.87 from 2031 | sourced (SSA F8, 2026 Trustees: +0.93 from 2027) | High-income business owners |
| SS-6 | Lower SS-2's threshold to $200K/$250K | about +0.1 more | sourced difference (SSA 2026: F9 at the ACA thresholds +1.32 against F11 at $400K +1.22) | Households above $200K/$250K |
| SS-7 | Raise the payroll rate 1 point (0.5 each side), phased over 10-20 years | +0.9 to +1.0 | estimate (Trustees' rate math) | All covered workers |
| SS-8 | Invest part of the reserves in equities | +0.5 to +1.0 | estimate | No one directly; market risk |
| SS-9 | Cover newly hired state and local workers | small | sourced (revenue tab) | New public employees |

**Recommendation (an option, not yet decided): baseline plus SS-5.** It closes about 84% of the gap (about 88% before the stacking haircut) and moves depletion to about 2081 (estimate, index/dedicated-funds.md), without a middle-class rate increase, keeping solvency entirely on high incomes. It leaves about 0.7% of payroll. SS-6 now adds only about 0.1 (SSA's current scores), so closing the rest needs SS-7 or SS-8, or a further high-income source; SS-7 is also the fallback if the business-income tax proves hard to administer.

## SS-10. A bipartisan path on the Warren-Moreno framework (option, not chosen; D8 stands unless Espen changes it)

**The real-world opening.** On June 23, 2026, Sens. Elizabeth Warren and Bernie Moreno (R-Ohio) published a joint New York Times op-ed proposing to lift the Social Security payroll-tax cap so high earners pay the same share of income as other workers, and said they are working together on legislation to remove the cap (Moreno and Warren press releases, June 23, 2026). No bill text or design details beyond lifting the cap were found; the design below is a scenario, not their bill.

**What the Talarico scenario model tested.** In the model a partisan Social Security bill fails 53-47 in March 2029; the next Trustees report brings the OASI cut close to the 2032 election; Finance negotiates on the Warren-Moreno framework through the summer, with an untested majority-rule carve-out held in reserve as leverage; and Republicans prefer a deal they shape at 67 votes to one imposed at 53. The modeled trade (scenario design, not scored):
- **Democrats get:** the cap lifted entirely, a minimum benefit at 125% of poverty (SS-3), caregiver credits (SS-B4), and permanent WEP/GPO repeal (already law since January 2025, so in practice a no-reversal guarantee).
- **Republicans get:** a bend-point adjustment for the top 8% of lifetime earners (lower benefit accrual at the top), no investment-income inclusion (no SS-2), no payroll-rate increase (no SS-7), a "donut" exempting earnings between the current cap and $400,000 that closes by 2040, and an enhanced benefit for long-career low-wage workers.
- **Result in the model:** solvent to 2081. The model's own figure; it has not been scored by SSA's actuaries.

**Why it matters for the base case.** D8's baseline is a regular-order bill that relies on D2's graduated cloture (F) or 60 votes, passes at best with the caucus alone, and leaves 28-35% of the gap open without a closer. A 67-vote law is a different asset from a 51- or 54-vote one: the scenario's finding is that "a 54-vote Social Security law is a repeal target for forty years; a 67-vote one is settled." The cost is the design: SS-10 drops SS-2 (about +1.1 to +1.36 of the balance and $0.75-1.2T of in-window trust-fund revenue) and replaces it with a bend-point change for top earners, which D8's "targeted increase" framing did not include, and the donut delays revenue from earnings between the cap and $400,000 until 2040.

| Option | Design | Effect | Basis |
| --- | --- | --- | --- |
| SS-10A | Pursue SS-10 first, with the D8 baseline held at 53 as the fallback (the scenario's "credible threat") | A 67-vote solvency law if it lands; D8 if it does not | scenario design |
| SS-10B | D8 baseline, with SS-10's minimum-benefit and long-career pieces offered to recruit Republican votes | Keeps SS-2; less likely to reach 60 | estimate |
| SS-10C | D8 as decided; no bipartisan track | The base case | — |

**Needs before it can be chosen:** an SSA actuarial score of the trade (the cap lift without SS-2 and with the donut and bend-point change); a check that the top-earner bend-point change passes D3 (it falls only on the top of the lifetime-earnings distribution, so it should); and Espen's decision on D8. **Timing:** if pursued, SS-10 is a 2029 negotiation, not a spring-2030 floor bill, since the leverage comes from the approaching OASI date and the bill would not need majority-rule floor days.

## Benefit add-ons (each widens the gap)

| ID | Add-on | Effect | Basis |
| --- | --- | --- | --- |
| SS-B1 | Across-the-board increase of about $200 a month, via the first bend point and the PIA factor | −1.46 | sourced (SSA 2023) |
| SS-B2 | Smaller flat increase, about $50-100 a month | −0.4 to −0.7 | estimate |
| SS-B3 | Student benefits to age 22 | −0.05 | sourced (SSA 2023) |
| SS-B4 | Caregiver credits | not scored here | |

A visible increase needs a matching closer. For example, SS-B2 paired with SS-5 and SS-6 keeps the package near balance.

## Options not chosen (D8)

| Option | Why not |
| --- | --- |
| A. Bill Book expansion: across-the-board increase, CPI-E, cap above $250K | Widens the gap; the 2032-34 crisis stays |
| C. Solvency only | No constituency gain; D8 chose a targeted increase |
| Retirement age to 69; chained CPI | Benefit cuts; fail the design rules. Kept only so the ledger can price a bipartisan path |

## Ten-year dollars (2030-39)

These are trust-fund figures, outside the general fund (D4).
- **Revenue:** SS-1 brings about $3.67T to the trust fund (range $3.3-3.9T) and SS-2 about $1.48T before the 15% haircut, about $1.26T after it (estimate: SSA's 2026 single-year scores applied from 2031, index/dedicated-funds.md). These are gross trust-fund receipts; the older $1.9T for SS-1 was scaled from a CBO budget score, which nets out the income-tax offset and is not what the trust fund receives.
- **Benefits:** SS-3, SS-4 and SS-1's benefit credit cost about $0.19T in the window (range $0.15-0.25T, estimate), since all three build slowly.
- **Ledger row:** SS-1 (legacy F5), with trust-fund revenue of about $4.93T at the midpoint after the haircut (rows O1, O2, OX).

## Vehicle, timing and floor time

- **Vehicle:** regular order, spring 2030, before the midterm. Section 310(g) bars Social Security from reconciliation, so the bill relies on D2's graduated cloture (F, adopted week one of 2029) or 60 votes. SS-10 would be a bipartisan alternative negotiated in 2029.
- **Floor time:** about 8 days.
- **Survival at 51 (D1):** only with the rules change and full caucus unity. The revenue sits entirely above $250K/$400K, which helps hold the caucus.
- **Felt date:** the minimum benefit and CPI-E start with the first COLA after enactment, about January 2031. Solvency is "felt" as the absence of the OASI cut (about 2032) and the combined-fund cut (2034).

## Dependencies

- **D2:** graduated cloture (F), or 60 votes (SS-10 aims at 67).
- **Overlap with REV-H1b:** SS-2's base overlaps H1b's 5% Medicare and investment-income rate above $400K (in the general fund). Both stack on the same income, and both carry a 15% avoidance haircut (domains/domain-revenue.md, stacking section). A joint behavioral score would replace the flat haircut. SS-10 would drop SS-2 and with it the stacking problem.
- **Capacity:** SSA staffing is in CAP-7 (domains/domain-capacity.md).

## Open items

1. **To do (Espen, Oct 20): test whether the 67-vote framework holds up, then compare the paths again.** A later session should put SS-10A, SS-10B and SS-10C side by side with the D8 baseline and its closers (SS-5, SS-7), on the same footing:
   - **Votes:** check the 67-vote premise against current reporting. Has Warren-Moreno legislation been introduced, who has cosponsored it, and does any Republican beyond Moreno back the cap lift? What does the Talarico scenario's 67-vote outcome assume that may not hold in a 52-54 seat Senate?
   - **Solvency:** the share of the 4.42% gap each path closes, on SSA actuarial scores where they exist (SS-10 needs one: the cap lift without SS-2, with the donut and the bend-point change).
   - **Revenue and incidence:** in-window trust-fund revenue (SS-10 drops SS-2's $0.75-1.2T), who pays, and the D3 test for the bend-point change.
   - **Durability and timing:** a 67-vote law in 2029 against a majority-rule law in spring 2030, the OASI depletion date (about 2032, as reported), and the floor days each uses.
   - **Interaction with D2:** whether pursuing SS-10 first weakens the "credible threat" of the D8 fallback, which rests on D2's graduated cloture being in place.
2. **SSA actuarial score** of the D8 package as a whole (needed for every path).

## Design-rule check

| Rule | How this file meets it |
| --- | --- |
| Durable instruments | Statute; an existing trust fund kept whole (D4). SS-10 adds the durability of a supermajority |
| Legibility | Minimum benefit and COLA visible on statements |
| Pairing | Solvency (structural) moves with a visible benefit for the lowest earners |
| Every number has a basis | Tagged; the package needs an SSA actuarial score, and so does SS-10 |

## Sources

- [SSA Office of the Chief Actuary, letter to Sen. Sanders, Feb 13, 2023](https://www.ssa.gov/OACT/solvency/BSanders_20230213.pdf): +2.46, +1.93, +0.92, −1.46, −0.41, −0.11, −0.05; 3.42% baseline deficit
- [SSA actuaries, provision E2.16](https://www.ssa.gov/oact/solvency/provisions/charts/chart_run424.pdf): +2.35 with benefit credit
- sources/revenue-channels-and-full-menu.md: 2026 Trustees 4.42% deficit, 2034 depletion, 83% payable; CBO $1.6T for the $250K threshold
- [CRFB on the 2019 Social Security Expansion Act](https://www.crfb.org/blogs/bernie-sanderss-social-security-expansion-act): provision shares of the shortfall, for comparison
- [Sen. Moreno, "Moreno, Warren NYT op-ed: lift the Social Security cap" (June 23, 2026)](https://www.moreno.senate.gov/press-releases/moreno-warren-nyt-op-ed-lift-the-social-security-cap/) and [Sen. Warren's release (June 23, 2026)](https://www.warren.senate.gov/newsroom/press-releases/warren-moreno-pen-nyt-op-ed-our-bipartisan-plan-to-save-social-security/): the framework and the legislation in development
- [Rep. Larson's statement on the Warren-Moreno framework (June 2026)](https://larson.house.gov/media-center/press-releases/larson-commends-senators-warren-and-moreno-bipartisan-breakthrough): OASI depletion "in as little as six years" (as reported)
- sources/scenario-talarico-2029-2037.md: the modeled 2029 sequence and trade (scenario, not a score)

**Calendar evidence note (October 23):** Earlier felt/floor-day labels in this file are planning assumptions unless tied to an adopted effective date. Current scenario scheduling is in `index/calendar-scenarios.md`; the separate delivery-opportunity screen is in `index/calendar-delivery-opportunities.md`. Earlier enactment does not itself establish implementation, reach or household receipt. Adopted designs, launch dates and fiscal profiles are unchanged.
