# Memo G8: The health contribution over time

Role: decision memo for Espen, fork 8 of stage G ([`README.md`](README.md); [`../2-settlement.md`](../2-settlement.md) parts 3 and 7). Status: **held November 24 (`DEC-2026-11-24-13`), then replaced by memo [G18](G18-g8-with-a-debt-goal.md) D′ (`DEC-2026-11-25-04`): the step-down comes only on two years of certified surplus beyond the debt goal's path, never below 3.25%.** Kept as the record of the choice. The first draft (#469) asked how to step a VAT up over time; you turned down a VAT (`DEC-2026-11-20-07`), so this redraft asks the same question about the instrument that replaced it, the health contribution's base rate. Nominal $B on the budget model's case `mixed` with the settlement booked (`models/data/inputs/settlement.json`; `../notes/booking-results.md`). Project arithmetic on exploratory models, not official scores.

## The question

The fiscal rule tests the general fund in FY2040 **and every later year**. The settlement closes them with one health contribution base rate, **3.80% from the January 2035 endpoint** (it was 2.25% before stage G; G2 C made it 3.25%; the fallback adds the rest).

One rate is more than the later years need. The rate each year would need on its own:

| | FY2040 | FY2042 | FY2045 | FY2050 | FY2056 |
| --- | --- | --- | --- | --- | --- |
| Base rate that closes the year | 3.77% | **3.80%** (the tightest) | 3.70% | 3.38% | 3.32% |
| Gap at 3.80% ($B; − is a surplus) | −6.0 | −0.4 | −26.4 | −143.2 | −205.4 |

Why the need falls: from FY2037 defense is held flat in real terms (G10 C), so it shrinks as a share of a growing economy, and that saving grows faster than health's costs. By FY2056 the general fund runs about $205B a year ahead.

The question: should the rate stay where FY2042 needs it, or come down as the surplus arrives?

**What hasn't changed from the first draft:** health's costs still grow faster than the economy (D2's GDP plus 1 point, and long-term care), so the package's margin in FY2040-44 is thin under every option here: $0.4-6B a year. None of these options adds margin there.

## The options

Each keeps FY2040-56 closed on the central estimate. "Workers ahead" is health's take-home test with everything counted (G2b, the reading you chose), at that year's rate; today's test year is FY2040, so later rates are shown at FY2040's population as a guide.

| | What | Rate path | FY2030-39 gap | Debt, FY2056 (baseline 180.2%) | Workers ahead at the later rate |
| --- | --- | --- | --- | --- | --- |
| **A** | **Steps down set in law** on fixed dates | 3.80% from 2035; 3.65% from FY2046; 3.40% from FY2051 | +$458.5B | 134.6% | 71.1%, then 74.5% |
| B | **A lower start that steps up** | 3.25% FY2035-39 (G2 C's fold alone); 3.80% from FY2040 | +$1,002.8B | 134.4% | 69.0% (76.2% before 2040) |
| C | **One fixed rate; the surplus pays down debt** | 3.80% from 2035, no step | +$458.5B | 133.1% | 69.0% |
| **D (recommended)** | **A fixed rate that steps down only on a finding** | 3.80% from 2035; a 0.25-point step down when the trustees certify a general-fund surplus above 0.1% of GDP for two years running, never below 3.25%; on the central estimate, one step, to 3.55% from FY2049 | +$458.5B | 134.1% | 72.5% from FY2049 |

**A, steps down on fixed dates.**
- *For:* households get the money back on a known schedule as the defense saving builds. From FY2051 the rate is 0.4 points lower than C: for a household with $60,000 of income above the exemption, about $240 a year.
- *Against:* the steps are written now on a 2040s forecast. If D2 or a yield misses, a step that was scheduled anyway would reopen a gap the backstop then has to close: the backstop raises the same rate that A has just lowered.
- *Leaves:* no surplus to speak of by FY2056 ($34B), so no room for the risks the backstop doesn't cover (the top end's response and the old scores, about $248B in FY2040 together; `../2-settlement.md` part 5).

**B, a lower start that steps up.**
- *For:* the rule doesn't test FY2035-39, so households could pay G2 C's 3.25% for the first five years after the endpoint. About 76% of workers are ahead then, against 69%.
- *Against:* it adds about **$544B of deficits over FY2035-39** (the decade figure goes from +$458B to +$1,003B) and 1.2 points to debt in FY2040. The plan's 2030s already run short in FY2036-39, and the G6 reserve ($250B) is sized for health's transition risk, not for this. And a rate that rises in 2040 is a tax increase a later Congress has to let happen.

**C, one fixed rate.**
- *For:* the simplest. Debt falls furthest (133.1% of GDP in FY2056, the lowest here), which lowers interest, the point you made in choosing cuts first. The later surplus is a cushion for the risks with no backstop.
- *Against:* by the 2050s households pay about 0.45 points more than the rule needs, about $200B a year, with nothing in law to give it back.

**D, a fixed rate that steps down on a finding (recommended).**
- *How it works:* the plan's fund trustees already publish each year how health spending ran against D2's path (memo G5's trigger). They would also publish the general fund's balance under the rule. When it has run a surplus above 0.1% of GDP (about $60-70B in the late 2040s) for two years running, and no backstop step is in force, the base rate falls by 0.25 points the next January. It never falls below G2 C's 3.25%, and a step that would reopen the year's gap on the trustees' own projection is skipped.
- *On the central estimate* that is one step, to 3.55% from FY2049. A second step, to 3.30%, would reopen FY2053-56, so it doesn't happen.
- *For:* it gives the surplus back only once it is real, not forecast, and keeps a 0.1%-of-GDP margin before anything is returned. It works the same way as the backstop in reverse, with the same trustees and the same published counts (design lens: published counts with a review trigger), and the same legal footing: Congress sets the rate, the step, the trigger and the floor, and the trustees find a fact (*Field v. Clark*, 1892; *J.W. Hampton v. United States*, 1928).
- *Against:* households wait longer for the money back than under A, and the 2050s rate (3.55%) is above what the rule needs (3.3-3.4%). Debt in FY2056 is 1 point higher than C.

## Recommendation

**D.** Hold 3.80% until the surplus has shown up in two years of actual results, then step down a quarter point at a time, never below 3.25%.
- It returns money to households only when it exists, which A doesn't guarantee.
- It keeps a margin first, which C keeps without limit and A doesn't keep at all.
- It doesn't borrow $544B in the late 2030s, which B does.

**What would change this:**
- If you weigh lower debt and interest above the later rate, then **C**.
- If you want households to see the step-down written in law now, then **A**.
- If the 2035-39 take-home matters more than the decade's deficits, then **B**.

## What step 7 booked, and why

The booking needed a rate path. It books **one rate, 3.80% from 2035, with no step**, labeled in `settlement.json` as a working assumption for the later years. That is C's path, and D's path before any finding. **No G8 choice is booked:** D's conditional step isn't booked because it rests on a finding that hasn't happened, and A's steps aren't booked because you haven't chosen them. Choosing A, B or D changes the booked path from FY2046, FY2035 or FY2049, and nothing in FY2040-45.

## Question for you

**G8.** Hold the health contribution at 3.80% from 2035 and step it down a quarter point only when the trustees certify two years of surplus above 0.1% of GDP, never below 3.25% (D, recommended)? Or step it down on fixed dates (A), start at 3.25% and step up in 2040 (B), or keep one rate with the surplus paying down debt (C)?
