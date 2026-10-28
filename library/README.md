# Library

Role: originals and their text versions, the catalog and the name index. Status: catalog seeded October 28, 2026; text versions of the non-text originals come with the dossiers that need them.

| File | What | Edited by |
| --- | --- | --- |
| `catalog.csv` | One row per document in `legacy/` and `library/intake/`: `SRC-` ID, path, title, kind, origin, rights, status, aliases, note | Hand (new files are appended by the script) |
| `catalog-facts.csv` | Size, SHA-256, first commit and last content change (following renames) | Script only |
| `name-index.md` | Every name a document has gone by (title, file name, alias, staging row, Bill Book chapter) and its one home | Script only |
| `intake/2026-10-28/` | Espen's October 28 uploads, unchanged, with `manifest.json` checksums | Never (originals) |

`python3 library/build_catalog.py` appends rows for new files and rebuilds the generated files. `--check` fails when a file is uncatalogued, a catalogued path is gone or the name index is stale; stale file facts print a note.

To add a name, add it to the row's `aliases` column (semicolon-separated) and rerun the script.

**Rights.** The repository is public.
- Open and public-domain material goes here in full.
- Licensed or paywalled material is cited and briefly quoted, never committed. The POLITICO Pro article from the October 28 intake is recorded only by checksum in the intake manifest.
- `permitting-reform-summary-1.pdf` is the Senate Energy and Natural Resources Committee's public one-pager, identified from its page-1 header.
