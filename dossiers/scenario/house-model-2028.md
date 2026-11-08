# The 2028 House and the 2029 trifecta

Role: the chance of a Democratic House in January 2029 on the current maps (mid-decade redistricting already in force, plus changes that could still land before 2028), and the chance of a full trifecta, combined run by run with the Senate model in `senate-model-2028.md`. Status: draft (stage B follow-up), November 8, 2026.

**What kind of evidence this is.** This is this project's own scenario arithmetic (`tools/house_model.py`; tables in `house-model-outputs.md`; tests in `tools/test_house_model.py`), not a forecast. It is a seats-votes curve pinned by published facts about the 2026 lines, not a district-by-district model: no district-level 2028 ratings or candidates exist yet. The map facts come from `2028-outlook.md`, section 2, which notes that both of its map sources lean progressive or reform. They need corroboration from a rater when 2028 ratings appear.

## In brief

- **The House is the binding chamber for a 2029 trifecta, not the Senate.** On the current maps, Democrats need about **D+1.5** in the presidential vote for an even chance at the House. At an even national vote they hold it in 35% of runs; at D+3, 75%; at D+6, 96%. The Senate is Democratic in 95-100% of runs in every environment from neutral up.
- **Trifecta odds:**

  | Environment | P(trifecta) |
  | --- | --- |
  | Neutral | 21% |
  | D+3 | 70% |
  | D+6 | 95% |
  | Evidence-weighted (D+3, SD 4.5) | **58%** |

  The evidence-weighted environment is the one in `senate-model-2028.md`, section 3. With a Democratic president the trifecta comes in **89%** of runs (Senate 100%, House 89%). Without one, Democrats hold the House in only 15% of runs, though they keep the Senate in 85%.
- **Seats:** with a Democratic president, a mean of 235 House seats, down from about 259 now. That is a working majority but a smaller one, consistent with the pattern that a midterm House majority shrinks in the next presidential year [SRC-0568].
- **What moves it most:**
  - the national environment;
  - the incumbency edge of the roughly 45 freshman Democrats who won Republican seats in 2026: 62-88% at D+3 across the tested range;
  - the map's break-even: D+2 to D+4 gives 62-84%;
  - pending redraws, which net about +1.5 Democratic seats in expectation: a New York redraw after a 2027 referendum, and Maryland's MD-1.

## 1. The curve and its calibration

**Three facts pin it** (data):
1. **The 2024 replay.** Under the 2026 lines Trump would have carried 234 districts to 201 while winning the nation by 1.48 points [SRC-0817] [SRC-0459].
2. **The median.** The median district, WI-1, is Trump +4.5, 3.0 points right of the nation. Wang independently puts the Democratic break-even near D+3 and the Republican map edge at "around 10 seats" [SRC-0817] [SRC-0818].
3. **The check.** Democrats won about 259 seats in 2026 at a House vote of D+12.9 (`1-results.md`).

A normal seats-votes curve through the first two facts has a spread of 47 points, or **3.7 seats per point** near the median. It gives:

| Presidential margin | R+3 | R+1.5 | Even | D+3 | D+6 | D+9 | D+12.9 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Democratic seats (uniform swing, no incumbency) | 195 | 201 | 206 | 218 | 229 | 240 | 254 |

At D+12.9 the curve gives 254 against about 259 won, so 2026 Democrats ran about 1.5 points ahead of uniform swing. They did that against Republican incumbents.

**The incumbency shift (an assumption: +1.5 points, tested 0.5-3.0).** In 2028 the seats Democrats flipped are held by Democratic incumbents. Two facts suggest Democratic House candidates run ahead of the presidential line in close seats:
- 2024: Democrats won 215 seats on lines where Harris carried only 205 districts [SRC-0817] (`1-results.md`), about 10 seats or 2.7 points ahead.
- 2026: about 1.5 points ahead, as above.

The +1.5 is therefore on the cautious side.

**Other pieces (assumptions):**
- The national House-vs-presidential deviation has SD 1.5 points. Since 2004 the House vote has run from 3.0 behind to 3.3 ahead of the presidential margin, partly an artifact of uncontested seats [SRC-0570].
- Seat noise has SD 5 seats.
- The presidency and Senate in each run come from `senate_model.py`, so the three outcomes share one national environment.

**Map changes that could still land before 2028** (assumptions on the cases in `2028-outlook.md`):

| Change | Chance | Democratic seats |
| --- | --- | --- |
| New York redraw: second legislative passage in 2027, then a November 2027 referendum [SRC-0815] | 45% | +3 |
| Maryland redraws MD-1 after Question 3 [SRC-0957] | 70% | +1 |
| Wisconsin gets a new map from the state supreme court suits [SRC-0959] | 30% | +1.5 |
| Mississippi redraws before its 2027 elections [SRC-0815] | 40% | −1 |
| Further Republican redraws or post-*Callais* rulings in the South [SRC-0816] | 30% | −2 |

Net: +1.5 seats in expectation, with a range of −3 to +6. Texas, California's Proposition 50 map, Missouri's restored 2022 lines and Utah's court map are already in the 2026 lines.

## 2. Results

| Environment | Mean Democratic seats | 90% range | P(Democratic House) | P(230+) | P(House and Senate) | P(trifecta) |
| --- | --- | --- | --- | --- | --- | --- |
| R+3 | 203 | 185-220 | 8% | 1% | 8% | 1% |
| Neutral | 214 | 196-231 | 35% | 7% | 35% | 21% |
| D+3 | 225 | 207-242 | 75% | 32% | 75% | 70% |
| D+6 | 236 | 218-253 | 96% | 72% | 96% | 95% |
| 2026 repeat (D+13) | 261 | 244-278 | 100% | 100% | 100% | 100% |
| Evidence-weighted (D+3, SD 4.5) | 224 | 192-257 | 64% | 40% | 63% | 58% |

| Evidence-weighted, by presidential winner | Share of runs | Mean House seats | P(Democratic House) | P(Democratic Senate control) | P(trifecta) |
| --- | --- | --- | --- | --- | --- |
| Democratic president | 66% | 235 | 89% | 100% | 89% |
| Republican president | 34% | 205 | 15% | 85% | 0 |

**Break-even.** The House reaches 50% at about D+1.5 and the trifecta at about D+2.0 (fixed-environment scan in half-point steps). A Democrat can win the presidency in the model at just above D+1 (the Electoral College bias in `senate-model-2028.md`), so narrow presidential wins come with a House at risk.

**Sensitivity at D+3** (`house-model-outputs.md`, section 4):

| Change | P(Democratic House) |
| --- | --- |
| Incumbency shift 0.5 | 62% |
| Incumbency shift 3.0 | 88% |
| Break-even D+2 | 84% |
| Break-even D+4 | 62% |
| Doubled House-vs-presidential error | 68% |
| Doubled seat noise | 69% |

## 3. What it means for Project 2050 (options and questions)

- **D1's House stipulation.** D1 assumes a 2029 House majority comes with the presidency. The model supports it: conditional on a Democratic president it holds in 89% of runs. But it fails in most narrow-win worlds: at a neutral environment, conditional on a Democratic win, 69% of runs have a Democratic House (mean 222 seats), and the odds fall fast below D+1.5. Question for Espen: should D1 add a House stress test (a 2029 Democratic president with a Republican House), the way it tests every item at 51 Senate seats? `2028-outlook.md` raised the same question.
- **Reconciliation needs the House too.** D5's three vehicles need a majority in both chambers. In the 11% of Democratic-president runs without the House, R1-R3 are unavailable, whatever the Senate size. Only executive action, state action and bipartisan bills remain. The 51-seat Senate test does not cover that world.
- **House margins in 2029.** The central Democratic-president outcome is about 235 seats, a margin of about 17 above 218. That is enough to absorb a moderate bloc on most votes but not a large one. The House whip count on the flagship bills (care, climate and the revenue pieces) is a question in its own right.
- **2027 levers on the House map.** In expectation, the New York referendum (November 2027) and Maryland's MD-1 redraw are worth about 2 seats together. The Wisconsin map case is worth about half a seat. Each is a 2027 action, the labeled exception in `DEC-2026-10-29-01` (`2027-races.md`).
- **After 2028.** D1 stipulates the House is "possibly lost or narrowed in 2030." This model does not chain the House forward. With a midterm swing of about 7 points against the president's party (`2030-2034-control.md`), a 235-seat House at D+5 would fall to about 205 at R+2 on this curve (incumbency included), a likely loss in 2030.

## Next questions

1. **District-level inputs.** The Downballot's or another source's district table for the 2026 lines, to replace the normal curve with the actual distribution near the median. The curve's 3.7 seats per point is an average.
2. **Freshman retirements and candidate quality** in the 45 or so seats Democrats flipped in 2026. That is the incumbency shift, the model's second-largest input.
3. **The New York amendment's path:** the 2027 second passage and the referendum odds. It is the largest single map change.
4. **A chained 2030 House.** The midterm penalty applied to the 2029 House, to state trifecta odds for the 2031-32 Congress alongside the Senate's.
5. **First published House ratings** (expected early 2027) as an independent check on the break-even near D+1.5 to D+3.
