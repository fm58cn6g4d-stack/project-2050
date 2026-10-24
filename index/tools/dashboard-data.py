"""Writes the ledger dashboard's data files (index/data/dashboard/) from ledger.json and paths.json.

The dashboard (https://claude.ai/artifact/RDuHM7DqCwvLUtVaB4ANMs) reads these as attached files: bills, revenue,
cuts (with alternative_to: rows not summed), conflicts and paths (Senate floor days under each D2 path).
After a run that changes them, the files are uploaded to the dashboard again (a Claude session does this).
"""
import json, os
L = json.load(open("ledger.json")); P = json.load(open("paths.json"))
os.makedirs("dashboard", exist_ok=True)
for name, rows in (("bills", L["bills"]), ("revenue", L["revenue"]), ("cuts", L["cuts"]),
                   ("conflicts", L["conflicts"]), ("paths", [dict(p, key=p["path"][0]) for p in P])):
    with open(os.path.join("dashboard", name + ".json"), "w") as f:
        json.dump(rows, f, indent=1, ensure_ascii=False)
        f.write("\n")
print("wrote dashboard/: bills, revenue, cuts, conflicts, paths")

C = json.load(open("calendar-scenarios.json"))
with open("dashboard/calendar.json", "w") as f:
    json.dump(dict(meta=C["meta"], runs=[{k:r[k] for k in ("run_id","condition","capacity","strategy","merged","frontload","shock","checks","scope_completed","scope_total","unfinished","on_frontier")} for r in C["runs"]]), f, indent=1)
