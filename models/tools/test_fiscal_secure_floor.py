"""The secure floor's booking (dossiers/secure-floor/6-cost.md part 6; milestone review step 7) matches the dossier.

Role: protects the secure floor booking. Run by run-all.sh after the recovery budget (it reads build/ledger.json and
build/recovery-budget.json); standard library only, plus the dossier's own path script through
secure_floor_booking.py. Checks that:
- every shape, component, perm and ledger amount in models/data/inputs/ equals secure_floor_booking.py's derivation
  from dossiers/secure-floor/tools/secure_floor_path.py, so a change to the dossier's path fails here instead of
  drifting, and every line of the path is booked once;
- FAM-1's benefit is the decided $1.85T (the American Family Act without the $2,200 floor) and the booked rows add to
  part 1's $2,626B over FY2030-39 and $303B in FY2040, plus part 2's two lines left to the booking (B-1, M-1);
- INC-2B books INC-2.02, SNAP's earned income deduction at 45% (Espen's option D, DEC-2026-11-13-03): about $12B in
  FY2030 and $138B over FY2030-39 on rail R1, its range $8-16B a year;
- INC-3 carries INC-3.03, SSI in the four territories (about $20B over FY2030-39);
- the leave fund steps 0.10 points (DEC-2026-11-12-14) and, at high take-up, never borrows from Treasury;
- Social Security's central case carries SS-7.01's one point on its expected path, not the two-point broad rate,
  with SS-8 recorded at zero (DEC-2026-11-12-13).
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


SFB = load("secure_floor_booking", HERE / "secure_floor_booking.py")
fiscal = load("sf_fiscal", HERE / "fiscal-model.py")
rows = lambda name: list(csv.DictReader(open(INPUTS / name, newline="", encoding="utf-8")))  # noqa: E731


class SecureFloorBooking(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.b = SFB.booking()
        cls.bills = {r["id"]: r for r in json.load(open(BUILD / "ledger.json"))["bills"]}
        cls.base = fiscal.read_baseline(ROOT / "models/data/fiscal-baseline.csv")
        cls.rb = json.load(open(BUILD / "recovery-budget.json"))
        cls.assumptions = json.load(open(HERE / "recovery-budget" / "assumptions.json"))

    def path(self, rid):
        return fiscal.row_path(self.base, self.bills[rid]["gf_mid"], fiscal.PR.BILLS[rid], rid)

    def test_inputs_equal_the_derivation(self):
        years = {r["id"]: [float(r["y%d" % y]) for y in W] for r in rows("fiscal-years.csv")}
        for k, v in self.b["years"].items():
            self.assertEqual(years[k], [float(x) for x in v], k)
        comps = {(r["owner"], r["component"]): r for r in rows("fiscal-components.csv")}
        parts = self.b["components"]["FAM-1"]
        self.assertEqual(sorted(n for o, n in comps if o == "FAM-1"), sorted(n for n, _, _ in parts))
        for n, amount, perm in parts:
            r = comps[("FAM-1", n)]
            self.assertEqual(float(r["mid10"]), amount, n)
            self.assertAlmostEqual(float(r["perm"]), 1.0 if perm is None else perm, places=6, msg=n)
        prof = {r["id"]: r for r in rows("fiscal-profiles.csv") if r["table"] == "bill"}
        for rid, perm in self.b["perms"].items():
            self.assertAlmostEqual(float(prof[rid]["perm"]), perm, places=6, msg=rid)
            self.assertEqual(prof[rid]["grow"], SFB.GROW, rid)
        bills = {r["id"]: r for r in rows("ledger-bills.csv")}
        for k, (lo, mid, hi) in self.b["ledger"].items():
            self.assertEqual(tuple(float(bills[k][c]) for c in ("cost_lo", "cost_mid", "cost_hi")), (lo, mid, hi), k)
            self.assertEqual((bills[k]["rail"], bills[k]["channel"]), ("R1", "General fund"), k)

    def test_the_benefit_is_the_decided_path(self):
        parts = {n: a for n, a, _ in self.b["components"]["FAM-1"]}
        self.assertEqual(parts["benefit"], 1.85)
        self.assertAlmostEqual(sum(parts.values()), self.b["ledger"]["FAM-1"][1], places=9)
        lo, _, hi = self.b["ledger"]["FAM-1"]
        self.assertTrue(SFB.BENEFIT_TN[0] < lo < parts["benefit"] < SFB.BENEFIT_TN[2] < hi)   # the range sits on 1.65-2.05

    def test_totals_are_section_6s(self):
        t = self.b["totals"]
        self.assertEqual(round(t["dossier_window"] * 1000), 2626)
        self.assertEqual(round(t["dossier_fy2040"]), 303)
        self.assertEqual(round(t["before_window"] * 1000), 2000)
        # The booking: part 1 less the benefit's rounding to $1.85T, plus B-1 and M-1
        self.assertAlmostEqual(t["booked_window"], t["dossier_window"] + t["b1_m1_window"] - (1.9 - 0.0477 - 1.85), places=2)

    def test_model_books_the_rows(self):
        booked = sum(sum(self.path(r)[y] for y in W) for r in ("FAM-1", "INC-1", "INC-2", "INC-2B", "INC-3", "INC-4", "INC-5"))
        self.assertAlmostEqual(booked, 1000 * sum(self.b["ledger"][k][1] for k in self.b["ledger"]), places=6)
        adoption = json.load(open(INPUTS / "recovery-adoption.json"))
        self.assertEqual(adoption["spending"]["participation_tn"], 0.1)   # LAB-10's envelope, unchanged
        for rid, v in self.b["fy2040"].items():
            if "/" not in rid:
                self.assertAlmostEqual(self.path(rid)[2040], v, delta=0.05 * v, msg=rid)

    def test_inc2b_is_option_d(self):
        self.assertEqual(self.b["years"]["INC-2B"][0], 12.0)
        self.assertEqual(self.b["ledger"]["INC-2B"], (0.092, 0.138, 0.183))
        self.assertAlmostEqual(self.b["fy2040"]["INC-2B"], 16.1, delta=0.1)
        self.assertEqual(self.bills["INC-2B"]["rail"], "R1")

    def test_inc3_carries_the_territories(self):
        ssi_t = SFB.path_module().lines()["INC-3.03, SSI in the territories (Espen, November 12)"]
        self.assertAlmostEqual(sum(ssi_t[y] for y in W), 19.7, delta=0.1)
        self.assertEqual(self.b["ledger"]["INC-3"][1], 0.043)

    def test_the_leave_fund_steps_ten_and_never_borrows(self):
        p = {r["key"]: r["value"] for r in rows("funds-parameters.csv")}
        self.assertEqual(float(p["leave_step"]), SFB.LEAVE_STEP)
        self.assertEqual(float(p["leave_cap"]), 1.1)
        lv = self.rb["cases"]["mixed"]["leave"]
        self.assertEqual(max(r["loan"] for r in lv["rows"]), 0.0)
        self.assertIsNone(lv["repayment_year"])
        rate = {r["year"]: r["rate"] for r in lv["rows"]}
        self.assertEqual(min(y for y in rate if rate[y] >= 1.1 - 1e-9), 2036)

    def test_social_security_is_the_decided_package(self):
        ss = self.assumptions["social_security"]
        self.assertNotIn("broad_rate_points", ss)
        for k, v in SFB.SS7.items():
            self.assertEqual(ss[k], v, k)
        self.assertEqual(ss["reserve_investment_booked_payroll_points"], SFB.SS8_BOOKED_PAYROLL_POINTS)
        self.assertIn("flagged", ss["basis"])


if __name__ == "__main__":
    unittest.main(verbosity=1)
