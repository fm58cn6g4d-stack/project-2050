# Dossier template

Role: the shape every dossier follows (`charter/PLAN.md` 3.3). Status: current; stage C (housing, then transportation) tests it and fixes it.

## Folder

```
dossiers/<name>/
  README.md            status, level, owner, sections done, open questions for Espen
  1-problem.md         what is wrong, for whom and how large
  2-what-works.md      research, programs at home and abroad, failures to avoid
  3-design.md          the real forks, options weighed, the choice and its reasons; decision memos
  4-specification.md   provisions section by section (IDs in provisions.json)
  5-delivery.md        administration, capacity, timeline, remedies, state roles
  6-cost.md            cost ranges from the models, fit with the fiscal rule
  7-validation.md      model runs, benchmarks, what the models miss, objections answered
  8-change-our-minds.md
  9-public-case.md     research brief and organizing material, never ahead of sections 1-8
  evidence.json        evidence register (EV-<CODE>-001 ...)
  provisions.json      provisions (HOU-4A.01 ...), from section 4 on
```

Sections are written in order. A section is added when it is drafted; the README lists what exists.

## Rules for every section

- **Top line.** Each file opens with its role and status: draft, reviewed (L2 or L3 milestone review) or current.
- **Evidence.**
  - Every number or factual claim cites an evidence ID in brackets, for example [EV-HOU-001].
  - **Reader-facing pages** (decision memos, lists Espen decides item by item, and the public case) also name each source in plain text before the tag. Give the publisher or research team, a short name a lay reader recognizes, and the year, taken from the source's catalog row, for example "(Family Options Study, Gubits and others, 2018) [EV-HOU-086]". Each option and recommendation in a memo states the evidence it rests on. Where it rests on judgment, a direction from Espen or a gap in the register, the memo says so plainly. Internal sections may keep tags only.
  - Each ID's entry in `evidence.json` names a catalogued source (`SRC-`) and the exact passage. The registry checker confirms that every figure appears in that passage.
  - Any credible source may be used: government data, peer-reviewed research, think-tank and advocacy analysis, international programs, practitioners. Public-domain and openly licensed documents are saved as text with `library/fetch_public.py`; licensed ones are catalogued as citation rows and quoted briefly, with a locator (`library/README.md`).
  - **Data or analysis.** Each evidence entry says which it is (`claim`). Data is a measured fact: a count, a rate, a price. Analysis interprets facts: causes, effects, projections, model estimates. A report can supply both, and its data can be used while its analysis is questioned. An agency's own causal account is graded as analysis (usually C), not as official data (A).
  - **Context.** Analysis entries, and data from a source with a stake in the answer, carry a `context` note: who published it, when, under which administration or funder, and what stance the publisher holds. Check whether a report's own numbers support its headline framing; record it where they do not.
  - **Corroboration.** An analysis entry lists the entries that support, contest or qualify it (`corroboration`). The dossier relies on an analysis only when at least one that supports or qualifies it comes from an independent publisher; where an independent source contests it, the dossier presents both views. Look across perspectives: academic research, nonpartisan agencies (CBO, CRS, GAO, the Federal Reserve), and analysts of different political leanings. Until then the checker warns, and the prose presents the analysis as one source's view.
  - Grade by the kind of evidence, not the publisher's sector; an advocacy group's own estimate is usually C, and its design proposals are positions to weigh in section 3, not evidence.
- **Gaps.** Where evidence is missing, say so in a short "Evidence still needed" list naming the source, instead of writing the claim without it.
- **Grades.** Each evidence entry carries a grade:
  - A: official data or primary law;
  - B: experimental or peer-reviewed research;
  - C: credible secondary analysis;
  - D: project estimate;
  - E: assumption.
- **Re-check dates.** Set each one to the source's next scheduled release.
- **Outcomes.** The problem and validation sections name the outcomes (`OUT-`) the dossier is meant to move.
- **Agenda items.** Agenda IDs (`HOU-4A`) are cited as they appear in `agenda/agenda.csv`. The dossier's design section is where an item's level and status change.
- **Model tier.** Problem and design sections are Most capable work. Evidence entries drafted from originals are Standard. Text extraction is Light (`charter/STANDARDS.md`).
