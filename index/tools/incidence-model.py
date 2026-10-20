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
import json

HH = 140e6          # households, mid-window (estimate: ~132M in 2023 grown ~0.8%/yr)
GROUPS = ["Q1", "Q2", "Q3", "Q4", "Q5"]
INC = {"Q1": 23e3, "Q2": 60e3, "Q3": 105e3, "Q4": 180e3, "Q5": 520e3, "T1": 4.3e6, "Q5x": 0}  # 2034 avg expanded cash income, estimate

# Distribution keys: shares of the total for Q1..Q5, and the top 1%'s share of the total (inside Q5).
K = {
 "wages":       ([3, 9, 16, 26, 46], 12),
 "wages_cap":   ([3, 10, 19, 30, 38], 3),
 "capital":     ([1, 2, 4, 8, 85], 50),
 "consumption": ([9, 14, 19, 24, 34], 4),
 "alcohol":     ([12, 17, 21, 23, 27], 2),  # alcohol excise: flatter than consumption (regressive as a share of income); estimate
 "energy":      ([11, 15, 20, 24, 30], 3),
 "gasoline":    ([10, 16, 21, 25, 28], 1.5),
 "persons":     ([15, 18, 21, 22, 24], 1),
 "above400k":   ([0, 0, 0, 0, 100], 70),
 "above450k":   ([0, 0, 0, 0, 100], 80),
 "above250k_wages": ([0, 0, 0, 2, 98], 55),
 "billionaires":([0, 0, 0, 0, 100], 100),
 "death_gains": ([0, 0, 0, 0, 100], 85),
 "estate":      ([0, 0, 0, 0, 100], 85),   # estate tax at 2009 parameters ($3.5M): top 0.2% of estates; estimate
 "inv400k":     ([0, 0, 0, 0, 100], 85),
 "enforcement": ([2, 4, 6, 8, 80], 55),
 "ftt":         ([1, 3, 6, 12, 78], 40),
 "donors":      ([0, 2, 8, 25, 65], 20),   # scholarship-credit donors losing a $1,700 credit: filers with liability, upper-middle and up; estimate
 "ctc":         ([33, 30, 21, 12, 4], 0),
 "childcare":   ([28, 30, 24, 13, 5], 0),
 "education":   ([24, 26, 22, 17, 11], 0.5),
 "meals":       ([8, 20, 27, 26, 19], 0.5),  # universal meals, increment over current free/reduced and CEP: families now paying full or reduced price; estimate
 "service":     ([26, 28, 22, 15, 9], 0),   # national service stipend and award: young adults, weighted lower-middle; estimate
 "housing":     ([60, 25, 10, 4, 1], 0),
 "aca_medicaid":([38, 30, 19, 10, 3], 0),
 "medicare":    ([24, 26, 21, 16, 13], 1),
 "partb":       ([15, 24, 23, 20, 18], 1),
 "ma":          ([22, 27, 23, 16, 12], 0.5),
 "public_opt":  ([18, 30, 27, 17, 8], 0),
 "medicaid_ltc":([50, 25, 14, 7, 4], 0),
 "employer_cov":([3, 12, 24, 31, 30], 2),
 "ss_benefit":  ([30, 28, 20, 13, 9], 0.5),
 "leave_benefit":([8, 17, 24, 28, 23], 1),
 "hh_clean":    ([8, 14, 22, 28, 28], 2),
 "workers_ai":  ([15, 25, 28, 22, 10], 0),
 "low_income_energy": ([60, 40, 0, 0, 0], 0),
 "brackets_top":([0, 0, 1, 8, 91], 50),
 "exclusion_cap":([2, 10, 24, 33, 31], 2),
 "surtax":      ([0, 0, 0, 6, 94], 55),
}

def corp(x):  # 25% labor / 75% capital (JCT/CBO convention)
    return [("wages", 0.25 * x), ("capital", 0.75 * x)]

ROWS = [
 # --- general-fund base (domain-revenue.md) ---
 ("G1", "Corporate rate to 28%", "cost", 1.65, corp(1.65), "ledger; 25/75 incidence"),
 ("G5", "Buyback tax 4%, corporate minimum 21%", "cost", 0.40, corp(0.40), "ledger; 25/75 incidence"),
 ("G7", "Foreign income at full rate", "cost", 0.41, corp(0.41), "ledger; 25/75 incidence"),
 ("G3", "39.6% top rate above $400K", "cost", 0.30, [("above400k", 0.30)], "ledger"),
 ("G9", "2025 cuts reversed above $450K", "cost", 1.45, [("above450k", 1.45)], "ledger"),
 ("G11", "Mark-to-market for billionaires", "cost", 0.65, [("billionaires", 0.65)], "ledger"),
 ("G6", "Gains taxed at death", "cost", 0.70, [("death_gains", 0.70)], "ledger"),
 ("H1b", "Medicare/NIIT to 5% above $400K", "cost", 0.50, [("inv400k", 0.50)], "ledger"),
 ("GX", "Overlap and avoidance haircut", "cost", -0.495, [("above450k", -0.495)], "ledger"),
 ("G8", "IRS enforcement", "cost", 0.40, [("enforcement", 0.40)], "ledger"),
 ("G10", "Financial transaction tax", "cost", 0.40, [("ftt", 0.40)], "ledger"),
 # --- dedicated channels ---
 ("H1a", "NIIT on active pass-through income (HI)", "cost", 0.50, [("inv400k", 0.50)], "ledger"),
 ("O1", "SS tax above $250K (SS-1)", "cost", 1.90, [("above250k_wages", 1.90)], "ledger"),
 ("O2", "SS tax on investment income above $400K, net of haircut", "cost", 0.935, [("inv400k", 0.935)], "ledger"),
 ("P1", "Paid-leave contribution 0.6%", "cost", 0.90, [("wages_cap", 0.90)], "ledger; both halves on workers"),
 ("C1", "Carbon fee (domestic)", "cost", 1.35, [("energy", 1.35)], "ledger (durability path, Oct 20); full pass-through to households"),
 ("C2", "Carbon border adjustment", "cost", 0.20, [("consumption", 0.20)], "ledger; full pass-through"),
 ("MR", "Moving America fuel steps and per-mile charge", "cost", 0.41, [("gasoline", 0.41)], "ledger MR1+MR2"),
 ("MRc", "Moving America truck, rail and aviation charges", "cost", 0.126, [("consumption", 0.126)], "ledger MR4+MR5"),
 ("PS1", "Safe Everywhere revenue title, durable sources (alcohol $0.07T, fraud assessment $0.012T, firearms and check fees $0.009T)", "cost", 0.091,
  [("alcohol", 0.07), ("consumption", 0.021)], "ledger PS1 restated Oct 20; full pass-through"),
 ("PB", "Part B premium increase (a quarter of HLT-2's new benefits)", "cost", 0.30, [("partb", 0.30)], "estimate from go-big tab (~$18/month)"),
 ("MA", "MA plans' reduced extras after full capture (30% pass-through)", "cost", 0.375, [("ma", 0.375)], "estimate: 30% of HLT-6's $1.25T"),
 ("EDU7", "Scholarship tax credit repealed (EDU-7): donors lose the credit", "cost", 0.04, [("donors", 0.04)], "ledger EDU-7 (new Oct 20)"),
 # --- benefits ---
 ("F1", "Child Tax Credit (FAM-1)", "benefit", 1.50, [("ctc", 1.50)], "ledger"),
 ("F2", "Child care and pre-K (FAM-2)", "benefit", 0.60, [("childcare", 0.60)], "ledger"),
 ("F3", "Paid leave benefits (FAM-3)", "benefit", 0.90, [("leave_benefit", 0.90)], "ledger"),
 ("EDU", "Education formula funding and higher education (EDU-1, EDU-5; was FAM-4)", "benefit", 0.65, [("education", 0.65)], "ledger (FAM-4 split Oct 20, same total)"),
 ("EDU3", "Universal school meals and Summer EBT (EDU-3)", "benefit", 0.27, [("meals", 0.27)], "ledger EDU-3 (new Oct 20)"),
 ("EDU4", "Educator pipeline (EDU-4)", "benefit", 0.03, [("education", 0.03)], "ledger EDU-4 (new Oct 20)"),
 ("H1", "Health restoration (HLT-1)", "benefit", 2.45, [("aca_medicaid", 2.45)], "ledger"),
 ("H2", "Medicare upgrades, gross of premiums (HLT-2)", "benefit", 1.37, [("medicare", 1.37)], "ledger 1.07 + premiums 0.30"),
 ("H3", "Public option and cost-sharing help (HLT-3)", "benefit", 1.90, [("public_opt", 1.90)], "ledger"),
 ("H4", "Medicaid, long-term care, safety net (HLT-4)", "benefit", 0.625, [("medicaid_ltc", 0.625)], "ledger"),
 ("H5p", "Hospital and drug price caps: lower employer premiums passed to wages", "benefit", 0.50, [("employer_cov", 0.50)], "estimate (go-big tab ~6% premium cut; conservative)"),
 ("F5", "Social Security minimum benefit and CPI-E (SS-3, SS-4)", "benefit", 0.25, [("ss_benefit", 0.25)], "ledger"),
 ("E2d", "Climate Dividend (CLI-2, 80%)", "benefit", 1.08, [("persons", 1.08)], "ledger (durability path, Oct 20)"),
 ("E2t", "Carbon transition share: low-income energy help (40% of $0.27T)", "benefit", 0.108, [("low_income_energy", 0.108)], "estimate"),
 ("HOU", "Housing (HOU-1 to HOU-6 fund, HOU-8: vouchers, emergency aid, credits, repair)", "benefit", 0.47, [("housing", 0.47)], "ledger HOU-1 (was E6 $0.60T)"),
 ("E1h", "Clean-energy credits, household share (30% of CLI-1)", "benefit", 0.27, [("hh_clean", 0.27)], "estimate: 30% of CLI-1's $0.9T"),
 ("E12", "AI and work transition support (AI-4)", "benefit", 0.20, [("workers_ai", 0.20)], "ledger"),
 ("LAB8", "Registered apprenticeships (LAB-8)", "benefit", 0.03, [("education", 0.03)], "ledger (new Oct 20)"),
 ("LAB9", "National service stipend and education award (LAB-9)", "benefit", 0.12, [("service", 0.12)], "ledger (new Oct 20)"),
]

OPTIONS = {
 "C18": ("cost", 0.62, [("brackets_top", 0.62)], "Top four brackets +1, gains +2, LIFO"),
 "C19": ("cost", 1.25, [("exclusion_cap", 1.25)], "Cap the employer health exclusion"),
 "C19b": ("cost", 0.66, [("exclusion_cap", 0.66)], "Cap the employer health exclusion at the 75th percentile (CBO alt. 2, scaled)"),
 "C20": ("cost", 0.67, [("surtax", 0.67)], "1-point surtax above $100K/$200K"),
 "C38": ("cost", 0.89, corp(0.665) + [("estate", 0.10), ("above400k", 0.03), ("capital", 0.075), ("above450k", 0.02)], "Top-end sprint package REV-TS1 to TS11, net of a 10% haircut (corporate items on the 25/75 convention)"),
 "C5":  ("benefit", -0.30, [("medicare", -0.30)], "Dental starts after the window"),
 "SAFR2": ("cost", -0.07, [("alcohol", -0.07)], "SAF-R2: drop the alcohol excise (replaced with top-end revenue, not modeled here)"),
 "C35": ("cost", 0.15, [("estate", 0.15)], "Estate tax at 2009 parameters, exemption frozen (REV-E1), increment beyond G9"),
 "C36": ("benefit", -0.19, [("meals", -0.19)], "Meals at community-eligibility scale (EDU-3B) instead of universal"),
 "EDUP": ("cost", 2.27, [("wages", 2.27)], "EDU-9B education contribution, ~1.4 points uncapped payroll (all on workers)"),
 "EDUB": ("benefit", 0.63, [("childcare", 0.24), ("education", 0.39)], "EDU-9B new benefits beyond the chosen rows (pre-K and child care share, teacher floor, PARA, Title I and IDEA top-ups)"),
}

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
        if side == "cost" and o not in ("SAFR2", "EDUP"):  # EDUP is a dedicated fund, not general-fund revenue
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
