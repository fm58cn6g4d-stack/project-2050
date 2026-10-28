# Project 2050: restructuring plan

October 28, 2026 · Proposal for Espen's approval, not yet adopted. Claude Code, branch `claude/research-intake`, from `main` at `9d04b7c`.

## The problem

Project 2050 produced deep research early on: the war-game set, the climate and carbon sessions, the transportation and rail work, the health memo analysis and the ChatGPT pilots. Most of it reached the repository only as conclusions. The domain files cite it by nickname ("Bill Book 12", "the map", "the durability session"), often with no file behind the name. Most domain files carry 0–10 source links. The October 26 fiscal and climate reports carry 0–16, and many have none, because they build on model outputs rather than evidence. Each new layer of work drew on the last summary, so detail thinned out with every pass.

The fix is structural. Research should be stored so it can be called up. Proposals should be written as bills and executive actions that tie back to that research. Models should test whether those proposals deliver the outcomes the project wants. Public content should sit on top and cite all three.

## The target: four layers, each resting on the one below

| Layer | What it holds | Every item must |
| --- | --- | --- |
| **1. Research** | Original sources, data and session reports; research notes and analysis; an evidence register of individual claims | Carry provenance: author, date, URL or original file, checksum and version. Each claim has an ID, a quoted passage and a strength label |
| **2. Models** | Fiscal, distributional, poverty, carbon, transportation and calendar models; their inputs and recorded runs | Trace each input parameter to an evidence ID or a labeled assumption. Record which proposal version each run evaluated |
| **3. Proposals** | Bills (section by section, with provision IDs) and executive actions, plus the policy designs and alternatives behind them | Cite evidence IDs for their rationale and model runs for their cost and effect. State status: selected, alternative or historical |
| **4. Public content** | Essays and research briefs, the illustrated vision and the analysis companion | Cite only proposals, model runs and evidence IDs. The story-page claim register already works this way |

`governing/` stays as it is: goals, decisions and working rules sit above all four layers.

## Principles

1. **Build on what exists.** Nothing is thrown away. Earlier work is catalogued and labeled current, superseded or historical.
2. **One home for each thing.** Every document gets one catalog entry with every name it has gone by, so a nickname always leads to a file.
3. **Claims cite evidence, not summaries.** A figure in a proposal or essay cites an evidence ID, never "per the Bill Book."
4. **Models judge proposals.** Models are the test of whether an action delivers an outcome. They are not a source of facts about the world.
5. **Move gradually.** Folders move one domain at a time, with links updated by script and checks kept green. There is no single big move that breaks every open branch.

## Proposed structure

```
research/
  catalog.csv            one row per document: id, title, aliases, path, layer, domain, version, supersedes, status, provenance
  intake/<date>/         raw uploads, unchanged (2026-10-28 is filed)
  library/<domain>/      originals worth keeping, converted to readable text where needed, with a source card each
  notes/<domain>/        analysis and session findings (most of today's sources/ reports)
  evidence/<domain>.csv  claim register: id, statement, figures, source id, locator/quote, date, strength, policy/provision ids
models/                  today's index/tools and index/data, unchanged at first; later each model gets an evidence map and run log
proposals/
  <domain>/design.md     today's domain file, slimmed to design choices, alternatives and their reasons
  <domain>/bills/<bill>/ section-by-section with provision IDs, cost and effect from model runs, evidence IDs
  executive/<id>.md      executive actions, same fields
public/                  today's index/public-2050 and its builders
governing/               unchanged
```

How today's folders map:

| Today | Becomes |
| --- | --- |
| `domains/` | `proposals/<domain>/design.md` plus bill and executive-action specs |
| `sources/` | Mostly `research/notes/`. Original-source copies go to `research/library/`, and generated model reports go to `models/` |
| `frameworks/`, `staging/` | `research/notes/` (reasoning) and catalog rows |
| `archive/` | `research/library/historical/`, labeled historical |
| `index/` | `models/` (tools, data, outputs) and `public/` (the public edition) |

## How the work proceeds

Each phase is one or two sessions and ends in a reviewable PR.

**Phase 0: preserve the uploads (done).** The three uploaded archives are filed unchanged in `research/intake/2026-10-28/` on this branch, with a checksum manifest. The public PDFs and CBO data are recorded by checksum only.

**Phase 1: catalog and lineage.** List every document in the repository and the intake: what it is, all its names, which version is current, what it supersedes, which domain and layer it belongs to, and whether it is current, superseded, historical or raw. This produces `research/catalog.csv` and a name index that resolves every nickname. It also reports duplicates and conflicting versions; examples already found are the PROJECT 2029 copies, the two carbon-fee baselines, and the Thriving map in Markdown and docx. No files move in this phase.

**Phase 2: one domain end to end, as the pilot.** I recommend **housing**. It is small, it already has a research brief and a partial evidence register, and the new material includes its main original (Bill Book 12). Steps:
- build `research/evidence/housing.csv` from the originals and primary sources;
- write the housing bill as a section-by-section with provision IDs;
- link the poverty and cost models to those provisions;
- rebuild the public brief on that base.

What the pilot teaches fixes the templates before they are rolled out.

**Phase 3: domain by domain.** Suggested order, set by how much new material is waiting and how live the decisions are:
1. climate (SEEC report, permitting, the FEMA Act, carbon models, the durability work);
2. health;
3. family and education;
4. labor and AI;
5. democracy, integrity and courts;
6. capacity;
7. revenue and fiscal, coordinated with Codex as the fiscal integration owner;
8. transportation, which is already closest to the target and is mostly mapping;
9. the rest.

**Phase 4: outcome models.** Write down the outcomes the charter commits to: income security, housing stability, health access, emissions, democratic participation and the rest. Map which actions move each one, and set each model to evaluate proposals against those outcomes, with recorded runs.

**Phase 5: rules and checks.** These are tier-3 changes and need your approval. Agents read the research layer for a domain before writing about it. A new factual claim cites an evidence ID. An automatic check flags nicknames that lead nowhere and claims with no evidence. The merge policy's path rules are updated for the new folders.

**Phase 6: public content.** The remaining essays are rewritten as research briefs, in the persuasive and optimistic tone you set, from the proposals and evidence. The front door is refreshed on the same base.

## Coordination and limits

Codex is active on the shared fiscal model, so restructuring claims one domain at a time in the queue and avoids moving fiscal paths while integration runs. Moving folders changes the merge-gate path rules, which is a tier-3 change. The intake files are untriaged: they become citable only after cataloguing, and older plans (PROJECT 2029, the war-game set) are labeled historical, not policy.

## Decisions for Espen

1. Approve the four-layer structure and the folder names, or adjust them.
2. Pilot domain: housing (recommended) or another.
3. Proposals format: section-by-section specs with provision IDs for every bill, with full legislative text only for priority bills (recommended), or full text throughout.
4. Pacing: one phase per session as credits allow. Phase 1 (the catalog) is the right next step either way.
