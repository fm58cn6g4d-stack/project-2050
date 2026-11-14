# Memo 8: Carbon capture retrofits on existing power plants

Role: decision memo for Espen. This is a new question, raised by the energy model's comparison with the Energy Policy Simulator, not one of the original forks. Status: **draft, for Espen's decision** (tier 3). Specified, pending the decision, in `../4-specification.md`, part C (CLI-4R.01).

**Decision line.** Recommended: **A. No new spending: count a verified retrofit as meeting the power plant standard, and pay a stored ton once, not twice.** A coal or gas unit that captures at least 90% of its CO2, measured over each year, is treated as clean under the standard that ends unabated coal by 2040. A stored ton escapes the carbon price; 45Q on that ton is reduced by the price it escaped, so the owner gets the larger of the two, not both. Cost about $0 over FY2030-39 and in FY2040 against the booking: on the energy model, with this rule no retrofit pays under the plan's price (MOD-energy, `models/tools/energy/results.md`, case `retro1`). Without the rule, 45Q would stack on top of the price, costing about $70 billion more over FY2030-39 and about $160 billion more in the 2040s on all capture, for no change in emissions (cases `retro1_stack` and `retro1`). It rests on EPA's cost model (EPA's power-sector model, 2024) [EV-CLP-725] [EV-CLP-726], the only operating record (Boundary Dam 3, as reported by EPA, 2026) [EV-CLP-727], EPA's lead-time estimate (EPA's 2024 rule, as restated in 2026) [EV-CLP-729], and the 45Q statute (26 U.S.C. 45Q) [EV-CLP-732]. The cost and capture figures rest on one agency's model and one plant's record; no independent source is in the evidence yet (see "Evidence still needed").

## The question

The Energy Policy Simulator (Energy Innovation, version 4.0.7, runs Espen made in November 2026) cuts power-sector emissions much faster than the project's energy model in 2031-2035, under the same carbon price. Nearly all of the difference is carbon capture fitted to existing coal and gas plants: about 760 TWh of captured-plant output in 2035, from none in 2030 (MOD-energy, benchmark EP-3). Should the plan pay for, require or allow such retrofits?

## What the evidence says, in five lines

1. **A retrofit is costly and eats a third of a coal unit's output** (EPA's power-sector model, 2024): about $2,506 per kW for a 700 MW coal unit and $1,380 per kW for a 300 MW combined cycle, in 2022 dollars, at 90% design capture [EV-CLP-725] [EV-CLP-726]. The capture plant raises the coal unit's fuel use per MWh by about 44% and the combined cycle's by about 21% [EV-CLP-726].
2. **Achieved capture has fallen well short of design** (Boundary Dam 3, as EPA reports it, 2026): the only commercial-scale capture on a coal unit captured no more than 63% of its CO2 in any year from 2014 to 2022 [EV-CLP-727]. Petra Nova, idled in 2020, restarted in 2023 [EV-CLP-730].
3. **The current administration says 90% capture is not demonstrated** (EPA's partial repeal, second Trump administration, 2026) [EV-CLP-728]; its 2024 predecessor said the opposite (EPA's 2024 rule, Biden administration). Both views stand on the same thin record.
4. **It takes about seven years** (EPA's 2024 rule) [EV-CLP-729], and storage is a bottleneck: 142 storage-well permit applications wait at EPA and at least 13 permitted wells operate (Congressional Research Service, 2026) [EV-CLP-731].
5. **45Q pays up to $85 a ton for 12 years, but only for projects begun before 2033**, and a power unit must be designed to capture at least 75% (26 U.S.C. 45Q) [EV-CLP-732].

## The question inside the question: does 45Q stack on the price?

Under a carbon price, a stored ton is not emitted, so it pays no fee. Under current law it also earns 45Q, up to $85 a ton. Nothing in the plan's specification stops an owner from getting both. Stacking is what decides whether retrofits pay: with both, a retrofit begun around 2032, when the plan's price is about $40-56 a ton, would earn about $125-140 a ton: enough for a combined-cycle retrofit, and for a coal retrofit at 90% capture (about $110 a ton). With the larger of the two only, it earns $85, far short. So the plan has to say which it means. Option A says the larger, not both.

## What the energy model finds

The energy model's default is the larger of the two, not both. Every case below says which it uses.

- **Timing rules retrofits out under the plan as decided, if 45Q does not stack.** The plan's standard ends unabated coal by 2040 (CLI-4A.01). A retrofit takes about seven years, so it must start by about 2033 to be running when that date arrives, and the plan's price then is about $56 a ton. At EPA's costs and 75% capture in operation, a coal retrofit pays only once the expected price passes about $140 a ton, around 2045, and at 75% it could not meet the standard anyway; at 90% capture it pays at about $110 (MOD-energy, `assumptions.csv`, `ccs_retrofit_*`; project estimate on EPA's costs).
- **At the research-based limits, none is built** (case `retro1`): emissions, costs and prices are the decided set's.
- **If 45Q stacks, retrofits start from 2031** (cases `retro1_stack` and `retro_hi_stack`):
  - **At 75% capture in operation** (the research-based limits): 25 GW are started by 2040, all combined cycles. About 10 GW are online by 2040 and 21 GW by 2050. No coal retrofit starts, because at 75% capture a coal unit could not meet the standard and would retire in 2040 anyway.
  - **At 90% capture and twice the limits:** about 6 GW of coal and 13 GW of combined cycles are online by 2040, and capture reaches about 65 Mt a year by 2050. These coal units keep running past 2040 as verified-capture units under A's rule.
  - **Emissions:** about the same as the decided set. Energy CO2 is 41% below 2005 in 2035 and 66% in 2050 in every case. Stacking raises power emissions by about 20 Mt a year in the early 2030s, because the model's builders hold back some wind, solar and gas plants while waiting for capture plants. It lowers them by about 20 Mt by 2050.
  - **Cost:** 45Q on all stored tons comes to about $92 billion over 2030-39, against about $20 billion without stacking, and about $160 billion in 2040-49, against about $0 (2025 dollars). Industrial capture and new gas plants with capture take most of it, because they would collect 45Q on top of a price that already pays them to capture. The retrofits' own 45Q adds about $2-9 billion over 2030-39 and $15-53 billion in the 2040s.
- **EPS's 2035 result comes from its retrofit terms.** On those terms as read from its code, unverified (95% capture, no capacity lost, one year to build, every plant eligible), the energy model's price-only run produces 768 TWh from retrofitted plants in 2035 against EPS's 762, and cuts slightly more than EPS (benchmark EP-3). On the measured record, those terms are optimistic.

## Options

**A. No new spending; a verified retrofit counts as compliance (recommended).**
- *What it does:*
  - a unit that captures at least 90% of its CO2, measured over each calendar year, is clean under the power plant standard;
  - it earns clean credits for its captured share under the clean electricity standard (CLI-3A.01 already counts captured output);
  - 45Q stays, but on a ton that escapes the carbon price it is reduced by that price, so a stored ton earns the larger of the two. Treasury runs it through the 45Q claim that exists today.
- *Cost:* about $0 against the booking; on the model none is built. Without the no-stacking rule, 45Q would cost about $70 billion more over FY2030-39.
- *What it costs owners:* from 2035, when the plan's price passes $85, 45Q adds nothing for a stored ton, since the price avoided already exceeds it. Before then, 45Q tops a ton up to $85. Capture sites built for 45Q before 2030 keep its value in those years.
- *What it gives up:* nothing the model can see before 2040; if capture costs fall faster than EPA expects, owners can still choose it.

**B. A performance contract for early coal retrofits.** Up to 10 GW of coal units that begin construction by 2031 get a contract paying per ton actually stored, topping the larger of the carbon price and 45Q up to about $140 a ton for 12 years. 45Q does not stack, as in A. Built on this schedule, they would run past the 2040 end-date only as verified-capture units (as in A).
- *Cost:* roughly $1-1.5 billion a year once the units are online, about 2038 with the seven-year lead: about $2.5 billion over FY2030-39 (two years of payments), on 10 GW capturing about 45 Mt a year. That is a project estimate: about 6.9 GW after derating, at a 70% capacity factor and EPA's heat rate, with a top-up of about $25 a ton over the plan's price of about $120-125 in 2038-40. If 45Q stacked, the top-up would not be needed, but 45Q itself on those tons would cost about $3.8 billion a year.
- *What it gives up:* money for a technology whose only commercial record captured 63%; the contract pays for tons stored, so underperformance costs the owner, not Treasury.

**C. Require capture instead of retirement.** Coal units running past 2039 must capture 90% by 2035, as EPA's 2024 rule did.
- *Cost:* on ratepayers; the federal cost is 45Q on the tons stored. It contradicts the plan's standard, which retires those units by 2040, and depends on a capture rate EPA now says is not demonstrated [EV-CLP-728].

**D. Extend 45Q for gas retrofits to 2039.** Combined cycles that begin capture construction by 2039 and capture at least 90% keep 45Q's 12 years.
- *Cost:* about $0 over FY2030-39; about $2.5 billion a year in the late 2040s on 30 GW capturing 30 Mt (project estimate on case `retro_hi`).
- *What it gives up:* little; it keeps a path open for firm gas with capture after 2040, which the 100% clean standard otherwise prices out.

**Why A.** The evidence does not support paying for retrofits on the plan's timetable: they arrive after the coal they would clean has retired, and the one record we have shows capture well below design. Letting 45Q stack on the price would get some retrofits built, about 6 GW of coal at best, but it would pay twice for tons the price already pays to store: about $70 billion more over FY2030-39, without changing the emissions the model sees. If Espen wants those coal retrofits anyway, B buys them for less, because it pays only the units it contracts. A costs nothing and keeps the option open. D is a reasonable add-on if Espen wants a firm, low-carbon gas path in the 2040s.

## Consequences

- *A coal plant owner* faces retirement by 2040, or capture at 90% measured, at its own cost, earning the larger of the carbon price avoided and 45Q (45Q if it starts by 2032 under current law).
- *Industrial and new gas capture* earn the same, the larger of the two; from about 2035 the price alone pays more than 45Q.
- *Taxpayers* pay nothing new under A, and avoid the second payment that stacking would make.
- *The 2035 goal* is unchanged: the model sees no retrofits before 2040 in any case it can defend.

## Evidence still needed

- An independent (non-EPA) estimate of retrofit costs and achieved capture: NETL's retrofit studies, the IEA's CCS database, Global CCS Institute project records.
- Boundary Dam 3's 2024-2026 performance from SaskPower's reports (catalogued as citations, not saved).
- Storage-well permit times by state, as more states take primacy.
