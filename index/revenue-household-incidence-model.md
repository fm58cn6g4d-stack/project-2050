# Revenue: D3 household net test, incidence model v1.4

Oct 20, 2026 · Espen Swanson · Generated from index/2029-trifecta-master-ledger.md (education batch on top of the full rebuild: base $6.37T, gap $4.13T, about −$0.05T after every option) by index/tools/incidence-model.py, incidence-years.py and incidence-make-md.py. Role: index. Regenerate it rather than editing by hand.

This is a first pass at the test Dec. D3 sets: every income group below the top comes out ahead on net from the agenda's combined taxes, fees and benefits, and new general-fund revenue comes mostly from the top 1% and corporations. The unit is the bottom four quintiles, with the top quintile split out. Figures are average dollars per household per year over 2030-39 (nominal), from ten-year totals divided across about 140M households (estimate). Every distribution share is an **estimate** anchored to a published pattern; no row is yet a microsimulation.

**Planning basis (Decision Brief 1, Oct 20): scenario P.** Package B (C18, C35, C19b, C20) plus the top-end sprint package C38 (REV-TS1 to TS11, about $0.89T, mostly corporate and top-1% items) is now the planning basis; the program trims are not yet decided and are left out. Every quintile below the top comes out ahead: Q1 +$10,952, Q2 +$9,429, Q3 +$5,867 and **Q4 +$1,304** a household a year on the ten-year average, and 72% of the new general-fund revenue comes from the top 1% and corporations. Q4 is still behind in 2030 (about −$1,509), roughly even in 2031 (+$380) and +$1,800 by 2034. The 2030 dip is the remaining D3 exposure; its levers are unchanged (start C19b with the public option in 2031, or front-load the dividend).

**Decided package (Decision Brief 2, Oct 20): scenario Q.** Scenario P plus three top-end rows that replace the program trims: REV-TS12 (a 28% cap on itemized deductions above $450K, C39), REV-HP1 (the CEO pay-ratio corporate surtax, C40) and REV-HP3 (an excise on top-officer pay, C41), about $0.54T. No trim is taken, so universal meals (EDU-3) and Medicare dental (C5 declined) stay. Every quintile below the top comes out ahead: Q1 +$10,947, Q2 +$9,419, Q3 +$5,847 and **Q4 +$1,269** a household a year on the ten-year average (P: +$1,304); the new rows fall on the top quintile, above all the top 1% (−$570,874 against −$541,416 on P). 72% of new general-fund revenue comes from the top 1% and corporations (P: 72%). Q4 in 2030 is −$1,539, then +$349 in 2031 and +$1,794 by 2034.

**What changed in v1.4 (later on Oct 20, Espen's decisions).** The carbon fee moves to the durability session's price path ($25 a ton in 2030 rising to about $100 by 2037, road fuels still exempt): the fee is $1.35T, the Climate Dividend $1.08T and the low-income share of the transition money $0.108T over ten years, and all three now follow the fee's own year profile (low early, rising), so the fee's bite in 2030-31 is smaller than on the old path, and so is the early dividend. C35 (the estate tax) is restated as the ~$0.15T increment beyond G9. **Effects:** on scenario B the fourth quintile's ten-year average moves from +$779 to +$756 (the fee grows by $0.10T and the dividend plus low-income share by $0.09T; every quintile still comes out ahead). In 2030 the fourth quintile improves by about $100 (−$1,926 to −$1,823), and 2031 turns slightly positive; the first quintile gives up about $90 in 2030 because the early dividend is smaller too. Front-loading the dividend (paying the 2030 dividend at the 2031 rate from a Treasury advance repaid from later receipts) is the lever if that matters.

**What changed in v1.3 (Oct 20, education batch).** Education moved to its own domain file (domains/domain-education.md):
- **FAM-4 became EDU-1 and EDU-5** at the same $0.65T, so the old F4 row is now `EDU`.
- **EDU-3 universal school meals** ($0.27T) was added as a benefit on a new `meals` key (the increment over today's free and reduced-price meals lands mostly on the second to fourth quintiles).
- **EDU-4 educator pipeline** ($0.03T) was added as a benefit, and **EDU-7** (repealing the scholarship tax credit) as a $0.04T cost on donors.
- **New options:** C35 (the estate tax at 2009 parameters), C36 (meals at community-eligibility scale) and the EDU-9B education fund (an uncapped payroll contribution of about 1.4 points plus the new benefits it would add). **Scenario G** tests EDU-9B as the closer in place of C19 and C20; **scenario H** adds C35 to B.

v1.2's changes (housing, the public-safety package, LAB-8 and LAB-9) are carried forward.

## Bottom line

- **On the full options list (B), the bottom four quintiles all come out ahead; the fourth by about +$756 a household a year** (0.4% of income), up from +$546 in v1.2, mostly because universal meals reach it. The first three gain clearly: +$10,691, +$9,035 and +$5,314.
- **The employer health-exclusion cap (C19) is still the swing.** Without it the fourth quintile gains about +$2,229; with the cap at the 75th percentile, about +$1,451. Drop the hospital-price pass-through to wages and the full list lands at +$202 for the fourth quintile, which is a coin-flip.
- **The education fund (EDU-9B) passes the quintile test as a closer, but it is not free for the fourth quintile.** Replacing C19 and C20 with EDU-9B's contribution (about 1.4 points, all counted on workers) and its added benefits leaves the first three quintiles better off than B (+$11,111, +$9,371, +$5,600) and the fourth slightly worse (+$613 against +$756). It is roughly gap-neutral against B: it relieves the general fund of about $2.0T (claims moved into the fund plus current spending it absorbs) against the $1.92T of C19 and C20 it replaces. Whether to use a middle-reaching contribution at all is a D3 and D4 decision, not a modeling result.
- **The revenue-mix test passes** in every scenario: the top 1% (by incidence) and corporations (statutory) bear about 69% of new general-fund revenue on the full list and 86% on the base alone; the rule is more than half. EDU-9B's contribution is a dedicated fund and is not counted as general-fund revenue.
- **The estate tax (C35) is invisible below the top:** scenario H moves no quintile below the top and takes about $9,107 more a year from the top 1%.
- **The 80th-99th percentiles lose about $12,005 a year** on the full list, where C18 and C20 land.
- **Averages hide losers inside the fourth quintile.** A household there without children, without marketplace or Medicare coverage, and with employer coverage above the median premium gets few of the benefits and most of the costs; under EDU-9B the same household also pays the contribution and gets no school benefit. The next version needs within-quintile spread.

## Results by scenario

Net = benefits minus costs, dollars per household per year, 2030-39 average.

| Scenario | Q1 | Q2 | Q3 | Q4 | Q5 | 80-99th | Top 1% | Top 1% + corporations, share of new GF revenue | Passes? |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| A. Base package only (gap unfunded) | +$11,037 | +$9,760 | +$6,632 | +$2,721 | −$30,754 | −$8,569 | −$452,272 | 86% | Yes (but the gap is unfunded) |
| B. Base plus the full options list (gap about $0.2T) | +$10,691 | +$9,035 | +$5,314 | +$756 | −$36,541 | −$12,005 | −$502,736 | 69% | Yes |
| C. B without the employer-exclusion cap (C19) | +$10,780 | +$9,481 | +$6,385 | +$2,229 | −$35,157 | −$10,642 | −$500,950 | 81% | Yes |
| D. B with the exclusion cap at the 75th percentile (C19b) | +$10,733 | +$9,245 | +$5,819 | +$1,451 | −$35,888 | −$11,361 | −$501,893 | 74% | Yes |
| E. B with no premium pass-through from the price caps | +$10,637 | +$8,820 | +$4,885 | +$202 | −$37,077 | −$12,531 | −$503,450 | 69% | Yes |
| F. B with SAF-R2 (alcohol excise dropped) | +$10,721 | +$9,077 | +$5,366 | +$813 | −$36,474 | −$11,939 | −$502,636 | 69% | Yes |
| G. EDU-9B education fund as the closer in place of C19 and C20 | +$11,111 | +$9,371 | +$5,600 | +$613 | −$36,977 | −$12,447 | −$503,054 | 83% | Yes |
| H. B plus the estate tax (C35) | +$10,691 | +$9,035 | +$5,314 | +$756 | −$37,077 | −$12,089 | −$511,843 | 70% | Yes |
| P. Planning basis: Package B plus the sprint package (C18, C35, C19b, C20, C38; trims not yet decided) | +$10,952 | +$9,429 | +$5,867 | +$1,304 | −$38,835 | −$12,383 | −$541,416 | 72% | Yes |
| Q. Decided (Decision Brief 2): P plus TS12, HP1 and HP3 (C39-C41); no trims | +$10,947 | +$9,419 | +$5,847 | +$1,269 | −$40,693 | −$12,789 | −$570,874 | 72% | Yes |

Scenario B adds the options that reach households: C18, C19 (median), C20 and C5. The other options (C17, C21, C29-C34, C36) do not reach households directly through a tax. Scenario G swaps C19 and C20 for EDU-9B (its contribution EDUP, its added benefits EDUB, and the estate tax dedicated to the fund). Scenario A fails D4 (the gap is unfunded) and is shown for comparison only.

### As a share of income (scenario B)

| | Q1 | Q2 | Q3 | Q4 | Q5 | Top 1% |
| --- | --- | --- | --- | --- | --- | --- |
| Benefits | $12,325 | $12,027 | $9,930 | $7,376 | $4,853 | $3,718 |
| Costs | $1,634 | $2,992 | $4,616 | $6,620 | $41,394 | $506,454 |
| Net, % of income | +46.5% | +15.1% | +5.1% | +0.4% | -7.0% | -11.7% |

Health benefits are valued at government cost, as CBO does, so the bottom quintile's gain is large relative to cash income. Most of it is coverage, not cash.

## What moves the fourth quintile (scenario B)

| Item | Benefit or cost | Per Q4 household a year |
| --- | --- | --- |
| C19: Cap the employer health exclusion | cost | $1,473 |
| C1: Carbon fee (domestic) | cost | $1,157 |
| H3: Public option and cost-sharing help (HLT-3) | benefit | $1,154 |
| P1: Paid-leave contribution 0.6% | cost | $964 |
| F3: Paid leave benefits (FAM-3) | benefit | $900 |
| H1: Health restoration (HLT-1) | benefit | $875 |
| E2d: Climate Dividend (CLI-2, 80%) | benefit | $849 |
| H2: Medicare upgrades, gross of premiums (HLT-2) | benefit | $783 |
| G1: Corporate rate to 28% | cost | $737 |
| F1: Child Tax Credit (FAM-1) | benefit | $643 |
| H5p: Hospital and drug price caps: lower employer premiums passed to wages | benefit | $554 |
| EDU: Education formula funding and higher education (EDU-1, EDU-5; was FAM-4) | benefit | $395 |
| MR: Moving America fuel steps and per-mile charge | cost | $366 |
| F2: Child care and pre-K (FAM-2) | benefit | $279 |
| E1h: Clean-energy credits, household share (30% of CLI-1) | benefit | $270 |
| EDU3: Universal school meals and Summer EBT (EDU-3) | benefit | $251 |
| PB: Part B premium increase (a quarter of HLT-2's new benefits) | cost | $214 |
| MA: MA plans' reduced extras after full capture (30% pass-through) | cost | $214 |
| G7: Foreign income at full rate | cost | $183 |
| G5: Buyback tax 4%, corporate minimum 21% | cost | $179 |
| C18: Top four brackets +1, gains +2, LIFO | cost | $177 |
| G10: Financial transaction tax | cost | $171 |
| C2: Carbon border adjustment | cost | $171 |
| C5: Dental starts after the window | benefit | $171 (negative) |
| E12: AI and work transition support (AI-4) | benefit | $157 |

## By year (v1.4)

Each ten-year total is spread over 2030-39 by a phase-in profile: about 4% annual growth for every row, plus ramps (estimates). Child care reaches the full cap in 2032. The public option opens in 2031 and auto-enrolls in 2032. Medicare hearing and vision start in 2031 and dental in 2033 (removed in-window under C5). Paid-leave benefits start in 2031 while contributions start in 2030. Moving America's fuel steps phase in through 2038. National service ramps to its 2034 scale, and the public-safety receipts start in 2031. **New in v1.3:** universal meals start with the 2030-31 school year, the IDEA glide path and Pell ramp, and the educator pipeline is front-loaded. Net dollars per household, nominal.

| Year | B: Q1 | Q2 | Q3 | Q4 | D (cap at 75th pct): Q4 | G (EDU-9B closer): Q4 |
| --- | --- | --- | --- | --- | --- | --- |
| 2030 | +$6,544 | +$4,163 | +$1,232 | **−$1,823** | −$1,244 | −$2,198 |
| 2031 | +$8,350 | +$6,633 | +$3,599 | **+$53** | +$656 | −$231 |
| 2032 | +$9,799 | +$8,480 | +$5,153 | **+$990** | +$1,617 | +$842 |
| 2033 | +$10,274 | +$8,893 | +$5,423 | **+$1,072** | +$1,724 | +$993 |
| 2034 | +$10,821 | +$9,400 | +$5,781 | **+$1,235** | +$1,913 | +$1,154 |
| 2035 | +$11,287 | +$9,779 | +$5,972 | **+$1,216** | +$1,921 | +$1,131 |
| 2036 | +$11,735 | +$10,146 | +$6,162 | **+$1,198** | +$1,931 | +$1,110 |
| 2037 | +$12,211 | +$10,535 | +$6,361 | **+$1,177** | +$1,939 | +$1,085 |
| 2038 | +$12,684 | +$10,932 | +$6,584 | **+$1,184** | +$1,977 | +$1,089 |
| 2039 | +$13,201 | +$11,384 | +$6,869 | **+$1,256** | +$2,080 | +$1,157 |

- **The fourth quintile is behind in 2030 and about even in 2031** on scenario B (−$1,823 and +$53), then positive from 2032 and near +$1,250-1,300 from 2034. Universal meals help from late 2030; the early-year shortfall is still the carbon fee, leave contributions and the exclusion cap arriving before the public option and full child care.
- **Year five (2034) passes for every quintile in every scenario**, which is D3's interim test. The 2030 shortfall still lands just before the November 2030 midterm.
- **The 75th-percentile cap (D) turns Q4 positive from 2031**, but 2030 is still about −$1,244. **EDU-9B (G) is worse in 2030-31** (−$2,198, −$231) because the contribution starts at full rate while pre-K seats ramp; starting the contribution with the 2031 school year, or at a lower first-year rate, is the lever.
- **Fixing 2030 is a sequencing choice, not a size choice.** The levers: start C19 and the carbon fee in 2031, front-load the Climate Dividend, or start leave contributions with benefits in 2031. Each costs about a year of revenue and needs a D4 check.

## Implications for open choices

These are options with their effects, not edits to any canonical file.

1. **C19, the exclusion cap.** At the median premium it decides the fourth quintile. The 75th-percentile version passes with more margin and reopens about $0.59T of the gap.
2. **EDU-9B, the education fund.** As a closer it beats C19 and C20 for the bottom three quintiles and costs the fourth about $140 a year against B. It needs Espen's call under D3 (a middle-reaching contribution) and D4 (a new dedicated fund) before it can be chosen.
3. **C35, the estate tax.** Pure top-end revenue; adding it lets one middle-reaching option go.
4. **SAF-R2.** Dropping the alcohol excise helps every quintile a little and the fourth by about $60 a year. It moves about $0.07T onto the top-end base.
5. **The Climate Dividend.** Shifting part of the 20% transition share into the dividend (CLI-2C) helps every quintile equally.
6. **Before final:** the hospital-price pass-through (H5p) remains the assumption most able to flip the result; it needs a sourced estimate.

## Dynamic effects and the D3 test (Oct 20)

The ledger now carries a dynamic sensitivity table (not in any total): under CBO/JCT-style conventions macroeconomic feedback is about −$0.56T over 2030-39 (−$1.42T to +$0.28T), and about +$0.55T under Talarico-style assumptions (estimates). It does not change the quintile results above, for three reasons. **Most of it is revenue, not household money:** the largest row is lower investment and more avoidance by corporations and the top 1%, which lands on the top quintile and the gap, not on the bottom four. **The household-facing pieces roughly offset:** the care labor-supply gain (about +$0.22T) raises earnings mostly in the second to fourth quintiles, while the small labor-supply drag from coverage and the Child Tax Credit falls on the same groups through slightly lower hours, a choice the household makes rather than a cost imposed on it. **Wage effects of corporate taxes are already in:** the model puts 25% of corporate taxes on workers (the JCT/CBO convention), which is the channel a dynamic score would otherwise add. If a dynamic gap had to be closed with middle-reaching revenue (C19 or C20) rather than top-end options, that choice would move the quintiles and should be run as its own scenario.

## Limits of v1.4

- **Shares are estimates.** Each row uses a pattern key; replacing them with published TPC and CBO tables is v2. The new `meals`, `donors` and `estate` keys are estimates.
- **Year profiles are shapes, not scored annual paths.**
- **No behavior.** Coverage shifts, avoidance beyond the ledger's 15% haircuts, and macro effects are left out (the education session's maternal-employment effect, plausibly $25-45B a year of federal revenue at maturity, is not counted).
- **Public goods are left out** on both sides: the agency rebuild, transit service, climate credits to firms, defense, education research (EDU-8) and the civic and information rows.
- **Full pass-through** of carbon, border, transport and alcohol charges to households, which is conservative for the middle. EDU-9B's contribution is counted entirely on workers.
- **Corporate taxes** use the JCT/CBO convention: 25% labor, 75% capital.
- **Not modeled:** the minimum wage (LAB-4), the H-1B fee, COM-5's bank-fee limits (a household benefit), veterans health (NSC-10), and immigration's legalization effects.

## Model inputs

| ID | Instrument | Side | 2030-39 ($T) | Key | Basis |
| --- | --- | --- | --- | --- | --- |
| G1 | Corporate rate to 28% | cost | 1.65 | wages, capital | ledger; 25/75 incidence |
| G5 | Buyback tax 4%, corporate minimum 21% | cost | 0.4 | wages, capital | ledger; 25/75 incidence |
| G7 | Foreign income at full rate | cost | 0.41 | wages, capital | ledger; 25/75 incidence |
| G3 | 39.6% top rate above $400K | cost | 0.3 | above400k | ledger |
| G9 | 2025 cuts reversed above $450K | cost | 1.45 | above450k | ledger |
| G11 | Mark-to-market for billionaires | cost | 0.65 | billionaires | ledger |
| G6 | Gains taxed at death | cost | 0.7 | death_gains | ledger |
| H1b | Medicare/NIIT to 5% above $400K | cost | 0.5 | inv400k | ledger |
| GX | Overlap and avoidance haircut | cost | -0.495 | above450k | ledger |
| G8 | IRS enforcement | cost | 0.4 | enforcement | ledger |
| G10 | Financial transaction tax | cost | 0.4 | ftt | ledger |
| H1a | NIIT on active pass-through income (HI) | cost | 0.5 | inv400k | ledger |
| O1 | SS tax above $250K (SS-1) | cost | 1.9 | above250k_wages | ledger |
| O2 | SS tax on investment income above $400K, net of haircut | cost | 0.935 | inv400k | ledger |
| P1 | Paid-leave contribution 0.6% | cost | 0.9 | wages_cap | ledger; both halves on workers |
| C1 | Carbon fee (domestic) | cost | 1.35 | energy | ledger (durability path, Oct 20); full pass-through to households |
| C2 | Carbon border adjustment | cost | 0.2 | consumption | ledger; full pass-through |
| MR | Moving America fuel steps and per-mile charge | cost | 0.41 | gasoline | ledger MR1+MR2 |
| MRc | Moving America truck, rail and aviation charges | cost | 0.126 | consumption | ledger MR4+MR5 |
| PS1 | Safe Everywhere revenue title, durable sources (alcohol $0.07T, fraud assessment $0.012T, firearms and check fees $0.009T) | cost | 0.091 | alcohol, consumption | ledger PS1 restated Oct 20; full pass-through |
| PB | Part B premium increase (a quarter of HLT-2's new benefits) | cost | 0.3 | partb | estimate from go-big tab (~$18/month) |
| MA | MA plans' reduced extras after full capture (30% pass-through) | cost | 0.375 | ma | estimate: 30% of HLT-6's $1.25T |
| EDU7 | Scholarship tax credit repealed (EDU-7): donors lose the credit | cost | 0.04 | donors | ledger EDU-7 (new Oct 20) |
| F1 | Child Tax Credit (FAM-1) | benefit | 1.5 | ctc | ledger |
| F2 | Child care and pre-K (FAM-2) | benefit | 0.6 | childcare | ledger |
| F3 | Paid leave benefits (FAM-3) | benefit | 0.9 | leave_benefit | ledger |
| EDU | Education formula funding and higher education (EDU-1, EDU-5; was FAM-4) | benefit | 0.65 | education | ledger (FAM-4 split Oct 20, same total) |
| EDU3 | Universal school meals and Summer EBT (EDU-3) | benefit | 0.27 | meals | ledger EDU-3 (new Oct 20) |
| EDU4 | Educator pipeline (EDU-4) | benefit | 0.03 | education | ledger EDU-4 (new Oct 20) |
| H1 | Health restoration (HLT-1) | benefit | 2.45 | aca_medicaid | ledger |
| H2 | Medicare upgrades, gross of premiums (HLT-2) | benefit | 1.37 | medicare | ledger 1.07 + premiums 0.30 |
| H3 | Public option and cost-sharing help (HLT-3) | benefit | 1.9 | public_opt | ledger |
| H4 | Medicaid, long-term care, safety net (HLT-4) | benefit | 0.625 | medicaid_ltc | ledger |
| H5p | Hospital and drug price caps: lower employer premiums passed to wages | benefit | 0.5 | employer_cov | estimate (go-big tab ~6% premium cut; conservative) |
| F5 | Social Security minimum benefit and CPI-E (SS-3, SS-4) | benefit | 0.25 | ss_benefit | ledger |
| E2d | Climate Dividend (CLI-2, 80%) | benefit | 1.08 | persons | ledger (durability path, Oct 20) |
| E2t | Carbon transition share: low-income energy help (40% of $0.27T) | benefit | 0.108 | low_income_energy | estimate |
| HOU | Housing (HOU-1 to HOU-6 fund, HOU-8: vouchers, emergency aid, credits, repair) | benefit | 0.47 | housing | ledger HOU-1 (was E6 $0.60T) |
| E1h | Clean-energy credits, household share (30% of CLI-1) | benefit | 0.27 | hh_clean | estimate: 30% of CLI-1's $0.9T |
| E12 | AI and work transition support (AI-4) | benefit | 0.2 | workers_ai | ledger |
| LAB8 | Registered apprenticeships (LAB-8) | benefit | 0.03 | education | ledger (new Oct 20) |
| LAB9 | National service stipend and education award (LAB-9) | benefit | 0.12 | service | ledger (new Oct 20) |
| C18 | Top four brackets +1, gains +2, LIFO | cost | 0.62 | brackets_top | ledger option |
| C19 | Cap the employer health exclusion | cost | 1.25 | exclusion_cap | ledger option |
| C19b | Cap the employer health exclusion at the 75th percentile (CBO alt. 2, scaled) | cost | 0.66 | exclusion_cap | ledger option |
| C20 | 1-point surtax above $100K/$200K | cost | 0.67 | surtax | ledger option |
| C38 | Top-end sprint package REV-TS1 to TS11, net of a 10% haircut (corporate items on the 25/75 convention) | cost | 0.89 | wages, capital, estate, above400k, capital, above450k | ledger option |
| C39 | 28% cap on the value of itemized deductions above $450K (REV-TS12; Decision Brief 2) | cost | 0.4 | above450k | ledger option |
| C40 | CEO pay-ratio corporate surtax (REV-HP1; 25/75 convention; Decision Brief 2) | cost | 0.08 | wages, capital | ledger option |
| C41 | 21% excise on top-officer pay above $1M (REV-HP3; executives in the top 1%; Decision Brief 2) | cost | 0.06 | billionaires | ledger option |
| C5 | Dental starts after the window | benefit | -0.3 | medicare | ledger option |
| SAFR2 | SAF-R2: drop the alcohol excise (replaced with top-end revenue, not modeled here) | cost | -0.07 | alcohol | ledger option |
| C35 | Estate tax at 2009 parameters, exemption frozen (REV-E1), increment beyond G9 | cost | 0.15 | estate | ledger option |
| C36 | Meals at community-eligibility scale (EDU-3B) instead of universal | benefit | -0.19 | meals | ledger option |
| EDUP | EDU-9B education contribution, ~1.4 points uncapped payroll (all on workers) | cost | 2.27 | wages | ledger option |
| EDUB | EDU-9B new benefits beyond the chosen rows (pre-K and child care share, teacher floor, PARA, Title I and IDEA top-ups) | benefit | 0.63 | childcare, education | ledger option |

**Distribution keys** (percent of the total by quintile, Q1 to Q5, and the top 1%'s share of the total). All are estimates; `meals`, `donors` and `estate` are new in v1.3.

| Key | Q1 | Q2 | Q3 | Q4 | Q5 | Top 1% |
| --- | --- | --- | --- | --- | --- | --- |
| wages | 3 | 9 | 16 | 26 | 46 | 12 |
| wages_cap | 3 | 10 | 19 | 30 | 38 | 3 |
| capital | 1 | 2 | 4 | 8 | 85 | 50 |
| consumption | 9 | 14 | 19 | 24 | 34 | 4 |
| alcohol | 12 | 17 | 21 | 23 | 27 | 2 |
| energy | 11 | 15 | 20 | 24 | 30 | 3 |
| gasoline | 10 | 16 | 21 | 25 | 28 | 1.5 |
| persons | 15 | 18 | 21 | 22 | 24 | 1 |
| above400k | 0 | 0 | 0 | 0 | 100 | 70 |
| above450k | 0 | 0 | 0 | 0 | 100 | 80 |
| above250k_wages | 0 | 0 | 0 | 2 | 98 | 55 |
| billionaires | 0 | 0 | 0 | 0 | 100 | 100 |
| death_gains | 0 | 0 | 0 | 0 | 100 | 85 |
| estate | 0 | 0 | 0 | 0 | 100 | 85 |
| inv400k | 0 | 0 | 0 | 0 | 100 | 85 |
| enforcement | 2 | 4 | 6 | 8 | 80 | 55 |
| ftt | 1 | 3 | 6 | 12 | 78 | 40 |
| donors | 0 | 2 | 8 | 25 | 65 | 20 |
| ctc | 33 | 30 | 21 | 12 | 4 | 0 |
| childcare | 28 | 30 | 24 | 13 | 5 | 0 |
| education | 24 | 26 | 22 | 17 | 11 | 0.5 |
| meals | 8 | 20 | 27 | 26 | 19 | 0.5 |
| service | 26 | 28 | 22 | 15 | 9 | 0 |
| housing | 60 | 25 | 10 | 4 | 1 | 0 |
| aca_medicaid | 38 | 30 | 19 | 10 | 3 | 0 |
| medicare | 24 | 26 | 21 | 16 | 13 | 1 |
| partb | 15 | 24 | 23 | 20 | 18 | 1 |
| ma | 22 | 27 | 23 | 16 | 12 | 0.5 |
| public_opt | 18 | 30 | 27 | 17 | 8 | 0 |
| medicaid_ltc | 50 | 25 | 14 | 7 | 4 | 0 |
| employer_cov | 3 | 12 | 24 | 31 | 30 | 2 |
| ss_benefit | 30 | 28 | 20 | 13 | 9 | 0.5 |
| leave_benefit | 8 | 17 | 24 | 28 | 23 | 1 |
| hh_clean | 8 | 14 | 22 | 28 | 28 | 2 |
| workers_ai | 15 | 25 | 28 | 22 | 10 | 0 |
| low_income_energy | 60 | 40 | 0 | 0 | 0 | 0 |
| brackets_top | 0 | 0 | 1 | 8 | 91 | 50 |
| exclusion_cap | 2 | 10 | 24 | 33 | 31 | 2 |
| surtax | 0 | 0 | 0 | 6 | 94 | 55 |

Other assumptions (estimates): about 140M households mid-window; 2034 average incomes of $23K, $60K, $105K, $180K and $520K by quintile, and $4.3M for the top 1%; 30% of Medicare Advantage capture passes to enrollees as fewer extras; 30% of clean-energy credits go to households; $0.30T of Part B premiums; $0.50T of hospital-price savings passed to wages. EDU-9B: ~1.4 points of uncapped payroll at ~$135B a point in 2030 growing 4% ($2.27T in 2030-39); $0.63T of benefits beyond the chosen rows (pre-K and child care share $0.24T; teacher floor, PARA and mental-health staff, Title I and IDEA top-ups $0.39T), from domains/domain-education.md.

## Sources

- [CBO, The Distribution of Household Income, 2022](https://www.cbo.gov/publication/62300)
- [CBO budget option, Reduce Tax Subsidies for Employment-Based Health Benefits](https://www.cbo.gov/budget-options/60953)
- [Fremstad and Paul, PERI WP434](https://peri.umass.edu/images/publication/WP434.pdf)
- [TPC TaxVox, Who benefits from health-care related tax expenditures?](https://taxpolicycenter.org/taxvox/who-benefits-health-care-related-tax-expenditures)
- [Tax Foundation on JCT's corporate incidence convention](https://taxfoundation.org/jct-corporate-tax-falls-partly-labor/)
- [CBO budget option 52284, alcohol at $16 per proof gallon (2016)](https://www.cbo.gov/budget-options/2016/52284)
- sources/education-transforming-education-act-analysis-and-trust-fund.md: EDU-3's increment and EDU-9B's rates and spending paths
- index/2029-trifecta-master-ledger.md and the domain files for every amount
