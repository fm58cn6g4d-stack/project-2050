# Project 2050: shared working instructions

Updated October 24, 2026. These rules apply across Codex, Claude Code, chats and research sessions. Espen owns policy choices. This file defines workflow, not an alternative policy summary.

## Start and authority

1. Fetch remote state and identify the source branch and full commit. After the October 24 consolidation into `main`, `main` is the integration branch. Verify it contains the consolidation; the former working branch was `claude/pensive-mendel-g1lwl5`, last pre-audit head `dafe93e5144f4a87b65709b9ef0b5990c8f9633b`. A branch name, default checkout or old handoff alone is not evidence of current content.
2. Read [the governing decisions](project-2050-governing-decisions.md), including standing design rules; [the charter](project-charter.md) for purpose/products; and [the shared queue](../sources/project-work-queue.md) for status and ownership. Read the post-pilot directions and task-relevant canonical domains/sources. Reuse verified context within a session; reread when files change, rather than repeatedly loading the entire corpus.
3. Check open PRs and concurrent work before assigning or editing. State the bounded task, expected deliverable and likely changed files. Use a task branch and an isolated worktree/checkout for concurrent writers. Do not overwrite another session's working files.

The approved charter governs goals, products and research standards. Governing decisions and explicitly approved amendments govern selected policy. Canonical domain files implement them. Research, decision briefs, models, source reports and public illustrations have their stated evidentiary roles; placement in `governing/` does not make every recommendation adopted. Under the October 26 standing delegation, the project coworker may decide and revise project elements to better serve the approved goals. Record consequential choices, reasoning, costs and affected inputs explicitly; do not silently replace authority. Espen retains decisions about project goals. Unresolved alternatives with no recommended action remain open.

## One maintained architecture

| Location | Responsibility |
| --- | --- |
| `governing/project-charter.md` | Approved purpose, public/professional products, outcomes, research and review method |
| `governing/project-2050-governing-decisions.md` | D1–D9 and design rules; retain adopted choices until approved revision |
| `governing/project-2050-post-pilot-decisions.md` | Approved development directions and historical review; current tasks live in the queue |
| `domains/` | One canonical design per policy and named alternatives, stable policy IDs. Transportation Draft 2 remains canonical until conversion; Safe Everywhere detail is supporting evidence |
| `index/options-register.md` | Authored options, exclusivity and overlap; check before combining or summing |
| `index/data/inputs/`, `index/tools/` | Authored model inputs and code; assumptions are not observations or policy approvals |
| Generated `index/` products | Rebuild with their documented generators; common runner does not generate every independent research product |
| `sources/` | Research, provenance, component specifications, methods and evidence; generated research reports remain generator-owned |
| `sources/project-work-queue.md` | Single cross-session assignment/status queue, including decisions and evidence gates |
| `frameworks/`, `staging/`, `archive/` | Reasoning and history; not a competing policy canon |

Do not mass-rename historical files or repeatedly append competing status summaries. Update the maintained record and link it from relevant domains/navigation. Pin historical citations to their original commit; use relative repository links for current navigation. File new documents in their role folder, lowercase kebab-case, domain first when applicable.

## Work toward products

The charter calls for a connected public vision/explorer, a governing blueprint with usable professional resources, and focused policy contributions. Order work by the claim, consequential uncertainty, dependency or decision deadline it will resolve. Technical roadmap items are candidates, not an automatic project-wide sequence. One bounded lead assignment at a time; launch another only with a clear independent owner and integration boundary. Research and public prototypes can continue while a distinct cost/legal question remains unresolved.

Completed CMS/DEM pilots and the child-poverty model are foundations to use, not pilots to restart. Poverty PRs #10–13 contain source-year CPS verification and completed conditional agenda experiments. Static 2030/2034 phasing scenarios are not future poverty forecasts or a full-agenda fiscal score. Do not require an elaborate current-law forecast as a prerequisite for using these results. The health component schedule and payment/vehicle comparison remain authorized development; adopted launch dates and financing remain unchanged.

Use [the writing guide](espen-writing-style-guide.md) for substantial drafting on Espen's behalf. It is a dated copy of their saved guide, not their private writing corpus. Retrieve relevant named samples when accessible; disclose access limits. Write plainly, explain mechanisms and uncertainty, and report results without asking Espen to execute routine commands.

## Preserve policy and numerical meaning

- **October 26 standing delegation:** Espen retains authority over project goals and has authorized the project coworker to decide project elements in service of those goals. Exercise judgment on policy instruments, implementation, prioritization and working fiscal choices; document consequential decisions and regenerate affected outputs. Do not infer a change to goals or silently relax D3/D4. A model passing is evidence, not a goal decision. All recommendations in PR #20 and associated materials were accepted, with the latest recommendations superseding earlier conflicting advice; options without a recommended action remain open.
- Tag numbers by basis (sourced/scaled/estimated/proposal), year/window, units and population. Separate observed data, conditional results and intended outcomes. Check current-world factual claims against current primary sources.
- After an approved input change, reconcile affected domain/options/input records and rerun generators. Never hand-edit generated outputs. A documented software/rounding correction may be implemented within an authorized audit; explain its numerical effect and validate that inputs are unchanged.
- Preserve D3/D4 and channel boundaries, no dynamic revenue counted, HI reserve, immediate CAP-7S legal availability versus unpriced FY2029 cash, and overlap controls. Do not claim a clean checker certifies legal, operational or causal validity.
- Do not communicate with other humans on Espen's behalf: no email, messages, records requests or outside submissions. The project-coworker delegation does not authorize such contact. Repository work and the specifically authorized PR #20 merge remain allowed; preparation is not permission to send.

## Research and file exchange

Follow [the file-exchange protocol](project-file-exchange.md). Default for substantive Project 2050 outputs: a repository branch/PR containing readable text, sources, context and reproducible code/data where appropriate. This standing instruction authorizes saving project research drafts for review; it does not authorize policy adoption, disclosure of private material, unrestricted bulk datasets or automatic merging of future work. If GitHub writing is unavailable, return a complete portable package and mark repository integration pending.

Library and attachments are useful source/distribution routes, not synchronization. Do not make Library access a prerequisite for routine repository work when the needed text is already committed. Never equate an empty reader response with an empty document. Confirm actual contents and completeness; preserve page/table limits and original provenance. Do not claim all source publications were read merely because their bibliography is readable.

## Validation and completion

Use [the tools readme](../index/tools/readme.md) for commands/dependencies. Run the common rebuild after relevant changes, and focused tests for touched tools. Child-poverty logic and stored-results checks run separately. A metadata-only task need not redownload large source datasets or rerun every simulation. Use `--fetch` only for an intentional source-vintage update. Inspect every generated diff and the consistency report; explain unresolved findings rather than change assumptions to silence them.

Open a coherent PR with problem/result, source base, changed scope, validation and limitations. Merge only with Espen's authorization; an instruction to perform and merge a bounded consolidation covers that consolidation. Recheck head/base and conflicts before merging, then verify the actual remote merged commit. Never force-push shared history. Do not merge an unrelated old PR because the user said to merge the current assignment.

Finish with a short handoff: outcome, branch/full source and final commit/PR, files or maintained entry points, checks actually run, unresolved decisions/source limits and next concrete action. Distinguish saved locally, committed, PR open and merged. Refresh the shared queue for material progress. Do not create a new general coordination document for every minor task.
