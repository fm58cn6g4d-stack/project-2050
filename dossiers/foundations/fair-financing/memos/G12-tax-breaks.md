# Memo G12: Tax breaks the plan hasn't touched

**Decided:** G12.1 C, kept as it is, `DEC-2026-11-24-05` (a question for the later innovation topic); G12.2 yes, `-06`; G12.3 no, `-07`. Booked in stage G step 7 (`../2-settlement.md`, `models/data/inputs/settlement.json`). The memo below is the record of the choice as put to Espen; its figures are the draft's.


Role: decision memo for Espen, fork 12 of stage G, from step 4b's whole-budget scan ([`../3-budget-scan.md`](../3-budget-scan.md) parts A and C, items C7 to C9). Status: **provisional, drafted on the recommendations, November 20, 2026. A new fork.** Not decided, not booked. Nominal $B on case `mixed`, priced by `models/tools/financing-protection/budget_scan.py`. Project arithmetic on exploratory models, not official scores.

## The question

A tax break works like spending through the tax code. The plan's revenue rows already end or cut most of the large ones that go mainly to the top:
- the fossil-fuel breaks, carried interest, like-kind exchanges above $500K (all inside C38);
- the untaxed gains at death (the ledger's row G6, not memo G6);
- the 2025 law's expensing (HS4);
- the low tax on foreign profits (row G7, not memo G7);
- the employer health exclusion (HX).

JCT's latest table shows what is left (the Joint Committee on Taxation, 2025) [EV-FIN-001]. Most of what's left is broad-based and middle-class: pensions, the charitable deduction, the mortgage deduction. Or it falls on states, as tax-free bonds do, or on small business, as the pass-through deduction below $450K does, which you asked the plan to spare (`DEC-2026-11-15-03`).

**Two top-heavy breaks are still untouched.** A third is priced for comparison. Each is decided on its own. G12.1 has three options, because one of the breaks is a start-up incentive and you asked on November 20 to "do more to encourage innovation, entrepreneurship and small business growth".

JCT's figures are not revenue estimates: they hold behavior fixed [EV-FIN-001]. The savings below allow for behavior with a working share, and each needs a JCT score against the post-2025 law before drafting.

| | What | JCT, last year of its window | Saving, FY2040 | FY2056 | Recommended |
| --- | --- | --- | --- | --- | --- |
| **G12.1** | **The small business stock exclusion (sec. 1202):** A end it; **B keep it, but roll back the 2025 law's widening**; C keep it as is | $5.9B | A −6.2 (range 4.4-8.0); **B −2.2** (range 1.3-3.1); C 0 | A about −11; **B about −3.9** | **B** |
| **G12.2** | **End like-kind exchanges entirely,** beyond the booked $500K cap | $10.8B | **−4.9** (range 2.5-7.5) | about −8.6 | **Yes** |
| G12.3 | Cap the mortgage interest deduction at $500K of debt (from $750K) | $54.9B | −14.9 | about −26 | **No** |

**G12.1, the small business stock exclusion.**
- *What it is:* investors who buy stock in a qualifying young company and hold it five years pay no tax on most of the gain, up to large limits.
  - The 2025 law widened it: a higher per-company limit on excluded gains, a larger company size test, and a partial exclusion after three and four years.
  - It is $5.9B in the last year of JCT's window, up from $4.4B in the first [EV-FIN-001].
- **The conflict.** This break is aimed at start-ups: it rewards people who put money into young companies and wait. Ending it (A) cuts against your direction on innovation and small business. Keeping it untouched (C) leaves the 2025 law's extension, which mostly reaches the largest gains in larger companies.
- **A, end it:**
  - −$6.2B in FY2040.
  - *Who loses:* founders, early employees with stock and early investors, mostly at the top, but including the people the incentive is meant for.
- **B, roll back the 2025 widening (recommended):**
  - The exclusion goes back to its pre-2025 terms: the old per-company limit, the old size test, and the five-year hold.
  - About −$2.2B in FY2040. The working share is a quarter of the tax expenditure (range 15-35%); no JCT score of the widening alone was found.
  - *Who loses:* investors with very large gains in larger companies, and those who sell between three and five years.
  - *What stays:* the incentive for founders and early backers of genuinely young companies, as it was before 2025.
- **C, keep it as is:** nothing saved; the 2025 extension stays.
- *The evidence:* whether the exclusion actually raises start-up investment is unsettled, and the register holds no study of it. That is an "Evidence still needed" item. So B is a judgment that the core incentive is worth keeping on your direction, not a finding that it works.
- *The saving* in A and B is likely understated. The plan's higher rates on large gains (HS3, C18) would apply to what the exclusion now shelters. And the 2025 widening applies to stock issued after July 2025, so its cost grows faster than the economy as that stock ages.

**G12.2, like-kind exchanges.**
- *What it is:* a real-estate investor who sells one property and buys another pays no tax on the gain until later. The plan already caps this at $500K of gain a year (REV-TS9, inside C38), which reaches most of the dollars. This ends the rest.
- *Who loses:* real-estate investors with smaller exchanges. Some will hold property instead of selling it, which is why only about 30% of JCT's figure is counted.

**G12.3, the mortgage interest cap (not recommended).**
- *What it is:* interest on mortgages above $500K would no longer be deductible. CRFB puts this cap at about $130B over FY2026-35 (via a search extract).
- *Why not:* it raises housing costs for middle- and upper-middle-income homeowners in high-cost places, against your direction to make life more affordable. The plan already caps the deduction's value above $450K of income (C39).

## Recommendation

**G12.1 B; yes to G12.2; no to G12.3.** Together the first two are about $7B a year in FY2040 (with G12.1 A instead, about $11B). They come from wealthy investors, and no worker's take-home changes. B keeps the start-up incentive your innovation direction points to, and trims only the 2025 law's extension of it.

## Questions for you

**G12.1.** For the small business stock exclusion: keep it, but roll back the 2025 law's widening (B, recommended)? Or end it (A), or keep it as is (C)?

**G12.2.** End like-kind exchanges beyond the booked $500K cap (yes, recommended)?

**G12.3.** Cap the mortgage interest deduction at $500K of debt (no, recommended)?
