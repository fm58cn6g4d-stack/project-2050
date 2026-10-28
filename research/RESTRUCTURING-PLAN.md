# Project 2050: restructuring plan

October 28, 2026 · Second draft, revised after a critical review. Proposal for Espen's approval, not yet adopted. Claude Code, branch `claude/research-intake`.

## The problem

Project 2050 produced deep research early on: the war-game set, the climate and carbon sessions, the transportation and rail work, the health memo analysis and the ChatGPT pilots. Most of it reached the repository only as conclusions. The domain files cite it by nickname ("Bill Book 12", "the map", "the durability session"), often with no file behind the name. Most domain files carry 0–10 source links. Several recent fiscal and climate reports carry none, because they build on model outputs rather than evidence. Each new layer of work drew on the last summary, so detail thinned out with every pass. The canonical files have also grown by appending dated updates ("October 26 integration update…"). Reading one now means reconstructing its history to find the current position.

The fix is structural. Research should be stored so it can be called up. Policy should be chosen and recorded on the evidence. Proposals should be written as legislative and executive provisions that tie back to that research. Models should then validate those proposals and illustrate their likely outcomes. Public content should sit on top and cite all of it.

## The target: four layers

| Layer | What it holds | Every item must |
| --- | --- | --- |
| **1. Research** | Original sources and data; research notes and analysis; evidence registers of the claims the project relies on | Carry provenance (author, date, URL or original file, checksum, version, access rights). Each claim has an ID, an exact quoted passage, an evidence grade and a check date |
| **2. Proposals** | Per policy area: a decision record (problem, options weighed, choice and reasons) and the provisions that implement it. Legislative vehicles and executive actions assemble provisions across areas | Rest on evidence IDs for their reasons. State status: selected, alternative or historical. State what would change the decision |
| **3. Models** | Fiscal, distributional, poverty, carbon, transportation and calendar models; their inputs and recorded runs | Validate and illustrate proposals; never serve as the reason a policy was chosen. Trace inputs to evidence IDs or labeled assumptions. Record which provision versions each run tested, and list what the model leaves out |
| **4. Public content** | Research briefs and essays, the illustrated vision and the analysis companion | Cite only evidence IDs, proposals and model runs. The story-page claim register already works this way |

Proposals sit below models in this table on purpose. Models test proposals that research has already justified. `governing/` stays above all four: goals, adopted decisions and working rules.

## Principles

1. **Build on what exists.** Nothing is thrown away. Earlier work is catalogued and labeled current, superseded, historical or raw.
2. **One home for each thing.** Every document gets one catalog entry listing every name it has gone by, so a nickname always leads to a file.
3. **Current position first, history separate.** A canonical file states what is decided now. Dated updates, superseded numbers and the reasoning behind changes move to a decision log, so readers don't have to reconstruct the history.
4. **Claims cite evidence, not summaries.** A figure in a proposal or essay cites an evidence ID with an exact passage, never "per the Bill Book." The story page's automatic anchor check proves this works, and the same check extends to the evidence registers.
5. **Research chooses policy; models validate and illustrate it.** A policy is chosen on the evidence, the project's goals and design judgment, and its decision record says so. Models come afterward. They check that a proposal is sound and affordable, show its likely outcomes, and expose weak spots, tradeoffs and failure cases. A model result can prompt a second look, but it is never by itself the reason to adopt or drop a policy, because models inherently miss things. Every model carries a plain list of what it leaves out, and models are not a source of facts about the world.
6. **Public language follows the same order.** Public content argues from the evidence and the project's values, and uses model results to illustrate what a policy would do. "Our analysis is that…" and "our research shows…" are fine. Wording that makes a model the reason ("the model chose…", "optimized by our model…") is not. Model figures always appear with their conditions and limits.
7. **Register what carries weight, not everything.** Evidence registers cover the claims that decisions, provisions and public content actually rely on, and they grow as work needs them. An exhaustive catalogue of every fact would never finish.
8. **Move as little as possible.** New layers get new folders. Existing paths that tools and checks depend on, chiefly `index/`, stay where they are. A file moves only when its new home is clearly better, with links updated by script and checks kept green.

## Structure

```
research/
  catalog.csv              one row per document: id, title, aliases, path, layer, area, version, supersedes, status, provenance, rights
  intake/<date>/           raw uploads, unchanged (2026-10-28 is filed)
  library/<area>/          originals worth keeping, as readable text where possible, each with a source card
  notes/<area>/            analysis and session findings (most of today's sources/ reports, moved area by area)
  evidence/<area>.json     claim register, validated by script; a readable page is generated from it
proposals/
  <area>/decision.md       the decision record: problem, evidence, options weighed, choice, reasons, what would change it
  <area>/provisions.json   provision IDs, text or specification, status, evidence IDs, model runs
  <area>/decision-log.md   dated history moved out of the canonical text
  vehicles/<vehicle>.md    bills and reconciliation vehicles (R1, R2, Moving America…) assembled from provision IDs
  executive/<id>.md        executive actions, same fields as provisions
index/                     unchanged: model tools, inputs, outputs and the public edition; each model gains an evidence map, run log and limits list
domains/                   kept until an area's pass is done; then becomes a short pointer to proposals/<area>/
governing/                 unchanged
```

**Evidence register entries** use one schema: id, statement, figures, source (catalog id plus exact anchor passage), evidence grade, date of the fact, date checked, re-check due date, and the provision IDs it supports. The re-check date is needed because facts like program counts or budget levels go stale.

**Evidence grades:**
- A: official data or primary law;
- B: experimental or peer-reviewed research;
- C: credible secondary analysis;
- D: project estimate;
- E: assumption.

**Access rights:** public-domain and openly licensed material can be stored in full. Copyrighted or paywalled material, such as a POLITICO Pro article, is kept as a citation with short quotations if the repository might ever become public. Public builds ship only quotations.

## How the work proceeds

**Phase 0: preserve the uploads (done).** The three archives are filed unchanged in `research/intake/2026-10-28/`, with a checksum manifest. Public PDFs and CBO data are recorded by checksum only. This is about one session's work, already finished.

**Phase 1: catalog, name index and interim rules (1–2 sessions).**
- Catalog every document in the repository and the intake: what it is, all its names, current version, what it supersedes, area, layer, status and rights.
- Produce the name index that resolves every nickname, and a duplicate and conflict report. Known cases: PROJECT 2029 copies, two carbon-fee baselines, the Thriving map in two formats.
- Flag places where a model output is treated as the reason for a choice.
- Propose small **interim working rules** in a separate tier-3 PR, so new work stops thinning out while the restructuring runs:
  - cite a file or source, never a nickname;
  - read an area's research before writing about it;
  - keep model results as validation, not as reasons.

  A check that flags unresolved nicknames goes in alongside.
- No files move.

**Phase 2: outcomes framework (short; Espen decides).** Write down the outcomes the charter commits to, such as income security, housing stability, health access, emissions and democratic participation, with how each is measured. These are goal-level choices, so they are Espen's to approve. They give every later validation the same yardstick.

**Phase 3: pilot area end to end, housing (2–3 sessions).** Housing is small and already has a research brief and partial evidence. The new material includes its main original, Bill Book 12. The pilot does each of the following:
1. Build the housing evidence register from the originals and primary sources.
2. Write the decision record: the problem, options weighed (the million awards, the guarantee, a cash alternative), the choice and reasons, and what would change it.
3. Restate the domain file as current position only, with history moved to the decision log.
4. Specify the provisions with IDs, and show how they assemble into the vehicles they ride.
5. Validate with the poverty and cost models, with recorded runs and limits lists.
6. Rebuild the public brief on that base.

Housing provisions ride shared vehicles such as R2, so the pilot also tests the vehicle structure. The templates are fixed from what the pilot teaches before roll-out.

**Phase 4: area by area, with validation inside each pass (1–3 sessions per area; about 20–30 sessions in all).** Suggested order, set by how much new material is waiting and how live the decisions are:
1. climate: the SEEC report, permitting, the FEMA Act, carbon models, the durability work. Several current choices were justified by model comparisons, so this pass restates their reasons from evidence;
2. health;
3. family and education;
4. labor and AI;
5. democracy, integrity and courts;
6. capacity;
7. revenue and fiscal, coordinated with Codex as the fiscal integration owner;
8. transportation, which is closest to the target already;
9. the rest.

Each area is done when it meets the definition below. Files move into the new folders for that area only, after the merge-policy paths for those folders are approved.

**Phase 5: permanent rules and checks (tier 3, Espen approves).** These replace the interim rules once the pilot shows what works:
- the reading order for agents;
- evidence-ID citations required for new factual claims;
- automatic checks for unresolved nicknames, unsupported figures and stale re-check dates;
- merge-policy path rules for the new folders.

The path rules go in **before** the first area's files move, alongside the pilot if needed.

**Phase 6: public content (alongside phase 4).** Each area's essay or brief is rewritten when its pass finishes, in the persuasive, forthright and optimistic tone Espen set. The front door is refreshed once enough areas are done.

## Definition of done for an area

- [ ] Every claim its decision record, provisions and public content rely on has an evidence ID with an exact, automatically checked passage.
- [ ] No unresolved nicknames remain.
- [ ] A decision record states the problem, the options weighed, the choice, the reasons from evidence, and what would change it.
- [ ] The canonical text states the current position only; history is in the decision log.
- [ ] Provisions have IDs, status, and the vehicles they ride.
- [ ] Model validation runs are recorded against provision versions, with each model's limits stated. No model result is presented as the reason for a choice.
- [ ] The public brief cites only evidence IDs, provisions and model runs, and passes the story builder's checks.

## Coordination, review and limits

- **Agents.** Codex owns the shared fiscal model and keeps working during the restructuring. Areas are claimed one at a time in the queue, and fiscal paths are not moved while integration runs. The plan itself goes to Codex for comment, since it changes how both agents work.
- **Review capacity.** Every tier 1–2 PR needs a second agent's review. Codex is out of review credits for now. Options: another Claude Code session as reviewer, or Espen approving tier-3 PRs directly. Restructuring PRs should be kept small enough to review in one sitting.
- **Ongoing policy work.** Decisions keep being made during the restructuring. Areas not yet converted follow the interim rules. Converted areas follow the new structure.
- **Intake status.** Intake files become citable only after cataloguing. Older plans (PROJECT 2029, the war-game set) are labeled historical, not policy.
- **What this does not do.** It doesn't change goals or adopted decisions, rewrite the models, or publish anything.

## Decisions for Espen

1. **Structure:** approve the four layers and the folder plan, including keeping `index/` in place, or adjust them.
2. **Outcomes framework:** agree to define the outcomes in phase 2 for your approval.
3. **Pilot:** housing (recommended) or another area.
4. **Proposal format:** provisions specified section by section with IDs, and full legislative text only for priority vehicles (recommended), or full text throughout.
5. **Interim rules:** approve the small interim rules PR at the end of phase 1.
6. **Reviewing:** who reviews restructuring PRs while Codex is out of credits: a second Claude session, or you directly.
7. **Pacing:** about 25–35 sessions in all, one phase or area at a time as credits allow. Phase 1 is the right next step either way.
