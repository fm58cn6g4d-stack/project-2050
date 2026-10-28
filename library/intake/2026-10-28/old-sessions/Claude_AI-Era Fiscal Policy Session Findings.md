# AI-Era Fiscal Policy: Session Findings

Oct 19, 2026 · @espen

## Overview and bottom line

A token tax is a useful price signal but a small revenue source: even a redesigned, aggressive version raises roughly $55–180B over ten years, against a payroll-tax hole that is 5 to 20 times larger. This session started from the Bridgewater op-ed (Jensen and Bar Dea, NYT, Aug. 14, 2026) and worked through what an AI token tax would look like, how much it would raise, what AI displacement could cost the payroll tax base, and which reforms could plausibly fill the gap.

Headline conclusions:

- **Narrow token tax:** an API-only, origin-based tax raises about $250M–1.2B a year at 2026 volumes. It is a rounding error in a federal budget near $5 trillion.
- **Redesigned token tax:** taxing subscription allotments, sourcing at place of use and using a 15% rate gives about $2.5B in 2026 rising to about $22B in 2035, roughly $109B cumulative (range $55–180B).
- **Payroll tax exposure:** my first estimate (28% job displacement by 2035, about $2T lost) was too aggressive. Recalibrated to 10–15% displacement, the ten-year loss is roughly $0.8–1T.
- **Better revenue levers:** CAMT expansion ($400–700B), lifting the Social Security wage cap ($2.7–3.4T gross) and a VAT dwarf the token tax. The Social Security piece cannot go through budget reconciliation.
- **Social Security fix:** a compressed top bend point preserves the "earned benefit" logic while capturing most of the no-credit revenue. In the CRFB Reformer stack you built, it lands near 124% of the 75-year gap closed and about 93–96% in year 75.
- **Confidence:** the token-tax and payroll-loss figures are my own models built on published anchors, not scored estimates. Section 7 lists what is sourced and what is not.

## The token consumption tax

The op-ed treats the price of a token as the closest thing to a wage for machine labor, and proposes taxing it so the tax code stops favoring machine labor over human labor. The authors leave the mechanics open, so this section sets out one workable design and what it would raise.

### Original design (API-only)

- **Base:** metered API token spend by businesses. Flat-fee consumer subscriptions fall outside it.
- **Collection:** the model provider collects at billing, like a telecom excise tax or marketplace-facilitator sales tax.
- **Open problems the authors flag:** tokens are not comparable across models, offshore or self-hosted models invite evasion, and a firm can replace domestic workers with overseas models and pay neither tax.
- **Revenue:** the metered foundation-model API market was about $12.5B globally in 2025, so a U.S. base of $8–12B in 2026. At 3–10% that is roughly $250M–1.2B a year.

### Revised design

- **Subscriptions taxed on allotment.** Each consumer or business plan is taxed on the usage value it includes, priced at the provider's own API rate card, whether or not the subscriber uses it. This closes the loophole where heavy users move to flat-rate plans.
- **Taxed at place of use.** Nexus follows the location of the end user or billing entity, not the server or the provider's headquarters. Any provider serving U.S.-billed users must register and remit, as under state marketplace-facilitator laws.
- **Rate:** 15% headline, bracketed 10–20%.

### Ten-year revenue (base case)

I started from Gartner's AI model spend of $32B in 2025 rising to nearly $60B in 2027 (global, API and subscription combined), extended it with a decelerating growth curve, assumed a 50% U.S. share, and let collection efficiency improve from about 75% to 90% over the decade.

| Year | Global usage-based AI spend | U.S. base (50%) | Effective rate collected | Federal revenue |
| --- | --- | --- | --- | --- |
| 2026 | $44B | $22B | \~11% | \~$2.5B |
| 2027 | $60B | $30B | \~12% | \~$3.5B |
| 2028 | $81B | $41B | \~12% | \~$4.9B |
| 2029 | $105B | $53B | \~12.5% | \~$6.5B |
| 2030 | $134B | $67B | \~13% | \~$8.5B |
| 2031 | $168B | $84B | \~13% | \~$11B |
| 2032 | $205B | $103B | \~13% | \~$13.5B |
| 2033 | $246B | $123B | \~13.5% | \~$16.5B |
| 2034 | $288B | $144B | \~13.5% | \~$19.5B |
| 2035 | $331B | $166B | \~13.5% | \~$22B |

Base-case cumulative revenue is about $109B. Varying the rate (10–20%), U.S. share (40–55%) and compliance ramp gives $1–4B in 2026 widening to $10–35B in 2035, and $55–180B cumulative.

### What the model leaves out

- **Demand response.** The growth curve assumes untaxed adoption. A 15% tax on a product whose price is falling fast probably slows growth by single-digit points a year, more for consumer plans than for embedded enterprise use, so the base case is likely somewhat high.
- **Scale.** At $22B a year in 2035, spread over roughly 260 million adults, a dividend would be under $100 per person. That is a behavioral lever and modest revenue supplement, not a funding source for a universal AI dividend.

## Payroll tax revenue lost to AI displacement

A realistic ten-year loss is roughly $0.8–1T, about 5 to 20 times what the redesigned token tax would raise. This is a much shakier estimate than the token tax because there is no metered data behind it.

### Starting point

Federal payroll tax (Social Security plus Medicare, employer and employee) brought in about $1.69T in fiscal 2025. Social Security's 12.4% applies only up to a $184,500 cap in 2026, while Medicare's 2.9% is uncapped. That makes Medicare the more exposed leg if displacement concentrates in white-collar work.

### First pass, and why I retracted it

- **Assumption:** Bridgewater's claim that 18% of U.S. jobs could be displaced within five years, extended to about 28% by 2035, with half of displaced wages permanently lost to the tax base.
- **Result:** about $27B lost in 2026 growing to about $344B in 2035, roughly $1.96T cumulative (range $1.2–2.7T).
- **Why it was too high:** Bridgewater's figure is at the top of the published range. Goldman Sachs puts direct displacement risk at 6–7% of the workforce, and a roughly 30-source average clusters near 6% by 2030, with a range of 0–18%. Measured AI-attributable job loss through mid-2026 is about 0.5%, far below the 3% I assumed for 2026. I also treated gross displacement as if it were net job loss.

### Recalibrated estimate

- **Displacement:** 10–15% cumulative by 2035, with 28% kept only as a tail scenario.
- **Ten-year loss:** about $800B–1T, roughly half the first-pass figure.
- **Comparison:** the redesigned token tax recovers somewhere between 5% and 20% of that loss, so the qualitative conclusion survives the lower estimate.

Nobody has a good model of this yet. The forecasting institutions themselves report wide disagreement, and the labor-market data covers about 18 months of a technology that keeps changing.

## Reform options and the stacked package

The most plausible near-term revenue moves build on existing law, not on a new AI-specific levy. The largest lever, lifting the Social Security wage cap, is also the one that cannot use the fast track.

### Menu of options

| Option | What it does | Scale and feasibility |
| --- | --- | --- |
| Lift Social Security wage cap | Applies the 12.4% tax to all wages, ending the exemption above $184,500 | $2.7–3.4T gross over 10 years (my recollection, not scored this session); politically contested |
| Federal VAT | Taxes consumption regardless of whether a human or a model produced it | $2–4T over 10 years at 5–10%; regressive without a rebate; dead on arrival for decades |
| Corporate Alternative Minimum Tax (CAMT) expansion | Strengthens the 15% minimum tax on book income | $400–700B over 10 years versus a $222B baseline; most shovel-ready |
| Automation depreciation reform | Slows bonus depreciation for AI and robotics capital, removing a subsidy for displacement | Small revenue, but fixes an existing distortion |
| Sovereign equity dividend | Government acquires stakes in AI firms and distributes shares, Alaska Permanent Fund style | No federal precedent; closest to the op-ed's own proposal |
| Pillar Two coordination | Prevents profit and IP shifting offshore | A necessary companion to any of the above |

### CAMT expansion

- **Current law:** a 15% minimum tax on adjusted financial statement income for firms averaging over $1 billion (or $100 million U.S. income for foreign-parented groups). About 150 companies owe it.
- **Levers:** lower the threshold to $250–500M, reverse the carve-outs, raise the rate, and extend coverage to large pass-through AI infrastructure vehicles.
- **Headwind:** since early 2025 Treasury has issued a run of interim notices weakening CAMT, including a higher safe-harbor threshold and delayed applicability dates. Senate Democrats have objected, but guidance needs no congressional approval, so only legislation can reverse it.

### Stacking CAMT, the token tax and the wage cap

| Mechanism | 10-year range | Base case |
| --- | --- | --- |
| CAMT expansion | $400–700B | \~$550B |
| Token tax (revised design) | $55–180B | \~$110B |
| Eliminate Social Security wage cap | $2.7–3.4T | \~$3.1T |
| Combined | $3.2–4.3T | \~$3.75T |

The three bases do not overlap, so they add. Combined revenue exceeds even the unadjusted $1.96T payroll-loss estimate and is three to four times the recalibrated $1T figure.

### Procedure: what can ride reconciliation

- **CAMT and the token tax** are ordinary tax law, eligible for budget reconciliation at 51 votes.
- **Social Security changes** are barred from reconciliation by the Byrd Rule, which excludes changes to Title II of the Social Security Act. They need 60 votes under regular order.
- **If the legislative filibuster were eliminated outright,** Social Security reform could pass at 51 votes as ordinary legislation, because the bill would no longer need reconciliation. A narrower carve-out helps only if Social Security is inside its stated scope.

The realistic path is therefore two vehicles: a reconciliation package of CAMT and the token tax (about $650–900B), and a separate, larger Social Security bill.

## Social Security: uncapping design

The design choice that matters most is how much future benefit the newly taxed earnings buy. A compressed top bend point keeps the contributory logic while capturing most of the revenue of a no-credit design.

### The problem and the proposal

- **Trust fund dates:** the 2026 Trustees Report projects the OASI fund depleted in Q4 2032 (about a 22% across-the-board cut) and the combined OASDI funds by 2034.
- **Gap:** the 75-year deficit is 4.42% of taxable payroll, up from 3.82% a year earlier, driven by lower fertility and immigration assumptions and lower income-tax revenue from benefits.
- **Warren-Moreno:** Senators Elizabeth Warren (D-MA) and Bernie Moreno (R-OH) published a joint NYT op-ed in late June 2026 calling for removing the payroll tax cap. They say they are working on legislation, and no bill text has been introduced. Per the Social Security actuaries, uncapping alone would close only about two-thirds of the long-run gap.

### Credit versus no credit

Two independent choices define an uncapping bill: how much income is taxed (full elimination or a donut hole between the current cap and a higher threshold such as $250,000) and whether the new earnings count toward benefits.

- **With credit:** earnings above the old cap enter the benefit formula normally. This preserves the "earned insurance" framing but creates large future benefit liabilities. It closes about 48% of the 75-year gap.
- **No credit:** the tax is collected but buys no benefit. It closes roughly 58–67%, because no offsetting liability is created.
- **Ten-year revenue is nearly identical under both.** I first presented the no-credit figure as lower, which was an error. I had compared a Trustees ten-year collections number to a figure I derived from a 75-year actuarial balance. The designs diverge only decades out, when today's high earners retire.

### Avoidance and compensation restructuring

Uncapping raises the payoff to shifting pay out of the wage base. The main channels:

- **S-corporation salary versus distributions:** the largest existing lever. Owners set "reasonable" salary low and take the rest as FICA-free distributions.
- **Incentive stock options:** exempt from FICA at exercise, unlike non-qualified options and RSUs.
- **Carried interest and capital-gains characterization:** pay recast as investment return.
- **Fringe benefits:** employer retirement contributions and health premiums sit outside the FICA base.
- **Deferred compensation:** a smaller lever, because Section 3121(v) taxes it at vesting.

Estimates of the elasticity of taxable income for high earners cluster around 0.3–0.5, a real but modest haircut on static scores. The much larger 1998 Heritage/WEFA offset is an outlier. A bill that also tightens the S-corp reasonable-compensation standard and treats ISO exercises like non-qualified options would close most of the leakage.

### The hybrid: a compressed top bend point

The benefit formula already pays a declining share of average indexed earnings across two bend points, 90% then 32% then 15%. The hybrid adds a fourth bracket at the old cap with a marginal replacement rate of about 2–5% instead of 15%.

- **Fiscal effect:** it recovers most of the gap between the credit and no-credit versions, likely closing the low-to-mid 60s percent of the long-run gap, by my rough extrapolation.
- **Political effect:** it keeps a real if small marginal credit, so the program still reads as earned. That matters more to its durability than the fiscal difference between a 5% and a 0% rate. It also softens the objection from near-retirees who would otherwise pay on earnings that buy nothing.
- **Likely landing point:** given Moreno's involvement, I expect any bill to look closer to this than to a pure no-credit design, but that is my inference and not reported.

## The CRFB Reformer package

Your twelve-provision stack closes 111% of the 75-year gap with full benefit credit and 128% with none; swapping in the hybrid bend point lands at about 124%, just short of full sustainability in year 75. The two saved Reformer runs differ only in the tax-max option, so the comparison isolates that one choice.

### The stack

Eleven provisions contribute the same 67 points in both runs:

| Provision | % of gap closed |
| --- | --- |
| Slow benefit growth for top half of earners | 38% |
| Increase payroll tax by 0.8% | 19% |
| Means-test benefits for high earners | 17% |
| Apply benefit formula to annual earnings | 9% |
| Cover newly-hired state and local workers | 5% |
| Tax all benefits for retirees making over $100,000 | 3% |
| Repeal the retirement earnings test | 1% |
| Index COLAs to CPI-E | -11% |
| Establish a basic minimum benefit | -6% |
| Provide earnings credit for child care | -5% |
| Expand widow(er) benefits to 75% of a couple's combined benefit | -3% |
| Subtotal, eleven provisions | 67% |

The four negative items are deliberate add-backs that protect lower earners and caregivers at a cost to solvency.

### Tax-max options and the hybrid

The tool offers only two options. I treated the marginal replacement rate on newly taxed earnings as the variable, from 15% (full credit) down to 0% (no credit), and assumed gap closure moves linearly between the two published points, which is about 1.13 points per point of rate. A 2–5% rate gives roughly 56–59%, and I used 57% as a midpoint.

|  | Full credit | Hybrid bend point | No credit |
| --- | --- | --- | --- |
| Tax-max provision alone | 44% | \~57% | 61% |
| 75-year average, all provisions | 111% | \~124% | 128% |
| Year 75 | 79% | \~93–96% | 100% |

The tool shows "sustainably solvent" only when year 75 reaches 100%. The hybrid package is solvent over the 75-year window but leaves a small residual gap in the final years. A modest adjustment to means-testing, state and local coverage or the payroll rate increase would probably close it.

### Remaining levers outside the stack

- **Dedicated investment-income tax:** an earmarked tax on investment income, worth roughly 10% of the gap by my rough estimate.
- **Partial trust fund equity investment:** a larger yield improvement, as Canada's CPP Investment Board has pursued since 1999, but exposed to market volatility.
- **Chained CPI and retirement-age changes:** each worth mid-to-high teens percent of the gap, with the distributional concerns that come with them.

The Social Security actuaries note that provisions interact, so the percentages do not sum cleanly in every combination. The Reformer handles this in the saved runs, but my interpolated figures sit outside that check.

## Caveats, corrections and open questions

The headline figures here are my own models resting on a few published anchors, so treat them as order-of-magnitude. The table separates what came from sources from what I built or recalled.

| Figure | Basis | Confidence |
| --- | --- | --- |
| Trust fund depletion dates (OASI Q4 2032, OASDI 2034), 4.42% deficit | 2026 Trustees Report, via SSA, CRFB and CRR coverage | High |
| Warren-Moreno op-ed and its stated aims | Senator press releases and news coverage, June–July 2026 | High; no bill text exists yet |
| CAMT threshold, Treasury notices, $222B baseline | News and policy coverage found in search | Medium-high |
| Global AI spend figures (Gartner, IDC) | Published forecasts found in search | Medium |
| Token tax ten-year table | My model on those anchors; U.S. share, growth curve and collection ramp are assumptions | Low-medium |
| Payroll tax loss | My model on Bridgewater's and others' displacement estimates | Low |
| Wage-cap revenue ($2.7–3.4T), VAT scale, CAMT expansion range | Recalled or derived by me, not re-verified this session | Low-medium |
| Hybrid bend-point closure (\~57%, \~124%) | My linear interpolation between two Reformer data points, not a CRFB-scored result | Low-medium |

### Corrections made during the session

- **Displacement path:** my 28% by 2035 scenario was too aggressive and was recalibrated to 10–15%.
- **Credit versus no-credit revenue:** I wrongly showed the no-credit design raising less in the first decade. The two raise about the same in ten years and diverge over 75.
- **Bend points:** the formula thresholds I quoted may be 2025 values rather than 2026. Check SSA's current figures before citing them.
- **Benefit-cut figures:** the 22% cut applies to OASI alone at its 2032 depletion; the Reformer's 17% figure refers to the theoretically combined funds in 2034.

### Open questions and next steps

1. Build a small model that applies a custom top bend-point rate to SSA's earnings-distribution data, replacing the linear interpolation with a real estimate.
2. Pull SSA actuary and CBO scores for the wage-cap and CAMT figures so every line in the stacked package has a source.
3. Model demand response in the token tax, since a 15% rate on a falling-price product likely slows adoption.
4. Decide whether the Social Security package is modeled as a standalone bill on the 60-vote track or under a filibuster-reform scenario, since the reconciliation route is closed to it.
5. Watch for Warren-Moreno bill text, which will settle whether it credits benefits, uses a donut hole, or adds a bend point.

### Sources

- [Bridgewater op-ed, "These A.I. Policies Will Hurt Our Business. We Should Do Them Anyway." (NYT, Aug. 14, 2026)](https://www.nytimes.com/2026/08/14/opinion/ai-policy-tax-technology.html)
- [CRFB analysis of the 2026 Social Security Trustees Report](https://www.crfb.org/papers/analysis-2026-social-security-trustees-report)
- [Center for Retirement Research, 2026 financial outlook update](https://crr.bc.edu/social-securitys-financial-outlook-the-2026-update-in-perspective/)
- [SSA Office of the Chief Actuary, solvency provisions](https://www.ssa.gov/oact/solvency/provisions/summary.pdf)
- [Warren-Moreno op-ed press release (Sen. Warren)](https://www.warren.senate.gov/newsroom/press-releases/warren-moreno-pen-nyt-op-ed-our-bipartisan-plan-to-save-social-security/)
- [ABC News on the Warren-Moreno proposal](https://abcnews.com/Politics/social-security-fix-proposed-sens-elizabeth-warren-bernie/story?id=134253518)
- [CRFB Social Security Reformer](https://www.crfb.org/socialsecurityreformer/) (the two saved runs you attached)
