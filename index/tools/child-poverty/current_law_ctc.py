#!/usr/bin/env python3
"""Schedule-8812 arithmetic with supplied, reviewed eligibility and tax limits.

This is a bounded credit worksheet, not an income-tax calculator or a CPS
eligibility imputer. CBO's target-year parameters are projections, not IRS
announcements of future indexed amounts. CTC and ODC remain combined where the
form combines them; do not import that total as model.current_law_ctc.
"""
import csv
import math
from pathlib import Path
from model import num, integer

PARAMETERS = Path(__file__).resolve().parent / "empirical/cbo-ctc-parameters-2026-02.csv"


def parameters(year, path=PARAMETERS):
    rows = list(csv.DictReader(Path(path).read_text().splitlines()))
    values = {r['variable'].removeprefix('tp_ctc_'): float(r['value'])
              for r in rows if r['date'] == 'CY' + str(year)}
    if set(values) != {'per_child', 'per_other_dependent', 'max_refundable', 'refund_threshold', 'refund_rate'}:
        raise ValueError('supported parameter years: 2025, 2030, 2034')
    return values


def calculate(case, year):
    """Use reviewed Schedule 8812 line inputs; return a combined credit ledger.

    qualifying_children and other_dependents must already satisfy statutory
    age, relationship, support, residence and identification requirements.
    credit_limit is Worksheet A's result, NOT gross federal tax before credits.
    payroll_alternative is reviewed max(0, line23-line24), not raw CPS FICA.
    Form2555 and Puerto Rico cases require a separate reviewed implementation.
    """
    for field in ('eligibility_review', 'credit_limit_review'):
        if not isinstance(case.get(field), str) or not case[field].strip():
            raise ValueError(field + ' required')
    if case.get('special_case') != 'none':
        raise ValueError('explicit special_case=none required; unsupported special return')
    if case.get('filing_status') not in ('joint', 'single', 'head', 'separate', 'widow'):
        raise ValueError('filing_status required')
    children = integer(case.get('qualifying_children'), 'qualifying_children', 0, 30)
    others = integer(case.get('other_dependents'), 'other_dependents', 0, 30)
    magi = num(case.get('modified_agi'), 'modified_agi')
    earned = num(case.get('earned_income'), 'earned_income')
    limit = num(case.get('credit_limit'), 'credit_limit', 0)
    p = parameters(year)
    maximum = children * p['per_child'] + others * p['per_other_dependent']
    threshold = 400000 if case['filing_status'] == 'joint' else 200000
    reduction = math.ceil(max(0, magi-threshold)/1000) * 50
    remaining = max(0, maximum-reduction)
    nonrefundable = min(remaining, limit)
    refundable_limit = min(max(0, remaining-nonrefundable), children*p['max_refundable'])
    earned_route = max(0, earned-p['refund_threshold'])*p['refund_rate']/100
    route = earned_route
    if children >= 3 and earned_route < refundable_limit:
        if not case.get('payroll_alternative_review'):
            raise ValueError('three-child payroll alternative and review required')
        route = max(route, num(case.get('payroll_alternative'), 'payroll_alternative', 0))
    refundable = min(refundable_limit, route)
    return {'year': year, 'parameter_basis': 'CBO February 2026 current-law parameter vintage',
            'maximum_ctc_and_odc': maximum, 'phaseout_reduction': reduction,
            'nonrefundable_ctc_and_odc': nonrefundable, 'refundable_actc': refundable,
            'combined_credit': nonrefundable+refundable,
            'ctc_only_allocation': None,
            'scope': 'Conditional worksheet arithmetic; no CPS claimant assignment or tax-liability recomputation'}
