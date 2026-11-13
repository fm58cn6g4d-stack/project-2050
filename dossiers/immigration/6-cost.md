# A new consensus on immigration: cost

Role: section 6 of the immigration dossier. It prices the provisions of `4-specification.md` on federal fiscal years against the January 2029 law. It reports the fiscal-rule effect to the financing settlement (`charter/STANDARDS.md`, "Fiscal rule in dossiers: report, don't gate", `DEC-2026-11-10-05`), and reprices memo 5 and points 1 and 7 as Espen decided them. Status: reviewed at L3 (`review-milestone.md`, #303), with the review's fix steps applied (#305, #307); the re-check was the booking (#310). On `DEC-2026-11-12-07` and `-12`. Every figure is project arithmetic, not an official score; none exists for a design like this (point 13 asks for one). **Nothing is booked here:** booking is a later step, after the milestone review, and part 6 lists the ledger rows and inputs it would change.

## Counting rules

- **Conventions.** Federal cost, nominal $ billion unless marked, against the January 2029 law (section 1, "The January 2029 baseline"), a cost positive. **On the general fund** unless a line says otherwise; Social Security's funds are reported apart (part 2).
- **Fiscal years.** FY y runs from October of y-1. The working timeline is `4-specification.md`, "Dates": filing opens about October 1, 2030 (FY2031); the single plan's first wave is January 1, 2031; E-Verify's first tranche is no earlier than October 1, 2030, on the first passing 90-day check, about July 1, 2031 (FY2031) on the working timeline (IMM-4.13, `DEC-2026-11-12-12`).
- **The model and the path.**
  - `tools/immigration_model.py` is this dossier's first, scoped immigration model (`charter/PLAN.md` 3.4). It covers USCIS's throughput and backlog with the fee and appropriation split, the courts' capacity and appointed counsel, detention at the cap against case management, and status's fiscal effect from CBO's published score. Every input traces to an evidence ID or is a labeled assumption with a range. Run: `python3 dossiers/immigration/tools/immigration_model.py`; test: `python3 dossiers/immigration/tools/test_immigration_model.py`.
  - `tools/immigration_path.py` lays the model's lines and the rest on fiscal years (run: `python3 dossiers/immigration/tools/immigration_path.py`).
  - Memo 6's health coverage, as amended, is priced on care's own path (`dossiers/care/tools/health_path.py`), through `immigration_model.care_cost_of_residual` (part 1).
  - Lines not in the model are memo 3's added workers, E-Verify and the restructure. They stay labeled judgment on outside scores, and labor-market effects stay as cited evidence (`7-validation.md`, part 2).
  - Ranges for the model's lines run all its inputs at their low and high values together. That is a bound, not a probability interval. For memo 1, the wider bound from section 3 is kept, because the model's inputs do not span the pattern's own uncertainty.
- **Spending lines and revenue effects stay apart** (`dossiers/TEMPLATE.md`, "One basis for each fiscal figure"). Two revenue effects have their own lines: the income-tax offset on the retained H-1B fee and E-Verify's on-budget revenue. Neither is added into a spending line.
- **The booked basis.** The budget model's central case (`mixed`), as `DEC-2026-11-12-08` records it: IMM-1 at −$140.0 billion over FY2030-39 and −$18.7 billion in FY2040; CAP-7S at $600 billion, of which USCIS's share is $40 billion [EV-IMM-573]. These figures are read from the model's audit lines (`legacy/sources/recovery-budget-audit.csv`), not rebuilt.
- **Each figure's status** (commitment, working assumption, open question) is in part 8.

## 1. The decided set on the general fund, by fiscal year

| Line | Provisions | 2030 | 2031 | 2032 | 2033 | 2034 | 2035 | 2036 | 2037 | 2038 | 2039 | **FY2030-39** | **2040** | Range FY2030-39 | Range 2040 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Status: tiers A and B and registration (memo 1) | IMM-1.01-1.14 | 0.0 | 1.0 | 2.0 | 3.5 | 5.1 | 5.6 | 6.6 | 8.1 | 9.1 | 9.6 | **50.5** | **10.1** | −50.0 to 150.0 | −5.0 to 20.0 |
| Records-first registry and fee waivers (memo 2) | IMM-1.05-1.09 | 0.3 | 1.9 | 1.5 | 0.7 | 0.3 | 0.2 | 0.2 | 0.2 | 0.1 | 0.1 | **5.4** | **0.1** | 2.0 to 12.9 | 0.0 to 0.3 |
| Legal immigration and the work routes (memo 3) | IMM-2.01-2.12 | −1.0 | −1.5 | −2.5 | −3.5 | −4.0 | −4.5 | −5.0 | −5.5 | −6.0 | −6.5 | **−40.0** | **−7.0** | −60.0 to −20.0 | −8.0 to −5.0 |
| Asylum, refugees, regional access, counsel (memo 4) | IMM-3.01-3.04, 3.12 | 1.8 | 2.9 | 2.9 | 3.0 | 3.1 | 3.2 | 2.5 | 2.6 | 2.6 | 2.7 | **27.2** | **2.8** | 15.7 to 44.6 | 1.5 to 4.6 |
| Judge teams above today's 753 (memo 4, part 2) | IMM-3.08 | 0.4 | 0.8 | 1.3 | 1.6 | 1.7 | 1.7 | 1.6 | 1.5 | 1.3 | 1.2 | **13.2** | **1.1** | 2.1 to 18.0 | 0.0 to 2.3 |
| Asylum fee repeals, net of the 25% offset (point 8) | IMM-3.06 | 0.3 | 0.3 | 0.3 | 0.3 | 0.2 | 0.2 | 0.2 | 0.2 | 0.2 | 0.2 | **2.8** | **0.2** | 2.0 to 5.0 | 0.1 to 0.4 |
| The detention cap and case management (memo 5, A's rules) | IMM-4.05-4.06 | 0.6 | 0.6 | 0.6 | 0.7 | 0.7 | 0.7 | 0.7 | 0.7 | 0.7 | 0.8 | **6.8** | **0.8** | −1.3 to 27.4 | −0.1 to 3.2 |
| Replacing ICE; the detention inspector (memo 5, part 1 B) | IMM-4.01-4.02, 4.09 | 0.2 | 0.7 | 0.7 | 0.5 | 0.3 | 0.1 | 0.1 | 0.1 | 0.1 | 0.1 | **3.0** | **0.1** | 1.5 to 5.0 | 0.1 to 0.3 |
| E-Verify operations and error correction (memo 5, part 2 A) | IMM-4.12-4.15 | 0.1 | 0.3 | 0.3 | 0.4 | 0.4 | 0.4 | 0.4 | 0.4 | 0.4 | 0.5 | **3.8** | **0.5** | 3.0 to 6.5 | 0.3 to 0.7 |
| The one eligibility table (memo 6, amended for health; IMM-1.15's returnees) | IMM-1.15, 1.20-1.36 | 0.0 | 3.5 | 5.8 | 7.0 | 8.1 | 9.3 | 10.7 | 12.2 | 13.8 | 15.7 | **86.1** | **16.9** | 43.2 to 158.4 | 8.0 to 31.9 |
| USCIS beyond memos 2 and 4; naturalization fees (memo 7) | IMM-6.01, IMM-5.04 | 1.5 | 1.5 | 1.5 | 1.2 | 1.2 | 0.8 | 0.5 | 0.5 | 0.5 | 0.5 | **9.8** | **0.6** | 5.6 to 17.6 | 0.3 to 1.0 |
| Wall money redirected (point 7) | IMM-3.07 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | **0.0** | **0.0** | 0.0 to 0.0 | 0.0 to 0.0 |
| **Spending lines** | | **4.3** | **12.1** | **14.5** | **15.4** | **17.0** | **17.8** | **18.5** | **21.0** | **23.1** | **24.9** | **168.6** | **26.2** | **−36.2 to 425.4** | **−2.8 to 59.7** |
| *Revenue effect:* income-tax offset on the retained H-1B fee (25%) | IMM-2.07 (IF1) | 0.0 | 0.4 | 0.4 | 0.4 | 0.4 | 0.4 | 0.4 | 0.4 | 0.4 | 0.5 | **3.7** | **0.5** | 2.3 to 4.5 | 0.3 to 0.5 |
| *Revenue effect:* E-Verify's on-budget revenue, JCT's convention (part 2) | IMM-4.12 | 0 | −0.1 | −0.8 | −1.6 | −2.5 | −3.4 | −3.5 | −3.6 | −3.8 | −3.9 | **−23.3** | **−4.1** | −34.9 to 0.0 | −6.1 to 0.0 |
| **Immigration on the general fund, all** | | **4.3** | **12.3** | **14.1** | **14.2** | **14.9** | **14.8** | **15.4** | **17.8** | **19.8** | **21.4** | **149.0** | **22.5** | **−68.8 to 429.9** | **−8.6 to 60.2** |

(Rows are rounded; the totals are the tool's unrounded sums.)

- **The decided set:** about **+$0.15 trillion over FY2030-39 (range about −$0.07 to +$0.43 trillion) and about +$22.5 billion in FY2040 (range about −$9 to +$60 billion)** on the general fund, with memo 6's health line at two-thirds of care's average use (Espen, November 13; part 7, W-1); at care's average it was +$175.1 billion and +$28.8 billion. The ranges are summed line by line, as section 3's were, so they are wide; the lines are not independent.
- **Memo 6, amended for health** (Espen, November 12, lead session). The single plan covers everyone with lawful or registered status, a filing receipt included; people with no status keep emergency care as today (IMM-1.21). Priced net:
  - *Coverage added:* only lawful residents above care's population base, that is memo 3's added immigrants (0.3-0.6 million by FY2039) and the refugees above the baseline (IMM-3.04), about 0.9 million by FY2039. On care's own path, at two-thirds of care's average newly covered person (about $13,500 in 2032; Espen, November 13, on the independent check in part 7, W-1), they cost about $53 billion over FY2030-39 and $12.7 billion in FY2040 (`immigration_model.table`, `care_cost_of_residual`, `lawful_added_cost_factor`; $79 billion and $18.9 billion at care's average). Memo 3's line nets CBO's per-person fiscal effect, which counts current-law health programs, so a small part may be counted in both; it is left in, on the high side.
  - *IMM-1.15's returnees:* about 50,000 people (range 20,000-150,000; about 3% of some 1.8 million removals in FY2025-28 [EV-IMM-659], a labeled assumption) return over FY2031-33. They are lawful residents above care's base, so their coverage is inside the figure above, about $6.5 billion over FY2030-39 and $1.0 billion in FY2040; their cases from abroad add about $0.1 billion (range $0.03-0.5 billion). In all about $6.6 billion (range about $2.6-20 billion).
  - *Coverage already counted:* the newly legalized, registered people and other lawfully present residents are already in care's population base, and care's plan cost already nets the federal Medicaid money it replaces, Emergency Medicaid included. Nothing is added for them here, and nothing is subtracted twice.
  - *Emergency care* for people with no status stays at today's cost, under the January 2029 law: not added.
  - *The five-year wait's programs:* about $2-4 billion a year (judgment), about $33 billion over FY2030-39.
  - *Residence-based coverage, for comparison:* covering the 1.5-3 million people left without status as well, as memo 6 C first read, would have added about $0.32 trillion over FY2030-39 (range $0.21-0.42 trillion) and $47 billion in FY2040 on care's path (milestone review, O-1).
- **Care's base is corrected in care's booking (not counted here).** Care's model covered the whole population except a 1% residual (about 3.55 million). Under the amended rule, people with no status are not covered: eligible people who have not yet filed (known people are assumed to file first, on their notices) and those who never file. Beyond the residual's share for status (taken as 2.25 million), care's figures counted about 7.8 million such people as covered in FY2031, 2.7 million in FY2035 and 1.7 million from FY2039, about **$430 billion over FY2030-39 (range about $210-510 billion) and $36 billion in FY2040** too high (`immigration_model.care_base_correction`). Care's booking now takes it out, less the Emergency Medicaid that keeps paying for everyone with no status (about $10 billion) and the federal uncompensated-care payment hospitals keep for their care at today's DSH-type share (about $8 billion; `DEC-2026-11-13-02`): **about −$411 billion and −$33 billion** on HLT-7's `status-rule` component (`dossiers/care/6-cost.md`, part 2b; `dossiers/care/tools/status_rule.py`, which reads this model's counts). Long-term care narrows too (IMM-1.23, `DEC-2026-11-13-01`): about −$3.6 billion and −$0.9 billion more (`dossiers/care/6bcd-cost.md`, part 2b). People who arrive without status after the act is signed would add to both.
- **Changes at the milestone review** (`review-milestone.md`), against the reviewed draft's +$132.8 billion and +$16.4 billion:
  - memo 6 as amended and priced on care's path: +$34.7 billion and +$11.7 billion;
  - case management at about 150,000 people, from today's 183,181 on alternatives [EV-IMM-171] less those who register (O-2): +$5.7 billion and +$0.7 billion;
  - counsel for the children in the court backlog (O-3): +$1.2 billion;
  - USCIS's backlog money for the year the six-month target needs (O-4): +$0.7 billion.
- **The judge teams** (IMM-3.08): about $13.2 billion over FY2030-39 and $1.1 billion in FY2040, for about 920 judges above today's 753 at about $1.5 million a team (`immigration_model.eoir`). Earlier drafts sized the corps at about 810 judges on 900 completions a judge; CRS's average of about 510 [EV-IMM-641] needs far more. *An alternative not in the total* (review A-1): after the backlog clears in FY2035, receipts need about 730 judges, below today's corps, so the added judges the model keeps until attrition are surplus. Hiring the increment on terms that end once the backlog clears saves about $5.5 billion over FY2036-39 and $1.1 billion in FY2040 (`immigration_model.term_increment`). It touches the court's tenure rules, which are democratic renewal's (CRT-5), so it goes there as a proposal.
- **Without E-Verify's on-budget gain** (if JCT's profit shift is not counted): about +$198.4 billion and +$32.9 billion.
- **Against section 3's recommended set** (+$0.13 trillion and +$19 billion), the decided set differs by the review's changes above, and by memo 5 as decided: E-Verify's on-budget revenue (−$23.3 billion and −$4.1 billion), its operations (+$3.75 billion and +$0.46 billion) and replacing ICE (+$3.0 billion and +$0.1 billion). Point 8's fee repeals (+$2.8 billion) and the H-1B fee's tax offset (+$3.7 billion) are counted here; section 3 named them without adding them.

  Point 7's redirection replaces a rescission that section 3 counted as unknown and unbooked, so it changes no figure. Point 1's later cutoff adds a few months of arrivals to registration, inside memo 1's range.

### Memo 5 as decided: what changed

- **Replacing ICE** (part 1 B): about $1-3 billion of transition over FY2030-34 (systems, facilities, re-credentialing and legal work), central $2 billion, and about $0.1 billion a year for the detention inspector. Both are judgment; no cost study of a DHS reorganization is in the register (section 4, "Evidence still needed"). The functions themselves cost what they cost now: the new components take over ICE's appropriations by function.
- **A's rules inside the new structure:** about +$6.8 billion over FY2030-39 (range −$1 to +$27 billion) (`immigration_model.detention`). The 30,000 cap saves about $1 billion a year against the base account's 41,500 beds [EV-IMM-362] at ICE's $187.48 a bed-day [EV-IMM-628], grown. Case management for about 150,000 people at a time (range 100,000-250,000) at $20-40 a day, less the $4.11 a day today's alternatives already cost [EV-IMM-629], spends more. The 150,000 starts from today's 183,181 on alternatives [EV-IMM-171] and about 35,000 more released to reach the cap, less the 35-50% who file for status and leave proceedings (IMM-1.10), plus releases under the surge rule (IMM-3.02), which have no count. The line's sign turns on that number.
- **Mandatory E-Verify** (part 2 A): part 2.

## 2. E-Verify on both budgets, and Social Security

The one score of a national mandate is CBO and JCT's 2013 estimate for the Legal Workforce Act [EV-IMM-394] [EV-IMM-395]:
- about $635 million to implement over five years;
- a $30 billion higher deficit over ten years, because some work moves off the books;
- off-budget payroll revenue down $88 billion, and on-budget revenue up $49 billion. JCT's convention holds total income fixed, so wages no longer reported show up as higher business profits.

So the cost falls on Social Security's funds. The general fund gains.

| Measure | FY2030-39 | FY2040 | Basis (judgment, `immigration_path.py`, `everify()`) |
| --- | --- | --- | --- |
| On-budget revenue (general fund) | about −$23 billion (a gain; range −$35 billion to zero) | about −$4.1 billion | 2013's per-year effect, grown 4% a year, scaled by 0.3 for the unauthorized workforce left after memo 1 (about 2-3.5 million against about 8 million in 2013), phased with the tranches from the first, about July 2031 (IMM-4.13), each covering 0.2, 0.45, 0.7 and all of that workforce; by fiscal year the coverage is about 0.05 (FY2031), 0.26, 0.51 and 0.78, then full from FY2035 (`immigration_model.everify_coverage`) |
| Operations and error correction (general fund) | about +$3.75 billion | about +$0.46 billion | CBO's implementation cost grown, plus IMM-4.14's ten-day contests and wage claims |
| **Social Security's funds** (off-budget payroll revenue) | **about −$42 billion** | **about −$7.4 billion** | The same scaling on the $88 billion |
| **Unified budget** | **about +$22 billion** | **about +$3.7 billion** | Off-budget loss less on-budget gain, plus operations |

- **How to read the gain.** The general-fund gain exists only because JCT's convention moves wages that go unreported into business profits, which are taxed. It is not a sign that the mandate pays for itself. The range runs to zero for that reason, and the general fund's figure without it is reported in part 1.
- **The pool is what makes the scaling uncertain.** About 30% of eligible people may not take up status (take-up about 70% [EV-IMM-609]), and arrivals after the cutoff add to the pool over time. A larger pool scales every line in this part up together.
- **Social Security's funds also gain from legalization** (memo 1), which this dossier has not quantified on its own design. The actuaries' score of S. 744 is the only measure: +$284 billion to the funds by 2024 [EV-IMM-604]. Unauthorized workers already pay about $12 billion a year more than the benefits paid on their earnings [EV-IMM-606]. Point 13 asks the actuaries for a score of this design.

## 3. What the total leaves out

| Item | Provision | FY2030-39 | FY2040 | Basis | Firm or contingent |
| --- | --- | --- | --- | --- | --- |
| The H-1B fee itself | IMM-2.07 (IF1) | about $15 billion of receipts, retained by USCIS and a training fund | about $1.5-2 billion | Ledger IF1 [EV-IMM-577]; spent within receipts, not general-fund room; its tax offset is counted in part 1 | Firm, outside the general fund |
| CRT-5, the Article I court | IMM-3.08-3.11 (requirements) | about $0.03 trillion (range $0.02-0.06 trillion), unscored [EV-IMM-576] | — | Democratic renewal's; scored with IMM-1, as both files ask | Democratic renewal's |
| CRT-5's own structure beyond the judge teams | IMM-3.11 | inside CRT-5's figure | — | The judge teams that clear the backlog are now priced here (part 1, IMM-3.08, about $13 billion). CRT-5's legacy $0.03 trillion should be re-scored without them, so the judges are counted once | To settle with democratic renewal |
| Social Security's gain from legalization | IMM-1 | not quantified | not quantified | Part 2; point 13 | Off-budget |
| E-Verify's loss to Social Security | IMM-4.12 | about −$42 billion | about −$7.4 billion | Part 2 | Off-budget |
| The redirected wall money | IMM-3.07 | zero against CBO's baseline | zero | CBO's baseline projects the 2025 appropriation as spent [EV-IMM-034]; the unobligated balance in mid-2029 is unknown. Against a lapse, redirecting it costs up to that balance | Firm at zero; contingent against a lapse |
| Legalization's growth effects | IMM-1, IMM-2 | not counted | not counted | The legacy DY8 sensitivity, +$0.02 to +$0.20 trillion (`legacy-research.md`, section 1); never a pay-for | Not counted |
| State and local costs | IMM-1.20-1.35 | outside the federal total | outside | Negative at the state and local level over the long run [EV-IMM-222] | Not federal |
| SNAP's immigrant rule restored | IMM-1.27 | inside the secure floor's INC-2.01 | inside | CBO's $187 billion for the nutrition subtitle includes sec. 10108 (`dossiers/secure-floor/6-cost.md`, part 2) | Firm, counted once there |
| Health coverage of the newly legalized | IMM-1.01-1.14 | from 2031 inside care's single plan; before it, inside memo 1's line | inside | CBO's 2021 score counts marketplace credits and Medicaid among its largest sources [EV-IMM-602]. Memo 1's line removes that health share for the years after January 2031 (`immigration_model.status_fiscal`: health share 0.6 × 0.9 of the window), because care's model already covers them: it covers the whole Social Security area population [EV-CAR-051] except a 1% residual (`sp_residual_unins`, about 3.55 million), and the newly legalized are not in the residual | Firm, counted once (confirmed at the milestone review, F-3) |
| Health and long-term care coverage of people with no status | IMM-1.21, IMM-1.23 | not added: emergency care as today (EMTALA, Emergency Medicaid), under the January 2029 law | not added | Memo 6 as amended for health (Espen, November 12, lead session). Care's base counted some of these people as covered beyond its 1% residual; care's booking corrects it (part 1), not counted here | Firm at today's cost |
| Health coverage of lawful residents above care's base | IMM-1.21 | inside memo 6's line (part 1): about $79 billion | about $18.9 billion | Memo 3's added immigrants and the refugees above the baseline, on care's own path | Counted once here |
| Medicaid and premium credits for lawfully present immigrants | IMM-1.22 | inside care's HLT-1.02 | inside | Decided and priced by care (`DEC-2026-11-10-09`) | Firm, counted once there |
| Labor-standards inspections | IMM-4.16 | inside CAP-7's Wage and Hour and OSHA lines | inside | Booked in the agency rebuild | Booked there |

## 4. Against the booked row

- **The booked IMM-1/E11 row** is −$140.0 billion over FY2030-39 and −$18.7 billion in FY2040: "S.744 CBO pattern (~$175B first decade), not rescored" [EV-IMM-570]. Section 3 showed the pattern does not transfer ("IMM-1's score, re-derived"). The decided set is a cost.
- **IMM-1's own legacy figure, re-derived.** Section 3 re-derived it as about **+$0.05 trillion** for status alone (memo 1), range −$0.05 to +$0.15 trillion. This section carries that figure unchanged as IMM-1's status line (part 1, first row), with memo 2's form at about +$5.4 billion beside it. The rest of the set is the other memos' lines.
- **USCIS in the agency rebuild.**
  - *CAP-7S:* the surge line carries a $40 billion USCIS share [EV-IMM-573], and a $6 billion asylum reserve is pending [EV-IMM-578]. This dossier's lines now carry USCIS's whole public-interest need: about $17-27 billion over FY2030-39, from memo 2's waivers, memo 4's asylum corps and memo 7's rest. So the CAP-7S share should go to zero, and the pending reserve proposal is withdrawn (point 9).
  - *CAP-7 may overlap as well.* The legacy file also gives USCIS "the same share of CAP-7's sustained increase" (`legacy/domains/domain-immigration.md`, line 120), and CAP-7's per-agency split is pro rata to the surge table. At 7% of $490 billion that would be about $34 billion over FY2030-39 (project arithmetic). Memo 7 compared its line with the surge share only. The booking should set USCIS's CAP-7 share to zero too, or show what it buys beyond this dossier's lines.

## 5. The fiscal-rule report

Each figure has one basis: federal fiscal years, $ billion, a cost positive, on the general fund, against what the budget model books (case `mixed`, `DEC-2026-11-12-08`).

| Measure | FY2030-39 | FY2040 (permanent) |
| --- | --- | --- |
| Immigration on the general fund, as decided (part 1) | about +$149.0 billion (range −$69 to +$430 billion) | about +$22.5 billion (0.042% of GDP) |
| *of which:* spending lines | +$168.6 billion | +$26.2 billion |
| *of which:* revenue effects (the H-1B fee's offset; E-Verify's on-budget revenue) | −$19.5 billion | −$3.6 billion |
| Booked for the same purposes: IMM-1 | −$140.0 billion | −$18.7 billion |
| **Net change a booking of IMM-1 would make** | **about +$289.0 billion** | **about +$41.2 billion (0.076% of GDP)** |
| CAP-7S's USCIS share, replaced (part 4) | −$40 billion | zero (the surge line ends in FY2035) |
| **Net change with CAP-7S corrected** | **about +$249.0 billion** | **about +$41.2 billion** |
| Care's base, corrected for people with no status (part 1; booked in care's HLT-7 and HLT-9, with Emergency Medicaid and hospitals' uncompensated-care share kept) | about −$414 billion | about −$34 billion |
| Social Security's funds (part 2) | E-Verify about −$42 billion; legalization's gain not quantified | E-Verify about −$7.4 billion |

- **The yearly cost** is in part 1: about $4 billion in FY2030, rising to about $15 billion a year by FY2032 and $27 billion in FY2039.
- **Permanent cost from FY2040:** about **$22.5 billion a year** on the general fund ($28.8 billion at care's average use), rising with the population covered and prices. Memo 6's table and memo 1's status are permanent; memo 3's added workers are a permanent gain; USCIS's surge, the restructure and the backlog work end. The FY2040 judge line ($1.1 billion) is the surplus A-1 describes, not a lasting need.
- **Its share of the plan-wide margin.**
  - *The gap:* the plan-wide general-fund primary gap in FY2040 is **$4,184.7 billion short** as booked (7.73% of GDP; `agenda_gf_primary_bn`, case `mixed`; a positive figure is a shortfall).
  - *A booking of the decided set* adds about $47.4 billion, to about **$4,232.1 billion (7.81% of GDP)**: **about 1.1% of the plan-wide gap**.
  - *Immigration's whole general-fund cost* in FY2040, $28.8 billion, is **about 0.69% of the gap**. About two-fifths of the booking's effect is removing a saving the plan never had.
  - *Care's base:* care's booking corrects it for people with no status (health and long-term care), and the plan-wide gap falls by about $34 billion in FY2040, from about $4,275 billion to $4,240 billion short (case `mixed`, after immigration's booking in #310), hospitals' uncompensated-care payment (`DEC-2026-11-13-02`) included.
  - *Memo 6's health line at two-thirds* (Espen, November 13), rebooked in one step with the secure floor's INC-4 rescoping: the plan-wide FY2040 gap goes from $4,256.6 billion to **$4,245.4 billion short** (7.84% of GDP), $11.3 billion less, of which $6.3 billion is this line and $5.0 billion INC-4. Immigration's whole general-fund cost, $22.5 billion in FY2040, is then **about 0.53% of the gap**.
  - *Basis:* additive on the primary balance before interest.
- **The test years.** The costs grow with prices and the covered population, and nothing sunsets. The general fund also stops counting a saving of about $18.7 billion in FY2040 that the legacy row assumed.
- **Report, don't gate** (`DEC-2026-11-10-05`). It is a figure to report, not an error to fix. The one choice here that was mainly about money, coverage for people without status, went to Espen at the milestone review and is decided (memo 6 amended for health, Espen, November 12, lead session).

## 6. What a booking would change (proposed, not made)

Tier 3, for the lead after the milestone review (`charter/STANDARDS.md`, "Milestone review": book once, after the fixes). This PR changes nothing in `models/data/inputs/`.
1. **`models/data/inputs/ledger-bills.csv`, line 37 (IMM-1, −0.25 / −0.14 / −0.02):** replace with rows split by decision, so each part can move with its own:
   - IMM-1, status and the registry (memos 1-2): **−0.048 / +0.056 / +0.163**;
   - the eligibility table (memo 6, amended for health), as an IMM-1 component or a row of its own: **+0.049 / +0.112 / +0.158**;
   - IMM-2 (memo 3): **−0.06 / −0.04 / −0.02**;
   - IMM-3 (memo 4 with the judge teams, point 8): **+0.020 / +0.043 / +0.068**;
   - IMM-4 (memo 5, spending only): **+0.003 / +0.014 / +0.039**;
   - E-Verify's on-budget revenue (JCT's convention), a revenue row of its own, not inside IMM-4 (counting rules): **−0.035 / −0.023 / 0.0**;
   - IMM-6 (memo 7): **+0.006 / +0.010 / +0.018**.

   The note on each row: "Re-derived in dossiers/immigration/6-cost.md (DEC-2026-11-12-07); project arithmetic bounded by CBO's 2013 and 2021 scores; not a score." The rows sum to about +$0.18 trillion; IF1's tax offset (+$3.7 billion, item 3) is on its own line, so with it the set is the $175.1 billion of part 1. Care's base correction for people with no status (part 1) is the health booking's, not a row here. Year shapes go in `fiscal-years.csv` from `tools/immigration_path.py`. The profile in `fiscal-profiles.csv` (line 37, "Net saving grows as legalized workers enter the tax base") becomes "Cost rising through the decade as statuses and coverage phase in", with rows in `models/data/budget/provisions.csv`.
2. **CAP-7S's USCIS share** ($40 billion, legacy `domain-capacity.md` line 127) to zero, and the batch 4 reserve's $6 billion USCIS proposal withdrawn (point 9). Check **CAP-7's** pro-rata USCIS share (about $34 billion if 7%, part 4) and set it to zero or state what it buys.
3. **IF1** (`ledger-revenue.csv`, line 24): from the revenue menu into the base, retained by USCIS and the training fund, with its 25% income-tax offset on the general fund as its own line (part 1).
4. **E-Verify's Social Security effect:** a line in the funds model's payroll revenue (about −$42 billion over FY2030-39, −$7.4 billion in FY2040), beside memo 1's gain once SSA's actuaries score it.
5. **`ledger-conflicts.csv`, line 28** ("CRT-5 is unscored; IMM-1 relies on it"): stays open until democratic renewal scores CRT-5 with the judge count (IMM-3.08).
6. **`ledger-dynamic.csv`, DY8** (legalization's growth effects): stays a sensitivity in no total.
7. **`votes-bills.csv`, line 38:** the vote model's IMM-1 row should reflect two bills (memo 7 part 3 B): R1's money at 51, and the immigration act in regular order. That is a vote-model change for the lead.

**Booked** (immigration booking, `models/tools/immigration_booking.py`; `DEC-2026-11-12-17` to `-19`). IMM-1 is booked as six components on this section's path (+$195 billion of spending over FY2030-39, the table taking the ledger's $1 billion rounding), with E-Verify's on-budget revenue (IMM-EV) and the H-1B fee's offset (IF1T) as base-revenue rows. CAP-7S's and CAP-7's USCIS shares come out pro rata: the recovery budget scales both to their adopted amounts ($0.105 trillion and $0.3 trillion, `recovery-adoption.json`), so the share removed is about $28 billion over FY2030-39 and $2.8 billion in FY2040, not the legacy $40 billion and $34 billion part 4 names. The plan-wide FY2040 general-fund primary gap (case `mixed`) goes from $4,229.9 billion (7.81% of GDP, after the secure floor's booking) to **$4,274.6 billion (7.89%)**, +$44.7 billion; over FY2030-39 the booking adds about $288 billion. **Rebooked** with memo 6's health line at two-thirds of care's average use (Espen, November 13; part 7, W-1): the table component falls from $112.5 billion to $86.5 billion over FY2030-39 (with the ledger's rounding; $86.1 billion on the path) and from $23.2 billion to $16.9 billion in FY2040, IMM-1's ledger row from 0.195 to 0.169 (range −0.036 to 0.425), and immigration on the general fund from $175.1 billion and $28.8 billion to $149.0 billion and $22.5 billion. Votes (`votes-bills.csv`, two bills) and SSA's funds line for E-Verify (about −$42 billion) are not booked: the first is the vote model's, the second waits on the funds model's payroll line.

## 7. Sensitivities

| Input | Central | Range | Effect on FY2030-39 | Basis |
| --- | --- | --- | --- | --- |
| Memo 1's status cost | +$50.5 billion | −$50 to +$150 billion | ±$0.1 trillion | H.R. 6's pattern scaled 2-3 times and netted [EV-IMM-600]; the largest single uncertainty |
| Judge teams (IMM-3.08) | +$13.2 billion | $2-18 billion | ±$0.01 trillion | Completions a judge (510; 450-750) [EV-IMM-641] and the team cost ($1.31-2.45 million) [EV-IMM-644] [EV-IMM-645]; a slower ramp lowers the decade's cost but clears the backlog later |
| Memo 6's table, amended for health | +$86.1 billion | $43-158 billion | −$0.04 to +$0.07 trillion | Lawful residents above care's base (0.3-0.6 million added immigrants, the refugees and 20,000-150,000 returnees under IMM-1.15) on care's path at two-thirds of its average use (Espen, November 13), 0.4 of it (the marginal-cost study) as the low end and care's average as the high; the five-year wait's programs at $2-4 billion a year |
| Take-up of status | about 70% | 60-85% | Higher take-up raises memos 1 and 6 and shrinks E-Verify's pool | [EV-IMM-609] |
| Memo 3's added workers | −$40 billion | −$60 to −$20 billion | ±$0.02 trillion | About $10,000 a year per added person [EV-IMM-220] on 0.3-0.6 million |
| E-Verify's on-budget gain | −$23 billion | −$35 billion to zero | up to +$0.02 trillion | JCT's convention; the pool after memo 1 |
| The E-Verify start date | about July 2031 (the first passing 90-day check) | from October 2030 to a year later | about ±$4 billion on the general fund (revenue) and ±$7 billion on Social Security | IMM-4.13 |
| The restructure | +$3 billion | $1.5-5 billion | small | Judgment |
| Case management (memo 5) | 150,000 at a time | 100,000-250,000 | −$5 to +$10 billion | Today's 183,181 [EV-IMM-171], less registrants, plus surge releases |
| **The general fund, all** | **+$149.0 billion** | **about −$69 to +$430 billion** | | |

### Independent checks of the three judgment lines (milestone review W-1)

Each line was checked against one published source from a publisher other than CBO and other than the dossier's own models. None of these checks changes the booking (`DEC-2026-11-12-17` to `-19`); the one that moves a number is reported for the lead.

| Line | Source | Verdict | What it says |
| --- | --- | --- | --- |
| Memo 3, about $10,000 a year of deficit reduction per added person (−$40 billion) | Penn Wharton Budget Model, 2024 [EV-IMM-660] | **Holds, on the cautious side** | PWBM scores exempting immigrants with advanced STEM degrees from the green-card limits at −$129 billion over 2025-2034, with the population up about 825 thousand by 2034. Even if all of that end-of-decade population were present for all ten years (the population in fact ramps up from about 0.2 million), that is at least about $15,000 a person-year (project arithmetic), above memo 3's $10,000. The cohort is higher-skilled and PWBM counts taxes on the larger labor force, as CBO's surge score does; memo 3's mix includes family numbers and children, which bring less, so $10,000 stays a reasonable blend and no check supports a figure above it. |
| Memo 6, a lawful added person at care's average newly covered person (about $13,500; factor 1.0, range 0.5-1.0) | KFF, 2024 [EV-IMM-661]; Kaushal and Muchomba, 2023 [EV-IMM-662] | **Qualifies, and moved the central line down: booked at two-thirds (Espen, November 13)** | Immigrants' average health spending is about two-thirds of U.S.-born citizens' ($4,875 against $7,277, 2021). The marginal cost of insuring a low-income immigrant adult is about $3800 a year against $9428 for a U.S.-born adult, a ratio of about 0.40. Both point below care's average, so the central factor of 1.0 sits at the top of what the evidence supports and the range's 0.5 low end is a little above the lowest estimate. See "What the check does to the figure" below. |
| Memo 1, status cost +$50.5 billion (H.R. 6 scaled 2-3 times, netted) | Bipartisan Policy Center, about 2017 [EV-IMM-663]; BPC's 2013 scenarios already in the register [EV-IMM-611] | **Holds in sign; the size stays judgment** | BPC, which favors legalization, accepts that legalizing large numbers of people costs more than the baseline in which they keep working unauthorized, which is the baseline here (section 1). Its 2013 model has legalization with E-Verify saving $10 billion in the first decade and costing about $150 billion over twenty years: a first decade near zero, rising later, consistent with the −$50 billion low end of memo 1's range. No independent score of a status bill this broad exists, so the scaling from H.R. 6 [EV-IMM-600] is not independently checked and stays "the largest single uncertainty" (above). |

**What the check does to the figure (memo 6).** At the central count of lawful added persons (memo 3's 0.45 million by FY2039 and the refugees above the baseline), `immigration_model.table` gives, for the memo 6 line as a whole:

| Cost factor against care's average | FY2030-39 | FY2040 | Change against care's average, $112.2 billion and $23.2 billion |
| --- | --- | --- | --- |
| 1.0 (booked until November 13) | $112.2 billion | $23.2 billion | none |
| **0.67 (KFF's all-immigrant ratio; booked, Espen, November 13)** | $86.1 billion | $16.9 billion | −$26.1 billion; −$6.3 billion |
| 0.5 (the model's low end) | $72.6 billion | $13.7 billion | −$39.6 billion; −$9.5 billion |
| 0.40 (the marginal-cost ratio) | $64.7 billion | $11.8 billion | −$47.5 billion; −$11.4 billion |

All three alternatives lie inside the line's stated range ($49-158 billion), so the range holds; at KFF's ratio the central value would be about $26 billion lower over FY2030-39 and $6.3 billion lower in FY2040 (about 0.15% of the FY2040 plan-wide gap of roughly $4,275 billion). Reasons to stay near 1.0: the surveys under-represent recent immigrants (KFF says so), the single plan has lower cost sharing than today's coverage (more use), and the marginal figure is for low-income adults only and rests on coefficients that are not statistically significant for immigrants. Espen chose two-thirds on November 13, and it is booked (part 6): the model's result, −$26.1 billion over FY2030-39 and −$6.3 billion in FY2040, is the estimate above. The reasons to stay near 1.0 are why care's average stays the range's high end.

## 8. What each figure is

| Input | Treatment (`DEC-2026-11-10-07`) |
| --- | --- |
| Who gets status; the registry's form; the fee rule; the table's rows; the numbers in memo 3; the refugee floor; the cap; the restructure; the mandate and its protections | Commitments (decided) |
| The two cutoffs and the E-Verify start rule | Commitments (`DEC-2026-11-12-12`); the first passing check's date is a working assumption |
| The population and take-up (12-14.5 million; about 70%) | Working assumptions, from section 1 and [EV-IMM-609] |
| Lawful residents above care's base (memo 3's added immigrants, refugees) and their cost against care's average (two-thirds, range 0.4-1.0; Espen, November 13); the residual's share for people with no status (2.25 million) | Working assumptions; the cost ratio now has two independent checks (KFF, Kaushal and Muchomba [EV-IMM-661] [EV-IMM-662]) on which Espen set the central factor at two-thirds (part 7, W-1), and the counts come from the first filings |
| Every line's cost and shape | Working assumptions on outside scores, laid on fiscal years |
| The working dates (filing October 2030, ICE replaced October 2031, E-Verify's first tranche about July 2031) | Working assumptions; each moves with the act's signature |
| The work routes' ceilings (50,000 each) | Working choice, reviewed after three years |
| E-Verify's pool after legalization (0.3) | Working assumption; study in implementation from the published counts (IMM-4.18) |
| The model's inputs (`immigration_model.INPUTS`) | Each an evidence ID, a legacy figure with its file, or a labeled assumption with a range; the judges needed (about 1,670 in all, 920 added; range about 860-2,400 in all) and the USCIS backlog's years to clear (about 5.5) are outputs |
| The statement route's volume and fraud | Study in implementation (IMM-6.06's audit) |
| Social Security's effect of the whole set | Open: SSA's actuaries' score (point 13) |
| The judges IMM-3.08 needs | Working assumption from the first model (about 1,670 in all); a fuller docket model with democratic renewal |
| The CAP-7 overlap | Open for the booking step (part 6, item 2) |
