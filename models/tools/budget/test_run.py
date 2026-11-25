#!/usr/bin/env python3
"""Tests for the budget model's one command (`run.py`, stage H step H4).

Role: checks that `run.py` rebuilds the engine without `build/` and reproduces the committed figures exactly: the
engine's `models/data/fiscal-paths.csv` and baseline, and the plan's case `mixed` in
`models/data/recovery-budget-paths.csv`; that a `rows` reform adds exactly its rows and the interest on them; that a
bad reform file is refused; and that `parameters.csv` says what the engine's code holds. Status: current. Run by
run-all.sh (step 6e2); standard library only.
"""
import csv, importlib.util, io, json, os, subprocess, sys, tempfile, unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
DATA = ROOT / 'models' / 'data'
sys.path.insert(0, str(HERE))
import run as R  # noqa: E402

TMP = None


def setUpModule():
    global TMP
    TMP = tempfile.TemporaryDirectory(prefix='budget-run-')
    run = lambda *a: subprocess.run([sys.executable, '-W', 'ignore::ResourceWarning', str(HERE / 'run.py'), *a], check=True,
                                    stdout=subprocess.DEVNULL)   # each run in its own process, as a user runs it
    run('--reform', str(HERE / 'reforms' / 'plan.json'), '--out', str(Path(TMP.name) / 'plan'))
    run('--reform', str(HERE / 'reforms' / 'cbo-2024-mandatory-2.json'), '--out', str(Path(TMP.name) / 'cbo'),
        '--from-build', str(Path(TMP.name) / 'plan'))


def tearDownModule():
    TMP.cleanup()


def out(*p):
    return Path(TMP.name).joinpath(*p)


def paths(f):
    return {(r['scenario'], int(r['year'])): r for r in csv.DictReader(open(f))}


class FreshRun(unittest.TestCase):
    def test_engine_outputs_equal_the_committed_files(self):
        """Built without build/ or run-all.sh, the engine's files are the committed ones, byte for byte."""
        self.assertEqual(out('plan', 'fiscal-paths.csv').read_bytes(), (DATA / 'fiscal-paths.csv').read_bytes())
        self.assertEqual(out('plan', 'fiscal-baseline.csv').read_bytes(), (DATA / 'fiscal-baseline.csv').read_bytes())

    def test_plan_is_case_mixed_exactly(self):
        lines = (DATA / 'recovery-budget-paths.csv').read_text().splitlines(keepends=True)
        mixed = [lines[0]] + [x for x in lines[1:] if x.startswith('mixed,')]
        self.assertEqual(out('plan', 'plan-paths.csv').read_text(), ''.join(mixed))

    def test_current_law_is_the_engine_base(self):
        p = paths(out('plan', 'paths.csv'))
        fp = {(r['scenario'], int(r['year'])): r for r in csv.DictReader(open(DATA / 'fiscal-paths.csv'))}
        for y in range(2026, 2057):
            self.assertAlmostEqual(float(p[('current-law', y)]['debt_bn']), float(fp[('BASE', y)]['debt']), places=2)
            self.assertAlmostEqual(float(p[('current-law', y)]['deficit_bn']), float(fp[('BASE', y)]['deficit']), places=2)

    def test_results_header(self):
        for name in ('plan', 'cbo'):
            d = json.loads(out(name, 'results.json').read_text())
            sys.path.insert(0, str(ROOT / 'models' / 'schema'))
            import results as S
            self.assertEqual(S.validate_header(d['header']), [], name)
            self.assertEqual(d['header']['model_id'], 'MOD-budget')
            self.assertIn(R.ROOT.joinpath('models/tools/budget/run.py').relative_to(ROOT).as_posix(), d['header']['code'])


class RowsReform(unittest.TestCase):
    def test_rows_and_interest(self):
        """The option changes outlays by exactly its rows; debt by the rows plus the engine's interest on them."""
        p = paths(out('cbo', 'paths.csv'))
        rf = json.loads((HERE / 'reforms' / 'cbo-2024-mandatory-2.json').read_text())
        rows = {int(y): v for y, v in rf['rows'][0]['fy'].items()}
        for y in range(2026, 2057):
            a, b = p[('current-law', y)], p[(rf['id'], y)]
            self.assertAlmostEqual(float(b['primary_outlays_bn']) - float(a['primary_outlays_bn']), rows.get(y, 0.0), delta=0.0015)
            self.assertEqual(a['revenue_bn'], b['revenue_bn'])
            if y < 2033:
                self.assertEqual(a, {**b, 'scenario': 'current-law'})
        d = json.loads(out('cbo', 'results.json').read_text())
        saved = -d['change']['2034']['debt_bn']
        self.assertGreater(saved, 6.7)            # the two years' $6.7B plus interest
        self.assertLess(saved, 6.7 * 1.05)

    def test_deficit_identity(self):
        for (sid, y), r in paths(out('cbo', 'paths.csv')).items():
            gap = float(r['primary_outlays_bn']) + float(r['interest_bn']) - float(r['revenue_bn']) - float(r['deficit_bn'])
            self.assertLess(abs(gap), 0.002, (sid, y))

    def test_bad_reform_refused(self):
        with tempfile.TemporaryDirectory() as t:
            f = Path(t) / 'bad.json'
            f.write_text(json.dumps({'id': 'x', 'label': 'x', 'source': 'x', 'kind': 'rows',
                                     'rows': [{'id': 'a', 'side': 'spending', 'fy': {'2030': 1}}]}))
            with self.assertRaises(SystemExit):
                R.read_reform(f)
            f.write_text(json.dumps({'id': 'x', 'label': 'x', 'source': 'x', 'kind': 'rows',
                                     'rows': [{'id': 'a', 'side': 'revenue', 'fy': {'2020': 1}}]}))
            with self.assertRaises(SystemExit):
                R.read_reform(f)


class Parameters(unittest.TestCase):
    """parameters.csv documents the engine's values; this keeps the two from drifting apart."""
    @classmethod
    def setUpClass(cls):
        cls.p = {(r['id'], r['year']): r['value'] for r in csv.DictReader(open(HERE / 'parameters.csv'))}
        sys.path.append(str(ROOT / 'models' / 'tools'))
        spec = importlib.util.spec_from_file_location('budget_test_fiscal_data', HERE / 'engine' / 'fiscal-data.py')
        cls.fd = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(cls.fd)
        cls.fm = R.module('budget_test_fiscal_model', HERE / 'engine' / 'fiscal-model.py')
        cls.funds = {r['key']: r['value'] for r in csv.DictReader(open(DATA / 'inputs' / 'funds-parameters.csv'))}

    def test_cpi(self):
        self.assertEqual(float(self.p[('cpi.growth', 'FY2026-FY2036')]), self.fm.CPI[2036])
        self.assertEqual(float(self.p[('cpi.growth', 'FY2037-FY2056')]), self.fm.CPI[2037])

    def test_fy2026_actuals(self):
        a = self.fd.FY2026_ACTUAL
        for pid, key in (('fy2026.revenue', 'rev_total'), ('fy2026.outlays', 'out_total'), ('fy2026.net_interest', 'out_net_interest'),
                         ('fy2026.customs', 'rev_customs'), ('fy2026.debt_public', 'debt_public')):
            self.assertAlmostEqual(float(self.p[(pid, 'FY2026')]), a[key], places=6, msg=pid)

    def test_adjustments(self):
        adj = {a['id']: a for a in self.fd.ADJUSTMENTS}
        self.assertEqual(float(self.p[('adj.tariff_ruling', 'FY2027-FY2036')]), adj['ADJ-T1']['ten_year_total'])
        self.assertEqual(float(self.p[('adj.tariff_refunds', 'FY2027')]), adj['ADJ-T2']['one_time'][2027])

    def test_funds(self):
        """Each funds parameter equals the value under its own key in funds-parameters.csv (the funds model's input)."""
        keys = {'fund.ss_reserve': 'ss_reserve_2025', 'fund.hi_reserve': 'hi_reserve_2025', 'fund.hi_payroll_ratio': 'hi_payroll_ratio',
                'fund.ss_cpie': 'ss_cpie_ssa_bump', 'fund.carbon_dividend_share': 'carbon_dividend_share'}
        for pid, key in keys.items():
            v = [r for k, r in self.p.items() if k[0] == pid]
            self.assertEqual(len(v), 1, pid)
            self.assertEqual(float(v[0]), float(self.funds[key]), f'{pid} vs funds-parameters.csv {key}')

if __name__ == '__main__':
    unittest.main()
