# Transportation: cost and financing

Role: section 6 of the transportation dossier. It prices the provisions of section 4 on the transportation model and the federal budget model, and reports the fiscal-rule effect to the financing settlement (`charter/STANDARDS.md`, "Fiscal rule in dossiers: report, don't gate"). Status: draft (stage C, step 7, PR 3), on the decisions in `DEC-2026-11-10-08`. Those decisions change no dollar figure, so the figures below are the legacy design's, rerun.

## Counting rules

- **Conventions.** The project's budget conventions (`models/tools/budget/CONVENTIONS.md`): nominal dollars by fiscal year, deficit effects positive for a cost, the common window FY2030-39 (`ASM-WINDOW`).
- **Increment.** The ledger counts what the plan adds above CBO's baseline (`ASM-INCREMENT`). For transportation that means:
  - the general-fund lines: the 2029 and 2030 packages, the renewal top-ups and the 2031 bill's expansion appropriations;
  - the new dedicated revenue, credited to the trust fund net of the standard 25% income and payroll tax offset (MR6, a scoring convention). The offset itself falls on the general fund and is not yet booked (section 3).
- **Two models.**
  - The transportation model (`models/tools/transportation/moving_america.py`) computes programs, receipts by source and the general-fund draw year by year. It has no demand response, so revenue from the steps and the premium is an upper bound [EV-MOV-206].
  - The budget model (`models/tools/budget/provisions.py`) books the ledger amounts on profiles (`models/data/inputs/fiscal-profiles.csv`).

## 1. What each law costs and raises

From the ledger (built from the transportation model by `models/tools/ledger-build.py`; `legacy/index/2029-trifecta-master-ledger.md`):

| Law | General-fund spending | New dedicated revenue (net of the offset) | Net | Window |
| --- | --- | --- | --- | --- |
| 2028 extension (MOV-28, 2027-28 exception) | A transfer keeping both accounts solvent through FY2031, not yet sized; working range up to about $131B (below) | Extends current rates; no new rates | — | FY2029-31 |
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
- **The 2028 extension's transfer: a working assumption.** Up to about $131 billion: CBO's cumulative shortfalls through FY2031 of $86.0 billion (highway account) and $45.2 billion (transit account) [EV-MOV-002], the upper bound under baseline case 1 (`3-design.md`). It is lower if a five-year law changes outlays or the 2029 act's receipts arrive first, and it is sized when the 2028 law is drafted. **How it scores:** under CBO's convention the baseline already assumes trust-fund outlays continue at current levels, so a general-fund transfer into the fund adds little or nothing to the measured deficit. The settlement should not count it as new cost. The cost of being wrong is small for this dossier: it is a 2027-28 exception and no 2029-on choice turns on it.

## 2. The general-fund draw by year

On the transportation model's own path. These are the plan's figures (grade D, project estimate). The draw is the general fund's share of the surface program's trust-fund, package and expansion lines (not sec. 1112's grants or the readiness reserve, below), not the increment over CBO's baseline:

| FY | Program ($B) | Dedicated receipts ($B) | General fund ($B) | % of GDP | 25% offset, not yet booked ($B) | Booked by the budget model ($B) |
| --- | --- | --- | --- | --- | --- | --- |
| 2029 | 119.0 | 50.0 | 69.0 | 0.194% | 0.0 | — |
| 2030 | 141.6 | 58.6 | 83.1 | 0.225% | 2.2 | 29.3 |
| 2032 | 164.2 | 84.3 | 79.9 | 0.200% | 7.5 | 54.7 |
| 2036 | 207.5 | 135.6 | 71.9 | 0.153% | 18.0 | 63.5 |
| 2037 | 196.1 | 147.0 | 49.1 | 0.100% | 20.8 | 38.0 |
| 2040 | 209.7 | 180.7 | 29.0 | 0.053% | 29.0 | 22.1 |
| 2044 | 234.8 | 220.8 | 14.0 | 0.022% | 38.7 | 25.6 |
| 2046 | 245.3 | 231.7 | 13.6 | 0.019% | 41.1 | 27.5 |

Sources: `Model().allocate(t)` in `moving_america.py` for the first four figures; the offset is `Model().cbo_basis(t)` less `allocate(t)`; the booked column is the budget model's MOV-29, MOV-30 and MOV-31 lines together (`provisions.py`, `score_all`, unified basis, on the profiles in `fiscal-profiles.csv`), whose window starts in FY2030. All run on November 10, 2026. The booked column is the increment over CBO's baseline, spread evenly over each act's window; the model's draw is the general fund's share of the program, timed as obligated (section 3, "Why the booked figure is lower"). The two paths cross: the booked path is below the model's in FY2030-36, when the packages and top-ups are paid, and above it from FY2037 on, as the booked successor grows with GDP while the model's draw falls with the premium. Section 3 also shows CBO's net basis, which adds the offset. The period averages match `golden/report.txt`: 0.180% in FY2032-36, 0.067% in FY2037-41, 0.026% in FY2042-46.

By FY2042-46, users cover 95% of highway renewal and all of transit's and rail's [EV-MOV-200] [EV-MOV-206].

### What the draw leaves out

The model's draw covers the trust-fund programs, the reconciliation packages and the 2031 bill's expansion appropriations. It leaves out two general-fund items that section 4 keeps. Both are disclosed here and not booked:

| Item | FY2032-36 | By year ($B) | Why it is separate |
| --- | --- | --- | --- |
| Sec. 1112's general-fund grants (multimodal freight and National Infrastructure Grants; MOV-31.27) | $17.24B authorized | 3.28 / 3.36 / 3.45 / 3.53 / 3.62 | Subject to appropriation, so these are authorizations, not expected outlays. H.R. 8870 authorizes similar grants, so part may already be in the baseline the plan starts from (`3-design.md`, baseline cases) |
| The readiness reserve (division A sec. 106(e); MOV-31.06) | $0 to $25B, contingent | illustrated 0 / 0 / 5 / 8 / 12 | Released only when a Tier 1 corridor clears its gates. Use could be anywhere from nothing to the cap |

If both were authorized and spent in full, the general fund's FY2032-36 figure would be $432.97 billion rather than $390.73 billion, and the peak year's all-in draw 0.208% of GDP rather than 0.200% (`moving_america.py`, `G1112`, `RESERVE`, `all_in_peak()`; run November 10, 2026). That is an upper bound, not an increment to book. How much of the grants is new depends on the baseline case, and how much of the reserve is used depends on readiness (section 8). Section 3's figures exclude both.

## 3. The fiscal-rule report

Under `DEC-2026-11-10-05`, the dossier reports its fiscal-rule effect and passes it to the settlement.

| Measure | As the budget model books it | On the transportation model's path |
| --- | --- | --- |
| FY2030-39, general-fund lines (MOV-29, -30, -31) | **$473.0 billion** (0.257 + 0.091 + 0.125 trillion), outlays spread over the window | The same lines, timed as obligated: packages in FY2029-31, top-ups and expansion in FY2032-36 |
| FY2030-39, new dedicated revenue | About $0.39 trillion (the surface trust fund channel, net of the offset) | $290.0B + $95.0B over each act's window |
| Permanent cost in FY2040, spending | **$22.1 billion**: a 30% tail on the reconciliation lines plus a successor authorization at 30% of MOV-31's run rate (`fiscal-profiles.csv`) | **$29.0 billion** (0.053% of GDP), the general fund's share of the program that year (excluding sec. 1112's grants and the reserve), falling to $14.0 billion by FY2044 as the premium phases in |
| The 25% offset (MR6), FY2040 | **Not yet booked; booking pending (step 2).** MR6's channel is the surface trust fund and it is on the revenue menu, not in the budget model's base (`ledger-revenue.csv`; `models/data/budget/provisions.csv`), so neither the ledger's general-fund total nor the fiscal model counts it | **$29.0 billion** (0.053% of GDP), rising from $2.2 billion in FY2030; $141.8 billion over FY2030-39 ($128.3 billion over each act's window in the ledger's MR6) |
| FY2040 general-fund effect, spending plus offset | **$51.1 billion** ($22.1 billion + $29.0 billion) | **$58.0 billion** (0.105% of GDP), the CBO-net basis below |
| Share of the plan-wide margin, FY2040 | The plan-wide shortfall the housing close-out reported, $50.8 billion (`models/data/recovery-budget-paths.csv`, case `mixed`, `agenda_gf_primary_bn`; `dossiers/home/6-cost.md`), includes transportation's $22.1 billion of spending, about 44% of it, and leaves out the offset. With the offset booked, the shortfall would be about $79.8 billion, and transportation's $51.1 billion about 64% of it | With the model's spending path as well, the shortfall would be about $86.7 billion, and transportation's $58.0 billion about two-thirds of it |

The shortfalls with the offset are this section's arithmetic (the reported $50.8 billion plus the unbooked amounts), before interest on the borrowing the offset adds in FY2030-39. Step 2's run of the budget model gives the booked figure.

**The figure reported to the settlement: in FY2040, $22.1 to $29.0 billion of spending (booked, and on the model's path) plus $29.0 billion of the 25% income and payroll tax offset, not yet booked: $51.1 to $58.0 billion in all, about 0.09% to 0.11% of GDP.**
- **Spending.** The first row counts spending only, booked and on the model's path, a gap of about $7 billion.
- **The offset.** It is lower income and payroll tax receipts on the new excises. Those receipts go to the general fund (and Social Security), not to the trust fund, and the transportation model credits the trust fund with gross receipts and spends them. So the general fund bears the offset. Its ledger line, MR6 (`models/data/inputs/ledger-revenue.csv`), books it on the trust fund's channel, which nets it against equal outlays, and the budget model leaves MR6 out of its base. It is therefore not yet booked; booking pending (step 2 of the milestone review's fixes, `review-milestone.md`, F-1): MR6 on the general fund in the base, as the carbon fee's identical offset (CX) is.
- **No double count.** Until step 2 lands, the offset is reported here on its own line. A figure that includes it (the CBO-net basis below) is labeled so and is never added to a spending line.

The model's CBO-net basis (`Model().cbo_basis(t)`) is the general fund's draw **with the offset included**, about $29 billion of the $58.0 billion in FY2040:

| FY | CBO-net draw, offset included ($B) | % of GDP |
| --- | --- | --- |
| 2032 | 87.4 | 0.218% |
| 2036 | 89.9 | 0.191% |
| 2040 | 58.0 | 0.105% |
| 2044 | 52.6 | 0.081% |

Its period averages are 0.209% in FY2032-36, 0.117% in FY2037-41 and 0.085% in FY2042-46 (`cbo_basis(t)`, run November 10, 2026). Draft 2's CBO-basis column, 0.220% in FY2032-36 and 0.143% in FY2037-41, gives each period's highest year, as `golden/report.txt` does (`report.py` prints the maximum), not its average.

**Why the booked figure is lower.** The budget model books $22.1 billion for three reasons:
- **Timing.** It spreads each act's ten-year amount evenly. The real money is packages in FY2029-31 and top-ups in FY2032-36.
- **Successor.** Its successor authorization is a placeholder at 30% of MOV-31's run rate.
- **Measure.** The model's draw is the general fund's share of the program (excluding sec. 1112's grants and the reserve), and CBO's baseline already carries trust-fund outlays at current levels. So part of the gap may be a difference of measure rather than of cost.

The spending range for FY2040, $22.1 to $29.0 billion (about 0.04% to 0.05% of GDP), is reported to the settlement as a working assumption. The offset is not part of that range: it is 25% of the new excises' gross receipts, $29.0 billion in FY2040, and like the receipts it is an upper bound, since the model has no demand response [EV-MOV-206]. No transportation choice turns on where in it the figure falls. Reconciling the two is the budget model's step that puts each bill in its own CBO window (B6 item 4).

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

The largest risk to the cost is revenue, not spending. Price pauses delay receipts, and the capped $25B backstop covers only part of it: three pauses would delay about $53.3B of FY2032-36 receipts against a $25B cap [EV-MOV-219]. The remaining roughly $28B is handled as Draft 2's sec. 108(c)(2) provides: once the backstop is exhausted, any shortfall in an account reduces its expansion programs first and its renewal programs only after those reach zero; sec. 105 and 106(e) amounts and executed agreements are not reduced. The deferred steps then resume, so the receipts return in later years, and the settlement decides whether to cover the gap from the general fund in the meantime. The model's lack of a demand response also overstates the steps' and the premium's yield.

## 5. Fit with the fairness test (D3)

Fuel taxes are a larger share of lower-income households' budgets, and transportation is the second-largest household expense [EV-MOV-013]. Section 7 reports the household cost by income. Whether the plan as a whole leaves lower- and middle-income households ahead is decided plan-wide in the financing settlement.

## Open questions

None for Espen; each is a question about money that stays with the settlement or the budget model:
1. **The 2028 extension's transfer** has a working range (up to about $131 billion, scoring at little or nothing against CBO's baseline; section 1). It is sized when the extension is drafted, on the baseline case then known.
2. **FY2040 booking of spending** ($22.1 billion booked; $29.0 billion on the model's spending path). For the budget model owner, with B6 item 4; a tier-3 inputs change if adopted.
3. **The 2030 act's window.** Rescore on FY2031-40 if it rides the FY2031 resolution (R3), as the ledger notes.
4. **The offset (MR6)** is not a question but a correction: $29.0 billion in FY2040, not yet booked; booking pending (step 2), a tier-3 inputs change because it touches `models/data/inputs/`.
