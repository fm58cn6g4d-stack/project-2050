# Public story page: essay set, editorial choices and decisions

**Context.** Claude Code, October 27, 2026, at Espen’s request for a new visual story page with short essays on the project’s components. Source: `main` at `650cadec751c8897401120d96852aff4f334a2b1` (PR #37 and PR #38 merged). Branch `claude/public-story-essays`, PR #39. Status: draft for editorial review; not published or deployed. No shared model inputs, outputs, governing records or adopted policy changed. This note is a synthesis of repository policy for public presentation, not a new policy decision.

**Review entry points:** [the page](../index/public-2050/story.html) (open in a browser), [build and checks](../index/tools/public-product/story/README.md), [claim register](public-story-claim-register.md), [essay text and claims](../index/tools/public-product/story/essays.json).

## What was built

Seven essays of about 560–670 words each (about 4,300 words in all), on one page with a reading order, six original illustrations labeled as imagined scenes, four explanatory figures and one chart. Each essay makes an argument, names its policies by purpose, links every consequential claim to a numbered evidence note, and ends with what it does not claim. Canonical policy IDs live in data attributes and the register, not the reading text.

| # | Essay | Argument in one line | Principle (blueprint) |
| --- | --- | --- | --- |
| 1 | A floor you can stand on | Income, care, leave and coverage should hold on a bad week, independent of work or family form; home care is the weakest part | A society that cares |
| 2 | A home you can keep | An award is not a home; assistance, supply and repair have to work as one program, and waiting-list luck should end | Freedom you can use |
| 3 | Work that leaves room for a life | Bargaining power, a livable floor and support after any job loss, without making work the price of a decent life | Freedom you can use |
| 4 | Cleaner power, and preparing for what is coming | Price, dividend, standards and grid together; the plan does not yet meet its own 2035 benchmark; preparation without promising safety | Responsibility across generations |
| 5 | Power that answers to people | Reforms judged by whether we would accept them from opponents; the court-expansion trigger was removed for that reason | Power that answers to people |
| 6 | A government that can deliver | Capacity is a precondition, sized from evidence (the surge was cut when priced), with remedies when delivery fails | Power that answers to people |
| 7 | Paying for it honestly | A written fiscal rule, a fairness test the plan does not yet pass, and the long arc to 2050 | Responsibility across generations |

## Research-brief format (pilot, October 27)

Espen asked that the essays work as persuasive research products: make the reader see a problem a particular way, then present and defend a solution. Essay 2 is rewritten as the pilot, titled “End the housing lottery” (about 1,600 words). Its structure is:

1. A thesis in the dek.
2. “The argument in brief”: four numbered claims.
3. The problem reframed (“A lottery, not a program”).
4. Where the problem is worst (“The shortage is at the bottom”).
5. The evidence that the remedy works (the randomized Family Options Study).
6. A pull quote.
7. A three-step proposal, with a figure.
8. Four objections, each stated in its strongest form and answered, including the evidence that cuts against the proposal (lease-up failure and a modest work effect).
9. “What would change our minds.”
10. A short conclusion.

It uses the project voice (“we”). New external evidence (NLIHC 2026, CBPP 2022, the Family Options Study) is quoted and dated in [the housing evidence record](public-story-housing-evidence.md), and the claim register now labels research results as “Research finding”. The builder supports both formats, so the remaining six essays can be converted one at a time once Espen approves the pilot.

The brief argues for the housing-security guarantee, a direction the project accepted for development on October 26. It presents the guarantee as the destination and the funded million awards and $135B as the first stage. It states that the guarantee is not priced and gives no cost figure for it.

## Why this set

- **Charter.** The “public vision and explorer” product calls for narrative chapters or essays, maps and household examples with visible assumptions. The October 25 strategic assessment recommended “a small number of substantial, illustrated essays linked to public evidence casebooks before building a larger personalized explorer.” Seven essays sit inside the requested five to eight.
- **Blueprint order.** Principles, then goals, then connected policy choices, then the democratic work of making them real. Essays 1–4 carry the goals and policies; 5–6 carry the democratic and delivery work; 7 carries the honest account of cost and time. Every essay is tagged with one of the blueprint’s four principles.
- **Coverage.** The set covers the six community stories of the front door (home, care, climate, work, commons, connections) and adds capacity and financing, which the October 26 decisions made central (resized surge, IRS enforcement, remedies duty, revenue-first rebalancing). Transportation, education beyond care, immigration, civil rights and national security are not given their own essays; they are better served later than thinly now.
- **Difficult tradeoffs in public.** The October 26 acceptance asked for a public narrative showing tradeoffs and practical remedies. Each essay names a cost or a loser (families who wait for care places; renters without awards; the home-care wage cost; buyouts; slower partisan payoff; the fourth income fifth).

## Choices made under the delegation

- **A separate page rather than extending the front door’s build.** The existing edition is pinned to an October 25 snapshot and its builder intentionally stops on any source change; refreshing it requires reviewing all of its public copy. The essays needed current figures, so they have their own builder with the same palette and editorial rules, and the front door is untouched. The new page links to the front door and the analysis companion; they do not yet link back.
- **Stricter claim discipline than the front door.** Every number on the page must be carried by a claim whose exact source passage is found at build time; rounding from raw model values is recomputed. This makes it hard to publish a stale or invented figure by accident.
- **Diagrams as HTML, not fixed SVG,** so they reflow at phone width and read as text to assistive technology.
- **First person used sparingly** (“I think”), matching the writing guide’s note that it is natural when the genre calls for it. Espen may prefer the project voice (“we”) throughout; that is a one-line edit per instance.

## Claims deliberately left out

Recorded in `essays.json` (`left_out`) and the register. In brief: no fully-financed claim; no “middle-income households come out ahead”; no FY2040 gap or debt-path numbers (they rest on unselected illustrative schedules and, for the recovery budget, a climate package not yet integrated); no “climate action makes this place safe”; no dates presented as receipt dates; no summed program costs; no political forecasts; no figures from the authored stress-test narrative.

Two inclusions go further than the October 25 blueprint’s public emphasis and are for Espen to confirm: the paying essay states that the central case does **not** pass the fairness test (fourth fifth about −$2,906 in FY2039) and that the downside case does not stabilize debt. Both are stated as limits, not as the gap figure the blueprint keeps in the companion.

## Editorial direction from Espen (October 27–28)

- **Format: approved.** The housing research brief is the model: “this is moving in the right direction for sure.” The other essays and future public-facing content move toward it.
- **Tone:** persuasive, compelling and forthright, but optimistic. The essays should inspire readers that the project has developed strategies to achieve real gains for people.
- **Sequencing:** close out this edition first, then convert the remaining six essays as part of the research-foundation restructuring (`research/RESTRUCTURING-PLAN.md` on branch `claude/research-intake`). That way each brief rests on a domain evidence register rather than on summaries.

## State of this edition and open questions

This edition merges with the housing brief in the new format and the other six essays in the earlier format, clearly a working edition. Still open for Espen, with no change needed to merge:

1. **Voice:** the brief uses the project “we”; the older essays keep occasional “I think.” Converting them settles this.
2. **Candor about financing:** the paying essay states that the plan does not yet pass its own fairness test. That fits “forthright,” but the conversion should frame it around the strategy for closing the gap.
3. **Front door:** link it to the essays now (requires advancing its evidence pin and reviewing its copy), or wait for the next edition.
4. **Publication:** nothing is published. Any public hosting needs Espen’s explicit approval.

## Limits

Essay prose follows the saved writing guide; Espen’s original writing samples were not accessible in this session. External facts were taken from repository passages; two (the 2026 Social Security Trustees figures and the NLIHC voucher count) were re-verified against their primary sources on October 27. No human comprehension test, screen-reader session or cross-browser check has been done. Model results remain conditional and are labeled as such at the point of use.
