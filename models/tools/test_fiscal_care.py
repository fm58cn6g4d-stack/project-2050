"""Care parts B-D's booking (dossiers/care/6bcd-cost.md part 5; milestone review F-3) matches the dossier's path.

Role: protects the care booking. Run by run-all.sh after the fiscal model (it reads build/ledger.json); standard
library only, plus the dossier's own path script through care_booking.py. Checks that:
- every care shape, component, perm and ledger amount in models/data/inputs/ equals care_booking.py's derivation from
  dossiers/care/tools/care_bcd_path.py, so a change to the dossier's path fails here instead of drifting;
- every line of the path is booked once, and the booked rows add to section 6's figures: $3,665B over FY2030-39 and
  $751B in FY2040 all-in ($3,537B and $729B for the decided pieces);
- HLT-4's legacy long-term care component (0.3194) is gone and the bridge carries the down payment, so nothing is
  counted twice; health's parts of HLT-4 keep their amounts;
- the states' long-term care payment is a negative (offsetting receipt) component labeled with the joint risk;
- the EDU-9B fund's care component is FAM-2's booked path, so part C is counted in one place;
- the household test's F2, H4 and H9 rows, the ltc_universal key and DY6 equal the derivation.
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


CB = load("care_booking", HERE / "care_booking.py")
fiscal = load("care_fiscal", HERE / "fiscal-model.py")
rows = lambda name: list(csv.DictReader(open(INPUTS / name, newline="", encoding="utf-8")))  # noqa: E731
W = range(2030, 2040)
OWNERS = ("HLT-4", "HLT-9", "HLT-10", "HLT-11", "FAM-2")


class CareBooking(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.b = CB.booking()
        cls.ledger = json.load(open(BUILD / "ledger.json"))
        cls.bills = {r["id"]: r for r in cls.ledger["bills"]}
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
            self.assertEqual(sorted(n for o, n in comps if o == owner), sorted(n for n, _, _, _ in parts), owner)
            for n, amount, perm, _ in parts:
                r = comps[(owner, n)]
                self.assertEqual(float(r["mid10"]), amount, n)
                if perm is not None:
                    self.assertAlmostEqual(float(r["perm"]), perm, places=6, msg=n)
        prof = {r["id"]: r for r in rows("fiscal-profiles.csv") if r["table"] == "bill"}
        for rid, perm in self.b["perms"].items():
            self.assertAlmostEqual(float(prof[rid]["perm"]), perm, places=6, msg=rid)
        bills = {r["id"]: r for r in rows("ledger-bills.csv")}
        for k, (lo, mid, hi) in self.b["ledger"].items():
            self.assertEqual(tuple(float(bills[k][c]) for c in ("cost_lo", "cost_mid", "cost_hi")), (lo, mid, hi), k)

    def test_totals_are_section_6s(self):
        t = self.b["totals"]
        self.assertEqual(round(t["decided_window"] * 1000), 3537)
        self.assertEqual(round(t["decided_fy2040"]), 729)
        self.assertEqual(round(t["allin_window"] * 1000), 3662)   # 3,665 less the status rule (DEC-2026-11-13-01)
        self.assertEqual(round(t["allin_fy2040"]), 750)
        self.assertAlmostEqual(t["booked_window"], t["allin_window"], places=9)   # every line booked once
        # the fiscal model's paths: the ledger keeps $1 billion per row, so the window is within $3 billion
        win = sum(sum(self.path(r)[y] for y in W) for r in OWNERS[1:]) + sum(
            sum(self.part("HLT-4", n)[y] for y in W) for n, _, _, g in self.b["components"]["HLT-4"] if g)
        self.assertAlmostEqual(win, t["allin_window"] * 1000, delta=3.0)
        fy40 = sum(self.path(r)[2040] for r in OWNERS[1:]) + sum(
            self.part("HLT-4", n)[2040] for n, _, _, g in self.b["components"]["HLT-4"] if g)
        self.assertAlmostEqual(fy40, t["allin_fy2040"], delta=1.0)

    def test_status_rule_lowers_new_users_only(self):
        """DEC-2026-11-13-01: long-term care covers people with lawful or registered status; only new users and
        nursing-home residents with no status come out (Medicaid's current users already have status)."""
        names = [n for n, _, _, _ in self.b["components"]["HLT-9"]]
        self.assertIn("status-rule", names)
        sr = self.part("HLT-9", "status-rule")
        self.assertTrue(all(sr[y] == 0 for y in range(2030, 2035)))
        self.assertTrue(all(sr[y] < 0 for y in range(2035, 2041)))
        win = sum(sr[y] for y in W)
        self.assertAlmostEqual(win, -3.3, delta=0.15)                 # 6bcd-cost.md part 2b
        benefit = sum(self.part("HLT-9", "home-care-benefit")[y] for y in W)
        self.assertLess(-win, 0.01 * benefit)                          # a small share: few users have no status

    def test_down_payment_retired_not_double_counted(self):
        comps = {(r["owner"], r["component"]) for r in rows("fiscal-components.csv")}
        self.assertNotIn(CB.RETIRED[:2], comps)
        names = [n for n, _, _, _ in self.b["components"]["HLT-4"]]
        self.assertIn("bridge", names)
        for n in CB.HEALTH_HLT4:
            self.assertIn(("HLT-4", n), comps)
        bridge = self.part("HLT-4", "bridge")
        self.assertTrue(all(bridge[y] == 0 for y in range(2036, 2057)))
        self.assertAlmostEqual(sum(self.path("HLT-4")[y] for y in W) / 1000, self.bills["HLT-4"]["gf_mid"], places=9)

    def test_states_payment_is_an_offsetting_receipt(self):
        pay = self.part("HLT-9", "states-payment")
        self.assertTrue(all(pay[y] < 0 for y in range(2035, 2057)))
        self.assertTrue(all(pay[y] == 0 for y in range(2030, 2035)))
        self.assertAlmostEqual(-pay[2040], self.b["totals"]["receipts_fy2040"], delta=0.5)
        note = next(r for r in rows("fiscal-components.csv") if r["owner"] == "HLT-9" and r["component"] == "states-payment")
        self.assertIn("JOINT RISK", note["basis"])
        self.assertIn("HLT-7.17", note["basis"])
        self.assertIn("$650B", note["basis"])

    def test_part_c_is_counted_once(self):
        A = json.load(open(HERE / "recovery-budget" / "assumptions.json"))
        self.assertEqual(A["education_components"]["care"].get("ledger_row"), "FAM-2")
        self.assertNotIn("anchors", A["education_components"]["care"])
        adoption = json.load(open(INPUTS / "education-adoption.json"))
        self.assertIn("FAM-2", adoption["cost_assumptions"]["transferred_agenda"])


class CareIncidence(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.inc = CB.incidence()
        cls.rows = {r["id"]: r for r in rows("incidence-rows.csv")}
        cls.keys = {r["key"]: r for r in rows("incidence-keys.csv")}
        cls.phase = {r["id"]: r for r in rows("incidence-phase-in.csv")}

    def test_rows_keys_and_shapes(self):
        self.assertEqual((self.rows["F2"]["amount"], self.rows["F2"]["parts"]), ("[FAM-2]", "childcare"))
        self.assertEqual((self.rows["H4"]["amount"], self.rows["H4"]["parts"]), ("[HLT-4]", "medicaid_ltc"))
        self.assertEqual((self.rows["H9"]["amount"], self.rows["H9"]["parts"], self.rows["H9"]["set"]),
                         ("[HLT-9]", "ltc_universal", "option"))
        for key, (q, t1) in self.inc["key"].items():
            k = self.keys[key]
            self.assertEqual([float(k[c]) for c in ("q1", "q2", "q3", "q4", "q5")], q, key)
            self.assertEqual(float(k["top1"]), t1, key)
            self.assertAlmostEqual(sum(q), 100, places=6)
        for rid, v in self.inc["shapes"].items():
            r = self.phase[rid]
            self.assertEqual(r["method"], "norm", rid)
            self.assertEqual([float(r["y%d" % y]) for y in W], v, rid)

    def test_dy6_scales_with_the_program(self):
        (lo, mid, hi, opt), _ = CB.dynamic_dy6()
        r = next(r for r in rows("ledger-dynamic.csv") if r["id"] == "DY6")
        self.assertEqual(tuple(float(r[c]) for c in ("lo", "mid", "hi", "optimistic_mid")), (lo, mid, hi, opt))


if __name__ == "__main__":
    unittest.main()
