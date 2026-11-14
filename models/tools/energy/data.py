"""MOD-energy's data layer: reads the public data the model is benchmarked and based on, from the library's text versions.

Role: one home per fact. Every series here is read from a file `library/fetch_public.py` saved under its official address
(header: source, retrieval date, SHA-256), so a value can be traced to its source line. Nothing is typed in by hand except
EIA's measured 2025 table, which `test_energy.py` checks against the saved text.
"""
import json, os, re

ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", ".."))
TEXT = os.path.join(ROOT, "library", "text")

# AEO2026 table 18 (energy CO2 by sector, Mt), two cases. The combination case (electrnp) drops EPA's 2024 power plant and
# vehicle rules, so it is the public projection nearest the January 2029 law (survey.md, 2.2).
AEO = {"combination": ("m4-eia-aeo2026-tab18-combination.txt", "SRC-5049"),
       "counterfactual": ("m4-eia-aeo2026-tab18-counterfactual.txt", "SRC-5050")}
AEO_SECTORS = {"residential": "ba_Direct", "commercial": "ca_Direct", "industry": "da_Direct", "transport": "ea_Direct",
               "power": "fa_Total", "total": "ga_Total"}


def _cells(path):
    """{row number: [cell, ...]} in sheet order, from a fetch_public.py workbook text ("row N | header = value")."""
    rows = {}
    with open(path, encoding="utf-8") as f:
        body = f.read().split("\n---\n", 1)[1]
    for line in body.splitlines():
        m = re.match(r"row (\d+) \|[^=]*= ?(.*)$", line)
        if m:
            rows.setdefault(int(m.group(1)), []).append(m.group(2).strip())
    return rows


def aeo_table18(case):
    """{sector: {year: Mt}} for an AEO2026 table 18 case, sectors as AEO_SECTORS (residential and commercial are direct)."""
    rows = _cells(os.path.join(TEXT, AEO[case][0]))
    head = next(v for v in rows.values() if v and v[0] == "Sector and Source")
    years = [int(x) for x in head[1:] if re.fullmatch(r"\d{4}", x)]
    keyed = {}
    for v in rows.values():
        if v and v[0].startswith("TCE000:"):
            nums = [float(x) for x in v[2:2 + len(years)]]
            keyed[v[0][7:]] = dict(zip(years, nums))
    out = {s: keyed[k] for s, k in AEO_SECTORS.items()}
    out["buildings"] = {y: out["residential"][y] + out["commercial"][y] for y in years}
    return out


# EIA, U.S. Energy-Related Carbon Dioxide Emissions, 2025 (SRC-5004), table 1, Mt CO2. Measured data.
EIA_2025 = {"residential": 331, "commercial": 256, "industry": 960, "transport": 1871, "power": 1485, "total": 4904}
EIA_2025_SRC = ("m4-eia-energy-co2-2025.txt", "SRC-5004")

# EPA inventory 1990-2023 (SRC-4460): net 2005, the goals' base (EPA Table ES-2; carried in the carbon model as 6,536).
EPA_NET_2005 = 6536.4


def degree_days(kind):
    """{May-April year ending: degree days} from NOAA Climate at a Glance, contiguous U.S. (SRC-5047 heating, SRC-5048 cooling)."""
    slug = {"heating": "m4-noaa-cag-us-heating-degree-days.txt", "cooling": "m4-noaa-cag-us-cooling-degree-days.txt"}[kind]
    with open(os.path.join(TEXT, slug), encoding="utf-8") as f:
        d = json.loads(f.read().split("\n---\n", 1)[1])["data"]
    return {int(k[:4]): v["value"] for k, v in d.items()}


def weather_2025():
    """2025's heating and cooling degree days against their 2015-2024 average (NOAA's May-April years ending 2025 and 2026
    split the calendar year; their mean stands for calendar 2025). A ratio above 1 means more heating or cooling than normal."""
    out = {}
    for kind in ("heating", "cooling"):
        d = degree_days(kind)
        y25 = (d[2025] + d[2026]) / 2
        normal = sum((d[y] + d[y + 1]) / 2 for y in range(2015, 2025)) / 10
        out[kind] = {"2025": y25, "normal_2015_2024": round(normal, 1), "ratio": round(y25 / normal, 4)}
    return out
