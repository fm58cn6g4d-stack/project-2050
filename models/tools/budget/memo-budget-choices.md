# Memo: five choices about how the plan's budget is counted

Role: decision memo for Espen, piece B7 of the budget workflow (`models/tools/budget/WORKFLOW.md`). It has five separate choices, each with options, a recommendation and what changes. Status: awaiting Espen's decision, one choice at a time. Nothing changes until Espen decides, and any change it leads to is a tier-3 PR. Sources: the "Choices for Espen" section of `models/tools/budget/CONVENTIONS.md` (B1, PR #107) and `dossiers/scenario/memo-defense-baseline-and-dem2.md`, choice (a). The `ASM-` IDs are in `models/data/budget/assumptions.csv`.

**How to read this.** Each choice is about how the plan's own numbers are judged. None of them changes a program. Today's practice is option A each time. Taken together, the recommendations make the plan more cautious and more visible, without making it impossible to compare with CBO.

---

## 1. Which baseline the plan is measured against as CBO updates it

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

---

## 2. Central estimates or cautious ones in the fiscal tests

**The question.** The D4 maturity test and the debt guardrails use each ledger row's midpoint (`ASM-CALIB-MID`). The ledger has a low and high end for every bill, but those never reach the fiscal model. A plan that passes on midpoints could fail if costs land high and revenue lands low.

**Options.**
- **A. Midpoints only** (today). This is the scorekeepers' practice, and the tests stay comparable.
- **B. The tests must also pass at the cautious end:** high costs and low revenue. This is the most prudent commitment, but it would probably need more revenue or smaller programs.
- **C. Midpoints decide; a cautious reading is reported beside every test.** It shows the margin, and the test is flagged when the cautious reading fails.

**Recommendation: C now, with B reconsidered once the uncertainty simulation exists** (`models/tools/roadmap.md`, item 1). The simulation gives a probability of passing instead of a worst-case stack. Stacking every high cost with every low revenue overstates the risk, because the errors aren't all in one direction. Reporting the cautious reading means you always see the margin.

**What changes under C.** Each D4 line in the fiscal report and the viewer gets a second number, "at the cautious end", with pass or fail. Midpoint results don't change.

---

## 3. FY2029 and the scoring window

**The question.** The plan starts in January 2029. The first reconciliation bill (R1) runs under an FY2029 budget resolution, but every total is FY2030-39 (`ASM-WINDOW`). Money spent or raised in FY2029 is outside the ledger, the D4 tests and the debt path. The known case is CAP-7S's FY2029 cash, recorded as "unpriced, not zero".

**Options.**
- **A. Keep FY2030-39, and price FY2029 as a separate, disclosed line.** No headline figure moves.
- **B. Move the window to FY2029-38.** It matches R1's official window, but every ten-year figure in the project changes.
- **C. Score each bill over its own resolution's window.** The most faithful, and the most work. Totals across bills would no longer share one window.

**Recommendation: A**, built so it can grow into C. The provision library (B3) already records each row's vehicle. Once it can score a bill over its own window, an R1 score over FY2029-38 can sit beside the plan's common FY2030-39 totals without changing them.

**What changes under A.** FY2029 rows get priced (CAP-7S first). The FY2029 total appears as its own line in the fiscal report and the viewer, and is added to the debt path from FY2029.

---

## 4. Whether the debt guardrails must hold if interest rates are higher

**The question.** The guardrails are judged at CBO's projected interest rates (`ASM-RATE-MARGINAL`, `ASM-RATE-LT`). Interest is the biggest single risk. One point higher on all debt from 2030 raises the decided program's 2056 debt from 156% to 197% of GDP (`ASM-RATE-SHIFT`). The guardrails compare the plan with the baseline, which also worsens, so they may still pass. The question is whether the plan commits to anything under stress.

**Options.**
- **A. Test at CBO's rates and report the stress case** (today).
- **B. The guardrails must also hold in the one-point-higher case.** The plan must not do worse than the baseline even when rates are higher.
- **C. Add an absolute condition under stress,** such as net interest below a stated share of GDP. This needs a threshold Espen would have to choose.

**Recommendation: B**, with C taken up in the fair financing foundation, where a threshold can be set against evidence rather than picked here. B is a real, testable commitment that uses only what the model already computes.

**What changes under B.** A third D4 reading, "at rates +1 point", becomes pass-or-fail in place of report-only. If it fails today, the fiscal report says so and by how much. That would be a finding for the fair financing work, not something to fix by changing the test.

---

## 5. Whether Social Security's new revenue counts toward the debt guardrails

**The question.** The maturity test reads the general fund only. The total-debt guardrails read the unified budget, where SS-1's payroll revenue lowers total debt along with general-fund borrowing (`ASM-GF-UNIFIED`). D4-B also says Social Security is kept whole and judged over 75 years. So can a trust-fund surplus help general-fund programs pass the debt test?

**Options.**
- **A. Unified reading** (today). This is the convention CBO's deficit uses.
- **B. Test total debt without the trust funds' own improvement.** It's stricter, and it matches "Social Security pays for Social Security".
- **C. Report both, with the stricter one as the commitment.**

**Recommendation: C.** It keeps the number comparable with CBO, and it makes the stricter reading, which matches D4-B, the one the plan is judged by. Social Security's new revenue then can't quietly fund other programs.

**What changes under C.** Each total-debt guardrail gets a second reading, "excluding Social Security's improvement", and pass or fail is judged on that one. If it fails where the unified reading passes, the gap shows how much other programs lean on Social Security's surplus. That's a finding for fair financing.

---

## After Espen decides

The budget model's owner makes each change in its own tier-3 PR, with a `DEC-` entry. Under the ownership proposal in PR #106, that's a Claude worker, with Codex asked to review. B5's viewer then shows the result. Choices 2, 4 and 5 add readings beside the existing tests, so their effect on today's pass or fail results will be visible before anything is relied on.
