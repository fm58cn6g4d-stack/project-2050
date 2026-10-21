"""Master ledger for Project 2050's 2029-30 trifecta agenda (full rebuild Oct 20, 2026; education batch the same day).

Every row is keyed by its domain-file ID; the legacy ledger ID (H1, E11, DEM1 ...) is kept
in its own column as a crosswalk. All dollar figures are ten-year totals for 2030-39 in
trillions. Positive cost = adds to deficit before financing; negative = savings.
basis: "sourced" (taken or scaled from a cited figure in a Project 2050 doc),
       "scaled" (outside source scaled to 2030-39), "estimate" (my estimate),
       "proposal" (an author's proposal sized against current programs, not a score).

Education batch (Oct 20, evening): FAM-4 moves to domains/domain-education.md and splits into
EDU-1 (K-12 formula funding, carrying EDU-2) and EDU-5 (higher education) at the same totals;
new rows EDU-3 (universal school meals), EDU-4 (educator pipeline), EDU-7 (voucher tax-credit
repeal, a saving) and EDU-8 (AI in education, student data and research, appropriations).
Climate durability options (CLI-9 to CLI-13) and Talarico-scenario options are not chosen and
add no rows; they appear in CONFLICTS and in the revenue menu where they carry a revenue figure.

Decisions later on Oct 20 (Espen): REV-C1 takes the durability session's price path ($25 rising to
~$100 by 2037, road fuels still exempt), so C1 is $1.35T and CLI-2's dividend $1.08T; D4 lets
borrowing finance time-limited climate capital (new alternative cut C37, exclusive with C29);
REV-E1/C35 restated as the increment beyond G9 (~$0.15T); DEM-1F adopted (DEM-1 after R1).
Cuts listed in ALT_CUTS are alternatives to another cut and are not summed.
"""
import csv, json
from inputs import read, num, flag

BUDGET_DAYS = 163  # 148 discretionary days (unified inventory) + 15 freed by Block 1's nomination caps (C28, hedged; estimate)
RECON_DAYS = 15    # floor days per reconciliation bill (frameworks/radical-means-moderate-ends.md)
RESOLUTION_DAYS = 2  # budget resolution vote-a-rama per vehicle (estimate)

RAILS = {
    "R1": "Reconciliation I (FY2029 resolution, spring 2029)",
    "R2": "Reconciliation II (FY2030 resolution, fall 2029)",
    "R3": "Reconciliation III (FY2031 resolution, summer 2030)",
    "FLOOR": "Regular order (needs majority cloture)",
    "APPROPS": "Annual appropriations",
    "LATER": "After the 2029-30 window",
    "T2": "Second trifecta (2033-36)",
}

def _moving_america():
    """Draft 2's figures from the transportation model (index/tools/transportation/), at the precision Draft 2 prints:
    package and top-up amounts to $0.01B, reconciliation scores to $0.1B. run-all.sh writes moving-america.json first."""
    try:
        f = json.load(open("moving-america.json"))["ledger"]
    except FileNotFoundError:
        import os, sys
        sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "transportation"))
        import report
        f = report.figures()["ledger"]
    r2 = {k: round(f[k], 2) for k in ("act29_package", "act29_topups", "act30_package", "act30_topups", "expansion_authority")}
    r1 = {k: round(f[k], 1) for k in ("act29_gross", "act29_net", "act30_gross", "act30_net", "score_fuel_steps",
                                      "score_truck_excise_ev_fee", "score_weight_distance", "score_rail_aviation")}
    r1["score_clean_vehicle"] = round(f["score_clean_vehicle"] - 12.9, 1) + 12.9   # clean-car line printed to $0.1B
    r1["score_offset"] = (r1["act29_net"] + r1["act30_net"]) - (r1["act29_gross"] + r1["act30_gross"])
    return {**r2, **r1}
MA = _moving_america()
MOV29 = round((MA["act29_package"] + MA["act29_topups"]) / 1000, 5)
MOV30 = round((MA["act30_package"] + MA["act30_topups"]) / 1000, 5)
DIV_E = 1.0   # $B, division E's general-fund items, FY2032-36 (Draft 2; estimate)
MOV31 = round((MA["expansion_authority"] + DIV_E) / 1000, 5)
MR = {k: round(MA[k] / 1000, 4) for k in ("score_fuel_steps", "score_clean_vehicle", "score_truck_excise_ev_fee",
                                          "score_weight_distance", "score_rail_aviation", "score_offset")}

MODEL = dict(MOV29=MOV29, MOV30=MOV30, MOV31=MOV31, MOV31_HI=round(MOV31 + 0.05, 5),
             MOV29_OWN=round(MA["act29_net"] / 1000, 3), MOV30_OWN=round(MA["act30_net"] / 1000, 3),
             MR1=MR["score_fuel_steps"], MR2=MR["score_clean_vehicle"], MR3=MR["score_truck_excise_ev_fee"],
             MR4=MR["score_weight_distance"], MR5=MR["score_rail_aviation"], MR6=MR["score_offset"])

def amount(s):
    """A number, or model:NAME for a figure the transportation model supplies."""
    return MODEL[s[6:]] if s.startswith("model:") else num(s)

# The tables are in index/data/inputs/ (ledger-*.csv); see the readme there for each column.
# Bills: one row per ledger bill. Notes on model rows take the model's figures ({act29_package:.1f} and so on).
B = []
for r in read("ledger-bills.csv"):
    model_row = r["cost_mid"].startswith("model:")
    B.append((r["id"], r["legacy_id"], r["bill"], r["domain"], r["source"], r["rail"], r["channel"],
              amount(r["cost_lo"]), amount(r["cost_mid"]), amount(r["cost_hi"]), amount(r["own_revenue_mid"]), r["basis"],
              r["note"].format(**MA, DIV_E=DIV_E) if model_row else r["note"],
              r["floor_days"], num(r["felt_months"]), num(r["durability"]), r["target"]))
# Revenue options: id, option, channel, lo, mid, hi, in_base, legal risk, overlap note, source, reaches_middle
REV = [(r["id"], r["option"], r["channel"], amount(r["lo"]), amount(r["mid"]), amount(r["hi"]), flag(r["in_base"]),
        r["legal_risk"], r["overlap"], r["source"], flag(r["reaches_middle"])) for r in read("ledger-revenue.csv")]
CONFLICTS = [(r["topic"], r["one_doc"], r["other_doc"], r["resolution"]) for r in read("ledger-conflicts.csv")]
# Cuts and options: id, change, dollars saved mid ($T), floor days saved, kind, rationale
CUTS = [(r["id"], r["change"], num(r["saves_tn"]), num(r["saves_days"]), r["kind"], r["why"]) for r in read("ledger-cuts.csv")]

# Dynamic sensitivity (added Oct 20, later). NOT in any total: the ledger and D4 stay on
# conventional scoring. Each row is a macroeconomic feedback on the general fund over 2030-39 in $T,
# positive = improves the budget, under CBO/JCT-style conventions (low, mid, high), plus an
# "optimistic" mid under Talarico-model-style assumptions. All are Claude's estimates.
DYNAMIC = [(r["id"], r["effect"], r["rows"], num(r["lo"]), num(r["mid"]), num(r["hi"]), num(r["optimistic_mid"]), r["basis"])
           for r in read("ledger-dynamic.csv")]

# How each bill's cost reaches the general fund (accounting rule, Oct 19):
#  all = every outlay is general-fund; residual = the channel pays first, the general fund backstops (floored at zero); none = inside a channel
GF_RULE = {"FAM-3":"none","CLI-5":"residual","SAF-10":"residual","DEM-1":"all","COM-1":"residual",
           "MOV-29":"all","MOV-30":"all","SS-1":"none","CLI-2":"none"}
_rv = {r[0]: r[3:6] for r in REV}
_c5 = tuple(round(0.2 * c1 + c2 + c3, 3) for c1, c2, c3 in zip(_rv["C1"], _rv["C2"], _rv["C3"]))  # CLI-5: REV-C1's 20%, REV-C2 and REV-C3
OWN_RANGE = {"FAM-3":(0.85,0.9,1.28),"CLI-5":_c5,"SAF-10":(0.08,0.09,0.10),"SS-1":(2.8,3.0,3.3),
             "CLI-2":tuple(_rv["C1"]),"MOV-29":(round(MA["act29_net"] / 1000, 3),) * 3,"MOV-30":(round(MA["act30_net"] / 1000, 3),) * 3,"COM-1":(0.004,0.004,0.004)}
ALT_OF = {"C29":"C37","C19":"C19b"}  # alternatives to an accepted cut; listed, never summed
ALT_CUTS = set(ALT_OF)
DECLINED = {"C5","C17","C33","C34","C36"}  # declined in Decision Brief 2 (Oct 20); kept as the record, never summed
OWN_CHANNEL = {"MOV-29":"Surface transportation trust fund","MOV-30":"Surface transportation trust fund"}

def channels(bills):
    """Gross revenue and gross outlay per channel, never netted against the general fund."""
    rv = {}
    for r in REV:
        if r[6] or r[2]=="General fund": continue
        rv.setdefault(r[2],[0,0,0]); rv[r[2]] = [a+b for a,b in zip(rv[r[2]],(r[3],r[4],r[5]))]
    rows = []
    def add(ch, rev, out, note):
        rows.append(dict(channel=ch, rev_lo=round(rev[0],3), rev_mid=round(rev[1],3), rev_hi=round(rev[2],3),
                         out_lo=round(out[0],3), out_mid=round(out[1],3), out_hi=round(out[2],3), note=note))
    by = {b["id"]:b for b in bills}
    o = lambda i: (by[i]["cost_lo"],by[i]["cost_mid"],by[i]["cost_hi"])
    add("Social Security (OASDI)", rv["Social Security trust fund"], o("SS-1"), "D8 baseline; closes ~64% of the 4.42% gap after the haircut (index/dedicated-funds.md); revenue stays in the trust fund")
    add("Medicare HI", (0.5+0.5,0.5+0.7,0.5+0.9), (0.8,0.85,0.9), "H1a ($0.5T) plus HLT-6's Part A share (~$0.7T, est.); D4 read on a 75-year window, so the ~$0.3T is HI's reserve")
    add("Paid-leave fund", rv["Paid-leave fund"], o("FAM-3"), "Step-up toward 0.85% and a repayable Treasury loan; no general-fund backstop")
    st = rv["Surface transportation trust fund"]
    add("Surface transportation trust fund", st, st, "Receipts net of the 25% offset; spent within receipts; general-fund top-ups counted in MOV-29 and MOV-30")
    add("Carbon fee (REV-C1)", rv["Carbon fee"], rv["Carbon fee"], f"80% dividend (CLI-2, ~${0.8 * rv['Carbon fee'][1]:.2f}T) plus 20% transition share to CLI-5 (~${0.2 * rv['Carbon fee'][1]:.2f}T)")
    add("Carbon border adjustment and methane fee (REV-C2, REV-C3)", rv["Carbon border adjustment"], o("CLI-5"), "Outlay is CLI-5's gross add-ons, financed by REV-C2, REV-C3 and REV-C1's transition share; residual to the general fund")
    add("Public safety", rv["Public safety"], o("SAF-10"), "Durable sources only (alcohol, fraud assessment, firearms, fees); residual (~$2.9B a year) to the general fund")
    add("Merger review", rv["Merger review"], (0.004,0.004,0.004), "HSR fee increase funds an equal enforcement increase (COM-2)")
    add("Immigration fees", rv["Immigration fees"], rv["Immigration fees"], "Statutory H-1B fee spent on adjudication and training (IMM-2)")
    return rows

def felt_by_mid(x):
    return x <= 22  # Nov 2030 = month 22 (Jan 2029 = 0)

def main():
    bills = []
    for r in B:
        (i,legacy,name,dom,src,rail,chan,lo,mid,hi,own,basis,note,days,felt,dur,tgt) = r
        y,m = map(int,tgt.split("-"))
        fm = (y-2029)*12 + (m-1) + felt
        bills.append(dict(id=i,legacy=legacy,bill=name,domain=dom,source=src,rail=rail,rail_name=RAILS[rail],channel=chan,
            cost_lo=lo,cost_mid=mid,cost_hi=hi,own_revenue=own,net_mid=round(mid-own,3),
            basis=basis,basis_note=note,floor_days=int(days),felt_months=felt,durability=dur,target=tgt,
            felt_by_midterm="Yes" if felt_by_mid(fm) else "No"))
    in_window = [b for b in bills if b["rail"] not in ("LATER","T2")]
    for b in bills:
        rule = GF_RULE.get(b["id"], "all" if b["channel"].startswith("General fund") or b["channel"]=="None" else "none")
        rlo,rmid,rhi = OWN_RANGE.get(b["id"], (b["own_revenue"],)*3)
        b["own_rev_lo"],b["own_rev_mid"],b["own_rev_hi"] = rlo,rmid,rhi
        b["own_rev_channel"] = OWN_CHANNEL.get(b["id"], b["channel"] if rule!="all" else "")
        b["gf_rule"] = rule
        if rule=="all": g = (b["cost_lo"],b["cost_mid"],b["cost_hi"])
        elif rule=="residual": g = (max(0,b["cost_lo"]-rhi), max(0,b["cost_mid"]-rmid), max(0,b["cost_hi"]-rlo))
        else: g = (0,0,0)
        b["gf_lo"],b["gf_mid"],b["gf_hi"] = [round(x,3) for x in g]
        b["net_mid"] = b["gf_mid"] if rule!="none" else round(b["cost_mid"]-b["own_revenue"],3)
    with open("bills.csv","w",newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(bills[0].keys())); w.writeheader(); w.writerows(bills)
    gf = [b for b in in_window if b["gf_rule"]!="none"]
    claims = {k: round(sum(b["gf_"+k] for b in gf),2) for k in ("lo","mid","hi")}
    gross_out = round(sum(b["gf_mid"] for b in gf if b["gf_mid"]>0),2)
    gross_sav = round(sum(b["gf_mid"] for b in gf if b["gf_mid"]<0),2)
    base = [r for r in REV if r[6] and r[2]=="General fund"]
    rev = {k: round(sum(r[j] for r in base),2) for k,j in (("lo",3),("mid",4),("hi",5))}
    floor_days = sum(b["floor_days"] for b in in_window)
    recon_vehicles = sorted({b["rail"] for b in in_window if b["rail"].startswith("R")})
    recon_days = len(recon_vehicles)*(RECON_DAYS+RESOLUTION_DAYS)
    total_days = floor_days + recon_days
    by_rail = {}
    for b in in_window:
        d = by_rail.setdefault(b["rail"], dict(rail=b["rail"], rail_name=b["rail_name"], bills=0, net_mid=0.0, floor_days=0))
        d["bills"] += 1
        if b in gf: d["net_mid"] = round(d["net_mid"] + b["net_mid"],3)
        d["floor_days"] += b["floor_days"]
    for r in recon_vehicles: by_rail[r]["floor_days"] += RECON_DAYS+RESOLUTION_DAYS
    by_domain = {}
    for b in in_window:
        d = by_domain.setdefault(b["domain"], dict(domain=b["domain"], rows=0, gf_lo=0.0, gf_mid=0.0, gf_hi=0.0, floor_days=0))
        d["rows"] += 1; d["floor_days"] += b["floor_days"]
        for k in ("lo","mid","hi"): d["gf_"+k] = round(d["gf_"+k] + b["gf_"+k],3)
    accepted = [c for c in CUTS if "accepted" in c[4]]
    summed = [c for c in CUTS if c[0] not in ALT_CUTS | DECLINED]
    cut_dollars = round(sum(c[2] for c in summed),2)
    summary = dict(
        gf_claims=claims, base_revenue=rev, gap_mid=round(claims["mid"]-rev["mid"],2),
        gap_lo=round(claims["lo"]-rev["hi"],2), gap_hi=round(claims["hi"]-rev["lo"],2),
        floor_days_needed=total_days, floor_budget=BUDGET_DAYS, floor_over=total_days-BUDGET_DAYS,
        regular_floor_days=floor_days, recon_days=recon_days, recon_vehicles=recon_vehicles,
        by_rail=list(by_rail.values()), by_domain=sorted(by_domain.values(), key=lambda d:-d["gf_mid"]),
        cut_dollars=cut_dollars, cut_days=sum(c[3] for c in summed),
        accepted_dollars=round(sum(c[2] for c in accepted),2),
        gap_after_accepted=round(claims["mid"]-rev["mid"]-sum(c[2] for c in accepted),2),
        gap_after_cuts=round(claims["mid"]-rev["mid"]-cut_dollars,2),
        days_after_cuts=total_days-sum(c[3] for c in summed),
        borrow_dollars=round(sum(c[2] for c in accepted if c[4].startswith("Borrow")),2),
        revenue_accepted=round(sum(c[2] for c in accepted if c[4].startswith("Revenue")),2),
        felt_by_midterm=sum(1 for b in in_window if b["felt_by_midterm"]=="Yes"), bills_in_window=len(in_window),
        gf_gross_outlays=gross_out, gf_gross_savings=gross_sav, channels=channels(bills),
        dynamic_lo=round(sum(r[3] for r in DYNAMIC),2), dynamic_mid=round(sum(r[4] for r in DYNAMIC),2),
        dynamic_hi=round(sum(r[5] for r in DYNAMIC),2), dynamic_optimistic=round(sum(r[6] for r in DYNAMIC),2),
    )
    json.dump(dict(summary=summary, bills=bills,
                   revenue=[dict(id=r[0],option=r[1],channel=r[2],lo=r[3],mid=r[4],hi=r[5],in_base="Yes" if r[6] else "No",reaches_middle="Yes" if r[10] else "No",legal_risk=r[7],overlap=r[8],source=r[9]) for r in REV],
                   conflicts=[dict(topic=c[0],one_doc=c[1],other_doc=c[2],resolution=c[3]) for c in CONFLICTS],
                   cuts=[dict(id=c[0],change=c[1],saves_tn=c[2],saves_days=c[3],kind=c[4],why=c[5],
                             alternative_to=ALT_OF.get(c[0]) or ("Declined (Decision Brief 2)" if c[0] in DECLINED else "")) for c in CUTS],
                   dynamic=[dict(id=r[0],effect=r[1],rows=r[2],lo=r[3],mid=r[4],hi=r[5],optimistic=r[6],basis=r[7]) for r in DYNAMIC]),
              open("ledger.json","w"), indent=1)
    print(json.dumps({k:v for k,v in summary.items() if k not in ("channels","by_rail","by_domain")}, indent=1))
    for d in summary["by_domain"]: print(d)
    for d in summary["by_rail"]: print(d)

if __name__ == "__main__":
    main()
