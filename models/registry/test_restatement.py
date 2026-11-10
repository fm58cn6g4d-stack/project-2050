"""Tests for the restatement check on a small artificial tree."""
import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import restatement  # noqa: E402

SOURCE = """# Old design
Decision A-23 sets $55.00B over FY2032-36 for MR1, see [link](https://example.com/2031/report-99).
The rate is 3 cents, 1,000 trucks, and 0.180% of GDP.
Dropped: the 91,000-lb pilot.
"""


class RestatementTests(unittest.TestCase):
    def tree(self, result, log=''):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        root = Path(tmp.name)
        (root / 'agenda').mkdir()
        (root / 'agenda/agenda.csv').write_text('id,name,home_dossier,level,status,source,note\nMR1,Fuel,x,L1,chosen,,\n')
        (root / 'legacy').mkdir()
        (root / 'legacy/old.md').write_text(SOURCE)
        (root / 'd').mkdir()
        (root / 'd/1.md').write_text(result)
        (root / 'd/log.md').write_text(log)
        return root

    def missing(self, root, accounted=()):
        r = restatement.compare(root, 'legacy/old.md', restatement.expand(root, ['d/1.md']),
                                restatement.expand(root, list(accounted)))
        return {m['token'] for m in r['missing']}, {m['token'] for m in r['accounted']}

    def test_full_restatement_has_nothing_missing(self):
        root = self.tree('A-23: $55B over FY2032-36 for MR1. 3 cents, 1000 trucks, 0.18% of GDP. 91,000 lb.')
        self.assertEqual(self.missing(root), (set(), set()))

    def test_dropped_numbers_and_ids_are_listed(self):
        root = self.tree('$55B over FY2032-36. 3 cents. 0.18%.')
        missing, _ = self.missing(root)
        self.assertEqual(missing, {'A-23', 'MR1', '1000', '91000'})

    def test_numbers_in_ids_and_urls_are_ignored(self):
        root = self.tree('A-23 $55B FY2032-36 MR1 3 1000 0.18 91000')
        missing, _ = self.missing(root)
        self.assertNotIn('99', missing)
        self.assertNotIn('23', missing)

    def test_backticked_tokens_in_the_log_count_as_accounted(self):
        root = self.tree('A-23 $55B FY2032-36 MR1 3 1000 0.18', log='- `91,000` the pilot ends; DEC-x. 1000 stray')
        missing, accounted = self.missing(root, ['d/log.md'])
        self.assertEqual((missing, accounted), (set(), {'91000'}))

    def test_a_stray_match_in_the_log_does_not_count(self):
        root = self.tree('A-23 $55B FY2032-36 MR1 3 1000 0.18', log='the 91,000-lb pilot ends')
        self.assertEqual(self.missing(root, ['d/log.md'])[0], {'91000'})

    def test_map_runs_every_pair(self):
        root = self.tree('A-23 $55B FY2032-36 MR1 3 1000 0.18 91000')
        (root / 'd/restatement.json').write_text(json.dumps(
            {'pairs': [{'source': 'legacy/old.md', 'result': ['d/1.md'], 'accounted': []}]}))
        reports = restatement.run_map(root, 'd/restatement.json', limit=None)
        self.assertEqual(len(reports), 1)
        self.assertEqual(reports[0]['missing'], [])

    def test_map_and_log_are_not_results(self):
        # A wide result glob also matches the map and the log; neither may make a token read as carried over.
        root = self.tree('A-23 $55B FY2032-36 MR1 3 1000 0.18', log='- `91,000` the pilot ends')
        (root / 'd/restatement.json').write_text(json.dumps(
            {'note': 'mentions A-23 and 91,000', 'pairs': [{'source': 'legacy/old.md', 'result': ['d/*'],
                                                        'accounted': ['d/log.md']}]}))
        r = restatement.run_map(root, 'd/restatement.json', limit=None)[0]
        self.assertEqual(r['results'], ['d/1.md'])
        self.assertEqual(([m['token'] for m in r['missing']], [m['token'] for m in r['accounted']]), ([], ['91000']))

    def test_leading_zeros_are_ignored(self):
        self.assertEqual([restatement.norm(n) for n in ('07', '0.50', '007.10', '0')], ['7', '0.5', '7.1', '0'])


if __name__ == '__main__':
    unittest.main()
