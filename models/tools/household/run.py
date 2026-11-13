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
from families import FAMILIES, marginal_rates
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


def money(v):
    return ("+" if v >= 0 else "−") + f"${abs(v):,.0f}"


def markdown(R):
    o = []
    A = o.append
    A("# Household model: results\n")
    A("Generated by `models/tools/household/run.py` from the committed CPS extract, the budget model's ledger and the "
      "adopted incidence rows. Role: generated results of `MOD-household` (`MODEL-CARD.md`). Regenerate it; never edit "
      "it by hand. Status: working (part 1 of step M3).\n")
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
    return "\n".join(o) + "\n"


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--ledger", required=True)
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    R = {}
    B25 = baseline(2025)
    R["baseline_2025"] = {"aggregates": aggregates(B25), "poverty": poverty_block(B25, True)}
    B = baseline(2029)
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
    os.makedirs(a.out, exist_ok=True)
    with open(os.path.join(a.out, "results.json"), "w") as f:
        json.dump(R, f, indent=1, sort_keys=True)
        f.write("\n")
    with open(os.path.join(a.out, "results.md"), "w") as f:
        f.write(markdown(R))
    print("household model: results written to", a.out)


if __name__ == "__main__":
    main()
