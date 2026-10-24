#!/usr/bin/env python3
"""Reconstructed child-SPM research engine. Standard library, explicit inputs.

This is NOT a national estimate, tax filing calculator, or adopted policy change.
See README.md, schema.md and the recovery report before interpreting outputs.
"""
import argparse
import copy
import hashlib
import json
import math
from collections import Counter, defaultdict
from pathlib import Path

VERSION = "project-2050-child-spm-rebuild-2"
SCENARIOS = ("current_law", "full_receipt", "delivered", "enhanced")
BRANCHES = ("ssn_only", "adult_itin", "adult_and_child_itin")
SUBGROUPS = ("age_group", "family_structure", "family_size", "earnings_band",
             "disability", "identification", "race_ethnicity", "geography", "tenure")
MECHANISMS = ("legal_exclusion", "eligible_nonreceipt",
              "resource_inadequacy_after_full", "service_unavailable")
SERVICES = ("care", "prek", "school_meal", "summer_ebt", "voucher", "emergency_aid")


def num(value, name, minimum=None, maximum=None):
    if isinstance(value, bool):
        raise ValueError(f"{name}: boolean is not a number")
    try:
        result = float(value)
    except (TypeError, ValueError):
        raise ValueError(f"{name}: missing/invalid number {value!r}") from None
    if not math.isfinite(result) or (minimum is not None and result < minimum) or (maximum is not None and result > maximum):
        raise ValueError(f"{name}: out of range {value!r}")
    return result


def boolean(value, name):
    if type(value) is not bool:
        raise ValueError(f"{name}: explicit boolean required")
    return value


def integer(value, name, minimum, maximum):
    result = num(value, name, minimum, maximum)
    if result != int(result):
        raise ValueError(f"{name}: integer required")
    return int(result)


def index_rows(rows, key):
    out = {}
    for row in rows:
        identifier = row.get(key)
        if not isinstance(identifier, str) or not identifier or identifier in out:
            raise ValueError(f"blank/duplicate {key}: {identifier!r}")
        out[identifier] = row
    return out


def validate_population(data):
    if data.get("schema_version") != 2:
        raise ValueError("schema_version must be 2")
    meta = data["metadata"]
    if meta.get("kind") not in ("synthetic", "source_year", "projected"):
        raise ValueError("metadata.kind must be synthetic, source_year or projected")
    for key in ("source_vintage", "baseline_description", "weight_basis"):
        if not meta.get(key):
            raise ValueError(f"metadata.{key} required")
    integer(meta.get("resource_year"), "resource_year", 1900, 2100)
    integer(meta.get("dollar_year"), "dollar_year", 1900, 2100)
    units = index_rows(data["units"], "spm_unit_id")
    taxes = index_rows(data.get("taxes", []), "tax_unit_id")
    people = index_rows(data["people"], "person_id")
    if not units or not people:
        raise ValueError("population cannot be empty")
    for u in units.values():
        num(u.get("resources"), "resources")
        num(u.get("threshold"), "threshold", 0.01)
        num(u.get("unit_weight"), "unit_weight", 0)
    for p in people.values():
        integer(p.get("age"), "age", 0, 120)
        num(p.get("person_weight"), "person_weight", 0)
        if p.get("spm_unit_id") not in units:
            raise ValueError("person has missing SPM unit")
        reps = p.get("replicate_weights", [])
        if not isinstance(reps, list):
            raise ValueError("replicate_weights must be an array")
        for w in reps:
            num(w, "replicate weight", 0)
    children = [p for p in people.values() if p["age"] < 18]
    if not children or sum(p["person_weight"] for p in children) <= 0:
        raise ValueError("positive-weight child population required")
    lengths = {len(p.get("replicate_weights", [])) for p in people.values()}
    if len(lengths) != 1:
        raise ValueError("replicate-weight dimensions differ across people")
    if meta["kind"] != "synthetic" and next(iter(lengths)) not in (0, 160):
        raise ValueError("CPS population requires all 160 replicate weights or none")
    return units, taxes, people, children


def validate_policy(data, policy):
    units, taxes, people, children = validate_population(data)
    year = integer(policy.get("year"), "policy.year", 2030, 2034)
    if year not in (2030, 2034):
        raise ValueError("rebuild explicitly supports 2030 and 2034")
    if data["metadata"]["kind"] != "synthetic":
        if data["metadata"]["resource_year"] != year or data["metadata"]["dollar_year"] != year:
            raise ValueError("target-year resources, population and dollars must be prepared before a policy run")
        for gate in ("target_year_baseline_review", "tax_unit_crosswalk_review", "service_valuation_review"):
            if not data["metadata"].get(gate):
                raise ValueError(f"audited input reference metadata.{gate} required")
    for key in ("policy_index", "reference_under17", "reference_age17", "phaseout_threshold_index"):
        num(policy.get(key), "policy." + key, 0)
    if policy["policy_index"] <= 0 or policy["phaseout_threshold_index"] <= 0:
        raise ValueError("index factors must be positive")
    if policy.get("age17_layer") not in ("expansion_only", "retained_reference"):
        raise ValueError("explicit age17_layer required")
    if policy.get("receipt_basis") not in ("replace_credit", "increment_only"):
        raise ValueError("explicit receipt_basis required")
    if policy.get("policy_status") != "research_only":
        raise ValueError("this tool implements research branches, not policy adoption")
    min_cell = integer(policy.get("min_cell"), "min_cell", 1, 1000000)
    if data["metadata"]["kind"] != "synthetic" and min_cell < 30:
        raise ValueError("non-synthetic subgroup cells require min_cell >= 30")
    for t in taxes.values():
        if t.get("spm_unit_id") not in units:
            raise ValueError("tax unit has missing SPM unit")
        if t.get("filing_status") not in ("joint", "head", "other"):
            raise ValueError("invalid filing status")
        ids = t.get("claimant_ids")
        required_count = 2 if t["filing_status"] == "joint" else 1
        if not isinstance(ids, list) or len(ids) != required_count or any(x not in ("ssn", "itin", "other") for x in ids):
            raise ValueError("claimant_ids must enumerate each filer, including both joint filers")
        num(t.get("agi"), "agi")
        num(t.get("current_law_ctc"), "current_law_ctc", 0)
        for s in ("delivered", "enhanced"):
            schedule = t.get("receipt", {}).get(s)
            if not isinstance(schedule, list) or len(schedule) != 12:
                raise ValueError("receipt must specify 12 monthly fractions of the annual award")
            for fraction in schedule:
                num(fraction, "receipt fraction", 0, 1)
            if sum(schedule) > 1 + 1e-9:
                raise ValueError("annual receipt fractions exceed 1")
            ontime = integer(t.get("on_time_months", {}).get(s), "on_time_months", 0, 12)
            if ontime > sum(f > 0 for f in schedule):
                raise ValueError("on_time_months exceeds months with a payment")
    for p in children:
        tid = p.get("tax_unit_id")
        if tid not in taxes or taxes[tid]["spm_unit_id"] != p["spm_unit_id"]:
            raise ValueError("child tax/SPM crosswalk missing or spans SPM units")
        if p.get("child_id") not in ("ssn", "itin", "other"):
            raise ValueError("explicit child identification class required; never infer from citizenship")
        boolean(p.get("qualifying_child"), "qualifying_child (non-ID rules)")
    prek_units = {p["spm_unit_id"] for p in children if p["age"] in (3, 4)}
    for u in units.values():
        for k in ("childcare_expense", "work_expense", "work_care_deduction", "care_family_income", "state_median_income",
                  "prek_spm_reduction", "school_meal_spm_delta", "summer_ebt_spm_delta",
                  "voucher_spm_delta", "emergency_aid_spm_delta"):
            num(u.get(k), k, 0)
        if u["work_care_deduction"] > u["work_expense"] + u["childcare_expense"] + 1e-6:
            raise ValueError("capped work/care deduction exceeds uncapped expenses")
        for k in ("care_need_eligible", "prek_eligible", "voucher_eligible",
                  "voucher_awarded", "emergency_aid_eligible", "emergency_aid_awarded"):
            boolean(u.get(k), k)
        if u["care_need_eligible"] and u["state_median_income"] <= 0:
            raise ValueError("positive family-size-adjusted state median income required")
        if u["voucher_awarded"] and not u["voucher_eligible"]:
            raise ValueError("voucher award to ineligible unit")
        if u["emergency_aid_awarded"] and not u["emergency_aid_eligible"]:
            raise ValueError("emergency award to ineligible unit")
        if u["voucher_spm_delta"] and u.get("housing_increment_cap") is None:
            raise ValueError("incremental SPM housing-subsidy cap required")
        if u.get("housing_increment_cap") is not None:
            num(u["housing_increment_cap"], "housing_increment_cap", 0)
        for s in ("full_receipt", "delivered", "enhanced"):
            delivery = u.get("delivery", {}).get(s, {})
            for k in SERVICES:
                boolean(delivery.get(k), f"delivery.{s}.{k}")
        if any(u["delivery"]["delivered"][k] and not u["delivery"]["full_receipt"][k] for k in SERVICES):
            raise ValueError("delivered service cannot exceed full available service")
        if u["prek_eligible"] and u["spm_unit_id"] not in prek_units:
            raise ValueError("pre-K eligibility requires a recorded child aged 3 or 4")
    # Awards are household/unit counts, never weighted child counts.
    award_count = sum(u["unit_weight"] for u in units.values() if u["voucher_awarded"])
    voucher_limit = 100000 * min(4, year - 2029)
    if award_count > voucher_limit + 1e-6:
        raise ValueError(f"incremental voucher awards {award_count} exceed adopted cumulative cap {voucher_limit}")
    return units, taxes, people, children


def eligible(child, tax, branch):
    if branch not in BRANCHES:
        raise ValueError(branch)
    ids = tax["claimant_ids"]
    adults_valid = all(x in ("ssn", "itin") for x in ids)
    if branch == "ssn_only":
        adults_valid = adults_valid and "ssn" in ids
    child_valid = child["child_id"] == "ssn" or (branch == "adult_and_child_itin" and child["child_id"] == "itin")
    return child["qualifying_child"] and adults_valid and child_valid


def credit_amount(children, tax, branch, policy):
    """Provisional two-stage integration, explicit dollar base and age-17 branch.

    Not a complete 26 USC 24 / 8812 implementation. In particular ODC, custody,
    territories and safe harbors require a reviewed tax baseline/crosswalk.
    """
    kids = [p for p in children if eligible(p, tax, branch)]
    gross = sum((3600 if p["age"] < 6 else 3000) * policy["policy_index"] for p in kids)
    reference = sum(policy["reference_under17"] if p["age"] < 17 else
                    (policy["reference_age17"] if policy["age17_layer"] == "retained_reference" else 0)
                    for p in kids)
    if reference > gross + 1e-8:
        raise ValueError("retained reference exceeds proposed gross credit")
    filing = tax["filing_status"]
    first = {"joint": 150000, "head": 112500, "other": 75000}[filing] * policy["phaseout_threshold_index"]
    second = (400000 if filing == "joint" else 200000) * policy["phaseout_threshold_index"]
    # Negative AGI is valid and cannot trigger a phaseout.
    first_cut = 50 * math.ceil(max(0, tax["agi"] - first) / 1000)
    second_cut = 50 * math.ceil(max(0, tax["agi"] - second) / 1000)
    return max(0, gross - reference - first_cut) + max(0, reference - second_cut)


def receipt_fraction(tax, scenario):
    return 1.0 if scenario == "full_receipt" else sum(tax["receipt"][scenario])


def credit_delta(entitlement, tax, scenario, policy):
    if scenario == "current_law":
        return 0.0
    baseline = tax["current_law_ctc"]
    if policy["receipt_basis"] == "replace_credit":
        # Unlike v1, this can report a loss when the replacement is not received.
        return entitlement * receipt_fraction(tax, scenario) - baseline
    if entitlement < baseline - 1e-8:
        raise ValueError("increment_only cannot represent a statutory loser; use replace_credit")
    return (entitlement - baseline) * receipt_fraction(tax, scenario)


def service_effect(unit, year, scenario):
    if scenario == "current_law":
        return {"cash": 0.0, "expense_reduction": 0.0, "in_kind": 0.0,
                "components": {}, "unavailable": []}
    u = unit
    d = u["delivery"][scenario]
    missing = []
    income, smi = u["care_family_income"], u["state_median_income"]
    income_eligible = smi > 0 and (income < .75 * smi if year < 2032 else income <= 2.5 * smi)
    care_eligible = u["care_need_eligible"] and income_eligible
    cap = 0 if year < 2032 else .07 * income
    # Raw SPM_CHILDCAREXPNS is NOT the capped SPM deduction. First compute
    # actual out-of-pocket savings, then recompute the combined deduction under
    # an unchanged earnings cap/work expense. Pre-K and care share these dollars.
    prek_saving = min(u["childcare_expense"], u["prek_spm_reduction"]) if u["prek_eligible"] and d["prek"] else 0.0
    remaining = max(0, u["childcare_expense"] - prek_saving)
    care_saving = max(0, remaining - cap) if care_eligible and d["care"] else 0.0
    before = u["work_care_deduction"]
    uncapped = u["work_expense"] + u["childcare_expense"]
    prek = before - min(before, uncapped - prek_saving)
    care = before - min(before, uncapped - prek_saving - care_saving) - prek
    if care_eligible and remaining > cap and not d["care"]:
        missing.append("care")
    if u["prek_eligible"] and u["prek_spm_reduction"] > 0 and not d["prek"]:
        missing.append("prek")
    school = u["school_meal_spm_delta"] if d["school_meal"] else 0.0
    summer = u["summer_ebt_spm_delta"] if d["summer_ebt"] else 0.0
    for name in ("school_meal", "summer_ebt"):
        if u[name + "_spm_delta"] > 0 and not d[name]:
            missing.append(name)
    voucher = min(u["voucher_spm_delta"], u.get("housing_increment_cap") or 0) if u["voucher_awarded"] and d["voucher"] else 0.0
    if u["voucher_eligible"] and (not u["voucher_awarded"] or not d["voucher"]):
        missing.append("voucher")
    # HOU-1 is temporary; a stale award flag cannot create 2034 income.
    emergency = u["emergency_aid_spm_delta"] if year <= 2031 and u["emergency_aid_awarded"] and d["emergency_aid"] else 0.0
    if year <= 2031 and u["emergency_aid_eligible"] and (not u["emergency_aid_awarded"] or not d["emergency_aid"]):
        missing.append("emergency_aid")
    return {"cash": emergency, "expense_reduction": prek + care,
            "in_kind": school + summer + voucher,
            "components": {"prek": prek, "care": care, "school_meal": school,
                           "summer_ebt": summer, "voucher": voucher, "emergency_aid": emergency},
            "unavailable": missing}


def poverty_metrics(records, weights=None, min_cell=1):
    weights = weights if weights is not None else [r["person_weight"] for r in records]
    total = sum(weights)
    out = {"unweighted_children": len(records), "weighted_children": total,
           "suppressed": len(records) < min_cell or total <= 0}
    indicators = {"poor": lambda r: r["resources"] < r["threshold"],
                  "deep_poor": lambda r: r["resources"] < .5 * r["threshold"],
                  "below150": lambda r: r["resources"] < 1.5 * r["threshold"],
                  "near_only": lambda r: r["threshold"] <= r["resources"] < 1.5 * r["threshold"]}
    for name, test in indicators.items():
        count = sum(w for r, w in zip(records, weights) if test(r))
        out[name + "_children"] = count
        out[name + "_rate"] = count / total if not out["suppressed"] else None
    out["child_weighted_gap_dollars"] = sum(w * max(0, r["threshold"] - r["resources"]) for r, w in zip(records, weights))
    out["child_weighted_deep_gap_dollars"] = sum(w * max(0, .5 * r["threshold"] - r["resources"]) for r, w in zip(records, weights))
    # Kish n_eff is a diagnostic; NOT a replacement for survey-design variance.
    out["kish_effective_n"] = total ** 2 / sum(w*w for w in weights) if any(weights) else 0
    return out


def replicate_intervals(records, current_records=None):
    count = len(records[0].get("replicate_weights", [])) if records else 0
    if not count:
        return {"status": "not_available", "n_replicates": 0}
    point = poverty_metrics(records)
    names = ("poor_rate", "deep_poor_rate", "below150_rate", "poor_children", "child_weighted_gap_dollars")
    base = poverty_metrics(current_records) if current_records is not None else None
    sums = dict.fromkeys(names, 0.0)
    paired = dict.fromkeys(names, 0.0)
    for i in range(count):
        weights = [r["replicate_weights"][i] for r in records]
        if sum(weights) <= 0:
            raise ValueError("zero-weight replicate cannot produce a poverty rate")
        estimate = poverty_metrics(records, weights)
        baseline = poverty_metrics(current_records, weights) if base is not None else None
        for name in names:
            sums[name] += (estimate[name] - point[name]) ** 2
            if base is not None:
                paired[name] += ((estimate[name] - baseline[name]) - (point[name] - base[name])) ** 2
    out = {"status": "computed", "n_replicates": count,
           "method": "CPS SDR: 4/R sum squared deviations from full-sample estimate",
           "interval": "normal approximation, 95 percent; sampling uncertainty only", "metrics": {}}
    for name in names:
        se = math.sqrt(4 / count * sums[name])
        lo, hi = point[name] - 1.96 * se, point[name] + 1.96 * se
        if name.endswith("rate"):
            lo, hi = max(0, lo), min(1, hi)
        out["metrics"][name] = {"se": se, "lower95": lo, "upper95": hi}
        if base is not None:
            diff, paired_se = point[name] - base[name], math.sqrt(4 / count * paired[name])
            out["metrics"][name]["paired_change"] = {"estimate": diff, "se": paired_se,
                "lower95": diff - 1.96 * paired_se, "upper95": diff + 1.96 * paired_se}
    return out


def baseline(data):
    units, _, _, children = validate_population(data)
    records = [{**p, "resources": units[p["spm_unit_id"]]["resources"],
                "threshold": units[p["spm_unit_id"]]["threshold"]} for p in children]
    return {"model": VERSION, "scope": "source-year public-use baseline; no Project policy",
            "metadata": data["metadata"], "all_children": poverty_metrics(records),
            "uncertainty": replicate_intervals(records)}


def simulate(data, policy):
    units, taxes, people, children = validate_policy(data, policy)
    kids_by_tax = defaultdict(list)
    taxes_by_spm = defaultdict(list)
    family_sizes = Counter(p["spm_unit_id"] for p in people.values())
    for p in children:
        kids_by_tax[p["tax_unit_id"]].append(p)
    for tid, t in taxes.items():
        taxes_by_spm[t["spm_unit_id"]].append(tid)
    results = {}
    for branch in BRANCHES:
        entitlements = {tid: credit_amount(kids_by_tax[tid], tax, branch, policy) for tid, tax in taxes.items()}
        scenario_results, raw_records, unit_ledgers = {}, {}, {}
        for scenario in SCENARIOS:
            ledgers = {}
            for uid, u in units.items():
                service = service_effect(u, policy["year"], scenario)
                ctc = sum(credit_delta(entitlements[tid], taxes[tid], scenario, policy) for tid in taxes_by_spm[uid])
                cash = ctc + service["cash"]
                total = cash + service["expense_reduction"] + service["in_kind"]
                ledgers[uid] = {"baseline_resources": u["resources"], "ctc_delta": ctc,
                    "cash_delta": cash, "expense_reduction": service["expense_reduction"],
                    "in_kind_delta": service["in_kind"], "total_delta": total,
                    "resources": u["resources"] + total, "service_components": service["components"],
                    "unavailable_services": service["unavailable"]}
            records = []
            child_unit_ids = {p["spm_unit_id"] for p in children}
            for p in children:
                uid = p["spm_unit_id"]
                groups = {k: p.get("subgroups", {}).get(k, "not_recorded") for k in SUBGROUPS}
                groups["age_group"] = "under6" if p["age"] < 6 else "6to17"
                groups["family_size"] = str(family_sizes[uid])
                records.append({**p, "resources": ledgers[uid]["resources"], "threshold": units[uid]["threshold"], "groups": groups})
            groups = {}
            for group in SUBGROUPS:
                buckets = defaultdict(list)
                for r in records:
                    buckets[r["groups"][group]].append(r)
                groups[group] = {label: poverty_metrics(rows, min_cell=policy["min_cell"]) for label, rows in sorted(buckets.items())}
            channels = {name: sum(units[uid]["unit_weight"] * l[name] for uid, l in ledgers.items())
                        for name in ("ctc_delta", "cash_delta", "expense_reduction", "in_kind_delta", "total_delta")}
            on_time_den = sum(p["person_weight"] for p in children if eligible(p, taxes[p["tax_unit_id"]], branch) and entitlements[p["tax_unit_id"]] > 0)
            on_time_sum = sum(p["person_weight"] * (12 if scenario == "full_receipt" else taxes[p["tax_unit_id"]]["on_time_months"][scenario])
                              for p in children if scenario != "current_law" and eligible(p, taxes[p["tax_unit_id"]], branch) and entitlements[p["tax_unit_id"]] > 0)
            scenario_results[scenario] = {"all_children": poverty_metrics(records), "subgroups": groups,
                "unit_weighted_gap_dollars_child_units": sum(u["unit_weight"] * max(0, u["threshold"] - ledgers[uid]["resources"]) for uid, u in units.items() if uid in child_unit_ids),
                "unit_weighted_resource_deltas_not_fiscal_cost": channels,
                "payment_reliability": {"eligible_positive_award_weighted_children": on_time_den if scenario != "current_law" else None,
                    "mean_on_time_months": on_time_sum / on_time_den if scenario != "current_law" and on_time_den else None,
                    "hardship_effect": "not estimated; annual SPM and payment timing are different outcomes"},
                "unit_resource_ledger": ledgers}
            raw_records[scenario], unit_ledgers[scenario] = records, ledgers
        for scenario in SCENARIOS:
            scenario_results[scenario]["uncertainty"] = replicate_intervals(raw_records[scenario], raw_records["current_law"])
        overlaps, ordered, coverage = Counter(), Counter(), Counter()
        details = []
        for p in children:
            uid, tid, w = p["spm_unit_id"], p["tax_unit_id"], p["person_weight"]
            allowed = eligible(p, taxes[tid], branch)
            flags = (not allowed,
                     allowed and entitlements[tid] > 0 and receipt_fraction(taxes[tid], "delivered") < 1 - 1e-9,
                     unit_ledgers["full_receipt"][uid]["resources"] < units[uid]["threshold"],
                     bool(unit_ledgers["delivered"][uid]["unavailable_services"]))
            for name, yes in zip(MECHANISMS, flags):
                if yes:
                    coverage[name] += w
            if unit_ledgers["delivered"][uid]["resources"] >= units[uid]["threshold"]:
                continue
            pattern = "".join("1" if f else "0" for f in flags)
            overlaps[pattern] += w
            category = next((name for name, yes in zip(MECHANISMS, flags) if yes), "no_flag")
            ordered[category] += w
            details.append({"person_id": p["person_id"], "weight": w, "pattern": pattern, "ordered": category})
        results[branch] = {"scenarios": scenario_results, "mechanisms": {
            "population": "children poor under delivered receipt only",
            "flag_order": MECHANISMS, "overlap_patterns_weighted_children": dict(sorted(overlaps.items())),
            "ordered_attribution_weighted_children": dict(sorted(ordered.items())),
            "coverage_flags_all_children_not_residual_counts": dict(sorted(coverage.items())),
            "residual_child_details": details}}
    return {"model": VERSION, "status": "research_only_not_nationally_calibrated",
            "scope": "focused FAM-1A/FAM-2A/EDU-3A/HOU-1A/HOU-4A, not full Project 2050",
            "source_metadata": data["metadata"], "policy": policy,
            "limitations": ["Provisional FAM-1 two-stage legal integration", "No full tax/transfer recomputation",
                "No automatic immigration/SSN imputation", "No empirical employment or hardship effect",
                "No national receipt, slot or lease-up calibration", "No D3/D4 or fiscal score from SPM deltas"],
            "results": results}


def load_json(path):
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def write_json(path, value):
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    Path(path).write_text(json.dumps(value, indent=2, sort_keys=True, allow_nan=False) + "\n", encoding="utf-8")


def sha256(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--data", required=True)
    parser.add_argument("--policy", help="Omit with --baseline-only")
    parser.add_argument("--baseline-only", action="store_true")
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    if not args.baseline_only and not args.policy:
        parser.error("--policy required unless --baseline-only")
    data = load_json(args.data)
    out = baseline(data) if args.baseline_only else simulate(data, load_json(args.policy))
    out["input_hashes"] = {"data_sha256": sha256(args.data)}
    if args.policy:
        out["input_hashes"]["policy_sha256"] = sha256(args.policy)
    write_json(args.output, out)
    print(f"Wrote {args.output}; research output, no national Project estimate")


if __name__ == "__main__":
    main()
