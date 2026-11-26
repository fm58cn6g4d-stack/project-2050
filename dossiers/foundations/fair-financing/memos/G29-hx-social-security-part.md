# Memo G29: The Social Security part of the tax on former premiums

Role: decision memo for Espen. It is question I2 from stage G step 11 (#507). You chose C on I2 (`DEC-2026-11-26-02`): source the share first, then set out the options. This memo does both. Status: **decided November 26, 2026: C with R2** (`DEC-2026-11-26-03`) **and booked in #515**, with the HEX fix (finding 3). The figures below are as drafted. Booked, OASDI's part is the sourced 0.28 rather than the working 0.297, so the fund builds $312.7B over FY2030-34, keeps $250B and draws $62.7B, and the FY2035 transfer is $304.6B (drafted: $307.9B, $57.9B and $313.8B). From FY2045 Social Security gets $144B in FY2045 and $248B in FY2056; the general fund still closes, with $19.2B to spare in FY2045. Social Security's funds last to 2069, at −1.17% of taxable payroll, as drafted. The plan's debt is 129.3% of GDP in FY2056 (`../2-settlement.md` part 8).

Nominal $B, mixed case. These are project figures on exploratory models, not official scores. The Social Security results come from the dedicated-fund engine (`models/tools/budget/engine/funds-model.py`), run on the 2026 Trustees' rates. The general-fund and reserve results come from the recovery budget (`models/tools/recovery-budget/model.py`), run in a scratch copy.

## The question

When people's health premiums end, the employer money that paid for them becomes taxable pay. The plan books the tax on that pay as HX. On the net, HX less HEX (the part the employer contribution takes back), that is $358B in FY2040.

That tax is income tax plus payroll tax. Under current law the Social Security (OASDI) part goes to Social Security's trust funds. It can't be health money (`DEC-2026-11-25-12`), so #507 left it out of the health fund and kept it on the general fund, pending your answer.

You have to decide where it goes. The rule that each important effect is booked in its appropriate place (`DEC-2026-11-25-28`) says to book it where the law puts it. The open question is whether the law should leave it with Social Security.

## Your note: isn't this canceled out by the new, larger health contribution?

You asked: "Isn’t this basically canceled out by the new larger health contribution? Maybe not, or maybe at least this isn’t how the budget model thinks about effects?" Both halves of that are partly right.

- **It isn't canceled out.** The health contribution replaces Medicare's HI taxes only: the worker's HI, the 0.9% extra Medicare tax, and HI on former premiums (`models/bookings/health_trust_fund.py`, the fold-in rows HCW, HCA, HCP and HCH). It doesn't touch Social Security's 12.4% tax. And by your rule its money pays only for health (`DEC-2026-11-25-12`). So nothing in it stands in for the Social Security money.
- **Where the Social Security part comes from.** When premiums end, the employer money that paid them becomes wages. Wages under the cap pay Social Security's 12.4%, like any other pay. Current law sends that tax to Social Security's trust funds (42 U.S.C. 401(a)). It is new Social Security revenue that the plan creates, not health money.
- **You are right that the budget's bottom line doesn't care where it goes.** The debt path uses the unified budget, which counts Social Security and the general fund together. The same dollars are collected either way, so under A, B or C the debt held by the public is the same.
- **Two other places do care.**
  - **The general fund.** By law Social Security's money is off-budget, outside the general fund's totals (42 U.S.C. 911(a)). The settlement's test is the general fund's gap. If the money goes to Social Security, the general fund has about $100B a year less in FY2040.
  - **Social Security's trust funds.** If they get the money, they last longer (2072 instead of 2061 under A).
- **So the choice is who gets it, not whether it exists.** That is the question below.

## What this memo finds first

1. **The Social Security part is about 28% of the money, not the 29.7% the booking guessed.** Sourced, the range is about 22-30%.
   - CBO and JCT (December 2024, EV-FIN-094): limiting the exclusion for both income and payroll tax raises $985B over 2025-34, and limiting it for income tax only raises $709B. Payroll is 28% of that partial limit.
   - For the whole exclusion, OMB's and CBO's figures (EV-FIN-095) put payroll at 38% in 2016 and 36% in 2026.
   - About 78% of the payroll part is Social Security's: 12.4 of the 15.3 points, and above the wage cap only Medicare's 2.9% applies. That gives 36% × 0.78 ≈ 28%. On CBO's partial-limit figure it would be about 22%.
2. **The amount is about $100B a year in FY2040, not $290B.** The 28% applies to the net money, HX less HEX. #507 applied it to HX alone, but HEX takes back the same income and payroll tax, so it carries the same Social Security part.
   - FY2030-34: about $78B, not $234B.
   - FY2040: about $100B (range $79-107B).
   - FY2056: about $248B.
3. **#507's booking needs a fix whichever option you choose.** It weights HX at 70.3% in the health fund's sources but leaves HEX at full weight, so the fund is charged for a Social Security take-back it never received. With HEX weighted like HX, as now booked:
   - The fund's reserve as built is **$307.9B**, not $159.5B.
   - The FY2035 transfer is $371.7B, not $497.8B.
   - The general fund's FY2030-39 gap is $776.5B, not $628.1B. The general fund now carries the take-back's Social Security part in FY2031-34.
   - From FY2040 the general-fund gap doesn't move, because the law fixes the general fund's share.
   - **Booked in #515** (`settlement.json`'s `source_shares`, budget model 0.5.0). The rate rule, rerun on the fixed figures, holds 3.80% through FY2043 (it stepped up in FY2041 in #507). It is then 4.05% in FY2044-45, 4.30% in FY2046-47, 4.05% in FY2048-51, 4.30% in FY2052-55 and 4.05% in FY2056.
   - With the new rate path, the plan's debt is 129.4% of GDP in FY2056, against 129.1% in #507. It is 121.5% in FY2045 and 124.7% in FY2050 (121.2% and 124.3%); FY2040 stays 117.8%.

## The options

| | Where the Social Security part goes | Social Security trust funds, with the plan's Social Security package (D8) | General fund |
| --- | --- | --- | --- |
| Today's booking | General fund | Depletion in 2061; 75-year balance −1.64% of taxable payroll | As booked (with the HEX fix) |
| **A** | Social Security, as current law does, from the start | **2072**; −1.07% (range 2070-2073) | About **$100B a year less in FY2040**, $248B in FY2056. FY2035 and FY2040 no longer close ($120B and $86B short). FY2045 on still close. FY2030-39 gap about $1,284B |
| **B** | General fund, by law | 2061; −1.64% | As booked |
| **C** (hybrid) | General fund through FY2044, then Social Security, both written in law | **2069**; −1.17% | As booked through FY2044. From FY2045 it still closes every year (FY2045 about $19B to spare; more after) |

All three leave the general fund's share of health and the debt path's FY2056 figure as they are. The Social Security run counts the revenue only. Higher taxed pay also raises the benefits people earn, which CBO counts, so the long-run gain to the trust funds is somewhat smaller than shown.

**A** keeps current law. Social Security gets 11 more years before depletion and closes about a third of the gap the plan's package leaves. But the settlement stops closing in FY2035-44: about $100B a year has to come from somewhere else. Two possible sources:
- a larger general-fund contribution from the health fund's side, by raising the contribution's fixed share by about a quarter to a third of a point of the rate (not allowed to pay for anything but health, `-12`, so only if health's cost needs it);
- or a little more of the later revenue (G24 B's VAT, re-scored).

**B** keeps the settlement as booked. Social Security gives up those 11 years, about 0.57% of taxable payroll over 75 years. That is about a fifth of what the plan's own Social Security package adds (2.81% of taxable payroll). It is a transfer from Social Security to the general fund, written in law.

**C** gives Social Security most of A's gain (eight of the eleven years). It gives up the money only while the general fund has no room. The cost is a statute that names a temporary redirect, and its end date has to hold.

B and C both need the plan's law to say so expressly. Section 710(b) of the Social Security Act (42 U.S.C. 911(b)) says no later law may move money between the trust funds and the general fund. Congress can still do it in a new law, and has: the 2011-12 payroll tax cut was made good to the trust funds from the general fund. But the plan would have to write it in on purpose.

## The reserve

On the fixed figures, the fund builds **$307.9B** over FY2030-34, after meeting its own FY2033-34 shortfalls. Your decision (`DEC-2026-11-25-31`, point 2) was a $250B standing reserve plus $141B lowering the FY2035 transfer, $391B in all, which was based on figures that counted Social Security's money as health's.

| | Standing reserve | Drawn in FY2035 | FY2035 transfer | Note |
| --- | --- | --- | --- | --- |
| R1. Keep all of it | $307.9B | none | $371.7B | A larger reserve, so the rate rule steps up later |
| **R2. Point 2 as far as the money goes** | **$250B** | **$57.9B** | **$313.8B** | Meets the $250B in full; draws what is left, not $141B |
| R3. Point 2 in full | $250B | $141B | $230.7B | Needs $83B more in FY2030-34 from the general fund, money that isn't health's |

None of A, B or C moves the reserve: each keeps the Social Security part out of the fund.

## Recommendation

**C, with R2.**
- **C.** Your booking rule (`-28`) puts the money where the law puts it. Current law puts it with Social Security, and the plan should change that law only where it must. C changes it only for FY2031-44, while the general fund can't spare it. From FY2045 the money goes back to Social Security, with most of the solvency gain.
- **A** is the clean reading of current law. Its cost is a settlement that no longer closes in FY2035-44, without a source named for $100B a year.
- **B** quietly takes Social Security's money for good. It is the hardest to defend once the money is large, $248B a year by FY2056.
- **R2.** It is point 2 as decided, carried as far as the fund's own money reaches. R3 would need $83B more from the general fund in FY2030-34. Point 2 assumed that money was already health's, but it was Social Security's.

**The HEX fix is booked already (#515).** It was the larger error, and the reserve figures above depend on it.
