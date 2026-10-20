#!/usr/bin/env python3
"""Checks that the transportation model still gives Draft 2's figures. Run from anywhere:
    python3 index/tools/transportation/test_moving_america.py            # protected figures + golden printout
    python3 index/tools/transportation/test_moving_america.py --legacy   # also rerun the old overlay stack (Python 3.12+)
A failure means a figure moved. That is a proposal for Espen, not a fix: update Draft 2, then rerun run-all.sh."""
import os, subprocess, sys, tempfile
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import moving_america as MA, report

# Draft 2's protected figures ($B, percent of GDP, percent coverage)
PROTECTED = dict(program_fy32_36=936.57, general_fund_fy32_36=390.73, expansion_fy32_36=123.66, topups_fy32_36=267.07,
                 draw_avg_fy32_36=0.180, draw_peak_fy32_36=0.200, draw_all_in_peak=0.208, draw_avg_fy42_46=0.026,
                 renewal_coverage_fy42_46={"hwy": 95, "tra": 109, "rail": 135})

def check():
    fails = []
    f = report.figures()
    for k, v in PROTECTED.items():
        if f[k] != v: fails.append(f"{k}: model {f[k]}, Draft 2 {v}")
    # dedicated receipts: Draft 2 prints $545.84B (program less general fund); the period sum rounds to 545.85
    if round(f["program_fy32_36"] - f["general_fund_fy32_36"], 2) != 545.84: fails.append("dedicated FY2032-36 is not $545.84B")
    s = MA.score_2029()
    if round(s["net"], 1) != 290.0: fails.append(f"2029 act net revenue {s['net']:.1f}, Draft 2 290.0")
    if round(MA.expansion_authority(), 2) != 123.70: fails.append("expansion authority is not $123.70B")
    lines = []; report.main(out=lines.append)
    golden = open(os.path.join(HERE, "golden", "report.txt")).read().splitlines()
    if lines != golden:
        bad = next(i for i, (a, b) in enumerate(zip(lines + [""] * len(golden), golden + [""] * len(lines))) if a != b)
        fails.append(f"printout differs from golden/report.txt at line {bad + 1}: {lines[bad] if bad < len(lines) else ''!r}")
    if "--legacy" in sys.argv and sys.version_info < (3, 12):
        fails.append("--legacy needs Python 3.12 or later (the old scripts use 3.12 f-string syntax)")
    elif "--legacy" in sys.argv:
        with tempfile.TemporaryDirectory() as tmp:   # the old scripts can write files into the current folder
            old = subprocess.run([sys.executable, os.path.join(HERE, "legacy", "final_v3.py")], cwd=tmp,
                                 capture_output=True, text=True, check=True).stdout.splitlines()
        if old != open(os.path.join(HERE, "golden", "legacy-final-v3.txt")).read().splitlines():
            fails.append("legacy/final_v3.py no longer matches golden/legacy-final-v3.txt")
    return fails

if __name__ == "__main__":
    fails = check()
    for x in fails: print("FAIL", x)
    if fails: sys.exit(1)
    if "--quiet" not in sys.argv: print("ok: Draft 2's figures reproduced")
