"""Carbon model for Project 2050's D7 design: emissions, REV-C1 and REV-C2 receipts, the dividend, and the companion measures.

Runs the structural carbon-fee model in models/tools/carbon/ (Espen's Carbon Dividend Model, v3.4, built in an earlier
project; see legacy/sources/climate-carbon-dividend-model-notes.md) on Project 2050's decided design rather than the design
that model was built for: REV-C1 at $25 a ton in 2030, D7's steps to 2032, then rising to $150 by 2037 (Oct 26), then 5% a year; gasoline and diesel
outside the fee and priced only by Moving America's fuel-tax steps; CO2 from fuel combustion only (methane fees and the
border adjustment are separate lines); 80% returned equally per adult (CLI-2A). Inputs: models/data/inputs/carbon-parameters.csv, the
transportation model and ledger.json. Writes carbon.json and climate-carbon-model.md. Needs node.
"""
import json, os, subprocess, sys
from inputs import read, num

HERE = os.path.dirname(os.path.abspath(__file__))
def find(*parts):
    for d in (os.path.join(HERE, *parts), os.path.join(HERE, "..", "models", "tools", *parts)):
        if os.path.exists(d): return os.path.normpath(d)
    raise FileNotFoundError(os.path.join(*parts))
CARBON = find("carbon")
sys.path.insert(0, find("transportation"))
import moving_america as ma

def _val(s):
    try: return num(s)
    except ValueError: return s.strip()
P = {r["key"]: _val(r["value"]) for r in read("carbon-parameters.csv")}
L = json.load(open("ledger.json"))
REV = {r["id"]: r for r in L["revenue"]}
BILL = {b["id"]: b for b in L["bills"]}
YRS = range(2025, 2051)
W = range(2030, 2040)
defl = lambda y: (1 + P["inflation"]) ** (y - 2025)

def d7_nominal(y):
    # D7 path: equal steps from the start price toward c1_slope_2037 until the kink year, then equal steps to c1_price_2037
    # (Oct 26: the original $25-to-$100 steps through 2032, then $150 by 2037), then c1_growth_after a year
    s, p0, p37 = P["c1_start_year"], P["c1_start_price"], P["c1_price_2037"]
    slope37, k = P.get("c1_slope_2037", p37), int(P.get("c1_kink_year", 2037))
    if y < s: return 0.0
    early = lambda yy: p0 + (slope37 - p0) * (yy - s) / (2037 - s)
    if y <= k: return early(y)
    if y <= 2037: return early(k) + (p37 - early(k)) * (y - k) / (2037 - k)
    return p37 * (1 + P["c1_growth_after"]) ** (y - 2037)
D7_REAL = {y: d7_nominal(y) / defl(y) for y in YRS}

# Moving America's fuel-tax steps as a road-fuel price, $ a ton of CO2 in 2025 dollars (gasoline: 0.0085 $/gal per $/t, as in the carbon model)
MOV = ma.Revenue(ma.Design(), premium=True)
ROAD_REAL = {y: max(MOV.gr(y) - 18.4, 0) / 100 / defl(y) / 0.0085 if y >= 2029 else 0.0 for y in YRS}

base_pol = {"permitYear": P["permit_year"], "startPrice": 0, "step": 0, "ratchet": False}
d7_pol = dict(base_pol, childShare=0, roadExempt=True, roadPath=ROAD_REAL, othRoad=P["oth_road"], offset=0, admin=0, dividendShare=P["dividend_share"],
              cover={"process": False, "methane": False, "fgas": False, "border": False, "bunkers": False}, ratchet=False)
ces = {"start": P["ces_start"], "target": P["ces_target"], "year": P["ces_year"]}
def ch4_nominal(y):  # $ a ton of methane
    if y < P["ch4_start"]: return 0.0
    return P["ch4_rate_2030"] if y == 2030 else P["ch4_rate_2031"] if y == 2031 else P["ch4_rate_2032"]
CH4_REAL = {y: ch4_nominal(y) / P["gwp100"] / defl(y) for y in YRS}   # $ a ton of CO2e, 2025 dollars
MF = {"start": P["ch4_start"], "mult": 0, "path": CH4_REAL, "ogShare": P["ch4_og_share"], "coal": bool(P["ch4_coal"]), "landfill": bool(P["ch4_landfill"]),
      "cert": {"s0": P["cert_s0"], "s1": P["cert_s1"], "year": P["cert_year"], "abate": P["cert_abate"]}}
full = dict(d7_pol, credits=True, ces=ces, standards=True, gridStatute=True, weatherize=True, methaneFee=MF)
CASES = [
    dict(id="cl", label="Current law (with the stipulated 2026-28 permitting deal)", policy=base_pol, price=None),
    dict(id="mov", label="+ Moving America's fuel-tax steps (no carbon fee)", policy=dict(base_pol, roadExempt=True, roadPath=ROAD_REAL), price=None),
    dict(id="d7", label="+ REV-C1 on D7's path, road fuels exempt (the fee alone)", policy=d7_pol, price=D7_REAL, mc=True),
    dict(id="d7cr", label="+ CLI-1 restored clean-energy credits", policy=dict(d7_pol, credits=True), price=D7_REAL),
    dict(id="d7ces", label="+ CLI-3 Clean Energy Standard (80% by 2035)", policy=dict(d7_pol, credits=True, ces=ces), price=D7_REAL),
    dict(id="d7st", label="+ CLI-4 vehicle and power standards", policy=dict(d7_pol, credits=True, ces=ces, standards=True), price=D7_REAL),
    dict(id="nomf", label="+ CLI-5 Weatherization heat pumps and CLI-6 grid statute", policy=dict(full, methaneFee=None), price=D7_REAL),
    dict(id="full", label="+ REV-C3 methane fee (the IRA charge reinstated, $1,200 a ton of methane in 2030 to $1,500 from 2032, with a certified leak-prevention exemption): **the decided package**", policy=full, price=D7_REAL, mc=True, households=2035, householdsBase="mov"),
    dict(id="opt_grid", label="Option: + a funded federal grid build-out (CLI-10's public builder, as the model's grid program)", policy=dict(full, grid=True), price=D7_REAL),
    dict(id="opt_nuc", label="Option: + an advanced nuclear program (CLI-9's reactor fleet order, as the model's nuclear program)", policy=dict(full, nuclear=True), price=D7_REAL),
    dict(id="border", label="Package with the border adjustment switched on (sizes REV-C2)", policy=dict(full, cover=dict(d7_pol["cover"], border=True)), price=D7_REAL),
    dict(id="ch4nocert", label="Package with the methane fee on every covered facility (no certification exemption)", policy=dict(full, methaneFee=dict(MF, cert=None)), price=D7_REAL),
    dict(id="ch4ira", label="Package with the methane fee on the IRA's own base (intensity thresholds and exemptions kept)", policy=dict(full, methaneFee=dict(MF, ogShare=P["ch4_og_share_ira"])), price=D7_REAL),
    dict(id="ch4x3", label="Package with the methane fee at three times the carbon fee per ton CO2e (methane's 20-year warming potential), an option", policy=dict(full, methaneFee={"start": P["ch4_start"], "mult": 3, "floor": 0, "ogShare": P["ch4_og_share"], "coal": True, "landfill": False}), price=D7_REAL),
    dict(id="ch4lf", label="Package with landfills added to the methane fee", policy=dict(full, methaneFee=dict(MF, landfill=True)), price=D7_REAL),
    dict(id="proc", label="Package with the carbon fee extended to industrial process CO2 and N2O (an option)", policy=dict(full, cover=dict(d7_pol["cover"], process=True)), price=D7_REAL),
    dict(id="econ", label="Package with road fuels priced at the fee too (REV-C1D-style convergence from 2030)", policy=dict(full, roadExempt=False), price=D7_REAL),
    dict(id="noces", label="Package without the CES (to show what CLI-3 does on top of the rest)", policy=dict(full, ces=None), price=D7_REAL),
    dict(id="nofee", label="Package with the fee repealed from 2033 (the durability test: credits, CES and standards carry on)", policy=dict(full), price={y: (D7_REAL[y] if y < 2033 else 0.0) for y in YRS}),
    dict(id="orig", label="The model's own design ($40 a ton in 2030 + $8 a year real, ratchet, wider coverage, 90% dividend; no companion measures)", policy={"permitYear": P["permit_year"]}, price=None),
]
cfg = dict(cases=CASES, mcDraws=P["mc_draws"], mcSeed=P["mc_seed"], world={"cesAcp": P["ces_acp"], "gsTx": P["grid_statute_tx"], "wxHomes": P["weatherize_homes_m"]})
json.dump(cfg, open("carbon-config.json", "w"))
R = json.loads(subprocess.run(["node", os.path.join(CARBON, "p2050-run.js"), "carbon-config.json"], check=True, capture_output=True, text=True).stdout)
C = {k: {r["year"]: r for r in v} for k, v in R["cases"].items()}

def nom_sum(case, f, yrs=W): return sum(f(C[case][y]) * defl(y) for y in yrs) / 1000   # $T nominal
def pct(x): return f"{100*x:.0f}%"
def pctile(xs, q):
    xs = sorted(xs); i = (len(xs) - 1) * q; lo = int(i); return xs[lo] + (xs[min(lo + 1, len(xs) - 1)] - xs[lo]) * (i - lo)
E2005, NET2005 = 5999, 6536

PK = "full"
c1 = lambda r: r["gross"] - r["rev"]["methane"]
c1_w = nom_sum(PK, c1)
c1_fee_alone = nom_sum("d7", c1)
c1_rows = {y: c1(C[PK][y]) * defl(y) for y in range(2030, 2051)}
c3_w = nom_sum(PK, lambda r: r["rev"]["methane"])
c3_nocert = nom_sum("ch4nocert", lambda r: r["rev"]["methane"]); c3_ira = nom_sum("ch4ira", lambda r: r["rev"]["methane"]); c3_x3 = nom_sum("ch4x3", lambda r: r["rev"]["methane"]); c3_lf = nom_sum("ch4lf", lambda r: r["rev"]["methane"])
proc_w = nom_sum("proc", lambda r: r["rev"]["process"])
c2_w = nom_sum("border", lambda r: r["rev"]["border"])
econ_extra = nom_sum("econ", c1) - c1_w
cred_w = nom_sum(PK, lambda r: r["credits"])
acp_w = nom_sum(PK, lambda r: r["cesAcp"])
mc = R["mc"]
def band(case, y, f):
    xs = [f({r["year"]: r for r in run}[y]) for run in mc[case]]
    return pctile(xs, 0.1), pctile(xs, 0.9)
c1_mc = [sum((r["gross"] - r["rev"]["methane"]) * defl(r["year"]) for r in run if r["year"] in W) / 1000 for run in mc[PK]]
c3_mc = [sum(r["rev"]["methane"] * defl(r["year"]) for r in run if r["year"] in W) / 1000 for run in mc[PK]]

out = dict(price_nominal={y: round(d7_nominal(y), 2) for y in YRS}, road_real={y: round(ROAD_REAL[y], 1) for y in YRS},
           c1_2030_39_tn=c1_w, c1_fee_alone_tn=c1_fee_alone, c1_band=[pctile(c1_mc, 0.1), pctile(c1_mc, 0.9)],
           c1_by_year_bn={y: round(v, 1) for y, v in c1_rows.items()}, c1_mid_ledger_basis="model package midpoint; the ledger sets its own figure", c2_2030_39_tn=c2_w, c3_2030_39_tn=c3_w, c3_band=[pctile(c3_mc, 0.1), pctile(c3_mc, 0.9)], c3_by_year_bn={y: round(C[PK][y]["rev"]["methane"] * defl(y), 1) for y in range(2030, 2051)}, process_option_tn=proc_w,
           road_exemption_revenue_tn=econ_extra, credit_cost_tn=cred_w, ces_acp_tn=acp_w,
           emissions={k: {y: dict(energy=round(C[k][y]["energy"]), below2005=round(C[k][y]["below2005"], 4), ghg_below2005=round(C[k][y]["ghgBelow2005"], 4),
                              clean_share=round(C[k][y]["cleanShare"], 3)) for y in (2030, 2035, 2040, 2050)} for k in C},
           households_2035=R["households"].get(PK))
json.dump(out, open("carbon.json", "w"), indent=1)

L_ = []; w = L_.append
fl, d7, cl, ec, nc = C[PK], C["d7"], C["cl"], C["econ"], C["noces"]
w("# Carbon fee model: emissions, receipts and the dividend under D7\n")
w("*Generated by `models/tools/carbon-model.py` (run by `run-all.sh`); do not edit by hand. The model is `models/tools/carbon/cfd-model.js`, Espen's Carbon Dividend Model (v3.4) from an earlier project, extended for Project 2050 (road fuels outside the fee, the Clean Energy Standard, the grid statute and Weatherization heat pumps; see `models/tools/carbon/readme.md`). Its design notes, sources and checks are in `legacy/sources/climate-carbon-dividend-model-notes.md`; its regression checks run on every rebuild. Inputs: `models/data/inputs/carbon-parameters.csv`, the transportation model and the ledger.*\n")
w("**What the model is.** A year-by-year structural simulation, 2025-2050, in 2025 dollars: power plants dispatched and built on cost (with a sourced build pipeline and grid-access limit), vehicle and truck fleets by age, heating equipment turnover, industrial efficiency, electrification and carbon capture, and methane and other gases, each responding to the fee and to the companion measures. It is calibrated to EIA's 2025 figures and its no-policy path sits inside Rhodium's and EIA's published ranges; against published fee studies it responds less in the first decade than NEMS, REGEN or E3, so its emission cuts lean conservative and its fee receipts lean high. Dollar figures are converted to nominal dollars at " + f"{P['inflation']*100:.1f}% a year (estimate) to match the ledger.\n")
w("**How Project 2050's climate policy is represented.**\n")
w(f"- **REV-C1 (D7, price revised Oct 26):** ${P['c1_start_price']} a ton in 2030 rising in D7's original equal steps through {int(P['c1_kink_year'])} (${d7_nominal(int(P['c1_kink_year'])):.0f}), then in equal steps to ${P['c1_price_2037']} in 2037, then {P['c1_growth_after']*100:.0f}% a year (nominal). CO2 from coal, natural gas and non-road petroleum; gasoline and diesel are outside it, priced only by Moving America's fuel-tax steps (from the transportation model), and half of other transport fuel is treated as exempt diesel (estimate). No ratchet (REV-C1C is an option). 80% returned equally per adult (CLI-2A: adults 18 and over, adult dependents included; children are covered by FAM-1).")
w("- **CLI-1A:** the model's restored credit set (the IRA's credits with bonus adders, from 2030, ten years for consumer credits).")
w(f"- **CLI-3A:** a tradable-credit Clean Energy Standard, {P['ces_target']*100:.0f}% clean electricity by {P['ces_year']} on a straight path from the 2029 share, held there after. Fossil output must buy credits; the credit price moves each year toward the level that meets the path and is capped at an alternative compliance payment of ${P['ces_acp']}/MWh (2025 dollars; estimate, CLI-3A sets no figure).")
w("- **CLI-4A:** the model's standards: vehicle rules as a soft floor on electric sales (25% of cars in 2032, 50% in 2037, 67% in 2040, 100% by 2050; trucks to 65%), unabated coal out by 2040, new baseload gas needing capture from 2033.")
w(f"- **CLI-5 and CLI-6:** Weatherization funding heat pumps in about {P['weatherize_homes_m']*1000:,.0f},000 low-income homes a year from 2031; the grid statute's interregional transfer minimums as {P['grid_statute_tx']} points a year of extra transmission growth and a slightly higher share of wind and solar usable before output is wasted (estimates). CLI-5's transmission ITC and 45X lines are inside CLI-1's credit set in the model.")
w("- **Not modeled:** CLI-7 and CLI-8 (disaster and adaptation; no emissions effect), CLI-4's statutory durability (the model assumes the rules hold), Moving America's transit and rail expansion, data-center load rules. Unchosen options CLI-9 and CLI-10 are shown as option rows.")
w("- The stipulated 2026-28 permitting deal is in every case, including current law.\n")

w("## Emissions\n")
w("Energy CO2 below 2005 (EIA's 2005 level, 5,999 Mt), net greenhouse gases below 2005 (EPA, 6,536 Mt), and the clean share of electricity. The first seven rows each add one layer to the row above; the rest change one thing against the decided package.\n")
w("| Case | Energy CO2 below 2005: 2030 / 2035 / 2040 / 2050 | Net GHG below 2005: 2035 / 2050 | Clean electricity: 2035 / 2050 |")
w("| --- | --- | --- | --- |")
for c in CASES:
    e = C[c["id"]]
    w(f"| {c['label']} | {' / '.join(pct(e[y]['below2005']) for y in (2030, 2035, 2040, 2050))} | {pct(e[2035]['ghgBelow2005'])} / {pct(e[2050]['ghgBelow2005'])} | {pct(e[2035]['cleanShare'])} / {pct(e[2050]['cleanShare'])} |")
w("")
lo35, hi35 = band("d7", 2035, lambda r: 1 - r["energy"] / E2005); lo50, hi50 = band("d7", 2050, lambda r: 1 - r["energy"] / E2005)
plo35, phi35 = band(PK, 2035, lambda r: 1 - r["energy"] / E2005); plo50, phi50 = band(PK, 2050, lambda r: 1 - r["energy"] / E2005)
w(f"**Uncertainty** ({P['mc_draws']} draws over the model's uncertain inputs; 10th-90th percentile): the decided package gives {pct(plo35)}-{pct(phi35)} below 2005 in 2035 and {pct(plo50)}-{pct(phi50)} in 2050 (the fee alone: {pct(lo35)}-{pct(hi35)} and {pct(lo50)}-{pct(hi50)}). These bands vary the model's inputs only; the disagreement between published models is wider, so treat them as a floor on the uncertainty.\n")
w("**Sectors under the decided package** (Mt CO2; change from current law in brackets):\n")
w("| Year | Power | Transport | Industry | Buildings |")
w("| --- | --- | --- | --- | --- |")
for y in (2030, 2035, 2040, 2050):
    w(f"| {y} | " + " | ".join(f"{fl[y][k]:,.0f} ({fl[y][k]-cl[y][k]:+,.0f})" for k in ("power", "transport", "industry", "buildings")) + " |")
w("")
miss = [y for y in range(P["ces_year"], 2051) if fl[y]["cleanShare"] < P["ces_target"] - 0.005]
hit = next((y for y in range(2030, 2051) if fl[y]["cleanShare"] >= P["ces_target"] - 0.005), None)
capyrs = [y for y in range(2030, 2051) if fl[y]["cesPrice"] >= P["ces_acp"] - 1e-6]
w(f"**The Clean Energy Standard (CLI-3).** With everything else in the package the clean share reaches {pct(fl[P['ces_year']]['cleanShare'])} in {P['ces_year']} against the {pct(P['ces_target'])} target, and first meets it in {hit or 'no year before 2051'}. " +
  (f"The credit price sits at the payment cap in {capyrs[0]}-{capyrs[-1]}, so suppliers pay the alternative compliance payment instead: about ${acp_w:.2f}T in 2030-39 (CLI-3 sends it to CLI-5's low-income energy lines). " if capyrs else "") +
  "The limit is grid access, not price: wind and solar can be connected only as fast as transmission allows (the model's sourced pipeline), which matches the durability session's warning that 80% by 2035 needs about 150 GW a year of clean builds. " +
  f"On top of everything else the CES changes power CO2 by {fl[2035]['power']-nc[2035]['power']:+,.0f} Mt in 2035 and {fl[2040]['power']-nc[2040]['power']:+,.0f} Mt in 2040: the fee and credits already push clean building to the grid limit, so with the fee in place the standard mostly sets a floor. Its value is durability: if the fee were repealed in 2033, the credits, standard and rules alone would still give {pct(C['nofee'][2035]['cleanShare'])} clean electricity in 2035 and {pct(C['nofee'][2040]['cleanShare'])} in 2040, and energy CO2 {pct(C['nofee'][2040]['below2005'])} below 2005 in 2040 against the package's {pct(fl[2040]['below2005'])} (row above).\n")
gap35 = ec[2035]["energy"] - fl[2035]["energy"]; gap50 = ec[2050]["energy"] - fl[2050]["energy"]
cum = sum(fl[y]["energy"] - ec[y]["energy"] for y in range(2030, 2051)) / 1000
cumpk = sum(cl[y]["energy"] - fl[y]["energy"] for y in range(2030, 2051)) / 1000
w(f"**The road-fuel exemption.** Pricing gasoline and diesel at the fee from 2030, on top of the package, would cut energy CO2 by a further {-gap35:,.0f} Mt in 2035 and {-gap50:,.0f} Mt in 2050: {cum:.1f} Gt over 2030-50 against the package's {cumpk:.1f} Gt below current law, about {100*cum/(cumpk+cum):.0f}% more. With the vehicle standards in place the pump price adds little, as the durability session found. Moving America's fuel steps reach about ${ROAD_REAL[2035]:.0f} a ton (2025 dollars) by 2035 and ${ROAD_REAL[2046]:.0f} by 2046, against the fee's ${D7_REAL[2035]:.0f} and ${D7_REAL[2046]:.0f}. The exemption gives up about ${econ_extra:.2f}T of receipts in 2030-39 (all on-road and most other diesel and gasoline; the revenue file's $0.27T was for the narrower REV-C1E).\n")

w("## Receipts and the dividend\n")
w(f"**REV-C1 (the domestic fee), on the decided package.** About **${c1_w:.2f}T** in 2030-39 (10th-90th percentile ${pctile(c1_mc,0.1):.2f}-{pctile(c1_mc,0.9):.2f}T), against the ledger's ${REV['C1']['mid']:.2f}T (range ${REV['C1']['lo']:.2f}-{REV['C1']['hi']:.2f}T, estimate). The fee alone would raise ${c1_fee_alone:.2f}T; the companion measures shrink its base by ${c1_fee_alone-c1_w:.2f}T. Because the model cuts emissions more slowly in the first decade than the large published models, its receipts sit toward the high side; a faster-responding model would land lower. The dividend (80%) is ${0.8*c1_w:.2f}T and the transition share ${0.2*c1_w:.2f}T.\n")
w("| Year | Fee ($/t, nominal) | Receipts ($B, nominal) | Energy CO2 (Mt) | Clean electricity | Dividend per adult ($, nominal) | Couple |")
w("| --- | --- | --- | --- | --- | --- | --- |")
for y in (2030, 2031, 2032, 2033, 2034, 2035, 2036, 2037, 2038, 2039, 2040, 2045, 2050):
    r = fl[y]; dv = P["dividend_share"] * c1(r) * defl(y) * 1e9 / (r["pop"] * 0.77 * 1e6)
    w(f"| {y} | {d7_nominal(y):.0f} | {c1(r)*defl(y):,.0f} | {r['energy']:,.0f} | {pct(r['cleanShare'])} | {dv:,.0f} | {2*dv:,.0f} |")
w("")
rv = lambda k: nom_sum(PK, lambda r: r["rev"][k])
w(f"By source, 2030-39: industry ${rv('industry'):.2f}T, buildings ${rv('buildings'):.2f}T, power ${rv('power'):.2f}T, non-road transport ${rv('transport'):.2f}T. Industry is the largest base because its abatement (efficiency, capture, electric heat) comes slowly; power is smaller because coal leaves quickly. Receipts keep rising after 2039 because the price (5% a year) rises faster than emissions fall. The per-adult dividend uses CBO's population path (the model's), with adults 77% of it.\n")
w(f"**REV-C2 (the border adjustment).** With the border adjustment on at the same price, the model nets about **${c2_w:.3f}T** in 2030-39: charges on the embodied carbon of covered imports (284 Mt, with a 15% credit for carbon prices paid abroad) less rebates on exports (211 Mt), which nearly offset each other. The ledger carries ${REV['C2']['mid']:.2f}T (estimate, scaled from a combined border-and-methane figure). The model's border inputs are partly judgment (see `legacy/sources/climate-border-adjustment-model-notes.md`).\n")
w(f"**REV-C3 (the methane fee).** The IRA's methane charge (the Waste Emissions Charge, Clean Air Act sec. 136) was the first federal fee on a greenhouse gas: $900 a ton of methane in its first year, $1,200 in its second and $1,500 from its third, not indexed, on oil and gas facilities above 25,000 t CO2e, charged only on methane above an intensity threshold and waived once EPA's sec. 111 methane standards (leak detection and repair, limits on venting and flaring) were in effect in every state. Congress repealed EPA's rule for it in March 2025 (P.L. 119-2) and the 2025 reconciliation law delayed the charge to 2034 (P.L. 119-21; CRS R48906, April 2026). REV-C3 reinstates it from {P['ch4_start']} at ${P['ch4_rate_2030']:,.0f} a ton of methane, rising to ${P['ch4_rate_2032']:,.0f} by 2032 (about ${P['ch4_rate_2032']/P['gwp100']:.0f} a ton of CO2e), on all methane at facilities above the 25,000-ton threshold (about {P['ch4_og_share']*100:.0f}% of the sector's methane, estimate), with no intensity threshold. It keeps the IRA's structure of a fee with a way out, made facility by facility: a facility is exempt for a year if it certifies, on an independent audit and measurement-based reporting, that it meets the leak-prevention standards; a super-emitter event or a failed audit ends the exemption. The model assumes {P['cert_s0']*100:.0f}% of covered methane is at certified facilities in 2030 and {P['cert_s1']*100:.0f}% by {P['cert_year']}, and that certification cuts a facility's methane by {P['cert_abate']*100:.0f}% (estimates; EPA put its 2024 standards at nearly 80%). It raises about **${c3_w:.3f}T** in 2030-39 (10th-90th percentile ${pctile(c3_mc,0.1):.3f}-{pctile(c3_mc,0.9):.3f}T), against ${c3_nocert:.2f}T with no exemption: the exemption trades revenue for compliance, which is the point. On the IRA's own narrow base it would raise only about ${c3_ira:.3f}T. The rate is fixed in dollars, so it falls below REV-C1 per ton of CO2e from {next((y for y in range(2030, 2051) if ch4_nominal(y) / P['gwp100'] < d7_nominal(y)), 'no year')} on. Options: three times the carbon fee per ton of CO2e (methane's 20-year warming potential) with coal mines, ${c3_x3:.2f}T without the exemption; landfills added, ${c3_lf:.3f}T. Net greenhouse gases: {pct(fl[2035]['ghgBelow2005'])} below 2005 in 2035 with the fee, against {pct(C['nomf'][2035]['ghgBelow2005'])} without it; methane is {C['nomf'][2035]['methane'] - fl[2035]['methane']:,.0f} Mt CO2e lower in 2035 and {C['ch4nocert'][2035]['methane'] - fl[2035]['methane']:,.0f} Mt lower than the same fee with no exemption would leave it, because certification requires the standards' deeper cuts.\n")
w(f"**Industrial process CO2 and N2O (an option).** Extending REV-C1's price to process emissions (cement, steel, ammonia, petrochemicals) would raise about ${proc_w:.2f}T more in 2030-39.\n")
w(f"**Credits in the model.** The package's credit outlays come to about ${cred_w:.2f}T in 2030-39 in the model's accounting, against the ledger's ${BILL['CLI-1']['cost_mid']:.2f}T for CLI-1A (range ${BILL['CLI-1']['cost_lo']:.2f}-{BILL['CLI-1']['cost_hi']:.2f}T) and CLI-5's transmission ITC and 45X lines (about $0.22T). The model's set includes bonus adders and the hydrogen credit and prices take-up off the larger clean build under the fee and the CES, so it is a cross-check on the high end, not a score.\n")

hh = R["households"].get(PK)
if hh:
    w("## Households in 2035 (the carbon channel alone)\n")
    w("Per household in 2025 dollars, from the model's household module (BLS Consumer Expenditure Survey 2024 quintiles), on the decided package: the fee's cost through heating fuel, electricity and everything else, against the dividend. **The dividend is the same for every adult at every income (CLI-2A); children get no share, since FAM-1's child credit covers them**; household totals differ only because households have different numbers of adults (the survey's lowest quintile averages 1.3, the highest 2.4). Costs rise with income because spending, and the carbon in it, does; an equal payment against costs that rise with income is what makes the dividend progressive. Gasoline costs nothing here because road fuels are outside the fee; Moving America's fuel steps and every other row are in the incidence model, which remains the D3 test.\n")
    w("| Quintile | Adults | Dividend per adult | Dividend per household | Heating | Electricity | Other goods | Net per household |")
    w("| --- | --- | --- | --- | --- | --- | --- | --- |")
    for g in hh:
        w(f"| {g['name']} | {g['people']-g['kids']:.1f} | {g['dividend']/max(g['people']-g['kids'],1e-9):,.0f} | {g['dividend']:+,.0f} | {-g['heat']:,.0f} | {-g['elec']:,.0f} | {-g['other']:,.0f} | {g['net']:+,.0f} |")
    w("")

w("## Against the ledger\n")
w("| Row | This model, 2030-39 ($T) | Ledger, mid (range) | Note |")
w("| --- | --- | --- | --- |")
lg = lambda i: f"{REV[i]['mid']:.2f} ({REV[i]['lo']:.2f}-{REV[i]['hi']:.2f})" if i in REV else "not in the ledger"
w(f"| REV-C1 (C1) | {c1_w:.2f} ({pctile(c1_mc,0.1):.2f}-{pctile(c1_mc,0.9):.2f}) | {lg('C1')} | the ledger sits below the model because the model responds slowly in the first decade |")
w(f"| REV-C2 (C2) | {c2_w:.3f} | {lg('C2')} | export rebates nearly cancel the import charge |")
w(f"| REV-C3 (C3) | {c3_w:.3f} ({pctile(c3_mc,0.1):.3f}-{pctile(c3_mc,0.9):.3f}) | {lg('C3')} | credited to CLI-5 |")
w(f"| Excise offset (CX) | {-0.25*(c1_w+c2_w+c3_w):.2f} | {lg('CX')} | 25% of the carbon, border and methane fees (the scorekeepers' convention, as MR6 for Moving America) |")
if capyrs: w(f"\nCLI-3's 80%-by-2035 target is not met in the model ({pct(fl[P['ces_year']]['cleanShare'])} in {P['ces_year']}); its alternative compliance payments, about ${acp_w:.2f}T in 2030-39, are an unsized channel. The incidence model spreads REV-C1 over the window with its own profile (`incidence-phase-in.csv`, C1); the model's year-by-year receipts could replace it.\n")
open("climate-carbon-model.md", "w").write("\n".join(L_))
print(f"carbon: package REV-C1 2030-39 ${c1_w:.2f}T (fee alone {c1_fee_alone:.2f}; ledger {REV['C1']['mid']}); energy CO2 below 2005 2035 {pct(fl[2035]['below2005'])}, 2050 {pct(fl[2050]['below2005'])}; clean 2035 {pct(fl[2035]['cleanShare'])}; C2 ${c2_w:.3f}T; C3 ${c3_w:.2f}T")
