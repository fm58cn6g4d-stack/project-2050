"""Carbon model for Project 2050's D7 design: emissions, REV-C1 and REV-C2 receipts, the dividend, and the companion measures.

Runs the structural carbon-fee model in index/tools/carbon/ (Espen's Carbon Dividend Model, v3.4, built in an earlier
project; see sources/climate-carbon-dividend-model-notes.md) on Project 2050's decided design rather than the design
that model was built for: REV-C1 at $25 a ton in 2030 rising to about $100 by 2037, then 5% a year; gasoline and diesel
outside the fee and priced only by Moving America's fuel-tax steps; CO2 from fuel combustion only (methane fees and the
border adjustment are separate lines); 80% returned per person. Inputs: index/data/inputs/carbon-parameters.csv, the
transportation model and ledger.json. Writes carbon.json and climate-carbon-model.md. Needs node.
"""
import json, os, subprocess, sys
from inputs import read, num

HERE = os.path.dirname(os.path.abspath(__file__))
def find(*parts):
    for d in (os.path.join(HERE, *parts), os.path.join(HERE, "..", "index", "tools", *parts)):
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
    s, p0, p37 = P["c1_start_year"], P["c1_start_price"], P["c1_price_2037"]
    if y < s: return 0.0
    if y <= 2037: return p0 + (p37 - p0) * (y - s) / (2037 - s)
    return p37 * (1 + P["c1_growth_after"]) ** (y - 2037)
D7_REAL = {y: d7_nominal(y) / defl(y) for y in YRS}

# Moving America's fuel-tax steps as a road-fuel price, $ a ton of CO2 in 2025 dollars (gasoline: 0.0085 $/gal per $/t, as in the carbon model)
MOV = ma.Revenue(ma.Design(), premium=True)
ROAD_REAL = {y: max(MOV.gr(y) - 18.4, 0) / 100 / defl(y) / 0.0085 if y >= 2029 else 0.0 for y in YRS}

base_pol = {"permitYear": P["permit_year"], "startPrice": 0, "step": 0, "ratchet": False}
d7_pol = dict(base_pol, roadExempt=True, roadPath=ROAD_REAL, othRoad=P["oth_road"], offset=0, admin=0, dividendShare=P["dividend_share"],
              cover={"process": False, "methane": False, "fgas": False, "border": False, "bunkers": False}, ratchet=False)
CASES = [
    dict(id="cl", label="Current law (with the stipulated 2026-28 permitting deal)", policy=base_pol, price=None),
    dict(id="mov", label="+ Moving America's fuel-tax steps (no carbon fee)", policy=dict(base_pol, roadExempt=True, roadPath=ROAD_REAL), price=None),
    dict(id="d7", label="+ REV-C1 on D7's path, road fuels exempt (the decided fee)", policy=d7_pol, price=D7_REAL, mc=True, households=2035, householdsBase="mov"),
    dict(id="d7cr", label="+ CLI-1 restored clean-energy credits", policy=dict(d7_pol, credits=True), price=D7_REAL),
    dict(id="d7crst", label="+ CLI-4 vehicle and power standards (restored authority, used)", policy=dict(d7_pol, credits=True, standards=True), price=D7_REAL, mc=True),
    dict(id="border", label="D7 fee with the border adjustment switched on (sizes REV-C2)", policy=dict(d7_pol, cover=dict(d7_pol["cover"], border=True)), price=D7_REAL),
    dict(id="methane", label="D7 fee extended to methane, process CO2 and N2O (sizes the methane-fee line)", policy=dict(d7_pol, cover=dict(d7_pol["cover"], methane=True, process=True)), price=D7_REAL),
    dict(id="econ", label="Same price on road fuels too (REV-C1D-style convergence from 2030)", policy=dict(d7_pol, roadExempt=False), price=D7_REAL),
    dict(id="orig", label="The model's own design ($40 a ton in 2030 + $8 a year real, ratchet, wider coverage, 90% dividend)", policy={"permitYear": P["permit_year"]}, price=None),
]
cfg = dict(cases=CASES, mcDraws=P["mc_draws"], mcSeed=P["mc_seed"])
json.dump(cfg, open("carbon-config.json", "w"))
R = json.loads(subprocess.run(["node", os.path.join(CARBON, "p2050-run.js"), "carbon-config.json"], check=True, capture_output=True, text=True).stdout)
C = {k: {r["year"]: r for r in v} for k, v in R["cases"].items()}

def nom_sum(case, f, yrs=W): return sum(f(C[case][y]) * defl(y) for y in yrs) / 1000   # $T nominal
def pct(x): return f"{100*x:.0f}%"
def pctile(xs, q):
    xs = sorted(xs); i = (len(xs) - 1) * q; lo = int(i); return xs[lo] + (xs[min(lo + 1, len(xs) - 1)] - xs[lo]) * (i - lo)
E2005, NET2005 = 5999, 6536

c1_w = nom_sum("d7", lambda r: r["gross"])
c1_rows = {y: C["d7"][y]["gross"] * defl(y) for y in range(2030, 2051)}
c2_w = nom_sum("border", lambda r: r["rev"]["border"])
meth_w = nom_sum("methane", lambda r: r["rev"]["methane"] + r["rev"]["process"])
econ_extra = nom_sum("econ", lambda r: r["gross"]) - c1_w
cred_w = nom_sum("d7cr", lambda r: r["credits"])
cred_all_w = nom_sum("d7crst", lambda r: r["credits"])
mc = {k: v for k, v in R["mc"].items()}
def band(case, y, f):
    xs = [f({r["year"]: r for r in run}[y]) for run in mc[case]]
    return pctile(xs, 0.1), pctile(xs, 0.9)
c1_mc = [sum(r["gross"] * defl(r["year"]) for r in run if r["year"] in W) / 1000 for run in mc["d7"]]

out = dict(price_nominal={y: round(d7_nominal(y), 2) for y in YRS}, road_real={y: round(ROAD_REAL[y], 1) for y in YRS},
           c1_2030_39_tn=c1_w, c1_band=[pctile(c1_mc, 0.1), pctile(c1_mc, 0.9)], c1_by_year_bn={y: round(v, 1) for y, v in c1_rows.items()},
           c2_2030_39_tn=c2_w, methane_fee_2030_39_tn=meth_w, road_exemption_revenue_tn=econ_extra, cli1_credit_cost_tn=cred_w,
           emissions={k: {y: dict(energy=round(C[k][y]["energy"]), below2005=round(C[k][y]["below2005"], 4), ghg_below2005=round(C[k][y]["ghgBelow2005"], 4))
                          for y in (2030, 2035, 2040, 2050)} for k in C},
           households_2035=R["households"].get("d7"))
json.dump(out, open("carbon.json", "w"), indent=1)

# ---------- report ----------
L_ = []; w = L_.append
w("# Carbon fee model: emissions, receipts and the dividend under D7\n")
w("*Generated by `index/tools/carbon-model.py` (run by `run-all.sh`); do not edit by hand. The model itself is `index/tools/carbon/cfd-model.js`, Espen's Carbon Dividend Model (v3.4) from an earlier project, with one addition for Project 2050: road fuels can be held outside the fee and priced by their own per-gallon tax. Its design notes, sources and checks are in `sources/climate-carbon-dividend-model-notes.md`; its 45 regression checks run on every rebuild. Inputs: `index/data/inputs/carbon-parameters.csv`, the transportation model and the ledger.*\n")
w("**What the model is.** A year-by-year structural simulation, 2025-2050, in 2025 dollars: power plants dispatched and built on cost (with a sourced build pipeline and grid-access limit), vehicle and truck fleets by age, heating equipment turnover, industrial efficiency, electrification and carbon capture, and methane and other gases, each responding to the fee and to the companion measures. It is calibrated to EIA's 2025 figures and its no-policy path sits inside Rhodium's and EIA's published ranges; against published fee studies it responds less in the first decade than NEMS, REGEN or E3 (the notes give the comparison), so its emission cuts lean conservative. Dollar figures here are converted to nominal dollars at " + f"{P['inflation']*100:.1f}% a year (estimate) to match the ledger.\n")
w("**How it is run for Project 2050.** REV-C1 at $" + f"{P['c1_start_price']}" + " a ton in 2030 rising in equal steps to $" + f"{P['c1_price_2037']}" + " in 2037, then " + f"{P['c1_growth_after']*100:.0f}" + "% a year (nominal; D7). Gasoline and diesel are outside the fee: their price moves only with Moving America's fuel-tax steps (from the transportation model, as a per-ton equivalent), and half of other transport fuel (rail, marine, off-road) is treated as diesel and exempt too (estimate). The fee covers CO2 from coal, natural gas and the remaining petroleum; methane, process CO2 and the border adjustment are separate lines, sized below. No ratchet (REV-C1C is an option). 80% is returned per person. The stipulated 2026-28 permitting deal is in every case, including current law.\n")

w("## Emissions\n")
w("Energy CO2 below 2005 (EIA's 2005 level, 5,999 Mt), and net greenhouse gases below 2005 (EPA, 6,536 Mt). Each row adds one measure to the row above, except the last four, which change one thing against the decided fee.\n")
w("| Case | Energy CO2 below 2005: 2030 / 2035 / 2040 / 2050 | Net GHG below 2005: 2035 / 2050 |")
w("| --- | --- | --- |")
for c in CASES:
    e = C[c["id"]]
    w(f"| {c['label']} | {' / '.join(pct(e[y]['below2005']) for y in (2030, 2035, 2040, 2050))} | {pct(e[2035]['ghgBelow2005'])} / {pct(e[2050]['ghgBelow2005'])} |")
w("")
lo35, hi35 = band("d7", 2035, lambda r: 1 - r["energy"] / E2005); lo50, hi50 = band("d7", 2050, lambda r: 1 - r["energy"] / E2005)
plo35, phi35 = band("d7crst", 2035, lambda r: 1 - r["energy"] / E2005); plo50, phi50 = band("d7crst", 2050, lambda r: 1 - r["energy"] / E2005)
w(f"**Uncertainty** ({P['mc_draws']} draws over the model's 37 uncertain inputs; 10th-90th percentile): the decided fee gives {pct(lo35)}-{pct(hi35)} below 2005 in 2035 and {pct(lo50)}-{pct(hi50)} in 2050; with CLI-1 and CLI-4, {pct(plo35)}-{pct(phi35)} and {pct(plo50)}-{pct(phi50)}. These bands are parametric only; the gap between published models is wider (see the notes).\n")
d7, mv, cl, ec = C["d7"], C["mov"], C["cl"], C["econ"]
w("**Sectors under the decided fee** (Mt CO2; change from current law in brackets):\n")
w("| Year | Power | Transport | Industry | Buildings |")
w("| --- | --- | --- | --- | --- |")
for y in (2030, 2035, 2040, 2050):
    w(f"| {y} | " + " | ".join(f"{d7[y][k]:,.0f} ({d7[y][k]-cl[y][k]:+,.0f})" for k in ("power", "transport", "industry", "buildings")) + " |")
w("")
gap35 = ec[2035]["energy"] - d7[2035]["energy"]; gap50 = ec[2050]["energy"] - d7[2050]["energy"]
cum = sum(d7[y]["energy"] - ec[y]["energy"] for y in range(2030, 2051)) / 1000
cumfee = sum(cl[y]["energy"] - d7[y]["energy"] for y in range(2030, 2051)) / 1000
w(f"**The road-fuel exemption.** Pricing gasoline and diesel at the fee from 2030 would cut energy CO2 by a further {-gap35:,.0f} Mt in 2035 and {-gap50:,.0f} Mt in 2050, {cum:.1f} Gt over 2030-50, against the {cumfee:.1f} Gt the decided fee cuts below current law: the exemption gives up about {100*cum/(cumfee+cum):.0f}% of an economy-wide fee's cuts. Road emissions respond little to price in the model, as in the durability session (which put a later gasoline phase-in at about 1% of the whole plan's avoided emissions); vehicle standards (CLI-4) do far more for transport (rows above). Moving America's fuel steps reach about ${ROAD_REAL[2035]:.0f} a ton (2025 dollars) by 2035 and ${ROAD_REAL[2046]:.0f} by 2046, against the fee's ${D7_REAL[2035]:.0f} and ${D7_REAL[2046]:.0f}. Exempting all on-road and most other diesel and gasoline gives up about ${econ_extra:.2f}T of receipts in 2030-39; the revenue file's $0.27T was for the narrower REV-C1E (a gasoline phase-in from 2032).\n")

w("## Receipts and the dividend\n")
w(f"**REV-C1 (the domestic fee).** About **${c1_w:.2f}T** in 2030-39 (10th-90th percentile ${pctile(c1_mc,0.1):.2f}-{pctile(c1_mc,0.9):.2f}T), against the ledger's ${REV['C1']['mid']:.2f}T (range ${REV['C1']['lo']:.2f}-{REV['C1']['hi']:.2f}T, estimate). Because the model cuts emissions less in the first decade than NEMS, REGEN or E3, its receipts sit toward the high side; a faster-responding model would land nearer the ledger's figure. The dividend (80%) is ${0.8*c1_w:.2f}T and the transition share ${0.2*c1_w:.2f}T.\n")
w("| Year | Fee ($/t, nominal) | Receipts ($B, nominal) | Energy CO2 (Mt) | Dividend per person ($, nominal) | Family of four |")
w("| --- | --- | --- | --- | --- | --- |")
for y in (2030, 2031, 2032, 2033, 2034, 2035, 2036, 2037, 2038, 2039, 2040, 2045, 2050):
    r = d7[y]; dv = P["dividend_share"] * r["gross"] * defl(y) * 1e9 / (r["pop"] * 1e6)
    w(f"| {y} | {d7_nominal(y):.0f} | {r['gross']*defl(y):,.0f} | {r['energy']:,.0f} | {dv:,.0f} | {4*dv:,.0f} |")
w("")
w(f"Receipts keep rising after 2039 because the price (5% a year) rises faster than emissions fall. The per-person dividend uses CBO's population path (the model's).\n")
w(f"**REV-C2 (the border adjustment).** With the border adjustment on at the same price, the model nets about **${c2_w:.3f}T** in 2030-39: charges on the embodied carbon of covered imports (284 Mt, with a 15% credit for carbon prices paid abroad) less rebates on exports (211 Mt), which nearly offset each other. The ledger carries ${REV['C2']['mid']:.2f}T (estimate, scaled from a combined border-and-methane figure). Without export rebates the charge alone would be several times larger; the model's notes list what a real border model would need.\n")
w(f"**Methane and process gases (the unsized methane-fee line).** Extending the same price to methane from oil, gas, coal mines and landfills, and to process CO2 and N2O, would raise about **${meth_w:.2f}T** in 2030-39 and cut net GHG further (row above). This is the first figure the project has for the methane-fee line that REV-C2 shares.\n")
w(f"**CLI-1's credits in the model.** Restoring the credits from 2030 costs about ${cred_w:.2f}T in 2030-39 in the model's accounting (with CLI-4's standards on, ${cred_all_w:.2f}T), against the ledger's ${BILL['CLI-1']['cost_mid']:.2f}T for CLI-1A (range ${BILL['CLI-1']['cost_lo']:.2f}-{BILL['CLI-1']['cost_hi']:.2f}T). The model's credit set is the IRA's restored with bonus adders, plus the hydrogen and transmission credits, and it prices take-up off its own (larger) clean build under the fee, so it runs above the ledger's scaled figure; it is a cross-check on CLI-1's high end, not a score.\n")

hh = R["households"].get("d7")
if hh:
    w("## Households in 2035 (the carbon channel alone)\n")
    w("Per household, from the model's household module (BLS Consumer Expenditure Survey 2024 quintiles): the fee's cost through heating fuel, electricity and everything else, against the dividend. Gasoline costs nothing here because road fuels are outside the fee; Moving America's fuel steps and every other row are in the incidence model, which remains the D3 test.\n")
    w("| Quintile | Heating | Electricity | Other goods | Dividend | Net |")
    w("| --- | --- | --- | --- | --- | --- |")
    for g in hh:
        w(f"| {g['name']} | {-g['heat']:,.0f} | {-g['elec']:,.0f} | {-g['other']:,.0f} | {g['dividend']:+,.0f} | {g['net']:+,.0f} |")
    w("")

w("## Findings for the ledger (proposals, not applied)\n")
w(f"- REV-C1's ten-year receipts come out at ${c1_w:.2f}T against the ledger's ${REV['C1']['mid']:.2f}T.")
w(f"- REV-C2 nets only about ${c2_w:.2f}T once export rebates are counted, against ${REV['C2']['mid']:.2f}T. CLI-5's financing leans on it.")
w(f"- A methane and process-gas fee at the same price would raise about ${meth_w:.2f}T.")
w("- The general fund carries no income- and payroll-tax offset for REV-C1. Scorekeepers reduce an excise's net receipts by about 25% because it lowers taxable incomes; the ledger books that offset for Moving America (MR6) but not for the carbon fee, so about " + f"${0.25*c1_w:.2f}T" + " of general-fund revenue loss is uncounted.")
w("- The incidence model spreads REV-C1 over the window with an assumed profile (`incidence-phase-in.csv`, C1); the model's year-by-year receipts could replace it.\n")
open("climate-carbon-model.md", "w").write("\n".join(L_))
print(f"carbon: REV-C1 2030-39 ${c1_w:.2f}T (ledger {REV['C1']['mid']}); energy CO2 below 2005 in 2035 {pct(d7[2035]['below2005'])}, 2050 {pct(d7[2050]['below2005'])}; C2 ${c2_w:.3f}T; methane ${meth_w:.2f}T")
