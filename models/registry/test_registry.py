"""Regression tests for the registry checker on a small artificial tree."""
import datetime
import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import check  # noqa: E402

TODAY = datetime.date(2026, 10, 28)
SOURCE = 'Rents rose 4.2% in 2025, and 1,000,000 new awards are proposed. The share was 0.00873.\n'


class RegistryTests(unittest.TestCase):
    def tree(self, evidence=None, provisions=None, charter_extra=''):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        root = Path(tmp.name)
        (root / 'library').mkdir()
        (root / 'library/catalog.csv').write_text('id,path,title,kind,origin,rights,status,aliases,note\n'
                                                  'SRC-0001,legacy/sources/rents.md,Rents,,,,,,\n'
                                                  'SRC-0002,library/report.pdf,Report,,,,,,\n')
        (root / 'legacy/sources').mkdir(parents=True)
        (root / 'legacy/sources/rents.md').write_text(SOURCE)
        (root / 'library/report.pdf').write_bytes(b'%PDF')
        (root / 'agenda').mkdir()
        (root / 'agenda/agenda.csv').write_text('id,name,home_dossier,level,status,source,note\nHOU-4A,Vouchers,home,L2,decided,,\n')
        (root / 'charter').mkdir()
        (root / 'charter/decisions.md').write_text('| ID | Date |\n| --- | --- |\n| DEC-2026-10-28-01 | x |\n' + charter_extra)
        (root / 'dossiers/home').mkdir(parents=True)
        entry = {'id': 'EV-HOU-001', 'statement': 'Rents rose 4.2% in 2025.', 'figures': ['4.2%', '2025'],
                 'source': 'SRC-0001', 'anchor': 'Rents rose 4.2% in 2025', 'grade': 'A', 'fact_date': '2025',
                 'checked': '2026-10-28', 'recheck': '2027-04-28', 'supports': ['HOU-4A.01']}
        (root / 'dossiers/home/evidence.json').write_text(json.dumps(evidence if evidence is not None else [entry]))
        (root / 'dossiers/home/provisions.json').write_text(json.dumps(
            provisions if provisions is not None else [{'id': 'HOU-4A.01', 'evidence': ['EV-HOU-001']}]))
        return root, entry

    def run_on(self, root):
        return check.run(root, TODAY, with_legacy=False)

    def test_valid_tree_passes(self):
        root, _ = self.tree()
        errors, warnings, counts = self.run_on(root)
        self.assertEqual((errors, warnings), ([], []))
        self.assertEqual(counts['evidence'], 1)

    def test_anchor_must_exist(self):
        root, e = self.tree()
        e['anchor'] = 'Rents rose 5% in 2025'
        (root / 'dossiers/home/evidence.json').write_text(json.dumps([e]))
        self.assertIn('anchor not found', ' '.join(self.run_on(root)[0]))

    def test_figures_trace_to_the_anchor_and_rounding_follows(self):
        root, e = self.tree()
        e['figures'] = ['4.5%']
        (root / 'dossiers/home/evidence.json').write_text(json.dumps([e]))
        self.assertIn("figure '4.5%' not in its anchors", ' '.join(self.run_on(root)[0]))
        e.update(figures=['0.9%'], anchor='The share was 0.00873',
                 rounded=[{'figure': '0.9%', 'value': '0.00873', 'scale': 100, 'places': 1}])
        (root / 'dossiers/home/evidence.json').write_text(json.dumps([e]))
        self.assertEqual(self.run_on(root)[0], [])
        e['rounded'][0]['figure'] = '1.0%'
        (root / 'dossiers/home/evidence.json').write_text(json.dumps([e]))
        self.assertIn('does not follow from 0.00873', ' '.join(self.run_on(root)[0]))

    def test_grade_dates_and_sources(self):
        root, e = self.tree()
        e.update(grade='F', checked='last week', recheck='2026-01-01')
        bad = dict(e, id='EV-HOU-002', source='SRC-0002')
        (root / 'dossiers/home/evidence.json').write_text(json.dumps([e, bad]))
        errors, warnings, _ = self.run_on(root)
        text = ' '.join(errors)
        self.assertIn('grade must be one of A-E', text)
        self.assertIn('checked must be a date', text)
        self.assertIn('give a text_version', text)
        self.assertEqual(len(warnings), 2)  # past-due re-checks warn, never fail

    def test_provisions_and_references_resolve(self):
        root, _ = self.tree(provisions=[{'id': 'HOU-9.01', 'evidence': ['EV-HOU-404']}],
                            charter_extra='Cites OUT-07 and SRC-0099; `OUT-01` is only a format example.\n')
        text = ' '.join(self.run_on(root)[0])
        self.assertIn('HOU-9 is not in agenda/agenda.csv', text)
        self.assertIn('unknown evidence EV-HOU-404', text)
        self.assertIn('OUT-07 does not resolve', text)
        self.assertIn('SRC-0099 does not resolve', text)
        self.assertNotIn('OUT-01', text)

    def test_duplicate_ids(self):
        root, e = self.tree(charter_extra='| DEC-2026-10-28-01 | again |\n')
        (root / 'dossiers/home/evidence.json').write_text(json.dumps([e, e]))
        text = ' '.join(self.run_on(root)[0])
        self.assertIn('DEC-2026-10-28-01 defined twice', text)
        self.assertIn('EV-HOU-001: defined twice', text)


if __name__ == '__main__':
    unittest.main()
