# Public-product prototype

Internal review edition, October 24, 2026. Source `main`: `3594c784b35651ee34fc7661274219bf82f3adcb`. Product proposal and implementation; no adopted policy, date or model input changes. Read the full [blueprint](../../../sources/public-product-blueprint.md) and [three treatments](../../public-2050/directions.html).

## View it

Open `index/public-2050/index.html` directly in a modern browser. It is self-contained, works offline, and links to `directions.html` and `manifest.json` in the same directory. Download those three files together from the task branch; GitHub's normal HTML view displays source rather than running the page. Professional evidence links use the pinned source commit and may require repository access. No local filesystem or Library link is required to read the scene and its limitations.

For a local HTTP preview, from the repository root:

```bash
python3 -m http.server 8765 --bind 127.0.0.1 --directory index/public-2050
```

Then open `http://127.0.0.1:8765/` on the **same machine**. A cloud workspace loopback address is not a desktop preview URL. No public or tunnel endpoint was created. Stop the server with Ctrl-C.

Browser screenshots are [desktop](../../public-2050/review-desktop.png), [mobile](../../public-2050/review-mobile.png) and [directions](../../public-2050/review-directions.png). They are review captures, not authoritative model outputs. The HTML is the working interaction.

## Build and checks

Requires Python 3.9+ and Git; no package installation for the artifact. No source download or model simulation occurs in this publisher.

```bash
python3 index/tools/public-product/build.py
python3 index/tools/public-product/build.py --check
python3 index/tools/public-product/test_build.py
```

The Python publisher reads `content.json`, CSS, the SVG illustration, navigation JavaScript and the direction template. It emits `index/public-2050/index.html`, `directions.html` and `manifest.json`; do not hand-edit these products. It reads the FY2040 DEC `gf_primary` field from the existing fiscal CSV, where positive values are deficits in nominal $B. It reads the three `adopted_cases` from the existing family comparison JSON. It does not add effects, interpolate cases, rephase costs or compute personal benefits.

Source evidence bytes must match `content.json`'s immutable commit. When a source changes, review the public claims and model semantics, set the new source commit explicitly and rebuild. The manifest records SHA-256 hashes for the referenced sources, publisher files and generated HTML. The enclosing release Git commit identifies editorial content; the source commit identifies the policy/evidence snapshot. The manifest excludes itself to avoid a circular hash.

Optional browser QA requires Playwright resolvable by Node, an installed Chromium and the loopback server above. It reads only that server, aborts HTTPS requests and saves screenshots under ignored `build/public-product-review/`. Set `PUBLIC_PRODUCT_BROWSER` to a different Chromium executable when necessary. The managed browser blocked `file:` navigation, so this pass verified HTTP rendering; direct-file opening is supported by the self-contained artifact but was not verified in this browser.

```bash
node index/tools/public-product/browser-check.cjs
```

The check covers all six navigation paths and evidence disclosures, keyboard activation/focus, browser back, deep links, mobile reflow, reduced-motion operation and the no-JavaScript fallback. It also checks all three direction treatments. The Python checks cover pinned-source drift rejection, numeric export fidelity, source/local link targets, unique IDs and manifest integrity. These protect against materially misleading output, not merely markup style.

After a reviewed visual change, copy the new browser captures to the three `review-*.png` paths in the public directory. Screenshots are not part of the initial page load. Their hashes are recorded in `review-sha256.txt`; regenerate it with the included screenshot names, never a wildcard that includes the manifest itself.

## Validation record for this pass

- Common `bash index/tools/run-all.sh` completed; all 21 compared generated products reproduced unchanged. Existing consistency findings: zero stale live headlines, four unknown IDs, one ledger-ID finding, four ledger/domain reconciliation findings and two table findings. These are pre-existing and do not certify legal, causal or operational validity.
- The new Python boundary tests and deterministic `--check` passed.
- Chromium browser checks passed at 1440px desktop and 320/390/768px reflow widths; desktop/mobile/direction screenshots were visually inspected. All six chapters and evidence paths work; no page JavaScript errors were observed.
- The current opening HTML is below the proposed 200 KB uncompressed budget, with no external runtime assets. No throttled performance score, screen-reader session, human comprehension study, Safari/Firefox check or WCAG conformance certification is claimed.
- A source-link target check verifies repository files at the pinned edition. Anonymous access to private repository evidence is not verified and must be addressed with public professional summaries before publication.
- Existing poverty aggregate outputs were reused. No raw microdata download or national rerun was needed; no new scientific result is asserted.
- Fifteen existing family-comparison tests passed, as did the stored eight-case/42-sensitivity agenda checks. These validate reuse boundaries; the historical stored cases do not become current adopted-package forecasts.

## Review boundaries

The map and related links are navigation. Scenes are fiction. The poverty table is a supported conditional comparison. The fiscal number is an existing working-model output. There are no numerical sliders or live calculations, personal data, accounts, analytics or deployment configuration. Full model compatibility and a comprehensive claims registry are proposed architecture, not implemented features.

The host recommendation is in the blueprint; no host was provisioned. In this environment an attempt to serve the repository on all network interfaces was rejected by automatic approval review. The safer loopback server served only the prototype directory and succeeded. That restriction does not block the deliverable; the screenshots and self-contained files provide the review path.
