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
        self.assertEqual(set(q['replace'].values()) | {'GXg', 'OUTg', 'DEDg', 'VATg', 'VATRg'}, set(SB.D3_ROWS))
        # G24 B's rows (DEC-2026-11-28-01): in Q-G, each on its own booked FY2030-39 profile, the rebate on G30's key
        rev = SB.revision_d3(self.der)
        self.assertEqual(set(rev), {'OUTg', 'DEDg', 'VATg', 'VATRg'})
        self.assertTrue(set(rev) <= set(q['options']))
        prof = {r['id']: r for r in csv.DictReader((INPUTS / 'incidence-phase-in.csv').open(newline=''))}
        for rid, (side, amt, key, label, path, src) in rev.items():
            self.assertEqual((rows[rid]['side'], rows[rid]['parts']), (side, key), rid)
            top = max(path.values())
            for y in range(2030, 2040):
                self.assertAlmostEqual(float(prof[rid]['y%d' % y]), path[y] / top, delta=0.0006, msg=(rid, y))
        self.assertEqual([prof['VATg']['y%d' % y] for y in range(2030, 2035)], ['0'] * 5)   # the VAT from FY2035 (G24.2)
        key = next(r for r in csv.DictReader((INPUTS / 'incidence-keys.csv').open(newline='')) if r['key'] == 'vat_rebate')
        sh, t1 = SB.rebate_key()
        self.assertEqual([float(key[q_]) for q_ in ('q1', 'q2', 'q3', 'q4', 'q5')] + [float(key['top1'])], sh + [t1])

    def test_booked_equals_screened(self):
        hr = self.doc['health_contribution_base_rate']
        screened = SB.gap(SB.screened_case(self.ctx, self.doc, hr['rate'], hr['path']))
        # the screens have no health fund: compare the general fund with the fund's own balance after its transfer
        # put back (DEC-2026-11-25-28 moves health money between the accounts, not out of the budget)
        # and HX's OASDI part, which G29 A sends to Social Security's funds from FY2031 (current law), put back too (off-budget)
        case = SB.booked_case(self.ctx)
        fund = case['health_fund']
        ssp = SB.K.m.social_security_part(case['audit'], self.doc['health_fund'])
        self.assertEqual(min(ssp), 2031)
        for y in range(2030, 2057):
            own = fund[y]['spending'] - fund[y]['sources'] - fund[y]['transfer']
            self.assertAlmostEqual(self.booked[y] + own - ssp.get(y, 0.0), screened[y], delta=0.05, msg=y)

    def test_health_fund_rule(self):
        # G27 A as booked: the share and the rate path are the rule's on the booked case; the steps are quarter points,
        # at most one a year, never below 3.25%; FY2040 stays at 3.80% (G26 A); FY2030-34's surplus stays in the fund
        hr, hf = self.doc['health_contribution_base_rate'], self.doc['health_fund']
        rule = SB.rate_rule(self.ctx, self.doc)
        self.assertAlmostEqual(hf['contribution_share'], rule['share'], places=6)
        self.assertEqual({int(k): v for k, v in hr['path'].items()}, rule['path'])
        prev = hr['rate']
        for y in range(2041, 2057):
            r = hr['path'][str(y)]
            self.assertIn(round(abs(r - prev), 2), (0.0, 0.25), y)
            self.assertGreaterEqual(r, hf['floor'])
            prev = r
        fund = SB.booked_case(self.ctx)['health_fund']
        self.assertEqual([fund[y]['transfer'] for y in range(2030, 2035)], [0.0] * 5)
        built = sum(fund[y]['balance'] for y in range(2030, 2035))
        keep = built if hf['standing_reserve_bn'] is None else hf['standing_reserve_bn']   # None: as built
        self.assertEqual(hf['standing_reserve_bn'], 250)   # G29 R2 (DEC-2026-11-26-03): $250B standing, the rest drawn in FY2035
        self.assertGreater(built, keep)
        self.assertAlmostEqual(fund[2039]['reserve'], keep, places=6)
        # G29: OASDI's part is 0.28 of HX and of HEX alike (sourced, EV-FIN-094, -095), out of the fund's sources
        self.assertEqual(hf['source_shares'], {'HX': 0.72, 'HEX': 0.72})
        self.assertEqual(hf['social_security_part']['from'], 2031)   # G29 A: Social Security's from HX's first year, as current law

    def test_closes_2040_on_at_g16b_rate(self):
        rate = self.doc['health_contribution_base_rate']['rate']
        # G29.1 option 1 (DEC-2026-11-28-01): with G24 B's sources and PH-3 booked (S12-S17), the general fund closes in
        # FY2035 and every year from FY2039; FY2036-38 stay short (the VAT's first years, before the deduction limits and
        # the surtax are whole). Without them (G29 A alone, DEC-2026-11-26-03) it was short in FY2040-44, closing from
        # FY2045; before HX's OASDI part it closed every year from FY2040. The health contribution can't fill the gap
        # (DEC-2026-11-25-12).
        ssp = SB.K.m.social_security_part(SB.booked_case(self.ctx)['audit'], self.doc['health_fund'])
        self.assertLessEqual(self.booked[2035], 0.05)
        self.assertTrue(all(self.booked[y] > 0.05 for y in range(2036, 2039)))
        self.assertTrue(all(self.booked[y] <= 0.05 for y in range(2039, 2057)))
        with SB.K.m.without_items(SB.K.m.revision_items()):
            alone = SB.gap(SB.booked_case(self.ctx))
        self.assertEqual(sorted(SB.K.m.revision_items()), ['S12', 'S13', 'S14', 'S15', 'S16', 'S17'])
        self.assertTrue(all(alone[y] <= 0.05 for y in range(2045, 2057)))
        self.assertTrue(all(alone[y] > 0 for y in range(2040, 2045)))
        self.assertTrue(all(alone[y] - ssp[y] <= 0.05 for y in range(2040, 2057)))
        # The rate's own check, on the settlement before G24 B and PH-3 (step 7's package): with them the general fund has
        # room to spare, which goes to the debt path (G23 B), not to a lower rate (DEC-2026-11-25-12)
        d = dict(self.doc, items=[it for it in self.doc['items'] if it.get('from') != 'fiscal_revision'])
        lower = SB.gap(SB.screened_case(self.ctx, d, round(rate - 0.05, 2)))
        # Booked as the lowest closing rate in step 7; G16 B (DEC-2026-11-25-02) then held it at 3.80% to FY2040. Since
        # CLI-1's step-down was booked (memo G25), 3.75% also closes; the room goes to the debt path, not a lower rate.
        self.assertEqual(rate, 3.80)
        lower2 = SB.gap(SB.screened_case(self.ctx, d, round(rate - 0.10, 2)))
        self.assertTrue(all(lower[y] <= 0.05 for y in range(2040, 2057)))
        self.assertFalse(all(lower2[y] <= 0.05 for y in range(2040, 2057)))

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
