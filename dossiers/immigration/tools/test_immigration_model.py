#!/usr/bin/env python3
"""Tests for the immigration model and section 6's path.

Run from the repository root: python3 dossiers/immigration/tools/test_immigration_model.py
Checks that every input traces to the register or is a labeled assumption with a range, that
each module behaves as its design says, and that section 6 reports the tool's figures.
"""
import json
import os
import re
import sys
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
sys.path.insert(0, HERE)
import immigration_model as m  # noqa: E402
import immigration_path as p   # noqa: E402


def register_ids():
    ids = set()
    for dirpath, _, files in os.walk(os.path.join(ROOT, 'dossiers')):
        if 'evidence.json' in files:
            ids |= {e['id'] for e in json.load(open(os.path.join(dirpath, 'evidence.json')))}
    return ids


class Inputs(unittest.TestCase):
    def test_every_input_traces(self):
        known = register_ids()
        for name, (c, lo, hi, basis) in m.INPUTS.items():
            cited = re.findall(r'EV-[A-Z]{2,4}-\d{3}', basis)
            labeled = basis.startswith(('assumption', 'legacy estimate', 'commitment'))
            self.assertTrue(cited or labeled, f'{name}: no evidence ID and no label')
            for ev in cited:
                self.assertIn(ev, known, f'{name}: {ev} is not in a register')
            if lo is not None:
                self.assertTrue(lo <= c <= hi, f'{name}: central outside its range')
            if basis.startswith('assumption') and lo is not None and not isinstance(c, tuple):
                self.assertTrue(lo < hi or name in ('clear_years',), f'{name}: an assumption needs a range')

    def test_filing_shape_sums_to_one(self):
        self.assertAlmostEqual(sum(m.INPUTS['filing_shape'][0]), 1.0, places=6)


class Modules(unittest.TestCase):
    def test_uscis_volume_matches_memo_1(self):
        self.assertTrue(8.0 <= m.uscis()['filings_m'] <= 10.0)   # memo 7: 8-10 million filings

    def test_courts_need_more_judges_when_slower(self):
        slow, fast = m.eoir('low'), m.eoir('high')
        self.assertGreater(slow['judges_needed'], fast['judges_needed'])
        central = m.eoir()
        self.assertGreater(central['judges_added'], 300)            # CRS and MI: several hundred more
        self.assertLessEqual(central['cleared_fy'], 2035)            # memo 4: about six years
        self.assertTrue(central['cleared_at_800'] is None or central['cleared_at_800'] > 2035)
        self.assertGreater(central['cleared_slow_ramp'], central['cleared_fy'])

    def test_detention_near_zero(self):
        self.assertLess(abs(m.window(m.detention())), 10)        # memo 5: about zero net

    def test_status_is_a_cost_bounded_by_section_3(self):
        total = m.window(m.status_fiscal())
        self.assertTrue(0 < total < 150)                           # 3-design.md: +0.05T, -0.05 to +0.15T

    def test_counsel_inside_memo_4(self):
        self.assertTrue(4 <= m.window(m.eoir()['counsel']) <= 14)  # memo 4: counsel B $6-12B, judgment


class SectionSix(unittest.TestCase):
    def test_section_6_reports_the_tool(self):
        spend, rev = p.lines(), p.revenue_lines()
        t = p.total({**spend, **rev})[0]
        window, y2040 = sum(t[y] for y in p.WINDOW), t[2040]
        text = open(os.path.join(ROOT, 'dossiers/immigration/6-cost.md')).read()
        row = next(line for line in text.splitlines() if line.startswith('| **Immigration on the general fund, all**'))
        self.assertIn(f'**{window:.1f}**', row)
        self.assertIn(f'**{y2040:.1f}**', row)


if __name__ == '__main__':
    unittest.main()
