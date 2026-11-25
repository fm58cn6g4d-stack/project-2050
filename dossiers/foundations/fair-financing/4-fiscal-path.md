# Stage G step 8: the fiscal path review

Role: the harder look at spending and debt that Espen started at the stage G boundary review (`DEC-2026-11-24-14`). It prices the three debt goals (`DEC-2026-11-24-15`), checks the budget model's and the long-term tools' methods, and adds a contained dynamic layer beside the conventional score. Later parts cover phasing, revenue, outside proposals, G8 and the decision batch (step 8b), and step 8c's budget process, debt limit and central rules ([`5-budget-process.md`](5-budget-process.md), memos G20-G22) and the strategy memo ([`6-strategy-memo.md`](6-strategy-memo.md)). Status: **parts 1 and 2 drafted in stage G step 8a (#483); parts 3 to 6 and the decision batch (memos G15-G19) in step 8b, November 24, 2026; the batch decided November 25** (`DEC-2026-11-25-01` to `-05`: G15 B made more aggressive, G16 B, G17 B, G18 D′, G19 B to be re-checked). Step 9's revision for those answers, the redrafted debt path (G23), G19's mix with a VAT (G24) and the CLI-1 correction (G25), is [`7-batch3-revision.md`](7-batch3-revision.md); the figures here are step 8's, before that revision. Step 8c's budget process and strategy memo are in [`5-budget-process.md`](5-budget-process.md) and [`6-strategy-memo.md`](6-strategy-memo.md). Nothing here is booked. The settlement as booked (#480, [`2-settlement.md`](2-settlement.md)) stays the plan's fiscal base (`DEC-2026-11-24-10`). This part recommends no goal: the goals draw on the same money, so step 8b recommends one, with the frontier below, in the decision batch.

Units: federal fiscal years, nominal $B or % of GDP. Project arithmetic on exploratory models, not official scores.

**The rules this review keeps** (Espen's directions, `DEC-2026-11-24-14` to `-18`; step 8a's brief):
- **Start populist in 2029** (`-18`): minimal new revenue from the middle class in the first years. As step 8 ran: no VAT (`DEC-2026-11-20-07`). **Since `DEC-2026-11-25-01`, a VAT or other broad measures are allowed, but not in the plan's first few years;** step 9 prices that ([`7-batch3-revision.md`](7-batch3-revision.md)).
- **Social Security's and Medicare's long-run finances are out of scope** (`-16`).
- **The hard rule.** Any debt goal the review recommends must be met on the conventional score with zero "works as designed" or dynamic savings. Those may only widen the margin, or lower a rate later through a trigger once they show up in measured results.

## In plain terms

1. **The settlement pays for the plan, but not for current law's own deficits.** Debt held by the public is 117.8% of GDP in FY2040 and 133.1% in FY2056, rising about a point a year, against current law's 132.7% and 180.2%.
2. **What's left is mostly interest.** In FY2040 the plan's deficit is 5.1% of GDP, and 4.6 points of that is interest on debt already run up. The primary deficit is 0.6%. The plan's Social Security package and HI's fold-in already more than close those funds' cash shortfalls, so keeping them out of scope costs no remaining deficit before FY2056. What it costs is levers.
3. **At CBO's rates, every goal costs about the same: 1.35-1.54% of GDP more deficit reduction from FY2036, about $730-830B in FY2040.** That is on top of the settlement, phased in from FY2032 with nothing in FY2029-31. Getting debt to fall from the mid-2030s turns out as dear as getting it under 100% by FY2050, because FY2036's hump (the plan's own FY2036-39 shortfall) binds the first goal.
4. **It turns on interest rates against growth.** If rates run half a point below growth, the goals cost a quarter to a half of that, and the booked path already stops rising after about FY2040. If rates run 1.5 points above growth, they cost about 2.5% of GDP. A rate shock of 100 to 200 basis points from FY2035 lifts the booked path's FY2056 debt to 157-186%.
5. **The money competes with the take-home test.** If the health contribution carried any of the goals alone, its rate would reach about 7.1-7.5% and about 38-40% of workers would come out ahead. Holding it at 3.80% (69.0%) means finding all of the $730-830B elsewhere. Reaching the 85% target (R about 2.57%) adds about $276B a year more in FY2040.
6. **The dynamic layer makes the goals harder, not easier.** Counted with the negatives in, the plan's own economic effects are a net cost: about −0.16% of GDP in FY2040, central, with a wide range (−0.87% to +0.18%), widest at the low end because of the top-rate stack. On the symmetric reading (A), which runs the same rate and output feedback on current law and the plan, FY2056 debt is about 147% rather than the conventional 133%. Current law's rises to about 209%, so the plan's lead over it widens, but its own level is worse. Only a sensitivity that credits the plan's whole distance below current law (reading B, likely overstated) shows a lower path, about 126%. Faster or slower productivity growth moves the path more than any policy channel: 0.3 points a year moves FY2056 debt by −24 or +29 points.
7. **Health "works as designed"** (spending a quarter point a year below D2's cap) would save about $77B in FY2040 and $780B in FY2056, measured below D2's path so D2 isn't counted twice. By the hard rule it counts toward no goal.

## Part 1. The debt gap and the frontier

The full tables are in [`notes/debt-gap-results.md`](notes/debt-gap-results.md) (`models/tools/fiscal_path.py`; `test_fiscal_path.py`).

### 1.1 Definitions

- **Debt** is federal debt held by the public at the end of the fiscal year: the budget model's unified reading, the settlement's reading of record (`2-settlement.md` part 6, item 9).
- **Trust funds** follow CBO's rule (`models/tools/budget/CONVENTIONS.md`; `ASM-TF-FULLPAY`): scheduled benefits are paid in full after a fund is exhausted, so exhaustion changes no outlay. A fund's surplus lowers debt held by the public. This matters here because the plan's Social Security package builds a reserve of about $4.1T by FY2040, which is lent to Treasury and lowers public debt.
- **Extra deficit reduction (X)** is a cut in the primary deficit beyond the booked plan, on the conventional score. Its interest saving is rolled at the model's marginal rate.
- **r − g** is the effective interest rate on the debt less nominal GDP growth, averaged over FY2036-56. The booked path's own is **+0.44** (CBO's February 2026 rates and growth), used as the central "+0.5". The other two readings shift every rate by about ±1 point from FY2030, reaching old debt as it rolls over, with growth on CBO's path.
- **The consolidation's shape:** nothing in FY2029-31 (`-18`), phased in over FY2032-36, then a constant share of GDP. Goal 1 is also priced year by year, at its literal minimum.

### 1.2 The booked path and what the remaining deficit is made of

| % of GDP | FY2035 | FY2040 | FY2045 | FY2050 | FY2056 |
| --- | --- | --- | --- | --- | --- |
| **Debt, the plan as booked** | 111.1 | 117.8 | 122.1 | 126.6 | 133.1 |
| Debt, current law | 120.5 | 132.7 | 145.8 | 160.5 | 180.2 |
| **The plan's deficit** | 4.77 | 5.12 | 5.18 | 5.27 | 5.63 |
| of which net interest | 4.25 | 4.56 | 4.81 | 5.01 | 5.29 |
| of which the primary deficit | 0.53 | 0.56 | 0.38 | 0.27 | 0.35 |
| Current law's deficit | 6.43 | 7.20 | 7.82 | 8.50 | 9.42 |
| of which net interest | 4.58 | 5.12 | 5.71 | 6.32 | 7.14 |
| of which Social Security's cash shortfall | 0.94 | 1.08 | 1.20 | 1.30 | 1.52 |
| of which Medicare HI's cash shortfall | 0.27 | 0.31 | 0.31 | 0.29 | 0.26 |
| of which everything else (general fund) | 0.64 | 0.69 | 0.60 | 0.58 | 0.51 |
| The plan's trust-fund effect (Social Security, HI, education, leave) | −1.43 | −1.51 | −1.69 | −1.73 | −1.73 |

**What the scope exclusion costs, honestly.** Interest is 89-94% of the plan's remaining deficit. Under current law, Social Security's and HI's cash shortfalls are 1.4-1.8% of GDP. The plan's decided Social Security package (SS-1 to SS-5 and the SS-7.01 fallback, D8) and HI's fold-in at the 2035 endpoint move the trust funds by −1.5 to −1.7 points, more than both shortfalls, through FY2056. So the out-of-scope funds aren't adding to what is left. The exclusion's cost is the levers it takes off the table, such as further benefit changes, the payroll cap beyond SS-1, or Medicare's eligibility age. Two notes:
- The plan's Social Security surplus is part of why its public debt is lower. That is the right reading of debt held by the public, but it is money the trust funds will draw back after the 2050s. On the budget model's CBO convention Social Security depletes in 2093.
- Medicare is folded into the single plan from 2035, so its cost growth is inside the plan's general fund under D2, which is booked.

### 1.3 Three readings of r − g, and the primary balance that holds debt flat

The primary balance that holds the debt ratio flat is about d × (r − g) / (1 + g).

| r − g | Debt FY2040 | Debt FY2056 | Primary balance that holds debt flat, FY2040 / FY2056 | The booked primary balance, FY2040 / FY2056 |
| --- | --- | --- | --- | --- |
| −0.5 | 109.7 | 107.5 | −0.66 / −0.41 | −0.56 / −0.35 |
| **+0.44 (booked)** | **117.8** | **133.1** | **+0.37 / +0.88** | −0.56 / −0.35 |
| +1.5 | 127.5 | 169.0 | +1.55 / +2.81 | −0.56 / −0.35 |

At r − g of −0.5 the booked plan already holds debt about flat from FY2040. At CBO's rates it is about 0.9 points of GDP short of that in FY2040, and 1.2 points short in FY2056.

### 1.4 The goals: extra deficit reduction needed, on the conventional score

Share of GDP from FY2036 (phased in over FY2032-36). X in $B. Interest saved is the cumulative total over FY2030-56.

| Goal | r − g | Share | X FY2035 | X FY2040 | X FY2050 | X FY2056 | Interest saved FY2030-56 | Debt FY2040 / FY2050 / FY2056 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **1. Falling from the mid-2030s** (no rise after FY2035) | −0.5 | 0.73% | 263 | 395 | 567 | 698 | $4.3T | 104.7 / 96.0 / 91.3 |
| | **+0.44** | **1.54%** | 553 | **833** | 1,194 | 1,471 | $13.0T | 106.8 / 99.0 / 94.9 |
| | +1.5 | 2.46% | 886 | 1,333 | 1,912 | 2,355 | $29.0T | 109.1 / 102.6 / 99.4 |
| **2. Under 100% by FY2050** | −0.5 | 0.49% | 175 | 263 | 378 | 465 | $2.9T | 106.4 / 100.0 / 96.7 |
| | **+0.44** | **1.48%** | 534 | **803** | 1,152 | 1,418 | $12.6T | 107.1 / 100.0 / 96.3 |
| | +1.5 | 2.59% | 933 | 1,404 | 2,014 | 2,480 | $30.5T | 108.1 / 100.0 / 95.6 |
| **3. Under 100% by FY2055** | −0.5 | 0.36% | 128 | 193 | 277 | 341 | $2.1T | 107.3 / 102.1 / 99.6 |
| | **+0.44** | **1.35%** | 486 | **732** | 1,050 | 1,293 | $11.5T | 108.1 / 102.4 / 99.6 |
| | +1.5 | 2.46% | 884 | 1,330 | 1,909 | 2,350 | $28.9T | 109.1 / 102.7 / 99.5 |

- **Goal 1 at its literal minimum** (each year just enough to hold the ratio flat; central): $720B in FY2036, $719B in FY2038, $452B in FY2040, $655B in FY2050, $947B in FY2056, holding debt at 111.1%. The FY2036-38 spike is the plan's own FY2036-39 general-fund shortfall ($190-280B a year). Step 8b's phasing could shrink it, and that is the cheapest way to make goal 1 cheaper than the speed goals.
- **Waiting costs.** Started over FY2036-40 instead of FY2032-36 (central), goal 2 needs 1.95% of GDP, not 1.48%, and goal 3 needs 1.66%, not 1.35%. Goal 1 can't wait that long.
- **The goals barely differ at CBO's rates.** Goal 1 on the smooth shape already reaches 99% by FY2050. The real choice is between a smooth path and a year-by-year one, and how much of FY2036-39's hump phasing can remove.

### 1.5 Stress: a rate shock of +100 to +200 basis points from FY2035

The reserve-currency tail: every rate higher from FY2035 on the central reading, reaching old debt as it rolls over (Treasury's maturity structure).

| Shock | Booked debt FY2040 / FY2050 / FY2056 | Interest FY2056, % of GDP | Share needed for goal 1 / 2 / 3 (central: 1.54 / 1.48 / 1.35) |
| --- | --- | --- | --- |
| +100 bp | 121.6 / 141.9 / 157.4 | 7.65 | 2.02 / 2.15 / 2.07 |
| +200 bp | 125.4 / 159.2 / 186.2 | 10.70 | 2.73 / 2.79 / 2.76 |

At the goals' central shares, a +100bp shock leaves FY2056 debt at 115-120%, and +200bp at 138-144%. A shock of this size undoes any goal unless the plan responds. That is the case for a trigger in the budget-process part (step 8c): deficit reduction that steps up automatically if the average rate on the debt runs a set margin above the plan's assumption.

### 1.6 The frontier: debt against the take-home test and the health contribution

Central reading, FY2040. A full point of the health contribution's base rate R raises about $224B in FY2040 and $429B in FY2056 (four quarter points of $56B, grown on HCU's path). Take-home is health's test at each R, everything counted, with no VAT (`budget_scan.take_home`).

| Goal | X FY2040 | If R carried all of it: R / workers ahead | Other money needed in FY2040 to hold R at 3.80% (69.0%) | at 3.25% (76.2%) | at the 85% target (R 2.57%) |
| --- | --- | --- | --- | --- | --- |
| 1. Falling from the mid-2030s | 833 | 7.52% / 38.0% | 833 | 956 | 1,109 |
| 2. Under 100% by FY2050 | 803 | 7.38% / 38.7% | 803 | 926 | 1,079 |
| 3. Under 100% by FY2055 | 732 | 7.07% / 40.4% | 732 | 855 | 1,008 |

The take-home curve: R 2.25%, 88.7%; 2.57%, 85%; 3.25%, 76.2%; 3.80%, 69.0%; 4.45%, about 61%; 5.5%, 50.9%; 6.5%, 44.0%. Beyond 6.5% it is extrapolated.

**Why the goals can't be recommended one at a time.** They draw on the same money:
- **The booked FY2056 surplus (about $205B)** is already in every figure above. If memo G8's option A gave it back as rate cuts, each goal's X rises by up to $205B in FY2056. Options C and D keep it.
- **The take-home goal (`DEC-2026-11-24-12`)** costs money that the debt goals also need. Each point of R below 3.80% is about $224B a year in FY2040 that has to come from elsewhere.
- **The populist start (`-18`)** pushes the money later. A later start makes the speed goals dearer (part 1.4).

So the batch has to price combinations: a goal, a take-home level and a G8 option, financed from the same list of sources (step 8b).

## Part 2. Methods and the dynamic layer

### 2.1 What the tools assume

| | What the budget model and long-term tools assume | Source | Assessment |
| --- | --- | --- | --- |
| **GDP growth** | Nominal 3.8% a year in FY2029-36, 3.7% in FY2036-46, 3.55% in FY2046-56. Real 1.8%, 1.7%, 1.5%. GDP prices 2.0% | CBO February 2026 (`ASM-GDP-PATH`; `models/data/cbo/`) | Standard. The plan's rows don't move GDP in any scored case (`ASM-DYN-CONVENTIONAL`). |
| **Labor force** | Potential labor force grows 0.43% a year in FY2029-36, 0.28% in FY2036-46, 0.10% in FY2046-56 | CBO's demographic and economic projections | Slowing labor-force growth is the main reason real growth falls. CBO's 2026 baseline carries lower net immigration after 2025. The plan's legalization and work programs would raise it, and that isn't counted. |
| **Productivity** | Potential labor productivity about 1.45% a year. Nonfarm TFP about 1.1-1.2% | CBO | No AI or investment upside or downside is in the baseline. The growth link (`ASM-GROWTH-LINK`) can stress it, and no scored case does. |
| **Demographics** | The trust-fund engine runs on the 2026 Trustees' demographics. The household model ages the 2025 CPS statically to 2029 (household model card, A-1) | Trustees; CBO; CPS | Fine for a ten-year window. For FY2056 the household figures (D3, take-home) are FY2040 readings. |
| **Interest rates** | Average rate on debt 3.75% (FY2030), 4.05% (FY2040), 4.15% (FY2056). New program borrowing at the higher of the average rate and a 40/60 bill/note blend through 2036 (about 3.9%), then the implied average (`ASM-RATE-MARGINAL`, `ASM-RATE-LT`) | CBO | **r − g about +0.44 over FY2036-56.** Rates don't respond to the plan's borrowing or saving (`ASM-RATE-NOFEEDBACK`). CBO's own long-term rates already carry CBO's feedback on its own baseline debt, so the baseline isn't feedback-free, but the plan's lower debt gets no credit. |
| **Rate stress** | +1 point from FY2030, phased in as debt rolls over (`ASM-RATE-SHIFT`, `-ROLLOVER`) | Treasury's maturity structure, end of FY2026 | Passes CBO's rule of thumb (SE-1). Reported beside the tests, never tested. |
| **Program rows** | Each row's ten-year ledger total spread on its profile and grown with GDP or CPI after FY2039. In a growth stress they stay in dollars | `fiscal-profiles.csv`; the ledger | A conventional score. Health grows at D2's GDP + 1 from 2037. |
| **The old dynamic table** | DEC-DYN: the DY1-DY9 midpoints summed (−$0.26T over FY2030-39, a net loss), one ramp, grown with GDP, kept in full after FY2039. The plan only, with no rate or crowding feedback | `ledger-dynamic.csv` | One-sided and coarse. DY1, its largest row, is "from memory". **DY4 is already zero** (#467, step 2A): the double count with LAB-1 that the board's item 4(c) names is fixed, so no tier-3 change is needed. |
| **The long-term model** | `fiscal-model.py` doesn't carry the settlement's lines. Its DEC scenario is a disclosed comparison. The budget model is the reading of record | `2-settlement.md` part 6, item 9 | Unchanged here. |

### 2.2 Where conventional scoring misses effects that would change the picture

Ranked by how much they could move FY2056 debt (`notes/dynamic-results.md`):

1. **The economy's own growth** (productivity ±0.3 points a year from FY2030: FY2056 debt 109% to 162%; labor force ±0.3: 118% to 150%). This is the largest by far. It isn't a policy effect, but the plan touches it at the margin through immigration, child care and investment. It is the strongest reason for the hard rule: a goal met only on hoped-for growth fails at CBO's growth.
2. **Rate and crowding-out feedback.** Debt this high pays for itself in higher rates and lower output under either path. On the symmetric reading A (from the FY2029 ratio), FY2056 debt is about 147% for the plan and 209% for current law. Conventional scoring gives neither path the feedback, and neither the plan's advantage nor its own cost. Reading B credits the plan with its whole 47-point distance below current law at the average coefficients (2 basis points per point, extrapolated in a straight line; CBO's average crowding out) and gets about 126%. That likely overstates the gain: deficit reduction financed by wealth and top-end taxes partly displaces saving, so it frees less private capital than the average.
3. **The negatives in the financing:** the 3.80% contribution's marginal rate on earnings (about −$54B in FY2040, central) and the top-rate stack and corporate rows (about −$65B central, and −$276B at the low end, which now includes JCT's 2017 recovery share). These outweigh every positive channel.
4. **Child care, pre-K and paid leave** (about +$43B in FY2040, central), **immigration** (+$16B) and **investment** (+$11B in FY2040, rising to about +$57B by FY2056).
5. **Health cost growth below D2's cap** (WAD-H1): not dynamic, but the largest "works as designed" item, and the one Espen named.

**Effects found too small to change the picture:** the health-coverage labor-supply convention (−$22B), job lock (+$11B; it partly overlaps the exclusion revenue already booked), work on-ramps (+$5B, a judgment with no derivation), the wealth tax beyond its allowance (−$11B), the child benefit's labor supply (−$11B, DY3) and the carbon fee's drag (−$11B, DY5).

### 2.3 The contained dynamic layer

**Pre-registered, then amended in the open.** The parameters, ranges and sources were written and committed before any debt path was run with them: [`notes/dynamic-preregistration.md`](notes/dynamic-preregistration.md) and `models/tools/fiscal_dynamic_params.json`, commit 87125a0. A test fails if the file changes. After an independent red-team (PR #483), three dated amendments, AM-1 to AM-3 (`fiscal_dynamic_amendments.json`), were applied on top:
- N-TOP's low end now includes JCT's 2017 anchor;
- N-CONTRIB's favorable end now sits at its own derivation's floor;
- DY3 and DY5 are added.
The registration's "Changes after registration" gives the reasons, and the results report the registered reading beside the amended one. **Not pre-registered, and disclosed:** the engine, the pairing of ends into cases, and the readings' roles. The first results came about 6.5 minutes after the registration. Results: [`notes/dynamic-results.md`](notes/dynamic-results.md) (`models/tools/fiscal_dynamic.py`).

**Three readings:**
- **C** is the plan's own channels alone, with no feedback.
- **A, the headline,** runs the rate and output feedback from the FY2029 debt ratio on current law and the plan alike.
- **B** runs the feedback from CBO's own baseline path, so only the plan's difference gets it. It is a sensitivity, and likely overstated (part 2.2).

The pessimistic case takes every channel at its low end and, on each reading, whichever feedback end gives the plan the higher FY2056 debt. For the goals, it takes whichever end makes each goal dearest by its own test years (the reviewer's note on #483).

**FY2056 debt, % of GDP** (conventional: plan 133.1, current law 180.2):

| Case | C, channels alone | **A, symmetric** | B, sensitivity | Current law on A |
| --- | --- | --- | --- | --- |
| Central | 137.5 | **147.3** | 125.9 | 208.5 |
| Pessimistic | 160.7 | **197.0** | 158.4 | 230.4 |
| Optimistic | 126.5 | **129.2** | 104.2 | 192.8 |

**The guardrails, and how each is met:**
- **Symmetry.** Reading A runs the same engine and coefficients on both paths. CBO's long-term projection already carries some feedback, so A overstates both levels. The plan's lead over current law widens (61 points, against 47 on the conventional score), but the plan's own level is worse.
- **Count the negatives.** All are in: the labor supply of the top-rate stack and of the 3.80% contribution, wealth-tax avoidance, fuller coverage's labor supply, the child benefit, the carbon fee, and crowding out in FY2036-39. That last one is in only on reading A; on B those years are charged only for their difference from current law's. The central net of the plan's own channels is **−0.16% of GDP in FY2040**, a cost.
- **Anchor the ranges.** The anchors:
  - CBO's working paper 2019-01: 2-3 basis points per point of debt;
  - CBO's 2016 federal investment study: a 5% return, a third offset;
  - CBO's 2014 ACA labor-supply estimate;
  - CBO's 2024 immigration estimate;
  - JCT's dynamic analysis of the 2017 law (JCX-69-17);
  - CBO's dynamic estimate of the 2025 law.

  The departures:
  - Child care, where CBO has published nothing dynamic.
  - The low end of rate sensitivity, for the dollar's reserve role.
  - **N-TOP's central (6% of top-end and corporate revenue, against JCT's roughly 25% for the 2017 cut).** JCT's anchor is now checked against the original (step 8c): growth offsets about $451B of the 2017 law's $1,456B conventional cost, and $385B net of higher interest, about 26% [EV-FIN-085]. So AM-1's low end stands, and the 6% central remains a named departure from it. CBO's 2025 estimate is still read through CRFB's summary.
- **Health.** D2 is booked, and the conventional base already banks its −$249B in FY2040 (without it the plan is $243B short). WAD-H1 is measured below the D2-held path, so it counts only spending below the cap and none of D2 twice. It fails if D2 fails. It is on its own line, never in the dynamic net.
- **The hard rule.** The conventional share is the requirement.

**Share of GDP from FY2036 each goal needs:**

| Goal | Conventional (the requirement) | Central: C / **A** / B | Pessimistic: C / **A** / B | Optimistic: C / **A** / B |
| --- | --- | --- | --- | --- |
| 1. Falling from the mid-2030s | **1.54%** | 1.88 / **1.91** / 1.74 | 2.83 / **2.93** / 2.78 | 1.45 / **1.46** / 1.21 |
| 2. Under 100% by FY2050 | **1.48%** | 1.67 / **1.67** / 1.23 | 2.58 / **2.66** / 2.38 | 1.22 / **1.20** / 0.52 |
| 3. Under 100% by FY2055 | **1.35%** | 1.52 / **1.52** / 0.95 | 2.38 / **2.47** / 2.12 | 1.09 / **1.07** / 0.20 |

Read across: on the channels alone and on the symmetric reading, every goal needs more than its conventional share. That is about 0.2-0.35 points of GDP in the central case, and over a point in the pessimistic one. Only reading B, the likely overstated sensitivity, needs less. So the dynamic layer gives no margin to count on. It is a risk to plan for: a goal met exactly on the conventional score has no cushion if the financing's labor-supply and investment costs come in near CBO's and JCT's anchors.

**How the layer may be used** (for step 8c's budget process):
- **As a risk margin, not a saving.** The central symmetric case shows how much a goal met exactly on the conventional score could fall short. Step 8b should weigh building that cushion into the goal's sources, or a trigger (next point) that adds deficit reduction if receipts come in below the conventional score.
- **Through a trigger,** never up front. Where a dynamic or "works as designed" saving shows up in measured results, a later rate may step down: for example the health contribution once the trustees certify spending below D2's path (memo G8's option D is that kind of trigger), or deficit reduction eased once the average rate on the debt runs below the plan's assumption.

**The independent red-team** (the lead session, on head 2dc35b0) found three blocking defects:
- the pessimistic pairing wasn't the worst case;
- the headline and its "margin" rested on reading B alone;
- N-TOP's range excluded its own anchor.

All three are fixed here, along with its other notes (AM-1 to AM-3; stronger tests of the symmetry and of the rate recursion). What remains open for step 8b:
- verify N-TOP's central against the primary sources;
- the 0.25 budget response;
- N-CONTRIB's elasticity;
- whether P-CARE and P-INVEST overlap the investment the crowding channel credits.

The standing reviewer reviews this head before any dynamic figure reaches Espen as more than a sensitivity.

## Part 3. The frontier: debt goal, take-home share and the health contribution

Full tables: [`notes/frontier-results.md`](notes/frontier-results.md) (`models/tools/fiscal_frontier.py`). Central r − g, conventional score. **Other money** is what must come from sources other than the health contribution's base rate R: phasing, cuts and other revenue. Every package in part 6 sits on this table.

| Debt goal | Take-home 69.0% (R 3.80%) | 76.2% (R 3.25%) | 80% (R 2.95%) | 85% (R 2.57%) |
| --- | --- | --- | --- | --- |
| No new goal (the booked path, 133% in FY2056) | 0 | 123 | 190 | 276 |
| **Debt held flat from FY2040** (about 117%; year by year) | 461 | 584 | 651 | 737 |
| Under 100% by FY2055 (from FY2036) | 732 | 855 | 922 | 1,007 |
| Under 100% by FY2050 (from FY2036) | 803 | 926 | 993 | 1,078 |
| Falling from the mid-2030s (from FY2036) | 833 | 956 | 1,023 | 1,108 |

Other money needed in FY2040, $B. By FY2056 each figure is about 1.8 times as large. The "held flat from FY2040" row is new in 8b: debt held at its FY2039 level of 116.9% of GDP. It costs 0.85% of GDP in FY2040 and 1.03% in FY2056, nothing at r − g −0.5, and 2.1-2.4% at +1.5.

**How to read it:**
- Raising take-home by one step costs about $60-70B a year in FY2040, whatever the goal.
- **R can't carry a goal by itself.** It would take R to about 5.9% for "held flat" (about 48% of workers ahead) and about 7.1-7.5% for the 100% goals (38-40%).
- **G8 interacts with every goal** (part 5).

## Part 4. The plan's own programs: what to phase, delay, trigger or right-size

Inventory: [`notes/program-inventory.md`](notes/program-inventory.md) (`models/tools/program_inventory.py`; a Standard-tier subagent's work, checked here).

**The FY2036-39 shortfall** ($277B, $272B, $259B and $193B; about $1.0T in all) is health's 2035 endpoint:
- Health's net cost steps up about $280B into FY2036, before D2's cap (from FY2037) and the defense saving bite.
- The long-term care benefit (HLT-9), net of the states' payment, rises from $104B in FY2035 to $283B in FY2039.
- Housing's stage 2, the clean-energy credits (CLI-1) and IMM-1 also grow fast.
- No flagship's dossier claims a federal saving later. Housing, the secure floor, work, immigration and child care each say their savings are "not counted". So **no line is protected for saving money later on the record.** The ones the evidence says will (child care, pre-K, the child benefit; dynamic layer P-CARE) are protected here anyway, because they are the plan's early delivery.

**The candidates run FY2035-39, one year wider than the shortfall:** PH-1 starts in FY2035, the endpoint's first year, and saves $62B that year (`notes/frontier-results.md` part 4).

| ID | Candidate | Saved FY2035-39 ($B) | Who waits, and the outcome it delays |
| --- | --- | --- | --- |
| PH-1 | Long-term care reaches full benefit in FY2039 instead of on its own ramp (40/55/70/85% of its FY2035-38 path) | 262 | Older and disabled people who need care. In FY2035 about 60% of the benefit's cost is deferred, about 45% in FY2036, falling to 15% in FY2038. It delays the care outcomes in health's and care's dossiers (OUT-03, OUT-08), and families keep paying privately or spend down to Medicaid for one to four years longer |
| PH-2 | Housing's stage 2 held at its FY2036 level until FY2040, net of its booked cap (S11) | 10 | Because G14 C's cap already slows stage 2, this saves little. Up to about 200,000 families wait one to three years for an award (on the cap's own count of about 810,000 families leased in FY2040). Delays the housing outcome (OUT-04) |
| PH-3 | Clean-energy credits held at their FY2037 level in FY2038-39 | 47 | Slower deployment in two years. The climate outcome (OUT-05) slips slightly |
| — | All three | 319 | |

**What the candidates buy:**
- On goal 1 ("falling from the mid-2030s"), all three cut the share needed from 1.54% to 1.35% of GDP.
- On the 100% goals they save 0.03-0.04 points, since those goals test later years.
- On "held flat from FY2040" they lower the debt carried into FY2040 by about $355B with interest, about 0.65 points of GDP.

**Not proposed:**
- **Delaying the 2035 health endpoint.** It is the plan's central promise, and delaying it costs the transition financing that runs with it.
- **Phasing the child benefit, child care or pre-K.** These are the populist start's delivery (`-18`).
- **Triggers that switch a benefit on only after a fiscal finding.** Per the lead's brief, they delay the delivery that earns trust. Triggers go on later revenue instead (part 6).

**Borrowing up front against back-loaded revenue.** The booked plan already does this. FY2030-34 run a general-fund surplus (−$589B, health's early surplus), and FY2036-39 run the deficit. Front-loading benefits and borrowing in FY2029-35 is cheaper the lower r − g is. At CBO's rates, a dollar borrowed in FY2032 and repaid in FY2040 costs about 37 cents of interest; at r − g −0.5, with rates about a point lower, about 27 cents.

## Part 5. Revenue, outside proposals, G8 and "works as designed"

### 5.1 What revenue is left (no VAT; no middle-class increases early)

The top end is nearly used:
- the wage stack is at 68-73% on top wages (`../notes/stack-2026-11-16.md`);
- the wealth tax is capped against the income taxes (G4 C1);
- corporate rows: the rate is at 28%, foreign income at the full rate, and the buyback tax and corporate minimum are booked.

What is left is **broad revenue, and it can only come later**, after the plan has delivered. The screen of outside proposals sizes it ([`notes/outside-proposals.md`](notes/outside-proposals.md), CBO's December 2024 options scaled to FY2040, to be re-scored after the 2025 law). Each of these reaches the middle class, so each is later only:

| Source | FY2040 ($B) | When |
| --- | --- | --- |
| Limits on itemized deductions beyond C39 | 123-312 | FY2037 on |
| A greenhouse-gas tax beyond the booked carbon fee | 111-147 | FY2037 on |
| An AGI surtax | 167-225 | FY2040 on |
| Ordinary rate increases | 85-179 | FY2040 on |
| The health contribution itself | about 224 a point | Any time, at a take-home cost |

A new payroll tax (194-384) is broad too. It is set aside while Social Security's finances are out of scope.

### 5.2 Outside proposals

The table has 55 rows: 34 from CBO, 7 from CRFB, 7 from Peterson's 2024 Solutions Initiative, 5 from the Progressive Caucus, and Simpson-Bowles and Domenici-Rivlin.

**Almost nothing outside fits that isn't already booked:**
- **About $28B in FY2040** (CRFB's SALT-workaround fix, to confirm against C39).
- **Already in the plan:**
  - CBO's pass-through investment-income tax is H1a;
  - the financial transactions tax is G10 and HS1;
  - the foreign income, corporate and estate options match booked rows;
  - CBO's Medicaid options overlap the single plan.
- **Set aside:**
  - **Conflict with a booked program:** CBO's international affairs cut (DEV-P).
  - **Fail the screen:** every Social Security and Medicare option fails the scope rule, and every Peterson plan fails it as a package.
  - **VAT:** CBO's VAT and Domenici-Rivlin's sales tax.
  - **Too large for the populist start:** Simpson-Bowles's scale and mix: about $4T over ten years, a quarter of it revenue from broadening the base and lowering rates.

### 5.3 G8 against the goals

**On any debt goal, memo G8's recommended D fails as written.** Its trigger, a general-fund surplus above 0.1% of GDP for two years, would fire on the goal's own deficit reduction and give it back as rate cuts. The finding has to be measured against the goal's path. Memo G18 re-asks G8 with that change (D′).

On the booked path with no goal:
- A leaves FY2056 debt at 134.6%;
- B leaves it at 134.4%;
- C and D leave it at 133.1%.

On a goal, A's step-downs cost $51B more other money in FY2050 and $172B more in FY2056.

### 5.4 "Works as designed" savings (`DEC-2026-11-24-14`, direction 1)

These are labeled, with a range, and never in a goal test.
- **WAD-H1: health spending growing a quarter point a year below D2's cap.** About $77B in FY2040 and $777B in FY2056, range 0 to twice that. It is measured below the D2-held path, so D2 is not counted twice, and it is void if D2 fails (part 2.3; [`notes/dynamic-results.md`](notes/dynamic-results.md)).
- **Its proper use is a trigger.** When the trustees certify spending below D2's path, the health contribution may step down (G16, G18). That gives it back to households only once it is real.
- No other "works as designed" saving is claimed: no flagship's dossier claims one (part 4).

## Part 6. The decision batch (decided November 25, 2026)

Memos G15 to G19 are in [`memos/`](memos/README.md). Espen decided each on its own on November 25 (`DEC-2026-11-25-01` to `-05`); none is booked. G15 B is to be made "a little more aggressive on debt", and G19 B is to be re-checked with a VAT allowed after the first years; both come back in batch 4 (memos G23 and G24). The set as recommended and chosen, shown on the frontier:
- **G15 B: hold debt flat from FY2040** at about 117% of GDP, met on the conventional score. Then step toward 100% by a debt-path rule as results allow (the rule is 8c's).
- **G16 B: hold R at 3.80% to FY2040,** then lower it by trigger toward 3.25% (76.2% take-home) as certified savings appear.
- **G17 B: hold the clean-energy credits at their FY2037 level in FY2038-39 (PH-3, about $47B; step 8b's first count of $52B also picked up four other climate lines, corrected in step 9)**, with long-term care's phasing (PH-1, $262B) named as the fallback. Housing's stage 2 (PH-2) saves only $10B on top of G14 C's cap, so it is left alone.
- **G18 D′:** G8's step-down measured against the debt goal.
- **G19 B: from FY2037, limits on itemized deductions and a larger carbon fee first,** an AGI surtax from FY2040 if needed, and R last.

**The recommended set's money in FY2040** ("held flat", R 3.80%): $461B of other money.
- Already found:
  - phasing, about $27B in FY2039 falling to zero by FY2040, plus the debt it avoids;
  - the outside fix, about $28B.
- Still to find: about $430B a year from FY2040, from G19's broad sources. That is about 0.8% of GDP of new revenue landing on the middle class from the late 2030s, the cost of a debt goal without a VAT or Social Security and Medicare changes.
- At r − g −0.5 none of it is needed. At +1.5 about twice as much is.

## Method and sources

- **The debt goals:** `models/tools/fiscal_path.py` on `models/tools/recovery-budget/model.py` case `mixed` (the settlement booked). Rate readings use `fiscal-model.py`'s `rate_shift_interest` and `read_rollover`. The take-home curve is `financing-protection/budget_scan.take_home`. The R yield is `packages.HCU_PER_QUARTER_POINT_2040` on HCU's path. The decomposition uses the funds engine's current-law Social Security and HI cash flows.
- **The dynamic layer:** `models/tools/fiscal_dynamic.py`, `fiscal_dynamic_params.json` (as registered) and `fiscal_dynamic_amendments.json` (AM-1 to AM-3). The growth sensitivity is `fiscal-model.py`'s `growth_path` (CBO publication 62257).
- **The frontier and phasing:** `models/tools/fiscal_frontier.py`; the inventory `models/tools/program_inventory.py`; the outside screen `notes/outside-proposals.md` (a subagent's table, checked here).
- **Tests:** `models/tools/test_fiscal_path.py` (run-all.sh step 8c2): the booked path reproduced, the r − g targets, each goal solved minimally, the debt identity, symmetry, the registration hash, DY4 at zero, and both notes current.
- **Sources for the anchors** (the registration has each one's use): CBO working paper 2019-01 (publication 55018); Dallas Fed working paper 2513 (2025); CBO publication 51628 (June 2016); CBO, *The Budget and Economic Outlook: 2014 to 2024*, appendix C; CBO publication 60165 (July 2024); JCT JCX-69-17 (December 22, 2017); CBO working paper 61257 (February 2026) and CRFB's summary of CBO's dynamic estimate of P.L. 119-21; CBO working paper 2012-12; SRC-1165 (CBO's April 2025 letter on dynamic analysis). These aren't yet in the evidence register. Step 8b adds them (EV-FIN) when it cites them in the batch.
