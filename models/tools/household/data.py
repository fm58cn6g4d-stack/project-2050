"""Load the household model's CPS extract and age it from the 2025 income year to a target year.

Role: the household model's data layer (`MODEL-CARD.md`, "Data" and assumption A-2). Status: working.

Aging is static: every record keeps its 2025 position, dollar amounts grow by type with CBO's February 2026
projections (wages per job, prices, investment income per household) and every weight grows with CBO's count of
households. Nothing about who lives where, works or marries changes.
"""
import csv
import gzip
import os

from params import uprating

DATA = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "data", "household")

UNIT_MONEY = {"wage_h": "wages", "wage_s": "wages", "se_h": "se", "se_s": "se", "interest": "interest",
              "dividends": "dividends", "rent": "rent", "capgain": "capgain", "pension": "pension", "ss": "ss",
              "ssi": "ssi", "tanf": "tanf", "uc": "uc", "vet": "vet", "disab_surv": "disab_surv", "other": "other",
              "child_support_rcvd": "child_support", "dep_wages": "dep_wages", "dep_other_income": "other",
              "premiums_paid": "premiums", "c_sttax": "state_tax", "ssi_dep": "ssi"}
SPM_MONEY = {"threshold": "threshold", "snap": "snap", "housing": "housing", "school_lunch": "school_lunch",
             "wic": "wic", "energy": "energy", "work_childcare": "work_childcare", "medical": "medical",
             "child_support_paid": "child_support_paid", "sttax": "state_tax",
             "childcare": "work_childcare"}
_CACHE = {}


def _read(name):
    if name not in _CACHE:
        with gzip.open(os.path.join(DATA, name), "rt", newline="") as f:
            rows = list(csv.DictReader(f))
        _CACHE[name] = [{k: (float(v) if "." in v else int(v)) for k, v in r.items()} for r in rows]
    return _CACHE[name]


def load(year=2025):
    """Tax units, SPM units and households for `year`, as lists of dicts (new copies each call)."""
    f = uprating(year)
    units = [dict(u) for u in _read("units.csv.gz")]
    spm = [dict(s) for s in _read("spm.csv.gz")]
    hhs = [dict(h) for h in _read("households.csv.gz")]
    if year != 2025:
        for u in units:
            for k, t in UNIT_MONEY.items():
                u[k] = u[k] * f[t]
            u["weight"] *= f["weight"]
        for s in spm:
            for k, t in SPM_MONEY.items():
                s[k] = s[k] * f[t]
            for k in ("weight", "w_people", "w_children", "w_18_64", "w_65"):
                s[k] *= f["weight"]
        for h in hhs:
            h["weight"] *= f["weight"]
            h["w_people"] *= f["weight"]
    return units, spm, hhs
