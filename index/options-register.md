# Options register: every open choice, listed once

Hand-written companion to the generated ledger, Oct 20, 2026 (after Espen's decisions that day; updated for Decision Brief 1: D2 decided, Package B and the borrowing readings accepted, the top-end sprint added). **Purpose:** one place that lists every option in the project once, says where it lives, and says which options exclude, duplicate or overlap each other, so nothing is counted twice or chosen twice. It sets no policy. The domain files govern each option's design and figures; the ledger (index/2029-trifecta-master-ledger.md) governs totals. If a figure here differs from a domain file, the domain file wins and this register is stale.

**How to read it.**
- **Status:** *Chosen* (the domain file's design); *Decided* (Espen decided it, Oct 19-20); *Option* (filed, not chosen; needs a decision); *Held* (filed, deliberately parked); *Retired* (ID kept for history, never reused); *Pointer* (the policy lives in another file).
- **Cost** is the general-fund effect over 2030-39 in $T at the midpoint, as the home file states it, and says whether it is a total or a change from the chosen design (Δ). Tags (estimate, scaled, scenario) are in the home file.
- **Group** names a set of options of which at most one can be taken (mutually exclusive). Options in a group are never summed.
- Ledger option IDs (C5 ... C38) are the ledger's names for the subset of options that close the general-fund gap. Each maps to exactly one domain option below.

## 1. Rules that keep the count honest

| Rule | What it means in practice |
| --- | --- |
| One home per policy | Every option below has one home file. A file that needs it carries a pointer, not a second design |
| Never sum a group | The groups in section 2 are alternatives. The ledger's "every option" figure takes one option per group (the ledger's ALT_CUTS list holds the alternatives it skips) |
| Count increments, not grosses, where options stack | REV-E1 is counted beyond G9; REV-SC1 beyond G3 and G9; the payroll raisers in section 4 draw on one wage base |
| Channel money is not general-fund money | Carbon, leave, Social Security, HI, transportation and public-safety receipts pay their own outlays; an option that moves money between a channel and the general fund says so |
| Borrowing is a financing choice, not an option's cost | C21, C30, C31, C32 and C37 change how a time-limited capital line is financed (D4), not what it buys |

## 2. Mutually exclusive groups (take at most one)

| Group | Members | Home | Note |
| --- | --- | --- | --- |
| G-CLI5 | **C29** (CLI-5B, trim the add-ons, $0.13T) / **C37** (CLI-5F, keep CLI-5 whole and borrow ~$0.10T of capital lines) | domain-climate.md | **Decided Oct 20: C37** (Decision Brief 1); C29 is listed in ALT_CUTS and never summed |
| G-EXCL | **C19** (= W2, median cap, $1.25T) / **C19b** (75th-percentile cap, $0.66T) | domain-revenue.md; incidence model | **Decided Oct 20: C19b** (Package B, the planning basis); C19 is the fallback if the sprint package falls short |
| G-MIDDLE | **C19/C20** (the middle-reaching closers) / **REV-ED1** used as the closer (incidence scenario G) | domain-revenue.md; domain-education.md | Scenario G replaces C19 and C20 with EDU-9B's contribution; not stacked |
| G-MEALS | EDU-3A (chosen) / EDU-3B (**C36**) / EDU-3C | domain-education.md | C36 is EDU-3B's saving |
| G-SERVICE | LAB-9A (chosen) / LAB-9B (**C33**) / LAB-9C / LAB-9D | domain-labor.md | LAB-9D starts at 9B's scale by bipartisan authorization, with 9A's R2 money as fallback |
| G-SAFCOMP | SAF-10A (chosen) / 10B / 10C / 10D (**C34**) | domain-public-safety.md | |
| G-CARBON | REV-C1A (decided Oct 20) / C1B / C1F | domain-revenue.md | Price paths. C1C (escalator) can sit on top of any; C1D (convergence) and C1E (gasoline phase-in) are scope choices, not paths |
| G-DIVSHARE | CLI-2A 80% (chosen) / CLI-2C 85-90% / CLI-2D 70% | domain-climate.md | Moves money between the dividend and CLI-5, not the general fund |
| G-SS | SS-10A / SS-10B / SS-10C (= D8 as decided) | domain-social-security.md | To do (Oct 20): test the 67-vote premise and compare again |
| G-DEM1-TIMING | Decided: DEM-1F | domain-democracy.md | Closed Oct 20 |
| G-D2 | Senate rules paths A-G | Senate Rules Reform: Options; governing doc | **Decided Oct 20: F** with Block 3, week one 2029; C with a 15-day backstop as the opening offer; G the written fallback |
| G-RECON | Reconciliation R1 / R3 / R4 | Senate Rules Reform: Options | R1 now; R3 vs R4 decided with D2's adoption resolution |
| G-D4 | D4 as written / D4-B fiscal-arc rule / D4-C deficit allowance | governing doc | Open: Espen directed a loosening (Oct 20); D4-B recommended, parameters pending |
| Every lettered set | Each domain's A/B/C/D options for one row (e.g. FAM-1A-D, HOU-3A-D, RTS-3A-E) | Each file | Treated as a group unless the file says an option can stack (e.g. EDU-4B-D add to EDU-4A; CLI-4D-F add to CLI-4A) |

## 3. Duplicates resolved: two names, one policy

| Names | One policy | Count it as |
| --- | --- | --- |
| C19 = W2 | Cap the employer health exclusion at the median premium | C19 (fallback); W2 is the revenue-menu row |
| C38 = REV-TS1 to TS11 net of REV-TSX | The top-end scoring sprint package (Oct 20) | C38 (~$0.89T); the TS rows are its parts |
| REV-TS3 and REV-SC3 | Fossil-subsidy repeal moved from SC3 to TS3 (Oct 20) | TS3; SC3 is now crop insurance only (~$0.05T) |
| Ledger revenue row T1 (keep current tariffs) vs REV-TS1 | Different policies; the sprint rows use TS so the old T1 tariff row keeps its ID | — |
| C20 = W4 | 1-point surtax above $100K/$200K | C20 |
| C35 = REV-E1 = E1 (ledger revenue row) | Estate tax at 2009 parameters, frozen exemption | **$0.15T, the increment beyond G9** (restated Oct 20 from $0.35T) |
| EDU-9C (retired Oct 20) | Was a second listing of C35 | REV-E1 |
| EDU-9D (retired Oct 20) | Was a second listing of EDU-1B | EDU-1B |
| REV-ED1 = ED1 = EDU-9B's contribution | Uncapped 1.28-1.4 point payroll contribution | Held; same base as W1 |
| REV-ED1 base = W1 base | 1% uncapped payroll (W1, general fund) vs 1.28-1.4 points dedicated (ED1) | One wage base: at most one, or a harmonized split (section 4) |
| C36 = EDU-3B | Meals at community-eligibility scale | C36 |
| C33 = LAB-9B; C34 = SAF-10D; C29 = CLI-5B; C37 = CLI-5F | | The C-ID in the ledger, the domain ID in the file |
| C21 = HOU-3C financing; C31 = HOU-5 financing; C32 = DEM-17 financing; C30 = Moving America capital (accepted) | Borrowing readings under D4 | Financing choices |
| AI-6D = REV-E2 | Public equity instead of a tax | REV-E2 (one version of the climate investment corporation and the Prosperity Fund) |
| O1 = SS-1; O2 = SS-2; OX = SS-2 haircut | Revenue-menu rows for the D8 baseline | Trust-fund channel, not options |
| FAM-4B-4D (retired); FAM-4E = EDU-5B; FAM-4F = EDU-5C | Old family-file education options | EDU-5B, EDU-5C |
| INT-5A (retired) | Fines-surcharge channel for small-dollar matching | INT-5B decided |
| G4 (replaced) | 25% minimum tax on $100M+ households | G11 in the base since Oct 19 (C22) |
| Stress test "RTS-3C" | Filed as **RTS-3E** (3C was already "without the RFRA exclusion") | RTS-3E |
| Old REV-C1A-E letters (before Oct 20) | Re-lettered when the durability path was chosen | Crosswalk in domain-revenue.md under REV-C1 |
| EXE-18B | Automatic continuing resolution | Pointer to CAP-4 (one design, in the capacity file) |
| DEM-14, DEM-15, CRT-14, NSC-2, NSC-9, AMD-3/AMD-6 statutes | Pointers | SAF-8, LAB-9, the repair's own file, EXE, climate, DEM-8/9 and DEM-5 |

## 4. Partial overlaps: options that draw on the same base or the same people

These are not duplicates, but taking both counts part of the money twice unless the second is netted.

| Pair | Overlap | Rule |
| --- | --- | --- |
| REV-E1 and G9 | G9 already reverses most of the 2025 $15M estate exemption (~$0.2-0.3T) | E1 counted as increment only |
| REV-SC1 and G3, G9 | Same top incomes | Joint score before use; inside GX's logic |
| REV-SC2 and H1a, SS-5 | Same pass-through base | Take at most one at full value |
| REV-TS3 and REV-C2 | Fossil-subsidy repeal overlaps the border adjustment's fossil scope at the margin | Net the fossil piece |
| REV-TS1 and G1 | A higher corporate rate raises the value of the denied pay deduction | Joint score |
| REV-HP1 to HP3 and REV-TS1 | All tax very high pay; HP2 and HP3 are scored net of or on top of TS1 | Score HP rows only after TS1 |
| REV-TS6 and REV-E1, G9 | Trusts and GRATs protect the same estate base | 20% haircut applied in TS6 |
| REV-TS12 and G3, G9, C18, SALT | The itemized cap stacks on top-rate options; the 2025 law already caps value at 35% | Held in reserve; needs a score |
| C18 and REV-SC1; C18 and Talarico capital-gains parity (not added) | Top brackets and gains rates | Joint score |
| **Payroll raisers** (REV-P1 leave 0.6% to 0.85%; REV-ED1 1.28-1.4 pts; W1 1%; SS-7 1 pt; SS-1 above $250K; SS-2 investment income; REV-H1a 3.8% on pass-through) | All draw on wages or the same high-income base | **Deferred to a revenue strategy session (Espen, Oct 20)**: decide how much of the wage base the agenda uses, in what order; EDU-9B's structure to be weighed "instead of or harmonized with" the others |
| CLI-11 worker guarantees (~$0.08T) and CLI-2's transition share (~$0.27T) | Same coal and energy-community workers | Draw CLI-11's worker piece from the transition share first |
| CLI-13 agriculture (~$0.08T) and CLI-5's ag R&D line | Same programs | Net against CLI-5 |
| CLI-1 and CLI-5 (45X and the transmission ITC) | Up to ~$0.2T (open, in the ledger note) | Score together |
| CLI-6C (clean load standard) and CLI-5D (data-center fee) and CLI-6E (disclosure) | One data-center question | CLI-6C is the home; CLI-5D the alternative; CLI-6E can stack |
| AI-4F and LAB-9 | Both pay young people for a public-purpose year | Build AI-4F as LAB-9's open-enrollment track if both are taken |
| AI-4C and LAB-8 | Employer-side training money | Take AI-4C only narrowed |
| EDU-4 and LAB-8 | Teacher apprenticeships | Counted in EDU-4 |
| HOU-9 and HOU-8, HOU-6 | Builder of last resort vs pilot sponsor vs zoning conditions | HOU-9A/B/C is the choice |
| CAP-7's IRS line and REV-G8 | Is G8 net of the enforcement spending? | Unchecked (CAP open item) |
| CAP-7's FTA line and Moving America | Transit staffing | Cut to zero unless it pays for staffing Moving America lacks |
| CAP-7's FTC/DOJ line and COM-2's fees | Fees fund most enforcement | Trim if fees rise |
| SAF-2 domestic deployments and NSC-1 | Savings inside a flat defense envelope | Not counted as public-safety revenue |
| CRT-5 and IMM-1 | One score for the court and the bill | Score together |
| INT-12 and CRT-2 | Judiciary disclosure | Drafted in CRT-2 |
| AMD statutes and DEM, CRT | Amendments back statutes held elsewhere | Statute in its file; amendment in AMD |

## 5. Decisions still open (by owner file)

Governing: D2 decided Oct 20 (F); the **D4 revision** (fiscal-arc options, parameters pending); the D4 Judgment Fund question (CLI-9, AAJA); D9's batch 4 reserve ($31B proposed of $37B); NSC-1's base definition.

Biggest fiscal choices: confirming the sprint package C38 (TS1-TS3 need fresh scores) and the program trims in Decision Brief 2; LAB-9 scope; EXE-14A vs 14B ($1.5-1.9T claim); the payroll-raiser strategy session.

The full list is in each file's open items; the per-domain tables below mark each open option.

## 6. Every option, by domain

### Revenue (domain-revenue.md)

| ID | What | Cost / revenue | Status | Note |
| --- | --- | --- | --- | --- |
| REV-G1, G3, G5-G11, H1b, GX | The top-end base | $6.37T mid | Chosen | G4 replaced by G11 |
| REV-H1a | 3.8% on active pass-through income, to HI | $0.5T (HI) | Chosen | Channel |
| REV-C1A | Carbon fee, $25 rising to ~$100 by 2037, road fuels exempt | $1.35T channel | **Decided Oct 20** | G-CARBON |
| REV-C1B | Old path, $50 rising 5% | $1.25T channel | Option | G-CARBON |
| REV-C1C | Emissions-indexed escalator | 0 if targets met | Option (study) | Stacks on C1A |
| REV-C1D | Road-fuel convergence (~2040) | ~0 in window | **Open, not adopted** | Would depart from D7 |
| REV-C1E | Gasoline phase-in from 2032 | +$0.27T gross | Not recommended | Conflicts with D7 |
| REV-C1F | Talarico path, $70 to $190 | ~2x receipts | Option | G-CARBON |
| REV-C2 | Border adjustment and methane fees | $0.20T channel | Chosen | Finances CLI-5 |
| REV-C2B | Clean product standard | 0 (regulatory) | Option | ◐ |
| REV-P1 | Paid-leave contribution 0.6% to 0.85% | $0.9T channel | Chosen (FAM-3A) | Payroll group |
| REV-E1 / C35 | Estate tax at 2009 parameters, frozen | **+$0.15T** (beyond G9) | **Accepted (planning basis)** | Restated Oct 20 |
| REV-E2 | Public investment corporation (= AI-6D) | Subsidy cost in CLI's ~$0.10T line | Option | |
| REV-ED1 / ED1 | Education contribution, 1.28-1.4 pts uncapped | ~$2.1T to a fund | Held | Revenue strategy session |
| REV-SC1 | 45% bracket above $5M | +$0.18T | Option | Overlaps G3, G9 |
| REV-SC2 | Pass-through and deferred-comp reform | +$0.35T | Option | Overlaps H1a, SS-5 |
| REV-SC3 | Crop insurance reform (fossil piece moved to TS3) | +$0.05T | Option | |
| REV-TS1 | 162(m) $1M pay-deduction limit for all employees of C corporations | +$0.34T | In C38; accepted in principle (Oct 20) | Joint score with G1 |
| REV-TS2 | Repeal FDII/FDDEI above the sec. 448(c) small-business receipts test (smaller C corporations keep it; decided Oct 20) | +$0.19T | In C38 | Needs a post-2025-law score; REV-TS2A (full repeal) +$0.01T |
| REV-TS3 | End fossil-fuel preferences, dual-capacity and foreign oil and gas rules | +$0.13T (0.09-0.17) | In C38; accepted in principle (Oct 20) | Green Book $110.2B (2025-34) verified |
| REV-TS4 to TS11 | Earnings stripping, spin-offs, trusts and GRATs, large retirement balances, partnership basis, like-kind, carried interest, crypto wash sales | +$0.05 / 0.05 / 0.10 / 0.03 / 0.02 / 0.025 / 0.02 / 0.03 | In C38 | |
| REV-TSX | 10% haircut on TS1-TS11 | −$0.10T | In C38 | |
| C38 | Sprint package (TS1-TS11 net of TSX) | **+$0.89T (0.60-1.14)** | Option, recommended | Mostly corporations and the top 1% |
| REV-TS12 | Cap itemized deductions' value at 28% above $450K | +$0.40T (0.25-0.55) | Held in reserve | Unscored |
| REV-HP1 | Pay-ratio surtax on corporations (high-pay guardrail) | +$0.08T (0.04-0.15) | Option | Sponsor estimate, haircut; stacks on G1 |
| REV-HP2 | Stock-option deduction limited to book expense | +$0.02T | Option | Net of TS1 |
| REV-HP3 | 21% excise on public-company top-officer pay above $1M | +$0.06T (0.03-0.10) | Option | On top of TS1 |
| REV-HP4 | Tax executives' deferred pay at vesting (sec. 409B) | unscored | Option | Pairs with TS7 |
| C18 | Top brackets +1, gains +2, LIFO repeal | +$0.62T | **Accepted (planning basis, Oct 20)** | Top-end |
| C19 (= W2) / C19b | Employer exclusion cap, median / 75th pct | +$1.25T / +$0.66T | **C19b accepted (planning basis)**; C19 fallback | G-EXCL |
| C20 (= W4) | 1-pt surtax above $100K/$200K | +$0.67T | **Accepted (planning basis)** | Reaches upper-middle; passes D3 |
| W1 | 1% uncapped payroll, general fund | +$1.6T | Option | Same base as ED1 |
| W3 | 5% VAT, narrow base | +$2.8T | Not recommended | Regressive without a rebate |
| T1 | Keep current tariffs | 0 | Baseline | Repeal = EXE-14B's claim |
| PS1 / SAF-R2 | Public-safety revenue title / swap alcohol for top-end revenue | $0.09T channel / ~$0.07T moved | Chosen / Option | |
| PS2 | Cannabis excise (contingent) | $0.02T | Option | Needs SAF-11C or separate legalization |
| MF1, IF1 | Merger and H-1B fees | ~0 net | Chosen | Channels |
| AI6 | AI levy | unscored | Held | AI-6A-C |

### Health (domain-health.md)

| ID | What | Cost | Status | Note |
| --- | --- | --- | --- | --- |
| HLT-1 to HLT-6 | Go-big bill, trimmed (D6) | $3.7T net, $4.4T GF | Decided (D6) | |
| HLT-A1 | Dental in traditional Medicare | in HLT-2 | Decided (kept) | **C5** delays it past the window (saves $0.3T) |
| HLT-A2 | Medicare at 60 | +$0.30-0.36T | Option | Scored separately (D6) |
| HLT-A3 | Medicare at 55 | +$0.6-0.9T | Option | Excludes A2 (55 contains 60) |
| HLT-A4 | Medicare for Kids / at Home | needs a broad tax | Option | |
| Health A, C, single-payer | Go-big as written; war-game version; single-payer | — | Not chosen | |

### Family (domain-family.md)

| ID | What | Cost (total) | Status |
| --- | --- | --- | --- |
| FAM-1A / 1B / 1C / 1D | CTC: 2021 design monthly / supplement / refundability only / 2025 AFA | chosen / ~0.45 / 0.3-0.5 / ~1.7 | A chosen |
| FAM-2A / 2B / 2C / 2D | Child care: phased / full cap 2030 / pre-K only / A with omnibus pre-K standards | chosen / 0.9 / 0.2-0.3 / ~+0.1-0.2 | A chosen; 2D can stack on A |
| FAM-3A / 3B / 3C / 3D / 3E | Paid leave: 0.6% with step-up / general fund / 4 weeks / 0.85% from start / open backstop | chosen / 0.9 / ~0.3 / below 0 / ~0 | A chosen |
| FAM-4 | Pointer to domain-education.md | — | Pointer |

### Social Security (domain-social-security.md)

| ID | What | Effect (share of the 4.42% gap) | Status |
| --- | --- | --- | --- |
| SS-1 to SS-4 | D8 baseline | ~65-72% | Decided (D8) |
| SS-5 | Investment-income tax on active S-corp holders and LPs | +0.9 (to 86-92%) | Option; **recommended closer** |
| SS-6 | Lower SS-2's threshold | +0.3-0.6 | Option |
| SS-7 | +1 pt payroll, phased | +0.9-1.0 | Option; payroll group |
| SS-8 | Equities in the reserves | +0.5-1.0 | Option |
| SS-9 | Cover new state and local hires | small | Option |
| SS-10A / 10B / 10C | Warren-Moreno bipartisan track first / D8 with SS-10 sweeteners / D8 only | — | Option (G-SS); **to do: re-test the 67-vote premise** |

### Education (domain-education.md)

| ID | What | Cost | Status |
| --- | --- | --- | --- |
| EDU-1A / 1B / 1C / 1D | Title I: $26B mandatory / $30B floor plus appropriations / omnibus $55B authorized / 1B plus accountability | chosen / ~0.14 (+0.06) / 0-0.35 / as B | A chosen; 1D held for ESEA |
| EDU-2A / 2B / 2C / 2D | IDEA to 40%: glide path with conditions / by FY2033 / authorized only / no conditions | chosen / ~0.35-0.40 / 0 durable / ~0.25 | A chosen |
| EDU-3A / 3B (C36) / 3C | Meals: universal / community eligibility / omnibus rates | 0.27 / ~0.08 / ~0.15 | A chosen; G-MEALS |
| EDU-4A + 4B / 4C / 4D | Pipeline; add teacher floor / PARA and mental health / bridge credit | chosen; +0.06-0.08 / +0.03-0.06 / ~+0.01 | Add-ons stack |
| EDU-5A / 5B / 5C / 5D / 5E | Pell $9,500 / doubled Pell / free community college / price-restraint conditions / HEA track | chosen / +0.3-0.4 / +0.13-0.15 / ~0 / 0 | A chosen; 5D can stack |
| EDU-6A / 6B / 6C | Department protections via CAP-8 / corporal punishment ban / ESEA reauthorization | chosen / ◐ / +4.5 floor days | A chosen |
| EDU-7, EDU-8, EDU-10 | Voucher credit repeal; AI in education; research | chosen | |
| EDU-9A / 9B | Mandatory spending / education fund | chosen / held | 9B to the revenue strategy session |
| EDU-9C, EDU-9D | — | — | **Retired Oct 20** (duplicates of REV-E1 and EDU-1B) |

### Climate (domain-climate.md)

| ID | What | Cost | Status |
| --- | --- | --- | --- |
| CLI-1A / 1B / 1C / 1D / 1E | Credits: restore all, refundable / IRA as written / household only / tech-neutral only / A to 2045 with start-of-construction rule | 0.9 / less / less / less / ~1.00 + 0.25 rebates | A chosen |
| CLI-2A / 2B / 2C / 2D | Dividend: tax-free 80% / taxable / 85-90% / 70% | 1.08 channel / −0.15-0.2 to households / CLI-5 −0.06-0.12 / −0.12 | A chosen; G-DIVSHARE |
| CLI-3A / 3B / 3C / 3D / 3E | CES: 80% by 2035 / by 2040 / none / by regulation / 80-90-100% by 2032-40 | 0.02 | A chosen |
| CLI-4A + 4D / 4E / 4F; 4B / 4C | Clean Air Act: delegations; power caps / vehicle standards / review channel in statute; or vehicles only / no statute | ~0 | A chosen; D-F stack |
| CLI-5A / 5B (C29) / 5C / 5D / 5E / **5F (C37)** | Add-ons: full / trimmed / plus relocation / data-center fee / climate bank / full with capital lines borrowed | 0.13 residual / 0 / +0.25-0.35 / own channel / ~0.10 capital / ~0.03 | **5F decided Oct 20 (C37)** |
| CLI-6A / 6B / 6C / 6D / 6E | Grid statute / minimums only / clean load standard / Congress permits the backbone / data-center disclosure | ~0 | A chosen |
| CLI-7 / 7B / 7C | Disaster and flood (unscored) / insurance help via R3 / reinsurance backstop | unscored / — / contingent exposure | 7C needs a D4 treatment |
| CLI-8 / 8B / 8C | Climate risk / extreme-risk ineligibility zones / electric-ready lending | ~0 | 8B not chosen; 8C option |
| CLI-9 | Contracts for difference | ~0.15 net | Option; borrowing-eligible (D4, Oct 20); Judgment Fund question open |
| CLI-10 | Public power and a transmission corporation | in ~0.10 lending line | Option; borrowing-eligible |
| CLI-11 | Coal securitization and worker guarantees | in ~0.10 line + ~0.08 | Option; overlaps CLI-2 transition share |
| CLI-12 | State redundancy, payment for results | ~0.15 | Option |
| CLI-13 | Farms, forests, removal | ~0.08 + ~0.03 | Option; overlaps CLI-5 ag line |

### Housing (domain-housing.md)

| ID | What | Cost | Status |
| --- | --- | --- | --- |
| HOU-1A / 1B / 1C | Emergency aid in R2 / in R1 / rental only | 0.085 / same / 0.04 | A chosen |
| HOU-2A / 2B / 2C | Credits: all three / LIHTC only / Neighborhood Homes only | — / 0.08-0.12 / 0.02-0.03 | A chosen |
| HOU-3A / 3B / 3C / 3D | Supply finance: $250B grants / loans / ~$72B grants plus loans / split | — / ~0.03 / ~0.075 / ~0.14 | C chosen; **C21 accepted** (borrowing) |
| HOU-4A / 4B / 4C | Vouchers mandatory / appropriated / entitlement | — / 0.06 / several hundred $B | A chosen |
| HOU-5 / 5B | Public housing repair / Faircloth repeal | 0.06 | Chosen; **C31 accepted** (borrowing) |
| HOU-7 / 7B | Investor limit permanent / leave ROAD as enacted | 0 | Chosen |
| HOU-9A / 9B / 9C | Federal builder: authorize with pilot / fold into HOU-8 / none | unscored | Option (Talarico) |

### Labor (domain-labor.md)

| ID | What | Cost | Status |
| --- | --- | --- | --- |
| LAB-1A / 1B / 1C | PRO Act full / without the right-to-work override / remedies only | 0 | A chosen; **Espen's call** |
| LAB-2B; LAB-3B | Article I labor court; sectoral bargaining | 0 | Held |
| LAB-4A / 4B / 4C | $17 then 2/3 median / $15 / index only | 0 direct | A chosen |
| LAB-7B | ABC test in the FLSA | 0 | Option |
| LAB-8A / **8B** | Apprenticeships / plus instructor pay line | 0.03 / +0.01-0.02 | A chosen; 8B new Oct 20 |
| LAB-9A / 9B (C33) / 9C / **9D** | Service: universal R2 / appropriations / no mixing / bipartisan authorization first | 0.12 / ~0.05 / — / ~0.05 then 0.12 fallback | A chosen; G-SERVICE |
| Codetermination; portable benefits | | | Not chosen |
| AI-4A-F, AI-5B, AI-11 | Cross-listed (home: domain-ai.md) | — | Pointer |

### Competition (domain-competition.md)

| ID | What | Status |
| --- | --- | --- |
| COM-1B | Guideline-level presumptions, no burden shift | Option |
| COM-3B | Interoperability only | Option |
| COM-4A / 4B / 4C | Non-compete ban: full / income threshold / health care first | A chosen |
| COM-5B | Junk fees as a standalone 60-vote bill | Option (path G fallback) |
| COM-6B | CFPB commission | Option |
| Staging 11.6, 11.8; Robinson-Patman | Financial regulation; public banking; Robinson-Patman | Held |

### AI and the information environment (domain-ai.md)

| ID | What | Cost | Status |
| --- | --- | --- | --- |
| AI-2A / 2B / 2C | Floor preemption / none / three-year field preemption | 0 | A chosen |
| AI-3B | Voluntary evaluation agreements in statute | 0 | Option |
| AI-4A | Transition authority | 0.20 | Chosen |
| AI-4C | Narrowed reskilling credit | +0.01-0.03 (as drafted +0.05-0.13) | Option; narrowed only |
| AI-4D | Occupations list and displacement data | ~0 | Option |
| AI-4E | Entry-level hiring credit | ~0.21 (scenario) | Option; demand side |
| AI-4F | Transitional employment guarantee | ~0.6 (scenario scale) | Option, second trifecta; overlaps LAB-9 |
| AI-5B | Limits on federal AI surveillance and enforcement | 0 | Option |
| AI-6A / 6B / 6C / 6D | Compute levy / token tax / excess-return tax / public equity (= REV-E2) | unscored | Held |
| AI-11 | AI in hiring | 0 | Chosen (rides AI-1) |

### Immigration (domain-immigration.md)

| ID | What | Status |
| --- | --- | --- |
| IMM-1A / 1B / 1C / 1D | Tiers A+B / A only / Dignity Act / all tiers | A chosen; tier C open |
| IMM-4A / 4B / 4C | Priorities and cap in statute / DHS split / executive guidance | A chosen |

### Rights (domain-rights.md)

| ID | What | Status |
| --- | --- | --- |
| RTS-1A / 1B / 1C | Full right / access only / access first, viability later | A chosen |
| RTS-3A / 3B / 3C / 3D / **3E** | H.R. 15 / athletics deferral / no RFRA exclusion / Fairness for All / athletics to joint rulemaking with sunset | A chosen; **athletics is Espen's call (A, B or E)** |

### Public safety (domain-public-safety.md)

| ID | What | Status |
| --- | --- | --- |
| SAF-2B | Personal officer liability (George Floyd Act version) | Option |
| SAF-5B | Background checks on commercial and gun-show sales only | Option |
| SAF-10A / 10B / 10C / 10D (C34) | Funding vehicle | A chosen; G-SAFCOMP |
| SAF-11A / 11B / 11C | Cannabis: deschedule / Schedule III / separate bill | A chosen; Espen's call |
| SAF-R2 | Top-end revenue instead of the alcohol excise | Option |

### National security (domain-national-security.md)

| ID | What | Status |
| --- | --- | --- |
| NSC-1A / 1B / 1C | Defense base: FY2029 / 2026-28 average / share of GDP | A chosen; base definition open |

### Democracy (domain-democracy.md)

| ID | What | Status |
| --- | --- | --- |
| DEM-1A with **1E** | One bill, with registration at benefit-delivery points | Chosen; **1E adopted Oct 20** |
| DEM-1B / 1C / 1D | Split Title III / floor only / broader results test | Option |
| **DEM-1F** | Timing: after R1, by spring 2030 | **Decided Oct 20** |
| DEM-2A / 2B / 2C / 2D / **2E** | Commissions plus ban / ban only / no exception / state maps / criteria, three-judge backstop, safe harbor | A chosen; 2E new Oct 20 |
| DEM-3A-C; DEM-4A-D | House size; STV (second-term package) | A chosen; 4C or 4D fallback to choose before 2032 |
| SAF-8 half and AI-8 riding DEM-1 | Batch 4 proposals | Open (Espen's call) |

### Courts (domain-courts.md)

| ID | What | Status |
| --- | --- | --- |
| CRT-P1 / P2 / P3 / **P4** | One bill / two bills / T1 only / judgeships split for 60 votes | P1 carried, **P2 recommended**; P4 refines P2 |
| CRT-2A-D; CRT-5A-C; CRT-15A-D | Ethics; immigration court; term limits | A chosen |
| CRT-16 | Expansion as contingent response | Held |

### Executive power (domain-executive-power.md)

| ID | What | Cost | Status |
| --- | --- | --- | --- |
| EXE-14A / 14B / 14C | Tariff approval triggers / plus sunset of existing tariffs / procedure only | 0 / **$1.5-1.9T claim** / 0 | A chosen |
| EXE-18A | Standing disbursement authority | 0 | Chosen (design rule adopted Oct 20) |
| EXE-18B | Automatic CR | 0 | Pointer to CAP-4 |
| EXE-18C | Debt-limit repeal or long suspension | 0 | Option |

### Integrity (domain-integrity.md)

| ID | What | Status |
| --- | --- | --- |
| INT-1A / 1B / 1C | Ownership ban / trading only / Congress only | A chosen |
| INT-5B / 5A / 5C | General revenue / fines (retired) / contractor assessment | B decided |
| INT-15A / 15B / 15C / 15D | Shareholder authorization: statute / SEC rule / states / disclosure only | A chosen |

### Capacity (domain-capacity.md)

| ID | What | Cost | Status |
| --- | --- | --- | --- |
| CAP-4 option | Merkley-Daines appropriations fast track | 0 | Option |
| CAP-7 at $0.5T (C17) | Agency rebuild at the low end | saves $0.1T | Option |
| CAP-7 batch 4 allocations | $31B of the $37B reserve (USCIS asylum $6B, civil-rights offices $6B, CAISI $6B, ATF/NICS $5B, State $8B) | within CAP-7 | Proposed, pending Espen |

### Amendments (domain-amendments.md)

| ID | What | Status |
| --- | --- | --- |
| AMD-1B | First-Congress recorded vote on AMD-1 (~1 floor day) | Option |
| AMD-4, AMD-8 | Suspensive veto; legislative override | Held |
| AMD-7 | Immunity amendment | Contingent |
| AMD-9 in the first Congress | Convention procedure statute (~2 floor days) | Option |
| AMD-11 | Convention applications | Held until AMD-9 |

### Transportation (transportation-moving-america-act-2031-draft-2.md)

Canonical until converted to a domain file. Its options are not yet given domain IDs; the ledger carries MOV-29 and MOV-30 and C30 (accepted). **When it is converted, its options should be added here.** D7 fixes one choice: road fuels are taxed only through its fuel-tax steps (REV-C1D, convergence, stays open in the revenue file).

## Sources

- The domain files named in each section (Oct 19-20, 2026), which govern each option.
- index/2029-trifecta-master-ledger.md and index/tools/ledger-build.py (Oct 20, later rebuild): the C-IDs, revenue rows and ALT_CUTS.
- index/revenue-household-incidence-model.md (v1.4): scenarios B, D, G, H and P (the planning basis).
- governing/decision-brief-01-senate-rules-and-gap.md (Oct 20): D2, the reconciliation dial, Package B, the borrowing readings and the sprint.
- frameworks/scenario-stress-test-talarico-2029-2037.md: where each stress-test proposal was filed.
