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

The figure and rounding rules live in `claims.py`. The public story builder uses the same module, so essays and evidence registers follow one rule set.

An evidence entry looks like this:

```json
{"id": "EV-HOU-001", "statement": "...", "figures": ["4.2%"],
 "rounded": [{"figure": "0.9%", "value": "0.00873", "scale": 100, "places": 1}],
 "source": "SRC-0001", "anchor": "exact passage", "text_version": "library/text/...md (for PDF or Word sources)",
 "grade": "A", "fact_date": "2025", "checked": "2026-10-28", "recheck": "2027-04-28", "supports": ["HOU-4A.01"]}
```
