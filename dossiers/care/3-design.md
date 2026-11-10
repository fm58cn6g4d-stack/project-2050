# Care you can count on, part A (health): design choices

Role: section 3 of the care dossier, health part: the real forks, the options weighed and a recommendation for each, with one decision memo per fork in `memos/`. Status: draft (stage D, step 3); decided by Espen, November 10, 2026 (`DEC-2026-11-10-09`, `DEC-2026-11-10-11`). After the comparison with S. 1506 (`research-s1506-comparison.md`): the endpoint is 2035, employer groups move with Medicaid in 2033-35, memo 3 B is confirmed, current Medicare enrollees get the upgrades from 2031, abortion and reproductive care are covered with no Hyde-type limits, and the VA, TRICARE and the Indian Health Service continue alongside the single plan. Nothing here is adopted until Espen decides; each memo and each point below is decided on its own (`charter/STANDARDS.md`, "Decision memos"). Cost and coverage figures come from the coverage model (`models/tools/health-coverage/`, exploratory; its results file and card name its limits) and from the evidence register.

## How to read this section

- **One batched set.** Five memos and seven yes-or-no points, so Espen can answer once. Memo 1 shapes the rest; memos 2-5 say how each answer applies under each of memo 1's options.
- **Medicare for All in full** (`DEC-2026-11-09-07`): single-payer is option C in memo 1 and the endpoint of option B, with the same evidence, cost, coverage and transition work as the legacy public option.
- **Legacy designs are options** (`DEC-2026-10-30-02`): restoration (HLT-1), Medicare upgrades (HLT-2), the public option (HLT-3), prices (HLT-5) and Medicare payment reform (HLT-6) each appear as an option to keep, change or drop.
- **Report, don't gate** (`DEC-2026-11-10-05`): each option's cost is reported for the financing settlement. Memo 1's choice is mainly about money, so it comes to Espen with its cost.
- **What needs an answer now** (`DEC-2026-11-10-07`): the memos decide the commitments (who is covered, the benefit, the rates' basis, the plumbing). Dates, tax mix and the exact rate by service are working assumptions or left to sections 4-6, as each memo says.

## The baseline in 2029

Section 1, part 8: the enhanced credits expired and were not extended; the 2025 law's Medicaid cuts (work requirements and six-month checks from January 2027, immigrant limits from October 2026, cost sharing from October 2028, provider-tax limits phasing down) and marketplace changes (verification before credits from 2028) are in force; CBO projects 36.6 million uninsured in 2029 (CBO, 2026) [EV-CAR-020]. The coverage model's 2032 baseline is 37.2 million.

## The forks at a glance

| Fork | Memo | Options | Recommended |
| --- | --- | --- | --- |
| 1. The shape of the system | `memos/1-architecture.md` | A public option on restored coverage (legacy); B staged path to single-payer with the endpoint in law; C single-payer phased in over 2032-35; D universal multi-payer with all-payer rates | **B** |
| 2. The transition | `memos/2-transition.md` | Order: by age, by payer with children first, all at once; plus five protections | **By payer, children first; all five protections** |
| 3. Financing interface | `memos/3-financing-interface.md` | A new revenue only; B keep public streams, states' maintenance of effort, employer contribution, new revenue for the rest; C income-related public premiums | **B** |
| 4. Benefits | `memos/4-benefits.md` | A legacy Medicare upgrades only; B comprehensive, no cost sharing; C comprehensive, small capped copays above 200% of poverty; D with long-term care | **C, long-term care decided in part B** |
| 5. Provider payment | `memos/5-provider-payment.md` | A Medicare's rates; B glide path to about 1.15 times Medicare with global budgets for rural and safety-net hospitals; C all-payer rate setting; D negotiation plus a 200% commercial cap (legacy HLT-5) | **B, plus the Medicare Advantage fix** |

## What the options cost (the coverage model, 2032)

| Option (memo 1) | Uninsured | New federal cost, 2032 | FY2030-39 federal | National spending, 2032 |
| --- | --- | --- | --- | --- |
| Current law in 2029 | 37.2 million | — | — | — |
| Restore only (point 1 below) | 23.6 million | about $190 billion | about $2.1 trillion | about +$60 billion |
| A. Public option | 14.5 million | about $240 billion | about $2.6 trillion | about flat (+$15 billion) |
| B. Staged path (2032 status) | about 14.0 million (Medicare at 60 only; children in the first wave would lower it, not modeled separately) | about $250 billion, rising to C's by the endpoint | endpoint 2037: about $17-28 trillion; 2040: about $3-22 trillion (project arithmetic; the lower end is nearer memo 2's order, which moves employer groups last) | about $40-80 billion lower, then C's |
| C. Single-payer | 3.6 million | about $3.4-3.5 trillion | about $28-29 trillion (2032-35 phase-in) | about −$130 billion to +$95 billion |

- These are exploratory. The model's CBO-like single-payer variant, about $3.44 trillion in 2032, is above the high end of CBO's 2020 range grown to 2032 (about $3.32 trillion), so its single-payer figures read high. More generally the model runs high against that range (its card explains why) and misses CBO's cost of permanent enhanced credits; both are reported, not tuned away.
- Single-payer's federal cost replaces about $1.7 trillion of household premiums and out-of-pocket costs and about $1.5 trillion of employer premiums in 2032. Who pays the new taxes is the financing settlement's decision, under D3.
- FY2040 permanent cost (`DEC-2026-11-10-05`): section 6 will report it from the model once Espen chooses; on the model's growth path, single-payer's net federal cost (and any staged path once it reaches the endpoint) would be about $5.5 trillion in FY2040, and the public option's about $0.4 trillion (project arithmetic, to be confirmed in section 6).

## Recommended without a memo: seven yes-or-no points

None is adopted by silence.

1. **Restore first, in the first 2029 bill, whatever memo 1 decides.** Repeal the 2025 law's coverage cuts (work requirements, six-month checks, retroactive-coverage limits, immigrant exclusions, cost sharing for expansion adults, the provider-tax and directed-payment cuts) and restore the enhanced credits until the new system replaces them. The legacy HLT-1, kept as the first step. *Cost:* about $190 billion in 2032, $2.1 trillion over FY2030-39 (the coverage model, which overstates the credits' cost against CBO's, so this is a high reading on that part), not counting the provider-tax and directed-payment restoration, which the model leaves at $0 in its central case (range up to about $60 billion a year, `mcd_financing_restore`); CBO estimates the law's Medicaid provisions cut $989.7 billion and its marketplace provisions $271.9 billion (CBO, via CRS, 2025; CBO, 2025) [EV-CAR-025] [EV-CAR-049]. If a 2027-28 deal restores the credits, this shrinks. **Recommended: yes.**
2. **Automatic enrollment and renewal from records, no work requirement.** Every option enrolls people from records the government holds (tax, Medicaid, Social Security), renews yearly at most and without forms where records suffice, and has no work requirement. *Why:* one extra step cut enrollment a third in Massachusetts (Shepard and Wagner, American Economic Review, 2025) [EV-CAR-206]; Arkansas's work requirement cut coverage and raised no employment (Sommers and others, New England Journal of Medicine, 2019) [EV-CAR-212] [EV-CAR-213]. *Burden:* lower than today's. **Recommended: yes.**
3. **Coverage for every resident, proposed to the immigration flagship (shared rule 3).** The 2025 law drops many lawfully present immigrants from Medicaid from October 2026 and from the credits from 2027 (Public Law 119-21) [EV-CAR-008] [EV-CAR-016]; noncitizens are already the least covered group, 28.9% uninsured (Census, 2026) [EV-CAR-103]. The care dossier proposes that the new system cover everyone who lives in the United States, with lawfully present immigrants restored in the first bill (point 1), and asks the immigration flagship, which owns the rule, to decide whether people without status are covered from the start or later. *Working answer for costing:* the model's residual 3.6 million uninsured under single-payer includes people not covered on status; covering everyone adds a modest cost to be priced. **Recommended: yes, as a proposal; the immigration flagship decides.**
4. **Medicare upgrades on the legacy dates under option A** (HLT-2: a $5,000 out-of-pocket cap, hearing and vision from 2031, dental from 2033). Under B and C the single plan's benefit (memo 4) replaces them for each group as it moves. **Recommended: yes.**
5. **Medicare Advantage: fix coding and benchmarks on MedPAC's method, and count the savings at MedPAC's lower 2026 estimate** (14%, about $76 billion in 2026: MedPAC, 2026) [EV-CAR-135], not the legacy assumption of full capture (HLT-6). The legacy financing leaned on this saving for both the general fund and the hospital trust fund (`legacy/domains/domain-health.md`, "Concentration risk"). **Recommended: yes.**
6. **A rural health role for USDA Rural Development: scale what exists, don't create a new service.** Espen asked (November 10, via the lead) whether a rural health service under USDA RD could help finance facilities or serve as a navigator. What exists:
   - USDA's Community Facilities program already lends to rural hospitals, clinics and nursing homes: 161 loans for $940.7 million in FY2025, at about zero or negative subsidy cost (`dossiers/foundations/rural-delivery.md`, citing SRC-2131 and SRC-2125). Its grants are 99% earmarked, leaving little for competitive awards (SRC-2112).
   - The Rural Health Transformation Program gives states $10 billion a year through FY2030 (Public Law 119-21) [EV-CAR-015]; HRSA's rural health office and Medicare's rural hospital designations cover operating support.
   - *Options:* (a) nothing new; (b) **raise Community Facilities direct lending to $3-5 billion a year for rural health facilities, restore $200-500 million of competitive grants, and make RD's state offices a front door that points rural providers to HRSA, CMS and the transformation fund** (the R1 note's menu, `rural-delivery.md`); (c) a new USDA rural health service.
   - *Why (b):* it uses a channel that already finances rural hospitals locally at almost no budget cost; the binding constraint is staff, which housing's rebuild of RD's offices (`DEC-2026-11-10-02`) already funds. A new service (c) would duplicate HRSA and CMS and add a second set of rules for rural providers, against the design lens. *Cost:* about $0.2-0.5 billion a year for the grants (judgment); the loans cost little. *Leave open:* the navigator's exact remit, decided in section 5 with the housing rebuild. **Recommended: (b).**
7. **The hospital trust fund kept whole on every path** (the legacy D4 rule), with any Medicare savings credited to it first. Under single-payer the fund folds into the single plan's fund (memo 3). **Recommended: yes.**

## Shared rules this section relies on

From `dossiers/shared-rules.md`; working answers, not decisions of other owners.

| Rule | Owner | Health's working answer | Range |
| --- | --- | --- | --- |
| 3. Immigrant eligibility | Immigration (flagship 6) | Lawfully present immigrants restored in the first bill; the new system covers every resident, with people without status decided by the owner (point 3) | Lawfully present only, to every resident |
| 1 and 2. Income and phase-outs | Secure floor (flagship 1) | Under A and in B's early stages, premium credits phase out on the enhanced schedule; under the single plan there is no premium to phase out, and memo 4's copays use one income line | Enhanced schedule to none |
| 4. Income lines | Secure floor | The federal poverty guidelines for health; memo 4's 200% line | — |
| 5. Who verifies | Democratic renewal | Records the government holds (point 2) | — |
| 7. Services that make housing work | **Care (owner)** | Unchanged until part B decides long-term care; housing's supportive-housing services stay financed as section 4 of housing says | — |
| 8. Workforce | Immigration and work | Supply is the risk in memos 4 and 5; part D (workforce) sizes it | — |

**Proposed update to rule 7's note, for the owner's later decision:** under single-payer, Medicaid's home and community services would move into the single plan only if part B chooses so; until then housing's working answer stands.

## How the choices fit together

- **The recommended set** (B, by payer with children first, plumbing B, benefits C, payment B) builds single-payer in about eight years from enactment. Each stage is automatic, enrolls people from records, and is paid from existing streams plus new revenue the settlement sets.
- **If memo 1 is A**, memos 2-5 shrink to: the five protections (only the first applies fully), the hospital trust fund kept whole, legacy Medicare upgrades (point 4), and payment option D or B for the public plan.
- **If memo 1 is C**, memo 2's order compresses to about four years; memo 3's employer contribution matters most, because all employers move at once.
- **Tensions to watch:** memo 4's free care raises demand while memo 5's lower rates trim supply (CBO, 2020) [EV-CAR-219]; part D (the workforce) must size the supply the recommended set needs before the endpoint.

## Evidence still needed

- CBO's estimate of a federal public option, and CBO's 2020 working paper tables for the five single-payer options (to tighten the model's benchmarks).
- The ACA applicable-percentage tables and Medicare premium tables (labeled assumptions in the model).
- An estimate of the cost of covering people without status (point 3).
- The current all-payer average hospital rate as a multiple of Medicare, to anchor memo 5's starting point.

## Questions for Espen

**Answered by Espen, November 10, 2026 (`DEC-2026-11-10-09`):** memo 1 B with a 2037 endpoint; memo 2 by payer with children first and all five protections, with the employer wave's timing reopened; memo 3 B provisionally, pending a comparison with S. 1506; memo 4 C; memo 5 B with the Medicare Advantage fix; points 1-7 yes, with point 6 as option (b). The list below is kept as asked.

One answer per item; each is decided on its own.

1. **Memo 1, the shape:** A (public option), B (staged path to single-payer with the endpoint in law; recommended), C (single-payer phased in over 2032-35) or D (universal multi-payer)? If B, is the endpoint 2037 (about $17-28 trillion over FY2030-39) or later, such as 2040 (about $3-22 trillion)?
2. **Memo 2, the transition:** order by payer with children first (recommended), by age, or all at once? Yes to the five protections?
3. **Memo 3, the money's plumbing:** B (keep public streams, states' maintenance of effort, employer contribution; recommended), A or C?
4. **Memo 4, benefits:** C (comprehensive, small capped copays above 200% of poverty; recommended), A, B or D? Long-term care in part B?
5. **Memo 5, payment:** B (glide path to about 1.15 times Medicare, global budgets for rural and safety-net hospitals; recommended), A, C or D? Yes to the Medicare Advantage fix at MedPAC's lower estimate?
6. **Points 1-7:** restore first; automatic enrollment, no work requirement; every resident (proposal to immigration); legacy Medicare upgrades under A; Medicare Advantage savings at MedPAC's estimate; rural health through USDA's existing Community Facilities program, not a new service; the hospital trust fund kept whole. Yes to each (recommended)?
