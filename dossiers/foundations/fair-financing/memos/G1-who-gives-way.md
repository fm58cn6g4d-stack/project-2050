# Memo G1: Which other spending gives way

**Decided:** A, `DEC-2026-11-20-05`. Booked in stage G step 7 (`../2-settlement.md`, `models/data/inputs/settlement.json`). The memo below is the record of the choice as put to Espen; its figures are the draft's.


Role: decision memo for Espen, fork 1 of stage G's batch ([`README.md`](README.md); [`../2-settlement.md`](../2-settlement.md) part 2; `../1-audit.md` part C, item 1). Status: **provisional, drafted on the recommendation, November 20, 2026; revised for the milestone review (#470: B-5, F-4, F-5).** Not decided, not booked. Nominal $B on case `mixed`, priced by `models/tools/financing-protection/packages.py` (results in [`../notes/settlement-results.md`](../notes/settlement-results.md)); the state table is in [`../notes/states-2026-11-20.md`](../notes/states-2026-11-20.md). Project arithmetic on exploratory models, not official scores.

## The question

Health comes first on the plan's revenue (`DEC-2026-11-15-04`). Its share, **$532.1B in FY2040**, is taken from the top-end and corporate rows first (`DEC-2026-11-15-20`; the allocation is in `../2-settlement.md` part 1). That leaves the rest of the plan without the money those rows were paying for.

You said: "We can downsize other expenditures in project 2050 plans in the financing settlement, but I want a healthcare system that works and is durable." This memo asks how much of the rest of the gap to close by giving way on other spending. Whatever this memo doesn't close, memo G3's VAT does. **Every $90B a year of downsizing in FY2040 is about one point less of that VAT.**

Each flagship's own memos already priced cheaper designs (a helper's sweep of every booked dossier, listed at the end). Most would undo something you decided.

## The options

| | What gives way | FY2040 | FY2056 | FY2030-39 | VAT it saves (FY2040) | Households |
| --- | --- | --- | --- | --- | --- | --- |
| **A (recommended)** | The $300 adult credit ends, and the states pay 100% of their current long-term care spending, as they already do for health | **−253.9** | −475.0 | −1,521.1 | about 2.8 points | No federal benefit is cut |
| A′ | The same, with long-term care at 80% | −194.6 | −350.0 | −1,279.0 | about 2.2 points | The same; the states keep a fifth of their relief |
| B | A, plus four cheaper designs from the flagships' own memos (each yes or no) | −406.9 | −735.4 | −2,551.1 | about 4.5 points | Families with children and care workers get less |
| C | The credit only | −105.8 | −162.3 | −915.8 | about 1.2 points | No benefit cut; states keep their long-term care relief |
| D | Cuts instead of a VAT: A, plus about **$263B more in FY2040, rising to $731B in FY2056** | −517 | −1,206 | | all of it | Whole programs end (see below) |

### A. End the $300 credit, and the states pay their full current share for long-term care (recommended)

**The $300 adult credit** is a refundable $300 a year for every adult, booked at $105.8B in FY2040 and $915.8B over the decade.
- **It has been carried in the booked gap without a decision.**
  - It came from the October 26 exploratory budget, as a coordinated household credit, visible early help and a payment for people unable to work (`legacy/sources/recovery-and-solvency-budget.md`).
  - The October 26 decision listed "neither universal-credit amount" as not selected, and asked for a better-targeted refundable credit instead (`legacy/governing/project-2050-governing-decisions.md`, lines 432 and 450).
  - It has stayed in the budget model's `mixed` case ever since, so it is inside every booked gap, the stage E checkpoint's included. No `DEC-` row adopts it, and none removes it.
- No flagship designs it, and D3 has never counted it as a benefit.
- The secure floor (the child benefit, the childless EITC, the SNAP and SSI repairs) and the health contribution's exemption below 250% of poverty now do much of what a targeted credit would. That is this memo's reading, not a dossier's finding.
- *Who loses:* every adult loses a $300 a year payment. For a household of two on $30,000, that is $600, or 2% of income.
- **Read it with memo G3.** Ending the credit and adding a VAT leaves the VAT with no offset. Keeping the credit as the VAT's rebate (G1 C with G3 B) costs about 1.2 VAT points.

**The states' long-term care payment at 100%.**
- *What changes:* today the states would pay 50% of their current long-term care spending into the plan, indexed (HLT-9.09, `DEC-2026-11-11-06`). For health they pay 100% of their former Medicaid spending (`DEC-2026-11-15-25`). Raising long-term care to 100% treats the two alike: the plan takes on the new benefit and the enrollment growth, while each state's payment grows with the plan's per-person cost index (CBO's Medicare category).
- *What it is beyond:* 100% is beyond what the care dossier priced. HLT-7.17's range is 0-80%, care memo 3b priced 65% and 80%, and care memo 17 priced 65% (−$44B in FY2040), noting that it "belongs with health's share in the financing settlement".
- **The states, by state** (the state table; MACPAC and CMS data for FY2024 and calendar 2023):
  - In the base year, the payment equals each state's current state share at 100%, and less at any lower share. In the data year's dollars it is $336B nationally, against $286B at 50%.
  - The care-heavy states lose the most relief. New York's payment rises from $32.5B to $41.8B; North Dakota's from 71% of its state share to 100%.
  - **Later years are the risk.** The payment grows with the plan's index. A state whose own long-term care costs would have grown more slowly would pay more than its own path. On a proxy (long-term care growth over 2019-23), 30 states grew more than a point a year slower than the national rate; Kansas, Tennessee, Utah, Massachusetts and North Dakota grew most slowly. So "no state pays more than it pays today" holds only in the base year.
- *Who loses:* the states. They lose about $148B in FY2040 of relief they would otherwise have had ($313B in FY2056). The plan's federal benefit doesn't change. But a state finds the money somewhere: optional state-only services outside the plan (housing supports, state supplements, behavioral health), Medicaid's remaining roles (HLT-4.08), or other budgets.
- *Legal risk:* moderate, and higher than at 50%. The payment is collected by offset against "any federal payment to the state" (HLT-9.09). That is wider than Medicare Part D's "clawback" of the states' former drug spending (now at 75%), which offsets Medicaid payments only; the clawback has stood since 2006, and the states' challenge then never reached a ruling on the merits. A larger mandatory payment, collected through a wider offset, is a bigger target for a claim that the federal government is coercing the states (*NFIB v. Sebelius*, 2012).

**A′, long-term care at 80%.** It keeps a fifth of the states' relief, costs about 0.65 more VAT points (3.6% from 2035), and sits at the top of HLT-7.17's range. A further variant would grow each state's payment with the lower of the plan's index and its own long-term care cost index. That would protect the slow-growth states, but needs state cost data the plan's fund doesn't hold yet. It isn't priced.

### B. A, plus the flagships' own cheaper designs

Each of these was priced and weighed in its dossier, and you chose the costlier design. The review checked each price (F-4):

| Item | Saves, FY2040 | What changes | Source |
| --- | --- | --- | --- |
| The child benefit at the 2021 credit's amounts ($3,600 and $3,000), no newborn payment | about 50 | Every child gets less than under the decided design. The figure is memo 1's option A less C; the booked design has no $2,200 floor, so it is close to, not exactly, like for like | Secure floor memo 1 C |
| Early educators get the care wage floor but not parity with pre-K teachers | about 41 | The infant-room pay gap stays | Care memo 15 C |
| Pre-K for 4-year-olds only | about 33 (about 25 at maturity) | About 2.9 million children reached instead of 5.2 million | Care memo 11 C |
| The care wage floor at $18 instead of $20 | about 33 | Care workers get about 5% more instead of about 12%; supply risk rises | Care memo 14 A |
| Less the overlap: the lower floor already lowers memo 15 C's floor-only cost | about −4 | | |
| **Together** | **about 153** (−$1,030B over the decade) | | |

- On D3 these trims cost the bottom fifth about $1,040 a year on the decade average, and the fourth fifth about $420.
- The VAT they replace costs the bottom fifth less, so B leaves the bottom three fifths worse off than A and the fourth fifth a little better off: Q1 +$13,544 against +$14,308; Q4 +$4,882 against +$4,553.
- B also raises the revenue-mix test's share, to 63% over FY2030-39 and 58% in FY2040 (memo G3), and cuts the VAT to 1.25% stepping to 2.95%.

### C. The credit only

The states keep their long-term care relief, and the VAT is about 1.6 points higher.

### D. Cuts instead of a new tax

With A and memo G2's option C, and no VAT, the plan is still **$263B short in FY2040, 0.49% of GDP, rising to $731B, 0.76% of GDP, in FY2056.**
- Closing FY2040 with spending alone would take most of child care and pre-K ($243B in FY2040), or the whole child benefit ($220B), or most of the clean-power, housing and education rows together.
- The cuts would also have to keep growing, because health's budget grows faster than the economy (memo G8).
- This option is listed so the scale is visible. It is not recommended.

## Recommendation

**A.** It closes about $254B a year in FY2040 without cutting any federal benefit a person was promised. The credit was never decided. The states keep paying what they pay today, in the base year.

**What would change this:**
- If you would rather trim benefits than add VAT points, then **B**: each of its four items stands on its own, and you could take any of them.
- If the states' legal exposure or their later-year risk worries you more than the extra VAT, then **A′** at 80%, or 65% (−$44B).
- If you want the credit kept as the VAT's offset, then **C** with memo G3 B.

## Not recommended, for the record

The sweep also found, among others:
- the child benefit tapered from about $40,000 (secure floor memo 1 B, −$110-145B);
- stronger Medicaid in place of the home care benefit (care memo 6 A, about −$305B);
- no clean-energy tax credits (clean power memo 2, −$55.9B in FY2040);
- a UI fix without a federal standard (work memo 7 A, about −$10B).

Each would reverse a decided design at the heart of a flagship.

## Question for you

**G1.** Close part of the gap by ending the $300 adult credit and having the states pay 100% of their current long-term care spending (A, recommended)? Or long-term care at 80% (A′), add the four cheaper designs (B, each yes or no), take the credit only (C), or cut instead of taxing (D)?
