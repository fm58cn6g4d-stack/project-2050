#!/usr/bin/env python3
"""Recreate tests and artificial diagnostics from any working directory."""
import argparse
import csv
import importlib.util
import io
import json
import platform
import re
import subprocess
import sys
import tempfile
import unittest
import zipfile
from pathlib import Path
from types import SimpleNamespace
from model import simulate, baseline, write_json, sha256
from fixtures import population, policy, unit, tax, person
from test_model import raw_config, raw_rows

ROOT = Path(__file__).resolve().parent


def legacy_regression():
    path = ROOT / "recovered/model-upstream-8a8f4b.py"
    if sha256(path) != "702c8e45badb933eb59851718a57dfaed7f0164e09a0961c7bdc1b9d88334bb9":
        raise ValueError("recovered upstream source differs from verified GitHub bytes")
    spec = importlib.util.spec_from_file_location("upstream_model", path)
    old = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(old)
    u = {"spm_unit_id": "u", "weight": 1, "spm_threshold": 20000, "spm_resources": 1000,
         "spm_care_expense": 0, "care_family_income": 0, "state_median_income": 50000,
         "care_slot": 0, "voucher_awarded": 0, "prek_spm_delta": 0,
         "school_meal_spm_delta": 0, "summer_ebt_spm_delta": 0,
         "voucher_spm_delta": 0, "emergency_aid_spm_delta": 0}
    for key in ("care", "prek", "school_meal", "summer_ebt", "voucher_leaseup", "emergency_aid"):
        for scenario in ("delivered", "enhanced"):
            u[key + "_" + scenario] = 0
    t = {"tax_unit_id": "t", "spm_unit_id": "u", "agi": 0, "filing_status": "head",
         "adult_id": "ssn", "current_law_ctc": 0, "months_delivered": 12, "months_enhanced": 12}
    ps = [{"person_id": "a", "spm_unit_id": "u", "tax_unit_id": "t", "age": 8, "child_id": "ssn"},
          {"person_id": "b", "spm_unit_id": "u", "tax_unit_id": "t", "age": 10, "child_id": "itin"}]
    with tempfile.TemporaryDirectory() as directory:
        args = {}
        for name, rows in (("units", [u]), ("taxes", [t]), ("people", ps)):
            dest = Path(directory) / (name+".csv")
            with dest.open("w", newline="") as f:
                writer = csv.DictWriter(f, fieldnames=rows[0])
                writer.writeheader()
                writer.writerows(rows)
            args[name] = str(dest)
        args.update(year=2030, vintage="synthetic mixed siblings", policy_index=1,
                    reference_under17=2200, reference_age17=2200)
        old_result = old.run(SimpleNamespace(**args))
    old_excluded = old_result["results"]["ssn_only"]["mechanisms"]["ordered_attribution_weighted_children"]["legal_exclusion"]
    data = {"schema_version": 2, "metadata": population()["metadata"], "units": [unit("u")],
            "taxes": [tax("t", "u")], "people": [person("a", "u", "t", 8), person("b", "u", "t", 10, child_id="itin")]}
    new_result = simulate(data, policy())
    new_excluded = new_result["results"]["ssn_only"]["mechanisms"]["ordered_attribution_weighted_children"]["legal_exclusion"]
    if (old_excluded, new_excluded) != (2, 1):
        raise AssertionError("mixed-sibling characterization/regression failed")
    return {"fixture": "two poor siblings, one SSN and one ITIN, equal person weights",
            "upstream_source_sha256": sha256(path), "upstream_excluded_children": old_excluded,
            "rebuilt_excluded_children": new_excluded, "expected_excluded_children": 1,
            "status": "original defect reproduced; rebuilt attribution correct"}


def cli_smoke(out):
    raw_path = out / "raw-person.csv"
    with raw_path.open("w", newline="") as f:
        rows = raw_rows()
        w = csv.DictWriter(f, fieldnames=rows[0])
        w.writeheader()
        w.writerows(rows)
    write_json(out / "raw-mapping.json", raw_config())
    zipped = out / "raw-fixture.zip"
    with zipfile.ZipFile(zipped, "w") as z:
        z.writestr(zipfile.ZipInfo("person.csv", (2026, 10, 24, 0, 0, 0)), raw_path.read_bytes())
        z.writestr(zipfile.ZipInfo("unrelated.csv", (2026, 10, 24, 0, 0, 0)), "unused\n0\n")
    commands = [[sys.executable, str(ROOT/"preprocess.py"), "--raw", str(zipped), "--member", "person.csv",
                 "--mapping", str(out/"raw-mapping.json"), "--output", str(out/"raw-normalized.json")],
                [sys.executable, str(ROOT/"model.py"), "--data", str(out/"raw-normalized.json"),
                 "--baseline-only", "--output", str(out/"raw-baseline.json")]]
    for command in commands:
        subprocess.run(command, check=True, capture_output=True, text=True)
    result = json.loads((out/"raw-baseline.json").read_text())
    if abs(result["all_children"]["poor_rate"] - 1/3) > 1e-10:
        raise AssertionError("raw ZIP -> normalized -> baseline CLI pipeline failed")
    # Exercise target-year model CLI and documented path handling too.
    subprocess.run([sys.executable, str(ROOT/"model.py"), "--data", str(ROOT/"synthetic/population.json"),
                    "--policy", str(ROOT/"synthetic/policy-2030.json"), "--output", str(out/"cli-model.json")],
                   check=True, capture_output=True, text=True)
    return {"status": "passed", "raw_fixture_children": 2, "weighted_children": 3,
            "baseline_poor_rate": 1/3, "meaning": "artificial CLI integration check only"}


def run(out):
    out.mkdir(parents=True, exist_ok=True)
    suite = unittest.defaultTestLoader.discover(str(ROOT), pattern="test_model.py")
    transcript = io.StringIO()
    result = unittest.TextTestRunner(stream=transcript, verbosity=2).run(suite)
    text = re.sub(r"Ran (\d+) tests in [\d.]+s", r"Ran \1 tests (elapsed time omitted for reproducibility)", transcript.getvalue())
    (out/"test-results.txt").write_text("Python " + platform.python_version() + "\n" + text, encoding="utf-8")
    if not result.wasSuccessful():
        raise SystemExit(text)
    write_json(out/"legacy-regression.json", legacy_regression())
    write_json(out/"cli-integration.json", cli_smoke(out))
    records = []
    for year in (2030, 2034):
        data, params = population(), policy(year)
        output = simulate(data, params)
        write_json(out/f"synthetic-{year}.json", output)
        for branch, b in output["results"].items():
            for scenario, s in b["scenarios"].items():
                c = s["all_children"]
                records.append({"status": "SYNTHETIC_NOT_EMPIRICAL", "year": year, "id_branch": branch,
                    "scenario": scenario, "weighted_children": c["weighted_children"], "poor_children": c["poor_children"],
                    "poor_rate": c["poor_rate"], "deep_poor_rate": c["deep_poor_rate"], "below150_rate": c["below150_rate"],
                    "child_weighted_gap": c["child_weighted_gap_dollars"], "unit_weighted_gap": s["unit_weighted_gap_dollars_child_units"],
                    **s["unit_weighted_resource_deltas_not_fiscal_cost"]})
    with (out/"synthetic-scenarios.csv").open("w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=records[0])
        w.writeheader()
        w.writerows(records)
    files = sorted(p for p in out.iterdir() if p.is_file() and p.name not in ("MANIFEST.sha256", "validation-summary.json"))
    hashes = {p.name: sha256(p) for p in files}
    write_json(out/"validation-summary.json", {"tests_run": result.testsRun, "failures": len(result.failures),
        "errors": len(result.errors), "python": platform.python_version(), "scenarios_generated": len(records),
        "legacy_regression": "passed", "cli_integration": "passed", "national_calibration": "NOT_RUN_NO_CPS_DATA",
        "files": hashes})
    files.append(out/"validation-summary.json")
    (out/"MANIFEST.sha256").write_text("".join(f"{sha256(p)}  {p.name}\n" for p in sorted(files)), encoding="utf-8")
    print(f"PASS: {result.testsRun} tests; legacy regression; raw ZIP and policy CLI checks; {len(records)} artificial scenario rows")


if __name__ == "__main__":
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--out", type=Path, default=ROOT/"diagnostics")
    run(p.parse_args().out.resolve())
