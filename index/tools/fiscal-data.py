#!/usr/bin/env python3
"""fiscal-data.py: build the all-of-government baseline for the long-term fiscal model.

Output: index/data/fiscal-baseline.csv, one row per fiscal year 1962-2056, in billions of
nominal dollars, with the same categories in every period:

  actual        FY1962-2025  CBO Historical Budget Data (Feb 2026 vintage)
  actual-prelim FY2026       CBO Monthly Budget Review, Sept 2026 (totals only; categories
                             stay at CBO's February projection, scaled to the actual totals)
  cbo-10yr      FY2027-2036  CBO Budget and Economic Outlook, Feb 2026 (10-year baseline)
  cbo-lt        FY2037-2056  CBO Long-Term Budget Outlook, Feb 2026 (% of GDP x CBO GDP)

Source files are CBO's own standardized CSVs (github.com/US-CBO/cbo-data, long format
date/variable/value). Run with --fetch to download them into the cache folder first.

Categories (all net, matching CBO's long-term groupings so the periods line up):
  rev_individual, rev_payroll, rev_corporate, rev_customs, rev_other (excise, estate, misc.)
  out_social_security, out_medicare_net (gross less Medicare offsetting receipts),
  out_health_other (Medicaid, CHIP, marketplace subsidies), out_other_mandatory (net of
  other offsetting receipts), out_disc_defense, out_disc_nondefense, out_net_interest
Known seam: before FY2025 the historical file does not split Medicare offsetting receipts
or CHIP and marketplace subsidies, so for FY1962-2024 out_health_other is Medicaid only and
out_medicare_net is the rest of CBO's net "major health care" line.

Post-February adjustments (the "adjusted" baseline the model uses by default) are in
ADJUSTMENTS below, each with a basis. The unadjusted CBO baseline stays in the file.
"""
import csv, os, sys, urllib.request, collections, argparse

HERE = os.path.dirname(os.path.abspath(__file__))
GH = "https://raw.githubusercontent.com/US-CBO/cbo-data/main/data/"
FILES = {
    "hist": "budget/historical_budget/annual_fy_2026-02.csv",
    "ten": "budget/ten_year_budget/annual_fy_2026-02.csv",
    "lt": "budget/long_term_budget/annual_fy_2026-02.csv",
    "econ": "economic/economic_projections/fiscal_2026-02.csv",
    "ltecon": "economic/long_term_economic/levels_2026-02.csv",
}

# FY2026 preliminary actuals (CBO Monthly Budget Review for September 2026, via AAF and
# CRFB, Oct 8, 2026): deficit $2.0T (up $218B from FY2025), revenue up $169B, outlays up
# $386B, net interest up $115B, customs down $22B, debt held by the public $32.4T.
FY2026_ACTUAL = {"rev_total": 5234.616 + 169, "out_total": 7009.986 + 386,
                 "out_net_interest": 969.938 + 115, "rev_customs": 194.866 - 22,
                 "debt_public": 32400.0}

# Adjustments to CBO's February 2026 baseline for events since (billions; + raises the
# deficit). Each is an estimate and can be switched off in fiscal-model.py.
ADJUSTMENTS = [
    # Learning Resources (Feb 2026) ended the IEEPA tariffs that CBO's February baseline
    # carried. CRFB: the replacement Section 301/338 tariffs raise about $950B through
    # FY2036, under 60% of the lost IEEPA revenue, so the net loss is at least ~$0.65T over
    # FY2027-36 (domain-revenue.md, tariffs section). Spread with GDP; continues after 2036
    # at the same share of GDP, fading by half by 2046 as CBO's customs share falls.
    {"id": "ADJ-T1", "label": "Tariff ruling: IEEPA tariffs replaced by smaller 301/338 tariffs (net revenue loss)",
     "kind": "rev_customs", "ten_year_total": -650.0, "years": (2027, 2036), "after": "fade_half_2046",
     "basis": "Estimate from CRFB (Jul 2026): replacement tariffs ~$950B through FY2036, <60% of lost IEEPA revenue"},
    # Of $166B in court-ordered refunds, about $130B was paid in FY2026 (already in the
    # actual); the remaining ~$36B falls in FY2027.
    {"id": "ADJ-T2", "label": "Remaining IEEPA tariff refunds", "kind": "rev_customs",
     "one_time": {2027: -36.0}, "basis": "AAF (Oct 2026): ~$130B of $166B refunded in FY2026"},
]

CATS_REV = ["rev_individual", "rev_payroll", "rev_corporate", "rev_customs", "rev_other"]
CATS_OUT = ["out_social_security", "out_medicare_net", "out_health_other", "out_other_mandatory",
            "out_disc_defense", "out_disc_nondefense", "out_net_interest"]


def load(path):
    d = collections.defaultdict(dict)
    with open(path) as f:
        for r in csv.DictReader(f):
            k = r["date"].replace("FY", "")
            try:
                d[r["variable"]][int(k)] = float(r["value"])
            except (ValueError, TypeError):
                pass
    return d


def fetch(cache):
    os.makedirs(cache, exist_ok=True)
    for k, p in FILES.items():
        out = os.path.join(cache, p.replace("/", "_"))
        urllib.request.urlretrieve(GH + p, out)
        print("fetched", out)


def build(cache):
    P = {k: load(os.path.join(cache, p.replace("/", "_"))) for k, p in FILES.items()}
    h, t, lt, e = P["hist"], P["ten"], P["lt"], P["econ"]
    rows = {}
    # --- history FY1962-2024 (FY2025 comes from the 10-year file, which splits offsets) ---
    for y in range(1962, 2025):
        gdp = h["revenues"][y] / h["revenues_gdp_share"][y] * 100
        r = {"year": y, "source": "actual", "gdp": gdp}
        r["rev_individual"] = h["rev_individual_income"][y]
        r["rev_payroll"] = h["rev_payroll"][y]
        r["rev_corporate"] = h["rev_corporate_income"][y]
        r["rev_customs"] = h["rev_customs"][y]
        r["rev_other"] = h["rev_excise"][y] + h["rev_estate_gift"][y] + h["rev_miscellaneous"][y]
        r["out_social_security"] = h["mand_social_security"][y]
        mh = h["mand_major_health_care"].get(y, 0.0)
        md = h["mand_medicaid"].get(y, 0.0)
        r["out_health_other"] = md
        r["out_medicare_net"] = mh - md
        r["out_other_mandatory"] = h["mand_total"][y] - h["mand_social_security"][y] - mh
        r["out_disc_defense"] = h["disc_defense"][y]
        r["out_disc_nondefense"] = h["disc_nondefense"][y]
        r["out_net_interest"] = h["outlays_net_interest"][y]
        r["debt_public"] = h["debt_held_by_public"][y]
        rows[y] = r
    # --- FY2025 actual and FY2026-2036 projections from the 10-year file ---
    for y in range(2025, 2037):
        r = {"year": y, "source": "actual" if y == 2025 else "cbo-10yr"}
        r["gdp"] = e["gdp"][y]
        r["rev_individual"] = t["proj_rev_individual_income"][y]
        r["rev_payroll"] = t["proj_rev_payroll"][y]
        r["rev_corporate"] = t["proj_rev_corporate_income"][y]
        r["rev_customs"] = t["proj_rev_customs"][y]
        r["rev_other"] = t["proj_rev_other"][y]
        ss = t["proj_mand_social_security"][y]
        mc = t["proj_mand_medicare"][y] + t["proj_offset_medicare"][y]
        ho = t["proj_mand_medicaid"][y] + t["proj_mand_chip"][y] + t["proj_mand_premium_tax_credits"][y]
        r["out_social_security"] = ss
        r["out_medicare_net"] = mc
        r["out_health_other"] = ho
        r["out_other_mandatory"] = t["proj_mand_incl_offsets"][y] - ss - mc - ho
        r["out_disc_defense"] = t["proj_disc_defense"][y]
        r["out_disc_nondefense"] = t["proj_disc_nondefense"][y]
        r["out_net_interest"] = t["proj_outlays_net_interest"][y]
        r["debt_public"] = t["proj_debt_held_by_public"][y]
        r["cbo_avg_rate"] = t["proj_debt_avg_interest_rate"][y]
        r["note10"] = e["treasury_note_rate_10yr"].get(y)
        r["bill3m"] = e["treasury_bill_rate_3mo"].get(y)
        rows[y] = r
    # --- FY2037-2056 from the long-term file (% of GDP) ---
    dshare = rows[2036]["out_disc_defense"] / (rows[2036]["out_disc_defense"] + rows[2036]["out_disc_nondefense"])
    for y in range(2037, 2057):
        g = lt["lt_gdp_trillions"][y] * 1000
        s = lambda v: lt[v][y] / 100 * g
        r = {"year": y, "source": "cbo-lt", "gdp": g}
        r["rev_individual"] = s("lt_rev_individual_income_gdp_share")
        r["rev_payroll"] = s("lt_rev_payroll_gdp_share")
        r["rev_corporate"] = s("lt_rev_corporate_income_gdp_share")
        r["rev_customs"] = s("lt_rev_customs_gdp_share")
        r["rev_other"] = s("lt_rev_other_gdp_share")
        r["out_social_security"] = s("lt_mand_social_security_gdp_share")
        r["out_medicare_net"] = s("lt_mand_medicare_gdp_share")
        r["out_health_other"] = s("lt_mand_medicaid_chip_gdp_share")
        r["out_other_mandatory"] = s("lt_mand_other_gdp_share")
        disc = s("lt_outlays_discretionary_gdp_share")
        r["out_disc_defense"] = disc * dshare
        r["out_disc_nondefense"] = disc * (1 - dshare)
        r["out_net_interest"] = s("lt_outlays_net_interest_gdp_share")
        r["debt_public"] = s("lt_debt_held_by_public_gdp_share")
        rows[y] = r
    # totals, deficits, implied average rate
    for y in sorted(rows):
        r = rows[y]
        r["rev_total"] = sum(r[c] for c in CATS_REV)
        r["out_total"] = sum(r[c] for c in CATS_OUT)
        r["out_primary"] = r["out_total"] - r["out_net_interest"]
        r["deficit"] = r["out_total"] - r["rev_total"]
        r["primary_deficit"] = r["out_primary"] - r["rev_total"]
        if y - 1 in rows and rows[y - 1].get("debt_public"):
            r["implied_rate"] = 100 * r["out_net_interest"] / rows[y - 1]["debt_public"]
    # FY2026 preliminary actuals: scale categories to the actual totals
    r = rows[2026]
    r["source"] = "actual-prelim"
    r["cbo_feb_deficit"] = r["deficit"]
    r["rev_customs"] = FY2026_ACTUAL["rev_customs"]
    other_rev = [c for c in CATS_REV if c != "rev_customs"]
    k = (FY2026_ACTUAL["rev_total"] - r["rev_customs"]) / sum(r[c] for c in other_rev)
    for c in other_rev: r[c] *= k
    r["out_net_interest"] = FY2026_ACTUAL["out_net_interest"]
    prim = [c for c in CATS_OUT if c != "out_net_interest"]
    k = (FY2026_ACTUAL["out_total"] - r["out_net_interest"]) / sum(r[c] for c in prim)
    for c in prim: r[c] *= k
    r["debt_public"] = FY2026_ACTUAL["debt_public"]
    r["rev_total"] = sum(r[c] for c in CATS_REV); r["out_total"] = sum(r[c] for c in CATS_OUT)
    r["out_primary"] = r["out_total"] - r["out_net_interest"]
    r["deficit"] = r["out_total"] - r["rev_total"]; r["primary_deficit"] = r["out_primary"] - r["rev_total"]
    # adjustment column (+ raises the deficit)
    for y in rows: rows[y]["adj_deficit"] = 0.0
    for a in ADJUSTMENTS:
        if "one_time" in a:
            for y, v in a["one_time"].items(): rows[y]["adj_deficit"] += -v
            continue
        y0, y1 = a["years"]
        gsum = sum(rows[y]["gdp"] for y in range(y0, y1 + 1))
        share = a["ten_year_total"] / gsum
        for y in range(y0, 2057):
            if y <= y1:
                f = 1.0
            else:
                f = max(0.5, 1 - 0.5 * (y - y1) / 10) if a["after"] == "fade_half_2046" else 1.0
            rows[y]["adj_deficit"] += -share * f * rows[y]["gdp"]
    return rows


def write(rows, out):
    cols = ["year", "source", "gdp"] + CATS_REV + ["rev_total"] + CATS_OUT + [
        "out_primary", "out_total", "deficit", "primary_deficit", "debt_public", "implied_rate",
        "cbo_avg_rate", "note10", "bill3m", "adj_deficit", "cbo_feb_deficit"]
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(cols)
        for y in sorted(rows):
            r = rows[y]
            w.writerow([r.get(c, "") if isinstance(r.get(c, ""), str) else round(r[c], 3) for c in cols])
    print("wrote", out, len(rows), "years")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--cache", default=os.path.join(HERE, "..", "data", "cbo"))
    ap.add_argument("--out", default=os.path.join(HERE, "..", "data", "fiscal-baseline.csv"))
    ap.add_argument("--fetch", action="store_true")
    a = ap.parse_args()
    if a.fetch: fetch(a.cache)
    write(build(a.cache), a.out)
