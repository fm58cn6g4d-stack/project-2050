# Index tools: how to regenerate the generated files

**In the repo (since Oct 20): run `bash index/tools/run-all.sh` from the repo root.** It does every step below in `build/`, handles the renames, and shows a diff; add `--write` to copy the outputs into `index/`. The manual steps below are kept for reference.

The transportation model behind Moving America (MOV-) is in `transportation/`, with its own readme. run-all.sh runs its test first (stopping if a Draft 2 figure moved) and writes `build/moving-america.json`, from which `ledger-build.py` takes the MOV-29/30/31 and MR1-MR6 rows.

These scripts regenerate the index/ files. Copy them into one working folder and run them in order:

1. `python3 ledger-build.py` writes ledger.json, bills.csv and the summary from the bill, revenue, conflict, options and dynamic tables in `index/data/inputs/ledger-*.csv` (see the readme there). Edit the tables there, never the ledger markdown. **Since the Oct 20 full rebuild every row is keyed by its domain-file ID** (HLT-1, CLI-5, IMM-1 ...), with the old ledger ID in a `legacy` column.
2. `python3 ledger-paths.py` writes paths.json, the floor-path model for D2 paths E, F, C and G. Its carve-out, top-fight and fast-track sets use domain IDs. Since Oct 20 (evening) it also prints a path C sensitivity (15, 20 and 25 days per minority fight, base and re-ordered top-fight lists) from the Talarico stress test; the sensitivity is printed only, not written to paths.json.
3. `python3 ledger-make-md.py` writes 2029-trifecta-master-ledger-v2.md. It copies two sections, "Transportation: the Moving America plan" and "Outside sources used for estimates", from the current index/2029-trifecta-master-ledger.md, so save that file as 2029-trifecta-master-ledger.md in the same folder first. File the output to index/2029-trifecta-master-ledger.md.
4. `python3 incidence.py` (filed as incidence-model.py) writes incidence.json, the D3 quintile model. Its rows (`index/data/inputs/incidence-rows.csv`) take their amounts from ledger.json by formula, so a ledger change flows through; keys are in `incidence-keys.csv`.
5. `python3 years.py` (filed as incidence-years.py) prints the year-by-year paths (phase-in profiles in `index/data/inputs/incidence-phase-in.csv`).
6. `python3 incidence-make-md.py` writes revenue-household-incidence-model.md from the two scripts above. File it to index/. (New Oct 20: the doc is now generated, not hand-written.)

7. **Long-term fiscal model (new Oct 20).** Run these after ledger-build.py:
   - `python3 fiscal-data.py --fetch --cache ../data/cbo --out ../data/fiscal-baseline.csv`: downloads CBO's standardized CSVs from github.com/US-CBO/cbo-data and writes index/data/fiscal-baseline.csv, the all-of-government baseline for FY1962-2056. Rerun only when CBO publishes a new vintage or an adjustment changes (FY2026_ACTUAL and ADJUSTMENTS live in the script).
   - `python3 fiscal-model.py --baseline ../data/fiscal-baseline.csv`: writes fiscal-model.json and fiscal-paths.csv. Year profiles for every ledger row live in `index/data/inputs/fiscal-profiles.csv` (loaded by fiscal-profiles.py): phase-in, growth index, time limits and the share that continues after 2039. A row with no profile is flagged and defaulted. Each profile is calibrated to the row's ledger ten-year midpoint, and a domain file's year-by-year score goes in `fiscal-years.csv`. Scenarios are the SCENARIOS list.
   - `python3 fiscal-make-md.py --baseline ../data/fiscal-baseline.csv`: writes fiscal-long-term-model.md; file it to index/.

8. **Consistency check (new Oct 20).** `python3 check-project.py` (run last; run-all.sh does it) writes index/check-report.md: headline figures quoted in the documents against this run, IDs cited but missing from their domain file, ledger and options-register mismatches, stale phrases from superseded decisions, each ledger row's figure against its domain file, scaled revenue figures re-run, and input-table checks. It changes nothing; the findings are for Espen to decide.
9. **Window rescaler.** `python3 window.py 272 2025-34` restates a ten-year figure in 2030-39 terms by CBO's nominal GDP path (`--index rev_individual` or another baseline category to track a tax base instead; `--to` for another window). The check uses it on revenue rows marked "scaled".

Two scripts import each other under their working names. Before running, rename incidence-model.py to incidence.py and incidence-years.py to years.py.

The dashboard (https://claude.ai/artifact/RDuHM7DqCwvLUtVaB4ANMs) reads bills.json, revenue.json, cuts.json and conflicts.json, which are split out of ledger.json. 

Current figures are not kept here: they are in the bottom line of index/2029-trifecta-master-ledger.md and the other generated files, and index/check-report.md lists any document still quoting an older figure. Sprint revenue rows use the prefix TS (TS1-TS12, TSX) so the old tariff row T1 keeps its ID.

The dashboard was republished Oct 20 (later) with the education batch and that day's decisions. cuts.json carries an `alternative_to` column: the page leaves those rows (C37) out of the every-option total.

Dynamic sensitivity (Oct 20, later): the DYNAMIC table (DY1-DY9, `index/data/inputs/ledger-dynamic.csv`) is printed in the ledger's "Dynamic sensitivity" section and summed into dynamic_lo/mid/hi/optimistic; it is never added to claims, the base or the gap (conventional mid −$0.56T, range −$1.42T to +$0.28T; Talarico-style +$0.55T; all estimates).

Caveat for the next rebuild: the prose in ledger-make-md.py (intro, the two "what changed" tables, the R2 paragraph, the calendar section; PREV_GAP and PREV_AFTER hold the previous rebuild's figures) and in incidence-make-md.py (bottom line, implications) is hardcoded around computed numbers. Update it by hand in the script when a batch lands.

Long-term model state (Oct 20): the adjusted baseline reaches 130% of GDP in 2039 and 180% in 2056, and the fiscal gap is 2.5% of GDP. With every option, the program brings 2056 debt to 162% and the gap to 1.9%. The general fund alone is about even by 2040; on the planning basis plus the sprint it is 0.26% of GDP short in 2039. D4-B's total-debt guardrails fail in every scenario. REV-TS1 and TS3 were accepted in principle, and the high-pay options REV-HP1 to HP4 were added; the ledger totals are unchanged.
