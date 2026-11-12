# A secure floor for every household: what the legacy research and models found

Role: the restatement of the legacy project's child-poverty, paid leave, Social Security and participation research and model results that the secure floor builds on, with every figure and ID kept, its file and line, its basis, and whether it is validated or needs re-running against the January 2029 baseline. Status: draft (board row S2), compiled November 12, 2026 by a Standard-tier subagent from `legacy/` and `models/` and checked by the dossier author. Statements about the 2025 law marked [not in repo, verify] are checked against the statute in `1-problem.md`, part A, which governs where they differ. It decides nothing; sections 1 and 2 cite it where a legacy figure bears, and S3's memos use it to say which figures they may rely on. Legacy files are cited, never edited (`charter/STANDARDS.md`).


## 0. Findings that change how the legacy may be used (read first)

1. **The child-poverty model is a static, source-year (income year 2025) experiment, not a 2029 current-law model.** Its own README and reports say so (`models/tools/child-poverty/README.md:3`, `:41`, `:135`; `legacy/sources/family-child-poverty-agenda-effects.md:5`). The "2030/2034" labels set policy phasing and price conventions; resources are held at 2025 purchasing power. No file builds a 2029 baseline.
2. **The model never applies the SSN requirement.** No SSN/ITIN status is imputed (`legacy/sources/family-child-poverty-cps-baseline.md:22`; `models/tools/child-poverty/README.md:41`, `:100`). Legal coverage is a scalar assumption (90% / 95% / 98% / 100%, `models/tools/child-poverty/agenda-assumptions.json:7-46`). Whether Census's tax-year-2025 credits already reflect P.L. 119-21 is not stated anywhere in the legacy files.
3. **The $2,200 credit is in the model's parameter table** (`models/tools/child-poverty/empirical/cbo-ctc-parameters-2026-02.csv`: CY2025 $2,200 / $1,700 refundable; CY2030 $2,400 / $1,900; CY2034 $2,600 / $2,100) and in the FAM-1A runs' retained-credit reference (`agenda_analysis.py:199-200`). **But the American Family Act (AFA) analogue, which is the adopted FAM-1D result, retains $2,000.04 per child in its own formula** ("statute's $166.67 monthly reference, not $2,200", `models/tools/child-poverty/comparison_analysis.py:37`). The headline 8.73% / 8.34% / 8.09% therefore rests on the bill's text, not on current law. Flag for re-run (section 2).
4. **Paid-leave "loan repaid 2048" is superseded: the current central result is 2058.** `legacy/domains/domain-family.md:75` still says 2048; `legacy/sources/capacity-round-two-integration.md:18` and `legacy/index/recovery-budget.md:59` say 2058 (after adding SSA administration of 3% of benefits plus $3B startup). At 6% administration the loan is not repaid by 2100 (about $96B outstanding, `capacity-round-two-integration.md:20`).
5. **The "$0.9T" leave cost is the middle take-up case; the recovery budget uses the high case ($1.4T of benefits 2030-39).** See section 3.
6. **No legacy design or model exists for SNAP, SSI, unemployment insurance, TANF or the EITC.** They appear only as context (section 5). The agenda file confirms: 25 secure-floor IDs, none for those programs (`agenda/agenda.csv`; `dossiers/secure-floor/README.md:51`).
7. **The 4.42% / 2034 / 83% / OASI-2032 figures are cited to secondary summaries** (two web summaries and a congressional press statement), not the Trustees PDF (`legacy/sources/revenue-channels-and-full-menu.md:188`; `legacy/domains/domain-social-security.md:11`, `:122`). The SSA provision scores the model uses do have primary SSA URLs (`models/data/inputs/funds-ss-ssa-summary.csv`).
8. **Raw CPS data are not in the repo and the "official archive" claim is qualified.** The baseline report says the official archive was downloaded (`family-child-poverty-cps-baseline.md:5`, `:13`). The later review says the original ZIP was not obtained and the national matrix ran on user-uploaded Census members in a repacked ZIP with its own hash (`legacy/sources/family-poverty-model-review-and-extension.md:100-102`; JSON `archive_sha256` 7513d204...0339 vs official fe819d04...7d93). Member hashes were verified; container identity was not. Nothing here can be re-run in this repo without that data.

---

## 1. Child benefit (FAM-1) and child poverty

### 1.1 What the model is

| Item | Statement | Where |
| --- | --- | --- |
| Name / status | "Child-poverty microsimulation: reconstructed research tool". "117 logic/extension tests; verified CPS source-year baseline and all 160 replicates; completed conditional agenda experiments, not a future poverty forecast." Dated October 24, 2026; source branch `claude/pensive-mendel-g1lwl5` at `df2911d1...` | `models/tools/child-poverty/README.md:1-3` |
| Provenance | Rebuilt from four research-report exports, three preliminary notes, a rule sheet and a surviving GitHub prototype. "Does **not** claim to recover the missing ZIP byte for byte." Original engine SHA-256 `702c8e45...4334bb9` | `README.md:5`; `legacy/sources/family-child-poverty-rebuild-findings-and-integration.md:19-31` |
| Data | CPS ASEC 2026 (survey year 2026, **income year 2025**), 134,729 persons, 31,444 children, 55,401 SPM units, 72,979 tax-unit keys, FILEDATE 72726; 160 replicate weights; person weight MARSUPWT | `family-child-poverty-cps-baseline.md:15`, `:30`; `family-child-poverty-target-year-preparation.md:9` |
| Method | Census SPM resources and thresholds; Census public-use tax-model credits kept in baseline resources; policy applied as an **increment** over observed CTC+ACTC (`tax_increment`, `agenda_analysis.py:203-212`); discrete receipt/allocation mixtures; SDR variance `4/R * sum((rep - full)^2)` | `README.md:41`, `:74`, `:129` |
| What is jointly modeled | CTC, care/pre-K (shared expense pool, recomputed capped SPM deduction), school meals and Summer EBT (net of baseline), capped household vouchers with separate award and lease-up, employee leave contribution as a cost | `README.md:41`, `:123-125`; `agenda-effects.md:45-51` |
| What is not | Employment response; leave benefits; health effects; other taxes/transfers; wages; housing supply; long-run child development; federal cost; D3/D4 certification | `README.md:131`; `agenda-effects.md:72` |
| Input contract | Schema v2 JSON; minimum policy record: year 2030 or 2034, `policy_status: research_only`, indexing, age-17 layer, receipt basis, `min_cell` >= 30 for real subgroup tables | `models/tools/child-poverty/schema.md:1-23` |

### 1.2 What is validated and what is not

| Check | Result | Where |
| --- | --- | --- |
| Test suite | 117 tests (62 model, 21 projection/credit, 19 agenda, 15 comparison). **I re-ran them on November 12, 2026: 117 pass, 0.077 s.** They use artificial units only; "not an independent validation of every source assumption" | `README.md:3`, `:21`; `family-poverty-model-review-and-extension.md:10` |
| Keyed join, one-to-one | 134,729 person records / 134,729 replicate records; 0 nonpositive thresholds; 0 SPM-status disagreements | `family-child-poverty-cps-baseline.md:30-33` |
| All-age SPM count vs Census README | 16,941 unweighted poor (match); 44,390,216.71 weighted poor (rounds to Census 44,390 thousand) | `cps-baseline.md:34-35` |
| Child SPM rate vs published | 13.3913% reproduces the published 13.4% rounding; script fails outside 13.35% to <13.45% | `cps-baseline.md:38`, `:46` |
| Tax/SPM identities | SPM resource identity reproduces for all 55,401 units; person-level ACTC, EITC and after-credit tax equal unit sums exactly; no tax unit spans two SPM units | `family-child-poverty-target-year-preparation.md:9` |
| Matched external comparator | Removing EITC + refundable ACTC lifts 6,141,800 people and 3,249,823 children (public use) vs Census internal-file 6.1M and 3.3M; tolerances 0.25M / 0.15M passed; "validates source-year accounting, not the Project's assumed delivery or future effects" | `agenda-effects.md:98`; `family-child-poverty-comparator-register.csv:7`; JSON `external_comparator` |
| Reproduction of historical result | Moderate 2034 (10.29%) reproduced exactly on the uploaded members; all 16 national cases identical on a second run | `family-poverty-model-review-and-extension.md:10`, `:100` |
| **Not validated** | Tax-claimant/dependent construction beyond the Census public-use model; any future-year tax/transfer baseline; receipt, coverage, care/pre-K/food/voucher access (all analyst assumptions); administrative-underreporting alignment; monthly payment behavior; subgroup-specific intervals; unit-level fiscal totals | `cps-baseline.md:50-52`; `rebuild-findings...:70-76`; `README.md:129` |
| Not reproduced | Recovered report 3's seven-test package and its fixture rates; "no recovered golden fixture"; report 4's code | `rebuild-findings...:68`; `:38-40` |
| Sampling intervals | Conditional on fixed assumptions; "exclude model, underreporting and policy-parameter uncertainty" | `cps-baseline.md:50`; `agenda-effects.md:74` |

Source-year benchmark note: Census 2025 child SPM and official+ child poverty both round to 13.4%; overall SPM is 13.1% (`family-child-poverty-comparator-register.csv:2`; `rebuild-findings...:42`). The value alone does not identify the measure; name measure, universe, year, table and file vintage.

### 1.3 Source-year baseline (model result, validated to Census rounding)

| Measure | Value | Where |
| --- | --- | --- |
| Child SPM poverty | **13.3913%** (SE 0.3425 pp; 95% sampling interval 12.7200%-14.0626%) | `cps-baseline.md:38`, `:41-42` |
| Poor children / child population | 9,652,806.50 / 72,082,589.85 | `cps-baseline.md:36-37` |
| Child deep poverty (<50% of threshold) | 3.4447% (2,483,011 children) | `cps-baseline.md:39`; `models/tools/child-poverty/empirical/cps-2026-baseline.json` |
| Children below 150% of threshold (incl. poor) | 32.5302%; near-only 19.14% (13.80M) | `cps-baseline.md:40`; JSON |
| Child-weighted poverty gap | $148.0B (repeats a family's gap per child; "not budget costs") | JSON `children_marsupwt`; `cps-baseline.md:44` |
| All-age SPM | 13.11% | JSON `all_people` |
| Target-year demographic sensitivities | CPS-anchored child counts about 69.17M (2030) and 66.75M (2034); rates stay near 13.4% because within-cell resources are frozen; `policy_ready: false` | `target-year-preparation.md:39`; JSON `demographic_sensitivities` |
| Same-scenario baselines | 13.39% (2030), 13.40% (2034); 15.35% / 11.66% under -5% / +5% resource stress | `agenda-effects.md:11`, `:19`; `family-poverty-model-review-and-extension.md:92` |
| Weak spots | 327 sample children have no positive claimant pointer (excluded from new credit in main runs); 171 dependents (141 children) have a different own-return TAX_ID from their claimant; 15,325 tax units have positive combined CTC/ODC | `target-year-preparation.md:15`; JSON `source_audit` |

### 1.4 Headline results: the adopted package (FAM-1D / AFA + 1,000,000 vouchers)

Adopted by Espen October 24, 2026: AFA credit (FAM-1D, replacing FAM-1A) plus one million **total** new HOU-4A awards (replaces 400,000), 250,000 a year 2030-33; HOU-4C broader assistance an optional add-on, not in base (`legacy/governing/project-2050-governing-decisions.md:394-400`; `models/tools/child-poverty/adopted-package.json:1-13`; `legacy/sources/family-adoption-architecture-bridge.md:7-17`). Analogue `AFA_2025_real`: annual-exposure face amounts preserved in 2025 purchasing power, 2034 population and valuation reference, source-year resources.

| Delivery case (analyst assumption) | Child poverty | Deep poverty | Poor children | Deep-poor children | Children lifted | Expected leases (of 1.0M awards) | Paired change in rate, 95% | Where |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| Same-scenario baseline (2034 CPS-anchored pop. 66.75M children) | 13.40% | 3.45% | 8,946,449 | 2,301,897 | | | | `family-comparison-model-checks.json` `adopted_cases[].baseline` |
| Moderate | **8.73%** | **1.97%** | 5,828,749 | 1,314,808 | 3,118,558 | 650,000 | -5.08 to -4.26 pp | `family-comparison-model-checks.md:44-48`; JSON |
| Enhanced | **8.34%** | **1.85%** | 5,568,379 | 1,238,190 | 3,378,358 | 850,000 | -5.49 to -4.63 pp | same |
| Full | **8.09%** | **1.78%** | 5,396,763 | 1,187,245 | 3,549,686 | 1,000,000 | -5.77 to -4.87 pp | same |

Mean unit resource gain per child (not a fiscal cost): $4,469 / $4,877 / $5,124 (JSON). Sampling SE of moderate poor rate 0.256 pp (95%: 8.23%-9.23%). Federal cost field is `null`: "every new federal cost stays null" (`family-poverty-model-review-and-extension.md:54`).

Assumptions behind these: delivery cases are "analyst assumptions, not measured program-performance estimates, forecast percentiles or confidence bounds" (`agenda-effects.md:24`). Moderate = coverage 0.95, CTC receipt 0.95, care 0.5 (2030) / 0.75 (2034), pre-K 0.6 / 0.85, food receipt 0.9, voucher lease-up 0.65; stressed 0.9 / 0.85 / 0.3 / 0.5 / 0.4 / 0.65 / 0.75 / 0.5; enhanced 0.98 / 0.98 / 0.75 / 0.9 / 0.85 / 0.95 / 0.98 / 0.85; full all 1.0 (`agenda-assumptions.json:7-46`; basis at `:71`: "Analyst stress tests, not estimated take-up probabilities"). Coverage is "a conditional eligible-family share, never imputed SSN/ITIN status". Adopted package: "Necessary in every design; moderate/enhanced/full are research assumptions, not adopted rates" (`adopted-package.json:8`). Moderate coverage x receipt = 90.25% (`family-poverty-model-review-and-extension.md:16`).

Later-year labels (not forecasts; 2034 valuation/population, real resources, rules and delivery held fixed): 2034 moderate 8.73%; 2040 enhanced 8.34%; 2050 full 8.09%; 2050 full with resources -5% of threshold: baseline 15.35% -> 9.44%; +5%: baseline 11.66% -> 6.88% (`family-comparison-model-checks.md:50-56`; paths `legacy/sources/family-later-year-scenario-paths.json`). Constant-real carry-forward of the earlier FAM-1A cases: 10.29% / 10.03% / 9.87% at 2034, 2040 and 2050 alike: "waiting longer produces no improvement in a static model without an explicit mechanism" (`family-comparison-model-checks.md:9-15`; `family-poverty-model-review-and-extension.md:82`).

### 1.5 Credit design comparison (400,000-award cap unless stated; 2034 reference)

| Design | Delivery | Awards | Child poverty | Deep poverty | Poor children | Where |
| --- | --- | ---: | ---: | ---: | ---: | --- |
| FAM-1A (2021 design, $3,600 / $3,000) | moderate / enhanced / full | 400,000 | 10.29 / 10.03 / 9.87% | 2.28 / 2.19 / 2.13% | 6,867,611 / 6,697,450 / 6,588,891 | `family-comparison-model-checks.md:23-25`; JSON `national_cases` |
| FAM-1D at 2030 face amounts | same | 400,000 | 9.34 / 9.02 / 8.81% | 2.13 / 2.04 / 1.97% | 6,233,857 / 6,020,076 / 5,882,657 | `:26-28` |
| AFA, 2025 real face amounts | same | 400,000 | 8.89 / 8.55 / 8.33% | 2.03 / 1.93 / 1.86% | 5,936,937 / 5,708,981 / 5,561,489 | `:29-31` |
| AFA, no newborn bonus | same | 400,000 | 8.95 / 8.61 / 8.40% | 2.05 / 1.95 / 1.88% | 5,975,099 / 5,750,211 / 5,604,604 | `:32-34` |
| FAM-1A, enhanced | enhanced | 1,000,000 | 9.80% | 2.11% | 6,539,113 | `:35` |
| AFA, enhanced | enhanced | 1,000,000 | 8.34% | 1.85% | 5,568,379 | `:36` |
| FAM-1A, enhanced, all proxy-eligible renters | enhanced | 6,755,114 | 7.52% | 1.34% | 5,020,366 | `:37` |
| AFA, enhanced, all proxy-eligible renters | enhanced | 6,755,114 | 6.32% | 1.16% | 4,219,745 | `:38` |

**The 1,000,000-voucher interaction.** Enhanced delivery, same credit: raising awards from 400,000 to 1,000,000 moves FAM-1A 10.03% -> 9.80% (-0.23 pp) and AFA 8.55% -> 8.34% (-0.21 pp). Expected leases at 1.0M awards: 850,000 enhanced, 650,000 moderate (65% lease-up), 1,000,000 full. The proxy-eligible renter pool is 6.76M households (6,755,114 awards; 5.74M expected leases); this is "an exploratory reach boundary: ... not an implementable or priced entitlement", assuming "enough feasible leases ... without demonstrating supply, landlord participation or rent effects" (`family-poverty-model-review-and-extension.md:36-38`). Comparing 6.32% with the moderate adopted case also changes delivery, so it is not a clean housing effect (`:38`). Voucher gains are a discrete award/non-award outcome mixture, not an averaged subsidy (`agenda-effects.md:49`). Award eligibility and the housing-need cap use state-median and waitlist proxies, "not HUD AMI or an observed waitlist" (`agenda-assumptions.json:76`).

Credit contribution diagnostic (AFA, 2025-dollar child-weighted unit amounts before receipt haircuts; not per-child awards, not fiscal totals): source-deep-poor children (2.30M) have mean existing credit $527 and mean statutory increment $6,574, 95.0% with a positive increment; poor-not-deep (6.64M): $2,188 existing, $4,903 increment, 97.4%; not poor (57.80M): $4,185 existing, $1,351 increment, 61.3% (JSON `contribution_diagnostics`; `family-poverty-model-review-and-extension.md:22`).

AFA arithmetic: monthly base $300 for ages 6-17; 120% under six; 800% in the first month of life; unindexed full-year exposures $3,600 (age 6-17), $4,320 (under six), $6,360 (age 0 with the first-month bonus; $4,320 without). "A full first twelve-month exposure is $6,360, not a guaranteed calendar-year award" (`legacy/domains/domain-family.md:19`; `family-comparison-model-checks.md:17`; `family-poverty-model-review-and-extension.md:62`). Sources: H.R.2763 and S.1393 (119th Congress, introduced April 9, 2025; "not current law", `:60`). Public example: ages three and eight = $4,320 + $3,600 = $7,920 a year = $660 a month, "gross credit ... not a net household gain" (`family-security-public-example.md:7`, `:21`).

### 1.6 Historical FAM-1A / 400,000-voucher results (kept for reproduction; **pre-adoption, do not present as the adopted package**)

Header of the file: "Historical pre-adoption experiment: FAM-1A and 400,000 new voucher awards" (`agenda-effects.md:3`). Package: FAM-1A + FAM-2A care/pre-K + EDU-3 food + HOU-4A (100,000 awards 2030, 400,000 by 2034) + employee leave contribution 0.3% of wages as a cost.

| Year | Case | Same-scenario baseline | After policy | Deep poverty after | Net fewer poor children | Where |
| --- | --- | ---: | ---: | ---: | ---: | --- |
| 2030 | Stressed / Moderate / Enhanced / Full | 13.39% | 11.08 / 10.61 / 10.36 / 10.17% | 2.57 / 2.40 / 2.32 / 2.27% | 1.60 / 1.92 / 2.10 / 2.23 million | `agenda-effects.md:15-18` |
| 2034 | Stressed / Moderate / Enhanced / Full | 13.40% | 10.80 / 10.29 / 10.03 / 9.87% | 2.47 / 2.28 / 2.19 / 2.13% | 1.74 / 2.08 / 2.25 / 2.36 million | `:19-22` |

Cumulative channels, moderate (order-dependent, not additive): 2030 CTC 10.85% (deep 2.45%); + care/pre-K 10.71% (2.43%); + school/summer food 10.60% (2.41%); + scarce vouchers 10.57% (2.40%); + employee leave contribution 10.61% (2.40%). 2034: 10.86% (2.45%); 10.70% (2.40%); 10.36% (2.32%); 10.23% (2.28%); 10.29% (2.28%) (`:32-43`).

One-at-a-time sensitivities from moderate (2030 / 2034): index from 2025 rather than 2030: 10.10% / 9.69%; baseline resources -5% of threshold: 12.32% / 11.88%; +5%: 9.13% / 8.75%; coverage gap concentrated in lowest-resource quarter: 11.01% / 10.67%; retain maximum adult-dependent ODC: 10.59% / 10.24%; employer leave fully borne in wages: 10.72% / 10.33%; add adult climate dividend and consumer-cost proxy: 10.52% / 10.12%; carbon proxy + 15% reduction in actual MOOP: 10.23% / 9.84%; + 30%: 9.97% / 9.56%; $10B temporary household cash: 10.37% / 10.29% (`:55-66`). Conditional 95% sampling intervals for the moderate rate reduction: 2.47-3.09 points (2030), 2.78-3.44 (2034) (`:74`). Counts: moderate 2034 leaves about 6.87M poor and 1.52M deeply poor children; about 6.59M remain poor even at full receipt (`:78`). Deep poverty falls from about 3.45% to 2.28% (`family-outcomes-design-review.md:25`). Other counts there: enhanced 6.70M, full 6.59M, index-from-2025 6.47M poor children in 2034 (about 170,000, 279,000 and 399,000 fewer than moderate) (`family-outcomes-design-review.md:18-23`). Stress cases: coverage gap concentrated in the lowest-resource quarter 10.67%; unresolved-claimant proxy 10.24% (`:27`).

Who remains poor (2034 moderate, overlapping, not additive; rate within group / share of remaining poor children): no positive earnings 62.66% / 27.04%; positive earnings 7.86% / 72.96%; multiple or no adults 8.26% / 68.68%; one adult 22.25% / 31.32%; owner/other 5.38% / 35.14%; renter 20.36% / 64.86%; Asian non-Hispanic head 9.44% / 3.33%; Black non-Hispanic 15.70% / 21.56%; Hispanic 16.81% / 39.20%; other non-Hispanic 8.86% / 6.10%; White non-Hispanic 5.99% / 29.80%. Race/ethnicity is the SPM unit head's; no subgroup under 30 sample children is published as a rate (`agenda-effects.md:80-94`).

Other assumptions that carry the historical numbers: dollar convention $3,600 / $3,000 set in 2030 nominal dollars and indexed thereafter (alternative: from 2025); first-stage thresholds follow 2021 filing-status levels; modal annual free-lunch SPM value $861 per school-age child; 2030 credits 80/179 of annual lunch gains and no Summer EBT increase; Summer EBT $60 a month for three months; employee leave 0.3%; 185% FPG eligibility proxy; state-median-income proxy from four-person CPS SPM units (national fallback $138,351, `family-comparison-model-checks.json` `source_audit`); pre-K expense share 0.5; HOU-1 temporary aid carries $0 primary cash value because its split is unsized (`agenda-effects.md:24-26`, `:45-51`; `agenda-assumptions.json:48-68`).

### 1.7 What reports 1-3 found

- **Report 1** (evidence review, `family-child-poverty-report-1.md`): "large poverty reduction is well supported; near-eradication is not" (`:182`); literal near-zero child SPM poverty "implausible under the package as currently specified" (`:23`, medium-high confidence). Four residual mechanisms: legal exclusion, nonreceipt, inadequate resources after receipt, unavailable service (`:44`). The unresolved record question is FAM-1's adult SSN/ITIN treatment ("2021 design" vs "builds on current law", `:56-58`, `:184`); child SSN requirement a likely exclusion (`:60`). Comparators: NASEM 2019 Roadmap $3,000 monthly child allowance, -5.3 pp from a 13.0% baseline (~41%), broad packages about 50% only with large housing/SNAP/earnings/child-support expansions (`:25`); NASEM 2026 Pathways PO12: 11.1% -> 6.5% with no employment response, 7.0 / 7.2 / 7.4% with low / medium / high responses (`:27`); PO12 residual rates about 37% for children with no workers, about 12% with a disabled nonelderly person, about 11% single-parent, about 10% cohabiting (`:50`); 2021 child SPM 5.2% was pandemic-era (`:38`). GAO: about 1.8M children received CCDF subsidies in 2021, about 15% of eligible; 2019 about 2M of nearly 8.7M (`:82`). HUD voucher success about 69% in one national study (`:102`). Timing: credits assigned by receipt year raise poverty (report 2: NASEM 2021 exercise 51% reduction by accrual vs 38% by receipt, `family-child-poverty-report-2.md:69`). Recommended a mutually exclusive residual decomposition and minimum microsimulation (`:150-178`).
- **Report 2**: SPM/tax-unit separation, source preprocessing, age-17 alternatives, five synthetic tests; NASEM 2019 reconstruction 16.3% -> 13.0% child SPM after TRIM3 corrections, deep poverty 4.9% -> 2.9%, public-use count 12.038M vs Census 12.026M (`report-2.md:11`, `:47`); Corinth et al. no-behavior 34% reduction falling to at most 22% with labor response (`:73`); Parolin et al. food insufficiency -7.5 pp (25%) after first monthly CTC payments (`:71`). Notes "$2,200 maximum CTC for 2026, with indexing and a refundable component under current law" and the joint-return one-qualifying-SSN rule (`report-2.md:53`). Its claimed package could not be recovered or rerun (`rebuild-findings...:38`).
- **Report 3**: reproduced the engine locally and found one genuine defect, **mixed-sibling attribution** (one child's legal exclusion treated as excluding all siblings in the SPM unit); poverty-resource arithmetic unaffected; corrected (`report-3.md:11`). Raw-CPS preprocessing still absent; seven-test package not independently matched (`rebuild-findings...:39`). The rebuild reproduced the defect against the exact recovered source (`:5`).
- **Report 4** (not filed; described only): person weights, pre-K/award/lease-up gates; it called 13.4% official rather than SPM child poverty, which is wrong because Census reports both at 13.4% (`rebuild-findings...:40-42`).
- Rebuild findings: "supports a substantial rebuild, but not recovery of a complete, calibrated national model" (`rebuild-findings...:5`). Two consequential accounting choices: increment-only vs replace-credit (v1 silently clipped the increment at zero), and capped vs uncapped SPM child-care expense (`:64-66`).

### 1.8 Comparator register

`legacy/sources/family-child-poverty-comparator-register.csv` (6 rows, lines 2-7): (2) Census 2025 poverty report: child SPM and official+ both 13.4%, overall SPM 13.1%, benchmark identity check; (3) Census SPM README: public-use SPM file vintage, preprocessing/weighting audit; (4) NASEM 2019 Roadmap ch. 6: 2015 population, TRIM3-adjusted, "leading packages meet approximately half-poverty objective in their own baseline", "never transfer result to Project 2050"; (5) NASEM 2026 Pathways ch. 9 PO12: 2018 baseline, non-ARPA EITC plus TCJA CTC, "not post-2025 law", 11.1% baseline, 6.5% no response, 7.0 / 7.2 / 7.4% with responses, "not a Project score"; (6) IRS Schedule 8812 2025 instructions: "Post-2025 current-law identification rules", joint return needs at least one qualifying SSN, other spouse SSN/ITIN, child SSN rule, "Rule-sheet review, not a complete 2030 tax baseline". (7) Census 2025 refundable-credit removal matched comparator (executed): 6.1418M people and 3.2498M children lifted; internal rounded 6.1M / 3.3M; tolerances 0.25M / 0.15M; passed.

### 1.9 FAM-1 policy record, cost, financing and household test

| Item | Figure | Basis | Where |
| --- | --- | --- | --- |
| FAM-1D (chosen Oct 24) cost 2030-39 | $1.7 / $1.9 / $2.1T | **estimate**: "rough planning estimate; exact score pending"; anchor TPC about $1.4T for AFA FY2026-35, later window and baseline "need reconciliation" | `legacy/domains/domain-family.md:9`, `:25`, `:32`, `:124` |
| FAM-1A (previous) | $1.5T | **scaled** historical (CRFB $1.7T for 2021 design through 2033) | `domain-family.md:31`, `:126` |
| FAM-1B supplement +$500 most children, +$1,500 under 6 | about $0.45T | **scaled** (CRFB $380B through 2033) | `:33`, `:126` |
| FAM-1C full refundability of current $2,200 credit only | about $0.3-0.5T | **estimate** | `:34` |
| Previous-to-adopted midpoint change | +$0.40T credit (+$0.09T vouchers = +$0.49T); "Do not claim the former $1.5T and $1.7T values established an exact $200B increment" | working planning | `family-adoption-architecture-bridge.md:25-32`; governing `:398` |
| Vouchers (one million) | $0.10 / $0.15 / $0.1875T (previous $0.06T); housing aggregate $0.40 / $0.56 / $0.7325T | **scaled** | `bridge.md:27-29` |
| Credit + care/pre-K + meals + vouchers subtotal | $2.42 / $2.92 / $3.5175T (previous $2.43T) | informational, not a ledger row | `bridge.md:30`; `family-outcomes-design-review.md:36` ($1.5T vs $1.7T "both scaled working figures") |
| Effect on financing | General-fund claims about $11.10T -> $11.59T; top-end base $5.99T; initial gap $5.60T; existing accepted revenue $3.71T and accepted investment borrowing $1.15T leave about $0.74T over the window; FY2040 GF primary shortfall about $53.7B (0.099% of GDP) vs old surplus about $3.3B; **"D4's maturity test now fails under the working inputs"**; ten-year GF primary deficit about $2.03T; debt about 155.1% of GDP in 2056 vs baseline 180.2% | **model result** (old CAP-7S cash proxy, uncertain scores) | `bridge.md:38-40` |
| Financing routes tested (not adopted) | Corporate rate 28% -> 31%: +$566B (after 20% haircut on roughly $707B), FY2040 receipts $69.1B, balance +$15.4B, Q4 net $1,120; payroll 0.35 points: +$560B, $68.3B, +$14.6B, Q4 $853; median health-exclusion cap replacing 75th-percentile cap: +$590B, $90.6B, +$37.0B, Q4 $678; all 3 clear the maturity screen; at a further 40% shortfall corporate and payroll fail (worst gaps $12.3B / $12.7B) | **model result**, comparison assumptions | `family-financing-comparison.md:7-35` |
| Household test, aggregate allocation key | FAM-1 distributed by key `ctc`: Q1-Q5 = 33 / 30 / 21 / 12 / 4%, top 1% 0 | **estimate** anchored to published patterns | `models/data/inputs/incidence-keys.csv` (`ctc`); `models/data/inputs/incidence-rows.csv` (F1) |
| F1 per fourth-quintile household | $814 a year benefit (at $1.9T) | **model result** | `legacy/index/revenue-household-incidence-model.md:54` |
| Incidence caveat | Existing credit/housing keys "provisional distribution proxies"; do not map AFA-specific high-income credit losses, legal exclusions or within-quintile winners and losers; the bridge reported Q4 about +$1,373 (October 24 vintage) but the regenerated scenario Q reads Q4 -$1,038 | | `bridge.md:44`; `revenue-household-incidence-model.md:9`, `:15` |
| Labor-supply sensitivity | DY3 "Child tax credit without a work requirement": -$0.12 / -$0.07 / -$0.02T (Talarico-style +$0.00) | **estimate**, in no total | `legacy/index/2029-trifecta-master-ledger.md:130` |
| Delivery / vehicle | IRS monthly payments; R1 vehicle; standing Treasury disbursement authority drafting note; "felt by Nov 2030: yes" | | `domain-family.md:9`, `:23`, `:99-103` |
| Ledger row | FAM-1 (legacy F1): 1.90 (1.70-2.10), basis "estimate", "Unverified" felt evidence | | `2029-trifecta-master-ledger.md:306` |

### 1.10 Open defects and limits the legacy files themselves list

- AFA mapping is "not exact legislative arithmetic": statutory CPI base years, lag, rounding, monthly custody/birth exposure, income elections, IDs, ODC and reconciliation unmapped; interview ages for tax-year ages; mapping of `other` filing status to single, no separate-return distinctions, MAGI exclusions, Puerto Rico (`bridge.md:19`, `:56`; `family-poverty-model-review-and-extension.md:64`).
- Eligibility/ID unresolved: citizenship is never an SSN/ITIN proxy; no national count of SSN/ITIN branches is supportable (`:66`; `README.md:100`).
- FAM-1's two-stage phaseout "remains provisional"; the tool imports actual current-law CTC and does not compute post-2025 taxes, ODC interactions, custody, territories, recapture or safe harbors (`rebuild-findings...:74`).
- Combined CTC/ODC: Census `CTC_CRD` mixes the two and cannot be imported as CTC alone; `SPM_FEDTAX` already includes refundable credits, so adding ACTC or EITC again would double count (`target-year-preparation.md:13`, `:31`). The main offset subtracts the entire combined amount; ODC sensitivity retains up to $500 per adult dependent (`agenda-effects.md:26`).
- No cost: poverty results "do not certify D3/D4"; resource deltas "are neither federal outlays nor social value" (`README.md:11`, `:131`; `rebuild-findings...:91`).
- Monthly payment reliability, annual receipt and on-time months are separate; the monthly 12-fraction input is an assumption (`schema.md:13`; `README.md:76`).
- No employment response; no behavioral case; no paid-leave benefits; health only as 15% / 30% MOOP stresses (`agenda-effects.md:51`, `:64`, `:72`).
- No target-year current-law forecast: "A national current-law poverty forecast requires recomputing income, taxes, transfers, expenses and thresholds together" (`target-year-preparation.md:5`, `:57`).
- Provenance of the national runs (point 8 above); report 4 and the original ZIP not recovered.
- Whole-agenda boundary: the headline "is not the entire Project 2050 household effect"; "the modeled results do not establish a pathway close to eradicating child poverty" (`agenda-effects.md:72`; `family-outcomes-design-review.md:10`). Charter ambition to approach eradication "needs defined measures, modeled effects ... and Espen's approval" (`legacy/governing/project-charter.md:246`).
- Overlay contract exists for reviewed health, tax/transfer/earnings and leave-benefit inputs; none supplied (`family-poverty-model-review-and-extension.md:68-78`).
- Talarico scenario, for contrast only: child allowance 41M households, child poverty -44% held 7 years, food insecurity -51%, non-filer take-up 91% by 2032, first checks 5 months after signature (`legacy/sources/scenario-talarico-2029-2037.md:146`). Scenario model figures, "not forecasts" (`:3`).

---

## 2. Check against the January 2029 baseline

STANDARDS requires "the current-law baseline as it will stand in 2029, counting enacted laws with later effective dates" (`charter/STANDARDS.md`, "Time frame"). Legacy facts versus what P.L. 119-21 sets:

| Element | What the legacy encodes | P.L. 119-21 / 2029 law **[not in repo, verify against statute text]** | Verdict |
| --- | --- | --- | --- |
| Credit amount | CBO February 2026 table: $2,200 (CY2025), $2,400 (CY2030), $2,600 (CY2034) per child; ODC $500 (`empirical/cbo-ctc-parameters-2026-02.csv`; `target-year-preparation.md:21-27`). FAM-1A runs use these as the retained credit reference (`agenda_analysis.py:199-200`). FAM-1C's name states "the current $2,200 credit" (`domain-family.md:34`) | $2,200 for tax years beginning after 2024, indexed after 2025; no sunset | **Consistent** in the parameter table. A 2029 value is not in the file (only 2025, 2030, 2034); do not invent one |
| Refundable portion | $1,700 (2025), $1,900 (2030), $2,100 (2034); earned-income threshold $2,500; 15% rate; three-child payroll alternative (`current_law_ctc.py:49-60`; CSV) | $1,700 refundable for 2025, indexed | **Consistent** |
| Phaseout | $400,000 joint / $200,000 other, $50 per $1,000 (`current_law_ctc.py:49-51`) | same, not indexed | **Consistent** |
| Indexing | CBO projections (nominal $2,400 by 2030), described as "projections, not IRS announcements" (`target-year-preparation.md:27`); report 2 cites IRS "$2,200 maximum CTC for 2026, with indexing" (`report-2.md:53`) | Indexed after 2025 | **Consistent**; the legacy indexing is a CBO projection, not statute arithmetic |
| SSN rules | Comparator register row 6 names the post-2025 identification rules (one qualifying SSN on a joint return; child SSN). The `current_law_ctc.py` worksheet takes eligibility as a "reviewed" input and "does not ... infer eligibility from CPS citizenship/age" (`README.md:117`). The **simulation applies no SSN test**; it uses a coverage scalar | Taxpayer (one spouse on a joint return) must have a work-eligible SSN; child needs SSN | **Not implemented.** The historical assertion that the child-SSN rule is "a likely legal exclusion" (`report-1.md:60`) is the only treatment |
| Baseline year | Resources = **2025 income year**, tax-year-2025 credits as computed in Census's public-use tax model and kept in SPM resources | P.L. 119-21 took effect for tax year 2025; July 2025 enactment | **Does not predate the law**, but **the files never say whether Census's 2025 tax model applied it.** Check: in the archive, the maximum per-child `CTC_CRD`+`ACTC_CRD` should reach $2,200 if it did |
| AFA analogue | Retains **$2,000.04 per child** from the first phaseout (`comparison_analysis.py:37`); thresholds $150,000 / $112,500 first, $400,000 / $300,000 second (`:35-36`) | Current credit is $2,200 and the second threshold $200,000 for non-joint | **Mismatch to resolve.** The AFA bill is a replacement of section 24 so the retained amount is a drafting choice, but the model should state which of $2,000 or $2,200 (indexed) the adopted FAM-1D keeps |
| Target year | Labels 2030 and 2034 only; no 2029 | Dossier baseline is January 2029 (tax-year 2029 for credits, 2029 resources) | **No 2029 run exists.** Nearest: CBO 2030 parameters |
| Other SPM-resource changes | Source-year resources (2025) contain none of the post-2025 benefit changes (SNAP, Medicaid, marketplace credits; Care dossier lists the "2025 reconciliation law's Medicaid and marketplace changes, the enhanced premium credits' expiry", `charter/PROGRESS.md:115`) | Phased 2026-2028 | Model baseline resources do not reflect them. The SNAP value, MOOP and `SPM_CAPHOUSESUB` inputs in the policy runs are 2025 |

**Where results need re-running.**

1. **FAM-1A eight cases and 42 sensitivities**: historical only; superseded by adoption. Do not carry forward as the secure floor's result.
2. **Adopted-package results (8.73 / 8.34 / 8.09%)**: re-run needed for (a) the $2,000.04 vs $2,200-indexed retained reference; (b) an explicit SSN/ID branch (parent SSN rule, child SSN rule) replacing the 90-100% coverage scalar; (c) a check of the Census tax-model vintage for the 2025 credits; (d) a TY2029 parameter set and a jointly recomputed 2029 current-law baseline (income, taxes, transfers, thresholds); (e) a faithful monthly AFA mapping (bridge upgrade item 1, `bridge.md:56`). None can be done in this repo without the ASEC 2026 members; the recovered code and tests run offline (117 pass) but the national runs do not.
3. **Counts**: the adopted-package counts (8.95M baseline, 66.75M children) use the CPS-anchored 2034 population ratios; the source-year baseline counts are 9.65M of 72.08M. The two bases must not be mixed.
4. Outside this model: the household test and the cost range ($1.7-2.1T) were set before the P.L. 119-21 baseline was reconciled; the TPC anchor is "against current law" at FY2026-35 (`domain-family.md:124`).

---

## 3. Paid leave (FAM-3)

### 3.1 Policy record

FAM-3A (chosen): 12 weeks of social insurance, progressive wage replacement "starting at about two-thirds of wages up to a cap", administered by SSA (accepted October 26) or a new office with state partnerships; contribution 0.6% of wages (0.3% each side) stepping 0.05 points each January if the reserve falls below one year of projected benefits, toward the 1.10% working cap; steps back down above 18 months (`legacy/domains/domain-family.md:69`, `:75`, `:134`). Vehicle R2; paid-leave fund; benefits from 2031 ("felt by Nov 2030: no", `:11`). Espen approved the 1.10 ceiling and SSA administration October 26 (`legacy/governing/project-2050-governing-decisions.md:448`, `:490`). Options: FAM-3E (0.6% with open general-fund backstop: net about 0, up to +$0.55T at high take-up), FAM-3B (fully general fund, $0.9T), FAM-3C (4 weeks, about $0.3T), FAM-3D (0.85% from the start; net below 0; costs the fourth quintile more up front) (`domain-family.md:83-87`). Agenda IDs FAM-3, 3A-3E; REV-P1 "Paid-leave contribution 0.6% toward 1.10% working ceiling" (`legacy/index/options-register.md:130`).

### 3.2 Figures, basis and traceability

| Figure | Value | Basis | Origin / outside source? | Where |
| --- | --- | --- | --- | --- |
| Cost 2030-39 | about **$0.9T**, range $0.6T-$1.4T | **estimate** | Range = take-up cases low / mid / high (mature cost 0.43% / 0.65% / 1.01% of payroll). The ledger row calls it "CBO $547B (BBB-era design); JCT break-even 0.85%; 0.6% raises ~$0.9T" | `domain-family.md:72`; `legacy/index/dedicated-funds.md:61-63`; ledger `:308` |
| CBO $547B | 12-week FAMILY Act-based design, ten years | cited | **Outside, secondhand**: American Action Forum "Paid leave and the reconciliation bill" (`domain-family.md:127`). The primary CBO document and its window are not cited ("BBB-era design"). Checkable at CBO/AAF; I could not check | `domain-family.md:72`, `:127` |
| JCT break-even | **0.85%** of wages at FMLA take-up; higher take-up runs "far above that" | cited | **Outside, secondhand**: same AAF article. Also in the same source: "0.4% CBO-linked rate" (not otherwise used) | `domain-family.md:72`, `:127` |
| Contribution revenue | 0.6% x about $15T of covered wages = about **$0.9T** over ten years | **estimate**, arithmetic | Model check: raises $0.97T in 2030-39 at 0.60% and $1.37T at the (old 0.85%) cap vs ledger P1 $0.90T and $1.28T | `domain-family.md:73`; `dedicated-funds.md:57`; ledger `:429` |
| Old cap 0.85% | "failed under high take-up" | model result | Pre-October 26 design | `domain-family.md:75`; `dedicated-funds.md:55`, `:59-65` |
| Old take-up cases (cap 0.85%) | low: mature 0.43%, never steps, receipts $0.97T, benefits $0.60T; mid: 0.65%, first step 2039, $0.98T, $0.90T; high: 1.01%, first step 2032, rate 0.80% / 0.85% / 0.85% (2035 / 2039 / 2050), receipts $1.23T, benefits $1.40T, Treasury loan owed $184B (2039), $865B (2050); "the loan never stops growing" | model result, **estimate** inputs | Benefit ramp 50% (2031), 80% (2032), full from 2033 | `dedicated-funds.md:59-65`; `models/data/inputs/funds-parameters.csv` (`leave_ramp`) |
| Domain file's loan estimate | about $120B in-window loan vs the model's $184B | estimate | | `dedicated-funds.md:65` |
| **Selected: 1.10 cap, high take-up** | Mature cost 1.012% of payroll. Rate path (central "mixed" case): 0.60% in 2030-31, 0.65 (2032), 0.70, 0.75, 0.80, 0.85, 0.90, 0.95, 1.00 (2039), 1.05 (2040), **1.10 from 2041**. 2030-39: receipts **$1.285T**, benefits **$1.400T**, administration **$45B**. Loan builds from 2034, peaks about **$185B in 2040**, repaid **2058**, terminal loan $0 | model result (`mixed`, `mixed_reserve_corridor` and all other mixed cases identical) | Generated: `models/data/recovery-budget.json` `cases.mixed.leave`; code `models/tools/recovery-budget/model.py:99-118`; inputs `assumptions.json:166-169`, `models/data/inputs/recovery-adoption.json` | `legacy/index/recovery-budget.md:59` |
| **Loan repaid 2048** | Pre-administration result at the 1.10 cap | model result | **Superseded** (see 2058). Still printed in `domain-family.md:75`; `recovery-and-solvency-budget.md:100` also says 2048 and "debt-free through 2100 in the extended run" | `domain-family.md:75`; `recovery-and-solvency-budget.md:100` |
| SSA administration | **3% of benefits plus $3B FY2030 startup**; original review proposed about **$30B** (range $18-60B; roughly $3-4B a year once mature) charged to the leave fund; at the high-take-up $1.4T of benefits the model books $45B (3% x $1.4T = $42B + $3B). Band 2-6% "not a score" | **estimate** | Claim-volume check: mature benefits about $120B a year at $6,000-10,000 per claim = about 12-20M claims; $150-350 per claim = $2-7B a year, 1.5-6% of benefits. Comparator: SSA's $14.8B administrative budget (OASDI $6,457.9M + Medicare $3,663M + SSI $4,659M of FY2026 LAE, SSA FY2027 Congressional Justification, URL in `capacity-round-two-integration.md:11`) | `legacy/sources/capacity-recovery-other-agencies-review.md:26-28`, `:188`, `:214`, `:228`; `capacity-round-two-integration.md:7`; `governing...:490` |
| High administration (6%) | Loan not repaid by 2100; about **$96B** outstanding at the end (peak about $441B in the model JSON) | model result | | `capacity-round-two-integration.md:20`; JSON `mixed_leave_admin_high` |
| Income-tax offset | 12.5% of leave receipts (an allowance, "not a JCT score"); general fund bears it; lending is not revenue | **estimate** | | `assumptions.json:166-169`; `tools/recovery-budget/README.md:130-131`; `domain-family.md:75` |
| **Household test D3** | Worker at $60,000: **$180** a year at 0.6% (0.3% worker share); up to **$330** at the 1.10% combined cap (0.55% worker share); "long-run economic incidence can include the employer share"; run at both rates; count against benefit, CTC and health savings | **estimate**, arithmetic (0.003 x 60,000; 0.0055 x 60,000) | | `domain-family.md:77` |
| Incidence model rows | P1 (cost, $0.9T, key `wages_cap` Q1-Q5 = 3 / 10 / 19 / 30 / 38%, "both halves on workers") **$964** per Q4 household a year; F3 (benefit, $0.9T, key `leave_benefit` 8 / 17 / 24 / 28 / 23%) **$900** per Q4 household a year | **model result**, **estimate** keys | These still use 0.6% / $0.9T, not the stepped path or $1.4T | `models/data/inputs/incidence-rows.csv` (P1, F3); `revenue-household-incidence-model.md:52-53`, `:78` |
| Child-poverty model's leave treatment | Employee contribution 0.3% of wages as a cost-side stress; **no benefits imputed**; employer incidence separately 0; it raises moderate 2030 poverty 10.57% -> 10.61% | **model result** | | `agenda-assumptions.json:61-62`, `:77`; `agenda-effects.md:32-43`, `:51` |
| Dynamic sensitivity | DY6 child care, pre-K and paid leave raise parental employment: +$0.15 / +$0.22 / +$0.30T (Talarico +$0.40T); in no total | **estimate** | | ledger `:133` |
| Ledger | FAM-3 (legacy F3): 0.90 (0.60-1.40), "Paid-leave fund" channel, GF 0, basis "estimate" | | | ledger `:308` |
| Not modeled | State and employer paid-leave programs ("existing state programs can opt in"); event-specific benefits; a reviewed net-benefit input contract exists but is unused | | | `domain-family.md:69`; `family-poverty-model-review-and-extension.md:74` |

The Treasury-loan convention: shortfall at the cap is a repayable loan with interest; "no open-ended benefit-cost guarantee is inferred"; "writing a permanent loan and describing it as a temporary bridge" is what the 1.10 ceiling is meant to avoid (`domain-family.md:75`; `recovery-and-solvency-budget.md:100`).

Which of these trace to a checkable outside source: CBO $547B and JCT 0.85% (via the AAF article; secondhand); the SSA administrative-outlay shares and $14.8B (SSA FY2027 Congressional Justification, primary, URL in the legacy file); everything else is the project's own estimate or model output.

---

## 4. Social Security (SS-1 to SS-10)

### 4.1 The gap

| Figure | Value | Basis | Where / source |
| --- | --- | --- | --- |
| 75-year deficit | **4.42%** of taxable payroll (2026 Trustees) | **sourced** (secondary) | `legacy/domains/domain-social-security.md:9`; `revenue-channels-and-full-menu.md:13`, `:188` (MyChesCo and Western CPE summaries) |
| Combined depletion / payable | **2034**, **83%** payable | **sourced** (secondary) | same; model check: 2034, 83%, -4.45% (model rounding) `dedicated-funds.md:13`, `:41` |
| OASI alone | "as little as six years", about **2032**; "as reported; not re-checked against the report here"; automatic cut "a fifth to a quarter" (scenario: about 23%; scenario ledger line says Q4 2032, scenario text Q3 2032) | **sourced** (secondhand: Rep. Larson, June 2026) | `domain-social-security.md:11`, `:122`; `scenario-talarico-2029-2037.md:25`, `:28`, `:108`; ledger `:282` |
| Annual gap at depletion | roughly $400-450B (17% cut of benefits that were $1.6T in 2025, about $2.6T in 2034) | **estimate** (author) | `revenue-channels-and-full-menu.md:26` |
| Rate needed | 17.3% after a 2034 depletion (about 4.9 points combined if delayed to 2034) | **sourced** (secondary) | `:30`, `:188` |
| 2023 comparison | SSA actuaries on Sanders-Warren against a 3.42% deficit: +2.46, +1.93, +0.92, -1.46, -0.41, -0.11, -0.05 | **sourced** (SSA letter Feb 13, 2023) | `domain-social-security.md:9`, `:117` |
| Medicare HI check | 2033, 0.56%, 89% payable (Trustees) vs model 2034 / -0.64% | context | `dedicated-funds.md:49`; `revenue-channels...:191` |

### 4.2 Chosen design (D8) and the closer

D8: solvency first with a targeted increase, as its own regular-order bill in spring 2030; Section 310(g) bars reconciliation, so it needs D2's graduated cloture (F) or 60 votes; about 8 floor days; felt date about January 2031 (first COLA); revenue sits entirely above $250K / $400K (`domain-social-security.md:5`, `:83-88`; `legacy/governing/project-2050-governing-decisions.md:196-201`).

| ID | Piece | 75-year effect (% of payroll) | Basis | Underlying scores | Where |
| --- | --- | --- | --- | --- | --- |
| **SS-1** | 12.4% on earnings above $250,000 (unindexed), with a 2% benefit credit on the added earnings, from 2031 | **+2.30** (by year 2031 / 2040 / 2060 / 2090: +2.34 / +2.52 / +2.54 / +2.45) | **estimate** on SSA 2026 scores | SSA E2.5 +2.52 (no credit, 2027), E2.17 +2.33 ($400K), E2.14 +2.41 (2% credit, 2028); the domain file also quotes SSA's 2027 versions at +2.37 (E2.16) and +2.41 (E2.14); elsewhere E2.16 is +2.35 | `domain-social-security.md:17`, `:118`; `dedicated-funds.md:21-23`, `:33`; `revenue-channels...:28` |
| **SS-2** | 12.4% on net investment income above $400,000 (unindexed), credited to the trust fund, from 2031 | **+1.17** before the haircut; **+0.99** after the 15% stacking haircut (by year +0.82 / +0.90 / +1.10 / +1.27) | SSA F11 +1.22 (2028 start, **sourced**); model moves it to 2031 (**estimate**); haircut is the domain file's **estimate** (stacking with REV-H1b) | F9 (ACA thresholds) +1.32 | `domain-social-security.md:18`; `dedicated-funds.md:24-25`, `:34` |
| **SS-3** | Minimum benefit 125% of poverty for 30-year workers, wage-indexed | **-0.11** (by year 0.00 / -0.04 / -0.14 / -0.19) | **sourced** (SSA B5.2, 2026 Trustees; about $1,630 a month in 2025; start 2027 shifted to 2031) | `funds-ss-ssa-summary.csv` run 196 | `domain-social-security.md:19`; `dedicated-funds.md:35` |
| **SS-4** | CPI-E for COLAs (about +0.15 points a year) | **-0.33** (by year -0.02 / -0.21 / -0.40 / -0.51) | **sourced** (SSA A6, 2026 Trustees; model -0.35 on rebuild) | run 116 | `domain-social-security.md:20`; `dedicated-funds.md:27`, `:36` |
| Baseline net (SS-1 to SS-4) | **about +2.85** after the haircut (+3.0 before); **about 64%** of the 4.42% gap (68% before); depletion **2034 -> about 2062**; about 1.6% of payroll remains; model: 2062, 90% payable, -1.60, reserve ratio 80% / 20% / 0% / 0% (2040 / 2060 / 2080 / 2100) | **estimate** ("interactions ignored", "not yet scored as a whole") | | `domain-social-security.md:21-24`; `dedicated-funds.md:42`; governing `:211` |
| **SS-5** (selected October 26) | Investment-income tax on active S-corporation holders and limited partners (Sanders-Warren section 8b), from 2031 | **+0.87** (by year +0.89 / +0.90 / +0.95 / +1.00); 2030-39 trust-fund **+$1.32T** | **sourced** (SSA F8, 2026 Trustees, +0.93 from 2027) moved to 2031 | SSA's F8 text is a **16.2% tax** with proceeds to OASDI "attributable to 12.4 percent of the total 16.2 percent tax rate", ACA thresholds $200K / $250K; not described that way in the domain file | `domain-social-security.md:30`; `dedicated-funds.md:37`; `funds-ss-ssa-summary.csv` run 259 |
| Baseline + SS-5 | **about 84%** (88% before the haircut) of the gap; depletion **about 2081**; leaves about 0.7% of payroll; model: 2081, 86% payable, -0.73, ratio 128% / 181% / 15% / 0%; "sustainable: no" | **estimate** | | `domain-social-security.md:36`; `dedicated-funds.md:43` |
| SS-6 | Lower SS-2's threshold to $200K / $250K | about **+0.1** more (**sourced** difference F9 +1.32 vs F11 +1.22); the options register says **+0.3-0.6** | conflict | | `domain-social-security.md:31`; `options-register.md:185` |
| SS-7 | +1 point payroll rate (0.5 each side), phased 10-20 years | +0.9 to +1.0 | **estimate** | | `:32`; `options-register.md:186` |
| SS-8 | Invest part of reserves in equities | +0.5 to +1.0 | **estimate** | | `:33` |
| SS-9 | Cover newly hired state and local workers | small | **sourced** (revenue tab) | | `:34` |
| SS-B1 | Across-the-board increase about $200 a month | **-1.46** | **sourced** (SSA 2023) | | `:61` |
| SS-B2 | Flat increase $50-100 a month | -0.4 to -0.7 | **estimate** | | `:62` |
| SS-B3 | Student benefits to age 22 | -0.05 | **sourced** (SSA 2023) | | `:63` |
| SS-B4 | Caregiver credits | not scored | | | `:64` |

SS-B2 paired with SS-5 and SS-6 "keeps the package near balance" (`:66`). Options not chosen: A (Bill Book expansion), C (solvency only), retirement age to 69 and chained CPI (priced only for a bipartisan path) (`:68-74`); other priced options in governing `:207-218` (remove cap without donut +2.5 to +3.0; cap at 90% of earnings +0.8 to +1.0; rate to 14.4% over 20 years +1.3 to +1.6; equities +0.5 to +1.0; retirement age 69 +1.0 to +1.3; chained CPI +0.5 to +0.6).

### 4.3 Dollars (2030-39, trust fund, outside the general fund)

| Item | Value | Basis | Where |
| --- | --- | --- | --- |
| SS-1 receipts | **$3.67T** (range $3.3-3.9T; dedicated-funds table shows $3.68T) | **estimate** (SSA single-year scores from 2031) | `domain-social-security.md:79`; `dedicated-funds.md:33`; ledger O1 `:426` |
| SS-2 receipts | $1.48T before the haircut; **$1.26T** after (range 1.30-1.65 before haircut) | **estimate** | `domain-social-security.md:79`; ledger O2/OX `:427-428` (OX = -$0.22T) |
| Combined trust-fund revenue | about **$4.93T** at the midpoint (3.67 + 1.26) | **estimate** | `domain-social-security.md:81` |
| Benefit costs (SS-3, SS-4, SS-1 credit) | about **$0.19T** (range $0.15-0.25T); the dedicated-funds table gives SS-3 -$0.02T and SS-4 -$0.17T (sum $0.19T) without a separate credit line | **estimate** | `domain-social-security.md:80`; `dedicated-funds.md:35-36`; ledger SS-1 row `:315` |
| SS-5 receipts | +$1.32T (not in the ledger rows O1/O2/OX) | **estimate** | `dedicated-funds.md:37` |
| Older SS-1 figure | $1.9T scaled from a CBO score (nets out income-tax offset; "not what the trust fund receives"); CBO via CRFB $1.6T 2025-34 | **scaled** | `domain-social-security.md:79`; `revenue-channels...:28` |
| Ledger SS-1 row | Cost 0.19 (0.15-0.25); "own revenue 3.000" column; 8 floor days; felt "unverified"; durability 92; basis "estimate" | | ledger `:315` |
| Household test | SS-1 key `above250k_wages` Q1-Q5 = 0 / 0 / 0 / 2 / 98 (top 1% 55); SS-2 key `inv400k` 0 / 0 / 0 / 0 / 100 (top 1% 85); SS-3/SS-4 benefits key `ss_benefit` 30 / 28 / 20 / 13 / 9; F5 benefit $0.19T | **estimate** keys | `models/data/inputs/incidence-keys.csv`; `incidence-rows.csv` (O1, O2, F5) |
| Top-rate stack | SS-1, SS-2 and the 5% Medicare rate (H1b) stack to about **57%** federal on wages and interest above $400K | **estimate** | governing `:201`; ledger `:379` |

### 4.4 SSA's own provision scores that anchor the model (checkable outside sources)

`models/data/inputs/funds-ss-ssa-summary.csv` (each with an ssa.gov/oact/solvency/provisions table URL, 2026 Trustees basis): E2.1 +2.55; E2.5 +2.52; E2.17 +2.33; E2.14 +2.41; F9 +1.32; F11 +1.22; F8 +0.93; F10 +1.81 (F10 taxes investment and pass-through together at $400K; F11 + F8 = 2.15, so "stacking SS-2 and SS-5 likely overstates them by up to a few tenths of a point", `dedicated-funds.md:15`); A6 -0.33; B5.2 -0.11. Model rebuild check against SSA: differences -0.00 to -0.02 (`dedicated-funds.md:19-27`). These are the legacy's best-sourced Social Security numbers.

### 4.5 Integrated recovery-budget view (not the D8 baseline)

- SS case in the recovery model: baseline plus SS-5 **plus a two-point broad payroll rate on the capped base, phased 2035-44**, an authored joint-interaction adjustment of **-0.34** payroll points, and a 12.5% income-tax offset; result "approximately **+0.50%**-of-payroll actuarial balance", passing the combined-fund reserve test through 2100; "not a joint SSA score, does not certify OASI and DI separately" (`recovery-and-solvency-budget.md:96`; `assumptions.json` `social_security`; `models/data/recovery-budget.json` `ss_actuarial_balance` 0.4953). **That two-point closer is not selected** (governing `:448`, `:450`; `domain-social-security.md:3`). The regenerated index reads "Combined OASDI: actuarial balance +0.495% ... conservative model solvency: False" (`legacy/index/recovery-budget.md:57`, `:61`).
- SSA administrative staff are split by current-law financing; trust funds pay their shares, general fund pays the SSI and Climate Dividend work (governing `:501`).
- Narrative vs regenerated: the assessment says the mixed budget's debt ratio falls to 113.9% by 2056 (`recovery-and-solvency-budget.md:72`, `:114`), whereas the regenerated `legacy/index/recovery-budget.md:7-12` shows 304.3% in 2056 for the same case name, because later integrations (climate, health, family) were included. Do not quote the 113.9% as current.

### 4.6 SS-10 (Warren-Moreno / Talarico scenario) and vote premise

Option, not chosen; "D8 stands unless Espen changes it" (`domain-social-security.md:38`). Real-world basis: June 23, 2026 Warren-Moreno New York Times op-ed to lift the payroll cap; "No bill text or design details beyond lifting the cap were found; the design below is a scenario" (`:40`). Scenario model: partisan bill fails 53-47 in March 2029; Trustees report moves OASI depletion to about Q3 2032; Finance negotiates through the summer with a majority-rule carve-out "sitting at 53 as leverage"; signed January 9, 2030 at 67-33 (`scenario-talarico-2029-2037.md:108-109`, `:93`). Modeled trade (scenario design, not scored): Democrats get the cap lifted entirely, minimum benefit at 125% FPL (SS-3), caregiver credits (SS-B4), permanent WEP/GPO repeal (already law since January 2025); Republicans get a bend-point adjustment for the top 8% of lifetime earners, no investment-income inclusion (no SS-2), no payroll-rate increase (no SS-7), a "donut" exempting earnings between the current cap ($184,500) and $400,000 closing by 2040, and an enhanced benefit for long-career low-wage workers. Result "solvent to 2081 ... The model's own figure; it has not been scored by SSA's actuaries" (`domain-social-security.md:42-45`; `scenario-talarico...:109`, `:147`: "~4M seniors out of poverty; unrepealable at 67 votes"). Cost of the trade to the base case: drops SS-2 (about +1.1 to +1.36 of balance and $0.75-1.2T in-window revenue) (`:47`). Options: SS-10A (pursue first, D8 as fallback), SS-10B (D8 with SS-10's minimum-benefit and long-career pieces), SS-10C (D8 only) (`:51-53`). Timing: a 2029 negotiation, not a spring-2030 floor bill; moving SS to a negotiated bill saves about 17 floor days at 25 days per fight (ledger `:154`; `frameworks/scenario-stress-test-talarico-2029-2037.md:13`, `:54-56`, `:74`). **Needs**: an SSA actuarial score of the trade; a D3 check of the bend-point change; Espen's decision; re-test of the 67-vote premise (Has Warren-Moreno legislation been introduced? who cosponsors?) (`domain-social-security.md:55`, `:98-104`). Scenario claim "A 54-vote Social Security law is a repeal target for forty years. A 67-vote one is settled" is the scenario's, not evidence (`scenario-talarico...:232`).

### 4.7 Vintage and the 2029 baseline

All SS numbers are 2026 Trustees vintage (`funds-ss-rates.csv`, `funds-ss-economics.csv`; taxable payroll 2030 $13,258B). The January 2029 baseline will rest on the 2027 and 2028 reports (not yet published today), so the gap, depletion year and every "share of gap" figure (64%, 84%) must be restated against the later report when available. P.L. 119-21's tax-on-benefits effects are in the 2026 report by construction **[not in repo, verify]**. The OASI/DI legal separation, an SSA score of the whole package, and HI calibration remain open (`recovery-budget.md:63`; `domain-social-security.md:104`).

---

## 5. LAB-10 and income support

### 5.1 LAB-10 (participation support; approved October 26)

| Item | Statement | Basis | Where |
| --- | --- | --- | --- |
| Envelope | **$100B FY2030-39** "working envelope" for practical access to employment, education, training and community participation; carried once by `participation_tn` = 0.1 in `recovery-adoption.json` | **estimate**; "The budget is an envelope, not proof of a particular number of successful placements" | `legacy/domains/domain-labor.md:279-283`; `recovery-and-solvency-budget.md:88`; governing `:442`; `models/data/inputs/recovery-adoption.json` |
| Institution | DOL leads through existing employment/training institutions with education, disability, care and housing agencies; "a proposed institutional home, not a claim that current American Job Centers have the authority, funding or capacity" | | `domain-labor.md:281`; `legacy/sources/fiscal-redesign-and-participation-2026-10-26.md:23` |
| Supports | transport, child care during training, accommodations, navigators, paid placements; preserve apprenticeships and national service; coordinate with AI-4; "A person need not prove AI caused displacement. Participation is an offer, not a work condition on income, housing, health or food assistance." Notice, appeal, accessible help; "do not claim a placement count from an expenditure envelope" | | `domain-labor.md:281-283` |
| Related | AI-4 reduced from $0.20T to **$0.12T** (ordinary displacement support; "sits on the unemployment-insurance base"); DOL administration of LAB-10 and AI-4 sits inside those rows (capacity CSV rows 129, 189) | **estimate** | `domain-ai.md:16`, `:98`; `domain-labor.md:190`; `legacy/sources/capacity-recovery-components.csv` |
| Net budget effect | Reducing AI-4 and capacity, adding $100B participation, $135B rental expansion (HOU-4D, since rebooked to $115B/$0.115T in the current input file), $100B delivery contingency: additions $335B; "$570B gross CAP/AI reduction, less those additions and the $200B IRS allowance, leaves only $35B net primary improvement" | | `recovery-and-solvency-budget.md:90`; `recovery-adoption.json` |
| Espen's direction | A decent life "should be attainable regardless of ability to compete or work, or family arrangement"; no needlessly complex work requirements; "Continue exploring support under the basic housing, health, food and income floor, including wider rental assistance" | decision | governing `:408` |
| Delivery rules | Participation cannot presume someone no longer needs disability or housing support; know consequences of trying work; prompt reinstatement; "Do not fund this by assuming benefit exits"; measure "sustained good work, learning progress, accessibility, income stability"; "Preserve the basic floor if a service is declined" | | `fiscal-redesign-and-participation...:25`, `:33` |
| Open | vehicle, precise eligibility, benefit caps, launch capacity | | `domain-labor.md:283` |

### 5.2 SNAP, SSI, UI, TANF, EITC

There is **no policy design, option ID, cost or model** for any of these in the legacy tree. What exists:

- **EITC**: only in the child-poverty comparator (EITC + refundable ACTC removal lifts 6.14M people and 3.25M children out of SPM poverty, section 1.2); the NASEM PO12 modified EITC/CTC (section 1.7); and the Talarico scenario's budget line "Less EITC expansion for childless workers -$0.12T" (`scenario-talarico-2029-2037.md:132`, scenario only). Census `SPM_EITC` is kept in baseline resources; adding it again would double count.
- **SNAP**: as an input to the child-poverty model's baseline (`SPM_SNAPSUB`) and as the Summer EBT eligibility proxy (185% FPG "or `SPM_SNAPSUB` > 0", `agenda_analysis.py:283`); school meals and Summer EBT are EDU-3 (not in this flagship). No SNAP policy row.
- **SSI**: only in SSA administrative cost routing ($4,659M of SSA's FY2026 LAE; general fund pays the SSI share; governing `:501`; `capacity-round-two-integration.md:8`) and Climate Dividend delivery (automatic payment to Social Security, SSI, VA and Railroad Retirement beneficiaries, `domain-climate.md:89`). No SSI benefit design.
- **Unemployment insurance**: AI-4 "sits on the unemployment-insurance base" (`domain-labor.md:190`); "domain-labor.md for unemployment insurance and labor standards" (`domain-ai.md:100`). No UI design in either file.
- **Income floor**: Espen's "basic housing, health, food and income floor" direction (governing `:408`); "preserve the basic floor" as selected direction (governing `:432`); unconditional claim behind the basic floor (strategic assessment `legacy/sources/project-2050-strategic-assessment-2026-10-25.md:27`). The **recovery model's universal adult credit** ($300 per adult annually in 2030 dollars, CPI-indexed, half-year in FY2029; cost $0.916T 2030-39; "Someone unable to work receives the adult credit and retains the basic floor") was a modeled financing/protection device, and the $300 and $1,500 credits were **not selected** (`recovery-and-solvency-budget.md:53-80`, `:110`; governing `:450`). Figures kept: $300 credit, fourth-quintile net 2039 -$2,697 (mixed) / -$4,307 (larger payroll); the $1,500 credit costs $4.579T with $4.023T of new AGI receipts, Q4 about -$392, debt/GDP about 118.4% in 2056, and about $207B extra FY2029 primary borrowing (`recovery-and-solvency-budget.md:66-78`); the dossier README correctly treats these as outside this flagship's design record (`dossiers/secure-floor/README.md:51`).
- **Fiscal redesign**: "a defined initial band of earnings, refundable credit ... with a nonworker component" for protecting workers from stacked contributions (`recovery-and-solvency-budget.md:80`) is a different instrument (contribution relief), unpriced; "I have not booked unpriced savings from targeting".
- **Stacked phase-outs / income definitions**: the stacking problem is acknowledged only for taxes (SS-1, SS-2, H1b ~57% top rate; leave plus education plus SS payroll accumulation making Q4 negative); no benefit-cliff analysis exists in legacy.

---

## 6. Figures the dossier should restate

Basis tags: sourced / scaled / estimate / model result / scenario. "Validated" means checked against an external benchmark or primary score, not merely unit-tested. "Superseded" or "conflict" flags are in the last column.

### 6.1 Child benefit and child poverty

| Figure | ID | path:line | Basis | Status | Validated? |
| --- | --- | --- | --- | --- | --- |
| Child SPM poverty 13.3913% (2025 resources, CPS ASEC 2026); 9,652,806 poor of 72,082,590 children | baseline | `legacy/sources/family-child-poverty-cps-baseline.md:36-38` | model result on data | sourced to Census data | **Yes**: reproduces the published 13.4% and all-age 16,941 / 44,390k counts |
| Deep poverty 3.4447%; below 150% 32.5302%; SE 0.3425 pp; 95% 12.7200-14.0626% | baseline | `cps-baseline.md:39-42` | model result | model result | Yes (sampling only) |
| EITC + refundable ACTC removal lifts 6.14M people / 3.25M children (internal 6.1M / 3.3M) | comparator | `agenda-effects.md:98`; `family-child-poverty-comparator-register.csv:7` | model result | model result | **Yes**, tolerances 0.25M / 0.15M |
| Adopted package child poverty 8.73 / 8.34 / 8.09% (moderate / enhanced / full) vs 13.40% | FAM-1D + HOU-4A (1,000,000) | `family-comparison-model-checks.md:44-48` | model result | model result (conditional static analogue) | **No**: assumptions unvalidated; $2,000.04 retained reference; no SSN rule |
| Deep poverty 1.97 / 1.85 / 1.78% | FAM-1D + HOU-4A | same | model result | model result | No |
| Poor children 5.83M / 5.57M / 5.40M vs 8.95M; lifted 3.12M / 3.38M / 3.55M; deep-poor 1.31M / 1.24M / 1.19M vs 2.30M; paired change -5.08 to -4.26 / -5.49 to -4.63 / -5.77 to -4.87 pp | FAM-1D + HOU-4A | `family-comparison-model-checks.json` `adopted_cases` | model result | model result (2034 CPS-anchored population 66.75M) | No |
| Expected leases 650,000 / 850,000 / 1,000,000 of 1,000,000 awards | HOU-4A | JSON `adopted_cases`; `adopted-package.json` | assumption (lease-up 65 / 85 / 100%) | estimate | No |
| 2034 / 2040 / 2050 labels: 8.73 / 8.34 / 8.09%; -5% stress 9.44% (baseline 15.35%); +5% stress 6.88% (baseline 11.66%) | later-year paths | `family-comparison-model-checks.md:50-56`; `family-later-year-scenario-paths.json` | model result | "not a forecast" | No |
| AFA at 400,000 awards: 8.89 / 8.55 / 8.33%; 2030-face 9.34 / 9.02 / 8.81%; no-bonus 8.95 / 8.61 / 8.40%; FAM-1A 10.29 / 10.03 / 9.87% | FAM-1A / 1D | `family-comparison-model-checks.md:23-34` | model result | model result | Only the 10.29% was reproduced exactly (regression gate) |
| 400k -> 1M awards at enhanced delivery: FAM-1A 10.03 -> 9.80%; AFA 8.55 -> 8.34% | HOU-4A | `:35-36` | model result | model result | No |
| Proxy-eligible renter boundary: 6,755,114 awards, 5.74M leases: FAM-1A 7.52% / 1.34%; AFA 6.32% / 1.16% | HOU-4C (not adopted) | `:37-38` | model result | exploratory, not priced | No |
| Historical FAM-1A cases: 2030 11.08 / 10.61 / 10.36 / 10.17%; 2034 10.80 / 10.29 / 10.03 / 9.87%; deep 2.57-2.27% (2030), 2.47-2.13% (2034); 1.60-2.23M / 1.74-2.36M fewer poor | FAM-1A | `agenda-effects.md:15-22` | model result | **historical** | Partly (accounting validated) |
| Channel order: 10.85 / 10.71 / 10.60 / 10.57 / 10.61% (2030); 10.86 / 10.70 / 10.36 / 10.23 / 10.29% (2034) | FAM-1A, FAM-2A, EDU-3, HOU-4A, FAM-3 | `agenda-effects.md:34-43` | model result | historical, not additive | No |
| Sensitivities (index from 2025: 10.10 / 9.69%; resource -5%: 12.32 / 11.88%; +5%: 9.13 / 8.75%; others in 1.6) | FAM-1A | `agenda-effects.md:57-66` | model result | historical | No |
| Remaining poor 2034 moderate: 6.87M poor, 1.52M deep, 6.59M at full; positive earnings 72.96%, renters 64.86% | FAM-1A | `agenda-effects.md:78-92` | model result | historical | No |
| Credit amounts: AFA $300 / $360 / $2,400 first month; $3,600, $4,320, $6,360 annual exposures; Maya $7,920 / $660 | FAM-1D | `legacy/domains/domain-family.md:19`; `family-security-public-example.md:7` | sourced to bill text (H.R.2763 / S.1393), not current law | sourced (arithmetic) | Not verified against bill text here |
| Current-law CTC parameters $2,200 / $2,400 / $2,600; refundable $1,700 / $1,900 / $2,100; ODC $500; threshold $2,500; 15% | current law | `target-year-preparation.md:21-27`; `empirical/cbo-ctc-parameters-2026-02.csv` | sourced (CBO Feb 2026) | sourced (projection) | Sourced; consistent with P.L. 119-21 **[verify]** |
| FAM-1D cost $1.7 / $1.9 / $2.1T (2030-39); FAM-1A $1.5T; FAM-1B about $0.45T; FAM-1C about $0.3-0.5T | FAM-1, 1A-1D | `domain-family.md:9`, `:31-34` | estimate / scaled | **estimate**; no score | No (TPC about $1.4T FY2026-35 anchor) |
| Midpoint change +$0.49T (credit +$0.40T, vouchers +$0.09T); vouchers $0.10 / $0.15 / $0.1875T; subtotal $2.42 / $2.92 / $3.5175T | FAM-1D, HOU-4A | `family-adoption-architecture-bridge.md:25-30` | scaled / estimate | working | No |
| FY2040 GF primary shortfall $53.7B (0.099% of GDP); D4 maturity fails; debt 155.1% (2056) vs 180.2% | financing | `bridge.md:38-40`; `family-financing-comparison.md:5` | model result | model result (old cash proxy) | No |
| Financing routes: corporate 31% +$566B; payroll 0.35 pts +$560B; median exclusion cap +$590B | financing options | `family-financing-comparison.md:9-11` | model result | not adopted | No |
| F1 per Q4 household $814 a year; keys 33 / 30 / 21 / 12 / 4 | D3 | `revenue-household-incidence-model.md:54`; `incidence-keys.csv` | estimate | provisional | No |
| Reports 1-3 comparators: NASEM 13.0% -> -5.3 pp; 11.1% -> 6.5% (7.0 / 7.2 / 7.4%); GAO 15%; HUD 69% | evidence | `family-child-poverty-report-1.md:25`, `:27`, `:82`, `:102` | sourced (secondhand, via model research report) | sourced | Not checked here |
| Model tests: 117 pass | tool | `models/tools/child-poverty/README.md:3` | model result | confirmed Nov 12, 2026 | Logic only |

### 6.2 Paid leave

| Figure | ID | path:line | Basis | Status | Validated? |
| --- | --- | --- | --- | --- | --- |
| Cost about $0.9T (range $0.6-1.4T) | FAM-3 | `legacy/domains/domain-family.md:72`; ledger `:308` | estimate | estimate | No |
| CBO $547B (12-week FAMILY Act-based) | FAM-3 | `domain-family.md:72`, `:127` | sourced (secondhand AAF) | sourced | Not independently |
| JCT break-even 0.85% of wages; "0.4% CBO-linked rate" | FAM-3D | `domain-family.md:72`, `:87`, `:127` | sourced (secondhand AAF) | sourced | Not independently |
| Contribution 0.6% (0.3% each side) raising about $0.9T on about $15T covered wages | FAM-3A, REV-P1 | `domain-family.md:73`; ledger `:429` | estimate | estimate | Model: $0.97T (`dedicated-funds.md:57`) |
| Step-up 0.05 points each January; down above 18 months; cap now **1.10%** (was 0.85%) | FAM-3A | `domain-family.md:75`; `options-register.md:130`, `:409` | decision (Espen, Oct 26) | decided | Model-tested |
| Treasury loan $184B (2039), $865B (2050) at 0.85% cap, high take-up; domain estimate $120B | FAM-3 | `dedicated-funds.md:63`, `:65` | model result | **superseded** by 1.10-cap run | n/a |
| Loan repaid **2048** | FAM-3A | `domain-family.md:75`; `recovery-and-solvency-budget.md:100` | model result | **superseded** | n/a |
| Loan repaid **2058**; peak about $185B in 2040; rate reaches 1.10% in 2041; 2030-39 receipts $1.285T, benefits $1.400T, administration $45B | FAM-3A | `legacy/index/recovery-budget.md:59`; `capacity-round-two-integration.md:18`; `models/data/recovery-budget.json` | model result | current central | Model-tested; assumptions unscored |
| SSA admin 3% of benefits + $3B startup (original about $30B, range $18-60B, 2-6% band) | FAM-3 | `capacity-recovery-other-agencies-review.md:26-28`, `:188`, `:228`; `capacity-round-two-integration.md:7` | estimate | estimate | Admin-share arithmetic only |
| 6% admin: loan not repaid by 2100, about $96B outstanding | FAM-3 | `capacity-round-two-integration.md:20` | model result | model result | no |
| Mature cost 0.43% / 0.65% / 1.01% of payroll (low / mid / high); benefit ramp 50% / 80% / 100% | FAM-3 | `dedicated-funds.md:61-63`; `funds-parameters.csv` | estimate | estimate | No |
| Household test $180 (0.6%) and up to $330 (1.10%) for a $60,000 worker | FAM-3, D3 | `domain-family.md:77` | estimate (arithmetic) | estimate | Arithmetic checks |
| P1 $964 and F3 $900 per Q4 household; keys 3 / 10 / 19 / 30 / 38 and 8 / 17 / 24 / 28 / 23 | D3 | `revenue-household-incidence-model.md:52-53`; `incidence-keys.csv` | estimate / model result | at 0.6% and $0.9T | No |
| DY6 +$0.15 / +$0.22 / +$0.30T employment effect (child care, pre-K, leave) | FAM-2, FAM-3 | ledger `:133` | estimate | in no total | No |
| Leave contribution as 0.3% child-poverty cost stress (10.57 -> 10.61%) | FAM-3 | `agenda-effects.md:43`, `:51` | model result | historical | No |

### 6.3 Social Security

| Figure | ID | path:line | Basis | Status | Validated? |
| --- | --- | --- | --- | --- | --- |
| 75-year deficit 4.42%; depletion 2034; 83% payable | SS | `domain-social-security.md:9`; `revenue-channels-and-full-menu.md:13`, `:188` | sourced (secondary) | sourced | Model matched 2034 / 83% / -4.45% (`dedicated-funds.md:13`) |
| OASI depletion "as little as six years", about 2032; cut 20-25% (about 23%) | SS-10 premise | `domain-social-security.md:11`; `scenario-talarico...:25`, `:28` | sourced (secondhand), "as reported" | sourced, unchecked | **No** |
| SS-1 +2.30 (3.67T, range 3.3-3.9T) | SS-1 | `domain-social-security.md:17`, `:79`; `dedicated-funds.md:33` | estimate on SSA scores | estimate | SSA provision scores reproduced within 0.02 |
| SS-2 +1.17 / +0.99 after 15% haircut ($1.48T -> $1.26T) | SS-2 | `:18`, `:79`; `dedicated-funds.md:34` | estimate (SSA F11 +1.22 sourced; haircut estimate) | estimate | F11 reproduced |
| SS-3 -0.11 | SS-3 | `:19`; `dedicated-funds.md:35` | sourced (SSA B5.2) | sourced | Yes (SSA table) |
| SS-4 -0.33 | SS-4 | `:20`; `dedicated-funds.md:36` | sourced (SSA A6) | sourced | Yes (SSA table; model -0.35) |
| SS-5 +0.87 (SSA F8 +0.93 from 2027; +$1.32T) | SS-5 | `:30`; `dedicated-funds.md:37` | sourced, moved to 2031 | sourced / estimate | Source yes |
| Baseline +2.85 = 64% of gap, depletion 2062, 1.6% remains | SS-1 to SS-4 | `:21-24`; `dedicated-funds.md:42` | estimate | estimate | **No SSA package score** (open item 2, `:104`) |
| With SS-5: 84% (88% before haircut), depletion 2081, 0.7% remains | SS-1 to SS-5 | `:36`; `dedicated-funds.md:43` | estimate | estimate | No |
| SS-6 +0.1 (domain) vs +0.3-0.6 (register) | SS-6 | `:31`; `options-register.md:185` | sourced difference vs estimate | **conflict** | No |
| SS-7 +0.9 to +1.0; SS-8 +0.5 to +1.0; SS-9 small | SS-7 to SS-9 | `:32-34` | estimate / sourced | estimate | No |
| SS-B1 -1.46; SS-B2 -0.4 to -0.7; SS-B3 -0.05; SS-B4 unscored | SS-B1 to SS-B4 | `:61-64` | sourced (SSA 2023) / estimate | sourced vs 3.42% base | Source yes |
| Ten-year: SS-1 $3.67T; SS-2 $1.26T ($1.48T before haircut); benefits about $0.19T ($0.15-0.25T) | SS-1, SS-2 | `:79-81`; ledger `:315`, `:426-428` | estimate | estimate | No |
| Recovery case +0.50% payroll (includes unselected two-point closer) | recovery | `recovery-and-solvency-budget.md:96`; `legacy/index/recovery-budget.md:57` | model result | **not selected design** | No |
| SS-10 "solvent to 2081" (Warren-Moreno trade), 67-33 | SS-10, SS-10A-C | `domain-social-security.md:45`; `scenario-talarico...:108-109` | scenario | scenario, "not scored" | **No** |
| Top rate stack about 57% | SS-1, SS-2, H1b | governing `:201` | estimate | estimate | No |

### 6.4 LAB-10 and income support

| Figure | ID | path:line | Basis | Status | Validated? |
| --- | --- | --- | --- | --- | --- |
| LAB-10 $100B FY2030-39 | LAB-10 | `legacy/domains/domain-labor.md:281`; governing `:442` | estimate (working envelope) | decided allocation | No |
| AI-4 $120B (was $200B) | AI-4A | `domain-ai.md:98`; governing `:441` | estimate | decided | No |
| HOU-4D +$135B in legacy (now $115B in input file) | HOU-4D | governing `:443`; `recovery-adoption.json` | estimate | check current value | No |
| Universal adult credit $300 (cost $0.916T); Q4 -$2,697 / -$4,307; $1,500 variant $4.579T | recovery | `recovery-and-solvency-budget.md:66-78` | model result | **not selected** | No |
| EITC expansion for childless workers -$0.12T (Talarico) | scenario | `scenario-talarico...:132` | scenario | scenario | No |
| SNAP / SSI / UI / TANF | none | n/a | none | **no legacy design or cost** | n/a |

### 6.5 Internal inconsistencies to resolve in the dossier rather than copy

1. Loan repayment 2048 (`domain-family.md:75`, `recovery-and-solvency-budget.md:100`) vs 2058 (`recovery-budget.md:59`).
2. Leave cap text "stepping toward 0.85%" in the ledger and incidence inputs (ledger `:308`, `:429`; `funds-parameters.csv` `leave_cap` 0.85) vs the selected 1.10% cap.
3. $0.9T (mid take-up) vs $1.4T (the take-up the recovery budget uses).
4. SS-6 +0.1 vs +0.3-0.6; E2.16 +2.37 vs +2.35; E2.14 described as a 2027 version in `domain-social-security.md:17` but it starts 2028 (`funds-ss-ssa-summary.csv`).
5. Benefit cost $0.19T described as SS-3 + SS-4 + SS-1's credit (`:80`) but the funds table gives SS-3 $0.02T + SS-4 $0.17T (`dedicated-funds.md:35-36`); SS-5's $1.32T is in no ledger row; ledger SS-1 shows own revenue 3.000.
6. Recovery narrative debt 113.9% (2056) vs regenerated 304.3%.
7. Bridge Q4 +$1,373 vs regenerated scenario Q Q4 -$1,038; the regenerated page also says "gains about -$1,038" (`revenue-household-incidence-model.md:15`), a sign slip.
8. Archive provenance (point 8, section 0).
9. FAM-1D retained reference $2,000.04 vs current $2,200 (section 2).
10. Scenario OASI date Q3 2032 (`scenario-talarico...:108`) vs Q4 2032 (ledger `:282`).
