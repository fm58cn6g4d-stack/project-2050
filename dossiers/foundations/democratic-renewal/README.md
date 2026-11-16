# Foundation: democratic renewal

Role: the democratic renewal foundation (`charter/PLAN.md` 3.1): "a democracy and a government that work for the 21st century". Status: **draft, stage F, step 1 (section 1, the problem)**. Research only: Espen allowed stage F groundwork before the stage E boundary review on the condition that it makes no design choices (November 16). Nothing here recommends, decides or changes a level or status. Level: every item homed here is **L1** in `agenda/agenda.csv`, as the legacy files left it (`DEC-2026-10-30-03`).

**What it covers** (`charter/PLAN.md` 3.1, exactly): "The voting floor, money in politics, ethics, courts, participation, long-run institutional reform, and a government that delivers: agency capacity, payment systems, and remedies when delivery fails. Each flagship's delivery section states its own needs; this foundation owns the cross-cutting state capacity." Stage F sizes that capacity "to the specified flagships" (`charter/PLAN.md` 6, stage F).

## Scope

**Homed here** (`agenda/agenda.csv`, `home_dossier` = `foundations/democratic-renewal`): 118 rows, 75 policies and 43 options, all L1. The brief for this step counted 92; the CSV holds 118 (checked November 16).

| Family | Rows | Policies | Legacy design file | Ledger rows that carry them today |
| --- | --- | --- | --- | --- |
| DEM: representation, elections, civic life | 38 | DEM-1 to DEM-20 (DEM-14 and DEM-15 are pointers to SAF-8 and LAB-9) | `legacy/domains/domain-democracy.md` | DEM-1, DEM-3 to DEM-6, DEM-11, DEM-16, DEM-17 |
| INT: anti-corruption and money in politics | 27 | INT-1 to INT-17 | `legacy/domains/domain-integrity.md` | INT-1; INT-2 and INT-5 ride DEM-1 |
| CRT: courts and administrative law | 34 | CRT-1 to CRT-19, packaging options CRT-P1 to P4 | `legacy/domains/domain-courts.md` | CRT-P1 |
| CAP: Congress and the successor state | 19 | CAP-1 to CAP-18 and CAP-7S | `legacy/domains/domain-capacity.md` | CAP-7, CAP-7S, CAP-8 |

**Read with it, homed elsewhere:**
- **Executive power** (`agenda/executive-power`, wave three; `legacy/domains/domain-executive-power.md`). Two of its rows are delivery plumbing this foundation's capacity part depends on: EXE-3 (anti-impoundment, a cause of action for the intended recipient) and EXE-18 (payment continuity in a lapse of appropriations). EXE-5 (inspectors general) and EXE-9 (independent agencies after *Slaughter*) set the template the FEC (INT-7) and the immigration court (CRT-5) use.
- **Amendments** (`agenda/amendments`, wave three; `legacy/domains/domain-amendments.md`): AMD-1 (money in politics), AMD-2 (judicial terms), AMD-3 (popular vote, carrying DEM-9), AMD-5 (right to vote), AMD-9 (convention procedure).
- **Election-worker protection** is SAF-8 (`agenda/public-safety`); **national service** is LAB-9 (`work`).
- **CRT-5, the Article I immigration court**, is homed here; the immigration flagship states what the immigration system needs from it as requirements without designing the court (`dossiers/immigration/README.md`, "How CRT-5 meets this dossier").

**Outcomes it serves** (`charter/outcomes.md`): OUT-09, "a democracy people can influence, and a government that delivers" (its own); OUT-10, connection and civic participation (with work); and, through delivery, every flagship's outcomes (OUT-01 to OUT-07).

## Layout

One file per section, each with a part per subject, as the immigration and secure floor dossiers did, because the parts meet in the same institutions: the same Senate rules decide whether DEM-1, CRT-P1 and INT-1 pass at all (D2), and the same agencies carry every flagship's delivery.

| Section | File | Status |
| --- | --- | --- |
| 1. The problem | `1-problem.md`: parts A (voting floor and election administration), B (money in politics), C (ethics), D (courts), E (participation and civic life), F (long-run institutional reform), G (a government that delivers), with the flagships' stated state-capacity needs in G.6; the January 2029 baseline; inherited assumptions traced; evidence still needed | Draft (this PR) |
| Capacity inventory | `capacity-needs-inventory.md`: every state-capacity need the flagships' delivery sections specify (about 190), with file and line, the hand-offs to this foundation and the agencies shared across flagships; the source of section 1, G.6 | Draft (this PR) |
| 2-9 | Not started | Later stage F steps |
| Evidence register | `evidence.json`, `EV-DEM-001` to `EV-DEM-144` (119 data, 25 analysis; graded A 62, B 4, C 77, D 1); each entry labelled data or analysis and graded (`DEC-2026-10-28-07`, `DEC-2026-10-30-01`); sources `SRC-5500` to 5606 in `library/catalog.csv` | Draft (this PR) |

## IDs reserved

- **Evidence code:** `EV-DEM-`.
- **Source block:** `SRC-5500` to 5899 (`library/reserved-blocks.csv`).

## Directions for later stages (recorded, not acted on)

- **DEM-2's structure** (one provision, a severable bill, two bills, or the legacy DEM-2E: criteria and a three-judge backstop with commissions as a voluntary safe harbor) goes to this dossier's memo set (`charter/PROGRESS.md`, "Directions for later stages"; `dossiers/scenario/memo-defense-baseline-and-dem2.md`, choice b). Section 1 gathers the facts it will need (part F) and decides nothing.
- **D2, the Senate rules question**, stays with the scenario's 2027-28 questions (`dossiers/scenario/3-framework-2027-28.md`, question 4) and the legacy decision (F, graduated cloture; `legacy/governing/project-2050-governing-decisions.md`, D2). Section 1 records why it decides which of these items can pass, without reopening it.

## Open questions for Espen

None from section 1 itself; the questions it surfaces are listed in the PR's "For the board" and are not asked as decisions here.
