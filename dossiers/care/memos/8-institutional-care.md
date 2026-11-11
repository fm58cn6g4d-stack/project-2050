# Memo 8: Nursing homes and other institutional care

Role: decision memo for Espen, fork 8 of the care dossier (part B; `../3b-design-home-care.md`). Status: **for Espen, not decided.** Health's working position is option A: institutional long-term care stays in Medicaid, as S. 1506 sec. 204 has it (`../4-specification.md`, HLT-7.07). This memo weighs keeping that against changing it. Sources are named in plain text; bracketed tags point to `../evidence.json`. Costs marked "judgment" are working assumptions; their basis is in `../3b-design-home-care.md`.

**This memo decides who pays for long stays in nursing homes and in intermediate care facilities for people with intellectual disabilities, after 2035.** Short post-hospital stays are already plan medical care (HLT-7.05). Psychiatric hospital care is plan medical care too.

## Why it matters

- **Long stays are the catastrophic risk.** A semi-private nursing-home room costs a median $114,975 a year (CareScout, 2025) [EV-CAR-437], a figure from a long-term care insurer's survey. ASPE expects about 22% of people turning 65 to need care for more than five years (ASPE, 2022) [EV-CAR-400].
- **Medicaid pays for most residents, after they spend down.** It is the primary payer for 63% of nursing-facility residents (KFF, 2025) [EV-CAR-438], after people deplete their savings to SSI's $2,000 limit (CRS, 2017) [EV-CAR-409].
- **Health's working split creates a cliff.** If memo 6 B passes and nursing homes stay in Medicaid, a person at home is covered without an asset test, but the same person moving to a nursing home must spend down. Families would face that cliff at the hardest moment.
- **States pay a large share.** States pay about 47 percent of Medicaid's long-term care [EV-CAR-448], and institutional Medicaid spending was $71.0 billion in 2022 (CMS) [EV-CAR-407].
- **The bills differ.** S. 1506 keeps institutional care in Medicaid with a state spending floor [EV-CAR-278]. The House bill covers all of it [EV-CAR-291].

## Options

**A. Institutional care stays in Medicaid, with a state floor (S. 1506 sec. 204; health's working position).**
- *For people:* nothing changes. A widow with $90,000 in savings who needs a nursing home spends it down to $2,000, then Medicaid pays.
- *Cost:* none new.
- *Risk:* the cliff between home and institution under memo 6 B. Medicaid keeps its asset test, estate recovery and state variation for the people with the longest, costliest needs.
- *Burden:* full financial applications for the people least able to make them.

**B. It stays in Medicaid, with federal protections against impoverishment.**
- **What it does.** It adds, from 2030:
  - higher resource limits ($4,100 and $6,200, indexed; S. 1506 sec. 1101) [EV-CAR-431];
  - no estate recovery (S. 1506 sec. 205) [EV-CAR-431];
  - the home always protected while a spouse or dependent lives there;
  - a higher personal-needs allowance for residents (judgment: about double today's typical amount).
- *For people:* the widow keeps a little more and her house passes to her children, but she still spends down.
- *Cost:* about $3-10 billion a year (judgment). MACPAC counts estate recovery at $733.4 million a year [EV-CAR-410].
- *Burden:* still a financial application.

**C. From January 1, 2035, the plan pays the care part, and residents pay room and board from income above a protected allowance (recommended).**
- **What it does.**
  - The plan pays a nursing home or intermediate care facility for the care it gives: nursing, personal care, therapy and supervision. Every resident who meets memo 7's threshold gets it, with no asset test.
  - Residents pay the room-and-board part from their income, keeping a protected personal allowance. A resident's spouse at home keeps the household income they need, as under today's spousal rules.
  - Residents who cannot pay room and board get it from Medicaid, with no asset test beyond income (judgment: a state program paid at the regular match).
  - States keep paying half of what they now spend on institutional care (maintenance of effort, as S. 1506's floor does) [EV-CAR-278].
- **Why it is built this way.** Japan's and Germany's insurance work the same way: insurance pays for care, and people pay for their room and food as they would at home [EV-CAR-442] [EV-CAR-440]. People at home pay their own rent too, so the line between home and institution falls in the same place.
- *For people:* the widow keeps her savings. Her Social Security pays most of her room and board, and the plan pays for her care.
- *Cost:* about $50-90 billion a year of new federal money in 2035, about $65-120 billion in FY2040 (judgment: states' share net of their payment, plus the care part of private-pay stays). The room-and-board share (30-40%, judgment) is the main unknown. Section 6 needs nursing-home spending by payer.
- *Risk:* nursing homes could shift costs into room-and-board charges. The plan sets the room-and-board rate it recognizes, which needs rate rules (section 4). Without memo 6 B, C alone would favor institutions over home, so C makes sense only with B.
- *Burden:* an income statement for room and board, from records the government already holds.

**D. The plan pays for all institutional care, room and board included (the House bill).**
- *For people:* the simplest promise: a nursing home costs a resident nothing.
- *Cost:* about $80-140 billion a year in 2035 (judgment), about $30-50 billion more than C.
- *Risk:* it pays for room and board in an institution but not at home, which tilts choices toward institutions. That runs against the evidence that people who leave institutions do better at home [EV-CAR-429].
- *Burden:* none.

## Recommendation: C, with B's protections in the 2030-34 bridge

- **It protects against the catastrophic risk your October 26 direction named,** long and intensive needs, and removes the cliff memo 6 B would otherwise create.
- **It treats home and institution alike:** the plan pays for care, and people pay for housing and food.
- **Against D,** the difference is about $30-50 billion a year, and D's tilt toward institutions.
- **Against A,** which is health's working position and S. 1506's design, A leaves the costliest needs means-tested.
- **Until 2035,** B's protections apply in the bridge (points 3 and 4 in `../3b-design-home-care.md`).
- **If you choose memo 6 A or C,** then B is the consistent choice here.

## If you decide

- **Section 4** amends HLT-7.07 so that institutional care's care part moves to the plan in 2035, and writes the room-and-board rule, the protected allowance, the spousal protection and the states' payment.
- **Section 6** prices it once nursing-home spending by payer is in the register.
