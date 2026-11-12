# Care you can count on, parts B-D (long-term care, child care and pre-K, the care workforce): L2/L3 milestone review

Role: the independent milestone review of the care dossier's parts B, C and D (`charter/PLAN.md` 3.2 and 5, "Review"; `charter/STANDARDS.md`, "Milestone review"), board row D-9r. The reviewer wrote none of the dossier. It tries to break the work on four fronts (weak evidence, missing populations, optimistic assumptions, cheaper alternatives). It also applies the design lens (`DEC-2026-11-09-13`), checks the fiscal-rule report against `DEC-2026-11-10-05`, checks consistency across sections 1-9, `provisions.json`, the memos and `agenda/agenda.csv`, and checks section 9 against sections 1-8. Status: current, as of main at commit `ee90299` (November 12, 2026, after #254 and #259). Reviewer: Claude Code, `session_01UQzgBwJgAerLpBpSRY`. It changes nothing in the dossier. Every fix below is a later step: the fix steps go to D-9's author, `session_01UQzgBw9VK9o3iPPDppbRg7`, and the booking to the lead.

Espen's decisions on parts B-D (`DEC-2026-11-11-02` to `-06`), health's decisions (`DEC-2026-11-10-09` to `-13`, `DEC-2026-11-11-01`) and `DEC-2026-11-11-07` (the settlement is now Claude's) are settled. Where a decided choice has a consequence the dossier does not show, this review says so; it does not argue the choice. Under `DEC-2026-11-10-07`, a clearly bounded uncertainty is not a defect. Every investigation asked for below names the decision it informs and whether it blocks that decision now.

## Verdicts

| Level | What it needs (`charter/PLAN.md` 3.2) | Verdict |
| --- | --- | --- |
| **L2, design** | Key parameters chosen (who, what, how much, who administers), with the main alternatives weighed | **Pass** (record fixes only, none blocking) |
| **L3, specified** | Provisions section by section (eligibility, benefit, administration, phase-in, remedies); evidence for each load-bearing claim; a cost range validated by models with stated limits; a delivery plan | **Not yet: close.** Three blockers |

**Why L2 passes.** Every fork in parts B-D (memos 6-16) had two to four options weighed on evidence, with a bill-by-bill table, benchmarked costs and the legacy designs as options. Memo 17's cost-down set followed Espen's cost direction. All are decided and recorded (`DEC-2026-11-11-02` to `-06`). The agenda rows HLT-4, HLT-9, HLT-10, HLT-11, FAM-2, FAM-2A and FAM-2G are L2 `decided`, and FAM-2B to 2F are L2 `alternative` (`agenda/agenda.csv:271-277`, `:288`, `:297`, `:515-517`). Five memo status lines still read "for Espen, not decided" (C-1). That is a record fix: the decision log, section 3c and section 4 all carry the decisions.

**Why L3 is not yet.** Most of L3 is in place:
- section 4 specifies 44 provisions with parameters, vehicle, agency, current-law change and evidence;
- section 5 has a timeline, remedies, states' roles and a rural plan;
- section 6 prices the decided designs on fiscal years and reproduces from its scripts (below);
- sections 7 and 8 give benchmarks, objections, triggers and hard stops.

The blockers:
1. **Room and board brings back the asset test that memo 8 C removed** (B-1). Memo 8 C, as decided, gives residents who cannot pay room and board Medicaid's help "with no asset test beyond income". Section 4 applies HLT-4.04's $10,000 limit to that help (HLT-4.04, HLT-4.08). Sections 7 and 9 then promise that savings are never spent down. Most long-stay nursing-home residents cannot pay room and board from income, so for them the decided protection, and section 9's headline promise, do not hold as specified. This is an inconsistent commitment against a decision, so it is a defect, not a bounded uncertainty.
2. **The territories are absent from parts B-D** (M-1). Health placed them (HLT-7.28). Parts B-D do not say whether children in Puerto Rico, Guam, the U.S. Virgin Islands, the Northern Mariana Islands and American Samoa get the child care guarantee and pre-K. They do not say how the bridge and the 2030-34 wage floor work under the territories' capped Medicaid allotments, or what the territories pay under HLT-9.09. This is the same class as health's blocking M-1.
3. **School-age children now on child care subsidies lose them** (M-2). Part C nets all of today's CCDF money (about $12 billion) into the under-5 guarantee (`3c-design-child-care.md:76`, `:81`), while school-age care is outside its scope (`1c-problem-child-care.md:9`). Nothing keeps CCDF for the children aged 5-12 it serves today. A design that silently ends a current benefit for a group it never weighs is a decision-changing omission.

**What can reach L3 once those land.** Every provision can. None is held back by an unspecified parameter. The open items are bounded working choices with ranges, or other owners' decisions:
- part B's new-user count and cost;
- the tier amounts;
- the room-and-board share;
- under-3 take-up;
- where part C is booked (the settlement's);
- the family-caregiver decision point (study in implementation).

## How this review was done

- **Read.** The charter: the standards; the board's stage D rows D-4r to D-9 and questions 0k to 0n; plan section 3.2's levels; `DEC-2026-11-10-05`, `-07` and `DEC-2026-11-11-02` to `-07`. Health's milestone review as the model, and the part B audit. Sections 4-9 for parts B-D in full. The parts of sections 1b-3d and memos 6-17 that sections 4-9 draw on, and every memo's status line. `tools/care_repricing.py`, `care_bcd_path.py` and `care_bcd_margin.py`. Health's HLT-7.17 and HLT-7.28 (`4-specification.md:51`, `:86`) and health's sections 6 and 8, where parts B-D lean on them.
- **Mechanical checks.** A Sonnet subagent ran them. The reviewer checked what it reported before using it, re-derived the totals by hand, and corrected one of its readings (C-4).
  - **Models.** All three scripts reproduce section 6:
    - FY2030-39: $3,537 billion; FY2040: $729.1 billion. By part: B $1,789 billion and $436.7 billion; C $1,149 billion and $176.2 billion; D $600 billion and $116.1 billion.
    - With part 2's items: $3,574 billion and $735.4 billion.
    - Net of what is booked: $2,432 billion and $580 billion. Of which long-term care and its workforce $1,811 billion and $456 billion; child care, pre-K and parity $622 billion and $124 billion.
    - Already booked: HLT-4's long-term care component $319 billion and $44 billion; the EDU-9B care component $786 billion and $106 billion.
    - The plan-wide FY2040 general-fund primary balance in case `mixed`: $3,749.6 billion short as booked; $4,205.7 billion with long-term care booked; **$4,242.7 billion with part C in the EDU-9B fund**; **$4,403.4 billion with part C on the general fund**. The fund's grant is $98.1, $135.2 and $66.3 billion.
    - Memo 17's decided totals: $3.80 trillion and $736 billion, on calendar and school years.
    - `care_bcd_margin.py` needs `build/fiscal-model.json`. It was run in a built copy of the repository; nothing was written to the branch.
  - **Sums.** Every table in section 6 re-adds within rounding ($1-2 billion). The calendar-to-fiscal bridge (`6bcd-cost.md:53-58`) adds to $3.88 trillion against the printed $3.89 trillion, which is rounding.
  - **IDs.** Every EV-CAR ID cited in parts B-D exists, and every source behind EV-CAR-400 to 647 is in `library/catalog.csv`. Every DEC ID cited exists. All 44 provisions (HLT-4.01-4.08, HLT-9.01-9.11, HLT-10.01-10.07, HLT-11.01-11.05, FAM-2.01-2.11, FAM-2G.01-2G.02) are in section 4, and every provision ID in sections 4-9 exists. No entry in EV-CAR-400 to 647 is uncited.
  - **Statuses.** No provision is still "proposed" or "for Espen". Five provisions' `decisions` arrays omit `DEC-2026-11-11-06`, which their text relies on (C-2).
  - **Registry.** `models/registry/check.py` passes. It gives 18 warnings in EV-CAR-400 to 647: ten uncorroborated analysis entries and eight contested entries (W-1).
  - **"Codex".** No line in parts B-D still says the settlement is Codex's.
- **The reviewer's own arithmetic.**
  - Pre-K's federal share against FAM-2.08's text (C-3).
  - The room-and-board help cost of following memo 8 C (B-1).
  - The child care copay's implicit marginal rate (design lens).
  - The joint exposure on health's offset instrument (F-1).
- **Checks.** `bash .github/scripts/run-checks.sh` passes on this branch.

## 1. The decisions, carried out

Each decision the brief listed, checked against section 4, `provisions.json`, sections 5-6 and the agenda:

| Decision | Where | Verdict |
| --- | --- | --- |
| Memo 6 B: the benefit in the single plan from January 1, 2035, no asset test, the 2030-34 bridge (`-02`) | HLT-4.01, HLT-9.01-9.07; `5bcd-delivery.md:62`; `6bcd-cost.md:28-33` | Faithful |
| Memo 7 part 1 C at three activities, with the hold-harmless (`-02`) | HLT-9.01, 9.02; `6bcd-cost.md:30` | Faithful. The hold-harmless covers users on December 31, 2034, re-assessed only on change |
| Memo 7 part 2 B: tier budgets, top tier at nursing-home level (`-02`) | HLT-9.03 | Faithful |
| Memo 8 C: the plan pays the care part; residents pay room and board from income above a protected allowance (`-02`) | HLT-9.08, HLT-4.04, 4.08 | **Not faithful on one point.** The memo gives room-and-board help "with no asset test beyond income" (`memos/8-institutional-care.md:39`); section 4 applies HLT-4.04's limits (B-1) |
| Memo 9 E: state options kept, respite and training, evaluate, then decide (`-02`) | HLT-4.06, HLT-9.05 | Faithful |
| Points 1-10 for part B (`-02`) | HLT-4.01-4.07, HLT-9.04, 9.06, 9.10 | Faithful |
| Memos 10 B, 11 A, 12 A, 13 A; points 1-10 for part C; the pre-K seam (`-03`) | FAM-2.01-2.11; `4bcd-specification.md:85` | Faithful, but the guarantee's netting of all of CCDF ends school-age subsidies (M-2), and the territories are unplaced (M-1) |
| Memo 14 B at $20; memo 15 B; memo 16 C; points 1-9 for part D (`-04`) | HLT-10.01-10.07, HLT-11.01-11.05, FAM-2G.01-2G.02 | Faithful. The evidence grades for memo 16 C are stated as the decision asked (`4bcd-specification.md:101`) |
| The cost direction: reprice, federal workforce costs only, states' shares (`-05`) | Section 6, parts 1 and 3 | Faithful. Only the federal share of publicly paid care is counted (O-2 notes who bears the rest) |
| The cost options: the state option below the line; the shares; the declining-state obligation; options 2, 4 and 5; parity kept at 2036 (`-06`) | HLT-4.08, HLT-9.03, 9.07, 9.08, 9.09, HLT-10.01, FAM-2.08, FAM-2G.01 | Faithful in substance. The pre-K share's wording differs from its pricing (C-3). The offset instrument carries a consequence the dossier does not show (F-1) |
| `-07`: the settlement is Claude's | `7bcd-validation.md:38` | Faithful |

## 2. Findings

IDs: B blocking design-record conflict, F fiscal, M missing populations, O optimistic assumptions, A cheaper alternatives, W weak evidence, E section 9, C consistency and record. **Blocking** means blocking L3.

### B. Room and board

**B-1. Section 4 puts an asset test on the room-and-board help that memo 8 C decided without one. Blocking.**
- **What the decision says.** Memo 8 C (decided, `DEC-2026-11-11-02`) gives residents who cannot pay room and board help "from Medicaid, with no asset test beyond income" (`memos/8-institutional-care.md:39`). Its own case is "the widow keeps her savings" (`:46`), and its comparison table has a widow with $90,000 who "keeps her savings" (`:72`).
- **What section 4 says.** The higher resource limits ($10,000 and $20,000) "apply until the benefit replaces the asset test in 2035, and afterward to Medicaid's room-and-board help (HLT-4.08)" (`4bcd-specification.md:41`). HLT-4.08 pays room and board "at the regular match, with HLT-4.04's limits" (`:45`). HLT-9.08 sends residents who cannot pay to "Medicaid's help (HLT-4.08)" (`:58`).
- **What sections 7 and 9 promise.**
  - "Savings and the home are never spent down" (`7bcd-validation.md:68`).
  - "No one spends down their savings or loses their home to get long-term care" (`9bcd-public-case.md:18`).
  - "Will my parent lose their home to pay for a nursing home? No." (`:41`). The answer names the $10,000 limit, but only as a 2030 improvement.
  - OUT-02's "the end of the long-term care spend-down" (`7bcd-validation.md:79`).
- **The scenario.** A widow in a nursing home in 2036 has $90,000 in savings and $24,000 a year in Social Security. Room and board is about $34,000-46,000 (`7bcd-validation.md:68`). The plan pays the care part. Her income falls about $10,000-22,000 a year short of room and board. As section 4 is written, she draws down her savings until she reaches $10,000, then gets Medicaid's help. That is the spend-down the memo removed, on a smaller bill. Medicaid is the primary payer for 63% of nursing-facility residents today [EV-CAR-438], mostly because their income cannot cover a stay. So this is the common case for long-stay residents, not an edge case.
- **Why blocking.** It is an inconsistent commitment: a decided protection, the public case's first promise and section 4 disagree. Under `DEC-2026-11-10-07` that is a defect.
- **The fix.**
  - Write HLT-4.04, HLT-4.08 and HLT-9.08 as memo 8 C decided: room-and-board help in Medicaid is income-tested only, with no resource limit, from January 1, 2035. HLT-4.04's limits then apply in 2030-34 and to the state option below the line, not to room and board after 2035.
  - Price it. The cost is Medicaid's room-and-board help for residents whose savings would have carried them for a while. On the reviewer's rough reading (not a model run), that is a few hundred thousand long-stay residents with savings above $10,000 and income below room and board. It comes to on the order of $3-6 billion a year in 2035, at about 60% federal. Put it in section 6, part 2, as a firm item with a range.
  - If the author reads the $10,000 limit as intended, that departs from a decided memo and goes back to Espen as a yes-or-no point. Sections 7 and 9 must then say that room and board above income can draw savings down to $10,000. The reviewer recommends the first route: it is what was decided, and its cost is small.

### F. The fiscal-rule report (`DEC-2026-11-10-05`) and the money

**The report itself follows `DEC-2026-11-10-05`.** Section 6 reports the yearly path on fiscal years ($3,537 billion over FY2030-39). It reports the permanent FY2040 cost ($729 billion, 1.3% of GDP), the net of what is already booked ($2,432 billion and $580 billion) and the plan-wide margin both ways ($4,243 billion or $4,403 billion short in FY2040, from $3,750 billion). It names the fund-solvency effect when part C stays in EDU-9B (about $87 billion a year on the fund's own receipts). It treats the gap as a figure to report, not a defect, and sends no part of it to Espen. Where part C is booked is left to the settlement, as it should be (`6bcd-cost.md:138`, `:173`). The bridge from memo 17's calendar figures to fiscal years is shown line by line. The memo 15 correction (+$0.09 trillion) is reported, not trimmed. The findings below are about inputs, not form.

**F-1. Three state obligations now sit on one untested instrument, and its offset base largely disappears after 2035. Not blocking; it must be in section 6 and section 8 before the booking.**
- **What is decided.** Health's HLT-7.17 is a direct obligation on the Part D clawback model, collected by offset (`4-specification.md:86`). Parts B-D put two more payments on the same instrument, as Espen decided (`DEC-2026-11-11-06`, items 2 and 2a): states' long-term care payment (HLT-9.09, about $115 billion in 2035 and $150 billion in FY2040) and a declining state's child care and pre-K share (FAM-2.08). This review does not argue the choice. Three consequences are not shown.
- **1. The offset base.** The clawback is offset "against federal Medicaid payments otherwise due to the State" [EV-CAR-354]. After January 1, 2035, the plan has taken over Medicaid's acute care (2033-35) and its home and institutional care. What federal Medicaid money a state still receives is room-and-board help, the state option below the line and services the plan does not cover (HLT-4.08), a small fraction of what it owes. So from 2035 the offset must reach federal payments outside Medicaid, as HLT-7.17's words ("federal payments to the state") allow. That departs from the clawback, the precedent the dossier's legal case rests on (`8bcd-change-our-minds.md:29`). An offset against highway or education money to collect a health payment is closer to the leverage *NFIB* barred [EV-CAR-351]. For a state that declined child care, the offset collects for a program it refused, and the offset base for that collection is never named.
- **2. The joint failure.** Section 6 prices each failure alone: long-term care +$0.6 trillion and +$150 billion; child care +$0.1 trillion and +$25 billion (`6bcd-cost.md:153-154`). Health prices its own (about $307 billion in 2032; `8-change-our-minds.md:15`). One ruling against the instrument ends all three. In FY2040 that is roughly $650 billion a year (health's payment of roughly $480 billion on its model's growth, plus $150 billion and $25 billion), against a plan-wide gap of $4,243 billion. The settlement needs that one row, because a correlated legal risk is the largest single swing in the plan's financing after the taxes themselves.
- **3. HLT-7.17's own clause.** Health wrote: "When part B decides long-term care, if it brings new federal money for states' long-term care, the payment moves to become a condition on that new money, which a state may decline, and the offset ends" (`4-specification.md:86`). Section 4 says this is "honored by HLT-9.09 for 2030-34 (the bridge) and does not apply after 2034" (`4bcd-specification.md:63`). Neither half is right as written:
  - The bridge's entry condition is about states' own home care spending (HLT-4.01). Health's payment is not made a condition on the bridge in 2033-34.
  - From 2035, the plan's taking over half of states' long-term care spending is, in substance, new federal money for states' long-term care.
  - Section 4's reason for not conditioning is sound (individuals are entitled, states run nothing, there is no program a state could decline), and so is the reason section 8 gave for health (`8-change-our-minds.md:25`). But the record should then say that HLT-7.17's clause is **superseded** by HLT-9.09, as HLT-9.11 does for HLT-7.07, not that it is honored.
- **The fix.**
  - In HLT-9.09 and FAM-2.08, name the offset base after 2035 (which federal payments) and say plainly that it goes beyond the clawback's Medicaid-only offset.
  - Add a joint-failure row to section 6, part 6, with health's figure. Add one line to section 8's legal events, and say what the hard stop at `8bcd-change-our-minds.md:39` means at that size.
  - Rewrite `4bcd-specification.md:63` to supersede HLT-7.17's clause, with the reason, and cross-refer in `provisions.json`.
  - Investigation: the L4 legal review. It informs bill drafting and the settlement's reserve for the risk. It does not block a decision now.

**F-2. The dependent care credit's and exclusion's fall is not counted. Not blocking; label it.** The 2025 law's dependent care credit (50% top rate) and $7,500 exclusion stay as current law (point 4; `3c-design-child-care.md:25`, `:205`). Families claim them for what they pay. When care becomes free at or below 85% of state median income and is capped at 7% above it, most families' claimable expenses fall, so the federal cost of the credit and the exclusion falls with them. That is a revenue gain against part C's cost: probably several billion dollars a year (reviewer's judgment, not a model run). Section 6, part 2 lists "not counted" items in both directions but not this one. It is also a seam with the secure floor (PR #258), which owns refundability (`4bcd-specification.md:83`): a refundable credit on a base the guarantee is shrinking is worth much less than today's figures suggest. The fix: a part 2 row, "lower net cost, not counted; the secure floor's refundability choice should be priced on the post-guarantee base". Working assumption; no investigation needed now.

**F-3. The booking list (part 5), reviewed for correctness only.** It will be the lead's separate tier-3 PR. Its structure is right:
- it retires HLT-4's $0.319 trillion long-term care component and books the bridge and the bridge-period floor in its place;
- it keeps HLT-4's safety-net component (the residency slots included, so HLT-10.07 is not counted twice);
- it moves part C to one home, the general fund or EDU-9B, the settlement's choice;
- it books states' payments as offsetting receipts.

Points to add to that PR:
1. B-1's room-and-board line and M-1's and M-2's lines, once priced.
2. Label the receipts rows (item 7) with F-1's joint risk, so the settlement sees the receipts as one contingent stream with health's.
3. Incidence (item 8). The decided long-term care benefit reaches higher quintiles than the `medicaid_ltc` key, as section 7 says (`7bcd-validation.md:63`). A new key, not `medicaid_ltc`, is the recommended choice.

### M. Missing populations

**M-1. The territories. Blocking.**
- **The gap.** No file in parts B-D mentions Puerto Rico or the territories. The only hit is Canada's (`2c-what-works-child-care.md:48`). Health placed them in HLT-7.28 (`4-specification.md:51`), so HLT-9.01's entitlement reaches territorial residents from 2035 by reference to HLT-7.01. Everything else is unplaced:
  - **Child care and pre-K.** FAM-2.01, 2.02 and 2.07 run through "each state's child care agency". Whether the guarantee, pre-K, the shares and the declining-state rule (FAM-2.08) apply to the territories is not said. Today CCDF and Head Start both serve the territories.
  - **The bridge and the 2030-34 floor.** Long-term care stays in Medicaid until 2035, under the territories' capped allotments. HLT-7.28 ends the cap only "for the care that moves", and long-term care moves in 2035. So in 2030-34, extra match points (HLT-4.01) add nothing once the cap binds. The $20 floor (HLT-10.01) would then fall entirely on the territories' own budgets. In Puerto Rico, where the minimum wage is far below $20, the floor's lift is much larger than the 8-18% section 6 assumes for the states.
  - **HLT-9.09.** What a territory pays from 2035 is not said.
- **Why blocking.** Eligibility and who pays are L3 elements. It is the same class as health's M-1, which health's review held blocking and health fixed.
- **The fix.**
  - Section 4: a provision or a sentence in each of FAM-2.07 and 2.08, HLT-4.01, HLT-10.01 and HLT-9.09. It says the territories take part on the states' terms, that the 2030-34 bridge points and floor are paid outside the cap (or that the cap is lifted for home care in 2030-34), and that the territories' long-term care payment follows HLT-7.28.
  - Section 6: price it outside the model total, with a range. The territories hold about 3.5 million people [EV-CAR-356] [EV-CAR-357], so the cost is small in plan terms.
  - It follows from point 3 of health ("every resident") and memo 13 A, so it needs no new decision from Espen unless the floor's cost in the territories makes it mainly a money choice.

**M-2. School-age children on today's child care subsidies. Blocking.**
- **The gap.** Part C covers children "from birth until they start kindergarten" and puts "school-age care before and after school" outside its scope (`1c-problem-child-care.md:9`). But its pricing nets "today's CCDF money (about $12 billion, federal)" into the guarantee as "moving in" (`3c-design-child-care.md:76`, `:81`; `care_repricing.py`, `CC_CCDF`). CCDF serves children up to age 13. School-age children are a large share of the children it serves today: roughly a third or more on ACF's administrative counts, a figure not yet in the register. If all of CCDF's money moves into the under-5 guarantee, nothing pays for them. FAM-2.04 keeps "the block grant" with its 2024 protections only "until July 2032" (`4bcd-specification.md:74`).
- **The scenario.** A single parent at 60% of state median income has a seven-year-old in after-school care paid by CCDF in 2031. In the 2032-33 school year the state's block grant money has moved into the under-5 guarantee, and the child's subsidy ends. Nothing in sections 4-9 says what happens to them.
- **Why blocking.** The design ends a current benefit for a group it never weighs. Under `DEC-2026-11-10-07` that is a decision-changing omission, not a bounded uncertainty.
- **The fix.**
  - Section 4: keep CCDF as a block grant for school-age care (children 5 to 12), at least at its FY2029 school-age share, indexed. Only the under-5 share moves into the guarantee. FAM-2.04's "in the meantime" protections then stay for it.
  - Section 6: net only CCDF's under-5 share. Show the school-age share as a firm item (several billion a year).
  - Add the school-age share to the register.
  - This keeps current law for a group outside part C's design, so it is not a new fork. Whether to expand school-age care is a later question, for this dossier or the education flagship. Name it in section 8 as left open.

**M-3. Groups the specification does not place. Not blocking.** Each needs a sentence in section 4 or 5, not a decision:
- **Veterans.** HLT-7.24 keeps the VA alongside the plan. Section 4 should say how HLT-9's benefit coordinates with the VA's home care, its community nursing homes, state veterans homes and the VA caregiver stipend (`2b-what-works-home-care.md:32`): who pays first, and whether the VA stipend and paid family care can both be drawn.
- **Children in foster care and kinship care.** FAM-2.06's "every child resident" covers them. Section 4 should say who counts as the family for the income determination (the child alone, as CCDF allows, is the low-burden choice).
- **Medicare home health and skilled nursing stays.** Short post-hospital stays stay plan medical care (HLT-9.08). Section 4 should say how a home health episode and HLT-9's tier budget sit together, so a user is not reassessed or double-billed.
- **People in prison or jail who need long-term care.** Health's M-2 asked the same for medical care. One sentence aligning HLT-9 with health's answer.

### O. Optimistic assumptions

**O-1. Child care's first year: about nine to twelve months from R2, with no readiness count. Not blocking.**
- **The timeline.** R2 passes "by about October 2029 to January 2030" (`4bcd-specification.md:18`). The free tier for families at or below 85% of state median income starts in the 2030-31 school year (FAM-2.03). In that time, ACF must approve fifty state plans, set a cost-of-care rate model and stand up the fallback. ACF's capacity was cut in 2025-26 (`5bcd-delivery.md:38`).
- **The supply limit.** The free tier comes before supply grows, and FAM-2.03 phases by date, not by slots. In the first year, eligible families will find no slot in many places.
- **The asymmetry.** Section 5 gives long-term care a readiness report 18 months ahead (`5bcd-delivery.md:37`). It gives child care none.
- **Why not blocking.** The dates are decided (memo 12 A), and the "latest date" rule for a late R2 is sound.
- **The fix.** Add a child care readiness count, published by spring 2030 and each spring after: plans approved, the rate model in use, slots and families waiting by state and age. It is a published count, not a gate, on the lens's terms. Section 8's "move the cap to 2033" trigger can then read from it. Study in implementation; no investigation now.

**O-2. The floor in mixed-payer providers, 2030-34. Bounded; label it.**
- **The design.** HLT-10.01 covers care "paid by Medicaid", and private-pay care is outside it (`4bcd-specification.md:93`). Section 6 counts only the federal share of Medicaid's part, as `DEC-2026-11-11-05` directs.
- **What it leaves unstated.** A nursing home or home care agency cannot pay the same aide $20 for Medicaid residents and less for others. In practice the floor lifts the whole payroll, and Medicare and private payers bear the rest through higher prices until 2035. Medicare's skilled nursing rates are not adjusted.
- **The fix.** One sentence in section 6, part 2 ("private-pay and Medicare prices rise with the floor in 2030-34; not a federal cost under `-05`, except Medicare's share, not counted"). Working assumption.

**O-3. The workforce.** About 2.8 million long-term care recruits (range 0.9-8.8 million; `5bcd-delivery.md:40`), on top of child care's and pre-K's 2031-33 hiring peak. The dossier names this as the binding constraint. It sets phasing (HLT-9.07), triggers (`7bcd-validation.md:103`) and a hard stop (`8bcd-change-our-minds.md:38`). A clearly bounded uncertainty, not a defect.

### A. Cheaper alternatives

Memo 17 already weighed a cost-down set under Espen's direction, with each option's burden and saving, and Espen chose among them (`DEC-2026-11-11-06`). The reviewer found no cheaper design reaching the same people that the dossier left unweighed. Two notes, neither blocking:
- **A-1.** B-1's fix is the cheaper of its two readings for families, though slightly dearer federally. Its cost (a few billion a year) belongs in the record either way.
- **A-2.** Pre-K's state share (C-3) charges states that already fund pre-K more for the same program: they pay their current spending plus 25% of the rest. For states like Oklahoma, Georgia or New York, that is a burden in effect penalizing early adopters. The decided share is not argued here. The consequence should be one line in section 3c's or section 6's state-share table.

### W. Weak evidence

**W-1. Registry warnings in the 400-647 block.** Ten analysis entries are uncorroborated: EV-CAR-423, 428, 446, 447, 450, 487, 544, 603, 609 and 612. Eight are contested: 489-491, 543, 544, 557, 559 and 565. Of these, two are load-bearing for a figure in section 6 or 7:
- **EV-CAR-447** is the bridge's only benchmark (Build Back Better's six-point match at about $150 billion, as KFF reports CBO; `7bcd-validation.md:12`). Add CBO's own score of that provision as a corroborating entry.
- **EV-CAR-603** is the second Trump administration's $55.1 billion staffing figure, already shown "as that administration's view" (`7bcd-validation.md:17`). That is the treatment `DEC-2026-10-30-01` asks for.

The contested pre-K entries (557, 559) are presented both ways in section 7, part 6 and section 8. Not blocking.

**W-2. Costs resting on judgment.** Part B's new users and cost per user, the room-and-board share, under-3 take-up and parity's path are working assumptions. Section 6, part 7 labels them so, with ranges, and section 7 says no US experience pins down the take-up figures. Parity has no independent cost model, which section 7 says (`:18`). Bounded; not a defect. Investigation: an outside parity estimate informs the settlement's central figure, not a choice, and blocks nothing now.

### E. Section 9 against sections 1-8

Every number in section 9 traces to sections 1-8 with its evidence ID or as labeled project arithmetic, and "on our estimates" is used where it should be. The cost is stated plainly: $3.5 trillion, $730 billion, 1.3% of GDP, $580 billion beyond what is booked. That is better than health's first draft (health's review, E-1). The "families come out ahead" claim is withheld until the taxes are set, and the state-refusal answer says the rule is untested.

**E-1. The spend-down promise. Blocking, as part of B-1.** `9bcd-public-case.md:18`, `:41` and the can-say rows promise more than section 4 specifies. Fix B-1 first, then make section 9 match whichever reading lands.

**E-2. Smaller points. Not blocking.**
- "States keep paying ... a fifth of child care's cost after three years" (`:16`) leaves out pre-K's quarter, which is the larger state payment at maturity (about $34 billion against $20 billion; `6bcd-cost.md:91-92`).
- The case in one paragraph says "From 2030, child care becomes free" (`:22`). The free tier starts in the 2030-31 school year, which the brief says correctly (`:13`).
- The territories and school-age children need a line once M-1 and M-2 land ("every child under 5, in every state and territory").

### Design lens (`DEC-2026-11-09-13`)

The design is strong on the lens:
- one assessment at home, reassessed only when needs change;
- no asset test for the benefit;
- one income determination a year from tax records or the family's statement, with copays never reclaimed;
- no activity test for child care;
- workforce counts from payroll records already held;
- the 80% check from providers' own payroll;
- published counts with triggers rather than gates.

Section 4's burden table (`4bcd-specification.md:138-148`) does what the template asks. Three gaps:
- **The copay's implicit marginal rate.** The working choice is a straight line in the copay *rate*, from 0% at 85% of state median income to 7% at 150% (FAM-2.01). Because the rate rises as income rises, a family whose care costs more than its cap faces an added charge of about 9 cents on each extra dollar at 85% of median income, rising to about 23 cents at 150%. On top of income tax and the other phase-outs, that is a steep slope for middle-income parents. A straight line in the copay *amount* gives a flat 16 cents. The table should state it, and pass it to the secure floor's shared rule 2 as a figure.
- **Two tests for people at two activities.** People below the line get help only through a state's Medicaid option, with Medicaid's financial rules (HLT-4.08). The table lists the line's burden, not this second test.
- **B-1's asset test, if kept.** It would be the one asset test the decided design brings back, and it would fall on nursing-home residents at the hardest moment, the cliff memo 8 was written to remove (`memos/8-institutional-care.md:13`).

### C. Consistency and record

- **C-1. Memo status lines.** Memos 9, 10, 11, 12 and 13 still read "for Espen, not decided" on line 3, though `DEC-2026-11-11-02` (memo 9 E) and `-03` (memos 10-13) decided them. Memo 17 keeps a "Questions for Espen" heading (`memos/17-cost-options.md:118`) after the questions were answered. Mark each decided, citing its DEC.
- **C-2. `provisions.json` decision arrays.** Five provisions' text relies on `DEC-2026-11-11-06` while their `decisions` arrays omit it: FAM-2.01, FAM-2.02 and FAM-2.08 (list only `-03`), FAM-2G.01 (only `-04`) and HLT-4.08 (only `-02`). Add `-06`. FAM-2.08's status text already cites it.
- **C-3. Pre-K's share: the wording against the pricing.** FAM-2.08 says the federal government pays pre-K "90% for three years, then 75%" and that states keep their current spending "as maintenance of effort (inside their share)" (`4bcd-specification.md:78`). The pricing pays 75% of the cost *above* states' current $14.4 billion (`care_repricing.py`, pre-K lines; `3c-design-child-care.md:83`, `:96`), so states pay about $34 billion of $91 billion and the federal share is about 63%. That is what Espen saw ("their $14.4 billion included"), so the pricing is the decision. The wording should say "75% of the cost above states' current spending, which they keep", in FAM-2.08 and `5bcd-delivery.md:85`.
- **C-4. "$4,243 billion" used for two things.** Health's own FY2040 net cost as booked is $4,243.0 billion (`6-cost.md:161`). The plan-wide gap with parts B-D and part C in EDU-9B is $4,242.7 billion (`6bcd-cost.md:126`). That is a coincidence, and both are right. But `6bcd-cost.md:129` ("about 12-15% of the plan-wide gap, after health's $4,243 billion") and `7bcd-validation.md:37-38` put them a line apart, and a reader will take them for the same number. Name each in full where they meet.
- **C-5. Calendar figures labeled as fiscal years.** Memo 17's $3.80 trillion and $736 billion are on calendar and school years (`6bcd-cost.md:49`, `:53`; `4bcd-specification.md:170`). `README.md:3` and `memos/17-cost-options.md:19`, `:23`, `:116` label them "FY2030-39". So does the board (`charter/PROGRESS.md:33`, `:130`, `:217`; the board is the lead's).
- **C-6. A third of states declining, on two bases.** `6bcd-cost.md:154` and `3c-design-child-care.md:92` compare $87 billion (gross, before today's CCDF money is netted) with $74 billion (net, with administration). On one basis the gap is about $7 billion smaller. The row's +$25 billion in FY2040 should be re-derived on one basis.
- **C-7. The README's agenda list.** `README.md:11` lists "HLT-1 to HLT-8, ... FAM-2 and FAM-2A to 2D". It omits HLT-9, HLT-10, HLT-11 and FAM-2E to 2G, which `agenda/agenda.csv` homes in care.
- **C-8. HLT-7.17's clause** (F-1, item 3). `4bcd-specification.md:63` should say "superseded", not "honored".

### Seams with other dossiers

- **The secure floor (PR #258, another session's).** Four seams. None blocks this dossier; each needs one line on each side:
  - The dependent care credit's refundability is the floor's (`4bcd-specification.md:83`), and the guarantee shrinks its base (F-2).
  - The child care copay is a phase-out to stack (shared rule 2), with an implicit rate of 9-23% (design lens).
  - A Social Security caregiver credit is the floor's (`7bcd-validation.md:40`). Relatives paid at the floor through public fiscal agents already earn Social Security credit on that pay (HLT-9.05, HLT-10.03), so the floor's credit matters for unpaid caregivers, and the two should not count the same hours.
  - SSI's own asset limit is the floor's (HLT-4.04), and HLT-4.04's $10,000 Medicaid limit should not be read back into SSI.
- **Health.** F-1, the shared offset instrument, is the main seam. HLT-9.11's amendment of HLT-7.07 is the right pattern, and C-8 asks for the same for HLT-7.17. Health's ownership guardrails reaching home care and nursing homes are noted in section 8 (`8bcd-change-our-minds.md:54`).
- **Education.** The pre-K seam is as decided. M-2's school-age care is a place where education may later want a say.

## For Espen

Nothing new, unless B-1's author reads the $10,000 limit on room and board as intended. In that case it is a yes-or-no point: "Should residents who cannot pay room and board from income keep their savings, as memo 8 C said (about $3-6 billion a year), or draw savings down to $10,000 first?" The reviewer recommends keeping memo 8 C as decided. Every other finding is a correction or a placement that follows from a decision already made:
- M-1 follows from "every resident" and memo 13 A;
- M-2 keeps current law for a group part C does not cover;
- F-1 is a record and reporting fix on an instrument Espen chose with its risk stated.

If covering the territories or keeping school-age care costs materially more than the few billion expected, that is a money question for the financing settlement under `DEC-2026-11-10-05`, now Claude's under `-07`. It would reach Espen only as such.

## What the next steps should do

For D-9's author, `session_01UQzgBw9VK9o3iPPDppbRg7`, unless marked for the lead. In order: steps 1 and 2 clear the blockers, and step 6 follows them.

1. **Room and board** (B-1, E-1; design lens).
   - Write HLT-4.04, HLT-4.08 and HLT-9.08 as memo 8 C decided: room-and-board help from 2035 is income-tested only. HLT-4.04's limits apply in 2030-34 and to the state option below the line.
   - Price it in section 6, part 2 as a firm item with a range.
   - Align `7bcd-validation.md:68`, `:79` and section 9 (`:18`, `:41`, the can-say rows) with it.
   - If you read the limit as intended instead, stop and put the yes-or-no point above to the lead for Espen; do not write it either way until answered.
   - **Who:** the author. Tier: Most capable. Routine PR.
2. **The territories and school-age children** (M-1, M-2, M-3).
   - Section 4:
     - the territories in FAM-2.07 and 2.08, HLT-4.01, HLT-10.01 and HLT-9.09, with the 2030-34 bridge points and floor paid outside the capped allotment;
     - CCDF kept as a school-age block grant, with only its under-5 share netted;
     - a sentence each for veterans, foster and kinship care, Medicare home health beside the tier budget, and people in custody.
   - Section 6: both priced outside the decided total, with ranges. Re-run `care_repricing.py` and `care_bcd_path.py` with CCDF's school-age share split out (a parameter, not a hand edit).
   - Register entries for CCDF's school-age share and the territories' child population.
   - **Who:** the author, with a Standard subagent for the entries. It can share a PR with step 1.
3. **The offset instrument** (F-1, C-8).
   - In HLT-9.09 and FAM-2.08, name the offset base after 2035 and say it goes beyond the clawback's Medicaid-only offset.
   - Add a joint-failure row to section 6, part 6 (health's payment, part B's and child care's, about $650 billion in FY2040), and one line in section 8's legal events and hard stops.
   - Rewrite `4bcd-specification.md:63` as superseding HLT-7.17's "when part B decides" clause, with its reason, and cross-refer in `provisions.json`.
   - **Who:** the author. Tier: Most capable (legal drafting). It can share a PR with steps 1 and 2.
4. **Section 6's smaller items** (F-2, O-2, C-3, C-4, C-6, A-2).
   - Part 2 rows for the dependent care credit's fall and the floor's private-pay incidence.
   - Pre-K's share worded as priced (FAM-2.08, `5bcd-delivery.md:85`).
   - The two $4,243 billion figures named apart.
   - The declining-states row re-derived on one basis.
   - The pre-K early-adopter line.
   - **Who:** the author, with a Standard subagent for the arithmetic. It can share a PR with step 3.
5. **Delivery, lens and evidence** (O-1, design lens, W-1).
   - A child care readiness count from spring 2030, with section 8's cap trigger reading from it.
   - Add to the burden table: the copay's implicit marginal rate (and the flat-amount alternative), and the second test for people at two activities.
   - A CBO entry corroborating EV-CAR-447.
   - **Who:** the author. Tier: Standard, with Most capable for the lens rows.
6. **Section 9** (E-1, E-2), after steps 1 and 2.
   - The spend-down promise to match B-1.
   - Pre-K's quarter beside child care's fifth.
   - "From the 2030-31 school year" in the paragraph.
   - "In every state and territory".
   - **Who:** the author. Tier: Most capable.
7. **Record fixes** (C-1, C-2, C-5, C-7).
   - Memos 9-13 marked decided; memo 17's question heading.
   - `provisions.json` arrays with `-06`.
   - README line 3's calendar label and line 11's agenda list; memo 17's calendar labels.
   - **Who:** the author, by a Light or Standard subagent. It can share a PR with step 5. The board's labels (`charter/PROGRESS.md:33`, `:130`, `:217`) are the lead's.
8. **The booking** (F-3; `6bcd-cost.md`, part 5).
   - The tier-3 PR, after steps 1-4, on the re-run path.
   - Retire HLT-4's long-term care component, and add the bridge, HLT-9, HLT-10 and HLT-11.
   - Book part C in one place, the settlement's choice.
   - Book states' payments as offsetting receipts, labeled with F-1's joint risk.
   - A new incidence key for HLT-9.
   - **Who:** the lead's booking (`DEC-2026-11-11-07`: the settlement is Claude's). Espen's label.
9. **A short L3 re-check** by a reviewer, limited to B-1, M-1, M-2 and the re-run. Then the lead moves HLT-4, HLT-9, HLT-10, HLT-11, FAM-2 and FAM-2G to L3 in `agenda/agenda.csv` and the README.
