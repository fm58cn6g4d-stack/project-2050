# Transportation: cost and financing

Role: section 6 of the transportation dossier. It prices the provisions of section 4 on the transportation model and the federal budget model, and reports the fiscal-rule effect to the financing settlement (`charter/STANDARDS.md`, "Fiscal rule in dossiers: report, don't gate"). Status: reviewed at L3 (`review-milestone.md`; fixes #208 to #211) and booked in the budget model: the offset MR6 (#209), Moving America's two acts in the years they name and the draw after the window (#289, `DEC-2026-11-12-08`), and the FY2037-39 draw (#297, `DEC-2026-11-12-10`). On the decisions in `DEC-2026-11-10-08`, which change no dollar figure: the transportation model's figures are the legacy design's, rerun; the booked figures are the budget model's generated row paths.

## Counting rules

- **Conventions.** The project's budget conventions (`models/tools/budget/CONVENTIONS.md`): nominal dollars by fiscal year, deficit effects positive for a cost, the common window FY2030-39 (`ASM-WINDOW`).
- **Increment.** The ledger counts what the plan adds above CBO's baseline (`ASM-INCREMENT`). For transportation that means:
  - the general-fund lines: the 2029 and 2030 packages, the renewal top-ups and the 2031 bill's expansion appropriations;
  - the new dedicated revenue, credited to the trust fund gross, with the income and payroll tax offset on it booked separately (MR6, a scoring convention) at JCT's 24.4% (`ASM-EXCISE-OFFSET`, `DEC-2026-11-12-08`). The offset itself falls on the general fund, where the budget model books it as MR6 (section 3). The transportation model's own figures keep Draft 2's 25%.
- **Two models.**
  - The transportation model (`models/tools/transportation/moving_america.py`) computes programs, receipts by source and the general-fund draw year by year. It has no demand response, so revenue from the steps and the premium is an upper bound [EV-MOV-206].
  - The budget model (`models/tools/fiscal-model.py`, with `models/tools/budget/provisions.py`) books the ledger amounts by year (`models/data/inputs/fiscal-years.csv` inside the window, `fiscal-after.csv` after it) and on profiles elsewhere (`fiscal-profiles.csv`).

## 1. What each law costs and raises

From the ledger (built from the transportation model by `models/tools/ledger-build.py`; `legacy/index/2029-trifecta-master-ledger.md`):

| Law | General-fund spending | New dedicated revenue (net of the model's 25% offset) | Net | Window |
| --- | --- | --- | --- | --- |
| 2028 extension (MOV-28, 2027-28 exception) | A transfer keeping both accounts solvent through FY2031, not yet sized; working range up to about $131B (below) | Extends current rates; no new rates | — | FY2029-31 |
| 2029 act (MOV-29, R1) | $47.0B package one + $209.74B renewal top-ups for FY2032-35 | $290.0B ($386.7B gross): fuel taxes indexed with steps, the clean-vehicle charge, truck excises | About $33.3B deficit reduction | FY2029-38 |
| 2030 act (MOV-30, R3) | $33.5B package two + $57.33B top-ups for FY2035-36 | $95.0B ($126.7B gross): weight-distance charge, rail diesel, aviation surcharge | About $4.2B deficit reduction | FY2030-39, to be rescored on FY2031-40 if carried on the FY2031 resolution |
| Moving America Act of 2031 (MOV-31) | $123.70B expansion and about $1B for division E | Restates the 2029-30 revenue | Cost | FY2032-36 |

Over FY2032-36 the 2031 bill authorizes $936.57B. Dedicated receipts cover $545.84B and the general fund $390.73B, or 0.180% of GDP a year [EV-MOV-200].

**Commitment, assumption or open question.**
- **Commitments** (decided): the program levels, the rates and the vehicles.
- **Working assumptions:**
  - the offset: JCT's 24.4% as booked (`DEC-2026-11-12-08`); the transportation model's figures in this section use Draft 2's 25%;
  - 2.5% inflation and 4.1% nominal GDP growth in the transportation model;
  - no demand response (an upper bound on receipts).
- **The 2028 extension's transfer: a working assumption.** Up to about $131 billion: CBO's cumulative shortfalls through FY2031 of $86.0 billion (highway account) and $45.2 billion (transit account) [EV-MOV-002], the upper bound under baseline case 1 (`3-design.md`). It is lower if a five-year law changes outlays or the 2029 act's receipts arrive first, and it is sized when the 2028 law is drafted. **How it scores:** under CBO's convention the baseline already assumes trust-fund outlays continue at current levels, so a general-fund transfer into the fund adds little or nothing to the measured deficit. The settlement should not count it as new cost. The cost of being wrong is small for this dossier: it is a 2027-28 exception and no 2029-on choice turns on it.

## 2. The general-fund draw by year

On the transportation model's own path. These are the plan's figures (grade D, project estimate). The draw is the general fund's share of the surface program's trust-fund, package and expansion lines (not sec. 1112's grants or the readiness reserve, below), not the increment over CBO's baseline:

| FY | Program ($B) | Dedicated receipts ($B) | General fund ($B) | % of GDP | 25% offset, model ($B) | Spending booked by the budget model ($B) | Offset booked (MR6 at 24.4%, $B) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2029 | 119.0 | 50.0 | 69.0 | 0.194% | 0.0 | — | — |
| 2030 | 141.6 | 58.6 | 83.1 | 0.225% | 2.2 | 40.1 | 1.9 |
| 2032 | 164.2 | 84.3 | 79.9 | 0.200% | 7.5 | 86.4 | 6.7 |
| 2036 | 207.5 | 135.6 | 71.9 | 0.153% | 18.0 | 67.6 | 15.9 |
| 2037 | 196.1 | 147.0 | 49.1 | 0.100% | 20.8 | 49.0 | 18.4 |
| 2040 | 209.7 | 180.7 | 29.0 | 0.053% | 29.0 | 29.0 | 24.5 |
| 2044 | 234.8 | 220.8 | 14.0 | 0.022% | 38.7 | 13.9 | 28.4 |
| 2046 | 245.3 | 231.7 | 13.6 | 0.019% | 41.1 | 13.6 | 30.5 |

Sources: `Model().allocate(t)` in `moving_america.py` for the first four figures; the offset is `Model().cbo_basis(t)` less `allocate(t)`; the transportation model's figures were run on November 10, 2026. The booked spending column is the budget model's MOV-29, MOV-30 and MOV-31 lines together, and the booked offset its MR6 line, from the fiscal model's generated row paths (`models/tools/fiscal-model.py`, the `rows` of its JSON output; unified and general-fund bases are the same for these rows), whose window starts in FY2030. MOV-29 and MOV-30 are booked in the years the acts pay, packages in FY2030-31 (FY2029's share counted in FY2030) and top-ups in FY2032-36, and nothing after (`DEC-2026-11-12-08`). From FY2037 MOV-31's successor line carries the model's own general-fund draw (`DEC-2026-11-12-10` for FY2037-39, `fiscal-years.csv`; `DEC-2026-11-12-08` after the window, `fiscal-after.csv`), so from FY2037 the booked column is the model's draw, rounded. Before FY2037 the two differ: the booked column is the increment over CBO's baseline, while the model's draw is the general fund's share of the program, timed as obligated (section 3, "Why the paths differ before FY2037"). Section 3 also shows CBO's net basis, which adds the offset. The period averages match `golden/report.txt`: 0.180% in FY2032-36, 0.067% in FY2037-41, 0.026% in FY2042-46.

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
| FY2030-39, general-fund lines (MOV-29, -30, -31) | **$597.0 billion** (0.257 + 0.091 + 0.249 trillion): the packages and top-ups in the years the acts name (`DEC-2026-11-12-08`), the expansion in FY2032-36, and from FY2037 the model's draw on MOV-31's successor line (`DEC-2026-11-12-10`) | The same lines, timed as obligated: packages in FY2029-31, top-ups and expansion in FY2032-36, then the general fund's share of the program |
| FY2030-39, new dedicated revenue | About $0.51 trillion gross in the surface trust fund channel; the offset is booked separately on the general fund (MR6) | $290.0B + $95.0B over each act's window |
| Permanent cost in FY2040, spending | **$29.0 billion**, booked on MOV-31's successor line at the transportation model's draw (`fiscal-after.csv`, `DEC-2026-11-12-08`), falling to $13.9 billion by FY2044 | **$29.0 billion** (0.053% of GDP), the general fund's share of the program that year (excluding sec. 1112's grants and the reserve), falling to $14.0 billion by FY2044 as the premium phases in |
| The offset (MR6), FY2040 | **$24.5 billion, booked** on the general fund in the budget model's base at JCT's 24.4%, as the carbon fee's identical offset (CX) is (#209; `ledger-revenue.csv`; `DEC-2026-11-12-08`); $125.3 billion over FY2030-39 (the ledger's MR6, each act's window) | **$29.0 billion** at the model's 25% (0.053% of GDP), rising from $2.2 billion in FY2030; $141.8 billion over FY2030-39 |
| FY2040 general-fund effect, spending plus offset | **$53.5 billion** ($29.0 billion + $24.5 billion) | **$58.0 billion** (0.105% of GDP), the CBO-net basis below |
| Share of the plan-wide margin, FY2040 | The plan-wide FY2040 general-fund primary balance is **$4,240.4 billion short** (7.83% of GDP; `models/data/recovery-budget-paths.csv`, case `mixed`, `agenda_gf_primary_bn`), nearly all of it health's premium-to-tax shift (`dossiers/care/6-cost.md`, part 5); transportation's $53.5 billion is about 1.3% of it | On the model's offset, $4.5 billion more |

**The two offset figures differ by about $4.5 billion in FY2040** ($24.5 billion booked against $29.0 billion on the model's path) because the booking applies JCT's 24.4% to the ledger's window totals (the model's yearly shape scaled to them) and carries the line on its profile after 2039, as CX is, while the model takes 25% of each year's gross receipts. No transportation choice turns on the difference.

**The figure reported to the settlement: in FY2040, $29.0 billion of spending (booked, and the model's draw) plus the income and payroll tax offset ($24.5 billion booked at 24.4%; $29.0 billion at the model's 25%): $53.5 to $58.0 billion in all, about 0.10% to 0.11% of GDP.**
- **Spending.** The booked FY2040 spending is the model's draw, so the two bases agree on it.
- **The offset.** It is lower income and payroll tax receipts on the new excises. Those receipts go to the general fund (and Social Security), not to the trust fund, and the transportation model credits the trust fund with gross receipts and spends them. So the general fund bears the offset. Its ledger line, MR6 (`models/data/inputs/ledger-revenue.csv`), books it on the general fund in the budget model's base, as the carbon fee's identical offset (CX) is (#209, step 2 of the milestone review's fixes, `review-milestone.md`, F-1).
- **The rate.** The booking uses JCT's 24.4% until JCT publishes a table on current law, then its yearly figures (`ASM-EXCISE-OFFSET`, `DEC-2026-11-12-08`). JCT's yearly offset rate has run 21% to 25% recently (24.3% in 2022), and CBO books the whole offset on-budget (CBO, 2022, publication 58421; SRC-2452, text SRC-2453). The model's column keeps Draft 2's flat 25%, so it slightly overstates the offset.
- **No double count.** The offset is reported on its own line. A figure that includes it (the CBO-net basis below) is labeled so and is never added to a spending line.

The model's CBO-net basis (`Model().cbo_basis(t)`) is the general fund's draw **with the offset included**, about $29 billion of the $58.0 billion in FY2040:

| FY | CBO-net draw, offset included ($B) | % of GDP |
| --- | --- | --- |
| 2032 | 87.4 | 0.218% |
| 2036 | 89.9 | 0.191% |
| 2040 | 58.0 | 0.105% |
| 2044 | 52.6 | 0.081% |

Its period averages are 0.209% in FY2032-36, 0.117% in FY2037-41 and 0.085% in FY2042-46 (`cbo_basis(t)`, run November 10, 2026). Draft 2's CBO-basis column, 0.220% in FY2032-36 and 0.143% in FY2037-41, gives each period's highest year, as `golden/report.txt` does (`report.py` prints the maximum), not its average.

**Why the paths differ before FY2037.** In FY2030-36 the booked lines are the increment over CBO's baseline in the years each act pays, while the model's draw is the general fund's share of the program (excluding sec. 1112's grants and the reserve). CBO's baseline already carries trust-fund outlays at current levels, so the gap is a difference of measure rather than of cost. From FY2037 the booked successor line is the model's draw (`DEC-2026-11-12-10`, `DEC-2026-11-12-08`), and it falls with the premium as the model's does.

The FY2040 spending figure, $29.0 billion (about 0.05% of GDP), is reported to the settlement as a working assumption. The offset is reported beside it: the booked $24.5 billion, or $29.0 billion at the model's 25%, and like the receipts it is an upper bound, since the model has no demand response [EV-MOV-206]. No transportation choice turns on where in that range the figure falls.

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
2. **The 2030 act's window.** Rescore on FY2031-40 if it rides the FY2031 resolution (R3), as the ledger notes.

Settled: the FY2040 spending is booked at the model's $29.0 billion (#289, `DEC-2026-11-12-08`), the FY2037-39 draw is booked (#297, `DEC-2026-11-12-10`), and the offset is booked at JCT's 24.4% ($24.5 billion in FY2040; #209, #289).
