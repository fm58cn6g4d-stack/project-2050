#!/usr/bin/env python3
"""Bounded health decision checks using existing project models.
No policy input changes, benefit score or launch certification.
Run after bash index/tools/run-all.sh; outputs are generator-owned research.
"""
import argparse
import csv
import hashlib
import importlib.util
import json
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
TOOLS = ROOT / 'index/tools'
sys.path.insert(0, str(TOOLS))


def module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def analyze():
    fiscal = module('health_fiscal', TOOLS / 'fiscal-model.py')
    cal = module('health_calendar', TOOLS / 'calendar/model.py')
    capacity = module('health_capacity', TOOLS / 'capacity-funding.py')
    from inputs import read
    baseline = fiscal.read_baseline(ROOT / 'index/data/fiscal-baseline.csv')
    built = ROOT / 'build'
    ledger = json.loads((built / 'ledger.json').read_text())
    fresult = json.loads((built / 'fiscal-model.json').read_text())
    dec = fresult['results']['DEC']['years']
    # Reuse debt_roll directly: row_path deliberately calibrates the old window
    # and cannot safely represent a pre-window cash move by changing its start.
    def roll(flows):
        return fiscal.debt_roll(baseline, flows)[1]
    unit_2030 = roll({2030: 1.0})
    unit_shift = roll({2029: 1.0, 2030: -1.0})
    zero = roll({})
    assert all(v == 0 for v in zero.values())
    double = roll({2030: 2.0})
    assert all(abs(double[y] - 2 * unit_2030[y]) < 1e-10 for y in unit_2030)
    assert sum({2029: 1.0, 2030: -1.0}.values()) == 0
    headroom = min((-dec[str(y)]['gf_primary'] * baseline[2040]['gdp'] / baseline[y]['gdp'], y)
                   for y in range(2040, 2057))
    cfg, _ = cal.load()
    calendar = []
    for condition in cal.K:
        r, _ = cal.run(cfg, condition=condition, capacity='working',
                       strategy='deadline', merged=False, frontload=True)
        for vehicle in ('R1', 'R2'):
            done = r['vehicles'][vehicle]['done']
            calendar.append(dict(condition=condition, vehicle=vehicle, completion=done,
                                 days_until_2030=None if done is None else
                                 (date(2030, 1, 1) - date.fromisoformat(done)).days,
                                 r1_latest=r['checks']['R1_latest'],
                                 dem_start=r['checks']['DEM_start']))
    surge_bill = next(x for x in ledger['bills'] if x['id'] == 'CAP-7S')
    surge = capacity.assess(next(x for x in read('capacity-funding.csv') if x['id'] == 'CAP-7S'),
                            surge_bill, next(x for x in read('fiscal-years.csv') if x['id'] == 'CAP-7S'))
    with (ROOT / 'sources/health-cms-implementation-cost-register.csv').open() as f:
        packages = [x for x in csv.DictReader(f) if x['work_package'] in
                    ['CMS-IMP-01', 'CMS-IMP-02', 'CMS-IMP-03', 'CMS-IMP-04',
                     'CMS-IMP-08', 'CMS-IMP-11', 'CMS-IMP-13']]
    assert all(x['net_increment_bn'] == '' and x['fy2029_outlays_bn'] == '' for x in packages)
    # Mechanical examples only: no plan-allowance or actual device-price estimate.
    # A partial supplemental promise requires item/quantity mapping, not merely
    # subtracting the nominal allowance from the claim. Deliberately no formula.
    overlap_cases = [
        dict(case='new_MA_item_no_existing_promise', payer='Original Medicare if qualifying bridge',
             amount=None),
        dict(case='existing_diagnostic_service', payer='MA plan', amount=None),
        dict(case='existing_supplemental_item', payer='MA plan to contractual extent', amount=None),
        dict(case='partial_or_exhausted_allowance', payer='Unresolved item/quantity/liability map', amount=None),
        dict(case='nonsignificant_change', payer='MA plan from statutory effective date', amount=None),
        dict(case='first_adjusted_contract_year', payer='MA plan; no duplicate FFS payment', amount=None),
    ]
    files = ['index/tools/fiscal-model.py', 'index/tools/calendar/model.py',
             'index/tools/capacity-funding.py', 'index/data/fiscal-baseline.csv',
             'index/data/inputs/ledger-bills.csv', 'index/data/inputs/fiscal-profiles.csv',
             'index/data/inputs/fiscal-years.csv', 'index/data/inputs/calendar-scenarios.json',
             'index/data/inputs/capacity-funding.csv',
             'sources/health-cms-implementation-cost-register.csv',
             'index/tools/health/decision_analysis.py']
    return dict(source_commit='846be172efdc0c383d5d8c24194de3704a1cbaa1',
                status='Research calculations; unit sensitivities, not health cost estimates',
                unit='billions of nominal dollars unless specified',
                unit_unfinanced_2030_cost_debt={str(y): unit_2030[y] for y in (2030, 2039, 2040, 2056)},
                unit_setup_shift_2030_to_2029_debt={str(y): unit_shift[y] for y in (2029, 2030, 2039, 2040, 2056)},
                maturity_headroom_2040_bn=headroom[0], maturity_binding_year=headroom[1],
                maturity_headroom_basis='Unfinanced recurring GF cost starting 2040, growing with GDP; conditional on old surge proxy; not available financing',
                calendar=calendar, surge=surge,
                packages=[dict(id=x['work_package'], net_increment_bn=None, fy2029_cash_bn=None) for x in packages],
                payment_cases=overlap_cases, actual_benefit_cost=None,
                source_sha256={p: hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in files},
                verification='Debt zero/linearity and cash-shift conservation; package unknowns retained; existing model checks run by common runner')


def render(r):
    lines = ['# Health design: checks using existing models', '',
             'Generated by `index/tools/health/decision_analysis.py`; regenerate rather than edit. Research source: `'+r['source_commit']+'`.', '',
             '**These are normalized arithmetic and existing scenario outputs, not hearing/vision prices, a new policy score or a forecast.** No policy inputs change. Actual benefit and administrative costs remain unpriced.', '',
             '## Fiscal implications', '',
             '| Calculation | FY2039 added debt, $B | FY2040 added debt, $B | FY2056 added debt, $B |',
             '| --- | ---: | ---: | ---: |']
    for label, key in [('An illustrative unfinanced $1B of additional FY2030 GF outlays', 'unit_unfinanced_2030_cost_debt'),
                       ('Shift the same $1B of setup from FY2030 to FY2029, no lifetime primary addition', 'unit_setup_shift_2030_to_2029_debt')]:
        d = r[key]
        lines.append(f"| {label} | {d['2039']:.6f} | {d['2040']:.6f} | {d['2056']:.6f} |")
    lines += ['', 'Uses existing `fiscal-model.py` baseline, marginal-rate rule and half-year interest convention through `debt_roll`. The $1B is a unit, not an estimate, borrowing approval or identified pay-for. Earlier cash affects interest even when lifetime setup is unchanged. Net federal cost needs an actual benefit/premium/offset/state-buy-in bridge first.', '',
              f"Under the **old surge cash proxy**, DEC has room for only about **${r['maturity_headroom_2040_bn']:.3f}B in FY2040** of an additional unfinanced recurring GF cost growing with GDP from 2040, before one of the modeled maturity years fails (binding year {r['maturity_binding_year']}). This is an arithmetic threshold through 2056, not available financing, a score, an every-later-year certificate or permission to spend it. It supports pricing permanent operating/cost-sharing changes before adopting them.", '',
              'The existing fiscal row calibrates HLT-2 as a combined title with a three-year ramp. Changing its start would rescale that title, not isolate an extra hearing/vision year. No such substitution was made. HI reserves and dynamic revenue are excluded from this exercise.', '',
              '## Calendar preparation interval', '',
              'Existing working-capacity, deadline strategy, separate-climate and opening-concentration cases. Conditions are illustrative, not probabilities. Completion assumes procedural eligibility, votes and final agreement. Days below are calendar arithmetic, not available CMS engineering workdays.', '',
              '| Condition | Vehicle | Conditional completion | Calendar days to January 1, 2030 | R1 March check | DEM March start check |',
              '| --- | --- | --- | ---: | --- | --- |']
    for c in r['calendar']:
        lines.append(f"| {c['condition']} | {c['vehicle']} | {c['completion'] or 'unfinished'} | {c['days_until_2030'] if c['days_until_2030'] is not None else 'unknown'} | {c['r1_latest']} | {c['dem_start']} |")
    lines += ['', 'No additional hearing/vision drafting, committee or floor hours were invented or inserted. These cases cannot quantify the incremental R1 burden or certify six-month implementation. Use them to preserve R1 protection and identify the shorter R2 preparation interval. The adopted 2031 hearing/vision floor and HLT-3 dates remain in the delivery generator.', '',
              '## Capacity and claim boundaries', '',
              f"The existing capacity module returns FY2029 surge cash **unpriced** and acceleration fiscal validation **{r['surge']['fiscal_validation']}**. All {len(r['packages'])} relevant CMS package increments and FY2029 cash values are blank in the cost register and are preserved as null in the JSON. Their existence supports ownership and overlap review, not a completed marginal budget.", '',
              '| Claim case | Payment boundary requiring confirmation against chosen benefit |', '| --- | --- |']
    for c in r['payment_cases']: lines.append(f"| {c['case']} | {c['payer']} |")
    lines += ['', 'Claim boundaries follow the primary-law analysis in the decision packet; they are an explicit review matrix, not an executable adjudication engine. Partial allowances are deliberately unresolved. Do not treat nominal allowance subtraction as legal claim allocation.', '',
              'The household-incidence model values combined HLT-2 benefits and premiums at quintile level. It cannot resolve the distribution of a device copayment or an MA bridge charge for a particular person. Use beneficiary examples for that question; do not claim the existing aggregate D3 result clears a new benefit rule.', '',
              'Reproduction: run `bash index/tools/run-all.sh`, then `python3 index/tools/health/decision_analysis.py`. Companion JSON includes source SHA-256 values and explicit unknowns. The completed CMS pilot supplies the state/vendor cost-chain method; no pilot or empirical poverty model is rerun.']
    return '\n'.join(lines)+'\n'


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--output', type=Path, default=ROOT/'sources/health-design-model-checks')
    args = p.parse_args()
    r = analyze()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.with_suffix('.json').write_text(json.dumps(r, indent=2)+'\n')
    args.output.with_suffix('.md').write_text(render(r))
    print('Health analysis: existing fiscal/calendar/capacity modules reused; actual costs unpriced; invariants passed.')


if __name__ == '__main__':
    main()
