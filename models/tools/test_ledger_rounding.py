"""Regression checks for decimal headline precision and the unchanged revenue inputs."""
import unittest
from inputs import money_sum, read


class LedgerPrecision(unittest.TestCase):
    def test_decimal_boundaries(self):
        self.assertEqual(money_sum([5.98, .005]), 5.99)
        self.assertEqual(money_sum([-5.98, -.005]), -5.99)
        self.assertEqual(money_sum([.1, .2, -.3]), 0)

    def test_input_order_does_not_change_headline(self):
        rows = [r for r in read('ledger-revenue.csv')
                if r['in_base'].lower() == 'yes' and r['channel'] == 'General fund' and r['id'] != 'CXP']
        # MR6's figure comes from the transportation model (model:MR6, -0.1253 trillion, each act's window:
        # JCT's 24.4% of $513.4B gross; -0.1283 at 25% until DEC-2026-11-12-08).
        self.assertEqual([r['id'] for r in rows if r['mid'].startswith('model:')], ['MR6'])
        values = [r['mid'] if r['id'] != 'MR6' else -0.1253 for r in rows]
        # 5.99 until Oct 26; the $150-by-2037 carbon price (Espen, Oct 26) raises the CX offset from -0.38 to -0.49;
        # 5.88 until MR6, Moving America's 25% offset, was booked on the general fund as CX (transportation review F-1);
        # 5.75 until HX, the health plan's exclusion revenue ($5.22T), was booked (care review F-4);
        # 10.97 until part 6's federal-coverage correction took HX to $4.84T (budget B6 item 7);
        # 10.58 until the CX and MR6 offsets took JCT's 24.4% rate in place of 25% (DEC-2026-11-12-08);
        # 10.6 until the immigration booking added E-Verify's on-budget revenue (IMM-EV, +0.0233) and the H-1B
        # fee's tax offset (IF1T, -0.0037) as base-revenue rows (immigration review step 5)
        self.assertEqual(money_sum(values), 10.62)
        self.assertEqual(money_sum(reversed(values)), 10.62)


if __name__ == '__main__':
    unittest.main()
