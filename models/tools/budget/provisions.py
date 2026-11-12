#!/usr/bin/env python3
"""provisions.py: the provision scoring library (budget workflow piece B3).

Role: turns a provision spec (models/data/budget/provisions.csv, one per ledger row) into
year-by-year budget authority, outlays and receipts by category, FY2026-2056, in nominal
dollars, with real and share-of-GDP views. Status: current, not yet read by fiscal-model.py.
Until piece B6 the fiscal model keeps its own copy of the method (fiscal-model.py, row_path)
and its profiles (models/data/inputs/fiscal-profiles.csv); test_provisions.py proves the two
give the same paths, float for float, and that the specs' model fields equal the profiles.
Standard library only. Units: billions of nominal dollars by federal fiscal year.

  specs()                  the provision specs, {id: spec}, in file order
  score(spec, ledger)      one provision's Score: deficit effect (general-fund and unified bases),
                           outlays or receipts, budget authority, category, kind
  score_all(ledger_path)   every spec the fiscal model uses, {id: Score}
  by_category(scores)      unified-basis totals by category, {category: {year: billions}}
  views(values)            {"nominal", "real", "pct_gdp"} through data.py's two conversions

What the money is ("kind"), each with one scoring method:

  discretionary  Outlays: the row's calibrated profile path (below), which stays canonical.
                 Budget authority: an estimate that leads outlays. Spend-out shares are B2's
                 CBO-calibrated ones, used as stored (spendout-discretionary-cbo.csv,
                 ASM-SPENDOUT): the timing of OMB's FY1993-2019 history, with ground
                 transportation taken out of nondefense, scaled so that CBO's projected budget
                 authority gives CBO's projected outlays over FY2029-36 (within 1%). Each year's
                 budget authority is the outlays it pays for over its spend-out, the next four
                 years' outlays weighted by the shares, divided by the square of the shares' sum:
                 BA(t) = sum over k of share(k) x outlays(t+k) / S^2. Spending that budget
                 authority out at the same shares then gives back the row's lifetime outlays, so
                 the level is consistent in both directions, and a program whose outlays start in
                 FY2030 shows budget authority from FY2027. Year by year the spend-out does not
                 give back the model's outlays exactly: the model's profiles spend faster at the
                 start and stop faster at a time limit than these rates allow. spendout_gap()
                 measures the difference. (The exact inverse, the only budget authority that
                 reproduces the outlays exactly, oscillates by several times a year's outlays,
                 because outlays jump from zero in FY2030; it is not a usable reading.) Years
                 after FY2056 are extended at the row's FY2055-56 growth. The shares are history's
                 shape, not CBO's account rates, so every discretionary budget-authority figure is
                 marked rough.
                 Highway, transit and airport grants under obligation limitations have
                 discretionary outlays but mandatory budget authority (contract authority, which
                 CBO's baseline carries: cbo-contract-authority.csv). The nondefense shares are
                 fit without ground transportation and calibrated to CBO's outlays without the
                 accounts that have no discretionary budget authority, and those outlays are
                 carried on their own (cbo_discretionary_outlays()). No ledger row carries
                 contract authority: Moving America's renewal top-ups (MOV-29, MOV-30) are
                 general-fund appropriations in addition to the trust fund's own contract
                 authority, which stays within its receipts (Draft 2 sec. 110; decision A-14).
  mandatory      Outlays: the calibrated profile path. Budget authority equals outlays in the
                 same year, CBO's usual reading of benefits and tax credits, where the spec says
                 so (budget_authority = outlays). Where the spec says on_enactment (a multi-year
                 direct appropriation) or unknown, no budget-authority path is produced: the
                 repository does not say how much is provided when.
  revenue        Receipts: minus the calibrated profile path (the path is a deficit effect, so a
                 revenue gain is negative). No budget authority.
  transfer       An interest-neutral transfer: a self-funded program whose dedicated receipt
                 pays it, so it adds nothing to the unified deficit and carries no interest
                 (FAM-3 paid leave, CLI-2 the carbon dividend). Scored like mandatory spending on
                 the general-fund basis, zero on the unified basis.
  none           No direct budget effect (a statute or authorization whose ledger amount is 0).

The calibrated profile path (method "profile", the fiscal model's method since October 2026):
a ten-year amount from the ledger (trillions, FY2030-39) is spread over the years by the spec's
phase-in (start year, ramp years), its growth index (indexation), and its time limit (expiry);
it is scaled so its FY2030-39 sum equals the ledger amount exactly; after 2039 it continues at
a share (continues_after_2039) of the run rate, shrinking by fade a year. Other methods:
"years" (a year-by-year shape in fiscal-years.csv, scaled to the ledger amount), "components"
(a bill split into disjoint parts in fiscal-components.csv, each with its own spec, all in the
parent's category), "split" (one provision enacted through more than one vehicle, board 0d: each
part, a "part" row in provisions.csv, takes a share of the provision's amount from
provision-splits.csv and is scored in its own kind, category and vehicle, so a mandatory part in
reconciliation and a discretionary part in regular appropriations land on their own lines),
"climate"
(the climate package's exact annual accounts, climate-integration.py, added to the profile path
of the row's pre-package amount), "dynamic" (the DY rows' summed midpoints on one profile; only
scenario DEC-DYN uses it) and "not_scored" (rows the fiscal model leaves out).

Sign convention (ASM-SIGN): a positive deficit effect raises the deficit. Outlays and budget
authority are reported as positive spending; receipts as positive revenue.
"""
import csv, importlib.util, json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
TOOLS = os.path.normpath(os.path.join(HERE, ".."))
ROOT = os.path.normpath(os.path.join(HERE, "..", "..", ".."))
SPECS = os.path.join(ROOT, "models", "data", "budget", "provisions.csv")
SPLITS = os.path.join(ROOT, "models", "data", "budget", "provision-splits.csv")
sys.path.insert(0, HERE)
import data as D  # noqa: E402

Y0, Y1 = 2026, 2056          # model years (ASM-HORIZON)
W0, W1 = 2030, 2039          # the ledger's scoring window (ASM-WINDOW)
# Growth of price-indexed rows: one rounded CPI-U rate (ASM-CPI-PATH). It is the fiscal model's
# rounded path, kept so the paths reproduce; it is a growth index for indexation, not a deflator.
# Real-dollar views never use it: they go through data.to_real. B6 may swap it for B2's series.
CPI_RATE = {y: 2.26 if y <= 2036 else 2.3 for y in range(Y0, Y1 + 1)}
SS_FADE = 0.015              # SS-1's net saving shrinks 1.5% a year after 2039 (ASM-PROF-SS1)

KINDS = ("discretionary", "mandatory", "revenue", "transfer", "none")
VEHICLES = ("regular_appropriations", "supplemental_emergency", "advance_appropriation",
            "reconciliation", "regular_order", "none", "unknown")
METHODS = ("profile", "years", "components", "split", "climate", "dynamic", "not_scored")
BUDGET_AUTHORITY = ("spendout", "outlays", "on_enactment", "none", "unknown")
SPENDOUT_GROUPS = ("defense", "nondefense")
UNIFIED = ("same", "zero", "net_of_own_revenue")
COLUMNS = ["id", "table", "parent", "label", "in_model", "category", "kind", "vehicle",
           "vehicle_source", "appropriation", "budget_authority", "spendout_group", "method",
           "start", "ramp", "indexation", "indexation_basis", "expiry", "expiry_basis",
           "continues_after_2039", "fade", "unified", "asm_ids", "notes"]
UNKNOWN = "unknown"


# ---------------------------------------------------------------- specs

def _num(v):
    return int(v) if v.lstrip("-").isdigit() else float(v)


def specs(path=SPECS):
    """{id: spec} in file order. Numeric model fields are parsed as typed (2 stays an integer,
    0.3 a float), the way fiscal-profiles.py parses them, so the arithmetic matches."""
    out = {}
    with open(path, newline="") as f:
        rd = csv.DictReader(f)
        if rd.fieldnames != COLUMNS:
            raise ValueError("provisions.csv columns differ from provisions.COLUMNS")
        for r in rd:
            s = dict(r)
            for k in ("start", "ramp", "fade", "continues_after_2039"):
                s[k] = None if r[k] in ("", UNKNOWN) else _num(r[k])
            s["expiry_year"] = _num(r["expiry"]) if r["expiry"] not in ("", "none", UNKNOWN) else None
            s["asm_ids"] = r["asm_ids"].split()
            if s["id"] in out:
                raise ValueError("provisions.csv: %s listed twice" % s["id"])
            out[s["id"]] = s
    return out


def problems(S):
    """Format errors in the specs (also run by test_provisions.py)."""
    errs = []
    cats = {c["category"] for c in D.categories("baseline")}
    for i, s in S.items():
        def bad(msg):
            errs.append("%s: %s" % (i, msg))
        if s["kind"] not in KINDS:
            bad("kind %r" % s["kind"])
        if s["vehicle"] not in VEHICLES:
            bad("vehicle %r" % s["vehicle"])
        if s["method"] not in METHODS:
            bad("method %r" % s["method"])
        if s["budget_authority"] not in BUDGET_AUTHORITY:
            bad("budget_authority %r" % s["budget_authority"])
        if s["in_model"] not in ("yes", "no"):
            bad("in_model %r" % s["in_model"])
        if s["in_model"] == "yes" and s["method"] == "not_scored":
            bad("in the model but not scored")
        if s["method"] != "not_scored":
            if s["category"] not in cats:
                bad("category %r is not in categories.csv" % s["category"])
            if s["unified"] not in UNIFIED:
                bad("unified %r" % s["unified"])
            if s["method"] in ("profile", "years", "components", "dynamic") and s["indexation"] in ("", UNKNOWN):
                bad("a scored row needs its growth index")
        if s["budget_authority"] == "spendout" and s["spendout_group"] not in SPENDOUT_GROUPS:
            bad("spend-out needs spendout_group %s" % " or ".join(SPENDOUT_GROUPS))
        if s["kind"] == "revenue" and s["budget_authority"] not in ("none",):
            bad("revenue has no budget authority")
        if s["parent"] and s["parent"] not in S:
            bad("parent %s has no spec" % s["parent"])
        if s["table"] == "part" and S.get(s["parent"], {}).get("method") != "split":
            bad("a part's parent must have method split")
        for a in s["asm_ids"]:
            if not a.startswith("ASM-"):
                bad("asm_ids entry %r" % a)
    errs += split_problems(S)
    return errs


def split_problems(S, splits=None):
    """A split provision's parts must exist, be its own, and take shares that add to one."""
    splits = read_splits() if splits is None else splits
    errs = []
    for i, s in S.items():
        if s["method"] != "split":
            continue
        parts = splits.get(i, [])
        if not parts:
            errs.append("%s: method split but no parts in provision-splits.csv" % i)
            continue
        if abs(sum(sh for _, sh in parts) - 1.0) > 1e-9:
            errs.append("%s: part shares add to %.6f, not 1" % (i, sum(sh for _, sh in parts)))
        for pid, _ in parts:
            if pid not in S or S[pid]["table"] != "part" or S[pid]["parent"] != i:
                errs.append("%s: part %s has no part row in provisions.csv" % (i, pid))
            elif S[pid]["method"] in ("split", "components", "climate", "dynamic", "not_scored"):
                errs.append("%s: part %s must be scored by profile or years" % (i, pid))
            elif S[pid]["vehicle"] == "reconciliation" and S[pid]["kind"] == "discretionary":
                errs.append("%s: part %s is on reconciliation but discretionary; a split's parts must each fit their vehicle" % (i, pid))
    for parent in splits:
        if parent not in S or S[parent]["method"] != "split":
            errs.append("provision-splits.csv: %s is not a split provision" % parent)
    return errs


def read_splits(path=None):
    """{parent: [(part id, share of the parent's amount)]} from provision-splits.csv."""
    out, path = {}, path or SPLITS
    if not os.path.exists(path):
        return out
    with open(path, newline="") as f:
        for r in csv.DictReader(f):
            out.setdefault(r["parent"], []).append((r["part"], float(r["share"])))
    return out


def vehicle_flags(S):
    """Rows whose vehicle and kind disagree: reconciliation carries only direct spending and
    revenue, and annual appropriations carry discretionary money. Each is an open design choice
    (board 0d, answered November 8, 2026: weigh provision by provision; a program may split
    across vehicles with the split method), reported, not rebooked. [(id, message)]"""
    out = []
    for i, s in S.items():
        if s["in_model"] != "yes" or s["method"] == "split" or s["table"] == "part":
            continue
        if s["vehicle"] == "reconciliation" and s["kind"] == "discretionary":
            out.append((i, "on a reconciliation bill but booked as discretionary"))
        elif s["vehicle"] == "regular_appropriations" and s["kind"] == "mandatory":
            out.append((i, "in annual appropriations but booked as mandatory"))
    return out


def _profile(s):
    """The spec's model fields as the fiscal model's profile dict (only fields that are set)."""
    p = {}
    if s["start"] is not None:
        p["start"] = s["start"]
    if s["ramp"] is not None:
        p["ramp"] = s["ramp"]
    if s["indexation"] not in ("", UNKNOWN):
        p["grow"] = s["indexation"]
    if s["expiry_year"] is not None:
        p["end"] = s["expiry_year"]
    if s["continues_after_2039"] is not None:
        p["perm"] = s["continues_after_2039"]
    if s["fade"] is not None:
        p["fade"] = s["fade"]
    return p


# ---------------------------------------------------------------- inputs read, not owned

def baseline():
    """The adopted baseline from data.py, rounded as fiscal-baseline.csv stores it (three
    decimals), which is what the fiscal model's growth indexes read."""
    if "B" not in _cache:
        B = {}
        for y, r in D.adopted_baseline().items():
            B[y] = {k: (round(v, 3) if isinstance(v, float) else v) for k, v in r.items()}
        _cache["B"] = B
    return _cache["B"]


def _inputs(name):
    with open(os.path.join(ROOT, "models", "data", "inputs", name), newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def year_shapes():
    """{id: [ten FY2030-39 values]} from fiscal-years.csv (the canonical home of the shapes)."""
    return {r["id"]: [_num(r["y%d" % y]) for y in range(W0, W1 + 1)] for r in _inputs("fiscal-years.csv")}


def component_amounts():
    """{(owner, component): ten-year $T} from fiscal-components.csv (the canonical home)."""
    return {(r["owner"], r["component"]): _num(r["mid10"]) for r in _inputs("fiscal-components.csv")}


def climate():
    """climate-integration.py, the climate package's annual accounts (read, not changed)."""
    if "CL" not in _cache:
        if TOOLS not in sys.path:
            sys.path.insert(0, TOOLS)
        sp = importlib.util.spec_from_file_location("climate_integration_b3", os.path.join(TOOLS, "climate-integration.py"))
        m = importlib.util.module_from_spec(sp)
        sp.loader.exec_module(m)
        _cache["CL"] = m
    return _cache["CL"]


_cache = {}


def ledger_amounts(ledger_path):
    """Ten-year amounts ($T, FY2030-39) by spec id, from ledger.json, on the fiscal model's two
    bases. A deficit effect: costs positive, revenue and savings negative.
      bills: general fund = gf_mid; unified = net_mid for SS-1, 0 when the spec's unified rule
             is zero, otherwise gf_mid
      base revenue (in the base, general-fund channel): -mid on both bases
      options (cuts with a scored profile): -saves_tn on both bases
      dynamic: the sum of the DY midpoints, negated, under the id DYN"""
    L = json.load(open(ledger_path))
    S = specs()
    out = {}
    for b in L["bills"]:
        s = S.get(b["id"])
        gf = b["gf_mid"]
        uni = gf
        if s and s["unified"] == "net_of_own_revenue":
            uni = b["net_mid"]
        elif s and s["unified"] == "zero":
            uni = 0.0
        out[b["id"]] = (gf, uni)
    for r in L["revenue"]:
        out[r["id"]] = (-r["mid"], -r["mid"])
    for c in L["cuts"]:
        out[c["id"]] = (-c["saves_tn"], -c["saves_tn"])
    out["DYN"] = (-sum(d["mid"] for d in L["dynamic"]),) * 2
    return out


# ---------------------------------------------------------------- the methods

def growth_index(B, key):
    if key == "gdp":
        return {y: B[y]["gdp"] for y in B if y >= Y0}
    if key == "cpi":
        idx, v = {}, 100.0
        for y in range(Y0, Y1 + 1):
            if y > Y0:
                v *= 1 + CPI_RATE[y] / 100
            idx[y] = v
        return idx
    if key == "special_ss":
        return {y: B[y]["rev_payroll"] for y in B if y >= Y0}
    return {y: B[y][key] for y in B if y >= Y0}


def profile_path(B, mid10, prof):
    """The calibrated profile path: FY2030-39 sums to mid10 ($T); see the module docstring.
    The floating-point operations follow fiscal-model.py's row_path in the same order."""
    start, ramp = prof.get("start", W0), prof.get("ramp", 1)
    end, perm, fade = prof.get("end"), prof.get("perm", 1.0), prof.get("fade", 0.0)
    g = growth_index(B, prof.get("grow", "gdp"))
    raw = {}
    for y in range(Y0, Y1 + 1):
        ph = 0.0 if y < start else min(1.0, (y - start + 1) / ramp)
        if end and y > end:
            ph = 0.0
        raw[y] = ph * g[y] / g[W0]
    s = sum(raw[y] for y in range(W0, W1 + 1))
    scale = (mid10 * 1000 / s) if s else 0.0
    out = {}
    for y in range(Y0, Y1 + 1):
        if y < W0:
            out[y] = 0.0
        elif y <= W1:
            out[y] = raw[y] * scale
        elif prof.get("grow") == "special_ss":
            gg = growth_index(B, "gdp")
            out[y] = out[W1] * gg[y] / gg[W1] * (1 - SS_FADE) ** (y - W1)
        else:
            # As fiscal-model.py: a ramp running past 2039 keeps rising; an end year after 2039
            # closes a tail. Rows fully phased in by 2040 with no such end get ph = 1.0 exactly.
            ph = 0.0 if y < start else min(1.0, (y - start + 1) / ramp)
            if end and end > W1 and y > end:
                ph = 0.0
            out[y] = perm * scale * ph * (g[y] / g[W0]) * (1 - fade) ** (y - W1)
    return out


def years_path(B, mid10, shape, prof):
    """A year-by-year FY2030-39 shape scaled to mid10; after 2039 the 2039 level continues at
    the spec's share, growing with its index."""
    s = sum(shape)
    out = {y: 0.0 for y in range(Y0, Y1 + 1)}
    for i, y in enumerate(range(W0, W1 + 1)):
        out[y] = shape[i] * (mid10 * 1000 / s if s else 0)
    g = growth_index(B, prof.get("grow", "gdp"))
    for y in range(W1 + 1, Y1 + 1):
        out[y] = out[W1] * prof.get("perm", 1.0) * g[y] / g[W1]
    return out


def deficit_path(spec, mid10, S=None, B=None):
    """A spec's deficit effect by year (billions) for a ten-year amount mid10 ($T), before the
    climate accounts. Dispatches on the spec's method."""
    S = S or specs()
    B = B or baseline()
    m = spec["method"]
    if m == "components":
        parts = [c for c in S.values() if c["parent"] == spec["id"] and c["table"] == "component"]
        amt = component_amounts()
        amounts = [amt[(spec["id"], c["id"].split("/", 1)[1])] for c in parts]
        if abs(sum(amounts) - mid10) > 1e-9:
            raise ValueError("component amounts differ from the ledger: " + spec["id"])
        shapes = year_shapes()   # a component with a fiscal-years.csv row (key owner/component) takes its shape
        paths = [years_path(B, a, shapes[c["id"]], _profile(c)) if c["method"] == "years" else profile_path(B, a, _profile(c))
                 for a, c in zip(amounts, parts)]
        return {y: sum(p[y] for p in paths) for y in range(Y0, Y1 + 1)}
    if m == "split":
        paths = [deficit_path(S[pid], share * mid10, S, B) for pid, share in read_splits()[spec["id"]]]
        return {y: sum(p[y] for p in paths) for y in range(Y0, Y1 + 1)}
    if m == "years":
        return years_path(B, mid10, year_shapes()[spec["id"]], _profile(spec))
    if m in ("profile", "climate", "dynamic"):
        return profile_path(B, mid10, _profile(spec))
    raise ValueError("%s is not scored (method %s)" % (spec["id"], m))


def climate_path(spec, S=None, B=None):
    """Climate rows: the profile path of the row's pre-package amount (zero for new rows), plus
    the package's exact annual account. Same on both bases, as the fiscal model has it."""
    CL = climate()
    B = B or baseline()
    rid = spec["id"]
    base = (profile_path(B, CL.CONFIG["legacy_gf_tn"][rid], _profile(spec))
            if rid in CL.CONFIG["legacy_gf_tn"] else {y: 0 for y in range(Y0, Y1 + 1)})
    return {y: base[y] + CL.delta_rows(y)[rid] for y in range(Y0, Y1 + 1)}


def _spendout(group):
    """B2's CBO-calibrated discretionary spend-out shares for a group (defense or nondefense),
    year of spending 0-3, as stored in spendout-discretionary-cbo.csv (ASM-SPENDOUT)."""
    rows = sorted((r for r in D.table("spendout-discretionary-cbo") if r["group"] == group),
                  key=lambda r: int(r["year_of_spending"]))
    return [float(r["share"]) for r in rows]


def spendout_ba(outlays, group):
    """Budget authority by year, FY2026-2056, as described in the module docstring: the
    outlays each year's budget authority pays for over its spend-out, at a level that spends
    out to the same lifetime outlays. Outlays after FY2056 are extended at the FY2055-56 growth
    rate (or held flat, or zero, where that is undefined)."""
    s = _spendout(group)
    tot = sum(s)
    o = dict(outlays)
    g = o[Y1] / o[Y1 - 1] if o.get(Y1 - 1) else 1.0
    for y in range(Y1 + 1, Y1 + len(s)):
        o[y] = o[y - 1] * g
    return {y: sum(s[k] * o.get(y + k, 0.0) for k in range(len(s))) / tot ** 2 for y in range(Y0, Y1 + 1)}


def cbo_discretionary_outlays(group):
    """CBO's February 2026 discretionary outlays for a group, FY2029-2036, rebuilt the way this
    library reads discretionary money: B2's shares applied to CBO's projected discretionary
    budget authority (account file), plus, for nondefense, the outlays of accounts with no
    discretionary budget authority (highway, transit and airport grants above all), carried as
    outlays on their own. {year: (rebuilt, CBO's own)}. B4 benchmarks against it."""
    cat = group.capitalize()
    ba = D.cbo_spending("ba", "discretionary", cat)
    out = D.cbo_spending("outlays", "discretionary", cat)
    extra = D.cbo_spending("outlays_without_ba", "discretionary", cat) if group == "nondefense" else {}
    back = spendout_apply(ba, group)
    return {y: (back[y] + extra.get(y, 0.0), out[y]) for y in range(2029, 2037)}


def spendout_gap(ba, outlays, group, years=range(W0, W1 + 1)):
    """{year: outlays from spending out ba at the group's shares, less the model's outlays}."""
    back = spendout_apply(ba, group)
    return {y: back[y] - outlays[y] for y in years}


def spendout_apply(ba, group):
    """Outlays by year from budget authority at the group's shares (the forward check)."""
    s = _spendout(group)
    return {y: sum(s[k] * ba.get(y - k, 0.0) for k in range(len(s))) for y in sorted(ba)}


class Score(dict):
    """id, category, kind, gf and unified deficit effects, and the budget-concept paths:
    outlays (spending kinds), receipts (revenue), budget_authority (or None where unknown), split
    into ba_mandatory and ba_discretionary (None where that type has none), and
    budget_authority_rough (True for every spend-out figure)."""


def score(spec, amounts, S=None, B=None):
    """Score one spec. amounts is ledger_amounts(...) (or {id: (gf $T, unified $T)})."""
    S = S or specs()
    B = B or baseline()
    i = spec["id"]
    if spec["method"] == "split":
        a_gf, a_uni = amounts[i]
        parts = [score(S[pid], {pid: (share * a_gf, share * a_uni)}, S, B) for pid, share in read_splits()[i]]
        out = Score(id=i, category="split", kind="split", parts=parts, budget_authority_rough=any(p["budget_authority_rough"] for p in parts))
        for k in ("gf", "unified", "outlays", "receipts", "budget_authority", "ba_mandatory", "ba_discretionary"):
            have = [p[k] for p in parts if p[k] is not None]
            out[k] = {y: sum(h[y] for h in have) for y in range(Y0, Y1 + 1)} if have else None
        return out
    if spec["method"] == "climate":
        gf = climate_path(spec, S, B)
        uni = dict(gf)
    else:
        a_gf, a_uni = amounts["DYN" if spec["method"] == "dynamic" else i]
        gf = deficit_path(spec, a_gf, S, B)
        uni = deficit_path(spec, a_uni, S, B)
    out = Score(id=i, category=spec["category"], kind=spec["kind"], gf=gf, unified=uni,
                outlays=None, receipts=None, budget_authority=None, budget_authority_rough=False,
                ba_mandatory=None, ba_discretionary=None)
    if spec["kind"] == "revenue":
        out["receipts"] = {y: -v for y, v in uni.items()}
    elif spec["kind"] in ("discretionary", "mandatory", "transfer"):
        out["outlays"] = dict(uni if spec["kind"] != "transfer" else gf)
        if spec["budget_authority"] == "spendout":
            out["ba_discretionary"] = spendout_ba(out["outlays"], spec["spendout_group"])
            out["budget_authority_rough"] = True
        elif spec["budget_authority"] == "outlays":
            out["ba_mandatory"] = dict(out["outlays"])
        parts = [p for p in (out["ba_mandatory"], out["ba_discretionary"]) if p is not None]
        if parts:
            out["budget_authority"] = {y: sum(p[y] for p in parts) for y in range(Y0, Y1 + 1)}
    return out


def score_all(ledger_path):
    """Every spec the fiscal model uses, {id: Score}. Components are scored inside their parent;
    the dynamic rows once, as DYN (their spec rows share it)."""
    S, B = specs(), baseline()
    amounts = ledger_amounts(ledger_path)
    out = {}
    for i, s in S.items():
        if s["in_model"] != "yes" or s["table"] in ("component", "part"):
            continue
        if s["method"] == "dynamic":
            if "DYN" not in out:
                out["DYN"] = score(dict(s, id="DYN"), amounts, S, B)
            continue
        out[i] = score(s, amounts, S, B)
    return out


def by_category(scores, basis="unified", ids=None):
    """{category: {year: billions}}: deficit effects summed by category (dynamic left out unless
    asked for by id)."""
    out = {}
    for i, sc in scores.items():
        if (ids is None and i == "DYN") or (ids is not None and i not in ids):
            continue
        for part in sc.get("parts") or [sc]:
            tgt = out.setdefault(part["category"], {y: 0.0 for y in range(Y0, Y1 + 1)})
            for y, v in part[basis].items():
                tgt[y] += v
    return out


def views(values, base_year=D.DEFAULT_BASE_YEAR, index=D.DEFAULT_INDEX):
    """Nominal, real (data.to_real) and share-of-GDP (data.to_pct_gdp) views of one path."""
    return {"nominal": dict(values), "real": D.to_real(values, base_year, index),
            "pct_gdp": D.to_pct_gdp(values)}


def window_total(path):
    """FY2030-39 sum, $T."""
    return sum(path[y] for y in range(W0, W1 + 1)) / 1000


# ---------------------------------------------------------------- each bill in its own CBO window

# Budget choice 3 (DEC-2026-11-08-05; ASM-BILL-WINDOW): each bill is also scored over its own CBO
# window, its budget resolution's year plus nine. The reconciliation bills' resolutions are the
# ledger's rail names; a regular-order bill or an appropriation is scored from the fiscal year its
# ledger target date falls in. Later-Congress rows (T2, LATER) have no window yet.
RAIL_FIRST_YEAR = {"R1": 2029, "R2": 2030, "R3": 2031}
SEASON_MONTH = {"spring": 4, "summer": 7, "fall": 10, "autumn": 10, "winter": 1}   # ledger targets like "2029-summer"
FY2029_FILE = os.path.join(ROOT, "models", "data", "inputs", "fiscal-fy2029.csv")


def fy2029_rows(path=FY2029_FILE):
    """{id: (amount or None, treatment)} from fiscal-fy2029.csv (the FY2029 line, ASM-FY2029-LINE)."""
    with open(path) as f:
        return {r["id"]: (float(r["fy2029_bn"]) if r["fy2029_bn"].strip() else None, r["treatment"]) for r in csv.DictReader(f)}


def first_year(bill):
    """A bill's first CBO window year, or None for a later Congress."""
    if bill["rail"] in RAIL_FIRST_YEAR:
        return RAIL_FIRST_YEAR[bill["rail"]]
    if bill["rail"] in ("FLOOR", "APPROPS"):
        y, m = bill["target"].split("-")[:2]
        m = SEASON_MONTH.get(m) or int(m)
        return int(y) + 1 if m >= 10 else int(y)
    return None


def bill_windows(scores, ledger_path, fy2029=None):
    """Each bill's deficit effect over its own CBO window (unified basis, $B, no interest on the
    bill's own borrowing, as CBO scores leave it out), from the same annual series as every
    other reading, with the priced FY2029 line added where the window reaches FY2029. Returns
    {id: dict(rail, first, window, out_years, fy2029)}: window is the ten-year sum; out_years
    the sum of the ten years after it (the Byrd rule's out-year test looks there); fy2029
    'priced', 'unpriced' or ''."""
    L = json.load(open(ledger_path))
    F = fy2029_rows() if fy2029 is None else fy2029
    out = {}
    for b in L["bills"]:
        sc = scores.get(b["id"])
        y0 = first_year(b)
        if sc is None or y0 is None:
            continue
        path = dict(sc["unified"])
        amt, treat = F.get(b["id"], (None, ""))
        if amt is not None:
            path[2029] = path.get(2029, 0.0) + amt
            if treat == "shift_from_2030":
                path[2030] -= amt
        win = range(y0, y0 + 10)
        out[b["id"]] = dict(rail=b["rail"], first=y0, window=sum(path.get(y, 0.0) for y in win),
                            out_years=sum(path.get(y, 0.0) for y in range(y0 + 10, min(y0 + 20, Y1 + 1))),
                            fy2029="" if b["id"] not in F else ("priced" if amt is not None else "unpriced"))
    return out


if __name__ == "__main__":
    import argparse
    ap = argparse.ArgumentParser(description="Score every provision spec and print FY2030-39 totals.")
    ap.add_argument("--ledger", default=os.path.join(ROOT, "build", "ledger.json"))
    a = ap.parse_args()
    for i, sc in score_all(a.ledger).items():
        ba = sc["budget_authority"]
        print("%-10s %-14s %-20s unified %8.3f T  BA %s" % (
            i, sc["kind"], sc["category"], window_total(sc["unified"]),
            ("n/a" if sc["kind"] == "revenue" else "unknown") if ba is None else "%8.3f T%s" % (window_total(ba), " (rough)" if sc["budget_authority_rough"] else "")))
