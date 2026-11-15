"""Health cost review: an independent rebuild of the single health plan's cost, service by service and payer by payer,
and the financing packages that follow from it.

Role: the analysis behind `dossiers/foundations/health-cost-review.md` (stage E). It tries to break the gross cost in
`dossiers/foundations/health-financing.md` (FY2040: $8,407B) by rebuilding the 2032 full-scale cost from CMS's 2024
spending table by service and payer (NHE Table 19, SRC in `library/text/cms-2024-nhe-table19-expenditure-by-program.txt`)
and switching the model's simplifications off one at a time, then prices financing packages against Espen's take-home
test. Status: exploratory analysis, November 15, 2026. It books nothing and changes no adopted input; every figure is
project arithmetic on the project's own models, not an official score.

Part 1, the cost bridge (`bridge()`): starting from the memo's corrected model (Medicare rebased to CBO), each step
changes one thing and reports its 2032 effect and its FY2040 effect (x g40, the memo's 2032-to-FY2040 scale):
  1. physicians and other non-hospital services at Medicare's fee schedule plus add-ons (1.05), as decided;
  2. the newly covered priced off people under 65, not an all-ages average that includes Medicare's enrollees;
  3. each payer's own mix of services (Table 19) instead of one national hospital share and drug share;
  4. price indexes averaged by volume (spending over price), not by spending;
  5. each payer's own administrative share (Table 19);
  6. out-of-pocket spending: nursing homes and over-the-counter products stay outside the plan (it covers neither),
     Medicare enrollees' cost sharing priced at Medicare's prices, dental at the plan's dental fees;
  7. Medicaid's hospital payments at their measured level against Medicare (with supplemental payments);
  8. Medicaid and CHIP rebased to CBO's February 2026 baseline (the Medicaid seam), with the states' share that follows.

Run: `python3 models/tools/health_cost_review.py` (tables) or `--json`.
"""
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
sys.path.insert(0, HERE)

import health_financing as HF  # noqa: E402

TABLE19 = os.path.join(ROOT, "library", "text", "cms-2024-nhe-table19-expenditure-by-program.txt")
COLS = ["total", "hospital", "physician", "other_prof", "dental", "ohrpc", "home_health", "nursing", "rx", "dme",
        "nondurable", "state_admin", "fed_admin", "net_cost"]
ROWS = {9: "oop", 11: "phi", 12: "medicare", 13: "medicaid", 16: "chip"}
CARE = ["hospital", "physician", "other_prof", "dental", "ohrpc", "home_health", "nursing", "rx", "dme", "nondurable"]
ADMIN = ["state_admin", "fed_admin", "net_cost"]

# ---- working assumptions and evidence (each stated in the memo) ---------------------------------------------------
# The decided plan prices, as multiples of Medicare (HLT-7.10, HLT-7.12, memo 5 B): hospitals 1.15 after the glide;
# physicians and other clinicians on Medicare's fee schedules with primary-care and rural add-ons on about half of
# spending, 1.05; the same for the other services Medicare prices on fee schedules.
PLAN_HOSPITAL = 1.15
PLAN_FEE = 1.05
# Dental: Medicare has no dental fee schedule. The plan pays dentists on its own schedule, set here at 90% of private
# dental prices (a working assumption, range 75-100%; Medicaid's dental fees are about half of private ones).
PLAN_DENTAL_OF_PRIVATE = 0.90
# Medicaid's hospital payments against Medicare's, with supplemental, directed and DSH payments: AHA's payment-to-cost
# ratios with supplemental payments, Medicaid 88 cents and Medicare 82-84 cents per dollar of cost (about 1.05);
# MACPAC: fee-for-service base rates 78% of Medicare (2011), with supplemental payments 20% and directed payments
# another 20% of Medicaid hospital payments (FY2022). Central 1.00, range 0.90-1.07 (not yet in the register). The
# model uses its physician fee index (0.72; Zuckerman and others, 2021) for all Medicaid claims.
MEDICAID_HOSPITAL_IDX = 1.00
# Private prices against Medicare by service: hospitals 2.54 (RAND round 5, EV-CAR-131); physicians 1.4 (the
# model's assumption); other professional, home health and equipment at 1.2 and nursing facilities at 1.1 (working
# assumptions; commercial premiums over Medicare are smaller outside hospitals and specialists).
PHI_IDX = {"hospital": 2.54, "physician": 1.4, "other_prof": 1.2, "home_health": 1.2, "nursing": 1.1, "dme": 1.2,
           "ohrpc": 1.2}
# The uninsured's ages: about 14% children (ACS: about 16% of the uninsured were children in 2023; adults' share
# rises under the 2025 law's adult coverage cuts). Working assumption, range 10-18%.
UNINS_CHILD_SHARE = 0.14
# CBO's February 2026 baseline (SRC-3395, EV-CAR-718's workbook): Medicaid's federal outlays, FY2032 ($B), and
# CHIP's federal subsidies (SRC-3000, Table A-1). The federal share of Medicaid spending is Table 19's for 2024
# (596.7 of 931.7), held for 2032 (range 0.62-0.67; CBO: "about two-thirds").
CBO_MEDICAID_FED_2032 = 833.971
CBO_CHIP_FED_2032 = 15.0
CHIP_FED_SHARE = 22.118 / 30.995


def table19():
    """CMS NHE Table 19, 2024, $ billion: {payer: {column: value}} for out of pocket, private insurance, Medicare,
    Medicaid and CHIP."""
    cells = {}
    for line in open(TABLE19, encoding="utf-8"):
        m = re.match(r"row (\d+) \| (.*?) = ?(.*)$", line.rstrip("\n"))
        if m and int(m.group(1)) in ROWS:
            cells.setdefault(int(m.group(1)), []).append(m.group(3).strip())
    out = {}
    for r, name in ROWS.items():
        vals = cells[r][1:1 + len(COLS)]
        out[name] = {c: (float(v) / 1000 if v not in ("—", "") else 0.0) for c, v in zip(COLS, vals)}
    return out


def _ctx():
    c = HF.coverage(True)
    HP, I, B, P = c["HP"], c["I"], c["B"], c["P"]
    return c, HP, I, B, P


def model_pieces(HP, I, B, P):
    """The model's own 2032 inputs to groups(): spending moving by group, out of pocket by group, and the rest."""
    S, adm = B["S"], B["adm"]
    ltc, ltc_fed = HP.mcd_ltc_kept(I, P)
    g = B["gross"]
    ng = g["ng_sub"] + g["ng_unsub"]
    esi_sh = g["esi"] / (g["esi"] + ng)
    oop_in = S["oop"] - B["oop_pp"]["unins"] * sum(B["cells0"]["uninsured"]) / 1000 \
        - B["oop_pp"]["other"] * sum(B["cells0"]["other"]) / 1000
    cnt = {"esi": g["esi"], "medicare": g["medicare"], "medicaid": g["medicaid"], "ng": ng}
    oopg = {k: B["oop_pp"][k] * n / 1000 for k, n in cnt.items()}
    k = oop_in / sum(oopg.values())
    oopg = {key: v * k for key, v in oopg.items()}
    unins0 = sum(B["cells0"]["uninsured"])
    new_n = max(0.0, unins0 - I["sp_residual_unins"] * B["pop"])
    covered_now = B["pop"] - sum(B["cells0"]["other"]) - unins0
    return dict(S=S, adm=adm, ltc=ltc, ltc_fed=ltc_fed, esi_sh=esi_sh, oopg=oopg, oop_in=oop_in, new_n=new_n,
                covered_now=covered_now, people=dict(esi=g["esi"], ng=ng, medicaid=g["medicaid"],
                                                     medicare=g["medicare"]))


DEFAULT = dict(physician=1.15, newly="all_ages", mix="national", average="spending", admin="model", oop="model",
               medicaid_hosp="fee_index", chip="out", medicaid_level="cms")


def rebuild(opts=None, hosp_rate=PLAN_HOSPITAL, I_over=None):
    """The 2032 full-scale cost of the single plan by group ($ billion), with the model's simplifications switched by
    `opts` (DEFAULT reproduces health_path.groups() exactly). Returns dict with cost, today, net, replaced, states,
    the household relief, the spending left outside the plan and diagnostics."""
    o = dict(DEFAULT, **(opts or {}))
    c, HP, I, B, P = _ctx()
    m = model_pieces(HP, I, B, P)
    I = dict(I, **(I_over or {}))
    T = table19()
    S = dict(m["S"])
    nhe24 = {"medicare": I["nhe_medicare"], "medicaid": I["nhe_medicaid"], "phi": I["nhe_phi"], "oop": I["nhe_oop"]}
    grow = {p: S[p] / nhe24[p] for p in nhe24}          # 2024 to 2032, as the model (Medicare rebased to CBO)
    a, cs, d = I["sp_admin"], I["sp_cs_low_rate"], I["sp_drug_cut"]
    u = I["sp_util_uplift"] * 0.5 * (1 - I["sp_unmet_share"])
    gross_up = (1 + u) * (1 / (1 - a) - cs)
    rx_nat = I["nhe_rx"] / I["nhe_total_2024"]
    wh = I["nhe_hospital"] / (I["nhe_hospital"] + I["nhe_physician"])
    c_idx = dict(B["c"])

    # Medicaid: spending that moves (outside long-term care), its federal part, and the states' part
    mcd_total, sub_mcd, chip_cost = S["medicaid"], I["sub_medicaid"], 0.0
    ltc, ltc_fed = m["ltc"], m["ltc_fed"]
    # CHIP: CBO counts its children in Medicaid and CHIP (EV-CAR-051) and its federal money in the subsidy the model
    # replaces (sub_medicaid), but CMS's Medicaid line leaves CHIP's spending out (Table 19 lists it separately), so
    # the model replaces CHIP's federal money without paying for CHIP's care. Grown at Medicaid's rate.
    grow["chip"] = grow["medicaid"]
    if o["medicaid_level"] == "cbo":
        fed_share = 596.694 / 931.692
        mcd_total = CBO_MEDICAID_FED_2032 / fed_share
        ltc = ltc * mcd_total / S["medicaid"]
        ltc_fed = ltc * I["nhe_mcd_ltc_fed_share"]
        sub_mcd = CBO_MEDICAID_FED_2032 + CBO_CHIP_FED_2032     # every federal Medicaid and CHIP dollar replaced
        grow["medicaid"] = mcd_total / nhe24["medicaid"]
        grow["chip"] = CBO_CHIP_FED_2032 / CHIP_FED_SHARE / T["chip"]["total"]
    mcd_moving = mcd_total - ltc

    def spend(payer):
        """2032 spending by column for a payer (Table 19's 2024 mix grown at the payer's rate)."""
        g_ = grow[payer]
        return {k: v * g_ for k, v in T[payer].items()}

    # ---- the ratio of the plan's price to the payer's price, by service
    blend = {"medicare": c_idx["medicare"], "medicaid": c_idx["medicaid"], "chip": c_idx["medicaid"],
             "phi": c_idx["phi"], "oop": c_idx["phi"], "oop_private": c_idx["phi"], "oop_medicare": c_idx["phi"],
             "oop_medicaid": c_idx["phi"]}
    # dental: the plan's schedule at PLAN_DENTAL_OF_PRIVATE of private prices; Medicaid's dental fees about half of
    # private ones (working assumption)
    dental_vs_private = {"medicaid": 0.5, "chip": 0.5, "oop_medicaid": 0.5}

    def plan_rate(svc):
        return hosp_rate if svc == "hospital" else o["physician"]

    def ratio(svc, payer):
        if o["average"] == "spending":
            return plan_rate(svc) / blend[payer]
        if o["average"] == "volume_hp" and svc not in ("hospital", "physician") \
                and payer in ("phi", "oop_private", "oop"):
            # step 4a: only the hospital and physician ratios divided service by service; every other private
            # service, dental included, stays at the model's blended index
            return plan_rate(svc) / blend[payer]
        if svc == "dental":
            return PLAN_DENTAL_OF_PRIVATE / dental_vs_private.get(payer, 1.0)
        if payer == "medicare":
            p_ = c_idx["medicare"]
        elif payer in ("medicaid", "chip", "oop_medicaid"):
            p_ = MEDICAID_HOSPITAL_IDX if (svc == "hospital" and o["medicaid_hosp"] == "measured") \
                else I["medicaid_fee_idx"]
        elif payer == "oop_medicare":
            p_ = c_idx["medicare"]
        else:                                   # private insurance and the privately insured's own payments
            p_ = PHI_IDX.get(svc, I["phys_commercial_ratio"])
        return plan_rate(svc) / p_

    def reprice(amount_by_svc, payer, admin_share):
        """Claims (spending less administration) repriced to the plan, before use and the plan's administration."""
        claims = sum(amount_by_svc.values()) * (1 - admin_share)
        if "all" in amount_by_svc:              # the model's split: one national hospital share and drug share
            nd = claims * (1 - rx_nat)
            return nd * (wh * ratio("hospital", payer) + (1 - wh) * ratio("physician", payer)) \
                + claims * rx_nat * (1 - d)
        care = {s_: amount_by_svc.get(s_, 0.0) for s_ in CARE}
        k = claims / sum(care.values())         # the claims spread over the payer's own mix of services
        return sum(v * k * ((1 - d) if s_ == "rx" else ratio(s_, payer)) for s_, v in care.items())

    adm = dict(m["adm"])
    if o["admin"] == "table":
        for p in ("medicare", "medicaid", "phi", "chip"):
            row = T[p]
            adm[p] = sum(row[x] for x in ADMIN) / row["total"]

    # ---- spending by group, by service (2032)
    sm = spend("medicare")
    smd = spend("medicaid")
    if o["mix"] == "national":
        mcd_svc = {"all": mcd_moving}
        med_svc = {"all": S["medicare"]}
        phi_svc = {"all": S["phi"]}
    else:
        # Medicaid's long-term care settings come out of nursing, home health and the other personal care line,
        # in that order, up to the model's long-term care amount (Table 19's three lines are an upper bound, EV-CAR-460)
        mcd_svc = dict(smd)
        left = ltc * (mcd_total / mcd_total)
        for s in ("nursing", "home_health", "ohrpc"):
            take = min(mcd_svc[s], left)
            mcd_svc[s] -= take
            left -= take
        mcd_svc.pop("total")
        med_svc = {k: v for k, v in sm.items() if k != "total"}
        phi_svc = {k: v for k, v in spend("phi").items() if k != "total"}
    oopg = m["oopg"]
    oop_mix = {k: v for k, v in spend("oop").items() if k in CARE}
    oop_tot = sum(oop_mix.values())
    outside = {}      # out-of-pocket spending that stays outside the plan (households keep paying it)

    def oop_group(amount, payer):
        if o["oop"] == "model":
            return {"all": amount}, 0.0
        mix = {s: amount * v / oop_tot for s, v in oop_mix.items()}
        kept = mix.pop("nursing") + mix.pop("nondurable")
        return mix, kept

    groups = {}
    for name, svc, payer, oop_amt, oop_payer, ad in [
            ("medicare", med_svc, "medicare", oopg["medicare"], "oop_medicare", adm["medicare"]),
            ("medicaid", mcd_svc, "medicaid", oopg["medicaid"], "oop_medicaid", adm["medicaid"]),
            ("employer", {k: v * m["esi_sh"] for k, v in phi_svc.items()}, "phi", oopg["esi"], "oop_private",
             adm["phi"]),
            ("individual", {k: v * (1 - m["esi_sh"]) for k, v in phi_svc.items()}, "phi", oopg["ng"], "oop_private",
             adm["phi"])]:
        osvc, kept = oop_group(oop_amt, oop_payer)
        outside[name] = kept
        cost = (reprice(svc, payer, ad) + reprice(osvc, "oop" if "all" in osvc else oop_payer, 0.0)) * gross_up
        groups[name] = dict(cost=cost, today=sum(svc.values()) + oop_amt, oop=oop_amt, oop_outside=kept)
    chip_today = 0.0
    if o["chip"] == "in":
        chip_svc = {k: v for k, v in spend("chip").items() if k != "total"} if o["mix"] != "national" \
            else {"all": T["chip"]["total"] * grow["chip"]}
        chip_cost = reprice(chip_svc, "chip", adm.get("chip", adm["medicaid"])) * gross_up
        groups["medicaid"]["cost"] += chip_cost
        chip_today = sum(chip_svc.values())
        groups["medicaid"]["today"] += chip_today

    # ---- the newly covered
    if o["newly"] == "all_ages":
        # the model: everyone now covered, Medicare's enrollees included, at the plan's prices
        claims_now = sum(groups[g]["cost"] for g in ("medicare", "medicaid", "employer", "individual")) / gross_up
        claims_now -= chip_cost / gross_up
        per = claims_now / m["covered_now"]
    else:
        # people under 65: private enrollees' repriced claims per person, children at the model's age index and
        # adults at the level that keeps the private average, mixed in the uninsured's proportions
        priv = (groups["employer"]["cost"] + groups["individual"]["cost"]) / gross_up
        n_priv = m["people"]["esi"] + m["people"]["ng"]
        kid_sh, kid_idx = I["win_esi_kids"], I["age_idx_kids"]
        adult_idx = (1 - kid_sh * kid_idx) / (1 - kid_sh)
        per = priv / n_priv * (UNINS_CHILD_SHARE * kid_idx + (1 - UNINS_CHILD_SHARE) * adult_idx)
    new_cost = m["new_n"] * I["new_enrollee_factor"] * per * (1 + u) * (1 / (1 - a) - cs)
    groups["uninsured"] = dict(cost=new_cost, today=0.0, per_person_2032=new_cost / m["new_n"] * 1000)

    R = I["sp_state_moe"] * max(0.0, (mcd_total - ltc) - (sub_mcd - ltc_fed)) + I["sp_retained_other"]
    replaced = dict(medicare=I["sub_medicare"], medicaid=sub_mcd - ltc_fed, employer=I["sub_esi"],
                    individual=I["sub_ptc"])
    net = {g: groups[g]["cost"] - replaced.get(g, 0.0) for g in groups}
    net["medicaid"] -= R
    state_former = (mcd_total - ltc) - (sub_mcd - ltc_fed)      # what states spent outside long-term care
    if o["chip"] == "in":
        state_former += chip_today * (1 - CHIP_FED_SHARE)
    return dict(groups=groups, net=net, net_total=sum(net.values()), cost_total=sum(v["cost"] for v in groups.values()),
                replaced=replaced, state_moe_booked=R, state_former=state_former, outside=outside,
                outside_total=sum(outside.values()), opts=o, gross_up=gross_up,
                # today's spending by the payers the plan takes over (CHIP's moves out of the model's "other")
                today_total=S["medicare"] + mcd_total + S["phi"] + S["oop"] + chip_today,
                fed_replaced_total=sum(replaced[g] for g in ("medicare", "medicaid", "individual")))


def check_reproduces():
    """DEFAULT must reproduce health_path.groups() on the rebased coverage model."""
    c, HP, I, B, P = _ctx()
    net, cost, _, _ = HP.groups(I, B, P)
    r = rebuild()
    return {g: r["net"][g] - net[g] for g in net}


STEPS = [
    ("1. Physicians and other non-hospital services at the decided fee-schedule rate (1.05, not the hospital 1.15)",
     dict(physician=PLAN_FEE)),
    ("2. The newly covered priced off people under 65 (not an average that includes Medicare's enrollees)",
     dict(newly="nonelderly")),
    ("3. Each payer's own service mix (Table 19), not one national hospital and drug share",
     dict(mix="service", average="spending")),
    ("4a. Private hospital and physician prices averaged by volume (2.54 and 1.4 divided service by service), an error",
     dict(average="volume_hp")),
    ("4b. Private prices for other services at 1.1-1.2 times Medicare and dental on the plan's schedule (working "
     "assumptions, not errors)", dict(average="volume")),
    ("5. Each payer's own administrative share (Table 19)", dict(admin="table")),
    ("6. Out of pocket: nursing homes and over-the-counter products stay outside; Medicare's cost sharing at "
     "Medicare's prices; dental on the plan's schedule", dict(oop="service")),
    ("7. Medicaid's hospital payments at their measured level against Medicare", dict(medicaid_hosp="measured")),
    ("8. CHIP's care added (its federal money was already counted as replaced)", dict(chip="in")),
    ("9. Medicaid and CHIP rebased to CBO's February 2026 baseline (the Medicaid seam)", dict(medicaid_level="cbo")),
]


def bridge(g40=None):
    """Each step's effect, cumulatively, on the 2032 full-scale cost and net federal cost, and FY2040's gross cost,
    states' former spending and the need (x g40). $ billion."""
    if g40 is None:
        g40 = json.load(open(os.devnull)) if False else _g40()
    opts, prev = {}, rebuild()
    rows = [dict(step="0. The memo's model (Medicare rebased to CBO)", cost=prev["cost_total"], net=prev["net_total"],
                 state_former=prev["state_former"], outside=prev["outside_total"],
                 new_pp=prev["groups"]["uninsured"]["per_person_2032"])]
    for label, ch in STEPS:
        opts.update(ch)
        cur = rebuild(opts)
        rows.append(dict(step=label, cost=cur["cost_total"], net=cur["net_total"], state_former=cur["state_former"],
                         outside=cur["outside_total"], new_pp=cur["groups"]["uninsured"]["per_person_2032"],
                         d_cost=cur["cost_total"] - prev["cost_total"], d_net=cur["net_total"] - prev["net_total"],
                         d_state=cur["state_former"] - prev["state_former"],
                         d_outside=cur["outside_total"] - prev["outside_total"],
                         d_national_2040=((cur["cost_total"] + cur["outside_total"] - cur["today_total"])
                                          - (prev["cost_total"] + prev["outside_total"] - prev["today_total"])) * g40,
                         d_fed_2040=(cur["fed_replaced_total"] - prev["fed_replaced_total"]) * g40,
                         d_cost_2040=(cur["cost_total"] - prev["cost_total"]) * g40,
                         d_state_2040=(cur["state_former"] - prev["state_former"]) * g40,
                         d_outside_2040=(cur["outside_total"] - prev["outside_total"]) * g40,
                         by_group={k: cur["groups"][k]["cost"] - prev["groups"][k]["cost"] for k in cur["groups"]}))
        prev = cur
    return rows, opts, g40


CORRECTED = {k: v for _, ch in STEPS for k, v in ch.items()}

LEVERS = [
    ("Administration 4% (design memo D1 B)", {}, dict(sp_admin=0.04)),
    ("Administration 3%", {}, dict(sp_admin=0.03)),
    ("Drug prices 25% below today's (15% decided)", {}, dict(sp_drug_cut=0.25)),
    ("Drug prices 35% below today's", {}, dict(sp_drug_cut=0.35)),
    ("Hospitals at 1.10 times Medicare (1.15 decided)", dict(hosp_rate=1.10), {}),
    ("Hospitals at 1.20 times Medicare", dict(hosp_rate=1.20), {}),
    ("Physicians at 1.00 (Medicare's fee schedule, no add-ons)", dict(physician=1.00), {}),
    ("Physicians at 1.10", dict(physician=1.10), {}),
    ("No added use when cost sharing ends (sp_util_uplift 0)", {}, dict(sp_util_uplift=0.0)),
    ("Twice the added use (sp_util_uplift 0.12)", {}, dict(sp_util_uplift=0.12)),
    ("Newly covered at 70% of comparable use (80% central)", {}, dict(new_enrollee_factor=0.7)),
    ("Newly covered at 100%", {}, dict(new_enrollee_factor=1.0)),
    ("No copays (design memo D4 B)", {}, dict(sp_cs_low_rate=0.0)),
    ("Private physician prices at 1.29 times Medicare (CBO), not 1.4", "phys129", {}),
    ("Private prices for other services at 1.4, as physicians", "other14", {}),
    ("Medicaid's hospital payments at 0.85 of Medicare", "mh085", {}),
    ("Medicaid's hospital payments at 1.05 of Medicare", "mh105", {}),
]


def levers(g40):
    """FY2040 effect on gross cost of each lever, from the corrected base ($ billion; x g40)."""
    global MEDICAID_HOSPITAL_IDX
    base = rebuild(CORRECTED)["cost_total"]
    out = []
    for label, o_, i_ in LEVERS:
        hr = PLAN_HOSPITAL
        opts = dict(CORRECTED)
        keep = (dict(PHI_IDX), MEDICAID_HOSPITAL_IDX)
        try:
            if o_ == "phys129":
                PHI_IDX["physician"] = 1.29
            elif o_ == "other14":
                for k_ in ("other_prof", "home_health", "nursing", "dme", "ohrpc"):
                    PHI_IDX[k_] = 1.4
            elif o_ == "mh085":
                MEDICAID_HOSPITAL_IDX = 0.85
            elif o_ == "mh105":
                MEDICAID_HOSPITAL_IDX = 1.05
            elif isinstance(o_, dict):
                hr = o_.get("hosp_rate", hr)
                opts.update({k_: v for k_, v in o_.items() if k_ != "hosp_rate"})
            cur = rebuild(opts, hosp_rate=hr, I_over=i_)["cost_total"]
        finally:
            PHI_IDX.clear()
            PHI_IDX.update(keep[0])
            MEDICAID_HOSPITAL_IDX = keep[1]
        out.append(dict(lever=label, d_2032=cur - base, d_2040=(cur - base) * g40))
    return out


def _g40():
    import health_booking as HB
    return HB.incidence()["fy2040"]["H7w"] / HB.incidence()["full_scale"]["employer_premiums"]



# ======================================================================================== Part 2: financing
# New general revenue not yet in the plan's base (FY2040, $ billion, central; each net of overlap with the booked rows
# and of avoidance; ranges in the memo). Key: the household model's legacy key for its burden.
NEW_STREAMS = [
    ("Financial transactions tax raised from 0.01% (booked, G10) to 0.1%", 60.0, "ftt", (30, 90)),
    ("Annual wealth tax: 2% above $50M, 3% above $1B, net of the billionaire mark-to-market (G11) it overlaps",
     150.0, "billionaires", (0, 250)),
    ("Capital gains and dividends taxed as ordinary income above $1M of income (gains at death already booked, G6)",
     45.0, "inv400k", (20, 70)),
    ("Corporate: rate 28% to 30% and the 2025 law's permanent expensing repealed", 70.0, "capital", (40, 100)),
    ("The 3.8% investment-income tax extended to active pass-through income (H1a, on the ledger, not booked)", 60.0,
     "above400k", (45, 75)),
]
# Booked general revenue the other flagships now use (FY2040, audit lines, case mixed; $ billion), which health may
# draw on first (Espen, November 15). The other flagships' cuts are left to stage G.
REASSIGNABLE = ("G1", "G9", "C38", "G6", "G11", "C18", "H1b", "G8", "C39", "G7", "G5", "G10", "G3", "C43", "C35",
                "C40", "C41", "GX", "New indexed income contributions")
# Small-employer allowance: the first $100,000 of each employer's pay in the band is exempt (no cliff). From SUSB
# 2022 (Census): about 6% of all pay falls inside it; working figure.
SMALL_FIRM_ALLOWANCE_SHARE = 0.06
# Per-person health cost growth (premiums, out of pocket) 2026-40, real: the memo's 4.8% a year nominal less 2.3%
# prices, 14 years (health-financing.md part 4.2).
REAL_HEALTH_2040 = (1.048 / 1.023) ** 14
COVERED_OOP_SHARE = 1 - (48.699 + 123.230) / 556.554   # out of pocket on services the plan covers (Table 19)


def reassignable():
    L = HF.audit_lines()
    rows = {k: -L.get(k, {}).get(HF.Y, 0.0) for k in REASSIGNABLE}
    return rows, sum(rows.values())


def cost_cases(g40):
    """FY2040 changes against the memo's package A inputs for two cost cases: the errors fixed, and also design memos
    D1 B (administration 4%), D2 B (a national health budget, GDP + 1 from 2037) and D5 (drugs 25% lower)."""
    rows, _, _ = bridge(g40)
    d = lambda k: sum(r.get(k, 0.0) for r in rows[1:])  # noqa: E731
    fixed = dict(gross=d("d_cost_2040"), fed=d("d_fed_2040"), state=d("d_state_2040"), outside=d("d_outside_2040"),
                 national=d("d_national_2040"))
    lv = {r["lever"]: r["d_2040"] for r in levers(g40)}
    ctx = HF.context()
    hold, plan = HF.growth_hold(ctx, 0.01)
    gross_fixed = 8407.05 + fixed["gross"]
    d2 = hold * gross_fixed / plan * (plan / 8448.78) if plan else 0.0
    design = dict(fixed, gross=fixed["gross"] + lv["Administration 4% (design memo D1 B)"]
                  + lv["Drug prices 25% below today's (15% decided)"] + d2,
                  d1=lv["Administration 4% (design memo D1 B)"], d5=lv["Drug prices 25% below today's (15% decided)"],
                  d2=d2)
    return dict(fixed=fixed, design=design)


def _keys_for_micro():
    for k in ("ftt", "billionaires", "inv400k", "above400k"):
        HF.EXTRA_BASES.setdefault(k, lambda h: max(h["capital"], 0.0))


def health_package(ctx, case, spec):
    """A package on a cost case. spec: second (points on AGI above $100K/$200K) or close='second', first (points on
    taxable income), streams (bool), allowance (bool), reassign (closing remainder from booked revenue: bool), emp
    (employer share). Returns the HF package plus the sources and the reassigned amount."""
    _keys_for_micro()
    f40 = dict(ctx["f40"])
    f40["states_moved"] += case["state"]
    f40["households"] -= case["outside"]
    need = ctx["need"] + case["gross"] - case["fed"] - HF.STATE_SHARE_BOOKED * case["state"]
    streams = sum(v for _, v, _, _ in NEW_STREAMS) if spec.get("streams") else 0.0
    allow = SMALL_FIRM_ALLOWANCE_SHARE / HF.band_share() if spec.get("allowance") else 0.0
    emp = spec.get("emp", 1.0) * (1 - allow)
    base = dict(HF.COMMON, emp_share=emp, need=need, f40=f40, savings=streams)
    if spec.get("reassign"):
        # households pay the fixed tiers; booked revenue closes the rest
        o = HF.package(ctx, **dict(base, first=spec.get("first", 0.0), second=spec.get("second", 0.0),
                                   close="second"))
        # what the second tier would have to be, against what is set: the difference is reassigned
        fixed_second = spec.get("second", 0.0)
        got_fixed = fixed_second * ctx["pp"]["high_income"]
        reass = (o["second"] - fixed_second) * ctx["pp"]["high_income"]
        o = HF.package(ctx, **dict(base, first=spec.get("first", 0.0), second=fixed_second,
                                   savings=streams + max(reass, 0.0), close="second"))
        o["reassigned"] = max(reass, 0.0)
    else:
        o = HF.package(ctx, **dict(base, first=spec.get("first"), second=spec.get("second", 0.0),
                                   close=spec.get("close", "first")))
        o["reassigned"] = 0.0
    o["streams"] = streams
    o["allowance_bn"] = allow / (1 - allow) * o["employer_premium_part"] if allow else 0.0
    o["employer_rate_statutory"] = o["employer_rate"] / (1 - allow)   # the rate above each employer's allowance
    if spec.get("streams"):
        extra = [(lb, -v, k) for lb, v, k, _ in NEW_STREAMS]
        o["rows"] = o["rows"] + extra
        o["households"] = HF.per_household(o["rows"], ctx["K"], ctx["hh"])
    o["need_case"] = need
    o["gross"] = 8407.05 + case["gross"]
    return o


PACKAGES2 = {
    "A1": ("Package A on the corrected cost (reference)", "fixed", dict(close="first")),
    "E": ("Take-home first: no charge below $100K/$200K, 4 points above it, new streams, booked revenue for the rest",
          "design", dict(second=4.0, streams=True, allowance=True, reassign=True)),
    "E0": ("Package E without design memos D1, D2 and D5 (the errors-only cost)", "fixed",
           dict(second=4.0, streams=True, allowance=True, reassign=True)),
    "F": ("No household contribution: new streams and booked revenue", "design",
          dict(second=0.0, streams=True, allowance=True, reassign=True)),
    "G": ("Self-financed above a line: the whole remainder on AGI above $100K/$200K, no booked revenue taken", "design",
          dict(streams=True, allowance=True, close="second")),
}


# ---- the take-home test -----------------------------------------------------------------------------------------
STD = {"single": 16100, "joint": 32200, "hoh": 24150}
BRACKETS = {"single": [(12400, .10), (50400, .12), (105700, .22), (201775, .24), (256225, .32), (640600, .35),
                       (1e12, .396)]}
BRACKETS["joint"] = [(a * 2, r) for a, r in BRACKETS["single"]]
LINE_HIGH = {"single": 100000 * 1.027, "joint": 200000 * 1.027}   # $100K/$200K of 2025, in 2026 dollars


def _marginal(taxable, fs):
    for top, r in BRACKETS["joint" if fs == "joint" else "single"]:
        if taxable <= top:
            return r
    return .396


def contribution(agi, fs, o, persons=1):
    """The household health contribution in 2026 dollars for a household in FY2040 under package o (the unified
    contribution of part 3 when o carries `unified`)."""
    if o.get("unified"):
        return unified_charge(agi, fs, persons, o["unified"])
    fsj = "joint" if fs == "joint" else "single"
    taxable = max(agi - STD["joint" if fs == "joint" else "single"], 0.0)
    return o["first"] / 100 * taxable + o["second"] / 100 * max(agi - LINE_HIGH[fsj], 0.0)


# The worker's Medicare payroll tax today: 1.45% of wages and 92.35% of self-employment income (the worker's half),
# and the 0.9% Additional Medicare Tax above $200,000 single / $250,000 joint (sec. 3101(b)(2), not indexed, so the
# threshold falls in real terms: divided by FY2040's price level when costs are in 2026 dollars).
WORKER_HI = 0.0145
AMT_RATE, AMT_THRESHOLD = 0.009, {"single": 200000, "joint": 250000}
LINE_LOW = {"single": 20000 * 1.027, "joint": 40000 * 1.027}      # the booked 2 points' line, 2026 dollars
# Medicare Part B's standard premium, 2026 ($202.90 a month, CMS, November 2025), grown as other premiums. The CPS's
# premiums paid (PHIP_VAL) leave Part B out (Census counts it separately in the SPM's medical costs); working assumption.
PART_B_2026 = 202.90 * 12
PRICE_2040 = None


def worker_hi(earn, fs):
    """The worker's HI and Additional Medicare Tax, FY2040, 2026 dollars, on `earn` (wages plus 92.35% of
    self-employment income, 2026 dollars)."""
    j = "joint" if fs == "joint" else "single"
    return WORKER_HI * max(earn, 0.0) + AMT_RATE * max(earn - AMT_THRESHOLD[j] / PRICE_2040, 0.0)


def visible(agi, fs, persons, kind, prem_share, oop, o, fpl200, earn=None, low2=False):
    """Today's and the plan's visible health costs (2026 dollars, FY2040). Today: premium share, out of pocket on
    covered services, and the worker's HI and 0.9% on `earn` (AGI if not given). The plan: the household contribution,
    copays (none below 200% of poverty), the tax on the pay that used to go to premiums before tax, and the worker's
    HI and 0.9% unless the package folds them into its contribution (part 3). `low2`: also the booked 2 points on AGI
    above $20,000/$40,000 for the other flagships (a stage G item, shown separately)."""
    earn = agi if earn is None else earn
    hi = worker_hi(earn, fs)
    folded = bool(o.get("unified"))
    cp = 0.0 if (agi < fpl200 or kind == "medicaid") else COPAY_2040 * persons
    agi_plan = agi + (prem_share if kind == "job" else 0.0)
    ptax = 0.062 + (0.0 if folded else WORKER_HI)
    tax_prem = prem_share * (_marginal(max(agi_plan - STD["joint" if fs == "joint" else "single"], 0), fs) + ptax) \
        if kind == "job" else 0.0
    plan = contribution(agi_plan, fs, o, persons) + cp + tax_prem + (0.0 if folded else hi)
    if low2:
        plan += 0.02 * max(agi_plan - LINE_LOW["joint" if fs == "joint" else "single"], 0.0)
    return prem_share + oop + hi, plan


COPAY_2040 = None


def _setup_visible(ctx):
    global COPAY_2040, PRICE_2040
    g = 1.048 ** 8 / ctx["price_2040"]                 # 2032 nominal to FY2040 in 2026 dollars
    COPAY_2040 = ctx["pp_person"]["copay"] * g
    PRICE_2040 = ctx["price_2040"]
    oop = {k: v * g * COVERED_OOP_SHARE for k, v in ctx["oop_pp"].items()}
    return g, oop


def earn_unit(u):
    """A tax unit's earnings on the HI base (2029 dollars): wages and 92.35% of self-employment income."""
    return u["wage_h"] + u["wage_s"] + 0.9235 * (max(u["se_h"], 0) + max(u["se_s"], 0))


def _is_worker(u):
    earn = u["wage_h"] + u["wage_s"] + max(u["se_h"], 0) + max(u["se_s"], 0)
    return not (earn <= 0 or (u["age_h"] >= 65 and u["n_medicare"] > 0 and u["wage_h"] <= 0))


def fpl200(persons):
    return 2 * (15650 + 5500 * (persons - 1))


def take_home_micro(ctx, o, low2=False, who="workers", part_b=True):
    """Each worker tax unit (wages or self-employment) on the household model: does what visibly leaves its pay and
    wallet fall? Today's cost counts the worker's HI and 0.9% (the plan's too, unless its contribution replaces them)
    and Medicare Part B's premium (`part_b`). `who`: 'workers', or 'others' (retirees on Medicare without wages and
    every unit with no earnings). Returns pass shares by AGI (2026 dollars), by coverage, and below 200% of
    poverty."""
    g, oop = _setup_visible(ctx)
    K, _, _, _, X = HF.keys()
    U = X["B"]["units"]
    hgrow = 1.048 ** 11 / ctx["price_2040"]            # 2029 nominal to FY2040, 2026 dollars, per person
    igrow = X["grow"] / ctx["price_2040"]
    partb = PART_B_2026 * REAL_HEALTH_2040 if part_b else 0.0
    bands = [(0, 25e3), (25e3, 50e3), (50e3, 75e3), (75e3, 100e3), (100e3, 150e3), (150e3, 200e3), (200e3, 1e12)]
    res = {b: [0.0, 0.0] for b in bands}
    bykind, low = {}, [0.0, 0.0]
    for u in U:
        if _is_worker(u) != (who == "workers"):
            continue
        agi = u["t_agi"] * igrow
        fs = "joint" if u["t_fs"] == "joint" else "single"
        n = max(u["n_people"], 1)
        kind = "job" if u["n_employer_cov"] > 0 else ("own" if u["n_marketplace"] > 0 else
                                                      ("medicaid" if u["n_medicaid"] > 0 else
                                                       ("medicare" if u["n_medicare"] > 0 else "uninsured")))
        prem = u["premiums_paid"] * hgrow
        oo = (u["n_employer_cov"] * oop["esi"] + u["n_marketplace"] * oop["ng_sub"] + u["n_medicaid"] * oop["medicaid"]
              + u["n_medicare"] * oop["medicare"]
              + max(n - u["n_employer_cov"] - u["n_marketplace"] - u["n_medicaid"] - u["n_medicare"], 0)
              * oop["uninsured"]) + u["n_medicare"] * partb
        today, plan = visible(agi, fs, n, kind, prem if kind == "job" else 0.0, oo + (prem if kind != "job" else 0.0),
                              o, fpl200(n), earn=earn_unit(u) * igrow, low2=low2)
        ok = plan <= today
        for b in bands:
            if b[0] <= agi < b[1]:
                res[b][0] += u["weight"]
                res[b][1] += u["weight"] * ok
        bk = bykind.setdefault(kind, [0.0, 0.0])
        bk[0] += u["weight"]
        bk[1] += u["weight"] * ok
        if agi < fpl200(n):
            low[0] += u["weight"]
            low[1] += u["weight"] * ok
    tot = sum(v[0] for v in res.values())
    return dict(by_agi={f"{int(b[0] / 1e3)}-{int(min(b[1], 1e9) / 1e3)}K": 100 * v[1] / v[0] for b, v in res.items()
                        if v[0]},
                by_kind={k: 100 * v[1] / v[0] for k, v in bykind.items()},
                kind_share={k: 100 * v[0] / tot for k, v in bykind.items()},
                all=100 * sum(v[1] for v in res.values()) / tot, below_200fpl=100 * low[1] / low[0],
                below_200fpl_share=100 * low[0] / tot, units_m=tot * ctx["hh"] / X["n29"] / 1e6)


# KFF 2026 (EV-CAR-722): workers' premium shares, single and family.
KFF_SHARE = {"single": 1672, "family": 7471}
# Marketplace premiums before credits (2026, a benchmark silver plan; working figures): single $7,500, family $22,000;
# credits on the original ACA schedule up to 400% of poverty (the enhanced credits ended after 2025).
MKT_PREM = {"single": 7500, "family": 22000}


def _aca_share(agi, persons):
    pct = agi / (15650 + 5500 * (persons - 1))
    if pct > 4:
        return None
    pts = [(1.33, .0210), (1.5, .0315), (2, .0420), (2.5, .0660), (3, .0838), (4, .0996)]
    for top, r in pts:
        if pct <= top:
            return r * agi
    return .0996 * agi


def grid(ctx, o):
    """The take-home grid (2026 dollars, FY2040): single and family of four, AGI $25K-$200K, with job coverage, with
    none (uninsured), and with a plan of their own. Today's costs are today's grown to FY2040 (like with like)."""
    g, oop = _setup_visible(ctx)
    out = []
    for hh_, fs, n in (("single", "single", 1), ("family", "joint", 4)):
        for agi in (25000, 40000, 55000, 72000, 90000, 110000, 150000, 200000):
            for kind in ("job", "uninsured", "own"):
                if kind == "job":
                    prem = KFF_SHARE[hh_] * REAL_HEALTH_2040
                    oo = oop["esi"] * n
                elif kind == "uninsured":
                    prem, oo = 0.0, oop["uninsured"] * n
                else:
                    full = MKT_PREM[hh_]
                    sub = _aca_share(agi, n)
                    prem = (min(full, sub) if sub is not None else full) * REAL_HEALTH_2040
                    oo = oop["ng_sub"] * n
                today, plan = visible(agi, fs, n, kind, prem if kind == "job" else 0.0,
                                      oo + (prem if kind != "job" else 0.0), o, fpl200(n))
                out.append(dict(household=hh_, agi=agi, kind=kind, today=today, plan=plan, change=plan - today,
                                plan_share=100 * plan / agi, today_share=100 * today / agi))
    return out


def household_T(ctx, o):
    """A single worker at $72,000 with job coverage paying about $175 a month and about $1,950 a year out of
    pocket (2026). Today's costs grown to FY2040; the plan at FY2040's rates; 2026 dollars."""
    _setup_visible(ctx)
    prem, oo = 2100 * REAL_HEALTH_2040, 1950 * REAL_HEALTH_2040
    agi = 72000 - 2100
    today, plan = visible(agi, "single", 1, "job", prem, oo, o, fpl200(1))
    c = contribution(agi + prem, "single", o)
    hi = worker_hi(agi, "single")
    hi_plan = 0.0 if o.get("unified") else hi
    return dict(today=today, today_hi=hi, plan=plan, plan_hi=hi_plan, contribution=c, copays=COPAY_2040,
                tax_on_premium=plan - c - COPAY_2040 - hi_plan, plan_without_hi=plan - hi_plan,
                today_without_hi=today - hi, today_2026=4050.0, change=plan - today, plan_share=100 * plan / 72000,
                today_share=100 * today / 72000)


# ---- employers by firm size (SUSB 2022, Census; 2026 dollars at the 2022 pay structure) -------------------------
SUSB = {"Under 20": (5720093, 21950184, 1086.4447), "20-99": (561160, 21977, 1174.6), "100-499": (93341, 18324, 1203.9),
        "500 and over": (21053, 73502, 5500.0)}
# Share of all workers covered by their own employer's plan, by firm size (working figures; KFF's 55% overall,
# EV-CAR-295, lower at small firms), and the employer's spending per covered worker (KFF 2026, EV-CAR-722: single
# $8,132, family $20,832, at a mix of about 55% single).
COVER = {"Under 20": 0.30, "20-99": 0.45, "100-499": 0.55, "500 and over": 0.62}
EMP_PER_COVERED = 0.55 * (9804 - 1672) + 0.45 * (28303 - 7471)


def firms(o, rate_band, neutral_rate=19.313):
    """Employer spending per worker by firm size, today's premiums grown to FY2040 against pay (k: calibrated so that
    employers as a whole pay the same at package A's neutral rate, as package A is built), against the contribution
    per worker at `rate_band`, after the small-employer allowance if the package has one. 2026 dollars."""
    def raw(k_):
        nf, emp, pay_bn = SUSB[k_]
        workers = emp if k_ == "Under 20" else emp * 1000
        avg = pay_bn * 1e9 / workers * 1.11
        return nf, workers, avg, max(avg - 20000, 0) * 0.85
    k = sum(raw(x)[1] * raw(x)[3] * neutral_rate / 100 for x in SUSB) / sum(raw(x)[1] * COVER[x] * EMP_PER_COVERED
                                                                           for x in SUSB)
    out = []
    kk = k
    for k, (nf, emp, pay_bn) in SUSB.items():
        workers = emp if k == "Under 20" else emp * 1000
        avg = pay_bn * 1e9 / workers * 1.11            # 2022 to 2026 pay (about 11%)
        band = max(avg - 20000, 0) * 0.85              # a rough band share for the spread of pay in a firm
        before = COVER[k] * EMP_PER_COVERED * kk
        after = rate_band / 100 * band
        firm_pay_band = band * workers / nf
        allow = min(100000, firm_pay_band) / firm_pay_band if o.get("allowance") else 0.0
        out.append(dict(size=k, firms=nf, workers=workers, avg_pay=avg, premiums_per_worker=before,
                        contribution_per_worker=after * (1 - allow), change=after * (1 - allow) - before,
                        share_of_pay_before=100 * before / avg, share_of_pay_after=100 * after * (1 - allow) / avg))
    return out


def _sources(ctx, o, case):
    """FY2040 sources of the gross cost ($ billion); `check` is what is left over (zero when they add up)."""
    v = HF.system_view(ctx, o)["sources"]
    src = dict(federal_general_revenue_committed=v["federal_general_revenue"] + case["fed"],
               health_payroll_contribution=v["health_payroll_contribution"],
               states=ctx["f40"]["states_moved"] + case["state"], employers=o["employer_gross"],
               households_net_of_credit=o["household_collected"] - o["credit_bn"], hx_remainder=v["hx_remainder"],
               general_revenue_new_streams=o["streams"], general_revenue_reassigned=o["reassigned"])
    src["check"] = o["gross"] - sum(src.values())
    return src


def md(out):
    """Markdown tables for the memo."""
    P = out["packages"]
    w = []
    w.append("| | " + " | ".join(P) + " |")
    w.append("| --- |" + " --- |" * len(P))
    for lab, f in [("Gross cost FY2040 ($B)", lambda p: f"{p['gross']:,.0f}"),
                   ("Household contribution on taxable income", lambda p: f"{p['first']:.1f}%"),
                   ("… on AGI above $100K/$200K (2025 dollars)", lambda p: f"{p['second']:.1f} points"),
                   ("Household contribution collected ($B)", lambda p: f"{p['household_collected']:,.0f}"),
                   ("Employer rate in the band (above the allowance)", lambda p: f"{p['employer_rate']:.1f}%"),
                   ("Employer contribution ($B)", lambda p: f"{p['employer_gross']:,.0f}"),
                   ("Small-employer allowance ($B)", lambda p: f"{p['allowance_bn']:,.0f}"),
                   ("New general revenue ($B)", lambda p: f"{p['streams']:,.0f}"),
                   ("Booked revenue taken from other flagships ($B)", lambda p: f"{p['reassigned']:,.0f}"),
                   ("Plan-wide FY2040 gap after health ($B)", lambda p: f"{p['plan_gap_2040']:,.0f}"),
                   ("Top federal rate on wages", lambda p: f"{p['top_rate']:.1f}%"),
                   ("Workers passing the take-home test", lambda p: f"{p['take_home']['all']:.0f}%"),
                   ("Single worker at $72,000: visible cost a year, HI counted on both sides (today grown: 6,692)",
                    lambda p: f"{p['T']['plan']:,.0f}"),
                   ("Net per household Q1 / Q2 / Q3", lambda p: " / ".join(f"{p['households'][q]:+,}" for q in ("Q1", "Q2", "Q3"))),
                   ("Net per household Q4 / Q5 / top 1%", lambda p: " / ".join(f"{p['households'][q]:+,}" for q in ("Q4", "Q5", "T1"))),
                   ("Bottom-four households losing cash (M; over 5%)", lambda p: f"{p['losers']['bottom_four']:.1f} ({p['losers']['bottom_four_5pct']:.1f})"),
                   ]:
        w.append(f"| {lab} | " + " | ".join(f(p) for p in P.values()) + " |")
    w.append("")
    w.append("| AGI (2026 dollars) | " + " | ".join(P) + " |")
    w.append("| --- |" + " --- |" * len(P))
    for b in next(iter(P.values()))["take_home"]["by_agi"]:
        w.append(f"| {b} | " + " | ".join(f"{p['take_home']['by_agi'][b]:.0f}%" for p in P.values()) + " |")
    for k in ("job", "own", "uninsured", "medicaid", "medicare"):
        w.append(f"| Coverage today: {k} ({next(iter(P.values()))['take_home']['kind_share'][k]:.0f}% of workers) | "
                 + " | ".join(f"{p['take_home']['by_kind'][k]:.0f}%" for p in P.values()) + " |")
    for k, p in P.items():
        w.append(f"\nGrid {k}: today (grown to FY2040) → plan, visible dollars a year, 2026 dollars")
        w.append("| Household | AGI | Job coverage | No coverage | Own plan |")
        w.append("| --- | --- | --- | --- | --- |")
        G = p["grid"]
        for hh_ in ("single", "family"):
            for agi in sorted({g["agi"] for g in G}):
                cells = []
                for kind in ("job", "uninsured", "own"):
                    g = [x for x in G if x["household"] == hh_ and x["agi"] == agi and x["kind"] == kind][0]
                    mark = "pass" if g["plan"] <= g["today"] else "**fail**"
                    cells.append(f"{g['today']:,.0f} → {g['plan']:,.0f} ({g['plan_share']:.1f}%) {mark}")
                w.append(f"| {hh_} | ${agi:,} | " + " | ".join(cells) + " |")
        w.append(f"\nFirms {k}:")
        w.append("| Firm size | Firms | Workers (M) | Average pay | Premiums per worker today | Contribution per worker | Change |")
        w.append("| --- | --- | --- | --- | --- | --- | --- |")
        for f in p["firms"]:
            w.append(f"| {f['size']} | {f['firms']:,} | {f['workers'] / 1e6:.1f} | ${f['avg_pay']:,.0f} | "
                     f"${f['premiums_per_worker']:,.0f} ({f['share_of_pay_before']:.1f}%) | "
                     f"${f['contribution_per_worker']:,.0f} ({f['share_of_pay_after']:.1f}%) | {f['change']:+,.0f} |")
        w.append(f"\nSources {k}: " + ", ".join(f"{a} {b:,.0f}" for a, b in p["sources"].items()))
        w.append(f"T {k}: " + ", ".join(f"{a} {b:,.0f}" for a, b in p["T"].items()))
        w.append(f"Losers by fifth {k}: {p['losers']['by_fifth']}")
    return "\n".join(w)


def run_part2():
    ctx = HF.context()
    g40 = _g40()
    cases = cost_cases(g40)
    re_rows, re_total = reassignable()
    out = dict(cases=cases, reassignable=re_rows, reassignable_total=re_total, packages={})
    for k, (label, case, spec) in PACKAGES2.items():
        o = health_package(ctx, cases[case], spec)
        m = HF.micro(ctx, o)
        th = take_home_micro(ctx, o)
        out["packages"][k] = dict(
            label=label, case=case, spec=spec, gross=o["gross"], first=o["first"], second=o["second"],
            employer_rate=o["employer_rate_statutory"], employer_gross=o["employer_gross"], streams=o["streams"],
            allowance_bn=o["allowance_bn"], sources=_sources(ctx, o, cases[case]),
            reassigned=o["reassigned"], household_collected=o["household_collected"], credit=o["credit_bn"],
            top_rate=o["top_rate_on_wages"], households=o["households"],
            losers=dict(bottom_four=m["bottom_four_losers_m"], bottom_four_5pct=m["bottom_four_lose_5pct_m"],
                        by_fifth={q: round(m[q]["losers_m"], 2) for q in HF.GROUPS}),
            take_home=th, grid=grid(ctx, o), T=household_T(ctx, o),
            firms=firms(spec, o["employer_rate_statutory"]),
            plan_gap_2040=70.0 + o["reassigned"])
    return out


# ======================================================================================== Part 3: the unified contribution
# Espen, November 15: one health contribution replacing the worker's 1.45% HI, the 0.9% Additional Medicare Tax and
# worker HI on former premiums (employers keep their 1.45%); collected by withholding on wages and on the return for
# other income; R% of all AGI, S points on AGI above $200,000/$250,000 of 2025 ($205,400/$256,750 in 2026 dollars,
# indexed as LINE_HIGH is), and a low-income exemption: nothing at or below `lo` times poverty for the tax unit's
# size, the full rate from `hi` times poverty, no cliff. Everything else is package E (cost case "design", the five
# new streams, the small-employer allowance, the worker transition credit; booked revenue closes the rest and may go
# negative, a surplus). Lines and the exemption are applied to FY2040 AGI in 2026 dollars.
SURCHARGE_LINE = {"single": 200000 * 1.027, "joint": 250000 * 1.027}
H1B_LINE = {"single": 400000 * 1.027, "joint": 400000 * 1.027}   # H1b's $400K (one line), indexed the same way
H1B_BN = 62.719            # H1b on the audit lines, FY2040 (Medicare and the investment-income tax to 5% above $400K)
# CBO's 2026 long-term Social Security projections (SRC-3813, table 2): taxable payroll, calendar years, $ trillion.
# HI's base is all covered earnings; taxable payroll is the part under the wage base, about CAP_SHARE (0.83) of it.
CBO_TAXABLE_PAYROLL = {2039: 18.186, 2040: 18.849}
# Plan-wide FY2040 gap before health takes booked revenue ($B), the convention of run_part2 (gap = 70 + reassigned).
GAP_BEFORE_REASSIGN = 70.0


def unified_spec(R, S=5.0, lo=1.38, hi=2.00, form="quadratic", h1b=0.0):
    """R and S in points; `form`: 'quadratic' (charge = R x AGI x the share of the way from lo to hi, the drafted
    design) or 'linear' (charge = R x hi/(hi - lo) x (AGI - lo x poverty), capped at R x AGI: one steady rate in the
    band); `h1b`: points on AGI above H1b's line (H1b restated as its own step)."""
    return dict(R=R, S=S, lo=lo, hi=hi, form=form, h1b=h1b)


def poverty(persons):
    return fpl200(max(persons, 1)) / 2


def unified_charge(agi, fs, persons, u, part="all"):
    """The unified contribution, 2026 dollars, FY2040. `part`: 'all', 'base' (R with the exemption), 'surcharge'
    or 'h1b'."""
    j = "joint" if fs == "joint" else "single"
    agi = max(agi, 0.0)
    out = 0.0
    if part in ("all", "base"):
        F, R, lo, hi = poverty(persons), u["R"] / 100, u["lo"], u["hi"]
        x = agi / F
        if x <= lo:
            b = 0.0
        elif x >= hi:
            b = R * agi
        elif u["form"] == "quadratic":
            b = R * agi * (x - lo) / (hi - lo)
        else:
            b = min(R * agi, R * hi / (hi - lo) * (agi - lo * F))
        out += b
    if part in ("all", "surcharge"):
        out += u["S"] / 100 * max(agi - SURCHARGE_LINE[j], 0.0)
    if part in ("all", "h1b"):
        out += u.get("h1b", 0.0) / 100 * max(agi - H1B_LINE[j], 0.0)
    return out


def exemption_marginal(u):
    """The exemption's own marginal rate (points) at the bottom and top of its band, on top of the other taxes."""
    R, lo, hi = u["R"], u["lo"], u["hi"]
    if u["form"] == "quadratic":
        return R * lo / (hi - lo), R * (2 * hi - lo) / (hi - lo)
    return R * hi / (hi - lo), R * hi / (hi - lo)


def _units(ctx):
    _, _, _, _, X = HF.keys()
    ig = X["grow"] / ctx["price_2040"]
    for u in X["B"]["units"]:
        yield u, u["t_agi"] * ig, ("joint" if u["t_fs"] == "joint" else "single"), max(u["n_people"], 1)


def _old_line_base(ctx):
    """The household model's AGI above $100K/$200K (package E's tier), FY2040, 2026 dollars, weighted 2029 units."""
    return sum(u["weight"] * max(a - LINE_HIGH[j], 0.0) for u, a, j, n in _units(ctx))


def unified_statutory_bn(ctx, u, part="all"):
    """The contribution's statutory yield, FY2040 $B: package E's yield per point above $100K/$200K (the budget
    model's, before the 20% allowance) scaled by the household model's base, as for every variant."""
    pts = 100 * sum(x["weight"] * unified_charge(a, j, n, u, part) for x, a, j, n in _units(ctx))
    return ctx["pp"]["high_income"] / (1 - ctx["pp"]["haircut"]) * pts / _old_line_base(ctx)


def _unified_key(ctx, u):
    """Register the contribution's own quintile key (and its avoidance key, all in the top fifth) on the 2029
    households; nothing else is changed. The top 1%'s share is scaled from the legacy key's 55%, as in the variants."""
    import provisions as P
    K, _, _, _, X = HF.keys()
    tag = "unified_" + "_".join(f"{k}{u[k]}" for k in sorted(u))
    if tag in K:
        return tag
    ig = X["grow"] / ctx["price_2040"]
    P.RULES[tag] = lambda x, L: unified_charge(x["t_agi"] * ig, x["t_fs"], max(x["n_people"], 1), u)
    sh, _ = P.micro_shares(X["B"], "rule:" + tag)
    vals = P.household_base(X["B"], "rule:" + tag)
    ratio = 100 * sum(x["weight"] * unified_charge(a, j, n, u) for x, a, j, n in _units(ctx)) / _old_line_base(ctx)
    t1 = min(K["income_high"][1] * (u["R"] + u["S"] + u.get("h1b", 0.0)) / ratio, sh[4])
    K[tag] = (sh, t1)
    HF.EXTRA_BASES[tag] = lambda h: vals[h["hh"]]
    K["avoid_" + tag] = HF.avoidance_key(K, tag, HF.AVOID_WEIGHTS["central"])
    HF.EXTRA_BASES["avoid_" + tag] = HF.EXTRA_BASES[tag]
    return tag


def worker_hi_bn(ctx, basis="cbo"):
    """The worker's 1.45% HI in FY2040, $B. 'cbo': CBO's taxable payroll (SRC-3813), fiscal year, over CAP_SHARE for
    the earnings above the wage base; 'hf': half of HF's 2.9% on the budget model's payroll point ($135B in 2030 at
    4% a year, assumptions.json's education fund figure); 'micro': the household model's earnings grown with GDP per
    household."""
    if basis == "hf":
        return HF.HI_RATE / 2 * ctx["pp"]["payroll_gross"]
    if basis == "micro":
        _, _, _, _, X = HF.keys()
        return sum(u["weight"] * WORKER_HI * earn_unit(u) * X["grow"] for u in X["B"]["units"]) \
            * ctx["hh"] / X["n29"] / 1e9
    fy = 0.25 * CBO_TAXABLE_PAYROLL[2039] + 0.75 * CBO_TAXABLE_PAYROLL[2040]
    return WORKER_HI * fy * 1000 / HF.CAP_SHARE


def fold_in_lost(ctx, o, basis="cbo"):
    """What the fold-in stops collecting, FY2040 $B: the worker's HI, the 0.9% (household model, statutory
    thresholds, earnings grown with GDP per household) and worker HI on former pre-tax premiums (in HX)."""
    _, _, _, _, X = HF.keys()
    scale = ctx["hh"] / X["n29"] / 1e9
    amt = {}
    for u in X["B"]["units"]:
        thr = AMT_THRESHOLD["joint" if u["t_fs"] == "joint" else "single"]
        amt[u["hh"]] = amt.get(u["hh"], 0.0) + AMT_RATE * max(earn_unit(u) * X["grow"] - thr, 0.0)
    A = sum(h["weight"] * amt.get(h["hh"], 0.0) for h in X["H"]) * scale
    HF.household_key("amt_fold", lambda h: amt.get(h["hh"], 0.0))
    W = worker_hi_bn(ctx, basis)
    hxp = WORKER_HI * o["hx_kept"] / ctx["tau"]
    return dict(W=W, A=A, hxp=hxp, total=W + A + hxp, basis=basis)


def unified_package(ctx, case, u, basis="cbo", haircut=None):
    """Package E with the unified contribution in place of its 4 points above $100K/$200K. Built from package F (no
    household contribution: the remainder booked revenue would close), plus the fold-in's lost revenue, less the
    contribution's yield; its rows feed per_household() and micro() on the contribution's own keys."""
    F = health_package(ctx, case, dict(PACKAGES2["E"][2], second=0.0))
    lost = fold_in_lost(ctx, F, basis)
    tag = _unified_key(ctx, u)
    h = ctx["pp"]["haircut"] if haircut is None else haircut
    st = unified_statutory_bn(ctx, u)
    got = st * (1 - h)
    rows = F["rows"] + [("Worker HI (1.45%) ends", lost["W"], "wages"),
                        ("Additional Medicare tax (0.9%) ends", lost["A"], "amt_fold"),
                        ("Worker HI on former pre-tax premiums ends (HX)", lost["hxp"], "exclusion_end"),
                        ("Unified health contribution: the statutory charge", -st, tag),
                        (f"Unified health contribution: less avoidance ({round(100 * h)}%)", st * h, "avoid_" + tag)]
    o = dict(F, rows=rows, unified=u, key=tag, lost=lost, remainder_F=F["reassigned"], statutory=st,
             household_collected=got, first=0.0, second=0.0, haircut=h,
             reassigned=F["reassigned"] + lost["total"] - got)
    o["plan_gap_2040"] = GAP_BEFORE_REASSIGN + o["reassigned"]
    o["households"] = HF.per_household(rows, ctx["K"], ctx["hh"])
    no_ex = dict(u, lo=0.0, hi=1e-9)
    o["exemption_cost_bn"] = (unified_statutory_bn(ctx, no_ex, "base") - unified_statutory_bn(ctx, u, "base")) * (1 - h)
    o["top_rate_on_wages"] = top_rate_unified(u)
    return o


def top_rate_unified(u, h1b_in_s=0.0):
    """The combined top federal rate on wages (statutory, both halves): the plan's before health (63.0, with H1b's
    5% Medicare rate) less Medicare's 5% (HI 2.9, the 0.9 and H1b's 1.2), plus the employer's 1.45%, R, S and H1b's
    restated step."""
    return HF.TOP_RATE_BEFORE_HEALTH - 5.0 + 1.45 + u["R"] + u["S"] + u.get("h1b", 0.0) + h1b_in_s


def h1b_restated(ctx, haircuts=(0.1, 0.2, 0.3, 0.4)):
    """H1b's wage half loses its base when HI is folded in. Its share of H1b: wages above $400K over AGI above $400K
    on the household model (the investment half stays as a 5% investment-income tax). Restated as its own step (points
    on AGI above $400K) or folded into S (extra surcharge points), each sized to keep the booked $62.7B whole; and
    each at other avoidance allowances (H1b's own yield moves the same way)."""
    _, _, _, _, X = HF.keys()
    ig = X["grow"] / ctx["price_2040"]
    ig_e = sum(x["weight"] * max(earn_unit(x) * ig - H1B_LINE[j], 0.0) for x, a, j, n in _units(ctx))
    ig_a = sum(x["weight"] * max(a - H1B_LINE[j], 0.0) for x, a, j, n in _units(ctx))
    share = ig_e / ig_a
    wage_half = H1B_BN * share
    one = dict(R=0.0, S=0.0, lo=0.0, hi=1e-9, form="quadratic")
    pt_400 = unified_statutory_bn(ctx, dict(one, h1b=1.0), "h1b")
    pt_s = unified_statutory_bn(ctx, dict(one, S=1.0), "surcharge")
    out = dict(wage_share=share, wage_half=wage_half, by_haircut={})
    for hc in haircuts:
        # the points needed to keep the booked wage half whole if the restated step loses `hc` to avoidance, and
        # what H1b itself would raise at that allowance (its booked figure assumes the plan's 20%)
        out["by_haircut"][hc] = dict(own_step_points=wage_half / (pt_400 * (1 - hc)),
                                     fold_into_s_points=wage_half / (pt_s * (1 - hc)),
                                     h1b_yield=H1B_BN * (1 - hc) / 0.8, wage_half_yield=wage_half * (1 - hc) / 0.8)
    out["own_step_points"] = out["by_haircut"][0.2]["own_step_points"]
    out["fold_into_s_points"] = out["by_haircut"][0.2]["fold_into_s_points"]
    return out


def per_household_2026(ctx, o):
    """Net per household by fifth, FY2040, in 2026 dollars (per_household() is in FY2040 dollars)."""
    return {k: round(v / ctx["price_2040"]) for k, v in o["households"].items()}


def unified_row(ctx, case, u, basis="cbo", others=True, part_b=True, haircut=None):
    """One row of the rate table: the package and its tests."""
    o = unified_package(ctx, case, u, basis, haircut)
    th = take_home_micro(ctx, o, part_b=part_b)
    m = HF.micro(ctx, o)
    T = household_T(ctx, o)
    lo_m, hi_m = exemption_marginal(u)
    row = dict(spec=u, reassigned=o["reassigned"], gap=o["plan_gap_2040"], collected=o["household_collected"],
               statutory=o["statutory"], lost=o["lost"], exemption_cost_bn=o["exemption_cost_bn"],
               pass_all=th["all"], pass_below_200=th["below_200fpl"], by_agi=th["by_agi"], by_kind=th["by_kind"],
               kind_share=th["kind_share"], losers=m["bottom_four_losers_m"], losers5=m["bottom_four_lose_5pct_m"],
               T=T, households_2026=per_household_2026(ctx, o), top_rate=o["top_rate_on_wages"],
               marginal_band=(lo_m, hi_m))
    row["pass_with_low2"] = take_home_micro(ctx, o, low2=True, part_b=part_b)["all"]
    if others:
        ot = take_home_micro(ctx, o, who="others", part_b=part_b)
        row["others"] = dict(all=ot["all"], below_200=ot["below_200fpl"], by_kind=ot["by_kind"],
                             kind_share=ot["kind_share"], units_m=ot["units_m"], by_agi=ot["by_agi"])
    return row


RATES = [2.0, 2.25, 2.5, 2.75, 3.0, 3.25, 3.5]
TARGET = 85.0      # Espen: "85-90% of workers to come out ahead (or more)"


def run_part3():
    ctx = HF.context()
    case = cost_cases(_g40())["design"]
    out = dict(lost_bases={b: worker_hi_bn(ctx, b) for b in ("hf", "cbo", "micro")}, rates={}, s4={}, phase={})
    # package E on the same test, for like-for-like household figures
    oE = health_package(ctx, case, PACKAGES2["E"][2])
    thE = take_home_micro(ctx, oE)
    out["E"] = dict(reassigned=oE["reassigned"], gap=GAP_BEFORE_REASSIGN + oE["reassigned"], pass_all=thE["all"],
                    pass_below_200=thE["below_200fpl"], T=household_T(ctx, oE), top_rate=oE["top_rate_on_wages"],
                    losers=HF.micro(ctx, oE)["bottom_four_losers_m"], households_2026=per_household_2026(ctx, oE),
                    others=take_home_micro(ctx, oE, who="others")["all"],
                    pass_with_low2=take_home_micro(ctx, oE, low2=True)["all"])
    for R in RATES:
        out["rates"][R] = unified_row(ctx, case, unified_spec(R))
    ok = [R for R in RATES if out["rates"][R]["pass_all"] >= TARGET]
    out["meets_target"] = ok
    near = sorted(RATES, key=lambda R: abs(R - (max(ok) if ok else RATES[0])))[:2]
    for R in sorted(near):
        out["s4"][R] = unified_row(ctx, case, unified_spec(R, S=4.0), others=False)
    Rc = max(ok) if ok else RATES[0]
    out["chosen"] = Rc
    for name, kw in (("to 250%", dict(hi=2.5)), ("to 300%", dict(hi=3.0)), ("steady rate to 200%", dict(form="linear")),
                     ("steady rate to 250%", dict(hi=2.5, form="linear"))):
        out["phase"][name] = unified_row(ctx, case, unified_spec(Rc, **kw), others=False)
    out["h1b"] = h1b_restated(ctx)
    out["haircut"] = {hc: unified_package(ctx, case, unified_spec(Rc), haircut=hc)["reassigned"]
                      for hc in (0.1, 0.2, 0.3, 0.4)}
    out["basis"] = {b: unified_package(ctx, case, unified_spec(Rc), basis=b)["reassigned"]
                    for b in ("hf", "cbo", "micro")}
    out["part_b_off"] = take_home_micro(ctx, unified_package(ctx, case, unified_spec(Rc)), who="others",
                                        part_b=False)["all"]
    return out


def md3(out):
    """Markdown tables for part 3 of the memo."""
    w = ["| R (S = 5) | Workers ahead | Below 200% of poverty | Retirees and non-workers ahead | With the booked 2 points "
         "| Bottom-four losers (M) | T: today → plan | Booked revenue taken ($B) | Plan-wide gap ($B) | Top rate on wages |",
         "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |"]
    E = out["E"]
    w.append(f"| E (4 above $100K/$200K, HI kept) | {E['pass_all']:.1f}% | {E['pass_below_200']:.1f}% | "
             f"{E['others']:.1f}% | {E['pass_with_low2']:.1f}% | {E['losers']:.1f} | "
             f"{E['T']['today']:,.0f} → {E['T']['plan']:,.0f} | {E['reassigned']:,.0f} | {E['gap']:,.0f} | "
             f"{E['top_rate']:.1f}% |")

    def line(lab, r):
        mark = " **✓**" if r["pass_all"] >= TARGET else ""
        oth = f"{r['others']['all']:.1f}%" if "others" in r else "—"
        return (f"| {lab}{mark} | {r['pass_all']:.1f}% | {r['pass_below_200']:.1f}% | {oth} | "
                f"{r['pass_with_low2']:.1f}% | {r['losers']:.1f} | {r['T']['today']:,.0f} → {r['T']['plan']:,.0f} | "
                f"{r['reassigned']:,.0f} | {r['gap']:,.0f} | {r['top_rate']:.2f}% |")
    for R, r in out["rates"].items():
        w.append(line(f"{R:.2f}%", r))
    for R, r in out["s4"].items():
        w.append(line(f"{R:.2f}% with S = 4", r))
    w += ["", "| Exemption at R = %.2f%% | Workers ahead | Below 200%% | Exemption's cost ($B) | Its own marginal rate "
          "(points) | Booked revenue taken ($B) | Gap ($B) |" % out["chosen"], "| --- | --- | --- | --- | --- | --- | --- |"]
    base = out["rates"][out["chosen"]]
    for lab, r in [("138% to 200%, as drafted", base)] + list(out["phase"].items()):
        lo, hi = r["marginal_band"]
        w.append(f"| {lab} | {r['pass_all']:.1f}% | {r['pass_below_200']:.1f}% | {r['exemption_cost_bn']:.1f} | "
                 f"{lo:.1f} to {hi:.1f} | {r['reassigned']:,.0f} | {r['gap']:,.0f} |")
    return "\n".join(w)


def main():
    if "--part3" in sys.argv:
        out = run_part3()
        print(md3(out) if "--md" in sys.argv else json.dumps(out, indent=1, default=float))
        return
    rows, opts, g40 = bridge()
    lv = levers(g40)
    if "--part2" in sys.argv:
        out = run_part2()
        print(md(out) if "--md" in sys.argv else json.dumps(out, indent=1, default=float))
        return
    if "--json" in sys.argv:
        print(json.dumps(dict(bridge=rows, g40=g40, reproduces=check_reproduces(), levers=lv), indent=1,
                         default=float))
        return
    print("Reproduces groups():", {k: round(v, 6) for k, v in check_reproduces().items()})
    print(f"g40 = {g40:.4f}")
    print(f"{'step':90s} {'cost32':>8s} {'d32':>7s} {'d2040':>7s} {'dNat40':>7s} {'dFed40':>7s} {'dState40':>8s} "
          f"{'dOut40':>7s} {'new pp':>7s}")
    for r in rows:
        print(f"{r['step'][:90]:90s} {r['cost']:8.0f} {r.get('d_cost', 0):7.0f} {r.get('d_cost_2040', 0):7.0f} "
              f"{r.get('d_national_2040', 0):7.0f} {r.get('d_fed_2040', 0):7.0f} "
              f"{r.get('d_state_2040', 0):8.0f} {r.get('d_outside_2040', 0):7.0f} {r['new_pp']:7.0f}")
    for r in lv:
        print(f"  {r['lever']:70s} {r['d_2040']:8.0f}")


if __name__ == "__main__":
    main()
