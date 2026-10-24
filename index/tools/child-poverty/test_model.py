#!/usr/bin/env python3
"""Logic/identity/regression tests. These do not establish external validity."""
import copy
import importlib.util
import math
import unittest
from pathlib import Path
from fixtures import population, policy, unit, tax, person
from model import (simulate, baseline, eligible, credit_amount, credit_delta,
                   service_effect, poverty_metrics, replicate_intervals, validate_policy)
from preprocess import construct, apply_overlay
from calibrate import compare
from project import project


class ModelTests(unittest.TestCase):
    def setUp(self):
        self.d = population()
        self.p = policy()

    def run_model(self):
        return simulate(self.d, self.p)["results"]

    def test_current_law_branch_invariance(self):
        r = self.run_model()
        b = r["ssn_only"]["scenarios"]["current_law"]
        self.assertEqual(b, r["adult_itin"]["scenarios"]["current_law"])
        self.assertEqual(b, r["adult_and_child_itin"]["scenarios"]["current_law"])

    def test_person_weights_not_unit_weights(self):
        b = baseline(self.d)["all_children"]
        self.assertEqual(b["weighted_children"], 21)
        self.assertEqual(b["poor_children"], 18)
        self.assertAlmostEqual(b["poor_rate"], 18/21)

    def test_low_income_credit_and_age(self):
        t = tax("t", "u")
        kids = [person("a", "u", "t", 5), person("b", "u", "t", 6), person("c", "u", "t", 17)]
        self.assertEqual(credit_amount(kids, t, "ssn_only", self.p), 9600)

    def test_first_phaseout_rounds_up(self):
        t = tax("t", "u")
        kids = [person("a", "u", "t", 5)]
        t["agi"] = 112500
        self.assertEqual(credit_amount(kids, t, "ssn_only", self.p), 3600)
        t["agi"] += .01
        self.assertEqual(credit_amount(kids, t, "ssn_only", self.p), 3550)

    def test_second_phaseout(self):
        t = tax("t", "u")
        t["agi"] = 201001
        self.assertEqual(credit_amount([person("a", "u", "t", 5)], t, "ssn_only", self.p), 2100)

    def test_negative_agi_permitted(self):
        self.d["taxes"][0]["agi"] = -1000
        validate_policy(self.d, self.p)
        self.assertEqual(credit_amount([self.d["people"][0]], self.d["taxes"][0], "ssn_only", self.p), 3600)

    def test_age17_interpretations_material(self):
        t = tax("t", "u")
        t["agi"] = 140000
        kids = [person("a", "u", "t", 17)]
        a = credit_amount(kids, t, "ssn_only", self.p)
        self.p["age17_layer"] = "retained_reference"
        b = credit_amount(kids, t, "ssn_only", self.p)
        self.assertEqual((a, b), (1600, 2200))

    def test_joint_one_ssn_with_itin_spouse(self):
        t = tax("t", "u", ["ssn", "itin"])
        t["filing_status"] = "joint"
        self.assertTrue(eligible(person("a", "u", "t", 4), t, "ssn_only"))

    def test_joint_unidentified_spouse_not_assumed_valid(self):
        t = tax("t", "u", ["ssn", "other"])
        t["filing_status"] = "joint"
        self.assertFalse(eligible(person("a", "u", "t", 4), t, "ssn_only"))

    def test_adult_itin_branches(self):
        t = tax("t", "u", ["itin"])
        c = person("a", "u", "t", 4)
        self.assertFalse(eligible(c, t, "ssn_only"))
        self.assertTrue(eligible(c, t, "adult_itin"))

    def test_child_itin_branch(self):
        t, c = tax("t", "u"), person("a", "u", "t", 4, child_id="itin")
        self.assertFalse(eligible(c, t, "adult_itin"))
        self.assertTrue(eligible(c, t, "adult_and_child_itin"))

    def test_non_id_qualifications_not_inferred(self):
        c = person("a", "u", "t", 4)
        c["qualifying_child"] = False
        self.assertFalse(eligible(c, tax("t", "u"), "adult_and_child_itin"))

    def test_partial_replacement_can_lose_current_credit(self):
        t = tax("t", "u", baseline=2200)
        t["receipt"]["delivered"] = [0]*12
        self.assertEqual(credit_delta(3600, t, "delivered", self.p), -2200)

    def test_increment_basis_is_explicit(self):
        t = tax("t", "u", baseline=2200)
        t["receipt"]["delivered"] = [1/12]*6 + [0]*6
        self.p["receipt_basis"] = "increment_only"
        self.assertAlmostEqual(credit_delta(3600, t, "delivered", self.p), 700)
        with self.assertRaises(ValueError):
            credit_delta(0, t, "delivered", self.p)

    def test_baseline_credit_not_double_counted(self):
        t = tax("t", "u", baseline=2200)
        self.assertEqual(credit_delta(3600, t, "full_receipt", self.p), 1400)

    def test_receipt_catchup_separate_from_on_time(self):
        r = self.run_model()["ssn_only"]["scenarios"]
        self.assertAlmostEqual(r["delivered"]["unit_resource_ledger"]["u6"]["ctc_delta"], r["full_receipt"]["unit_resource_ledger"]["u6"]["ctc_delta"])
        self.assertLess(r["delivered"]["payment_reliability"]["mean_on_time_months"], 12)

    def test_full_receipt_dominates_same_available_delivery(self):
        for b in self.run_model().values():
            s = b["scenarios"]
            for uid in s["delivered"]["unit_resource_ledger"]:
                self.assertLessEqual(s["delivered"]["unit_resource_ledger"][uid]["resources"], s["full_receipt"]["unit_resource_ledger"][uid]["resources"] + 1e-8)

    def test_mixed_sibling_exclusion_is_child_specific(self):
        r = self.run_model()["ssn_only"]["mechanisms"]["residual_child_details"]
        by_id = {x["person_id"]: x for x in r}
        self.assertEqual(by_id["c2"]["pattern"][0], "0")
        self.assertEqual(by_id["c3"]["pattern"][0], "1")

    def test_nonpoor_exclusion_not_counted_as_poor_residual(self):
        m = self.run_model()["ssn_only"]["mechanisms"]
        self.assertNotIn("c4", [x["person_id"] for x in m["residual_child_details"]])
        self.assertGreater(m["coverage_flags_all_children_not_residual_counts"]["legal_exclusion"], 3)

    def test_ordered_and_overlap_partition_delivered_poor(self):
        for b in self.run_model().values():
            poor = b["scenarios"]["delivered"]["all_children"]["poor_children"]
            m = b["mechanisms"]
            self.assertAlmostEqual(sum(m["ordered_attribution_weighted_children"].values()), poor)
            self.assertAlmostEqual(sum(m["overlap_patterns_weighted_children"].values()), poor)

    def test_no_care_slot_even_full_receipt(self):
        u = self.d["units"][0]
        effect = service_effect(u, 2030, "full_receipt")
        self.assertEqual(effect["expense_reduction"], 0)
        self.assertIn("care", effect["unavailable"])

    def test_prek_slot_gate(self):
        u = self.d["units"][0]
        u["delivery"]["full_receipt"]["care"] = False
        u["delivery"]["full_receipt"]["prek"] = True
        self.assertEqual(service_effect(u, 2030, "full_receipt")["expense_reduction"], 2000)

    def test_prek_and_care_do_not_double_count(self):
        u = self.d["units"][0]
        u["delivery"]["full_receipt"]["care"] = True
        u["delivery"]["full_receipt"]["prek"] = True
        self.assertEqual(service_effect(u, 2030, "full_receipt")["expense_reduction"], 6000)

    def test_care_transition_and_mature_schedule(self):
        u = self.d["units"][2]
        self.assertEqual(service_effect(u, 2030, "full_receipt")["expense_reduction"], 0)
        self.assertEqual(service_effect(u, 2034, "full_receipt")["expense_reduction"], 4200)

    def test_strict_75_percent_boundary(self):
        u = self.d["units"][2]
        u["care_family_income"] = 37500
        self.assertEqual(service_effect(u, 2030, "full_receipt")["expense_reduction"], 0)
        u["care_family_income"] -= 1
        self.assertEqual(service_effect(u, 2030, "full_receipt")["expense_reduction"], 7000)

    def test_care_above_250_percent_ineligible(self):
        u = self.d["units"][2]
        u["care_family_income"] = 125001
        self.assertEqual(service_effect(u, 2034, "full_receipt")["expense_reduction"], 0)

    def test_capped_work_care_deduction_not_raw_expense(self):
        u = self.d["units"][0]
        u.update(childcare_expense=10000, work_expense=2000, work_care_deduction=3000)
        u["delivery"]["full_receipt"]["care"] = True
        effect = service_effect(u, 2030, "full_receipt")
        self.assertEqual(effect["expense_reduction"], 1000)

    def test_housing_award_and_leaseup_both_required(self):
        u = self.d["units"][1]
        self.assertEqual(service_effect(u, 2030, "delivered")["components"]["voucher"], 0)
        self.assertEqual(service_effect(u, 2030, "full_receipt")["components"]["voucher"], 3500)
        u["voucher_awarded"] = False
        self.assertEqual(service_effect(u, 2030, "full_receipt")["components"]["voucher"], 0)

    def test_housing_spm_cap(self):
        u = self.d["units"][1]
        u["housing_increment_cap"] = 1200
        self.assertEqual(service_effect(u, 2030, "full_receipt")["components"]["voucher"], 1200)

    def test_voucher_awards_use_household_weights(self):
        self.d["units"][1]["unit_weight"] = 100001
        with self.assertRaisesRegex(ValueError, "voucher awards"):
            validate_policy(self.d, self.p)
        self.p["year"] = 2034
        validate_policy(self.d, self.p)

    def test_emergency_aid_award_and_expiration(self):
        u = self.d["units"][0]
        self.assertEqual(service_effect(u, 2030, "full_receipt")["cash"], 1000)
        self.assertEqual(service_effect(u, 2034, "full_receipt")["cash"], 0)
        u["emergency_aid_awarded"] = False
        self.assertEqual(service_effect(u, 2030, "full_receipt")["cash"], 0)

    def test_channel_identity(self):
        for b in self.run_model().values():
            for s in b["scenarios"].values():
                for l in s["unit_resource_ledger"].values():
                    self.assertAlmostEqual(l["total_delta"], l["cash_delta"] + l["expense_reduction"] + l["in_kind_delta"])
                    self.assertAlmostEqual(l["resources"], l["baseline_resources"] + l["total_delta"])

    def test_gap_estimands_are_different(self):
        s = self.run_model()["ssn_only"]["scenarios"]["current_law"]
        self.assertNotEqual(s["all_children"]["child_weighted_gap_dollars"], s["unit_weighted_gap_dollars_child_units"])

    def test_small_cells_suppress_rates(self):
        self.p["min_cell"] = 30
        groups = self.run_model()["ssn_only"]["scenarios"]["current_law"]["subgroups"]["age_group"]
        self.assertTrue(all(x["poor_rate"] is None and x["suppressed"] for x in groups.values()))

    def test_replicate_variance_hand_calculation(self):
        rows = [{"resources": 0, "threshold": 100, "person_weight": 1, "replicate_weights": [2, 0]},
                {"resources": 200, "threshold": 100, "person_weight": 1, "replicate_weights": [0, 2]}]
        v = replicate_intervals(rows)["metrics"]["poor_rate"]
        self.assertAlmostEqual(v["se"], 1)
        self.assertEqual((v["lower95"], v["upper95"]), (0, 1))

    def test_paired_current_law_change_zero(self):
        u = self.run_model()["ssn_only"]["scenarios"]["current_law"]["uncertainty"]
        self.assertEqual(u["metrics"]["poor_rate"]["paired_change"]["se"], 0)

    def test_missing_replicates_reported(self):
        for p in self.d["people"]:
            del p["replicate_weights"]
        self.assertEqual(baseline(self.d)["uncertainty"]["status"], "not_available")

    def test_no_implicit_target_year_projection(self):
        self.d["metadata"].update(kind="source_year", resource_year=2025, dollar_year=2025)
        for p in self.d["people"]:
            p.pop("replicate_weights")
        with self.assertRaisesRegex(ValueError, "target-year"):
            validate_policy(self.d, self.p)

    def test_missing_policy_index_rejected(self):
        self.p["policy_index"] = None
        with self.assertRaises(ValueError):
            validate_policy(self.d, self.p)

    def test_missing_service_flags_rejected(self):
        del self.d["units"][0]["delivery"]["delivered"]["care"]
        with self.assertRaises(ValueError):
            validate_policy(self.d, self.p)

    def test_duplicate_people_rejected(self):
        self.d["people"].append(copy.deepcopy(self.d["people"][0]))
        with self.assertRaises(ValueError):
            baseline(self.d)

    def test_nonfinite_rejected(self):
        self.d["units"][0]["resources"] = float("nan")
        with self.assertRaises(ValueError):
            baseline(self.d)

    def test_credit_reference_cannot_exceed_gross(self):
        self.p["reference_under17"] = 10000
        with self.assertRaises(ValueError):
            self.run_model()

    def test_tax_spm_crosswalk_rejected(self):
        self.d["people"][0]["tax_unit_id"] = "t2"
        with self.assertRaises(ValueError):
            self.run_model()

    def test_receipt_over_one_rejected(self):
        self.d["taxes"][0]["receipt"]["delivered"] = [1]*12
        with self.assertRaises(ValueError):
            self.run_model()

    def test_subgroup_weight_totals_match(self):
        r = self.run_model()["ssn_only"]["scenarios"]["delivered"]
        for group in r["subgroups"].values():
            self.assertEqual(sum(x["weighted_children"] for x in group.values()), 21)


def raw_config():
    return {"metadata": {"kind": "synthetic", "source_vintage": "synthetic CSV", "resource_year": 2025,
                         "dollar_year": 2025, "baseline_description": "synthetic baseline", "weight_basis": "explicit scales"},
            "fields": {key: {"column": col, "scale": .01 if "weight" in key else 1}
                       for key, col in {"household_id": "H_SEQ", "person_number": "PPPOS", "tax_unit_id": "TAX_ID",
                                        "spm_unit_id": "SPM_ID", "age": "A_AGE", "person_weight": "MARSUPWT",
                                        "unit_weight": "SPM_WEIGHT", "resources": "SPM_RESOURCES", "threshold": "SPM_POVTHRESHOLD"}.items()}}


def raw_rows():
    return [{"H_SEQ": "1", "PPPOS": "1", "TAX_ID": "1", "SPM_ID": "00010", "A_AGE": "4",
             "MARSUPWT": "100", "SPM_WEIGHT": "100", "SPM_RESOURCES": "1000", "SPM_POVTHRESHOLD": "20000"},
            {"H_SEQ": "2", "PPPOS": "1", "TAX_ID": "1", "SPM_ID": "00020", "A_AGE": "8",
             "MARSUPWT": "200", "SPM_WEIGHT": "100", "SPM_RESOURCES": "22000", "SPM_POVTHRESHOLD": "20000"}]


class PipelineTests(unittest.TestCase):
    def test_namespaces_tax_and_preserves_spm_id(self):
        d = construct(raw_rows(), raw_config())
        self.assertEqual({t["tax_unit_id"] for t in d["taxes"]}, {"1:1", "2:1"})
        self.assertEqual(d["people"][0]["spm_unit_id"], "00010")

    def test_explicit_weight_scale(self):
        d = construct(raw_rows(), raw_config())
        self.assertEqual(baseline(d)["all_children"]["weighted_children"], 3)
        self.assertAlmostEqual(baseline(d)["all_children"]["poor_rate"], 1/3)

    def test_ambiguous_scale_rejected(self):
        c = raw_config()
        c["fields"]["person_weight"]["scale"] = None
        with self.assertRaises(ValueError):
            construct(raw_rows(), c)

    def test_repeated_unit_inconsistency_rejected(self):
        rows = raw_rows()
        rows[1].update(H_SEQ="1", PPPOS="2", SPM_ID="00010")
        with self.assertRaisesRegex(ValueError, "inconsistent"):
            construct(rows, raw_config())

    def test_cross_spm_tax_rejected(self):
        rows = raw_rows()
        rows[1].update(H_SEQ="1", PPPOS="2")
        with self.assertRaisesRegex(ValueError, "spans"):
            construct(rows, raw_config())

    def test_unknown_ids_not_fabricated(self):
        rows = raw_rows()
        rows[0]["TAX_ID"] = "0"
        d = construct(rows, raw_config())
        self.assertIsNone(d["people"][0]["tax_unit_id"])
        self.assertNotIn("child_id", d["people"][0])

    def test_duplicate_raw_person_rejected(self):
        rows = raw_rows()
        rows.append(copy.deepcopy(rows[0]))
        with self.assertRaises(ValueError):
            construct(rows, raw_config())

    def test_replicates_join_by_keys(self):
        c, rows = raw_config(), raw_rows()
        c.update(replicate_columns=["R1", "R2"], replicate_scale=.01)
        reps = [{"H_SEQ": "2", "PPPOS": "1", "R1": "210", "R2": "190"},
                {"H_SEQ": "1", "PPPOS": "1", "R1": "90", "R2": "110"}]
        d = construct(rows, c, reps)
        self.assertEqual(d["people"][0]["replicate_weights"], [.9, 1.1])

    def test_incomplete_replicate_join_rejected(self):
        c = raw_config()
        c.update(replicate_columns=["R1"], replicate_scale=1)
        with self.assertRaises(ValueError):
            construct(raw_rows(), c, [])

    def test_overlay_cannot_change_census_resources(self):
        d = construct(raw_rows(), raw_config())
        with self.assertRaisesRegex(ValueError, "cannot overwrite"):
            apply_overlay(d, {"units": {"00010": {"resources": 99999}}, "provenance": "test"})

    def test_opm_benchmark_rejected(self):
        with self.assertRaisesRegex(ValueError, "SPM"):
            compare(population(), {"measure": "OPM", "population": "children_under18"})

    def test_benchmark_pass_and_fail_are_explicit(self):
        d = population()
        b = {"measure": "SPM", "population": "children_under18", "resource_year": 2030,
             "source_url": "synthetic", "table": "test", "vintage": "test", "tolerance_rationale": "exact fixture",
             "poor_rate": 18/21, "poor_children": 18, "weighted_children": 21,
             "absolute_tolerances": {"poor_rate": 0, "poor_children": 0, "weighted_children": 0}}
        self.assertTrue(compare(d, b)["pass"])
        b["poor_children"] = 100
        self.assertFalse(compare(d, b)["pass"])

    def test_projection_without_ledger_refused(self):
        with self.assertRaises(ValueError):
            project(population(), {"year": 2030})

    def test_partial_projection_refused(self):
        with self.assertRaisesRegex(ValueError, "every"):
            project(construct(raw_rows(), raw_config()), {"year": 2030, "projection_provenance": "test", "tax_baseline_provenance": "test",
                                  "population_controls_provenance": "test", "units": {}, "taxes": {}, "people": {}})

    def test_projection_before_policy_overlay_required(self):
        with self.assertRaisesRegex(ValueError, "before attaching"):
            project(population(), {"year": 2034})

    def test_complete_projection_and_controls(self):
        source = construct(raw_rows(), raw_config())
        inputs = {"year": 2034, "projection_provenance": "synthetic ledger",
                  "tax_baseline_provenance": "synthetic tax review", "population_controls_provenance": "synthetic controls",
                  "units": {u["spm_unit_id"]: {k: v for k, v in u.items() if k != "spm_unit_id"} for u in source["units"]},
                  "taxes": {t["tax_unit_id"]: {"agi": 0, "current_law_ctc": 0} for t in source["taxes"]},
                  "people": {p["person_id"]: {"person_weight": p["person_weight"], "replicate_weights": [p["person_weight"]]*160} for p in source["people"]},
                  "controls": {"children": {"age_min": 0, "age_max": 17, "weighted_count": 3, "absolute_tolerance": 0}}}
        projected = project(source, inputs)
        self.assertEqual(projected["metadata"]["resource_year"], 2034)
        self.assertEqual(projected["people"][0]["age"], source["people"][0]["age"])
        self.assertEqual(len(projected["people"][0]["replicate_weights"]), 160)
        inputs["controls"]["children"]["weighted_count"] = 999
        with self.assertRaisesRegex(ValueError, "control failed"):
            project(source, inputs)


if __name__ == "__main__":
    unittest.main(verbosity=2)
