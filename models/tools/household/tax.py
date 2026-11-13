"""Federal income and payroll tax for one tax unit, under the law of `params.law(year)`.

Role: the household model's tax calculator (`MODEL-CARD.md`, "Rules modeled"). Status: working.

Covers the regular income tax (ordinary brackets and the 0/15/20% rates on gains and dividends), the standard
deduction with its additions at 65 and the 2025-2028 senior deduction, taxable Social Security (sec. 86), the net
investment income tax, the child tax credit with the credit for other dependents and the refundable part (ACTC), the
earned income credit, and payroll taxes (employee and employer halves, self-employment tax and the additional Medicare
tax). Not modeled (`MODEL-CARD.md`, "What it does not do"): itemized deductions, the AMT, the dependent care,
education, saver's and premium credits, the 2025-2028 tips, overtime and car-loan deductions (the CPS cannot see them),
and the ACTC's alternative formula for three or more children.
"""

def filing_status(u):
    """'joint', 'hoh' or 'single'. Census FILESTAT 1-3 are joint returns, 4 head of household, 5 single, 6 nonfiler."""
    fs = u["filestat"]
    if fs in (1, 2, 3) or u["age_s"] >= 0:
        return "joint"
    if fs == 4 or (fs == 6 and u["n_dep"] > 0):
        return "hoh"
    return "single"


def bracket_tax(income, edges, rates):
    tax, lo = 0.0, 0.0
    for edge, rate in zip(edges + [float("inf")], rates):
        if income <= lo:
            break
        tax += (min(income, edge) - lo) * rate
        lo = edge
    return tax


def payroll(wages, se, L, fs, other_wages=0.0):
    """Employee and employer payroll tax on one person's wages and self-employment earnings."""
    base = L["ss_wage_base"]
    ee = L["ss_rate"] * min(wages, base) + L["hi_rate"] * wages
    er = ee
    se_earn = max(se, 0) * 0.9235
    ss_room = max(base - wages, 0)
    se_tax = 2 * L["ss_rate"] * min(se_earn, ss_room) + 2 * L["hi_rate"] * se_earn
    return ee, er, se_tax, se_earn


def taxable_ss(ss, other_income, fs, L):
    if ss <= 0:
        return 0.0
    prov = other_income + 0.5 * ss
    b, a = L["ss_base"][fs], L["ss_adj_base"][fs]
    if prov <= b:
        return 0.0
    if prov <= a:
        return min(0.5 * ss, 0.5 * (prov - b))
    return min(0.85 * ss, 0.85 * (prov - a) + min(0.5 * ss, 0.5 * (a - b)))


def eitc(earned, agi, invest, n_kids, fs, ages, L):
    k = min(n_kids, 3)
    if k == 0:
        lo, hi = L["eitc_childless_ages"]
        if not any(lo <= a <= hi for a in ages if a >= 0):
            return 0.0
    if invest > L["eitc_invest_limit"]:
        return 0.0
    po_start = L["eitc_po_start"]["joint" if fs == "joint" else "single"][k]
    max_credit = L["eitc_rate"][k] * L["eitc_earned"][k]
    credit = min(L["eitc_rate"][k] * max(earned, 0), max_credit)
    credit -= L["eitc_po_rate"][k] * max(max(agi, earned) - po_start, 0)
    return max(credit, 0.0)


def unit_tax(u, L, refundable=True):
    """Taxes and credits for one tax unit (dollars a year). `u` holds the extract's fields, already uprated.

    `refundable=False` withholds refundable credits (the baseline's treatment of units the Census tax model marks as
    nonfilers, assumption A-6)."""
    fs = filing_status(u)
    ages = [u["age_h"], u["age_s"]]
    ee_h, er_h, se_h, sen_h = payroll(u["wage_h"], u["se_h"], L, fs)
    ee_s, er_s, se_s, sen_s = payroll(u["wage_s"], u["se_s"], L, fs)
    ee_d, er_d, _, _ = payroll(u["dep_wages"], 0, L, fs)
    wages = u["wage_h"] + u["wage_s"]
    se = u["se_h"] + u["se_s"]
    se_tax = se_h + se_s
    addl_hi = L["addl_hi_rate"] * max(wages + max(sen_h + sen_s, 0) - L["addl_hi_threshold"][fs], 0)
    invest = u["interest"] + u["dividends"] + u["capgain"] + max(u["rent"], 0)
    pre = (wages + se - 0.5 * se_tax + u["interest"] + u["dividends"] + max(u["rent"], -3000) + u["capgain"]
           + u["pension"] + u["disab_surv"] + u["uc"])
    tss = taxable_ss(u["ss"], pre, fs, L)
    agi = pre + tss
    n65 = sum(a >= 65 for a in ages)
    ded = L["std"][fs] + n65 * L["std_aged"][fs]
    if L["senior_deduction"] and n65:
        ded += max(n65 * L["senior_deduction"] - 0.06 * max(agi - L["senior_phaseout"][fs], 0), 0)
    ti = max(agi - ded, 0.0)
    pref = min(max(u["dividends"] + u["capgain"], 0), ti)
    ordinary = ti - pref
    tax = bracket_tax(ordinary, L["brackets"][fs], L["rates"])
    z, f = L["cg_brackets"][fs]
    at0 = max(min(z, ti) - ordinary, 0)
    at15 = max(min(f, ti) - max(ordinary, z), 0)
    tax += 0.15 * min(at15, pref - min(at0, pref)) + 0.20 * max(pref - at0 - at15, 0)
    niit = L["niit_rate"] * max(min(invest, agi - L["niit_threshold"][fs]), 0)
    # child tax credit and the credit for other dependents
    kids = u["n_dep_u6"] + u["n_dep_6_16"]
    others = u["n_dep"] - kids
    credit = kids * L["ctc"] + others * L["ctc_odc"]
    over = max(agi - L["ctc_phaseout"][fs], 0)
    credit = max(credit - L["ctc_phaseout_rate"] * (-(-over // 1000) * 1000), 0)
    nonref = min(credit, tax)
    earned = wages + se - 0.5 * se_tax
    actc = 0.0
    if refundable and kids:
        actc = min(credit - nonref, kids * L["ctc_refundable"],
                   L["ctc_refund_rate"] * max(earned - L["ctc_earn_floor"], 0))
        actc = max(actc, 0.0)
    e_kids = u["n_dep_u6"] + u["n_dep_6_16"] + u["n_dep_17"] + u["n_dep_18"] + u["n_dep_19_23_student"]
    e = eitc(earned, agi, invest, e_kids, fs, ages, L) if refundable else 0.0
    before = tax + niit
    income_tax = before - nonref - actc - e
    return {"fs": fs, "agi": agi, "taxable_income": ti, "tax_before_credits": before, "ctc_nonref": nonref,
            "actc": actc, "eitc": e, "ctc_total": nonref + actc, "income_tax": income_tax, "niit": niit,
            "fica_ee": ee_h + ee_s + ee_d + addl_hi, "fica_er": er_h + er_s + er_d, "se_tax": se_tax,
            "payroll": ee_h + ee_s + ee_d + addl_hi + er_h + er_s + er_d + se_tax}
