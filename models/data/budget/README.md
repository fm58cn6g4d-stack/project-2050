# Budget data layer

Role: the budget series every piece of the federal budget model reads (workflow piece B2, `models/tools/budget/WORKFLOW.md`). It holds plain CSV series by category and year, the category list, and their sources. Status: current. Read it with `models/tools/budget/data.py`, the loader. That loader holds the only two conversions later pieces may use: `to_real` (nominal to real dollars) and `to_pct_gdp` (nominal to share of GDP).

**There is one baseline.** This layer adds no second one. From these files alone, `data.adopted_baseline()` rebuilds the adopted baseline, `models/data/fiscal-baseline.csv`, for FY1962-2056. Every cell matches: each category, the totals, the FY2026 actuals and the ADJ-T1 and ADJ-T2 adjustments. The baseline file stores billions to three decimals, the nearest $1 million, and that is its only rounding. Before rounding, each value is the same floating-point number that `fiscal-data.py` computes, so the match holds to the cent. `models/tools/budget/test_data.py` checks this on every run (`run-all.sh` step 5b). `fiscal-data.py` stays the canonical builder until piece B6, when Codex makes the fiscal model read this layer.

**Units.** Billions of nominal dollars by federal fiscal year, unless a column says otherwise. Shares of GDP are percentages.

## Files

| File | What it holds | Years | Written by |
| --- | --- | --- | --- |
| `categories.csv` | The category list later pieces must use: each category's kind (receipts, mandatory, discretionary or interest), what it measures, how it is built from CBO's variables in each period, and the OMB functions it maps to | — | by hand |
| `post-february.csv` | FY2026 preliminary actuals and the post-February adjustments ADJ-T1 and ADJ-T2. A copy of `FY2026_ACTUAL` and `ADJUSTMENTS` in `fiscal-data.py`; the test fails if the two differ | FY2026-2056 | by hand |
| `cbo-historical.csv` | CBO historical budget data, the variables the baseline uses | FY1962-2025 | `build_data.py` |
| `cbo-ten-year.csv` | CBO's February 2026 ten-year baseline, including discretionary budget authority, defense and nondefense, base and emergency | FY2025-2036 | `build_data.py` |
| `cbo-long-term.csv` | CBO's February 2026 long-term budget outlook, as shares of GDP, with GDP | FY2026-2056 | `build_data.py` |
| `cbo-economic.csv` | CBO's fiscal-year economic projections: GDP, CPI-U, GDP price index, 3-month bill and 10-year note rates | FY2023-2036 | `build_data.py` |
| `cbo-economic-historical.csv` | CBO's fiscal-year economic history: GDP, CPI-U, GDP price index | FY1950-2025 | `build_data.py` |
| `cbo-long-term-economic.csv` | CBO's long-term economic levels: GDP, CPI-U and GDP price index levels | calendar 1996-2056 | `build_data.py` |
| `deflators.csv` | CPI-U and the GDP price index as one fiscal-year series each (see "Deflators") | FY1950-2056 | `build_data.py` |
| `omb-outlays-by-function.csv` | OMB Historical Table 3.2: outlays by function and subfunction | FY1962-2025 | `build_data.py` |
| `omb-ba-by-function.csv` | OMB Historical Table 5.1: budget authority by function and subfunction | FY1976-2025 | `build_data.py` |
| `omb-discretionary.csv` | OMB Historical Tables 5.6 and 8.7: discretionary budget authority and outlays by program group, defense and nondefense | BA FY1976-2025; outlays FY1962-2025 | `build_data.py` |
| `spendout-discretionary.csv` | Estimated spend-out of discretionary budget authority, defense and nondefense (see "Spend-out") | fit on FY1993-2019 | `build_data.py` |
| `omb/*.xlsx` | The four OMB tables as published, the source for the OMB files above | — | downloaded |

Run `python3 models/tools/budget/build_data.py` to rewrite the generated files. Add `--check` to compare them with the committed copies instead. The CBO values are copied exactly as CBO wrote them. OMB's values are converted from millions to billions exactly. OMB's estimate columns (FY2026 on) are the administration's proposals and are left out: only actual years are kept. Where OMB prints no amount, the cell is blank and `flag` says why (`none`, `under_0.5m` for "$500 thousand or less", `n/a`).

## Sources

| Source | Address | Retrieved | Rights |
| --- | --- | --- | --- |
| CBO, *The Budget and Economic Outlook: 2026 to 2036* and *The Long-Term Budget Outlook: 2026 to 2056* (February 2026), as CBO's standardized CSVs: historical budget, ten-year budget, long-term budget, fiscal-year economic projections, fiscal-year economic history, long-term economic levels | `https://github.com/US-CBO/cbo-data`, files `data/budget/{historical_budget/annual_fy,ten_year_budget/annual_fy,long_term_budget/annual_fy}_2026-02.csv` and `data/economic/{economic_projections/fiscal,historical_economic/annual_fy,long_term_economic/levels}_2026-02.csv` | Cached in `models/data/cbo/` (in the repository since October 28, 2026). On November 8, 2026 all six were byte-identical to the repository's current copies (commit `284a956`, June 12, 2026) | US government work, public domain |
| OMB, *Historical Tables, Budget of the U.S. Government, Fiscal Year 2027* (April 2026): tables 3.2, 5.1, 5.6, 8.7 | `https://www.whitehouse.gov/wp-content/uploads/2026/04/hist_fy2027.zip` (page: `https://www.whitehouse.gov/omb/information-resources/budget/historical-tables/`); zip SHA-256 `7a5033e6ef074e190442084a1af528fd459040a951e06659432f5bb4ec01ef9d` | November 8, 2026 | US government work, public domain |
| FY2026 preliminary actuals: CBO *Monthly Budget Review for September 2026*, as reported by AAF and CRFB, October 8, 2026 | as cited in `fiscal-data.py` | carried over from `fiscal-data.py` | cited only |
| ADJ-T1 (CRFB, July 2026) and ADJ-T2 (AAF, October 2026) | as cited in `fiscal-data.py` | carried over from `fiscal-data.py` | cited only; these are analysis (estimates), not data |

**Which administration.** The OMB tables come from the FY2027 Budget of the second Trump administration. Only the actual years are used. Those are recorded outlays and budget authority, which is data, not analysis. They are checked against CBO's independent historical series: total outlays are identical through FY2019 and within 0.6% in FY2020-2025, and discretionary defense and nondefense outlays are within 0.2% in every year (`test_data.py`). The FY2020-2025 gap is largest in FY2020 (OMB $36.8 billion lower) and FY2024 ($15.6 billion lower). The layer keeps both series and does not explain the gap; the benchmarks piece (B4) should, before either is used for those years.

**Blocked.** `www.cbo.gov` returns 403 to this session, as the board's "Known gaps" notes. CBO's standardized CSVs on GitHub carry everything above. One useful CBO file is not on GitHub, and Espen could upload it from cbo.gov: CBO's *Spending Projections, by Budget Account* for the February 2026 baseline (the budget-account spreadsheet). It has budget authority and outlays by account, which would let B3 use CBO's own account-level spend-out instead of the estimate below. GovInfo was not needed: OMB's own site served the tables.

## Categories

`categories.csv` has twelve baseline categories (`level` = `baseline`). They add up to the totals: five receipts categories, seven outlays categories (four mandatory, two discretionary, one interest). Six detail rows give discretionary budget authority, defense and nondefense, total, base and emergency (`level` = `detail`). The columns `cbo_historical`, `cbo_ten_year` and `cbo_long_term` give each category's recipe in that period: CBO variables added or subtracted left to right, or for FY2037-2056 a share of GDP (`gdp_share:`), with total discretionary split by CBO's FY2036 defense share (`gdp_share_split:`). `omb_functions` maps each outlay category to OMB budget functions. `omb_discretionary` names the OMB discretionary program group for the two discretionary categories. Receipts have no function: OMB reports them by source.

Later pieces use these categories as they are. Adding or splitting one is a change to this file, and every piece reading it must agree (workflow, "Shared interfaces").

## Deflators

`deflators.csv` holds CPI-U (CBO's base, 1982-84 = 100) and the GDP price index (BEA's base, calendar 2017 = 100) by fiscal year:

- FY1950-2025: CBO's fiscal-year economic history (actuals);
- FY2026-2036: CBO's fiscal-year economic projections;
- FY2037-2056: CBO publishes long-term price levels by calendar year only, at three significant decimals. The series continues from FY2036 by each calendar year's growth in CBO's long-term level. The result averages 2.27% a year for CPI-U and 2.00% for the GDP price index over FY2037-2056. CBO's long-term levels are rounded, so single-year growth rates are uneven by a few hundredths of a point.

`to_real(values, base_year, index)` turns nominal into constant dollars of `base_year`. It defaults to the GDP price index and FY2026 dollars (`DEFAULT_INDEX`, `DEFAULT_BASE_YEAR` in `data.py`). Those defaults are proposals for the assumptions register (piece B1), and a later piece can change either one there. `to_pct_gdp(values)` divides by the adopted baseline's GDP series: CBO's historical GDP to FY2024, the fiscal-year economic projection FY2025-2036, the long-term budget file's GDP after that. So a share of GDP here always matches the baseline's own.

The fiscal model's in-code CPI path (`CPI` in `fiscal-model.py`: 2.26% to 2036, 2.3% after) is a rounded version of this series. It is not replaced here: that is B6.

## Spend-out

OMB publishes discretionary budget authority and outlays, but not how fast each year's budget authority is spent. `spendout-discretionary.csv` estimates that from the totals. It fits outlays in year t as shares of budget authority in years t, t-1, t-2 and t-3, by least squares, over FY1993-2019. That window starts after credit reform and ends before the pandemic emergency appropriations. The result:

| | Year 1 | Year 2 | Year 3 | Year 4 | Shares add to | Fit error |
| --- | --- | --- | --- | --- | --- | --- |
| Defense | 44% | 34% | 24% | -4% | 0.98 | 2.2% of mean outlays |
| Nondefense | 27% | 37% | 31% | 15% | 1.10 | 3.6% |

Read these as rough. The defense year-4 share is slightly negative, which is noise in the fit. Nondefense shares add to more than one because nondefense discretionary outlays include highway and transit spending under obligation limitations. That budget authority is mandatory contract authority, so OMB does not count it as discretionary. B3 should treat these shares as placeholders until CBO's account-level spend-out is uploaded (see "Blocked").
