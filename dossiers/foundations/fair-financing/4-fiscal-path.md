# Stage G step 8: the fiscal path review

Role: the harder look at spending and debt that Espen started at the stage G boundary review (`DEC-2026-11-24-14`). It prices the three debt goals (`DEC-2026-11-24-15`), checks the budget model's and the long-term tools' methods, and adds a contained dynamic layer beside the conventional score. Later parts cover phasing, revenue, outside proposals, G8 and the decision batch (step 8b), and the strategy memo, budget process and the central rules (step 8c). Status: **parts 1 and 2 drafted, stage G step 8a, November 24, 2026**; parts 3 on are for 8b and 8c. Nothing here is booked. The settlement as booked (#480, [`2-settlement.md`](2-settlement.md)) stays the plan's fiscal base (`DEC-2026-11-24-10`). This part recommends no goal: the goals draw on the same money, so step 8b recommends one, with the frontier below, in the decision batch.

Units: federal fiscal years, nominal $B or % of GDP. Project arithmetic on exploratory models, not official scores.

**The rules this review keeps** (Espen's directions, `DEC-2026-11-24-14` to `-18`; step 8a's brief):
- **Start populist in 2029** (`-18`): minimal new revenue from the middle class in the first years. No VAT (`DEC-2026-11-20-07`).
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

The pessimistic case takes every channel at its low end and, on each reading, whichever feedback end gives the plan the higher FY2056 debt.

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
  - **N-TOP's central (6% of top-end and corporate revenue, against JCT's roughly 25% for the 2017 cut).** That departure is **not yet verified** against the primary sources. Step 8b reads JCX-69-17's table, and CBO's 2025 estimate directly rather than through CRFB's summary.
- **Health.** D2 is booked, and the conventional base already banks its −$249B in FY2040 (without it the plan is $243B short). WAD-H1 is measured below the D2-held path, so it counts only spending below the cap and none of D2 twice. It fails if D2 fails. It is on its own line, never in the dynamic net.
- **The hard rule.** The conventional share is the requirement.

**Share of GDP from FY2036 each goal needs:**

| Goal | Conventional (the requirement) | Central: C / **A** / B | Pessimistic: C / **A** / B | Optimistic: C / **A** / B |
| --- | --- | --- | --- | --- |
| 1. Falling from the mid-2030s | **1.54%** | 1.88 / **1.91** / 1.74 | 2.83 / **2.86** / 2.78 | 1.45 / **1.46** / 1.21 |
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

## Method and sources

- **The debt goals:** `models/tools/fiscal_path.py` on `models/tools/recovery-budget/model.py` case `mixed` (the settlement booked). Rate readings use `fiscal-model.py`'s `rate_shift_interest` and `read_rollover`. The take-home curve is `financing-protection/budget_scan.take_home`. The R yield is `packages.HCU_PER_QUARTER_POINT_2040` on HCU's path. The decomposition uses the funds engine's current-law Social Security and HI cash flows.
- **The dynamic layer:** `models/tools/fiscal_dynamic.py`, `fiscal_dynamic_params.json` (as registered) and `fiscal_dynamic_amendments.json` (AM-1 to AM-3). The growth sensitivity is `fiscal-model.py`'s `growth_path` (CBO publication 62257).
- **Tests:** `models/tools/test_fiscal_path.py` (run-all.sh step 8c2): the booked path reproduced, the r − g targets, each goal solved minimally, the debt identity, symmetry, the registration hash, DY4 at zero, and both notes current.
- **Sources for the anchors** (the registration has each one's use): CBO working paper 2019-01 (publication 55018); Dallas Fed working paper 2513 (2025); CBO publication 51628 (June 2016); CBO, *The Budget and Economic Outlook: 2014 to 2024*, appendix C; CBO publication 60165 (July 2024); JCT JCX-69-17 (December 22, 2017); CBO working paper 61257 (February 2026) and CRFB's summary of CBO's dynamic estimate of P.L. 119-21; CBO working paper 2012-12; SRC-1165 (CBO's April 2025 letter on dynamic analysis). These aren't yet in the evidence register. Step 8b adds them (EV-FIN) when it cites them in the batch.
