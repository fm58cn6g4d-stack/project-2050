"""Checks on stage G's financing settlement as booked (step 7; `models/data/inputs/settlement.json`).

Role: the booking's guard, as `test_fiscal_health.py` is health's. Status: current. Run after the common rebuild:
    python3 models/tools/test_settlement_booking.py
It checks that the committed paths and D3 rows equal `settlement_booking.py`'s derivation; that the budget model's
booked case equals the same package priced the screens' way; that it closes FY2040 and every later year to FY2056 on
the general fund at the booked base rate and not 0.05 points below it; that every DEC- row the booking names exists;
and that the duty to house's HOU-1 component is gone (G14 C).
"""
import csv
import json
import unittest
from pathlib import Path

import settlement_booking as SB

ROOT = Path(__file__).resolve().parents[2]
INPUTS = ROOT / 'models/data/inputs'


class SettlementBooking(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.ctx = SB.K.Context()
        cls.doc = SB.doc()
        cls.der = SB.derive(cls.ctx, cls.doc)
        cls.booked = SB.gap(SB.booked_case(cls.ctx))

    def test_paths_are_the_derivation(self):
        committed = {r['id']: r for r in csv.DictReader((INPUTS / 'settlement-paths.csv').open(newline=''))}
        self.assertEqual(set(committed), {it['id'] for it in self.doc['items']})
        for it, o, p in self.der:
            for y in SB.YEARS:
                self.assertAlmostEqual(float(committed[it['id']]['y%d' % y]), p[y], delta=0.0006, msg=(it['id'], y))

    def test_d3_rows_are_the_derivation(self):
        rows = {r['id']: r for r in csv.DictReader((INPUTS / 'incidence-rows.csv').open(newline=''))}
        for rid, amt in SB.d3_amounts(self.der).items():
            self.assertAlmostEqual(float(rows[rid]['amount']), amt, delta=0.0006, msg=rid)
        q = next(s for s in json.loads((INPUTS / 'scenarios.json').read_text())['incidence'] if s['id'] == 'Q-G')
        self.assertNotIn('ICB', q['options'])
        self.assertEqual(set(q['replace'].values()) | {'GXg'}, set(SB.D3_ROWS))

    def test_booked_equals_screened(self):
        screened = SB.gap(SB.screened_case(self.ctx, self.doc, self.doc['health_contribution_base_rate']['rate']))
        for y in range(2030, 2057):
            self.assertAlmostEqual(self.booked[y], screened[y], delta=0.05, msg=y)

    def test_closes_2040_on_at_the_lowest_rate(self):
        rate = self.doc['health_contribution_base_rate']['rate']
        self.assertTrue(all(self.booked[y] <= 0.05 for y in range(2040, 2057)))
        lower = SB.gap(SB.screened_case(self.ctx, self.doc, round(rate - 0.05, 2)))
        self.assertFalse(all(lower[y] <= 0.05 for y in range(2040, 2057)))

    def test_decisions_named_exist(self):
        text = (ROOT / 'charter/decisions.md').read_text()
        import re
        ids = set(re.findall(r'DEC-\d{4}-\d{2}-\d{2}-\d{2}', json.dumps(self.doc)))
        self.assertTrue(ids)
        for d in ids:
            self.assertIn('| %s |' % d, text, d)

    def test_duty_to_house_removed(self):
        comps = list(csv.DictReader((INPUTS / 'fiscal-components.csv').open(newline='')))
        self.assertFalse(any(r['component'] == 'hou-4d-01-duty-to-house' for r in comps))
        hou = [float(r['mid10']) for r in comps if r['owner'] == 'HOU-1']
        mid = next(float(r['cost_mid']) for r in csv.DictReader((INPUTS / 'ledger-bills.csv').open(newline='')) if r['id'] == 'HOU-1')
        self.assertAlmostEqual(sum(hou), mid, places=9)


if __name__ == '__main__':
    unittest.main()
