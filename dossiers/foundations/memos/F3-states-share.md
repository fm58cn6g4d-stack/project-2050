# Memo F3: What share of their former Medicaid spending states keep paying

Role: decision memo for Espen, fork 3 of the financing checkpoint's health batch (`README.md`; `../checkpoint-financing.md`, part B). Status: **superseded, November 15, 2026, by [`../health-financing.md`](../health-financing.md) (its part 9 holds the new questions); kept for the record.** Earlier status: **for decision, November 14, 2026**. Figures are FY2040, from `models/tools/health_financing.py` (project arithmetic, not an official score). Each option's household figures include the income contribution (memo F1, A) sized to close the rest and memo F2 at A.

## The question

States now pay about $449 billion (2032) of Medicaid for the people who move into the plan. The design has them keep paying a share by a direct obligation in the Act, on the model of Medicare Part D's clawback, collected by offset against federal payments (HLT-7.17; care memo 3 B, `DEC-2026-11-10-11`). Long-term care stays with them (HLT-7.07). The share is a working 50% (range 0-80%), left to the settlement. Each 10 points is about **$69 billion** in FY2040.

**Legal risk, the same for every share above zero** (HLT-7.17): *NFIB v. Sebelius* (2012) held that threatening states' existing Medicaid funds to force a new program was coercive. The clawback is an obligation, not a condition, and has never been decided on the merits. If the payment fails, it ends (hold harmless) and the plan covers the difference, which is option D.

## The options

**A. 50% (the working figure).** States stop paying about $344B a year.
- *Gap:* $0 against the booking; the household contribution is about 16.8%.
- *Households (D3):* Q1 +$6,689, Q2 +$10,465, Q3 +$10,345, Q4 +$3,404; Q5 −$43,885; top 1% −$294,397.
- *Administrative burden:* low (a monthly payment, offset as the clawback is).
- *Political risk:* the most state support.

**B. 80% (recommended).** States stop paying about $137B a year.
- *Gap:* −$207B against A; the household contribution falls to about 15.7%.
- *Households:* Q1 +$6,712, Q2 +$10,703, Q3 +$11,077, Q4 +$4,921; Q5 −$39,551; top 1% −$278,055.
- *Administrative burden:* as A.
- *Political risk:* states still save, so they keep a reason to support the plan, and they also carry new shares in long-term care and child care (care parts B-D).

**C. 100%.** States pay what they pay today for the people who move; no state saves.
- *Gap:* −$345B against A; the household contribution is about 14.9%.
- *Households:* Q1 +$6,727, Q2 +$10,862, Q3 +$11,566, Q4 +$5,932; Q5 −$36,661; top 1% −$267,160.
- *Administrative burden:* as A.
- *Political risk:* governors gain nothing from the move and carry its risks. The larger the payment, the more a court may see the offset as leverage.

**D. Nothing** (as S. 1506; also the fallback if the payment fails in court).
- *Gap:* +$345B against A; the household contribution is about 18.8%.
- *Households:* Q1 +$6,651, Q2 +$10,068, Q3 +$9,124, Q4 **+$875**; Q5 −$51,109; top 1% −$321,633.
- *Administrative burden:* none.
- *Political risk:* the federal tax carries all of it, and states gain about $689B a year, with nothing asked in return.

None of these counts what states do with what they save or must raise. Their own taxes are not in the household model, and most are less progressive than the federal income contribution. A higher state share therefore spends some of the progressivity the federal contribution buys.

## Recommendation

**B.** It keeps a real saving for states (about $137B a year) while lowering the federal household rate by about a point against A, and it keeps the fourth fifth's gain near $5,000. C buys about 0.8 more points at the cost of every state's reason to support the plan. D is the fallback the plan must be able to absorb, and it leaves the fourth fifth only just ahead. That is a reason to keep the obligation's legal design robust, not to choose it.

**What would change this:**
- a legal reading that a larger payment raises the coercion risk would favor A;
- care parts B-D's state shares, weighed together at stage G (`DEC-2026-11-11-05`), could move the right level for health.

## Question for you

Which states' share: A, B (recommended), C or D?
