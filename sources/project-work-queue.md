# Project 2050: current work queue

Updated October 26, 2026. Single cross-session assignment/status record, not a second policy canon. Verified main: `55a675f825cbf4c783f94a0ec1b3586d623b15e1` (PRs #24/#35/#36 merged). Fetch again and inspect open PRs before work. This records known activity, not visibility into every chat.

## Current direction and collaboration

Espen accepted the recommendations in PR #20 and associated materials, with the latest controlling conflicts. The project coworker may decide project elements in service of approved goals; Espen retains goal decisions. No communication with other humans on Espen's behalf. [Governing approval](../governing/project-2050-governing-decisions.md#recovery-and-solvency-recommendations-approved-october-26) is authoritative; [collaboration strategy](../governing/project-collaboration.md) sets the parallel workflow.

The substantive priority is the **joint contribution-and-protection settlement**: current-law household data, overlapping taxes and health savings, supported agency costs, and the education care/IDEA boundaries. The accepted mixed education architecture and working spending allocations are in [recovery-adoption.json](../index/data/inputs/recovery-adoption.json). Complete illustrative tax schedules and universal-credit amounts remain unselected. Preserve D3/D4 and visible downside/household failures. Historical ledger CSVs are comparisons, not the complete selected recovery budget.

## Assignments and owned paths

| Work / state | Owner | Deliverable and boundary | Owned paths / integration |
| --- | --- | --- | --- |
| Collaboration refresh — integrated through PR #21 | Codex, this session | Update shared/vendor instructions, remove obsolete launch assignments and prepare Claude re-entry message; no policy/model-number changes | Root entry files, shared instructions/handoff/strategy, this queue and re-entry note; focused PR |
| Joint contribution-and-protection settlement — PR #24 merged; counted-revenue reconciliation merged in PR #38 | Codex | Price coordinated worker/nonworker contribution relief and joint financing; test household, debt and fund effects; resolve educational accounting dependencies | `index/tools/recovery-budget/`, shared fiscal/incidence inputs and outputs, recovery adoption record; integration owner for shared numerical changes |
| Capacity reviews — PRs #22/#23/#25 merged; surge $105B, FY2029 $5B, DEV-P and fund administration integration active on Codex branch | Claude Code | Initial IRS/CMS/HUD/Education budget and workload review; retain/reduce/expand/reserve recommendations within or explicitly challenging $300B surge/$300B sustained; test IRS yield and administration overlaps | `sources/capacity-recovery-budget-review.md`, `sources/capacity-recovery-components.csv`, `index/tools/capacity-review/`; read shared model, return proposed deltas for coordinated integration |
| Agent automation and merge tiers — merged (PR #27, `ff5b602`); Espen completed the GitHub settings and labels on Oct 26 | Claude Code | Tiered merging through the merge gate, PR checks (rebuild, drift, tier, cross-agent review), CODEOWNERS and daily digest. Codex's integration (`chatgpt-codex-connector`) recorded in the merge policy after its first review | `.github/`, `governing/agent-automation-setup.md`; rules in `governing/project-collaboration.md#merging-three-tiers` |
| Public story page and essays — PR #39, ready for Espen's approval; format and tone approved Oct 28 (from `650cade`) | Claude Code | Visual story page carrying seven short essays on major components, with original SVG illustrations, a claim register and tests; reviewable artifact in the repo, not published. Existing front door and its pinned edition unchanged | `index/tools/public-product/story/`, `index/public-2050/story*`, `sources/public-story-*`; no shared model inputs, outputs or governing records |
| Independent challenge — not assigned | Gemini or a fresh reviewer session | Reproduce and challenge a consequential result once there is a concrete package; financial logic/household/baseline errors before editorial suggestions | Review artifact linked to exact source commit; isolated fixes if needed; no third competing fiscal model |

A queue row reserves scope but is not a lock or proof of a running agent. Check branches/PRs, publish an early draft PR for a substantive claim where available, and record acknowledgement/start head. Owners may change; these are temporary assignments, not vendor territories. Keep two substantive authors initially, with bounded independent review as useful. Queue/governing/options edits are coordinated during integration; no two agents should regenerate the common model in a shared checkout.

[Claude re-entry message](claude-code-reentry-2026-10-26.md) gives the update and first assignment. The previous `codex-handoff.md` health assignment is retired. Returning agents must not resurrect it or the historical Claude branch as authority.

## Completed foundations — reuse them

| Work | Current home | Limits / remaining relevant questions |
| --- | --- | --- |
| Consolidation and shared architecture — PRs #1/#14; earlier capacity/calendar/CMS/DEM work | [Shared instructions](../governing/project-instructions.md), [charter](../governing/project-charter.md), [audit](project-2050-consistency-audit-2026-10-24.md) | Main is the integration branch. Completed pilots are foundations, not a request for another exhaustive audit |
| Child poverty — PRs #10–13 | [Analysis](family-child-poverty-agenda-effects.md), [model](../index/tools/child-poverty/README.md) | Source-year CPS and replicate analysis; conditional scenarios are not future/full-agenda forecasts. Reuse validated components rather than rebuild |
| Health — PRs #9/#15–17 | [Selected specification](health-selected-design-specification.md), [component register](health-delivery-component-register.csv), [resource bridge](health-delivery-resource-bridge.md) | Protect rapid restoration and adopted dates. Actual marginal costs remain unpriced; CMS capacity review should use existing work, not repeat the hearing/vision decision packet |
| Family/housing — PR #18 | [Adoption bridge](family-adoption-architecture-bridge.md) | AFA and a million new voucher awards selected; old financing comparisons did not choose a pay-for. PR #20 adds a bounded $135B housing envelope, not a demonstrated additional award count |
| Public platform — PR #19 | [Blueprint](public-product-blueprint.md), [public edition](../index/public-2050/index.html), [build instructions](../index/tools/public-product/README.md) | Retain front door. Its numerical evidence pin predates recovery revisions; no automatic claim refresh or publication |
| Strategy, full education and recovery — PR #20 merged at `3de6bd15af186b4cc4b304310e2e24aa3b52c93c` | [Assessment](recovery-and-solvency-budget.md), [results](../index/recovery-budget.md), [method](../index/tools/recovery-budget/README.md), [148-row inventory](fiscal-recovery-inventory.csv) | Recommendations accepted, latest superseding earlier. Architecture/working allocations selected; exact financing remains unresolved and neither complete illustrative schedule passes D3 |

## Subsequent work, ordered by consequential decisions

After the financing/protection and capacity findings can be integrated, develop the approved **climate portfolio allocation** on common cost/emissions assumptions: public grid delivery, adaptation, workforce, procurement and marginal credits, with bill effects and liabilities. Do not bank unscored savings or start a general rewrite now.

Housing security and all-age care remain accepted development directions. Retain the bounded housing expansion and immediate Medicaid/HCBS improvements while pricing broader promises. Revisit education's current-law care boundary and IDEA ramp within the fiscal settlement; do not open a disconnected trust-fund model. A bounded public example of conflicting needs and remedies can proceed without waiting for every score, but numerical claims require reviewed evidence.

Democracy's existing permission/reach/remedy work and adverse-political-condition comparisons remain available focused tasks when they resolve a live decision. Do not treat the historical backlog as a mandate to start all domains. Post-election D1 rebaselining is triggered after November 3, 2026, not before actual results exist. No model-derived political certainty or outside human contact.

## Integration and recovery

Use one task branch/worktree per author; record source SHA and claimed paths in the PR. Authors return complete artifacts, source references, assumptions, tests, proposed input changes and remaining questions. The shared-model owner reconciles each accepted package against current main and regenerates combined outputs once. Preserve both branches and meanings if conflicts arise. Agents can make element-level decisions under the delegation, but should record tradeoffs and obtain real independent scrutiny when consequential rather than imply unseen approval.

PR #20 is merged; its merge authorization does not authorize every future PR. Follow applicable merge authorization and verify the remote result. Do not merge superseded PR #8 or unrelated historical branches. At interruption, leave the next step and actual committed/uncommitted state in the task PR. At completion, change the task state here; a saved file or an open PR is not a merge.

### Current integration checkpoint, October 26

Codex branch `codex/capacity-integration`, from aa8552d: applies PR #22's $250B IRS allowance, records four-agency allocations inside existing CAP envelopes, adds the $12.2B whole-package PHA fee correction once in recovery housing spending, and retains fixed HOU-4D. Common model rebuilt; 13 financial tests pass. The first joint financing screen is in `sources/financing-protection-initial-screen.md`; six exploratory cases expose the tradeoff between universal credits, middle-income contributions and debt. Next: household cells/current-law tax-benefit evidence and a priced worker/nonworker credit formula. This is active work, not a completed household guarantee. No merge authorization inferred.


October 26 steering: establish the revenue-rebalancing envelope first, then compare sustainable spending packages. Espen reserves the final strategic downsizing decision. PR #23 is open with a proposed capacity surge reduction; Codex has posted a focused scope/accounting review, and its cuts are not adopted. Financing screen now includes zero additional broad/upper-income contribution cases while retaining already-modeled corporate/wealth reforms and dedicated financing; these are starting diagnostics, not completed alternative tax packages.


Maintained financing reading entry: [Revenue rebalancing and a sustainable governing agenda](revenue-rebalancing-and-sustainable-agenda.md). Defines the three revenue cases, six overlap clusters, usable-envelope calculation and three spending-package comparisons. No spending reductions selected.


Current checkpoint: PRs #23/#25 integrated; $105B surge/$5B FY2029 advance, DEV-P, leave administration and SSA/SMI routing implemented with explicit proxies and Medicare split sensitivities. See `sources/capacity-round-two-integration.md`. `sources/spending-package-comparisons.md` reports twelve central/adverse package/financing cases. Cuts remain exploratory. Next: current-law corporate/capital-revenue reconciliation and household/service effects of larger permanent redesigns.

## Current review and financing boundary

PR #24 merged at `55a675f`; its capacity/fund integration and net climate comparison are available. PR #37 merged at `a82a015` with the $150 carbon-price integration and Espen's O5/CLI-7C decisions; PR #40 clarified the pricing report. The [climate handoff](codex-handoff-climate-financing-2026-10-26.md) identifies the remaining coordinated Package A/O5/CLI-7C ledger and recovery integration. PR #38 merged the [counted-revenue reconciliation](revenue-counted-reconciliation.md); its current-vintage bridge lowers the same GF receipt subset from $8.115T to $8.005T through CX alone. Its subsequent research recommendation is a joint current-law corporate score for G1/G5/G7 and corporate C38 components. Preserve pending integration boundaries and Espen's final strategic downsizing decisions.

## Ongoing Codex participation

As requested October 26, **Project 2050 coworker** is enabled with hourly polling outside GitHub. Setup is confirmed; the first unattended execution remains to be verified. See [setup](../governing/agent-automation-setup.md#ongoing-agent-work-separate-from-automatic-merging) for scope, failure handling and pause controls. Inbox priority: authored-PR feedback/checks, explicit or ownership-required reviews, other ready peer reviews, then one bounded authorized queue task. PR #34's review/override and main-update rules are merged. PR #36 is merged: recurring Codex runs cannot approve one another’s authored work. Follow current main’s gate rules.
