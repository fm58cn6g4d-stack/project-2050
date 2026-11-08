# 2027 scorecard outputs (generated)

Role: the tables `tools/scorecard_2027.py --write` produces, read by `2027-scorecard.md`. Status: generated; do not edit by hand. This project's exploratory scenario arithmetic, not a forecast. Headline odds come from `senate_model.py`, `house_model.py` and `redistricting_2030.py` run unchanged at the moved prior; n = 20000 runs per row (half that for the 2033 House), seeded.

## 1. On-track benchmarks for D+3.0, and how far each result moves the 2028 estimate

Off-year excess (how far a contest ran ahead of the state's next presidential margin): courts and other non-governor statewide races +6.2 on average; specials +8.0 over the next presidential change (ASSUMPTION). Governor races keep 40% of their own state's excess beyond that.

| Contest | Date | Lean (vs nation) | On track for D+3.0 | On track for Even / D+6 | Noise SD | Move in 2028 estimate per point above track: full slate / alone |
| --- | --- | --- | --- | --- | --- | --- |
| Minnesota U.S. Senate special | Nov 2 | D+2.5 | D+12.7 | D+9.7 / D+15.7 | 6.1 | 0.07 / 0.25 |
| Pennsylvania Supreme Court, open seat | Nov 2 | D+1.1 | D+10.2 | D+7.2 / D+13.2 | 7.0 | 0.06 / 0.22 |
| Wisconsin Supreme Court (only if a conservative runs) | Apr 6 | R+1.9 | D+7.2 | D+4.2 / D+10.2 | 7.0 | 0.06 / 0.22 |
| Kentucky governor (open D seat) | Nov 2 | R+28.1 | R+10.3 | R+13.3 / R+7.3 | 9.0 | 0.03 / 0.16 |
| Mississippi governor (open R seat) | Nov 2 | R+18.1 | R+8.6 | R+11.6 / R+5.6 | 9.0 | 0.03 / 0.16 |
| Louisiana governor (runoff, if a Democrat makes it) | Nov 20 | R+19.3 | R+2.6 | R+5.6 / D+0.4 | 9.0 | 0.03 / 0.16 |
| Special-election average, all of 2027 (vs. Harris 2024) | all year | — | D+12.5 | D+9.5 / D+15.5 | 5.0 | 0.11 / 0.29 |

KY governor excess by race, incumbency removed: +21.1, +29.3, +32.6; carried over: +14.8.

MS governor excess by race, incumbency removed: -13.0, +11.5, +22.7; carried over: +6.5.

LA governor excess by race, incumbency removed: +31.9, +18.3; carried over: +13.7.

Translation noise (shared by every 2027 contest) TAU = 4.8 points; full-slate gain 0.40; posterior SD after the full slate 3.5 (from 4.5).

## 2. Calibration: did off-year results predict the next cycle?

Signal = average Democratic gain over the state's previous presidential margin (governor races); specials as reported. Next change = next national result minus the previous presidential margin.

| Off-year | Target | Governor-race swing | Specials average | Next national change |
| --- | --- | --- | --- | --- |
| 2017 (VA, NJ) | 2018 midterm | +1.8 | +10.6 | +6.5 |
| 2021 (VA, NJ) | 2022 midterm | -12.4 | -4.0 | -7.1 |
| 2025 (VA, NJ) | 2026 midterm | +9.0 | +13.0 | +14.4 |
| 2015 (KY, LA, MS) | 2016 presidential | +7.0 | — | -1.8 |
| 2019 (KY, LA, MS) | 2020 presidential | +21.8 | — | +2.4 |
| 2023 (KY, MS) | 2024 presidential | +22.2 | +5.7 | -5.9 |

Fits: before midterms, next change = +5.1 + 1.00 x governor swing (residuals -0.5, +0.2, +0.3); specials, slope 1.14. Before presidential years, slope -0.01: no usable relation, and in 2023 the sign was wrong.

Gain sensitivity (same contests, all on track except a 5-point miss across the board):

| Full-slate gain k | Implied TAU | 2028 estimate after a 5-point miss | Posterior SD |
| --- | --- | --- | --- |
| 0.2 | 8.6 | D+2.0 | 4.0 |
| 0.4 (pre-registered) | 4.8 | D+1.0 | 3.5 |
| 0.7 | 1.3 | R+0.4 | 2.6 |

## 3. What each reading of 2027 does to the plan's odds

"Across the board" moves every numeric contest by the same amount (Wisconsin left out). Minnesota is fixed held or lost by its own result; New York and Virginia stay at their current probabilities.

| 2027 reading | 2028 estimate (SD) | Minnesota | P(trifecta) | P(55+ Senate) | P(55+), D president | Mean seats, D president | P(D House 2033), no DEM-2 / with |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Today, before any 2027 result | D+3.0 (4.5) | 90% | 59% | 63% | 84% | 56.7 | 46% / 54% |
| 10 points ahead of track | D+6.9 (3.5) | held | 88% | 88% | 92% | 57.6 | 65% / 74% |
| 5 ahead | D+5.0 (3.5) | held | 77% | 78% | 88% | 57.0 | 55% / 64% |
| On track | D+3.0 (3.5) | held | 60% | 66% | 84% | 56.5 | 45% / 54% |
| 5 behind | D+1.0 (3.5) | held | 42% | 52% | 80% | 56.1 | 36% / 44% |
| 10 behind | R+0.9 (3.5) | held | 25% | 37% | 76% | 55.8 | 27% / 34% |
| 15 behind (a 2021-sized turn) | R+2.9 (3.5) | lost | 13% | 14% | 52% | 54.6 | 20% / 25% |

**Single results, the rest on track.**

| Result | 2028 estimate | P(trifecta) | P(55+ Senate) | P(D House 2033), no DEM-2 |
| --- | --- | --- | --- | --- |
| Minnesota held by 20 (7 above track) | D+3.6 | 66% | 70% | 48% |
| Minnesota held by 3 | D+2.2 | 53% | 60% | 41% |
| Minnesota lost by 2 | D+1.8 | 49% | 42% | 39% |
| Kentucky lost by 15 | D+2.8 | 59% | 65% | 44% |
| Mississippi won by 3 | D+3.5 | 65% | 69% | 47% |
| Specials average only Harris +5 | D+2.1 | 52% | 59% | 41% |
| Specials average Harris +18 | D+3.7 | 67% | 71% | 49% |
| New York referendum passes | D+3.0 | 63% | 66% | 47% |
| New York referendum fails | D+3.0 | 59% | 66% | 44% |
| Virginia Senate lost (21-19 flips) | D+3.0 | 60% | 66% | 45% |
| New York fails and Virginia Senate lost | D+3.0 | 59% | 66% | 44% |

## 4. Plan-change tests

Option B (#80) plans for a 53-56 Senate. With a Democratic president: P(53-56), P(53+), mean seats and P(D2-F has the votes, the round-4 whip count); and P(Democratic president) itself:

| Case | P(53-56) | P(53+) | Mean seats | P(D2-F has the votes) | P(D president) |
| --- | --- | --- | --- | --- | --- |
| Today (D+3.0, SD 4.5) | 43% | 97% | 56.7 | 64% | 66% |
| 2027 on track, Minnesota held | 47% | 97% | 56.5 | 61% | 69% |
| Minnesota lost and mid-2028 environment D+1 (SD 3) | 70% | 90% | 54.9 | 41% | 50% |
| Minnesota lost and mid-2028 environment Even (SD 3) | 72% | 89% | 54.7 | 37% | 39% |
| Minnesota lost and mid-2028 environment R+3 (SD 3) | 74% | 85% | 54.4 | 32% | 13% |
| Minnesota held and mid-2028 environment D+6 (SD 3) | 35% | 99% | 57.2 | 69% | 92% |

How far the environment would have to fall before a Democratic president's Senate drops below option B (Minnesota lost, environment known to SD 2): mean seats and P(53+), by environment:

| Environment | R+6.0 | R+4.0 | R+2.0 | D+0.0 | D+2.0 |
| --- | --- | --- | --- | --- | --- |
| Mean seats, D president | 53.8 | 54.1 | 54.2 | 54.5 | 54.8 |
| P(53+), D president | 80% | 84% | 84% | 86% | 90% |
| P(D president) | 1% | 4% | 14% | 36% | 64% |
