#!/usr/bin/env python3
"""Render the verified agenda experiment as a report and compact chart view."""
import argparse
import html
import json
from pathlib import Path
from model import load_json
from check_agenda_results import check


def pct(value):
    return f'{value*100:.2f}%'


def million(value):
    return f'{value/1e6:.2f} million'


def markdown(r):
    intervals=[]
    for y in (2030,2034):
        c=next(c for c in r['cases'] if c['year']==y and c['scenario']=='moderate')
        ci=c['stages'][-1]['sampling_uncertainty']['paired_poor_rate_change']
        intervals.append(f"{-100*ci['upper95']:.2f}–{-100*ci['lower95']:.2f} points in {y}")
    rows=[]
    for c in r['cases']:
        s=c['stages'][-1]
        rows.append(f"| {c['year']} | {c['scenario'].title()} | {pct(c['baseline']['poor_rate'])} | {pct(s['poor_rate'])} | {pct(s['deep_poor_rate'])} | {million(c['baseline']['poor_children']-s['poor_children'])} |")
    steps=[]
    for year in (2030,2034):
        c=next(c for c in r['cases'] if c['year']==year and c['scenario']=='moderate')
        for s in c['stages']:
            steps.append(f"| {year} | {s['label']} | {pct(s['poor_rate'])} | {pct(s['deep_poor_rate'])} |")
    sensitivity=[]
    names={'index_from_2025':'Index benefits from 2025 instead of 2030',
           'resources_minus_5pct_threshold':'Baseline resources lower by 5% of threshold',
           'resources_plus_5pct_threshold':'Baseline resources higher by 5% of threshold',
           'coverage_gap_in_lowest_resource_quarter':'Same coverage gap concentrated in lowest-resource quarter',
           'retain_adult_ODC_bound':'Retain maximum possible adult-dependent ODC',
           'employer_leave_fully_wage_borne':'Employer leave contribution fully borne in wages',
           'carbon_dividend_and_cost_proxy':'Add adult climate dividend and consumer-cost proxy',
           'carbon_plus_health15pct':'Add carbon proxy and 15% reduction in actual MOOP',
           'carbon_plus_health30pct':'Add carbon proxy and 30% reduction in actual MOOP',
           'temporary_cash_10B':'Assume $10B temporary household cash, separate from construction'}
    for name,label in names.items():
        pair=[next(x for x in r['sensitivities'] if x['year']==y and x['name']==name) for y in (2030,2034)]
        sensitivity.append(f"| {label} | {pct(pair[0]['result']['poor_rate'])} | {pct(pair[1]['result']['poor_rate'])} |")
    mature=next(c for c in r['cases'] if c['year']==2034 and c['scenario']=='moderate')
    subgroup=[]
    for category in ('earnings','adults','tenure','head_race_ethnicity'):
        for label,v in mature['subgroups'][category].items():
            subgroup.append(f"| {label} | {pct(v['poor_rate']) if v['poor_rate'] is not None else 'Suppressed'} | {pct(v['residual_share'])} |")
    comparison=r['external_comparator']
    return f'''# Child poverty under Project 2050: completed conditional agenda analysis

> Historical pre-adoption experiment: FAM-1A and 400,000 new voucher awards. Espen subsequently adopted FAM-1D/AFA and one million awards. Use [current selected-package comparisons](family-comparison-model-checks.md) and the [adoption bridge](family-adoption-architecture-bridge.md) for current policy; the results below retain their original assumptions.

October 24, 2026. Source branch claude/pensive-mendel-g1lwl5 at {r['project_base']}. This report records a completed static scenario analysis, not a forecast of the poverty rate in 2030 or 2034 and not a change to adopted policy.

The modeled package materially reduces child poverty and deep poverty. FAM-1A supplies most of the early reduction; mature food assistance and scarce housing assistance add to it. Full modeled receipt still leaves substantial poverty. Better delivery matters, but the tested delivery improvements alone do not eliminate the remaining gap.

## Main results

The observed source-year child SPM baseline is {pct(r['source_baseline']['poor_rate'])}. Ages and family relationships come from the 2026 CPS ASEC; resources refer to 2025. The 2030/2034 labels select policy phasing, price conventions and optional demographic growth ratios, with source-year net resources held in 2025 purchasing power. Future tax/transfer law is not comprehensively forecast. Counts use the CPS-anchored population scenarios rather than CBO's absolute Social Security-area totals.

| Phasing year | Conditional delivery case | Same-scenario baseline | After modeled policies | Deep poverty after | Net fewer poor children |
| --- | --- | ---: | ---: | ---: | ---: |
{chr(10).join(rows)}

Stressed, moderate, enhanced and full are analyst assumptions, not measured program-performance estimates, forecast percentiles or confidence bounds. Moderate assumes a 95% conditional coverage share, 95% annual receipt of the incremental CTC, 50%/75% usable care access and 60%/85% pre-K access in 2030/2034, 90% food receipt and 65% voucher lease-up. Full means complete modeled coverage/receipt/access within income rules, the stated food calendar and the voucher award cap; it does not give every eligible renter a voucher. Conditional coverage is an aggregate family-level research convention, not imputed SSN/ITIN status. The main construction leaves the 327 children without a positive Census claimant pointer without a new credit; their proxy inclusion is a separate sensitivity.

The main dollar convention sets the $3,600/$3,000 child credit in 2030 nominal dollars and indexes it thereafter. A coequal sensitivity indexes those amounts from 2025. Neither convention is silently adopted as a legal drafting decision. First-stage increase thresholds follow the 2021 filing-status levels; the retained credit uses the recorded CBO parameter vintage. The age-17 layer is separately branched. Interview ages proxy for tax-year ages because exact birthdays are unavailable; the Census claimant pointer is not proof of legal qualifying-child status. Actual source-year credits remain in baseline resources. Receipt applies to the net expansion, preserving baseline credits; this is the explicit increment-only convention, not a model of replacement, reconciliation or repayment losses. Source nonrefundable CTC includes ODC; the main offset subtracts the entire observed combined amount before computing an increment, while the ODC sensitivity retains the maximum possible adult-dependent portion.

## How the channels interact

Each row recomputes poverty jointly after adding the next channel to the same families. These are order-dependent cumulative comparisons, not independent effects to add together.

| Year | Cumulative policy channels, moderate delivery | Child poverty | Deep poverty |
| --- | --- | ---: | ---: |
{chr(10).join(steps)}

FAM-2A reduces the actual capped work/care deduction. Pre-K and care share the same expense pool, so one saved dollar cannot be counted twice. Monetary gains are limited for families reporting no paid care, even when access to a new service could improve their lives or employment. Care eligibility uses state weighted medians for four-person CPS SPM units and an explicit size adjustment; these are proxies rather than administrative state median income determinations. Usable services and the pre-K share of paid expenses are assumptions varied in the results.

Food gains are net of baseline lunch and Summer EBT values. The empirical modal annual free-lunch value is $861 per school-age child in the source data. School-age counts proxy for enrollment. The main 2030 case credits 80/179 of annual school-lunch gains and no Summer EBT increase, consistent with a conservative fall-2030 launch convention; a full-year food case is also reported. Three summer months, the $60 monthly policy amount and a source-year 185%-FPG/direct-certification eligibility proxy determine the mature summer increment. Existing summer payments are deducted before adding the new amount. Some summer EBT is embedded in school-lunch values and some may be reported with SNAP. Breakfast is beneficial but receives no value under the Census SPM method, so no breakfast dollars are inserted here.

HOU-4A awards are capped at 100,000 households in 2030 and 400,000 in 2034. Allocation includes adult-only households and separates award from lease-up. The code integrates discrete recipient/nonrecipient poverty outcomes; it does not spread an average subsidy across every renter. The income/waitlist proxy and housing-need cap remain uncertain, and no construction capital becomes family cash. HOU-1 has no automatic primary cash value because its household-cash/construction split is unsized; the explicit temporary-cash sensitivity expires after 2031.

The employee paid-leave contribution is included as a cost-side stress at 0.3% of wage income. Leave benefits are not assigned without an observed leave event. The higher employee rate and full employer wage incidence are separately varied. This is a conservative cost-side inclusion, not a net evaluation of paid leave.

## Uncertainty and broader agenda channels

| One-at-a-time change from moderate case | 2030 child poverty | 2034 child poverty |
| --- | ---: | ---: |
{chr(10).join(sensitivity)}

The resource-adequacy cases shift each unit's baseline resources by plus or minus 5% of its SPM threshold. Their baselines change as well; the displayed after-policy rates are not measured against an unchanged 13.4% baseline. They are stresses, not economic predictions. Coverage concentration puts the same total gap in the lowest-resource quarter, without assigning legal status to observed families. The full result file also varies SMI, pre-K expense allocation, age 17, unresolved claimants, food timing, population weighting and the automatic leave contribution ceiling.

The carbon extension takes both sides of CLI-2A/REV-C1 from the existing project carbon model: adult-only dividends and consumer-price costs. Source-year household income quintiles and a carbon-price scaling rule provide a reduced-form proxy; these are not observed household energy bills. Health cases reduce actual SPM medical out-of-pocket expenses by 15% or 30%; those percentages are sensitivities, not calibrated estimates of the health bill's effects. Joint carbon/health cases are recomputed rather than obtained by adding separate poverty reductions.

The main estimate covers the child-policy channels above. It is not the entire Project 2050 household effect: health coverage and quality, leave benefits, wage and employment changes, other taxes and transfers, public services, housing supply, inflation and long-run child development remain outside the quantified headline. The existing household-incidence and fiscal generators remain the D3/D4 checks. No SPM resource gain or child-weighted poverty gap is presented as a federal budget cost or social value.

All 160 replicate weights are retained, and paired policy changes use the same replicate weights as their baseline. For moderate delivery, the conditional 95% sampling intervals for the poverty-rate reduction are {" and ".join(intervals)}. Sampling intervals exclude uncertainty in legal rules, receipt, proxies, allocation and future conditions. The wider scenario and sensitivity comparisons must be read alongside them. No employment response is credited in the primary runs.

## Who remains poor

In the moderate 2034 case, about {million(mature['stages'][-1]['poor_children'])} children remain poor and {million(mature['stages'][-1]['deep_poor_children'])} remain deeply poor. About {million(mature['residual']['poor_even_with_full_modeled_receipt'])} would remain poor even with full modeled coverage and receipt at the same benefit levels and scarce-voucher limits. The difference is a scenario comparison, not a causal attribution: fixed exclusions, proxy choices and unmodeled channels also remain in that full case.

| Overlapping family characteristic, 2034 moderate | Poverty rate within group | Share of remaining poor children |
| --- | ---: | ---: |
{chr(10).join(subgroup)}

These rows overlap across categories and must not be added. Race/ethnicity refers to the SPM unit head, not the child's own identity. No subgroup below 30 sample children is published as a rate. Low-earnings families have the highest risk, but most remaining poor children live in units with positive earnings. Renters also account for a disproportionate share. Those patterns argue for examining income adequacy, reliable work, housing and health costs alongside delivery, rather than interpreting the residual as a single eligibility or employment problem.

## Verification, sources and reproduction

The source baseline reproduces the previously verified 13.3913% child SPM rate. All person/replicate keys match. Source-year SPM resources and refundable tax amounts reconcile as recorded in the preceding audit. The matched element-removal comparator finds that EITC plus refundable ACTC lifts {million(comparison['public_use_people_lifted'])} people, including {million(comparison['public_use_children_lifted'])} children, out of poverty in the public-use data. Census publishes rounded internal-file figures of 6.1 million and 3.3 million. Both pass predeclared public-use/internal tolerances; no weights or benefits were adjusted to pass them. This validates source-year accounting, not the Project's assumed delivery or future effects.

The suite passes 102 tests, including nonlinear receipt-mixture, household award-cap, shared-care, claimant-link, credit-boundary and temporary-aid checks. The empirical checker additionally verifies all eight main cases, 42 sensitivities, population/count identities, paired changes, stage monotonicity and the end of temporary aid. An average income gain is never substituted for the recipient/nonrecipient poverty mixture.

Run from the repository root:

```bash
python3 index/tools/child-poverty/run_validation.py
python3 index/tools/child-poverty/agenda_analysis.py --archive /path/to/asecpub26csv.zip --output index/tools/child-poverty/empirical/agenda-results.json
python3 index/tools/child-poverty/check_agenda_results.py --results index/tools/child-poverty/empirical/agenda-results.json
python3 index/tools/child-poverty/report_agenda.py --results index/tools/child-poverty/empirical/agenda-results.json --markdown sources/family-child-poverty-agenda-effects.md --html index/child-poverty-agenda-analysis.html
```

The assumptions file names every research convention and its basis. The result file records the official archive hash, assumptions hash and official input-subset hashes. The package manifest supplies code/output integrity hashes. The source data remain outside Git; the official archive URL is recorded in the baseline report.

Primary references: [Census 2025 poverty report](https://www2.census.gov/library/publications/2026/demo/p60-290.pdf), [Census SPM technical documentation](https://www2.census.gov/programs-surveys/supplemental-poverty-measure/datasets/spm/spm_techdoc.pdf), [2026 ASEC dictionary](https://www2.census.gov/programs-surveys/cps/datasets/2026/march/asec2026_ddl_pub_full.pdf), [2025 HHS poverty guidelines](https://public-inspection.federalregister.gov/2025-01377.pdf), and [CBO official machine-readable data](https://www.cbo.gov/data/budget-economic-data). Project policy authority is the governing document and canonical FAM, EDU and HOU files; the carbon extension uses index/climate-carbon-model.md.

The four child-poverty report exports were available locally. The attached bibliography again returned no readable content, and its saved-file download failed; it was not treated as evidence. The analysis implements Espen's direction to complete bounded agenda scenarios without overbuilding a speculative target-year current-law forecast. It adopts no new policy, eligibility rule or poverty target.
'''


def fragment(r):
    # Only compact aggregate results enter the in-conversation visual.
    compact={str(y):dict(cases=[dict(name=c['scenario'],baseline=c['baseline'],result=c['stages'][-1])
        for c in r['cases'] if c['year']==y],
        stages=next(c['stages'] for c in r['cases'] if c['year']==y and c['scenario']=='moderate'),
        sensitivity=[dict(name=s['name'],rate=s['result']['poor_rate']) for s in r['sensitivities']
            if s['year']==y and s['name'] in ('index_from_2025','carbon_plus_health15pct','carbon_plus_health30pct')])
        for y in (2030,2034)}
    return '''<div id="poverty-effects-2050">
<style>
#poverty-effects-2050 { color:var(--foreground); }
#poverty-effects-2050 .head { display:flex; flex-wrap:wrap; align-items:center; gap:16px; padding-right:90px; }
#poverty-effects-2050 .chart { margin:20px 0 28px; }
#poverty-effects-2050 .row { margin:15px 0; }
#poverty-effects-2050 .labels { display:flex; flex-wrap:wrap; justify-content:space-between; gap:6px 16px; margin-bottom:6px; }
#poverty-effects-2050 .track { background:var(--muted); height:14px; position:relative; }
#poverty-effects-2050 .fill { height:14px; background:var(--viz-series-1); transition:width .3s; }
#poverty-effects-2050 .baseline { background:var(--muted-foreground); }
#poverty-effects-2050 .whisker { height:2px; background:var(--foreground); position:absolute; top:6px; }
#poverty-effects-2050 .axis { display:flex; justify-content:space-between; margin-top:8px; color:var(--muted-foreground); }
#poverty-effects-2050 h3 { margin-top:24px; }
#poverty-effects-2050 .note { color:var(--muted-foreground); margin-top:8px; }
@media (prefers-reduced-motion:reduce) { #poverty-effects-2050 .fill { transition:none; } }
</style>
<p><strong>Historical pre-adoption experiment:</strong> FAM-1A and 400,000 voucher awards. <a href="../sources/family-comparison-model-checks.md">Current adopted AFA/one-million package comparisons</a>.</p>
<div class="head"><h2>Conditional child-poverty effects</h2><div><label class="form-label" for="poverty-year">Policy phasing</label><select class="form-select" id="poverty-year"><option>2030</option><option>2034</option></select></div></div>
<div class="note text-small">CPS-based scenarios · not a future poverty forecast · primary credit indexed from 2030</div>
<div id="poverty-bars" class="chart" role="img" aria-label="Child SPM poverty rates by conditional delivery case"></div>
<div class="note text-small">Bars: child SPM poverty · whiskers: conditional 95% sampling intervals</div>
<h3>Cumulative channels — moderate delivery</h3>
<table class="table table-sm"><thead><tr><th scope="col">Channels included</th><th scope="col" class="text-end">Poverty</th><th scope="col" class="text-end">Deep poverty</th></tr></thead><tbody id="poverty-stages"></tbody></table>
<h3>Selected assumptions — moderate delivery</h3>
<table class="table table-sm"><thead><tr><th scope="col">Change</th><th scope="col" class="text-end">Child poverty</th></tr></thead><tbody id="poverty-sensitivity"></tbody></table>
<div id="poverty-summary" class="note text-small" aria-live="polite"></div>
<script>
(function(){
const root=document.getElementById('poverty-effects-2050');
const data=__DATA__;
const pct=x=>(100*x).toFixed(2)+'%';
const names={stressed:'Stressed delivery',moderate:'Moderate delivery',enhanced:'Enhanced delivery',full:'Full modeled receipt/access'};
const sensNames={index_from_2025:'Credit indexed from 2025',carbon_plus_health15pct:'Carbon proxy + 15% medical-cost relief',carbon_plus_health30pct:'Carbon proxy + 30% medical-cost relief'};
const extrema=Object.values(data).flatMap(x=>x.cases.flatMap(c=>[c.baseline.sampling_uncertainty.poor_rate.upper95,c.result.sampling_uncertainty.poor_rate.upper95]));
const max=Math.ceil(Math.max(...extrema)*100/5)*5;
function draw(){
 const year=root.querySelector('#poverty-year').value,d=data[year];
 const rows=[{label:'Baseline in this population scenario',value:d.cases[0].baseline,base:true},...d.cases.map(c=>({label:names[c.name],value:c.result}))];
 root.querySelector('#poverty-bars').innerHTML=rows.map(row=>{
  const v=row.value,ci=v.sampling_uncertainty.poor_rate;
  return '<div class="row"><div class="labels"><span>'+row.label+'</span><span class="tabular-nums">'+pct(v.poor_rate)+' · '+(v.poor_children/1e6).toFixed(2)+'m children</span></div><div class="track"><div class="fill '+(row.base?'baseline':'')+'" style="width:'+((100*v.poor_rate)/max*100)+'%"></div><div class="whisker" style="left:'+(100*ci.lower95/max*100)+'%;width:'+(100*(ci.upper95-ci.lower95)/max*100)+'%"></div></div></div>';
 }).join('')+'<div class="axis text-small"><span>0%</span><span>'+max/2+'%</span><span>'+max+'%</span></div>';
 root.querySelector('#poverty-stages').innerHTML=d.stages.map(s=>'<tr><th scope="row">'+s.label+'</th><td class="text-end tabular-nums">'+pct(s.poor_rate)+'</td><td class="text-end tabular-nums">'+pct(s.deep_poor_rate)+'</td></tr>').join('');
 root.querySelector('#poverty-sensitivity').innerHTML=d.sensitivity.map(s=>'<tr><th scope="row">'+sensNames[s.name]+'</th><td class="text-end tabular-nums">'+pct(s.rate)+'</td></tr>').join('');
 const c=d.cases.find(x=>x.name==='moderate');
 root.querySelector('#poverty-summary').textContent=((c.baseline.poor_children-c.result.poor_children)/1e6).toFixed(2)+' million net fewer poor children · conditional '+year+' moderate case';
}
root.querySelector('#poverty-year').addEventListener('change',draw);draw();
})();
</script>
</div>
'''.replace('__DATA__',json.dumps(compact,separators=(',',':')))


def standalone(view):
    return '''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Project 2050 child-poverty scenarios</title><style>
:root { color-scheme:light dark; --foreground:light-dark(#202c39,#edf1f5); --muted:light-dark(#e9edf1,#323d47); --muted-foreground:light-dark(#596b7c,#b0bdc9); --viz-series-1:light-dark(#237c7d,#6cc8c3); --border:light-dark(#ccd5de,#4a5662); background:light-dark(#ffffff,#19212a); }
body { max-width:850px; margin:36px auto; padding:0 20px; font:16px/1.5 system-ui,sans-serif; } h2,h3,th { font-weight:500; } .text-small { font-size:13px; } .tabular-nums { font-variant-numeric:tabular-nums; } .table { width:100%; border-collapse:collapse; } th,td { text-align:left; padding:9px 6px; border-bottom:1px solid var(--border); } .text-end { text-align:right; } select { padding:8px; font:inherit; } label { display:block; } a { color:inherit; }
</style></head><body>'''+view+'''<p>These are conditional static experiments, not a complete forecast or a fiscal score. Receipt, legal coverage, usable services and proxy household inputs remain assumptions. The headline covers FAM-1A/FAM-2A/EDU-3A/HOU-4A plus employee leave contributions; carbon and health are separate sensitivities.</p><p><a href="../sources/family-child-poverty-agenda-effects.md">Read the complete methods, results and limits</a></p></body></html>'''


if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--results',required=True);p.add_argument('--markdown');p.add_argument('--html');p.add_argument('--fragment')
    args=p.parse_args();r=load_json(args.results);check(r)
    for path,content in ((args.markdown,markdown(r)),(args.html,standalone(fragment(r))),(args.fragment,fragment(r))):
        if path:
            Path(path).parent.mkdir(parents=True,exist_ok=True);Path(path).write_text(content,encoding='utf-8')
    print('Rendered validated agenda analysis')
