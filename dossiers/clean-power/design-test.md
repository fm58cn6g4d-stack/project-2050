# Clean power: the decided package tested on the energy model

Role: the design-improvement step Espen asked for after the booking (lead's handoff, November 14): use the energy model (MOD-energy, `models/tools/energy/`) alongside the dossier's external evidence to test the decided package and look for stronger or cheaper designs. Status: first pass, on the model's committed runs (`results.json`, main at `ed0766a`, after #359). No new model runs; the model is M4's. Any change to a decided item goes to Espen as a decision memo: one so far, memo 8.

## The runs, side by side

Energy CO2 and net greenhouse gases below 2005; clean share of generation; national retail price (2025 cents a kWh); nominal $ billion over FY2030-39. Cumulative energy CO2 2030-50 against the decided set, Mt (trapezoid over 2030, 2035, 2040 and 2050; project arithmetic on `results.json`).

| Run | CO2 2035 | GHG 2050 | Clean 2040 | Price 2040 | Credits FY2030-39 | Standard's payments | Cumulative CO2 vs decided |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2029 current law | 27% | 38% | 60% | 14.7 | 0 | 0 | — |
| **The decided set** | **41%** | **67%** | **87%** | **16.1** | **1,037** | **163** | — |
| Builder everywhere (memo 4 A, full strength) | 42% | 68% | 92% | 15.5 | 1,172 | 93 | −1,458 |
| Decided set with the permitting package | 42% | 69% | 94% | 15.6 | 1,125 | 74 | −2,159 |
| Standby builder at 25% | 40% | 67% | 85% | 16.3 | 967 | 199 | +864 |
| Economy-wide price (memo 1 A) | 42% | 69% | 87% | 16.1 | 1,041 | 175 | −1,258 |
| Price repealed from 2033 (durability) | 37% | 61% | 83% | 15.3 | 986 | 253 | +5,395 |

Layer by layer, the clean electricity standard (80% by 2035, 100% by 2040) moves energy CO2 from 39.1% to 39.0% below 2005 in 2035 and cuts about 255 Mt over 2030-50, while suppliers pay about $193 billion over FY2030-39 at that layer and the 2040 price rises from 15.7 to 16.3 cents (`results.md`, the layered tables).

## What the runs say

1. **The grid is the binding lever, as the dossier's evidence says.** Every run that adds grid access cuts more than any price or standard change: the full-strength builder about 1.5 Gt over 2030-50 and the permitting package about 2.2 Gt, both with lower bills. The external evidence agrees: transmission must roughly double its growth rate [EV-CLP-400]; projects wait 55 months and 13% are built [EV-CLP-409] [EV-CLP-408]. The engine's own note: grid access, not price, limits wind and solar (SRC-0077).
2. **When the grid binds, the standard is mostly a fee.** Its payments ($163 billion on the decided set) are large and its added cut small, because suppliers cannot connect the clean power the standard asks for. The payments fall as the grid grows: to $93 billion with the full builder and $74 billion with permitting. That points at using the payments to build the grid that ends them: **memo 8**.
3. **The full builder is cost-effective on the model.** Against the decided half-strength builder, it adds about $135 billion of program cost and credited generation over FY2030-39 (counted in the engine's credits) for about 1.46 Gt less CO2 over 2030-50: about **$90 a ton**, project arithmetic, against EPA's 2023 social cost of carbon of $230 a ton in 2030 (2020 dollars; SRC-5006). Bills are about 0.6 cents a kWh lower in 2040.
4. **The economy-wide price (memo 1 A, not chosen)** cuts about 1.26 Gt more over 2030-50, mostly after 2035, with about $840 billion more receipts and a heating charge on households. Espen chose B (`DEC-2026-11-13-06`); nothing here reopens it.
5. **The methane fee is the cheapest tonne in the set:** it lifts net greenhouse gases from 41.0% to 42.8% below 2005 in 2035 and raises money (about $22 billion). Kept as decided.

## Limits

- The builder is a labeled assumption in the engine: its federal grid program at a fraction of full strength (`assumptions.csv`, `grid_standby_scale`, 0.5, range 0.25-1.0; $12 billion a year in 2025 dollars at full strength). How fast a real builder can site lines is the open question [EV-CLP-435] [EV-CLP-437].
- Two of the model's benchmarks fail (HI-1, PR-2; `6-cost.md`, part 6, 1a): its near-term power cuts and early receipts lean high. The grid lever acts on wind and solar access rather than coal-to-gas switching, so the comparison between runs is less exposed than the levels.
- The household split of memo 8's options is not modeled: the household module reads the price, not where the payments go.

## Next

- Memo 8 to Espen (where the standard's payments go).
- Asked M4 whether one-off runs (the builder at 0.75, the standard's cap at $20 and $60) can be made without committing; they would narrow memo 8's range.
- M4's CCS retrofit memo and evidence come next in this folder; this file does not touch sections 3-9 meanwhile.
