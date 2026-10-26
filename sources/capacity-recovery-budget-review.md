# Capacity recovery budget review: IRS, CMS, HUD, Education

**Status:** review-ready, revised Oct 26 after Codex's review of 762b9b3 (Claude Code; branch `claude/pensive-mendel-g1lwl5` from main 7bddcb1, PR #22).

**Round 2 (Oct 26):** the other CAP-7 agencies are in [capacity-recovery-other-agencies-review.md](capacity-recovery-other-agencies-review.md). Its summary across all 28 agencies supersedes this file's four-agency totals and remainder. It proposes keeping the $300B sustained envelope and cutting the surge to about $100B.

**What this is.** Evidence and a recommended allocation. Nothing here is adopted. Data: [capacity-recovery-components.csv](capacity-recovery-components.csv). Arithmetic: `python3 index/tools/capacity-review/review.py` (add `--json` for the numbers). The script only reads.

**Scope.** It tests the approved envelopes in `index/data/inputs/recovery-adoption.json` against real budgets, staffing and agenda workload at four agencies. The envelopes are:
- **CAP-7S, the surge:** $300B, a lifetime amount, available on enactment.
- **CAP-7, the sustained increase:** $300B over FY2030-39.
- **The IRS receipt-risk allowance:** $200B.

The four agencies are the IRS, CMS, HUD and the Education Department (ED). Other agencies are out of scope, and so are operating manuals and the other queued work.

## Recommendation in brief

1. **Allocate about $148B of the $600B to these four agencies, mostly as sustained funding (range $91-202B; table below).**
   - That is a little over half their pro-rata share of the new envelopes ($265B) and under a third of the old unsourced split ($481B).
   - What these agencies need is mainly **recurring**: restoring staff lost in 2025, plus ongoing agenda workload.
   - About $22B is surge and about $126B is sustained. The total rose from $124B when the IRS enforcement row was enlarged (Espen, Oct 26; item 3).
2. **Keep both envelope totals for now, and hold the remainder unallocated:** about $278B of surge and $174B of sustained.
   - Other agencies are not reviewed yet. SSA comes next and is probably the largest.
   - **Watch the shape.** If other agencies also turn out to need mostly recurring money, the surge is oversized and the sustained line is tight. Moving money from surge to sustained is not neutral under D4-B: the sustained line must be paid for at maturity, while the surge is borrowed inside the envelope.
3. **IRS: give it about $101B (range $64-130B), of which about $92B is sustained.** Of that, $62B is enforcement and $40B is support: service, systems and payments.
   - **Decided (Espen, Oct 26): fund more enforcement (option a).**
     - The enforcement row rises from +14,000 to **+24,000 FTE** (range 18,000-28,000), hired over three years (30/60/90% in FY2030-32). That is about 8,000 hires a year, near the FY2024 pace.
     - It costs about $24B more over FY2030-39.
   - **Revenue.** On CBO-based enforcement ratios adjusted for scale, with a one- to two-year lag, the enforcement row yields about **$0.13-0.14T** in the window (range $0.085-0.18T). The smaller row yielded $0.09-0.10T.
   - **It still falls short of $0.2T.** Reaching $0.2T on these ratios would need about $78-91B of enforcement funding, more than hiring pace and falling returns support.
   - **Recommended allowance: about $250B** (G8 counted at about $0.15T). That is this enforcement yield plus a small credit for the support spending; the IRA's package ratio, a looser comparator, gives about $0.23T on this allocation.
     - The allowance is a shared fiscal input, so Codex makes the change.
     - Until then, $200B stays the provisional value.
     - The rejected alternatives were (b) raising the allowance to about $300B without more enforcement, and (c) keeping $200B on a non-CBO basis.
   - **It helps the 2040 test.** The bigger build adds about $3.4B a year to the IRS's FY2040 sustained cost ($12.2B against $8.8B). On these ratios the enforcement row alone returns about $20B a year by then.
   - **Correct the scoring note.** CBO's scorekeeping Guideline 14 excludes enforcement revenue from official scores in every vehicle, reconciliation included. The IRA's $180B yield was only a CBO memo item.
4. **CMS: give it about $22B (range $13-36B), plus explicit program-row costs.**
   - The public plan's claims administration belongs in its premium and in HLT-3's cost.
   - State Medicaid administration belongs in the Medicaid scores, through the federal match.
   - The approved $100B delivery contingency stays the backstop for health delivery risk.
   - The largest CMS item, Medicare claims and contractor operations for HLT-2's new benefits, is still **unpriced**.
5. **HUD: give it about $13B (range $9-20B).**
   - Separately, **HOU-4 is missing housing agencies' administrative fees** across the whole adopted million-award package. Its $15,200 voucher-year anchor is renewal funding only, and FY2026 fees add 8.1% on top.
   - The correction is about **+$12.2B** on HOU-4's $150B midpoint (range $8.1-15.2B), counted once inside HOU-1. It is a program-row correction, not a capacity cost.
   - For HOU-4D's $135B, which carries 5%, the default reading keeps the approved envelope and buys about 2.9% fewer awards. The alternative is about +$4.0B if a fixed cohort is adopted.
6. **Education Department: give it about $11B (range $6-16B).**
   - School meals (USDA) and child care and pre-K (HHS) are not ED's capacity.
   - The research and statistics restoration (IES and NCES) is already inside EDU-8's row.

| Agency | Surge, lifetime | Sustained, FY2030-39 | Total | FY2040 run rate | Old split (surge + sustained) | Pro rata of $300B + $300B | Unpriced items |
| --- | --- | --- | --- | --- | --- | --- | --- |
| IRS | 9.0 (5.5-14.0) | 92.4 (58.2-116.2) | 101.4 (63.7-130.2) | 12.2 (7.7-15.3) | 236.2 | 130.0 | 2 |
| CMS | 8.0 (4.0-14.0) | 14.5 (8.5-21.8) | 22.5 (12.5-35.8) | 1.9 (1.1-2.8) | 90.8 | 50.0 | 1 |
| HUD | 2.8 (1.6-4.6) | 10.4 (7.0-15.8) | 13.2 (8.6-20.4) | 1.3 (0.9-2.0) | 81.8 | 45.0 | 1 |
| ED | 2.3 (1.1-4.1) | 8.3 (4.7-11.4) | 10.6 (5.8-15.5) | 1.1 (0.6-1.5) | 72.7 | 40.0 | 0 |
| **Four agencies** | **22.1 (12.2-36.7)** | **125.7 (78.4-165.2)** | **147.8 (90.6-201.9)** | **16.5 (10.3-21.6)** | 481.4 | 265.0 | 4 |

**How to read the table:**
- **Units.** $B, nominal; midpoint with the low-high range in brackets. Every allocation figure is a proposal built from the cited evidence (tags are in the CSV).
- **Sustained rows.** Each is an annual cost in FY2026 dollars. It is phased in at 50% in FY2030 and 80% in FY2031, and grows 3.5% a year (both estimates). The resulting multiplier over FY2030-39 is 12.65. The IRS enforcement row phases in more slowly: 30%, 60% and 90% in FY2030-32.
- **Old split.** The historical $600B split plus the same share of the old $490B sustained line.
- **Unpriced items stay unpriced:** the IRS mark-to-market valuation unit and Climate Dividend payments; CMS's HLT-2 claims operations; HUD's ROAD Act programs. They are not hidden in the totals, and the remainder is where they would be funded.

## How the money was tested

- **Increments, not totals.** Each figure is added to the agency's current-law baseline. That baseline is now the reduced, post-2025 level, since CBO projects FY2026 appropriations forward with inflation. "Restoration" therefore counts as new money against the baseline.
- **Budget authority and outlays.** Surge figures are budget authority available on enactment (R1, FY2029). Sustained figures are annual budget authority. For staff-heavy rows that is close to annual outlays (estimate: 90-95% spent in the first year). IT surges spend out over two to four years.
- **FY2029: availability, obligations and cash.**
  - **Legal availability:** the whole surge is available on R1 enactment, assumed about April 2029 (the ledger's HLT-1 input). That leaves about five to six months of FY2029.
  - **First priorities:**
    - IRS hiring and training, since revenue agents take a year or more to become productive;
    - CMS's HLT-1 conversion for plan year 2030;
    - ED's servicing contracts;
    - the start of HUD's restoration.
  - **Bounded estimate for the four agencies** (CSV rows marked `fy2029`):
    - obligations of about **$2.6B (range $1.2-5.4B)**;
    - cash of about **$0.8B (range $0.3-2.2B)**.
    - Cash is lower than obligations because hires are on payroll for only a few months and contracts spend out over years.
  - **What fits the $10B and what is unresolved.** The four agencies' FY2029 cash fits inside the $10B of surge cash shifted into FY2029 (`early_admin_bn`). But that $10B is for every surge agency, not just these four. Whether it covers SSA, USCIS and the others is **unresolved** until they are reviewed.
  - **If enactment slips** toward the end of FY2029, FY2029 cash approaches zero and the work moves into FY2030.
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

**What rebuilding means.** Return total staff to about 101,000, above FY2025's 94,000:
- about 24,000 in enforcement (raised from 14,000 on Espen's Oct 26 decision). That restores the FY2024 enforcement level and goes beyond it, hired at about 8,000 a year;
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
- **Separate enforcement from support.** Of the $101B, **$61.6B (range $41-72B) is enforcement**: the enforcement staffing row. **$39.7B is support**: service, operating systems, the monthly-credit payment rows and the modernization surge. Enforcement is 61% of this allocation; it was 58% of the original IRA package.
- **Which comparator applies to what:**
  - **CBO 2020** ($20B yields $61B, a ratio of 3.05; $40B yields $103B, 2.58): added funding for examinations and collections, spread over 2021-30. It applies to the enforcement row only. Returns fall as the amount grows. For a row near $60B the script uses 2.3 as the midpoint (extrapolated from CBO's two points; derived) and CBO's $40B ratio, 2.58, as the high.
  - **CBO 2024** (cutting $20B loses $44B, 2.2; cutting $35B loses $89B, 2.54): rescissions taken from enforcement. It applies to the enforcement row and to cuts in it.
  - **IRA memo** ($79.6B yields $180.4B, 2.27): a mixed package, 58% enforcement. It is only a cross-check on the whole allocation, adjusted for this allocation's enforcement share. Service and modernization have no separate CBO yield estimate.
- **Lag and window.** Each CBO ratio is an in-window figure for funding spread evenly over ten years, so it already contains hiring and collection lags. This path is back-loaded (phase-in plus growth). The script turns each ratio into a steady multiple at a one- or two-year lag and counts only revenue that lands by FY2039. Revenue from late-window hires falls after 2039 and is not counted.
- **Results:**
  - **The enforcement row yields about $0.13-0.14T at the midpoint** ($0.085T low funding at 2.2; $0.18T high funding at 2.58). The lag choice moves it by about $0.005T.
  - The IRA cross-check gives $0.23-0.24T. That is an upper reading: it credits support spending at the IRA's package rate and ignores falling returns.
  - Before Espen's decision, the +14,000 row yielded $0.09-0.10T (at CBO's 2.58 midpoint).
- **What each G8 level needs:**
  - G8 at **$0.15T** needs about $58-68B of enforcement funding, which is this row.
  - G8 at **$0.2T** needs about $78-91B. That would mean about +29,000 enforcement FTE hired more slowly, and on this scheme it yields only about $0.16T inside the window, because returns fall with scale and late hires pay off after 2039.
  - G8 at **$0.4T** needs Treasury-type yields. Treasury counts deterrence and high-end enforcement, which CBO does not.
- **Verdict:**
  - With the larger enforcement row, the evidence supports G8 at about **$0.15T**: a **$250B allowance**, recommended in place of the provisional $200B.
  - Counting $0.2T would still rest on yields CBO does not count.
- **Two links to carry in the model:**
  - **Enforcement cuts cost revenue.** A cut to the *enforcement* row loses about $2.2-2.5 per dollar (CBO 2024, which cut enforcement). A cut to service or modernization has no CBO yield estimate. It may still lower enforcement productivity and service quality, but that is not quantified here.
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
- **The anchor is renewals only.** HOU-4's $15,200 anchor is $34.9B ÷ 2.3M. Administrative fees ran 8.1% of renewals in FY2026 ($2.836B).
- **Neither earlier figure contains the fees.** Rebuilt at the anchor with 3% growth, half-year first-year cost, full lease-up and no attrition:
  - the old 400,000-award path costs **$64B** in renewal funding alone, more than the old **$60B** (Bill Book 12; archive, ideas only);
  - the adopted one-million-award path costs **$161B**, more than the adopted **$150B** midpoint.

  Neither carried figure can include fees on top of rents. The likelier reading is that each embeds incomplete lease-up or a lower rent path. The source does not say, and that is for the housing owner to settle.
- **The correction covers the whole package.** It applies to all of HOU-4, the earlier $60B and the $90B expansion alike: **+$12.2B mid ($8.1B / $12.2B / $15.2B on $100B / $150B / $187.5B)**. It is counted once, in HOU-4's component inside HOU-1, not added to HOU-1 again.
- **HOU-4D ($135B, 5% allowance; no cohort adopted).** Two readings:
  - **Fixed envelope (default):** keep the approved $135B and accept about **2.9% fewer awards**, about 29,000 of the illustrative million.
  - **Fixed delivery:** if a specific cohort is later adopted, it costs about **+$4.0B**.

  This correction is separate from HOU-4's and is not double counted.
- **Not a capacity cost.** These fees pay local housing agencies, not HUD staff, so they stay out of capacity.

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
     - IRS 9.0 surge / 92.4 sustained;
     - CMS 8.0 / 14.5;
     - HUD 2.8 / 10.4;
     - ED 2.3 / 8.3.
   - Record the remainder as unallocated.
   - The midpoint sustained path for the four agencies ($B nominal, FY2030-39) is 4.7, 8.5, 11.9, 12.9, 13.4, 13.9, 14.4, 14.9, 15.4, 15.9. It sits inside the existing sustained profile, so the model's totals do not change.
2. **REV-G8 note** (`ledger-revenue.csv` note text and domain-revenue.md):
   - State that G8 is gross, earned by the IRS capacity rows.
   - Replace "CBO may not score it on a given vehicle" with the Guideline 14 wording above.
   - Add the dependency: G8 at about $0.15T rests on about $62B of IRS *enforcement* funding over FY2030-39 (+24,000 FTE). Cutting that row loses about $2.2-2.5 of G8 per dollar.
   - **In `recovery-adoption.json`, set `irs_receipt_risk_tn` from 0.2 to 0.25** (Espen chose option (a) on Oct 26; this is the matching allowance). Effect: G8 counted at about $0.15T, $50B less revenue over FY2030-39, on G8's existing annual profile. The extra IRS spending (+$24B) stays inside the unchanged $300B sustained envelope.
3. **Housing (housing owner and Codex):**
   - Add PHA administrative fees to all of HOU-4: +$12.2B mid ($8.1-15.2B), once, inside HOU-1. Or show that the carried $150B already includes them.
   - Treat HOU-4D's fee gap as about 2.9% fewer awards within $135B, unless a fixed cohort is adopted (then +$4.0B).
4. **domain-capacity.md (owner):** once accepted, replace the historical split for these four agencies with this allocation. Mark the overlaps checked: IRS/G8 (no double count), CMS/HLT and HUD/HOU-4 (program-row boundaries above), Education/FAM-4 (outside items listed).
5. **Queue:** this PR moves the row to review-ready. Next bounded step: SSA, then USCIS, on the same method.

## Uncertainty and limits

- **Estimates.** Per-staff costs, the hiring ramp and the 3.5% growth rate are estimates. So are all four agencies' surge sizes, except where the CSV cites an anchor.
- **Staff counts.** Different sources count differently (FTE, on-board headcount, year-end). The CSV labels each.
- **Not checked against primary documents:**
  - FY2026 enacted ED account levels;
  - HUD fee levels, taken from NAHRO's comparison;
  - the TIGTA staffing counts, taken from press reports of the report.
- **IRS yield ratios** are CBO's. They exclude deterrence and apply here only to the enforcement row. The lag treatment is a simple bound (a one- or two-year delay before a dollar yields), not a model of case cycles; large-corporate cases average about 36 months (IRS FY2027 budget-in-brief). Treasury's estimates are several times higher.
- **FY2029 figures** are bounded estimates that depend on the R1 date. They are not a priced spend plan.
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
