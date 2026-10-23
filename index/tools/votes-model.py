"""Vote simulator: the odds the agenda passes the 2029-30 Congress, bill by bill, under each D2 rules path.

Ported from the war-game simulator (archive/wargame-trifecta-2029-simulator.jsx) and re-pointed at the ledger:
the bills are the ledger's rows, the reconciliation packages are its R1-R3 vehicles (with the revenue that rides
them), and the regular-order bills get floor time from the same day counts as ledger-paths.py.

How a vote works (the war game's model, unchanged):
- Each Democratic senator outside the roster is "solid"; on each bill at most one solid member defects, with
  probability defect_solid x the number of solid members.
- Each roster member objects to a bill with probability defect[archetype] x caution(margin) (x1.35 for an
  independent), capped at 0.95. caution = 1 + (5 - margin) x 0.07, held to 0.7-1.6: narrow winners are warier.
- Republicans cross over on a bill with gop_pool tries at gop_prob each.
- A reconciliation package needs a simple majority (Vice President breaks a tie) and gets no Republican votes; a
  member votes no on it while it holds any provision they object to. Departure from the war game, whose two-bill
  packages could pass as written: the ledger's R2 holds two dozen provisions, so as written it almost never passes,
  and real packages (ARP, IRA) passed after leadership dropped what holdouts objected to. So when a package is
  short, the provision whose removal wins back the most votes is dropped, and again, until it passes; the model
  reports how often each package passes as written, how often some version passes, and how often each provision
  survives into the enacted version.
- A regular-order bill needs cloture: 60, or a majority once the rules change for that bill is adopted. The rules
  vote: each solid member and roster member supports it with the probability for their archetype (the carve-out is
  easier than full reform), less the stated number of holdouts; it needs 50 plus the Vice President.
- The House: 34 frontliners each defect with probability house_sweep x 0.11; the bill needs 218. For a package or
  the omnibus a frontliner reacts to its most exposed provision (the war game's any-provision rule would sink every
  multi-title package, which the 2021-22 House did not).
Calendar: under each path a regular-order bill also needs floor days. Capacity is reserved for DEM-1 and SS-1 first, then bills are taken in target-window order (must-pass first within a window) against
the 163-day budget (less the reconciliation bills and the rules vote); one that does not fit gets no first-Congress
vote. Annual appropriations (CAP-7, NSC-1 ...) are one omnibus vote with a bipartisan crossover pool.
CAP-7S targets R1; this routing assumes eligibility and does not model Byrd/jurisdiction review.

Inputs: index/data/inputs/votes-bills.csv (per-bill parameters, each with its basis) and votes-senate.csv (the
roster and which seats each seat-count scenario includes). Every parameter is the war game's or an estimate.
Writes votes.json and vote-simulation.md. Run after ledger-build.py and ledger-paths.py.
"""
import json, math, os, random, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from inputs import read, num, flag

N = 4000                 # trials per scenario
SEED = 20290120
BASE_SEATS = 43          # Democratic seats not on the roster's races (the war game's base, incl. the three sitting members listed)
HOUSE_D = 221            # Democratic House seats in 2029 (the war game's default, D+6 in 2026); estimate
HOUSE_FRONTLINE, HOUSE_DRAG = 34, 0.11
HOLDOUTS = 1             # senators who vote against any rules change regardless (the war game's default)
PLANNING_SEATS = 53      # D1: plan for 52-54
BUDGET = 163             # first-Congress Senate floor days
OMNIBUS_GOP = (10, 0.40) # Republican crossover on the annual appropriations omnibus (estimate)
# Rules-vote support by archetype. Carve-out (G) and full reform (F, E) are the war game's; C, the talking
# filibuster offered to holdouts, is set halfway between (estimate).
REFORM = {"carveout": dict(solid=0.995, progressive=0.998, moderate=0.92, populist=0.80, institutionalist=0.65),
          "full": dict(solid=0.99, progressive=0.995, moderate=0.85, populist=0.65, institutionalist=0.50)}
REFORM["talking"] = {k: (REFORM["carveout"][k] + REFORM["full"][k]) / 2 for k in REFORM["full"]}
PATHS = {  # path: (rules package, which bills get majority cloture once it is adopted)
    "F": ("full", "all"), "C": ("talking", "all"), "E": ("full", "all"), "G": ("carveout", "carveout"), "none": (None, "none")}
PATH_NAMES = {"F": "F, graduated cloture (decided)", "C": "C, talking filibuster (opening offer)", "E": "E, majority cloture (upper bound)",
              "G": "G, democracy carve-out (fallback)", "none": "No rules change"}
MUST_PASS = ["DEM-1", "HLT-3", "CLI-6", "CLI-7", "IMM-1", "AI-1", "AI-4"]

clamp = lambda v, a, b: max(a, min(b, v))
caution = lambda margin: clamp(1 + (5 - margin) * 0.07, 0.7, 1.6)

def load():
    bills = []
    for r in read("votes-bills.csv"):
        d = {k: float(r["defect_" + k]) for k in ("solid", "moderate", "populist", "progressive")}
        bills.append(dict(id=r["id"], vehicle=r["vehicle"], defect=d, gop_pool=int(r["gop_pool"]), gop_prob=float(r["gop_prob"]),
                          house_sweep=float(r["house_sweep"]), carveout=flag(r["carveout"]), basis=r["basis"], label=r["label"]))
    senate = read("votes-senate.csv")
    return bills, senate

def roster_for(senate, seats):
    col = f"in_{seats}"
    members = [dict(seat=r["seat"], archetype=r["archetype"], margin=float(r["margin"]), ind=flag(r["independent"]))
               for r in senate if flag(r[col])]
    races = sum(1 for r in senate if flag(r[col]) and r["cycle"] != "sitting")
    return BASE_SEATS + races, members

def obj_p(bill, m):
    d = bill["defect"].get(m["archetype"], bill["defect"]["moderate"])
    return clamp(d * caution(m["margin"]) * (1.35 if m["ind"] else 1), 0, 0.95)

def house_pass(p_frontliner):
    """P(at most HOUSE_D - 218 of the frontliners defect)."""
    slack = HOUSE_D - 218
    if slack < 0: return 0.0
    return sum(math.comb(HOUSE_FRONTLINE, k) * p_frontliner ** k * (1 - p_frontliner) ** (HOUSE_FRONTLINE - k) for k in range(min(slack, HOUSE_FRONTLINE) + 1))

def calendar(ledger, paths):
    """Capacity allocation, not a dated schedule: protect DEM/SS, then target windows.
    Reservation order does not require other bills to wait for SS or R1.
    Seasonal labels are windows, not guessed passage months.
    """
    fast = {"INT-1", "CAP-8", "LAB-9D"}; top = ["DEM-1", "DEM-5", "LAB-1", "RTS-1", "HLT-3", "SS-1"]
    floor = sorted([b for b in ledger["bills"] if b["rail"] == "FLOOR" and b["floor_days"] > 0 and b["id"] != "D2-RULES"],
                   key=lambda b: (b["id"] not in {"DEM-1", "SS-1"}, b["target"], b["id"] not in MUST_PASS, b["id"]))
    days_fn = {"F": lambda b: b["floor_days"] if b["id"] in fast else max(b["floor_days"], 4.5),
               "C": lambda b: max(b["floor_days"], 15) if b["id"] in top else b["floor_days"],
               "E": lambda b: b["floor_days"], "G": lambda b: b["floor_days"], "none": lambda b: b["floor_days"]}
    room = BUDGET - ledger["summary"]["recon_days"] - 4
    out = {}
    for p, fn in days_fn.items():
        used, fits = 0.0, {}
        for b in floor:
            used += fn(b); fits[b["id"]] = used <= room
        out[p] = fits
    return out

def simulate(bills, seats, members, holdouts=HOLDOUTS, seed=SEED):
    rng = random.Random(seed).random
    solid = seats - len(members)
    vehicles = {v: [b for b in bills if b["vehicle"] == v] for v in ("R1", "R2", "R3", "APPROPS")}
    floor = [b for b in bills if b["vehicle"] == "FLOOR"]
    P = {b["id"]: [obj_p(b, m) for m in members] for b in bills}
    sen = {p: {b["id"]: 0 for b in floor} for p in PATHS}
    pkg = {v: 0 for v in vehicles}; intact = {v: 0 for v in vehicles}; survive = {v: {b["id"]: 0 for b in vehicles[v]} for v in ("R1", "R2", "R3")}
    omni = {p: 0 for p in PATHS}; reform = {p: 0 for p in PATHS}
    for _ in range(N):
        objected = {b["id"]: [rng() < q for q in P[b["id"]]] for b in bills}
        solid_def = {b["id"]: 1 if rng() < b["defect"]["solid"] * solid else 0 for b in bills}
        adopted = {}
        for p, (kind, _) in PATHS.items():
            if kind is None: adopted[p] = False; continue
            r = REFORM[kind]
            votes = round(solid * r["solid"]) + sum(1 for m in members if rng() < r.get(m["archetype"], 0.6)) - holdouts
            adopted[p] = votes >= 50
            reform[p] += adopted[p]
        # reconciliation packages: no Republican votes; leadership trims provisions until a majority holds
        for v in ("R1", "R2", "R3"):
            keep = [b["id"] for b in vehicles[v]]
            objs = [{k for k in keep if objected[k][i]} for i in range(len(members))]
            yes = lambda ks: solid + sum(1 for o in objs if not (o & ks))
            cur = set(keep)
            intact[v] += yes(cur) >= 50
            while cur and yes(cur) < 50:
                no = [o & cur for o in objs if o & cur]
                unlock = {k: sum(1 for o in no if o == {k}) for k in cur}
                hits = {k: sum(1 for o in no if k in o) for k in cur}
                drop = max(cur, key=lambda k: (unlock[k], hits[k], k))
                cur.discard(drop)
            if cur:
                pkg[v] += 1
                for k in cur: survive[v][k] += 1
        # annual appropriations omnibus
        mem = vehicles["APPROPS"]
        yes = solid + sum(1 for i in range(len(members)) if not any(objected[b["id"]][i] for b in mem))
        yes += sum(1 for _ in range(OMNIBUS_GOP[0]) if rng() < OMNIBUS_GOP[1])
        for p, (kind, scope) in PATHS.items():
            majority = adopted[p] and scope == "all"
            omni[p] += (yes >= 50) if majority else (yes >= 60)
        # regular-order bills
        for b in floor:
            yes = solid - solid_def[b["id"]] + objected[b["id"]].count(False)
            yes += sum(1 for _ in range(b["gop_pool"]) if rng() < b["gop_prob"])
            for p, (kind, scope) in PATHS.items():
                majority = adopted[p] and (scope == "all" or (scope == "carveout" and b["carveout"]))
                sen[p][b["id"]] += (yes >= 50) if majority else (yes >= 60)
    hp = lambda mem: house_pass(max(b["house_sweep"] for b in mem) * HOUSE_DRAG)
    res = dict(seats=seats, holdouts=holdouts, reform={p: reform[p] / N for p in PATHS},
               packages={v: dict(senate=pkg[v] / N, intact=intact[v] / N, house=hp(vehicles[v]), members=[b["id"] for b in vehicles[v]],
                                 survive={k: c / N for k, c in survive[v].items()}) for v in ("R1", "R2", "R3")},
               omnibus={p: dict(senate=omni[p] / N, house=hp(vehicles["APPROPS"])) for p in PATHS},
               floor={p: {b["id"]: dict(senate=sen[p][b["id"]] / N, house=hp([b])) for b in floor} for p in PATHS})
    for v, d in res["packages"].items(): d["enact"] = d["senate"] * d["house"]
    for p in PATHS:
        res["omnibus"][p]["enact"] = res["omnibus"][p]["senate"] * res["omnibus"][p]["house"]
        for d in res["floor"][p].values(): d["enact"] = d["senate"] * d["house"]
    return res

def main():
    ledger = json.load(open("ledger.json")); paths = json.load(open("paths.json"))
    bills, senate = load()
    labels = {b["id"]: b["label"] for b in bills}
    fits = calendar(ledger, paths)
    runs = {}
    for seats in (51, 52, 53, 54):
        s, members = roster_for(senate, seats)
        assert s == seats, (seats, s)
        runs[seats] = simulate(bills, s, members)
    s, members = roster_for(senate, PLANNING_SEATS)
    hold = {h: simulate(bills, s, members, holdouts=h)["reform"] for h in (0, 2, 3)}
    hold[HOLDOUTS] = runs[PLANNING_SEATS]["reform"]
    base = runs[PLANNING_SEATS]
    def floor_enact(res, p, b, cal=True):
        x = res["floor"][p][b]["enact"]
        return x if (not cal or fits[p].get(b, True)) else 0.0
    def expected(res, p):
        return sum(floor_enact(res, p, b) for b in res["floor"][p])
    json.dump(dict(runs={str(k): v for k, v in runs.items()}, holdouts={str(k): v for k, v in hold.items()},
                   calendar=fits, params=dict(N=N, seed=SEED, house_d=HOUSE_D, holdouts=HOLDOUTS)), open("votes.json", "w"), indent=1)

    pc = lambda x: f"{round(100 * x)}%"
    nfloor = len(base["floor"]["F"])
    o = []; A = o.append
    A("# Vote simulation: the odds the agenda passes the 2029-30 Congress\n")
    A(f"*Generated by index/tools/votes-model.py from the ledger and index/data/inputs/votes-bills.csv and votes-senate.csv ({N:,} simulated Congresses per scenario, fixed seed). Do not edit by hand. Every vote parameter is the war-game simulator's or an estimate (each row's basis is in votes-bills.csv); the Senate roster is the war game's mid-2026 map and is re-baselined after the Nov 3 election. Read the results as relative odds for comparing paths and packages, not forecasts.*\n")
    r53 = base["packages"]
    lack = sorted(((v, k, 1 - x / max(r53[v]["senate"], 1e-9)) for v in r53 for k, x in r53[v]["survive"].items()), key=lambda t: -t[2])[:3]
    dropped = ", ".join(f"{k} ({labels[k]}; missing from {pc(m)} of passing versions)" for v, k, m in lack)
    A(f"**Bottom line ({PLANNING_SEATS} seats, the middle of D1's 52-54; {HOUSE_D} House seats).** Under graduated cloture (F, decided) the rules change is adopted in {pc(base['reform']['F'])} of simulated Congresses. "
      f"Some version of each reconciliation bill passes the Senate in {pc(r53['R1']['senate'])} (R1), {pc(r53['R2']['senate'])} (R2) and {pc(r53['R3']['senate'])} (R3) of them, but as written only {pc(r53['R1']['intact'])}, {pc(r53['R2']['intact'])} and {pc(r53['R3']['intact'])}: the rest pass after provisions are dropped. The provisions most often dropped are {dropped}. "
      f"Of {nfloor} regular-order bills, about {expected(base, 'F'):.1f} are enacted on average under F once the calendar is counted, against {expected(base, 'G'):.1f} under the carve-out fallback (G) and {expected(base, 'none'):.1f} with no rules change.\n")
    A("## By rules path\n")
    A("**CAP-7S routing assumption (Oct 21):** the full multi-year surge targets R1, immediately available on enactment. Vote results assume reconciliation eligibility, not a Byrd/jurisdiction certification, including SSA scope. FY2029 cash costing is separate.\n")
    A(f"{PLANNING_SEATS} seats. Packages need a simple majority whatever the path; the path decides cloture for regular-order bills and the appropriations omnibus.\n")
    A("| Path | Rules change adopted | Regular-order bills enacted (of %d), with the calendar | Without the calendar limit | Appropriations omnibus enacted |\n| --- | --- | --- | --- | --- |" % nfloor)
    for p in PATHS:
        A(f"| {PATH_NAMES[p]} | {pc(base['reform'][p]) if PATHS[p][0] else '—'} | {expected(base, p):.1f} | {sum(floor_enact(base, p, b, False) for b in base['floor'][p]):.1f} | {pc(base['omnibus'][p]['enact'])} |")
    A("\n## Reconciliation packages\n")
    A("A package needs 50 senators plus the Vice President and gets no Republican votes. As written: no provision draws an objection that costs the majority. Some version: leadership drops the provisions holdouts object to until a majority holds (see the provisions table below for what survives).\n")
    A("| Package | Provisions | Passes the Senate as written | Some version passes the Senate | House | Some version enacted |\n| --- | --- | --- | --- | --- | --- |")
    for v, d in r53.items():
        A(f"| {v} | {len(d['members'])} | {pc(d['intact'])} | {pc(d['senate'])} | {pc(d['house'])} | {pc(d['enact'])} |")
    A("\n## Must-pass items (D1)\n")
    A("| Item | Vehicle | F (decided) | C | G (fallback) | No rules change | Gets floor time under F |\n| --- | --- | --- | --- | --- | --- | --- |")
    veh = {b["id"]: b["vehicle"] for b in bills}
    for b in MUST_PASS:
        if veh[b] == "FLOOR":
            A(f"| {b}: {labels[b]} | Regular order | {pc(floor_enact(base, 'F', b))} | {pc(floor_enact(base, 'C', b))} | {pc(floor_enact(base, 'G', b))} | {pc(floor_enact(base, 'none', b))} | {'Yes' if fits['F'].get(b, True) else 'No'} |")
        else:
            d = r53[veh[b]]; x = pc(d["survive"][b] * d["house"]); A(f"| {b}: {labels[b]} | {veh[b]} (survives the trim) | {x} | {x} | {x} | {x} | Reconciliation |")
    A("\n## Seats\n")
    A("Under F. Each added seat comes from the roster's next race (Iowa for 52, Texas for 53, Alaska for 54); a different seat with a different senator changes the result.\n")
    A("| Senate seats | Rules change (F) | R1 as written | R2 as written | R3 as written | R2, some version | Regular-order bills enacted (of %d) |\n| --- | --- | --- | --- | --- | --- | --- |" % nfloor)
    for seats, res in runs.items():
        pk = res["packages"]
        A(f"| {seats} | {pc(res['reform']['F'])} | {pc(pk['R1']['intact'])} | {pc(pk['R2']['intact'])} | {pc(pk['R3']['intact'])} | {pc(pk['R2']['senate'])} | {expected(res, 'F'):.1f} |")
    A("\n## Holdouts\n")
    A(f"Senators who vote against any rules change regardless (the planning case assumes {HOLDOUTS}), at {PLANNING_SEATS} seats.\n")
    A("| Holdouts | F adopted | C adopted | G adopted |\n| --- | --- | --- | --- |")
    for h in sorted(hold): A(f"| {h} | {pc(hold[h]['F'])} | {pc(hold[h]['C'])} | {pc(hold[h]['G'])} |")
    A("\n## Every regular-order bill\n")
    A(f"{PLANNING_SEATS} seats. Senate and House columns are for F; \"Floor time\" says whether the bill fits the 163-day calendar in capacity allocation with protected DEM/SS reservations (no: unresolved capacity, not approved deferral).\n")
    A("| Bill | Senate (F) | House | Enacted (F) | Floor time (F) | Enacted (G) | Basis |\n| --- | --- | --- | --- | --- | --- | --- |")
    basis = {b["id"]: b["basis"] for b in bills}
    for b, d in sorted(base["floor"]["F"].items(), key=lambda kv: -kv[1]["enact"]):
        A(f"| {b}: {labels[b]} | {pc(d['senate'])} | {pc(d['house'])} | {pc(floor_enact(base, 'F', b))} | {'Yes' if fits['F'].get(b, True) else 'No'} | {pc(floor_enact(base, 'G', b))} | {basis[b]} |")
    A("\n## Package provisions\n")
    A(f"{PLANNING_SEATS} seats: how often each provision is in the package the Senate passes (share of all simulated Congresses). A dropped revenue provision opens a hole that the rest of the package, or another vehicle, must fill (the Byrd rule tests each bill's out-years).\n")
    A("| Package | Provision | Survives into the passed package | Basis |\n| --- | --- | --- | --- |")
    for v, d in r53.items():
        for k, x in sorted(d["survive"].items(), key=lambda kv: kv[1]):
            A(f"| {v} | {k}: {labels[k]} | {pc(x)} | {basis[k]} |")
    A("\n## Limits\n\n- Objection rates are the war game's archetype rates where a bill maps to one, otherwise estimates; nothing here is polling or whip counts.\n- Objections are independent across senators and bills; real holdouts move together, so the packages' odds are probably too low at the extremes and too high in the middle.\n- Trimming ignores the Byrd rule: a package that drops revenue but keeps permanent spending would fail the out-year test, so a dropped revenue provision means replacement revenue or a smaller program, which the vehicle checker on the roadmap will test.\n- DEM-1 must begin floor consideration by March 2029; SS has a spring-2030 target. Capacity reservations protect them but do not validate these dated deadlines. Other priorities can move early/in parallel. Seasonal target labels do not select a passage month.\n- Byrd challenges, amendments, conference and timing inside the year are not modeled; the House model is the war game's frontliner drag (for a package, its most exposed provision).\n- The roster is the war game's mid-2026 map; re-baseline it in votes-senate.csv after Nov 3.\n")
    open("vote-simulation.md", "w").write("\n".join(o) + "\n")
    print(f"votes: F adopted {pc(base['reform']['F'])}; packages as written R1 {pc(r53['R1']['intact'])} R2 {pc(r53['R2']['intact'])} R3 {pc(r53['R3']['intact'])}, some version {pc(r53['R1']['enact'])} {pc(r53['R2']['enact'])} {pc(r53['R3']['enact'])}; regular order {expected(base, 'F'):.1f} of {nfloor}")

if __name__ == "__main__":
    main()
