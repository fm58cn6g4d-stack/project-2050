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
INTAKE = os.path.join(ROOT, "library", "intake", "2026-11-08", "cbo")   # Espen's CBO uploads (read only)
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


def _sheet_part(z, name):
    """Worksheet part for a sheet name (the first sheet when name is None)."""
    if name is None:
        return "xl/worksheets/sheet1.xml"
    R = "{http://schemas.openxmlformats.org/officeDocument/2006/relationships}id"
    wb = ET.fromstring(z.read("xl/workbook.xml"))
    rid = [s.get(R) for s in wb.find("m:sheets", NS) if s.get("name") == name]
    if len(rid) != 1:
        raise SystemExit("%s: no sheet named %r" % (z.filename, name))
    rels = ET.fromstring(z.read("xl/_rels/workbook.xml.rels"))
    tgt = [r.get("Target") for r in rels if r.get("Id") == rid[0]][0]
    return tgt.lstrip("/") if tgt.startswith("/") else "xl/" + tgt


def xlsx_rows(path, sheet=None):
    z = zipfile.ZipFile(path)
    shared = []
    if "xl/sharedStrings.xml" in z.namelist():
        for si in ET.fromstring(z.read("xl/sharedStrings.xml")).findall("m:si", NS):
            shared.append("".join(t.text or "" for t in si.iter("{%s}t" % NS["m"])))
    sheet = ET.fromstring(z.read(_sheet_part(z, sheet)))
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
    "ground transportation": ("ground_transportation", "nondefense"),
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


SPENDING_DETAIL = "budget_spending_detail_annual_fy_2026-02.csv"   # CBO publication 51142


SPENDING_JUNE = "budget_spending_detail_annual_fy_2026-06.csv"   # extracted from Espen's upload
SPENDING_COLS = ["date", "tin", "title", "disc_or_mand", "category", "agency", "bureau",
                 "function_code", "subfunction_code", "off_budget", "budget_authority", "outlays"]


def spending_xlsx(fname, sheet):
    """CBO's Spending Projections by Budget Account workbook -> rows in cbo-data's
    spending_detail layout (one row per account and year, millions), text fields stripped."""
    rows = xlsx_rows(os.path.join(INTAKE, fname), sheet)
    hi = next(i for i, r in enumerate(rows) if r and (r[0] or "").startswith("Treasury Identification"))
    hdr = rows[hi]
    yc = [i for i, h in enumerate(hdr) if h and re.fullmatch(r"\d{4}(\.0)?", str(h).strip())]
    n = len(yc) // 2                        # budget authority block, then outlays block
    ba_c, out_c = yc[:n], yc[n:]
    years = [int(float(hdr[i])) for i in ba_c]
    if years != [int(float(hdr[i])) for i in out_c]:
        raise SystemExit("%s: budget authority and outlay years differ" % fname)
    out = []
    for r in rows[hi + 1:]:
        if not r or not re.match(r"\d{3}-\d{4}-", (r[0] or "").strip()):
            continue                         # notes and "Back to Table of Contents" lines
        r = r + [None] * (max(out_c) + 1 - len(r))
        txt = [(r[i] or "").strip() for i in range(9)]
        for y, b, o in zip(years, ba_c, out_c):
            out.append(dict(zip(SPENDING_COLS, ["FY%d" % y] + txt +
                                ["%s" % float(r[b] or 0), "%s" % float(r[o] or 0)])))
    order = {y: i for i, y in enumerate(years)}
    out.sort(key=lambda d: order[int(d["date"][2:])])   # cbo-data lists all accounts for a year, then the next
    return SPENDING_COLS, out


def spending_june_vs_february(june_rows):
    """June 2026 update (CBO publication 62385) against the February baseline the layer uses,
    by year, discretionary or mandatory and CBO category, in billions. Net interest is left out:
    the June file has no function 900 accounts."""
    with open(os.path.join(CBO, SPENDING_DETAIL), newline="") as f:
        feb_rows = list(csv.DictReader(f))
    S = {}
    for tag, src in (("feb", feb_rows), ("jun", june_rows)):
        for r in src:
            if r["function_code"] == "900":
                continue
            k = (int(r["date"][2:]), r["disc_or_mand"].lower(), r["category"])
            d = S.setdefault(k, {c: Decimal(0) for c in ("ba_feb", "ba_jun", "outlays_feb", "outlays_jun")})
            d["ba_" + tag] += Decimal(r["budget_authority"] or 0)
            d["outlays_" + tag] += Decimal(r["outlays"] or 0)
    b = lambda v: format((v / 1000).normalize(), "f") if v else "0"
    rows = [{"year": k[0], "disc_or_mand": k[1], "category": k[2], **{c: b(v) for c, v in d.items()},
             "outlays_change": b(d["outlays_jun"] - d["outlays_feb"])} for k, d in sorted(S.items())]
    return ["year", "disc_or_mand", "category", "ba_feb", "ba_jun", "outlays_feb", "outlays_jun",
            "outlays_change"], rows


def cbo_spending_by_function():
    """CBO's Spending Projections by Budget Account (February 2026 baseline), summed over
    accounts by year, discretionary or mandatory, CBO category and budget function. Millions
    become billions exactly. outlays_without_ba is the outlays of accounts with zero budget
    authority in that year (chiefly highway, transit and airport grants under obligation
    limitations, whose contract authority is mandatory)."""
    S = {}
    with open(os.path.join(CBO, SPENDING_DETAIL), newline="") as f:
        for r in csv.DictReader(f):
            k = (int(r["date"].replace("FY", "")), r["disc_or_mand"].lower(), r["category"], r["function_code"])
            d = S.setdefault(k, {"accounts": 0, "ba": Decimal(0), "outlays": Decimal(0), "nob": Decimal(0)})
            ba, out = Decimal(r["budget_authority"] or 0), Decimal(r["outlays"] or 0)
            d["accounts"] += 1; d["ba"] += ba; d["outlays"] += out
            if ba == 0:
                d["nob"] += out
    b = lambda v: format((v / 1000).normalize(), "f") if v else "0"
    rows = [{"year": k[0], "disc_or_mand": k[1], "category": k[2], "function_code": k[3],
             "accounts": d["accounts"], "ba": b(d["ba"]), "outlays": b(d["outlays"]),
             "outlays_without_ba": b(d["nob"])} for k, d in sorted(S.items())]
    return ["year", "disc_or_mand", "category", "function_code", "accounts", "ba", "outlays",
            "outlays_without_ba"], rows


CA_FUNCTION = "400"          # transportation
CA_GROUPS = {"Federal Highway Administration": "highway_transit", "Federal Transit Administration": "highway_transit",
             "National Highway Traffic Safety Administration": "highway_transit",
             "Federal Motor Carrier Safety Administration": "highway_transit",
             "Federal Aviation Administration": "airports"}


def cbo_contract_authority():
    """Contract authority under obligation limitations, from CBO's account file: transportation
    (function 400) accounts with discretionary outlays and no discretionary budget authority in
    any year, whose budget authority CBO records as mandatory under the same account. By year
    and group (highway_transit: the Highway Trust Fund's FHWA, FTA, NHTSA and FMCSA accounts;
    airports: FAA's grants-in-aid): accounts, mandatory contract authority, discretionary
    outlays, and their ratio. Millions become billions exactly."""
    rows = []
    with open(os.path.join(CBO, SPENDING_DETAIL), newline="") as f:
        rows = list(csv.DictReader(f))
    dba, dout, mba = collections.Counter(), collections.Counter(), collections.Counter()
    bureau = {}
    for r in rows:
        if r["function_code"] != CA_FUNCTION:
            continue
        ba, out = Decimal(r["budget_authority"] or 0), Decimal(r["outlays"] or 0)
        if r["disc_or_mand"] == "Discretionary":
            dba[r["tin"]] += abs(ba); dout[r["tin"]] += out; bureau[r["tin"]] = r["bureau"]
        else:
            mba[r["tin"]] += ba
    sel = {t for t in dout if dba[t] == 0 and dout[t] > 0 and mba[t] > 0}
    unknown = sorted(bureau[t] for t in sel if bureau[t] not in CA_GROUPS)
    if unknown:
        raise ValueError("contract-authority accounts with no group: %s" % unknown)
    S = {}
    for r in rows:
        if r["tin"] not in sel:
            continue
        k = (int(r["date"].replace("FY", "")), CA_GROUPS[bureau[r["tin"]]])
        d = S.setdefault(k, {"tins": set(), "ca": Decimal(0), "outlays": Decimal(0)})
        d["tins"].add(r["tin"])
        if r["disc_or_mand"] == "Discretionary":
            d["outlays"] += Decimal(r["outlays"] or 0)
        else:
            d["ca"] += Decimal(r["budget_authority"] or 0)
    b = lambda v: format((v / 1000).normalize(), "f") if v else "0"
    out = [{"year": k[0], "group": k[1], "accounts": len(d["tins"]), "contract_authority": b(d["ca"]),
            "outlays": b(d["outlays"]), "ca_to_outlays": "%.4f" % (d["ca"] / d["outlays"])}
           for k, d in sorted(S.items())]
    return ["year", "group", "accounts", "contract_authority", "outlays", "ca_to_outlays"], out
CAL_YEARS = (2029, 2036)   # calibration years: CBO's account projections start in FY2026, the fit needs three earlier years


def _fit(pairs, years):
    """Least-squares shares w_k, k = 0..LAGS-1, with outlays(t) = sum_k w_k * BA(t-k)."""
    X = [[pairs[y - k][0] for k in range(LAGS)] for y in years]
    yv = [pairs[y][1] for y in years]
    A = [[sum(x[i] * x[j] for x in X) for j in range(LAGS)] for i in range(LAGS)]
    b = [sum(x[i] * v for x, v in zip(X, yv)) for i in range(LAGS)]
    return solve(A, b)


def _err(w, pairs, years):
    fit = [sum(w[k] * pairs[y - k][0] for k in range(len(w))) for y in years]
    yv = [pairs[y][1] for y in years]
    return 100 * (sum((f - v) ** 2 for f, v in zip(fit, yv)) / len(yv)) ** 0.5 / (sum(yv) / len(yv))


# CBO's own spend-out of one year's regular defense budget authority: the base-budget (regular
# appropriations) line of three CBO cost estimates of National Defense Authorization Acts, which
# CBO says it estimates "using historical spend-out rates". Millions of dollars: the authorization
# level for the act's first year, and CBO's estimated outlays from it in years 1-5. Read through
# the Exa search tool's page reader on November 12, 2026 (www.cbo.gov's bot check blocks direct
# downloads; Espen allowed this route on November 8); cited, not saved.
CBO_DEFENSE_ACTS = {
    "FY2014": ("SRC-2454", 544478, (347627, 115466, 42699, 18950, 7933)),     # S. 1197, Table 1
    "FY2017": ("SRC-2455", 543234, (335887, 119350, 44058, 20248, 9030)),     # H.R. 4909, Table 1
    "FY2023": ("SRC-2456", 838789, (484281, 206029, 68655, 34954, 14960)),    # H.R. 7900, Table 1
}
DEFENSE_CHECK_YEARS = (2030, 2036)   # five shares need four earlier years of CBO budget authority (FY2026 on)


def defense_act_shares():
    """The average of CBO's year-by-year spend-out of the three acts' new budget authority:
    five shares, years of spending 0-4, every one positive. The part not spent in five years
    (about 3%) is left out, as CBO's five-year tables leave it out."""
    per = [[o / ba for o in out] for _, ba, out in CBO_DEFENSE_ACTS.values()]
    return [sum(p[k] for p in per) / len(per) for k in range(len(per[0]))]


def spendout_cbo(disc_rows, by_function):
    """Spend-out of discretionary budget authority, by group, checked against CBO's projections.

    Defense: CBO's own rates, the average of its spend-out of three regular defense acts
    (CBO_DEFENSE_ACTS), used as they are: no fit and no scaling to CBO's baseline, so CBO's
    projected outlays test the shares instead of setting them. (Until November 12, 2026 defense
    used a four-year least-squares fit to OMB's FY1993-2019 totals, scaled to CBO's outlays; its
    fourth share was negative, -4.3%. The fit cannot tell the years apart well, because budget
    authority in neighboring years moves together.) history_share keeps that fit for comparison.

    Nondefense: timing (the shape of the shares) from OMB's history, FY1993-2019, as in
    spendout(), with ground transportation taken out of both budget authority and outlays,
    because most of its outlays rest on mandatory contract authority. The shares are then scaled
    by one factor so that, applied to CBO's projected discretionary budget authority (account
    file, FY2026-2036), they reproduce CBO's projected outlays over CAL_YEARS. CBO's outlays
    leave out accounts with no budget authority in the year (outlays_without_ba: highway, transit
    and airport grants above all), which have no budget authority to spend out and are carried
    as outlays on their own. All four nondefense shares are positive."""
    H = collections.defaultdict(dict)
    for r in disc_rows:
        if r["ba"] and r["outlays"]:
            H[r["program"]][r["year"]] = (float(r["ba"]), float(r["outlays"]))
    hist = {"defense": H["defense_total"],
            "nondefense": {y: (v[0] - H["ground_transportation"][y][0], v[1] - H["ground_transportation"][y][1])
                           for y, v in H["nondefense_total"].items() if y in H["ground_transportation"]}}
    C = {"defense": collections.defaultdict(lambda: [0.0, 0.0]), "nondefense": collections.defaultdict(lambda: [0.0, 0.0])}
    for r in by_function:
        if r["disc_or_mand"] != "discretionary":
            continue
        g = r["category"].lower()
        c = C[g][int(r["year"])]
        c[0] += float(r["ba"])
        c[1] += float(r["outlays"]) - (float(r["outlays_without_ba"]) if g == "nondefense" else 0.0)
    hy = range(SPEND_YEARS[0], SPEND_YEARS[1] + 1)
    out = []
    for g in ("defense", "nondefense"):
        w = _fit(hist[g], hy)
        cbo = {y: tuple(v) for y, v in C[g].items()}
        if g == "defense":
            ws = defense_act_shares()
            scale, cal, cy = 1.0, "none", range(DEFENSE_CHECK_YEARS[0], DEFENSE_CHECK_YEARS[1] + 1)
            timing = "CBO's spend-out of the FY2014, FY2017 and FY2023 defense acts (%s)" % ", ".join(
                v[0] for v in CBO_DEFENSE_ACTS.values())
        else:
            cy = range(CAL_YEARS[0], CAL_YEARS[1] + 1)
            fit = sum(sum(w[k] * cbo[y - k][0] for k in range(LAGS)) for y in cy)
            scale = sum(cbo[y][1] for y in cy) / fit
            ws = [x * scale for x in w]
            cal = "%d-%d" % CAL_YEARS
            timing = "OMB history, FY%d-%d, scaled to CBO's outlays" % SPEND_YEARS
        for k in range(len(ws)):
            out.append({"group": g, "year_of_spending": k, "share": "%.4f" % ws[k],
                        "history_share": "%.4f" % w[k] if k < LAGS else "", "scale": "%.4f" % scale,
                        "sum_of_shares": "%.4f" % sum(ws), "timing": timing, "history_years": "%d-%d" % SPEND_YEARS,
                        "calibration_years": cal, "check_years": "%d-%d" % (cy[0], cy[-1]),
                        "history_rmse_pct": "%.2f" % _err(w, hist[g], hy),
                        "check_rmse_pct": "%.2f" % _err(ws, cbo, cy)})
    return ["group", "year_of_spending", "share", "history_share", "scale", "sum_of_shares", "timing",
            "history_years", "calibration_years", "check_years", "history_rmse_pct", "check_rmse_pct"], out


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
    sf_cols, sf_rows = cbo_spending_by_function()
    files["cbo-spending-by-function.csv"] = render(sf_cols, sf_rows)
    files["spendout-discretionary-cbo.csv"] = render(*spendout_cbo(drows, sf_rows))
    files["cbo-contract-authority.csv"] = render(*cbo_contract_authority())
    jcols, jrows = spending_xlsx("51142-2026-06-Spending-Projections.xlsx", "1. Updated Spending Projections")
    files[os.path.join("..", "cbo", SPENDING_JUNE)] = render(jcols, jrows)    # a cache file, like CBO's own CSVs
    files["cbo-spending-2026-06-vs-02.csv"] = render(*spending_june_vs_february(jrows))
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
