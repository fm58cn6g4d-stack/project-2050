#!/usr/bin/env python3
"""Bounded financing comparisons using existing fiscal/incidence tools.
Research scenarios only; no tax, score or canonical input is adopted.
Run after run-all.sh. Generated report/JSON live in sources/.
"""
import argparse
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import sys

ROOT=Path(__file__).resolve().parents[2]
TOOLS=ROOT/'index/tools'
sys.path.insert(0,str(TOOLS))


def module(name,path):
    s=importlib.util.spec_from_file_location(name,path)
    m=importlib.util.module_from_spec(s);sys.modules[name]=m;s.loader.exec_module(m)
    return m


def assessed_gap(years, revenue):
    adjusted={str(y):years[str(y)]['gf_primary']-revenue[y] for y in range(2040,2057)}
    binding=max(adjusted,key=adjusted.get)
    return dict(fy2040_primary_gap_bn=adjusted['2040'],
                worst_maturity_gap_bn=adjusted[binding],binding_year=int(binding),
                maturity_screen_pass=adjusted[binding]<=1e-9)


def combine(paths):
    return {y:sum(p[y] for p in paths) for y in range(2026,2057)}


def analyze():
    fiscal=module('family_finance_fiscal',TOOLS/'fiscal-model.py')
    # Existing incidence reader expects the generated ledger in its working directory.
    previous=os.getcwd()
    try:
        os.chdir(ROOT/'build')
        incidence=module('incidence',ROOT/'build/incidence.py')
        years_module=module('years',ROOT/'build/years.py')
    finally:os.chdir(previous)
    baseline=fiscal.read_baseline(ROOT/'index/data/fiscal-baseline.csv')
    model=json.loads((ROOT/'build/fiscal-model.json').read_text())['results']['DEC']
    ledger=json.loads((ROOT/'build/ledger.json').read_text())
    g1=next(r for r in ledger['revenue'] if r['id']=='G1')['mid']
    base_incidence,_=incidence.run(incidence.QO)
    base_annual=years_module.series(incidence.QO)
    base_gf=incidence.gf_test(incidence.QO)
    def path(mid,grow):return fiscal.row_path(baseline,mid,dict(start=2030,ramp=1,grow=grow))
    corporate_gross=g1*3/7  # 28% -> 31%, linear scale of adopted 21% -> 28% working score
    corporate=corporate_gross*.8  # additional illustrative 20% yield haircut; not estimated avoidance
    payroll=1.6*.35  # existing 1-point general-fund option, scaled to 0.35 percentage points
    corp_path=path(corporate,'rev_corporate')
    wage_path=path(payroll,'gdp')  # GDP is a wage-base proxy, not an audited payroll forecast
    median=combine([fiscal.row_path(baseline,1.25,fiscal.PR.CUTS['C19'],'C19'),
                    {y:-v for y,v in fiscal.row_path(baseline,.66,fiscal.PR.CUTS['C19b'],'C19b').items()}])
    median_incidence,_=incidence.run([o if o!='C19b' else 'C19' for o in incidence.QO])
    median_annual=years_module.series([o if o!='C19b' else 'C19' for o in incidence.QO])
    cases=[]
    for name,revenue,mid,parts,corporate_remit in [
        ('Corporate 31% illustrative route',corp_path,corporate,[('wages',.25*corporate),('capital',.75*corporate)],corporate),
        ('General-fund payroll contribution 0.35 points',wage_path,payroll,[('wages',payroll)],0),
        ('Median health-exclusion cap replacing 75th-percentile cap',median,1.25-.66,None,0)]:
        if parts is None:
            net={g:median_incidence[g]['net'] for g in incidence.GROUPS[:4]}
            annual={str(y):{g:median_annual[y][g] for g in incidence.GROUPS[:4]} for y in (2030,2034,2039)}
            gf=incidence.gf_test([o if o!='C19b' else 'C19' for o in incidence.QO])
            mix=gf[3]
        else:
            distributed=incidence.dist(parts)
            net={g:base_incidence[g]['net']-incidence.per_hh(distributed[g],g) for g in incidence.GROUPS[:4]}
            annual={str(y):{g:base_annual[y][g]-distributed[g]/mid*revenue[y]*1e9/(incidence.HH*.2)
                            for g in incidence.GROUPS[:4]} for y in (2030,2034,2039)}
            numerator=base_gf[1]+base_gf[2]+(corporate_remit if corporate_remit else distributed['T1'])
            mix=round(100*numerator/(base_gf[0]+mid))
        cases.append(dict(name=name,revenue_2030_39_tn=mid,fy2040_receipts_bn=revenue[2040],
            **assessed_gap(model['years'],revenue),net_household_annual_average=net,
            annual_household_net=annual,top1_plus_corporations_share_pct_proxy=mix,
            window_residual_after_existing_accepted_arrangements_tn=ledger['summary']['gap_after_accepted']-mid,
            revenue_path_bn={str(y):v for y,v in revenue.items()}))
    stress=[]
    for name,receipts in [('Corporate route',corp_path),('Payroll route',wage_path),('Median exclusion fallback',median)]:
        for loss in (0,.2,.4):
            stress.append(dict(name=name,additional_yield_loss=loss,
                **assessed_gap(model['years'],{y:v*(1-loss) for y,v in receipts.items()})))
    thresholds={}
    for name,p in [('corporate',path(1,'rev_corporate')),('payroll',path(1,'gdp'))]:
        needed=max(model['years'][str(y)]['gf_primary']/p[y] for y in range(2040,2057))
        thresholds[name]=dict(required_2030_39_tn_at_assumed_profile=max(0,needed),
                              basis='Break-even calculation under current working paths, not a tax score')
    files=['index/tools/family-financing.py','index/tools/fiscal-model.py','index/tools/fiscal-profiles.py',
           'index/tools/incidence-model.py','index/tools/incidence-years.py','index/data/inputs/ledger-bills.csv',
           'index/data/inputs/ledger-revenue.csv','index/data/inputs/ledger-cuts.csv',
           'index/data/inputs/fiscal-profiles.csv','index/data/inputs/fiscal-components.csv',
           'index/data/inputs/incidence-keys.csv','index/data/inputs/incidence-rows.csv',
           'index/data/inputs/incidence-phase-in.csv','index/data/fiscal-baseline.csv','domains/domain-revenue.md']
    return dict(status='ILLUSTRATIVE_FINANCING_NOT_ADOPTED_OR_SCORED',
        source_main='31d2e584d790c6dc6e3c243e1643b1ab3a8d050e',source_pr_head='b375cc961ce89c3d7c332b8c950772d99fba605b',
        corporate_gross_linear_tn=corporate_gross,corporate_extra_haircut=.2,
        payroll_point_option_tn=1.6,base_fy2040_gap_bn=model['years']['2040']['gf_primary'],
        base_q4_average_net=base_incidence['Q4']['net'],cases=cases,stress=stress,thresholds=thresholds,
        unpriced_high_income_guardrails=['REV-HP4 deferred-compensation vesting reform; excluded from receipts',
            'Further high-income base changes need fresh specification/joint scoring; no assumed yield'],
        source_sha256={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in files})


def render(r):
    lines=['# Family financing: bounded choice comparison','',
        'Generated by `index/tools/family-financing.py`; regenerate rather than edit. Research, not policy adoption or an official score. Source main: `'+r['source_main']+'`; continues PR #18 at `'+r['source_pr_head']+'`.','',
        f"The adopted AFA/one-million-award package is retained. Existing financing leaves an FY2040 GF primary gap of ${r['base_fy2040_gap_bn']:.1f}B. Compare incremental revenue only; existing taxes and accepted borrowing remain committed.", '',
        '| Route | Additional 2030–39 revenue | FY2040 receipts | FY2040 primary balance after route | Q4 net, annual average |',
        '| --- | ---: | ---: | ---: | ---: |']
    for c in r['cases']:
        gap=c['fy2040_primary_gap_bn'];label=f'${abs(gap):.1f}B '+('deficit' if gap>0 else 'surplus')
        lines.append(f"| {c['name']} | ${c['revenue_2030_39_tn']*1000:.0f}B | ${c['fy2040_receipts_bn']:.1f}B | {label} | ${c['net_household_annual_average']['Q4']:,.0f} |")
    lines += ['', f"{sum(c['maturity_screen_pass'] for c in r['cases'])} of {len(r['cases'])} cases clear the existing model’s maturity-only screen through 2056 at their assumed yields. This does not establish a full official fiscal/Byrd score, permit permanent-benefit borrowing, validate the old CAP-7S cash proxy or certify exact AFA household incidence. The ten-year residual after existing accepted arrangements is also reported in JSON; it is not the same measure as the fiscal model’s GF primary deficit.", '',
        '## What each route actually assumes','',
        '**Corporate/high-income route:** the quantified example raises the corporate rate from the adopted 28% to 31%. It scales the existing seven-point G1 working score linearly for three additional points, then takes a further illustrative 20% yield haircut: roughly $707B gross becomes $566B. This is a comparison assumption, not a fresh estimate of behavior or a validated rate-to-revenue relationship. Interactions with the minimum tax, international provisions and deduction-denial measures require joint scoring. Further high-income/vested deferred-compensation guardrails remain possible but unpriced and contribute no assumed receipts here. SS-5/HI pass-through bases are not spent again.', '',
        '**Payroll route:** 0.35 percentage points on uncapped payroll for general revenue, scaled from the existing 1-point/$1.6T option. The path uses GDP as a wage-base proxy. At $60,000 of covered wages the total statutory contribution would be $210 annually; an equal split would be $105 each for worker and employer before economic incidence. The screen assigns the full burden to wages, so an employer split is not treated as free money. Coordinate it with existing leave/SS contributions; this is not a new trust fund or adoption of the held education fund.', '',
        '**Health-exclusion fallback:** replace C19b with C19. The $590B is the difference between existing $1.25T and $0.66T working estimates, not the full $1.25T counted again. It uses the existing Medicare-premium-growth fiscal proxy and existing incidence case. Actual employer plans, premium changes, wage pass-through and employee tax rates matter; the aggregate positive Q4 result can hide losers.', '',
        '## Robustness and household effects','',
        '| Route | Further receipt shortfall | Worst FY2040–56 primary gap | Maturity screen |',
        '| --- | ---: | ---: | --- |']
    for s in r['stress']:
        lines.append(f"| {s['name']} | {s['additional_yield_loss']:.0%} | ${s['worst_maturity_gap_bn']:.1f}B | {'passes' if s['maturity_screen_pass'] else 'fails'} |")
    lines += ['', 'The corporate stress is additional to its initial 20% assumed haircut. These are stresses, not probabilities. A small positive surplus at the central assumption is not a guaranteed financing cushion. Break-even yield requirements under each profile are in JSON.', '',
        'The original aggregate household model remains a proxy allocation of ledger benefits/costs. It does not resolve exact AFA tax losses, legal exclusions, within-quintile incidence or health-plan behavior. The JSON shows bottom-four averages and 2030/2034/2039 paths; favorable ten-year averages do not eliminate early-year exposure. All cases retain the adopted family benefits. Payroll and corporate incidence assumptions are explicit; new household revenue-mix shares are approximate because the existing financing totals are rounded.', '',
        '## Recommendation and stopping point','',
        '**First pursue a fresh, jointly scored corporate/high-income route; keep the modest payroll route as a fully specified alternative.** The illustration obtains similar recurring revenue with a smaller modeled Q4 burden through the corporate route. That preference depends on real incremental corporate receipts surviving interactions and behavior; it is not a recommendation to adopt 31% from this calculation alone. If a credible top-end route falls short, compare the size and household protection needed for a smaller broad contribution. The median health-exclusion cap remains a consequential fallback, with the largest modeled Q4 cost of these examples.', '',
        'Next decision: choose which route to develop into a supported financing specification, or request the limited joint-score comparison. No financing instrument, rate or offset is adopted here, and no merge is authorized. Do not add previously adopted estate/SC1/sprint/pay taxes again, use the HI reserve, count dynamic revenue or convert shrinking carbon receipts into permanent benefit financing.', '',
        'Sources: [revenue domain](../domains/domain-revenue.md), G1, C19/C19b, W1/payroll and high-pay options; [family adoption bridge](family-adoption-architecture-bridge.md); existing fiscal/incidence modules and hashed input tables. No new external score or legal clearance obtained. The source estimates are inherited working figures with different vintages; the new rate scaling/haircuts are labeled assumptions. Reproduce after `bash index/tools/run-all.sh` with `python3 index/tools/family-financing.py`. Tests cover incremental replacement, calibration and the sign of the maturity gap. Canonical policy, numerical inputs and generated common products are unchanged by this research.']
    return '\n'.join(lines)+'\n'


if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--output',type=Path,default=ROOT/'sources/family-financing-comparison')
    a=p.parse_args();r=analyze();a.output.with_suffix('.json').write_text(json.dumps(r,indent=2)+'\n');a.output.with_suffix('.md').write_text(render(r));print(r['status'])
