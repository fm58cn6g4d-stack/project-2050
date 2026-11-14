# Memo 8: Where the clean standard's payments go

Role: decision memo for Espen, from the design test on the energy model (`../design-test.md`). Status: **open**. It would amend CLI-3A.02 (memo 3 part 1 B, `DEC-2026-11-13-06`) and the standby builder's reach under CLI-10.03 (memo 4 B, `DEC-2026-11-13-10`); nothing else in those decisions changes.

**Decision line.** Recommended: **B, the payments build the grid.** When suppliers fall short of the standard and pay the capped payment, Treasury puts the money into the standby builder's and the second tranche's transmission work instead of adding it to bill protection and the bill credit. The bill credit keeps its own money from the transition share. On the energy model this cuts about 1.5 billion more tons of CO2 over 2030-50 and lowers the 2040 electricity price by about 0.6 cents a kWh. The payments shrink as the grid catches up, to about $93 billion over FY2030-39 from $163 billion.

## The question

The standard asks for 80% clean power by 2035 and 100% by 2040. On the energy model the grid, not price, holds clean power back: 73% in 2035 and 87% in 2040, so suppliers pay the $40 cap on the shortfall every year, about $163 billion over FY2030-39 and $41 billion in FY2040 (`6-cost.md`, part 2). As decided, that money goes back to lower- and moderate-income households through bill protection and the bill credit. The question is whether it does more good building the grid that is causing the shortfall.

## What the evidence says, in five lines

1. **The grid is the limit.** Transmission must roughly double its growth rate [EV-CLP-400]; projects wait 55 months to connect and 13% are built [EV-CLP-409] [EV-CLP-408]; the energy model finds grid access, not price, limits wind and solar (SRC-0077).
2. **On the model, the standard adds little carbon when the grid binds.** Its layer cuts about 255 Mt of CO2 over 2030-50 while suppliers pay about $193 billion over FY2030-39 and the 2040 price rises 0.6 cents (`../design-test.md`).
3. **Grid access is the strongest lever the model has.** A full-strength builder cuts about 1.46 Gt more over 2030-50, with clean power at 92% in 2040 and the price at 15.5 cents against 16.1 (`../design-test.md`).
4. **Federal grid lending has a good record:** DOE's loan office lost about 3% of what it lent [EV-CLP-427].
5. **Building lines across states is slow whoever pays:** the Grain Belt Express lost its federal guarantee in 2025 [EV-CLP-435] [EV-CLP-437]. Money alone does not site a line.

## The options

**A. As decided: payments to bill protection and the bill credit.**
- *What it does:* the payments return to lower- and moderate-income households, on top of the bill credit's own funding.
- *Outcome on the model:* the decided set (41% below 2005 in 2035; clean 87% in 2040; 16.1 cents).
- *Cost:* the payments net to zero on the general fund except JCT's 24.4% offset, about $40 billion over FY2030-39 and $10 billion in FY2040 (booked, `6-cost.md` part 6, 6a).
- *Burden:* none new.

**B. The payments build the grid (recommended).**
- *What it does:* each year's payments go to a grid account that the standby builder (TVA, Bonneville, WAPA and the eastern corporation) and the second tranche draw on, first in the regions where suppliers paid. The builder's one-year trigger and competitive-cost test stay; the money lets it act at full strength where the standard is being missed. Bill protection and the bill credit keep their booked funding from the transition share.
- *Outcome on the model* (the full-strength builder run, the nearest the model has): 42% below 2005 in 2035; clean 92% in 2040; 15.5 cents in 2040, about 0.6 cents lower for every household; about 1.46 Gt less CO2 over 2030-50.
- *Cost:* the builder's extra program cost (about $6 billion a year in 2025 dollars, about $65-70 billion over FY2030-39) comes out of the payments, so the general fund is no worse, and the offset falls about $17 billion as the payments shrink. The extra credited wind and solar (about $65 billion more) is CLI-1's disclosed risk. On the model the whole change is about **$90 a ton** (project arithmetic).
- *Burden:* a grid account at DOE with yearly allocation rules, in place of a transfer to the bill credit's administrators.
- *Who could lose:* lower-income households lose the payments' top-up to bill protection and the credit, though their bills fall with everyone's. The household model does not yet split this: to check at the next household run.

**C. A full-strength builder everywhere, paid from the general fund (memo 4 option A).**
- *What it does:* the same grid build, without waiting for the standard to be missed, and the payments stay with households.
- *Outcome:* as B.
- *Cost:* about $65-70 billion more on the general fund over FY2030-39, plus the credits' risk.
- *Burden:* the federal-builder risk memo 4 weighed: a large public builder everywhere, which Espen did not choose.

**Why B.** It aims the payments at the cause of the shortfall: the more the grid grows, the less suppliers pay, so the money spends itself out. It costs the general fund nothing more and keeps the standby builder's trigger as decided. The trade is the household top-up; the bill credit itself is untouched.

## Limits

- The builder's strength is a labeled assumption in the engine (`grid_standby_scale`; $12 billion a year at full strength). The payments ($93-163 billion) roughly match the extra build B needs, but no run ties the build to the payments year by year. I've asked M4 whether such a run can be made.
- The model's near-term power cuts lean high (HI-1; `6-cost.md`, part 6, 1a). The grid lever works through wind and solar access, so the comparison between runs is less exposed than the levels.

## Consequences if B

CLI-3A.02 changes where the payments go; CLI-10.03 gains the grid account. The booking's C3A and CXA rows stay; CLI-3A's pay-out becomes grid capital, time-limited (D4-B), in a follow-up tier-3 change. Section 7's households table and section 9's bill answer would gain the lower 2040 price.
