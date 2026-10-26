# Project 2050

A fair shot at a good life, and the democratic capacity to build it. Project 2050 connects a public vision through 2050 to a governing blueprint: policies, evidence, resources, legal routes, delivery and reproducible analysis.

## Start here

After the October 24 consolidation, **`main` is the integration branch**. Fetch and verify the live head; the former working branch `claude/pensive-mendel-g1lwl5` is historical, not a second canon. The consolidation incorporates its completed work through PR #13 and the architecture audit. Do not select an old uploaded snapshot merely because its title says “current.”

1. [Approved charter](governing/project-charter.md): purpose, public/professional deliverables, research standards and review.
2. [Governing decisions](governing/project-2050-governing-decisions.md): adopted D1–D9 and design rules.
3. [Shared instructions](governing/project-instructions.md): source roles, approvals, Git workflow and completion.
4. [Current work queue](sources/project-work-queue.md): completed work, next assignments and decision/evidence gates.
5. [Codex handoff](governing/codex-handoff.md): opening instructions and first bounded task.

`AGENTS.md`, `CLAUDE.md` and `GEMINI.md` point agents to the same guidance. Chats and research sessions remain useful; substantive results return through reviewed repository changes. [File exchange](governing/project-file-exchange.md) explains reliable text export, Library recovery and cross-agent handoffs.

## Find the work

| Area | Maintained home |
| --- | --- |
| Policy designs | `domains/domain-*.md`; [options and overlaps](index/options-register.md). Transportation Draft 2 remains canonical |
| Evidence and source access | [Research register](sources/project-2050-research-register.md), [complete annotated bibliography](sources/project-2050-annotated-bibliography.md) and domain sources |
| Health delivery | [2029 restoration component register](sources/health-delivery-component-register.csv), [research reconciliation](sources/health-delivery-resource-bridge.md), [hearing/vision decision packet](sources/health-hearing-vision-decision-packet.md) |
| Child poverty | [Completed conditional agenda analysis](sources/family-child-poverty-agenda-effects.md), [interactive results](index/child-poverty-agenda-analysis.html), [model and reproduction](index/tools/child-poverty/README.md) |
| Democracy | [Post-pilot review packet](sources/democracy-post-pilot-review-packet.md), [approved directions](governing/project-2050-post-pilot-decisions.md) and canonical democracy file |
| Legislative calendar | [Scenario analysis](index/calendar-scenarios.md), [explorer](index/calendar-scenario-explorer.html), [delivery opportunities](index/calendar-delivery-opportunities.md); 172/163 is legacy provenance |
| Fiscal recovery and full education adoption | [Recommendations](sources/fiscal-recovery-and-education-redesign.md), [integrated selected-scope model](index/fiscal-recovery-model.md), [all-row inventory](sources/fiscal-recovery-inventory.csv). Full EDU-9B scope/payroll institution adopted; rates and other reforms conditional |
| Pre-education fiscal comparison/resources | [Ledger](index/2029-trifecta-master-ledger.md), [D3 household incidence](index/revenue-household-incidence-model.md), [D4 fiscal paths](index/fiscal-long-term-model.md), [funds](index/dedicated-funds.md), [surge limits](index/capacity-funding-model.md) |
| Validation and unresolved findings | [Generated consistency report](index/check-report.md), [October 24 audit](sources/project-2050-consistency-audit-2026-10-24.md), [tools commands](index/tools/readme.md) |
| Reasoning/history | `frameworks/` informs inquiry; `staging/` and `archive/` do not set current policy |

## Validate and rebuild

Python 3.9+ and Node.js are required for the common suite; use Python 3.12+ for the recorded poverty environment. No Python third-party package is needed for these runners.

```bash
bash index/tools/run-all.sh          # common suite; build/ and diff, no overwrite
bash index/tools/run-all.sh --write  # regenerate committed common products
python3 index/tools/child-poverty/run_validation.py
python3 index/tools/child-poverty/check_agenda_results.py --results index/tools/child-poverty/empirical/agenda-results.json
```

The poverty suite is independent of the fiscal/incidence suite. Official-data reruns require the separately retrieved CPS archive; the stored aggregate checker does not redownload or reexecute it. Use the documented report generator for poverty text/HTML; never hand-edit generated products. The [tools roadmap](index/tools/roadmap.md) describes capabilities and gaps, not a mandatory project-wide development order.

A reproducible run does not establish policy validity. Child-poverty results are conditional static agenda experiments, not future poverty forecasts or a full-project score. Health acceleration remains under development with the adopted fallback. FY2029 surge cash and legal eligibility remain unresolved. No synthetic result, contract ceiling or assumed delivery rate becomes an empirical estimate by filing it here.

The public edition is pinned to its earlier evidence vintage. Education adoption and the new fiscal review have not been released into that edition; do not present its old fiscal headline as the new integrated result.
