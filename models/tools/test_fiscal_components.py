"""Protect component ownership, calibration and permanent voucher spending."""
import importlib.util
from pathlib import Path
import sys
import unittest

HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE))
spec=importlib.util.spec_from_file_location('component_fiscal',HERE/'fiscal-model.py')
fiscal=importlib.util.module_from_spec(spec);spec.loader.exec_module(fiscal)

class ComponentTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.base=fiscal.read_baseline(HERE.parent/'data/fiscal-baseline.csv')

    def test_total_is_ledger_cost_not_an_additional_claim(self):
        path=fiscal.row_path(self.base,.56,fiscal.PR.BILLS['HOU-1'],'HOU-1')
        self.assertAlmostEqual(sum(path[y] for y in range(2030,2040)),560)

    def test_full_voucher_increment_survives_2040(self):
        parts=fiscal.PR.COMPONENTS['HOU-1']
        base=fiscal.row_path(self.base,parts[0][1],parts[0][2])
        extra=fiscal.row_path(self.base,parts[1][1],parts[1][2])
        total=fiscal.row_path(self.base,.56,fiscal.PR.BILLS['HOU-1'],'HOU-1')
        self.assertAlmostEqual(total[2040]-base[2040],extra[2040])
        self.assertGreater(extra[2040],extra[2039])
        self.assertEqual(parts[1][2]['perm'],1)
        self.assertEqual(parts[1][2]['ramp'],4)

    def test_mismatched_component_allocation_fails(self):
        with self.assertRaises(ValueError):
            fiscal.row_path(self.base,.47,fiscal.PR.BILLS['HOU-1'],'HOU-1')

if __name__=='__main__':unittest.main()
