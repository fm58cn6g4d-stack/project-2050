# Transit / intercity rail split — framework handoff

> **Filed Oct 20, 2026** from the Surface Transportation claude.ai Project (`claude/transit-rail-split-framework.md`). Project paths are rewritten to their repo locations; the model scripts are in `index/tools/transportation/`. Where this file differs from `domains/transportation-moving-america-act-2031-draft-2.md` (Draft 2, canonical for MOV-), Draft 2 governs.


> **Numbers superseded 2026-10-12; the framework stands.** This was written on 2026-10-04 against the 55/45 split, a flat-real highway baseline and the wrong fiscal years. Three things have changed since: the baseline moved to H.R. 8870's highway levels, the trust fund moved to architecture C (floors plus a 35/50/15 split of the increment), and the authorization window was corrected to **FY2032-36**. The *reasoning* below — the flow-versus-stock asymmetry, transit gets a floor and rail the residual, rail bears the forecast risk, and the 49 U.S.C. 5307 question being the real hinge — is still the live contribution and is why this file is kept. The specific ratios and envelope figures are not; read them against `sources/transportation-arca-status-oct12.md` and `index/tools/transportation/transit_fiscal_model.py`.

## Why the split matters

The parity envelope is defined as **rail + transit as a share of highways**, converging to 1.00 by FY2045 (the glide path now reaches it in FY2042). It is a single combined number. Everything either bill claims about its own affordability depends on how that number divides.

Current figures, on H.R. 8870 highway levels and the corrected window:

- Combined envelope, FY2032-36: **$313.7B** (~$63B/yr average)
- Combined envelope, FY2037-46: **~$961.3B**

Against those, ATRA draws $224.42B and ARCA $254.03B, which is 1.53× the combined envelope between them — the build-out premium, discussed in the ARCA doc's fiscal-envelope section.

*(Superseded: the earlier figures were $279.6B and $854.7B, with rail's 45 percent share putting ARCA at 2.02× a $125.8B allotment.)*

## The structural asymmetry (the actual framework)

Transit and intercity rail do not have the same *kind* of claim, and the split should follow from that rather than from a negotiated percentage.

**Transit's need is a flow.** Its dominant driver is state of good repair — a backlog in the neighborhood of $180B that does not retire when funded. It is a maintenance treadmill that grows with the asset base. Add the post-2020 operating gaps at WMATA, BART, SEPTA, MTA and CTA. These obligations cannot be deferred a year without service failures.

**Intercity rail's need is a stock.** Its dominant driver is network construction: lumpy, front-loaded, and finite per corridor. CAHSR Phase 1 stops needing construction money when it is built. A project schedule can slip a year; an SGR backlog cannot.

Three consequences:

1. **Transit gets a floor; rail gets the residual.** Do not legislate percentages for transit. Build its floor in dollars from (a) formula base indexed, (b) a legislated SGR amortization schedule, (c) CIG at a stated level. Rail takes what the growing envelope leaves. Architecture C implements the first half of this — the FY2028 account floors are exactly that mechanism — but then legislates a percentage for the increment too, which is a departure from this framework and a deliberate one.
2. **Rail bears the forecast risk.** If the envelope grows slower than projected, rail absorbs the shortfall. This is both the politically necessary concession and the correct risk allocation, given the asymmetry above. Division A section 108's expansion-first trigger is where this now lives: rail's expansion programs are the largest expansion lines in the bill, so they give first.
3. **Rail's share should rise and then fall.** It cannot absorb a large early share — the corridor pipeline delivers 19 corridors by FY2031 in both the base and accelerated cases, because trains already funded and building cannot be accelerated. And rail construction tapers once the second-generation corridors complete (post-2046 on current modeling). Write the taper trigger into statute now even though it bites outside the window; it is what buys transit's consent to the surge.

## Where the numbers actually landed

The 60/40 recommendation below was not adopted. Architecture C legislates **35 / 50 / 15** of incremental fund receipts, which on the corrected window produces dedicated coverage of 73 percent for highways, 66 percent for transit and 27 percent for rail across FY2032-36. Equalizing coverage of each mode's renewal programs in FY2042-46 would give roughly **35 / 54 / 12** — highway's 35 percent is exactly right, and the open gap is four points of transit against four of rail. That gap is left for the EV fee redesign.

*(Superseded, kept for the reasoning: the anchors below were the basis for recommending 60/40 in the authorization period, converging to 55/45 later.)*

| Anchor | Transit / rail |
|---|---|
| FY2026 recurring ($16.3B / $2.6B) | 86 / 14 |
| IIJA-era (~$21.6B / ~$13.2B per year) | **~60 / 40** |
| Earlier ARCA assumption | 55 / 45 |

The IIJA ratio was the strongest single defensible number because it is observed behavior rather than an estimate, and the most recent occasion on which Congress funded both modes seriously. The 55/45 figure sat *outside* the plausible historical range — more rail-favorable than any precedent — which was the real weakness, not the margin of error. What replaced it is not a ratio at all but a floors-plus-increment structure, which is a better answer to the same problem.

## The one question that moves the split more than any need estimate

**49 U.S.C. 5307's bar on federal operating assistance for large urbanized areas.** This is a statutory question, not a funding-level question. On the corrected window, moving from scenario B (the drafted conditional tier) to scenario C (broad eligibility) takes the combined FY2032-36 draw from 0.174 to 0.190 percent of GDP and moves the split by about four points.

Resolve operating eligibility *before* fixing the split. Every need estimate downstream of it is conditional on the answer. It remains unresolved and is the first of the six merge blockers.

## Pressure-relief idea

Do not anchor on "transit = urban, rail = intercity." Every new ARCA corridor generates station-access demand, which is a rail-program interest. Division A section 109 now implements part of this for joint facilities — cost attribution by share of train movements — and the finding that commuter trains run 79 percent of movements at Chicago Union Station is what killed the old 30 percent transit-share placeholder. An explicit eligibility letting rail capital fund station-area access and feeder service beyond the terminals is still worth scoping.
