# Memo G9: Three small forks

**Decided:** G9.1 (a), `DEC-2026-11-20-12`; G9.2 A, `-13`; G9.3 B, the $100B line dropped and memo 10's contingency kept with guardrails, `-14` (guardrails in `../2-settlement.md` part 7.2). Booked in stage G step 7 (`../2-settlement.md`, `models/data/inputs/settlement.json`). The memo below is the record of the choice as put to Espen; its figures are the draft's.


Role: decision memo for Espen, fork 9 of stage G's batch ([`README.md`](README.md); [`../2-settlement.md`](../2-settlement.md) part 4; `../1-audit.md` part C, items 31-33). Status: **provisional, drafted on the recommendations, November 20, 2026.** Not decided, not booked. Each point is decided on its own. Together they move the FY2040 gap by under $3B.

## Point 1: what CRT-P1, the court bills, pays for

CRT-P1 books **$10.0B over FY2030-39 and $1.33B in FY2040** for the court bills: new judgeships, court integrity and terms. Its contents cost far less than that: about $0.4-0.6B for the judgeships and a few million dollars a year for the rest. The booking uses the room for the Article I immigration court's own structure (CRT-5.09): about $6.9B over the decade (range $3.2-9.7B) and $0.95B in FY2040 (`dossiers/foundations/democratic-renewal/6-cost.md` part 4).

- **(a) Keep CRT-P1 as booked, carrying the court's structure (recommended).** No change. The court's cost range ($3.2-9.7B) straddles the booking's room.
- **(b) Cut CRT-P1 to its contents** and book the court's structure as its own row. About −$2.5B over FY2030-39 (range −$6.3B to +$0.4B) and −$0.3B in FY2040.

**Recommendation: (a).** The court isn't specified yet, and its range runs both above and below the booking, so a cut now could need reversing. Revisit when the court's bill is drafted. The Article I court is inside CRT-P1, so it is not to be added again anywhere (`../1-audit.md` part B3).

## Point 2: the agency-capacity residual from #404

The booked capacity sizes are $98.0B of surge (CAP-7S) and $279.2B sustained (CAP-7). Espen's October 26 sizes were $105B and $300B. The difference ($7.0B and $20.8B, about $2.8B in FY2040) comes from how the immigration booking removed USCIS's share before the sizes were scaled (`models/tools/budget/note-cap7-sizes.md`).

- **A. Leave as booked (recommended).** No change.
- **B. Espen's sizes less USCIS's reviewed share** (about $101.5B and $299.8B): +$24.1B over FY2030-39, +$2.7B in FY2040.
- **C. Espen's sizes exactly:** +$27.8B and +$2.8B.

**Recommendation: A.** Democratic renewal's bottom-up allocation, agency by agency, fits inside the booked sizes with room to spare ($54.8B of surge and $249.5B sustained against $98.0B and $279.2B). So the extra money would buy nothing that has been identified.

## Point 3: the two delivery contingencies

The plan holds two reserves for delivery failures:
- **Memo 10's contingency** (democratic renewal): the money left inside CAP-7S and CAP-7 after the bottom-up allocation. It is released by OMB only against a written need. It is $78.5B on the booking's ramp. The dossier says $72.9B, on a different window.
- **The $100B `delivery_contingency` line** from the October 26 recovery decisions: $14.0B in FY2040, separate from CAP-7.

Neither has a written lane, so one delivery failure could draw on both (`../1-audit.md` part B3).

- **A. Keep both, with written lanes (recommended).** Memo 10's covers agency staffing and systems for the programs the capacity rows name. The $100B line covers delivery failures elsewhere: payment systems, state partners and the programs without a capacity row. Each release is published with its reason. No cost change.
- **B. Drop the $100B line** and rely on memo 10's: −$100B over FY2030-39 and −$14.0B in FY2040.
- **C. Merge them into one contingency** with one release rule: the same money, simpler to run.

**Recommendation: A.** The reviewer's note on #467 matters here. The long-term model's cautious reading (DEC-CAUT) now books the capacity rows at their adopted amounts, so it no longer carries any cost risk for agency capacity. These two contingencies are the plan's only cushion for delivery. B would save $14B a year, but at a moment when the plan is adding a large new tax (memo G3) and a national health budget, which are both delivery-heavy.

## Questions for you

- **G9.1.** Keep CRT-P1 as booked, carrying the immigration court's structure (reading (a), recommended), or cut it to its contents (b)?
- **G9.2.** Leave the capacity sizes as booked (A, recommended), or book B or C?
- **G9.3.** Keep both delivery contingencies with written lanes (A, recommended), drop the $100B line (B), or merge them (C)?
