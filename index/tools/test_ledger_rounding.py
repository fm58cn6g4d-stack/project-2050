"""Regression checks for decimal headline precision and the unchanged revenue inputs."""
import unittest
from inputs import money_sum, read


class LedgerPrecision(unittest.TestCase):
    def test_decimal_boundaries(self):
        self.assertEqual(money_sum([5.98, .005]), 5.99)
        self.assertEqual(money_sum([-5.98, -.005]), -5.99)
        self.assertEqual(money_sum([.1, .2, -.3]), 0)

    def test_input_order_does_not_change_headline(self):
        values = [r['mid'] for r in read('ledger-revenue.csv')
                  if r['in_base'].lower() == 'yes' and r['channel'] == 'General fund']
        self.assertEqual(money_sum(values), 5.99)
        self.assertEqual(money_sum(reversed(values)), 5.99)


if __name__ == '__main__':
    unittest.main()
