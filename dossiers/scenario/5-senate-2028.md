# The 2028 Senate map and the Senate of 2029

Role: the seats up in 2028, how the 2024 and 2026 results bear on each, and a scenario estimate of the Senate a 2029 Democratic government would work with. It is the evidence for the proposed update to D1 (`d1-planning-scenario.md`). Status: draft (stage B follow-up), November 8, 2026. The estimate is **this project's own exploratory arithmetic** (`tools/senate_2028_sim.py`), not a published forecast; no rater has published 2028 Senate ratings yet. 2026 margins are unofficial.

## In brief

- **35 races in 2028:** the 34 regular Class 3 seats plus, probably, a Tennessee special for Blackburn's seat, since she won the governorship (the appointee serves "until the next November election," read here as 2028; recheck) [SRC-0564] [SRC-0571]. **Republicans defend 19, Democrats 16**, counting the Ohio seat Brown won in the 2026 special, which is up again for the full term [SRC-0568].
- **Democrats not up in 2028: 38, or 40 if they win the uncalled Alaska and Mississippi seats**, both Class 2 and next up in 2032. Alaska leans Peltola and Mississippi Colom (`1-results.md`), so 40 is the more likely base.
- **A Democratic majority in January 2029 is likely in every environment where a Democrat wins the presidency.** From 40 seats not up: about 54 seats on average in a tied national vote, about 55-56 at D+3, about 57 at D+6. The structural risks are Ohio, Arizona and Nevada; the openings are Wisconsin and North Carolina, then Iowa.
- **The map is not 2026.** Since 1994, a midterm environment reverted by about 4 to 8 points in the next presidential year in four of six cases; it was about unchanged from 2022 to 2024, and it grew from 2006 to 2008, an open-seat year after an unpopular two-term president and the closest analog to 2028 [SRC-0570]. Senate races now follow the state's presidential vote about 90% of the time [SRC-0569].

## 1. The seats

2022 and 2024 margins from Wikipedia's results tables [SRC-0565] [SRC-0459]; 2026 statewide margins from NBC (unofficial) [SRC-0574] [SRC-0483]; candidate reports from the sources named. "P(D)" is the estimated chance a Democrat wins at a national D+3 (section 3).

**Seats where the outcome is in doubt**

| State | Holder (January 2027) | 2022 | 2024 pres. | 2026 statewide | What is known | P(D) at D+3 |
| --- | --- | --- | --- | --- | --- | --- |
| Wisconsin | Johnson (R) | R+1.0 | R+0.9 | Gov D+8.0 | Johnson has signaled he will not run; Wikler (D) is considering it [SRC-0573] | 0.60 |
| North Carolina | Budd (R) | R+3.2 | R+3.2 | Sen D+19.6 | Budd running; a primary challenger filed [SRC-0564] | 0.54 |
| Arizona | Kelly (D) | D+4.9 | R+5.5 | Gov D+13.1 | Kelly weighing a presidential run [SRC-0564] | 0.67 |
| Nevada | Cortez Masto (D) | D+0.8 | R+3.1 | Gov D+7.6 | Intent unknown | 0.67 |
| Georgia | Warnock (D) | D+2.8 (runoff) | R+2.2 | Sen D+18.0; Gov D+8.6 | Intent unknown | 0.77 |
| Pennsylvania | Fetterman (D) | D+4.9 | R+1.7 | Gov D+22.1 | Many possible primary challengers [SRC-0564] | 0.81 |
| New Hampshire | Hassan (D) | D+9.2 | D+2.8 | Sen D+13.7; Gov R+4.3 | Intent unknown | 0.81 |
| Ohio | Brown (D, won the 2026 special) | (2026 special D+4.8) | R+11.2 | Sen D+4.8; Gov D+7.9 | Up for the full term | 0.35 |
| Iowa | Grassley (R) | R+12.2 | R+13.2 | Sen D+4.1; Gov D+11.0 | Grassley, 95 in 2028, decides in 2027 [SRC-0572] | 0.15 |
| Florida | Moody (R, won the 2026 special) | (2026 special R+2.9) | R+13.1 | Sen R+2.9; Gov R+1.3 | Up for the full term | 0.06 |
| Alaska | Murkowski (R) | R+7.4 (final round) | R+13.1 | Senate uncalled | Gov. Dunleavy floated as a challenger [SRC-0564] | 0.04 |
| Kansas | Moran (R) | R+23.0 | R+16.1 | Sen D+5.0 | Intent unknown | 0.04 |
| South Carolina | Scott (R) | R+25.9 | R+17.9 | Sen D+4.5 | Scott running [SRC-0564] | 0.02 |

**Safe in every scenario modeled.** Democratic: California, Colorado, Connecticut, Hawaii, Illinois, Maryland, New York, Oregon, Vermont, Washington. Republican: Alabama, Arkansas, Idaho, Indiana, Kentucky, Louisiana, Missouri, North Dakota, Oklahoma, South Dakota, Tennessee (special), Utah.

Fox News coverage lists New Hampshire, Nevada, Arizona, Georgia, Pennsylvania and Ohio as Republican targets, and Wisconsin, Iowa and North Carolina as seats Republicans must defend [SRC-0566]; NBC's pre-election preview named the same core [SRC-0568]. Nate Silver's November 6 first look (ratings paywalled, not read) frames three environments, a repeat of 2026, a D+5 year and an R+3 year [SRC-0567].

## 2. History as a guide

| Midterm (House vote) | Next presidential year (House vote; presidential margin) | Change toward the midterm's losing party |
| --- | --- | --- |
| 1994 R+7.0 | 1996 R+0.4; Clinton D+8.5 | about 6.6 |
| 2006 D+6.4 | 2008 D+10.6; Obama D+7.3 | none: the wave grew by 4.2 |
| 2010 R+6.6 | 2012 D+1.4; Obama D+3.9 | about 8.0 |
| 2014 R+5.1 | 2016 R+0.9; Clinton D+2.1 | about 4.2 |
| 2018 D+8.7 | 2020 D+3.0; Biden D+4.5 | about 5.7 |
| 2022 R+2.6 | 2024 R+2.5; Trump R+1.5 | about 0 |
| **2026 about D+13** | 2028: ? | Reversion of 0-8 points (4-8 in the four cases with substantial reversion) would leave about D+5 to D+13; growth, as in 2008, more |

House vote from Brookings's *Vital Statistics on Congress* [SRC-0570]; presidential margins from Wikipedia. The Clerk of the House's 2006 figures give about D+8.0 rather than D+6.4, which would make the 2008 growth about 2.6 points rather than 4.2; recheck the table. Small differences from `1-results.md` (2018 D+8.7 here against D+8.6; Ohio D+4.8 and Kansas D+5.0 here, from NBC, against D+4.9 and D+5.1 from civicAPI) are differences between sources, not typos. Two Brookings rows on Senate seat changes look inconsistent and are not used. Split Senate results: none in 2016, one in 2020, four of 34 in 2024; since 2012, 91% of Senate races matched the state's latest presidential vote (Pew) [SRC-0569].

## 3. The estimate

**Method** (labeled assumptions, `tools/senate_2028_sim.py`). Each seat's expected Democratic margin = 0.7 × the state's 2024 presidential lean + 0.3 × its 2026 statewide margins relative to the D+13 national House vote, plus the national environment E (the 2028 Democratic presidential margin) and an incumbency adjustment (+3 points for an elected incumbent; smaller for appointees, Fetterman and Murkowski's special case; none for seats treated as open, Wisconsin and Iowa). Each of 200,000 runs draws a shared national error (SD 2.5 points) and a state error (SD 7). Sensitivity runs (weights 0.5 to 1.0, SDs 6-8 and 2-4) moved the probabilities by up to 10 points.

**Democratic-caucus seats in January 2029**

| Environment | Not up (AK, MS result) | Mean | 90% range | P(≥50) | P(≥52) | P(≥55) | P(≥58) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| R+3 | 38 (R wins both) | 50.7 | 48-54 | 0.74 | 0.32 | 0.02 | 0 |
| R+3 | 40 (D wins both) | 52.7 | 50-56 | 0.97 | 0.74 | 0.16 | 0 |
| Even | 38 | 52.1 | 49-55 | 0.92 | 0.63 | 0.09 | 0 |
| Even | 40 | 54.1 | 51-57 | 1.00 | 0.92 | 0.42 | 0.03 |
| D+3 | 38 | 53.5 | 51-56 | 0.99 | 0.87 | 0.30 | 0.01 |
| D+3 | 40 | 55.5 | 53-58 | 1.00 | 0.99 | 0.72 | 0.13 |
| D+6 | 38 | 54.9 | 52-58 | 1.00 | 0.97 | 0.60 | 0.06 |
| D+6 | 40 | 56.9 | 54-60 | 1.00 | 1.00 | 0.92 | 0.37 |

**Reading it for the plan.** D1 plans for a Democratic president from January 2029, which in practice means a national environment of about even or better; an R+3 year is shown for completeness, and in it the presidency itself is unlikely. Conditional on a Democratic president and the more likely 40-seat base:
- a Senate of **about 53-57 seats** is the central range (even to D+6);
- **52 or more** is very likely (above 90%), and **50 plus the Vice President** almost certain;
- **58 or more** is an upside that needs a D+6 year (about 13-37%), and **60** is remote (6% at D+6).
From the 38-seat base, every figure drops by about two seats.

**What would change it.** Grassley or Johnson running again (moves Iowa or Wisconsin about 3 points toward Republicans); weak nominees from primaries (Pennsylvania, Oklahoma, Alaska); Kelly leaving the Senate race to run for president; new vacancies; the Tennessee special's timing. The 2032 class is a separate exposure: Democrats will defend the six Republican-held seats they won in 2026 (Texas, North Carolina, South Carolina, Kansas, Iowa, Maine), and Alaska and Mississippi if they win them, all elected in a D+13 year.

## 4. Recheck

Alaska and Mississippi calls (they set the 38 or 40 base); the Tennessee special's timing and appointee; certified 2026 margins; the final national House vote; retirement decisions (Grassley in 2027, Johnson, Murkowski, Kelly); the first published 2028 ratings (Cook, Sabato, Inside Elections), expected in the coming months.
