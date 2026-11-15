# The single health plan: an independent cost review, and financing that passes the take-home test

Role: the stage E memo that tries to break `health-financing.md`'s cost estimate. It then redesigns the plan's financing around Espen's take-home test of November 15. It replaces that memo's gross cost (part 1.1, and with it part 1.2b's correction, now made here) and the package choice (parts 3 and 9, questions 1 and 2); those parts are marked superseded there. Everything else in `health-financing.md` stands: the payer accounting, the employer protections, the worker transition credit, the states' maintenance of effort and the Medicare seam.

Status: **for Espen's decision, November 15, 2026.** It recommends and books nothing. The coverage model, the booked rows and the adopted inputs are unchanged. Any correction goes to a later tier-3 booking PR (part 5). The household contribution Espen chose on November 15 (one unified contribution in place of package E's tier) is rebuilt and priced across rates in `health-household-contribution.md`.

Units:
- **Households: 2026 dollars.** These are FY2040's amounts with price growth taken out.
- **Budget totals: FY2040, nominal $B,** case `mixed`.
- **One income measure: AGI.**
- **"Today" means today's law grown to FY2040.** Premiums and medical bills grow about 4.8% a year per person, about 1.40 times today's in real terms by FY2040. So today and the plan are compared like with like, in the same year.
- Every figure is project arithmetic on the project's own models, not an official score. Code: `models/tools/health_cost_review.py`. Test: `models/tools/test_health_cost_review.py`.

## Reference card (FY2040)

| | `health-financing.md` (package A) | This review |
| --- | --- | --- |
| Gross cost of the single system | $8,407B | **$7,795B** with the errors fixed; **$7,345B** with three design changes (D1, D2, D5) |
| National health spending against today's law | −$0.80T (−6%) | **About −$1.0T (−8%)** with the errors fixed |
| Household contribution | 10.6% of taxable income | **Recommended package E: none on the first $100,000 of AGI ($200,000 for a couple), 4% above it** |
| Single worker at $72,000: visible health cost a year | $7,394 (today: $5,679) | **$1,371**, about $4,300 less than today |
| Workers whose visible health costs fall | about a third (36%, on the corrected cost) | **9 in 10** (all workers below $100,000) |
| Bottom-four households losing cash (losing more than 5% of income) | 26.9 million (6.2 million) | **1.6 million (0.1 million)** |
| Employers as a whole | pay what they would have spent | pay about 10% less: the small-employer allowance exempts each firm's first $100,000 of pay in the band |
| What it takes from the rest of the plan | nothing | **$579B a year of booked revenue**, so the plan-wide FY2040 gap rises from $70B to **$649B** for stage G to settle |

**Three ways to read the recommended contribution** (single, AGI $150,000):
- **The rate:** 4% of AGI above $102,700, the $100,000 line of 2025 indexed to 2026.
- **The dollars:** 4% × ($150,000 − $102,700) = **$1,892**.
- **The share of AGI:** **1.3%**.

At $72,000 it is $0; at $500,000 it is $15,892 (3.2%).

**Glossary:**
- **Visible cost:** money a household sees leave its paycheck or wallet for health care. Today that is its premium share and its out-of-pocket costs. Under the plan it is the household contribution, copays, and the tax on the pay that used to go to premiums before tax. Employers' spending, and any future raise, are not counted (Espen, November 15). The worker's 1.45% Medicare payroll tax is the same in both worlds, so it is left out of both.
- **Take-home test:** whether a household's visible cost falls under the plan.
- **Gross cost:** everything the plan pays out: claims, administration and the items it adds.
- **National health spending:** all health spending by everyone, inside the plan and outside it.
- **Seam:** a gap between two of the model's data sources, here CMS's and CBO's projections. It belongs to no payer.
- **Band:** each worker's pay between the $20,000 low-pay line and the Social Security wage base, the employer contribution's base.
- **Small-employer allowance:** the first $100,000 of each employer's pay in the band is free of the employer contribution. There is no cliff, because every employer gets it.
- **Booked revenue:** taxes the plan already counts, now spent on its other flagships.
- **Fifths:** households ranked by size-adjusted income, Q1 poorest to Q5 richest, with the top 1% shown on its own.

## In plain terms

1. **You were right: the cost was too high, through errors.** Checked line by line, and separately by a second agent, the model overstates the plan's cost. The four biggest errors:
   - **The newly covered were priced like the average American, Medicare enrollees included.** The uninsured are almost all under 65, so each cost about twice what they should: about $12,700 a person in 2032 against about $6,700. Fixing it: **−$310B**.
   - **Medicaid's hospitals were priced at its doctors' discount** (72% of Medicare's rates). With its supplemental payments, Medicaid pays hospitals about what Medicare does. So raising Medicaid to the plan's rates costs much less: **−$352B**.
   - **Doctors were priced at the hospitals' rate** (1.15, not about 1.05): **−$275B** (#386 found this one).
   - **Medicaid's spending came from a projection made before the 2025 law** (the "Medicaid seam"): **−$137B**. It also overstated what the states spend now, by about $223B.
2. **Some errors ran the other way, and they are fixed too.**
   - The model averaged employers' prices wrongly, so it overstated what single payer saves on employer plans: **+$235B**. A further **+$238B** is not an error fix: it is this review's own judgment (a working assumption) that private prices for services other than hospitals and doctors are only 10-20% above Medicare's, and it is labeled as such (part 1.2, step 4b).
   - It also left out CHIP's care (**+$81B**), and it moved nursing-home and over-the-counter spending into the plan, which covers neither.
   - The honest net: the system costs **$7.8 trillion in FY2040, not $8.4 trillion**. The country spends **about $1.0 trillion (8%) less** than under today's law, not 6% less.
3. **Three design changes take it to $7.3 trillion:** administration at 4% (D1), a national health budget from 2037 (D2), and drug prices 25% below today's rather than 15% (D5). Peer countries pay about a third of US drug prices.
4. **Even so, a broad household contribution can't pass your take-home test.** Package A on the corrected cost needs 7.9% of taxable income. The single worker at $72,000 would still see about $5,800 a year leave their pay and wallet, against about $5,700 today. Only about a third of workers come out ahead in what they see.
5. **So the recommended package (E) charges typical workers nothing new:**
   - **Households pay no contribution below $100,000 of AGI ($200,000 for a couple), and 4% above it.**
   - **Employers pay what they would have spent, less a small-employer allowance:** the first $100,000 of each firm's pay in the band is free. Most firms under 20 workers pay little or nothing.
   - **About $385B a year of new general revenue, priced one by one** (part 2.2): a wealth tax on fortunes above $50 million, a financial transactions tax of 0.1%, capital gains taxed like pay above $1 million of income, two corporate measures, and the investment-income tax on pass-through business income.
   - **About $579B a year of revenue the plan already counts for its other flagships.** You said health comes first. It leaves those flagships about $649B short in FY2040, for the stage G settlement.
   - **Everything else as before:** the federal money already spent on health, the states' payment, the 2.9% payroll tax (unchanged for workers), the worker transition credit and the employer protections.
6. **What that means for people** (FY2040, 2026 dollars):
   - **The single worker at $72,000:** visible health costs fall from about $5,700 to about **$1,400** (copays, and tax on the pay that used to go to the premium). That is **$4,300 a year less, every year**, without counting any raise.
   - **9 in 10 workers see their costs fall,** including every worker below $100,000 of AGI. The ones who don't are mostly single people above about $190,000, and well-paid workers who are uninsured or on Medicare today.
   - **Bottom-four households losing cash fall from 26.9 million to 1.6 million.** The middle fifth gains about **$12,900** a household a year.
7. **The catch: who pays.** The top 1% pays about $212,000 more a household a year (2026 dollars), and the rest of the plan loses $579B a year of revenue. That is the trade you named: health first, and the other flagships cut back or refinanced in stage G.
8. **Durability:**
   - **For:** typical workers see no new charge, and the national budget holds growth.
   - **Against:** about $1 trillion a year rests on top-end and corporate taxes that are less certain than broad contributions. The wealth tax ($150B) carries real legal risk; if a court struck it down, the line rate would need about 2 more points, or more booked revenue would have to be used.
9. **Your questions are in part 4,** each with a recommendation.

## Part 1. The cost review

### 1.1 How it was checked

- **The code path:**
  - `health_path.groups()` prices each coverage group in 2032 at full scale.
  - The coverage model's `run_single_payer()` uses the same formulas.
  - `health_financing.system_view()` scales them to FY2040 (×1.533) and adds the booked items.
- **The rebuild.** The review rebuilt that calculation by service and by payer from CMS's 2024 spending table (National Health Expenditure Table 19, `library/text/cms-2024-nhe-table19-expenditure-by-program.txt`): hospitals, physicians, other professionals, dental, home health, nursing homes, drugs, equipment, over-the-counter products and administration, for Medicare, Medicaid, CHIP, private insurance and out of pocket.
- **It reproduces the model to the cent** when the model's simplifications are switched on (`check_reproduces()`). Each simplification was then switched off in turn.
- **An independent agent re-derived the cost by its own route** (part 1.5).

### 1.2 The bridge from $8,407B to $7,795B

Effects are in $B. The 2032 column is at full scale; FY2040 is ×1.533. Each step builds on the one before.

| Step | 2032 | FY2040 gross cost | FY2040 national spending | Real error? |
| --- | --- | --- | --- | --- |
| **0. The memo's model** (Medicare rebased to CBO) | 5,575 | 8,407 | 11,651 | — |
| **1. Physicians at the decided fee-schedule rate.** The plan pays them Medicare's fees plus add-ons, about 1.05, but the code used the hospital target, 1.15 (#386, part 1.2b) | −180 | **−275** | −275 | Yes |
| **2. The newly covered priced off people under 65.** The code took 80% of the average repriced claim of everyone now covered, Medicare's enrollees included: $12,700 a person in 2032. Off private enrollees' repriced claims, at the uninsured's ages (about 14% children), it is $6,700 | −202 | **−310** | −310 | Yes |
| **3. Each payer's own mix of services** (one national hospital share and drug share had been used for every payer) | −37 | −56 | −56 | A simplification |
| **4a. Private hospital and physician prices averaged by volume.** The code set private prices at 2.08 times Medicare, a spending-weighted average of the hospital ratio (2.54) and the physician ratio (1.4). To reprice, the plan's rates must be divided by each service's own price ratio and the results added, which is the same as a harmonic average. Other private services stay at the model's 2.08 | +153 | **+235** | +235 | Yes, in the other direction (the independent agent: +$251B) |
| **4b. Private prices for other services at 1.1-1.2 times Medicare, and dental on the plan's own schedule** (90% of private dental prices). These are **working assumptions, not error fixes**. No source gives these ratios; commercial premiums over Medicare are smaller outside hospitals and specialists (CBO 2022: primary care 1.17). Range: 0 at the model's blend; +$160B with other services at 1.4, like physicians; +$238B central | +155 | +238 | +238 | **A judgment** (cautious: it raises the cost) |
| **5. Each payer's own administrative share** (Table 19: Medicare 6.5%, Medicaid 9.2%, private 10.7%, against 6%, 6% and 12%) | −32 | −50 | −50 | Data |
| **6. Out of pocket.** Nursing homes ($48.7B in 2024) and over-the-counter products ($123.2B) stay outside the plan, which covers neither (HLT-7.05, HLT-7.07). Medicare enrollees' cost sharing is priced at Medicare's prices, not commercial ones | +9 | +13 | **+360** | Yes. Households keep paying about $346B outside the plan |
| **7. Medicaid's hospital payments at their measured level** (1.00 times Medicare, against the 0.72 physician fee index) | −230 | **−352** | −352 | Yes |
| **8. CHIP's care added.** The code replaced CHIP's federal money but never paid for its 3.5 million children's care: CMS lists CHIP outside "Medicaid" | +53 | +81 | +11 | Yes (an omission) |
| **9. Medicaid and CHIP rebased to CBO's February 2026 baseline** (the Medicaid seam) | −89 | **−137** | +15 | Yes. Federal money committed rises by $153B, and the states' current spending falls by $223B |
| **Total** | **−399** | **−612 → $7,795B** | **−184** | Errors and data corrections: −$850B; the judgment in 4b: +$238B |

What each change does:
- **To the household rate under package A:** about −2.75 points, from 10.61% to **7.86%**. This counts the states' lower payment.
- **To national spending:** under the plan it is about $1.0T (8%) below today's law in FY2040, against the memo's $0.8T (6%).
- **To households directly:** step 6 means about $346B of out-of-pocket spending stays with households, so their gains are a little smaller.

**Evidence for the new steps** (sources not yet in the register are named in plain text, with their addresses):
- **Step 2:** CMS's per-person spending, $22,356 at 65 and over against $9,154 at working age [EV-CAR-057]. CBO counts 37.2 million uninsured in 2032, almost all under 65 [EV-CAR-051].
- **Step 4:** CBO's review of commercial prices: hospitals more than twice Medicare's, physicians 1.29 times (CBO, 2022, cbo.gov/publication/57778). RAND, hospitals 2.54 times [EV-CAR-131]. The model's 1.4 for physicians is kept as central; at CBO's 1.29 the cost is $96B higher.
- **Step 7:**
  - The 0.72 is a physician fee index (Zuckerman, Skopec and Aarons, Health Affairs 2021).
  - With supplemental payments, Medicaid pays about 88 cents per dollar of hospital cost and Medicare 82-84 cents, a ratio of about 1.05 (American Hospital Association fact sheets, 2020 and 2023).
  - Supplemental and directed payments are about 40% of Medicaid's hospital payments (MACPAC, 2024, "Medicaid Base and Supplemental Payments to Hospitals").
  - The AHA has a stake: it argues both programs underpay. The ratio of its two figures is still the best available comparison.
  - Range 0.90-1.07; at 0.85 the cost is $153B higher.
- **Step 9:**
  - CBO's February 2026 baseline: federal Medicaid outlays of $834.0B in FY2032 (`library/text/cbo-51118-2026-02-budget-projections-workbook.txt`, row 10); CHIP's federal subsidy $15B (SRC-3000, Table A-1).
  - The total is taken at Table 19's 2024 federal share (596.7 of 931.7).
  - As with Medicare, the model's population is CBO's, after the 2025 law, while its spending grew on CMS's path.

### 1.3 Every driver against the evidence (FY2040, corrected base)

Each row gives the FY2040 effect on gross cost, then the household rate under package A (about $195B a point).

| Driver | What the plan assumes | What the evidence supports | Effect of the alternative | Risk to quality and access | Grade |
| --- | --- | --- | --- | --- | --- |
| **Hospital rates** | 1.15 times Medicare after a glide to 2036 (memo 5 B) | Urban's single-payer variants: 115% [SRC-3223]; Warren: 110% [EV-CAR-744]. CBO's lower-rate case was 13% lower and cut supply 2% [EV-CAR-220]. Commercial prices are 2.0-2.5 times Medicare's (CBO 2022; RAND [EV-CAR-131]) | 1.10: **−$126B** (−0.6 pt); 1.20: +$126B | Rural and safety-net hospitals, which have thin margins; the glide protects them | Reasonable; keep (D3) |
| **Physicians** | 1.15 in the code; about 1.05 in the design | Medicare's fee schedule plus primary-care and rural add-ons; commercial prices 1.29 times (CBO 2022) | Fixed: **−$275B**. At 1.00, −$172B more; at 1.10, +$172B | Low at 1.05: primary care gains, specialists lose about a quarter of commercial prices | **Error, fixed** |
| **Administration** | 5% of gross cost | Traditional Medicare 1.4% [EV-CAR-217]; Urban 6%, judging 3% insufficient [SRC-3223, EV-CAR-742]. US insurers' and providers' administration was 34% of spending, against 17% in Canada [EV-CAR-132] | 4%: **−$85B**; 3%: −$168B | Payment integrity and member service need protecting below 4% | Slightly high; book 4% (D1) |
| **Provider-side administration** | Not counted: rates are set, so lower billing costs show up only through rates | Billing and insurance costs are a large share of provider revenue [EV-CAR-132]; Galvani and PERI count the saving [EV-CAR-230, EV-CAR-231] | Not booked. It is the reason hospitals can accept 1.15, and the case for revisiting it in 2036 | — | Reasonable as a margin, not a booked saving |
| **Drugs** | 15% below today's prices | US prices 2.78 times 33 OECD countries'; brands 3.08 times after rebates; generics 0.67 times (RAND for ASPE, 2024, rand.org/pubs/research_reports/RRA788-3). CBO's lower-rate case: 23% [EV-CAR-220]. Warren: brands −70%, generics −30% [EV-CAR-744] | 25%: **−$115B**; 35%: −$231B | Launch delays for some new drugs; a 25% cut still leaves US prices about twice peers' | **Too cautious; book 25% (D5)** |
| **Copays and induced use** | Small capped copays above 200% of poverty; 1.5% more use by the already insured (`sp_util_uplift` 6% × 0.5 for low cost sharing × 0.5 unmet) | RAND: 9.8% more demand with no supply limit, counting the newly insured and long-term care [EV-CAR-228]; CBO: demand outruns supply [EV-CAR-219] | No added use: −$117B; double: +$117B; no copays: +$233B | Waits if demand outruns supply | Reasonable, perhaps low |
| **Medicaid rising to the plan's rates** | All Medicaid claims at 0.72 of Medicare | Hospitals at about 1.00 with supplemental payments (part 1.2); physicians at 0.72 | **Error, fixed: −$352B**. At 0.85: +$153B | Better access for Medicaid patients: their doctors' fees rise about 45% | **Error, fixed** |
| **The newly covered** | 80% of an all-ages average | 80% of people under 65 [EV-CAR-057] | **Error, fixed: −$310B**. At 70%: −$51B; at 100%: +$101B | — | **Error, fixed** |
| **Long-term care** | Outside the plan (HLT-7.07) | Urban's "enhanced" +21% includes it [SRC-3223] | Nursing-home out-of-pocket spending had leaked in (step 6) | — | **Leak fixed** |
| **The growth path** | CBO's growth in federal health subsidies, about 5.5% a year 2032-40, against nominal GDP at 3.8% | CMS: 5.4% a year for all health spending, 2025-34, against GDP at 4.1% [EV-CAR-056]; Holahan: holding growth to GDP has never been done [EV-CAR-742] | A national budget at GDP + 1 from 2037: **−$249B** | Squeezes rates or volume if growth runs hot; the review trigger is the guard | Reasonable as a baseline; D2 is the lever |
| **The other payers taken over** | All out-of-pocket spending moved into the plan; CHIP left out | Nursing-home and over-the-counter spending stays with households; CHIP moves | Step 6, +$13B (with $346B left with households); step 8, +$81B | — | **Errors, fixed** |
| **Double counting** | CHIP's federal money counted as replaced without its care; the states' share taken as CMS's total less CBO's federal subsidy | Steps 8 and 9 | The states' payment base falls $223B; federal money committed rises $153B | — | **Fixed** |
| **Private prices** | 2.08 times Medicare, blended | A volume-weighted average service by service | Hospitals and physicians: **+$235B** (step 4a, an error fixed). Other services at 1.1-1.2: **+$238B** (step 4b, a working assumption; range 0 to +$238B). Physicians at 1.29: +$96B more | — | 4a: **error, fixed**; 4b: **judgment, labeled** |

### 1.4 Against the independent literature

| Study | National spending under single payer | What drives it | How this plan compares |
| --- | --- | --- | --- |
| Urban 2019 [SRC-3223, EV-CAR-731] | "Lite" −6%; "enhanced" +21% | Lite: hospitals 115%, cost sharing; enhanced: no cost sharing, long-term care, dental | **−8% corrected.** Lite's prices, near-enhanced cost sharing, no long-term care |
| CBO 2020 [EV-CAR-218, EV-CAR-220] | −$0.7T to +$0.3T in 2030 (about −13% to +5%) | Rates dominate; the lower-rate case is 9% below the higher one | Inside the range, toward the low end |
| Galvani et al., Lancet 2020 [EV-CAR-230] | −13% | Administration, drugs, hospital rates near Medicare's | The gap is mainly D1, D5, hospitals at 1.15 rather than about 1.0, and provider-side administration |
| PERI 2018 [EV-CAR-231] | −10% | Administration, drugs, provider rates | Similar to this plan with D1, D2 and D5 |
| RAND 2019 [EV-CAR-228] | +1.8% (+9.8% with no supply limit) | Long-term care included, no cost sharing | Long-term care is outside this plan |
| Mercatus 2018 [EV-CAR-226] | $32.6T of new federal commitments over 10 years | Assumes provider payments more than 40% below private rates; argues they are unrealistic | This plan cuts private prices about 55% for hospitals (1.15 against 2.54) and about 25% for physicians, with a glide to 2036. Mercatus's doubt applies, and the glide and D3's 2036 review are the answer to it |
| Warren 2019 [EV-CAR-723, EV-CAR-724, EV-CAR-743] | Flat (sponsor); CRFB: +3% | Hospitals 110%, administration 2.3%, deep drug cuts, slower growth | With D1, D2 and D5, this plan sits between Warren's assumptions and Urban's |

Peer countries spend 11.2% of GDP on average against the US's 17.2% in 2024 [EV-CAR-128, EV-CAR-125]. On the model's growth path, national health spending in FY2040 is about 21% of GDP under the plan with the errors fixed, against about 23% under today's law. Part of the remaining gap to peers is higher US prices that the plan keeps on purpose: hospitals at 1.15 rather than about 1.0, and the glide. That is a choice for access, not an error.

### 1.5 The independent re-derivation

A separate agent (November 15) wrote its own version of the cost formula from `inputs.csv` and Table 19, without this tool. It reproduced the model's 2032 totals exactly ($5,755.5B as booked, $5,575.1B rebased) and the FY2040 gross of $8,407B.

It found the same errors and sized them close to this review. Leaving out the physician correction, its central combined estimate is −$506B in FY2040 (range −$383B to −$506B), against this review's −$338B for the same steps.

| Item | The agent | This review | Why they differ |
| --- | --- | --- | --- |
| Newly covered | −$327B | −$310B | Age mix |
| Medicaid's hospital index | −$397B (1.00, and hospitals 62% of benefits) | −$352B (1.00) | Service shares |
| Medicaid seam | −$227B gross; states' base −$115B at 50% (−$230B at 100%) | −$137B gross, −$223B states | The agent rebased the total on CBO's growth (3.7% a year); this review uses CBO's FY2032 level over Table 19's federal share. The agent's 2024 federal outlays came from its own knowledge, so this review doesn't use them |
| Private price average | +$251B | +$235B (4a), plus +$238B of working assumptions (4b) | The agent re-weighted all private non-drug services at a harmonic index; this review prices other services and dental separately, as a stated judgment |
| Out of pocket | +$63B net | +$13B | Service mix |
| CHIP | +$48B (CBO level) | +$81B (then −$9B in the rebase) | Level |
| Physician fix, payer-specific hospital shares | −$333B | −$275B (then −$56B in step 3) | Order of the steps |

This review's estimate is the more cautious of the two, and the recommendation does not depend on the difference. The agent's scripts and its `results.md` were kept in the session scratchpad and are summarized here.

### 1.6 Package A re-run with the corrections (Espen asked for the physician fix)

Households in 2026 dollars; losers in millions of bottom-four households (losing more than 5% of income).

| | Household rate | Q1 | Q2 | Q3 | Q4 | Q5 | Top 1% | Bottom-four losers |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Package A as merged (#386) | 10.61% | +5,062 | +7,837 | +7,164 | +782 | −17,150 | −97,247 | 26.9 (6.2) |
| **Physician fix only (1.05)** | **9.21%** | +5,098 | +8,178 | +8,124 | +2,651 | −13,742 | −84,837 | **22.3 (4.0)** |
| All the errors fixed (A1) | 7.86% | +4,642 | +7,501 | +7,338 | +2,096 | −13,191 | −75,160 | 22.1 (3.5) |

A1's poorest fifths gain slightly less than with the physician fix alone. The reason is step 6: households keep paying for nursing homes and over-the-counter products. Losers by fifth under A1 (millions): Q1 0.5, Q2 2.5, Q3 5.2, Q4 13.8.

## Part 2. Financing that passes the take-home test

### 2.1 The tests

1. **The take-home test (primary):** what visibly leaves a worker's pay and wallet must fall for most workers.
   - Today that is the premium share plus out-of-pocket costs on services the plan covers.
   - Under the plan it is the household contribution, copays, and the tax on the pay that used to go to the premium before tax.
   - A raise doesn't count.
2. **Employers no worse off as a group,** with small firms protected.
3. **Affordable at every income:** few households lose cash.
4. **Durable:** visible costs, growth against income, legal risk.
5. **The plan-wide gap kept visible.**

### 2.2 What can pay, besides households

**The cost.** With the errors fixed and D1, D2 and D5, the FY2040 gross is $7,345B.

**Sources every package shares** (FY2040, $B):
- federal money already spent on health, committed to the plan: 2,876 (the memo's 2,724 plus 153 from the Medicaid rebase);
- the 2.9% health payroll contribution, unchanged: 580;
- the states, at 100% of their former Medicaid spending: 466;
- the tax on pay that used to go to premiums: 292-358.

**New general revenue not yet in the plan** (FY2040, $B, central; each is net of what it overlaps on the ledger, `models/data/inputs/ledger-revenue.csv`):

| Stream | Central (range) | Evidence | Overlap with what is booked | Legal and durability risk |
| --- | --- | --- | --- | --- |
| Financial transactions tax raised from 0.01% to 0.1% | 60 (30-90) | Warren: about $800B over ten years at 0.1% [EV-CAR-729]. Trading volume falls as the rate rises | G10 (0.01%, $49B) stays; this is the increment | Low legal risk. Volatile with markets |
| Wealth tax: 2% above $50M, 3% above $1B | 150 (0-250) | Warren's plan [EV-CAR-730]. CRFB scored her wealth and accrual taxes at $1.5T central against $3.2T claimed [EV-CAR-738]. Valuing private businesses is hard [EV-CAR-733] | Net of G11 (billionaire mark-to-market, $82B) and G6 (gains at death) | **High:** apportionment of direct taxes (*Moore*, 2024, left it open). Stacked rates could pass 100% [EV-CAR-736] |
| Capital gains and dividends taxed as ordinary income above $1M of income | 45 (20-70) | Warren counted $2T over ten years for annual taxation of the top 1% [EV-CAR-730]; this is the narrower step. Realizations respond strongly | G6 (death), C18 (+1 point on top-bracket gains), G9 | Low legal risk. Behavioral risk is high |
| Corporate: rate 28% to 30%; the 2025 law's permanent expensing repealed | 70 (40-100) | Ledger: $135.7B per point over ten years (G1 note); Warren's corporate package [EV-CAR-729] | G1 (28%), G5, G7, C38 | Low legal risk |
| The 3.8% investment-income tax on active pass-through income | 60 (45-75) | Ledger H1a, $0.5T over ten years, priced but not booked | Not booked; SC2 overlaps it | Low |
| **Total** | **385 (about 200-560)** | | | |

**Booked revenue health may use first** (Espen: "We can downsize other expenditures in project 2050 plans in the financing settlement"). FY2040 audit lines, $B:

| Row | Booked FY2040 | Row | Booked FY2040 |
| --- | --- | --- | --- |
| G1 corporate 28% | 201 | C18 more top-end | 78 |
| G9 2025 cuts reversed above $450K | 182 | H1b Medicare and investment-income tax to 5% above $400K | 63 |
| C38 top-end scoring package | 114 | G8 enforcement | 55 |
| G6 gains at death | 92 | C39 itemized deductions capped at 28% | 50 |
| G11 billionaire mark-to-market | 82 | G7, G5, G10, G3 | 50, 49, 49, 38 |
| C43 45% above $5M; C35 estate tax; C40; C41 | 23, 20, 10, 7 | GX overlap adjustment | −62 |
| The indexed income contributions (4 points above $100K/$200K, 2 above $20K/$40K) | 484 | **Total available** | **1,582** |

Package E takes $579B of it, and F takes $847B. The other flagships keep the rest. Which rows go to health, and which flagships are cut, is stage G's question: health needs the money, not any particular row.

**This list includes the indexed income contributions,** and with them 2 points on AGI above $20,000/$40,000, which nearly every worker pays. If stage G keeps that row and gives it to health, it is a broad charge on workers that this memo's take-home test does not show. For the single worker at $72,000 it is about 2% × ($72,000 − $20,000) ≈ $1,040 a year, and they still pass ($1,371 + $1,040 = $2,411, against $5,679). **The grid and the pass rates show health's own charges only.** Recommended for stage G: take health's share from the top-end and corporate rows first, so the take-home result holds for the plan as a whole.

**Employers.** Package A sets employers as a whole at what they would otherwise spend. Packages E to G keep that rate (19.3% in the band) but add the **small-employer allowance**: the first $100,000 of each employer's pay in the band is exempt. It costs about $215B in FY2040, so employers as a whole pay about 10% less than they would have spent.
- It has no cliff, unlike Warren's exemption below 50 workers (Burman [EV-CAR-735]).
- **One allowance per controlled group:** businesses under common control share one $100,000, as the tax code does for benefit plans and as the phase-in's status rule does (`health-financing.md`, part 2.6). A firm can't split itself to multiply it.
- A firm of four $45,000 workers has $100,000 of pay in the band and pays nothing.
- It rests on a rough working figure: SUSB 2022 firm counts and pay (Census) give about 6% of all pay inside the allowance.
- Firms that offered no coverage in 2028 keep the phase-in, and the pay protections stay (`health-financing.md`, part 2.6).

### 2.3 The packages (FY2040)

Households in 2026 dollars; budget lines in FY2040 $B.

| | **A1. Package A, corrected** | **E. Take-home first (recommended)** | F. No household contribution | G. Self-financed above a line |
| --- | --- | --- | --- | --- |
| Gross cost | 7,795 | 7,345 | 7,345 | 7,345 |
| Household contribution | **7.9% of taxable income** | **0 below $100K/$200K; 4% of AGI above** | none | 12.7% of AGI above $100K/$200K |
| … collected | 1,549 | 268 | 0 | 847 |
| Worker transition credit paid back | 123 | 111 | 111 | 111 |
| Employer contribution (rate in the band) | 2,156 (19.3%) | 1,945 (19.3% above the allowance) | 1,945 | 1,945 |
| New general revenue | 0 | 385 | 385 | 385 |
| Booked revenue taken from other flagships | 0 | **579** | 847 | 0 |
| **Plan-wide FY2040 gap after health** | 70 | **649** | 917 | 70 |
| Top federal rate on wages | 70.9% | 67.0% | 63.0% | 75.7% |
| **Workers whose visible costs fall** | 36% | **90%** | 100% | 81% |
| **The single worker at $72,000: visible cost a year** (today 5,679) | 5,833 (fails) | **1,371** | 1,371 | 1,371 |
| Net per household Q1 / Q2 / Q3 | +4,642 / +7,501 / +7,338 | +4,819 / +9,453 / +12,949 | +4,819 / +9,453 / +12,961 | +4,819 / +9,453 / +12,925 |
| Q4 / Q5 / top 1% | +2,096 / −13,191 / −75,160 | +12,947 / −7,069 / −212,131 | +13,186 / −892 / −142,002 | +12,430 / −20,434 / −363,878 |
| Bottom-four households losing cash (losing more than 5%), millions | 22.1 (3.5) | **1.6 (0.1)** | 1.3 (0.0) | 2.3 (0.2) |
| On the evidence | Holds; fails the take-home test | Holds if the new streams come in near the center | Holds; the largest cut to the rest of the plan | **Doesn't hold:** at a 75.7% top rate the top tier yields far less than its statutory charge (`health-financing.md`, part 2.4) |

**Package E rests on yes to questions 2 and 3** (D1, D2 and D5, $449B together; D2 alone is $249B, and holding growth near GDP's has never been done [EV-CAR-742]). **On the errors-only cost ($7,795B, package E0 in the tool):**
- either **booked revenue taken rises from $579B to $1,029B** and the plan-wide gap from $649B to **$1,099B**;
- or the line rate rises from 4 points to **about 10.7 points** above $100K/$200K, near package G's ground and its top-rate problem.

Households below the line, the take-home result and the loser counts are the same either way.

**The sources add up exactly** (`_sources()`). E's in $B: federal money committed 2,876; health payroll contribution 580; states 466; employers 1,945; households 156 net of the credit; tax on former premiums 358; new streams 385; booked revenue 579. Total 7,345.

### 2.4 Who passes the take-home test

This is a worker tax unit by tax unit count on the household model's records (CPS, 2029, grown to FY2040; `take_home_micro()`). It covers every unit with wages or self-employment income. Each unit's visible cost today is its CPS-reported premiums plus out of pocket on covered services, by coverage.

| AGI (2026 dollars) | A1 | **E** | F | G |
| --- | --- | --- | --- | --- |
| Under $25,000 | 96% | **100%** | 100% | 100% |
| $25,000-50,000 | 58% | **100%** | 100% | 100% |
| $50,000-75,000 | 35% | **100%** | 100% | 100% |
| $75,000-100,000 | 31% | **100%** | 100% | 100% |
| $100,000-150,000 | 24% | **96%** | 100% | 80% |
| $150,000-200,000 | 13% | **85%** | 100% | 71% |
| $200,000 and over | 4% | **59%** | 100% | 29% |
| Job coverage today (67% of workers) | 28% | **88%** | 100% | 75% |
| A plan of their own (5%) | 75% | **98%** | 100% | 95% |
| Uninsured (14%) | 49% | **96%** | 100% | 92% |
| Medicaid (10%) | 45% | **98%** | 100% | 97% |
| Medicare (4%) | 50% | **91%** | 100% | 83% |
| **All workers** | 36% | **90%** | 100% | 81% |

**Who fails under E, and why:**
- **Single workers above about $190,000 with job coverage.** Their premium share is the same as everyone's, but the contribution grows with income.
- **Well-paid workers who are uninsured or on Medicaid today,** whose visible costs today are small.
- **Workers 65 and over on Medicare with high incomes.**

None of them is below $100,000.

### 2.5 The take-home grid (package E; FY2040, 2026 dollars a year)

Each cell is today's visible cost (grown to FY2040) → the plan's (its share of AGI).
- **Job coverage:** KFF's 2026 worker premium share [EV-CAR-722] and the model's out-of-pocket costs on covered services.
- **No coverage:** the uninsured's out-of-pocket costs.
- **Own plan:** a marketplace plan at $7,500 single and $22,000 family before credits (working figures), with credits on the original ACA schedule up to 400% of poverty.
- Copays are about $500 a person a year above 200% of poverty, and none below.

| Household | AGI | Job coverage | No coverage | Own plan |
| --- | --- | --- | --- | --- |
| Single | $25,000 | 3,910 → 414 (1.7%) | 2,038 → 0 | 4,359 → 0 |
| Single | $40,000 | 3,910 → 959 (2.4%) | 2,038 → 498 (1.2%) | 7,587 → 498 (1.2%) |
| Single | $55,000 | 3,910 → 959 (1.7%) | 2,038 → 498 (0.9%) | 10,568 → 498 (0.9%) |
| Single | $72,000 | 3,910 → 1,194 (1.7%) | 2,038 → 498 (0.7%) | 13,403 → 498 (0.7%) |
| Single | $90,000 | 3,910 → 1,194 (1.3%) | 2,038 → 498 (0.6%) | 13,403 → 498 (0.6%) |
| Single | $110,000 | 3,910 → 1,579 (1.4%) | 2,038 → 790 (0.7%) | 13,403 → 790 (0.7%) |
| Single | $150,000 | 3,910 → 3,226 (2.2%) | 2,038 → 2,390 (1.6%) **fails** | 13,403 → 2,390 (1.6%) |
| Single | $200,000 | 3,910 → 5,226 (2.6%) **fails** | 2,038 → 4,390 (2.2%) **fails** | 13,403 → 4,390 (2.2%) |
| Family of four | $25,000 | 16,738 → 1,849 (7.4%) | 8,152 → 0 | 12,282 → 0 |
| Family of four | $40,000 | 16,738 → 1,849 (4.6%) | 8,152 → 0 | 12,724 → 0 |
| Family of four | $55,000 | 16,738 → 2,058 (3.7%) | 8,152 → 0 | 14,785 → 0 |
| Family of four | $72,000 | 16,738 → 4,052 (5.6%) | 8,152 → 1,994 (2.8%) | 18,209 → 1,994 (2.8%) |
| Family of four | $90,000 | 16,738 → 4,052 (4.5%) | 8,152 → 1,994 (2.2%) | 22,121 → 1,994 (2.2%) |
| Family of four | $110,000 | 16,738 → 4,052 (3.7%) | 8,152 → 1,994 (1.8%) | 26,908 → 1,994 (1.8%) |
| Family of four | $150,000 | 16,738 → 5,100 (3.4%) | 8,152 → 1,994 (1.3%) | 42,394 → 1,994 (1.3%) |
| Family of four | $200,000 | 16,738 → 5,303 (2.7%) | 8,152 → 1,994 (1.0%) | 42,394 → 1,994 (1.0%) |

**Why the grid's single worker at $72,000 differs from test household T (2.6):**
- **The grid uses averages:** KFF's 2026 worker share for single coverage ($1,672) and the model's average out-of-pocket costs on covered services (about $1,110 a person in 2026). Grown to FY2040, today's cost is $3,910, the plan's $1,194, a saving of $2,716.
- **T uses the case in the brief:** $2,100 a year toward the premium and $1,950 out of pocket, both above those averages. Grown to FY2040, today's cost is $5,679, the plan's $1,371, a saving of $4,307.
- The plan's figure differs only through the tax on the larger premium share.
- So the same pay with average costs saves about $2,700, and with T's costs about $4,300.

| Single, $72,000, job coverage | Today (grown to FY2040) | Package E | Change |
| --- | --- | --- | --- |
| At KFF's and the model's averages (the grid) | 3,910 | 1,194 | −2,716 |
| **At T's own costs** | **5,679** | **1,371** | **−4,307** |

The job-coverage column's plan figure is mostly the income and payroll tax on the premium share that now comes as pay. Each worker gets that pay in full and keeps most of it. For the family at $72,000, $1,994 is four people's copays and $2,058 is the tax on the $10,500 that used to go to their premium share.

Under package A1 (the corrected broad contribution), every single worker with job coverage above about $45,000 fails, and so does every uninsured single worker above about $35,000. The full grids for all four packages are printed by `python3 models/tools/health_cost_review.py --part2 --md`.

### 2.6 Test household T: a single worker at $72,000

Today the worker pays about $175 a month ($2,100 a year) toward the premium and about $1,950 out of pocket: $4,050, or 5.6% of pay, in 2026. These are the case's own figures, from the brief, and both are above the averages the grid uses (2.5). Grown to FY2040 like everything else here (×1.40 in real terms), that is **$5,679**.

| Under | Household contribution | Copays | Tax on the pay that used to go to the premium | **Visible cost a year** | Against today |
| --- | --- | --- | --- | --- | --- |
| Package A (#386) | 10.6% × taxable income | 498 | 873 | 7,394 (10.3% of pay) | **+1,715: fails** |
| Package A, physician fix only | 9.2% | 498 | 873 | 6,600 | +921: fails |
| A1, all errors fixed | 7.86% × ($69,900 AGI + $2,945 former premium share − $16,100) = 4,461 | 498 | 873 | 5,833 | +154: fails |
| **E (recommended)** | **0** (AGI below $102,700) | 498 | 873 | **1,371 (1.9% of pay)** | **−4,307: passes** |

Under E the worker's take-home pay rises by about $2,945 (2026 dollars), the premium share that is no longer withheld, less $873 of tax on it. Their wallet keeps about $2,735 a year of former medical bills, less $498 of copays. That counts no raise from the employer's savings.

### 2.7 Employers by firm size

Per worker, 2026 dollars at FY2040's relative costs. Census SUSB 2022 firms and pay, raised 11% to 2026. Today's premiums assume these shares of workers covered by their own employer: 30% for firms under 20 workers, 45% for 20-99, 55% for 100-499 and 62% for 500 and over (working figures; 55% overall [EV-CAR-295]). They are grown so that employers as a whole break even under package A, as it is built.

| Firm size | Firms | Workers | Average pay | Premiums per worker today | Package A: contribution per worker | **Package E** (with the allowance) |
| --- | --- | --- | --- | --- | --- | --- |
| Under 20 | 5.72M | 22.0M | $54,940 | $4,941 (9.0% of pay) | $5,736 (+$795) | **$703 (−$4,238)** |
| 20-99 | 561,000 | 22.0M | $59,326 | $7,411 (12.5%) | $6,456 (−$956) | **$5,963 (−$1,449)** |
| 100-499 | 93,000 | 18.3M | $72,928 | $9,058 (12.4%) | $8,689 (−$370) | **$8,590 (−$468)** |
| 500 and over | 21,000 | 73.5M | $83,059 | $10,211 (12.3%) | $10,352 (+$141) | **$10,346 (+$135)** |

These are averages:
- **Within each size,** firms that offered generous coverage save, and firms that offered none pay more. The no-offer phase-in (2035-44) and the pay protections cover the second group.
- **Under E, a small firm that offered nothing** pays little or nothing, because the allowance covers most of its pay in the band.
- **Large firms are about even.** High-paying firms with lean plans pay a little more, as under package A.

### 2.8 Durability

| | A1 | **E** | F | G |
| --- | --- | --- | --- | --- |
| **Visible costs for typical workers** | High: 7.9% of taxable income | **None below $100K/$200K** | None | None below the line |
| **Growth against income** | The rate drifts up about 0.1 point a year, since health grows faster than incomes. With D2, little drift | General revenue must grow 5-6% a year. Top-end bases grow faster than GDP, which partly covers it. D2 holds the gap to about 1 point | The same, and larger | The line rate drifts up fastest |
| **Legal risk** | Low | **Medium:** the wealth tax ($150B). Without it, booked revenue rises to $729B (gap $799B), or the line rate to about 6.2 points | Medium | Medium |
| **Political risk** | A visible new tax on most workers | Taxes on the very rich, which are popular but contested. Stage G must cut or refinance $579B elsewhere | The largest hole in the rest of the plan | A 75.7% top rate; the yield falls short |
| **The stack on capital income** | As booked | Gains taxed as ordinary income above $1M (about 39.6% + 5% H1b + 1 point C18 + the 45% bracket above $5M), on top of G11's mark-to-market and a 2% wealth tax. At a 6% return, a 2% wealth tax equals about a 33% tax on that return, so the combined charge on the very wealthiest can pass 100% of their return [EV-CAR-736]. **For stage G:** add up the capital stack as `health-financing.md` 2.4 does for wages, and cap the wealth tax and the accrual taxes together | The same | Smaller (no wealth tax needed if the line rate rises) |
| **Reliance on the budget** | Low: most money is contributions | About $960B (13%) from general revenue beyond federal health money already spent. The law commits it to the plan's fund | About $1.2T (17%) | Low |

### 2.9 Recommendation: package E

- **It passes Espen's test:** 9 in 10 workers see their visible health costs fall, every worker below $100,000 does, and the single worker at $72,000 saves about $4,300 a year without counting any raise.
- **It is the fairest:** 1.6 million bottom-four households lose cash, against 22 million under A1, and the middle fifths gain $9,500-13,000.
- **It keeps employers whole,** and small firms better than whole.
- **It keeps a health contribution,** small and above a high line. That ties the plan's own fund to a visible, earmarked source, and it is the lever to adjust if the new streams fall short.
- **Its price:** about $1 trillion a year from the top and from corporations, and **$579B less for the rest of the plan**, so the FY2040 plan-wide gap rises to **$649B** for stage G.
- **Why not F:** it costs $268B more of other flagships' money for a 10-point gain in the pass rate, all of it among workers above $100,000.
- **Why not G:** it fails on the evidence of how top incomes respond.

**Not done here:** the year-by-year path for E (FY2030-39) and the decade gap. The household contribution's start in the waves (`health-financing.md`, part 2.3) would follow the same line. Both go to the booking PR.

## Part 3. What the review leaves standing in `health-financing.md`

- **Kept:**
  - the Medicare seam;
  - the payer accounting (part 1.3), with this review's national figures;
  - the employer contribution's base, the phase-in and the pay protections (part 2.6);
  - the worker transition credit (part 2.7; $111B in E);
  - the states at 100%, now on a $466B base;
  - the 2.9% payroll contribution;
  - part 7's comparison with the bills.
- **Superseded:**
  - the gross cost ($8,407B → $7,795B, or $7,345B with D1, D2 and D5) and part 1.2b (made here);
  - the national saving (6% → about 8%);
  - the package choice (part 3) and part 9's questions 1, 2, 12 and 17;
  - the household rate under A (10.6% → 7.9%).
- **Design memo D5 is new** (drugs 25% below today's prices). D1 and D2 are unchanged.

## Part 4. Questions for Espen

Each is decided on its own; none is adopted by silence.

1. **The cost corrections** (part 1.2, steps 1 to 9): book them in the next tier-3 booking PR? **Recommended: yes.**
2. **D5, drug prices 25% below today's** instead of 15%: about −$115B in FY2040. **Recommended: yes.** US prices would still be about twice peers'.
3. **D1 (administration 4%) and D2 (a national health budget at GDP + 1 from 2037):** as recommended in `health-financing.md`, now −$85B and −$249B. **Recommended: yes.**
4. **The package:** E (recommended), F, G, or A1? E's figures as shown assume yes to questions 2 and 3. Without them, E needs $1,029B of booked revenue (gap $1,099B), or about 10.7 points above the line (part 2.3).
5. **The household contribution under E:** 4% of AGI above $100,000 single / $200,000 couple (2025 dollars, indexed)? **Recommended: yes.** The alternatives: 0% (package F), or a lower line such as $75,000/$150,000, which raises more but fails more workers between the lines.
6. **The small-employer allowance:** the first $100,000 of each employer's pay in the band exempt, at about $215B? **Recommended: yes.** The alternatives: none (as package A), or $50,000.
7. **Each new revenue stream, decided one by one** (part 2.2):
   - **a.** the financial transactions tax at 0.1%;
   - **b.** the wealth tax, high legal risk;
   - **c.** capital gains taxed as ordinary income above $1M;
   - **d.** corporate 30% and repeal of permanent expensing;
   - **e.** the investment-income tax on active pass-through income.
   **Recommended: all five, with (b) drafted with a fallback** (a deferral charge on unrealized gains, as G11's).
8. **Health's first call on booked revenue:** $579B in FY2040, leaving a plan-wide gap of about $649B for stage G to close by cutting or refinancing the other flagships? **Recommended: yes,** as you directed.
9. **The worker transition credit and the employer protections** stay as in `health-financing.md`? **Recommended: yes.**

## Part 5. What a booking PR would change (tier 3, after Espen answers)

- The coverage model and the care path:
  - price the newly covered off people under 65;
  - Medicaid's hospital index;
  - payer-specific service mixes and volume-weighted price ratios;
  - administrative shares from Table 19;
  - out-of-pocket scope;
  - CHIP;
  - the Medicaid rebase to CBO;
  - the physician rate.
- The booked HLT-7 rows and HX on the corrected path; the states' share at 100% of the rebased base.
- The design memos adopted (D1, D2, D5).
- The package's rows, year by year: the line contribution, the employer allowance, the new revenue rows (each on the ledger with its overlap), and the reassignment of booked revenue to the plan's fund. The other flagships' gap stays visible on the board.

## Method and sources

- **Code:** `models/tools/health_cost_review.py`:
  - `table19`, `rebuild`, `check_reproduces`, `bridge`, `levers`, `cost_cases`;
  - `health_package`, `_sources`, `take_home_micro`, `grid`, `household_T`, `firms`, `reassignable`, `md`.
- **Run:** `python3 models/tools/health_cost_review.py` prints the bridge and the levers; `--part2 --md` prints the packages. **Test:** `python3 models/tools/test_health_cost_review.py`.
- **What it reads** (it changes none of them): `health_financing.py` and through it the coverage model, the care path, the booking, the budget model's audit and paths, and the household model's 2029 records; Table 19; CBO's February 2026 workbook.
- **Evidence in the register:**
  - CBO's coverage and subsidies [EV-CAR-051, EV-CAR-052];
  - per-person spending [EV-CAR-057];
  - NHE [EV-CAR-056, EV-CAR-120, EV-CAR-121];
  - RAND hospital prices [EV-CAR-131];
  - administration [EV-CAR-132, EV-CAR-217];
  - CBO's single-payer options [EV-CAR-218 to EV-CAR-220];
  - Mercatus [EV-CAR-226]; RAND [EV-CAR-228]; Galvani [EV-CAR-230]; PERI [EV-CAR-231];
  - OECD and Commonwealth Fund [EV-CAR-124, EV-CAR-125, EV-CAR-128];
  - KFF [EV-CAR-295, EV-CAR-722];
  - Warren and its reviews [EV-CAR-723 to EV-CAR-744];
  - Urban [SRC-3223].
- **Evidence still needed** (cited here in plain text). **Each needs an evidence entry before the booking PR relies on it**, above all those behind step 7 (−$352B, resting partly on the AHA, an interested party), step 4a (CBO 2022) and D5 (RAND for ASPE):
  - Medicaid's hospital payments against Medicare's: AHA payment-to-cost fact sheets, 2020 and 2023; MACPAC, "Medicaid Base and Supplemental Payments to Hospitals," 2024;
  - the physician fee index (Zuckerman, Skopec and Aarons, Health Affairs, 2021);
  - CBO, "The Prices That Commercial Health Insurers and Medicare Pay for Hospitals' and Physicians' Services," 2022;
  - RAND for ASPE, "International Prescription Drug Price Comparisons," 2024;
  - Census SUSB 2022, by enterprise size;
  - KFF's coverage rates by firm size, to replace the working figures in 2.7;
  - the wealth tax's yield and its legal standing (Saez and Zucman; Summers and Sarin; *Moore v. United States*, 2024).
- **Working assumptions,** each with a range in the text:
  - private prices for services other than hospitals and physicians: 1.1-1.2 times Medicare;
  - dental on the plan's schedule at 90% of private prices;
  - the uninsured's child share, 14%;
  - the new streams' central yields;
  - the allowance's 6% of pay;
  - coverage shares by firm size;
  - marketplace premiums.
