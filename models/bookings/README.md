# The plan's bookings

Role: where the plan is booked on the federal budget model, kept apart from the models themselves so the released folders hold only models (stage H step H4; `models/stage-h/1-audit.md`, part 1.9). Status: current. Nothing here is part of `MOD-budget`: these scripts pin each dossier's booked figures in the model's inputs and stay in the project's checks (`models/tools/run-all.sh`).

| Group | Files |
| --- | --- |
| Dossier bookings | `care_booking.py`, `health_booking.py` (and `health_before_booking.json`, frozen), `clean_power_booking.py`, `immigration_booking.py`, `secure_floor_booking.py`, `work_booking.py`, `democratic_renewal_booking.py`, `settlement_booking.py` |
| Their checks | `test_fiscal_care.py`, `test_fiscal_health.py`, `test_fiscal_clean_power.py`, `test_fiscal_immigration.py`, `test_fiscal_secure_floor.py`, `test_fiscal_work.py`, `test_fiscal_democratic_renewal.py`, `test_fiscal_counting.py`, `test_fiscal_mr6.py`, `test_fiscal_health_financing.py`, `test_settlement_booking.py` |
| The fiscal path analyses (stage G steps 8 and 9) | `fiscal_path.py`, `fiscal_dynamic.py` (and its registered `fiscal_dynamic_params.json` and `fiscal_dynamic_amendments.json`), `fiscal_frontier.py`, `cli1_tail.py`, `fiscal_revision.py`, `health_trust_fund.py` (step 10, analysis only); tests `test_fiscal_path.py`, `test_cli1_tail.py`, `test_fiscal_revision.py` |
| Dossier cost tools | `democratic_renewal_cost.py` and `democratic_renewal_pace.py` (democratic renewal's sections 6 and 7) and `test_democratic_renewal.py`, `capacity-funding.py` and its test, `health_financing.py`, `health_cost_review.py` and their tests (not run by the checks; `test_health_cost_review.py` takes about three minutes), `program_inventory.py` |

**The old paths still work.** Each script here, except the three democratic renewal tools (moved without shims so open PR #493's edits to them carry over), has a shim at its old path in `models/tools/` that runs it unchanged, so commands quoted in the dossiers and the scripts that load each other by path keep working. Inside these files `HERE` still names `models/tools/` (where the shared readers and the other models are); each file's own folder is this one.

**Not moved yet:** `family-financing.py`, `health/`, `strategic-review/`, `capacity-review/` and `financing-protection/` (`.github/scripts/run-checks.sh` or several scripts name their paths; they move with step H2b).
