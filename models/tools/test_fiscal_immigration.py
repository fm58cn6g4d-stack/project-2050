"""The immigration booking (dossiers/immigration/6-cost.md part 6; milestone review step 5) matches the dossier.

Role: protects the immigration booking. Run by run-all.sh after the recovery budget (it reads build/ledger.json);
standard library only, plus the dossier's own path script through immigration_booking.py. Checks that:
- every shape, component, perm and ledger amount in models/data/inputs/ equals immigration_booking.py's derivation
  from dossiers/immigration/tools/immigration_path.py, and every line of the path is booked once;
- IMM-1 is now a cost, not the legacy S.744 saving, and its spending and the two revenue rows add to section 6's
  decided set ($149.0B over FY2030-39 and $22.5B in FY2040, part 1, with memo 6's health line at two-thirds of care's
  average use, Espen, November 13; $175.1B and $28.8B at 1.0);
- E-Verify's on-budget revenue is its own base-revenue row, not netted inside IMM-1 (counting rules);
- CAP-7S's USCIS share ($40B) and CAP-7's pro-rata USCIS share are out.
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


IB = load("immigration_booking", HERE / "immigration_booking.py")
fiscal = load("imm_fiscal", HERE / "fiscal-model.py")
rows = lambda name: list(csv.DictReader(open(INPUTS / name, newline="", encoding="utf-8")))  # noqa: E731


class ImmigrationBooking(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.b = IB.booking()
        cls.bills = {r["id"]: r for r in json.load(open(BUILD / "ledger.json"))["bills"]}
        cls.base = fiscal.read_baseline(ROOT / "models/data/fiscal-baseline.csv")

    def path(self, rid):
        return fiscal.row_path(self.base, self.bills[rid]["gf_mid"], fiscal.PR.BILLS[rid], rid)

    def test_inputs_equal_the_derivation(self):
        years = {r["id"]: [float(r["y%d" % y]) for y in W] for r in rows("fiscal-years.csv")}
        for k, v in self.b["years"].items():
            self.assertEqual(years[k], [float(x) for x in v], k)
        comps = {(r["owner"], r["component"]): r for r in rows("fiscal-components.csv")}
        parts = self.b["components"]["IMM-1"]
        self.assertEqual(sorted(n for o, n in comps if o == "IMM-1"), sorted(n for n, _, _ in parts))
        for n, amount, perm in parts:
            r = comps[("IMM-1", n)]
            self.assertEqual(float(r["mid10"]), amount, n)
            self.assertAlmostEqual(float(r["perm"]), perm, places=6, msg=n)
            self.assertEqual(r["grow"], IB.GROW, n)
        bills = {r["id"]: r for r in rows("ledger-bills.csv")}
        for k, (lo, mid, hi) in list(self.b["ledger"].items()) + list(self.b["cap"].items()):
            self.assertEqual(tuple(float(bills[k][c]) for c in ("cost_lo", "cost_mid", "cost_hi")), (lo, mid, hi), k)
        rev = {r["id"]: r for r in rows("ledger-revenue.csv")}
        prof = {r["id"]: r for r in rows("fiscal-profiles.csv") if r["table"] == "base revenue"}
        for k, (lo, mid, hi) in self.b["revenue"].items():
            self.assertEqual(tuple(float(rev[k][c]) for c in ("lo", "mid", "hi")), (lo, mid, hi), k)
            self.assertEqual((rev[k]["channel"], rev[k]["in_base"]), ("General fund", "yes"), k)
            self.assertAlmostEqual(float(prof[k]["perm"]), self.b["revenue_perms"][k], places=6, msg=k)

    def test_totals_are_section_6s(self):
        t = self.b["totals"]
        self.assertEqual(round(t["dossier_window"] * 1000, 1), 149.0)
        self.assertEqual(round(t["dossier_fy2040"], 1), 22.5)
        self.assertAlmostEqual(t["spending_window"] + t["revenue_window"], t["dossier_window"], places=3)
        self.assertGreater(self.b["ledger"]["IMM-1"][1], 0)    # a cost now, not the S.744 saving

    def test_everify_revenue_is_its_own_row(self):
        self.assertNotIn("everify-revenue", [n for n, _, _ in self.b["components"]["IMM-1"]])
        self.assertAlmostEqual(self.b["revenue"]["IMM-EV"][1], 0.0233, places=4)

    def test_model_books_the_rows(self):
        booked = sum(self.path("IMM-1")[y] for y in W)
        self.assertAlmostEqual(booked, 1000 * self.b["ledger"]["IMM-1"][1], places=6)
        p = self.path("IMM-1")
        self.assertAlmostEqual(p[2040], sum(v for k, v in self.b["fy2040"].items() if k.startswith("IMM-1/")), delta=0.5)

    def test_uscis_shares_are_out(self):
        self.assertAlmostEqual(IB.CAP7S[1] - self.b["cap"]["CAP-7S"][1], 0.04, places=9)
        self.assertAlmostEqual(self.b["cap"]["CAP-7"][1], round(0.49 * 0.93, 4), places=9)


if __name__ == "__main__":
    unittest.main(verbosity=1)
