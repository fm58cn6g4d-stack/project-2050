# Climate and grid portfolio allocation

**Context.** Claude Code, October 26, 2026. Policy IDs: CLI-1 to CLI-13, REV-C1/C2/C3, CLI-2, Moving America's fuel steps (D7). Source base: `main` at `77f8a5e551367a52319e5323e8a33789894ebc67`; branch `claude/climate-portfolio`, draft PR #26. Status: completed for review, not merged. New: a common-baseline comparison of 24 model cases, a 26-row component register and a reproducible script. Nothing here changes an adopted design, a shared fiscal input or a generated shared output. The proposed deltas at the end go to Codex, the integration owner.

**Files.** This recommendation; the model results [climate-portfolio-model-results.md](climate-portfolio-model-results.md) (generated, with JSON alongside); the component register [climate-portfolio-components.csv](climate-portfolio-components.csv); the code in [index/tools/climate-portfolio/](../index/tools/climate-portfolio/README.md).

## Bottom line

1. **Add public grid delivery, in stages.** Fund a builder-of-last-resort and reconductoring program of about $120B (2025 dollars, roughly $0.15T nominal over 2030-39) as time-limited capital under D4-B. Release it in two tranches gated on delivery, with a workforce pipeline as a condition. In the model it is by far the cheapest addition per ton: about $24-43 per extra ton, avoiding 1.6 Gt of extra CO2 over 2030-50. It still avoids 1.0 Gt if delivery is weak, and it keeps working after a 2037 repeal because the lines stay built.
2. **Keep the clean-energy credits for now; do not bank any saving.** The credits differ a lot in value, and that finding should shape the next decisions:
   - The heat-pump credit is cheap per ton.
   - Industrial support does the most work, but it is unpriced.
   - The vehicle and wind/solar credits are expensive per extra ton in this model, because the fee, the Clean Energy Standard and the vehicle standards already do most of their work. Their value is insurance: if the fee is repealed or the standards are struck down, they matter much more. They also hold electricity bills down.
3. **Develop, don't yet fund, two further additions.**
   - Tripled low-income heat-pump retrofits: about $190-260 a ton, plus direct bill relief for low-income owners and renters.
   - A priced clean-industry procurement tranche (CLI-9, with no reactor-fleet order).
4. **Price adaptation on loss reduction, not tons.** A standing pre-disaster mitigation fund and CLI-7's scoring belong in a separate loss-and-vulnerability assessment. Federal mitigation grants save about $6 for every $1 spent (NIBS 2019).
5. **The package is far from the benchmark, and allocation alone won't close the gap.** The decided package reaches 43% below 2005 in 2035 and 64% in 2050 in this model, against the 2035 NDC range of 61-66% and net zero by 2050. The best portfolio here adds about 2 points in 2035. The model is conservative in the first decade, but the gap is a goal-level question for Espen (below).

## What was compared, and on what basis

**One baseline.** Every case starts from the carbon model's decided package (the `full` case behind [the carbon model report](../index/climate-carbon-model.md)). That package is:
- REV-C1 on the D7 price path, road fuels exempt, with the 80% dividend;
- CLI-1A's credits, CLI-3's 80% standard and CLI-4's standards;
- CLI-5's Weatherization heat pumps, CLI-6's grid statute and REV-C3's methane fee.

Each case then changes only the named levers, with the same physical assumptions throughout: costs, fuel prices, demand, transmission and the build pipeline. That is what "common baseline" means here. It reuses and extends the ten-case screen in [the October 26 redesign](fiscal-redesign-and-participation-2026-10-26.md) rather than starting a new model.

**What each column means.**
- **Cost.** The change in the model's spending accumulator (credits plus grid or nuclear program costs), plus any external cost named in the assumptions. It is in constant 2025 dollars and is a budget-cost proxy, not a score.
- **Basis.** It is not a social cost either. The model omits the cost of industrial support, so those cases carry no cost per ton.
- **Tons.** Energy CO2 avoided against the decided package over 2030-50, with the 2035 and 2050 endpoints in net greenhouse gases.
- **Bills.** Change in the average residential bill at 899 kWh a month.
- **Fee interaction.** Change in REV-C1 receipts and the per-adult dividend.

The full tables are in the [model results](climate-portfolio-model-results.md).

**The inventory** is in [the component register](climate-portfolio-components.csv). It has one row per climate instrument, split three ways:
- **Decided:** the D7 channel, CLI-1A split into four groups, CLI-3 to CLI-8 and Moving America's fuel steps.
- **Accepted for development on October 26:** public grid delivery, standing adaptation, targeted clean-industry procurement and workforce.
- **Options:** CLI-9 to CLI-13.

For each row the register gives the instrument, cost basis, D4 class, the authority/outlay distinction, liabilities, delivery bottleneck, durability and the model case that tests it.

## Findings

### 1. The credits are not one thing

Removing each credit group in turn from the decided package (2025 dollars; outlays over 2030-39, tons over 2030-50):

| Credit group | Outlays saved, 2030-39 | Extra CO2 lost, 2030-50 | Implied cost per ton kept | Bill effect if removed (2035/2040, $ a month) |
| --- | ---: | ---: | ---: | --- |
| Heat pumps (25C) | $28B | 0.37 Gt | about $80 | −0.21 / −0.39 |
| Industrial support and hydrogen (48C, 45V) | $89B (hydrogen only; industrial cost not modeled) | 0.81 Gt | unpriced | −0.29 / +0.28 |
| Vehicles (30D, 25E, 45W, 30C) | $454B | 0.40 Gt | about $1,350 | −0.13 / −0.22 |
| Wind, solar and storage (45Y/48E) | $431B | 0.21 Gt | about $2,600 | **+2.29 / +3.59** |
| Whole bundle (diagnostic) | $1,195B | 2.20 Gt | about $670 | +1.13 / +3.01 |

**Why vehicle and power credits score poorly here.** The model has the fee, the Clean Energy Standard and CLI-4's vehicle standards already pushing clean building up against the grid-access limit, so most credited projects would be built anyway. That matches the real bottleneck. The interconnection queue held about 2,300 GW at the end of 2024, and only 13% of capacity that applied in 2000-19 had been built (LBNL, *Queued Up 2025*).

**Their value is insurance.**
- If the fee is repealed from 2033, removing the wind and solar credits costs another 0.59 Gt and raises bills by $2-4 a month.
- If CLI-4's standards are struck down, the vehicle credits are worth about $290 a ton rather than $1,350.
- The whole-bundle diagnostic confirms the October 26 finding that grid delivery does not make the credits dispensable.

### 2. Public grid delivery is the strongest addition

| Case | Extra CO2 avoided, 2030-35 / 2030-50 | Net extra outlays, 2030-39 (2025 $) | Cost per extra ton (undiscounted / 3%) | Clean power 2035 |
| --- | --- | ---: | --- | --- |
| Public grid, as assumed | 0.36 / 1.62 Gt | $91B | $24 / $43 | 82% (package 76%) |
| Weak delivery (half the transmission and reconductoring gain) | 0.19 / 0.96 Gt | $118B | $101 / $129 | 79% |
| Twice the cost | 0.36 / 1.62 Gt | $211B | $98 / $127 | 82% |
| Built, then the fee and consumer credits repealed in 2037 | about 1.2 Gt more than repeal alone (2030-50) | $164B more than repeal alone | n/a | 81% |

**Why the net cost is lower than the program.** The program costs $120B, but net outlays are only $91B because cheaper delivered clean power reduces other modeled subsidy outlays. That offset is a model result, not a saving to bank.

**What the result depends on.** The physical gain is assumed: faster transmission growth and about 15 GW a year of reconductoring capacity. The direction is sourced (Berkeley/GridLab on advanced conductors), but the magnitude is a planning assumption, so it has to be earned by delivery. The delivery gap is real:
- **Transmission.** About 888 miles of 345 kV-plus line were finished in 2024 (revised FERC data), against about 5,000 miles a year needed (ACEG/Grid Strategies 2025, citing DOE's National Transmission Planning Study).
- **Federal grid programs.** In October 2025 DOE terminated about $7.6B of grid and other awards, and more GRIP money is stalled.

The gap between full and weak delivery, about 0.66 Gt, is what workforce, permitting and supply chains decide.

**The redirect test.** This asks whether the grid program could replace the wind and solar credits. In the model it does:
- It saves about $330B (2025 dollars) and still avoids 1.43 Gt more than the package.
- It still gains 0.78 Gt with weak delivery and breaks even on tons after a 2033 fee repeal.
- But it raises the average bill by about $2.50-4.70 a month, because the credits lower generation cost.

It also rests on one model's assumption about grid access, and the October 26 approval kept the credits during the comparison. **So I don't recommend redirecting now.** It is a staged option for after the first grid tranche has delivered, paired with bill protection. No saving is booked.

### 3. Household electrification, clean industry and firm power

- **Tripled low-income heat-pump retrofits** (+0.5 million homes a year, 2031-39):
  - Cost: about $67.5B ($45-113B), on a planning estimate of $10,000-25,000 a home. DOE's Weatherization cost-per-unit cap, about $8,500 in 2025 state plans, covers shell work, not a heat pump.
  - Effect: 0.35 Gt over 2030-50, about $190-260 a ton.
  - Its main value is that it cuts heating bills for low-income owners and renters, which tons don't capture.
  - It is moderately non-additive with the grid program: together they avoid 2.08 Gt for $233B net.
- **Clean industry.** Doubling the model's industrial support, as a proxy for CLI-9 contracts, avoids 0.49 Gt. The model books no cost for it, so there is no cost per ton until a contract price is set. Industry is the fee's largest base and its slowest-abating sector, so a priced procurement tranche is the right next piece of work.
- **Nuclear program** (the model's design, not a reactor fleet): about $300-340 a ton, 0.44 Gt. Paired with the grid it adds less than the sum of the two. This supports the October 26 direction not to preselect a fleet order.

### 4. Adaptation and workforce don't rank by tons

**Adaptation reduces losses rather than emissions.**
- NIBS (2019) finds that federal mitigation grants save about $6 per $1, and model building codes about $11 per $1.
- FEMA's BRIC program was cancelled in 2025. A federal court ruled the cancellation unlawful in December 2025, and FEMA said in March 2026 that it would release the remaining funds. That record argues for a standing, mandatory fund with anti-impoundment terms rather than a discretionary competition.
- I size a planning range of $3-6B a year for development, to be priced alongside CLI-7's unscored premium support and NFIP debt. It does not compete with credits on cost per ton.

**Workforce is a condition of delivery, not a separate abatement option.**
- BLS counts about 818,700 electricians in 2024 and about 81,000 openings a year.
- A grid program that cannot staff line crews and substations turns into the weak-delivery case.
- I put a $5-15B planning cost on an electrical and grid apprenticeship and instructor pipeline tied to the grid tranches, preferably carried inside LAB-8 or LAB-10 rather than as new money.

### 5. Durability under a hostile trifecta

D1 stipulates a Democratic Senate through 2036, so the stress test is a 2037 trifecta that repeals the fee and closes consumer credits to new claims. In the model:
- Power credits keep running in this case, which is a limit of the model.
- Cumulative CO2 is 4.1 Gt higher over 2030-50, and the 2050 endpoint falls from 64% to 58% below 2005.
- With the public grid built first, the loss is 2.9 Gt.
- A 2033 fee repeal costs 5.2 Gt.

Built assets, contracts with Judgment Fund backing, and numbers written in statute (CLI-4D/4E) survive; annual credits and the fee depend on the law staying put.

## Recommended allocation

| Action | Item | Money (2030-39) | D4 treatment | Status after this review |
| --- | --- | --- | --- | --- |
| Retain | REV-C1/C2/C3 and the Climate Dividend | channel | self-financing | decided; unchanged |
| Retain | CLI-1A credits at the ledger's $0.90T (0.60-1.10) | unchanged | permanent | decided; unchanged. Vehicle credits are the lead redesign candidate *if* money is needed (income-targeted, used-EV and trade-in focus), and only once CLI-4E puts vehicle numbers in statute |
| Retain | CLI-3 to CLI-8 and CLI-5F | unchanged | as decided | decided; unchanged |
| **Add** | **Public grid delivery (CLI-10G)**: tranche 1, $60B (2025 $), obligated 2030-31 for reconductoring and plan-selected lines where no regional builder acts; tranche 2, $60B, released on delivery milestones (miles energized, GW of transfer capability, crews hired) | about $0.15T nominal gross; about $0.10T net in model accounting | time-limited capital, borrowing-eligible inside the D4-B investment envelope; TVA/BPA/WAPA lending at subsidy cost | proposed working allocation (delegation decision below), for Codex to integrate |
| **Add (condition)** | Electrical and grid workforce pipeline tied to the tranches | $5-15B, inside LAB-8/LAB-10 | time-limited | proposed |
| Develop | CLI-5W: tripled low-income heat-pump retrofits | about $0.084T nominal ($0.056-0.14T) | to be classified; recommend time-limited grants | development; not funded until financed |
| Develop | Priced clean-industry procurement tranche (CLI-9, no reactor fleet) | contract price needed | full expected cost when obligated | development |
| Develop | Standing pre-disaster mitigation fund with CLI-7 scoring | $3-6B a year (planning) | design choice | development; separate loss-reduction assessment |
| Defer | Redirecting wind and solar credits to grid delivery | none booked | n/a | staged option after tranche 1 delivers, with bill protection |
| Defer | Nuclear/reactor fleet (CLI-9N) | none | n/a | option |

**Financing note.** On October 26 the agency rebuild surge (CAP-7S) was cut from $300B to about $105B, which leaves about $195B less borrowing inside the D4-B investment envelope. The grid program qualifies as the same kind of time-limited capital. Whether to use part of that room for it, or keep the lower borrowing, is a fiscal choice for the integration owner and Espen. It is not automatic.

## Proposed input deltas for Codex (not applied here)

1. **New program row CLI-10G, public grid delivery.**
   - Budget authority: $120B in 2025 dollars, about $0.15T nominal over 2030-39.
   - Timing: tranche 1 obligated FY2030-31, tranche 2 FY2032-33 subject to milestones. Outlays follow construction, roughly even over FY2031-39.
   - Classification: D4-B time-limited investment, general fund.
   - Do not net the model's ~$0.05T of subsidy offsets, and add no REV-C1 change to receipts. The model shows grid delivery lowering fee receipts by about $0.08T over 2030-39 as emissions fall. That is a real interaction for the channel, but it should be carried as a sensitivity, not a selected-baseline change, until Codex reconciles it with the incidence model's REV-C1 profile.
2. **Workforce condition: $5-15B inside LAB-10's $100B (or LAB-8), tagged to CLI-10G.** This adds no new money unless Codex finds LAB-10 fully committed.
3. **No change** to CLI-1, CLI-5 or the REV-C1/C2/C3 inputs, and no unscored climate saving.
4. **Not yet a delta:** CLI-5W retrofits, clean-industry procurement and the mitigation fund stay as development items until financed or priced.
5. **For the capacity integration (PR #24):** the DOE loan and grid office row (+400 staff, about $0.1B a year) was sized before CLI-10G. A public builder would also need TVA/BPA/WAPA or new-corporation project staff, mostly on their own balance sheets. I'd flag it as a known understatement rather than resize it now.

## Decisions

**For Espen (goal level).**
1. **Emissions benchmark.** Should the project's climate goal be the 2035 NDC range (61-66% below 2005) and net zero by 2050? The decided package reaches about 43% and 64% in this model. Closing that gap needs instruments beyond this allocation, not just a reallocation:
   - CLI-4D/4E statutory caps and vehicle numbers;
   - CLI-6C's clean load standard;
   - CLI-13 and REV-C1C's ratchet.

   It also needs a check of how conservative the model is in the first decade. If you set that goal, the next climate task is a gap-closing package. If not, the project should state the target it does hold itself to.
2. **Using freed D4-B room.** Should part of the ~$195B of borrowing room freed by the smaller rebuild surge carry the grid program, or should that lower borrowing be kept?

**Decided under the project-coworker delegation (recorded here; reversible).**
- Public grid delivery is the principal climate addition, staged in two milestone-gated tranches, with a workforce condition. It goes to Codex as a proposed working allocation, not as an integrated input.
- Credits stay at the decided level during this cycle. The wind/solar redirect and vehicle-credit retargeting are recorded as staged options, with no savings booked.
- Adaptation is assessed on loss reduction, separately from tons.
- The carbon model gained two cost settings (45W and 25C credit per sale). Their defaults reproduce existing outputs exactly.

## Limits

- **One model.** The model is a single structural model, extended from Espen's earlier project. It is slower to cut emissions in the first decade than the large published models and carries no reliability, air-quality or regional congestion value.
- **Assumed magnitudes.** The grid program's physical effect and cost, the retrofit cost and the workforce cost are planning assumptions. They are tested by sensitivity, not scored.
- **Incomplete costs.** The model omits the cost of industrial support, and it books only partial-repeal behavior for power credits after 2037.
- **What the cost column is.** It is undiscounted model outlays in 2025 dollars (a 3% discounted ratio is also shown). It is not a CBO score, and the ratios do not establish budget-neutral swaps.
- **Bills.** The retail price tracks generation cost and does not add transmission capital recovery, so ratepayer-funded lines would raise bills where federal funding does not.
- **Uncertainty.** No Monte Carlo band is run on the differences. The carbon model's own band for the package is 39-42% below 2005 in 2035.

## Current-world facts used (checked October 26, 2026)

- **FY2026 appropriations.** The FY2026 Energy and Water act was enacted in January 2026, with DOE at about $49B. The Loan Programs Office now operates as the Office of Energy Dominance Financing, with existing loan authority kept. These come from secondary summaries ([Mintz](https://www.mintz.com/insights-center/viewpoints/2151/2026-02-02-washington-update-sustainable-energy-infrastructure), [BCSE](https://bcse.org/?p=33136)); I did not verify them against the enacted text.
- **Wind and solar credits.** Credits require construction to have begun by about July 4, 2026, or service by the end of 2027, under IRS Notice 2025-42's physical-work test ([Wipfli](https://www.wipfli.com/insights/articles/tax-irs-notice-2025-42-new-guidance-on-beginning-of-construction)). That window has now closed. Household and vehicle credit end dates are as in [domain-climate.md](../domains/domain-climate.md).
- **Interconnection queue.** About 1,400 GW of generation and 890 GW of storage were queued at the end of 2024 ([LBNL Queued Up 2025](https://emp.lbl.gov/publications/queued-2025-edition-characteristics)).
- **Transmission build.** 888 miles of 345 kV-plus line in 2024 (revised), against about 5,000 a year needed ([ACEG/Grid Strategies](https://cleanenergygrid.org/?p=14494)).
- **Grid award terminations.** DOE terminated 321 awards (about $7.56B) in October 2025, including GRIP transmission awards ([RTO Insider](https://www.rtoinsider.com/tag/grid-resilience-and-innovation-partnerships-grip-program), [Canary Media](https://canarymedia.com/articles/politics/trump-blocking-billions-to-fix-grid)). Totals differ by source.
- **BRIC.** The cancellation was ruled unlawful in December 2025, and FEMA said in March 2026 that it would release the remaining funds ([Massachusetts AG](https://www.mass.gov/news/ag-campbell-secures-court-order-requiring-trump-administration-to-restore-billions-in-disaster-mitigation-funding)). I could not confirm later disbursement.
- **NDC and Paris.** The U.S. NDC of December 2024 sets 61-66% below 2005 by 2035 and net zero by 2050. The Paris withdrawal took effect January 27, 2026. Rhodium projects 26-35% below 2005 by 2035 under current policy ([Taking Stock 2025](https://rhg.com/research/taking-stock-2025/)).
- **Mitigation returns.** NIBS, [Natural Hazard Mitigation Saves 2019](https://www.nibs.org/files/pdfs/ms_v3_federalgrants.pdf): federal grants save $6 per $1.
- **Electricians.** BLS [Occupational Outlook Handbook](https://www.bls.gov/ooh/Construction-and-Extraction/Electricians.htm): 818,700 in 2024, about 81,000 openings a year.
- **Household electricity use.** EIA [FAQ 97](https://www.eia.gov/tools/faqs/faq.php?id=97&t=3): about 10,791 kWh a year (899 a month) in 2022.
- **Weatherization cost cap.** DOE Weatherization [average cost per unit](https://www.energy.gov/cmei/scep/wap/average-cost-dwelling-unit); the 2025 state plan maximum is about $8,500 (Oklahoma draft plan).

## Proposed queue update (for integration)

Add a row: "Climate and grid portfolio allocation — review-ready (PR #26) | Claude Code | Common-baseline comparison; recommends staged public grid delivery (~$0.15T nominal, D4-B) with a workforce condition, credits retained, retrofits/procurement/adaptation in development | `sources/climate-portfolio-*`, `index/tools/climate-portfolio/`; deltas to Codex." Change the capacity row to "rounds 1-2 merged; surge ~$105B and FY2029 $5B decided (PR #25); integration in PR #24."

## Validation

- **Tests.** `python3 index/tools/climate-portfolio/test_portfolio.py` passes all 12 checks:
  - the selected case reproduces the carbon model's decided package exactly;
  - cost-only changes leave emissions unchanged;
  - weak delivery is lower;
  - removing a credit group saves money and loses tons;
  - unpriced cases report no cost per ton;
  - combinations are non-additive;
  - the committed report matches a fresh build.
- **Carbon model.** `node index/tools/carbon/cfd-tests.js` passes.
- **Rebuild.** `bash index/tools/run-all.sh` (dry run) leaves every shared generated output unchanged.
