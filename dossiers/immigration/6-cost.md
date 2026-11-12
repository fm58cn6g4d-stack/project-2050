# A new consensus on immigration: cost

Role: section 6 of the immigration dossier. It prices the provisions of `4-specification.md` on federal fiscal years against the January 2029 law. It reports the fiscal-rule effect to the financing settlement (`charter/STANDARDS.md`, "Fiscal rule in dossiers: report, don't gate", `DEC-2026-11-10-05`), and reprices memo 5 and points 1 and 7 as Espen decided them. Status: draft (stage E, board row I4, PR 1), on `DEC-2026-11-12-07`. Every figure is project arithmetic, not an official score; none exists for a design like this (point 13 asks for one). **Nothing is booked here:** booking is a later step, after the milestone review, and part 6 lists the ledger rows and inputs it would change.

## Counting rules

- **Conventions.** Federal cost, nominal $ billion unless marked, against the January 2029 law (section 1, "The January 2029 baseline"), a cost positive. **On the general fund** unless a line says otherwise; Social Security's funds are reported apart (part 2).
- **Fiscal years.** FY y runs from October of y-1. The working timeline is `4-specification.md`, "Dates": filing opens about October 1, 2030 (FY2031); the single plan's first wave is January 1, 2031; E-Verify's first tranche is no earlier than October 1, 2032 (FY2033).
- **The model and the path.**
  - `tools/immigration_model.py` is this dossier's first, scoped immigration model (`charter/PLAN.md` 3.4). It covers USCIS's throughput and backlog with the fee and appropriation split, the courts' capacity and appointed counsel, detention at the cap against case management, and status's fiscal effect from CBO's published score. Every input traces to an evidence ID or is a labeled assumption with a range. Run: `python3 dossiers/immigration/tools/immigration_model.py`; test: `python3 dossiers/immigration/tools/test_immigration_model.py`.
  - `tools/immigration_path.py` lays the model's lines and the rest on fiscal years (run: `python3 dossiers/immigration/tools/immigration_path.py`).
  - Lines not in the model are memo 3's added workers, memo 6's table, E-Verify and the restructure. They stay labeled judgment on outside scores, and labor-market effects stay as cited evidence (`7-validation.md`, part 2).
  - Ranges for the model's lines run all its inputs at their low and high values together. That is a bound, not a probability interval. For memo 1, the wider bound from section 3 is kept, because the model's inputs do not span the pattern's own uncertainty.
- **Spending lines and revenue effects stay apart** (`dossiers/TEMPLATE.md`, "One basis for each fiscal figure"). Two revenue effects have their own lines: the income-tax offset on the retained H-1B fee and E-Verify's on-budget revenue. Neither is added into a spending line.
- **The booked basis.** The budget model's central case (`mixed`) on main at `7512852`: IMM-1 at −$140.0 billion over FY2030-39 and −$18.7 billion in FY2040; CAP-7S at $600 billion, of which USCIS's share is $40 billion [EV-IMM-573]. These figures are read from the model's audit lines (`legacy/sources/recovery-budget-audit.csv`), not rebuilt.
- **Each figure's status** (commitment, working assumption, open question) is in part 8.

## 1. The decided set on the general fund, by fiscal year

| Line | Provisions | 2030 | 2031 | 2032 | 2033 | 2034 | 2035 | 2036 | 2037 | 2038 | 2039 | **FY2030-39** | **2040** | Range FY2030-39 | Range 2040 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Status: tiers A and B and registration (memo 1) | IMM-1.01-1.14 | 0.0 | 1.0 | 2.0 | 3.6 | 5.1 | 5.6 | 6.6 | 8.1 | 9.1 | 9.6 | **50.8** | **10.2** | −50.0 to 150.0 | −5.0 to 20.0 |
| Records-first registry and fee waivers (memo 2) | IMM-1.05-1.09 | 0.3 | 1.9 | 1.5 | 0.7 | 0.3 | 0.2 | 0.2 | 0.2 | 0.1 | 0.1 | **5.4** | **0.1** | 2.0 to 12.9 | 0.0 to 0.3 |
| Legal immigration and the work routes (memo 3) | IMM-2.01-2.12 | −1.0 | −1.5 | −2.5 | −3.5 | −4.0 | −4.5 | −5.0 | −5.5 | −6.0 | −6.5 | **−40.0** | **−7.0** | −60.0 to −20.0 | −8.0 to −5.0 |
| Asylum, refugees, regional access, counsel (memo 4) | IMM-3.01-3.04, 3.12 | 1.8 | 2.6 | 2.7 | 2.8 | 2.8 | 2.9 | 2.5 | 2.6 | 2.6 | 2.7 | **26.0** | **2.8** | 15.3 to 41.2 | 1.5 to 4.6 |
| Asylum fee repeals, net of the 25% offset (point 8) | IMM-3.06 | 0.3 | 0.3 | 0.3 | 0.3 | 0.2 | 0.2 | 0.2 | 0.2 | 0.2 | 0.2 | **2.8** | **0.2** | 2.0 to 5.0 | 0.1 to 0.4 |
| The detention cap and case management (memo 5, A's rules) | IMM-4.05-4.06 | 0.1 | 0.1 | 0.1 | 0.1 | 0.1 | 0.1 | 0.1 | 0.1 | 0.1 | 0.1 | **1.1** | **0.1** | −3.3 to 9.1 | −0.4 to 1.1 |
| Replacing ICE; the detention inspector (memo 5, part 1 B) | IMM-4.01-4.02, 4.09 | 0.2 | 0.7 | 0.7 | 0.5 | 0.3 | 0.1 | 0.1 | 0.1 | 0.1 | 0.1 | **3.0** | **0.1** | 1.5 to 5.0 | 0.1 to 0.3 |
| E-Verify operations and error correction (memo 5, part 2 A) | IMM-4.12-4.15 | 0.0 | 0.1 | 0.3 | 0.3 | 0.4 | 0.4 | 0.4 | 0.4 | 0.4 | 0.4 | **3.3** | **0.5** | 2.5 to 6.0 | 0.3 to 0.7 |
| The one eligibility table (memo 6) | IMM-1.20-1.35 | 0.0 | 4.0 | 7.0 | 8.0 | 8.5 | 9.0 | 9.5 | 10.0 | 10.5 | 11.0 | **77.5** | **11.5** | 50.0 to 110.0 | 8.0 to 15.0 |
| USCIS beyond memos 2 and 4; naturalization fees (memo 7) | IMM-6.01, IMM-5.04 | 1.5 | 1.5 | 1.5 | 1.2 | 0.8 | 0.5 | 0.5 | 0.5 | 0.5 | 0.5 | **9.1** | **0.6** | 5.2 to 15.8 | 0.3 to 1.0 |
| Wall money redirected (point 7) | IMM-3.07 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | **0.0** | **0.0** | 0.0 to 0.0 | 0.0 to 0.0 |
| **Spending lines** | | **3.2** | **10.8** | **13.6** | **14.0** | **14.6** | **14.6** | **15.2** | **16.8** | **17.8** | **18.4** | **139.0** | **19.0** | **−34.8 to 335.0** | **−3.1 to 38.4** |
| *Revenue effect:* income-tax offset on the retained H-1B fee (25%) | IMM-2.07 (IF1) | 0.0 | 0.4 | 0.4 | 0.4 | 0.4 | 0.4 | 0.4 | 0.4 | 0.4 | 0.5 | **3.7** | **0.5** | 2.3 to 4.5 | 0.3 to 0.5 |
| *Revenue effect:* E-Verify's on-budget revenue, JCT's convention (part 2) | IMM-4.12 | 0 | 0 | 0 | −0.6 | −1.5 | −2.4 | −3.5 | −3.6 | −3.8 | −3.9 | **−19.3** | **−4.1** | −29.0 to 0.0 | −6.1 to 0.0 |
| **Immigration on the general fund, all** | | **3.2** | **11.2** | **14.0** | **13.8** | **13.6** | **12.6** | **12.1** | **13.6** | **14.5** | **15.0** | **123.4** | **15.4** | **−61.5 to 339.5** | **−8.9 to 38.9** |

(Rows are rounded; the totals are the tool's unrounded sums.)

- **The decided set:** about **+$0.12 trillion over FY2030-39 (range about −$0.06 to +$0.34 trillion) and about +$15.4 billion in FY2040 (range about −$9 to +$39 billion)** on the general fund. The ranges are summed line by line, as section 3's were, so they are wide; the lines are not independent.
- **Without E-Verify's on-budget gain** (if JCT's profit shift is not counted): about +$142.7 billion and +$19.5 billion.
- **The largest lines** are memo 6's table (health coverage for people without status from 2031, and no five-year wait for the newly legalized) and memo 1's status, against memo 3's added workers.
- **Against section 3's recommended set** (+$0.13 trillion and +$19 billion; at this tool's central values, $129.9 billion and $18.3 billion), the decided set differs by:
  - E-Verify's on-budget revenue: −$19.3 billion and −$4.1 billion;
  - E-Verify's operations: +$3.3 billion and +$0.45 billion;
  - replacing ICE: +$3.0 billion and +$0.1 billion;
  - two lines section 3 named but did not add: point 8's fee repeals (+$2.8 billion and +$0.25 billion) and the H-1B fee's tax offset (+$3.7 billion and +$0.5 billion).

  Point 7's redirection replaces a rescission that section 3 counted as unknown and unbooked, so it changes no figure. Point 1's later cutoff adds a few months of arrivals to registration, inside memo 1's range.

### Memo 5 as decided: what changed

- **Replacing ICE** (part 1 B): about $1-3 billion of transition over FY2030-34 (systems, facilities, re-credentialing and legal work), central $2 billion, and about $0.1 billion a year for the detention inspector. Both are judgment; no cost study of a DHS reorganization is in the register (section 4, "Evidence still needed"). The functions themselves cost what they cost now: the new components take over ICE's appropriations by function.
- **A's rules inside the new structure:** about +$1.1 billion over FY2030-39 (range −$3 to +$9 billion), near section 3's "about zero" (`immigration_model.detention`). The 30,000 cap saves about $1 billion a year against the base account's 41,500 beds [EV-IMM-362] at ICE's $187.48 a bed-day [EV-IMM-628], grown. Case management for about 100,000 people at $20-40 a day, less the $4.11 a day today's alternatives already cost [EV-IMM-629], spends a little more.
- **Mandatory E-Verify** (part 2 A): part 2.

## 2. E-Verify on both budgets, and Social Security

The one score of a national mandate is CBO and JCT's 2013 estimate for the Legal Workforce Act [EV-IMM-394] [EV-IMM-395]:
- about $635 million to implement over five years;
- a $30 billion higher deficit over ten years, because some work moves off the books;
- off-budget payroll revenue down $88 billion, and on-budget revenue up $49 billion. JCT's convention holds total income fixed, so wages no longer reported show up as higher business profits.

So the cost falls on Social Security's funds. The general fund gains.

| Measure | FY2030-39 | FY2040 | Basis (judgment, `immigration_path.py`, `everify()`) |
| --- | --- | --- | --- |
| On-budget revenue (general fund) | about −$19 billion (a gain; range −$29 billion to zero) | about −$4.1 billion | 2013's per-year effect, grown 4% a year, scaled by 0.3 for the unauthorized workforce left after memo 1 (about 2-3.5 million against about 8 million in 2013), phased with the tranches: 0.2, 0.45, 0.7, then full from FY2036 |
| Operations and error correction (general fund) | about +$3.3 billion | about +$0.45 billion | CBO's implementation cost grown, plus IMM-4.14's ten-day contests and wage claims |
| **Social Security's funds** (off-budget payroll revenue) | **about −$35 billion** | **about −$7.4 billion** | The same scaling on the $88 billion |
| **Unified budget** | **about +$19 billion** | **about +$3.7 billion** | Off-budget loss less on-budget gain, plus operations |

- **How to read the gain.** The general-fund gain exists only because JCT's convention moves wages that go unreported into business profits, which are taxed. It is not a sign that the mandate pays for itself. The range runs to zero for that reason, and the general fund's figure without it is reported in part 1.
- **The pool is what makes the scaling uncertain.** About 30% of eligible people may not take up status (take-up about 70% [EV-IMM-609]), and arrivals after the cutoff add to the pool over time. A larger pool scales every line in this part up together.
- **Social Security's funds also gain from legalization** (memo 1), which this dossier has not quantified on its own design. The actuaries' score of S. 744 is the only measure: +$284 billion to the funds by 2024 [EV-IMM-604]. Unauthorized workers already pay about $12 billion a year more than the benefits paid on their earnings [EV-IMM-606]. Point 13 asks the actuaries for a score of this design.

## 3. What the total leaves out

| Item | Provision | FY2030-39 | FY2040 | Basis | Firm or contingent |
| --- | --- | --- | --- | --- | --- |
| The H-1B fee itself | IMM-2.07 (IF1) | about $15 billion of receipts, retained by USCIS and a training fund | about $1.5-2 billion | Ledger IF1 [EV-IMM-577]; spent within receipts, not general-fund room; its tax offset is counted in part 1 | Firm, outside the general fund |
| CRT-5, the Article I court | IMM-3.08-3.11 (requirements) | about $0.03 trillion (range $0.02-0.06 trillion), unscored [EV-IMM-576] | — | Democratic renewal's; scored with IMM-1, as both files ask | Democratic renewal's |
| Judges above 800 and their staff | IMM-3.08 | not priced here | not priced | Set from a docket model with democratic renewal; inside CRT-5's figure or added to it, to be settled there | Open |
| Social Security's gain from legalization | IMM-1 | not quantified | not quantified | Part 2; point 13 | Off-budget |
| E-Verify's loss to Social Security | IMM-4.12 | about −$35 billion | about −$7.4 billion | Part 2 | Off-budget |
| The redirected wall money | IMM-3.07 | zero against CBO's baseline | zero | CBO's baseline projects the 2025 appropriation as spent [EV-IMM-034]; the unobligated balance in mid-2029 is unknown. Against a lapse, redirecting it costs up to that balance | Firm at zero; contingent against a lapse |
| Legalization's growth effects | IMM-1, IMM-2 | not counted | not counted | The legacy DY8 sensitivity, +$0.02 to +$0.20 trillion (`legacy-research.md`, section 1); never a pay-for | Not counted |
| State and local costs | IMM-1.20-1.35 | outside the federal total | outside | Negative at the state and local level over the long run [EV-IMM-222] | Not federal |
| SNAP's immigrant rule restored | IMM-1.27 | inside the secure floor's INC-2.01 | inside | CBO's $187 billion for the nutrition subtitle includes sec. 10108 (`dossiers/secure-floor/6-cost.md`, part 2) | Firm, counted once there |
| Health coverage of the newly legalized | IMM-1.01-1.14 | from 2031 inside care's single plan; before it, inside memo 1's line | inside | CBO's 2021 score counts marketplace credits and Medicaid among its largest sources [EV-IMM-602]. Memo 1's line removes that health share for the years after January 2031 (`immigration_model.status_fiscal`: health share 0.6 × 0.9 of the window), because the single plan's cost counts every resident already. The newly legalized are residents in care's population; only people without status sit in its 1% residual (`legacy-research.md`, finding 7), and memo 6 prices them. To confirm at the milestone review against care's population base | Firm, counted once (to confirm) |
| Medicaid and premium credits for lawfully present immigrants | IMM-1.22 | inside care's HLT-1.02 | inside | Decided and priced by care (`DEC-2026-11-10-09`) | Firm, counted once there |
| Labor-standards inspections | IMM-4.16 | inside CAP-7's Wage and Hour and OSHA lines | inside | Booked in the agency rebuild | Booked there |

## 4. Against the booked row

- **The booked IMM-1/E11 row** is −$140.0 billion over FY2030-39 and −$18.7 billion in FY2040: "S.744 CBO pattern (~$175B first decade), not rescored" [EV-IMM-570]. Section 3 showed the pattern does not transfer ("IMM-1's score, re-derived"). The decided set is a cost.
- **IMM-1's own legacy figure, re-derived.** Section 3 re-derived it as about **+$0.05 trillion** for status alone (memo 1), range −$0.05 to +$0.15 trillion. This section carries that figure unchanged as IMM-1's status line (part 1, first row), with memo 2's form at about +$4.5 billion beside it. The rest of the set is the other memos' lines.
- **USCIS in the agency rebuild.**
  - *CAP-7S:* the surge line carries a $40 billion USCIS share [EV-IMM-573], and a $6 billion asylum reserve is pending [EV-IMM-578]. This dossier's lines now carry USCIS's whole public-interest need: about $17-27 billion over FY2030-39, from memo 2's waivers, memo 4's asylum corps and memo 7's rest. So the CAP-7S share should go to zero, and the pending reserve proposal is withdrawn (point 9).
  - *CAP-7 may overlap as well.* The legacy file also gives USCIS "the same share of CAP-7's sustained increase" (`legacy/domains/domain-immigration.md`, line 120), and CAP-7's per-agency split is pro rata to the surge table. At 7% of $490 billion that would be about $34 billion over FY2030-39 (project arithmetic). Memo 7 compared its line with the surge share only. The booking should set USCIS's CAP-7 share to zero too, or show what it buys beyond this dossier's lines.

## 5. The fiscal-rule report

Each figure has one basis: federal fiscal years, $ billion, a cost positive, on the general fund, against what the budget model books (case `mixed`, main at `7512852`).

| Measure | FY2030-39 | FY2040 (permanent) |
| --- | --- | --- |
| Immigration on the general fund, as decided (part 1) | about +$123.4 billion (range −$62 to +$340 billion) | about +$15.4 billion (0.03% of GDP) |
| *of which:* spending lines | +$139.0 billion | +$19.0 billion |
| *of which:* revenue effects (the H-1B fee's offset; E-Verify's on-budget revenue) | −$15.6 billion | −$3.6 billion |
| Booked for the same purposes: IMM-1 | −$140.0 billion | −$18.7 billion |
| **Net change a booking of IMM-1 would make** | **about +$263.4 billion** | **about +$34.1 billion (0.063% of GDP)** |
| CAP-7S's USCIS share, replaced (part 4) | −$40 billion | zero (the surge line ends in FY2035) |
| **Net change with CAP-7S corrected** | **about +$223.4 billion** | **about +$34.1 billion** |
| Social Security's funds (part 2) | E-Verify about −$35 billion; legalization's gain not quantified | E-Verify about −$7.4 billion |

- **The yearly cost** is in part 1: about $2 billion in FY2030, rising to about $14 billion a year by FY2033 and $15 billion by FY2039.
- **Permanent cost from FY2040:** about **$15.4 billion a year** on the general fund, rising with the population covered and prices. Memo 6's table and memo 1's status are permanent; memo 3's added workers are a permanent gain; USCIS's surge, the restructure and the backlog work end.
- **Its share of the plan-wide margin.**
  - *The gap:* the plan-wide general-fund primary gap in FY2040 is **$4,184.7 billion short** as booked (7.73% of GDP; `agenda_gf_primary_bn`, case `mixed`; a positive figure is a shortfall).
  - *A booking of the decided set* adds about $34.1 billion, to about **$4,218.8 billion (7.79% of GDP)**: **about 0.81% of the plan-wide gap**.
  - *Immigration's whole general-fund cost* in FY2040, $15.4 billion, is **about 0.37% of the gap**. Most of the booking's effect is removing a saving the plan never had.
  - *Basis:* additive on the primary balance before interest.
- **The test years.** The costs grow with prices and the covered population, and nothing sunsets. The general fund also stops counting a saving of about $18.7 billion in FY2040 that the legacy row assumed.
- **Report, don't gate** (`DEC-2026-11-10-05`). It is a figure to report, not an error to fix. No part of it goes to Espen on its own: the choices that are mainly about money were weighed in the memos (memo 6 B, memo 1 B), and Espen decided them.

## 6. What a booking would change (proposed, not made)

Tier 3, for the lead after the milestone review (`charter/STANDARDS.md`, "Milestone review": book once, after the fixes). This PR changes nothing in `models/data/inputs/`.
1. **`models/data/inputs/ledger-bills.csv`, line 37 (IMM-1, −0.25 / −0.14 / −0.02):** replace with rows split by decision, so each part can move with its own:
   - IMM-1, status and the registry (memos 1-2): **−0.048 / +0.056 / +0.163**;
   - the eligibility table (memo 6), as an IMM-1 component or a row of its own: **+0.05 / +0.078 / +0.11**;
   - IMM-2 (memo 3): **−0.06 / −0.04 / −0.02**;
   - IMM-3 (memo 4, point 8): **+0.017 / +0.029 / +0.046**;
   - IMM-4 (memo 5): **−0.028 / −0.012 / +0.020**;
   - IMM-6 (memo 7): **+0.005 / +0.009 / +0.016**.

   The note on each row: "Re-derived in dossiers/immigration/6-cost.md (DEC-2026-11-12-07); project arithmetic bounded by CBO's 2013 and 2021 scores; not a score." The rows sum to about +$0.12 trillion; IF1's tax offset (+$3.7 billion, item 3) is on its own line, so with it the set is the $123.4 billion of part 1. Year shapes go in `fiscal-years.csv` from `tools/immigration_path.py`. The profile in `fiscal-profiles.csv` (line 37, "Net saving grows as legalized workers enter the tax base") becomes "Cost rising through the decade as statuses and coverage phase in", with rows in `models/data/budget/provisions.csv`.
2. **CAP-7S's USCIS share** ($40 billion, legacy `domain-capacity.md` line 127) to zero, and the batch 4 reserve's $6 billion USCIS proposal withdrawn (point 9). Check **CAP-7's** pro-rata USCIS share (about $34 billion if 7%, part 4) and set it to zero or state what it buys.
3. **IF1** (`ledger-revenue.csv`, line 24): from the revenue menu into the base, retained by USCIS and the training fund, with its 25% income-tax offset on the general fund as its own line (part 1).
4. **E-Verify's Social Security effect:** a line in the funds model's payroll revenue (about −$35 billion over FY2030-39, −$7.4 billion in FY2040), beside memo 1's gain once SSA's actuaries score it.
5. **`ledger-conflicts.csv`, line 28** ("CRT-5 is unscored; IMM-1 relies on it"): stays open until democratic renewal scores CRT-5 with the judge count (IMM-3.08).
6. **`ledger-dynamic.csv`, DY8** (legalization's growth effects): stays a sensitivity in no total.
7. **`votes-bills.csv`, line 38:** the vote model's IMM-1 row should reflect two bills (memo 7 part 3 B): R1's money at 51, and the immigration act in regular order. That is a vote-model change for the lead.

## 7. Sensitivities

| Input | Central | Range | Effect on FY2030-39 | Basis |
| --- | --- | --- | --- | --- |
| Memo 1's status cost | +$50.8 billion | −$50 to +$150 billion | ±$0.1 trillion | H.R. 6's pattern scaled 2-3 times and netted [EV-IMM-600]; the largest single uncertainty |
| Memo 6's table | +$77.5 billion | $50-110 billion | ±$0.03 trillion | Coverage for 1.5-3 million people without status at $3,000-5,000; the five-year wait's programs at $2-4 billion a year |
| Take-up of status | about 70% | 60-85% | Higher take-up raises memos 1 and 6 and shrinks E-Verify's pool | [EV-IMM-609] |
| Memo 3's added workers | −$40 billion | −$60 to −$20 billion | ±$0.02 trillion | About $10,000 a year per added person [EV-IMM-220] on 0.3-0.6 million |
| E-Verify's on-budget gain | −$19 billion | −$29 billion to zero | up to +$0.02 trillion | JCT's convention; the pool after memo 1 |
| The E-Verify start date | October 2032 | a year later or earlier | about ±$4 billion on the general fund (revenue) and ±$7 billion on Social Security | IMM-4.13 |
| The restructure | +$3 billion | $1.5-5 billion | small | Judgment |
| **The general fund, all** | **+$123.4 billion** | **about −$62 to +$340 billion** | | |

## 8. What each figure is

| Input | Treatment (`DEC-2026-11-10-07`) |
| --- | --- |
| Who gets status; the registry's form; the fee rule; the table's rows; the numbers in memo 3; the refugee floor; the cap; the restructure; the mandate and its protections | Commitments (decided) |
| The cutoff (signature date) and the E-Verify start test | Specified; small questions for Espen |
| The population and take-up (12-14.5 million; about 70%) | Working assumptions, from section 1 and [EV-IMM-609] |
| Every line's cost and shape | Working assumptions on outside scores, laid on fiscal years |
| The working dates (filing October 2030, ICE replaced October 2031, first tranche October 2032) | Working assumptions; each moves with the act's signature |
| The work routes' ceilings (50,000 each) | Working choice, reviewed after three years |
| E-Verify's pool after legalization (0.3) | Working assumption; study in implementation from the published counts (IMM-4.18) |
| The model's inputs (`immigration_model.INPUTS`) | Each an evidence ID, a legacy figure with its file, or a labeled assumption with a range; the judges needed (about 810, range about 615-1,120) and the USCIS backlog's years to clear (about 5.5) are outputs |
| The statement route's volume and fraud | Study in implementation (IMM-6.06's audit) |
| Social Security's effect of the whole set | Open: SSA's actuaries' score (point 13) |
| The judges IMM-3.08 needs | Open, with democratic renewal's docket model |
| The CAP-7 overlap | Open for the booking step (part 6, item 2) |
