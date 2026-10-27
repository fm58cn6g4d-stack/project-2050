# Public story page: seven illustrated essays

October 27, 2026 · Claude Code, PR #39 on `claude/public-story-essays`. Evidence snapshot: `main` at `650cadec751c8897401120d96852aff4f334a2b1`. Working edition for editorial review; not published or deployed. Editorial rationale, the essay set and the decisions for Espen are in [the editorial note](../../../../sources/public-story-essays.md).

## What it is

`index/public-2050/story.html` sits beside the existing front door (“A day in a possible 2050”) and its analysis companion. It carries seven essays, each with an original illustration labeled as an imagined scene, numbered evidence notes, a “what this essay does not claim” box and its policies named by purpose. Four explanatory figures (an award-to-home flow, a delivery chain with its remedy loop, the fiscal rule, and the long arc to 2050) are HTML so they reflow and read as text; one chart (the Climate Dividend per adult) is drawn from its anchored data with a table view.

It is a separate page with its own builder because the existing edition is deliberately pinned to an October 25 evidence snapshot and its builder stops when cited sources change. The essays need current figures (the $150 carbon price, O5, CLI-7C, the resized capacity surge). Advancing the front door’s pin is a separate editorial review. Both pages share the palette and voice; neither rewrites the other.

## Files

| File | Role |
| --- | --- |
| `essays.json` | Essays, reading key, plain policy names with canonical IDs and markers, the claim register and the claims deliberately left out |
| `art/*.svg` | Six original scene illustrations (static, self-contained) |
| `art/*.html` | Four explanatory figures |
| `story.css` | Page styles; light palette shared with the front door |
| `build_story.py` | Validates claims and builds the outputs |
| `anchors.lock.json` | Generated: line of every cited passage in the pinned commit |
| `test_story.py` | Claim-tracing, structure and editorial-boundary tests |
| `story-browser-check.cjs` | Optional Chromium check at 320, 390, 768 and 1440 px |

Generated outputs, never edited by hand: `index/public-2050/story.html`, `index/public-2050/story-claims.json`, `sources/public-story-claim-register.md` and `anchors.lock.json`.

## How claims are kept honest

Every claim in `essays.json` names one or more repository passages by exact text (`anchor`). The builder:

- fails if a passage is no longer in its file, or a policy marker is missing;
- fails if a paragraph, limits box, caption or figure shows a number that none of its cited claims carries, or if a claim lists a figure that is not in its own passages (rounded model shares are recomputed from the raw value);
- fails if a claim is unused, a policy ID is unknown, or a title, dek or illustration contains a number;
- links each note to its passage at the pinned commit, with the line number from `anchors.lock.json`.

The only number allowed without a claim is 2050, the project’s name. External facts are recorded with the repository passage that carries them and, where re-verified for this edition, the external URL and check date.

## Build, check and review

```bash
python3 index/tools/public-product/story/build_story.py            # build
python3 index/tools/public-product/story/build_story.py --check    # verify outputs and every claim
python3 index/tools/public-product/story/test_story.py
python3 -m http.server 8765 --bind 127.0.0.1 --directory index/public-2050   # then, in another shell:
node index/tools/public-product/story/story-browser-check.cjs
```

The common runner (`index/tools/run-all.sh`, step 8d) runs `--report` and the tests in report mode. It fails only if the story’s own content changed without a rebuild. If another change moves or rewrites a cited passage, it prints `REVIEW public story claims` with the claim IDs and the page stays as it was. That is a signal for editorial review, not a failure of the other change.

To move to newer evidence: `build_story.py --review-ref origin/main` lists changed sources and the claims that cite them. Reread those claims against the new passages, edit `essays.json`, set `source_commit` to the new full SHA, rebuild (with that commit fetched, so the lock can be refreshed) and run the tests and browser check.

## Validation record (October 27)

- `test_story.py`: 16 tests pass (one skipped in report mode).
- `build_story.py --check` passes; the page is about 143 KB of HTML/CSS/SVG with no scripts or external requests.
- Browser check passes at 320, 390, 768 and 1440 px: no horizontal scroll, skip link first and working, contents and note links land on their targets, chart table opens from the keyboard, body text at least 16 px, no console errors. Desktop and phone captures were inspected.
- Text and background color pairs computed at 5.25:1 or higher (WCAG AA).
- No screen-reader session, Safari/Firefox check, throttled performance test or human comprehension review is claimed.
