"""The clean power booking (dossiers/clean-power/6-cost.md part 6; review-m4.md) matches the dossier.

Role: protects clean power's booking. Run by run-all.sh after the recovery budget (it reads build/fiscal-model.json);
standard library only, plus the dossier's own path script through clean_power_booking.py. Checks that:
- every shape, perm, after-window amount and ledger amount in models/data/inputs/ equals clean_power_booking.py's
  derivation from dossiers/clean-power/tools/clean_power_path.py and the energy model's results.json;
- the model's paths for the booked rows move the general fund by section 6's change against the booking
  (+$43.0B over FY2030-39 and -$51.6B in FY2040, part 1), plus the offset on the standard's payments, the one
  line section 6 left to the booking (about $38B and $10B);
- memo 1 B's REV-C1 is about $1.20T, CLI-2 stays 80% of it, and the dividend and the fee stay off the general fund;
- the standard's payments are received and paid out in equal amounts (C3A, CLI-3A), so their net is the offset (CXA);
- the transition share is general-fund revenue only from FY2040 (C1T, DEC-2026-11-13-13).
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


CB = load("clean_power_booking", HERE / "clean_power_booking.py")
rows = lambda name: list(csv.DictReader(open(INPUTS / name, newline="", encoding="utf-8")))  # noqa: E731
CHANGED = ("CX", "CLI-5")                                   # booked rows the booking reshapes
NEW = ("CLI-10", "CLI-5H", "CLI-11", "CLI-3A", "C1T", "C3A", "CXA")


class CleanPowerBooking(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.b = CB.booking()
        cls.model = {r["id"]: r for r in json.load(open(BUILD / "fiscal-model.json"))["rows"]}
        before = {}
        with open(ROOT / "dossiers" / "clean-power" / "tools" / "booked-before.csv") as f:
            for r in csv.DictReader(f):
                before[r["line"]] = {y: float(r["y%d" % y]) for y in range(2030, 2041)}
        cls.before = before

    def gf(self, rid, y):
        return float(self.model[rid]["gf"][str(y)])

    def test_inputs_equal_the_derivation(self):
        years = {r["id"]: [float(r["y%d" % y]) for y in W] for r in rows("fiscal-years.csv")}
        for k, v in self.b["years"].items():
            self.assertEqual(years[k], [float(x) for x in v], k)
        after = {r["id"]: r for r in rows("fiscal-after.csv")}
        for k, v in self.b["after"].items():
            self.assertEqual(float(after[k]["y2040"]), v[2040], k)
        prof = {(r["table"], r["id"]): r for r in rows("fiscal-profiles.csv")}
        for k, perm in self.b["perms"].items():
            t = "base revenue" if k in ("CX", "C3A", "CXA", "C1T") else "bill"
            self.assertAlmostEqual(float(prof[(t, k)]["perm"] or 1.0), perm, places=6, msg=k)
        bills = {r["id"]: r for r in rows("ledger-bills.csv")}
        for k, v in self.b["ledger"].items():
            self.assertEqual(tuple(float(bills[k][c]) for c in ("cost_lo", "cost_mid", "cost_hi")), v, k)
            self.assertEqual(bills[k]["channel"], "Carbon fee" if k == "CLI-2" else "General fund", k)
        rev = {r["id"]: r for r in rows("ledger-revenue.csv")}
        for k, v in self.b["revenue"].items():
            self.assertEqual(tuple(float(rev[k][c]) for c in ("lo", "mid", "hi")), v, k)
        for k in ("CX", "C1T", "C3A", "CXA"):
            self.assertEqual((rev[k]["channel"], rev[k]["in_base"]), ("General fund", "yes"), k)
        self.assertEqual((rev["C1"]["channel"], rev["C1"]["in_base"]), ("Carbon fee", "no"))
        adoption = json.load(open(INPUTS / "climate-adoption.json"))
        self.assertEqual(adoption["legacy_gf_tn"]["CLI-5"], self.b["legacy_gf_cli5"])

    def test_memo_1_b(self):
        c1 = self.b["revenue"]["C1"][1]
        self.assertAlmostEqual(c1, 1.2027, places=4)
        self.assertAlmostEqual(self.b["ledger"]["CLI-2"][1] - 0.8 * c1, 1.5311296000407166 - 0.8 * 1.9, places=4)
        self.assertEqual(self.b["revenue"]["CX"][1], round(-0.244 * (c1 + 0.03 + 0.022), 3))

    def test_the_payments_net_to_their_offset(self):
        self.assertEqual(self.b["years"]["C3A"], self.b["years"]["CLI-3A"])
        self.assertEqual(self.b["revenue"]["C3A"], self.b["ledger"]["CLI-3A"])
        for y in list(W) + [2040]:
            self.assertAlmostEqual(self.gf("C3A", y) + self.gf("CLI-3A", y), 0.0, places=6, msg=y)
            self.assertAlmostEqual(self.gf("CXA", y), 0.244 * self.gf("CLI-3A", y), delta=0.05, msg=y)

    def test_transition_share_from_fy2040_only(self):
        self.assertEqual([self.gf("C1T", y) for y in W], [0.0] * 10)
        self.assertAlmostEqual(self.gf("C1T", 2040), -33.1, places=6)
        self.assertEqual([self.gf("CLI-5H", y) for y in W], [0.0] * 10)
        self.assertAlmostEqual(self.gf("CLI-5H", 2040), 9.9, places=6)

    def test_model_moves_the_general_fund_by_section_6s_change(self):
        t = self.b["totals"]
        change = {}
        for y in list(W) + [2040]:
            change[y] = (sum(self.gf(k, y) - self.before[k][y] for k in CHANGED) +
                         sum(self.gf(k, y) for k in NEW))
        window = sum(change[y] for y in W)
        self.assertEqual(round(t["change_window"] * 1000, 1), 43.0)
        self.assertEqual(round(t["change_fy2040"], 1), -51.6)
        self.assertAlmostEqual(window, 1000 * t["change_window"] + 1000 * t["acp_offset_window"], delta=0.5)
        self.assertAlmostEqual(change[2040], t["change_fy2040"] + t["acp_offset_fy2040"], delta=0.5)


if __name__ == "__main__":
    unittest.main()
