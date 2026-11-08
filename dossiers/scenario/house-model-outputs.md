# House model outputs (generated)

Role: the tables `tools/house_model.py --write` produces, read by `house-model-2028.md`. Status: generated; do not edit by hand. This project's exploratory scenario arithmetic, not a forecast. n = 20000 runs per row, seeded; the Senate and presidency in each run come from `senate_model.py`.

## 1. The curve

Fitted spread 47.0 points; seats per point of national margin near the median: 3.7. Democratic seats on the 2026 lines by presidential margin, before incumbency, map changes and noise:

| Presidential margin | R+3 | R+1.5 | Even | D+3 | D+6 | D+9 | D+12.9 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Democratic seats | 195 | 201 | 206 | 218 | 229 | 240 | 254 |

Check against 2026: the curve gives 254 seats at D+12.9 against about 259 won (House vote D+12.9; 1-results.md), so 2026 Democrats ran about 1.5 points ahead of uniform swing.

## 2. The House and the trifecta in January 2029

| Environment | Mean D seats | 90% range | P(D House) | P(230+) | P(D House and D Senate) | P(trifecta) |
| --- | --- | --- | --- | --- | --- | --- |
| R+3 | 203 | 185-220 | 8% | 1% | 8% | 1% |
| Neutral | 214 | 196-231 | 35% | 7% | 35% | 21% |
| D+3 | 225 | 207-242 | 75% | 32% | 75% | 70% |
| D+6 | 236 | 218-253 | 96% | 72% | 96% | 95% |
| 2026 repeat (D+13) | 261 | 244-278 | 100% | 100% | 100% | 100% |
| Evidence-weighted prior, D+3 with SD 4.5 | 224 | 192-257 | 64% | 40% | 63% | 58% |

## 3. By presidential winner (evidence-weighted prior)

| Winner | Share | Mean D House seats | P(D House) | P(D Senate control) | P(trifecta) |
| --- | --- | --- | --- | --- | --- |
| Democratic president | 66% | 235 | 89% | 100% | 89% |
| Republican president | 34% | 205 | 15% | 85% | 0 |

## 4. Sensitivity (D+3)

| Change | Mean D seats | P(D House) | P(trifecta) |
| --- | --- | --- | --- |
| Base | 224 | 74% | 69% |
| Incumbency shift 0.5 | 221 | 62% | 59% |
| Incumbency shift 3.0 | 230 | 88% | 78% |
| Break-even D+2 | 231 | 84% | 77% |
| Break-even D+4 | 220 | 62% | 59% |
| House-vs-presidential SD 3 | 224 | 68% | 62% |
| Seat noise SD 10 | 224 | 69% | 63% |

Map changes before 2028 (assumptions): mean +1.5 Democratic seats, range -3 to +6. New York redraw (2027 referendum) 45% chance of +3.0; Maryland MD-1 70% chance of +1.0; Wisconsin new map 30% chance of +1.5; Mississippi redraw 40% chance of -1.0; Other Republican redraws or Callais rulings 30% chance of -2.0.

## 5. Break-even environments

The presidential margin at which each outcome reaches 50% (scan in 0.5-point steps, fixed environment):

| Outcome | 50% at |
| --- | --- |
| D House | D+1.5 |
| trifecta | D+2.0 |

## 6. Is "Senate control with a Democratic president" really near 100%?

Evidence-weighted prior, runs with a Democratic president. "Narrow win" means a presidential margin under 3 points. Every run already carries race, regional and Senate-wide errors, so a split result is possible; the stressed rows widen them (race SD 8, regional SD 4, Senate-wide SD 2) and/or lose all three uncertain seats not up (Alaska and Mississippi 2026, Minnesota 2027).

| Case | 51+ seats | Exactly 50 (+ VP) | 49 or fewer | Narrow wins: 50 or fewer | Narrow wins: 49 or fewer |
| --- | --- | --- | --- | --- | --- |
| Base | 100% | <1% | <1% | 1% | <1% |
| Lose AK, MS and MN (37 not up) | 96% | 3% | 1% | 12% | 4% |
| Wider errors | 99% | 1% | <1% | 3% | 1% |
| Both | 91% | 5% | 4% | 21% | 10% |
