"""Every decided revenue source is booked (DEC-2026-11-28-01). Cheap: reads the decision log and the booked inputs only.

Role: the booking principle's guard. Status: current. Espen, November 28: "all revenues being raised under the plan's
decisions, at any given time, are being booked correctly". `models/data/inputs/decided-revenue.csv` names, for each
stage G decision that raises, cuts or rules on revenue, where it is booked (settlement items, switches or the health
contribution's rate) or why it books nothing (a rule, a goal, a contingent backstop, superseded). The test fails when:
  * a decision from stage G on (dated 2026-11-20 or later) whose headline names a tax, fee, levy, contribution, VAT,
    surtax or revenue is not in the register (classify it, and book it if it raises money);
  * a register row says booked but its settlement item is missing from settlement-paths.csv or books nothing, or its
    switch or the health contribution's rate is missing from settlement.json;
  * a settlement item on the revenue side, or one booked from fiscal_revision.py, is named by no booked row.
Earlier decisions are booked through the ledger's rows (ledger-revenue.csv), which the ledger checks already cover.
Run: python3 models/bookings/test_decided_revenue.py
"""
import csv
import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
INPUTS = ROOT / 'models/data/inputs'
FROM = '2026-11-20'
KEYWORDS = re.compile(r'\b(VAT|surtax|tax|taxes|fee|fees|revenue|contribution|levy)\b', re.I)
STATUSES = {'booked', 'contingent', 'not_a_source', 'superseded'}


def decisions():
    out = {}
    for line in (ROOT / 'charter/decisions.md').read_text().splitlines():
        if line.startswith('| DEC-'):
            c = line.split('|')
            out[c[1].strip()] = (c[2].strip(), c[3].split('Espen')[0])
    return out


class DecidedRevenue(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.dec = decisions()
        with (INPUTS / 'decided-revenue.csv').open(newline='') as fh:
            cls.reg = {r['dec']: r for r in csv.DictReader(fh)}
        cls.doc = json.loads((INPUTS / 'settlement.json').read_text())
        with (INPUTS / 'settlement-paths.csv').open(newline='') as fh:
            cls.paths = {r['id']: max(abs(float(v)) for k, v in r.items() if k.startswith('y')) for r in csv.DictReader(fh)}

    def test_register_rows_are_decisions(self):
        for d, r in self.reg.items():
            self.assertIn(d, self.dec, d)
            self.assertIn(r['status'], STATUSES, d)
            self.assertEqual(bool(r['booked_as']), r['status'] == 'booked', d)

    def test_every_revenue_decision_is_classified(self):
        missing = [d for d, (date, head) in self.dec.items() if date >= FROM and KEYWORDS.search(head) and d not in self.reg]
        self.assertEqual(missing, [], 'decided revenue sources not in decided-revenue.csv (book or classify them)')

    def test_booked_rows_are_booked(self):
        for d, r in self.reg.items():
            for b in filter(None, r['booked_as'].split(';')):
                if b.startswith('switch:'):
                    self.assertIn(b[7:], self.doc['switches'], (d, b))
                elif b == 'health_contribution_base_rate':
                    self.assertIn('path', self.doc[b], d)
                else:
                    self.assertIn(b, self.paths, (d, b))
                    self.assertGreater(self.paths[b], 0.05, (d, b))   # it books money in some year

    def test_revenue_items_are_registered(self):
        named = {b for r in self.reg.values() for b in r['booked_as'].split(';')}
        for it in self.doc['items']:
            if (it['side'] == 'revenue' and it['dec'].startswith('DEC-')) or it.get('from') == 'fiscal_revision':
                self.assertIn(it['id'], named, it['id'])


if __name__ == '__main__':
    unittest.main()
