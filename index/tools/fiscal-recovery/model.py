#!/usr/bin/env python3
"""Selected education scope + explicitly conditional financing; additive accounting bridge.
Never overwrites the pre-adoption common-suite comparison or its inputs.
"""
import argparse, contextlib, csv, hashlib, importlib.util, io, json, os, sys, tempfile
from pathlib import Path
ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT/'index/tools'))
A = json.loads((HERE/'assumptions.json').read_text())
ADOPTION = json.loads((ROOT/'index/data/inputs/education-adoption.json').read_text())
E = dict(ADOPTION['cost_assumptions'], **A['education'])
W = range(2030,2040)
Y = range(2026,2057)

def module(name, path):
    spec = importlib.util.spec_from_file_location(name,path)
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    return m

def geometric(points,y):
    points={int(k):v for k,v in points.items()}
    if y in points: return points[y]
    a=max(k for k in points if k<y); b=min(k for k in points if k>y)
    return points[a]*(points[b]/points[a])**((y-a)/(b-a))

def phase(y,start,n): return min(1,max(0,(y-start+1)/n))

def education(rate=2, start=2031, bridge=True, payroll_growth=None,
              cost_growth=None, recession=False, cost_multiplier=1, interest_shift=0, gf_share=0, care_share_floor=0):
    pg=E['payroll_growth'] if payroll_growth is None else payroll_growth
    cg=E['outlay_growth_after_2049'] if cost_growth is None else cost_growth
    rows=[]; reserve=0; depletion=None
    for y in range(2030,2105):
        out=(geometric(E['outlays_bn'],y) if y<=2049 else E['outlays_bn']['2049']*(1+cg)**(y-2049))*cost_multiplier
        federal_share=1 if y<=2034 else max(.6,.9-.05*(y-2035))
        care=(geometric({2030:12,2033:88,2036:106,2040:106,2045:123,2049:143},y) if y<=2049 else 143*1.032**(y-2049))
        extra_care=care*max(0,care_share_floor-federal_share)/federal_share
        out+=extra_care
        shock={2036:.97,2037:.95,2038:.97,2039:.99}.get(y,1) if recession else 1
        receipts=rate*phase(y,start,E['phase_years'] if start==E['phase_start'] else 1)*E['payroll_bn_per_point_2030']*(1+pg)**(y-2030)*shock
        # A fixed end date makes the transition cost visible. No implicit perpetual GF guarantee.
        grant=max(gf_share*out,max(0,out-receipts) if bridge and y<=E['bridge_last_year'] else 0)
        ir=(F.marginal_rate(B,y) if y<=2056 else E['interest_after_2056'])+interest_shift
        interest=reserve*ir
        reserve+=interest+receipts+grant-out
        if reserve < -1e-7 and depletion is None: depletion=y
        rows.append(dict(year=y,rate_points=rate*phase(y,start,E['phase_years'] if start==E['phase_start'] else 1),
                         outlays_bn=out,extra_care_bn=extra_care,payroll_bn=receipts,gf_bridge_bn=grant,interest_bn=interest,
                         reserve_bn=reserve,reserve_to_outlays=reserve/out))
    return dict(rate_points=rate,start=start,bridge=bridge,payroll_growth=pg,cost_growth_after2049=cg,
                cost_multiplier=cost_multiplier,interest_shift=interest_shift,recession=recession,gf_share=gf_share,care_share_floor=care_share_floor,
                first_negative_reserve=depletion,minimum_reserve_bn=min(r['reserve_bn'] for r in rows),
                terminal_ratio=rows[-1]['reserve_to_outlays'],
                nondeclining_terminal_ratio=rows[-1]['reserve_to_outlays']>=rows[-6]['reserve_to_outlays'],
                payroll_2030_39_tn=sum(r['payroll_bn'] for r in rows if r['year'] in W)/1000,
                bridge_2030_39_tn=sum(r['gf_bridge_bn'] for r in rows if r['year'] in W)/1000,rows=rows)

def fund_experiments():
    # funds-model.py writes at import; isolate all those side effects in a temporary directory.
    import shutil
    with tempfile.TemporaryDirectory() as tmp:
        for name in ('ledger.json','fiscal-model.json','moving-america.json'):
            shutil.copyfile(ROOT/'build'/name,Path(tmp)/name)
        before=os.getcwd()
        try:
            os.chdir(tmp)
            with contextlib.redirect_stdout(io.StringIO()): funds=module('recovery_funds',ROOT/'index/tools/funds-model.py')
        finally: os.chdir(before)
    paths=[funds.SSF[k] for k in ('SS-1','SS-2','SS-3','SS-4','SS-5')]
    sa=A['social_security']
    loss=lambda y:(-sa['interaction_loss_payroll_points'] if y>=2031 else 0,0)
    def run(rate,start=sa['broad_rate_start']):
        return funds.run_ss(paths+[loss,lambda y:(rate*phase(y,start,sa['broad_rate_phase_years']),0)])
    lo,hi=0,5
    for _ in range(45):
        mid=(lo+hi)/2
        if run(mid)['sustainable']: hi=mid
        else: lo=mid
    rounded=__import__('math').ceil(hi*10)/10
    def compact(r):
        return {k:v for k,v in r.items() if k!='rows'} | {'years':{x['year']:x for x in r['rows']}}
    ss={'D8':compact(funds.run_ss(paths[:4])), 'D8_plus_SS5_joint_haircut':compact(run(0)),
        'plus_1_point':compact(run(1)), 'solved_rate_points':hi,'rounded_rate_points':rounded,
        'rounded_case':compact(run(rounded)), 'later_2040_case':compact(run(rounded,2040))}
    leave={}
    for cap in (.85,1.10,1.20):
        funds.P['leave_cap']=cap
        leave[str(cap)]=funds.run_leave('high')
    old=funds.HIS
    funds.HIS=lambda y: old(y)*(.5+.35)/1.2
    hi_low=funds.run_hi(True)
    funds.HIS=old
    hi_cases={k:compact(v) for k,v in funds.hi.items()}
    hi_cases['Half HLT6 HI savings']=compact(hi_low)
    return dict(ss=ss,leave=leave,hi=hi_cases,htf_last_year=max(x['fy'] for x in funds.htf),
                caveat='SS extra rate is capped-base, education uncapped. Joint income-tax offsets and cross-tax responses are not scored. These fund experiments are NOT summed into the education/unified fiscal scenarios.')

def check_comparison_inputs(provenance,rebased,read):
    """Refuse a changed comparison input unless comparison-rebase.json records its exact new hash."""
    for path,expected in provenance.items():
        if path.startswith('index/data/') and path.endswith('.csv'):
            actual=hashlib.sha256(read(path)).hexdigest()
            if actual!=expected and rebased.get(path)!=actual:
                raise ValueError('Comparison input changed; reconcile/rebase education bridge explicitly: '+path)

def run():
    # Do not silently relabel a future changed numerical baseline as this comparison vintage.
    provenance=json.loads((ROOT/'sources/strategic-review-arithmetic.json').read_text())['source_sha256']
    rebased={e['path']:e['sha256'] for e in json.loads((HERE/'comparison-rebase.json').read_text())['entries']} if (HERE/'comparison-rebase.json').exists() else {}
    check_comparison_inputs(provenance,rebased,lambda path:(ROOT/path).read_bytes())
    global F,B
    F=module('recovery_fiscal',ROOT/'index/tools/fiscal-model.py')
    B=F.read_baseline(ROOT/'index/data/fiscal-baseline.csv')
    model=json.loads((ROOT/'build/fiscal-model.json').read_text())
    ledger=json.loads((ROOT/'build/ledger.json').read_text())
    old=model['results']['DEC']['years']; oldrows={r['id']:r for r in model['rows']}
    transfer={y:sum(oldrows[k]['gf'][str(y)] for k in E['transferred_agenda']) for y in Y}
    scale=E['absorbed_current_law_2030_39_tn']*1000/sum((1+E['absorbed_current_law_growth'])**(y-2030) for y in W)
    absorbed={y:scale*(1+E['absorbed_current_law_growth'])**(y-2030) if y>=2030 else 0 for y in Y}
    cases={
        'source_1.4_immediate_no_estate':education(1.4,2030,False),
        'phased_1.4_with_bridge':education(1.4),
        'phased_1.8_with_bridge':education(1.8),
        'phased_2.0_with_bridge':education(2),
        'phased_2.0_recession':education(2,recession=True),
        'phased_2.0_cost_plus10':education(2,cost_multiplier=1.1),
        'phased_2.0_low_payroll_high_cost':education(2,payroll_growth=.035,cost_growth=.042),
        'phased_2.0_interest_minus1':education(2,interest_shift=-.01),
        'phased_2.0_no_bridge':education(2,bridge=False),
        'mixed_1.4_GF30':education(1.4,gf_share=.30),
        'mixed_1.4_GF30_care_floor80':education(1.4,gf_share=.30,care_share_floor=.8),
        'mixed_1.4_GF30_care_floor100':education(1.4,gf_share=.30,care_share_floor=1),
        'mixed_1.4_GF30_recession':education(1.4,gf_share=.30,recession=True),
        'mixed_1.4_GF30_cost_plus10':education(1.4,gf_share=.30,cost_multiplier=1.1),
        'mixed_1.4_GF30_low_payroll_high_cost':education(1.4,gf_share=.30,payroll_growth=.035,cost_growth=.042)}
    ref={r['year']:r for r in cases['mixed_1.4_GF30']['rows']}
    bridge=[]
    for y in Y:
        rr=ref.get(y,{}); out=rr.get('outlays_bn',0); pay=rr.get('payroll_bn',0); grant=rr.get('gf_bridge_bn',0)
        new=out-transfer[y]-absorbed[y]
        offset=pay*E['employer_tax_offset_fraction']; protection=pay*E['household_protection_reserve_fraction']
        gf=-transfer[y]-absorbed[y]+grant+offset+protection
        uni=new-pay+offset+protection
        bridge.append(dict(year=y,fund_outlays_bn=out,old_agenda_transfer_bn=transfer[y],current_law_absorbed_bn=absorbed[y],
                           new_benefits_bn=new,payroll_bn=pay,gf_bridge_bn=grant,tax_offset_bn=offset,
                           protection_reserve_bn=protection,gf_delta_bn=gf,unified_delta_bn=uni,
                           fund_primary_deficit_bn=out-pay-grant))
    accounting={}
    for name,c in cases.items():
        win=[x for x in c['rows'] if x['year'] in W]
        out=sum(x['outlays_bn'] for x in win)/1000
        pay=c['payroll_2030_39_tn']; grants=c['bridge_2030_39_tn']
        oldcost=sum(transfer[y]+absorbed[y] for y in W)/1000
        off=pay*E['employer_tax_offset_fraction']; protect=pay*E['household_protection_reserve_fraction']
        accounting[name]=dict(outlays_tn=out,payroll_tn=pay,grants_tn=grants,offset_tn=off,protection_tn=protect,
            net_gf_relief_tn=oldcost-grants-off-protect,unified_improvement_tn=pay-(out-oldcost)-off-protect)
    # Household diagnostic: preserve old benefit rows; add ONLY the new spending increment and full worker tax incidence.
    before=os.getcwd()
    try:
        os.chdir(ROOT/'build')
        inc=module('incidence',ROOT/'build/incidence.py'); sys.modules['incidence']=inc
        yrs=module('recovery_years',ROOT/'build/years.py')
        old_inc=yrs.series(inc.QO)
    finally: os.chdir(before)
    by={r['year']:r for r in bridge}
    incidence={}
    for y in W:
        new=by[y]['new_benefits_bn']/1000
        # Existing option allocation .24/.39 normalised to the actual incremental cost, not a second whole package.
        ben=inc.dist([('childcare',new*.24/.63),('education',new*.39/.63)])
        cost=inc.dist([('wages',by[y]['payroll_bn']/1000)])
        incidence[y]={q:dict(old_net=old_inc[y][q],new_net_before_unallocated_protection=old_inc[y][q]+round((ben[q]-cost[q])*1e12/(inc.HH*.2))) for q in inc.GROUPS}
    rc=A['recovery']; stress={y:0 for y in Y}; deferred={y:0 for y in Y}; removed={y:0 for y in Y}
    for rid,amt in rc['extra_low_receipts_tn'].items():
        profiles=F.PR.BILLS if rid=='HLT-6' else F.PR.REVENUE if rid in F.PR.REVENUE else F.PR.CUTS
        p=F.row_path(B,amt,profiles[rid],rid)
        for y in Y: stress[y]+=p[y]
    g11=next(r for r in ledger['revenue'] if r['id']=='G11')['mid']
    gp=F.row_path(B,g11,F.PR.REVENUE['G11'],'G11')
    for y in Y:
        if y>=2040: stress[y]+=gp[y]*rc['g11_post2039_loss_fraction']
    for rid in rc['middle_tax_rows']:
        p=model['opt_rows'][rid]['gf']
        for y in Y:
            removed[y]+=-p[str(y)]
            deferred[y]+=-p[str(y)]*(1-phase(y,rc['middle_tax_phase_start'],rc['middle_tax_phase_years']))
    first=json.loads((ROOT/'sources/strategic-review-arithmetic.json').read_text())
    housing={int(y):v for y,v in first['housing'][0]['path_bn'].items()}
    scenarios=[]
    for name,lost,extra,delay in [
        ('Education reference',False,False,'none'),
        ('Recovery: delay C19b/C20',False,False,'delay'),
        ('Recovery downside',True,False,'delay'),
        ('Recovery plus housing/service space',False,True,'delay'),
        ('Recovery plus housing/service space downside',True,True,'delay'),
        ('Replace C19b/C20 plus housing/service space downside',True,True,'remove')]:
        gf={}; uni={}
        for y in Y:
            extra_cost=(housing[y]+B[y]['gdp']*.001*phase(y,2030,5)) if extra else 0
            change=(stress[y] if lost else 0)+extra_cost+(deferred[y] if delay=='delay' else removed[y] if delay=='remove' else 0)
            gf[y]=old[str(y)]['gf_primary']+by[y]['gf_delta_bn']+change
            uni[y]=old[str(y)]['prog_primary']+by[y]['unified_delta_bn']+change
        pi,pd=F.debt_roll(B,uni)
        _,pd_hi=F.debt_roll(B,uni,shift=1)
        binding=max(range(2040,2057),key=lambda y:gf[y]/B[y]['gdp'])
        need=max(0,100*gf[binding]/B[binding]['gdp']+rc['maturity_margin_gdp_percent'])
        paths={}
        for y in Y:
            d=old[str(y)]['base_debt']+pd[y]
            deficit=old[str(y)]['base_deficit']+uni[y]+pi[y]
            previous=(old[str(y-1)]['base_debt']+pd[y-1]) if y>2026 else d
            growth=B[y]['gdp']/B[y-1]['gdp']-1 if y>2026 else 0
            paths[y]=dict(gf_primary_bn=gf[y],unified_program_primary_bn=uni[y],total_debt_bn=d,
                          total_debt_gdp=100*d/B[y]['gdp'],total_deficit_bn=deficit,
                          total_interest_bn=old[str(y)]['base_interest']+pi[y],
                          extra_primary_adjustment_for_flat_debt_ratio_gdp=100*(deficit-growth*previous)/B[y]['gdp'],
                          program_debt_bn=pd[y],program_debt_rate_plus1_bn=pd_hi[y])
        # Additional NET resources, phased 2035-44, sufficient for nonincreasing
        # debt/GDP in every modeled year 2045-56. No tax instrument or fund credit inferred.
        def stabilized(k):
            u={y:uni[y]-k/100*B[y]['gdp']*phase(y,2035,10) for y in Y}
            ii,dd=F.debt_roll(B,u)
            return {y:100*(old[str(y)]['base_debt']+dd[y])/B[y]['gdp'] for y in Y}
        lo,hi_=0,10
        for _ in range(42):
            mid=(lo+hi_)/2; rr=stabilized(mid)
            if all(rr[y]<=rr[y-1]+1e-9 for y in range(2045,2057)): hi_=mid
            else: lo=mid
        scenarios.append(dict(name=name,stabilizing_net_gdp_percent=hi_,stabilized_debt_gdp=stabilized(hi_),net_new_gdp_requirement_with_margin=need,binding_year=binding,
            gf_2030_39_primary_tn=sum(gf[y] for y in W)/1000,
            unified_2030_39_delta_vs_pre_education_tn=sum(uni[y]-old[str(y)]['prog_primary'] for y in W)/1000,
            maturity_pass=all(gf[y]<=0 for y in range(2040,2057)),years=paths))
    for scenario in scenarios: scenario.update(F.CL.disclosure())
    files=['index/tools/climate-integration.py','index/data/inputs/climate-adoption.json','sources/climate-portfolio-pricing.json','index/tools/fiscal-recovery/model.py','index/tools/fiscal-recovery/assumptions.json','index/data/inputs/education-adoption.json',
        'index/tools/fiscal-model.py','index/tools/funds-model.py','index/tools/incidence-model.py',
        'index/tools/incidence-years.py','index/tools/inputs.py','index/tools/fiscal-profiles.py',
        'index/data/fiscal-baseline.csv','build/ledger.json','build/fiscal-model.json',
        'sources/strategic-review-arithmetic.json','sources/education-transforming-education-act-analysis-and-trust-fund.md']
    files += [str(p.relative_to(ROOT)) for p in sorted((ROOT/'index/data/inputs').glob('*.csv'))]
    return dict(assumptions=A,adoption=ADOPTION,education_cases=cases,education_bridge=bridge,
                totals_2030_39_tn={k:sum(r[k] for r in bridge if r['year'] in W)/1000 for k in bridge[0] if k!='year'},
                education_accounting_cases=accounting,incidence_diagnostic=incidence,fiscal_scenarios=scenarios,funds=fund_experiments(),
                delayed_middle_receipts_2030_39_tn=sum(deferred[y] for y in W)/1000,
                source_sha256={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in files})

def inventory(path):
    fields=['kind','id','label','status','channel','low_tn','mid_tn','high_tn','basis_or_overlap']
    rows=[]
    for name,kind in [('ledger-bills.csv','bill'),('ledger-revenue.csv','revenue'),('ledger-cuts.csv','option'),('ledger-dynamic.csv','dynamic')]:
        for r in csv.DictReader((ROOT/'index/data/inputs'/name).open()):
            mid=r.get('cost_mid',r.get('mid',r.get('saves_tn','')))
            # Preserve formulas/source strings instead of inventing a second score.
            rows.append(dict(kind=kind,id=r['id'],label=r.get('bill',r.get('option',r.get('change',r.get('effect','')))),
                status=('Transferred into adopted EDU-9B; use education bridge' if r['id'] in E['transferred_agenda'] else
                        'Payroll institution adopted; rates in this legacy row superseded by conditional scenarios' if r['id']=='ED1' else
                        r.get('kind', 'Base' if r.get('in_base')=='yes' else 'Dedicated/option; see canonical domain' if kind=='revenue' else 'Legacy agenda' if kind=='bill' else 'Sensitivity; never a pay-for')),
                channel=r.get('channel','General fund' if kind in ('dynamic','option') else ''),
                low_tn=r.get('cost_lo',r.get('lo','')),mid_tn=mid,high_tn=r.get('cost_hi',r.get('hi','')),
                basis_or_overlap=r.get('note',r.get('overlap',r.get('why',r.get('basis',''))))))
    with path.open('w') as f:
        w=csv.DictWriter(f,fieldnames=fields,lineterminator='\n'); w.writeheader(); w.writerows(rows)

def render(r):
    t=r['totals_2030_39_tn']; out=['# Fiscal recovery: integrated education bridge and financing tests','',
        '> **Climate risk disclosure:** CLI-7C contingent exposure is $75–150B, unscored; its annual expected cost is included in the integrated comparison.','',
        '> **Superseded calculation:** The aggregate education residual below is retained as the earlier experiment. Use the [Recovery and Solvency budget](recovery-budget.md) for component-level current-law reconciliation and integrated SS/HI/leave fiscal flows. Its revised education cost is conditional on stated care/current-law boundaries. Neither supplement adopts financing rates or certifies D3/D4.','',
        'Generated by `index/tools/fiscal-recovery/model.py`. Full EDU-9B benefit scope and payroll institution are adopted. **Every rate, timing, transition grant, protection allowance and further reform here is conditional.** The pre-education common-suite DEC/Q outputs remain the comparison vintage, not complete current-policy totals. Read the [recommendations](../sources/fiscal-recovery-and-education-redesign.md) for policy judgments and source limits.','',
        'Nominal dollars; FY2030–39 totals in trillions. No estate receipts are moved or counted twice.','',
        '| Education mixed reference: 1.4 points, phased 2031–35, plus 30% GF share | $T |','| --- | ---: |']
    for k in ('fund_outlays_bn','old_agenda_transfer_bn','current_law_absorbed_bn','new_benefits_bn','payroll_bn','gf_bridge_bn','tax_offset_bn','protection_reserve_bn','gf_delta_bn','unified_delta_bn'):
        out.append(f"| {k.removesuffix('_bn').replace('gf_bridge','gf grants including transition').replace('_',' ')} | {t[k]:.3f} |")
    out+=['','Negative delta improves the balance. GF relief includes transfers; unified improvement only counts new external receipts minus additional benefits and allowances. Bridge grants cancel inside the consolidated government. Fund interest is intragovernmental; it is not new unified revenue.','',
        '| FY | Gross fund outlays | New benefits | Payroll | GF grants | Net GF relief | Unified improvement |','| --- | ---: | ---: | ---: | ---: | ---: | ---: |']
    for row in r['education_bridge']:
        if row['year'] in (2030,2031,2033,2035,2040,2049,2056):
            out.append('| '+str(row['year'])+' | '+' | '.join(f'{row[k]*sign:.1f}' for k,sign in [('fund_outlays_bn',1),('new_benefits_bn',1),('payroll_bn',1),('gf_bridge_bn',1),('gf_delta_bn',-1),('unified_delta_bn',-1)])+' |')
    out+=['','## Education reserve tests','',
        'Seventy-five years, 2030–2104. Post-2049 extrapolations are assumptions, not a forecast or actuarial certification. Negative balances are unmet financing, never statutory spending authority. Extra transition grants stop after 2034; mixed cases continue a permanent 30% general-fund share.','',
        '| Case | Payroll 2030–39 ($T) | Total GF grants ($T) | First negative reserve | Reserve / spending 2104 | Terminal ratio stable/rising? |','| --- | ---: | ---: | --- | ---: | --- |']
    for name,c in r['education_cases'].items():
        out.append(f"| {name} | {c['payroll_2030_39_tn']:.3f} | {c['bridge_2030_39_tn']:.3f} | {c['first_negative_reserve'] or 'none'} | {c['terminal_ratio']:.2f} | {c['nondeclining_terminal_ratio']} |")
    out+=['','## General-fund and whole-government paths','',
        f"Delaying C19b/C20 to a three-year 2033–35 phase-in forgoes ${r['delayed_middle_receipts_2030_39_tn']:.3f}T; these receipts are not moved to the back of the window. Further net revenue requirements include a 0.1%-GDP maturity margin, but no revenue is inserted to meet them.", '',
        '| Case | GF primary 2030–39 ($T) | Extra net receipts needed at maturity (% GDP) | FY2040 GF gap ($B) | Total debt/GDP 2056 | FY2056 extra primary adjustment for flat debt/GDP |','| --- | ---: | ---: | ---: | ---: | ---: |']
    for c in r['fiscal_scenarios']:
        out.append(f"| {c['name']} | {c['gf_2030_39_primary_tn']:.3f} | {c['net_new_gdp_requirement_with_margin']:.3f}% | {c['years'][2040]['gf_primary_bn']:.1f} | {c['years'][2056]['total_debt_gdp']:.1f}% | {c['years'][2056]['extra_primary_adjustment_for_flat_debt_ratio_gdp']:.2f}% GDP |")
    out+=['','| Case | Additional net resources phased 2035–44 (% GDP at maturity) | Debt/GDP 2056 after illustrative adjustment |','| --- | ---: | ---: |']
    for c in r['fiscal_scenarios']:
        out.append(f"| {c['name']} | {c['stabilizing_net_gdp_percent']:.2f}% | {c['stabilized_debt_gdp'][2056]:.1f}% |")
    out+=['','The second table solves for nonincreasing debt/GDP in every year 2045–56, with additional net resources phased 2035–44. These are financing requirements after any offsets and protection, not tax rates or scored receipts; SS/HI reforms are not added again. No behavior, inflation or implementation forecast is implied.','', 'Debt-stabilizing adjustment is a one-year diagnostic, not a scored reform or simulated path after implementation. Inherited SS/HI cash conventions remain; fund experiments below are not added to these paths. Rate-plus-one JSON paths stress only the program increment. No D3/D4 or whole-government solvency certification.','',
        '## Household diagnostic','',
        'Average annual net benefit by quintile, dollars per household. All existing benefits/taxes retained, plus only incremental education benefits and the full employer/employee payroll burden. The 20% protection reserve is not distributed to households without a microdata score. Service value at cost is not cash or proof of receipt.','',
        '| FY | Q1 | Q2 | Q3 | Q4 |','| --- | ---: | ---: | ---: | ---: |']
    for y in W:
        out.append(f'| {y} | '+' | '.join(f"{r['incidence_diagnostic'][y][q]['new_net_before_unallocated_protection']:,}" for q in ('Q1','Q2','Q3','Q4'))+' |')
    ss=r['funds']['ss']
    out+=['','## Trust-fund redesign comparisons','',
        f"Social Security: D8 plus SS-5, with a 0.34-point joint-interaction haircut, needs approximately **{ss['solved_rate_points']:.2f} additional payroll points** in the model's 2035–44 phase-in to pass its conservative test (no depletion, terminal reserve ≥ one year's cost, nondeclining final ratio within the engine's tolerance). A rounded **{ss['rounded_rate_points']:.1f}-point** case is compared below. These are additions to the current 12.4% capped-base OASDI rate, split between employer/employee; education uses an uncapped base. Not a joint SSA score.",'',
        '| SS case | Depletion | Actuarial balance (% payroll) | Conservative solvency test |','| --- | --- | ---: | --- |']
    for name in ('D8','D8_plus_SS5_joint_haircut','plus_1_point','rounded_case','later_2040_case'):
        c=ss[name]; out.append(f"| {name} | {c['depletion'] or 'none to 2100'} | {c['balance']:.2f} | {c['sustainable']} |")
    out+=['','| Paid leave, high take-up | Loan 2039 ($B) | Loan 2050 ($B) | Loan 2060 ($B) |','| --- | ---: | ---: | ---: |']
    for cap,c in r['funds']['leave'].items():
        out.append(f"| Rate cap {cap}% | {c['loan_2039']:.1f} | {c['loan_2050']:.1f} | {c['rows'][-1]['loan']:.1f} |")
    out+=['','| Medicare HI | Depletion | Model balance (% payroll) |','| --- | --- | ---: |']
    for name,c in r['funds']['hi'].items():out.append(f"| {name} | {c['depletion'] or 'none to 2100'} | {c['balance']:.2f} |")
    out+=['','HI baseline does not reproduce the Trustees exactly; use improvement against its own baseline, not the absolute balance as certification. Transportation is modeled only to 2046: renewal coverage then does not prove 75-year solvency. The CSV [financial inventory](../sources/fiscal-recovery-inventory.csv) preserves all 148 bill/revenue/option/dynamic rows without summing alternatives. Full assumptions, annual paths and source hashes are in the [JSON](data/fiscal-recovery-model.json).','']
    return '\n'.join(out)

if __name__=='__main__':
    p=argparse.ArgumentParser(); p.add_argument('--output-dir',type=Path); args=p.parse_args()
    r=run()
    if args.output_dir:
        args.output_dir.mkdir(parents=True,exist_ok=True); md=args.output_dir/'fiscal-recovery-model.md'; js=args.output_dir/'fiscal-recovery-model.json'; inv=args.output_dir/'fiscal-recovery-inventory.csv'
    else: md=ROOT/'index/fiscal-recovery-model.md'; js=ROOT/'index/data/fiscal-recovery-model.json'; inv=ROOT/'sources/fiscal-recovery-inventory.csv'
    md.write_text(render(r)); js.write_text(json.dumps(r,indent=2)+'\n'); inventory(inv)
    print(md)
