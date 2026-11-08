# The 2027 scorecard

Role: a pre-registered reading of the November 2027 results. For each contest it gives the result that would be "on track" for the published 2028 prior (D+3.0, SD 4.5); how far each outcome should move that prior, by a rule fixed now; what the moved prior does to P(trifecta), P(55+ Senate) and P(Democratic House in 2033); and the 2027-28 signals that call for contingency preparation, not just new numbers. Status: draft (stage B follow-up), November 8, 2026. It builds on #92's indicators (`model-credibility.md`, section 4 and next questions 3-4) and on b-4's race list (`2027-races.md`).

**What kind of evidence this is.** This is this project's own arithmetic (`tools/scorecard_2027.py`; tables in `2027-scorecard-outputs.md`; tests in `tools/test_scorecard_2027.py`). The special-election series is committed as `specials-by-year.csv`, derived from The Downballot's trackers [SRC-1092] by `tools/specials_extract.py`. Other past results are cited in the script and catalogued as SRC-1070 to SRC-1091. 2016 state margins come from FiveThirtyEight's files [SRC-0600]. The headline odds come from the Senate, House and redistricting models, run unchanged at the moved prior. Every "on track" figure is analysis, not a rating; no rater has published 2027 ratings.

**Planning premise (#80, 14:20 UTC, November 8, 2026).** Espen settled #80's House sub-choice: plan on a Democratic trifecta in 2029-30, with the House, Senate and White House all Democratic. The scorecard does not reopen that premise. A 2027 reading that points to a narrow 2028 win, or a loss, triggers contingency preparation (the divided-government and Republican-branch notes), not a change to the 2029 plan.

## The scorecard on one screen

"On track" means consistent with a D+3.0 presidential environment in 2028. The move column is how far the 2028 estimate shifts per 5 points the result runs above or below track, if the whole slate reports. A contest read alone moves the estimate about two to five times as much.

| Contest (2027) | On track for D+3.0 | Per 5 points off track: 2028 estimate moves | Why it matters beyond the number |
| --- | --- | --- | --- |
| Special-election average, all year (Democratic margin minus Harris 2024) | **Harris +11.2** | ±0.6 (±1.5 alone) | The best single gauge; it has to stay close to the 2025-26 pace (+12.5 over 110 races) just to be on track |
| Minnesota U.S. Senate special, Nov 2 | **D+12.7** | ±0.4 (±1.3 alone) | Its seat itself: losing it cuts P(55+ Senate) from 66% to 42% with everything else on track |
| Pennsylvania Supreme Court, open seat, Nov 2 | **D+10.2** | ±0.3 (±1.1 alone) | Court control can't flip; a close race is the signal |
| Wisconsin Supreme Court, Apr 6 (only if a conservative runs) | **Liberal +7.2** | ±0.3 (±1.1 alone) | The first reading of the year |
| Kentucky governor (open D seat), Nov 2 | **R+10.3** | ±0.2 (±0.8 alone) | Holding it would be well above track |
| Mississippi governor (open R seat), Nov 2 | **R+8.6** | ±0.2 (±0.8 alone) | A win is about 12 points above track; Mississippi's 2031 pen |
| Louisiana governor runoff, Nov 20 (if a Democrat makes it) | **R+2.6** (weak benchmark: it rests on Edwards's two wins) | ±0.2 (±0.8 alone) | Kennedy's 2028 seat |
| New York redistricting referendum, Nov 2 | Not an environment reading | Pass: P(trifecta) 63%, fail 59% | Up to 3 seats in 2028, and New York's 2031 pen |
| Virginia Senate (21-19 D), Nov 2 | Democrats hold | A loss ends the 2031 map restart | Small seat effect (section 4) |
| New Jersey legislature; Louisiana and Mississippi supermajorities | Democrats hold New Jersey; both Southern supermajorities stand | Not scored | Map and amendment power, not the environment |

| If 2027 comes in... | 2028 estimate | P(trifecta) | P(55+ Senate) | P(D House 2033), no DEM-2 |
| --- | --- | --- | --- | --- |
| Today, before any result | D+3.0 (SD 4.5) | 59% | 63% | 46% |
| 10 points ahead of track | D+6.9 (SD 3.5) | 88% | 88% | 65% |
| 5 ahead | D+5.0 | 77% | 78% | 55% |
| **On track** | **D+3.0 (SD 3.5)** | **60%** | **66%** | **45%** |
| 5 behind | D+1.0 | 42% | 52% | 36% |
| 10 behind | R+0.9 | 25% | 37% | 27% |
| 15 behind (a 2021-sized turn; Minnesota lost) | R+2.9 | 13% | 14% | 20% |

The two plain points:
- **Winning is not the test.** The D+3.0 prior already assumes Democrats keep running far ahead of the 2024 map in off-year races, as they did in 2023 and 2025. Holding Minnesota by 5, or specials averaging Harris +5, would be bad news.
- **2027 can move the estimate by a few points, not more.** Before midterms the off-year record has been an excellent guide. Before presidential years it has been no guide at all (section 3). The rule splits the difference: a full slate 5 points off track moves the 2028 estimate 2 points.

## 1. How the rule works

1. **The benchmark.** Each contest's on-track result has two parts:
   - the state's expected 2028 presidential margin at D+3.0, which is the Senate model's lean plus 3.0;
   - its "off-year excess": how far that kind of contest has run ahead of the state's next presidential result.
   
   The excess comes from three sources:
   - **Courts:** the 2019 and 2023 Wisconsin Supreme Court races and the 2023 Pennsylvania Supreme Court race ran an average of 6.2 points ahead of their states' next presidential margins. That figure is used for the courts and the Senate special.
   - **Governor races:** each keeps 40% of its own state's excess beyond 6.2, the same carry-over the Senate model uses for candidate effects. Kentucky's history is +21 to +33, from Conway and Beshear; Mississippi's is −13 to +23; Louisiana's is +18 and +32, from Edwards.
   - **Specials:** before the two presidential years with data, they ran 2.3 points (2019) and 11.1 points (2023) ahead of the next national change. The rule uses the mean, 6.7, so on track is the 2028 change from 2024 (+4.5) plus 6.7: **Harris +11.2**. Before the three midterms the excess was smaller (−0.5 to +4.7).
2. **The reading.** Each result's distance from its benchmark is averaged, weighting each contest by its noise:
   - specials, SD 5;
   - the Senate special, SD 6.1 (the Senate model's open-seat and regional errors);
   - courts, SD 7;
   - governors, SD 9, because they are the most candidate-driven.
3. **The update.** The 2028 estimate moves by k times that average. k is 0.40 when the whole slate reports. This is the Bayesian gain implied by a shared 4.8-point noise in translating an off-year electorate into a presidential one. After the full slate, the SD falls from 4.5 to 3.5. One contest alone gets a gain of 0.16-0.29, depending on its noise.
4. **The odds.** The moved estimate runs through the Senate, House and redistricting models unchanged. Minnesota's seat, the New York referendum and the Virginia Senate are set to their actual outcomes, since the models carry each as a probability (90%, 45% and 25%).

## 2. Contest by contest

**Minnesota Senate special (November 2, 2027).**
- **On track:** D+12.7, at lean D+2.5, plus 3.0, the 6.2 excess and 1 for the appointee.
- **Each 5 points:** moves the estimate 0.4 on a full slate.
- **The seat:** its own effect is larger than its signal. Held, P(55+) is 66%. Lost by 2 points, P(55+) falls to 42% and P(trifecta) to 49%.
- **Watch:** the appointee in January and the Republican nominee (`2027-races.md`, section 4).

**The special-election average (all of 2027).**
- **On track:** Harris +11.2.
  - The 2025-26 cycle averaged +12.5 over 110 counted races (2025: +13.9 over 67; 2026 through August: +10.4 over 43).
  - So a 2027 at the 2025-26 pace would be about 1 point above track; at 2026's pace, about 1 below.
- **Both ways:** an average of only Harris +5 moves the estimate to D+2.2, and Harris +18 to D+3.9.
- **The series:** `specials-by-year.csv` holds the per-year series for 2017-2026: races, races counted, average and median swing, official results, and the federal subset. It is derived from every D-vs-R special since 2017 (463 races) in The Downballot's trackers, by `tools/specials_extract.py` [SRC-1092].
  - The Downballot asks users to "refrain from reproducing entire spreadsheets", so the race-level extract (date, district, presidential baseline, result, swing) is not committed.
  - The extractor writes it to `dossiers/scenario/.local/`, which is untracked, for checking.
  - Rerun the extractor, then the scorecard, as 2027 results come in.

**Pennsylvania Supreme Court (open seat) and the two retentions.**
- **On track:** D+10.2 for the open seat.
- **Retentions:** not scored. A retention vote turns on the judge and on spending, and only one statewide Pennsylvania judge has lost one since 1968 (`2027-races.md`, section 3).
- **What would count:** a Mundy-kept, Todd-ousted night would be a strong negative signal outside the rule.

**Wisconsin Supreme Court (April 6).**
- **On track:** liberal +7.2, if a conservative enters. If not (none had by July), it is not scored.
- **Timing:** it is the year's first reading. Alone it moves the estimate 1.1 per 5 points.

**Governors.**
- **Kentucky:** on track R+10.3. Holding the seat would be about 10 points above track; losing it by 15 is about 5 below. Each moves the estimate only 0.2.
- **Mississippi:** on track R+8.6. A win by 3 is about 12 above and moves the estimate to D+3.5. Its plan effect is larger: a Democratic governor holds a veto over the 2031 maps (`redistricting-2030-model.md`).
- **Louisiana:** on track R+2.6, the weakest benchmark, built on Edwards's two wins. It is scored only if a Democrat reaches the runoff.

**Not scored for the environment.**
- **New York's referendum:**
  - pass gives P(trifecta) 63% and P(D House 2033) 47%;
  - fail gives 59% and 44%.
  - It is a map, not a mood.
- **The Virginia Senate:**
  - a loss ends the 2031 restart of its map amendment;
  - it moves P(D House 2033) by less than a point, since Virginia is one of twelve pens.
- **The New Jersey legislature, and the Louisiana and Mississippi supermajorities:** amendment and map power, with no environment reading.
- **The mayors:** they test the party's internal argument, not 2028 (`2027-races.md`, section 5).

## 3. Calibration: did off-year results predict the next cycle?

| Off-year | Next cycle | Governor-race swing vs. last presidential | Specials average | Next national change |
| --- | --- | --- | --- | --- |
| 2017 (VA, NJ) | 2018 midterm | +1.8 | +11.2 | +6.5 |
| 2021 (VA, NJ) | 2022 midterm | −12.4 | −4.4 | −7.1 |
| 2025 (VA, NJ) | 2026 midterm | +9.0 | +13.9 | +14.4 |
| 2015 (KY, LA, MS) | 2016 presidential | +7.0 | — | −1.8 |
| 2019 (KY, LA, MS) | 2020 presidential | +21.8 | +4.7 | +2.4 |
| 2023 (KY, MS) | 2024 presidential | +22.2 | +5.2 | −5.9 |

**Before midterms, the relation is close to perfect.**
- The next national change equals the Virginia-New Jersey swing plus 5.1, with a slope of 1.00. The three residuals are within half a point.
- The specials give a slope of 1.07.
- On this record alone, 2027 would carry most of the weight.

**Before presidential years, there is no relation.**
- The slope is −0.01.
- 2023 had the wrong sign: Democrats won Kentucky by 5 and ran ahead in specials, then lost the 2024 popular vote by 1.5.
- Two reasons are plausible: the presidential electorate is larger and younger than the off-year one, and the nominees reset the race.

**Why k = 0.40.** 2028 is a presidential year, so the midterm record cannot be borrowed whole. But it is an open-seat race in which the in-party is the one being judged, as in 2007-08 (not tabulated) rather than 2023-24, when the incumbent ran again. The rule sets k at 0.40, nearer the presidential record than the midterm one.

| Full-slate gain k | 2028 estimate after a 5-point miss across the board | SD after |
| --- | --- | --- |
| 0.2 | D+2.0 | 4.0 |
| **0.4 (pre-registered)** | **D+1.0** | **3.5** |
| 0.7 | R+0.4 | 2.6 |

## 4. Signals that call for contingency preparation, not just new numbers

Each signal below is stated now, with what it would change. Each is a question for Espen, not a decision. D1 (#80) stays Espen's.

1. **Minnesota lost, and the environment under D+1 by mid-2028.**
   - **The test as first framed:** whether option B's 53-56 planning range is too high.
   - **Option B itself holds:**
     - with a Democratic president, the Senate still averages 54.9, and P(53+) is 90%;
     - even at R+6 the average stays at 53.8, because a Democratic president in a bad year implies a good draw for Senate races too.
   - **What changes is D2-F:**
     - **Defection room shrinks:** P(D2-F has the votes) falls from 61% to 41%. The average Senate shrinks from 56.5 to 54.9 seats, so it can absorb about one and a half fewer defections, against the same whip count;
     - **A Democratic president becomes a coin flip:** 50%, from 69%.
   - **The response (contingency preparation; the 2029 premise stays a trifecta):**
     - ready D2's written fallback (G, the democracy carve-out) and its opening offer (C) to be used if needed;
     - step up preparation of the Republican-presidency branch (`2028-republican-branch.md`).
2. **The full slate 5 or more points behind track** (estimate D+1 or lower):
   - **The odds:** P(trifecta) falls below a coin flip (42%).
   - **The response:** contingency preparation. Give more 2028 preparation time to work that pays off under both presidencies. The 2029 premise stays a trifecta.
3. **The full slate 10 or more points ahead** (estimate D+7 or higher):
   - **The odds:** P(55+) reaches 88%.
   - **The question it raises:** whether #80's planning band should reach above 56 for the 2029-30 Congress. The 2030 and 2032 drops still argue against planning the later Congresses on it (`2030-2034-control.md`).
4. **Kentucky lost by more than 10, and Mississippi and Louisiana each lost by more than 10:**
   - **The numbers:** each is about 5 points below track, which moves the estimate little.
   - **The plan question:** it would say the 2026 Deep South shift was federal and anti-Trump, so 2032's Class 2 defense in Mississippi, South Carolina, Kansas, Iowa and Alaska is the place to shift plan weight (`senate-model-2028.md`, section 7, option d).
5. **The New York referendum fails.** That leaves P(D House 2033) about 3 points below a pass (44% against 47%); a Virginia Senate loss adds little. It would raise the weight on DEM-2 Title II (`redistricting-2030-model.md`), since the 2031 maps would then rest more on court-drawn and Republican-drawn states.
6. **The special-election average below Harris +5 for 2027:**
   - **On its own:** it is 6.2 points below track, which moves the estimate to D+2.2.
   - **With a generic ballot under D+1 by spring 2028:** apply signal 1.

## 5. Limits

- **The calibration rests on six off-years** and two kinds of contest: Virginia and New Jersey governors before midterms, Southern governors before presidential years. It proves the off-year signal's strength before midterms. Its weight before a presidential year (k = 0.40) is a judgment, set in advance so it cannot be bent afterwards.
- **The special-election series is one compiler's.**
  - **Baselines:** the presidential margins by legislative district are The Downballot's calculations from Dave's Redistricting App; no official source publishes them for most states.
  - **Results:** the tracker marks which results are the official canvass. In 2025-26, 92 of the 111 races are marked official.
  - **Cross-check:** all seven federal 2025-26 specials (FL-1, FL-6, VA-11, AZ-7, TN-7, GA-14, NJ-11) match published results to within 0.1 point. The comparison was against Wikipedia's tables, because the state election offices' pages could not be retrieved.
  - **Two sheet errors:** the averages recomputed from the race rows match the tracker's own for every off-year. 2018 and 2020 differ (+11.0 against +9.9, +5.7 against +5.0) because a few sheet rows carry a typed margin that contradicts their vote shares, such as Alabama HD-21 in 2018. The extractor recomputes margins from the shares.
  - **The old figures:** the press figures this PR first used (SRC-1085 to SRC-1088) agree with the series within 1 point in every year (for example, 2023: +5.2 in the series against the 5.7 used before).
- **Two benchmarks rest on unconfirmed figures:**
  - **Pennsylvania 2023:** the court excess uses McCaffery's unofficial 53-47 [SRC-1091].
  - **Virginia and New Jersey 2025:** both governor margins come from infoboxes not marked certified.
- **The governor benchmarks are the weakest.** They rest on two or three races per state, dominated by Beshear and Edwards. They carry little weight for that reason.
- **The rule reads only the environment.** It does not judge nominees, scandals or turnout operations; a result explained by one of those should be read with that caveat.

## Next questions

1. **Monthly reruns in 2027.** The per-year special-election series is committed (`specials-by-year.csv`). Should the scorecard be rerun monthly as 2027 specials post, with the running average logged against Harris +11.2?
2. **A 2007-08 row.** The open-seat presidential year whose in-party was unpopular is the closest analog to 2028. Adding Kentucky 2007, Mississippi 2007 and Louisiana 2007 would test whether k = 0.40 is too low.
3. **The Wisconsin decision in January.** If no conservative files, drop Wisconsin and note that the slate's gain falls slightly.
4. **A generic-ballot rule for 2028.** Signal 1 needs a stated mid-2028 environment. Should the scorecard add a second, pre-registered step that folds in the generic-ballot average on June 1, 2028?
