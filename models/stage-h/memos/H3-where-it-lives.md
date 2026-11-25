# Memo H3: Where the toolkit and the site live

Role: decision memo for Espen, stage H step 1 (`../1-audit.md`, part 3.4). Status: **provisional, drafted November 25, 2026. Not decided.** Decided on its own, not as a package. The lead recommends keeping the site's code in this repository for now, and Espen has turned off the Lovable, Wix and AnimatedWebs connectors; every option below keeps the code here.

## The question

Stage H ends with a toolkit and a site that someone can find. Where should each live, and in what form? Nothing is published until Espen approves it (H11).

## The options

**A. Both in this repository; the site on GitHub Pages (recommended).**
- The toolkit is the `models/` folders with the register, cards and a tagged release (for example `toolkit-v0.1`) that anyone can download. The site is built from `public/site/` by a GitHub Action and served at the repository's GitHub Pages address; a custom domain can be added later.
- Packaging inside A: each release attaches a toolkit-only archive built by the Action, and a small `pyproject.toml` lets anyone install the models with one `pip install` from the tag (no package index, no second repository).
- *For:* no new account or service; the repository stays the only source of truth; every published page traces to a commit. *Against:* GitHub Pages offers less control over headers and redirects than a dedicated host; the toolkit sits inside a large repository full of dossier work.

**B. The toolkit in its own repository; the site on GitHub Pages.**
- A second repository holds only the released models, copied from this one at each release.
- *For:* a clean, small download that looks like a professional product. *Against:* two copies to keep in step; a copy can drift from the models the dossiers actually use. A's release archive gives the same clean download without the drift.

**C. Both in this repository; the site on a static host such as Cloudflare Pages.**
- The October blueprint's recommendation (`legacy/sources/public-product-blueprint.md`, "Hosting and release maintenance"): built by GitHub Actions, served with a CDN, deploy history and rollback.
- *For:* the most control and the best performance. *Against:* Espen has to create and own an account; one more service to manage.

**D. Private claude.ai pages only, until the plan goes public in 2028.**
- The site is published as private artifacts that Espen can share by link.
- *For:* nothing is public before Espen chooses. *Against:* no public address; artifacts are copies, not built from the repository, and are not a home for a toolkit.

## Recommendation

**A**, using private claude.ai artifacts for review copies before anything goes public. Move to C if a custom domain needs features GitHub Pages lacks.

## Consequences

- **A:** H11 adds a Pages workflow (a `.github/` change, tier 3) and a release tag.
- **B:** H11 also creates the second repository (Espen creates it; agents never create repositories outside this one).
- **C:** Espen creates the host account; H11 adds its deploy workflow.
- **D:** H11 publishes artifacts and records their links on the board.
