import merge_decisions as D, transit_fiscal_model as M
B="B: conditional tier"
FUEL_SHARE=0.85; GAS_W=0.65   # (A) fuel taxes ~85% of legacy receipts; gasoline ~65% of fuel receipts
def fuel_factor(t):
    inc=0 if t<2029 else 5*min(t-2028,3)          # +5 cents a year FY2029-31
    g=(18.4+inc)/18.4; d=(24.4+inc)/24.4
    f=GAS_W*g+(1-GAS_W)*d
    return f*(1.025**max(t-2031,0))               # CPI-indexed from FY2032
def clean_rate(t): return 0 if t<2029 else 1.5*1.03**(t-2029)   # cents/mi, NHCCI+0.5% ~3%
def clean_stock(t):  # millions plug-ins, model's path
    pts=[(2029,9),(2035,25),(2040,45),(2045,70),(2052,90)]
    for (a,va),(b,vb) in zip(pts,pts[1:]):
        if a<=t<=b: return va+(vb-va)*(t-a)/(b-a)
def clean_vmt_rev(t): return 0 if t<2029 else clean_stock(t)*11000*0.9*clean_rate(t)/100/1000*0.9  # $B, 10% admin
def fund_new(t):
    if t<2029: return M.legacy(t)
    leg=M.legacy(t); fuel=leg*FUEL_SHARE*fuel_factor(t); other=leg*(1-FUEL_SHARE)*M.infl(t,2028)
    return fuel+other+clean_vmt_rev(t)
old=M.fund_revenue
base={t:old(t) for t in range(2029,2047)}
M.fund_revenue=fund_new
print("FY   fund_old fund_new  cleanVMT  draw")
for t in (2029,2031,2032,2034,2036,2041,2046):
    a=M.allocate(t,"C",B); print(t, round(base[t],1), round(fund_new(t),1), round(clean_vmt_rev(t),1), f"{a['gf_pct']:.3%}")
for r in M.period_rows("C",B)[1:]:
    print(r['period'], f"avg {r['gf_pct_avg']:.3%} peak {r['gf_pct_peak']:.3%} ({r['peak_year']})", "ded",{k:round(v,1) for k,v in r['ded'].items()}, "cov", {k:f"{r['ded'][k]/r['prog'][k]:.0%}" for k in r['ded']})
print("FY2032-36 fund", round(sum(fund_new(t) for t in range(2032,2037)),1), "vs", round(sum(base[t] for t in range(2032,2037)),1))
