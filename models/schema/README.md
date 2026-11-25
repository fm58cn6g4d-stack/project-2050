# The toolkit's common frame

Role: the conventions every core model follows to meet the toolkit standard (`charter/PLAN.md` 3.4): parameter files, results files, validation tables, versions, the run log and the register. Status: current, set in stage H step H2a (`models/stage-h/1-audit.md`, part 3, row H2a, and part 3.5). The release criteria are provisional until Espen answers memo H1 (`models/stage-h/memos/H1-what-released-means.md`); nothing in the register is "released" or "preview" before then. The models move onto the frame in steps H3 to H6; the health coverage model carries its results header, changelog and run-log stamping already. Standard library only.

| File | What it is |
| --- | --- |
| `models/MODEL-CARD-TEMPLATE.md` | The card every model copies: the standard's seven elements and the headings the check reads |
| `models/schema/parameters.py` | The parameter-file schema, its validator and the card's evidence-table generator |
| `models/schema/results.py` | The results header and the disclaimer line |
| `models/schema/validation.py` | The validation-table convention, used from a model's test code |
| `models/runlog.py` | Builds and stamps the header; records published runs in `models/runs.csv` |
| `models/runs.csv` | The run log: one `RUN-` row per recorded run |
| `models/toolkit.csv`, `models/release-criteria.csv` | The register of model IDs, and the criteria its columns record |
| `models/registry/toolkit_check.py` | Checks the register, the run log, every results header and the version rule |

## Parameter files

Every input a model reads is one row of a CSV parameter file: `id`, `value`, `unit`, `year` (the year the value is for: `2032`, `FY2032`, `CY2032`, a span such as `FY2030-FY2039`, or `none` for a ratio or elasticity with no year), `kind` (`evidence`, a measured or published figure; `assumption`, a judgment; `policy`, a parameter of current law or of a reform), `source` (an `EV-`, `SRC-`, `DEC-` or `ASM-` ID or an https URL for evidence and policy rows; the basis in words for an assumption), `low` and `high` (required for an assumption, its tested range), and `note`. Optional `label`, `group` and `statute` columns are carried along. The card's evidence table is generated from the file (`python3 models/schema/parameters.py FILE --card MODEL-CARD.md`), so the card and the inputs can't disagree. A value that varies by year is one row per year, with ids such as `ptc_pct.2030`; uprating rules stay in code and are named in the card's mechanisms.

## Results files

A JSON results file has a top-level `header` object; a Markdown results file opens with the same block. The header holds the model ID, version, status, commit, the sha256 of every code and input file, units, price basis, year type, baseline vintage, scoring convention and the line "Project 2050 analysis of the evidence: not an official score or a benefit determination", all stamped by `models/runlog.py`, never typed.

- **Reference outputs** (the committed `results.json` and `results.md`, which `run-all.sh` rebuilds and compares byte for byte) carry `commit: null`. A file can't hold the hash of the commit that adds it; the code and input hashes identify the run exactly.
- **Recorded runs** (a figure about to be quoted in a dossier, a booking, a release) run with `--record`: the helper stamps the commit, refuses if the model's code or inputs differ from it, and appends a `RUN-<model>-<date>-<letter>` row to `models/runs.csv` (commit, command, results path and hash, a digest of the inputs). The dossier cites the run ID. Nothing in `run-all.sh` records, so the checks never change tracked files.

## Validation tables

A model's benchmarks are `validation.Benchmark` records in its test code: target (a number or a published range), its source and vintage, the unit, and a tolerance (relative, absolute, or the range itself) fixed in the code before the model figure is filled in. `evaluate()` works out the difference and the pass or miss; `render()` writes the table (target, source and vintage, model, difference, tolerance, result, explanation); `problems()` fails a miss or an in-sample check without an explanation. A miss is a reported result, not a test failure: the test fails on `problems()`, or when the committed table differs from the one the code renders. Tolerances change only with a changelog line that says so.

## Versions

Each model has a version (`MAJOR.MINOR.PATCH`) in its results header and a `CHANGELOG.md` beside its code, newest first, one `## X.Y.Z (date)` entry per version, saying how far the headline results moved.

- **Major:** a change in results (any figure in a results file outside its header) or in the interface (inputs, arguments, the results file's shape).
- **Minor:** a new scenario or parameter that leaves existing results unchanged.
- **Patch:** no change in results (a fix to text, speed or code structure).
- **Before 1.0.0** (no model is released yet), a results or interface change takes a minor version, as semantic versioning allows.

`toolkit_check.py` enforces the mechanical part against the merge base with `origin/main`: a changed results file needs a higher version and a changelog entry for it, and a patch bump may not change anything outside the header. Whether a change is major or minor is the author's call under the rule above, and the reviewer's to check.

## The register and the release criteria

`models/toolkit.csv` has one row per core model ID, with its path, status, owner, card, parameter files, results files and tests, and one column per release criterion. The criteria are the rows of `models/release-criteria.csv` (memo H1's eleven, provisional): to change them, edit that file and the register's columns together, and the check accepts the new set. Each criterion reads `pass`, `partial`, `fail` or `n/a`. For each criterion a script can test (`auto` = yes), the check recomputes it: a recorded `pass` it can't confirm is an error, so the register can understate a model but never overstate it.

## Commands

```bash
python3 models/registry/toolkit_check.py            # the register, the run log, headers, versions (against origin/main)
python3 models/schema/test_schema.py                # the schemas
python3 models/test_runlog.py                       # the run-log helper
python3 models/registry/test_toolkit_check.py       # the check
python3 models/schema/parameters.py FILE [--map old=new] [--table] [--card CARD]
python3 models/schema/results.py FILE...            # validate results headers
python3 models/tools/health-coverage/model.py --out build/hc --record   # a recorded run
```
