"""Year-by-year extension of incidence v1.4: spreads each ten-year total over 2030-39 by a phase-in profile."""
from incidence import ROWS, OPTIONS, dist, HH, GROUPS
from inputs import read, num
YRS = list(range(2030, 2040))
def norm(v): s = sum(v); return [x / s for x in v]
grow = [1.04 ** i for i in range(10)]
def ramp(levels): return norm([l * g for l, g in zip(levels, grow)])
# Phase-in profiles, models/data/inputs/incidence-phase-in.csv: "ramp" levels grow 4% a year and are normalised;
# "norm" levels are normalised as typed; same_as borrows another row's profile.
P = {}
for r in read("incidence-phase-in.csv"):
    if r["same_as"]: P[r["id"]] = P[r["same_as"]]; continue
    lv = [num(r[f"y{y}"]) for y in YRS]
    P[r["id"]] = ramp(lv) if r["method"] == "ramp" else norm(lv)
def series(opts):
    rows = list(ROWS) + [(o, l, s, a, p, "") for o, (s, a, p, l) in OPTIONS.items() if o in opts]
    out = {y: {g: 0.0 for g in GROUPS} for y in YRS}
    for rid, label, side, amt, parts, _ in rows:
        d = dist(parts); w = P.get(rid, P["flat"]); sign = 1 if side == "benefit" else -1
        for i, y in enumerate(YRS):
            for g in GROUPS: out[y][g] += sign * d[g] * w[i]
    return {y: {g: round(v * 1e12 / (HH * 0.2)) for g, v in out[y].items()} for y in YRS}
if __name__ == "__main__":
    from incidence import QO, QEDU
    for name, o in [("Q", QO), ("Q-EDU", QEDU)]:
        s = series(o); print(name)
        for y in YRS: print(" ", y, [s[y][g] for g in GROUPS[:4]])
