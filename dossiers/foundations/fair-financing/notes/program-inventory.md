# Program inventory: cost and timing of every flagship and major line, FY2030-56

Role: a list of each flagship's and each major line's cost and timing in the booked budget model, so stage G step 8b (the fiscal path review) can pick candidates to phase in, delay, trigger or right-size. It recommends nothing and cuts nothing. Status: research note, stage G step 8b, November 24, 2026; built by a Standard-tier subagent, checked by the step's author. Every figure below is printed by `models/tools/program_inventory.py`; none is typed by hand.

## How it was built

- **Command:** `python3 models/tools/program_inventory.py` (parts: `--part tables`, `--part hump`, `--part top`; `--json` for the raw figures). Run after `bash models/tools/run-all.sh` has written `build/`. It loads the model as `models/tools/financing-protection/packages.py` does and reads case `mixed` (`models/tools/recovery-budget/model.py`, `build_case('mixed', ...)`), the booked case. It writes nothing under `models/data/inputs/`.
- **Units:** nominal $B, federal fiscal years. A spending line is its audit row's `primary_outlay_change_bn`; a revenue line is `revenue_change_bn`. Names come from `build/ledger.json` and `models/data/inputs/ledger-bills.csv`, with short names added in the script.
- **The gap this note is about:** the model's `agenda_gf_primary_bn`, the general-fund shortfall: FY2035 46.6, FY2036 276.8, FY2037 272.1, FY2038 258.8, FY2039 192.5, FY2040 -6.0 (table in part 6).
- **Cut-offs:** spending lines of at least $5B in FY2040 or in any of FY2036-39; revenue lines of at least $20B (either sign) in FY2040. CAP-7S and CAP-7P are added because the brief names them; both are below the cut.
- **Start, full, term (rules in the script's docstring):** *start* = the first FY a line is at least $0.5B. *Full* = the first FY after which the line's growth stays within 2 points of GDP growth, so a line that keeps outgrowing the economy (Social Security's package, the education fund) shows a late year or FY2056. *Term*: "permanent" if it is still at least $0.5B in FY2056; "ends after FYxxxx" if not; "runs down" if it stays but falls under a quarter of its peak share of GDP.
- **Gross, not net.** Health's single plan (HLT-7) is booked as gross spending of about $3 trillion in FY2036; the money it replaces comes in as the health financing lines in part 2 (HEC, HX, HCU and the rest). Read health's cost as part 6's "Health, net" table, not as HLT-7 alone. Likewise (F) marks lines paid by a dedicated fund (Social Security, Medicare HI, the education fund, paid leave): they sit in the unified budget but outside the general-fund gap.
- **What is left out.** The "matched dedicated uses" line (equal revenue and outlay, a presentation gross-up) is shown in part 2 only. Lines under the cut are in the group totals (part 4) but not listed. Group assignment follows the ledger's domain and the dossier that books the line; education lines (EDU-1, EDU-3, EDU-5) have no flagship of their own and sit under "Other", though the secure floor dossier cites EDU-3 and EDU-5.

## 1. Spending lines

Lines with at least $5B in any of FY2036-39 or in FY2040, plus CAP-7S and CAP-7P (named in the brief, below the cut). $B, nominal. "Full" is the first FY after which the line's growth stays within 2 points of GDP growth (for a line that ends, the year it stops growing faster). "Term" says whether it is permanent or ends. F = paid by a dedicated fund, outside the general-fund gap.

### Housing

| ID | Line | FY2030 | FY2033 | FY2036 | FY2037 | FY2038 | FY2039 | FY2040 | FY2045 | FY2056 | FY2030-39 | Start | Full | Term |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| HOU-1 | Housing reconciliation title (aid, credits, construction, vouchers, repair) | 36.5 | 63.6 | 75.6 | 78.2 | 82.6 | 92.1 | 80.0 | 92.9 | 128.5 | 688.0 | 2030 | 2039 | permanent |
| housing_extra | Housing stage 2 and other added housing money (model "extras") | 0.0 | 0.0 | 14.4 | 22.4 | 31.0 | 40.2 | 39.5 | 47.5 | 69.8 | 115.0 | 2035 | 2039 | permanent |

### Health (single plan and Medicaid)

| ID | Line | FY2030 | FY2033 | FY2036 | FY2037 | FY2038 | FY2039 | FY2040 | FY2045 | FY2056 | FY2030-39 | Start | Full | Term |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| HLT-7 | Single plan (Medicare for All), gross spending, waves 2031-35 | 0.0 | 961.0 | 3,055.4 | 3,166.9 | 3,288.7 | 3,399.7 | 3,532.1 | 4,557.2 | 7,214.7 | 18,938.0 | 2031 | 2036 | permanent |
| HLT-4 | Medicaid, long-term care, safety net (wave to 2034, then lower) | 37.9 | 72.8 | 18.2 | 18.8 | 19.6 | 20.3 | 21.1 | 25.9 | 39.2 | 414.0 | 2030 | 2032 | permanent but runs down to 23% of its peak share |

### Care parts B-D (long-term care, child care, care workforce)

| ID | Line | FY2030 | FY2033 | FY2036 | FY2037 | FY2038 | FY2039 | FY2040 | FY2045 | FY2056 | FY2030-39 | Start | Full | Term |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| HLT-9 | Long-term care in the single plan, from 2035 | 0.0 | 0.0 | 309.1 | 372.7 | 402.4 | 422.7 | 444.1 | 577.1 | 937.3 | 1,697.0 | 2035 | 2038 | permanent |
| FAM-2 | Child care and universal pre-K (with educators' pay) | 0.0 | 137.8 | 195.0 | 210.6 | 220.8 | 231.6 | 242.8 | 291.8 | 429.0 | 1,484.0 | 2031 | 2037 | permanent |
| HLT-10 | Care wage floor in the plan's rates, from 2035 | 0.0 | 0.0 | 39.5 | 45.1 | 48.4 | 51.0 | 53.9 | 70.0 | 113.7 | 210.0 | 2035 | 2038 | permanent |
| HLT-11 | Nursing home staffing standard | 0.0 | 1.5 | 6.1 | 6.3 | 6.5 | 6.7 | 6.9 | 8.5 | 12.8 | 36.0 | 2031 | 2036 | permanent |

### Secure floor

| ID | Line | FY2030 | FY2033 | FY2036 | FY2037 | FY2038 | FY2039 | FY2040 | FY2045 | FY2056 | FY2030-39 | Start | Full | Term |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| FAM-1 | Monthly child benefit | 173.3 | 188.1 | 201.1 | 205.8 | 210.5 | 215.3 | 220.3 | 246.8 | 317.0 | 1,947.0 | 2030 | 2030 | permanent |
| LEAVE (F) | Paid family and medical leave (fund) | 3.0 | 156.2 | 175.9 | 182.3 | 188.9 | 195.8 | 202.9 | 242.1 | 350.4 | 1,426.4 | 2030 | 2033 | permanent |
| SS pkg (F) | Social Security package (fund) | 0.9 | 13.6 | 25.1 | 29.5 | 36.0 | 41.1 | 46.5 | 74.0 | 157.7 | 197.5 | 2030 | 2056 | permanent |
| INC-2 | SNAP cuts repealed | 20.5 | 22.1 | 23.8 | 24.4 | 25.0 | 25.6 | 26.3 | 29.4 | 37.8 | 230.0 | 2030 | 2030 | permanent |
| INC-1 | EITC for workers without children | 0.0 | 15.5 | 16.4 | 16.7 | 17.1 | 17.4 | 17.8 | 19.9 | 25.6 | 145.0 | 2031 | 2031 | permanent |
| INC-2B | SNAP earned-income deduction | 12.0 | 13.2 | 14.4 | 14.8 | 15.2 | 15.7 | 16.2 | 18.1 | 23.3 | 138.0 | 2030 | 2030 | permanent |
| LAB-10 | Participation help, paid on-ramps (LAB-10) | 2.4 | 10.8 | 12.1 | 12.5 | 13.0 | 13.5 | 14.0 | 16.8 | 24.7 | 100.0 | 2030 | 2033 | permanent |
| INC-3 | SSI asset limits, territories | 1.7 | 4.4 | 4.9 | 5.0 | 5.2 | 5.4 | 5.6 | 6.2 | 8.0 | 43.0 | 2030 | 2033 | permanent |

### Immigration

| ID | Line | FY2030 | FY2033 | FY2036 | FY2037 | FY2038 | FY2039 | FY2040 | FY2045 | FY2056 | FY2030-39 | Start | Full | Term |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| IMM-1 | Immigration (status, courts, enforcement, USCIS) | 4.3 | 15.5 | 18.6 | 21.1 | 23.2 | 25.0 | 26.2 | 31.5 | 46.4 | 169.0 | 2030 | 2039 | permanent |

### Clean power

| ID | Line | FY2030 | FY2033 | FY2036 | FY2037 | FY2038 | FY2039 | FY2040 | FY2045 | FY2056 | FY2030-39 | Start | Full | Term |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| CLI-1 | Clean-energy credits restored | 84.5 | 95.7 | 50.8 | 48.6 | 71.6 | 72.8 | 55.9 | 77.2 | 77.5 | 756.6 | 2030 | 2042 | permanent |
| CLI-5 | Thriving Economy add-ons (credits, LIHEAP/WAP, minerals) | 11.5 | 30.1 | 26.8 | 28.8 | 35.0 | 35.8 | -0.2 | 6.8 | 11.9 | 271.9 | 2030 | 2047 | permanent but runs down to 17% of its peak share |
| CLI-9 | Clean-industry contracts | 2.8 | 8.3 | 13.7 | 15.5 | 17.2 | 18.9 | 20.5 | 0.0 | 0.0 | 109.5 | 2030 | 2041 | ends after FY2041 |
| CLI-7K | Disaster capital pieces | 5.5 | 11.7 | 12.4 | 12.7 | 13.0 | 13.3 | 0.0 | 0.0 | 0.0 | 112.5 | 2030 | 2032 | ends after FY2039 |
| CLI-10 | Second grid tranche, builder of last resort | 0.0 | 3.0 | 9.0 | 10.0 | 11.0 | 13.0 | 0.0 | 0.0 | 0.0 | 60.0 | 2033 | 2039 | ends after FY2039 |
| CLI-5W | Low-income heat-pump retrofits | 0.0 | 8.9 | 9.5 | 9.7 | 10.0 | 10.2 | 0.0 | 0.0 | 0.0 | 84.0 | 2031 | 2031 | ends after FY2039 |
| CLI-7 | Disaster permanent pieces | 3.8 | 8.1 | 8.6 | 8.8 | 9.0 | 9.2 | 9.4 | 10.5 | 13.3 | 78.1 | 2030 | 2032 | permanent |
| CLI-5H | Automatic energy bill credit (from FY2040) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 9.9 | 11.1 | 14.2 | 0.0 | 2040 | 2040 | permanent |

### Work

| ID | Line | FY2030 | FY2033 | FY2036 | FY2037 | FY2038 | FY2039 | FY2040 | FY2045 | FY2056 | FY2030-39 | Start | Full | Term |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| AI-4 | AI and work: wage insurance, training | 0.0 | 22.7 | 25.4 | 26.4 | 27.4 | 28.4 | 29.5 | 35.4 | 52.1 | 200.0 | 2031 | 2033 | permanent |
| LAB-11 | Unemployment insurance on the general fund | 0.9 | 6.0 | 6.7 | 7.0 | 7.2 | 7.5 | 7.8 | 9.3 | 13.7 | 59.0 | 2030 | 2032 | permanent |
| LAB-9 | National service | 1.1 | 4.7 | 6.2 | 6.3 | 6.5 | 6.6 | 6.7 | 8.1 | 11.9 | 49.0 | 2030 | 2034 | permanent |
| LAB-1 | Labor bill (PRO Act core, wage floor, enforcement) | 0.3 | 2.3 | 4.6 | 4.9 | 5.1 | 5.3 | 5.5 | 6.6 | 9.7 | 32.0 | 2031 | 2037 | permanent |

### Democratic renewal

| ID | Line | FY2030 | FY2033 | FY2036 | FY2037 | FY2038 | FY2039 | FY2040 | FY2045 | FY2056 | FY2030-39 | Start | Full | Term |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| CAP-8 | Civil service and congressional capacity | 1.8 | 3.9 | 4.4 | 4.6 | 4.7 | 4.9 | 5.1 | 6.1 | 9.0 | 40.0 | 2030 | 2031 | permanent |

### Transportation

| ID | Line | FY2030 | FY2033 | FY2036 | FY2037 | FY2038 | FY2039 | FY2040 | FY2045 | FY2056 | FY2030-39 | Start | Full | Term |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| MOV-31 | Moving America Act of 2031 | 0.0 | 24.0 | 26.8 | 49.0 | 41.6 | 33.8 | 29.0 | 14.0 | 19.3 | 249.0 | 2032 | 2037 | permanent but runs down to 20% of its peak share |
| MOV-30 | Moving America 2030 reconciliation act | 16.7 | 0.0 | 40.8 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 91.0 | 2030 | 2036 | ends after FY2036 |

### Capacity (CAP-7, 7S)

| ID | Line | FY2030 | FY2033 | FY2036 | FY2037 | FY2038 | FY2039 | FY2040 | FY2045 | FY2056 | FY2030-39 | Start | Full | Term |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| CAP-7 | Sustained agency capacity (about 0.12% of GDP) | 14.0 | 46.9 | 52.4 | 54.4 | 56.4 | 58.6 | 60.8 | 73.0 | 107.3 | 456.0 | 2030 | 2032 | permanent |
| CAP-7S | Agency rebuild surge | 65.3 | 112.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 560.0 | 2030 | 2032 | ends after FY2035; below the cut |
| CAP-7P | CAP-7 hiring-pace timing | -3.4 | -2.3 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | -17.0 | - | - | n/a; below the cut |

### Other (education, defense, AI, development, veterans, misc.)

| ID | Line | FY2030 | FY2033 | FY2036 | FY2037 | FY2038 | FY2039 | FY2040 | FY2045 | FY2056 | FY2030-39 | Start | Full | Term |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| EDU-1 | K-12 and special education formulas | 10.1 | 33.9 | 37.9 | 39.4 | 40.8 | 42.4 | 44.0 | 52.8 | 77.7 | 330.0 | 2030 | 2032 | permanent |
| EDU fund (F) | Education fund, benefits net of current law (fund) | 19.7 | 31.7 | 37.0 | 38.2 | 39.5 | 41.0 | 42.6 | 53.4 | 95.3 | 302.3 | 2030 | 2056 | permanent |
| EDU-5 | Pell and student-loan fixes | 28.9 | 30.9 | 33.0 | 33.8 | 34.6 | 35.3 | 36.2 | 40.5 | 52.0 | 320.0 | 2030 | 2030 | permanent |
| EDU-3 | Free school meals, Summer EBT | 24.4 | 26.1 | 27.9 | 28.5 | 29.2 | 29.8 | 30.5 | 34.2 | 43.9 | 270.0 | 2030 | 2030 | permanent |
| DEV-P | Permanent development programs | 3.0 | 9.8 | 10.4 | 10.7 | 10.9 | 11.2 | 11.4 | 12.8 | 16.5 | 92.0 | 2030 | 2032 | permanent |
| NSC-10 | Veterans health and capacity | 2.1 | 7.2 | 8.0 | 8.3 | 8.7 | 9.0 | 9.3 | 11.2 | 16.5 | 70.0 | 2030 | 2032 | permanent |

## 2. Revenue lines of at least $20B in FY2040 (either sign)

Positive = more receipts; negative = receipts lost or an offset. "Middle class" is a reading of each line's definition, not a model output; the ledger's `reaches_middle` flag is quoted where the line has an ID in it.

| ID | Line | FY2030 | FY2033 | FY2036 | FY2037 | FY2038 | FY2039 | FY2040 | FY2045 | FY2056 | FY2030-39 | Start | Full | Falls on the middle class? |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| HEC | Employer health contribution (19.3% of pay) | 0.0 | 453.7 | 1,533.0 | 1,626.5 | 1,726.5 | 1,832.6 | 1,945.3 | 2,377.2 | 3,479.7 | 9,678.0 | 2031 | 2040 | YES, payroll: employer contribution, 19.3% of pay between $20,000 and the wage base (wages bear part of it) |
| HX | End of employer tax exclusion | 0.0 | 221.0 | 775.2 | 818.7 | 865.0 | 914.0 | 965.8 | 1,255.1 | 2,038.5 | 4,835.0 | 2031 | 2036 | YES: employer premium exclusion ends, on the full pass-through convention |
| SS pkg (F) | Social Security package receipts (fund) | 0.0 | 532.1 | 605.3 | 647.4 | 688.4 | 731.4 | 778.4 | 1,050.7 | 1,594.1 | 5,323.2 | 2031 | 2046 | Mostly high earners (wage-base lift, high-base package); a payroll piece reaches workers; check SS dossier |
| HCU | Household health contribution (HCU) | 0.0 | 329.2 | 664.3 | 689.3 | 715.3 | 742.2 | 770.3 | 950.6 | 1,475.5 | 4,606.0 | 2031 | 2036 | YES (HCU: 2.25% of AGI, exempt to 138% of poverty, phased to 250%; surcharge above $205,400) |
| HEX | Tax on former premiums (offsets HX) | 0.0 | -141.7 | -478.9 | -508.1 | -539.3 | -572.4 | -607.7 | -742.6 | -1,152.6 | -3,023.0 | 2031 | 2040 | YES (reduces HX; same households) |
| S06 | S06: HCU base rate raised above 2.25% from FY2035 | 0.0 | 0.0 | 299.4 | 310.7 | 322.4 | 334.6 | 347.2 | 428.5 | 665.1 | 1,533.9 | 2035 | 2036 | YES: raises HCU's base rate (a step in FY2036) |
| HCW | Worker 1.45% HI tax folded in | 0.0 | 0.0 | -279.0 | -290.2 | -301.8 | -313.8 | -326.4 | -391.4 | -572.9 | -1,386.0 | 2035 | 2036 | YES, a cut: the worker 1.45% HI tax ends, replaced inside HCU |
| EDU fund (F) | Education payroll contribution (EDUP), net of its offset (fund) | 0.0 | 131.5 | 246.6 | 256.5 | 266.7 | 277.4 | 288.5 | 351.0 | 540.4 | 1,723.2 | 2031 | 2035 | YES, payroll: education contribution (EDUP), 1.4 points, all on workers |
| NIC | New indexed income contributions (4 high-income points) | 0.0 | 68.8 | 230.7 | 239.4 | 248.5 | 257.8 | 267.6 | 321.5 | 472.7 | 1,410.4 | 2033 | 2035 | No: high-income points only (broad rate 0) |
| MATCHED | Matched dedicated receipts (gross proxy, equal outlay) | 102.5 | 171.9 | 243.8 | 260.7 | 258.7 | 257.3 | 259.2 | 290.4 | 373.1 | 1,979.8 | 2030 | 2037 | Includes carbon, fuel taxes: reaches households |
| G1 | Corporate rate 28% | 142.3 | 156.8 | 171.7 | 177.7 | 184.1 | 192.9 | 201.4 | 246.7 | 373.8 | 1,650.0 | 2030 | 2030 | Ledger says reaches the middle class: No |
| LEAVE (F) | Paid leave contributions (fund) | 69.5 | 104.9 | 162.4 | 168.3 | 174.4 | 180.8 | 187.4 | 223.5 | 323.5 | 1,286.2 | 2030 | 2036 | YES, payroll: leave contributions on workers and employers |
| G9 | Reverse 2025 tax cuts above $450K | 120.2 | 134.8 | 153.0 | 159.7 | 167.0 | 174.3 | 181.9 | 224.5 | 348.4 | 1,450.0 | 2030 | 2030 | Ledger says reaches the middle class: No |
| HS2 | Annual wealth tax | 103.5 | 115.7 | 129.3 | 134.2 | 139.2 | 144.5 | 149.9 | 185.1 | 287.2 | 1,230.0 | 2030 | 2030 | Ledger says reaches the middle class: No |
| C38 | Legacy revenue row C38 | 40.1 | 88.4 | 96.8 | 100.1 | 103.8 | 108.7 | 113.5 | 139.1 | 210.7 | 890.0 | 2030 | 2031 |  |
| G6 | Capital gains at death | 30.3 | 67.9 | 77.0 | 80.4 | 84.1 | 87.8 | 91.6 | 113.1 | 175.5 | 700.0 | 2030 | 2031 | Ledger says reaches the middle class: No |
| G11 | Billionaire mark-to-market | 53.9 | 60.4 | 68.6 | 71.6 | 74.8 | 78.2 | 81.5 | 100.6 | 156.2 | 650.0 | 2030 | 2030 | Ledger says reaches the middle class: No |
| C18 | Legacy revenue row C18 | 51.4 | 57.6 | 65.4 | 68.3 | 71.4 | 74.5 | 77.8 | 96.0 | 149.0 | 620.0 | 2030 | 2030 |  |
| HS4 | Corporate rate 30%, expensing repealed | 48.3 | 54.0 | 60.3 | 62.6 | 65.0 | 67.4 | 70.0 | 85.7 | 129.9 | 574.0 | 2030 | 2030 | Ledger says reaches the middle class: No |
| S03 | S03: HCU avoidance allowance | 0.0 | 26.9 | 54.3 | 56.4 | 58.5 | 60.7 | 63.0 | 77.7 | 120.7 | 376.7 | 2031 | 2036 | YES: a yield allowance on HCU (booked as added receipts; the label says allowance, so the sign is worth a check by the step author) |
| H1b | Medicare/investment-income rates 5% above $400K | 41.4 | 46.5 | 52.7 | 55.1 | 57.6 | 60.1 | 62.7 | 77.4 | 120.1 | 500.0 | 2030 | 2030 | Ledger says reaches the middle class: No |
| GX | Overlap and avoidance adjustment (high-income) | -41.0 | -46.0 | -52.2 | -54.5 | -57.0 | -59.5 | -62.1 | -76.6 | -118.9 | -495.0 | 2030 | 2030 | Ledger says reaches the middle class: No |
| HS1 | Financial transactions tax to 0.1% | 41.4 | 46.3 | 51.7 | 53.7 | 55.7 | 57.8 | 60.0 | 76.6 | 120.7 | 492.0 | 2030 | 2043 | Ledger says reaches the middle class: No |
| H1a | Investment-income tax on pass-through income (GF share) | 0.0 | 0.0 | 51.7 | 53.6 | 55.6 | 57.7 | 59.9 | 73.9 | 114.8 | 256.0 | 2035 | 2036 | Ledger says reaches the middle class: No |
| G8 | IRS enforcement yield | 12.1 | 40.6 | 46.1 | 48.1 | 50.3 | 52.5 | 54.8 | 67.6 | 104.9 | 400.0 | 2030 | 2032 | Ledger says reaches the middle class: No |
| HCA | Additional Medicare Tax folded in | 0.0 | 0.0 | -45.7 | -47.5 | -49.4 | -51.4 | -53.5 | -64.1 | -93.8 | -227.0 | 2035 | 2036 | No (top earners; a cut) |
| C39 | Legacy revenue row C39 | 33.2 | 37.2 | 42.2 | 44.1 | 46.1 | 48.1 | 50.2 | 61.9 | 96.1 | 400.0 | 2030 | 2030 |  |
| G7 | Foreign income at full corporate rate | 35.4 | 39.0 | 42.7 | 44.1 | 45.7 | 47.9 | 50.1 | 61.3 | 92.9 | 410.0 | 2030 | 2030 | Ledger says reaches the middle class: No |
| G5 | Buyback tax, corporate minimum | 34.5 | 38.0 | 41.6 | 43.1 | 44.6 | 46.8 | 48.8 | 59.8 | 90.6 | 400.0 | 2030 | 2030 | Ledger says reaches the middle class: No |
| G10 | Financial transactions tax 0.01% | 33.7 | 37.6 | 42.0 | 43.6 | 45.3 | 47.0 | 48.8 | 58.6 | 86.1 | 400.0 | 2030 | 2030 | Ledger says reaches the middle class: No |
| HS3 | Capital gains as ordinary income above $1M | 31.0 | 34.7 | 38.8 | 40.3 | 41.8 | 43.3 | 45.0 | 55.5 | 86.2 | 369.0 | 2030 | 2030 | Ledger says reaches the middle class: No |
| HCH | H1b wage half folded in | 0.0 | 0.0 | -37.5 | -39.0 | -40.4 | -42.0 | -43.5 | -53.7 | -83.4 | -186.0 | 2035 | 2036 | No (high earners; a cut) |
| CX | Income/payroll offset on carbon fees | -11.8 | -25.3 | -39.9 | -43.3 | -42.4 | -41.5 | -42.3 | -50.8 | -74.7 | -306.0 | 2030 | 2037 | Offset on carbon fees, which reach households (see carbon row) |
| C3A | Clean electricity standard payments | 0.0 | 11.6 | 21.1 | 24.5 | 29.4 | 35.0 | 41.5 | 49.9 | 73.4 | 163.0 | 2032 | 2040 | Ledger says reaches the middle class: No |
| S04 | S04: stack cap on the wealth tax | -27.6 | -30.9 | -34.5 | -35.8 | -37.1 | -38.5 | -40.0 | -49.4 | -76.6 | -328.1 | 2030 | 2030 | No (wealth tax) |
| G3 | Top rate 39.6% | 24.9 | 27.9 | 31.6 | 33.0 | 34.5 | 36.1 | 37.6 | 46.4 | 72.1 | 300.0 | 2030 | 2030 | Ledger says reaches the middle class: No |
| IRS allow. | IRS yield allowance (reduces G8) | -7.5 | -25.4 | -28.8 | -30.1 | -31.4 | -32.8 | -34.2 | -42.2 | -65.6 | -250.0 | 2030 | 2032 | No |
| C1T | Carbon transition remainder in GF (from FY2040) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 33.1 | 39.8 | 58.5 | 0.0 | 2040 | 2040 | Ledger says reaches the middle class: No |
| MR6 | Income/payroll offset on new excises | -1.9 | -8.8 | -15.9 | -18.4 | -21.0 | -23.6 | -24.5 | -29.4 | -43.3 | -125.3 | 2030 | 2039 | Offset on excises that reach households |
| C43 | Legacy revenue row C43 | 14.9 | 16.7 | 19.0 | 19.8 | 20.7 | 21.6 | 22.6 | 27.9 | 43.3 | 180.0 | 2030 | 2030 |  |
| C35 | Legacy revenue row C35 | 11.5 | 13.6 | 16.1 | 17.1 | 18.1 | 19.1 | 20.2 | 26.8 | 49.1 | 150.0 | 2030 | 2056 |  |

Carbon fee receipts (REV-C1 plus REV-C2, gross), which sit inside the "matched dedicated receipts" gross-up and are not a line of their own in the audit. Recomputed from the model's carbon table (`u.carbon`, FY2030-39) and its post-2039 rule (GDP growth less 2% a year). Ledger: reaches the middle class, YES (C1, C2). Offset line CX is in the table above.

| FY2030 | FY2033 | FY2036 | FY2037 | FY2038 | FY2039 | FY2040 | FY2045 | FY2056 |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 40.8 | 97.5 | 163.2 | 179.5 | 179.2 | 179.5 | 182.6 | 198.3 | 233.5 |

## 3. Settlement lines that reduce spending (negative outlay of at least $5B in any hump year or FY2040)

These are in the booked case as explicit adjustments; they net against the lines above in each group. Spending lines in section 1 are before them.

| Line | Group | FY2030 | FY2033 | FY2036 | FY2037 | FY2038 | FY2039 | FY2040 | FY2045 | FY2056 |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Settlement S05: The states' long-term care payment at 100% (HLT-9.09) | Care parts B-D (long-term care, child care, care workforce) | 0.0 | 0.0 | -119.6 | -126.1 | -133.1 | -140.4 | -148.1 | -192.5 | -312.6 |
| Settlement S07: Defense flat in real terms from FY2037 (NSC-1A, extended after FY2039) | Other (education, defense, AI, development, veterans, misc.) | 0.0 | 0.0 | 0.0 | -4.1 | -12.0 | -24.3 | -41.9 | -166.0 | -541.5 |
| Settlement S08: Defense restructured, 5% below the flat-real path by FY2033 | Other (education, defense, AI, development, veterans, misc.) | 0.0 | -51.7 | -55.0 | -56.1 | -57.2 | -58.4 | -59.5 | -65.7 | -81.8 |
| Settlement S09: Crop insurance reform (REV-SC3) | Other (education, defense, AI, development, veterans, misc.) | -2.1 | -4.4 | -4.6 | -4.7 | -4.8 | -4.9 | -5.0 | -5.5 | -6.9 |
| Settlement S11: Housing stage 2 (HOU-4D.01) a capped program, not a right, shaped on enrollment | Housing | 0.0 | 0.0 | 0.0 | -6.4 | -13.3 | -20.9 | -18.6 | -22.3 | -32.8 |
| Smaller capacity and AI authorizations | Other (education, defense, AI, development, veterans, misc.) | -59.3 | -119.7 | -30.5 | -31.6 | -32.8 | -34.1 | -35.3 | -42.5 | -62.4 |

## 4. Flagship totals (all audit spending lines mapped to the group, before settlement reductions)

Sums every positive-or-negative outlay line the mapping puts in the group, small lines included; fund lines (F) are kept in the totals and shown separately. $B.

| Group | FY2030 | FY2033 | FY2036 | FY2037 | FY2038 | FY2039 | FY2040 | FY2045 | FY2056 | FY2030-39 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Housing | 36.5 | 63.6 | 90.0 | 100.7 | 113.6 | 132.3 | 119.5 | 140.4 | 198.3 | 803.0 |
| Health (single plan and Medicaid) | 79.8 | 1,071.7 | 3,074.0 | 3,186.2 | 3,308.7 | 3,420.4 | 3,553.7 | 4,583.6 | 7,254.5 | 19,513.0 |
| Care parts B-D (long-term care, child care, care workforce) | 0.0 | 139.2 | 549.7 | 634.7 | 678.1 | 712.1 | 747.7 | 947.3 | 1,492.8 | 3,427.0 |
| Secure floor | 213.9 | 426.4 | 476.5 | 494.0 | 514.0 | 533.0 | 552.7 | 657.1 | 949.0 | 4,252.0 |
| Immigration | 4.3 | 15.5 | 18.6 | 21.1 | 23.2 | 25.0 | 26.2 | 31.5 | 46.4 | 169.0 |
| Clean power | 112.9 | 162.1 | 142.8 | 147.6 | 175.3 | 184.5 | 106.2 | 108.1 | 112.0 | 1,525.8 |
| Work | 3.9 | 42.2 | 50.3 | 52.3 | 54.2 | 56.1 | 58.0 | 69.7 | 102.4 | 402.0 |
| Democratic renewal | 9.9 | 15.6 | 17.4 | 13.1 | 13.5 | 14.0 | 14.3 | 17.1 | 24.6 | 143.0 |
| Transportation | 40.1 | 84.0 | 67.6 | 49.0 | 41.6 | 33.8 | 29.0 | 14.0 | 19.3 | 597.0 |
| Capacity (CAP-7, 7S) | 76.0 | 156.6 | 52.4 | 54.4 | 56.4 | 58.6 | 60.8 | 73.0 | 107.3 | 999.0 |
| Other (education, defense, AI, development, veterans, misc.) | 91.3 | 149.3 | 165.2 | 170.1 | 175.4 | 180.9 | 186.7 | 220.1 | 324.2 | 1,481.4 |


Two cautions on part 2. (a) *Checked by the step's author: the sign is right.* S03 narrows the allowance from 20% to 10% on the base rate, so it adds receipts and lowers the gap by $63.0B in FY2040 (`2-settlement.md` part 2). The subagent's original note: S03 ("HCU's avoidance allowance") is booked by the model as added receipts of $63.0B in FY2040, although its label reads as a cut to yield; the step's author should check its sign against `models/tools/financing-protection/packages.py` before relying on it. (b) The "middle class" column is a reading of each line's definition (and the ledger's `reaches_middle` flag where the line has an ID in the ledger), not a model output. The legacy rows C18, C35, C38, C39 and C43 have no ledger flag; their definitions are in `models/data/inputs/ledger-revenue.csv`.

## 5. Which outcomes each flagship serves, and whether the dossier claims later savings

Outcome IDs are `charter/outcomes.md` (OUT-01 to OUT-12; OUT-12 is transportation's). The "serves" column is the record's own "Moved mainly by" column; the dossier README's cited IDs are added where they differ. "Claim" quotes the dossier, with the path.

| Flagship (lines) | Serves | Claims it saves money later? |
| --- | --- | --- |
| Housing (HOU-1, housing_extra) | OUT-04; also OUT-01, OUT-02 (`charter/outcomes.md`; `dossiers/home/README.md`) | **None claimed.** "No offsetting savings are counted anywhere: not shelter or Medicaid savings from Housing First ... and not lower spending on homelessness programs. That is CBO's practice for savings outside the bill's own accounts, and the cautious choice." (`dossiers/home/6-cost.md`, "Revenue effects", line 91). Public case: "the plan counts no savings" (`dossiers/home/9-public-case.md`, line 98). Denver: "savings elsewhere offset about half the yearly cost per person, $6,876 ... That gives the scale, not the split." (`dossiers/home/6-cost.md`, line 182). |
| Health: single plan and Medicaid (HLT-1, 2, 4, 7) | OUT-03; OUT-01, OUT-02, OUT-08 (`dossiers/care/README.md`) | **A claim about national spending, not about the federal budget.** The public case says "On our estimates, about $500 billion less national health spending a year at full scale" and warns against "It saves money" without "on our estimates" and "national spending"; "the federal budget's cost rises by about $2.7 trillion a year at full scale" (`dossiers/care/9-public-case.md`, line 64). No later federal saving is booked. |
| Care parts B-D (HLT-9, HLT-10, HLT-11, FAM-2) | OUT-03, OUT-08; OUT-01 for child care | **None booked; evidence noted.** "Mothers' added earnings and taxes; lower turnover; less public assistance; quality | not counted ... CBO's conventional scores leave them out; Quebec's evidence puts child care's long-run fiscal recapture at 75-117% of cost [EV-CAR-534], Norway's much less [EV-CAR-544] | Not counted" (`dossiers/care/6bcd-cost.md`, line 80). The public case: "It pays for itself" is a claim not to make (`dossiers/care/9bcd-public-case.md`, line 64). |
| Secure floor (FAM-1, INC-1, INC-2, INC-2B, INC-3, LAB-10, leave, Social Security) | OUT-01, OUT-02, OUT-06, OUT-08 | **None claimed.** "A work response to the child benefit ... not counted"; "Parents' added earnings from paid leave and child care ... $0.15-0.30 trillion with child care ... Not counted" (`dossiers/secure-floor/6-cost.md`, lines 72 and 74). |
| Immigration (IMM-1) | OUT-07; README also cites OUT-01, OUT-03, OUT-06, OUT-09 | **None claimed.** "Legalization's growth effects ... not counted ... never a pay-for" (`dossiers/immigration/6-cost.md`, line 98); legalization "pays for itself" is the claim to avoid (`dossiers/immigration/9-public-case.md`, line 83). E-Verify's general-fund gain "is not a sign that the mandate pays for itself" (`dossiers/immigration/6-cost.md`, line 84). |
| Clean power (CLI-*) | OUT-05 (`charter/outcomes.md`; its README cites no OUT-IDs) | **None claimed** for later budget savings. Its one saving is inside the plan: bill protection "can only shorten" ("Firm, a possible saving", `dossiers/clean-power/6-cost.md`, line 106). |
| Work (LAB-*, AI-4) | OUT-06, OUT-02, OUT-08, OUT-10 | **None claimed.** "Higher wages' tax effects beyond the floor ... not counted" (`dossiers/work/6-cost.md`, line 166). |
| Democratic renewal (CAP-8, DEM, CRT) | OUT-09, OUT-10 | **None for the foundation's own lines.** "no saving is counted" for data-sharing (`dossiers/foundations/democratic-renewal/6-cost.md`, line 70). Its capacity lines do carry a return: the IRS's enforcement yield is revenue row G8, "$400 billion over FY2030-39, $54.8 billion in FY2040" (same file, line 98); G8 is in part 2. |
| Capacity (CAP-7, CAP-7S) | none of its own; it serves every flagship's delivery (OUT-09 for government that delivers) | The G8 yield above is the only return booked against it; CAP-7P is a timing row, "not savings" (`models/tools/democratic_renewal_booking.py` docstring). |
| Transportation (MOV-29 to MOV-31) | OUT-12 (also OUT-05, OUT-11 in `dossiers/agenda/transportation/README.md`) | **None claimed** in its cost section; its stated cost risk is receipts, not outlays (`dossiers/agenda/transportation/6-cost.md`, line 117). |

## 6. The FY2036-39 shape

What the tables below show, in plain words. The general-fund gap goes from $46.6B in FY2035 to $276.8B in FY2036 (a step of $230.2B), eases to $192.5B by FY2039 and is -$6.0B in FY2040. The hump has three parts.

1. **Health's 2035 endpoint arrives in full in FY2036.** The endpoint is January 2035 (`HLT-7` in the ledger), so FY2035 holds about three quarters of a year of the endpoint lines and FY2036 the first full year (my reading of the dates; the tables show the jump, not the cause). Health's step into FY2036 is large on both sides: gross health spending rises by $528.8B and the health financing lines by $248.4B, a net step of about $280B, more than the whole step in the gap. HLT-7 alone rises $420.6B, and the long-term care benefit (HLT-9, starts FY2035) another $119.1B and the care wage floor (HLT-10) $13.4B. Two health savings end at the same time: the Medicare Advantage fix (HLT-6) and the HI fund's matching Part A saving fall to zero in FY2036 ($20.7B and $13.6B less saving), and the Medicare upgrades (HLT-2, $34.2B in FY2035) end.
2. **Health's rate steps are in the revenue side's step too.** HCU's base rate rises from FY2035 (S06, +$32.7B step), the worker's 1.45% tax and the Additional Medicare Tax fold into HCU (HCW -$77.8B step), and the employer lines step up ($173.4B for HEC, $92.4B for HX, less $54.2B for HEX). The financing lines do not keep pace with spending: from FY2036 to FY2039 gross health spending rises $472.2B and the financing lines $465.8B, so health's net stays about $560-595B a year (part 6 table).
3. **Lines still growing faster than the economy in FY2036-39:** long-term care HLT-9 (+36.8%, $113.6B), housing stage 2 (housing_extra, +179% as it ramps to FY2039), the Social Security package (+63.7%), child care FAM-2 (+18.7%), the clean-energy credits CLI-1 (+43.4%; they fall in FY2035 and rise again as the credit schedule turns), clean-industry contracts CLI-9 (+37.4%), the second grid tranche CLI-10 (+44.4%, ends FY2039) and immigration IMM-1 (+34.5%). Clean power's group total rises $41.7B between FY2036 and FY2039, then falls $78.3B in FY2040 when CLI-10, CLI-7K and CLI-5W end (FY2040 less FY2039 in part 4).
4. **Lines that fall away in the window, easing it:** transportation (MOV-30 ends after FY2036; MOV-31 peaks at $49.0B in FY2037), the capacity surge (CAP-7S ends after FY2035) and the 2029-35 reconciliation tranches (MOV-29, HLT-2) are all gone by FY2036. Their drop-offs are in the "fall away" table below and keep the FY2036 gap from being larger.
5. **Why it closes in FY2040:** the tables show the hump ending at FY2039-40 with a gap of -$6.0B (the group table's FY2040 column). The lines that end in FY2039-40 are CLI-5 (to -$0.2B), CLI-10, CLI-7K and CLI-5W; defense falls (settlement S07, part 3) and the tax lines keep growing. This note does not test why the model closes the gap; that is the step's author's to check.

### The general-fund gap, by year ($B; positive = shortfall; the model's `agenda_gf_primary_bn`)

| FY2033 | FY2034 | FY2035 | FY2036 | FY2037 | FY2038 | FY2039 | FY2040 | FY2041 |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| -42.0 | -166.2 | 46.6 | 276.8 | 272.1 | 258.8 | 192.5 | -6.0 | -5.1 |

### Spending lines that step up or grow fastest ($B; non-fund lines first)

Step = FY2036 less FY2035. Growth = FY2039 less FY2036. Ranked by step plus growth, lines with at least $2B of either.

| ID | Line | FY2034 | FY2035 | FY2036 | Step into FY2036 | FY2039 | Growth FY2036-39 | Growth % | FY2040 less FY2039 |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| HLT-7 | Single plan (Medicare for All), gross spending, waves 2031-35 | 1,546.9 | 2,634.8 | 3,055.4 | 420.6 | 3,399.7 | 344.3 | 11.3% | 132.5 |
| HLT-9 | Long-term care in the single plan, from 2035 | 0.0 | 190.0 | 309.1 | 119.1 | 422.7 | 113.6 | 36.8% | 21.3 |
| FAM-2 | Child care and universal pre-K (with educators' pay) | 169.9 | 184.8 | 195.0 | 10.2 | 231.6 | 36.6 | 18.7% | 11.3 |
| housing_extra | Housing stage 2 and other added housing money (model "extras") | 0.0 | 6.9 | 14.4 | 7.5 | 40.2 | 25.8 | 179.3% | -0.7 |
| LEAVE (F) | Paid family and medical leave (fund) | 162.8 | 169.7 | 175.9 | 6.2 | 195.8 | 19.9 | 11.3% | 7.1 |
| HLT-10 | Care wage floor in the plan's rates, from 2035 | 0.0 | 26.0 | 39.5 | 13.4 | 51.0 | 11.6 | 29.3% | 2.8 |
| HLT-6 | Medicare Advantage fix, a saving (to the 2035 endpoint) | -81.4 | -20.7 | 0.0 | 20.7 | 0.0 | 0.0 | nan% | 0.0 |
| SS pkg (F) | Social Security package (fund) | 17.3 | 21.2 | 25.1 | 3.9 | 41.1 | 16.0 | 63.7% | 5.4 |
| CLI-1 | Clean-energy credits restored | 92.9 | 53.5 | 50.8 | -2.7 | 72.8 | 22.0 | 43.4% | -17.0 |
| FAM-1 | Monthly child benefit | 192.4 | 196.7 | 201.1 | 4.4 | 215.3 | 14.2 | 7.1% | 5.0 |
| HOU-1 | Housing reconciliation title (aid, credits, construction, vouchers, repair) | 72.1 | 74.2 | 75.6 | 1.5 | 92.1 | 16.5 | 21.8% | -12.1 |
| HI fund (F) | Medicare HI fund: Part A savings (fund) | -53.7 | -13.6 | 0.0 | 13.6 | 0.0 | 0.0 | nan% | 0.0 |
| CLI-5 | Thriving Economy add-ons (credits, LIHEAP/WAP, minerals) | 32.1 | 25.1 | 26.8 | 1.7 | 35.8 | 9.0 | 33.7% | -36.1 |
| EDU fund (F) | Education fund, benefits net of current law (fund) | 30.8 | 32.7 | 37.0 | 4.3 | 41.0 | 4.0 | 10.8% | 1.6 |
| CAP-7 | Sustained agency capacity (about 0.12% of GDP) | 48.7 | 50.5 | 52.4 | 1.9 | 58.6 | 6.2 | 11.7% | 2.2 |
| MOV-31 | Moving America Act of 2031 | 24.9 | 25.8 | 26.8 | 1.0 | 33.8 | 7.0 | 26.1% | -4.8 |
| IMM-1 | Immigration (status, courts, enforcement, USCIS) | 17.1 | 17.8 | 18.6 | 0.7 | 25.0 | 6.4 | 34.5% | 1.3 |
| CLI-9 | Clean-industry contracts | 10.1 | 11.9 | 13.7 | 1.8 | 18.9 | 5.1 | 37.4% | 1.6 |
| EDU-1 | K-12 and special education formulas | 35.2 | 36.5 | 37.9 | 1.4 | 42.4 | 4.5 | 11.7% | 1.6 |
| CLI-10 | Second grid tranche, builder of last resort | 6.0 | 8.0 | 9.0 | 1.0 | 13.0 | 4.0 | 44.4% | -13.0 |

### Lines that fall away just before or inside the hump (spending that ends)

| ID | Line | FY2033 | FY2034 | FY2035 | FY2036 | FY2039 | FY2040 |
|---|---|---:|---:|---:|---:|---:|---:|
| CAP-7S | Agency rebuild surge | 112.0 | 93.3 | 56.0 | 0.0 | 0.0 | 0.0 |
| HLT-2 | Medicare upgrades until the 2035 endpoint | 113.0 | 133.2 | 34.2 | 0.0 | 0.0 | 0.0 |
| MOV-29 | Moving America 2029 reconciliation act | 60.0 | 55.0 | 31.7 | 0.0 | 0.0 | 0.0 |
| HLT-4 | Medicaid, long-term care, safety net (wave to 2034, then lower) | 72.8 | 71.6 | 30.3 | 18.2 | 20.3 | 21.1 |
| CLI-1 | Clean-energy credits restored | 95.7 | 92.9 | 53.5 | 50.8 | 72.8 | 55.9 |
| CLI-11 | Transition guarantee for workers and places | 2.0 | 2.2 | 1.7 | 1.2 | 0.9 | 0.7 |

### Revenue lines that step up or down into FY2036 ($B)

| Line | FY2034 | FY2035 | FY2036 | Step | FY2039 |
|---|---:|---:|---:|---:|---:|
| Worker 1.45% HI tax folded in | 0.0 | -201.2 | -279.0 | -77.8 | -313.8 |
| Tax on former premiums (offsets HX) | -282.5 | -424.7 | -478.9 | -54.2 | -572.4 |
| Paid leave contributions (fund) | 123.0 | 142.4 | 162.4 | 20.0 | 180.8 |
| Social Security package receipts (fund) | 561.7 | 584.0 | 605.3 | 21.3 | 731.4 |
| S06: HCU base rate raised above 2.25% from FY2035 | 0.0 | 266.7 | 299.4 | 32.7 | 334.6 |
| Household health contribution (HCU) | 412.8 | 591.8 | 664.3 | 72.5 | 742.2 |
| End of employer tax exclusion | 440.5 | 682.8 | 775.2 | 92.4 | 914.0 |
| Employer health contribution (19.3% of pay) | 904.3 | 1,359.7 | 1,533.0 | 173.4 | 1,832.6 |

### What moves the general-fund gap, by group ($B, change in primary deficit, non-fund lines; the fund remainder is by difference)

| Group | FY2035 | FY2036 | FY2037 | FY2038 | FY2039 | FY2040 | Step into FY2036 | Change FY2036-39 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Health spending (HLT-1 to HLT-11, gross) | 2,899.9 | 3,428.7 | 3,610.3 | 3,766.0 | 3,900.9 | 4,058.5 | 528.8 | 472.2 |
| Health financing (HX, HCU, HEC, HEX, HCW, HCA, HCH, HS1-4, H1a, H1b, S03, S06) | -2,621.2 | -2,869.7 | -3,016.3 | -3,171.8 | -3,335.5 | -3,508.0 | -248.4 | -465.8 |
| Capacity (CAP-7, 7S) | 106.5 | 52.4 | 54.4 | 56.4 | 58.6 | 60.8 | -54.1 | 6.2 |
| Other (education, defense, AI, development, veterans, misc.) | -6.9 | 42.4 | 40.0 | 33.7 | 23.2 | 7.4 | 49.3 | -19.2 |
| Other revenue lines (taxes, carbon offsets, IRS) | -955.6 | -994.1 | -1,032.7 | -1,079.4 | -1,132.3 | -1,219.9 | -38.6 | -138.2 |
| Care parts B-D (long-term care, child care, care workforce) | 98.7 | 75.5 | 84.5 | 87.8 | 91.2 | 94.7 | -23.2 | 15.7 |
| Housing | 81.1 | 90.0 | 94.3 | 100.3 | 111.4 | 100.9 | 8.9 | 21.4 |
| Secure floor | 267.4 | 274.1 | 280.7 | 287.5 | 294.5 | 301.6 | 6.7 | 20.4 |
| Transportation | 74.2 | 67.6 | 49.0 | 41.6 | 33.8 | 29.0 | -6.7 | -33.8 |
| Small revenue lines (under $20B in FY2040) | 1.9 | 6.2 | 6.8 | 7.2 | 7.6 | 8.3 | 4.3 | 1.3 |
| Dedicated funds (SS, HI, education, paid leave), net, by difference | -122.3 | -125.3 | -132.9 | -136.5 | -140.2 | -144.0 | -3.0 | -14.9 |
| Clean power | 140.1 | 142.8 | 147.6 | 175.3 | 184.5 | 106.2 | 2.7 | 41.7 |
| Work | 48.1 | 50.3 | 52.3 | 54.2 | 56.1 | 58.0 | 2.2 | 5.7 |
| Immigration | 17.8 | 18.6 | 21.1 | 23.2 | 25.0 | 26.2 | 0.7 | 6.4 |
| Democratic renewal | 16.9 | 17.4 | 13.1 | 13.5 | 14.0 | 14.3 | 0.6 | -3.5 |
| **General-fund gap (sum)** | 46.6 | 276.8 | 272.1 | 258.8 | 192.5 | -6.0 | 230.2 | -84.3 |

### Health, net: gross spending less the health financing lines ($B; positive = health costs the general fund more than it raises)

| | FY2030 | FY2033 | FY2036 | FY2037 | FY2038 | FY2039 | FY2040 | FY2045 | FY2056 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Health spending (HLT lines) | 79.8 | 1,073.1 | 3,428.7 | 3,610.3 | 3,766.0 | 3,900.9 | 4,058.5 | 5,239.1 | 8,318.3 |
| Health financing lines | 265.7 | 1,186.3 | 2,869.7 | 3,016.3 | 3,171.8 | 3,335.5 | 3,508.0 | 4,391.6 | 6,735.6 |
| Net | -185.9 | -113.2 | 559.0 | 594.0 | 594.2 | 565.4 | 550.5 | 847.5 | 1,582.7 |

The health financing set is HX, HCU, HEC, HEX, HCW, HCA, HCH, HS1-HS4, H1a, H1b and settlement S03 and S06. Lines that also appear as general revenue (G-rows) are not counted here. This is a reading of the audit, not a model total.


## 7. Top 10 lines by FY2036-39 cost

Top 10 by FY2036-39 cost (sum of the four years, $B):

| # | Line | FY2036-39 total |
|---|---|---:|
| 1 | HLT-7 | 12,910.7 |
| 2 | HLT-9 | 1,507.0 |
| 3 | FAM-2 | 858.0 |
| 4 | FAM-1 | 832.8 |
| 5 | LEAVE (F) | 742.9 |
| 6 | HOU-1 | 328.6 |
| 7 | CLI-1 | 243.8 |
| 8 | CAP-7 | 221.8 |
| 9 | HLT-10 | 184.0 |
| 10 | EDU-1 | 160.5 |

Top 10 without the single plan's gross line and without fund lines (the general-fund view):

| # | Line | FY2036-39 total |
|---|---|---:|
| 1 | HLT-9 | 1,507.0 |
| 2 | FAM-2 | 858.0 |
| 3 | FAM-1 | 832.8 |
| 4 | HOU-1 | 328.6 |
| 5 | CLI-1 | 243.8 |
| 6 | CAP-7 | 221.8 |
| 7 | HLT-10 | 184.0 |
| 8 | EDU-1 | 160.5 |
| 9 | MOV-31 | 151.2 |
| 10 | EDU-5 | 136.7 |
