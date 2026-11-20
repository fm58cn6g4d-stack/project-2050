"""The democratic renewal booking (dossiers/foundations/democratic-renewal/6-cost.md part 9) matches the dossier.

Role: protects the democratic renewal booking. Run by run-all.sh after the recovery budget (it reads build/ledger.json
and build/recovery-budget-audit.csv); standard library only, plus the dossier's two tools through
democratic_renewal_booking.py. Checks that:
- every ledger amount, year shape, perm and revenue row in models/data/inputs/ equals the booking tool's derivation;
- the four new rows are the lines section 6 names (the library line, legal aid, and D4 option B's two timing rows),
  and the lines section 6 leaves out of the booking (the court's structure, inside CRT-P1's room; statute tracking,
  inside CAP-8) are named, not booked twice;
- D4's timing rows net to section 7's figures (outlays about $16.6B lower, the IRS yield about $16.1B lower over
  FY2030-39) and are zero in FY2040, so they move no permanent cost;
- no adopted row's amount moved: CAP-7 and CAP-7S still book $279.2B and $98.0B in the model, and memo 10's
  contingency is inside them, not added;
- the model books each new row's amount, with the right signs, and the rows are not subject to the capacity rows'
  October 26 scaling.
"""
import csv
import importlib.util
import json
import os
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
BUILD = Path(os.environ.get("BUILD", ROOT / "build"))
INPUTS = ROOT / "models" / "data" / "inputs"
W = range(2030, 2040)


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


DB = load("democratic_renewal_booking", HERE / "democratic_renewal_booking.py")
fiscal = load("drb_fiscal_test", HERE / "fiscal-model.py")
rows = lambda name: list(csv.DictReader(open(INPUTS / name, newline="", encoding="utf-8")))  # noqa: E731
NOT_BOOKED = ["CAP-6.01, statute tracking", "CRT-5.09, the immigration court's structure"]
NEW = ["DEM-17.02", "CRT-20.01", "CAP-7P", "G8P"]


def audit_sum(line, years=W):
    out = 0.0
    for r in csv.DictReader(open(BUILD / "recovery-budget-audit.csv", newline="", encoding="utf-8")):
        if r["case"] == "mixed" and r["line"] == line and int(r["year"]) in years:
            out += float(r["primary_deficit_change_bn"])
    return out


class DemocraticRenewalBooking(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.b = DB.booking()
        cls.bills = {r["id"]: r for r in json.load(open(BUILD / "ledger.json"))["bills"]}
        cls.base = fiscal.read_baseline(ROOT / "models/data/fiscal-baseline.csv")

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

    def test_the_new_rows_and_the_lines_left_out(self):
        self.assertEqual(sorted(list(self.b["ledger"]) + list(self.b["revenue"])), sorted(NEW))
        self.assertEqual(self.b["unbooked"], NOT_BOOKED)
        ids = [i for i, *_ in DB.SPENDING] + [i for i, *_ in DB.REVENUE]
        self.assertEqual(len(ids), len(set(ids)), "a line is booked in two rows")

    def test_the_two_new_lines_are_section_6s(self):
        t = self.b["totals"]
        self.assertAlmostEqual(t["lines"]["DEM-17.02"], 7.8, delta=0.05)
        self.assertAlmostEqual(t["lines"]["CRT-20.01"], 4.6, delta=0.05)
        self.assertAlmostEqual(self.b["fy2040"]["DEM-17.02"], 0.91, delta=0.01)
        self.assertAlmostEqual(self.b["fy2040"]["CRT-20.01"], 0.66, delta=0.01)
        lo, mid, hi = self.b["ledger"]["DEM-17.02"]
        self.assertAlmostEqual(lo * 1000, 5.2, delta=0.25)           # the ledger rounds to $1B
        self.assertAlmostEqual(hi * 1000, 10.0, delta=0.6)            # 10.5 in section 6; the ledger rounds to $1B

    def test_d4_option_b_nets_to_section_7(self):
        t = self.b["totals"]
        self.assertAlmostEqual(t["lines"]["CAP-7P"], -16.6, delta=0.05)                # outlays lower (unrounded path)
        self.assertAlmostEqual(t["lines"]["G8P"], 16.1, delta=0.05)                    # revenue lower
        self.assertAlmostEqual(t["pace_outlay_window"] * 1000, -17.0, delta=0.05)      # the ledger's $1B rounding
        self.assertAlmostEqual(t["pace_g8_window"] * 1000, 16.1, delta=0.05)
        self.assertEqual(self.b["fy2040"]["CAP-7P"] + 0.0, 0.0)                         # no change in FY2040
        self.assertEqual(self.b["fy2040"]["G8P"] + 0.0, 0.0)
        self.assertAlmostEqual(self.b["perms"]["CAP-7P"], 0.0)
        self.assertAlmostEqual(self.b["perms"]["G8P"], 0.0)
        # outlays: never more than booked in any year; the revenue lag is a loss through FY2034 and about zero after
        self.assertTrue(all(v <= 0 for v in self.b["years"]["CAP-7P"]))
        self.assertTrue(all(v >= 0 for v in self.b["years"]["G8P"][:5]))
        self.assertAlmostEqual(sum(self.b["years"]["G8P"][5:]), -0.32, delta=0.05)     # paced yield catches up: a small gain
        # ranges are section 7's (outlays 7.0 to 36.0; revenue 7.7 to 28.9)
        lo, mid, hi = self.b["ledger"]["CAP-7P"]
        self.assertAlmostEqual(lo * 1000, -36.0, delta=0.6)
        self.assertAlmostEqual(hi * 1000, -7.0, delta=0.6)
        lo, mid, hi = self.b["revenue"]["G8P"]
        self.assertAlmostEqual(-hi * 1000, 7.7, delta=0.1)
        self.assertAlmostEqual(-lo * 1000, 28.9, delta=0.1)

    def test_totals_are_section_6s(self):
        t = self.b["totals"]
        # firm lines +12.5 (7.84 + 4.62) and D4's two timing rows -0.4 (-16.56 + 16.12): +12.0 over FY2030-39 on the
        # tool's paths, +12.1 on the ledger's $1B rounding (8 + 5 - 17 + 16.1)
        self.assertAlmostEqual(sum(t["lines"].values()), 12.0, delta=0.05)
        self.assertAlmostEqual(t["net_window"] * 1000, 12.1, delta=0.05)
        self.assertAlmostEqual(t["net_fy2040"], 1.58, delta=0.02)                       # 0.91 + 0.66, nothing from D4

    def test_the_booked_capacity_rows_are_unchanged(self):
        booked, _ = DB.DRC.booked()                      # the audit lines at the October 26 scaling
        self.assertAlmostEqual(sum(booked["CAP-7S"][y] for y in W), 98.0, delta=0.05)
        self.assertAlmostEqual(sum(booked["CAP-7"][y] for y in W), 279.2, delta=0.05)
        self.assertAlmostEqual(booked["CAP-7"][2040], 37.2, delta=0.05)
        bills = {r["id"]: r for r in rows("ledger-bills.csv")}
        self.assertAlmostEqual(float(bills["CAP-7"]["cost_mid"]), 0.4557, places=4)
        self.assertAlmostEqual(float(bills["CRT-P1"]["cost_mid"]), 0.01, places=4)      # CRT-5.09 fits inside; no amount moves
        self.assertAlmostEqual(float(bills["CAP-8"]["cost_mid"]), 0.04, places=4)
        for k in ("CAP-7", "CAP-7S"):
            self.assertIn("contingency", bills[k]["note"], k)
        self.assertIn("CRT-5.09", bills["CRT-P1"]["bill"])
        self.assertIn("CAP-6.01", bills["CAP-8"]["note"])

    def test_model_books_the_rows(self):
        for rid, (lo, mid, hi) in self.b["ledger"].items():
            p = fiscal.row_path(self.base, self.bills[rid]["gf_mid"], fiscal.PR.BILLS[rid], rid)
            self.assertAlmostEqual(sum(p[y] for y in W), 1000 * mid, places=6, msg=rid)
            self.assertAlmostEqual(p[2040], self.b["fy2040"][rid], delta=0.05, msg=rid)
            self.assertAlmostEqual(audit_sum(rid), 1000 * mid, places=2, msg=rid)
        for rid, (lo, mid, hi) in self.b["revenue"].items():
            self.assertAlmostEqual(audit_sum(rid), -1000 * mid, places=2, msg=rid)       # a lost gain is a cost

    def test_the_capacity_rows_still_scale_to_october_26(self):
        # CAP-7P is not one of the rows the model's "Smaller capacity and AI authorizations" line scales: its audit
        # amount is its own, and CAP-7 and CAP-7S keep the figures section 6 publishes.
        self.assertAlmostEqual(audit_sum("CAP-7P"), 1000 * self.b["ledger"]["CAP-7P"][1], places=2)

    def test_plain_printout_runs(self):
        import subprocess
        import sys
        out = subprocess.run([sys.executable, str(HERE / "democratic_renewal_booking.py")], capture_output=True, text=True)
        self.assertEqual(out.returncode, 0, out.stderr)
        self.assertIn("totals", out.stdout)


if __name__ == "__main__":
    unittest.main(verbosity=1)
