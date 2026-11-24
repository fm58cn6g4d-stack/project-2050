# Memo G10: The defense path

**Decided:** G10.1 C, `DEC-2026-11-24-01`; G10.2 B, `-02`. Booked in stage G step 7 (`../2-settlement.md`, `models/data/inputs/settlement.json`). The memo below is the record of the choice as put to Espen; its figures are the draft's.


Role: decision memo for Espen, fork 10 of stage G, from step 4b's whole-budget scan ([`../3-budget-scan.md`](../3-budget-scan.md) parts B and C; results in [`../notes/budget-scan-results.md`](../notes/budget-scan-results.md)). Status: **provisional, drafted on the recommendation, November 20, 2026. A new fork.** Not decided, not booked. Nominal $B on case `mixed`, priced by `models/tools/financing-protection/budget_scan.py` against the settlement as you decided it, with no VAT. Project arithmetic on exploratory models, not official scores.

## The question

You turned down a VAT and asked for cuts and reallocations across the whole budget (`DEC-2026-11-20-07`). After your other answers the plan is **$262B short in FY2040 and $728B short in FY2056.**

Defense is the largest area of the budget the plan hasn't touched.
- It is $1,232B in FY2040, 2.27% of GDP, on CBO's baseline.
- The plan books it at $0. Its rule, NSC-1A, holds defense "roughly flat in real terms" from whatever FY2029 enacts, through FY2039, and that is about what CBO's baseline already assumes (the project's national-security file) [EV-FIN-013].
- In October you asked for "ways to reduce defense over time" (the same file, open item 1a). This memo is that study's first pass.

Two questions:
- **G10.1:** how far to bring defense down.
- **G10.2:** what to do if Congress raises the base in 2027-28.

## What CBO's baseline already does, and what it doesn't

- **To FY2036, CBO grows defense with inflation from the FY2026 level.** As a share of the economy that is already a decline: from 2.61% of GDP in FY2029 to 2.35% in FY2036. The lowest share since at least FY1962 was 2.91%, in FY1999 and FY2001 (CBO's historical data). The baseline is already below that from FY2026 (2.73%), so it is already historically low.
- **After FY2036, the baseline grows defense with the economy,** at 2.27% of GDP every year. That is a scoring convention for the long-term outlook, not a law or a plan.
- **NSC-1A says "flat real through FY2039".** So for FY2037-39 the model counts more defense than the plan's own rule allows. Correcting that is a pricing fix ($40B over the decade), not a choice. Holding the rule after FY2039 is the choice.

## The options (G10.1)

The FY2040 and FY2056 columns are defense alone. The "R needed" and "workers ahead" columns include the farm, tax and housing items of memos G11, G12 and G14 at their recommendations. "R" is the health contribution's base rate (the fallback) that would close every year from FY2040 to FY2056 with one rate; you decided 3.25% for the fold (`DEC-2026-11-20-06`). "Workers ahead" is health's take-home test with everything counted (G2b).

| | What | FY2040 | FY2056 | Defense, % of GDP (FY2040 / FY2056) | R needed | Workers ahead |
| --- | --- | --- | --- | --- | --- | --- |
| A | As booked: CBO's baseline | 0 | 0 | 2.27 / 2.27 | 4.85% | 56.8% |
| B | NSC-1A held after FY2039: defense flat in real terms from FY2037 | −41.9 | −541.5 | 2.20 / 1.71 | 4.1% | 64.9% |
| **C (recommended)** | **B, plus a named restructuring about 5% below that path by FY2033** | **−101.4** | **−623.3** | **2.09 / 1.62** | **3.85%** | **68.2%** |
| D | CBO's deepest topline option: about 10% below the baseline, keeping its growth with GDP | −123.2 | −217.7 | 2.04 / 2.04 | 4.3% | 62.6% |

### A. As booked

No change. The fallback rate has to be about 4.85%, and 56.8% of workers come out ahead.

### B. NSC-1A held after FY2039

- *What changes:* defense keeps growing with prices after FY2036, as NSC-1A already says through FY2039, instead of with the economy.
- *Who loses:* no one in dollars. It is the same real budget as FY2036 every year after. But the costs inside defense, pay and health care above all, grow faster than prices, so a flat budget buys a gradually smaller force. CBO's 2025 projection of DoD's own plans had their costs growing about 11% faster than inflation over the following ten years (via a search extract).
- *Strategic cost:* by FY2056 defense would be 1.71% of GDP. That is lower than any year since at least 1962, and far below the 5% (3.5% core) NATO's members agreed in 2025 [EV-FIN-013].

### C. B plus a named restructuring (recommended)

- *What changes:* about 5% below B's path, phased in over FY2031-33. It cuts no one's pay; it changes what is bought:
  - **The nuclear plan:** keep all three legs, but extend today's Minuteman III missiles for part of the force instead of buying every new Sentinel, and defer or drop the new nuclear cruise missiles. Nuclear forces are about $95B a year on CBO's estimate (CBO, through Breaking Defense, 2025) [EV-FIN-004].
  - **Missile defense held to research:** no fleet of space-based interceptors. CBO prices the notional "Golden Dome" at nearly $1.2T to build and run, most of it 7,800 interceptors in orbit (CBO, through The War Zone, 2026) [EV-FIN-005].
  - **The weapons mix:** fewer of the programs with the worst cost growth. GAO found 46 of 72 major programs reporting cost increases totaling $122B (GAO, through Defense News, 2026) [EV-FIN-010].
  - **Service contracts and headquarters:** fewer of both, checked by the audit DoD has never passed (Defense News, 2025) [EV-FIN-012]. Not by the kind of savings claims DOGE made, most of which GAO couldn't verify (GAO, 2026) [EV-FIN-007].
  - **TRICARE fees for working-age military retirees,** at CBO's option's levels, until the single plan covers everyone in 2035.
- *The 5% is a working assumption, not a score.* No independent estimate of this package exists. The benchmark is CBO's own deepest topline option, about 10% below the baseline, about $1T over ten years (CBO, through Fox Business, 2024) [EV-FIN-006]. The range is 3-7%: −$90B to −$156B in FY2040 with the other items.
- *Who loses:*
  - defense contractors and the places that build these systems; the ICBM and cruise-missile work is concentrated in a few states;
  - military retirees under 65, through higher TRICARE fees until 2035;
  - and the strategic margin, as in B.
- *How it holds:* defense is appropriated every year, so only Congress holds it. The plan uses the machinery Congress has used before: statutory caps on defense budget authority, as in the Budget Control Act (2011) and the Fiscal Responsibility Act (2023), with emergency money only for a declared emergency.
- *What it buys:* the largest saving in the long run, which is when the plan's costs grow fastest. It brings the fallback rate down from 4.85% to 3.85%.

### D. CBO's topline option

- *What changes:* about 10% below the baseline from FY2034, mostly through a smaller force, but with the baseline's growth with GDP kept.
- *Compared with C:* it saves more in the 2030s (−$822B over FY2030-39, against −$475B) and much less later (−$218B in FY2056, against −$623B). So the fallback rate has to be about 4.3%, set by the 2050s.
- *Who loses:* the same groups as C, sooner and harder. Fewer people in uniform is CBO's main lever.

## The FY2029 base (G10.2)

- **NSC-1A takes whatever FY2029 enacts,** leaving out one-time reconciliation money [EV-FIN-013].
- The administration asked for **$1.5T for FY2027**: $1.15T in the regular bills plus $350B through reconciliation (CSIS, 2026) [EV-FIN-009]. Congress's bills are lower, around $1.07-1.1T (via search extracts), but well above CBO's February path, about $0.92T.
- Stage B priced the paths for the Defense bill: $131B to $424B above flat real over FY2030-39 (`dossiers/scenario/compounding-defense.md`).
- **Against today's baseline nothing changes.** But the next CBO baseline will carry FY2027-28's level forward, and NSC-1A would lock it in.

| | What | Effect |
| --- | --- | --- |
| A | NSC-1A as decided: the base is whatever FY2029 enacts | A 2027-28 buildup becomes the plan's base |
| **B (recommended)** | **A ceiling: the plan's base is no higher than CBO's February 2026 path (FY2026 grown with inflation); any excess is phased out over FY2030-32, and any new money is paid for inside defense, as D9 says** | Against a re-based baseline it saves about the excess every year; against today's, nothing |

This is also stage B's open question 0a ("the FY2028 defense path before summer 2027"). If you'd rather answer it then, say so, and the settlement carries A until you do.

## Recommendation

- **G10.1: C.** Defense stays flat in real terms after FY2036, as the plan's own rule already says through FY2039, with a named 5% restructuring that changes what is bought rather than anyone's pay. It closes about $101B in FY2040 and $623B in FY2056, the largest part of what the VAT would have done. It brings the fallback rate to 3.85%.
- **G10.2: B.** A buildup in 2027-28 shouldn't become the 2029 plan's base by default.

**What would change this:**
- **If the strategic risk weighs more than the rate,** then B (no restructuring). The fallback rate is 4.1%.
- **If you'd rather cut sooner and less later,** then D. It saves more in the 2030s, but leaves the long run to the health contribution.
- **If the threat picture worsens by 2029** (a war, or a collapse of arms control), the plan's fund trustees' annual report and the defense caps' emergency clause are the review points. A step back toward the baseline would raise the fallback rate by about 0.2 points per $45B.

## Not recommended, for the record

The scan also looked at these, and doesn't recommend them:
- veterans' disability compensation and VA health care: they are earned benefits for disabled veterans, and VA health care folds into the single plan;
- military retirement: pensions already earned;
- across-the-board cuts to pay or force without a named restructuring: they cut readiness first.

## Questions for you

**G10.1.** Hold defense flat in real terms after FY2036, as the plan's rule already does through FY2039, and restructure it to about 5% below that path by FY2033 (C, recommended)? Or flat real only (B), CBO's 10% topline option (D), or as booked (A)?

**G10.2.** Cap the plan's FY2029 defense base at CBO's February 2026 path, phasing out any 2027-28 buildup over FY2030-32 (B, recommended)? Or keep NSC-1A's base as whatever FY2029 enacts (A), or answer this with stage B's question 0a in 2027?
