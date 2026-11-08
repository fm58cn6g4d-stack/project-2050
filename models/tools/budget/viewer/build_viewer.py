#!/usr/bin/env python3
"""build_viewer.py: writes the fiscal viewer, one self-contained HTML page.

Role: piece B5 of the federal budget model workflow (models/tools/budget/WORKFLOW.md), first version.
Status: current. Standard library only; reads the generated files, holds no numbers of its own.

Reads (all at build time):
  fiscal-model.json   the fiscal model's output (scenarios, D4 tests, composition); run-all.sh
                      writes it to build/. Without --model this script regenerates it in a temp dir.
  models/data/budget/ through data.py, the only place nominal -> real and nominal -> % of GDP happen
  models/data/budget/assumptions.csv   the ASM- register
  viewer/snapshot.json   the headline figures the page showed last time ("what changed")
Writes: --out (the page) and --snapshot-out (the updated snapshot). run-all.sh compares both
with the committed copies (the drift check).

Every figure printed in the page's text goes through Figures.n(), which keeps a record of the
printed text, the raw value and the source path. test_viewer.py re-reads each source and checks.
"""
import argparse, csv, html, json, os, re, shutil, subprocess, sys, tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, "..", "..", "..", ".."))
sys.path.insert(0, os.path.join(HERE, ".."))
import data  # noqa: E402  (models/tools/budget/data.py)

SNAPSHOT = os.path.join(HERE, "snapshot.json")
MODEL_TOOLS = os.path.join(ROOT, "models", "tools")
ASSUMPTIONS = os.path.join(ROOT, "models", "data", "budget", "assumptions.csv")
BASELINE_CSV = os.path.join(ROOT, "models", "data", "fiscal-baseline.csv")

METRICS = [  # key in the model's per-year rows, label, what it is
    ("deficit", "Deficit", "Spending minus revenue, in the fiscal year"),
    ("debt", "Debt held by the public", "Federal debt owed to the public at the end of the fiscal year"),
    ("interest", "Net interest", "Interest the government pays on its debt, net of what it earns"),
    ("rev", "Revenue", "All federal revenue"),
    ("out", "Spending", "All federal spending, interest included"),
]
UNITS = [("nominal", "Nominal dollars"), ("real", "Real dollars"), ("pct", "% of GDP")]
# Scenario colours: fixed slots, in the model's order (never cycled). The baseline is the ink colour.
SLOTS = {"BASE": "ink", "GROSS": 1, "PB": 2, "PB+S": 3, "DEC": 4, "DEC+ENV": 5, "DEC-DYN": 6,
         "DEC-R1": 7, "DEC+TRIMS": "grey", "BASE-R1": "inkdash"}
DEFAULT_ON = ["BASE", "DEC"]
# An assumption "drives what is on screen" when the code or file it lives in feeds the page.
DRIVES = re.compile(r"fiscal-(data|model|profiles|years|components)|fiscal-baseline|climate-integration|"
                    r"budget/data\.py|deflators|ledger-bills|ledger-build")


# ---------------------------------------------------------------- figures and their sources
class Figures:
    """Prints numbers and remembers where each came from (checked by test_viewer.py)."""
    def __init__(self):
        self.records = []

    def n(self, raw, src, kind="pct1"):
        """Format raw and record it. src is 'model:<dotted path>', 'baseline:<year>:<column>',
        'snapshot:<key>', 'count' or 'year'."""
        text = fmt(raw, kind)
        self.records.append({"text": text, "raw": raw, "src": src, "kind": kind})
        return text


def fmt(v, kind):
    if v is None:
        return "n/a"
    s = {"pct1": "%.1f", "pct2": "%.2f", "tn2": "%.2f", "int": "%d"}[kind] % v
    s = s.replace("-", "−")
    if s.startswith("−") and float(s[1:] or 0) == 0:
        s = s[1:]
    return s


def esc(s):
    return html.escape(str(s), quote=True)


# ---------------------------------------------------------------- the model file
def generate_model(tmp):
    """Rebuild fiscal-model.json the way run-all.sh does (steps 0, 1 and 6), in tmp."""
    for f in ("ledger-build.py", "inputs.py", "fiscal-profiles.py", "fiscal-model.py", "climate-integration.py"):
        shutil.copy(os.path.join(MODEL_TOOLS, f), tmp)
    env = dict(os.environ, P2050_INPUTS=os.path.join(ROOT, "models", "data", "inputs"))
    run = lambda *a: subprocess.run(a, cwd=tmp, env=env, check=True, stdout=subprocess.DEVNULL)
    run(sys.executable, os.path.join(MODEL_TOOLS, "transportation", "report.py"), "--json",
        os.path.join(tmp, "moving-america.json"))
    run(sys.executable, "ledger-build.py")
    run(sys.executable, "fiscal-model.py", "--baseline", BASELINE_CSV)
    return os.path.join(tmp, "fiscal-model.json")


def load_model(path):
    if path:
        return json.load(open(path))
    with tempfile.TemporaryDirectory() as tmp:
        return json.load(open(generate_model(tmp)))


# ---------------------------------------------------------------- data for the charts
def chart_data(M):
    """{unit: {metric: {scenario: [values by year]}}}, years list. Nominal comes from the model;
    real and % of GDP only from data.to_real and data.to_pct_gdp."""
    R = M["results"]
    years = sorted(int(y) for y in R["BASE"]["years"])
    out = {u: {m[0]: {} for m in METRICS} for u, _ in UNITS}
    for sid, r in R.items():
        for key, _, _ in METRICS:
            nom = {y: r["years"][str(y)][key] for y in years}
            for unit, conv in (("nominal", lambda v: v), ("real", data.to_real), ("pct", data.to_pct_gdp)):
                out[unit][key][sid] = [round(conv(nom)[y], 3) for y in years]
    return years, out


def category_data(years):
    """Baseline by category from the data layer: {unit: {category: [values]}}, plus the labels."""
    cats = [c for c in data.categories("baseline")]
    base = data.adopted_baseline()
    out = {u: {} for u, _ in UNITS}
    for c in cats:
        nom = {y: base[y][c["category"]] for y in years}
        out["nominal"][c["category"]] = [round(nom[y], 3) for y in years]
        out["real"][c["category"]] = [round(data.to_real(nom)[y], 3) for y in years]
        out["pct"][c["category"]] = [round(data.to_pct_gdp(nom)[y], 3) for y in years]
    return cats, out


# ---------------------------------------------------------------- snapshot (what changed)
def headline(M, F=None):
    """The small set of figures the page compares with last time: {key: {label, value, kind}}."""
    R, h = M["results"], {}
    ty = sorted(R["DEC"]["tests"]["prog_debt_pct"], key=int)   # the model's own report years
    HY = (ty[1], ty[-1])
    for sid, r in R.items():
        Y = r["years"]
        for y in HY:
            h["%s.debt_pct.%s" % (sid, y)] = dict(label="%s: debt held by the public, %% of GDP, FY%s" % (sid, y),
                                                  value=round(Y[y]["debt_pct"], 1), kind="pct1")
        h["%s.interest_pct.%s" % (sid, HY[1])] = dict(label="%s: net interest, %% of GDP, FY%s" % (sid, HY[1]),
                                               value=round(Y[HY[1]]["interest_pct"], 1), kind="pct1")
        h["%s.fiscal_gap" % sid] = dict(label="%s: fiscal gap, %% of GDP (hold the 2029 debt ratio)" % sid,
                                        value=round(r["fiscal_gap_hold_2029"], 2), kind="pct2")
        if r.get("tests"):
            t = r["tests"]
            h["%s.gf_worst" % sid] = dict(label="%s: D4 test 1, general-fund balance in its worst year, %% of GDP" % sid,
                                          value=round(t["gf_worst_2040_56_pct"], 2), kind="pct2")
            h["%s.maturity_pass" % sid] = dict(label="%s: D4 test 1 (paid for at maturity)" % sid,
                                               value="passes" if t["maturity_pass"] else "fails", kind="text")
            h["%s.envelope_room" % sid] = dict(label="%s: D4 test 2, envelope room left, $T" % sid,
                                               value=round(t["envelope_room"], 2), kind="tn2")
    return h


def load_snapshot():
    if os.path.exists(SNAPSHOT):
        return json.load(open(SNAPSHOT))
    return None


def fmt_head(item, which="value"):
    v = item[which]
    if item["kind"] == "text":
        return v
    return fmt(v, item["kind"])


def reference_and_snapshot(current, snap):
    """The figures to compare with, and the snapshot to write. Idempotent: once the snapshot
    holds the current figures, the comparison is with the figures before them."""
    if snap is None:
        return None, {"figures": current, "previous": None}
    if snap["figures"] != current:
        return snap["figures"], {"figures": current, "previous": snap["figures"]}
    return snap["previous"], snap


# ---------------------------------------------------------------- page sections
def scen_name(M, sid):
    return M["results"][sid]["label"]


def section_scenarios(M, F):
    R = M["results"]
    ty = sorted(R["DEC"]["tests"]["prog_debt_pct"], key=int)   # the model's own test years
    head = "".join("<th>Debt, FY%s, %% of GDP</th>" % esc(y) for y in ty)
    rows = []
    for sid, r in R.items():
        cells = "".join('<td class="num">%s</td>' % F.n(r["years"][y]["debt_pct"], "model:results.%s.years.%s.debt_pct" % (sid, y)) for y in ty)
        ni = F.n(r["years"][ty[-1]]["interest_pct"], "model:results.%s.years.%s.interest_pct" % (sid, ty[-1]))
        gap = F.n(r["fiscal_gap_hold_2029"], "model:results.%s.fiscal_gap_hold_2029" % sid, "pct2")
        rows.append('<tr><th scope="row"><span class="tag" data-sid="%s">%s</span> <span data-quoted>%s</span></th>%s'
                    '<td class="num">%s</td><td class="num">%s</td></tr>' % (esc(sid), esc(sid), esc(r["label"]), cells, ni, gap))
    return ('<div class="tablewrap"><table><thead><tr><th>Scenario</th>%s<th>Net interest, FY%s, %% of GDP</th>'
            '<th>Fiscal gap, %% of GDP</th></tr></thead><tbody>%s</tbody></table></div>' % (head, F.n(int(ty[-1]), "year", "int"), "".join(rows)))


def section_d4(M, F):
    R = M["results"]
    ids = [s for s in ("PB+S", "DEC", "DEC+ENV", "DEC-DYN", "DEC-R1", "DEC+TRIMS") if R[s].get("tests")]
    mp = lambda sid, k, f="pct2": F.n(R[sid]["tests"][k], "model:results.%s.tests.%s" % (sid, k), f)
    verdict = lambda ok: '<span class="%s">%s</span>' % ("ok" if ok else "bad", "passes" if ok else "fails")
    def row(label, fn):
        return "<tr><th scope=\"row\">%s</th>%s</tr>" % (label, "".join("<td>%s</td>" % fn(s) for s in ids))
    def mpath(sid, k, y):
        return F.n(R[sid]["tests"][k][y], "model:results.%s.tests.%s.%s" % (sid, k, y), "pct1")
    my = sorted(R["DEC"]["tests"]["margin_pts"], key=int)
    rows = [
        row("D4-1. Paid for at maturity: general-fund balance in the first test year, % of GDP (at or below zero passes)",
            lambda s: mp(s, "gf_2040_pct")),
        row("&hellip; worst year from then to the end of the horizon (the test)",
            lambda s: "%s %s" % (mp(s, "gf_worst_2040_56_pct"), verdict(R[s]["tests"]["maturity_pass"]))),
        row("D4-2. Investment envelope over the ten-year window, $T: room / held by accepted borrowing lines / left (no pass mark is set)",
            lambda s: "%s / %s / %s" % (mp(s, "envelope_10yr", "tn2"), mp(s, "envelope_used", "tn2"), mp(s, "envelope_room", "tn2"))),
        row("D4-3a. Total debt below the baseline every year",
            lambda s: verdict(R[s]["tests"]["below_baseline_every_year"])),
        row("D4-3b. Points of GDP below the baseline: " + " / ".join("FY" + y for y in my) + " (widening passes)",
            lambda s: "%s %s" % (" / ".join(mpath(s, "margin_pts", y) for y in my), verdict(R[s]["tests"]["margin_widening"]))),
        row("D4-3c. Net interest % of GDP, program vs baseline: " + " / ".join("FY" + y for y in my),
            lambda s: "%s vs %s %s" % (" / ".join(mpath(s, "interest_pct", y) for y in my),
                                      " / ".join(mpath(s, "base_interest_pct", y) for y in my),
                                      verdict(R[s]["tests"]["interest_below_baseline"]))),
        row("Ten-year general-fund primary deficit, $T (information)", lambda s: mp(s, "gf_10yr_primary", "tn2")),
    ]
    head = "".join('<th scope="col"><span class="tag" data-sid="%s">%s</span></th>' % (esc(s), esc(s)) for s in ids)
    d4 = ('<div class="tablewrap"><table class="d4"><thead><tr><th>Test</th>%s</tr></thead><tbody>%s</tbody></table></div>' % (head, "".join(rows)))
    # general fund beside unified
    gy = sorted(R["DEC"]["tests"]["gf_debt_pct"], key=int)
    grows = []
    for sid in ("PB+S", "DEC", "DEC+ENV", "DEC+TRIMS"):
        t = R[sid]["tests"]
        gf = "".join('<td class="num">%s</td>' % F.n(t["gf_debt_pct"][y], "model:results.%s.tests.gf_debt_pct.%s" % (sid, y)) for y in gy)
        un = "".join('<td class="num">%s</td>' % F.n(t["prog_debt_pct"][y], "model:results.%s.tests.prog_debt_pct.%s" % (sid, y)) for y in gy)
        grows.append('<tr><th scope="row"><span class="tag" data-sid="%s">%s</span></th>%s<td class="sep"></td>%s</tr>' % (esc(sid), esc(sid), gf, un))
    yh = "".join("<th>FY%s</th>" % y for y in gy)
    gfu = ('<div class="tablewrap"><table><thead><tr><th rowspan="2">Scenario</th>'
           '<th colspan="%d">General-fund reading</th><th></th><th colspan="%d">Unified reading (what the guardrails use)</th></tr>'
           '<tr>%s<th></th>%s</tr></thead><tbody>%s</tbody></table></div>' % (len(gy), len(gy), yh, yh, "".join(grows)))
    # interest stress
    srows = []
    for sid, base in (("DEC", "BASE"), ("DEC-R1", "BASE-R1")):
        t, Y = R[sid]["tests"], R[sid]["years"]
        deb = "".join('<td class="num">%s</td>' % F.n(Y[y]["debt_pct"], "model:results.%s.years.%s.debt_pct" % (sid, y)) for y in my)
        bdeb = "".join('<td class="num">%s</td>' % F.n(R[base]["years"][y]["debt_pct"], "model:results.%s.years.%s.debt_pct" % (base, y)) for y in my)
        mar = "".join('<td class="num">%s</td>' % mpath(sid, "margin_pts", y) for y in my)
        i56 = F.n(Y[my[-1]]["interest_pct"], "model:results.%s.years.%s.interest_pct" % (sid, my[-1]))
        b56 = F.n(R[base]["years"][my[-1]]["interest_pct"], "model:results.%s.years.%s.interest_pct" % (base, my[-1]))
        srows.append('<tr><th scope="row"><span class="tag" data-sid="%s">%s</span> <span data-quoted>%s</span></th>%s%s%s'
                     '<td class="num">%s</td><td class="num">%s</td></tr>' % (esc(sid), esc(sid), esc(R[sid]["label"]), deb, bdeb, mar, i56, b56))
    yh2 = "".join("<th>FY%s</th>" % y for y in my)
    stress = ('<div class="tablewrap"><table><thead><tr><th rowspan="2">Case</th><th colspan="%d">Program debt, %% of GDP</th>'
              '<th colspan="%d">Baseline debt, same rates</th><th colspan="%d">Points below baseline</th>'
              '<th rowspan="2">Program net interest, last year shown</th><th rowspan="2">Baseline net interest, last year shown</th></tr>'
              '<tr>%s%s%s</tr></thead><tbody>%s</tbody></table></div>' % (len(my), len(my), len(my), yh2, yh2, yh2, "".join(srows)))
    return d4, gfu, stress


def section_categories(M, cats, F):
    """Baseline vs decided program by category, % of GDP, from the model's composition block."""
    comp = M["composition"]
    ys = sorted(comp["BASE"], key=int)
    head = "".join('<th colspan="3">FY%s</th>' % y for y in ys)
    sub = "".join("<th>Base</th><th>Decided</th><th>Diff</th>" for _ in ys)
    rows = []
    for c in cats:
        k = c["category"]
        if k not in comp["BASE"][ys[0]]:
            continue
        cells = ""
        for y in ys:
            b, d = comp["BASE"][y][k], comp["DEC"][y][k]
            cells += '<td class="num">%s</td><td class="num">%s</td><td class="num">%s</td>' % (
                F.n(b, "model:composition.BASE.%s.%s" % (y, k), "pct1"), F.n(d, "model:composition.DEC.%s.%s" % (y, k), "pct1"),
                F.n(d - b, "diff:composition.%s.%s" % (y, k), "pct1"))
        rows.append('<tr><th scope="row" data-quoted>%s</th>%s</tr>' % (esc(c["label"]), cells))
    return ('<div class="tablewrap"><table class="cat"><thead><tr><th rowspan="2">Category (%% of GDP)</th>%s</tr><tr>%s</tr></thead>'
            "<tbody>%s</tbody></table></div>" % (head, sub, "".join(rows)))


def section_assumptions(F):
    rows = list(csv.DictReader(open(ASSUMPTIONS, newline="")))
    shown = [r for r in rows if DRIVES.search(r["where"])]
    out = []
    for r in shown:
        d = r["decided_by"]
        if d.startswith("unrecorded"):
            flag, cls = "No recorded decision", "warn"
        elif d.startswith("Proposed"):
            flag, cls = "Proposed, not yet decided", "warn"
        else:
            flag, cls = "Decided", "good"
        out.append(
            '<details id="%s" class="asm %s"><summary><span class="flag %s">%s</span> <code>%s</code> '
            '<span data-quoted>%s</span></summary><dl>'
            '<dt>Value</dt><dd data-quoted>%s</dd><dt>Source</dt><dd data-quoted>%s</dd>'
            '<dt>Who decided</dt><dd data-quoted>%s</dd><dt>Why it matters</dt><dd data-quoted>%s</dd>'
            '<dt>Where in the code or data</dt><dd data-quoted><code>%s</code></dd></dl></details>' % (
                esc(r["id"]), cls, cls, flag, esc(r["id"]), esc(r["label"]), esc(r["value"]), esc(r["source"]),
                esc(d), esc(r["matters"]), esc(r["where"])))
    n_un = sum(1 for r in shown if r["decided_by"].startswith(("unrecorded", "Proposed")))
    summary = "%s of the %s assumptions behind this page have no recorded decision, or are only proposed." % (
        F.n(n_un, "count:assumptions-flagged", "int"), F.n(len(shown), "count:assumptions-shown", "int"))
    return summary, "".join(out), shown


def section_changes(current, reference, F, M):
    if reference is None:
        return "<p>This is the first build, so there is nothing to compare with yet. The next run will list any figure it moves.</p>"
    items = []
    for k, cur in current.items():
        old = reference.get(k)
        if old is None:
            items.append("<li><span data-quoted>%s</span>: new, now %s</li>" % (esc(cur["label"]), F.n_text(fmt_head(cur), "snapshot:%s" % k, cur["value"], cur["kind"])))
        elif old["value"] != cur["value"]:
            items.append('<li><span data-quoted>%s</span>: %s &rarr; %s</li>' % (
                esc(cur["label"]), F.n_text(fmt_head(old), "snapshot-prev:%s" % k, old["value"], old["kind"]),
                F.n_text(fmt_head(cur), "snapshot:%s" % k, cur["value"], cur["kind"])))
    for k, old in reference.items():
        if k not in current:
            items.append("<li><span data-quoted>%s</span>: no longer produced</li>" % esc(old["label"]))
    if not items:
        return "<p>Nothing moved. Every headline figure matches the last run.</p>"
    return "<p>These headline figures differ from the last run:</p><ul>%s</ul>" % "".join(items)


def _n_text(self, text, src, raw, kind):
    self.records.append({"text": text, "raw": raw, "src": src, "kind": kind})
    return text


Figures.n_text = _n_text


# ---------------------------------------------------------------- the page
def build(model_path=None, reference_snapshot=None):
    """Returns (html text, new snapshot dict, figures records)."""
    M = load_model(model_path)
    F = Figures()
    years, series = chart_data(M)
    cats, catseries = category_data(years)
    current = headline(M)
    snap = reference_snapshot if reference_snapshot is not False else None
    reference, new_snap = reference_and_snapshot(current, snap)
    deflator_name = {"gdp_price_index": "GDP price index", "cpiu": "consumer price index (CPI-U)"}[data.DEFAULT_INDEX]
    scen = [{"id": sid, "label": r["label"], "slot": SLOTS.get(sid, "grey"), "on": sid in DEFAULT_ON} for sid, r in M["results"].items()]
    payload = {"years": years, "scenarios": scen, "metrics": [{"key": k, "label": l, "note": n} for k, l, n in METRICS],
               "units": [{"key": k, "label": l} for k, l in UNITS], "series": series,
               "categories": [{"key": c["category"], "label": c["label"], "kind": c["kind"]} for c in cats],
               "catseries": catseries, "base_year": data.DEFAULT_BASE_YEAR, "deflator": deflator_name,
               "gdp_note": "Share of GDP uses the adopted baseline's GDP in every case."}
    d4, gfu, stress = section_d4(M, F)
    asm_summary, asm_html, shown = section_assumptions(F)
    first, last = F.n(years[0], "year", "int"), F.n(years[-1], "year", "int")
    base_year = F.n(data.DEFAULT_BASE_YEAR, "year", "int")
    subs = {
        "FIRST_YEAR": first, "LAST_YEAR": last, "BASE_YEAR": base_year, "DEFLATOR": esc(deflator_name),
        "SCENARIO_TABLE": section_scenarios(M, F), "D4_TABLE": d4, "GFU_TABLE": gfu, "STRESS_TABLE": stress,
        "CATEGORY_TABLE": section_categories(M, cats, F), "ASM_SUMMARY": asm_summary, "ASM_LIST": asm_html,
        "CHANGES": section_changes(current, reference, F, M),
        "DATA_JSON": json.dumps(payload, separators=(",", ":")).replace("</", "<\\/"),
        "ASM_DEFLATOR": "ASM-DEFLATOR-DEFAULT", "ASM_BASEYEAR": "ASM-BASE-YEAR",
    }
    page = open(os.path.join(HERE, "template.html"), encoding="utf-8").read()
    for k, v in subs.items():
        page = page.replace("{{%s}}" % k, v)
    return page, new_snap, F.records


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--model", help="fiscal-model.json (default: regenerate it in a temp dir)")
    ap.add_argument("--out", default=os.path.join(HERE, "fiscal-viewer.html"))
    ap.add_argument("--snapshot-out", default=SNAPSHOT)
    a = ap.parse_args()
    page, snap, _ = build(a.model, load_snapshot())
    with open(a.out, "w", encoding="utf-8") as f:
        f.write(page)
    with open(a.snapshot_out, "w", encoding="utf-8") as f:
        json.dump(snap, f, indent=1, sort_keys=True)
        f.write("\n")
    print("wrote", a.out)


if __name__ == "__main__":
    main()
