#!/usr/bin/env python3
"""The immigration model's one command: every scenario's figures as one results file (`MOD-immigration`).

Role: the entry point of `MOD-immigration` (`MODEL-CARD.md`, "How to run"; stage H step H6). Status: working.
Standard library only; it needs no `build/` folder.

    python3 models/tools/immigration/immigration_run.py                     # writes results.json beside this file
    python3 models/tools/immigration/immigration_run.py --out DIR           # writes DIR/results.json
    python3 models/tools/immigration/immigration_run.py --scenario low      # one scenario (central, low or high)
    python3 models/tools/immigration/immigration_run.py --print             # the plain-text report, no file
    python3 models/tools/immigration/immigration_run.py --record --out build/immigration-recorded

The results file (`results.json`, on the toolkit's results schema, `models/schema/README.md`) holds, for each
scenario asked for: the model's seven general-fund lines by fiscal year, FY2030-40 (`lines`); the courts, USCIS,
the term-limited judge increment and care's base correction (`courts`, `uscis`, `term_increment`,
`care_base_correction`); and, from the central inputs, section 6's whole path (`path`: every line with its range,
the revenue lines and the totals, as `immigration_path.py` prints them) and the labor-market module
(`labor_market`), whose figures are reported beside the booked ones and never added to them. `central`, `low` and
`high` run every input at its central, low or high value together: a bound, not a probability interval.

`--record` stamps the commit and appends a `RUN-immigration-...` row to `models/runs.csv` (`models/runlog.py`).
"""
import argparse, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(ROOT, 'models'))
import runlog  # noqa: E402  (models/runlog.py)
import immigration_model as M  # noqa: E402
import immigration_path as P  # noqa: E402
import immigration_labor as L  # noqa: E402

MODEL_ID, VERSION, STATUS = 'MOD-immigration', '0.1.0', 'working'
SCENARIOS = ('central', 'low', 'high')
INPUT_FILES = [M.PARAMETERS, M.PLAN, L.PARAMETERS,
               # read by care's path, which memo 6's coverage line and care's base correction run on
               os.path.join(ROOT, 'models', 'tools', 'health-coverage', 'inputs.csv'),
               os.path.join(ROOT, 'models', 'tools', 'health-coverage', 'scenarios.csv'),
               os.path.join(ROOT, 'models', 'tools', 'health-coverage', 'results.json')]
UNITS = ('$ billion, nominal, a cost positive (a revenue gain negative), by federal fiscal year FY2030-40, on the general '
         'fund unless a key says off-budget; people in millions; judges as counts')
BASELINE = ("current law as it will stand in January 2029 (dossiers/immigration/6-cost.md); the status line scales CBO's "
            "2021 score of H.R. 6 (February 2021 baseline, EV-IMM-600); the courts start from EOIR's FY2026 counts "
            "(EV-IMM-100, -102, -103); E-Verify's lines scale CBO and JCT's 2013 score (EV-IMM-394, -395)")
SCORING = ('conventional: no macroeconomic feedback; the labor-market module (labor_market) is a separate reading of '
           'the evidence, not booked and not added to any line')
UNCERTAINTY = ('bounds, not probability intervals: the low and high scenarios run every input at its low or high value '
               'together; the path\'s ranges are section 3\'s, summed linearly; the labor-market module reports its '
               'own low and high')


def r(x, n=4):
    return None if x is None else round(x + 0.0, n)


def fy(path):
    return {str(y): r(path[y]) for y in M.YEARS}


def scenario(case):
    lines = M.lines(case)
    e, u, t, cb = M.eoir(case), M.uscis(case), M.term_increment(case), M.care_base_correction(case)
    return {
        'lines': {k: fy(p) for k, p in lines.items()},
        'window_fy2030_39': {k: r(M.window(p)) for k, p in lines.items()},
        'fy2040': {k: r(p[2040]) for k, p in lines.items()},
        'courts': {'judges_needed': e['judges_needed'], 'judges_added': e['judges_added'], 'judges_peak': r(e['judges_peak'], 1),
                   'cleared_fy': e['cleared_fy'], 'cleared_fy_at_800_judges': e['cleared_at_800'],
                   'cleared_fy_at_150_hires_a_year': e['cleared_slow_ramp'],
                   'not_cleared_means': f'null: the backlog does not clear by FY{M.COURT_LAST_FY}, the last year court_path runs',
                   'judges_by_year': {str(y): r(j, 1) for y, j in e['judges_by_year'].items()},
                   'judge_teams_fy2030_39': r(M.window(e['judges_cost'])), 'counsel_fy2030_39': r(M.window(e['counsel'])),
                   'detained_court_cases_k_a_year': r(e['detained_cases_k'], 1)},
        'uscis': {'filings_m': r(u['filings_m']), 'filings_by_year_m': fy(u['filings_by_year']),
                  'backlog_years_to_clear': r(u['backlog_years_to_clear'], 2), 'backlog_cleared_m': r(u['backlog_cleared_m']),
                  'backlog_left_m': r(u['backlog_left_m'])},
        'term_increment': {'steady_state_judges': r(t['need'], 1), 'saving_fy2036_39': r(t['saving_window']),
                           'saving_fy2040': r(t['saving_2040'])},
        'care_base_correction': {'note': "for care's booking (dossiers/care/tools/status_rule.py), not counted in this model's lines",
                                 'saving': fy(cb['saving']), 'people_m': fy(cb['people']),
                                 'saving_fy2030_39': r(M.window(cb['saving']))},
    }


def path_block():
    spend, rev = P.lines(), P.revenue_lines()

    def rows(d):
        return [{'line': k, 'fy': fy(p), 'fy2030_39': r(sum(p[y] for y in P.WINDOW)), 'fy2040': r(p[2040]),
                 'range_fy2030_39': [r(lo), r(hi)], 'range_fy2040': [r(lo40), r(hi40)]}
                for k, (p, lo, hi, lo40, hi40) in d.items()]
    totals = {}
    for label, d in (('spending', spend), ('revenue', rev), ('all_general_fund', {**spend, **rev})):
        t, lo, hi, lo40, hi40 = P.total(d)
        totals[label] = {'fy': fy(t), 'fy2030_39': r(sum(t[y] for y in P.WINDOW)), 'fy2040': r(t[2040]),
                         'range_fy2030_39': [r(lo), r(hi)], 'range_fy2040': [r(lo40), r(hi40)]}
    ev = P.everify()
    off, on = ev['off'], ev['on'][0]
    adm = spend['IMM-4.12-4.15: E-Verify operations and error correction (memo 5, A)'][0]
    return {'note': "section 6's path (dossiers/immigration/6-cost.md, part 1) from the central inputs, with section 3's ranges",
            'spending': rows(spend), 'revenue': rows(rev), 'totals': totals,
            'everify_off_budget': {'fy': fy(off), 'fy2030_39': r(sum(off[y] for y in P.WINDOW)), 'fy2040': r(off[2040]),
                                   'note': "Social Security's funds: a loss (a cost), booked as IMM-EV-SS"},
            'everify_unified_with_operations': {'fy2030_39': r(sum(off[y] + on[y] + adm[y] for y in P.WINDOW)),
                                                'fy2040': r(off[2040] + on[2040] + adm[2040])}}


def build(cases=SCENARIOS):
    out = {'scenarios': {c: scenario(c) for c in cases}, 'path': path_block(), 'labor_market': L.results()}
    out['crs_replay'] = {'note': "CRS R47637's projection run through court_path (benchmark only; SRC-4089)",
                         'cleared_fy_by_corps': {str(j): M.crs_replay(j) for j in range(649, 1650, 100)}}
    return out


def code_files():
    """Every repository module this run loaded (the run-log helper refuses a header that leaves one out)."""
    files = set()
    for m in list(sys.modules.values()):
        f = getattr(m, '__file__', None)
        if not f:
            continue
        p = os.path.realpath(f)
        if p.startswith(ROOT + os.sep) and not p.startswith(os.path.join(ROOT, 'models', 'schema') + os.sep) \
                and os.path.basename(p) not in ('runlog.py',) and not os.path.basename(p).startswith('test_'):
            files.add(p)
    files.add(os.path.realpath(__file__))
    return sorted(files)


def header(cases, commit=None):
    return runlog.header(MODEL_ID, VERSION, STATUS, code=code_files(), inputs=INPUT_FILES, units=UNITS,
                         price_basis='nominal dollars (unit costs grown at price_growth from their price year)',
                         year_type='fiscal', baseline_vintage=BASELINE, scoring_convention=SCORING,
                         scenarios=list(cases), uncertainty=UNCERTAINTY, commit=commit)


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split('\n')[0])
    ap.add_argument('--out', default=HERE, help='directory for results.json (default: this folder)')
    ap.add_argument('--scenario', default='all', choices=('all',) + SCENARIOS)
    ap.add_argument('--print', action='store_true', help="print the model's and the path's plain-text reports; write nothing")
    ap.add_argument('--record', action='store_true', help='stamp the commit and append a RUN- row to models/runs.csv')
    a = ap.parse_args(argv)
    if a.print:
        M.report()
        print()
        P.main()
        print()
        L.report()
        return 0
    cases = SCENARIOS if a.scenario == 'all' else (a.scenario,)
    res = build(cases)
    commit = runlog.commit_for(code_files() + INPUT_FILES) if a.record else None
    out = runlog.stamp(res, header(cases, commit))
    os.makedirs(a.out, exist_ok=True)
    path = os.path.join(a.out, 'results.json')
    runlog.write_json(path, out)
    if a.record:
        cmd = 'python3 models/tools/immigration/immigration_run.py --record' + (
            '' if os.path.abspath(a.out) == HERE else f' --out {os.path.relpath(a.out, ROOT)}')
        print('recorded', runlog.record(path, cmd))
    return 0


if __name__ == '__main__':
    sys.exit(main())
