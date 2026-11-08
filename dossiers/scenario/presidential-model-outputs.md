# 2028 presidential model: outputs (n = 20000 per row, seeded)

## 1. State leans (D margin relative to the nation, points; from senate_model.lean)

| State | Electors | Lean (base) | Lean (presidential results only) |
| --- | --- | --- | --- |
| NM | 5 | +8.5 | +7.2 |
| VA | 13 | +7.1 | +6.8 |
| ME | 4 | +3.7 | +7.3 |
| MN | 10 | +2.5 | +4.8 |
| NH | 4 | +1.4 | +3.9 |
| PA | 19 | +1.1 | -1.1 |
| NC | 16 | -0.0 | -2.9 |
| GA | 16 | -1.0 | -1.7 |
| NV | 6 | -1.9 | -1.7 |
| WI | 10 | -1.9 | -0.7 |
| MI | 15 | -2.1 | -0.4 |
| AZ | 11 | -3.7 | -4.1 |

## 2. By national environment (shared national swing with the Senate model)

| Environment | P(D wins the Electoral College) | Mean D electors | Top tipping-point states | P(D Senate control), D president | P(D Senate control), R president | Runs where the Senate model's ec_bias rule picks the same winner |
| --- | --- | --- | --- | --- | --- | --- |
| R+3 | 10% | 229 | PA 16%, MI 15%, GA 15%, NC 14% | 99% | 82% | 91% |
| Neutral | 38% | 259 | PA 16%, MI 15%, GA 15%, NC 14% | >99% | 94% | 75% |
| D+3 | 75% | 292 | PA 16%, MI 15%, GA 15%, NC 14% | >99% | 98% | 80% |
| D+6 | 95% | 326 | PA 16%, MI 15%, GA 15%, NC 14% | >99% | >99% | 95% |
| Evidence-weighted (D+3, SD 4.5), as in the Senate model | 65% | 293 | PA 16%, MI 15%, GA 15%, NC 14% | >99% | 86% | 87% |

The tipping-point shares do not depend on the environment: with a uniform national swing, the order of states is set by lean and the regional and state errors alone.

## 3. Implied Electoral College bias (national margin where P(D win) = 50%)

| Case | Break-even D margin |
| --- | --- |
| Base (Senate-model leans, state SD 3) | +0.9 |
| State SD 2 | +0.8 |
| State SD 4 | +1.0 |
| Presidential leans only (2026 weight 0) | +1.3 |
| 2026 weight 0.45 | +0.8 |
