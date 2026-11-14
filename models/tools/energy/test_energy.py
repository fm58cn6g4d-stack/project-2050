"""Tests for MOD-energy: accounting identities, boundary cases, data traced to its source, the driver against the legacy one,
and the benchmarks the model's status rests on. Run from the repository root: python3 models/tools/energy/test_energy.py"""
import json, os, subprocess, sys, tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import data  # noqa: E402
import model as m  # noqa: E402
import run  # noqa: E402

fails = []


def ok(name, cond, note=""):
    print(("PASS " if cond else "FAIL ") + name + (f"  [{note}]" if note else ""))
    if not cond:
        fails.append(name)


# --- data: every hand-typed value is in the saved source text; parsed tables add up
eia = open(os.path.join(data.TEXT, data.EIA_2025_SRC[0]), encoding="utf-8").read()
for k, v in data.EIA_2025.items():
    ok(f"EIA 2025 {k} ({v:,}) is in the saved EIA text", f"{v:,}" in eia)
for case in data.AEO:
    t = data.aeo_table18(case)
    gap = max(abs(t["total"][y] - sum(t[s][y] for s in ("residential", "commercial", "industry", "transport", "power"))) for y in range(2025, 2051))
    ok(f"AEO2026 {case}: sectors add to the total every year", gap < 1.0, f"largest gap {gap:.2f} Mt")
ok("NOAA degree days parse, 1896-2026", min(data.degree_days("heating")) == 1896 and max(data.degree_days("cooling")) == 2026)

# --- one engine run for everything below
cfg = m.config()
cfg["mcDraws"] = 3
cfg["cases"] += run.bench_cases()
R = m.run_engine(cfg)
E = {c: {r["year"]: r for r in rows} for c, rows in R["cases"].items()}
ACC = {c: m.accounts(rows) for c, rows in R["cases"].items()}

# --- accounting identities
for c in ("price", "decided", "opt_1a"):
    worst = max(abs(a["dividend"] + a["transition"] - a["c1"]) for a in ACC[c].values())
    ok(f"{c}: dividend plus transition share equal combustion receipts (80/20)", worst < 1e-9)
    worst = max(abs(a["offset"] + m.OFFSET * (a["c1"] + a["c1p"] + a["c2"] + a["c3"])) for a in ACC[c].values())
    ok(f"{c}: the offset is {m.OFFSET} of the four fees", worst < 1e-9)
ok("the offset rate is the adopted one (excise-offset.csv)", abs(m.OFFSET - 0.244) < 1e-12, str(m.OFFSET))

# --- boundary cases
ok("current law raises nothing", all(abs(a[k]) < 1e-12 for a in ACC["cl"].values() for k in ("c1", "c1p", "c2", "c3", "dividend")))
ok("memo 1 C (no price) raises no carbon-price receipts", all(abs(a["c1"]) < 1e-12 for a in ACC["opt_1c"].values()))
ok("no price before 2030", all(abs(ACC["decided"][y]["c1"]) < 1e-12 for y in range(2025, 2030)))
ok("memo 1 B: homes and commercial buildings pay nothing", all(r["rev"]["buildings"] == 0 and r["feeHeat"] == 0 for r in E["decided"].values()))
ok("memo 1 A raises more than memo 1 B", m.window(ACC["opt_1a"], "c1") > m.window(ACC["decided"], "c1"))
ok("the decided set cuts emissions against current law every year from 2031",
   all(E["decided"][y]["ghgNet"] < E["cl"][y]["ghgNet"] for y in range(2031, 2051)))
ok("the methane fee's receipts stay out of the dividend", all(abs(a["dividend"] - 0.8 * a["c1"]) < 1e-9 for a in ACC["decided"].values()))
ok("industry coverage moves receipts the right way", m.window(ACC["ind_lo"], "c1") < m.window(ACC["decided"], "c1") < m.window(ACC["ind_hi"], "c1"))

# --- the driver against the carbon model's own driver, on the legacy package
with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False) as f:
    leg = next(c for c in cfg["cases"] if c["id"] == "b_legacy")
    json.dump(dict(cases=[dict(id="x", policy=leg["policy"], price=leg["price"])], world={k: v for k, v in cfg["world"].items() if k in ("cesAcp", "gsTx", "wxHomes")}, mcDraws=0, mcSeed=7), f)
old = json.loads(subprocess.run(["node", os.path.join(HERE, "..", "carbon", "p2050-run.js"), f.name], check=True, capture_output=True, text=True).stdout)["cases"]["x"]
os.unlink(f.name)
ok("engine.js and p2050-run.js agree on the legacy package", all(abs(a["energy"] - E["b_legacy"][a["year"]]["energy"]) < 1e-9 and abs(a["gross"] - E["b_legacy"][a["year"]]["gross"]) < 1e-9 for a in old))

# --- the engine copy: its own regression checks, and identical to the legacy original when no M4 option is set
r = subprocess.run(["node", os.path.join(HERE, "engine", "cfd-tests.js")], capture_output=True, text=True)
ok("the engine copy passes the carbon model's regression checks and the M4 additions", r.returncode == 0, r.stdout.strip().splitlines()[-1])
same = subprocess.run(["node", "-e", """
const A = require(process.argv[1]), B = require(process.argv[2]), w = A.world();
const pols = [{}, { permitYear: 2027 }, { permitYear: null, startPrice: 0, step: 0, ratchet: false }, { permitYear: 2027, credits: true, standards: true, grid: true, nuclear: true }];
let bad = 0; for (const p of pols) { const a = A.simulate(p, A.world()), b = B.simulate(p, B.world());
  a.forEach((r, i) => { if (r.energy !== b[i].energy || r.gross !== b[i].gross || r.retail !== b[i].retail || r.ghgNet !== b[i].ghgNet) bad++; }); }
console.log(bad);""", os.path.join(HERE, "..", "carbon", "cfd-model.js"), os.path.join(HERE, "engine", "cfd-model.js")], capture_output=True, text=True).stdout.strip()
ok("the engine copy with default options equals the legacy original, four designs, every year", same == "0", same + " rows differ")

same = subprocess.run(["node", "-e", """
const M = require(process.argv[1]); const pol = { permitYear: null, ces: { start: 2030, target: 0.8, year: 2035, target2: 1.0, year2: 2040 } };
const off = M.simulate(pol, M.world()), w = M.world(); w.retailAcp = true; const on = M.simulate(pol, w);
const y = on.findIndex(r => r.year === 2041), r = on[y];
console.log(JSON.stringify({ acp: on[y - 1].cesAcp, d: r.retail - off[y].retail }));""", os.path.join(HERE, "engine", "cfd-model.js")], capture_output=True, text=True).stdout.strip()
v = json.loads(same)
ok("the standard's capped payments reach the retail price (retailAcp; review R-2)", v["acp"] > 0 and v["d"] > 0, f"payments ${v['acp']:.0f}B in 2040, retail +{v['d']:.2f} cents in 2041")

# --- benchmarks the status rests on
B = {b["id"]: b for b in run.benchmarks(E, ACC, R["households"]) if "id" in b}
for bid in ("DA-1", "DA-2", "BL-1", "PR-1", "BK-1"):
    ok(f"benchmark {bid} passes", B[bid]["result"].startswith("pass"), B[bid]["model"])

# --- the history check (HI-1): inputs traced to the saved EIA text; it runs every year and the gap is reported, not tuned away
import history  # noqa: E402
gen, cap = history.annual(*history.SRC["gen"]), history.annual(*history.SRC["cap"])
gtxt = open(os.path.join(data.TEXT, history.SRC["gen"][0]), encoding="utf-8").read()
ctxt = open(os.path.join(data.TEXT, history.SRC["cap"][0]), encoding="utf-8").read()
ok("history: every year 2015-2025 parsed from each EIA table", all(sorted(history.annual(*v)) == list(range(2015, 2026)) for v in history.SRC.values()))
ok("history: 2024 coal generation is in the saved EIA text", f"{gen[2024][0]:,.0f}" in gtxt or f"{gen[2024][0]:,.1f}" in gtxt, f"{gen[2024][0]:,.0f} GWh")
ok("history: 2024 coal capacity is in the saved EIA text", f"{cap[2024][0]:,.1f}" in ctxt, f"{cap[2024][0]:,.0f} MW")
co2 = history.measured_co2()
ok("history: measured 2025 coal + gas power CO2 near 1,460 Mt", 1400 < sum(co2[2025]) < 1520, f"{sum(co2[2025]):,.0f} Mt")
H = run.history.run()
ok("history: runs 11 years, total fossil generation within 2% of measured each year",
   len(H) == 11 and all(abs((h["model_coal_twh"] + h["model_gas_twh"]) / (h["measured_coal_twh"] + h["measured_gas_twh"]) - 1) < 0.02 for h in H))
ok("HI-1 is computed, not pending", B["HI-1"]["result"].split(" ")[0] in ("pass", "fail"), B["HI-1"]["model"])

# --- the regional fuel price spread: traced to EIA's state tables; the 2025 calibration holds with it
sp = data.fuel_spread()
ctab = data._state_col(data.FUEL_SPREAD_SRC["coal"][0])
ok("fuel spread: Nebraska's and Virginia's 2025 coal prices read from the saved EIA table", ctab.get("Nebraska") == 1.29 and ctab.get("Virginia") == 4.54, str((ctab.get("Nebraska"), ctab.get("Virginia"))))
ok("fuel spread: coal 20-40% and gas 10-30% of the average price, and the model uses it", 0.2 <= sp["coal"] <= 0.4 and 0.1 <= sp["gas"] <= 0.3 and all(abs(m.WORLD["fuelSpread"][k] - sp[k] * m.a("fuel_spread_mult")) < 1e-3 for k in sp), str(sp))
cal = json.loads(subprocess.run(["node", "-e", """
const M = require(process.argv[1]); const w = Object.assign(M.world(), JSON.parse(process.argv[2])); const r = M.simulate({ permitYear: null }, w)[0];
console.log(JSON.stringify({ coal: r.gen.coal, power: r.power }));""", os.path.join(HERE, "engine", "cfd-model.js"),
    json.dumps({k: m.WORLD[k] for k in ("fuelSpread", "coalVom", "emCal")})], capture_output=True, text=True).stdout)
ok("2025 calibration with the spread: coal output 750 TWh and power CO2 1,485 Mt, within 0.5%", abs(cal["coal"] / 749.8 - 1) < 0.005 and abs(cal["power"] / 1484.6 - 1) < 0.005, f"{cal['coal']:.0f} TWh, {cal['power']:.0f} Mt")
ok("HI-1: the spread narrows the history gap against one national price", B["HI-1"]["result"].startswith("pass") or float(B["HI-1"]["model"].split("average gap ")[1].split("%")[0]) < 9.1, B["HI-1"]["model"])

# --- the power credits follow the decided step-down (CLI-1A.02), not the IRA's emissions trigger
step = json.loads(subprocess.run(["node", "-e", """
const M = require(process.argv[1]); const sched = JSON.parse(process.argv[2]); const pol = { permitYear: null, credits: true };
const on = M.simulate(pol, Object.assign(M.world(), { crPowSched: sched })), trig = M.simulate(pol, M.world());
const cr = rows => Object.fromEntries(rows.filter(r => r.year >= 2034 && r.year <= 2042).map(r => [r.year, r.credits]));
console.log(JSON.stringify({ on: cr(on), trig: cr(trig) }));""", os.path.join(HERE, "engine", "cfd-model.js"), json.dumps(m.WORLD["crPowSched"])], capture_output=True, text=True).stdout)
ok("power credits: the model uses CLI-1A.02's dates (full through 2034, 60% through 2037, storage through 2039)",
   m.WORLD["crPowSched"] == {"full": 2034, "part": 0.6, "partEnd": 2037, "firm": 2039}, str(m.WORLD["crPowSched"]))
ok("power credits: the decided step-down costs less in 2036-39 than the trigger rule", sum(step["on"][str(y)] for y in range(2036, 2040)) < sum(step["trig"][str(y)] for y in range(2036, 2040)),
   f"{sum(step['on'][str(y)] for y in range(2036, 2040)):.0f} vs {sum(step['trig'][str(y)] for y in range(2036, 2040)):.0f} $B")
ret = json.loads(subprocess.run(["node", "-e", """
const M = require(process.argv[1]); const w = Object.assign(M.world(), JSON.parse(process.argv[2]));
const rows = M.simulate({ permitYear: null, credits: true, ces: { start: 2030, target: 0.8, year: 2035, target2: 1.0, year2: 2040 } }, w);
console.log(JSON.stringify(rows.filter(r => r.year >= 2030).map(r => r.retail)));""", os.path.join(HERE, "engine", "cfd-model.js"),
    json.dumps({k: m.WORLD[k] for k in ("fuelSpread", "coalVom", "emCal", "crPhase", "crPowSched", "retailNetCredits", "retailAcp")})], capture_output=True, text=True).stdout)
ok("retail price moves under 0.75 cents in any one year (no credit cliff)", max(abs(b - a) for a, b in zip(ret, ret[1:])) < 0.75, f"largest step {max(abs(b - a) for a, b in zip(ret, ret[1:])):.2f}")

# --- HI-2, the monthly history run
MO = run.history.monthly({k: m.WORLD[k] for k in ("fuelSpread", "coalVom", "emCal")})
ok("HI-2: 72 months, 2019-2024, each with measured CO2 and prices", len(MO) == 72 and all(r["measured_co2"] > 0 and r["gas_coal_ratio"] > 0 for r in MO))
co2 = run.history.mer_series(run.history.MER_MONTHLY["co2"], "CLEIEUS")
ok("HI-2: January 2021 coal power CO2 read from the saved EIA text (82.018 Mt)", co2[(2021, 1)] == 82.018)
ok("HI-2 is reported and HI-1 scores every year", B["HI-2"]["result"] == "reported" and "leaving out" in B["HI-1"]["model"], B["HI-1"]["model"])

# --- carbon-capture retrofits (engine option retro): off in the plan's runs; traced inputs; the sensitivities behave
ipm = open(os.path.join(data.TEXT, "m4-epa-ipm-2023-ch6-ccs-retrofit.txt"), encoding="utf-8").read()
ok("retrofits: EPA's coal capital ($2,506/kW) and heat-rate penalty (44.25%) are in the saved IPM text", "2,506" in ipm and "44.25" in ipm)
ok("retrofits: off in the decided set's runs (scale 0) and in the legacy reproduction", m.WORLD["retro"] is None and run.LEGACY_WORLD["retro"] is None)
ok("retrofits: at the research-based limits none pays under the plan's price, so retro1 equals the decided set",
   E["retro1"][2050]["retroStarted"] == 0 and abs(E["retro1"][2050]["ghgNet"] - E["decided"][2050]["ghgNet"]) < 1e-6)
ok("retrofits: at design capture and twice the limits, gas retrofits come online by 2050 and capture CO2",
   E["retro_hi"][2050]["retroGas"] > 0 and E["retro_hi"][2050]["retroCapt"] > 0, f"{E['retro_hi'][2050]['retroGas']:.0f} GW, {E['retro_hi'][2050]['retroCapt']:.0f} Mt")
ok("retrofits: on EPS's terms the price-only run cuts more by 2035 than without them (EP-3)",
   E["b_eps1_retro"][2035]["ghgNet"] < E["b_eps1"][2035]["ghgNet"])

# --- Espen's EPS runs of the plan's settings (EP-1, EP-2)
ep = data.eps_p2050()
ok("EPS runs: both runs start at the current-policies 2025 total", ep["run1_price"][2025] == ep["run2_package"][2025] == data.eps_runs()["current_policies"][2025])
ok("EPS runs: the package cuts more than the price alone from 2030", all(ep["run2_package"][y] < ep["run1_price"][y] for y in range(2030, 2051)))
ok("EP-1 and EP-2 are reported", B["EP-1"]["result"] == B["EP-2"]["result"] == "reported")
eg = data.eps_generation()
ok("EPS generation: three runs, 2025-2050, the same 2025 total", sorted(eg) == ["current_policies", "run1_price", "run2_package"] and all(len(eg[r]) == 26 for r in eg)
   and abs(eg["run1_price"][2025]["total"] - eg["current_policies"][2025]["total"]) < 0.01)
ok("EPS generation: types add up to the total", all(abs(sum(v for k, v in eg[r][y].items() if k != "total") - eg[r][y]["total"]) < 0.05 for r in eg for y in eg[r]))
ok("EP-3 is reported", B["EP-3"]["result"] == "reported", B["EP-3"]["model"][:60])

# --- the design menu (menu.py): one-off runs start from a committed case and reproduce the named runs
import menu  # noqa: E402
mz = menu.main([], show=False)
ok("menu: no changes reproduces the decided set", mz["run"] == mz["base_run"])
m75 = menu.main(["--builder", "0.75"], show=False)["run"]
rs = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "results.json")))["scenarios"]["bld_75"]
ok("menu: --builder 0.75 reproduces the committed bld_75 run", round(m75["co2_below_2005"][2035] / 100, 3) == round(rs["years"]["2035"]["below2005"], 3)
   and abs(m75["fy2030_39_bn"]["acp"] - rs["window_2030_39"]["acp"]) < 1)

print(f"{len(fails)} FAILED: {fails}" if fails else "energy model: all passed")
sys.exit(1 if fails else 0)
