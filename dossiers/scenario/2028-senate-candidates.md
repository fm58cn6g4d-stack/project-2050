# 2028 Senate candidates: who is running, primary risks, and how much nominee quality could move the map

Role: for each competitive 2028 Senate race in the Senate model (`senate-model-2028.md`), the declared and likely candidates, the risk that a weak nominee wins a primary, and incumbent retirements to watch; then a rough candidate-quality adjustment in points, with its reasoning, and which races are most sensitive to it. Status: draft (stage B), as of November 8, 2026, five days after the midterms. **Analysis only.** It does not re-tune `senate_model.py`; section 4 lists adjustments for b-3 to test. Sensitivities come from `tools/senate_candidates_2028.py`, which calls the model unchanged through its `overrides` argument; tables in `2028-senate-candidates-outputs.md`.

**How to read the sources.** Almost everything here is news reporting from the week of the midterms, cited by publisher and date; most is licensed and recorded as citation rows only. Candidate fields this early are thin: no 2028 head-to-head polls exist in any of these states, and several "fields" are a list of names floated by reporters. No second-Trump-administration executive-branch source is used (`DEC-2026-10-30-01`); the only government sources are FEC filings, which are data. Cash figures are the model's FEC extract for September 30, 2026 (`senate-model-fec-cash.csv`) [SRC-0577]. "(Judgment)" marks this file's own reading.

**One correction to the request.** Michigan has no 2028 Senate race: its Class 2 seat was up in 2026 and Slotkin's Class 1 seat is up in 2030, so it is not in the model's 2028 list (`senate-model-2028.md`, section 1).

## In brief

- **Three races are most sensitive to nominee quality: North Carolina, Wisconsin and Nevada**, then Pennsylvania and Arizona. Each point of margin there moves the chance of 55+ Democratic seats by about 1.2-1.5 points in a neutral year, and the race itself by about 6 points (section 3). Ohio is as sensitive race by race, but starts further behind.
- **Taken together, nominee quality is the largest unmodeled swing in the Senate forecast.** A 2-point shift toward Democrats in every competitive race at once takes P(55+) from 39% to 59% at a neutral environment; 2 points the other way takes it to 21%. The back-test found Democrats outran the model by about 4 points in 2018-24 (`model-credibility.md`).
- **The biggest open questions are retirements, not primaries.** Kelly (Arizona) and Warnock (Georgia) are weighing presidential runs; Brown (Ohio), 73, has not said whether he will run for the full term, and the model assumes he does; Johnson (Wisconsin), Grassley (Iowa) and Murkowski (Alaska) may retire.
- **The main primary risks are on both sides.** For Democrats, Pennsylvania: party leaders are coalescing around Rep. Chris Deluzio against Fetterman, who has hinted he could run outside the party. For Republicans, an open Arizona seat (a Kari Lake-type nominee) and an open Wisconsin seat.
- **Recommended for b-3 (section 4):** add a turnout chance for Brown (about 0.7), keep Kelly's at 0.75 and Johnson's at 0.25, and test a uniform nominee-quality term of +1 and +2 points for Democrats, then replace it race by race once the 2028 primaries settle the nominees.

## 1. The evidence on candidate quality

**What moves the margin, and by how much.**
- **Candidate quality matters less than it did, but still about 3 points on average.** Split Ticket's wins-above-replacement models put the average candidate effect at about 6 points per race in 2016 and about 3 in 2024; races with effects over 10 points fell from 59 to 13, and none passed 20 in 2024 [SRC-1135]. Split Ticket puts incumbency at about 3 points of margin in 2024 [SRC-1137].
- **Incumbency has shrunk.** One study finds the Senate incumbency advantage peaked in the 2000s and was not statistically significant for 2010-16, while the effect of the presidential vote on the Senate vote rose from 0.38 in the 1980s to 0.72 (Sievert and McKee, 2018) [SRC-1140].
- **Weak nominees still cost seats.** Split Ticket's 2022 model found Republicans "should have won 53 seats" but won 49; candidate quality decided Nevada, Arizona, Georgia and Pennsylvania [SRC-1136]. Its per-candidate scores were revised in December 2024, so this file uses them for direction only. Inside Elections' 2022 vote-above-replacement scores put the Republican nominees in Arizona, Georgia and New Hampshire about 3-4 points below replacement and Kelly, Warnock and Hassan about 3-4 above [SRC-1138].
- **Extreme primary winners lose ground.** In U.S. House races 1980-2010, nominating the more extreme candidate in a close primary cut the party's general-election vote share by about 9-13 points, mostly in open seats (Hall, 2015) [SRC-1134]. That is a House estimate in a less nationalized era; this file treats it as an upper bound for 2028 Senate races (judgment).
- **Split tickets are rarer but not gone.** In 2024, 4 of 34 Senate races went to a different party than the state's presidential winner: Arizona, Michigan, Nevada and Wisconsin (Pew, 2024) [SRC-0569]. The 2024 Arizona case is the clearest recent nominee effect: Gallego beat Lake by 2.4 points while Trump carried the state by 5.5, a gap of about 8 [SRC-0576] [SRC-0459].

**How the model handles it now.** The candidate effect is incumbency (2 points) plus 40% of the holder's last over- or under-performance, capped at 6; there is no term for the quality of the challenger or of an open-seat nominee (`senate-model-2028.md`, section 2). So the model captures Kelly's or Warnock's record but not a weak Republican nominee against them, and gives an open seat no quality term at all.

## 2. Race by race

Ordered by the model's P(D) in a neutral environment. "Model" gives the model's current P(D) at neutral and at D+3.

### New Hampshire: Hassan (D). Model 84% / 93%
- **Incumbent:** has a 2028 committee with $2.0 million on hand; no direct statement on her plans found.
- **Republicans:** businessman Vikram Mansharamani has filed for 2028 (FEC, January 2025) [SRC-1110]. Gov. Kelly Ayotte, just reelected, is seen as a possible challenger; an analyst says she "has to look ahead to 2028" (WCAX, November 4, 2026) [SRC-1111].
- **Primary risk:** low on both sides (judgment).
- **What would move it:** Ayotte running. A popular sitting governor is the one Republican who would offset Hassan's edge; suggested test −2 (section 4).

### Georgia: Warnock (D). Model 71% / 85%
- **Incumbent:** has a 2028 committee; also openly weighing a presidential run: "in a matter of months... I'll be in a race" (Newsweek, October 30, 2026) [SRC-1104] [SRC-1103]. In an AJC/UGA poll, 74% of likely Democratic voters favored a Warnock presidential run but 54% of all likely voters opposed one (AJC, October 23, 2026) [SRC-1105]. $4.1 million on hand.
- **Republicans:** no post-midterm reporting on the field. In 2026, Ossoff beat the Trump-backed Rep. Mike Collins 59-41 (ABC News, November 5, 2026) [SRC-1106].
- **Primary risk:** a Trump-endorsed nominee in the Walker or Collins mold (judgment).
- **Retirement to watch:** whether Warnock runs for president. Unlike Arizona, this file has not found that Georgia lets him run for both; that needs checking. The model assumes he runs for the Senate (p_run 1.0).

### Nevada: Cortez Masto (D). Model 59% / 76%
- **Incumbent:** filed a 2028 statement of candidacy in July 2026; "I'm not done fighting" (Semafor, November 6, 2026) [SRC-0976]. Not an explicit commitment. $3.5 million on hand.
- **Republicans:** Gov. Lombardo was seen as the top recruit (Nevada Current, April 3, 2026) [SRC-1108]; he lost to Aaron Ford about 52-44 (AP, November 4, 2026) [SRC-1109]. No other named candidates.
- **Primary risk:** a weak Republican nominee is the likely case; the same Nevada Current piece calls the bench "a perennially shallow pool" (judgment from reporting).
- **What would move it:** a weak Republican field, +1 to +2 toward Cortez Masto.

### Pennsylvania: Fetterman (D). Model 56% / 73%
- **Incumbent:** "let's revisit after the midterm"; he is "not a Republican" (CBS News, September 27, 2026) [SRC-1112]. He addressed a Republican convention by video, and CNN raised the possibility that he runs as a Democrat, an independent "or even Republican" (CNN, September 13, 2026) [SRC-1113].
- **Democratic challengers:** Rep. Brendan Boyle ruled out a run on November 4, leaving Rep. Chris Deluzio, just reelected with 63%, as the front-runner (PennLive, November 6, 2026) [SRC-1114]. Others mentioned: Conor Lamb (denies plans), Reps. Madeleine Dean and Summer Lee, Speaker Joanna McClinton and state Rep. Malcolm Kenyatta (NBC10, November 7, 2026) [SRC-1115].
- **Polling:** 69% of Democratic likely voters viewed Fetterman unfavorably; 49/43 favorable among all likely voters (Inquirer/NYT/Siena, August 25, 2026) [SRC-1116].
- **Republicans:** no declared field.
- **Primary risk: the highest in the map, on the Democratic side.** Three branches (judgment):
  - Fetterman renominated as a Democrat after a bruising primary: about −1 to −2 against the lean (an alienated base).
  - Fetterman beaten in the primary, and the race open with a Deluzio-type nominee: about 0 (no incumbency, no brand damage).
  - Fetterman beaten and running as an independent or Republican: −3 to −6 toward the Republican, depending on his share. This is the one scenario that could cost Democrats a seat they would otherwise win.
- The model already widens this race (extra error 3) and sets its candidate effect to 0.

### Arizona: Kelly (D). Model 54% / 71%
- **Incumbent:** will decide on the Senate and on a presidential run "on the other side of this election"; Arizona lets him run for both, and his Senate signatures are not due until March 20, 2028, after the early presidential primaries (Axios Phoenix, October 22, 2026) [SRC-0581]. "I am thinking about it" (Deseret News, October 28, 2026) [SRC-1101]. $26.5 million on hand, the most of any 2028 incumbent.
- **Republicans:** a Republican consultant says some candidates would run only for an open seat [SRC-0581]. No major recruits named; Kari Lake is listed as a potential candidate [SRC-0564]. In 2026, Hobbs beat the Turning Point-backed Andy Biggs 55.6-42.5 (New York Times, November 4, 2026) [SRC-1102].
- **Primary risk:** a Lake-type nominee, most likely if the seat opens (judgment from the 2022, 2024 and 2026 pattern).
- **What would move it:** if Kelly runs, a weak Republican, +1 to +2; if the seat opens, a weak Republican largely offsets the lost incumbency (+2 to +3 against the open-seat baseline).

### North Carolina: Budd (R). Model 45% / 65%
- **Incumbent:** expected to run; his spokesman says the campaign is "very confident" (WRAL, November 8, 2026) [SRC-1117]. He moved his chief of staff to his political operation in December 2025 (News & Observer, December 3, 2025) [SRC-1118]. $0.7 million on hand.
- **Republican challenger:** former Rep. Mark Walker has a 2028-cycle committee with no reported money (FEC) [SRC-1119]. He took about 9% against Budd in the 2022 primary. Low risk (judgment).
- **Democrats:** no named 2028 candidates. In 2026, Roy Cooper won the other seat by about 20 points; a Cooper strategist calls Budd "the most vulnerable Republican" in the Senate if Democrats deliver on affordability [SRC-1117].
- **What would move it:** the Democratic nominee. A proven statewide winner, +1 to +2; an untested nominee, 0. This is the race where nominee quality matters most for 55+ (section 3).

### Wisconsin: Johnson (R). Model 38% / 57%
- **Incumbent:** "I don't want to... you can't say never" (2025) [SRC-0586]. No newer statement found. The model gives him a 25% chance of running. $1.1 million on hand.
- **Democrats:** former state party chair Ben Wikler is exploring a run, which has "rankled" some insiders (NBC News, July 29, 2026) [SRC-0573]; a minor democratic-socialist candidate has filed.
- **Republicans:** no named successors. The Trump-endorsed Tom Tiffany lost the 2026 governor's race to David Crowley 54-46 (AP, November 4, 2026) [SRC-1121].
- **Primary risk: both sides, if the seat opens.** A hard-right Republican nominee, +1 to +2 toward Democrats; a Democratic nominee from the party's left (the 2026 governor's primary was decided by about 4,000 votes against a democratic socialist), −1 to −2 (judgment). Net about 0, but wider: suggested extra error of 2-3 points, as for Pennsylvania.

### Ohio: Brown (D). Model 21% / 38%
- **Incumbent:** Brown beat Husted 50.0-45.2 in the 2026 special (NPR, November 4, 2026) [SRC-1122]; he is assured only two years and "will have to decide" on 2028 (Statehouse News Bureau, November 3, 2026) [SRC-1123]. He is 73. **The model assumes he runs (no turnout chance).**
- **Republicans:** none declared. Sen. Bernie Moreno, likely to lead the Republican campaign committee, joked it would be "tempting" to beat Brown again (Semafor, October 20, 2026) [SRC-1124]. Strategists in both parties expect Ohio to be competitive (Politico, November 6, 2026) [SRC-1141].
- **What would move it:** Brown retiring. His +4.2 candidate effect would go, and the seat would be an open race in a state about 9 points right of the nation. Suggested p_run about 0.7 (judgment: age, a new full-term race two years after a $400-million campaign, and no statement either way).

### Iowa: Grassley (R). Model 5% / 12%
- **Incumbent:** will decide in 2027 [SRC-0572]; "is not resigning" before Democratic Gov.-elect Rob Sand takes office (Iowa Capital Dispatch, November 5, 2026) [SRC-1125]. The model gives him a 35% chance of running.
- **If open:** names floated are Rep. Ashley Hinson, who lost the 2026 Senate race to Josh Turek, and Iowa House Speaker Pat Grassley, the senator's grandson [SRC-1125]. No Democrats named.
- **What would move it:** a crowded Republican primary, 0 to +1 for Democrats. Low leverage on 55+ (section 3).

### Alaska: Murkowski (R). Model 3% / 6% (Democratic win; the model's branch logic also counts independents)
- **Incumbent:** "pondering" reelection amid retirement speculation; she endorsed the Democrat for governor in 2026 (Politico, October 28, 2026) [SRC-1126]. Her approval fell to 33-60 in a July 2025 poll (Alaska Beacon, August 5, 2025) [SRC-0590].
- **Challenger:** Gov. Dunleavy is reported to be "primed" to run, with Trump's encouragement, on unnamed sources (Fox News, 2025) [SRC-0584]; he has not declared.
- **The rules matter more than the names.** The repeal of top-four primaries and ranked-choice voting (Measure 2) was trailing 48-52 with about 72% counted; certification is November 25 (Alaska Public Media, November 4, 2026) [SRC-1127]. If it fails, Murkowski avoids a closed Republican primary against Dunleavy. The model already handles this through its Alaska branches (`senate-model-2028.md`, section 5).

### Florida: Moody (R). Model 2% / 6%
- **Incumbent:** won the 2026 special 50.9-48.0 over Angie Nixon (New York Times/AP) [SRC-1129].
- **Democrats:** Nixon says she is undecided about a rematch. Rep. Jared Moskowitz kept the door open (Washington Examiner, November 5, 2026) [SRC-1130].
- **What would move it:** the Democratic nominee. A Moskowitz-type moderate against Nixon's 2026 run is worth perhaps +1 to +2 (judgment). Low leverage: the seat flips only in a large wave.

### Kansas: Moran (R). Model <1% / 2%
- **Incumbent:** "up for reelection in 2028"; he keeps Trump "at a distance" (Kansas City Star, November 5, 2026) [SRC-1131]. In 2026, Democrat Adam Hamilton beat Sen. Roger Marshall 51-46 in the other seat (NBC News, November 4, 2026) [SRC-1132].
- **What would move it:** almost nothing in the 2028 range of environments; the 2026 upset was against a weaker incumbent in a wave year (judgment).

### Also up: the Tennessee special (R, safe)
Governor-elect Blackburn will appoint her successor to serve until the November 2028 special; her shortlist is Glenn Jacobs, Reps. Tim Burchett and Chuck Fleischmann, and Stuart McWhorter. Burchett says he will run in 2028 even if not appointed (Nashville Banner, November 7, 2026) [SRC-1133]. That sets up a possible appointee-versus-Burchett primary, which matters for Tennessee's delegation but not for control.

## 3. Which races are most sensitive

From `2028-senate-candidates-outputs.md`: each race shifted by 2 points toward either party, one at a time, with everything else as in the Senate model.

| Race | P(D) per point of margin (neutral) | P(55+) per point (neutral) | P(55+) per point (D+3) |
| --- | --- | --- | --- |
| North Carolina | +6.5 | +1.5 | +1.3 |
| Wisconsin | +5.8 | +1.3 | +1.2 |
| Nevada | +6.3 | +1.2 | +1.1 |
| Pennsylvania | +6.0 | +1.2 | +1.1 |
| Arizona | +5.9 | +1.2 | +1.1 |
| Ohio | +4.8 | +1.0 | +1.1 |
| Georgia | +5.5 | +0.9 | +0.8 |
| New Hampshire | +4.1 | +0.6 | +0.5 |
| Iowa, Florida, Alaska, Kansas | under +3.2 | +0.4 or less | +0.4 or less |
| **All but Kansas at once** | — | **+9.3** (21% at −2, 59% at +2) | **+8.7** (49% to 84%) |

Reading it (analysis):
- **The 55+ threshold runs through North Carolina, Wisconsin and Nevada.** They are the closest to 50-50 among the seats Democrats need beyond the first 51, so a point there buys the most.
- **Senate control barely moves:** it is 96% in a neutral year and 99% at D+3, so no single nominee changes it.
- **The correlated case is the one that matters.** Nominee quality is not independent across races: a party whose primaries reward the same kind of candidate pays the price everywhere at once, as Republicans did in 2022 [SRC-1136]. The all-at-once row is the honest range.

## 4. Adjustments for b-3 to test (not applied)

| # | Change | Value | Reasoning |
| --- | --- | --- | --- |
| 1 | Turnout chance for Brown (Ohio) | p_run 0.7 | No statement; age 73; a second costly race in two years. The model now assumes he runs |
| 2 | Keep Kelly's p_run 0.75 and Johnson's 0.25; consider Warnock 0.85 | — | Reporting since the model was built confirms both are undecided; Warnock is weighing a presidential run and Georgia's rule on running for both is unchecked |
| 3 | A uniform nominee-quality term, toward Democrats | +1 and +2 points in every competitive race | The back-test's 4-point Democratic over-performance (2018-24) and the 2022 pattern; the average effect is now about 3 points [SRC-1135] |
| 4 | Pennsylvania branch: Fetterman beaten in the primary and running outside the party | −3 to −6, with a 10-20% chance (judgment) | The one scenario that loses a seat Democrats would otherwise win |
| 5 | Wisconsin open seat: wider error | extra error 2-3 | Primary risk on both sides nets about 0 but widens the range |
| 6 | Arizona open seat with a weak Republican nominee | +2 to +3 against the open-seat baseline | The 2024 Lake gap (about 8 points against the presidential result) |
| 7 | New Hampshire with Ayotte as the nominee | −2 | A popular sitting governor |
| 8 | Nevada with a weak Republican field | +1 to +2 | Lombardo's 2026 loss leaves no proven statewide Republican |

Items 3-8 should be replaced by observed nominees after the 2028 primaries (most by August 2028; Arizona's filing deadline is March 2028).

## 5. Limits

- The candidate fields are early and partly speculative; names floated in the week after a midterm often do not run.
- No 2028 head-to-head polls exist; quality judgments rest on past results and reporting, not voters' current views.
- The adjustments are judgment anchored to published estimates, not fitted values.
- The sensitivity runs use the model as it stands, including its assumptions on which incumbents run.

## Next questions

1. **Georgia's rule:** can Warnock appear on the 2028 ballot for both president and Senate, as Kelly can in Arizona?
2. **Brown's decision:** any signal before 2027 filing? Ohio's filing deadline for 2028 needs checking.
3. **Ayotte:** does she rule a Senate run in or out in 2027?
4. **A fitted nominee-quality term (`model-credibility.md`, next question 1):** estimate it from 2010-24 WAR scores and decide whether it applies once nominees are known.
