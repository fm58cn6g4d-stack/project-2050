# Memo G5: D2 and the wealth tax: balance with them, or hold a backstop

**Decided:** B, `DEC-2026-11-20-09`; its backstop steps are redrawn without a VAT in memo G13 (A, `DEC-2026-11-24-08`), whose text is in `../2-settlement.md` part 7.1. Booked in stage G step 7 (`../2-settlement.md`, `models/data/inputs/settlement.json`). The memo below is the record of the choice as put to Espen; its figures are the draft's.


Role: decision memo for Espen, fork 5 of stage G's batch ([`README.md`](README.md); [`../2-settlement.md`](../2-settlement.md) parts 3 and 5; `../1-audit.md` part C, items 4 and 13). Status: **provisional, drafted on the recommendation, November 20, 2026.** Not decided, not booked. Nominal $B on case `mixed`, priced by `models/tools/financing-protection/packages.py`. Project arithmetic on exploratory models, not official scores.

## The question

Two of the plan's largest money lines could fail for reasons outside the plan's control.

- **D2, the national health budget** (`DEC-2026-11-15-08`), holds the single plan's spending growth to GDP plus 1 point from 2037. It saves **$249.4B in FY2040, $324B in FY2045 and $526B in FY2056.** No country has held health spending to that path for long with a system of this size [EV-CAR-742]. Espen asked that stage G always report the gap without it.
- **HS2, the wealth tax** (`DEC-2026-11-15-16`), raises **$149.9B in FY2040 and $287B in FY2056.** Its legal risk is high. Most scholars read a wealth tax as a direct tax that the Constitution requires to be apportioned among the states by population, and the Supreme Court left that question open in *Moore* (2024). Its drafted fallback, a deferral charge on unrealized gains, mostly reaches the same base as G11, so it recovers little.

If both failed, the general-fund gap after the recommended package would be about **$396B in FY2040 and $811B in FY2056** (`../notes/settlement-results.md`, the risk table). That is about 4.4 points of memo G3's VAT in FY2040 and 5.1 points in FY2056. On the backstop's full trigger the VAT would be about **7.3% in FY2040 and 9.7% by FY2056**, against the package's 2.95% and 4.6% (the review's F-2).

The question: should the package balance to the figure *with* D2 and HS2 and hold a backstop in case either fails, or balance now to a figure without them?

## The options

| | What | Cost now | What happens if D2 or HS2 fails |
| --- | --- | --- | --- |
| A | Balance with both; report the without figures; no backstop | None | Congress has to find $150-400B a year then, with no plan for it |
| **B (recommended)** | Balance with both, and enact a **contingent backstop** with the plan: named steps that switch on only on a published finding | None unless triggered | The backstop switches on: up to about 2.7 VAT points for D2 (FY2040 terms), and HS2's deferral charge plus up to 1.6 VAT points for the wealth tax |
| C | Balance now to the gap without D2 | About +$249B a year from FY2040 (2.7 VAT points), rising to $526B in FY2056 | Already covered |
| D | Balance now to the gap without both | About +$400B in FY2040 (4.4 points), about $811B in FY2056 | Already covered |

**A, report only.** It costs nothing until something fails. But then the plan is $150-400B a year short with no agreed way to close it, and the pressure would fall on health, which Espen wants protected.

**B, a contingent backstop (recommended).**
- *The trigger for D2:* the plan's fund trustees publish each year whether health spending stayed within GDP plus 1. If it runs more than 0.25% of GDP above that path for two years running, the backstop's first step takes effect the next January.
- *The trigger for HS2:* a final court ruling against the wealth tax switches on its fallback (the deferral charge) and the VAT step at once.
- *The steps are in law from the start,* so markets and budget scorers see a funded plan. Congress can replace a step with something else by passing an alternative of equal size.
- *Bridging:* health's early surplus, if held as a reserve (memo G6), is about $0.66T plus interest. The general fund covers health's FY2035-39 call in the package, so the reserve is held for D2 and the backstop only, not spent twice (the review's F-8). It covers roughly two to three years of a D2 shortfall while a step phases in.
- *Legal footing* (the review's F-7): Congress sets the rate and the trigger, and an officer finds the fact. That is contingent legislation of the kind the Supreme Court upheld in *Field v. Clark* (1892) and *J.W. Hampton v. United States* (1928). If a trustees' finding were challenged, the statute should say the step takes effect by default on its date. With no VAT, the steps are redrawn in the health contribution by memo [G13](G13-backstop-without-vat.md) (A, `DEC-2026-11-24-08`), and step 7 wrote them into the settlement's specification (`../2-settlement.md` part 7.1).
- *What it doesn't cover:* the yield risks (the top end's response, the old scores, the VAT's own yield) have no backstop. Together they are about $313B in FY2040. A miss there falls on a later Congress, unless memo G8's margin option is taken.
- *Burden:* none unless triggered. It is one published annual comparison, which the trustees already need for D2 itself (design lens: published counts with a review trigger, `charter/STANDARDS.md`).

**C, balance without D2 now.**
- *Cost:* households pay about 2.7 more VAT points from the start. In FY2040 that is about $2,650 a year for a fourth-fifth household, and $1,000 for the bottom fifth, to insure against a risk that may not come.
- *What it buys:* certainty.
- *Side effect:* it removes the plan's own pressure to make D2 work. The national health budget's credibility partly rests on there being no automatic money if it fails.

**D, balance without both.** The same as C, plus about 1.6 more points for the wealth tax.

## Recommendation

**B.** Balance to the gap with D2 and HS2, which are both decided, and enact the backstop with the plan.
- It costs households nothing unless a risk comes true. When one does, the money is already agreed, so health isn't the line that gets cut.
- It keeps the national health budget's discipline: the backstop is a tax step everyone can see, not quiet extra money for the plan.

**What would change this:** if Espen prefers certainty to discipline, then C for D2 alone. D2 is the larger and longer-lasting risk, and the wealth tax's failure would be known within a few years of enactment.

## Question for you

**G5.** Balance the package with D2 and the wealth tax counted, and enact a **contingent backstop** that switches on only if D2 misses its path or the wealth tax is struck down (B, recommended)? Or report only (A), or balance now without D2 (C) or without both (D)?
