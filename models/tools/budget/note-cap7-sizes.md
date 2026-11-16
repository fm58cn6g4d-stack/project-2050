# CAP-7S and CAP-7: what the budget model books

Role: a check of the agency-capacity rows against Espen's October 26 sizes, written for the board, after PR #397's finding. Status: finding, November 16, 2026. It changes no adopted input and no figure.

## The question

PR #397 found that `models/data/inputs/ledger-bills.csv` carries CAP-7S, the agency rebuild surge, at $560B (`fiscal-years.csv`, FY2030-35) and CAP-7, the sustained increase, at $455.7B over FY2030-39 (`fiscal-profiles.csv`, about 0.12% of GDP). Espen's October 26 decisions set about $105B lifetime for CAP-7S and keep CAP-7 at $300B over FY2030-39 as a planning ceiling (`legacy/governing/project-2050-governing-decisions.md`, "Capacity surge resized and FY2029 shift reduced", lines 510 and 521). Nothing later changes those sizes: no `DEC-` row in `charter/decisions.md` names CAP-7 or CAP-7S, and nothing in the legacy file after October 26 resizes them.

## What the model books

**The plan-wide gap already uses the October 26 sizes.** The ledger rows are the pre-October-26 amounts, but the budget model's central case (`models/tools/recovery-budget/model.py`, case `mixed`, the source of the plan-wide gap in `models/data/recovery-budget-paths.csv`) scales them down in its line "Smaller capacity and AI authorizations" (`model.py` line 217). It reads `recovery-adoption.json`'s `cap_surge_tn` 0.105 and `cap_sustained_tn` 0.3 against the original $0.6T and $0.49T, and the FY2029 shift (`early_admin_bn` 5) as its own line. From the audit lines (`legacy/sources/recovery-budget-audit.csv`, case `mixed`):

| Row | Ledger, FY2030-39 | Booked in the gap, FY2030-39 | Espen, October 26 | Booked in FY2040 |
| --- | --- | --- | --- | --- |
| CAP-7S | $560.0B | $98.0B (FY2030-35), plus the $5B shift into FY2029 | about $105B lifetime | $0 |
| CAP-7 | $456.0B | $279.2B | $300B ceiling | $37.2B |

The same line also takes AI-4 from $200B to $120B; the three reductions together are $718.8B over FY2030-39 and $35.3B in FY2040. So **the plan-wide gap does not carry about $0.6T of extra capacity spending.** Rebooking the ledger rows to $105B and $300B without also removing that line would count the reduction twice.

## The residual, and why it is a judgment call

The booked sizes sit $7.0B (CAP-7S) and $20.8B (CAP-7) below Espen's, about $2.8B in FY2040. The cause is the immigration booking (`DEC-2026-11-12-07`, point 9; `dossiers/immigration/6-cost.md` part 4), which removed USCIS's pro-rata share from the ledger rows before the scaling: $40B of $600B for CAP-7S, and 7% for CAP-7. The scaling then carries those proportions into the smaller sizes.

USCIS's own share of the reviewed allocation behind the October 26 sizes is smaller: about $3.5B of surge (backlog clearance and online filing) and about $0.02B a year sustained (`legacy/sources/capacity-recovery-components.csv`). The $105B is a ceiling covering the review's high case, not a sum of parts. Which figure the two decisions together imply is a choice:

- **A. Leave as booked** ($98.0B and $279.2B): the proportional reading. No change.
- **B. Book Espen's sizes less USCIS's reviewed share** (about $101.5B and about $299.8B): adds about $24B over FY2030-39 and about $3B in FY2040.
- **C. Book Espen's sizes exactly** ($105B and $300B), reading USCIS's removal as already outside the October 26 review: adds about $28B over FY2030-39 and $2.8B in FY2040.

The difference is about 0.5% of the plan-wide FY2040 gap. It is small enough to settle in stage G's audit rather than now.

## Clean-up, not a size change

Two things are stale but move no gap figure:
- The ledger's notes for CAP-7S and CAP-7 still describe $0.60T and about 0.12% of GDP as the working amounts, and `capacity-funding.csv` and `ledger-cuts.csv` C42 still say $0.6T.
- `fiscal-model.py`'s DEC scenario (`models/data/fiscal-paths.csv` and the D4 envelope tests) reads the ledger directly, so it does carry the larger sizes, about $639B more over FY2030-39 than the gap model.

Bringing the ledger rows to the booked sizes and dropping the CAP part of the scaling line would fix both with no change to the plan-wide gap. It is a tier-3 change to adopted inputs and model code, best done with stage G's audit or alongside option B or C.
