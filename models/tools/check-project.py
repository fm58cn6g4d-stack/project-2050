"""Consistency checker for Project 2050 (Oct 20, 2026). Writes check-report.md.

It reads the run's own outputs (ledger.json, paths.json, fiscal-model.json, incidence.json, in the current
folder) and the hand-written documents, and lists where they disagree. It changes nothing: every finding is
for Espen or a later session to decide. Checks:
  1. headline numbers quoted in the documents against this run's results
  2. IDs: cited but defined nowhere in their domain file; ledger rows missing from their domain file or the
     options register
  3. stale phrases from superseded decisions
  4. reconcile: each ledger row's middle figure against the figures its domain file gives for that ID
  5. scaled figures: revenue rows whose source quotes a dollar figure in another window, re-scaled to 2030-39
  6. table checks: incidence rows against the ledger, fiscal profiles for every ledger row
Run by run-all.sh after the other steps; on its own, run it from build/ after run-all.sh.
"""
import csv, json, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from inputs import read, path as input_path
import window

def find_root():
    for d in (os.environ.get("P2050_ROOT"), os.getcwd(), os.path.dirname(os.path.abspath(__file__))):
        while d and d != os.path.dirname(d):
            if os.path.isdir(os.path.join(d, "governing")) and os.path.isdir(os.path.join(d, "domains")): return d
            d = os.path.dirname(d)
    raise SystemExit("check-project: repo root not found")
ROOT = find_root()
rel = lambda p: os.path.relpath(p, ROOT)

# Documents a headline figure may be quoted in. Decision briefs and sources are records of their day; generated
# index files are computed. The data/inputs CSVs are checked for IDs and stale phrases only.
def doc_files(stale=False):
    fs = [os.path.join(ROOT, "CLAUDE.md"), os.path.join(ROOT, "governing", "project-2050-governing-decisions.md"),
          os.path.join(ROOT, "index", "options-register.md"), os.path.join(ROOT, "index", "revenue-assignment-audit.md"),
          os.path.join(ROOT, "index", "tools", "readme.md")]
    fs += sorted(os.path.join(ROOT, "domains", f) for f in os.listdir(os.path.join(ROOT, "domains")) if f.endswith(".md"))
    if stale: fs += sorted(os.path.join(ROOT, "frameworks", f) for f in os.listdir(os.path.join(ROOT, "frameworks")) if f.endswith(".md"))
    return [f for f in fs if os.path.exists(f)]

def lines(f):
    with open(f, encoding="utf-8") as h:
        return h.read().splitlines()

HISTORICAL = re.compile(r"\b(was|were|previously)\b", re.I)
# A passage that reports an earlier state on its own terms (a dated "after X" note). Its figures are listed
# separately: often history to leave alone, sometimes a state line that should be refreshed or marked as dated.
DATED = re.compile(r"\*\*(?:After|Before|Later|Earlier)\b|\*Later the same day\*|\bafternoon\b|education batch|full rebuild|"
                   r"after Decision Brief 1|before the program trims|State saved|\(Oct 1\d\)|on Oct 1\d", re.I)

# ---------------------------------------------------------------------------------------------
# This run's results
# ---------------------------------------------------------------------------------------------
L = json.load(open("ledger.json")); S = L["summary"]
FM = json.load(open("fiscal-model.json")); DEC = FM["results"]["DEC"]; BASE = FM["results"]["BASE"]
PATHS = {p["path"][0]: p for p in json.load(open("paths.json"))}
INC = json.load(open("incidence.json"))
QN = next(k for k in INC if k.startswith("Q.")); Q4 = INC[QN]["res"]["Q4"]["net"]

def debt(res, y): return res["years"][str(y)]["debt_pct"]
FACTS = [
 # name, value, format, patterns (each captures the figure), plausible range for the captured figure
 ("general-fund claims", S["gf_claims"]["mid"], "${:.2f}T",
  [r"claims (?:of |~|about )*\$(\d+\.\d+)T", r"\$(\d+\.\d+)T (?:net )?(?:of )?(?:general-fund )?claims", r"(?:about|~)\$(\d+\.\d+)T net over 2030-39",
   r"claims (?:from \$[\d.]+T )?to (?:about )?\**\$(\d+\.\d+)T"], (8, 14)),
 ("top-end base", S["base_revenue"]["mid"], "${:.2f}T",
  [r"against (?:a |the )?\$(\d+\.\d+)T (?:top-end )?base", r"\$(\d+\.\d+)T from the top-end base", r"base (?:revenue )?(?:of )?\$(\d+\.\d+)T"], (5, 8)),
 ("ten-year gap", S["gap_mid"], "${:.2f}T",
  [r"an? \$(\d+\.\d+)T gap", r"gap (?:of )?\**\$(\d+\.\d+)T\**", r"gap is (?:about )?\**\$(\d+\.\d+)T", r"gap (?:from \$[\d.]+T )?to (?:about )?\**\$(\d+\.\d+)T",
   r"\$(\d+\.\d+)T short"], (3, 6.5)),
 ("gap after accepted options", S["gap_after_accepted"], "{:+.2f}T",
  [r"([−-]\$0\.\d+)T over ten years", r"gap[^.;]{0,80}?(?:about|~|leaves?)\s?\**([−-]\$0\.\d+)T",
   r"(?:after|with) (?:every option|all of them|the accepted options)[^.;]{0,40}?([−-]\$0\.\d+)T", r"([−-]\$0\.\d+)T (?:after|with) (?:every option|the accepted)"], (-1, 1)),
 ("accepted revenue", S["revenue_accepted"], "${:.2f}T", [r"accepted revenue (?:\([^)]*\) )?(?:is )?\$(\d+\.\d+)T"], (2, 5)),
 ("envelope borrowing", S["borrow_dollars"], "${:.2f}T", [r"\$(\d+\.\d+)T of (?:envelope )?borrowing", r"borrowing lines \([^)]*\) are \$(\d+\.\d+)T"], (0.5, 2)),
 ("legacy Senate floor days under F", PATHS["F"]["days"], "{}", [r"(\d{3}) (?:Senate )?floor days under F", r"F needs (\d{3}) floor days"], (100, 300)),
 ("legacy assumed floor-day budget", S["floor_budget"], "{}", [r"floor days (?:under F )?against (\d{3})", r"(\d{3})-day budget"], (100, 300)),
 ("DEC ten-year general-fund deficit", DEC["tests"]["gf_10yr_primary"], "${:.2f}T",
  [r"ten-year general-fund deficit (?:~|about |is about )*\$(\d\.\d+)T", r"general fund runs a primary deficit of \$(\d\.\d+)T"], (0, 3)),
 ("DEC total debt, 2056", debt(DEC, 2056), "{:.1f}%", [r"total debt (?:is )?(\d{3}\.\d)% of GDP in 2056", r"(\d{3}\.\d)% in 2056 vs"], (100, 250)),
 ("baseline debt, 2056", debt(BASE, 2056), "{:.1f}%", [r"baseline'?s? (\d{3}\.\d)%", r"(\d{3}\.\d)% in 2056\b(?! vs)"], (150, 250)),
 ("incidence scenario Q, fourth quintile", Q4, "+${:,}", [r"(?:Q4|fourth quintile)[^$]{0,30}\+\$([\d,]+)"], (0, 5000)),
]
FACT_CONTEXT = {"incidence scenario Q, fourth quintile": re.compile(r"scenario Q(?![-\w])|\(Q\)|Incidence scenario Q(?![-\w])"),
                "baseline debt, 2056": re.compile(r"baseline"),
                "DEC total debt, 2056": re.compile(r"\bDEC\b|decided|total debt")}

def parse_num(s):
    return float(s.replace("−", "-").replace("$", "").replace(",", ""))

def check_headlines():
    out, dated, ok, hist = [], [], 0, 0
    for f in doc_files():
        for n, line in enumerate(lines(f), 1):
            for name, val, fmt, pats, (lo, hi) in FACTS:
                ctx = FACT_CONTEXT.get(name)
                if ctx and not ctx.search(line): continue
                if "quintile" in name and re.search(r"scenario Q-(?:EDU|C19|H5p|SAF)", line): continue   # a variant's figure
                for p in pats:
                    for m in re.finditer(p, line):
                        x = parse_num(m.group(1))
                        if not lo <= x <= hi: continue
                        tol = 0.5 if "quintile" in name else (0.05 if "%" in fmt else 0.005)
                        if abs(x - val) <= tol: ok += 1; continue
                        if HISTORICAL.search(line[max(0, m.start() - 80):m.end() + 40]): hist += 1; continue
                        (dated if DATED.search(line) else out).append((rel(f), n, name, m.group(0), fmt.format(val)))
    return sorted(set(out)), sorted(set(dated)), ok, hist

# ---------------------------------------------------------------------------------------------
# IDs
# ---------------------------------------------------------------------------------------------
PREFIX_FILE = {"HLT": "domain-health.md", "FAM": "domain-family.md", "SS": "domain-social-security.md", "DEM": "domain-democracy.md",
               "CRT": "domain-courts.md", "EXE": "domain-executive-power.md", "INT": "domain-integrity.md", "CAP": "domain-capacity.md",
               "CLI": "domain-climate.md", "HOU": "domain-housing.md", "LAB": "domain-labor.md", "COM": "domain-competition.md",
               "IMM": "domain-immigration.md", "RTS": "domain-rights.md", "SAF": "domain-public-safety.md", "AI": "domain-ai.md",
               "NSC": "domain-national-security.md", "AMD": "domain-amendments.md", "EDU": "domain-education.md",
               "REV": "domain-revenue.md", "MOV": "transportation-moving-america-act-2031-draft-2.md"}
ID = re.compile(r"\b(" + "|".join(PREFIX_FILE) + r")-((?:[A-Z]{1,3})?\d+[A-Za-z]?)\b")

def check_ids():
    defined = {}
    for p, fn in PREFIX_FILE.items():
        text = open(os.path.join(ROOT, "domains", fn), encoding="utf-8").read()
        defined[p] = {f"{p}-{m.group(2)}" for m in ID.finditer(text) if m.group(1) == p}
    def known(p, i):
        if i in defined[p]: return True
        base = re.sub(r"[a-z]$", "", i)          # REV-C1a style sub-letters count if the parent is defined
        return base in defined[p]
    missing = {}
    sources = doc_files() + [os.path.join(ROOT, "governing", f) for f in os.listdir(os.path.join(ROOT, "governing"))]
    sources += [input_path(f) for f in ("ledger-bills.csv", "ledger-revenue.csv", "ledger-cuts.csv", "ledger-conflicts.csv", "incidence-rows.csv")]
    for f in sorted(set(sources)):
        for n, line in enumerate(lines(f), 1):
            for m in ID.finditer(line):
                p, i = m.group(1), m.group(0)
                if p == "MOV": continue          # Draft 2 uses its own A- tags until converted; noted once below
                if not known(p, i): missing.setdefault(i, []).append(f"{rel(f)}:{n}")
    ledger = []
    for b in L["bills"]:
        p = b["id"].split("-")[0]
        if p in PREFIX_FILE and p != "MOV" and b["id"] not in defined[p]:
            ledger.append((b["id"], f"not found in domains/{PREFIX_FILE[p]}"))
    rv = open(os.path.join(ROOT, "domains", "domain-revenue.md"), encoding="utf-8").read()
    channel_rows = re.compile(r"^(MR\d|PS\d|MF1|IF1|AI6|W\d|O\d|OX|P1|T1|E1|H1[ab]|C\d)$")
    for r in L["revenue"]:
        if f"REV-{r['id']}" not in rv and not channel_rows.match(r["id"]):
            ledger.append((r["id"], "no REV- entry in domains/domain-revenue.md"))
    reg = open(os.path.join(ROOT, "index", "options-register.md"), encoding="utf-8").read()
    cut_ids = {c["id"] for c in L["cuts"]}
    for c in sorted(cut_ids, key=lambda x: (len(x), x)):
        if not re.search(rf"\b{c}\b", reg): ledger.append((c, "not in index/options-register.md"))
    for c in sorted({m.group(0) for m in re.finditer(r"(?<![-\w])C\d{1,2}b?\b", reg)} - cut_ids, key=lambda x: (len(x), x)):
        ledger.append((c, "in index/options-register.md but not in ledger-cuts.csv"))
    return missing, ledger

# ---------------------------------------------------------------------------------------------
# Stale phrases (superseded decisions)
# ---------------------------------------------------------------------------------------------
STALE = [
 (r"2033 queue", r"no 2033 queue", "D1: no 2033 queue except DEM-3, DEM-4, DEM-9"),
 (r"\bD2\b[^.;]{0,25}\b(?:open|OPEN)\b", r"was open|reopen|no longer open", "D2 is decided (F, Oct 20)"),
 (r"fully paid for over ten years", r"was|before D4-B|D4-A|old", "D4-B (Oct 20): permanent programs paid for at maturity, not over ten years"),
 (r"65-72%|65% to 72%|86-92%", r"$^", "D8 on SSA's 2026 scores: about 64%, 84% with SS-5 (index/dedicated-funds.md)"),
 (r"\bclaude/", r"not claude/|\(not claude/|old `?claude/|claude\.ai Project", "old claude.ai Project path"),
 (r"\$10\.06T|\$3\.69T|\$10\.48T|\$4\.11T|\$4\.13T", None, "an earlier headline figure"),
 (r"Beyond Health Care", r"superseded|archive|ideas only|replaces|assume", "Beyond Health Care is superseded (archive, ideas only)"),
 (r"\$400K pledge", r"no \$400K|not .{0,20}\$400K|drop|is gone|What does the \$400K pledge cover", "D3: no $400K pledge"),
 (r"run `?final_v3\.py", None, "transportation: run report.py (final_v3.py is in legacy/)"),
]
def check_stale():
    out = []
    files = doc_files(stale=True) + [input_path(f) for f in ("ledger-bills.csv", "ledger-revenue.csv", "ledger-cuts.csv", "incidence-rows.csv")]
    for f in files:
        for n, line in enumerate(lines(f), 1):
            for pat, unless, why in STALE:
                m = re.search(pat, line)
                if m and not (unless and re.search(unless, line, re.I)) and not HISTORICAL.search(line[max(0, m.start() - 60):m.end() + 30]):
                    out.append((rel(f), n, m.group(0), why + (" (dated passage)" if DATED.search(line) else "")))
    return out

# ---------------------------------------------------------------------------------------------
# Reconcile: ledger middle figures against the domain files
# ---------------------------------------------------------------------------------------------
TN = re.compile(r"[−-]?\$(\d+(?:\.\d+)?)(?:-(\d+(?:\.\d+)?))?\s?(T|B)\b")
BARE = re.compile(r"(?<![\w$.,/])[−-]?(\d+\.\d+)(?![\w%.])")
def amounts(line, ident=None):
    """Dollar figures ($T, $B) on a line; on a table row that names the ID, also bare decimals ($T by convention)."""
    out = []
    if ident and line.lstrip().startswith("|"):
        cells = [c.strip() for c in line.split("|")[1:-1]]
        if any(re.search(rf"\b{re.escape(ident)}\b", c) for c in cells[:2]):
            for c in cells[2:]:
                if "$" not in c and "%" not in c: out += [float(x) for x in BARE.findall(c)]
    for m in TN.finditer(line):
        k = 1.0 if m.group(3) == "T" else 0.001
        out += [float(m.group(1)) * k] + ([float(m.group(2)) * k] if m.group(2) else [])
    return out

def check_reconcile():
    rows = []
    def one(i, mid, lo, hi, fn, aliases):
        text = lines(os.path.join(ROOT, "domains", fn))
        found = []
        for line in text:
            if any(re.search(rf"\b{re.escape(a)}\b", line) for a in aliases): found += amounts(line, aliases[0])
        if not found: return ("no dollar figure next to the ID", [])
        if any(abs(abs(x) - abs(mid)) <= max(0.006, 0.02 * abs(mid)) for x in found): return None
        if any(abs(abs(x) - abs(lo)) <= 0.006 for x in found) and any(abs(abs(x) - abs(hi)) <= 0.006 for x in found): return None
        near = sorted(set(round(x, 3) for x in found if x >= 0.001), key=lambda x: abs(x - abs(mid)))[:4]
        return ("ledger middle not among the figures given for this ID", near)
    for b in L["bills"]:
        p = b["id"].split("-")[0]
        if p not in PREFIX_FILE or p == "MOV" or b["cost_mid"] == 0: continue
        r = one(b["id"], b["cost_mid"], b["cost_lo"], b["cost_hi"], PREFIX_FILE[p], [b["id"]])
        if r: rows.append((b["id"], b["cost_mid"], "domains/" + PREFIX_FILE[p], r[0], r[1], b["basis_note"]))
    for v in L["revenue"]:
        if v["mid"] == 0 or v["id"].startswith(("MR", "PS", "MF", "IF", "W", "T1", "O", "P1")): continue
        r = one(v["id"], v["mid"], v["lo"], v["hi"], "domain-revenue.md", [f"REV-{v['id']}"])
        if r: rows.append((v["id"], v["mid"], "domains/domain-revenue.md", r[0], r[1], v["overlap"]))
    return rows

# ---------------------------------------------------------------------------------------------
# Scaled figures: re-run the window scaling on revenue rows whose source quotes another window
# ---------------------------------------------------------------------------------------------
SRC = re.compile(r"\$(\d+(?:\.\d+)?)(B|T)[^)]{0,25}?(20\d\d)-(\d\d)\b")
def check_scaled():
    out = []
    for v in L["revenue"]:
        if "scaled" not in v["source"].lower() or v["mid"] == 0: continue
        m = SRC.search(v["source"])
        if not m: continue
        amt = float(m.group(1)) * (1 if m.group(2) == "T" else 0.001)
        a = int(m.group(3)); b = int(str(a)[:2] + m.group(4))
        if b - a != 9: continue
        sc = window.rescale(amt, (a, b))
        out.append((v["id"], f"{m.group(0)}", round(sc, 3), v["mid"], round(v["mid"] / sc - 1, 2)))
    return out

# ---------------------------------------------------------------------------------------------
# Table checks
# ---------------------------------------------------------------------------------------------
def check_tables():
    out = []
    import importlib
    sys.path.insert(0, os.getcwd())
    inc = importlib.import_module("incidence")
    for r in read("incidence-rows.csv"):
        if r["check"]:
            a, c = inc.amount(r["amount"]), inc.amount(r["check"])
            if abs(a - c) > 1e-9: out.append(f"Incidence row {r['id']} uses {a} where the ledger gives {r['check']} = {c}.")
    prof = {r["id"] for r in read("fiscal-profiles.csv")}
    for b in L["bills"]:
        if b["id"] not in prof: out.append(f"Ledger bill {b['id']} has no fiscal profile (the long-term model defaults it).")
    for c in L["cuts"]:
        if c["id"] not in prof: out.append(f"Option {c['id']} has no fiscal profile.")
    for r in read("ledger-revenue.csv"):
        if r["in_base"] == "yes" and r["id"] not in prof and r["channel"] == "General fund":
            out.append(f"Base revenue row {r['id']} has no fiscal profile.")
    for k in read("incidence-keys.csv"):
        t = sum(float(k[q]) for q in ("q1", "q2", "q3", "q4", "q5"))
        if abs(t - 100) > 1e-6: out.append(f"Incidence key {k['key']} sums to {t}, not 100.")
    return out

# ---------------------------------------------------------------------------------------------
def main():
    head, dated, ok, hist = check_headlines(); missing, ledger_ids = check_ids()
    seen = {(f, n) for f, n, *_ in head + dated}
    stale = [x for x in check_stale() if not (x[3].startswith("an earlier headline") and (x[0], x[1]) in seen)]
    rec = check_reconcile(); scaled = check_scaled(); tables = check_tables()
    o = []; A = o.append
    A("# Project consistency check\n")
    funding = json.load(open("capacity-funding.json"))
    if funding["fy2029_outlay_bn"] is None:
        A("**Outstanding surge costing:** CAP-7S is fully available on enactment in FY2029, targeting R1; FY2029 cash is unpriced, not zero. Fiscal/debt/interest/envelope results retain the old cash proxy and do not validate acceleration. Reconciliation eligibility remains pending. See index/capacity-funding-model.md.\n")
    A("*Generated by index/tools/check-project.py on each run of run-all.sh. Do not edit by hand. It lists where the documents and the input tables disagree with this run's results or with each other, and changes nothing: each finding is for Espen or a later session to decide. Decision briefs and sources/ are records of their day and are not checked for headline numbers.*\n")
    A(f"**Summary:** {len(head)} stale headline figures (and {len(dated)} in dated passages); {len(missing)} IDs cited but not found in their domain file; {len(ledger_ids)} ledger or register ID mismatches; {len(stale)} stale phrases; {len(rec)} ledger rows to reconcile against their domain file; {len(tables)} table findings. Headline mentions that match: {ok}; skipped as historical: {hist}.\n")
    A("## 1. Headline numbers\n")
    A("Current values from this run: " + "; ".join(f"{n} {fmt.format(v)}" for n, v, fmt, *_ in FACTS) + ".\n")
    if head:
        A("| File | Line | Figure | Quoted | This run |\n| --- | --- | --- | --- | --- |")
        for f, n, name, q, cur in head: A(f"| {f} | {n} | {name} | {q} | {cur} |")
    else: A("Every headline figure quoted in the checked documents matches this run.")
    if dated:
        A("\nIn dated passages (an \"after X\" note or a saved state). Usually history to leave alone, sometimes a state line to refresh or mark as dated:\n")
        A("| File | Line | Figure | Quoted | This run |\n| --- | --- | --- | --- | --- |")
        for f, n, name, q, cur in dated: A(f"| {f} | {n} | {name} | {q} | {cur} |")
    A("\n## 2. IDs\n")
    A("IDs cited somewhere but never mentioned in their own domain file (a typo, a retired ID, or an option the domain file does not yet carry):\n")
    if missing:
        A("| ID | Cited at |\n| --- | --- |")
        for i in sorted(missing, key=lambda x: (x.split("-")[0], len(x), x)):
            locs = missing[i]; A(f"| {i} | {', '.join(locs[:4])}{' and %d more' % (len(locs) - 4) if len(locs) > 4 else ''} |")
    else: A("None.")
    A("\nLedger and register:\n")
    if ledger_ids:
        A("| ID | Finding |\n| --- | --- |")
        for i, w in ledger_ids: A(f"| {i} | {w} |")
    else: A("Every ledger row is in its domain file, and the ledger's options match the options register.")
    A("\nMOV-29, MOV-30 and MOV-31 are the ledger's own IDs for Moving America: Draft 2 uses decision tags (A-1 and so on) until it is converted to a domain file, so they are not checked against it. The transportation model checks those rows' figures.")
    A("\n## 3. Stale phrases\n")
    if stale:
        A("| File | Line | Phrase | Why |\n| --- | --- | --- | --- |")
        for f, n, p, w in stale: A(f"| {f} | {n} | {p} | {w} |")
    else: A("None found.")
    A("\n## 4. Reconcile: ledger against domain files\n")
    A("For each ledger row with a cost, the domain file's lines that name the ID are searched for dollar figures. Listed here: rows where the ledger's middle figure (or its low and high together) is not among them. Many are fine (the domain file gives a per-year figure, or a component); each is worth a look.\n")
    if rec:
        A("| ID | Ledger middle ($T) | Domain file | Finding | Nearest figures there ($T) | Ledger note |\n| --- | --- | --- | --- | --- | --- |")
        for i, mid, f, w, near, note in rec: A(f"| {i} | {mid} | {f} | {w} | {', '.join(str(x) for x in near) or '—'} | {note.replace('|', '/')} |")
    else: A("Every ledger row's figure appears in its domain file.")
    A("\n## 5. Scaled figures\n")
    A("Revenue rows whose source quotes a ten-year figure in another window, rescaled to 2030-39 by nominal GDP (index/tools/window.py, CBO's February 2026 path). A large difference means the row carries a haircut, a newer score or a different base; the row's note should say which.\n")
    if scaled:
        A("| ID | Source figure | Rescaled to 2030-39 ($T) | Ledger middle ($T) | Difference |\n| --- | --- | --- | --- | --- |")
        for i, src, sc, mid, d in scaled: A(f"| {i} | {src} | {sc} | {mid} | {d:+.0%} |")
    else: A("None.")
    A("\n## 6. Table checks\n")
    A("\n".join(f"- {t}" for t in tables) if tables else "All input tables are consistent with the ledger.")
    open("check-report.md", "w", encoding="utf-8").write("\n".join(o) + "\n")
    print(f"check: {len(head)} stale headlines, {len(missing)} unknown IDs, {len(ledger_ids)} ledger ID findings, "
          f"{len(stale)} stale phrases, {len(rec)} to reconcile, {len(tables)} table findings")

if __name__ == "__main__":
    main()
