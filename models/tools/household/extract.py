#!/usr/bin/env python3
"""Build the household model's compact extract from the CPS ASEC 2026 public-use archive.

Role: the household model's data step (`MODEL-CARD.md`, "Data"). Status: working.

Reads the official Census archive (income year 2025), checks its SHA-256, and writes three small,
deterministic gzip CSVs to `models/data/household/`:
  * `units.csv.gz`: one row per tax unit (Census TAX_ID within a household), the filer's and spouse's
    ages and earnings, the unit's other income by type, its dependents by age, health coverage counts and
    the Census tax model's own figures (kept for benchmarking);
  * `spm.csv.gz`: one row per SPM unit, the Census SPM resource elements, threshold and person weights
    by age group;
  * `households.csv.gz`: one row per household, its weight, state and size.

The archive is not committed (it is 139 MB); the extract is, so the model and its tests run in the checks
without it. CPS public-use data are U.S. government works. Run from the repository root:

  python3 models/tools/household/extract.py --archive /path/to/asecpub26csv.zip

Source: https://www2.census.gov/programs-surveys/cps/datasets/2026/march/asecpub26csv.zip
"""
import argparse
import csv
import gzip
import hashlib
import io
import os
import zipfile
from collections import defaultdict

SOURCE_URL = "https://www2.census.gov/programs-surveys/cps/datasets/2026/march/asecpub26csv.zip"
SHA256 = "fe819d0d2fc4470c282e76c247b8aa8b6054811619730307e9f2fe6186707d93"
OUT = os.path.join(os.path.dirname(__file__), "..", "..", "data", "household")

PERSON_COLS = [
    "PH_SEQ", "A_LINENO", "A_AGE", "TAX_ID", "DEP_STAT", "FILESTAT", "MARSUPWT", "SPM_ID", "A_ENRLW",
    "WSAL_VAL", "SEMP_VAL", "FRSE_VAL", "INT_VAL", "DIV_VAL", "RNT_VAL", "CAP_VAL", "PNSN_VAL", "ANN_VAL",
    "SS_VAL", "SSI_VAL", "PAW_VAL", "UC_VAL", "VET_VAL", "DIS_VAL1", "DIS_VAL2", "SUR_VAL1", "SUR_VAL2",
    "OI_VAL", "CSP_VAL", "ED_VAL", "FIN_VAL", "CHSP_VAL", "PTOTVAL",
    "AGI", "FEDTAX_BC", "FEDTAX_AC", "EIT_CRED", "CTC_CRD", "ACTC_CRD", "FICA", "STATETAX_A",
    "NOW_MCAID", "NOW_MCARE", "NOW_GRP", "NOW_MRK", "PHIP_VAL",
    "SPM_WEIGHT", "SPM_NUMPER", "SPM_NUMKIDS", "SPM_NUMADULTS", "SPM_POVTHRESHOLD", "SPM_RESOURCES",
    "SPM_TOTVAL", "SPM_SNAPSUB", "SPM_CAPHOUSESUB", "SPM_SCHLUNCH", "SPM_WICVAL", "SPM_ENGVAL",
    "SPM_FEDTAX", "SPM_FEDTAXBC", "SPM_EITC", "SPM_ACTC", "SPM_FICA", "SPM_STTAX", "SPM_CAPWKCCXPNS",
    "SPM_CHILDCAREXPNS",
    "SPM_MEDXPNS", "SPM_CHILDSUPPD", "SPM_POOR", "SPM_TENMORTSTATUS",
    "HRSWK", "WKSWORK", "PRDISFLG",
]
HH_COLS = ["H_SEQ", "HSUP_WGT", "GESTFIPS", "H_NUMPER", "H_TENURE"]

UNIT_FIELDS = [
    "hh", "tid", "spm", "weight", "filestat", "age_h", "age_s", "wage_h", "wage_s", "se_h", "se_s",
    "interest", "dividends", "rent", "capgain", "pension", "ss", "ssi", "tanf", "uc", "vet", "disab_surv",
    "other", "child_support_rcvd", "dep_wages", "dep_other_income",
    "n_people", "n_dep", "n_dep_u6", "n_dep_6_16", "n_dep_17", "n_dep_18", "n_dep_19_23_student", "n_dep_other",
    "n_age65", "n_medicaid", "n_medicare", "n_employer_cov", "n_marketplace", "premiums_paid",
    "c_agi", "c_fedtax_bc", "c_fedtax_ac", "c_eitc", "c_ctc", "c_actc", "c_fica", "c_sttax",
    "n_dep_u5", "n_dep_5_12", "ssi_dep", "n_ssi", "n_ssi_earn", "n_ssi_unearned",
]
SPM_FIELDS = [
    "spm", "hh", "weight", "numper", "numkids", "numadults", "threshold", "resources", "totval", "snap",
    "housing", "school_lunch", "wic", "energy", "fedtax", "fedtax_bc", "eitc", "actc", "fica", "sttax",
    "work_childcare", "medical", "child_support_paid", "poor", "tenure",
    "w_people", "w_children", "w_18_64", "w_65",
    "n_abawd_prior", "n_abawd_55_64", "n_parent_child14", "elderly_or_disabled", "childcare"]
HH_FIELDS = ["hh", "weight", "state", "numper", "tenure", "w_people"]


def i(x):
    return int(float(x)) if x not in ("", None) else 0


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for block in iter(lambda: f.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()


def rows(zf, member, cols):
    with zf.open(member) as raw:
        r = csv.reader(io.TextIOWrapper(raw, encoding="latin-1", newline=""))
        head = next(r)
        idx = [head.index(c) for c in cols]
        for line in r:
            yield {c: line[k] for c, k in zip(cols, idx)}


def build(archive):
    got = sha256(archive)
    if got != SHA256:
        raise SystemExit(f"archive hash {got} is not the recorded {SHA256}")
    zf = zipfile.ZipFile(archive)
    people = defaultdict(list)          # (hh, tid) -> person dicts
    spm = {}
    hh_people = defaultdict(float)
    for p in rows(zf, "pppub26.csv", PERSON_COLS):
        people[(i(p["PH_SEQ"]), i(p["TAX_ID"]))].append(p)
        hh_people[i(p["PH_SEQ"])] += i(p["MARSUPWT"]) / 100
        s = i(p["SPM_ID"])
        if s not in spm:
            spm[s] = {"spm": s, "hh": i(p["PH_SEQ"]), "weight": i(p["SPM_WEIGHT"]) / 100,
                      "numper": i(p["SPM_NUMPER"]), "numkids": i(p["SPM_NUMKIDS"]),
                      "numadults": i(p["SPM_NUMADULTS"]), "threshold": i(p["SPM_POVTHRESHOLD"]),
                      "resources": i(p["SPM_RESOURCES"]), "totval": i(p["SPM_TOTVAL"]),
                      "snap": i(p["SPM_SNAPSUB"]), "housing": i(p["SPM_CAPHOUSESUB"]),
                      "school_lunch": i(p["SPM_SCHLUNCH"]), "wic": i(p["SPM_WICVAL"]),
                      "energy": i(p["SPM_ENGVAL"]), "fedtax": i(p["SPM_FEDTAX"]),
                      "fedtax_bc": i(p["SPM_FEDTAXBC"]), "eitc": i(p["SPM_EITC"]), "actc": i(p["SPM_ACTC"]),
                      "fica": i(p["SPM_FICA"]), "sttax": i(p["SPM_STTAX"]),
                      "work_childcare": i(p["SPM_CAPWKCCXPNS"]), "medical": i(p["SPM_MEDXPNS"]),
                      "childcare": i(p["SPM_CHILDCAREXPNS"]),
                      "child_support_paid": i(p["SPM_CHILDSUPPD"]), "poor": i(p["SPM_POOR"]),
                      "tenure": i(p["SPM_TENMORTSTATUS"]),
                      "w_people": 0.0, "w_children": 0.0, "w_18_64": 0.0, "w_65": 0.0}
        u = spm[s]; w = i(p["MARSUPWT"]) / 100; a = i(p["A_AGE"])
        u["w_people"] += w
        u["w_children" if a < 18 else ("w_65" if a >= 65 else "w_18_64")] += w

    # SNAP's work rule (P.L. 119-21 sec. 10102), counted per SPM unit: adults not disabled who worked under 20 hours
    # a week on average last year, by the group the rule reaches (`snap2025.py`)
    members = defaultdict(list)
    for ps in people.values():
        for p in ps:
            members[i(p["SPM_ID"])].append(p)
    for sid, ms in members.items():
        ages = [i(p["A_AGE"]) for p in ms]
        kids = [a for a in ages if a < 18]
        u = spm[sid]
        u["n_abawd_prior"] = u["n_abawd_55_64"] = u["n_parent_child14"] = 0
        u["elderly_or_disabled"] = int(any(a >= 60 for a in ages) or any(i(p["PRDISFLG"]) == 1 for p in ms))
        for p, a in zip(ms, ages):
            if i(p["PRDISFLG"]) == 1 or not 18 <= a <= 64:
                continue
            if max(i(p["HRSWK"]), 0) * max(i(p["WKSWORK"]), 0) / 52 >= 20:
                continue
            if not kids:
                u["n_abawd_prior" if a <= 54 else "n_abawd_55_64"] += 1
            elif min(kids) >= 14:
                u["n_parent_child14"] += 1

    units = []
    for (hh, tid), ps in people.items():
        ps.sort(key=lambda p: i(p["A_LINENO"]))
        filers = [p for p in ps if i(p["DEP_STAT"]) == 0]
        deps = [p for p in ps if i(p["DEP_STAT"]) != 0]
        if not filers:                          # every Census tax unit has a filer; guard all the same
            filers, deps = deps[:1], deps[1:]
        h = filers[0]; s = filers[1] if len(filers) > 1 else None
        adults = filers[:2]
        extra = filers[2:]                      # never seen in the 2026 file; counted with dependents' income
        def tot(cols, group):
            return sum(i(p[c]) for p in group for c in cols)
        u = {"hh": hh, "tid": tid, "spm": i(h["SPM_ID"]), "weight": i(h["MARSUPWT"]) / 100,
             "filestat": i(h["FILESTAT"]), "age_h": i(h["A_AGE"]), "age_s": i(s["A_AGE"]) if s else -1,
             "wage_h": i(h["WSAL_VAL"]), "wage_s": i(s["WSAL_VAL"]) if s else 0,
             "se_h": i(h["SEMP_VAL"]) + i(h["FRSE_VAL"]),
             "se_s": (i(s["SEMP_VAL"]) + i(s["FRSE_VAL"])) if s else 0,
             "interest": tot(["INT_VAL"], adults), "dividends": tot(["DIV_VAL"], adults),
             "rent": tot(["RNT_VAL"], adults), "capgain": tot(["CAP_VAL"], adults),
             "pension": tot(["PNSN_VAL", "ANN_VAL"], adults), "ss": tot(["SS_VAL"], adults),
             "ssi": tot(["SSI_VAL"], adults), "tanf": tot(["PAW_VAL"], adults), "uc": tot(["UC_VAL"], adults),
             "vet": tot(["VET_VAL"], adults),
             "disab_surv": tot(["DIS_VAL1", "DIS_VAL2", "SUR_VAL1", "SUR_VAL2"], adults),
             "other": tot(["OI_VAL", "ED_VAL", "FIN_VAL"], adults),
             "child_support_rcvd": tot(["CSP_VAL"], adults),
             "dep_wages": tot(["WSAL_VAL", "SEMP_VAL", "FRSE_VAL"], deps + extra),
             "dep_other_income": sum(i(p["PTOTVAL"]) for p in deps + extra)
                                 - tot(["WSAL_VAL", "SEMP_VAL", "FRSE_VAL"], deps + extra),
             "n_people": len(ps), "n_dep": len(deps),
             "n_dep_u6": sum(i(p["A_AGE"]) < 6 for p in deps),
             "n_dep_6_16": sum(6 <= i(p["A_AGE"]) <= 16 for p in deps),
             "n_dep_17": sum(i(p["A_AGE"]) == 17 for p in deps),
             "n_dep_18": sum(i(p["A_AGE"]) == 18 for p in deps),
             "n_dep_19_23_student": sum(19 <= i(p["A_AGE"]) <= 23 and i(p["A_ENRLW"]) == 1 for p in deps),
             "n_age65": sum(i(p["A_AGE"]) >= 65 for p in adults),
             "n_medicaid": sum(i(p["NOW_MCAID"]) == 1 for p in ps),
             "n_medicare": sum(i(p["NOW_MCARE"]) == 1 for p in ps),
             "n_employer_cov": sum(i(p["NOW_GRP"]) == 1 for p in ps),
             "n_marketplace": sum(i(p["NOW_MRK"]) == 1 for p in ps),
             "premiums_paid": tot(["PHIP_VAL"], ps),
             "c_agi": i(h["AGI"]), "c_fedtax_bc": i(h["FEDTAX_BC"]), "c_fedtax_ac": i(h["FEDTAX_AC"]),
             "c_eitc": i(h["EIT_CRED"]), "c_ctc": i(h["CTC_CRD"]), "c_actc": i(h["ACTC_CRD"]),
             "c_fica": tot(["FICA"], ps), "c_sttax": i(h["STATETAX_A"]),
             # for the secure floor's rules (`rules.py`): the care credit's children (under 13) and the child care
             # guarantee's (under 5); SSI received by dependents (children's SSI), and SSI recipients among the
             # head and spouse with earnings or with other unearned income (INC-3.02's exclusions)
             "n_dep_u5": sum(i(p["A_AGE"]) < 5 for p in deps),
             "n_dep_5_12": sum(5 <= i(p["A_AGE"]) <= 12 for p in deps),
             "ssi_dep": tot(["SSI_VAL"], deps + extra),
             "n_ssi": sum(i(p["SSI_VAL"]) > 0 for p in ps),
             "n_ssi_earn": sum(i(p["SSI_VAL"]) > 0 and i(p["WSAL_VAL"]) + i(p["SEMP_VAL"]) + i(p["FRSE_VAL"]) > 0
                               for p in ps),
             "n_ssi_unearned": sum(i(p["SSI_VAL"]) > 0 and i(p["PTOTVAL"]) - i(p["SSI_VAL"]) - i(p["WSAL_VAL"])
                                   - i(p["SEMP_VAL"]) - i(p["FRSE_VAL"]) > 0 for p in ps)}
        u["n_dep_other"] = (u["n_dep"] - u["n_dep_u6"] - u["n_dep_6_16"] - u["n_dep_17"] - u["n_dep_18"]
                            - u["n_dep_19_23_student"])
        units.append(u)
    units.sort(key=lambda u: (u["hh"], u["tid"]))

    hhs = []
    for h in rows(zf, "hhpub26.csv", HH_COLS):
        if i(h["H_NUMPER"]) == 0:              # vacant or non-interview records carry no people
            continue
        k = i(h["H_SEQ"])
        hhs.append({"hh": k, "weight": i(h["HSUP_WGT"]) / 100, "state": i(h["GESTFIPS"]),
                    "numper": i(h["H_NUMPER"]), "tenure": i(h["H_TENURE"]), "w_people": hh_people[k]})
    hhs.sort(key=lambda h: h["hh"])
    return units, sorted(spm.values(), key=lambda s: s["spm"]), hhs


def fmt(v):
    if isinstance(v, float):
        return f"{v:.2f}".rstrip("0").rstrip(".")
    return str(v)


def write(path, fields, data):
    buf = io.StringIO()
    w = csv.writer(buf, lineterminator="\n")
    w.writerow(fields)
    for d in data:
        w.writerow([fmt(d[f]) for f in fields])
    with open(path, "wb") as f, gzip.GzipFile(fileobj=f, mode="wb", mtime=0, filename="") as g:
        g.write(buf.getvalue().encode())


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--archive", required=True)
    ap.add_argument("--out", default=OUT)
    a = ap.parse_args()
    units, spm, hhs = build(a.archive)
    os.makedirs(a.out, exist_ok=True)
    write(os.path.join(a.out, "units.csv.gz"), UNIT_FIELDS, units)
    write(os.path.join(a.out, "spm.csv.gz"), SPM_FIELDS, spm)
    write(os.path.join(a.out, "households.csv.gz"), HH_FIELDS, hhs)
    print(f"{len(units)} tax units, {len(spm)} SPM units, {len(hhs)} households written to {a.out}")


if __name__ == "__main__":
    main()
