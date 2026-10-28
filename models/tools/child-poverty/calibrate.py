#!/usr/bin/env python3
"""Compare a named public-use baseline with predeclared child-SPM benchmarks.

This does not adjust weights or force a fit. Public-use/internal differences
need a documented tolerance and explanation, not an undisclosed correction.
"""
import argparse
from model import baseline, load_json, write_json, num


def compare(data, benchmark):
    meta = data["metadata"]
    if benchmark.get("measure") != "SPM" or benchmark.get("population") != "children_under18":
        raise ValueError("benchmark must be SPM for children under 18; OPM is not interchangeable")
    if benchmark.get("resource_year") != meta["resource_year"]:
        raise ValueError("benchmark year mismatch")
    for k in ("source_url", "table", "vintage", "tolerance_rationale"):
        if not benchmark.get(k):
            raise ValueError(f"benchmark.{k} required")
    values = baseline(data)["all_children"]
    checks = {}
    for metric in ("poor_rate", "weighted_children", "poor_children"):
        expected = num(benchmark.get(metric), metric, 0)
        tolerance = num(benchmark.get("absolute_tolerances", {}).get(metric), metric + " tolerance", 0)
        observed = values[metric]
        checks[metric] = {"observed": observed, "expected": expected, "absolute_tolerance": tolerance,
                          "difference": observed - expected, "pass": abs(observed - expected) <= tolerance}
    return {"scope": "source-year public-use benchmark comparison only", "benchmark": benchmark,
            "checks": checks, "pass": all(c["pass"] for c in checks.values()),
            "national_policy_estimate_ready": False}


if __name__ == "__main__":
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--data", required=True)
    p.add_argument("--benchmark", required=True)
    p.add_argument("--output", required=True)
    a = p.parse_args()
    result = compare(load_json(a.data), load_json(a.benchmark))
    write_json(a.output, result)
    raise SystemExit(0 if result["pass"] else 1)
