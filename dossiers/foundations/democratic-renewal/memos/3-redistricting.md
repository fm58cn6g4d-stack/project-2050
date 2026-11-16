# Memo 3: How DEM-2, redistricting, is written

Role: decision memo for Espen, fork 3 of the democratic renewal foundation (`../3-design.md`). It takes up choice (b) of the scenario memo (`dossiers/scenario/memo-defense-baseline-and-dem2.md`, lines 48-108), which the board's "Directions for later stages" sends here. Status: **awaiting Espen's decision**. Sources are named in plain text; bracketed tags point to `../evidence.json`. Agenda rows: DEM-2, DEM-2A to 2E (all L1). Answers section 2's question 9.

**Decision line.** Recommended: **D, the legacy DEM-2E written as three severable titles**: (I) a ban on mid-decade congressional redistricting from enactment, with an exception for a redraw Congress itself orders (the 2034 House-size package); (II) federal criteria, with traditional neutral criteria in one section and a measurable partisan-fairness test in a separate, severable one; (III) a three-judge federal court that hears challenges on a fast track and draws a remedial map where a state's fails, with independent commissions meeting set standards as a safe harbor rather than a mandate. Cost: about zero (commission start-up grants, legacy estimate up to $0.01 trillion). Evidence: commission studies that disagree on size, a 2021 review that finds final authority is what matters, the *Arizona* holding, and the scenario dossier's model.

## The question

The legacy DEM-2 mandates independent commissions for congressional maps under the Elections Clause and bans mid-decade redraws (`legacy/domains/domain-democracy.md`, lines 104-126). Should it be written so its parts stand separately, and should the commission mandate be in it at all?

## Why it matters

- **The parts carry different legal risk** (scenario memo, line 56; analysis): the ban is a "times, places and manner" rule of the kind Congress already makes; criteria are workable in statute after *Rucho*; a commission mandate faces the argument that "Legislature" means the legislature. *Arizona State Legislature v. AIRC* (2015) let a state's voters choose a commission; it did not decide whether Congress may impose one, and two of its four dissenters and the Chief Justice, who wrote the principal dissent, still sit [EV-DEM-262].
- **The value sits in the criteria.** The scenario dossier's model puts Titles I-II at about +7 Democratic House seats on the 2032 maps (10th-90th percentile +2 to +11), with the ban alone adding about zero to them (scenario memo, line 58; analysis, the project's own model).
- **Design matters more than the label.** Commissions with final authority, balanced membership and binding review drew less biased maps in 2021; advisory or one-party commissions were often overridden (Wang and Sippy, 2021 cycle review) [EV-DEM-261]. California's commission maps were more competitive than the 2001 legislative maps (Kogan and McGhee) [EV-DEM-259], which a simulation study contests (as reported) [EV-DEM-260].

## The options (the scenario memo's four, restated)

**A. One provision, as the legacy file writes it (DEM-2A, the working choice).** Commissions mandated, plus the ban with the 2034 exception.
- *For:* the reform that most changes who draws the maps.
- *Against:* if a court strikes the mandate without severability, the ban may fall with it, and the 2031 maps are drawn by whoever won in 2030.

**B. One bill, severable, in order of risk.** Title I the ban, Title II criteria, Title III the mandate; each stands alone.
- *For:* the low-risk value survives; same floor time.
- *Against:* a mandate enacted in 2029-30 would very likely still be in court when states draw in 2031 (census data arrive in spring 2031), so states that oppose it would wait (scenario memo, line 87).

**C. Two bills: the ban and criteria first, commissions later.**
- *For:* the ban has bipartisan precedent (CRS counts about 70 bills since the mid-2000s; scenario memo, line 59) and could move sooner.
- *Against:* two fights under D2; commissions may never get their own slot before 2031.

**D. Criteria and a court backstop, commissions as a safe harbor (legacy DEM-2E; recommended).** Title I the ban; Title II criteria, split internally so a struck fairness test leaves the neutral criteria; Title III a three-judge court on a fast track (the existing 28 U.S.C. 2284 form) that draws a remedial map where a state's fails, with a commission map that meets set standards presumed compliant. No state is ordered to create a commission.
- *For:* there is no mandate for a court to strike, so the law is settled before 2031 if Titles I-II hold; it rewards the commission design the 2021 review found works [EV-DEM-261].
- *Against:* fewer states will have commissions; the fairness test is new and its enforcement rests on federal courts.

**Add-on: DEM-2D** (conditional funding for state legislative maps). Spending-power exposure under *NFIB*; the legacy file holds it as a state track (line 112). **Not recommended.**

## What it costs, against outside scores

About zero: commission start-up grants only (legacy, up to $0.01 trillion, estimate; line 110). No CBO score of a stand-alone redistricting bill was found; DEM-2 is carried inside the ledger's DEM-1 row (`models/data/inputs/ledger-bills.csv`).

## Against the bills

| Bill or design | What it does | Against the recommendation |
| --- | --- | --- |
| Fair Representation Act (117th Congress) [EV-DEM-258] | Ranked-choice multi-member districts and independent commissions | **Diverge:** commissions mandated; that act's districts are memo 13 |
| Bipartisan mid-decade bans (CRS count; a House bill with five Republican cosponsors, effective after November 2032; scenario memo, line 59) | Ban only | **Match** on Title I; D applies it from enactment, through the 2031 cycle |
| Legacy DEM-2A | Mandate plus ban | **Diverge:** mandate replaced by safe harbor |
| Legacy DEM-2E | Criteria, backstop, safe harbor | **Match**, with the ban and the internal split added |

## What it means for people

- *A voter in a state whose legislature draws to entrench itself:* under D, a fast-track federal court tests the map against published criteria before 2032 and can replace it; under A or B, the outcome may wait on the mandate's litigation.
- *A state that already has a commission:* nothing changes under D except the presumption that its map complies.

## Inherited assumptions, traced (not decided by Espen as designs, `DEC-2026-10-30-03`)

| Assumption | Where | Status |
| --- | --- | --- |
| Commission mandate plus ban (DEM-2A) | `domain-democracy.md`, lines 104-120 | Working choice |
| The 2034 exception | Line 108 | Follows from the legacy second-term package (memo 13); a working choice |
| DEM-2E open | Line 16 | Open option |
| +7 seats from Titles I-II | Scenario memo, line 58 | The scenario dossier's model (analysis; "figures may move") |

## Recommendation: D

- It keeps the value (the criteria) and removes the part most likely to be in court during the 2031 redraw.
- *Burden:* none on voters; on states, published criteria and a court test.
- **What would change this:** a ruling before 2029 confirming Congress may mandate commissions (then B, with Title III effective for the 2041 cycle, as the scenario memo suggests).
- **A related change, not made here:** legacy D1 makes the 2033 House conditional on DEM-1 and DEM-2 in force before 2031; under D it would read "DEM-2's criteria (Title II) in force". That wording is a tier-3 change to a legacy decision and goes in a separate PR after Espen decides.

## Questions for you

1. A (mandate, legacy), B (severable mandate), C (two bills) or D (criteria, backstop and safe harbor, recommended)?
2. Apply the ban from enactment through the 2031 cycle, which also freezes the 2025-26 maps until then (recommended), or from 2032?
