#!/usr/bin/env python3
"""Import an externally audited target-year baseline; never invent projections.

Reweighting, tax/transfer recomputation, dollar aging and demographic projection
are substantive inputs. This adapter checks a complete, explicit replacement
ledger and target-population controls. It is not itself a forecast model.
"""
import argparse
import copy
from model import load_json, write_json, num, validate_population


def project(source, inputs):
    out = copy.deepcopy(source)
    if any("delivery" in u for u in out["units"]):
        raise ValueError("project the source-year baseline before attaching target-year policy/service overlays")
    if inputs.get("year") not in (2030, 2034):
        raise ValueError("target year must be 2030 or 2034")
    for field in ("projection_provenance", "tax_baseline_provenance", "population_controls_provenance"):
        if not inputs.get(field):
            raise ValueError(f"{field} required")
    ukeys = {u["spm_unit_id"] for u in out["units"]}
    pkeys = {p["person_id"] for p in out["people"]}
    tkeys = {t["tax_unit_id"] for t in out["taxes"]}
    for section, keys in (("units", ukeys), ("people", pkeys), ("taxes", tkeys)):
        if set(inputs.get(section, {})) != keys:
            raise ValueError("projection must explicitly cover every unit/person/tax ID")
    for u in out["units"]:
        changes = inputs["units"][u["spm_unit_id"]]
        required = set(u) - {"spm_unit_id"}
        for k in required:
            if k not in changes:
                raise ValueError(f"target-year {k} required")
        if set(changes) - required:
            raise ValueError("unexpected projection unit field")
        u.update(changes)
    for p in out["people"]:
        changes = inputs["people"][p["person_id"]]
        if set(changes) != {"person_weight", "replicate_weights"}:
            raise ValueError("explicit target-year base AND replicate weights required for every person")
        p.update(changes)
    for t in out["taxes"]:
        changes = inputs["taxes"][t["tax_unit_id"]]
        if set(changes) != {"agi", "current_law_ctc"}:
            raise ValueError("explicit target-year AGI and current-law CTC required for every tax unit")
        if "raw_observations" in t:
            t["source_year_raw_observations"] = t.pop("raw_observations")
        t.update(changes)
    # Snapshot reweighting keeps observed ages/composition. Cohort aging and new
    # families require a separately reconstructed population, never age += years.
    out["metadata"].update(kind="projected", resource_year=inputs["year"], dollar_year=inputs["year"],
        projection_method="audited replacement/reweighting of fixed source cross-section; not cohort aging",
        projection_provenance=inputs["projection_provenance"], target_year_baseline_review=inputs["tax_baseline_provenance"])
    validate_population(out)
    controls = inputs.get("controls", {})
    if not controls:
        raise ValueError("at least one explicit population control required")
    for name, control in controls.items():
        lo, hi = control["age_min"], control["age_max"]
        actual = sum(p["person_weight"] for p in out["people"] if lo <= p["age"] <= hi)
        if abs(actual - num(control["weighted_count"], name, 0)) > num(control["absolute_tolerance"], name+" tolerance", 0):
            raise ValueError(f"population control failed: {name}")
    return out


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--data", required=True)
    parser.add_argument("--inputs", required=True)
    parser.add_argument("--output", required=True)
    a = parser.parse_args()
    write_json(a.output, project(load_json(a.data), load_json(a.inputs)))
