#!/usr/bin/env python3
"""Static, conditional agenda-effects experiments on verified CPS microdata.

The 2030/2034 labels select policy phasing and price/population scenarios. They
are NOT forecasts of current-law poverty. No legal SSN/ITIN status is imputed.
Receipt is an outcome mixture, never an average benefit assigned to everyone.
"""
import argparse
import copy
import csv
import io
import itertools
import json
import math
from array import array
from collections import Counter, defaultdict
from pathlib import Path
import zipfile
from model import credit_for_ages, service_effect, sha256, write_json
from cps_projection import read_inputs, resource_total, COMPONENTS
from current_law_ctc import parameters

HERE = Path(__file__).resolve().parent
METRICS = ('poor_rate', 'deep_poor_rate', 'below150_rate', 'child_weighted_gap_dollars')


def weighted_quantile(rows, fraction=.5):
    rows = sorted((float(v), float(w)) for v, w in rows if w > 0)
    if not rows:
        raise ValueError('empty weighted distribution')
    target = sum(w for _, w in rows)*fraction
    running = 0
    for value, weight in rows:
        running += weight
        if running >= target:
            return value
    return rows[-1][0]


def fpg(size, state):
    # HHS 2025 guidelines; used only as a source-year food-eligibility proxy.
    base, increment = (19550, 6880) if state == '02' else ((17990, 6330) if state == '15' else (15650, 5500))
    return base + increment*(size-1)


def parse_archive(archive):
    households, units, taxes, people, line_people = {}, {}, {}, {}, {}
    with zipfile.ZipFile(archive) as z:
        with z.open('hhpub26.csv') as f:
            for r in csv.DictReader(io.TextIOWrapper(f)):
                households[r['H_SEQ']] = dict(state=r['GESTFIPS'].zfill(2),
                    renter=r['H_TENURE'] == '2', weight=float(r['HSUP_WGT'])/100,
                    summer_reported=r['HESEBT_YN'] == '1', units=set(), members=0, cash=0)
        with z.open('pppub26.csv') as f:
            for r in csv.DictReader(io.TextIOWrapper(f)):
                hh, uid = r['PH_SEQ'], r['SPM_ID']
                pid, tid = hh+':'+r['PPPOS'], hh+':'+r['TAX_ID']
                if pid in people:
                    raise ValueError('duplicate person')
                h = households[hh]
                values = {k: float(r[k]) for k in COMPONENTS}
                if abs(resource_total(values)-values['SPM_RESOURCES']) > 2:
                    raise ValueError('Census resource identity failed')
                if uid not in units:
                    units[uid] = dict(values, uid=uid, hh=hh, members=[], child_ids=[],
                        weight=float(r['SPM_WEIGHT'])/100, earnings=0, wages=0,
                        care=float(r['SPM_CHILDCAREXPNS']), work=float(r['SPM_WKXPNS']),
                        deduction=float(r['SPM_CAPWKCCXPNS']),
                        hispanic=r['SPM_HHISP']=='1', race=int(r['SPM_HRACE']))
                    h['units'].add(uid)
                    h['cash'] += values['SPM_TOTVAL']
                elif any(units[uid][k] != v for k, v in values.items()):
                    raise ValueError('inconsistent repeated SPM values')
                p = dict(pid=pid, uid=uid, hh=hh, tid=tid, line=r['A_LINENO'],
                         dependent=int(r['DEP_STAT']), age=int(r['A_AGE']),
                         sex={'1':'male', '2':'female'}[r['A_SEX']],rounded_weight=float(r['MARSUPWT'])/100)
                people[pid] = p
                line_key = hh+':'+str(int(r['A_LINENO']))
                if line_key in line_people:
                    raise ValueError('duplicate household line')
                line_people[line_key] = p
                u = units[uid]
                u['members'].append(pid)
                u['earnings'] += float(r['PEARNVAL'])
                u['wages'] += float(r['WSAL_VAL'])
                h['members'] += 1
                if p['age'] < 18:
                    u['child_ids'].append(pid)
                if tid not in taxes:
                    taxes[tid] = dict(tid=tid, uid=uid, agi=0, nonrefundable=0,
                                      refundable=0, statuses=set(), child_ages=[], adult_dependents=0)
                t = taxes[tid]
                if t['uid'] != uid:
                    raise ValueError('tax unit spans SPM units')
                t['agi'] += float(r['AGI'])
                t['nonrefundable'] += float(r['CTC_CRD'])
                t['refundable'] += float(r['ACTC_CRD'])
                t['statuses'].add(r['FILESTAT'])
        children, joined = [], set()
        with z.open('asec_csv_repwgt_2026.csv') as f:
            for r in csv.DictReader(io.TextIOWrapper(f)):
                pid = r['h_seq']+':'+r['PPPOS']
                if pid in joined:
                    raise ValueError('duplicate replicate key')
                joined.add(pid)
                p = people.get(pid)
                if p is not None and p['age'] < 18:
                    p['weight'] = float(r['pwwgt0'])
                    if p['weight'] <= 0:
                        raise ValueError('positive precise child base weight required for ratio-scaled replicate analysis')
                    p['reps'] = array('d', (float(r['pwwgt'+str(i)]) for i in range(1,161)))
                    children.append(p)
    if joined != set(people):
        raise ValueError('incomplete replicate join')
    unresolved, different_return = [], 0
    for p in people.values():
        claimant = line_people.get(p['hh']+':'+str(p['dependent'])) if p['dependent'] > 0 else None
        if p['dependent'] and claimant is None:
            raise ValueError('unresolved positive claimant pointer')
        if claimant:
            target = taxes[claimant['tid']]
            if target['uid'] != p['uid']:
                raise ValueError('claimant spans SPM units')
            if p['age'] < 18:
                target['child_ages'].append(p['age'])
                different_return += p['tid'] != claimant['tid']
            else:
                target['adult_dependents'] += 1
        elif p['age'] < 18:
            unresolved.append(p['pid'])
    for t in taxes.values():
        t['filing'] = 'joint' if t['statuses'] & {'1','2','3'} else ('head' if '4' in t['statuses'] else 'other')
    four = [(u['SPM_TOTVAL'], u['weight']) for u in units.values() if len(u['members']) == 4]
    national = weighted_quantile(four)
    state_smi, fallback = {}, []
    for state in sorted({h['state'] for h in households.values()}):
        rows = [(u['SPM_TOTVAL'], u['weight']) for u in units.values()
                if len(u['members']) == 4 and households[u['hh']]['state'] == state]
        state_smi[state] = weighted_quantile(rows) if len(rows) >= 30 else national
        if len(rows) < 30:
            fallback.append(state)
    lunch_values = Counter()
    for u in units.values():
        h = households[u['hh']]
        school = sum(5 <= people[p]['age'] <= 17 for p in u['members'])
        if school and u['SPM_TOTVAL'] <= 1.3*fpg(len(u['members']), h['state']):
            embedded = 120*school if h['summer_reported'] and u['SPM_SNAPSUB'] == 0 else 0
            value = round(max(0, u['SPM_SCHLUNCH']-embedded)/school, 2)
            if value > 500:
                lunch_values[value] += 1
    if not lunch_values:
        raise ValueError('no empirical lunch valuation donors')
    lunch = lunch_values.most_common(1)[0][0]
    income_cutoffs = [weighted_quantile([(h['cash'], h['weight']) for h in households.values()], q/5) for q in range(1,5)]
    for h in households.values():
        h['quintile'] = sum(h['cash'] > cut for cut in income_cutoffs)
    child_units = {p['uid']: units[p['uid']] for p in children}
    by_unit = defaultdict(list)
    for t in taxes.values():
        if t['child_ages']:
            by_unit[t['uid']].append(t)
    return dict(units=units, child_units=child_units, households=households, taxes_by_unit=by_unit,
                people=people, children=children, smi=state_smi, lunch=lunch,
                audit=dict(people=len(people), children=len(children), spm_units=len(units),
                    tax_units=len(taxes), unresolved_child_claimants=len(unresolved),
                    child_own_return_differs=different_return, donor_lunch_value=lunch,
                    smi_national_four_person_proxy=national, smi_fallback_states=fallback))


def external_comparator(data):
    totals = [0.,0.]
    for p in data['people'].values():
        u = data['units'][p['uid']]
        before = u['SPM_RESOURCES']-u['SPM_EITC']-u['SPM_ACTC'] < u['SPM_POVTHRESHOLD']
        after = u['SPM_RESOURCES'] < u['SPM_POVTHRESHOLD']
        change = p['rounded_weight']*(before-after)
        totals[0] += change
        if p['age'] < 18:
            totals[1] += change
    # Predeclared allowance covers public-use/internal differences and rounding
    # of the published figures. No input or weight is adjusted to pass it.
    match = abs(totals[0]-6.1e6) <= .25e6 and abs(totals[1]-3.3e6) <= .15e6
    if not match:
        raise ValueError('external source-year refundable-credit comparator outside declared tolerance')
    return dict(policy='Removal of EITC + refundable ACTC only; no behavior change',
        income_year=2025,population='All persons and children under18; March2026 ages',
        public_use_people_lifted=totals[0],public_use_children_lifted=totals[1],
        published_internal_people_lifted_rounded=6.1e6,published_internal_children_lifted_rounded=3.3e6,
        absolute_tolerances=dict(all_people=250000,children=150000),passed=match,
        source='https://www2.census.gov/library/publications/2026/demo/p60-290.pdf',
        interpretation='Matched source-year element-removal validation; not independent validation of Project eligibility, delivery or future projections')


def policy_parameters(year, cfg, econ):
    cpi = econ[(year, 'cpiu')]/econ[(2025, 'cpiu')]
    anchor = cfg['index_base_year']
    anchor_cpi = 1 if anchor == 2025 else econ[(2030, 'cpiu')]/econ[(2025, 'cpiu')]
    return dict(year=year, policy_index=cpi/anchor_cpi, phaseout_threshold_index=1,
                reference_under17=parameters(year)['per_child'],
                reference_age17=parameters(year)['per_child'], age17_layer=cfg['age17_layer']), cpi, anchor_cpi


def tax_increment(tax, policy, cpi, offset):
    award = credit_for_ages(tax['child_ages'], tax['agi']*cpi, tax['filing'], policy)/cpi
    nonref = tax['nonrefundable']
    if offset == 'lower':
        nonref = max(0, nonref-500*tax['adult_dependents'])
    elif offset != 'upper':
        raise ValueError('ODC offset must be upper or lower')
    baseline = nonref+tax['refundable']
    # Preserve observed credits; receipt applies to the incremental expansion.
    return max(0, award-baseline)


def coupled_access(care, prek):
    """Shared capacity draw; explicit positive correlation, not independence."""
    cutoffs = sorted({0, care, prek, 1})
    return [(b-a, (a+b)/2 < care, (a+b)/2 < prek)
            for a,b in zip(cutoffs, cutoffs[1:]) if b > a]


def binary(probability):
    if not 0 <= probability <= 1:
        raise ValueError('probability outside [0,1]')
    return [(p, flag) for p, flag in ((1-probability, False),(probability, True)) if p > 0]


def concentrate_coverage(data, prepared, weights, coverage):
    """Put the same total coverage gap in the lowest-resource quarter.

    An aggregate sensitivity, not an SSN/ITIN assignment or a claim about any
    observed family. A fractional boundary unit preserves weighted totals.
    """
    unit_weights = Counter()
    for p,w in zip(data['children'],weights):
        unit_weights[p['uid']] += w
    quarter = sum(weights)*.25
    gap_rate = (1-coverage)/.25
    if gap_rate > 1:
        raise ValueError('concentrated sensitivity supports coverage >=75%')
    remaining = quarter
    for uid in sorted(prepared,key=lambda u:prepared[u]['base']/prepared[u]['service']['threshold']):
        weight = unit_weights[uid]
        share = min(1,max(0,remaining)/weight) if weight else 0
        prepared[uid]['coverage_override'] = 1-gap_rate*share
        remaining -= weight*share


def expected_metrics(resources, threshold, outcomes):
    if abs(sum(p for p, _ in outcomes)-1) > 1e-9:
        raise ValueError('outcome probabilities do not sum to one')
    result = [0.0]*5
    for probability, delta in outcomes:
        value = resources+delta
        indicators = (value < threshold, value < .5*threshold, value < 1.5*threshold,
                      max(0, threshold-value))
        for i, indicator in enumerate(indicators):
            result[i] += probability*indicator
        result[4] += probability*delta
    return result


def prepare_units(data, year, cfg, pop, econ):
    policy, cpi, anchor_cpi = policy_parameters(year, cfg, econ)
    eligible_hh = set()
    for hid, h in data['households'].items():
        if not h['members']:
            continue
        smi = data['smi'][h['state']]*math.sqrt(h['members']/4)*cfg['smi_scale']
        assisted = any(data['units'][uid]['SPM_CAPHOUSESUB'] > 0 for uid in h['units'])
        if h['renter'] and not assisted and h['cash'] <= .3*smi:
            eligible_hh.add(hid)
    eligible_weight = sum(data['households'][hid]['weight'] for hid in eligible_hh)
    award_cap = 100000*min(4, year-2029)
    award_probability = min(1, award_cap/eligible_weight) if eligible_weight else 0
    emergency_budget = cfg['emergency_cash_budget_2030'] if year <= 2031 else 0
    emergency_probability = min(1, emergency_budget/(eligible_weight*cfg['emergency_grant_2025_dollars'])) if eligible_weight else 0
    prepared = {}
    for uid, u in data['child_units'].items():
        h = data['households'][u['hh']]
        ages = [data['people'][pid]['age'] for pid in u['child_ids']]
        school = sum(5 <= age <= 17 for age in ages)
        under13 = sum(age < 13 for age in ages)
        prek_n = sum(age in (3,4) for age in ages)
        adults = len(u['members'])-len(ages)
        share = len(u['members'])/h['members']
        income = max(0, u['SPM_TOTVAL'])
        smi = data['smi'][h['state']]*math.sqrt(len(u['members'])/4)*cfg['smi_scale']
        summer_eligible = income <= 1.85*fpg(len(u['members']),h['state']) or u['SPM_SNAPSUB'] > 0
        summer_old = 120*school if h['summer_reported'] else 0
        embedded = summer_old if u['SPM_SNAPSUB'] == 0 else 0
        lunch_old = max(0, u['SPM_SCHLUNCH']-embedded)
        lunch_new = data['lunch']*school
        lunch_delta = max(0,lunch_new-lunch_old)*(cfg['school_2030_fraction'] if year == 2030 else 1)
        summer_new = cfg['summer_monthly_nominal']/anchor_cpi*cfg['summer_months']*school if summer_eligible else 0
        summer_delta = max(0,summer_new-summer_old)*(cfg['summer_2030_fraction'] if year == 2030 else 1)
        housing_cap = max(0,cfg['housing_threshold_share']*u['SPM_POVTHRESHOLD']-.3*income-u['SPM_CAPHOUSESUB'])
        service = dict(resources=u['SPM_RESOURCES'], threshold=u['SPM_POVTHRESHOLD'],
            childcare_expense=u['care'], work_expense=u['work'], work_care_deduction=u['deduction'],
            care_family_income=income, state_median_income=smi,
            care_need_eligible=bool(under13 and u['care'] > 0), prek_eligible=bool(prek_n),
            prek_spm_reduction=u['care']*cfg['prek_expense_fraction']*prek_n/max(1,under13),
            school_meal_spm_delta=lunch_delta, summer_ebt_spm_delta=summer_delta,
            voucher_eligible=u['hh'] in eligible_hh, voucher_awarded=u['hh'] in eligible_hh,
            voucher_spm_delta=housing_cap, housing_increment_cap=housing_cap,
            emergency_aid_eligible=u['hh'] in eligible_hh, emergency_aid_awarded=u['hh'] in eligible_hh,
            emergency_aid_spm_delta=cfg['emergency_grant_2025_dollars']*share, delivery={})
        increment = sum(tax_increment(t,policy,cpi,cfg['odc_offset']) for t in data['taxes_by_unit'][uid])
        if cfg['unassigned_children'] == 'include_proxy':
            assigned = sum(len(t['child_ages']) for t in data['taxes_by_unit'][uid])
            if assigned < len(ages):
                unmatched = [data['people'][p]['age'] for p in u['child_ids'] if data['people'][p]['dependent'] == 0]
                increment += credit_for_ages(unmatched,income*cpi,'other',policy)/cpi
        levy = (cfg['employee_leave_rate']+cfg['employer_leave_incidence'])*u['wages']
        carbon = 0
        if cfg['include_carbon_proxy']:
            dividend = (197 if year == 2030 else 454)/cpi*adults
            cost_2035 = [458,646,818,1070,1713][h['quintile']]
            fee_ratio = (25 if year == 2030 else 68)/79*(1.022**(2035-year))
            carbon = dividend-cost_2035*fee_ratio*share
        prepared[uid] = dict(service=service, ctc=increment,
            base=u['SPM_RESOURCES']+cfg['baseline_resource_shift']*u['SPM_POVTHRESHOLD'],
            cost=-levy+carbon+cfg['health_moop_reduction']*u['SPM_MEDXPNS'],
            voucher_probability=award_probability if u['hh'] in eligible_hh else 0,
            emergency_probability=emergency_probability if u['hh'] in eligible_hh else 0)
    return prepared, dict(eligible_households_weighted=eligible_weight,
        expected_awarded_households=eligible_weight*award_probability, award_cap=award_cap,
        expected_emergency_cash_all_households=eligible_weight*emergency_probability*cfg['emergency_grant_2025_dollars'],
        allocation='Random across proxy-eligible households, including adult-only households; conditional outcome mixture')


def unit_effect(prepared, year, delivery, stage):
    s = prepared['service']
    if stage == 'baseline':
        return expected_metrics(prepared['base'],s['threshold'],[(1,0)])
    credit_p = prepared.get('coverage_override',delivery['coverage'])*delivery['ctc_receipt']
    access = coupled_access(delivery['care_'+str(year)] if stage >= 2 else 0,
                            delivery['prek_'+str(year)] if stage >= 2 else 0)
    food = binary(delivery['food_receipt'] if stage >= 3 else 0)
    voucher = binary(prepared['voucher_probability']*delivery['voucher_leaseup'] if stage >= 4 else 0)
    emergency = binary(prepared['emergency_probability'] if stage >= 4 else 0)
    outcomes = []
    for (pc, credit), (pa, care, prek), (pf, foods), (pv, v), (pe, e) in itertools.product(binary(credit_p),access,food,voucher,emergency):
        probability = pc*pa*pf*pv*pe
        if not probability:
            continue
        s['delivery']['analysis'] = dict(care=care,prek=prek,school_meal=foods,summer_ebt=foods,voucher=v,emergency_aid=e)
        gain = service_effect(s,year,'analysis')
        amount = prepared['ctc']*credit+gain['cash']+gain['expense_reduction']+gain['in_kind']
        if stage >= 5:
            amount += prepared['cost']
        outcomes.append((probability,amount))
    return expected_metrics(prepared['base'],s['threshold'],outcomes)


def aggregate(data, effects, weights, base_effects=None, intervals=True):
    children = data['children']
    total = sum(weights)
    vectors = [[effects[p['uid']][m] for p in children] for m in range(4)]
    sums = [sum(w*x for w,x in zip(weights,v)) for v in vectors]
    point = dict(zip(METRICS,[sums[0]/total,sums[1]/total,sums[2]/total,sums[3]]))
    point.update(weighted_children=total, poor_children=sums[0], deep_poor_children=sums[1],
                 below150_children=sums[2], unweighted_children=len(children))
    if base_effects:
        point['poor_children_lifted'] = sum(w*base_effects[p['uid']][0]*(1-effects[p['uid']][0])
                                           for p,w in zip(children,weights))
        point['children_newly_poor'] = sum(w*(1-base_effects[p['uid']][0])*effects[p['uid']][0]
                                          for p,w in zip(children,weights))
    if len(next(iter(effects.values()))) > 4:
        point['mean_unit_resource_gain_per_child_not_fiscal_cost'] = sum(
            w*effects[p['uid']][4] for p,w in zip(children,weights))/total
    if not intervals:
        return point
    base_vector = [base_effects[p['uid']][0] for p in children] if base_effects else vectors[0]
    base_rate = sum(w*x for w,x in zip(weights,base_vector))/total
    deviations = [0.,0.,0.,0.]
    for i in range(160):
        wr = [p['reps'][i]*w/p['weight'] if p['weight'] else 0 for p,w in zip(children,weights)]
        den = sum(wr)
        if den <= 0:
            raise ValueError('zero-weight replicate')
        poor = sum(w*x for w,x in zip(wr,vectors[0]))/den
        deep = sum(w*x for w,x in zip(wr,vectors[1]))/den
        baseline = sum(w*x for w,x in zip(wr,base_vector))/den
        deviations[0] += (poor-point['poor_rate'])**2
        deviations[1] += (deep-point['deep_poor_rate'])**2
        deviations[2] += ((poor-baseline)-(point['poor_rate']-base_rate))**2
        deviations[3] += (poor*den-point['poor_children'])**2
    se = [math.sqrt(4/160*x) for x in deviations]
    point['sampling_uncertainty'] = dict(
        poor_rate=dict(se=se[0],lower95=max(0,point['poor_rate']-1.96*se[0]),upper95=min(1,point['poor_rate']+1.96*se[0])),
        deep_poor_rate=dict(se=se[1]), poor_children=dict(se=se[3]),
        paired_poor_rate_change=dict(estimate=point['poor_rate']-base_rate,se=se[2],
            lower95=point['poor_rate']-base_rate-1.96*se[2],upper95=point['poor_rate']-base_rate+1.96*se[2]),
        method='CPS SDR; conditional on fixed proxies, allocation probabilities and external growth ratios; excludes model uncertainty')
    return point


def subgroups(data, effects, weights):
    buckets = defaultdict(lambda: defaultdict(list))
    for p,w in zip(data['children'],weights):
        u = data['units'][p['uid']]
        n_kids = len(u['child_ids'])
        labels = dict(age='Under 6' if p['age'] < 6 else '6–17',
            adults='One adult' if len(u['members'])-n_kids == 1 else 'Multiple/no adults',
            earnings='No positive earnings' if u['earnings'] <= 0 else 'Positive earnings',
            children='3+ children' if n_kids >= 3 else '1–2 children',
            tenure='Renter' if data['households'][p['hh']]['renter'] else 'Owner/other',
            head_race_ethnicity='Hispanic head' if u['hispanic'] else {1:'White non-Hispanic head',2:'Black non-Hispanic head',4:'Asian non-Hispanic head'}.get(u['race'],'Other non-Hispanic head'))
        for group,label in labels.items():
            buckets[group][label].append((w,effects[p['uid']]))
    output = {}
    for group, groups in buckets.items():
        output[group] = {}
        for label, rows in groups.items():
            den = sum(w for w,_ in rows)
            poor = sum(w*e[0] for w,e in rows)
            output[group][label] = dict(unweighted_children=len(rows),weighted_children=den,
                poor_children=poor,poor_rate=poor/den if len(rows)>=30 and den else None,
                deep_poor_rate=sum(w*e[1] for w,e in rows)/den if len(rows)>=30 and den else None,
                residual_share=None)
    poor_total = sum(w*effects[p['uid']][0] for p,w in zip(data['children'],weights))
    for groups in output.values():
        for record in groups.values():
            record['residual_share'] = record['poor_children']/poor_total if poor_total else 0
    return output


def validate_assumptions(spec):
    for values in spec['scenarios'].values():
        for name in ('coverage','ctc_receipt','care_2030','care_2034','prek_2030','prek_2034','food_receipt','voucher_leaseup'):
            if not isinstance(values.get(name),(int,float)) or not math.isfinite(values[name]) or not 0 <= values[name] <= 1:
                raise ValueError('invalid scenario probability: '+name)
    cfg = spec['common']
    if cfg['index_base_year'] not in (2025,2030) or cfg['unassigned_children'] not in ('exclude','include_proxy'):
        raise ValueError('unsupported legacy/index/claimant convention')
    if cfg['smi_scale'] <= 0 or not 0 <= cfg['prek_expense_fraction'] <= 1:
        raise ValueError('invalid SMI/pre-K assumption')


def run(archive, assumptions, output):
    data = parse_archive(archive)
    comparator = external_comparator(data)
    pop, econ, input_hashes = read_inputs(HERE/'empirical')
    spec = json.loads(Path(assumptions).read_text())
    validate_assumptions(spec)
    cases, sensitivity_results = [], []
    for year in (2030,2034):
        common = copy.deepcopy(spec['common'])
        prepared, awards = prepare_units(data,year,common,pop,econ)
        weights = [p['weight']*pop[(year,p['age'],p['sex'])]/pop[(2026,p['age'],p['sex'])] if common['demographic_growth'] else p['weight'] for p in data['children']]
        baseline_effects = {u:unit_effect(v,year,{},'baseline') for u,v in prepared.items()}
        baseline = aggregate(data,baseline_effects,weights)
        for name,delivery in spec['scenarios'].items():
            stages = []
            for stage,label in enumerate(('CTC','CTC + care/pre-K','+ school/summer food','+ scarce vouchers','+ employee leave contribution'),1):
                effects = {u:unit_effect(v,year,delivery,stage) for u,v in prepared.items()}
                result = aggregate(data,effects,weights,baseline_effects,intervals=stage in (1,5))
                stages.append(dict(stage=stage,label=label,**result))
            full = spec['scenarios']['full']
            full_effects = {u:unit_effect(v,year,full,5) for u,v in prepared.items()}
            residual_floor = sum(w*full_effects[p['uid']][0] for p,w in zip(data['children'],weights))
            cases.append(dict(year=year,scenario=name,assumptions=delivery,baseline=baseline,
                stages=stages,award_checks=dict(awards,expected_leased_households=awards['expected_awarded_households']*delivery['voucher_leaseup']),
                residual=dict(poor_even_with_full_modeled_receipt=residual_floor,
                    additional_poor_under_selected_delivery=stages[-1]['poor_children']-residual_floor,
                    interpretation='Ordered scenario comparison, not an estimated causal attribution; food/care eligibility and scarce voucher allocation remain fixed'),
                subgroups=subgroups(data,effects,weights)))
            print(f'{year} {name}: {stages[-1]["poor_rate"]:.4%}',flush=True)
        variations = {
            'resources_minus_5pct_threshold':dict(baseline_resource_shift=-.05),
            'resources_plus_5pct_threshold':dict(baseline_resource_shift=.05),
            'index_from_2025':dict(index_base_year=2025),
            'retain_adult_ODC_bound':dict(odc_offset='lower'),
            'age17_retained_layer':dict(age17_layer='retained_reference'),
            'resolve_unassigned_proxy':dict(unassigned_children='include_proxy'),
            'SMI_minus_25pct':dict(smi_scale=.75), 'SMI_plus_25pct':dict(smi_scale=1.25),
            'preK_expense_share_25pct':dict(prek_expense_fraction=.25),
            'preK_expense_share_75pct':dict(prek_expense_fraction=.75),
            'employee_leave_upper_rate':dict(employee_leave_rate=.00425),
            'employer_leave_fully_wage_borne':dict(employer_leave_incidence=.003),
            'carbon_dividend_and_cost_proxy':dict(include_carbon_proxy=True),
            'health_MOOP_minus_15pct':dict(health_moop_reduction=.15),
            'health_MOOP_minus_30pct':dict(health_moop_reduction=.30),
            'carbon_plus_health15pct':dict(include_carbon_proxy=True,health_moop_reduction=.15),
            'carbon_plus_health30pct':dict(include_carbon_proxy=True,health_moop_reduction=.30),
            'temporary_cash_10B':dict(emergency_cash_budget_2030=1e10),
            'full_year_food_2030':dict(school_2030_fraction=1,summer_2030_fraction=1),
            'fixed_source_population':dict(demographic_growth=False)}
        variations['coverage_gap_in_lowest_resource_quarter'] = dict(coverage_pattern='low_resource_quarter')
        for label,changes in variations.items():
            cfg = dict(common,**changes)
            ps, check = prepare_units(data,year,cfg,pop,econ)
            ws = weights if cfg['demographic_growth'] else [p['weight'] for p in data['children']]
            if cfg.get('coverage_pattern') == 'low_resource_quarter':
                concentrate_coverage(data,ps,ws,spec['scenarios']['moderate']['coverage'])
            base = {u:unit_effect(v,year,{},'baseline') for u,v in ps.items()}
            ef = {u:unit_effect(v,year,spec['scenarios']['moderate'],5) for u,v in ps.items()}
            sensitivity_results.append(dict(year=year,name=label,changes=changes,
                baseline=aggregate(data,base,ws,intervals=False),result=aggregate(data,ef,ws,base,intervals=False),award_checks=check))
    source_effects = {u:[float(v['SPM_RESOURCES']<v['SPM_POVTHRESHOLD']),
                        float(v['SPM_RESOURCES']<.5*v['SPM_POVTHRESHOLD']),
                        float(v['SPM_RESOURCES']<1.5*v['SPM_POVTHRESHOLD']),
                        max(0,v['SPM_POVTHRESHOLD']-v['SPM_RESOURCES'])] for u,v in data['child_units'].items()}
    source = aggregate(data,source_effects,[p['weight'] for p in data['children']],intervals=False)
    if abs(source['poor_rate']-.1339131451759891)>1e-9:
        raise ValueError('source-year child baseline changed')
    result = dict(model='Project2050-child-poverty-static-agenda-v1',status='CONDITIONAL_SCENARIOS_NOT_FORECAST',
        project_base=spec['source_base'], source_income_year=2025,survey_year=2026,dollar_year=2025,
        archive_sha256=sha256(archive),assumptions_sha256=sha256(assumptions),official_input_hashes=input_hashes,
        source_audit=data['audit'],source_baseline=source,external_comparator=comparator,
        cases=cases,sensitivities=sensitivity_results,
        scope='Joint FAM-1A/FAM-2A/EDU-3A/HOU-4A with FAM-3 employee cost; optional HOU-1, carbon and health proxy sensitivities. Not all Project2050 household/fiscal effects.',
        limitations=['Conditional legal coverage, receipt and usable service assumptions are not estimated probabilities',
            'Frozen source-year resources and credits; no comprehensive target-year current-law tax/transfer forecast',
            'SPM-age and family-size/SMI/enrollment/waitlist/ODC proxies; birth, custody and legal qualification unresolved',
            'Baseline credits preserved; no recapture or repayment-loss model',
            'No employment, inflation, long-run child-development or hardship response',
            'Housing awards use households and include adult-only households; allocation and valuation uncertainty excluded from SDR',
            'Breakfast, public-service quality and housing construction have no assigned immediate SPM cash value',
            'SPM resource deltas are not federal cost or social value; D3/D4 remain separate'])
    write_json(output,result)
    return result


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--archive',required=True)
    parser.add_argument('--assumptions',default=HERE/'agenda-assumptions.json')
    parser.add_argument('--output',required=True)
    args = parser.parse_args()
    run(args.archive,args.assumptions,args.output)
