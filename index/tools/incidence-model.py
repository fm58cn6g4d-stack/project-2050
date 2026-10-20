"""D3 household net test (v1.3, Oct 20, 2026: education batch on top of the full ledger rebuild).

Distributes every household-facing instrument in the ledger by income quintile, with the
top 1% split out of the top quintile. Units: ten-year totals for 2030-39 in $T, converted to
average dollars per household per year. Shares are estimates anchored to the published
patterns cited in the doc; every row says which pattern it uses.

v1.2 changes (ledger rebuild, Oct 20): housing restated to HOU-1's $0.47T (was E6, $0.60T);
the public-safety package restated to its durable sources (PS1, $0.09T: deployment savings and
Crime Victims Fund receipts are not household taxes); LAB-8 apprenticeships and LAB-9 national
service added as benefits. Row IDs keep their v1 names where unchanged.

v1.3 changes (education batch, Oct 20 evening): F4 becomes EDU (EDU-1 and EDU-5, same $0.65T);
EDU-3 universal meals ($0.27T, new `meals` key), EDU-4 educator pipeline ($0.03T) and EDU-7
(repeal of the scholarship tax credit, a $0.04T cost on donors, new `donors` key) added.
New options: C35 (estate tax at 2009 parameters, new `estate` key), C36 (meals at community-
eligibility scale), and the EDU-9B education fund (EDUP contribution, EDUB new benefits).
Scenario G tests EDU-9B as the closer in place of C19 and C20.
Scenario P (Oct 20, Decision Brief 1) is the planning basis: Package B plus the top-end sprint package C38.

v1.4 changes (Espen's decisions later on Oct 20): the carbon fee moves to the durability path
($25 rising to ~$100 by 2037; C1 $1.35T, dividend $1.08T, transition share $0.27T); C35 is
restated as the increment beyond G9 ($0.15T). The ten-year totals hide one gain: the new path's
lower early price makes 2030-32 better for every quintile than the old path (see the years model).
"""
import json, re
from inputs import read, num

HH = 140e6          # households, mid-window (estimate: ~132M in 2023 grown ~0.8%/yr)
GROUPS = ["Q1", "Q2", "Q3", "Q4", "Q5"]
INC = {"Q1": 23e3, "Q2": 60e3, "Q3": 105e3, "Q4": 180e3, "Q5": 520e3, "T1": 4.3e6, "Q5x": 0}  # 2034 avg expanded cash income, estimate

# The tables are in index/data/inputs/: incidence-keys.csv (distribution keys) and incidence-rows.csv (the package
# rows and the options). A row's amount is a number or a formula over ledger IDs, e.g. [G1] or [EDU-1]+[EDU-5],
# read from ledger.json, so a ledger change flows through. Parts split the amount (x) across keys.
# Distribution keys: shares of the total for Q1..Q5, and the top 1%'s share of the total (inside Q5).
K = {r["key"]: ([num(r[q]) for q in ("q1", "q2", "q3", "q4", "q5")], num(r["top1"])) for r in read("incidence-keys.csv")}

def _ledger():
    try:
        L = json.load(open("ledger.json"))
    except FileNotFoundError:
        raise SystemExit("incidence: ledger.json not found; run ledger-build.py first (run-all.sh does)")
    v = {b["id"]: b["cost_mid"] for b in L["bills"]}
    v.update({r["id"]: r["mid"] for r in L["revenue"]}); v.update({c["id"]: c["saves_tn"] for c in L["cuts"]})
    return v
LEDGER = _ledger()

def amount(f):
    """A number, or a formula over ledger IDs in brackets: [G1], [O2]+[OX], -0.3*[HLT-6]."""
    expr = re.sub(r"\[([^\]]+)\]", lambda m: repr(LEDGER[m.group(1)]), f)
    return round(eval(expr, {"__builtins__": {}}), 10)

def parts(spec, x):
    """'key' (the whole amount) or 'key expr; key expr', where expr may use x, the row's amount."""
    out = []
    for p in spec.split(";"):
        k, _, e = p.strip().partition(" ")
        out.append((k, eval(e, {"__builtins__": {}}, {"x": x}) if e else x))
    return out

ROWS, OPTIONS = [], {}
for r in read("incidence-rows.csv"):
    amt = amount(r["amount"]); ps = parts(r["parts"], amt)
    if r["set"] == "package": ROWS.append((r["id"], r["label"], r["side"], amt, ps, r["basis"]))
    else: OPTIONS[r["id"]] = (r["side"], amt, ps, r["label"])

def dist(parts):
    out = {g: 0.0 for g in GROUPS}; out["T1"] = 0.0
    for key, amt in parts:
        sh, t1 = K[key]
        assert abs(sum(sh) - 100) < 1e-6, key
        for g, s in zip(GROUPS, sh): out[g] += amt * s / 100
        out["T1"] += amt * t1 / 100
    return out

def per_hh(tn, g):
    n = HH * (0.01 if g == "T1" else (0.19 if g == "Q5x" else 0.2))
    return tn * 1e12 / 10 / n

def run(opts, drop=()):
    rows = [r for r in ROWS if r[0] not in drop]
    for o in opts:
        side, amt, parts, label = OPTIONS[o]; rows.append((o, label, side, amt, parts, "ledger option"))
    tot = {"cost": {}, "benefit": {}}
    lines = []
    for rid, label, side, amt, parts, basis in rows:
        d = dist(parts); lines.append((rid, label, side, amt, d, basis))
        for g, v in d.items(): tot[side][g] = tot[side].get(g, 0) + v
    groups = GROUPS + ["Q5x", "T1"]
    for side in tot:
        tot[side]["Q5x"] = tot[side]["Q5"] - tot[side]["T1"]
    res = {}
    for g in groups:
        b, c = tot["benefit"][g], tot["cost"][g]
        res[g] = dict(benefit=round(per_hh(b, g)), cost=round(per_hh(c, g)), net=round(per_hh(b - c, g)),
                      pct=round(100 * per_hh(b - c, g) / INC[g], 1) if INC[g] else None)
    return res, lines

def gf_test(opts):
    gf_ids = ["G1", "G5", "G7", "G3", "G9", "G11", "G6", "H1b", "GX", "G8", "G10"]
    total = top1 = corpstat = 0.0
    for rid, label, side, amt, parts, basis in ROWS:
        if rid in gf_ids:
            total += amt
            if rid in ("G1", "G5", "G7"): corpstat += amt
            else: top1 += dist(parts)["T1"]
    for o in opts:
        side, amt, parts, label = OPTIONS[o]
        if side == "cost" and o not in ("SAFR2", "EDUP"):  # C40 is corporate: counted with the top 1% via its 75% capital share  # EDUP is a dedicated fund, not general-fund revenue
            total += amt; d = dist(parts); top1 += d["T1"]
    return round(total, 2), round(top1, 2), round(corpstat, 2), round(100 * (top1 + corpstat) / total)

SCEN = {
    "A. Base package only (gap unfunded)": ([], ()),
    "B. Base plus the full options list (gap about $0.2T)": (["C18", "C19", "C20", "C5"], ()),
    "C. B without the employer-exclusion cap (C19)": (["C18", "C20", "C5"], ()),
    "D. B with the exclusion cap at the 75th percentile (C19b)": (["C18", "C19b", "C20", "C5"], ()),
    "E. B with no premium pass-through from the price caps": (["C18", "C19", "C20", "C5"], ("H5p",)),
    "F. B with SAF-R2 (alcohol excise dropped)": (["C18", "C19", "C20", "C5", "SAFR2"], ()),
    "G. EDU-9B education fund as the closer in place of C19 and C20": (["C18", "C5", "EDUP", "EDUB", "C35"], ()),
    "H. B plus the estate tax (C35)": (["C18", "C19", "C20", "C5", "C35"], ()),
    "P. Planning basis: Package B plus the sprint package (C18, C35, C19b, C20, C38; trims not yet decided)": (["C18", "C35", "C19b", "C20", "C38"], ()),
    "Q. Decided (Decision Brief 2): P plus TS12, HP1 and HP3 (C39-C41); no trims": (["C18", "C35", "C19b", "C20", "C38", "C39", "C40", "C41"], ()),
}

if __name__ == "__main__":
    out = {}
    for name, (o, drop) in SCEN.items():
        res, lines = run(o, drop)
        out[name] = dict(res=res, gf=gf_test(o))
        print(name, gf_test(o))
        for g in GROUPS + ["Q5x", "T1"]: print("  ", g, res[g])
    res, lines = run(["C18", "C19", "C20", "C5"])
    out["lines"] = [(rid, label, side, amt, {g: round(v, 3) for g, v in d.items()}, basis) for rid, label, side, amt, d, basis in lines]
    json.dump(out, open("incidence.json", "w"), indent=1)
    print("Q4 lines, scenario B:")
    q4 = sorted(((abs(per_hh(d["Q4"], "Q4")), rid, side, round(per_hh(d["Q4"], "Q4"))) for rid, label, side, amt, d, basis in lines), reverse=True)
    for _, rid, side, v in q4[:30]: print("  ", rid, side, v)
