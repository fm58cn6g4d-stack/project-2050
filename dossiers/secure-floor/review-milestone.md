# A secure floor for every household: L2/L3 milestone review

Role: the independent milestone review of the secure floor dossier (flagship 1; `charter/PLAN.md` 3.2 and 5, "Review"; `charter/STANDARDS.md`, "Milestone review"), board "Next" step 2. The reviewer wrote none of the dossier. It tries to break the work on four fronts (weak evidence, missing populations, optimistic assumptions, cheaper alternatives). It also applies the design lens (`DEC-2026-11-09-13`), checks the fiscal-rule report against `DEC-2026-11-10-05`, checks every decided item against `DEC-2026-11-12-06` and `-09`, and checks section 9 against sections 1-8. Status: current, as of main at commit `6a029ae` (November 12, 2026, after #293 and #295). Reviewer: Claude Code, `session_01UQzgBwAwdHFG8ArnCwHdrQ`. It changes nothing in the dossier. Every fix below is a later step: the fix steps go to a fresh Most capable session (S4's author takes on nothing more, per the board), and the booking to the lead.

Espen's decisions on the secure floor (`DEC-2026-11-12-06`, `-09`) and immigration's rule 3 (`DEC-2026-11-12-07`, memo 6 C) are settled. Where a decided choice has a cost or gap the dossier does not show, this review says so and sends it to Espen as a question; it does not argue the choice. Under `DEC-2026-11-10-07`, a clearly bounded uncertainty is not a defect. Every investigation asked for below names the decision it informs and whether it blocks that decision now.

## Verdicts

| Level | What it needs (`charter/PLAN.md` 3.2) | Verdict |
| --- | --- | --- |
| **L2, design** | Key parameters chosen (who, what, how much, who administers), with the main alternatives weighed | **Pass** (record fixes only, none blocking) |
| **L3, specified** | Provisions section by section (eligibility, benefit, administration, phase-in, remedies); evidence for each load-bearing claim; a cost range validated by models with stated limits; a delivery plan | **Not yet: close.** Three blockers |

**Why L2 passes.** Every fork (memos 1-7, ten forks) had two to four options weighed on evidence, with a forks-at-a-glance table, a bill-by-bill table, outside benchmarks (TPC, PolicyEngine, CBO, JCT, SSA's actuaries, Urban) and the legacy designs as options. All are decided and recorded (`DEC-2026-11-12-06`, `-09`), and every memo's status line says so. Memo 6's own figures are stale (C-1, the known double count), but section 6 carries the corrected figure.

**Why L3 is not yet.** Most of L3 is in place:
- section 4 specifies 42 provisions with parameters, vehicle, agency, current-law change and evidence, and a consistency table;
- section 5 has a timeline, remedies, states' roles and a rural plan;
- section 6 prices the decided set on fiscal years and reproduces from its tool (below);
- sections 7 and 8 give benchmarks, objections, triggers and hard stops.

The blockers:
1. **Social Security's gap-closer rests on an estimate its own specification cannot reach** (O-1). Memo 6 C closes the gap with SS-8, the stock investment, at a legacy estimate of +0.5 to +1.0% of payroll (grade D). SS-8.01 caps it at 20% of reserves, phased in from 2032. On the reviewer's arithmetic the trust funds would need reserves several times today's for 20% of them in stocks to yield that much, and the package does not build such reserves. So the central package is nearer +3.7 than +4.3 against a 4.42% gap, and the fallback (SS-7.01) is the expected case, not a contingency. Sections 6, 7 and 9 state the package "at or near 75-year balance". An unsupported claim stated as settled is a defect.
2. **The monthly child benefit can be seized for debts** (B-1). Nothing in section 4 exempts the benefit from Treasury's refund offsets or from garnishment. As a refundable credit it is subject to them by default (26 U.S.C. 6402). The 2021 advance payments were exempt by statute (26 U.S.C. 7527A(e)(3)); the 2021 lump sum on the return was not. Families with old federal or state debts, who are disproportionately the poorest, would see the monthly payment taken. That is a missing delivery mechanism for the dossier's central promise.
3. **The territories' child benefit rests on a misreading of 2021, and their income support is unplaced** (M-1). Section 4 says Puerto Rico is "paid by the territory with federal reimbursement, as the 2021 credit was". In 2021 Puerto Rico's families claimed the credit from the IRS on a federal return and got no advance payments; only mirror-code territories that elected and had a plan approved could pay in advance (26 U.S.C. 7527A(e)(4)). SNAP, SSI and the childless earned income credit mostly do not reach the territories at all, and no file says so.

**What can reach L3 once those land.** Every provision can. None is held back by an unspecified parameter. The open items are bounded working choices with ranges, or other owners' decisions:
- the child benefit's cost range, until a JCT or Treasury score;
- paid leave's take-up;
- the 2029 child-poverty rate;
- how the budget model records SS-8 (the booking step's);
- the repayment cap, the stipend's level, SS-7's trigger level and SS-8's share (working choices).

## How this review was done

- **Read.** The charter: the standards, the board, `DEC-2026-11-09-13`, `DEC-2026-11-10-05`, `-07` and `DEC-2026-11-12-06`, `-07`, `-09`. Care's parts B-D review (#260) as the model. Sections 3-9 in full; memos 1-7 and their status lines; sections 1, 2 and `legacy-research.md` where sections 3-9 draw on them; `provisions.json`; both tools; `models/data/budget/assumptions.csv`, ASM-FUND-LEAVE.
- **Mechanical checks.** A Standard subagent ran them; the reviewer checked what it reported before using it (see "Checks run" at the end).
- **The reviewer's own arithmetic** (not model runs): SS-8's yield at a 20% share (O-1); the leave fund at a faster step-up (A-1); the child benefit at $250,000 (section 7's example, reproduced: $4,660 against $5,000); the phase-out break-even incomes; the childless credit's phase-out against the ceiling's design rule (L-1).
- **Primary law looked up:** 26 U.S.C. 7527A (the 2021 advance payments' offset exception and possessions rules).

## 1. The decisions, carried out

Each decided item checked against section 4, `provisions.json`, sections 5-6 and the memos:

| Decision (`DEC-2026-11-12-06` unless noted) | Where | Verdict |
| --- | --- | --- |
| Memo 1 part 1 A, the American Family Act, no earnings test (point 1) | FAM-1.01, 1.03 | Faithful |
| Point 2 no: no $2,200 floor, the bill's phase-out | FAM-1.02; `6-cost.md` part 1 | Faithful; repriced (−$48 billion FY2030-39, −$5.8 billion FY2040) |
| Memo 1 part 2 B, the child's own ID, paid to the parent the child lives with (point 3) | FAM-1.04, 1.05 | Faithful. The payee rule has a gap for survivors of abuse (M-3) |
| Point 4, no repayment below 200% of poverty | FAM-1.06 | Faithful; the cap is a labeled working choice |
| Memo 2 B, records-based payment, one rail, front doors (points 5, 6) | FAM-1.07 to 1.10 | Faithful, but no offset or garnishment protection (B-1) |
| Memo 3 part 1 B, the 2021 childless credit permanent; point 9 | INC-1.01, 1.02 | Faithful. Its 15.3% phase-out sits below 200% of poverty, against memo 7's design rule as written (L-1) |
| Memo 3 part 2 B, SNAP restored, SSI's limits; point 8 | INC-2.01, INC-3.01, 3.02 | Faithful; neither reaches most territories (M-1) |
| Point 7, the refundable dependent care credit net of both guarantees | INC-4.01 | Faithful |
| Memo 4 B, paid on-ramps inside $100 billion; point 10 | LAB-10.01 to 10.05 | Faithful |
| Memo 5 B, twelve weeks, 85/69/50, job restoration, 0.6% to 1.10%, SSA, state equivalence | FAM-3.01 to 3.08 | Faithful. FAM-3.04 labels the 0.05-point step "decided"; ASM-FUND-LEAVE records the steps as unrecorded, not Espen's (A-1, C-4) |
| Memo 6 part 1 C, D8 with SS-5 and SS-8, SS-7 as fallback | SS-1.01, 2.01, 5.01, 8.01, 7.01 | Faithful in text; its effect is overstated (O-1) |
| Memo 6 part 2 yes (minimum benefit, CPI-E, caregiver credit); part 3 yes; points 11, 12 | SS-3.01, 4.01, B4.01, 11.01 | Faithful. SS-11's "zero if on time" has no cash-flow basis (O-2) |
| Memo 7 part 1 B, part 2 B | INC-5.01 to 5.03 | Faithful; the design rule needs its exception named (L-1) |
| `-09`: the $500 credit for other dependents ends | FAM-1.11; `6-cost.md` part 2 | Faithful; the saving is reported and not counted, as decided |
| `-07`, memo 6 C (rule 3) | FAM-1.04, 1.08, INC-2.01 | Faithful; cited, not re-decided |

## 2. Findings

IDs: B blocking delivery gap, O optimistic assumptions, M missing populations, A cheaper alternatives, F fiscal report, W weak evidence, L design lens, E section 9, C consistency and record. **Blocking** means blocking L3. Line numbers are at `6a029ae`.

### B. Delivery

**B-1. The monthly child benefit is not protected from offsets and garnishment. Blocking.**
- **What section 4 says.** FAM-1.07 pays the benefit monthly "under Treasury's permanent appropriation for refunds" and excludes it from income for programs (26 U.S.C. 6409) (`4-specification.md:40`). No provision says whether the payment can be offset or garnished. `grep` finds no "offset" or "garnish" in sections 4 or 5 for the child benefit.
- **The default.** A refundable credit is an overpayment the IRS may apply to past-due federal debts, child support, state income tax debts and unemployment overpayments before paying (26 U.S.C. 6402(c)-(f); 31 U.S.C. 3716, 3720A). Bank deposits are open to private creditors' garnishment unless the payment is protected.
- **What 2021 did.** The advance payments were exempt: "shall not be subject to reduction or offset pursuant to subsection (c), (d), (e), or (f) of section 6402 or any similar authority permitting offset" (26 U.S.C. 7527A(e)(3)). The half claimed on the 2021 return was not, and families lost it to offsets.
- **The scenario.** A single mother in 2030 with a defaulted federal student loan from 2012, or a state unemployment overpayment, is enrolled from records. Her $660 a month is taken in full until the debt is cleared. The families most likely to carry such debts are the poorest ones the benefit is designed for, and the records-based design (memo 2 B) reaches them precisely because they do not file.
- **Why blocking.** The benefit's delivery (who actually receives it) is an L3 element, and this omission undoes the central promise for a group the design targets. Under `DEC-2026-11-10-07` it is a missing delivery mechanism, not a bounded uncertainty.
- **The fix.** Add to FAM-1.07: the monthly payments, and any amount paid with the return, are exempt from reduction or offset under 26 U.S.C. 6402(c)-(f), 31 U.S.C. 3716 and 3720A and any similar authority, and from levy, as 7527A(e)(3) did; and deposits are protected from garnishment for two months' payments, as Treasury's rule protects federal benefits (31 C.F.R. part 212). Say whether child support arrears are excepted: the reviewer recommends no exception, because the payee is the parent the child lives with (FAM-1.05) and an offset would take the child's money for the payee's debts. This follows memo 2 B's and point 4's intent ("a mistake never becomes a debt"), so it needs no new decision. Price it: forgone offset collections, probably $1-3 billion a year (reviewer's judgment; the fix step should find Treasury Offset Program volumes and add an entry). Apply the same protection to INC-1.01's and INC-4.01's refundable parts only if the author judges it worth the forgone collections; that part is a working choice.

### O. Optimistic assumptions

**O-1. SS-8's effect at the specified 20% share, and the package's balance. Blocking.**
- **What is claimed.** SS-8 adds "about +0.5 to +1.0 (legacy estimate)" (`4-specification.md:107`; `6-cost.md:112`). The package is "about +4.0 to +4.6 against the 4.42% gap: at or near 75-year balance" (`6-cost.md:114`; `7-validation.md:15`). Memo 6 C chose SS-8 over a broad rate (memo 6 B) as the gap-closer.
- **The evidence.** EV-SEC-697 is a grade D legacy closers-table line with no share stated ("Invest part of the reserves in equities | +0.5 to +1.0 | estimate | No one directly; market risk"), qualified only by the Cassidy-Kaine fund (EV-SEC-466), which is a separate borrowed fund, not a reserve share.
- **The reviewer's arithmetic.** +0.5% of taxable payroll is about $60 billion a year in the 2030s (payroll about $12 trillion). At an excess return over Treasury bonds of about 3% a year, that needs about $2 trillion held in stocks on average; at 20%, reserves of about $10 trillion. The combined funds hold about $2.6 trillion today and fall to zero in 2034 under current law [EV-SEC-400]. The package's revenue (SS-1, SS-2 and SS-5 from 2031) roughly matches the funds' yearly shortfall in the early 2030s, so reserves stay in the low trillions, not near $10 trillion. At 20% of a few trillion, SS-8 yields on the order of +0.05 to +0.2. The package is then about +3.6 to +3.9 against 4.42, about 82-88% of the gap, and SS-7.01's one point (+0.9 to +1.0 if fully used [EV-SEC-697]) is needed nearly in full. SS-7.01 phases in at 0.1 point a year from a trigger read from 2035, so its full rate arrives around the mid-2040s, and its 75-year effect is below +0.9 on that timing.
- **What follows.** The decision stands. But the dossier presents SS-7 as a contingency that may not fire, and section 9 tells the public "if the gap returns, a small contribution increase starts automatically" (`9-public-case.md:40`). On this arithmetic the increase is the expected case. For Espen, this is the cost of the decision memo 6 did not show: C becomes, in practice, close to B with a delay.
- **Why blocking.** A load-bearing figure (the package's balance) rests on a D-grade estimate that its own specified share cannot reach, and it is stated as settled in sections 6, 7 and 9.
- **The fix.**
  - Section 6, part 4: show SS-8's yield as a function of its share and the reserves the package builds, with the reviewer's range (+0.05 to +0.2 at 20%) beside the legacy +0.5 to +1.0, and the package at about +3.6 to +4.6. Say SS-7.01 is expected to carry about 0.5 to 0.8 points. Sections 4 (SS-8.01, SS-7.01), 7 (part 1, Social Security row; part 5, the stock-market objection), 8 and 9 follow.
  - Put one question to Espen (below): keep C as decided, knowing the fallback is the likely closer; or raise SS-8's share (a working choice up to now) or start SS-7 earlier.
  - Investigation: SSA's score (point 12) settles it. It informs the booking and the question to Espen; the reviewer's arithmetic is enough to correct the record now, so it does not block.

**O-2. SS-11's loan is "zero if the 2030 act passes on time", with no cash-flow path. Not blocking.** `6-cost.md:62` and section 9 rest on the act's revenue starting in January 2031, before the retirement fund's depletion in the fourth quarter of 2032 [EV-SEC-400]. The dossier has no year-by-year trust-fund path for the decided package: the budget model's fund run carries a two-point broad rate the design does not have (the known gap, F-2). Whether the package's first-years revenue keeps the retirement fund (OASI, not the combined funds) above zero in 2032-34 is not shown; SS-1 and SS-2 revenue would need to be credited to OASI, or a reallocation from DI enacted. The fix: one line in SS-1.01/2.01/5.01 on which fund the revenue goes to (and a DI-to-OASI reallocation if needed), and a short annual path in part 4 once the booking settles SS-8's treatment. Bounded; for the booking step.

**O-3. The leave fund's margin at the ceiling. Bounded; label it.** At high take-up the mature cost is 1.01% of payroll plus SSA's 3% of benefits, about 1.04%, against the 1.10% ceiling (`6-cost.md:91-99`). That leaves about 0.06 points of payroll to repay a $182 billion loan, which is why repayment takes to 2058. Any take-up above the high case leaves the loan unrepaid. Section 8 has the trigger (`8-change-our-minds.md:20`). One sentence in part 4 saying how thin the margin is would let the settlement see it.

### M. Missing populations

**M-1. The territories. Blocking.**
- **The child benefit.** Section 4 says "Puerto Rico and the territories with mirror codes are paid by the territory with federal reimbursement, as the 2021 credit was (H.R. 2763's coordination with possessions; working choice to use it)" (`4-specification.md:131`; `5-delivery.md:76`). That misdescribes 2021. Puerto Rico has no mirror code: its residents claimed the 2021 credit from the IRS on a federal return. The advance payments excluded them (26 U.S.C. 7527A(e)(4)(A) applies section 24(i)(1) "without regard to the phrase 'or is a bona fide resident of Puerto Rico'"). The mirror-code territories (Guam, the U.S. Virgin Islands, the Northern Mariana Islands) paid advances only if they elected and Treasury approved a plan; American Samoa only through an approved plan (7527A(e)(4)(B)-(C)). So in 2021 almost no territorial child got monthly payments. Memo 2 B's records-based monthly payment is not designed for any of them, and no evidence entry supports the sentence.
- **Income support.** SNAP does not run in Puerto Rico, American Samoa or the Northern Mariana Islands (they get nutrition block grants). SSI does not reach Puerto Rico, Guam, the Virgin Islands or American Samoa (only the Northern Marianas). Puerto Rico's residents mostly do not file federal returns, so the childless earned income credit (INC-1.01) does not reach them; ARPA's federal match for Puerto Rico's own earned income credit is the existing channel. No file says any of this, so INC-2 and INC-3's "every household" framing silently leaves out about 3.5 million people.
- **Paid leave and Social Security** do reach the territories (covered earnings), but FAM-3's contribution base and SS-1's revenue are not checked for them; one sentence each.
- **Why blocking.** Who is eligible and how they are paid are L3 elements. Health's and care's reviews held the same gap blocking (care's M-1).
- **The fix.**
  - Section 4: rewrite "Where particular groups fall" for the territories from the statute: Puerto Rico's families paid monthly by the IRS directly (the benefit is federal, so this needs only that FAM-1.07 not exclude them), and the mirror-code territories and American Samoa paid by the territory with full federal reimbursement and a Treasury-approved monthly plan as a condition, with the IRS paying directly where a territory declines. Add register entries for 7527A(e)(4) and section 24(k).
  - Name what INC-1 to INC-3 do in the territories: today's channels (the nutrition block grants, the Puerto Rico earned income credit match, the Northern Marianas' SSI) and whether the floor raises them. Extending SSI to Puerto Rico, Guam, the Virgin Islands and American Samoa is a new benefit for a group, so it is a fork for Espen, not a fix: put it to Espen with a cost (reviewer's judgment, a few billion dollars a year; the fix step should find CBO's or SSA's estimate), or record it in section 8 as left open with its alternatives.
  - Section 6: the territories' child benefit and any block-grant top-up priced outside the total, with a range.

**M-2. Tribal nations. Not blocking.** No file mentions tribes. Each needs a sentence, not a decision: front doors at tribal offices and IHS facilities (FAM-1.10), which matter more than SSA offices in much of Indian Country; LAB-10's grants through WIOA's Native American programs (section 166) and tribal workforce boards; SNAP's restoration alongside the Food Distribution Program on Indian Reservations, which households choose instead of SNAP; paid leave's coverage of tribal government employers; and the records match (FAM-1.08) reaching IHS and tribal enrollment records only with tribal consent.

**M-3. Survivors of domestic violence under the payee rule. Not blocking; a design-lens gap.** FAM-1.05 keeps payment with the current payee during a dispute, decided within 60 days (`4-specification.md:38`; `5-delivery.md:63`). A parent who leaves an abusive partner with the children loses two months or more of the benefit to the person they fled, and the review could put the two in contact. The fix: a payee change on a statement that the child now lives with the claimant, effective the next month, with the burden on the other parent to dispute it; an address-confidentiality rule; and no joint notice. It is one sentence in FAM-1.05 and fits point 3 as decided.

**M-4. Groups placed well.** Mixed-status families, foster and kinship care, people without a fixed address, people in prison or jail, SSI and SSDI recipients and the self-employed are each placed (`4-specification.md:129-135`). Children with no identification number of any kind are named as still missing out (`7-validation.md:56`), which is honest; their number is not given, and should be, from the register (EV-SEC-016 counts the parent rule, not children with no number).

### A. Cheaper alternatives

Memo 1 weighed the large cheaper design (B, a Canada-style taper, about $0.9-1.3 trillion less), and Espen chose A. Memo 3 weighed C. The reviewer found no unweighed cheaper design reaching the same people for the general-fund lines. One for the leave fund:

**A-1. A faster step-up removes the paid leave fund's loan. Not blocking; for Espen as a question.**
- **The known gap, confirmed.** At high take-up the loan peaks at about $182 billion in FY2040 as booked ($185 billion on the fund's own scale) and is repaid in 2058 (`6-cost.md:99`, `:103`). The board's earlier $124 billion and 2048 left out SSA's administration. Reproduced roughly by the reviewer from part 4's own rows: about $174 billion in FY2040 at 4% interest.
- **Why it arises.** The rate starts at 0.6% and steps 0.05 points a year, reaching 1.05% only in 2040, while benefits reach about 0.9-1.0% of payroll by 2033.
- **The alternative.** The same 0.6% start and 1.10% ceiling with 0.10-point steps (from 2032) reach the ceiling in 2036. On part 4's own payroll, benefits and administration, the fund then never borrows: its balance bottoms out at about $13 billion in 2035 and is about $70 billion in 2040 (reviewer's arithmetic, 4% interest). It avoids roughly 25 years of interest on a loan of up to $180 billion, paid by workers' later contributions, and the risk in O-3.
- **What it costs in burden.** Workers reach the ceiling's $330 a year (at $60,000) about five years sooner. Nothing else changes for anyone.
- **Who decides.** ASM-FUND-LEAVE records "the start rate and steps unrecorded"; only the 1.10% ceiling is Espen's (October 26). `DEC-2026-11-12-06` decided "the 0.6% contribution stepping to the 1.10% ceiling", not the step. So the step is a working choice the dossier can set, but it is an adopted model input (`models/data/inputs/funds-parameters.csv`), so changing it is tier 3. The reviewer recommends offering Espen the faster step as a yes-or-no point with the booking.

### F. The fiscal-rule report (`DEC-2026-11-10-05`) and the money

**The report itself follows `DEC-2026-11-10-05`.** Section 6, part 5 gives the yearly cost (about $196 billion in FY2030 rising to $278 billion in FY2039 on the general fund), the permanent cost from FY2040 ($284 billion, 0.53% of GDP), the net change a booking would make (+$469 billion over FY2030-39 and +$55.8 billion in FY2040) and the share of the plan-wide margin (about 1.3% of a $4,182.6 billion FY2040 gap; 6.7% for the whole floor). It is on one basis (fiscal years, against the booked case `mixed` at `34faa21`), shows the booking beside it and says why they differ (the floor declined; the new lines). Spending lines and revenue effects stay apart: the leave fund's income-tax offset is its own line, and the new lines are said to carry none. Part 2 lists what the total leaves out with amounts, keeping contingent items (SS-11, SS-7) apart from firm ones. It treats the gap as a figure to report and sends no part of it to Espen. That is right: memo 1 already put the large money choice (A against B) to Espen.

**F-1. The plan-wide gap's base is out of date. Not blocking; a record fix.** Part 5 uses $4,182.6 billion short in FY2040 and $4,238 billion with the booking (`6-cost.md:136`), at commit `34faa21`. A build at the head gives **$4,184.7 billion** (case `mixed`, 7.73% of GDP), the figure `DEC-2026-11-12-08` records "instead of 4,182.6"; with the booking it is about $4,240.5 billion. The 1.3% and 7.8% hold; the whole floor's share is 6.8% of the unbooked gap, not 6.7%. Restate part 5 on the head's figure, and cite `DEC-2026-11-12-08` rather than `34faa21`.

**F-2. The Social Security booking (the known gap), confirmed and sharpened.** `6-cost.md:118` is right that the budget model runs its own fund model with a two-point broad payroll rate phased in over 2035-44, which the decided design has only as a one-point fallback, so the booking overstates trust-fund revenue and the general fund's income-tax offset ($520 billion over FY2030-39, $90 billion in FY2040). Given O-1, the correction is smaller than "remove the broad rate": the decided design's expected case has SS-7.01 carrying most of a point from the late 2030s. The booking should replace the two-point rate with SS-7.01's one-point path at its trigger, as the expected case, and SS-8 at the reviewer's low yield until SSA's score, and record how SS-8's stock purchases are treated (open, `6-cost.md:118`). The SS-1 ledger note's "net −$2.75T" against its −$4.74 trillion path should be corrected in the same PR (`6-cost.md:147`).

**F-3. Items not counted, in both directions. Not blocking; label them.**
- B-1's offset protection: forgone collections, a cost (about $1-3 billion a year, judgment).
- The territories' child benefit (M-1), if the territories' own reimbursement is not already in the booked FAM-1 range: say whether it is.
- The leave fund's loan interest (about $5-7 billion a year at the peak, fund-paid) and the general fund's exposure as lender: one memo line in part 5, since the loan is general-fund money lent to the fund even though it is not a general-fund cost.
- Care's review (F-2 there) noted that the child care guarantee shrinks the dependent care credit's base. INC-4.01 prices refundability net of both guarantees (`3-design.md:192`), so that seam is closed from this side.

**F-4. The booking list (part 6), reviewed for correctness only.** It will be the lead's tier-3 PR. Its structure is right: FAM-1 to 1.65/1.85/2.05 with its note; five INC rows and a FAM-1 delivery component with year shapes from the tool; LAB-10 named in `provisions.csv`; no FAM-3 change; Social Security re-specified; incidence keys updated; DY3 kept as a sensitivity. Points to add:
1. B-1's and M-1's lines once priced.
2. Social Security per F-2: SS-7.01's one-point expected path, not zero and not two.
3. If Espen takes A-1, `funds-parameters.csv`'s step from 0.05 to 0.10 and the loan rows re-run.
4. The incidence row for FAM-1 should use the decided design's distribution (part 6, item 6), and INC-1's key should be low-wage workers without children, not the child credit's.

### W. Weak evidence

**W-1. Load-bearing D and E entries.** Three figures that sections 6, 7 or 9 rely on rest on legacy grade D estimates:
- SS-8's +0.5 to +1.0 (EV-SEC-697): O-1.
- SS-7's +0.9 to +1.0 (EV-SEC-697): its timing under SS-7.01's trigger is not the legacy table's.
- The leave fund's 2058 repayment (EV-SEC-694): reproduced roughly here (A-1), so it holds as a project estimate.

The child benefit's $1.85 trillion is a legacy planning range checked against TPC and the CPS; section 6 says so and keeps it untrimmed, which is the right treatment. The registry warnings for the EV-SEC block are under "Checks run".

**W-2. Search-extract quotations.** Section 3 asks the reviewer to spot-check EV-SEC-600 to 673, which were taken from search-tool extracts, and EV-SEC-610's flattened table row in particular (`3-design.md:261`). The subagent's check is under "Checks run"; the rest is for the fix step's Standard subagent against the originals. Not blocking: the figures they carry (the childless credit's TPC and JCT scores) agree with each other.

**W-3. The floor's tool runs outside the repository.** `tools/afa_floor.py` needs the CPS ASEC 2026 archive, which is not committed (correctly). Section 6's floor figures therefore reproduce only where the archive is fetched. The fix step should record the fetch command and the archive's hash in the tool's docstring (the hash is in `6-cost.md:9`), so a reviewer can re-run it. The board's nit (the docstring should cite sec. 1(f)(6), not 1(f)(4)) is already fixed at the head (`tools/afa_floor.py:28`); the lead can drop it from "Known gaps".

### L. Design lens (`DEC-2026-11-09-13`)

The design is strong on the lens:
- no earnings test, no work condition anywhere (FAM-1.03, LAB-10.04);
- payment from records, confirmed by silence (FAM-1.08);
- one attestation for the payee, a short review in disputes (FAM-1.05);
- a safe harbor so honest mistakes never become debts (FAM-1.06);
- the floor's payments never counted against other programs (INC-5.01), and one income finding reused (INC-5.03);
- the ceiling met by design rules with published counts and a review trigger, not a statutory cap (INC-5.02);
- SNAP's work-rule paperwork and SSI's asset test for savings up to $10,000 removed.

Section 4's burden table (`4-specification.md:157-170`) does what the template asks for the child benefit, paid leave and LAB-10. Gaps:

**L-1. The childless credit's phase-out against the ceiling's design rule. Not blocking; a record fix.** INC-5.02's first design rule is "no plan benefit adds a phase-out below 200% of poverty" (`4-specification.md:120`; memo 7, `:65`). INC-1.01 doubles the childless credit's phase-out rate to 15.3%, over roughly 75-140% of poverty for a single adult. Memo 7 counted it (the single adult at 40-57 cents), so the decided set meets the ceiling; but the rule as written is broken by a decided provision. Fix: the rule reads "no plan benefit adds a phase-out below 200% of poverty beyond those this dossier's decided design sets out (INC-1.01's)", and the burden table gains an INC-1.01 row (its 15.3 cents, what it buys, why kept).

**L-2. Rows the burden table leaves out.** INC-1.01 (above); INC-4.01's claim (Form 2441 with provider information, the main reason eligible families do not claim); FAM-3.03's recent-earnings test (a test, though a light one); and SS-B4.01's 960-hour record (who certifies unpaid care hours, and how, is unstated: self-attestation with SSA's records of the child's or relative's age is the low-burden choice). Each needs a line; SS-B4.01's certification needs a sentence in section 4.

**L-3. M-3's payee rule** is the one place the design puts the burden on the person in the worst situation.

### E. Section 9 against sections 1-8

Every number in section 9 traces to sections 1-8 with its evidence ID or as labeled project arithmetic (the subagent's table check is under "Checks run"), and "on our estimates" is used where it should be. The cost is stated plainly ($1.85 trillion, $2.47 trillion, $284 billion a year), the losers above $210,000 are named, and the can't-say list refuses "solved for 75 years". That is better than housing's first draft.

**E-1. Social Security, as part of O-1. Blocking with O-1.** "If the gap returns, a small contribution increase starts automatically" (`9-public-case.md:40`) and "closes most of the gap" (`:17`) should match whichever reading of SS-8 lands. On the reviewer's arithmetic: "a contribution increase of up to one point, split between workers and employers, is expected to start in the late 2030s".

**E-2. Job restoration's vehicle. Not blocking.** "Paid leave, from 2031 ... with your job back" (`:15`, `:31`; story at `:46`). Job restoration (FAM-3.07) rides the 2030 Social Security act, a regular-order bill needing 60 votes or the rules reform (`4-specification.md:19`, `:25`); paid leave's benefit rides R2. If the act stalls, leave arrives without job protection. Section 9 should carry the condition, or the fix step should move FAM-3.07 to a vehicle with a better chance (its own short bill, or the work flagship's labor bill, which section 4 names as the alternative). The 90-day job-tenure condition also belongs in the story.

**E-3. Smaller points. Not blocking.**
- "About 3 million fewer poor children" (`:19`) against section 6's "about 3 million to 3.5 million": say "3 million or more".
- The paragraph's "no child is left out because a parent earned too little" (`:23`) is right; "every child counts" (`:28`) should not imply children without a number are reached (section 7, part 4).
- The source table cites "Section 4, SS-11.01" for "late 2032, 78%" (`:72`); the figure's home is section 1, part F and EV-SEC-400. Fine as is, but name section 1.

### C. Consistency and record

- **C-1. Memo 6's stale figures (the known double count, confirmed).** Memo 6's decision line and part 2 (`memos/6-social-security.md:5`, `:75`), `memos/README.md:14` and section 3's cost table (`3-design.md:83`) say "+4.2 to +4.7 from part 1 ... −0.5 to −0.6 from part 2", which counts SS-3 and SS-4 in both. Section 6 corrects it to +4.0 to +4.6 (`6-cost.md:116`). Mark the memo and section 3 with the corrected figure beside the decided text (the memo's text stays as decided), and then restate all of them per O-1.
- **C-2. "$340 a child".** Section 8 says families above about $210,000 lose "about $340-1,100 a child" (`8-change-our-minds.md:10`). $340 is a two-child family's loss at $250,000 (section 7, `7-validation.md:47`), not a per-child figure; per child the loss is up to about $500 in 2030 and $1,100 by 2040 (`6-cost.md:47`).
- **C-3. The leave loan's trigger.** Section 7 sets the review trigger at "loan above about $185 billion, the booked peak" (`7-validation.md:79`); the booked peak is $182 billion, $185 billion on the fund's own scale (`6-cost.md:103`). Name one.
- **C-4. FAM-3.04's label.** It marks the 0.05-point step "decided (memo 5 B; Espen, October 26)" (`4-specification.md:89`). Espen decided the 0.6% start and the 1.10% ceiling; the step is a legacy working choice (ASM-FUND-LEAVE). Label it so (A-1).
- **C-5. The cost objection.** Section 7's "It costs too much" answer gives the child benefit's $1.85 trillion and then "about 1.3% of the plan-wide FY2040 gap beyond what is already booked" (`7-validation.md:62`). The 1.3% is the whole set's net change; the child benefit's own net change is a saving against the booking (−$5.8 billion in FY2040). Say which.
- **C-6. Section status lines.** Sections 4-9 read "draft (stage D, board row S4, PR 1/2)". After this review they should read "reviewed (L2); L3 after the fix steps", and the README's status line likewise.
- Items the subagent's checks found are under "Checks run".

### Seams with other dossiers

- **Care.** INC-4.01's base is net of both guarantees, closing care's F-2 from this side. Care's review asked that HLT-4.04's $10,000 Medicaid limit not be read back into SSI; INC-3.01 uses the same figure for SSI on its own (the SSI Savings Penalty Elimination Act), which is consistent. SS-B4.01 counts paid care hours as earnings and never toward the credit, as care asked. Child care's copay slope (9-23 cents) is cited at `4-specification.md:125`; the household model checks the overlap.
- **Immigration.** Rule 3 is cited, not re-decided (FAM-1.04, FAM-1.08, INC-2.01); SNAP's sec. 10108 is priced here once. No change while I4 is in review.
- **Health.** SS-11 and the 2030-34 premium-credit layer are the seams; both are named.
- **Clean power.** FAM-1.09's rail is a proposal; built for the child benefit whatever clean power decides. Good.
- **Work.** FAM-3.07's vehicle (E-2) and LAB-8 are the seams.

## For Espen

Two questions, each about a cost or gap of a decision already made; neither reopens it.
1. **Social Security's gap-closer** (O-1). "On our arithmetic, investing up to 20% of reserves in stocks closes about 0.05-0.2% of payroll, not the 0.5-1.0 the memo assumed, so the one-point fallback rate rise is likely to be needed in the late 2030s. Keep memo 6 C as decided, with that stated? Or (a) raise the share of reserves invested, or (b) start the fallback earlier?" The reviewer recommends keeping C as decided and stating it plainly; SSA's score (point 12) can refine it in 2027-28.
2. **The leave fund's step-up** (A-1), with the booking. "Paid leave's contribution steps up 0.05 points a year, so the fund borrows up to about $182 billion and repays it in 2058. Stepping 0.10 points a year to the same 1.10% ceiling avoids the loan; a worker at $60,000 reaches $330 a year about five years sooner. Switch to 0.10?" The reviewer recommends yes.

Possibly a third, from M-1, if the fix step judges it a real fork rather than leaving it open: "Extend SSI to Puerto Rico, Guam, the Virgin Islands and American Samoa (about a few billion dollars a year, to be priced)?"

## What the next steps should do

For a fresh Most capable fix session started by the lead (S4's author takes on nothing more), unless marked for the lead. In order: steps 1-3 clear the blockers, and step 6 follows them.

1. **The child benefit's protection from offsets** (B-1).
   - FAM-1.07: exempt the monthly payments and the return amount from offset (26 U.S.C. 6402(c)-(f), 31 U.S.C. 3716, 3720A) and levy, and protect two months' deposits from garnishment; no child-support exception, with the reason.
   - Price the forgone collections in section 6, part 2, with an entry for Treasury Offset Program volumes; register entries for 7527A(e)(3) and 6402.
   - Sections 5 (remedies) and 7 (reach) follow.
   - **Tier:** Most capable (legal drafting). Routine PR.
2. **The territories, tribes and survivors** (M-1, M-2, M-3, M-4).
   - Section 4: the territories' child benefit rewritten from the statute (IRS-direct for Puerto Rico; reimbursed territorial plans with a monthly-payment condition elsewhere, IRS-direct where a territory declines); what INC-1 to INC-3 do in the territories; one sentence each for tribal front doors, LAB-10 through WIOA section 166, FDPIR, tribal employers and consent for tribal records; FAM-1.05's survivor rule; the count of children with no number.
   - Section 6: the territories priced outside the total, with a range.
   - If SSI's extension to the territories is put as a fork, stop and send the yes-or-no point to the lead for Espen; do not write it either way until answered.
   - **Tier:** Most capable, with a Standard subagent for the register entries (7527A(e)(4), section 24(k), the territories' child counts, SSI's and SNAP's territorial rules). It can share a PR with step 1.
3. **Social Security's package** (O-1, O-2, E-1, C-1).
   - Section 6, part 4: SS-8's yield by share and reserves, with the reviewer's range beside the legacy one; the package at about +3.6 to +4.6; SS-7.01 as the expected closer, with its timing; which fund the revenue is credited to.
   - SS-7.01, SS-8.01 and SS-1.01/2.01/5.01 in section 4; section 7 (part 1, the stock-market objection), section 8 and section 9 (`:17`, `:40`) to match.
   - Memo 6, `memos/README.md:14` and `3-design.md:83`: the corrected figures beside the decided text.
   - Put question 1 (above) to the lead for Espen in the PR's "For the board".
   - **Tier:** Most capable. It can share a PR with steps 1 and 2.
4. **Section 6's smaller items and the leave fund** (F-1, F-3, O-3, A-1, C-3, C-4).
   - The plan-wide gap re-read at the head; part 2 rows for B-1's and M-1's costs and the loan's interest; the leave margin sentence; the faster step-up shown as an alternative with its loan path (re-run on the funds model, not by hand); FAM-3.04's label; one loan trigger figure.
   - Put question 2 to the lead for Espen.
   - **Tier:** Standard, with the reviewer's arithmetic re-done on the model. It can share a PR with step 3.
5. **Lens, evidence and tools** (L-1, L-2, W-2, W-3).
   - INC-5.02's rule with INC-1.01's exception; burden-table rows for INC-1.01, INC-4.01, FAM-3.03 and SS-B4.01; SS-B4.01's certification sentence.
   - The spot-check of EV-SEC-600 to 673 against originals.
   - `afa_floor.py`'s docstring: the archive's fetch and hash.
   - **Tier:** Standard. It can share a PR with step 4.
6. **Section 9 and the record** (E-1 to E-3, C-2, C-5, C-6), after steps 1-3.
   - Social Security's wording per step 3; job restoration's vehicle and its 90-day condition (or move FAM-3.07 to its own short bill, a working choice); "3 million or more"; the per-child loss figure in section 8; the cost objection's 1.3%; section status lines "reviewed (L2)".
   - **Tier:** Most capable for section 9; the record fixes by a Light subagent.
7. **The booking** (F-2, F-4; `6-cost.md`, part 6). For the lead, after steps 1-4.
   - The tier-3 PR: FAM-1 to 1.65/1.85/2.05; the INC rows and the FAM-1 delivery component; LAB-10's name; Social Security with the two-point rate replaced by SS-7.01's one-point expected path and SS-8 at the low yield, and SS-8's purchases' treatment recorded; the SS-1 ledger note corrected; the incidence rows; B-1's and M-1's lines; the leave step if Espen takes A-1.
   - **Who:** the lead's booking. Espen's label.
8. **A short L3 re-check** by the standing reviewer, limited to B-1, M-1, O-1 and the re-run. Then the lead moves FAM-1, FAM-3, LAB-10, INC-1 to INC-5 and the SS items to L3 in `agenda/agenda.csv` and the README.

## Checks run

A Standard (Sonnet) subagent ran these at `6a029ae`; the reviewer checked its readings against the files before using them, and re-did the loan and the plan-wide gap by hand.

- **The path.** `tools/secure_floor_path.py` runs and reproduces every cell of `6-cost.md` part 1 within 0.1 ($2,469.06 billion and $284.43 billion unrounded; booked $2,000.0 and $228.7 billion; new lines $516.7 and $61.6 billion; floor −$47.7 and −$5.8 billion; net +$469.1 and +$55.8 billion). Re-adding the printed cells gives rounding differences only (the total row's cells add to $2,468.8 billion). The anchors in the tool's comments match part 1's "other paths" bullet.
- **The floor tool.** `tools/afa_floor.py` needs the CPS archive (`--archive`), which is not in the container, so its tax-year values could not be re-run (W-3). Its values (`FLOOR_TY`) match part 1's floor table, and the fiscal-year conversion is the monthly rule (0.75 of the tax year plus 0.25 of the year before), as part 1's counting rule says.
- **Paid leave.** Part 4's rows match the recovery-budget model's audit lines; the offset is 12.5% of contributions every year. With no interest the loan would be $159 billion in FY2040; the printed $182 billion includes interest at the Treasury rate (`model.py:119-121`). The model's own `leave` rows are about 2% higher ($185.4 billion in FY2040), the macro scale part 4 names; repayment is 2058 (`leave_repayment_year`). `1-problem.md:121` and memo 5 say "near $185 billion"; no stale $124 billion or 2048 remains in the dossier.
- **The budget model.** Built in a copy of the head: `recovery-budget.json` is byte-identical to the committed one. FAM-1 $1,900.0 and $214.7 billion; LAB-10 $100.0 and $14.0 billion; Social Security trust-fund revenue $5,697.5 billion over FY2030-39; its income-tax offset $520.1 and $90.0 billion; the leave offset $158.6 and $25.6 billion. All as section 6 states. The plan-wide gap is $4,184.7 billion (F-1).
- **IDs.** All 447 EV-SEC IDs cited exist in `evidence.json` (491 entries); every SRC behind them is in `library/catalog.csv`; all 21 DEC IDs cited exist; all 42 provisions in `provisions.json` are in section 4, and every provision ID cited exists (HLT-4.04 and HLT-9.05 are care's). 44 register entries are cited nowhere; the fix step should either cite or drop them.
- **Statuses.** Every memo's status line says decided. Every provision's `decisions` array includes `DEC-2026-11-12-06`; FAM-1.11 has `-09`; FAM-1.04, 1.08 and INC-2.01 have `-07`. "Proposed" on FAM-1.09 and LAB-10.05 means proposed to other dossiers, which is right, though the wording could say "decided yes, as a proposal". Leftovers: `3-design.md:229` "Proposed notes, for Espen with memo 7" (memo 7 is decided), and `README.md:137` "Open questions for Espen" over a body that says none is open. `README.md:110` names fair financing as Codex's; it is Claude's (`DEC-2026-11-11-07`).
- **Registry.** `models/registry/check.py` passes with 52 EV-SEC warnings: 13 uncorroborated analysis entries (146, 228, 446, 447, 449-454, 467, 469, 473) and 39 contested ones. Two matter here. EV-SEC-447 to 454 are SSA's single-provision scores, flagged only for want of a second publisher; SSA's actuaries are the standard source and the flag is not a defect. EV-SEC-212 (the 2021 payments' "no effect on work") is contested, and section 9 states it flatly (`9-public-case.md:36`); the next sentence gives the other side, which is the template's treatment, but "found no effect" should read "found little or no effect".
- **The agenda.** FAM-1, FAM-1D, FAM-3, FAM-3A, LAB-10, SS-1 to SS-5, SS-7, SS-8, SS-B4, SS-11 and INC-1 to INC-5 are homed here at L2 `decided`, citing `DEC-2026-11-12-06` (INC-2 also `-07`); the alternatives are L2 `alternative`. That matches.
- **Section 9.** Every number traces to sections 1-8. Two source-table rows point to the wrong section (E-3): "late 2032, 78%" and "$2,000 since 1989" live in sections 1 and 3.
- **Other stale figures.** Memo 1 and `3-design.md:76` keep "$1.9 trillion / about $220 billion" as decided text, with the repricing noted in the memo's status line; that is acceptable. Memo 6's +4.2 to +4.7 is C-1.
- **Checks.** `bash .github/scripts/run-checks.sh` on this branch: passes (77 tests; "All checks passed").
