# Care you can count on, part B (care at home for all ages): design choices

Role: section 3 of the care dossier, part B: the real forks, the options weighed, a recommendation for each, one decision memo per fork in `memos/` (memos 6-9), and a numbered list of narrower yes-or-no points. Status: draft (stage D, step 5); **for Espen, none decided**. It builds on health's decided path: a staged path to one public plan, with every resident covered by January 1, 2035 (`DEC-2026-11-10-09`, `-11`, `-12`, `-13`, `DEC-2026-11-11-01`). Under that path long-term care stays in Medicaid until this part decides (`4-specification.md`, HLT-7.07). Sources are named in plain text in the points and memos; bracketed tags point to `evidence.json`.

## How to read this section

- **One batched set.** Four memos and ten yes-or-no points, so Espen can answer once. Memo 6 shapes the rest; memos 7-9 say how each answer applies under each of memo 6's options. Each is decided on its own, and none is adopted by silence.
- **Legacy designs are options** (`DEC-2026-10-30-02`).
  - The October 26 legacy direction asked for an all-age home-support benefit (`legacy/domains/domain-health.md`, line 137). It specified protection against prolonged intensive-care costs, assessed help without asset spend-down, a genuine paid-family-caregiver option, and preservation of stronger Medicaid services, compared with enhanced Medicaid and catastrophic-only insurance. It appears here as memo 6 B, weighed against both.
  - The legacy HLT-4 "HCBS down payment" (enhanced Medicaid matching plus workforce support) is memo 6 A and the bridge in point 1.
- **Health's working position on institutional care is an option, not a given.** S. 1506 keeps institutional long-term care in Medicaid (sec. 204) [EV-CAR-278], and so does health's HLT-7.07 for now. Memo 8 weighs keeping it there against moving all or part of it into the plan.
- **Report, don't gate** (`DEC-2026-11-10-05`). Each option's cost is reported for the financing settlement as a working assumption with its basis and range (`DEC-2026-11-10-07`); nothing is trimmed to fit. Memo 6 is mainly about money and reaching people, so it comes to Espen with its cost. The budget model books part B only after sections 4-6.
- **Design lens** (`DEC-2026-11-09-13`). Each option says what it asks of people: forms, tests, waiting.

## The baseline in 2029

Section 1, part 6, gives the full baseline:
- **Medicaid.** Medicaid is the only broad payer, after spend-down to SSI's $2,000 asset limit [EV-CAR-409]. Home care is mostly an optional waiver service with enrollment caps, so almost 650,000 people wait 34 months on average [EV-HOU-691].
- **The 2025 law.** It cuts retroactive coverage from 2027 [EV-CAR-418], caps home equity at $1,000,000 from 2028 [EV-CAR-415], adds a lower-need waiver option from July 2028 [EV-CAR-414], and suspends nursing-home staffing standards to September 2034 [EV-CAR-416].
- **Expirations.** Money Follows the Person and the home-care spousal protections expire after FY2027 [EV-HOU-697].
- **The 2024 access rule.** Its 80% worker-pay rule (from July 2030) and waiting-list reporting (from 2027) may be rescinded [EV-CAR-419] [EV-CAR-420].
- **Health's plan.** Medicaid enrollees join the single plan in 2033-35, but their long-term care stays in Medicaid (HLT-7.07).

## The forks at a glance

| Fork | Memo | Options | Recommended |
| --- | --- | --- | --- |
| 6. How care at home is guaranteed | `memos/6-home-care-guarantee.md` | A stronger Medicaid (legacy HLT-4); B an all-age home and community care benefit in the single plan from 2035, no asset test (legacy October 26 direction; S. 1506 sec. 201); C public catastrophic insurance after a waiting period, Medicaid for the rest | **B** |
| 7. Who qualifies and how much the benefit covers | `memos/7-benefit-scope.md` | Part 1, the need threshold: A two daily activities or equivalent; B one (House bill); C three (WA Cares). Part 2, depth: A full assessed need, no cap; B set budgets by need tier, high enough for intensive need at home; C a basic allowance | **Part 1 A; part 2 B** |
| 8. Nursing homes and other institutional care | `memos/8-institutional-care.md` | A stays in Medicaid with a state floor (S. 1506 sec. 204; health's working position); B stays in Medicaid with federal protections against impoverishment; C the plan pays the care part from 2035, residents pay room and board from income with a protected allowance; D the plan pays all of it (House bill) | **C, with B's protections in the bridge** |
| 9. Family caregivers | `memos/9-family-caregivers.md` | A paid through self-direction at the benefit's rates, spouses and parents included, plus respite and training; B A plus a cash option; C services only; D a caregiver tax credit | **A** |

## What the options cost

These are working assumptions with their basis and range (`DEC-2026-11-10-07`), not a model run. Sections 4-6 price the decided design on the coverage model, whose single-payer variant assumes $200 billion a year for all long-term care (range $100-400 billion; `models/tools/health-coverage/MODEL-CARD.md`). The estimates below put home care alone at about that level, so section 6 must reconcile the two.

**The basis (project arithmetic, judgment where marked).**
- **Medicaid spending.** Medicaid long-term care was $257.0 billion in 2023 (CRS, 2025) [EV-CAR-404], 63.8% of it for home care (CMS, 2025) [EV-CAR-406]: about $164 billion for home care and $93 billion for institutions.
- **Users.** The 2022 cost per home-care user was about $16,600, from $129.4 billion for 7.8 million users [EV-CAR-407].
- **States' share.** States pay about 47 percent [EV-CAR-448].
- **Growth (working assumption).** Spending grows 5.5% a year in nominal terms, range 4.5-6.5%, from wage growth and a population 85 and older that nearly doubles by 2040 [EV-CAR-403]. This multiplies 2023 spending by about 1.9 by 2035.
- **States' maintenance of effort.** States keep paying half of what they now spend on whatever moves to the plan, as health's working figure for the rest of Medicaid (`4-specification.md`, HLT-7.17; range 0-80%, set by the financing settlement).
- **New users (judgment).** Three to five million people of every age, not now served by Medicaid, who meet memo 7's threshold and use paid care. Their average cost is $12,000-20,000 in 2022 dollars, below Medicaid's average because family care continues alongside it. The basis is ASPE's 7.2 million older adults with significant disabilities in 2020 [EV-CAR-402], against about 3.2 million Medicaid home-care users 65 and over (40.5% of 7.8 million) [EV-CAR-408] [EV-CAR-407], and Urban's finding that nearly two-thirds of older adults who get help get only unpaid help [EV-CAR-448].

| Option | New federal cost in 2035, first full year ($ billion) | Main pieces | FY2040 permanent cost (about) |
| --- | --- | --- | --- |
| Memo 6 A, stronger Medicaid | about 45 (35-70) | 10-point match increase on home care, about 31; states must serve everyone eligible, which ends waiting lists, with a federal share of about 13; resource limits updated, 2-5 (judgment) | about 60 |
| **Memo 6 B, home benefit in the plan** (memo 7 A and B) | **about 215 (125-370)** | Relief of states' home-care share net of maintenance of effort, about 73 (29-147); waiting lists served, about 22; new users, about 120 (72-201). Federal Medicaid home-care money, about $165 billion, moves in as a transfer and is not counted as new | **about 280 (165-485)** |
| Memo 6 C, catastrophic insurance | about 100-200 (judgment; Urban finds front-end and catastrophic benefits cost about the same [EV-CAR-446]) | The front end stays with Medicaid and families, and so do the waiting lists unless A is added | about 130-260 |
| Part D wage floor, if it raises home-care pay 20% (part D's decision) | about 55 on top of 6 B | 20% on the labor share (about 60%, judgment) of the benefit | about 70 |
| Memo 8 C, the care part of institutional care in the plan | about 50-90 | States' institutional share net of maintenance of effort; the care part (60-70%, judgment) of private-pay stays for the roughly 23% of residents whose primary payer is neither Medicaid nor Medicare [EV-CAR-438], at CareScout's $114,975 [EV-CAR-437] | about 65-120 |
| Memo 8 D, all institutional care in the plan | about 80-140 | C plus room and board | about 105-185 |
| Point 1, the bridge, FY2030-34 | about 24 a year in 2030; about 0.13 trillion over FY2030-34 | 10-point match on about $239 billion of home care in 2030 | ends 2034 |

- **Over FY2030-39**, the recommended set adds up as follows, roughly, in calendar years; section 6 converts to fiscal years:
  - the bridge, about $0.13 trillion;
  - memo 6 B from 2035, about $1.2 trillion (range $0.7-2.1 trillion);
  - memo 8 C from 2035, about $0.3-0.5 trillion;
  - in total, about $1.6-1.8 trillion before any part D wage floor.
- **Checks against outside estimates.** Urban and CBO both expect single-payer long-term care to add "hundreds of billions of dollars" a year in federal cost [EV-CAR-448]. CBO put a 2021 home-care match increase at about $150 billion over ten years (KFF, 2021) [EV-CAR-447], in line with option A's scale.
- **Who pays now.** Most of 6 B's cost replaces what families now pay out of pocket or give unpaid [EV-CAR-401] [EV-CAR-436]. It is a shift to public money as well as new care. Who pays the new taxes is the financing settlement's decision (Codex), not this part's.

## Recommended without a memo: ten yes-or-no points

Each is decided on its own. None is adopted by silence. Costs are judgment unless an evidence tag gives them.

1. **The bridge, 2030-34: a temporary 10-point increase in the federal match for Medicaid home care**, the legacy HLT-4 "down payment." It is paid on three conditions: states keep their own spending, cut their waiting lists by half by 2033, and pass the increase into rates and workers' pay. It ends when the benefit starts in 2035, or, under memo 6 A, it becomes permanent. *Why:* ARPA's one-year increase showed states put such money into the workforce, but temporary money buys one-time gains (MACPAC, 2026) [EV-CAR-425]. Five years tied to the 2035 start lets states hire and train ahead of the benefit. *Cost:* about $24 billion in 2030, about $0.13 trillion over FY2030-34. *Burden:* state reporting the access rule already requires [EV-CAR-432]. **Recommended: yes.**
2. **Make Money Follows the Person and the home-care spousal protections permanent from FY2028**, in a 2027-28 extender if one moves (a 2027-28 exception) or in the first 2029 bill. They fold into the benefit in 2035. *Why:* the program has moved 127,184 people since 2008 (CMS, 2025) [EV-CAR-421], with quality-of-life gains and lower spending for those who left nursing homes (CMS report to Congress, 2017) [EV-CAR-429]. Both expire after FY2027 (CMS, 2024) [EV-HOU-697]. *Cost:* about $0.45 billion a year for the program [EV-HOU-697]. **Recommended: yes.**
3. **No estate recovery for correctly paid Medicaid, from 2030** (S. 1506 sec. 205) [EV-CAR-431]. *Why:* recovery brought in about $733.4 million in FY2019, only 0.55 percent of fee-for-service long-term care spending, and falls on modest estates (MACPAC, 2021) [EV-CAR-410]. *Cost:* the federal share of what states recover, under $0.5 billion a year (judgment from MACPAC's total). *Burden:* it removes a burden from families. **Recommended: yes.**
4. **Raise the SSI-linked resource limits that Medicaid long-term care uses** to the S. 1506 levels, $4,100 for an individual and $6,200 for a couple, then index them [EV-CAR-431]. Repeal the 2025 law's $1,000,000 home equity cap [EV-CAR-415]. Both apply from 2030 until the benefit replaces the asset test. *Why:* the $2,000 limit [EV-CAR-409] forces people to impoverish themselves first. *Owner:* the SSI limit itself belongs to the secure floor (flagship 1). This point asks only that Medicaid's long-term care test use the higher figure, whatever SSI does. *Cost:* small, a few billion dollars a year (judgment). **Recommended: yes.**
5. **Services that make housing work (shared rule 7, which care owns): include tenancy-sustaining services, housing navigation and assertive community treatment** in the home benefit from 2035, and as covered home-care services states may claim under the bridge's match. *Why:* housing asked for this (`dossiers/home/4-specification.md`, HOU-4.12), since waivers must now be budget neutral (Public Law 119-21) [EV-HOU-337] and CMS withdrew its housing-services guidance [EV-HOU-339]. Housing's HUD backstop for tenants whose state Medicaid does not cover these services runs through 2035 (`DEC-2026-11-09-10`), the year the benefit starts, so the seam closes. *Cost:* inside memo 6 B's new-user line (judgment). **Recommended: yes.** The proposed update to rule 7's note is below.
6. **CAPABLE's clinical part: a CMS demonstration in 2030-34, then the home benefit covers it from 2035.** CAPABLE pairs nurse and occupational-therapist visits with the home repairs housing's fund pays for (HOU-12.04). *Why:* in a randomized trial it cut disability scores 30% at about $2,825 a person (Szanton and others, JAMA Internal Medicine, 2019) [EV-HOU-686]. The effect faded by 12 months, and its savings estimate is uncertain [EV-HOU-688], so a Medicare benefit now (housing memo 12, part 2 C) would run ahead of the evidence. *Cost:* small, inside the benefit. **Recommended: yes.**
7. **Write the 2024 access rule's waiting-list and timeliness reporting into law.** Leave its 80% worker-pay rule and any wage floor to part D, the workforce. *Why:* the reporting is light, starts in 2027 [EV-CAR-432] [EV-CAR-433], and is the only national count of who waits, and CMS plans to rescind or revise provisions of the 2024 rules [EV-CAR-420]. The 80% rule decides how providers' payments split between wages and everything else, which is part D's question. *Burden:* state reporting already in place. **Recommended: yes.**
8. **One plain need assessment, run locally.** States, or the plan's regional offices where a state declines, assess need with one national tool, under contract to the plan and conflict-free (the assessor does not provide the services). People are reassessed only when their needs change, not on a calendar. Under memo 6 A it is the Medicaid assessment. *Why:* the design lens, and S. 1506 gives each regional office a deputy for home and community care [EV-CAR-280]. *Burden:* one visit, at home. **Recommended: yes.**
9. **PACE and other integrated programs continue** as ways to receive the benefit. PACE serves about 89,659 people (MACPAC, 2026) [EV-CAR-427]. **Recommended: yes.**
10. **The 2025 law's nursing-home staffing moratorium** (to September 30, 2034) [EV-CAR-416]: **leave open for part D.** The alternatives are to repeal the moratorium and restore the 2024 standards from 2030, with rates that fund them, or to set a new standard with part D's workforce plan. What would make it matter now: a 2027-28 vehicle that could carry the repeal. *Not adopted by silence:* the dossier carries no staffing commitment until part D decides.

## Shared rules this section relies on

From `dossiers/shared-rules.md`. These are working answers, not decisions of the other owners.

| Rule | Owner | Part B's working answer | Range |
| --- | --- | --- | --- |
| 3. Immigrant eligibility | Immigration (flagship 6) | The home benefit follows the single plan's every-resident rule (`3-design.md`, point 3). Medicaid's rules apply in the bridge | Lawfully present only, to every resident |
| 1, 2 and 4. Income, phase-outs, income lines | Secure floor (flagship 1) | Under memo 6 B there is no income or asset test. Memo 4 C's capped copays above 200% of poverty apply, as for all plan care. Under A and in the bridge, Medicaid's SSI-based tests, with point 4's limits | — |
| 5. Who verifies | Democratic renewal | Need by one assessment (point 8). Residency from the plan's records | — |
| 7. Services that make housing work | **Care (owner)** | See the proposal below | — |
| 8. Workforce | Immigration and work; part D of this dossier | Every option is priced with a wage line shown separately. Part D sets wages, training and supply; memo 9's family-caregiver pay is a seam with it | — |

**Proposed update to rule 7's note**, for Espen's decision with point 5. Under memo 6 B, the single plan's home benefit pays for tenancy-sustaining services, housing navigation and assertive community treatment for everyone who meets the need test, from 2035. Before 2035, states may claim them under the bridge's match. Housing pays only the HUD backstop it already carries (HOU-4.12) for people the benefit or their state's Medicaid does not reach. Under memo 6 A, the note stays as housing wrote it.

## How the choices fit together

- **The recommended set.** It runs in two steps.
  - *2030-34, the bridge.* A five-year Medicaid bridge: a higher match tied to shorter waiting lists, Money Follows the Person permanent, no estate recovery, higher resource limits.
  - *From January 1, 2035.* One home and community care benefit in the single plan for everyone of any age who needs help with two daily activities or the equivalent. It pays set budgets by need tier, with no asset test, paid family caregivers and a self-directed option. The plan pays the care part of nursing-home stays, and residents pay room and board from income above a protected allowance.
  - *Where it meets health.* The start is the same date as health's endpoint, so people move once. Medicaid's long-term care role shrinks to room and board for people who cannot pay it.
- **Against the legacy direction.** Memo 6 B meets each test it set.
  - *Prolonged intensive-care costs:* memo 7 B's top tier and memo 8 C.
  - *Assessed help without spend-down:* no asset test.
  - *A genuine paid-family-caregiver option:* memo 9 A.
  - *Stronger Medicaid services preserved:* memo 7 B's exceptions and the state floor.
  - *An outside-care option:* agency care is always available.
- **If memo 6 is A.** Points 1 to 4 become the program. The match increase is permanent, states must cover everyone eligible, and resource limits rise. Memo 8 stays A or B, and memo 9 A applies through Medicaid self-direction.
- **If memo 6 is C.** Medicaid and points 1 to 4 carry the front end. The federal benefit starts after a waiting period. Memo 7's threshold applies, and memo 8 C applies after the waiting period.
- **Tensions to watch.**
  - Free care at home raises demand for workers that part D must supply [EV-CAR-423].
  - The benefit's start lines up with health's busiest years (2033-35), which strains CMS's capacity (`5-delivery.md`). The one assessment (point 8) runs through states to spread that load.
  - States lose control of a program they now shape. The maintenance-of-effort payment keeps them paying.

## For housing (no decision here)

Housing reconsiders rental help for older renters who are not disabled "once the care program is scoped" (`DEC-2026-11-09-10`). If Espen chooses memo 6 B, the care program reaches older renters through services whatever their housing: help at home, a service coordinator's link (HOU-13.03) and tenancy services (point 5). Their rent stays housing's question. The lead should tell housing when memos 6-9 are decided.

## Evidence still needed

- **Independent counts of new users.** Counts of people of every age with long-term care needs who receive no paid help would tighten the new-user line, the largest uncertainty: the National Health and Aging Trends Study, and MEPS or NHIS for younger people (section 1).
- **CBO's own estimates.** CBO's December 2020 working paper with its option 5 including long-term care, and its 2021 Build Back Better estimate, from CBO itself.
- **Room and board.** Nursing-home spending by payer and the room-and-board share (memo 8).
- **Germany's cash take-up.** The share of German beneficiaries choosing cash, and quality under the cash option (memo 9).

## Questions for Espen

One answer per item; each is decided on its own.

1. **Memo 6, the guarantee:** A (stronger Medicaid), B (an all-age home and community care benefit in the single plan from 2035, no asset test; recommended), or C (catastrophic insurance)?
2. **Memo 7, scope:** part 1, the threshold of two daily activities or the equivalent (A, recommended), one (B) or three (C)? Part 2, set budgets by need tier (B, recommended), full assessed need (A) or a basic allowance (C)?
3. **Memo 8, nursing homes:** the plan pays the care part from 2035, with residents paying room and board from income above a protected allowance (C, recommended), or A, B or D?
4. **Memo 9, family caregivers:** paid through self-direction, spouses and parents included, with respite and training (A, recommended), or B, C or D?
5. **Points 1-10:**
   - 1, the bridge;
   - 2, Money Follows the Person permanent;
   - 3, no estate recovery;
   - 4, higher resource limits and no home equity cap;
   - 5, tenancy services in the benefit, with rule 7's note;
   - 6, CAPABLE's demonstration;
   - 7, reporting in law;
   - 8, one local assessment;
   - 9, PACE;
   - 10, the staffing moratorium left to part D.

   Yes to each (recommended)?
