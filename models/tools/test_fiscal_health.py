"""The health plan's booking (care milestone review F-4; dossiers/care/6-cost.md part 5) matches the dossier's path.

Role: protects care fix step 5. Run by run-all.sh after the fiscal model (it reads build/ledger.json); standard library
only, plus the dossier's own path script through health_booking.py. Checks that:
- every health shape, component and ledger amount in models/data/inputs/ equals health_booking.py's derivation from
  dossiers/care/tools/health_path.py, so a change to the dossier's path fails here instead of drifting;
- the fiscal model books the spending line at the path's FY2040 figure and the exclusion revenue (HX) at its own;
- the plan's net cost on the model's basis (HLT-1 plus HLT-7's spending line, less HX) is the dossier's $21.74T with
  the Medicare seam (DEC-2026-11-15-28) and the cost review's corrections (DEC-2026-11-15-05) taken out, as booked by
  the health financing booking (test_fiscal_health_financing.py checks its other rows);
- HLT-7's status-rule component (DEC-2026-11-12-19) is care_base_correction's coverage, less the Emergency Medicaid
  and the hospitals' DSH-type uncompensated-care share (DEC-2026-11-13-02) that keep paying, booked once on its own
  component;
- the package's revenue rows are general-fund base revenue, HX among them, and none is netted in HLT-7;
- HLT-3 and HLT-5 are retired, HLT-1, HLT-2 and HLT-6 end with the 2035 endpoint, and HLT-4's retired parts end
  with their waves while its safety-net part continues (its long-term care is care_booking.py's, test_fiscal_care.py);
- the household test's health rows (incidence-rows.csv H7h, H7w, H7x, H7c and package E's HCUw, HCU, HCW to HCH, HEC,
  HEX and HS1 to HS4, with PB, H2 and H5p; their keys and phase-in shapes) equal health_booking.py's incidence_booked()
  derivation on the corrected, booked path, and scenario Q-H7 carries them with health's contributions outside the
  revenue-mix test (DEC-2026-11-15-29).
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
        # HLT-4's row is care_booking.py's (care parts B-D booking): health's three parts keep their amounts in it
        for n, amount, _ in self.b["hlt4_parts"]:
            self.assertEqual(float(comps[("HLT-4", n)]["mid10"]), amount, n)
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
        for k, (lo, mid, hi) in self.b["revenue"].items():     # the package's rows (health_booking.financing())
            self.assertEqual(tuple(float(rev[k][c]) for c in ("lo", "mid", "hi")), (lo, mid, hi), k)
        prof = {r["id"]: r for r in rows("fiscal-profiles.csv") if r["table"] == "base revenue"}
        for k in self.b["revenue"]:
            self.assertAlmostEqual(float(prof[k]["perm"]), self.b["perms"][k], places=6, msg=k)
        hx = next(r for r in rows("fiscal-profiles.csv") if r["id"] == "HX")
        self.assertAlmostEqual(float(hx["perm"]), self.b["perms"]["HX"], places=6)

    def test_h1a_booked_once(self):
        """DEC-2026-11-16-02 gives H1a's FY2030-34 and FY2035's first quarter to Medicare's HI fund: the funds model
        credits HI with them (funds-parameters.csv hi_h1a_bn), the ledger row books only the rest on the general fund,
        so the two add to the stream once, and D3 charges households the whole stream (financing audit part D, item 1)."""
        hi = self.b["hi"]["H1a"]
        par = next(r for r in rows("funds-parameters.csv") if r["key"] == "hi_h1a_bn")
        self.assertEqual([float(x) for x in par["value"].split("/")], hi[:6])
        self.assertTrue(all(v == 0 for v in hi[6:]))
        gf = self.b["years"]["H1a"]
        self.assertTrue(all(v == 0 for v in gf[:5]))
        full = HB.financing()["rows"]["H1a"]
        for i, y in enumerate(W):
            self.assertAlmostEqual(gf[i] + hi[i], full[y], delta=0.011, msg=y)
        self.assertAlmostEqual(self.rev["H1a"]["mid"] + sum(hi) / 1000, sum(full[y] for y in W) / 1000, delta=0.001)
        inc = next(r for r in rows("incidence-rows.csv") if r["id"] == "H1a")
        self.assertAlmostEqual(eval(inc["amount"].replace("[H1a]", repr(self.rev["H1a"]["mid"]))),
                               sum(full[y] for y in W) / 1000, delta=0.001)

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
        fedcov = t(self.part("HLT-7", "federal-coverage"))
        net = t(self.path("HLT-1")) + t(self.part("HLT-7", "plan-spending")) + fedcov + t(hx)
        # the dossier's $21.74T, less part 6's federal-coverage correction (FEHB, TRICARE and the VA; B6 item 7), the
        # Medicare seam (-$1.28T, DEC-2026-11-15-28) and the cost review's corrections (DEC-2026-11-15-05)
        T = self.b["totals"]
        self.assertAlmostEqual(net, T["net_window"] + T["federal_coverage_net"] + T["seam_window"] + T["corrected_window"],
                               delta=0.002)
        self.assertAlmostEqual(round(T["net_window"], 2), 21.74)
        self.assertAlmostEqual(T["seam_window"], -1.28, delta=0.005)
        self.assertAlmostEqual(self.b["totals"]["federal_coverage_net"], -0.365, delta=0.005)   # part 6: $0.2-0.5T high
        self.assertLess(fedcov, 0)
        self.assertAlmostEqual(t(self.part("HLT-7", "worker-help")), 0.06, places=9)   # HLT-7.16, FY2033-38
        self.assertEqual(self.part("HLT-7", "worker-help")[2040], 0)
        self.assertAlmostEqual(round(self.b["totals"]["with_contribution"], 2), 16.43)

    def test_status_rule_is_booked_once(self):
        """DEC-2026-11-12-19: care's base no longer covers people with no status beyond the residual; Emergency
        Medicaid keeps paying for them, and so does hospitals' DSH-type uncompensated-care share (DEC-2026-11-13-02)
        (dossiers/care/tools/status_rule.py; 6-cost.md part 2b)."""
        t = lambda p: sum(p[y] for y in W) / 1000  # noqa: E731
        sr = self.part("HLT-7", "status-rule")
        self.assertAlmostEqual(t(sr), self.b["totals"]["status_rule_window"], delta=0.0005)
        self.assertAlmostEqual(sr[2040], self.b["fy2040"]["status_rule"], delta=0.5)
        # part 2b's -$0.41T on care's base; on the corrected base the people removed cost the cost review's price for
        # the newly covered, with D1 and D5 (health_booking.status_rule(); #394's follow-up)
        sr_ = HB.status_rule(HB.corrected())
        self.assertAlmostEqual(sr_["care_base"][1] / 1000, -0.4105, delta=0.0005)
        self.assertAlmostEqual(self.b["totals"]["status_rule_window"], -0.2293, delta=0.0005)
        self.assertTrue(all(0.5 < sr_["scale"][y] < 0.7 for y in range(2031, 2041)))
        self.assertTrue(all(sr[y] < 0 for y in range(2031, 2041)))     # a saving from wave 1
        self.assertEqual(sr[2030], 0)
        lo, mid, hi = self.b["totals"]["status_rule_range"]
        self.assertLess(lo, mid)
        self.assertLess(mid, hi)
        # the same people as the immigration model's care_base_correction, whose coverage part it is
        SR = load("t_status_rule", ROOT / "dossiers/care/tools/status_rule.py")
        h = SR.health(1)
        self.assertAlmostEqual(sum(h["removed"][y] for y in W), -429.5, delta=0.5)
        self.assertGreater(sum(h["em_kept"][y] for y in W), 0)
        # DEC-2026-11-13-02: the DSH-type share, on everyone with no status as Medicaid moves into the plan
        dsh = h["dsh_kept"]
        self.assertAlmostEqual(sum(dsh[y] for y in W), 8.4, delta=0.05)
        self.assertAlmostEqual(dsh[2040], 1.1, delta=0.05)
        self.assertEqual(dsh[2030], 0)
        self.assertTrue(all(dsh[y] > 0 for y in range(2031, 2041)))
        for y in list(W) + [2040]:
            self.assertAlmostEqual(h["net"][y], h["removed"][y] + h["em_kept"][y] + dsh[y], places=9)
        lo, hi = (sum(SR.health(i)["dsh_kept"][y] for y in W) for i in (0, 2))
        self.assertLess(lo, sum(dsh[y] for y in W))
        self.assertLess(sum(dsh[y] for y in W), hi)

    def test_package_rows_are_base_revenue(self):
        # HX and the package's rows (DEC-2026-11-15-09) are general-fund base revenue; none is netted in HLT-7
        health = [r for r in self.ledger["revenue"] if "HLT-7" in r["option"] or "care" in r.get("source", "")]
        self.assertEqual([r["id"] for r in health], ["HX"])
        for k in ["HX"] + list(self.b["revenue"]):
            self.assertEqual((self.rev[k]["channel"], self.rev[k]["in_base"]), ("General fund", "Yes"), k)
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
        safety = self.part("HLT-4", "safety-net-centers-residency-momnibus-title-x")   # long-term care is care's now
        self.assertGreater(safety[2040], safety[2039])
        total = self.path("HLT-4")
        self.assertAlmostEqual(sum(total[y] for y in W) / 1000, self.bills["HLT-4"]["gf_mid"], places=9)


class HealthIncidence(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.inc = HB.incidence()
        cls.ib = HB.incidence_booked()
        cls.rows = {r["id"]: r for r in rows("incidence-rows.csv")}
        cls.keys = {r["key"]: r for r in rows("incidence-keys.csv")}
        cls.phase = {r["id"]: r for r in rows("incidence-phase-in.csv")}

    def test_rows_equal_the_derivation(self):
        """The D3 rows are on the corrected, booked path (#394's follow-up): HLT-7's household rows with the cost
        review's correction, the credit, and package E's household-facing rows with the four new streams."""
        ib = self.ib
        for rid, amount in ib["amounts"].items():
            r = self.rows[rid]
            self.assertEqual(r["set"], "option", rid)
            self.assertEqual(r["amount"], str(amount), rid)
            self.assertEqual(r["parts"], ib["parts"][rid], rid)
            self.assertEqual(r["side"], "benefit" if rid in ("H7h", "H7w", "H7c") else "cost", rid)
        # each row's ten-year amount is its booked path's: the ledger's for the package's rows, HCU split in two
        led = {r["id"]: r["mid"] for r in json.load(open(BUILD / "ledger.json"))["revenue"]}
        for rid in ("HCW", "HCA", "HCP", "HCH", "HEC", "HEX", "HS1", "HS2", "HS3", "HS4"):
            self.assertAlmostEqual(led[rid], ib["window"][rid], delta=0.0015, msg=rid)
        self.assertAlmostEqual(ib["window"]["HCU"] + ib["window"]["HCUw"], led["HCU"], delta=0.0015)
        self.assertAlmostEqual(ib["rows"]["H7c"], ib["credit_window"], delta=0.0005)
        # the corrections against the care path: the spending that stays outside the plan, and federal coverage
        self.assertLess(ib["rows"]["H7h"], self.inc["rows"]["H7h"])
        self.assertAlmostEqual(ib["rows"]["H7w"] / self.inc["rows"]["H7w"], 1 - HB.FEDCOV_REVENUE_2032 / 680.0, delta=0.001)
        self.assertEqual(self.rows["H1a"]["set"], "package")          # H1a has been a row of Q since before health
        self.assertEqual(self.rows["H5p"]["amount"], "0")
        self.assertEqual((self.rows["PB"]["amount"], self.rows["H2"]["amount"]), ("0.28*[HLT-2]", "1.28*[HLT-2]"))

    def test_keys_and_shapes_equal_the_derivation(self):
        for key, (q, t1) in list(self.inc["key"].items()) + list(self.ib["keys"].items()):
            k = self.keys[key]
            self.assertEqual([float(k[c]) for c in ("q1", "q2", "q3", "q4", "q5")], q, key)
            self.assertEqual(float(k["top1"]), t1, key)
            self.assertAlmostEqual(sum(q), 100, places=6)
        shapes = {**{k: v for k, v in self.inc["shapes"].items() if k not in ("H7h", "H7w")}, **self.ib["shapes"]}
        for rid, v in shapes.items():
            r = self.phase[rid]
            self.assertEqual(r["method"], "norm", rid)
            self.assertEqual([float(r["y%d" % y]) for y in W], v, rid)
        self.assertEqual((self.phase["PB"]["same_as"], self.phase["H7x"]["same_as"]), ("H2", "H7w"))

    def test_scenario_and_revenue_mix(self):
        """Scenario Q-H7 carries every health row; DEC-2026-11-15-29 leaves health's contributions out of D3's
        revenue-mix test, in d3.py as in health_booking.py."""
        S = json.load(open(INPUTS / "scenarios.json"))
        q = next(s for s in S["incidence"] if s["id"] == "Q-H7")
        self.assertEqual(set(q["options"]) - {"DEC"}, set(self.ib["amounts"]) | {"H9"})
        D3 = load("t_d3", HERE / "household" / "d3.py")
        self.assertEqual(D3.HEALTH_CONTRIBUTIONS, HB.D3_CONTRIBUTIONS)
        self.assertTrue(set(HB.D3_CONTRIBUTIONS) <= set(self.ib["amounts"]))
        self.assertNotIn("HEX", HB.D3_CONTRIBUTIONS)

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
        self.assertAlmostEqual(self.inc["full_scale"]["household_removed"], 1547.3, delta=1.0)  # 6-cost.md part 8


if __name__ == "__main__":
    unittest.main()
