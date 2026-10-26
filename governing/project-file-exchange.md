# Project 2050: readable research and cross-agent file exchange

October 24, 2026. Operational protocol; no policy change. The project repository is the common home across Codex, Claude Code and research chats. The [shared instructions](project-instructions.md) govern approval and integration.

## Preferred paths

| Situation | Producer | Receiving agent |
| --- | --- | --- |
| Repository-capable task | Save full Markdown/report text in `sources/`, code and explicit assumptions in the existing tool area; open a focused PR with context | Fetch the exact branch/commit, read actual files, inspect diff and run relevant validation |
| Deep Research or chat cannot write GitHub | Return the full report as UTF-8 `.md` plus original PDF if useful; include data/code and a file manifest for multi-file work | Integrating agent receives actual attached bytes or an authorized Library copy, verifies contents, then opens a repository PR |
| Library source | Give exact filename, stable Library ID and version/date; keep a durable project text copy in GitHub when authorized | Discover the available Library app/skill, resolve the item, read full content with pagination or materialize original bytes using that skill |
| Local file explicitly supplied | Give actual path in the current environment; attach/export to transfer to another environment | Read local bytes directly; do not send a local path to a Library reader or assume another session shares the directory |
| Large/public raw dataset | Record official URL, version, license/access terms, hash and retrieval/reproduction command; retain small aggregate outputs in Git | Retrieve intentionally when needed; verify hash and adapter/schema. Do not commit raw CPS data or infer it is bundled |

Saving a file, linking a preview, creating a native report and committing a repository file are different actions. Temporary `sandbox:` links and absolute local paths are session artifacts, not durable cross-session locators. A ZIP link inside another chat may not expose its bytes here. Native Library IDs are Library-tool inputs, not public download URLs or filesystem paths. Other agents may have no Library connector at all; the repository text is their default reading route.

## Producer completion contract

For substantive research, put a short context block at the start of the report or in its existing integration note: task/policy IDs; source branch/full commit; date; draft/completed/merged status; what is new and superseded; adopted policy versus alternatives/research assumptions; source URLs and page/table locations; missing access; tests and next decision. Reuse an existing report/register rather than require a new directory of paperwork for a small task.

The report body must be complete text, not a summary pointing to inaccessible attachments. Resolve session-only citation tokens into bibliographic entries and ordinary source URLs before export where possible. Preserve original reports and caveats; an integration synthesis must say it is a synthesis. PDF remains useful for layout, but provide text alongside it, especially for wide or clipped tables. CSV/JSON tables need units, definitions and provenance. Code packages need entry commands, dependencies, tests, explicit assumptions and a SHA-256 manifest. Do not manually edit generator-owned outputs.

Before reporting completion, verify the file is nonempty and includes its ending/appendices; record page or line coverage and any truncation. For a multi-file package, confirm required files exist and hashes match. A saved item or successful upload does not establish that its parser can read it. Where feasible, read the committed text back by path and SHA before handing it off.

## Receiver recovery order

1. Prefer the supplied actual local attachment when available. Inspect its type/bytes and extract using format-appropriate tools. Read relevant content in full; paginate rather than mistake a capped response for a complete file.
2. For a Library-only source, discover the Library skill and available tools. Resolve by exact filename/ID, check version, then choose one route: full read (continue `has_more`/`next_read`) or materialization for original bytes. Current skill/tool schemas govern; do not hard-code an old connector name or guess an authenticated download endpoint.
3. If the reader returns no content, distinguish metadata access from body access. Try original-byte materialization once when supported. Inspect actual format: a native research export may be JSON whose report is in `widget_state.report_message.content.parts`, even if its title looks like a PDF or Markdown file. Parse and preserve all report parts; source-search snippets are retrieval leads, not additional report text or independently read evidence.
4. If bytes are PDF/DOCX, use extraction; render affected pages for diagrams, scans or clipped tables. OCR may be necessary for scanned pages. State exact missing/clipped content. Never reconstruct a missing ZIP from a report and call it an exact recovery.
5. If recovery fails, stop repeating equivalent failed reads. Record filename/ID/version, readable coverage and the blocked operation. Request an actual `.md`/`.txt` attachment or PDF export only for the missing body; continue independent work. Do not require the user to repeatedly prove they can see the preview.

The October 24 bibliography illustrates the distinction: earlier Library reads failed, but the attached original bytes contained the full 81-entry report in native JSON. The recovered [repository text](../sources/project-2050-annotated-bibliography.md) now makes it available across agents. Its original opaque citation tokens lack a verified token/URL crosswalk; the exported source-search URL index is retained as leads, not invented exact citations. This establishes a successful recovery route for this file, not a diagnosis of every recent attachment error.

## Integration and publication

For parallel agents, follow [the collaboration strategy](project-collaboration.md) and the live queue's owned paths. Include the exact source/head commit, task state, affected policy IDs and proposed common-input delta in the task PR. A data handoff must distinguish current-law levels, new spending, transfers, overlapping estimates, budget authority and outlays, with units and time windows. The shared-model owner reconciles those deltas before regenerating combined outputs. Do not silently promote a source estimate to an adopted input or ask Espen to relay repository files between capable agents. An interrupted session should leave its actual committed/uncommitted state and next step in that same PR.

Research sessions should save to GitHub by default when the available connection supports writing, under the shared standing instruction. Use a task branch, never overwrite current authority or concurrent work. Add links/status to the existing research register and queue where material; do not copy the same report into multiple canonical locations. Review code, assumptions, provenance and policy implications before merge. If scope includes a substantive policy change, put that decision to Espen explicitly.

A Library copy can help reading and distribution but is optional for repository-backed deliverables and must not become a second independently edited canon. Keep private writing samples, credentials, personal records and restricted datasets out of research commits. A stable handoff names repository path, immutable source commit and PR; after merge it also names the actual merge commit. Public-facing products should point to reviewed research and retain its claim limits.
