# MOD-housing: changelog

Role: the version history of the housing model (`models/schema/README.md`, "Versions"). Status: current. Newest first.

## 0.1.0 (2026-11-25)

First version (stage H step H7; memo H5 A, `DEC-2026-11-25-22`). Rebuilds `dossiers/home/6-cost.md` section 1.2 from its inputs (26 lines built, 9 taken as published), section 1.4's lease-up table, households reached by stage and income band, and the rent readings and supply range from the register. Inputs in `parameters.csv`, `plan.csv`, `published.csv` and `market.csv` on the toolkit's schema; results on the results schema; reproduction and benchmark tables written by the test code.

Results: first results. Housing $807.2 billion over FY2030-39 (6-cost.md: $806 billion, the sum of its rounded lines) and $120.8 billion in FY2040 (6-cost.md: $120 billion; booked $120.5 billion). No booked figure or adopted input changes.
