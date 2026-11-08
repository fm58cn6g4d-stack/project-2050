# Memo: five choices about how the plan's budget is counted

Role: decision memo for Espen, piece B7 of the budget workflow (`models/tools/budget/WORKFLOW.md`). It has five separate choices, each with options, a recommendation and what changes. Status: all five choices decided by Espen on November 8, 2026. Choices 1, 2, 4 and 5 follow CBO's practice. For choice 3, Espen asked first whether CBO's practice would break the consistency of the plan's data, then agreed to the lead session's answer: A, plus a score in each bill's own CBO window. Espen's direction, relayed by the lead session: "do what CBO would do for all except 3, the 2029 window, where i want you to tell me if it will mess things up for consistency of our plan's data to do as CBO does." (Choice 5 was decided first, with "do what CBO would do".) Nothing changes until Espen decides, and any change it leads to is a tier-3 PR. Sources: the "Choices for Espen" section of `models/tools/budget/CONVENTIONS.md` (B1, PR #107) and `dossiers/scenario/memo-defense-baseline-and-dem2.md`, choice (a). The `ASM-` IDs are in `models/data/budget/assumptions.csv`.

**About the figures.** The numbers quoted in choice 5 come from `legacy/index/fiscal-long-term-model.md`. That report is the **pre-EDU-9B comparison vintage**: by its own header, its "decided package" results don't establish whether today's plan passes D3 or D4 (see also `legacy/index/fiscal-recovery-model.md`). Here they show what each rule would do to a package like the plan, not whether the current plan passes or fails. Each test is rerun on the current plan once the budget model is integrated (B6).

**How to read this.** Each choice is about how the plan's own numbers are judged. None of them changes a program. Today's practice is option A each time. Taken together, the recommendations make the plan more cautious and more visible, without making it impossible to compare with CBO. Choice 5 keeps the rule already decided, because the stricter reading would make the decided package fail every year (see below).

**What CBO would do.** Espen's answer on choice 5 was to follow CBO's practice. Each choice below ends with a short note on whether its recommendation matches what CBO does and, where it departs, why. Espen then applied the same principle to every choice except 3, which was decided after a consistency check. Each decided choice opens with its decision; the recommendations as first written are kept beneath for the record.

---

## 1. Which baseline the plan is measured against as CBO updates it

**Decision (Espen, November 8, 2026): C, CBO's practice.** The tests use CBO's latest baseline, as CBO does. The 2027-28 changes are disclosed beside it, like CBO's own baseline-change tables. This matches the recommendation.

*This includes the defense question already on the board (`memo-defense-baseline-and-dem2.md`, choice a). Deciding this one decides that one too.*

**The question.** The plan's numbers are increments over CBO's current-law baseline, which is February 2026 today. When CBO publishes its 2027 and 2028 baselines, whatever Congress enacts in 2027-28 joins the baseline and drops out of the plan's numbers:
- a higher defense level (NSC-1A reads $0 either way, with $0.13-0.30 trillion over 2030-39 at stake);
- a lame-duck extension of the 2025 law's tax cuts (about $33 billion in FY2029, then about $70 billion a year);
- emergency supplementals, which the baseline then carries forward with inflation.

**Options.**
- **A. Adopt each new CBO baseline as it comes** (today's rule). Comparable with every scorekeeper. But the cost of the 2027-28 deals disappears from the plan.
- **B. Hold a fixed reference:** February 2026 as adjusted, kept for good. The plan always shows what 2027-28 cost, but no outside scorekeeper will reproduce its numbers.
- **C. Measure against CBO's latest baseline, and disclose the 2027-28 changes as lines beside it.** Each line is measured against the February 2026 reference: defense above flat-real, any tax extension, and supplementals carried forward. The tests use CBO's baseline. The disclosed lines show what the deals cost and can't be missed.

**Recommendation: C, for all three**, not for defense alone. Then the plan doesn't follow one rule for defense and another for taxes. It's the defense memo's option C, made general, and it can be tightened to B later if Espen wants the tests themselves to count the deals.

**What changes under C.** The fiscal report and the viewer (B5) carry a "Changes since the February 2026 reference" block. The D4 tests don't change. It's put in place before FY2028 is enacted.

**What CBO does.** CBO scores legislation against its latest baseline, and each new baseline takes in whatever has been enacted (option A). It extends emergency and supplemental funding forward with inflation, as its baseline rules require. It also publishes how each baseline differs from the last, split into legislative, economic and technical changes (for example, Table 5-1 of the February 2026 baseline file). C matches CBO for the tests. Its disclosed lines are the plan's own version of CBO's change tables, measured from the February 2026 reference. B departs from CBO.

---

## 2. Central estimates or cautious ones in the fiscal tests

**Decision (Espen, November 8, 2026): C, CBO's practice.** Midpoints decide, as CBO's central estimates do. A cautious reading is reported beside them once it is computed, as CBO reports uncertainty separately. This matches the recommendation.

**The question.** The D4 maturity test and the debt guardrails use each ledger row's midpoint (`ASM-CALIB-MID`). The ledger has a low and high end for every bill, but those never reach the fiscal model. A plan that passes on midpoints could fail if costs land high and revenue lands low.

**Options.**
- **A. Midpoints only** (today). This is the scorekeepers' practice, and the tests stay comparable.
- **B. The tests must also pass at the cautious end:** high costs and low revenue. This is the most prudent commitment, but it would probably need more revenue or smaller programs.
- **C. Midpoints decide; a cautious reading is reported beside every test.** It shows the margin, and the test is flagged when the cautious reading fails.

**Note: the cautious reading isn't computed yet.** The ledger's low and high ends don't reach the fiscal model today. Under C or B, the first step is to carry them through (B3 records them per provision), and only then would the readings exist.

**Recommendation: C now, with B reconsidered once the uncertainty simulation exists** (`models/tools/roadmap.md`, item 1). The simulation gives a probability of passing instead of a worst-case stack. Stacking every high cost with every low revenue overstates the risk, because the errors aren't all in one direction. Reporting the cautious reading means you always see the margin.

**What changes under C.** Each D4 line in the fiscal report and the viewer gets a second number, "at the cautious end", with pass or fail. Midpoint results don't change.

**What CBO does.** CBO's estimates are central estimates, meant to sit in the middle of the range of likely outcomes. It discusses uncertainty separately, through ranges and sensitivity analyses, rather than scoring at a cautious end. A and C match CBO; C adds a reported cautious reading, which CBO's practice allows. B departs: CBO doesn't hold a proposal to a worst case.

---

## 3. FY2029 and the scoring window

**Decision (Espen, November 8, 2026, agreeing with the lead session's recommendation): A, plus each bill's own CBO window.** Espen asked whether scoring as CBO does would break the consistency of the plan's data. The answer: not if both come from one series.
- **Plan totals and the D4 tests** keep one common FY2030-39 window, with FY2029 priced as a separate, disclosed line (option A).
- **Each bill is also scored over its own CBO window:** the budget year plus nine, so R1 under an FY2029 resolution is scored over FY2029-38. This is required now, not later, so the Byrd rule's out-year test and each resolution's limits can be checked.
- **The viewer and the reports show both, labeled.** Both are sums of the same annual series, so they always reconcile.

This builds the recommendation's "can grow into C" now. It goes into the scope of B3 (per-bill window scoring), B5 (both labeled readings) and B6 (FY2029 on the debt path); the workflow (`models/tools/budget/WORKFLOW.md`) adds it in a follow-up once PR #104 merges.

**The question.** The plan starts in January 2029. The first reconciliation bill (R1) runs under an FY2029 budget resolution, but every total is FY2030-39 (`ASM-WINDOW`). Money spent or raised in FY2029 is outside the ledger, the D4 tests and the debt path. The known case is CAP-7S's FY2029 cash, recorded as "unpriced, not zero".

**Options.**
- **A. Keep FY2030-39, and price FY2029 as a separate, disclosed line.** No headline figure moves.
- **B. Move the window to FY2029-38.** It matches R1's official window, but every ten-year figure in the project changes.
- **C. Score each bill over its own resolution's window.** The most faithful, and the most work. Totals across bills would no longer share one window.

**Recommendation, as written before the decision: A**, built so it can grow into C. The provision library (B3) already records each row's vehicle. Once it can score a bill over its own window, an R1 score over FY2029-38 can sit beside the plan's common FY2030-39 totals without changing them.

**What changes under A.** FY2029 rows get priced (CAP-7S first). The FY2029 total appears as its own line in the fiscal report and the viewer, and is added to the debt path from FY2029.

**What CBO does.** CBO scores each bill over the window of the budget resolution in force: the budget year plus the following nine years. R1, under an FY2029 resolution, would be scored over FY2029-38. That is option C. A departs from CBO: it keeps one common FY2030-39 window across the plan, so that totals for bills passed in different years add up. The departure is disclosed, and A is built to grow into C, so an R1 score in CBO's own window can sit beside the common totals.

---

## 4. Whether the debt guardrails must hold if interest rates are higher

**Decision (Espen, November 8, 2026): A, CBO's practice.** The guardrails are tested at CBO's projected rates. The +1-point stress case is reported beside them, with no pass-or-fail condition. This differs from the recommendation (B), which is kept below for the record. An absolute interest threshold (option C) can still be taken up in the fair financing foundation.

**The question.** The guardrails are judged at CBO's projected interest rates (`ASM-RATE-MARGINAL`, `ASM-RATE-LT`). Interest is the biggest single risk (`ASM-RATE-SHIFT` sets the stress case: one point higher on all debt from 2030). The guardrails compare the plan with the baseline, which also worsens, so they may still pass. The question is whether the plan commits to anything under stress.

**Options.**
- **A. Test at CBO's rates and report the stress case** (today).
- **B. The guardrails must also hold in the one-point-higher case.** The plan must not do worse than the baseline even when rates are higher.
- **C. Add an absolute condition under stress,** such as net interest below a stated share of GDP. This needs a threshold Espen would have to choose.

**Recommendation, as written before the decision: B**, with C taken up in the fair financing foundation, where a threshold can be set against evidence rather than picked here. B is a real, testable commitment that uses only what the model already computes. **Whether the plan passes B today isn't stated here.** The size of the stress case (DEC-R1, BASE-R1) is diagnostic only until B4's benchmark SE-1 is resolved (`models/tools/budget/MODEL-CARD.md`, "What is not yet validated"), so it can't support a decision memo. The model reprices all debt at the higher rate at once, while CBO's rule of thumb phases it in as debt rolls over, so the model's stress case is likely harsher than CBO's. Choosing B fixes the rule. Whether the plan meets it is reported once SE-1 is resolved (it needs CBO's rules-of-thumb workbook, board question 0e), or once Espen approves using the readings before then (board question 0f).

**What would have changed under B** (not adopted). A third D4 reading, "at rates +1 point", becomes pass-or-fail in place of report-only. If it fails today, the fiscal report says so and by how much. That would be a finding for the fair financing work, not something to fix by changing the test.

**What CBO does.** CBO projects at its central interest rates and reports how the outlook changes if rates are higher, through its rules of thumb and the long-term outlook's alternative scenarios. It reports these; it doesn't set a pass-or-fail condition, because CBO makes no policy recommendations. That is option A. B departs from CBO: the guardrails are the plan's own commitments, not a scoring convention, and B asks them to hold under a stress CBO only reports. If Espen applies "do what CBO would do" to this choice as well, it points to A. CBO's rule of thumb also phases higher rates in as debt rolls over, which the model doesn't yet do (benchmark SE-1).

---

## 5. Whether Social Security's new revenue counts toward the debt guardrails

**The question.** The maturity test reads the general fund only. The total-debt guardrails read the unified budget, where SS-1's payroll revenue lowers total debt along with general-fund borrowing (`ASM-GF-UNIFIED`). D4-B also says Social Security is kept whole and judged over 75 years. So can a trust-fund surplus help general-fund programs pass the debt test?

**Options.**
- **A. Unified reading** (today). This is the convention CBO's deficit uses.
- **B. Test total debt without the trust funds' own improvement.** It's stricter, and it matches "Social Security pays for Social Security".
- **C. Report both, with the stricter one as the commitment.**

**What the stricter reading would show (comparison vintage).** The decided package fails it in every year. Its general-fund-attributable debt is above zero throughout: 5.4% of GDP in 2039, 5.9% in 2045 and 5.1% in 2056. Over 2030-39 the general fund runs a $2.30 trillion primary deficit, while the unified budget, with SS-1's surplus, shows −$2.94 trillion (`legacy/index/fiscal-long-term-model.md`). Most of the general fund's 2030-35 deficit is time-limited spending the D4 investment envelope already allows (CAP-7S's surge, Moving America's capital lines). But the deficit doesn't end with the surge. The general fund's primary deficit is still $72 billion in 2040, $47 billion in 2042 and $9 billion in 2045, and it turns to surplus only by 2050. So in that vintage the package also **fails D4's maturity test** (general-fund balance in FY2040 at or below zero), whichever reading this choice picks.

**Decision (Espen, November 8, 2026): CBO's practice, which is option A.** Espen's answer, relayed by the lead session: "do what CBO would do." CBO's practice is the unified budget. By law, Social Security's two trust funds (and the Postal Service) are off-budget. CBO's headline deficit and its debt held by the public still count them, and CBO reports the on-budget and off-budget parts separately beside the total. So the decided unified rule stays, and the reading without Social Security is shown beside it as disclosure, not as a test. One difference to keep in view: the plan's general-fund reading is not CBO's on-budget figure, because CBO's on-budget total also includes other trust funds, such as Medicare's.

**Recommendation, as written before the decision: A, the rule already decided, with the general-fund reading kept beside it.** The fiscal report already shows that reading "for information", and states that under the decided rule it isn't a guardrail. Switching to B or C would make the decided package fail every year. It would also reverse a decision Espen has made, and the failure would come mostly from the planned, time-limited investment surge. The plain finding: the plan's ten-year general-fund deficit is $2.30 trillion, in the comparison vintage a smaller general-fund deficit continues into the mid-2040s (a maturity-test failure), and Social Security's surplus is what keeps total debt on its path. Whether the general fund should carry that on its own is a fair financing question, and it belongs there.

**What changes under A.** Nothing in the tests. The viewer (B5) shows the general-fund reading next to the unified one, so the gap is never hidden.

---

## After Espen decides

The budget model's owner makes each change in its own tier-3 PR, with a `DEC-` entry. Under the ownership proposal in PR #106, that's a Claude worker, with Codex asked to review. B5's viewer then shows the result. With the decisions taken, choices 2 and 5 add readings beside the existing tests, and choice 4 keeps the stress case as a reported reading; none of them changes a pass or fail result. Choice 1 adds the disclosed 2027-28 lines. The `DEC-` entries for all five choices are filed with the first tier-3 PR that records the budget choices.
