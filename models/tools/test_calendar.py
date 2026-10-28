"""Regression checks for approved timing and protected capacity, not dated feasibility."""
import csv
import importlib.util
import json
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'index/tools'))
spec = importlib.util.spec_from_file_location('votes_model', ROOT / 'index/tools/votes-model.py')
votes = importlib.util.module_from_spec(spec)
spec.loader.exec_module(votes)

class CalendarChecks(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.ledger = json.loads((ROOT / 'build/ledger.json').read_text())
        with (ROOT / 'index/data/inputs/ledger-bills.csv').open() as stream:
            cls.rows = {r['id']: r for r in csv.DictReader(stream)}

    def test_dem_floor_start_and_ss_window(self):
        self.assertEqual(self.rows['DEM-1']['target'], '2029-03')
        self.assertEqual(self.rows['SS-1']['target'], '2030-spring')

    def test_reconciliation_windows(self):
        for r in self.rows.values():
            if r['rail'] in ('R1', 'R2', 'R3'):
                self.assertEqual(r['target'], {'R1':'2029-02','R2':'2029-summer','R3':'2030-summer'}[r['rail']])

    def test_protected_items_fit_before_discretionary_allocation(self):
        fit = votes.calendar(self.ledger, {})['F']
        self.assertTrue(fit['DEM-1'])
        self.assertTrue(fit['SS-1'])
        self.assertEqual(len(fit), 21)
        self.assertNotIn('MOV-31', fit)

    def test_protection_does_not_create_capacity(self):
        fit = votes.calendar(self.ledger, {})['F']
        fast = {'INT-1','CAP-8','LAB-9D'}
        used = sum((b['floor_days'] if b['id'] in fast else max(b['floor_days'],4.5))
                   for b in self.ledger['bills'] if fit.get(b['id'], False))
        self.assertLessEqual(used + self.ledger['summary']['recon_days'] + 4, votes.BUDGET)
        self.assertFalse(all(fit.values()))

    def test_mov_stays_second_congress(self):
        self.assertEqual(self.rows['MOV-31']['rail'], 'LATER')
        self.assertTrue(self.rows['MOV-31']['target'].startswith('2031-'))

    def test_legislative_windows_do_not_assert_household_receipt(self):
        for b in self.ledger['bills']:
            if b['rail'] in ('R1','R2','R3') or b['id'] in ('DEM-1','SS-1'):
                self.assertEqual(b['felt_by_midterm'], 'Unverified')

if __name__ == '__main__':
    unittest.main()
