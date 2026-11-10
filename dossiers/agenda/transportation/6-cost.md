# Transportation: cost and financing

Role: section 6 of the transportation dossier. It prices the provisions of section 4 on the transportation model and the federal budget model, and reports the fiscal-rule effect to the financing settlement (`charter/STANDARDS.md`, "Fiscal rule in dossiers: report, don't gate"). Status: draft (stage C, step 7, PR 3), on the decisions in `DEC-2026-11-10-08`. Those decisions change no dollar figure, so the figures below are the legacy design's, rerun.

## Counting rules

- **Conventions.** The project's budget conventions (`models/tools/budget/CONVENTIONS.md`): nominal dollars by fiscal year, deficit effects positive for a cost, the common window FY2030-39 (`ASM-WINDOW`).
- **Increment.** The ledger counts what the plan adds above CBO's baseline (`ASM-INCREMENT`). For transportation that means:
  - the general-fund lines: the 2029 and 2030 packages, the renewal top-ups and the 2031 bill's expansion appropriations;
  - the new dedicated revenue, credited to the trust fund net of the standard 25% income and payroll tax offset (MR6, a scoring convention).
- **Two models.**
  - The transportation model (`models/tools/transportation/moving_america.py`) computes programs, receipts by source and the general-fund draw year by year. It has no demand response, so revenue from the steps and the premium is an upper bound [EV-MOV-206].
  - The budget model (`models/tools/budget/provisions.py`) books the ledger amounts on profiles (`models/data/inputs/fiscal-profiles.csv`).

## 1. What each law costs and raises

From the ledger (built from the transportation model by `models/tools/ledger-build.py`; `legacy/index/2029-trifecta-master-ledger.md`):

| Law | General-fund spending | New dedicated revenue (net of the offset) | Net | Window |
| --- | --- | --- | --- | --- |
| 2028 extension (MOV-28, 2027-28 exception) | A transfer keeping both accounts solvent through FY2031, **not yet sized** | Extends current rates; no new rates | — | FY2029-31 |
| 2029 act (MOV-29, R1) | $47.0B package one + $209.74B renewal top-ups for FY2032-35 | $290.0B ($386.7B gross): fuel taxes indexed with steps, the clean-vehicle charge, truck excises | About $33.3B deficit reduction | FY2029-38 |
| 2030 act (MOV-30, R3) | $33.5B package two + $57.33B top-ups for FY2035-36 | $95.0B ($126.7B gross): weight-distance charge, rail diesel, aviation surcharge | About $4.2B deficit reduction | FY2030-39, to be rescored on FY2031-40 if carried on the FY2031 resolution |
| Moving America Act of 2031 (MOV-31) | $123.70B expansion and about $1B for division E | Restates the 2029-30 revenue | Cost | FY2032-36 |

Over FY2032-36 the 2031 bill authorizes $936.57B. Dedicated receipts cover $545.84B and the general fund $390.73B, or 0.180% of GDP a year [EV-MOV-200].

**Commitment, assumption or open question.**
- **Commitments** (decided): the program levels, the rates and the vehicles.
- **Working assumptions:**
  - the 25% offset (CBO's convention);
  - 2.5% inflation and 4.1% nominal GDP growth in the transportation model;
  - no demand response (an upper bound on receipts).
- **Open:** the size of the 2028 extension's transfer. It depends on the baseline case (`3-design.md`) and is sized when the 2028 law is drafted.

## 2. The general-fund draw by year

On the transportation model's own path. These are the plan's figures (grade D, project estimate). The draw is the general fund's share of the whole surface program, not the increment over CBO's baseline:

| FY | Program ($B) | Dedicated receipts ($B) | General fund ($B) | % of GDP |
| --- | --- | --- | --- | --- |
| 2029 | 119.0 | 50.0 | 69.0 | 0.194% |
| 2030 | 141.6 | 58.6 | 83.1 | 0.225% |
| 2032 | 164.2 | 84.3 | 79.9 | 0.200% |
| 2036 | 207.5 | 135.6 | 71.9 | 0.153% |
| 2037 | 196.1 | 147.0 | 49.1 | 0.100% |
| 2040 | 209.7 | 180.7 | 29.0 | 0.053% |
| 2044 | 234.8 | 220.8 | 14.0 | 0.022% |
| 2046 | 245.3 | 231.7 | 13.6 | 0.019% |

Source: `Model().allocate(t)` in `moving_america.py`, run on November 10, 2026. The period averages match `golden/report.txt`: 0.180% in FY2032-36, 0.067% in FY2037-41, 0.026% in FY2042-46.

By FY2042-46, users cover 95% of highway renewal and all of transit's and rail's [EV-MOV-200] [EV-MOV-206].

## 3. The fiscal-rule report

Under `DEC-2026-11-10-05`, the dossier reports its fiscal-rule effect and passes it to the settlement.

| Measure | As the budget model books it | On the transportation model's path |
| --- | --- | --- |
| FY2030-39, general-fund lines (MOV-29, -30, -31) | **$473.0 billion** (0.257 + 0.091 + 0.125 trillion), outlays spread over the window | The same lines, timed as obligated: packages in FY2029-31, top-ups and expansion in FY2032-36 |
| FY2030-39, new dedicated revenue | About $0.39 trillion (the surface trust fund channel, net of the offset) | $290.0B + $95.0B over each act's window |
| Permanent cost in FY2040 | **$22.1 billion**: a 30% tail on the reconciliation lines plus a successor authorization at 30% of MOV-31's run rate (`fiscal-profiles.csv`) | **$29.0 billion** (0.053% of GDP), the whole general-fund draw that year, falling to $14.0 billion by FY2044 as the premium phases in |
| Share of the plan-wide margin | Already inside the plan-wide totals the housing close-out reported (FY2040 short of balance by $50.8 billion; `dossiers/home/6-cost.md`) | Up to about $7 billion more in FY2040 than booked, if the successor's draw follows the model |

**Reading the difference.** The two columns differ for three reasons:
- **Timing.** The budget model spreads each act's ten-year amount evenly. The real money is packages in FY2029-31 and top-ups in FY2032-36.
- **Successor.** The budget model's successor authorization is a placeholder at 30% of the run rate.
- **Basis.** The transportation model's draw is the whole general-fund share, not the increment over CBO's baseline.

The range for FY2040, $22 to $29 billion (about 0.04% to 0.05% of GDP), is reported to the settlement as a working assumption. No transportation choice turns on where in the range it falls.

**Booking.** PR #192's booking shapes (an end year and a fade after 2039) can express the model's path:
- the reconciliation lines closed at their expenditure deadlines (time-limited, under the ledger's C30 resolution);
- the successor fading as the premium arrives.

Rebooking changes adopted inputs (`models/data/inputs/`), a tier-3 decision. It belongs with the budget model's integration step that puts each bill in its own CBO window (board, B6 item 4), not in this dossier. It is listed under "Open questions" below for the budget model's owner.

## 4. Sensitivities (the plan's model)

Each line changes one choice, holding the rest; the average draw is for FY2032-36 (`golden/report.txt`, SENS) [EV-MOV-203] [EV-MOV-206] [EV-MOV-207] [EV-MOV-210]:

| Case | Average draw FY2032-36 | Draw FY2042-46 | General fund FY2032-36 ($B) |
| --- | --- | --- | --- |
| As decided | 0.180% | 0.026% | 390.7 |
| Three price pauses | 0.204% | 0.026% | 444.0 |
| Weight-distance at 2 cents | 0.185% | 0.032% | 402.7 |
| 2-cent fuel steps | 0.209% | 0.076% | 454.1 |
| Indexing only | 0.267% | 0.174% | 580.9 |
| Transit operating help at $70B | 0.196% | 0.043% | 425.7 |
| No transit operating help | 0.164% | 0.010% | 356.7 |
| No fossil premium | 0.180% | 0.065% | 390.7 |

The largest risk to the cost is revenue, not spending. Price pauses delay receipts, which the capped $25B backstop covers [EV-MOV-219], and the model's lack of a demand response overstates the steps' and the premium's yield.

## 5. Fit with the fairness test (D3)

Fuel taxes are a larger share of lower-income households' budgets, and transportation is the second-largest household expense [EV-MOV-013]. Section 7 reports the household cost by income. Whether the plan as a whole leaves lower- and middle-income households ahead is decided plan-wide in the financing settlement.

## Open questions

None for Espen; each is a question about money that stays with the settlement or the budget model:
1. **The 2028 extension's transfer** is not sized. It is sized when the extension is drafted, on the baseline case then known.
2. **FY2040 booking** ($22.1 billion booked; $29.0 billion on the model's path). For the budget model owner, with B6 item 4; a tier-3 inputs change if adopted.
3. **The 2030 act's window.** Rescore on FY2031-40 if it rides the FY2031 resolution (R3), as the ledger notes.
