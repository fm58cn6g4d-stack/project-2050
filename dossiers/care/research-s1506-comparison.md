# Care, health part: the project's design against the Medicare for All Act of 2025, and when employer groups move

Role: research note for stage D, step 3c. It compares the health design Espen decided on November 10 (`DEC-2026-11-10-09`) with the Medicare for All Act of 2025 (S. 1506, 119th Congress, Sen. Sanders; House companion H.R. 3069, Rep. Jayapal). It also re-examines memo 2's choice to move employer groups last, and confirms or changes memo 3. Status: draft, for review and for Espen's answers in part (d). It decides nothing. Memo 1 B, the 2037 endpoint, memo 4 C and memo 5 B are settled and are not re-argued. Where the bill differs on them, the table says so.

Sources: the bill texts are saved in the library as SRC-3260 (S. 1506) and SRC-3261 (H.R. 3069). Bracketed tags point to `evidence.json`. The bill entries are EV-CAR-270 to 292; the employer-coverage entries are EV-CAR-293 to 314. Figures marked "project arithmetic" come from `tools/employer_wave.py`, which reuses the coverage model's inputs and single-payer formulas (`models/tools/health-coverage/`). They are exploratory, not a score.

## What to know first

- **The bill is faster and simpler than the project's path, and it levies no tax.** Under S. 1506 everyone is in the program on January 1 of the fourth calendar year after enactment [EV-CAR-272]. For a 2029 law that is 2033, against the project's 2037. Before that, children go first and a buy-in opens at ages 55, 45 and 35 in years one to three [EV-CAR-273]. The trust fund pools existing federal money and the revenue from ending employer plans and the Exchanges [EV-CAR-287]. There is no state maintenance of effort except for nursing homes [EV-CAR-278], no employer contribution, and no new tax. The House bill takes 2 years [EV-CAR-290].
- **Memo 2's main claim does not hold as written.** Employer coverage works better than the individual market, and most people in it are satisfied. But it leaves 29% of its enrollees underinsured [EV-CAR-109], its cost comes out of workers' pay [EV-CAR-296], and it is least available to lower-wage workers [EV-CAR-295]. "Best-functioning" is not a sound reason to move it last.
- **Memo 1's claim that employer groups "carry most of the cost" is also wrong on the net federal measure.** Moving them adds about $0.75 trillion of the single plan's $3.55 trillion in 2032. Medicaid adds about $1.1 trillion and current Medicare about $0.9 trillion (project arithmetic). An employer contribution of about 71% of today's employer premiums makes their move cost the federal budget nothing.
- **The recommendation changes, but only partly.** The reasons left for not forcing employer groups early are disruption, the shock to hospital revenue and political risk; "best-functioning" is no longer one of them. So the note recommends opening the single plan to employer groups and workers from wave 2, voluntarily, with the transitional contribution, and moving everyone at the 2037 endpoint (option C in part b).
- **Memo 3 B is confirmed**, with one addition: name the revenue from ending the employer tax exclusion as a stream, as the bill does.

## (a) Provision by provision

"Ours" means the decided design (`DEC-2026-11-10-09`): memo 1 B (staged path, 2037 endpoint), memo 2 by payer with children first plus five protections, memo 3 B provisionally, memo 4 C, memo 5 B, and points 1-7 yes, with point 6 as option (b). "Stricter" means it asks more of people or payers, or limits more; "looser" means it commits less.

| Topic | What S. 1506 says | What the project decided | Same, stricter, looser or different | Why ours differs (evidence, design lens) | Recommendation |
| --- | --- | --- | --- | --- | --- |
| **Entitlement, residency, immigration** | Sec. 102(a): "Every individual who is a resident of the United States is entitled to benefits"; residency criteria by rule; sec. 102(b)(2) bars travel "for the sole purpose of obtaining health care" [EV-CAR-270]. No immigration-status test for residents. The interim buy-in (sec. 1011) is limited to citizens, nationals and permanent residents. | Point 3: cover every resident, proposed to the immigration flagship, which owns shared rule 3; lawfully present immigrants restored in the first bill (point 1). | Same aim; ours is looser as a commitment, because the status question is deferred to its owner. | Shared rule 3 belongs to the immigration flagship; noncitizens are already the least-covered group (28.9% uninsured) [EV-CAR-103]. | **Keep ours.** Give the immigration flagship the bill's residency rule as the model proposal. |
| **Enrollment** | Sec. 105: "automatic enrollment of individuals at the time of birth ... (or upon establishment of residency)"; a card that "shall not include an individual's Social Security number" [EV-CAR-271]. | Point 2: automatic enrollment and renewal from records the government holds, no work requirement. | Same. The bill adds the card without the Social Security number. | Both follow the design lens; one extra step cuts take-up [EV-CAR-206]. | **Keep ours; adopt the card rule** in section 4. |
| **Effective date and transition** | Sec. 106: full program on "January 1 of the fourth calendar year that begins after the date of enactment" (2033 for a 2029 law); people under 19 from the first January (2030) [EV-CAR-272]. Title X: a buy-in at 55, 45 and 35 in years one to three, at a premium of 1/12 of average cost [EV-CAR-273]; a Medicare Transition plan through the Exchanges for any resident and for qualified employers, at 90% actuarial value and Medicare rates [EV-CAR-274]; Medicare upgrades in year one [EV-CAR-289]. House: 2 years [EV-CAR-290]. | Memo 1 B: endpoint 2037. Memo 2: wave 1 in 2031 (the uninsured, the individual market and children, enrolled automatically, plus Medicare at 60); Medicaid in 2033-35; employer groups by 2037; Medicare at 50 in 2035. | **Different: ours is 4 years slower than the Senate bill and 6 slower than the House's.** The bill's age steps are a voluntary buy-in at full average cost; ours are automatic entitlement. | Espen chose 2037 so each step can be built, staffed and paid for, and to give the financing a decade (memo 1). The bill's buy-in charges a premium near average cost, with tax credits; that is a step that drops eligible people [EV-CAR-206]. Ours uses automatic enrollment, as the lens prefers. | **Keep ours** (decided). **Two findings.** (1) The bill's Transition plan lets employers buy in early; part (b) builds on that. (2) Memo 2 never says when today's Medicare enrollees move or get upgrades. The bill upgrades them in year one: a $1,500 cap and $0 deductibles [EV-CAR-289]. Under ours they could wait until 2037. **Put to Espen** (part d, question 3). |
| **Duplicative private coverage** | Sec. 107: from the start date it is unlawful "to sell health insurance coverage that duplicates the benefits"; coverage of "additional benefits not covered" stays legal. Secs. 801-802 bar duplicative employer plans and repeal COBRA [EV-CAR-275]. | Implied by memo 1 B (single-payer at the endpoint); not yet written. Before the endpoint, private and employer plans continue for groups not yet moved. | Not yet considered at the level of a rule. | — | **Adopt the bill's rule for the endpoint** in section 4: no duplicative coverage, supplemental coverage allowed. It follows from memo 1 B, so it needs no new decision. |
| **Benefits, including long-term care** | Sec. 201: comprehensive, including "Comprehensive reproductive care, including abortion"; dental, vision, hearing; "Home- and community-based long-term care services and supports" [EV-CAR-276]. Sec. 204: institutional long-term care stays in Medicaid, with a state floor based on fiscal year 2024 spending [EV-CAR-278]. House: all long-term care, institutional and home-based [EV-CAR-291]. | Memo 4 C: comprehensive benefits; long-term care decided in part B of the dossier. Abortion is not mentioned. | **Looser now** (no long-term care yet) and **silent on abortion**. | Part B was set up to weigh an all-age home benefit against other designs; Medicaid pays for over two-thirds of home care today [EV-CAR-138]. | **Keep ours on long-term care.** Part B should weigh the Senate bill's split: home care federal, nursing homes in state Medicaid with a floor. **Abortion and reproductive care has not been considered: put to Espen** (question 4). The bill also lifts federal funding limits on reproductive care for trust fund money (sec. 701(b)(3)) [EV-CAR-287]. |
| **Cost sharing** | Sec. 202: none, except an optional drug schedule that "does not exceed $200 annually per individual" and is "not imposed" at or below "250 percent of the poverty line" [EV-CAR-277]. House: none at all [EV-CAR-291]. | Memo 4 C: none below 200% of poverty, or anywhere for primary care, prevention, maternity, mental health and chronic-condition drugs; small copays above that, with a cap of $1,000 a person (working figure). | **Stricter**: more cost sharing and a lower income line. | Memo 4 uses copays to damp use where supply is tightest, because CBO expects demand to outrun supply [EV-CAR-219]. The design lens counts against copays; memo 4 accepted that cost. | **Keep ours** (decided). No defect: the bill's $200 is a drug cap, not a cap on all care. Section 4 can note that the bill's 250% line is the stricter protection. |
| **Provider participation and private contracts** | Secs. 301-302: participation agreements, no balance billing, an ethics duty against bonuses "based on patient utilization". Sec. 303: private contracts only where the program pays nothing, with a provider affidavit for "the 1-year period" [EV-CAR-279]. | Not decided. Memo 5 sets rates, not participation rules. | Not yet considered. | — | **Adopt the bill's structure in section 4**: all-in or all-out private contracting, as Medicare's opt-out works today, and a ban on utilization bonuses. |
| **Administration, regional offices, ombudsman** | Title IV: regional offices, each with a deputy for home and community care; a Beneficiary Ombudsman who handles complaints and appeals but "shall not serve as an advocate for any increases in payments"; GAO audits [EV-CAR-280]. | Not decided. Section 5 (delivery) holds it; the legacy work found CMS capacity is the binding constraint. | Not yet considered. | — | **Adopt the ombudsman** in section 4: low cost, and it helps people through the system. Regional offices are a section 5 question, to settle with the capacity review. |
| **National health budget** | Sec. 601: a yearly national budget with operating, capital, special projects, quality, education, administration, reserve and prevention parts [EV-CAR-281]. | Not decided. Memo 5 B sets rates and gives global budgets to rural and safety-net hospitals only. | **Different**: the bill budgets the whole system; ours controls price, not the total. | Memo 5 chose a rate glide path and targeted global budgets on evidence from Maryland [EV-CAR-259]. | **Keep ours** (decided). Record a national budget as the alternative section 8 names if spending growth beats its target. |
| **Worker assistance** | Sec. 602: "at least 1 percent of the national health budget" for up to 5 years, for wage replacement, retirement benefits, training, placement and preferential hiring [EV-CAR-282]. On the single plan's 2032 scale, 1% is about $69 billion a year (project arithmetic). | Memo 2, protection 2: wage replacement and coverage for up to three years, training, and first claim on the plan's jobs; a working assumption of $5-15 billion a year. | **Looser**: a need-based program at a fraction of the bill's floor. | Ours sizes help to the people displaced: about 601,800 insurer jobs [EV-CAR-233], 1.8 million gross insurance and billing jobs at most [EV-CAR-232]. A budget share sizes help to the system, not to need. | **Keep the need-based design; widen the working range in section 6.** $5-15 billion is untested against the trade-adjustment record. The bill shows how much more the sponsors would spend. |
| **Global budgets and fee-for-service** | Sec. 611: hospitals, nursing and dialysis facilities get a quarterly global budget set "through negotiations between the provider and the regional director", which may not cover capital; sec. 612: a national fee schedule for individual providers [EV-CAR-283]. Sec. 615: payments may not go to "the profit or net revenue of the provider" or marketing [EV-CAR-284]. | Memo 5 B: rates on a glide path to about 1.15 times Medicare; global budgets for rural, critical-access and safety-net hospitals; fee-for-service elsewhere. | **Different**: the bill uses global budgets for every institution, funds capital separately and bars profit. It sets no rate level; Medicare's payment systems are its baseline. | Memo 5 limits global budgets to thin markets, where Maryland's evidence is strongest [EV-CAR-259], and uses a target above Medicare to protect supply [EV-CAR-220]. | **Keep ours** (decided). Two items the project hasn't considered, for section 4 as open questions: separate capital funding, and the bar on profit and marketing. Neither is a defect in memo 5. |
| **Drug pricing** | Sec. 614: prices "negotiated annually by the Secretary" and a formulary that promotes generics [EV-CAR-285]. The Transition plan has a fallback: the lowest of the VA price and Medicaid's best price (sec. 1012(d)). | Memo 5 B: negotiate all drugs, extending the 2022 law's Medicare negotiation. | Same. The bill adds a formulary and a fallback price. | — | **Adopt a fallback price** in section 4: negotiation needs a price that applies when talks fail. A formulary is a section 4 detail. |
| **Trust fund and financing** | Sec. 701 (headed "Taxes"): 100% of the net revenue increase from secs. 801 and 902, meaning the tax exclusion and the credits that end. In the first year it also receives the prior year's appropriations for Medicare "(other than amounts attributable to any premiums)", Medicaid (federal money), FEHB and other programs; the Medicare trust fund balances transfer in [EV-CAR-287]. House: adds TRICARE's purchased care [EV-CAR-292]. **No state maintenance of effort except for nursing homes** [EV-CAR-278], **no employer contribution, no tax levied.** | Memo 3 B (provisional): keep Medicare's public streams, states pay a fixed share (half their Medicaid spending, working figure), employer premiums become a contribution, new revenue for the rest. Point 7: the hospital trust fund kept whole, folding in at the endpoint. | **Stricter**: ours asks states for about $300 billion a year and asks employers for a contribution; the bill relieves states of their Medicaid share and leaves the gap unfunded in its text. | The bill leaves taxes to separate legislation. A plan has to show the gap and who fills it (`DEC-2026-11-10-05`). Vermont's plan stopped when the full tax became visible [EV-CAR-245]. | **Keep ours; confirm memo 3 B** (part c), adding the tax-exclusion revenue as a named stream, as sec. 701 does. Point 7 matches the bill's transfer of trust fund balances. |
| **Medicare Advantage** | Not named. Sec. 901 ends all Medicare benefits, Advantage included, on the start date [EV-CAR-288]; no reform before. | Point 5: fix coding and benchmarks on MedPAC's method now, counting savings at MedPAC's 2026 estimate (14%, about $76 billion) [EV-CAR-135]; Advantage ends at the endpoint. | **Stricter** in the transition. | Under a staged path Medicare lasts eight more years, so the overpayment matters; under the bill it lasts four. | **Keep ours.** |
| **Health equity and primary care offices** | Secs. 616-617: an Office of Health Equity and, within it, an Office of Primary Health Care that sets national goals within a year; equity data may not be used "for any law enforcement or immigration purpose" [EV-CAR-286]. | Not considered. | — | — | **Adopt both offices and the data firewall** in section 4. The firewall supports point 3: people avoid programs whose records can be used against them. Its immigration side goes to the immigration flagship with point 3. |

### What the bill does that the project hasn't considered

- **Upgrades for today's Medicare enrollees in year one**: the $1,500 cap, $0 deductibles, a $300 drug threshold, dental, vision and hearing [EV-CAR-289]. Ours applies the legacy upgrades only under memo 1 A (point 4). Under B, current enrollees have no stated date. That is a gap; question 3.
- **Ending Medicare's 24-month wait for people on disability** (sec. 1004). For section 4, priced in section 6.
- **Guaranteed issue of Medigap** during the transition (sec. 1005). It matters for the eight years Medicare stays separate under ours.
- **Abortion and reproductive care**, and the override of federal funding limits for trust fund money; question 4.
- **No estate recovery for correctly paid Medicaid** (sec. 205). For part B (long-term care).
- **Non-discrimination with a private right of action** (sec. 104), and the bar on using quality metrics to set payment (sec. 615(e)). For section 4.
- **Early access for employers** to the Transition plan (sec. 1012) [EV-CAR-274]. Used in part (b).

Things the project has that the bill doesn't: restoring the 2025 law's coverage cuts first (point 1); automatic Medicare at 60 and 50 rather than a buy-in; a glide path for provider rates and protected hospital budgets (memo 5 B); a fixed state share and an employer contribution (memo 3 B); rural health through USDA (point 6 (b)); the Advantage fix (point 5); and a priced amount to be financed.

**Two drafting errors inside S. 1506**, worth knowing if it is used as a base text: sec. 204 adds Social Security Act section 1949, while secs. 204 and 901 refer to it as 1948; and the date that fixes which extra Medicaid services continue is March 1, 2025 in sec. 204 but January 1, 2023 in sec. 901.

## (b) The employer wave, re-examined

Memo 2 moved employer groups last because they are "the largest and best-functioning part" of the system and should move "after the public plan has a track record". Espen asked for a defense or a change. The evidence below runs both ways.

### What the evidence says

**1. Deductibles and underinsurance.** Employer coverage protects better than the individual market, but not well for a large minority.
- In 2026, 29% of working-age adults with employer coverage were underinsured, against half of those in marketplace plans (Commonwealth Fund, 2026) [EV-CAR-109].
- Thirty-eight percent of covered workers had a single deductible of $2,000 or more: 55% at smaller firms, 33% at larger ones (KFF Employer Health Benefits Survey, 2026) [EV-CAR-293].
- Four in ten adults with employer coverage had trouble paying medical bills or cost sharing in the past year (KFF and Los Angeles Times, 2019) [EV-CAR-314].

**2. Premiums paid out of wages.**
- A family premium was $28,303 in 2026, with workers paying $7,471 directly [EV-CAR-111] [EV-CAR-112].
- Research finds that rising premiums come out of pay and jobs:
  - a 10% premium rise lowers the wages of the employer-covered by 2.3% (Baicker and Chandra, Journal of Labor Economics, 2006) [EV-CAR-296];
  - hospital mergers raised prices and cut wages by a similar $638 (Arnold and Whaley, RAND, 2020) [EV-CAR-297];
  - rising prices act as "a de facto payroll tax on labor" (Brot-Goldberg and others, NBER, 2024) [EV-CAR-298].
- The pass-through is about half, mostly through higher worker contributions (Anand, Health Economics, 2017) [EV-CAR-299].
- Over the last five years, premiums grew close to wages: 28% against 26.9% (KFF, 2026) [EV-CAR-294].
- So the cost reaches workers, but it is not currently outrunning pay by much.

**3. Job lock, and coverage gaps at job loss.**
- Job lock was large before the ACA: it cut voluntary job changes by 25% (Madrian, Quarterly Journal of Economics, 1994) [EV-CAR-300].
- Since the ACA it has been small:
  - Medicaid expansion changed employment and job switching little (Gooptu and others, Health Affairs, 2016) [EV-CAR-301];
  - self-employment rose only briefly, in a narrow group (Blume-Kohout, ILR Review, 2024) [EV-CAR-302].
- Coverage often ends with the job.
  - In 2010, 34% of eligible jobless workers took COBRA, most who didn't cited cost, and nearly 25% were uninsured for two years or more (Mathematica for the Labor Department, 2015) [EV-CAR-303].
  - In 2008-10, 57% of adults who lost a job with benefits became uninsured (Commonwealth Fund, 2011) [EV-CAR-304].
  - Both figures are from before the ACA marketplaces. The 2029 baseline, with the enhanced credits expired and the 2025 law's cuts in force, makes them more relevant again: CBO projects 36.6 million uninsured in 2029 [EV-CAR-020].

**4. Unequal access.**
- Ninety-two percent of workers are at a firm that offers coverage, but only 55% are covered by their own employer's plan.
- At offering firms with many lower-wage workers, 47% are covered, against 61% elsewhere (KFF, 2026) [EV-CAR-295].
- Smaller firms carry the highest deductibles [EV-CAR-293].
- *Evidence still needed:* employer coverage by race and ethnicity (Census detailed table H-04). The Census report's figure gives private coverage only in a layout that can't be anchored.

**5. Satisfaction and trust.** This is the strongest support for "works well".
- Eighty-one percent of insured adults rate their insurance excellent or good, yet 60% of the employer-covered reported a problem with it in the past year (KFF, 2023) [EV-CAR-305].
- Sixty-five percent rate their own coverage excellent or good, against 24% for coverage nationally (Gallup, 2025) [EV-CAR-306].
- An insurer-commissioned poll reports 89% satisfied (AHIP, 2026) [EV-CAR-307]. That poll comes from an interested party.

**6. Disruption and political risk of moving about 157 million people** [EV-CAR-295].
- In September 2026, 52% favored Medicare for All even if it ended private insurers, up from 37% in 2020; 66% favored it in general (KFF, 2026) [EV-CAR-308].
- Opposition rose to 76% when people heard of possible delays in care, and to 64% when they heard of higher taxes [EV-CAR-308].
- Thirty-five percent prefer a single government system and 31% a mix (Pew, 2025) [EV-CAR-309].
- The risk is real and lower than in 2020. It is greatest for a required move. A move people can choose is easier to defend.

**7. Fiscal timing** (project arithmetic, 2032; `tools/employer_wave.py`).

| Group moving into the single plan | People today (millions) | Net federal cost when it moves | Change in national spending |
| --- | --- | --- | --- |
| Medicaid and CHIP | 70.7 | about +$1,095 billion | about +$760 billion (Medicaid's low rates rise to the plan's) |
| Medicare today | 70.8 | about +$886 billion | about +$110 billion |
| Employer groups | 169.5 | about +$753 billion | about **−$1,110 billion** (commercial prices, about 2.5 times Medicare's [EV-CAR-131], fall to the plan's) |
| The uninsured (newly covered) | 37.2 | about +$532 billion | — |
| Long-term care (model assumption) | — | about +$211 billion | — |
| Individual market | 19.7 | about +$73 billion | about −$140 billion |
| **All** | | **about +$3,549 billion (the model's single-plan figure)** | |

  - People counts are CBO's 2032 figures by source, before removing double counting, so they don't sum to the population.
  - The employer group is not where most of the federal cost sits. Its move costs $753 billion because the plan pays about $1.43 trillion for its care, less the $680 billion tax exclusion that ends.
  - Its move is also where national spending falls most: the price gap is the saving. That makes it the largest cut to hospital revenue, which is the strongest real reason for care in timing.
  - Memo 2's protection 4 keeps employers contributing until their workers move. A contribution of about 71% of today's employer premiums ($1.55 trillion in 2032) makes the move cost the federal budget nothing, net of the income and payroll tax the same money would raise as wages. At 80% the federal budget gains about $100 billion a year.
  - Caveat: on memo 5's glide path, rates are above the target in the early waves. Each 0.1 above 1.15 times Medicare adds about $115 billion a year (2032 terms) to the employer group's cost.

**8. Administrative capacity.**
- Medicare enrolled about 19 million people when it began in 1966, most of them already in Social Security's records (Social Security Administration) [EV-CAR-310].
- HealthCare.gov launched in 2013 without verification that it met its requirements (GAO, 2014) [EV-CAR-311], and recovered within 2 months (HHS Inspector General, 2016) [EV-CAR-312].
- The Medicaid unwinding struggled with the volume of renewals, systems and staffing (KFF, 2024) [EV-CAR-313].
- Employer groups are the easiest to enroll, from payroll records. But moving all of them at the endpoint puts about 170 million employer-covered people and about 71 million Medicare enrollees into the plan in one year, the largest enrollment event in U.S. history. Spreading the employer move lowers that peak.

**Verdict on memo 2's claim.** "Largest" is right. "Best-functioning" is only half right. Employer coverage is better than the individual market and well liked, but it leaves about three in ten underinsured, its cost comes out of pay, it ends with the job and it reaches lower-wage workers least. The good reasons to avoid forcing employer groups in early are the political risk of a required move and the hit to hospital revenue. With the employer contribution, fiscal timing is not one of them.

### Options, priced over FY2030-39 on the 2037 endpoint

Project arithmetic (`tools/employer_wave.py`):
- Wave 1 is the coverage model's staged path. Medicaid moves in 2034, the midpoint of memo 2's wave 2. Everyone else moves in 2037.
- Each group's 2032 cost is grown on the model's growth path, at the plan's target rate.
- "With contribution" subtracts an employer contribution, at the stated share of today's employer premiums, for groups that move before 2037.
- After 2037 every option is the same. FY2040 is about $5.5 trillion on every path.

| Option | FY2030-39 federal, before contribution | With a contribution at 71% / 80% of today's employer premiums | For it | Against it |
| --- | --- | --- | --- | --- |
| **A. Employers last** (memo 2 as decided) | about $20.4 trillion | the same (no one moves early) | The public plan gets a track record first. The smallest early political risk. Prices Medicaid's wave for the first time: memo 1's lower figure ($16.5 trillion on the model) plus about $3.9 trillion. | The employer-covered wait to 2037 for relief from deductibles and premiums. The endpoint carries the largest one-year enrollment and the full hospital-revenue shock. Its stated reason doesn't hold. |
| **B. Employer groups with Medicaid in wave 2** (2033-35) | about $23.1 trillion | about $20.4 / $20.1 trillion | Earlier relief for about 170 million people. The endpoint load and the hospital-revenue shock are spread. Close to the bill's pace. | A required move of employer plans in the mid-2030s: the largest political risk. The revenue cut lands mid-glide, while rates are still high. Employers must start paying the contribution by law. |
| **C. Voluntary early move from wave 2; everyone at 2037 (recommended)** | about $21.1 trillion at 25% take-up (range $20.7-21.5 trillion at 10-40%) | about $20.4 / $20.3 trillion | Employer groups can enroll whole, paying the transitional contribution, and individual workers can move with their employer paying it for them, as the bill lets employers into its Transition plan [EV-CAR-274]. Tests capacity on willing groups, spreads the endpoint, and keeps the move a choice until 2037. | Selection: firms with costly workforces join first. A contribution set as a share of each firm's own current premium should remove most of that (working assumption, to study in implementation). One optional step for employers. Take-up is a guess; at a contribution close to today's premiums it will be lower. |
| **D. Employer groups in wave 2, Medicaid at the endpoint** | about $19.2 trillion | about $16.5 / $16.2 trillion | The cheapest: employer moves pay for themselves and Medicaid's rate increase waits. | Leaves the lowest-income enrollees, in the program with the weakest provider access, for last. Against the plan's aims; shown for transparency, not recommended. |

**Recommendation: C.**
- It drops "best-functioning" as the reason and keeps what is real: no one is forced out of a plan they like before 2037, while employers and workers who want out can leave from 2033-35.
- With the contribution set at or above the federal-neutral share (about 71% on the model's treatment of the tax exclusion; the share itself is the financing settlement's), it costs about the same as A over FY2030-39. It also lowers the 2037 peak.
- It follows the design lens: no new test for people, and one payroll-based step for employers who choose it.
- If Espen prefers a single required date for employers, B with the contribution costs about the same; A remains defensible on political risk alone.

**What would change this:** a financing settlement that sets the employer contribution well below 71% (C's opt-ins would then add federal cost, and A becomes cheaper); evidence in wave 1 that the plan's capacity is short (slow C's opening); or a 2027-28 shift that makes a required employer move politically safe (B).

## (c) Memo 3: confirmed, with one addition

**B is confirmed.** The comparison shows the bill pools the same federal streams as memo 3 B: Medicare's non-premium funding, federal Medicaid, FEHB and other programs, plus the trust funds' balances [EV-CAR-287]. It also credits itself with the revenue from ending employer plans and the credits. It differs in asking nothing of states except for nursing homes [EV-CAR-278] and nothing of employers, and in levying no tax.

Memo 3 B's two extra streams survive the comparison:
- **States' share.** Without it, the bill lifts about $300 billion a year of states' Medicaid spending onto the federal budget (the coverage model's `sp_state_moe`). Nothing in the bill text says why states should keep that money.
- **The employer contribution.** It is what makes part (b)'s early moves affordable: at about 71% of today's premiums, employer moves cost the federal budget nothing.

**The addition:** name the revenue from ending the employer tax exclusion (about $680 billion in 2032 on the model) as a stream into the fund, as sec. 701 does. The model already counts it as an offset; memo 3's text does not name it. The amount left for new revenue is unchanged. This is a clarification for section 4, not a new choice.

**What would change this:** the financing settlement preferring one broad tax to an employer contribution (memo 3's own condition). Or a decision to hold states harmless, as the bill does. Either would raise the new revenue needed by the amount of the stream dropped.

## (d) For Espen

1. **Employer timing.** Let employer groups and workers move into the public plan voluntarily from 2033-35, with employers paying a contribution, and move everyone else at 2037 (recommended)? Or keep employers last, or move them all with Medicaid in 2033-35? On our estimates all three cost about $20 trillion over 2030-39 if employers keep paying about 71% or more of what they pay in premiums today (the financing settlement sets that share); without it, the 2033-35 options cost about $21-23 trillion.
2. **Memo 3.** Confirm B (keep the public money, states' share, employer contribution), adding the revenue from ending the employer tax break as a named source, as the Sanders bill does? Recommended: yes.
3. **People on Medicare now.** Give them the legacy upgrades (an out-of-pocket cap, then hearing, vision and dental) from 2031, rather than waiting until they join the single plan in 2037? Recommended: yes. The Sanders bill does it in year one. Legacy priced the upgrades at $0.9-1.2 trillion over 2030-39 (`legacy/domains/domain-health.md`, HLT-2).
4. **Abortion and reproductive care.** Cover them in the benefit, with federal funding limits not applying to the health fund, as both bills do? Recommended: yes. The project hasn't decided it yet.

## Evidence still needed

- Employer coverage by race and ethnicity (Census table H-04).
- A post-ACA measure of coverage loss after job loss (Census SIPP).
- The cost of ending the disability waiting period and of guaranteed-issue Medigap (CBO).
- The trade-adjustment record, to price worker assistance (protection 2) in section 6.
