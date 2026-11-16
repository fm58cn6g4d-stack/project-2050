# Memo 2: Repairing the Voting Rights Act, and the shape of DEM-1

Role: decision memo for Espen, fork 2 of the democratic renewal foundation (`../3-design.md`). Status: **awaiting Espen's decision**. Sources are named in plain text; bracketed tags point to `../evidence.json`. Agenda rows: DEM-1 Titles II and III, DEM-1A to 1D, DEM-1F (all L1). Answers section 2's question 3. D2, the Senate rules question, is read as a constraint and not decided here (`../README.md`).

**Decision line.** Recommended: **B, one bill with severable modules**: the floor (memo 1), a preclearance title written on a record of recent violations, and a Section 2 title in two parts, a results test restored and, separately, rules of proof that make an intent claim winnable under *Callais*, each able to stand if a court strikes another. Floor consideration by March 2029 and enactment by spring 2030 stay as the legacy timing. Cost: near zero in federal money (the Justice Department's review work, inside its budget); no outside score of preclearance alone exists. Evidence: one quasi-experimental study of preclearance; the holdings of *Shelby County* and *Callais*; contested legal readings.

## The question

What answers *Shelby County* (2013), which left preclearance inoperable, and *Louisiana v. Callais* (April 29, 2026), which limits Section 2 to cases with a strong inference of intentional discrimination [EV-DEM-011] [EV-DEM-007]? And does the answer travel in one bill with the voting floor or apart?

## Why it matters

- **Preclearance worked while it ran:** coverage under the 1975 revision raised long-run turnout 4 to 8 points through minority participation (Ang, American Economic Journal: Applied Economics, quasi-experimental; abstract read) [EV-DEM-157].
- **After *Callais*, existing districts are exposed:** CRS expects challenges to majority-minority districts drawn to comply with Section 2 [EV-DEM-008]; the Brennan Center counts three changes that make cases much harder to win [EV-DEM-009]; the Manhattan Institute argued the old framework, not the Act, was the problem [EV-DEM-010].
- **The 2031 maps are the deadline.** Whatever answers *Callais* must be law before states redraw after the 2030 census (legacy D1; `legacy/domains/domain-democracy.md`, line 80).

## The options

**A. One bill, as the legacy file writes it (DEM-1A, the working choice).** Titles I (floor), II (a new coverage formula), III (a results test restored, race-conscious remedies authorized, a Fifteenth Amendment record), IV (the match, memo 4).
- *For:* the floor's popularity carries the title with "the least independent constituency" (line 80); one floor fight under D2.
- *Against:* Title III restores a results test the Court has just read out of Section 2 on constitutional as well as statutory grounds; the legacy file says "no guarantee of judicial survival is claimed" (line 84).

**B. One bill, severable modules (recommended).** A's titles, with Title III written in two parts, as the legacy record's October 23 direction asks ("parallel restoration and intent/enforcement modules", line 366):
- III-A restores the results test, with findings on the current record;
- III-B, standing alone, sets rules of proof for intent claims (what evidence supports the "strong inference" *Callais* requires, discovery of map-drawers' data, a burden shift once a prima facie case is made), so relief survives if III-A falls;
- Title II's coverage formula rests on violations in a recent window and updates itself, which answers *Shelby County*'s objection to a frozen formula [EV-DEM-011].
- *For:* the same floor time as A; whatever a court strikes, the rest stands before 2031.
- *Against:* III-B is new drafting with no court test; a weaker message than "restore the Voting Rights Act".

**C. Split Title III into its own bill (DEM-1B).**
- *For:* the floor can move faster.
- *Against:* strands the piece with the 2031 deadline and the fewest votes behind it (line 91); a second floor fight under D2.

**D. Floor only, preclearance dropped (DEM-1C).**
- *For:* removes the hardest legal fight.
- *Against:* abandons the one remedy with a measured effect [EV-DEM-157].

**Add-on to A or B: DEM-1D**, a results test across the civil-rights code, not only Section 2 (line 93). *For:* a broader record. *Against:* broader exposure to the same constitutional objection. **Not recommended** now.

## What it costs, against outside scores

- **No score of the Voting Rights Advancement Act alone exists.** The House Judiciary Committee's 2019 report says it "requested but not received a formal cost estimate" (H. Rept. 116-317) [EV-DEM-323]. In 2022 CBO scored preclearance only inside the Freedom to Vote: John R. Lewis Act, which as a whole cut the deficit by $131 million over 2022-2031 (CBO and JCT, 2022) [EV-DEM-322].
- **The legacy estimate** gives Titles I-III no federal cost beyond the match (`domain-democracy.md`, line 82), a working assumption this memo keeps.

## Against the bills

| Bill | What it does | Against the recommendation |
| --- | --- | --- |
| John Lewis Voting Rights Advancement Act (2019, 2021) [EV-DEM-323] | Rolling coverage formula; practice-based preclearance | **Match** on Title II; written before *Callais* |
| Freedom to Vote: John R. Lewis Act (2022) [EV-DEM-322] | Floor plus preclearance in one bill | **Match** on one bill; B adds the intent module |
| Legacy DEM-1A | One bill, four titles | **Match**, with Title III split into severable parts |

## What it means for people

- *A Black voter in a district redrawn after *Callais*:* under A, relief depends on the restored results test surviving; under B, if it falls, an intent claim with the new rules of proof is still available before 2031; under D, nothing new.
- *A county election office in a newly covered state:* under A and B, changes to polling places are reviewed before they take effect; under C and D, not.

## Inherited assumptions, traced (not decided by Espen as designs, `DEC-2026-10-30-03`)

| Assumption | Where | Status |
| --- | --- | --- |
| One bill, DEM-1A | `domain-democracy.md`, lines 73-98 | Working choice |
| DEM-1F: floor by March 2029, enactment by spring 2030 | Lines 4, 96 | Adopted October 20 in the legacy record; a working choice (`agenda.csv` note) |
| No federal cost beyond the match | Line 82 | Working assumption |
| The 40-seat Talarico counterfactual behind DEM-1F | Line 96 | Scenario figure, not evidence; not used |

## Recommendation: B

- It keeps the one remedy with a measured effect [EV-DEM-157] and makes the *Callais* answer survive a partial loss, which the 2031 deadline requires.
- *Burden:* none on voters; on covered jurisdictions, review of changes.
- **What would change this:** a ruling before 2029 that also narrows intent claims (then III-B carries the record for an amendment, AMD-5); a Senate path that needs the floor alone (then C, with the risk named).

## If you decide

- Section 4 writes Titles II and III with severability clauses and findings; the courts' forum rules for challenges (CRT-3) apply.
- Yes-or-no point 3 in `../3-design.md` keeps DEM-1F's timing.

## Questions for you

1. A (one bill, legacy), B (one bill, severable modules, recommended), C (split Title III) or D (floor only)?
2. Add DEM-1D, the results test across the civil-rights code? (Recommended: no, for now.)
