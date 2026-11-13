#!/usr/bin/env python3
"""Run the household model: the 2029 baseline, its benchmarks, the typical families and the provision scenarios.

Role: the household model's one command (`MODEL-CARD.md`, "How to run"). Status: working.

  python3 models/tools/household/run.py --ledger build/ledger.json --out build/household

Writes `results.json` and `results.md` (generated; regenerate, never edit). `run-all.sh` runs it after the ledger is
built and copies both into `models/tools/household/`.
"""
import argparse
import json
import os

from budget import baseline
from distribution import assign, average_rates, table
from families import CEILING, CEILING_CASES, FAMILIES, ceiling_check, marginal_rates
from poverty import rates
import provisions as P

TPC_2029 = {  # Tax Policy Center T26-0045 (June 18, 2026), 2029, % of expanded cash income: income tax, payroll
    1: (-3.66, 6.08), 2: (-0.07, 7.70), 3: (4.52, 7.69), 4: (7.71, 7.90), 5: (16.16, 5.52), "T1": (23.33, 2.13),
    "all": (10.85, 6.51)}
CENSUS_2025 = {"all": 13.1, "children": 13.4, "18_64": 12.3, "65_plus": 15.4}  # P60-290, table 4
SOI_2023 = {"eitc_bn": 66.27, "ctc_odc_nonref_bn": 84.42, "actc_bn": 34.53}     # IRS SOI tables 2.5 and 3.3


def r1(x):
    return round(x, 1)


def unit_distribution(B):
    """Tax units ranked by expanded cash income, quintiles of equal numbers of people (TPC's convention)."""
    us = B["units"]
    for u in us:
        u["expanded"] = u["cash"] + u["t_fica_er"]
        u["income_tax"] = u["t_income_tax"]
        u["payroll"] = u["t_payroll"]
        u["numper"] = u["n_people"]
    assign(us, "expanded", by="people")
    return average_rates(us)


def aggregates(B):
    us = B["units"]
    s = lambda k: sum(u["weight"] * u[k] for u in us) / 1e9
    return {"agi_bn": r1(s("t_agi")), "census_agi_bn": r1(s("c_agi")),
            "income_tax_bn": r1(s("t_income_tax")), "census_income_tax_bn": r1(s("c_fedtax_ac") - s("c_eitc") - s("c_actc")),
            "eitc_bn": r1(s("t_eitc")), "census_eitc_bn": r1(s("c_eitc")),
            "ctc_bn": r1(s("t_ctc_total")), "census_ctc_bn": r1(s("c_ctc") + s("c_actc")),
            "actc_bn": r1(s("t_actc")), "census_actc_bn": r1(s("c_actc")),
            "payroll_employee_bn": r1(s("t_fica_ee") + s("t_se_tax")), "census_fica_bn": r1(s("c_fica")),
            "households_m": r1(sum(h["weight"] for h in B["households"]) / 1e6)}


def poverty_block(B, with_census_field=False):
    out = {"model": {k: {kk: round(vv, 2) for kk, vv in v.items()} for k, v in rates(B["spm"], "resources_model").items()},
           "census_taxes": {k: {kk: round(vv, 2) for kk, vv in v.items()} for k, v in rates(B["spm"], "resources_census").items()}}
    if with_census_field:
        out["census_published_field"] = {k: round(v["rate"], 2) for k, v in rates(B["spm"], "resources").items()}
    return out


def provision_runs(B, ledger_path):
    led = P.ledger_values(ledger_path)
    pkg, opts = P.rows(led)
    S = P.scenarios()
    KL = P.legacy_keys()
    KM, src = P.model_keys(B)
    hh = P.mid_window_households(B)
    inc = P.model_incomes(B)
    out = {"keys": {k: {"source": src[k], "shares": [r1(x) for x in KM[k][0]], "top1": r1(KM[k][1]),
                        "legacy": KL[k][0], "legacy_top1": KL[k][1]} for k in KM},
           "households_mid_window_m": r1(hh / 1e6), "group_income_mid_window": {k: round(v) for k, v in inc.items()},
           "scenarios": {}}
    for name, (o, drop) in S.items():
        legacy = P.run(pkg, opts, o, drop, KL)[0]
        model = P.run(pkg, opts, o, drop, KM, hh, inc)[0]
        out["scenarios"][name] = {"legacy": legacy, "model": model}
    # reconciliation, scenario Q: from the legacy setup to the model's, one change at a time
    qname = next(n for n in S if n.startswith("Q."))
    o, drop = S[qname]
    steps = [("Legacy model (legacy keys, 140M households)", dict(KL), P.LEGACY_HH)]
    K = dict(KL)
    steps.append((f"Households: the CPS count grown to FY2034-35, {hh / 1e6:.1f}M", dict(K), hh))
    for k in sorted(KM, key=lambda k: k):
        if src[k] == "micro":
            K[k] = KM[k]
            steps.append((f"Key `{k}` measured on the CPS", dict(K), hh))
    rec, prev = [], None
    for label, keys, n in steps:
        res = P.run(pkg, opts, o, drop, keys, n)[0]
        row = {"step": label, **{g: res[g]["net"] for g in P.GROUPS + ["Q5x", "T1"]}}
        if prev:
            row["change_q4"] = row["Q4"] - prev["Q4"]
            row["change_q1"] = row["Q1"] - prev["Q1"]
        rec.append(row)
        prev = row
    out["reconciliation_q"] = rec
    # sensitivity (the lead's answer on #318): the housing key as typed (60% in Q1) in place of the CPS measure
    Ks = dict(KM)
    Ks["housing"] = KL["housing"]
    out["sensitivity_housing_legacy_q"] = {
        "central": {g: out["scenarios"][qname]["model"][g]["net"] for g in P.GROUPS + ["Q5x", "T1"]},
        "housing_legacy": {g: v["net"] for g, v in P.run(pkg, opts, o, drop, Ks, hh, inc)[0].items()}}
    return out


def state_medians(B):
    """Median cash income of four-person SPM units, nationally and by state (states with 40 or more such units), in
    2029 dollars: the CPS's stand-in for HHS's state median income, which FAM-2.01's lines use."""
    st = {h["hh"]: h["state"] for h in B["households"]}
    by = {}
    for s in B["spm"]:
        if s["numper"] == 4:
            by.setdefault(st[s["hh"]], []).append((s["totval_y"], s["weight"]))

    def med(v):
        v, acc = sorted(v), 0.0
        half = sum(w for _, w in v) / 2
        for x, w in v:
            acc += w
            if acc >= half:
                return x
    states = {k: med(v) for k, v in by.items() if len(v) >= 40}
    return {"national": round(med([x for v in by.values() for x in v])), "lowest": round(min(states.values())),
            "lowest_state_fips": min(states, key=states.get), "states": len(states)}



def ceiling_options(B):
    """What two fixes would cost on the 2029 households (static, full take-up), for the lead's options."""
    from collections import defaultdict
    out = {}
    for x in (500, 750):
        c = sum(u["weight"] * min(u["t_tax_before_credits"], x * (u["n_dep_u6"] + u["n_dep_6_16"] + u["n_dep_17"]))
                for u in B["units"])
        out[f"family_offset_{x}_bn"] = r1(c / 1e9)
    earn = defaultdict(float)
    for u in B["units"]:
        earn[u["spm"]] += max(u["wage_h"] + u["wage_s"] + u["se_h"] + u["se_s"] + u["dep_wages"], 0)
    out["snap_earnings_deduction_45_bn_upper"] = r1(sum(s["weight"] * 0.3 * 0.25 * earn[s["spm"]]
                                                        for s in B["spm"] if s["snap"] > 0) / 1e9)
    return out


def secure_floor_rules(B, ledger_path):
    """The secure floor's rules on the 2029 baseline households: what each pays in 2029 at full take-up, against the
    booked FY2030-39 yearly average; and INC-1.02's other reading (`rules.inc1_02_age_aligned`)."""
    from rules import RULES, inc1_02_age_aligned
    led = P.ledger_values(ledger_path)
    us, L = B["units"], B["law"]
    tot = lambda fn: sum(u["weight"] * fn(u, L) for u in us) / 1e9
    snap_cut = sum(h["weight"] * h["snap_cut"] for h in B["households"]) / 1e9
    out = {"inc1_childless_eitc_bn": r1(tot(RULES["inc1_childless_eitc"])), "inc1_booked_avg_bn": r1(100 * led["INC-1"]),
           "snap_cut_bn": r1(snap_cut), "inc2_booked_avg_bn": r1(100 * led["INC-2"]),
           "inc3_02_exclusions_bn_2034_prices": round(tot(RULES["ssi_exclusions_indexed"]), 2),
           "inc4_cdctc_refundable_bn": round(tot(RULES["cdctc_refundable"]), 2), "inc4_booked_avg_bn": r1(100 * led["INC-4"]),
           "smi4": round(L["smi4"])}
    alt = [(u["weight"], inc1_02_age_aligned(u, L)) for u in us]
    out["inc1_02_age_aligned"] = {"units_losing_m": round(sum(w for w, x in alt if x < 0) / 1e6, 2),
                                  "loss_bn": round(sum(w * x for w, x in alt if x < 0) / 1e9, 2),
                                  "avg_loss": round(sum(w * x for w, x in alt if x < 0) / max(sum(w for w, x in alt if x < 0), 1))}
    return out


def money(v):
    return ("+" if v >= 0 else "−") + f"${abs(v):,.0f}"


def markdown(R):
    o = []
    A = o.append
    A("# Household model: results\n")
    A("Generated by `models/tools/household/run.py` from the committed CPS extract, the budget model's ledger and the "
      "adopted incidence rows. Role: generated results of `MOD-household` (`MODEL-CARD.md`). Regenerate it; never edit "
      "it by hand. Status: working (step M3, part 2 under way).\n")
    b25, b29 = R["baseline_2025"], R["baseline_2029"]
    A("## 1. SPM poverty, baseline\n")
    A("Percent of people below the SPM line. 2025 is the survey year; 2029 is current law aged to 2029 (`MODEL-CARD.md`, A-2 to A-6). "
      "\"Census taxes\" keeps the Census tax model's figures (at their 2025 share of cash income when aged); \"model\" puts "
      "the model's own federal income and payroll taxes in their place.\n")
    A("| Group | Census, published 2025 (P60-290) | 2025, Census taxes | 2025, model taxes | 2029, Census taxes held | 2029, model |\n| --- | --- | --- | --- | --- | --- |")
    names = {"all": "All people", "children": "Children under 18", "18_64": "Adults 18-64", "65_plus": "65 and over"}
    for k, n in names.items():
        A(f"| {n} | {CENSUS_2025[k]}% | {b25['poverty']['census_taxes'][k]['rate']:.1f}% | {b25['poverty']['model'][k]['rate']:.1f}% "
          f"| {b29['poverty']['census_taxes'][k]['rate']:.1f}% | {b29['poverty']['model'][k]['rate']:.1f}% |")
    A(f"\nPoor people in 2029 (model): {b29['poverty']['model']['all']['poor_m']:.1f} million, of whom "
      f"{b29['poverty']['model']['children']['poor_m']:.1f} million children. SPM poverty gap in 2029: "
      f"${b29['poverty_gap_bn']:.0f} billion a year.\n")
    sl = R["snap_law_2029"]
    A("### SNAP under P.L. 119-21 in the 2029 baseline (A-8)\n")
    A("The 2029 baseline applies the 2025 law's SNAP changes (`snap2025.py`): the wider work rule, calibrated to CBO's "
      "participation estimates by group, and the energy-assistance and internet-cost changes. Not applied: the state cost "
      "share's state responses and the noncitizen rule.\n")
    A(f"- SNAP in 2029, as the CPS reports it: ${sl['snap_prior_law_bn']}B at prior law, ${sl['snap_bn']}B under the law "
      f"({sl['cut_pct']}% less). About {sl['people_losing_m']} million people (on the CPS's weights) lose benefits under the "
      f"work rule. Probabilities that an at-risk adult loses benefits: 55-64 without children {sl['probabilities']['n_abawd_55_64']}, "
      f"parents whose youngest child is 14-17 {sl['probabilities']['n_parent_child14']}, 18-54 without children "
      f"{sl['probabilities']['n_abawd_prior']}.")
    pl = sl["prior_law_poverty"]
    m = b29["poverty"]["model"]
    A(f"- SPM poverty in 2029: {pl['all']['rate']:.2f}% at prior-law SNAP, {m['all']['rate']:.2f}% under the law "
      f"(children {pl['children']['rate']:.2f}% and {m['children']['rate']:.2f}%); "
      f"{(m['all']['poor_m'] - pl['all']['poor_m']) * 1000:,.0f} thousand more people poor. The CPS records under half "
      "of SNAP's benefits, so this understates the law's effect (`MODEL-CARD.md`, A-8).\n")
    A("## 2. Tax aggregates against the Census tax model, 2025 law\n")
    A("Billions of dollars, income year 2025, the same records. The Census tax model is the published companion of the "
      "CPS; the model's own calculator is what provisions run through.\n")
    A("| Item | Model | Census tax model |\n| --- | --- | --- |")
    a = b25["aggregates"]
    for lab, m, c in [("Adjusted gross income", "agi_bn", "census_agi_bn"),
                      ("Income tax after all credits", "income_tax_bn", "census_income_tax_bn"),
                      ("Earned income credit", "eitc_bn", "census_eitc_bn"),
                      ("Child tax credit and other-dependent credit, with the refundable part", "ctc_bn", "census_ctc_bn"),
                      ("  of which refundable (ACTC)", "actc_bn", "census_actc_bn"),
                      ("Employee payroll and self-employment tax", "payroll_employee_bn", "census_fica_bn")]:
        A(f"| {lab} | {a[m]:,.1f} | {a[c]:,.1f} |")
    A(f"\nIRS Statistics of Income, tax year 2023 (2023 law, all returns): earned income credit ${SOI_2023['eitc_bn']}B; child and "
      f"other-dependent credits ${SOI_2023['ctc_odc_nonref_bn']}B nonrefundable plus ${SOI_2023['actc_bn']}B refundable. "
      "`MODEL-CARD.md`, \"Benchmarks\", explains the gaps.\n")
    A("## 3. Distribution, 2029 baseline\n")
    A("### D3 convention: households by size-adjusted expanded cash income, equal numbers of households\n")
    A("| Group | Households (M) | Average expanded cash income | Income tax rate | Payroll tax rate | Federal rate (these two) | Share of income tax |\n| --- | --- | --- | --- | --- | --- | --- |")
    for g, lab in [("1", "Q1"), ("2", "Q2"), ("3", "Q3"), ("4", "Q4"), ("5", "Q5"), ("T1", "Top 1%"), ("all", "All")]:
        v = b29["distribution_d3"][g]
        A(f"| {lab} | {v['households_m']:.1f} | ${v['avg_income']:,.0f} | {v['income_tax_rate']:.1f}% | {v['payroll_rate']:.1f}% | {v['federal_rate']:.1f}% | {v['share_income_tax']:.1f}% |")
    A("\n**Deciles** (same convention): average expanded cash income and the two federal rates.\n")
    A("| Decile | " + " | ".join(str(d) for d in range(1, 11)) + " |\n| --- |" + " --- |" * 10)
    D = b29["distribution_deciles"]
    A("| Income | " + " | ".join(f"${D[str(d)]['avg_income'] / 1000:,.0f}K" for d in range(1, 11)) + " |")
    A("| Income tax | " + " | ".join(f"{D[str(d)]['income_tax_rate']:.1f}%" for d in range(1, 11)) + " |")
    A("| Payroll | " + " | ".join(f"{D[str(d)]['payroll_rate']:.1f}%" for d in range(1, 11)) + " |")
    A("\n### Benchmark: tax units, equal numbers of people (the Tax Policy Center's convention), against TPC T26-0045 (2029)\n")
    A("| Group | Model income tax | TPC income tax | Model payroll | TPC payroll |\n| --- | --- | --- | --- | --- |")
    for g, lab in [("1", "Q1"), ("2", "Q2"), ("3", "Q3"), ("4", "Q4"), ("5", "Q5"), ("T1", "Top 1%"), ("all", "All")]:
        v = b29["distribution_tpc"][g]
        t = TPC_2029[int(g) if g.isdigit() else g]
        A(f"| {lab} | {v['income_tax_rate']:.1f}% | {t[0]:.1f}% | {v['payroll_rate']:.1f}% | {t[1]:.1f}% |")
    A("\n## 4. Typical families: cents lost per added dollar of earnings, 2029 law\n")
    A("The baseline for the secure floor's 65-cent ceiling (INC-5.02). Layers: employee payroll tax, income tax after "
      "credits (with the earned income and child credits), SNAP on federal rules (no excess shelter deduction) and, where "
      "shown, the premium tax credit for a family on the marketplace. Housing's rent rule is outside the ceiling. "
      "Medicaid and CHIP end at lines, not rates (`families.py`, `cliffs`). The \"plan preview\" adds FAM-1's child benefit "
      "and INC-1.01's childless credit only; it is not the ceiling check, which is part 2. A figure above 100 marks a cliff "
      "inside the $1,000 step (SNAP's gross or net income test), not a rate.\n")
    for fk, f in FAMILIES.items():
        A(f"**{f['label']}**\n")
        A("| % of poverty | Earnings | Payroll | Income tax | SNAP | Total | With the premium credit | With a $1,400 rent (SNAP shelter deduction) | Plan preview |\n| --- | --- | --- | --- | --- | --- | --- | --- | --- |")
        for row, m, sh, pl in zip(R["families"][fk]["current"], R["families"][fk]["marketplace"], R["families"][fk]["shelter"], R["families"][fk]["plan"]):
            A(f"| {row['pct_poverty']}% | ${row['earnings']:,} | {row['payroll']:.1f} | {row['income_tax']:.1f} | {row['snap']:.1f} | **{row['total']:.1f}** | {m['total']:.1f} | {sh['total']:.1f} | {pl['total']:.1f} |")
        A("")
    pr = R["provisions"]
    A("## 5. Provisions by household group (the D3 net test), FY2030-39 average\n")
    A(f"Net dollars per household per year (benefits minus costs). \"Legacy\" reproduces the legacy incidence model "
      f"(`legacy/index/revenue-household-incidence-model.md`); \"model\" measures the keys `keys.csv` marks `micro` on the "
      f"2029 CPS households and divides by the model's mid-window household count ({pr['households_mid_window_m']}M: the CPS's count grown "
      f"with CBO's households; the legacy model used 140M). Amounts are the booked ledger rows in both.\n")
    A("| Scenario | Version | Q1 | Q2 | Q3 | Q4 | Q5 | 80-99th | Top 1% |\n| --- | --- | --- | --- | --- | --- | --- | --- | --- |")
    for n, v in pr["scenarios"].items():
        for ver in ("legacy", "model"):
            r = v[ver]
            A(f"| {n.split('.')[0]} | {ver} | " + " | ".join(money(r[g]["net"]) for g in P.GROUPS + ["Q5x", "T1"]) + " |")
    A("\n### Reconciliation, scenario Q: from the legacy figures to the model's, one change at a time\n")
    A("| Step | Q1 | Q2 | Q3 | Q4 | Q5 | Top 1% | Change in Q4 |\n| --- | --- | --- | --- | --- | --- | --- | --- |")
    for row in pr["reconciliation_q"]:
        ch = money(row["change_q4"]) if "change_q4" in row else ""
        A(f"| {row['step']} | " + " | ".join(money(row[g]) for g in ["Q1", "Q2", "Q3", "Q4", "Q5", "T1"]) + f" | {ch} |")
    sv = pr["sensitivity_housing_legacy_q"]
    A("\n### Sensitivity, scenario Q: the housing key\n")
    A("The central case measures housing's key on the CPS (today's assisted households, 93% in Q1). The sensitivity "
      "keeps the legacy key (60% in Q1), for awards that reach further up than today's assistance.\n")
    A("| Housing key | Q1 | Q2 | Q3 | Q4 | Q5 |\n| --- | --- | --- | --- | --- | --- |")
    for lab, k in (("CPS-measured (central)", "central"), ("Legacy, 60% in Q1 (sensitivity)", "housing_legacy")):
        A(f"| {lab} | " + " | ".join(money(sv[k][g]) for g in P.GROUPS) + " |")
    A("\n### The keys: measured against legacy\n")
    A("Percent of each key's total by quintile, and the top 1%'s share. Only keys marked `micro` in `keys.csv` change.\n")
    A("| Key | Source | Model Q1-Q5 | Model top 1% | Legacy Q1-Q5 | Legacy top 1% |\n| --- | --- | --- | --- | --- | --- |")
    for k, v in pr["keys"].items():
        if v["source"] == "micro":
            A(f"| {k} | measured | {', '.join(f'{x:g}' for x in v['shares'])} | {v['top1']:g} | {', '.join(f'{x:g}' for x in v['legacy'])} | {v['legacy_top1']:g} |")
    A("\nThe other keys stay as the legacy model typed them; `keys.csv` says why for each.\n")
    sf = R["secure_floor_rules"]
    a102 = sf["inc1_02_age_aligned"]
    A("## 6. The secure floor's INC-1 to INC-5 on the 2029 households\n")
    A("Each is a row of the D3 test (`incidence-rows.csv`, INC1 to INC5). Its amount is the booked ledger line; the "
      "household model gives its key (`keys.csv`, `rules.py`). Model amounts are 2029, at full take-up; booked amounts "
      "are the FY2030-39 yearly average.\n")
    A("| Item | Key | Model, 2029 | Booked, yearly average |\n| --- | --- | --- | --- |")
    A(f"| INC-1: the 2021 childless credit (INC-1.01) | `eitc_childless` (rule) | ${sf['inc1_childless_eitc_bn']}B | ${sf['inc1_booked_avg_bn']}B |")
    A(f"| INC-2: SNAP's 2025 cuts repealed | `snap_cut` 43.7%, `snap` 56.3% (CBO's sections) | ${sf['snap_cut_bn']}B of cuts the model applies (CPS-reported SNAP) | ${sf['inc2_booked_avg_bn']}B |")
    A("| INC-3: SSI's limits, exclusions and the territories | `ssi` 75.5%, `ssi_exclusions` 24.5% (the booking's parts) | — | — |")
    A(f"| INC-4: the refundable dependent care credit | `cdctc` (rule) | ${sf['inc4_cdctc_refundable_bn']}B | ${sf['inc4_booked_avg_bn']}B |")
    A("| INC-5: the exclusion rule's forgone offsets | `housing` | — | — |")
    A(f"\n- **INC-4 measures far below its booking.** On the CPS's child care spending, net of the child care guarantee "
      f"(free below 85% of median income, a capped charge above; the CPS's national median for four-person units, "
      f"${sf['smi4']:,}, stands in for state median income), refundability pays about ${sf['inc4_cdctc_refundable_bn']}B "
      "a year. Most families who pay for care owe enough tax to use today's credit, and the guarantee takes over the "
      "care of the youngest children. The CPS misses care for dependent adults and under-reports spending, so this "
      "is a floor, but the booked $4.5 billion (a judgment, $3-6 billion) looks high. The key's shares are used, not "
      "its level; the booking is unchanged (a change would be its own tier-3 step). *Why the CPS may run low:* the "
      "survey under-reports what families pay for care, most of all informal and part-year care; it has no care for "
      "dependent adults; its national median income for four ($" + f"{sf['smi4']:,}" + ") runs above HHS's state "
      "medians, so more care counts as free under the guarantee; and families with little tax who pay for care are "
      "few in it. The full-take-up assumption pushes the other way. *What would settle it:* IRS Statistics of "
      "Income's Form 2441 claims by income and tax owed (the share of today's credit that liability limits), or a "
      "published score of a refundable credit (JCT's or TPC's for the 2021 version), each adjusted for the "
      "guarantee.")
    A(f"- **INC-1.02 moves no money on the CPS** under the reading the rule takes: the Census already assigns each child "
      "to one tax unit by residence. If the earned income credit's age test were instead aligned to the child "
      f"benefit's (under 18), about {a102['units_losing_m']} million filing units with an 18-year-old or a student "
      f"19-23 would lose about ${-a102['loss_bn']}B a year (about ${-a102['avg_loss']:,} each). The specification "
      "(`dossiers/secure-floor/4-specification.md`, INC-1.02) does not say which reading it means.")
    A("- **INC-3.03's territory residents are not in the CPS**, nor in the D3 test's households; their benefit is "
      "spread like today's SSI.\n")
    ceiling_markdown(R, A)
    return "\n".join(o) + "\n"


def ceiling_markdown(R, A):
    C = R["ceiling"]
    sm, chk, op = C["state_median_income_4"], C["check"], C["options"]
    A("## 7. The 65-cent ceiling check (INC-5.02, shared rule 2)\n")
    A("For the three typical families at 50% to 300% of poverty: the combined cents lost per added dollar of earnings "
      "from every federal layer under the decided plan, taxes included, against the published ceiling of 65 cents. "
      "Housing's 30% rent rule is outside it, as INC-5.02 says. Layers (`families.py`, `plan_budget`): payroll with paid "
      "leave's worker share (FAM-3.04, 0.3%); income tax at 2029 law with FAM-1's child benefit in place of today's "
      "child credit and INC-1.01's childless credit; SNAP on the rules INC-2 restores, with and without the excess "
      "shelter deduction; the premium tax credit on the marketplace in 2030-34, which the single plan ends from 2035; "
      "child care's charge for the child under 5 (FAM-2.01), net of INC-4's refundable credit. The charge depends on "
      f"the state's median income: the CPS's lowest state (${sm['lowest']:,} for four in 2029) and its national median "
      f"(${sm['national']:,}) stand in for HHS's figures. 2029 law and prices throughout.\n")
    lab = {"single_parent_2": "Single parent, two children", "married_2": "Married couple, two children (one earner)",
           "single_adult": "Single adult"}
    A("| Family | Case | Highest rate (cents) | At % of poverty | Above 65 at | Result |\n| --- | --- | --- | --- | --- | --- |")
    for k, v in chk.items():
        for case, _ in CEILING_CASES:
            r = v[f"{case} | lowest-income state"]
            over = ", ".join(f"{x}%" for x in r["over"]) or "—"
            A(f"| {lab[k]} | {case} | {r['max']} | {r['at']}% | {over} | {'**meets**' if r['pass'] else '**fails**'} |")
    A("\nThe typical state gives the same highest rates: the charge starts above 300% of poverty there, and where it "
      "does reach these families (the lowest-income state, from about 240%), their rate is 26-32 cents from 2035 and "
      "39-46 cents in 2032-34 with the premium credit. Paid leave at "
      "its 1.10% ceiling adds 0.25 cents everywhere. Steps that cross SNAP's net income test (the single adult at 125% "
      "with the rent) are cliffs, not rates, and exist under current law.\n")
    sp = {r["pct_poverty"]: r for r in chk["single_parent_2"][CEILING_CASES[1][0] + " | lowest-income state"]["rows"]}
    r = sp[100]
    A(f"**Where it fails:** single parent at 100% of poverty, 2035 on, with the rent: payroll {r['payroll']}, income "
      f"tax {r['income_tax']} (the earned income credit's 21.06% phase-out plus the 10% bracket), SNAP {r['snap']} "
      f"(30% of a net income that rises by $1.20 a dollar once the shelter deduction shrinks), total **{r['total']}**. "
      "Two things push it past memo 7's arithmetic: SNAP's shelter interaction (36 cents, not 24), and FAM-1, which "
      "replaces the child credit whose nonrefundable part today offsets the 10% bracket at these incomes (+10 cents).\n")
    A("**What two fixes would cost** (2029, static, full take-up; for the lead's options, not decided):\n")
    A(f"- a nonrefundable family offset against income tax of $750 a child: about ${op['family_offset_750_bn']}B a "
      f"year (${op['family_offset_500_bn']}B at $500, which falls short at 125% of poverty). It removes the 10% "
      "bracket's 10 cents at 100-125%: from 2035 the shelter case comes to the ceiling exactly (65.0, so paid leave "
      "at its ceiling would tip it over), and the 2030-34 marketplace case to 55; with the rent in 2030-34 it is still "
      "67.1;")
    A(f"- SNAP's earned income deduction from 20% to 45%: up to about ${op['snap_earnings_deduction_45_bn_upper']}B a "
      "year on the CPS's annual earnings of SNAP households (an upper bound: SNAP counts monthly income only in months "
      "on SNAP, and the CPS records under half of SNAP). SNAP's rate falls to about 25 cents with the shelter "
      "deduction and 17 without; every case meets the ceiling except the married couple on the marketplace in "
      "2030-34 with the rent (65.9).\n")
    A("Only the two together clear every case. Neither is decided; the options are the lead's to put to Espen "
      "(INC-5.02's own rule is a review by the owning dossiers when a family type is above the ceiling for two years).\n")


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--ledger", required=True)
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    R = {}
    B25 = baseline(2025)
    R["baseline_2025"] = {"aggregates": aggregates(B25), "poverty": poverty_block(B25, True)}
    B0 = baseline(2029, snap_law=False)
    R["snap_law_2029"] = {"prior_law_poverty": poverty_block(B0)["model"]}
    B = baseline(2029)
    R["snap_law_2029"].update(B["snap_law"])
    H = B["households"]
    assign(H, "size_adjusted", n=10)
    deciles = average_rates(H, n=10)
    assign(H, "size_adjusted")
    from poverty import gap
    R["baseline_2029"] = {
        "law": {k: B["law"][k] for k in ("std", "ctc", "ctc_refundable", "eitc_earned", "ss_wage_base", "fpl")},
        "aggregates": aggregates(B), "poverty": poverty_block(B),
        "poverty_gap_bn": r1(gap(B["spm"]) / 1e9),
        "distribution_d3": {str(k): {kk: r1(vv) for kk, vv in v.items()} for k, v in average_rates(H).items()},
        "distribution_deciles": {str(k): {kk: r1(vv) for kk, vv in v.items()} for k, v in deciles.items()},
        "distribution_tpc": {str(k): {kk: r1(vv) for kk, vv in v.items()} for k, v in unit_distribution(B).items()},
    }
    R["families"] = {k: {"current": marginal_rates(f), "marketplace": marginal_rates(f, marketplace=True),
                         "shelter": marginal_rates(f, shelter=1400 * 1.107), "plan": marginal_rates(f, plan=True)}
                     for k, f in FAMILIES.items()}
    R["provisions"] = provision_runs(B, a.ledger)
    sm = state_medians(B)
    R["ceiling"] = {"state_median_income_4": sm, "check": ceiling_check(sm["lowest"], sm["national"]),
                    "options": ceiling_options(B)}
    R["secure_floor_rules"] = secure_floor_rules(B, a.ledger)
    os.makedirs(a.out, exist_ok=True)
    with open(os.path.join(a.out, "results.json"), "w") as f:
        json.dump(R, f, indent=1, sort_keys=True)
        f.write("\n")
    with open(os.path.join(a.out, "results.md"), "w") as f:
        f.write(markdown(R))
    print("household model: results written to", a.out)


if __name__ == "__main__":
    main()
