# Specification, uncertainty and the whole plan

Role: discussion note for Claude's review, requested by Espen. Status: reflections and proposals, not an amendment to the standards or a new policy decision. Source: Espen and Codex's conversation on November 9, 2026 (Eastern; November 10 UTC), following the housing specification and milestone work through PR #187.

## Espen's reflection

Espen sees the recent housing work as a strength: it supplies detailed policy provisions that the legacy framework lacked. They also see a risk in how agents pursue individual assignments. In their words:

> i agree. in general, i think the process is getting a lot right in the areas the legacy framework was lacking (detailed specification of policy provisions) but sometimes agents are losing sight of the bigger picture and getting bogged down in solving the problem they were given in their particular prompt, when that problem may be better served by being flagged as a complex issue with multiple reasonable outcomes, or as a question deserving further study, instead of trying to generate a specific answer to every question at this juncture. we can make specific policy decisions without knowing all the answers about how a policy will behave; that's part of government and politics

This is a reason to keep uncertainty visible while making decisions, rather than require every uncertainty to be resolved before proceeding. It does not ask agents to stop specifying policy or to hide inconvenient costs and evidence.

## Codex's assessment of progress

The housing work has moved broad commitments toward an implementable specification: who qualifies, what happens when a voucher cannot secure a home, how rural delivery works, how programs interact, and which costs continue after 2039. Espen's willingness to revisit designs has improved their coherence. The simpler eligibility tests, duty to help people find housing, buyer-assistance caps, and rural provisions are examples. The design lens in `DEC-2026-11-09-13` gives those choices a common purpose.

Specification has nevertheless advanced faster than integration and validation. The dossier contains more developed commitments than the adopted budget inputs and completed model runs represent. Some estimates depend on uncertain take-up, household counts, construction timing and costs. Precise prose and tables can make those estimates seem more certain than they are. The [housing milestone review](../dossiers/home/review-milestone.md) helped expose that distinction; finishing a specification is not the same as validating its predictions.

Independent reviews have caught substantive problems, including the USDA direct-loan omission in #158 and inconsistencies in how the FY2029 bridge was recorded across prose and machine-readable provisions in #179. They also reveal a maintenance cost: decisions recur across memos, specifications, cost sections, provision records, the agenda and the board. Rapid changes can leave these copies disagreeing. Serial work on overlapping files and clear canonical homes should reduce repair work.

Espen's correction to dossier-level fiscal gating was valuable. The current [standards](STANDARDS.md), under `DEC-2026-11-10-05`, require honest reporting and plan-wide balancing in the financing settlement. Repeatedly treating an isolated dossier gap as a design failure was prompting decisions at the wrong level. The fiscal rules still apply to the whole plan.

## What needs an answer now?

Codex's proposed distinction is between specifying what government commits to do and predicting everything that will happen because it does it. The first needs enough detail to make a real commitment. The second will retain uncertainty, competing explanations and political judgment.

A bounded assignment can reward producing a specific answer even when a useful result would be an unresolved question. A plausible estimate can become a precise parameter and then appear to be a prerequisite for the policy. More detail does not always improve the decision.

Before extending a research or specification task, ask: **What decision would a different answer change?** If no meaningful decision would change now, record the uncertainty instead of automatically making it a prerequisite for progress. This is a proposed stopping rule, not a reason to ignore a newly discovered legal, delivery or fiscal risk.

| Treatment | When it is useful | What to leave in the record |
| --- | --- | --- |
| Decide now | The answer defines the commitment: eligibility, benefit, authority, responsible agency, rights or protections | The choice, rationale and consequences; real forks remain Espen's decision |
| Use a working assumption | A number is needed for budgeting or comparing options, but is not established knowledge | Its basis, range and the consequences of being wrong; distinguish it from measured evidence |
| Leave an open question | Several outcomes are reasonable and choosing among them would not change today's decision | The alternatives and what future finding would make the question consequential |
| Study during implementation | Pilots, administrative experience or evaluation can answer more than further desk research | A proportionate way to learn and adjust, without inventing a new reporting burden for every uncertainty |

These treatments can coexist. A benefit can be decided while its take-up remains uncertain; the budget can show a central assumption and a cautious case without making either a promise. An uncertainty belongs on the critical path when a plausible alternative would materially change the choice, undermine the stated commitment, or reveal an unaddressed legal or delivery obstacle.

## What reviews should distinguish

Unsupported claims presented as settled, inconsistent commitments, omissions that change the decision, and missing delivery mechanisms are defects. An explicitly bounded uncertainty about behavior is not automatically a defect. It may call for sensitivity analysis, monitoring or later study. A reviewer should explain which decision a requested investigation would inform and whether the issue blocks that decision now.

Political judgment remains necessary. Choosing a policy means judging it worth pursuing with the knowledge available, including reasonable disagreement about its effects. The process should make that judgment informed and accountable without treating certainty as a prerequisite for action. Espen retains goals, real policy forks and final strategic scope decisions.

## Proposed next use

For housing, Codex recommends a defined integration finish line: fold in the decisions, address the milestone's remaining blocking findings under the current standards, seek Espen's authorization for adopted-input changes, run the model, and conduct a focused L3 re-check. Additional research should resolve a consequential finding or be recorded as a later uncertainty. This is a recommendation for the lead's sequencing, not a new assignment or a reopening of paused budget work.

Claude's review should consider whether this note captures the practical problem fairly, whether the stopping rule would help future briefs and reviews, and what—if anything—should later be proposed for the standards or dossier template. Merging this discussion note alone does not adopt those process changes or alter milestone requirements, D3/D4, merge policy, policy commitments or adopted inputs.
