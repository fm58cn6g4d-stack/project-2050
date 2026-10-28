# Moving America Act of 2031 — status (2026-10-12, night)

> **Filed Oct 20, 2026** from the Surface Transportation claude.ai Project (`claude/merge-status.md`). Project paths are rewritten to their repo locations; the model scripts are in `index/tools/transportation/`. Where this file differs from `domains/transportation-moving-america-act-2031-draft-2.md` (Draft 2, canonical for MOV-), Draft 2 governs.


Current doc: Draft 2, https://claude.ai/code/artifact/ccc503f2-81d0-4edc-937e-a11be3caf1ed. It supersedes the archived merge doc (https://claude.ai/code/artifact/6aae1b34-e426-48b0-8d3e-85b483b00918, rev 122) and the ARCA, ATRA and package docs wherever they conflict. Assumptions A-1 to A-28; Draft 2's table gives each old tag.

Governing figures come from `index/tools/transportation/final_v3.py` (fossil premium + 40-mpg clean-car peg + PHEVs at 30%), built on `fossil_final.py`, `fossil_premium.py`, `final_bill.py`, `revenue_plan.py`, `final_architecture.py`, `merge_decisions.py` and `transit_fiscal_model.py`. The model file itself still carries superseded settings; fold the overlays in.

## Design
- Revenue: fuel taxes permanent and CPI-indexed from FY2030 + ten 3-cent Fix-It-First steps (2029 $) with a deferring price pause; clean-vehicle per-mile charge at parity with the ROAD-USE rate pegged to a 40-mpg car (gas road-use rate / 40; diesel road-use rate / 6.5 for trucks; PHEVs 30%) from Oct 1, 2030, so no clean car pays more per mile than a 40-mpg hybrid; weight-distance charge (3-cent Class 7-8 avg) replacing the use tax; truck/tire excises permanent, 4% for ZE trucks; rail diesel 15/7.5 by STB class; aviation surcharge $4 -> $16; EV fee FY2030 bridge; corridor surcharge dropped.
- Fossil transition premium (A-28): five 2-cent steps FY2040-44 on gasoline and diesel only; enacted in the 2029 act; credited by general-fund need.
- Shares 35/50/15 through FY2036, 45/40/15 from FY2037.
- Vehicles: 2028 extension; 2029 act (package $47.0B, top-ups $209.74B, net deficit reduction ~$33.3B); 2030 act (package $33.5B, top-ups $57.33B, ~$4.2B); 2031 bill.
- Division B: IBR (1104, $30.77B), fix-it-first (1106), Safe System (1109), resilience 4% NHPP + CRP restored at 2% of formula + CMAQ alt-fuel 10% (1110), 1112 GF grants $17.24B, truck parking, 91k-lb pilot ends, 1116 Charging Gap Program replacing NEVI.

## Governing figures (FY2032-36)
- Program $936.57B (461.12 / 221.42 / 254.03). Dedicated $545.84B (321.19 / 154.27 / 70.38); GF $390.73B = $123.66B expansion + $267.07B top-ups (139.93 / 36.69 / 90.45).
- Draw 0.180% avg, 0.200% peak (FY2032); all-in FY2032 0.208% (0.002 over benchmark, accepted). FY2029-31 0.194 / 0.225 / 0.215%.
- FY2037-41 0.067%; FY2042-46 0.026% ($17.1B/yr); renewal coverage FY2042-46 95 / 109 / 135; self-sufficient renewal transit FY2036, rail FY2040.

## Biggest open items
2028 extension transfer sizing; cash-flow model; CBO/JCT score; demand response to steps and premium; PHEV share of plug-in stock (assumed 20%); division B against H.R. 8870 as enacted; sec. 1104 apportionment data; sec. 1116 gap map.
