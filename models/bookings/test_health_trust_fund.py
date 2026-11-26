"""The health fund's account note matches what the code builds from the booked case (stage G step 11).

Role: guards `dossiers/foundations/fair-financing/notes/health-trust-fund-results.md` against going stale: the note went
out of date once already, when #493 changed the booked case and nothing re-ran `health_trust_fund.py`. Run by
run-all.sh after the recovery budget (it reads build/); standard library only. Checks that:
- the committed note equals `health_trust_fund.markdown(health_trust_fund.run())` on the current build;
- the account's FY2030-34 surplus that reaches the general fund's figures is the one the booked health fund holds
  (`DEC-2026-11-25-31` point 2: $250B standing, the rest drawn in FY2035), so the note and the booking read one account.
"""
import importlib.util
import os
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


HT = load('health_trust_fund', HERE / 'health_trust_fund.py')


class HealthFundNote(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.r = HT.run()

    def test_note_is_current(self):
        self.assertEqual(HT.NOTE.read_text(), HT.markdown(self.r),
                         'the note is stale: run python3 models/bookings/health_trust_fund.py --write')

    def test_reserve_is_the_booked_funds(self):
        built, draw = self.r['reserve']
        fund = self.r['fund']
        self.assertAlmostEqual(built, fund['built_2030_34'], places=6)
        self.assertAlmostEqual(sum(draw.values()), fund['drawn'], places=6)
        self.assertAlmostEqual(built - sum(draw.values()), fund['standing'], places=6)


if __name__ == '__main__':
    unittest.main(verbosity=1)
