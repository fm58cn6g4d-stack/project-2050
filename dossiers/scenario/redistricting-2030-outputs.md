# Redistricting model outputs (generated)

Role: the tables `tools/redistricting_2030.py --write` produces, read by `redistricting-2030-model.md`. Status: generated; do not edit by hand. This project's exploratory scenario arithmetic, not a forecast. Runs come from `senate_model.simulate_chain` (evidence-weighted 2028 environment, D+3 with SD 4.5), n = 20000, seeded.

## 1. Who holds the 2031 pens

Share of runs in which each state's 2031 congressional map is Democratic-drawn / neutral (court, commission, deadlock) / Republican-drawn. Average 2030 environment: R+1.5 with a Democratic president, D+4.9 with a Republican president.

| State | Seats | Swing (D map − R map) | Democratic president: D / N / R | Republican president: D / N / R |
| --- | --- | --- | --- | --- |
| TX | 42 | 10.0 | 1% / 27% / 71% | 6% / 50% / 44% |
| FL | 31 | 6.5 | <1% / 7% / 93% | 2% / 20% / 78% |
| NC | 15 | 5.5 | 4% / 9% / 87% | 13% / 22% / 66% |
| PA | 16 | 5.0 | 10% / 56% / 34% | 28% / 59% / 13% |
| GA | 14 | 4.5 | 2% / 50% / 48% | 9% / 66% / 25% |
| OH | 15 | 5.0 | 2% / 21% / 77% | 7% / 40% / 54% |
| WI | 8 | 2.5 | 16% / 41% / 43% | 39% / 42% / 19% |
| NV | 4 | 1.5 | 40% / 29% / 31% | 67% / 22% / 11% |
| MI | 13 | 0.0 | 0 / 100% / 0 | 0 / 100% / 0 |
| AZ | 10 | 0.0 | 0 / 100% / 0 | 0 / 100% / 0 |
| VA | 11 | 3.0 | 25% / 75% / 0 | 25% / 75% / 0 |
| NY | 24 | 6.0 | 45% / 55% / 0 | 46% / 54% / 0 |

## 2. The 2032 House maps, with and without DEM-2 Titles I-II

| 2028 president | Net partisan map effect, 12 states (D seats) | Net, all states | Expected D House seats 2032, no DEM-2 | With Titles I-II | Value of Titles I-II (10th-90th percentile) | P(D House 2033), no DEM-2 | With |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Democratic | -10.9 | -14.8 | 214 | 223 | +9.7 (+2.7 to +15.1) | 42% | 57% |
| Republican | -4.6 | -8.6 | 191 | 196 | +5.6 (-3.1 to +13.1) | 15% | 19% |

Average 2032 environment: D+4.9 (Democratic president elected 2028), R+3.1 (Republican). Title I (the mid-decade ban) does not change the decennial 2031 maps, so the 2032 value is Title II's; Title I's value is in section 4.

## 3. Sensitivity (Democratic president)

| Change | Value of Titles I-II, D seats 2032 | P(D House 2033): without / with |
| --- | --- | --- |
| Base (f = 0.65) | +9.5 | 44% / 58% |
| Title II removes 40% | +5.9 | 44% / 52% |
| Title II removes 85% | +12.5 | 44% / 63% |
| Rest-of-country net effect 0 | +6.9 | 49% / 60% |
| Rest-of-country net effect -8 | +12.1 | 38% / 56% |
| Partisan-fairness standard also cuts geographic bias by a quarter | +11.3 | 44% / 61% |
| 2028 environment neutral (SD 2) | +11.1 | 24% / 40% |

## 4. Title I, the mid-decade ban

Title I matters after the 2031 maps: it stops a party that gains a trifecta in 2032-36 from redrawing again before 2041, as in 2025-26. Illustration (ASSUMPTION): without the ban, a mid-decade round happens in a given cycle with probability 0.5, moving each redrawing state by a quarter of its swing toward the party in power. The 2025-26 round moved little net (most Republican redraws were offset or backfired, per #86), so its expected seat value is near zero and its main effect is on variance:

Mid-decade move without Title I: mean +0.0 seats, 10th-90th percentile -2.4 to +2.5; with Title I: 0.

