# Transit package — context notes from the ARCA products

> **Filed Oct 20, 2026** from the Surface Transportation claude.ai Project (`claude/transit-context-notes.md`). Project paths are rewritten to their repo locations; the model scripts are in `index/tools/transportation/`. Where this file differs from `domains/transportation-moving-america-act-2031-draft-2.md` (Draft 2, canonical for MOV-), Draft 2 governs.


Written 2026-10-04 after reading the ARCA bill architecture doc (rev 230, full text), the corridor pipeline grid (v8) and the network map. Not read: the embedded trust-fund cash-flow model and the doc's comment threads. Revised the same day after the transit model was built; see `sources/transportation-transit-package-status-oct12.md` for the package itself.

## What the rail work fixes that the transit package matches

- **Baseline is "BUILD America 250-Plus", not H.R. 8870 as reported.** The rail doc models a lame-duck compromise on top of H.R. 8870: rail $62.4B as reported -> $73.3B, $22B (30%) guaranteed, ~$60B delivered. The transit package uses the same four-column construction. H.R. 8870 transit as reported: $87.4B contract authority FY2027-31, no advance appropriations, CIG $3B/yr subject to appropriation.
- **Era bands used in the grid:** BUILD America 250-Plus FY2026-28, reconciliation FY2029-30, ARCA FY2031-35, FY2036 reauthorization FY2036-46. Map horizons 2036 / 2045 / 2055.
- **Doc skeleton mirrored:** what changed; real baseline; the 250-Plus compromise; reconciliation window with Byrd table; modeled FY2027-31 baseline; bottom-up need table; at a glance; fiscal envelope; titles with drafted text; one canonical authorization table; phasing; next decade; political path; fallback tiers; sources.
- **Visual system:** Archivo + Source Serif 4, paper/ink palette, light and dark tokens. Grid rows carry stage as cell colour, construction as an amber underline, service as a red edge.
- **Parity glide path:** rail + transit at 45% of highways FY2027-30, 75% FY2031-35, 90% FY2036-40, 100% FY2041-45; highways held flat-real from $62.657B.
- **Byrd drafting rule:** fund the program, do not amend it; conditions on the new money are allowed as "terms and conditions under which mandatory outlays are made".
- **Permitting:** formula apportionment plus State/local project selection is what escapes "predominant federal control"; the MAP-21 sec. 1316 right-of-way exemption already covers transit. CIG sits on the Tier 1 side of that line.

## Findings that bear on the transit design

1. **SEC. 101 writes rail's share and not transit's.** 101(c) gives rail 8/15/22/28% of amounts credited to the Fund. 101(d) only floors the Mass Transit Account at its FY2028 credited amount, indexed (about $7.5B in FY2031, about $10B in FY2041-45). On ARCA's revenue rows the fund is about $118B a year in FY2041-45; rail's aviation and diesel taxes sit on top of its 28% share. Dedicated coverage in FY2041-45 comes out at rail 101%, highways 79%, transit 16%. (An earlier version of this note back-solved a $175B fund and a $30B transit residual; that was wrong.)
2. **The 0.192%-of-GDP test has no transit growth in it,** and its rows could not be reproduced. All-in, ARCA alone runs 0.174% in FY2029-30 and 0.158% in FY2031-35 against reported 0.105% and 0.099%. The like-for-like cap is 0.206%.
3. **Two SEC. 101 texts coexist.** The reformed Surface Transportation Trust Fund text and the older standalone Intercity Passenger Rail Trust Fund text (IRC 9512) are both in the doc. The older text and sec. 109 bar any use for chapter 53 purposes. Secs. 107 and 601 still name the standalone fund.
4. **ARCA raises transit agencies' costs.** Sec. 1103 adds a state-of-good-repair component to NEC-style access charges; eight commuter authorities pay under that policy.
5. **Shared assets already in ARCA:** sec. 310 terminals, sec. 604 through-ticketing with transit agencies, sec. 1201 equipment pool, and three different Buy America thresholds (Amtrak >50%, FTA 70%, FRA 100%).
6. **Reconciliation overlap:** the rail $48.5B includes $3.0B "station access and ADA backlog".
7. **Highways denominator (verify):** H.R. 8870 reportedly guarantees FHWA $376B over FY2027-31 (~$75B/yr) against the envelope's $66.7B/yr for FY2027-30.

## Stale items seen on the rail side (for its own audit)

- Title II table still shows sec. 203 at $5.90B and sec. 205 at $6.65B (sums to $63.65B); canonical table has $4.70B and $4.15B ($59.95B).
- Title III table and the map footer show sec. 303 at $40B; canonical table has $55B.
- Coalition table still cites sec. 203 with a $1.2B set-aside and Texas at $8.2B.
- Grid notes still cite 49 U.S.C. 24911 as the operating-commitment chokepoint; the doc corrected this to 24712(g)(2).
- Cash-flow and scoring sections remain on the $185.43B program (already a known open item).
