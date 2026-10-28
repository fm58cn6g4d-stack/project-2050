# Library

Role: originals and their text versions, the catalog and the name index. Status: catalog seeded October 28, 2026; text versions of the non-text originals come with the dossiers that need them.

| File | What | Edited by |
| --- | --- | --- |
| `catalog.csv` | One row per document in `legacy/`, `library/intake/` and `library/text/`, plus citation rows for sources the repository cites but does not hold: `SRC-` ID, path, title, kind, origin, rights, status, aliases, `copy_of`, note. `copy_of` marks an original upload that duplicates a working copy in `legacy/`, so its names lead to that one home | Hand (new files are appended by the script) |
| `catalog-facts.csv` | Size, SHA-256, first commit and last content change (following renames) | Script only |
| `name-index.md` | Every name a document has gone by (title, file name, alias, staging row, Bill Book chapter) and its one home | Script only |
| `text/` | Verbatim text versions of public U.S. government documents and openly licensed (Creative Commons) documents, made by `fetch_public.py` with the source address, retrieval date and the original's SHA-256 in a header. Evidence entries anchor to these | Script only |
| `intake/2026-10-28/` | Espen's October 28 uploads, unchanged, with `manifest.json` checksums | Never (originals) |

`python3 library/build_catalog.py` appends rows for new files and rebuilds the generated files. `--check` fails when a file is uncatalogued, a catalogued path is gone, the name index is stale, or a title or alias leads to two homes (file names may repeat). Stale file facts only print a note.

To add a name, add it to the row's `aliases` column (semicolon-separated) and rerun the script.

**Rights.** The repository is public. Any credible source can be used, government or not; the rights decide how.
- **Public domain** (U.S. government works): saved in full with `fetch_public.py URL SLUG "Publisher"`.
- **Openly licensed** (a Creative Commons license the publisher states on the work, as many research institutes and open-access journals do): saved in full with `fetch_public.py URL SLUG "Publisher" --rights "CC BY 4.0"`, naming the license.
- **Licensed, paywalled or all rights reserved** (most journal articles, books, news, and think-tank reports without an open license): never committed. Add a citation row to `catalog.csv` by hand: a new `SRC-` ID, the source's address (URL or `https://doi.org/...`) as `path`, kind `citation (not saved)`, the title, the publisher and year as `origin`, and the rights as stated (for example, `licensed (journal)`). Evidence entries quote it briefly: each anchor is a quotation of at most 60 words, with a `locator` (page, section or table). The checker still traces every figure to the quotation; the reviewer checks the quotation against the original.
- When Espen has access to a licensed source the agent cannot reach, Espen can upload it for reading; the upload stays out of the repository and only the citation row and short quotations go in. The POLITICO Pro article from the October 28 intake is recorded only by checksum in the intake manifest.
- `permitting-reform-summary-1.pdf` is the Senate Energy and Natural Resources Committee's public one-pager, identified from its page-1 header.
