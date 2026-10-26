# Recovery and Solvency budget

Exploratory total-federal-budget analysis, October 26, 2026. Source branch
`codex/strategic-review`, commit `348d6ae3bcdbea06d4c58e889b6be5b42c6e1b7a`;
remote main verified at `beeba090020b7916f8ed08bcff36161fb70d1e69`. Full EDU-9B
scope is adopted. This package **does not adopt** tax rates, spending cuts, a
credit, transfers or a relaxation of D3/D4. Read the
[assessment](../../../sources/recovery-and-solvency-budget.md).

## Reproduce

Python 3.9+, standard library; the common suite also requires Node.js. From root:

```bash
bash index/tools/run-all.sh --write
python3 -W ignore::ResourceWarning index/tools/recovery-budget/test_model.py
python3 -W ignore::ResourceWarning index/tools/recovery-budget/model.py --output-dir /tmp/recovery-budget-check
sha256sum -c index/tools/recovery-budget/MANIFEST.sha256
```

The common runner produces this supplement after the historical comparisons.
Standalone runs require `build/ledger.json`, `build/fiscal-model.json` and
`build/moving-america.json`. They default to `build/recovery-budget/` and do not
overwrite canonical inputs. The common runner copies the generated Markdown,
JSON and paths CSV into `index/`; the component and audit CSVs go in `sources/`.
`assumptions.json` contains source anchors, adopted-scope boundaries and authored
scenario parameters. JSON retains annual fund paths and sensitivities. The audit
CSV reconciles each change in receipts and primary outlays. Tests establish
accounting consistency, not forecast validity.

## Education: what was actually reconciled

The source session's seven component anchors, rather than its aggregate anchors,
are geometrically interpolated separately. They sum to $441B in 2049; the source
aggregate says $442B. No eighth component is invented. Separate interpolation
gives $2.572T in 2030–39 versus the preceding aggregate interpolation's $2.602T.

For meals, Title I-A and IDEA section 611, these are **gross spending targets**.
Assigned current-law spending is subtracted to calculate the new federal
increment. Source session language calling IDEA totals an “increase” is
inconsistent with its calculation of a percentage of average per-pupil spending.
The module treats those values as total federal section 611 funding.

| Assigned current law | Observation | Scope and projection assumption |
| --- | --- | --- |
| Child nutrition | FY2025 $147.9B total food assistance × rounded 22% child-nutrition share = $32.538B | USDA ERS; includes NSLP, breakfast, CACFP, summer meals/EBT and related child-nutrition spending, not SNAP/WIC. Rounded-share proxy, not an exact Treasury account series |
| Title I-A | FY2026 $18.426802B | CRS R45977, Table 1; appropriation used as a steady-state outlay proxy |
| IDEA section 611 | FY2026 $14.233714B recurring | CRS R41833, Table 1: Part B $14.777314B minus section 619 recurring $0.420B, section 619 supplement $0.0161B and section 611 supplement $0.1075B. Rounded published values; Parts C/D remain outside |
| Existing care, retained outside in reference | FY2026 CCDF $12.381B + Head Start $12.357B + PDG $0.315B = $25.053B | Consolidation variant moves this same spending into the fund and out of the GF, without changing benefits or consolidated cost. CCDBG is already inside CCDF; never add it again |

The reference grows these observations 3% annually to each model year; 2% and 4%
variants are retained. That is **not a CBO program baseline**. Appropriations are
not equivalent to that year's cash outlays, future population and indexing differ
by program, and USDA's share is rounded. This pass verifies the accounting
boundary and independently anchors its starting levels; it does not establish an
exact current-law account forecast.

The care anchors are provisionally the **incremental expansion above retained
CCDF/Head Start/PDG**. The $12B 2030 care anchor cannot include all existing
programs, already about $25B in FY2026. Conversely, the source does not identify
all spending displaced by new care entitlements. If those programs are replaced,
their overlap must be resolved; this increment convention is not a verified
score of the entire care system. Teacher/PARA grants are new spending; existing
Title II/SEED are not automatically subtracted because different purposes do not
prove duplication. Their narrower overlaps remain open.

The old EDU-1 row contains $0.08T Title I and $0.25T IDEA; split its annual profile
in that proportion. Together with FAM-2 $0.60T, EDU-3 $0.27T and EDU-4 $0.03T,
this moves $1.230T of prior agenda increments. Do not add those again. Negative
changes relative to an old component are retained and flagged. A separate upper
sensitivity preserves every old component's annual increment, adding $23.1B in
2030–39; it is not automatic policy adoption or evidence that an old temporary
pipeline profile should continue forever.

The exact identity, by component and year, is:

`full fund = assigned current law + old agenda increment + change over old agenda`.

The last term can be negative for an individual component/year. For the reference
window it is $0.488T; varying current-law growth gives $0.408–0.562T. This range
does not include all benefit-cost, participation or wage uncertainty. Consolidating
existing care increases both the full fund and current-law transfers by $0.323T,
to $2.895T and $1.177T, leaving $0.488T unchanged. Keeping the same tax rate after
that consolidation would require different GF grants; a fund boundary is not a
source of consolidated savings.

## Total federal budget and fund bridge

The existing `fiscal-baseline.csv` already contains current revenue, spending and
debt: CBO February 2026 economic/budget vintages, preliminary FY2026 totals and
the repository's subsequent tariff adjustments. Its provenance and limitations
remain in `fiscal-data.py` and `fiscal-long-term-model.md`. Existing categories
are retained, including Social Security, Medicare, other health, other mandatory,
defense, nondefense and interest. No new federal baseline is invented.

The old fiscal model's displayed `rev` remained baseline revenue while signed
program costs **and taxes** changed displayed `out`. This supplement instead
classifies revenue-category rows as receipts and spending-category rows as
outlays, then accumulates interest on the net primary change. It replaces the
old SS-1 net row completely with annual fund-engine receipts and benefit changes,
beginning in 2031. It adds the actual paid-leave primary balance, previously
assumed zero, and HI's H1a receipts and Part A share of HLT-6 savings, previously
outside consolidated fiscal totals. The existing HI funding gap is not a new
program cost. Estate revenue is not counted a second time for education.

For each year:

* Total revenue = adjusted current-law revenue + separately recorded changes.
* Total primary outlays = current-law primary outlays + recorded changes.
* Total deficit = primary outlays + total net interest − revenue.
* Public debt = adjusted current-law public debt + accumulated program change.
* GF program balance = consolidated program balance minus the education, SS, HI
  and leave fund primary balances. Grant spending is in the GF and grant receipts
  are in the fund; both cancel in consolidation.

This GF measure is **the agenda's incremental GF balance**, not a reconstructed
current-law Treasury general-fund statement. It excludes trust-fund interest and
loan principal transactions; the latter are financing, not external receipts.
Fund interest is an internal transfer. Consolidated interest is calculated once,
from public-debt changes. Reserve depletion is reported, never silently treated
as legal authority to borrow or reduce benefits.

SSA fund calculations keep their own Trustees economics. The fiscal bridge
multiplies fund dollar changes by CBO GDP / SSA GDP in each year, preserving their
share of GDP; the no-translation sensitivity shows the effect. This is a declared
translation between vintages, not a harmonized actuarial forecast. SS joint
interaction remains an authored −0.34 payroll-point adjustment; OASI and DI are
not separately certified. HI's summary-rate interpolation misses the reported
current-law actuarial balance by about 0.08 payroll point. The HI grant is
therefore a scenario, not an actuarially exact closer.

Payroll income-tax offsets are explicit: 12.5% of education receipts, leave
receipts and new SS covered-earnings/rate receipts. This is an allowance, not a
JCT score. No additional blanket offset is applied to SSA's NII/pass-through
bases, already behaviorally adjusted. Their interactions with new AGI taxes,
NIIT, employer deductions and existing GX/TSX remain uncertain. The 20% new-income
yield haircut is applied **only to the new AGI contribution**, in addition to
preserving existing GX/TSX. The downside raises it to 40%.

## Where the total-budget view is still approximate

Several old rows net their own dedicated receipts against spending. To avoid
showing carbon dividends and similar uses as costless, the supplement grosses up
both sides for C1/C2/C3, PS1, MF1, IF1 and MR1–MR6. This is an **equal matched-flow
presentation proxy**, not a new deficit saving. Carbon uses the existing fee
profile through 2039 and an explicit subsequent fade. Other channels use the
recorded window total and a GDP profile. Transport uses only recorded new net
receipts, including its income/payroll offset, not existing HTF receipts again.

Annual spending/receipt lags, transportation budget authority versus outlays,
existing HTF baseline overlap, trapped account surpluses, refundable-credit
classification and the exact agency budget crosswalk remain incomplete. Thus
the totals are a usable, reproducible federal budget **scenario**, not official
gross Treasury totals or a completed account-level budget. The matched proxy
affects reported government size, not the calculated deficit. The downside net
loss is separately identified rather than falsely classified entirely as taxes.
Neither state/local budgets nor every other federal trust fund is reconstructed.
Do not infer that D4's all-fund 75-year requirement is satisfied: HTF still stops
in 2046 and total public debt in 2056.

## Tax, credit, stress and household assumptions

CBO/JCT's December 2024 option supplies a 2034 yield of $180.4B for one AGI point
above indexed $20k/$40k and $133.9B for two points above indexed $100k/$200k.
The model converts the latter to $66.95B per point, scales both with GDP, then
applies the new-yield haircut. Thresholds are 2025 dollars, indexed thereafter;
the tiers are additive above the higher threshold. This is an old-law scoring
anchor; it is not valid to describe the result as a current-law joint score.
Large-rate extrapolation is particularly uncertain. The solver exploits only
the model's static linearity and tests **every year 2045–56**, not just an endpoint.

The $300 annual adult credit is refundable, employment/family-neutral and CPI
indexed, with six months in FY2029. All resident adults are provisionally included;
population 346M × 78% in 2030, growing 0.4%, comes from existing fund assumptions.
Those are demographic proxies, not eligibility microdata. Nonfiler enrollment,
territorial treatment and payment delays are not scored. The $1,500 alternative
costs five times as much; neither is an adopted benefit. The previous unallocated
20%-of-education-payroll protection reserve is **not** added again.

The household diagnostic replaces old education, SS, leave and AI rows with
the corresponding scenario flows, retains unchanged instruments on their older
incidence schedules and uses existing distribution keys. Broad AGI tax shares
1/5/12/24/58% are authored; high-tier uses the existing surtax key. Employer payroll
shares fall on workers over time. Unallocated tax offsets and delivery-contingency
benefits are not credited to households. This is not microdata or a D3 certificate;
within-quintile, family structure, disability, nonworker and self-employment
differences require the next joint distributional analysis.

The downside combines +15% education costs, slower payroll growth, faster long-run
education costs, a recession, half the HI health savings, weaker health/G8/high-end
receipts and half post-2039 G11. A separate +1 point interest case applies to
**all public debt**, using BASE-R1 plus program interest. SS/leave demographics
are not shocked in these cases; this is not a comprehensive macro stress test.

## External observations and source locations

Accessed October 26, 2026. CRS pages were read through EveryCRSReport mirrors;
Congress.gov access was unavailable. All new observed fiscal anchors are in
`assumptions.json`; projections and calculations are authored.

1. [CRS R45977, July 9, 2026, Table 1](https://www.everycrsreport.com/files/2026-07-09_R45977_e4e601012053fcdd1e41fb43a43cc220e72ca7fe.html): ESEA appropriations, including Title I-A, Title II-A and SEED.
2. [CRS R41833, October 22, 2026, Table 1 and supplement notes](https://www.everycrsreport.com/files/2026-10-22_R41833_88e7d93e81fb4a06b439f795a80ec883f561baef.html): IDEA appropriations and recurring/supplemental boundaries.
3. [CRS R48970, May 28, 2026, FY2026 program tables](https://www.everycrsreport.com/reports/R48970.html): Head Start, CCDBG, PDG and ED accounts. ED departmental management alone excludes student-aid administration; it is not the entire agency operating baseline.
4. [HHS, CCDF final rule, May 12, 2026, background](https://www.federalregister.gov/documents/2026/05/12/2026-09382/restoring-flexibility-in-the-child-care-and-development-fund-ccdf): $12.381B FY2026 CCDF. CCDBG must not be counted again.
5. [USDA ERS, August 31, 2026, food-assistance composition chart](https://www.ers.usda.gov/data-products/chart-gallery/58388): $147.9B and 22% child nutrition. Exact underlying FNS account tables were unavailable; rounded-share approximation disclosed above.
6. [CBO, December 12, 2024, option 60938, JCT table](https://www.cbo.gov/budget-options/60938): the two AGI contribution anchors. It predates the current baseline.
7. [CRS IF13024, March 12, 2026, enacted funding](https://www.everycrsreport.com/reports/IF13024.html): NOAA $6.1B appropriations, $6.6B discretionary direct obligations, different concepts.
8. [IRS SOI individual returns tables](https://www.irs.gov/statistics/soi-tax-stats-individual-income-tax-returns-complete-report-publication-1304-basic-tables-part-1): 2023 Table 1.2 workbook identified but not successfully ingested. No claim of IRS microdata or a priced targeted-credit score is made.

Internal evidence: `education-transforming-education-act-analysis-and-trust-fund.md`
(seven-component table and pre-K shares), `domain-education.md` (old $0.08/$0.25T
split), `domain-capacity.md` (explicitly judgmental allocations), existing
SSA/HI input CSVs and source notes, `fiscal-recovery-inventory.csv` (148-row agenda
inventory), `fiscal-redesign-and-participation-2026-10-26.md` (climate experiments).

## Package integrity

`MANIFEST.sha256` covers authored code, assumptions, notes, assessment and generated
outputs. JSON also records hashes of its immediate build inputs. The prior fiscal
CSV/input vintage is unchanged; notices identify this successor where the earlier
aggregate education reconciliation is superseded. The public product is not
rebuilt or deployed. Next decision is the financing/protection design, not a merge
or automatic selection of a modeled tax schedule.
