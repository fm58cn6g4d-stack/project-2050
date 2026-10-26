# Capacity recovery budget review: IRS, CMS, HUD, Education

**Status:** review-ready (Claude Code, Oct 26, 2026; branch `claude/pensive-mendel-g1lwl5` from main 7bddcb1, draft PR #22).

**What this is.** Evidence and a recommended allocation. Nothing here is adopted. Data: [capacity-recovery-components.csv](capacity-recovery-components.csv). Arithmetic: `python3 index/tools/capacity-review/review.py` (add `--json` for the numbers). The script only reads.

**Scope.** It tests the approved envelopes in `index/data/inputs/recovery-adoption.json` against real budgets, staffing and agenda workload at four agencies. The envelopes are:
- **CAP-7S, the surge:** $300B, a lifetime amount, available on enactment.
- **CAP-7, the sustained increase:** $300B over FY2030-39.
- **The IRS receipt-risk allowance:** $200B.

The four agencies are the IRS, CMS, HUD and the Education Department (ED). Other agencies are out of scope, and so are operating manuals and the other queued work.

## Recommendation in brief

1. **Allocate about $124B of the $600B to these four agencies, mostly as sustained funding (range $73-179B; table below).**
   - That is less than half their pro-rata share of the new envelopes ($265B) and about a quarter of the old unsourced split ($481B).
   - What these agencies need is mainly **recurring**: restoring staff lost in 2025, plus ongoing agenda workload.
   - About $22B is surge and about $102B is sustained.
2. **Keep both envelope totals for now, and hold the remainder unallocated:** about $278B of surge and $198B of sustained.
   - Other agencies are not reviewed yet. SSA comes next and is probably the largest.
   - **Watch the shape.** If other agencies also turn out to need mostly recurring money, the surge is oversized and the sustained line is tight. Moving money from surge to sustained is not neutral under D4-B: the sustained line must be paid for at maturity, while the surge is borrowed inside the envelope.
3. **IRS: give it about $77B (range $47-107B), of which about $68B is sustained.**
   - **Keep the $200B receipt-risk allowance.** It brings REV-G8 from $0.4T to $0.2T. That is about what CBO's yield ratios give on this much IRS money ($0.18T at the midpoint).
   - Do not allocate less than about $70B to the IRS while G8 counts $0.2T.
   - Do not count G8 above $0.2T unless the IRS gets roughly $130-180B.
   - **Correct the scoring note.** CBO's scorekeeping Guideline 14 excludes enforcement revenue from official scores in every vehicle, reconciliation included. The IRA's $180B yield was only a CBO memo item.
4. **CMS: give it about $22B (range $13-36B), plus explicit program-row costs.**
   - The public plan's claims administration belongs in its premium and in HLT-3's cost.
   - State Medicaid administration belongs in the Medicaid scores, through the federal match.
   - The approved $100B delivery contingency stays the backstop for health delivery risk.
   - The largest CMS item, Medicare claims and contractor operations for HLT-2's new benefits, is still **unpriced**.
5. **HUD: give it about $13B (range $9-20B).**
   - Separately, **HOU-4 is missing housing agencies' administrative fees.** Its $15,200 voucher-year anchor is renewal funding only. FY2026 fees add 8.1% on top.
   - That is a program-row correction (about +$7B mid on HOU-4's increment and +$4B on the $135B housing addition). It is not a capacity cost.
6. **Education Department: give it about $11B (range $6-16B).**
   - School meals (USDA) and child care and pre-K (HHS) are not ED's capacity.
   - The research and statistics restoration (IES and NCES) is already inside EDU-8's row.

| Agency | Surge, lifetime | Sustained, FY2030-39 | Total | FY2040 run rate | Old split (surge + sustained) | Pro rata of $300B + $300B | Unpriced items |
| --- | --- | --- | --- | --- | --- | --- | --- |
| IRS | 9.0 (5.5-14.0) | 68.4 (41.0-92.7) | 77.4 (46.5-106.7) | 8.8 (5.2-11.9) | 236.2 | 130.0 | 2 |
| CMS | 8.0 (4.0-14.0) | 14.5 (8.5-21.8) | 22.5 (12.5-35.8) | 1.9 (1.1-2.8) | 90.8 | 50.0 | 1 |
| HUD | 2.8 (1.6-4.6) | 10.4 (7.0-15.8) | 13.2 (8.6-20.4) | 1.3 (0.9-2.0) | 81.8 | 45.0 | 1 |
| ED | 2.3 (1.1-4.1) | 8.3 (4.7-11.4) | 10.6 (5.8-15.5) | 1.1 (0.6-1.5) | 72.7 | 40.0 | 0 |
| **Four agencies** | **22.1 (12.2-36.7)** | **101.7 (61.2-141.8)** | **123.8 (73.4-178.5)** | **13.0 (7.8-18.1)** | 481.4 | 265.0 | 4 |

**How to read the table:**
- **Units.** $B, nominal; midpoint with the low-high range in brackets. Every allocation figure is a proposal built from the cited evidence (tags are in the CSV).
- **Sustained rows.** Each is an annual cost in FY2026 dollars. It is phased in at 50% in FY2030 and 80% in FY2031, and grows 3.5% a year (both estimates). The resulting multiplier over FY2030-39 is 12.65.
- **Old split.** The historical $600B split plus the same share of the old $490B sustained line.
- **Unpriced items stay unpriced:** the IRS mark-to-market valuation unit and Climate Dividend payments; CMS's HLT-2 claims operations; HUD's ROAD Act programs. They are not hidden in the totals, and the remainder is where they would be funded.

## How the money was tested

- **Increments, not totals.** Each figure is added to the agency's current-law baseline. That baseline is now the reduced, post-2025 level, since CBO projects FY2026 appropriations forward with inflation. "Restoration" therefore counts as new money against the baseline.
- **Budget authority and outlays.** Surge figures are budget authority available on enactment (R1, FY2029). Sustained figures are annual budget authority. For staff-heavy rows that is close to annual outlays (estimate: 90-95% spent in the first year). IT surges spend out over two to four years.
- **FY2029 cash stays unpriced.** The first obligations should go to:
  - IRS hiring and training pipelines, since revenue agents take a year or more to become productive;
  - CMS's HLT-1 conversion;
  - ED's servicing contracts.

  These fit the $10B already shifted into FY2029 (`early_admin_bn`). No FY2029 cash figure is proposed.
- **Recurring versus finite.** Staff, servicing, claims, and running new systems are recurring. They go in CAP-7 even when they are "rebuilding". The surge holds only finite builds: systems, backlogs, launches and reintegration. Putting recurring staff in a surge that ends would mean hiring and then laying off.
- **Administration already financed inside programs** is marked `program_row` in the CSV and kept out of capacity (see Boundaries).

## IRS

**Where it stands.** Treasury's FY2027 budget-in-brief gives the IRS's discretionary money (new appropriations) and its total resources (adding the Inflation Reduction Act money, fees and carryover):

| | FY2025 | FY2026 | FY2027 request |
| --- | --- | --- | --- |
| New appropriations | $12.32B | $11.20B (enacted) | $9.83B |
| Total resources | $20.0B | $16.8B | $15.9B |
| Staff (FTE) | 94,095 | 70,829 | 69,031 |

- The FY2027 request cuts another 4,714 FTE.
- Examination and collection staff rose to 27,217 in FY2024 on IRA hiring. They fell to 17,517 by January 2026 (TIGTA).
- Audit revenue fell from $10B to $6.5B in one year.
- Of the IRA's $78.9B, $53.5B has been rescinded across four laws. The rest is largely used by FY2028 (derived; check).
- For scale: the IRS had about 95,000 FTE in 2010. Real appropriations fell about 20% from 2010 to 2018.

**What rebuilding means.** Return total staff to about 91,000, a little below FY2025:
- about 14,000 in enforcement, which restores roughly the FY2024 enforcement level plus growth;
- about 6,000 in service and operations.

The cost is $212.7K per FTE, which is FY2025's total resources divided by its FTE (derived; $190K in the low case). On top of that:
- about $1B a year to run the systems the IRA modernized;
- a $5-12B surge to continue modernization, at the $2.2B a year the IRA was paying.

**Agenda workload.**
- Monthly Child Tax Credit payments (FAM-1): ARPA's $0.397B paid for six months of advance payments. A permanent monthly system costs more to build and less to run.
- Climate Dividend payments (CLI-2): no agency assigned and no price; check whether CLI-2's cost already includes administration.
- Mark-to-market valuation (REV-G11): no basis found.
- The last two are unpriced.

**Revenue (REV-G8) and the overlap.**
- **No double count.** G8 is **gross** revenue: the CBO and Treasury yields it rests on exclude the funding. The IRS capacity rows are the cost of earning it.
- **How much revenue IRS money yields:**
  - CBO credited the IRA's $79.6B with $180.4B over 2022-31, a ratio of 2.27 inside the window.
  - CBO's 2020 estimate: an extra $20B yields $61B (3.05); $40B yields $103B (2.58). Returns fall as the amount grows.
  - CBO's 2024 rescission estimates run the other way: cutting $20B loses $44B (2.2).
- **Applied here:** about $77B of IRS money yields **$0.17-0.24T** at these ratios ($0.18T at the IRA ratio). The full range is $0.10-0.33T.
- **What each G8 level needs:**
  - G8 at **$0.2T** needs about $66-91B of IRS money.
  - G8 at **$0.4T** needs about $131-182B, or Treasury's much higher yields. Treasury counts deterrence and high-end enforcement, which CBO does not.
- **Verdict:** the **$200B allowance is sensible, not excessive**. It puts G8 at the CBO-convention yield of the IRS money proposed here.
- **Two links to carry in the model:**
  - **Cuts cost revenue.** Every IRS dollar cut below this allocation loses about $2.2-2.5 of G8 (CBO's 2024 rescission ratios). A smaller IRS line is not a saving one-for-one.
  - **Official scores credit none of it.** Guideline 14 excludes the revenue from the official score in every vehicle (Penn Wharton, citing CBO's IRA estimate). G8 can count in the project's own D4 tests, as now, but no bill's official score will credit it. The ledger note "CBO may not score it on a given vehicle" should say "CBO's official score excludes it; CBO reports it as a memo item."

**If the IRS gets less.** Revenue falls, as above. Service also suffers: phone service, refund timing and the reliability of monthly credit payments depend on the service row.

## CMS

**Where it stands** (from the October 21 CMS review, not repeated here):
- Program Management discretionary funding is $4.125B, and $7.38B with collections.
- The broad administrative budget is $12.0B.
- Program Management has about 4,700 FTE.

The review found that the old implied increment ($90.8B over 2030-39) was not a costed plan.

**What is new here.**
- **Federal staff:** the review's own sensitivity of 1,500-3,500 FTE at $250-350K, a midpoint of $0.75B a year.
- **Drug negotiation at 50 drugs a year (HLT-6):** about $0.4B a year (range $0.3-0.5B). The IRA program costs about $0.24B a year for 10-20 drugs (GAO-25-106996).
- **Launch surge:** $8B (range $4-14B) covers four launches at once:
  - the public plan and automatic enrollment;
  - Medicare cap and benefit edits;
  - commercial price-cap compliance;
  - accelerated risk-adjustment audits.

  Past federal launches each received about $1-3B in implementation funding. The IRA's negotiation program got $3B over 12 years.

**What stays out of CMS capacity.** These belong in the program rows:
- public-plan claims administration and reserves (in its premium and HLT-3);
- state Medicaid eligibility systems and casework (in the Medicaid match, which CBO's Medicaid scores normally include);
- marketplace operations (insurer user fees).

**The open item.** Medicare claims and contractor operations for HLT-2's dental, vision and hearing benefits are unpriced, and it is unknown whether HLT-2's score includes them. Until that is settled, the $100B delivery contingency is the backstop. This is the largest unknown in the four agencies.

**If CMS gets less.** Launch dates slip, or the launches ship without enrollment-integrity controls (GAO's marketplace findings). HLT-6's audit-dependent savings also become less certain.

## HUD

**Where it stands.**
- Management and Administration funding is $2.003B (FY2026).
- Staff fell 29%, from about 8,800 to about 6,300, between December 2024 and December 2025, and to about 5,800 by September 2026. More than half of those who left had 10 or more years at HUD (GAO-26-108442).
- Tenant-based rental assistance is $38.4B, including $34.9B of renewals for about 2.3M vouchers. Fees paid to local housing agencies are $2.836B.

**Allocation.**
- Restore about 2,500 staff at $220-300K loaded (estimate): $0.63B a year.
- A credit office for HOU-3's $30B-plus a year of direct loans: about $0.1B a year. Federal credit-reform rules keep loan administration out of the subsidy cost, so it needs its own money.
- HUD oversight of about 2M added vouchers: $0.1B a year.
- A systems and inspection-backlog surge: $2.5B.
- A loan platform: $0.3B.
- The roughly 35 programs the ROAD Act assigned to HUD stay unpriced.

**Program-row correction (proposed to the housing owner).**
- HOU-4's $15,200 anchor is $34.9B ÷ 2.3M, which is renewals only.
- Administrative fees ran 8.1% of renewals in FY2026.
- Adding them raises HOU-4's $90B midpoint increment by about $7B.
- The $135B housing addition carries a 5% allowance. At 8.1% it would be about $4B higher.
- These fees pay local housing agencies, not HUD staff, so they stay out of capacity.

**If HUD gets less.** Vouchers are issued slowly, the loan program cannot originate at scale, and inspections and grant awards lag. GAO already finds these delays at today's staffing.

## Education Department

**Where it stands.**
- FY2025 funding: Student Aid Administration $2.06B (salaries $1.06B plus servicing $1.0B for 43.3M borrowers); Program Administration $0.42B; Office for Civil Rights $0.14B.
- The FY2027 request cuts Program Administration 76% and the civil-rights office 35%.
- Staff fell from 4,133 to about 2,183 after March 2025. No current official count was found.
- Fourteen interagency agreements are moving about 148 programs to six agencies.

**Allocation.**
- Restore about 1,800 staff: $0.40B a year.
- Servicing for statutory income-driven repayment and Public Service Loan Forgiveness (EDU-5): $0.2B a year. Like HUD's loans, servicing sits outside EDU-5's subsidy score under credit-reform rules.
- Civil-rights office restored: $0.06B a year.
- A student-aid systems and backlog surge: $2.0B.
- Reintegrating programs moved by interagency agreement: $0.3B.
- Title I, IDEA, Pell and the educator grants are formula programs. Their monitoring is covered by the restored staff.

**Outside ED.**
- School meals: USDA's Food and Nutrition Service.
- Child care, pre-K and Head Start: HHS's Administration for Children and Families.
- IES and NCES: inside EDU-8's row.

**If ED gets less.** Repayment and loan-forgiveness backlogs return, and the EDU-6 staffing floor has no money behind it.

## Proposed input changes (for the owners; not made here)

1. **`recovery-adoption.json` (Codex).**
   - **No change** to `cap_surge_tn` (0.3), `cap_sustained_tn` (0.3) or `irs_receipt_risk_tn` (0.2).
   - Optionally, record a *proposed, not adopted* allocation block with the four agencies' midpoints:
     - IRS 9.0 surge / 68.4 sustained;
     - CMS 8.0 / 14.5;
     - HUD 2.8 / 10.4;
     - ED 2.3 / 8.3.
   - Record the remainder as unallocated.
   - The midpoint sustained path for the four agencies ($B nominal, FY2030-39) is 4.6, 7.6, 9.9, 10.2, 10.6, 11.0, 11.3, 11.7, 12.2, 12.6. It sits inside the existing sustained profile, so the model's totals do not change.
2. **REV-G8 note** (`ledger-revenue.csv` note text and domain-revenue.md):
   - State that G8 is gross, earned by the IRS capacity rows.
   - Replace "CBO may not score it on a given vehicle" with the Guideline 14 wording above.
   - Add the dependency: G8 at $0.2T assumes at least about $70-90B of IRS capacity funding over FY2030-39.
3. **Housing (housing owner and Codex):** add PHA administrative fees to HOU-4 (+about $7B mid) and lift the housing addition's 5% allowance to about 8% (+about $4B), or say why not.
4. **domain-capacity.md (owner):** once accepted, replace the historical split for these four agencies with this allocation. Mark the overlaps checked: IRS/G8 (no double count), CMS/HLT and HUD/HOU-4 (program-row boundaries above), Education/FAM-4 (outside items listed).
5. **Queue:** this PR moves the row to review-ready. Next bounded step: SSA, then USCIS, on the same method.

## Uncertainty and limits

- **Estimates.** Per-staff costs, the hiring ramp and the 3.5% growth rate are estimates. So are all four agencies' surge sizes, except where the CSV cites an anchor.
- **Staff counts.** Different sources count differently (FTE, on-board headcount, year-end). The CSV labels each.
- **Not checked against primary documents:**
  - FY2026 enacted ED account levels;
  - HUD fee levels, taken from NAHRO's comparison;
  - the TIGTA staffing counts, taken from press reports of the report.
- **IRS yield ratios** are CBO's. They exclude deterrence, and they vary with the mix of enforcement and service spending. Treasury's estimates are several times higher.
- **No official score.** This is not a legal, actuarial or official score, and it was not independently reviewed.

## Sources

- **IRS:**
  - Treasury, [IRS FY2027 Budget in Brief](https://home.treasury.gov/system/files/266/14.-IRS-FY-2027-BIB.pdf);
  - CBO, [Trends in the IRS's Funding and Enforcement](https://www.cbo.gov/publication/56467) (2020);
  - CBO, [IRS rescissions](https://www.cbo.gov/publication/59972) (2024);
  - Penn Wharton, [scoring of IRS funding (Guideline 14)](https://budgetmodel.wharton.upenn.edu/p/2023-11-01-why-are-changes-to-irs-funding-always-scored-as-increasing-the-deficit/);
  - Tax Policy Center, [IRS funding and staffing since 2010](https://taxpolicycenter.org/sites/default/files/2025-04/IRS%20funding%20and%20staffing%20since%202010.pdf);
  - TIGTA staffing findings as reported by the [Journal of Accountancy](https://www.journalofaccountancy.com/news/2026/aug/irs-enforcement-activity-fell-despite-record-tax-collections-tigta.html);
  - ARPA administration funding per [Tax Notes](https://www.taxnotes.com/lr/resolve//3k64z).
- **CMS:**
  - [sources/health-cms-capacity-review-2026-10-21.md](health-cms-capacity-review-2026-10-21.md) and its cited CMS budget documents;
  - GAO, [GAO-25-106996](https://www.gao.gov/products/gao-25-106996).
- **HUD:**
  - CRS, [HUD FY2027 Budget Request: In Brief](https://www.everycrsreport.com/files/2026-04-30_R48927_c91a8d9ad32492c3c02250b542547e4dfe142226.html);
  - GAO, [GAO-26-108442](https://www.gao.gov/products/gao-26-108442);
  - NLIHC, [FY26 final analysis](https://nlihc.org/sites/default/files/FY26_Final_Analysis_021726.pdf);
  - NAHRO, [FY2027 HUD funding](https://www.nahro.org/news/fy2027-hud-funding-house-thud-road-act/).
- **Education Department:**
  - ED, [FY2027 Budget Summary](https://www.ed.gov/media/document/fy-2027-budget-summary-113552.pdf);
  - States Newsroom, [March 2025 staff cuts](https://floridaphoenix.com/2025/03/12/repub/u-s-education-department-to-cut-hundreds-of-staff-members/);
  - EdWeek, [interagency agreements](https://www.edweek.org/policy-politics/the-education-department-will-send-more-of-its-programs-to-other-agencies/2026/02).
