"""The health plan's booking (care milestone review F-4; dossiers/care/6-cost.md part 5) matches the dossier's path.

Role: protects care fix step 5. Run by run-all.sh after the fiscal model (it reads build/ledger.json); standard library
only, plus the dossier's own path script through health_booking.py. Checks that:
- every health shape, component and ledger amount in models/data/inputs/ equals health_booking.py's derivation from
  dossiers/care/tools/health_path.py, so a change to the dossier's path fails here instead of drifting;
- the fiscal model books the spending line at the path's FY2040 figure and the exclusion revenue (HX) at its own;
- the plan's net cost on the model's basis (HLT-1 plus HLT-7's spending line, less HX) is the dossier's $21.74T;
- the employer contribution is not booked on any channel, and HX is general-fund base revenue;
- HLT-3 and HLT-5 are retired, HLT-1, HLT-2 and HLT-6 end with the 2035 endpoint, and HLT-4's retired parts end
  with their waves while its long-term care and safety-net parts continue;
- the household test's health rows (incidence-rows.csv H7h, H7w, H7x, with PB, H2 and H5p; their keys and phase-in
  shapes) equal health_booking.py's incidence() derivation (care follow-up 2).
"""
import csv
import importlib.util
import json
import os
import sys
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
BUILD = Path(os.environ.get("BUILD", ROOT / "build"))
INPUTS = ROOT / "models" / "data" / "inputs"
sys.path.insert(0, str(HERE))


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


HB = load("health_booking", HERE / "health_booking.py")
fiscal = load("health_fiscal", HERE / "fiscal-model.py")
rows = lambda name: list(csv.DictReader(open(INPUTS / name, newline="", encoding="utf-8")))  # noqa: E731
W = range(2030, 2040)


class HealthBooking(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.b = HB.booking()
        cls.ledger = json.load(open(BUILD / "ledger.json"))
        cls.bills = {r["id"]: r for r in cls.ledger["bills"]}
        cls.rev = {r["id"]: r for r in cls.ledger["revenue"]}
        cls.base = fiscal.read_baseline(ROOT / "models/data/fiscal-baseline.csv")

    def path(self, rid):
        return fiscal.row_path(self.base, self.bills[rid]["gf_mid"], fiscal.PR.BILLS[rid], rid)

    def part(self, owner, name):
        amount, p = next((a, p) for n, a, p in fiscal.PR.COMPONENTS[owner] if n == name)
        return fiscal.row_path(self.base, amount, p, p.get("years"))

    def test_inputs_equal_the_derivation(self):
        years = {r["id"]: [float(r["y%d" % y]) for y in W] for r in rows("fiscal-years.csv")}
        for k, v in self.b["years"].items():
            self.assertEqual(years[k], [float(x) for x in v], k)
        comps = {(r["owner"], r["component"]): r for r in rows("fiscal-components.csv")}
        for owner, parts in self.b["components"].items():
            self.assertEqual(sorted(n for o, n in comps if o == owner), sorted(n for n, _, _ in parts), owner)
            for n, amount, perm in parts:
                r = comps[(owner, n)]
                self.assertEqual(float(r["mid10"]), amount, n)
                if perm:
                    self.assertAlmostEqual(float(r["perm"]), perm, places=6, msg=n)
        bills = {r["id"]: r for r in rows("ledger-bills.csv")}
        rev = {r["id"]: r for r in rows("ledger-revenue.csv")}
        for k, (lo, mid, hi) in self.b["ledger"].items():
            r, cols = (rev[k], ("lo", "mid", "hi")) if k == "HX" else (bills[k], ("cost_lo", "cost_mid", "cost_hi"))
            self.assertEqual(tuple(float(r[c]) for c in cols), (lo, mid, hi), k)
        hx = next(r for r in rows("fiscal-profiles.csv") if r["id"] == "HX")
        self.assertAlmostEqual(float(hx["perm"]), self.b["perms"]["HX"], places=6)

    def test_fy2040_lines_are_the_paths(self):
        spend = self.part("HLT-7", "plan-spending")
        self.assertAlmostEqual(spend[2040], self.b["fy2040"]["spending"], delta=0.5)
        self.assertAlmostEqual(self.part("HLT-7", "territories")[2040], HB.TERRITORIES_FY2040, delta=0.5)
        self.assertEqual(self.part("HLT-7", "transition-fund")[2040], 0)
        hx = fiscal.row_path(self.base, -self.rev["HX"]["mid"], fiscal.PR.REVENUE["HX"], "HX")
        self.assertAlmostEqual(-hx[2040], self.b["fy2040"]["exclusion"], delta=0.5)
        self.assertTrue(all(hx[y] < 0 for y in range(2031, 2057)))     # a revenue gain, every year from wave 1
        # FY2041 and FY2042 keep growing with premiums (CBO's Medicare category)
        self.assertGreater(spend[2042], spend[2041])
        self.assertGreater(spend[2041], spend[2040])

    def test_net_cost_is_the_dossiers(self):
        t = lambda p: sum(p[y] for y in W) / 1000  # noqa: E731
        hx = fiscal.row_path(self.base, -self.rev["HX"]["mid"], fiscal.PR.REVENUE["HX"], "HX")
        net = t(self.path("HLT-1")) + t(self.part("HLT-7", "plan-spending")) + t(hx)
        self.assertAlmostEqual(net, self.b["totals"]["net_window"], delta=0.002)
        self.assertAlmostEqual(round(net, 2), 21.74)
        self.assertAlmostEqual(round(self.b["totals"]["with_contribution"], 2), 16.43)

    def test_contribution_is_not_booked(self):
        # the only revenue row from the health plan is HX: no employer contribution (HLT-7.18) and no FEHB money
        health = [r for r in self.ledger["revenue"] if "HLT-7" in r["option"] or "care" in r.get("source", "")]
        self.assertEqual([r["id"] for r in health], ["HX"])
        self.assertEqual((self.rev["HX"]["channel"], self.rev["HX"]["in_base"]), ("General fund", "Yes"))
        self.assertEqual(self.bills["HLT-7"]["own_revenue"], 0)

    def test_retired_and_ended_rows(self):
        for rid in ("HLT-3", "HLT-5"):
            self.assertTrue(all(v == 0 for v in self.path(rid).values()), rid)
        for rid in ("HLT-1", "HLT-2", "HLT-6"):
            p = self.path(rid)
            self.assertTrue(all(p[y] == 0 for y in range(2036, 2057)), rid)
        kids, dental = self.part("HLT-4", "children-continuous-coverage"), self.part("HLT-4", "medicaid-dental-and-bundle")
        self.assertTrue(all(kids[y] == 0 for y in range(2032, 2057)))
        self.assertTrue(all(dental[y] == 0 for y in range(2036, 2057)))
        ltc = self.part("HLT-4", "ltc-hcbs-care-workforce")
        self.assertGreater(ltc[2040], ltc[2039])
        total = self.path("HLT-4")
        self.assertAlmostEqual(sum(total[y] for y in W) / 1000, self.bills["HLT-4"]["gf_mid"], places=9)


class HealthIncidence(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.inc = HB.incidence()
        cls.rows = {r["id"]: r for r in rows("incidence-rows.csv")}
        cls.keys = {r["key"]: r for r in rows("incidence-keys.csv")}
        cls.phase = {r["id"]: r for r in rows("incidence-phase-in.csv")}

    def test_rows_equal_the_derivation(self):
        for rid in ("H7h", "H7w"):
            self.assertEqual(float(self.rows[rid]["amount"]), self.inc["rows"][rid], rid)
        self.assertEqual(self.rows["H7x"]["amount"], "[HX]")
        self.assertEqual((self.rows["H7x"]["side"], self.rows["H7h"]["side"], self.rows["H7w"]["side"]),
                         ("cost", "benefit", "benefit"))
        self.assertEqual(self.rows["H5p"]["amount"], "0")
        self.assertEqual((self.rows["PB"]["amount"], self.rows["H2"]["amount"]), ("0.28*[HLT-2]", "1.28*[HLT-2]"))

    def test_keys_and_shapes_equal_the_derivation(self):
        for key, (q, t1) in self.inc["key"].items():
            k = self.keys[key]
            self.assertEqual([float(k[c]) for c in ("q1", "q2", "q3", "q4", "q5")], q, key)
            self.assertEqual(float(k["top1"]), t1, key)
            self.assertAlmostEqual(sum(q), 100, places=6)
        for rid, v in self.inc["shapes"].items():
            r = self.phase[rid]
            self.assertEqual(r["method"], "norm", rid)
            self.assertEqual([float(r["y%d" % y]) for y in W], v, rid)
        self.assertEqual((self.phase["PB"]["same_as"], self.phase["H7x"]["same_as"]), ("H2", "H7w"))

    def test_exclusion_caps_end_with_the_exclusion(self):
        """C19b and C19 cap a base HX ends: their inputs equal health_booking.c19b() and they collect nothing once
        the last employer cohort has moved (care follow-up 2)."""
        cuts = {r["id"]: r for r in rows("ledger-cuts.csv")}
        years = {r["id"]: [float(r["y%d" % y]) for y in W] for r in rows("fiscal-years.csv")}
        for rid, before in (("C19b", HB.C19B_BEFORE_PLAN_TN), ("C19", HB.C19_BEFORE_PLAN_TN)):
            d = HB.c19b(before)
            self.assertEqual(float(cuts[rid]["saves_tn"]), d["mid"], rid)
            self.assertEqual(years[rid], [float(x) for x in d["years"]], rid)
            self.assertTrue(all(v == 0 for v in d["years"][6:]), rid)   # FY2036-39
        self.assertEqual(self.phase["C19b"]["method"], "norm")
        self.assertEqual(self.phase["C19"]["same_as"], "C19b")

    def test_household_total_is_the_dossiers(self):
        self.assertAlmostEqual(self.inc["full_scale"]["household_removed"], 1527.5, delta=1.0)  # 6-cost.md part 8


if __name__ == "__main__":
    unittest.main()
