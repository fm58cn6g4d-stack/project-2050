#!/usr/bin/env python3
"""Project 2050 merge gate: tier classification, cross-agent review, Espen approval, merge and daily digest.

Standard library only. The rules live in .github/merge-policy.json; the plain-language version is in
governing/project-collaboration.md and governing/agent-automation-setup.md.

  agent_gate.py classify --base SHA --head SHA --out FILE    tier from changed paths and headline numbers (git only)
  agent_gate.py headlines [--rev REV]                        headline numbers read from committed outputs
  agent_gate.py gate --pr N [--classification FILE] [--event ACTION]
                                                             set the merge-tier and agent-review statuses, update the
                                                             PR's gate comment and, when allowed, merge (GitHub API)
  agent_gate.py digest                                       update the daily digest issue (GitHub API)

Everything here identifies agents by what they write (branch prefix, Agent-Author / Agent-Review lines), because
every agent currently pushes as Espen's GitHub account. That is an honest-agent protocol and an audit trail, not
security against an agent that ignores the rules; see governing/agent-automation-setup.md.
"""
import argparse
import csv
import fnmatch
import io
import json
import os
import re
import subprocess
import sys
import urllib.error
import urllib.request
from collections import Counter
from datetime import datetime, timedelta, timezone

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
POLICY_PATH = os.path.join(ROOT, ".github", "merge-policy.json")
MARK = "<!-- agent-gate -->"
DATA = re.compile(r"<!-- agent-gate-data (\{.*?\}) -->", re.S)
DIGEST_MARK = "<!-- agent-digest -->"


def load_policy(path=POLICY_PATH):
    with open(path, encoding="utf-8") as f:
        return json.load(f)


# ------------------------------------------------------------------------------------------------
# git helpers
# ------------------------------------------------------------------------------------------------
def git(*args, check=True):
    r = subprocess.run(["git", *args], cwd=ROOT, capture_output=True, text=True)
    if check and r.returncode:
        raise RuntimeError(f"git {' '.join(args)}: {r.stderr.strip()}")
    return r.stdout


def file_at(rev, path):
    r = subprocess.run(["git", "show", f"{rev}:{path}"], cwd=ROOT, capture_output=True, text=True)
    return r.stdout if r.returncode == 0 else None


def changed_files(base, head):
    """[(status, path, old_path)] between the merge base of base..head and head."""
    out = []
    for line in git("diff", "--name-status", "-M", f"{base}...{head}").splitlines():
        parts = line.split("\t")
        st = parts[0][0]
        if st == "R":
            out.append(("R", parts[2], parts[1]))
        else:
            out.append((st, parts[1], parts[1]))
    return out


def diff_lines(base, head, path):
    removed, added = [], []
    for line in git("diff", "-U0", f"{base}...{head}", "--", path).splitlines():
        if line.startswith("---") or line.startswith("+++"):
            continue
        if line.startswith("-"):
            removed.append(line[1:])
        elif line.startswith("+"):
            added.append(line[1:])
    return removed, added


# ------------------------------------------------------------------------------------------------
# Wording and program-ID tests
# ------------------------------------------------------------------------------------------------
NUM = re.compile(r"\d[\d,]*(?:\.\d+)?")
POLICY_ID = re.compile(r"\b[A-Z]{2,4}-(?:[A-Z]{0,3}\d+[A-Za-z]?|[A-Z]{1,3})\b")


def tokens(lines):
    text = "\n".join(lines)
    return Counter(NUM.findall(text)) + Counter(POLICY_ID.findall(text))


def wording_only(removed, added):
    """True when the changed lines keep exactly the same numbers and policy IDs (a wording fix)."""
    return tokens(removed) == tokens(added)


def program_ids(text):
    return set(POLICY_ID.findall(text or ""))


_DOMAIN_IDS = {}


def all_domain_ids(rev):
    if rev not in _DOMAIN_IDS:
        ids = set()
        for path in git("ls-tree", "-r", "--name-only", rev, "--", "domains").splitlines():
            ids |= program_ids(file_at(rev, path))
        _DOMAIN_IDS[rev] = ids
    return _DOMAIN_IDS[rev]


# ------------------------------------------------------------------------------------------------
# Headline numbers, read from committed generated files (the drift check makes them match the inputs)
# ------------------------------------------------------------------------------------------------
def headlines_at(rev=None):
    """{name: value}. Names start with 'test:', 'margin:' or 'num:'; see merge-policy.json for the tiers."""
    read = (lambda p: file_at(rev, p)) if rev else (lambda p: _read(p))
    h = {}
    fp = read("index/data/fiscal-paths.csv")
    if fp:
        try:
            by = {int(r["year"]): r for r in csv.DictReader(io.StringIO(fp)) if r["scenario"] == "DEC"}
            pct = lambda y: float(by[y]["gf_primary"]) / float(by[y]["gdp"]) * 100
            h["margin:D4 general-fund balance FY2040, % of GDP (fiscal model DEC; deficit > 0)"] = round(pct(2040), 4)
            worst = max(pct(y) for y in by if 2040 <= y <= 2056)
            h["test:D4 paid-for-at-maturity test passes, FY2040-56 (fiscal model DEC)"] = worst <= 0
            h["num:Total debt 2039, % of GDP (fiscal model DEC)"] = float(by[2039]["debt_pct"])
            h["num:Total debt 2056, % of GDP (fiscal model DEC)"] = float(by[2056]["debt_pct"])
        except (KeyError, ValueError) as e:
            h["test:fiscal-paths.csv readable"] = f"unreadable: {e}"
    rb = read("index/data/recovery-budget.json")
    if rb:
        try:
            d = json.loads(rb)
            case = d["adoption"]["selected_architecture_case"]
            s = d["cases"][case]["summary"]
            tag = f"(recovery budget, {case})"
            h[f"margin:Largest mature general-fund gap FY2040+, % of GDP {tag}"] = round(s["max_mature_agenda_gf_gap_gdp"], 4)
            h[f"test:D4 debt ratio non-increasing 2045-56 {tag}"] = s["debt_ratio_nonincreasing_2045_56"]
            h[f"test:Social Security sustainable {tag}"] = s["ss_sustainable"]
            h[f"test:HI trust fund depletion year {tag}"] = s["hi_depletion"]
            h[f"test:Education fund depletion year {tag}"] = s["education_depletion"]
            h[f"num:Total debt 2039, % of GDP {tag}"] = round(s["debt_gdp_2039"], 3)
            h[f"num:Total debt 2056, % of GDP {tag}"] = round(s["debt_gdp_2056"], 3)
            h[f"num:New income tax FY2030-39, $T {tag}"] = round(s["new_income_tax_tn"], 3)
            hh = d["household_diagnostic"]["per_household_annual_dollars"]
            hc = case if case in hh else "mixed"
            for y in ("2034", "2039"):
                h[f"test:D3 quintiles 1-4 all ahead in {y} (household diagnostic, {hc})"] = all(
                    hh[hc][y][q] >= 0 for q in ("Q1", "Q2", "Q3", "Q4"))
            for q in ("Q1", "Q2", "Q3", "Q4"):
                h[f"num:{q} net per household 2039, $ (household diagnostic, {hc})"] = hh[hc]["2039"][q]
        except (KeyError, ValueError, TypeError) as e:
            h["test:recovery-budget.json readable"] = f"unreadable: {e}"
    return h


def _read(path):
    try:
        with open(os.path.join(ROOT, path), encoding="utf-8") as f:
            return f.read()
    except OSError:
        return None


def compare_headlines(base, head, policy):
    """Rows of (name, base, head, tier) for headlines that moved; tier 3 for tests/margins/large moves."""
    hp = policy["headlines"]
    rows = []
    for name in sorted(set(base) | set(head)):
        b, a = base.get(name, "missing"), head.get(name, "missing")
        if b == a:
            continue
        kind = name.split(":", 1)[0]
        tier = 3
        if kind == "margin" and isinstance(a, (int, float)) and isinstance(b, (int, float)):
            tier = 3 if abs(a - b) > hp["margin_tolerance_pct_gdp"] else 2
        elif kind == "num" and isinstance(a, (int, float)) and isinstance(b, (int, float)):
            rel = abs(a - b) / max(abs(b), hp["absolute_floor"])
            tier = 3 if rel > hp["relative_tolerance"] else 2
        rows.append((name.split(":", 1)[1], b, a, tier))
    return rows


# ------------------------------------------------------------------------------------------------
# Tier classification
# ------------------------------------------------------------------------------------------------
def match_rule(path, policy):
    for r in policy["rules"]:
        if fnmatch.fnmatch(path, r["pattern"]):
            return r
    return {"tier": 2, "why": "unlisted"}


def owners_of(path, policy):
    return {o["owner"] for o in policy["owners"] if fnmatch.fnmatch(path, o["pattern"])}


def is_generated(path, policy):
    return any(fnmatch.fnmatch(path, p) for p in policy["generated_outputs"])


def classify(base, head, policy):
    files = changed_files(base, head)
    reasons, owners, outputs_changed = [], set(), False
    for st, path, old in files:
        owners |= owners_of(path, policy) | owners_of(old, policy)
        if is_generated(path, policy):
            if path in policy["wording_outputs"]:
                reasons.append((path, 1, "consistency report (follows document edits)"))
            else:
                outputs_changed = True
                reasons.append((path, 2, "regenerated model output"))
            continue
        rule = match_rule(path, policy)
        tier, why = rule["tier"], rule["why"]
        if tier == "domain":
            before = file_at(f"{base}", old) if st != "A" else ""
            after = file_at(head, path) if st != "D" else ""
            # A program is new if no domain file mentioned it before, removed if no domain file mentions it after;
            # citing an existing program from another domain file is not a new program.
            gained = sorted(program_ids(after) - program_ids(before) - all_domain_ids(base))
            lost = sorted(program_ids(before) - program_ids(after) - all_domain_ids(head))
            if gained or lost:
                tier, why = 3, "program IDs added/removed: " + ", ".join([f"+{i}" for i in gained] + [f"-{i}" for i in lost])
            elif st == "M" and wording_only(*diff_lines(base, head, path)):
                tier, why = 1, "domain wording fix (same numbers and IDs)"
            else:
                tier, why = 2, "domain design change (numbers changed, same programs)"
        elif st == "M" and tier == 1 and path.endswith(".md") and wording_only(*diff_lines(base, head, path)):
            why += "; wording only"
        reasons.append((path, tier, why))
    rows = []
    if outputs_changed or any(p.startswith("index/data/inputs/") for _, p, _ in files):
        rows = compare_headlines(headlines_at(base), headlines_at(head), policy)
        for name, b, a, t in rows:
            reasons.append((f"headline: {name}", t, f"{fmt(b)} -> {fmt(a)}"))
    tier = max([r[1] for r in reasons], default=1)
    return {
        "base": git("rev-parse", base).strip(), "head": git("rev-parse", head).strip(),
        "tier": tier, "reasons": reasons, "headline_changes": rows, "owners": sorted(owners),
        "files": len(files),
    }


def fmt(v):
    if isinstance(v, float):
        return f"{v:,.4g}" if abs(v) < 1000 else f"{v:,.1f}"
    return str(v)


# ------------------------------------------------------------------------------------------------
# Agent identity, reviews and Espen's approval
# ------------------------------------------------------------------------------------------------
AUTHOR = re.compile(r"^\s*Agent-Author:\s*([a-z][a-z-]*)(?:[ \t]+(\S+))?[ \t]*$", re.M | re.I)
REVIEW = re.compile(r"^\s*Agent-Review:\s*(approve|changes-requested)\s*$", re.M | re.I)
REVIEWED_HEAD = re.compile(r"^\s*Reviewed-Head:\s*([0-9a-f]{7,40})\s*$", re.M | re.I)
REVIEWER = re.compile(r"^\s*Reviewer:\s*([a-z][a-z-]*)(?:[ \t]+(\S+))?[ \t]*$", re.M | re.I)


def pr_author(body, branch, policy):
    m = AUTHOR.search(body or "")
    if m and m.group(1).lower() in policy["agents"]:
        return m.group(1).lower(), m.group(2)
    for agent, cfg in policy["agents"].items():
        if any(branch.startswith(p) for p in cfg["branch_prefixes"]):
            return agent, None
    return None, None


def parse_review(body):
    """(verdict, head prefix, agent, session) or None."""
    body = body or ""
    v, h, r = REVIEW.search(body), REVIEWED_HEAD.search(body), REVIEWER.search(body)
    if not (v and h and r):
        return None
    return v.group(1).lower(), h.group(1).lower(), r.group(1).lower(), r.group(2)


def evaluate_reviews(items, head_sha, author, owners, policy):
    """items: [{'body','created_at','app'}] in any order. Returns (ok, summary, approvals)."""
    author_agent, author_session = author
    latest = {}
    trusted = set(policy["trusted_logins"])
    for it in sorted(items, key=lambda x: x["created_at"]):
        if it.get("user") not in trusted:
            continue  # on a public repository anyone can comment
        p = parse_review(it["body"])
        if not p:
            continue
        verdict, h, agent, session = p
        if agent not in policy["agents"] or not head_sha.startswith(h):
            continue
        own = policy["agents"][agent].get("apps") or []
        others = {a for name, cfg in policy["agents"].items() if name != agent for a in cfg.get("apps") or []}
        if (own and it.get("app") not in own) or it.get("app") in others:
            continue  # the comment did not come through the claimed agent's own integration
        if agent == author_agent and (not session or not author_session or session == author_session):
            continue  # an author cannot review their own PR; same-vendor reviews need distinct sessions
        latest[(agent, session)] = (verdict, it.get("app"))
    approvals = sorted(k for k, v in latest.items() if v[0] == "approve")
    blocks = sorted(k for k, v in latest.items() if v[0] == "changes-requested")
    if blocks:
        return False, "changes requested by " + ", ".join(f"{a} {s or ''}".strip() for a, s in blocks), approvals
    if not approvals:
        return False, f"no approving agent review of {head_sha[:7]}", approvals
    missing = [o for o in owners if o != author_agent and o not in {a for a, _ in approvals}]
    if missing:
        return False, "path owner must review: " + ", ".join(missing), approvals
    return True, "approved by " + ", ".join(f"{a} {s or ''}".strip() for a, s in approvals), approvals


def label_added_before(events, name, when):
    """True when the label's latest 'labeled' event is older than `when` (an ISO time, e.g. the push)."""
    added = [e.get("created_at") or "" for e in events if e.get("event") == "labeled" and (e.get("label") or {}).get("name") == name]
    return bool(added) and (not when or max(added) < when)


def espen_approval(events, policy):
    """(ok, detail) from the PR's issue events for the espen-approved label (latest labeled event wins)."""
    name = policy["labels"]["espen_approved"]
    ev = [e for e in events if e.get("event") in ("labeled", "unlabeled") and (e.get("label") or {}).get("name") == name]
    if not ev or ev[-1]["event"] != "labeled":
        return False, "no espen-approved label"
    e = ev[-1]
    actor = (e.get("actor") or {}).get("login")
    app = (e.get("performed_via_github_app") or {}).get("slug")
    if actor not in policy["espen_logins"]:
        return False, f"label added by {actor}, not Espen"
    if app and app not in policy["espen_label_apps_allowed"]:
        return False, f"label added through the {app} app (an agent integration), not by Espen directly"
    return True, f"label added by {actor} directly" + (f" via {app}" if app else "")


# ------------------------------------------------------------------------------------------------
# GitHub API (GITHUB_TOKEN from Actions)
# ------------------------------------------------------------------------------------------------
class GitHub:
    def __init__(self, repo, token):
        self.repo, self.token = repo, token

    def call(self, method, path, data=None):
        url = path if path.startswith("https://") else f"https://api.github.com/repos/{self.repo}{path}"
        req = urllib.request.Request(url, method=method, data=json.dumps(data).encode() if data is not None else None)
        req.add_header("Authorization", f"Bearer {self.token}")
        req.add_header("Accept", "application/vnd.github+json")
        req.add_header("X-GitHub-Api-Version", "2022-11-28")
        try:
            with urllib.request.urlopen(req) as r:
                raw = r.read()
                return json.loads(raw) if raw else None
        except urllib.error.HTTPError as e:
            raise RuntimeError(f"{method} {path}: {e.code} {e.read().decode()[:300]}") from None

    def pages(self, path):
        out, page = [], 1
        sep = "&" if "?" in path else "?"
        while True:
            chunk = self.call("GET", f"{path}{sep}per_page=100&page={page}")
            out += chunk
            if len(chunk) < 100:
                return out
            page += 1


def status(gh, sha, context, state, desc, url=None):
    gh.call("POST", f"/statuses/{sha}", {"state": state, "context": context, "description": desc[:140],
                                        **({"target_url": url} if url else {})})


def set_tier_label(gh, n, labels, tier, policy):
    pre = policy["labels"]["tier_prefix"]
    want = f"{pre}{tier}"
    for l in labels:
        if l.startswith(pre) and l != want:
            gh.call("DELETE", f"/issues/{n}/labels/{l}")
    if want not in labels:
        gh.call("POST", f"/issues/{n}/labels", {"labels": [want]})


def gate(args, policy):
    gh = GitHub(os.environ["GITHUB_REPOSITORY"], os.environ["GITHUB_TOKEN"])
    run_url = os.environ.get("RUN_URL")
    n = args.pr
    pr = gh.call("GET", f"/pulls/{n}")
    if pr["state"] != "open":
        print("PR is not open; nothing to do."); return 0
    head = pr["head"]["sha"]
    if pr["head"]["repo"] is None or pr["head"]["repo"]["full_name"] != pr["base"]["repo"]["full_name"]:
        print("PR from a fork: the gate never merges it; Espen reviews it by hand."); return 0
    labels = [l["name"] for l in pr["labels"]]
    L = policy["labels"]
    comments = gh.pages(f"/issues/{n}/comments")
    mine = [c for c in comments if (c.get("user") or {}).get("type") == "Bot" and MARK in (c.get("body") or "")]
    sticky = mine[-1] if mine else None
    prev = json.loads(DATA.search(sticky["body"]).group(1)) if sticky and DATA.search(sticky["body"]) else {}

    cls = None
    if args.classification and os.path.exists(args.classification):
        with open(args.classification) as f:
            cls = json.load(f)
    elif prev.get("head") == head:
        cls = prev.get("classification")
    if not cls or cls.get("head") != head:
        status(gh, head, "merge-tier", "pending", "Waiting for rebuild-and-tests to classify this head", run_url)
        status(gh, head, "agent-review", "pending", "Waiting for rebuild-and-tests", run_url)
        print("No classification for the current head yet."); return 0

    # New commits after Espen's approval void it: they approved a specific version.
    events = gh.pages(f"/issues/{n}/events")
    for e in events:
        if (e.get("label") or {}).get("name") == L["espen_approved"]:
            print(f"{e['event']} {L['espen_approved']} at {e.get('created_at')} by {(e.get('actor') or {}).get('login')}, "
                  f"performed_via_github_app={(e.get('performed_via_github_app') or {}).get('slug')}")
    if args.event == "synchronize" and L["espen_approved"] in labels and label_added_before(events, L["espen_approved"], args.pushed_at):
        gh.call("DELETE", f"/issues/{n}/labels/{L['espen_approved']}")
        labels.remove(L["espen_approved"])
        events.append({"event": "unlabeled", "label": {"name": L["espen_approved"]}})
        gh.call("POST", f"/issues/{n}/comments", {"body": "New commits were pushed after `espen-approved` was added, so "
                "the label was removed. Espen: re-add it if you approve the current version.\n\n" + FOOTER_BOT})

    tier = cls["tier"]
    if L["needs_espen"] in labels:
        tier = 3
    espen_ok, espen_detail = espen_approval(events, policy)
    print(f"Espen approval: {espen_ok} ({espen_detail})")
    set_tier_label(gh, n, labels, tier, policy)

    if tier < 3:
        tier_state, tier_desc = "success", f"Tier {tier}: may merge after checks and an agent review"
    elif espen_ok:
        tier_state, tier_desc = "success", f"Tier 3: approved by Espen ({espen_detail})"
    else:
        tier_state, tier_desc = "failure", f"Tier 3: needs Espen. They add the label {L['espen_approved']} to approve ({espen_detail})"
    status(gh, head, "merge-tier", tier_state, tier_desc, run_url)

    author = pr_author(pr.get("body"), pr["head"]["ref"], policy)
    items = [{"body": c.get("body"), "created_at": c["created_at"], "user": c["user"]["login"],
              "app": (c.get("performed_via_github_app") or {}).get("slug")} for c in comments]
    for r in gh.pages(f"/pulls/{n}/reviews"):
        if r.get("body"):
            items.append({"body": r["body"], "created_at": r.get("submitted_at") or "", "user": r["user"]["login"],
                          "app": (r.get("performed_via_github_app") or {}).get("slug")})
    for it in items:
        if parse_review(it["body"]):
            print(f"review comment by {it['user']} at {it['created_at']}, performed_via_github_app={it['app']}: {parse_review(it['body'])}")
    rev_ok, rev_desc, approvals = evaluate_reviews(items, head, author, cls.get("owners", []), policy)
    if not rev_ok and tier == 3 and espen_ok:
        rev_ok, rev_desc = True, "Espen approved directly"
    if author[0] is None and not (tier == 3 and espen_ok):
        rev_ok, rev_desc = False, "unknown author: add 'Agent-Author: <agent> <session>' to the PR description"
    status(gh, head, "agent-review", "success" if rev_ok else "failure", rev_desc, run_url)

    base_now = gh.call("GET", f"/branches/{pr['base']['ref']}")["commit"]["sha"]
    ready, why_not = merge_ready(gh, pr, labels, tier_state, rev_ok, cls, base_now, policy)
    body = gate_comment(cls, tier, tier_desc, rev_desc, author, ready, why_not, head)
    data = {"head": head, "classification": cls, "tier": tier, "notified_tier3": prev.get("notified_tier3", False)}
    if tier == 3 and not espen_ok and not data["notified_tier3"] and not pr.get("draft"):
        gh.call("POST", f"/issues/{n}/comments", {"body": f"@{policy['espen_logins'][0]} this PR needs your decision "
                f"(tier 3). Reasons are in the gate comment. Add the label `{L['espen_approved']}` to approve the "
                "current version, or comment what should change.\n\n" + FOOTER_BOT})
        data["notified_tier3"] = True
    body += f"\n{MARK}\n<!-- agent-gate-data {json.dumps(data, separators=(',', ':'))} -->"
    if sticky:
        if sticky["body"] != body:
            gh.call("PATCH", f"/issues/comments/{sticky['id']}", {"body": body})
    else:
        gh.call("POST", f"/issues/{n}/comments", {"body": body})

    if ready:
        print(f"Merging #{n} at {head}")
        gh.call("PUT", f"/pulls/{n}/merge", {"merge_method": "merge", "sha": head,
                                             "commit_title": f"Merge PR #{n}: {pr['title']}"[:250],
                                             "commit_message": f"Tier {tier}; {rev_desc}. Merged by the agent gate."})
        if tier == 2:
            gh.call("POST", f"/issues/{n}/comments", {"body": f"@{policy['espen_logins'][0]} merged automatically as "
                    "tier 2 (auto-merge and notify). Headline numbers that moved:\n\n" + headline_table(cls) + "\n\n" + FOOTER_BOT})
    else:
        print(f"Not merging: {why_not}")
    return 0


FOOTER_BOT = "---\n_Posted by the Project 2050 agent gate (`.github/scripts/agent_gate.py`)._"


def merge_ready(gh, pr, labels, tier_state, rev_ok, cls, base_now, policy):
    if os.environ.get("AGENT_AUTOMERGE", "").lower() != "on":
        return False, "automatic merging is off (repository variable AGENT_AUTOMERGE is not 'on')"
    if pr.get("draft"):
        return False, "draft PR"
    if policy["labels"]["hold"] in labels:
        return False, "hold label"
    if tier_state != "success":
        return False, "tier gate not passed"
    if not rev_ok:
        return False, "agent review not passed"
    runs = gh.call("GET", f"/commits/{pr['head']['sha']}/check-runs?check_name=rebuild-and-tests")["check_runs"]
    runs.sort(key=lambda r: r.get("started_at") or "")
    if not runs or runs[-1].get("conclusion") != "success":
        return False, "rebuild-and-tests has not passed on this head"
    if cls.get("tested_base") and cls["tested_base"] != base_now:
        return False, (f"main moved since the checks ran (tested against {cls['tested_base'][:7]}, main is {base_now[:7]}); "
                       "merge main into this branch to re-run them")
    if pr.get("mergeable") is False:
        return False, "merge conflict"
    return True, ""


def headline_table(cls):
    rows = cls.get("headline_changes") or []
    if not rows:
        return "_No headline number moved._"
    out = ["| Headline | Base | This PR | Tier |", "| --- | --- | --- | --- |"]
    out += [f"| {n} | {fmt(b)} | {fmt(a)} | {t} |" for n, b, a, t in rows]
    return "\n".join(out)


def gate_comment(cls, tier, tier_desc, rev_desc, author, ready, why_not, head):
    names = {1: "auto-merge", 2: "auto-merge and notify Espen", 3: "Espen decides"}
    lines = [f"### Merge gate: tier {tier} ({names[tier]})", "",
             f"Head `{head[:7]}`; checked against main `{(cls.get('tested_base') or cls['base'])[:7]}`. "
             f"Author: {author[0] or 'unknown'} {author[1] or ''}".rstrip(), "",
             f"- **Tier:** {tier_desc}", f"- **Agent review:** {rev_desc}",
             f"- **Merge:** {'ready, merging now' if ready else why_not}", ""]
    top = sorted(cls["reasons"], key=lambda r: -r[1])[:25]
    lines += ["<details><summary>Why this tier</summary>", "", "| Path or headline | Tier | Reason |", "| --- | --- | --- |"]
    lines += [f"| `{p}` | {t} | {w} |" for p, t, w in top]
    if len(cls["reasons"]) > 25:
        lines.append(f"| ... {len(cls['reasons']) - 25} more | | |")
    lines += ["", "</details>", "", "**Headline numbers**", "", headline_table(cls), "",
              "To approve as another agent, comment with these three lines (current head):",
              "```", "Agent-Review: approve", f"Reviewed-Head: {head}", "Reviewer: <claude-code|codex|gemini> <session or task id>", "```",
              FOOTER_BOT]
    return "\n".join(lines)


# ------------------------------------------------------------------------------------------------
# Daily digest
# ------------------------------------------------------------------------------------------------
def digest(args, policy):
    gh = GitHub(os.environ["GITHUB_REPOSITORY"], os.environ["GITHUB_TOKEN"])
    now = datetime.now(timezone.utc)
    since = now - timedelta(hours=args.hours)
    iso = lambda t: datetime.fromisoformat(t.replace("Z", "+00:00"))
    L = policy["labels"]

    closed = gh.call("GET", "/pulls?state=closed&sort=updated&direction=desc&per_page=50")
    merged = [p for p in closed if p.get("merged_at") and iso(p["merged_at"]) >= since]
    opened = gh.pages("/pulls?state=open")
    waiting = [p for p in opened if {l["name"] for l in p["labels"]} & {f"{L['tier_prefix']}3", L["needs_espen"]}
               and L["espen_approved"] not in {l["name"] for l in p["labels"]}]
    issues = [i for i in gh.pages(f"/issues?state=open&labels={L['needs_espen']}") if "pull_request" not in i]

    old = git("rev-list", "-1", f"--before={since.isoformat()}", "HEAD").strip()
    moved = compare_headlines(headlines_at(old), headlines_at("HEAD"), policy) if old else []

    out = [f"## Agent digest, {now:%Y-%m-%d} (last {args.hours} hours)", ""]
    out += [f"### Merged ({len(merged)})", ""]
    for p in merged:
        tiers = [l["name"] for l in p["labels"] if l["name"].startswith(L["tier_prefix"])]
        out.append(f"- #{p['number']} {p['title']} ({', '.join(tiers) or 'no tier label'}; merged by {(p.get('merged_by') or {}).get('login', 'unknown')})")
    if not merged:
        out.append("- Nothing merged.")
    out += ["", f"### Waiting on Espen ({len(waiting) + len(issues)})", ""]
    out += [f"- PR #{p['number']} {p['title']}" for p in waiting]
    out += [f"- Issue #{i['number']} {i['title']}" for i in issues]
    if not waiting and not issues:
        out.append("- Nothing.")
    out += ["", "### Headline numbers that moved on main", ""]
    if moved:
        out += ["| Headline | Before | Now | Tier it implies |", "| --- | --- | --- | --- |"]
        out += [f"| {n} | {fmt(b)} | {fmt(a)} | {t} |" for n, b, a, t in moved]
    else:
        out.append(f"- None (main `{old[:7] if old else 'n/a'}` -> `{git('rev-parse', 'HEAD').strip()[:7]}`).")
    out += ["", f"Open PRs: {len(opened)}. Rules: governing/project-collaboration.md.", "", FOOTER_BOT]
    text = "\n".join(out)
    print(text)
    if args.dry_run:
        return 0

    found = [i for i in gh.pages("/issues?state=open&labels=agent-digest") if "pull_request" not in i]
    body = f"{DIGEST_MARK}\nThis issue is rewritten every day by `.github/workflows/daily-digest.yml`. " \
           "Each day with news also adds a comment, which is what sends a notification.\n\n" + text
    if found:
        num = found[0]["number"]
        gh.call("PATCH", f"/issues/{num}", {"body": body})
    else:
        num = gh.call("POST", "/issues", {"title": "Daily agent digest", "body": body, "labels": ["agent-digest"]})["number"]
    if merged or waiting or issues or moved:
        gh.call("POST", f"/issues/{num}/comments", {"body": text})
    return 0


# ------------------------------------------------------------------------------------------------
def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    c = sub.add_parser("classify"); c.add_argument("--base", required=True); c.add_argument("--head", required=True)
    c.add_argument("--tested-base"); c.add_argument("--out")
    h = sub.add_parser("headlines"); h.add_argument("--rev")
    g = sub.add_parser("gate"); g.add_argument("--pr", type=int, required=True); g.add_argument("--classification")
    g.add_argument("--event", default="")
    g.add_argument("--pushed-at", default="", help="time of the push that triggered a synchronize event")
    d = sub.add_parser("digest"); d.add_argument("--hours", type=int, default=24); d.add_argument("--dry-run", action="store_true")
    args = ap.parse_args(argv)
    policy = load_policy()
    if args.cmd == "classify":
        res = classify(args.base, args.head, policy)
        res["tested_base"] = args.tested_base
        text = json.dumps(res, indent=1)
        if args.out:
            with open(args.out, "w") as f:
                f.write(text)
        print(f"Tier {res['tier']} ({res['files']} files)")
        for p, t, w in sorted(res["reasons"], key=lambda r: -r[1]):
            print(f"  {t}  {p}: {w}")
        return 0
    if args.cmd == "headlines":
        print(json.dumps(headlines_at(args.rev), indent=1))
        return 0
    if args.cmd == "gate":
        return gate(args, policy)
    return digest(args, policy)


if __name__ == "__main__":
    sys.exit(main())
