#!/usr/bin/env python3
"""Project 2050 child-SPM microsimulation v1.

Input is an audited, de-identified SPM/tax-unit extract, NOT raw CPS ASEC.
This engine does not infer tax law, SPM thresholds, survey weights or receipt
from raw survey variables. See README.md before using its outputs.
"""
import argparse
import csv
import json
import math
from collections import Counter, defaultdict
from pathlib import Path

SCENARIOS = ("current_law", "full_receipt", "delivered", "enhanced")
ID_BRANCHES = ("ssn_only", "adult_itin", "adult_and_child_itin")
SUBGROUPS = ("age_group", "family_structure", "earnings_band", "disability",
             "identification", "race_ethnicity", "geography", "tenure")


def read_rows(path, required):
    with open(path, newline="", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        if not reader.fieldnames or set(required) - set(reader.fieldnames):
            raise ValueError(f"{path}: missing columns {sorted(set(required) - set(reader.fieldnames or []))}")
        rows = list(reader)
    if not rows:
        raise ValueError(f"{path}: no rows")
    return rows


def number(row, key, minimum=None):
    try:
        value = float(row[key])
    except (KeyError, TypeError, ValueError):
        raise ValueError(f"invalid numeric {key}: {row.get(key)!r}") from None
    if not math.isfinite(value) or (minimum is not None and value < minimum):
        raise ValueError(f"out-of-range {key}: {value}")
    return value


def flag(row, key):
    value = row.get(key, "")
    if value not in ("0", "1"):
        raise ValueError(f"{key} must be 0 or 1, got {value!r}")
    return value == "1"


def unique(rows, key):
    result = {}
    for row in rows:
        identifier = row[key]
        if not identifier or identifier in result:
            raise ValueError(f"blank or duplicate {key}: {identifier!r}")
        result[identifier] = row
    return result


def id_allowed(person, tax, branch):
    adult = tax["adult_id"]
    child = person["child_id"]
    if branch == "ssn_only":
        return adult == "ssn" and child == "ssn"
    if branch == "adult_itin":
        return adult in ("ssn", "itin") and child == "ssn"
    if branch == "adult_and_child_itin":
        return adult in ("ssn", "itin") and child in ("ssn", "itin")
    raise ValueError(branch)


def credit_amount(children, tax, branch, policy_index, reference_under17,
                  reference_age17):
    """Illustrative 2021-style two-stage phaseout layered over a 2025-law base.

    This is a *legal integration assumption*, not an adopted statutory rule.
    The independently calculated current-law credit is subtracted afterward.
    """
    eligible = [p for p in children if id_allowed(p, tax, branch)]
    gross = sum((3600 if int(p["age"]) < 6 else 3000) * policy_index for p in eligible)
    reference = sum(reference_under17 if int(p["age"]) < 17 else reference_age17
                    for p in eligible)
    if reference > gross + 1e-8:
        raise ValueError("reference credit exceeds proposed credit; revise indexing assumptions")
    filing = tax["filing_status"]
    if filing not in ("joint", "head", "other"):
        raise ValueError(f"unknown filing_status {filing}")
    agi = number(tax, "agi", 0)
    first_threshold = {"joint": 150000, "head": 112500, "other": 75000}[filing]
    second_threshold = 400000 if filing == "joint" else 200000
    first_cut = 50 * math.ceil(max(0, agi - first_threshold) / 1000)
    remaining_increase = max(0, gross - reference - first_cut)
    second_cut = 50 * math.ceil(max(0, agi - second_threshold) / 1000)
    return max(0, reference - second_cut) + remaining_increase


def observed_fraction(tax, scenario):
    if scenario == "full_receipt":
        return 1.0
    months = number(tax, "months_" + scenario, 0)
    if months > 12 or int(months) != months:
        raise ValueError("CTC receipt months must be integers from 0 through 12")
    return months / 12.0


def service_fraction(unit, key, scenario):
    if scenario == "full_receipt":
        return 1.0
    return float(flag(unit, key + "_" + scenario))


def service_delta(unit, year, scenario):
    """Only SPM-countable changes; no construction spending as immediate cash."""
    if scenario == "current_law":
        return 0.0
    delta = 0.0
    care_cost = number(unit, "spm_care_expense", 0)
    family_income = number(unit, "care_family_income", 0)
    state_median = number(unit, "state_median_income", 0)
    if state_median == 0 and care_cost > 0:
        raise ValueError("state_median_income required for care calculations")
    eligible = family_income <= 2.5 * state_median
    if year < 2032:
        cap = 0.0 if family_income < 0.75 * state_median else care_cost
    else:
        cap = 0.07 * family_income if eligible else care_cost
    if flag(unit, "care_slot") and eligible:
        delta += max(0.0, care_cost - cap) * service_fraction(unit, "care", scenario)
    delta += number(unit, "prek_spm_delta", 0) * service_fraction(unit, "prek", scenario)
    delta += number(unit, "school_meal_spm_delta", 0) * service_fraction(unit, "school_meal", scenario)
    delta += number(unit, "summer_ebt_spm_delta", 0) * service_fraction(unit, "summer_ebt", scenario)
    if flag(unit, "voucher_awarded"):
        delta += number(unit, "voucher_spm_delta", 0) * service_fraction(unit, "voucher_leaseup", scenario)
    delta += number(unit, "emergency_aid_spm_delta", 0) * service_fraction(unit, "emergency_aid", scenario)
    return delta


def summarise(records, field):
    total = sum(r["weight"] for r in records)
    poor = sum(r["weight"] for r in records if r[field] < r["threshold"])
    deep = sum(r["weight"] for r in records if r[field] < 0.5 * r["threshold"])
    near = sum(r["weight"] for r in records if r[field] < 1.5 * r["threshold"])
    gap = sum(r["weight"] * max(0, r["threshold"] - r[field]) for r in records)
    return {"weighted_children": round(total, 3),
            "poverty_rate": round(poor / total, 6) if total else None,
            "deep_poverty_rate": round(deep / total, 6) if total else None,
            "below_150pct_rate": round(near / total, 6) if total else None,
            "child_weighted_poverty_gap_dollars": round(gap, 2)}


def run(args):
    units = unique(read_rows(args.units, (
        "spm_unit_id", "weight", "spm_threshold", "spm_resources",
        "spm_care_expense", "care_family_income", "state_median_income",
        "care_slot", "care_delivered", "care_enhanced",
        "prek_spm_delta", "prek_delivered", "prek_enhanced",
        "school_meal_spm_delta", "school_meal_delivered", "school_meal_enhanced",
        "summer_ebt_spm_delta", "summer_ebt_delivered", "summer_ebt_enhanced",
        "voucher_awarded", "voucher_spm_delta", "voucher_leaseup_delivered",
        "voucher_leaseup_enhanced", "emergency_aid_spm_delta",
        "emergency_aid_delivered", "emergency_aid_enhanced")), "spm_unit_id")
    taxes = unique(read_rows(args.taxes, (
        "tax_unit_id", "spm_unit_id", "agi", "filing_status", "adult_id",
        "current_law_ctc", "months_delivered", "months_enhanced")), "tax_unit_id")
    people = unique(read_rows(args.people, (
        "person_id", "spm_unit_id", "tax_unit_id", "age", "child_id")), "person_id")
    if args.year not in (2030, 2034):
        raise ValueError("v1 explicitly models 2030 and 2034 only")
    if args.policy_index <= 0 or args.reference_under17 < 0 or args.reference_age17 < 0:
        raise ValueError("index and reference values must be nonnegative")
    if args.policy_index < 0.5 or args.policy_index > 5:
        raise ValueError("implausible index factor: check units")
    child_by_tax = defaultdict(list)
    child_by_spm = defaultdict(list)
    for p in people.values():
        age = number(p, "age", 0)
        if age > 120 or int(age) != age:
            raise ValueError("invalid age")
        if p["spm_unit_id"] not in units or p["tax_unit_id"] not in taxes:
            raise ValueError(f"person {p['person_id']} has missing unit")
        if taxes[p["tax_unit_id"]]["spm_unit_id"] != p["spm_unit_id"]:
            raise ValueError("tax units spanning SPM units require a separate allocation module")
        if age < 18:
            child_by_tax[p["tax_unit_id"]].append(p)
            child_by_spm[p["spm_unit_id"]].append(p)
    for tax in taxes.values():
        if tax["spm_unit_id"] not in units:
            raise ValueError("tax unit has missing SPM unit")
        if tax["adult_id"] not in ("ssn", "itin", "other"):
            raise ValueError("invalid adult_id")
        number(tax, "current_law_ctc", 0)
        for scenario in ("delivered", "enhanced"):
            observed_fraction(tax, scenario)
    for p in people.values():
        if p["child_id"] not in ("ssn", "itin", "other"):
            raise ValueError("invalid child_id")
    for u in units.values():
        number(u, "weight", 0)
        number(u, "spm_threshold", 0.01)
        number(u, "spm_resources")
        for key in ("care_slot", "voucher_awarded"):
            flag(u, key)
        for key in ("care", "prek", "school_meal", "summer_ebt", "voucher_leaseup", "emergency_aid"):
            for scenario in ("delivered", "enhanced"):
                flag(u, key + "_" + scenario)
        for key in ("spm_care_expense", "care_family_income", "state_median_income",
                    "prek_spm_delta", "school_meal_spm_delta", "summer_ebt_spm_delta",
                    "voucher_spm_delta", "emergency_aid_spm_delta"):
            number(u, key, 0)
    results = {}
    for branch in ID_BRANCHES:
        credits = {}
        for tid, tax in taxes.items():
            kids = child_by_tax.get(tid, [])
            entitlement = credit_amount(kids, tax, branch, args.policy_index,
                                        args.reference_under17, args.reference_age17)
            baseline = number(tax, "current_law_ctc", 0)
            credits[tid] = max(0.0, entitlement - baseline)
        scenario_results = {}
        for scenario in SCENARIOS:
            unit_resources = {}
            for uid, u in units.items():
                ctc_delta = 0 if scenario == "current_law" else sum(
                    credits[tid] * observed_fraction(tax, scenario)
                    for tid, tax in taxes.items() if tax["spm_unit_id"] == uid)
                extra = service_delta(u, args.year, scenario)
                unit_resources[uid] = number(u, "spm_resources") + ctc_delta + extra
            child_records = []
            for uid, kids in child_by_spm.items():
                u = units[uid]
                for p in kids:
                    age = int(p["age"])
                    child_records.append({
                        "weight": number(u, "weight", 0),
                        "threshold": number(u, "spm_threshold", 0.01),
                        "resources": unit_resources[uid],
                        "age_group": "under6" if age < 6 else "6to17",
                        **{key: p.get(key, "not_recorded") or "not_recorded"
                           for key in SUBGROUPS if key != "age_group"}})
            groups = {}
            for key in SUBGROUPS:
                labels = sorted({r[key] for r in child_records})
                groups[key] = {label: summarise(
                    [r for r in child_records if r[key] == label], "resources")
                    for label in labels}
            scenario_results[scenario] = {
                "all_children": summarise(child_records, "resources"),
                "subgroups": groups,
                "spm_unit_weighted_gap_dollars": round(sum(
                    number(u, "weight", 0) * max(0, number(u, "spm_threshold") - unit_resources[uid])
                    for uid, u in units.items() if uid in child_by_spm), 2)}
        # Mechanisms evaluated at delivered receipt, with residual-after-full
        # defined using the full-receipt counterfactual, not an additive category.
        overlaps = Counter()
        ordered = Counter()
        for uid, kids in child_by_spm.items():
            u = units[uid]
            threshold = number(u, "spm_threshold")
            if scenario_results["delivered"] is None:  # pragma: no cover
                raise AssertionError
            tax_ids = {p["tax_unit_id"] for p in kids}
            excluded = any(not id_allowed(p, taxes[p["tax_unit_id"]], branch) for p in kids)
            nonreceipt = any(credits[tid] > 0 and observed_fraction(taxes[tid], "delivered") < 1
                             for tid in tax_ids)
            service_missing = any((
                flag(u, "care_slot") and not flag(u, "care_delivered")
                and number(u, "spm_care_expense") > 0,
                flag(u, "voucher_awarded") and not flag(u, "voucher_leaseup_delivered"),
                number(u, "school_meal_spm_delta") > 0 and not flag(u, "school_meal_delivered"),
                number(u, "summer_ebt_spm_delta") > 0 and not flag(u, "summer_ebt_delivered")))
            full_resources = number(u, "spm_resources") + sum(
                credits[tid] for tid, t in taxes.items() if t["spm_unit_id"] == uid) + service_delta(u, args.year, "full_receipt")
            flags = (excluded, nonreceipt, full_resources < threshold, service_missing)
            label = "".join("1" if x else "0" for x in flags)
            count = len(kids) * number(u, "weight")
            overlaps[label] += count
            order = ("legal_exclusion", "eligible_nonreceipt", "resource_inadequacy_after_full",
                     "service_unavailable")
            ordered[next((name for name, yes in zip(order, flags) if yes), "no_flag")] += count
        results[branch] = {
            "scenarios": scenario_results,
            "mechanisms": {
                "flag_order": ["legal_exclusion", "eligible_nonreceipt",
                               "resource_inadequacy_after_full", "service_unavailable"],
                "overlap_patterns_weighted_children": dict(sorted(overlaps.items())),
                "ordered_attribution_weighted_children": dict(sorted(ordered.items()))}}
    return {
        "model": "project-2050-child-spm-v1",
        "year": args.year, "source_vintage": args.vintage,
        "baseline": "post-2025 current-law SPM resource extract supplied by analyst",
        "scope": "focused FAM-1A FAM-2A EDU-3A HOU-1A HOU-4A; no whole-package claim",
        "assumptions": {"policy_index_factor": args.policy_index,
                        "reference_under17": args.reference_under17,
                        "reference_age17": args.reference_age17,
                        "tax_phaseout": "provisional two-stage 2021-style integration",
                        "receipt": "observed/analyst-specified per-unit, not national haircut",
                        "service_deltas": "SPM-countable increments precomputed by analyst",
                        "weights": "SPM unit weight applied to each child"},
        "n_spm_units": len(units), "n_tax_units": len(taxes),
        "n_children": sum(map(len, child_by_spm.values())),
        "results": results}


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--units", required=True)
    p.add_argument("--taxes", required=True)
    p.add_argument("--people", required=True)
    p.add_argument("--year", type=int, required=True)
    p.add_argument("--vintage", required=True, help="Named CPS ASEC/SPM vintage and extract version")
    p.add_argument("--policy-index", type=float, required=True, help="Index multiplier from policy dollar base year")
    p.add_argument("--reference-under17", type=float, required=True,
                   help="Provisional current-law reference credit per eligible child under 17")
    p.add_argument("--reference-age17", type=float, required=True,
                   help="Provisional first-phaseout reference for 17-year-olds")
    p.add_argument("--output", required=True)
    args = p.parse_args()
    output = run(args)
    Path(args.output).parent.mkdir(parents=True, exist_ok=True)
    with open(args.output, "w", encoding="utf-8") as f:
        json.dump(output, f, indent=2, sort_keys=True)
        f.write("\n")
    print(f"Wrote {args.output}: {output['n_children']} unweighted children; NOT a Project 2050 estimate")


if __name__ == "__main__":
    main()
