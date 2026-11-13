# A new consensus on immigration: L2/L3 milestone review

Role: the independent milestone review of the immigration dossier (flagship 6; `charter/PLAN.md` 3.2 and 5, "Review"; `charter/STANDARDS.md`, "Milestone review"), board "Next" step 3. The reviewer wrote none of the dossier. It tries to break the work on four fronts: weak evidence, missing populations, optimistic assumptions and cheaper alternatives. It also:
- applies the design lens (`DEC-2026-11-09-13`);
- checks the fiscal-rule report against `DEC-2026-11-10-05`;
- checks every decided item against `DEC-2026-11-12-07` and `-12`;
- checks section 9 against sections 1-8;
- reproduces section 6 from the tools.

Status: current, as of main at commit `4b9ca52` (November 12, 2026, after #299). Outcome on main: the verdicts below are the review's at that commit (#303); its fix steps (#305, #307) closed the blockers, Espen's answers to its questions are `DEC-2026-11-12-17` to `-19`, and the booking (#310) was also the L3 re-check: IMM-1 to IMM-6 are at L3 in `agenda/agenda.csv`, the alternatives at L2. Reviewer: Claude Code, `session_01UQzgBtaHE8nkT9Znw8gZVp`. It changes nothing in the dossier. Every fix below is a later step: the fix steps go to a fresh Most capable session, or to this reviewer if the lead asks, and the booking goes to the lead.

Espen's decisions (`DEC-2026-11-12-07`, `-12`) are settled. Where a decided choice has a cost or gap the dossier does not show, this review says so and sends it to Espen as a question; it does not argue the choice. Under `DEC-2026-11-10-07`, a clearly bounded uncertainty is not a defect. Espen noted on November 12 that the court plan will likely shift again once democratic renewal's judicial branch plan is done. This review treats that as expected, not as a defect (C-3 asks only that sections 7-8 say so).

## Verdicts

| Level | What it needs (`charter/PLAN.md` 3.2) | Verdict |
| --- | --- | --- |
| **L2, design** | Key parameters chosen (who, what, how much, who administers), with the main alternatives weighed | **Pass** (record fixes only, none blocking) |
| **L3, specified** | Provisions section by section (eligibility, benefit, administration, phase-in, remedies); evidence for each load-bearing claim; a cost range validated by models with stated limits; a delivery plan | **Not yet: close.** Two blockers, both in eligibility law |

**Why L2 passes.** Memos 1-7 weigh two to four options at each of twelve forks. They use outside scores (CBO 2013, 2021 and 2024; JCT; SSA's actuaries; BPC; Penn Wharton) and bill comparisons, and they treat the legacy designs as options. Every fork is decided and recorded (`DEC-2026-11-12-07`, `-12`). Every memo's status line says so, and `agenda/agenda.csv` holds IMM-1 to IMM-6 at L2 `decided`, with the alternatives at L2 `alternative`.

**Why L3 is not yet.** Most of L3 is in place:
- section 4 specifies 85 provisions with parameters, vehicle, agency and evidence, plus a vehicle table, a groups table, a burden table and a consistency table;
- section 5 has a timeline, remedies, states' roles and a rural plan;
- section 6 reproduces exactly from its tools (see "Checks run");
- sections 7 and 8 give benchmarks, objections, triggers and hard stops.

The blockers:
1. **The inadmissibility grounds and old removal orders are not waived** (M-1). Point 2 decided "no bar for immigration-only offenses". IMM-1.08 writes that only for the crimes of unlawful entry and reentry (8 U.S.C. 1325, 1326). The grounds that actually stop long-settled people from getting a green card are left standing:
   - unlawful presence and reentry after it (8 U.S.C. 1182(a)(9)(B), (C));
   - prior removal (1182(a)(9)(A));
   - entry without inspection (1182(a)(6)(A));
   - false claims to citizenship, often made on an I-9 (1182(a)(6)(C)(ii), with no waiver);
   - reinstatement of a prior order, which bars "any relief" (8 U.S.C. 1231(a)(5)).

   Final removal orders are not addressed either. EOIR's non-detained docket held 1.6 million people with final orders in February 2026 [EV-IMM-170] (`1-problem.md:213`). That is a decision-changing omission for the decided promise of "registration ... and protection for everyone present before the cutoff".
2. **Nothing protects eligible people between signature and filing** (B-1). Registration's cutoff is the signature date, but protection from removal starts only "from the day of filing" (IMM-1.10). Filing opens up to 270 days later (IMM-1.05). In that window an eligible person can be arrested outside the priorities with a written reason (IMM-4.03) and removed, and nothing in the act stops it. The same is true for anyone who files late. That is a missing delivery mechanism.

**What can reach L3 once those land.** Every provision can. The open items are bounded working assumptions or other owners' decisions:
- memo 1's status cost (−$50 to +$150 billion);
- memo 6's per-person health cost (O-1);
- case management's population (O-2);
- the E-Verify pool;
- the judge count, which is democratic renewal's;
- SSA's score (point 13).

## How this review was done

- **Read.**
  - The charter: the standards, the board, `DEC-2026-11-09-13`, `-10-05`, `-10-07`, `-12-07`, `-12-08` and `-12-12`.
  - The secure floor's review (#298) as the model.
  - Sections 3-9, `README.md` and `provisions.json` in full; memos 1-7 where sections 4-9 draw on them, and their status lines; sections 1-2 and `legacy-research.md` by search.
  - Both tools and the test.
  - Care's `6-cost.md` part 1 and `models/tools/health-coverage/` (the residual), and `legacy/domains/domain-courts.md`, CRT-5.
- **Mechanical checks.** A Standard subagent ran them. The reviewer spot-checked its readings against the files before using them (see "Checks run").
- **The reviewer's own arithmetic** (not model runs):
  - care's cost per newly covered person (O-1);
  - case management against today's alternatives (O-2);
  - the judge corps against the post-clearance need (A-1);
  - CRT-5 without the judge teams and counsel (F-2);
  - the booking rows against the counting rule (F-1).
- **No new research thread was opened.** The legal grounds in M-1 are cited from the statute, without new register entries; the fix step adds them.

## 1. The decisions, carried out

Each decided item checked against section 4, `provisions.json`, sections 5-6 and the memos:

| Decision | Where | Verdict |
| --- | --- | --- |
| Memo 1 A: tiers, the three changes, a green card on approval, TPS/DACA/parole in tier A (`-07`) | IMM-1.01 to 1.14 | Faithful, except that point 2's intent is not carried into the inadmissibility grounds (M-1), and protection runs only from filing (B-1) |
| Cutoffs: tier A on January 1 of the year of enactment; registration on signature day; tier B unchanged (`-12`) | IMM-1.01, 1.03, 1.04 | Faithful. IMM-2.08 and IMM-4.03 cite "the cutoff" without saying which (C-1). Section 8 misstates the cutoff's effect in a debate-year surge (E-1) |
| Memo 2 C: records first, rolling registry, no penalty, no fee below 200%, work permit on filing, no closing window | IMM-1.05 to 1.10, 6.06 | Faithful. Tier A's work-history test has no records-first rule (L-1) |
| Memo 3 part 1 B and part 2 B | IMM-2.01 to 2.12 | Faithful |
| Memo 4 part 1 D; part 2 yes, counsel B | IMM-3.01 to 3.12 | Faithful. The judge corps is now priced here (F-2, A-1) |
| Point 7 changed: wall money redirected | IMM-3.07 | Faithful |
| Memo 5 part 1 B with A's rules (replace ICE, no name, rules in statute, 30,000 cap, case management default) | IMM-4.01 to 4.11 | Faithful |
| Memo 5 part 2 A with B's enforcement, and the start rule (`-12`): no earlier than October 1 of the year after enactment; IG conditions (a)-(e); 90-day repeats; later tranches a year apart with a 1% wait; no exemption or appeal | IMM-4.12 to 4.18 | Faithful in substance. Condition (e)'s benchmark is ambiguous, and IMM-4.18's GAO audit reads as an extra gate (L-4). Stale "at least a year" text remains (C-2) |
| Memo 6 C, the one table | IMM-1.20 to 1.36 | Faithful. The coverage cost is counted once (F-3, open item 2) |
| Memo 7 parts 1-3 B | IMM-5.04, 6.01 to 6.07; the vehicle table | Faithful |
| Points 2-6, 8-14 yes | Throughout | Faithful (point 2: see M-1) |

## 2. Findings

IDs:
- B: blocking delivery gap;
- O: optimistic assumptions;
- M: missing populations;
- A: cheaper alternatives;
- F: fiscal report and the money;
- W: weak evidence;
- L: design lens;
- E: section 9 against sections 1-8;
- C: consistency and record.

**Blocking** means blocking L3. Line numbers are at `4b9ca52`.

### B. Delivery

**B-1. No protection from removal between the cutoff and filing. Blocking.**
- **What section 4 says.** Registered status reaches anyone "present on the day the act is signed" (IMM-1.03, `4-specification.md:56`). Protection starts "from the day of filing" (IMM-1.10, `:63`). Filing opens "no later than 270 days after the act's signature" (IMM-1.05, `:58`). The priorities bind from signature, but an arrest outside them needs only "a written reason, reviewed by a supervisor" (IMM-4.03, `:143`). `grep` finds no stay of removal for people who appear eligible before they file.
- **The scenario.** The act is signed in December 2029. In March 2030, ICE (still in place until October 2031) arrests a woman with 11 years here at a traffic stop. It gives a written reason, and with an old final order she is removed in days. She was eligible for tier B, but filing has not opened. Once removed she is no longer "present", so no route reaches her. The same happens to anyone who has not yet filed in 2031-32, when the notices go first and others wait their turn (`5-delivery.md:29-32`).
- **Why blocking.** The decided promise is protection for everyone present before the cutoff (`DEC-2026-11-12-07`, memo 1 change 2). The window is the period of greatest risk, and a removal in it cannot be undone. Under `DEC-2026-11-10-07` this is a missing delivery mechanism.
- **The fix.** Add to IMM-1.10 or a new IMM-1.15:
  - from signature, a person who appears eligible for tier A, tier B or registration may not be removed, and is released from detention unless within IMM-4.03's security or public-safety priorities, until a decision on a filing made while filing has been open, or a set period after it opens (working choice: one year);
  - an officer or judge who meets such a person gives them a chance to show eligibility, and removal proceedings pause;
  - S. 744 (2013) and the U.S. Citizenship Act (2021) each carried such a rule; the fix step should cite one of them with a register entry.

  No new decision is needed: this carries out memo 1 change 2 and point 3.

### M. Missing populations

**M-1. The inadmissibility grounds, reinstated orders and final orders. Blocking.**
- **What section 4 says.** IMM-1.08 keeps 1259's existing grounds, "with no bar for immigration-only offenses (unlawful entry and reentry, 8 U.S.C. 1325 and 1326, and status violations)" (`4-specification.md:61`). IMM-1.10 closes *pending* removal cases on filing (`:63`).
- **What stays in the way.**
  - Tier A and registered status are new statuses the act defines. Unless the act says otherwise, an applicant for permanent residence must be admissible.
  - The grounds that fall on long-settled people without status are 1182(a)(6)(A) (entry without inspection), (a)(9)(B) and (C) (unlawful presence, and reentry after it, a ten-year or permanent bar), (a)(9)(A) (prior removal), (a)(7) (no valid documents) and (a)(6)(C)(ii) (a false claim to citizenship, a permanent bar with no waiver, often incurred by checking "citizen" on an I-9 to get work). Reinstatement under 8 U.S.C. 1231(a)(5) makes a person who reentered after removal ineligible for "any relief".
  - The registry route is narrower (1259 lists only some grounds), but 1231(a)(5) and good moral character still reach it.
  - Final orders are not mentioned: 1.6 million people on the non-detained docket had one in February 2026 [EV-IMM-170]. Many are in absentia orders, 15% of which were later overturned in 2008-18 [EV-IMM-316]. Memo 5's own story has a mother with a final order (`memos/5-enforcement.md:39`).
- **Why blocking.** These grounds, not the crimes of 1325 and 1326, are what bar most long-settled people today. Left in place, they would exclude a large share of the population memo 1 is designed for: the reinstated, the previously removed, and workers who made a false claim on an I-9. Who is eligible is an L3 element.
- **The fix.**
  - In IMM-1.08, for tier A, tier B and registration: (a)(5), (a)(6)(A), (a)(7) and (a)(9)(B) do not apply; (a)(6)(B), (a)(6)(C), (a)(9)(A) and (a)(9)(C) are waivable for family unity, humanitarian reasons or the public interest. The waiver for a false claim to citizenship is made by an employment attestation.
  - 1231(a)(5) does not bar any route.
  - A final order does not bar a filing. On approval the order is vacated, and a filing stays its execution (with B-1).
  - The fix step should take the list from S. 744's sec. 2101 (new INA 245B(b)) or the U.S. Citizenship Act's tier text, with a register entry, and check it line by line against the statute.
  - This carries out point 2 as decided ("no bar for immigration-only offenses"), so it needs no new decision.
  - Section 6: no cost change (the population counts already assume these people are in).

**M-2. Long-settled residents removed or driven out in 2025-28. Not blocking; a fork for Espen.** Section 1 records the 2025-26 enforcement surge, but no file places people who lived here for years and were removed, or left, before the act. Every route requires presence on a date in the year of enactment. The U.S. Citizenship Act let some people deported after January 2017, with at least three years' prior presence, apply from abroad for family unity. Reaching them is a new group, so it is a fork for Espen, not a fix. Put it as a yes-or-no point (question 1 below), with the count from DHS's removal statistics (the fix step adds an entry) and a cost (mostly USCIS and State work, small on the general fund; reviewer's judgment). Or record it in section 8 as left open, with the alternatives.

**M-3. Smaller placements. Not blocking.** One sentence each:
- *People detained when they file:* released unless a priority (with B-1).
- *Asylum applicants who register:* closing the removal case on filing (IMM-1.10) should be at the applicant's election, because an asylum grant brings derivative status for a spouse and children abroad that registration does not.
- *The territories:* the routes apply in Puerto Rico, Guam, the U.S. Virgin Islands and the Northern Mariana Islands as part of the INA's "United States". The Northern Marianas' CW-1 workers and long-term residents need a line. American Samoa runs its own entry controls.
- *Border tribes:* IMM-3.07 consults them on wall projects. The Tohono O'odham and others also need the protected-places and identification rules applied on tribal land, which the act can state in a line.

### O. Optimistic assumptions

**O-1. Health coverage for people without status at $3,000-5,000 a person. Not blocking; bounded, but it needs a basis.**
- Memo 6's $3-9 billion a year covers 1.5-3 million people "at about $3,000-5,000 a person, well below the average of $15,474 ... for a younger, working population (judgment)" (`memos/6-eligibility-table.md:41`; `6-cost.md:154`). No register entry supports the ratio.
- Care's own model prices the newly covered at $456 billion for about 33.6 million people in 2032, about $13,600 a person (`dossiers/care/6-cost.md:31`; `tools/health_path.py:114`, the uninsured less the 1% residual). The $3,000-5,000 is a quarter to a third of that. A younger population costs less, but a plan with low cost sharing raises use.
- At half care's figure (about $6,800), the line would be about $10-20 billion a year, not $3-9 billion, adding about $40-60 billion to memo 6 over FY2030-39. That is inside the total's range but above memo 6's own.
- **Fix.** Price the group in care's model rather than by judgment (F-3's fix): lower `sp_residual_unins` by memo 6's count and take the difference as immigration's line. Any age adjustment then comes from the model's cells, not a guess. Otherwise add a register source for the ratio (published studies of unauthorized immigrants' health spending against U.S.-born adults') and widen the range. It informs the booking. It does not block the decision, which is made.

**O-2. Case management for about 100,000 people. Not blocking; label it.**
- `cm_people_k` is 100,000 (70,000-140,000), "assumption: memo 5" (`tools/immigration_model.py:88`; `6-cost.md:56`; `5-delivery.md:48`).
- Today 183,181 people are on alternatives to detention [EV-IMM-171]. The cap releases about 35,000 more of the 65,765 held then.
- After the act, many of today's participants register and leave proceedings (IMM-1.10), so a lower number is defensible. But the dossier does not say so, and the surge rule releases arrivals "to case management" (IMM-3.02) with no count.
- At 200,000 the detention line is about +$10 billion over FY2030-39, not +$1.1 billion (reviewer's arithmetic: 100,000 more at about $26 a day net, grown).
- **Fix.** Give the basis: today's 183,181, less those who register, plus surge releases. Widen the high end to about 250,000, and say the detention line's sign turns on it. Section 9's "about +$1 billion" follows.

**O-3. Children's counsel counts only new cases. Not blocking.**
- Counsel B covers every child in removal proceedings. The model prices 40,000 child cases a year (`children_cases_k`, an unsourced assumption).
- The 3.3 million backlog the corps clears by FY2035 includes children's cases that will also need counsel, and they are not counted.
- At a few hundred thousand pending child cases and $5,000 each, that is roughly $1-2 billion more (judgment).
- **Fix.** Add the backlog's child cases from EOIR or TRAC counts, with an entry, and source the unit costs. Section 4's "Evidence still needed" already names the counsel study.

**O-4. USCIS's six-month target is not funded through the backlog. Not blocking; price it.** Section 5 finds that 1.4 million cases remain when the backlog money ends, "so the six-month target (IMM-6.03) needs the money for about a year longer or a faster unit cost" (`5-delivery.md:27`). Section 6 does not add that year. Add about $0.7-1.0 billion (one more year at EV-IMM-575's pace) to memo 7's line, or state in sections 6 and 8 that the statutory target slips by about a year.

### A. Cheaper alternatives

The memos weighed the large cheaper designs (memo 1 B and C, memo 6 B), and Espen chose. One remains:

**A-1. A term-limited increment for the judge corps. Not blocking; for democratic renewal, with the cost shown here.**
- The model hires to about 1,673 judges by FY2033. After the backlog clears in FY2035, it lets the corps shrink only by attrition: 1,579 in FY2036 and 1,254 in FY2040 (`immigration_model.py` output).
- The steady-state need after clearance is about receipts after legalization over completions a judge: about 529,000 × 0.7 / 510, or about 730 judges. That is at or below today's 753.
- So the corps carries roughly 500-830 surplus judge teams in FY2036-40: about $5 billion over FY2036-39, and the $1.1 billion in the FY2040 "permanent" line (reviewer's arithmetic).
- Hiring the increment as temporary judges on terms tied to the backlog (EOIR already uses them [EV-IMM-103]), or planning a return to the steady-state corps, would save that with no loss to anyone.
- It touches IMM-3.11's independence and CRT-5's tenure, which are democratic renewal's. Show it in section 6 as an alternative with its saving, and send it with the court requirements. The FY2040 permanent cost should say that its judge line is a surplus, not a need.

### F. The fiscal-rule report (`DEC-2026-11-10-05`) and the money

**The report itself follows `DEC-2026-11-10-05`.** Section 6, part 5 gives:
- the yearly cost;
- the permanent cost from FY2040 ($16.4 billion, 0.03% of GDP);
- the net change a booking would make (+$272.8 billion over FY2030-39, +$35.1 billion in FY2040; +$232.8 billion with CAP-7S corrected);
- the share of the plan-wide margin (0.84% of the gap; 0.39% for the whole set).

It is on one basis against the booked case `mixed`, and the gap it uses, $4,184.7 billion (7.73% of GDP), is the head's figure (`DEC-2026-11-12-08`). Social Security's funds are reported apart. It sends nothing to Espen on money, which is right: memo 6 B and memo 1 B carried the money choices, and Espen decided them.

**F-1. E-Verify's revenue is folded into a spending row in the booking list. Not blocking; a record fix.**
- The counting rule keeps spending and revenue effects apart (`6-cost.md:14`). Part 1 does: the H-1B offset and E-Verify's on-budget revenue are their own lines.
- Part 6's booking rows do not. IMM-4's row (−0.033 / −0.016 / +0.021, `6-cost.md:137`) is memo 5's spending (+$7.9 billion) plus E-Verify's −$23.3 billion of revenue, which makes an enforcement row a net saving. IF1's offset gets its own line (item 3) while E-Verify's does not.
- **Fix.** IMM-4 at +0.001 / +0.008 / +0.021 (spending only), and a revenue row for E-Verify's on-budget effect (−0.035 / −0.023 / 0.0) with its JCT-convention note. The low end is −0.034 on the tool's rounded values (the subagent's check), so restate it.

**F-2. CRT-5's re-score must drop counsel as well as the judge teams (open item 3). Not blocking; for democratic renewal and the booking.**
- The legacy CRT-5 figure is "about $0.03T, range $0.02T to $0.06T ... A court of this size with appointed counsel for two populations" (`legacy/domains/domain-courts.md`, CRT-5, "Cost"). So it holds both the corps and counsel.
- IMM-3 now carries both: the judge teams ($13.2 billion, IMM-3.08) and counsel for children, people with serious mental illness and everyone detained ($8.0 billion, IMM-3.12, inside memo 4's $26.0 billion). Section 6 names only the judge teams (`6-cost.md:85`).
- Re-scored without either, CRT-5 is the court's structure:
  - setup and the new appellate and administrative divisions beyond the Board of Immigration Appeals;
  - restored Article III review and its added federal-court caseload;
  - A-file access and bond hearings.

  EOIR's existing budget (about $1 billion a year) moves with the court and is not new cost. On that basis CRT-5 is on the order of **$0.003-0.01 trillion** over FY2030-39 (reviewer's judgment), not $0.03 trillion.
- Nothing is double counted today, because CRT-5 is in no total (ledger, "Not in any total"). The risk comes when democratic renewal books it.
- **Fix.** `6-cost.md:84-85`, part 6 item 5 and section 7 part 2 name counsel too, and carry the reviewer's placeholder for CRT-5 without the judges and counsel. Section 8's left-open row says the court plan will move with democratic renewal's judicial branch plan (C-3). The lead updates `ledger-conflicts.csv:28`'s note when booking.

**F-3. The newly legalized people's health coverage is counted once (open item 2). Confirmed, with one condition for the booking.**
- *Care's base.* Care's model covers the whole Social Security area population (355.2 million [EV-CAR-051]) except a residual of 1% (`sp_residual_unins`, about 3.55 million), described as people "not yet enrolled or not covered because of immigration status" (`models/tools/health-coverage/inputs.csv:182`). The booked health rows (#230, #237, #279) use that 1%. Care's own file leaves covering people without status "not priced" (`dossiers/care/6-cost.md:89`).
- *The newly legalized.* They are in care's covered base, not its residual. Memo 1's line removes CBO's health share for the years after January 2031 (`immigration_model.status_fiscal`: 0.6 × 0.9 of the window; `6-cost.md:92`). Before 2031 their Medicaid and credits stay in memo 1's line. **Counted once.**
- *People still without status.* Memo 6's 1.5-3 million sit inside care's 3.55 million residual, and memo 6 prices them (`6-cost.md:31`). Care does not. **Counted once.**
- *The condition.* The booking must not both add memo 6's coverage line and lower care's residual. The cleaner fix, which also answers O-1, is the reverse: lower `sp_residual_unins` by memo 6's count in the care path, take the cost difference as immigration's coverage line, and record in care's `6-cost.md:89` that it is priced there. Either way one note in each file says where it is counted. Change `6-cost.md:92`'s "(to confirm)" to "confirmed at the milestone review".
- *The remaining uninsured.* About 0.5-2 million stay uninsured for other reasons. Sections 7 and 9 do not claim otherwise; keep it that way.

**F-4. Smaller money points. Not blocking.**
- `6-cost.md:99` says memo 2's form is "about +$4.5 billion"; the table and tool give $5.4 billion.
- `:119`'s yearly path ("$3 billion ... $13 billion by FY2032 and $15 billion by FY2039") should read about $4 billion, $14.5 billion and $16 billion (table row `:37`).
- `:70`'s "0.2, 0.45, 0.7, then full" are tranche levels. The yearly shares are 0.05, 0.26, 0.51 and 0.78, then 1.0; say so.
- `:45`'s $19.3 billion is $19.2 billion on the tool.
- `:31` should read IMM-1.20-1.36.
- The booked basis is cited at `7512852` (`:15`, `:106`); the IMM-1 audit lines are unchanged at the head, so cite `DEC-2026-11-12-08` instead.
- E-Verify's start-date sensitivity (`:158`, ±$4 billion and ±$7 billion) is not a tool run; run it, or label it judgment.

### W. Weak evidence

**W-1. Load-bearing judgment lines.** The three largest uncertain lines rest on judgment:
- memo 1's status cost, H.R. 6 scaled (the range covers it);
- memo 6's per-person cost (O-1);
- memo 3's −$40 billion, $10,000 per added person on CBO's 2024 surge [EV-IMM-220], which is uncorroborated in the register.

Each is labeled. The fix step should add one independent check for memo 3, such as Penn Wharton's or the Bipartisan Policy Center's per-immigrant fiscal estimates, or widen its range.

*Resolved* (`6-cost.md`, part 7, "Independent checks"): memo 3 holds on Penn Wharton's score [EV-IMM-660]; memo 6's per-person factor is qualified by KFF and Kaushal and Muchomba [EV-IMM-661] [EV-IMM-662], which put the central factor at the top of the supported range and would lower the memo 6 line by about $26 billion over FY2030-39 at KFF's ratio (booking unchanged, reported for the lead); memo 1 holds in sign on BPC's reading [EV-IMM-663], its size staying judgment.

**W-2. E-Verify's error rates are from FY2009** [EV-IMM-391]. They carry condition (e)'s context, the burden table and section 9. They are named in "Evidence still needed". Bounded, because condition (e) measures the rate at the time; see L-4.

**W-3. Search-extract quotations.** Section 3 asks the reviewer to spot-check EV-IMM-608 and 610-621 (`3-design.md:249`). Not done here (usage is tight). The fix step's Standard subagent should check them against the originals. None of them carries a section 9 figure except through EV-IMM-613 (Cato's 370,000-1.2 million wrongly flagged), which section 4 uses only in the burden table.

*Resolved* (November 13): all 13 quotations and figures match their originals. Two catalog dates were wrong or loose and are fixed (Cato's Policy Analysis No. 775 is dated July 7, 2015; MPI's page shows December 2020 beside a bullet that says "as of 2021", noted in the entries). Each entry's `checked` date and context records the check.

**W-4. The 30,000 cap's basis is a grade D legacy entry** [EV-IMM-571]. That is fine for a decided parameter; it is a commitment, not a claim.

### L. Design lens (`DEC-2026-11-09-13`)

The design is strong on the lens:
- records first, with a sworn statement only for gaps (IMM-1.06);
- people USCIS knows start on a notice (IMM-1.07);
- no penalty, and no fee below 200% of poverty, claimed on the form (IMM-1.09);
- a work permit as the filing receipt (IMM-1.10);
- numbers issued without a visit (IMM-1.12);
- residence, not status, in the universal programs;
- one firewall;
- E-Verify on new hires only, free, with a default to confirmation and lost wages paid;
- officers' written reasons rather than people's papers.

The burden table (`4-specification.md:233-248`) covers twelve requirements. Its closing claim, that "nothing else in the act adds a document, a fee, a test or a periodic report for people" (`:248`), does not hold for four:

**L-1. Tier A's work-history test has no records-first rule. Not blocking.** Group 3 needs 1,035 hours or 180 days of farm, care or construction work in two years (IMM-1.01, `:54`). Care and construction work for households is often paid in cash, with no W-2. IMM-1.06's records-first rule covers residence, not work. Fix: the same rule for work history (records, then a sworn statement plus one document, an employer's or co-worker's statement counting as one), as the farmworker bill's evidence rule does. Add a burden-table row.

**L-2. Registered status renews every five years. Not blocking; a working choice to change.** IMM-1.03 gives five years "at a time (working choice)", renewed free below 200% (`:56`). That is a periodic filing for 2-4 million people, most of whom will reach the registry at ten years anyway. Fix: valid until the person reaches ten years and the registry (with biometrics refreshed from records), or renewed automatically from records. Either way, add a row. It costs USCIS less.

**L-3. Two tests the table leaves out.**
- Tier B's absence rule (180 days in one trip, 365 in all; IMM-1.02, `:55`).
- The five-year wait for registered adults in SNAP, SSI and TANF (IMM-1.27, `:84`, a working choice). The wait falls on the poorest registered adults; give its saving beside its burden.

Each needs a row.

**L-4. Two E-Verify details against `DEC-2026-11-12-12`. Not blocking.**
- Condition (e) reads "no higher than permanent residents' (0.7% in FY2009 [EV-IMM-391])" (`:158`). Espen's test compares newly registered workers with permanent residents. It should name the permanent residents' rate measured in the same published test, with FY2009's 0.7% as context only, so an out-of-date benchmark does not make the test easier than decided.
- IMM-4.18's "A GAO audit before each tranche" (`:163`) and section 5's "each after a published error count and a GAO audit" (`5-delivery.md:83`) read as a gate that Espen did not set ("No separate employer exemption or appeal process"; the 1% wait is the only condition on later tranches). Say the audit is published before each tranche and does not delay it.

### E. Section 9 against sections 1-8

Every number in section 9 traces to sections 1-8 (the subagent's trace is under "Checks run"). "On our estimates" is used where it should be, the cost is stated plainly, and the can't-say list refuses "pays for itself". Points:

**E-1. The debate year's arrivals can register. Not blocking.**
- Section 8 says "the cutoff is the signature date, so a surge changes no eligibility" (`8-change-our-minds.md:40`). That is wrong under `DEC-2026-11-12-12`: anyone who arrives before signature, a surge during the debate included, can register (IMM-1.03, 1.04). Only tier A is closed.
- Section 7's "the cutoff allows no arrival after the law is known" (`7-validation.md:77`) and section 9's answer (`9-public-case.md:62`) are accurate only for arrivals after signature.
- **Fix.** Section 8: "A surge before signature can reach registered status, not tier A; the surge rule answers the flow." Sections 7 and 9 say the same in a clause.
- The cost of the decision goes to Espen as question 2.

**E-2. Social Security. Not blocking.** "Social Security's funds gain from legalization" (`9-public-case.md:44`, and `:63`) omits E-Verify's loss to the funds, about −$42 billion over FY2030-39 (`6-cost.md:72`), and the gain for this design is not quantified. Fix: "Social Security's funds gained from legalization in the 2013 Senate bill's score; the E-Verify mandate costs them about $42 billion over ten years on our estimates."

*Resolved* before this step: `9-public-case.md:46` already carries that clause (and the case's own source table lists the $42 billion); no further edit.

**E-3. Smaller points.**
- "5.3 million citizen children have a parent who would gain status" (`:55`): should be "could", since about 30% may not file and some are barred.
- The GAO's 99% (`:35`) is for "the full-service component ... with a scheduled hearing" [EV-IMM-354]; carry that, as section 7 does.
- "Without a warrant" (`:36`) should add "or an emergency" (IMM-4.07).
- "Against CBO's baseline it is about zero" for detention (`:84`) is a section 3 carry-over; use section 6's figure, revised for O-2.
- "About 900 more immigration judges" (`:29`) should add "a number to be set with the court plan" (C-3).

### C. Consistency and record

- **C-1. Which cutoff (open item 1).**
  - **IMM-2.08** (`4-specification.md:108`) should mean tier A's cutoff. Certified agricultural worker status serves farmworkers present on the signature date who arrived after January 1 of the year of enactment, and so missed tier A, on the bill's hours test. A farmworker who arrives after signature comes through the H-2A reform, not certified status; otherwise the provision opens a route after the law is known, against IMM-1.04. Write "present on the day the act is signed (registration's cutoff) and not in tier A (after its January 1 cutoff)".
  - **IMM-4.03** (`:143`) should mean registration's cutoff, the signature date. A person who arrived between January 1 and signature holds or can claim registered status, so making them a priority contradicts IMM-1.03. Write "after the day the act is signed (registration's cutoff), and within the last two years".
  - Change both in `provisions.json` too.
- **C-2. Stale E-Verify text.** `README.md:3` ("phased in at least a year after the status programs run"), `3-design.md:58` (the decided row) and the Espen quotation at `4-specification.md:135` ("wait at least a year") predate `DEC-2026-11-12-12`. Mark each "amended by `DEC-2026-11-12-12`". `provisions.json`'s IMM-1.01 status string should name `-12`, as its `decisions` array does.
- **C-3. The court plan will shift (Espen, November 12).** Sections 7 and 8 name democratic renewal only for the judge count and CRT-5's score (`7-validation.md:32`, `8-change-our-minds.md:49`). Add a line to section 8's "Left open" and to section 7 part 2: the court requirements (IMM-3.08-3.12), the corps and its cost are expected to change once democratic renewal's judicial branch plan is done, and this dossier's figures stand until then. This is a record of an expected change, not a defect.
- **C-4. Other stale lines.**
  - `memos/4-asylum-courts.md:57` keeps "about 1,000-1,200 judges" as decided text; add the model's 1,670 beside it, as the secure floor did for its memo 6.
  - `1-problem.md:280` still has the child-ID rule "awaiting Espen" (decided, `DEC-2026-11-12-06`).
  - "Pending Espen" for the $6 billion reserve (`README.md:18`, `:110`; `1-problem.md:323`; `legacy-research.md:34`, `:73`, `:171`) is answered by point 9; legacy quotes can stay, with a note.
  - The order of section 5's timeline rows (`5-delivery.md:79-80`) puts January 2031 before October 2030.
  - IMM-3.08's parenthesis "at the slow end of completions a judge even 250 hires a year clear" (`:127`, also `7-validation.md:32`) is garbled.
- **C-5. Evidence records.** 64 entries' `supports` point to `2-options.md`, which does not exist (the file is `2-what-works.md`), and the registry checker does not catch it. 22 entries are cited nowhere (EV-IMM-015, 025, 038, 061, 108, 115, 143, 147, 168, 206, 306, 309, 311, 320, 352, 396, 607, 620, 625, 630, 631, 632); cite or drop them.

  *Resolved* (November 13): the `supports` paths were repointed in fix steps 1-4 and all now resolve. Of the 22 uncited entries, EV-IMM-015 was already cited; 14 are now cited where they support a claim (EV-IMM-025, 038, 108, 143, 168, 206, 306, 352, 396, 620, 625, 630, 631, 632) and 7 are marked "Not relied on" in their context with the reason (EV-IMM-061, 115, 147, 309, 311, 320, 607). Nothing is deleted.
- **C-6. The tools are outside CI.** `test_immigration_model.py` (8 tests, passing) is not run by `run-checks.sh`, so the model can drift from section 6 unseen. Add it to the check script (a `.github/` change, tier 3, for the lead), or move it with the model to `models/` at stage H.
- **C-7. Section status lines.** Sections 4-9 read "draft (stage E, board row I4, PR 1/2)". After this review they should read "reviewed (L2); L3 after the fix steps", and the README likewise. The board's immigration row says L1, and the agenda says L2; the lead fixes the board.

### Seams with other dossiers

- **Secure floor.** IMM-1.25 matches FAM-1.04; SNAP's rule is counted once in INC-2.01; IMM-1.12's numbers bring legalized parents into the earned income credit. Consistent with the secure floor's review.
- **Care.** F-3 (counted once, with the booking condition). Care's `6-cost.md:89` row needs the cross-reference. The care workforce asks are answered.
- **Housing.** Its open items are answered in IMM-1.30 to 1.35.
- **Democratic renewal.** F-2 and A-1, with C-3's expected shift; IMM-5.05 is proposed.
- **Work.** IMM-4.16 and 4.17 are proposed.

## For Espen

Two questions, each about a cost or gap. Neither reopens a decision.
1. **People removed or driven out in 2025-28** (M-2). "The plan's status routes reach only people here in the year the law passes. Should long-settled residents removed or pushed out in 2025-28 (for example, here three years or more before removal, with a citizen or resident spouse, parent or child) be able to apply from abroad, as the U.S. Citizenship Act proposed? Yes / no / leave open." The reviewer recommends yes, limited to family unity. The cost is mostly agency work and is small on the general fund (to be priced).
2. **Arrivals during the debate year** (E-1). "Because registration's cutoff is the signing day, people who arrive while Congress debates the bill can register (a work permit and protection, a green card at ten years), though not get the fastest green card. Opponents will call that a magnet. Keep it as decided, stated plainly, with the surge rule as the answer? Or move registration's cutoff to the day the bill is introduced or passes its first chamber?" The reviewer recommends keeping it as decided and saying so.

## What the next steps should do

For a fresh Most capable fix session started by the lead, or this reviewer if the lead asks, unless marked for the lead. In order: step 1 clears the blockers, and steps 4-5 follow it.

1. **Eligibility law** (M-1, B-1, M-3, C-1).
   - IMM-1.08: the inadmissibility grounds that do not apply and those that are waivable, 1231(a)(5), and final orders (vacated on approval; execution stayed on filing), from S. 744's sec. 2101 or the U.S. Citizenship Act, checked against the statute.
   - IMM-1.10 or a new IMM-1.15: no removal of an apparently eligible person from signature until a decision or a year after filing opens; release from detention unless a security or public-safety priority.
   - M-3's sentences: detained filers, the asylum election, the territories, border tribes.
   - IMM-2.08 and IMM-4.03 name their cutoffs (C-1), in section 4 and `provisions.json`.
   - Sections 5 (remedies, timeline) and 7 (who is not reached) follow.
   - If question 1 is put to Espen, stop and send it to the lead; write nothing on it until answered.
   - **Tier:** Most capable (legal drafting), with a Standard subagent for register entries (the statutes, the 2021 and 2013 bill texts, DHS's removal counts). Routine PR.
2. **Section 6's costs** (O-1 to O-4, F-1 to F-4, A-1).
   - Memo 6's coverage line priced in care's path (residual lowered by memo 6's count, the difference taken here), with the note in both files (F-3).
   - Case management's basis and range (O-2); the backlog's child cases and the counsel unit costs sourced (O-3); USCIS's extra year (O-4).
   - The booking list with E-Verify's revenue on its own row (F-1); CRT-5's re-score note naming counsel and the placeholder (F-2); A-1 shown as an alternative with its saving; F-4's text fixes.
   - Re-run the tools and update sections 4, 7 and 9 where the figures move.
   - **Tier:** Standard for the tool changes and reruns, with the Most capable session checking O-1 and F-3. It can share a PR with step 1.
3. **Lens and evidence** (L-1 to L-4, W-1, W-3).
   - The work-history records rule (L-1); registered status valid to ten years or renewed from records (L-2, a working choice); burden rows for L-1 to L-3.
   - Condition (e)'s benchmark and IMM-4.18's audit wording (L-4).
   - One independent check on memo 3's per-person figure (W-1); the spot-check of EV-IMM-608 and 610-621 against originals (W-3).
   - **Tier:** Standard. It can share a PR with step 2.
4. **Sections 7-9 and the record** (E-1 to E-3, C-2 to C-5, C-7), after steps 1-2.
   - Section 8's surge line; sections 7 and 9 on the debate year; Social Security's wording; the smaller section 9 points.
   - The court plan's expected shift in sections 7 and 8 (C-3).
   - The stale E-Verify and "pending Espen" lines; memo 4's judge figure annotated; the timeline order; `supports` paths fixed and uncited entries cited or dropped; status lines "reviewed (L2)".
   - Put questions 1 and 2 to the lead for Espen in the PR's "For the board".
   - **Tier:** Most capable for section 9; the record fixes by a Light subagent.
5. **The booking** (`6-cost.md`, part 6, as corrected). For the lead, after steps 1-2 (and question 1, if it changes a line).
   - The tier-3 PR:
     - IMM-1/E11 replaced by the split rows, with IMM-4 as spending only and E-Verify's revenue as its own row;
     - year shapes from `immigration_path.py`;
     - the profile text;
     - CAP-7S's USCIS share to zero, and CAP-7's share zeroed or stated;
     - IF1 into the base with its offset;
     - E-Verify's payroll effect in the funds model;
     - `ledger-conflicts.csv:28`'s CRT-5 note (without judges and counsel);
     - the vote model's two bills;
     - care's residual handled per F-3, so coverage is counted once;
     - the immigration test added to `run-checks.sh` (C-6), if the lead takes it.
   - **Who:** the lead's booking. Espen's label.
6. **A short L3 re-check** by the standing reviewer, limited to M-1, B-1, F-1, F-3 and the re-run. Then the lead moves IMM-1 to IMM-6 to L3 in `agenda/agenda.csv` and the README.

## Checks run

A Standard (Sonnet) subagent ran these at `4b9ca52`. The reviewer checked its readings against the files before using them (6-cost's stale prose, the 3-design and memo 4 lines, the section 9 lines), and re-did the booking rows, the residual and the judge arithmetic by hand.

- **The tools.** `immigration_model.py` and `immigration_path.py` run. `test_immigration_model.py` passes (8 tests; not part of CI, C-6). Every cell of part 1's table, its totals and ranges, part 2 and part 5 reproduces from `immigration_path.py` to rounding:
  - all-in $132.79 billion and $16.44 billion;
  - spending $152.34 billion and $20.07 billion;
  - revenue −$19.55 billion and −$3.63 billion;
  - net change $272.8 billion and $35.1 billion.

  Re-adding the printed cells gives rounding differences only (largest: the fee-repeal row, 2.4 against 2.8, values of 0.25 shown as 0.3/0.2). The judge figures reproduce: 1,673 in all, 920 added, range 863-2,403; at 150 hires a year, FY2037; at 800 judges, not cleared. Prose figures that do not match are F-4.
- **The budget model.** `models/data/recovery-budget-paths.csv`, case `mixed`: FY2040 gap $4,184.7 billion on GDP of $54,167 billion (7.73%), as `DEC-2026-11-12-08` records. The shares 0.03%, 0.065%, 0.84% and 0.39% reproduce. Immigration's only booked row is IMM-1 (`ledger-bills.csv:37`), −$140.0 billion over FY2030-39 and −$18.66 billion in FY2040 by the audit lines, unchanged since `7512852`. Part 6's file and line references are all correct.
- **IDs.**
  - All EV IDs cited in the dossier exist in some register (343 EV-IMM entries; EV-CAR and EV-HOU entries present). Every SRC is in `library/catalog.csv`, and every DEC ID exists.
  - All 85 provisions are in section 4, and every IMM ID in section 4 is in `provisions.json`. No cited provision ID is missing.
  - 22 uncited entries and 64 broken `supports` paths (C-5).
- **Statuses.**
  - Memos 1-7 and the memos README say decided (`-07`; memos 1 and 5 also `-12`). Section 3 says decided; sections 4-9 say draft.
  - All 85 provisions cite `-07`; IMM-1.01, 1.03, 1.04 and 4.13 also cite `-12` (1.01's status string omits it, C-2).
  - The agenda's 13 IMM rows are L2, with decided or alternative status as the memos say. Stale lines are C-2 and C-4.
- **Registry.** `models/registry/check.py` passes with 40 immigration warnings: 39 uncorroborated analysis entries and one contested entry (EV-IMM-570, the legacy row the dossier rejects, which is the right treatment). Cited in section 6: EV-IMM-220 (W-1), 570, 573, 578, 600 and 602, each a CBO, legacy or SSA figure used as labeled. In section 9 only EV-IMM-600 is cited, as an outside score.
- **Numbers across files.** Judges, backlogs, the cap, the floor, the population, the tiers and the cost totals agree everywhere except memo 4's 1,000-1,200 (C-4) and the stale prose in F-4.
- **Section 9.** Every number traces to sections 1-8. Flags: E-2 and E-3; the 14 million (Pew) beside MPI's 45% is two sources' figures in one sentence, which is acceptable with both named.
- **Checks.** `bash .github/scripts/run-checks.sh` on this branch passes: 164 tests and "All checks passed".
