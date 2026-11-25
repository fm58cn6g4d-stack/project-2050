#!/usr/bin/env python3
"""Tests for the toolkit's parameter, results and validation schemas (stage H step H2a).

    python3 models/schema/test_schema.py
"""
import json, sys, tempfile, unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import parameters as P  # noqa: E402
import results as R  # noqa: E402
import validation as V  # noqa: E402

GOOD = """id,value,unit,year,kind,source,low,high,note
cbo_unins,37.2,million people,2032,evidence,EV-CAR-051,,,Uninsured
po_rate,1.6,ratio,none,assumption,Washington's 160 percent (EV-CAR-236),1.2,2.0,Public option payment rate
top_rate,0.37,share,FY2030-FY2039,policy,https://www.law.cornell.edu/uscode/text/26/1,,,Top rate
label_row,staged,text,2032,policy,DEC-2026-11-10-05,,,A label
"""


def rows(text):
    with tempfile.NamedTemporaryFile('w', suffix='.csv', delete=False) as f:
        f.write(text)
    return P.read(f.name)


class Parameters(unittest.TestCase):
    def test_good_file_passes(self):
        self.assertEqual(P.validate(rows(GOOD)), [])

    def bad(self, line, fragment):
        errs = P.validate(rows(GOOD.splitlines()[0] + '\n' + line + '\n'))
        self.assertTrue(any(fragment in e for e in errs), errs)

    def test_each_rule(self):
        self.bad('Bad-ID,1,share,2032,evidence,EV-CAR-051,,,', 'id must be')
        self.bad('a,1,share,2032,guess,EV-CAR-051,,,', 'kind must be')
        self.bad('a,1,share,32,evidence,EV-CAR-051,,,', 'is not 2032')
        self.bad('a,1,share,2034-2030,evidence,EV-CAR-051,,,', 'backward')
        self.bad('a,x,share,2032,evidence,EV-CAR-051,,,', 'not a number')
        self.bad('a,1,share,2032,evidence,CBO says so,,,', 'needs an evidence ID')
        self.bad('a,1,share,2032,assumption,judgment,,,', 'needs a low and a high')
        self.bad('a,1,share,2032,assumption,judgment,2,3,', 'outside its range')
        self.bad('a,1,share,2032,assumption,judgment,3,2,', 'low is above high')
        self.bad('a,1,share,,evidence,EV-CAR-051,,,', 'empty year')

    def test_duplicate_and_missing_column(self):
        errs = P.validate(rows(GOOD + 'cbo_unins,1,share,2032,evidence,EV-CAR-051,,,\n'))
        self.assertTrue(any('duplicate' in e for e in errs))
        self.assertEqual(P.validate(rows('id,value\na,1\n')), ['missing column(s): unit, year, kind, source'])

    def test_column_map(self):
        old = GOOD.replace(',source,', ',evidence_id_or_basis,', 1)
        self.assertTrue(P.validate(rows(old)))
        with tempfile.NamedTemporaryFile('w', suffix='.csv', delete=False) as f:
            f.write(old)
        self.assertEqual(P.validate(P.read(f.name, {'evidence_id_or_basis': 'source'})), [])

    def test_table_and_card_block(self):
        t = P.table(rows(GOOD))
        self.assertIn('4 inputs: 1 traced to evidence, 2 policy parameters, 1 labeled assumptions', t)
        self.assertIn('| `po_rate` Public option payment rate | 1.6 | ratio | none | assumption |', t)
        self.assertIn('1.2 to 2.0', t)
        with tempfile.NamedTemporaryFile('w', suffix='.md', delete=False) as f:
            f.write(f'# Card\n\n{P.START}\nold\n{P.END}\n\nafter\n')
        new = P.update_card(f.name, 'NEW')
        self.assertIn(f'{P.START}\nNEW\n{P.END}', new)
        self.assertTrue(new.endswith('after\n'))

    def test_health_coverage_inputs_report_their_gap(self):
        # the demonstration model: its inputs map onto the schema except the effective year (step H3)
        hc = P.read(HERE.parent / 'tools/health-coverage/inputs.csv', {'evidence_id_or_basis': 'source'})
        errs = P.validate(hc)
        self.assertTrue(errs)
        self.assertTrue(all('year' in e for e in errs), [e for e in errs if 'year' not in e][:5])


def header(**kw):
    h = {'schema': R.SCHEMA, 'model_id': 'MOD-test', 'model_version': '1.2.3', 'status': 'working', 'commit': None,
         'code': {'models/tools/test/model.py': 'a' * 64}, 'inputs': {'models/tools/test/inputs.csv': 'b' * 64},
         'units': '$ billion', 'price_basis': 'nominal dollars', 'year_type': 'fiscal',
         'baseline_vintage': 'CBO, February 2026', 'scoring_convention': 'conventional', 'disclaimer': R.DISCLAIMER}
    h.update(kw)
    return h


class Results(unittest.TestCase):
    def test_valid(self):
        self.assertEqual(R.validate_header(header()), [])
        self.assertEqual(R.validate_header(header(commit='c' * 40)), [])

    def test_invalid(self):
        cases = {'model_id': 'household', 'model_version': '1.2', 'status': 'official', 'commit': 'abc',
                 'disclaimer': 'not an official score', 'units': '', 'inputs': {}, 'schema': 'other'}
        for k, v in cases.items():
            with self.subTest(k):
                self.assertTrue(R.validate_header(header(**{k: v})))
        self.assertTrue(R.validate_header(header(code={'/abs/model.py': 'a' * 64})))
        self.assertTrue(R.validate_header(header(code={'m.py': 'short'})))
        h = header()
        del h['units']
        self.assertEqual(R.validate_header(h), ['missing field "units"'])
        self.assertEqual(R.validate_header(header(extra=1)), ['unknown field "extra"'])

    def test_files(self):
        d = Path(tempfile.mkdtemp())
        (d / 'r.json').write_text(json.dumps({'results': {}, 'header': header()}, sort_keys=True))
        (d / 'r.md').write_text('# Results\n\n' + R.markdown_header(header()) + '\n')
        (d / 'bare.json').write_text('{"results": {}}')
        (d / 'bare.md').write_text('# Results\n')
        self.assertEqual(R.check_file(d / 'r.json'), [])
        self.assertEqual(R.check_file(d / 'r.md'), [])
        self.assertEqual(R.check_file(d / 'bare.json'), ['no "header" object'])
        self.assertEqual(R.check_file(d / 'bare.md'), ['no results header block'])
        self.assertIn('not an official score or a benefit determination', R.DISCLAIMER)


class Validation(unittest.TestCase):
    def bm(self, **kw):
        base = dict(id='BM-1', quantity='Uninsured', target=10.0, source='EV-CAR-051', vintage='CBO, Feb 2026',
                    unit='million', tolerance=0.1)
        base.update(kw)
        return V.Benchmark(**base)

    def test_relative_absolute_range(self):
        self.assertTrue(V.evaluate(self.bm(), 10.9).passed)
        self.assertFalse(V.evaluate(self.bm(), 11.1).passed)
        r = V.evaluate(self.bm(tolerance=0.5, tolerance_kind='absolute'), 9.6)
        self.assertTrue(r.passed)
        self.assertAlmostEqual(r.difference, -0.4)
        r = V.evaluate(self.bm(target=(5.0, 8.0), tolerance=0.0, tolerance_kind='range'), 9.0)
        self.assertFalse(r.passed)
        self.assertAlmostEqual(r.difference, 1.0)
        self.assertTrue(V.evaluate(self.bm(target=(5.0, 8.0), tolerance=0.25), 9.9).passed)   # within 25% of 8
        self.assertEqual(V.evaluate(self.bm(target=(5.0, 8.0), tolerance_kind='range'), 6.0).difference, 0.0)
        with self.assertRaises(ValueError):
            V.evaluate(self.bm(tolerance_kind='range'), 1.0)
        with self.assertRaises(ValueError):
            V.evaluate(self.bm(target=(8.0, 5.0)), 1.0)

    def test_problems(self):
        ok = V.evaluate(self.bm(), 10.0)
        miss = V.evaluate(self.bm(id='BM-2'), 20.0)
        insample = V.evaluate(self.bm(id='BM-3', in_sample=True), 10.0)
        self.assertEqual(V.problems([ok]), [])
        self.assertEqual(V.problems([ok, miss, insample]),
                         ['BM-2: a miss needs an explanation', 'BM-3: an in-sample check needs an explanation'])
        self.assertIn('BM-1: duplicate benchmark ID', V.problems([ok, ok]))
        self.assertIn('BM-1: not evaluated', V.problems([self.bm()]))
        self.assertIn('BM-1: a target needs its source and vintage', V.problems([V.evaluate(self.bm(vintage=' '), 10.0)]))

    def test_render(self):
        miss = V.evaluate(self.bm(id='BM-2', explanation='CBO counts more.'), 20.0)
        t = V.render([V.evaluate(self.bm(), 10.0), miss])
        self.assertTrue(t.startswith('2 benchmarks: 1 pass, 1 miss.'))
        self.assertIn('| BM-2 | Uninsured | 10.0 million | EV-CAR-051; CBO, Feb 2026 | 20.0 | 10.0 | 10% | **miss** | CBO counts more. |', t)


if __name__ == '__main__':
    unittest.main()
