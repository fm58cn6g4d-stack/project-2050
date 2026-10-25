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


def claim_split(allowed, remaining_deductible, qmb=False):
    """Illustrative assigned FFS 80/20 claim, not actual adjudication.
    Other coverage and state-payment amounts are unknown; QMB cannot be billed.
    """
    if allowed is None or remaining_deductible is None:
        return dict(medicare=None, patient=None, non_medicare_share=None)
    if allowed < 0 or remaining_deductible < 0:
        raise ValueError('Negative allowed amount or deductible')
    deductible = min(allowed, remaining_deductible)
    medicare = .8 * (allowed - deductible)
    share = allowed - medicare
    return dict(medicare=medicare, patient=0.0 if qmb else share,
                non_medicare_share=share)


def payer_route(enrollment, adjusted=False, existing_obligation=False,
                significance='unknown', overlap_known=False):
    """Boundary experiment under the packet's assumptions, not a payer decision.
    A nominal supplemental allowance does not establish a residual claim amount.
    """
    if enrollment not in ('FFS', 'MA'):
        raise ValueError('Unknown enrollment type')
    if significance not in ('unknown', 'significant', 'nonsignificant'):
        raise ValueError('Unknown determination')
    if enrollment == 'FFS':
        return 'FFS'
    if adjusted or existing_obligation or significance == 'nonsignificant':
        return 'MA'
    if significance == 'significant' and overlap_known:
        return 'FFS'
    return 'unresolved'


def hcbs_split(eligible_spending, base_match, increase, separate_grants):
    """Illustrative separate service/grant resource pools; not a matching ruling."""
    if any(v is None for v in (eligible_spending, base_match, increase, separate_grants)):
        return dict(federal=None, state=None, resources=None)
    if min(eligible_spending, base_match, increase, separate_grants) < 0 or base_match + increase > 1:
        raise ValueError('Invalid expenditure or match assumptions')
    federal = (base_match + increase) * eligible_spending + separate_grants
    state = (1 - base_match - increase) * eligible_spending
    return dict(federal=federal, state=state, resources=eligible_spending + separate_grants)


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
    claims = [dict(case=name, allowed=allowed, remaining_deductible=deductible, qmb=qmb,
                   **claim_split(allowed, deductible, qmb))
              for name, allowed, deductible, qmb in [
                  ('ordinary_after_deductible', 1000.0, 0.0, False),
                  ('ordinary_100_remaining', 1000.0, 100.0, False),
                  ('QMB_100_remaining', 1000.0, 100.0, True),
                  ('unknown_allowed_amount', None, 100.0, False)]]
    match_example = hcbs_split(100.0, .60, .10, 10.0)
    assert abs(match_example['federal'] + match_example['state'] - match_example['resources']) < 1e-10
    with (ROOT / 'sources/health-restoration-remedy-cohorts.csv').open() as f:
        cohorts = list(csv.DictReader(f))
    with (ROOT / 'sources/health-enrollment-work-map.csv').open() as f:
        enrollment = list(csv.DictReader(f))
    assert len({x['cohort'] for x in cohorts}) == len(cohorts)
    assert len({x['category'] for x in enrollment}) == len(enrollment)
    for x in cohorts:
        date.fromisoformat(x['baseline_effective_date'])
    files = ['index/tools/fiscal-model.py' , 'index/tools/calendar/model.py',
             'index/tools/capacity-funding.py', 'index/data/fiscal-baseline.csv',
             'index/data/inputs/ledger-bills.csv', 'index/data/inputs/fiscal-profiles.csv',
             'index/data/inputs/fiscal-years.csv', 'index/data/inputs/fiscal-components.csv', 'index/data/inputs/calendar-scenarios.json',
             'index/data/inputs/capacity-funding.csv',
             'sources/health-cms-implementation-cost-register.csv',
             'index/tools/health/decision_analysis.py',
             'index/tools/health/test_decision_analysis.py',
             'sources/health-restoration-remedy-cohorts.csv',
             'sources/health-enrollment-work-map.csv']
    return dict(source_commit='846be172efdc0c383d5d8c24194de3704a1cbaa1',
                status='Research calculations; unit sensitivities, not health cost estimates',
                unit='billions of nominal dollars unless specified',
                unit_unfinanced_2030_cost_debt={str(y): unit_2030[y] for y in (2030, 2039, 2040, 2056)},
                unit_setup_shift_2030_to_2029_debt={str(y): unit_shift[y] for y in (2029, 2030, 2039, 2040, 2056)},
                maturity_headroom_2040_bn=headroom[0], maturity_binding_year=headroom[1],
                maturity_headroom_basis='Signed margin for recurring GF stream from 2040 growing with GDP; negative is an existing funding gap; conditional on old surge proxy; not financing',
                calendar=calendar, surge=surge,
                packages=[dict(id=x['work_package'], net_increment_bn=None, fy2029_cash_bn=None) for x in packages],
                payment_cases=overlap_cases, actual_benefit_cost=None,
                normalized_claim_examples=claims,
                normalized_claim_examples_unit='illustrative dollars per assigned claim, not billions; not price estimates',
                normalized_hcbs_example=match_example,
                normalized_hcbs_assumptions=dict(eligible_spending=100.0, base_match=.60, increase=.10, separate_grants=10.0, unit='illustrative currency units; not 2029 assumptions'),
                remedy_cohort_count=len(cohorts), enrollment_category_count=len(enrollment),
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
              f"Under the **old surge cash proxy**, DEC's signed maturity margin is **${r['maturity_headroom_2040_bn']:.3f}B in FY2040-equivalent terms** for a recurring GF stream growing with GDP (binding year {r['maturity_binding_year']}). A negative value is an existing financing gap, not spare headroom; the October 24 family adoption is included in the current fiscal inputs. This threshold runs through 2056 and is neither available financing nor a score or permission to spend. Price further permanent costs and close the gap before claiming D4 compliance.", '',
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
    lines += ['', '## Selected-specification accounting examples', '',
              'Illustrative dollars per assigned covered FFS claim. These assume the payer map and eligibility are already resolved; $1,000 is not a device-price estimate. Other coverage is omitted. For QMBs, the non-Medicare share is not collectible from the patient; this does not imply that Medicaid pays all of it or that Medicare pays more.', '',
              '| Case | Allowed | Remaining deductible | Medicare | Patient before other coverage (QMB protection applied) | Non-Medicare share |',
              '| --- | ---: | ---: | ---: | ---: | ---: |']
    for c in r['normalized_claim_examples']:
        def show(v): return 'unpriced' if v is None else f'{v:.2f}'
        lines.append('| '+c['case']+' | '+' | '.join(show(c[k]) for k in ('allowed','remaining_deductible','medicare','patient','non_medicare_share'))+' |')
    h = r['normalized_hcbs_example']
    lines += ['', f"HCBS accounting illustration only: 100 units of eligible services at an assumed 60% base match plus 10 percentage points, and 10 units of **separate** grant-funded work, give federal {h['federal']:.1f}, state {h['state']:.1f}, total resources {h['resources']:.1f}. None of those rates/amounts is a selected 2029 assumption. Match contributions are shares of the 100 service units, not additional resources on top; the 10 grant units must cover separate costs. An invoice cannot occupy both pools.", '',
              f"The authored work maps contain {r['remedy_cohort_count']} OBBBA coverage/tax baseline cohorts and {r['enrollment_category_count']} enrollment categories. Dates are statutory baseline triggers, not observed loss dates or headcounts. Their complete source hashes are in the JSON. The mapped cohorts do not claim to exhaust every health-cut provision. Historical lookbacks identify people for streamlined current-coverage restoration, not a general cut-period medical-claims payment program; normal restored application rules, separate tax questions and possible medical-debt relief have distinct scopes.", '',
              'Focused boundary tests: `python3 index/tools/health/test_decision_analysis.py`. The payer function tests assumptions and unresolved branches; it does not certify a real claim, significant-cost determination or supplier authority.']
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
