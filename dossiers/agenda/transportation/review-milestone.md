# Moving America: L2/L3 milestone review

Role: the independent milestone review of the transportation dossier (`charter/PLAN.md` 3.2 and 5, "Review"; `charter/STANDARDS.md`, "Milestone review"), board row 7r. The reviewer wrote none of the dossier. It tries to break the work on four fronts (weak evidence, missing populations, optimistic assumptions, cheaper alternatives), applies the design lens (`DEC-2026-11-09-13`), checks the fiscal-rule report against `DEC-2026-11-10-05`, and checks internal consistency, including section 9 against sections 1-8. Status: current, as of main at commit `4d49daa` (November 10, 2026, after #203 and #206). Reviewer: Claude Code, `session_01UQzgBv9R4sR9sZVApMhR1T`. It changes nothing in the dossier: every fix below is a later step, which the lead assigns.

Espen's six memo decisions and eight points (`DEC-2026-11-10-08`) are settled. Where a decided choice has a consequence the dossier does not show, this review says so; it does not argue the choice. Under `DEC-2026-11-10-07`, a clearly bounded uncertainty is not a defect, and every investigation asked for below names the decision it informs and whether it blocks that decision now.

## Verdicts

| Level | What it needs (`charter/PLAN.md` 3.2) | Verdict |
| --- | --- | --- |
| **L2, design** | Key parameters chosen (who, what, how much, who administers), with the main alternatives weighed | **Pass** (record fixes only, none blocking) |
| **L3, specified** | Provisions section by section (eligibility, benefit, administration, phase-in, remedies); evidence for each load-bearing claim; a cost range validated by models with stated limits; a delivery plan | **Not yet: close.** Two blockers |

**Why L2 passes.** Every fork has two to four options weighed on evidence, "keep the legacy design" is an explicit option where `DEC-2026-10-30-02` asks for it, and all six memos and eight points are decided and recorded (`DEC-2026-11-10-08`; each memo's status line; `3-design.md:3`, `:213`; agenda rows 500-509 at L2, `decided`). The memos are honest about what rests on judgment. The record fixes (C-1 to C-4) are small.

**Why L3 is not yet.** Three of the four L3 parts are in place. Section 4 specifies 82 provisions with parameters, vehicle, agency, current-law change and evidence; section 5 is a real delivery plan with a timeline, capacity, remedies and a reluctant-agency section; the evidence register is complete (every EV-MOV ID cited, every source catalogued). The blockers:
1. **The 25% income and payroll tax offset is not booked anywhere in the plan-wide totals, although section 6 says it is** (F-1). That is about $29 billion in FY2040 and about $128 billion over the acts' windows. The FY2040 figure the dossier reports to the settlement is spending only, and the "share of the plan-wide margin" row says transportation is "already inside" totals that leave the offset out. This is an unsupported claim stated as settled, not a test-year gap, so it is a defect under `DEC-2026-11-10-07`.
2. **Section 9 runs ahead of sections 1-8 in three places** (E-1 to E-3): it states the general-fund draw without the offset, stops the household cost at 2036 although the decided fossil premium and indexing nearly double it again by the mid-2040s, and says "most of the money goes to roads" when the highway division is 49% of the bill and transit gets half of new receipts through FY2036.

**What can reach L3 once those land.** Every provision can. None is held back by an unspecified parameter: the items still open (the 2028 transfer's size, review-trigger thresholds set by rule, the Buy America standard for joint fleets) are bounded working choices or drafting details (O-4, C-3).

## How this review was done

- Read the charter (standards, the board's rows 7 and 7r, plan section 3.2's levels, `DEC-2026-11-10-08`), the template, housing's review (#182) as the model, sections 1 and 3 in full, sections 4 to 9 and the memos selectively for load-bearing claims, and the parts of `moving_america.py`, `ledger-build.py`, `fiscal-model.py` and `models/data/budget/provisions.csv` that book transportation.
- A Sonnet subagent ran the mechanical checks; the reviewer checked what it reported before using it:
  - **IDs.** All 82 EV-MOV IDs cited exist and all are cited; all 82 sources are in `library/catalog.csv`; all 82 provisions are in `4-specification.md`. MOV-31.39, .59 and .79 appear only as range ends (`4-specification.md:86`, `:107`, `:125`), which is harmless.
  - **Statuses.** Agenda rows MOV-28 to MOV-31 and MR1 to MR6 are L2, `decided`. In `provisions.json`, 47 provisions are decided, 34 chosen (drafting detail) and 1 decided by reference (MOV-31.91). Nothing decided is still "proposed".
  - **Sums.** Section 4's consistency table re-adds, and so do section 6's tables.
  - **Models.** `test_moving_america.py` passes; `report.py` reproduces `golden/report.txt`; `Model().allocate(t)` gives FY2040 $28.99 billion; the budget model books MOV-29 to MOV-31 at $0.257, $0.091 and $0.125 trillion (FY2030-39, $473.0 billion) and $22.08 billion in FY2040.
  - **Restatement.** The restatement check passes. Draft 2 is restated in full, and each of the ten `by_reference` reasons is file-specific.
- The reviewer re-ran `Model().cbo_basis(t)` against `allocate(t)` to size the offset by year (F-1), and `Revenue.gr(t)` for the household fuel-tax cost after 2036 (E-2).
- `bash .github/scripts/run-checks.sh` passes on this branch.

## Fixes from #203 verified

The fixes from #203's three review rounds were checked against the files and hold. They are not re-raised here.
- **FY2040 basis.** Both columns count spending only, and the booked and model-path figures sit side by side with three reasons for the gap (`6-cost.md:70-95`). F-1 is a different point: whether MR6, the line those columns point to, is booked at all.
- **Restatement reasons.** Each `by_reference` reason is file-specific.
- **Price-pause backstop gap.** The $25 billion cap against $53.3 billion delayed, with the roughly $28 billion remainder falling on expansion first (`6-cost.md:118`; `8-change-our-minds.md:12`; `7-validation.md:69`).
- **Privacy timing.** The location bar and three-year deletion run from October 1, 2031, and this is disclosed in sections 5, 7 and 9.
- **Grants and reserve.** Sec. 1112's $17.24 billion and the reserve's $0 to $25 billion are disclosed beside the draw, not booked (`6-cost.md:55-64`).

## Findings

Each finding has an ID, where it is, what goes wrong, and a severity. **Blocking** means blocking for L3; **not blocking** means fix when convenient. Line numbers are at `4d49daa`.

### 1. The fiscal-rule report (`DEC-2026-11-10-05`)

**What it gets right.** Section 6 reports instead of gating:
- It states yearly cost on the model path, the FY2030-39 total and FY2040 permanent cost, booked and model-path.
- It does not treat the FY2040 gap as a defect or put it to Espen ("None for Espen", `6-cost.md:126`).
- It sends the booking question to the budget model's owner as a tier-3 inputs change (`6-cost.md:101`, `:128`).

That is the rule followed.

**F-1. The 25% offset (MR6) is not in the plan-wide totals, but section 6 says it is.** Blocking.
- **What section 6 says.** "The 25% income and payroll tax offset on the new excises is a revenue effect, booked separately in the ledger as MR6 ... Adding it to these figures would count it twice" (`6-cost.md:77`). The share-of-margin row says the FY2040 cost is "already inside the plan-wide totals the housing close-out reported" (`6-cost.md:75`). The template repeats it as a rule (`dossiers/TEMPLATE.md`, "One basis for each fiscal figure").
- **What the code does.**
  - MR6's channel is the surface transportation trust fund, not the general fund (`models/data/inputs/ledger-revenue.csv:59`).
  - The fiscal model books only general-fund revenue lines that are in the base (`models/tools/fiscal-model.py:160`). MR1 to MR6 are not in the base.
  - The ledger's channel table nets the trust fund's receipts after the offset against equal outlays ("Receipts net of the 25% offset; spent within receipts", `models/tools/ledger-build.py:129`).
  - The budget model lists MR6 as "Not in the model: on the revenue menu, not in the base" (`models/data/budget/provisions.csv:163`).
  - So the offset reduces neither reading.
- **Why it is a general-fund cost.** The offset is lower income and payroll tax receipts, which go to the general fund (and Social Security), not to the trust fund. The transportation model credits the trust fund with gross receipts and spends them: `cbo_basis` adds the offset back on top of the draw (`moving_america.py:394-396`). Either the trust fund spends gross receipts and the general fund loses the offset, or the trust fund spends net receipts and the program is short by the same amount. In both cases the general fund bears it, and no line books it.
- **The carbon fee is booked the other way.** Its identical 25% offset, CX, is booked on the general fund at -$0.54 trillion (`ledger-revenue.csv:19`, "Scoring convention, as MR6 for Moving America").
- **How much.**
  - On the model path the offset is $2.2 billion in FY2030, rising to $18.0 billion in FY2036 and $29.0 billion in FY2040 (`cbo_basis(t)` less `allocate(t)`). That is $141.8 billion over FY2030-39.
  - The ledger's own MR6 is -$128.3 billion over each act's window (`ledger_rows()["score_offset"]`).
  - FY2040's general-fund effect is therefore about $51 to $58 billion, not $22.1 to $29.0 billion: the spending range plus $29.0 billion. It is about 0.10% of GDP, the figure section 6 already prints as the CBO-net basis (`6-cost.md:85`).
  - Against housing's FY2040 plan-wide shortfall of $50.8 billion (`dossiers/home/6-cost.md:382`), it is a large share.
- **Why it is a defect, not a gap.** A gap in a test year is not a defect (`DEC-2026-11-10-05`). This is different: a claim stated as settled that the code contradicts. It means the plan-wide total the settlement balances is low by the offset.
- **Fix.**
  1. *Section 6, now:* report the FY2040 figure with the offset on its own line ($22.1-29.0 billion spending plus $29.0 billion offset, not yet booked). Restate the share-of-margin row. Correct `6-cost.md:75-79` and `:128` and the template rule.
  2. *Budget model:* book MR6 as a general-fund revenue loss in the base, as CX is. This is an adopted-inputs change, tier 3, so Espen applies the label as for every tier-3 PR. It is a correction, not a fork. It belongs with B6 item 4, already named in `6-cost.md:95`.
- **Investigation it needs.** None; the figures are above.

**F-2. The share of the plan-wide margin is not stated as a share.** Not blocking; fold into F-1's fix.
- `DEC-2026-11-10-05` asks for "its share of the plan-wide margin". `6-cost.md:75` gives a location ("already inside") and a difference ("about $7 billion more"), not a share.
- Once F-1 is fixed, state transportation's FY2040 figure beside the plan-wide FY2040 balance the budget model reports, and give the share. Section 6 also shows the model's yearly draw for eight selected years; the booked path by year (`fiscal-profiles.csv` rows 58-60) should sit beside it so the timing reason (`6-cost.md:91`) can be seen.

### 2. Weak evidence

**W-1. Section 7's transit check compares the tier with the fare loss only.** Not blocking.
- `7-validation.md:15` marks transit operations "Holds" because the $6.0 billion first-year tier exceeds the $4.1 billion nominal fare loss from 2019 to 2025.
- The same figures [EV-MOV-100] show operating expenses up $19.4 billion. Net operating cost (expenses less fares) is therefore up about $23.5 billion nominal.
- The federal share of operating cost rose from 8% to 17% with relief [EV-MOV-103]. On about $70 billion of expenses, the nine points that are ending are roughly $6 billion a year.
- So the tier about replaces the expiring relief. It covers about a quarter of the growth in net operating cost.
- Fix: "Partly", with both comparisons. This informs no open decision; memo 4's size is decided.

**W-2. "Hasn't gone up since 1993" is tagged to entries that do not state it.**
- `9-public-case.md:9` and `:74` cite EV-MOV-016 and EV-MOV-202. One gives the current rate and the 2028 fall; the other gives the 1993 rate in 2029 dollars. Neither says the rate was last raised in 1993.
- Not blocking: add the passage to EV-MOV-016's entry, or add an entry (the Omnibus Budget Reconciliation Act of 1993).

**W-3. The operating tier's apportionment rests on Draft 2's own NTD figures.** These are 11.9% of net cost, New York at 27.7%, and the ceiling binding in 69 areas ("the NTD is not in its source list", MOV-31.40). `models/tools/transportation/ntd_uza_2024.py` holds 2024 NTD data.
- Not blocking: tag the figures to the NTD through an evidence entry when section 4 is next touched. They inform no open decision.

**W-4. Handled well.**
- Executive-branch analysis is labeled with its administration: BTS's 32% loss of buying power [EV-MOV-008], with an independent cost index beside it.
- One analyst's delay count is labeled as such (`1-problem.md:67`).
- "Who it hurts" lines say "judgment" where they are.
- Section 1's evidence-still-needed list is limited to what would change a choice.

### 3. Missing populations

**M-1. Riders who depend on paratransit.** Not blocking.
- Section 7's "Reach" (`7-validation.md:41-46`) and memo 4 name riders without a car, but not disabled riders using ADA complementary paratransit. That is the fastest-growing and costliest service per trip for many agencies.
- The operating tier apportions on revenue hours and trips, and the service floor is in vehicle revenue hours (MOV-31.40). An agency can meet the floor by cutting fixed-route coverage, which shrinks the paratransit service area tied to it.
- Fix: one sentence in section 7, and a line in FTA's published report (MOV-31.40) on paratransit service area and trips. No new condition is needed under the design lens.
- Investigation: none now. Paratransit's share of operating cost is something to study in implementation from the NTD.

**M-2. Tribal nations are provided for in section 4 but absent from the reach section.** Not blocking. Provisions carry a 3% tribal bridge set-aside, tribal transit under 5311 and the federal lands and tribal program (MOV-31.20, MOV-31.21, MOV-31.46), and exempt tribal governments from the clean-vehicle charge (MOV-29.03). Section 7 never says so, and section 1 has no tribal road or safety figure. Fix: one line in section 7. Section 1's gap goes on its "Evidence still needed" list only if a choice turns on it; none does now.

**M-3. Intrastate heavy trucks have no "records already filed".** Not blocking; a delivery gap.
- The design lens rests the weight-distance charge on "the mileage records carriers already file each quarter" (`4-specification.md:206`; `3-design.md:59`, `:101`). Those are IFTA returns, and IFTA covers vehicles that cross state lines.
- A truck over 26,000 lb that runs inside one state files no IFTA return. Under MOV-30.01 it would report odometer miles "on quarterly returns under State IFTA agreements", which is a new filing for those carriers.
- Fix: section 5 should say how intrastate carriers file (for example annually, with the registration that already records declared weight), and section 4's lens note should state the burden honestly.
- This blocks nothing now; it informs the 2030 act's drafting.

**M-4. Already bounded, and correctly left open:**
- the count of households without a car (`1-problem.md:105`);
- fuel-tax burden by income, for the settlement's household model (`7-validation.md:38`);
- rural and income incidence of the per-mile charges, reported yearly under MOV-31.82.

None changes a choice now, and each names its source.

### 4. Optimistic assumptions

**O-1. Demand response and the fossil premium.** Bounded, and labeled correctly. Receipts are an upper bound with no demand response [EV-MOV-206], said in sections 3, 6, 7, 8 and 9, with an EV-share trigger for the premium (`8-change-our-minds.md:13`). Not a defect.

**O-2. Section 9's "fairness test is run across the whole plan" is stated as done.** The household model does not yet carry fuel taxes (`7-validation.md:38`). Not blocking for the design; fix with E-1 to E-3: "will be run", not "is run" (`9-public-case.md:58`).

**O-3. The weight-distance and clean-vehicle charges' collection cost.** The 10% ceiling against Oregon's 11% and Utah's 14.2% is disclosed as something to study in implementation, with GAO's review (`5-delivery.md:41`). Bounded; see A-1 for the fallback.

**O-4. The 2028 transfer is "not yet sized" with no range.**
- `6-cost.md:21`, `:34`, `:127`. A working assumption needs a basis and a range (`DEC-2026-11-10-07`). One is to hand: CBO's cumulative shortfalls through FY2031 of $86.0 billion (highway) and $45.2 billion (transit) [EV-MOV-002], about $131 billion, as the upper bound under case 1.
- State also how it scores. Under CBO's convention the baseline already assumes trust-fund outlays continue, so a general-fund transfer to the fund adds little or nothing to the measured deficit. Say so, so the settlement does not count it as new cost.
- Not blocking. It informs the 2028 extension's drafting (a 2027-28 exception) and does not block that decision now.

**O-5. Program levels are nominal.** A-5 keeps them unindexed, and construction costs are flagged with a trigger (`7-validation.md:26`; `8-change-our-minds.md:16`). Bounded, and decided as a working choice. Not a defect.

### 5. Cheaper alternatives

**A-1. A flat annual fee as the clean-vehicle charge's fallback.** Not blocking; for section 8.
- If collection runs above the 10% ceiling, the dossier's only fallback is "more state agreements" (`8-change-our-minds.md:14`).
- A flat annual federal fee by vehicle class, collected at registration, costs far less to collect. Oregon's 2025 law offers one (`2-what-works.md:16`). At 10% of the charge's $14.5 billion over FY2032-36 (MOV-29.03), collection could cost up to $1.45 billion.
- This keeps memo 1's decision; it adds a cheaper fallback the successor bill can use.

**A-2. Already the cheaper path, and kept.** These are memo 4 option D and memo 5 option B as decided. They are the lighter, cheaper versions; the review found nothing cheaper that reaches the same people:
- the published reports in place of two accounting tests;
- the preservation shift and lifecycle gate turned into published reports;
- the odometer-only base;
- the set-asides inside existing formula money (point 5).

### 6. Design lens (`DEC-2026-11-09-13`)

Section 4's lens note (`4-specification.md:199-217`) does what the lens asks. It states what each kept burden costs and what it buys, and turns two up-front gates into published counts with review triggers. Two corrections:
- **L-1.** The weight-distance charge's "no new filing" holds only for interstate carriers (M-3).
- **L-2.** Housing's zoning condition on new transportation money (MOV-31.91) is a condition the lens would ordinarily question. It is housing's decision (`DEC-2026-11-09-04`), and section 4 rightly confines it to new money. Nothing to fix here.

### 7. Internal consistency

**C-1. README's status line contradicts itself.** Not blocking. `README.md:3` says the items are "at L2 (decided)" and then "every item is at L1 in `agenda/agenda.csv`". The second sentence is stale: the agenda has them at L2. Also note, not fixed here: `README.md:27` gives care's source range as SRC-3000 to 3299; it is 3000 to 3399 (`dossiers/care/README.md:39`, the one home for care's range; board row D2 agrees). The board's handoff notes say 3499 (`charter/PROGRESS.md:47`); that line should follow care's README too.

**C-2. Section 3 still reads as a batch to send.** Not blocking. These lines are in the future tense of the memo round: "The six are sent together as one batch" (`3-design.md:13`), "None is adopted by silence" (`:14`, `:142`), and "Recommendation" in each fork. The status line and the closing "None open" record the decision. One "Decided: `DEC-2026-11-10-08`" line under each fork and point, as housing's C-1 asked, would make the record read right.

**C-3. A stale cross-reference in section 4's choices list.** `4-specification.md:268` cites `3-design.md` as saying "FY2029-31 or FY2030-34" for the contingency's years. `3-design.md:144` now says "for the years to FY2031", which agrees with the brief. Not blocking: drop the item.

**C-4. Memo 4's "peak year of 0.223%" is the all-in peak** (`memos/4-transit-operating-help.md:45`). The model's peak-year draw for that case is 0.215%; 0.223% includes sec. 1112's grants [EV-MOV-210]. The memo compares it with the 0.200% base peak, which excludes them. Not blocking: say "all-in" and give 0.208% as the base all-in peak, or use 0.215%.

**C-5. A standalone privacy bill with no provision.** Not blocking.
- Sections 5 and 9 and MOV-29.03's parameters say a standalone privacy bill before October 1, 2030 would close the one-year gap, and that "the plan would rather" pass one (`5-delivery.md:80`; `9-public-case.md:59`).
- No provision, vehicle or agenda row carries it. The timing disclosure from #203 stands.
- Fix, either:
  - add it as a small provision (a 2029-30 regular-order bill), or
  - say in section 9 that it is Draft 2's suggestion, not a plan commitment.

### 8. Section 9 against sections 1-8

Most of section 9 traces: each figure appears in the section its source table names, with its evidence ID, and project estimates are labeled "the plan's model". Three blocking, three not.

**E-1. The general-fund draw is stated without the offset.** Blocking (F-1).
- `9-public-case.md:31`, `:91`: "The general fund pays about 0.18% of GDP a year in 2032-36, falling to about 0.03% by the mid-2040s."
- That is the spending-only draw. With the offset, which falls on the general fund (F-1), section 6 prints 0.220% in FY2032-36 and 0.081% in FY2044 (`6-cost.md:83-88`).
- Fix: state the CBO-net figures, or say "before the income-tax offset, about 0.04 points more".

**E-2. The household cost stops at 2036.** Blocking.
- `9-public-case.md:32`, `:49`, `:58` give "$88 a year today to $225 in 2036", and the messages table makes it the line not to cross ("Say how much").
- The decided fossil premium (FY2040-44) and continued indexing take the same car's federal fuel tax to about $317 in FY2040, $406 in FY2044 and $427 in FY2046 nominal. In 2029 dollars that is about $280 from FY2044 (`Revenue.gr(t)`; FY2046's $427 is in MOV-29.03).
- This is the consequence of a decided choice that section 9 hides. Fix: add the long-run figure, nominal and in 2029 dollars, to section 3 or 7 with its evidence tag, then to section 9.
- Also `9-public-case.md:32`: "about 37 cents a day by 2036" follows "$225", but 37 cents is the increase ($137 ÷ 365 = 37.5 cents, which rounds to 38). $225 is about 62 cents a day. Say "about 38 cents a day more".

**E-3. "Most of the money goes to roads."** Blocking.
- `9-public-case.md:60` answers "Why should my taxes pay for city transit?" this way. Division B (highways) is $461.12 billion of $936.57 billion, 49% (`4-specification.md:234`). New receipts are shared 35% highways and 50% transit through FY2036 (MOV-29.05).
- So the answer is wrong on the total, and it hides a decided choice's consequence: half of the new fuel-tax money goes to transit for the first seven years.
- Fix: "About half goes to highways, about a quarter to transit and a quarter to rail; for the first years, half of the new revenue goes to transit, which reaches self-sufficiency first (memo 3)", with tags.

**E-4.** "The plan's fairness test is run across the whole plan" (O-2). Not blocking.

**E-5.** The source table lists figures the brief does not use (4.3 cents). It omits some the brief does use: the $1.1 trillion backlog (Messages), deaths "fell 6.7%" (can-say) and the three-year deletion. Not blocking: complete the table.

**E-6.** "Hasn't gone up since 1993" (W-2). Not blocking.

## For Espen

Nothing. No finding is a real fork. F-1's budget-model fix changes adopted inputs, so it needs Espen's tier-3 approval label like any such PR, but it corrects a booking to match the convention already used for the carbon fee's identical offset. It is not a choice between options. When the corrected figure reaches the settlement, transportation's FY2040 effect will be about $51 to $58 billion rather than $22 to $29 billion. Any money choice that follows is the settlement's, under `DEC-2026-11-10-05`.

## What the next steps should do (for the lead)

In order; each is small.

1. **Section 6 and the template: the offset** (F-1, F-2).
   - Report FY2040 as spending plus the unbooked offset, and correct the share-of-margin row, `6-cost.md:75-79` and `:128`.
   - Give the share and the booked yearly path.
   - In the template's "One basis for each fiscal figure" rule, correct only the claim that MR6 is booked. Its point that a figure including the offset is labeled so and never added to a spending line stays true.
   - Tier: Most capable. One routine PR. It unblocks step 3.
2. **Budget model: book MR6 on the general fund in the base, as CX is** (F-1).
   - Run the plan-wide total and report the new FY2040 balance to the lead.
   - Tier: Most capable. A tier-3 adopted-inputs PR (Espen's label), with Codex's review requested by comment as for budget-model integration. It can run in parallel with step 1. Fold it into B6 item 4 if that is open.
3. **Section 9 and its sources** (E-1 to E-6, W-2, O-2).
   - Draw figures with the offset.
   - Give the long-run household cost; put the post-2036 figures into section 3 or 7 first, with a D-grade evidence entry from the model.
   - Correct the roads-and-transit answer and the "cents a day".
   - Make the fairness test "will be run".
   - Complete the source table and tag the 1993 claim.
   - Tier: Most capable. After step 1.
4. **Sections 5, 7 and 8: delivery and reach** (M-1 to M-3, W-1, O-4, A-1, C-5).
   - Section 5: how intrastate heavy trucks file.
   - Section 7: paratransit riders and tribal provisions in "Reach", and transit "Partly".
   - Section 6: the 2028 transfer's working range and how it scores.
   - Section 8: a flat-fee fallback for the clean-vehicle charge.
   - The standalone privacy bill: a provision, or labeled as Draft 2's suggestion.
   - Tier: Standard. It can share a PR with step 5.
5. **Record fixes** (C-1 to C-4, W-3).
   - The README status line and care's source range.
   - "Decided" lines in section 3.
   - Drop the stale item at `4-specification.md:268`.
   - Memo 4's all-in label.
   - Tag the operating-tier NTD figures.
   - Tier: Standard (or Light for the README and memo lines).
6. **A short L3 re-check** by a reviewer, limited to F-1 and E-1 to E-3. Then the lead moves MOV-28 to MOV-31 and MR1 to MR6 to L3 in `agenda/agenda.csv` and the README.
