# Transit / intercity rail split — framework handoff

> **Filed Oct 20, 2026** from the Surface Transportation claude.ai Project (`claude/transit-rail-split-framework.md`). Project paths are rewritten to their repo locations; the model scripts are in `index/tools/transportation/`. Where this file differs from `domains/transportation-moving-america-act-2031-draft-2.md` (Draft 2, canonical for MOV-), Draft 2 governs.


> **The framework stands; the figures are Draft 2's.** The baseline is H.R. 8870's highway levels, the trust fund uses architecture C (account floors plus a legislated split of the increment) and the authorization window is **FY2032-36**. The *reasoning* below — the flow-versus-stock asymmetry, transit gets a floor and rail the residual, rail bears the forecast risk, and the 49 U.S.C. 5307 question being the real hinge — is the live contribution and is why this file is kept. Figures come from Draft 2 and `index/tools/transportation/moving_america.py`; where they differ, Draft 2 governs.

## Why the split matters

The parity envelope is defined as **rail + transit as a share of highways**, converging to 1.00 by FY2045 (the glide path reaches it in FY2042). It is a single combined number. Parity is a policy statement and a target date, not a binding test: the binding tests are renewal programs covered by dedicated revenue, the general-fund benchmark (0.206% of GDP), and expansion giving way first under division A section 108. How the envelope divides still frames the split.

On H.R. 8870 highway levels and the FY2032-36 window:

- Combined envelope, FY2032-36: **$313.7B** (~$63B/yr average)
- Combined envelope, FY2037-46: **~$961.3B**

Against those, Draft 2's transit division is $221.42B and ARCA's rail division $254.03B, about 1.52× the combined envelope between them — the build-out premium, discussed in the ARCA doc's fiscal-envelope section.

## The structural asymmetry (the actual framework)

Transit and intercity rail do not have the same *kind* of claim, and the split should follow from that rather than from a negotiated percentage.

**Transit's need is a flow.** Its dominant driver is state of good repair — a backlog in the neighborhood of $180B that does not retire when funded. It is a maintenance treadmill that grows with the asset base. Add the post-2020 operating gaps at WMATA, BART, SEPTA, MTA and CTA. These obligations cannot be deferred a year without service failures.

**Intercity rail's need is a stock.** Its dominant driver is network construction: lumpy, front-loaded, and finite per corridor. CAHSR Phase 1 stops needing construction money when it is built. A project schedule can slip a year; an SGR backlog cannot.

Three consequences:

1. **Transit gets a floor; rail gets the residual.** Do not legislate percentages for transit. Build its floor in dollars from (a) formula base indexed, (b) a legislated SGR amortization schedule, (c) CIG at a stated level. Rail takes what the growing envelope leaves. Architecture C implements the first half of this — the FY2028 account floors are exactly that mechanism — but then legislates a percentage for the increment too (35 / 50 / 15 through FY2036, 45 / 40 / 15 from FY2037), which is a departure from this framework and a deliberate one.
2. **Rail bears the forecast risk.** If the envelope grows slower than projected, rail absorbs the shortfall. This is both the politically necessary concession and the correct risk allocation, given the asymmetry above. Division A section 108's expansion-first trigger is where this lives: rail's expansion programs are the largest expansion lines in the bill, so they give first.
3. **Rail's share should rise and then fall.** It cannot absorb a large early share — the corridor pipeline delivers 19 corridors by FY2031 in both the base and accelerated cases, because trains already funded and building cannot be accelerated. And rail construction tapers once the second-generation corridors complete (post-2046 on current modeling). Write the taper trigger into statute now even though it bites outside the window; it is what buys transit's consent to the surge.

## Where the numbers actually landed

The 60/40 recommendation below was not adopted. Architecture C legislates **35 / 50 / 15** of incremental fund receipts through FY2036 (Draft 2, A-7) and **45 / 40 / 15** from FY2037 (A-8). Across FY2032-36 dedicated receipts cover 70 percent of the highway program, 70 percent of transit and 28 percent of rail (renewal coverage 70 / 81 / 44). The equal-coverage solve, the alternative to A-7, is **50.0 / 38.2 / 11.8**. The FY2037 shift is what keeps transit from stranding receipts while highway renewal lags; with it, renewal coverage reaches 95 / 109 / 135 in FY2042-46.

The anchors below were the basis for this framework's 60/40 recommendation for the authorization period, converging to 55/45 later; they are kept for the reasoning.

| Anchor | Transit / rail |
|---|---|
| FY2026 recurring ($16.3B / $2.6B) | 86 / 14 |
| IIJA-era (~$21.6B / ~$13.2B per year) | **~60 / 40** |
| Earlier ARCA assumption | 55 / 45 |

The IIJA ratio was the strongest single defensible number because it is observed behavior rather than an estimate, and the most recent occasion on which Congress funded both modes seriously. The 55/45 figure sat *outside* the plausible historical range — more rail-favorable than any precedent — which was the real weakness, not the margin of error. What replaced it is not a ratio at all but a floors-plus-increment structure, which is a better answer to the same problem.

## The one question that moves the split more than any need estimate

**49 U.S.C. 5307's bar on federal operating assistance for large urbanized areas.** This is a statutory question, not a funding-level question. Moving from scenario B (the drafted conditional tier, $35.00B) to scenario C (broad eligibility, $70.00B) takes the FY2032-36 general-fund draw from 0.180 to 0.196 percent of GDP on average.

Resolve operating eligibility *before* fixing the split: every need estimate downstream of it is conditional on the answer. Draft 2 resolves it with scenario B, a conditional operating tier through a new 5307(i) (A-3); scenario C is the alternative.

## Pressure-relief idea

Do not anchor on "transit = urban, rail = intercity." Every new ARCA corridor generates station-access demand, which is a rail-program interest. Division A section 109 implements part of this for joint facilities — cost attribution by share of train movements; at Chicago Union Station commuter trains run 79 percent of movements, and the transit share is attributed on that count. An explicit eligibility letting rail capital fund station-area access and feeder service beyond the terminals is still worth scoping.
