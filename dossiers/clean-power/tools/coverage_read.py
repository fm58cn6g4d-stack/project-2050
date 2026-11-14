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
    dict(id="mov", policy=dict(base_pol, roadExempt=True, roadPath=ROAD_REAL), price=None),
    dict(id="full", policy=full, price=D7_REAL, households=2035, householdsBase="mov"),
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
    run.households = R["households"].get("full")
    run.share_2035 = rows[2035]["share_B"]
    return rows


def households_B():
    """2035, 2025 dollars, by CEX quintile: the model's household module on the full package, and memo 1 B's version of it.
    Under B no heating fuel is charged; the electricity cost (the retail price change) is kept; the cost passed through
    everything else is the B receipts per household less electricity, spread as the module spreads it; the dividend scales
    with the receipts. Project arithmetic on the module's own output."""
    if not hasattr(run, "households"):
        run()
    hh, s = run.households, run.share_2035
    allg = hh[0]
    total = allg["heat"] + allg["elec"] + allg["other"]          # the module's net receipts per household (gasoline is zero)
    other_b = max(0.0, s * total - allg["elec"]) / allg["other"]
    out = []
    for g in hh:
        adults = g["people"] - g["kids"]
        div_b = g["dividend"] * s
        out.append(dict(name=g["name"], adults=round(adults, 1), dividend=round(g["dividend"]), heat=round(g["heat"]),
                        elec=round(g["elec"]), other=round(g["other"]), net=round(g["net"]),
                        dividend_B=round(div_b), other_B=round(g["other"] * other_b),
                        net_B=round(div_b - g["elec"] - g["other"] * other_b)))
    return out


def standard_payments():
    """The clean electricity standard's alternative compliance payments (CLI-3A.02), $ billion nominal, by year.
    Runs the carbon model twice on the decided package: `full` holds the standard at 80% after 2035 (the legacy CLI-3A, whose
    payments are the $0.05T the dossier first carried [EV-CLP-723]); `ces100` is the decided path, a straight line to 80% in
    2035 and on to 100% in 2040 (memo 3 part 1 B, DEC-2026-11-13-06). The model's credit price sits at the $40 cap (2025
    dollars) whenever the target is missed, so suppliers pay the cap on every missing megawatt-hour. The model prices every
    sector (it cannot leave buildings unpriced); the clean share is grid-limited, not price-limited, so memo 1 B barely moves
    it. Project arithmetic on the model's own output, milestone review O-1."""
    ces2 = dict(ces, target2=1.0, year2=2040)
    cases = [dict(id="full", policy=full, price=D7_REAL), dict(id="ces100", policy=dict(full, ces=ces2), price=D7_REAL)]
    cfg = dict(cases=cases, mcDraws=0, mcSeed=P["mc_seed"],
               world={"cesAcp": P["ces_acp"], "gsTx": P["grid_statute_tx"], "wxHomes": P["weatherize_homes_m"]})
    with tempfile.TemporaryDirectory() as d:
        f = os.path.join(d, "carbon-config.json")
        json.dump(cfg, open(f, "w"))
        out = subprocess.run(["node", os.path.join(TOOLS, "carbon", "p2050-run.js"), f], check=True,
                             capture_output=True, text=True).stdout
    R = json.loads(out)
    rows = {}
    for r80, r100 in zip(R["cases"]["full"], R["cases"]["ces100"]):
        y = r80["year"]
        if 2030 <= y <= 2050:
            rows[y] = dict(clean_80=round(r80["cleanShare"], 3), clean_100=round(r100["cleanShare"], 3),
                           acp_80=round(r80.get("cesAcp", 0) * defl(y), 2), acp_100=round(r100.get("cesAcp", 0) * defl(y), 2))
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
    print("\nHouseholds, 2035, 2025 dollars (package, then memo 1 B): dividend, heating, electricity, other, net")
    for g in households_B():
        print(f"{g['name']:22s} {g['dividend']:6d} {-g['heat']:6d} {-g['elec']:6d} {-g['other']:7d} {g['net']:+6d}   |  "
              f"B: {g['dividend_B']:5d}      0 {-g['elec']:6d} {-g['other_B']:7d} {g['net_B']:+6d}")
    sp = standard_payments()
    print("\nThe standard's payments, $ billion nominal (80% held after 2035, then the decided 100% by 2040)")
    for y in list(W) + [2040, 2045, 2050]:
        r = sp[y]
        print(f"{y}  clean {r['clean_80']:.3f} {r['clean_100']:.3f}  payments {r['acp_80']:6.2f} {r['acp_100']:6.2f}")
    print(f"FY2030-39 sums: 80% held {sum(sp[y]['acp_80'] for y in W):.1f}; decided path {sum(sp[y]['acp_100'] for y in W):.1f}")
    if "--json" in sys.argv:
        json.dump({str(k): v for k, v in rows.items()}, open(sys.argv[sys.argv.index("--json") + 1], "w"), indent=1)
    return rows


if __name__ == "__main__":
    main()
