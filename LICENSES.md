# Licenses

Role: which license covers which files in this repository (memo H2 A, `DEC-2026-11-25-33`; step H2b). Status: current. This is a summary, not legal advice; the license files themselves govern.

| What | License | File |
| --- | --- | --- |
| **Code**: Python, JavaScript, shell scripts, HTML templates and workflows the project wrote, including the Carbon Dividend Model's engine in `models/tools/carbon/` and its copy in `models/tools/energy/engine/` (`DEC-2026-11-25-29`) | Apache License 2.0 | [`LICENSE`](LICENSE) |
| **Writing**: the charter, dossiers, memos, notes, model cards, READMEs and the public site's text | CC BY 4.0 | [`LICENSE-docs`](LICENSE-docs) |
| **Parameter and data files** the project compiled: `parameters.csv` files, input tables in `models/data/inputs/`, generated results and run logs | CC0 1.0 | [`LICENSE-data`](LICENSE-data) |

**Not covered.** Material the project did not write keeps its own terms:
- government texts and data in `library/`, which are generally public domain already;
- quoted passages in `evidence.json` files and elsewhere, which belong to their sources;
- data from CBO, Census and other publishers.

Licensed or paywalled material is never committed (`library/README.md`).

**How to cite.** See [`CITATION.cff`](CITATION.cff).

**Not an official score.** The models are research tools, not official cost estimates or benefit determinations. Each model card says what its model can't answer.
