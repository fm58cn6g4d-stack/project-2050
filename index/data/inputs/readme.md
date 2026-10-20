# Input tables

These are the hand-entered tables behind the generated files in `index/`. Edit them here, in a spreadsheet or a text editor, then run `bash index/tools/run-all.sh` (dry run with a diff) and `--write`. The scripts in `index/tools/` read them through `index/tools/inputs.py`. Before Oct 20, 2026 the same tables were typed inside the scripts; moving them changed no output.

Conventions:
- **Amounts** are ten-year totals for 2030-39 in $T unless a column says otherwise. Positive cost raises the deficit; savings are negative.
- **Numbers keep their form.** Type `0` or `0.0` as the old table had it: the generated files print `2` and `2.0` differently.
- **Yes/no columns** take `yes` or `no`.
- **Blank cells** mean "not set": the script's default applies.
- Keep commas inside quoted text. A spreadsheet does this when it saves as CSV.

| File | One row per | What it feeds |
| --- | --- | --- |
| `ledger-bills.csv` | ledger bill (keyed by domain-file ID; `legacy_id` is the old ledger ID) | the master ledger: claims, floor days, felt-by-midterm |
| `ledger-revenue.csv` | revenue option; `in_base` = in the general-fund base | the ledger's revenue menu and base |
| `ledger-cuts.csv` | option to close the gap (C-numbers); `kind` decides how it counts ("accepted", "Declined", "Borrow") | gap after accepted options |
| `ledger-conflicts.csv` | conflict between documents, with the `batch` it was raised in | the ledger's conflicts section |
| `ledger-dynamic.csv` | macroeconomic feedback (DY-) | the dynamic sensitivity section; never in a total |
| `incidence-keys.csv` | distribution key: shares Q1-Q5 (summing to 100) and the top 1%'s share of the total | the D3 household test |
| `incidence-rows.csv` | household-facing row (`set` = package) or option (`set` = option) | the D3 household test |
| `incidence-phase-in.csv` | phase-in profile for the year-by-year incidence | the incidence doc's years table |
| `fiscal-profiles.csv` | ledger row's year profile (`table` = bill, base revenue or option) | the long-term fiscal model |
| `votes-bills.csv` | bill or package provision that faces a vote: Democratic objection rate by archetype, Republican crossover, House exposure, carve-out flag, basis | the vote simulation |
| `votes-senate.csv` | Democratic senator or race: archetype, margin, and which seat-count scenarios (51-54) include it | the vote simulation |
| `funds-ss-rates.csv` | year 2026-2100: OASDI income and cost rates (% of taxable payroll), 2026 Trustees intermediate | the dedicated-fund engine (Social Security) |
| `funds-ss-economics.csv` | Trustees anchor year: taxable payroll, GDP, the trust-fund interest factor (interpolated between) | the dedicated-fund engine (all funds' payroll and interest) |
| `funds-ss-provisions.csv` | D8 provision (SS-1 to SS-5) on its face: kind of tax or benefit change, rate, threshold, start year, benefit credit, extra haircut, the ledger rows holding its ten-year figure | the dedicated-fund engine (Social Security scenarios) |
| `funds-ss-ssa-runs.csv` | SSA actuaries' single-year score of a provision (run), by year 2026-2101: change in cost, income and balance (% of payroll), 2026 Trustees basis | the tax bases the D8 provisions are evaluated on, and the model's checks |
| `funds-ss-ssa-summary.csv` | SSA run: provision number, description, start year, 75-year changes, source URL | the same |
| `funds-hi-rates.csv` | year the Medicare Trustees publish an HI cost or income rate | the dedicated-fund engine (HI) |
| `funds-parameters.csv` | one parameter (reserves, leave rule, carbon dividend share, population, EDU-9B base), each with its basis | the dedicated-fund engine |
| `fiscal-years.csv` | row with a year-by-year path ($B, 2030-39) that overrides its profile | the long-term fiscal model |

## Figures that come from elsewhere
- **`model:NAME`** in a ledger cell (MOV-29/30/31, MR1-MR6) means the transportation model supplies the figure (`index/tools/transportation/`). Notes on those rows carry the model's figures as `{act29_package:.1f}` and similar.
- **Incidence amounts** are formulas over ledger IDs, for example `[G1]`, `[O2]+[OX]` or `-0.3*[HLT-6]`. They are read from the ledger when the incidence model runs, so a ledger change flows through. A plain number is used where the incidence row is its own estimate (PB, H5p, EDUB, SAFR2) or differs from the ledger. The four rows that differ carry the matching ledger formula in `check`: MR 0.41 vs 0.4098, MRc 0.126 vs 0.1267, PS1 0.091 vs 0.09, EDUP 2.27 vs ED1 2.10.
- **Incidence parts** split a row's amount `x` across keys. `above450k` alone takes all of it. `wages 0.25*x; capital 0.75*x` is the 25/75 corporate convention. Plain numbers are fixed amounts.
- **Phase-in methods:** for `ramp`, the yearly levels grow 4% a year and are then normalised. For `norm`, the levels are normalised as typed. `same_as` borrows another row's profile.

The scenario lists (incidence `SCEN`, fiscal `SCENARIOS`) and the accounting rules (`GF_RULE`, `OWN_RANGE` in ledger-build.py) are still in the scripts.
