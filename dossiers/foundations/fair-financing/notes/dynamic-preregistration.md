# The fiscal path review's dynamic layer: pre-registration

Role: the parameters, ranges and sources of stage G step 8a's contained dynamic layer, written and committed **before any debt path was run with them** (the guardrail in step 8a's brief). The values live in [`models/tools/fiscal_dynamic_params.json`](../../../../models/tools/fiscal_dynamic_params.json); this note says where each comes from and where it departs from CBO and JCT. Status: registered November 24, 2026, stage G step 8a. A change after the first run is a new registration: add a dated line under "Changes after registration" with the reason, and leave the old values in Git. Read with [`../4-fiscal-path.md`](../4-fiscal-path.md) part 2.

## The rules this layer keeps

1. **Beside, never instead.** Every figure is shown next to the conventional score (`fiscal_path.py`), which stays the reading of record. Nothing here enters the ledger, the gap, D3 or D4.
2. **The hard rule.** A debt goal the review recommends must be met on the conventional score, with zero dynamic or "works as designed" savings. These may only widen the margin, or lower a rate later through a trigger once the effect shows up in measured results (receipts, employment, the trustees' health spending).
3. **Symmetry.** The rate and crowding-out feedback applies to the current-law baseline as well as to the plan. The budget model's `ASM-RATE-NOFEEDBACK` leaves it out of both, so turning it on for the plan alone would flatter the plan.
4. **The negatives are counted with the positives**, and the central net is whatever the numbers give.
5. **Anchored to CBO and JCT,** whose published dynamic estimates are usually small. Every departure is named below.
6. **An independent red team.** The layer needs a red-team review by an agent that did not write it before any figure from it reaches Espen as more than a sensitivity.

## A. The symmetric feedback: debt, interest rates and output

Applied the same way to the baseline and to the plan. **Two readings:**
- **A, from the FY2029 debt ratio (107.4% of GDP),** as the brief asks. CBO's long-term projection already carries some debt feedback of its own, so reading A counts part of it again for both paths. Its levels overstate both, and the gap between them is the useful figure.
- **B, from CBO's own baseline debt path.** Only the plan's difference from current law gets the feedback, so the baseline doesn't move. This is the cleaner reading of what the plan changes.

| Parameter | Low | Central | High | Source and reasoning |
| --- | --- | --- | --- | --- |
| Interest rates, basis points per point of debt-to-GDP | 1 | 2 | 3 | CBO's working paper 2019-01 (publication 55018): about 2 to 3 basis points per point of debt, the average long-run effect. The Dallas Fed's 2025 working paper 2513 finds about 3. The Yale Budget Lab uses 2. The low end allows for the reserve-currency demand that keeps US rates less sensitive to debt than the literature's average. The rate change reaches the average rate on the debt over about 5.9 years, Treasury's average time to repricing (`ASM-RATE-ROLLOVER`). |
| Output, % of GDP per point of debt-to-GDP (long run) | 0.01 | 0.02 | 0.035 | CBO's long-term outlooks assume each dollar of added debt displaces about a third of a dollar of private capital (CBO, *The Macroeconomic and Budgetary Effects of Federal Investment*, June 2016, publication 51628, and the long-term outlooks' crowding-out convention). At a net return on capital of about 6%, that is about 0.02% of GDP per point of debt. The range runs from a quarter of a dollar at 4% to half a dollar at 7%. Output moves toward its long-run level by 10% of the remaining distance a year, since capital accumulates slowly. |
| Budget effect of a change in GDP | 0.25 | 0.25 | 0.25 | Revenue is about 18% of GDP. CBO's rules of thumb (publication 62257, Table 2) add mandatory spending and interest effects that put the deficit's response near a quarter of the GDP change. One value, not a range: it scales the other ranges. |

**The FY2036-39 crowding out** isn't its own parameter. Those years' deficits raise the debt ratio, and the output channel charges them for it, in the plan and the baseline alike.

## B. The plan's own channels (the plan only)

Each is a budget effect at FY2040, % of GDP (+ lowers the deficit), phased in from its start. Its GDP effect for the debt ratio's denominator is the budget effect over 0.25. "DY" rows are the legacy dynamic table (`models/data/inputs/ledger-dynamic.csv`), restated here with their IDs. The table is an adopted input and isn't changed.

| ID | Channel | Low | Central | High | Phase-in | Anchor, and where it departs |
| --- | --- | --- | --- | --- | --- | --- |
| P-CARE | Child care, pre-K, paid leave: parents' employment | +0.03 | +0.08 | +0.15 | FY2030, 6 years | DY6 (+$0.45T over FY2030-39 at its mid; `domain-education.md`'s $25-45B a year at maturity, scaled 2.04 with FAM-2's booking). DY6 calls itself an upper reading, so the central is below it. CBO has published no dynamic score of universal child care. Quebec's program raised mothers' employment by about 8 points (Lefebvre and Merrigan 2008, SRC-3032). **Departs from CBO:** CBO's child care cost estimates are conventional. |
| P-HEALTHWORK | Coverage not tied to a job; premiums turned into wages | 0.00 | +0.02 | +0.05 | FY2035, 3 years | No CBO or JCT score counts it. Kept small, and zero at the low end. |
| N-HEALTHCOV | Fuller coverage lowers labor supply (CBO's ACA convention) | −0.08 | −0.04 | −0.01 | FY2031, 5 years | DY2 (−$0.15T over FY2030-39). CBO's 2014 ACA estimate: about 1.5-2.0% fewer hours by 2024, from subsidies phasing out and the tax on high-cost plans (CBO, *The Budget and Economic Outlook: 2014 to 2024*, appendix C). Follows CBO. |
| N-CONTRIB | The 3.80% contribution's marginal rate on earnings | −0.20 | −0.10 | −0.04 | FY2035, 2 years | A 3.80% charge on AGI raises the marginal rate on most workers' earnings by up to 3.8 points. The premiums it replaces are not a marginal charge. At CBO's range of labor-supply elasticities (about 0.1 to 0.3 for total hours and earnings; CBO working paper 2012-12), earnings fall about 0.3-1.2%. That costs about $40-110B a year in FY2040 at the federal marginal rate, net of what the 2.25% already booked would have done. Follows CBO's labor-supply approach. |
| N-TOP | The top-rate stack and corporate rows: labor, saving, investment | −0.25 | −0.12 | −0.05 | FY2030, 5 years | DY1 (−$0.6T over FY2030-39 at its mid, recorded "from memory"). The new anchors: JCT's dynamic analysis of the 2017 tax law (JCX-69-17) raised average GDP by about 0.7% and recovered roughly a quarter to a third of its conventional cost (to confirm against the PDF). CBO's dynamic estimate of the 2025 law found its growth effect outweighed by higher interest rates: dynamic effects added about $125B through 2034 (CRFB's summary of CBO's figures; CBO working paper 61257). Raising these taxes reverses part of that, at a smaller share, because conventional scores and the GX and HCU allowances already count avoidance. The central is about 6% of the FY2040 top-end and corporate revenue (about $1.1T, `2-settlement.md` part 1), the low about 12%, the high about 3%. |
| N-WEALTH | The wealth tax: avoidance and saving at the top beyond its allowance | −0.06 | −0.02 | 0.00 | FY2032, 3 years | The booked yield already carries an avoidance allowance, and the stack cap (S04) limits it. The low end is about half of HS2's net FY2040 yield again, for Saez and Zucman's low avoidance against Summers's high. There is no CBO or JCT dynamic score of a wealth tax. |
| P-IMM | Immigration: legalization raises measured employment and wages | +0.01 | +0.03 | +0.06 | FY2030, 6 years | DY8 (+$0.06T over FY2030-39). CBO's 2013 S.744 estimate: $197B of deficit reduction with labor-supply effects against $175B without. CBO's July 2024 estimate of the immigration surge: −$0.9T over 2024-34, with GDP 3.2% higher in 2034 (publication 60165). The plan's legalization adds fewer workers than a surge, so it is smaller. |
| P-WORK | Work: paid on-ramps and participation, beyond LAB-1 | 0.00 | +0.01 | +0.02 | FY2030, 5 years | The floor's own indirect effect is booked in LAB-1 (CBO's 2021 score), so it is not counted here. DY4 is zero for the same reason. |
| P-INVEST | Clean power, infrastructure, R&D: productivity | 0.00 | +0.02 | +0.05; FY2056 +0.02 / +0.06 / +0.12 | FY2030, 10 years, rising to FY2056 | DY7 (+$0.12T over FY2030-39). CBO 2016 (publication 51628): federal investment returns about 5% a year on average, half of private investment's. About a third of it is offset by lower state, local and private investment, and the gains come mostly after a decade. Follows CBO. |

**The central net of the plan's channels at FY2040 is about −0.12% of GDP:** a small cost, not a gain, before the symmetric feedback. That is in line with CBO's and JCT's usually small dynamic estimates. The registered values give it; it isn't tuned to a result.

## C. Health "works as designed": WAD-H1

Espen allows a labeled "works as designed" health saving with a range (`DEC-2026-11-24-14`, direction 1). It is not a dynamic effect, and it is never counted toward a debt goal.

- **What:** the single plan's gross cost grows 0 / 0.25 / 0.5 points a year below D2's cap (GDP + 1 point from FY2037), from FY2037.
- **The D2 check:** D2 is booked: the national budget holds the plan's gross cost to GDP + 1, −$249.4B in FY2040 and −$526.3B in FY2056 (`packages.opt_without_d2`, HLT-7's `national-budget` component). WAD-H1 is measured against the D2-held path (gross $7,681B in FY2040, `health_booking.corrected()`, grown at GDP + 1 after FY2040). It counts only spending below the cap, so none of D2's saving is counted twice. **If D2 fails, WAD-H1 fails with it.** Its saving is conditional on D2 and can't be added to the backstop's case (G13).
- **What it isn't:** D1 (administration at 4%) and D5 (drug prices) are booked components. WAD-H1 adds nothing for them.
- **Why the range:** D2 itself has never been done (EV-CAR-742). Growth below it is the wishful end Espen allowed, so the low end is zero.

## D. What the layer reports

- Debt held by the public, % of GDP, for FY2040, FY2050 and FY2056, for the baseline and the plan, on readings A and B: conventional, central, pessimistic (every channel low, feedback high) and optimistic (every channel high, feedback low).
- Each channel's FY2040 and FY2056 budget effect, so no single line hides in a net.
- WAD-H1 on its own line, never summed into the dynamic net.
- For each debt goal, the conventional share of GDP needed next to what the dynamic central and pessimistic cases would need. Under the hard rule, the conventional share is the recommendation.

## Changes after registration

None.
