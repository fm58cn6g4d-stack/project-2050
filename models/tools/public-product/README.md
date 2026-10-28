# Project 2050: working public edition

October 25, 2026 · Draft PR #19 on `codex/public-product-blueprint`. Source `main`: `3594c784b35651ee34fc7661274219bf82f3adcb`. The expanded edition implements Espen’s direction: principles, goals and connected policy choices in plain language, with democratic movement and long-term accountability. Detailed funding and model discussion lives in the separate analysis companion. No adopted policy, date or model input changed. Read the [blueprint](../../../sources/public-product-blueprint.md).

## Subsequent policy development

The full EDU-9B package/payroll institution has since been adopted and a new [fiscal review](../../../sources/fiscal-recovery-and-education-redesign.md) produced. This edition remains pinned to the earlier evidence snapshot; its fiscal headline is not the integrated new education result. Review affected policy/fiscal copy and source contracts before advancing the pin. No publication or deployment occurred in the fiscal review.

## View it

Download `public/site/` from the task branch and open `index.html` in a modern browser, or run this command from the repository root:

```bash
python3 -m http.server 8765 --bind 127.0.0.1 --directory public/site
```

Open `http://127.0.0.1:8765/` on the **same machine**. A cloud workspace loopback address is not a desktop preview URL. No public or tunnel endpoint was created. Stop the server with Ctrl-C. GitHub’s normal HTML view displays source rather than running the page.

The page works offline, with a JavaScript enhancement for choosing scenes. Follow “The analysis” for the companion. Keep these five generated files together: `index.html`, `analysis.html`, `directions.html`, `public-map.json`, `manifest.json`. Professional source links use the pinned commit and may require repository access; the authored public and analytical explanations do not. The original three design treatments remain available from the companion’s edition notes.

Review captures: [desktop page](../../public-2050/review-desktop.png), [mobile page](../../public-2050/review-mobile.png), [community story](../../public-2050/review-story.png), [analysis entrance](../../public-2050/review-analysis.png) and [three treatments](../../public-2050/review-directions.png). These are screenshots; the HTML provides the working interaction.

## Build and check

Requires Python 3.9+ and Git; the artifact needs no package installation, source download or model simulation.

```bash
python3 models/tools/public-product/build.py
python3 models/tools/public-product/build.py --check
python3 models/tools/public-product/test_build.py
```

The publisher reads `content.json`, `site.html`, CSS, the SVG illustration, navigation JavaScript and the direction template. It generates the five files listed above; do not hand-edit them. The analysis reads FY2040 DEC `gf_primary` and GDP from the existing fiscal CSV, where a positive primary gap is a deficit in nominal $B. It reads three `adopted_cases` from the family comparison JSON. The GDP share is a direct ratio of those same-row fields. It does not add policy effects, interpolate cases, rephase costs or determine personal benefits.

## Keep public wording connected to the analytical project

- `content.json` holds readable public names and prose. Stable scene, step and policy IDs connect that presentation to canonical policies. Rename a public label without renaming its canonical ID.
- Each of the 18 policy explanations has `policy_ids`. The policy dictionary records the canonical path, identifying marker and selected-option reference where needed. These are references, not a second policy definition. Technical IDs are present in HTML data attributes and exported data, not in the public reading text.
- Generated `public-map.json` connects stories, agenda themes and main sections to their source paths and public URLs. The same authored records generate both the public explanations and the companion’s policy references.
- All referenced evidence must match the pinned source commit. A source edit stops the build and names affected records. After fetching main, report what a newer source version would affect:

```bash
python3 models/tools/public-product/build.py --review-ref origin/main
```

The report lists changed sources and affected public URLs. Review the relevant wording, selected-design status and numerical contracts, then explicitly advance `source_commit` and rebuild. The command never changes public copy or adoption decisions. It is a local review tool, not a scheduled GitHub notification service. A future publication workflow should run it in CI against the proposed release sources.

The manifest records SHA-256 hashes for evidence, publisher files and generated products, excluding itself to avoid a circular hash. The release Git commit identifies the editorial edition; `source_commit` identifies the policy/evidence snapshot. The mapping is a practical dependency graph, not a full claims CMS or model compatibility registry. Existing scenario labels remain separate; no global scenario switch is introduced.

## Browser validation

Optional QA requires Playwright resolvable by Node, Chromium and the loopback server above. It reads only that server, aborts HTTPS requests and saves captures under ignored `build/public-product-review/`. Set `PUBLIC_PRODUCT_BROWSER` for another Chromium executable.

```bash
node models/tools/public-product/browser-check.cjs
```

The managed browser blocks `file:` navigation, so this pass verifies HTTP rendering. Direct-file opening is supported by the self-contained artifact but was not verified in this browser.

After a reviewed visual change, copy the five captures (`desktop`, `mobile`, `story`, `analysis`, `directions`) to the matching `review-*.png` paths. Regenerate `review-sha256.txt` using those explicit filenames. Screenshots are separate from the page payload.

## Validation record

- Eight Python publication-boundary tests pass: numerical scope/units, plain public labels, pinned-source drift rejection, affected-story reporting, unknown-policy rejection, full canonical-domain reach, source/local destinations and hash integrity.
- Deterministic regeneration and `--check` pass. Review against live `origin/main` reports no changed evidence; a simulated family-policy change correctly identifies affected stories and the relevant agenda theme.
- Chromium checks pass for four principles, six goal/story paths, 18 policy explanations, seven agenda themes, movement content, companion navigation and numerical disclosures. Keyboard activation/focus, back navigation, deep links, reduced motion, no-JavaScript fallback and both pages at 320/390/768px pass. No JavaScript errors observed. Desktop, mobile, story and companion captures were visually inspected.
- Public HTML remains below 200 KB uncompressed with no external runtime assets. No throttled performance score, screen-reader session, human comprehension study, Safari/Firefox check or WCAG conformance certification is claimed.
- Source destinations exist at the pinned edition. Anonymous access to private repository evidence is not verified; accessible professional summaries/source passages are still required before publication.
- The October 24 baseline validation ran the common toolchain and reproduced all 21 compared products unchanged. It reported zero stale live headlines and existing consistency findings (four unknown IDs, one ledger-ID finding, four ledger/domain findings and two table findings). Fifteen family-comparison tests and stored eight-case/42-sensitivity checks also passed then. The October 25 change touches only this publisher and its product documentation; unchanged model generators were not rerun. No raw microdata or new scientific result is involved.

## Scope and publication

Map points and goals are navigation; scenes are fiction; the companion’s poverty table is a conditional comparison; its fiscal result is a working model output. There are no numerical controls, personal determinations, accounts, behavioral analytics or deployment configuration.

Before publication: focused claim review, accessible supporting evidence, human accessibility/comprehension review and release approval. Resolving the residual fiscal gap is not required to explain the public vision; a fully financed claim would require separate support. More communities, deeper professional features, full scenario reconciliation and operating manuals are later work. The blueprint recommends static hosting; no host was provisioned or deployed.
