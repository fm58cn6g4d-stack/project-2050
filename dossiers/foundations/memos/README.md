# Financing decision memos: the health batch

Role: the decision memos of the stage E settlement checkpoint (`../checkpoint-financing.md`, part B), one batch, sent together so Espen can decide it in one round. Status: **superseded, November 15, 2026, by [`../health-financing.md`](../health-financing.md) (its part 9 holds the new questions); kept for the record.** Earlier status: **for Espen's decision, November 14, 2026**; none decided. Each memo is decided on its own (`charter/STANDARDS.md`, "Decision memos"); a decision gets a `DEC-` entry from the lead, and any booking that follows is a tier-3 change to adopted inputs.

## The forks at a glance

| Memo | Question | Options | Recommended | FY2040 effect on the gap |
| --- | --- | --- | --- | --- |
| [F1](F1-household-contribution.md) | How households pay in place of premiums | A income contribution; B worker payroll; C income plus a VAT with a rebate | **A**: about 15.7% of income above $20,000/$40,000, with the income tax | Closes what F2 and F3 leave: about −$2,827B |
| [F2](F2-employer-side.md) | What employers pay | A 65%, then the same yield as a payroll contribution from 2036; B 65% of former premiums, never converted; C 100% of former premiums; D nothing | **A**: about 7.7% of pay from 2036 | −$1,060B (A, B); −$1,631B (C); $0 (D) |
| [F3](F3-states-share.md) | What share of their former Medicaid spending states keep paying | A 50% (working figure); B 80%; C 100%; D nothing | **B** | −$207B against A (C −$345B; D +$345B) |

Narrower points are the four yes-or-no points in `../checkpoint-financing.md`, part B4.

Together, at the recommendations, the batch closes the single plan's FY2040 net cost of $4,094B. Every bottom-four fifth comes out ahead on average: about +$6,700, +$10,700, +$11,100 and +$4,900 a household a year. The figures come from `models/tools/health_financing.py`, on the project's exploratory models, not an official score.

## What the batch rests on, and who decided it

| Assumption | Source | Decided by Espen? |
| --- | --- | --- |
| The plan's design: who is covered and when, the benefit, the 1.15 rate and its glide, the fund's streams | Care memos 1 to 5 (`DEC-2026-11-10-09` to `-13`), the status rule (`DEC-2026-11-12-19`), the hospitals' payment (`DEC-2026-11-13-02`) | Yes |
| An employer contribution until the settlement's payroll contribution; the states' maintenance of effort; the exclusion's end as a named stream | Care memo 3 B (`DEC-2026-11-10-11`) | Yes; the levels are the settlement's |
| 65% as the employer share | Care `6-cost.md`, part 4: the share at which employer moves cost the federal budget nothing | No: a working figure |
| The states' 50% | Care `6-cost.md`, part 4; HLT-7.17 | No: a working figure (range 0-80%) |
| Full pass-through of premium savings into pay | HX's convention (CBO's: total compensation fixed) | No: CBO's convention, tested at half (`../checkpoint-financing.md`, part B3) |
| Yields per point | The budget model's broad tier and payroll point (`models/tools/recovery-budget/assumptions.json`); the legacy VAT menu | No: authored translations of CBO and JCT options, before the 2025 law's rescoring |
| Household keys | The household model's measured keys on the 2029 CPS (`models/tools/household/keys.csv`), plus AGI above the line | No: model method (`MODEL-CARD.md`) |
| The fiscal rule tests the general fund in FY2040; dossiers report, the settlement balances | `DEC-2026-11-10-05`; D4 | Yes |
