"""MOD-energy: clean power's decided set on the energy and climate model, scenario by scenario, with its accounts.

Role: the policy and accounting layer of the energy and climate model (survey.md, section 4). It builds the scenarios,
runs the engine (Espen's carbon model, through engine.js) and turns its rows into receipts, the offset, the dividend,
credits, prices and emissions by year. Inputs: the adopted carbon parameters (models/data/inputs/carbon-parameters.csv,
read unchanged), the transportation model's fuel steps, the adopted offset rate (excise-offset.csv) and this model's own
labeled assumptions (assumptions.csv). Money: the engine works in 2025 dollars; accounts are nominal $ billion at the
carbon parameters' inflation rate, calendar year y booked as fiscal year y (the ledger's convention for these rows).
"""
import csv, json, os, subprocess, sys, tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
TOOLS = os.path.normpath(os.path.join(HERE, ".."))
sys.path.insert(0, TOOLS)
sys.path.insert(0, os.path.join(TOOLS, "transportation"))
from inputs import read, num, offset_rate  # noqa: E402
import moving_america as ma  # noqa: E402
import data  # noqa: E402

YRS = range(2025, 2051)
WINDOW = range(2030, 2040)


def _val(s):
    try:
        return num(s)
    except ValueError:
        return s.strip()


P = {r["key"]: _val(r["value"]) for r in read("carbon-parameters.csv")}            # adopted (tier 3)
A = {r["key"]: dict(value=float(r["value"]), low=float(r["low"]), high=float(r["high"]), basis=r["basis"])
     for r in csv.DictReader(open(os.path.join(HERE, "assumptions.csv"), encoding="utf-8"))}
a = lambda k: A[k]["value"]
OFFSET = offset_rate(2030)
defl = lambda y: (1 + P["inflation"]) ** (y - 2025)


def price_nominal(y):
    """REV-C1A.01: $25 in 2030, D7's equal steps to the 2032 kink, equal steps to $150 in 2037, then 5% a year (nominal)."""
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


PRICE = {y: price_nominal(y) / defl(y) for y in YRS}                                # 2025 dollars, as the engine reads it
_MOV = ma.Revenue(ma.Design(), premium=True)
ROAD = {y: max(_MOV.gr(y) - 18.4, 0) / 100 / defl(y) / 0.0085 if y >= 2029 else 0.0 for y in YRS}  # Moving America's fuel steps, $/t


def _ch4_nominal(y):
    if y < P["ch4_start"]:
        return 0.0
    return P["ch4_rate_2030"] if y == 2030 else P["ch4_rate_2031"] if y == 2031 else P["ch4_rate_2032"]


CH4 = {y: _ch4_nominal(y) / P["gwp100"] / defl(y) for y in YRS}
METHANE_FEE = {"start": P["ch4_start"], "mult": 0, "path": CH4, "ogShare": P["ch4_og_share"], "coal": bool(P["ch4_coal"]),
               "landfill": bool(P["ch4_landfill"]),
               "cert": {"s0": P["cert_s0"], "s1": P["cert_s1"], "year": P["cert_year"], "abate": P["cert_abate"]}}
NO_FEE = {"startPrice": 0, "step": 0, "ratchet": False}
COVER_NONE = {"process": False, "methane": False, "fgas": False, "border": False, "bunkers": False}
MEMO1B = {"buildings": 0, "industry": a("ind_cover"), "nonroad": 0}                # REV-C1G.01-.02
CES = {"start": P["ces_start"], "target": P["ces_target"], "year": P["ces_year"], "target2": a("ces_target2"), "year2": int(a("ces_year2"))}
HEAT = {"start": int(a("heat_std_start")), "share": a("heat_std_share"), "step": a("heat_std_step")}
WORLD = {"cesAcp": P["ces_acp"], "gsTx": P["grid_statute_tx"], "wxHomes": P["weatherize_homes_m"],
         "crYears": int(a("credit_years")), "crVehYears": int(a("vehicle_credit_years")), "retailNetCredits": True, "retailAcp": True,
         "gpTx": 0.8 * a("grid_standby_scale"), "gpRecon": 15 * a("grid_standby_scale"), "gpCurt": 0.05 * a("grid_standby_scale"), "gpCost": 12 * a("grid_standby_scale"),  # the standby builder: the engine's grid program, scaled
         "fuelSpread": {k: round(v * a("fuel_spread_mult"), 4) for k, v in data.fuel_spread().items()},  # regional and plant fuel prices (HI-1): plants switch between coal and gas gradually
         # recalibrated with the spread to the engine's own 2025 targets (EIA coal output 750 TWh, power CO2 1,485 Mt): coal's running cost
         # $3.59/MWh (engine default 4) and the emissions calibration 0.986 (engine default 1.024). test_energy.py checks both targets.
         "coalVom": 3.59, "emCal": 0.986,
         "crPhase": True,  # without a schedule, the power credits phase out over three years after the trigger, as the IRA provides
         "crPowSched": {"full": int(a("power_credit_full_through")), "part": a("power_credit_part"), "partEnd": int(a("power_credit_part_through")),
                        "firm": int(a("storage_credit_full_through"))}}  # the decided step-down (CLI-1A.02), not the IRA's emissions trigger


def scenarios(permit=None):
    """The layers of the decided set, each adding to the one before, then the options memo 1 weighed and sensitivities."""
    base = dict(NO_FEE, permitYear=permit)
    mov = dict(base, roadExempt=True, roadPath=ROAD, othRoad=P["oth_road"])
    fee = dict(mov, startPrice=0, roadExempt=True, cover=dict(COVER_NONE, process=True), sectorPrice=MEMO1B,
               offset=0, admin=0, dividendShare=P["dividend_share"], childShare=0, ratchet=False)
    L = [("cl", "2029 current law (no new policy)", base, None),
         ("mov", "+ Moving America's fuel steps (MOV-29; road fuels priced by the gallon)", mov, None),
         ("price", "+ the carbon price on power plants and large industry, with process emissions (memo 1 B; REV-C1A, C1G, C1P)", fee, PRICE),
         ("border", "+ the border adjustment (REV-C2)", dict(fee, cover=dict(fee["cover"], border=True)), PRICE)]
    prev = L[-1][2]
    for cid, label, add in [("credits", "+ the credits, stepping down (memo 2 B; CLI-1A)", {"credits": True}),
                            ("ces", "+ the clean electricity standard, 80% by 2035 and 100% by 2040 (memo 3 B; CLI-3A)", {"ces": CES}),
                            ("std", "+ vehicle and power plant standards in statute (memo 3 part 2 A; CLI-4A, 4E)", {"standards": True}),
                            ("heat", "+ the clean-heat standard from 2032 (point 9; CLI-4H)", {"heatStd": HEAT}),
                            ("homes", "+ Weatherization heat pumps and the grid statute (CLI-5W, CLI-6)", {"weatherize": True, "gridStatute": True}),
                            ("builder", "+ public power as standby builder of last resort (memo 4 B, DEC-2026-11-13-10; CLI-10.03), the engine's grid program at half strength", {"grid": True}),
                            ("decided", "+ the methane fee (point 3; REV-C3): **the decided set**", {"methaneFee": METHANE_FEE})]:
        prev = dict(prev, **add)
        L.append((cid, label, prev, PRICE))
    decided = prev
    opts = [("opt_1a", "Option: memo 1 A, the economy-wide fee (buildings and non-road fuel priced; industry in full)",
             dict(decided, sectorPrice={"buildings": 1, "industry": 1, "nonroad": 1}), PRICE),
            ("opt_1c", "Option: memo 1 C, no carbon price (credits, standards and the methane fee only)", dict(decided), None),
            ("opt_1d", "Option: memo 1 D, the economy-wide fee from 2032",
             dict(decided, sectorPrice={"buildings": 1, "industry": 1, "nonroad": 1}), {y: (PRICE[y] if y >= 2032 else 0.0) for y in YRS}),
            ("nofee33", "Durability: the decided set with the price repealed from 2033", dict(decided), {y: (PRICE[y] if y < 2033 else 0.0) for y in YRS}),
            ("ind_lo", f"Sensitivity: industry coverage {A['ind_cover']['low']:.0%}", dict(decided, sectorPrice=dict(MEMO1B, industry=A["ind_cover"]["low"])), PRICE),
            ("ind_hi", f"Sensitivity: industry coverage {A['ind_cover']['high']:.0%}", dict(decided, sectorPrice=dict(MEMO1B, industry=A["ind_cover"]["high"])), PRICE),
            ("bld_lo", f"Sensitivity: the standby builder at {A['grid_standby_scale']['low']:.0%} of a full grid program", dict(decided, gridScale=A["grid_standby_scale"]["low"]), PRICE),
            ("bld_hi", "Sensitivity: a builder everywhere (memo 4 option A: the full grid program)", dict(decided, gridScale=A["grid_standby_scale"]["high"]), PRICE)]
    return L, opts


def config():
    L, O = scenarios()
    def case(c, l, p, pr):
        p = dict(p)
        k = p.pop("gridScale", None)
        out = dict(id=c, label=l, policy=p, price=pr)
        if k is not None:
            out["world"] = {"gpTx": 0.8 * k, "gpRecon": 15 * k, "gpCurt": 0.05 * k, "gpCost": 12 * k}
        return out
    cases = [case(*x) for x in L + O]
    LP, _ = scenarios(permit=int(a("permit_year_sensitivity")))
    cases += [dict(id="cl_permit", label="Sensitivity: 2029 current law with the 2026-28 permitting package enacted", policy=LP[0][2], price=None),
              dict(id="decided_permit", label="Sensitivity: the decided set with the permitting package", policy=LP[-1][2], price=PRICE)]
    for c in cases:
        if c["id"] == "decided":
            c["mc"] = True
            c["households"] = {"year": 2035, "base": "mov"}
    return dict(cases=cases, mcDraws=int(a("mc_draws")), mcSeed=int(P["mc_seed"]), world=WORLD)


def run_engine(cfg):
    with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False) as f:
        json.dump(cfg, f)
    try:
        out = subprocess.run(["node", os.path.join(HERE, "engine.js"), f.name], check=True, capture_output=True, text=True).stdout
    finally:
        os.unlink(f.name)
    return json.loads(out)


def accounts(rows):
    """Nominal $ billion by year, from one case's engine rows (2025 dollars, $bn)."""
    out = {}
    for r in rows:
        y, d, rv = r["year"], defl(r["year"]), r["rev"]
        c1 = (rv["power"] + rv["industry"] + rv["buildings"] + rv["transport"]) * d
        c1p, c2, c3, acp = rv["process"] * d, rv["border"] * d, rv["methane"] * d, r["cesAcp"] * d
        adults = a("adult_share") * r["pop"]
        out[y] = dict(c1=c1, c1p=c1p, c2=c2, c3=c3, acp=acp, offset=-OFFSET * (c1 + c1p + c2 + c3),
                      dividend=P["dividend_share"] * c1, transition=(1 - P["dividend_share"]) * c1,
                      per_adult=P["dividend_share"] * c1 * 1e9 / (adults * 1e6) if adults else 0.0,
                      credits=r["credits"] * d, price=r["price"] * d)
    return out


def window(acc, key, yrs=WINDOW):
    return sum(acc[y][key] for y in yrs)
