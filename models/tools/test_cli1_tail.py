#!/usr/bin/env python3
"""Tests for `cli1_tail.py` (stage G step 9): the clean-energy credits' cost after FY2039 against the decided
step-down (CLI-1A.02). Run after the common rebuild (run-all.sh step 8c3).

Checks: the energy model's decided path ends by FY2047 and matches its committed FY2040 figure; the corrected path
keeps the booked window, falls every year after FY2041 and is zero from FY2047; the what-if moves no year before
FY2040 and lowers the gap by exactly the CLI-1 saving in FY2040; the fiscal-after.csv row the correction needs gives
the corrected path once the climate export's delta is added; and the committed note equals what the code writes.
"""
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'models/tools'))
import cli1_tail as T   # noqa: E402

D = T.build()


class Cli1Tail(unittest.TestCase):
    def test_energy_path(self):
        res = json.loads((ROOT / 'models/tools/energy/results.json').read_text())['scenarios']['decided']
        self.assertAlmostEqual(T.ENERGY_DECIDED[2040], res['fy2040']['credits'], delta=0.05)
        self.assertAlmostEqual(sum(T.ENERGY_DECIDED[y] for y in range(2030, 2040)), res['window_2030_39']['credits'], delta=0.5)
        self.assertTrue(all(T.ENERGY_DECIDED[y] == 0 for y in range(2047, 2051)))

    def test_corrected_path(self):
        p0, p1 = D['booked'], D['fixed']
        for y in range(2026, 2040):
            self.assertAlmostEqual(p0[y], p1[y], places=6)
        for y in range(2042, 2047):
            self.assertLess(p1[y], p1[y - 1])
        for y in range(2047, 2057):
            self.assertAlmostEqual(p1[y], 0.0, places=6)

    def test_what_if_moves_only_the_tail(self):
        r0, r1 = D['r0'], D['r1']
        for y in range(2026, 2040):
            self.assertAlmostEqual(r0[y]['agenda_gf_primary_bn'], r1[y]['agenda_gf_primary_bn'], places=6)
        saving = D['booked'][2040] - D['fixed'][2040]
        self.assertAlmostEqual(r0[2040]['agenda_gf_primary_bn'] - r1[2040]['agenda_gf_primary_bn'], saving, places=3)
        self.assertLess(r1[2056]['debt_gdp'], r0[2056]['debt_gdp'])

    def test_after_row_reproduces_the_path(self):
        if D["is_booked"]:   # the committed fiscal-after.csv row is the one this tool computes
            row = D['f'].PR.AFTER['CLI-1']
            for y in T.AFTER_YEARS:
                self.assertAlmostEqual(row[y], D['after'][y], places=2)
        tgt = T.corrected(D['booked'])
        for y in T.AFTER_YEARS:
            self.assertAlmostEqual(D['after'][y] + D['delta'][y], tgt[y], delta=0.01)

    def test_note_current(self):
        self.assertEqual(T.OUT.read_text(), T.markdown(D))


if __name__ == '__main__':
    unittest.main()
