#!/usr/bin/env python3
"""How far LAB-11.01's benefit cap (two-thirds of the state's average weekly wage) varies by state.

Role: memo 7's table for Espen's November 18 answer W8 (`dossiers/work/memos/7-unemployment-insurance.md`,
"Who pays, and how far the cap varies"). Status: draft (stage F, revision for the November 18 answers).
Project arithmetic on BLS's 2025 annual QCEW average weekly wages (EV-WRK-478, SRC-5815), not a forecast.
Run:  python3 dossiers/work/tools/ui_cap_by_state.py           (table in Markdown)
      python3 dossiers/work/tools/ui_cap_by_state.py --check   (spot checks)

Method: cap = 2/3 x the state's 2025 annual average weekly wage, all industries and ownerships. A state's
legal figure is set by its own law and lags a year or more, so this is a guide to the spread, not each
state's exact cap. The weekly benefit is 75% of high-quarter weekly pay up to the cap (LAB-11.01), so the
cap binds for a worker whose high-quarter weekly pay is above cap / 0.75, about 0.89 of the state's wage.
"""
import csv
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "..", "..", "..", "library", "text", "wrk-r18-bls-qcew-2025-annual-all-industries.txt")

NAMES = {
    "01": "Alabama", "02": "Alaska", "04": "Arizona", "05": "Arkansas", "06": "California",
    "08": "Colorado", "09": "Connecticut", "10": "Delaware", "11": "District of Columbia",
    "12": "Florida", "13": "Georgia", "15": "Hawaii", "16": "Idaho", "17": "Illinois",
    "18": "Indiana", "19": "Iowa", "20": "Kansas", "21": "Kentucky", "22": "Louisiana",
    "23": "Maine", "24": "Maryland", "25": "Massachusetts", "26": "Michigan", "27": "Minnesota",
    "28": "Mississippi", "29": "Missouri", "30": "Montana", "31": "Nebraska", "32": "Nevada",
    "33": "New Hampshire", "34": "New Jersey", "35": "New Mexico", "36": "New York",
    "37": "North Carolina", "38": "North Dakota", "39": "Ohio", "40": "Oklahoma", "41": "Oregon",
    "42": "Pennsylvania", "44": "Rhode Island", "45": "South Carolina", "46": "South Dakota",
    "47": "Tennessee", "48": "Texas", "49": "Utah", "50": "Vermont", "51": "Virginia",
    "53": "Washington", "54": "West Virginia", "55": "Wisconsin", "56": "Wyoming",
    "72": "Puerto Rico", "78": "U.S. Virgin Islands", "US": "United States",
}
# Worked examples at 2025 wages: weekly pay in the high quarter (40 hours a week).
EXAMPLES = [("$17 an hour", 17 * 40), ("$30 an hour", 30 * 40), ("$45 an hour", 45 * 40)]


def load():
    """Average weekly wage by area, from the saved QCEW text (after its header)."""
    with open(SRC) as f:
        lines = f.read().split("---\n", 1)[1].splitlines()
    out = {}
    for r in csv.DictReader(lines):
        fips = r["area_fips"]
        if r["own_code"] == "0" and r["industry_code"] == "10" and (
                (fips.endswith("000") and r["agglvl_code"] == "50") or fips == "US000"):
            out[fips[:2]] = int(r["annual_avg_wkly_wage"])
    return out


def benefit(weekly_pay, aww, rate=0.75):
    return min(rate * weekly_pay, 2 / 3 * aww)


def main():
    aww = load()
    if "--check" in sys.argv:
        assert aww["28"] == 1024 and aww["24"] == 1568 and aww["US"] == 1514 and aww["72"] == 700
        assert round(2 / 3 * aww["28"]) == 683 and round(2 / 3 * aww["24"]) == 1045
        assert len(aww) == 54  # 50 states, D.C., Puerto Rico, the Virgin Islands and the U.S.
        print("ui_cap_by_state: checks pass")
        return
    rows = sorted(aww.items(), key=lambda kv: kv[1])
    print("| State | Average weekly wage, 2025 | Cap: two-thirds | " +
          " | ".join(f"Benefit at {n}" for n, _ in EXAMPLES) + " |")
    print("| --- | --- | --- |" + " --- |" * len(EXAMPLES))
    for k, v in rows:
        cells = [f"${benefit(p, v):,.0f}" for _, p in EXAMPLES]
        print(f"| {NAMES[k]} | ${v:,} | ${2 / 3 * v:,.0f} | " + " | ".join(cells) + " |")
    states = [v for k, v in aww.items() if k not in ("US", "72", "78")]
    print()
    print(f"States and D.C.: cap from ${2 / 3 * min(states):,.0f} to ${2 / 3 * max(states):,.0f}; "
          f"middle state ${2 / 3 * sorted(states)[len(states) // 2]:,.0f}")


if __name__ == "__main__":
    main()
