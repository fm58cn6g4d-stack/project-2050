#!/usr/bin/env python3
"""data.py: loader for the budget data layer (models/data/budget/).

Role: the one way later budget pieces (B3-B6) read budget series, and the only place they
convert units. Status: current (budget workflow piece B2). Standard library only.

  categories()              the category list (categories.csv), in order
  table(name)               a data-layer CSV as a list of row dicts (strings, as stored)
  cbo_series(cat)           {fiscal year: billions} for one category, CBO February 2026, unadjusted
  adopted_baseline()        the adopted baseline, rebuilt from the layer alone: the rows of
                            models/data/fiscal-baseline.csv, unrounded
  gdp()                     {fiscal year: billions}, the adopted baseline's nominal GDP
  deflator(index)           {fiscal year: index level}, "cpiu" or "gdp_price_index"
  omb_function(measure)     OMB actuals by function: {(year, code): billions}
  to_real(values, ...)      nominal -> real (constant) dollars       } the only conversions any
  to_pct_gdp(values)        nominal -> percent of GDP                 } later piece may use

Units everywhere: billions of nominal dollars by federal fiscal year, unless a name says
otherwise. The rebuild follows models/tools/fiscal-data.py step for step, in the same order
of floating-point operations, so that rounding to fiscal-baseline.csv's three decimals gives
the identical file. fiscal-data.py stays the canonical builder until piece B6 (Codex).
"""
import csv, os

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.normpath(os.path.join(HERE, "..", "..", "data", "budget"))

DEFAULT_INDEX = "gdp_price_index"   # proposed default deflator; an assumption for B1's register
DEFAULT_BASE_YEAR = 2026            # proposed default base year (dollars of FY2026); same

PERIODS = (  # (first year, last year, column of categories.csv, source label in the baseline)
    (1962, 2024, "cbo_historical", "actual"),
    (2025, 2036, "cbo_ten_year", "cbo-10yr"),
    (2037, 2056, "cbo_long_term", "cbo-lt"),
)
MISSING_IS_ZERO = {"mand_major_health_care", "mand_medicaid"}   # blank before the programs began
CATS_REV = ["rev_individual", "rev_payroll", "rev_corporate", "rev_customs", "rev_other"]
CATS_OUT = ["out_social_security", "out_medicare_net", "out_health_other", "out_other_mandatory",
            "out_disc_defense", "out_disc_nondefense", "out_net_interest"]
BASELINE_COLUMNS = (["year", "source", "gdp"] + CATS_REV + ["rev_total"] + CATS_OUT +
                    ["out_primary", "out_total", "deficit", "primary_deficit", "debt_public",
                     "implied_rate", "cbo_avg_rate", "note10", "bill3m", "adj_deficit",
                     "cbo_feb_deficit"])

_cache = {}


def table(name):
    """Rows of models/data/budget/<name> (with or without .csv), values as stored."""
    name = name if name.endswith(".csv") else name + ".csv"
    if name not in _cache:
        with open(os.path.join(DATA, name), newline="") as f:
            _cache[name] = list(csv.DictReader(f))
    return _cache[name]


def by_year(name):
    """{year: {variable: float}} for a wide data-layer file; blank cells are left out."""
    out = {}
    for r in table(name):
        out[int(r["year"])] = {k: float(v) for k, v in r.items()
                               if k not in ("year", "estimate_type", "source") and v not in ("", None)}
    return out


def categories(level=None):
    """The category list. level="baseline" gives the twelve that add up to the totals."""
    return [r for r in table("categories") if level in (None, r["level"])]


def _value(expr, row, done, year):
    """Evaluate 'a + b - c' left to right; names are data-layer variables or categories
    already computed for the year (done)."""
    toks = expr.split()
    total, sign = None, 1.0
    for t in toks:
        if t in "+-":
            sign = 1.0 if t == "+" else -1.0
            continue
        if t in done:
            v = done[t]
        elif t in row:
            v = row[t]
        elif t in MISSING_IS_ZERO:
            v = 0.0
        else:
            raise KeyError("FY%d: %s has no value" % (year, t))
        total = v if total is None else (total + v if sign > 0 else total - v)
    return total


def _cbo_rows():
    """CBO February 2026 baseline in the project's categories, FY1962-2056, before the FY2026
    actuals and post-February adjustments (the same steps as fiscal-data.py's build())."""
    if "_cbo_rows" in _cache:
        return _cache["_cbo_rows"]
    H, T, L = by_year("cbo-historical"), by_year("cbo-ten-year"), by_year("cbo-long-term")
    E = by_year("cbo-economic")
    cats = categories("baseline")
    rows = {}
    for y in range(1962, 2025):
        h = H[y]
        r = {"year": y, "source": "actual", "gdp": h["revenues"] / h["revenues_gdp_share"] * 100}
        for c in cats:
            r[c["category"]] = _value(c["cbo_historical"], h, r, y)
        r["debt_public"] = h["debt_held_by_public"]
        rows[y] = r
    for y in range(2025, 2037):
        t = T[y]
        r = {"year": y, "source": "actual" if y == 2025 else "cbo-10yr", "gdp": E[y]["gdp"]}
        for c in cats:
            r[c["category"]] = _value(c["cbo_ten_year"], t, r, y)
        r["debt_public"] = t["proj_debt_held_by_public"]
        r["cbo_avg_rate"] = t["proj_debt_avg_interest_rate"]
        r["note10"] = E[y].get("treasury_note_rate_10yr")
        r["bill3m"] = E[y].get("treasury_bill_rate_3mo")
        rows[y] = r
    d36 = rows[2036]
    dshare = d36["out_disc_defense"] / (d36["out_disc_defense"] + d36["out_disc_nondefense"])
    for y in range(2037, 2057):
        lt = L[y]
        g = lt["lt_gdp_trillions"] * 1000
        r = {"year": y, "source": "cbo-lt", "gdp": g}
        for c in cats:
            rule = c["cbo_long_term"].split(":")
            v = lt[rule[1]] / 100 * g
            if rule[0] == "gdp_share_split":
                v = v * dshare if rule[2] == "defense" else v * (1 - dshare)
            r[c["category"]] = v
        r["debt_public"] = lt["lt_debt_held_by_public_gdp_share"] / 100 * g
        rows[y] = r
    for y in sorted(rows):
        _totals(rows[y])
        if y - 1 in rows and rows[y - 1].get("debt_public"):
            rows[y]["implied_rate"] = 100 * rows[y]["out_net_interest"] / rows[y - 1]["debt_public"]
    _cache["_cbo_rows"] = rows
    return rows


def _totals(r):
    r["rev_total"] = sum(r[c] for c in CATS_REV)
    r["out_total"] = sum(r[c] for c in CATS_OUT)
    r["out_primary"] = r["out_total"] - r["out_net_interest"]
    r["deficit"] = r["out_total"] - r["rev_total"]
    r["primary_deficit"] = r["out_primary"] - r["rev_total"]


def cbo_series(category):
    """{year: billions} for one category of CBO's February 2026 baseline, unadjusted.
    Budget-authority detail rows come from the ten-year file only (FY2025-2036)."""
    c = next(x for x in categories() if x["category"] == category)
    if c["level"] == "baseline":
        return {y: r[category] for y, r in _cbo_rows().items()}
    T = by_year("cbo-ten-year")
    return {y: _value(c["cbo_ten_year"], T[y], {}, y) for y in sorted(T)}


def post_february():
    return table("post-february")


def adopted_baseline():
    """The adopted baseline (models/data/fiscal-baseline.csv), rebuilt from the layer alone:
    CBO's categories, then the FY2026 preliminary actuals, then the adjustment column.
    Returns {year: row dict}, unrounded."""
    rows = {y: dict(r) for y, r in _cbo_rows().items()}
    pf = post_february()
    act = {a["category"]: float(a["base"]) + float(a["change"]) if a["change"] else float(a["base"])
           for a in pf if a["kind"] == "fy2026_actual"}
    # FY2026 preliminary actuals: totals from CBO's Monthly Budget Review; categories scaled
    r = rows[2026]
    r["source"] = "actual-prelim"
    r["cbo_feb_deficit"] = r["deficit"]
    r["rev_customs"] = act["rev_customs"]
    other_rev = [c for c in CATS_REV if c != "rev_customs"]
    k = (act["rev_total"] - r["rev_customs"]) / sum(r[c] for c in other_rev)
    for c in other_rev:
        r[c] *= k
    r["out_net_interest"] = act["out_net_interest"]
    prim = [c for c in CATS_OUT if c != "out_net_interest"]
    k = (act["out_total"] - r["out_net_interest"]) / sum(r[c] for c in prim)
    for c in prim:
        r[c] *= k
    r["debt_public"] = act["debt_public"]
    _totals(r)
    # implied_rate is left as computed from CBO's February values, as fiscal-data.py does
    # adjustment column (+ raises the deficit)
    for y in rows:
        rows[y]["adj_deficit"] = 0.0
    for a in pf:
        if a["kind"] != "adjustment":
            continue
        amt, y0, y1 = float(a["base"]), int(a["year"]), int(a["year_end"])
        if a["rule"] == "one_time":
            rows[y0]["adj_deficit"] += -amt
            continue
        if a["rule"] != "gdp_spread":
            raise ValueError("unknown adjustment rule: " + a["rule"])
        gsum = sum(rows[y]["gdp"] for y in range(y0, y1 + 1))
        share = amt / gsum
        for y in range(y0, 2057):
            if y <= y1:
                f = 1.0
            else:
                f = max(0.5, 1 - 0.5 * (y - y1) / 10) if a["after"] == "fade_half_2046" else 1.0
            rows[y]["adj_deficit"] += -share * f * rows[y]["gdp"]
    return rows


def gdp():
    """{fiscal year: billions}: nominal GDP as the adopted baseline uses it (CBO historical
    FY1962-2024, CBO's fiscal-year economic projection FY2025-2036, the long-term budget
    file FY2037-2056)."""
    return {y: r["gdp"] for y, r in _cbo_rows().items()}


def deflator(index=DEFAULT_INDEX):
    """{fiscal year: level} from deflators.csv. CPI-U is in CBO's base (1982-84 = 100); the
    GDP price index in BEA's (calendar 2017 = 100)."""
    if index not in ("cpiu", "gdp_price_index"):
        raise ValueError("deflator index must be 'cpiu' or 'gdp_price_index'")
    return {int(r["year"]): float(r[index]) for r in table("deflators")}


def to_real(values, base_year=DEFAULT_BASE_YEAR, index=DEFAULT_INDEX):
    """Nominal {year: billions} -> {year: billions of base_year dollars} by the named deflator."""
    d = deflator(index)
    return {y: v * d[base_year] / d[y] for y, v in values.items()}


def to_pct_gdp(values):
    """Nominal {year: billions} -> {year: percent of GDP}, on the adopted baseline's GDP."""
    g = gdp()
    return {y: 100 * v / g[y] for y, v in values.items()}


def omb_function(measure="outlays", level="function"):
    """OMB Historical Tables 3.2 (outlays) or 5.1 (budget authority), actual years:
    {(year, code): billions}. Blank OMB cells (no amount) are left out."""
    name = {"outlays": "omb-outlays-by-function", "ba": "omb-ba-by-function"}[measure]
    return {(int(r["year"]), r["code"]): float(r[measure]) for r in table(name)
            if r["level"] == level and r[measure] != ""}


def baseline_csv_rows(rows=None):
    """Rows formatted exactly as fiscal-data.py writes fiscal-baseline.csv (three decimals)."""
    rows = rows or adopted_baseline()
    out = []
    for y in sorted(rows):
        r = rows[y]
        cells = []
        for c in BASELINE_COLUMNS:
            v = r.get(c, "")
            cells.append(v if isinstance(v, str) else ("" if v is None else str(round(v, 3))))
        out.append(cells)
    return out
