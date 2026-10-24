#!/usr/bin/env python3
"""Audit CPS tax/SPM links and run a clearly bounded demographic sensitivity.

Not a 2030/2034 current-law forecast. Real resources and within-cell poverty
patterns are held fixed. CBO Social Security-area growth ratios are applied to
observed CPS age/sex cells, without asserting equal population universes.
"""
import argparse
import csv
import io
from collections import Counter, defaultdict
from pathlib import Path
import zipfile
from model import poverty_metrics, replicate_intervals, sha256, write_json
from current_law_ctc import parameters

HERE = Path(__file__).resolve().parent
COMPONENTS = ('SPM_TOTVAL', 'SPM_SNAPSUB', 'SPM_CAPHOUSESUB', 'SPM_SCHLUNCH',
              'SPM_WICVAL', 'SPM_ENGVAL', 'SPM_FEDTAX', 'SPM_STTAX', 'SPM_FICA',
              'SPM_CAPWKCCXPNS', 'SPM_CHILDSUPPD', 'SPM_MEDXPNS', 'SPM_RESOURCES',
              'SPM_POVTHRESHOLD', 'SPM_ACTC', 'SPM_EITC')


def resource_total(unit):
    return (unit['SPM_TOTVAL'] + sum(unit[k] for k in COMPONENTS[1:6])
            - sum(unit[k] for k in COMPONENTS[6:12]))


def claimant_record(key, person, lines):
    pointer = int(person['DEP_STAT'])
    claimant = lines.get((key[0], str(pointer))) if pointer > 0 else None
    return {'person_id': ':'.join(key), 'age_at_survey': person['age'],
            'own_census_tax_unit_id': ':'.join(person['tax_id']),
            'census_claimant_line': pointer or None,
            'census_claimant_tax_unit_id': ':'.join(claimant['tax_id']) if claimant else None,
            'status': 'Census tax-model pointer; legal eligibility not established' if claimant
                      else 'Unresolved; no claimant assigned'}


def read_cps(archive):
    people, lines, units, taxes, children = {}, {}, {}, defaultdict(list), {}
    tax_to_spm = defaultdict(set)
    with zipfile.ZipFile(archive) as z:
        with z.open('pppub26.csv') as f:
            for raw in csv.DictReader(io.TextIOWrapper(f)):
                key = (raw['PH_SEQ'], raw['PPPOS'])
                line = (raw['PH_SEQ'], raw['A_LINENO'])
                if key in people or line in lines:
                    raise ValueError('duplicate person or household-line key')
                uid = raw['SPM_ID']
                tid = (raw['PH_SEQ'], raw['TAX_ID'])
                values = {k: float(raw[k]) for k in COMPONENTS}
                if uid in units and units[uid] != values:
                    raise ValueError('inconsistent repeated SPM components')
                units[uid] = values
                person = {k: raw[k] for k in ('DEP_STAT', 'FILESTAT', 'A_LINENO', 'A_SPOUSE')}
                person.update(tax_id=tid, unit_id=uid, age=int(raw['A_AGE']),
                              ctc_odc=float(raw['CTC_CRD']), actc=float(raw['ACTC_CRD']),
                              eitc=float(raw['EIT_CRED']), fedtax=float(raw['FEDTAX_AC']))
                people[key] = person
                lines[line] = person
                taxes[tid].append(person)
                tax_to_spm[tid].add(uid)
                if person['age'] < 18:
                    children[key] = {'age': person['age'],
                                     'sex': {'1': 'male', '2': 'female'}[raw['A_SEX']],
                                     'resources': values['SPM_RESOURCES'],
                                     'threshold': values['SPM_POVTHRESHOLD']}
        joined = set()
        with z.open('asec_csv_repwgt_2026.csv') as f:
            for raw in csv.DictReader(io.TextIOWrapper(f)):
                key = (raw['h_seq'], raw['PPPOS'])
                if key in joined:
                    raise ValueError('duplicate replicate key')
                joined.add(key)
                if key in children:
                    children[key].update(person_weight=float(raw['pwwgt0']),
                        replicate_weights=[float(raw['pwwgt'+str(i)]) for i in range(1, 161)])
    if joined != set(people):
        raise ValueError('person/replicate key sets differ')
    links = Counter()
    crosswalk = []
    for key, p in people.items():
        if p['age'] < 18:
            crosswalk.append(claimant_record(key, p, lines))
        if int(p['DEP_STAT']) > 0:
            target = lines.get((key[0], str(int(p['DEP_STAT']))))
            links['dependent_pointers'] += 1
            links['missing_claimant_line'] += target is None
            if target is not None:
                links['claimant_in_other_tax_unit'] += p['tax_id'] != target['tax_id']
                links['claimant_in_other_spm_unit'] += p['unit_id'] != target['unit_id']
        elif p['age'] < 18:
            links['children_without_positive_dependent_pointer'] += 1
    links['children_with_claimant_in_other_tax_unit'] = sum(
        bool(r['census_claimant_tax_unit_id']) and
        r['census_claimant_tax_unit_id'] != r['own_census_tax_unit_id'] for r in crosswalk)
    sums = defaultdict(lambda: defaultdict(float))
    for p in people.values():
        for k in ('actc', 'eitc', 'fedtax'):
            sums[p['unit_id']][k] += p[k]
    def reconciliation(observed, target):
        differences = [abs(sums[u][observed]-v[target]) for u, v in units.items()]
        return {'units_with_difference_over_2_dollars': sum(d > 2 for d in differences),
                'max_absolute_difference': max(differences)}
    gaps = [abs(resource_total(u)-u['SPM_RESOURCES']) for u in units.values()]
    if max(gaps) > 2 or any(len(v) != 1 for v in tax_to_spm.values()):
        raise ValueError('SPM resource identity or tax/SPM containment failed')
    audit = {'people': len(people), 'children': len(children), 'spm_units': len(units),
             'tax_units': len(taxes), 'tax_units_spanning_spm_units': 0,
             'dependent_links': dict(links),
             'resource_identity': {'units_reconciled_within_2_dollars': len(units),
                                   'max_absolute_difference': max(gaps)},
             'actc_reconciliation': reconciliation('actc', 'SPM_ACTC'),
             'eitc_reconciliation': reconciliation('eitc', 'SPM_EITC'),
             'after_credit_federal_tax_reconciliation': reconciliation('fedtax', 'SPM_FEDTAX'),
             'ctc_odc_combined_nonrefundable_positive_tax_units': sum(
                 any(p['ctc_odc'] > 0 for p in ps) for ps in taxes.values()),
             'identification_status': 'SSN/ITIN and legal qualifying-child status not observed',
             'ctc_only_allocation_status': 'Not inferred from combined CTC_CRD'}
    return list(children.values()), audit, crosswalk


def read_inputs(directory):
    pop = defaultdict(float)
    pop_path = directory/'cbo-child-population-2026-01.csv'
    seen = set()
    for r in csv.DictReader(pop_path.read_text().splitlines()):
        key = (int(r['year']), int(r['age']), r['sex'], r['marital'])
        if key in seen or r['marital'] not in ('divorced', 'married', 'single', 'widowed'):
            raise ValueError('duplicate or unsupported population cell')
        seen.add(key)
        pop[(int(r['year']), int(r['age']), r['sex'])] += float(r['number_of_people'])
    expected = {(y, a, s) for y in (2026, 2030, 2034) for a in range(18) for s in ('male', 'female')}
    if set(pop) != expected or len(seen) != 4*len(expected) or any(v <= 0 for v in pop.values()):
        raise ValueError('complete, positive single-age/sex population cells required')
    econ_path = directory/'cbo-calendar-factors-2026-02.csv'
    econ = {(int(r['date']), r['variable']): float(r['value'])
            for r in csv.DictReader(econ_path.read_text().splitlines())}
    return pop, econ, {p.name: sha256(p) for p in (pop_path, econ_path,
                         directory/'cbo-ctc-parameters-2026-02.csv')}


def sensitivity(children, population, year):
    factors = {(a, s): population[(year, a, s)]/population[(2026, a, s)]
               for a in range(18) for s in ('male', 'female')}
    projected = []
    for r in children:
        factor = factors[(r['age'], r['sex'])]
        projected.append(dict(r, person_weight=r['person_weight']*factor,
                         replicate_weights=[w*factor for w in r['replicate_weights']]))
    # Counts are CPS-anchored ratio targets, not absolute CBO population levels.
    cells = []
    for (age, sex), factor in sorted(factors.items()):
        source = sum(r['person_weight'] for r in children if (r['age'], r['sex']) == (age, sex))
        actual = sum(r['person_weight'] for r in projected if (r['age'], r['sex']) == (age, sex))
        target = source*factor
        if abs(actual-target) > .01:
            raise ValueError('CPS-anchored cell accounting failed')
        cells.append({'age': age, 'sex': sex, 'growth_factor': factor,
                      'source_cps_count': source, 'ratio_target_count': target, 'achieved_count': actual})
    return {'year': year, 'status': 'DEMOGRAPHIC_SENSITIVITY_NOT_CURRENT_LAW_FORECAST',
            'assumptions': 'Frozen real resources, thresholds, household composition and within-cell poverty; fixed external age/sex growth ratios',
            'dollar_year': 2025, 'population_base_year': 2026,
            'all_children': poverty_metrics(projected),
            'conditional_sampling_uncertainty': replicate_intervals(projected),
            'cells': cells}


def run(archive, directory, crosswalk_output=None):
    children, audit, crosswalk = read_cps(archive)
    if crosswalk_output:
        Path(crosswalk_output).parent.mkdir(parents=True, exist_ok=True)
        with open(crosswalk_output, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=crosswalk[0])
            writer.writeheader()
            writer.writerows(crosswalk)
    population, econ, hashes = read_inputs(directory)
    factors = {str(y): {v: econ[(y, v)]/econ[(2025, v)] for v in
                        ('cpiu', 'chained_cpiu', 'eci_wages_salaries', 'cpiu_medical_price_index')}
               for y in (2030, 2034)}
    return {'status': 'PROJECTION_INPUTS_AND_SENSITIVITY_ONLY',
            'archive_sha256': sha256(archive), 'input_subset_sha256': hashes,
            'source_income_year': 2025, 'survey_year': 2026,
            'source_audit': audit, 'calendar_year_index_factors_from_2025': factors,
            'index_factor_limits': 'Not used to scale net SPM resources or taxes; CPI-U alone is not an SPM threshold forecast; calendar chained CPI is not the statutory indexing window',
            'current_law_ctc_parameters': {str(y): parameters(y, directory/'cbo-ctc-parameters-2026-02.csv')
                                          for y in (2025, 2030, 2034)},
            'demographic_sensitivities': [sensitivity(children, population, y) for y in (2030, 2034)],
            'policy_ready': False,
            'remaining_requirements': ['Reviewed tax-year claimant/eligibility and CTC-only allocation',
                'Component income aging and joint federal/state tax/transfer recomputation',
                'SPM threshold/expense and housing-valuation projection',
                'CPS-universe population controls and replicate calibration',
                'Reviewed program eligibility, receipt, supply and delivery overlays']}


if __name__ == '__main__':
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--archive', required=True)
    p.add_argument('--input-directory', type=Path, default=HERE/'empirical')
    p.add_argument('--output', required=True)
    p.add_argument('--crosswalk-output', help='Optional source-year child/claimant CSV; keep own return distinct')
    args = p.parse_args()
    write_json(args.output, run(args.archive, args.input_directory, args.crosswalk_output))
    print('Wrote audited source links and demographic sensitivities; full current-law forecast remains incomplete')
