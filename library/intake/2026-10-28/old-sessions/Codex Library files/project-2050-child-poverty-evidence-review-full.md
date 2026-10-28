# Project 2050 Child-Poverty Evidence Review

## Deliverables and authority baseline

The authoritative branch was verified before the substantive assessment: `fm58cn6g4d-stack/project-2050`, branch `claude/pensive-mendel-g1lwl5`, at commit `e15c5c4a711b4cd2b482bac8300de45f2e08721f`. The repository's shared instructions make the approved GitHub governing document authoritative over external Claude artifacts, Google Docs, exports, and unmerged proposals, and they reserve policy decisions to Espen. I did **not** substitute `main`. fileciteturn2file0 fileciteturn10file0

The two requested deliverables are complete:

[Download `project-2050-child-poverty-evidence-review.md`](sandbox:/mnt/data/project2050_outputs/project-2050-child-poverty-evidence-review.md)

[Download `project-2050-child-poverty-design-implications.md`](sandbox:/mnt/data/project2050_outputs/project-2050-child-poverty-design-implications.md)

The adopted-policy reading comes from the fixed-commit governing decisions and canonical family, education, housing, options-register, consistency-report and incidence-model files. FAM-1A is $3,600 for children under six and $3,000 for ages six through seventeen, fully refundable, monthly and indexed; FAM-2A phases from pre-K plus free care below 75 percent of state median income into a 7-percent-of-income cap through 250 percent of state median income from 2032; EDU-3A provides universal school breakfast and lunch plus a larger Summer EBT benefit; and HOU-4A adds 400,000 mandatory Housing Choice Vouchers rather than establishing a rental-assistance entitlement. fileciteturn11file0 fileciteturn12file0 fileciteturn13file0

I found no basis to change the October 23 approved baseline. The repository's approved branch already contains the relevant authority and capacity work. The existing Project incidence model is useful for household net-incidence checks but expressly says its distribution shares are estimates and that it is **not a microsimulation**; it therefore cannot answer how many children remain below the SPM threshold. fileciteturn16file0 fileciteturn17file0

Three requested saved materials were not independently retrievable through the connected sources available in this run: the external approved-charter file named in the handoff, the saved bibliography/report, and Espen's saved writing-guide file. Their descriptions in the handoff were treated as leads rather than primary authority. The requested `$deep-research` app connector also was not exposed as an invokable connector in this session, so I did not represent it as having run; the research was done directly against the authoritative GitHub branch and primary web sources. The attached preliminary reports were used to identify questions, not as conclusions to ratify. fileciteturn0file0 fileciteturn0file1 fileciteturn0file2

## Bottom-line assessment

**The adopted package has a strong evidentiary basis for a large reduction in child poverty. It does not have a defensible evidentiary basis for claiming eradication or near-eradication.** My confidence is high in the first sentence and high that a Project-specific residual rate is presently unknown. I have medium-high confidence in the stronger inference that literal near-zero child SPM poverty is **implausible under the package as currently specified**, rather than merely “not yet demonstrated.”

That conclusion follows from the closest National Academies analogues, not from transferring their scores. In the 2019 *Roadmap*, an unconditional $3,000 monthly child allowance reduced the committee's adjusted child SPM rate by about 5.3 percentage points from a 13.0 percent baseline—roughly a 41 percent reduction, leaving about 7.7 percent by subtraction. Broader packages reached approximately a 50 percent reduction only by combining child benefits with large expansions of housing, SNAP, earnings supports, child support and, in one package, immigrant eligibility. The Roadmap modeled those packages jointly and explicitly warned against treating component effects as additive. Its population was 2015 and its tax-law baselines were 2015/2018, not Project 2050's 2030s environment. citeturn4search1turn4search0turn5search0turn5search1

The 2026 *Pathways* report provides the closest tax-credit analogue. Its PO12 uses the same $3,000/$3,600 maxima, covers children under eighteen, and removes the CTC earnings requirement. But it uses 2018 CPS ASEC data expressed in 2021 dollars, starts from a non-ARPA EITC plus approximately TCJA-era CTC baseline, pairs the CTC with the EITC, and imposes a faster phase-out beginning at $75,000 for heads of household and $110,000 for married couples. It is therefore not FAM-1. In that simulation, child poverty falls from 11.1 percent to 6.5 percent with no employment response; under the committee's low, medium and high employment-response assumptions it is roughly 7.0, 7.2 and 7.4 percent. citeturn22view2turn22view1

Those results establish an **evidence corridor, not a Project score**:

| Evidence case | Population and baseline | Policy | Result | Proper use here |
|---|---|---|---|---|
| 2019 NASEM child allowance | 2015 population; adjusted SPM 13.0%; 2015/2018 tax-law variants | $3,000 monthly allowance with its own eligibility/replacement rules | −5.3 percentage points | Evidence that unconditional per-child cash at this scale is powerful |
| 2019 NASEM broad packages | Same underlying population/model | Cash plus housing/SNAP/work supports and other changes | About 50% reduction for leading packages | Evidence that closing more of the residual requires multiple jointly modeled instruments |
| 2026 NASEM PO12 | 2018 population; approximate TCJA/non-ARPA baseline | $3,000/$3,600 no-earnings CTC plus EITC, faster phase-out | 11.1% → 6.5% before employment response; about 7.0–7.4% with behavior | Closest evidence on benefit adequacy and behavioral uncertainty |
| Project 2050 | 2030s population and post-2025 law not yet microsimulated | FAM-1A + delivered FAM-2/EDU-3/housing + other adopted household policies | **Unknown** | Must be estimated directly |

The historical 2021 result does not fill that blank. Census's child SPM rate reached 5.2 percent in 2021, but that year combined the expanded CTC with stimulus payments, expanded unemployment benefits, nutrition assistance and other pandemic-era policies. *Pathways* finds that the estimated CTC contribution changes materially with the counterfactual and with whether credits are allocated to their accrual year or actual receipt year. The 2021 low therefore cannot be called “the FAM-1 poverty rate.” citeturn10search0turn15view2

The current observed child SPM rate is also only a reality check, not a Project baseline: Census reported 13.4 percent for children in 2025. A proper 2030/2034 counterfactual must project the population, thresholds, post-2025 tax law and transfer system rather than simply applying a percentage reduction to 13.4. citeturn15view0

## Why the adopted package leaves a residual

The central finding is that the likely residual comes from four distinct mechanisms: **legal exclusion, nonreceipt, inadequate resources even after receipt, and failure to convert nominal service eligibility into an actual service.** Treating all four as “the CTC isn't big enough” would point to the wrong design choices.

### FAM-1 is powerful at the bottom, but it is not an income floor

Full refundability is the strongest feature of the adopted design. A family with zero earnings can receive the full statutory FAM-1 amount rather than being shut out by an earnings phase-in. Both National Academies reports show why this matters for deep poverty. But a fixed per-child amount does not guarantee total family resources above an SPM threshold. Rent, adult count, family size, work expenses and medical expenses vary; the same $3,000 can close one family's gap and leave another far below it. citeturn4search1turn22view2

The 2026 subgroup results make that residual concrete. Under PO12, the overall modeled rate is 6.5 percent before employment response, but the rate remains about 37 percent among children in families with no workers and about 12 percent in units containing a nonelderly person with a disability. Single-parent and cohabiting-parent families remain around 11 and 10 percent respectively, well above married-parent families. These figures are not Project predictions; they show why the same nominal child benefit does not erase poverty uniformly. citeturn8view1turn8view2

Family size cuts another way. Because the credit is per child while the SPM threshold rises less than proportionately with each additional child, the *Pathways* model finds substantially stronger proportional poverty reduction among larger families than among one-child families. A one-child family with very low earnings and high rent is therefore one plausible residual case even with perfect FAM-1 receipt. citeturn8view2

### Immigration rules create a real coverage boundary

The canonical FAM-1 text creates a consequential specification problem by saying both that it “builds on current law” and that FAM-1A is the “full 2021 design.” fileciteturn11file0

Those phrases are not equivalent for adult claimant identification. Under the 2021 expanded CTC, adult filers could generally use an SSN or ITIN while the qualifying child still needed the required SSN; current post-2025 IRS instructions impose a claimant/spouse SSN condition as well as the qualifying-child SSN condition. FAM-1's text does not expressly resolve which adult rule survives. citeturn16search0turn16search1turn16search12

The child rule is less ambiguous: adopting the “2021 design” alone does not include children lacking the qualifying SSN, because the 2021 credit itself generally retained that child-SSN requirement. Unless another canonical provision overrides it, those children remain a likely **legal exclusion**, not a take-up problem. citeturn16search0turn16search12

This matters because *Pathways* finds exceptionally high residual poverty among mixed-status and noncitizen groups and separately models extension to children without SSNs and to parents without SSNs. Under PO12, for example, poverty remains far higher for foreign-born children and several mixed-status groups than for all-citizen families; explicitly broadening SSN eligibility reduces those disparities. Again, that is evidence for the mechanism, not a Project score. citeturn8view3turn7view3

Territorial treatment, main-home/residency requirements, custody transitions, newborn updates and reconciliation rules are also not fully specified in the FAM-1 canonical prose. These should be treated as **specialist drafting questions** rather than silently resolved in a poverty model. fileciteturn11file0

### “Monthly” only matters if the money reliably arrives monthly

FAM-1's monthly design is an important adopted strength, and the family file explicitly seeks standing disbursement authority so a shutdown does not stop payments. fileciteturn11file0

But legal entitlement, annual receipt and twelve reliable payments are different things. The National Academies take-up review identifies filing requirements, limited information, language and digital barriers, qualifying-child complexity, custody changes and IRS administrative data as sources of nonreceipt. Such barriers are not evenly distributed; many are concentrated among lower-income and immigrant families. The committee therefore cautions against treating statutory eligibility as empirical 100-percent receipt. citeturn17search0

The 2021 rollout illustrates both the potential and the limitation. Only half the annual expanded credit was scheduled for advance payment during July–December, with the remainder reconciled later, and *Pathways* produces a higher poverty estimate when it assigns tax credits to the year cash was actually received rather than the year of accrual. That is direct evidence that a Project model should represent payment timing rather than merely divide an annual award by twelve. citeturn10search0turn16search10turn16search11

The canonical Project design does not yet specify a permanent non-filer pathway, proactive enrollment, offline and multilingual filing assistance, rapid birth/custody updates, failed-payment replacement, correction timelines or the precise safe harbor/reconciliation architecture. That is best classified as **missing delivery analysis**, not evidence that the program will fail. fileciteturn11file0

### FAM-2 helps only when an actual care slot exists

FAM-2A is an expense-reduction and service policy, not another cash benefit. The relevant poverty effect for a family is the reduction in its actual out-of-pocket child-care cost conditional on obtaining usable care; any increase in parental earnings is a separate channel, and child-development effects are longer-run. fileciteturn11file0

The canonical family file sensibly responds to supply risk with phased implementation, supply grants and wage parity. It also states, however, that this phased baseline was selected by the file author rather than taken from a separate Espen decision. FAM-2A remains the canonical chosen row at the approved commit, but that sentence is an **authority/provenance issue to preserve**, not a license for the research review to replace FAM-2A with a different option. fileciteturn11file0

Existing CCDF experience demonstrates the difference between eligibility and actual service: GAO found roughly 1.8 million children receiving subsidies in 2021, about 15 percent of those eligible under federal rules; in 2019, roughly 2 million of nearly 8.7 million federally eligible children received subsidies. Project 2050 is deliberately much more ambitious and finances supply, so those percentages are not take-up forecasts for FAM-2. They are evidence that a model that grants every income-eligible family the full theoretical child-care saving would be structurally optimistic. citeturn20search13turn20search15

The hardest access cases are likely to include infant/toddler care, disability-accessible care, rural or Tribal care, nonstandard work hours and places where the workforce ramp lags the subsidy. The poverty model therefore needs a **realized-slot parameter**, not merely the 7-percent statutory cap.

### EDU-3 substantially reduces food burden without becoming unrestricted cash

EDU-3A's universal school breakfast and lunch is a high-reach adopted in-kind benefit for enrolled students, and the $60 monthly Summer EBT expansion addresses a genuine seasonal gap. fileciteturn12file0

Summer delivery nevertheless needs its own receipt assumptions. Under the existing federal Summer EBT framework, many children are automatically enrolled through SNAP, TANF or school-meal eligibility, while others must apply, and actual availability depends on participating states, territories and Tribes. USDA's national summer-meals work identifies lack of awareness as the most frequent reason for nonparticipation among families living near summer meal sites. citeturn20search4turn20search5

That makes “universal school meals” and “universal year-round food support” different claims. Unless Project 2050 explicitly rewrites the Summer EBT eligibility/participation architecture, the simulation should not assume the latter.

There is also a smaller canonical basis issue: EDU-3A says reimbursement is at current free-meal rates, indexed, while the cost discussion separately examines higher Senate rates. That should be reconciled for costing and capacity purposes, but it does not change the adopted universality of school-year meals. fileciteturn12file0

### Housing is probably the largest non-CTC reason the residual cannot be assumed away

The housing package combines very different channels. HOU-1 is temporary 2030–31 aid. HOU-4A creates 400,000 additional vouchers, phased in through 2033. HOU-3C's state revolving funds and $300 billion of federal direct-loan commitments, LIHTC changes, public-housing repair and supply incentives act through construction, preservation and rents over longer horizons. Treating all those budget dollars as if they entered poor families' SPM resources immediately would be a serious category error. fileciteturn13file0 fileciteturn14file0

The decisive point is that HOU-4A is still **rationed**. The canonical file explicitly keeps a broader entitlement for extremely-low-income renters as HOU-4C, an option rather than the chosen design. Poor renter families outside the 400,000 additional awards therefore do not receive a recurring rent subsidy merely because Project 2050 spends heavily on housing. fileciteturn14file0

And even receiving a voucher is not identical to leasing with one. HUD's historical research summarized voucher success around 69 percent in one national study, lower in tight markets and higher where source-of-income protections were present; experimental housing evidence also finds substantial homelessness reductions for families that successfully lease with assistance. The exact historical figures should not be transplanted to 2030, but the mechanism is clear enough to require lease-up, local vacancy, landlord participation and PHA capacity in the simulation. citeturn21search16

## Material hardship, deep poverty and labor-supply uncertainty

A headline SPM rate is not enough to evaluate the package. Monthly cash can reduce food insecurity or utility hardship even when a family's annual resources remain below the poverty threshold. Conversely, a child whose annual resources cross the line can still experience a missed-payment month, eviction risk or food insufficiency. The policy should therefore be evaluated separately on annual poverty, poverty depth, monthly liquidity and material hardship.

Subsequent causal work on the 2021 advance CTC supports this separation. Parolin and coauthors estimate a sizable reduction in food insufficiency among lower-income households with children after monthly payments began; Pilkauskas and coauthors find reductions in multiple hardships among very-low-income families. These are temporary-program, pandemic-period results and do not establish the annual Project poverty rate, but they strengthen the case that reliable monthly payment has welfare effects beyond an annual SPM headcount. citeturn18search3turn18search9

The short-run employment evidence is substantially less alarming than the strongest ex ante critiques. Ananat and coauthors and Enriquez, Jones and Tedeschi find little evidence of a broad short-run employment reduction from the 2021 CTC. citeturn18search2turn18search7

But a permanent program is a different question. Corinth and coauthors obtain much larger labor-supply losses and consequently much smaller poverty reductions when they impose relatively large employment responses, while Bastian's published permanent-CTC simulation finds a much smaller employment decline and still substantial reductions in poverty and deep poverty. The 2026 National Academies committee reviewed this disagreement and chose a range of low, medium and high employment elasticities rather than treating either zero response or the most pessimistic estimate as settled. citeturn19search0turn18search0turn22view1

That is the appropriate approach for Project 2050. **Do not bury an employment assumption in the baseline.** Report no-response and National Academies-style low/medium/high cases. Child-care-induced employment gains belong in a separate scenario because simply adding a positive FAM-2 labor estimate to a negative FAM-1 estimate would combine models, populations and overlaps that were never jointly estimated.

Longer-run child-development, health, educational and adult-earnings effects should likewise be reported separately from current child poverty. Evidence suggests income support in childhood can produce downstream benefits, but those effects are not dollars available to a child in the SPM resource unit in 2034. They can strengthen a long-run social-return case without being used to make a present-day poverty rate disappear. citeturn19search3turn19search8

## Most consequential design choices

The evidence distinguishes **adopted policies**, **findings**, **analysis proposals**, **record conflicts**, and **specialist questions**.

| Item | Status | Evidence implication |
|---|---|---|
| FAM-1A amount/full refundability/monthly/indexed | **Adopted** | Strong antipoverty design, especially at zero earnings; still not an income guarantee |
| Adult claimant SSN treatment | **Conflicting/underspecified record** | “Full 2021 design” and “builds on current law” plausibly imply different rules; resolve or model both |
| Child SSN treatment | **Likely adopted exclusion unless overridden elsewhere** | 2021 rules themselves generally required the child's qualifying SSN |
| Non-filer/proactive enrollment/payment repair | **Missing delivery design / proposal for comparison** | Could close eligible-nonrecipient gaps without increasing the statutory benefit |
| FAM-2A | **Canonical chosen design with provenance caveat** | Poverty effect must be conditioned on actual slot availability |
| EDU-3A school meals | **Adopted** | Broad in-kind school-year support |
| Summer EBT automatic/jurisdictional reach | **Underspecified** | Requires a distinct participation assumption |
| HOU-4A 400,000 vouchers | **Adopted** | Important for recipients but structurally incapable of being universal |
| HOU-4C voucher entitlement | **Filed alternative, not adopted** | Probably among the largest direct alternatives for high-rent residual poverty |
| Larger CTC/FAM-1D | **Filed alternative, not adopted** | Addresses benefit inadequacy but spends broadly and does not cure exclusion/nonreceipt |
| Residual-income supplement | **Illustrative proposal only** | Would directly target recipients who remain poor, but creates a new means-tested instrument |

The highest-value **first comparison** is probably not “how much larger should FAM-1 be?” but a decomposition of the residual into children who are excluded, eligible but not receiving, full recipients who remain poor, and families whose service eligibility does not produce an actual care/food/housing service.

That decomposition then makes the policy choices legible:

A child excluded by an SSN rule is not helped by better take-up. An eligible non-filer is not necessarily best helped by raising the benefit for millions of existing recipients. A zero-income renter already receiving the full CTC but still far below the SPM threshold has an adequacy/housing problem. A parent facing a nominal 7-percent child-care cap but no infant slot has a supply problem. A family with a voucher that cannot lease has a housing-market/delivery problem.

Among alternatives, the 2026 National Academies evidence makes **broader SSN eligibility** unusually targeted to groups with high residual poverty. citeturn8view3turn22view2

A **larger FAM-1**, including the filed FAM-1D direction, is the cleanest response to benefit inadequacy; the National Academies simulations consistently find larger maximum credits produce larger poverty reductions. But *Pathways* also finds that only a relatively small share of broad CTC fiscal outlays goes to children who are actually below the poverty line, which is why a benefit increase should be compared on poverty-gap reduction per dollar rather than gross transfer size. citeturn22view2

A **broader voucher entitlement**, such as the unchosen HOU-4C, attacks a different residual that a per-child cash credit cannot perfectly target: very high rent burdens among extremely-low-income renters. The 2019 Roadmap's roughly 50-percent packages relied on much more comprehensive housing/SNAP support than Project 2050's adopted 400,000-voucher expansion, which is one reason it would be unwarranted to transfer those package reductions to Project 2050. citeturn4search0 fileciteturn14file0

A **residual-income supplement** is analytically attractive because it could target the remaining poverty gap rather than increasing every child's credit. It is not an adopted Project policy, and this review assigns it no amount, eligibility formula or financing. It should remain an illustration until a baseline simulation shows who the full-credit residual actually is.

## Minimum microsimulation required before publishing a residual rate

The minimum useful model is not a general audit of Project 2050 and does not require full dynamic general equilibrium. It does require a household-level SPM microsimulation that jointly represents the adopted policies rather than distributing program costs across income quintiles.

| Model element | Minimum requirement |
|---|---|
| Population | Named recent CPS ASEC/SPM microdata, aged or reweighted to the implementation year; document benefit-underreporting corrections |
| Counterfactual | Actual post-2025 current law projected to the modeled year, not 2018 TCJA law and not the exceptional 2021 pandemic baseline |
| Timing | At least **2030 transition** and **2033–34 mature-service** results |
| SPM mechanics | Correct resource units, geographic and housing-tenure thresholds, taxes, refundable credits, SNAP/housing resources, work/child-care expenses and medical out-of-pocket deductions |
| FAM-1 | Exact benefit/indexing, age, phase-out, child/adult SSN, residency/territory, custody, newborn, advance-payment, reconciliation and safe-harbor rules |
| Receipt | Full statutory receipt; realistic delivered receipt; enhanced-delivery scenario |
| Payment reliability | Monthly timing and interruptions distinct from annual entitlement |
| Employment | No-response plus NASEM low/medium/high sensitivities |
| FAM-2 | Actual out-of-pocket reduction conditional on a usable slot; age, disability, hours, geography and state/Tribal capacity |
| EDU-3 | School-meal participation and Summer EBT eligibility/take-up modeled separately |
| Housing | Existing assistance in baseline; allocate 400,000 incremental HOU-4 vouchers to eligible households; model lease-up; keep HOU-1 temporary |
| Housing supply | HOU-2/HOU-3/HOU-6 rent effects as a separate, lagged market scenario rather than household cash |
| Whole-package boundary | Include household-facing Project taxes/fees that change SPM resources if the result is called the “Project 2050 package”; otherwise label it a focused family/housing simulation |

The required outputs should go beyond one rate. At minimum, report child SPM poverty, deep poverty below 50 percent of the threshold, near poverty, poverty-gap dollars and a poverty-severity measure, all in rates and child counts. Then report the residual by family structure, child age, number of children, zero/low earnings, disability, citizenship/nativity/SSN status, housing tenure, geography, race/ethnicity and major-program receipt.

Most important, produce a **mutually exclusive residual decomposition**:

**legally excluded → legally eligible but nonreceiving → receiving full FAM-1 but still poor → reached by FAM-1 but missing an available care/food/housing service → no longer poor.**

That decomposition would answer the actual design question much more cleanly than an aggregate percentage.

The first validation exercise should reproduce at least one 2019 Roadmap case and the 2026 Pathways baseline/PO12 closely enough to explain differences. Only after the tax units, SPM units, underreporting adjustment and interactions benchmark correctly should the model substitute Project 2050 rules. That prevents a superficially precise Project estimate built on an unvalidated poverty engine. citeturn5search1turn22view2

## Limits and handoff

The preliminary research hypothesis survives scrutiny, but in a sharper form: **large poverty reduction is well supported; near-eradication is not.** The most likely residual is not one homogeneous population. It consists of children legally excluded from FAM-1, eligible children missed administratively, full-credit recipients whose total resources remain inadequate, low-income renters who do not receive one of the 400,000 added vouchers, families unable to obtain the child-care service their nominal subsidy promises, children with disability-related constraints, and children whose food support becomes less reliable outside the school year. citeturn8view1turn8view3turn17search0turn20search4 fileciteturn11file0 fileciteturn14file0

The most important unresolved **record question** is FAM-1's adult-SSN/ITIN treatment. The most important **missing analysis** is the child-level joint microsimulation. The most important **design weakness** for a literal eradication objective is that the adopted package contains no universal residual income floor and no universal rental-assistance guarantee. The most important **delivery questions** are reliable monthly CTC receipt, usable child-care supply, summer nutrition enrollment and voucher lease-up.

The most consequential alternatives to test, without adopting them, are therefore enhanced FAM-1 enrollment/payment administration; broader adult and/or child SSN eligibility; FAM-1D or another larger maximum; a separately specified residual-income supplement; HOU-4C or another broader recurring rental entitlement; stronger guarantees that FAM-2 eligibility translates into actual care; and more automatic summer food delivery. They should be compared one at a time and jointly only where interactions are explicitly modeled.

No Project policy, canonical file, cost estimate or model input was changed. The research artifacts are the two markdown files above. The next decision-quality step is **not another general literature sweep**: it is to resolve or branch the few genuinely ambiguous eligibility/delivery rules and run the minimum microsimulation. Until that is done, the most defensible Project 2050 characterization is **“a package likely to cut child poverty substantially and reduce material hardship, but not one presently shown—or, on the available evidence, plausibly expected—to drive child SPM poverty close to zero.”**