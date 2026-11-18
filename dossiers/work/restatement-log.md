# Work: restatement log

Role: what the dossier dropped or kept by reference from the legacy labor file on purpose, for the restatement check (`charter/PLAN.md` 4; `restatement.json`; `dossiers/TEMPLATE.md`, "Converting legacy content"). Status: written in the milestone review's fix step 4 (finding W-7).

The legacy file is `legacy/domains/domain-labor.md` (SRC-0025). Run `python3 models/registry/restatement.py legacy/domains/domain-labor.md <the dossier's files> --accounted dossiers/work/restatement-log.md`. The check lists 15 policy IDs and 3 numbers in the file that no dossier file contains; each is accounted for below, in backticks. The file's rows are otherwise restated: the options are weighed in memos 1 to 9, and every legacy choice stands as an option, not a decision (`DEC-2026-10-30-02`).

## Group 1: content the dossier changed or left out that the check does not flag

These carry numbers or definitions that the dossier states differently, so the check finds them "carried" by other uses of the same figures. The review (W-7) named them.

| Legacy content | Legacy line | What the dossier does | Why |
| --- | --- | --- | --- |
| LAB-9's offer to "every 18-to-26-year-old" | L157 | Not carried: LAB-9.01 to 9.06 state no age band, and memo 9 did not weigh one | Memo 9 chose a scale (150,000 civic positions, a gated tranche of 50,000) and not an eligibility band; AmeriCorps' own rules would apply unless the act says otherwise, which the register does not check. **Flagged, not decided:** an age band is a design choice for Espen if wanted (listed in the PR for the lead) |
| The standards boards' cost, "about zero to the general fund" (0.00 / 0.00 / 0.01) | L13, L76 | Replaced by memo 5's about $0.2-0.4 billion a year for the commission and boards office, and about $1-3 billion over the decade, labeled judgment (`4-specification.md`, "What each part costs"; `6-cost.md`) | The legacy figure counted no staff or board members; memo 5 priced the office. The legacy figure stays registered as EV-WRK-708 |
| The phase-in by firm size: "large firms (500+ workers or $1B+ revenue) over five years, the smallest over eight" | L84 | Not carried: one national schedule with no size tiers (memo 1 part 2, `DEC-2026-11-17-02`, `-34`), plus a credit for employers under 50 workers | The decision replaced the legacy size tiers with one schedule and a credit, so the 500-worker and $1 billion definitions have no job to do. The 50-worker credit threshold is the decision's own, not a restatement |

## Group 2: policy IDs that point to other files (15)

| Token(s) | Legacy line | What it is | Why it is not carried |
| --- | --- | --- | --- |
| `CRT-10` | L63 | Staging pointer for civil penalties sought in district court | The substance is carried in memo 3 B and LAB-2: penalties sought in district court with a jury available. The ID names a legacy staging item, not an agenda row |
| `EXE-9` | L65 | The executive-power file's structure for the Board | The substance (partisan balance, staggered terms, no removal protection) is carried in memo 3 and LAB-2.04; the ID is the other file's |
| `CRT-5` | L69 | The immigration-court model for LAB-2B's Article I labor court | LAB-2B was decided no (point 9, `DEC-2026-11-17-22`); LAB-2B itself is carried |
| `HLT-4` | L74 | The health file's Medicaid home care rate dependency | Home care's wage floor is carried through the care payer floor (memo 5 B, the care dossier), not through the health file's row |
| `HOU-3` `HOU-6` | L135 | Housing rows the construction apprentices supply | LAB-8 names four sectors, construction among them; the housing rows do not set LAB-8's line, so the dossier names the sector, not the other dossier's IDs |
| `CLI-1` `CLI-5` | L136 | Climate rows the energy apprenticeships serve | As above: the energy sector is named, not the rows |
| `FAM-2` | L137 | The family file's child care supply grants | As above: the care sector is named; and LAB-9's placements in child care are carried (LAB-9.01) |
| `EDU-4` | L143 | The education file's teacher apprenticeships | Counted in EDU-4, not in LAB-8 (the legacy file says so, L143) |
| `NSC-8` | L163 | Public-health and preparedness placements for service | LAB-9.01 names public health among the placements; the row ID is not needed |
| `DEM-11` | L164 | Election administration placements for service | LAB-9.01 names election administration; the ID is not needed |
| `AI-1` | L195 | The AI file's row that AI-11 rides | AI-11 is the AI file's row, listed in the legacy table for view; LAB-19 and the AI seams are in section 4 (`DEC-2026-11-17-96`) |
| `AI-5B` | L196 | An AI option that the legacy file calls "not a labor row" | Not a labor row, so the dossier does not carry it |
| `DEM-15` | L222 | The democracy file's pointer to LAB-9 | Pointer confirmed in `agenda/agenda.csv` (`DEC-2026-11-17-68`); the democratic renewal dossier holds it |

## Group 3: numbers (3)

| Token(s) | Legacy line | What it is | Why |
| --- | --- | --- | --- |
| `11.4` `15.1` | L3 | Rows of the staging inventory that the legacy file says it replaces "on substance" | Bookkeeping for the legacy consolidation, not policy or data |
| `4.1` | L63 | The staging inventory's row 4.10, with its trailing zero dropped by the check | As above |

## Group 4: should be carried

None other than the age band in group 1, which is a flagged question, not an omission to repair here.
