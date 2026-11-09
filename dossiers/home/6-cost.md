# A home you can keep: cost

Role: section 6 of the housing dossier. It prices each provision of section 4 (`4-specification.md`, `provisions.json`) on the delivery timeline of section 5 (`5-delivery.md`, PR #137), with budget authority, outlays, revenue effects and a low, central and high figure, and tests the result against the fiscal rule (D4-B) with the budget model's own figures. Status: draft (stage C, step 5). It changes no ledger figure, adopted input or model code: every change it implies is a proposal, listed in section 5 below, for Espen and the lead (tier 3). The tax credits (HOU-2) are shown for options B and D side by side, undecided.

## How to read this section

- **Counting rules.** The project's budget conventions (`models/tools/budget/CONVENTIONS.md`). Amounts are nominal dollars by federal fiscal year (FY), as deficit effects: a cost is positive. The common window is FY2030-39 (`ASM-WINDOW`), with FY2029 shown as its own line. Each bill is also read over its own CBO window (budget choice 3). For R2, under the FY2030 budget resolution, that window is FY2030-39, the same as the plan's. "At maturity" means FY2040 and after, where the D4-B maturity test reads (`ASM-MATURITY`). Each provision is measured as an increment over the adopted baseline (`ASM-INCREMENT`). Interest on the added borrowing is left out of each provision's cost, as in a CBO score; the debt tests in section 3 include it (`CONVENTIONS.md`, section 10).
- **Low, central and high.** The central figure is the one the tests use: midpoints decide, with a cautious reading beside them (budget choice 2, `ASM-CALIB-MID`). Low and high move every judgment input in the same direction, so they bracket the result rather than give a probability.
- **What is model output and what is this section's arithmetic.** The model's figures are quoted from its generated files: `legacy/index/fiscal-long-term-model.md` (the fiscal model's D4 tests, scenario DEC), `models/data/recovery-budget-paths.csv` (the Recovery and Solvency budget, which carries the adopted spending allocations; `ASM-REC-EXPLORATORY`), and the provision library's paths for the housing rows (`models/tools/budget/provisions.py`). The provision-level figures are this section's arithmetic. They are an estimate, not a score: the inputs are listed in section 1.1 and every judgment is marked. Section 3 lays this arithmetic over the model's published paths; that is not a model run, and the model stays canonical until a tier-3 PR changes its inputs.
- **Validation status.** The budget model's benchmarks have not all passed (`models/tools/budget/MODEL-CARD.md`, milestone status). The D4 readings rest on the accounting identities and the interest arithmetic, which do pass, and on the ledger's midpoints, which no benchmark tests. Year-by-year budget authority for discretionary rows is rough (PS-4a and PS-4b fail); this section's housing rows are mandatory, but the spend-out of its capital grants is this section's judgment, not CBO's rate.

## In brief

1. **The housing plan costs about $0.57 trillion over FY2030-39 with tax credit option B, or $0.60 trillion with option D** (central; range about $0.45-0.78 trillion). That is about $0.13 trillion below what the budget model now books for housing: $0.71 trillion, the ledger's $0.56 trillion plus the $0.147 trillion of HOU-4D and the housing-agency fee allowance that the recovery budget adds. The window falls because the new awards lease up over months rather than at once, the one-time $85 billion package (HOU-1A) is replaced by a smaller start and a standing fund, stage 2 starts in 2034 rather than 2030, and the credits are narrower than the legacy package.
2. **At maturity it costs more than the model books.** In FY2040 the plan's permanent housing lines cost about $77 billion (0.14% of GDP), against the $65 billion the model carries. Stage 3 for disabled renters (about $9 billion in FY2040, $14 billion by FY2042), the standing emergency fund (about $6 billion), and stage 2 at its true timing make up most of the difference. Capital money still being spent after FY2039 adds about $16 billion in FY2040, falling to zero by FY2043.
3. **Fit with the fiscal rule.**
   - The fiscal model's decided program (scenario DEC) already fails the maturity test by 0.13% of GDP in FY2040, before HOU-4D or any of this section's new costs.
   - The adopted recovery architecture passes it with a margin of $4.5 billion in FY2040, and only that year is tight.
   - Swapped into it, this section's central housing costs use up that margin. FY2040 then fails by about $7 billion counting the permanent lines alone, or $23 billion with the capital tail. From FY2041 the test passes again, by about $25 billion, and by more each year after.
   - The high case fails FY2040 and FY2041. The low case passes.
   - So housing's new permanent costs are not yet paid for in FY2040. The financing settlement has to cover them, or the timing has to change (questions 1 and 5).
4. **Stage 3 checks out at the lead's rough figure.** On HUD's 2023 counts, about 0.5-0.8 million households qualify if the stage covers people under 62 with severe housing problems. Fully enrolled, they cost about $14 billion a year in FY2042 dollars (range $8-26 billion). If stage 3 also covers disabled people 62 and over, the count could roughly double, and it is unpriced.

## 1. Each provision's cost

### 1.1 Inputs common to the rental help lines

| Input | Central | Low | High | Basis |
| --- | --- | --- | --- | --- |
| Rent subsidy per leased household, FY2030 | $17,000 | $15,500 | $18,500 | HUD's 2023 spending per voucher unit, $1068 a month (about $12,800 a year) [EV-HOU-370], grown at 4% a year to 2030. That lands within 1% of the legacy planning figure ($15,200 in FY2026, growing 3%; `legacy/domains/domain-housing.md`, HOU-4A). The range is judgment: price growth of 2.3% to 5% a year from 2023. The account grew 34% in four years to FY2023 [EV-HOU-187] |
| Growth after 2030 | 3% a year | 2.3% (CPI, `ASM-CPI-PATH`) | 4% | Legacy planning input; range is judgment |
| Share of awards leased at steady state | 90% | 84% | 98% | National vouchers run 84% occupied [EV-HOU-370]. Section 5's full fees, search help, over-issue and reallocation should do better (judgment) |
| Time from award to lease | 6 months | 9 | 3 | Emergency Housing Vouchers took 77 days from issuance to lease, but only 67% were leased after almost two years (section 5, 2.2). The central figure is judgment |
| Housing agency fees | 8.1% of the subsidy, plus a $750 issuance fee per award | 7%, $500 | 10%, $1,000 | The legacy fee allowance ($12.2 billion on $150 billion; `recovery-adoption.json`, `housing_admin_basis`). Section 5 requires fees in full, never prorated; HUD now prorates regular fees at 85% (section 5, 2.2). If the legacy 8.1% reflects prorated fees, full fees are about 9.5%, inside the high case. The issuance fee is judgment |
| Search help (HOU-4.07) | $2,000 per new award and per reissue (10% of leased households a year) | $1,000 | $3,500 | Judgment, pending the design research section 4 still owes. Includes section 5's landlord damage and vacancy fund |
| Award timing | R2 signed about January 14, 2030; first awards from April 2030; 250,000 in each of FY2030-33 | | | Section 5's central calendar date; awards within six months of enactment |

### 1.2 The table

FY2030-39 outlays in billions, central (low-high). "BA" is budget authority. FY2040 is the first year of the maturity test. "Kind" is how the money is enacted (section 4's vehicles).

| Provision | Kind and vehicle | BA, FY2030-39 | Outlays FY2030-39 | FY2040 | At maturity | Source |
| --- | --- | --- | --- | --- | --- | --- |
| HOU-4A.01-.02 One million awards, with full fees | Mandatory, R2 | About equal to outlays, plus each award year's unspent first-year money, which stays available until spent | 147 (116-194): rent 136, fees 12 | 22 (18-30) | Permanent; grows with rents. 900,000 households leased from FY2034 | Section 1.1 |
| HOU-4.07 Search help, all new awards and moves | Mandatory, R2, as a per-award fee beside the agency fee | Equal to outlays | 8 (3-17) | 1 | Permanent, about $0.6-1 billion a year | Section 1.1 |
| HOU-4D.01 Stage 2 guarantee, 2034 on | Mandatory, R2; a right from 2037 | Equal to outlays ("such sums" once it is a right) | 81 (44-142) | 23 (12-44) | Permanent. About 920,000 families leased (590,000-1,470,000) | Section 1.3 |
| HOU-4.08 Stage 3, disabled renters, 2038 on | Mandatory, R2 (effective 2038) | Equal to outlays | 5 (2-13), FY2038-39 only | 9 (5-18) | Permanent. About $14 billion in FY2042 (8-26) when fully enrolled | Section 2.1 |
| HOU-1D.04 One-time start, 2030-31 | Mandatory, R2, one-time | 15 (10-25) in FY2030 | 15 (10-25), spent FY2030-32 | 0 | None | Section 2.2 |
| HOU-1D.01-.03 Standing emergency fund | Mandatory, R2; a capped yearly amount, indexed | 5 a year from FY2031, indexed: 49 (30-79) | 49 (29-78) | 6 (4-10) | Permanent | Section 2.2 |
| HOU-3C.01 State revolving fund grants | Mandatory, R2; borrowed inside the envelope (C21) | 72 | 60 | 7 | Time-limited; about $12 billion spent FY2040-42 | Legacy amounts (section 4); spend-out is this section's judgment: 15%, 35%, 30%, 20% over four years |
| HOU-3C.02 Construction loans, $300 billion | Credit subsidy, R2 (Federal Credit Reform Act) | Subsidy BA at commitment: about 15 at a 5% rate | 13 | 1 | Time-limited | Legacy: subsidy rate 2-10%, central 5%; needs CBO's rate |
| HOU-5.01 Public housing repair | Mandatory, R2; borrowed inside the envelope (C31) | 58 ($5.8 billion a year more than FY2026) | 50 | 5 | Time-limited; about $8 billion spent FY2040-42 | Legacy amount; spend-out judgment |
| HOU-6.01 Zoning reward (Innovation Fund) | Mandatory, R2 | 30 | 25 | 3 | Time-limited as priced (question 6) | Legacy amount; awards follow finished homes, so spending lags (judgment) |
| HOU-8.01 Social housing pilot, equity | Mandatory, R2 | 10 | 9 | 1 | Time-limited | Legacy |
| HOU-9A.01 Small federal builder, capital | Mandatory, R2 (capital); regular bill (the corporation) | 5 (2-20) | 5 | 0 | Time-limited capital; its loans repay | Placeholder, judgment: the legacy file leaves it unscored |
| HOU-4.10 Recovery housing, 2030-34 | Mandatory, R2, time-limited | 1.5 | 1.5 | 0 | Appropriations after 2034 if renewed | Placeholder, judgment; no evidence on per-place cost in the register |
| HOU-4.12 HUD services backstop | Mandatory, R2, 2030-39; appropriations after | 6 | 6 | 1 | Permanent at about $0.7 billion as priced, but as appropriations | Placeholder, judgment (section 2.3) |
| **Spending, total** | | | **473 (373-637)** | **78 with the capital tail; 62 permanent** | | |
| HOU-2.01 Tax credits, option B | Revenue, R2 | None (a revenue loss) | 100 (80-120) | about 15 (12-22) | Permanent for the low-income credit | Section 4 |
| HOU-2.01 Tax credits, option D | Revenue, R2 | None | 122 (102-142) | about 16 (13-24) | As B, plus trial credits claimed to about 2048 | Section 4 |
| **Housing, with option B** | | | **573 (453-757)** | **93 (67-139)** | | |
| **Housing, with option D** | | | **595 (475-779)** | **94 (68-140)** | | |

**Provisions with no cost of their own.** HOU-4.01 to HOU-4.06, HOU-4.09, HOU-4.11, HOU-5.02, HOU-6.02, HOU-7B.01 and HOU-3C.03 are rules, conditions or regular-bill items. Their costs, if any, sit in the rows above. HOU-4.05's neighborhood payment limits change the cost per award, and the register has no national estimate of by how much (section 4).

**Revenue effects.** HOU-2 is the only revenue line. The construction loans' repayments and interest are inside their subsidy cost under credit reform (legacy file). No offsetting savings are counted anywhere: not shelter or Medicaid savings from Housing First, which the National Academies advise not to expect except perhaps among the heaviest users [EV-HOU-315] [EV-HOU-318], and not lower spending on homelessness programs. That is CBO's practice for savings outside the bill's own accounts, and the cautious choice.

**FY2029, disclosed.** Housing puts nothing in R1, so its FY2029 line is $0 in mandatory money. HUD's readiness work in 2029 runs on appropriations and the agency rebuild (CAP-7S, CAP-7; section 5). If Espen approves section 5's readiness tranche in R1 (section 5, question 1), it would be a FY2029 line of roughly $0.5-1 billion (judgment, unpriced) in R1's own window, FY2029-38.

### 1.3 How the rental help lines are built

- **HOU-4A.** 250,000 awards a year, issued evenly from April 2030 (FY2030) and through FY2031-33. Each award leases after the lag, at the steady-state share, and costs the subsidy plus fees.
  - Over the window that is 6.7 million household-years leased (central), against 8.0 million if every award leased the day it was issued.
  - On that no-lag assumption, this section's subsidy gives about $160 billion of rent help, near the legacy $150 billion. The lease-up lag and the 90% leased share take about $24 billion off, leaving $136 billion. Fees are about the legacy allowance ($11.7 billion against $12.2 billion). Search help ($3.6 billion for these awards) is a separate line.
  - So the central figure, $147 billion with fees, is about $15 billion below the legacy $162.2 billion, mostly because the legacy figure pays for every award from its first day.
- **HOU-4D.** Enrollment opens in FY2034 at up to 300,000 families a year. In FY2037 every remaining family that applies enrolls. The group is HUD's 1.717 million extremely low-income families with children with worst case needs in 2023 [EV-HOU-186], less the families the first million reach. Memo 2's split puts that remainder at about 1.2 million, which this section takes as central (1.0-1.5 million). Of them, 85% apply (70-100%; judgment: no take-up evidence for a housing right is in the register). After 2037 the count is held flat, new eligible families replacing those who leave, as memo 2 assumed.
  - Central: about $81 billion through FY2039 and $22 billion in FY2039. Memo 2's arithmetic gave $114 billion at full sign-up, or $123 billion with fees, and about $27 billion a year by 2039. The central case is lower because it counts take-up, the lease-up lag and the leased share; the high case, at full sign-up, is $142 billion.
  - **The $135 billion envelope fits the window but books the wrong years.** The recovery budget spreads it from FY2030 on a four-year ramp (`models/tools/recovery-budget/model.py`, `housing_extra`). So it carries about $35 billion in FY2030-33, before stage 2 opens, and $18.9 billion in FY2040, against $22.7 billion here. The window cost is overstated and the maturity cost understated. Section 5 lists the fix.
- **Stage 2's exit rule** (families keep help while under 80% of area median income, section 4) is inside the flat-count assumption. A tighter line, such as 50%, would lower the mature count. The register has no exit data to price it.

## 2. The new costs the decisions add

### 2.1 Stage 3: disabled extremely low-income renters, from 2038

**Who.** HUD's 2023 count gives 1.162 million very low-income renter households with someone younger than 62 with a disability and worst case needs. Of them, 345,000 are families with children, 57,000 older-adult households, 175,000 other families and 585,000 other single-person or nonfamily households [EV-HOU-371].
- The families with children fall in stage 2 if they are extremely low income. That leaves about 817,000 households (this section's arithmetic).
- HUD does not split them by extremely low and very low income. Across all renters, extremely low-income households are 68.6% of worst case needs [EV-HOU-185]. A person living alone on SSI had $914 a month in 2023 [EV-HOU-372], under the extremely low-income line almost everywhere, so the share among disabled households is likely higher (judgment).
- At a 69-85% share that is about 560,000-690,000 households. With 85-100% applying, and room for growth or a broader test, the central count is 600,000 (450,000-800,000).
- That matches the lead's rough range of 0.5-0.8 million.

**Cost.** Enrollment over 2038-40, a third a year (judgment; section 4 leaves the pace to the care flagship and this section), at the same subsidy, fees and lease-up as the other awards.
- FY2038-39: about $5 billion (2-13), inside the window and outside the $135 billion, as memo 2's condition requires.
- FY2040: $9 billion (5-18).
- Fully enrolled: about 540,000 households leased, about $14 billion in FY2042 (8-26) and $15.5 billion in FY2045.
- **Check of the lead's estimate.** "$12-19 billion a year at maturity" holds. At FY2042 rents, with fees, 0.5-0.8 million households leased would cost about $13-21 billion; with 90% of them leased, as section 1.1 assumes, about $12-19 billion. The central case, $14 billion, is inside both.

**What the count leaves out, unpriced.**
- **Disabled people 62 and over.** HUD's report counts disability only under 62 [EV-HOU-371]. Section 4 says older renters who are *not* disabled have no funded route, which implies older disabled renters are in stage 3. There are 1.749 million older extremely low-income worst-case households [EV-HOU-186]. Two-thirds of older voucher holders report a disability (HUD's 2023 voucher data, not in the register), so the older disabled group could be as large as the under-62 group or larger. The register has no count, so it is unpriced (question 2).
- **The severe-problems test.** This section assumes stage 3 uses stage 2's test: unassisted, with severe problems. Without it, all unassisted extremely low-income disabled renters would qualify, a larger and uncounted group.
- **Services.** Stage 3's home and community-based services are the care flagship's (shared rule 7); see section 2.3. The accessible homes come from HOU-3C's existing money (HOU-3C.03), at no added cost in this section.

**Financing.** Stage 3 is a permanent claim from FY2038, so under D4 it must be paid for from FY2040 (section 4, HOU-4.08). Section 3 shows it is the largest single reason housing's FY2040 cost exceeds the model's.

### 2.2 The emergency fund (HOU-1D)

**Form.** Section 4 leaves the amount to this section. A standing fund that paid every eligible crisis would be open-ended: 23% of renters fell behind on rent at some point in 2025 [EV-HOU-008], and landlords filed 1.23 million eviction cases in 2025 in the places Eviction Lab tracks, only part of the country [EV-HOU-077]. So this section prices it as a **capped yearly amount, set in the statute and indexed to prices**, paid through the grantee network by need formula. Mandatory money of a fixed size, not an entitlement, is how the 2021-22 program and Emergency Housing Vouchers were funded [EV-HOU-150] [EV-HOU-188].

**Size (judgment, central $5 billion a year from FY2031; range $3-8 billion).**
- At about $3,500 per household, with legal help and administration, $5 billion serves roughly 1.4 million households a year. That is about the scale of the tracked eviction filings and a small share of renters who fall behind.
- The per-household figure is judgment. It sits between the Santa Clara trial's average of about $2,000 [EV-HOU-109] and the cap of four months' Fair Market Rent (HOU-1D.01).
- Targeting decides value: in Chicago, preventing one case of homelessness cost about $10,300, and less with better targeting [EV-HOU-108].

**The one-time start (HOU-1D.04): central $15 billion over 2030-31 (range $10-25 billion).** It is smaller than the $85 billion of HOU-1A, and rent help only. The binding limit is what a network built in 2030 can pay out well. The 2021 program spent about 6% of its first $25 billion in five months, and paid 2% of households twice [EV-HOU-150]. Section 5 has the network named in 2030. Outlays are spread over FY2030-32 (30%, 50%, 20%; judgment).

**Against the ledger.** The ledger's housing title carries HOU-1A at $85 billion (section 4). HOU-1D costs $64 billion over the window: $15 billion one-time and $49 billion standing. So the window falls about $21 billion. But the standing fund adds about $6 billion a year at maturity, where HOU-1A added nothing.

### 2.3 Supportive-housing services: what is housing's and what is care's

| Cost | Whose | Where it is counted | Priced here? |
| --- | --- | --- | --- |
| Rent for supportive-housing tenants | Housing | HOU-4A stage 1 awards (HOU-4.11, item 4) | Yes, inside HOU-4A |
| Tenancy-sustaining services, housing navigation, assertive community treatment for Medicaid enrollees | Care (HLT-4, Medicaid home and community-based services) | The care flagship's HLT-4 row, with Medicaid restored by HLT-1 | No: counting it here would count it twice |
| Medicines for opioid use disorder and other treatment | Care and health coverage (HLT-1, HLT-4) | Health rows | No |
| Stage 3's home and community-based services | Care (HLT-4) | Health rows | No |
| The same services for tenants without Medicaid | Housing (HOU-4.12 backstop) | This section | Placeholder |
| Peer training, wage floors and caseload limits on the HUD backstop | Housing | Inside HOU-4.12 | Placeholder |
| VA case managers for HUD-VASH | VA, care flagship (section 5, 2.6) | Not housing | No |

**The backstop is a placeholder.** It is priced at $0.5 billion in FY2030, growing 3% a year: about $6 billion over the window and $0.7 billion in FY2040 (judgment). The register has neither the per-tenant service cost nor the count of supportive-housing tenants without Medicaid (section 4, "Evidence still needed").
- In Denver, savings elsewhere offset about half the yearly cost per person, $6,876 [EV-HOU-318]. That gives the scale, not the split.
- Section 5's question 3 would extend the backstop to tenants whose state Medicaid program does not cover the services, through 2035. That could cost several times more, depending on how many states opt out of HLT-4's benefit, and it is unpriced.

**The rule against double counting.** HLT-4's row prices the Medicaid services. This dossier prices only the backstop, for people HLT-4 does not reach. When HLT-4 is costed, its documentation should say whether it includes tenancy supports and assertive community treatment, as section 4 asks (HOU-4.12, item 1). If it does not, the gap stays with care, not housing.

### 2.4 Full housing agency fees and administration

- **Fees in full, never prorated, with an issuance fee** (section 5, 2.2) are inside HOU-4A, HOU-4D and HOU-4.08: about $12 billion, $7 billion and $1 billion over the window. That is 8.1% of the subsidy plus $750 an award.
- If "in full" means the unprorated rate and the legacy allowance was set at prorated rates, the fee is about 9.5%. That adds about $2.5 billion over the window and $0.7 billion a year at maturity (this section's arithmetic; inside the high case).
- **HUD's own staff** are in the agency rebuild (CAP-7S, CAP-7), not here (section 4, HOU-4A.02).
- Section 5's proposal to set aside a share of each new mandatory program for federal administration, systems and evaluation is **unpriced**. If carved out of the amounts above, it adds nothing. If added, 0.5% of housing's mandatory outlays would be about $2.5 billion over the window (judgment).

### 2.5 The guarantee from 2037

Stage 2 becomes a right in 2037: every eligible family that applies gets help (HOU-4D.01). That turns its cost from a capped envelope into an estimate.
- **The year it becomes a right.** FY2037 enrollments take stage 2 from about 900,000 families awarded to the full group, about 1.02 million in the central case. Its cost rises from $12 billion in FY2036 to $18 billion in FY2037 and $22 billion by FY2039 (central).
- **Remedies.** The private right of action and deemed approval (section 5, 6.3 and question 5) are not separately priced. Deemed approval pays some families before checks, and its error cost is unknown.
- **The risk.** The high case, $44 billion in FY2040, is about twice the central one. Full sign-up, a larger group and faster rent growth drive it, and none of them is in the government's control once help is a right. That is what memo 2 warned: "the $135 billion becomes an estimate, not a cap."

## 3. Fit with the fiscal rule

### 3.1 The rule

D4-B has three parts (`ASM-MATURITY`, `ASM-ENVELOPE`, `ASM-GUARDRAILS`; Decision Brief 2):
- **Maturity.** Permanent programs are paid for: the general fund's primary balance from the program must be at or below zero in FY2040 and every later year to 2056.
- **Envelope.** Time-limited investments may be borrowed for inside 0.5% of GDP to 2034, tapering to zero by 2040.
- **Guardrails.** Total debt and net interest stay below the baseline.

### 3.2 What the model says today

| Reading | Result | Housing inside it | Source |
| --- | --- | --- | --- |
| Fiscal model, decided program (DEC): maturity | **Fails**: general fund 0.13% of GDP short in FY2040 (about $72 billion) and in its worst year | HOU-1 only ($0.56 trillion over the window; $44.7 billion in FY2040). No HOU-4D, no fee allowance | `legacy/index/fiscal-long-term-model.md`, "D4 tests" |
| Fiscal model, DEC: envelope | $1.60 trillion of room over 2030-39; $1.30 trillion held by accepted borrowing lines; $0.30 trillion left | C21 (HOU-3C's state grants, $0.06 trillion) and C31 (HOU-5's repair, $0.06 trillion) | Same; `models/data/inputs/ledger-cuts.csv` |
| Fiscal model, DEC: guardrails | Pass: total debt 2.8, 11.6 and 23.8 points below the baseline in 2035, 2045 and 2056; net interest below the baseline | As above | Same |
| Recovery budget, mixed case (the adopted architecture; its tax rates exploratory) | **Passes** the maturity test, by $4.5 billion in FY2040, $49.6 billion in FY2041 and $96.7 billion in FY2042; the margin widens every year to 2056 | HOU-1's two components, HOU-4D's $135 billion and the $12.2 billion fee allowance: $65.2 billion in FY2040 | `models/data/recovery-budget-paths.csv`, case `mixed`, `agenda_gf_primary_bn`; `ASM-REC-EXPLORATORY` |

The two readings differ because the recovery budget adds the adopted architecture's new revenue and spending changes. Its tax schedule is exploratory and no financing is adopted. Neither model certifies D4 (`legacy/index/recovery-budget.md`).

### 3.3 This section's housing costs in the rule

Replace the model's housing paths with this section's, and leave everything else as the model has it.

| FY | Model's housing | This section, central (B) | Difference | Recovery budget's general-fund balance, adjusted | Test |
| --- | --- | --- | --- | --- | --- |
| 2039 | 88.9 | 90.0 | +1.1 | 138.5 (inside the envelope years) | Not a maturity year |
| 2040 | 65.2 | 93.1 (76.7 permanent) | +27.9 (+11.5) | **+23.4 (+7.0 permanent only)**, 0.04% (0.01%) of GDP | **Fails** |
| 2041 | 67.5 | 91.5 | +24.1 | −25.5 | Passes |
| 2042 | 69.8 | 88.4 | +18.6 | −78.1 | Passes |
| 2045 | 77.2 | 93.5 | +16.2 | −205.6 | Passes |
| 2056 | 110.8 | 130.1 | +19.4 | −479.2 | Passes |

Billions. The adjusted balance is the recovery budget's FY figure plus the difference; negative passes.
- **Low case:** FY2040 passes, at −$2 billion.
- **High case:** FY2040 fails by $69 billion (0.13% of GDP) and FY2041 by $24 billion. It passes from FY2042.
- **Option D** adds about $1 billion a year to option B through 2047.
- **Against the fiscal model's DEC,** which carries no HOU-4D, this section's housing adds about $48 billion in FY2040. That widens DEC's shortfall from 0.13% to about 0.22% of GDP.

**What this means.**
1. **Housing's new permanent claims are not yet financed in FY2040.** Stage 3, the standing fund and stage 2 at its true timing add about $12 billion a year at maturity to what the model carries. FY2040 is the one year with no margin to absorb it. From FY2041 the adopted architecture's margin covers housing's central costs, and its high case from FY2042.
2. **The capital tail is the other FY2040 problem.** Grants and repair money awarded in FY2037-39 are still being spent in FY2040-42: about $16 billion in FY2040. The envelope ends in 2040, and nothing in the D4 text exempts a time-limited line's last outlays from the FY2040 test. Two fixes: schedule the capital awards so they are spent by FY2039 (move the last two years' awards forward, keeping the amounts), or rule that a time-limited line's tail counts as time-limited (question 5).
3. **The guardrails are not at risk from housing.** Before interest, this section's central costs sum to about $0.12 trillion less than the model's through 2035, about the same through 2045, and $0.18 trillion more through 2056: 0.19% of 2056 GDP. The high case is 1.6% of 2056 GDP more, perhaps two to three points of debt with interest (this section's arithmetic, not run). The DEC guardrails pass by 2.8, 11.6 and 23.8 points in 2035, 2045 and 2056, and housing's high case lowers debt through 2035.
4. **The Byrd rule.** R2's permanent housing lines raise deficits after the window. Reconciliation strikes a provision that adds to deficits beyond the resolution's window (`CONVENTIONS.md`, section 5), unless other provisions in its title offset it in those years. So R2 needs the offsets for stage 2, stage 3, the standing fund and the credits in the same bill, or the lines must sunset. This is the per-bill test budget choice 3 asks for, and B3 has not built it (`models/tools/roadmap.md`).

### 3.4 Within the envelope

Housing uses $0.12 trillion of the envelope through C21 and C31, unchanged by this section. Of the $0.30 trillion left, housing could ask for HOU-8's equity grant and HOU-9A's capital (about $0.014 trillion, time-limited capital). That would lower the general-fund window claim by that much and leave the maturity test unchanged. The emergency fund's start and the vouchers are not investment, so they stay general-fund claims.

## 4. The tax credits, options B and D, side by side (undecided)

Memo 3 part 1 is still before Espen. The figures are memo 3's research (`memo-3-part1-research.md`; `memos/3-production.md`). None is a JCT score.

| | **B. Narrower credits, permanent affordability** | **D. A bit of all three, each where it adds homes** |
| --- | --- | --- |
| Low-income credit increase with the deep-income boost | Yes | Yes, as in B |
| Middle-income credit | Postponed until GAO's July 2027 report [EV-HOU-242] | Tight markets only, 2030-34 awards, a trial with lottery evaluation: about $7 billion over 2030-39, with claims running to about 2048 |
| Neighborhood Homes credit | Dropped | 2030-34, with evaluation: about $15 billion over five years [EV-HOU-269] [EV-HOU-270] |
| FY2030-39 revenue loss | About $0.10 trillion ($0.08-0.12; legacy estimate HOU-2B) | About $0.12 trillion ($0.10-0.14) |
| FY2040 | About $15 billion (12-22) | About $16 billion (13-24) |
| After 2040 | Permanent; grows with the credit's claims | As B; the trial credits stop adding cost by about 2048 |
| Against the ledger's $0.15 trillion (HOU-2A) | −$0.05 trillion | −$0.03 trillion |

**The credits' FY2040 cost is the least certain figure in this section.** Each year's low-income credits are claimed over ten years once a building is in service. So a permanent allocation increase keeps building in cost for a decade before it levels off.
- This section spreads the legacy window estimate on a three-year ramp, which gives about $15 billion in FY2040.
- If claims instead build year by year from 2031, the same $0.10 trillion window total implies about $22 billion in FY2040 (this section's arithmetic).
- Neither is a score. The 2025 tax law's 12% increase scored at $15.7 billion over ten years [EV-HOU-261], which shows the scale of one such change. A JCT score of the chosen option is needed before the maturity test can rely on it.

## 5. Changes this section proposes for the ledger and the models (for Espen and the lead; tier 3)

None is made here. Each moves figures, so each is an adopted-input change for its own PR (`models/tools/budget/WORKFLOW.md`, B6).

1. **Replace HOU-1's two components** (`fiscal-components.csv`: the legacy title at $0.47 trillion with 55% continuing, and the voucher increment at $0.09 trillion) with provision-level components or `split` rows, one per line of the table in section 1.2. Each gets its own continuing share:
   - permanent: HOU-4A, HOU-4.07, HOU-4D, HOU-4.08, HOU-1D's standing fund, HOU-2's low-income part, and HOU-4.12 (as appropriations after 2039);
   - time-limited: HOU-1D.04, HOU-3C, HOU-5, HOU-6.01, HOU-8, HOU-9A and HOU-4.10.

   The title's single 55% continuation (`ASM-PROF-TIMELIMITED`, `ASM-PROF-COMPONENTS`) mixes one-time and permanent pieces.
2. **Retime HOU-4D** (`housing_extra_tn` in `recovery-adoption.json`, read by the recovery budget with a 2030 start and four-year ramp). Start it in FY2034, rising to the full group in FY2037. Central $0.081 trillion over the window, $22.7 billion in FY2040.
3. **Fold the fee allowance** (`housing_base_admin_tn`, $0.0122 trillion) into the HOU-4A component, at fees in full plus an issuance fee. Add HOU-4.07's search help as its own line.
4. **Add stage 3 (HOU-4.08)** as a permanent mandatory row from FY2038: central $0.005 trillion over the window and about $14 billion a year from FY2042, outside the $135 billion.
5. **Replace HOU-1A's $0.085 trillion** with HOU-1D:
   - a one-time $0.015 trillion over FY2030-32;
   - a standing fund of $5 billion a year from FY2031, indexed to prices, permanent.
6. **Book HOU-2** as its own revenue row once Espen decides: $0.10 trillion (B) or $0.12 trillion (D), with a claims-based continuing profile, pending JCT.
7. **Splits** (`provision-splits.csv`, empty today):
   - HOU-4.12: mandatory in R2 for FY2030-39, appropriations after;
   - HOU-4.10: mandatory for 2030-34, appropriations if renewed;
   - HOU-6.01: R2 money, with the eligibility rules in the regular bill at no cost.
8. **Capital spend-out.** Record budget authority and outlays separately for HOU-3C.01, HOU-5.01 and HOU-6.01. Their budget authority ($72, $58 and $30 billion) exceeds their window outlays ($60, $50 and $25 billion). Decide question 5 before the FY2040 test is read.
9. **Provision specs** (`provisions.csv`): the housing components' `budget_authority` is `unknown` today. For the rental help lines it would be `outlays`; for the capital lines, provided in full on enactment with spend-out.
10. **Byrd check.** When B3 builds the per-bill window test, run R2's housing title through it (section 3.3, item 4).

The net effect on the headline (central, option B): about −$0.13 trillion over FY2030-39, about +$12 billion a year in FY2040 for the permanent lines, and about +$28 billion in FY2040 with the capital tail.

## 6. What is still unpriced

- **The tax credits' JCT score** and their FY2040 run rate (section 4).
- **Stage 3 for disabled people 62 and over,** and stage 3 without a severe-problems test (section 2.1).
- **Supportive-housing services:** the per-tenant cost and the count of tenants without Medicaid behind the HOU-4.12 placeholder, and section 5's extension of it to states that do not cover the services (section 2.3).
- **HOU-9A's builder:** capital, operating cost and loan subsidy (placeholder).
- **HOU-4.10's recovery housing:** grants per place (placeholder).
- **Search help's design and cost** (HOU-4.07): the research section 4 still owes.
- **Neighborhood payment limits** (HOU-4.05): their effect on cost per award.
- **Attached awards** (HOU-4.04): whether they cost more or less than tenant-based ones. The register has no evaluation.
- **Rent offsets from other flagships' benefits** (shared rule 1): new income outside the tax code raises tenants' rent and lowers housing's cost by up to 30 cents a dollar. That is the household model's work.
- **The capital tail after FY2039** under either answer to question 5, and CBO's subsidy rate for the construction loans.
- **Section 5's smaller items:** the R1 readiness tranche (FY2029), HUD's administration set-aside, fair housing testing grants for 2030-34, a tribal set-aside (a share, not more money), and the cost of deemed approval.
- **Inflow and outflow in stage 2** after 2037. The count is held flat, and the exit rule's effect is unmeasured.

## Questions for Espen

Each is yes or no, and none is adopted until you answer. "Housing's FY2040 gap" means the shortfall in the fiscal rule's maturity test in FY2040, on the budget model's adopted architecture.

1. **Should housing's FY2040 gap go to the financing settlement rather than be closed by trimming housing?** On the central figures housing is about $7 billion short in FY2040 counting permanent programs only, or $23 billion with the capital tail. From FY2041 the adopted architecture's margin covers it. The alternative is to slow something in housing: stage 3's enrollment over 2038-41 instead of 2038-40 would save about $3 billion in FY2040 (this section's arithmetic). Recommendation: yes, send it to the settlement, with the slower stage 3 as the fallback.
2. **Does stage 3 include disabled renters 62 and over?** Section 4 implies it does. HUD's worst case needs report (2025) counts disability only under 62. The older group could be as large again, unpriced. Recommendation: decide with the care flagship; until then, price stage 3 for people under 62 and say so.
3. **Should stage 3 use stage 2's test: unassisted, with severe housing problems?** This section assumes yes. Without it, the eligible group is larger and uncounted. Recommendation: yes.
4. **Should the standing emergency fund be a capped yearly amount of about $5 billion, indexed to prices, with a one-time start of about $15 billion in 2030-31?** Both sizes rest on judgment: the Santa Clara trial (Phillips and Sullivan) [EV-HOU-109], the 2021-22 program's start-up record (Congressional Research Service, 2023) [EV-HOU-150], and Eviction Lab's filing counts (2025) [EV-HOU-077]. An open-ended fund that paid every eligible crisis has no reliable cost. Recommendation: yes.
5. **Should the last two years of construction and repair money be awarded earlier, so it is spent by FY2039?** The amounts stay as you decided. Otherwise about $16 billion of capital spending falls in FY2040, the first year the rule tests, after the borrowing envelope closes. Recommendation: yes.
6. **Does the zoning reward (HOU-6.01) end with the FY2030-39 money?** Section 4 removes the Innovation Fund's 2033 end date but sets no money after 2039. Continuing at the same scale would be about $3 billion a year at maturity. Recommendation: yes, it ends unless renewed on its results.
7. **Should the central estimate for stage 2 assume 85% of eligible families apply, rather than memo 2's full sign-up?** The rule's tests use the central figure. Full sign-up is the high case: about $142 billion through 2039 rather than $81 billion. No evidence on take-up of a housing right is in the register. Recommendation: yes, with full sign-up reported as the cautious reading (budget choice 2).
8. **Should "fees in full" mean HUD's unprorated rate?** HUD now pays agencies 85% of their fees (section 5). The unprorated rate costs about $2.5 billion more over the window than the legacy allowance. Recommendation: yes.

## Evidence still needed

- A JCT score of tax credit option B or D, whichever Espen chooses.
- The number of extremely low-income renters with disabilities, by age, from the American Housing Survey or the American Community Survey (HUD tabulation or a custom run).
- Per-tenant service costs in supportive housing, and the share of tenants without Medicaid (research note's gap).
- HUD's housing agency fee rates in dollars and the national proration history, to settle the fee rate.
- Take-up of an entitlement to rental help: France's housing allowance [EV-HOU-156] is the nearest case in the register, but it is not a take-up estimate.
- CBO's credit subsidy rate for HUD-FFB risk-share lending.
- The year-by-year spend-out of HUD capital grants (HOME, the Capital Fund) from CBO's account-level projections, to replace this section's judgment.
