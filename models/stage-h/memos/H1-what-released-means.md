# Memo H1: What "released" means for a model

Role: decision memo for Espen, stage H step 1 (`../1-audit.md`, part 1 and part 3.5). Status: **provisional, drafted November 25, 2026. Not decided.** Decided on its own, not as a package.

## The question

PLAN 3.4 gives each model a status: exploratory, working or released. Nothing says what earns "released". The audit finds three models near the standard (household, health coverage, energy), three with real gaps (budget, immigration, transportation) and one missing (housing). Staff and researchers will read "released" as a promise of quality. What should the label promise, and do models that aren't there yet ship at all?

## The checklist

Every option uses the same published checklist, recorded criterion by criterion in `models/toolkit.csv` and checked by script where it can be (the Policy Simulation Library's catalog criteria work this way):
1. a license; 2. a version number and changelog; 3. a model card with all seven elements; 4. parameters with sources (evidence IDs) and ranges; 5. a validation table, every benchmark run, every miss explained; 6. one command that runs from a fresh clone with public or documented data; 7. tests in the project's checks; 8. a machine-written run log; 9. the "not an official score" line on every output; 10. a known-issues list; 11. the project's reviewer has tried to break it.

## The options

**A. Released means all eleven criteria are met; models that meet the first ten except review ship too, labeled "preview" (recommended).**
- *For:* a clear bar the project can meet with its own sessions; a reader can see exactly which criterion a preview model misses; nothing usable is hidden. PolicyEngine and the Policy Simulation Library list incubating models the same way.
- *Against:* no outside eye; a model can be "released" and still wrong in a way no agent spotted.
- *What it means now:* household, health coverage and energy can reach "released" in stage H (energy once its engine is licensed, memo H2); the budget model after H4; immigration after H6; transportation after H5. Health coverage's three benchmark misses stay in its validation table.

**B. A, plus a review by an outside expert before "released".**
- *For:* the strongest claim of quality, and what a congressional office would trust most.
- *Against:* agents never contact other people for Espen, so Espen would have to find and ask reviewers; it can't be scheduled from here. Models would sit at "preview" until then.

**C. Only released models ship; the rest stay in the repository, unlisted.**
- *For:* nothing in the toolkit is unfinished. *Against:* the budget and immigration models, the ones most users want, may be absent from the first release.

**D. Ship every model at whatever status it has, labeled only by its card.**
- *For:* everything at once. *Against:* readers skip labels; a wrong number from an exploratory model would be quoted as the project's.

## Recommendation

**A**, with B as a later upgrade Espen can pursue when the plan goes public in 2028. Under any option, every output, page and card says the toolkit never produces official scores or individual benefit determinations (PLAN 3.4).

## Consequences

- **A:** stage H ends with three to six models released and the rest in preview with their missing criteria listed. The reviewer's milestone review (H11) is the release gate.
- **B:** models stay in preview until Espen's outreach succeeds.
- **C:** the first release may hold three models.
- **D:** no gate; the cards carry all the weight.
