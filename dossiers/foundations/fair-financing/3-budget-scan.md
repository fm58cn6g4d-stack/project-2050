# Stage G, step 4b: the whole-budget scan for cuts and reallocations

Role: the targeted pass Espen asked for on November 20 (`DEC-2026-11-20-07`): no VAT; cuts and reallocations across the whole federal budget come first, and a larger health contribution (memo G3 option E) is the fallback for whatever they don't close. It sets out a current-law baseline of the whole budget by area, screens the large areas, sizes options in the best few, recommends a set, and prices the fallback. Status: **the record of step 4b, November 20, 2026. Its forks are decided** (`DEC-2026-11-24-01` to `-09`: G10.1 C, G10.2 B, G11.1 no, G11.2 yes, G12.1 C, G12.2 yes, G12.3 no, G13 A, G14 C) **and booked in step 7** (`2-settlement.md`; `models/data/inputs/settlement.json`), where the fallback rate is restated at 3.80% and G14 is shaped on enrollment. The figures below are the scan's, priced before the decisions. The forks are memos G10 to G13 in [`memos/`](memos/).

**Naming:** "step 7" is stage G's booking step. "G1" to "G14" are the memos; G10 to G14 are this step's. Some of the plan's booked revenue rows have the same names as memos (G6 gains at death, G7 foreign income, G8 IRS enforcement, G9 the 2025 cuts reversed above $450K, G11 mark-to-market). This file calls those **"row G6"** and so on; a bare "G6" is always a memo.

Units and sources:
- Federal fiscal years, nominal $B, case `mixed`. A positive gap is a shortfall; a cut is negative.
- **The base is the settlement as Espen decided it:** G1 A, G2 C (the health contribution's base rate R at 3.25% from 2035), G4 C1, G5 B, G6 C, G7 B (1.65 points), G9.1 (a) and G9.2 A (`DEC-2026-11-20-05` to `-13`), with no VAT. G8 is open and G9.3 waits on Espen; neither is touched here.
- The baseline is the adopted one (`models/data/fiscal-baseline.csv`: CBO's February 2026 baseline, with CBO's long-term outlook after FY2036) and CBO's account-level spending file (`models/data/cbo/`, publication 51142).
- The screens are `models/tools/financing-protection/budget_scan.py`. Full output is in [`notes/budget-scan-results.md`](notes/budget-scan-results.md). Project arithmetic on the project's exploratory models, not official scores.

## In plain terms

1. **What's left to close.** On the decided settlement, the plan is **$262.1B short in FY2040 (0.48% of GDP), rising to $728.4B (0.76%) in FY2056.** Memo G3 had $263B and $731B; G7's 1.65 points moves it slightly, and G6 changes only the decade.
2. **Most of the obvious places are already taken.** The plan's booked revenue rows already end the fossil-fuel tax breaks, tax carried interest as ordinary income, cap like-kind exchanges, tax gains at death and repeal the 2025 law's expensing (part B). Medicare Advantage's overpayments are already booked through 2034 and disappear into the single plan in 2035. Health, the child benefit and child care already net out the programs they replace.
3. **The one large area the plan hasn't touched is defense.** It is booked at $0: NSC-1A holds defense "roughly flat in real terms", which costs nothing against CBO's baseline. Defense is $1,232B in FY2040, 2.27% of GDP.
4. **The recommended set** (part C) does five things:
   - **holds defense flat in real terms after FY2036,** as NSC-1A already says through FY2039 (G10);
   - **restructures defense to about 5% below that path by FY2033**: the nuclear plan, missile defense held to research, the weapons mix, service contracts and headquarters (G10);
   - **reverses the 2025 law's farm-subsidy increases and reforms crop insurance** (G11);
   - **trims two tax breaks for wealthy investors** that the plan hasn't touched (G12):
     - like-kind exchanges end;
     - the small business stock exclusion keeps its startup incentive but loses the 2025 law's widening. Full repeal is priced too; it conflicts with Espen's November 20 direction to encourage innovation and small business;
   - **keeps housing's stage 2 as a capped program, not a right** (G14, Espen's November 20 question):
     - about 810,000 families housed in FY2040 instead of about 1.53 million;
     - stage 1's million awards, stage 3 and the rest of the housing plan stay;
     - the right becomes a 2040s target with a review.

   Together they are **$138.6B in FY2040 and $684.4B in FY2056**, about 53% of the FY2040 shortfall and 94% of FY2056's.
5. **The fallback closes the rest:** the health contribution's base rate at about **3.85% from 2035**, not 3.25%.
   - With it, every year from FY2040 to FY2056 closes; the tightest is FY2042, at −$5.6B.
   - From the mid-2040s the defense path builds a surplus, so a later Congress could lower the rate. That is memo G8's question, still open.
6. **For households:**
   - Health's take-home test reads the same both ways, because none of the cuts charges workers directly (G2b). **68.2% of workers come out ahead**, against 76.2% at 3.25%.
   - The VAT package Espen turned down had 57.8% ahead with the VAT counted.
   - Below 200% of poverty, 98.9% come out ahead.
   - Every fifth below the top comes out ahead on D3. The fourth fifth is +$5,490 a year, against +$4,553 with the VAT. D3's housing rows are not edited for G14.
7. **Debt falls further:** 117.8% of GDP in FY2040 and 132.9% in FY2056, against the baseline's 132.7% and 180.2%. Net interest in FY2056 is about $396B lower than on the decided settlement without the cuts.
8. **The hard part is defense.** By FY2056 the recommended path takes defense to about 1.6% of GDP.
   - The lowest since at least FY1962 is 2.91%, in FY1999 (and FY2001). CBO's baseline is already below that from FY2026 (2.73%), and 2.61% by FY2029.
   - It is the same real budget as FY2036, less 5%, but a smaller share of a larger economy.
   - Memo G10 sets out the alternatives, including CBO's own 10% topline option, and what the plan gives up.
9. **G5's backstop without a VAT** (memo G13):
   - If D2 misses, the health contribution steps up, by up to about 1.1 points in FY2040 terms.
   - If the wealth tax is struck down, its drafted deferral charge comes first, then up to about 0.6 points.

## The forks at a glance

Each is decided on its own (`charter/STANDARDS.md`, "Decision memos"). FY2040 effects are on the general-fund gap against the decided settlement ($262.1B short).

| Memo | Question | Options | Recommended | FY2040 | FY2056 |
| --- | --- | --- | --- | --- | --- |
| [G10](memos/G10-defense-path.md) | G10.1, the defense path; G10.2, the FY2029 base | G10.1: A as booked; B flat real after FY2036; C B plus a 5% restructuring; D CBO's 10% topline. G10.2: A as NSC-1A; B capped at CBO's February path | **C; B** | −101.4 | −623.3 |
| [G11](memos/G11-farm-programs.md) | Farm subsidies (two yes-or-no items) | G11.1 the 2025 increases reversed; G11.2 crop insurance reform | **Yes; yes** | −11.5 | −15.8 |
| [G12](memos/G12-tax-breaks.md) | Tax breaks the plan hasn't touched | G12.1 the small business stock exclusion: A repeal, B roll back the 2025 widening, C keep; G12.2 like-kind exchanges; G12.3 the mortgage cap | **G12.1 B; G12.2 yes; G12.3 no** | −7.1 | −12.5 |
| [G14](memos/G14-housing-guarantee.md) | The housing guarantee (stage 2's right from 2037) | A as booked; B stage 2 dropped, a 2040s target; C stage 2 capped, not a right; D the right deferred to 2045 | **C** | −18.6 | −32.8 |
| [G13](memos/G13-backstop-without-vat.md) | G5's backstop without a VAT | A the health contribution for D2, the deferral charge and top surcharge for the wealth tax; B defense for the wealth tax; C named cuts | **A** | 0 unless triggered | |
| (follows) | The fallback rate | Whatever G10-G12 and G14 leave: 3.85% at the recommendations; 4.1% with G10 B; 4.3% with G10 D; 4.85% with no defense change; 3.95% with no housing change | | | |

## Part A. The current-law baseline, by area

The whole federal budget on the adopted baseline. The tables are in [`notes/budget-scan-results.md`](notes/budget-scan-results.md), from CBO's February 2026 baseline and its account file.

**By broad category** ($B, share of GDP):

| | FY2029 | FY2036 | FY2040 | FY2056 |
| --- | --- | --- | --- | --- |
| Social Security | 1,978 (5.49%) | 2,746 (5.88%) | 3,144 (5.80%) | 5,733 (5.99%) |
| Medicare, net | 1,204 (3.34%) | 1,970 (4.22%) | 2,473 (4.57%) | 5,219 (5.45%) |
| Medicaid, CHIP, ACA credits | 874 (2.43%) | 1,145 (2.45%) | 1,352 (2.50%) | 2,518 (2.63%) |
| Other mandatory | 1,010 (2.80%) | 1,166 (2.50%) | 1,323 (2.44%) | 2,186 (2.29%) |
| **Discretionary defense** | **938 (2.61%)** | **1,100 (2.35%)** | **1,232 (2.27%)** | **2,177 (2.27%)** |
| Discretionary nondefense | 1,010 (2.80%) | 1,144 (2.45%) | 1,282 (2.37%) | 2,264 (2.37%) |
| Net interest | 1,324 (3.68%) | 2,144 (4.59%) | 2,702 (4.99%) | 6,631 (6.93%) |
| **Total outlays** | 8,340 (23.16%) | 11,416 (24.44%) | 13,509 (24.94%) | 26,728 (27.93%) |
| Revenue | 6,320 (17.55%) | 8,301 (17.77%) | 9,749 (18.00%) | 17,988 (18.80%) |
| **Deficit** | 2,020 (5.61%) | 3,115 (6.67%) | 3,760 (6.94%) | 8,740 (9.13%) |

**How to read the later years.**
- CBO's ten-year baseline runs to FY2036. It grows discretionary spending with inflation from the FY2026 enacted level (CBO's convention for appropriations).
- After FY2036 the adopted baseline uses CBO's long-term outlook, which holds discretionary spending at a constant share of GDP (`models/data/budget/categories.csv`, `gdp_share_split`).
- So **from FY2037 the baseline grows defense with the economy, not with prices.** That is a scoring convention, not a law, and it matters for part C.

**By function, discretionary and mandatory** (FY2029 / FY2036, $B; the full table is in the results note):
- **Defense (050):** discretionary $938 / $1,100; mandatory $58 / $49 (mostly military retirement accruals and the DoD retiree health fund).
- **The large mandatory programs:**
  - Social Security (650), $1,979 / $2,747;
  - Medicare (570), $1,204 / $1,970;
  - health (550: Medicaid, the ACA credit, federal employees' and retirees' health), $930 / $1,204;
  - income security (600: federal retirement, SNAP, SSI, the refundable credits, unemployment insurance, housing assistance), $602 / $707;
  - veterans (700), $338 / $490.
- **Nondefense discretionary** is spread across 15 functions. Transportation ($166 / $190), education and training ($117 / $134), income security ($118 / $133), veterans' medical care ($130 / $155) and health research and public health ($96 / $110) are the largest.
- **Agriculture (350)** is small: $34B mandatory a year, which is crop insurance plus the commodity programs, and $8-9B discretionary.

**The main programs** (CBO account file, outlays, FY2029 / FY2036, $B):

| Program | FY2029 | FY2036 | | Program | FY2029 | FY2036 |
| --- | --- | --- | --- | --- | --- | --- |
| DoD operation and maintenance | 352 | 415 | | VA compensation and pensions | 253 | 370 |
| DoD military personnel | 225 | 283 | | Civil service retirement | 124 | 146 |
| DoD procurement | 194 | 196 | | Military retirement | 85 | 113 |
| DoD research and development | 148 | 170 | | SNAP | 95 | 103 |
| NNSA (nuclear weapons) | 25 | 29 | | SSI | 72 | 97 |
| Crop insurance (FCIC fund) | 15.1 | 16.0 | | EITC, refundable part | 69 | 70 |
| Commodity programs (CCC fund) | 17.3 | 15.0 | | ACA premium tax credit | 81 | 132 |

**Spending through the tax code.** JCT's latest table counts the tax expenditures for FY2025-29 [EV-FIN-001]. The largest in FY2029, and whether the plan already touches them (each is FY2029's figure, except the oil and gas row, which is the five-year FY2025-29 total):

| Tax expenditure, FY2029 ($B) | Size | Already touched by a booked row |
| --- | --- | --- |
| Defined contribution pensions | 301.9 | REV-TS7 (large balances, inside C38) only |
| Employer health exclusion | 281.1 | **Yes: ended by HX** from the 2035 endpoint |
| Lower rates on dividends and capital gains | 252.1 | **Yes:** C18 (+2 points), HS3 (ordinary rates above $1M), G9 |
| Defined benefit pensions | 171.1 | No |
| Gains at death (step-up) | 84.2 | **Yes: row G6** taxes gains at death above an exemption |
| Qualified business income (199A) | 80.8 | Above $450K, probably through row G9 (the stack note reads it so; unconfirmed) |
| State and local taxes | 65.5 | C39's 28% cap above $450K |
| Charitable deduction, other | 64.8 | C39 |
| Equipment depreciation beyond ADS | 59.7 | **Yes: HS4** repeals the 2025 law's permanent expensing |
| Mortgage interest | 54.9 | C39 only (above $450K) |
| Active income of foreign subsidiaries | 41.0 | **Yes: row G7** (foreign income at the full rate) |
| Tax-exempt bond interest | 30.2 | No |
| Small business stock (sec. 1202) | 5.9 | **No** |
| Like-kind exchanges | 10.8 | **Partly: REV-TS9** caps deferral at $500K a year (inside C38) |
| Oil and gas depletion and drilling costs (five-year totals, FY2025-29) | 3.4 and 2.3 | **Yes: REV-TS3** (inside C38) |

The table's figures are not revenue estimates. JCT computes each one with behavior held fixed and one provision at a time [EV-FIN-001]. A repeal raises less.

## Part B. The screen: every large area, and why it is or isn't a candidate

Sizes are the baseline's ($B, FY2040 unless stated). "Booked" means a ledger row already takes it.

| Area | Size | Candidate? | Why |
| --- | --- | --- | --- |
| **Defense** (function 050, discretionary) | 1,232 (2.27% of GDP); 2,177 in FY2056 | **Yes, the largest** | Booked at $0. NSC-1A ("flat real from the FY2029 base", D9, decided in Decision Brief 2) costs nothing against CBO's baseline. Espen asked in October for "ways to reduce defense over time" (`legacy/domains/domain-national-security.md`, open item 1a) [EV-FIN-013]. Part C, G10 |
| — the nuclear modernization path | about $95B a year over 2025-34 on CBO's estimate [EV-FIN-004] | Yes, inside G10 | Sentinel breached its Nunn-McCurdy limit in 2024, and its new cost is not yet in CBO's figure. A Minuteman III life extension for part of the force, and fewer new delivery systems, are the standard alternatives. No CBO score of them was found |
| — missile defense ("Golden Dome") | CBO: nearly $1.2T to develop, field and operate a notional system [EV-FIN-005] | Yes, inside G10 | CBO's baseline carries no build-out of this size. Holding it to research keeps it from crowding the rest of a flat envelope |
| — procurement and cost growth | GAO: 46 of 72 major programs reported cost increases totaling $122B, and 16 decreases totaling $47B [EV-FIN-010] | Yes, inside G10 | Weapon systems acquisition has been on GAO's high-risk list since 1990 |
| — the FY2028 base (stage B's NSC-1A question) | 0 against today's baseline; +$131B to +$424B over FY2030-39 if 2027-28 raise the Defense bill's base (`dossiers/scenario/compounding-defense.md`); more if the FY2027 request's levels stick [EV-FIN-009] | Yes, as a rule, not a number | NSC-1A takes whatever FY2029 enacts. G10.2 |
| — overseas operations | No separate war funding in the baseline | No | War funding is emergency money, and the baseline carries no war account forward. The June 2026 Iran agreement ended the live case |
| **Farm subsidies** (crop insurance and commodity programs) | about 34 (mandatory, function 350) | **Yes, small** | The 2025 law added $53.060B to the commodity programs and $5.980B to crop insurance over FY2025-34 [EV-FIN-002]. Crop insurance reform (REV-SC3) is an open legacy option [EV-FIN-014]. G11 |
| — ad hoc farm aid | The $12B "bridge" payments (December 2025) and earlier emergency aid | No saving | Not in the baseline, so not cutting it saves nothing against it. The plan should not repeat it |
| **Fossil-fuel tax breaks** | Oil and gas depletion $3.4B and drilling costs $2.3B over FY2025-29 [EV-FIN-001] | **No: booked** | REV-TS3, inside C38 ($0.13T over FY2030-39, with the dual-capacity and foreign oil and gas rules) |
| **Other industry subsidies** | Cato counts about $181B a year on a broad definition (via search extract; an advocate's count) | Mostly no | Most of the large items are either booked (C38's corporate items, row G7, HS4), decided plan designs (clean power's credits, CLI-1), or programs with no budget cost: GAO, citing outside studies, puts the sugar program's cost to consumers at $2.5-3.5B a year in higher prices, with almost nothing in outlays [EV-FIN-011]. Its reform is worth doing for prices, but closes no gap |
| **Medicare Advantage and payment integrity** | MedPAC: MA is paid 14% more than traditional Medicare would pay for the same people, about $76B in 2026 [EV-FIN-003] | **No: booked and absorbed** | HLT-6.01 fixes coding and benchmarks on MedPAC's method from 2030 (−$0.546T over FY2030-34, booked as HLT-6). From the January 2035 endpoint the single plan replaces MA (HLT-7.14, HLT-7.25), priced at traditional Medicare's rates. Counting it again would double count (`health-cost-review.md`; `dossiers/care/6-cost.md`) |
| **Improper payments** | GAO: $186B in FY2025, government-wide [EV-FIN-008] | No booking | An improper payment is not a saving. Most of Medicaid's are missing paperwork, not payments to people who weren't eligible. Medicare's and Medicaid's ($57B and $37B) go into the single plan's rules. The EITC's come from its own complex rules, and the secure floor's redesign is where to fix them. CBO scores program-integrity money only for named activities (the IRS's enforcement, which row G8 books) |
| **Federal contracting** | About $790B of contract obligations a year, about three-fifths of it DoD's (via search extract) | Inside G10 only | No CBO or GAO score of contracting reform exists. GAO found DOGE's claimed savings largely unverifiable [EV-FIN-007]. The budget model's rule holds: reductions are smaller authorizations, not efficiency claims (`models/tools/recovery-budget/model.py`). DoD's service contracts are part of G10's restructuring; DoD has never passed an audit [EV-FIN-012] |
| **Tax expenditures the plan hasn't touched** | Part A's table | **Two small ones** | The rest of like-kind exchanges is top-heavy and untouched, and so is the small business stock exclusion's 2025 widening (G12; full repeal conflicts with Espen's innovation direction). The mortgage interest cap is priced but not recommended. 199A below $450K falls on small business, which Espen asked the plan to spare (`DEC-2026-11-15-03`). Pensions, tax-exempt bonds and the charitable deduction are broad-based or state-and-local items, not recommended |
| **Programs the flagships make redundant** | | Nearly all netted already | Health nets Medicare, Medicaid, CHIP and the ACA credits (HLT-7). The child benefit (FAM-1) is priced net of today's child tax credit. Child care (FAM-2) nets CCDF. Housing is priced as increments over the baseline, so today's vouchers stay outside it. GAO's duplication work, about $774.3B of benefits so far, is mostly already in the baseline [EV-FIN-015]. Two small leads, not priced: the child and dependent care credit for children the child-care guarantee covers, and homelessness grants once HOU-4D houses families. Each is a few billion a year. "Evidence still needed" |
| **Housing's stage 2** (the guarantee from 2037) | $39.5B in FY2040, $69.8B in FY2056 (booked as `housing_extra`) | **Yes, at Espen's request** | A decided design, so a money choice under `DEC-2026-11-15-04`. Espen asked on November 20 whether it could be a 2040s goal. Part C10, G14 |
| **Veterans' benefits** | VA compensation and pensions 370 in FY2036; medical care 155 | No | CBO's options cut disability compensation for disabled veterans. That is outside the design lens and against health first |
| **Federal civilian and military retirement** | 146 and 113 in FY2036 | No | CBO's options cut earned pensions of federal workers and service members. They are middle-income households, and the savings are small in FY2040 |
| **Social Security, SNAP, SSI, the EITC** | | No | The secure floor protects them. Their own redesigns are booked |
| **Nondefense discretionary, across the board** | 1,282 | No | It holds the plan's own priorities (research, education, transportation, the agency rebuild). An across-the-board cut would undo booked designs |
| **Net interest** | 2,702 (4.99% of GDP); 6,631 (6.93%) in FY2056 | Not a lever on the rule | The fiscal rule tests the general fund's primary balance, so interest saved never closes a year. But every cut lowers debt, and debt lowers interest: the recommended set saves about $377B of interest in FY2056 against the decided settlement. This is the direct link to Espen's point about interest rates. The budget model holds rates fixed (ASM-RATE-NOFEEDBACK), so it doesn't count the lower rates themselves |

**A baseline risk, not a cut.** The baseline counts customs duties at their current level ($441B in FY2040). If the 2025-26 tariffs are struck down or repealed, the baseline deficit rises. The plan's gap doesn't, because the gap measures only the plan's own changes. Stage G's later re-runs at each new CBO baseline will show it.

## Part C. The sized options

Each option is priced on the budget model against the decided settlement (`budget_scan.py`; [`notes/budget-scan-results.md`](notes/budget-scan-results.md)).

### C1. Defense held flat in real terms after FY2036 (NSC-1A extended)

- **What:** from FY2037, defense grows with prices (the GDP price index), not with GDP.
  - **Through FY2039 this is the booked design:** NSC-1A is "the FY2029 base grown with the defense deflator through FY2039" [EV-FIN-013]. The model's baseline grows defense with GDP from FY2037, so it over-counts the booked design by $4B, $12B and $24B in FY2037-39. Pricing that correctly is an agent's item for step 7 (part F).
  - **From FY2040 it extends NSC-1A,** which says nothing after FY2039. That is Espen's call (G10.1).
- **Saving:** **−$41.9B in FY2040, −$166B in FY2045, −$541.5B in FY2056;** −$40.4B over FY2030-39.
  - Defense falls from 2.27% of GDP to 2.20% in FY2040, 2.02% in FY2045 and 1.71% in FY2056.
  - Range: about ±15% in FY2056, from the gap between the GDP price index and defense's own costs (personnel and health costs rise faster than prices).
- **Who loses:** in real dollars no one; the budget is what it was in FY2036. But **real costs inside defense grow faster than prices,** so a flat budget buys a gradually smaller force. CBO's 2025 projection of DoD's plans had their costs rising 11% in real terms over the 10 years after the plan period (via search extract).
- **Burden:** none on households. The risk is strategic: a smaller force, and allies who agreed to 5% of GDP at NATO's 2025 summit (3.5% core) [EV-FIN-013].
- **Delivery:** defense is appropriated every year, so nothing holds it but Congress. Use the existing machinery: statutory caps on defense budget authority, as in the Budget Control Act (2011) and the Fiscal Responsibility Act (2023), with emergency money only for a declared emergency. Legal risk: none.
- **Overlap:** none. Nothing booked touches defense.

### C2. Defense restructured, about 5% below the path by FY2033

- **What:** a named restructuring, phased in over FY2031-33, at about 5% of the path (range 3-7%). It doesn't cut pay; it changes what is bought and how. Its parts:
  - **the nuclear plan:** keep the triad, but extend Minuteman III for part of the ICBM force instead of buying every Sentinel, and defer or drop the new nuclear cruise missiles. Nuclear forces are about $95B a year on CBO's estimate [EV-FIN-004];
  - **missile defense held to research:** no space-based interceptor fleet. CBO prices a notional system at nearly $1.2T to develop, field and operate, most of it 7,800 space-based interceptors [EV-FIN-005];
  - **the weapons mix:** fewer of the programs with the worst cost growth [EV-FIN-010];
  - **service contracts and headquarters:** cut DoD's service contracting and headquarters staff, verified by the audit DoD has never passed [EV-FIN-012];
  - **TRICARE fees for working-age military retirees**, as CBO's options set them, until the single plan covers everyone in 2035.
- **Saving:** **−$61.6B in FY2040 on the baseline path, −$59.5B on C1's flat-real path, rising with it;** about −$434B over FY2030-39 on that path.
  - With C1: **−$101.4B in FY2040, −$231.7B in FY2045, −$623.3B in FY2056; −$474.7B over FY2030-39.** Defense is 2.09% of GDP in FY2040 and 1.62% in FY2056.
  - **The 5% is a working assumption, not a score.** No CBO estimate of this package exists. It is benchmarked against CBO's deepest topline option, about 10% below the baseline, about $1T over ten years [EV-FIN-006]. The range is 3-7%.
- **Who loses:** defense contractors and the places that build these systems (the ICBM and cruise-missile programs are concentrated in a few states); retirees under 65, who pay higher TRICARE fees until 2035; and the strategic margin.
- **Delivery:** the program choices are made through the annual budget and the NDAA. They need the defense caps of C1 to hold.
- **Overlap:** none booked. After 2035 the single plan absorbs TRICARE's medical spending (HLT-7's federal-coverage correction), so the TRICARE fee piece ends then.

### C3. The alternative: CBO's topline option (about 10% below the baseline)

- **Saving:** −$123.2B in FY2040, −$148.1B in FY2045, −$217.7B in FY2056; −$821.8B over FY2030-39.
- It cuts more in the 2030s than C1 and C2 together, and much less later: it keeps the baseline's growth with GDP.
- **Who loses:** the same groups as C2, more sharply and sooner. CBO's version reaches its size through force structure, which means fewer people in uniform.

### C4. The FY2029 base (G10.2): what if 2027-28 raises it?

- **NSC-1A takes whatever FY2029 enacts,** excluding one-time reconciliation money [EV-FIN-013].
- The FY2027 request was $1.5T for national defense: $1.15T discretionary plus $350B through reconciliation [EV-FIN-009]. Congress's bills are lower, around $1.07-1.1T (via search extract), but well above CBO's February path (about $0.92T of budget authority in FY2027).
- Stage B priced the Defense bill's paths: +$131B to +$424B over FY2030-39 above flat real from FY2026.
- **Against today's baseline, nothing changes:** the plan's figures are measured on CBO's February 2026 baseline. But at the next baseline, a higher FY2027-28 level raises the baseline deficit, and NSC-1A carries it forward. A ceiling at CBO's February path, with any excess phased out over FY2030-32, would score as a saving against that later baseline, of about the excess.
- G10.2 asks which. It is also stage B's open question 0a ("the FY2028 defense path before summer 2027"), so Espen may prefer to answer it then.

### C5. Farm: the 2025 law's increases reversed

- **What:** the commodity programs' reference prices and the crop-insurance increases go back to the 2018 farm bill's levels, in the 2029 farm bill. The 2025 law added $53.060B and $5.980B over FY2025-34 [EV-FIN-002], about $5.9B a year.
- **Saving:** **−$6.5B in FY2040** (range 3-10, because the commodity payments depend on crop prices), grown with prices; −$8.9B in FY2056.
- **Who loses:** farm operations, mostly the larger ones that produce the most of the covered crops. Their payments fall back to the levels of 2024.
- **Political risk:** high in farm states. The scenario dossier counts several of them among the 2028 and 2030 Senate races.
- **Overlap:** none. CLI-13's conditioned farm payments ($0.0308T over FY2030-39) are separate and stay.

### C6. Crop insurance reform (REV-SC3)

- **What:** the legacy menu's option: premium subsidies cut toward 40% for the costliest policies, and the insurers' expense reimbursement and guaranteed return capped. It is $0.05T over FY2030-39 (range 0.03-0.10) [EV-FIN-014].
- CRFB puts the premium-share piece at about $35B over FY2026-35 (via search extract), at the top of that range.
- **Saving:** **−$5.0B in FY2040** (range 3-10).
- **Who loses:** crop insurers, through their reimbursements, and the farms with the largest policies. Smaller farms keep most of their subsidy.
- **Overlap with C5:** the 2025 law's crop-insurance increase ($5.980B over FY2025-34) is mostly higher premium subsidies, and SC3 also cuts premium subsidies. Priced separately, the two may overlap by up to about $0.6B a year. It is inside C6's range and is not netted.
- **Delivery:** the Risk Management Agency's existing contracts with the insurers (the Standard Reinsurance Agreement).

### C7. The small business stock exclusion (sec. 1202): its 2025 widening rolled back

- **What it is:** investors who hold qualifying start-up stock for five years pay no tax on most of the gain, up to large limits. It is $5.9B in FY2029, and the 2025 law widened it: a higher per-company cap, a larger asset test, and partial exclusions after three and four years [EV-FIN-001].
- **The conflict.** Espen asked on November 20 to "do more to encourage innovation, entrepreneurship and small business growth". This exclusion is a start-up incentive. So the scan prices three choices (memo G12.1):

| G12.1 | What | FY2040 | FY2056 |
| --- | --- | --- | --- |
| A | Repeal: gains taxed like other gains (recapture 0.7, range 0.5-0.9) | −6.2 | −11.0 |
| **B (recommended)** | **Keep the exclusion, roll back the 2025 widening** (working share 0.25 of the tax expenditure, range 0.15-0.35) | **−2.2** | **−3.9** |
| C | Keep as is | 0 | 0 |

- **Why B fits the direction:** the incentive founders and early employees use stays as it was before 2025. What goes is the 2025 extension to larger companies and shorter holds, which mostly reaches the largest gains.
- The evidence on whether the exclusion raises start-up investment is thin either way, and none is in the register; "Evidence still needed".
- **Who loses under B:** investors with very large gains in larger companies, and those who sell between three and five years.
- **Overlap:** none booked. HS3's and C18's higher rates on gains would apply to what A or B unshelters; that is not counted.
- **Growth is cautious:** the 2025 widening applies to stock issued after July 4, 2025, held three to five years. So its cost grows faster than GDP after FY2029, and growing it with GDP understates A's and B's saving.

### C8. Like-kind exchanges repealed beyond the booked cap

- **What:** REV-TS9 (inside C38) already caps deferral at $500K of gain a year. This ends deferral entirely. JCT counts $10.8B in FY2029 [EV-FIN-001], most of which TS9 already reaches.
- **Saving:** **−$4.9B in FY2040** at a working share of 0.3 of the tax expenditure, net of TS9 and of behavior. The range is $2.5-7.5B.
- **Who loses:** real-estate investors with smaller exchanges.
- **Overlap:** TS9, netted as above.

### C9. Priced, not recommended: the mortgage interest deduction capped at $500K of debt

- **Saving:** −$14.9B in FY2040, calibrated to CRFB's figure for the same cap (about $130B over FY2026-35, via search extract) against JCT's $54.9B [EV-FIN-001].
- **Why not:** it raises housing costs for middle- and upper-middle-income owners in high-cost places, against Espen's affordability priority. C39 already caps its value above $450K. It is in memo G12 for completeness.

### C10. Housing's stage 2: a right, a capped program, or a 2040s goal (memo G14)

Espen asked on November 20 whether the full housing guarantee should be cut back: "a guarantee might be too ambitious for now (could be a 2040s goal?)".

- **What is booked:** the plan's housing has three stages (`dossiers/home/6-cost.md`).
  - Stage 1 is a million new awards (HOU-4A, about $22B in FY2040).
  - Stage 2 is the right for extremely low-income families with children from 2037 (HOU-4D.01), with the duty to house and the wider entry for families with no home of their own.
  - Stage 3 is disabled renters from 2038 (HOU-4.08).
- **Stage 2's size:** it is booked as the recovery budget's housing line, **$39.5B in FY2040 and $69.8B in FY2056**. The housing dossier's own lines add up to about the same: the guarantee $23B, the duty to house $1.3B, the wider entry $8B and the restated count $8B.
- **Stage 2's reach:** about 1.53 million families leased in FY2040: 920,000, plus 306,000 from the wider entry, plus about 300,000 from the restated count.
- **This is a money choice about a decided design** (`DEC-2026-11-15-04`; the design is `DEC-2026-11-09-10` and `-12`). The housing dossier isn't edited here.

| G14 | What | FY2040 | FY2056 | FY2030-39 | Families leased in stage 2, FY2040 |
| --- | --- | --- | --- | --- | --- |
| A | As booked: a right from 2037 | 0 | 0 | 0 | about 1.53 million |
| B | Stage 2 dropped (the right, the duty to house, the wider entry); stage 1, stage 3 and the rest kept; a 2040s target with a review trigger | −39.5 | −69.8 | −115.0 | none in stage 2 |
| **C (recommended)** | **Stage 2 kept as a capped program, not a right:** the pre-right size, about 900,000 awards at 90% leased; no duty to house; the wider-entry families enter within the cap by need-based intake; a 2040s target with a review | **−18.6** | **−32.8** | **−44.0** | **about 810,000** |
| D | The right deferred to 2045, capped as C until then | −18.6 | 0 | −44.0 | about 810,000 until 2045, then 1.53 million |

- **The working share for C:** 0.53 of the right's cost, the capped families over the right's families leased. The range is 0.45-0.65, depending on the cap's size.
- **What is lost for homeless and doubled-up families.**
  - Stage 1 stays: its one plain test, "no home of your own", covers literally homeless families and doubled-up families with children first (`DEC-2026-11-09-12`), so they still have the first claim on a million awards.
  - Under C, the families stage 2's right would have reached beyond the cap (about 720,000 in FY2040) wait instead. That includes part of the 306,000 the wider entry adds.
  - The duty to house, a placement when a search fails, goes. A family whose voucher search fails gets search help and a higher payment standard, not a home.
  - Under B, stage 2's families lose that door entirely. Under D, they get it back in 2045.
- **Delivery:** C is what stage 2 is before 2037 anyway: a capped program with enrollment of up to 300,000 a year. So it needs no new machinery. The cap is the yearly appropriation, with published counts and a review trigger (design lens).
- **The take-home test doesn't see this.** Housing help is a benefit, not a charge, and no worker pays more under any of these options. So the readings both ways are unchanged; the loss is to the families who would have been housed.
- **Overlap:** none. No other cut in the set touches housing.

### The recommended set

| Item | Memo | FY2040 | FY2045 | FY2056 | FY2030-39 |
| --- | --- | --- | --- | --- | --- |
| C1 and C2: defense flat real after FY2036, restructured 5% | G10 | −101.4 | −231.7 | −623.3 | −474.7 |
| C5 and C6: farm | G11 | −11.5 | −12.7 | −15.8 | −98.7 |
| C7 B and C8: the two tax items | G12 | −7.1 | −8.5 | −12.5 | −58.2 |
| C10 C: housing's stage 2 capped | G14 | −18.6 | −22.3 | −32.8 | −44.0 |
| **Together** | | **−138.6** | **−275.3** | **−684.4** | **−675.5** |
| *Left for the fallback* | | *123.5* | | *44.0* | |
| Range: every item at its low end / high end (defense 3% / 7%; farm $3B / $10B each; the tax items' shares 0.15 / 0.35 and 0.15 / 0.45; housing's cap at 0.65 / 0.45 of the right) | | −101.2 / −177.4 | | −629.9 / −740.3 | |

**It closes about 53% of FY2040 and 94% of FY2056.** The evidence supports no more without cutting what Espen protected:
- Every larger area left is health (decided, and first), Social Security and the secure floor (protected), veterans' and federal pensions (earned benefits for middle-income households), or the plan's own flagships (every booked design stands but housing's stage 2, which Espen asked about).
- With C3 in place of C1 and C2, the set is −$160.4B in FY2040 but only −$278.8B in FY2056, so the fallback rate stays near 4.3% in the 2050s instead of falling.
- With C2 alone, it is −$98.8B in FY2040.
- With G14 B instead of C, add −$20.9B in FY2040 (fallback 3.75%); with no housing change, the fallback is 3.95%.

## Part D. What's left for the fallback

The fallback is memo G3's option E: the health contribution's base rate R above G2 C's 3.25%, from the 2035 endpoint, with its exemption as decided (nothing at or below 138% of poverty, phasing in to 250%).
- It is priced at the fold's rate: about $56B a quarter point in FY2040, grown on the contribution's path (`health-household-contribution.md` section 2).
- It is linear: the avoidance risk at higher rates is in the settlement's risk table (`2-settlement.md` part 5).

**The rate needed, year by year** (R that would close each year; decided 3.25%):

| Set | FY2040 | FY2045 | FY2050 | FY2056 |
| --- | --- | --- | --- | --- |
| No cuts (G3 E alone) | 4.42% | 4.73% | 4.71% | 4.95% |
| **The recommended set** | **3.80%** | **3.73%** | **3.41%** | **3.35%** |
| With C3 instead of C1 and C2 | 3.70% | 4.04% | 4.03% | 4.30% |
| With C2 alone | 3.98% | 4.30% | 4.30% | 4.55% |

**The package: the recommended set with R = 3.85% from 2035** (the lowest rate, to 0.05 points, that closes every year from FY2040 to FY2056 with one rate):

| General-fund gap ($B) | FY2035 | FY2040 | FY2042 | FY2045 | FY2050 | FY2056 | FY2030-39 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| The decided settlement, no cuts, R = 3.25% | 214.9 | 262.1 | | 409.0 | 491.9 | 728.4 | 1,704.0 |
| **The package** | **41.9** | **−10.9** | **−5.6** | **−32.1** | **−149.9** | **−213.5** | **434.7** |

- **Every year from FY2040 to FY2056 closes.** The tightest is FY2042 (−$5.6B).
  - From the mid-2040s the defense path builds a surplus ($214B in FY2056).
  - A rate that steps down later, or one that steps up instead of starting at 3.85%, is memo G8's question (open; Espen's "I remain skeptical about VAT" left it to a redraft). The scan doesn't pre-empt it.
- **The decade:** +$434.7B short on the model's books. G6 C holds about $250B of health's early surplus as a reserve, so the rest of the plan's own decade figure is about +$685B. The rule doesn't test those years.
- **Debt:** 117.8% of GDP in FY2040 (baseline 132.7%) and 132.9% in FY2056 (baseline 180.2%). Without the cuts, at R = 3.25%, it is 121.0% and 149.7%.

**The take-home test, both ways** (`DEC-2026-11-20-06`, G2b; FY2040; `take_home_vat.py`'s method at each rate, no VAT):

| Base rate R | Workers ahead, health costs only | **Workers ahead, everything counted** | Below 200% of poverty | 250-400% of poverty | Retirees and others |
| --- | --- | --- | --- | --- | --- |
| 3.25% (G2 C alone) | 76.2% | 76.2% | 100.0% | 89.9% | 98.0% |
| **3.85% (the package)** | **68.2%** | **68.2%** | **98.9%** | **80.7%** | **97.5%** |
| 4.45% (G3 E, no cuts) | 60.8% | 60.8% | 98.2% | 69.0% | 96.9% |
| *For comparison: the VAT package Espen turned down (R = 3.25%, VAT 2.95%)* | *76.2%* | *57.8%* | *90.4%* | *64.3%* | *89.9%* |

- **The two readings are equal here.** None of the recommended cuts charges a worker directly:
  - defense is not a household charge;
  - the farm items fall on farm operations;
  - the two tax items fall on investors with large gains, almost none of them in the test's working population;
  - G14 lowers a benefit, which the test doesn't count as a charge.
  - What everything counted adds over health costs only is the contribution above 3.25%, and the take-home test already counts the contribution.
- **Against the decided target** of 85-90% of workers ahead (`DEC-2026-11-15-02`, on health costs), 68.2% is short.
  - It is 10 points above the VAT package on the reading Espen chose to judge by.
  - The group just above the exemption (250-400% of poverty) bears most of it.
- **D3** (FY2030-39 average, $ a household a year): Q1 +14,791, Q2 +12,848, Q3 +11,261, **Q4 +5,490**, Q5 −65,397, top 1% −937,349.
  - Every fifth below the top comes out ahead. D3 has no rows for defense, farm payments or the two tax items, and its housing rows are not edited for G14, so they don't move it; the rate does.
  - G14 C would lower the bottom fifth's housing benefit from FY2037, almost none of it inside D3's FY2030-39 average. Step 7 edits the row if Espen chooses it.
  - With the VAT, Q4 was +$4,553.
- **D3's revenue-mix test:** 65% over FY2030-39, on its decided window (G3b). The test leaves out the health contribution, by `DEC-2026-11-15-29`.

## Part E. G5's backstop without a VAT (memo G13)

`DEC-2026-11-20-09` keeps the backstop and asks for its steps redrafted without a VAT. On the package, if D2 or the wealth tax fails, the gap and the base-rate points that would close it are:

| | FY2040 gap | R points | FY2056 gap | R points |
| --- | --- | --- | --- | --- |
| Without D2 | 238.5 | +1.06 | 312.8 | +0.73 |
| Without HS2 | 139.1 | +0.62 | 73.7 | +0.17 |
| Without both | 388.4 | +1.73 | 600.0 | +1.40 |

**Proposed instrument (memo G13 A):**
- **If D2 misses its path** for two years: the health contribution's base rate steps up, by 0.25 points a year, up to what closes the overrun (about 1.1 points in FY2040 terms). It is health's own instrument, visible to every household, which keeps the pressure on D2 where it belongs.
- **If the wealth tax is struck down:** its drafted deferral charge on unrealized gains takes effect first. Then the surcharge tier of the health contribution steps up before the base rate does.
  - But memo G5 says the deferral charge mostly reaches the same base as row G11 (mark-to-market), so it recovers little. The surcharge tier has little room, with top wages already taxed at 68-73%.
  - **So in practice most of a wealth-tax loss lands on the base rate,** which is how the table prices it (+0.62 points in FY2040).
- With both triggered, R would be about 5.6%, and 50.2% of workers would come out ahead. With D2 alone, R would be about 4.9% and about 56% would.
- The legal footing is the memo's: contingent legislation, as in *Field v. Clark* (1892) and *J.W. Hampton* (1928).
- The alternatives are a further defense step or named cuts (G13 B and C). They are listed with their costs.

## Part F. What step 7 books, if Espen takes the recommendations, and what this scan leaves open

**Agent items for step 7 (no fork):**
- NSC-1A's FY2037-39 years priced at flat real, its own rule (−$4.1B, −$12.0B and −$24.3B; −$40.4B over the decade). Booked as a defense row against the baseline (tier 3: it is a ledger row).

**Book if decided (tier 3, with the settlement's step 7 PR):**
- **Defense:** a new ledger row (`out_disc_defense`) for G10's path. NSC-1A's text gains an after-FY2039 clause and, if G10.2 B, a base ceiling.
- **Farm:** G11's two items as an agriculture outlay row.
- **Tax:** G12's items as revenue rows, with a JCT score against the post-2025-law baseline before drafting.
- **Housing:** G14's choice as a change to the housing line (`housing_extra`, HOU-4D.01), with the housing dossier's text (`6-cost.md`, `4-specification.md`) restated in the same PR, and D3's housing row.
- **The health contribution's base rate:** at the rate the answers leave, from 2035. The fold row (HCU), D3's HCU row and the take-home test are restated.
- **G13's backstop** as statutory text in the settlement's specification.

**Left open:**
- G8 (the later years), with the package's later surplus as its new input.
- G9.3.
- Two redundancy leads (the dependent care credit under FAM-2's guarantee; homelessness grants under HOU-4D) for the full model.
- The tariff baseline risk.

**The full model.** Espen asked for a model of every federal account later, on the same base. CBO's account file (1,979 accounts, FY2026-36) is in the repository, with OMB's history, and `budget_scan.py`'s tables read it. The next step is to map each account to the plan's rows, so every booked design shows the current-law account it changes.

**Evidence still needed:**
- CBO's own tables for its December 2024 options, read directly. CBO blocks automated downloads, and this pass read its figures only through search extracts, so the option 28 figure is a benchmark, not a price.
- A CBO or other independent score of a nuclear restructuring (Minuteman III life extension, fewer new delivery systems).
- JCT scores, against the post-2025-law baseline, of G12's items.
- USDA's or CBO's distribution of commodity payments by farm size.
- A JCT score of rolling back the 2025 law's widening of the small business stock exclusion, and research on whether the exclusion raises start-up investment.
- For G14: how fast a capped stage 2 fills, and what the waiting families' outcomes are (the housing dossier's section 7 warning lines).
- CBO's FY2026 long-term defense cost projection (report 62301) in full.

## Method and sources

- **Gap, debt and interest:** `models/tools/recovery-budget/model.py` `build_case`, case `mixed`, via `budget_scan.run_case`. Each cut is an "Exploratory: ..." outlay adjustment on top of the decided settlement (`budget_scan.DECIDED`: `packages.REC_BASE` with the education fund at 1.65 points).
- **The defense paths:** the adopted baseline's `out_disc_defense`, held at its FY2036 level in real terms on the GDP price index (`models/data/budget/deflators.csv`). The restructuring is a share of that path, phased in over FY2031-33.
- **The farm items:** FY2040 levels grown with prices from FY2030, phased in over two years. **The tax items:** JCT's FY2029 tax expenditure, grown with GDP to FY2040, times a recapture share.
- **Housing (G14):** shares of the booked `housing_extra` path from FY2037 (`budget_scan.opt_housing_guarantee`), with the housing dossier's own counts of families.
- **The fallback:** `packages.opt_fold_broad_points` at the rate R. The rate needed each year is the gap left over the fold's price on HCU's path (`budget_scan.r_needed`).
- **The take-home test:** `take_home_vat.build` at each R with no VAT (`budget_scan.take_home`). It reproduces the settlement's 76.2% at 3.25% and 60.8% at 4.45%.
- **D3 and the revenue-mix test:** `packages.Household`, as in `2-settlement.md`.
- **The baseline tables:** `models/data/fiscal-baseline.csv`, `models/data/budget/cbo-spending-by-function.csv` and CBO's account file. The historical low of defense as a share of GDP is from `cbo-historical.csv` and `cbo-economic-historical.csv` (FY1962-2025; 2.91% in FY1999).
- **Tests:** `python3 models/tools/financing-protection/test_budget_scan.py`, after the common rebuild. It checks the target, that the flat-real path is zero through FY2036, that the set adds up, that the package closes FY2040-56, and that `models/data/inputs/` is untouched.
- **Search:** Exa and Firecrawl were out of credits, so this pass used WebSearch and direct fetches (`DEC-2026-11-12-02`). CBO's site blocked direct reads (`DEC-2026-11-08-10`). Figures read only through a search extract are marked so and used only as benchmarks or ranges.
- **The second Trump administration's figures** (the FY2027 request, DOGE's savings claims, USDA's aid announcements) are used only as announced amounts, never as analysis, by `DEC-2026-10-30-01`. GAO's review of DOGE's claims is the independent check [EV-FIN-007].
