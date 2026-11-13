# Dossier: Care you can count on (flagship 2)

Role: the care flagship (`charter/PLAN.md` 3.1). Status: specified, reviewed and booked (L3), stage D, all four parts. **Health (part A):** sections 1-9 and memos 1-5, decided (`DEC-2026-11-10-09`, `-11`, `-12`, `-13`; RTS-2's scope `DEC-2026-11-11-01`); milestone review #224, fixes #225 to #228, L3 re-check #229; booked (#230, #237, #279). **Parts B-D (long-term care, child care and pre-K, the care workforce):** sections 1b-3d and 4bcd-9bcd, memos 6-17, decided (`DEC-2026-11-11-02` to `-06`); milestone review #260, fixes #261 and #262, L3 re-check #263; booked (#265). **Both:** the status rule for people with no immigration status (#313, `DEC-2026-11-12-19`, `DEC-2026-11-13-01`) and the hospitals' uncompensated-care payment for them (#316, `DEC-2026-11-13-02`) are booked. Level in `agenda/agenda.csv`: HLT-1, 2, 4, 6, 7, 8, 9, 10, 11, A1, A2, A4, RTS-2, FAM-2 and FAM-2G at L3; FAM-2A at L2; HLT-3, HLT-5, HLT-A3 and FAM-2B to 2F are alternatives at L2. Priority pieces go to L4 later. As booked: health about $21.5 trillion over FY2030-39 and $4,094 billion in FY2040 net (`6-cost.md`, part 5), parts B-D about $3.66 trillion and $750 billion (`6bcd-cost.md`); the plan-wide FY2040 general-fund balance is $4,240 billion short (case `mixed`), nearly all of it the premium-to-tax shift the financing settlement designs.

**What it brings together** (`charter/PLAN.md` 3.1):
- health coverage restored and extended, by single-payer Medicare for All, a public option or a staged path between them, weighed in full (`DEC-2026-11-09-07`; the charter wording is #195, for Espen);
- long-term care: support at home and in nursing homes for older and disabled people;
- child care and pre-K;
- the care workforce.

**Agenda items:** HLT-1 to HLT-8, HLT-A1 to HLT-A4, RTS-2 (its home moved to care in `DEC-2026-11-10-11`), HLT-9, HLT-10, HLT-11, FAM-2 and FAM-2A to 2G (`agenda/agenda.csv`, `home_dossier` = `care`). Legacy designs: `legacy/domains/domain-health.md`, `legacy/domains/domain-family.md` (FAM-2) and the `legacy/sources/health-*` files.

**Outcomes it serves:**
- OUT-03, care people can count on, for every age;
- OUT-02, planning beyond the next paycheck (medical bills and debt);
- OUT-08, time and practical freedom (child care and family caregiving);
- OUT-01, child poverty (children's coverage, child care).

## The map: every care file, section by section

Health came first, because its choice (single-payer, a public option or a staged path) shaped the rest: what home care builds on, how child care relates to the health system's financing, and who employs the care workforce. Parts B-D followed once Espen decided health's forks. Every section below is at L3 after its part's milestone review and re-check, and every design section is decided.

| Section | Health (part A) | Parts B-D (B long-term care; C child care and pre-K; D the care workforce) |
| --- | --- | --- |
| 1. The problem | `1-problem.md`: who is uninsured and underinsured, medical debt, prices against peers, Medicare Advantage overpayment, outcomes; the January 2029 baseline (the enhanced credits' expiry, the 2025 law's Medicaid and marketplace changes, CBO's 36.6 million uninsured in 2029) | B `1b-problem-home-care.md`: who needs help, who pays, waiting lists, family caregivers, the 2029 baseline. C `1c-problem-child-care.md`: prices, who gets help, pre-K's reach, the workforce's pay, the 2029 baseline. D `1d-problem-workforce.md` |
| 2. What works | `2-what-works.md`: coverage and mortality, automatic enrollment, single-payer estimates, Vermont and California, state public options, peer countries, price caps and Maryland, failures to avoid | B `2b-what-works-home-care.md`; C `2c-what-works-child-care.md`; D `2d-what-works-workforce.md` (its arithmetic in `tools/workforce_demand.py`) |
| 3. Design choices | `3-design.md`, memos 1-5 (`memos/1-architecture.md` to `5-provider-payment.md`) and seven points; decided (`DEC-2026-11-10-09`, `-11`, `-12`, `-13`) | B `3b-design-home-care.md`, memos 6-9 (`DEC-2026-11-11-02`); C `3c-design-child-care.md`, memos 10-13 (`DEC-2026-11-11-03`); D `3d-design-workforce.md`, memos 14-16 (`DEC-2026-11-11-04`); the cost direction and memo 17's cost options (`DEC-2026-11-11-05`, `-06`) |
| 4. Specification | `4-specification.md`: the 2029 reconciliation act restores coverage; the Medicare for All Act of 2029 builds one public plan in waves to the January 1, 2035 endpoint (HLT-1, 2, 6, 7, 8 and RTS-2) | `4bcd-specification.md`: HLT-4, HLT-9, HLT-10, HLT-11, FAM-2 and FAM-2G. Both parts' provisions are in the one register, `provisions.json` |
| 5. Delivery | `5-delivery.md`: CMS runs the plan from records; the timeline to 2035; remedies; states' roles; rural delivery | `5bcd-delivery.md` |
| 6. Cost | `6-cost.md`, on the coverage model (`models/tools/health-coverage/`) with `tools/health_path.py`, and the status rule with `tools/status_rule.py`; part 5 is the booked fiscal-rule report | `6bcd-cost.md`, with `tools/care_bcd_path.py`; part 2b is long-term care's status rule |
| 7. Validation | `7-validation.md` | `7bcd-validation.md` |
| 8. What would change our minds | `8-change-our-minds.md` | `8bcd-change-our-minds.md` |
| 9. The public case | `9-public-case.md` | `9bcd-public-case.md` |
| Milestone review | `review-milestone.md` (#224; fixes #225 to #228; re-check #229) | `review-milestone-bcd.md` (#260; fixes #261, #262; re-check #263); before it, the independent audit of part B's recommendations, `review-part-b-evidence.md` |
| Booking (`models/tools/health_booking.py`, `models/tools/care_booking.py`) | #230, #237, #279; the status rule #313 and the hospitals' payment #316 | #265; long-term care's status rule #313 |
| Other work | `research-s1506-comparison.md` (the design against the Medicare for All Act of 2025; `tools/employer_wave.py`); the health coverage model (`models/tools/health-coverage/`, #201, #204) | — |

**Layout for parts B to D (chosen when part B started, November 11, 2026).** Each later part gets its own numbered files with a letter: `1b-problem-home-care.md`, `2b-what-works-home-care.md`, `3b-design-home-care.md`, and later `1c-`, `1d-` and so on, with memos numbered on from health's (part B's are 6-9). *Why:* health's sections 1-9 are decided and at L3. Adding part B inside them would put draft text under status lines that say decided, and every later edit would risk the reviewed health text. Separate files keep each part's status honest, let each part be reviewed on its own, and keep health's files stable. Sections 4-9 for part B are a separate choice, made when part B's memos are decided: part B's provisions belong inside health's bill (the home benefit is a title of the Medicare for All Act of 2029), so its section 4 rows will likely join `4-specification.md` and `provisions.json` under new HLT-9 IDs, while its delivery, cost and public case may need their own `5b-` to `9b-` files.

**Layout for sections 4-9 of parts B to D (chosen November 12, 2026, board row D-9).** One new set of files covers parts B, C and D together: `4bcd-specification.md`, `5bcd-delivery.md`, `6bcd-cost.md`, `7bcd-validation.md`, `8bcd-change-our-minds.md` and `9bcd-public-case.md`, each with a part for B, C and D and the pieces they share. Their provisions join the one register, `provisions.json`, under new IDs on HLT-4, HLT-9, HLT-10, HLT-11 and FAM-2. *Why not extend health's files:* health's sections 4-9 are decided and at L3, and the same reason that kept parts B-D out of health's sections 1-3 holds: draft text under an L3 status line, and every later edit risking reviewed text. *Why one set for B-D rather than a file per part per section:* the three parts were decided and priced together (memo 17, `DEC-2026-11-11-06`). They share vehicles, the states' instrument (health's HLT-7.17 offset), the wage floor that runs through B's and C's rates, one cost total and fiscal-rule report, and one public case. Eighteen files would split each of those across three places. Where a reader needs only one part, each file's part headings stand alone. Health's own files change only by the short Break Up Big Medicine note in `8-change-our-minds.md` ("For later consideration").

## Files

- `1-problem.md`, `2-what-works.md` (health, sections 1-2).
- `evidence.json`: EV-CAR-001 to 050 (the 2029 baseline), 100 to 141 (the problem), 200 to 268 (what works), 270 to 316 (the S. 1506 comparison), 330 to 350 (sections 4-6), 400 to 451 (part B, sections 1-3). Sources SRC-3000 to 3399 are reserved for care.
- `3-design.md` and `memos/1-architecture.md` to `5-provider-payment.md` (health, section 3).
- `4-specification.md`, `provisions.json`, `5-delivery.md`, `6-cost.md`, `7-validation.md`, `8-change-our-minds.md`, `9-public-case.md` (health, sections 4-9); `tools/health_path.py` prices the decided path on the coverage model. Evidence EV-CAR-330 to 350 (sources SRC-3281 to 3295) back them.
- `1b-problem-home-care.md`, `2b-what-works-home-care.md`, `3b-design-home-care.md` and `memos/6-home-care-guarantee.md` to `9-family-caregivers.md` (part B, sections 1-3, revised in board row D-5b after `review-part-b-evidence.md`, the independent audit). Evidence **EV-CAR-400 to 499 is reserved for part B's sections 1-3**: 400 to 451 (the first draft), 452 to 459 and 463 (the revision: CBO's 2020 single-payer options, the WISH Act actuarial estimates, Japan's 2005 reform, the WA Cares vote, the inspector general on personal care fraud), 470 to 499 (the audit); 460 to 462 are health's. Sources SRC-3313 to 3354 (23 saved federal texts and 19 citation rows), SRC-3361 to 3386 (the audit) and SRC-3387 to 3394 (the revision). Care's reserved source block ends at 3399, so later parts may need a new reservation (`dossiers/TEMPLATE.md`, "Reserve ID ranges first").
- `1c-problem-child-care.md`, `2c-what-works-child-care.md`, `3c-design-child-care.md` and `memos/10-child-care-guarantee.md` to `13-delivery-head-start.md` (part C, sections 1-3). Evidence **EV-CAR-500 to 599 is reserved for part C's sections 1-3** (500 to 593 used). Sources **SRC-3011 to 3099**, an unused part of care's reserved block, chosen to stay clear of other workers near SRC-3360-3399 (SRC-3011 to 3077 used: 13 saved federal texts and 52 citation rows).
- `1d-problem-workforce.md`, `2d-what-works-workforce.md`, `3d-design-workforce.md` and `memos/14-care-pay.md` to `16-nursing-home-staffing.md` (part D, sections 1-3); its arithmetic in `tools/workforce_demand.py`. Evidence **EV-CAR-600 to 699 is reserved for part D** (600 to 647 used; 641-647 by row D-8). Numbers 700 to 799 in the EV-CAR series are reserved for parts B-D's sections 4-9 (row D-9). Sources **SRC-3124 to 3199 are reserved for part D**, an unused part of care's block, agreed with the lead on November 11, 2026, and assigned by hand because `build_catalog.py` can auto-assign inside reserved ranges (SRC-3124 to 3155 used: 7 saved federal texts and 25 citation rows; source numbers 3156 to 3199 remain, for row D-9).
- `4bcd-specification.md`, `5bcd-delivery.md`, `6bcd-cost.md` (parts B-D, sections 4-6; board row D-9); provisions HLT-4.01 to 4.08, HLT-9.01 to 9.11, HLT-10.01 to 10.07, HLT-11.01 to 11.05, FAM-2.01 to 2.11 and FAM-2G.01, 2G.02 in `provisions.json`; `tools/care_bcd_path.py` puts the decided pieces on fiscal years. `7bcd-validation.md`, `8bcd-change-our-minds.md`, `9bcd-public-case.md` (sections 7-9; PR 2).
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
7. **People with no immigration status:** health and long-term care cover people with lawful or registered status, decided (`DEC-2026-11-12-19`, `DEC-2026-11-13-01`); hospitals' uncompensated-care payment for the emergency care of people the plan doesn't cover, decided (`DEC-2026-11-13-02`). Left to the specification: that payment's vehicle and formula (`6-cost.md`, part 2b).
