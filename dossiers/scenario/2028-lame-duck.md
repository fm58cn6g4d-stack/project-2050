# The 2028 lame duck and the OBBBA expirations

Role: what in the 2025 reconciliation law (Public Law 119-21, "OBBBA") expires at the end of 2028, what extending each piece would cost, and what the November-December 2028 lame duck is likely to do with it under each 2028 outcome. It also covers what that means for the FY2029 baseline Project 2050 starts from, and for D3's leverage in the divided case of `house-stress-test-2029.md`. Status: draft (stage B follow-up), November 8, 2026. **Analysis only.** It changes no adopted fiscal input; section 4 flags what would. D1 (#80) and D3 are Espen's.

**What kind of evidence this is.**
- **Expiry dates:** from the statute itself [SRC-1096].
- **Costs:** JCT's estimates, sent with CBO's letter of August 4, 2025 to the Senate Budget Committee's ranking member [SRC-1093]. They are measured against CBO's January 2025 baseline, so CBO's later baselines will re-estimate them.
- **One secondary source:** the senior deduction's income phase-out comes from a summary [SRC-1094], not the statute text.
- **The lame-duck scenarios:** this project's analysis.
- **Administration sources:** no figure here comes from the administration. Treasury and the Council of Economic Advisers under the second Trump administration have published claims about who gains from these deductions. Under `DEC-2026-10-30-01` those would be that administration's view, not evidence, and none is used.

## In brief

- **Four household deductions end after tax year 2028:** no tax on tips, no tax on overtime, car-loan interest, and the $6,000 deduction for people 65 and over (statute). Five other provisions also end after 2028 or 2029: the $1,000 children's account pilot, expensing for factories, the higher SALT cap, the clean fuel credit and a small film and sound-recording rule.
- **What extending them would cost (JCT, August 2025):**
  - **The four household deductions:** $33 billion in FY2029, because only part of that year's tax receipts is affected, then $68-73 billion a year. That is $384 billion over FY2029-34, about 0.18% of GDP a year once fully phased in.
  - **All ten temporary provisions that CBO and JCT costed:** $787 billion over the same years, $166 billion in FY2034, or 0.38% of GDP.
- **Who holds the cards in the lame duck.** The 2027-28 Democratic Congress sits until January 3, 2029, and President Trump until January 20.
  - Any extension needs Trump's signature, and 60 Senate votes, which needs Republicans, or a reconciliation bill.
  - Reconciliation would need a Democratic budget resolution written for it, which Democrats would not offer.
  - So a lame-duck deal is one the Democratic Congress chooses to write and Trump chooses to sign.
- **The likely lame duck, by outcome (analysis):**

  | 2028 outcome | Likely lame duck | Starting baseline for 2029 |
  | --- | --- | --- |
  | Democratic trifecta | No deal; the provisions lapse, and the new government decides in its own reconciliation bills | Current law, the adopted baseline: no change |
  | Democratic president and Senate, Republican House | The highest-stakes case: lapse, keeping the leverage, or a Democratic-designed extension that Trump signs | Lapse, unless the outgoing Congress spends the leverage |
  | Republican president, Democratic Senate | A standoff. Republicans cannot pass a 2029 reconciliation bill without the Senate, so the provisions lapse unless Democrats trade for something | Lapse, with a likely 2029 deal that would lower revenue |

- **D3's leverage in the divided case.**
  - Once the provisions lapse, Republicans need a Democratic Senate and a Democratic president to bring back their signature tax cuts.
  - That makes the lapse the strongest bargaining chip the divided case has. `house-stress-test-2029.md` found that reconciliation is lost in this case.
  - D3 only has that leverage if its position is settled before November 2028. That means deciding which extension, if any, passes the household test, and what it would be traded for.
- **The flag for Codex.** The adopted baseline is CBO's February 2026 current-law baseline with two tariff adjustments, and it assumes the provisions lapse. A permanent lame-duck extension would call for a new revenue adjustment in `models/tools/fiscal-data.py`, about −$33 billion in FY2029 and −$68 to −$73 billion a year after (section 4). This note does not make it.

## 1. What expires, and what extending it costs

Costs are JCT's estimates of the added deficit from making each provision permanent, in billions by fiscal year, from CBO's August 4, 2025 letter, Table 2 [SRC-1093]. They run against CBO's January 2025 baseline and exclude interest.

| Provision (P.L. 119-21 section) | What it does | Ends | FY2029 | FY2030 | FY2034 | FY2029-34 |
| --- | --- | --- | --- | --- | --- | --- |
| No tax on tips (70201, new IRC 224) | Deduct up to $25,000 of qualified tips; phases out above $150,000 of modified AGI ($300,000 joint); SSN required | "Any taxable year beginning after December 31, 2028" [SRC-1096] | 3 | 9 | 11 | 52 |
| No tax on overtime (70202, new IRC 225) | Deduct up to $12,500 ($25,000 joint) of FLSA overtime premium pay; same phase-out | Same wording [SRC-1096] | 15 | 24 | 25 | 137 |
| Car-loan interest (70203, IRC 163(h)(4)) | Deduct up to $10,000 of interest on a loan for a new, US-assembled personal vehicle; phases out above $100,000 ($200,000 joint) | Taxable years "before January 1, 2029" [SRC-1096] | 6 | 11 | 13 | 66 |
| Senior deduction (70103, IRC 151(d)(5)(C)) | $6,000 more for each person 65 or older; phases out above $75,000 ($150,000 joint) [SRC-1094] | Taxable years "beginning before January 1, 2029" [SRC-1096] | 9 | 24 | 24 | 129 |
| **The four household deductions** | | **End of 2028** | **33** | **68** | **73** | **384** |
| Children's accounts and the $1,000 pilot (70204) | $1,000 deposit for children born 2025-2028 | End of 2028 | 4 | 4 | 4 | 22 |
| Expensing for qualified production property (70307) | 100% first-year write-off for new factories | Construction begun before 2029 | 5 | 15 | 39 | 163 |
| SALT cap at $40,000 (70120) | Higher cap on the state and local tax deduction | After 2029, back to $10,000 | 0 | 17 | 37 | 165 |
| Clean fuel production credit (70521) | Extended credit | After 2029 | 0 | 5 | 13 | 53 |
| Sound-recording expensing (70434); carbon-sequestration limit (70522) | Small | 2028-29 | * | * | * | 1 |
| **All ten provisions** | | | **42** | **108** | **166** | **787** |

**Reading the costs.**
- **The fiscal-year pattern.** FY2029 shows only part of tax year 2029 (refunds come in calendar 2030), which is why the household deductions jump from $33 billion to $68 billion.
- **Interest.** CBO puts the added interest on the full ten-provision extension at $789 billion with the enacted law, against $718 billion without it, over 2025-34. So the extension adds about $71 billion of interest in that window [SRC-1093].
- **Later baselines.** CBO's February 2026 baseline, which the project uses, will have re-estimated all of these. JCT's August 2025 numbers are the latest per-provision extension costs found. CBO's or JCT's next estimates should replace them when published.

**Not on the 2028 list.**
- The enhanced child tax credit, the standard deduction, the rate structure and the expensing of equipment are permanent in P.L. 119-21. They are not in CBO's list of ten temporary provisions [SRC-1093]; their sections were not re-read here.
- The SALT cap's reversion and the clean fuel credit come a year later, so they belong to the 2029 Congress, not the lame duck.

## 2. The lame duck: who sits where

| Who | November 6, 2028 to January 3, 2029 | After January 3, 2029 |
| --- | --- | --- |
| House | Democratic (the 2027-28 Congress; about 259 seats, `1-results.md`) | Decided in 2028 |
| Senate | Democratic, short of 60 | Decided in 2028 |
| President | Trump, to January 20, 2029 | Decided in 2028 |

**Routes for an extension in the lame duck.**
- **Regular order:** House passage, 60 votes for cloture in the Senate, and Trump's signature. That needs Republicans in the Senate and a Democratic decision to bring the bill up.
- **Reconciliation:** a FY2029 budget resolution with tax instructions, which the Democratic Congress would have to write. Using its own reconciliation bill to extend Trump's deductions would also cost Democrats the FY2029 slot. It is not a realistic route (analysis).
- **So:** in the lame duck, Democrats decide whether anything passes, and Trump decides whether it becomes law.

**What else is in the lame duck (analysis).**
- **FY2029 appropriations:** probably on a continuing resolution into December, since fiscal year 2029 begins October 1, 2028. The FY2029 level sets the floor for the 2029 government (D9 in `4-2029-plan.md`).
- **A tax package:** any expiring-provision package is likely to ride with that spending bill.
- **Retroactive repair:** a lapse on January 1 can be repaired retroactively in early 2029. The American Taxpayer Relief Act of 2012 was signed on January 2, 2013 and applied from January 1 [SRC-1095]. So a lapse is a bargaining position, not an irreversible loss.
- **What a lapse does affect:** withholding tables for 2029, and how tax-year 2029 returns are filed. Those matter for how households feel the change.

## 3. Three 2028 outcomes

### A. A Democratic trifecta

- **Likely lame duck: nothing passes, and the provisions lapse.**
  - The incoming government gets the provisions in its own reconciliation bills (D5), where they can be redesigned under D3, so it has no reason to spend Democratic votes on Trump's versions in December.
  - Trump has no route to pass them without Democrats.
  - A short one-year patch is possible if withholding disruption becomes a political problem. It would have to be written by Democrats and signed by Trump.
- **The FY2029 baseline: current law, as adopted.** R1 and R2 then choose what, if anything, replaces each deduction.
  - Restoring the four household deductions permanently costs about $68-73 billion a year from FY2030.
  - That money would come out of the same envelope as the secure floor and care flagships.
- **For D3:**
  - The question is design. The deductions are worth nothing to workers with no income-tax liability, and they phase out at fixed incomes.
  - A refundable credit would reach the households D3 is meant to protect. It could be the secure floor's child benefit or income support, or a capped work credit.
  - That choice can be made inside R1 or R2 without lame-duck pressure.

### B. A Democratic president and Senate, with a Republican House (the stress case)

This is the case `house-stress-test-2029.md` puts at about 11% of Democratic-president runs. Reconciliation is lost for 2029-30, because a Republican House will not adopt a Democratic budget resolution and a Democratic Senate will not adopt a Republican one.

**Two lame-duck choices for the outgoing Democratic Congress.**

| Choice | What happens | What it does to D3's leverage |
| --- | --- | --- |
| **Lapse** (no lame-duck bill) | On January 1, 2029, tips, overtime, car-loan interest and the senior deduction end. The new Republican House wants them back but cannot reconcile, so it needs 60 Senate votes and the Democratic president's signature | **Kept, and at its peak.** The deductions are Republicans' signature tax cuts. Restoring them becomes a trade the Democratic Senate and president can price under D3: for example a refundable version, a pairing with a secure-floor or care item, or top-end revenue to pay for it |
| **A Democratic-designed extension that Trump signs** | The outgoing Congress writes the version D3 prefers, for example capped, refundable and paid for, and offers it to Trump before he leaves | **Spent.** It locks in the design, but it gives up the one bargaining chip the divided government would have against the House. Trump might also refuse a paid-for version |

**Likely (analysis): lapse.**
- **The other levers are weak.** In the divided case they are appropriations at the FY2029 base, nominations, executive action, and possibly a debt limit if one binds. The expirations are the only lever that runs in the Democrats' favor.
- **The risk of lapse:** the change hits withholding in January 2029, and Republicans will call it a tax increase. That makes D3's public position, set in advance, part of the strategy.

**The FY2029 baseline:** lapse at first. Then a likely 2029 deal that restores some deductions in exchange for Democratic items. Its revenue cost depends on the design. The project's starting baseline holds until that deal.

### C. A Republican president with a Democratic Senate

**Likely lame duck: a standoff, then lapse.**
- `2028-republican-branch.md` finds that a Democratic Senate blocks a 2029 Republican reconciliation bill, because the budget resolution needs both chambers.
- In the lame duck, the outgoing Democratic Congress has no reason to extend the deductions for an incoming Republican president without a price.
- In 2029, a Republican president and, likely, a Republican House need the Democratic Senate's 60th vote, or several Democratic votes, to restore them.

**What a trade could look like (analysis):**
- the lapsed household deductions for items the Democratic Senate values, such as the ACA premium credits (CBO: permanent extension $350 billion over 2026-35 [SRC-0850]) or appropriations levels;
- the SALT cap's 2029 expiry adds a second Republican priority to the same bargain.

**The baseline:** this branch does not use Project 2050's 2029 ledger. It matters for what a 2033 government would inherit (`2030-2034-control.md`).

## 4. What it means for the FY2029 baseline (flagged, not changed)

**The adopted input.**
- **What it is:** CBO's February 2026 ten-year and long-term baselines, adjusted for the tariff ruling (ADJ-T1) and the remaining tariff refunds (ADJ-T2) (`models/tools/fiscal-data.py`; `build/fiscal-long-term-model.md`).
- **What it assumes:** CBO's baseline is current law, so it assumes every provision in section 1 lapses on schedule.

**What would change it, for Codex to decide; nothing is changed here.**
1. **A permanent lame-duck extension of the four household deductions** would need a third adjustment to individual income tax revenue.
   - **Size:** about −$33 billion in FY2029, then −$68 billion (FY2030) to −$73 billion (FY2034), and about 0.17-0.18% of GDP after that.
   - **Interest:** it would carry its own interest.
   - **The fiscal gap:** the gap of holding debt at its 2029 ratio, 2.48% of GDP, would rise by roughly that share.
2. **Extending all ten provisions** would be about −$42 billion in FY2029, rising to −$166 billion (0.38% of GDP) by FY2034.
3. **A one-year patch** would move only FY2029 and FY2030 (about −$33 billion and part of −$68 billion). That is within the model's noise but should be logged.
4. **A 2029 deal in case B or C** would enter as a policy line in the ledger, not as a baseline change. Whether a deal struck by others belongs in the baseline or in the ledger is a convention for Codex to set.

**When to check.** Re-read the estimates when CBO publishes its 2027 and 2028 baselines, which will re-estimate the provisions, and again after the lame duck.

## 5. D3 in the divided case: what has to be decided before November 2028

`4-2029-plan.md` already flags whether any extension passes the household test, decided before the 2028 fight. In the divided case that becomes the negotiating position. Options for Espen, not recommendations:

| Option | Position going into 2029 | Fits D3 because | Risk |
| --- | --- | --- | --- |
| a. **No restoration** | Let all four lapse; spend the money elsewhere | Revenue is kept for the floor and care flagships | Read as a tax increase on tipped and hourly workers and seniors; gives up the trade |
| b. **Convert, not restore** | Offer a refundable, capped work credit and a senior credit in place of the deductions, at about the same cost | Reaches households with no income-tax liability, whom the deductions miss | Republicans may refuse a credit in place of their branded deductions |
| c. **Restore for a price** | Restore some or all as written, but only paired with a Democratic item and top-end revenue | Middle-income households come out ahead on net if the pairing is large enough | The deductions become permanent with their design flaws |
| d. **Decide by design test, not by name** | Set the test now (net gain by income decile, refundability, cost), and let the 2029 negotiators fit any offer to it | Keeps D3 a principle rather than a fixed offer | Weaker as an opening position |

## 6. Limits

- **The costs are JCT's August 2025 estimates against CBO's January 2025 baseline.** CBO's February 2026 baseline, the project's input, will differ, as will CBO's next baselines and any re-estimate after the IRS's first filing season with the deductions.
- **One parameter is secondary.** The senior deduction's phase-out thresholds come from a summary [SRC-1094]; the dollar amount and the expiry come from the statute.
- **The lame-duck outcomes are judgment.** The Senate's 60-vote math and the reconciliation rules are statutory. What Trump would sign, and what a 2029 Republican House would trade, are not.
- **Not covered:** a debt limit that might bind in 2028-29, and FY2029 appropriations in detail. Both affect lame-duck leverage.

## Next questions

1. Run the household test on each of the four deductions, and on option b's credit, before the 2028 fight: the net gain by income decile and refundability. This is a short fair-financing note (`compounding-2029-2050.md`, question 4).
2. Codex: should a lame-duck extension enter the baseline (`fiscal-data.py` adjustments) or the ledger? Set the convention before November 2028.
3. Re-cost the four deductions against CBO's February 2027 baseline when it is published.
4. Check whether a debt limit binds in 2028-29. If one does, it changes case B's leverage.
