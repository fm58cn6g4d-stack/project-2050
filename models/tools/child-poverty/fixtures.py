"""Artificial examples for software verification only; no population calibration."""
import copy
from pathlib import Path
from model import SERVICES, write_json


def policy(year=2030):
    return {"year": year, "policy_status": "research_only", "policy_index": 1.0,
            "reference_under17": 2200, "reference_age17": 2200,
            "age17_layer": "expansion_only", "phaseout_threshold_index": 1.0,
            "receipt_basis": "replace_credit", "min_cell": 1,
            "parameter_provenance": "synthetic test values, NOT target-year tax law"}


def unit(uid, resources=1000, threshold=20000, weight=1):
    return {"spm_unit_id": uid, "resources": resources, "threshold": threshold, "unit_weight": weight,
            "childcare_expense": 0, "work_expense": 0, "work_care_deduction": 0,
            "care_family_income": 0, "state_median_income": 50000,
            "care_need_eligible": False, "prek_eligible": False, "prek_spm_reduction": 0,
            "school_meal_spm_delta": 0, "summer_ebt_spm_delta": 0,
            "voucher_eligible": False, "voucher_awarded": False, "voucher_spm_delta": 0,
            "housing_increment_cap": 0, "emergency_aid_eligible": False,
            "emergency_aid_awarded": False, "emergency_aid_spm_delta": 0,
            "delivery": {s: {k: False for k in SERVICES} for s in ("full_receipt", "delivered", "enhanced")}}


def tax(tid, uid, ids=None, baseline=0):
    return {"tax_unit_id": tid, "spm_unit_id": uid, "agi": 0,
            "filing_status": "head", "claimant_ids": ids or ["ssn"], "current_law_ctc": baseline,
            "receipt": {s: [1/12]*12 for s in ("delivered", "enhanced")},
            "on_time_months": {"delivered": 12, "enhanced": 12}}


def person(pid, uid, tid, age, weight=1, child_id="ssn"):
    return {"person_id": pid, "spm_unit_id": uid, "tax_unit_id": tid, "age": age,
            "person_weight": weight, "child_id": child_id, "qualifying_child": age < 18,
            "replicate_weights": [weight*.8, weight*1.2],
            "subgroups": {"family_structure": "synthetic_family", "earnings_band": "synthetic",
                          "disability": "not_recorded", "identification": "synthetic_ID",
                          "race_ethnicity": "not_recorded", "geography": "synthetic", "tenure": "renter"}}


def population():
    units = [unit("u1", 2000, 15000, 1), unit("u2", 10000, 20000, 2),
             unit("u3", 38000, 30000, 3), unit("u4", 14500, 16000, 1),
             unit("u5", -500, 18000, 1), unit("u6", 13000, 14000, 8)]
    units[0].update(childcare_expense=6000, work_care_deduction=6000,
                    care_need_eligible=True, prek_eligible=True, prek_spm_reduction=2000,
                    school_meal_spm_delta=500, summer_ebt_spm_delta=60,
                    voucher_eligible=True, emergency_aid_eligible=True,
                    emergency_aid_awarded=True, emergency_aid_spm_delta=1000)
    units[1].update(school_meal_spm_delta=1000, voucher_eligible=True,
                    voucher_awarded=True, voucher_spm_delta=3500, housing_increment_cap=4000)
    units[2].update(childcare_expense=7000, work_care_deduction=7000,
                    care_need_eligible=True, care_family_income=40000)
    for u in units:
        for k in SERVICES:
            u["delivery"]["full_receipt"][k] = True
            u["delivery"]["enhanced"][k] = True
    # u1 has no usable care/pre-K slot in the supplied physical baseline; even
    # full receipt cannot invent one. Enhanced supply is an explicit comparison.
    for k in ("care", "prek"):
        units[0]["delivery"]["full_receipt"][k] = False
    units[0]["delivery"]["delivered"]["school_meal"] = True
    units[1]["delivery"]["delivered"]["school_meal"] = True
    units[2]["delivery"]["delivered"]["care"] = True
    taxes = [tax("t"+str(i), "u"+str(i)) for i in range(1, 7)]
    taxes[0]["receipt"]["delivered"] = [1/12]*6 + [0]*6
    taxes[0]["on_time_months"]["delivered"] = 6
    taxes[2]["claimant_ids"] = ["itin"]
    taxes[2]["current_law_ctc"] = 0
    taxes[3]["agi"] = 140000
    taxes[5]["current_law_ctc"] = 2200
    taxes[5]["receipt"]["delivered"] = [1/12]*6 + [0]*5 + [.5]
    taxes[5]["on_time_months"]["delivered"] = 6
    kids = [person("c1", "u1", "t1", 4, 1), person("c2", "u2", "t2", 8, 2),
            person("c3", "u2", "t2", 10, 3, "itin"), person("c4", "u3", "t3", 3, 3),
            person("c5", "u4", "t4", 17, 1), person("c6", "u5", "t5", 7, 1, "other"),
            person("c7", "u6", "t6", 5, 10)]
    adults = [person("a"+str(i), "u"+str(i), "t"+str(i), 35, i) for i in range(1, 7)]
    return {"schema_version": 2, "metadata": {"kind": "synthetic", "source_vintage": "artificial fixture v2",
            "resource_year": 2030, "dollar_year": 2030, "weight_basis": "explicit synthetic person/unit weights",
            "baseline_description": "deliberately artificial; no national interpretation"},
            "units": units, "taxes": taxes, "people": kids + adults}


if __name__ == "__main__":
    folder = Path(__file__).parent / "synthetic"
    write_json(folder / "population.json", population())
    for year in (2030, 2034):
        write_json(folder / f"policy-{year}.json", policy(year))
