"""Year-by-year extension of incidence v1.4: spreads each ten-year total over 2030-39 by a phase-in profile."""
from incidence import ROWS, OPTIONS, dist, HH, GROUPS
YRS = list(range(2030, 2040))
def norm(v): s = sum(v); return [x / s for x in v]
grow = [1.04 ** i for i in range(10)]
def ramp(levels): return norm([l * g for l, g in zip(levels, grow)])
P = {
 "flat": ramp([1] * 10),
 "F2": ramp([.4, .5, .9, 1, 1, 1, 1, 1, 1, 1]),
 "H3": ramp([0, .5, 1, 1, 1, 1, 1, 1, 1, 1]),
 "H2": ramp([.3, .7, .8, 1, 1, 1, 1, 1, 1, 1]),
 "PB": ramp([.3, .7, .8, 1, 1, 1, 1, 1, 1, 1]),
 "F3": ramp([0, 1, 1, 1, 1, 1, 1, 1, 1, 1]),
 "MR": ramp([.2, .3, .4, .5, .6, .7, .8, .9, 1, 1]),
 "F5": ramp([.2, .4, .5, .6, .7, .8, .85, .9, .95, 1]),
 "G11": ramp([1.6, 1.6, 1.4, 1.2, 1, .8, .7, .7, .7, .7]),
 "H5p": ramp([0, .3, .6, .8, 1, 1, 1, 1, 1, 1]),
 "C5": ramp([0, 0, 0, 1, 1, 1, 1, 1, 1, 1]),
 "LAB9": ramp([.2, .4, .6, .8, 1, 1, 1, 1, 1, 1]),   # national service ramps to 250,000 new slots by 2034
 "PS1": ramp([0, 1, 1, 1, 1, 1, 1, 1, 1, 1]),         # SAF-10 rides R3 (summer 2030); receipts from 2031
 "EDU3": ramp([.35, 1, 1, 1, 1, 1, 1, 1, 1, 1]),      # universal meals from the 2030-31 school year (v1.3)
 "EDU4": ramp([1.4, 1.4, 1.4, 1.2, 1, .8, .5, .4, .4, .4]),  # pipeline surge front-loaded, tapering after 2034 (v1.3)
 "EDU": ramp([.5, .7, .8, .9, 1, 1, 1, 1, 1, 1]),     # IDEA glide path and Pell ramp (v1.3)
 "EDUB": ramp([.1, .4, .8, 1, 1, 1, 1, 1, 1, 1]),     # EDU-9B's added benefits ramp with pre-K (v1.3)
 # v1.4: carbon fee on the durability path, price $25-110 x an emissions index falling ~4%/yr (estimate);
 # the dividend and transition share follow the fee
 "C1": norm([25, 34.6, 42.3, 50.2, 57.8, 64.8, 69.4, 75.0, 75.6, 75.9]),
}
P["E2d"] = P["C1"]; P["E2t"] = P["C1"]
def series(opts):
    rows = list(ROWS) + [(o, l, s, a, p, "") for o, (s, a, p, l) in OPTIONS.items() if o in opts]
    out = {y: {g: 0.0 for g in GROUPS} for y in YRS}
    for rid, label, side, amt, parts, _ in rows:
        d = dist(parts); w = P.get(rid, P["flat"]); sign = 1 if side == "benefit" else -1
        for i, y in enumerate(YRS):
            for g in GROUPS: out[y][g] += sign * d[g] * w[i]
    return {y: {g: round(v * 1e12 / (HH * 0.2)) for g, v in out[y].items()} for y in YRS}
if __name__ == "__main__":
    for name, o in [("B", ["C18", "C19", "C20", "C5"]), ("D", ["C18", "C19b", "C20", "C5"]), ("G", ["C18", "C5", "EDUP", "EDUB", "C35"])]:
        s = series(o); print(name)
        for y in YRS: print(" ", y, [s[y][g] for g in GROUPS[:4]])
