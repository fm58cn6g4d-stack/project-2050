# Capacity recovery review, round 2: the other agencies

**Status:** review-ready (Claude Code, Oct 26, 2026; branch `claude/pensive-mendel-g1lwl5` from main aa8552d, PR #23). Evidence and a recommendation; nothing here is adopted.

**Method.** Same as round 1 ([IRS, CMS, HUD, Education](capacity-recovery-budget-review.md)). Each agency is sized from:
- its current-law baseline (FY2026 enacted, or the nearest verified level);
- its staffing losses since January 2025;
- the workload the domain files actually assign it.

Administration that program rows, fees or trust funds already carry is kept out. **Surge** holds finite builds. **Sustained** holds recurring staff and operations. Data: [capacity-recovery-components.csv](capacity-recovery-components.csv) (174 rows). Arithmetic: `python3 index/tools/capacity-review/review.py`. Units are $B, nominal, midpoint with the range in brackets. All allocation figures are proposals; the CSV tags each one's basis.

## Recommendation in brief

1. **The sustained envelope fits; the surge envelope does not.**
   - Across all 28 agencies sized in both rounds, the project's stated needs come to:
     - **sustained: about $227B (range $138-314B) of the $300B over FY2030-39;**
     - **surge: about $38B (range $20-66B) of the $300B.**
   - The 28 agencies are round 1's four, the 20 left on the CAP-7 list, and four agencies off the list that the domain files assign work to.
   - Most rebuilding is recurring: it means rehiring staff and keeping them. Finite builds (systems, backlogs, launches) are small by comparison.
2. **Keep the sustained envelope at $300B.** The $73B of headroom covers:
   - the top of the range ($314B);
   - unpriced recurring items, mainly CMS's Medicare claims operations for HLT-2's new benefits;
   - agencies a later domain decision may add.
3. **Cut the surge envelope from $300B to about $100B.** This changes an approved working allocation, so it is Espen's call.
   - **Why $100B.** It covers the top of the range ($66B) plus about $35B for unpriced finite builds:
     - the IRS's dividend system and mark-to-market unit;
     - HUD's ROAD Act programs;
     - surprises.
   - **Effect.** About $200B less borrowing inside the D4-B investment envelope, mostly FY2030-35. FY2040 is unaffected, because the surge ends. Interest is lower.
   - **Smaller cut.** If Espen prefers a smaller cut, $150B still leaves more than double the high estimate.
   - **No surge-to-sustained transfer is needed.** Sustained fits as it is.
4. **Cut the FY2029 cash shift from $10B to about $5B.**
   - FY2029 cash for every reviewed agency is about **$1.7B (range $0.5-4.5B)**; obligations are about $5.2B (range $2.1-10.5B).
   - That resolves the open question from round 1. The $10B covers everyone with room to spare, so $5B still covers the high case.
5. **Six agencies change most against the old unsourced split** (round-2 figures are surge plus sustained over FY2030-39):

| Agency | Old split, 2030-39 | This review | Why |
| --- | --- | --- | --- |
| NOAA | $73B | $2.3B | Satellites and research are program spending, not capacity. Its articulated work is weather staff and flood-map data |
| FTA | $55B | $0.1B | Moving America funds FTA's administration from 2031 (sec. 5334, $0.9-1.0B a year). Only a FY2029-30 bridge remains |
| USCIS | $84B | $9.2B | About 97% fee-funded. Legalization adjudication and its 12,000 hires are fee-funded. CAP pays the asylum corps, the backlog and online filing |
| Development agency (USAID successor) | $109B | $19.7B | Operating capacity only. **The foreign-assistance program level is not set anywhere in the project** (see below) |
| SSA | $100B | $29.8B | Restores about 8,000 staff plus workload growth. **The OASDI share is paid from the trust funds under current law** |
| CDC | $27B | $9.1B | Rehiring plus a biosurveillance build. NSC-8's grants are program spending |

6. **Two decisions surfaced for Espen:**
   - **Foreign-assistance program level.** FY2026 foreign assistance is $35.0B (CRS). No domain file sets a level to restore or hold. The development agency's capacity should follow that decision, not lead it.
   - **SSA financing.** Under current law, the Social Security share of SSA's administration is charged to the trust funds. Either CAP-7 pays it explicitly from the general fund, or the funds model carries it as a small trust-fund cost. Codex should route it one way, once.

## All agencies

| Agency | Surge, lifetime | Sustained, FY2030-39 | Total | FY2040 run rate | Old split (surge + sustained) |
| --- | --- | --- | --- | --- | --- |
| IRS (round 1) | 9.0 (5.5-14.0) | 92.4 (58.2-116.2) | 101.4 (63.7-130.2) | 12.2 | 236.2 |
| CMS (round 1) | 8.0 (4.0-14.0) | 14.5 (8.5-21.8) | 22.5 (12.5-35.8) | 1.9 | 90.8 |
| HUD (round 1) | 2.8 (1.6-4.6) | 10.4 (7.0-15.8) | 13.2 (8.6-20.4) | 1.3 | 81.8 |
| ED (round 1) | 2.3 (1.1-4.1) | 8.3 (4.7-11.4) | 10.6 (5.8-15.5) | 1.1 | 72.7 |
| SSA | 3.9 (2.0-6.8) | 25.9 (13.2-37.4) | 29.8 (15.2-44.2) | 3.3 | 99.9 |
| USCIS | 3.5 (1.8-6.0) | 5.7 (3.3-10.1) | 9.2 (5.1-16.1) | 0.7 | 83.6 |
| Development agency | 2.0 (1.0-3.5) | 17.7 (12.7-20.2) | 19.7 (13.7-23.7) | 2.3 | 109.0 |
| State (diplomacy) | 0.5 (0.3-1.0) | 11.4 (6.3-17.7) | 11.9 (6.6-18.7) | 1.5 | 14.5 |
| CDC | 1.5 (0.8-3.0) | 7.6 (4.6-12.7) | 9.1 (5.4-15.7) | 1.0 | 27.2 |
| FEMA | 1.0 (0.5-1.8) | 9.5 (6.1-12.4) | 10.5 (6.6-14.2) | 1.2 | 14.5 |
| NOAA | 0.5 (0.3-1.0) | 1.8 (1.1-2.8) | 2.3 (1.4-3.8) | 0.2 | 72.7 |
| FTA | 0.15 (0.1-0.3) | 0 | 0.15 | 0 | 54.5 |
| EPA | 0.2 (0.1-0.4) | 1.8 (1.0-3.0) | 2.0 (1.1-3.4) | 0.2 | 9.1 |
| DOE (loan and grid offices) | 0.2 (0.1-0.4) | 1.3 (0.9-1.9) | 1.5 (1.0-2.3) | 0.2 | 7.3 |
| DOL (Wage and Hour, OSHA) | 0.2 (0.1-0.4) | 4.6 (2.7-6.3) | 4.8 (2.8-6.7) | 0.6 | 10.9 |
| NLRB | 0.05 | 1.9 (1.3-3.2) | 1.9 (1.3-3.3) | 0.2 | 7.3 |
| FTC and DOJ Antitrust | 0 | 0.4 (0-1.0) | 0.4 (0-1.0) | 0.0 | 5.5 |
| Integrity units (FinCEN, FARA, OGE) | 0.2 (0.1-0.4) | 1.9 (1.0-3.0) | 2.1 (1.1-3.4) | 0.2 | 21.8 |
| FEC | 0 | 0.5 (0.3-0.8) | 0.5 (0.3-0.8) | 0.1 | 5.5 |
| EAC | 0 | 0.4 (0.3-0.6) | 0.4 (0.3-0.6) | 0.0 | 5.5 |
| OPM | 0.3 (0.1-0.6) | 1.0 (0.6-1.5) | 1.3 (0.8-2.1) | 0.1 | 18.2 |
| Civil-rights offices (DOJ, EEOC, HHS) | 0 | 2.3 (1.5-3.3) | 2.3 (1.5-3.3) | 0.3 | 10.9 |
| NIST CAISI and DOE labs | 0.3 (0.1-0.6) | 1.6 (0.8-2.5) | 1.9 (0.9-3.1) | 0.2 | 10.9 |
| ATF and NICS | 0.1 (0.05-0.2) | 0.6 (0.4-1.3) | 0.7 (0.4-1.5) | 0.1 | 9.1 |
| HHS ACF (not on list) | 1.0 (0.5-2.0) | 1.9 (1.0-3.8) | 2.9 (1.5-5.8) | 0.2 | — |
| HRSA (not on list) | 0 | 0.6 (0.3-1.3) | 0.6 (0.3-1.3) | 0.1 | — |
| USDA FNS (not on list) | 0 | 0.4 (0.1-0.8) | 0.4 (0.1-0.8) | 0.0 | — |
| Treasury Fiscal Service (not on list) | 0.3 (0.15-0.6) | 0.6 (0.3-1.3) | 0.9 (0.4-1.9) | 0.1 | — |
| **All 28** | **38.0 (20.4-65.8)** | **227.0 (137.8-314.1)** | **265.0 (158.3-379.9)** | **29.4** | 1,079 |

The old split column is the historical $600B split plus the same share of the old $490B sustained line. The batch 4 items (State, civil rights, CAISI, ATF/NICS and USCIS's asylum $6B) were proposals against its $37B reserve.

**Midpoint sustained path, all agencies, $B nominal FY2030-39:** 9.3, 16.1, 21.7, 23.1, 23.9, 24.8, 25.7, 26.5, 27.5, 28.4.

## Agency notes

**SSA.**
- **Baseline.** Administrative budget (LAE) $14.84B in FY2026: base $12.27B, program integrity $2.40B.
- **Staff.** About 57,000 in January 2025, about 49,000 in February 2026. State disability examiners (DDS) are about 13,700 more.
- **Backlog.** Initial disability claims pending: 862,000, down from a 1.26 million peak. The inspector general disputes SSA's phone metrics.
- **Proposal, sustained:**
  - restore about 8,000 staff, about $200K per staff year: $1.6B a year;
  - workload growth: $0.4B a year;
  - Climate Dividend payments to beneficiaries: $0.05B a year. SSA pays beneficiaries, per domain-climate.md.
- **Proposal, surge:**
  - IT modernization: $3B;
  - disability backlog clearance: $0.5B;
  - systems for the D8 benefit changes and the dividend: $0.4B.
- **Financing boundary.** The OASDI share of SSA's administration is paid from the trust funds under current law.

**USCIS.**
- **Baseline.** About 12 million cases pending (May 2026), up about 2 million since January 2025. Appropriations are under 5% of the budget.
- **Fee-funded (boundary):** IMM-6's 12,000 hires for legalization, and any start-up advance, which fees repay.
- **Proposal, sustained:** asylum officers and refugee processing (IMM-3), which fees barely cover: $0.43B a year. Overlap check: IMM-3 already carries about $0.01T of processing costs.
- **Proposal, surge:** backlog clearance, about $0.7B a year for four to five years (the anchor is a member request): $3B; online filing: $0.5B.

**Development agency and State.**
- **Baseline.** USAID's operating budget fell from $1.57B (FY2025) to $0.11B (FY2026). Foreign assistance is $35.0B; State's Diplomatic Programs $9.36B.
- **Development agency.** Restoring the operating budget at the FY2025 program scale costs about $1.4B a year, plus a $2B rebuild surge. Size it to whatever program level Espen chooses.
- **State (NSC-4).** Restore about 3,000 positions at about $300K each: $0.9B a year. The about-3,000 figure for 2025 departures is as widely reported, not verified here. A $0.5B training surge.

**CDC (NSC-8).**
- **Baseline.** About $9.25B in FY2024 (CDC and ATSDR). FY2026 enacted not found. About 3,000-4,300 staff lost from 13,674 (secondary source).
- **Proposal.** Rehire about 3,000 ($0.6B a year) and a $1.5B biosurveillance and data build. BARDA and the preparedness grants stay in NSC-8's program cost.

**FEMA (CLI-7).**
- **Baseline.** Staff fell from 25,134 to 20,968 (April 2026). GAO found the cuts were made without a workforce analysis.
- **Proposal.** Rehire about 4,000 ($0.7B a year), less any share the Disaster Relief Fund pays. Independence costs $0.05B a year. The Universal Survivor Application and the regional rebuild are a $1B surge.
- **Boundary.** The flood maps themselves are CLI-7's unscored program work.

**NOAA.**
- **Baseline.** $6.1B (FY2026). The National Weather Service lost about 560-600 positions in 2025, with partial rehiring.
- **Proposal.** Staff restoration ($0.14B a year) and a $0.5B surge for precipitation and coastal data that future-conditions flood maps need.

**FTA.**
- **Baseline.** Staff fell from 781 (FY2024) to 552 (FY2026).
- **Covered from 2031.** Moving America funds planning, administration and oversight at $0.9-1.0B a year from 2031.
- **Proposal.** Only a FY2029-30 bridge: $0.15B.

**EPA (CLI-4).**
- **Baseline.** $8.82B in FY2026. About 3,300 FTE lost (20%).
- **Proposal.** The domain files ask only for the air office and enforcement behind CLI-4: about 700 staff, $0.14B a year. Restoring all of EPA (about $0.66B a year) would need a domain decision first.

**DOE and FERC.**
- **Baseline.** 123 of the Loan Programs Office's 210 staff took buyouts.
- **Proposal.** Loan and grid office staff, $0.1B a year (partly recoverable from loan fees).
- **Boundary.** FERC recovers its costs through annual charges.

**DOL.**
- **Baseline.** Wage and Hour investigators: 611 (May 2025), against a 2012 peak of 1,067. OSHA federal officers: 629 (September 2025), against 878 in FY2023.
- **Proposal.** About 1,300 Wage and Hour staff ($0.23B a year) and about 700 OSHA staff ($0.13B a year) for LAB-4, LAB-6 and LAB-7.
- **Boundary.** Participation (LAB-10) and AI transition (AI-4) administration stay inside those rows.

**NLRB.**
- **Baseline.** Field staff are about 510 against about 670 needed.
- **Proposal.** $0.15B a year: a former general counsel's estimate of about $100M for current law, plus the PRO Act caseload.

**FTC and DOJ Antitrust.**
- **Baseline.** The FTC's $384M is mostly merger fees; DOJ Antitrust's $245M is fee-funded.
- **Proposal.** CAP pays only what COM-2's fees miss: about $0.03B a year.

**Integrity, FEC, EAC and OPM** (sized from CRS FY2026 levels):
- FinCEN ($185M): beneficial-ownership enforcement, $0.1B a year.
- DOJ FARA unit: $0.02B a year.
- OGE ($23M): $0.03B a year.
- FEC ($81M): an enforcement bureau, $0.04B a year.
- EAC ($59M): $0.03B a year.
- OPM ($418M): $0.08B a year plus a $0.3B HR systems surge.
- SEC staffing for INT-15 is fee-funded.

**Batch 4 items.**
- **Civil-rights offices** (DOJ lost more than 250 of about 380 attorneys): $0.18B a year with EEOC and HHS. ED's civil-rights office is in round 1.
- **NIST CAISI** (appropriated $10M; outside estimates of need run $26-84M) plus DOE lab evaluation: $0.13B a year and a $0.3B testbed surge.
- **ATF and NICS:** $0.05B a year. No verified baseline was found.

**Agencies not on the CAP-7 list that the domain files assign work to.** These were not reviewed in depth:
- **HHS ACF** runs FAM-2's child care and pre-K: $0.15B a year plus a $1B build. It is the largest.
- **HRSA** for HLT-4.
- **USDA FNS** for EDU-3.
- **Treasury's Fiscal Service**, which disburses the monthly credit and the dividend.

**Not added.**
- AmeriCorps: inside LAB-9.
- Immigration courts: inside CRT-5.

## Proposed input changes (for the owners; not made here)

1. **`recovery-adoption.json` (Codex), if Espen accepts:**
   - `cap_surge_tn` 0.3 → **0.1**;
   - `early_admin_bn` 10 → **5**;
   - `cap_sustained_tn` stays 0.3.
   - Optionally record the per-agency allocation and the sustained path above as a *proposed* block.
2. **SSA financing (Codex).** Route the OASDI share of SSA's increase through the funds model, or state that CAP-7 pays it from the general fund.
3. **Governing record (on Espen's decision).**
   - Record the surge cut.
   - Record the foreign-assistance program-level question as open.
   - Add ACF, HRSA, FNS and the Fiscal Service to D9's list, or say why not.
4. **domain-capacity.md (owner).** Replace the historical split table with these allocations once accepted, and mark the overlap notes resolved:
   - FTA and Moving America: covered by sec. 5334.
   - FTC and COM-2: fees cover most.
   - NOAA: program, not capacity.
   - CDC and NSC-8: named work sized.

## Uncertainty and limits

- **Estimates.** Per-staff costs, staffing restoration targets, surge sizes and the FY2029 figures are estimates. So are the unlisted-agency rows, which are not reviewed in depth.
- **Secondary and missing baselines:**
  - Several staffing figures come from press or advocacy reporting: CDC, State, NOAA and the DOJ Civil Rights Division.
  - FY2026 enacted levels were not found for CDC, ATF or NICS.
- **Sized only to written needs.** These figures cover needs the domain files actually state. A later decision that adds work to an agency (all of EPA, foreign-assistance programs) adds to them.
- Not an official score.

## Sources

- **SSA:**
  - CRS, [SSA LAE FY2027](https://www.everycrsreport.com/files/2026-07-28_R49047_9cc5620b83db19704e98e943df28afde352a6afb.html);
  - SSA, [FY2027 testimony](https://waysandmeans.house.gov/wp-content/uploads/2026/06/SSA-Testimony-FY-2027-Budget.pdf);
  - staffing per CRS as summarized by the [Alliance for Retired Americans](https://retiredamericans.org/new-report-confirms-steep-decline-in-social-security-administration-staffing-levels/);
  - CBPP, [SSA customer service](https://www.cbpp.org/research/social-security/trump-administration-personnel-policies-harming-social-security-customer).
- **USCIS:**
  - [Moulton letter](https://moulton.house.gov/news/press-releases/moulton-leads-letter-demanding-answers-backlog-uscis);
  - [Correa letter](https://correa.house.gov/news/press-releases/correa-calls-to-tackle-immigration-backlog);
  - CRS, [USCIS operations](https://www.everycrsreport.com/reports/R48021.html).
- **State and development:** CRS, [SFOPS/NSRP FY2026](https://www.everycrsreport.com/files/2026-07-15_R48624_48cf729af75f7e8e8c710d63e39078520bd54f59.html).
- **CDC:**
  - TFAH, [CDC budget fact sheet](https://www.tfah.org/wp-content/uploads/2025/09/TFAH_Report-Congressional-Fact-Sheet-Text_091725_vfinal-dl.pdf);
  - [Fedtools on CDC staffing](https://www.fedtools.com/blog/cdc-workforce-cuts-2026) (secondary).
- **FEMA:** GAO, [GAO-26-108427](https://www.gao.gov/products/GAO-26-108427); [Taxpayers for Common Sense](https://www.taxpayer.net/disaster/government-watchdog-dings-fema-for-staff-reductions-and-lack-of-planning/).
- **NOAA:** [NPR on National Weather Service rehiring](https://www.hppr.org/2025-06-03/stabilizing-operations-the-national-weather-service-hires-again-after-trump-cuts).
- **EPA:** CRS, [EPA FY2026](https://www.everycrsreport.com/files/2026-03-25_IF13191_951e03a5009e0c3ed51fa505a446ad16444b361d.html).
- **DOE:** [ANS on the loan office](https://www.ans.org/news/article-6972/nuclear-); FAS, [DOE staff shortages](https://fas.org/publication/doe-staff-shortages/).
- **DOL and NLRB:**
  - EPI, [Wage and Hour investigators](https://www.epi.org/chart/h-1b-weighted-lottery-comment-2025-figure-b-number-of-federal-wage-and-hour-investigators-is-near-its-historic-low-number-of-wage-and-hour-division-investigators-u-s-department-of-labor-1973-2025/);
  - [Business Insurance on OSHA](https://www.businessinsurance.com/osha-inspector-ranks-fell-sharply-before-projected-2026-increase-agency-says/);
  - Bloomberg Law, [NLRB regions](https://news.bloomberglaw.com/daily-labor-report/labor-board-regions-struggle-with-understaffing-as-cases-pile-up).
- **Competition:** FTC, [FY2026 justification](https://www.ftc.gov/system/files/ftc_gov/pdf/fy-2026-cbj.pdf).
- **Integrity, FEC, EAC and OPM:** CRS, [FSGG FY2026](https://www.everycrsreport.com/files/2026-07-02_R49017_f837cbdd18cbeb92d7a2744997feae70aca0e902.html).
- **Civil rights:** Bloomberg Government, [DOJ Civil Rights Division](https://news.bgov.com/daily-labor-report/over-two-thirds-of-lawyers-leave-doj-civil-rights-unit-in-exodus).
- **CAISI:** IFP, [funding for CAISI](https://ifp.org/funding-for-caisi/).
- **FTA:** the Moving America draft, sec. (14) and its 2027-28 record list.
