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
| CO | Bennet (D) | +11.6 | +3.8 | 100% | 100% | 100% |
| IL | Duckworth (D) | +11.7 | +3.4 | 100% | 99% | 100% |
| CT | Blumenthal (D) | +12.1 | +1.9 | 100% | 99% | 100% |
| OR | Wyden (D) | +10.5 | +2.7 | 100% | 99% | 100% |
| NY | Schumer (D) | +11.9 | +1.3 | 100% | 99% | 100% |
| NH | Hassan (D) | +1.4 | +4.5 | 100% | 84% | 93% |
| GA | Warnock (D) | -1.0 | +4.3 | 100% | 71% | 85% |
| NV | Cortez Masto (D) | -1.9 | +3.3 | 100% | 60% | 77% |
| PA | Fetterman (D) | +1.1 | +0.0 | 100% | 56% | 73% |
| AZ | Kelly (D) | -3.7 | +5.8 | 75% | 56% | 72% |
| NC | Budd (R) | -0.0 | -0.7 | 100% | 45% | 65% |
| WI | Johnson (R) | -1.9 | +0.1 | 25% | 39% | 57% |
| OH | Brown (D) | -9.1 | +4.2 | 100% | 21% | 38% |
| IA | Grassley (R) | -10.3 | -0.2 | 35% | 5% | 12% |
| AK | Murkowski (R) | -11.9 | branch model | 100% | 3% | 6% |
| FL | Moody (R) | -11.6 | -0.6 | 100% | 2% | 6% |
| KS | Moran (R) | -13.5 | -2.6 | 100% | <1% | 1% |
| MO | Schmitt (R) | -17.8 | +1.1 | 100% | <1% | 1% |
| SC | Scott (R) | -14.4 | -4.0 | 100% | <1% | <1% |
| IN | Young (R) | -18.4 | -0.8 | 100% | <1% | <1% |
| LA | Kennedy (R) | -19.3 | -2.0 | 100% | <1% | <1% |
| AL | Britt (R) | -26.6 | -3.5 | 100% | 0 | 0 |
| AR | Boozman (R) | -28.1 | -1.8 | 100% | 0 | 0 |
| ID | Crapo (R) | -35.1 | +1.1 | 100% | 0 | 0 |
| KY | Paul (R) | -28.1 | +2.3 | 100% | 0 | <1% |
| ND | Hoeven (R) | -35.8 | -2.0 | 100% | 0 | 0 |
| OK | Lankford (R) | -31.9 | +1.0 | 100% | 0 | 0 |
| SD | Thune (R) | -28.5 | -5.9 | 100% | 0 | 0 |
| TN* | Blackburn appointee (R) | -25.8 | -1.0 | 100% | 0 | 0 |
| UT | Lee (R) | -21.5 | -2.0 | 100% | 0 | <1% |

## 2. Democratic-caucus seats in January 2029, by national environment

| Environment | Mean | 90% range | P(≥50) | P(≥51) | P(≥52) | P(≥55) | P(≥58) | P(≥60) | P(D president) | P(D control) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| R+3 | 52.4 | 49-56 | 94% | 83% | 66% | 15% | <1% | <1% | 2% | 83% |
| Neutral | 53.9 | 51-57 | 99% | 96% | 88% | 39% | 3% | <1% | 31% | 96% |
| D+3 | 55.4 | 52-58 | 100% | 99% | 98% | 70% | 14% | 1% | 84% | 100% |
| D+6 | 56.8 | 54-60 | 100% | 100% | 100% | 90% | 36% | 5% | 99% | 100% |
| 2026 repeat (D+13) | 59.9 | 57-63 | 100% | 100% | 100% | 100% | 92% | 59% | 100% | 100% |
| Evidence-weighted prior, D+3 with SD 4.5 | 55.3 | 50-60 | 98% | 95% | 90% | 63% | 23% | 6% | 66% | 95% |

## 3. By presidential winner (evidence-weighted prior)

| Winner | Share of runs | Mean seats | 90% range | P(≥50) | P(≥51) | P(≥55) | P(≥60) | P(D control) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Democratic president | 66% | 56.6 | 53-60 | 100% | 100% | 84% | 9% | 100% |
| Republican president | 34% | 52.8 | 49-56 | 93% | 85% | 22% | <1% | 85% |

## 4. Tipping-point seats (evidence-weighted prior)

The seat that delivers the 50th, 51st or 60th Democratic-caucus seat when the races are ranked by margin; share of runs in which each race is that seat.

| Race | 50th seat | 51st seat | 60th seat |
| --- | --- | --- | --- |
| NH | 14% | 17% | <1% |
| GA | 9% | 14% | <1% |
| NV | 6% | 9% | 1% |
| PA | 6% | 9% | 2% |
| AZ | 5% | 9% | 2% |
| NY | 12% | 7% | 0 |
| OR | 12% | 7% | 0 |
| NC | 3% | 6% | 2% |
| CT | 11% | 6% | <1% |
| WI | 3% | 5% | 3% |
| IL | 8% | 4% | 0 |
| CO | 7% | 4% | 0 |

The 60th seat, ranked: FL 15%, IA 15%, AK 14%, KS 11%, MO 10%, SC 7%, OH 7%, IN 6%.

## 5. Espen's priors as a scenario

Extra points toward Democrats: AZ +3.0, GA +2.5, NC +3.0, NV +5.5, WI +3.0.

| Environment | Model: mean seats | Priors: mean seats | Model P(hold AZ, GA and NV) | Priors P(hold all three) | Model P(win NC and WI) | Priors P(win both) |
| --- | --- | --- | --- | --- | --- | --- |
| Neutral | 53.9 | 54.9 | 30% | 56% | 19% | 38% |
| D+3 | 55.4 | 56.1 | 52% | 76% | 38% | 60% |

Per seat in a neutral year, model against priors: OH 21% against 21%; AZ 56% against 71%; GA 71% against 84%; NV 60% against 87%; NC 45% against 64%; WI 39% against 57%.


Democratic-held seats ranked by P(D) in a neutral year (model):

| Seat | P(D) neutral | P(D) D+3 |
| --- | --- | --- |
| OH | 21% | 38% |
| AZ | 56% | 72% |
| PA | 56% | 73% |
| NV | 60% | 77% |
| GA | 71% | 85% |
| NH | 84% | 93% |

## 6. Alaska: the Murkowski branches

Who wins the Alaska seat (Murkowski / the Democrat / Dunleavy or another Republican), and the share of runs in which the winner caucuses with Democrats, by branch and national environment.

| Branch | Voting system | Neutral: M / D / R; D caucus | D+3 | D+6 |
| --- | --- | --- | --- | --- |
| R | top four + RCV | 25% / 1% / 74%; 1% | 38% / 2% / 59%; 2% | 51% / 5% / 43%; 5% |
| R | repealed (closed primary, plurality) | <1% / 1% / 99%; 1% | <1% / 3% / 97%; 3% | 1% / 6% / 93%; 6% |
| I-D | top four + RCV | 19% / 0 / 81%; 19% | 34% / 0 / 66%; 34% | 51% / 0 / 49%; 51% |
| I-D | repealed (closed primary, plurality) | 19% / 0 / 81%; 19% | 34% / 0 / 66%; 34% | 51% / 0 / 49%; 51% |
| I-none | top four + RCV | 36% / 0 / 64%; 0 | 53% / 0 / 47%; 0 | 70% / 0 / 30%; 0 |
| I-none | repealed (closed primary, plurality) | 2% / 0 / 98%; 0 | 5% / 0 / 95%; 0 | 10% / 0 / 90%; 0 |
| retire | top four + RCV | 0 / 3% / 97%; 3% | 0 / 9% / 91%; 9% | 0 / 19% / 81%; 19% |
| retire | repealed (closed primary, plurality) | 0 / 3% / 97%; 3% | 0 / 9% / 91%; 9% | 0 / 19% / 81%; 19% |

Mixture weights (assumption): I-D 6%, I-none 8%, R 56%, retire 30%; P(repeal) 15%.

## 6b. The "wild map": Republican-held seats by environment

| Seat | Neutral | D+3 | D+6 | 2026 repeat (D+13) |
| --- | --- | --- | --- | --- |
| NC (Budd) | 45% | 65% | 81% | 98% |
| WI (Johnson) | 39% | 57% | 74% | 96% |
| IA (Grassley) | 5% | 12% | 25% | 66% |
| AK (Murkowski) | 3% | 6% | 12% | 31% |
| FL (Moody) | 2% | 6% | 16% | 56% |
| KS (Moran) | <1% | 1% | 4% | 30% |
| SC (Scott) | <1% | <1% | 2% | 18% |
| MO (Schmitt) | <1% | 1% | 4% | 28% |
| IN (Young) | <1% | <1% | 1% | 15% |
| UT (Lee) | 0 | <1% | <1% | 4% |
| LA (Kennedy) | <1% | <1% | 1% | 9% |

Expected Republican-held seats won: neutral 0.9; D+3 1.5; D+6 2.2; D+13 4.5.

## 7. Sensitivity (D+3, mean seats and P(≥55))

| Change | Mean seats | P(≥55) | P(≥60) | P(D control) |
| --- | --- | --- | --- | --- |
| Base | 55.4 | 69% | 1% | 100% |
| 2026 weight 0.15 | 55.3 | 67% | <1% | 100% |
| 2026 weight 0.45 | 55.5 | 71% | 1% | 100% |
| Incumbency 1.0 | 55.3 | 68% | 1% | 99% |
| Incumbency 3.5 | 55.5 | 70% | 1% | 100% |
| Carry-over 0.2 | 55.1 | 62% | <1% | 99% |
| Carry-over 0.6 | 55.7 | 74% | 1% | 100% |
| Race error 4 | 55.5 | 72% | <1% | 100% |
| Race error 6 | 55.4 | 68% | 1% | 100% |
| Regional error 1.5 | 55.4 | 71% | <1% | 100% |
| Regional error 3.5 | 55.4 | 68% | 1% | 99% |
| AK and MS 2026 both R | 53.7 | 36% | <1% | 97% |
| AK and MS 2026 both D | 55.7 | 76% | 1% | 100% |
| MN 2027 special lost | 54.5 | 52% | <1% | 98% |
| Electoral College bias 0 | 55.4 | 69% | 1% | 100% |
| Electoral College bias 3 | 55.4 | 69% | 1% | 99% |
| Governor incumbency 5, weight 1.0 | 55.4 | 68% | 1% | 100% |

## 8. Control through 2033: the 2030 and 2032 classes

**Evidence-weighted prior, Democratic president elected in 2028** (13150 runs)

| After the election of | Seated | Mean D seats | P(≥50) | P(≥51) | P(≥55) | P(60+) |
| --- | --- | --- | --- | --- | --- | --- |
| 2028 | January 2029 | 56.7 | 100% | 100% | 84% | 9% |
| 2030 | January 2031 | 54.2 | 82% | 76% | 48% | 16% |
| 2032 | January 2033 | 49.0 | 47% | 42% | 23% | 7% |

Held in every Congress from January 2029 (50+ / 55+ / 60+): the 2029-30 Congress 100% / 84% / 9%; through the 2031-32 Congress 82% / 46% / 6%; through the 2033-34 Congress 47% / 22% / 4%.

**D1 stipulation: Democratic president 2029-2037** (9446 runs)

| After the election of | Seated | Mean D seats | P(≥50) | P(≥51) | P(≥55) | P(60+) |
| --- | --- | --- | --- | --- | --- | --- |
| 2028 | January 2029 | 57.0 | 100% | 100% | 88% | 12% |
| 2030 | January 2031 | 54.9 | 85% | 80% | 53% | 19% |
| 2032 | January 2033 | 51.3 | 61% | 54% | 30% | 10% |

Held in every Congress from January 2029 (50+ / 55+ / 60+): the 2029-30 Congress 100% / 88% / 12%; through the 2031-32 Congress 85% / 52% / 8%; through the 2033-34 Congress 60% / 29% / 5%.

**Near-neutral 2028 (SD 2), Democratic president** (7255 runs)

| After the election of | Seated | Mean D seats | P(≥50) | P(≥51) | P(≥55) | P(60+) |
| --- | --- | --- | --- | --- | --- | --- |
| 2028 | January 2029 | 55.4 | 100% | 100% | 70% | 1% |
| 2030 | January 2031 | 51.5 | 67% | 59% | 26% | 3% |
| 2032 | January 2033 | 44.8 | 22% | 17% | 5% | <1% |

Held in every Congress from January 2029 (50+ / 55+ / 60+): the 2029-30 Congress 100% / 70% / 1%; through the 2031-32 Congress 67% / 24% / <1%; through the 2033-34 Congress 22% / 5% / <1%.

Midterm swing against the president's party (1990-2026): mean 7.2, SD 6.9 points. Presidential-year drift SD 5.7.

