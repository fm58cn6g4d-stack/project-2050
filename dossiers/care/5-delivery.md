# Care you can count on, part A (health): delivery

Role: section 5 of the care dossier, health part. It says who runs each provision of section 4, what capacity it needs, the timeline from enactment to the endpoint, how people get remedies, and what states do. Status: draft (stage D, step 4, PR 1), on `DEC-2026-11-10-09` and `DEC-2026-11-10-11`. Dates are the decided ones; where a step's date is a working choice, it says so.

## 1. Who runs what

| Job | Agency | Channel it uses | Provisions |
| --- | --- | --- | --- |
| Run the plan: enrollment, claims, payment, rules | HHS (CMS) | Medicare's claims contractors and payment systems, extended to every enrollee | HLT-7.01 to 7.14, 7.19 |
| Find and enroll people from records | CMS with SSA and the IRS | Social Security and tax records, state Medicaid files, marketplace files, and the coverage reports employers already file with the IRS | HLT-7.02, 7.03 |
| Collect the employer contribution | Treasury (IRS) | The quarterly payroll tax deposit; the base-year premium from the employer-paid cost of coverage already reported on W-2s | HLT-7.18 |
| Collect the states' payments | CMS | One yearly formula per state, netted against the federal Medicaid money it still receives for long-term care | HLT-7.17 |
| Worker help | Labor | American Job Centers, the channel trade adjustment uses (TAA for Workers had $633.6 million in FY2021: CRS, 2022) [EV-CAR-345] | HLT-7.16 |
| Hospital transition fund and global budgets | CMS | Medicare cost reports for each hospital's baseline revenue and payer mix | HLT-7.11, 7.15 |
| Rural front door | USDA Rural Development state offices | Community Facilities loans and grants; referral to HRSA, CMS and the Rural Health Transformation Program | HLT-8.01 |
| Complaints and appeals | The Beneficiary Ombudsman; Medicare's appeals system | — | HLT-7.20 |
| Equity, primary care, data firewall | HHS offices | — | HLT-7.21 |
| Federal systems | VA, Defense, the IHS (with tribal consultation), OPM for FEHB | Their own systems; the plan pays their facilities as providers | HLT-7.24, 7.26 |

**One agency, not a new one.** Memo 1 B builds the plan as an expansion of Medicare, so CMS runs it with Medicare's machinery. When Medicare began in 1966, about 19 million people enrolled, most already in Social Security's records (Social Security Administration) [EV-CAR-310]. The plan starts the same way: from records, with a card issued without a form (HLT-7.02).

## 2. Capacity

The legacy capacity work found CMS's capacity is the binding constraint for any health plan (`legacy/sources/health-cms-capacity-review-2026-10-21.md`). Recent launches show where the risk is:
- HealthCare.gov launched in 2013 without verification that it met its requirements (GAO, 2014) [EV-CAR-311], and recovered within two months (HHS Inspector General, 2016) [EV-CAR-312].
- The Medicaid unwinding struggled with the volume of renewals, systems and staffing (KFF, 2024) [EV-CAR-313].

What the plan needs:
- **Staff and systems funded before 2031.** The plan-wide agency rebuild (CAP-7S, funded on enactment in FY2029, and CAP-7's permanent increase; `models/data/inputs/ledger-bills.csv`) carries CMS's build. The plan's own administration, about 5% of its spending on the coverage model (working assumption, range 3-8%), pays for running it once it starts.
- **Enrollment from records, not applications**, so volume is a data-matching task, not a paperwork task.
- **Readiness reports** (HLT-7.03): HHS publishes, 18 months before each date, what is built, what is tested and what is behind. They are published counts with a review trigger, not gates: a date moves only if Congress votes to move it.

**The largest loads.** Wave 1 moves the uninsured, the individual market and every child at once. On the coverage model's 2032 inputs that is about 37 million uninsured under current law (fewer after restoration), 20 million in the individual market and about 37 million children with employer coverage [EV-CAR-051], plus children in Medicaid and CHIP. That is several times Medicare's 1966 launch. The endpoint then moves today's 71 million Medicare enrollees and the last third of Medicaid and employer groups [EV-CAR-051]. Medicare enrollees are already in CMS's own systems, which makes that load smaller than its size. Section 8 names wave 1's size as a risk and says what would slow it.

## 3. Timeline

| When | What happens | Who |
| --- | --- | --- |
| 2029, first months | 2029 reconciliation act: restoration, the Advantage fix, drug negotiation, USDA lending and grants (R1) | Congress |
| 2029 | The Medicare for All Act of 2029, regular order under the rules reform (D2) | Congress |
| 2029-30 | Rules: the plan's fee schedules and hospital conversion factor, copay schedule, provider agreements, the employer contribution's base year and collection; readiness report for wave 1 (July 2029) | CMS, IRS |
| Plan year 2030 | Restoration in force; enhanced credits for 2030; Advantage fix at half strength | CMS, IRS |
| January 1, 2031 | **Wave 1**: the uninsured, the individual market, every child; Medicare at 60; upgrades for today's Medicare enrollees (cap, hearing, vision); no disability wait; Medigap guaranteed issue; drug negotiation applies to the plan; hospital glide starts at about 1.25 times Medicare | CMS |
| July 2031 | Readiness report for wave 2 | HHS |
| 2032 | HHS publishes each hospital's projected revenue change under the plan from its cost report, and the transition fund's formula (if Espen approves HLT-7.15) | CMS |
| January 1, 2033 | Wave 2, first cohort: a third of Medicaid (by state) and of employer groups (smallest firms first); employer contribution starts for them; worker help opens; dental for Medicare enrollees | CMS, IRS, Labor |
| July 2033 | Readiness report for the endpoint | HHS |
| January 1, 2034 | Wave 2, second cohort | CMS, IRS |
| January 1, 2035 | **Endpoint**: the last cohort and everyone else, including today's Medicare and FEHB enrollees; Advantage, Medigap for covered services, COBRA and duplicative coverage end; the hospital insurance trust fund folds into the plan's fund | CMS |
| 2036 | Hospital rates reach about 1.15 times Medicare | CMS |
| Until the settlement's payroll contribution starts | Employer contribution continues | IRS |
| FY2038 | Worker help and the transition fund close | Labor, CMS |

**Cohorts inside wave 2 (working choice).** HHS assigns states to the three Medicaid cohorts and sets the employer cohorts by firm size so that each holds about a third of the group. Smaller firms go first, because they carry the highest deductibles (55% of covered workers at smaller firms had a single deductible of $2,000 or more in 2026, against 33% at larger ones: KFF, 2026) [EV-CAR-293]. A state may ask to move earlier.

**If the rules reform fails.** The plan's money (the waves' spending, the fund's streams and the employer contribution) can be carried by a later reconciliation act. The entitlement's rights, the provider rules, the offices and the endpoint would then wait for 60 votes. Restoration and the Advantage fix are in the 2029 reconciliation act either way. Section 8 names this as the main legislative risk.

## 4. Remedies

- **Coverage.** Anyone not enrolled is enrolled at the point of care (HLT-7.02); no one loses old coverage before the plan is active for them (HLT-7.04).
- **Complaints and appeals** go to the Ombudsman and through Medicare's appeals process (HLT-7.20).
- **Discrimination** can be enforced by a private suit (HLT-7.09).
- **Providers** appeal rates and global budgets through Medicare's provider appeals process.
- **Oversight**: the HHS Inspector General and GAO audit the plan and the fund. The readiness reports are published.

## 5. States' roles

| Period | What states do |
| --- | --- |
| 2029-30 | Run restored Medicaid (HLT-1.01 to 1.03) |
| 2031 | Their children move into the plan; Medicaid continues for adults until their cohort |
| Their cohort (2033, 2034 or 2035) | Medicaid's acute care moves to the plan; the state starts paying its fixed share (HLT-7.17) |
| From then | Long-term care stays in Medicaid until part B decides (HLT-7.07); insurance regulators oversee supplemental coverage and Medigap (HLT-2.02, 7.23) |

State public options and state-funded premium help fold into the plan when their enrollees move.

## 6. Rural delivery

- **Capital:** USDA Community Facilities direct loans of $3-5 billion a year for rural hospitals, clinics and nursing homes, and $200-500 million of grants (HLT-8.01), through the offices that housing's rebuild of Rural Development staffs (`DEC-2026-11-10-02`).
- **Operating:** global budgets for rural, critical-access and safety-net hospitals (HLT-7.11), and the transition fund if approved (HLT-7.15).
- **The navigator's remit** (point 6 left it to this section). Working choice: each Rural Development state office has a health facilities lead who helps rural providers apply for Community Facilities money, the Rural Health Transformation Program (whose $10 billion a year runs through FY2030: Public Law 119-21) [EV-CAR-015], HRSA's rural grants and the plan's global budgets. It does not run a program of its own.

## 7. What delivery leaves open

- *Regional offices* (S. 1506 title IV): CMS's regional structure is settled with its capacity plan in 2029-30, not now; no decision turns on it.
- *Exact cohort sizes and the order of states*: set by HHS with the readiness reports (study in implementation).
- *IHS funding alongside the plan* (HLT-7.24): open. The IHS had $8.12 billion enacted for FY2026, including the next year's advance appropriation (CRS, 2026) [EV-CAR-350], and advance appropriations have continued each year since the FY2023 act (CRS, 2026; Public Law 117-328) [EV-CAR-348] [EV-CAR-349]. Whether they continue once the plan pays IHS facilities for its enrollees is for part B or a later step, with tribal consultation.
