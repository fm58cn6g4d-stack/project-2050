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

Every input a model reads is one row of a CSV parameter file: `id`, `value` (a finite number, or a label with unit `text`), `unit`, `year` (the year the value is for: `2032`, `FY2032`, `CY2032`, a span such as `FY2030-FY2039`, or `none` for a ratio or elasticity with no year), `kind`, `source`, `low` and `high`, and `note`. The pair (`id`, `year`) is unique, so a value that changes by year is one row per year under the same id, as Tax-Calculator and PolicyEngine key values by year.

- **Kinds:** `evidence` (a measured or published figure: source an `EV-`, `SRC-` or `DEC-` ID or an https URL); `policy` (a parameter of current law, set by statute: same sources; a reform's values belong in the model's scenario or reform files, not here); `calibrated` (fit so the model reproduces a benchmark: source names the `BM-` ID, which is then in-sample); `assumption` (a judgment: the basis in words, an `ASM-` ID where one exists, and a `low` and `high`).
- **Ranges:** `low` and `high` are the tested sensitivity range the model is run across, not a confidence interval.
- **Optional columns:** `locator` (the table, page or section of the source the number is on: one evidence entry often feeds several rows), `price_year` (the dollars a money value is in), `uprating` (`none`, an index name or a parameter id; reserved now, used from step H3), and `label`, `group` and `statute`.

The card's evidence table is generated from the file (`python3 models/schema/parameters.py FILE --card MODEL-CARD.md`), so the card and the inputs can't disagree.

## Results files

A JSON results file has a top-level `header` object; a Markdown results file opens with the same block. The header holds the model ID, version, status, commit, the sha256 of every code and input file, units, price basis, year type, baseline vintage, scoring convention, the scenarios the file holds, a plain statement of uncertainty ("not quantified" is an answer), and the line "Project 2050 analysis of the evidence: not an official score or a benefit determination", all stamped by `models/runlog.py`, never typed. `code` lists every repository file the run executes: the helper refuses a header when an imported repository module is missing from it (the frame itself and test files excepted). JSON results are written with `runlog.write_json`, the one serialization, so hashes can be compared.

- **Reference outputs** (the committed `results.json` and `results.md`, which `run-all.sh` rebuilds and compares byte for byte) carry `commit: null`. A file can't hold the hash of the commit that adds it; the code and input hashes identify the run exactly.
- **Recorded runs** (a figure about to be quoted in a dossier, a booking, a release) run with `--record`: the helper stamps the commit, refuses if the model's code or inputs differ from it, and appends a `RUN-<model>-<date>-<letter>` row to `models/runs.csv` (commit, Python version, command, results path, a digest of the inputs, and the results' hash with commit null, which equals the committed reference output's hash when the recorded run is the committed one, so anyone can check it with `git show <commit>:<path>`). The dossier cites the run ID. The log is append-only, and each row's commit must stay an ancestor of `main` (so PRs that carry `RUN-` rows merge with a merge commit, not a squash). Nothing in `run-all.sh` records, so the checks never change tracked files.

## Validation tables

A model's benchmarks are `validation.Benchmark` records in its test code: target (a number or a published range), its source and vintage, the unit, a tolerance (relative, absolute, or the range itself) and the tolerance's basis (why that band), fixed in the code before the model figure is filled in. `evaluate()` works out the difference, in units and as a share of the target, and the pass or miss; `render()` writes the table (target, source and vintage, model, difference, tolerance and basis, result, explanation) and counts independent and in-sample checks separately, so a calibrated target never inflates the pass count; `problems()` fails a miss or an in-sample check without an explanation, or a tolerance without a basis. A miss is a reported result, not a test failure: the test fails on `problems()`, or when the committed table differs from the one the code renders. Tolerances change only with a changelog line that says so (moving benchmarks into a per-model `benchmarks.csv` that the check compares with the base is the next step, H3).

## Versions

Each model has a version (`MAJOR.MINOR.PATCH`) in its results header and a `CHANGELOG.md` beside its code, newest first, one `## X.Y.Z (date)` entry per version, with a `Results:` line saying how far the headline figures moved ("no figure moved" included).

- **Major:** a change in results (any figure in a results file outside its header) or in the interface (inputs, arguments, the results file's shape).
- **Minor:** a new scenario or parameter that leaves existing results unchanged.
- **Patch:** no change in results (a fix to text, speed or code structure).
- **Before 1.0.0** (no model is released yet), a results or interface change takes a minor version, as semantic versioning allows.

`toolkit_check.py` enforces the mechanical part against the merge base with `origin/main` (`--require-base` in CI, so a shallow clone fails instead of skipping): a changed results file needs a higher version and a changelog entry with a `Results:` line, entries run newest first, and a patch bump may not change any JSON results file outside its header. Any edit to a model's code changes its hash in the header, so it takes at least a patch. Whether a change is major or minor is the author's call under the rule above, and the reviewer's to check.

*Open for the lead:* the professional-practice review proposes the convention Tax-Calculator, PolicyEngine and OG-USA follow instead: major for an interface break or a change of method, minor for results that move (a new baseline vintage, a corrected parameter, a new scenario), patch for no figure moved. With two CBO baselines a year, the rule above would make every model's major number climb twice a year and stop telling users whether their scripts break. Until the lead decides, the rule above (the audit's) stands; before 1.0.0 both rules agree.

## The register and the release criteria

`models/toolkit.csv` has one row per core model ID, with its path, status, owner, card, parameter files, results files, tests and the version the criteria were assessed at (`assessed_version`, which must match the results header), and one column per release criterion. The register's status must match the header's. The criteria are the rows of `models/release-criteria.csv` (memo H1's eleven, provisional): to change them, edit that file and the register's columns together, and the check accepts the new set. Each criterion reads `pass`, `partial`, `fail` or `n/a`. For each criterion a script can test (`auto` = yes), the check recomputes it: a recorded `pass` it can't confirm is an error, so the register can understate a model but never overstate it. A criterion checked by review (`auto` = no) reads `pass` only with a link to the review in `notes`.

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
