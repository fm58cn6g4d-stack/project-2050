# Memo: how the plan counts defense, and how DEM-2 is written

Role: decision memo for Espen with two separate choices: (a) what the plan's fiscal tests count defense against, and (b) whether DEM-2 is written so its parts stand separately, and in what order. Status: awaiting Espen's decision; nothing changes until Espen decides, one choice at a time. This memo does not edit `charter/`, `legacy/` or the model inputs; any change it leads to is tier 3. Evidence: `compounding-defense.md` and `tools/compounding-defense.py` for (a); `compounding-redistricting.md` for (b).

## Choice (a): what defense is counted against

### The question

The plan holds defense flat in real terms from the FY2029 level (NSC-1A). Its fiscal tests (the ledger and the D4 checks) measure everything against CBO's current-law baseline. Should defense instead be measured against a stated path, so that the 2027-28 choice of defense level shows up in the plan's own numbers?

### Why it matters

- **Today the two agree.** The fiscal model's baseline is CBO's February 2026 outlook (`legacy/index/fiscal-long-term-model.md`). CBO projects discretionary spending at the latest enacted level grown with inflation (the baseline rules in section 257 of the Balanced Budget and Emergency Deficit Control Act; memory, verify against CBO's own description). So NSC-1A's $0 today means roughly "flat in real terms from the FY2026 level," which is path 1 in `compounding-defense.md`.
- **They split when the baseline is rebuilt.** Once FY2027-28 bills are enacted, CBO's next baseline starts from the new level. If Congress enacts the Lame-Duck Ledger's parity path ($905 billion in FY2028), defense over 2030-39 is about **$0.30 trillion** higher than path 1, and the ledger still shows $0, because the higher level is now the baseline. The D4 guardrails (debt below CBO's path) move with it. The plan would then never show what the 2027-28 deal cost.
- **The ledger already has a range for it.** NSC-1's ledger row reads 0.0 / 0.0 / 0.3 trillion, with the high end described as "a one-time +3.2% level increase" (`models/data/inputs/ledger-bills.csv`). The parity path is about +3.0% in real terms, so the existing high end is close to it; the question is whether it should move from the high end to the middle when it is enacted.

### Options

**A. Keep CBO's baseline for everything (the current rule).**
- *How it shows:* NSC-1 stays $0 after every rebaseline; whatever 2027-28 enacts disappears into the baseline.
- *For it:* the standard convention; comparable with CBO, CRFB and other scorekeepers; no model change.
- *Against it:* the 2027-28 defense decision becomes invisible to the plan, the choice the framework (question 5) asks Espen to make.

**B. Count defense against a fixed reference path, and book the difference as a cost.**
- *The path:* flat in real terms from the FY2026 enacted level ($838.7 billion in the Defense bill), stated once and kept.
- *How it shows:* after FY2028 is enacted, NSC-1's middle estimate becomes the gap (about $0.13 trillion on the middle path, $0.30 trillion on parity); the D4 checks use CBO's baseline adjusted down by the same amount, as the model already adjusts CBO for the FY2026 actuals and the tariff ruling.
- *For it:* the plan shows its own choice; a decision to accept parity in 2027 has a visible price in 2029.
- *Against it:* departs from CBO's convention for one line; invites the question why defense and not, say, nondefense increases the plan likes (which pre-load CAP-7S and would be booked the other way).

**C. Keep CBO's baseline for the tests, and add a disclosed line (recommended).**
- *How it shows:* the ledger and the fiscal report carry a line, "defense above the FY2026 flat-real reference," next to NSC-1, with the 2030-39 total; the D4 tests do not change.
- *For it:* keeps CBO comparability and the D4 rule as decided; makes the 2027-28 choice visible; cheap; can be upgraded to B later.
- *Against it:* a disclosed line does not bind; a reader could ignore it.

**Recommendation: C**, decided now so the line is in place before FY2028 is enacted, with B kept as an option if Espen wants the tests themselves to bite. For symmetry, the disclosure could carry nondefense too: the FY2027-28 nondefense increases above the same reference, which reduce what CAP-7S needs in 2029.

### What changes under each

| | A | B | C |
| --- | --- | --- | --- |
| Ledger NSC-1 line after FY2028 is enacted | $0 | The gap ($0.13-0.30 trillion) | $0, plus a disclosed line |
| D4 guardrails | CBO's baseline | CBO's baseline, adjusted | CBO's baseline |
| Model inputs (`models/data/inputs/`, tier 3) | None | `ledger-bills.csv` NSC-1 and the baseline adjustment | A new disclosure row or report section |
| Who does the work | — | **Codex**, which leads the federal budget model (`charter/STANDARDS.md`, "Roles"), with Espen's approval because adopted inputs are tier 3 | Codex, with Espen's approval |

**Owner.** The common fiscal inputs (`models/data/inputs/`, including `ledger-bills.csv` and `fiscal-profiles.csv`) and the federal budget model belong to Codex's lead role; changing an adopted input is a decision for Espen. Under B or C, this project would ask Codex in a PR comment, as the standards require, after Espen decides.

## Choice (b): how DEM-2 is written

### The question

DEM-2 (legacy domain file) is one provision: a federal mandate for congressional redistricting commissions under the Elections Clause, with a ban on mid-decade redistricting carrying a 2034 exception. D1 makes the 2033 House trifecta conditional on DEM-1 and DEM-2 being in force before the 2031 maps. Should DEM-2 be written so that each part stands even if a court strikes another, and in what order?

### Why it matters

- **The parts carry different legal risk** (`compounding-redistricting.md`, section 2; analysis). Lowest: the mid-decade ban, a "times, places and manner" rule of the kind Congress already makes (the single-member district law). Middle: federal anti-partisan criteria, workable in statute after *Rucho*. Highest: mandated commissions, which face the argument that the Elections Clause's "Legislature" means the legislature itself; three justices now on the Court dissented when it upheld state commissions in 2015 (memory, verify).
- **The value sits in the 2031 maps.** With a Democratic President, the 2030 midterm would probably let Republicans draw in Texas, Florida, North Carolina, Georgia and Ohio; against those maps DEM-2 is worth about 5 to 10 Democratic seats a cycle (analysis). If the whole statute falls because one part does, that value is lost.
- **The ban has bipartisan precedent.** CRS counts about 70 bills since the mid-2000s to bar more than one redraw a decade, ten in the 119th Congress from both parties [SRC-1040]; a House bill with five Republican cosponsors would ban mid-decade redraws, though only after November 2032 [SRC-1041].

### Options

**A. One provision, as in the legacy file.**
- *For it:* a single, clear reform; the commission mandate is the part that most changes how maps are drawn.
- *Against it:* if a court strikes the commission mandate without a severability clause, the ban may fall with it, and the 2031 maps are drawn by whoever won in 2030.

**B. One bill, severable, in order of legal risk (recommended).**
- *Title I:* the mid-decade ban (with D1's 2034 exception for the House-size package).
- *Title II:* federal criteria, including a partisan-fairness standard, enforceable in court.
- *Title III:* the commission mandate.
- *Severability and fallback:* each title stands alone; if Title III falls, maps are drawn by the state under Title II's criteria, with a court remedy where a state fails.
- *For it:* keeps the low-risk value whatever happens to the commissions; same floor time as A.
- *Against it:* a weaker political message than "independent commissions everywhere"; Title II alone still lets legislatures draw.

**C. Two bills: the ban and criteria first (in DEM-1 or alone), commissions later.**
- *For it:* the ban might attract Republican votes and could ride DEM-1; it is in force sooner.
- *Against it:* two floor fights under D2's rules; commissions may never get their own slot before 2031.

**D. Criteria and a court backstop, with commissions as a voluntary safe harbor (legacy DEM-2E).**
- *Source:* the legacy domain file records DEM-2E as an open option under "Decisions in force": "criteria and a three-judge backstop, with commissions as a voluntary safe harbor" (`legacy/domains/domain-democracy.md`, line 16). It does not say whether the mid-decade ban comes with it; this memo assumes it does, as Title I, since the ban is the lowest-risk part.
- *How it works:* Title I, the ban. Title II, federal criteria with a partisan-fairness standard. Title III, enforcement: a three-judge federal court hears challenges on a fast track and draws a remedial map where a state's map fails the criteria; a map drawn by an independent commission that meets set standards is presumed compliant (the safe harbor). No state is ordered to create a commission.
- *For it:* removes the highest-risk part, the claim that Congress cannot displace the "Legislature" under the Elections Clause, so there is no mandate for a court to strike. Court-drawn remedial maps are routine after failed redistricting, and three-judge panels with direct appeal to the Supreme Court already exist for redistricting cases (28 U.S.C. 2284; memory, verify). It is settled law before the 2031 maps rather than mid-litigation.
- *Against it:* fewer states would have commissions; legislatures keep drawing where they choose to, policed only by criteria and courts. The partisan-fairness standard is new and its enforcement depends on federal courts, including a Supreme Court that held partisan gerrymandering claims non-justiciable under the Constitution (*Rucho*); a statutory standard is different, but untested. Weaker message than "independent commissions everywhere."

**Weighing B against D.** They share Titles I and II; the difference is the third title.
- *If the commission mandate would be upheld,* B is better: every state gets a commission.
- *If it would be struck,* B falls back to D's position anyway, but only after the litigation ends. Enacted in 2029-30, a mandate would very likely still be in court when states draw in 2031 (census data arrive in spring 2031). States that oppose it would decline to set up commissions while it is challenged, and the 2031 maps would be drawn under uncertainty or under an injunction. D gives the same fallback without the wait.
- *On the 2031 maps, the ones D1 cares about,* D is the safer bet; B's extra value arrives mostly from the 2041 cycle.

**Recommendation: D, written as B's Titles I-II plus a court backstop and a commission safe harbor.** This changes the recommendation from the earlier draft (B), after weighing DEM-2E. B stays the choice if Espen wants the mandate tried in court: in that case, set Title III's effective date at the 2041 cycle, so a pending challenge cannot cloud the 2031 maps, and keep D's backstop as the fallback. Two related choices go with either:
- **Effective date:** the ban should apply from enactment through the 2031 cycle, not after 2032 (the bipartisan bill's date), or it leaves 2031 untouched. From enactment, it also freezes the 2025-26 Republican maps and any 2028 Democratic maps until 2031; that is the price of using it at all before 2031.
- **D1's stipulation** would read as "DEM-2's ban and criteria in force before the 2031 maps," with commissions as the goal rather than the condition. That restatement changes D1's wording, a tier-3 change that also depends on how PR #80 lands; it would go in a separate tier-3 PR after both decisions, not in this memo.

### What changes under each

| | A | B | C | D (DEM-2E) |
| --- | --- | --- | --- | --- |
| DEM-2 in the agenda | One item | One item, three titles (sub-IDs added when the democratic-renewal dossier specifies it) | Two items | One item, three titles; the legacy DEM-2E label |
| D1's House stipulation | Unchanged | Restated around Titles I-II | Restated; depends on the first bill's date | Restated around Titles I-II |
| Floor time (D2) | One bill | One bill | Two bills | One bill |
| Commissions | Mandated | Mandated, severable | Mandated, in a later bill | Voluntary, rewarded by the safe harbor |
| If a court strikes commissions | Risk to the whole | Ban and criteria stand, after the litigation | Ban stands if already enacted | Nothing to strike |
| State of the law for the 2031 maps | Mandate likely in court | Mandate likely in court | Second bill may not exist | Settled, if Titles I-II hold |

## Decide one at a time

Each choice stands alone. Approving one does not approve the other. Neither changes `charter/` until Espen decides; a decision would then be recorded with a `DEC-` entry and, for (a), a request to Codex.
