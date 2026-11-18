"""The health financing booking (stage E's financing checkpoint, DEC-2026-11-15-05 to -29) matches its derivation.

Role: protects the booking of package E with the unified household contribution (dossiers/foundations/
health-cost-review.md part 5; health-household-contribution.md). Run by run-all.sh after the budget model (it reads
build/ledger.json and build/recovery-budget-paths.csv). Checks that:
- HLT-7 is booked on the corrected path: the Medicare seam is CBO's (DEC-2026-11-15-28: about -$0.30T in FY2040 and
  -$1.28T over FY2030-39), the path with no correction reproduces the rebased model, and D1, D5 and D2 land at the
  decided figures (DEC-2026-11-15-06 to -08), D2 only from FY2037;
- the states pay 100% of their former Medicaid spending on the rebased base (DEC-2026-11-15-25): health_cost_review's
  $466B in FY2040;
- the package's rows equal health_cost_review.unified_package() in FY2040 (DEC-2026-11-15-09 to -24), the employer
  contribution follows the waves from FY2031, and nothing that depends on part 9, question 9 (the household
  contribution's transition path, not decided: DEC-2026-11-15-29) is booked before the January 2035 endpoint;
- the fiscal model books each row at its FY2040 figure;
- health's first call on booked revenue is about $516B in FY2040 and the plan-wide FY2040 gap about $586B
  (DEC-2026-11-15-11, -20), on the budget model's own run.
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
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE / "household"))


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


import health_booking as HB  # noqa: E402
import health_cost_review as CR  # noqa: E402
import health_financing as HF  # noqa: E402

fiscal = load("hfb_fiscal", HERE / "fiscal-model.py")
W = range(2030, 2040)
STREAM_IDS = ("HS1", "HS2", "HS3", "HS4", "H1a")
ENDPOINT_ROWS = ("HCU", "HCW", "HCA", "HCP", "HCH") + STREAM_IDS


# Work's booking moved the plan-wide gap by these amounts ($B, case mixed; FY2040 602.7 to 614.0): lower in FY2030-36, where it
# replaces the booked legacy rows (LAB-5, LAB-8, LAB-9), higher after. Health's own first call is unchanged.
WORK_BOOKING = {2030: -0.3, 2031: -10.9, 2032: -8.8, 2033: -10.1, 2034: -8.3, 2035: -8.2, 2036: -8.1, 2037: 10.6, 2038: 10.9, 2039: 11.2, 2040: 11.3}
WORK_BOOKING_FY2040 = WORK_BOOKING[2040]


class HealthFinancingBooking(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.b = HB.booking()
        cls.cor = HB.corrected()
        cls.fin = HB.financing()
        cls.ledger = json.load(open(BUILD / "ledger.json"))
        cls.bills = {r["id"]: r for r in cls.ledger["bills"]}
        cls.rev = {r["id"]: r for r in cls.ledger["revenue"]}
        cls.base = fiscal.read_baseline(ROOT / "models/data/fiscal-baseline.csv")

    def part(self, name):
        amount, p = next((a, p) for n, a, p in fiscal.PR.COMPONENTS["HLT-7"] if n == name)
        return fiscal.row_path(self.base, amount, p, p.get("years"))

    def revenue(self, rid):
        return {y: -v for y, v in fiscal.row_path(self.base, -self.rev[rid]["mid"], fiscal.PR.REVENUE[rid], rid).items()}

    def test_seam_and_corrections(self):
        f40 = self.b["fy2040"]
        self.assertAlmostEqual(f40["seam"], -300, delta=5)                        # DEC-2026-11-15-28
        self.assertAlmostEqual(self.b["totals"]["seam_window"], -1.28, delta=0.005)
        # the rebased model with no correction is health_financing's rebased path (rebuild() reproduces groups())
        sm = HF.seam()
        for y in W:
            self.assertAlmostEqual(self.cor["model"][y], sm["rebased"][y], delta=1e-6, msg=y)
        self.assertTrue(all(abs(v) < 1e-6 for v in CR.check_reproduces().values()))
        # the nine corrections: the cost review's errors-only net federal change, about -$650B in FY2040
        self.assertAlmostEqual(f40["corrections"], -650, delta=10)

    def test_design_memos(self):
        f40 = self.b["fy2040"]
        self.assertAlmostEqual(f40["admin-4pct"], -85.1, delta=1.0)       # D1, DEC-2026-11-15-07
        self.assertAlmostEqual(f40["drug-prices"], -115.3, delta=2.0)     # D5, DEC-2026-11-15-06
        self.assertAlmostEqual(f40["national-budget"], -249.5, delta=2.0)  # D2, DEC-2026-11-15-08
        d2 = self.b["hlt7_fy"]["national-budget"]
        self.assertTrue(all(d2[y] == 0 for y in range(2030, 2037)))
        self.assertTrue(all(d2[y] < d2[y - 1] for y in range(2038, 2041)))
        # the ledger's high end leaves D2 out (never achieved, EV-CAR-742)
        lo, mid, hi = self.b["ledger"]["HLT-7"]
        self.assertGreater(hi - mid, -sum(d2[y] for y in W) / 1000)

    def test_states_at_100_percent(self):
        st = self.b["hlt7_fy"]["states-payment"]
        g40 = st[2040] / -(self.cor["state_former_full"] - self.cor["states_netted_full"])
        total = -st[2040] + self.cor["states_netted_full"] * g40
        self.assertAlmostEqual(total, 465.6, delta=2)                     # health_cost_review's states, FY2040
        self.assertEqual(st[2030], 0)
        self.assertTrue(all(st[y] < 0 for y in range(2031, 2041)))

    def test_rows_equal_the_package_in_fy2040(self):
        o, r = self.fin["package"], self.b["fy2040"]["revenue"]
        lost = o["lost"]
        self.assertAlmostEqual(r["HCU"], o["household_collected"], places=6)
        self.assertAlmostEqual(r["HCU"], 770.3, delta=0.5)
        for k, v in (("HCW", lost["W"]), ("HCA", lost["A"]), ("HCP", lost["hxp"]), ("HCH", lost["H1b"])):
            self.assertAlmostEqual(r[k], -v, places=6, msg=k)
        self.assertAlmostEqual(r["HEC"], o["employer_gross"], delta=0.01)
        self.assertAlmostEqual(r["HEC"], 1945.3, delta=0.5)
        self.assertAlmostEqual(r["HEX"], -self.fin["tau"] * r["HEC"], places=6)
        self.assertAlmostEqual(self.b["fy2040"]["worker-credit"], o["credit_bn"], delta=0.01)
        for k, (_, v, _, _) in zip(STREAM_IDS, CR.NEW_STREAMS):
            self.assertAlmostEqual(r[k], v, places=6, msg=k)
        # the decided design: R 2.25%, S = 5 + H1b's fold-in (5.96), the steady exemption from 138% to 250%
        u = self.fin["spec"]
        self.assertEqual((u["R"], u["lo"], u["hi"], u["form"]), (2.25, 1.38, 2.5, "linear"))
        self.assertAlmostEqual(u["S"], 5.96, delta=0.005)
        self.assertAlmostEqual(o["reassigned"], 515.7, delta=0.5)

    def test_timing(self):
        """DEC-2026-11-16-01 to -03: the fold-in starts with the January 2035 endpoint; the household contribution steps
        with the waves from 2031 (5-point surcharge, no fold-in); the streams start in FY2030; the employer contribution
        follows the moved coverage from 2031, with the allowance."""
        rf = self.b["revenue_fy"]
        for k in ("HCW", "HCA", "HCP", "HCH"):
            self.assertTrue(all(rf[k][y] == 0 for y in range(2030, 2035)), k)
            self.assertTrue(0.6 < rf[k][2035] / rf[k][2036] < 0.75, k)     # FY2035: three quarters of a year
        hcu = rf["HCU"]
        self.assertEqual(hcu[2030], 0)
        self.assertEqual(HB.WAVE_STEPS, {2031: 0.6, 2032: 0.6, 2033: 1.0, 2034: 1.4})
        f = self.fin
        self.assertTrue(all(hcu[y] > 0 for y in range(2031, 2041)))
        # FY2032 is calendar 2031-32's 0.6% and the 5-point surcharge, at FY2032's income growth
        per = {y: HF.per_point(HF.plan_gap(), y)["high_income"] for y in (2032, 2040)}
        want = (f["base_2040"] * 0.6 / 2.25 + f["surcharge5_2040"]) * per[2032] / per[2040]
        self.assertAlmostEqual(hcu[2032], want, places=6)
        self.assertLess(hcu[2034], hcu[2035])
        g30 = HF.per_point(HF.plan_gap(), 2030)["high_income"] / per[2040]
        for k, (_, v, _, _) in zip(STREAM_IDS, CR.NEW_STREAMS):     # in full from FY2030, grown with GDP
            self.assertAlmostEqual(rf[k][2030], v * g30, places=6, msg=k)
            self.assertTrue(all(rf[k][y] < rf[k][y + 1] for y in range(2030, 2040)), k)
        cr = self.b["hlt7_fy"]["worker-credit"]
        self.assertTrue(all(cr[y] == 0 for y in range(2030, 2035)))
        hec = rf["HEC"]
        self.assertEqual(hec[2030], 0)
        self.assertTrue(all(hec[y] > 0 for y in range(2031, 2041)))     # on the premiums of the coverage moved
        self.assertTrue(hec[2033] > 2.5 * hec[2032])
        self.assertAlmostEqual(f["allowance_share"], HF.band_share() and CR.SMALL_FIRM_ALLOWANCE_SHARE / HF.band_share())

    def test_fiscal_model_books_the_rows(self):
        for k, v in self.b["fy2040"]["revenue"].items():
            p = self.revenue(k)
            self.assertAlmostEqual(p[2040], v, delta=0.5, msg=k)
            self.assertAlmostEqual(sum(p[y] for y in W) / 1000, self.b["revenue"][k][1], delta=0.0005, msg=k)
        for k in HB.NEW_HLT7:
            self.assertAlmostEqual(self.part(k)[2040], self.b["fy2040"][k], delta=0.5, msg=k)
        self.assertAlmostEqual(self.part("plan-spending")[2040], self.b["fy2040"]["spending"], delta=0.5)
        self.assertEqual((self.rev["H1a"]["channel"], self.rev["H1a"]["in_base"]), ("General fund", "Yes"))

    def test_credit_ends_after_the_window(self):
        """DEC-2026-11-15-24: in full through 2044, none from 2049. Both the fiscal model and the provisions library
        (whose long-run path to 2056 is the debt model's) book fiscal-after.csv's phase-down, not the 2039 level grown."""
        want = self.b["after"]["HLT-7/worker-credit"]
        rows = {r["id"]: r for r in csv.DictReader(open(ROOT / "models/data/inputs/fiscal-after.csv", newline=""))}
        r = rows["HLT-7/worker-credit"]
        self.assertEqual({y: float(r["y%d" % y]) for y in HB.AFTER_YEARS}, want)
        fm = self.part("worker-credit")
        # the budget library's provisions.py and data.py, not the household model's modules of the same names
        keep = sys.modules.get("data")
        sys.modules["data"] = load("data", HERE / "budget" / "data.py")
        try:
            P = load("hfb_provisions", HERE / "budget" / "provisions.py")
        finally:
            if keep is not None:
                sys.modules["data"] = keep
            else:
                del sys.modules["data"]
        S = P.specs()
        pv = P.deficit_path(S["HLT-7"], self.bills["HLT-7"]["gf_mid"])
        full = fiscal.row_path(self.base, self.bills["HLT-7"]["gf_mid"], fiscal.PR.BILLS["HLT-7"], "HLT-7")
        for y in range(2040, 2057):
            self.assertAlmostEqual(fm[y], want.get(y, 0.0), places=6, msg=y)
            self.assertAlmostEqual(pv[y], full[y], places=6, msg=y)      # the two agree, credit included
        self.assertTrue(all(fm[y] == 0 for y in range(2050, 2057)))
        self.assertLess(fm[2049], 0.1 * fm[2044])
        self.assertGreater(fm[2044], fm[2040])

    def test_employer_contribution_after_the_window(self):
        """DEC-2026-11-15-23 (b): the no-offer phase-in is full in 2044, so HEC's after-window path adds its last
        steps (FY2041-45) instead of growing FY2040's partly phased-in level; HEX follows at the exclusion's rate."""
        rows = {r["id"]: r for r in csv.DictReader(open(ROOT / "models/data/inputs/fiscal-after.csv", newline=""))}
        g = fiscal.growth_index(self.base, "rev_payroll")
        for k in ("HEC", "HEX"):
            want = self.b["after"][k]
            self.assertEqual({y: float(rows[k]["y%d" % y]) for y in HB.HEC_AFTER_YEARS}, want, k)
            p = self.revenue(k)
            for y in HB.HEC_AFTER_YEARS:     # fiscal-after.csv keeps a revenue row's gain negative
                self.assertAlmostEqual(p[y], -want[y], delta=0.01, msg=(k, y))
            self.assertAlmostEqual(p[2046] / p[2045], fiscal.growth_index(self.base, fiscal.PR.REVENUE[k]["grow"])[2046]
                                   / fiscal.growth_index(self.base, fiscal.PR.REVENUE[k]["grow"])[2045], places=9)
        hec = {y: -v for y, v in self.b["after"]["HEC"].items()}
        self.assertAlmostEqual(hec[2040], self.b["fy2040"]["revenue"]["HEC"], delta=0.01)
        for y in range(2041, 2046):     # above FY2040 grown with pay, by the steps no longer uncharged
            self.assertGreater(hec[y], hec[2040] * g[y] / g[2040], y)
        self.assertAlmostEqual(hec[2045] / g[2045], (hec[2040] + self.fin["path"][2040]["phase_in"]) / g[2040], delta=0.01)

    def test_first_call_and_the_plan_wide_gap(self):
        calls, need, own = HB.first_call(self.b)
        # DEC-2026-11-15-20's about $516B, plus the status rule priced on the corrected base (about $15B in FY2040)
        self.assertAlmostEqual(calls[2040], 532.1, delta=3)
        paths = {int(r["year"]): float(r["agenda_gf_primary_bn"]) for r in csv.DictReader(open(BUILD / "recovery-budget-paths.csv"))
                 if r["case"] == "mixed"}
        self.assertAlmostEqual(paths[2040], CR.GAP_BEFORE_REASSIGN + calls[2040] + WORK_BOOKING_FY2040, delta=3)
        self.assertAlmostEqual(paths[2040], 614.0, delta=5)        # DEC-2026-11-15-11's $586B, plus the status rule, plus work's booking (602.7 before it)
        before = HF.paths()
        for y in W:     # the rest of the plan's gap before the booking, plus health's first call
            rest = float(before[y]["agenda_gf_primary_bn"]) - HF.need_path(HF.seam())[y]["booked"]
            self.assertAlmostEqual(paths[y], rest + calls[y] + WORK_BOOKING[y], delta=6, msg=y)
        # with the streams from FY2030 and the steps from 2031, health's own sources exceed its need before 2035
        self.assertTrue(all(calls[y] < 0 for y in range(2030, 2035)))

    def test_transition_options(self):
        t = HB.transition_options()
        o = t["options"]
        self.assertEqual(o["endpoint"]["collected_window"], 0)
        booked = sum(self.fin["before_endpoint"][y] for y in range(2031, 2036))      # 'waves', at the rounded steps
        self.assertAlmostEqual(booked, o["waves"]["collected_window"], delta=0.1 * booked)
        self.assertLess(o["waves"]["collected_window"], o["full"]["collected_window"])
        self.assertGreater(o["waves"]["collected_window"], 0)
        for y in range(2031, 2035):
            self.assertLess(t["moved_share"][y], 1)
        self.assertEqual(t["moved_share"][2035], 1)


if __name__ == "__main__":
    unittest.main()
