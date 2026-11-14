# Memo 8: Carbon capture retrofits on existing power plants

Role: decision memo for Espen. This is a new question, raised by the energy model's comparison with the Energy Policy Simulator, not one of the original forks. Status: **draft, for Espen's decision** (tier 3). Specified, pending the decision, in `../4-specification.md`, part C (CLI-4R.01).

**Decision line.** Recommended: **A. No new spending: count a verified retrofit as meeting the power plant standard, and keep 45Q as it is.** A coal or gas unit that captures at least 90% of its CO2, measured over each year, is treated as clean under the standard that ends unabated coal by 2040. Cost about $0 over FY2030-39 and in FY2040 against the booking (on the energy model, no retrofit pays under the plan's price; MOD-energy, `models/tools/energy/results.md`, case `retro1`). It rests on EPA's cost model (EPA's power-sector model, 2024) [EV-CLP-725] [EV-CLP-726], the only operating record (Boundary Dam 3, as reported by EPA, 2026) [EV-CLP-727], EPA's lead-time estimate (EPA's 2024 rule, as restated in 2026) [EV-CLP-729], and the 45Q statute (26 U.S.C. 45Q) [EV-CLP-732].

## The question

The Energy Policy Simulator (Energy Innovation, version 4.0.7, runs Espen made in November 2026) cuts power-sector emissions much faster than the project's energy model in 2031-2035, under the same carbon price. Nearly all of the difference is carbon capture fitted to existing coal and gas plants: about 760 TWh of captured-plant output in 2035, from none in 2030 (MOD-energy, benchmark EP-3). Should the plan pay for, require or allow such retrofits?

## What the evidence says, in five lines

1. **A retrofit is costly and eats a third of a coal unit's output** (EPA's power-sector model, 2024): about $2,506 per kW for a 700 MW coal unit and $1,380 per kW for a 300 MW combined cycle, in 2022 dollars, at 90% design capture [EV-CLP-725] [EV-CLP-726]. The capture plant raises the coal unit's fuel use per MWh by 44.27% and the combined cycle's by 21.07% [EV-CLP-726].
2. **Achieved capture has fallen well short of design** (Boundary Dam 3, as EPA reports it, 2026): the only commercial-scale capture on a coal unit captured no more than 63% of its CO2 in any year from 2014 to 2022 [EV-CLP-727]. Petra Nova, idled in 2020, restarted in 2023 [EV-CLP-730].
3. **The current administration says 90% capture is not demonstrated** (EPA's partial repeal, second Trump administration, 2026) [EV-CLP-728]; its 2024 predecessor said the opposite (EPA's 2024 rule, Biden administration). Both views stand on the same thin record.
4. **It takes about seven years** (EPA's 2024 rule) [EV-CLP-729], and storage is a bottleneck: 142 storage-well permit applications wait at EPA and at least 13 permitted wells operate (Congressional Research Service, 2026) [EV-CLP-731].
5. **45Q pays up to $85 a ton for 12 years, but only for projects begun before 2033**, and a power unit must be designed to capture at least 75% (26 U.S.C. 45Q) [EV-CLP-732].

## What the energy model finds

- **Timing rules retrofits out under the plan as decided.** The plan's standard ends unabated coal by 2040 (CLI-4A.01). A retrofit must start by about 2033 to beat that date, when the plan's price is about $56 a ton. At EPA's costs and 75% capture in operation, a coal retrofit pays only once the expected price passes about $140 a ton, around 2045; at 90% capture, about $110 (MOD-energy, `assumptions.csv`, `ccs_retrofit_*`; project estimate on EPA's costs).
- **At the research-based limits, none is built** (case `retro1`): emissions, costs and prices are the decided set's.
- **At design capture and twice the limits, about 30 GW of combined cycles are retrofitted by 2050**, capturing about 30 Mt a year (case `retro_hi`). They come in the 2040s, after coal is gone.
- **Raising 45Q to $120-150 a ton gets 6-12 GW started, but they come online after the coal fleet retires** (one-off runs, November 14, 2026). Money cannot buy back the seven years.
- **EPS's 2035 result comes from its retrofit terms.** On those terms as read from its code (95% capture, no capacity lost, one year to build, every plant eligible), the energy model's price-only run produces 768 TWh from retrofitted plants in 2035 against EPS's 762, and cuts slightly more than EPS (benchmark EP-3). On the measured record, those terms are optimistic.

## Options

**A. No new spending; a verified retrofit counts as compliance (recommended).**
- *What it does:* a unit that captures at least 90% of its CO2, measured over each calendar year, is clean under the power plant standard and earns clean credits for its captured share under the clean electricity standard (CLI-3A.01 already counts captured output). 45Q stays as enacted.
- *Cost:* about $0 against the booking; on the model none is built.
- *What it gives up:* nothing the model can see before 2040; if capture costs fall faster than EPA expects, owners can still choose it.

**B. A performance contract for early coal retrofits.** Up to 10 GW of coal units that begin construction by 2031 get a contract paying per ton actually stored, topping the larger of the carbon price and 45Q up to about $140 a ton for 12 years. Built on this schedule, they would run past the 2040 end-date only as verified-capture units (as in A).
- *Cost:* roughly $1-1.5 billion a year from about 2037, about $3.5 billion over FY2030-39, on 10 GW capturing about 45 Mt a year (project estimate: about 6.9 GW after derating, at a 70% capacity factor and EPA's heat rate; a top-up of about $25 a ton over the plan's price of about $115-125 in 2037-40). 45Q, at about $85 a ton, is paid on top under current law wherever it applies.
- *What it gives up:* money for a technology whose only commercial record captured 63%; the contract pays for tons stored, so underperformance costs the owner, not Treasury.

**C. Require capture instead of retirement.** Coal units running past 2039 must capture 90% by 2035, as EPA's 2024 rule did.
- *Cost:* on ratepayers; the federal cost is 45Q on the tons stored. It contradicts the plan's standard, which retires those units by 2040, and depends on a capture rate EPA now says is not demonstrated [EV-CLP-728].

**D. Extend 45Q for gas retrofits to 2039.** Combined cycles that begin capture construction by 2039 and capture at least 90% keep 45Q's 12 years.
- *Cost:* about $0 over FY2030-39; about $2.5 billion a year in the late 2040s on 30 GW capturing 30 Mt (project estimate on case `retro_hi`).
- *What it gives up:* little; it keeps a path open for firm gas with capture after 2040, which the 100% clean standard otherwise prices out.

**Why A.** The evidence does not support paying for retrofits on the plan's timetable: they arrive after the coal they would clean has retired, and the one record we have shows capture well below design. A costs nothing and keeps the option open. D is a reasonable add-on if Espen wants a firm, low-carbon gas path in the 2040s.

## Consequences

- *A coal plant owner* faces retirement by 2040, or capture at 90% measured, at its own cost with 45Q if it starts by 2032.
- *Taxpayers* pay nothing new under A.
- *The 2035 goal* is unchanged: the model sees no retrofits before 2040 in any case it can defend.

## Evidence still needed

- An independent (non-EPA) estimate of retrofit costs and achieved capture: NETL's retrofit studies, the IEA's CCS database, Global CCS Institute project records.
- Boundary Dam 3's 2024-2026 performance from SaskPower's reports (catalogued as citations, not saved).
- Storage-well permit times by state, as more states take primacy.
