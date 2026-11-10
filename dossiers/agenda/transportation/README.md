# Dossier: transportation (wave two; the reference dossier)

Role: the transportation dossier, converted from the legacy Moving America design as the reference example of a finished dossier (`charter/PLAN.md` 3.1). Status: in progress, stage C step 7: sections 1-9 drafted; the memo set decided as recommended (`DEC-2026-11-10-08`). Level: MOV-28 to MOV-31 and MR1 to MR6 are at L3 (specified) in `agenda/agenda.csv`, after the milestone review (`review-milestone.md`), its fixes (#208, #209, #210, #211) and the L3 re-check; priority pieces go on to L4.

**What it brings together:** highways and highway safety, public transportation, intercity passenger rail, and the Surface Transportation Trust Fund that pays for them, carried by four laws: a 2028 extension (a labeled 2027-28 exception), the 2029 and 2030 reconciliation acts, and the Moving America Act of 2031.

**Agenda items:** MOV-29, MOV-30, MOV-31 and MR1 to MR6 (`agenda/agenda.csv`, `home_dossier` = `agenda/transportation`).

**Sources being converted:** `legacy/domains/transportation-moving-america-act-2031-draft-2.md` (Draft 2 governs where sources disagree), `legacy/sources/transportation-*.md`, `legacy/frameworks/transportation-transit-rail-split.md`, and the transportation model in `models/tools/transportation/`. This is a conversion, not new research: gaps are filled only where a decision needs them (`charter/STANDARDS.md`, "What needs an answer now").

**Restatement check:** `restatement.json` maps each legacy file to the files that replace it; `python3 models/registry/restatement.py --map dossiers/agenda/transportation/restatement.json` lists every number and policy ID not carried over. Anything dropped on purpose goes in `restatement-log.md` (from section 4 on) or the decision log.

**Outcomes it serves:** OUT-12 (getting where you need to go, safely and affordably; added with `DEC-2026-11-10-08`), OUT-05 (clean power and a prepared country: transport emissions and resilience) and OUT-11 (the fiscal and fairness tests).

| Section | Status |
| --- | --- |
| 1. The problem | Draft: `1-problem.md`. The trust fund's 2028 cliff, repair, the Interstate, buying power, deaths, slow grants, transit, rail, household cost and emissions; legacy facts traced or left out. Evidence EV-MOV-001 to 018 and 100 onward |
| 2. What works | Draft: `2-what-works.md`. Paying for roads (indexing, polling, per-mile and weight-mile experience), induced demand, safety countermeasures, transit relief and costs, European high-speed rail, failures to avoid |
| 3. Design choices | Draft, decided (`DEC-2026-11-10-08`): `3-design.md`. The baseline in 2029 as a working assumption with three cases; the 0.206% benchmark retired as a design rule (`DEC-2026-11-10-05`); six forks, each with a memo in `memos/`, sent as one batch (`memos/README.md`); eight yes-or-no points; all 28 legacy calls (A-1 to A-28) placed. Project-estimate figures EV-MOV-200 to 226 |
| 4. Specification | Draft (PR 3): `4-specification.md` and `provisions.json`, the four laws provision by provision (MOV-28.01; MOV-29.xx; MOV-30.xx; MOV-31.xx by division), with the decisions applied (memo 3's report in place of the benchmark trigger, memo 4's published reports, memo 5's published reports and review, point 1's contingency authorization, MOV-31.90), a design-lens note and a consistency table. Dropped legacy figures are in `restatement-log.md` |
| 5. Delivery | Draft (PR 3): `5-delivery.md`. Who runs what; a 2027-2044 timeline on the scenario calendar; capacity (Treasury collection, audits, FRA and FTA staff, states, agencies); getting money to projects; what the statute must say for a reluctant agency; remedies; where a state refuses; lessons |
| 6. Cost and financing | Draft (PR 3): `6-cost.md`. Each law's spending and revenue from the ledger; the general-fund draw by year on the transportation model; the fiscal-rule report: $473.0 billion over FY2030-39 as the budget model books it, and FY2040 permanent cost of $22.1 billion booked, $29.0 billion on the model's spending path, reported to the settlement; sensitivities; fairness. No adopted input changed |
| 7. Validation | Draft (PR 3): `7-validation.md`. The design against CBO, FHWA, the National Academies, the NTD, FRA, NEVI and state per-mile programs; what the models miss (demand response, construction costs, the baseline, CBO scoring); how it lands with housing, clean power, fair financing and the floor; reach; seven objections; failure signals |
| 8. What would change our minds | Draft (PR 3): `8-change-our-minds.md`. For each decision, the uncertainty, a threshold, who sees it and when, and the fallback; political and legal events; the fallback tiers; three hard stops; when the evidence arrives |
| 9. The public case | Draft (PR 3): `9-public-case.md`. A brief, the case in one paragraph, seven messages with the line each must not cross, hard questions, composite stories, a can-say list and a source table; only from sections 1-8 |

Evidence register: `evidence.json` (EV-MOV-001 to 099 section 1; 100 to 199 transit, rail and section 2; 200 to 299 project estimates from the legacy model). Source IDs numbered 3500 to 3599 are reserved for this dossier (the care dossier has SRC-3000 to 3399, per `dossiers/care/README.md`, the one home for care's range). Provisions: `provisions.json`, IDs under the agenda's MOV- rows (from section 4).

## Open questions for Espen

None open. Espen decided the memo set and the eight points as recommended on November 10, 2026 (`DEC-2026-11-10-08`). The open items left are for the settlement and the budget model, not decisions: the 2028 extension's transfer size, the FY2040 booking ($22.1 billion booked, $29.0 billion on the model's spending path; `6-cost.md`) and the household fuel-tax burden for the fairness test (`7-validation.md`).
