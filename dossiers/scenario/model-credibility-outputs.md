# Model credibility outputs (generated)

Role: the tables `tools/backtest.py --write` produces, read by `model-credibility.md`. Status: generated; do not edit by hand. This project's own back-test of its scenario models, seeded.

## 1. Senate back-test, with only what was known two years earlier

A: given the actual national environment (tests the state-level structure). B: with the environment drawn from a two-years-out rule (section 3), as the 2028 model does. Races without a Democrat-v-Republican contest, Maine and Vermont are left out.

| Year | Races | Environment used (A; B mean ± SD) | Brier, A | Brier, B | Naive (last presidential winner) | D seats predicted, A (90%) | B (90%) | Actual | Wrong calls in A |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2018 | 32 | D+8.7; D+5.0 ± 7.6 | 0.092 | 0.106 | 0.219 | 19.8 (18-22) | 18.0 (11-24) | 21 | FL (0.98; actual -0.1), MT (0.25; actual +3.6), WV (0.00; actual +3.3) |
| 2020 | 33 | D+4.5; D+5.4 ± 5.0 | 0.059 | 0.056 | 0.121 | 13.6 (11-16) | 14.3 (9-20) | 15 | AZ* (0.32; actual +2.3), GA (0.29; actual +1.2), GA* (0.26; actual +2.1), NC (0.52; actual -1.7) |
| 2022 | 34 | R+2.6; R+3.3 ± 7.1 | 0.091 | 0.086 | 0.029 | 11.8 (10-14) | 11.8 (6-18) | 16 | AZ (0.21; actual +4.9), GA (0.20; actual +1.0), GA (0.19; actual +2.8), NV (0.36; actual +0.8), PA (0.27; actual +4.9) |
| 2024 | 33 | R+1.5; D+0.9 ± 4.7 | 0.063 | 0.049 | 0.030 | 16.0 (13-18) | 17.0 (12-21) | 18 | AZ (0.32; actual +2.4), MI (0.30; actual +0.3), NV (0.42; actual +1.6), PA (0.70; actual -0.2) |

Pooled Brier: A 0.076, B 0.074, naive 0.098 (lower is better; always saying 50% scores 0.250).

Calibration, A, all four years pooled (predicted band: races, mean predicted, share Democrats won):

| Band | Races | Mean predicted P(D) | Share won by D |
| --- | --- | --- | --- |
| 0-10% | 54 | 1% | 2% |
| 10-35% | 16 | 24% | 62% |
| 35-65% | 6 | 50% | 83% |
| 65-90% | 7 | 81% | 86% |
| 90-100% | 49 | 99% | 98% |

## 2. House back-test

The curve re-fitted on the previous election's seats and House vote (same spread as `house_model.py`), then given the actual House vote (A) or the two-years-out rule (B).

| Year | Implied break-even | Predicted D seats, A (90%) | P(D majority), A | Predicted, B (90%) | P(D majority), B | Actual D seats |
| --- | --- | --- | --- | --- | --- | --- |
| 2018 | D+5.5 | 229 (221-238) | 99% | 216 (169-262) | 47% | 235 |
| 2020 | D+3.9 | 214 (206-222) | 21% | 220 (188-252) | 54% | 222 |
| 2022 | D+1.8 | 201 (193-210) | <1% | 199 (155-243) | 24% | 213 |
| 2024 | R+1.4 | 213 (205-222) | 18% | 223 (192-254) | 61% | 215 |

## 3. The national environment two years out

Presidential years 1992-2024: the margin two years before the election, by four simple rules.

| Rule | Error (RMSE, points) | Mean error (actual minus rule) | What it gives for 2028 |
| --- | --- | --- | --- |
| Midterm House margin | 6.9 | +3.6 | D+12.9 |
| Previous presidential margin | 6.7 | +0.7 | R+1.5 |
| Average of the two | 4.5 | +2.1 | D+5.7 |
| Even (0) | 4.8 | +3.2 | D+0.0 |

This project's 2028 prior: D+3.0 with SD 4.5.

Midterm rule (the previous House vote moved against the president's party by the mean of earlier midterm swings):

| Midterm | Rule | Actual House vote | Error | SD of earlier swings |
| --- | --- | --- | --- | --- |
| 2006 | R+0.5 | D+6.4 | +6.9 | 7.1 |
| 2010 | D+7.1 | R+6.6 | -13.7 | 6.8 |
| 2014 | R+4.4 | R+5.1 | -0.7 | 8.3 |
| 2018 | D+5.0 | D+8.7 | +3.7 | 7.6 |
| 2022 | R+3.3 | R+2.6 | +0.7 | 7.1 |
| 2026 | D+3.8 | D+12.9 | +9.1 | 6.7 |

## 4. How much the headline numbers move with the prior

Center and spread of the 2028 national environment (Democratic presidential margin):

| Prior | P(D president) | P(55+ Senate seats) | P(D House 2029) | P(trifecta) | P(D House 2033), no DEM-2 / with Titles I-II (D president) |
| --- | --- | --- | --- | --- | --- |
| D+0.0, SD 4.5 | 42% | 42% | 41% | 35% | 50% / 61% |
| D+1.5, SD 4.5 | 54% | 53% | 53% | 47% | 53% / 63% |
| D+3.0, SD 3.0 | 71% | 65% | 67% | 61% | 51% / 63% |
| D+3.0, SD 4.5 | 65% | 63% | 64% | 58% | 57% / 67% |
| D+3.0, SD 6.0 | 62% | 61% | 61% | 56% | 62% / 71% |
| D+4.5, SD 4.5 | 76% | 72% | 74% | 70% | 61% / 71% |
| D+5.7, SD 4.5 | 83% | 78% | 81% | 77% | 65% / 74% |
| D+7.0, SD 4.5 | 88% | 84% | 86% | 84% | 70% / 78% |

## 5. The back-test bias, and what it would mean for 2028

A uniform shift toward Democrats in every back-test race (mode A) that would remove the Senate seat bias:

| Shift (points) | Predicted D seats, four classes | Actual | Pooled Brier |
| --- | --- | --- | --- |
| +0 | 61.3 | 70 | 0.076 |
| +1 | 63.2 | 70 | 0.070 |
| +2 | 65.2 | 70 | 0.064 |
| +3 | 67.2 | 70 | 0.060 |
| +4 | 69.2 | 70 | 0.058 |

If the same shift applied to 2028 (evidence-weighted prior; every 2028 race moved toward Democrats):

| Shift | Mean D seats, Jan 2029 | P(55+) | P(60+) | With a D president: mean, P(55+) |
| --- | --- | --- | --- | --- |
| +0 | 55.3 | 63% | 6% | 56.7, 84% |
| +2 | 56.3 | 75% | 11% | 57.6, 93% |
| +4 | 57.2 | 85% | 19% | 58.5, 98% |
