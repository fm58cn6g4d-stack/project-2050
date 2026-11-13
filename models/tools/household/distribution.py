"""Quintiles, deciles and the top 1%, and average tax rates, from the baseline household budget.

Role: the household model's distribution layer (`MODEL-CARD.md`, "Distribution conventions"). Status: working.

The D3 convention (the project's household fairness test): households ranked by expanded cash income adjusted for
household size (divided by the square root of the number of people), in groups with equal numbers of households, so a
per-household average is comparable with the legacy incidence model's. The benchmark conventions (`groups(...,
by="people")`) put equal numbers of people in each group, as CBO and the Tax Policy Center do.
"""


def assign(records, rank_key, weight_key="weight", n=5, by="units", people_key="numper"):
    """Sets record['g<n>'] to its group 1..n (and 'top1' for the top 1%) and returns the group cut points."""
    rs = sorted(records, key=lambda r: r[rank_key])
    w = [r[weight_key] * (r[people_key] if by == "people" else 1) for r in rs]
    total = sum(w)
    run = 0.0
    cuts = []
    for r, wi in zip(rs, w):
        mid = (run + wi / 2) / total
        g = min(int(mid * n) + 1, n)
        r[f"g{n}"] = g
        r["top1"] = mid >= 0.99
        if len(cuts) < g - 1:
            cuts.append(r[rank_key])
        run += wi
    return cuts


def table(records, fields, n=5, weight_key="weight"):
    """Weighted totals of `fields` by group, plus the top 1% ('T1') and all ('all')."""
    out = {g: {"weight": 0.0, **{f: 0.0 for f in fields}} for g in list(range(1, n + 1)) + ["T1", "all"]}
    for r in records:
        w = r[weight_key]
        for g in (r[f"g{n}"], "all") + (("T1",) if r["top1"] else ()):
            o = out[g]
            o["weight"] += w
            for f in fields:
                o[f] += w * r[f]
    return out


def average_rates(records, n=5, income="expanded"):
    """Average federal tax rates by group: individual income tax (after refundable credits) and payroll taxes
    (both halves), as shares of expanded cash income."""
    t = table(records, [income, "income_tax", "payroll"], n)
    res = {}
    for g, o in t.items():
        inc = o[income]
        res[g] = {"households_m": o["weight"] / 1e6,
                  "avg_income": inc / o["weight"] if o["weight"] else 0,
                  "income_tax_rate": 100 * o["income_tax"] / inc if inc else 0,
                  "payroll_rate": 100 * o["payroll"] / inc if inc else 0,
                  "share_income_tax": 100 * o["income_tax"] / t["all"]["income_tax"]}
        res[g]["federal_rate"] = res[g]["income_tax_rate"] + res[g]["payroll_rate"]
    return res
