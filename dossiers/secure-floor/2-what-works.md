# A secure floor for every household: what works

Role: section 2 of the secure floor dossier. It covers the research, the programs at home and abroad and the failures to avoid, behind S3's design choices. It runs part by part, as in section 1: the child benefit (A), income support and participation help, with how government delivers and what the future economy demands (B), paid leave (C), Social Security (D), and coordinating phase-outs (E). Status: draft (stage D, board row S2). Every figure cites the evidence register (`evidence.json`). Each claim that may carry a recommendation names its evidence strength (randomized trial, quasi-experimental, program evaluation, international practice, simulation or judgment) and where it was tried. The legacy designs are working choices, weighed as options, not settled (`DEC-2026-10-30-02`).

## In brief

- **Cash for children cuts child poverty quickly; the employment effect is contested.**
  - In 2021 the expanded monthly credit took SPM child poverty to 5.2%, the lowest on record [EV-SEC-202]. Census credits the expansion alone with 2.1 million children [EV-SEC-204]. Food insufficiency fell about a quarter after the first payment (quasi-experimental) [EV-SEC-209].
  - Studies of the six months of payments find no detectable effect on parents' work [EV-SEC-212] [EV-SEC-213].
  - Simulations of a permanent credit predict 367,000 to 1.5 million parents leaving work [EV-SEC-219] [EV-SEC-218]. One careful study finds a drop among less-educated unmarried mothers [EV-SEC-217].
  - Both sides are presented in part A. Neither can test a permanent program.
- **Canada shows it works at scale and lasts.** An income-tested child benefit paid monthly from the tax return took child poverty from 16.3% in 2015 to 10.7% in 2023 [EV-SEC-240]. One study finds no labor supply response [EV-SEC-241].
- **How a benefit is delivered decides who gets it.**
  - Randomized trials show that simpler letters and help raise take-up [EV-SEC-102] [EV-SEC-103]. Default enrollment matters most [EV-SEC-101] [EV-CAR-206].
  - Closing SSA field offices cut disability recipients nearby by 16% [EV-SEC-106].
  - The 2021 credit reached about 61 million children, nearly 9 in 10 families by automatic deposit [EV-SEC-107] [EV-SEC-108], because the IRS paid from returns it already held.
- **State paid leave raises leave-taking, and its long-run effect on mothers' careers is contested.**
  - California's program doubled mothers' leave and raised fathers' leave by 46% (quasi-experimental) [EV-SEC-355] [EV-SEC-362].
  - The best tax-record study finds no long-run gain, and some harm, for first-time mothers [EV-SEC-357].
  - Employers report few problems [EV-SEC-363] [EV-SEC-364]. Infant and older-adult health improve [EV-SEC-366] [EV-SEC-368].
  - Washington shows how a capped contribution can fall behind claims [EV-SEC-327] [EV-SEC-329].
- **Social Security is the best evidence for a universal floor.** It explains the whole fall in elderly poverty from 1967 to 2000 (quasi-experimental) [EV-SEC-442] [EV-SEC-443]. It costs under 1% of its spending to run [EV-SEC-115], and it is trusted across parties [EV-SEC-116]. Every solvency bill in the register needs new revenue, and none has a current actuarial score [EV-SEC-477].
- **Smoothing phase-outs changes behavior less than expected.** A randomized trial of a gentler disability-benefit offset raised the share earning above the line but not average earnings [EV-SEC-546]. Coordination works mainly by being simpler for families, not by producing more work.

## Part A. The child benefit

### A.1 The 2021 expanded credit: poverty and hardship

**Design.** ARPA section 9611 paid $3,000 a child, $3,600 under 6. The credit was fully refundable, included 17-year-olds and phased out above $150,000 for couples [EV-SEC-200]. Half was paid in advance from July to December 2021 [EV-SEC-201]. It lasted one year.

| Finding | Evidence strength; where | Evidence |
| --- | --- | --- |
| SPM child poverty fell from 9.7% (2020) to 5.2% (2021), the lowest on record, and rose to 12.4% in 2022 | Official data; national | [EV-SEC-202] [EV-SEC-205] |
| The credit lifted 2.9 million children out of poverty; the expansion alone 2.1 million, without which the rate would have been 8.1% | Census accounting, no behavior (analysis); national | [EV-SEC-203] [EV-SEC-204] |
| The 2022 rise came largely from the end of the stimulus payments and tax credits together, not the credit alone | Census accounting | [EV-SEC-206] |
| Monthly child poverty rose from 12.1% to 17% the month after the last payment, 3.7 million more children | Simulation, Columbia CPSP (authors favor the credit) | [EV-SEC-208] |
| Food insufficiency fell about 26% after the first payment (16.4% in a second model) | Quasi-experimental, Census Pulse survey | [EV-SEC-209] |
| Monthly payments cut food insufficiency 2.4 points (19%); the lump sum did not, but reduced housing arrears | Quasi-experimental, Pulse | [EV-SEC-210] |
| Fewer hardships, especially food, among low-income families | Quasi-experimental | [EV-SEC-211] |

- **Caveat.** BLS corrected the SPM thresholds in July 2026, lowering the overall rates for 2019-24 by 0.1 to 0.3 points [EV-SEC-207]. The corrected child series was not available, so the 5.2% and 12.4% figures stand as first published.
- **What it shows.** A large, monthly, fully refundable credit cuts child poverty fast. The monthly form mattered for food: that is the only head-to-head evidence on payment timing [EV-SEC-210].

### A.2 The employment debate, both sides

| Side | Study | Design; where | Finding | Evidence |
| --- | --- | --- | --- | --- |
| No detectable effect | Ananat, Glasner, Hamilton and Parolin | Difference-in-differences, CPS and Pulse, April-December 2021 | Very small, inconsistently signed, insignificant | [EV-SEC-212] |
| No detectable effect | Enriquez, Jones and Tedeschi | CPS, by size of income gain | No strong evidence of a change | [EV-SEC-213] |
| No detectable effect | Pilkauskas and others | Very-low-income families | No impact on labor supply | [EV-SEC-214] |
| Small or subgroup | Pac and Berger | Caregivers against childless adults | A decline of 344,000 to 495,000, not significant | [EV-SEC-215] |
| Small or subgroup | Schanzenbach and Strain | CPS | No effect in broad groups; 4.5 points lower for unmarried women with some college or less (a subgroup chosen after the fact) | [EV-SEC-216] [EV-SEC-217] |
| Predicted loss | Corinth, Meyer, Stadnicki and Wu | Simulation with literature elasticities | 1.5 million workers (2.6% of working parents) leave work; child poverty falls at most 22%, not 34% | [EV-SEC-218] |
| Predicted loss | Bastian | Simulation | 367,000 parents stop working; child poverty down 28%, deep poverty 49% | [EV-SEC-219] |
| Predicted loss | Strauss and others | Structural model on PSID data | Employment about 1 point lower | [EV-SEC-223] |
| The design question | Goldin and others | Quasi-experimental, California tax records | Removing a credit's work requirement caused very few mothers to leave work | [EV-SEC-224] |

- **The dispute.** AEI's Winship argues Bastian's own numbers imply far more single mothers leaving work [EV-SEC-220]. Corinth and Meyer argue the observed studies are too short and imprecise to rule out large effects [EV-SEC-221]. The Niskanen Center argues the Corinth estimate is an outlier against earlier work [EV-SEC-222].
- **How to weigh it.**
  - The observed studies are the stronger design, but they cover a temporary, pandemic-year credit of six months, which people knew would lapse. They cannot rule out an effect from a permanent one.
  - The simulations answer the right question, but they rest on elasticities from the 1990s welfare and earned income credit reforms. Those are themselves contested (A.6).
  - The California study is the closest quasi-experimental test of what a work requirement buys. It finds almost nothing [EV-SEC-224].
  - The fair reading: a permanent, fully refundable credit would probably reduce work a little, with estimates from near zero to about 2.6% of working parents. It would cut child poverty by a quarter to a third even after that response [EV-SEC-218] [EV-SEC-219].
- **The legacy model's treatment.** It credits no employment response (`legacy-research.md`, 1.10), and the legacy ledger's labor-supply sensitivity is −$0.12 to −$0.02 trillion (`legacy-research.md`, 1.9). S3 should show results with and without the range above.

### A.3 Cash and children's development: the trials

| Study | Design; where | Finding | Evidence |
| --- | --- | --- | --- |
| Baby's First Years | Randomized trial, four U.S. cities; $333 a month against $20 | No significant effect on four preregistered child outcomes at age 4 | [EV-SEC-227] |
| Baby's First Years, age 1 | Same trial, brain activity (n = 435) | More high-frequency brain activity, sensitive to specification | [EV-SEC-228] |
| OpenResearch | Randomized trial, two states; $1,000 a month to adults for three years | Earnings fell about $1,900 a year; participation fell 4.2 points | [EV-SEC-230] |
| Rx Kids, Flint | Quasi-experimental (difference-in-differences); every expectant mother paid in pregnancy and infancy | Preterm births 2.7 points and low birthweight 4.2 points lower than in matched cities | [EV-SEC-231] |
| Food stamps rollout, 1961-75 | Quasi-experimental, U.S. counties | Better adult health, and economic self-sufficiency for women | [EV-SEC-232] |
| Mothers' Pensions, 1911-35 | Quasi-experimental | Sons lived a year longer, with more schooling and income | [EV-SEC-233] |
| National Academies, 2019 | Synthesis | Child poverty costs $800 billion to $1.1 trillion a year; two packages, one with a $225-a-month child allowance, halve child poverty at $90.7 billion and $108.8 billion a year | [EV-SEC-225] [EV-SEC-226] |

- **How to read them.** The best-designed recent trial, Baby's First Years, found no developmental effect at age 4 from a modest monthly payment [EV-SEC-227]. That is a real finding against claims of quick developmental gains. AEI reads it as favoring work-linked aid [EV-SEC-229]. The historical studies find long-run gains from income in childhood [EV-SEC-232] [EV-SEC-233], as do the earned income credit studies (A.6), and Rx Kids finds birth-outcome gains in one city [EV-SEC-231]. OpenResearch's adult transfer was three times a child benefit and went to adults, not parents, so it bounds rather than measures a child benefit's work effect [EV-SEC-230].
- **For the design.** The strongest case for a child benefit is its direct effect on poverty and hardship (A.1). The case for long-run development is plausible from history but not settled by current trials.

### A.4 Canada's child benefit

- **Design.** Since July 2016 Canada has paid up to $8,157 a year for each child under 6 and $6,883 for each child 6 to 17 (from July 2026) [EV-SEC-234].
  - It is reduced by 7%, 13.5%, 19% or 23% of family net income between $38,237 and $82,847, by number of children, and at lower rates above that [EV-SEC-234] [EV-SEC-235] [EV-SEC-557].
  - It is tax-free, monthly, indexed and paid on the prior year's tax return: about 3.5 million families received $26.3 billion [EV-SEC-236] [EV-SEC-237] [EV-SEC-558].
  - Parents can apply at their child's birth registration, with consent [EV-SEC-113].
- **Results.**
  - The government reports child poverty fell from 16.3% in 2015 to 10.7% in 2023 [EV-SEC-240]. On the older measure, the rate reached 4.7% in 2020 with pandemic aid and rose back to 10.7% by 2023 [EV-SEC-238]; on the new 2023-base measure, 11.5% in 2024 [EV-SEC-239]. The two measures are not comparable.
  - Baker, Messacar and Stabile find the child benefit cut child poverty more than the benefit it replaced, with no labor supply response (quasi-experimental, single mothers against childless women) [EV-SEC-241]. They warn that their two data sources disagree on the size of the effect [EV-SEC-242].
- **What it shows.**
  - An income-tested benefit with no earnings phase-in can cut child poverty a lot and keep it lower. The rate falls fastest at the bottom, where the U.S. credit pays least.
  - Its phase-out rates are part of the stack Canada families face (part E).
  - Its gains erode when other aid ends and prices rise. Indexing protects the benefit, not the poverty line.

### A.5 The UK's two-child limit

The UK removed its two-child limit on child benefits from April 2026, by an act passed in March [EV-SEC-243]. The government expects 450,000 fewer children in relative poverty by 2030 [EV-SEC-244] [EV-SEC-245]. The IFS put the effect at 540,000 children over the absolute line at £2.5 billion a year, but found the benefit cap blocks the gain for 70,000 of the poorest households [EV-SEC-246]. The lesson for the design is that a ceiling elsewhere in the system can cancel a child benefit for the poorest families. These are projections (international practice).

### A.6 The earned income credit literature, both sides

| Side | Study | Design; where | Finding | Evidence |
| --- | --- | --- | --- | --- |
| Raises work | Eissa and Liebman | Quasi-experimental, 1986 expansion | Single mothers' participation up to 2.8 points | [EV-SEC-247] |
| Raises work | Meyer and Rosenbaum | Quasi-experimental, 1984-96 | A large share of the rise in single mothers' work | [EV-SEC-248] |
| Raises work | Schanzenbach and Strain | Quasi-experimental, every expansion since 1975 | Each $1,000 of maximum credit adds 3.0 to 3.3 points of employment for unmarried mothers | [EV-SEC-253] |
| Does not | Kleven | Quasi-experimental, about 500 event studies | No robust effect apart from 1993, which coincided with welfare reform | [EV-SEC-252] |
| Poverty | Hoynes and Patel | Quasi-experimental | $1,000 more cuts single-mother poverty 8.4 points | [EV-SEC-249] |
| Children | Hoynes, Miller and Simon | Quasi-experimental | $1,000 more cuts low birth weight 2-3% | [EV-SEC-250] |
| Children | Bastian and Michelmore | Quasi-experimental | $1,000 more at ages 13-18 raises college by 4.2% and later earnings | [EV-SEC-251] |
| Childless workers | Paycheck Plus, New York | Randomized trial, about 6,000 adults | Employment up 2.6 and 2.1 points in years 2 and 3 | [EV-SEC-254] |
| Childless workers | Paycheck Plus, Atlanta | Randomized trial, about 4,000 adults | No employment effect | [EV-SEC-255] |

- **How to weigh it.** The earned income credit's poverty and child-outcome effects are well established. Its employment effect, long the main argument for tying aid to work, is now genuinely contested [EV-SEC-252] [EV-SEC-253], and the two trials of a larger childless credit split [EV-SEC-254] [EV-SEC-255]. This matters twice: it bounds how much work a phase-in buys, and the same elasticities drive the simulated losses in A.2.
- **2021's childless expansion** tripled the maximum credit to $1,502 and lowered the age to 19 for one year [EV-SEC-256]. 4.3 million young workers received almost $900 on average [EV-SEC-257].
- **Errors.** The IRS estimates 32.7% of earned income credit payments in fiscal 2025 were improper ($21.1 billion), against 13.6% for the refundable child credit [EV-SEC-258]. The estimate counts honest errors, mostly about which child qualifies, as well as fraud. Simpler eligibility rules are the main remedy.

### A.7 The bills, compared

| Bill | Design | Cost and status | Matches the legacy FAM-1D? | Evidence |
| --- | --- | --- | --- | --- |
| Current law (P.L. 119-21) | $2,200, indexed; $1,700 refundable after a 15% phase-in; SSN rules | Enacted, permanent | Baseline | [EV-SEC-259] |
| American Family Act (H.R. 2763, S. 1393, April 2025) | $300 a month for 6-17, $360 under 6, $2,400 in the first month; fully refundable; phased out above $150,000 (couples), with a second reduction above $400,000; indexed; a taxpayer identification number for the child, no parent SSN rule | TPC about $1.4 trillion over FY2026-35; PolicyEngine $2.5 trillion over 2025-34 against an older baseline; Columbia: child poverty 13.3% to 8.8%; referred to committee | It is FAM-1D | [EV-SEC-260] to [EV-SEC-268] |
| 2021 credit (ARPA) | $3,600 under 6, $3,000 6-17, fully refundable, monthly | Expired | It is FAM-1A | [EV-SEC-200] |
| Tax Relief for American Families and Workers Act (H.R. 7024, Wyden-Smith, 2024) | Refundable portion raised in steps to $2,000 per child by 2025, with the phase-in kept | Passed the House 357-70; failed cloture in the Senate with 48 votes; CBO about $33 billion | Bipartisan; far smaller, keeps the earnings test | [EV-SEC-269] [EV-SEC-270] [EV-SEC-271] [EV-SEC-272] |
| Romney's Family Security Act (2021) | $350 a month under 6 and $250 6-17, paid by SSA; funded by ending other credits | Penn Wharton: $283 billion over the window before SNAP and TANF changes; not introduced as a bill | Similar amounts; differs on delivery (SSA, not the IRS) and on funding by consolidation | [EV-SEC-273] [EV-SEC-274] |
| Family Security Act 2.0 (2022) | The same amounts, a full benefit only with $10,000 of earnings, plus prenatal payments | Proposal | Adds an earnings floor, which the legacy design does not | [EV-SEC-275] |

- **Where the legacy choice sits.** FAM-1D matches the American Family Act's amounts and structure. It differs from the bipartisan 2024 bill by dropping the earnings test, and from Romney's design by delivering through the IRS rather than SSA and by not paying for itself through consolidation.
- **Two open differences.** The bill keeps a taxpayer identification number rule for the child but drops the 2025 law's parent SSN rule [EV-SEC-264]. Shared rule 3 decides this with the immigration flagship. And the legacy model's version of the bill keeps $2,000 rather than current law's $2,200 a child (`legacy-research.md`, 2).

## Part B. Income support, delivery and the economy ahead

### B.1 How government delivers the floor

**What the research finds** (Espen's November 11 direction; `README.md`):

| Finding | Evidence strength; where | Evidence |
| --- | --- | --- |
| Take-up rises with automatic or default enrollment and falls with administrative barriers | Review of U.S. and UK research | [EV-SEC-101] |
| Burdens are policy choices; Social Security's administrators kept them low on purpose | Synthesis (Herd and Moynihan) | [EV-SEC-100] |
| A simpler IRS letter brought substantial new earned income credit claims among 35,050 people who had not claimed | Randomized field experiment, IRS | [EV-SEC-102] |
| Information raised SNAP enrollment among eligible older people from 6% to 11%, and information plus help to 18% | Randomized trial, 30,000 people, Pennsylvania | [EV-SEC-103] |
| The people the outreach brought in got smaller benefits and were less sick than the average enrollee: the steps screen out the neediest most | Same trial | [EV-SEC-104] |
| Later-in-the-month recertification interviews cut SNAP renewal by over 20% | Quasi-experimental, San Francisco | [EV-SEC-105] |
| Closing an SSA field office cut disability recipients nearby by 16% | Quasi-experimental, national | [EV-SEC-106] |
| Removing automatic enrollment cut Massachusetts's subsidized coverage by a third | Quasi-experimental (care's register) | [EV-CAR-206] |
| Most people dropped in the Medicaid unwinding lost coverage for paperwork reasons | Administrative data (care's register) | [EV-CAR-210] |

**Delivery models.**
- **The 2021 credit.** The IRS paid from 2019 or 2020 returns and a non-filer tool [EV-SEC-109]. By October 2021 it reached families of about 61 million children [EV-SEC-107], nearly 9 in 10 by automatic deposit [EV-SEC-108]. The gap was non-filers: CBPP estimated up to 4 million children could be missed [EV-SEC-110] [EV-SEC-058]. By October 2022, 4.1 million recipients had not filed the return that reconciles the advance [EV-SEC-059]. Treasury mapped unclaimed children to target outreach [EV-SEC-061].
- **Canada.** The child benefit can be claimed at the child's birth registration. The province shares the proof of birth with the tax agency, with the parent's consent [EV-SEC-113]. The agency invited about 2 million low-income people with simple taxes to file by phone or a simple form in 2024 [EV-SEC-114]. It is not fully automatic, but the default runs through records the state already holds.
- **Social Security.** Benefits are over 99% of its cost; administration and related costs are under 1% [EV-SEC-115]. Pew finds SSA viewed favorably on balance by both parties [EV-SEC-116], against 37% favorable for the IRS [EV-SEC-117].
- **State paid leave.** Washington aims to pay within three weeks and met that in 16 of 30 months [EV-SEC-118]. Moving staff from phones to claims cut processing time and lengthened phone waits [EV-SEC-119].
- **Free filing.** In its 2024 pilot, IRS Direct File drew 140,803 accepted returns and a 90% satisfaction rating [EV-SEC-112]. It has since ended (section 1, B.5).

**What it means.** Outreach helps, but in the SNAP trial it still missed the neediest [EV-SEC-104]; automatic delivery reaches them without it. The strongest evidence for the design lens (`DEC-2026-11-09-13`) is here: in the trials, defaults and simple steps beat requirements. The 2021 credit reached most children because it paid from records the IRS held. It missed the families who do not file, the poorest. Canada's registration-at-birth and simplified filing are the tested ways to close that gap.

### B.2 SNAP, SSI and work conditions

- **Food aid in childhood pays off later.** Children whose counties got food stamps early were healthier as adults, and women were more self-sufficient (quasi-experimental) [EV-SEC-232].
- **Work conditions mostly remove eligible people.** Arkansas's Medicaid work requirement cut coverage with no gain in employment (quasi-experimental; care's register) [EV-CAR-212]. This dossier has no evaluation of the 2025 SNAP time limit yet; CBO expects it to remove about 2.4 million people (section 1, B.2). LAB-10's rule that participation is an offer is consistent with this evidence.
- **Evidence still needed**: an evaluation of SSI's asset limit (care's part B uses the bipartisan bill's figures [EV-CAR-478]) and of the SNAP time limit's effect on work.

### B.3 Participation help and on-ramps

Espen asked how the floor can carry people into the jobs the plan creates: care, construction, trades, housing production, infrastructure and clean power (`README.md`).

| Finding | Evidence strength; where | Evidence |
| --- | --- | --- |
| Sector-focused training for low-wage workers, with screening, occupational and soft-skills training and support services, produces earnings gains of 11 to 40 percent that last | Randomized trials pooled (Year Up, Project QUEST, WorkAdvance, Per Scholas; the journal version reportedly gives 12 to 34 percent) | [EV-SEC-143] |
| Registered apprentices earned $5,839 more in the ninth year than similar non-participants | Matched comparison, ten states (Mathematica for the Labor Department) | [EV-SEC-144] |
| Trade adjustment assistance: fourth-year earnings $3,300 lower or no different | Matched comparison (Mathematica for the Labor Department) | [EV-SEC-147] |
| Trade adjustment assistance: $50,000 more in cumulative earnings over ten years | Quasi-random assignment of investigators, Census data | [EV-SEC-148] |
| Lack of child care keeps low-income parents out of training | Interviews with 17 programs (Urban Institute) | [EV-SEC-149] |

- **How to read it.** The randomized evidence favors programs built with employers for specific occupations, not general job search. The trade assistance studies disagree, and the quasi-random one, with the longer horizon, finds large gains [EV-SEC-147] [EV-SEC-148]. Income and child care during training are the support the evidence names as barriers. They are what LAB-10's envelope was meant to buy.
- **Where the jobs are.** Health care and social assistance add the most jobs to 2035, over 2.2 million, with home care for older and disabled people adding 625,400; solar and wind trades grow fastest but add fewer than 15,000 (BLS projection) [EV-SEC-133]. An industry group puts construction's need at 349,000 new workers in 2026 [EV-SEC-145], and its model counts about 3,450 jobs per $1 billion of construction spending [EV-SEC-146]. Both are an industry group's figures, uncorroborated.
- **Design implication (for S3).** Pair LAB-10 with the plan's own job programs: care at the $20 floor (`DEC-2026-11-11-04`), housing's production and repair funds, transportation's repair and rail, clean power. Use sector partnerships and registered apprenticeship (LAB-8), with paid training time, income during training and child care during training.

### B.4 The economy ahead: what it may demand and offer

These are projections and should be read as such.
- **Work arrangements.** In July 2023, 11.9 million people (7.4% of workers) were independent contractors on their main job and 2.8 million were on call [EV-SEC-120]. A 2015 survey found alternative arrangements had risen to 15.8% of workers [EV-SEC-121]; BLS's official count is lower. Income volatility is common: 30% had income that varied in 2025 [EV-SEC-054].
  - **Portable benefits.** A Republican Senate bill would let firms offer benefits to independent workers without reclassification risk [EV-SEC-142]. The state portable-benefit laws are not yet in the register.
  - **For the design.** Benefits that attach to the person, not the job, travel with gig workers: a child benefit paid to the family, paid leave run as social insurance (as the state programs and FAM-3 are), and Social Security.
- **AI.**
  - The estimates range widely. Acemoglu estimates productivity gains of at most 0.66% over ten years [EV-SEC-124]. Eloundou and others find large shares of tasks exposed [EV-SEC-125]. The IMF puts 60% of jobs in advanced economies as exposed [EV-SEC-126].
  - On employment, the Yale Budget Lab found no discernible disruption through late 2025 [EV-SEC-127]. Brynjolfsson, Chandar and Chen find no economy-wide displacement through mid-2026, but young workers in exposed jobs 19% below trend [EV-SEC-128].
  - The legacy plan answers with AI-4's wage insurance and transition support, with no need to prove AI caused the job loss [EV-SEC-129], and a per-person AI rebate held because it is unscored [EV-SEC-130]. Its October 26 allocations were $120 billion for AI-4 and $100 billion for LAB-10 [EV-SEC-131].
  - **For the design.** No decision here turns on a displacement forecast. An evidence-based floor reaches displaced workers the same way it reaches anyone whose income falls. Whether a dividend joins the floor's payment channel is a delivery question for S3.
- **An older country.** On Census's 2023 projection, people 65 and older outnumber children from 2029 [EV-SEC-132]. About 63 million adults gave ongoing care in the past year [EV-SEC-134]. This raises the stakes of Social Security's solvency, of credit for caregiving (part D) and of care jobs as an on-ramp (B.3).

## Part C. Paid leave

### C.1 What state programs do

| Finding | Evidence strength; where | Evidence |
| --- | --- | --- |
| California doubled mothers' leave from about 3 to 6 weeks; later weekly hours of employed mothers of toddlers rose 10-17% | Quasi-experimental, CPS 1999-2010 | [EV-SEC-355] |
| Higher work and employment for mothers 9-12 months after birth | Quasi-experimental, national youth survey (shares an author with the row above) | [EV-SEC-356] |
| **No gain in women's employment or earnings; lower employment and earnings for first-time mothers about a decade later** | Regression discontinuity in time, IRS and SSA records, California | [EV-SEC-357] |
| Less labor force detachment for mothers, lasting up to nine years; similar in New Jersey, Rhode Island and New York | Quasi-experimental, survey data | [EV-SEC-358] |
| Young women's participation up 1.5 points, and unemployment up 0.3-1.5 points | Quasi-experimental | [EV-SEC-359] |
| CRS: the employment evidence is mixed | Review | [EV-SEC-360] |
| Fathers 46% more likely to take leave in the child's first year | Quasi-experimental, California | [EV-SEC-362] |
| Higher benefits near the cap did not lengthen leave or hurt later earnings, and raised return to the same employer | Regression discontinuity, California administrative data | [EV-SEC-361] |
| Employers: 89-99% report positive or no effects on productivity, profitability, turnover and morale | Employer survey, no comparison group (CEPR) | [EV-SEC-363] |
| New York small firms found long absences easier to handle, with no adverse effects; opposition rose from 4.1% to 9.5% | Matched comparison, New York against Pennsylvania | [EV-SEC-364] [EV-SEC-365] |
| Infant hospital admissions fell | Quasi-experimental, all California infant admissions | [EV-SEC-366] |
| Better school-age health, especially for less advantaged children | Quasi-experimental | [EV-SEC-367] |
| Nursing home use by older people fell 11% | Quasi-experimental | [EV-SEC-368] |
| Exclusive breastfeeding up 3-5 points | Quasi-experimental | [EV-SEC-369] |

- **The contested finding, both sides.** The studies that find mothers' work rising use surveys and short horizons [EV-SEC-355] [EV-SEC-356] [EV-SEC-358]. The one with the largest and most precise data, tax records, finds no long-run benefit and some harm for first-time mothers [EV-SEC-357]. The program studied paid 6 weeks at 55% of wages; California now pays 8 weeks at 60-90%, with a progressive formula [EV-SEC-314] [EV-SEC-315], which no study has evaluated. The health and fathers' findings are consistent across studies. The case for paid leave rests most securely on leave-taking, child and family health, and fathers' share, not on mothers' long-run earnings.

### C.2 Design lessons from the states

- **Take-up is lowest where need is highest.** California's lowest-earning quarter and small-firm workers claim least [EV-SEC-372]. 40-47% of employed new mothers and 4-12% of fathers made a bonding claim [EV-SEC-373]. Black and Hispanic workers report more unmet need [EV-SEC-374]. California's 2018 change and Washington's formula replace up to 90% for low earners [EV-SEC-314] [EV-SEC-311], but no study yet shows that raises take-up: evidence still needed.
- **Job protection matters for low earners.** Two-thirds of workers with unmet need could not afford unpaid leave, and 45% feared losing their job [EV-SEC-307]. 18% of low-wage leave-takers lost a job [EV-SEC-308]. California's benefit carries no job protection of its own; Oregon's does after 90 days [EV-SEC-313]. The 2025 FAMILY Act would protect the job at any employer size [EV-SEC-342].
- **Financing.** All state programs are payroll-financed, mostly by employees [EV-SEC-312]. Washington's rate has risen from 0.40% to the 1.2% cap as claims grew [EV-SEC-323] [EV-SEC-325] [EV-SEC-326]. Its actuary and auditors find the capped formula too low [EV-SEC-327] [EV-SEC-329]. It still collected $4.5 billion and paid $4.2 billion through 2023 [EV-SEC-328]. Take-up assumptions drive the rate: American Action Forum's illustrations run from 0.4% to 2.9% of wages [EV-SEC-345]. This is the closest real test of FAM-3A's automatic step-up, and it shows the step-up needs room above the cap.
- **The employer credit has little reach.** Section 45S reached 1,230 firms in 2020, with 88% of the dollars going to firms with revenue over $1 billion [EV-SEC-334]. Brookings finds it covers at most 25% of an employer's cost [EV-SEC-335].
- **Administration.** Washington's processing times show a new program's staffing trade-offs (B.1) [EV-SEC-118] [EV-SEC-119].

### C.3 Abroad

| Finding | Evidence strength; where | Evidence |
| --- | --- | --- |
| The OECD average paid maternity leave is 18.5 weeks; the U.S. alone has none nationally | International practice | [EV-SEC-375] [EV-SEC-376] |
| Short leaves raise women's employment; very long leaves lower their relative wages | Quasi-experimental, nine European countries, 1969-93 | [EV-SEC-377] |
| Most estimates of leave's effect on women's work are negligible to weakly positive; early education and child care do more | Review | [EV-SEC-378] |
| Norway's father month raised fathers' take-up from 3% to 35%, with spillovers to coworkers and brothers | Quasi-experimental | [EV-SEC-379] |
| Quebec's higher benefits and five father-only weeks raised fathers' participation 250% | Quasi-experimental | [EV-SEC-380] |
| Germany's 2007 earnings-related leave: mothers worked less in the first year and more after | Quasi-experimental | [EV-SEC-381] |
| Germany's reform raised fertility of tertiary-educated women up to 22% relative to others | Quasi-experimental | [EV-SEC-382] |

Twelve weeks sits well inside the short-leave range where the international evidence finds no harm to women's work [EV-SEC-377]. Reserving weeks for fathers is the clearest lever on fathers' take-up [EV-SEC-379] [EV-SEC-380].

### C.4 The bills, compared

| Bill or program | Design | Cost and status | Against the legacy FAM-3A | Evidence |
| --- | --- | --- | --- | --- |
| FAMILY Act 2025 (S. 2823, H.R. 5390) | 12 weeks; 85%, 69% and 50% of earnings in bands, $580 to $4,000 a month; job restoration; run by an office in SSA; grants to states with programs at least as good; no financing section in the text read | Referred to committee; not scored | Same weeks and administrator; more progressive replacement; FAM-3A adds a payroll contribution and step-up the 2025 bill does not specify | [EV-SEC-338] [EV-SEC-339] [EV-SEC-340] [EV-SEC-341] [EV-SEC-342] [EV-SEC-343] |
| FAMILY Act 2019 (H.R. 1185) | Up to 12 weeks at about two-thirds of earnings; 0.4% payroll tax | CBO and JCT, 2020: $547 billion of spending over 2020-30 against $361 billion of tax | The legacy file's "$547B" is this score of the older bill | [EV-SEC-344] |
| Build Back Better (2021) | 4 weeks, from 2024 | CBO about $205 billion (via CRFB); dropped from the enacted law | FAM-3C | [EV-SEC-346] [EV-SEC-347] [EV-SEC-348] |
| President's FY2025 budget | 12 weeks, SSA | $325 billion over a decade (CRFB, from OMB) | Close to FAM-3B's general-fund form | [EV-SEC-349] [EV-SEC-350] |
| More Paid Leave for More Americans Act (H.R. 3089, House bipartisan working group, 2025) | Grants of $1.5-7 million to states, and interstate networks; no federal benefit | Referred; hearing February 2026 | Not a benefit: a floor states may build | [EV-SEC-351] [EV-SEC-352] |
| Section 45S employer credit | 12.5-25% of leave wages, permanent from the 2025 law | 1,230 firms in 2020 | Current law | [EV-SEC-330] [EV-SEC-334] |
| Cassidy-Sinema (2019); New Parents Act (2023) | Advance $5,000 of the child credit, or borrow three months of Social Security, repaid later | Proposals | Republican alternatives that fund leave from families' own future benefits | [EV-SEC-353] [EV-SEC-354] |
| State programs | 13 operating; payroll-financed; 50-100% replacement | — | FAM-3A's model, at national scale | [EV-SEC-309] [EV-SEC-311] [EV-SEC-312] |

**Where the legacy choice sits.** FAM-3A follows the FAMILY Act's 12 weeks and SSA administration and the states' payroll financing. It departs from the 2025 FAMILY Act by setting a contribution with an automatic step-up, and its replacement rate ("about two-thirds") is the 2019 bill's, less progressive than the 2025 text [EV-SEC-340]. The bipartisan House approach is state grants, not a federal benefit. The Republican Senate ideas fund leave from families' own credits or Social Security.

## Part D. Social Security

### D.1 What it does

- Elderly poverty falls about one for one with benefits. Social Security explains the whole fall in elderly poverty from 1967 to 2000 (Engelhardt and Gruber; quasi-experimental, birth cohorts) [EV-SEC-442] [EV-SEC-443]. Brookings independently reads the evidence the same way [EV-SEC-444].
- It moved 28.8 million people out of poverty in 2025 [EV-SEC-420], costs under 1% to run [EV-SEC-115] and is trusted across parties [EV-SEC-116]. It is the plan's model of a floor that works: universal, automatic, earned and paid monthly.

### D.2 Benefit designs: minimum benefit, cost-of-living and caregivers

| Design | Evidence | Strength | Cost (SSA, % of payroll) |
| --- | --- | --- | --- |
| A minimum benefit at 125% of poverty for 30 years of work (legacy SS-3; in Social Security 2100 and the 2016 bipartisan commission) | Today's special minimum reaches almost no one [EV-SEC-439]; the commission proposed a basic minimum [EV-SEC-475] | Program record; judgment | −0.11 [EV-SEC-445] |
| CPI-E (legacy SS-4) | CPI-E has grown about 0.2 points a year faster [EV-SEC-440] [EV-SEC-441] | Experimental index; it does not adjust for seniors' discounts or quality | −0.33 [EV-SEC-455] |
| Caregiver credits | Germany credits a parent with average earnings for three years per child [EV-SEC-478]; Canada drops caregiving years from the formula [EV-SEC-480]; the OECD finds a five-year care break cuts pensions 5% on average [EV-SEC-479]; Social Security 2100 credits 960 hours of care a year [EV-SEC-460] | International practice | A child-care dropout year: −0.06 [EV-SEC-445] |
| An across-the-board increase (legacy SS-B1) | — | — | −1.56 on the 2026 score (the legacy file's −1.46 is from 2023) [EV-SEC-446] |

Care's memo 9 left a Social Security caregiver credit to this dossier (`README.md`, "Seams"). The international designs credit caregiving through the benefit formula, not through a separate payment.

### D.3 Solvency: the packages and the bills

| Bill or plan | Design | Score | Status | Against legacy D8 | Evidence |
| --- | --- | --- | --- | --- | --- |
| Social Security 2100 Act (H.R. 9519, June 2026; S. 5042, July 2026) | Higher first benefit factor for 2027-36; COLA the higher of CPI-W and CPI-E; minimum benefit at 125% of poverty; repeal of the wage base after 2026; 12.4% on investment income above $400,000; caregiver credits | None for the 2026 text; the 2023 version moved depletion from 2034 to 2066 | Referred; five Democratic cosponsors | Close to SS-1 to SS-4 plus a caregiver credit; removes the cap fully rather than above $250,000 | [EV-SEC-456] [EV-SEC-457] [EV-SEC-458] [EV-SEC-459] [EV-SEC-460] [EV-SEC-482] [EV-SEC-454] [EV-SEC-477] |
| Social Security Expansion Act (Warren-Sanders, 2023) | Payroll tax above $250,000, investment income and benefit increases | 2023: deficit 3.42% to 0.12% on 2022 assumptions; would not hold at 4.42% | No 2025-26 letter found | The legacy package's base and its SS-5 come from it | [EV-SEC-453] |
| Warren-Moreno framework (June 2026) | Lift the cap so high earners pay the same share | SSA scores removing the cap without benefit credit at 2.55% (58% of the gap) | An op-ed, no bill as of November 2026 | SS-10's opening | [EV-SEC-461] [EV-SEC-462] [EV-SEC-448] [EV-SEC-465] |
| Cassidy-Kaine fund | $1.5 trillion borrowed and invested in stocks over 75 years | Unscored; sponsors claim 65% to about 75% of the shortfall | Proposal | A form of SS-8 | [EV-SEC-466] [EV-SEC-467] [EV-SEC-468] [EV-SEC-469] |
| Commissions: PROMISE Act (S. 4979, bipartisan), Bipartisan Social Security Commission Act (H.R. 9187), Fiscal Commission Act (S. 4012) | A process, not a design | — | Introduced 2026 | The 1983 route | [EV-SEC-470] [EV-SEC-471] [EV-SEC-472] |
| Republican Study Committee | FY2025: full retirement age from 67 to 69; 2026 document: no retirement-age rise | — | Budget documents | Benefit cuts, which D8 rejects | [EV-SEC-473] [EV-SEC-474] |
| Bipartisan Policy Center commission (2016) | A basic minimum benefit; retirement age indexed to longevity, to 69 | — | Report | Shares SS-3; differs on the retirement age | [EV-SEC-475] |

- **Republican openness.** Reps. Cole and Smucker say they would consider raising the cap [EV-SEC-463]. Three of 20 Republican Senate candidates in 2026 endorsed raising or removing it [EV-SEC-464]. That is the basis for testing SS-10's 67-vote premise, which the register cannot yet confirm.
- **The 1983 precedent.** A presidential commission reported in January 1983 and the amendments passed that spring [EV-SEC-415], against a gap less than half of today's [EV-SEC-414].
- **Process.** Section 310(g) bars Social Security from reconciliation [EV-SEC-476].
- **What it shows.** Every serious plan closes most of the gap with revenue from high earnings. The cap-removal score (2.55) [EV-SEC-448] is close to the legacy SS-1 (+2.30 on SSA's +2.52 base [EV-SEC-447]). The legacy package, the 2100 Act and the Warren-Moreno idea all rely on it. The plans differ on investment income, benefit increases and whether a commission or a bill comes first. None has a current whole-package actuarial score.

## Part E. Coordinating phase-outs

### E.1 Do stacked rates and cliffs change behavior?

| Finding | Evidence strength; where | Evidence |
| --- | --- | --- |
| A $1-for-$2 offset in place of SSDI's earnings cliff raised the share earning above the line (7% in one stage, 23% among volunteers) but not average earnings; it cost more than it saved | Randomized trial, SSA, national | [EV-SEC-546] [EV-SEC-547] [EV-SEC-548] |
| Bunching at the earned income credit's kink appears only among the self-employed | Quasi-experimental, tax data | [EV-SEC-549] |
| Bunching at the premium credit's poverty-line notch appears only among the self-employed | Quasi-experimental, Census | [EV-SEC-550] |
| Bunching below the 400% cliff appears among wage earners too, mostly through retirement contributions | Quasi-experimental, IRS data | [EV-SEC-551] [EV-SEC-552] |
| AFDC's benefit-reduction rate fell from 100% to 67% in 1967 and the 1981 law raised it to 78% for workers | Program history | [EV-SEC-553] [EV-SEC-554] |
| A HUD rent rule built to reward work did not raise earnings after six years | Randomized trial (housing's register) | [EV-HOU-400] |

- **How to read it.** The evidence is consistent: smoothing rates helps families keep more and is fairer, but it changes work little, except where people can easily adjust reported income. Some evidence on the 400% cliff conflicts [EV-SEC-549] [EV-SEC-551]. So the case for a ceiling on combined rates (shared rule 2) is mainly fairness and simplicity, and modestly work.

### E.2 How others coordinate

| Approach | Where | What it does | Evidence |
| --- | --- | --- | --- |
| One benefit, one taper | UK Universal Credit | Six benefits merged with a single 55% taper (cut from 63% in 2021) | [EV-SEC-555] |
| — its failure | Same | The National Audit Office found it not value for money and its employment effect unmeasurable; its rollout was troubled | [EV-SEC-556] |
| One income test from the tax return | Canada child benefit | Prior-year family net income, the same for federal and provincial benefits | [EV-SEC-558] [EV-SEC-557] |
| Low tapers on a single family benefit | Australia | 20 cents, then 30 cents, a dollar | [EV-SEC-559] |
| Excluding credits from income | U.S., 26 U.S.C. 6409 | Refundable credits never count for other programs | [EV-SEC-534] |
| Borrowing another program's finding | U.S.: HUD, express lane eligibility | One income finding used twice | [EV-SEC-510] [EV-SEC-562] |
| Holding benefits steady through a change | SNAP transitional benefits (24 states); child care's continued help to 85% of state median income | Benefits frozen up to 5 months; a graduated exit | [EV-SEC-560] [EV-SEC-561] [EV-SEC-529] |
| Escrowing the rent rise | HUD Family Self-Sufficiency | Part of the rent increase from higher earnings saved for the family | [EV-HOU-236] |
| Keeping help past the line | Colorado's cliff pilot | Child care help above the entry limit; no comparison group | [EV-SEC-563] |

- **What it shows.** The tested coordination is at the level of rules: one income definition, one test reused, credits excluded, benefits held steady through a change. Their effects on work are mostly unmeasured. The UK shows that merging benefits into one is a large delivery risk. The US already has the cheapest tool, section 6409's exclusion, and paying the floor's benefits through it keeps them out of other programs' tests.
- **For S3's ceiling.**
  - The plan's own benefits can be excluded from each other's tests, as section 6409 does for credits.
  - Its new phase-outs (child care's 7%) can be kept low.
  - The income test can be one: the prior-year return, as Canada does, or a shared verification under shared rule 5.

## Failures to avoid

1. **An earnings phase-in that excludes the poorest children.** The current credit and the bipartisan 2024 bill keep one [EV-SEC-011] [EV-SEC-269]. The employment case for it is contested (A.2, A.6).
2. **A benefit only filers can get.** Non-filers missed the 2021 credit [EV-SEC-110] [EV-SEC-059]. Use records already held, birth registration and a simple non-filer route.
3. **A temporary benefit.** The 2021 credit's gains reversed within a month of its last payment [EV-SEC-208] [EV-SEC-205]. Permanence matters for both poverty and any work response.
4. **A contribution that cannot rise with take-up.** Washington's capped paid-leave rate fell behind claims [EV-SEC-327].
5. **Paid leave without job protection or full wages for low earners.** The workers who need it most claim least [EV-SEC-372] [EV-SEC-308].
6. **A merged system launched all at once.** Universal Credit's rollout is the warning [EV-SEC-556].
7. **Relying on unproven analysis in the second Trump administration's data.** SSA's self-reported service gains and the administration's ending of food-security data (section 1, B.4, B.5).
8. **Running out the Social Security clock.** Depletion arrives in late 2032 [EV-SEC-400], and only a regular-order law can fix it [EV-SEC-476].

## Evidence still needed

- Census's revised SPM child series after July 2026's threshold correction [EV-SEC-207].
- A CBO or JCT score of the American Family Act on the 2025 law's baseline; the JCT document for H.R. 7024.
- Evidence that higher wage replacement raises low earners' paid leave take-up (California's 2018 change; Washington).
- California EDD's 2016 economic impact study (Bedard and Rossin-Slater); Irish and others on maternal mental health.
- CBO's own score of Build Back Better's paid leave; any score of the 2025 FAMILY Act.
- SSA actuarial scores of the 2026 Social Security 2100 Act, the legacy package as a whole, and SS-10's trade.
- Research on Disability Insurance and SSI and poverty; the UK's Carer's Credit.
- State portable-benefit laws (Utah, Alabama, Tennessee); research on SNAP churn (Unrath; Ganong and Liebman).
- Evaluations of the 2025 SNAP time limit and of SSI's asset limit.
- A Government of Canada evaluation of the Canada child benefit; the Resolution Foundation's two-child limit estimate.
- Quotations several gatherers took from search-tool page extracts, flagged in their catalog rows, to be spot-checked by the reviewer (EV-SEC-231 and EV-SEC-120 were re-checked).

## Questions this section leaves for section 3

The forks are listed in `README.md` ("Forks for S3"). Section 2 bears on them as follows:
1. **The child benefit's form**: full refundability and no earnings test (FAM-1A, 1C, 1D, Canada), against keeping a phase-in (current law, the 2024 bill). The poverty evidence favors the first; the work evidence is contested.
2. **Delivery**: automatic payment from held records and birth registration, against claims. B.1 favors the first.
3. **Paid leave's replacement rate and job protection**: the 2025 FAMILY Act's progressive bands and job restoration, against FAM-3A's two-thirds.
4. **Paid leave's financing**: a contribution with headroom above any cap (C.2).
5. **Social Security**: which revenue base, which benefit improvements (minimum, CPI-E, caregiver credit), and a commission or a bill first (D.3).
6. **The phase-out ceiling**: exclusions and one income test before lower rates (E.2).
