#!/usr/bin/env python3
"""Tests for the toolkit check (`toolkit_check.py`, stage H step H2a): the register, the run log and the version rule.

    python3 models/registry/test_toolkit_check.py
"""
import contextlib, io, json, shutil, subprocess, sys, tempfile, unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[1]
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(REPO / 'models'))
import toolkit_check as T  # noqa: E402
import runlog  # noqa: E402

CRIT = [l.split(',')[0] for l in (REPO / 'models/release-criteria.csv').read_text().splitlines()[1:]]
COLS = T.FIXED + CRIT + T.TAIL


def sh(root, *args):
    return subprocess.run(['git', '-C', str(root), *args], check=True, capture_output=True, text=True).stdout.strip()


def toy_header(root, version):
    real = runlog.ROOT
    runlog.ROOT = root
    try:
        return runlog.header('MOD-toy', version, 'exploratory', code=['models/tools/toy/model.py'],
                             inputs=['models/tools/toy/inputs.csv'], units='$ billion', price_basis='nominal dollars',
                             year_type='fiscal', baseline_vintage='CBO, February 2026', scoring_convention='conventional')
    finally:
        runlog.ROOT = real


class Check(unittest.TestCase):
    def setUp(self):
        self.root = r = Path(tempfile.mkdtemp())
        (r / 'models/tools/toy').mkdir(parents=True)
        shutil.copy(REPO / 'models/release-criteria.csv', r / 'models/release-criteria.csv')
        shutil.copy(REPO / 'models/MODEL-CARD-TEMPLATE.md', r / 'models/MODEL-CARD-TEMPLATE.md')
        (r / 'models/runs.csv').write_text(','.join(T.RUN_COLUMNS) + '\n')
        (r / 'models/tools/run-all.sh').write_text('python3 "$TOOLS"/toy/test_toy.py\n')
        (r / 'models/tools/toy/model.py').write_text('print(1)\n')
        (r / 'models/tools/toy/inputs.csv').write_text('id,value\n')
        (r / 'models/tools/toy/test_toy.py').write_text('\n')
        self.row = {c: 'fail' for c in COLS}
        self.row.update(model_id='MOD-toy', name='Toy', path='models/tools/toy', status='exploratory', owner='x', card='',
                        parameters='', parameters_map='', results='models/tools/toy/results.json',
                        tests='models/tools/toy/test_toy.py', notes='', rc_tests_in_checks='pass', rc_validation='partial')
        self.write_register()
        self.write_results('0.1.0', {'x': 1})
        self.write_changelog(['0.1.0'])
        sh(r, 'init', '-q')
        sh(r, 'config', 'user.email', 'test@example.invalid')
        sh(r, 'config', 'user.name', 'test')
        sh(r, 'add', '.')
        sh(r, 'commit', '-q', '-m', 'base')
        self.base = sh(r, 'rev-parse', 'HEAD')
        self.real = T.ROOT
        T.set_root(r)

    def tearDown(self):
        T.set_root(self.real)

    def write_register(self, cols=None):
        cols = cols or COLS
        lines = [','.join(cols), ','.join(self.row.get(c, '') for c in cols)]
        (self.root / 'models/toolkit.csv').write_text('\n'.join(lines) + '\n')

    def write_results(self, version, results):
        d = {'header': toy_header(self.root, version), 'results': results}
        (self.root / 'models/tools/toy/results.json').write_text(json.dumps(d, indent=1, sort_keys=True))

    def write_changelog(self, versions):
        (self.root / 'models/tools/toy/CHANGELOG.md').write_text('# Toy\n\n' + ''.join(f'## {v} (2026-11-25)\n\n- x\n\n' for v in versions))

    def run_check(self, *args):
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            rc = T.main(['--base', self.base, *args])
        return rc, buf.getvalue()

    def test_clean_base_passes(self):
        self.row['rc_versioned'] = 'pass'
        self.row['rc_disclaimer'] = 'pass'
        self.write_register()
        rc, out = self.run_check()
        self.assertEqual(rc, 0, out)

    def test_results_change_without_bump_fails(self):
        self.write_results('0.1.0', {'x': 2})
        rc, out = self.run_check()
        self.assertEqual(rc, 1)
        self.assertIn('changed but the version did not go up (0.1.0 -> 0.1.0)', out)

    def test_bump_without_changelog_fails(self):
        self.write_results('0.2.0', {'x': 2})
        rc, out = self.run_check()
        self.assertEqual(rc, 1)
        self.assertIn('the newest changelog entry is 0.1.0, the results header says 0.2.0', out)

    def test_minor_bump_with_changelog_passes(self):
        self.write_results('0.2.0', {'x': 2})
        self.write_changelog(['0.2.0', '0.1.0'])
        rc, out = self.run_check()
        self.assertEqual(rc, 0, out)

    def test_patch_bump_may_not_change_results(self):
        self.write_results('0.1.1', {'x': 2})
        self.write_changelog(['0.1.1', '0.1.0'])
        rc, out = self.run_check()
        self.assertEqual(rc, 1)
        self.assertIn('is a patch release but', out)
        self.write_results('0.1.1', {'x': 1})   # a header-only change is a patch
        (self.root / 'models/tools/toy/model.py').write_text('print(1)  # comment\n')
        self.write_results('0.1.1', {'x': 1})
        self.assertEqual(self.run_check()[0], 0)

    def test_version_down_fails(self):
        self.write_results('0.0.9', {'x': 2})
        self.write_changelog(['0.0.9', '0.1.0'])
        self.assertIn('did not go up', self.run_check()[1])

    def test_register_cannot_overstate(self):
        self.row['rc_run_log'] = 'pass'   # no RUN- row exists
        self.row['rc_license'] = 'pass'   # no LICENSE file
        self.write_register()
        rc, out = self.run_check('--no-git')
        self.assertEqual(rc, 1)
        self.assertIn('rc_run_log recorded "pass" but the check finds fail', out)
        self.assertIn('rc_license recorded "pass"', out)

    def test_understatement_warns(self):
        rc, out = self.run_check('--no-git')   # rc_versioned and rc_disclaimer recorded fail, but both pass
        self.assertEqual(rc, 0, out)
        self.assertIn('warning: toolkit.csv MOD-toy: rc_versioned recorded fail but the check finds pass', out)

    def test_no_release_before_memo_h1(self):
        for status in ('released', 'preview'):
            self.row['status'] = status
            self.write_register()
            self.assertIn('before memo H1 is decided', self.run_check('--no-git')[1])

    def test_columns_follow_the_criteria_file(self):
        self.write_register([c for c in COLS if c != 'rc_review'])
        self.assertIn('toolkit.csv columns must be', self.run_check('--no-git')[1])
        crit = self.root / 'models/release-criteria.csv'
        crit.write_text('\n'.join(l for l in crit.read_text().splitlines() if not l.startswith('rc_review')) + '\n')
        rc, out = self.run_check('--no-git')   # criteria and columns changed together: accepted
        self.assertNotIn('columns must be', out)

    def test_bad_values_and_ids(self):
        self.row['rc_card'] = 'maybe'
        self.row['model_id'] = 'household'
        self.write_register()
        out = self.run_check('--no-git')[1]
        self.assertIn('rc_card is "maybe"', out)
        self.assertIn('"household" is not a MOD- ID', out)

    def test_run_rows(self):
        runs = self.root / 'models/runs.csv'
        good = ['RUN-toy-2026-11-25-a', '2026-11-25', 'MOD-toy', '0.1.0', 'c' * 40, 'cmd', 'build/r.json', 'a' * 64, 'b' * 64, '']
        runs.write_text(','.join(T.RUN_COLUMNS) + '\n' + ','.join(good) + '\n')
        self.assertNotIn('runs.csv', self.run_check('--no-git')[1])
        bad = list(good)
        bad[0], bad[4] = 'RUN-toy-2026-11-24-a', 'abc'
        runs.write_text(','.join(T.RUN_COLUMNS) + '\n' + ','.join(good) + '\n' + ','.join(good) + '\n' + ','.join(bad) + '\n')
        out = self.run_check('--no-git')[1]
        self.assertIn('RUN-toy-2026-11-25-a appears twice', out)
        self.assertIn('does not match its model ID and date', out)
        self.assertIn('commit must be a 40-character hash', out)


class RealRepository(unittest.TestCase):
    def test_register_and_headers_pass(self):
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            rc = T.main(['--no-git'])
        self.assertEqual(rc, 0, buf.getvalue())


if __name__ == '__main__':
    unittest.main()
