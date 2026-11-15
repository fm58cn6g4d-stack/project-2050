# Health financing: household-contribution variants priced November 15, 2026

Role: a working record of the household-contribution variants that the lead priced for Espen on November 15, after Espen approved package E's recommendations (`../../health-cost-review.md`, part 4), so the next lead and the booking worker can pick them up. Status: **exploratory and not reviewed.** These are quick runs by a subagent of the lead session (`session_01UQzgBseNG9rnTV4o1vPqMq`). They layer onto `models/tools/health_cost_review.py` by monkeypatching it, and none is booked. Before any of them is adopted, a worker must rebuild the chosen design properly in `health_cost_review.py`, with tests, and the reviewer must check it.

Files: `price_variant.py` (E, V2/V3, M4/M5), `price_u.py` (U), `price_w.py` (W), `price_x.py` (X), and their JSON outputs. Run them from `models/tools/`. They were written in a scratch directory; check their paths before rerunning.

## Espen's directions (November 15, verbatim, in order)

1. "all health financing recommendations for package E approved, but let's also test the personal contribution at 6% of income above a $40,000 threshold (first 40k only pays the minimal point of care copays and such)". Then: "I meant $40,000 threshold for single, so let's do $80,000 or a bit lower for couple".
2. On the middle ground: "Price middle ground."
3. "The Medicare HI tax of today needs to be folded into a single health tax under the new plan, somehow [...] in practice, most workers have their income tax withheld from their paychecks, anyways. What if we test a version with a single health tax/contribution, and have a collection strategy that is based on a payroll tax for workers but also uses alternate tax collection methods for income outside payroll? Otherwise I'm good with your 4% rec but open to that shifting as it's unified with the existing Medicare HI payroll tax". Then: "We could also test a $30,000/$60,000 threshold?"
4. "Test a unified tax on all pay version, plus an extra charge on high earners like the current Medicare rate structure does [...] I know this will seem to make low wage earners come out worse off, but they pay no copays/other charges at point of care below 200% poverty level, plus you gotta account for not just premiums they pay today they'd no longer pay, but also current out of pocket health costs (uninsured) that they'd save".
5. "what about 4% on all income plus an extra charge above 205/257, plus a low-income exemption to essentially take the place of part of Medicaid".
6. On drugs: "please verify that the drug pricing cost reductions are reasonable and backed by evidence [...] I've seen other estimates of similar bills suggest drug prices could fall as much as 50% but maybe those are overly optimistic?"

**Still open with Espen:** which household contribution replaces package E's "4% above $100K/$200K". The lead recommended **X3** (3% on all AGI, a 5-point surcharge above $205,400/$256,750, the low-income exemption, and HI folded in). It offered 3.5% as a middle way. Espen had not answered when the lead handed over.

## Method (common to all)

- FY2040, package E's cost case ("design": the errors fixed, plus D1, D2 and D5), streams, the small-employer allowance and the worker transition credit.
- Booked revenue closes whatever the household tier leaves, and may go negative.
- Each tier's yield per point is E's above-line yield scaled by the household model's base at the new line. Avoidance is a 20% haircut, all placed in the top fifth. The top 1%'s share is scaled from the legacy 55%, which is a judgement call.
- Lines are indexed as `LINE_HIGH` is (2025 dollars × 1.027).
- The take-home test is `take_home_micro`. From U onward it also counts the worker's 1.45% HI and the 0.9% in today's visible cost. That isn't in the repository's test yet.
- The per-fifth nets in the tool's output are in FY2040 nominal dollars (about 1.377 times the memo's 2026-dollar figures). The table below leaves them out.

## Results (FY2040; booked revenue and the gap in $B; household figures in 2026 dollars a year)

Test household T is a single worker at $72,000 with job coverage. Today's visible cost is $5,679, or $6,692 once its $1,014 of HI is counted (columns U onward).

| Variant | Household tier | Booked revenue taken / plan-wide gap | Workers passing take-home | T: plan (with booked 2 points) | Bottom-four losers, M |
| --- | --- | --- | --- | --- | --- |
| E (approved package) | 4% of AGI above $100K/$200K | 579 / 649 | 90.4% | 1,371 | 1.6 |
| M4 | 4% above $40K/$80K | 288 / 358 | 74.6% | 2,642 (3,688) | 4.7 |
| M5 | 5% above $40K/$80K | 148 / 218 | 69.2% | 2,960 | 5.6 |
| V2 | 6% above $40K/$80K | 8.5 / 78 | 64.6% | 3,277 | 6.7 |
| V3 | 6% above $40K/$70K | −27 / 43 | 63.4% | 3,277 | 7.0 |
| U1 | HI folded in; 6.57% above $40K/$80K | 288 / 358 | 74.0% | 3,417 (4,463) | 5.2 |
| U2 | HI folded in; 5% above $40K/$80K | 507 / 577 | 82.6% | 2,917 | 3.8 |
| U1-30 | HI folded in; 5.77% above $30K/$60K | 288 / 358 | 72.4% | 3,752 | 5.6 |
| U2-30 | HI folded in; 4.39% above $30K/$60K | 507 / 577 | 82.4% | 3,172 | 3.9 |
| W1 | HI folded in; 3.60% of all AGI + 2 points above $205,400/$256,750 | 288 / 358 | 70.1% | 3,948 (4,995) | 7.7 |
| W2 | 3.20% + 4 points | 288 / 358 | 75.2% | 3,662 | 6.4 |
| W3 | 3% + 5.03 points | 288 / 358 | 77.6% | 3,514 (4,560) | 5.7 |
| W4 | 2.25% + 4 points | 507 / 577 | 89.2% | 2,966 | 3.5 |
| X1 | 4% + 5 points + exemption | 84 / 154 | 65.0% | 4,243 (5,289) | 7.3 |
| X2 | 4% + 4 points + exemption | 130 / 200 | 65.3% | 4,243 | 7.3 |
| **X3 (recommended)** | 3% + 5 points + exemption | 308 / 378 | **78.7%** (98.6% below 200% of poverty) | 3,514 (4,560) | **4.5** |

Notes on the results:
- **The exemption** charges nothing at or below 138% of poverty for the household's size, then phases in smoothly to the full rate at 200%: charge = R% × AGI × (AGI/FPL − 1.38)/0.62, with no cliff. It is claimed on the W-4 and reconciled on the return, like the premium tax credit. It costs $25.3B at R = 4% and $19.0B at R = 3%.
- **HI folded in (U, W, X)** means three things:
  - The new contribution replaces $359B a year: the worker's HI ($290B, half of HF's 2.9%), the 0.9% additional Medicare tax ($53.5B, a working estimate from the household model, probably low), and worker HI on former premiums ($16B).
  - On the household model, worker HI is $343B rather than $290B. That would put U1's rate near 6.95%.
  - Employers keep their 1.45%, presented as one contribution with the band rate.
- **H1b interacts with the fold-in.** H1b is the booked rise to 5% above $400K, $62.7B. Folding HI in removes the base of its wage half, so it needs restating as its own surcharge, or folding into the surcharge.
- **Take-home grid, single with job coverage:**
  - M4, M5 and U1 fail from $110K, and V2 from $90K.
  - W2, W3 and X3 pass up to $150K.
  - X1 and X2 fail from $110K.
  - Families pass everywhere in every variant.
- **The booked 2 points on AGI above $20K/$40K,** a charge for the other flagships, aren't in the take-home test. Adding them, singles fail from about $90K in most variants. Stage G should drop or fold this charge if a $40K-type or flat design is adopted.
- **Medicaid workers** pay almost nothing today. Without the exemption, a charge from the first dollar fails about 40-50% of them. With it (X3), 30% still fail, mostly above 200% of poverty or in units where only the children are on Medicaid.

## The drug-price check (the lead's subagent, November 15)

**Conclusion:** D5's 25% is the central estimate on the plan's measure. The range is 15-35%: 35% only if the fallback price (the lower of the VA price and Medicaid's best price) and the formulary bite; 40% is optimistic. 50% is defensible only for brand list prices, or for brand net prices against commercial payers alone.

**The measure:** all-payer net retail drug spending (`sp_drug_cut` on `nhe_rx`, net of rebates). Drugs given in hospitals and doctors' offices sit in the hospital and physician lines.

**The evidence:**
- RAND for ASPE (2024): US brand prices are 4.22 times peers' gross and at least 3.22 times net; generics are 0.67 times.
- CBO's lower-rate case: 23%.
- CMS's first negotiated prices: 22% (2026, 10 drugs) and 44% (2027, 15 drugs), Medicare only.
- What the single-payer studies assumed: Galvani 40% on all drugs; Hwang and Kesselheim 9-49%, against private insurers only; Warren 70% for brands.

**Supply risk:** CBO estimates the IRA means 13 fewer drugs out of about 1,300 over 30 years; H.R. 3, covering the whole market, is the closer comparison.

**What higher cuts are worth:** each point is about $11.5B in FY2040.

**Also:**
- `health-cost-review.md` cites "3.08" for brand prices net of rebates, where ASPE gives "at least 3.22"; check this at booking.
- The plan's design has no compulsory licensing. That could be a later decision memo.

## For the booking PR (beyond `health-cost-review.md` part 5)

- Rebuild the chosen household design in `health_cost_review.py`, and add HI to today's visible cost in `take_home_micro`. **Done in #392** (confirmed at booking: `take_home_micro` counts the worker's HI and the 0.9% in today's cost).
- Restate H1b. **Booked:** its wage half ($43.5B in FY2040) is row HCH, won back in the unified contribution's surcharge (S = 5.96, `DEC-2026-11-15-13`); the investment half stays in H1b.
- Record the 0.9% working figure. **Booked** as row HCA at $53.5B in FY2040, labeled a working figure (probably low: nearer $70B with the CPS's top-coding).
- Update Espen's calculator page (https://claude.ai/artifact/UTnkf4c11ANSxt5BbVcsz9, private; it still shows package A) to the chosen package.
