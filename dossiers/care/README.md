# Dossier: Care you can count on (flagship 2)

Role: the care flagship (`charter/PLAN.md` 3.1). Status: started, stage D; part B (long-term care: support at home and in nursing homes for older and disabled people) sections 1-3 drafted and revised after the independent audit (`review-part-b-evidence.md`), its memo set (memos 6-9) decided (`DEC-2026-11-11-02`); part C (child care and pre-K) sections 1-3 drafted, its memo set (memos 10-13) decided (`DEC-2026-11-11-03`). Part D (the care workforce) sections 1-3 drafted, its memo set (memos 14-16) decided (`DEC-2026-11-11-04`). Parts B-D repriced in step 8 under Espen's cost direction (`DEC-2026-11-11-05`), and memo 17's cost options decided November 11: about $3.80 trillion over FY2030-39 and $736 billion in FY2040. Sections 4-9 for parts B-D are next. Level: the health rows HLT-1, 2, 6, 7, 8, A1, A2 and A4 are at L3 in `agenda/agenda.csv` after the milestone review (`review-milestone.md`), its fixes (#225-#228) and the L3 re-check on the close-out PR; RTS-2 is at L3 since Espen settled its foreign-assistance scope (`DEC-2026-11-11-01`: the Helms amendment ends too); HLT-3, HLT-5 and HLT-A3 are alternatives; the other care items are at L1 (`DEC-2026-10-30-03`); legacy designs are working choices weighed as options (`DEC-2026-10-30-02`). The target is L3, with priority pieces at L4.

**What it brings together** (`charter/PLAN.md` 3.1):
- health coverage restored and extended, by single-payer Medicare for All, a public option or a staged path between them, weighed in full (`DEC-2026-11-09-07`; the charter wording is #195, for Espen);
- long-term care: support at home and in nursing homes for older and disabled people;
- child care and pre-K;
- the care workforce.

**Agenda items:** HLT-1 to HLT-8, HLT-A1 to HLT-A4, RTS-2 (its home moved to care in `DEC-2026-11-10-11`), FAM-2 and FAM-2A to 2D (`agenda/agenda.csv`, `home_dossier` = `care`). Legacy designs: `legacy/domains/domain-health.md`, `legacy/domains/domain-family.md` (FAM-2) and the `legacy/sources/health-*` files.

**Outcomes it serves:**
- OUT-03, care people can count on, for every age;
- OUT-02, planning beyond the next paycheck (medical bills and debt);
- OUT-08, time and practical freedom (child care and family caregiving);
- OUT-01, child poverty (children's coverage, child care).

## Order of work

Health comes first, because its choice (single-payer, a public option or a staged path) shapes the rest: what home care builds on, how child care relates to the health system's financing, and who employs the care workforce. The other areas follow once Espen decides health's forks.

| Part | Sections | Status |
| --- | --- | --- |
| **A. Health** | 1. The problem: `1-problem.md`. Who is uninsured and underinsured, medical debt, spending and prices against peers, Medicare Advantage overpayment, long-term care waiting lists, outcomes; and the January 2029 baseline: the enhanced credits' expiry (not extended), the 2025 reconciliation law's Medicaid and marketplace changes date by date from the statute, CBO's 36.6 million uninsured in 2029 | Draft (stage D, step 2) |
| | 2. What works: `2-what-works.md`. Coverage and mortality, automatic enrollment, churn and work requirements; single-payer estimates (CBO, Urban, RAND, Mercatus, the Lancet, PERI) and what drives their range; Vermont and California; state public options (Washington, Colorado, Nevada); Taiwan, Canada, the Netherlands, Switzerland, Germany, Australia; price caps and Maryland; a lower Medicare age; failures to avoid | Draft (stage D, step 2) |
| | 3. Design choices: `3-design.md` and five memos in `memos/` (1 the shape: public option, staged path to single-payer, single-payer, universal multi-payer; 2 the transition; 3 the financing interface; 4 benefits; 5 provider payment), plus seven yes-or-no points (restore first; automatic enrollment, no work requirement; every resident, proposed to immigration; Medicare upgrades; Medicare Advantage at MedPAC's estimate; rural health through USDA's Community Facilities program; the hospital trust fund). One batched set for Espen; each decided on its own | Decided (`DEC-2026-11-10-09`, `-11`, `-12`, `-13`) |
| | The health coverage model (`charter/PLAN.md` 3.4): `models/tools/health-coverage/` (exploratory), only what the memo set needs: coverage, federal cost and household cost by option, with a model card and CBO benchmarks | Done (step 3m, #201 and #204) |
| | 4. Specification: `4-specification.md`, `provisions.json` (41 provisions: HLT-1, 2, 6, 7, 8 and RTS-2). The 2029 reconciliation act restores coverage; the Medicare for All Act of 2029 builds one public plan in waves (2031; 2033-35) to the January 1, 2035 endpoint | Draft (stage D, step 4, PR 1) |
| | 5. Delivery: `5-delivery.md`. CMS runs the plan from records; the timeline to 2035; remedies; states' roles; rural delivery | Draft (step 4, PR 1) |
| | 6. Cost: `6-cost.md`, on the coverage model with `tools/health_path.py`, on fiscal years. About $21.7 trillion over FY2030-39 and $4.2 trillion in FY2040 ($4,157 billion) net federal cost before the employer contribution (about $16.4 trillion and $3.1 trillion with it at 65%), with Medicaid's long-term care kept in Medicaid (board row D-4c); exploratory, not a score | Draft (step 4; revised after the milestone review) |
| | 7. Validation: `7-validation.md`. Against CBO, Urban and the Lancet; what the models miss; household cost by income; objections; signs of failure | Draft (step 4, PR 2) |
| | 8. What would change our minds: `8-change-our-minds.md`. Triggers by choice, political and legal events (the rules reform; the states' payment and coercion), hard stops | Draft (step 4, PR 2) |
| | 9. The public case: `9-public-case.md`. Brief, messages, hard questions, can say / can't say, source table; only from sections 1-8 | Draft (step 4, PR 2) |
| | Health milestone review: `review-milestone.md` (#224). L2 passes; L3 after the fix steps (states' payment, territories, fiscal-year basis, section 9, delivery and record fixes) and a short re-check | Fix steps in progress |
| **B. Long-term care: support at home and in nursing homes for older and disabled people** | 1. The problem: `1b-problem-home-care.md`. Who needs help and for how long (all ages; half of Medicaid home-care users are under 65), who pays, waiting lists, family caregivers, the workforce, and the January 2029 baseline (the 2025 law's long-term care provisions, Money Follows the Person's expiry, the 2024 access rule at risk) | Draft (stage D, step 5) |
| | 2. What works: `2b-what-works-home-care.md`. Home against institutional care and what expansion costs; Medicaid's tools (waivers, Community First Choice, ARPA sec. 9817, Money Follows the Person, self-direction, PACE); CLASS and WA Cares; Germany, Japan, the Netherlands and the Nordic countries; failures to avoid | Draft (step 5) |
| | 3. Design choices: `3b-design-home-care.md` and four memos (6 the guarantee: stronger Medicaid, a home and community care benefit in the single plan, or catastrophic insurance; 7 who qualifies and how much; 8 nursing homes; 9 family caregivers), plus ten yes-or-no points (the 2030-34 bridge, Money Follows the Person, estate recovery, resource limits, tenancy services under rule 7, CAPABLE, reporting in law, one assessment, PACE, the staffing moratorium left to part D). One batched set for Espen; each decided on its own | For Espen (step 5) |
| **C. Child care and pre-K** | 1. The problem: `1c-problem-child-care.md`. Prices, who gets help (16% of eligible children), pre-K's reach, the workforce's pay, and the January 2029 baseline (the 2025 law's 45F, sec. 129 and sec. 21 changes; CCDBG and Head Start levels; the 2024 rule rescinded from July 2026; the Head Start immigrant directive enjoined) | Draft (stage D, step 6) |
| | 2. What works: `2c-what-works-child-care.md`. Quebec, Canada, Norway and the Nordic systems; New Mexico, Washington, Vermont, DC and the military system; Tulsa, Boston, Tennessee and Head Start; costs; the under-3 problem; the 2014 law, ARPA, BBB, the CCWFA and the 2025-26 bills | Draft (step 6) |
| | 3. Design choices: `3c-design-child-care.md` and four memos (10 the guarantee: block grant, capped cost or universal flat fee; 11 pre-K; 12 phasing and supply; 13 delivery and Head Start), ten yes-or-no points, the bill comparison, inherited assumptions traced, and the proposed pre-K seam with education. One batched set for Espen; each decided on its own | For Espen (step 6) |
| **D. The care workforce** | 1-3, across health, home care and child care; meets shared rule 8 | Later |

Sections 4-9 are written once per dossier where the parts can share them, or per part where they can't; the choice is made when part B starts.

**Layout for parts B to D (chosen when part B started, November 11, 2026).** Each later part gets its own numbered files with a letter: `1b-problem-home-care.md`, `2b-what-works-home-care.md`, `3b-design-home-care.md`, and later `1c-`, `1d-` and so on, with memos numbered on from health's (part B's are 6-9). *Why:* health's sections 1-9 are decided and at L3. Adding part B inside them would put draft text under status lines that say decided, and every later edit would risk the reviewed health text. Separate files keep each part's status honest, let each part be reviewed on its own, and keep health's files stable. Sections 4-9 for part B are a separate choice, made when part B's memos are decided: part B's provisions belong inside health's bill (the home benefit is a title of the Medicare for All Act of 2029), so its section 4 rows will likely join `4-specification.md` and `provisions.json` under new HLT-9 IDs, while its delivery, cost and public case may need their own `5b-` to `9b-` files.

## Files

- `1-problem.md`, `2-what-works.md` (health, sections 1-2).
- `evidence.json`: EV-CAR-001 to 050 (the 2029 baseline), 100 to 141 (the problem), 200 to 268 (what works), 270 to 316 (the S. 1506 comparison), 330 to 350 (sections 4-6), 400 to 451 (part B, sections 1-3). Sources SRC-3000 to 3399 are reserved for care.
- `3-design.md` and `memos/1-architecture.md` to `5-provider-payment.md` (health, section 3).
- `4-specification.md`, `provisions.json`, `5-delivery.md`, `6-cost.md`, `7-validation.md`, `8-change-our-minds.md`, `9-public-case.md` (health, sections 4-9); `tools/health_path.py` prices the decided path on the coverage model. Evidence EV-CAR-330 to 350 (sources SRC-3281 to 3295) back them.
- `1b-problem-home-care.md`, `2b-what-works-home-care.md`, `3b-design-home-care.md` and `memos/6-home-care-guarantee.md` to `9-family-caregivers.md` (part B, sections 1-3, revised in board row D-5b after `review-part-b-evidence.md`, the independent audit). Evidence **EV-CAR-400 to 499 is reserved for part B's sections 1-3**: 400 to 451 (the first draft), 452 to 459 and 463 (the revision: CBO's 2020 single-payer options, the WISH Act actuarial estimates, Japan's 2005 reform, the WA Cares vote, the inspector general on personal care fraud), 470 to 499 (the audit); 460 to 462 are health's. Sources SRC-3313 to 3354 (23 saved federal texts and 19 citation rows), SRC-3361 to 3386 (the audit) and SRC-3387 to 3394 (the revision). Care's reserved source block ends at 3399, so later parts may need a new reservation (`dossiers/TEMPLATE.md`, "Reserve ID ranges first").
- `1c-problem-child-care.md`, `2c-what-works-child-care.md`, `3c-design-child-care.md` and `memos/10-child-care-guarantee.md` to `13-delivery-head-start.md` (part C, sections 1-3). Evidence **EV-CAR-500 to 599 is reserved for part C's sections 1-3** (500 to 593 used). Sources **SRC-3011 to 3099**, an unused part of care's reserved block, chosen to stay clear of other workers near SRC-3360-3399 (SRC-3011 to 3077 used: 13 saved federal texts and 52 citation rows).
- `1d-problem-workforce.md`, `2d-what-works-workforce.md`, `3d-design-workforce.md` and `memos/14-care-pay.md` to `16-nursing-home-staffing.md` (part D, sections 1-3); its arithmetic in `tools/workforce_demand.py`. Evidence **EV-CAR-600 to 699 is reserved for part D** (600 to 640 used). Sources **SRC-3124 to 3199 are reserved for part D**, an unused part of care's block, agreed with the lead on November 11, 2026, and assigned by hand because `build_catalog.py` can auto-assign inside reserved ranges (SRC-3124 to 3151 used: 7 saved federal texts and 21 citation rows).
- `research-s1506-comparison.md` (stage D, step 3c): the design against the Medicare for All Act of 2025 (S. 1506, H.R. 3069), the employer wave re-examined, memo 3 confirmed; its arithmetic in `tools/employer_wave.py`. Evidence EV-CAR-270 to 316 (block 270-329 reserved for this note); sources SRC-3260 to 3280.

## Shared rules care is likely to own or touch

From `dossiers/shared-rules.md`; proposed in the design section, never overwritten here:
- **Rule 7, services that make housing work:** care owns it (HLT-4).
- **Rule 3, which immigrants are eligible:** owned by the immigration flagship; care states the exception it needs for coverage (for example whether a universal program covers everyone resident).
- **Rules 1, 2 and 4** (income, phase-outs, income lines): health premium credits and Medicaid use the poverty guidelines and phase out on their own schedules; owned by the secure floor.
- **Rule 8, the workforce:** care workers; owned by the immigration and work flagships.

## Open questions for Espen

1. **Health, section 3:** decided (`DEC-2026-11-10-09`, `-11`, `-12`).
2. **Health, section 6, part 3:** the hospital transition fund, decided (`DEC-2026-11-10-13`).
3. **Part B, long-term care:** memos 6-9 and points 1-10, decided (`DEC-2026-11-11-02`).
4. **Part C, child care and pre-K:** memos 10-13, points 1-10 and the pre-K seam, decided (`DEC-2026-11-11-03`).
5. **Part D, the care workforce:** memos 14-16 and points 1-9, decided (`DEC-2026-11-11-04`).
6. **Care's cost options:** memo 17, decided November 11 (`DEC-2026-11-11-06`), including that a state that declines child care or pre-K still owes its share (`memos/17-cost-options.md`).
