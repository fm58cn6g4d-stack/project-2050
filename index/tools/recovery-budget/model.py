#!/usr/bin/env python3
"""Exploratory total-federal-budget bridge. Nominal $B, fiscal years unless labeled.
Run common suite first. Historical inputs/outputs are never overwritten here.
"""
import argparse, contextlib, csv, hashlib, importlib.util, io, json, os, shutil, sys, tempfile
from pathlib import Path
ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
A = json.loads((HERE/'assumptions.json').read_text())
ADOPTION = json.loads((ROOT/'index/data/inputs/recovery-adoption.json').read_text())
A['spending'] = ADOPTION['spending']
A['leave']['cap_points'] = ADOPTION['leave_cap_points']
Y = range(2026,2057)
W = range(2030,2040)

def module(name,path):
    s=importlib.util.spec_from_file_location(name,path)
    m=importlib.util.module_from_spec(s); sys.modules[name]=m; s.loader.exec_module(m)
    return m

def phase(y,start,n): return min(1,max(0,(y-start+1)/n))
def geometric(points,y):
    if y in points: return points[y]
    lo=max(k for k in points if k<y); hi=min(k for k in points if k>y)
    return points[lo]*(points[hi]/points[lo])**((y-lo)/(hi-lo))

def load():
    sys.path.insert(0,str(ROOT/'index/tools'))
    f=module('rb_fiscal',ROOT/'index/tools/fiscal-model.py')
    b=f.read_baseline(ROOT/'index/data/fiscal-baseline.csv')
    m=json.loads((ROOT/'build/fiscal-model.json').read_text())
    with tempfile.TemporaryDirectory() as tmp:
        for name in ('ledger.json','fiscal-model.json','moving-america.json'):
            shutil.copyfile(ROOT/'build'/name,Path(tmp)/name)
        before=os.getcwd()
        try:
            os.chdir(tmp)
            with contextlib.redirect_stdout(io.StringIO()): funds=module('rb_funds',ROOT/'index/tools/funds-model.py')
        finally: os.chdir(before)
    return f,b,m,funds

def education_components(m,growth=None,consolidated=False,multiplier=1,post_growth=None):
    """Total = actual assigned current-law proxy + incremental target, not residual guess.
    Negative change relative to an old component is retained and flagged, not clipped.
    """
    g=A['current_law_growth'] if growth is None else growth
    old={r['id']:r for r in m['rows']}; rows=[]
    weights={'meals':{'EDU-3':1},'idea':{'EDU-1':.25/.33},
             'title_i':{'EDU-1':.08/.33},'care':{'FAM-2':1},'pipeline':{'EDU-4':1}}
    for y in range(2030,2057):
        for k,c in A['education_components'].items():
            pts=dict(zip(A['education_anchor_years'],c['anchors']))
            cg=A['education']['cost_growth_after2049'] if post_growth is None else post_growth
            gross=(geometric(pts,y) if y<=2049 else pts[2049]*(1+cg)**(y-2049))*multiplier
            current=c['current_law_bn']*(1+g)**(y-c['base_year'])
            legacy=sum(old[r]['gf'][str(y)]*w for r,w in weights.get(k,{}).items())
            if consolidated and k=='care':
                extra=A['childcare_current_law_2026_bn']*(1+g)**(y-2026)
                gross+=extra; current+=extra
            rows.append(dict(year=y,component=k,full_fund_outlays_bn=gross,current_law_transfer_bn=current,
                             increment_over_current_law_bn=gross-current,old_agenda_transfer_bn=legacy,
                             change_over_old_agenda_bn=gross-current-legacy,
                             lower_than_old_component=gross-current<legacy-1e-8))
    return rows

def edu_fund(components,b,f,rate=1.4,gf_share=.3,stress=False,corridor=False):
    e=A['education']; rows=[]; reserve=0
    by={y:sum(r['full_fund_outlays_bn'] for r in components if r['year']==y) for y in range(2030,2057)}
    pg=A['stress']['education_payroll_growth'] if stress else e['payroll_growth']
    cg=A['stress']['education_cost_growth'] if stress else e['cost_growth_after2049']
    for y in range(2030,2105):
        out=by[y] if y<=2056 else by[2056]*(1+cg)**(y-2056)
        shock={2036:.97,2037:.95,2038:.97,2039:.99}.get(y,1) if stress else 1
        pay=rate*phase(y,e['phase_start'],e['phase_years'])*e['payroll_per_point_2030_bn']*(1+pg)**(y-2030)*shock
        grant=max(gf_share*out,max(0,out-pay) if y<=e['bridge_last_year'] else 0)
        ir=f.marginal_rate(b,y) if y<=2056 else .04
        interest=reserve*ir
        base_grant=grant; gross_pay=pay
        if corridor and y>=2035:
            # Build a one-year reserve over 2035-39, then keep between one and two
            # years of current outlays. Extra GF support is an explicit obligation.
            floor=out*phase(y,2035,5)
            grant=max(grant,floor-reserve-interest-pay+out)
            excess=max(0,reserve+interest+pay+grant-out-2*out)
            reduction=min(grant,excess); grant-=reduction; excess-=reduction
            pay-=min(pay,excess)  # prospective contribution reduction, not free GF revenue
        reserve+=interest+pay+grant-out
        rows.append(dict(year=y,outlays=out,receipts=pay,grant=grant,base_grant=base_grant,
                         contribution_reduction=gross_pay-pay,interest=interest,reserve=reserve,ratio=reserve/out))
    return dict(rows=rows,depletion=next((r['year'] for r in rows if r['reserve'] < -1e-7),None),
                terminal_ratio=rows[-1]['ratio'],terminal_rising=rows[-1]['ratio']>=rows[-6]['ratio'])

def leave_fund(u,cap=1.1,take_up='high',admin_fraction=None):
    """Extend the existing reserve/loan convention to 2100; unchanged through 2060."""
    admin=ADOPTION['administration']; admin_fraction=admin['leave_fraction'] if admin_fraction is None else admin_fraction
    p=u.P; target=u.BILL['FAM-3']['cost_'+{'low':'lo','mid':'mid','high':'hi'}[take_up]]*1000
    ramp=[float(x) for x in p['leave_ramp'].split('/')]
    ph=lambda t: 0 if t<2031 else ramp[t-2031] if t-2031<len(ramp) else 1
    mature=target/sum(ph(y)*u.payroll(y) for y in W)
    rt=p['leave_rate']; reserve=loan=0; rows=[]
    for y in range(2030,2101):
        benefit=ph(y)*mature*u.payroll(y)
        administration=benefit*admin_fraction+(admin['leave_startup_bn'] if y==2030 and admin_fraction else 0)
        cost=benefit+administration
        if y>2030:
            if reserve-loan<p['leave_low_years']*cost and rt<cap-1e-9: rt=min(cap,round(rt+p['leave_step'],4))
            elif reserve-loan>p['leave_high_years']*cost and rt>p['leave_rate']+1e-9: rt=max(p['leave_rate'],round(rt-p['leave_step'],4))
        pay=rt/100*u.payroll(y); reserve=reserve*(1+u.rate(y))+pay-cost
        if reserve<0: loan-=reserve; reserve=0
        loan*=1+u.rate(y)
        repaid=min(loan,reserve); loan-=repaid; reserve-=repaid
        rows.append(dict(year=y,rate=rt,receipts=pay,benefits=benefit,administration=administration,reserve=reserve,loan=loan))
    return dict(rows=rows,mature_cost_points=100*mature,terminal_loan=loan,
                repayment_year=next((r['year'] for r in rows if r['year']>2040 and r['loan']<1e-8),None))

def credit(y):
    c=A['recovery_credit']
    if y<c['start']: return 0
    dollars=c['annual_per_adult_2030_dollars']*(1+c['cpi'])**(y-2030)
    adults=c['population_m_2030']*c['adult_share']*(1+c['population_growth'])**(y-2030)
    return dollars*adults/1000*(c['first_year_fraction'] if y==c['start'] else 1)

def tax_yield(b,y,high_rate,broad_rate,haircut):
    t=A['tax']
    return (1-haircut)*b[y]['gdp']/b[2034]['gdp']*(
        high_rate*t['high_threshold_per_point_2034_bn']*phase(y,t['high_start'],t['high_phase_years'])+
        broad_rate*t['broad_threshold_per_point_2034_bn']*phase(y,t['broad_start'],t['broad_phase_years']))

def capacity_accounts(y,b,u,hi_fraction=None):
    a=ADOPTION['administration']; shares=a['ssa_source_outlays_mn']; den=sum(shares.values())
    # Source proposal ramp and nominal growth, then constant payroll share after 2039.
    if y<2030: gross=0
    elif y<=2039: gross=a['ssa_recurring_2026_bn']*({2030:.5,2031:.8}.get(y,1))*1.035**(y-2026)
    else: gross=a['ssa_recurring_2026_bn']*1.035**13*u.payroll(y)/u.payroll(2039)
    if 2030<=y<=2035: gross+=a['ssa_surge_bn']/6 # authored spendout proxy
    hi=a['medicare_hi_fraction'] if hi_fraction is None else hi_fraction
    medicare=gross*shares['medicare']/den
    hlt=0 if y<2031 else a['hlt2_recurring_2026_bn']*({2031:.5,2032:.8}.get(y,1))*1.035**(min(y,2039)-2026)*(u.payroll(y)/u.payroll(2039) if y>2039 else 1)
    return dict(oasdi=gross*shares['oasdi']/den,hi=medicare*hi,smi=medicare*(1-hi)+hlt)

def build_case(name,f,b,m,u,alternative=False,stress=False,rate_shift=0,broad_rate=None,translate=True,corridor=False,legacy_education_floor=False,credit_multiple=1,high_rate=None,medicare_hi_fraction=None,spending_adjustments=None,leave_admin_fraction=None):
    e=A['education']; ss=A['social_security']; s=A['spending']; st=A['stress']
    comp=education_components(m,multiplier=st['education_cost_multiplier'] if stress else 1,
                              post_growth=st['education_cost_growth'] if stress else None)
    if legacy_education_floor:
        for r in comp:
            extra=max(0,-r['change_over_old_agenda_bn'])
            for k in ('full_fund_outlays_bn','increment_over_current_law_bn','change_over_old_agenda_bn'): r[k]+=extra
    edu=edu_fund(comp,b,f,rate=2 if alternative else 1.4,gf_share=0 if alternative else e['gf_share_mixed'],stress=stress,corridor=corridor)
    er={r['year']:r for r in edu['rows']}
    ss_paths=[u.SSF[k] for k in ('SS-1','SS-2','SS-3','SS-4','SS-5')]
    ss_paths += [lambda y:(-ss['joint_interaction_payroll_points'] if y>=2031 else 0,0),
                 lambda y:(ss['broad_rate_points']*phase(y,ss['start'],ss['phase_years']),0)]
    accounts=lambda y:capacity_accounts(y,b,u,medicare_hi_fraction)
    def fund_dollars(y,key):
        factor=b[y]['gdp']/u.gdp(y) if translate and y in b else b[2056]['gdp']/u.gdp(2056) if translate else 1
        return accounts(y)[key]/factor
    ss_paths += [lambda y:(0,100*fund_dollars(y,'oasdi')/u.payroll(y))]
    sr=u.run_ss(ss_paths)
    # Internal HI grant: improves that account, never consolidated external resources.
    his=u.HIS
    hi_fraction=(.5+.7*(st['hi_health_savings_fraction'] if stress else 1))/1.2
    hp=A['hi']; grant_rate=lambda y:hp['gf_support_payroll_points']*phase(y,hp['start'],hp['phase_years'])
    u.HIS=lambda y:his(y)*hi_fraction+grant_rate(y)
    try: hr=u.run_hi(True,administration=lambda y:100*fund_dollars(y,'hi')/u.hi_payroll(y))
    finally: u.HIS=his
    hi_ratios=[r['reserve']/(r['cost']/100*u.hi_payroll(r['year'])) for r in hr['rows']]
    hr['terminal_rising']=hi_ratios[-1]>=hi_ratios[-6]; hr['terminal_ratio']=hi_ratios[-1]
    lr=leave_fund(u,A['leave']['cap_points'],A['leave']['take_up'],admin_fraction=leave_admin_fraction); leave={r['year']:r for r in lr['rows']}
    old={r['id']:r for r in m['rows']}; base=m['results']['BASE-R1' if rate_shift else 'BASE']['years']
    ledger=json.loads((ROOT/'build/ledger.json').read_text())
    rev={r['id']:r for r in ledger['revenue']}
    # Show gross matched receipts and uses already netted in GF lines. Transport uses the
    # recorded NET new-receipt estimate, not the entire existing HTF budget. Cash profile
    # is an authored proxy; it cannot verify actual highway baseline or outlay timing.
    matched_ids=['C1','C2','C3','PS1','MF1','IF1','MR1','MR2','MR3','MR4','MR5','MR6']
    matched={k:f.row_path(b,rev[k]['mid'],dict(ramp=1,grow='gdp')) for k in matched_ids}
    # Carbon uses its recorded declining fee profile rather than a GDP perpetuity.
    carbon={r['year']:r for r in u.carbon}
    for y in W:
        matched['C1'][y]=carbon[y]['c1']; matched['C2'][y]=carbon[y]['c2']
    for y in range(2040,2057):
        for k in ['C1','C2']:
            matched[k][y]=matched[k][2039]*b[y]['gdp']/b[2039]['gdp']*.98**(y-2039)
    losses={y:0 for y in Y}
    if stress:
        for rid,amt in st['receipt_losses_tn'].items():
            prof=f.PR.BILLS[rid] if rid in f.PR.BILLS else f.PR.REVENUE[rid] if rid in f.PR.REVENUE else f.PR.CUTS[rid]
            p=f.row_path(b,amt,prof,rid)
            for y in Y: losses[y]+=p[y]
        for y in range(2040,2057): losses[y]+=-old['G11']['gf'][str(y)]*st['g11_post2039_loss_fraction']
    extras={k:f.row_path(b,s[k+'_tn'],dict(ramp=4,grow='gdp')) for k in ('housing_extra','participation','delivery_contingency')}
    housing_admin=f.row_path(b,s['housing_base_admin_tn'],dict(ramp=4,grow='cpi',perm=1))
    development=f.row_path(b,s['development_program_tn'],dict(ramp=3,grow='cpi',perm=1))
    irs_risk=f.row_path(b,s['irs_receipt_risk_tn'],f.PR.REVENUE['G8'],'G8')
    # Reductions are explicit smaller authorizations, not unspent holdbacks or efficiency claims.
    savings={y:sum(old[k]['gf'][str(y)]*(1-s[key]/amt) for k,key,amt in
                [('CAP-7S','cap_surge_tn',.6),('CAP-7','cap_sustained_tn',.49),('AI-4','ai_transition_tn',.2)]) for y in Y}
    adjustments={}
    for label,spec in (spending_adjustments or {}).items():
        adjustments[label]=f.row_path(b,spec['delta_tn'],spec['profile'])
    rows=[]; audit=[]
    broad=A['tax']['broad_rate_points'] if broad_rate is None else broad_rate
    for y in Y:
        key=str(y); baseline=base[key]; dr=do=0
        def entry(label,revenue=0,outlay=0):
            nonlocal dr,do
            dr+=revenue; do+=outlay
            if abs(revenue)+abs(outlay)>1e-10: audit.append(dict(year=y,line=label,revenue_change_bn=revenue,primary_outlay_change_bn=outlay,primary_deficit_change_bn=outlay-revenue))
        # Legacy net rows: explicitly un-net revenue by account classification.
        for r in m['rows']:
            if r['id']=='SS-1': continue
            v=r['uni'][key]
            entry(r['id'],revenue=-v if r['cat'].startswith('rev_') else 0,outlay=v if not r['cat'].startswith('rev_') else 0)
        for k in f.DEC:
            if k in ('C19b','C20'):
                if not alternative: continue
                v=m['opt_rows'][k]['uni'][key]*phase(y,2033,3)
            else: v=m['opt_rows'][k]['uni'][key]
            r=m['opt_rows'][k]
            entry(k,revenue=-v if r['cat'].startswith('rev_') else 0,outlay=v if not r['cat'].startswith('rev_') else 0)
        grossup=sum(p[y] for p in matched.values())
        entry('Matched dedicated uses (gross presentation proxy)',revenue=grossup,outlay=grossup)
        ec=[r for r in comp if r['year']==y]
        current=sum(r['current_law_transfer_bn'] for r in ec); legacy=sum(r['old_agenda_transfer_bn'] for r in ec)
        ed=er.get(y,dict(outlays=0,receipts=0,grant=0))
        entry('EDU replacement, net of existing-law and old agenda',revenue=ed['receipts']*(1-e['tax_offset_fraction']),outlay=ed['outlays']-current-legacy)
        factor=b[y]['gdp']/u.gdp(y) if translate else 1
        si=sum(p(y)[0] for p in ss_paths)/100*u.payroll(y)*factor
        so=sum(p(y)[1] for p in ss_paths)/100*u.payroll(y)*factor
        # Deductibility/wage feedback allowance applies to new covered earnings/payroll only;
        # SSA NII/pass-through bases already contain responses; no second blanket haircut.
        wage_ss=max(0,u.SSF['SS-1'](y)[0]+ss['broad_rate_points']*phase(y,ss['start'],ss['phase_years']))/100*u.payroll(y)*factor
        ss_offset=wage_ss*ss['income_tax_offset_fraction']
        entry('SS actual 2031 start, high-base package and later rate',revenue=si-ss_offset,outlay=so)
        hi_amount=his(y)/100*u.hi_payroll(y)*factor
        hi_tax=hi_amount*.5/1.2
        hi_saving=hi_amount*.7/1.2*(st['hi_health_savings_fraction'] if stress else 1)
        hi_grant=grant_rate(y)/100*u.hi_payroll(y)*factor
        entry('HI H1a and Part A HLT-6 share',revenue=hi_tax,outlay=-hi_saving)
        lv=leave.get(y,dict(receipts=0,benefits=0,administration=0,loan=0))
        leave_offset=lv['receipts']*factor*A['leave']['income_tax_offset_fraction']
        entry('Paid leave actual contributions and benefits',revenue=lv['receipts']*factor-leave_offset,outlay=(lv['benefits']+lv['administration'])*factor)
        entry('Recovery credit',outlay=credit(y)*credit_multiple)
        entry('Smaller capacity and AI authorizations',outlay=-savings[y])
        ac=accounts(y); smi_premium=ac['smi']*ADOPTION['administration']['smi_premium_fraction']
        for label,path in adjustments.items(): entry('Exploratory: '+label,outlay=path[y])
        entry('DEV-P permanent development programs',outlay=development[y])
        # OASDI cost is in so and formerly inside capacity: remove once.
        entry('SSA OASDI capacity reclassification',outlay=-ac['oasdi'])
        entry('SMI administration premiums',revenue=smi_premium)
        entry('HOU-4A PHA administration correction',outlay=housing_admin[y])
        entry('IRS yield allowance with smaller capacity budget',revenue=-irs_risk[y])
        # Advance part of the remaining surge, conserving lifetime cash.
        early=s['early_admin_bn'] if y==2029 else -s['early_admin_bn'] if y==2030 else 0
        entry('2029 delivery advance from 2030 surge',outlay=early)
        for k,p in extras.items(): entry(k,outlay=p[y])
        high=0 if alternative else A['tax']['high_rate_points'] if high_rate is None else high_rate
        taxes=tax_yield(b,y,high,broad,st['new_tax_yield_haircut'] if stress else A['tax']['additional_yield_haircut'])
        entry('New indexed income contributions',revenue=taxes)
        # Mixed receipt/cost downside is recorded as a separately labeled NET reserve;
        # not claimed as independently classified official tax/outlay categories.
        entry('Downside net loss allowance',outlay=losses[y])
        primary=do-dr
        # Recover GF from consolidated delta by stripping fund primary balances.
        fund_primary=(ed['outlays']-ed['receipts']-ed['grant'])+(so-si)+(-hi_tax-hi_saving-hi_grant)+(lv['benefits']+lv['administration']-lv['receipts'])*factor+ac['hi']
        gf=primary-fund_primary
        rows.append(dict(year=y,gdp_bn=b[y]['gdp'],baseline_revenue_bn=baseline['rev'],
                         baseline_primary_outlays_bn=baseline['out']-baseline['interest'],
                         revenue_change_bn=dr,primary_outlay_change_bn=do,program_primary_bn=primary,
                         agenda_gf_primary_bn=gf,education_gf_grant_bn=ed['grant'],education_current_law_transfer_bn=current,
                         education_old_agenda_transfer_bn=legacy,hi_gf_grant_bn=hi_grant,
                         ssa_oasdi_admin_bn=ac['oasdi'],ssa_hi_admin_bn=ac['hi'],smi_admin_bn=ac['smi'],smi_admin_premiums_bn=smi_premium,leave_admin_bn=lv['administration']*factor,development_program_bn=development[y],ss_income_tax_offset_bn=ss_offset,leave_income_tax_offset_bn=leave_offset,
                         new_income_tax_bn=taxes,recovery_credit_bn=credit(y)*credit_multiple,matched_grossup_bn=grossup,
                         macro_translation=factor,baseline_debt_bn=baseline['debt'],baseline_interest_bn=baseline['interest']))
    interest,debt=f.debt_roll(b,{r['year']:r['program_primary_bn'] for r in rows},shift=rate_shift)
    for r in rows:
        y=r['year']; r['revenue_bn']=r['baseline_revenue_bn']+r['revenue_change_bn']
        r['primary_outlays_bn']=r['baseline_primary_outlays_bn']+r['primary_outlay_change_bn']
        r['interest_bn']=r['baseline_interest_bn']+interest[y]; r['outlays_bn']=r['primary_outlays_bn']+r['interest_bn']
        r['deficit_bn']=r['outlays_bn']-r['revenue_bn']; r['debt_bn']=r['baseline_debt_bn']+debt[y]
        for k in ('revenue','outlays','deficit','debt','interest'): r[k+'_gdp']=100*r[k+'_bn']/r['gdp_bn']
    by={r['year']:r for r in rows}
    def total(k):return sum(by[y][k] for y in W)/1000
    summary=dict(name=name,broad_income_rate_points=broad,high_income_rate_points=high,credit_multiple=credit_multiple,debt_gdp_2039=by[2039]['debt_gdp'],debt_gdp_2056=by[2056]['debt_gdp'],
        debt_ratio_nonincreasing_2045_56=all(by[y]['debt_gdp']<=by[y-1]['debt_gdp']+1e-8 for y in range(2045,2057)),
        deficit_gdp_2056=by[2056]['deficit_gdp'],credit_tn=total('recovery_credit_bn'),
        primary_change_2030_39_tn=total('program_primary_bn'),education_grants_tn=total('education_gf_grant_bn'),
        hi_grants_tn=total('hi_gf_grant_bn'),new_income_tax_tn=total('new_income_tax_bn'),
        max_mature_agenda_gf_gap_gdp=max(100*by[y]['agenda_gf_primary_bn']/b[y]['gdp'] for y in range(2040,2057)),
        ss_sustainable=sr['sustainable'],ss_depletion=sr['depletion'],ss_actuarial_balance=sr['balance'],
        hi_depletion=hr['depletion'],hi_terminal_rising=hr['terminal_rising'],hi_terminal_ratio=hr['terminal_ratio'],
        education_depletion=edu['depletion'],education_terminal_rising=edu['terminal_rising'],education_terminal_ratio=edu['terminal_ratio'],
        leave_terminal_loan_bn=lr['terminal_loan'],leave_repayment_year=lr['repayment_year'])
    return dict(summary=summary,rows=rows,audit=audit,education=edu,ss=sr,hi=hr,leave=lr)

def household_diagnostic(d,f,b,m,u):
    """Reconcile changed household rows; estimates of incidence, not microsimulation.
    Does not value unspecified delivery/admin money as household cash or certify D3.
    """
    before=os.getcwd()
    try:
        os.chdir(ROOT/'build'); inc=module('incidence',ROOT/'build/incidence.py')
        years=module('rb_incidence_years',ROOT/'build/years.py')
    finally: os.chdir(before)
    output={}; keys={k:inc.K[k][0] for k in inc.K}
    # Broad-income allocation is a stated author assumption, not IRS microdata.
    keys['broad_income']=[1,5,12,24,58]
    for case in ['mixed','larger_payroll','mixed_larger_credit']:
        c=d['cases'][case]; annual={r['year']:r for r in c['rows']}
        edu={r['year']:r for r in c['education']['rows']}; lv={r['year']:r for r in c['leave']['rows']}
        result={y:{g:0.0 for g in inc.GROUPS} for y in W}
        def add(y,amount_bn,key):
            for i,g in enumerate(inc.GROUPS):result[y][g]+=amount_bn*keys[key][i]/100*1e9/(inc.HH*.2)
        # Retain untouched instruments on their existing incidence phasing. Flag this
        # timing approximation instead of claiming full fiscal/incidence harmonization.
        removed={'O1','O2','P1','F2','F3','EDU3','EDU4','F5','E12'}
        rows=list(inc.ROWS)+[(k,v[3],v[0],v[1],v[2],'') for k,v in inc.OPTIONS.items() if k in inc.QO]
        for rid,label,side,amount,parts,_ in rows:
            if rid in removed or rid in ('C19b','C20') and case!='larger_payroll':continue
            for y in W:
                ratio=(.32/.65 if rid=='EDU' else 1)*(phase(y,2033,3) if rid in ('C19b','C20') else 1)
                for key,v in parts:add(y,(1 if side=='benefit' else -1)*v*1000*years.P.get(rid,years.P['flat'])[y-2030]*ratio,key)
        for y in W:
            a=annual[y]; scale=a['macro_translation']; ed=edu[y]
            for r in d['education_components']:
                if r['year']==y:add(y,r['increment_over_current_law_bn'], 'childcare' if r['component']=='care' else 'meals' if r['component']=='meals' else 'education')
            add(y,-a['smi_admin_premiums_bn'],'medicare'); add(y,-ed['receipts'],'wages'); add(y,a['recovery_credit_bn'],'adults')
            for k,key in [('SS-1','above250k_wages'),('SS-2','inv400k'),('SS-5','surtax')]:
                add(y,-u.SSF[k](y)[0]/100*u.payroll(y)*scale,key)
            add(y,A['social_security']['joint_interaction_payroll_points']/100*u.payroll(y)*scale if y>=2031 else 0,'inv400k')
            add(y,-A['social_security']['broad_rate_points']*phase(y,2035,10)/100*u.payroll(y)*scale,'wages_cap')
            benefits=sum(u.SSF[k](y)[1] for k in ('SS-1','SS-2','SS-3','SS-4','SS-5'))/100*u.payroll(y)*scale
            add(y,benefits,'ss_benefit'); add(y,lv[y]['benefits']*scale,'leave_benefit'); add(y,-lv[y]['receipts']*scale,'wages_cap')
            high=tax_yield(b,y,c['summary']['high_income_rate_points'],0,A['tax']['additional_yield_haircut'])
            broad=a['new_income_tax_bn']-high
            add(y,-high,'surtax'); add(y,-broad,'broad_income')
            # Same fiscal profiles as modeled new offers; AI cut reduces actual benefits.
            for k,key in [('housing_extra','housing'),('participation','workers_ai')]:
                add(y,f.row_path(b,A['spending'][k+'_tn'],dict(ramp=4,grow='gdp'))[y],key)
            add(y,f.row_path(b,A['spending']['ai_transition_tn'],f.PR.BILLS['AI-4'],'AI-4')[y],'workers_ai')
        output[case]={y:{g:round(v) for g,v in r.items()} for y,r in result.items()}
    return dict(per_household_annual_dollars=output,
                limitations='Inherited distribution keys and unchanged-row timing; no microdata, no within-quintile guarantee; tax offsets and delivery contingency not distributed. Broad-income shares authored 1/5/12/24/58%; SS5 uses surtax proxy. Existing health savings/wage pass-through remain assumptions. D3 not certified.')

def run():
    f,b,m,u=load()
    components=education_components(m)
    cases={}
    for name,opts in [('mixed',{}),('larger_payroll',{'alternative':True}),
                      ('mixed_downside',{'stress':True}),('mixed_all_debt_rate_plus1',{'rate_shift':1}),
                      ('mixed_no_macro_translation',{'translate':False}),
                      ('mixed_leave_admin_high',{'leave_admin_fraction':.06}),
                      ('mixed_ssa_medicare_all_hi',{'medicare_hi_fraction':1}),
                      ('mixed_ssa_medicare_all_smi',{'medicare_hi_fraction':0}),
                      ('mixed_reserve_corridor',{'corridor':True}),
                      ('mixed_corridor_downside',{'corridor':True,'stress':True}),
                      ('mixed_legacy_education_floor',{'legacy_education_floor':True}),
                      ('mixed_larger_credit',{'credit_multiple':5,'high_rate':10})]:
        cases[name]=build_case(name,f,b,m,u,**opts)
    # Marginal broad-rate solution is a diagnostic, not an automatic policy adoption.
    # One additional point is linear in primary flows and debt in this static model.
    solutions={}
    for name,opts in [('mixed',{}),('larger_payroll',{'alternative':True}),('mixed_downside',{'stress':True}),('mixed_all_debt_rate_plus1',{'rate_shift':1})]:
        c=cases[name]; plus=build_case(name,f,b,m,u,broad_rate=A['tax']['broad_rate_points']+1,**opts)
        x={r['year']:r for r in c['rows']}; z={r['year']:r for r in plus['rows']}
        required=max((x[y]['debt_gdp']-x[y-1]['debt_gdp'])/((x[y]['debt_gdp']-x[y-1]['debt_gdp'])-(z[y]['debt_gdp']-z[y-1]['debt_gdp'])) for y in range(2045,2057))
        solutions[name]=max(0,A['tax']['broad_rate_points']+required)
    inputs=['index/data/fiscal-baseline.csv','index/data/inputs/education-adoption.json',
            'index/data/inputs/recovery-adoption.json',
            'index/tools/recovery-budget/assumptions.json','build/fiscal-model.json','build/ledger.json',
            'index/tools/fiscal-profiles.py','index/tools/funds-model.py',
            'sources/education-transforming-education-act-analysis-and-trust-fund.md']
    inputs+=sorted(str(p.relative_to(ROOT)) for p in (ROOT/'index/data/inputs').glob('funds-*.csv'))
    result=dict(status=A['status'],adoption=ADOPTION,source_commit=A['source_commit'],units='nominal $B; window totals $T; federal fiscal years',
                source_sha256={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in inputs},
                education_components=components,consolidated_childcare=education_components(m,consolidated=True),
                current_law_growth_sensitivity={str(g):education_components(m,growth=g) for g in (.02,.04)},
                cases=cases,required_broad_rate_points=solutions,
                baseline={y:m['results']['BASE']['years'][str(y)] for y in Y})
    result['household_diagnostic']=household_diagnostic(result,f,b,m,u)
    return result

def markdown(d):
    out=['# Recovery and Solvency budget: exploratory results','',
         '> **Approval implemented:** Espen selected the recommended architecture and working spending changes; [adopted inputs](data/inputs/recovery-adoption.json) feed this model. The preferred architecture is the mixed reserve-corridor case. Its illustrative tax rates, credit and grant parameters remain unselected, and no complete financing schedule is adopted. Read [the assessment](../sources/recovery-and-solvency-budget.md) and [method/source notes](tools/recovery-budget/README.md). Nominal dollars; FY2030–39 window. Existing federal revenue/spending/debt are included; gross-flow, state/local and annual account reconciliation remain incomplete. No D3/D4 or all-fund solvency certification.','',
         '| Case | Debt/GDP 2039 | Debt/GDP 2056 | Deficit/GDP 2056 | Stable debt ratio 2045–56? | Broad-income rate needed, total points |',
         '| --- | ---: | ---: | ---: | --- | ---: |']
    for k,c in d['cases'].items():
        s=c['summary']; need=d['required_broad_rate_points'].get(k)
        out.append(f"| {k} | {s['debt_gdp_2039']:.1f}% | {s['debt_gdp_2056']:.1f}% | {s['deficit_gdp_2056']:.2f}% | {s['debt_ratio_nonincreasing_2045_56']} | {need:.2f} |" if need is not None else f"| {k} | {s['debt_gdp_2039']:.1f}% | {s['debt_gdp_2056']:.1f}% | {s['deficit_gdp_2056']:.2f}% | {s['debt_ratio_nonincreasing_2045_56']} | — |")
    out+=['','The last column is the total broad-tier rate required under this static tax-yield proxy, replacing the proposed two-point broad tier, with the high tier unchanged. It is not a tax score.','',
          '| Education component | Full fund $T | Current law moved $T | Increment vs current law $T | Old agenda moved $T | Change vs old agenda $T |',
          '| --- | ---: | ---: | ---: | ---: | ---: |']
    for k in list(A['education_components'])+['TOTAL']:
        rr=[r for r in d['education_components'] if r['year'] in W and (k=='TOTAL' or r['component']==k)]
        vals=[sum(r[v] for r in rr)/1000 for v in ['full_fund_outlays_bn','current_law_transfer_bn','increment_over_current_law_bn','old_agenda_transfer_bn','change_over_old_agenda_bn']]
        out.append('| '+k+' | '+' | '.join(f'{v:.3f}' for v in vals)+' |')
    out+=['','| Fixed-grant comparison, FY | Current-law revenue | Current-law primary spending | Total revenue | Total spending | Net interest | Deficit | Debt/GDP |',
          '| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |']
    for r in d['cases']['mixed']['rows']:
        if r['year'] in [2029,2030,2035,2039,2045,2056]:
            out.append(f"| {r['year']} | {r['baseline_revenue_bn']:.0f} | {r['baseline_primary_outlays_bn']:.0f} | {r['revenue_bn']:.0f} | {r['outlays_bn']:.0f} | {r['interest_bn']:.0f} | {r['deficit_bn']:.0f} | {r['debt_gdp']:.1f}% |")
    out+=['','Totals above are $B, not $T. The audit CSV exposes every increment and matched gross-up. Internal fund grants do not appear as new external resources.','',
          '| Household diagnostic, FY2039 annual net $/household | Q1 | Q2 | Q3 | Q4 | Q5 |',
          '| --- | ---: | ---: | ---: | ---: | ---: |']
    for k,years in d['household_diagnostic']['per_household_annual_dollars'].items():
        out.append('| '+k+' | '+' | '.join(f'{v:,}' for v in years[2039].values())+' |')
    out+=['','These are approximate quintile averages including modeled benefits, not a D3 certification or guarantees for individual households. See the assumptions and limits in the assessment.','',
          '| Fund, mixed case | Result |','| --- | --- |']
    s=d['cases']['mixed']['summary']
    out += [f"| Education | Depletion: {s['education_depletion']}; terminal reserve/outlays {s['education_terminal_ratio']:.2f}; rising: {s['education_terminal_rising']} |",
            f"| Combined OASDI | Depletion: {s['ss_depletion']}; conservative model solvency: {s['ss_sustainable']}; actuarial balance {s['ss_actuarial_balance']:+.2f}% payroll |",
            f"| HI | Depletion: {s['hi_depletion']}; terminal reserve/cost {s['hi_terminal_ratio']:.2f}; rising: {s['hi_terminal_rising']} |",
            f"| Leave, high take-up | Loan repaid {s['leave_repayment_year']}; terminal loan ${s['leave_terminal_loan_bn']:.1f}B |",'',
            'OASI/DI legal separation, the HI annual-data calibration, HTF beyond 2046, and long-run category/cash mappings remain unresolved. A positive balance in one fund cannot fund a second account without legislation.','']
    return '\n'.join(out)

def write_csv(path,rows):
    with path.open('w',newline='') as fh:
        w=csv.DictWriter(fh,fieldnames=list(rows[0]),lineterminator='\n'); w.writeheader(); w.writerows(rows)

if __name__=='__main__':
    p=argparse.ArgumentParser(); p.add_argument('--output-dir',type=Path); args=p.parse_args()
    d=run(); dest=args.output_dir or ROOT/'build/recovery-budget'; dest.mkdir(parents=True,exist_ok=True)
    export=dict(d,cases={k:{n:v for n,v in c.items() if n!='audit'} for k,c in d['cases'].items()},
                audit_file='sources/recovery-budget-audit.csv')
    (dest/'recovery-budget.json').write_text(json.dumps(export,indent=2)+'\n')
    (dest/'recovery-budget.md').write_text(markdown(d))
    write_csv(dest/'education-component-reconciliation.csv',d['education_components'])
    write_csv(dest/'recovery-budget-paths.csv',[dict(case=k,**r) for k,c in d['cases'].items() for r in c['rows']])
    write_csv(dest/'recovery-budget-audit.csv',[dict(case=k,**r) for k,c in d['cases'].items() for r in c['audit']])
    for k,c in d['cases'].items(): print(k,json.dumps(c['summary']))
    print('Required broad rates:',d['required_broad_rate_points'])
