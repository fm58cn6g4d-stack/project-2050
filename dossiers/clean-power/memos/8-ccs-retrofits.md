# Memo 8: Carbon capture retrofits on existing power plants

Role: decision memo for Espen. This is a new question, raised by the energy model's comparison with the Energy Policy Simulator, not one of the original forks. Status: **decided: D** (`DEC-2026-11-14-01`). Espen, November 14, 2026: "Yes the new D: the tax credit on top of the carbon price for retrofits begun by 2039, no double payment otherwise". Specified in `../4-specification.md`, part C (CLI-4R.01). Its cost is not yet booked; that waits for a later tier-3 booking change.

**Decision line.** Decided: **D** (`DEC-2026-11-14-01`; recommended). A retrofit credit, inside a rule that pays a stored ton once everywhere else.**
- **The compliance rule:** a coal or gas unit that captures at least 90% of its CO2, measured over each year, counts as clean under the standard that ends unabated coal by 2040.
- **The credit:** for retrofits that begin construction by 2039, 45Q is paid on top of the carbon price the captured ton avoids.
- **Everywhere else:** for industrial capture and new plants built with capture, a stored ton earns the larger of the price avoided and 45Q, not both.
- **Cost:** about $2-9 billion over 2030-39 and $20-61 billion in the 2040s, depending on how well capture performs (2025 dollars).
- **What the model shows:** about 10-19 GW retrofitted by 2040, mostly combined cycles, and 29-86 Mt a year captured by 2050 (MOD-energy, `models/tools/energy/results.md`, cases `retro1_rcredit` and `retro_hi_rcredit`).
- **It followed Espen's direction** before the decision (November 14, as the outgoing M4 session summarized it): keep the retrofit credits, expect gas plants to use them more than coal, and stay open to requiring capture (option C).
- **Costs and effects** are the energy model's calendar-year sums in 2025 dollars, not fiscal years. D lowers carbon-price receipts very slightly, by about $1-2 billion over 2030-39, because retrofitted plants emit less (cases against `decided`).
- **Builds on the legacy work:** the legacy carbon model already netted 45Q against the fee's storage refund ("storage refund reduced by 45Q claimed", SRC-0077). Its standards option required capture on new baseload gas from 2033 (SRC-0077), and the durability findings proposed a statutory capture date for new gas plants after about 2031 (SRC-0079). D keeps that netting everywhere but at retrofits.
It rests on EPA's cost model (EPA's power-sector model, 2024) [EV-CLP-725] [EV-CLP-726], the only operating record (Boundary Dam 3, as reported by EPA, 2026) [EV-CLP-727], EPA's lead-time estimate (EPA's 2024 rule, as restated in 2026) [EV-CLP-729], and the 45Q statute (26 U.S.C. 45Q) [EV-CLP-732]. The cost and capture figures rest on one agency's model and one plant's record; no independent source is in the evidence yet (see "Evidence still needed").

## The question

The Energy Policy Simulator (Energy Innovation, version 4.0.7, runs Espen made in November 2026) cuts power-sector emissions much faster than the project's energy model in 2031-2035, under the same carbon price. Nearly all of the difference is carbon capture fitted to existing coal and gas plants: about 760 TWh of captured-plant output in 2035, from none in 2030 (MOD-energy, benchmark EP-3). Should the plan pay for, require or allow such retrofits?

## What the evidence says, in five lines

1. **A retrofit is costly and eats a third of a coal unit's output** (EPA's power-sector model, 2024): about $2,506 per kW for a 700 MW coal unit and $1,380 per kW for a 300 MW combined cycle, in 2022 dollars, at 90% design capture [EV-CLP-725] [EV-CLP-726]. The capture plant raises the coal unit's fuel use per MWh by about 44% and the combined cycle's by about 21% [EV-CLP-726].
2. **Achieved capture has fallen well short of design** (Boundary Dam 3, as EPA reports it, 2026): the only commercial-scale capture on a coal unit captured no more than 63% of its CO2 in any year from 2014 to 2022 [EV-CLP-727]. Petra Nova, idled in 2020, restarted in 2023 [EV-CLP-730].
3. **The current administration says 90% capture is not demonstrated** (EPA's partial repeal, second Trump administration, 2026) [EV-CLP-728]; its 2024 predecessor said the opposite (EPA's 2024 rule, Biden administration). Both views stand on the same thin record.
4. **It takes about seven years** (EPA's 2024 rule) [EV-CLP-729], and storage is a bottleneck: 142 storage-well permit applications wait at EPA and at least 13 permitted wells operate (Congressional Research Service, 2026) [EV-CLP-731].
5. **45Q pays up to $85 a ton for 12 years, but only for projects begun before 2033**, and a power unit must be designed to capture at least 75% (26 U.S.C. 45Q) [EV-CLP-732].

## The question inside the question: does 45Q stack on the price?

Under a carbon price, a stored ton is not emitted, so it pays no fee. Under current law it also earns 45Q, up to $85 a ton. Nothing in the plan's specification stops an owner from getting both. Stacking is what decides whether retrofits pay: with both, a retrofit begun around 2032, when the plan's price is about $40-56 a ton, would earn about $125-140 a ton: enough for a combined-cycle retrofit, and for a coal retrofit at 90% capture (about $110 a ton). With the larger of the two only, it earns $85, far short. So the plan has to say which it means. A says the larger everywhere; D says both at retrofits only, and the larger elsewhere.

## What the energy model finds

The energy model's default is the larger of the two, not both. Every case below says which it uses; `rcredit` cases stack at retrofits only (option D).

- **Timing rules retrofits out under the plan as decided, if 45Q does not stack.** The plan's standard ends unabated coal by 2040 (CLI-4A.01). A retrofit takes about seven years, so it must start by about 2033 to be running when that date arrives, and the plan's price then is about $56 a ton. At EPA's costs and 75% capture in operation, a coal retrofit pays only once the expected price passes about $140 a ton, around 2045, and at 75% it could not meet the standard anyway; at 90% capture it pays at about $110 (MOD-energy, `assumptions.csv`, `ccs_retrofit_*`; project estimate on EPA's costs).
- **At the research-based limits, none is built** (case `retro1`): emissions, costs and prices are the decided set's.
- **If 45Q stacks, retrofits start from 2031** (cases `retro1_stack` and `retro_hi_stack`):
  - **At 75% capture in operation** (the research-based limits): 25 GW are started by 2040, all combined cycles. About 10 GW are online by 2040 and 21 GW by 2050. No coal retrofit starts, because at 75% capture a coal unit could not meet the standard and would retire in 2040 anyway.
  - **At 90% capture and twice the limits:** about 6 GW of coal and 13 GW of combined cycles are online by 2040, and capture reaches about 65 Mt a year by 2050. These coal units keep running past 2040 as verified-capture units under the compliance rule.
  - **Emissions:** about the same as the decided set. Energy CO2 is 41% below 2005 in 2035 and 66% in 2050 in every case. Stacking raises power emissions by about 20 Mt a year in the early 2030s, because the model's builders hold back some wind, solar and gas plants while waiting for capture plants. It lowers them by about 20 Mt by 2050.
  - **Cost:** 45Q on all stored tons comes to about $92 billion over 2030-39, against about $20 billion without stacking, and about $160 billion in 2040-49, against about $0 (2025 dollars). Industrial capture and new gas plants with capture take most of it, because they would collect 45Q on top of a price that already pays them to capture. The retrofits' own 45Q adds about $2-9 billion over 2030-39 and $15-53 billion in the 2040s.
- **EPS's 2035 result comes from its retrofit terms.** On those terms as read from its code, unverified (95% capture, no capacity lost, one year to build, every plant eligible), the energy model's price-only run produces 768 TWh from retrofitted plants in 2035 against EPS's 762, and cuts slightly more than EPS (benchmark EP-3). On the measured record, those terms are optimistic.

## Options

Every option keeps the compliance rule: a unit that captures at least 90% of its CO2, measured over each calendar year, is clean under the power plant standard. It also earns clean credits for its captured share under the clean electricity standard, which CLI-3A.01 already counts. The options differ in what is paid on top.

**A. No new spending, and no stacking anywhere.** 45Q on a ton that escapes the carbon price is reduced by that price, so every stored ton earns the larger of the two.
- *Cost:* about $0 against the booking. On the model, no retrofit is begun in time (case `retro1`). Current-law 45Q also shrinks once the price passes $85, about 2035; that saving is not booked and is not estimated here.
- *What it gives up:* the retrofit credits Espen wants. Owners can still choose capture at their own cost.

**B. A performance contract for early coal retrofits.** Up to 10 GW of coal units that begin construction by 2031 get a contract paying per ton actually stored. It tops the larger of the carbon price and 45Q up to about $140 a ton for 12 years.
- *Cost:* roughly $1-1.5 billion a year once the units are online, about 2038 with the seven-year lead. That is about $2.5 billion over 2030-39, two years of payments, on 10 GW capturing about 45 Mt a year. It is a project estimate: about 6.9 GW after derating, a 70% capacity factor and EPA's heat rate, with a top-up of about $25 a ton over the plan's price of about $120-125 in 2038-40.
- *What it gives up:* it aims at coal, which Espen expects to use the credits least. It pays for a technology whose only commercial record captured 63%, though underperformance costs the owner, because the contract pays only for tons stored.

**C. Require capture.** Combined cycles that keep running at high output after 2040 must capture 90%, as EPA's 2024 rule required of new baseload gas from 2032.
- *Cost:* on ratepayers; the federal cost is 45Q on the tons stored. The 100% clean standard in 2040 (CLI-3A.01) already presses the same plants to capture or run less, so C mostly makes that pressure explicit.
- *Risks:* it depends on a capture rate EPA now says is not demonstrated [EV-CLP-728]. Units that cannot meet it would run less or retire, so the grid needs firm clean power in their place.
- *With D:* C can follow the credit, for example taking effect from 2045, once the credit has had a decade to get plants retrofitted. That date is a working choice, not modeled here.

**D. A retrofit credit (recommended).** For retrofits that begin construction by 2039, 45Q is paid on top of the carbon price for 12 years. Elsewhere, a stored ton earns the larger of the two, as in A.
- *Results on the model:*

  | Case | Online by 2040 | Online by 2050 | Captured, 2050 | 45Q on retrofits, 2030-39 | 45Q on retrofits, 2040s |
  | --- | --- | --- | --- | --- | --- |
  | Research-based limits, 75% capture (`retro1_rcredit`) | 10 GW of combined cycles | 21 GW | 29 Mt a year | about $2B | about $20B |
  | 90% capture, twice the limits (`retro_hi_rcredit`) | 6 GW of coal and 13 GW of combined cycles | 6 GW and 34 GW | 86 Mt a year | about $9B | about $61B |

  Power CO2 falls by about 8-15 Mt a year from 2040, with no early rise.
- *Against stacking everywhere:* paying both on all capture would add about $72 billion of 45Q over 2030-39, mostly to industrial capture and new gas plants the price already pays to capture. It would also raise power emissions in the early 2030s (cases `retro1_stack` and `retro_hi_stack`). D avoids both.
- *What it gives up:* money for capture whose record is short. At 75% capture in operation, coal units cannot meet the standard, so on the research-based terms the credit goes to gas, as Espen expects. Coal retrofits come only if 90% capture proves out.

**Why D.** Espen wants the retrofit credits and expects gas plants to use them. D pays them where they change what gets built, retrofits, and nowhere else, so it doesn't pay twice for capture the price already pays for. It costs about $2-9 billion over 2030-39. A is the no-cost alternative, but it builds no retrofits. C can be added later as a backstop for combined cycles that neither capture nor wind down.

## Consequences

- *A combined-cycle owner* can retrofit by 2039 and earn the carbon price avoided plus 45Q on each captured ton for 12 years. Without capture, it faces the 100% clean standard in 2040.
- *A coal plant owner* faces retirement by 2040, unless it captures 90% measured; a retrofit under way that will meet that keeps the unit running.
- *Industrial and new gas capture* earn the larger of the price and 45Q. From about 2035, the price alone pays more than 45Q.
- *Taxpayers* pay about $2-9 billion over 2030-39 and $20-61 billion in the 2040s for the credit.
- *The 2035 goal* is unchanged: retrofits arrive from about 2038.

## What the statute needs

- 45Q (26 U.S.C. 45Q) is amended so that a ton excluded from the carbon price gets 45Q only to the extent it exceeds the price avoided, except at qualifying retrofits.
- For a qualifying retrofit, the construction deadline is extended to 2039 and the full credit is paid on top of the price.
- This goes in the FY2030 reconciliation act with the price.

## Evidence still needed

- An independent (non-EPA) estimate of retrofit costs and achieved capture: NETL's retrofit studies, the IEA's CCS database, Global CCS Institute project records.
- Boundary Dam 3's 2024-2026 performance from SaskPower's reports (catalogued as citations, not saved).
- Storage-well permit times by state, as more states take primacy.
