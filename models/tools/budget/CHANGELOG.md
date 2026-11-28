# Federal budget model: changelog

Role: the version history of `MOD-budget` (`models/schema/README.md`, "Versions"), newest first. Status: current.

## 0.8.0 (2026-11-28)

Espen decided G29.1 (option 1, `DEC-2026-11-28-01`): every revenue source the plan has decided is booked wherever the models report it. New inputs and one engine hook; no change to the interface.
- **G24 B and PH-3 booked** as settlement items S12-S17 (`settlement.json`, `settlement-paths.csv`): the SALT-workaround fix and the itemized-deduction limits from FY2037, the AGI surtax from FY2040, the VAT at 2.88% from FY2035 with its rebate under G30 (`DEC-2026-11-25-14`, `-15`, `-16`, `DEC-2026-11-26-04`), and G17 B's hold on the clean-energy credits in FY2038-39 (`DEC-2026-11-25-03`). Priced by `models/bookings/fiscal_revision.py` `booking()`: $499.3B in FY2040 (the three steps $313.0B, the VAT net of its rebate $186.3B); PH-3 $47.2B over FY2038-39.
- **Engine:** `recovery-budget/model.py` gains `without_items()` and `revision_items()`, so a tool can build the booked case without the items it prices (fiscal_revision solves G24 B's VAT on the plan without G24 B; on itself it would solve to zero). Every case built otherwise carries them.
- **Results:** debt is 114.5% of GDP in FY2040, 113.3% in FY2045, 111.4% in FY2050 and 110.0% in FY2056, the decided goal (G23 B), against 117.8%, 121.4%, 124.5% and 129.3%. The general fund's gap is −$20.1B in FY2035 (+$57.3B), +$200.4B, +$83.9B and +$41.6B in FY2036-38, −$32.3B in FY2039, −$413.1B in FY2040 (+$86.2B), −$619.2B in FY2045, −$849.2B in FY2050 and −$1,071.5B in FY2056, and +$78.5B over FY2030-39 (+$1,225.9B). The health fund, its rate path and Social Security don't move.
- Current law and the CBO option change only in the hashes of the changed inputs.

## 0.7.0 (2026-11-27)

Espen changed G29 from C to A (`DEC-2026-11-26-03`): no law in the plan diverts Social Security payroll tax from the trust funds. One input changes; no change to the code or the interface. 0.6.0 was never on main.
- **G29 A:** the OASDI part of HX and HEX (0.28) goes to Social Security's trust funds from FY2031, HX's first year, as current law does (`settlement.json` `social_security_part` `from` 2031, not 2045). The recovery budget takes it off the general fund from then; HX-SS (`funds-ss-hx.csv`) starts in FY2031. Unified figures don't move.
- **Results:** debt is unchanged (121.4% of GDP in FY2045, 124.5% in FY2050, 129.3% in FY2056), as are the health fund's reserve ($250B standing, $62.7B drawn in FY2035) and the rate path. The general fund's gap is +$57.3B in FY2035 and +$86.2B in FY2040, falling to +$1.8B in FY2044 (it closed in every one of those years in 0.6.0); −$19.2B in FY2045, −$132.9B in FY2050 and −$189.4B in FY2056, as in 0.6.0; and +$1,225.9B over FY2030-39 ($718.5B). With the plan's package, Social Security's funds last to 2072, not 2069, and the 75-year balance is −1.07% of taxable payroll, not −1.17%.
- Current law and the CBO option change only in the hashes of the changed inputs.

## 0.6.0 (2026-11-26)

Espen's G29 and G30 decisions booked (`DEC-2026-11-26-03`, `-04`). New inputs and one new engine series; no change to the interface.
- **G29 C:** the OASDI part of the tax on former premiums (HX and HEX) is now 0.28, as memo G29 sources it, not the working 0.297 (`settlement.json` `source_shares` 0.72). It stays on the general fund through FY2044 and goes to Social Security's trust funds from FY2045 (`social_security_part`). The recovery budget takes it off the general fund from FY2045 (`social_security_part()`); the dedicated-fund engine books it as HX-SS (`funds-ss-hx.csv`, a new `direct` series). Unified figures don't move. With the plan's package, Social Security's funds last to 2069, not 2061, and the 75-year balance is −1.17% of taxable payroll, not −1.64%.
- **G29 R2:** a $250B standing reserve, with the rest of FY2030-34's surplus drawn against the FY2035 transfer: $312.7B built, $62.7B drawn, an FY2035 transfer of $304.6B. The rate rule, rerun on the $250B start, steps up in FY2043, a year earlier than in 0.5.0.
- **Results:** the plan's debt is 129.3% of GDP in FY2056, against 129.4% in 0.5.0. The general fund's gap is −$19.2B in FY2045, −$132.9B in FY2050 and −$189.4B in FY2056 (−$162.7B, −$322.2B and −$437.5B in 0.5.0), and $718.5B over FY2030-39 ($776.5B).
- **G30** is booked in `models/bookings/fiscal_revision.py` (the rebate's phase-out), not in this model's reference results.
- Current law and the CBO option change only in the hashes of the changed inputs.

## 0.5.0 (2026-11-26)

The health fund's sources weight HEX like HX (memo G29, finding 3; `settlement.json` `source_shares`). HEX, the tax on former premiums that the employer contribution takes back from HX, carries the same Social Security part as HX. 0.4.0 left HX's part out of the fund but kept HEX's take-back in full. A new input, with no change to the code or the interface.
- **Results:** the fund's reserve as built is $307.9B, up from $159.5B. The FY2035 transfer is $371.7B, down from $497.8B. The general fund's FY2030-39 gap is $776.5B, up from $628.1B, because the general fund now carries the take-back's Social Security part in FY2031-34. From FY2040 the general fund's gap doesn't move, since the law fixes its share.
- **The rate rule steps later:** 3.80% through FY2043, 4.05% FY2044-45, 4.30% FY2046-47, 4.05% FY2048-51, 4.30% FY2052-55 and 4.05% FY2056. The plan's debt in FY2056 is 129.4% of GDP, against 129.1% in 0.4.0 (0.4.0's entry says 129.3%, its figure before the HX fix). FY2040 stays 117.8%.
- Current law and the CBO option didn't move: their headers change only in the hashes of the changed inputs.

## 0.4.0 (2026-11-25)

Stage G step 11: the health fund booked as its own account (`DEC-2026-11-25-28`, `-30` to `-32`) and IMM-1 rebooked (I1 A, `-27`).
- **Interface:** the engine (`recovery-budget/model.py`) has a `health_fund()` account. Each case's rows add `health_fund_sources_bn`, `health_fund_spending_bn`, `health_fund_gf_transfer_bn` and `health_fund_reserve_bn`, and each case adds `health_fund`. The general fund's gap counts only the transfer to the fund. The settlement's S06 takes a rate path (`settlement.json`), and the funds model a third `direct` Social Security line, IMM-1-SS.
- **Results:** the plan's debt in FY2056 is 129.3% of GDP, down from 131.5% in 0.3.0: 2.0 points from the fund's rule and 0.1 from IMM-1. FY2040 stays 117.8%. The plan's general-fund gap moves in FY2030-35 with the fund holding its early surplus; unified figures don't. Current law and the CBO option didn't move: their headers change only in the hashes of the changed inputs.

## 0.3.0 (2026-11-25)

The plan's figures moved with CLI-1's step-down after FY2039 (memo G25; #493's `fiscal-after.csv` row): a new input, no change to the code or the interface.
- Results: the plan (`results/plan.json`) has debt at 131.5% of GDP in FY2056, 1.6 points below 0.2.0's 133.1%; FY2040 stays 117.8%. Current law and the CBO option did not move; their headers change only in the hash of `fiscal-after.csv`.

## 0.2.0 (2026-11-25)

Stage H step H4: the model released to the toolkit standard (not marked "released": memo H1 is undecided).
- One command, `run.py --reform FILE --out DIR`, from a fresh clone: the baseline, ledger, paths and funds into DIR, then the reform against current law. Current law is the default; `reforms/` ships current law, a neutral CBO option (Mandatory Spending Option 2, SRC-1855) and the plan as booked (case `mixed`).
- The engine (`fiscal-model.py`, `fiscal-data.py`, `fiscal-profiles.py`, `ledger-build.py`, `funds-model.py`, `climate-integration.py`, `window.py` and four tests) moved to `engine/`, with shims at the old paths; `fiscal-model.py` takes `--out-dir`. The plan's bookings and dossier tools moved to `models/bookings/`.
- The card on `models/MODEL-CARD-TEMPLATE.md`: evidence map from `parameters.csv`, the owner role, `MOD-budget`, status working, the validation-convention table, known issues.
- Results on the toolkit's schema: `results/*.json` with the header.
- Results: no figure moved. `run-all.sh` reproduces every committed figure; only the source hashes in `recovery-budget.json` and `fiscal-recovery-model.json` changed, because the engine files they hash moved.

## 0.1.0 (2026-11-12)

The budget model as built in pieces B1 to B6 (`WORKFLOW.md`): the data layer, the provision library, the benchmarks (B4 milestone met by `DEC-2026-11-12-11`), the viewer. No results header; versioned here for the first time.
- Results: the reference figures before step H4.
