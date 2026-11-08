#!/usr/bin/env python3
"""build_data.py: write the budget data layer (models/data/budget/) from its cached sources.

Role: the only writer of the generated CSVs in models/data/budget/ (the README there lists
them). Status: current (budget workflow piece B2). Standard library only.

Sources, all cached in the repository:
  models/data/cbo/*.csv          CBO's February 2026 standardized CSVs (github.com/US-CBO/cbo-data),
                                 the same files fiscal-data.py reads
  models/data/budget/omb/*.xlsx  OMB Historical Tables, FY2027 Budget (April 2026), tables 3.2,
                                 5.1, 5.6 and 8.7; public domain

The CBO values are copied as CBO wrote them (no re-rounding), so the loader and the
reproduction test see exactly the numbers fiscal-data.py sees. OMB values are converted from
millions to billions exactly (decimal arithmetic). OMB's estimate columns (FY2026 on, the
administration's proposals) are left out: only actual years are kept.

Usage (from the repo root):
  python3 models/tools/budget/build_data.py           # write the files
  python3 models/tools/budget/build_data.py --check   # exit 1 if a committed file differs
"""
import argparse, collections, csv, io, os, re, sys, zipfile
from decimal import Decimal
from xml.etree import ElementTree as ET

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, "..", "..", ".."))
CBO = os.path.join(ROOT, "models", "data", "cbo")
OUT = os.path.join(ROOT, "models", "data", "budget")
OMB = os.path.join(OUT, "omb")
LAST_ACTUAL = 2025   # last fiscal year OMB and CBO report as actual in these vintages
ROUND_TOL = Decimal("0.005")  # billions: OMB rounds each function line to $1 million on its own; the gap to the published total is at most $3 million (FY1962-2025)

# CBO variables carried into the layer, by file. Anything a category formula in
# categories.csv or a loader function names must be here.
CBO_FILES = {
    "cbo-historical.csv": ("budget_historical_budget_annual_fy_2026-02.csv", [
        "revenues", "revenues_gdp_share", "rev_individual_income", "rev_payroll",
        "rev_corporate_income", "rev_customs", "rev_excise", "rev_estate_gift",
        "rev_miscellaneous", "rev_total", "mand_social_security", "mand_major_health_care",
        "mand_medicare", "mand_medicaid", "mand_income_security", "mand_federal_retirement",
        "mand_veterans", "mand_other", "mand_offsetting_receipts", "mand_total",
        "disc_defense", "disc_nondefense", "disc_total", "outlays_net_interest",
        "outlays_total", "deficit_total", "debt_held_by_public"]),
    "cbo-ten-year.csv": ("budget_ten_year_budget_annual_fy_2026-02.csv", [
        "proj_rev_individual_income", "proj_rev_payroll", "proj_rev_corporate_income",
        "proj_rev_customs", "proj_rev_other", "proj_rev_total",
        "proj_mand_social_security", "proj_mand_medicare", "proj_offset_medicare",
        "proj_mand_medicaid", "proj_mand_chip", "proj_mand_premium_tax_credits",
        "proj_mand_incl_offsets", "proj_outlays_mandatory",
        "proj_disc_defense", "proj_disc_nondefense", "proj_outlays_discretionary",
        "proj_disc_defense_ba_timing_adj", "proj_disc_defense_base_ba_timing_adj",
        "proj_disc_defense_emergency_ba_timing_adj", "proj_disc_nondefense_ba_timing_adj",
        "proj_disc_nondefense_base_ba_timing_adj", "proj_disc_nondefense_emergency_ba_timing_adj",
        "proj_disc_total_ba_timing_adj", "proj_outlays_net_interest", "proj_outlays_total",
        "proj_deficit_total", "proj_debt_held_by_public", "proj_debt_avg_interest_rate",
        "proj_timing_adjustment"]),
    "cbo-long-term.csv": ("budget_long_term_budget_annual_fy_2026-02.csv", [
        "lt_gdp_trillions", "lt_rev_individual_income_gdp_share", "lt_rev_payroll_gdp_share",
        "lt_rev_corporate_income_gdp_share", "lt_rev_customs_gdp_share", "lt_rev_other_gdp_share",
        "lt_rev_total_gdp_share", "lt_mand_social_security_gdp_share", "lt_mand_medicare_gdp_share",
        "lt_mand_medicaid_chip_gdp_share", "lt_mand_other_gdp_share",
        "lt_outlays_discretionary_gdp_share", "lt_outlays_net_interest_gdp_share",
        "lt_outlays_total_gdp_share", "lt_deficit_total_gdp_share",
        "lt_debt_held_by_public_gdp_share"]),
    "cbo-economic.csv": ("economic_economic_projections_fiscal_2026-02.csv", [
        "gdp", "cpiu", "gdp_price_index", "treasury_note_rate_10yr", "treasury_bill_rate_3mo"]),
    "cbo-economic-historical.csv": ("economic_historical_economic_annual_fy_2026-02.csv", [
        "gdp", "cpiu", "gdp_price_index"]),
    "cbo-long-term-economic.csv": ("economic_long_term_economic_levels_2026-02.csv", [
        "nominal_gdp_level", "cpiu_index_level", "gdp_price_index_level"]),
}


def cbo_table(src, keep):
    """CBO long file (date, variable, value[, estimate_type]) -> rows by year, values verbatim."""
    vals, est = collections.defaultdict(dict), {}
    with open(os.path.join(CBO, src)) as f:
        for r in csv.DictReader(f):
            if r["variable"] not in keep:
                continue
            y = int(r["date"].replace("FY", ""))
            if r["value"] not in ("", None):
                vals[y][r["variable"]] = r["value"]
            if r.get("estimate_type"):
                est.setdefault(y, set()).add(r["estimate_type"])
    cols = ["year"] + (["estimate_type"] if est else []) + keep
    rows = []
    for y in sorted(vals):
        row = {"year": str(y), **vals[y]}
        if est:
            row["estimate_type"] = "/".join(sorted(est.get(y, [])))
        rows.append(row)
    return cols, rows


# ---------- OMB Historical Tables (xlsx, read with the standard library) ----------
NS = {"m": "http://schemas.openxmlformats.org/spreadsheetml/2006/main"}


def xlsx_rows(path):
    z = zipfile.ZipFile(path)
    shared = []
    if "xl/sharedStrings.xml" in z.namelist():
        for si in ET.fromstring(z.read("xl/sharedStrings.xml")).findall("m:si", NS):
            shared.append("".join(t.text or "" for t in si.iter("{%s}t" % NS["m"])))
    sheet = ET.fromstring(z.read("xl/worksheets/sheet1.xml"))
    out = []
    for row in sheet.iter("{%s}row" % NS["m"]):
        cells = {}
        for c in row.findall("m:c", NS):
            col = re.match(r"[A-Z]+", c.get("r")).group()
            n = 0
            for ch in col:
                n = n * 26 + ord(ch) - 64
            v = c.find("m:v", NS)
            t = c.get("t")
            if t == "s" and v is not None:
                val = shared[int(v.text)]
            elif t == "inlineStr":
                val = "".join(x.text or "" for x in c.iter("{%s}t" % NS["m"]))
            else:
                val = v.text if v is not None else None
            cells[n - 1] = val
        if cells:
            out.append([cells.get(i) for i in range(max(cells) + 1)])
    return out


def year_columns(header):
    """Column index -> fiscal year, for actual years only (drops TQ and 'estimate' columns)."""
    cols = {}
    for i, h in enumerate(header):
        h = (h or "").strip()
        if re.fullmatch(r"\d{4}", h) and int(h) <= LAST_ACTUAL:
            cols[i] = int(h)
    return cols


def billions(raw):
    """OMB cell (millions) -> (billions as exact decimal string, flag)."""
    s = (raw or "").strip()
    if s in ("", "N/A"):
        return "", "n/a"
    if set(s) == {"."}:
        return "", "none"          # OMB prints dots where there is no amount
    if s == "*":
        return "", "under_0.5m"     # OMB: $500 thousand or less
    return format((Decimal(s) / 1000).normalize(), "f"), ""


def omb_by_function(fname, value_name):
    rows = xlsx_rows(os.path.join(OMB, fname))
    hdr_i = next(i for i, r in enumerate(rows) if r and (r[0] or "").startswith("Function and Subfunction"))
    ycols = year_columns(rows[hdr_i])
    out, cur, names, subs, totalled = [], None, {}, collections.defaultdict(list), set()

    def close(c):
        """A function with one subfunction and no "Total" line (570 Medicare, 650 Social
        Security): its subfunction is the function total."""
        if c is not None and c not in totalled:
            if len(subs[c]) != 1:
                raise SystemExit("%s: function %03d has no total line" % (fname, c))
            out.extend(dict(x, level="function", code="%03d" % c, name=names[c])
                       for x in out if x["level"] == "subfunction" and x["code"] == subs[c][0])
            totalled.add(c)

    for r in rows[hdr_i + 1:]:
        label = (r[0] or "").strip()
        m = re.match(r"^(\d{3}) (.*?)(:)?$", label)
        if m and m.group(3) and int(m.group(1)) % 10:
            continue                             # "051 Department of Defense-Military:" groups detail lines
        if m and m.group(3):                     # "050 National Defense:" opens a function (codes end in 0)
            close(cur)
            cur = int(m.group(1)); names[cur] = m.group(2).strip()
            continue
        if m:
            level, code, name = "subfunction", int(m.group(1)), m.group(2)
            subs[cur].append("%03d" % code)
        elif label.startswith("Total, ") and cur is not None:
            level, code, name = "function", cur, names[cur]
            totalled.add(cur)
        elif label.startswith("Total outlays") or label.startswith("Total budget authority"):
            close(cur)
            level, code, name = "total", 0, "Total"
        else:
            continue                             # sub-subfunction detail, on/off-budget splits, notes
        for i, y in ycols.items():
            v, flag = billions(r[i] if i < len(r) else None)
            out.append({"year": y, "level": level, "code": "%03d" % code, "name": name.strip(),
                        value_name: v, "flag": flag})
    # the function rows must add to the published total in every year (integer millions)
    for y in sorted(set(x["year"] for x in out)):
        f = sum(Decimal(x[value_name] or 0) for x in out if x["year"] == y and x["level"] == "function")
        t = [Decimal(x[value_name]) for x in out if x["year"] == y and x["level"] == "total"]
        if len(t) != 1 or abs(f - t[0]) > ROUND_TOL:
            raise SystemExit("%s FY%d: functions sum to %s, table total %s" % (fname, y, f, t))
    out.sort(key=lambda x: (x["year"], {"total": 9}.get(x["level"], 0), x["code"], x["level"] != "function"))
    return ["year", "level", "code", "name", value_name, "flag"], out


DISC_LABELS = {  # Table 5.6 / 8.7 row label (lowercased) -> (program id, group)
    "dod-military (051)": ("defense_051", "defense"),
    "other defense": ("defense_other", "defense"),
    "total national defense": ("defense_total", "defense"),
    "international affairs": ("international_affairs", "nondefense"),
    "total general science, space and technology": ("science_space_technology", "nondefense"),
    "energy": ("energy", "nondefense"),
    "natural resources and environment": ("natural_resources_environment", "nondefense"),
    "agriculture": ("agriculture", "nondefense"),
    "commerce and housing credit": ("commerce_housing_credit", "nondefense"),
    "total transportation": ("transportation", "nondefense"),
    "community and regional development": ("community_regional_development", "nondefense"),
    "total education, training, employment and social services": ("education_training_social", "nondefense"),
    "health": ("health", "nondefense"),
    "medicare": ("medicare", "nondefense"),
    "housing assistance": ("housing_assistance", "nondefense"),
    "total income security": ("income_security", "nondefense"),
    "social security": ("social_security", "nondefense"),
    "veterans benefits and services": ("veterans", "nondefense"),
    "administration of justice": ("administration_of_justice", "nondefense"),
    "general government": ("general_government", "nondefense"),
    "allowances": ("allowances", "nondefense"),
    "total nondefense": ("nondefense_total", "nondefense"),
    "total discretionary budget authority": ("discretionary_total", "total"),
    "total outlays for discretionary programs": ("discretionary_total", "total"),
}


def omb_discretionary():
    data = {}
    for fname, col in (("hist05z6.xlsx", "ba"), ("hist08z7.xlsx", "outlays")):
        rows = xlsx_rows(os.path.join(OMB, fname))
        hdr_i = next(i for i, r in enumerate(rows) if r and (r[0] or "").startswith("Category and Program"))
        ycols = year_columns(rows[hdr_i])
        seen = set()
        for r in rows[hdr_i + 1:]:
            key = (r[0] or "").strip().lower()
            if key not in DISC_LABELS:
                continue
            pid, grp = DISC_LABELS[key]
            if pid in seen:   # "Other" and "Medicare" style labels appear once each; guard anyway
                raise SystemExit("%s: duplicate row %s" % (fname, pid))
            seen.add(pid)
            for i, y in ycols.items():
                v, flag = billions(r[i] if i < len(r) else None)
                d = data.setdefault((y, pid), {"year": y, "program": pid, "group": grp,
                                               "ba": "", "outlays": "", "flag": ""})
                d[col] = v
                if flag and flag != "none":
                    d["flag"] = (d["flag"] + " " + col + ":" + flag).strip()
        missing = set(v[0] for v in DISC_LABELS.values()) - seen
        if missing:
            raise SystemExit("%s: rows not found: %s" % (fname, sorted(missing)))
    rows = [data[k] for k in sorted(data)]
    rows = [r for r in rows if r["ba"] != "" or r["outlays"] != "" or r["year"] >= 1976]
    return ["year", "program", "group", "ba", "outlays", "flag"], rows


# ---------- derived: deflators and spend-out ----------
def deflators(hist, proj, lt):
    """Fiscal-year CPI-U and GDP price index, FY1950-2056, in CBO's own index bases."""
    H = {int(r["year"]): r for r in hist}
    P = {int(r["year"]): r for r in proj}
    L = {int(r["year"]): r for r in lt}
    out, last = [], {}
    for y in range(min(H), 2057):
        if y in H and y <= LAST_ACTUAL:
            src, c, g = "cbo-economic-historical", float(H[y]["cpiu"]), float(H[y]["gdp_price_index"])
        elif y in P:
            src, c, g = "cbo-economic", float(P[y]["cpiu"]), float(P[y]["gdp_price_index"])
        else:  # after FY2036: grow the FY2036 level by the long-term calendar-year index growth
            src = "cbo-long-term-economic growth from FY2036"
            c = last["c"] * float(L[y]["cpiu_index_level"]) / float(L[y - 1]["cpiu_index_level"])
            g = last["g"] * float(L[y]["gdp_price_index_level"]) / float(L[y - 1]["gdp_price_index_level"])
        out.append({"year": y, "cpiu": "%.4f" % c, "gdp_price_index": "%.4f" % g, "source": src})
        last = {"c": c, "g": g}
    return ["year", "cpiu", "gdp_price_index", "source"], out


def solve(A, b):
    """Gaussian elimination for a small dense system."""
    n = len(A)
    M = [row[:] + [b[i]] for i, row in enumerate(A)]
    for i in range(n):
        p = max(range(i, n), key=lambda r: abs(M[r][i]))
        M[i], M[p] = M[p], M[i]
        for r in range(n):
            if r != i:
                f = M[r][i] / M[i][i]
                M[r] = [a - f * c for a, c in zip(M[r], M[i])]
    return [M[i][n] / M[i][i] for i in range(n)]


SPEND_YEARS = (1993, 2019)   # post credit reform, before the pandemic emergency appropriations
LAGS = 4                     # outlays this year from budget authority of this year and 3 before


def spendout(disc_rows):
    """Estimated spend-out of discretionary budget authority, by group: least-squares weights w_k
    in outlays(t) = sum_k w_k * BA(t-k), k = 0..LAGS-1, over SPEND_YEARS. An estimate from
    annual totals, not CBO's program-level outlay rates; see the README."""
    S = collections.defaultdict(dict)
    for r in disc_rows:
        if r["program"] in ("defense_total", "nondefense_total") and r["ba"] and r["outlays"]:
            S[r["program"]][r["year"]] = (float(r["ba"]), float(r["outlays"]))
    out = []
    for prog, grp in (("defense_total", "defense"), ("nondefense_total", "nondefense")):
        d = S[prog]
        yrs = range(SPEND_YEARS[0], SPEND_YEARS[1] + 1)
        X = [[d[y - k][0] for k in range(LAGS)] for y in yrs]
        yv = [d[y][1] for y in yrs]
        A = [[sum(x[i] * x[j] for x in X) for j in range(LAGS)] for i in range(LAGS)]
        b = [sum(x[i] * v for x, v in zip(X, yv)) for i in range(LAGS)]
        w = solve(A, b)
        fit = [sum(wi * xi for wi, xi in zip(w, x)) for x in X]
        rmse = (sum((f - v) ** 2 for f, v in zip(fit, yv)) / len(yv)) ** 0.5
        mean = sum(yv) / len(yv)
        ratio = sum(v for v in yv) / sum(d[y][0] for y in yrs)
        for k, wk in enumerate(w):
            out.append({"group": grp, "year_of_spending": k, "share": "%.4f" % wk,
                        "fit_years": "%d-%d" % SPEND_YEARS, "sum_of_shares": "%.4f" % sum(w),
                        "rmse_pct_of_mean_outlays": "%.2f" % (100 * rmse / mean),
                        "outlay_to_ba_ratio": "%.4f" % ratio})
    return ["group", "year_of_spending", "share", "fit_years", "sum_of_shares",
            "rmse_pct_of_mean_outlays", "outlay_to_ba_ratio"], out


def render(cols, rows):
    buf = io.StringIO()
    w = csv.DictWriter(buf, fieldnames=cols, lineterminator="\n", extrasaction="raise")
    w.writeheader()
    for r in rows:
        w.writerow({c: r.get(c, "") for c in cols})
    return buf.getvalue()


def build():
    files = {}
    tables = {}
    for out, (src, keep) in CBO_FILES.items():
        cols, rows = cbo_table(src, keep)
        tables[out] = rows
        files[out] = render(cols, rows)
    files["omb-outlays-by-function.csv"] = render(*omb_by_function("hist03z2.xlsx", "outlays"))
    files["omb-ba-by-function.csv"] = render(*omb_by_function("hist05z1.xlsx", "ba"))
    dcols, drows = omb_discretionary()
    files["omb-discretionary.csv"] = render(dcols, drows)
    files["spendout-discretionary.csv"] = render(*spendout(drows))
    files["deflators.csv"] = render(*deflators(tables["cbo-economic-historical.csv"],
                                               tables["cbo-economic.csv"],
                                               tables["cbo-long-term-economic.csv"]))
    return files


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true", help="compare with the committed files; write nothing")
    a = ap.parse_args()
    bad = 0
    for name, text in build().items():
        path = os.path.join(OUT, name)
        if a.check:
            old = open(path).read() if os.path.exists(path) else None
            if old != text:
                print("  CHANGED" if old else "  NEW", path); bad += 1
        else:
            with open(path, "w") as f:
                f.write(text)
            print("wrote", os.path.relpath(path, ROOT))
    sys.exit(1 if bad else 0)
