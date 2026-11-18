# Memo 10: Measuring job displacement, and a standby trigger that scales help up

Role: decision memo for Espen, written in section 4 as `DEC-2026-11-17-96` directs: "measurement of displacement (AI-4D) and a standby displacement trigger go to Espen in work's section 4, and the whole AI-and-work strategy (AI-4A to 4F) becomes its own topic in a later stage". It starts from the follow-up note's part d, recommendation (iii) (`../notes/espen-questions-2026-11-17.md`). Status: **open, for Espen; drafted in section 4 on the recommendation and provisional** (`../4-specification.md`, part E, LAB-19.01 to 19.05), as the lead asked on November 18 relaying Espen's wish to keep going and review decisions in the morning. Nothing in section 4's decided provisions depends on the answer. AI-4D is the AI topic's agenda row (`agenda/agenda.csv`, home `agenda/ai`); this memo proposes the work flagship's part of it. The legacy designs (AI-4's measurement "set in statute, published annually, and audited by GAO"; AI-4D's occupations list) are working choices, not Espen's (`DEC-2026-10-30-02`; `legacy/domains/domain-ai.md`, AI-4). Sources are named in plain text; bracketed tags point to `../evidence.json` or another dossier's register.

**Decision line.** Recommended: **part 1 C, measure displacement from the records the plan already builds: hours and occupation added to every state's quarterly wage records (already decided for wage insurance, way iii), a reason box on the 90-day layoff notice that includes technology and automation, and a yearly BLS report of displacement by occupation, industry, region and age, with AI-exposed occupations flagged as an analysis, never as an eligibility test; part 2 C, a standby trigger: where measured displacement in an occupation group or region rises well above its own recent level for two quarters running, help expands automatically and within a yearly cap (wage insurance for a third year and from one year's tenure, and priority apprenticeship and service-to-apprenticeship places for workers under 30), and switches off when the measure falls back. It starts once part 1 has two years of data.** Cost: part 1 about **$0.5-1 billion over FY2030-39** (judgment); part 2 **zero while it is off**, up to its cap when on, about **$0 to +$0.02 trillion over FY2030-39** on today's evidence (judgment). Evidence: official data on displacement and its costs; working papers on AI's early effects, which disagree about entry-level jobs; Extended Benefits as the one U.S. precedent for an automatic trigger, with disputed effects. No displacement trigger has been evaluated anywhere in the register.

## The question

Espen decided wage insurance "for now" and asked for "a plan for potential AI job displacement", worried that wage insurance alone is "more of a patch than a strategic plan" (`DEC-2026-11-17-12`, `-95`). The follow-up note found two gaps a strategic plan needs and the plan lacks:
- nothing measures displacement, AI's or any other, often or finely enough to act on;
- nothing scales help up if displacement grows, except Extended Benefits, which responds to recessions only.

This memo asks how to fill each. Who gets help is already settled and does not change: help never asks what caused a job loss (memo 8; LAB-18.01).

## Why it matters

- **Job loss is common and costly now.** 3.3 million long-tenured workers were displaced in 2023-25, up 746,000 on the previous survey (BLS) [EV-WRK-315]. Only 49% of those back in full-time work earned as much as before, down from 62% two years earlier [EV-WRK-317]. Losses last for years (Jacobson, LaLonde and Sullivan) [EV-WRK-321].
- **The best current measure is slow.** BLS's displaced-worker survey asks about the last three years once every two years, in January 2024 and January 2026 [EV-WRK-315] [EV-WRK-317]. It cannot show where displacement is rising this year.
- **AI's effect is not yet visible overall, but may be at entry level.**
  - The Yale Budget Lab finds no clear disruption through August 2026 [EV-WRK-357] [EV-WRK-358].
  - Brynjolfsson, Chandar and Chen find employment of workers aged 22 to 25 in AI-exposed occupations 19% below trend in payroll data, with no gap for experienced workers [EV-WRK-355].
  - Dallas Fed economists put the most that shift could add to unemployment at 0.1 point [EV-WRK-359].
  - About 80% of workers have at least a tenth of their tasks exposed to large language models (Eloundou and co-authors) [EV-SEC-125].
- **For a household.** A 23-year-old graduate who cannot find a first job in an exposed field has no job to lose, so unemployment and wage insurance miss them. A 50-year-old claims processor laid off after 15 years gets wage insurance for two years. Neither is helped more if their occupation's losses double.

## What the evidence says, in four lines

1. **The facts to measure exist in records already held.** States decide why each claimant's job ended, sorting separations into lack of work, quits and discharges [EV-WRK-414] [EV-WRK-416], and they hold employers' quarterly earnings reports (the follow-up note, part d; no register entry). Adding hours and occupation to wage records is already decided for wage insurance (`DEC-2026-11-17-95`, way iii). How many states record hours today is not in the register (Evidence still needed).
2. **Early AI studies disagree, and change fast.** Most are 2025-26 working papers [EV-WRK-355] [EV-WRK-358] [EV-WRK-361]. That is a reason to measure, not to act on any one of them.
3. **Automatic triggers exist for recessions, with disputed effects.** Extended Benefits switch on at set unemployment rates [EV-WRK-395]. Their effect on unemployment ranges from 2 points on one design [EV-WRK-374] to at most 0.3 on a cleaner one [EV-WRK-375]. No trigger tied to displacement in an occupation has been evaluated.
4. **The help a trigger would expand is evaluated.** Wage insurance raised older trade-displaced workers' employment 8 to 17 points and paid for itself (Hyman, Kovak and Leive) [EV-WRK-365]. Sector training built with employers raised earnings 11-40% in pooled randomized trials [EV-SEC-143].

## Part 1. Measuring displacement

**A. Today's surveys only.** BLS's displaced-worker survey every two years [EV-WRK-315], and the plan's yearly counts (the apprenticeship report, LAB-8.04; the transition guarantee's report, CLI-11.05).
- *Cost:* zero.
- *What it leaves:* no measure by occupation and region often enough to act on, and nothing a trigger could read.

**B. The legacy AI-4D.**
- *What it does:* a Labor Department list of "AI-augmented" occupations, set with public comment and demographic and geographic analysis; displacement reporting by federally funded workforce grantees; equity benchmarks (the AI Education and Workforce Readiness Act's secs. 4, 209 and 305; `legacy/domains/domain-ai.md`, AI-4D).
- *What it buys:* a working definition of an "AI-affected" occupation.
- *What it costs:* little money. Grantee reports count only workers who reach a grantee, and a list of AI occupations invites disputes about eligibility, which the plan has ruled out (cause is never asked).

**C. Displacement measured from records the plan already builds (recommended).**
- *Records:* hours and occupation on every state's quarterly wage report by January 1, 2033 (LAB-18.06, already decided as wage insurance's way iii), so BLS can count, every quarter, long-tenured workers who lose a job, by occupation, industry, region and age, and what they earn after.
- *Notice:* the 90-day layoff notice (LAB-13.01, decided) carries a reason box, with "a change in technology or automation" one of the choices, filed with the state as the notice already is.
- *Report:* BLS publishes a yearly displacement report from these records and the survey, with AI-exposed occupations flagged using published exposure measures [EV-SEC-125]. The method is set in statute and audited by GAO, as the legacy AI-4 proposed.
- *Never an eligibility test:* the flags inform policy and the trigger (part 2), not who gets help.
- *Cost:* about $0.5-1 billion over FY2030-39 (judgment: BLS's report and the survey's move to every year, about $20-50 million a year, plus a one-time grant to states for the new fields, about $0.2-0.5 billion). The hours field itself is in memo 7's data agreement and memo 8's administration.
- *Burden:* employers add two fields to a quarterly report they already file; workers do nothing.

**D. C plus employers' reports of AI use.** Employers of 500 or more file a yearly report of AI systems that replaced or changed jobs.
- *What it buys:* a direct measure of adoption, not only of outcomes.
- *What it costs:* a new report with no tested design behind it, and answers that depend on how each employer reads "replaced". The guide-don't-police lens counts against it (`DEC-2026-11-09-13`).

## Part 2. A standby trigger

**A. None beyond Extended Benefits.** Help grows only in recessions [EV-WRK-395], or when Congress acts.
- *What it leaves:* concentrated displacement, in an occupation or a region during a good economy, gets no more help than today.

**B. Report and respond.** When part 1's measure crosses a threshold, Labor reports to Congress within 90 days with options. Nothing changes automatically. This is the transition guarantee's rule (CLI-11.05).
- *What it buys:* attention, at no cost.
- *What it costs:* it depends on Congress acting in time. TAA lapsed in July 2022 and has certified no one since [EV-WRK-330].

**C. An automatic, capped expansion (recommended).**
- *The test:* BLS's quarterly measure (part 1 C). An occupation group or a state is "in a displacement period" when either measure stays well above its own recent level for two quarters running (working choice: 50% above):
  - the share of long-tenured workers in it who lose their jobs, against its average of the prior five years;
  - or the employment of workers under 26 in it, against its trend.
- *What switches on, for workers from that occupation or state:*
  - wage insurance for a third year, and from one year's tenure instead of three (LAB-18.01, 18.02);
  - for workers under 30, priority for apprenticeship places with LAB-8's grants, and for service-to-apprenticeship places (LAB-9.03) once that tranche is open.
- *The cap:* the expansion spends at most $5 billion a year in all (working choice). If the cap binds, the third year is paid first.
- *Switching off:* the period ends when the measure falls back below the threshold for two quarters. A worker already enrolled keeps the expanded help.
- *Starts:* once part 1 C has two years of data, about 2035 on the working timeline.
- *Cost:* zero while off. Up to the cap when on. About $0 to +$0.02 trillion over FY2030-39 on today's evidence (judgment), since broad displacement does not yet appear [EV-WRK-358] and the trigger starts late in the decade.
- *Why:* it answers Espen's "patch" worry with a rule that grows help where displacement grows, without asking whether AI caused it. The cap keeps it inside a known envelope.

**D. C plus a demand-side response that switches on.** In a displacement period, an entry-level hiring credit (AI-4E: 25% of the first $40,000 of wages for two years for workers under 27, about $0.21 trillion at the legacy scenario's scale) or a transitional job offer (AI-4F, which memo 9 proposed not to take) opens automatically.
- *What it buys:* the only answer to a demand gap inside firms, which the legacy stress test found training cannot fix (`legacy/domains/domain-ai.md`, AI-4).
- *What it costs:* much more when on, with no U.S. evaluation of either. Both are better weighed in the AI-and-work topic (`-96`).

## Against the bills and the legacy

| Design | Measurement | Trigger | Against the recommendation |
| --- | --- | --- | --- |
| **Legacy AI-4** (`domain-ai.md`) | BLS measures AI-attributable displacement; method in statute, yearly, audited by GAO | The benefit's allocation follows measurement; no cause test | **Match** on statute and audit; **diverge**: C measures all displacement and flags AI exposure, rather than attributing losses to AI |
| **Legacy AI-4D** (the AI Education and Workforce Readiness Act, secs. 4, 209, 305) | An occupations list, grantee reporting, benchmarks | — | Option B; C keeps the list as an analytic flag |
| **Extended Benefits, reformed** (memo 7; S. 2312) [EV-WRK-395] | Unemployment rates | Automatic, by state, for recessions | C borrows the shape for occupations and regions |
| **Clean power's guarantee** (CLI-11.05) | Yearly counts | A report to Congress in 90 days | Option B |
| **TAA** [EV-WRK-330] | Petitions, case by case | Certification per petition | C replaces petitions with records |

No CBO score of a displacement trigger exists.

## Consequences at a glance

| | Part 1 A | B | **C** | D |
| --- | --- | --- | --- | --- |
| Displacement by occupation and region | Every two years, survey only | Grantees only | Every quarter, all covered workers | As C, plus adoption |
| New burden | None | Grantee reports | Two fields on an existing report | A new employer report |
| FY2030-39 | Zero | About zero | About $0.5-1 billion | Slightly more |

| | Part 2 A | B | **C** | D |
| --- | --- | --- | --- | --- |
| Help grows when displacement grows | Recessions only | If Congress acts | Automatically, capped | Automatically, larger |
| A 23-year-old in an exposed field | Nothing new | Nothing new unless Congress acts | Priority apprenticeship and service places | Also a hiring credit or a job offer |
| A 50-year-old laid off after 15 years | Two years of wage insurance | The same | A third year in a displacement period | As C |
| FY2030-39 | Zero | Zero | About $0 to +$0.02 trillion | More, unscored |

## Recommendation: part 1 C, part 2 C

- **Measure first, from records the plan already builds.** The hours field is decided; adding occupation and a reason box costs little and gives the plan its own measure of displacement, AI's included, without a new report for workers.
- **A rule that grows help where displacement grows** turns wage insurance from a patch into the first layer of a plan. The cap and the switch-off keep it bounded, and it never asks what caused a loss.
- **The demand-side tools (D) belong in the AI-and-work topic.** They are larger and unevaluated, and `-96` puts that strategy in a later stage.
- **What it costs in burden:** two fields for employers on a quarterly report; nothing for workers.

**What would change this:** the 2026 entry-level finding [EV-WRK-355] confirmed and growing in later data (start part 2 sooner, or take D's hiring credit); an evaluation showing that occupation-level triggers fire on noise (move to B); states unable to add hours by 2033 (keep A's survey and move the trigger's start).

## If you decide

- Section 4 has drafted parts 1 C and 2 C as LAB-19.01 to 19.05 (agenda row LAB-19, L1 until decided). If Espen chooses otherwise, those provisions are revised or dropped. AI-4D stays the AI topic's row.
- **Vehicle:** the records, the report and the notice box ride the labor act; the trigger's spending rides the reconciliation act with wage insurance, as contingent spending.
- **Preparation before 2029:** the UI data agreement adds the occupation field to the hours field already planned.

## Options for the future labor economy, to explore later (`DEC-2026-11-17-96`)

Espen asked that later work explore several options for the future U.S. labor economy, and not treat wage insurance as the answer. These are the options the repository already names. The AI-and-work topic (AI-4A to 4F) takes them up as its own topic in a later stage; none is decided or costed here.
- **Demand for entry-level workers:** an entry-level hiring credit (AI-4E); a transitional job guarantee (AI-4F, which memo 9 proposed not to take now).
- **Skills:** training accounts (AI-4A's legacy design, about $8,000 a worker); a narrowed AI reskilling credit (AI-4C).
- **Income while work changes:** wage insurance's length and level (memo 8 B, decided for now); portable benefits for people between jobs (AI-4A; point 12 declined a separate program for contractors); work sharing at larger scale (LAB-11.03).
- **Voice in how technology arrives:** technology change named as a subject of bargaining and of standards boards' rules (the note's part d); sectoral bargaining over time (LAB-3B, `DEC-2026-11-17-06`); worker seats on boards (point 11, being studied); rules on AI in hiring and evaluation (AI-11).
- **Sharing the gains:** the AI revenue instruments the legacy file holds (AI-6A to 6D); labor's share of income, which BLS's index shows falling since 2000 [EV-WRK-404], as a measure the plan reports; the capital-income stack for stage G (`dossiers/foundations/notes/stack-2026-11-16.md`).
- **Time:** shorter standard hours or a lower overtime line as productivity rises. No evidence is in the register; this is a question to research, not an option yet.

The lead is asked to name the AI-and-work topic as a later-stage board step (the note's recommendation iii).
