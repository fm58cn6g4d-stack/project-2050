# Climate and grid portfolio allocation

**Context.** Claude Code, October 26, 2026 (second round, updated after Espen approved the $150-by-2037 price and immediate funding of the fuller disaster tier; third update the same day on branch `claude/climate-financing`: price integrated into the shared ledger, floor measures in Package A, payment options and CLI-7C). Policy IDs: CLI-1 to CLI-13, REV-C1/C2/C3, CLI-2, Moving America's fuel steps (D7), CAP-7. Source base: `main` at `77f8a5e551367a52319e5323e8a33789894ebc67`; branch `claude/climate-portfolio`, PR #26. Status: completed for review, not merged.

**What's new in this round.** It follows Espen's direction: higher climate goals; grid payment that can include borrowing, direct loan authority and contract authority; lower borrowing kept where possible; credit caps or phase-downs if warranted; pricing everything; and optimizing packages rather than single policies. It adds:
- a search of every combination of eleven levers (13,824 packages; the clean-heat lever and a 50% industry option added Oct 26);
- a recommended package, with layering and stress tests;
- a credit phase-down timeline;
- grid financing windows;
- a whole-package budget;
- the disaster preparedness and response package ([its own file](climate-portfolio-disaster-resilience.md)).

The Oct 26 update changes shared inputs only for the approved price (Espen authorized Claude to make that integration while Codex was offline). Everything else here is a proposed delta for Codex.

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
   - a clean-heat standard (floor measure; Oct 26);
   - clean-industry support at 50% through contracts (floor measure, up from doubled; Oct 26);
   - the carbon fee extended to industrial process emissions;
   - clean-energy credits redesigned to step down as those standards and the grid take over.

   The $150-by-2037 price Espen approved on October 26 is now in the shared ledger (`carbon-parameters.csv`), so it is part of the decided package that every package is measured against. It is no longer a Package A lever.

   In the model Package A reaches 48% below 2005 in 2035, 63% in 2040 and 74% in 2050, against the decided package's 44%, 56% and 67% (both at the $150 price). Farms, forests and carbon removal (CLI-13, estimated outside the model) add about 2 points in 2035 and 8 in 2050. Its modeled climate outlays are about $12B above the decided package's over 2030-39. It still reaches 66% in 2050 after a 2037 repeal, against 58% for the decided package. With the floor measures included it meets the 50% domestic floor for 2035 at CLI-13's mid estimate, but only just (about 50.0%: 48.0% modeled plus 2.1 points). The clean-heat standard now starts in 2032, as designed (Codex review), which cost about 0.2 points. The margin is not robust.
2. **Yes, the credits should step down on a timeline.** Every efficient package redesigns them. The schedule is below. In ledger terms the redesign saves about $0.18-0.35T nominal over 2030-39 against the decided package; count the low end until scored. The savings are still about $53B in FY2040 (central) and reach zero soon after, because the decided package's credits also wind down.
3. **Finance the grid mostly with loans and contracts.** A lean first tranche ($25B grants, $100B direct loans, $20B capacity contracts) costs about $32B in deficit terms ($28-40B) and enables about $165B of construction. That is more than the earlier $120B all-grant program, at about a quarter of the budget cost. A full second tranche ($40B, $200B and $40B) follows if delivery milestones are met.
4. **Payment: O5, decided by Espen on October 27.** Process-emissions receipts pay the package's net general-fund cost, and the combustion fee keeps D7's 80/20 split (section 5). Under D7 as it stands, the package and the disaster tiers cost the general fund about +$79B over 2030-39 in the central case (+$166B conservative) and about $18B a year by FY2050. Under O5, FY2040 and FY2050 are at or below zero in all four cases. The cost to households: about $28-51 a year per consumer unit from the dividend over 2030-39 (lowest to highest quintile), and about $86-159 in 2050 (nominal). Over 2030-39 the general fund nets +$20B central (+$95B conservative).
   - **D4-B borrowing:** about $0.15T (0.11-0.21T), inside the ~$195B freed room except in the unfavorable case, which overshoots by about $17B. If that happens, slow tranche 2 or the buyout pace.
5. **The higher goals are not yet met, and the reason matters.** Espen raised the goals: net zero by 2050, and 61-66% below 2005 by 2035. Even with every instrument the model represents pushed hard (below), it tops out at about 49% in 2035 and 76% in 2050, or roughly 53% and 87% adding CLI-13's high estimates. International results (the [international file](climate-portfolio-international.md)) close most of the rest of the 2035 range. The domestic gap comes from how fast vehicle, building and equipment stocks turn over, and from this model being slower than the large published models in the first decade. Money is not what limits it.
6. **The approved price is now in the baseline.** It moved REV-C1 to $1.90T ($1.65-2.10T), the dividend to $1.52T and the CX offset to −$0.49T. This lowered the general-fund base by $0.11T and worsened DEC's FY2040 gap by about $18B, to about $72B. D3 is not settled: the fourth quintile's scenario-Q ten-year average falls from +$1,373 to +$1,261, but the mixed recovery case has Q4 at −$2,906 in FY2039 (Codex review). Household protection is the revenue settlement's job, not something this package secures.
7. **The reinsurance backstop (CLI-7C) is decided (Espen, October 27).** It is a Treasury facility above a 1-in-100-year loss, with a $150B cap, risk-priced premiums and TRIA-style recoupment. Expected net cost is about +$0.3B a year (−0.3 to +1.0), with a $75-150B disclosed contingent liability ([disaster file](climate-portfolio-disaster-resilience.md), D10).

## 1. How the search works

**The baseline.** Every package starts from the carbon model's decided package (case `full`): the D7 fee and dividend, CLI-1A credits, the 80% clean electricity standard, CLI-4 rules, Weatherization heat pumps, the grid statute and the methane fee. Each package is run with identical physical assumptions.

**The eleven levers.**
- credits: 4 designs;
- clean-power standard: 3;
- vehicle standards: 3;
- carbon price path: 2 (the approved $150 path, now the baseline, and the old $100 path for comparison);
- public grid: on or off;
- low-income retrofits: on or off;
- clean-heat standard: on or off;
- clean-industry support: 3 (decided 15%, doubled 30%, 50%);
- process-emissions fee: on or off;
- methane fee design: 2;
- coal retirement: on or off.

That gives 13,824 packages.

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
| Save at least $400B | credits redesigned, CES 90/100, grid, industry doubled, process fee | 46% / 58% / 68% | +2.1 | +$0.12 |
| Save at least $200B, bill under +$3 | credits redesigned, CES 90/100, vehicle standards, industry doubled, process fee | 46% / 59% / 72% | +4.2 | +$2.62 |
| About no added cost (Package A plus coal by 2032) | credits redesigned, CES 90/100, vehicle standards, grid, retrofits, clean heat, industry 50%, process fee, coal | 48% / 63% / 75% | +7.8 | +$2.84 |
| **Package A ($12B over the decided package)** | **the above without the coal lever** | **48% / 63% / 74%** | **+7.8** | **+$2.03** |

All rows are against the decided package at the approved $150 price. Coal retirement by 2032 adds about 0.04 Gt and saves about $19B of outlays inside Package A. It stays an option for its worker and community guarantees, not for tons.

**Layering: what each lever is worth inside Package A** (alone, then inside the package; Gt over 2030-50 / $B 2025 over 2030-39):

| Lever | Alone | Inside Package A | What the difference means |
| --- | --- | --- | --- |
| Credit redesign (standard-led) | −0.47 Gt / −$550B | −0.17 Gt / −$825B | Once standards bind, the credits pay for adoption the standards already require. Redesigning them saves more inside the package and costs fewer tons. |
| Statutory vehicle standards (cars and trucks) | +3.53 / +$480B | +3.97 / +$202B | The biggest single lever. Alone, it looks expensive only because kept EV credits pay out on mandated sales. |
| Public grid delivery | +1.84 / +$165B | +2.07 / +$61B | Worth more with the 90/100 standard and electrification: more clean load needs more grid. Alone, kept credits make it costlier. |
| Clean-heat standard (proxy, from 2032) | +0.75 / +$75B | +0.75 / +$22B | A floor measure, cheap per ton inside the package. |
| Clean-industry support at 50% | +0.86 / +$87B | +0.88 / +$87B | A floor measure. Financed from the carbon channel. |
| Low-income retrofits | +0.35 / +$119B | +0.30 / +$67B | Alone at $150, extra heat-pump load delays the IRA power-credit trigger by a year (about $51B more credits). Inside the package, with the trigger redesigned, only the $67.5B program cost remains. |
| CES 90% by 2035 / 100% by 2040 | +0.24 / $0 | +0.09 / $0 | Small in tons while the fee is in place. It is the backstop that holds power-sector cuts if the fee goes. |
| Process-emissions fee | +0.16 / about $0 outlay | +0.16 / $0; about +$0.24T receipts | Under O5 it pays the package's net general-fund cost. |

**What doesn't earn a place.**
- **Tripling the methane fee** without the certification exit *raises* emissions by 0.66 Gt. It weakens the incentive to certify against the leak standards, which cut methane 75%. Keep REV-C3 as decided.
- **Faster coal retirement** adds almost nothing on top of the fee (+0.06 Gt). Keep CLI-11 as an option for its worker and community guarantees, not for tons.

**Stress tests for Package A** (net GHG below 2005 in 2035 / 2050):

| Case | Package A | Decided package |
| --- | --- | --- |
| Central | 48% / 74% | 44% / 67% |
| Weak grid delivery | 47% / 74% | 44% / 67% |
| 2037 repeal (fee ends, consumer credits closed) | 46% / 66% | 42% / 58% |

Statutory standards and built grid assets are what survive a repeal.

**Households in 2035** (carbon channel, change against the decided package; the higher price raises both fee costs and the dividend):
- lowest quintile: +$40;
- second quintile: +$31;
- middle quintile: +$3;
- fourth quintile: −$79;
- top quintile: −$351.

The fourth quintile is the D3 group to test in Codex's incidence model.

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
- **Savings.** Standard-led alone saves $0.70T nominal over 2030-39 in the model, about $0.35-0.70T in ledger terms. Inside Package A it saves $1.05T in the model, because stronger standards raise credit claims if the credits are kept. Against the decided package, Package A's credit outlays are $0.18-0.35T lower in ledger terms over 2030-39 (industrial support is now a separate line). They fall to zero by about 2040.
- **What it costs.**
  - About 0.12 Gt inside the package.
  - A bill increase of about $4-28 a year per household over 2033-39. With the higher price the 2040 bill rises about $4 a month in total. Offsetting the bill increase for low- and moderate-income households costs about $19B nominal over 2033-39.
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

## 5. Whole-package budget by account, and how to pay for it

Package A plus both disaster tiers, measured against the decided package (which now carries the $150 price), in nominal $B. There are four cases: favorable / central / conservative / unfavorable. The cases pair savings and costs consistently. Conservative counts only the low end of credit savings (the project rule until scored) with central costs. Year-by-year paths and every item are in the [pricing file](climate-portfolio-pricing.md).

**Rules carried from review.**
- Under D7, 80% of added REV-C1 receipts go to the dividend and 20% to the transition share, and the general fund books a 25% tax offset (CX). Programs are financed only from the transition share; any shortfall is charged to the general fund.
- Industrial support is outside the credit saving.
- NFIP debt resolution is included.
- Removal purchases are outside the package.
- FY2040 and FY2050 test D4-B maturity.

| Item | Account | 2030-39 | FY2040 | FY2050 |
| --- | --- | --- | --- | --- |
| Credit redesign (ledger terms) | general fund | −354 / −266 / −179 / −179 | −70 / −53 / −35 / −35 | 0 |
| CX offset on the package's added REV-C1 receipts | general fund | +26 | 0 | 0 |
| LMI bill protection | general fund | +7 / +7 / +7 / +8 | +2 | +1 / +2 / +2 / +2 |
| Disaster permanent pieces (D2, D3, D6, D7, D8) | general fund | +41 / +78 / +78 / +135 | +5 / +9 / +9 / +16 | +6 / +12 / +12 / +20 |
| CLI-7C reinsurance, expected net cost (from FY2031) | general fund | −3 / +3 / +3 / +11 | 0 / 0 / 0 / +1 | 0 / 0 / 0 / +1 |
| NFIP debt resolution (FY2030) | general fund | 0 / +2 / +2 / +7 | 0 | 0 |
| CLI-13 agricultural payments | general fund | +12 / +31 / +31 / +62 | +1 / +3 / +3 / +7 | +2 / +4 / +4 / +9 |
| Low-income retrofits (paid from credit savings) | general fund | +56 / +84 / +84 / +140 | 0 | 0 |
| Public grid, lean tranche 1 | D4-B | +34 / +39 / +39 / +49 | 0 | 0 |
| Disaster capital (D1, D5, D9) | D4-B | +73 / +112 / +112 / +163 | 0 | 0 |
| Clean-industry contracts (50% support) | carbon channel | +74 / +110 / +110 / +146 | +14 / +21 / +21 / +27 | 0 |
| CLI-13 forests | carbon channel | +12 / +25 / +25 / +43 | 0 | 0 |

**The channel.** Against the new baseline the package adds only about $103B of REV-C1 receipts over 2030-39. Process coverage adds $244B, and faster abatement removes about $141B of combustion receipts. Under D7 the transition share gets only $21B against $134B of channel uses, so about $114B of shortfall falls on the general fund (central). That is the main reason the old "transition-share surplus" is gone. The price increase moved into the baseline, and the shared ledger credits its transition share (about $0.09T over 2030-39) to CLI-5, whose general-fund residual falls from $0.26T to $0.17T. That is part of why claims fell to $11.50T, so it is not available to the package.

**Paying for it: four options** (O4 withdrawn after review: it spent the step's transition share a second time) (general fund in nominal $B, favorable / central / conservative / unfavorable; dividend change per consumer unit against D7, lowest to highest quintile, central, nominal $):

| Option | GF 2030-39 | GF FY2040 | GF FY2050 | Dividend, 2030-39 average | Dividend, 2050 |
| --- | --- | --- | --- | --- | --- |
| O1. D7 as is | −151 / +79 / +166 / +378 | −49 / −17 / 0 / +19 | +9 / +18 / +18 / +33 | 0 | 0 |
| O2. 25% of added receipts to the GF (CX recapture) | −176 / +53 / +141 / +352 | −48 / −17 / +1 / +19 | +9 / +18 / +18 / +32 | −12 to −22 | −1 to −2 |
| O3. Process fee outside the dividend, surplus to the GF | −346 / −117 / −29 / +183 | −80 / −48 / −31 / −13 | −35 / −26 / −26 / −12 | −93 to −171 | −208 to −385 |
| **O5. Process receipts cover the package's remaining general-fund cost each year; rest follows D7** | **−209 / +20 / +95 / +234** | **−49 / −17 / 0 / 0** | **0 / 0 / 0 / 0** | **−28 to −51** | **−86 to −159** |

**Decided: O5 (Espen, October 27).**
- It is the only option at or below zero in FY2040 and FY2050 in every case. The package's permanent pieces (disaster D2-D8, farm payments, bill protection) are paid at maturity by the fee on the emissions that cause the losses.
- Process receipts leave the dividend only in years the package would otherwise draw on the general fund. That is why O5 costs households about a third of what O3 does.
- The combustion fee keeps D7's 80/20 split untouched. In 2035, a year with credit savings, the dividend is unchanged.
- O2 hardly moves the general fund, because the package adds few receipts against the new baseline.
- The ten-year central result is +$20B (+$95B conservative, with CLI-7C's expected cost); in those early years the credit savings, not process receipts, carry the package. The unfavorable case still needs about $234B over 2030-39 from the revenue work. That is the case where credit savings come in low and costs come in high.
- **Implementation:** the process-emissions fee is written like REV-C3, with its own receipts account. A statutory waterfall pays (1) the carbon-channel uses the transition share does not cover, then (2) the package's general-fund items each year, with any remainder going to the Climate Dividend. *Corrected after review (Oct 26):* the first version of O5 also spent the $150 step's transition share (about $93B), which the shared ledger already credits to CLI-5. Without it, O5 still meets the FY2040 and FY2050 test in every case, but its ten-year central result moves from −$68B to +$21B (+$17B after the clean-heat standard was moved to its 2032 start).

**Other notes.**
- **D4-B borrowing:** about $152B central ($108-212B), inside the ~$195B freed room except in the unfavorable case.
- **D1 is labeled "standing" but priced as a ten-year program.** If it continues past 2039, it adds about $4.5B a year (2025 dollars) to the permanent line, which O5's waterfall would also cover while process receipts last.

## 6. Reaching the higher goals: what's left

How far the model can go, adding steps cumulatively to Package A (the clean-heat standard and 50% industrial support are now inside it):

| Step | Net GHG below 2005: 2035 / 2040 / 2050 | Outlays (2025 $) | 2040 bill |
| --- | --- | --- | --- |
| **Package A (approved price, with the floor measures)** | **48.0% / 62.8% / 74.4%** | **+$12B** | **+$2.03** |
| + price to $200 by 2037 | 48.5% / 63.6% / 76.2% | +$33B | +$3.68 |
| + coal out by 2032 | 48.4% / 63.5% / 76.3% | +$15B | +$4.35 |

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

1. **CLI-1 revision (standard-led credit redesign with snap-back).** Revise CLI-1's working cost over 2030-39 from $0.90T toward about $0.72T, the low end of the ledger-scaled saving ($0.18-0.35T). The saving is zero after about 2040. Reconcile the split between CLI-1 and CLI-5's ITC and 45X lines; the scaling denominator spans both.
2. **New CLI-10G, public grid delivery.**
   - Tranche 1: $25B budget authority (grants), $100B direct loan authority (FCRA subsidy about $3B) and $20B contract authority (expected cost about $4B).
   - Deficit cost about $0.04T nominal, D4-B time-limited.
   - Tranche 2 is contingent on milestones.
3. **CLI-5W, low-income heat-pump retrofits:** $67.5B (2025 $) over 2031-39, financed from the CLI-1 revision.
4. **CLI-9 clean-industry contracts at 50% support:** about $0.11T nominal. **CLI-13 forests:** about $0.03T. Both are financed by the carbon channel under O5.
5. **The clean-heat standard (floor measure)**, the **CLI-3E and CLI-4E standards** (statutory; no direct outlay), and **CLI-7 disaster preparedness**, core and fuller tiers, both funded (see that file).
6. **The approved price: done in this PR** (Claude, acting for Codex with Espen's permission). It uses a kink parameter (`c1_slope_2037`, `c1_kink_year`), the shared ledger (C1, CX, CLI-2), the headline documents and an explicit education-bridge rebase (`index/tools/fiscal-recovery/comparison-rebase.json`). See the Codex handoff note.
7. **Payment (O5, decided Oct 27).** Add the process-emissions fee as a REV-C1 coverage line with its own account (about $0.24T gross, 2030-39). Book its waterfall: transition-share shortfall, then package general-fund items, then dividend. The $150 step's transition share stays with CLI-5, as `ledger-build.py` already computes; the CLI-5 row's own-revenue column (0.43) and note now say so.
8. **CLI-7C reinsurance (decided Oct 27):** a permanent line of about +$0.3B a year (−0.3 to +1.0) at expected net cost, plus a disclosed contingent-liability line of $75-150B in every D4 test.
9. **No change to REV-C3**, and no climate saving banked from abatement.

## Decisions

**Espen (goal level), recorded from this round.** Climate goals are revised higher: net zero by 2050, and the 2035 NDC range (61-66% below 2005) as the project's benchmark. Section 6 shows what remains to reach them.

**Espen, October 26 (after round 2):** "i approve the carbon price increase for 2037, and fund fuller disaster tier asap, not waiting for a federal reinsurance backstop, but let that be an open question for next turn."
- **Decided:** the 2037 price rises from $100 to $150 a ton, keeping D7's 2030-32 path. Package A includes it.
- **Decided:** the fuller disaster tier (D8 insurance help and D9 buyouts) is funded from FY2030 alongside the core tier. D8 does not wait for a reinsurance backstop; states must adopt CLI-8 codes within three years to keep it.
- **Open for next turn:** the federal reinsurance backstop (CLI-7C).

- **Designed Oct 26 (pending Espen):** the federal reinsurance backstop (CLI-7C, D10), recommended.

**Espen, October 26 (after the price integration):** "i'm ready to fix payment for climate. what do you recommend? ... i want to let you edit the carbon price adjustment since codex is offline"; "it's ok for you to make design choices in place of codex, just ask me to approve, and then leave clear notes for codex".
- **Done (authorized):** the $150 price is integrated into the shared inputs in this PR.
- **Decided by Espen, October 27** ("approve O5 and CLI-7C"): payment option O5 (section 5) and CLI-7C (the reinsurance facility, with a recoupment surcharge flat up to 1% and risk-weighted above).

**Decided under the project-coworker delegation (recorded; reversible).**
- **Package A** is the recommended climate allocation and goes to Codex as proposed deltas.
- **Credits follow the standard-led step-down with snap-back.** This replaces round 1's "retain for now", because the package search shows the redesign on every efficient package.
- **Grid financing** uses the three windows, starting with the lean tranche.
- **Retrofits** are financed from credit savings rather than borrowing, to keep borrowing lower.
- **Clean-industry contracts and forests** are financed from the transition share of the added receipts, not from receipts the dividend already uses.
- **Removal purchases** stay outside the package until they have their own financing and maturity test.
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
