# Care you can count on, part C (child care and pre-K): design choices

Role: section 3 of the care dossier, part C. It sets out the real forks for child care from birth to school age and for pre-K, the options weighed with their evidence, a recommendation for each, one decision memo per fork (memos 10-13), and a numbered list of narrower yes-or-no points. Status: reviewed at L3 (parts B-D, `review-milestone-bcd.md`; see the README); **decided by Espen, November 11, 2026: all as recommended** (`DEC-2026-11-11-03`). States' share set out in step 8 (`DEC-2026-11-11-05`) and decided by Espen, November 11, 2026 (board question 0n, `DEC-2026-11-11-06`): child care at 90% for three years, then 80%; pre-K unchanged. A state that declines still owes its share (decided separately, `DEC-2026-11-11-06` item 2a). Part C's decided cost: about $1.32 trillion over FY2030-39 and $177 billion in FY2040. Sources are named in plain text in the memos and points; bracketed tags point to `evidence.json`.

## How to read this section

- **The subject.** This part covers two things:
  - paid care and early education for children from birth until kindergarten;
  - public pre-K for 3- and 4-year-olds.

  It is not a family-benefit or entitlement program in general. The Child Tax Credit (FAM-1) and paid leave (FAM-3) are the secure floor's. Care workers' wages are part D's. Health covers every child from 2031 (HLT-7.03).
- **One batched set.** Four memos and ten yes-or-no points, so Espen can answer once. Memo 10 shapes the rest. Each is decided on its own, and none is adopted by silence.
- **Legacy designs are options** (`DEC-2026-10-30-02`). FAM-2 and FAM-2A to 2D (`legacy/domains/domain-family.md`) are weighed below. The legacy FAM-2A, a phased path, was chosen by an agent, not by Espen. The legacy file says so: "the one baseline in this file I chose rather than took from a decision". "Inherited assumptions" below traces each one.
- **Evidence strength is stated** for every recommendation: randomized trial, lottery, quasi-experimental study, program evaluation, international practice or expert judgment.
- **Report, don't gate** (`DEC-2026-11-10-05`). Costs are working assumptions with basis and range (`DEC-2026-11-10-07`), reported for the financing settlement and not trimmed to fit. Memo 10 is partly about money, because its options reach many of the same families at different cost, so it comes with its cost.
- **Design lens** (`DEC-2026-11-09-13`). Each option says what it asks of families and providers: forms, tests, waiting.
- **Time frame** (`DEC-2026-10-29-01`). The law is enacted in 2029 and starts in the 2030-31 school year. Dates before 2029 are labeled as 2027-28 or preparation.

## The baseline in 2029

Section 1, part 5, gives it in full:
- **The block grant.** CCDF is about $12.4 billion (FY2026), with the mandatory $3.550 billion permanent [EV-CAR-511] [EV-CAR-505]. It reaches about 16 percent of federally eligible children [EV-CAR-507].
- **The 2024 rule rescinded.** Its 7% copayment cap and pay-by-enrollment are gone from July 2026 [EV-CAR-510].
- **Pre-K and Head Start.** State pre-K reaches 37% of 4-year-olds and 9% of 3-year-olds [EV-CAR-519]. Head Start is near $12.4 billion [EV-CAR-504], and its immigrant-eligibility directive is enjoined [EV-CAR-513].
- **The 2025 law's tax changes.** A larger 45F employer credit, a $7,500 dependent care exclusion and a 50% top rate on the nonrefundable dependent care credit, all permanent from 2026 [EV-CAR-500] [EV-CAR-501] [EV-CAR-502]. They stay in the baseline (point 4).

## The forks at a glance

| Fork | Memo | Options | Recommended |
| --- | --- | --- | --- |
| 10. What families of children under 5 are guaranteed | `memos/10-child-care-guarantee.md` | A grow the block grant and make the dependent care credit refundable (the bipartisan route; with pre-K, the legacy FAM-2C); B a capped-cost guarantee: free at or below 85% of state median income, never more than 7% of income above it, no upper income limit (the Child Care for Working Families Act; FAM-2A's end state); C a universal low flat fee or free care, no income test (Quebec, Canada, New Mexico) | **B** |
| 11. Pre-K | `memos/11-pre-k.md` | A free, school-day pre-K for every 3- and 4-year-old, through states, in schools, Head Start and child care programs alike, at one rate (the CCWFA's pre-K title; FAM-2A's pre-K); B 3s and 4s inside memo 10's guarantee, one birth-to-five system; C 4-year-olds only | **A** |
| 12. How fast, and how supply is built | `memos/12-phasing-supply.md` | A phased behind supply: pre-K and free care at or below 85% of state median income from 2030, the full cap from 2032, with operating and facility grants and pay by enrollment (FAM-2A, updated); B the full guarantee from 2030 (FAM-2B); C each state starts when it shows the slots | **A** |
| 13. Who runs it, and Head Start | `memos/13-delivery-head-start.md` | A states run it under a federal floor, HHS runs it directly where a state declines, Head Start stays federal-to-local and joins at the guarantee's rates; B as A, with Head Start's money moved into the states' systems; C a federal program paying providers directly in every state | **A** |

## Against the bills and state models

Each recommendation is set against the main legislative designs. *Match* means the recommendation takes the same choice. *Diverge* means it does not, with the reason.

| Feature | Recommended here | Child Care for Working Families Act (2025) [EV-CAR-580] [EV-CAR-581] | Build Back Better (House, 2021) [EV-CAR-587] | Bipartisan route (S. 847, PACE Act, 2025 law) [EV-CAR-583] [EV-CAR-584] | State models | Why |
| --- | --- | --- | --- | --- | --- | --- |
| Who pays nothing | Families at or below 85% of state median income | **Match:** free at or below 85% | Phased up the income scale (not verified in bill text) | No guarantee | New Mexico: everyone [EV-CAR-547] | CCWFA's line, which is also the block grant's federal ceiling, so states know it |
| Most anyone pays | 7% of income | **Match:** 7% above 150% of state median income | **Match:** 7% | None | Washington: 7% cap, now paused [EV-CAR-549] | The cap the 2024 rule used [EV-CAR-510]; the U.S. consensus figure |
| Upper income limit | None | **Match:** none found | Diverge: phased to a limit | — | New Mexico: none | Everyone pays at most 7%, so no cliff |
| Activity test (work or study) | **None** (point 2) | Diverge: requires an "eligible activity" | Diverge: work-related | Credits require work | New Mexico: none | Design lens; the test costs paperwork and gaps when jobs change (shared rule 6) |
| Duration | Permanent, mandatory | Diverge: FY2026-31 | Diverge: six years | Permanent (tax) | — | Temporary money is failure 3 (section 2) |
| Pre-K | Free, school-day, 3s and 4s, mixed delivery, one rate | **Match** in shape | **Match** in shape | None | Colorado: 15 free hours [EV-CAR-593]; Boston and Tulsa in schools | Lottery and RD evidence [EV-CAR-557] [EV-CAR-555] |
| Pre-K federal share | 90% for three years, then 75% (judgment) | Diverge: steps to 60% by FY2031 | Stepped down | — | — | 60% repeats the state-opt-out risk BBB's score assumed [EV-CAR-587]; costs reported either way |
| Workforce pay | **Left to part D**, with a wage line shown | Rates must give a living wage at elementary-educator parity | Wage requirements | None | DC pay equity fund [EV-CAR-550] | Part D decides wages across all care (shared rule 8) |
| States that decline | HHS runs it directly (memo 13) | Grants to states | States opt in | — | — | BBB's score assumed a third or more of children in non-participating states [EV-CAR-587] |
| Tax credits | Keep the 2025 law's changes; refundability left to the secure floor (point 4) | — | — | Expanded 45F, 129, 21; PACE adds refundability | — | They help families above the free line pay copays |

**Why BBB's design failed, and what this set does about each.**
- *It was temporary.* The six-year life made it look cheaper and gave states and providers no reason to build. Here the program is permanent.
- *It depended on states opting in.* Here HHS has a fallback.
- *Its rules were complex for providers.* Here providers are paid by enrollment at one rate per age (point 3; memo 12).
- *It came in a bill that lost one senator over inflation and its total size* [EV-CAR-589].

The last risk is political, not design, and remains (see each memo).

## What the options cost

Working assumptions, not a model run (`DEC-2026-11-10-07`). Federal new money at maturity (2033, nominal dollars), against the 2029 baseline. Today's CCDF money (about $12.4 billion) is counted as moving into the program, not as new. Child care lines are priced at **cost-of-care rates at today's wage levels grown with inflation**. Any wage floor is part D's line, shown separately. Pre-K is priced **with pay parity**, because every pre-K design weighed here builds it into the standard (NIEER's cost model) [EV-CAR-566].

**The basis (project arithmetic; judgment where marked).**
- **Children.**
  - *By year of age.* About 3.7 million children in each year of age under 5 [EV-CAR-520].
  - *Under 3, using paid care under memo 10 B.* About 4.5 million full-time equivalents (range 3.5-6.0 million; judgment, the largest uncertainty, see section 1).
  - *3s and 4s in pre-K under memo 11 A.* About 5.2 million: 80% of 4s and 65% of 3s (judgment, from Boston's and Oklahoma's take-up; range 4.4-5.8 million).
- **Cost per child (2032).**
  - *Infant-toddler care at cost-of-care rates.* About $22,000 a year (range $18,000-28,000; judgment).
  - *Its basis.* It is above today's prices of $6,552-15,600 a year [EV-CAR-514], because infant rooms lose money at today's prices.
  - *School-day pre-K with parity.* About $17,500 (NIEER's $12,500 in 2020 grown with prices and wages) [EV-CAR-566].
  - *Wraparound care around the pre-K day.* About $6,000 a child, used by about 60% of pre-K children, those whose parents' hours run past the school day: about 3.1 million (judgment; range 45-75%).
- **Families' payments.** Copayments under memo 10 B recover about 15% of gross child care cost (range 10-20%; judgment, from the share of families above 85% of state median income).
- **The federal share.** 90% of child care direct services net of copayments, as in the CCWFA [EV-CAR-580] (the working figure; step 8 recommends 90% for three years, then 80%, below); today's CCDF money (about $12 billion, federal) is netted as moving in. Administration is about 5% of gross child care cost, paid federally (judgment). Pre-K is 90% for three years, then 75%. States keep their current pre-K and child care spending as maintenance of effort.

| Option | New federal cost at maturity, 2033 ($ billion) | Main pieces | FY2040 (about) |
| --- | --- | --- | --- |
| Memo 10 A, block grant tripled and the credit refundable | about 25 (15-35) | CCDBG to about $26 billion, about 18; a refundable dependent care credit, about 7 (judgment). Still rationed by states | about 30 |
| **Memo 10 B, capped-cost guarantee** | **about 85 (50-145)** | Under-3 care, 4.5 million × $22,000 ≈ 99 gross; wraparound, 3.1 million × $6,000 ≈ 19; gross 118. Less copayments, 15% ≈ 18: net 100. Federal share 90% ≈ 90, less today's CCDF ≈ 12: 78. Plus administration, 5% of gross ≈ 6. Total ≈ 84 | **about 110** |
| Memo 10 C, universal low flat fee or free | about 115 (75-185) | B plus copayments forgone above 85% of state median income, 18 × 90% ≈ 16, and more use by higher-income families, 10-20 gross, about 9-18 federal | about 150 |
| **Memo 11 A, universal school-day pre-K, 3s and 4s** | **about 60 (45-80)** | About 5.2 million children at about $17,500, about 91 gross; the federal share of the cost above states' current $14.4 billion [EV-CAR-519]; Head Start's 3- and 4-year-olds stay in its own budget | **about 80** |
| Memo 11 C, 4-year-olds only | about 35 (25-45) | Half the children, higher take-up | about 45 |
| Part D wage floor at elementary-educator parity, if part D chooses it | **about 45 on top of 10 B (30-65)** | Labor is about two-thirds of the 118 gross ≈ 79; parity raises most staff pay by half or more, ≈ +40-60 gross, at the 90% share (judgment; Bruenig, People's Policy Project, 2021, illustrates unsubsidized infant care rising to about $29,000 under parity; not in the register) | about 60 |
| Facilities grants (point 7) | about 5 a year, 2030-34 | Capital for new rooms, infant rooms first | 0 |

**States' share (step 8; the financing settlement decides).** Espen asked that states pay a portion (`DEC-2026-11-11-05`). The working figures above are 90% federal on child care's direct services and 90% for three years then 75% on pre-K, with states keeping their current spending. The anchor across care is health's decided rule, that states keep paying half of what they now spend (HLT-7.17). Here, though, states run the programs (memo 13 A), so their share is a match, and the risk is that they decline. Where a state declines, HHS runs the program directly (memo 13 A), so children are covered. Unless the law says otherwise, the federal government then pays all of it. On that rule alone, declining saves a state its whole share at no cost to its families, so any state share is voluntary in effect. The risk column below assumes the recommended remedy: a declining state still owes its share (after the table). Figures at maturity (`tools/care_repricing.py`):

| Option | Federal, 2033 | States, 2033 | Federal, FY2040 | Burden | Risk that states decline |
| --- | --- | --- | --- | --- | --- |
| *Child care:* 90% (the CCWFA [EV-CAR-580]) | about $84 billion | about $10 billion | about $110 billion | Least | Lowest |
| ***Child care:* 90% for three years, then 80% (recommended)** | **about $74 billion** (about $87 billion before today's CCDF money is netted, against $80 billion on that basis, if a third of states decline with no obligation; `6bcd-cost.md`, part 6) | **about $20 billion** | **about $97 billion** | States budget a fifth of a program they run and whose rates they help set | Low if a declining state still owes its share; otherwise real, because declining would save a state its share |
| *Child care:* 90% for three years, then 75% | about $69 billion | about $25 billion | about $90 billion | As pre-K's share | As above, larger |
| *Pre-K:* 90% throughout | about $69 billion | about $22 billion, their $14.4 billion included | about $95 billion | Least | Lowest |
| ***Pre-K:* 90% for three years, then 75% (recommended, unchanged)** | **about $57 billion** | **about $34 billion**, their $14.4 billion included [EV-CAR-519] | about $80 billion | States already run pre-K, mostly through schools | Low if a declining state still owes its share; otherwise real |
| *Pre-K:* 90% for three years, then 60% (the CCWFA's pre-K title [EV-CAR-581]; H.R. 10421 [EV-CAR-582]) | about $46 billion | about $45 billion | about $64 billion | States carry two-fifths | **High.** CBO assumed about a third of children lived in states that would not take Build Back Better's child care and pre-K [EV-CAR-587], even though declining there left those children without it. Here declining costs a state's families nothing, so the pull is stronger, and the larger the share the more a declining state saves |

- *What makes declining costly (recommended).* A state that declines child care or pre-K still owes the share it would have paid. The share is collected as a direct obligation by offset against federal payments, the instrument health uses for its states' payment (HLT-7.17). HHS then runs the program in that state with the state's money, so declining saves the state nothing and only gives up control of rates, providers and delivery. It carries health's caveat: the instrument has never been tested in court, and a court could read the offset as coercion (*NFIB v. Sebelius*).
- *If that obligation is not adopted, or fails,* the saving is at risk. With a third of states declining and HHS paying all there, the federal government pays about $87 billion of child care's $100 billion at maturity at an 80% share, against $90 billion at 90% with every state in. That keeps about a third of the saving: about $0.03 trillion over FY2030-39 and $4 billion in FY2040 rather than $0.08 trillion and $13 billion. Pre-K at 75% would cost about $64 billion rather than $57 billion.
- *Recommendation (decided, the obligation included):* child care at 90% for three years, then 80%, which saves about $0.08 trillion over FY2030-39 and $13 billion in FY2040 if states stay in or still pay; pre-K unchanged; and a declining state still owes its share. Pre-K's state share stays a little higher than child care's because states already run and fund pre-K, while child care for every family is new and states must build it. Memo 15's parity and the wage floor follow the same shares.

**Over FY2030-39**, on memo 12 A's phasing (calendar years, roughly; section 6 converts):
- pre-K, about $0.56 trillion;
- child care (memo 10 B), about $0.8 trillion (about $20 billion in 2030 for the free tier, rising to about $85 billion in 2033 and about $107 billion in 2039);
- facilities, about $0.03 trillion;
- **in total, about $1.4 trillion (range $0.9-2.1 trillion)** before any part D wage floor (about $1.32 trillion, range about $0.85-2.0 trillion, at the recommended child care share; FY2040 about $177 billion), which would add about $0.4 trillion if adopted from 2032. FY2040's permanent cost is about $190 billion (range $140-280 billion) plus any wage line.

**Checks against outside estimates.**
- **CBO, Build Back Better.**
  - *As written.* $381 billion over six years for the pair (CBO, via CRFB) [EV-CAR-587].
  - *If permanent.* $752 billion over ten years.
  - *What lowers those figures.* CBO assumed a third or more of children lived in states that would not take part, and the window was 2022-31, in lower prices.
  - *Scaled.* At full participation and 2030s prices, that points to roughly $150-200 billion a year at maturity for the pair. This set's about $145 billion (10 B plus 11 A) sits at the bottom of it, mainly because families above 85% of state median income pay copays and the rates are at today's wage levels.
- **Penn Wharton.** About $400 billion as written, plus $394 billion if permanent [EV-CAR-588], the same scale as CBO.
- **The National Academies.** At least $140 billion a year from all sources in 2018 dollars for a high-quality birth-to-five system, with public money rising by up to $53 billion a year [EV-CAR-567].
  - *Comparability.* This set's federal cost is higher, because it makes care free for most families and covers pre-K at parity.
  - *The gap.* Grown to the 2030s and with parity, the Academies' total is close to this set's gross cost.
- **The CCWFA.** About $60 billion a year in one estimate with no method given (PERI) [EV-CAR-591]. That looks low against CBO's scores of a similar design, and this dossier does not rely on it.
- **New Mexico.** The state's fiscal staff warn that universal free care could nearly double its program's cost if families now paying privately join [EV-CAR-547]. Take-up is the risk in every option.

**Against the legacy figure.** FAM-2A's $0.6 trillion (range $0.4-0.9 trillion) over 2030-39 was scaled from CRFB's BBB figure (`legacy/domains/domain-family.md`). This set is about $1.4 trillion for three reasons:
- the legacy figure kept BBB's state non-participation and its 2021 prices;
- it ended before the program matured;
- this set adds 3-year-olds at parity and drops the activity test.

The legacy file itself warned that "mature-program years cost more".

**What the totals leave out.**
- *Mothers' added earnings and taxes.* Not counted, as CBO's conventional scores do not count them. Quebec's evidence puts the long-run fiscal recapture at 75-117 percent of cost [EV-CAR-534]. Norway's suggests much less where mothers already work [EV-CAR-544].
- *Head Start's own budget.* About $12.4 billion, kept outside.
- *Families' current spending.* Most of memo 10 B's cost replaces what families pay today [EV-CAR-514]. It is a shift to public money as well as new care.
- *Who pays.* That is the financing settlement's question, not this part's. The legacy EDU-9B payroll institution, which carried child care and pre-K, is a working choice for the settlement, not assumed here.

## Inherited assumptions, traced

| Assumption | Where it comes from | Espen decided, or a working choice? | Here |
| --- | --- | --- | --- |
| Phasing: pre-K and a lowest-income tier first (2030-31), the full cap from 2032 (FAM-2A) | Legacy FAM-2 (`domain-family.md`), from legacy design rule 5, "supply with demand" | **Working choice**, chosen by an agent ("I chose rather than took from a decision"); `DEC-2026-10-30-02` | Memo 12 A, updated: the free tier is set at 85% of state median income, not 75% |
| Supply with demand (design rule 5) | Legacy governing decisions, design rules | A guiding principle, settled under `DEC-2026-10-30-02` | Applied: memo 12 |
| The 7% of income cap | Legacy FAM-2, from the CCWFA and BBB | Working choice | Memo 10 B keeps it, on the CCWFA's 2025 scale [EV-CAR-580] |
| Free below 75% of state median income | Legacy FAM-2A | Working choice | Updated to 85%, the 2025 CCWFA's line |
| Eligibility up to 250% of state median income | Legacy FAM-2 (BBB-era figure) | Working choice | Dropped: the 2025 CCWFA has no upper limit; everyone pays at most 7% |
| Wage parity for care workers from 2030-31 | Legacy FAM-2A | Working choice | Moved to part D (shared rule 8); priced as a separate line |
| Mandatory funding, not appropriations | Legacy FAM-2; legacy design rule "durable instruments" | Principle settled; the vehicle is a working choice | Kept |
| Cost $0.6 trillion over 2030-39 | Legacy, scaled from CRFB | Working estimate | Replaced (about $1.4 trillion); reasons above |
| Pre-K standards: 1,020 hours, K-12 pay parity, BA within seven years, 4% to tribes, localities apply directly, federal share 100% stepping to 60% (FAM-2D) | The Bonamici omnibus, now H.R. 10421 [EV-CAR-582] | Working choice (an alternative in the legacy) | Memo 11 A takes hours and parity; point 6 makes the BA a supported goal; point 9 sets the tribal share; memo 13 A's federal fallback covers direct applications |
| The under-3 staffing critique | Legacy education session (`domain-family.md`, FAM-2) | Analysis, not a decision | Weighed: memos 11 and 12, with New York City's evidence [EV-CAR-569] |
| Pre-K's one home is FAM-2, not education | Legacy `domain-education.md` and `domain-family.md`; `agenda.csv` (FAM-2 in care) | Working choice, consistent with `charter/PLAN.md` 3.1, which Espen adopted (`DEC-2026-10-28-02`) | Kept; the split is proposed below |
| Financing through the EDU-9B education fund (payroll) | Espen adopted the full EDU-9B package, October 25-26 (legacy governing decisions) | **Espen's legacy decision**, now a working choice under `DEC-2026-10-30-02`; financing is the settlement's (`DEC-2026-11-10-05`) | Not assumed; cost reported only |
| Vehicle: the summer-2029 reconciliation bill (R2) | Legacy governing decisions | Working choice | Kept as the working vehicle; section 4 decides |
| HHS's Administration for Children and Families runs it | Legacy FAM-2 and EDU dependencies | Working choice | Memo 13 A |
| Health covers every child from 2031 | `DEC-2026-11-10-09`, `-11` (HLT-7.03) | **Espen decided** | A boundary: care's health services stay in the plan |
| Housing ignores the value of child care when setting voucher rent | `DEC-2026-11-10-03` | **Espen decided** | Consistent: a free or capped benefit adds no counted income |
| The time frame, the design lens, report don't gate, what needs an answer now | `DEC-2026-10-29-01`, `DEC-2026-11-09-13`, `DEC-2026-11-10-05`, `-07` | **Espen decided** | Applied throughout |

## Seams with other dossiers (named, not settled)

- **Pre-K and education.**
  - *The record.* `charter/PLAN.md` 3.1 puts "child care and pre-K" in care and education in wave two "beyond care". The agenda's home for FAM-2 is care. The legacy education file says pre-K "stays in domains/domain-family.md FAM-2 (one home)".
  - *Care owns.* Pre-K for 3s and 4s and all care from birth to school entry, as one birth-to-five system: eligibility, the per-child rate, standards for classrooms in any setting, and Head Start's place.
  - *Education owns.* Kindergarten and K-12 (EDU-1); the K-12 side of the transition (records, kindergarten entry, IDEA Part B preschool services under EDU-2); and the educator pipeline in schools of education (EDU-4).
  - *Part D owns.* Pay and the workforce plan across care, coordinated with EDU-4's pipeline so pre-K hiring is staffed ahead of the 2031-33 peak.
  - *The financing.* The legacy EDU-9B fund goes to the settlement.
  - *What would change this.* If Espen prefers pre-K in education (as the Bonamici bill frames it), memo 11's design moves there unchanged, and memo 12's phasing must still fund under-3 care in the same law.
- **Workforce (part D).** Each option is priced without a new wage floor, and the wage line is shown. The CCWFA's living-wage and parity rule is part D's to decide [EV-CAR-581].
- **Health.**
  - *What the plan covers.* Developmental screening, children's health services and Early Intervention-related health care stay in the plan from 2031 (HLT-7.03).
  - *What this part does.* Child care programs do not bill the plan.
  - *Head Start.* Its health services coordinate with the plan instead of paying for care the plan covers.
- **Secure floor.**
  - *Paid leave.* Paid leave (FAM-3) shortens the infant months that need care.
  - *The Child Tax Credit.* FAM-1 adds money but no slots.
  - *The dependent care credit.* Whether to make it refundable is a tax-credit question for the secure floor (point 4).
  - *Shared rules.* Rules 1, 2 and 4 on income lines and phase-outs are the secure floor's. The 7% cap is itself a phase-out, so it must be stacked with the others.
- **Financing.** Cost is reported here; taxes are the settlement's (`DEC-2026-11-10-05`).
- **Housing.** Housing asked how care interacts with its guarantee for families with children (`DEC-2026-11-09-06`). Memo 10 B makes care free for the families housing reaches first (all well below 85% of state median income), and housing already ignores the value of child care in rent (`DEC-2026-11-10-03`).

## Recommended without a memo: ten yes-or-no points

Each is decided on its own. None is adopted by silence. Costs are judgment unless a tag gives them.

1. **Put the 2024 rule's protections in statute in the 2029 law: copayments capped at 7% of income, payment by enrollment and in advance, and grants or contracts for scarce care.**
   - *Why:* HHS rescinded them from July 2026 [EV-CAR-510]. They are the bridge until memo 10's guarantee starts, and its payment rules after.
   - *2027-28:* defend the block grant and Head Start at FY2026 levels or better [EV-CAR-504] [EV-CAR-506]. This is a labeled 2027-28 exception.
   - *Cost:* small inside memo 10.
   - *Evidence:* program design (the rule). The ARPA operating grants showed providers can be paid for supply [EV-CAR-509].

   **Recommended: yes.**
2. **No work or study test: the guarantee follows the child.**
   - *Why:* the design lens. An activity test costs families paperwork and drops children when a parent loses a job, the moment care matters for the search. The CCWFA keeps a test [EV-CAR-580]. New Mexico has none.
   - *Shared rule 6:* owned by the work flagship. The legacy direction is "an offer, not a work condition" (LAB-10).
   - *Cost:* about $3-6 billion a year more take-up (judgment).
   - *Political risk:* "paying for care for parents who don't work" is the predictable attack. The answer is that most families with young children have every parent at work [EV-CAR-518], and the test catches job-seekers and students.

   **Recommended: yes.**
3. **One yearly income determination, from the prior year's tax record or the family's own statement, with 12-month eligibility and no asset test.**
   - *Why:* the 2014 law's 12-month rule [EV-CAR-585] and the design lens.
   - *How copays are set:* once a year. They are corrected only at the next year's determination, never reclaimed mid-year.
   - *Shared rules:* rules 1 and 5 (secure floor; democratic renewal).
   - *Burden:* one statement a year.

   **Recommended: yes.**
4. **Keep the 2025 law's child care tax changes (45F, the $7,500 exclusion, the 50% credit rate)** [EV-CAR-500] [EV-CAR-501] [EV-CAR-502].
   - *How they fit:* families keep claiming the credit and exclusion for what they pay, including copays.
   - *Refundability:* whether to make the credit refundable (the bipartisan PACE Act) [EV-CAR-584] is **left to the secure floor**, which owns tax credits for families. Memo 10 B makes it matter less, because families below 85% of state median income pay nothing.
   - *Cost:* none new (already in the baseline).

   **Recommended: yes.**
5. **Immigrant eligibility follows the child: every child resident in the state, and Head Start under its rules before July 2025.**
   - *Why:* the 2025 directive is enjoined [EV-CAR-513], and a child's eligibility should not depend on a parent's status.
   - *Shared rule 3:* proposed to the immigration flagship. Health's every-resident rule is the parallel (`3-design.md`, point 3).
   - *Cost:* small (judgment).

   **Recommended: yes, as a proposal to immigration.**
6. **Teachers' credentials: support, don't mandate.** FAM-2D's lead-teacher degree within seven years becomes a funded pathway: tuition, paid release time and pay steps by credential through part D. It is not a hard deadline.
   - *Why:* Tennessee's certified teachers still produced harm [EV-CAR-559], while Boston's gains came with curriculum and coaching [EV-CAR-557].
   - *Evidence:* judgment. The register holds no meta-analysis on degrees and quality ("Evidence still needed").
   - *Burden:* none on providers. A hard deadline would close family child care homes.

   **Recommended: yes.**
7. **A facilities fund, about $5 billion a year in 2030-34,** for new and converted rooms, with infant and toddler rooms and areas with few slots first.
   - *Why:* Canada built too few spaces [EV-CAR-538] [EV-CAR-540]. Penn Wharton's 2022 pre-K estimate includes facilities (not in the register).
   - *Cost:* about $25 billion in all (judgment).

   **Recommended: yes.**
8. **Every kind of provider on the same terms.** Centers, family child care homes, Head Start, schools, and faith-based providers chosen by parents are paid at the same rates and standards.
   - *Why:* New York City first left family child care out of pre-K and reversed course in 2018 (Roosevelt Institute; not in the register). New Mexico's home providers shrank as licensed care grew (context of EV-CAR-548).
   - *Faith-based providers:* section 4 checks the constitutional route, in which parents' choice directs the money.
   - *Political risk:* both sides contest religious providers' participation.

   **Recommended: yes.**
9. **A tribal share: at least 4% of the guarantee's and pre-K's money,** run by tribes on their own plans, as in FAM-2D and housing's tribal set-asides (`DEC-2026-11-09-16`).
   - *Cost:* inside the totals.

   **Recommended: yes.**
10. **Built-in evaluation.** Pre-registered evaluations of pre-K and the guarantee, using admissions lotteries where programs are oversubscribed (Boston's method) [EV-CAR-557], with data the program already collects, run with education's research center (EDU-10).
    - *Cost:* small.
    - *Burden:* none new.

    **Recommended: yes.**

## Shared rules this section relies on

From `dossiers/shared-rules.md`. These are working answers, not decisions of the other owners.

| Rule | Owner | Part C's working answer | Range |
| --- | --- | --- | --- |
| 1, 2 and 4. Income, phase-outs, income lines | Secure floor | State median income lines (85%, 100%, 125%, 150%) as in the CCWFA [EV-CAR-580]; the 7% cap is a phase-out to stack with others | Poverty-guideline lines instead; 0-7% |
| 3. Immigrant eligibility | Immigration | Every resident child (point 5) | Current law's PRWORA lists, to every resident |
| 5. Who verifies | Democratic renewal | One yearly determination from tax records or self-statement (point 3) | — |
| 6. Conditions on help | Work flagship | No activity test (point 2) | The CCWFA's activity test |
| 8. Workforce | Immigration and work; part D | Priced without a wage floor; the wage line shown | Up to elementary-educator parity |

## How the choices fit together

- **The recommended set, in two steps.**
  - *From the 2030-31 school year.* Free care for every child under 5 in families at or below 85% of state median income. Free school-day pre-K for 4-year-olds everywhere, and for 3-year-olds where states are ready. Facilities and operating money, with providers paid by enrollment. Head Start continues.
  - *From July 2032.* The full guarantee: no family pays more than 7% of income, with no upper limit and no activity test. 3-year-olds everywhere by the 2033-34 school year.
- **Against the legacy.** It keeps FAM-2A's phased shape and its reason, supply with demand. It updates the income lines to the 2025 bill, drops the 250% limit and moves wages to part D.
- **If memo 10 is A.** Pre-K (memo 11) becomes the main program, which is the legacy FAM-2C. It is exposed to the under-3 critique unless the block grant grows enough to fund infant care, and points 1 and 7 matter more.
- **If memo 10 is C.**
  - *What changes.* There is no copayment. Supply pressure is highest, so memo 12 A's phasing matters most.
  - *The risks.* Canada's waitlists [EV-CAR-539] and Quebec's quality [EV-CAR-536] are the risks to manage.
- **Tensions to watch.**
  - *Workers.* Demand for care workers rises faster than part D can train them. Pre-K hiring peaks in 2031-33.
  - *State capacity.* States' administrative capacity varies.
  - *Health's overlap.* The 2031-33 build-out overlaps health's first wave, which strains HHS's capacity, though at different agencies.

## Evidence still needed

- **Take-up.** Child care arrangements by age and income (SIPP, NSECE) to narrow the under-3 take-up assumption, the largest cost uncertainty.
- **Credentials and quality.** Meta-analytic evidence on lead-teacher degrees and classroom quality (point 6).
- **CBO's own tables** for Build Back Better's child care and pre-K, and any CBO estimate of the CCWFA.
- **Supply counts** by county and age (facilities sizing, point 7).

## Questions for Espen

One answer per item; each is decided on its own.

1. **Memo 10, the guarantee:**
   - A: grow the block grant;
   - B: free at or below 85% of state median income, never more than 7% of income, no upper limit (recommended);
   - C: universal low flat fee or free.
2. **Memo 11, pre-K:**
   - A: free school-day pre-K for 3s and 4s, mixed delivery (recommended);
   - B: inside the child care guarantee;
   - C: 4-year-olds only.
3. **Memo 12, phasing:**
   - A: phased behind supply, full cap from 2032 (recommended);
   - B: full from 2030;
   - C: state readiness triggers.
4. **Memo 13, delivery:**
   - A: states with an HHS fallback, Head Start kept federal-to-local (recommended);
   - B: Head Start's money moved into the states' systems;
   - C: a federal program.
5. **Points 1-10, yes to each (recommended)?**
   1. the 2024 protections in statute;
   2. no activity test;
   3. one yearly income check;
   4. keep the 2025 tax changes, refundability to the secure floor;
   5. every resident child, proposed to immigration;
   6. credentials supported, not mandated;
   7. a facilities fund;
   8. all providers on the same terms;
   9. a 4% tribal share;
   10. built-in evaluation.
6. **The pre-K seam:** care keeps pre-K, education keeps K-12 and the transition, part D keeps pay. Agree?
