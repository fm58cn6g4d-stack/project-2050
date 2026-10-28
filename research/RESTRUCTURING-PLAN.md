# Project 2050: restructuring plan

October 28, 2026 · Third draft. Proposal for Espen's approval, not yet adopted. Claude Code, branch `claude/research-intake`. It supersedes the earlier drafts on this branch.

## 1. What this plan is for

Project 2050 should work like a serious research project. Its policies should rest on evidence that anyone can call up and check. They should be written as legislative and executive provisions. They should be tested by models that express that evidence and that professionals can use. They should be explained to the public in persuasive, forthright and optimistic terms that never claim more than the evidence supports.

**Success, concretely.** At the end of this plan:
1. any number or factual claim in a decision, provision, model input or public text leads, by an ID, to the exact passage it rests on, and a script checks that it still does;
2. every nickname for a document leads to a file;
3. each policy area has one readable statement of what is decided now, the reasons, and what would change the decision, with its history kept separately;
4. the project's main models carry model cards, benchmarks and run logs good enough for outside professionals to use;
5. the public essays and the front door are rebuilt on that base.

**Not in scope.** This plan does not change goals or adopted decisions, rewrite models from scratch, or publish anything. Policy changes found along the way go through the usual decision routes.

## 2. What went wrong, briefly

The early research is deep: the war-game set and Bill Book, the climate and carbon sessions, the transportation and rail work, the health memo analysis, the ChatGPT pilots and the SEEC report. But most of it reached the repository only as conclusions. Domain files cite it by nickname, often with no file behind the name. Most carry 0–10 source links. Several recent fiscal and climate reports carry none, because they build on model outputs. Each pass drew on the last summary, so detail thinned out. Canonical files also grew by appending dated updates, so finding the current position means reading the history.

The October 28 uploads supply most of the missing originals. The problem now is organization and process, not missing material.

## 3. The design

### Four layers

| Layer | What it holds | What every item must do |
| --- | --- | --- |
| **1. Research** | Original sources and data, research notes and analysis, and evidence registers of the claims the project relies on | Carry provenance: author, date, URL or original file, checksum, version and access rights. Each registered claim has an ID, an exact quoted passage, an evidence grade and check dates |
| **2. Decisions and proposals** | For each policy area, a decision record and the provisions that implement it. Bills and other vehicles are assembled from provisions in the existing ledger | Rest on evidence IDs for their reasons. Cite the governing decision that adopted them. State status (selected, alternative or historical) and what would change the decision |
| **3. Models and analytical toolkit** | Fiscal, distributional, poverty, carbon, transportation, calendar and vote models, their inputs and recorded runs, and documentation that lets outside professionals run, inspect and adapt them | Express the evidence. Every input and key mechanism traces to evidence IDs, or is a labeled assumption with a tested range. Record which provision versions each run tested. State what the model leaves out. Meet the toolkit standard (section 6) |
| **4. Public and organizing content** | Research briefs and essays, the illustrated vision, the analysis companion, and organizing and accountability material | Cite only evidence IDs, provisions and model runs, through a claim register like the essay page's |

`governing/` sits above all four. It holds the goals, the charter, Espen's adopted decisions and the working rules.

**Which layer serves which charter product:**
- **Public vision and organizing:** layer 4.
- **Governing blueprint and professional resources:** layers 1–3.
- **Focused policy contributions:** drawn from all four as each area matures.

### Authority: no second canon

The project's rules forbid competing policy canons, and this design keeps to that:

| What | Where | Who decides it |
| --- | --- | --- |
| Goals, the charter, adopted decisions (D1–D9, dated approvals) | `governing/` | Espen |
| Design choices under the standing delegation, and the reasons for all choices | Area decision records | Agents, recorded and reviewable; goal conflicts go to Espen |
| Policy IDs and options | Existing domain files and `index/options-register.md` | Stay authoritative. They are restated, not replaced |
| Which provisions ride which vehicle, and their costs | Existing ledger inputs (`index/data/inputs/ledger-*.csv`) | Already canonical. Provisions link to ledger rows rather than duplicating them |

A decision record explains and cites. It never adopts anything by itself. Its reasoning follows the charter's existing format for decision reviews: current wording and source; purpose; original basis and assumptions; new findings; strengths, weaknesses and confidence.

### Principles

1. **Build on what exists.** Nothing is thrown away. Everything is catalogued and labeled current, superseded, historical or raw. Existing structures are extended, not duplicated: policy IDs, the options register, the ledger, the story builder's claim checks.
2. **One home for each thing.** Every document has one catalog entry listing every name it has gone by.
3. **Current position first, history separate.** A canonical text states what is decided now. Dated updates and superseded numbers move to a decision log.
4. **Claims cite evidence, not summaries.** A figure cites an evidence ID with an exact passage, and a script checks the passage is still there. The essay page has shown this works.
5. **Models express the evidence, and inform decisions only as far as they do.** Models are often part of the reasoning: comparing options, sizing a program, finding where a design fails. That is legitimate when:
   - the model's inputs cite evidence;
   - its mechanisms rest on documented research;
   - thin evidence is represented by labeled assumptions with ranges;
   - its omissions are stated.

   A model result carries the weight of the evidence beneath it, no more. A decision record that relies on one names that evidence and weighs what the model misses. A result built on untraced assumptions, or one that conflicts with stronger direct evidence, is a reason to look harder, not a basis for a decision.
6. **Public language presents models as analysis of evidence.** "Our analysis is that…" and "our research shows…" are the right register. Avoid wording that presents a model as an independent authority. Model figures appear with their conditions and limits.
7. **Register what carries weight.** Evidence registers cover the claims that decisions, provisions, models and public content rely on, and grow as work needs them. The charter warns that a comprehensive register could become an administrative task in itself.
8. **The toolkit is a product.** The models are built to a standard outside professionals can rely on: legislative and committee staff, budget and policy analysts, researchers, advocates.
9. **Move as little as possible.** New layers get new folders. Paths that tools and checks depend on, chiefly `index/`, stay where they are.
10. **Prove that restructuring changes nothing it shouldn't.** When a canonical file is restated, a script compares every number and policy ID before and after. Anything not carried over must appear in the decision log or be flagged.

## 4. The data model

Every record has a stable ID, and one checker verifies the links between records.

| Record | ID form | Lives in | Authored or generated |
| --- | --- | --- | --- |
| Source | `SRC-0001` | `research/catalog.csv`: authored fields (aliases, status, area, rights, notes) in `catalog-authored.csv`; facts (path, size, checksum, first and last commit) generated | Both, kept in separate files so they don't conflict |
| Evidence claim | `EV-HOU-001` | `research/evidence/<area>.json` | Authored; readable page generated |
| Outcome | `OUT-01` | `governing/outcomes-record.md` (the charter's "small outcomes record") | Authored; Espen approves |
| Policy and option | Existing, e.g. `HOU-4`, `HOU-4A` | Domain files, options register | Existing |
| Provision | `HOU-4A.01` (option ID plus number) | `proposals/<area>/provisions.json` | Authored |
| Vehicle and ledger row | Existing, e.g. `R2`, row `HOU-1` | `index/data/inputs/ledger-*.csv` | Existing; gains a provision crosswalk |
| Decision record | `DR-HOU` | `proposals/<area>/decision.md` | Authored |
| Model | `MOD-fiscal`, `MOD-poverty`… | `index/tools/<model>/MODEL-CARD.md` | Authored |
| Model run | `RUN-poverty-2026-11-02-a` | `index/tools/<model>/runs.json` | Generated by the model |
| Public claim | e.g. `share-served` | Each public builder's claim register | Authored, as on the essay page |

**Evidence entries** record:
- the statement;
- its figures;
- the source ID and the exact anchor passage;
- the evidence grade (A official data or primary law; B experimental or peer-reviewed research; C credible secondary analysis; D project estimate; E assumption);
- the date of the fact, the date checked, and a re-check date for facts that go stale;
- the provisions, outcomes and model inputs it supports.

**The checker.** The registry checker (`index/tools/registry/`) generalizes the essay builder's proven logic to all records. It verifies:
- every ID resolves;
- every anchor passage exists in its source;
- every figure in authored text belongs to a cited claim;
- rounded figures follow from raw values;
- re-check dates aren't past due.

Like the essay builder, it fails on content errors and only reports when a cited source moves.

**Originals.** Each original kept in the library has a source card and, where possible, a text version: PDFs via `pdftotext`, Word and Excel via Python, HTML via text extraction. Anchors are checked against the text version, with the original's checksum recorded.

**Access rights.** Public-domain and openly licensed material is stored in full. Copyrighted or paywalled material, such as the POLITICO Pro article in the intake, is reduced to citations and short quotations before anything leaves the private repository. Public builds ship only quotations.

## 5. File layout

```
research/
  catalog.csv, catalog-authored.csv   every document (section 4)
  name-index.md                       generated: every alias to its file
  intake/2026-10-28/                  raw uploads, unchanged (filed)
  library/<area>/                     originals kept, with source cards and text versions
  notes/<area>/                       analysis and session findings, moved area by area from sources/
  evidence/<area>.json                evidence registers
proposals/
  <area>/decision.md                  decision record
  <area>/provisions.json              provisions
  <area>/decision-log.md              dated history moved out of canonical text
governing/outcomes-record.md          outcomes (Espen approves)
index/                                unchanged: models, inputs, outputs, public editions
  tools/registry/                     the registry checker
  tools/<model>/MODEL-CARD.md, runs.json
domains/                              stays authoritative for policy IDs; each file is restated to current position only, linking to its decision record
```

Domain files keep their paths and their role as the home of policy IDs, so the merge rules for `domains/` still apply. That avoids the riskiest move. Only `sources/` research reports move, area by area, into `research/notes/`, after the merge-policy paths for `research/` and `proposals/` are approved.

## 6. The toolkit standard

Each model the project relies on or offers professionals carries:
- **a model card:**
  - the question it answers, and the questions it cannot;
  - its evidence map, linking each input to an evidence ID or to a labeled assumption with a range;
  - key mechanisms and their research basis;
  - known limits;
  - its status: exploratory, working or released;
  - who owns it;
- **benchmarks:** comparison with official or independent estimates where they exist, with differences explained. The sources are CBO, the Joint Committee on Taxation, SSA's actuaries, the Treasury, the Tax Policy Center, the Energy Information Administration and the Census Bureau's poverty measure;
- **a stable interface:** documented inputs, outputs and scenarios, runnable from one command with public or documented data, and no hidden manual steps;
- **tests:** accounting identities, boundary cases, and reproduction of published project results;
- **a run log:** each published result linked to the model version, inputs and provision versions it used.

The toolkit never claims to produce official scores or individual benefit determinations. Some current tools are one-off report generators. The catalog marks which tools are toolkit models; the rest stay as they are, documented.

## 7. How work proceeds

### Session protocol

Each working session, whether Claude, Codex or another agent, should run the same way:
1. Read this plan and the progress board (`research/PROGRESS.md`): which phase, which area, what's done, what's next.
2. Claim the area or task in the queue.
3. Work in one area. Keep each PR small enough to review in one sitting.
4. Run the registry checker and the common checks.
5. Update the progress board with what was done, what's next, and open questions.
6. End with a PR.

Nothing depends on memory between sessions. The repository is the only state.

### The area pass

The same steps for each policy area:
1. **Inventory.** List the area's documents from the catalog, its nicknames, its models, its open options and its public content.
2. **Evidence.** Build the evidence register for the claims that carry weight, from the originals and primary sources. Re-verify time-sensitive facts.
3. **Decision record.** For each major choice in the area, record:
   - the problem;
   - the evidence;
   - the options weighed;
   - the governing decision that adopted the choice, if one did;
   - the reasons;
   - the role any model played and what it misses;
   - what would change the decision.
4. **Restate the domain file.** State the current position only, and move history to the decision log. A script proves no number or policy ID was lost.
5. **Provisions.** Specify provisions with IDs under their options, and link them to ledger rows and vehicles.
6. **Models.** Bring the area's models up to the toolkit standard. Use them to compare and validate. Record runs.
7. **Public content.** Rebuild the area's brief in the research-brief format and tone.
8. **Check against the definition of done.**

**Definition of done for an area:**
- [ ] Every load-bearing claim has an evidence ID with an anchored, checked passage.
- [ ] No unresolved nicknames remain.
- [ ] A decision record covers each major choice, citing governing decisions and evidence, with the role and limits of any model stated.
- [ ] The domain file states the current position. History is in the decision log, and the restatement check passes.
- [ ] Provisions have IDs, status and ledger links.
- [ ] Each model the area relies on meets the toolkit standard, or the reason it doesn't is recorded.
- [ ] The public brief passes its claim checks.
- [ ] The registry checker and common checks pass.

### After an area is converted

New facts enter the evidence register first. Changed decisions update the decision record, citing the governing approval where one is needed. Provisions and ledger rows follow, then a recorded model run, then the public text. Re-check dates surface stale facts automatically.

## 8. Phases, effort and order

A "session" means one focused working session of the kind in this conversation. The estimates assume one agent working at a time.

| Phase | Work | Output | Sessions |
| --- | --- | --- | --- |
| **0. Preserve** (done) | File the uploads with checksums | `research/intake/2026-10-28/` | done |
| **0b. Land the plan** | PR merging the intake and this plan into main, so every session can see them; marked `needs-espen` | Merged plan and intake | under 1 |
| **1. Catalog** | Catalog every document (about 170 outside `index/`, plus `index/` reports and 95 intake files) using scripts plus per-file judgment; name index; duplicate and conflict report; list of model results that decisions rely on without traced evidence; progress board | `research/catalog*.csv`, `name-index.md`, `PROGRESS.md` | 2 |
| **1b. Interim rules** | Small tier-3 PR: agents must cite files, not nicknames; read an area's research before writing about it; trace model inputs to evidence or label them as assumptions. Add a nickname check | Approved rules and check | under 1 |
| **2. Outcomes record** | Draft the charter's small outcomes record: outcomes, measures, baselines | `governing/outcomes-record.md` for Espen | 1 |
| **3. Registry checker** | Generalize the essay builder's checks to all records; add the restatement check; propose merge-policy paths for `research/` and `proposals/` (tier 3) | `index/tools/registry/` | 1–2 |
| **4. Housing pilot** | Full area pass on housing; set the templates (source card, evidence entry, decision record, provisions file, model card) | Housing done; templates fixed | 2–3 |
| **5. Area passes** | In order:<br>1. climate (3)<br>2. health (2–3)<br>3. family and education (2)<br>4. labor and AI (2)<br>5. democracy, integrity and courts (2)<br>6. capacity (1)<br>7. revenue and fiscal, with Codex (2–3)<br>8. transportation (1–2)<br>9. remaining areas: Social Security, immigration, rights, public safety, national security, competition, executive power, amendments (4–6) | Areas done, briefs rebuilt | about 20–25 |
| **6. Permanent rules** | Replace the interim rules with the checks that proved useful: agents' reading order, citation requirements, registry checks in CI | Tier-3 rules PR | 1 |
| **7. Toolkit release** | Professional entry page; consistent scenario definitions where models are compatible, and statements where they aren't; benchmark report; worked examples; licensing and packaging. Candidates in order of readiness:<br>- fiscal, ledger, incidence and fund models;<br>- carbon;<br>- transportation;<br>- child poverty;<br>- calendar and votes;<br>- the intake's CBO scorer | Released toolkit | 5–10 |
| **8. Front door** | Refresh the illustrated vision on the converted areas | New public edition | 1–2 |

**Total:** about 35–45 sessions.

**If sessions are scarce,** do phases 0b through 4 first, about 8 sessions. The pilot needs the checker (phase 3) and the housing outcomes (phase 2). Together these give the most value per session: everything findable, nicknames resolved, new work stopped from thinning, and one fully worked area as a model for the rest. After that, add areas in order of how live their decisions are.

**Time-sensitive work comes first.** The post-election rebaseline of the planning scenario (D1) is due after the November 3 results. It must not wait for the restructuring. It proceeds under the interim rules, and its evidence goes straight into the new registers.

## 9. Coordination and review

- **Codex** owns the shared fiscal model and keeps working throughout. Fiscal and revenue files are converted together with Codex, at a point when integration isn't running. The plan goes to Codex for comment once Codex has credits again.
- **Review.** Every tier 1–2 PR needs a second agent's review, and Codex is currently out of review credits. Until that changes, restructuring PRs are reviewed by a second Claude Code session, or approved by Espen directly where the tier requires it. PRs stay small to keep review practical.
- **Claims.** One area at a time is claimed in the queue. Other work in unconverted areas continues under the interim rules.
- **Intake.** Intake files are citable only once catalogued. Older plans (PROJECT 2029, the war-game set) are historical sources, not policy.

## 10. Capabilities and limits of the agents doing this

- **No memory between sessions.** Each session starts fresh, so the repository, this plan and the progress board carry all state. Startup reading costs part of every session.
- **Limited context.** No agent can hold the whole corpus at once, so cataloguing relies on scripts (titles, headings, links, dates, git history) plus file-by-file judgment.
- **Material agents can't reach:** the claude.ai Projects, the ChatGPT Library, paywalled sources, or anything outside the repository. Those need Espen to upload them.
- **Agents can:**
  - convert PDF, Word, Excel and HTML to text;
  - check public sources on the web;
  - write and test Python;
  - fetch official data for benchmarks.
- **Scanned PDFs** with no text layer may need OCR that is unreliable. They are flagged rather than trusted.
- **Judgment calls can be wrong:** status labels, which claims carry weight, evidence grades. That's why the checks are automatic and every PR is reviewed.
- **Agents never contact other people** on Espen's behalf. Any outside data request, records request or expert review needs Espen.

## 11. Risks and how the plan handles them

| Risk | Handling |
| --- | --- |
| The restructuring swallows the policy work | Small phases, interim rules early, time-sensitive work first, and a defined minimum path |
| Registers grow into busywork | Register only claims that carry weight, with the charter's caution as the rule |
| Restating domain files silently changes policy | The script-based restatement check, and history kept in decision logs |
| A second canon appears | The authority table: provisions extend existing IDs and the ledger; decision records cite governing decisions |
| The toolkit implies precision it lacks | Model cards, benchmarks and stated limits, and no claim to official scores or individual benefits |
| Reviewer shortage stalls merges | A second Claude session as reviewer, small PRs, and direct approval by Espen where needed |
| Copyrighted material leaks into public builds | The rights field in the catalog, and quotations only in public builds |

## 12. Decisions for Espen

1. **Design:** approve the four layers, the authority table and keeping `domains/` and `index/` in place.
2. **Land the plan:** approve merging the intake and this plan into main (phase 0b).
3. **Outcomes record:** agree that I draft it for your approval (phase 2).
4. **Pilot:** housing (recommended) or another area.
5. **Provision format:** specified section by section with IDs, and full legislative text only for priority vehicles (recommended), or full text throughout.
6. **Interim rules:** approve the small rules PR after the catalog (phase 1b).
7. **Toolkit:** who it serves first, whether to license it openly, and which models to release first.
8. **Reviewing:** a second Claude session as reviewer while Codex is out of credits, or your direct approval.
9. **Pace:** the minimum path (about 8 sessions) first, then areas as credits allow (about 35–45 in all).
