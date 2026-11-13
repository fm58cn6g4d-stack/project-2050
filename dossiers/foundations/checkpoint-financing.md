# Stage E checkpoint memo: plan-wide financing, first draft

Role: the short financing checkpoint at the end of stage E (`charter/PLAN.md`, section 6, stage G's row; board, "Next, in order", item 4). It reports the plan-wide gap, what drives it, which inputs are still moving, the revenue options the legacy work already holds, and the questions the financing settlement will put to Espen. Status: **first draft, November 13, 2026, with clean power pending** (not yet booked). It decides nothing and asks for no decision now. Figures are read from the budget model's generated files at `origin/main` `6e44502`, case `mixed`. Federal fiscal years, nominal $ billion unless marked $T, a positive gap a shortfall.

## In plain terms

- **The gap.** In FY2040, the first year the fiscal rule tests, the plan's general fund comes up about **$4.24 trillion short (7.83% of GDP)**. That is after counting the roughly $2.5 trillion a year of new revenue the model already books for that year.
- **Why.** Almost all of it is the single health plan. It replaces what employers and families now pay in premiums (about $1.55 trillion a year from each, at 2032 scale) with public spending. The gap is mostly that shift from private premiums to public financing, and the settlement's main job is to design how it is paid for.
- **What's already counted.** The corporate and top-end taxes the legacy work chose, a 2-point broad and 4-point high income contribution, and the end of the tax break for employer insurance are already booked. They can't be counted a second time.
- **What's left on the menu.** The employer contribution health already designed (about $1.06 trillion in FY2040, reported but not yet booked), broad payroll or income contributions, a value-added tax, more top-end measures (small next to the gap), state shares, and spending offsets.
- **What you'll be asked in stage G.** Four questions, at the end of this memo. None needs an answer now.

## 1. The gap today

The fiscal rule (`D4`) asks that permanent programs be paid for on the general fund in FY2040 and every later year, and that total debt and net interest stay below the baseline path. Only time-limited capital may be borrowed, inside an investment envelope (D4-B; `legacy/governing/decision-brief-02-trims-scope-and-fiscal-rule.md`). How it is read is decided: CBO's current-law baseline with disclosed changes (`DEC-2026-11-08-03`), midpoints with a cautious reading beside them (`-04`), one FY2030-39 window plus each bill's own CBO window (`-05`), CBO's interest rates with a +1-point stress reported (`-06`), the unified budget for the debt guardrails with the general fund shown beside it (`-07`), and the counting inputs in `DEC-2026-11-12-08`, `-10` and `-11`. Dossiers report their cost; balancing happens here (`DEC-2026-11-10-05`).

| Measure (case `mixed`) | FY2030 | FY2035 | FY2039 | **FY2040** | FY2030-39 total |
| --- | --- | --- | --- | --- | --- |
| General-fund primary balance, short ($B) | 56 | 3,009 | 4,135 | **4,240** | **$23.4T** |
| Share of GDP | 0.15% | 6.69% | 7.92% | **7.83%** | — |

Source: `models/data/recovery-budget-paths.csv`, column `agenda_gf_primary_bn` (the decade total is the sum of its ten rows). Primary means before interest. For disclosure, the unified reading, which also counts the dedicated funds' own surpluses (Social Security, Medicare HI, education, paid leave), is $3,321 billion short in FY2040 (`program_primary_bn`). The gap passes $3 trillion when the health plan reaches full scale in 2035 and stays near 8% of GDP after that.

## 2. What drives it

FY2040 and FY2030-39, from `legacy/sources/recovery-budget-audit.csv` (case `mixed`, column `primary_deficit_change_bn`), summed by flagship. A cost is positive; revenue is negative.

| Driver | Rows | FY2040 ($B) | FY2030-39 ($T) |
| --- | --- | --- | --- |
| Health, the single plan (flagship 2, part A) | HLT-1 to HLT-8 (HLT-7 is $5,040B) | 5,062 | 26.58 |
| Health's own revenue: the employer exclusion ends | HX | −966 | −4.84 |
| Care parts B-D: long-term care, child care and pre-K, the care wage floor | HLT-9 to HLT-11, FAM-2 | 748 | 3.43 |
| Secure floor (flagship 1) | FAM-1, INC-1 to INC-5, LAB-10 | 292 | 2.53 |
| Clean power (flagship 4), legacy climate rows, **pending** | CLI-*, CX, CXP | 165 | 1.81 |
| Housing (flagship 3) | HOU-1, HOU-4D | 121 | 0.81 |
| Transportation | MOV-29 to MOV-31, MR6 | 54 | 0.72 |
| Immigration (flagship 6) | IMM-1, IMM-EV, IF1T | 29 | 0.18 |
| Everything else: education, agency capacity, work and AI, democracy, the recovery credit | EDU-*, CAP-*, LAB-8, LAB-9, AI-*, DEM-*, others | 352 | 3.07 |
| Revenue already booked: corporate, top-end, estate, enforcement | G1 to G11, H1b, GX, C18, C35, C38 to C43, IRS allowance | −1,064 | −8.49 |
| Revenue already booked: new income contributions | 2 points above $20K/$40K from 2035; 4 points above $100K/$200K from 2033 | −484 | −1.91 |
| Fund-boundary items, net (general-fund grants to the education and HI funds, less income-tax offsets; the residual to the general-fund reading) | — | −67 | −0.48 |
| **General-fund gap** | | **4,240** | **23.40** |

Health, net of HX, is about $4.1 trillion of the FY2040 gap, nearly all of it (care's `6-cost.md`, part 5: "Health's net cost is nearly all of the plan-wide gap"). Every other flagship together adds about $1.4 trillion in FY2040, roughly what the booked corporate and top-end package raises.

## 3. Inputs still moving

- **Clean power: not yet booked.** The recommended set, against the legacy climate rows above, is about **+$0.11T over FY2030-39 and about −$9B in FY2040** (`dossiers/clean-power/3-design.md`). It waits on Espen's memo answers, then sections 4-9, the milestone review and the booking. It moves FY2040 by less than 0.5% of the gap.
- **The secure floor's 65-cent ceiling (D).** The household model finds the ceiling isn't met for some families with children (`dossiers/secure-floor/7-validation.md`). The options are a SNAP earned-income deduction at 45% (up to about **$32B a year**), a $750-a-child offset (about $43B), both, or reading the ceiling as memo 7 measured it. That choice is the lead's to put to Espen.
- **The household model (M3).** Part 2 is under way (`models/tools/household/`). Stage G's fairness test (D3) needs it, along with incidence keys for INC-1 to INC-5.
- **Smaller, known items:** the hospital uncompensated-care payment is booked (`DEC-2026-11-13-02`, about $1B); SS-8's stock investment is booked at zero until its budget treatment is checked; and the climate pricing export still uses a 25% offset (about $0.6B over the decade).

## 4. The revenue options the legacy work holds

**Already counted, so not available again.** The legacy reconciliation traces **$8.005T over FY2030-39 and $989B in FY2040** of general-fund reforms already in the `mixed` case (`legacy/sources/revenue-counted-reconciliation.md`). They include G1 (corporate rate to 28%, $1.65T), G9 (reverse the 2025 cuts above $450K, $1.45T), C38 (the sprint package REV-TS1 to TS11, $0.89T), G6 (gains at death, $0.70T), G7, G10, G11, G5, G8, G3, H1b, C18, C35, C39 to C41 and C43, less the GX and CX offsets. On top of these come the new income contributions ($1.91T) and HX ($4.84T). Health's 65% employer contribution is designed but not booked.

**Not yet counted** (FY2030-39 midpoints in $T from the legacy menu, scaled from CBO and Treasury; `legacy/domains/domain-revenue.md`, "Closing the general-fund gap"; `legacy/sources/revenue-channels-and-full-menu.md`):

| Family | Option (legacy ID) | FY2030-39, $T | Who pays; main risk |
| --- | --- | --- | --- |
| Health's own financing | Employer transitional contribution at about 65% (HLT-7.18) | 5.31 (about $1,061B in FY2040, net of HX) | Employers, in place of premiums; how long it runs and when a payroll contribution replaces it |
| | States' share of the plan (HLT-7.17) | Inside HLT-7 at a working figure (about $225B in 2032; each 10 points about $45B) | States; enforceability, and the hold-harmless fallback |
| Payroll | New 1% general-fund payroll contribution, no cap (W1) | 1.6 per point | All workers; shrinks take-home pay unless it replaces premiums |
| Broad income | Surtax above $20K/$40K | 1.8 per point | Most households; breaks a $400K pledge |
| | Surtax above $100K/$200K (C20) | 0.67 per point | Upper-middle; accepted in Package B, but the `mixed` case leaves it out |
| | All bracket rates +1 point | 1.45 | Most taxpayers |
| Consumption | 5% value-added tax, narrow or broad base, before any rebate | 2.8 / 4.2 | Regressive without a rebate; new collection system |
| Top end and capital | Top four brackets +1 more point; pass-through and deferred-pay reform (REV-SC2); stock-option deduction (REV-HP2) | 0.36 per point; 0.35; 0.02 | High earners; overlaps G3, G9, H1a and SS-5 |
| Carbon and excise | Steeper carbon path (REV-C1F); road-fuel convergence (REV-C1D); alcohol and tobacco | Roughly doubles carbon receipts; small; 0.13 and 0.06 | Shrinking bases; the carbon fee is dedicated to the dividend |
| Spending offsets | Drug negotiation; site-neutral payment (check overlap with HLT-7's rates first) | 0.12-0.22; 0.19-0.23 | Providers |
| Borrowing within the rule | Time-limited capital inside the investment envelope (precedent C21) | Doesn't help FY2040 | Allowed only for capital, never for permanent programs |

**Not available:** keeping current tariffs (already in the baseline, so no new revenue), the HI reserve, and counted rows used a second time. **A quick staleness check.** CBO's latest options volume is still *Options for Reducing the Deficit: 2025 to 2034* (December 2024; cbo.gov/publication/60557), which predates P.L. 119-21. Options that interact with the 2025 law's rates and deductions need rescoring against the 2029 baseline before they are counted, as the legacy files already warn. Two scales show the size of the task. The model's own diagnostic says a broad income tier alone would need about 32 points to stop debt rising after 2045 (`models/data/recovery-budget.json`, `required_broad_rate_points`, a static proxy, not a proposal). And every top-end option still unused adds up to well under $1T over the decade. **No single family closes the gap**, so the settlement is a mix.

## 5. Questions for Espen when stage G starts (no answer now)

1. **How much of health's premium shift does a broad contribution carry?** People and employers stop paying about $3 trillion a year in premiums (2032 scale). The choices: a payroll contribution in place of premiums (the main candidate), an employer contribution kept longer, or a broad income contribution or VAT with a rebate.
2. **How far should the plan go beyond the top-end pledge?** Corporate and top-end measures already raise about $8.5T over FY2030-39 in this case, with $1.9T more from the new income contributions, and what remains at the top is small. Closing the rest means asking middle-income households to pay something, which the household fairness test (D3) has to show is fair net of what they gain.
3. **What share do states pay?** States' shares appear across health, long-term care, child care and pre-K, and the questions are their levels and the fallback when a state won't pay (`DEC-2026-11-11-05`).
4. **How strict is the timing?** Should the plan accept the fiscal rule's FY2040 test as decided and phase revenue in to meet it, or pair later starts with revenue triggers? This is a question about phase-ins, not about re-opening the rule.

The settlement also picks up the items dossiers sent it:
- housing's FY2040 and FY2041 maturity gaps (`DEC-2026-11-09-09`, `DEC-2026-11-10-04`);
- the education fund going negative in 2035 at the 1.4-point rate (about 1.7 points keeps it solvent);
- R1's child benefit, about $2.3T in the ten years after its window (the Byrd rule);
- transportation's fuel-tax path (`DEC-2026-11-10-14`);
- HOU-2D's revenue row;
- the rebuild of the financing screens in `models/tools/financing-protection/`.
