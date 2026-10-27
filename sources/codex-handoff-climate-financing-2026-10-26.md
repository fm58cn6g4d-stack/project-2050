# Codex handoff: carbon price integration, climate payment and reinsurance (Oct 26, 2026)

**From:** Claude Code (session_01SWGgUF3Bj4gThFLoeJSLwc). Branch `claude/climate-financing`, from `main` at `55a675f`.

**Why Claude touched shared inputs.** While Codex was offline, Espen wrote: "i want to let you edit the carbon price adjustment since codex is offline for another hour and a half". He added: "it's ok for you to make design choices in place of codex, just ask me to approve, and then leave clear notes for codex to get up to speed once back online". The price was already decided (Espen, Oct 26). Two further designs need Espen's approval before anyone books them: payment option O5 and CLI-7C. Both are recorded only in Claude's research files.

## 1. What changed in shared inputs (commit `d8692b1`)

| File | Change |
| --- | --- |
| `index/data/inputs/carbon-parameters.csv` | `c1_price_2037` 100 → 150. New `c1_slope_2037` = 100 and `c1_kink_year` = 2032, so 2030-32 keep D7's original steps ($25, ~$36, ~$46) and the price then rises linearly to $150 in 2037. Growth is 5% a year after that, unchanged. |
| `index/tools/carbon-model.py` | `d7_nominal` reads the two new parameters. With them absent, the path reduces to the old linear one. Docstring and text updated. |
| `index/data/inputs/ledger-revenue.csv` | C1 lo/mid/hi 1.65 / 1.90 / 2.10 (was ~1.25 / 1.45 / 1.60). Carbon model $2.00T; the midpoint is set lower, as in the Oct 21 method. CX −0.54 / −0.49 / −0.42 (was about −0.38). |
| `index/data/inputs/ledger-bills.csv` | CLI-2 cost 1.32 / 1.52 / 1.68, own_revenue 1.90. |
| `index/tools/test_ledger_rounding.py` | GF-base pin 5.99 → 5.88, with a comment. |
| `index/tools/fiscal-recovery/comparison-rebase.json` (new) and `model.py` | The education bridge refuses changed comparison inputs. The two ledger files are rebased **explicitly**, with their sha256, reason and approval line. The guard accepts a changed hash only if it matches this file. Codex owns that bridge: keep the mechanism or replace it with your preferred rebase. |
| `index/tools/strategic-review/test_analysis.py` | The corporate-route check now compares the **increment over DEC** (−$69.06B in FY2040 both before and after). The stored report was on the old baseline. `MANIFEST.sha256` in that folder, like `index/tools/fiscal-recovery/MANIFEST.sha256`, is a historical record and was not re-hashed. |
| Headline docs | `domain-revenue.md`, `domain-climate.md`, `governing/project-2050-governing-decisions.md` (lines 100, 104, 136) and `index/revenue-assignment-audit.md` are updated to the regenerated figures. The check report shows 0 stale headlines and the same 5 reconcile rows as main. |
| Regenerated outputs | `run-all.sh --write` regenerated recovery budget, fiscal-recovery model, ledger, incidence, long-term model, dedicated funds, carbon model and dashboards. `.github/scripts/run-checks.sh` passes. |

**Headline moves:**
- GF claims $11.59T → $11.50T.
- Top-end base $5.99T → $5.88T.
- Gap $5.60T → $5.62T.
- Gap after accepted options +$0.74T → +$0.76T.
- DEC ten-year GF primary deficit $2.03T → $2.05T.
- 2056 debt 155.1% → 155.7%.
- **DEC FY2040 GF primary gap $53.7B → $71.9B (0.133% of GDP)**.
- Incidence scenario Q, fourth quintile, +$1,373 → +$1,261.

**For Codex to check:**
- D3 incidence at the higher price. The top two quintiles pay more fee and all get a larger dividend. As your review notes, scenario Q's +$1,261 fourth-quintile ten-year average is not a whole-recovery pass: the mixed recovery case has Q4 at −$2,906 in FY2039, and the historical Q screen has −$1,413 in 2030. Household protection is not secured; that belongs to the revenue settlement.
- Whether the $18B FY2040 deterioration changes the revenue settlement's sizing. Part of it comes from the C1 and CX year shapes now following the carbon model (`incidence-phase-in.csv` C1, `fiscal-years.csv` CX; PR #37 review).

**The $150 step's transition share is already spent.** `ledger-build.py` computes CLI-5's own revenue as 0.2 × C1 + C2 + C3, so the step's ~$0.09T lowers CLI-5's general-fund residual (0.26 → 0.17). That is part of why claims fell to $11.50T. An earlier draft called it "unassigned"; the reviewer caught that, and the CLI-5 row's own-revenue column (0.43) and note now match the computed value.

## 2. Climate package (research paths only; proposed deltas)

**Package A** now contains:
- the floor measures: a clean-heat standard and clean-industry support at 50%;
- standard-led credits;
- CES 90/100;
- car and truck ZEV standards;
- public grid;
- tripled retrofits;
- the process fee.

Against the decided package at $150, it reaches 48.0% / 62.8% / 74.4% below 2005 (2035 / 2040 / 2050) for +$12B of outlays over 2030-39 (2025 $). It meets the 50% domestic floor at the CLI-13 mid estimate, narrowly (50.0%), so international results count (mid total about 57.8%). The clean-heat standard starts in 2032 (`hpPremPolicy`/`hpPremYear` in `cfd-model.js`, default off), per your review. Details: [allocation](climate-portfolio-allocation.md), [packages](climate-portfolio-packages.md), [pricing](climate-portfolio-pricing.md), [international](climate-portfolio-international-pricing.md).

The proposed ledger deltas are unchanged in kind from PR #26, with the sizes updated:
- CLI-1 → about $0.72T;
- new CLI-10G, lean tranche, about $0.04T, D4-B;
- CLI-5W $67.5B (2025 $);
- CLI-9 at 50%, about $0.11T nominal;
- CLI-13 forests about $0.03T;
- CLI-7 core and fuller disaster tiers.

The CLI-1/CLI-5 split of the credit scaling is still open.

## 3. Payment: proposed O5, pending Espen

Four options are computed in `pricing.py` (`budget.payment`). O4 was withdrawn because it double counted the step. Under O5:
- The process-emissions fee has its own account, like REV-C3.
- Each year, process receipts cover any remaining general-fund cost of the package. The remainder goes to the dividend under D7.
- The combustion fee keeps D7's 80/20 split.

Results (nominal $B, favorable / central / conservative / unfavorable):
- GF 2030-39: −205 / +17 / +93 / +227.
- FY2040: −48 / −18 / 0 / 0.
- FY2050: 0 in all four cases.
- Dividend change per consumer unit: −$28 to −$51 a year over 2030-39 (lowest to highest quintile) and −$84 to −$154 in 2050.

Under D7 as is (O1), the GF figures are +75 central over 2030-39 and +18 in FY2050.

**If approved, ledger work for Codex:**
1. Add a process-fee row (REV-C1 coverage, about $0.24T gross over 2030-39, CX at 25%) with its waterfall.
2. Book the package's permanent items (disaster D2-D8, CLI-13 farm payments, bill protection) as covered by that waterfall in the FY2040+ test.

## 4. CLI-7C reinsurance backstop: designed, recommended, pending Espen

The design is a Treasury facility:
- It reinsures residential wind, wildfire, hail and opt-in earthquake losses between a state-level 1-in-100 and a 1-in-250 year loss.
- Insurers retain 10% of the layer.
- The cap is $150B a year.
- Only states with CLI-8 codes and disclosure qualify.
- Premiums are risk-priced at 1.3-1.5 times expected loss.
- Treasury borrowing authority covers draws, with a TRIA-style recoupment surcharge capped at 3% of residential premiums for up to 15 years.

**D4:**
- A permanent expected-net-cost line of −0.3 / +0.3 / +1.0 $B a year.
- A disclosed contingent liability of $75-150B.

It sits in `pricing.json` as tier `option`, so no budget figure changes until it is approved. See the [disaster file](climate-portfolio-disaster-resilience.md), D10.

## 5. Mechanical notes

- `packages.py` writes the full results (about 15 MB) to `build/` only. The committed JSON drops `results`, and no committed consumer reads them.
- The test for the retrofit lever now uses standard-led credits. Under kept credits at $150, the extra heat-pump load delays the IRA power-credit trigger (383 Mt) by a year, which adds about $51B of credits. That is real model behavior at a threshold, not a bug.
- `international.json` marks the floor measures as already inside Package A.
- Live queue: Claude did not change it. Update the climate row when you pick this up.
