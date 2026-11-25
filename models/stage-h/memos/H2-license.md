# Memo H2: The license for the code and the writing

Role: decision memo for Espen, stage H step 1 (`../1-audit.md`, part 1.1). Status: **provisional, drafted November 25, 2026. Not decided.** Decided on its own, not as a package. This memo explains common choices; it is not legal advice.

## The question

The repository is public but has no license file. Without one, people can read the code but have no legal permission to copy, change or reuse it: legislative staff and researchers, the users PLAN 3.4 names, generally can't adopt it. Which license should the project's own code and writing carry?

What a license can't cover: the library's government texts are public domain already, and licensed or paywalled material is never committed (`library/README.md`). Data from CBO, Census and others keeps its own terms. Espen's Carbon Dividend Model (`models/tools/carbon/`, and its modified copy in `models/tools/energy/engine/`) is Espen's own work and is licensed only if Espen says so. **This gates the energy model:** `MOD-energy` runs on that engine, so it can't be released unless Espen licenses the engine on the same terms or keeps it under a separate license that permits reuse.

Norms in this field: the Policy Simulation Library's models (Tax-Calculator, OG-USA) use CC0, a public-domain dedication; PolicyEngine uses AGPL, a strong copyleft; government models such as CBO's are public domain by law.

## The options

**A. Open and permissive: Apache 2.0 for code, CC BY 4.0 for writing (recommended).**
- Anyone may use, change and share, including in their own office's tools, if they credit the project. Apache 2.0 also grants patent rights and is common in government and research software.
- *For:* the widest adoption; credit is kept; CC BY 4.0 is the same license the library already accepts from research institutes. A variant: CC0 for parameter and data files, since attribution on facts hinders reuse.
- *Against:* anyone, including opponents, can reuse the work without sharing their changes.

**B. MIT for code, CC BY 4.0 for writing.**
- Like A but shorter, with no patent clause.
- *For:* the simplest and best known. *Against:* slightly weaker protection for users than A; otherwise the same.

**C. Copyleft: GPL 3.0 for code, CC BY-SA 4.0 for writing.**
- Reusers must release their changes under the same terms.
- *For:* improvements stay public. *Against:* many government offices and firms can't adopt GPL code, which cuts against the toolkit's purpose.

**D. No license for now.**
- *For:* keeps every option open until 2028. *Against:* the toolkit can't be "released" in any useful sense (memo H1); the site's text can't be legally quoted at length.

## Recommendation

**A**, with CC0 for parameter files, and a separate answer from Espen on the Carbon Dividend Model's engine. The license files and a `CITATION.cff` (so others can cite the toolkit) go in their own tier-3 PR.

## Consequences

- **A or B:** H2 adds `LICENSE` (code) and `LICENSE-docs` (writing) and a line in each model card.
- **C:** the same files with copyleft terms; fewer institutional users.
- **D:** H11 publishes without a license and the cards say "all rights reserved".
