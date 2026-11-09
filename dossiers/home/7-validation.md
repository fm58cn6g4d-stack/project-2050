# A home you can keep: validation

Role: section 7 of the housing dossier, the adversarial section. It checks the plan's key numbers against independent sources, runs the models that apply and says what they miss, tests how housing lands with health, child care, the child tax credit and the secure floor for each group Espen named (`DEC-2026-11-09-06`), checks who the plan reaches by race, place and disability, answers the strongest objections, and names what would make the plan fail with the signals that would show it early. Status: draft (stage C, step 6). It reads sections 4 (`4-specification.md`, `provisions.json`), 5 (`5-delivery.md`) and 6 (`6-cost.md`), as revised for Espen's November 9 decisions (`DEC-2026-11-09-08` to `-11`): about $0.63 trillion over FY2030-39 and a FY2040 gap of about $12-19 billion, which goes to the financing settlement; stage 2's wider entry under `DEC-2026-11-09-12` is not yet in those figures (roughly $7-12 billion more in FY2040). Where those decisions answer a finding below, the finding says so. It changes no provision, cost or model input: every change it argues for is listed at the end, for the section owners or for Espen. Choices that are Espen's are questions, listed at the end and in the README.

## How to read this section

- **Evidence.** Tags in brackets point to `evidence.json`. Entries new to this section are EV-HOU-390 to 418. Section 5's evidence (EV-HOU-340 to 352) is cited here mostly by section and paragraph ("section 5, 2.2"). "This section's arithmetic" marks a calculation done here from cited figures; "judgment" marks reasoning without evidence behind it.
- **Outcomes.** The plan is meant to move OUT-04 (a home people can keep), OUT-02 (planning beyond the next paycheck) and OUT-01 (child poverty). Section 9 of this file ties each early-warning signal to one of them.
- **Other dossiers.** Health, care, the child benefit, the secure floor and immigration have no dossier sections yet. Where this section relies on their designs it reads `legacy/domains/` and the ledger and labels the finding **provisional**. Section 4 lists the checks those dossiers owe.
- **What "holds" means.** A number holds when an independent source lands inside the plan's low-high range. It is "at risk" when independent evidence sits at or beyond one end of the range.

## In brief

1. **The money per household holds.** The plan's subsidy per leased household ($17,000 in FY2030, section 6) follows HUD's own 2023 spending [EV-HOU-370] and sits above CBO's older per-voucher figure [EV-HOU-391] for reasons that hold up: rents rose fast, and the plan's households are poorer and larger than the average voucher family. The risk runs upward, not downward, and the high case covers it.
2. **Lease-up is the weakest assumption.** Section 6 assumes 90% of awards are leased at steady state, after reissue. The closest precedent, Emergency Housing Vouchers, had 67% of its awards leased after about two years despite full fees and waivers (section 5, 2.2), and the share of individual searches that succeed fell from 66% in 2020 to 57% in 2022 [EV-HOU-395]. A lower lease rate makes the plan cheaper and the reach smaller: at 75% leased, about 150,000 fewer households are housed by 2034 than the central case says. The right that begins in 2037 could have become a right to a voucher a family cannot use; Espen's duty to house (`DEC-2026-11-09-10`) now requires a placement when a search fails, which answers that for stage 2 but not for stage 1's awards.
3. **Stage 1 may be larger than the million.** Section 4 counts families doubled up for economic hardship as "without a home". That definition is far wider than the one-night count, and nobody has counted it for this plan. If it is used, stage 1 alone could take every award and push stage 2 back.
4. **The plan's own building is small next to the shortage.** Section 4's count is about 1.3 million homes the plan pays for over the decade, credits and loan-only homes included, and about 1.0 million net new homes once crowd-out and the zoning reward are counted (HOU-3C.04). The shortage is 4-5 million homes, and 7.1 million affordable rentals for the poorest renters [EV-HOU-017] [EV-HOU-018]. Espen decided to publish a production target (`DEC-2026-11-09-10`); section 4 now proposes three numbers (HOU-3C.04): about 1.3 million homes the plan pays for, credits and loan-only homes included; homes finished in zoning-reward places at least 1% of their stock above their prior pace, about 600,000 nationally; and a national goal of 15 million homes over 2030-39, about today's pace. Section 1.4's arithmetic supports the construction money's share if costs stay in its range.
5. **Income counting mostly works, with two clawbacks.** The monthly child benefit does not raise rent [26 U.S.C. 6409; section 4]. But free child care removes the child care deduction from voucher rent, so housing takes back about 30 cents of each dollar of care costs a family no longer pays [EV-HOU-409] [EV-HOU-410]. New Social Security and SSI income, and paid leave, count in full.
6. **Mixed-status families were the clearest gap; the design now closes it.** The adopted child benefit uses a taxpayer identification number [EV-HOU-404], so families with parents filing on ITINs get it. Housing prorates their help under Section 214, and HUD's February 2026 proposed rule would make that proration temporary, pushing these families out [EV-HOU-402] [EV-HOU-403]. Espen decided to protect prorated help and repeal the proposed rule, possibly in statute (`DEC-2026-11-09-10`), and to keep the shared record to basic information with a bar on immigration enforcement use (`-11`). Section 4 writes both (HOU-4.01, HOU-4.02). The gap remains until the regular bill passes.
7. **A worker on a voucher keeps about 25 cents of each added dollar.** In the earned-income credit's phase-out range, voucher rent, the credit's phase-out and SNAP take about 75 cents before payroll and income taxes [EV-HOU-410] [EV-HOU-416] [EV-HOU-417] [EV-HOU-418]. That is current law, but the plan brings about 1.8 million more households into it. The evidence says rent rules alone change earnings little [EV-HOU-400].
8. **Tribal areas and older non-disabled renters fell through.** Tribal housing problems are mostly physical condition and crowding, which vouchers do not fix [EV-HOU-406]. Espen decided on dedicated tribal policy and set-asides (`DEC-2026-11-09-10`): section 4 now sets aside shares of the emergency fund, the new awards and the construction grants, through tribes (HOU-4.13). Whether the shares match the need is unknown, because the register has no count of tribal homes needing repair. About 1.75 million older extremely low-income renters with severe problems still have no funded route in the 2030s [EV-HOU-186]; Espen will reconsider them once the care program is scoped (`-10`).
9. **What holds up:** the targeting (vouchers for homeless families are among the best-evidenced social programs [EV-HOU-086] [EV-HOU-408]), the take-up assumption for stage 2 (inside the range of SNAP and the earned-income credit [EV-HOU-398] [EV-HOU-399]), the guardrails, and the delivery design's answers to the last national program's failures.

## 1. Benchmarks

Each row sets the plan's figure beside independent ones. "Plan" is section 6's central figure with its low-high range.

### 1.1 Cost per voucher

| Source | Figure | Year | Grown to FY2030 (this section's arithmetic) |
| --- | --- | --- | --- |
| HUD, spending per voucher unit [EV-HOU-370] | $1,068 a month, about $12,800 a year | 2023 | $15,800 at 3% a year; $16,900 at 4%; $18,000 at 5% |
| CBO, average spending per voucher household [EV-HOU-391] | $9,400 a year | 2019 | HUD's 2023 figure is already 36% higher, about 8% a year, so CBO's older figure is superseded |
| CBO, all households at or below 30% of area median income, phased in over ten years [EV-HOU-390] | $290 billion for 4.5 million households over 2016-25 | 2015 | About $11,700 per household-year in 2016-25 dollars if the phase-in is even (this section's arithmetic) |
| Urban Institute, average subsidy for a new voucher under full funding [EV-HOU-392] | $765 a month, about $9,200 a year | 2022 | Lower than the plan because Urban's new vouchers reach everyone under 50% of area median income, not only the poorest |
| **Plan** (section 6) | **$17,000** ($15,500-18,500) subsidy, plus 8.1% fees | FY2030 | — |

**Verdict: holds, with the risk upward.**
- The plan's figure is HUD's 2023 spending grown at 4% a year. The account grew much faster than that in FY2019-23 [EV-HOU-187], so 4% is not generous.
- The plan's households are poorer than the average voucher household. Stage 1 is homeless households and stage 2 extremely low-income families with children, so tenants pay less and families need larger units. Both raise the subsidy above the national average (judgment; the register has no subsidy by household type).
- Three design choices push the cost per award up. Section 6 now prices two of them: payment standards up to 120% where lease-up is low (about $7 billion over the window; section 6, 1.2) and full fees (section 6, question 8). The third, neighborhood payment limits (HOU-4.05), which raise payments in high-rent ZIP codes [EV-HOU-095], is still unpriced.
- The high case ($18,500, 5% a year) covers all of this. **Ask of section 6:** report the cost per award for stage 2's families separately from the national average, once HUD's tabulation by household type is in the register.

### 1.2 Lease-up

| Source | Measure | Figure |
| --- | --- | --- |
| Emergency Housing Vouchers, with full fees and waivers (section 5, 2.2) | **Awards leased, with reissue** (the plan's own measure) | 87% leased or issued after a year; 67% leased after about two years; 129 of 610 agencies under half |
| Searches that succeeded [EV-HOU-395] | Per search, within the search term | 57% in 2022, down from 66% in 2020; median successful search 78 days |
| New voucher holders [EV-HOU-092] | Per new holder, within six months | 61% (2015-19) |
| Rural against urban agencies [EV-HOU-396] | Per search, within six months | 58.5% against 62.3% (2019); success is lower in rural counties in 2022 too [EV-HOU-395] |
| National voucher units [EV-HOU-370] | **Units occupied** of units authorized, held down by funding as well as by search | 84% (2023) |
| Urban Institute's caveat on full funding [EV-HOU-394] | Per search | The success rate "would likely fall" as more households search |
| **Plan** (section 6) | **Awards leased at steady state, with reissue** | **90%** (84-98%); 6 months from award to lease (3-9) |

**Verdict: at risk.** The measures differ, so they are not compared one for one. A per-search rate understates the plan's measure, because a household whose first search fails can search again with a reissued voucher. The national occupancy rate is held down by funding limits as much as by search, so it is not a ceiling. The verdict rests on the two measures that bear directly: the only precedent measured the plan's way, Emergency Housing Vouchers, reached 67% after about two years, more than twenty points below the plan's 90%; and search success has been falling [EV-HOU-395]. Section 5's fixes (full fees, search help, over-issue, reallocation, a backstop administrator, source-of-income protection) are the right ones, and each has evidence behind it. But no program in the register has reached 90% at the plan's pace, and the plan's first awards land in the tight markets where homelessness is concentrated [EV-HOU-414] and lease-up is worst [EV-HOU-092].

**What a lower rate does** (this section's arithmetic on section 6's central case: the rent cost scales with the leased share).

| Leased share | HOU-4A rent cost, FY2030-39 | Households leased of the million (from FY2034) | Reach lost against the central case |
| --- | --- | --- | --- |
| 90% (central) | $136 billion | 900,000 | — |
| 84% (section 6's low case) | about $127 billion | 840,000 | 60,000 |
| 75% | about $113 billion | 750,000 | 150,000 |
| 67% (EHV after about two years) | about $101 billion | 670,000 | 230,000 |

- A low lease rate shows up in the budget as a saving and in people's lives as a failure. Section 6's low case already includes 84%. Section 6 now has a 75% reading (about $0.59 trillion over the window, about 390,000 fewer households housed in FY2042) and reports households housed as a range, saying lower lease-up is not a saving (section 6, 1.4). That ask is met. It remains that a shortfall must not count toward the D4 test as available money.
- **Stage 2 compounds it.** Section 6 assumes 85% of eligible families apply, and 90% of those lease: about 77% of the group housed. At a 75% lease rate it is about 64% (this section's arithmetic). After 2037 the statute promises help to every eligible family that applies (HOU-4D.01). A family whose voucher expires unused would have the right on paper only. **Ask of section 4, met:** Espen made help finding a home part of the right (`DEC-2026-11-09-10`), and HOU-4D.01 now requires search help, landlord recruitment and, when a search fails, an offer of an attached home or a reissued voucher with a higher payment standard by a deadline (60 days proposed). Section 6 prices it at about $3 billion over FY2037-39. The verdict on lease-up stays **at risk**: the duty protects stage 2's families from 2037, but stage 1's awards in 2030-33 carry no such duty, and placements depend on attached homes existing in tight markets.

### 1.3 Take-up of the right

| Program | Share of eligible people or filers who take it up |
| --- | --- |
| SNAP [EV-HOU-398] | 88% (FY2022, the highest on record) |
| Earned income credit [EV-HOU-399] | 78% of filers, 81% of dollars (tax year 2021) |
| **Plan, stage 2** (section 6) | **85% apply** (70-100%) |

**Verdict: holds.** The central figure sits between two large programs, and stage 2's families have severe housing problems, which should raise sign-up. Full take-up (the high case) is unlikely by these benchmarks. The larger risk is in the count, not the rate: when help becomes a right, families now doubled up may form their own households and apply, and the 1.2 million central count would grow. The Urban Institute's simulation leaves this out for the same reason [EV-HOU-392]. **Ask of section 6:** add the count risk to the high case's description.

### 1.4 Homes per dollar of capital

When this section was drafted, the plan set no target for homes built or preserved by HOU-3C, HOU-8 and HOU-9A, so neither section 7 nor voters could check the capital against a promise. Espen decided to publish one (`DEC-2026-11-09-10`), and Espen then asked for three numbers. Section 4 proposes them (HOU-3C.04): about 1.3 million homes the plan pays for directly, credits included (range 0.8-1.9 million), of which the construction money below is about 900,000 (600,000-1.3 million), counting grant-financed homes and loan-only homes; a zoning-reward goal; and a national goal of 15 million homes over 2030-39. This section's rough arithmetic (judgment on every input):

| Line | Money | Cost per home used | Homes financed |
| --- | --- | --- | --- |
| HOU-3C.01 revolving fund grants, with the 20% state match | About $86 billion | $150,000-300,000 of gap subsidy per home | About 290,000-580,000 |
| Of which: at least 30% as deep grants for extremely low-income homes | About $26 billion | $200,000-300,000 | About 85,000-130,000 |
| HOU-3C.02 construction and acquisition loans | $300 billion of commitments | $250,000-350,000 of loan per home | Up to about 0.9-1.2 million, overlapping with the grants and tax credits, and fewer where loans buy existing buildings |

- **Cost per home.** Median development cost per tax-credit home was $321,967 in Washington State's recent certifications, and $406,303 in the latest year [EV-HOU-412]; about $708,000 in California in 2023 [EV-HOU-411]. Soltas puts the cost per *net new* home of a tax-credit expansion near $1 million nationally and about half that in dense places [EV-HOU-275] [EV-HOU-277].
- **Net new homes.** One subsidized home adds a third to a half of a home to the stock on average [EV-HOU-114]. So the plan's net addition is perhaps 0.2-0.5 million homes over the decade (this section's arithmetic), against a national shortage of 4-5 million [EV-HOU-017] and 7.1 million for the poorest renters [EV-HOU-018].
- **What this means.** The plan is a rental help plan with a construction supplement, which is what Espen chose (memo 1 B, memo 3 part 3 B). It should say so plainly rather than let the capital lines read as a supply answer. Acquisition and preservation keep existing homes affordable, which counts for tenants, but adds nothing to the stock.
- **Ask of section 4, met:** HOU-3C.04 sets the target, reports built and preserved homes apart, estimates net additions without targeting them, and reports yearly by place and income band. **Verdict on the construction money's share: holds within this arithmetic's range** if gap subsidy stays near $150,000-250,000 a home; at $300,000 or more the grants alone reach about 290,000 and the target needs loan-only deals at scale. The credits' share rests mostly on an industry estimate with a stake [EV-HOU-444], so it is the softest part of the direct count. The national goal is plausible: it holds the 2022-25 pace [EV-HOU-440], but the Joint Center's baseline demand alone would let building fall to about a million a year [EV-HOU-441], so meeting it depends on closing the shortage, which federal policy influences but does not control.

### 1.5 Homelessness

| Evidence | What it says |
| --- | --- |
| Family Options Study, randomized [EV-HOU-086] | Priority access to a long-term subsidy reduced homelessness for families in shelters, at 9% more cost than usual care |
| Welfare to Work Vouchers, as summarized by CBPP [EV-HOU-408] | Families in shelters or on the street fell from 13% to 3%; without a home of their own from 45% to 9%; crowding from 46% to 22% |
| HUD-VASH [EV-HOU-176] | Each added voucher cut homeless veterans by about one |
| Communities over time [EV-HOU-083] | One added permanent housing bed went with 0.12 fewer homeless people, fading after a year |
| Housing First trials [EV-HOU-099] [EV-HOU-100] [EV-HOU-101] | Large gains in stable housing for people with serious mental illness |
| One-night count against a year's flow [EV-HOU-014] [EV-HOU-415] | 745,652 people on a night in 2025; in 2018, about 1.45 million people used a shelter at some time in the year, against about 580,000 on a night in 2020 |

**Verdict: the direction holds; the size is unknown, and the plan should not promise to end homelessness.**
- For the household that gets the voucher, the effect is large and well tested.
- For the national count, the evidence runs from about one fewer homeless person per targeted voucher [EV-HOU-176] to about one in eight per added bed [EV-HOU-083]. The gap is inflow: people keep losing homes, and a year's flow is more than twice a night's count [EV-HOU-415].
- On the plan's numbers (this section's arithmetic): 0.7-0.9 million households leased from the first million by 2034, mostly stage 1. At the VASH rate that would be most of the one-night count; at the community rate, about 0.1 million fewer people on a given night. Section 4's check ("share of homeless households reached by 2033") is the right test, but it needs a counted denominator.
- **Stage 1's size is not defined.** Section 4's draft included families doubled up because of economic hardship. Espen has since decided one plain test that includes doubled-up families with children, with no cap, counts published yearly and a review if stage 1 and stage 2 fall out of balance two years running (`DEC-2026-11-09-12`). That is close to the Education Department's definition for homeless students, not HUD's for its homelessness programs, and it is many times larger than the one-night count (the register has no count; evidence still needed). If the plan uses it, stage 1 could absorb all million awards and delay stage 2. **Ask of section 4, and a question for Espen:** whether doubled-up families are in stage 1, in stage 2, or in stage 1 only when they have children.

### 1.6 Emergency aid: cost per crisis averted

| Evidence | Figure |
| --- | --- |
| Chicago, callers when funds happened to be available [EV-HOU-108] | 76% less likely to enter a shelter; about $10,300 per case of homelessness averted (2010-12), less with better targeting |
| Santa Clara trial [EV-HOU-109] | About $2,000 average aid; 81% less likely to become homeless in six months, 73% in twelve |
| J-PAL review [EV-HOU-407] | $1.99-2.47 of benefits per net dollar in two studies; averting homelessness cost 35% less for very low-income families; each added week of waiting raised the chance of an eviction filing by up to 29% |
| Five broad pandemic lotteries [EV-HOU-153] | Aid raised rent payment but changed housing stability little |
| **Plan** (section 6) | $5 billion a year at about $3,500 per household: about 1.4 million households a year |

**Verdict: at risk on targeting, not on cost.**
- The cost per crisis averted is the cost per household divided by how much aid lowers each household's risk. A household whose chance of homelessness is 20% in a year, cut by three-quarters, costs about $23,000 per homelessness averted at $3,500; at a 5% risk, about $93,000 (this section's arithmetic).
- Chicago's low figure came from people calling a homelessness line [EV-HOU-108]. The plan's fund is open to any renter under half of area median income with a notice, a filing or a shutoff (HOU-1D.01), a broader and lower-risk group. The broad pandemic programs found little effect on stability [EV-HOU-153].
- So the fund's value rests on the risk screen and on speed (HOU-1D.02, 30-day payment) [EV-HOU-407]. Both are in the design. **Ask of section 4:** randomize at the margin of the screen in each grantee's first year, as the Santa Clara and Chicago studies did, so the fund measures what it averts.

### 1.7 Summary of the benchmarks

| Number | Plan | Independent range | Verdict |
| --- | --- | --- | --- |
| Subsidy per leased household, FY2030 | $17,000 | $15,800-18,000 from HUD's 2023 figure | Holds; risk upward |
| Awards leased at steady state, with reissue | 90% | 67% after about two years (EHV); per-search success 57-66% and falling | At risk |
| Take-up of stage 2 | 85% | 78-88% | Holds |
| Homes the plan pays for | Proposed: about 1.3 million built or preserved, credits and loan-only homes included (0.8-1.9 million); construction money's share 900,000 | About 290,000-580,000 from the grants, more with loan-only deals; credits' share from an industry estimate; 0.2-0.5 million net from the capital (arithmetic) | Holds within the range; at risk if costs run high; the credits' share is soft |
| National homes finished, 2030-39 | Proposed goal: 15 million (13-16.5 million); the plan's own net addition about 1.0 million | 1.39-1.63 million a year in 2022-25 [EV-HOU-440]; holding that pace builds about 6 million more than baseline demand (about 8.7 million in completion terms), against a 1.5-5.5 million shortage [EV-HOU-441] [EV-HOU-442] | Plausible; depends on closing the shortage |
| Homelessness reduction | Not stated | 0.12-1 fewer homeless person per targeted award | Direction holds; size unknown |
| Emergency fund | $5 billion a year, 1.4 million households | Value depends on risk targeting | At risk on targeting |

## 2. Model runs

### 2.1 What was run

| Tool | Run | Result |
| --- | --- | --- |
| Child poverty microsimulation (`models/tools/child-poverty/`) | `run_validation.py` and `check_agenda_results.py`, November 9, 2026 | Both pass: 117 tests, the stored eight cases and 42 sensitivities. The national rerun needs the Census archive, which is not in the repository; the stored national results are used below |
| Budget model (`models/tools/budget/`, fiscal model) | Through `bash .github/scripts/run-checks.sh` | 19 benchmarks, 16 pass, 3 fail (PS-4a, PS-4b, TF-2); milestone not passed (`MODEL-CARD.md`) |
| Household incidence (`models/tools/incidence-model.py`) | Through the same checks | Housing carried as one row, $0.56 trillion on a 60/25/10/4/1 quintile key (`models/data/inputs/incidence-keys.csv`) |
| Scenario calendar | Read through section 5 | Ranges only |

### 2.2 What the household model can say

The stored national run (`legacy/sources/family-comparison-model-checks.md`) compares voucher counts with the child benefit held fixed:

| Credit | Delivery | New awards | Child poverty | Deep poverty |
| --- | --- | --- | --- | --- |
| AFA (FAM-1D analogue) | Enhanced | 400,000 | 8.55% | 1.93% |
| AFA | Enhanced | 1,000,000 | 8.34% | 1.85% |
| AFA | Enhanced | 6,755,114 (about every eligible renter) | 6.32% | 1.16% |

- **The million awards lower child poverty by about 0.2 points** over 400,000, with the child benefit in place. The full-coverage case cuts it by about 2.2 points. The Urban Institute's independent simulation finds full voucher funding cuts child poverty by 23% [EV-HOU-393], which is the same order as the model's full case (8.55% to 6.32% is about 26%).
- **It understates the plan for children, for four reasons.** The model hands out awards at random among proxy-eligible renters, adult-only households included, while the plan puts homeless families and then families with children first (HOU-4.03). It has no stage 2 (about 0.9-1.0 million more families with children by 2039), no stage 3 and no emergency fund (its primary case gives the fund no cash value). And it caps awards on the legacy 100,000-a-year path.
- **It may overstate it in one way.** It assumes the lease-up rate it is given, and section 1.2 argues the real rate could be lower.
- **What it would take** to score the plan's order: an allocation rule that follows HOU-4.03, a stage 2 cohort, and the Census archive (an upload from Espen, as before). That is model work, not done here, and it belongs to the household model's owner with the secure floor dossier.

### 2.3 What the budget model can say

- **It can** carry section 6's paths and read the D4 tests: the maturity test, the envelope and the guardrails. The arithmetic and interest benchmarks that those readings rest on pass.
- **It cannot** estimate what a housing provision costs: each row's total comes from the ledger (`MODEL-CARD.md`, "What it is not for"). Section 6's figures are section 6's arithmetic, laid over the model's paths, not a model run. No benchmark tests a housing cost.
- **The open benchmarks do not bear directly on housing's rental lines**, which are mandatory. They do bear on the capital spend-out, which section 6 sets by judgment (15/35/30/20%) and which decides the FY2040 capital tail (section 6, 3.3).
- **The cautious readings are not computed** (`ASM-CALIB-MID`). Housing's high case fails FY2040 and FY2041 (section 6, 3.3), and the model has not run it.

### 2.4 What the incidence model can say

- The D3 screen counts housing as $0.56 trillion, 60% to the bottom fifth (`legacy/index/revenue-household-incidence-model.md`). It does not include HOU-4D, stage 3 or section 6's new paths.
- **Its housing key treats every dollar as a benefit to tenants.** Two parts are not: tax credits, where developers keep about half the subsidy in profit and another quarter goes to competing for awards [EV-HOU-276]; and any part of voucher spending that raises market rents for unassisted renters (section 5.1 below) [EV-HOU-397]. For D3 this changes little, since housing's share of the package is small and both effects fall mostly outside the fourth quintile, but the housing row's bottom-fifth benefit is overstated (judgment).

### 2.5 What the models miss

1. **Rent offsets from other flagships' benefits** (shared rule 1). No model applies the 30% rent rule to new income or to deductions that shrink (section 3 below).
2. **SNAP's response to lower rent.** When a voucher lowers a family's rent, SNAP's shelter deduction can fall and SNAP benefits with it. That lowers the family's net gain and federal SNAP spending. CBO would count the SNAP change in a score of the bill; section 6 counts no offset (judgment).
3. **The plan's order of reach** (2.2 above).
4. **Lease-up as a result, not an input.** Every model takes the lease rate as given.
5. **Market rents.** No model lets vouchers move rents [EV-HOU-397] [EV-HOU-096].
6. **Labor supply.** No housing row has an earnings response [EV-HOU-088] [EV-HOU-400].
7. **Supply.** No model turns capital into homes, or homes into rents.
8. **Place.** No model works below the national level, so tight markets, rural areas and tribal lands are invisible.
9. **Immigration status.** The household model, rightly, imputes no status (`models/tools/child-poverty/README.md`), so it cannot see proration or the proposed HUD rule.
10. **Homelessness.** No model has the homeless population, which is not in the household surveys.

## 3. How housing lands with the rest of the plan, by group

Espen's direction (`DEC-2026-11-09-06`): say how housing lands together with the health coverage expansion, child care, the expanded child tax credit and the secure floor, for each group in need. The mechanisms below are checked against current law where the register has it. **Everything about the other flagships' designs is provisional**: it reads the legacy domain files, not decided dossiers.

### 3.1 The income rules, checked

| Benefit | Counted for voucher rent? | Basis | What it does to a voucher family |
| --- | --- | --- | --- |
| Monthly child benefit (FAM-1D, refundable, advance payments) | No | 26 U.S.C. 6409 excludes refundable credits and their advance payments (shared rule 1) | Kept in full |
| Earned income credit | No | Same | Kept in full |
| Child care made free or capped (FAM-2) | Not as income, but **the child care deduction shrinks** | Adjusted income subtracts reasonable child care costs needed for work or school [EV-HOU-409]; voucher rent is 30% of adjusted income [EV-HOU-410] | A family that stops paying $1 of care pays about 30 cents more rent. Net gain 70 cents |
| Medicare's out-of-pocket cap (HLT-2); home care through Medicaid (HLT-4) | Not as income, but **the medical and attendant-care deduction can shrink** | For elderly or disabled families, medical costs above 10% of income are deducted [EV-HOU-409] | A small clawback, only where costs exceed 10% of income |
| Higher minimum Social Security benefit (SS-3), CPI-E (SS-4) | Yes | Income counts all sources not excluded (shared rule 1) | About 30 cents of each new dollar goes to rent |
| Paid leave benefits (FAM-3) | Yes | Same | Replaces wages that counted anyway: neutral |
| Higher wages (LAB-4) | Yes | Same | 30 cents a dollar, at the next annual review (shared rule 2) |
| Medicaid, CHIP, marketplace subsidies | No | Not income for rent | — |
| SNAP | No; but **SNAP falls when rent falls** | SNAP is the food plan minus 30% of net income [EV-HOU-417], and rent above half of income is deducted | Part of the voucher's value is taken back by SNAP for rent-burdened families entering help |

**Findings.**
- The child benefit and the earned income credit are safe. That is the most important interaction, and it works.
- **The child care clawback is the one a family would notice.** It is current law working as written, but the plan creates it at scale: FAM-2's free care below 75% of state median income removes the deduction for every voucher family that used it. Options for the secure floor and care dossiers (not decided here): count the value of free care as a continuing deduction, or exclude care benefits from the adjusted-income calculation by statute. The register has no count of voucher families taking the child care deduction (evidence still needed).
- **Social Security and SSI increases are clawed back by 30%** for assisted older and disabled renters. This is the 1437a rule working as designed for income. Whether to exempt new benefits is the secure floor's call (shared rule 1); section 6 should report the effect at both ends.

### 3.2 How fast help falls as earnings rise

A single parent with two children, on a voucher and SNAP, earning in the earned income credit's phase-out range, loses on each added dollar (this section's arithmetic; payroll and income taxes not included):

| Layer | Cents of each added dollar |
| --- | --- |
| Voucher rent: 30% of adjusted income [EV-HOU-410] | 30 |
| Earned income credit phase-out, two or more children [EV-HOU-416] | 21 |
| SNAP: 30% of net income [EV-HOU-417], after the 20% earnings deduction [EV-HOU-418] | 24 |
| **Total before payroll and income taxes** | **about 75** |

- The plan's child benefit adds nothing to this: it is fully refundable and phases out well above these incomes (FAM-1D; provisional, judgment). FAM-2's 7%-of-income cap would add up to 7 cents above 75% of state median income, and its design may create a cliff there if the 7% applies to all income at once (for the care dossier to check).
- **This is current law, not something the plan adds.** But the plan brings about 1.8 million more households into it by 2039 (stages 1 and 2). CBO's average for low- and moderate-income workers is 31%, because most households do not take every program at once [EV-HOU-401].
- **What the evidence says it does.** In Chicago's voucher lottery, using a voucher cut labor force participation by about 4 points and earnings by 10% [EV-HOU-088]. The Family Options Study found a small drop in any employment and no effect on average earnings [EV-HOU-086]. HUD's randomized Rent Reform Demonstration found that a rent rule built to reward work did not raise earnings after six years [EV-HOU-400]. So the stacked rate is real, but changing housing's 30% alone would buy little work.
- **Timing softens it.** Earnings rises are counted at the next annual review (shared rule 2), so within a year the housing layer is often zero.
- **For the secure floor (shared rule 2):** the ceiling on the combined rate must be set with housing in it. Housing's working answer (no new phase-out) stands; the escrow-only Family Self-Sufficiency pilot [EV-HOU-236] is the cheapest test of a way to bank the rent rise.

### 3.3 Cliffs

| Where | What happens | Size or status |
| --- | --- | --- |
| Stage 2 entry at the extremely low-income line (HOU-4D.01) | A family $1 above the line gets no long-term help until no stage covers it | A notch, by design; the exit line (80% of area median) is generous, so there is no exit cliff |
| Emergency fund at 50% of area median income (HOU-1D.01) | A hard eligibility line, softened by the program-enrollment route | Small: one-time help |
| Child care at 75% of state median income (FAM-2; provisional) | Free care ends; the 7% cap begins | For the care dossier |
| Medicaid to marketplace at 138% of poverty (HLT-1; provisional) | With enhanced credits made permanent, the premium step is small | For the health dossier |
| Gross-income test for SNAP (current law; varies by state) | SNAP can end at once | For the secure floor |

### 3.4 Group by group

**Families with children.**
- *Housing:* stage 1 for homeless families; stage 2, the right from 2037, for the poorest families with severe problems; attached homes outside high-poverty areas; search help.
- *With the rest:* the child benefit is kept in full (3.1); child care raises voucher rent slightly through the lost deduction; the stacked phase-out applies to working parents (3.2).
- *Gaps:* a family above the extremely low-income line with severe problems has no route; mixed-status families with children (below).
- *Checks owed:* the household model's run with the plan's order (2.2); the care dossier on the deduction.

**The lowest-income households.**
- *Housing:* the stages in order, and the emergency fund for crises.
- *With the rest:* new income outside the tax code costs 30 cents a dollar in rent; SNAP takes back part of a voucher's value (2.5).
- *Gaps:* single adults and other households with severe problems who are not homeless, not disabled and not in a family with children have no funded route in the 2030s: 1.78 million other nonfamily households and 0.56 million other families among the extremely low-income with severe problems [EV-HOU-186].

**Immigrants.** *Provisional*: the immigration dossier owns the table (shared rule 3).

| Program | Rule for a family with citizen children and parents without status who file on ITINs |
| --- | --- |
| Housing (HOU-4A, 4D, 4.08) | Section 214: help prorated to eligible members, under the statute (shared rule 3). HUD's proposed rule would make proration temporary pending verification of every member [EV-HOU-402]; a HUD analysis of the draft found about 20,000 mixed-status families affected, 16,000 with children [EV-HOU-403] |
| Emergency fund (HOU-1D) | Not set (section 4 leaves it to the immigration table). As a new federal program it may fall under the 1996 welfare law's limits unless its statute says otherwise; the register does not show how the 2021-22 program handled this (evidence still needed) |
| Child benefit (FAM-1D, as introduced) | Allowed: the child and the taxpayer need a taxpayer identification number, not a Social Security number [EV-HOU-404]. Current law since 2025 requires a valid Social Security number [EV-HOU-405], so FAM-1D would restore these families |
| Health (HLT-1, HLT-4) | Children's coverage follows the health dossier; the parents' follows immigration |
| New statuses from legalization (IMM-1) | Tier B is barred from means-tested federal benefits for five years in the legacy design; a new status is not on Section 214's list unless the law adds it (shared rule 3) |

- **The gap, and the decision.** The same family was fully in the child benefit and partly or wholly out of housing. Espen decided to protect prorated help and repeal HUD's proposed rule, possibly in statute (`DEC-2026-11-09-10`). Section 4 now has the January 2029 executive action withdraw the rule, or rescind it if final, and the regular bill write proration and the right not to contend status into Section 214 (HOU-4.01), as this section recommended. **Verdict: closed by design, open until the regular bill passes.**
- **The conflict inside the plan, resolved.** Section 5 barred the shared household record from immigration enforcement use, while HUD's proposed rule would verify every member through DHS's SAVE system and report people found without status to DHS (as summarized by a law firm; the register has the rule's verification text only [EV-HOU-402]). Espen decided that the record collects only the basic information collected for everyone, where possible, and that the statute bars its use or sharing for immigration enforcement, with penalties (`DEC-2026-11-09-11`; HOU-4.02). That rule governs the record.
- *Checks owed:* the immigration dossier's single table across housing, the fund, health, FAM-1 and FAM-2 (section 4, check 4).

**People currently and chronically homeless.**
- *Housing:* stage 1 first; Housing First as federal law; supportive housing with a navigator duty on providers; Medicaid services offered.
- *With the rest:* Medicaid is the main funder of services (shared rule 7). If HLT-1 does not restore coverage, the 2027 Medicaid work requirements reach homeless adults, whom CMS does not treat as medically frail for homelessness alone [EV-HOU-336]. Then services fail where the vouchers land.
- *Gaps:* homeless families may not file taxes, so the child benefit needs the common application's enrollment offer to reach them (HOU-4.02). The services workforce is short (section 5, 2.6) [EV-HOU-338].
- *Race:* Black people are 32% of people homeless on a night, against 12% of the population [EV-HOU-413]. Stage 1 therefore reaches Black households heavily, which is where the need is.

**People with substance use disorders.**
- *Housing:* no treatment condition; voluntary recovery housing that accepts medicines (HOU-4.10); treatment access in supportive housing (HOU-4.11).
- *With the rest:* medicines and contingency management depend on Medicaid coverage and on HLT-4 including tenancy supports (HOU-4.12). Without HLT-1, the work requirements bite here too [EV-HOU-336].
- *Gaps:* the trials missed people with active addiction [EV-HOU-105]; HOU-4.10's evaluation is the plan's only answer.

**Older people.**
- *Housing:* nothing new for older renters who are not disabled. About 1.75 million older extremely low-income renter households had severe problems in 2023 [EV-HOU-186]. Espen will reconsider them once the care program is scoped (`DEC-2026-11-09-10`).
- *With the rest:* Social Security increases raise their rent if they are already assisted (3.1). Medicare's cap may shrink their medical deduction slightly.
- *The double-count risk.* Stage 3's age limit is undecided (section 6, question 2). If older disabled renters are in stage 3 and older non-disabled ones are not, the line between them will be drawn by a disability test, which many older renters can meet. That makes stage 3's count hard to bound.

**Disabled people.**
- *Housing:* stage 3 from 2038; accessible homes reserved from plan-financed buildings (HOU-3C.03). Chronically homeless people have disabilities by definition, so stage 1 reaches some disabled people from 2030.
- *With the rest:* stage 3 depends on HLT-4's home and community-based services. Medicaid attendant care paid by HLT-4 can shrink the attendant-care deduction (3.1).
- *Gaps:* an eight-year wait. About 1.16 million households with worst case needs include someone under 62 with a disability [EV-HOU-032], and none is in a funded stage until 2038 unless homeless or in a family with children.

### 3.5 Section 4's eight cross-dossier checks

| Check (section 4) | Status here | Who owes the rest |
| --- | --- | --- |
| 1. Rent offsets at 0 and 30 cents | Mechanism checked (3.1); not quantified | Secure floor, with the household model |
| 2. Deductions that shrink (child care, medical) | Statute read [EV-HOU-409]: both apply to vouchers [EV-HOU-410] | Care and health dossiers; HUD data on deduction use |
| 3. Stacked phase-outs | Worked example: about 75 cents before taxes (3.2) | Secure floor's ceiling |
| 4. One immigrant table | Gap found: child benefit and housing differ; HUD's proposed rule (3.4) | Immigration dossier |
| 5. Reach by race, place, disability, children's age | Section 4 of this file | Household model run with the plan's order |
| 6. Services in place | Risk named: Medicaid work requirements; workforce | Care and health dossiers |
| 7. Common application sharing income findings | Not checked; consent route stands (section 5) | Democratic renewal (CAP-13) |
| 8. Construction workforce | Not checked here; capital arithmetic (1.4) assumes no shortage | Immigration and work dossiers |

Also found here, not on section 4's list: **SNAP's response to lower rent** (2.5), which belongs on it.

## 4. Who it reaches

Memo 8 promised that this section would check who the order reaches by race, place and disability.

### 4.1 By race

| Group | Need | Who current help reaches | What the plan's order does |
| --- | --- | --- | --- |
| Black households | 10.1% of all Black households have worst case needs [EV-HOU-036]; 32% of people homeless [EV-HOU-413] | 48% of voucher households [EV-HOU-190]; 39.4% of Black very low-income renters report assistance [EV-HOU-034] | Stage 1 reaches them heavily. Landlord refusal falls hardest on them where it is legal [EV-HOU-093], so HOU-4.06's protection matters most here |
| Hispanic households | 11.5% of all Hispanic households have worst case needs [EV-HOU-036] | 22.1% of Hispanic very low-income renters report assistance [EV-HOU-034] | Stage 2 (families with children, severe problems, unassisted) should reach them well. Mixed-status proration and HUD's proposed rule cut against them [EV-HOU-402] |
| Asian households | 55.1% of Asian very low-income renters have worst case needs, the highest share [EV-HOU-034] | 20.6% report assistance [EV-HOU-034] | Stage 2 should reach them; language access in the common application matters (judgment) |
| White households | 4.3% of all White households [EV-HOU-036] | 30% of voucher households [EV-HOU-190] | Older white renters are a large share of the older group with no route (judgment; the register has no race split of older worst case needs) |
| American Indian and Alaska Native households | In tribal areas, physical problems and crowding far above the national rate [EV-HOU-406] | — | See tribal areas below |

- The Urban Institute finds full voucher funding cuts poverty most for Hispanic people (19%), then Black (15%) and white people (9%) [EV-HOU-393]. The plan reaches a part of that group, in an order that favors homeless and family households.
- The pandemic rental program reached Black and extremely low-income renters well above their share of the eligible [EV-HOU-085]. The emergency fund's one-administrator, need-formula design keeps that model.
- **Check owed:** the household model's run with the plan's order, by race of household head (2.2).

### 4.2 By place

| Place | What the plan does there | Risk |
| --- | --- | --- |
| Tight markets | Most homeless people are in the 50 largest cities and their suburbs [EV-HOU-414]; attached homes from 2032; neighborhood payment limits | Lease-up is worst [EV-HOU-092]; rent pass-through risk is highest (5.1); the 25% attached share is small |
| Loose markets | Tenant-based vouchers; lease-up easier | Fewer homeless people per award; supply money has the least to do |
| Rural areas | Same vouchers; HUD's definition of homelessness misses doubling up, which section 4 counts | Search success is lower at rural agencies [EV-HOU-395] [EV-HOU-396]; small agencies; the register has no rural share of new awards |
| Tribal lands | Dedicated set-asides through tribes, by the block grant formula, in the form each tribe's plan chooses: proposed 3% of the emergency fund, 3% of new-award money and 5% of the revolving-fund grants (HOU-4.13, `DEC-2026-11-09-10`) | Tribal housing problems are physical condition and crowding (23% and 16%, against 5% and 2% nationally), with 42,000-85,000 homeless people living doubled up [EV-HOU-406]. Vouchers buy rent, not repair or new homes; the grant share and the tribes' freedom to use award money for homes now reach that, at a scale not yet tested against need |

- **The tribal gap was the largest place gap; the design now addresses it.** Espen decided on dedicated tribal policy and investment, with set-asides, respecting sovereignty and self-determination (`DEC-2026-11-09-10`). Section 4's HOU-4.13 sets aside shares of the emergency fund, the new awards and the revolving-fund grants (about $13 billion over FY2030-39 at the proposed shares; section 6, 2.6), paid through tribes by the block grant formula. The ERA precedent gave tribes about 3% of its first round (section 5, question 2). **Verdict: the gap is narrowed; whether the shares are enough is unknown.** At $150,000-300,000 of gap subsidy a home (1.4), the grant share's $3.6 billion would repair or build roughly 12,000-24,000 homes, against overcrowding in 16% of tribal-area households [EV-HOU-406] (this section's arithmetic). HOU-4.13's proposed need report is the test.
- **Rural:** the register cannot say how many awards reach rural places. **Ask of section 5:** report awards, issuances and leases by rural and urban county, monthly, from the shared record.

### 4.3 By disability

- Stage 1 reaches chronically homeless people, who have a disability by definition.
- Stage 2 reaches disabled members of poor families with children.
- Everyone else with a disability waits for stage 3 in 2038: about 1.16 million households under 62 with worst case needs include a disabled person [EV-HOU-032], and section 6 counts about 0.6 million in stage 3 (section 6, 2.1). Older disabled renters are unpriced.
- Accessible homes come only from plan-financed buildings, at turnover, from 2038 (HOU-3C.03). On the capital arithmetic (1.4), that is a small stock.

## 5. Objections answered

Each objection is put as strongly as its best advocate would put it. The answer says what the evidence supports, what the plan does about it, and what remains.

### 5.1 "Vouchers raise rents, so landlords capture the money"

*The objection.* Susin found that vouchers raised rents for unsubsidized poor households by 16%, so low-income non-recipients paid $8.2 billion more while recipients got $5.8 billion [EV-HOU-397]. France's housing allowance went 78% to landlords [EV-HOU-156]. More generous vouchers mostly raise rents [EV-HOU-095]. The plan roughly doubles the voucher program by the 2040s.

*The answer.*
- The best later study finds no rise in overall rents from more vouchers, with price rises concentrated on units near the voucher ceiling in cities where supply cannot respond [EV-HOU-096]. Susin's estimate is on 1974-93 data and is contested. Both views stand: the effect is real where supply is fixed and small where it is not.
- The plan's design leans against it: neighborhood payment limits rather than metro-wide generosity [EV-HOU-095]; attached homes in tight markets, built or bought with the plan's capital (HOU-4.04); the zoning reward; and a phase-in of 250,000 a year rather than a single jump.
- **Two parts of the plan push the other way.** Section 5's payment standards up to 120% where lease-up is low, and the right in 2037, which removes the cap on demand. Both are in the tightest markets.
- *What remains.* An early-warning signal (section 6 below): rent growth for units near the payment standard against other units, in tight markets, published yearly. **Ask of section 4:** a statutory trigger that raises the attached share above 25% where that gap widens.

### 5.2 "Subsidized building just replaces private building"

*The objection.* Nearly all tax-credit building may be offset by less private building [EV-HOU-115]; one subsidized home adds a third to a half of a home [EV-HOU-114].

*The answer.* The plan is a rental help plan first (1.4), and its tenant-based vouchers are the tool the crowd-out research favors for reaching people who would otherwise lack a home [EV-HOU-114]. The capital money is weighted to acquisition, preservation and deep affordability, where crowd-out is less of an issue: a preserved home keeps its tenants whether or not it adds to the stock. Crowd-out is smaller in dense places [EV-HOU-277] and in declining neighborhoods [EV-HOU-284], and the credits Espen chose (option D, `DEC-2026-11-09-08`) aim the new middle-income and neighborhood credits there, as five-year trials with evaluations (HOU-2D.02, .03). The low-income increase is not targeted that way, so most of its crowd-out remains [EV-HOU-275]. *What remains:* the production target's number is proposed, not yet set (HOU-3C.04), and the credits are unscored.

### 5.3 "It costs too much"

*The objection.* About $0.63 trillion over ten years, permanent claims of about $81 billion a year by FY2040 before stage 2's wider entry, and a high case well above the central at maturity (section 6).

*The answer.* At about 0.16% of GDP in FY2040 (section 6), the plan stays inside the range that rich countries spend on housing allowances, where the United States sits at 0.1-0.3% of GDP and the United Kingdom at 1.4% [EV-HOU-159]. CBO priced vouchers for every household under 30% of area median income at $290 billion over 2016-25 in 2015 [EV-HOU-390]; Urban puts full funding at $118 billion a year more [EV-HOU-392]. The plan does part of that and phases it. The strongest evidence on cost-effectiveness is for exactly the plan's first groups [EV-HOU-086] [EV-HOU-102]. *What remains:* the 2037 right's cost is set by take-up and rents, not by Congress (section 6, 2.5); the 2040 gap below.

### 5.4 "The fiscal rule fails in 2040"

*The objection.* Section 6 finds FY2040 short by about $12 billion on permanent lines, $19 billion with the capital tail, before stage 2's wider entry (roughly $7-12 billion more), and the high case fails FY2040 and FY2041.

*The answer.* The gap is real and housing should own it. It comes from stage 3, the standing fund, stage 2 at its true timing and its wider entry for families with no home of their own, and the duty to house, all permanent claims Espen chose, and from capital still being spent after 2039. Espen decided both fixes (`DEC-2026-11-09-09`): the permanent gap goes to the financing settlement, without trimming housing yet, and the last capital is awarded earlier, which halves the capital tail; slight FY2040 overshoots are acceptable at this stage of design. **This section adds one:** the lease-up risk (1.2) means the central case may overstate FY2040 cost, but that is not money to spend. The plan should not count a reach shortfall as fiscal room. *What remains:* the D4 cautious reading is not computed (2.3), and housing's high case fails. The Byrd rule's per-bill test for R2's permanent lines (section 6, 3.3) is unbuilt and could force sunsets.

### 5.5 "States will refuse, and the federal government cannot make them"

*The objection.* The anticommandeering rule bars the federal government from ordering states to run its programs; states create housing agencies and can limit them; some states already block local source-of-income laws.

*The answer.* The plan does not depend on states for its core.
- The awards go to housing agencies, with a backstop administrator where an agency declines (section 5, 5).
- The revolving funds and emergency fund pass to cities, counties, nonprofits or direct federal loans where a state refuses (section 5, 5).
- The source-of-income protection is a federal civil rights floor in the Fair Housing Act (HOU-4.06), and state laws that protect more stay [EV-HOU-247].
- The zoning reward and the transportation condition stay inside the coercion limit by applying only to new money (HOU-6.02).

*What remains.* A state could still slow the plan by restricting its own agencies (judgment), and Medicaid, which decides whether services reach supportive housing, is a state program. That is the HOU-4.12 backstop's job, and section 5's question 3.

### 5.6 "Landlords won't take vouchers"

*The objection.* Landlords refused voucher holders in most tests in three of five metros [EV-HOU-093]; participating landlords fell while vouchers rose (section 5, 2.3).

*The answer.* Where state or local law barred refusal, few refused [EV-HOU-093]; source-of-income laws reduced neighborhood poverty for voucher holders, with mixed effects on lease-up [EV-HOU-094]. The plan adds the national protection, mandatory testing money for 2030-34 (adopted, `DEC-2026-11-09-10`; HOU-4.06), payment within 30 days, a damage fund, quick inspections and search help [EV-HOU-091]. *What remains:* lease-up (1.2) is where this objection would show, and it is the plan's weakest number.

### 5.7 "Housing help discourages work"

*The objection.* Voucher use cut participation by 4 points and earnings by 10% in Chicago [EV-HOU-088]; the stacked rate is about 75 cents (3.2).

*The answer.* The effects are modest and the alternatives tested do no better: a rent rule built to reward work did not raise earnings over six years [EV-HOU-400], and homeless families with vouchers saw no change in average earnings [EV-HOU-086]. The plan's first groups are homeless households and families with young children, where stability comes before work. The plan adds no new phase-out and no work condition (shared rule 6). *What remains:* the ceiling on the combined rate belongs to the secure floor (3.2).

### 5.8 "It doesn't go far enough"

*The objection, from the left.* By the early 2040s the plan houses about 2.4 million more households (about 0.9 million from the million awards, 0.9 million in stage 2 and 0.5 million in stage 3; section 6), while 8.46 million had worst case needs in 2023 [EV-HOU-020] and 5.8 million extremely low-income households had severe problems [EV-HOU-186]. Single adults, older renters and families just above the line wait indefinitely. Vienna houses 43% of its people in social housing [EV-HOU-163]; the OECD average is 7% of the stock [EV-HOU-161]; the plan's social housing is a $10 billion pilot. A universal voucher would cut child poverty by about a quarter [EV-HOU-393]; the plan's million cuts it by about 0.2 points in the model (2.2).

*The answer.* The objection is right about the scale and the plan says so: it sequences help to the groups with the strongest evidence and pays for each permanent claim from FY2040 (D4). Its design can grow: each stage is written so a later Congress can open the next by statute, and the social housing pilot and the small builder are written to be scaled on their results (memo 3). *What remains for Espen:* whether to state now the route and date for the households with no funded stage (single adults and families just above the line), even if unfunded, so the guarantee's promise is visible. Older non-disabled renters are to be reconsidered once the care program is scoped (`DEC-2026-11-09-10`). A question at the end.

### 5.9 "Social housing should be the core, not a pilot"

*The objection.* Public and nonprofit ownership keeps homes affordable for good, does not leak subsidy to landlords [EV-HOU-156] and builds a stock the market will not.

*The answer.* The register has no independent evaluation of a U.S. public developer (memo 3), Vienna's model rests on a century of land and finance institutions [EV-HOU-162] [EV-HOU-165], and the plan's permanent-affordability rule (HOU-3C.03) already applies the core of the idea to every home it finances. *What remains:* the pilot's size ($10 billion, section 6) means its evaluation will say little by the 2030s. If Espen wants social housing to be a real test, the pilot needs a target and an evaluation date (a question at the end).

## 6. What would make the plan fail, and the early-warning signals

| Failure | How it would happen | Signal | Threshold (judgment) | Outcome |
| --- | --- | --- | --- | --- |
| Awards that are not used | Lease-up far below 90% (1.2) | Share of awards leased 12 and 18 months after issue, by agency and market type | Below 70% at 18 months nationally, or below 50% at any agency of 500+ awards | OUT-04 |
| A right on paper only | Stage 2 families whose searches fail after 2037 | Share of eligible applicants housed within six months; expired vouchers among entitled families | More than 20% of entitled families unhoused after six months | OUT-04, OUT-01 |
| Stage 1 out of balance | Doubled-up families take most of stage 1, or single homeless adults wait for years (1.5) | Stage 1's yearly published counts by group (`DEC-2026-11-09-12`) | An imbalance two years running triggers a review, not a restriction (`DEC-2026-11-09-12`) | OUT-01, OUT-04 |
| Rents rise with the vouchers | Payment standards and the right push up rents near the ceiling in tight markets (5.1) | Rent growth for units near the payment standard against other units, tight markets | Gap above 2 points a year for two years | OUT-04 |
| The fund pays the wrong people | Risk screen too broad (1.6) | Share of paid households with a filing or court date; shelter entry after payment, from the linked records | Fewer than half with a filing or notice | OUT-04, OUT-02 |
| Services never arrive | Medicaid gaps and workforce shortages (3.4) | Supportive-housing tenants without a navigator; unfilled posts | More than 10% without a navigator after 90 days | OUT-04 |
| Mixed-status families pushed out | HUD's rule final; no statutory fix (3.4) | Mixed-status households in assisted housing, yearly | Any fall after 2029 | OUT-01 |
| A slow or hostile HUD | Staff cuts, missed deadlines (section 5, 8) | Statutory deadlines missed; payments over 30 days late | Any deadline missed by 90 days | All |
| The fiscal gap grows | Take-up, rents and stage 3's count above central (section 6) | Housing's FY2040 path on each new estimate | Above section 6's central by more than $10 billion | D4 |
| Capital does not become homes | States slow; costs above $400,000 a home (1.4) | Homes financed, preserved and added net, by place and income band | Below the yearly path to HOU-3C.04's target | OUT-04 |
| Tribal and rural places left out | Vouchers that cannot be used there; set-asides too small for the need (4.2) | Awards and leases per eligible household, rural and tribal against urban; homes repaired or built with tribal set-asides | Rural lease rate more than 10 points below urban; tribal set-asides unspent after three years | OUT-04 |

Most of these signals come from the shared household record (HOU-4.02; section 5, 4), which section 5 makes public monthly by statute. That record is the plan's most important early-warning tool, and its data system is the one piece that must be built in 2029 whatever else slips.

## 7. What holds up

- **Targeting.** The first two stages are the groups with the strongest evidence of benefit: homeless families and people [EV-HOU-086] [EV-HOU-099] [EV-HOU-408], and poor children who move young [EV-HOU-090].
- **The cost per household,** within its range (1.1).
- **Take-up,** within its range (1.3).
- **The child benefit's interaction** with rent (3.1).
- **The delivery design's answers** to the 2021-22 rental program's failures: one administrator per place, rules before money, self-attestation with landlord checks, error measurement from year one (section 5, 9).
- **The guardrails** (section 6, 3.3).
- **Federalism:** no core program depends on a willing state (5.5).

## Changes this section asks of sections 4-6

For their owners; none is made here. Items that change what the plan commits to are also questions for Espen below.

| Section | Change | Why |
| --- | --- | --- |
| 4 (HOU-4.03) | Define "without a home" for stage 1 and decide where doubled-up families go | Stage 1's size is unbounded (1.5). Decided: `DEC-2026-11-09-12` |
| 4 (HOU-4D.01) | ~~Under the right, a failed search triggers an attached home, a reissued voucher with search help, or a higher payment standard, by deadline~~ Met: the duty to house (`DEC-2026-11-09-10`) | A right that ends with an expired voucher (1.2) |
| 4 (HOU-3C, HOU-8, HOU-9A) | ~~A published target for homes financed, preserved and added net, reported by place and income band~~ Met: HOU-3C.04, three numbers (`DEC-2026-11-09-10`); the numbers are proposed, for Espen | No production target (1.4) |
| 4 (HOU-1D.02) | Randomize at the margin of each grantee's risk screen in its first year | The fund's value is unmeasured without it (1.6) |
| 4 (HOU-4.04) | A trigger that raises the attached share where rents near the payment standard rise faster | Rent pass-through (5.1) |
| 4 (interactions) | Add SNAP's response to lower rent to the cross-dossier checks | Missing check (2.5) |
| 4 (HOU-4.01) | Note that the voucher rent rule uses the same adjusted income as 1437a (closing the shared-rules open check) [EV-HOU-410] | Settled here |
| 5 | Monthly reporting of awards and leases by rural and urban county, and for tribal areas | Reach by place is invisible (4.2) |
| 5 | ~~State which rule governs the shared record if HUD's verification rule requires reporting to DHS~~ Met: the statutory enforcement bar governs (`DEC-2026-11-09-11`; HOU-4.02) | Conflict (3.4) |
| 6 | ~~Add a 75% leased reading, reported as reach lost, not as saving~~ Met at section 6's head (1.4) | Lease-up (1.2) |
| 6 | Report stage 2 families' cost per award separately when the data exist | Cost per award (1.1) |
| 6 | Add the count risk (doubled-up families forming households) to the high case | Take-up (1.3) |
| 6 | Count SNAP's response to lower rent, as CBO would | Missing offset (2.5) |
| `shared-rules.md` | Close the open check on 1437f(o); add the child care and medical deductions to rule 1 | Settled here [EV-HOU-409] [EV-HOU-410] |

**Owed by other dossiers** (section 4's checks, with this section's findings): secure floor, the rent offsets and the combined phase-out ceiling (3.1, 3.2); care, the child care deduction and FAM-2's possible cliff at 75% of state median income (3.3); health, Medicaid coverage for homeless adults and tenancy services in HLT-4 (3.4); immigration, the single table, including the emergency fund and HUD's proposed rule (3.4); democratic renewal, the common application (check 7); household model, a run with the plan's order and stage 2 (2.2).

## Questions for Espen

Each is yes or no; none is adopted until you answer. Espen decided questions 1 to 6 on November 9 (`DEC-2026-11-09-10` to `-12`) and part of question 7; they are marked, and stay here so the reasoning can be traced.

1. **Should stage 1 count families doubled up because of economic hardship as "without a home"?** If yes, stage 1 may take all million awards and delay stage 2; if no, those families wait for stage 2 when they have children. Recommendation: count them in stage 1 only when they have children, and report the count before the 2032 awards (judgment). **Decided (`DEC-2026-11-09-12`): yes for families with children, by one plain test with no cap;** an imbalance two years running triggers a review, not a restriction.
2. **Should the plan publish a target for homes financed, preserved and added net?** The capital is small next to the shortage, and without a target nobody can check it. Recommendation: yes. **Decided: yes** (`DEC-2026-11-09-10`; HOU-3C.04, the number proposed, for Espen).
3. **Should the regular bill write mixed-status proration, and the right not to contend status, into Section 214, and should the 2029 executive action withdraw HUD's February 2026 proposed rule if it is final?** Families with citizen children would otherwise be in the child benefit and out of housing. Recommendation: yes, with the immigration dossier deciding the wider table. **Decided: yes; protect prorated help and repeal the proposed rule, possibly in statute** (`DEC-2026-11-09-10`; HOU-4.01).
4. **Should the shared household record bar immigration enforcement use even where HUD's verification uses DHS's system?** Section 5's rule and HUD's proposed rule conflict. Recommendation: verification only, no reporting from the record, written into the regular bill (judgment). **Decided: the record collects only the basic information collected for everyone, where possible, and the statute bars its use or sharing for immigration enforcement, with penalties** (`DEC-2026-11-09-11`; HOU-4.02).
5. **Should the right from 2037 include a duty to house a family whose voucher search fails** (an attached home, a reissued voucher or a higher payment standard, by deadline)? Recommendation: yes. **Decided: yes; the duty includes helping the family find a home** (`DEC-2026-11-09-10`; HOU-4D.01, item 5).
6. **Should the plan add a tribal construction and repair line,** or a tribal set-aside in the revolving funds through the Native American housing block grant? Vouchers do little where the problem is condition and crowding. Recommendation: yes, a set-aside in HOU-3C.01 sized from need data, which is section 5's question 2 extended to capital. **Decided: yes, as dedicated tribal policy and investment with set-asides that respect sovereignty and self-determination** (`DEC-2026-11-09-10`; HOU-4.13, sizes proposed, for Espen).
7. **Should the plan state a route and date for the households with no funded stage** (older non-disabled renters, single adults, families just above the line), even if unfunded? Recommendation: yes, as a stated next stage for the 2040s, so the guarantee's limits are visible. **Partly decided:** older non-disabled renters are reconsidered once the care program is scoped (`DEC-2026-11-09-10`); single adults and families just above the line are still open.
8. **Should the social housing pilot have a size target and an evaluation date,** so it can inform a scale-up decision? Recommendation: yes.
9. **Should voucher rent ignore the value of free or capped child care,** so the care plan does not raise rent? This is a shared rule (the secure floor and care dossiers own it); housing's recommendation is yes, priced by section 6.

## Evidence still needed

- A count of families doubled up for economic hardship, by children and income (Education Department homeless student data; American Community Survey tabulations).
- HUD tabulation of voucher subsidy by household type and of families taking the child care and medical deductions.
- How the 2021-22 Emergency Rental Assistance program applied the 1996 welfare law's immigrant limits (Treasury guidance).
- HUD's own estimate of mixed-status households affected by the February 2026 proposed rule, from its regulatory analysis.
- Rural and tribal shares of voucher issuance and lease-up from HUD's records, and the use of vouchers on tribal lands.
- The share of homelessness by race in rural and tribal areas.
- Evidence on rent pass-through from a recent large voucher expansion, such as Emergency Housing Vouchers by market.
- Development costs per home nationally (a national tax-credit cost series), to replace this section's state examples.
