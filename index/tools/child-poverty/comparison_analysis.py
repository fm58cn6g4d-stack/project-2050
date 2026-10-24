#!/usr/bin/env python3
"""Bounded family alternatives and later-year constant-real scenarios.
Existing official results remain unchanged. No forecast or adopted policy.
Without --archive, national alternative effects remain null, never synthetic.
"""
import argparse
import copy
import json
import math
import hashlib
import zipfile
from pathlib import Path
from agenda_analysis import (HERE, parse_archive, prepare_units, unit_effect,
                             aggregate, external_comparator, policy_parameters)
from cps_projection import read_inputs
from model import sha256, write_json

ROOT = HERE.parents[2]
DESIGNS = ('FAM-1A', 'FAM-1D_2030_face', 'AFA_2025_real', 'AFA_no_newborn_bonus')
YEARS = (2034, 2040, 2050)


def annual_analogue(ages, agi, filing, real_index=1., newborn=True):
    """Annual exposure analogue of proposed 24A, not exact monthly tax law.
    Single/head/other mapping omits MFS; no inferred eligibility or lookback AGI.
    Inflation is explicit constant-real scenario input, not statutory rounding.
    """
    if filing not in ('joint', 'head', 'other') or not math.isfinite(agi):
        raise ValueError('Unsupported filing/income')
    if not math.isfinite(real_index) or real_index <= 0:
        raise ValueError('positive price factor required')
    if any(type(a) is not int or not 0 <= a < 18 for a in ages):
        raise ValueError('Supplied qualifying ages must be 0..17')
    gross = sum(6360 if a == 0 and newborn else 4320 if a < 6 else 3600 for a in ages)*real_index
    first = (150000 if filing == 'joint' else 112500)*real_index
    second = (400000 if filing == 'joint' else 300000)*real_index
    retained = 2000.04*len(ages)  # statute's $166.67 monthly reference, not $2,200
    cut = min(max(0, gross-retained), .05*max(0, second-first), .05*max(0, agi-first))
    return max(0, gross-cut-.05*max(0, agi-second))


def alternative_increment(tax, cpi, design, anchor_cpi):
    if design not in DESIGNS[1:]:
        raise ValueError('Named alternative required')
    # Annual 2030 face amounts vs full preservation of 2025 real face amounts.
    real_factor = 1/anchor_cpi if design == 'FAM-1D_2030_face' else 1.
    # AGI and first thresholds both in 2025 purchasing power for this analogue.
    # Thresholds share the scenario factor; exact statutory inflation/rounding is not modeled.
    award = annual_analogue(tax['child_ages'], tax['agi']*cpi, tax['filing'],
                            real_factor*cpi, design != 'AFA_no_newborn_bonus')/cpi
    baseline = tax['nonrefundable']+tax['refundable']
    # Signed: an alternative can reduce a high-income family's credit.
    return award-baseline


def apply_overlays(prepared, rows):
    """Reviewed net amounts; reject duplicates/unsupported cash attribution.
    Externally calibrated inputs are required; none supplied by default.
    """
    seen = set()
    for row in rows:
        uid, component = row['unit_id'], row['component']
        key = (uid, component)
        if key in seen or uid not in prepared:
            raise ValueError('Duplicate or unmatched overlay')
        if component not in ('health_moop_saving', 'net_tax_transfer_earnings', 'net_leave_benefit'):
            raise ValueError('Unsupported overlay component')
        if not row.get('review') or row.get('baseline_reconciled') is not True:
            raise ValueError('Reviewed baseline/overlap reconciliation required')
        delta = row['delta_2025_dollars']
        if type(delta) not in (int,float) or not math.isfinite(delta):
            raise ValueError('Finite net amount required')
        if component == 'health_moop_saving':
            if not 0 <= delta <= prepared[uid]['source_moop']:
                raise ValueError('Medical saving exceeds actual source deduction')
        prepared[uid]['cost'] += delta
        seen.add(key)


def evaluate(data, spec, pop, econ, design, delivery_name, awards=400000, overlays=(),
             resource_shift=0.):
    if design not in DESIGNS or delivery_name not in spec['scenarios']:
        raise ValueError('Unsupported design or delivery')
    if type(awards) is not int or awards < 0:
        raise ValueError('Nonnegative award cap required')
    if not math.isfinite(resource_shift) or not -.2 <= resource_shift <= .2:
        raise ValueError('Resource stress must be within +/-20% of threshold')
    cfg = copy.deepcopy(spec['common'])
    cfg['baseline_resource_shift'] = resource_shift
    prepared, check = prepare_units(data,2034,cfg,pop,econ)
    _, cpi, anchor = policy_parameters(2034,cfg,econ)
    eligible = check['eligible_households_weighted']
    probability = min(1, awards/eligible) if eligible else 0
    for uid, p in prepared.items():
        p['source_moop'] = data['units'][uid]['SPM_MEDXPNS']
        p['voucher_probability'] = probability if p['service']['voucher_eligible'] else 0
        if design != 'FAM-1A':
            p['ctc'] = sum(alternative_increment(t,cpi,design,anchor) for t in data['taxes_by_unit'][uid])
    apply_overlays(prepared,overlays)
    weights = [p['weight']*pop[(2034,p['age'],p['sex'])]/pop[(2026,p['age'],p['sex'])]
               if cfg['demographic_growth'] else p['weight'] for p in data['children']]
    baseline = {u:unit_effect(p,2034,{},'baseline') for u,p in prepared.items()}
    delivery = spec['scenarios'][delivery_name]
    effects = {u:unit_effect(p,2034,delivery,5) for u,p in prepared.items()}
    result = aggregate(data,effects,weights,baseline)
    return dict(design=design,delivery=delivery_name,award_cap=awards,
                expected_awards=eligible*probability,
                expected_leases=eligible*probability*delivery['voucher_leaseup'],
                baseline=aggregate(data,baseline,weights),result=result,
                federal_cost=None, overlay_rows=len(overlays))


def contribution_diagnostics(data, spec, pop, econ):
    prepared,_=prepare_units(data,2034,spec['common'],pop,econ)
    groups={name:dict(weighted_children=0.,ctc_sum=0.,baseline_credit_sum=0.,positive_increment=0.)
            for name in ('source_deep_poor','source_poor_not_deep','source_not_poor')}
    for person in data['children']:
        uid=person['uid'];unit=data['units'][uid]
        w=person['weight']*pop[(2034,person['age'],person['sex'])]/pop[(2026,person['age'],person['sex'])]
        ratio=unit['SPM_RESOURCES']/unit['SPM_POVTHRESHOLD']
        name='source_deep_poor' if ratio<.5 else 'source_poor_not_deep' if ratio<1 else 'source_not_poor'
        row=groups[name];row['weighted_children']+=w
        row['ctc_sum']+=w*prepared[uid]['ctc']
        row['baseline_credit_sum']+=w*sum(t['nonrefundable']+t['refundable'] for t in data['taxes_by_unit'][uid])
        row['positive_increment']+=w*(prepared[uid]['ctc']>0)
    for row in groups.values():
        weight=row['weighted_children']
        row['mean_unit_ctc_increment_per_child']=row.pop('ctc_sum')/weight if weight else None
        row['mean_existing_unit_credit_per_child']=row.pop('baseline_credit_sum')/weight if weight else None
        row['share_positive_statutory_increment']=row.pop('positive_increment')/weight if weight else None
    return dict(basis='Child-weighted unit amounts in 2025 dollars before receipt haircut; source-resource groups, not causal attribution or federal costs',groups=groups)


def carry_forward(stored):
    """Static reference, not an extrapolation of an improving poverty trend."""
    output = []
    for case in stored['cases']:
        if case['year'] != 2034:
            continue
        end = case['stages'][-1]
        for year in YEARS:
            output.append(dict(year=year,reference_year=2034,scenario=case['scenario'],
                poor_rate=end['poor_rate'],deep_poor_rate=end['deep_poor_rate'],
                poor_children=end['poor_children'],
                basis='Constant 2034 population mix, real resources, real policy rules and delivery; not cohort aging or forecast'))
    return output


def verify_archive(archive, stored, manifest_path=None):
    actual = sha256(archive)
    if actual == stored['archive_sha256']:
        return dict(kind='original_archive',archive_sha256=actual)
    if manifest_path is None:
        raise ValueError('Source archive differs; uploaded-member manifest required')
    manifest=json.loads(Path(manifest_path).read_text())
    if manifest.get('origin') != 'user_supplied_census_members' or manifest.get('original_archive_sha256') != stored['archive_sha256']:
        raise ValueError('Unrecognized source lineage')
    required={'hhpub26.csv','pppub26.csv','asec_csv_repwgt_2026.csv'}
    if not required <= set(manifest['members']):
        raise ValueError('Incomplete member manifest')
    with zipfile.ZipFile(archive) as z:
        for name, expected in manifest['members'].items():
            if z.getinfo(name).file_size != expected['bytes']:
                raise ValueError('Source member length changed: '+name)
            digest=hashlib.sha256()
            with z.open(name) as f:
                for block in iter(lambda:f.read(1024*1024),b''):digest.update(block)
            if digest.hexdigest()!=expected['sha256']:
                raise ValueError('Source member hash changed: '+name)
    return dict(kind='uploaded_members_in_local_container_not_original_zip',
                archive_sha256=actual,manifest_sha256=sha256(manifest_path))


def analyze(archive=None, overlays=(), paths=None, manifest_path=None):
    stored_path=HERE/'empirical/agenda-results.json'
    stored=json.loads(stored_path.read_text())
    spec=json.loads((HERE/'agenda-assumptions.json').read_text())
    paths = paths or [dict(year=y, delivery='moderate', resource_shift=0.,
                         review='Constant-real reference; no economic or delivery trend') for y in YEARS]
    for path in paths:
        if path.get('year') not in YEARS or not path.get('review') or path.get('delivery') not in spec['scenarios']:
            raise ValueError('Explicit supported year, delivery and path review required')
        shift=path.get('resource_shift')
        if type(shift) not in (int,float) or not math.isfinite(shift) or not -.2 <= shift <= .2:
            raise ValueError('Finite bounded threshold-resource stress required')
    out=dict(status='NATIONAL_ALTERNATIVES_NOT_RUN' if archive is None else 'CONDITIONAL_NATIONAL_ALTERNATIVES',
        stored_sha256=sha256(stored_path), source_income_year=2025,
        source_main='31d2e584d790c6dc6e3c243e1643b1ab3a8d050e',
        years=list(YEARS),valuation_year=2034,carry_forward=carry_forward(stored),
        national_cases=None,later_path_cases=None, paths=paths,archive_sha256=None,missing='Census archive not locally available' if archive is None else None,
        code_sha256=sha256(Path(__file__)),
        dependencies_sha256={p:sha256(HERE/p) for p in ('agenda_analysis.py','model.py','agenda-assumptions.json','cps_projection.py','current_law_ctc.py','empirical/cbo-calendar-factors-2026-02.csv','empirical/cbo-child-population-2026-01.csv','empirical/cbo-ctc-parameters-2026-02.csv')},
        examples=dict(kind='Illustrative conditional tax awards only; not national outcomes',
            one_child_age4=annual_analogue([4],0,'head'),
            one_child_age8=annual_analogue([8],0,'head'),
            infant_full_year_exposure=annual_analogue([0],0,'head'),
            infant_no_bonus=annual_analogue([0],0,'head')))
    out['examples']['infant_no_bonus']=annual_analogue([0],0,'head',newborn=False)
    if archive is not None:
        provenance=verify_archive(archive,stored,manifest_path)
        data=parse_archive(archive)
        comparator=external_comparator(data)
        print('Source parsed and external credit-removal comparator passed.',flush=True)
        pop,econ,_=read_inputs(HERE/'empirical')
        cases=[]
        cache={}
        def calculate(design,delivery,cap=400000,shift=0.):
            key=(design,delivery,cap,shift)
            if key not in cache:
                cache[key]=evaluate(data,spec,pop,econ,design,delivery,cap,overlays,shift)
            return cache[key]
        for design in DESIGNS:
            for delivery in ('moderate','enhanced','full'):
                cases.append(calculate(design,delivery))
                print(design,delivery, f"{cases[-1]['result']['poor_rate']:.4%}",flush=True)
        # A bounded reach scenario and a full proxy-eligible boundary; not adopted entitlements.
        eligible=prepare_units(data,2034,spec['common'],pop,econ)[1]['eligible_households_weighted']
        for cap in (1000000, math.ceil(eligible)):
            for design in ('FAM-1A','AFA_2025_real'):
                cases.append(calculate(design,'enhanced',cap))
        reference=next(c for c in stored['cases'] if c['year']==2034 and c['scenario']=='moderate')['stages'][-1]
        if not overlays and abs(cases[0]['result']['poor_rate']-reference['poor_rate'])>1e-12:
            raise ValueError('Legacy moderate reference failed reproduction')
        later=[]
        for path in paths:
            for design in ('FAM-1A','AFA_2025_real'):
                c=calculate(design,path['delivery'],shift=path['resource_shift'])
                later.append(dict(year=path['year'],reference_year=2034,path=path,**c))
        out.update(national_cases=cases,later_path_cases=later,archive_sha256=sha256(archive),overlay_sha256=None,source_provenance=provenance,external_comparator=comparator,source_audit=data['audit'],legacy_moderate_reproduced=not overlays,contribution_diagnostics=contribution_diagnostics(data,spec,pop,econ))
    return out


def render(r):
    lines=['# Family comparisons and later-year reference checks','',
        'Generated by `index/tools/child-poverty/comparison_analysis.py`; do not hand edit.','',
        f"Status: **{r['status']}**. National effects are populated only after a validated microdata run; federal costs remain unpriced.", '',
        'The table carries the existing 2034 calculation forward with population composition, real resources, policy value and delivery fixed. It shows why a later date alone creates no improvement. Counts are reference-population counts, not projected future populations.', '',
        '| Delivery | 2034 child poverty | 2040 constant-real reference | 2050 constant-real reference |',
        '| --- | ---: | ---: | ---: |']
    for name in ('moderate','enhanced','full'):
        z=[x for x in r['carry_forward'] if x['scenario']==name]
        lines.append('| '+name+' | '+' | '.join(f"{x['poor_rate']*100:.2f}%" for x in z)+' |')
    lines += ['', 'These are repeated static comparisons, not independent new estimates, forecasts or a claim that no policy has long-run effects.', '',
        'Annual AFA exposure examples at unindexed face values: age 4 $4,320; age 8 $3,600; age 0 full-year exposure $6,360 versus $4,320 without the first-month bonus. These examples do not reconstruct birth dates, exact calendar-year awards, eligibility or total tax liability.', '',
        'The runnable alternative matrix holds 2034 valuation and population fixed across 2034/2040/2050 labels; separate moderate/enhanced/full delivery comparisons are conditional stages, not a dated transition forecast. New component overlays require explicit reviewed net amounts and overlap reconciliation; none are calibrated or supplied by default.']
    if r['national_cases'] is not None:
        lines += ['', '| Design | Delivery | Award cap | Child poverty | Deep poverty |', '| --- | --- | ---: | ---: | ---: |']
        for c in r['national_cases']:
            lines.append(f"| {c['design']} | {c['delivery']} | {c['award_cap']:,} | {c['result']['poor_rate']*100:.2f}% | {c['result']['deep_poor_rate']*100:.2f}% |")
    if r['later_path_cases'] is not None:
        lines += ['', '| Year label | Design | Delivery | Threshold-resource stress | Child poverty |', '| --- | --- | --- | ---: | ---: |']
        for c in r['later_path_cases']:
            lines.append(f"| {c['year']} | {c['design']} | {c['delivery']} | {c['path']['resource_shift']:+.1%} | {c['result']['poor_rate']*100:.2f}% |")
    return '\n'.join(lines)+'\n'


if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--archive',type=Path)
    p.add_argument('--source-manifest',type=Path,help='Fingerprint ledger for user-uploaded source members in a repacked local container')
    p.add_argument('--overlays',type=Path)
    p.add_argument('--paths',type=Path,help='Reviewed year/delivery/resource stresses; no inferred economic forecast')
    p.add_argument('--output',type=Path,default=ROOT/'sources/family-comparison-model-checks')
    args=p.parse_args()
    rows=json.loads(args.overlays.read_text()) if args.overlays else []
    if rows and args.archive is None:
        p.error('Overlays require a verified archive')
    paths=json.loads(args.paths.read_text()) if args.paths else None
    result=analyze(args.archive,rows,paths,args.source_manifest)
    if args.paths:
        result['paths_sha256']=sha256(args.paths)
    if args.overlays:
        result['overlay_sha256']=sha256(args.overlays)
    write_json(args.output.with_suffix('.json'),result)
    args.output.with_suffix('.md').write_text(render(result))
    print(result['status'])
