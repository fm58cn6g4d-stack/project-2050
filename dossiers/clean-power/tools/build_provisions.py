"""Builds dossiers/clean-power/provisions.json from the provision tables in 4-specification.md.

Role: keeps section 4 and provisions.json one source (TEMPLATE.md, "Consistency while writing"). Each table row whose first
cell is a provision ID becomes an entry; the vehicle comes from section 4's vehicles table, set here by ID.
Run from the repository root:  python3 dossiers/clean-power/tools/build_provisions.py [--check]
"""
import json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
DOSSIER = os.path.normpath(os.path.join(HERE, ".."))
SPEC = os.path.join(DOSSIER, "4-specification.md")
OUT = os.path.join(DOSSIER, "provisions.json")
ID = re.compile(r"^[A-Z]{2,4}-[A-Z]{0,3}\d+[A-Za-z]?\.\d{2}$")

R2 = ("R2", "mandatory", "FY2030 reconciliation act")
R3 = ("R3", "mandatory", "FY2031 reconciliation act")
FLOOR = ("FLOOR", "authorizing", "the clean power and climate act (regular order)")
VEHICLE = {
    **{i: [R2] for i in ["REV-C1G.01", "REV-C1G.02", "REV-C1A.01", "REV-C1P.01", "CLI-2A.01", "CLI-2A.02", "CLI-2A.03",
                         "CLI-2A.04", "CLI-2O.01", "CLI-1A.01", "CLI-1A.02", "CLI-1A.03", "CLI-1A.04", "CLI-9.01",
                         "CLI-10G.01", "CLI-5L.01", "CLI-5W.01", "CLI-7C.01", "CLI-7N.01", "CLI-7K.01", "CLI-13A.01",
                         "CLI-13F.01"]},
    **{i: [R3] for i in ["REV-C2.01", "REV-C3.01", "CLI-5F.01", "CLI-5H.01", "CLI-5H.02", "CLI-10.01", "CLI-10.02",
                         "CLI-11.02", "CLI-11.03", "CLI-11.04", "CLI-11.05", "CLI-11.06", "CLI-11.07"]},
    **{i: [FLOOR] for i in ["CLI-3A.01", "CLI-3A.02", "CLI-3A.03", "CLI-3A.04", "CLI-4A.01", "CLI-4E.01", "CLI-4H.01",
                            "CLI-14.01", "CLI-14.02", "CLI-6A.01", "CLI-6A.02", "CLI-6A.03", "CLI-10.03", "CLI-9.02",
                            "CLI-7.01", "CLI-8.01", "CLI-11.01", "CLI-11.08"]},
}
COST = {"REV": "6-cost.md, part 1 (memo 1 B)", "CLI-2": "6-cost.md, part 1 (the dividend's own channel)",
        "CLI-1": "6-cost.md, part 1 (credits, as booked)", "CLI-9": "6-cost.md, part 1 (credits and industry, as booked)",
        "CLI-3": "6-cost.md, part 1 (standards, as booked)", "CLI-4": "6-cost.md, part 1 (no direct cost)",
        "CLI-14": "6-cost.md, part 2 (inside EPA's base)", "CLI-6": "6-cost.md, part 1 (no direct cost; FERC is fee-funded)",
        "CLI-10": "6-cost.md, part 1 (memo 4 B)", "CLI-5": "6-cost.md, part 1 (bills and add-ons; memo 5 B)",
        "CLI-7": "6-cost.md, part 1 (adaptation, as booked)", "CLI-8": "6-cost.md, part 1 (no direct cost)",
        "CLI-11": "6-cost.md, part 1 (memo 7 B)", "CLI-13": "6-cost.md, part 1 (farms and forests, as booked)"}


def cost_source(pid):
    for k in sorted(COST, key=len, reverse=True):
        if pid.startswith(k):
            return COST[k]
    return "6-cost.md"


def build():
    out = []
    for line in open(SPEC, encoding="utf-8"):
        cells = [c.strip() for c in line.strip().strip("|").split("|")] if line.startswith("| ") else []
        if len(cells) != 5 or not ID.match(cells[0]):
            continue
        pid, prov, params, agency, ev = cells
        m = re.match(r"\*\*(.+?)\*\*\s*\((.+)\)\s*$", prov)
        title, status = (m.group(1), m.group(2)) if m else (prov, "")
        decs = []
        if re.search(r"\bmemo\b", status):
            decs.append("DEC-2026-11-13-06")
        if re.search(r"\bpoints?\b", status):
            decs.append("DEC-2026-11-13-07")
        evidence = [e.strip() for e in ev.split(",") if e.strip().startswith("EV-")]
        out.append(dict(id=pid, title=title, agenda=pid.rsplit(".", 1)[0], status=status, decisions=decs,
                        parameters=params, eligibility="",
                        vehicle=[dict(vehicle=v, kind=k, note=n) for v, k, n in VEHICLE[pid]],
                        agency=agency, current_law="", evidence=evidence, sources=[], cost_source=cost_source(pid),
                        spec="dossiers/clean-power/4-specification.md"))
    missing = sorted(set(VEHICLE) - {p["id"] for p in out})
    if missing:
        raise SystemExit(f"vehicle set for IDs not in section 4: {missing}")
    return out


if __name__ == "__main__":
    text = json.dumps(build(), indent=1, ensure_ascii=False) + "\n"
    if "--check" in sys.argv:
        sys.exit(0 if os.path.exists(OUT) and open(OUT, encoding="utf-8").read() == text else "provisions.json is stale")
    open(OUT, "w", encoding="utf-8").write(text)
    print(f"{len(json.loads(text))} provisions written")
