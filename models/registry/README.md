# Registry checker

Role: verifies every link between project records (`charter/PLAN.md`, section 4). Status: current (stage A, step 4). It runs on every PR as step 8e of `models/tools/run-all.sh`.

`python3 models/registry/check.py` (add `--strict` to fail on past-due re-checks) checks:

| Record | Check |
| --- | --- |
| `agenda/agenda.csv` | Every legacy policy and option ID appears once; levels are L0–L4 |
| `library/catalog.csv` | Every document in `legacy/` and the intake is catalogued; paths exist; the name index is current |
| `charter/decisions.md`, `charter/outcomes.md` | `DEC-` and `OUT-` IDs are unique |
| `dossiers/*/evidence.json` | A catalogued source; the exact anchor passage, or each passage in a list of them, exists in it (or in its `text_version`), or, for a citation row (a licensed source the repository does not hold), each anchor is a quotation of at most 60 words with a `locator`; every figure and every number in the statement appears in the anchors; every rounded figure follows from an anchored value; grade A–E; data or analysis, and an analysis entry's corroboration resolves (a warning until one that supports or qualifies it comes from an independent publisher); valid dates; a past-due re-check warns |
| `dossiers/*/provisions.json` | `HOU-4A.01`-style IDs whose parent is in the agenda, citing known evidence |
| Text in `charter/`, `dossiers/`, `public/`, `agenda/`, `models/` | Every cited `SRC-`, `EV-`, `OUT-` and `DEC-` ID resolves |

In Markdown, an ID in a fenced code block is a format example and is not checked. Any other ID, plain or in inline code, is a citation and must resolve; placeholders such as `DEC-YYYY-MM-DD-NN` never match an ID pattern.

**Restatement check** (`restatement.py`, `charter/PLAN.md` 4). When legacy content becomes a dossier, it lists every number and policy ID in the legacy file that the dossier files no longer contain: `python3 models/registry/restatement.py SOURCE RESULT... [--accounted LOG...]`, or `--map dossiers/<name>/restatement.json` for one dossier's pairs. Thousands commas and trailing decimal zeros are ignored ("$55.00B" matches "$55B"); leading zeros are dropped; numbers inside IDs and URLs are skipped. Matching is set-wide: a token counts as carried over if it appears anywhere in the result files, so the report finds what was dropped, not what was changed. The map and the accounted files never count as results. A token dropped on purpose counts as accounted for when it is written in `backticks` in an accounted file (the dossier's restatement log or the decision log). A pair may instead carry `"by_reference": "<reason>"` when the dossier incorporates that file's remaining detail by reference (a drafting base, or a status note merged into a governing file): the report prints one line with the reason, and `--strict` does not count it. Each such file needs its own accurate reason. Step 8e runs it on every map (`--all`) as a report; it never fails the checks (`--strict` makes it exit 1 for local use). Tests: `test_restatement.py`.

The figure and rounding rules live in `claims.py`. The public story builder uses the same module, so essays and evidence registers follow one rule set.

An evidence entry looks like this:

```json
{"id": "EV-HOU-001", "statement": "...", "figures": ["4.2%"],
 "rounded": [{"figure": "0.9%", "value": "0.00873", "scale": 100, "places": 1}],
 "source": "SRC-0001", "anchor": "exact passage", "text_version": "library/text/...md (for PDF or Word sources)",
 "grade": "A", "fact_date": "2025", "checked": "2026-10-28", "recheck": "2027-04-28", "supports": ["HOU-4A.01"]}
```
