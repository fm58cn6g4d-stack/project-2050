"""Clean power, memo 1 part 1 B: a read of the carbon model for the decided coverage (power plants and large industry).

Role: a dossier tool, not a booking. It runs the legacy carbon model (`models/tools/carbon/`, through its Project 2050 driver
`p2050-run.js`) on the same decided package `models/tools/carbon-model.py` runs (case `full`), and on the same package with
industrial process CO2 and N2O priced (case `proc`), and reads the fee's receipts by source, year by year, in nominal dollars.
Under memo 1 B (`dossiers/clean-power/4-specification.md`, REV-C1.01) the price is charged on power plants' and large
industrial facilities' fuel and on their process emissions; buildings and non-road transport are not charged directly.

What it is and is not:
- The model prices every covered sector at one price; it has no switch for leaving buildings and non-road transport out.
  So this is a read of the receipts the decided package's power and industry sectors pay, not a run of a narrower price.
  Leaving buildings unpriced lowers their abatement in the model, which the clean-heat standard (CLI-4H) is meant to replace;
  it barely moves power and industry's own receipts (power's load changes a little), so the read is a fair basis for the
  receipts, and says nothing about buildings' emissions.
- Nothing here changes `models/`. Inputs come from `models/data/inputs/carbon-parameters.csv` and the transportation model,
  exactly as `carbon-model.py` reads them.

Run from the repository root (needs node):  python3 dossiers/clean-power/tools/coverage_read.py [--json out.json]
"""
import json, os, subprocess, sys, tempfile

ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", ".."))
TOOLS = os.path.join(ROOT, "models", "tools")
sys.path.insert(0, TOOLS)
sys.path.insert(0, os.path.join(TOOLS, "transportation"))
from inputs import read, num  # noqa: E402
import moving_america as ma  # noqa: E402


def _val(s):
    try:
        return num(s)
    except ValueError:
        return s.strip()


P = {r["key"]: _val(r["value"]) for r in read("carbon-parameters.csv")}
YRS = range(2025, 2051)
defl = lambda y: (1 + P["inflation"]) ** (y - 2025)


def d7_nominal(y):  # the same price path as carbon-model.py
    s, p0, p37 = P["c1_start_year"], P["c1_start_price"], P["c1_price_2037"]
    slope37, k = P.get("c1_slope_2037", p37), int(P.get("c1_kink_year", 2037))
    if y < s:
        return 0.0
    early = lambda yy: p0 + (slope37 - p0) * (yy - s) / (2037 - s)
    if y <= k:
        return early(y)
    if y <= 2037:
        return early(k) + (p37 - early(k)) * (y - k) / (2037 - k)
    return p37 * (1 + P["c1_growth_after"]) ** (y - 2037)


D7_REAL = {y: d7_nominal(y) / defl(y) for y in YRS}
MOV = ma.Revenue(ma.Design(), premium=True)
ROAD_REAL = {y: max(MOV.gr(y) - 18.4, 0) / 100 / defl(y) / 0.0085 if y >= 2029 else 0.0 for y in YRS}
base_pol = {"permitYear": P["permit_year"], "startPrice": 0, "step": 0, "ratchet": False}
d7_pol = dict(base_pol, childShare=0, roadExempt=True, roadPath=ROAD_REAL, othRoad=P["oth_road"], offset=0, admin=0,
              dividendShare=P["dividend_share"],
              cover={"process": False, "methane": False, "fgas": False, "border": False, "bunkers": False}, ratchet=False)
ces = {"start": P["ces_start"], "target": P["ces_target"], "year": P["ces_year"]}


def ch4_nominal(y):
    if y < P["ch4_start"]:
        return 0.0
    return P["ch4_rate_2030"] if y == 2030 else P["ch4_rate_2031"] if y == 2031 else P["ch4_rate_2032"]


CH4_REAL = {y: ch4_nominal(y) / P["gwp100"] / defl(y) for y in YRS}
MF = {"start": P["ch4_start"], "mult": 0, "path": CH4_REAL, "ogShare": P["ch4_og_share"], "coal": bool(P["ch4_coal"]),
      "landfill": bool(P["ch4_landfill"]),
      "cert": {"s0": P["cert_s0"], "s1": P["cert_s1"], "year": P["cert_year"], "abate": P["cert_abate"]}}
full = dict(d7_pol, credits=True, ces=ces, standards=True, gridStatute=True, weatherize=True, methaneFee=MF)
CASES = [
    dict(id="full", policy=full, price=D7_REAL),
    dict(id="proc", policy=dict(full, cover=dict(d7_pol["cover"], process=True)), price=D7_REAL),
    dict(id="border", policy=dict(full, cover=dict(d7_pol["cover"], border=True)), price=D7_REAL),
]


def run():
    cfg = dict(cases=CASES, mcDraws=0, mcSeed=P["mc_seed"],
               world={"cesAcp": P["ces_acp"], "gsTx": P["grid_statute_tx"], "wxHomes": P["weatherize_homes_m"]})
    with tempfile.TemporaryDirectory() as d:
        f = os.path.join(d, "carbon-config.json")
        json.dump(cfg, open(f, "w"))
        out = subprocess.run(["node", os.path.join(TOOLS, "carbon", "p2050-run.js"), f], check=True,
                             capture_output=True, text=True).stdout
    R = json.loads(out)
    C = {k: {r["year"]: r for r in v} for k, v in R["cases"].items()}
    rows = {}
    for y in range(2030, 2051):
        r, rp, rb = C["full"][y], C["proc"][y], C["border"][y]
        nom = lambda x: x * defl(y)
        src = {k: nom(r["rev"][k]) for k in ("power", "industry", "buildings", "transport")}
        c1 = sum(src.values())
        covered = src["power"] + src["industry"]
        adults = r["pop"] * 0.77  # the model's own convention (carbon-model.py): adults are 77% of CBO's population
        rows[y] = dict(price=round(d7_nominal(y), 2), **{k: round(v, 2) for k, v in src.items()},
                       c1_package=round(c1, 2), c1_covered_B=round(covered, 2), share_B=round(covered / c1, 4),
                       process=round(nom(rp["rev"]["process"]), 2), border=round(nom(rb["rev"]["border"]), 2),
                       dividend_adult_package=round(P["dividend_share"] * c1 * 1e9 / (adults * 1e6), 0),
                       dividend_adult_B=round(P["dividend_share"] * covered * 1e9 / (adults * 1e6), 0))
    return rows


def main():
    rows = run()
    W = range(2030, 2040)
    tot = lambda k: sum(rows[y][k] for y in W)
    print("Carbon model read for memo 1 B (nominal $ billion; the decided package, case `full`)")
    print("year  price  power industry bldgs  trans  C1pkg  C1(B)  shareB  process border  div/adult pkg  B")
    for y in list(W) + [2040]:
        r = rows[y]
        print(f"{y}  {r['price']:6.1f} {r['power']:6.1f} {r['industry']:7.1f} {r['buildings']:6.1f} {r['transport']:6.1f} "
              f"{r['c1_package']:6.1f} {r['c1_covered_B']:6.1f} {r['share_B']:6.3f} {r['process']:7.1f} {r['border']:6.1f} "
              f"{r['dividend_adult_package']:7.0f} {r['dividend_adult_B']:6.0f}")
    print(f"FY2030-39 sums: package {tot('c1_package'):.1f}; power and industry {tot('c1_covered_B'):.1f} "
          f"({tot('c1_covered_B') / tot('c1_package'):.3f}); process {tot('process'):.1f}; border {tot('border'):.1f}")
    if "--json" in sys.argv:
        json.dump({str(k): v for k, v in rows.items()}, open(sys.argv[sys.argv.index("--json") + 1], "w"), indent=1)
    return rows


if __name__ == "__main__":
    main()
