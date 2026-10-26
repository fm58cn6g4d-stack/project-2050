#!/usr/bin/env python3
"""Tests for the merge gate's tier rules, review parsing and Espen-approval check (standard library only)."""
import json
import os
import shutil
import subprocess
import sys
import tempfile
import unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import agent_gate as g  # noqa: E402

POLICY = g.load_policy()
HEAD = "a" * 40


def item(body, t="2026-10-26T12:00:00Z", user="fm58cn6g4d-stack", app=None):
    return {"body": body, "created_at": t, "user": user, "app": app}


def review(verdict="approve", head=HEAD, who="codex task-1"):
    return f"Looks fine.\n\nAgent-Review: {verdict}\nReviewed-Head: {head}\nReviewer: {who}\n"


class Wording(unittest.TestCase):
    def test_wording_fix(self):
        self.assertTrue(g.wording_only(["The surge is $105B for CAP-7S."], ["The rebuild surge is $105B for CAP-7S."]))

    def test_number_change_is_not_wording(self):
        self.assertFalse(g.wording_only(["The surge is $105B."], ["The surge is $110B."]))

    def test_id_change_is_not_wording(self):
        self.assertFalse(g.wording_only(["See HLT-2."], ["See HLT-3."]))

    def test_program_ids(self):
        self.assertEqual(g.program_ids("CAP-7S and DEV-P and SS-5, not FY2029 or D4-B"), {"CAP-7S", "SS-5", "DEV-P"})


class Rules(unittest.TestCase):
    def tier(self, path):
        return g.match_rule(path, POLICY)["tier"]

    def test_paths(self):
        self.assertEqual(self.tier("governing/project-collaboration.md"), 3)
        self.assertEqual(self.tier("index/data/inputs/recovery-adoption.json"), 3)
        self.assertEqual(self.tier(".github/workflows/pr-checks.yml"), 3)
        self.assertEqual(self.tier("AGENTS.md"), 3)
        self.assertEqual(self.tier("sources/project-work-queue.md"), 1)
        self.assertEqual(self.tier("sources/capacity-recovery-budget-review.md"), 1)
        self.assertEqual(self.tier("index/tools/capacity-review/review.py"), 1)
        self.assertEqual(self.tier("domains/domain-health.md"), "domain")
        self.assertEqual(self.tier("something/new.txt"), 2)

    def test_generated_and_owners(self):
        self.assertTrue(g.is_generated("index/data/dashboard/bills.json", POLICY))
        self.assertTrue(g.is_generated("index/recovery-budget.md", POLICY))
        self.assertFalse(g.is_generated("index/options-register.md", POLICY))
        self.assertEqual(g.owners_of("index/tools/recovery-budget/model.py", POLICY), {"codex"})
        self.assertEqual(g.owners_of("sources/climate-portfolio-allocation.md", POLICY), {"claude-code"})


class Headlines(unittest.TestCase):
    def test_current_files_parse(self):
        h = g.headlines_at()
        self.assertTrue(any(k.startswith("margin:D4 general-fund balance FY2040") for k in h), h)
        self.assertFalse(any("unreadable" in str(v) for v in h.values()), h)

    def test_tiers(self):
        base = {"num:debt": 100.0, "margin:m": 0.10, "test:t": True}
        self.assertEqual(g.compare_headlines(base, dict(base), POLICY), [])
        small = g.compare_headlines(base, {**base, "num:debt": 100.5}, POLICY)
        self.assertEqual([r[3] for r in small], [2])
        big = g.compare_headlines(base, {**base, "num:debt": 102.0}, POLICY)
        self.assertEqual([r[3] for r in big], [3])
        self.assertEqual(g.compare_headlines(base, {**base, "margin:m": 0.12}, POLICY)[0][3], 3)
        self.assertEqual(g.compare_headlines(base, {**base, "margin:m": 0.101}, POLICY)[0][3], 2)
        self.assertEqual(g.compare_headlines(base, {**base, "test:t": False}, POLICY)[0][3], 3)
        self.assertEqual(g.compare_headlines(base, {"num:debt": 100.0, "margin:m": 0.10}, POLICY)[0][3], 3)


class Reviews(unittest.TestCase):
    author = ("claude-code", "session_A")

    def ev(self, items, owners=()):
        return g.evaluate_reviews(items, HEAD, self.author, list(owners), POLICY)

    def test_other_vendor_approves_current_head(self):
        self.assertTrue(self.ev([item(review(), app="chatgpt-codex-connector")])[0])

    def test_review_must_come_through_claimed_agents_app(self):
        # Claude Code posts through the 'claude' app; a Claude session cannot pass itself off as Codex.
        self.assertTrue(self.ev([item(review(who="claude-code session_B"), app="claude")])[0])
        self.assertFalse(self.ev([item(review(who="claude-code session_B"), app=None)])[0])
        self.assertFalse(self.ev([item(review(who="codex t1"), app="claude")])[0])

    def test_stale_head_does_not_count(self):
        self.assertFalse(self.ev([item(review(head="b" * 40), app="chatgpt-codex-connector")])[0])

    def test_changes_requested_on_older_head_still_blocks(self):
        old = item(review("changes-requested", head="b" * 40), t="2026-10-26T12:00:00Z", app="chatgpt-codex-connector")
        other = item(review(who="claude-code session_B"), t="2026-10-26T13:00:00Z", app="claude")
        ok, why, _ = self.ev([old, other])
        self.assertFalse(ok)
        self.assertIn("codex", why)
        again = item(review(), t="2026-10-26T14:00:00Z", app="chatgpt-codex-connector")
        self.assertTrue(self.ev([old, other, again])[0])

    def test_codex_must_post_through_its_connector(self):
        self.assertFalse(self.ev([item(review(), app=None)])[0])
        self.assertFalse(self.ev([item(review(), app="claude")])[0])

    def test_short_sha_prefix_counts(self):
        self.assertTrue(self.ev([item(review(head=HEAD[:12]), app="chatgpt-codex-connector")])[0])

    def test_author_cannot_self_review(self):
        self.assertFalse(self.ev([item(review(who="claude-code session_A"))])[0])
        self.assertFalse(self.ev([item(review(who="claude-code"))])[0])

    def test_other_session_same_vendor(self):
        self.assertTrue(self.ev([item(review(who="claude-code session_B"), app="claude")])[0])

    def test_changes_requested_blocks_until_reapproved(self):
        a = item(review(), t="2026-10-26T12:00:00Z", app="chatgpt-codex-connector")
        b = item(review("changes-requested"), t="2026-10-26T13:00:00Z", app="chatgpt-codex-connector")
        c = item(review(), t="2026-10-26T14:00:00Z", app="chatgpt-codex-connector")
        self.assertFalse(self.ev([a, b])[0])
        self.assertTrue(self.ev([a, b, c])[0])

    def test_outsider_comment_ignored(self):
        self.assertFalse(self.ev([item(review(), user="someone-else", app="chatgpt-codex-connector")])[0])

    def test_path_owner_must_review(self):
        ok, why, _ = self.ev([item(review(who="claude-code session_B"), app="claude")], owners=["codex"])
        self.assertFalse(ok)
        self.assertIn("codex", why)
        self.assertTrue(self.ev([item(review(who="codex t1"), app="chatgpt-codex-connector")], owners=["codex"])[0])

    def test_author_from_body_or_branch(self):
        self.assertEqual(g.pr_author("x\nAgent-Author: codex task-9\n", "whatever", POLICY), ("codex", "task-9"))
        self.assertEqual(g.pr_author("", "claude/agent-automation", POLICY), ("claude-code", None))
        self.assertEqual(g.pr_author("", "feature/x", POLICY), (None, None))


class EspenApproval(unittest.TestCase):
    def ev(self, actor="fm58cn6g4d-stack", app=None, event="labeled"):
        return {"event": event, "label": {"name": "espen-approved"}, "actor": {"login": actor},
                "performed_via_github_app": {"slug": app} if app else None}

    def test_direct_label(self):
        self.assertTrue(g.espen_approval([self.ev()], POLICY)[0])

    def test_label_via_agent_app_rejected(self):
        self.assertFalse(g.espen_approval([self.ev(app="claude")], POLICY)[0])

    def test_other_actor_rejected(self):
        self.assertFalse(g.espen_approval([self.ev(actor="someone")], POLICY)[0])

    def test_removed_label(self):
        self.assertFalse(g.espen_approval([self.ev(), self.ev(event="unlabeled")], POLICY)[0])


class LabelTiming(unittest.TestCase):
    def test_label_before_and_after_push(self):
        ev = [{"event": "labeled", "label": {"name": "espen-approved"}, "created_at": "2026-10-26T16:20:00Z"}]
        self.assertTrue(g.label_added_before(ev, "espen-approved", "2026-10-26T16:21:00Z"))
        self.assertFalse(g.label_added_before(ev, "espen-approved", "2026-10-26T16:19:00Z"))
        self.assertFalse(g.label_added_before([], "espen-approved", "2026-10-26T16:19:00Z"))


class FakeGitHub:
    """Answers the digest's API calls from fixed data and records writes."""
    def __init__(self, repo, token):
        self.writes = []
        FakeGitHub.last = self

    def call(self, method, path, data=None):
        if method != "GET":
            self.writes.append((method, path, data))
            return {"number": 99}
        if path.startswith("/pulls?state=closed"):
            return [{"number": 30, "title": "Wording fix", "merged_at": "2999-01-01T00:00:00Z",
                     "labels": [{"name": "tier-1"}], "merged_by": {"login": "github-actions[bot]"}},
                    {"number": 29, "title": "Old", "merged_at": "2000-01-01T00:00:00Z", "labels": []}]
        raise AssertionError(path)

    def pages(self, path):
        if path.startswith("/pulls?state=open"):
            return [{"number": 31, "title": "Adopt new input", "labels": [{"name": "tier-3"}]},
                    {"number": 32, "title": "Approved", "labels": [{"name": "tier-3"}, {"name": "espen-approved"}]}]
        if "labels=needs-espen" in path:
            return [{"number": 40, "title": "Choose a surge size"}]
        if "labels=agent-digest" in path:
            return []
        raise AssertionError(path)


class Retry(unittest.TestCase):
    def setUp(self):
        import urllib.request
        self.urlopen, self.delays = urllib.request.urlopen, g.RETRY_DELAYS
        g.RETRY_DELAYS = (0, 0)

    def tearDown(self):
        import urllib.request
        urllib.request.urlopen, g.RETRY_DELAYS = self.urlopen, self.delays

    def fake(self, codes):
        import io, urllib.error, urllib.request
        calls = []

        class Resp(io.BytesIO):
            def __enter__(self): return self
            def __exit__(self, *a): return False

        def urlopen(req):
            calls.append(1)
            code = codes[len(calls) - 1]
            if code != 200:
                raise urllib.error.HTTPError(req.full_url, code, "err", {}, io.BytesIO(b"{}"))
            return Resp(b'{"ok": true}')
        urllib.request.urlopen = urlopen
        return calls

    def test_retries_server_errors_then_succeeds(self):
        calls = self.fake([502, 503, 200])
        self.assertEqual(g.GitHub("o/r", "t").call("GET", "/pulls/1"), {"ok": True})
        self.assertEqual(len(calls), 3)

    def test_gives_up_after_retries(self):
        self.fake([502, 502, 502])
        with self.assertRaises(RuntimeError):
            g.GitHub("o/r", "t").call("GET", "/pulls/1")

    def test_client_errors_are_not_retried(self):
        calls = self.fake([404])
        with self.assertRaises(RuntimeError):
            g.GitHub("o/r", "t").call("GET", "/pulls/1")
        self.assertEqual(len(calls), 1)


class MergePatience(unittest.TestCase):
    class GH:
        def __init__(self, errors):
            self.errors, self.calls = list(errors), 0

        def call(self, method, path, data=None):
            self.calls += 1
            if self.errors:
                raise RuntimeError(self.errors.pop(0))
            return {"merged": True}

    PENDING = 'PUT /pulls/1/merge: 405 {"message":"Repository rule violations found 2 of 3 required status checks are pending."}'

    def test_waits_for_statuses_to_register(self):
        gh = self.GH([self.PENDING, self.PENDING])
        self.assertEqual(g.merge_with_patience(gh, 1, {}, delays=(0, 0, 0)), {"merged": True})
        self.assertEqual(gh.calls, 3)

    def test_other_refusals_fail_at_once(self):
        gh = self.GH(['PUT /pulls/1/merge: 405 {"message":"Pull Request is not mergeable"}'])
        with self.assertRaises(RuntimeError):
            g.merge_with_patience(gh, 1, {}, delays=(0, 0))
        self.assertEqual(gh.calls, 1)


class Digest(unittest.TestCase):
    def test_digest_lists_merged_and_waiting(self):
        old, os.environ["GITHUB_REPOSITORY"], os.environ["GITHUB_TOKEN"] = g.GitHub, "o/r", "x"
        g.GitHub = FakeGitHub
        try:
            import argparse, contextlib, io
            out = io.StringIO()
            with contextlib.redirect_stdout(out):
                g.digest(argparse.Namespace(hours=24, dry_run=False), POLICY)
        finally:
            g.GitHub = old
        text = out.getvalue()
        self.assertIn("#30 Wording fix", text)
        self.assertNotIn("#29", text)
        self.assertIn("PR #31", text)
        self.assertNotIn("PR #32", text)
        self.assertIn("Issue #40", text)
        writes = FakeGitHub.last.writes
        self.assertEqual(writes[0][1], "/issues")          # creates the digest issue
        self.assertEqual(writes[1][1], "/issues/99/comments")  # and comments because there is news


class Classify(unittest.TestCase):
    """Runs classify() on a scratch git repository."""

    def setUp(self):
        self.tmp = tempfile.mkdtemp()
        self.old_root = g.ROOT
        g.ROOT = self.tmp
        g._DOMAIN_IDS.clear()
        self.git("init", "-q", "-b", "main")
        self.git("config", "user.email", "t@example.com"); self.git("config", "user.name", "t")
        self.write("domains/domain-x.md", "# X\n\nHLT-1 costs $10B. The plan is good.\n")
        self.write("sources/notes.md", "Research note.\n")
        self.write("governing/rules.md", "Rule.\n")
        self.commit("base")
        self.base = self.git("rev-parse", "HEAD").strip()

    def tearDown(self):
        g.ROOT = self.old_root
        shutil.rmtree(self.tmp)

    def git(self, *a):
        return subprocess.run(["git", *a], cwd=self.tmp, capture_output=True, text=True, check=True).stdout

    def write(self, path, text):
        p = os.path.join(self.tmp, path)
        os.makedirs(os.path.dirname(p), exist_ok=True)
        with open(p, "w") as f:
            f.write(text)

    def commit(self, msg):
        self.git("add", "-A"); self.git("commit", "-qm", msg)
        return self.git("rev-parse", "HEAD").strip()

    def test_research_is_tier1(self):
        self.write("sources/notes.md", "Research note, expanded with 3 sources.\n")
        self.assertEqual(g.classify(self.base, self.commit("s"), POLICY)["tier"], 1)

    def test_domain_wording_is_tier1(self):
        self.write("domains/domain-x.md", "# X\n\nHLT-1 costs $10B. The plan works.\n")
        self.assertEqual(g.classify(self.base, self.commit("d"), POLICY)["tier"], 1)

    def test_domain_number_is_tier2(self):
        self.write("domains/domain-x.md", "# X\n\nHLT-1 costs $12B. The plan is good.\n")
        self.assertEqual(g.classify(self.base, self.commit("d"), POLICY)["tier"], 2)

    def test_new_program_is_tier3(self):
        self.write("domains/domain-x.md", "# X\n\nHLT-1 costs $10B. HLT-9 is new. The plan is good.\n")
        res = g.classify(self.base, self.commit("d"), POLICY)
        self.assertEqual(res["tier"], 3)
        self.assertTrue(any("+HLT-9" in r[2] for r in res["reasons"]))

    def test_citing_existing_program_is_not_new(self):
        self.write("domains/domain-y.md", "# Y\n\nNothing yet.\n")
        base = self.commit("y")
        self.write("domains/domain-y.md", "# Y\n\nWorks with HLT-1.\n")
        self.assertEqual(g.classify(base, self.commit("cite"), POLICY)["tier"], 2)

    def test_removed_program_is_tier3(self):
        self.write("domains/domain-x.md", "# X\n\nThe plan is good.\n")
        self.assertEqual(g.classify(self.base, self.commit("rm"), POLICY)["tier"], 3)

    def test_governing_is_tier3(self):
        self.write("governing/rules.md", "Rule, reworded.\n")
        self.assertEqual(g.classify(self.base, self.commit("g"), POLICY)["tier"], 3)


if __name__ == "__main__":
    unittest.main(verbosity=1)
