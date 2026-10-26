# Climate and grid portfolio allocation

**Context.** Claude Code, October 26, 2026 (second round, same day). Policy IDs: CLI-1 to CLI-13, REV-C1/C2/C3, CLI-2, Moving America's fuel steps (D7), CAP-7. Source base: `main` at `77f8a5e551367a52319e5323e8a33789894ebc67`; branch `claude/climate-portfolio`, PR #26. Status: completed for review, not merged.

**What's new in this round.** It follows Espen's direction: higher climate goals; grid payment that can include borrowing, direct loan authority and contract authority; lower borrowing kept where possible; credit caps or phase-downs if warranted; pricing everything; and optimizing packages rather than single policies. It adds:
- a search of every combination of ten levers (4,608 packages);
- a recommended package, with layering and stress tests;
- a credit phase-down timeline;
- grid financing windows;
- a whole-package budget;
- the disaster preparedness and response package ([its own file](climate-portfolio-disaster-resilience.md)).

Nothing here changes an adopted input or a shared generated output. The proposed deltas go to Codex.

**Files.**
- This recommendation.
- Generated results:
  - [single-lever comparison](climate-portfolio-model-results.md)
  - [package search](climate-portfolio-packages.md)
  - [pricing and budget](climate-portfolio-pricing.md)
  - [disaster components](climate-portfolio-disaster-components.csv)
- The [instrument register](climate-portfolio-components.csv) and the [code](../index/tools/climate-portfolio/README.md).

## Bottom line

1. **Adopt Package A as the climate allocation.** It is built from levers that work together, not from the best single policies:
   - a statutory clean-power path of 90% by 2035 and 100% by 2040;
   - statutory zero-emission vehicle standards for cars and heavy trucks;
   - public grid delivery;
   - tripled low-income heat-pump retrofits;
   - doubled clean-industry support through contracts;
   - the carbon fee extended to industrial process emissions;
   - clean-energy credits redesigned to step down as those standards and the grid take over.

   In the model it reaches 47% below 2005 in 2035, 60% in 2040 and 70% in 2050, against the decided package's 43%, 54% and 64%. Farms, forests and carbon removal (CLI-13, estimated outside the model) add about 2 points in 2035 and 8 in 2050. It **saves** about $71B in modeled outlays over 2030-39, and it still reaches 65% in 2050 after a 2037 repeal, against 58% for the decided package.
2. **Yes, the credits should step down on a timeline.** Every efficient package redesigns them. The schedule is below. In ledger terms the redesign saves about $0.18-0.35T nominal over 2030-39 inside Package A. That pays for the low-income retrofits, disaster preparedness's permanent pieces and LMI bill protection, and still leaves a net permanent saving.
3. **Finance the grid mostly with loans and contracts.** A lean first tranche ($25B grants, $100B direct loans, $20B capacity contracts) costs about $32B in deficit terms ($28-40B) and enables about $165B of construction. That is more than the earlier $120B all-grant program, at about a quarter of the budget cost. A full second tranche ($40B, $200B and $40B) follows if delivery milestones are met.
4. **Borrowing stays well inside the room already freed.** Package A plus core disaster preparedness borrows about $0.12T nominal under D4-B ($0.09-0.16T), roughly 61% of the ~$195B freed by the smaller rebuild surge. Permanent items stay a net saving, and the process-emissions fee covers clean-industry contracts and removal purchases.
5. **The higher goals are not yet met, and the reason matters.** Espen raised the goals: net zero by 2050, and 61-66% below 2005 by 2035. Even with every instrument the model represents pushed hard (below), it tops out at about 49% in 2035 and 76% in 2050, or roughly 53% and 87% adding CLI-13's high estimates. The 2035 gap comes from how fast vehicle, building and equipment stocks turn over, and from this model being slower than the large published models in the first decade. Money is not what limits it. Closing the gap is the next climate task (section 6).
6. **A higher carbon price is the biggest remaining lever, and it is Espen's call.** REV-C1H keeps D7's low start, then rises to $150 a ton by 2037 instead of $100. Added to Package A, it avoids 2.3 Gt more over 2030-50 at no outlay. The costs are about $1.70 a month more on the average 2040 bill and larger fee costs for the top two quintiles; the dividend keeps the bottom three positive. D7 is decided, so this needs Espen.

## 1. How the search works

**The baseline.** Every package starts from the carbon model's decided package (case `full`): the D7 fee and dividend, CLI-1A credits, the 80% clean electricity standard, CLI-4 rules, Weatherization heat pumps, the grid statute and the methane fee. Each package is run with identical physical assumptions.

**The ten levers.**
- credits: 4 designs;
- clean-power standard: 3;
- vehicle standards: 3;
- carbon price path: 2;
- public grid: on or off;
- low-income retrofits: on or off;
- clean-industry support: on or off;
- process-emissions fee: on or off;
- methane fee design: 2;
- coal retirement: on or off.

That gives 4,608 packages.

**Each package reports:**
- net greenhouse gases in 2035, 2040 and 2050, and cumulatively over 2030-50;
- outlays: credits, programs, the model's new industrial-support estimate and named external costs;
- fee receipts;
- residential bills;
- household carbon-channel effects.

The search finds the best package for each budget cap and bill cap and the full cost and abatement frontier. It then measures how each lever's value changes inside the recommended package and stress-tests the leading packages for weak grid delivery and a 2037 repeal.

**Model changes.** To represent these levers, the carbon model gained eight settings that are all off by default: credit cost per sale, a vehicle-credit term, the power-credit phase-out trigger, optional zero-emission sales schedules, a second clean-power standard step, and a reported industrial-support cost. The project's rebuild leaves all 29 shared outputs unchanged.

## 2. What the search found

**The frontier has one shape.** Every efficient package redesigns the credits. Beyond that, packages add statutory standards and grid delivery before anything else, then the higher price, then retrofits and industry. Selected rows from the [package results](climate-portfolio-packages.md):

| Budget (2030-39 outlays vs decided, 2025 $) | Best package | Net GHG below 2005: 2035 / 2040 / 2050 | Extra Gt avoided 2030-50 | 2040 bill |
| --- | --- | --- | --- | --- |
| Save at least $400B | credits redesigned, CES 90/100, higher price, grid, industry, process fee | 46% / 58% / 68% | +4.7 | +$2.65 |
| Save at least $200B, bill under +$3 | credits redesigned, CES 90/100, higher price, grid, retrofits, industry, process fee | 46% / 58% / 69% | +5.1 | +$2.45 |
| **No added cost, bill under +$3 (Package A)** | **credits redesigned, CES 90/100, vehicle standards, grid, retrofits, industry, process fee** | **47% / 60% / 70%** | **+6.8** | **+$2.32** |
| No added cost (Package A with REV-C1H) | Package A plus the higher price | 48% / 62% / 73% | +9.1 | +$3.98 |

**Layering: what each lever is worth inside Package A** (alone, then inside the package; Gt over 2030-50 / $B 2025 over 2030-39):

| Lever | Alone | Inside Package A | What the difference means |
| --- | --- | --- | --- |
| Credit redesign (standard-led) | −0.49 Gt / −$549B | −0.12 Gt / −$755B | Once standards bind, the credits pay for adoption the standards already require. Redesigning them saves more inside the package and costs fewer tons. |
| Statutory vehicle standards (cars and trucks) | +3.49 / +$476B | +4.07 / +$284B | The biggest single lever. Alone, it looks expensive only because kept EV credits pay out on mandated sales. |
| Public grid delivery | +1.62 / +$91B | +2.10 / +$123B | Worth more with the 90/100 standard and electrification: more clean load needs more grid. |
| Clean-industry support | +0.68 / +$27B | +0.70 / +$27B | Independent of the rest. |
| Low-income retrofits | +0.35 / +$67B | +0.41 / +$67B | Slightly more valuable on a cleaner grid. |
| CES 90% by 2035 / 100% by 2040 | +0.19 / $0 | +0.23 / $0 | Small in tons while the fee is in place. It is the backstop that holds power-sector cuts if the fee goes. |
| Process-emissions fee | +0.15 / about $0 outlay, +$0.11T receipts | +0.15 / $0 | Finances clean-industry contracts and removal. |

**What doesn't earn a place.**
- **Tripling the methane fee** without the certification exit *raises* emissions by 0.66 Gt. It weakens the incentive to certify against the leak standards, which cut methane 75%. Keep REV-C3 as decided.
- **Faster coal retirement** adds almost nothing on top of the fee (+0.06 Gt). Keep CLI-11 as an option for its worker and community guarantees, not for tons.

**Stress tests for Package A** (net GHG below 2005 in 2035 / 2050):

| Case | Package A | Decided package |
| --- | --- | --- |
| Central | 47% / 70% | 43% / 64% |
| Weak grid delivery | 46% / 70% | 43% / 64% |
| 2037 repeal (fee ends, consumer credits closed) | 46% / 65% | 42% / 58% |

Statutory standards and built grid assets are what survive a repeal.

**Households in 2035** (carbon channel, change against the decided package):
- bottom two quintiles: +$7 each;
- middle quintile: +$1;
- fourth quintile: −$13;
- top quintile: −$60.

The fourth-quintile change is small, but it is the D3 group to watch in Codex's incidence model.

## 3. Credit phase-down timeline (recommended)

The credits are worth most before standards and the grid take hold, and as insurance if those fail. The design keeps them as a bridge, ends them on a schedule tied to the instruments that replace them, and brings them back automatically if the replacements are repealed.

| Credit | 2030 restoration | Step-down | Why | Model effect |
| --- | --- | --- | --- | --- |
| New-EV (30D) and commercial-vehicle (45W) credits | Restored with income limits ($150k/$300k) and price caps ($55k/$80k); the new-EV credit is about half the IRA value | End for vehicles placed in service after 2032, when the statutory standard requires about 60% zero-emission sales | After the standard binds, the credit pays for sales the law already requires. EV sales fell from about 8% to 5-6% of the market after the credit ended in 2025, so the credit matters while no standard binds, which is the bridge years | Most of the redesign's saving |
| Used-EV credit (25E) and charging (30C) | Restored, income-qualified | Keep through 2039 | Reaches lower-income buyers; small cost | (inside the vehicle group) |
| Heat-pump credit (25C) | Restored, point of sale | Keep through 2039; revisit with a clean-heat standard | Cheapest credit per ton (about $80) | Kept |
| Wind, solar and storage (45Y/48E) | Restored, technology-neutral, direct pay | Phase down once power-sector CO2 falls below 600 Mt (about 2034-35 in Package A) instead of the IRA's 383 Mt trigger (about 2037). Projects that start construction before then keep their full credit (CLI-1E grandfathering) | With 90% clean power by 2035, statutory 100% by 2040 and public grid delivery, late credits mostly pay for projects that would be built anyway. Bills rise about $2.30 a month by 2040, offset for LMI households (below) | Saves outlays; about 0.1 Gt |
| Industrial (48C, 45V) | Restored | Keep; move part into priced CLI-9 contracts | Industry is the slowest sector to cut emissions | Doubled support (contracts) |
| Transmission ITC and 45X grid components (CLI-5) | As decided | Keep | Complements public grid delivery | Kept |
| **Snap-back** | | If the carbon fee, the clean-power standard or the vehicle standard is repealed or enjoined, the matching credits revert to the IRA schedule automatically | This keeps the credits' insurance value without paying for it every year | Contingent cost; not modeled |

**What the redesign is worth.**
- **Savings.** Standard-led alone saves $0.70T nominal over 2030-39 in the model, about $0.35-0.70T in ledger terms. Inside Package A it saves $0.84T in the model, because stronger standards raise credit claims if the credits are kept. Against the decided package, Package A's credit outlays are $0.18-0.35T lower in ledger terms.
- **What it costs.**
  - About 0.12 Gt inside the package.
  - A bill increase of about $4-28 a year per household over 2033-39. Offsetting it for low- and moderate-income households costs about $6B.
- **Status.** These are model estimates. Count the low end in D4 tests until there is a JCT-style score.

## 4. Grid delivery and its financing

| Variant | Grants / loans / contracts ($B, 2025) | Deficit cost | Build enabled | Gross Treasury financing | Loan repayment on bills |
| --- | --- | --- | --- | --- | --- |
| All appropriated (round 1) | 120 / 0 / 0 | $120B | $120B | $120B | $0 |
| **Lean tranche 1 (recommended first)** | 25 / 100 / 20 | **$28-40B (mid $32B)** | $165B | $129B | about +$1.20/month before system savings |
| Full program if tranche 1 delivers | 40 / 200 / 40 | $46-70B | $320B | $248B | about +$2.50/month before system savings |

**The three windows:**
- **Federal construction and grants** go only to lines no regional builder will build and to reconductoring on federal power-marketing systems.
- **Direct loans** go, at Treasury rates for 30-40 years, to a TVA-model federal transmission corporation, TVA, BPA, WAPA, public power and co-ops, repaid from transmission charges. They are scored at subsidy cost (1-8%). For scale, BPA's Treasury authority is $13.7B, rising to $17.7B in FY2028, and TVA's debt cap is $30B, unchanged since 1979. Both would need raising.
- **Capacity contracts** let DOE buy up to half of an anchor line's capacity for 10-20 years and resell it. This expands the Transmission Facilitation Program, whose $2.5B revolving fund was nearly used up after two rounds. The contracts carry Judgment Fund backing, so they are a disclosed contingent liability.

**Bills and delivery.**
- **Bills.** DOE's National Transmission Planning Study finds $1.60-1.80 of system cost saved per $1 of transmission, so bills should fall on net. That saving is not banked.
- **Delivery is the real limit, not money.**
  - About 888 miles of 345 kV-plus line were finished in 2024, against about 5,000 a year needed.
  - Interconnection queues held about 2,300 GW at the end of 2024.
  - Weak delivery cuts the grid's value by about 40%.

  The tranche 2 milestones are therefore physical: miles energized, transfer capability added and crews hired. A $5-15B electrical and grid workforce pipeline inside LAB-8/LAB-10 is a condition of both tranches.

## 5. Whole-package budget, 2030-39

Package A plus the core disaster tier, in $T nominal (low / mid / high). Detail is in the [pricing file](climate-portfolio-pricing.md).

| Item | D4 class | Financing | $T nominal |
| --- | --- | --- | --- |
| Credit redesign under stronger standards (ledger terms) | permanent | reduces CLI-1 | −0.18 / −0.26 / −0.35 |
| LMI bill protection, 2033-39 | permanent | general fund | +0.008 |
| Disaster core, permanent pieces | permanent | general fund | +0.02 / +0.04 / +0.08 |
| CLI-13 agricultural payments | permanent | general fund | +0.01 / +0.03 / +0.06 |
| Public grid, lean tranche 1 | time-limited capital | D4-B; loans repaid by transmission charges | +0.03 / +0.04 / +0.05 |
| Low-income heat-pump retrofits | time-limited capital | credit-redesign savings | +0.06 / +0.08 / +0.14 |
| Disaster core, capital pieces (mitigation fund, wildfire) | time-limited capital | D4-B | +0.05 / +0.08 / +0.11 |
| Clean-industry contracts | time-limited capital | process-fee receipts (+0.11) first | +0.02 / +0.03 / +0.05 |
| CLI-13 forests and carbon-removal purchases | time-limited capital | process-fee receipts first | +0.04 / +0.08 / +0.15 |

**Totals:**
- **Permanent items:** a net saving even after paying for the retrofits (−$0.06 to −$0.10T).
- **D4-B borrowing:** about $0.12T (0.09-0.16), about 61% of the freed room.
- **Process-fee receipts:** about $0.11T, against about $0.11T of contracts and removal purchases.
- **Not financed:** the disaster fuller tier (+$0.07T), still in development.

## 6. Reaching the higher goals: what's left

How far the model can go, adding steps cumulatively to Package A:

| Step | Net GHG below 2005: 2035 / 2040 / 2050 | Outlays (2025 $) | 2040 bill |
| --- | --- | --- | --- |
| Package A | 47% / 60% / 70% | −$71B | +$2.32 |
| + REV-C1H price ($150 by 2037) | 48% / 62% / 73% | −$50B | +$3.98 |
| + clean-heat standard (heat-pump premium removed from 2032) | 48% / 63% / 74% | −$25B | +$4.97 |
| + clean-industry support at 50% | 48% / 63% / 75% | +$29B | +$5.01 |
| + price to $200 by 2037 | 49% / 64% / 76% | +$128B | +$6.08 |
| + coal out by 2032 | 49% / 64% / 76% | +$113B | +$6.70 |

**CLI-13, outside the model**, adds 60-250 Mt in 2035 and 250-730 Mt in 2050 (mid 135 and 500, about 2 and 8 points). It costs about $45-175B over 2030-39, mostly for removal purchases, which grow to $60-120B a year by 2050 at 300 Mt.

**So with today's instruments the plan reaches roughly 50% in 2035 and 80-87% in 2050.** The 2035 NDC range and net zero need more. The next climate task should develop and price:
1. **Faster turnover:** trade-in and scrappage for old vehicles and furnaces, plus appliance standards (CLI-1E rebates, CLI-8C electric-ready lending).
2. **Industrial transformation:** a clean product standard (REV-C2B) and procurement at scale.
3. **Data-center load:** a clean load standard (CLI-6C).
4. **Larger and earlier removal**, with its cost growing after 2040.
5. **A second, faster-responding model** to check how much of the 2035 gap is this model's caution. The model responds more slowly than NEMS, REGEN and E3 in the first decade.

## 7. Single-lever findings (round 1, still valid)

These are in the [single-lever comparison](climate-portfolio-model-results.md):
- Public grid delivery costs about $24-43 per extra ton.
- Heat-pump credits are cheap per ton.
- Vehicle and wind/solar credits are expensive per extra ton while the fee and standards bind, but valuable as insurance.
- Retrofits cost about $190-260 a ton.
- The nuclear program costs about $300-340 a ton and is not selected; no reactor-fleet order.
- Adaptation is priced on loss reduction (the disaster file), not tons.

## Proposed deltas for Codex (not applied)

1. **CLI-1 revision (standard-led credit redesign with snap-back).** Revise CLI-1's working cost from $0.90T toward $0.55-0.72T nominal over 2030-39. That is the ledger-scaled redesign saving inside Package A, low end counted until scored.
2. **New CLI-10G, public grid delivery.**
   - Tranche 1: $25B budget authority (grants), $100B direct loan authority (FCRA subsidy about $3B) and $20B contract authority (expected cost about $4B).
   - Deficit cost about $0.04T nominal, D4-B time-limited.
   - Tranche 2 is contingent on milestones.
3. **CLI-5W, low-income heat-pump retrofits:** $67.5B (2025 $) over 2031-39, financed from the CLI-1 revision.
4. **CLI-9 clean-industry contracts:** about $0.03T nominal, paired with the process-emissions fee (+$0.11T receipts, REV-C1 coverage option) for joint scoring with the revenue work.
5. **CLI-3E and CLI-4E standards** (statutory; no direct outlay), and **CLI-7 disaster preparedness** (see that file).
6. **CLI-13 and the higher price (REV-C1H)** stay outside the selected baseline until Espen decides REV-C1H and the off-model estimates are refined.
7. **No change to REV-C3**, and no climate saving banked from abatement.

## Decisions

**Espen (goal level), recorded from this round.** Climate goals are revised higher: net zero by 2050, and the 2035 NDC range (61-66% below 2005) as the project's benchmark. Section 6 shows what remains to reach them.

**For Espen now.**
1. **REV-C1H.** Keep D7's start but raise the 2037 price from $100 to $150 a ton? It is the largest remaining lever (+2.3 Gt at no outlay). It costs the top two quintiles more, and the dividend keeps the bottom three positive.
2. **The disaster fuller tier** (insurance help and buyouts): fund now, or after the core tier and codes? I recommend after.

**Decided under the project-coworker delegation (recorded; reversible).**
- **Package A** is the recommended climate allocation and goes to Codex as proposed deltas.
- **Credits follow the standard-led step-down with snap-back.** This replaces round 1's "retain for now", because the package search shows the redesign on every efficient package.
- **Grid financing** uses the three windows, starting with the lean tranche.
- **Retrofits** are financed from credit savings rather than borrowing, to keep borrowing lower.
- **The process-emissions fee** is proposed with its receipts going first to clean-industry contracts and removal purchases.
- **CLI-7** is priced and its "unscored" status ends (disaster file).

## Limits

- **Assumed magnitudes.** One structural model, conservative in its first decade. The grid program's effect, the heavy-truck schedule, retrofit and workforce costs, and the industrial-support cost are planning estimates or assumptions, tested by sensitivity rather than scored.
- **Proxies.** The vehicle-standard and clean-heat cases are proxies.
- **Not modeled.** Credit snap-back and power-credit behavior after a 2037 repeal.
- **Outside the model.** CLI-13 figures are planning estimates.
- **What the costs are.** Outlays are model outlays plus named external costs, not CBO or JCT scores, and no Monte Carlo band is run on the differences.
- **Bills.** Before transmission cost recovery and system savings.

## Current-world facts used (checked October 26, 2026)

- **Wind and solar credits:** must have begun construction by about July 4, 2026, or be in service by the end of 2027 (IRS Notice 2025-42).
- **EVs:** the federal EV credit ended September 30, 2025. EV share fell from 7.8% (2025) to about 5-6% in 2026 (Cox Automotive and Edmunds via [NPR, Sept 30, 2026](https://www.opb.org/article/2026/09/30/one-year-after-the-end-of-the-ev-tax-credit-is-the-future-still-electric/); [Electrek](https://electrek.co/2026/03/27/used-ev-sales-boom-new-ev-sales-drop-28-percent-q1-2026/)).
- **Interconnection queues:** about 2,300 GW at the end of 2024 ([LBNL](https://emp.lbl.gov/publications/queued-2025-edition-characteristics)).
- **Transmission build:** 888 miles of 345 kV-plus line in 2024 against about 5,000 needed ([ACEG/Grid Strategies](https://cleanenergygrid.org/?p=14494)).
- **Transmission value:** $1.60-1.80 saved per $1 ([DOE NTP Study](https://www.energy.gov/node/4845558)).
- **Reconductoring:** less than half the cost of new lines for similar capacity ([GridLab/Berkeley](https://pv-magazine-usa.com/2024/04/24/reconductoring-could-enable-764-gw-of-transmission-connected-solar-by-2035/)).
- **Transmission Facilitation Program:** $2.5B borrowing authority, nearly used up ([DOE](https://www.energy.gov/edf/transmission-facilitation-program)).
- **BPA and TVA borrowing:** BPA $13.7B rising to $17.7B ([BPA testimony 2024](https://www.energy.gov/sites/default/files/2024-05/May%2016%202024%20HNR%20BPA%20Final%20Testimony.pdf)); TVA debt cap $30B ([CRS R43172](https://www.everycrsreport.com/reports/R43172.html)).
- **Grid award terminations:** DOE terminated about $7.56B of awards in October 2025.
- **FY2026 appropriations:** the Energy and Water act gave DOE about $49B (secondary summaries).
- **Conservation money:** OBBBA moved IRA conservation money into the EQIP/CSP baseline without climate targeting ([CRS IF13114](https://www.everycrsreport.com/files/2025-09-26_IF13114_d9ef5a7983a5670459a7562013109297a2bb79a4.html)).
- **Direct air capture:** projected at $230-540 a ton by 2050 ([ETH Zurich via Carbon Herald](https://carbonherald.com/new-study-places-future-direct-air-capture-costs-230-540-range/)).
- **NDC and Paris:** the U.S. NDC of December 2024 sets 61-66% by 2035; the Paris withdrawal took effect January 27, 2026. Rhodium projects 26-35% by 2035 under current policy ([Taking Stock 2025](https://rhg.com/research/taking-stock-2025/)).
- **Electricians:** BLS counts 818,700 in 2024 ([OOH](https://www.bls.gov/ooh/Construction-and-Extraction/Electricians.htm)).
- **Household electricity use:** EIA, 899 kWh a month ([FAQ 97](https://www.eia.gov/tools/faqs/faq.php?id=97&t=3)).
- Disaster sources are in [the disaster file](climate-portfolio-disaster-resilience.md).

## Proposed queue update (for integration)

Add a row: "Climate and grid portfolio allocation — review-ready (PR #26) | Claude Code | Package A (standard-led credits with snap-back, statutory CES 90/100 and vehicle standards, public grid via grants/loans/contracts, retrofits, clean-industry contracts, process fee) plus a priced CLI-7 disaster package; goal gap work next | `sources/climate-portfolio-*`, `index/tools/climate-portfolio/`, default-off carbon-model settings; deltas to Codex." Change the capacity row: rounds 1-2 merged, surge ~$105B and FY2029 $5B decided, integration in PR #24.

## Validation

- **Tests:**
  - `python3 index/tools/climate-portfolio/test_portfolio.py`: 12 checks pass.
  - `python3 index/tools/climate-portfolio/test_packages.py`: 26 checks pass, including every combination run, retrofit costs counted, frontier dominance, budget-cap winners verified, and committed outputs matching a fresh build.
  - `node index/tools/carbon/cfd-tests.js`: passes.
- **Rebuild:** `bash index/tools/run-all.sh` (dry run) leaves all 29 shared outputs unchanged.
