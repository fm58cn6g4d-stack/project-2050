#!/usr/bin/env python3
"""Tests for the reserved-block rules of library/build_catalog.py (no Git or catalog needed)."""
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import build_catalog as bc

BLOCKS = [('a', 3000, 3399), ('b', 4000, 4399)]


class ReservedBlocks(unittest.TestCase):
    def test_next_number_when_clear(self):
        self.assertEqual(bc.next_free(100, BLOCKS), 101)

    def test_number_before_a_block_skips_it(self):
        self.assertEqual(bc.next_free(3999, BLOCKS), 4400)

    def test_inside_a_block_skips_to_the_end(self):
        self.assertEqual(bc.next_free(4391, BLOCKS), 4400)
        self.assertEqual(bc.next_free(2999, BLOCKS), 3400)

    def test_free_gap_is_used(self):
        self.assertEqual(bc.next_free(3500, BLOCKS), 3501)

    def test_adjacent_blocks_chain(self):
        self.assertEqual(bc.next_free(3999, [('a', 4000, 4099), ('b', 4100, 4199)]), 4200)

    def test_no_blocks(self):
        self.assertEqual(bc.next_free(10, []), 11)

    def test_declared_file_is_valid(self):
        blocks = bc.reserved_blocks()
        self.assertTrue(blocks)
        self.assertEqual(bc.block_problems(blocks), [])

    def test_problems_found(self):
        self.assertTrue(bc.block_problems([('a', 5, 1)]))
        self.assertTrue(bc.block_problems([('a', 1, 10), ('b', 10, 20)]))

    def test_catalog_numbering_skips_blocks(self):
        # the real catalog's highest ID sits inside a reserved block; a new file must not be numbered there
        top = max(int(r['id'][4:]) for r in bc.load(bc.CATALOG, bc.COLUMNS))
        new = bc.next_free(top, bc.reserved_blocks())
        self.assertFalse(any(a <= new <= b for _, a, b in bc.reserved_blocks()))
        self.assertGreater(new, top)


if __name__ == '__main__':
    unittest.main()
