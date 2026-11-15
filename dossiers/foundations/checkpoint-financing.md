# Stage E checkpoint memo: the plan-wide gap, and making the single health plan affordable

Role: the financing checkpoint at the end of stage E (`charter/PLAN.md`, section 6, stage G's row; board, "Next, in order", item 2). It reports the plan-wide gap, what drives it, which inputs are still moving and the revenue options the legacy work holds; it works out, whole-system, how the single health plan (HLT-1 to HLT-8) becomes affordable public financing (Espen, November 14); and it lists what is left for stage G. Status: **for Espen's decision, November 14, 2026**, on `origin/main` `8295bbc`, with clean power booked (#359, #372, #377). It recommends and books nothing: memos F1 to F3 (`memos/`) and the yes-or-no points in part B4 are Espen's to decide, and any booking that follows is a tier-3 change to adopted inputs. Federal fiscal years, nominal $ billion unless marked $T, a positive gap a shortfall, case `mixed`. Every figure is project arithmetic on the project's exploratory models, not an official score; the health-financing figures come from one run of `models/tools/health_financing.py` (test: `models/tools/test_health_financing.py`).

## In plain terms

> **Superseded (items 2 to 8, the health items), November 15, 2026:** replaced by [`health-financing.md`](health-financing.md), the fresh start on the single health plan's pricing and financing. Kept for the record; don't rely on its health figures.


1. **The gap.** In FY2040, the first year the fiscal rule tests, the plan's general fund is about **$4.16 trillion short (7.69% of GDP)**.
2. **Health is nearly all of it.** The single health plan's booked net cost is **$4.09 trillion** in FY2040. Everything else in the plan, after the revenue already booked, is about **$0.07 trillion** short.
3. **Health is cheaper for the country.** National health spending falls about **$0.49 trillion (6%)** in 2032 on the coverage model, about $0.75 trillion in FY2040, while covering about 34 million more people.
4. **The government's bill is money that already exists.** In FY2040 households stop paying about **$2.37 trillion** in premiums and out-of-pocket costs, employers about **$2.37 trillion** in premiums, and states about **$0.34 trillion**. The plan's new federal spending, about **$5.06 trillion**, is close to their total. It comes out close because two other terms roughly cancel: the national saving lowers the federal bill, while some of today's spending on these people is paid by sources the model names no payer for (part B1).
5. **So affordable means moving that money, fairly.** The plan is affordable for the government if the money households, employers and states stop paying comes in as public contributions; the national saving covers the rest. It must be done so that households below the top come out ahead, which is the project's fairness test (D3).
6. **The recommended way** (memos F1 to F3):
   - employers keep paying 65% of their former premiums during the move, then the same amount as a payroll contribution of about 7.7% from 2036;
   - states pay 80% of their former Medicaid spending for the people who move, instead of the working 50%;
   - households pay an income-based health contribution of about 15.7% of income above $20,000 single or $40,000 joint, collected with the income tax, in place of premiums and deductibles.
7. **What households get.** In FY2040 the average household in the bottom four fifths comes out ahead: about **+$6,700** (poorest fifth), **+$10,700**, **+$11,100** and **+$4,900** (fourth fifth) a year. The top fifth pays about $39,600 more, and the top 1% about $278,000 more.
8. **The main risks.**
   - The rate looks large: it replaces premiums, but it is a visible tax.
   - Employers have to pass their premium savings into pay.
   - The rate creeps up about a quarter of a point a year if health spending keeps growing faster than incomes.
   - The revenue-mix half of the fairness test fails unless health's contributions are counted as replacing premiums.
9. **After health**, about $70 billion a year is left in FY2040, plus about $1.9 trillion over FY2030-39. A small menu covers it (part C).

## Part A. The plan-wide gap

### A1. The gap today

The fiscal rule (`D4`) asks that permanent programs be paid for on the general fund in FY2040 and every later year, and that total debt and net interest stay below the baseline path. Only time-limited capital may be borrowed, inside an investment envelope (D4-B; `legacy/governing/decision-brief-02-trims-scope-and-fiscal-rule.md`). How it is read is decided:
- CBO's current-law baseline with disclosed changes (`DEC-2026-11-08-03`);
- midpoints with a cautious reading beside them (`-04`);
- one FY2030-39 window plus each bill's own CBO window (`-05`);
- CBO's interest rates with a +1-point stress (`-06`);
- the unified budget for the debt guardrails, with the general fund beside it (`-07`);
- the counting inputs (`DEC-2026-11-12-08`, `-10`, `-11`).

Dossiers report their cost, and balancing happens here (`DEC-2026-11-10-05`).

| Measure (case `mixed`) | FY2030 | FY2035 | FY2039 | **FY2040** | FY2030-39 total |
| --- | --- | --- | --- | --- | --- |
| General-fund primary balance, short ($B) | 68 | 3,009 | 4,124 | **4,164** | **$23.40T** |
| Share of GDP | 0.18% | 6.68% | 7.90% | **7.69%** | — |

Source: `models/data/recovery-budget-paths.csv`, column `agenda_gf_primary_bn`. Primary means before interest. The unified reading, which also counts the dedicated funds' own balances (Social Security, Medicare HI, education, paid leave), is $3,245 billion short in FY2040 (`program_primary_bn`). Since the first draft (#325, $4,240 billion), FY2040 is about $76 billion lower, mostly from clean power's booking.

### A2. What drives it

FY2040 and FY2030-39 by flagship, from `legacy/sources/recovery-budget-audit.csv` (case `mixed`, `primary_deficit_change_bn`); a cost is positive, revenue negative.

| Driver | Rows | FY2040 ($B) | FY2030-39 ($T) |
| --- | --- | --- | --- |
| Health, the single plan (flagship 2, part A) | HLT-1 to HLT-8 (HLT-7 is $5,040B; HLT-4's health parts $18.8B) | 5,060 | 26.35 |
| Health's own revenue: the employer exclusion ends | HX | −966 | −4.84 |
| **Health, net** | | **4,094** | **21.51** |
| Care parts B-D: long-term care, child care and pre-K, the care wage floor | HLT-9 to HLT-11, FAM-2, HLT-4's care parts | 750 | 3.66 |
| Secure floor (flagship 1) | FAM-1, INC-1 to INC-5, LAB-10 | 303 | 2.63 |
| Clean power (flagship 4), booked | CLI-*, CX, CXA, CXP, C1T | 125 | 1.90 |
| Housing (flagship 3) | HOU-1, HOU-4D | 121 | 0.81 |
| Transportation | MOV-29 to MOV-31, MR6 | 54 | 0.72 |
| Immigration (flagship 6) | IMM-1, IMM-EV, IF1T | 23 | 0.15 |
| Everything else: education, agency capacity, work and AI, democracy, the recovery credit | EDU-*, CAP-*, LAB-5, LAB-8, LAB-9, AI-*, DEM-*, others | 352 | 3.07 |
| Revenue already booked: corporate, top-end, estate, enforcement | G1 to G11, H1b, GX, C3A, C18, C35, C38 to C43, the IRS allowance | −1,106 | −8.66 |
| Revenue already booked: new income contributions | 2 points above $20K/$40K from 2035 (phasing in to 2044); 4 points above $100K/$200K from 2033 | −484 | −1.91 |
| Fund-boundary items, net: the dedicated funds' own lines (Social Security −732, education −202, HI −66, paid leave +16 and others; −986 in all) with the general fund's grants to them added back (+919) | — | −67 | −0.48 |
| **General-fund gap** | | **4,164** | **23.40** |

**Health is 98% of the FY2040 gap.** The rest of the plan's costs (about $1.73 trillion in FY2040) are matched by the revenue already booked and the fund-boundary items (about $1.66 trillion): **after health, about $70 billion is left in FY2040 and about $1.89 trillion over FY2030-39.**

### A3. Inputs still moving

- **Clean power is booked** (#359, #372, #377: about $1.73 trillion over FY2030-39 and $82 billion in FY2040 for its own rows) and paused at L3; its parked items don't move FY2040 by more than a few billion dollars.
- **The secure floor's D is booked** (SNAP's earned-income deduction, #330); SS-8, the trust funds' stock investment, is booked at zero until its budget treatment is checked.
- **Health:**
  - the employer contribution is reported, not booked (HLT-7.18; this memo's F2);
  - the states' share is a working 50% (HLT-7.17; F3);
  - the payment rate dominates the cost: each 0.1 of the 1.15 target moves FY2040 by about $0.7 trillion (care `6-cost.md`, part 6). It is decided (memo 5 B) and not reopened here.
- **The household model** (M3) carries health's household rows only as scenario Q-H7, before financing; this memo adds the financing rows outside the model's scenarios (part B3). Moving them into `scenarios.json` is a tier-3 change, once Espen decides.
- **Known later items:** a new CBO baseline (each one re-runs the settlement, plan section 6); E-Verify's Social Security funds line (about −$42 billion over FY2030-39, from #328); the items dossiers sent the settlement (part C).

### A4. The revenue options the legacy work holds

**Already counted, so not available again.** The legacy reconciliation traces $8.005T over FY2030-39 and $989B in FY2040 of general-fund reforms already in the `mixed` case (`legacy/sources/revenue-counted-reconciliation.md`), among them:
- G1, the corporate rate to 28% ($1.65T);
- G9, reversing the 2025 cuts above $450K ($1.45T);
- C38, the sprint package REV-TS1 to TS11 ($0.89T);
- G6, gains at death ($0.70T);
- G7, G10, G11, G5, G8, G3, H1b, C18, C35, C39 to C41 and C43, less the GX and CX offsets.

On top of these come the new income contributions ($1.91T) and HX ($4.84T).

**Not yet counted** (FY2030-39 midpoints in $T from the legacy menu, scaled from CBO and Treasury; `legacy/domains/domain-revenue.md`, "Closing the general-fund gap"; `legacy/sources/revenue-channels-and-full-menu.md`), with this memo's FY2040 yield per point beside them (part B2):

| Family | Option (legacy ID) | FY2030-39, $T | FY2040, $B | Who pays; main risk |
| --- | --- | --- | --- | --- |
| Health's own financing | Employer transitional contribution at about 65% (HLT-7.18) | 5.31 | about 1,060 net | Employers, in place of premiums |
| | States' share above the working 50% (HLT-7.17) | — | about 69 per 10 points | States; enforceability (*NFIB v. Sebelius*) |
| Payroll | New general-fund payroll contribution, no cap (W1) | 1.6 per point | about 200 per point, gross | All workers |
| Broad income | Contribution above $20K/$40K | 1.8 per point | about 180 per point | Most households |
| | Surtax above $100K/$200K (C20) | 0.67 per point | about 67 per point | Upper-middle; overlaps the 4 booked points on the same base |
| Consumption | 5% value-added tax, narrow or broad base, before any rebate | 2.8 / 4.2 | about 105 per point, broad | Regressive without a rebate; a new collection system |
| Top end and capital | Top four brackets +1 more point; pass-through and deferred-pay reform (REV-SC2); stock-option deduction (REV-HP2) | 0.36 per point; 0.35; 0.02 | — | High earners; overlaps G3, G9, H1a and SS-5 |
| Carbon and excise | Steeper carbon path (REV-C1F); road-fuel convergence (REV-C1D); alcohol and tobacco | — ; small; 0.13 and 0.06 | — | Shrinking bases; the carbon fee is dedicated to the dividend |
| Spending offsets | Inside the plan: administration and drug prices (part B2) | — | up to about 256 | Providers; not booked |
| Borrowing within the rule | Time-limited capital inside the investment envelope (precedent C21) | Doesn't help FY2040 | — | Capital only |

**Not available:** keeping current tariffs (already in the baseline), the HI reserve, C19b's cap on the exclusion once HX ends it (care `6-cost.md`, part 8), and counted rows used a second time.

**A staleness check.** CBO's latest options volume is still *Options for Reducing the Deficit: 2025 to 2034* (December 2024), which predates P.L. 119-21. Options that interact with the 2025 law's rates and deductions need rescoring against the 2029 baseline before they are booked. The model's static diagnostic, about 32 points of a broad income tier to stop debt rising after 2045 (`models/data/recovery-budget.json`, `required_broad_rate_points`), is a proxy, not a proposal.

## Part B. Making the single health plan affordable (superseded)

> **Superseded (all of part B), November 15, 2026:** replaced by [`health-financing.md`](health-financing.md), the fresh start on the single health plan's pricing and financing. Kept for the record; don't rely on its health figures.


Espen, November 14: "in the financing memo I want particular attention paid to a holistic look at making Medicare for all affordable. In theory, it should come out cheaper for the country, but that also means it needs to be affordable for the government." The plan's design is decided (memos 1 to 5, `DEC-2026-11-10-09` to `-13`; `DEC-2026-11-12-19`; `DEC-2026-11-13-02`) and is not reopened here; this part chooses how it is paid for.

### B1. National health spending now and under the plan, and who pays

**The country spends less.** On the coverage model's full-scale year (2032, decided variant: rates about 1.15 times Medicare, low copays, Medicaid's long-term care kept in Medicaid, administration at 5%; care `6-cost.md`, part 1):

| | Current law, 2032 | The plan, 2032 | Change |
| --- | --- | --- | --- |
| National health spending ($B) | 8,276 | 7,785 | **−491 (−5.9%)** |
| Uninsured (millions) | 37.2 | 3.6 | −33.6 |
| FY2040 equivalent (on the booking's path) | | | about −752 |

Where the change comes from, by group (2032, $B):
- **Lower prices and administration:**
  - employer groups −1,171: commercial prices about 2.1 times Medicare fall to 1.15, and administration falls from 12% to 5%;
  - the individual market −150.
- **Spent on covering everyone:**
  - care for the newly covered +445;
  - Medicaid's low rates (0.72 of Medicare) rise to the plan's +465;
  - today's Medicare enrollees +10.

So the savings on private coverage pay for covering everyone and paying Medicaid's doctors and hospitals the same as everyone else's, with about half a trillion dollars to spare. This is the "cheaper for the country" claim, and on the project's model it holds. CBO's five illustrative single-payer options changed national spending in 2030 by between −$0.7 trillion and +$0.3 trillion, mostly on their payment rates (CBO, 2020) [EV-CAR-218]; the plan's −$0.49 trillion in 2032 sits inside that range.

**Who pays today.** Across all national health spending in 2024, the federal government sponsored 31%, households 28%, private businesses 18%, state and local governments 16% and other private sources 6% (CMS, 2025) [EV-CAR-717].

**Who stops paying, and who pays instead, under the plan.** These are the people and the care that move into the plan, FY2040 on the booked path (`health_financing.py`, `flows`):

| | Today | Under the plan, before new financing |
| --- | --- | --- |
| **Households** | Premiums (workers' shares, individual policies, Medicare's Parts B and D and Medigap) and out-of-pocket costs | They stop paying about **$2,372B**; they keep only the plan's small copays above 200% of poverty |
| **Employers** | Premiums for their workers' coverage | They stop paying about **$2,372B** (about 11.9% of all pay) |
| **States** | Their share of Medicaid for the people who move (about $449B in 2032) | They pay half of it (HLT-7.17), so they stop paying about **$344B**; long-term care stays with them (HLT-7.07) |
| **Federal government** | Medicare, Medicaid, the premium credits, and the tax break for employer coverage | New spending of about **$5,060B** (HLT-1 to HLT-8, net of the federal money the plan replaces and the states' payment), less about **$966B** of income and payroll tax on former premiums that become pay (HX): **$4,094B net** |

The federal government's new spending (about $5.06 trillion) is close to what households, employers and states stop paying (about $5.09 trillion). That closeness comes from two terms that roughly cancel. Written out on the coverage model's 2032 full-scale figures ($B, decided variant; `health_financing.py`; the two terms are found group by group from `health_path.groups`):

| | 2032 ($B) |
| --- | --- |
| Employers stop paying | 1,547 |
| Households stop paying (net of the copays they keep paying) | 1,547 |
| States stop paying (half their former Medicaid spending for the people who move) | 224 |
| **Other spending on these people today, with no named payer** (below) | **565** |
| Less the national saving (lower prices and administration, net of covering everyone) | −491 |
| **= New federal spending, net of the federal money the plan replaces and the states' payment** | **3,392** |

**The missing term.** About $565 billion of today's spending on the people who move is in the model's spending figures but is not assigned to households, employers or states. By group it is:
- today's Medicare enrollees, $301B: CMS's Medicare spending is above CBO's net federal subsidy plus enrollees' premiums and out-of-pocket costs. The difference is Medicare's other receipts and the seam between CMS's and CBO's figures, which the model card says do not reconcile exactly;
- employer groups $170B, the individual market $37B and Medicaid $33B;
- care for the uninsured paid by others (hospitals' uncompensated care and other programs), $22B.

About $169B of the total is the copays households keep paying under the plan, which the table counts net. The rest, about $0.4 trillion, is a seam in the model's accounts, not a payer who can be asked to keep paying.

**What it means.**
- The national saving does lower the federal bill: without it the government would need about $0.49 trillion more in 2032.
- The saving and the missing term roughly offset each other, which is why the new federal spending comes out close to what households, employers and states stop paying.
- In FY2040 terms the two are about $0.75 trillion (saving) and $0.88 trillion (missing term).
- The financing below is sized to the booked federal cost ($4,094B net in FY2040), not to this identity, so the seam does not change any recommendation. It does bound how far "they stop paying X, so they can pay X" holds: to within about a tenth.

**What "affordable for the government" therefore means.** The plan needs no money the country doesn't already spend. It needs about $4.1 trillion a year (FY2040) now paid to insurers and providers to be paid as public contributions instead. The test of fairness is whether each household pays in less than it stops paying.

### B2. The financing options and what each raises

FY2040 yields, from the budget model's own parameters (`models/tools/recovery-budget/assumptions.json`) and the coverage model (`health_financing.py`, `per_point`, `sensitivities`):

| Option | FY2040 effect on the gap | Basis |
| --- | --- | --- |
| **Employer contribution at 65% of former premiums** (HLT-7.18, designed, reported, not booked) | **−1,060** net (−1,541 gross, less 482 of tax on pay that no longer rises) | Care `6-cost.md`, part 4: 65% is the share at which employer moves cost the federal budget nothing |
| The same yield as a **payroll contribution** on all pay | −1,060 at about **7.7%** of pay | A payroll point raises about $200B gross in FY2040 (the education fund's parameter, $135B in 2030 growing 4% a year) |
| Employer contribution at 100% of former premiums (on payroll, about 11.9%) | −1,631 | The same arithmetic |
| **States' share** from 50% to 80% (or 100%) | −207 (−345) | About $69B per 10 points in FY2040 ($45B in 2032; care `6-cost.md`, part 4) |
| **Income-based health contribution** above $20,000/$40,000 | about −180 per point | The budget model's broad tier: $180.4B per point in 2034 at GDP scale, less a 20% allowance for avoidance |
| **Worker payroll contribution** on all earnings | about −200 per point | As above; no income-tax offset on the worker's side |
| **Value-added tax**, broad base | about −105 per point, before any rebate | Legacy menu: 5% broad, $4.2T over FY2030-39 |
| **Savings: administration** 5% → 3% of spending | −187 (8%: +296) | Traditional Medicare's own administration was 1.4% of its spending in 2017 (CBO testimony) [EV-CAR-217]; 5% is the plan's working figure |
| **Savings: drug prices** 15% → 23% below today's | −69 (5%: +86) | CBO's lower-rate scenario: drug prices 23% lower (CBO, 2019) [EV-CAR-220] |
| **Other health tax breaks** (the medical-expense deduction, health savings and flexible spending accounts, the self-employed deduction) | Small; not estimated | Mostly lose their base when premiums and out-of-pocket costs end; HX already counts the employer exclusion, the large one |

The savings levers are real but small next to the need, and the evidence supports them only as upside: the plan's administrative budget and drug prices are set in its specification and in practice. They are not booked (yes-or-no point 1).

### B3. What each choice does to households

**Method.** FY2040, health only, per household by D3 quintile. Households are ranked by size-adjusted income, with equal numbers in each fifth. The keys are the household model's measured ones on the 2029 CPS households (`models/tools/household/keys.csv`): premiums and out-of-pocket costs on `health_hh`, employer premiums that become pay on `employer_cov`, HX on `exclusion_end`, a payroll contribution on `wages`, the income contribution on AGI above the line (a new key computed in the script), the VAT on `consumption` and its rebate on `persons`. There are about 151 million households in FY2040 (the model's count grown with CBO's households). Average incomes in FY2040 are about $34K, $92K, $156K, $246K and $562K by fifth, and $1.88M for the top 1%.

The method has limits:
- it shows averages, not the spread inside a fifth;
- it counts cash only, not the value of coverage to people now uninsured;
- it assumes full pass-through of premium savings into pay (HX's convention);
- the CPS top-codes high incomes, so the top 1%'s share of the income contribution (12% here) is understated, which overstates what the top fifth's lower part and the fourth fifth pay.

**The recommended package** (F1 A, F2 A, F3 B), net dollars per household a year, FY2040:

| | Q1 | Q2 | Q3 | Q4 | Q5 | Top 1% |
| --- | --- | --- | --- | --- | --- | --- |
| Premiums and out-of-pocket costs they stop paying | +4,629 | +9,493 | +16,161 | +22,280 | +25,889 | +21,967 |
| Employer premiums that become pay, less the tax on it (HX) | +3,024 | +6,890 | +9,784 | +11,666 | +12,589 | +7,305 |
| The employer contribution: pay that doesn't rise, net of tax | −628 | −2,426 | −4,863 | −8,307 | −18,831 | −84,132 |
| Health contribution on income (about 15.7%) | −312 | −3,255 | −10,005 | −20,718 | −59,197 | −223,194 |
| **Net** | **+6,712** | **+10,703** | **+11,077** | **+4,921** | **−39,551** | **−278,055** |
| Net as a share of income | +20.0% | +11.7% | +7.1% | +2.0% | −7.0% | −14.8% |

The middle fifth pays about 6.4% of its income in the health contribution and stops paying about 10.4% of it in premiums and out-of-pocket costs.

**Beside the rest of the plan.** Without health, the decided package (scenario Q) gives Q1 to Q4 +$11,461, +$7,253, +$4,848 and +$552 in 2039 (`models/tools/household/results.md`, section 8). With health financed as recommended, every fifth below the top comes out ahead, the fourth by about $5,500 a year.

**The other choices, net per household, FY2040** (each with the other two memos at their recommendations):

| Choice | FY2040 rate | Q1 | Q2 | Q3 | Q4 | Q5 | Top 1% |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **F1 A: income contribution (recommended)** | 15.7% above $20K/$40K | +6,712 | +10,703 | +11,077 | +4,921 | −39,551 | −278,055 |
| F1 B: worker payroll contribution | 14.1% of all earnings | +5,349 | +7,489 | +8,114 | +3,484 | −30,575 | −279,231 |
| F1 C: half income, half VAT with a per-person rebate | 7.8% income; VAT 13.5% | +3,631 | +6,471 | +7,419 | +3,706 | −27,366 | −210,703 |
| F2 B: employer contribution kept on former premiums, never converted | 7.7% of pay equivalent | +5,316 | +8,047 | +8,127 | +3,583 | −31,211 | −201,914 |
| F2 C: employers pay all of their former premiums (payroll) | 11.9% payroll; 12.5% income | +6,437 | +10,054 | +10,479 | +4,631 | −37,739 | −278,292 |
| F2 D: no employer contribution | 21.6% income | +7,223 | +11,908 | +12,188 | +5,459 | −42,917 | −277,614 |
| F3 A: states at 50% (as booked) | 16.8% income | +6,689 | +10,465 | +10,345 | +3,404 | −43,885 | −294,397 |
| F3 C: states at 100% | 14.9% income | +6,727 | +10,862 | +11,566 | +5,932 | −36,661 | −267,160 |
| F3 D: states pay nothing (also the fallback if the payment fails in court) | 18.8% income | +6,651 | +10,068 | +9,124 | +875 | −51,109 | −321,633 |

Every option passes D3's household test on average, because premiums are a heavy, flat charge today. The income-based contribution leaves every fifth below the top better off than either the payroll or the VAT version.

**Two checks.**
- **If employers pass only half of their savings into pay** (Anand, 2017) [EV-CAR-299], the fourth fifth's gain falls to about +$1,300 and the middle's to about +$7,500, before the contribution rises to make up the lost tax (project arithmetic, approximate). The federal side loses about $130 billion of HX in FY2040 (care `6-cost.md`, part 6). The employer contribution is the guard against that: it collects the premium savings directly where pay may not rise.
- **The revenue-mix test** (D3's second half: more than half of new general-fund revenue from the top 1% and corporations) is 51% on scenario Q-H7 before financing. With health's contributions counted as new revenue it falls to roughly a quarter (rough arithmetic). They replace premiums rather than add a burden, so this memo proposes counting them outside that test (yes-or-no point 2).

### B4. The recommendation, and what Espen decides

**Recommended: premiums become contributions.**
1. **Employers** pay the designed transitional contribution, 65% of former premiums, from each group's move. From 2036 it becomes a payroll contribution of the same yield, about 7.7% of pay, on all employers (memo F2, A).
2. **States** pay 80% of their former Medicaid spending for the people who move, by the clawback-style obligation already designed (memo F3, B).
3. **Households** pay an income-based health contribution above $20,000/$40,000, collected with the income tax. It phases in with the waves (2031 for wave 1, then thirds in 2033-35) and reaches about 15.7% in FY2040 (memo F1, A).

Together they close health's FY2040 cost ($1,060B + $207B + $2,827B = $4,094B). On the same path they would cover its FY2030-39 cost of about $21.5 trillion, about $5.3 trillion of it from employers (care `6-cost.md`, part 4).

**Yes-or-no points** (none adopted by silence):
1. Book no savings lever now. Administration and drug prices stay at the plan's working figures. The upside (up to about $256 billion in FY2040) is reported and revisited when the specification sets the administrative budget and drug negotiation.
2. Count health's contributions outside D3's revenue-mix test, as replacements for premiums, and judge them by the household net test instead.
3. Phase the household contribution in with the waves (wave 1 in 2031, then thirds in 2033-35), not at full rate from the start.
4. Pay all of health's contributions into the plan's fund (HLT-7.22), with the general fund covering any shortfall, so the contribution's purpose stays visible. The budget model keeps booking on the general fund.

**What would change the recommendation:**
- if Espen wants no new tax called a health contribution, F1 B (payroll) is the next best for the bottom four fifths;
- if the states' payment fails in court (F3 D), the household rate rises about 3 points;
- if the specification holds the plan's growth to income growth, the rate stops creeping (below).

**Risks to say plainly.**
- **The rate is large.** 15.7% on most income, on top of the 2 broad and 4 high points already booked, is the largest tax change in the plan, even though it replaces more than it takes from most households. Vermont's single-payer plan stopped when its full tax became visible (VTDigger, 2014; State of Vermont, 2014) [EV-CAR-245] [EV-CAR-244]. The public case has to show the family's premiums ending alongside the rate.
- **Top rates.** With the booked measures, the top federal rate on wages would pass 60%. The budget model's 20% avoidance allowance may be too small at that scale. Stage G should test a lower rate on the first tier with more at the top.
- **Growth.** The plan's cost grows on CBO's health path, about 5.7% a year after 2036 (care `6-cost.md`), and incomes about 3.8%. At that pace the needed rate rises about a quarter of a point a year unless the plan's national budget holds growth near income growth. This is the long-run affordability question, for the specification.
- **Within-fifth losers.** A household with high income, no premiums today (for example coverage through a spouse's generous employer plan that paid everything) and few medical costs can pay more than it saves. The household model's within-quintile spread is its next addition (`results.md`, section 8).

### B5. Benchmarks

- **Vermont's 2014 single-payer plan** needed an 11.5% employer payroll tax plus an income-based public premium rising to 9.5% of income, capped at $27,500 (State of Vermont, 2014) [EV-CAR-244]. This memo's 7.7% and 15.7% are of the same order, with the employer's share lower and the household's higher, and no cap.
- **Sanders's options paper** proposed a 7.5% employer payroll premium and a 4% household income premium, with about $4.6 trillion of other taxes and $4.2 trillion from ending health tax breaks beside them [EV-CAR-713]. This memo's employer side (about 7.7%) is close. Its household side is larger because it replaces the other taxes: the top-end measures the paper used are already booked here for the rest of the plan. The paper's figures are the sponsor's own and qualified, not confirmed, by CRFB and TPC [EV-CAR-714] [EV-CAR-715] [EV-CAR-716]; part E compares them in full.
- **CBO's single-payer options** put federal subsidies $1.5 to $3.0 trillion higher in 2030 [EV-CAR-218]. The plan's $2.71 trillion (2032, model basis) sits in the upper half (care `6-cost.md`, part 1), so the contribution is sized to a cautious cost.

## Part C. The rest of the gap after health

> **Superseded (the "What remains" arithmetic where it rests on part B's package; the list of items for stage G and the menu stay), November 15, 2026:** replaced by [`health-financing.md`](health-financing.md), the fresh start on the single health plan's pricing and financing. Kept for the record; don't rely on its health figures.


**What remains.** With health financed as recommended, the FY2040 gap is about **$70 billion** (0.13% of GDP). Over FY2030-39 it is about **$1.89 trillion**, spread across the decade at roughly $0.1 to $0.27 trillion a year (project arithmetic: the gap less health's booked rows, year by year), and it falls to the FY2040 figure as the booked income contributions phase in. The decade figure matters for the debt guardrail, not the FY2040 test.

**Items dossiers sent the settlement** (each to price at stage G):
- housing's FY2040 and FY2041 maturity gaps (`DEC-2026-11-09-09`, `DEC-2026-11-10-04`) and HOU-2D's revenue row;
- the education fund going negative in 2035 at the 1.4-point rate (about 1.7 points keeps it solvent);
- R1's child benefit, about $2.3T in the ten years after its window (the Byrd rule);
- transportation's fuel-tax path (`DEC-2026-11-10-14`);
- SS-8's budget treatment and E-Verify's funds line;
- the rebuild of the financing screens in `models/tools/financing-protection/`;
- the +1-point interest stress (`DEC-2026-11-08-06`).

**The menu for it, briefly:**
1. One more point above $100,000/$200,000 (about $67 billion in FY2040) closes FY2040 on its own. It overlaps the 4 booked points on the same base.
2. Top-end and capital options not yet used (REV-SC2, REV-HP2, a fifth bracket point), well under $1 trillion over the decade in all.
3. Sequencing: starting the household contribution with wave 1 (2031) and moving later costs to match revenue, for the decade's debt path.
4. The administration and drug savings in part B2, if the specification bears them out.

## Part D. Questions for Espen

> **Superseded (questions 1 to 4, memos F1 to F3 and part B4's points; the new questions are in its part 9), November 15, 2026:** replaced by [`health-financing.md`](health-financing.md), the fresh start on the single health plan's pricing and financing. Kept for the record; don't rely on its health figures.


**Now (this memo's batch):**
1. Memo F1, the household side: A (income contribution, recommended), B (worker payroll) or C (income plus VAT)?
2. Memo F2, the employer side: A (65%, then a payroll contribution from 2036, recommended), B (premium-based, never converted), C (100% of former premiums) or D (none)?
3. Memo F3, the states' share: A (50%), B (80%, recommended), C (100%) or D (none)?
4. Part B4's four yes-or-no points.

**At stage G, the full settlement after stage F, which re-audits what this checkpoint settles (Espen, November 14; no answer needed now):**
1. The rate structure of the health contribution: one rate, or a lower first tier with more at the top.
2. How strictly to phase revenue to the FY2040 test and the decade's debt path (part C).
3. The states' shares across health, long-term care, child care and pre-K, together (`DEC-2026-11-11-05`).
4. Whether to weigh Medicare "Part E" (employers offer plans meeting Medicare's standards or pay in, indefinitely; board, "Directions for later stages"). It would reopen the 2035 endpoint (memo 1), so it is outside this memo; F2 B is its financing half.

## Part E. How the Medicare for All bills propose to pay, beside this plan

> **Note, November 15, 2026:** [`health-financing.md`](health-financing.md), part 7, extends this comparison and corrects three points (S. 1506's state obligations, the per-employee transition floor, and the Medicare trust fund transfer).

A comparison only. It changes no decision and no booked figure, and recommends nothing. Sources: Sen. Sanders's S. 1506 (SRC-3260) and his options paper (SRC-3041), Rep. Jayapal's H.R. 3069 (SRC-3261), and the care dossier's comparison (`dossiers/care/research-s1506-comparison.md`, row "Trust fund and financing") with its cost section (`dossiers/care/6-cost.md`, part 4).

**What was found.**
- **Both bills levy no tax.** Sec. 701(b)(1) of each credits the trust fund with 100 percent of the net revenue increase "attributable to" secs. 801 and 902 (the end of duplicative employer plans, and of the Exchanges) [EV-CAR-287, EV-CAR-292]. The bills set no rate and no base. A search of H.R. 3069's text found no tax rate, employer contribution or state payment.
- **Sanders's options paper is a menu, not a plan.** It is the sponsor's own, undated, and written before S. 1506: it cites 2016 premiums and 2014 tax data. Sanders's site holds no 2025 version (searched November 13, 2026). Its main options [EV-CAR-713]:

| Option in the paper | Rate | Base and exemption | Revenue the paper claims, ten years |
| --- | --- | --- | --- |
| Employer income-based premium | 7.5% | Payroll; an employer's first $2 million exempt | $3.9T |
| Household income-based premium | 4% | Income after the standard deduction; a family of four under $29,000 pays none | $3.5T |
| End health tax expenditures | — | The employer-premium exclusion, cafeteria-plan exclusion, medical-expense deduction | $4.2T |
| More progressive income tax | 40% to 52% | Income above $250,000, capital gains taxed as work income, itemized deductions capped at 28% | $1.8T |
| Wealth tax | 1% | Net worth above $21 million, top 0.1% of households | $1.3T |
| Estate tax | 45% to 55% | Estates above $3.5M single or $7M couple, plus a 10% surtax above $500M | $0.25T |
| Offshore profits, bank fee, business-owner loophole, LIFO repeal | one-time tax; 0.07%; —; — | Corporate and financial | $0.77T, $0.12T, $0.25T, $0.11T |

All of these sum to about $16.2 trillion (project arithmetic). The paper states no cost for the program, so it cannot say whether that covers it.
- **Jayapal has published no separate financing plan that I could find.** In February 2019 she said she would release a list of suggested funding mechanisms for her earlier bill [SRC-3079]. Nothing like it turned up for H.R. 3069. An absence is hard to prove.

**How far to trust the paper's figures (grading).** They are the sponsor's own estimates, grade C analysis [EV-CAR-714]. Two independent scorers looked at a later, February 2020 version of the options, so they qualify the figures rather than confirm them [EV-CAR-715, EV-CAR-716]:
- CRFB concurred with the campaign's $12.2 trillion for three direct offsets, and with its $5.2 trillion for the employer tax on the campaign's method. CRFB's own earlier estimate of that tax was $4 trillion, and it puts the difference down to how interactions are distributed.
- The Tax Policy Center put the earmarked provisions at $13.4 trillion for 2021 to 2030. The paper's five main items add to about $13.65 trillion, so the totals are close, but the versions, windows and sets differ.
- The household premium, employer premium and exclusion figures in the later version ($4.0T, $5.2T, $3.0T) differ from the paper's ($3.5T, $3.9T, $4.2T). Rely on the paper for what it proposes, not for what it raises. All of this is before the 2025 law changed the tax base.

**Side by side.**

| | Sanders (bill plus options paper) | Jayapal (House bill) | This plan |
| --- | --- | --- | --- |
| What the bill text funds | A trust fund fed by last year's federal Medicare, Medicaid, FEHB and similar money, the Medicare trust fund balances and the revenue from ending employer plans and Exchange credits [EV-CAR-287] | The same, plus TRICARE's purchased care [EV-CAR-292] | The same federal streams pooled (memo 3 B), plus the employer-exclusion revenue named as a stream (research note, part c) |
| New taxes proposed, and where | None in the bill. The paper offers the menu above | None in the bill; no separate plan found | Recommended here (part B4): an income-based health contribution, about 15.7% above $20K/$40K in FY2040; Espen decides (memo F1) |
| What employers pay | Nothing in the bill. The paper: 7.5% of payroll above $2 million, and in the four-year transition the higher of that or 75% of today's premiums | Nothing in the text | A transitional contribution of about 65% of former premiums, then the same yield as a payroll contribution, about 7.7% (memo F2); about $1,060B net in FY2040 |
| What states pay | Nothing, except a floor for nursing-home spending (fiscal 2024 level) [EV-CAR-278] | Nothing; long-term care moves into the program [EV-CAR-291] | A fixed share of their former Medicaid spending outside long-term care: 50% working, 80% recommended (memo F3) |
| The gap left open | All of the program's new money, and the paper does not price the program | The same, with no menu | None for health if memos F1 to F3 are adopted as recommended; about $70B for the rest of the plan in FY2040 (part C) |

**An illustration for two families of four, one earner with employer coverage, on the paper's terms. This is an illustration, not a model result.** It compares what the paper's household premium would cost with the worker premiums the family stops paying. Premiums are KFF's 2026 averages: $28,303 for family coverage, of which workers pay $7,471 [EV-CAR-111, EV-CAR-112], so employers pay about $20,832. Incomes are the household model's 2029 averages by quintile (`models/tools/household/results.md`, section 3).

| Family of four, one earner | Pays the 4% premium | Stops paying (worker share) | Difference for the family | Employer's side: 7.5% of pay against the premium it stops paying |
| --- | --- | --- | --- | --- |
| Fourth quintile, $173,693 | 4% of ($173,693 − $29,000) = about $5,800 | about $7,500 | about $1,700 better off | about $13,000 against $20,800 |
| Middle quintile, $110,181 | 4% of ($110,181 − $29,000) = about $3,200 | about $7,500 | about $4,200 better off | about $8,300 against $20,800 |

What it leaves out:
- it assumes the earner's pay is the whole income, an average employer plan and a large employer (so the $2 million payroll exemption doesn't bite);
- it uses the paper's $29,000 deduction, which CRFB equates to the pre-2018 standard deduction and exemptions, not today's;
- it leaves out out-of-pocket costs saved, the other options and the tax that ending the exclusion adds on former premiums that become pay.

Who bears the employer's share is contested; studies find workers bear part of it through pay [EV-CAR-296, EV-CAR-299]. Part B3 does the same comparison for this plan on the household model, for every fifth.
