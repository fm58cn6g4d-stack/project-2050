#!/usr/bin/env python3
"""Unit tests for democratic renewal's two model tools: democratic_renewal_cost.py (section 6) and
democratic_renewal_pace.py (section 7, part 1.3, and decision-sheet item D4).

Role: pins the figures dossiers/foundations/democratic-renewal/6-cost.md and 7-validation.md publish, so a change
to the budget model's audit lines or to either tool that moves a published figure fails here (milestone review C-6,
`review-milestone.md`). Status: current (milestone fix step 1). Run by models/tools/run-all.sh, and so by
`bash .github/scripts/run-checks.sh`.

    python3 models/tools/test_democratic_renewal.py
"""
import importlib.util
import os
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))


def _load(name, file):
    spec = importlib.util.spec_from_file_location(name, os.path.join(HERE, file))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


cost = _load("democratic_renewal_cost", "democratic_renewal_cost.py")
pace = _load("democratic_renewal_pace", "democratic_renewal_pace.py")
YEARS = list(range(2030, 2040))


class CostTool(unittest.TestCase):
    """6-cost.md, parts 1, 3, 5 and 8."""

    @classmethod
    def setUpClass(cls):
        cls.s = cost.summary()
        cls.rows, cls.other = cost.booked()

    def test_booked_rows_by_year(self):
        # 6-cost.md part 1.1, rounded to one decimal as the table prints them.
        table = {
            "DEM-1": [0.8, 0.9, 0.9, 0.9, 1.0, 1.0, 1.1, 1.1, 1.1, 1.2],
            "DEM-11": [1.8, 1.8, 1.9, 1.9, 2.0, 2.0, 2.1, 2.1, 2.2, 2.2],
            "DEM-16": [0.8, 0.9, 0.9, 0.9, 1.0, 1.0, 1.1, 1.1, 1.1, 1.2],
            "DEM-17": [3.8, 4.0, 4.1, 4.3, 4.4, 4.6, 4.8, 0, 0, 0],
            "DEM-3": [0, 0, 0, 1.3, 1.3, 1.4, 1.4, 1.5, 1.5, 1.6],
            "CRT-P1": [0.3, 0.6, 1.0, 1.0, 1.1, 1.1, 1.1, 1.2, 1.2, 1.3],
            "CAP-8": [1.8, 3.6, 3.8, 3.9, 4.1, 4.2, 4.4, 4.6, 4.7, 4.9],
            "CAP-7S": [11.4, 19.6, 21.2, 19.6, 16.3, 9.8, 0, 0, 0, 0],
            "CAP-7": [8.6, 17.8, 27.7, 28.7, 29.8, 30.9, 32.1, 33.3, 34.5, 35.8],
        }
        for row, values in table.items():
            for y, v in zip(YEARS, values):
                with self.subTest(row=row, year=y):
                    self.assertAlmostEqual(self.rows[row][y], v, delta=0.05 + 1e-9)

    def test_booked_totals(self):
        b = self.s["booked"]
        for row, (w, f) in {"DEM-1": (10.0, 1.22), "DEM-11": (20.0, 2.26), "DEM-16": (10.0, 1.22),
                            "DEM-17": (30.0, 0.0), "DEM-3": (10.0, 1.65), "CRT-P1": (10.0, 1.33),
                            "CAP-8": (40.0, 5.09), "CAP-7S": (98.0, 0.0), "CAP-7": (279.2, 37.20)}.items():
            with self.subTest(row=row):
                self.assertAlmostEqual(b[row]["fy2030_39"], w, delta=0.05)
                self.assertAlmostEqual(b[row]["fy2040"], f, delta=0.005)
        self.assertAlmostEqual(self.s["booked_all"]["fy2030_39"], 507.2, delta=0.05)
        self.assertAlmostEqual(self.s["booked_all"]["fy2040"], 49.98, delta=0.005)

    def test_booked_all_by_year(self):
        all_rows = [29.4, 49.2, 61.5, 62.6, 60.9, 56.1, 48.0, 44.8, 46.5, 48.2]
        for y, v in zip(YEARS, all_rows):
            with self.subTest(year=y):
                self.assertAlmostEqual(sum(r[y] for r in self.rows.values()), v, delta=0.05 + 1e-9)

    def test_contingency_and_gap(self):
        c = self.s["contingency"]
        self.assertAlmostEqual(c["surge"], 43.2, delta=0.05)
        self.assertAlmostEqual(c["sustained"], 29.7, delta=0.05)
        self.assertAlmostEqual(c["fy2040"], 4.7, delta=0.05)
        self.assertAlmostEqual(self.s["gap_2040"], 614.0, delta=0.05)
        sh = self.s["share_of_gap_2040"]
        self.assertAlmostEqual(100 * sh["booked"], 8.14, delta=0.005)  # 8.29 before the work booking raised the gap to 614.0
        self.assertAlmostEqual(100 * sh["unbooked"], 0.41, delta=0.005)
        self.assertAlmostEqual(100 * sh["unbooked_hi"], 0.62, delta=0.005)

    def test_other_lines(self):
        o = self.s["other"]
        g8 = o[cost.OTHER_LINES["G8"]]
        allowance = o[cost.OTHER_LINES["IRS yield allowance with smaller capacity budget"]]
        self.assertAlmostEqual(g8["fy2030_39"], -400.0, delta=0.05)
        self.assertAlmostEqual(allowance["fy2030_39"], 250.0, delta=0.05)
        self.assertAlmostEqual(g8["fy2030_39"] + allowance["fy2030_39"], -150.0, delta=0.05)
        self.assertAlmostEqual(g8["fy2040"] + allowance["fy2040"], -20.54, delta=0.005)
        ssa = o[cost.OTHER_LINES["SSA OASDI capacity reclassification"]]
        self.assertAlmostEqual(ssa["fy2030_39"], -15.0, delta=0.05)

    def test_unbooked_lines(self):
        u = self.s["unbooked"]
        for line, (mid, lo, hi, f) in {
            "DEM-17.02, the permanent library line": (7.84, 5.22, 10.45, 0.91),
            "CRT-5.09, the immigration court's structure": (6.87, 3.22, 9.74, 0.95),
            "CAP-6.01, statute tracking": (0.09, 0.05, 0.13, 0.01),
            "CRT-20.01, civil legal aid through LSC": (4.62, 2.31, 8.47, 0.66),
        }.items():
            with self.subTest(line=line):
                self.assertAlmostEqual(u[line]["fy2030_39"], mid, delta=0.005)
                self.assertAlmostEqual(u[line]["lo_30_39"], lo, delta=0.005)
                self.assertAlmostEqual(u[line]["hi_30_39"], hi, delta=0.005)
                self.assertAlmostEqual(u[line]["fy2040"], f, delta=0.005)
        a = self.s["unbooked_all"]
        self.assertAlmostEqual(a["fy2030_39"], 19.4, delta=0.05)
        self.assertAlmostEqual(a["lo_30_39"], 10.8, delta=0.05)
        self.assertAlmostEqual(a["hi_30_39"], 28.8, delta=0.05)
        self.assertAlmostEqual(a["fy2040"], 2.54, delta=0.005)

    def test_imm1_split_window(self):
        # 6-cost.md part 5: about -$4.3 billion over FY2036-39 (range -3.5 to -5.0). The FY2040 figure's year shape
        # is review C-6's open slip (-0.90 printed, 78% of -1.06 is -0.83), left to a later fix step.
        t = self.s["later_tier3"]["CRT-5.06, the judges' split, against IMM-1"]
        self.assertAlmostEqual(t["fy2030_39"], -4.3, delta=0.005)
        self.assertAlmostEqual(t["lo_30_39"], -3.5, delta=0.005)
        self.assertAlmostEqual(t["hi_30_39"], -5.0, delta=0.005)

    def test_self_check_passes(self):
        cost.check()


class PaceTool(unittest.TestCase):
    """7-validation.md part 1.3; 6-cost.md part 7 (D4)."""

    @classmethod
    def setUpClass(cls):
        cls.s = pace.summary()

    def test_ramp_mean(self):
        self.assertAlmostEqual(pace.ramp_mean(0.25, 0), 0.125)
        self.assertAlmostEqual(pace.ramp_mean(0.25, 3), 0.875)
        self.assertAlmostEqual(pace.ramp_mean(0.25, 4), 1.0)
        self.assertAlmostEqual(pace.ramp_mean(0.5, 1), 0.75)
        self.assertAlmostEqual(pace.ramp_mean(1 / 3, 2), 5 / 6)

    def test_full_strength_year(self):
        # 7-validation.md part 1.3: the fifth-a-year runs reach full strength in FY2035, not FY2034 (review C-6).
        self.assertEqual(pace.full_staff_year(0.20), 2035)
        self.assertEqual(pace.full_staff_year(0.25), 2034)
        self.assertEqual(pace.full_staff_year(1 / 3), 2033)

    def test_booked_path(self):
        for y, v in zip(range(2030, 2034), (8.56, 17.77, 27.66, 28.71)):
            self.assertAlmostEqual(self.s["booked"][y], v, delta=0.005)
        self.assertAlmostEqual(self.s["booked_window"], 279.2, delta=0.05)
        for y, v in zip(range(2030, 2033), (0.33, 0.67, 1.00)):
            self.assertAlmostEqual(self.s["booked_share_of_full"][y], v, delta=0.005)
        self.assertAlmostEqual(self.s["booked_implied_rate"], 0.50, delta=0.005)

    def test_the_three_bases(self):
        self.assertAlmostEqual(self.s["allocation_on_booked_ramp_window"], 243.9, delta=0.05)
        self.assertAlmostEqual(self.s["contingency_on_booked_ramp_window"], 35.3, delta=0.05)
        self.assertAlmostEqual(self.s["full_allocation_window"], 266.6, delta=0.05)
        self.assertAlmostEqual(self.s["part_g_own_path_window"], 250.7, delta=0.05)
        # Laid on the booked ramp, the allocation and the contingency add back to the booking.
        self.assertAlmostEqual(self.s["allocation_on_booked_ramp_window"] + self.s["contingency_on_booked_ramp_window"],
                               self.s["booked_window"], delta=0.11)

    def test_working_run(self):
        w = self.s["runs"][pace.WORKING]
        self.assertAlmostEqual(w["window"], 227.3, delta=0.05)
        self.assertAlmostEqual(w["fy2030_33"], 55.7, delta=0.05)
        self.assertAlmostEqual(w["short_of_booked"], 51.9, delta=0.05)
        self.assertAlmostEqual(w["outlay_effect"], 16.6, delta=0.05)
        self.assertAlmostEqual(w["outlay_effect_part_g_own_path"], 19.6, delta=0.05)
        self.assertAlmostEqual(w["outlay_effect_no_ramp"], 39.3, delta=0.05)
        self.assertAlmostEqual(w["irs_outlay_effect"], 6.3, delta=0.05)
        self.assertEqual(w["g8_lag"], {"0": 14.0, "1": 16.1, "2": 18.9})
        self.assertAlmostEqual(w["net_deficit_change"], -0.4, delta=0.05)

    def test_d4_ranges(self):
        d = self.s["d4"]
        self.assertEqual(d["outlay_range"], (7.0, 36.0))
        self.assertEqual(d["g8_lag_range"], (7.7, 28.9))
        self.assertEqual(d["net_range"], (-11.2, 3.1))
        self.assertEqual(d["own_path_range"], (9.4, 40.5))
        self.assertEqual(d["no_ramp_range"], (29.7, 58.7))
        self.assertAlmostEqual(d["superseded_draft_figure"], 22.2, delta=0.05)

    def test_paced_window_range(self):
        windows = [v["window"] for v in self.s["runs"].values()]
        self.assertEqual((min(windows), max(windows)), (207.9, 236.9))
        early = [v["fy2030_33"] for v in self.s["runs"].values()]
        self.assertEqual((min(early), max(early)), (38.9, 65.2))
        short = [v["short_of_booked"] for v in self.s["runs"].values()]
        self.assertEqual((min(short), max(short)), (42.3, 71.3))

    def test_one_basis_identity(self):
        # On the booking's basis the paced allocation plus the pace effect is the allocation on the booked ramp,
        # and the pace effect plus the contingency is what the booking does not spend.
        for k, v in self.s["runs"].items():
            with self.subTest(run=k):
                self.assertAlmostEqual(v["window"] + v["outlay_effect"], self.s["allocation_on_booked_ramp_window"],
                                       delta=0.11)
                self.assertAlmostEqual(v["outlay_effect"] + self.s["contingency_on_booked_ramp_window"],
                                       v["short_of_booked"], delta=0.11)

    def test_fy2040_unchanged(self):
        for k, v in self.s["runs"].items():
            with self.subTest(run=k):
                self.assertAlmostEqual(v["fy2040_change"], 0.0, places=6)
                self.assertAlmostEqual(v["path"][2040], pace.ALLOC_2040, delta=0.005)

    def test_irs_yield_lag_exceeds_irs_outlay_saving(self):
        # 6-cost.md part 1.3: for the IRS, a slow path delays the yield more than it saves outlays.
        for k, v in self.s["runs"].items():
            with self.subTest(run=k):
                self.assertGreater(v["g8_lag"]["1"], v["irs_outlay_effect"])

    def test_g8_lag_zero_when_pace_matches_booking(self):
        # If staff came on as fast as the booked ramp assumes, no yield would be lost.
        self.assertAlmostEqual(self.s["g8_net_booked_window"], 150.0, delta=0.05)
        self.assertLess(pace.g8_lag(0.5, 1), 1.0)

    def test_hiring(self):
        h = self.s["hiring"]
        self.assertEqual(h["a quarter a year (working)"]["net_added_a_year_six_agencies"], 13500)
        self.assertEqual(h["a fifth a year"]["net_added_a_year_six_agencies"], 10800)
        self.assertEqual(h["a third a year"]["net_added_a_year_six_agencies"], 18000)
        self.assertEqual(h["a quarter a year (working)"]["irs_net_added_a_year"], 7500)

    def test_self_check_passes(self):
        pace.check()


if __name__ == "__main__":
    unittest.main(verbosity=1)
