# Memo 17: Bringing care's costs down

Role: decision memo for Espen on care parts B-D's cost, after their decisions (`DEC-2026-11-11-02` to `-04`) and Espen's cost direction (`DEC-2026-11-11-05`). Status: **decided by Espen, November 11, 2026, in the lead session, `DEC-2026-11-11-06`** (board question 0n). Espen: "1. yes 2. as recommended 3. keep child care educator parity by 2036, but yes to the rest". So the state option below the line, yes; the state shares as recommended; options 2, 4 and 5 yes; option 3 no, so parity stays at 2036. Espen then approved separately, with a "yes", the item added to question 2 after the review: a state that declines child care or pre-K still owes its share. It reports the new totals after the three repricing steps Espen asked for. It then sets out further options to lower the cost, each with its savings, who loses what, and its evidence, and recommends a set. Every figure is project arithmetic in `../tools/care_repricing.py` (judgment where marked), in calendar years against current law. Section 6 converts to fiscal years. Bracketed tags point to `../evidence.json`.

**Espen's direction.** "i want these costs to come down some. maybe start with people qualifying for B2 at three daily activities instead of 2, and also make sure you're only counting workforce costs that are actual costs to the federal government (not assuming govt pays all of projected wage increases for workers... also, states should certainly pay for a portion of all of this, yes?"

**The fiscal rule still holds.** Costs are reported, not trimmed to fit (`DEC-2026-11-10-05`). This memo answers a request to lower them: it trims only where the decided designs stay whole.

## The short version

| | Before (the decision sheet) | Steps 1-2: the decided designs, priced as directed, at today's working state shares | Plus step 3: the recommended state shares (question 2) | Plus the decided options 2, 4 and 5 and the state option (questions 1 and 3, decided) |
| --- | --- | --- | --- | --- |
| **Part B, long-term care**, FY2030-39 | $2.6 trillion | **$2.15 trillion** | $2.15 trillion | **$1.9 trillion** |
| Part B, FY2040 | $590 billion | **$460 billion** | $460 billion | **$440 billion** |
| **Part C, child care and pre-K**, FY2030-39 | $1.4 trillion | **$1.4 trillion** | $1.32 trillion | **$1.32 trillion** |
| Part C, FY2040 | $190 billion | **$190 billion** | $177 billion | **$177 billion** |
| **Part D, the workforce**, FY2030-39 | $0.65 trillion | **$0.63 trillion** | $0.58 trillion | **$0.58 trillion** |
| Part D, FY2040 | $130 billion | **$124 billion** | $117 billion | **$117 billion** |
| **All three**, FY2030-39 | **$4.65 trillion** | **$4.18 trillion** (10% lower) | **$4.05 trillion** (13% lower) | **about $3.80 trillion** (18% lower) |
| **All three**, FY2040 | **$910 billion** | **$772 billion** (15% lower) | **$752 billion** (17% lower) | **about $736 billion** (19% lower) |

- **The second column is decided.** It is the decided designs, priced as Espen directed: three activities with the hold-harmless, and workforce lines at the federal cost only. States' shares stay at today's working figures: 90% federal for the bridge's floor, 90% for child care and parity, pre-K's 90% then 75%, and half of current long-term care spending.
- **The third and fourth columns are now decided too.** The third adds the state shares Espen accepted (question 2); its child care saving holds because a declining state still owes its share (decided separately, `DEC-2026-11-11-06` item 2a; step 3). The fourth adds options 2, 4 and 5 and the state option in question 1. **The fourth column is care's decided cost: about $3.80 trillion over FY2030-39 and $736 billion in FY2040.** With option 3 as well, it would have been about $3.76 trillion.
- Ranges are in the part files. The largest uncertainty is still part B's count of new users.

**What states pay, on the recommended shares.**
- About $115 billion a year in 2035 toward long-term care: half of what they would have spent on Medicaid long-term care.
- About $6 billion a year toward the wage floor in 2030-34.
- About $20 billion a year toward child care.
- About $34 billion a year toward pre-K, their own $14.4 billion included.

## Step 1: part B at three daily activities (decided; repriced)

The full workings are in `../3b-design-home-care.md`, "What the options cost".
- **Who qualifies.**
  - About 5.7 million older people met the two-activity test in 2011 [EV-CAR-482].
  - Nearly 3 million older people outside nursing homes got help with three or more self-care or mobility activities [EV-CAR-641], and 84% of nursing-home residents have three or more limitations [EV-CAR-647].
  - So about two-thirds of people at the two-activity line also meet three.
  - Among people not now served, the share is lower. People with three or more limitations are far likelier to get help already (85% against 45%) [EV-CAR-642] and to be on Medicaid (24%) [EV-CAR-643].
- **New users in 2035:** about 3.9 million (range 2.8-5.6 million), against 6.5 million (5-8 million) at two activities.
- **Cost per new user** rises about a fifth, to about $50,000, because the lightest-need tier drops out. People at this line get about 9 hours of help a day, paid and unpaid [EV-CAR-644].
- **Memo 6 B in 2035:** about **$300 billion** (range $130-655 billion), against $380 billion.
- **Benchmarks, adjusted the same way:** Urban's model gives about $390-560 billion; CBO's, about $280-320 billion. The project's figure sits inside the CBO-based range and below Urban's, as before.
- **The hold-harmless is kept:** everyone on Medicaid home care on December 31, 2034 keeps their help. On its own it costs about $47 billion in 2035, $0.18 trillion over 2035-39 and $24 billion in FY2040 (judgment), inside the figures above. It does not cover people who would have entered Medicaid home care later below the new line. That saves about $24 billion by FY2040, and question 1 asks whether to keep that door open.

## Step 2: workforce costs at the federal cost only (audited; three corrections)

`../3d-design-workforce.md`, "What is and isn't counted", gives each line's test.
- **No baseline wage growth is counted.**
  - Memo 14's 12% payroll increase is the lift above the wages the baseline already projects for 2026. Against 2024 wages a $20 floor would add about 19-20%; the dossier never used that figure.
  - The floor is indexed to average wages, the same growth the baseline gives care wages. So the government pays only the gap the floor opens, never the raises workers would have had anyway.
  - Parity in memo 15 is a ratio on part C's base, which grows only with prices. Elementary teachers' pay grows with wages, so the gap parity closes widens a little each year. Part C priced the raise at today's gap, so that widening is left out; it is an understatement, not a count of baseline growth.
- **Only care public programs pay for is counted.**
  - The floor covers publicly paid care only. Private-pay home care and employers' own payrolls are outside it.
  - Child care families' payments are capped at a share of income, so the raise falls on the program, not on them. The few families paying full price are a rounding error.
- **The federal share.**
  - *Corrected:* the bridge's wage floor was 90% federal. It is now matched at each state's bridge rate, about 68% (step 3).
  - *Corrected:* memo 16's nursing-home staffing is fully federal from 2035, not about 80%, because the plan then pays the care part of every stay (memo 8 C). Its cost rises about $1 billion a year.
  - *Corrected:* memo 14's base falls with step 1, from $617 billion to $538 billion of home care in 2035. So the $20 floor costs about $42 billion in 2035, not $47 billion.
- **Flagged for the booking, not changed here.** The budget model's HLT-4 row ($0.50 trillion over FY2030-39) carries the legacy "HCBS down payment and care workforce". Part B's bridge and memo 14's bridge-period floor are that down payment. When part B is booked, they replace HLT-4's long-term care part rather than adding to it (`../6-cost.md`).

## Step 3: states' shares (recommended levels; the settlement decides)

Each part's options, with federal cost, cost to states, burden and the risk that states opt out, are in its section 3 file: long-term care in `../3b-design-home-care.md`, the bridge and wages in `../3d-design-workforce.md`, child care and pre-K in `../3c-design-child-care.md`. **The anchor is health's decided maintenance of effort:** states keep paying half of their current Medicaid spending for the people who move (`DEC-2026-11-10-09`, memo 3 B; `../4-specification.md`, HLT-7.17).

| Part | Today's working figure | Options | Recommended | Federal change |
| --- | --- | --- | --- | --- |
| Long-term care, from 2035 | States keep paying half of their current long-term care spending | 50%; 65%; 80%; 50% plus 10% of the new benefit | **50%, as in health** | none |
| The bridge's wage floor, 2030-34 | 90% federal | 90%; each state's bridge rate (regular match plus the bridge's points, about 68%); the regular match (about 60%) | **The bridge rate** | about −$0.02 trillion |
| Child care | 90% federal | 90%; 90% for three years, then 80%; then 75% | **90%, then 80%** | about −$0.08 trillion; −$13 billion in FY2040 |
| Pre-K | 90% for three years, then 75% | 90% throughout; 75%; 60% (the Child Care for Working Families Act's pre-K title [EV-CAR-581]) | **75%, unchanged** | none |

- **Why not higher for long-term care.**
  - From 2035 states run nothing in the benefit, so a bigger share buys no state effort.
  - Health's own share is 50%. Keeping one rule across health and long-term care keeps states' payment to one formula.
  - The payment is a direct obligation on Medicare Part D's clawback model, which no court has tested (HLT-7.17). The larger it is, the larger the legal and political target.
  - If the settlement raises health's share, part B's should move with it (option 7).
- **Child care and pre-K: what stops a state from declining.**
  - Where a state declines, HHS runs the program (memo 13 A), so its children are still covered. On that rule alone, declining saves a state its whole share at no cost to its families, at 80%, 75% or any share. A state share is then voluntary in effect.
  - This is a sharper risk than Build Back Better's: CBO assumed a third of children would live in states that declined it [EV-CAR-587], even though declining there left those children without the program.
  - **Recommended: a state that declines still owes its share**, as a direct obligation collected by offset against federal payments, the same instrument as health's payment (HLT-7.17), with the same caveat that no court has tested it. HHS then runs the program with the state's money, and declining saves the state nothing.
  - *If that obligation is not adopted, or fails in court,* the saving is at risk. With a third of states declining, the federal government pays about $87 billion of child care's $100 billion at maturity at an 80% share, against $90 billion at 90% with every state in. That keeps only about a third of the saving: about $0.03 trillion and $4 billion in FY2040, not $0.08 trillion and $13 billion. Pre-K at 75% would then cost about $64 billion rather than $57 billion.
  - *Why not lower for pre-K:* at 60% the share a declining state saves is larger still, and without the obligation it is the likeliest to unravel.

## Further options to bring the cost down

Each saving is against the third column. Each is judgment unless tagged.

| # | Option | Saves, FY2030-39 | Saves, FY2040 | Who loses what | Evidence |
| --- | --- | --- | --- | --- | --- |
| 1 | **The bridge at 6 match points**, entry conditions only, not up to 10 with 4 for progress | up to $0.05 trillion | 0 | States get about $10 billion a year less in 2030-34, and nothing rewards progress on the access measures | Build Back Better's 6 points [EV-CAR-447]; the Balancing Incentive Program, with no penalty, got partial results [EV-CAR-480]; ARPA's temporary points went mainly to workers [EV-CAR-425] |
| 2 | **Tier budgets 10% lower below the top tier.** The top tier stays at nursing-home level | $0.09 trillion | $21 billion | People in the middle tiers get about a tenth fewer paid hours; families fill more. The exceptions process and the top tier are unchanged | Germany's partial benefit lost value until indexed [EV-CAR-440] [EV-CAR-441]. Tier amounts are working assumptions until a national assessment study sets them (memo 7) |
| 3 | **Early educators reach parity by 2038, not 2036.** The floor still starts in 2030-31 | $0.04 trillion | 0 | Early educators wait two more years for full parity, and pre-K keeps pulling staff from infant rooms longer | DC's pay fund cut turnover from 51% to 37% [EV-CAR-550]; New York City's pre-K drew 2,700 infant seats [EV-CAR-569] |
| 4 | **New users phased in over 2035-36, heaviest needs first.** Everyone on Medicaid home care moves on January 1, 2035; new users in the top tiers start then, and everyone meeting the line by January 2037 | $0.14 trillion | 0 | People with moderate needs at the line wait up to two years for paid help | The hiring need is the largest risk to part B (`../1d-problem-workforce.md`), and CBO's estimates assume supply meets demand [EV-CAR-452]. A staged entry eases the 2035 hiring peak. Design lens: a start date by tier, set by the one assessment, adds no new test |
| 5 | **Nursing-home residents contribute toward the care part**, up to 20% of it, from income left after room and board and the protected allowance | $0.04 trillion | $10 billion | Middle-income residents with pensions pay more, but never below the protected allowance | Japan made residents pay room and board in 2005 [EV-CAR-457] [EV-CAR-458]; the care share is judgment. The income check already happens for room and board, so it adds no new test |
| 6 | **A 10% copay on home-benefit hours above 200% of poverty**, capped at 5% of income a year | $0.07 trillion | $16 billion | Middle-income users pay, and some use less help | Judgment. It adds monthly bills and income checks, which the design lens counts against, and memo 4 C's copays already apply |
| 7 | **Part B's maintenance of effort at 65%**, moved with health's | $0.19 trillion | $44 billion | States pay about $35 billion a year more and get less relief | Health's range is 0-80% (HLT-7.17). Legal exposure grows with the payment |

**Recommendation: options 2, 3, 4 and 5**, saving about $0.31 trillion over FY2030-39 and $31 billion in FY2040. **Decided: 2, 4 and 5**, saving about $0.27 trillion and $31 billion; option 3 no, so parity stays at 2036.
- They keep every decided design whole:
  - the three-activity line and the hold-harmless;
  - the top tier at nursing-home level;
  - the $20 floor;
  - parity as the end point;
  - the plan paying the care part of nursing-home stays.
- Option 4 also lowers the largest delivery risk, the 2035 hiring peak.
- **Not recommended:**
  - option 1, because the progress points are the bridge's accountability;
  - option 6, because the burden falls on people at the point of care and memo 4 C's copays already apply;
  - option 7 on its own, because it belongs with health's share in the financing settlement.

**The protection that adds a little back (question 1).**
- Under the decided hold-harmless, a low-income person who first needs help with two daily activities after 2034 gets nothing, even where their state's Medicaid would have served them under current law. California's home care serves many people below three activities [EV-CAR-645]; Washington's Medicaid serves almost none [EV-CAR-646].
- Recommended: keep a state option in Medicaid to serve people below the line, at the regular match.
- It costs about $0.026 trillion and $15 billion in FY2040 if every such state keeps it.
- With it, the recommended set came to about $3.76 trillion over FY2030-39 and $736 billion in FY2040. As decided, without option 3, it is about $3.80 trillion and $736 billion.

## Questions for Espen

0n. **Decided** (see Status): 1 yes; 2 as recommended; 3 yes to options 2, 4 and 5, no to option 3. The questions as asked:
1. **Below the three-activity line:** keep a state option in Medicaid to serve people below it who meet Medicaid's income rules, at the regular match (recommended; about $15 billion in FY2040), or only today's users, as decided?
2. **States' shares** (recommended levels, for the financing settlement):
   - long-term care at 50%, as in health;
   - the bridge's wage floor at each state's bridge rate;
   - child care at 90%, then 80% after three years;
   - pre-K unchanged at 75% after three years;
   - a state that declines child care or pre-K still owes its share, collected as health's payment is.

   Agree? Without the last item, the child care saving is at risk if states decline (step 3).
3. **Further options:** 2 (tier budgets), 3 (parity by 2038), 4 (phase-in over 2035-36) and 5 (residents' contribution), yes to each (recommended)? Options 1, 6 and 7 are not recommended.

## If you decide

- Sections 3b-3d and memos 6-16 carry the chosen figures. Section 6 converts them to fiscal years when parts B-D are booked, with HLT-4's down payment netted.
- The state shares go to the financing settlement as working figures.
