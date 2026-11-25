"""The work booking (dossiers/work/6-cost.md part 9) matches the dossier.

Role: protects the work booking. Run by run-all.sh after the recovery budget (it reads build/ledger.json); standard
library only, plus the dossier's own path script through work_booking.py. Checks that:
- every ledger amount, year shape, perm, revenue row and Social Security series in models/data/inputs/ equals
  work_booking.py's derivation from dossiers/work/tools/work_path.py, and every path line is booked once or named as
  not booked (the gated tranche, the standby trigger, Extended Benefits in a downturn, the UI trust funds' own lines,
  the AmeriCorps match);
- the booked rows add to section 6's firm lines plus the lines Espen decided on November 18 and priced apart (W1, W4):
  about $226.9B over FY2030-39 and $31.9B in FY2040, within the ledger's $1B rounding per row;
- the three revenue effects are base-revenue rows of their own, with the right signs (the UI offset a loss, income
  tax on wage insurance and penalties gains);
- the model books each row's amount, and FY2040 within $0.5B of the dossier's;
- WRK-UI-SS follows its input year by year and rides with the plan's scenarios, not current law.
"""
import csv
import importlib.util
import json
import os
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
HERE = ROOT / "models" / "tools"   # models/tools: this file moved to models/bookings/ in stage H step H4
BUILD = Path(os.environ.get("BUILD", ROOT / "build"))
INPUTS = ROOT / "models" / "data" / "inputs"
W = range(2030, 2040)


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


WB = load("work_booking", HERE / "work_booking.py")
fiscal = load("wrk_fiscal_test", HERE / "fiscal-model.py")
rows = lambda name: list(csv.DictReader(open(INPUTS / name, newline="", encoding="utf-8")))  # noqa: E731
NOT_BOOKED = ["eb_recession", "service_match", "tranche", "trigger", "ui_tax", "ui_tf"]


class WorkBooking(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.b = WB.booking()
        cls.bills = {r["id"]: r for r in json.load(open(BUILD / "ledger.json"))["bills"]}
        cls.base = fiscal.read_baseline(ROOT / "models/data/fiscal-baseline.csv")

    def path(self, rid):
        return fiscal.row_path(self.base, self.bills[rid]["gf_mid"], fiscal.PR.BILLS[rid], rid)

    def test_inputs_equal_the_derivation(self):
        years = {r["id"]: [float(r["y%d" % y]) for y in W] for r in rows("fiscal-years.csv")}
        for k, v in self.b["years"].items():
            self.assertEqual(years[k], [float(x) for x in v], k)
        bills = {r["id"]: r for r in rows("ledger-bills.csv")}
        for k, (lo, mid, hi) in self.b["ledger"].items():
            self.assertEqual(tuple(float(bills[k][c]) for c in ("cost_lo", "cost_mid", "cost_hi")), (lo, mid, hi), k)
        prof = {(r["table"], r["id"]): r for r in rows("fiscal-profiles.csv")}
        rev = {r["id"]: r for r in rows("ledger-revenue.csv")}
        for k, (lo, mid, hi) in self.b["revenue"].items():
            self.assertEqual(tuple(float(rev[k][c]) for c in ("lo", "mid", "hi")), (lo, mid, hi), k)
            self.assertEqual((rev[k]["channel"], rev[k]["in_base"]), ("General fund", "yes"), k)
            self.assertAlmostEqual(float(prof[("base revenue", k)]["perm"]), self.b["perms"][k], places=6, msg=k)
        for k in self.b["ledger"]:
            self.assertAlmostEqual(float(prof[("bill", k)]["perm"]), self.b["perms"][k], places=6, msg=k)
        ss = {int(r["year"]): float(r["wrk_ui_pct_payroll"]) for r in rows("funds-ss-offbudget.csv")}
        self.assertEqual(ss, {y: v for y, v in self.b["ss_pct"].items()})

    def test_every_line_is_booked_or_named(self):
        self.assertEqual(self.b["unbooked"], NOT_BOOKED)

    def test_no_line_is_in_two_rows(self):
        ids = [i for _, ids, *_ in WB.SPENDING for i in ids] + [i for _, ids, *_ in WB.REVENUE for i in ids]
        self.assertEqual(len(ids), len(set(ids)), "a path line is booked in two rows")
        self.assertNotIn(WB.SS_LINE, ids)

    def test_totals_are_section_6s(self):
        t = self.b["totals"]
        self.assertAlmostEqual(t["net_window"] * 1000, 226.9, delta=1.5)   # 222.4 firm + 4.5 decided apart, plus the ledger's $1B rounding
        self.assertAlmostEqual(t["net_fy2040"], 31.94, delta=0.05)         # 31.26 firm + 0.68 decided apart
        self.assertAlmostEqual(t["ss_window"] * 1000, 43.3, delta=0.1)
        self.assertAlmostEqual(t["ss_fy2040"], 5.96, delta=0.01)

    def test_revenue_signs(self):
        r = self.b["revenue"]
        self.assertLess(r["LAB-11T"][1], 0)        # the offset is lost revenue
        self.assertGreater(r["LAB-18T"][1], 0)     # income tax on wage insurance is a gain
        self.assertGreater(r["LAB-2P"][1], 0)      # penalties are a gain
        for k, (lo, mid, hi) in r.items():
            self.assertLessEqual(lo, mid, k)
            self.assertLessEqual(mid, hi, k)

    def test_credit_and_tranche(self):
        self.assertAlmostEqual(self.b["ledger"]["LAB-5"][1], 0.002, places=3)     # about $2.1B (DEC-2026-11-18-22)
        self.assertNotIn("LAB-9.03", self.b["ledger"])                           # the gated tranche is not booked
        self.assertAlmostEqual(self.b["fy2040"]["LAB-5"], 0.0, places=6)        # the credit ends after 2032

    def test_model_books_the_rows(self):
        for rid, (lo, mid, hi) in self.b["ledger"].items():
            p = self.path(rid)
            self.assertAlmostEqual(sum(p[y] for y in W), 1000 * mid, places=6, msg=rid)
            self.assertAlmostEqual(p[2040], self.b["fy2040"][rid], delta=0.5, msg=rid)

    def test_wrk_ui_ss_rides_with_the_plan(self):
        sys.path.insert(0, str(HERE))
        from test_funds_model import load_funds      # the funds model runs at import, in a scratch copy of build/
        F = load_funds()
        p = F.SSP["WRK-UI-SS"]
        self.assertEqual((p["kind"], p["start"]), ("direct", 2031))
        f = F.SSF["WRK-UI-SS"]
        self.assertEqual(f(2030), (0.0, 0.0))
        for t in range(2031, 2041):
            self.assertEqual(f(t), (-self.b["ss_pct"][t], 0.0), t)
        self.assertEqual(f(2100), (-self.b["ss_pct"][2040], 0.0))
        self.assertNotIn("WRK-UI-SS", F.SS_SCEN["Current law"])
        self.assertIn("WRK-UI-SS", F.SS_SCEN["D8 baseline"])
        self.assertIn("WRK-UI-SS", F.SS_SCEN["D8 + SS-5"])

    def test_plain_printout_runs(self):
        out = subprocess.run([sys.executable, str(HERE / "work_booking.py")], capture_output=True, text=True)
        self.assertEqual(out.returncode, 0, out.stderr)
        self.assertIn("totals", out.stdout)


if __name__ == "__main__":
    unittest.main(verbosity=1)
