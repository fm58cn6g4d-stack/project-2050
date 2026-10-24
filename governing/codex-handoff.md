# Project 2050: Codex and Claude Code handoff

October 24, 2026. Espen requested an audited, consolidated GitHub workflow and authorized its merge. Repository: `fm58cn6g4d-stack/project-2050` (private). Audit source: `claude/pensive-mendel-g1lwl5` at `dafe93e5144f4a87b65709b9ef0b5990c8f9633b`, including merged child-poverty PRs #10–13 and health PR #9.

## Open the project

Use the repository checkout in Codex or Claude Code. Fetch first; after the consolidation is merged, **`main` is the integration branch**. Verify `main` contains this handoff, the charter and PR #13's analysis. The older Claude-named branch is retained as history, not a parallel authority. Record the actual current remote SHA in your opening note. Do not assume another agent's local folder is current or clean, and do not reset it to recover an old handoff baseline.

Read root `AGENTS.md`, [shared instructions](project-instructions.md), [governing decisions](project-2050-governing-decisions.md), [charter](project-charter.md) and [queue](../sources/project-work-queue.md), then the task's relevant files. The short `CLAUDE.md`/`GEMINI.md` point to the same rules. The user need not reproduce the whole project history in each prompt.

Official OpenAI documentation describes repository `AGENTS.md` discovery, including possible overrides and size limits: [Custom instructions with AGENTS.md](https://learn.chatgpt.com/docs/agent-configuration/agents-md), checked October 24. Keep this root entry short and explicitly load linked project guidance; do not assume every chat product automatically follows repository instructions. Tool access, models and account limits vary; verify what is actually available rather than require a particular model name or brand.

## What is ready, and what remains open

- Adopted D1–D9 and subsequent approved directions remain in force. This audit reorganizes operation and corrects display precision; it adopts no new policy, eligibility, launch, cost input or target.
- Child poverty is completed and merged: verified source-year CPS measurement, claimant/tax audit, all 160 replicates, eight conditional agenda cases, 42 sensitivities and 102 logic tests. Use [the report](../sources/family-child-poverty-agenda-effects.md), [interactive analysis](../index/child-poverty-agenda-analysis.html) and model README. Moderate results are about 10.6%/10.3% under the two phasing conventions; these are not predictions for 2030/2034 or the entire agenda's effect. Do not rebuild the model or expand future forecasting by default.
- The completed health research supports component-specific 2029 restoration development and a January-2030 hearing/vision comparison. The existing Original-Medicare payment bridge qualifies the report's early-R1 preference. No acceleration has been selected; retain 2031 hearing/vision, dental from 2033 and HLT-3 in 2031/2032 pending decisions.
- Completed CMS/DEM pilots are reusable foundations. Missing FY2029 cash, incremental CMS/state costs, actual registration permissions/reach, legal review, MA score split and joint revenue interactions remain evidence gaps. A rebuild does not clear them.
- [Audit findings](../sources/project-2050-consistency-audit-2026-10-24.md) explain remaining checker flags and source limits. The approved charter, complete exported bibliography and writing guide now have readable repository copies. Historical source-baseline strings do not direct checkout.

## First substantive assignment

Complete the existing [health hearing/vision packet](../sources/health-hearing-vision-decision-packet.md), with a restoration companion based on the component register. Bound the work to the decision that must precede R1 text freeze:

1. Compare early R1 authority; summer R2 with express MA mid-cycle machinery; summer R2 using the existing Original-Medicare payment bridge and any exact amendments needed; and the adopted 2031 fallback. Separate beneficiary access from incorporation in MA contracts.
2. Specify hearing/vision services, devices, replacement, cost sharing, providers, payment and implementation assumptions. Missing policy choices remain branches/questions rather than new defaults.
3. Build a marginal cost/funding bridge: added CY2030 benefit year, truly additional versus shifted setup, Part B/GF effects, FY2029 CMS cash and CAP/HLT overlaps. Unsupported amounts remain unpriced; do not take one-tenth of the combined dental/hearing/vision score.
4. Carry forward component-level HLT-1/4 2029 prospective dates, case repair/reinstatement and retroactivity, gap operating mechanism and HCBS financing/capacity. Use existing CMS-IMP packages.
5. Return one compact decision brief, updated component table, evidence/legal questions and a clear go/no-go recommendation with confidence and fallback. Identify the statutory, scoring or operational evidence that could change it. Do not delay or jeopardize rapid R1 merely to include acceleration.

Use primary-source research where needed; seek no outside contact. Specialist review remains an identified need, not an opinion already obtained. Update existing packet/source/domain references only as warranted. Stop after this coherent deliverable and validation; do not simultaneously start every queue item.

## Commands and merge workflow

From a clean task checkout, use Python 3.9+ and Node.js; the poverty validation environment recorded Python 3.12.14. Run the relevant commands yourself:

```bash
bash index/tools/run-all.sh
python3 index/tools/child-poverty/run_validation.py
python3 index/tools/child-poverty/check_agenda_results.py --results index/tools/child-poverty/empirical/agenda-results.json
```

The common runner has a dry-run diff and `--write` regeneration. It is independent of empirical poverty execution. Official CPS data are not in Git; reproduction locators/hashes are in the baseline report. A documentation task can validate stored results without claiming a new raw-data run. Read [the tools readme](../index/tools/readme.md) for generator ownership, outputs and additional commands. Inspect generated changes and remaining checker flags before committing.

Make one task branch from current integration head, review the diff, preserve inputs and open a focused PR. Espen's authorization is required to merge future assignments unless already provided for that task. Recheck incoming work/head before integration and verify the actual remote result afterward. Never force-push shared branches or merge the superseded PR #8. Finish with a short handoff and update the shared queue.

## Research chats remain part of the workflow

Use chats/Deep Research for evidence synthesis, policy alternatives and bounded independent questions when useful. Give them source commit, governing/task files and an exact output contract. [File exchange](project-file-exchange.md) makes full Markdown plus provenance the default repository return path. A missing Library text response is an access failure, not proof of an empty report. Materialize original bytes or receive an actual attachment; do not depend on a temporary link from another session. Repository-backed deliverables need no duplicate Library canon.

## Suggested first prompt

> Continue Project 2050 from the current remote integration branch. Read AGENTS.md and governing/codex-handoff.md, verify branch/head and open PRs, and report any incoming work before editing. Complete only the bounded health payment/vehicle and 2029 restoration packet specified in that handoff. Reuse completed pilots and research; preserve adopted policy and model inputs. Keep unpriced costs and source/legal limits explicit. Use a task branch, validate and prepare one coherent PR with a short handoff. Do not merge without my authorization, send emails or records requests, or start the other queued workstreams.
