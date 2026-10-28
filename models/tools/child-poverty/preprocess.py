#!/usr/bin/env python3
"""Auditable CSV/ZIP CPS-to-model constructor; no guessed eligibility or taxes.

Baseline-only use needs no tax/ID/delivery imputations. A policy run needs a
separate reviewed overlay. Field names/scales are explicit by source vintage.
"""
import argparse
import csv
import io
import math
import zipfile
from collections import defaultdict
from pathlib import Path
from model import load_json, write_json, sha256, num, validate_population


def csv_rows(path, member=None):
    if zipfile.is_zipfile(path):
        with zipfile.ZipFile(path) as z:
            names = [n for n in z.namelist() if n.lower().endswith(".csv")]
            if member is None:
                if len(names) != 1:
                    raise ValueError("ZIP contains multiple CSVs; name the person-file --member explicitly")
                member = names[0]
            if member not in names:
                raise ValueError("selected CSV member not present")
            with z.open(member) as f:
                yield from csv.DictReader(io.TextIOWrapper(f, encoding="utf-8-sig", newline=""))
    else:
        with open(path, encoding="utf-8-sig", newline="") as f:
            yield from csv.DictReader(f)


def extract(row, mapping, key, numeric=True):
    spec = mapping.get(key)
    if not isinstance(spec, dict) or not spec.get("column"):
        raise ValueError(f"field map for {key} required")
    column = spec["column"]
    if column not in row or row[column].strip() == "":
        raise ValueError(f"missing field {column} for {key}")
    if not numeric:
        return row[column].strip()
    if spec.get("scale") is None:
        raise ValueError(f"explicit scale for {key} required; do not guess weight decimals")
    scale = num(spec["scale"], f"{key} scale", 0)
    if scale == 0:
        raise ValueError("scale must be positive")
    return num(row[column], column) * scale


def same(a, b):
    return math.isclose(a, b, abs_tol=.005, rel_tol=1e-10) if isinstance(a, (int, float)) else a == b


def construct(rows, config, replicate_rows=None):
    metadata = dict(config["metadata"])
    fields = config["fields"]
    spm_fields = config.get("unit_fields", {})
    units, people, tax_observations = {}, {}, defaultdict(list)
    tax_spm = {}
    # Separate files join by household/person keys. Never by row position.
    reps_by_person = {}
    rep_fields = config.get("replicate_columns", [])
    if rep_fields and len(rep_fields) != 160 and metadata["kind"] != "synthetic":
        raise ValueError("explicit list of all 160 replicate columns required")
    rep_scale = config.get("replicate_scale")
    if rep_fields and rep_scale is None:
        raise ValueError("explicit replicate_scale required")
    if replicate_rows is not None:
        for r in replicate_rows:
            key = (extract(r, config.get("replicate_keys", fields), "household_id", False),
                   extract(r, config.get("replicate_keys", fields), "person_number", False))
            if key in reps_by_person:
                raise ValueError("duplicate replicate-file person key")
            reps_by_person[key] = r
    seen_rep_keys = set()
    missing_tax_links = 0
    row_count = 0
    for row in rows:
        row_count += 1
        hh = extract(row, fields, "household_id", False)
        pn = extract(row, fields, "person_number", False)
        pid = hh + ":" + pn
        uid = extract(row, fields, "spm_unit_id", False)
        # Preserve SPM_ID exactly; TAX_ID is namespaced by household.
        tax_raw = extract(row, fields, "tax_unit_id", False) if "tax_unit_id" in fields else None
        tid = hh + ":" + tax_raw if tax_raw and tax_raw not in config.get("missing_tax_ids", ["0", "-1"]) else None
        age = extract(row, fields, "age")
        if age != int(age):
            raise ValueError("age must be integer")
        p = {"person_id": pid, "spm_unit_id": uid, "tax_unit_id": tid,
             "age": int(age), "person_weight": extract(row, fields, "person_weight")}
        if pid in people:
            raise ValueError("duplicate person in CPS extract")
        if tid is None:
            missing_tax_links += 1
        elif tid in tax_spm and tax_spm[tid] != uid:
            raise ValueError("tax unit spans SPM units; audited allocation required")
        else:
            tax_spm[tid] = uid
        if rep_fields:
            key = (hh, pn)
            rr = reps_by_person.get(key) if replicate_rows is not None else row
            if rr is None:
                raise ValueError("person missing from replicate weights; complete keyed join required")
            seen_rep_keys.add(key)
            p["replicate_weights"] = [num(rr.get(k), k, 0) * num(rep_scale, "replicate_scale", 0.000000001) for k in rep_fields]
        p["subgroups"] = {name: extract(row, {name: spec}, name, False)
                          for name, spec in config.get("subgroup_fields", {}).items()}
        u = {"spm_unit_id": uid, "resources": extract(row, fields, "resources"),
             "threshold": extract(row, fields, "threshold"), "unit_weight": extract(row, fields, "unit_weight")}
        for key, spec in spm_fields.items():
            u[key] = extract(row, {key: spec}, key)
        if uid in units and any(not same(units[uid].get(k), v) for k, v in u.items()):
            raise ValueError(f"inconsistent repeated SPM unit fields: {uid}")
        units[uid] = u
        people[pid] = p
        if tid:
            # Retain person-level tax-model observations. Do not sum duplicated
            # joint-return credits or infer a legal claimant from household age.
            observation = {"person_id": pid}
            for k, spec in config.get("tax_observation_fields", {}).items():
                observation[k] = extract(row, {k: spec}, k)
            tax_observations[tid].append(observation)
    if not row_count:
        raise ValueError("empty raw extract")
    if replicate_rows is not None and set(reps_by_person) != seen_rep_keys:
        raise ValueError("replicate file has unmatched persons; scope/crosswalk must be explicit")
    metadata["tax_assignment_status"] = "Census TAX_ID links only; legal dependent/claimant review outstanding"
    metadata["unassigned_tax_persons"] = missing_tax_links
    metadata["row_count"] = row_count
    out = {"schema_version": 2, "metadata": metadata,
           "units": list(units.values()), "people": list(people.values()),
           "taxes": [{"tax_unit_id": tid, "spm_unit_id": uid, "raw_observations": tax_observations[tid]}
                     for tid, uid in tax_spm.items()]}
    validate_population(out)
    return out


def apply_overlay(data, overlay):
    """Attach audited policy data without overwriting Census baseline totals."""
    import copy
    out = copy.deepcopy(data)
    allowed = {
        "units": {"care_family_income", "state_median_income", "care_need_eligible", "prek_eligible",
                  "prek_spm_reduction", "school_meal_spm_delta", "summer_ebt_spm_delta",
                  "voucher_eligible", "voucher_awarded", "voucher_spm_delta", "housing_increment_cap",
                  "emergency_aid_eligible", "emergency_aid_awarded", "emergency_aid_spm_delta", "delivery"},
        "taxes": {"agi", "filing_status", "claimant_ids", "current_law_ctc", "receipt", "on_time_months"},
        "people": {"tax_unit_id", "child_id", "qualifying_child", "subgroups"}}
    for section, id_key in (("units", "spm_unit_id"), ("taxes", "tax_unit_id"), ("people", "person_id")):
        records = {r[id_key]: r for r in out[section]}
        for key, changes in overlay.get(section, {}).items():
            if key not in records:
                raise ValueError(f"overlay unknown {section} ID: {key}")
            if set(changes) - allowed[section]:
                raise ValueError("policy overlay cannot overwrite baseline resources/weights/thresholds or unrecognized fields")
            records[key].update(changes)
    # New nonfiler/kinship tax assignments must be explicit, with their crosswalk.
    existing = {t["tax_unit_id"] for t in out["taxes"]}
    for tax in overlay.get("additional_tax_units", []):
        if not tax.get("tax_unit_id") or tax["tax_unit_id"] in existing:
            raise ValueError("additional tax unit duplicates an existing ID")
        existing.add(tax["tax_unit_id"])
        out["taxes"].append(tax)
    if not overlay.get("provenance"):
        raise ValueError("overlay provenance required")
    out["metadata"]["policy_overlay_provenance"] = overlay["provenance"]
    for key, reference in overlay.get("reviews", {}).items():
        if key not in ("tax_unit_crosswalk_review", "service_valuation_review") or not isinstance(reference, str) or not reference.strip():
            raise ValueError("overlay reviews require named crosswalk/service references")
        out["metadata"][key] = reference
    validate_population(out)
    return out


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--raw", required=True)
    p.add_argument("--member")
    p.add_argument("--mapping", required=True)
    p.add_argument("--replicates")
    p.add_argument("--replicate-member")
    p.add_argument("--overlay")
    p.add_argument("--output", required=True)
    a = p.parse_args()
    result = construct(csv_rows(a.raw, a.member), load_json(a.mapping),
                       csv_rows(a.replicates, a.replicate_member) if a.replicates else None)
    if a.overlay:
        result = apply_overlay(result, load_json(a.overlay))
    result["metadata"]["input_hashes"] = {"raw": sha256(a.raw), "mapping": sha256(a.mapping)}
    if a.replicates:
        result["metadata"]["input_hashes"]["replicates"] = sha256(a.replicates)
    if a.overlay:
        result["metadata"]["input_hashes"]["overlay"] = sha256(a.overlay)
    write_json(a.output, result)
    print(f"Constructed {len(result['people'])} persons, {len(result['units'])} SPM units; not a calibrated target-year baseline")


if __name__ == "__main__":
    main()
