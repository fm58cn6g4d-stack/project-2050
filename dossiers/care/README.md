# Dossier: Care you can count on (flagship 2)

Role: the care flagship (`charter/PLAN.md` 3.1). Status: started, stage D. Level: every care item is at L1 in `agenda/agenda.csv` (`DEC-2026-10-30-03`); legacy designs are working choices weighed as options (`DEC-2026-10-30-02`). The target is L3, with priority pieces at L4.

**What it brings together** (`charter/PLAN.md` 3.1):
- health coverage restored and extended, by single-payer Medicare for All, a public option or a staged path between them, weighed in full (`DEC-2026-11-09-07`; the charter wording is #195, for Espen);
- care at home for all ages;
- child care and pre-K;
- the care workforce.

**Agenda items:** HLT-1 to HLT-6, HLT-A1 to HLT-A4, FAM-2 and FAM-2A to 2D (`agenda/agenda.csv`, `home_dossier` = `care`). Legacy designs: `legacy/domains/domain-health.md`, `legacy/domains/domain-family.md` (FAM-2) and the `legacy/sources/health-*` files.

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
| | 3. Design choices: `3-design.md` and five memos in `memos/` (1 the shape: public option, staged path to single-payer, single-payer, universal multi-payer; 2 the transition; 3 the financing interface; 4 benefits; 5 provider payment), plus seven yes-or-no points (restore first; automatic enrollment, no work requirement; every resident, proposed to immigration; Medicare upgrades; Medicare Advantage at MedPAC's estimate; rural health through USDA's Community Facilities program; the hospital trust fund). One batched set for Espen; each decided on its own | Draft (stage D, step 3), for Espen |
| | The health coverage model (`charter/PLAN.md` 3.4): `models/tools/health-coverage/` (exploratory), only what the memo set needs: coverage, federal cost and household cost by option, with a model card and CBO benchmarks | In review (step 3m, PR #201) |
| | 4. Specification: `4-specification.md`, `provisions.json` (40 provisions: HLT-1, 2, 6, 7, 8 and RTS-2). The 2029 reconciliation act restores coverage; the Medicare for All Act of 2029 builds one public plan in waves (2031; 2033-35) to the January 1, 2035 endpoint | Draft (stage D, step 4, PR 1) |
| | 5. Delivery: `5-delivery.md`. CMS runs the plan from records; the timeline to 2035; remedies; states' roles; rural delivery | Draft (step 4, PR 1) |
| | 6. Cost: `6-cost.md`, on the coverage model with `tools/health_path.py`. About $25.7 trillion over FY2030-39 and $4.7 trillion in FY2040 net federal cost before the employer contribution (about $20.1 trillion and $3.7 trillion with it at 65%); exploratory, not a score | Draft (step 4, PR 1) |
| | 7-9: validation, what would change our minds, the public case | Next (step 4, PR 2) |
| **B. Care at home for all ages** | 1-3, building on health's choice; the legacy long-term-care direction of October 26 (an all-age home-support benefit) is weighed as an option; meets housing's aging-in-place work (`dossiers/home/memos/12-aging-in-place.md`) and shared rule 7 | Later |
| **C. Child care and pre-K** | 1-3 (FAM-2 and its options) | Later |
| **D. The care workforce** | 1-3, across health, home care and child care; meets shared rule 8 | Later |

Sections 4-9 are written once per dossier where the parts can share them, or per part where they can't; the choice is made when part B starts.

## Files

- `1-problem.md`, `2-what-works.md` (health, sections 1-2).
- `evidence.json`: EV-CAR-001 to 050 (the 2029 baseline), 100 to 141 (the problem), 200 to 268 (what works), 270 to 316 (the S. 1506 comparison), 330 to 350 (sections 4-6). Sources SRC-3000 to 3399 are reserved for care.
- `3-design.md` and `memos/1-architecture.md` to `5-provider-payment.md` (health, section 3).
- `4-specification.md`, `provisions.json`, `5-delivery.md`, `6-cost.md` (health, sections 4-6); `tools/health_path.py` prices the decided path on the coverage model. Evidence EV-CAR-330 to 350 (sources SRC-3281 to 3295) back them.
- `research-s1506-comparison.md` (stage D, step 3c): the design against the Medicare for All Act of 2025 (S. 1506, H.R. 3069), the employer wave re-examined, memo 3 confirmed; its arithmetic in `tools/employer_wave.py`. Evidence EV-CAR-270 to 316 (block 270-329 reserved for this note); sources SRC-3260 to 3280.

## Shared rules care is likely to own or touch

From `dossiers/shared-rules.md`; proposed in the design section, never overwritten here:
- **Rule 7, services that make housing work:** care owns it (HLT-4).
- **Rule 3, which immigrants are eligible:** owned by the immigration flagship; care states the exception it needs for coverage (for example whether a universal program covers everyone resident).
- **Rules 1, 2 and 4** (income, phase-outs, income lines): health premium credits and Medicaid use the poverty guidelines and phase out on their own schedules; owned by the secure floor.
- **Rule 8, the workforce:** care workers; owned by the immigration and work flagships.

## Open questions for Espen

1. **Health, section 3:** decided (`DEC-2026-11-10-09`, `-11`, `-12`).
2. **Health, section 6, part 3:** soften the hospital transition with a capped transition fund and a revenue floor for rural and safety-net global budgets, keeping the five-year glide path (HLT-7.15)? Recommended: yes.
