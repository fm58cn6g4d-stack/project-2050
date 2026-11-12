# Dossier template

Role: the shape every dossier follows (`charter/PLAN.md` 3.3). Status: current; revised after stage C (housing, closed at L3, and transportation, the reference conversion) with what both taught.

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
  memos/               one decision memo per real fork, and memos/README.md, the batch Espen decides in one round
  evidence.json        evidence register (EV-<CODE>-001 ...)
  provisions.json      provisions (HOU-4A.01 ...), from section 4 on
  restatement.json     for a dossier converted from legacy files: each legacy file and the files that replace it
  restatement-log.md   what the conversion dropped or kept by reference on purpose
```

**Reserve ID ranges first.** Before drafting evidence, the README names the dossier's evidence code and a block of source IDs no other dossier uses (for example SRC-3500 to 3599 for transportation); check the other active dossiers' READMEs for the blocks already reserved. `library/build_catalog.py` assigns the next free number, so two dossiers drafting at once will collide without a reservation. Transportation's first block collided with care's and had to be renumbered in review.

Sections are written in order. A section is added when it is drafted; the README lists what exists.

## Rules for every section

- **Top line.** Each file opens with its role and status: draft, reviewed (L2 or L3 milestone review) or current.
- **Evidence.**
  - Every number or factual claim cites an evidence ID in brackets, for example [EV-HOU-001].
  - **Reader-facing pages** (decision memos, lists Espen decides item by item, and the public case) also name each source in plain text before the tag. Give the publisher or research team, a short name a lay reader recognizes, and the year, taken from the source's catalog row, for example "(Family Options Study, Gubits and others, 2018) [EV-HOU-086]". Each option and recommendation in a memo states the evidence it rests on. Where it rests on judgment, a direction from Espen or a gap in the register, the memo says so plainly. Internal sections may keep tags only.
  - Each ID's entry in `evidence.json` names a catalogued source (`SRC-`) and the exact passage. The registry checker confirms that every figure appears in that passage.
  - Any credible source may be used: government data, peer-reviewed research, think-tank and advocacy analysis, international programs, practitioners. Public-domain and openly licensed documents are saved as text with `library/fetch_public.py`; licensed ones are catalogued as citation rows and quoted briefly, with a locator (`library/README.md`).
  - **Data or analysis.** Each evidence entry says which it is (`claim`). Data is a measured fact: a count, a rate, a price. Analysis interprets facts: causes, effects, projections, model estimates. A report can supply both, and its data can be used while its analysis is questioned. An agency's own causal account is graded as analysis (usually C), not as official data (A).
  - **Context.** Analysis entries, and data from a source with a stake in the answer, carry a `context` note: who published it, when, under which administration or funder, and what stance the publisher holds. Check whether a report's own numbers support its headline framing; record it where they do not. For an executive-branch source, the context names the administration (for example "HUD, second Trump administration, 2025"). Analysis from the second Trump administration is presented as that administration's view and never carries a recommendation on its own, even after corroboration: the dossier rests on the independent sources, citing the administration's analysis beside them. Its data can still be used, but note any change in method, scope or release schedule that coincides with the administration.
  - **Corroboration.** An analysis entry lists the entries that support, contest or qualify it (`corroboration`). The dossier relies on an analysis only when at least one that supports or qualifies it comes from an independent publisher; where an independent source contests it, the dossier presents both views. Look across perspectives: academic research, nonpartisan agencies (CBO, CRS, GAO, the Federal Reserve), and analysts of different political leanings. Until then the checker warns, and the prose presents the analysis as one source's view.
  - Grade by the kind of evidence, not the publisher's sector; an advocacy group's own estimate is usually C, and its design proposals are positions to weigh in section 3, not evidence.
- **Time frame.** Recommendations are for a plan that starts in January 2029 (`charter/STANDARDS.md`, "Time frame"). The design section states the baseline as it will stand in 2029, including enacted laws with later effective dates and sunsets, and labels anything meant for 2027-28 or for preparation before 2029.
- **Gaps.** Where evidence is missing, say so in a short "Evidence still needed" list naming the source, instead of writing the claim without it.
- **Grades.** Each evidence entry carries a grade:
  - A: official data or primary law;
  - B: experimental or peer-reviewed research;
  - C: credible secondary analysis;
  - D: project estimate;
  - E: assumption.
- **Re-check dates.** Set each one to the source's next scheduled release.
- **Commitment, assumption, open question or something to study in implementation.** Each material input in the cost and validation sections says which it is: a commitment (decided), a working assumption (with basis and range), an open question (with the alternatives) or something to study in implementation (with the pilot or administrative data that will answer it), so precise numbers don't read as more certain than they are (`charter/STANDARDS.md`, "What needs an answer now").
- **Outcomes.** The problem and validation sections name the outcomes (`OUT-`) the dossier is meant to move.
- **Shared rules.** The design section lists each rule in `dossiers/shared-rules.md` the dossier relies on (what counts as income, immigrant eligibility, phase-outs, verification, conditions on help), with its working answer and a range, unless the owner dossier has decided it. The specification keeps each such rule in one place so it can change without a rewrite.
- **Agenda items.** Agenda IDs (`HOU-4A`) are cited as they appear in `agenda/agenda.csv`. The dossier's design section is where an item's level and status change.
- **Consistency while writing.** An amount, limit or status that changes changes everywhere in the same PR: sections 3 to 9, `provisions.json`, the agenda row, the README's headline and the memo status lines. Section 4 keeps a consistency table of every decided amount and where it appears. Before opening a PR, search the dossier for the old figure. Housing's L3 review found stale totals in four sections, decided items still marked "proposed" and a section 3 with no "Decided" lines (`dossiers/home/review-milestone.md`, part 6). Each was small; together they blocked L3.
- **One basis for each fiscal figure.** Section 6 compares like with like. It reports each fiscal-rule figure (yearly cost, permanent cost from FY2040, share of the plan-wide margin) on the same basis as the budget model's booking, shows the booking beside it, and says why they differ. Spending lines and revenue effects stay apart: the 25% income and payroll tax offset on new excises is a revenue effect with its own ledger line (MR6 for transportation), so a figure that already includes it is labeled so and never added to a spending line. Section 6 also checks that the line is booked where it falls, in the budget model's base and on the general fund, and if it is not, reports the offset on its own line as not yet booked (transportation's MR6 was not, at its L3 review, #207). Transportation's section 6 first mixed bases and then double-counted the offset before review settled it ($29.0 billion on the model's spending path against $22.1 billion booked for FY2040; `dossiers/agenda/transportation/6-cost.md`, section 3).
- **Say what a model figure leaves out.** When section 6 quotes a model total, it lists the items the model leaves out that section 4 keeps, with their amounts, and says why each is not in the total. It keeps authorization apart from expected outlay (a grant subject to appropriation, or partly in the baseline already) and contingent money apart from firm money (a reserve released only when its gates clear, shown as a range from zero to its cap). It does not add these to the booked figure or call the sum an established score. Transportation's draw left out sec. 1112's grants ($17.24 billion) and the readiness reserve ($0 to $25 billion); review found it (#203).
- **Decision memos in one batch.**
  - Collect every real fork into one memo set, two to four options each with a recommendation, indexed in `memos/README.md`.
  - Narrower points go in section 3 as a numbered yes-or-no list. None is adopted by silence.
  - Send the batch once, so Espen decides in one round. Sections 4 to 9 may be drafted on the recommendations meanwhile, and are revised for any other answer.
  - Once decided, each memo's status line and section 3 cite the `DEC-` entry.
  - What a good memo set has (care's `3-design.md`, memos 1-5, and the S. 1506 comparison are the model): a forks-at-a-glance table; costs benchmarked against outside scores (CBO, JCT, SSA's actuaries, TPC and others); a bill-by-bill comparison; plain consequences for real households; every inherited assumption traced to its source, saying whether Espen decided it.
  - Offer Espen a decision sheet (an artifact listing each memo's options and the recommendation) alongside the board question.
- **Rural delivery.** Where a program must reach rural places, section 5 looks first at USDA's local channels (Rural Housing Service, Rural Utilities Service, Rural Business-Cooperative Service, the state and area offices) before building new ones, and weighs scaling them up, with the staff, money and eligibility they need (`DEC-2026-11-09-26`; evidence in `dossiers/foundations/rural-delivery.md`).
- **Section 9 only from sections 1 to 8.**
  - Every number in the public case appears in sections 1 to 8 with its evidence ID, and a source table at the end traces each one.
  - A project estimate is shown as one, with "about", its range or "on our estimates", and a result that holds only under conditions carries them.
  - Section 9 is written last, and revised in the same PR as any section it draws on.
  - A promise in section 9 holds from the date the provision behind it takes effect. Where provisions start at different times, say when each protection begins. Transportation's first draft promised privacy rules from the charge's first day, although they arrive a year later in the 2031 bill (#203 review).
  - Housing's review blocked section 9 for estimates stated as facts and a fiscal pass stated without its conditions (`dossiers/home/review-milestone.md`, W-1, E-1 to E-5).
- **Converting legacy content.**
  - Run the restatement check (`models/registry/restatement.py`) on each legacy file against the dossier.
  - The governing file is restated in full or accounted for in `restatement-log.md`, with each dropped number or ID in backticks and its reason. Detail files can be marked `by_reference` in `restatement.json`, each with its own accurate reason, not shared boilerplate; the reviewer checks every reason, because the opt-out skips `--strict` for that file. #203's review caught seven files with the same note.
  - A legacy fact without a source is traced to one or left out, and section 1 lists what it left out.
  - Legacy model figures a memo relies on enter the register as grade D entries anchored in the legacy text, so every memo number traces.
- **Model tier.** Problem and design sections are Most capable work. Evidence entries drafted from originals are Standard. Text extraction is Light (`charter/STANDARDS.md`).
