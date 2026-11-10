# Care you can count on, part A (health): L2/L3 milestone review

Role: the independent milestone review of the care dossier's health part (`charter/PLAN.md` 3.2 and 5, "Review"; `charter/STANDARDS.md`, "Milestone review"), board row D-4r. The reviewer wrote none of the dossier. It tries to break the work on four fronts (weak evidence, missing populations, optimistic assumptions, cheaper alternatives), applies the design lens (`DEC-2026-11-09-13`), checks the fiscal-rule report against `DEC-2026-11-10-05`, checks internal consistency across sections 1-9, `provisions.json` and `agenda/agenda.csv`, and checks section 9 against sections 1-8. Status: current, as of main at commit `5371d3a` (November 10, 2026, after #220 and #222). Reviewer: Claude Code, `session_01UQzgBupQZyXMABBVLAHyji`. It changes nothing in the dossier: every fix below is a later step, which the lead assigns.

Espen's decisions (`DEC-2026-11-09-07`, `DEC-2026-11-10-09`, `-11`, `-12`) are settled. Where a decided choice has a consequence the dossier does not show, this review says so; it does not argue the choice. Board question 0i (the hospital transition fund, HLT-7.15) is with Espen and is not decided or re-argued here. Under `DEC-2026-11-10-07`, a clearly bounded uncertainty is not a defect, and every investigation asked for below names the decision it informs and whether it blocks that decision now.

## Verdicts

| Level | What it needs (`charter/PLAN.md` 3.2) | Verdict |
| --- | --- | --- |
| **L2, design** | Key parameters chosen (who, what, how much, who administers), with the main alternatives weighed | **Pass** (record fixes only, none blocking) |
| **L3, specified** | Provisions section by section (eligibility, benefit, administration, phase-in, remedies); evidence for each load-bearing claim; a cost range validated by models with stated limits; a delivery plan | **Not yet: close.** Three blockers |

**Why L2 passes.** Every fork had two to four options weighed on evidence, with single-payer given full weight (`DEC-2026-11-09-07`) and the legacy designs as options (`DEC-2026-10-30-02`). All five memos and seven points are decided and recorded, and the S. 1506 comparison was done as Espen asked before memo 3 was confirmed. Agenda rows HLT-1, 2, 6, 7, 8, A1, A2, A4 and RTS-2 are L2 `decided`, HLT-3, 5 and A3 L2 `alternative`, and HLT-4 stays L1 for part B (`agenda/agenda.csv:283-294`, `:456`). Section 3 itself was not brought up to date with the later decisions (C-1). That is a record fix, because the decisions, memo status lines and section 4 carry them.

**Why L3 is not yet.** Most of L3 is in place. Section 4 specifies 40 provisions with parameters, vehicle, agency, current-law change and evidence. Section 5 has a timeline, remedies and states' roles. Section 6 prices the decided path on the coverage model, with its limits stated. Every decision the brief listed is carried out faithfully (part 1). The blockers:
1. **The states' payment has no single mechanism, and the one section 5 uses is the one section 8 says the Constitution rules out** (F-1). This is a stream of about $307 billion a year in 2032. It is an inconsistent commitment with a legal obstacle, so it is a defect under `DEC-2026-11-10-07`, not a bounded uncertainty.
2. **The entitlement is silent on the territories** (M-1). That is about 3.5 million residents of Puerto Rico, Guam, the U.S. Virgin Islands, the Northern Mariana Islands and American Samoa, whose Medicaid is capped today. The coverage model leaves them out, and nothing says so. Eligibility is an L3 element, and "every resident" (point 3) does not settle it.
3. **Section 9 does not say how large the new taxes are** (E-1). Section 6 says about $2.4 trillion a year at full scale in 2032 and $3.7 trillion in FY2040, after the employer contribution. Section 7 calls it "far larger than any other dossier's" and cites Vermont, whose plan stopped when its tax became visible. The brief says only "new taxes fill the rest". This carries forward the standing reviewer's open note on #222.

**What can reach L3 once those land.** Every provision can, apart from HLT-7.15, which waits on Espen's question 0i. None is held back by an unspecified parameter. The open items (people without status, IHS funding, TRICARE's purchased care, the copay schedule, the cohort order) are bounded working choices or other owners' decisions.

## How this review was done

- Read the charter (standards, the board's stage D rows and question 0i, plan section 3.2's levels, `DEC-2026-11-10-05`, `-07`, `-09`, `-11` and `-12`), the template, and both earlier milestone reviews as models. Read sections 3-9 in full, the memo status lines, the README, `tools/health_path.py` and the coverage model's card and inputs where section 6 relies on them. Sections 1-2 and `research-s1506-comparison.md` were read for the claims sections 3-9 draw on.
- A Sonnet subagent ran the mechanical checks. The reviewer checked what it reported before using it, and re-ran the figures it doubted.
  - **IDs.** Every EV-CAR ID cited in the dossier exists (240 entries). Every source is in `library/catalog.csv`. Every HLT provision is cited in section 4, and every DEC ID cited exists. Nine entries are never cited: EV-CAR-003, 004, 036, 053, 054, 057, 058, 059 and 334. That is harmless, but 334 belongs to the 330-350 block written for sections 4-6.
  - **Statuses.** In `provisions.json`, 39 provisions are decided or adopted from the S. 1506 comparison. HLT-7.15 is "recommended; for Espen", consistently in sections 4, 6, 8 and the README. Nothing decided is still "proposed".
  - **Sums.** Every table in section 6 re-adds. The one exception is part 5, where the legacy FY2040 rows sum to $570 billion against the $569 billion printed (C-6). The sensitivity table (part 6) was re-run row by row with parameter overrides, and every row matches.
  - **Models.** `health_path.py` reproduces section 6, as follows:
    - FY2030-39: $25,681 billion;
    - FY2040: $4,743 billion;
    - 2032 at full scale: $3,052 billion;
    - the neutral contribution share: 0.650;
    - the exclusion revenue: $680 billion in 2032 and $1,057 billion in FY2040;
    - the seven-year glide: $289 billion.

    The coverage model's 23 tests and the registry's 10 tests pass.
  - **Registry.** `models/registry/check.py` passes. It gives 38 corroboration warnings on care entries, all analysis entries; the two in the 330-350 block (EV-CAR-344 and 347) are already called "a single source" in section 6.
  - **Quotes.** All 123 entries with a saved text match their anchors verbatim. EV-CAR-340 and 342 are citation-only. The reviewer fetched both originals on November 10, and every anchor appears verbatim (W-1).
- The reviewer re-ran `health_path.py` on a fiscal-year basis (F-2) and sized the exclusion revenue at the wage pass-through the dossier's own evidence reports (F-3).
- `bash .github/scripts/run-checks.sh` passes on this branch.

## 1. The decisions, carried out

Each decision the brief listed, checked against section 4, `provisions.json`, sections 5-6 and the agenda:

| Decision | Where | Verdict |
| --- | --- | --- |
| 2035 endpoint (`-11`, 1a) | HLT-7.03, 7.14, 7.23, 7.25, 7.26; sections 5, 6 | Faithful. Memo 1 and 2's 2037 figures are marked superseded in their status lines and in `4-specification.md:129`. Section 3 still carries them (C-1) |
| Employer groups with Medicaid in 2033-35, required, with a contribution (`-11`, 1) | HLT-7.03, 7.18; `5-delivery.md:46`, `:54`; `6-cost.md:111-114` | Faithful. The contribution runs until the settlement's payroll contribution, as decided |
| Memo 3 B, with exclusion revenue only on premiums that become wages (`-11`, 2) | HLT-7.22; `6-cost.md:109-111`; `health_path.py` `contribution()` | Faithful in the accounting: the contribution is netted against the exclusion it displaces and is never added to a full exclusion figure. But "premiums that become wages" is read as all premiums not paid as the contribution, which the dossier's own evidence contradicts (F-3) |
| Medicare upgrades from 2031 (`-11`, 3) | HLT-2.01; `6-cost.md:61` | Faithful |
| Abortion covered, Hyde ended in general (`-11`, 4) | HLT-7.05, RTS-2.01, 2.02 | Faithful, with the scope of "in general" still to confirm for a few limits outside Labor-HHS (W-4) |
| VA, TRICARE and IHS kept alongside (`-11`, 5) | HLT-7.24; `5-delivery.md:87` | Faithful in the specification. The model counts TRICARE and veterans' coverage inside employer coverage, which moves into the plan (F-4) |
| No duplicative private coverage at the endpoint (`-12`, 1) | HLT-7.23; `5-delivery.md:49` | Faithful. Its legal basis is asserted without register entries (W-2) |
| Ownership kept, with targeted guardrails (`-12`, 2) | HLT-7.27; `4-specification.md:141` | Faithful. Section 3 and memo 5's status line do not cite `-12` (C-1, C-3) |

## 2. Findings

IDs: F fiscal, M missing populations, O optimistic assumptions, A cheaper alternatives, W weak evidence, E section 9, C consistency and record. **Blocking** means blocking L3.

### F. The fiscal-rule report (`DEC-2026-11-10-05`) and the money

**The report itself follows `DEC-2026-11-10-05`.** Section 6 reports the yearly path, the permanent FY2040 cost ($4,743 billion before the contribution, $3,668 billion after it) and the plan-wide margin both ways (`6-cost.md:120-131`). It does not treat health's gap as a defect. It splits the spending line ($5,800 billion in FY2040) from the revenue lines (the exclusion, $1,057 billion; the contribution, $1,075 billion) and never adds them together. Its one question for Espen (HLT-7.15) is one where the options reach different hospitals at different cost. That is the kind of question the rule sends to Espen. The findings below are about the inputs to that report, not its form.

**F-1. The states' payment: three sections, three mechanisms, and a legal obstacle. Blocking.**
- **What the sections say:**
  - Section 4 makes the payment an unconditional duty: "Each state pays the fund a fixed amount for its residents who move" (`4-specification.md:85`; `provisions.json`, HLT-7.17).
  - Section 5 collects it by "one yearly formula per state, netted against the federal Medicaid money it still receives for long-term care" (`5-delivery.md:12`).
  - Section 8 says the payment "must therefore be a condition on new money, or the state's choice to keep running long-term care with federal match, not a threat to existing funds" (`8-change-our-minds.md:25`, citing *NFIB v. Sebelius*).
- **Why it matters.** Netting against the long-term care match that states already receive is withholding existing funds, which is the leverage section 8 rules out. After the move, long-term care is most of what is left of a state's Medicaid. So it is closer to the 2012 facts than the Medicare Part D "clawback", the nearest precedent, which is enforced the same way but was never tested on the merits.
- **Size.** The stream is $307 billion in 2032 (`6-cost.md:21`) and about $480 billion in FY2040 on the model's growth.
- **The fallback is not specified.** Section 8 prices dropping the payment (`8-change-our-minds.md:15`). It does not say how a "condition on a new federal grant" would work when the plan replaces the state's acute-care Medicaid. It is unclear what new grant a state would take.
- **No register entry.** *NFIB* has no register entry ("evidence still needed").
- **Why blocking.** This is an inconsistent commitment and a missing delivery mechanism on a stream larger than most dossiers' whole cost. Under `DEC-2026-11-10-07` it belongs on the critical path, because a plausible answer (the payment cannot be enforced as section 5 writes it) undermines the commitment.
- **The fix.**
  - Choose one mechanism and write it the same way in sections 4, 5, 6 and 8 and in `provisions.json`. Candidates:
    - a condition on a new grant (for example, the plan's payments for the state's long-term care population, or a new state-option long-term care match on better terms), with acceptance optional;
    - the clawback model, with its risk stated;
    - a hold-harmless that drops the payment.
  - Add an evidence entry for *NFIB* (567 U.S. 519, 2012). Add one for the Part D clawback statute (42 U.S.C. 1396u-5(c)).
  - The choice of mechanism is a drafting and legal choice that follows from memo 3 B. If the only enforceable mechanism costs materially more, the money question goes to the settlement, not to Espen by itself.

**F-2. Fiscal years are counted as calendar years. FY2030-39 reads about $1.1 trillion high. Not blocking for L3; it must be fixed before the booking.**
- **What the script does.** `health_path.py` counts each January move for the whole fiscal year that contains it (`health_path.py:23`). But FY2031 runs from October 2030 to September 2031, so wave 1 covers only nine of its twelve months.
- **Re-run on a fiscal-year basis** (each fiscal year taking three-quarters of its calendar year and a quarter of the one before):
  - the window falls from $25.68 trillion to about $24.56 trillion;
  - with the contribution at 65%, from $20.12 trillion to about $19.25 trillion;
  - FY2040 falls by about $63 billion (to about $4,680 billion);
  - the year-by-year path shifts most in FY2031 (868 to about 673) and FY2035 (3,680 to about 3,283).
- **Why not blocking.** The simplification is disclosed (`6-cost.md:166`; `7-validation.md:31`) but not sized, and "none changes a decision" is right. It is a bounded overstatement of about 4%, in the cautious direction.
- **Why it must be fixed before the booking.** The budget model books by fiscal year, and part 5 proposes booking these figures as fiscal-year rows. The template's "One basis for each fiscal figure" rule then requires the fiscal-year path. Fix it in the script, not by hand, so that sections 4, 6 and 9 and the README all move together.

**F-3. The exclusion revenue assumes every former premium not paid as the contribution becomes taxable wages. Not blocking; label it and show the low reading.**
- **What the dossier assumes.** Section 7 states the assumption and, beside it, its own evidence: "about half of premium cost passes into pay (Anand, 2017) [EV-CAR-299]" (`7-validation.md:28`).
- **Why it matters.** `DEC-2026-11-10-11` counts the stream "only on former premiums that become taxable wages". The dossier treats the full pass-through as a fact rather than as what it is: CBO's scoring convention, which holds total compensation fixed. The convention is a defensible basis for a score. But the decision's wording makes the evidence relevant, and the settlement will rely on the figure.
- **The low reading at half pass-through** of the employer-paid share (employee-paid premiums become take-home pay by construction):
  - with the contribution at 65%, the 2032 revenue falls by about $85 billion and FY2040 by about $130 billion;
  - with no contribution, by about $240 billion and $375 billion.
  Some of the difference would be taxed as profits instead, so the true loss is smaller.
- **The fix.**
  - Label the line in `6-cost.md:109-111` "on CBO's convention (total compensation fixed)".
  - Show the half pass-through reading as a sensitivity row in part 6.
  - Carry the range into the settlement figure at `6-cost.md:176`.
  - Working assumption; no investigation needed now.

**F-4. The booking proposal (part 5), reviewed for correctness only.** The lead will make it a separate tier-3 PR. Its structure is right: a spending row, a revenue row for the exclusion on the general fund, and the contribution kept off the books until the settlement sets its share. Points to fix in that PR:
1. **Fiscal-year phasing.** As F-2.
2. **HLT-4 kept whole "until part B decides long-term care"** (`6-cost.md:138`). Legacy HLT-4 is more than long-term care: it also carries children's continuous coverage and Medicaid dental (`legacy/domains/domain-health.md:14`). Both are replaced by the plan when children move (2031) and when Medicaid moves (2033-35). Keeping those parts after each group's wave double-counts. Split HLT-4, retiring the replaced parts from each wave. Section 4 should also say what becomes of HLT-4's other parts (health centers doubled, 14,000 residency slots, the Momnibus, Title X), which neither section 4 nor part B now owns.
3. **TRICARE, veterans' programs and FEHB inside the employer group.** The model's employment-based cell "includes FEHB, TRICARE, veterans programs" (`models/tools/health-coverage/inputs.csv:7`). So the plan prices them as movers, counts their federal outlays among the "employer premiums" removed, and counts a contribution from them as revenue.
   - The federal government paying the fund for its own workers is intragovernmental, not revenue.
   - TRICARE and the VA continue under `-11`, so their outlays are not removed at all.
   - HLT-7.22 also lists "FEHB's employer share" as a stream, while HLT-7.26 has the government pay the contribution (`4-specification.md:100`, `:104`). That is the same money twice in the text.

   Size it with the model's cell shares, or label it as a known overstatement of the contribution and the employer savings. It does not change a decision now.
4. **States' payments are offsetting receipts.** Netting them in the spending row is the usual treatment. Label the row so that F-1's mechanism, once chosen, books the same way.
5. **The legacy FY2040 sum.** It is $570 billion, not $569 billion (C-6). The plan-wide arithmetic at `6-cost.md:129` moves by $1 billion.

### M. Missing populations

**M-1. The territories. Blocking.**
- **The gap.** HLT-7.01 entitles "every person who lives in the United States" (`4-specification.md:47`). No section mentions the territories (a search of `dossiers/care/` finds no "territor" or "Puerto"). The coverage model is built on CBO's 50-state baseline.
- **Why it matters.** About 3.5 million people live in the five inhabited territories, most of them in Puerto Rico (Census Bureau; not yet in the register). Their Medicaid runs under a capped federal allotment, and their Medicare Advantage share is high. Whether they are in the plan, on what date and with what local payment is an eligibility and cost commitment. Point 3's "every resident" points to inclusion, and the specification has to say it.
- **The fix.**
  - Section 4: state the territories' entitlement and wave (Medicaid enrollees with wave 2 would follow the design), and how the territories' share works in place of HLT-7.17's state payment.
  - Section 6: price it as an item outside the model total, with a range. Add the population and allotment figures to the register.
  - Section 9: "everyone who lives here" then holds.
  - This follows from point 3, so it needs no new decision from Espen unless the cost is large enough to make it mainly a money choice.

**M-2. Groups the specification does not place. Not blocking.** Each needs a sentence in section 4 or 5, not a decision:
- **Dual eligibles** (people on both Medicare and Medicaid). Their Medicare moves at the endpoint and their long-term care stays in Medicaid (HLT-7.07). The state payment formula (HLT-7.17) should say whether a state's spending on duals' Medicare cost sharing, which ends, counts in "own current Medicaid spending for them".
- **State and local government employers.** They are employer groups and would pay HLT-7.18's contribution. A nondiscriminatory federal levy on states as employers is generally permitted (*South Carolina v. Baker*, 1988), but section 4 should say they are covered, and section 6 should confirm their premiums are in the model's employer cell.
- **Collectively bargained and multiemployer plans.** Wave 2 moves them by firm size, but a multiemployer plan has no single firm size. Contracts that traded wages for health benefits run past cohort dates. Section 5 should say how cohorts are set for these plans and whether the contribution is owed under a contract in force.
- **Employer retiree coverage.** Pre-65 retirees on employer plans are not in a stated wave. Post-65 retiree wraparounds end at the endpoint as duplicative (HLT-7.23). Whether the contribution's base-year premium includes retiree coverage is not stated.
- **People in prison or jail.** Medicaid's inmate exclusion and the plan's "every resident" are not reconciled. State whether the plan pays for care of incarcerated people or the custodial authority does, as now.

Housing's review asked the same of each population, and transportation's found paratransit riders and tribes missing. These are in the same class.

### O. Optimistic assumptions

**O-1. Wave 1: size, time and the readiness report's date. Not blocking.**
- **Size.** Wave 1 moves the uninsured (about 27 million after restoration), the individual market (20 million), about 37 million children with employer coverage and Medicaid's and CHIP's children, plus Medicare at 60, on January 1, 2031 (`5-delivery.md:33`). That is over 100 million people.
- **Time.** The move comes about two years after an act passed in 2029 under a rules reform not yet made. Medicare's 1966 launch moved 19 million people, most already in Social Security's records (`5-delivery.md:20`, EV-CAR-310). The dossier says wave 1 is "several times" that.
- **Section 8's fallback is narrow.** It covers only employer-covered children (`8-change-our-minds.md:10`).
- **The readiness report's date.** The report that would trigger the fallback is dated July 2029 (`5-delivery.md:41`; `8-change-our-minds.md:41`). That is 18 months before the date, but it may come before the act is law, or just after.
- **Why not blocking.** The dates are decided (`DEC-2026-11-10-09`, memo 2), and a delay needs a vote by design. The point is that the safety valve is mistimed.
- **The fix.**
  - Date wave 1's readiness report from enactment (for example, nine months after) as well as from the wave date.
  - Add to section 8 a second fallback step, moving the individual market or Medicaid's children a year later.
  - Section 9 should say "unless Congress votes to delay it" next to the 2031 date, as it does for the steps in general (`9-public-case.md:50`).
  - Investigation: none now. The readiness report is the "study in implementation" for the 2031 date.

**O-2. Hospital revenue, read on national averages. Bounded; not a defect.** Section 6 part 3 gives the range (about 4% lower to 1% higher after the glide), names its basis, and asks for hospital-level data before the fund's formula is set (2032). That is a clearly bounded uncertainty under `DEC-2026-11-10-07`. Two notes:
- the "low reading" is the one section 8 ties to raising the 1.15 target (`8-change-our-minds.md:12`), and that is the link a reader needs;
- section 9's hospital answer says the gains come "from patients who were on Medicaid or uninsured" (`9-public-case.md:46`), leaving out today's Medicare patients, about $126 billion of the gain.

### A. Cheaper alternatives

Within the decided design, the dossier already compares the cheaper option where one exists: the fund against a slower glide (part 3), copays against none, and states' and employers' shares (part 6). Two notes, neither blocking:
- **A-1. Medicare at 60 in wave 1** (HLT-2.04, decided). Its uninsured and individual-market members are already in wave 1, so what remains is a choice for 60-64-year-olds with employer coverage. That is priced as an upper bound of about $13 billion a year through FY2034 (`6-cost.md:51`). It adds a separate entitlement category for four years. The consequence (cost and one more rule set, against the design lens) should be stated in section 4's design-lens table, which lists every other added requirement. Not argued here.
- **A-2. Ending the disability waiting period** (HLT-2.03). The cost rests on one 2009 Mathematica figure (EV-CAR-344, flagged uncorroborated). The Commonwealth Fund brief behind EV-CAR-342, fetched in this review, quotes CBO's estimate: $6.8 billion in the first year (2011) and $110 billion through 2019. That is a second, independent anchor for the working range. Add it as an entry.

### W. Weak evidence

**W-1. EV-CAR-340 and 342, checked against the originals. Pass.** Both were fetched on November 10, 2026. The CBO report (January 2022, publication 57778) contains all three of EV-CAR-340's anchors verbatim, and the statement is faithful. The same page also finds that a provider's share of Medicare and Medicaid patients is unrelated to commercial prices, which contests the "cost shifting" explanation, and the entry's context already notes this. The Commonwealth Fund brief (Guterman and Drake, May 2009) contains EV-CAR-342's anchor verbatim. Both entries can drop the "from search extracts" caveat (`4-specification.md:198`). The catalog rows stay citation-only, since the rights and the download refusals are unchanged.

**W-2. The legal basis for HLT-7.23 and HLT-7.17 is asserted, not registered. Not blocking at L3; needed before L4.** Section 8 states two legal conclusions without entries (`8-change-our-minds.md:25-26`), and the register has no entry for either:
- *NFIB v. Sebelius* (567 U.S. 519, 2012): the Spending Clause holding for F-1, and the taxing-power holding for HLT-7.18's contribution.
- The commerce-power basis for ending duplicative coverage:
  - *United States v. South-Eastern Underwriters Association* (322 U.S. 533, 1944) holds that insurance is interstate commerce;
  - the McCarran-Ferguson Act (15 U.S.C. 1012(b)) leaves insurance regulation to the states unless a federal law "specifically relates to the business of insurance". HLT-7.23 should say expressly that it does.

The sentence "regulating health insurance sold across state lines" is narrower than the doctrine and should be restated. Note too that NFIB's commerce holding limits compelling people to buy coverage, not prohibiting a sale, so HLT-7.23 sits on firmer ground than the 2012 mandate. Investigation: the L4 legal review. It informs bill drafting, not a choice, and does not block one now.

**W-3. Citation-only entries in sections 4-9.** The subagent counted 44 citation-only entries cited in sections 4-9. In the 330-350 block, EV-CAR-338 (87 rural closures and 68 conversions), 343 and 344 were not checked against originals. They are load-bearing for HLT-7.15's case and for HLT-2.03's cost. Check them as W-1 did. Not blocking.

**W-4. The scope of "end the Hyde Amendment in general".** RTS-2.02 lists the Labor-HHS, FEHB, D.C. and State-Foreign Operations riders, 10 U.S.C. 1093, the IHS cross-reference, CHIP's limits and 42 U.S.C. 18023 (`4-specification.md:125`). Section 4 should say whether `DEC-2026-11-10-11`'s "in general" also reaches three further limits; the reviewer has not checked the current act's section numbers:
- the Commerce-Justice-Science act's limit on abortion for people in federal prisons;
- the Peace Corps limit;
- Title X's section 1008 (42 U.S.C. 300a-6).

The Helms amendment (22 U.S.C. 2151b(f)) is foreign assistance, and section 4 should say it is out of scope if it is. 42 U.S.C. 18023 and the FY2026 riders need entries (already listed at `4-specification.md:192`). Not blocking.

### E. Section 9 against sections 1-8

Every number in section 9 appears in sections 1-8 with its evidence ID or as labeled project arithmetic, and "on our estimates" is used where it should be. The fairness claim carries its condition (`9-public-case.md:40`, `:65`).

**E-1. The size of the new taxes is missing. Blocking.**
- **What the brief says.** "How it's paid for" (`9-public-case.md:21`) gives the premiums removed ($1.5 trillion from households, $1.5 trillion from employers) and the national saving, then says "New taxes fill the rest".
- **What sections 1-8 say.** The rest is about $2.4 trillion a year in 2032 terms after the employer contribution, and about $3.7 trillion in FY2040 (`6-cost.md:112`; `7-validation.md:36`, `:70`).
- **Why it matters.** A reader of the brief cannot see the figure that section 7 says sank Vermont, while the answer to "Will my taxes go up?" (`:40`) gives none either. Section 9 is not ahead of sections 1-8 here; it hides what they say. Housing's W-1 and E-1 blocked for a fiscal pass stated without its conditions, and this is the same class of defect.
- **The fix.**
  - State it in the brief and in the tax answer: "on our estimates, about $2.4 trillion a year at full scale (2032), about the same as the premiums households and employers stop paying".
  - Add a can-say row.
  - Carry F-2's and F-3's corrections into the figure if they land first.

**E-2. Smaller points. Not blocking.**
- "The gap is mostly prices" (`:11`) cites EV-CAR-131 only; section 1 rests it on EV-CAR-129 and 131 (`1-problem.md:15`).
- The 58% of collections is dated 2022 (publication year) against a 2021 fact date (EV-CAR-117).
- The source table's row for the 29% omits `1-problem.md:34`.
- The hospital answer omits today's Medicare patients (O-2).
- The 2031 promises need "unless Congress votes to delay it" beside them (O-1).

### Design lens (`DEC-2026-11-09-13`)

The design is strong on the lens:
- enrollment and renewal from records;
- no work requirement;
- copays from tax records, with no record meaning no copay;
- one formula per state, not per person;
- the contribution on the payroll deposit, with non-offering firms paying nothing;
- readiness reports as published counts, not gates.

Section 4's burden table (`4-specification.md:149-158`) does what the template asks. Two minor gaps:
- Medicare at 60's separate category (A-1) is missing from the table;
- the transition fund's claim is listed, but its 5% loss test needs a revenue baseline for every hospital, which CMS must build. Section 5 should name that build (it already plans the 2032 cost-report publication).

### C. Consistency and record

- **C-1. Section 3 not brought up to date.** `3-design.md` needs these changes:
  - line 3 still says "Nothing here is adopted until Espen decides";
  - the cost table at line 34 gives the 2037 endpoint's figures and "memo 2's order, which moves employer groups last";
  - line 39's FY2040 figure (about $5.5 trillion) is the project-central variant, not section 6's $4.7 trillion;
  - line 74 says single-payer "in about eight years from enactment" (2029 to 2035 is six);
  - `DEC-2026-11-10-12` is not cited;
  - there are no "Decided" lines on the forks and points. The template asks for them, and housing's review counted their absence.

  Replace the stale lines and add a "Decided" line to each memo row and point, citing `-09`, `-11` and `-12`.
- **C-2. The README is stale.**
  - Line 3 says "every care item is at L1"; thirteen health rows are now L2.
  - Line 19's agenda list omits HLT-7, HLT-8 and RTS-2.
  - Lines 27, 28 and 35 say section 3 is "for Espen", the model is "in review (#201)" and the milestone review is "next".
- **C-3. Memo record.**
  - `memos/README.md`, the batch index the template asks for, does not exist.
  - Memo 4's status line (`memos/4-benefits.md:3`) does not cite `-11` item 4, which added abortion and reproductive care to its benefit.
  - Memo 5's status line does not cite `-11` (the softened transition) or `-12`, whose decision-log row names memo 5 as its home.
- **C-4. Provision labels.**
  - HLT-7.14 (Advantage ends) is labeled "decided, point 5", but point 5 is the Advantage payment fix. The end of Advantage follows from memo 1 B and HLT-7.23.
  - HLT-7.22 and HLT-7.26 carry FEHB's employer money twice (F-4).
- **C-5. Never-cited entries.** EV-CAR-334 is never cited; cite it or drop it.
- **C-6. The legacy FY2040 sum.** `6-cost.md:123` prints $569 billion for rows that sum to $570 billion.

## For Espen

Nothing new. No finding is a real fork:
- F-1's mechanism is a drafting and legal choice that follows from memo 3 B.
- M-1's territories follow from point 3 ("every resident").
- The rest are corrections.

If the enforceable form of the states' payment, or covering the territories, turns out to cost materially more, that is a money question for the financing settlement under `DEC-2026-11-10-05`. It would come to Espen only as such.

Board question 0i (the hospital transition fund) stays with Espen. This review found nothing that changes its framing. The national-average basis is stated, and hospital-level data is planned before the fund's formula is set.

## What the next steps should do (for the lead)

In order. Steps 1 to 3 clear the blockers.

1. **The states' payment** (F-1, W-2's *NFIB* entry).
   - Choose one enforceable mechanism and write it the same way in sections 4, 5, 6 and 8 and in HLT-7.17's provision.
   - Add the *NFIB* and Part D clawback entries.
   - Tier: Most capable (legal and design). Routine PR.
2. **The territories and the unplaced groups** (M-1, M-2).
   - Section 4: the territories' entitlement, wave and local share; a sentence each for duals, state and local employers, multiemployer and bargained plans, retirees and incarcerated people.
   - Section 6: the territories priced outside the model total, with a range.
   - Register entries for the population and allotment figures.
   - Tier: Most capable for the provisions; Standard subagent for the entries. It can share a PR with step 1.
3. **Section 9** (E-1, E-2), after steps 1 and 2 and step 4's numbers if those land first.
   - Give the new taxes' size in the brief and in the tax answer, with a can-say row.
   - Make the source-table and tag fixes; give the hospital answer's Medicare gains; put "unless Congress votes to delay it" beside 2031.
   - Tier: Most capable.
4. **Section 6's basis** (F-2, F-3, F-4 items 3 and 5, C-6).
   - Put fiscal-year phasing in `health_path.py`, and re-run sections 4, 6, 7 and the README from it.
   - Label the exclusion revenue as CBO's convention, with the half pass-through row.
   - Label the TRICARE, veterans' and FEHB overstatement, or size it.
   - Fix the $570 billion sum.
   - Tier: Standard (code and tables to this spec), checked by a Most capable session. It can run in parallel with step 1.
5. **The booking PR** (F-4), the lead's separate tier-3 PR.
   - Book on step 4's fiscal-year path.
   - Split HLT-4, retiring children's continuous coverage and Medicaid dental from each wave.
   - Keep the contribution and FEHB money off the revenue side.
   - Tier: Most capable. Espen's label, with Codex's review requested by comment as for budget-model integration. After step 4.
6. **Delivery and evidence** (O-1, A-1, A-2, W-1, W-3, W-4).
   - Date wave 1's readiness report from enactment, and add section 8's second fallback step.
   - Add Medicare at 60 to the burden table, and CBO's disability-wait estimate as an entry.
   - Drop the "search extracts" caveat for EV-CAR-340 and 342.
   - Check EV-CAR-338, 343 and 344 against their originals.
   - Settle RTS-2.02's scope list.
   - Tier: Standard (Most capable for the RTS-2 scope).
7. **Record fixes** (C-1 to C-5).
   - Bring section 3 up to date with "Decided" lines.
   - Update the README status and agenda list.
   - Write `memos/README.md` and memo 4 and 5's status lines.
   - Fix HLT-7.14's label; cite or drop EV-CAR-334.
   - Tier: Standard (Light for the README and memo lines). It can share a PR with step 6.
8. **A short L3 re-check** by a reviewer, limited to F-1, M-1, E-1 and F-2's re-run. Then the lead moves the health rows (HLT-1, 2, 6, 7, 8, A1, A2, A4 and RTS-2) to L3 in `agenda/agenda.csv` and the README. HLT-7.15 moves when Espen answers question 0i.
