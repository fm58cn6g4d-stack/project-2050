# How far to trust the scenario models

Role: a credibility check of the scenario model stack: the Senate model (`senate-model-2028.md`), the House model (`house-model-2028.md`), the 2030-2034 chain (`2030-2034-control.md`) and the redistricting model (`redistricting-2030-model.md`). It back-tests them on 2018-2024, stress-tests the national-environment prior they all share, and lists the five assumptions that matter most, with what to watch. Status: draft (stage B follow-up), November 8, 2026.

**What kind of evidence this is.** This is this project's own back-test (`tools/backtest.py`; tables in `model-credibility-outputs.md`; tests in `tools/test_backtest.py`). The historical results come from FiveThirtyEight's public results files (CC BY 4.0) [SRC-0600], extracted to `model-credibility-data.json`. The extract reproduces the Senate model's typed-in 2020 and 2024 presidential margins in every state but New York, where FiveThirtyEight separates fusion-party lines.

## In brief

- **Given the national environment, the Senate model is good but leans Republican.**
  - Re-run for the 2018, 2020, 2022 and 2024 Senate classes with only what was known two years earlier, and given each year's actual environment, it scores a pooled Brier of **0.076**. A naive rule (each state votes for its last presidential winner) scores 0.098, and 0.250 is a coin flip.
  - But it **under-predicted Democratic seats in every class**: 19.8 against 21 in 2018, 13.6 against 15, 11.8 against 16 and 16.0 against 18. Democrats won 62% of the races it put at 10-35%, and 5 of the 6 it put near 50%.
  - The misses are swing-state Democrats running ahead of their states in a Trump-era series: Arizona, Georgia, Nevada, Pennsylvania and Michigan. A uniform 4-point shift toward Democrats would have removed the bias.
- **The House curve shows the same lean.** Re-fitted on each previous election, and given the actual House vote, it under-predicted Democratic seats by 2-12 (about 7 on average). 2022's new maps account for the largest miss. The 2028 House model's +1.5-point incumbency shift already moves in that direction.
- **The environment prior is cautious, and about right in width.** The best simple two-years-out rule for a presidential year is the average of the midterm House margin and the previous presidential margin. Since 1992 it has missed by 4.5 points (RMSE), the same as the prior's SD of 4.5. For 2028 that rule says **D+5.7**; the models use D+3.0.
- **What it means for the headlines.** On the back-test record, the published numbers are more likely too low for Democrats than too high:

  | Change | P(55+ Senate seats) | P(trifecta) |
  | --- | --- | --- |
  | As published | 63% | 58% |
  | Half the back-test bias (+2 points) | 75% | |
  | The full bias (+4 points) | 85% | |
  | The rule's environment (D+5.7) | 78% | 77% |

  The caution is deliberate. The bias may be particular to 2018-24 Republican nominees, and the 2028 nominees are unknown. Treat the published figures as a floor-leaning central case, not a midpoint.
- **The five assumptions that matter most** are listed in section 4, each with a leading indicator to watch: the national environment; the candidate-quality gap the back-test found; the three uncertain seats not up; the House break-even; and the caucus's filibuster positions.

## 1. The back-test

**How it was run.** For each Senate class from 2018 to 2024, the model was re-run with:
- **The lean, from what was known two years earlier:** the two latest presidential results and the latest midterm Senate result in the state, net of incumbency, with the same weights as the 2028 model (0.2, 0.5, 0.3);
- **The candidate effect:** from the incumbent's own previous race, with the same formula;
- **Whether the incumbent ran:** taken from the actual ballot. This is the one piece of hindsight.

It was scored two ways:
- **(A) Given the actual national environment.** This tests the state-level structure.
- **(B) With the environment drawn from a two-years-out rule** (section 2), as the 2028 model does.

Races without a Democratic-Republican contest are left out, as are Maine and Vermont: 32-34 races a year.

| Year | Races | Brier (A) | Brier (B) | Naive | Democratic seats: predicted (A), 90% range | Actual | Wrong calls (A) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2018 | 32 | 0.092 | 0.106 | 0.219 | 19.8 (18-22) | 21 | FL, MT, WV |
| 2020 | 33 | 0.059 | 0.056 | 0.121 | 13.6 (11-16) | 15 | AZ, GA, GA (special), NC |
| 2022 | 34 | 0.091 | 0.086 | 0.029 | 11.8 (10-14) | 16 | AZ, GA, GA (runoff), NV, PA |
| 2024 | 33 | 0.063 | 0.049 | 0.030 | 16.0 (13-18) | 18 | AZ, MI, NV, PA |

**Reading it:**
1. **The model beats the naive rule overall, but not in 2022 or 2024.** In those years nearly every state voted its presidential lean, and the model's honest uncertainty cost it in races that were never close.
2. **The actual seat count fell outside the 90% range once, in 2022.** That is consistent with a range that is a little too narrow, or with the bias.
3. **The bias is the main finding.**

   | Uniform shift toward Democrats | 0 | +1 | +2 | +3 | +4 |
   | --- | --- | --- | --- | --- | --- |
   | Predicted Democratic seats, four classes (70 actual) | 61.3 | 63.2 | 65.2 | 67.2 | 69.2 |
   | Pooled Brier | 0.076 | 0.070 | 0.064 | 0.060 | 0.058 |

   The model is not changed for it. Four cycles is a small sample, and the likeliest cause is the Republican nominees of 2018-24 (several weak candidates in exactly these states). That may or may not repeat in 2028 (section 4).

**The House** (curve re-fitted on the previous election's seats and House vote):

| Year | Implied break-even | Predicted Democratic seats (A), 90% range | Actual |
| --- | --- | --- | --- |
| 2018 | D+5.5 | 229 (221-238) | 235 |
| 2020 | D+3.9 | 214 (206-222) | 222 |
| 2022 | D+1.8 | 201 (193-210) | 213 |
| 2024 | R+1.4 | 213 (205-222) | 215 |

The curve called the majority correctly in 2018, 2022 and 2024, and missed 2020: it gave Democrats 21%, and they held it with 222 seats.

## 2. The environment prior

**Where D+3.0 with SD 4.5 comes from** (`senate-model-2028.md`, section 3):
- **The history of reversion.** Since 1994 the next presidential year has reverted from the midterm by 0-8 points, except 2006-08, when the wave grew.
- **Compressed presidential margins:** none since 1992 has exceeded 8.5 points.
- **Unknown nominees.**

The back-test shows how those judgments compare with simple rules applied two years out:

| Rule (presidential years 1992-2024) | Error (RMSE) | Mean error (actual minus rule) | For 2028 |
| --- | --- | --- | --- |
| The midterm House margin | 6.9 | +3.6 | D+12.9 |
| The previous presidential margin | 6.7 | +0.7 | R+1.5 |
| **The average of the two** | **4.5** | +2.1 | **D+5.7** |
| Always even | 4.8 | +3.2 | Even |

- **The center.** The best simple rule puts 2028 at D+5.7, so the prior's D+3.0 is 2.7 points more cautious. The prior is a judgment, not the rule's output.
- **The width.** The prior's SD of 4.5 matches the rule's historical error, which supports the width.
- **Midterms are harder.** The rule for midterm years (the previous House vote moved against the president's party by the average swing) has missed by up to 13.7 points (2010) and by 9.1 in 2026. That is why the 2030 step of the chain is the least certain.

**How much the headlines move with the prior** (`model-credibility-outputs.md`, section 4):

| Prior | P(D president) | P(55+ Senate seats) | P(D House 2029) | P(trifecta) | P(D House 2033), D president: no DEM-2 / with Titles I-II |
| --- | --- | --- | --- | --- | --- |
| Even, SD 4.5 | 42% | 42% | 41% | 35% | 34% / 49% |
| D+1.5, SD 4.5 | 54% | 53% | 53% | 47% | 37% / 52% |
| D+3.0, SD 3.0 | 71% | 65% | 67% | 61% | 36% / 51% |
| **D+3.0, SD 4.5 (published)** | **65%** | **63%** | **64%** | **58%** | **42% / 56%** |
| D+3.0, SD 6.0 | 62% | 61% | 61% | 56% | 48% / 61% |
| D+4.5, SD 4.5 | 76% | 72% | 74% | 70% | 47% / 60% |
| D+5.7, SD 4.5 (the rule) | 83% | 78% | 81% | 77% | 51% / 64% |
| D+7.0, SD 4.5 | 88% | 84% | 86% | 84% | 57% / 69% |

- **The center matters most.** Each 1.5 points moves the trifecta by about 11-12 points.
- **The spread matters little.** Over SD 3-6, the trifecta moves by 5 points.
- **The 2033 House barely moves,** because the 2030 midterm and the 2032 environment dominate it. DEM-2's gain is about 13-15 points in every row.

**What would move the prior between now and 2028.** Each is a signal to fold in as it arrives; none is in the model yet:

| Signal | When | What would move the center |
| --- | --- | --- |
| Presidential approval | Continuous | Trump's approval was 31% in Reuters/Ipsos in October 2026, a record low [SRC-0824] [SRC-0541]. A sustained recovery toward the low 40s would argue for the prior's caution; staying near 30 would argue for the rule's D+5.7 |
| The generic congressional ballot | From 2027 | It was D 47, R 35 in mid-October 2026 (`2028-outlook.md`). Its 2027-28 level, against the 2026 result, is the cleanest direct read on reversion |
| Special elections | 2027-28 | Democratic over- or under-performance against each district's presidential lean, averaged across the cycle's specials. The project should compile its own series rather than rely on one outlet's |
| The November 2027 off-year results | November 2, 2027 | Virginia and New Jersey legislatures; Kentucky, Louisiana and Mississippi governors; **Minnesota's Senate special** (a seat in every scenario); Pennsylvania's Supreme Court; New York's redistricting referendum |
| Nominees | 2027-28 | The Democratic and Republican presidential nominees, and the Senate nominees in AZ, GA, NV, PA, NC and WI (section 4) |

## 3. Limits of the check

- **Four cycles is a small sample,** and all four are Trump-era. The bias the back-test found may be an era effect.
- **One piece of hindsight.** The Senate back-test uses who actually ran. The 2028 model instead draws that for Kelly, Grassley and Johnson.
- **The House back-test** re-fits on the previous election's maps, so a redistricting year (2022) is out of sample by construction.
- **The environment rules are scored on nine presidential years.** Their errors are estimated loosely.
- **Untested pieces:** the redistricting model's pen calls and the D2-F whip count have no historical analog in this check.

## 4. The five assumptions that matter most, and what to watch

| # | Assumption | How much it moves the headline | Leading indicator to watch through 2027-28 |
| --- | --- | --- | --- |
| 1 | **The 2028 national environment: D+3.0, SD 4.5** | Each 1.5 points moves P(trifecta) by about 11-12 points; the best simple rule says D+5.7 | Trump's approval; the generic ballot; the special-election average; the November 2027 off-year results; the nominees |
| 2 | **Candidate effects carry over at 40%, with no extra term for nominee quality** | The back-test found Democrats outran the model by about 4 points in 2018-24 Senate races; +2 points takes P(55+) from 63% to 75% | Who wins the Republican primaries in AZ, GA, NV, PA, NC and WI. Quarterly FEC cash (Kelly's $26.5M against Budd's $0.7M and Johnson's $1.1M, `senate-model-fec-cash.csv`). Kelly's, Grassley's and Johnson's decisions |
| 3 | **The three uncertain seats not up: Alaska 2026 (78%), Mississippi 2026 (87%), Minnesota 2027 (90%)** | Losing all three takes a Democratic president's chance of 51+ Senate seats in a narrow win from about 99% to about 88% (79% with wider errors), and of control from about 99% to 90-96% (`house-model-outputs.md`, section 6) | The Alaska and Mississippi certifications (November 25 and December 3, 2026); Klobuchar's appointee and the Republican candidate for the November 2027 special |
| 4 | **The House break-even about D+1.5,** with a +1.5-point incumbency shift and about +1.5 net seats from pending redraws | A break-even of D+2 to D+4 moves P(Democratic House) at D+3 between 62% and 84% | The New York referendum (November 2027); Maryland's MD-1 map; the Wisconsin rulings; freshman Democrats' retirements; the first Cook and Inside Elections ratings in early 2027 |
| 5 | **The caucus's filibuster positions,** which give D2-F the votes in 63% of runs (range 14-87%) | It decides whether a large Senate turns into regular-order bills, and so whether DEM-2 and statehood can pass at all | Statements by the 2026 reform camp (Turek, Andrews, Pappas) on graduated cloture specifically; Colom's and Peltola's positions if seated; any 2027 cloture-reform votes; Fetterman's 2028 primary |

**Also high-leverage, but not top five:** how much of a gerrymander DEM-2's Title II would remove in court. It is worth +6 to +13 House seats across its tested range, and it is a legal question, not an electoral one (`redistricting-2030-model.md`).

## Next questions

1. **A nominee-quality term.** Should the Senate model add one, estimated from 2010-2024, and decide in 2028 whether it applies once the nominees are known?
2. **A longer back-test.** Extend it to 2010-2016 to see whether the Democratic over-performance is a Trump-era effect or a general bias in the lean formula.
3. **A special-election series** for 2027-28, compiled and committed, so the prior's center can be updated by a stated rule rather than by judgment.
4. **The November 2027 results** as a formal update: off-year margins against lean, folded into the 2028 prior with a weight set in advance.
