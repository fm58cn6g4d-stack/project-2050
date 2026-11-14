# Clean, affordable power and a prepared country: L2/L3 milestone review

Role: the independent milestone review of the clean power dossier (flagship 4, stage E; `charter/PLAN.md` 3.2 and 5, "Review"; `charter/STANDARDS.md`, "Milestone review"). The reviewer wrote none of the dossier. It tries to break the work on four fronts: weak evidence, missing populations, optimistic assumptions and cheaper alternatives. It also applies the design lens (`DEC-2026-11-09-13`) and the rule to use existing machinery first (`DEC-2026-11-13-08`). It checks the fiscal-rule report against `DEC-2026-11-10-05`, every decided item against `DEC-2026-11-13-06` and `-07`, and section 9 against sections 1-8. It also lays out the one open choice Espen has not yet made: who the builder of last resort is (part 3). Status: current, as of main at commit `d1ec067` (November 13, 2026, after #338 and #341). Outcome on main: the verdicts below are the review's at that commit (#344); its fixes are the next PR (`claude/clean-power-review-fixes`), which also corrects three line references to section 8 here; the booking and the L3 re-check follow. Reviewer: Claude Code, `session_01UQzgButU9bQRw8o2Tq3QvS`. It changes nothing in the dossier. Every fix below is a later step, in a second PR by this reviewer once this one is approved. The booking is the lead's tier-3 step after those fixes.

Espen's decisions on clean power (`DEC-2026-11-13-06`, memos 1-7; `-07`, points 1-14) are settled. Where a decided choice has a cost or gap the dossier does not show, this review says so and puts it to Espen as a question. It does not argue the choice. Under `DEC-2026-11-10-07`, a clearly bounded uncertainty is not a defect. Every investigation asked for below names the decision it informs and whether it blocks that decision now.

## Verdicts

| Level | What it needs (`charter/PLAN.md` 3.2) | Verdict |
| --- | --- | --- |
| **L2, design** | Key parameters chosen (who, what, how much, who administers), with the main alternatives weighed | **Pass** (record fixes only, none blocking) |
| **L3, specified** | Provisions section by section (eligibility, benefit, administration, phase-in, remedies); evidence for each load-bearing claim; a cost range validated by models with stated limits; a delivery plan | **Not yet: close.** Three blockers, each a contained fix |

**Why L2 passes.** Seven memos weighed eleven forks, with two to four options each. The memos have a forks-at-a-glance table, outside benchmarks (JCT, CBO, Penn Wharton, Canada's PBO, NIBS) and the legacy designs as options. Fourteen narrower points went to Espen as a yes-or-no list. All are decided and recorded (`DEC-2026-11-13-06`, `-07`), and every memo's status line says so. Memo 7's own cost ($0.08 trillion) is superseded by section 6's bottom-up figure, and both the memo and the index say so.

**Why L3 is not yet.** Most of L3 is in place:
- section 4 specifies 53 provisions with parameters, vehicle, agency and evidence, plus a consistency table;
- section 5 puts every job through a named existing agency and record, with a timeline, remedies, states' roles and rural delivery;
- section 6 prices the decided set by fiscal year and reproduces from its tool to the cell (below);
- sections 7 and 8 give benchmarks, a household table, objections, triggers and hard stops.

The blockers:
1. **The first Climate Dividend has no rail on the date promised** (B-1). CLI-2A.03 pays the first dividend in the first quarter of 2030, "on the child benefit's rail" (CLI-2A.02). The secure floor's rail first pays "by July 2030" (`dossiers/secure-floor/5-delivery.md:46`). The price starts January 1, 2030, possibly days after R2 is enacted, against the dossier's own six-month rule for a late act. "Paid first" is a decided commitment (memo 1 part 2 A; a hard stop in section 8). As written it has no delivery mechanism.
2. **Money and its terms ride different bills** (B-2). The transition guarantee's payments ride R3 (51 votes), but who is covered (CLI-11.01) and its paid-first rule (CLI-11.08) ride the 60-vote clean power act. Premium help (CLI-7.01) is spending but rides the 60-vote act too. And the reinsurance facility (R2) is "offered only in states that meet" a codes condition that also rides the 60-vote act. Section 8 says what reconciliation carries "stands alone". On the dossier's own vehicles, it does not. These are inconsistent commitments.
3. **The 100%-by-2040 standard is unmodeled, and its payments are uncounted and have no destination** (O-1). The project's carbon model reaches 91% clean power in 2040, with an economy-wide fee and a standard held at 80%. At the $40 cap, suppliers would pay on the shortfall: on the reviewer's arithmetic, roughly $15-25 billion a year around 2040. That money flows from ratepayers to the Treasury. Section 6 does not count it. Section 7's bill figures leave it out. Section 9 says bills rise only "at first". And the payments' only named use, bill protection, sunsets on its own trigger.

**What can reach L3 once those land.** Every provision can. None is held back by an unspecified parameter. The open items are bounded working choices with ranges, other owners' decisions or the booking's questions:
- the guarantee's inputs (a count of workers at closing plants and mines);
- automatic LIHEAP's reach;
- the covered-facility count;
- where the transition share sits after FY2039, and how the budget records the public builders' borrowing (left to the booking, as the lead asked);
- the builder of last resort's vehicle, which is Espen's (part 3).

## How this review was done

- **Read.** The charter: the standards, the board, plan 3.2, the template, `DEC-2026-11-09-13`, `-10-05`, `-10-07` and `DEC-2026-11-13-06` to `-09`. The secure floor's review as the pattern. All of `dossiers/clean-power/`: the README, sections 1-9, memos 1-7 and their index, `provisions.json` and the three tools. The evidence entries behind every load-bearing figure. The reviewer's notes on #338 and #341. `legacy/index/climate-carbon-model.md` for the model's clean-power path.
- **Mechanical checks.** A Standard (Sonnet) subagent ran them. The reviewer re-checked its key readings (the plan-wide gap at the head, the tool's hard-coded gap, the transition share) before using them. See "Checks run".
- **Primary law looked up:**
  - 16 U.S.C. 824p(k): federal backstop siting does not apply in ERCOT.
  - 42 U.S.C. 16421a: WAPA's Transmission Infrastructure Program. Its terminus and purpose limits, its $3.25 billion cap, project-only repayment and forgiveness of unpaid balances.
  - 42 U.S.C. 18713: DOE's Transmission Facilitation Program and its partnership and ownership authority.
- **The reviewer's own arithmetic** (not model runs): the standard's shortfall payments to 2040 (O-1); automatic LIHEAP's matched households against $12 billion (O-2); the transition-share and plan-wide-gap restatements (F-1).

## 1. The decisions, carried out

Each decided item checked against section 4, `provisions.json`, sections 5-6 and the memos:

| Decision | Where | Verdict |
| --- | --- | --- |
| Memo 1 part 1 B, power and industry, with the border adjustment; point 2 | REV-C1G.01, .02, REV-C1A.01, REV-C1P.01, REV-C2.01 | Faithful. The charge point moved from "fuel sold to power plants" (memo 1 B) to reported emissions, as a labeled working choice. That is sound under `DEC-2026-11-13-08`, but industrial facilities report yearly, not quarterly (B-1), and coverage outside the Acid Rain Program's area needs checking (M-2) |
| Memo 1 part 2 A, the dividend per adult, paid first; points 5, 6 | CLI-2A.01 to .04 | Faithful in text. "Paid first" has no rail on the date (B-1) |
| Point 3, the methane fee from 2030 | REV-C3.01 | Faithful |
| Memo 2 part 1 B, credits with a step-down; point 7 | CLI-1A.01 to .04 | Faithful; the cost risk is disclosed and bounded by the trigger |
| Memo 2 part 2 A, contracts for difference and Buy Clean | CLI-9.01, .02 | Faithful |
| Memo 3 part 1 B, 80% by 2035 and 100% by 2040, capped payment | CLI-3A.01, .02 | Faithful in text. The 2040 target is not run on any model, and its payments are unpriced (O-1) |
| Memo 3 part 2 A, the finding and the numbers in statute | CLI-4A.01, CLI-4E.01 | Faithful |
| Memo 4 part 1 B, the grid statute and financing, public power as builder of last resort; points 10, 11 | CLI-6A.01 to .03, CLI-10G.01, CLI-10.01 to .03 | Faithful, except the builder's vehicle. Memo 4 B says "a federal transmission authority, on TVA's model"; CLI-10.03 uses WAPA's program, extended. That is open with Espen (part 3) |
| Memo 4 part 2 A, permitting in either case | CLI-3A.03, .04 | Faithful |
| Memo 5 B, the automatic bill credit; point 12 | CLI-5H.01, .02, CLI-5L.01, CLI-5W.01, CLI-5F.01 | Faithful. Reach and cost rest on an untested linear assumption (O-2); FDPIR households are missed (M-1) |
| Memo 6 A, the disaster package with reinsurance; point 13 | CLI-7K.01, CLI-7.01, CLI-7N.01, CLI-7C.01, CLI-8.01 | Faithful in substance; the vehicles split the money from its condition (B-2) |
| Memo 7 B, with Espen's four parameters | CLI-11.01 to .08 | Faithful on every parameter: cap at twice the median wage, unemployment benefits counted, contractors covered, hourly top-up with no job test and published counts. Eligibility rides the wrong bill (B-2); tribal governments' lost revenue is not covered (M-1) |
| Points 1, 8, 9, 14 | CLI-14.01, .02, CLI-4H.01, CLI-13A.01, CLI-13F.01 | Faithful. CLI-4H.01's schedule is an optimistic working choice (O-4) |

## 2. Findings

IDs: B blocking delivery gap; O optimistic assumptions; M missing populations; A cheaper alternatives; F fiscal report; W weak evidence; L design lens; E section 9; C consistency and record. **Blocking** means blocking L3. Line numbers are at `d1ec067`.

### B. Delivery

**B-1. The first dividend, and the price's collection, on the stated dates. Blocking.**
- **What the dossier says.** "The first payment goes out in the first quarter of 2030, before the price reaches bills, from an advance repaid ... within the year" (CLI-2A.03, `4-specification.md:45`). It is paid "on the child benefit's rail and notice (FAM-1.09)" (CLI-2A.02, `:44`). The timeline enacts R2 "by January 2030", starts the price January 1, 2030, and pays the dividend in the first quarter (`5-delivery.md:65-67`). "No dividend paid after the price starts" is a hard stop (`8-change-our-minds.md:54`).
- **The gap.**
  - The child benefit's rail first pays "by July 2030" (`dossiers/secure-floor/5-delivery.md:46`; FAM-1.07). A first-quarter dividend on that rail cannot be paid.
  - If R2 is enacted in late 2029 or January 2030, a January 1 price breaks the dossier's own late-act rule: the price starts "at least six months after enactment" (`5-delivery.md:80`).
  - So under the hard stop, the price start moves to about mid-2030. Section 6 prices FY2030 on the booked year shape, which assumes the price from January 2030, and never says what a later start does.
- **Collection.** CLI-2A.01 and REV-C1G.01 charge "each covered facility's reported emissions for the quarter". Power plants report quarterly under 40 CFR part 75, but industrial facilities report once a year, by March 31, under part 98. "EPA certifies a quarterly total per facility" (`5-delivery.md:11`) does not exist for industry.
- **The measuring base depends on the 60-vote act.** The price relies on part 98. EPA stopped publishing the inventory in 2025-26 [EV-CLP-103], and the reporting program itself has been cut back (`1-problem.md`, part C). Keeping part 98 in statute is CLI-14.02, which rides the 60-vote act, not R2 with the price.
- **Why blocking.** "Paid first" is the design's central political protection (memo 1, the lesson from Canada) and a decided commitment. As written it has no delivery mechanism on its date.
- **The fix** (no new decision; it carries out memo 1 part 2 A):
  1. Pay the first dividend as a one-time payment by Treasury from the latest return and SSA, VA and Railroad Retirement records, the 2020-21 economic impact payments' machinery, which already exists. Then move to the shared rail from its first month. Alternatively, start the price on the first quarter that begins at least six months after enactment and after the rail's first payment (July 2030 at the earliest), and say what that does to FY2030 in section 6.
  2. Make the six-month rule the base case, not only the late-act case.
  3. Industrial facilities pay quarterly estimated amounts on last year's reported emissions, trued up on the annual part 98 report, as estimated taxes are. Power plants pay on part 75's quarterly data.
  4. Put the part 98 reporting duty the price needs into R2, as part of the tax base's definition. Leave the inventory's publication date in CLI-14.02.

**B-2. Money and its terms on different bills. Blocking.**
- **What section 4 says.** R3 carries "the transition guarantee's money (CLI-11.02 to .07)". The clean power and climate act (60 votes, or the rules reform) carries "the transition guarantee's terms (CLI-11.01, .08)" and "the disaster statute's rules and codes (CLI-7.01, CLI-8.01)" (`4-specification.md:21-22`). R2 carries the reinsurance facility, "offered only in states that meet CLI-8.01" (`:115`).
- **The gap.**
  - CLI-11.01 says who is covered. Without it, R3's payments have no beneficiaries.
  - CLI-11.08 (paid first from the transition share, and an entitlement) is a money rule.
  - CLI-7.01's premium help is spending.
  - If the 60-vote act fails, R2's facility either runs with no codes condition or not at all, and the dossier does not say which.
  - Section 8 says that if the rules reform fails, what reconciliation carries, "the guarantee and the disaster package", "stands alone" (`8-change-our-minds.md:39`). On the dossier's own vehicles it does not.
- **Why blocking.** These are inconsistent commitments on the delivery path of two decided memos (6 A and 7 B), and the rules reform is uncertain (legacy D2).
- **The fix.**
  - Move CLI-11.01 and CLI-11.08 into R3 with the money. Eligibility that determines outlays is reconciliation-eligible.
  - Move CLI-7.01's premium help into R2 with the disaster capital. Leave its non-budget rules (one survivor application, the heat hazard) in the act.
  - For the facility, write the codes condition into R2 as a condition on the facility's own coverage. Say the Byrd-rule risk plainly, and what happens if it is struck: the facility waits for the act, or starts without the condition. That fallback is a working choice; the reviewer suggests waiting, which keeps point 13 whole.
  - Section 8's "stands alone" sentence then holds as written.

**B-3. Smaller delivery points. Not blocking.**
- **Contractors' records** (CLI-11.01). The guarantee covers contractors' workers from "the employer's and contractors' payroll records for the site, filed once with the notice" (`4-specification.md:124`). Nothing requires a contractor to file, and the WARN Act does not reach contractors' employees. One sentence: the facility owner's notice lists its site contractors; each contractor files its site payroll within 30 days; the same remedy applies (`5-delivery.md:89`). A contractor's worker may also show coverage from their own pay stubs.
- **"Permanently cuts its workforce"** (CLI-11.01) has no threshold. Use the WARN Act's mass-layoff definition, and the state notice for smaller sites, so the rule is the one employers already know.

### O. Optimistic assumptions

**O-1. The 100%-by-2040 standard, and where its payments go. Blocking.**
- **What is claimed.** The standard rises in a straight line to 80% in 2035 and 100% in 2040 (CLI-3A.01). A supplier short of credits pays $40 a megawatt-hour in 2025 dollars, indexed (CLI-3A.02). The payments go to bill protection, "on the carbon model about $0.05 trillion over 2030-39" (`4-specification.md:71`). Bill protection ends when real prices stay below their 2029 level for two years (CLI-5L.01, point 12). Section 7 checks only 2035 (`7-validation.md:13`). Section 9 says bills rise "somewhat, at first" (`9-public-case.md:40`).
- **The evidence.** The legacy carbon model's $0.05 trillion is for a standard of 80% by 2035 held at 80% afterwards. Under that standard, the clean share is 75% in 2035, 80% in 2037 and **91% in 2040**, with an economy-wide fee and every other measure (`legacy/index/climate-carbon-model.md`, the yearly table and the Clean Energy Standard paragraph) [EV-CLP-708] [EV-CLP-723]. The model says the limit is grid access, not price. At the cap, a higher target buys no more clean building, only more payments. No model has run 100% by 2040.
- **The reviewer's arithmetic.**
  - On the decided path the requirement is 84% in 2036, 88% in 2037, 92% in 2038, 96% in 2039 and 100% in 2040.
  - Against the model's path, the shortfall is about 6-9 points a year from 2036.
  - At about 4,500-5,000 TWh of retail sales around 2040 (judgment; today's sales are about 4,000 TWh), one point is about 45-50 TWh.
  - So payments are roughly $15-20 billion a year in 2025 dollars by 2038-40, about $15-25 billion nominal. That puts 2030-39 at roughly $0.08-0.12 trillion, against the $0.05 trillion the dossier carries, and the payments continue until the target is met.
  - The range is wide, and memo 1 B's narrower price could move it a little either way. It is the right order of magnitude.
- **What follows.**
  - (a) Ratepayers carry this as a charge on every bill. Section 7's household table and section 9's "at first" leave it out.
  - (b) The payments are federal receipts (Treasury collects them, `4-specification.md:71`). Under the plan's convention an excise-like receipt carries the 24.4% income and payroll tax offset (CX). The full flow is not in section 6. Even the model's $0.05 trillion does not match the $7.2 billion booked for bill protection (CLI-5L).
  - (c) Once bill protection sunsets, the payments have no named use. That is a missing delivery mechanism for money the act raises.
- **Why blocking.** A material flow is left out of the fiscal report and the bill figures, and section 9 states the opposite of what the arithmetic shows.
- **The fix** (no new decision: the cap and targets are decided; the payments' use is a working choice):
  1. Section 6, part 2: the payments by year on the reviewer's arithmetic, as a receipt and an outlay, with the CX offset noted as the booking's question.
  2. CLI-3A.02: the payments go to the bill credit (CLI-5H.01), which section 8 already says "continues; it does not sunset" (`8-change-our-minds.md:33`). Bill protection is then the part of the credit they pay for, and nothing is stranded. Section 8's alternative (into transmission) stays the fallback.
  3. Section 7: a line on 2036-40, and the payments' effect on bills by about 2040.
  4. Section 9: "Somewhat, while the grid is built; what utilities pay when they fall short goes back to lower- and moderate-income households."
  5. The booking's rerun runs the decided 100%-by-2040 path. That **informs the booking**. It does not block, because the reviewer's arithmetic is enough to correct the record now.

**O-2. Automatic LIHEAP: who is matched, against a fixed $12 billion. Not blocking.**
- **What is claimed.** Households enrolled in SNAP, SSI or LIHEAP "at any time in the prior year" get a credit "toward 6% of income" (CLI-5H.01). The money is "LIHEAP's block grant made mandatory at about $12 billion a year", on the assumption that it reaches "about half" of eligible households, three times today's 17% [EV-CLP-038] (`6-cost.md:58`).
- **The gap.**
  - LIHEAP's 5.9 million households at 17% imply about 35 million eligible [EV-CLP-038].
  - SNAP alone serves about 22 million households in an average month (USDA; reviewer's figure, not in the register), and more over a year. Add SSI and today's LIHEAP households, and the automatic roll is likely well over half of those eligible.
  - At $12 billion, that is roughly $400-500 a household, below the average benefit today, and short of 6% of income for many.
  - "$12 billion is three times $4 billion" is a linear assumption the tool does not label (Checks run, 3), and the 2.2% growth rate has no basis.
- **What follows.** The design is decided; how much each household gets is not. The dossier should say which it is:
  - a fixed pot with a published formula that prorates the credit (the reviewer recommends this: simpler, and the cost is known); or
  - an entitlement to the 6% target, at roughly $15-20 billion a year (reviewer's judgment).
- **The fix.** Register SNAP's and SSI's household counts. State the matched households, the average credit at $12 billion, and the pot-or-entitlement choice as a working choice. Label the linear assumption and the 2.2% rate. If the entitlement is preferred, put it to Espen with its cost. **Investigation:** the 2027-28 preparation match sizes it. It informs the credit's size, and does not block.
- **Timing.** The money starts "from FY2030", but CLI-5H.01 rides R3, enacted about summer 2030, with first credits in winter 2030-31. Say FY2031.

**O-3. The guarantee's count leaves out the gas fleet's wind-down. Not blocking.** The 8,000 covered layoffs a year rest on coal: about 140 GW closing by 2040 at about 0.18 jobs a megawatt, plus contractors, mines, refineries and gas plants (`6-cost.md:67`). But CLI-11.01 covers gas-fired plants too. Under 100% clean power by 2040, unabated gas must stop serving retail sales by then, or pay O-1's payments. Gas plants employ fewer people per megawatt than coal, but the fleet is several times larger, so covered layoffs in 2036-40 and the FY2040 cost ($1.7 billion) lean low. The fix: one line in the input table saying the range's top ($40 billion; $5 billion in FY2040) is the gas-fleet case. Add EIA's gas fleet and plant employment to "Evidence still needed". It is bounded: the cost of being wrong is a few billion dollars a year (`6-cost.md:80`), and the guarantee is an entitlement either way.

**O-4. The clean-heat standard's schedule. Not blocking; a design-lens point.**
- **The schedule.** CLI-4H.01 sets one share for "space- and water-heating equipment": 60% heat pumps or other zero-emission heat in 2032, 5 points more a year, 100% in 2040 (working choice).
- **The problem.** For space heating, heat pumps already sell about as well as gas furnaces (reviewer's understanding; AHRI's data, which "Evidence still needed" asks for, settles it). For water heaters, heat pumps are a small share today. A manufacturer that makes mostly water heaters could not reach 60% in 2032.
- **The household burden.** At 100% in 2040, a household whose furnace or water heater fails must buy a heat pump. In cold climates, homes on propane or oil, and homes that need a panel upgrade, that is a real cost at the worst moment. Point 9's burden line ("the choice of equipment") understates it, and low-income help comes only through the credits (under 80% of area median income) and Weatherization.
- **The fix** (working choices): separate schedules for space and water heating, each starting from AHRI's 2029 shares; a burden-table row with the replacement-cost range and who pays it; and an emergency-replacement rule (a household may install a like-for-like unit once during the phase-in, counted against the manufacturer's next year).

**O-5. Receipts above the threshold. Not blocking; label it.** The read takes power and industry's receipts from the carbon model's sectors (`6-cost.md:42`). The model's "industry" includes combustion at facilities below 25,000 tons, which REV-C1G.01 does not charge. So the receipts and the dividend lean high. The fiscal effect is small: each lost dollar of receipts lowers the offset by 24.4 cents and raises the add-ons' cost by 20 cents. Say so in part 1 and in sensitivities. The covered-facility count (`4-specification.md:177`) sizes it.

### M. Missing populations

**M-1. Tribal nations. Not blocking; one question for Espen.**
- **The bill credit misses FDPIR households.** Households on the Food Distribution Program on Indian Reservations may not take SNAP at the same time, so a match of SNAP rolls misses them. Many tribes also run their own LIHEAP grants. CLI-5H.01 should match FDPIR rolls and pay through tribal LIHEAP grantees as through states.
- **Tax-base replacement does not reach tribal governments.** CLI-11.06 replaces lost *property tax* for "a county, school district or other local taxing unit". Tribal governments that host coal plants and mines lose lease, royalty and tax revenue under tribal law, not county property tax. The Navajo Generating Station and Kayenta mine closures in 2019 are the example (reviewer's knowledge; the fix step registers a source). As written, the places with the deepest dependence get nothing. Extending CLI-11.06 to a tribal government's lost revenue from a covered facility is a benefit for a new group, so it is Espen's (question 2). The cost is likely small, a few hundred million dollars over ten years (reviewer's judgment; the fix step should find the Navajo Nation's and Hopi Tribe's reported losses).
- **Front doors.** The dividend uses the child benefit's front doors (CLI-2A.02). If the secure floor's fixes added tribal offices and IHS facilities there (its review's M-2), say so here. If not, add them.

**M-2. Places where the price falls hardest. Not blocking.**
- **Coverage outside the Acid Rain Program's area.** REV-C1G.01 defines power plants as part 75 units. The reviewer understands the Acid Rain Program's affected units to be in the contiguous states. If so, oil-fired plants in Hawaii, Puerto Rico and Alaska are covered only if they count as "industrial facilities" under part 98, which the provision does not say. The fix step should check this against 40 CFR parts 72-75 and 98 and write coverage explicitly. Either way, the territories' line (`4-specification.md:151`) should say whether their power plants pay.
- **The household table is national.** It "has no regional split" (`7-validation.md:25`). Low-income households where power is mostly coal (West Virginia, Wyoming, Missouri) or oil (Hawaii, Puerto Rico) see larger electricity increases against the same dividend, and may be behind on the carbon channel. Section 7, part 4 should say so, with what reaches them first (the bill credit, bill protection). Section 9's "the lowest-income two-fifths ... come out ahead" should read "on average, nationally" (E-1).

**M-3. Groups placed well.** Each is placed:
- households heating with gas or oil;
- adults outside the tax and benefit systems;
- children (through the child benefit);
- renters with heat in the rent;
- rural co-op customers;
- oil and gas field workers, who are left out of the guarantee on purpose, priced in part 2 and named in section 9's can't-say list (`4-specification.md:146-152`).

### A. Cheaper alternatives

Memo 1 weighed an economy-wide fee, no price and a delayed fee. Memo 2 weighed a cheaper credit set (C). Memo 5 weighed relying on the dividend alone. The reviewer found no unweighed cheaper design that reaches the same people for the main lines. Two points use existing machinery more fully:

**A-1. The first dividend through the economic impact payments' machinery** (B-1's fix). Existing, proven in 2020-21, and cheaper than waiting for, or rushing, the new rail.

**A-2. DOE's Transmission Facilitation Program, already national** (part 3). 42 U.S.C. 18713 already lets DOE "participate with an eligible entity in designing, developing, constructing, operating, maintaining, or owning" a line in a national interest corridor, or one that crosses states or planning regions. Costs are recovered "through rates charged to customers benefitting", and borrowing is $2.5 billion. The dossier runs both grid tranches through this office but never weighs it as the builder. It needs a partner today; one amendment would let DOE build alone where no partner files. Part 3 weighs it as the fallback.

### F. The fiscal-rule report (`DEC-2026-11-10-05`) and the money

**The report itself follows `DEC-2026-11-10-05`.** Section 6, part 4:
- gives the yearly cost (about $126 billion in FY2030 rising to $226 billion in FY2039) and the permanent cost from FY2040 ($147.4 billion, 0.27% of GDP);
- gives the net change a booking would make (+$42 billion over FY2030-39, −$17.5 billion in FY2040), and the share of the plan-wide margin;
- is on one basis (fiscal years, against the booked case `mixed`), shows the booking beside it and says why they differ;
- keeps spending lines and revenue effects apart: the CX offset is never added to a spending line;
- keeps contingent items (the credits' risk, the facility's exposure, permit damages) apart from firm ones in part 2.

It reports the gap and sends no part of it to Espen, which is right.

**The figures asked for, traced.**

| Figure | Reproduced | Traced to |
| --- | --- | --- |
| $1,852.4 billion over FY2030-39 (about $1.85 trillion) | Yes, every cell within 0.1 | The booked rows (audit lines, case `mixed`) plus four changes |
| +$41.6 billion against the booked rows ($1,810.8 billion) | Yes | Memo 1 B −$30.7 billion; memo 4 B +$60 billion; memo 7 B +$12.2 billion |
| $147.4 billion in FY2040, −$17.5 billion | Yes | Memo 1 B −$29.1 billion; memo 5 B +$9.9 billion; memo 7 B +$1.7 billion |
| Memo 1 B: share 68.5% to 58.1%; $1.26 of $2.00 trillion | Yes (1,263.7 of 1,996.0) | The carbon model read [EV-CLP-714], a grade D project estimate, labeled |
| Memo 4 B: $60 billion | Yes ($61.8 billion entered as 60) | First tranche's ratio, $32 billion for $145 billion [EV-CLP-717], grade D, labeled; the year shape is judgment |
| Memo 5 B: $9.9 billion in FY2040 | Yes | $4 billion [EV-CLP-035] and 17% [EV-CLP-038]; "half" and the tripling are judgment, unlabeled (O-2); 2.2% growth unlabeled |
| Memo 7 B: $12.2 billion; $1.7 billion | Yes (workers $5.5 billion, places $6.5 billion, refinancing $0.25 billion) | The wage gap [EV-CLP-517] [EV-CLP-518], coal capacity [EV-CLP-508], mine jobs [EV-CLP-500], Rosebud [EV-CLP-514]; every other input labeled judgment in `6-cost.md:67-75`. Four inputs in the tool are unlabeled (W-1) |

**F-1. The plan-wide gap is out of date. Not blocking; a record fix.** Part 4 uses $4,256.6 billion (7.86% of GDP) "at main's head" (`6-cost.md:126`). That was the value at `6204281`. #339 (the INC-4 and immigration memo 6 rebook) has since merged, and the head gives **$4,245.4 billion (7.84%)**. On that base:
- the decided set is 3.5% of the gap (3.47%);
- the booking's change is −0.41%, to about $4,228 billion (7.81%);
- "now under way" should read "merged".

Also:
- `6-cost.md:9` and `:112` call `6204281` "main's head"; the booked climate rows are byte-identical at the head, so name the head or say "booked rows unchanged at `d1ec067`";
- `clean_power_path.py` hard-codes the old gap (`PLAN_GAP_FY2040 = 4256.6`); read it from `models/data/recovery-budget-paths.csv` instead;
- `3-design.md:106`'s "$4,239 billion after #313" can stay as the first estimate, but should say so.

**F-2. The transition share in FY2040.** Part 2 says "about $32 billion" (`6-cost.md:90`). On the tool's own numbers FY2040 is $33.1 billion ($32.6 billion is FY2039). Use $33 billion. Where the share sits after FY2039 is the booking's question, as the lead set it.

**F-3. Items not counted, in both directions. Not blocking; label them.**
- The standard's payments (O-1): a receipt and an outlay, with the CX question.
- WAPA's program forgives any balance left at the end of a project's life (42 U.S.C. 16421a(d)(2)). So does the Transmission Facilitation Program (42 U.S.C. 18713(d)(4)(B)). Whichever builder Espen chooses, its borrowing is not costless if a line's rates do not repay it. Part 2's row on the builders' borrowing should name this for the booking.
- The builders' borrowing limits bound the builder: WAPA's program at $10 billion (CLI-10.02) covers a few large lines at most. Say so beside CLI-10.03.
- B-1's first dividend, if paid before the price raises anything: an advance with a few months' interest, small.

**F-4. The booking list (part 6), reviewed for correctness only.** It will be the lead's tier-3 PR. Its structure is right: rerun or keep the read; REV-C1 at about $1.20 trillion with CX following; CLI-2 at 80% of the new C1; new rows for CLI-10, CLI-5H and CLI-11; the rows left as booked. Points to add:
1. The standard's payments (O-1), and whether they carry the CX offset.
2. CLI-5H's start in FY2031 (O-2), and the pot-or-entitlement choice.
3. The FY2030 price start if B-1's fix moves it.
4. Forgiveness under the builder's statute (F-3).
5. Where the booking can use the M4 energy model (`models/tools/energy/`, `DEC-2026-11-13-09`): for the 100%-by-2040 run and memo 1 B's coverage, if M4 has them by then. The booking need not wait for M4: the legacy model's coverage setting (part 6, step 1) is enough.

### W. Weak evidence

**W-1. Load-bearing D and E figures.** Labeled, and that is right, but:
- Memo 1 B's receipts and dividend are the legacy model read (grade D) [EV-CLP-714] [EV-CLP-705]. The model responds slowly, so the dividend leans high; section 7 says so.
- The guarantee's inputs are mostly judgment. Four inputs in `clean_power_path.py` have no label at all: training months (12), administration (5%), the first-year factor (0.5) and the places line's 2% growth. Label them in the tool and in part 1's table.
- The second tranche's ratio rests on one legacy figure [EV-CLP-717].

**W-2. Registry.** `models/registry/check.py` passes with 43 EV-CLP warnings on 40 entries: 35 uncorroborated analysis entries and 8 contested ones. Most of the uncorroborated ones are the grade D legacy restatements (700-724), which are flagged only for want of a second publisher, and the dossier presents them as project estimates. That is not a defect. EV-CLP-302 and 303 (British Columbia) are contested, and sections 2, 7 and the memo present both views. Four warned entries (241, 248, 316, 712) are cited nowhere. With 27 other uncited entries, the fix step should cite or drop them.

**W-3. "Cheaper" power.** Section 9's "New solar and wind cost less than new gas plants before any tax credit" (`9-public-case.md:31`) rests on ranges that overlap ($40-98 and $37-99 against $51-129) [EV-CLP-456] [EV-CLP-457], and levelized cost leaves out firming. Say "often cost less".

### L. Design lens (`DEC-2026-11-09-13`, `DEC-2026-11-13-08`)

The design is strong on both rules:
- no household is charged directly;
- the dividend is paid from records, with one page for the rest;
- the bill credit comes with no application for anyone already on SNAP, SSI or LIHEAP;
- the guarantee pays on records the employer already files, with no means test and no job test, and is watched by published counts with a review trigger, not a gate;
- the price is charged on emissions EPA already measures, not on fuel tracked through every distributor;
- the standard uses the states' certificate systems, not a new registry;
- tax-base payments go through PILT;
- codes are a condition on new aid only.

Section 5 names an existing agency, record and payment system for every job (`5-delivery.md:9-37`). Gaps:
- **L-1.** The clean-heat standard's household burden (O-4).
- **L-2.** The burden table (`3-design.md`, "Burden of each requirement") lacks rows for the guarantee's monthly hours statement (one form a month for up to two years, checked after the fact; a reasonable price for no job test, but say so) and for the contractor's six-in-twelve-months test (B-3).
- **L-3.** Part 3 below applies `DEC-2026-11-13-08` to the builder.

### E. Section 9 against sections 1-8

Every number traces to sections 1-8 with its ID or as labeled project arithmetic, with the exceptions below. "On our estimates" is used where it should be. The can't-say list refuses "meets the 2035 goal" and "every family comes out ahead", and section 9 states the cost plainly. That is good public-case practice.

**E-1. Claims to correct with the blockers.**
- "Somewhat, at first" (`:40`): per O-1.
- "Paid before the price reaches bills" (`:11`, `:58`): per B-1's fix.
- "The lowest-income two-fifths ... come out ahead" (`:40`, `:59`): add "on average, nationally" (M-2).

**E-2. Traces that miss.** Not blocking.
- "Disasters costing $1 billion or more hit 23 times in 2025, at about $115 billion" [EV-CLP-130] (`:7`). Section 1 says 24 at $118.5 billion [EV-CLP-124] [EV-CLP-125], the later revision. Use section 1's figure and fix the source-table row (`:72`).
- Marcus's "$26 an hour" job and lineworker training (`:49`) appear nowhere in sections 1-8. Section 7's miner (`7-validation.md:68`) has them, so cite section 7, part 4 in the row (`:80`), not section 4.
- Rosebud County (`:50`), "close to what the budget already carries" (`:21`, `:41`) and "before the plan's financing" have no source-table rows. Add them (sections 4 and 6).
- "The top two-fifths pay more than they get" (`:59`): the middle fifth is −$6 too. Section 7 calls it "about even", so this holds, but "the top three-fifths are about even or behind" is the exact reading.
- "Above a once-in-a-century loss" (`:43`, `:63`) simplifies a state-level 1-in-100 to 1-in-250 layer. That is fine for the public case, with the cap stated, as it is.

**E-3. The builder's vehicle.** #338's review asked that the WAPA change be surfaced. The README's note does it for Espen. Section 9's "a public builder" is neutral and can stay until Espen decides (part 3).

### C. Consistency and record

The E-C2 worker said it applied the reviewer's notes on #338 and #341. Each one checked:

| Note | Applied? |
| --- | --- |
| ERCOT and WAPA cost recovery (#338, 1) | Yes: CLI-10.03 names PUCT-approved cost-of-service rates in ERCOT and says WAPA's program "has mostly lent and partnered". Part 3 finds the ERCOT route is not workable as written (no federal siting backstop there, and PUCT's approval is not the act's to give) |
| Surfacing the WAPA vehicle change (#338, 2) | Yes: the README's note for Espen and `5-delivery.md:42` |
| Coal figures, 172 GW against 140 GW (#338, 3) | Yes: `6-cost.md:67` and the tool's comment agree |
| Stale totals in section 3, the memo index and the decision entry (#338, 4) | Yes: the memo index and section 3's status line carry both figures; the decision entry stays as labeled "before booking" |
| The 42% emissions floor (#341, 1) | Yes: now 40-48%, with both ends explained. The top end is Package A's result with buildings priced and a 90% standard; since the model finds the standard's level barely moves 2035 emissions, the decided set probably sits in the middle. A one-line note will do |
| Large loads in ERCOT (#341, 2) | Yes: CLI-6A.03's condition on federal money |

Other record points:
- **C-1.** `3-design.md:96-97` shows the FY2040 subtotals as $71.0 and $76.4 billion; the exact values are $71.1 and $76.3 billion (the total ties).
- **C-2.** `clean_power_path.py:71`'s comment says "about $9.7B in FY2040"; the code gives $9.9 billion.
- **C-3.** Memo 1 B's "about $430 an adult in 2035" and "charged on fuel sold to power plants" are decided text. Section 6's $439 and section 4's charge on reported emissions supersede them. Add a line to memo 1's status line, as memo 7's has.
- **C-4.** The agenda: CLI-13 (the parent) is L1 `option` while CLI-13A and 13F are L2 `decided`. Give the parent a note that its decided children are at L2. All 36 decided rows are L2 `decided` and cite `-06` or `-07` correctly.
- **C-5.** Status lines. Sections 4-9 and the README read "draft ... at L2, for the milestone review". After the fixes they should read "reviewed (L2); L3 after the fixes and the booking".

### Seams with other dossiers

- **Secure floor.** The dividend's rail is the floor's FAM-1.09, and its first-payment date is B-1's. The offset protection follows FAM-1.07 as a working choice. Shared rule 1 is cited, not re-decided.
- **Immigration.** Rule 3 is cited, not re-decided.
- **Work.** Oil and gas field workers and LAB-8 are the seam, named.
- **Transportation.** Road fuels are out (point 2) and MOV-29 prices them.
- **Housing.** HOU-12 is the front door.
- **Care.** The guarantee carries no health benefit; that seam is named.
- **Fair financing.** The CX offset, the standard's payments (O-1) and the transition share after FY2039 are its seams.
- **M4.** The booking may use it but need not wait (F-4).

## 3. The builder of last resort: a choice for Espen

**The question.** Memo 4 B, as Espen approved it, adds "a federal transmission authority, on TVA's model, that builds national-interest lines where no one else will". Section 4 delivers it instead through WAPA's Transmission Infrastructure Program, extended nationwide, with TVA and Bonneville building in their own regions (CLI-10.03), under the rule to use existing machinery first. Espen has not decided. This part compares the two:
- **A.** WAPA's program, extended nationwide (the current draft).
- **B.** TVA, Bonneville and WAPA building in their own regions, plus a new TVA-style authority only for the gaps: the East outside TVA, and Texas.

CLI-10.03 is not changed until Espen decides.

**What the law says today.**
- **WAPA's program** (42 U.S.C. 16421a) may already borrow up to $3.25 billion for "constructing, financing, facilitating, planning, operating, maintaining" lines. So it may build, not only lend, though it has mostly lent and partnered. But each line must have "at least one terminus within the area served by" WAPA (15 western and central states), and must deliver power from renewable resources. Each project is accounted for separately, its own revenue is "the only source" of repayment, and any balance left at the end of its life is forgiven.
- **Federal backstop siting** (16 U.S.C. 824p) "shall not apply" in ERCOT (subsection (k)). FERC sets no rates there.
- **DOE's Transmission Facilitation Program** (42 U.S.C. 18713) is already national. DOE may co-own and help build lines in a national interest corridor, or lines that serve demand across states or planning regions, and may recover costs through the rates of those who benefit. It needs a partner, and its borrowing limit is $2.5 billion.

| | **A. WAPA nationwide** | **B. Regional builders plus a TVA-style authority for the gaps** |
| --- | --- | --- |
| **Legal authority needed** | Amend 16421a: drop the western-terminus and renewable-only limits; raise the borrowing cap well above CLI-10.02's $10 billion; let WAPA own and operate lines inside other regions' markets and file rates there. Small in words, large in effect: it turns a western program into a national one | TVA, Bonneville and WAPA build in their own areas under authority they largely have, with point 11's borrowing. A new charter for the East: a federal corporation with a board, bond authority, rate-setting under FERC, and the right to build and own. More drafting, but one clean statute |
| **Start-up staff and offices where there is no federal power presence** | WAPA opens Eastern offices from nothing (the dossier's judgment: a few hundred staff). WAPA's western customers' rates are walled off by the separate-project rule, but its leadership and governance stay western | The new authority starts from nothing too: about the same field staff, plus a board and corporate functions. TVA (in the Southeast) and the other regional builders need no new offices |
| **Cost recovery in ERCOT** | No path as written: no federal siting backstop in ERCOT; PUCT need not admit a federal owner's costs to Texas's cost-of-service charge; FERC has no rate jurisdiction | The same problem. A new authority has no better standing in Texas than WAPA |
| **Delivery risk** | One agency and one budget line. But its program has done only a handful of projects since 2009 (reviewer's understanding), its borrowing cap covers a few large lines, and as part of DOE it depends on appropriations and on the administration of the day. The 2025 cancellations (EV-CLP-438, EV-CLP-440) show that exposure | A new corporation takes years to stand up (reviewer's judgment: two to four). But no window closes before about 2033, so that is not on the critical path. A corporation with its own bonds and board is better insulated from a later administration than a DOE office, and each regional builder knows its own utilities and markets |
| **Fit with Espen's decisions** | Fits "existing machinery first" in name. In the East it builds a new organization under WAPA's name | Fits memo 4 B as decided ("on TVA's model"). Fits "existing machinery first" wherever machinery exists, and creates something new only where none does |

**Texas, under either option.** Neither builder can site or recover costs inside ERCOT without Texas's cooperation. The reviewer recommends:
- leave lines inside ERCOT off the national-interest list unless Texas opts in by agreement;
- list ties between ERCOT and its neighbors, which FERC can order without making ERCOT federally regulated;
- for the rest of Texas, rely on the large-loads rule (CLI-6A.03, conditioned on federal money) and on Texas's own record of building lines when it decides to.

Under either option, CLI-10.03's ERCOT sentence changes.

**Recommendation: B, built lean.**
- TVA, Bonneville and WAPA, under its existing program, which can already build where a line touches its area, are the builders in their own regions, with point 11's borrowing. Southwestern Power Administration, which has lines in Arkansas, Missouri and Oklahoma, could be named for its area too.
- A new TVA-style transmission corporation is chartered in the act for the East outside TVA. It has a small staff until the first two-year windows close (about 2033), then grows as lines are assigned to it.
- ERCOT is off the list unless Texas opts in.
- If Espen wants no new entity at all, the cheaper fallback is not A but DOE's Transmission Facilitation Program, which is already national. One amendment would let DOE build alone where no partner files.
- The reason against A: it needs about as much new law and the same new Eastern staff as B. It bolts a national mission onto a western agency whose own statute fences it. It is no better in Texas. And it leaves the builder inside a DOE that was able to cancel grid commitments in 2025.

**In plain words, for Espen.** You approved "a federal transmission authority, on TVA's model". The draft instead stretches WAPA, a western federal power agency, to build anywhere in the country. WAPA's law lets it build only lines that touch its western territory, so either way Congress has to write new law, and either way someone has to hire new staff in the East from scratch. The difference is what you get at the end. Stretching WAPA makes a western agency inside the Energy Department responsible for the whole country. Option B lets TVA, Bonneville and WAPA build in the regions they already know, and creates a TVA-style public company only for the East, where nothing like it exists. We recommend B. Texas is a problem for both: federal law keeps Washington from siting or setting rates for power lines inside the Texas grid. We recommend leaving Texas off the list unless Texas agrees, while still building connections between Texas and its neighbors.

## For Espen

Two questions. The first is the open choice above. The second is a gap in a decided design. Neither reopens a decision.
1. **The builder of last resort** (part 3). "Build through WAPA nationwide (A), or through TVA, Bonneville and WAPA in their own regions plus a new TVA-style authority for the East (B)? And leave lines inside Texas off the list unless Texas agrees?" The reviewer recommends B, and Texas off unless it agrees.
2. **Tribal governments in the transition guarantee** (M-1). "The guarantee replaces a county's lost property tax when a plant or mine closes. Tribal nations that host plants and mines lose lease and royalty income instead, so as written they get nothing. Extend the declining ten-year replacement to that lost tribal revenue (likely a few hundred million dollars over ten years, to be priced)?" The reviewer recommends yes.

Possibly a third, from O-2, if the fix step finds the automatic bill credit's matched households far above half of those eligible: "Keep the bill credit as a fixed $12 billion a year shared across everyone matched (about $400-500 each), or guarantee each household the 6%-of-income target (about $15-20 billion a year)?"

## What the next steps should do

For the fix PR, by this reviewer once this PR is approved (`claude/clean-power-review-fixes`), unless marked for the lead. Steps 1-3 clear the blockers. Anything that changes a decided commitment, an adopted input in `models/data/inputs/` or the booking goes to the lead, not into the fixes.

1. **The first dividend and collection** (B-1, A-1). CLI-2A.02, .03 and REV-C1G.01: the first dividend as a one-time payment through the 2020-21 payments' machinery, then the shared rail; the six-month rule as the base case; quarterly estimated payments for part 98 facilities with an annual true-up; the part 98 duty the price needs moved into R2. Section 5's timeline, section 6 (the FY2030 note) and section 8's hard stop follow. **Tier:** Most capable.
2. **The vehicles** (B-2, B-3). CLI-11.01 and .08 into R3; CLI-7.01's premium help into R2; the facility's codes condition written into R2, with its Byrd-rule fallback (the reviewer suggests the facility waits); section 8's "stands alone" checked. The contractors' filing rule and the WARN threshold. **Tier:** Most capable.
3. **The standard's payments** (O-1, F-3, E-1). Section 6, part 2: the payments by year on the reviewer's arithmetic, as a receipt and an outlay, with the CX question for the booking; CLI-3A.02's payments to the bill credit; section 7's 2036-40 line; section 9's bill answer. **Tier:** Most capable.
4. **Section 6's record and the smaller cost items** (F-1, F-2, O-2, O-3, O-5, W-1, C-2). The plan-wide gap at the head, read from the paths file, not hard-coded; the transition share at $33 billion; LIHEAP's matched households, average credit and pot-or-entitlement choice, with FY2031; the gas-fleet note; the threshold note; the tool's unlabeled inputs. If the bill credit question goes to Espen, stop and send it to the lead. **Tier:** Standard, checked by the reviewer.
5. **Populations and the lens** (M-1, M-2, O-4, L-2). FDPIR and tribal LIHEAP in CLI-5H.01; tribal front doors; coverage outside the Acid Rain Program's area, from the regulations; the regional note in section 7; the clean-heat standard's separate schedules and emergency rule; burden-table rows. Do not write CLI-11.06's tribal extension until Espen answers question 2. **Tier:** Most capable, with a Standard subagent for the register entries (SNAP and SSI household counts, FDPIR, the Navajo and Hopi revenue losses, part 72-75 applicability).
6. **Section 9 and the record** (E-1 to E-2, W-2, W-3, C-1, C-3 to C-5), after steps 1-3. The disaster figure, source-table rows, "often cost less", "on average, nationally"; uncited entries cited or dropped; the section 3 subtotals; memo 1's status line; CLI-13's note in `agenda/agenda.csv`; status lines "reviewed (L2)". **Tier:** Most capable for section 9; record fixes by a Light subagent.
7. **CLI-10.03** after Espen answers question 1, on the lead's word. Under either answer, the ERCOT sentence changes as part 3 says.
8. **The booking** (F-4; `6-cost.md`, part 6). For the lead, after steps 1-6: the tier-3 PR, with F-4's additions and the two open items the lead already holds (the transition share after FY2039; the builders' borrowing). **Who:** the lead's booking, with Espen's label.
9. **A short L3 re-check** by the standing reviewer, limited to B-1, B-2, O-1 and the booking's rerun. Then the lead moves the decided items to L3 in `agenda/agenda.csv` and the README.

## Checks run

A Standard (Sonnet) subagent ran these at `d1ec067`. The reviewer re-checked the plan-wide gap at the head, the tool's hard-coded gap and the transition share before using them.

- **The path.** `tools/clean_power_path.py` and `tools/coverage_read.py` run, and reproduce every cell of `6-cost.md` part 1 within 0.1: $1,852.4 and $147.4 billion; +$41.6 and −$17.5 billion; memo 1 B −$30.7 and −$29.1 billion; memo 7 B $12.2 and $1.7 billion; the dividend $133, $439 and $492; the shares 68.5%, 64.5%, 59.3% and 58.1%; $1,263.7 of $1,996.0 billion; $1,202.7, $962.2 and $240.5 billion on the booked $1,898.9 billion. The transition share in FY2040 is $33.1 billion, not "about $32 billion" (F-2). `tools/build_provisions.py --check` passes.
- **The booked basis.** $1,810.8 and $164.9 billion reproduce from `legacy/sources/recovery-budget-audit.csv` (case `mixed`, sixteen lines). The climate rows are byte-identical at `6204281` and the head. The group subtotals match section 6; section 3 rounds two FY2040 subtotals differently (C-1).
- **The plan-wide gap.** `agenda_gf_primary_bn`, case `mixed`, FY2040, is $4,245.4 billion (7.84% of GDP) at the head, against the $4,256.6 billion `6-cost.md:126` and the tool use (F-1).
- **Input trace.** Memo 7 B's inputs are cited or labeled judgment in part 1's table, except four unlabeled in the tool (W-1). Memo 4 B rests on EV-CLP-717 (grade D) and a judgment year shape. Memo 5 B's tripling and 2.2% growth are unlabeled (O-2).
- **IDs.** All 344 EV-CLP IDs cited exist in `evidence.json` (375 entries). Every SRC behind them is in `library/catalog.csv`. All 15 DEC IDs cited exist. The 53 provisions in `provisions.json` and section 4 match in both directions. FAM-1.07, 1.09 and 1.10 are the secure floor's. 31 register entries are cited nowhere (W-2).
- **Registry.** `models/registry/check.py` passes, with 43 EV-CLP warnings on 40 entries (W-2).
- **The agenda.** 76 rows are homed here. All 36 decided rows are L2 `decided` citing `-06` or `-07` correctly. CLI-13's parent row is the one inconsistency (C-4).
- **Stale figures.** "+$0.11 trillion", "$156 billion" and "3.7%" remain only as section 3's labeled first estimate. "$4,256.6" and "`6204281` as head" are stale (F-1). No "proposed" status remains.
- **Section 9.** Every number traces, except the items in E-2.
- **Checks.** `bash .github/scripts/run-checks.sh` on this branch passes ("All checks passed"; 77 tests in the last suite).
