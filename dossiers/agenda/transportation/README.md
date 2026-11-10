# Dossier: transportation (wave two; the reference dossier)

Role: the transportation dossier, converted from the legacy Moving America design as the reference example of a finished dossier (`charter/PLAN.md` 3.1). Status: in progress, stage C step 7 (sections 1-3 drafted; memo set with Espen). Level: every item is at L1 in `agenda/agenda.csv`; the target is L3, with priority pieces at L4.

**What it brings together:** highways and highway safety, public transportation, intercity passenger rail, and the Surface Transportation Trust Fund that pays for them, carried by four laws: a 2028 extension (a labeled 2027-28 exception), the 2029 and 2030 reconciliation acts, and the Moving America Act of 2031.

**Agenda items:** MOV-29, MOV-30, MOV-31 and MR1 to MR6 (`agenda/agenda.csv`, `home_dossier` = `agenda/transportation`).

**Sources being converted:** `legacy/domains/transportation-moving-america-act-2031-draft-2.md` (Draft 2 governs where sources disagree), `legacy/sources/transportation-*.md`, `legacy/frameworks/transportation-transit-rail-split.md`, and the transportation model in `models/tools/transportation/`. This is a conversion, not new research: gaps are filled only where a decision needs them (`charter/STANDARDS.md`, "What needs an answer now").

**Restatement check:** `restatement.json` maps each legacy file to the files that replace it; `python3 models/registry/restatement.py --map dossiers/agenda/transportation/restatement.json` lists every number and policy ID not carried over. Anything dropped on purpose goes in `restatement-log.md` (from section 4 on) or the decision log.

**Outcomes it serves:** OUT-05 (clean power and a prepared country: transport emissions and resilience) and OUT-11 (the fiscal tests). `charter/outcomes.md` has no transportation outcome of its own; whether it needs one is a question for section 1.

| Section | Status |
| --- | --- |
| 1. The problem | Draft (PR 2): `1-problem.md`. The trust fund's 2028 cliff, repair, the Interstate, buying power, deaths, slow grants, transit, rail, household cost and emissions; legacy facts traced or left out. Evidence EV-MOV-001 to 018 and 100 onward |
| 2. What works | Draft (PR 2): `2-what-works.md` |
| 3. Design choices | Draft (PR 2): `3-design.md`. The baseline in 2029 as a working assumption with three cases; the 0.206% benchmark retired as a design rule (`DEC-2026-11-10-05`); six forks, each with a memo in `memos/`, sent as one batch (`memos/README.md`); eight yes-or-no points; all 28 legacy calls (A-1 to A-28) placed. Project-estimate figures EV-MOV-200 to 226 |
| 4. Specification | Not started (PR 3), with `provisions.json` |
| 5. Delivery | Not started (PR 3) |
| 6. Cost and financing | Not started (PR 3), on the transportation model and the budget model |
| 7. Validation | Not started (PR 3) |
| 8. What would change our minds | Not started (PR 3) |
| 9. The public case | Not started (PR 3), only from sections 1-8 |

Evidence register: `evidence.json` (EV-MOV-001 to 099 section 1; 100 to 199 transit, rail and section 2; 200 to 299 project estimates from the legacy model). Source IDs numbered 3500 to 3599 are reserved for this dossier (the care dossier uses 3000 to 3299). Provisions: `provisions.json`, IDs under the agenda's MOV- rows (from section 4).

## Open questions for Espen

One batch (`memos/README.md`): memos 1 to 6 and the eight yes-or-no points in `3-design.md`, "Recommended without a memo". Point 7 (a transportation outcome) would be a charter change in its own PR. Sections 4-9 are written on the recommendations and revised for any other answer.
