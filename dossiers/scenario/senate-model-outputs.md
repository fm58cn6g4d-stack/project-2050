# Senate model outputs (generated)

Role: the tables `tools/senate_model.py --write` produces, read by `senate-model-2028.md` and `2030-2034-control.md`. Status: generated; do not edit by hand. Every figure is this project's exploratory scenario arithmetic, not a forecast. n = 20000 simulated elections per row, seeded.

## 1. Inputs as computed

| Race | Holder | Lean | Candidate effect | P(incumbent is nominee) | P(D) neutral | P(D) D+3 |
| --- | --- | --- | --- | --- | --- | --- |
| HI | Schatz (D) | +26.1 | +6.0 | 100% | 100% | 100% |
| MD | Van Hollen (D) | +25.5 | +3.1 | 100% | 100% | 100% |
| VT | Welch (D) | +32.4 | +6.0 | 100% | 100% | 100% |
| CA | Padilla (D) | +21.2 | +1.9 | 100% | 100% | 100% |
| WA | Murray (D) | +18.3 | +1.2 | 100% | 100% | 100% |
| CO | Bennet (D) | +11.6 | +3.8 | 100% | 99% | 100% |
| IL | Duckworth (D) | +11.7 | +3.4 | 100% | 99% | 100% |
| CT | Blumenthal (D) | +12.1 | +1.9 | 100% | 99% | 100% |
| NY | Schumer (D) | +11.9 | +1.3 | 100% | 99% | 100% |
| OR | Wyden (D) | +10.5 | +2.7 | 100% | 99% | 100% |
| NH | Hassan (D) | +1.4 | +4.5 | 100% | 84% | 93% |
| GA | Warnock (D) | -1.0 | +4.3 | 100% | 71% | 85% |
| NV | Cortez Masto (D) | -1.9 | +3.3 | 100% | 59% | 76% |
| PA | Fetterman (D) | +1.1 | +0.0 | 100% | 56% | 73% |
| AZ | Kelly (D) | -3.7 | +5.8 | 75% | 54% | 71% |
| NC | Budd (R) | -0.0 | -0.7 | 100% | 45% | 65% |
| WI | Johnson (R) | -1.9 | +0.1 | 25% | 38% | 57% |
| OH | Brown (D) | -9.1 | +4.2 | 100% | 21% | 38% |
| IA | Grassley (R) | -10.3 | -0.2 | 35% | 5% | 12% |
| AK | Murkowski (R) | -11.9 | branch model | 100% | 3% | 6% |
| FL | Moody (R) | -11.6 | -0.6 | 100% | 2% | 6% |
| KS | Moran (R) | -13.5 | -2.6 | 100% | <1% | 1% |
| MO | Schmitt (R) | -17.8 | +1.1 | 100% | <1% | 1% |
| SC | Scott (R) | -14.4 | -4.0 | 100% | <1% | <1% |
| IN | Young (R) | -18.4 | -0.8 | 100% | <1% | <1% |
| LA | Kennedy (R) | -19.3 | -2.0 | 100% | <1% | <1% |
| UT | Lee (R) | -21.5 | -2.0 | 100% | <1% | <1% |
| AL | Britt (R) | -26.6 | -3.5 | 100% | 0 | 0 |
| AR | Boozman (R) | -28.1 | -1.8 | 100% | 0 | 0 |
| ID | Crapo (R) | -35.1 | +1.1 | 100% | 0 | 0 |
| KY | Paul (R) | -28.1 | +2.3 | 100% | 0 | <1% |
| ND | Hoeven (R) | -35.8 | -2.0 | 100% | 0 | 0 |
| OK | Lankford (R) | -31.9 | +1.0 | 100% | 0 | 0 |
| SD | Thune (R) | -28.5 | -5.9 | 100% | 0 | 0 |
| TN* | Blackburn appointee (R) | -25.8 | -1.0 | 100% | 0 | 0 |

## 2. Democratic-caucus seats in January 2029, by national environment

| Environment | Mean | 90% range | P(≥50) | P(≥51) | P(≥52) | P(≥55) | P(≥58) | P(≥60) | P(D president) | P(D control) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| R+3 | 52.4 | 49-56 | 94% | 83% | 65% | 14% | <1% | <1% | 2% | 83% |
| Neutral | 53.9 | 51-57 | 99% | 96% | 88% | 39% | 3% | <1% | 31% | 96% |
| D+3 | 55.4 | 52-58 | 100% | 99% | 97% | 70% | 14% | 1% | 84% | 99% |
| D+6 | 56.8 | 54-60 | 100% | 100% | 100% | 90% | 36% | 5% | 99% | 100% |
| 2026 repeat (D+13) | 59.9 | 57-63 | 100% | 100% | 100% | 100% | 92% | 59% | 100% | 100% |
| Evidence-weighted prior, D+3 with SD 4.5 | 55.3 | 50-60 | 98% | 95% | 90% | 63% | 23% | 6% | 66% | 95% |

## 3. By presidential winner (evidence-weighted prior)

| Winner | Share of runs | Mean seats | 90% range | P(≥50) | P(≥51) | P(≥55) | P(≥60) | P(D control) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Democratic president | 66% | 56.7 | 53-60 | 100% | 100% | 84% | 9% | 100% |
| Republican president | 34% | 52.7 | 49-56 | 93% | 85% | 22% | <1% | 85% |

## 4. Tipping-point seats (evidence-weighted prior)

The seat that delivers the 50th, 51st or 60th Democratic-caucus seat when the races are ranked by margin; share of runs in which each race is that seat.

| Race | 50th seat | 51st seat | 60th seat |
| --- | --- | --- | --- |
| NH | 13% | 18% | <1% |
| GA | 9% | 14% | <1% |
| NV | 6% | 10% | 1% |
| PA | 6% | 9% | 2% |
| AZ | 6% | 9% | 2% |
| NY | 12% | 7% | 0 |
| OR | 12% | 7% | <1% |
| CT | 11% | 6% | <1% |
| NC | 3% | 6% | 2% |
| WI | 3% | 5% | 3% |
| CO | 8% | 4% | 0 |
| IL | 8% | 4% | 0 |

The 60th seat, ranked: FL 15%, IA 15%, AK 15%, KS 10%, MO 10%, OH 7%, SC 7%, IN 5%.

## 5. Espen's priors as a scenario

Extra points toward Democrats: AZ +3.0, GA +2.5, NC +3.0, NV +5.5, WI +3.0.

| Environment | Model: mean seats | Priors: mean seats | Model P(hold AZ, GA and NV) | Priors P(hold all three) | Model P(win NC and WI) | Priors P(win both) |
| --- | --- | --- | --- | --- | --- | --- |
| Neutral | 53.9 | 54.9 | 30% | 56% | 19% | 38% |
| D+3 | 55.4 | 56.1 | 52% | 76% | 38% | 60% |

Per seat in a neutral year, model against priors: OH 21% against 21%; AZ 54% against 72%; GA 71% against 84%; NV 59% against 87%; NC 45% against 65%; WI 38% against 56%.


Democratic-held seats ranked by P(D) in a neutral year (model):

| Seat | P(D) neutral | P(D) D+3 |
| --- | --- | --- |
| OH | 21% | 38% |
| AZ | 54% | 71% |
| PA | 56% | 73% |
| NV | 59% | 76% |
| GA | 71% | 85% |
| NH | 84% | 93% |

## 6. Alaska: the Murkowski branches

Who wins the Alaska seat (Murkowski / the Democrat / Dunleavy or another Republican), and the share of runs in which the winner caucuses with Democrats, by branch and national environment.

| Branch | Voting system | Neutral: M / D / R; D caucus | D+3 | D+6 |
| --- | --- | --- | --- | --- |
| R | top four + RCV | 25% / 1% / 74%; 1% | 38% / 2% / 59%; 2% | 51% / 5% / 43%; 5% |
| R | repealed (closed primary, plurality) | 30% / 1% / 69%; 1% | 30% / 3% / 67%; 3% | 31% / 6% / 63%; 6% |
| I-D | top four + RCV | 19% / 0 / 81%; 19% | 34% / 0 / 66%; 34% | 51% / 0 / 49%; 51% |
| I-D | repealed (closed primary, plurality) | 19% / 0 / 81%; 19% | 34% / 0 / 66%; 34% | 51% / 0 / 49%; 51% |
| I-none | top four + RCV | 36% / 0 / 64%; 0 | 53% / 0 / 47%; 0 | 70% / 0 / 30%; 0 |
| I-none | repealed (closed primary, plurality) | 2% / 0 / 98%; 0 | 5% / 0 / 95%; 0 | 10% / 0 / 90%; 0 |
| retire | top four + RCV | 0 / 3% / 97%; 3% | 0 / 9% / 91%; 9% | 0 / 19% / 81%; 19% |
| retire | repealed (closed primary, plurality) | 0 / 3% / 97%; 3% | 0 / 9% / 91%; 9% | 0 / 19% / 81%; 19% |

Mixture weights (assumption): I-D 6%, I-none 8%, R 56%, retire 30%; P(repeal) 4%.

## 6b. The "wild map": Republican-held seats by environment

| Seat | Neutral | D+3 | D+6 | 2026 repeat (D+13) |
| --- | --- | --- | --- | --- |
| NC (Budd) | 45% | 65% | 81% | 98% |
| WI (Johnson) | 38% | 57% | 74% | 96% |
| IA (Grassley) | 5% | 12% | 24% | 66% |
| AK (Murkowski) | 3% | 6% | 11% | 31% |
| FL (Moody) | 2% | 6% | 15% | 56% |
| KS (Moran) | <1% | 1% | 5% | 30% |
| SC (Scott) | <1% | <1% | 2% | 18% |
| MO (Schmitt) | <1% | 1% | 4% | 27% |
| IN (Young) | <1% | <1% | 1% | 15% |
| UT (Lee) | <1% | <1% | <1% | 4% |
| LA (Kennedy) | <1% | <1% | <1% | 8% |

Expected Republican-held seats won: neutral 0.9; D+3 1.5; D+6 2.2; D+13 4.5.

## 7. Sensitivity (D+3, mean seats and P(≥55))

| Change | Mean seats | P(≥55) | P(≥60) | P(D control) |
| --- | --- | --- | --- | --- |
| Base | 55.4 | 69% | 1% | 100% |
| 2026 weight 0.15 | 55.3 | 66% | 1% | 100% |
| 2026 weight 0.45 | 55.5 | 71% | 1% | 100% |
| Incumbency 1.0 | 55.3 | 68% | 1% | 99% |
| Incumbency 3.5 | 55.5 | 70% | 1% | 100% |
| Carry-over 0.2 | 55.1 | 63% | 1% | 99% |
| Carry-over 0.6 | 55.7 | 74% | 1% | 100% |
| Race error 4 | 55.5 | 71% | 1% | 100% |
| Race error 6 | 55.4 | 68% | 1% | 100% |
| Regional error 1.5 | 55.4 | 71% | 1% | 100% |
| Regional error 3.5 | 55.4 | 68% | 1% | 99% |
| AK and MS 2026 both R | 53.8 | 36% | 0 | 97% |
| AK and MS 2026 both D | 55.8 | 76% | 1% | 100% |
| MN 2027 special lost | 54.5 | 52% | <1% | 99% |
| Electoral College bias 0 | 55.4 | 69% | 1% | 100% |
| Electoral College bias 3 | 55.4 | 69% | 1% | 99% |
| Governor incumbency 5, weight 1.0 | 55.4 | 68% | 1% | 99% |

## 8. Control through 2033: the 2030 and 2032 classes

**Evidence-weighted prior, Democratic president elected in 2028** (13136 runs)

| After the election of | Seated | Mean D seats | P(≥50) | P(≥51) | P(≥55) | P(60+) |
| --- | --- | --- | --- | --- | --- | --- |
| 2028 | January 2029 | 56.7 | 100% | 100% | 85% | 9% |
| 2030 | January 2031 | 54.1 | 82% | 75% | 48% | 15% |
| 2032 | January 2033 | 48.9 | 47% | 41% | 22% | 7% |

Held in every Congress from January 2029 (50+ / 55+ / 60+): the 2029-30 Congress 100% / 85% / 9%; through the 2031-32 Congress 82% / 46% / 6%; through the 2033-34 Congress 46% / 21% / 3%.

**D1 stipulation: Democratic president 2029-2037** (9477 runs)

| After the election of | Seated | Mean D seats | P(≥50) | P(≥51) | P(≥55) | P(60+) |
| --- | --- | --- | --- | --- | --- | --- |
| 2028 | January 2029 | 57.0 | 100% | 100% | 87% | 12% |
| 2030 | January 2031 | 54.8 | 84% | 79% | 53% | 19% |
| 2032 | January 2033 | 51.2 | 60% | 54% | 30% | 9% |

Held in every Congress from January 2029 (50+ / 55+ / 60+): the 2029-30 Congress 100% / 87% / 12%; through the 2031-32 Congress 84% / 51% / 8%; through the 2033-34 Congress 60% / 29% / 5%.

**Near-neutral 2028 (SD 2), Democratic president** (7166 runs)

| After the election of | Seated | Mean D seats | P(≥50) | P(≥51) | P(≥55) | P(60+) |
| --- | --- | --- | --- | --- | --- | --- |
| 2028 | January 2029 | 55.4 | 100% | 100% | 69% | 1% |
| 2030 | January 2031 | 51.4 | 67% | 59% | 26% | 3% |
| 2032 | January 2033 | 44.8 | 21% | 17% | 5% | <1% |

Held in every Congress from January 2029 (50+ / 55+ / 60+): the 2029-30 Congress 100% / 69% / 1%; through the 2031-32 Congress 67% / 23% / <1%; through the 2033-34 Congress 21% / 4% / <1%.

Midterm swing against the president's party (1990-2026): mean 7.2, SD 6.9 points. Presidential-year drift SD 5.7.


## 9. Round 4: Minnesota's 2027 special

Minnesota lean +2.5 (2020 D+7.1, 2024 D+4.2, 2026 Senate D+10.1 open). P(Democrats hold) by the 2027 national environment, with an appointee running as a weak incumbent (+1):

| 2027 environment | R+3 | Even | D+3 | D+8 | D+13 |
| --- | --- | --- | --- | --- | --- |
| P(D) | 53% | 71% | 84% | 96% | 99% |

What losing it does to January 2029 (mean seats, P(≥55), P(D control)):

| Environment | Minnesota held | Minnesota lost |
| --- | --- | --- |
| Neutral | 54.0; 40%; 96% | 53.0; 23%; 90% |
| D+3 | 55.5; 71%; 100% | 54.5; 52%; 98% |
| D+6 | 56.9; 91%; 100% | 55.9; 80%; 100% |
| Evidence-weighted prior, D+3 with SD 4.5 | 55.4; 64%; 95% | 54.4; 51%; 91% |

## 10. Round 4: the D2-F whip count against the Senate

Opponents drawn per run from the whip table in the script (assumptions anchored on public statements); D2-F passes if Democratic seats minus opponents reach 50 with a Democratic Vice President (51 without).

| Environment | Mean seats | Mean opponents | Mean margin before defections | P(5+ opponents) | P(D2-F has the votes) |
| --- | --- | --- | --- | --- | --- |
| Neutral, Democratic president | 55.1 | 6.0 | 5.1 | 77% | 44% |
| D+3, Democratic president | 55.7 | 6.2 | 5.7 | 79% | 51% |
| D+6, Democratic president | 56.8 | 6.4 | 6.8 | 82% | 65% |
| Evidence-weighted prior, D+3 with SD 4.5, Democratic president | 56.6 | 6.4 | 6.6 | 81% | 62% |

Sensitivity (evidence-weighted, Democratic president): unnamed senators' probabilities halved, P(votes) 89% (mean opponents 4.2); doubled, 9% (10.8). Fetterman, Hamilton and Cooper are held at their stated positions.


## 11. Round 4: what drives the 2032 drop, and what would change it

Evidence-weighted prior, Democratic president elected in 2028. Each Democratic-held Class 2 seat: P(held in 2032), and its share of all Democratic 2032 losses.

| Seat | P(held) | Share of losses | Expected loss |
| --- | --- | --- | --- |
| MS | 10% | 15% | 0.79 |
| SC | 27% | 13% | 0.73 |
| KS | 32% | 13% | 0.68 |
| IA | 37% | 12% | 0.63 |
| AK | 28% | 10% | 0.56 |
| TX | 57% | 8% | 0.43 |
| MI | 61% | 7% | 0.39 |
| ME | 76% | 4% | 0.24 |
| MN | 77% | 4% | 0.23 |
| NH | 78% | 4% | 0.22 |

Levers (same runs; held 50+ means in every Congress through 2033-34). With statehood the chamber has 102 or 104 seats, so the thresholds are chamber-adjusted: "50+" means control with a Democratic Vice President (51 of 102, 52 of 104) and "55+" shifts the same way; mean seats are raw.

| Lever | Mean seats Jan 2031 | Mean seats Jan 2033 | P(control-equivalent 50+) Jan 2033 | Held 50+ through 2033-34 | Held 55+ through 2033-34 |
| --- | --- | --- | --- | --- | --- |
| Base | 54.1 | 48.9 | 47% | 46% | 21% |
| Mild 2030 midterm (half the usual penalty) | 55.9 | 50.7 | 56% | 56% | 28% |
| Every 2026 winner runs again (no Class 2 retirements) | 54.1 | 49.0 | 48% | 47% | 22% |
| Retention: 2026 winners keep 60% of their overperformance | 54.1 | 48.9 | 46% | 46% | 21% |
| Candidate and campaign strength: +2 points in the six most exposed seats | 54.1 | 49.4 | 49% | 49% | 23% |
| D.C. statehood, seated January 2031 | 56.1 | 50.9 | 52% | 52% | 25% |
| D.C. and Puerto Rico, seated January 2031 | 57.3 | 52.1 | 53% | 53% | 26% |
| D.C. and Puerto Rico, seated January 2033 | 54.1 | 52.1 | 53% | 52% | 26% |
| D.C. and Puerto Rico 2031, a mild midterm and +2 in the exposed seats | 59.1 | 54.3 | 65% | 65% | 37% |
