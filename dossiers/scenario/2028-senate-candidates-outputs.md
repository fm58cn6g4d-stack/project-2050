# 2028 Senate candidate-quality sensitivity (n = 20000 per row, seeded)

A shift of 2 points toward the Democrat (+) or the Republican (-) in one race at a time, with
everything else as in `senate_model.py`. Alaska runs through the model's branch logic, so its
shift applies to the underlying margin. 55+ = Democratic-caucus seats; "seats per point" is the change
in expected seats per point of shift. The last row shifts every listed race but Kansas together.

## Environment: neutral (base: control 96%, 55+ seats 39%, mean 53.9 seats)

| Race | P(D) at -2 / base / +2 | Race odds per point | P(55+) at -2 / +2 | P(55+) per point | Seats per point |
| --- | --- | --- | --- | --- | --- |
| NC | 32% / 45% / 58% | +6.5 pts | 36% / 42% | +1.5 pts | +0.07 |
| WI | 27% / 38% / 50% | +5.8 pts | 36% / 41% | +1.3 pts | +0.06 |
| NV | 46% / 59% / 71% | +6.3 pts | 36% / 41% | +1.2 pts | +0.06 |
| PA | 44% / 56% / 68% | +6.0 pts | 36% / 41% | +1.2 pts | +0.06 |
| AZ | 43% / 54% / 66% | +5.9 pts | 36% / 41% | +1.2 pts | +0.06 |
| OH | 13% / 21% / 32% | +4.8 pts | 37% / 41% | +1.0 pts | +0.05 |
| GA | 59% / 71% / 81% | +5.5 pts | 37% / 40% | +0.9 pts | +0.06 |
| NH | 74% / 84% / 90% | +4.1 pts | 37% / 40% | +0.6 pts | +0.04 |
| IA | 2% / 5% / 9% | +1.6 pts | 38% / 40% | +0.3 pts | +0.02 |
| FL | 1% / 2% / 5% | +0.9 pts | 39% / 39% | +0.2 pts | +0.01 |
| AK | 2% / 3% / 5% | +0.8 pts | 39% / 39% | +0.2 pts | +0.01 |
| KS | <1% / <1% / 1% | +0.2 pts | 39% / 39% | +0.0 pts | +0.00 |
| **All but KS at once** | - | - | 21% / 59% | +9.3 pts | +0.48 |

## Environment: D+3 (base: control 99%, 55+ seats 70%, mean 55.4 seats)

| Race | P(D) at -2 / base / +2 | Race odds per point | P(55+) at -2 / +2 | P(55+) per point | Seats per point |
| --- | --- | --- | --- | --- | --- |
| NC | 52% / 65% / 76% | +6.0 pts | 66% / 72% | +1.3 pts | +0.06 |
| WI | 44% / 57% / 69% | +6.2 pts | 67% / 72% | +1.2 pts | +0.06 |
| NV | 65% / 76% / 85% | +5.0 pts | 67% / 72% | +1.1 pts | +0.05 |
| OH | 26% / 38% / 52% | +6.3 pts | 67% / 72% | +1.1 pts | +0.06 |
| AZ | 61% / 71% / 80% | +4.9 pts | 67% / 71% | +1.1 pts | +0.05 |
| PA | 62% / 73% / 82% | +4.9 pts | 67% / 71% | +1.1 pts | +0.05 |
| GA | 76% / 85% / 91% | +3.8 pts | 67% / 71% | +0.8 pts | +0.04 |
| NH | 87% / 93% / 97% | +2.3 pts | 68% / 70% | +0.5 pts | +0.02 |
| IA | 7% / 12% / 20% | +3.2 pts | 69% / 70% | +0.4 pts | +0.03 |
| FL | 3% / 6% / 12% | +2.1 pts | 69% / 70% | +0.2 pts | +0.02 |
| AK | 4% / 6% / 9% | +1.4 pts | 69% / 70% | +0.2 pts | +0.01 |
| KS | 1% / 1% / 3% | +0.7 pts | 69% / 70% | +0.1 pts | +0.01 |
| **All but KS at once** | - | - | 49% / 84% | +8.8 pts | +0.46 |

