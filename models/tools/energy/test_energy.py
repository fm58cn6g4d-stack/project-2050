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

# --- benchmarks the status rests on
B = {b["id"]: b for b in run.benchmarks(E, ACC, R["households"])}
for bid in ("DA-1", "DA-2", "BL-1", "PR-1", "BK-1"):
    ok(f"benchmark {bid} passes", B[bid]["result"].startswith("pass"), B[bid]["model"])

print(f"{len(fails)} FAILED: {fails}" if fails else "energy model: all passed")
sys.exit(1 if fails else 0)
