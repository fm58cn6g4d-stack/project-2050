# Stage G, step 1: the financing audit

Role: the first step of stage G, the financing settlement (`charter/PLAN.md` section 6, stage G; `DEC-2026-11-14-06`). It restates the plan-wide gap as booked on main after stage F, audits every booked revenue row and every booked cost, gives a finding and a proposed treatment for each open item, lists the errors found and proposes the rest of stage G. The later stage G steps work from it. Status: **audit, November 20, 2026; read-only.** Part F records the figures after step G2's model fixes (#467), which G4 starts from. It books nothing, changes no adopted input and decides nothing. It changes nothing that is settled: health comes first on the plan's revenue (`DEC-2026-11-15-04`); health's share comes from top-end and corporate rows first (`-20`); the fiscal rule is report, don't gate (`DEC-2026-11-10-05`); and every booked flagship design stands as decided. Where an item looks like a real fork, this file says so and leaves the choice to Espen's decision batch.

Units and sources:
- Federal fiscal years, case `mixed`. Nominal $B. A positive gap is a shortfall; in the row tables a cost is positive and revenue negative.
- **The figures come from a rerun on main at `6e115d3`** (after #461 and #462). `bash models/tools/run-all.sh` rebuilt every output, and every generated file matched the committed copy. The paths are in `models/data/recovery-budget-paths.csv` and the row lines in `legacy/sources/recovery-budget-audit.csv`. Health's first call is from `models/tools/health_booking.py` (`first_call()`), and the D2 component from `fiscal-model.py`'s component paths (`fiscal-components.csv`, HLT-7/national-budget).
- Every figure is project arithmetic on the project's exploratory models, not an official score.
- "Size" in part D means the effect on the gap if the error were fixed: + raises the gap, − lowers it.

## In plain terms

1. **The gap after stage F is $615.6B in FY2040 (1.14% of GDP) and $3,762.5B over FY2030-39.** The rerun reproduces the board's figures exactly. Health's first call on other flagships' revenue is $532.1B of the FY2040 figure. The rest of the plan's own shortfall is $83.5B: the checkpoint's $70B, plus work (+$11.3B) and democratic renewal (+$1.6B).
2. **The test that binds is the general-fund test in FY2040 and every later year.** The debt guardrail passes: on the unified budget the plan's debt is 126% of GDP in FY2040 against the baseline's 133%, and 162% against 180% in FY2056. The gap does not shrink after FY2040. It is 1.04% of GDP in FY2045 and 1.21% in FY2056 ($1,158B).
3. **Without D2, the national health budget, the gap is $865.0B in FY2040 and $4,106.7B over the decade.** The checkpoint had $852B, on the $603B base.
4. **The booked figures are sound row by row.** Five helper audits and a check of their work found every booked cost and revenue row in the model matching its dossier, apart from the superseded text listed in part D. Two errors move a figure the plan reports:
   - **H1a's early years are counted twice** across the general fund and Medicare's HI fund, $234B over FY2030-35 (part D, item 1).
   - **The household test (D3) is not run on the package the gap books.** It counts two charges the gap does not book. It leaves out $1.9T over the decade of income contributions the gap does book, and the education fund's contribution (EDU-9B) and benefits, which the gap also books. On the nearest existing scenario with the education fund (Q-EDU), the fourth quintile is behind, so whether every group below the top comes out ahead is in doubt (part D, item 2).
5. **The stage G forks are few and large.** Which rows give way for health's $532B; whether to drop or fold the 2 points on income above $20K/$40K (+$216B in FY2040 if dropped); the cap on the capital-income stack; and whether D2 is counted in the figure the plan balances to. Part E proposes how to bring them to Espen in one batch.

## Part A. The gap as booked on current main

### A1. The gap by year

| | FY2030 | FY2031 | FY2032 | FY2033 | FY2034 | FY2035 | FY2036 | FY2037 | FY2038 | FY2039 | **FY2040** | FY2030-39 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| General-fund primary balance, short ($B) | −201 | −87 | 86 | 86 | −23 | 541 | 840 | 851 | 856 | 813 | **616** | **3,763** |
| Share of GDP | −0.54% | −0.22% | 0.21% | 0.21% | −0.05% | 1.20% | 1.80% | 1.76% | 1.70% | 1.56% | **1.14%** | — |

Source: `agenda_gf_primary_bn`, case `mixed`. Later years: $676B in FY2045 (1.04% of GDP), $825B in FY2050 (1.06%) and $1,158B in FY2056 (1.21%).

**Against the rule's other legs** (D4; the reading is decided: `DEC-2026-11-08-03` to `-07`):
- **The unified reading** (`program_primary_bn`) is a $237.9B primary surplus in FY2040, because the dedicated funds run surpluses, Social Security's above all.
- **Debt and net interest stay below the baseline path** on the budget model: debt is 126.2% of GDP in FY2040 against 132.7%, and 161.9% against 180.2% in FY2056. Net interest is $2,638B against $2,772B in FY2040. *Caveat:* these debt figures count H1a's FY2030-35 revenue twice (part D, item 1), so they are low by about $234B of debt plus its interest, about 0.4-0.5% of GDP. The margin below the baseline survives it.
- **The +1-point rate stress** (`mixed_all_debt_rate_plus1`) leaves the primary gap unchanged. Debt is 135.0% of GDP in FY2040 against the stressed baseline's 142.1%, and 196.2% against 217.4% in FY2056.
- **The downside case** (`mixed_downside`: receipt losses and stressed costs) gives a gap of $904B in FY2040 and $5,702B over the decade. Debt reaches 181.0% in FY2056, just above the baseline's 180.2%.
- **The long-term model reads the guardrail differently.** Its DEC scenario (`fiscal-model.py`, `models/data/fiscal-paths.csv`) has debt at 194.3% of GDP in FY2056 against 180.2%, so the plan would be above the baseline. Part of the difference is the $639B of capacity the gap model trims (part B3). Part C, item 26, proposes naming one reading of record.

### A2. By flagship

FY2040 and FY2030-39 ($B), from the audit lines. A cost is positive and revenue negative. This follows the checkpoint's part A2 and adds stage F's flagships. AI-4's trim to $0.12T sits in the line "Smaller capacity and AI authorizations"; here it is moved to work and AI, and the rest of that line stays with agency capacity.

| Driver | Rows | FY2040 | FY2030-39 | FY2035 | FY2045 |
| --- | --- | --- | --- | --- | --- |
| Health, the single plan's spending (net of the federal money it replaces and the states' payment) | HLT-1, 2, 4, 6, 7, 8 | 3,553.7 | 19,513.0 | 2,679.0 | 4,583.6 |
| Health's own financing | HEC, HX, HCU, HEX, HCW, HCA, HCP, HCH, HS1 to HS4, H1a | −3,019.0 | −17,389.0 | −2,259.5 | −3,788.6 |
| **Health, net** | | **534.7** | **2,124.0** | 419.5 | 795.0 |
| Care parts B to D | HLT-9, 10, 11, FAM-2 | 747.7 | 3,427.0 | 405.7 | 947.3 |
| Secure floor | FAM-1, INC-1 to INC-5, INC-2B, LAB-10 | 303.3 | 2,628.0 | 269.1 | 340.9 |
| Clean power | CLI-*, CX, CXA, CXP, C1T | 125.1 | 1,896.6 | 184.3 | 130.8 |
| Housing | HOU-1, `housing_extra` (HOU-4D) | 120.5 | 806.0 | 81.1 | 141.5 |
| Transportation | MOV-29 to 31, MR6 | 53.5 | 722.3 | 87.6 | 43.5 |
| Immigration | IMM-1, IMM-EV, IF1T | 22.6 | 149.4 | 14.9 | 27.2 |
| Work and AI | LAB-* (but LAB-10), AI-1, AI-4 (net of its trim), AI-9 | 54.6 | 387.0 | 45.3 | 65.6 |
| Democratic renewal and agency capacity | DEM-*, CRT-*, CAP-7, CAP-7S, CAP-7P, CAP-8, the capacity trims, the delivery contingency, the SSA reclassification, the FY2029 advance | 63.9 | 583.2 | 67.5 | 76.5 |
| Education (ledger rows) | EDU-1, 3, 4, 5, 7, 8 | 111.5 | 925.0 | 96.8 | 128.6 |
| Other | Recovery credit, DEV-P, NSC-8, NSC-10, SAF-10, G8P | 133.3 | 1,145.9 | 116.1 | 153.1 |
| Revenue booked: corporate, top end, estate, enforcement | G1 to G11, GX, H1b, C3A, C18, C35, C38 to C43, the IRS allowance | −1,105.8 | −8,658.0 | −880.7 | −1,359.6 |
| Revenue booked: the indexed income contributions | 4 points above $100K/$200K; 2 points above $20K/$40K | −483.8 | −1,906.9 | −252.3 | −754.6 |
| Fund lines | Social Security (−731.9), the education fund (−202.2), paid leave (+15.6), HI, SMI | −918.8 | −6,598.4 | −730.2 | −1,202.9 |
| The general fund's grants to the funds, added back | | 853.5 | 6,131.3 | 616.8 | 1,143.5 |
| **General-fund gap** | | **615.6** | **3,762.5** | 541.4 | 676.3 |

**Health's first call** (`first_call()`, health's booked need less its own revenue) is $532.1B in FY2040 and $1,886.8B over FY2030-39: −$883.2B over FY2030-34 (health's sources run ahead of its need) and +$2,770.0B over FY2035-39. The rest of the plan is $83.5B in FY2040 and $1,875.7B over the decade. Health's rows net to $534.7B, slightly above its first call, because HLT-4's care parts and H1a's early years sit on the fund boundary.

### A3. By revenue row

FY2040 and FY2030-39 ($B, revenue shown positive). The vintage column says what the score rests on. "Pre-2025 law" means a score made before P.L. 119-21, the 2025 reconciliation act.

| Row (legacy ID) | What | FY2040 | FY2030-39 | Score and vintage |
| --- | --- | --- | --- | --- |
| G1 (REV-G1) | Corporate rate to 28% | 201.4 | 1,650 | Treasury Green Book FY2025, ×1.2; pre-2025 law |
| G9 (REV-G9) | The 2025 law's cuts reversed above $450K | 181.9 | 1,450 | TPC's share of the 2025 law's relief; current |
| C38 (REV-TS1 to TS11) | The sprint package | 113.5 | 890 | Green Book FY2025 via ITEP; pre-2025 law; TS1 to TS3 "need fresh scores" (`ledger-cuts.csv`) |
| G6 (REV-G6) | Gains taxed at death | 91.6 | 700 | CBO option, scaled; pre-2025 law |
| G11 (REV-G11) | Mark-to-market for the wealthiest | 81.5 | 650 | JCT $557B 2022-31 (the 2021 Wyden draft), carried to 2030-39; pre-2025 law |
| C18 | Top four brackets +1, gains +2, LIFO repeal | 77.8 | 620 | CBO, scaled; pre-2025 law |
| H1b (REV-H1b) | Medicare and investment-income rates to 5% above $400K | 62.7 | 500 | Treasury FY2025 via CRFB; pre-2025 law. Its wage half ($43.5B) is taken back by HCH |
| G8 (REV-G8) | IRS enforcement | 54.8 | 400 | Estimate; net of the IRS allowance (−34.2, −250) it is 20.5 and 150 |
| G7 (REV-G7) | Foreign income at the full rate | 50.1 | 410 | CBO, scaled; pre-2025 law |
| C39 (REV-TS12) | | 50.2 | 400 | Unscored estimate |
| G5 (REV-G5) | Buyback tax 4%, corporate minimum 21% | 48.8 | 400 | Treasury; pre-2025 law |
| G10 (REV-G10) | Financial transactions tax, 0.01% | 48.8 | 400 | CBO, scaled |
| C3A | Clean electricity standard compliance payments | 41.5 | 163 | Energy model, November 2026 |
| G3 (REV-G3) | Top rate to 39.6% above $400K | 37.6 | 300 | Treasury; pre-2025 law |
| C43 (REV-SC1) | A 45% bracket above $5M | 22.6 | 180 | Scenario figure, not a score |
| C35 (REV-E1) | | 20.2 | 150 | Estimate; post-2025 law, counted beyond G9 |
| C40 (REV-HP1) | CEO pay-ratio surtax | 9.8 | 80 | Sponsor's estimate with a 50% haircut |
| C41 (REV-HP3) | | 7.3 | 60 | Estimate |
| GX (REV-GX) | Overlap haircut, 15% of G11, G6, G9 and H1b | −62.1 | −495 | Project estimate |
| **Corporate, top end, estate, enforcement** (with the IRS allowance) | | **1,105.8** | **8,658** | |
| Indexed income contributions: 4 points above $100K/$200K, from 2033 | | 267.6 | 1,410.4 | CBO December 2024 and JCT option 60938, translated on GDP; pre-2025 law |
| Indexed income contributions: 2 points above $20K/$40K, from 2035, full in 2044 | | 216.3 | 496.5 | The same. At its full 2 points it is $417.7B in FY2044 |
| **Indexed income contributions** | | **483.8** | **1,906.9** | |
| HEC | Employer health contribution | 1,945.3 | 9,678 | Package E, November 2026 |
| HX | The exclusion ends: tax on former premiums | 965.8 | 4,835 | The same |
| HCU | Household health contribution | 770.3 | 4,606 | The same, net of the 20% avoidance allowance |
| HEX | Tax HEC takes from HX | −607.7 | −3,023 | The same |
| HCW, HCA, HCP, HCH | The worker's Medicare taxes folded into HCU | −439.6 | −1,864 | The same. HCA is $53.5B, a working figure |
| HS1 to HS4 | The new streams: FTT 0.1%, wealth tax, gains as ordinary income above $1M, corporate 30% and expensing repealed | 324.9 | 2,665 | Round figures, "net of" overlaps by label (`models/tools/health_cost_review.py`) |
| H1a (REV-H1a) | 3.8% on active pass-through income | 60.0 | 492 | CBO $440B 2026-35; pre-2025 law |
| **Health's own financing** | | **3,019.0** | **17,389** | |
| Social Security line | SS-1 to SS-5, SS-7.01's fallback, net of its income-tax offset | 731.9 net (778.4 revenue, 46.5 outlays) | 5,125.7 net | SSA's 2026 scores; current |

About $4.9T of the decade's booked general-fund revenue rests on pre-2025-law scores (G1, G3, G5, G6, G7, G10, G11, H1a, H1b, C18, C38 and the indexed income contributions). CBO's latest options volume (December 2024) predates the law (checkpoint part A4). Part C, item 22, proposes the treatment.

### A4. The without-D2 figure, Social Security and the household quintiles

- **Without D2** (HLT-7/national-budget: −$249.4B in FY2040, −$344.2B over FY2030-39, from FY2037): **$865.0B in FY2040 and $4,106.7B over the decade.** D2 grows to −$324B in FY2045 on CBO's Medicare growth.
- **Social Security** (`legacy/index/dedicated-funds.md`; the funds model after the work booking added WRK-UI-SS): current law depletes in 2034. The D8 baseline closes 63% of the 75-year gap and depletes in **2060**. D8 plus SS-5 closes 82% and depletes in **2079**. The board's "83%, 2080" was the reading after #405; WRK-UI-SS (−$43.3B to the fund over FY2031-39) moved it.
- **The household quintiles** (D3, `models/tools/household/results.md` section 5; FY2030-39 average, measured keys; scenario Q-H7, health as booked): Q1 +$14,663, Q2 +$13,279, Q3 +$12,587, **Q4 +$8,171**, Q5 −$56,423, top 1% −$867,330. Every quintile below the top comes out ahead. The revenue-mix test reads 66%. **But Q-H7 is not the package the gap books** (part D, item 2), so these figures are a reading of a nearby package. Q-H7 leaves out the education fund, which `mixed` books at 1.4 points. Scenario Q-EDU, which adds it to Q (without health), puts Q4 at −$1,294 against Q's −$90. So on the booked package Q4's sign, not only its size, is in doubt. The health take-home test (`health-household-contribution.md`) is separate: 88.7% of workers ahead without the booked 2 points, 70.1% with them.

## Part B. Every booked revenue row and every booked cost

Five Standard-tier helpers audited the cost files and the revenue rows against the audit lines and the ledger. This step checked their claims against both sides, and one claim was wrong (B3). Every booked row matches its dossier's cost file to rounding, except where a cost file still quotes a superseded booking (part D, items 5 to 8).

### B1. Revenue rows

- **Matches:** every row in A3 matches its ledger midpoint and dossier source. GX's FY2040 path follows its own profile ($62.1B against 15% of its four rows, $62.7B). That difference is immaterial.
- **Double counts:**
  - *H1a in FY2030-35, confirmed:* part D, item 1.
  - *GX on H1b's folded wage half, confirmed:* GX still takes 15% of all of H1b, but HCH takes H1b's wage half back from FY2035 (`DEC-2026-11-15-13`). The haircut is therefore taken on $43.5B the plan no longer books there. Fixing it lowers the gap by about $6.5B in FY2040 and $28B over the decade (part D, item 3).
  - *HS4 against G1, plausible, not confirmed:* the ledger calls HS4 the increment above G1's 28%, at a round $70B. Two points at G1's own per-point yield are $57.5B, which leaves about $12.5B for repealing permanent expensing. G1 is scored on a pre-2025-law baseline, where bonus depreciation was already phasing out. So part of HS4's expensing piece may restore something G1's base already assumed. The fix step should read the Green Book's depreciation baseline.
  - *HS1 to HS3 are round figures "net of" their overlaps by label, not by computation.* HS3's stated overlaps (G6, C18, G9) omit G11 and HS2. That does not prove a double count, but the netting is unverified.
  - *Not double counts:* the carbon fee receipts (C1, C2, CB1, C1P) are matched receipts outside the general fund; the dividend is off it; and CX, CXA and CXP are correctly signed costs. H1b and HCU are not double counts, because HCH takes the wage half back. REV-SC2 is not booked.
- **Stacking.** GX's 15% covers only G11, G6, G9 and H1b. The wage stack (G3, G9, C18, C43, the 4 points, HCU's surcharge, SS-1) is booked at about 80-85% yield. At the project's working elasticity (0.25) the stack note finds 60-64% (`dossiers/foundations/notes/stack-2026-11-16.md`, part 3). A rough, unverified reading puts the overstatement at up to about $140B in FY2040. This is a working-assumption question (part C, item 12), not an error.
- **Stale bases:** about $4.9T of the decade's revenue rests on pre-2025-law scores (A3). The payroll point ($135B for 2030, `assumptions.json` `education.payroll_per_point_2030_bn`) is CBO's capped taxable payroll read as all pay. It understates revenue on uncapped bases and slightly overstates it on capped ones. Within the general-fund gap the effect is small, because the education fund's grant is set as a share of its outlays (part C, item 16).
- **Labels:** HS2's legal risk is "High" in the ledger and "Medium" in `health-cost-review.md` (line 379, the package table). The 0.9% Additional Medicare Tax (HCA, $53.5B) is a working figure and probably low, nearer $70B (`health-household-contribution.md` 6). If $70B, the gap rises about $16.5B in FY2040.

### B2. Health part A and care parts B to D

- **Matches:** HLT-1, 2, 4, 6, 7 and 8, HX and HLT-9 to 11 and FAM-2 match the model. The care parts sum to $750.0B in FY2040 and $3,662B over the decade, HLT-4's part included.
- **Superseded text, not booked figures:** `dossiers/care/6-cost.md` part 5 still shows HLT-7 at $26,007B and $5,040.3B (line 166) against the booked $18,938B and $3,532.1B, with a header that still says "booked". The ledger's HLT-7 row still cites it as its source (part D, item 5).
- **Double counts:** none confirmed.
  - Part C child care and pre-K, inside the education fund (EDU-9B), is netted: the replacement line takes FAM-2's booked path out as the "old agenda" transfer (`models/tools/recovery-budget/model.py` 51-66).
  - HLT-9 is an increment over current law, and HLT-7 leaves Medicaid's long-term care out of the plan.
  - One small, unconfirmed overlap: Medicaid's patient-pay left "as is" against HLT-9.08's resident contribution from 2035, on the pre-#394 path.
- **The education fund** goes negative in 2035 at 1.4 points (−$30B), reaching −$254B in FY2040. It stays solvent at 1.7 points (+$106B in FY2040). The `mixed_reserve_corridor` case never goes negative, because it adds general-fund grants, and it raises the gap to $660.6B in FY2040 and $4,361.9B over the decade. The negative reserve does not understate the booked general-fund gap. The fund's outlays are booked in full.

### B3. Secure floor, clean power, housing, transportation, immigration, work and democratic renewal

- **Matches:** every booked row matches its file to rounding. The stage F bookings reconcile: work +$11.3B and −$23.0B, democratic renewal +$1.6B and +$12.1B.
- **AI-4 is trimmed, as booked.** A helper reported that work's "$0.12 trillion in `mixed`" (`dossiers/work/6-cost.md` part 9) contradicted AI-4's $200B line. It does not. The trim is applied in the line "Smaller capacity and AI authorizations" (`model.py` 216-217; `recovery-adoption.json` `ai_transition_tn` 0.12), which also trims CAP-7S to $105B and CAP-7 to $300B before the USCIS removal. Those trims total $718.8B over the decade: $80B of AI-4 and $638.8B of capacity. That $638.8B is the "$639B more capacity" the long-term model carries (A1).
- **Double counts:**
  - *DEC-DYN's DY4 and LAB-1, confirmed:* both rest on CBO's 2021 Raise the Wage score. DY4 is in `ledger-dynamic.csv` (line 5; −$0.07T mid) and feeds only the long-term model's DEC-DYN scenario. LAB-1 is booked at $32.0B and $5.5B. **DEC-DYN does not feed case `mixed` or the gap.** Dropping DY4 is the right fix, because dropping LAB-1 would move the gap. The scenario's label also still reads "about −$0.56T" against a ledger sum now near −$0.33T (`scenarios.json` line 91).
  - *LAB-18 and AI-4's wage-insurance part, confirmed and bounded:* up to about $3.35B in FY2040 and $22B over the decade, until the AI topic re-scopes AI-4. Re-scoping lowers the gap by up to that amount.
  - *Agency builds paid twice in a ceiling, confirmed and absorbed:* the IRS child-benefit build, HUD's lending office and EPA's reporting staff sit in flagship rows and also in the legacy CAP-7 and CAP-7S rows (about $4.4B over the decade and $0.35B in FY2040). They fall inside memo 10's unclaimed headroom, so the gap does not move.
  - *CRT-5.09, the Article I immigration court:* it is carried inside CRT-P1's booked $10.0B (`dossiers/foundations/democratic-renewal/6-cost.md` part 1). Democratic renewal's design section (`3-design.md`) and the board still call it "$3-10B, unbooked". Adding it in stage G would count it twice.
  - *The two delivery contingencies* (memo 10's, inside CAP-7S and CAP-7, and the $100B `delivery_contingency` line): their lanes are not written down, so one delivery failure could draw on both. They are ceilings, so this is a lane question, not a gap error (part C, item 31).
  - *DEM-17.02 against the IMLS baseline, plausible:* the line books a whole permanent IMLS level and nets no baseline. If CBO's baseline still carries IMLS's Grants to States (about $0.18B a year), the line is overstated by about $2.1B over the decade and $0.25B in FY2040.
- **Housing:** no errors, and no double count with Rural Development. HOU-14.01 costs its rebuild once, sized for housing's loans alone. Four other flagships use its front doors and pay none of its staff, a possible understatement of a few hundred million dollars a year (part C, item 33). `financing-protection/packages.py` line 17's screen "additional housing 135 to 100" predates HOU-4D's $115B and its FY2035 start. It is historical, as the file's docstring says, and is rebuilt in stage G (part C, item 25).
- **Transportation:** no errors. MR6 slightly front-loads its offset (it books MOV-29's FY2029 receipts from FY2030). That is minor and disclosed.
- **Immigration:** no booked-row errors. Its cost file still describes the E-Verify funds line as unbooked (part D, item 7).
- **Clean power:** C3A (−$41.5B in FY2040) is compliance payments that vanish if suppliers comply, on an energy model whose benchmarks miss by 5.7% and 26%. It is the largest risk-bearing revenue row outside the top end (part C, item 34).

## Part C. Every open item, with a finding and a proposed treatment

The treatments follow `charter/STANDARDS.md`, "What needs an answer now": **decide now** (a fork for Espen's batch, or an agent's choice where it defines no commitment), **working assumption**, **leave open** or **study in implementation**. "Fork" marks the items that look like real forks for Espen. Each is to be marked provisional when drafted (Espen's stage G method).

**Sources of the list:** `checkpoint-financing.md` part C (C) and part D (D1 to D16); the board's "For stage G" list (B) and In motion item 4 (c) and (d); and Known gaps, "For the financing settlement" (K).

### C1. Settling the gap

| # | Item (source) | Finding | Proposed treatment |
| --- | --- | --- | --- |
| 1 | Which flagships give way for health's call, and which rows (D6; `DEC-2026-11-15-20`) | Health's call is $532.1B in FY2040 and $1,886.8B over the decade. The rest of the plan is $83.5B and $1,875.7B. The order is settled: top-end and corporate rows first. | **Decide now, fork.** Step 2 drafts a recommended package that closes FY2040 and every later year on the general fund, with cuts or refinancing by flagship and the rows reassigned. |
| 2 | Health's early surplus: held as a reserve or counted against the rest of the plan (D3; C menu 1) | −$883.2B over FY2030-34. `DEC-2026-11-15-29` pays it into the plan's fund; the model books it on the general fund. It does nothing for FY2040. | **Decide now, fork** (the plan's fund rules). Recommendation to draft: hold it as the plan's fund reserve against the endpoint years, and show the decade figure both ways. |
| 3 | How strictly to phase revenue to the FY2040 test and to the decade's debt path (D16) | The debt guardrail passes on the budget model; the general-fund test binds from FY2035 and grows after FY2050. | **Working assumption:** balance FY2040 and every later year on the general fund (the rule), and report the decade figure for the guardrail only. |
| 4 | D2's risk: report the gap without it (D2; B; `DEC-2026-11-15-08`) | $865.0B and $4,106.7B without D2, against $615.6B and $3,762.5B with it. | **Decide now** (how it is reported): every stage G figure shows both. Whether the package balances to the with-D2 figure, or holds a backstop for D2's failure, is a **fork** for the batch. |
| 5 | The +1-point interest stress (C; `DEC-2026-11-08-06`) | The primary gap does not move, and debt stays below the stressed baseline (A1). | **Working assumption:** reported, not balanced to, as decided. Restate each run. |
| 6 | Re-run triggers: each new CBO baseline, later waves, before 2028 (plan section 6) | Not an item to settle now. | **Leave open.** Record it in step 5's close-out. |

### C2. The household side

| # | Item | Finding | Proposed treatment |
| --- | --- | --- | --- |
| 7 | The booked 2 points above $20K/$40K (D1; B; `DEC-2026-11-15-11`) | $216.3B in FY2040 and $496.5B over the decade, $417.7B at its full 2 points in FY2044. With it, 70.1% of workers come out ahead instead of 88.7%. | **Decide now, fork:** drop, or fold into HCU. Dropping raises the gap by $216B in FY2040; folding moves the same base into the health contribution's rate. Step 2 prices both. |
| 8 | The household test on the booked package (part D, item 2) | D3's Q-H7 counts C19b and C20, which the gap doesn't book. It leaves out the $1.9T indexed income contributions and the education fund (EDU-9B), which the gap does book. Q4's sign is in doubt. | **Decide now (agent):** step 3 runs D3 on the package the gap books, before the batch. |
| 9 | The 20% avoidance allowance, set by tier (D7; B) | Each 10 points moves HCU by about $104B. On a broad base collected by withholding, avoidance is likely smaller. | **Working assumption:** 10% on the withheld base below the surcharge and 20% above it, with a range of 10-25%. Step 2 shows the effect. |
| 10 | The states' shares across health, long-term care, child care and pre-K, together (D14; `DEC-2026-11-11-05`) | Health is at 100% of former Medicaid ($466B in FY2040), long-term care at 50% (HLT-9.09) and child care at the bridge's match. The three rest on one instrument. | **Decide now (agent):** a table of the combined state payment against states' current spending, for the batch. **Leave open** unless it shows a state's payment rising above today's. |

### C3. The top end

| # | Item | Finding | Proposed treatment |
| --- | --- | --- | --- |
| 11 | The capital-income stack cap (D4; B; `DEC-2026-11-15-16`) | The combined charge passes 100% of a 6% return above $50M: 105-109%, and 126% above $1B. The stack note's cap menu runs from A (no cap, $0) to C2 (a 75% ceiling, about $125B) and D1 (about $100B). | **Decide now, fork:** the cap design. The recommendation is drafted in step 2 from the stack note's menu. |
| 12 | The top rate on wages across flagships (D5) | 68.3% at $500K and 72.7% at $20M in FY2040; 69.7% and 74.1% at maturity. Health's 67.7% leaves out C18's point and SS-7.01's fallback. The booked yields assume 80-85% of the stack's statutory revenue; the working elasticity gives 60-64%. | **Working assumption** for the yield (part B1), with its range. A wage-stack ceiling (F5) belongs to item 11's fork. |
| 13 | The wealth tax's legal risk (D4) | $149.9B in FY2040 and $1,230B over the decade. If it fell, the gap would rise by about that much, and its fallback (a deferral charge, as G11's) is mostly G11's base. | **Working assumption:** booked, with a without-HS2 line in every stage G figure. The backstop is part of item 4's fork. |
| 14 | REV-HP2 and a fifth bracket point; REV-SC2 overlaps H1a (C menu 3) | Small: well under $1T together over the decade, and they meet item 11's cap. | **Leave open**, as menu items for step 2. |

### C4. The model's own items

| # | Item | Finding | Proposed treatment |
| --- | --- | --- | --- |
| 15 | The 0.9% Additional Medicare Tax at $53.5B (D13) | Probably nearer $70B: +$16.5B in FY2040 and about +$70B over the decade. | **Working assumption,** re-derived in the fix step from the CPS's top wages. |
| 16 | The payroll point: $135B against about $158B on all pay (D8; B) | It understates uncapped bases, slightly overstates capped ones, and leaves the general-fund gap almost unmoved. | **Decide now (agent):** the fix step names each row's base and uses the matching point. Tier 3 where it moves an adopted input. |
| 17 | SS-8's budget treatment (D9; C; `ss8-budget-treatment.md`) | Booked at zero under a Railroad Retirement-style clause. The memo line is about $0.7T of debt held in stocks by 2039. Without the clause it is +$0.49-0.62T over the decade. | **Working assumption:** zero, with the clause written into SS-8.01 at the secure floor's next touch, and the $0.7T memo line shown in stage G's report. |
| 18 | E-Verify's funds line (C) | Booked in the funds model (IMM-EV-SS, about −$42B over the decade). | **Done.** Immigration's text is fixed in part D, item 7. |
| 19 | D3 small follow-ups from #394 (D10 to D12) | Done in #402, except D2's cautious after-window path, which errs low on revenue. | **Leave open.** |
| 20 | `fiscal-model.py`'s DEC scenario carries $639B more capacity (B) | Confirmed: the trims of part B3. | **Decide now (agent):** a tier-3 clean-up applies the trims in the long-term model (part D, item 4). |
| 21 | SS-8's clause into SS-8.01; SRC-3666's date is April 1999 (B) | Text items. | **Done at the secure floor's next touch,** not in stage G. |
| 22 | Pre-2025-law scores (checkpoint A4; part A3) | About $4.9T of the decade's revenue. | **Working assumption** for stage G, with a stated range. **Study** in the lead-up to 2028: rescore against the 2029 baseline before the plan goes public. |
| 23 | The budget model's held nits (Known gaps): HLT-7's ledger note; "−0.00 points" | Cosmetic. | **Leave open.** |
| 24 | The DY4 and LAB-1 double count in DEC-DYN (In motion 4(c)) | Confirmed. It does not feed the gap. | **Decide now (agent):** drop DY4 in a tier-3 clean-up (it is an adopted input) and fix the −$0.56T label. |

### C5. Items dossiers sent the settlement

| # | Item | Finding | Proposed treatment |
| --- | --- | --- | --- |
| 25 | Rebuild the financing screens in `models/tools/financing-protection/` (C; Known gaps, housing) | The screens predate HOU-4D and the health booking. | **Decide now (agent):** step 4 rebuilds `packages.py` and `screen.py` on the settlement's package, or retires them. |
| 26 | One reading of record for the debt guardrail (new) | The budget model passes the guardrail; the long-term model's DEC scenario does not (A1). | **Decide now (agent):** name the budget model as the reading of record, and bring the long-term model into line in the item 20 clean-up. |
| 27 | Housing's FY2040 and FY2041 maturity gaps, and HOU-2D's revenue row (C; `DEC-2026-11-09-09`, `-10-04`) | Housing is $120.5B in FY2040 (+$55.3B on the plan at booking) and $124.4B in FY2041, as booked. HOU-2D's credits are booked as outlays inside HOU-1 ($16B in FY2040). HOU-4.03, the 2040s route, is not booked: about $60B a year once fully enrolled. | **Working assumption:** as booked. Its own revenue row is a tier-3 presentation change (**leave open**). HOU-4.03 is **leave open** unless the batch takes it up. |
| 28 | The education fund going negative in 2035 at 1.4 points (C; K) | Confirmed on the current model: −$254B in FY2040. 1.7 points keeps it solvent; the corridor case adds $45B to the FY2040 gap. | **Decide now, fork:** the fund's rate (1.4 or about 1.7 points) or more general-fund support. Each is priced in step 2. |
| 29 | R1's child benefit after its window, the Byrd rule (C; K) | FAM-1 is $2,445.6B over FY2040-49 (not $2.3T). All of R1's rows come to about $3.47T. | **Decide now (agent):** report it on R1's whole rail. Financing it in the out-years is part of item 1. The Byrd-rule vehicle is a **leave open** item for the 2029 drafting. |
| 30 | Transportation's fuel-tax path (C; `DEC-2026-11-10-14`) | Indexing alone is about +$190B in FY2032-36. Two-cent steps are +$63B, and three pauses +$53B. | **Leave open,** as decided ("revisit later"). Step 2 lists it as a menu item. |
| 31 | Both delivery contingencies (In motion 4(d)) | Memo 10's contingency sits inside CAP-7S and CAP-7: $43.2B plus $35.3B on the booking's ramp, $78.5B in all (the dossier says $72.9B). The $100B line is separate. FY2040 exposure is $18.7B. | **Decide now (agent):** write the two lanes down. Whether to keep both is a money choice for the batch (**fork**, small). |
| 32 | CRT-P1's reading (a) or (b) (In motion 4(d)) | (a) is booked. (b) is −$2.5B over the decade (range −$6.3B to +$0.4B) and −$0.3B in FY2040. | **Decide now, small fork:** recommend (a) until the court is specified, because the range straddles the booking. |
| 33 | #404's CAP-7 residual, options A to C (In motion 4(d); B) | $7.0B and $20.8B. B is +$24.1B over the decade and +$2.7B in FY2040; C is +$27.8B and +$2.8B. The allocation fits inside the booking either way. | **Decide now, small fork:** recommend A (no change), because part G's allocation fits with headroom. |
| 34 | Whether DEM-17.02 sits above IMLS's baseline (In motion 4(d)) | Plausibly overstated by about $2.1B and $0.25B. | **Decide now (agent):** read CBO's nondefense baseline for IMLS in the fix step. |
| 35 | The IMM-1 rebooking for memo 9 part 2 (In motion 4(d)) | About −$4.3B over FY2036-39 and −$0.83B in FY2040. Tier 3, with a DEC row. | **The lead's choice** (Espen, November 20, about 07:47 UTC), so not in the batch. |
| 36 | CAP-7P against the SSA trust-fund reclassification (In motion 4(d)) | Confirmed: the general-fund gap is understated by about $1.0-1.2B over FY2030-33, with no effect on FY2040. | **Decide now (agent):** re-lay the reclassification on CAP-7P's pace in the fix step. |
| 37 | LAB-18 and AI-4's wage-insurance part (In motion 4(c)) | Up to $3.35B in FY2040 and $22B over the decade. | **Leave open** until the AI topic re-scopes AI-4, and show it as a known overlap. |
| 38 | Work's recommended set and the employer-financed unemployment benefits (B) | Booked at $227.0B and $31.9B. The UI benefits, matched by employers' state taxes, are about $42B a year (range $25-66B), against the memo's $15-25B. They are outside the federal budget. | **Leave open** (outside the federal budget). Report the corrected size in stage G's report. |
| 39 | Democratic renewal's bottom-up capacity need against the booking (B) | $54.8B and $249.5B against $98.0B and $279.2B: the item 31 contingency. | Treated with item 31. |
| 40 | The Article I immigration court, $3-10B, unbooked (B) | It is inside CRT-P1 (part B3). | **Done:** not to be added. Fix the board's and `3-design.md`'s wording. |
| 41 | Rural Development's rebuild (B) | Costed once in HOU-14.01, at $0.35B a year, for housing's loans alone. Four other flagships use its front doors and pay nothing. | **Working assumption:** add about $0.1-0.2B a year of front-door staff in the fix step, or **study** it in implementation. It is too small to matter for the batch. |
| 42 | Medicare "Part E" (D15; board directions) | It would reopen the 2035 endpoint, which `DEC-2026-11-15-04` settles for stage G. | **Leave open:** outside stage G. |
| 43 | C3A's compliance payments (part B3) | They vanish if suppliers comply. | **Working assumption,** with a without-C3A line in the risk table. |

## Part D. Errors found, for a fix step

None is fixed here. "Size" is the effect on the gap if fixed: + raises it, − lowers it. Items 1 to 4 change model code or adopted inputs (tier 3 where they touch `models/data/inputs/`). Items 5 to 12 are text.

1. **H1a's FY2030-35 revenue is counted twice.**
   - *Where:* the ledger row H1a books it on the general fund from FY2030 (`models/data/inputs/ledger-revenue.csv` line 3). The budget model books it again on Medicare's HI fund for FY2030-35 (`models/tools/recovery-budget/model.py` lines 256-259, the line "HI H1a and Part A HLT-6 share"; HI's credit is set in `models/tools/funds-model.py` lines 200-222).
   - *Size:* the HI line is $41.3B in FY2030, rising to $47.5B in FY2034, plus $12.3B in FY2035: **$234B in all.** The audit lines carry H1a's ledger row at nearly the same amounts ($41.4B to $48.0B, and $49.8B in FY2035).
   - *What it means:* the general-fund reading strips the HI line out (`fund_primary`, line 285), so the gap counts H1a once. But `DEC-2026-11-16-02` "restores H1a's early years to Medicare's HI fund", so those years belong to HI, not the general fund. Whichever fund keeps the money, the unified reading counts $234B of revenue twice, so **the unified deficit and debt are understated** by about that much, plus its interest, through FY2035 and after. If HI keeps the early years, as the decision says, the general-fund gap is also understated, by about **+$234B over FY2030-39**. FY2040 is unaffected.
   - *Fix:* book H1a once. HLT-6's Part A share shows the pattern to follow: its ledger row books only the general-fund share (`funds-model.py` line 217).
2. **The household test is not run on the package the gap books.**
   - *Where:* scenario Q-H7 (`models/data/inputs/scenarios.json`, the `incidence` block) builds on Q, the "decided package", which includes C19b and C20. The budget model's case `mixed` skips C19b and C20 (`model.py` line 236). No incidence row carries the "New indexed income contributions" (`models/data/inputs/incidence-rows.csv`; `model.py` `tax_yield`, lines 138-142). `mixed` also books the education fund (EDU-9B) at 1.4 points (`model.py` `edu_fund`; the line "EDU replacement", $1,462B of net receipts over FY2030-39), but Q-H7 carries neither its contribution (incidence row EDUP, $2.27T, all on workers) nor its benefits (EDUB, $0.63T).
   - *Size:* D3 charges households for C19b ($0.163T) and C20 ($0.67T), which the gap doesn't book. It leaves out the 4 points above $100K/$200K ($1.41T) and the 2 points above $20K/$40K ($0.50T), which the gap does book. Net of those, D3 leaves out about $1.08T of income contributions over the decade, most of it on Q4 and Q5, and the education fund's net charge on workers (EDUP less EDUB, about $1.6T on D3's keys). C19b also overlaps HX after the exclusion ends (`results.md` section 8 says the settlement must take that overlap out). The effect on Q4's +$8,171 is not sized here. Q-EDU's −$1,294 (against Q's −$90) does not size the fund alone, because Q-EDU differs from Q in two ways at once: it adds EDU-9B and drops C19b and C20. The $1,204 difference nets the fund against dropping those rows, so the fund's own effect on Q4 is larger than $1,200, and the income contributions push the same way. So **Q4's sign is in doubt**, not only its size.
   - *Fix:* align Q-H7 with `mixed`: drop C19b and C20; add EDUP and EDUB; add incidence rows for both income contributions. Then rerun D3 and `intervals.py`, and report beside the take-home test. Tier 3 where it touches `scenarios.json` or `incidence-rows.csv`. No effect on the gap.
3. **GX haircuts H1b's folded wage half.**
   - *Where:* `ledger-revenue.csv` line 15 (GX: 15% of G11, G6, G9 and all of H1b), with HCH taking H1b's wage half back from FY2035.
   - *Size:* **−$6.5B in FY2040 and about −$28B over FY2030-39**, if GX is narrowed to H1b's remaining half. This is a judgment call: HCU's own 20% allowance covers the folded half.
4. **The long-term model carries the untrimmed capacity, and DY4 twice.**
   - *Where:* `fiscal-model.py` DEC reads the ledger's CAP-7S ($560B), CAP-7 ($456B) and AI-4 ($200B) untrimmed, $718.8B more than the gap model ($638.8B of capacity and $80B of AI-4), and adds `ledger-dynamic.csv` line 5 (DY4), which overlaps LAB-1.
   - *Size:* **no effect on the gap.** It moves the long-term model's DEC debt path (debt 194.3% of GDP in FY2056, against the budget model's 161.9%) and DEC-DYN by DY4's $70B over the decade (about $14.7B in FY2040). The DEC-DYN label's "−$0.56T" is stale (`scenarios.json` line 91); the ledger sum is about −$0.33T.
5. **Care's health cost file still reads as booked on the superseded path.**
   - *Where:* `dossiers/care/6-cost.md` line 3 ("booked in the budget model"), part 5 (line 166: HLT-7 at $26,007B and $5,040.3B, against the booked $18,938B and $3,532.1B; the plan-wide gap at $4,240.4B) and parts 1, 4 and 6. Also `dossiers/care/6bcd-cost.md`: the plan-wide gap at $4,240.4B, and the joint-failure figure (about +$650B), which uses the 50% state share. `ledger-bills.csv` line 8 still cites `dossiers/care/6-cost.md` as HLT-7's source.
   - *Size:* 0 on the gap. A reader can take −$7,069B and −$1,508B of superseded difference as current.
   - *Fix:* a superseded banner pointing to `health-cost-review.md` and `health_booking.py`, and re-point the ledger's HLT-7 source (tier 3, an input file).
6. **The secure floor's "booked basis" is stale.**
   - *Where:* `dossiers/secure-floor/6-cost.md` line 10 and part 1 (FAM-1 at $1,900B and $214.7B "as committed at `34faa21`"; table line 149). The model books $1,947B and $220.3B. The plan-wide gap quotes are $4,184.7B to $4,256.6B.
   - *Size:* 0 on the gap; +$47B and +$5.6B of drift in the text.
7. **Immigration's cost file is stale in two places.**
   - *Where:* `dossiers/immigration/6-cost.md` describes E-Verify's funds line as unbooked (part 6), but `funds-ss-provisions.csv` books it. It also states the plan's FY2040 position on the pre-booking IMM-1 basis (−$140B, "net change +$289B and +$41.2B"). And it calls the Article I court democratic renewal's, "unscored", where CRT-P1 now carries it.
   - *Size:* 0.
8. **Plan-wide gap quotes are stale in every flagship cost file.**
   - *Where:* housing ($50.8B), transportation ($602.7B; share 8.9%, now 8.7%), work ($602.7B and $3,773B), clean power ($4,245.4B and $4,164.0B), immigration ($4,184.7B to $4,245.4B), care and the secure floor (above).
   - *Size:* 0. Each says the figure moves. Refresh at each file's next touch, or replace each with a pointer to this file.
9. **Work's part 8 quotes the pre-booking result.** `dossiers/work/6-cost.md` line 299: "about $613.4 billion short", against the booked $614.0B (part 9). The board flagged it. Size 0.
10. **Democratic renewal's contingency and window figures.**
    - `6-cost.md` line 38 says the $5B FY2029 advance is "netted in FY2030", but the table is not netted. Its $503.2B over FY2030-39 is $498.2B on the model's window.
    - Lines 96, 200 and 203, and `7-validation.md` line 139, quote memo 10's contingency as $72.9B (about $173B with the $100B line). On the booking's ramp, which line 90 says stage G should use, it is $78.5B (about $178.5B).
    - `models/tools/budget/note-cap7-sizes.md` line 15's "$98.0B (FY2030-35), plus the $5B shift" reads as $103B. It is $98.0B lifetime, of which $5B falls in FY2029.
    - `3-design.md` and the board call the Article I court "$3-10B, unbooked" (part B3).
    - Size 0 on the gap; +$5.6B in reported unclaimed money.
11. **Housing typo.** `dossiers/home/6-cost.md` line 100: "$22 billion in FY2039" should read FY2040 (the table at line 49). Size 0.
12. **Capacity tooling text.** `models/tools/capacity-funding.py`, its generated `legacy/index/capacity-funding-model.md` and `models/data/inputs/capacity-funding.csv`'s note still state "Full $560B on enactment", against the booked $98.0B. The ledger notes for CAP-7S and CAP-7 still say $0.60T. Size 0.

**Also stale, outside these files:** `checkpoint-financing.md`'s figures ($603B, $3,773B, $852B, "83%, 2080") are as of #402. This audit restates them and leaves the checkpoint as the record of what stage E settled. `dossiers/README.md`'s row for the checkpoint still says "first draft" (the board's small items), and it has no row for this folder yet.

## Part E. A proposed plan for the rest of stage G

This follows Espen's stage G method (board, In motion item 3): draft on the recommendations, mark new forks provisional, bring Espen one decision batch, then revise for the answers. Tier-3 PRs wait for Espen's label.

| Step | What | Tier | Output |
| --- | --- | --- | --- |
| **G2. Fix step** | Part D's items 1 to 4 (model and inputs; tier 3, `needs-espen`, in one PR with the reasons) and items 5 to 12 (text, tier 1, a separate PR). Part C's agent items 16, 34 and 36. A Standard session can do the text; items 1 and 2 need a Most capable session or a careful Standard one with a written spec. | Most capable for items 1-2; Standard for the rest | The gap restated after the fixes, likely about +$234B over the decade from item 1 and nothing in FY2040 |
| **G3. The household test on the booked package** | Part C, item 8: rerun D3 and its intervals on `mixed`'s package, then on each option item 7 prices. It can run alongside G2's text PR. | Standard, checked by the lead | D3 by quintile on the booked package and on each option |
| **G4. The settlement draft** | Part C, items 1, 2, 4, 7, 9, 11, 13 and 28. A recommended package that closes FY2040 and every later year on the general fund, taking health's share from the top-end and corporate rows first. It is shown with and without D2 and HS2, on the take-home test and D3, with the cap on the stack. Alternatives at each fork. Rebuild the financing screens (item 25). | **Most capable** | `2-settlement.md` and decision memos G1 to Gn, drafted on the recommendations and marked provisional |
| **G5. Milestone review** | An adversarial review of G4: weak evidence, optimistic yields, missing populations, cheaper alternatives. | Most capable (the standing reviewer or a fresh one) | Review PR and fixes |
| **G6. Espen's decision batch** | One interactive sheet with every fork in it, each decided on its own. | Lead | Espen's answers, recorded as `DEC-` rows (tier 3) |
| **G7. Revise and book** | Revise for the answers; book the package (tier 3); restate the gap, D3, the take-home test and Social Security; close stage G. | Most capable for the booking; Light for regenerating outputs | The booked settlement and stage G's close |

**The real forks for Espen's one batch** (each provisional until answered):
1. **Which flagships give way, and by how much**, for health's $532B and the rest of the plan's $84B (item 1). This is the settlement itself.
2. **The 2 points above $20K/$40K:** drop, or fold into the health contribution (item 7).
3. **The cap on the capital-income stack** (item 11).
4. **D2 and the wealth tax:** whether the package balances to the gap with D2 and HS2 counted, or holds a backstop for either failing (items 4 and 13).
5. **Health's early surplus:** a reserve for the plan's fund, or counted against the rest of the plan's decade gap (item 2).
6. **The education fund:** its rate (1.4 or about 1.7 points) or more general-fund support (item 28).
7. **Small forks, recommended as drafted:** CRT-P1's reading (a) (item 32); #404's option A (item 33); and keeping both delivery contingencies with written lanes (item 31).

**What the batch does not reopen:** health comes first; the top-end and corporate rows go first; report, don't gate; every booked flagship design. A fork that would reopen a booked design, such as a cut to a flagship's benefit, goes into the batch as a choice about money under `DEC-2026-11-15-04` ("We can downsize other expenditures in project 2050 plans in the financing settlement"), with its consequences stated.

**Sequencing:** G2's tier-3 fixes and G3 run in parallel, under the three-session limit. G4 starts on G2's restated gap. Steps G4 to G7 are about four to six sessions, inside the plan's three to five for stage G once this audit and the fix step are counted.

## Part F. The figures after step G2 (#467)

Step G2 fixed part D's items 1, 2 and 4 in the model and its inputs (#467). G4 starts from these figures, not from part A's. Case `mixed`, nominal $B. A positive gap is a shortfall. Part D's items 5 to 12, the text ones, are fixed in #468 and change no figure.

**The gap, restated**

| | Part A (before G2) | After G2 |
| --- | --- | --- |
| General-fund gap, FY2040 | 615.6 | **615.6** |
| General-fund gap, FY2030-39 | 3,762.5 | **3,998.5** |
| General-fund gap, FY2045 / FY2050 / FY2056 | 676.3 / 824.6 / 1,158.3 | 676.4 / 824.7 / 1,158.5 |
| Without D2, FY2040 / FY2030-39 | 865.0 / 4,106.7 | 865.0 / about 4,342.7 |
| Health's first call, FY2040 | 532.1 | 532.1 |
| Unified program primary balance, FY2030-39 (a surplus is negative) | −2,368.8 | −2,132.8 |
| Debt, % of GDP, FY2040 (baseline 132.7%) | 126.2% | 126.8% |
| Debt, % of GDP, FY2056 (baseline 180.2%) | 161.9% | 162.5% |
| Downside case, debt FY2056 | 181.0% | 181.7% |
| +1-point rate stress, debt FY2056 (stressed baseline 217.4%) | 196.2% | 197.0% |
| Social Security (depletion; 75-year balance) and Medicare HI (depletion) | 2093; −0.31% of payroll; HI 2038 | unchanged |
| Long-term model, DEC: debt FY2056 | 194.3% | 191.8% |

**What changed and why**

1. **H1a is counted once** (part D, item 1). Its FY2030-34 years, and FY2035's first quarter, are Medicare HI's (`DEC-2026-11-16-02`): $235.8B, held in the funds parameter `hi_h1a_bn`. The ledger row now carries only the general fund's share, from the January 2035 endpoint ($0.256T over FY2030-39). The general-fund gap rises $236.0B over the decade and does not move in FY2040. The unified reading loses the double count, as part A1's caveat said. The budget model's debt guardrail still passes: a margin of 5.9 points of GDP in FY2040 and 17.7 points in FY2056.
2. **D3 runs on the package the gap books** (part D, item 2, and step G3). Scenario Q-H7 drops C19b and C20. It adds the education fund as `mixed` books it (EDUP $1.462T, net of its 12.5% income-tax offset; EDUB $0.302T) and the two indexed income contributions (ICH, 4 points above $100K/$200K, $1.410T; ICB, 2 points above $20K/$40K, $0.496T, on a new measured key, `broad_20k`).

   | Q-H7, $ a household a year, FY2030-39 average (90% sampling interval) | Q1 | Q2 | Q3 | Q4 | Q5 | Top 1% |
   | --- | --- | --- | --- | --- | --- | --- |
   | Before G2 | +14,663 | +13,279 | +12,587 | +8,171 | −56,422 | −867,318 |
   | **On the booked package** | **+14,840 ±152** | **+13,209 ±196** | **+12,070 ±190** | **+6,837 ±172** | −62,271 ±400 | −910,567 ±5,154 |

   - **Q4's sign holds.** Every quintile below the top comes out ahead on average. Taking out C19b and C20 raises Q4 to +$8,464; the education fund then takes it to +$7,445, the 4 points to +$7,213 and the 2 points to +$6,837.
   - With EDUP and EDUB at their older typed amounts ($2.27T and $0.63T), Q4 would be +$6,358.
   - The revenue-mix test is 64% (66% before).
   - **Beside the take-home test** (`intervals.py`, the same CPS), at 2.25%: 88.7% ±0.3 of workers come out ahead without the 2 points above $20K/$40K, and **70.1% ±0.5 with them**, as the gap books them. Retirees and others: 98.6% ±0.1.
   - So about 30% of workers are behind on health's take-home test, while every quintile is ahead on average. That is the evidence for fork 2.
3. **The long-term model carries the adopted trims** (part D, item 4). `fiscal-model.py` applies the capacity and AI trims ($718.8B: CAP-7S to $98.0B, CAP-7 to $279.2B, AI-4 to $120B) in every program scenario. It reads them from the one table the budget model also reads (`CAPACITY_TRIMS`).
   - DY4 is zero: it was the same CBO score that LAB-1 books. The DEC-DYN label now reads about −$0.26T.
   - The long-term DEC debt in FY2056 is 191.8%, against the budget model's 162.5%. That difference is lines the long-term model doesn't carry, so naming one reading of record (part C, item 26) is still G4's.

**Taken up in G4 (#469)**

Each of these items now has its home in [`2-settlement.md`](2-settlement.md):
- **Part D item 3** (GX and H1b's folded half; −$6.5B in FY2040): narrowed in the recommended package (part 2, step 1; part 6, item 1).
- **The payroll convention in D3** (#467's review): `2-settlement.md` puts every payroll row in gross, as households pay it. On the booked package that moves Q4 by −$168, to +$6,669 (part 3; part 6, item 5). Step 7 sets EDUP's incidence row to gross when it books.
- **DEC-CAUT and capacity risk** (#467's review): the risk table names the two delivery contingencies as the cushion (part 5).
- **Part C items 16, 34 and 36:** carried to step 7, small (part 6).
