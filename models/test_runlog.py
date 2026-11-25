#!/usr/bin/env python3
"""Tests for the run-log helper, `models/runlog.py` (stage H step H2a), in a scratch Git repository.

    python3 models/test_runlog.py
"""
import csv, json, subprocess, sys, tempfile, unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import runlog  # noqa: E402

FIELDS = dict(units='$ billion', price_basis='nominal dollars', year_type='fiscal',
              baseline_vintage='CBO, February 2026', scoring_convention='conventional', scenarios=['baseline'],
              uncertainty='not quantified')


def sh(root, *args):
    subprocess.run(['git', '-C', str(root), *args], check=True, capture_output=True)


class RunLog(unittest.TestCase):
    def setUp(self):
        self.real_root = runlog.ROOT
        self.root = Path(tempfile.mkdtemp())
        sh(self.root, 'init', '-q')
        sh(self.root, 'config', 'user.email', 'test@example.invalid')
        sh(self.root, 'config', 'user.name', 'test')
        m = self.root / 'models/tools/toy'
        m.mkdir(parents=True)
        (m / 'model.py').write_text('print(1)\n')
        (m / 'inputs.csv').write_text('id,value\na,1\n')
        sh(self.root, 'add', '.')
        sh(self.root, 'commit', '-q', '-m', 'toy')
        runlog.ROOT = self.root
        self.runs = self.root / 'models/runs.csv'
        self.m = m

    def tearDown(self):
        runlog.ROOT = self.real_root

    def head(self):
        return subprocess.run(['git', '-C', str(self.root), 'rev-parse', 'HEAD'], capture_output=True, text=True).stdout.strip()

    def write(self, commit):
        h = runlog.header('MOD-toy', '1.0.0', 'working', code=['model.py'], inputs=['inputs.csv'], base=self.m,
                          commit=commit, **FIELDS)
        out = runlog.stamp({'results': {'x': 1}, 'header': {'old': True}}, h)
        p = self.root / 'build/results.json'
        p.parent.mkdir(exist_ok=True)
        runlog.write_json(p, out)
        return p, out

    def test_header_and_stamp(self):
        p, out = self.write(None)
        self.assertEqual(list(out)[0], 'header')
        h = out['header']
        self.assertEqual(set(h['code']), {'models/tools/toy/model.py'})
        self.assertEqual(h['inputs']['models/tools/toy/inputs.csv'], runlog.sha256_file(self.m / 'inputs.csv'))
        self.assertIsNone(h['commit'])
        self.assertIn('not an official score or a benefit determination', h['disclaimer'])
        with self.assertRaises(ValueError):
            runlog.header('household', '1.0.0', 'working', code=['model.py'], inputs=['inputs.csv'], base=self.m, **FIELDS)
        with self.assertRaises(ValueError):
            runlog.header('MOD-toy', '1.0.0', 'working', code=['/etc/hostname'], inputs=['inputs.csv'], base=self.m, **FIELDS)

    def test_reference_runs_are_not_recorded(self):
        p, _ = self.write(None)
        with self.assertRaises(ValueError):
            runlog.record(p, 'cmd', runs=self.runs)
        self.assertFalse(self.runs.exists())

    def test_record_appends_rows(self):
        c = runlog.commit_for([self.m / 'model.py', self.m / 'inputs.csv'])
        self.assertEqual(c, self.head())
        p, _ = self.write(c)
        a = runlog.record(p, 'python3 model.py --record', 'first', runs=self.runs, date='2026-11-25')
        b = runlog.record(p, 'python3 model.py --record', '', runs=self.runs, date='2026-11-25')
        self.assertEqual((a, b), ('RUN-toy-2026-11-25-a', 'RUN-toy-2026-11-25-b'))
        rows = list(csv.DictReader(self.runs.read_text().splitlines()))
        self.assertEqual(list(rows[0]), runlog.COLUMNS)
        self.assertEqual(rows[0]['commit'], c)
        self.assertEqual(rows[0]['results_path'], 'build/results.json')
        self.assertTrue(rows[0]['python'])
        self.assertTrue(runlog.RUN_RE.match(rows[1]['run_id']))
        # the row's hash is the reference output's: the same run with commit null, as committed
        ref, _ = self.write(None)
        self.assertEqual(rows[0]['results_sha256'], runlog.sha256_file(ref))

    def test_record_refuses_other_files(self):
        p, out = self.write(self.head())
        p.write_text(json.dumps(out))   # not the standard serialization: its hash could not be checked
        with self.assertRaises(ValueError):
            runlog.record(p, 'cmd', runs=self.runs, date='2026-11-25')
        outside = Path(tempfile.mkdtemp()) / 'r.json'
        runlog.write_json(outside, out)
        with self.assertRaises(ValueError):
            runlog.record(outside, 'cmd', runs=self.runs, date='2026-11-25')

    def test_unlisted_imports_are_refused(self):
        mod = self.m / 'helper.py'
        mod.write_text('X = 1\n')
        sys.path.insert(0, str(self.m))
        try:
            import helper  # noqa: F401
            with self.assertRaises(ValueError):
                runlog.header('MOD-toy', '1.0.0', 'working', code=['model.py'], inputs=['inputs.csv'], base=self.m, **FIELDS)
            runlog.header('MOD-toy', '1.0.0', 'working', code=['model.py', 'helper.py'], inputs=['inputs.csv'], base=self.m, **FIELDS)
        finally:
            sys.path.remove(str(self.m))
            sys.modules.pop('helper', None)

    def test_dirty_code_is_refused(self):
        (self.m / 'model.py').write_text('print(2)\n')
        with self.assertRaises(RuntimeError):
            runlog.commit_for([self.m / 'model.py'])
        # a header stamped with a commit whose code has since changed is refused at record time
        p, _ = self.write(self.head())
        with self.assertRaises(ValueError):
            runlog.record(p, 'cmd', runs=self.runs, date='2026-11-25')


if __name__ == '__main__':
    unittest.main()
