# Project 2050: consistency audit and workflow consolidation

October 24, 2026. Espen authorized a repository consistency/conforming audit, updated guidance, consolidation/merge and a Codex handoff. This is an operational and computational audit, not a new official score, comprehensive legal review or policy adoption.

## Baseline and branch reconciliation

The verified source is `claude/pensive-mendel-g1lwl5` at `dafe93e5144f4a87b65709b9ef0b5990c8f9633b`. Child-poverty PRs #10–13 are merged, as is health PR #9. GitHub still defaulted to `main` at the October 20 import, `9dbfaa0139d6b0981a12dcbc5307481cbaa86c14`, 52 commits behind the working head. This mismatch made default checkouts and unqualified file links especially likely to serve stale work.

All 17 remote branches and all 13 PR records were checked. Fourteen branches are ancestors of the working head; one is the head itself. Two diverge: the superseded poverty prototype and the old shared-authority branch. The latter's seven commits contain the earlier authority/entry-point/model-guidance work already represented by merged PR #2 and later guidance. Its history is not a reason to replace current files. No unrelated branch is merged or deleted. PR #8 remains untouched/unmerged under Espen's earlier instruction; exact surviving prototype code is already preserved in the rebuilt model.

The consolidation path is a focused audit PR into the former working branch, followed by the existing PR #1 into `main`, with PR #1's stale title/body rewritten to describe the full consolidated project. After verified promotion, `main` becomes the integration branch; the older branch remains history. This removes the default-checkout trap without rewriting history or relying on a local folder as authority. Final merge SHAs belong in the PRs and completion handoff, rather than a self-referential hash embedded in its own commit.

## Findings and conforming actions

| Finding | Action / maintained home |
| --- | --- |
| Approved charter absent from GitHub; old baseline exports could be mistaken for authority | File the complete supplied approved editorial revision as [project-charter.md](../governing/project-charter.md), with original export hash and historical-state notice. Do not rewrite charter goals or repeat completed pilots |
| Bibliography repeatedly unreadable through prior readers | Recover full report text from the supplied native JSON and file [the complete report](project-2050-annotated-bibliography.md), including exported source-search URL leads and explicit citation-crosswalk limits |
| Critical pilot/follow-up text dependent on Library access | File full reader text for CMS pilot/follow-up, DEM pilot, Title III alternatives and Medicaid-registration transaction; preserve identity, coverage and historical limits in each header. File supplied child-poverty reports 1–3 as original lineage, separate from the completed rebuilt model |
| Governing document embeds another long policy/instruction summary | Remove that duplicate, retain the actual D1–D9 and standing rules, and point to charter/shared guidance. Mark completed surge-availability and fund-module work as complete |
| Shared guidance says all `index/` is generated, understates dependencies and treats roadmaps as a fixed order | Distinguish authored tools/inputs from generated reports, common versus independent runners, Python/Node dependencies and external dashboard deployment |
| Append-only status records describe different moments as current | Put current reading/status map at the front of the research register; mark post-pilot and model-brief next steps as historical. Use one [work queue](project-work-queue.md) with completed foundations, bounded next outputs and gates |
| Local/Library saves mistaken for cross-session delivery | Adopt [file exchange](../governing/project-file-exchange.md): default full readable research text plus provenance in a task branch/PR; byte recovery, completeness and failure handling; no automatic policy adoption or future merging |
| Agent guidance needs portable entry and completion rules | Update short AGENTS/CLAUDE/GEMINI pointers, shared guidance, readable writing guide and [Codex handoff](../governing/codex-handoff.md). No permanent role assignment by product brand |
| Same unchanged inputs rebuild to different two-place headlines | Correct decimal summation/rounding at the ledger revenue headline and print fiscal calibration at three places; add signed-boundary and input-order regression checks |

## Numerical reconciliation

The recorded general-fund revenue midpoints sum to **5.985T** in decimal arithmetic. Binary accumulation can fall just below or above that boundary, making `round(..., 2)` print 5.98T or 5.99T across summation implementations. This explains the historical 5.12/5.11T gap and 0.26/0.25T remainder differences without a new score or changed source amount.

`inputs.money_sum` now sums decimal representations and rounds once, half away from zero, for the two-place base headline. It prints 5.99T, matching the pre-audit committed headline; the fiscal calibration separately prints 5.985T before headline rounding. The low/high display remains unchanged. This is display precision, not a new revenue assumption or permission to count extra funds. Common fiscal CSV paths, policy inputs and child-poverty code/assumptions/results remain byte-identical to the source commit. The fiscal Markdown calibration sentence and generated consistency report change through the runner.

The revenue audit's earlier totals/ranges are explicitly a historical snapshot; current navigation points to generated results. It is not silently relabeled a new full revenue audit. The substantive HLT-6/GF/HI and joint TS12 scoring issues remain.

## Remaining checker findings and their meaning

The regenerated report has **zero current stale headline figures**, one dated historical headline, four ID flags, one register flag, four ledger/domain extraction flags and two input-table findings. These are retained and explained, not suppressed to manufacture a clean result.

| Flag | Assessment / next action |
| --- | --- |
| COM-02, COM-03 and LAB-04 | Bibliography entry IDs in the approved charter, not policy IDs. The generic policy-ID scanner cannot distinguish this namespace; preserve the approved text |
| FAM-4B | Explicitly retired education option already crosswalked in the education file/options register; not an unimplemented new family policy |
| C22 | Retired minimum-tax option referenced as history of replacement by G11, not an additional live ledger cut |
| FAM-3, CRT-P1, CAP-8, SAF-10 | The checker searches figures on the same lines as IDs and misses component/annual/package context. These flags are not proof of four wrong scores. FAM-3 financing, court/immigration scope, CAP component ownership and SAF annual/one-time totals remain reviewable in their canonical files; do not overwrite inputs with the scanner's “nearest” figures |
| PS1: 0.091 incidence versus 0.09 ledger | Actual precision/scope discrepancy remains; confirm channel components and pass-through before changing either input |
| EDUP: 2.27 incidence versus ED1 2.1 | Held education-fund contribution differs from its check target. Reconcile fund scope, phase-in and overlap with FAM-2 before deciding whether the values should match |
| Dated revenue-audit headline | Retained historical snapshot, with current totals and generated-ledger navigation at the top |

Unpriced FY2029 CAP-7S cash, reconciliation eligibility, embedded HLT/CAP administration, delivery reach, registration permissions, Title III legal review and independent scoring remain real gaps. The checker is advisory and does not certify D3/D4 completeness, delivery readiness or causal validity. No test result resolves those questions by itself.

## Validation performed

- Materialized all 253 source-commit blobs and verified their Git blob hashes before editing, including preservation of CRLF where present. No local preexisting checkout was treated as source authority.
- Ran the complete common rebuild before changes and after the precision/guidance updates. Transportation, calendar, vote/calendar regressions, carbon, dedicated funds, fiscal and surge modules completed. Two new precision tests pass; calendar produces 146 conditional cases and 49 delivery screens, still illustrative.
- Ran the independent poverty validation: **102 tests**, legacy sibling-regression demonstration, raw-ZIP/policy CLI checks and 24 artificial scenario rows pass.
- Checked the committed aggregate agenda results: **eight main cases and 42 sensitivities** pass stored-results accounting/invariant checks. This audit did not redownload or reexecute the official CPS archive; the empirical execution/provenance remains the completed PR #13 record.
- Verified all original numerical input files, existing child-poverty tool files and annual fiscal paths against the source blob hashes; no changes. Verified the approved charter and recovered bibliography report bodies are preserved in full. Checked maintained navigation, whitespace and a second common dry run after generation.

Validation distinguishes successful execution from accepted assumptions. A generated report's source-access statements remain history of its originating session; do not edit them manually merely because this audit later recovered the source.

## Source and coverage limits

The supplied October 21 governing/instruction exports are older than the verified repository; they were not promoted over current decisions. The approved charter is the supplied October 23 editorial/long-range revision, filed intact with a contextual header. The saved writing guide was readable and used; its policy-memo sample was inspected for voice, not used as policy evidence.

The bibliography export contains the report body and source-search records. Original session citation tokens do not provide a verified token-to-URL crosswalk here; the URL index is preserved as retrieval leads, not invented exact attribution. This audit reviews architecture and relevant methods, not the full text or current accuracy of every cited publication. The successful JSON recovery does not diagnose the cause of all recent file-reader errors; preview access, metadata, extracted text and downloadable bytes can succeed or fail separately.

Five pilot/follow-up Library reports were retrieved through their complete reader ranges with `has_more=false`; these are text exports, not byte-identical binary recoveries. Temporary attachment links within original reports remain historical. The CMS workbook/source ZIP, original health PDF, fourth original child-poverty report body and separate administration-talent slate are not copied by this audit. Their existing locators/recovery records or separate ownership remain; do not claim an exhaustive migration of every chat artifact or that every embedded attachment is accessible. Full health findings, limitations and next packet are already integrated. Future work needing an omitted original should follow file exchange, retrieve it and file a readable copy rather than recreate completed research.

## Next action

Open the current repository in Codex and use the handoff's bounded health payment/vehicle and 2029 restoration assignment. Preserve rapid R1, the adopted hearing/vision fallback and component distinctions. Use completed poverty findings for the subsequent charter outcome/design review and a sourced public example. Do not restart pilots, overbuild the future poverty forecast or launch every queue row at once. All substantive policy, eligibility, launch, financing and target choices remain Espen's.
