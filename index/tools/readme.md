# Index tools: how to regenerate the generated files

**Run `bash index/tools/run-all.sh` from the repo root.** It does every step below in `build/`, handles the renames, and shows a diff against `index/`; add `--write` to copy the outputs into `index/`, and `--fetch` to re-download CBO's data first. Never edit the generated files by hand: change an input table in `index/data/inputs/` (see the readme there) or a script, then regenerate.

The steps, in the order run-all.sh runs them:

0. **Transportation.** `transportation/test_moving_america.py` checks that the Moving America model still gives Draft 2's figures (run-all stops if one moved), then `transportation/report.py --json` writes `moving-america.json`, from which the ledger takes the MOV-29/30/31 and MR1-MR6 rows. The model has its own readme.
1. `ledger-build.py` writes ledger.json and bills.csv from the bill, revenue, conflict, options and dynamic tables in `index/data/inputs/ledger-*.csv`. Every row is keyed by its domain-file ID (HLT-1, CLI-5, IMM-1 ...), with the old ledger ID in a `legacy` column.
2. `ledger-paths.py` writes paths.json, the floor-path model for D2 paths E, F, C and G (carve-out, top-fight and fast-track sets by domain ID), and prints a path C sensitivity from the Talarico stress test (15, 20 and 25 days per minority fight; printed only).
3. `ledger-make-md.py` writes the master ledger (index/2029-trifecta-master-ledger.md) from ledger.json, paths.json and moving-america.json.
4. `incidence-model.py` (run as incidence.py) writes incidence.json, the D3 household net test. Its rows (`incidence-rows.csv`) take their amounts from ledger.json by formula, so a ledger change flows through; keys are in `incidence-keys.csv`. Scenario Q is the decided package; the other scenarios (in the script's SCEN list) vary one choice against it. `incidence-years.py` (run as years.py) spreads each row over 2030-39 with the profiles in `incidence-phase-in.csv`. `incidence-make-md.py` writes index/revenue-household-incidence-model.md. The two incidence scripts import each other under their working names, which is why run-all.sh renames them.
5. `fiscal-data.py` builds index/data/fiscal-baseline.csv, the all-of-government baseline for FY1962-2056, from CBO's standardized CSVs (github.com/US-CBO/cbo-data, cached in index/data/cbo/; `--fetch` re-downloads). FY2026_ACTUAL and ADJUSTMENTS live in the script.
6. `fiscal-model.py` writes fiscal-model.json and index/data/fiscal-paths.csv. Year profiles for every ledger row are in `fiscal-profiles.csv` (loaded by fiscal-profiles.py): phase-in, growth index, time limits and the share that continues after 2039; each is calibrated to the row's ledger ten-year midpoint, and a year-by-year score goes in `fiscal-years.csv`. Scenarios are the script's SCENARIOS list (DEC is the decided package). `fiscal-make-md.py` writes index/fiscal-long-term-model.md.
7. **Consistency check.** `check-project.py` writes index/check-report.md: headline figures quoted in the documents against this run, IDs cited but missing from their domain file, ledger and options-register mismatches, stale phrases from superseded decisions, each ledger row's figure against its domain file, scaled revenue figures re-run, and input-table checks. It changes nothing; the findings are for Espen to decide.

**Window rescaler.** `python3 index/tools/window.py 272 2025-34` restates a ten-year figure in 2030-39 terms by CBO's nominal GDP path (`--index rev_individual` or another baseline category to track a tax base instead; `--to` for another window). The check uses it on revenue rows marked "scaled".

**Conventions.** Sprint revenue rows use the prefix TS (TS1-TS12, TSX) so the tariff row T1 keeps its ID; high-pay options are HP1-HP3. The dynamic sensitivity table (DY1-DY9) is printed in the ledger and never added to claims, the base or the gap.

**Dashboard.** The ledger dashboard (https://claude.ai/artifact/RDuHM7DqCwvLUtVaB4ANMs) reads bills.json, revenue.json, cuts.json and conflicts.json, split out of ledger.json; cuts.json carries an `alternative_to` column so the page leaves alternatives out of the totals.

Current figures are not kept here: they are in the generated files, and index/check-report.md lists any document still quoting an older one.
