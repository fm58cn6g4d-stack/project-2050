"""MOD-energy, one command: runs every scenario, the benchmarks and the accounts, and writes results.json and results.md.

Usage (from the repository root):  python3 models/tools/energy/run.py [--out DIR]
DIR defaults to models/tools/energy/; run-all.sh writes to build/energy/ and compares with the committed copies.
Outputs carry no dates: the run log is the hashes of every input, so the same inputs give the same files.
"""
import argparse, csv, hashlib, json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import data  # noqa: E402
import history  # noqa: E402
import model as m  # noqa: E402

ROOT = data.ROOT
MARK = ("energy", "below2005", "ghgBelow2005", "cleanShare", "power", "transport", "industry", "buildings", "process", "methane", "retail", "evShare", "hp")
SCC_2020 = {2030: 230, 2040: 270, 2050: 310}   # EPA 2023 (SRC-5006), SC-CO2 at a 2% near-term rate, 2020 dollars per ton
TCRE = (0.27, 0.45, 0.63)                      # IPCC AR6 WG1 SPM D.1.1 (SRC-5037), deg C per 1,000 Gt CO2


LEGACY_WORLD = {"crYears": 10, "crVehYears": None, "retailNetCredits": False, "retailAcp": False, "fuelSpread": {"coal": 0, "gas": 0}, "coalVom": 4, "emCal": 1.024, "crPhase": False, "crPowSched": None}   # undo this model's world settings: carbon-model.py runs the defaults


EPS2_WORLD = {"zevPath": {2032: 0.25, 2037: 0.5, 2040: 0.67, 2050: 1.0}, "zevTrkPath": {2032: 0.03, 2037: 0.20, 2040: 0.26, 2050: 0.65}}   # EPS run 2's sales standards


def bench_cases():
    """Extra engine runs the benchmarks need (none is a policy Project 2050 proposes)."""
    mov = m.scenarios()[0][1][2]
    econ = dict(mov, cover=dict(m.COVER_NONE, process=True), sectorPrice={"buildings": 1, "industry": 1, "nonroad": 1}, offset=0, admin=0, ratchet=False)
    cbo = dict(m.NO_FEE, permitYear=None, cover=dict(m.COVER_NONE, process=True), offset=0, admin=0, ratchet=False)
    P = m.P
    legacy = dict(m.NO_FEE, permitYear=P["permit_year"], childShare=0, roadExempt=True, roadPath=m.ROAD, othRoad=P["oth_road"], offset=0, admin=0,
                  dividendShare=P["dividend_share"], cover=dict(m.COVER_NONE), ratchet=False, credits=True,
                  ces={"start": P["ces_start"], "target": P["ces_target"], "year": P["ces_year"]}, standards=True, gridStatute=True, weatherize=True, methaneFee=m.METHANE_FEE)
    # Espen's EPS runs (models/data/energy/eps-us-4.0.7-runs-2026-11-13-p2050.csv): price points as set, straight lines between
    pts = {2029: 0, 2030: 23.1, 2031: 31.35, 2032: 39.6, 2033: 56.1, 2035: 87.45, 2036: 102.3, 2037: 115.5, 2038: 118.8, 2040: 125.4, 2045: 143.55, 2050: 165}
    eps_path = {y: (interp(pts, y) if y >= 2030 else 0.0) for y in m.YRS}
    eps1 = dict(m.NO_FEE, permitYear=None, cover=dict(m.COVER_NONE, process=True, fgas=True), fgasRate=1.0, sectorPrice={"buildings": 0, "industry": 1, "nonroad": 0},
                offset=0, admin=0, ratchet=False, methaneFee={"start": 2030, "mult": 1, "floor": 0, "ogShare": 1, "coal": True, "landfill": False})
    eps2 = dict(eps1, credits=True, ces=m.CES, standards=True, heatStd=m.HEAT)
    cbo_path = {y: (25 * 1.05 ** (y - 2025) if y >= 2025 else 0.0) / 1.0 for y in m.YRS}   # CBO option 73: $25 in 2025 rising 5% a year above inflation
    return [dict(id="b_econ", label="Benchmark run: economy-wide price on the decided path, nothing else", policy=econ, price=m.PRICE),
            dict(id="b_cbo", label="Benchmark run: CBO's option ($25 a ton from 2025, +5% a year real, all fuels)", policy=cbo, price=cbo_path),
            dict(id="b_cr", label="Benchmark run: the credits alone, no price", policy=dict(mov, credits=True), price=None),
            dict(id="b_legacy", label="Benchmark run: the legacy decided package as carbon-model.py runs it", policy=legacy, price=m.PRICE, world=LEGACY_WORLD),
            dict(id="b_eps1", label="Matched to Espen's EPS run 1: the price on power and all industry, with process CO2, oil, gas and coal-mine methane and fluorinated gases priced (EPS's defaults)", policy=eps1, price=eps_path),
            dict(id="b_eps2", label="Matched to Espen's EPS run 2: run 1 plus the credits, the 80%/100% standard, EPS's sales-standard paths and the clean-heat standard", policy=eps2, price=eps_path, world=EPS2_WORLD)]


def interp(tbl, y):
    ks = sorted(tbl)
    if y <= ks[0]:
        return tbl[ks[0]]
    for lo, hi in zip(ks, ks[1:]):
        if y <= hi:
            return tbl[lo] + (tbl[hi] - tbl[lo]) * (y - lo) / (hi - lo)
    return tbl[ks[-1]]


def smape(a, b):
    return 100 * sum(abs(x - y) / ((abs(x) + abs(y)) / 2) for x, y in zip(a, b)) / len(a)


def benchmarks(E, ACC, HH):
    """Each benchmark: id, what, model, target, tolerance, result (pass, fail or reported), why a difference arises."""
    out = []
    add = lambda **k: out.append(k)
    cl, r25 = E["cl"], E["cl"][2025]
    eia = data.EIA_2025
    miss = {s: (r25[k] - eia[s]) / eia[s] for s, k in [("power", "power"), ("transport", "transport"), ("industry", "industry"), ("total", "energy")]}
    miss["buildings"] = (r25["buildings"] - eia["residential"] - eia["commercial"]) / (eia["residential"] + eia["commercial"])
    worst = max(miss, key=lambda k: abs(miss[k]))
    add(id="DA-1", what="Energy CO2 by sector, 2025, against EIA's measured figures (SRC-5004)",
        model=", ".join(f"{k} {100 * v:+.1f}%" for k, v in miss.items()), target="EIA 2025: total 4,904 Mt", tol="within 2% in every sector",
        result="pass (in-sample)" if abs(miss[worst]) <= 0.02 else "fail",
        why="The engine is calibrated to these figures, so the pass shows the starting point is right, not that the model predicts. EIA's October Monthly Energy Review revises 2025 to 4,916 Mt (+0.2%).")
    add(id="DA-2", what="Net greenhouse gases in 2005, the goals' base (EPA inventory, SRC-4460)", model=f"{6536:,} Mt", target=f"{data.EPA_NET_2005:,} Mt",
        tol="within 0.1%", result="pass (in-sample)" if abs(6536 - data.EPA_NET_2005) / data.EPA_NET_2005 < 0.001 else "fail",
        why="The engine carries EPA's figure; this checks the two have not drifted apart.")
    aeo = data.aeo_table18("combination")
    yrs = (2030, 2035, 2040)
    gaps = {y: (cl[y]["energy"] - aeo["total"][y]) / aeo["total"][y] for y in yrs + (2050,)}
    add(id="BL-1", what="Energy CO2 under 2029 current law, against AEO2026's combination case (SRC-5049)",
        model=", ".join(f"{y}: {cl[y]['energy']:,.0f}" for y in yrs + (2050,)), target=", ".join(f"{y}: {aeo['total'][y]:,.0f}" for y in yrs + (2050,)),
        tol="within 5% in 2030, 2035 and 2040; 2050 reported", result="pass" if all(abs(gaps[y]) <= 0.05 for y in yrs) else "fail",
        why=f"Gaps {', '.join(f'{y} {100 * g:+.1f}%' for y, g in gaps.items())}. They part after 2040: AEO2026 has power CO2 rising again from 2040 (to {aeo['power'][2050]:,.0f} Mt in 2050, with data-center load and gas build), while the engine keeps retiring coal and adding wind and solar ({cl[2050]['power']:,.0f} Mt); and the engine's electric-vehicle uptake is faster ({cl[2050]['transport']:,.0f} against {aeo['transport'][2050]:,.0f} Mt of transport CO2). EIA's own reference cases have missed energy CO2 by 14.6% on average (SRC-5002), so the 2050 gap is inside the range of a baseline's error.")
    s = smape([cl[y]["energy"] for y in range(2026, 2051)], [aeo["total"][y] for y in range(2026, 2051)])
    add(id="EM-1", what="Closeness of the current-law path to AEO2026's combination case, 2026-2050 (symmetric mean absolute percentage error, the En-ROADS practice, SRC-5045)",
        model=f"{s:.1f}%", target="0%", tol="reported", result="reported", why="One number for how far apart two whole paths are; the year-by-year gaps are in BL-1.")
    g35 = 100 * cl[2035]["ghgBelow2005"]
    add(id="BL-2", what="Net greenhouse gases below 2005 in 2035 under current policy", model=f"{g35:.0f}%",
        target="Rhodium 26-35% (SRC-4474); the 2026 review's OBBBA runs 31-37% (SRC-4479)", tol="inside 26-37%",
        result="pass" if 26 <= g35 <= 37 else "fail", why="Both benchmarks include the 2025 law; Rhodium's lower end assumes high gas prices and slower clean build.")
    eps = data.eps_runs()
    ch = lambda path, y: 100 * (path[y] / path[2025] - 1)
    mc_ = {y: ch({k: cl[k]["ghgNet"] for k in cl}, y) for y in (2035, 2050)}
    ec_ = {y: ch(eps["current_policies"], y) for y in (2035, 2050)}
    add(id="BL-3", what="Net greenhouse gases under current policy, change from 2025 (the Energy Policy Simulator's Current Policies pathway, run by Espen, November 13, 2026)",
        model=f"2035 {mc_[2035]:+.0f}%, 2050 {mc_[2050]:+.0f}%", target=f"EPS 4.0.7: 2035 {ec_[2035]:+.0f}%, 2050 {ec_[2050]:+.0f}%",
        tol="within 5 points in 2035; 2050 reported", result="pass" if abs(mc_[2035] - ec_[2035]) <= 5 else "fail",
        why=f"Compared as changes from each model's own 2025, because the bases differ: EPS starts at {eps['current_policies'][2025]:,.0f} Mt with its land sink, the engine at 5,360 Mt (Rhodium's 2025 estimate, 18% below 2005). EPS's baseline includes the 2025 law and later EPA actions (SRC-5017), like this one. After 2040 EPS's emissions level off ({eps['current_policies'][2040]:,.0f} Mt in 2040, {eps['current_policies'][2050]:,.0f} in 2050) as AEO2026's do (BL-1), while the engine keeps falling.")
    md, me = ch({k: E["decided"][k]["ghgNet"] for k in E["decided"]}, 2035), ch(eps["us_climate_action"], 2035)
    add(id="PK-1", what="A package against a package: the decided set against the Energy Policy Simulator's US Climate Action pathway, change in net greenhouse gases from 2025 to 2035 (and 2050)",
        model=f"2035 {md:+.0f}%, 2050 {ch({k: E['decided'][k]['ghgNet'] for k in E['decided']}, 2050):+.0f}%", target=f"EPS: 2035 {me:+.0f}%, 2050 {ch(eps['us_climate_action'], 2050):+.0f}%",
        tol="reported (not like for like)", result="reported",
        why="The EPS package is far wider and has no carbon price: the IRA's credits restored through 2050, a clean standard of 76% in 2035 and 95% from 2040, federal and state vehicle sales standards from 2031, building electrification and efficiency standards, about 150 industrial electrification and 100 efficiency settings, a 50% low-carbon fuel standard, methane capture, land, farm and forest measures, and direct air capture and rock weathering of roughly 370 Mt a year by 2050 (SRC-5044; the run's settings file). The decided set leaves farms and forests as booked, adds no carbon removal, and its industry and building measures are fewer. The gap shows what those extra measures would have to do; it is not a test of either model.")
    ep, cp = data.eps_p2050(), eps["current_policies"]
    for bid, cid, k, what in (("EP-1", "b_eps1", "run1_price", "the price alone"), ("EP-2", "b_eps2", "run2_package", "the package")):
        mod = {y: cl[y]["ghgNet"] - E[cid][y]["ghgNet"] for y in (2030, 2035, 2040, 2050)}
        epsd = {y: cp[y] - ep[k][y] for y in mod}
        add(id=bid, what=f"Same settings, two models: the cut from {what} (Espen's EPS run {bid[-1]}, against each model's own current-policy run), Mt CO2e",
            model=", ".join(f"{y}: {mod[y]:,.0f}" for y in mod), target="EPS: " + ", ".join(f"{y}: {epsd[y]:,.0f}" for y in epsd),
            tol="reported", result="reported",
            why=f"This model's cut is {mod[2030] / epsd[2030]:.0%} of EPS's in 2030, {mod[2035] / epsd[2035]:.0%} in 2035 and {mod[2050] / epsd[2050]:.0%} in 2050: about the same size over the period, with a different shape. " + (
                "This engine cuts more at first, because its power plants switch from coal to gas as soon as the price makes coal dearer. The regional fuel price spread (HI-1) slows that switching but does not remove the gap: from 2020 to 2021, when gas prices doubled, measured coal power rose 16% while the engine's roughly doubled. Part of that was the coal shortage, which annual data cannot separate out, so the engine's first-year power response is likely still too strong; monthly or plant-level history would settle it. EPS's cut comes mostly in 2031-2035, as plants retire and new capacity is built, and then levels off, while this engine's keeps growing as the price rises 5% a year and equipment turns over. Methane and fluorinated gases are priced in both runs, as EPS's defaults do." if bid == "EP-1" else
                "The settings differ where the sliders allowed: EPS's construction subsidies start in 2026, its sales standards also cover buses, motorbikes and light trucks, its building electrification covers appliances too, and its methane capture covers coal mines and landfills; this model's standards also retire unabated coal by 2040. EPS's package cut is larger through 2040 and this model's larger by 2050, the same pattern as EP-1."))
    b, base = E["b_econ"], E["mov"]
    per = {y: 100 * (base[y]["energy"] - b[y]["energy"]) / base[y]["energy"] / b[y]["price"] for y in (2035, 2040)}
    add(id="PR-1", what="Response to a carbon price: % cut in energy CO2 per dollar a ton (economy-wide price alone, against current law with Moving America)",
        model=", ".join(f"{y}: {v:.2f}% at ${E['b_econ'][y]['price']:.0f}" for y, v in per.items()), target="EMF 37: 0.06-0.31% per dollar (SRC-5024)",
        tol="inside the range in 2035 and 2040", result="pass" if all(0.06 <= v <= 0.31 for v in per.values()) else "fail",
        why="The engine sits in the range's lower half, as its own validation found against NEMS, REGEN and E3 (SRC-0077, v2.3): it responds slowly in the first decade, so its receipts lean high and its cuts lean low. EMF 37's prices are in 2018-2020 dollars, the engine's in 2025 dollars.")
    cy = {y: (ACC["b_cbo"][y]["c1"] + ACC["b_cbo"][y]["c1p"]) * (1 - m.OFFSET) for y in range(2025, 2035)}
    cbo = sum(0.75 * cy[y] + 0.25 * cy.get(y - 1, 0.0) for y in cy)   # CBO's fiscal years (October to September); first year three quarters
    add(id="PR-2", what="Receipts on CBO's price path, 2025-2034, net of the income and payroll tax offset", model=f"${cbo:,.0f}B",
        target="CBO option 73: $919B (SRC-5036)", tol="within 25%", result="pass" if abs(cbo - 919.3) / 919.3 <= 0.25 else "fail",
        why=f"{100 * (cbo - 919.3) / 919.3:+.0f}%, about the same in every year (FY2025 ${0.75 * cy[2025]:.0f}B against CBO's $53B; FY2034 ${0.75 * cy[2034] + 0.25 * cy[2033]:.0f}B against $118B). The engine cuts emissions slowly in its first decade (PR-1, lower half of EMF 37's range), which keeps its tax base, and so its receipts, high; the legacy ledger set REV-C1's midpoint about 5% below the model for the same reason (ledger-revenue.csv, C1). CBO covers energy CO2 and some large manufacturers' other gases from 2025; the engine prices fuel CO2 and industrial process CO2 and N2O, and starts its price with no warning (CBO's estimate is static apart from the offset).")
    cr = 100 * (E["b_cr"][2035]["below2005"] - base[2035]["below2005"])
    add(id="CR-1", what="Restoring the credits alone (from 2030, stepping down): points of energy CO2 below 2005 in 2035", model=f"{cr:.1f} points",
        target="The IRA against no IRA in the 2026 review: 39-48% against 27-35% below 2005 in 2035 (SRC-4479), about 8-13 points",
        tol="reported", result="reported",
        why="Not like for like: the IRA's credits ran from 2023 with twelve years to 2035 and longer terms; these start in 2030; the household credits step down from 2035 and the power credits to 60% for projects starting 2035-37 (CLI-1A.02); and grid access, not cost, limits wind and solar building (SRC-0077, v2.4).")
    dr = E["b_cr"][2035]["retail"] - base[2035]["retail"]
    add(id="BI-1", what="Retail electricity price from restoring the credits, 2035 (cents a kWh, 2025 dollars)", model=f"{dr:+.2f}",
        target="Repealing them raised bills: Rhodium $78-192, REPEAT about $280, Energy Innovation $460 a household in 2035 (SRC-4477, SRC-4478, SRC-5020)",
        tol="reported (direction: restoring lowers prices)", result="pass (direction)" if dr <= 0 else "fail (direction)",
        why="Their figures are total household energy spending, including fuel; this is the electricity price alone.")
    lg = re.search(r"About \*\*\$([0-9.]+)T\*\*", open(os.path.join(ROOT, "legacy/index/climate-carbon-model.md"), encoding="utf-8").read())
    leg = sum(ACC["b_legacy"][y]["c1"] for y in m.WINDOW) / 1000
    add(id="BK-1", what="The legacy run reproduced: the decided legacy package through this model's driver, REV-C1 receipts FY2030-39", model=f"${leg:.3f}T",
        target=f"legacy/index/climate-carbon-model.md: ${lg.group(1)}T (SRC-0056)", tol="within 0.5% (the legacy figure is rounded)",
        result="pass" if lg and abs(leg - float(lg.group(1))) / float(lg.group(1)) <= 0.005 else "fail",
        why="Shows the engine's new options default to the old behavior and the accounts read the engine as carbon-model.py does; the drift check on the legacy outputs shows the same from the other side.")
    dec, memo = sum(ACC["decided"][y]["c1"] for y in m.WINDOW) / 1000, 1.2
    add(id="BK-2", what="Memo 1 B's arithmetic against a run: the carbon price's receipts FY2030-39 and the dividend per adult in 2035",
        model=f"${dec:.2f}T; ${ACC['decided'][2035]['per_adult']:,.0f}", target="memo 1 B (proportional estimate on the legacy model): about $1.2T; about $430 an adult",
        tol="within 10%", result="pass" if abs(dec - memo) / memo <= 0.10 and abs(ACC["decided"][2035]["per_adult"] - 430) / 430 <= 0.10 else "fail",
        why="Memo 1 scaled the legacy model's receipts by power and industry's share; this runs the narrower price, so buildings and non-road fuel respond as unpriced sectors and industry pays on its covered share.")
    hh = [g for g in (HH.get("decided") or []) if "percent" in g["name"]]   # the five fifths, lowest first (the survey's all-households column dropped)
    ok = len(hh) == 5 and hh[0]["net"] > 0 and hh[1]["net"] > 0 and hh[4]["net"] < 0
    add(id="DI-1", what="Who comes out ahead in 2035 on the carbon channel (dividend less costs, by income fifth)",
        model=", ".join(f"{g['name']} {g['net']:+,.0f}" for g in hh), target="Treasury, TPC and RFF: lower fifths ahead, top behind with a per-adult rebate (SRC-4615, SRC-5035, SRC-4620)",
        tol="bottom two fifths ahead, top fifth behind", result="pass (shape)" if ok else "fail (shape)",
        why="A shape test: the levels depend on the coverage and on the 20% that does not return as the dividend.")
    HW = {k: m.WORLD[k] for k in ("fuelSpread", "coalVom", "emCal")}
    H, H0 = history.run(HW), history.run({"fuelSpread": {"coal": 0, "gas": 0}})   # the second: the engine as it was, one national price
    SHOCK = (2021, 2022)   # coal supply shortfall: low stockpiles, rail and mine limits (SRC-5062, SRC-5063)
    for h, h0 in zip(H, H0):
        h["gap_pct_single_price"] = h0["gap_pct"]
        h["coal_supply_shock"] = h["year"] in SHOCK
    test = [h for h in H if not h["coal_supply_shock"]]
    mae = sum(abs(h["gap_pct"]) for h in test) / len(test)
    mae0 = sum(abs(h["gap_pct_single_price"]) for h in H if not h["coal_supply_shock"]) / len(test)
    worst = max(test, key=lambda h: abs(h["gap_pct"]))
    mae_all = sum(abs(h["gap_pct"]) for h in H) / len(H)
    oos = [h for h in test if h["year"] != 2025]          # 2025 is in-sample: the engine is calibrated to it
    mae_out = sum(abs(h["gap_pct"]) for h in oos) / len(oos)
    low = sum(h["gap_pct"] < 0 for h in oos)
    sp0 = data.fuel_spread()
    test_mae = sum(abs(h["gap_pct"]) for h in H if h["year"] >= 2023) / len([h for h in H if h["year"] >= 2023])
    H1 = history.run({"fuelSpread": sp0, "coalVom": 5.07, "emCal": 1.002})   # the measured spread alone, recalibrated to 2025 the same way
    mae1 = sum(abs(h["gap_pct"]) for h in H1 if h["year"] not in SHOCK) / len(test)
    add(id="HI-1", what="History run, power sector: the engine's dispatch on each year's measured fleet, generation and fuel prices, 2015-2025, against EIA's measured coal and gas power CO2 (SRC-5052 to 5057)",
        model=f"scored years: average gap {mae:.1f}% ({mae_out:.1f}% without 2025, the calibration year); largest {worst['gap_pct']:+.1f}% ({worst['year']}); all eleven years {mae_all:.1f}%; 2021 and 2022 {H[6]['gap_pct']:+.0f}% and {H[7]['gap_pct']:+.0f}%, not scored", target="EIA, Monthly Energy Review table 11.6",
        tol="average absolute gap 5% or less, and every year within 10%, outside the 2021-22 coal shortage", result="pass (2021-22 excluded)" if mae <= 5 and abs(worst["gap_pct"]) <= 10 else "fail",
        why=f"Total fossil generation is right by construction; the test is the split between coal and gas. With one national fuel price the engine switched the whole fleet at once: its average gap was {mae0:.1f}% in the scored years and {H0[6]['gap_pct']:+.0f}% in 2021. Plants pay different delivered prices by region, so the dispatch now splits each block of plants by the spread of fuel prices: EIA measures {sp0['coal']:.0%} of the average price for coal and {sp0['gas']:.0%} for gas across states, weighted by what each state's power plants buy (SRC-5058 to SRC-5061). That understates what plants act on (some states are withheld; contracts, plants that must run and differences within a state add to it), so the model uses {m.a('fuel_spread_mult'):.1f} times it, a labeled calibration: fitted to 2015-2020 and tested on 2023-2025 ({test_mae:.1f}% there), and the largest multiple that keeps coal's recalibrated running cost near the engine's sourced $4/MWh (assumptions.csv, fuel_spread_mult). With the measured spread alone the scored gap is {mae1:.1f}%. "
            f"2021 and 2022 are shown but not scored: gas prices doubled, and coal plants could not run harder because coal was short (stockpiles 37% below their five-year average in September 2021; rail and mine limits through 2022; EIA, SRC-5062 and SRC-5063). The engine has no fuel-supply limit, so it still runs too much coal in those years. Counting every year, the average gap is {mae_all:.1f}%, which would fail. "
            f"Of the {len(oos)} scored years other than 2025, {low} run low: the engine still burns too little coal and too much gas when gas is cheap, so it still switches toward gas too readily, if far less than before. A carbon price works through the same switch, so the engine's near-term power cut still leans high; EP-1 shows the same. The full-engine history run (vehicles, buildings and building decisions from 2015) is still to be built.")
    out.append({"_history": H})
    return out


def sha(path):
    return hashlib.sha256(open(path, "rb").read()).hexdigest()[:16]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=HERE)
    args = ap.parse_args()
    cfg = m.config()
    cfg["cases"] += bench_cases()
    R = m.run_engine(cfg)
    E = {cid: {r["year"]: r for r in rows} for cid, rows in R["cases"].items()}
    ACC = {cid: m.accounts(rows) for cid, rows in R["cases"].items()}
    labels = {c["id"]: c["label"] for c in cfg["cases"]}
    L, O = m.scenarios()
    layers, options = [c[0] for c in L], [c[0] for c in O] + ["cl_permit", "decided_permit"]
    B = benchmarks(E, ACC, R["households"])
    HIST = next(b["_history"] for b in B if "_history" in b)
    B = [b for b in B if "_history" not in b]
    D, cl = E["decided"], E["cl"]
    pct = lambda xs, q: sorted(xs)[min(len(xs) - 1, max(0, int(round(q * (len(xs) - 1)))))]
    mc = R["mc"]["decided"]
    band = {}
    for y in (2035, 2050):
        e = [1 - next(r for r in run if r["year"] == y)["energy"] / 5999 for run in mc]
        band[y] = (pct(e, 0.1), pct(e, 0.9))
    c1w = [sum((r["rev"]["power"] + r["rev"]["industry"] + r["rev"]["buildings"] + r["rev"]["transport"]) * m.defl(r["year"]) for r in run if 2030 <= r["year"] <= 2039) for run in mc]
    c1band = (pct(c1w, 0.1), pct(c1w, 0.9))
    # avoided emissions, valuation and temperature (decided set against current law)
    avoid = {y: cl[y]["ghgNet"] - D[y]["ghgNet"] for y in range(2030, 2051)}
    avoid_co2 = sum(cl[y]["energy"] + cl[y]["process"] - D[y]["energy"] - D[y]["process"] for y in range(2030, 2051))
    scc_val = sum(avoid[y] * interp(SCC_2020, y) for y in avoid) / 1000   # $ billion, 2020 dollars, undiscounted sum of yearly values
    # provisions for the budget model's booking step (nominal $ billion by fiscal year; a cost is positive)
    A = ACC["decided"]
    prov = {"REV-C1A": ("carbon price receipts on covered combustion (REV-C1A, C1G)", lambda y: -A[y]["c1"]),
            "REV-C1P.01": ("process-emissions receipts", lambda y: -A[y]["c1p"]),
            "REV-C2.01": ("border adjustment, net of export rebates", lambda y: -A[y]["c2"]),
            "REV-C3.01": ("methane fee", lambda y: -A[y]["c3"]),
            "CX": ("income and payroll tax offset on all four fees (24.4%)", lambda y: -A[y]["offset"]),
            "CLI-2A.04-dividend": ("Climate Dividend (80% of combustion receipts)", lambda y: A[y]["dividend"]),
            "CLI-2A.04-transition": ("transition share (20% of combustion receipts)", lambda y: A[y]["transition"]),
            "CLI-3A.02": ("clean standard's capped payments, to bill protection", lambda y: -A[y]["acp"]),
            "CLI-1A-model": ("the engine's credit cost (a cross-check on the booking, not a score)", lambda y: A[y]["credits"])}
    led = {r["id"]: r for r in csv.DictReader(open(os.path.join(ROOT, "models/data/inputs/ledger-revenue.csv"), encoding="utf-8"))}
    booked = {"REV-C1A": ("C1", -1), "REV-C1P.01": ("C1P", -1), "REV-C2.01": ("C2", -1), "REV-C3.01": ("C3", -1)}
    files = ["models/tools/energy/engine/cfd-model.js", "models/tools/energy/engine/cfd-households.js", "models/tools/carbon/cfd-cex-2024.json", "models/tools/energy/engine.js", "models/tools/energy/model.py",
             "models/tools/energy/run.py", "models/tools/energy/data.py", "models/tools/energy/assumptions.csv", "models/data/inputs/carbon-parameters.csv",
             "models/data/inputs/excise-offset.csv", "models/tools/transportation/moving_america.py", "models/data/energy/eps-us-4.0.7-runs-2026-11-13.csv",
             "models/data/energy/eps-us-4.0.7-runs-2026-11-13-p2050.csv", "models/tools/energy/history.py", "models/tools/energy/history.js"] + [os.path.relpath(os.path.join(data.TEXT, f), ROOT) for f, _ in history.SRC.values()] + ["library/text/m4-eia-mer-t11-06-power-co2.txt"] + [os.path.relpath(os.path.join(data.TEXT, f), ROOT) for pair in data.FUEL_SPREAD_SRC.values() for f in pair] + [os.path.relpath(os.path.join(data.TEXT, f), ROOT) for f, _ in data.AEO.values()]
    res = {
        "model": "MOD-energy", "status": "working",
        "run": {"inputs_sha256_16": {f: sha(os.path.join(ROOT, f)) for f in files}, "offset_rate": m.OFFSET, "inflation": m.P["inflation"],
                "mc_draws": cfg["mcDraws"], "convention": "calendar year y booked as fiscal year y; nominal $ billion; a cost is positive in provisions"},
        "scenarios": {cid: {"label": labels[cid], "years": {y: {k: round(E[cid][y][k], 4) for k in MARK} for y in (2030, 2035, 2040, 2050)},
                            "window_2030_39": {k: round(m.window(ACC[cid], k), 2) for k in ("c1", "c1p", "c2", "c3", "acp", "offset", "dividend", "transition", "credits")},
                            "fy2040": {k: round(ACC[cid][2040][k], 2) for k in ("c1", "c1p", "c2", "c3", "acp", "offset", "dividend", "transition", "credits")},
                            "per_adult": {y: round(ACC[cid][y]["per_adult"]) for y in (2030, 2035, 2040)}}
                      for cid in layers + options},
        "provisions": {pid: {"label": lab, "by_year": {y: round(f(y), 2) for y in range(2030, 2051)}, "fy2030_39": round(sum(f(y) for y in m.WINDOW), 1),
                             "fy2040": round(f(2040), 1), "booked_mid_fy2030_39": (round(1000 * float(led[booked[pid][0]]["mid"]), 1) * booked[pid][1] if pid in booked else None)}
                       for pid, (lab, f) in prov.items()},
        "households_2035": R["households"].get("decided"),
        "uncertainty": {"energy_below2005_p10_p90": {y: [round(v, 3) for v in band[y]] for y in band}, "c1_2030_39_p10_p90": [round(v, 1) for v in c1band]},
        "valuation": {"avoided_ghg_2030_2050_mt": round(sum(avoid.values())), "scc_2020usd_bn_undiscounted": round(scc_val),
                      "avoided_co2_2030_2050_gt": round(avoid_co2 / 1000, 2), "warming_avoided_c": [round(avoid_co2 / 1e6 * t, 4) for t in TCRE]},
        "weather_2025": data.weather_2025(),
        "history_power": HIST,
        "benchmarks": B,
    }
    os.makedirs(args.out, exist_ok=True)
    json.dump(res, open(os.path.join(args.out, "results.json"), "w"), indent=1, sort_keys=True)
    open(os.path.join(args.out, "results.md"), "w").write(report(res, E, ACC, layers, options, labels))
    print(f"energy: decided set {100 * D[2035]['below2005']:.0f}% / {100 * D[2050]['below2005']:.0f}% below 2005 (energy CO2, 2035 / 2050); "
          f"REV-C1 FY2030-39 ${m.window(A, 'c1') / 1000:.2f}T; benchmarks: " + ", ".join(f"{b['id']} {b['result']}" for b in B))


def report(res, E, ACC, layers, options, labels):
    L = []
    w = L.append
    S = res["scenarios"]
    pc = lambda x: f"{100 * x:.0f}%"
    w("# Energy and climate model: results\n")
    w("*Generated by `models/tools/energy/run.py` (run by `run-all.sh`); do not edit by hand. What the model is, its evidence and its limits are in `MODEL-CARD.md`. Status: **working**.*\n")
    w("Every case below is the decided clean power set built up one layer at a time against the January 2029 current law, then the options memo 1 weighed and the sensitivities. The permitting package is not assumed except in the rows that say so. Energy CO2 is against EIA's 2005 level (5,999 Mt); net greenhouse gases against EPA's (6,536 Mt).\n")
    w("## Emissions\n")
    w("| Case | Energy CO2 below 2005: 2030 / 2035 / 2040 / 2050 | Net GHG below 2005: 2035 / 2050 | Clean electricity: 2035 / 2050 |")
    w("| --- | --- | --- | --- |")
    for cid in layers + options:
        y = S[cid]["years"]
        w(f"| {S[cid]['label']} | {' / '.join(pc(y[k]['below2005']) for k in (2030, 2035, 2040, 2050))} | {pc(y[2035]['ghgBelow2005'])} / {pc(y[2050]['ghgBelow2005'])} | {pc(y[2035]['cleanShare'])} / {pc(y[2050]['cleanShare'])} |")
    u = res["uncertainty"]["energy_below2005_p10_p90"]
    w(f"\n**Uncertainty** (the carbon model's uncertain inputs, {res['run']['mc_draws']} draws, 10th-90th percentile): the decided set is {pc(u[2035][0])}-{pc(u[2035][1])} below 2005 in 2035 and {pc(u[2050][0])}-{pc(u[2050][1])} in 2050. Published models disagree by more than this for the same policy (EMF 32: 26-47% for one tax in 2030; survey.md, 2.9), so treat the band as a floor on the uncertainty.\n")
    D, cl = E["decided"], E["cl"]
    w("**By sector, the decided set** (Mt CO2; change from 2029 current law in brackets):\n")
    w("| Year | Power | Transport | Industry | Buildings | Process CO2 and N2O | Methane |")
    w("| --- | --- | --- | --- | --- | --- | --- |")
    for y in (2030, 2035, 2040, 2050):
        w(f"| {y} | " + " | ".join(f"{D[y][k]:,.0f} ({D[y][k] - cl[y][k]:+,.0f})" for k in ("power", "transport", "industry", "buildings", "process", "methane")) + " |")
    acp = res["scenarios"]["decided"]["window_2030_39"]["acp"]; acpp = res["scenarios"]["decided_permit"]["window_2030_39"]["acp"]
    w(f"\n**The clean electricity standard.** On the decided set clean power reaches {pc(D[2035]['cleanShare'])} of generation in 2035 against the 80% target, and {pc(D[2040]['cleanShare'])} in 2040 against 100%: suppliers short of credits pay the capped payment, about ${acp:,.0f} billion over FY2030-39 (${acpp:,.0f} billion with the permitting package). Grid access, not price, limits wind and solar building in the engine (SRC-0077, v2.4), so the standard works mainly as a floor and a source of bill-protection money; memo 3's figure of about $0.05 trillion was on the legacy model with the permitting package assumed and the 80% target only.")
    w("\nPoint 1's goal is 61-66% below 2005 in 2035 (net); the decided set reaches about " + pc(D[2035]["ghgBelow2005"]) + ", as section 3 of the dossier says plainly that no modeled package reaches the range.\n")
    w("## For clean power's re-review (`DEC-2026-11-13-12`; the list in #346)\n")
    X, C0 = E["decided"], E["cl"]
    acp40, acpP = ACC["decided"][2040]["acp"], res["scenarios"]["decided_permit"]["window_2030_39"]["acp"]
    w(f"1. **The 100%-by-2040 standard.** Clean power reaches {pc(X[2035]['cleanShare'])} in 2035, {pc(X[2040]['cleanShare'])} in 2040 and {pc(X[2045]['cleanShare'])} in 2045, held back by grid access, not price. Suppliers short of credits pay about ${res['scenarios']['decided']['window_2030_39']['acp']:,.0f} billion over FY2030-39 and ${acp40:,.0f} billion in FY2040 (${acpP:,.0f} billion over FY2030-39 with the permitting package). #346 carries about $110 billion and $29 billion in 2040 from the legacy model, which assumes the permitting package in every run and reaches 91% in 2040; this model does not assume the package, and with it the payments fall to the figure in brackets, below #346's; the two models also differ in grid build (here the standby builder adds lines) and in the target path (100% by 2040 here). Retail electricity in 2040 is {X[2040]['retail']:.1f} cents a kWh against {C0[2040]['retail']:.1f} under current law (2025 dollars, national average).")
    w(f"2. **Memo 1 B's narrower price.** Receipts and the dividend are in the next table: about ${S['decided']['per_adult'][2035]:,} an adult in 2035 (#346: about $439). Energy CO2 is {pc(X[2035]['below2005'])} below 2005 in 2035 and net greenhouse gases {pc(X[2035]['ghgBelow2005'])}, inside the dossier's judged 40-48%. Buildings emit {X[2035]['buildings']:,.0f} Mt in 2035 with the clean-heat standard and no price, against {E['opt_1a'][2035]['buildings']:,.0f} Mt under memo 1 A's economy-wide price.")
    w("3. **Bills by region.** Not answered: the engine is one national market. The households table below is by income; a regional split needs the household model's state codes and regional generation mixes, a later step.")
    fl = lambda r, k: (r["cap"].get(k, 0) or 0)
    w("4. **The coal and gas fleets' wind-down** (GW of capacity, and TWh generated in brackets), for the guarantee's count of covered closures:\n")
    w("| Year | Coal, current law | Coal, decided set | Gas, current law | Gas, decided set |")
    w("| --- | --- | --- | --- | --- |")
    gas = lambda r: fl(r, "cc") + fl(r, "ct") + fl(r, "ccs")
    gg = lambda r: sum((r["gen"].get(k, 0) or 0) for k in ("cc", "ct", "ccs"))
    for y in (2030, 2035, 2040, 2045):
        w(f"| {y} | {fl(C0[y], 'coal'):,.0f} ({C0[y]['gen'].get('coal', 0):,.0f}) | {fl(X[y], 'coal'):,.0f} ({X[y]['gen'].get('coal', 0):,.0f}) | {gas(C0[y]):,.0f} ({gg(C0[y]):,.0f}) | {gas(X[y]):,.0f} ({gg(X[y]):,.0f}) |")
    w(f"\n5. **The credits against the booking.** The engine counts about ${res['scenarios']['decided']['window_2030_39']['credits']:,.0f} billion over FY2030-39 (the standby builder adds about ${res['scenarios']['builder']['window_2030_39']['credits'] - res['scenarios']['homes']['window_2030_39']['credits']:,.0f} billion of it: its own program cost at half strength, which the engine counts with the credits, and the extra credited wind, solar and storage its lines connect) against the booked CLI-1 of $757 billion; a cross-check, not a score.")
    w("6. **Outside runs.** BL-3 and PK-1 in the benchmarks compare with Espen's Energy Policy Simulator runs.\n")
    w("The transition guarantee (memo 7 B, CLI-11, with tribal governments' lost revenue, DEC-2026-11-13-11) is a fiscal program the dossier prices; this model supplies the closures (item 4), not its cost.\n")
    w("## Receipts, the offset and the dividend (FY2030-39 and FY2040, nominal $ billion)\n")
    w("| Case | Carbon price (combustion) | Process | Border | Methane | Standard's payments | Offset (24.4%) | Dividend | Transition share | Dividend per adult, 2035 |")
    w("| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |")
    for cid in ("price", "border", "credits", "ces", "decided", "opt_1a", "opt_1c", "opt_1d", "decided_permit"):
        x, f = S[cid]["window_2030_39"], S[cid]["fy2040"]
        w(f"| {S[cid]['label']} | {x['c1']:,.0f} ({f['c1']:,.0f}) | {x['c1p']:,.0f} ({f['c1p']:,.0f}) | {x['c2']:,.0f} ({f['c2']:,.0f}) | {x['c3']:,.0f} ({f['c3']:,.0f}) | {x['acp']:,.0f} ({f['acp']:,.0f}) | {x['offset']:,.0f} ({f['offset']:,.0f}) | {x['dividend']:,.0f} ({f['dividend']:,.0f}) | {x['transition']:,.0f} ({f['transition']:,.0f}) | ${S[cid]['per_adult'][2035]:,} |")
    lo, hi = res["uncertainty"]["c1_2030_39_p10_p90"]
    w(f"\nFY2040 in brackets. The carbon price's receipts on the decided set: 10th-90th percentile ${lo:,.0f}-{hi:,.0f} billion over FY2030-39. The dividend is 80% of combustion receipts (CLI-2A.04); process receipts follow the O5 account (CLI-2O.01); the offset applies to all four fees, as CX and CXP book it. The standard's payments carry no offset here (a capped compliance payment, not a tax).\n")
    w("## For the budget model's booking step\n")
    w("Nominal $ billion by fiscal year, a cost positive, the decided set (`results.json`, `provisions`, has every year to 2050). The booked column is the ledger's midpoint today (`models/data/inputs/ledger-revenue.csv`); the booking step, not this model, changes the ledger.\n")
    w("| Provision | FY2030-39 | FY2040 | Booked, FY2030-39 |")
    w("| --- | --- | --- | --- |")
    for pid, p in res["provisions"].items():
        bk = f"{p['booked_mid_fy2030_39']:,.0f}" if p["booked_mid_fy2030_39"] is not None else "—"
        w(f"| {pid}: {p['label']} | {p['fy2030_39']:,.0f} | {p['fy2040']:,.0f} | {bk} |")
    w("")
    hh = res["households_2035"] or []
    if hh:
        w("## Households in 2035 (the carbon channel, against Moving America's current-law path)\n")
        w("Per household, 2025 dollars, by income fifth (BLS Consumer Expenditure Survey 2024, the carbon model's household module). Under memo 1 B homes pay no heating charge; the cost comes through electricity and goods.\n")
        w("| Fifth | Adults | Dividend | Heating | Electricity | Other goods | Net |")
        w("| --- | --- | --- | --- | --- | --- | --- |")
        for g in hh:
            w(f"| {g['name']} | {g['people'] - g['kids']:.1f} | {g['dividend']:+,.0f} | {-g['heat']:,.0f} | {-g['elec']:,.0f} | {-g['other']:,.0f} | {g['net']:+,.0f} |")
        w("")
    w("## Prices\n")
    w("| Case | Retail electricity, cents a kWh (2025 dollars): 2030 / 2035 / 2040 |")
    w("| --- | --- |")
    for cid in ("cl", "price", "credits", "ces", "decided", "opt_1a", "opt_1c"):
        w(f"| {S[cid]['label']} | " + " / ".join(f"{S[cid]['years'][y]['retail']:.1f}" for y in (2030, 2035, 2040)) + " |")
    w("\nThe engine's retail price is its 2025 average (EIA, 17.3 cents) plus the change in the power sector's average cost, passed through in full: the cost-of-service treatment of regulated utilities (survey.md, 4.1). It is a national average; regional prices differ.\n")
    v = res["valuation"]
    w("## Avoided emissions, valued, and warming\n")
    w(f"Against 2029 current law, the decided set avoids about {v['avoided_ghg_2030_2050_mt']:,} Mt CO2e over 2030-2050, {v['avoided_co2_2030_2050_gt']} Gt of it CO2. **Valuation (a labeled side table, not booked):** at EPA's 2023 social cost of carbon (2% near-term discount rate, $230 a ton in 2030 rising to $310 in 2050, 2020 dollars; SRC-5006), that is about ${v['scc_2020usd_bn_undiscounted']:,} billion of avoided damages, summed without discounting and valuing every gas at the CO2 rate. The second Trump administration's OMB directs agencies not to monetize greenhouse gas effects (M-25-27, SRC-5007) and withdrew the interagency estimates (EO 14154, SRC-4732); this table is Project 2050's labeled valuation on EPA's peer-reviewed 2023 estimates, not federal guidance. **Warming:** at IPCC's 0.45°C per 1,000 Gt CO2 (likely 0.27-0.63; SRC-5037), the avoided CO2 is about {v['warming_avoided_c'][1]:.4f}°C ({v['warming_avoided_c'][0]:.4f}-{v['warming_avoided_c'][2]:.4f}); methane's shorter-lived warming is not converted.\n")
    wt = res["weather_2025"]
    w(f"**Weather in the starting year.** NOAA's degree days (SRC-5047, SRC-5048) put 2025 at {100 * wt['heating']['ratio']:.0f}% of the 2015-2024 heating average and {100 * wt['cooling']['ratio']:.0f}% of the cooling average, so the engine's 2025 calibration needs no weather adjustment beyond a few percent of buildings CO2 (EIA's \"colder winter\" was colder than 2024's, not than normal).\n")
    w("## Benchmarks\n")
    w("| ID | Benchmark | Model | Target | Tolerance | Result |")
    w("| --- | --- | --- | --- | --- | --- |")
    for b in res["benchmarks"]:
        w(f"| {b['id']} | {b['what']} | {b['model']} | {b['target']} | {b['tol']} | **{b['result']}** |")
    w("\n**HI-1, year by year** (power-sector CO2 from coal and gas, Mt; generation, TWh):\n")
    w("| Year | Model CO2 | Measured CO2 | Gap | Gap with one national fuel price | Coal, model / measured | Gas, model / measured |")
    w("| --- | --- | --- | --- | --- | --- | --- |")
    for h in res["history_power"]:
        yr = f"{h['year']} (coal shortage, not scored)" if h["coal_supply_shock"] else str(h["year"])
        w(f"| {yr} | {h['model_co2']:,.0f} | {h['measured_co2']:,.0f} | {h['gap_pct']:+.1f}% | {h['gap_pct_single_price']:+.1f}% | {h['model_coal_twh']:,.0f} / {h['measured_coal_twh']:,.0f} | {h['model_gas_twh']:,.0f} / {h['measured_gas_twh']:,.0f} |")
    cp, ep = data.eps_runs()["current_policies"], data.eps_p2050()
    w("\n**EP-1 and EP-2, the curves** (net greenhouse gases, Mt CO2e, land use included as each model books it). Espen's EPS runs of the plan's settings (EPS 4.0.7, 2026-11-13) beside this engine's runs of the same settings; each model's cut is against its own current-policy run, since the two models start from different totals:\n")
    w("| Year | EPS current policies | EPS run 1, price | EPS run 2, package | Engine current policies | Engine, price | Engine, package | Cut, price: EPS / engine | Cut, package: EPS / engine |")
    w("| --- | --- | --- | --- | --- | --- | --- | --- | --- |")
    for y in (2030, 2035, 2040, 2045, 2050):
        c, p1, p2 = E["cl"][y]["ghgNet"], E["b_eps1"][y]["ghgNet"], E["b_eps2"][y]["ghgNet"]
        w(f"| {y} | {cp[y]:,.0f} | {ep['run1_price'][y]:,.0f} | {ep['run2_package'][y]:,.0f} | {c:,.0f} | {p1:,.0f} | {p2:,.0f} | {cp[y] - ep['run1_price'][y]:,.0f} / {c - p1:,.0f} | {cp[y] - ep['run2_package'][y]:,.0f} / {c - p2:,.0f} |")
    w("\n**Why the differences arise.**\n")
    for b in res["benchmarks"]:
        w(f"- **{b['id']}.** {b['why']}")
    w("\n## Run log\n")
    w(f"Offset rate {res['run']['offset_rate']}, inflation {res['run']['inflation']}; {res['run']['convention']}. Inputs (first 16 hex digits of each file's SHA-256):\n")
    for f, h in sorted(res["run"]["inputs_sha256_16"].items()):
        w(f"- `{f}`: `{h}`")
    return "\n".join(L) + "\n"


if __name__ == "__main__":
    main()
