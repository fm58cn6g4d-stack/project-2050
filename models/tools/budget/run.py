#!/usr/bin/env python3
"""The federal budget model's one command: current law, or current law plus a reform, from a fresh clone.

Role: the entry point of `MOD-budget` (`models/tools/budget/MODEL-CARD.md`, "How to run"; stage H step H4). Status:
working. Standard library only; it needs no `build/` folder and no `run-all.sh`.

    python3 models/tools/budget/run.py --out DIR                                        # current law
    python3 models/tools/budget/run.py --reform models/tools/budget/reforms/cbo-2024-mandatory-2.json --out DIR
    python3 models/tools/budget/run.py --reform models/tools/budget/reforms/plan.json --out DIR

It builds, into DIR, what `run-all.sh` builds for the budget model: the baseline (`fiscal-baseline.csv`, from CBO's
committed February 2026 files), the ledger (`ledger.json`), the engine's paths (`fiscal-model.json`,
`fiscal-paths.csv`) and the dedicated funds (`funds.json`). Then it applies the reform and writes
`results.json` (on the toolkit's results schema, `models/schema/README.md`) and `paths.csv` (current law and the
reform, year by year, FY2026-2056).

A reform file is JSON with an `id`, a `label`, a `source` and a `kind`:
- `rows`: changes to revenue or outlays by fiscal year, in nominal $B (`rows`, each with `id`, `label`, `side`
  `revenue` or `outlays`, and `fy` {year: $B}); positive revenue lowers the deficit, positive outlays raise it.
  Interest on the added debt follows the engine's own rule (`fiscal-model.py`, `debt_roll`: CBO's projected
  rates on new borrowing), so a reform's paths are built exactly as the engine builds a program row's.
- `plan`: Project 2050's plan as booked, a case of the recovery budget (`case`, e.g. `mixed`): the agenda ledger
  with stage G's financing settlement. Its rows are written to `plan-paths.csv` in the recovery budget's own
  columns, so they can be compared with `models/data/recovery-budget-paths.csv` cell for cell.
- `current-law`: no change (the default when `--reform` is left out).

`--from-build DIR` reuses an engine run already in DIR (run-all.sh's `build/`) instead of rebuilding it;
`--record` stamps the commit and appends a `RUN-budget-...` row to `models/runs.csv` (`models/runlog.py`).
"""
import argparse, csv, importlib.util, json, os, shutil, subprocess, sys, tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
TOOLS = ROOT / 'models' / 'tools'
ENGINE = HERE / 'engine'
DATA = ROOT / 'models' / 'data'
sys.path.insert(0, str(ROOT / 'models'))
import runlog  # noqa: E402

MODEL_ID, VERSION, STATUS = 'MOD-budget', '0.7.0', 'working'
Y0, Y1 = 2026, 2056
ENGINE_OUT = ('moving-america.json', 'ledger.json', 'fiscal-baseline.csv', 'fiscal-model.json', 'fiscal-paths.csv', 'funds.json')
CURRENT_LAW = {'id': 'current-law', 'label': 'Current law (CBO\'s February 2026 baseline with the documented adjustments)',
               'kind': 'current-law', 'source': 'models/data/fiscal-baseline.csv'}
HEADLINE_YEARS = (2029, 2034, 2039, 2040, 2045, 2050, 2056)
PATH_COLS = ['gdp_bn', 'revenue_bn', 'primary_outlays_bn', 'interest_bn', 'deficit_bn', 'debt_bn',
             'deficit_gdp', 'debt_gdp', 'interest_gdp']


def module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    m = importlib.util.module_from_spec(spec)
    sys.modules[name] = m
    spec.loader.exec_module(m)
    return m


def build_engine(out):
    """The engine's run, the steps run-all.sh takes for it (0, 1, 5, 6 and 6c), into `out`."""
    py = [sys.executable, '-W', 'ignore::ResourceWarning']
    run = lambda *a: subprocess.run([*py, *map(str, a)], cwd=out, check=True, stdout=subprocess.DEVNULL)
    run(TOOLS / 'transportation' / 'report.py', '--json', out / 'moving-america.json')
    run(ENGINE / 'ledger-build.py')
    run(ENGINE / 'fiscal-data.py', '--cache', DATA / 'cbo', '--out', out / 'fiscal-baseline.csv')
    run(ENGINE / 'fiscal-model.py', '--ledger', out / 'ledger.json', '--baseline', out / 'fiscal-baseline.csv', '--out-dir', out)
    run(ENGINE / 'funds-model.py')


def read_reform(path):
    if not path:
        return dict(CURRENT_LAW), None
    r = json.loads(Path(path).read_text(encoding='utf-8'))
    for k in ('id', 'label', 'kind', 'source'):
        if k not in r:
            raise SystemExit(f'{path}: a reform file needs "{k}"')
    if r['kind'] not in ('rows', 'plan', 'current-law'):
        raise SystemExit(f'{path}: kind must be rows, plan or current-law, not {r["kind"]!r}')
    if r['kind'] == 'rows':
        for row in r.get('rows', []):
            if row.get('side') not in ('revenue', 'outlays'):
                raise SystemExit(f'{path}: row {row.get("id")}: side must be revenue or outlays')
            bad = [y for y in row.get('fy', {}) if not (Y0 <= int(y) <= Y1)]
            if bad:
                raise SystemExit(f'{path}: row {row["id"]}: years {bad} are outside FY{Y0}-{Y1}')
    return r, Path(path).resolve()


def current_law(fm):
    """Current law, year by year: the engine's BASE scenario (the baseline, nothing added)."""
    out = {}
    for y in range(Y0, Y1 + 1):
        v = fm['results']['BASE']['years'][str(y)]
        out[y] = dict(gdp_bn=v['gdp'], revenue_bn=v['rev'], primary_outlays_bn=v['out'] - v['interest'], interest_bn=v['interest'],
                      deficit_bn=v['deficit'], debt_bn=v['debt'])
    return out


def with_pct(path):
    for v in path.values():
        g = v['gdp_bn']
        v.update(deficit_gdp=100 * v['deficit_bn'] / g, debt_gdp=100 * v['debt_bn'] / g, interest_gdp=100 * v['interest_bn'] / g)
    return path


def apply_rows(F, B, base, reform):
    """Current law plus the reform's rows, with interest on the added debt by the engine's own rule."""
    rev = {y: 0.0 for y in range(Y0, Y1 + 1)}
    out = dict(rev)
    for row in reform.get('rows', []):
        for y, v in row['fy'].items():
            (rev if row['side'] == 'revenue' else out)[int(y)] += float(v)
    primary = {y: out[y] - rev[y] for y in rev}
    PI, PD = F.debt_roll(B, primary)
    path = {}
    for y, b in base.items():
        path[y] = dict(gdp_bn=b['gdp_bn'], revenue_bn=b['revenue_bn'] + rev[y], primary_outlays_bn=b['primary_outlays_bn'] + out[y],
                       interest_bn=b['interest_bn'] + PI[y], deficit_bn=b['deficit_bn'] + primary[y] + PI[y], debt_bn=b['debt_bn'] + PD[y])
    return path


def plan_case(build, reform):
    """The plan as booked: the recovery budget's case (`mixed`), built on this run's engine outputs."""
    RB = module('budget_run_recovery', TOOLS / 'recovery-budget' / 'model.py')
    f, b, m, u = RB.load(build, build / 'fiscal-baseline.csv')
    opts = {k: v for k, v in reform.get('options', {}).items()}
    c = RB.build_case(reform['case'], f, b, m, u, **opts)
    with (build / 'plan-paths.csv').open('w', newline='') as fh:
        rows = [dict(case=reform['case'], **r) for r in c['rows']]
        w = csv.DictWriter(fh, fieldnames=list(rows[0]), lineterminator='\n')
        w.writeheader()
        w.writerows(rows)
    path = {r['year']: dict(gdp_bn=r['gdp_bn'], revenue_bn=r['revenue_bn'], primary_outlays_bn=r['primary_outlays_bn'],
                            interest_bn=r['interest_bn'], deficit_bn=r['deficit_bn'], debt_bn=r['debt_bn']) for r in c['rows']}
    return path, RB


def summary(path):
    s = {str(y): {k: round(path[y][k], 3) for k in ('deficit_bn', 'debt_bn', 'deficit_gdp', 'debt_gdp', 'interest_gdp')}
         for y in HEADLINE_YEARS}
    s['FY2030-2039'] = {'deficit_bn': round(sum(path[y]['deficit_bn'] for y in range(2030, 2040)), 3)}
    return s


def code_files(kind):
    files = [Path(__file__), *sorted(ENGINE.glob('*.py')), TOOLS / 'inputs.py', TOOLS / 'scenarios.py',
             *sorted((TOOLS / 'transportation').glob('*.py'))]
    files = [f for f in files if not f.name.startswith('test_')]
    if kind == 'plan':
        files += [TOOLS / 'recovery-budget' / 'model.py']
    return [f for f in files if f.exists()]


def input_files(kind, reform_path):
    files = sorted((DATA / 'inputs').glob('*')) + sorted((DATA / 'cbo').glob('*')) + sorted((DATA / 'budget').glob('*.csv'))
    files += [ROOT / 'legacy' / 'sources' / 'climate-portfolio-pricing.json']
    if kind == 'plan':
        files += [TOOLS / 'recovery-budget' / 'assumptions.json']
    if reform_path:
        files.append(reform_path)
    return [f for f in files if f.is_file()]


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument('--reform', help='a reform file (models/tools/budget/reforms/); current law if left out')
    ap.add_argument('--out', required=True, help='the folder to build into')
    ap.add_argument('--from-build', help="reuse an engine run already in this folder (run-all.sh's build/)")
    ap.add_argument('--record', action='store_true', help='stamp the commit and append a RUN- row to models/runs.csv')
    a = ap.parse_args(argv)
    reform, reform_path = read_reform(a.reform)
    out = Path(a.out).resolve()
    out.mkdir(parents=True, exist_ok=True)
    if a.from_build:
        src = Path(a.from_build).resolve()
        if src != out:
            for n in ENGINE_OUT:
                shutil.copyfile(src / n, out / n)
    else:
        build_engine(out)
    F = module('budget_run_fiscal', ENGINE / 'fiscal-model.py')
    B = F.read_baseline(out / 'fiscal-baseline.csv')
    fm = json.loads((out / 'fiscal-model.json').read_text())
    base = with_pct(current_law(fm))
    if reform['kind'] == 'rows':
        path = with_pct(apply_rows(F, B, base, reform))
    elif reform['kind'] == 'plan':
        path = with_pct(plan_case(out, reform)[0])
    else:
        path = base
    with (out / 'paths.csv').open('w', newline='') as fh:
        w = csv.writer(fh, lineterminator='\n')
        w.writerow(['scenario', 'year'] + PATH_COLS)
        for sid, p in (('current-law', base), (reform['id'], path)) if reform['kind'] != 'current-law' else (('current-law', base),):
            for y in range(Y0, Y1 + 1):
                w.writerow([sid, y] + [round(p[y][c], 3) for c in PATH_COLS])
    scen = ['current-law'] + ([reform['id']] if reform['kind'] != 'current-law' else [])
    commit = runlog.commit_for([*code_files(reform['kind']), *input_files(reform['kind'], reform_path)]) if a.record else None
    h = runlog.header(MODEL_ID, VERSION, STATUS, code=code_files(reform['kind']), inputs=input_files(reform['kind'], reform_path),
                      units='nominal $B by federal fiscal year; shares of GDP in percent',
                      price_basis='nominal dollars', year_type='fiscal',
                      baseline_vintage="CBO, The Budget and Economic Outlook: 2026 to 2036 and the long-term budget outlook "
                                       "(February 2026), with the FY2026 actuals and post-February adjustments in fiscal-data.py",
                      scoring_convention='conventional: no macroeconomic feedback; interest on added debt at CBO\'s projected rates',
                      scenarios=scen, commit=commit,
                      uncertainty='not quantified in this file: a reform is applied at its central figures. The engine reports '
                                  'the plan\'s cautious end (scenario DEC-CAUT) and an interest-rate stress (DEC-R1) in '
                                  'fiscal-paths.csv; benchmarks.md lists the misses.')
    res = {'reform': {k: reform[k] for k in reform if k != 'rows'},
           'rows': reform.get('rows', []),
           'current_law': summary(base),
           'reform_result': summary(path),
           'change': {str(y): {k: round(path[y][k] - base[y][k], 3) for k in ('deficit_bn', 'debt_bn', 'debt_gdp')} for y in HEADLINE_YEARS},
           'files': sorted(ENGINE_OUT + ('paths.csv',) + (('plan-paths.csv',) if reform['kind'] == 'plan' else ()))}
    runlog.write_json(out / 'results.json', runlog.stamp(res, h))
    if a.record:
        cmd = 'python3 models/tools/budget/run.py ' + ' '.join(argv if argv is not None else sys.argv[1:])
        print(runlog.record(out / 'results.json', cmd))
    d = res['reform_result']
    print(f"{reform['id']}: debt {d['2039']['debt_gdp']:.1f}% of GDP in FY2039, {d['2056']['debt_gdp']:.1f}% in FY2056 "
          f"(current law {res['current_law']['2039']['debt_gdp']:.1f}%, {res['current_law']['2056']['debt_gdp']:.1f}%)")
    return 0


if __name__ == '__main__':
    sys.exit(main())
