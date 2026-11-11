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
        # MR6's figure comes from the transportation model (model:MR6, -0.1283 trillion, each act's window).
        self.assertEqual([r['id'] for r in rows if r['mid'].startswith('model:')], ['MR6'])
        values = [r['mid'] if r['id'] != 'MR6' else -0.1283 for r in rows]
        # 5.99 until Oct 26; the $150-by-2037 carbon price (Espen, Oct 26) raises the CX offset from -0.38 to -0.49;
        # 5.88 until MR6, Moving America's 25% offset, was booked on the general fund as CX (transportation review F-1);
        # 5.75 until HX, the health plan's exclusion revenue ($5.22T), was booked (care review F-4)
        self.assertEqual(money_sum(values), 10.97)
        self.assertEqual(money_sum(reversed(values)), 10.97)


if __name__ == '__main__':
    unittest.main()
