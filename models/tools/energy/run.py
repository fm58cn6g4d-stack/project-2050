"""MOD-energy, one command: runs every scenario, the benchmarks and the accounts, and writes results.json and results.md.

Usage (from the repository root):  python3 models/tools/energy/run.py [--out DIR]
DIR defaults to models/tools/energy/; run-all.sh writes to build/energy/ and compares with the committed copies.
Outputs carry no dates: the run log is the hashes of every input, so the same inputs give the same files.
"""
import argparse, csv, hashlib, json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import data  # noqa: E402
import model as m  # noqa: E402

ROOT = data.ROOT
MARK = ("energy", "below2005", "ghgBelow2005", "cleanShare", "power", "transport", "industry", "buildings", "process", "methane", "retail", "evShare", "hp")
SCC_2020 = {2030: 230, 2040: 270, 2050: 310}   # EPA 2023 (SRC-5006), SC-CO2 at a 2% near-term rate, 2020 dollars per ton
TCRE = (0.27, 0.45, 0.63)                      # IPCC AR6 WG1 SPM D.1.1 (SRC-5037), deg C per 1,000 Gt CO2


LEGACY_WORLD = {"crYears": 10, "crVehYears": None, "retailNetCredits": False}   # undo this model's world settings: carbon-model.py runs the defaults


def bench_cases():
    """Extra engine runs the benchmarks need (none is a policy Project 2050 proposes)."""
    mov = m.scenarios()[0][1][2]
    econ = dict(mov, cover=dict(m.COVER_NONE, process=True), sectorPrice={"buildings": 1, "industry": 1, "nonroad": 1}, offset=0, admin=0, ratchet=False)
    cbo = dict(m.NO_FEE, permitYear=None, cover=dict(m.COVER_NONE, process=True), offset=0, admin=0, ratchet=False)
    P = m.P
    legacy = dict(m.NO_FEE, permitYear=P["permit_year"], childShare=0, roadExempt=True, roadPath=m.ROAD, othRoad=P["oth_road"], offset=0, admin=0,
                  dividendShare=P["dividend_share"], cover=dict(m.COVER_NONE), ratchet=False, credits=True,
                  ces={"start": P["ces_start"], "target": P["ces_target"], "year": P["ces_year"]}, standards=True, gridStatute=True, weatherize=True, methaneFee=m.METHANE_FEE)
    cbo_path = {y: (25 * 1.05 ** (y - 2025) if y >= 2025 else 0.0) / 1.0 for y in m.YRS}   # CBO option 73: $25 in 2025 rising 5% a year above inflation
    return [dict(id="b_econ", label="Benchmark run: economy-wide price on the decided path, nothing else", policy=econ, price=m.PRICE),
            dict(id="b_cbo", label="Benchmark run: CBO's option ($25 a ton from 2025, +5% a year real, all fuels)", policy=cbo, price=cbo_path),
            dict(id="b_cr", label="Benchmark run: the credits alone, no price", policy=dict(mov, credits=True), price=None),
            dict(id="b_legacy", label="Benchmark run: the legacy decided package as carbon-model.py runs it", policy=legacy, price=m.PRICE, world=LEGACY_WORLD)]


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
        why="Not like for like: the IRA's credits ran from 2023 with twelve years to 2035 and longer terms; these start in 2030 and step down from 2033. The engine's power credits stop at its trigger, and grid access, not cost, limits wind and solar building (SRC-0077, v2.4).")
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
    add(id="HI-1", what="History run (engine started from 2015 and run to 2025 against EIA's measured CO2)", model="not built", target="EIA 2015-2025",
        tol="—", result="pending", why="The engine starts in 2025; a 2015 start needs that year's fleet, prices and policies. Planned (survey.md, section 3).")
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
    files = ["models/tools/carbon/cfd-model.js", "models/tools/carbon/cfd-households.js", "models/tools/energy/engine.js", "models/tools/energy/model.py",
             "models/tools/energy/run.py", "models/tools/energy/data.py", "models/tools/energy/assumptions.csv", "models/data/inputs/carbon-parameters.csv",
             "models/data/inputs/excise-offset.csv", "models/tools/transportation/moving_america.py"] + [os.path.relpath(os.path.join(data.TEXT, f), ROOT) for f, _ in data.AEO.values()]
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
