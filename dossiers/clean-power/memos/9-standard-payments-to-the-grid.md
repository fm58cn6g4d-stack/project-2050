# Memo 9: Where the clean standard's payments go

Role: decision memo and its record, from the design test on the energy model (`../design-test.md`). Status: **decided, B** (`DEC-2026-11-13-14`), with the grid account sized each year to ready-to-build transmission projects and anything beyond that kept as general-fund receipts. It amends CLI-3A.02 (memo 3 part 1 B, `DEC-2026-11-13-06`) and the standby builder's reach under CLI-10.03 (memo 4 B, `DEC-2026-11-13-10`) on this point only. The bill credit keeps its own funding.

**Decision line.** Decided: **B, the payments build the grid.** When suppliers fall short of the standard and pay the capped payment, Treasury puts the money into a grid account that the standby builder and the second tranche draw on, instead of adding it to bill protection and the bill credit. Each year the account takes only what ready-to-build transmission work can use; the rest is general-fund receipts. On the energy model's full-builder run, which is an upper bound for B, this cuts **up to about 1.4 billion tons** more CO2 over 2030-50 and lowers the 2040 electricity price by **up to about 0.5 cents** a kWh. The booking's general-fund cost is unchanged; on the model the extra build costs about $60 billion over FY2030-39 before the receipts the account does not spend. Lower- and moderate-income households lose the payments' top-up (about $163 billion over FY2030-39) and keep the bill credit.

Espen: "my answer on the clean electricity standard fee revenue is B, with any excess not needed for transmission build out counted as receipts to the general fund"; on the sizing, "size it to ready-to-build projects"; and on the framing, "I'm not doubting a federal builder could be the best option, I just want policy to fully account for real process." This memo honors that framing: the account pays for the steps that actually hold transmission back (see "How transmission actually gets built" in `../design-test.md`), and money is rarely the step that binds.

## The question

The standard asks for 80% clean power by 2035 and 100% by 2040. On the energy model the grid, not price, holds clean power back: 73% in 2035 and 87% in 2040, so suppliers pay the $40 cap on the shortfall every year, about $163 billion over FY2030-39 and $41 billion in FY2040 (`../6-cost.md`, part 2). As first decided, that money went back to lower- and moderate-income households through bill protection and the bill credit. The question was whether it does more good building the grid that causes the shortfall.

## What the evidence says, in five lines

1. **The grid is the limit.** Transmission must roughly double its growth rate [EV-CLP-400]; the typical project built in 2025 waited about 61 months to connect [EV-CLP-733] and 13% of requests are built [EV-CLP-408]; only about 435 miles of 345 kV and above were built in 2025 [EV-CLP-734]. The energy model finds grid access, not price, limits wind and solar (SRC-0077).
2. **On the model, the standard adds little carbon when the grid binds.** Its layer cuts about 315 Mt of CO2 over 2030-50 (summed year by year) and slightly raises 2035 emissions, while suppliers pay about $193 billion over FY2030-39 at that layer (`../design-test.md`). The cap's level barely matters for carbon: at $20, $40 or $60 the 2035 cut is 41% in all three, while payments are $85, $163 or $229 billion.
3. **Grid access is the strongest lever the model has.** A full-strength builder cuts about 1.43 Gt more over 2030-50, with clean power at 92% in 2040 and the price at 15.5 cents against 16.1 (`../design-test.md`). The engine treats it generously (ramped in by 2032, added on top of permitting, no supply limit), so this is an upper bound.
4. **Money is rarely what binds.** Siting authority, cost allocation, equipment and lead times are. WAPA's $3.25 billion loan authority has financed two lines in seventeen years [EV-CLP-738] [EV-CLP-739]; DOE cancelled its last three national-interest corridors partly for lack of developer interest in federal backstop siting [EV-CLP-736] [EV-CLP-737]; transformers ran about 30% short in 2025, mostly imported [EV-CLP-747].
5. **Building lines across states is slow whoever pays:** the Grain Belt Express lost its federal guarantee in 2025 [EV-CLP-435] [EV-CLP-437], and SunZia took almost two decades to permit, plan and finance [EV-CLP-756]. Money alone does not site a line.

## The options as weighed

All figures on the energy model (MOD-energy, `models/tools/energy/`, main at `37ee069`), nominal $ billion over FY2030-39, against the decided set; project arithmetic. "On the booking" means the budget model's rows as booked (`../6-cost.md`, part 6), which carry CLI-1 apart from the model.

**A. As first decided: payments to bill protection and the bill credit.**
- *What it does:* the payments return to lower- and moderate-income households, on top of the bill credit's own funding.
- *Outcome on the model:* the decided set (41% below 2005 in 2035; clean 87% in 2040; 16.1 cents).
- *Cost:* the payments net to zero on the general fund except JCT's 24.4% offset, about $40 billion over FY2030-39 and $10 billion in FY2040 (booked: C3A, CLI-3A, CXA).
- *Households:* lower- and moderate-income households receive about **$163 billion over FY2030-39 and $41 billion in FY2040**.

**B. The payments build the grid (decided).**
- *What it does:* each year's payments go to a grid account that the standby builder (TVA, Bonneville, WAPA and the eastern corporation) and the second tranche draw on, sized to ready-to-build work, with the rest kept as receipts. The builder's one-year trigger and competitive-cost test stay.
- *Outcome on the model, up to:* the full-strength builder run (`bld_hi`) is the most B could achieve: **up to** 42% below 2005 in 2035, **up to** 92% clean in 2040, **up to** 0.5 cents lower in 2040 (15.5 cents), **up to about 1.43 Gt** less CO2 over 2030-50. B falls short of that because the money starts only when payments do (none in FY2030-31, $7-9 billion a year in FY2032-33), reaches only where ready-to-build work exists, and waits on the trigger. The builder at three-quarters strength (`bld_75`) gives 41.3% in 2035, 52.8% in 2040 (against 40.8% and 51.8%), 15.8 cents and about 0.75 Gt less: a reasonable middle case.
- *Cost on the booking:* nothing more; the booked rows don't move until the follow-up booking change (below).
- *Cost on the model:* about **+$60 billion** on the general fund over FY2030-39 if the account pays the builder's program. The full builder's credits are +$135 billion, of which about $74 billion is the program (paid from the account) and about **$62 billion is extra credited wind and solar** (CLI-1's disclosed risk, a general-fund outlay). Faster coal retirement shrinks the carbon price's receipts by $75 billion, which moves **−$15 billion** of the transition share onto CLI-5's general-fund draw (the other $60 billion is the dividend, which falls with the receipts and is off the general fund). JCT's offset on the smaller receipts is about **$18 billion** lower, which helps. Net about +$59 billion. **This depends on how much the account spends:** the full builder's payments are $93 billion against a $74 billion program, so if the account spends only the program, about $19 billion returns as receipts and the net is about +$40 billion; if real ready-to-build need is smaller, as the research suggests, more returns and the outcome falls further below the upper bound.
- *Households:* lower- and moderate-income households lose A's top-up (about $163 billion over FY2030-39 and $41 billion in FY2040) and keep the bill credit's own $12 billion a year. In return everyone's price falls by up to 0.5 cents in 2040, less before: on 1,500-1,800 TWh of household use that is **up to about $8-9 billion a year in 2040** for all households, and up to about $50 billion over FY2030-39, of which lower-income households get a fraction (judgment; the household model reads the price, not where the payments go). The transfer B gives up is several times what it returns to the households A protected.
- *Burden:* a grid account at DOE with a yearly sizing rule (below), in place of a transfer to the bill credit's administrators.

**C. A full-strength builder everywhere, paid from the general fund (memo 4 option A).**
- *What it does:* the same build without waiting for the standard to be missed; the payments stay with households.
- *Outcome on the model, up to:* as B's upper bound.
- *Cost on the booking:* about +$74 billion over FY2030-39 (the program).
- *Cost on the model:* about **+$132 billion** (the full +$135 billion of credits, plus $15 billion of transition share, less $18 billion of offset), with no receipts back.
- *Burden:* the federal-builder risk memo 4 weighed: a large public builder everywhere, which Espen did not choose.

B and C differ in who pays the program and whether households keep the payments, not in the model's best outcome.

## Why B was chosen

It aims the payments at the cause of the shortfall: the more the grid grows, the less suppliers pay, so the money spends itself out. Sizing to ready-to-build work keeps it from paying for lines that can't yet be sited, and anything unspent is a receipt. The trade is the household top-up; the bill credit itself is untouched.

## The grid account

**Ready-to-build.** A transmission line or upgrade is ready to build when it has (1) accepted cost allocation in a FERC-approved plan, or a signed offtake or anchor contract, (2) siting under way with the lead state or FERC (application filed), and (3) its long-lead equipment (transformers, breakers, conductor) procured or reserved. Reconductoring and grid-enhancing technologies on existing rights of way meet (2) by definition. DOE certifies the list each year and publishes it with the account's size: the sum of what those projects can draw that year. Working choice, from the research in `../design-test.md`; it uses the plans, filings and contracts that already exist rather than a new review.

**What the account pays for, in order** (working choice):
1. **Reconductoring and grid-enhancing technologies first**, including on Bonneville's, WAPA's, the other power marketing administrations' and TVA's own systems (about 14% of US transmission [EV-CLP-749]). These add capacity in 18-36 months per project on existing rights of way.
2. **Risk instruments rather than capital that rates repay:** capacity contracts that anchor stranded or merchant lines, and first-loss cover for interregional and cross-seam lines, where the needs study finds the most value [EV-CLP-755]. The builder's own capital stays on its borrowing authority and rates (CLI-10.02, CLI-10.03).
3. **A pooled DOE equipment reserve** for transformers, breakers and conductor, sold on at cost to ready-to-build projects, to cut the lead times that bind [EV-CLP-747].
4. **Host-community and state siting grants**, replacing the rescinded IRA §50152 [EV-CLP-754].
5. **Borrowing against future payments** for early, fast assets, since no payments arrive in FY2030-31.

**Unspent payments** are general-fund receipts in the year collected. The account does not carry a balance beyond one year (working choice), so it cannot grow into a standing fund.

## Limits

- The builder's strength is a labeled assumption in the engine (`grid_standby_scale`; $12 billion a year at full strength), with five generous features listed in `../design-test.md`. No run ties the build to the payments year by year.
- The model's near-term power cuts lean high (HI-1; `../6-cost.md`, part 6, 1a). The grid lever works through wind and solar access, so the comparison between runs is less exposed than the levels.
- The household split is judgment until the household model can route the payments.

## Consequences

CLI-3A.02 changes where the payments go; CLI-10.03 gains the grid account; CLI-5H.01 and CLI-5L.01 lose the payments as a funding source (bill protection then runs on the bill credit's own funding). The booking's C3A and CXA rows stay; CLI-3A's pay-out becomes grid-account outlays sized to ready-to-build need, with the rest kept as receipts, in a follow-up tier-3 change with the specification rows. Section 7's households table and section 9's bill answer gain the lower 2040 price.
