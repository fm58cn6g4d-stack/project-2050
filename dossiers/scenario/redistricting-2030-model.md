# Who draws the 2031 maps, and what DEM-2 is worth

Role: a model of who holds the 2031 congressional redistricting pens in the twelve states that matter most, linked to the same national swing as the Senate and House models, and the value of DEM-2 Titles I-II in House seats on the 2032 maps. Status: draft (stage B follow-up), November 8, 2026.

This file is the numbers; the qualitative state-by-state account is `compounding-redistricting.md` (PR #86), whose seat projections and partisan swings it uses rather than repeats. DEM-2's titles follow the memo in PR #89:
- **Title I:** the mid-decade ban.
- **Title II:** federal criteria with a partisan-fairness standard, enforceable in court.
- **Title III:** commissions.

**What kind of evidence this is.** This is this project's own scenario arithmetic (`tools/redistricting_2030.py`; tables in `redistricting-2030-outputs.md`; tests in `tools/test_redistricting_2030.py`), not a forecast. The office break-even points, the share of a gerrymander that Title II would remove, and the partisan effects outside the twelve states are labeled assumptions with tested ranges.

## In brief

- **Under a Democratic president, Republicans probably draw most of the big maps.** The 2030 midterm swing against the president's party, drawn from 1990-2026, puts the average 2030 environment at about R+1.5. Republicans then hold the pen in Florida (93% of runs), North Carolina (87%), Ohio (77%) and Texas (71%), and in Georgia half the time. On average they draw 3.8 of those five states, and all five in 39% of runs. Democrats draw New York only if its November 2027 referendum passes (45%). Pennsylvania and Wisconsin are mostly deadlocked or Republican.
- **DEM-2 Titles I-II are worth about +10 Democratic House seats on the 2032 maps under a Democratic president.** The 10th-90th percentile range is +3 to +15, and the sensitivity range +6 to +13.
  - Without DEM-2, the 2032 maps carry a net Republican partisan effect of about 15 seats: 11 from the twelve states and 4 from the rest of the country.
  - With Title II removing about two-thirds of each gerrymander, P(Democratic House, January 2033) rises from **42% to 57%**.

  This matches the upper half of #86's analysis-based "+5 to +10."
- **Title I adds nothing to the 2032 maps.** The ban does not touch the decennial 2031 redraw. Its value is after 2032: it stops a 2033-40 round of mid-decade redraws. On the 2025-26 evidence that round nets about zero in expectation but swings plus or minus 2-3 seats (section 4). The 2032 value is Title II's, which supports #89's ordering (ban, then criteria, then commissions) only if Title II is in the bill: a ban-only DEM-2 is worth about zero seats in 2032.
- **One correction to #86.** #86 calls DEM-2 "about neutral" if Democrats sweep 2030. In the model, even with a Republican president (an average 2030 of about D+4.9), Republicans still draw Florida 78% and North Carolina 66% of the time, because the North Carolina Senate, Florida's chambers, Ohio's legislature and the Texas Senate sit far to the right of their states. Democrats rarely gain a pen, so DEM-2 is still worth about +6 seats. A Republican president would not sign it, so this is a note on the maps, not a plan.

## 1. How the model works

For each simulated run of `senate_model.simulate_chain` (evidence-weighted 2028 environment), the model:
1. **Takes the shared environments.** It uses the 2028 presidential winner and that run's 2030 and 2032 national environments, which are already shared with the Senate model.
2. **Decides the 2030 offices.** Each office that decides a state's map (governor, each chamber) goes Democratic if the 2030 environment, plus a regional error and an office error, beats that office's break-even.
3. **Assigns the pen.** A party holds the pen if it wins every office the map needs. Otherwise the map is neutral: a court, a commission, a bipartisan deal or a deadlock.
4. **Applies the map effect.** A Democratic pen moves the state's 2032 delegation by +g seats against a neutral map, and a Republican pen by −g, where 2g is #86's D-drawn-to-R-drawn swing.
5. **Builds the national House.** The 2032 House is the `house_model.py` curve on geography alone, plus every state's map effect, plus noise.

**The twelve states** (seats after 2030 and swings from #86; break-evens are assumptions):

| State | Seats | Swing (D map − R map) | What decides the 2031 map | Break-even national environment (assumption) |
| --- | --- | --- | --- | --- |
| Texas | 42 | 10 | Governor and both chambers | Governor D+5.6 (Hinojosa, first-term incumbent); House D+9 (won 83-67 at D+12.9); Senate D+18 |
| Florida | 31 | 6.5 | Governor and both chambers | Governor D+14.6 (Donalds, incumbent); chambers D+20 |
| North Carolina | 15 | 5.5 | Both chambers; **no governor's veto** | House D+10 (flipped in 2026); Senate D+13.5 (still 25-24 R at D+12.9) |
| Pennsylvania | 16 | 5 | Governor (open) and both chambers | Governor R+1.1; House R+2.5 (held at R+2.6 and R+2.7); Senate D+10 (26-24 D at D+12.9) |
| Georgia | 14 | 4.5 | Governor and both chambers | Governor R+2.0 (Bottoms, incumbent); House D+12.5 (a 91-seat majority by a local count); Senate D+15 |
| Ohio | 15 | 5 | Governor and legislature (a Democratic governor forces a bipartisan or commission map) | Governor D+6.1 (Acton, incumbent); legislature D+18 |
| Wisconsin | 8 | 2.5 | Governor and both chambers | Governor R+1.1 (Crowley, incumbent); chambers D+4 (both flipped in 2026 on fairer maps) |
| Nevada | 4 | 1.5 | Governor and legislature | Governor R+1.1 (Ford, incumbent); legislature R+4 |
| Michigan, Arizona | 13, 10 | 0 | Independent commissions | Always neutral |
| Virginia | 11 | 3 | Commission, unless a restarted amendment passes in 2028-29 (25%, assumption) | Elected in 2029, not tied to 2030 |
| New York | 24 | 6 | The legislature by simple majority if the November 2027 referendum passes (45%), else the commission | Decided in 2027 |

How the break-evens are set:
- **Governors:** the state's lean from the Senate model (2020/2024 presidential and 2026 statewide), plus 3 points for an incumbent.
- **Chambers:** placed from their 2022-26 results, as shown in the table.

Office errors have SD 7 for governors and SD 5 for chambers; governor races stray about four points further from lean than Senate races [SRC-0589].

**Outside the twelve:** a fixed net Republican partisan effect of 4 seats (SD 2; tested 0 and 8). D-drawn Illinois, Maryland, Oregon and New Mexico add about +6; R-drawn Tennessee, Louisiana, Alabama, South Carolina, Indiana, Missouri, Kentucky, Kansas, Utah and Mississippi about −10. The PNAS study of the 2021 maps found partisan effects of +8.6 Republican and +6.2 Democratic seats nationally (#86, section 2).

**Geography:** the 2026 lines' break-even of D+3.0 (`house-model-2028.md`) is split into about 1.9 points of geography and about 1.1 points (4 seats) of net partisan maps. That split is an assumption.

## 2. Results

**Who holds the 2031 pens** (share of runs; `redistricting-2030-outputs.md`, section 1):

| State | Democratic president: D / neutral / R | Republican president: D / neutral / R |
| --- | --- | --- |
| Texas | 1% / 27% / 71% | 6% / 50% / 44% |
| Florida | <1% / 7% / 93% | 2% / 20% / 78% |
| North Carolina | 4% / 9% / 87% | 13% / 22% / 66% |
| Pennsylvania | 10% / 56% / 34% | 28% / 59% / 13% |
| Georgia | 2% / 50% / 48% | 9% / 66% / 25% |
| Ohio | 2% / 21% / 77% | 7% / 40% / 54% |
| Wisconsin | 16% / 41% / 43% | 39% / 42% / 19% |
| Nevada | 40% / 29% / 31% | 67% / 22% / 11% |
| New York | 45% / 55% / 0 | 46% / 54% / 0 |
| Virginia | 25% / 75% / 0 | 25% / 75% / 0 |
| Michigan, Arizona | neutral | neutral |

**The 2032 House maps:**

| 2028 president | Net partisan map effect (D seats): 12 states / all | Expected D House seats in 2032, no DEM-2 | With Titles I-II | Value (10th-90th percentile) | P(D House, Jan 2033): no DEM-2 / with |
| --- | --- | --- | --- | --- | --- |
| **Democratic** | −10.9 / −14.8 | 214 | 223 | **+9.7** (+2.7 to +15.1) | **42% / 57%** |
| Republican | −4.6 / −8.6 | 191 | 196 | +5.6 (−3.1 to +13.1) | 15% / 19% |

The average 2032 environment is D+4.9 in Democratic-president runs (winning in 2028 selects the better environments) and R+3.1 in Republican-president runs.

**Sensitivity of the value** (Democratic president; `redistricting-2030-outputs.md`, section 3):

| Change | Value of Titles I-II | P(D House 2033): without / with |
| --- | --- | --- |
| Title II removes 40% of each gerrymander | +5.9 | 44% / 52% |
| Title II removes 85% | +12.5 | 44% / 63% |
| No net effect outside the twelve states | +6.9 | 49% / 60% |
| An 8-seat net Republican effect outside them | +12.1 | 38% / 56% |
| The partisan-fairness standard also cuts geographic bias by a quarter | +11.3 | 44% / 61% |
| A near-neutral 2028 | +11.1 | 24% / 40% |

The value is robust in sign and size, about +6 to +13 seats. Its size rests mainly on how much of a gerrymander Title II's criteria remove in court, which is a legal question, not an electoral one.

## 3. What it means for Project 2050 (options and questions)

- **D1's House stipulation.** D1 makes a 2033 House trifecta conditional on DEM-1 and DEM-2 being in force before the 2031 maps. With a Democratic president elected in 2028, the model puts P(Democratic House, January 2033) at 42% without DEM-2 and 57% with Titles I-II. **DEM-2 is necessary but not sufficient.** Even with it, the 2033 House is close to a coin flip. #89 proposes restating the stipulation around Titles I-II; these numbers support that, and suggest it read "improves the odds from about 4 in 10 to about 6 in 10," not "secures."
- **Title II carries the 2032 value.** The ban (Title I) has the lowest legal risk but adds nothing to the 2031 maps. If DEM-2 is severable (#89, option B) and Title II falls in court while Title I stands, the 2032 value falls to about zero. Question for Espen: should Title II be written to survive on its own, for example with criteria tied to existing Elections Clause precedent, and should its partisan-fairness standard be the plan's priority rather than the commission mandate?
- **Timing.** The value exists only if Titles I-II are in force before states draw in 2031, which means enactment in 2029-30 under D2's rules change. The whip count in `senate-model-2028.md`, section 9, puts that at about 63%. DEM-1F already targets DEM-1 floor time by March 2029; DEM-2's own slot is not fixed.
- **The 2030 races still matter.** Without DEM-2, the five big Republican-leaning pens (TX, FL, NC, GA, OH) are Republican in an average of 3.8 states under a Democratic president. The model's most movable pens are Georgia (about half deadlocked), Pennsylvania (56% deadlocked), Wisconsin, Texas (27% deadlocked through Hinojosa's veto) and Nevada. Holding governors' vetoes in Texas, Georgia, Wisconsin and Ohio is worth more than flipping chambers that sit 10-20 points to the right of their states.
- **New York's 2027 referendum** is the one pen Democrats can gain before 2030. At +3 seats, against a neutral commission map, it is worth about 1.4 seats in expectation. That is a 2027 decision (`2027-races.md`).

## Next questions

1. **Ohio's rule in detail.** Ohio's 2018 amendment routes failed maps through a commission of statewide officials, which this model treats as neutral. Who holds the auditor's and secretary of state's offices in 2030, and how would the commission vote?
2. **State legislative chamber data.** The chamber break-evens are placed from 2022-26 results. A seat-by-seat state legislative model, using district presidential results for the state maps, would replace them.
3. **Texas's two-thirds override.** The model treats a Democratic governor's veto as decisive. Republican supermajorities in both Texas chambers would override it, and the model gives them little chance, but that is untested.
4. **Title II's legal reach.** How much of a partisan gerrymander can statutory criteria remove in court after *Rucho*? This is the model's most valuable input (+6 to +13 seats across the tested range).
5. **The 2033-40 decade.** Chain the 2034 and 2036 House and the mid-decade question (Title I) to state DEM-2's full-decade value.
