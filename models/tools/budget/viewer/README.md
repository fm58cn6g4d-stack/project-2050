# Fiscal viewer (budget piece B5, first version)

Role: one self-contained page, `fiscal-viewer.html`, that shows how the plan moves the federal fiscal path to FY2056, with every assumption one click away. Status: current (first version, on today's outputs; B3's provision outputs are added later).

**Open it:** open `fiscal-viewer.html` in any browser. No server, no external requests. It is generated, never edited by hand.

**Files**
- `build_viewer.py`: the generator. Reads `fiscal-model.json` (the model's output, written to `build/` by `run-all.sh`; the script regenerates it in a temp dir if you give no `--model`), the budget data layer through `../data.py` (the only place nominal figures become real dollars or % of GDP), and `models/data/budget/assumptions.csv`.
- `template.html`: layout, styles and the chart code. It holds no figures.
- `snapshot.json`: the headline figures the page showed last time. The page lists any that differ now ("What changed"). `run-all.sh` updates it with `--write`, keeping the figures from before, so rebuilding gives the same page.
- `test_viewer.py`: every printed figure traces to a source value; no hand-typed numbers; chart data matches its sources; no external requests; builds from a clean checkout. Run by `run-all.sh` (step 8g).
- `screenshots/`: the browser check at phone (390 px) and desktop (1440 px) widths.

**Regenerate:** `bash models/tools/run-all.sh --write` (the drift check in `.github/scripts/run-checks.sh` fails if the page or snapshot is stale).

**Which assumptions appear:** the `ASM-` entries whose `where` field points at code or data this page reads (`DRIVES` in `build_viewer.py`). Entries with `decided_by` of "unrecorded" are flagged "No recorded decision"; entries "Proposed by" a session are flagged "Proposed, not yet decided".

**Not shown yet:** budget authority versus outlays and appropriation types (B3); cautious-end readings; the decided program by category in dollars; other deflators or base years.
