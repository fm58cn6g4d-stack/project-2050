#!/usr/bin/env python3
"""test_viewer.py: checks for the fiscal viewer (piece B5). Run: python3 models/tools/budget/viewer/test_viewer.py

1. The page builds from a clean checkout (the model is regenerated in a temp dir).
2. Every figure printed in the page's text traces to a source value (re-read here, independently).
3. Every number in the page's visible text is one of those traced figures: nothing is hand-typed.
4. Quoted text (assumptions, labels) equals the source cell exactly.
5. The chart data equals the source values; real and % of GDP follow data.py's conversions and a direct
   recomputation from deflators.csv and the model's own GDP.
6. The generator holds no numeric literals beyond a small allowlist; the page makes no external requests.
7. Flagged assumptions are flagged; rebuilding with the snapshot it wrote gives the same page.
"""
import ast, csv, html, json, os, re, sys, tempfile, unittest
from html.parser import HTMLParser

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, ".."))
import build_viewer as bv  # noqa: E402
import data  # noqa: E402

TMP = tempfile.TemporaryDirectory()
MODEL_PATH = bv.generate_model(TMP.name)
MODEL = json.load(open(MODEL_PATH))
PAGE, SNAP, RECORDS = bv.build(MODEL_PATH, None)


class Visible(HTMLParser):
    """Visible text split into plain text and quoted text (inside data-quoted elements)."""
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.plain, self.quoted, self.stack, self.skip, self.q = [], [], [], 0, 0
    def handle_starttag(self, tag, attrs):
        if tag in ("script", "style", "title"):
            self.skip += 1
        if tag in ("br", "meta", "link", "input", "hr", "img", "line"):
            return
        self.stack.append((tag, "data-quoted" in dict(attrs)))
        self.q += self.stack[-1][1]
    def handle_endtag(self, tag):
        if tag in ("script", "style", "title"):
            self.skip -= 1
        while self.stack:
            t, q = self.stack.pop()
            self.q -= q
            if t == tag:
                break
    def handle_data(self, d):
        if self.skip:
            return
        (self.quoted if self.q else self.plain).append(d)


def visible(page):
    v = Visible(); v.feed(page); return " ".join(v.plain), v.quoted


def dig(obj, path):
    for k in path.split("."):
        obj = obj[k]
    return obj


def source_value(src):
    kind, _, rest = src.partition(":")
    if kind == "model":
        return dig(MODEL, rest)
    if kind == "diff":   # composition.<year>.<category>: decided minus baseline
        _, y, c = rest.split(".")
        return MODEL["composition"]["DEC"][y][c] - MODEL["composition"]["BASE"][y][c]
    raise AssertionError("unknown source kind " + src)


class TestViewer(unittest.TestCase):
    def test_builds_from_clean_checkout(self):
        page, snap, recs = bv.build(None, None)   # regenerates the model itself
        self.assertEqual(page, PAGE)
        self.assertIn("Fiscal Viewer", page)

    def test_figures_trace_to_sources(self):
        self.assertGreater(len(RECORDS), 300)
        years = {int(y) for y in MODEL["results"]["BASE"]["years"]}
        asm = list(csv.DictReader(open(bv.ASSUMPTIONS)))
        n_shown = sum(1 for r in asm if bv.DRIVES.search(r["where"]))
        n_flag = sum(1 for r in asm if bv.DRIVES.search(r["where"]) and r["decided_by"].startswith(("unrecorded", "Proposed")))
        cur = bv.headline(MODEL)
        for r in RECORDS:
            kind = r["src"].split(":")[0]
            if kind in ("model", "diff"):
                self.assertEqual(r["raw"], source_value(r["src"]), r["src"])
            elif kind == "year":
                self.assertIn(r["raw"], years | {data.DEFAULT_BASE_YEAR})
            elif kind == "count":
                want = {"assumptions-shown": n_shown, "assumptions-flagged": n_flag}[r["src"].split(":")[1]]
                self.assertEqual(r["raw"], want)
            elif kind == "snapshot":
                self.assertEqual(r["raw"], cur[r["src"].split(":", 1)[1]]["value"])
            self.assertEqual(r["text"], bv.fmt(r["raw"], r["kind"]) if r["kind"] != "text" else r["text"])

    def test_no_hand_typed_numbers_in_text(self):
        plain, _ = visible(PAGE)
        allowed = {re.sub(r"^[−+-]", "", r["text"]) for r in RECORDS}
        tokens = re.findall(r"(?<![\w\-.])[−+-]?\d[\d,]*(?:\.\d+)?", plain)
        self.assertGreater(len(tokens), 300)
        stray = [t for t in tokens if re.sub(r"^[−+-]", "", t) not in allowed]
        self.assertEqual(stray, [], "numbers in the page text with no recorded source")

    def test_quoted_text_equals_source(self):
        _, quoted = visible(PAGE)
        asm = list(csv.DictReader(open(bv.ASSUMPTIONS)))
        ok = set()
        for r in asm:
            ok.update(v.strip() for v in r.values())
        for r in MODEL["results"].values():
            ok.add(r["label"])
        ok.update(c["label"] for c in data.categories("baseline"))
        for item in bv.headline(MODEL).values():
            ok.add(item["label"])
        bad = [q for q in quoted if q.strip() not in ok]
        self.assertEqual(bad, [])

    def test_chart_data_matches_sources(self):
        m = re.search(r'<script id="viewer-data" type="application/json">(.*?)</script>', PAGE, re.S)
        D = json.loads(m.group(1).replace("<\\/", "</"))
        years = D["years"]
        defl = {int(r["year"]): float(r[data.DEFAULT_INDEX]) for r in csv.DictReader(open(os.path.join(data.DATA, "deflators.csv")))}
        for sid, res in MODEL["results"].items():
            for key, _, _ in bv.METRICS:
                nom = [res["years"][str(y)][key] for y in years]
                self.assertEqual(D["series"]["nominal"][key][sid], [round(v, 3) for v in nom])
                real = [v * defl[data.DEFAULT_BASE_YEAR] / defl[y] for v, y in zip(nom, years)]
                for a, b in zip(D["series"]["real"][key][sid], real):
                    self.assertAlmostEqual(a, b, delta=0.002)
                pct = [100 * v / res["years"][str(y)]["gdp"] for v, y in zip(nom, years)]
                for a, b in zip(D["series"]["pct"][key][sid], pct):
                    self.assertAlmostEqual(a, b, delta=0.002)
            for key, own in (("deficit", "deficit_pct"), ("debt", "debt_pct"), ("interest", "interest_pct")):
                for a, y in zip(D["series"]["pct"][key][sid], years):
                    self.assertAlmostEqual(a, res["years"][str(y)][own], delta=0.002)
        rows = {int(r["year"]): r for r in csv.DictReader(open(bv.BASELINE_CSV))}
        for k, vals in D["catseries"]["nominal"].items():
            for v, y in zip(vals, years):
                self.assertAlmostEqual(v, float(rows[y][k]), delta=0.0011)
        self.assertEqual(D["base_year"], data.DEFAULT_BASE_YEAR)

    def test_generator_has_no_numeric_literals_beyond_allowlist(self):
        tree = ast.parse(open(os.path.join(HERE, "build_viewer.py")).read())
        found = sorted({n.value for n in ast.walk(tree) if isinstance(n, ast.Constant)
                        and isinstance(n.value, (int, float)) and not isinstance(n.value, bool)})
        self.assertTrue(set(found) <= set(range(8)), found)   # 0-3 digits and indexing; 1-7 are colour-slot numbers

    def test_no_external_requests(self):
        for pat in (r'(src|href)\s*=\s*["\']https?:', r'url\(\s*["\']?https?:', r"@import", r"fetch\(", r"XMLHttpRequest"):
            self.assertIsNone(re.search(pat, PAGE), pat)

    def test_assumption_flags(self):
        asm = {r["id"]: r for r in csv.DictReader(open(bv.ASSUMPTIONS))}
        shown = re.findall(r'<details id="(ASM-[A-Z0-9-]+)" class="asm (\w+)">', PAGE)
        self.assertGreater(len(shown), 20)
        for aid, cls in shown:
            d = asm[aid]["decided_by"]
            self.assertEqual(cls, "warn" if d.startswith(("unrecorded", "Proposed")) else "good", aid)
        ids = [a for a, _ in shown]
        for must in ("ASM-GF-UNIFIED", "ASM-RATE-SHIFT", "ASM-DEFLATOR-DEFAULT", "ASM-BASE-YEAR"):
            self.assertIn(must, ids)
        self.assertNotIn("ASM-FUND-SS-RESERVE", ids)

    def test_changes_and_idempotence(self):
        self.assertIn("first build", PAGE)
        page2, snap2, _ = bv.build(MODEL_PATH, SNAP)            # same sources, snapshot it wrote
        self.assertEqual(snap2, SNAP)
        self.assertIn("first build", page2)                      # nothing before it to compare with
        old = json.loads(json.dumps(SNAP))
        k = sorted(old["figures"])[0]
        old["figures"][k]["value"] = old["figures"][k]["value"] + 1.0
        page3, snap3, recs3 = bv.build(MODEL_PATH, old)
        self.assertIn(old["figures"][k]["label"], html.unescape(page3))
        self.assertEqual(snap3["previous"], old["figures"])
        page4, snap4, _ = bv.build(MODEL_PATH, snap3)           # once recorded, the same list again
        self.assertEqual(page4, page3)


if __name__ == "__main__":
    unittest.main(verbosity=1)
