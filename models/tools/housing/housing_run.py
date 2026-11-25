#!/usr/bin/env python3
"""The housing model's one command: cost, reach and rents as one results file (`MOD-housing`).

Role: the entry point of `MOD-housing` (`MODEL-CARD.md`, "How to run"; stage H step H7). Status: exploratory.
Standard library only; it needs no `build/` folder.

    python3 models/tools/housing/housing_run.py                    # writes results.json beside this file
    python3 models/tools/housing/housing_run.py --out DIR          # writes DIR/results.json
    python3 models/tools/housing/housing_run.py --scenario low     # one case (central, low or high)
    python3 models/tools/housing/housing_run.py --leased 0.75      # every rental line at another leased share
    python3 models/tools/housing/housing_run.py --print            # a plain-text summary, no file
    python3 models/tools/housing/housing_run.py --record --out build/housing-recorded

The results file holds, for each case: every line of `dossiers/home/6-cost.md` section 1.2 (FY2030-39 window,
FY2040, FY2041, the yearly path FY2030-45 for built lines, and whether the line is built or taken as published)
and the totals (`cost`); and, from the central inputs, the reproduction of section 1.2 line by line
(`reproduction`), section 1.4's lease-up table (`lease_up`), households reached by stage and income band
(`reach`), and the rent readings and the supply range (`rents`), which are never added to the cost.

`--record` stamps the commit and appends a `RUN-housing-...` row to `models/runs.csv` (`models/runlog.py`).
"""
import argparse, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(ROOT, 'models'))
import runlog  # noqa: E402  (models/runlog.py)
import housing_model as M  # noqa: E402

MODEL_ID, VERSION, STATUS = 'MOD-housing', '0.1.0', 'exploratory'
UNITS = ('$ billion, nominal, a cost positive (the tax credits\' revenue loss positive), by federal fiscal year; '
         'households and homes as counts')
BASELINE = ('current law as it will stand in January 2029, against the adopted baseline (CBO, February 2026) that '
            'dossiers/home/6-cost.md prices each provision over (ASM-INCREMENT); the subsidy starts from HUD\'s 2023 '
            'spending per voucher unit (EV-HOU-370); the pools from HUD\'s Worst Case Housing Needs 2025 (2023 data)')
SCORING = ('conventional, as a CBO score: no offsetting savings outside housing\'s accounts, no macroeconomic feedback, '
           'no interest; credit lines on a credit-reform basis as 6-cost.md prices them; the rent readings are a '
           'separate reading of the evidence, not booked and never added to any line')
UNCERTAINTY = ('bounds, not probability intervals: low and high move every judgment input in the same direction '
               '(6-cost.md); lines built from decided amounts carry 6-cost.md\'s own ranges; the rent readings move '
               'their three inputs together; supply is a range from the evidence, not a forecast')


def r(x, n=4):
    return None if x is None else round(x + 0.0, n)


def rr(o, n=4):
    if isinstance(o, dict):
        return {str(k): rr(v, n) for k, v in o.items()}
    if isinstance(o, (list, tuple)):
        return [rr(v, n) for v in o]
    if isinstance(o, float):
        return r(o, n)
    return o


def cost(case, leased=None):
    L = M.lines(case, leased)
    t = M.totals(L)
    return {'lines': {k: {'window_fy2030_39': r(d['window']), 'fy2040': r(d['fy2040']), 'fy2041': r(d['fy2041']),
                          'method': d['method'], 'credit_revenue_loss': k in M.CREDITS,
                          'path': None if d['path'] is None else {str(y): r(v) for y, v in d['path'].items()}}
                      for k, d in L.items()},
            'totals': rr(t)}


def reproduction():
    """6-cost.md 1.2 against the model, line by line: the published central, low and high, and the model's."""
    C, Lo, Hi = M.lines('central'), M.lines('low'), M.lines('high')
    rows = []
    for k, label, c, lo, hi, f40 in M.TABLE_1_2:
        rows.append({'line': k, 'label': label, 'method': C[k]['method'],
                     'published': {'central': c, 'low': lo, 'high': hi, 'fy2040': f40},
                     'model': {'central': r(C[k]['window'], 3), 'low': r(Lo[k]['window'], 3), 'high': r(Hi[k]['window'], 3),
                               'fy2040': r(C[k]['fy2040'], 3), 'central_as_published': M.displayed(C[k]['window'], c)}})
    tc, tl, th = M.totals(C), M.totals(Lo), M.totals(Hi)
    return {'rows': rows, 'totals': {
        'spending': {'published': list(M.TABLE_SPENDING), 'model': [r(tc['spending_window'], 2), r(tl['spending_window'], 2), r(th['spending_window'], 2)]},
        'credits': {'published': list(M.TABLE_CREDITS[:3]), 'model': [r(tc['credits_window'], 2), r(tl['credits_window'], 2), r(th['credits_window'], 2)]},
        'housing': {'published': list(M.TABLE_HOUSING[:3]), 'model': [r(tc['housing_window'], 2), r(tl['housing_window'], 2), r(th['housing_window'], 2)]},
        'housing_fy2040': {'published': M.TABLE_HOUSING[3], 'model': r(tc['housing_fy2040'], 2)},
        'spending_fy2040': {'published': M.TABLE_FY2040_SPENDING, 'model': r(tc['spending_fy2040'], 2)},
        'sum_of_published_lines': {'central': r(sum(x[2] for x in M.TABLE_1_2), 2), 'low': r(sum(x[3] for x in M.TABLE_1_2), 2),
                                   'high': r(sum(x[4] for x in M.TABLE_1_2), 2)}}}


def build(cases, leased=None):
    out = {'cost': {c: cost(c, leased) for c in cases}}
    if leased is None:
        out['reproduction'] = reproduction()
        out['lease_up'] = rr(M.lease_up())
    out['reach'] = rr(M.reach('central', leased), 0 if False else 4)
    out['rents'] = rr(M.rents(leased))
    out['leased_share'] = leased if leased is not None else 'as in parameters.csv (0.9 central)'
    return out


def code_files():
    return [os.path.join(HERE, 'housing_run.py'), os.path.join(HERE, 'housing_model.py')]


def run(cases=M.CASES, leased=None, record=False):
    res = build(cases, leased)
    paths = code_files() + M.INPUTS
    scen = list(cases) + ([f'leased {leased}'] if leased is not None else [])
    h = runlog.header(MODEL_ID, VERSION, STATUS, code=code_files(), inputs=M.INPUTS, units=UNITS,
                      price_basis='nominal dollars', year_type='federal fiscal year', baseline_vintage=BASELINE,
                      scoring_convention=SCORING, scenarios=scen, uncertainty=UNCERTAINTY,
                      commit=runlog.commit_for(paths) if record else None)
    return runlog.stamp(res, h)


def report(res):
    out = []
    for c, d in res['cost'].items():
        t = d['totals']
        out.append(f"{c}: housing ${t['housing_window']:.1f}B over FY2030-39 (spending {t['spending_window']:.1f}, credits "
                   f"{t['credits_window']:.1f}); FY2040 ${t['housing_fy2040']:.1f}B")
    if 'reproduction' in res:
        for row in res['reproduction']['rows']:
            p, m = row['published'], row['model']
            out.append(f"  {row['label'][:52]:52s} {p['central']:>7} {m['central']:>9.2f}  ({row['method']})")
    lt = res['reach']['leased_total']
    out.append('households leased: ' + ', '.join(f'FY{y} {v / 1e6:.2f}M' for y, v in lt.items() if y in ('2034', '2040', '2042')))
    rc = res['rents']['readings']['central']['fy2040']
    out.append(f"rents (FY2040, central): landlord capture ${rc['landlord_capture_tight'] + rc['landlord_capture_other']:.1f}B "
               f"of ${res['rents']['added_rent_subsidy']['fy2040']:.1f}B added subsidy; never added to the cost")
    return '\n'.join(out)


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument('--out', default=HERE)
    ap.add_argument('--scenario', choices=M.CASES)
    ap.add_argument('--leased', type=float, help='steady-state leased share for every rental line (6-cost.md 1.4)')
    ap.add_argument('--print', action='store_true')
    ap.add_argument('--record', action='store_true')
    a = ap.parse_args(argv)
    if a.leased is not None and not 0 < a.leased <= 1:
        ap.error('--leased is a share between 0 and 1')
    cases = (a.scenario,) if a.scenario else M.CASES
    res = run(cases, a.leased, a.record)
    if a.print:
        print(report(res))
        return 0
    os.makedirs(a.out, exist_ok=True)
    path = os.path.join(a.out, 'results.json')
    runlog.write_json(path, res)
    print(f'wrote {os.path.relpath(path, ROOT)}')
    if a.record:
        cmd = 'python3 models/tools/housing/housing_run.py --record --out ' + os.path.relpath(a.out, ROOT)
        print(runlog.record(path, cmd))
    return 0


if __name__ == '__main__':
    sys.exit(main())
