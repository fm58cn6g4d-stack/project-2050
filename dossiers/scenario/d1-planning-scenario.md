# D1, the planning scenario

Role: the decision in force on D1, "Which scenario do we plan for?", replacing the legacy D1 (`legacy/governing/project-2050-governing-decisions.md`). Status: decided by Espen (`DEC-2026-11-08-01`): Senate option B, and on the House, option 1 as Espen directed on PR #80 (November 8). The legacy file is read-only (`charter/STANDARDS.md`), so the updated decision lives here and the decision log points to it; the options are kept as the memo it was decided on.

## In brief

Two things are settled here:
- **The Senate band:** B, plan for 53-56 seats, keep the 51-seat test, and treat 58 or more as upside (recommended; Espen decides it with the label).
- **The House:** Espen's direction on PR #80 is to plan on a full trifecta in 2029-30, the House included. Other outcomes are modeled and prepared for from 2030 on. So the House stipulation stays (option 1) and no House tag is added.

D2 to D9 do not change.

## The evidence, as of November 8 (main at `7d50150`)

All figures are this project's own scenario models, not forecasts. No rater has published 2028 ratings yet.

- **2026** produced 54 Democratic seats called, likely 55-56 (`1-results.md`). The 2029 Senate is set in 2028, when Republicans defend 19 seats and Democrats 16.
- **The Senate with a Democratic president** averages about 57 seats (90% range 53-60). 55 or more comes in 84% of runs, 60 or more in 9%. Source: `senate-model-2028.md` and `senate-model-outputs.md`, section 3 (PR #82 at `6301362`, round 4 in PR #84 at `44c0411`). This replaces the first estimate in `5-senate-2028.md`, which was about 53-57.
- **A bad year** still averages about 55 with a Democratic president: Minnesota's 2027 special lost and the environment under D+1 (`2027-scorecard.md`, PR #96 at `2d80193`, PR #98 at `f6972db`).
- **The models more likely run low for Democrats than high.** A 2018-24 back-test under-predicted Democratic Senate and House seats in every year (`model-credibility.md`, PR #92 at `845619f`).
- **The binding Senate constraint is D2's whip count, not seats.** Graduated cloture (F) has the votes in about 63% of runs (`senate-model-2028.md`, section 9).
- **The House** needs about D+1.5 for an even chance. With a Democratic president it is Democratic in 89% of runs, so the realistic divided case is about 11% (`house-model-2028.md` and `house-stress-test-2029.md`, PR #88 at `634947d`).
- **The White House** goes Democratic in 65% of runs under the shared environment (`presidential-model-2028.md`, PR #87 at `7d50150`).

## Choice 1: the Senate band

| Option | Band | Test | Upside | Against the current models |
| --- | --- | --- | --- | --- |
| A. Keep the legacy D1 | 52-54 | 51 | 56+ | Below even the bad-year average of about 55 |
| **B. Recommended** | **53-56** | **51** | **58+** | Covers the lower half of the Democratic-president range: conservative, reached in about 95% of runs |
| C. Plan for the center | 55-57 | 52 | 60 | Matches the central estimate; fails in the bad year |

**Why B, though the models now center near 57.**
- A planning band should hold in a bad year as well as an average one.
- The constraint that decides regular-order bills is D2's whip count, which a higher band does not change.
- B keeps the 51-seat test, so nothing that survives today drops out.

If the 2027 races run well ahead of track (`2027-scorecard.md`, signal 3), Espen can raise the band then.

## Choice 2: the House

Every Senate option assumes a Democratic House comes with the presidency. If it does not, all three reconciliation bills (D5) are lost until a House is won back. Rules, enforcement and appointments still move; money and legal status do not (`house-stress-test-2029.md`).

| Option | What it means | Cost |
| --- | --- | --- |
| **1. Keep the stipulation (Espen's direction)** | Plan on a trifecta in 2029-30, the House included | No 2029 plan for the divided case; it stays analysis in `house-stress-test-2029.md` |
| 2. Add an "H" tag | Each item also says whether it survives a Republican House: ✔ if executive, state or Senate-only, ✖ otherwise. One more column beside D1's existing ✔ / ◐ / ✖ | Light |
| 3. Write a divided-2029 branch plan | First-100-days executive actions, the confirmation slate, negotiating positions, the 2030 ask | More work |

**Decided: 1.** Espen, on PR #80: "Act as if the House goes to Democrats in the 2028 election along with the Senate and White House. For 2030 and beyond, we can model and prepare for other outcomes, but the premise of the Project 2050 work includes an initial trifecta window in 2029-30." The project's own models put a Democratic House at 89% of Democratic-president runs (`house-model-2028.md`); the stipulation is a planning premise, not a forecast.

## The decision

**D1, decided:**
- **Plan for a Senate of 53-56 seats.** Test every item against 51 and treat 58 or more as upside.
- **Tag each item for the Senate, as before:** ✔ survives at 51 (reconciliation, state, executive, House-only); ◐ needs a D2 majority-precedent path; ✖ needs 60, 67 or Republican votes.
- **Plan on a trifecta in 2029-30.** Outcomes from 2030 on (a lost House, a narrower Senate) are modeled and prepared for, not assumed away.

**Stipulations for modeling.** These are modeling assumptions, not forecasts.
- **White House:** a Democrat holds it from January 2029 to at least January 2037 (unchanged).
- **Senate:** Democrats hold 53-56 seats from January 2029. Holding the Senate through 2036 is no longer stipulated:
  - control holds through the 2031-32 Congress in about 82% of runs, but only 46% through 2033-34 (`2030-2034-control.md`);
  - the 2032 class contains the seats won in 2026's wave, which Democrats must defend.
- **House:** Democrats hold it in the 2029-30 Congress, with the presidency and the Senate. It is possibly lost or narrowed in 2030, and plans for 2031 on prepare for that. A trifecta comes again from January 2033 if DEM-1 (with DEM-2 and the *Callais* response) is in force before the 2031 redistricting.
- **Permitting:** a version of S. 5653, the bipartisan permitting bill, is enacted in the 2026 lame duck or the 2027-28 Congress (unchanged; record its status after the lame duck).
- **First-trifecta scope:** unchanged from the legacy D1.

## Where it bears on D2 to D9 (notes only)

- **D2:** the seat band matters less than the whip count. If the 2027 signals turn bad, the scorecard points to D2's fallback (G) and opening offer (C) as the working path, not to a lower band.
- **D5:** the three reconciliation vehicles stay as planned for 2029-30. The divided case, in which they are lost, is analysis only (`house-stress-test-2029.md`).
- **D3, D4, D6 to D9:** no direct effect.
