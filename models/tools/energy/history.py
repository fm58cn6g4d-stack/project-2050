"""HI-1, the history run (power sector): does the engine's dispatch reproduce measured U.S. power-sector CO2, 2015-2025?

Role: the first part of the history check planned in survey.md, section 3. Each year from 2015 to 2025 the engine's own
dispatch (engine/cfd-model.js) is given that year's measured fleet, generation and fuel prices (EIA's Electric Power Annual,
saved in library/text/) and no carbon price; its coal and gas generation and CO2 are compared with EIA's measured figures
(Monthly Energy Review, table 11.6). Wind, solar, nuclear and every other source are set to what they actually generated,
so the test is the engine's coal-to-gas switching and emission factors, not its investment rules; the full-engine history
run (vehicles, buildings and building decisions from 2015) is still to be built.
Labeled choices: fuel prices are EIA's nominal costs (not deflated: the effect on the coal-gas order is under $1/MWh);
gas capacity is split into combined cycle and combustion turbines in the engine's 2025 proportion; battery capacity is
EIA's "other energy sources" capacity, which is mostly batteries.
"""
import json, os, re, subprocess, tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
TEXT = os.path.normpath(os.path.join(HERE, "..", "..", "..", "library", "text"))
YEARS = range(2015, 2026)
SRC = {"gen": ("m4-eia-epa-table-03_01_a.txt", 15), "ren": ("m4-eia-epa-table-03_01_b.txt", 13), "cap": ("m4-eia-epa-table-04_02_a.txt", 11),
       "rcap": ("m4-eia-epa-table-04_02_b.txt", 10), "fuel": ("m4-eia-epa-table-07_04.txt", 14)}
NUM = re.compile(r"-?[\d,]+(\.\d+)?")


def annual(slug, k):
    """{year: [k values]} from an Electric Power Annual table saved one cell per line (its 'Annual Totals' block)."""
    lines = [l.strip() for l in open(os.path.join(TEXT, slug), encoding="utf-8").read().split("\n---\n", 1)[1].splitlines()]
    j = lines.index("Annual Totals") + 1 if "Annual Totals" in lines else lines.index("2015")
    out = {}
    while j < len(lines) and re.fullmatch(r"20\d\d", lines[j]) and int(lines[j]) not in out:
        out[int(lines[j])] = [float(x.replace(",", "")) if NUM.fullmatch(x) else None for x in lines[j + 1:j + 1 + k]]
        j += 1 + k
    return out


def measured_co2():
    """{year: (coal, gas)} Mt, EIA Monthly Energy Review table 11.6, electric power sector, annual (month 13)."""
    out = {}
    for line in open(os.path.join(TEXT, "m4-eia-mer-t11-06-power-co2.txt"), encoding="utf-8"):
        m = re.match(r'"(CLEIEUS|NNEIEUS)","(\d{4})13","([\d.]+)"', line)
        if m and int(m.group(2)) in YEARS:
            out.setdefault(int(m.group(2)), {})[m.group(1)] = float(m.group(3))
    return {y: (v["CLEIEUS"], v["NNEIEUS"]) for y, v in out.items()}


def inputs():
    T = {k: annual(*v) for k, v in SRC.items()}
    rows = []
    for y in YEARS:
        g, r, c, rc, f = T["gen"][y], T["ren"][y], T["cap"][y], T["rcap"][y], T["fuel"][y]
        twh = lambda v: v / 1000.0
        wind, solar = twh(r[0]), twh(g[7])
        other = twh(g[6] + (g[8] - r[0]) + g[9] + g[10] + g[1] + g[2] + g[4])   # hydro, other renewables, pumped storage, other, oil, other gas
        cc_share = 290 / (290 + 222)
        wind_gw = rc[0] / 1000                                            # table 4.2.B, MW to GW
        rows.append(dict(year=y, G=twh(g[11]), nuclear_twh=twh(g[5]),
                         S=dict(coal=c[0] / 1000, cc=c[2] / 1000 * cc_share, ct=c[2] / 1000 * (1 - cc_share), stor=max(0.1, c[8] / 1000),
                                wind=wind_gw, solar=c[6] / 1000 - wind_gw,
                                windE=wind, solE=solar),
                         world=dict(hydroOther=other, coalPower=f[7], gasPower=f[11])))
    return rows


def run(over=None):
    """over: world settings to apply in every year (the energy model passes its fuel spread and 2025 calibration)."""
    rows = inputs()
    with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False) as fh:
        for r in rows:
            r["world"].update(over or {})
            r["S"]["nuc"] = r.pop("nuclear_twh") / (0.92 * 8.76)        # the engine's nuclear capacity factor, so its nuclear output is the measured one
        json.dump(rows, fh)
    try:
        out = json.loads(subprocess.run(["node", os.path.join(HERE, "history.js"), fh.name], check=True, capture_output=True, text=True).stdout)
    finally:
        os.unlink(fh.name)
    meas = measured_co2()
    gen = annual(*SRC["gen"])
    res = []
    for o in out:
        y = o["year"]
        mc, mg = meas[y]
        res.append(dict(year=y, model_co2=round(o["co2"], 1), measured_co2=round(mc + mg, 1), gap_pct=round(100 * (o["co2"] - mc - mg) / (mc + mg), 2),
                        model_coal_twh=round(o["coal"], 1), measured_coal_twh=round(gen[y][0] / 1000, 1),
                        model_gas_twh=round(o["gas"], 1), measured_gas_twh=round(gen[y][3] / 1000, 1)))
    return res


if __name__ == "__main__":
    for r in run():
        print(r)
