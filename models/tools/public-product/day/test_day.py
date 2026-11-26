#!/usr/bin/env python3
"""Tests for the front door's content builder and the docs pages (stage H step H8).

Each test breaks one rule on a copy of the content and checks the builder catches it, so a later edit that
weakens a check fails here. Standard library only.

  python3 models/tools/public-product/day/test_day.py
"""
import copy
import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE.parent / 'docs'))
import build_day as B  # noqa: E402
import build_docs as D  # noqa: E402


def scene(content, sid):
    return next(s for s in content['scenes'] if s['id'] == sid)


def moment(content, fid, sid):
    fam = next(f for f in content['families'] if f['id'] == fid)
    return next(m for m in fam['moments'] if m['scene'] == sid)


class Content(unittest.TestCase):
    def setUp(self):
        self.content = B.load()
        self.lock = B.read_lock()

    def problems(self, content):
        return B.validate(content)

    def test_committed_content_traces(self):
        self.assertEqual(self.problems(self.content), [])
        self.assertEqual(B.lock_problems(self.content, self.lock), [])

    def test_committed_preview_is_current(self):
        outputs = B.render(self.content, self.lock)
        for name in B.OUTPUTS:
            self.assertEqual((B.PREVIEW / name).read_text(encoding='utf-8'), outputs[name], name)

    def test_untraced_figure_fails(self):
        c = copy.deepcopy(self.content)
        moment(c, 'maya-sam', 'floor')['beats'][0]['text'] += ' It is $999 a month.'
        self.assertTrue(any('figures without a cited claim' in p and '999' in p for p in self.problems(c)))

    def test_figure_missing_from_its_passage_fails(self):
        c = copy.deepcopy(self.content)
        c['claims']['leave-cost']['figures'].append('$181')
        self.assertTrue(any("claim leave-cost: figure '$181' not in its anchors" in p for p in self.problems(c)))

    def test_source_outside_sections_1_to_8_fails(self):
        c = copy.deepcopy(self.content)
        c['claims']['leave-cost']['sources'][0]['path'] = 'dossiers/secure-floor/9-public-case.md'
        self.assertTrue(any('not a dossier section 1-8 file' in p for p in self.problems(c)))
        c['claims']['leave-cost']['sources'][0]['path'] = 'dossiers/foundations/fair-financing/memos/G21-debt-limit.md'
        self.assertTrue(any('not a dossier section 1-8 file' in p for p in self.problems(c)))

    def test_banned_phrase_fails_unless_negated(self):
        c = copy.deepcopy(self.content)
        scene(c, 'money')['detail']['limits'].append('The plan pays for itself.')
        self.assertTrue(any("banned phrase 'pays for itself'" in p for p in self.problems(c)))
        c = copy.deepcopy(self.content)
        scene(c, 'money')['detail']['limits'].append('It is not an official score.')
        self.assertFalse(any('banned phrase' in p for p in self.problems(c)))

    def test_estimate_must_be_worded_as_one(self):
        c = copy.deepcopy(self.content)
        d = scene(c, 'floor')['detail']
        d['cost'][0] = d['cost'][0].replace('On our estimates the', 'The').replace('about ', '')
        self.assertTrue(any('scene floor cost 1: cites an estimate' in p for p in self.problems(c)))

    def test_titles_and_placeholders_carry_no_figures(self):
        c = copy.deepcopy(self.content)
        scene(c, 'money')['detail']['placeholders'][0]['text'] += ' About 117% of GDP.'
        self.assertTrue(any('placeholder fund-rate' in p for p in self.problems(c)))
        c = copy.deepcopy(self.content)
        moment(c, 'jordan', 'clinic')['title'] = 'Covered since 2031'
        self.assertTrue(any('jordan clinic title' in p for p in self.problems(c)))
        c = copy.deepcopy(self.content)
        c['families'][0]['about'] = 'A man of 25.'
        self.assertTrue(any('family jordan' in p for p in self.problems(c)))

    def test_every_moment_has_a_beat_for_its_family(self):
        c = copy.deepcopy(self.content)
        m = moment(c, 'jordan', 'immigration')
        m['beats'] = [b for b in m['beats'] if b['person'] is None]
        self.assertTrue(any('jordan immigration: no beat for a member of the jordan family' in p for p in self.problems(c)))

    def test_every_family_ends_on_the_money_and_every_scene_is_met(self):
        c = copy.deepcopy(self.content)
        c['families'][1]['moments'] = [m for m in c['families'][1]['moments'] if m['scene'] != 'money']
        self.assertTrue(any('family maya-sam: its day must end on the money' in p for p in self.problems(c)))
        c = copy.deepcopy(self.content)
        for f in c['families']:
            f['moments'] = [m for m in f['moments'] if m['scene'] != 'childcare']
        self.assertTrue(any('scene childcare: no family meets it' in p for p in self.problems(c)))

    def test_scenes_need_dates_limits_and_questions(self):
        c = copy.deepcopy(self.content)
        scene(c, 'power')['detail']['limits'] = []
        self.assertTrue(any('scene power: needs at least one item under limits' in p for p in self.problems(c)))

    def test_unused_claim_fails(self):
        c = copy.deepcopy(self.content)
        c['claims']['spare'] = dict(c['claims']['leave-cost'])
        self.assertTrue(any('claims not used' in p and 'spare' in p for p in self.problems(c)))


class Families(unittest.TestCase):
    def setUp(self):
        self.content = B.load()

    def test_three_families_and_a_chooser(self):
        """DEC-2026-11-25-23: three families, with a way to choose whose day you read."""
        self.assertEqual([f['id'] for f in self.content['families']], ['jordan', 'maya-sam', 'carol-dev'])
        page = B.render(self.content, B.read_lock())['day.html']
        self.assertIn('aria-label="Choose a family"', page)
        for f in self.content['families']:
            self.assertIn(f'<a href="#{f["id"]}">', page)
            self.assertIn(f'<article class="family" id="{f["id"]}"', page)

    def test_one_family_and_the_money_last(self):
        days, money, _ = B.arrange(self.content, family='carol-dev')
        self.assertEqual([f['id'] for f, _ in days], ['carol-dev'])
        self.assertEqual(days[0][1][-1]['scene'], 'money')
        people = self.content['people']
        for m in days[0][1]:
            self.assertTrue(any(b['person'] and people[b['person']]['family'] == 'carol-dev' for b in m['beats']))

    def test_money_position_and_optional_scenes(self):
        first, *_ = B.arrange(self.content, money='first')
        last, *_ = B.arrange(self.content, money='last')
        for (_, a), (_, b) in zip(first, last):
            self.assertEqual(a[0]['scene'], 'money')
            self.assertEqual(b[-1]['scene'], 'money')
        without, *_ = B.arrange(self.content, optional={'transportation': False})
        self.assertFalse(any(m['scene'] == 'transit' for _, day in without for m in day))
        self.assertTrue(scene(self.content, 'transit').get('optional'))  # DEC-2026-11-25-24

    def test_placeholders_render_and_figures_do_not_leak(self):
        page = B.render(self.content, B.read_lock())['day.html']
        for ph in scene(self.content, 'money')['detail']['placeholders']:
            self.assertIn(f'data-placeholder="{ph["id"]}"', page)
            self.assertNotIn(ph['waits_on'], page)  # what it waits on is for the register, not the reader

    def test_evidence_note_ids_are_unique(self):
        import re
        page = B.render(self.content, B.read_lock())['day.html']
        ids = re.findall(r' id="([^"]+)"', page)
        self.assertEqual(len(ids), len(set(ids)))


class PinAndDrift(unittest.TestCase):
    def setUp(self):
        self.content = B.load()
        self.lock = B.read_lock()

    def test_build_never_reads_git_history(self):
        """The check runs from a shallow clone: with Git unavailable it still builds from the lock."""
        def no_git(*a, **k):
            raise AssertionError('the build called git')
        with mock.patch.object(B.subprocess, 'check_output', no_git), mock.patch.object(B.subprocess, 'check_call', no_git):
            outputs, gone, changed = B.build(self.content, self.lock, strict=False)
        self.assertIn('day.html', outputs)

    def test_lock_must_cover_every_passage(self):
        c = copy.deepcopy(self.content)
        c['claims']['leave-cost']['sources'].append({'path': 'dossiers/secure-floor/6-cost.md', 'anchor': 'a new passage here'})
        self.assertTrue(B.lock_problems(c, self.lock))

    def test_drift_is_reported_not_fatal_in_report_mode(self):
        tmp = Path(tempfile.mkdtemp())
        try:
            for path in self.lock['blobs']:
                dest = tmp / path
                dest.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy(B.ROOT / path, dest)
            gone, changed = B.drift(self.content, self.lock, tmp)
            self.assertEqual(gone, [])
            target = tmp / self.content['claims']['leave-cost']['sources'][0]['path']
            anchor = self.content['claims']['leave-cost']['sources'][0]['anchor']
            target.write_text(target.read_text().replace(anchor, 'rewritten'))
            gone, changed = B.drift(self.content, self.lock, tmp)
            self.assertTrue(any('claim leave-cost' in g for g in gone))
            self.assertIn(str(target.relative_to(tmp)), changed)
        finally:
            shutil.rmtree(tmp)

    def test_blob_hash_matches_git(self):
        path = next(iter(self.lock['blobs']))
        try:
            expected = subprocess.check_output(['git', 'hash-object', str(B.ROOT / path)], cwd=B.ROOT).decode().strip()
        except (OSError, subprocess.CalledProcessError):
            self.skipTest('git not available')
        self.assertEqual(B.blob_hash((B.ROOT / path).read_bytes()), expected)

    def test_stale_preview_fails_the_check(self):
        tmp = Path(tempfile.mkdtemp())
        try:
            for name in B.OUTPUTS:
                shutil.copy(B.PREVIEW / name, tmp / name)
            (tmp / 'day.html').write_text('edited by hand')
            with mock.patch.object(B, 'PREVIEW', tmp):
                self.assertEqual(B.main(['--report']), 1)
        finally:
            shutil.rmtree(tmp)


class Docs(unittest.TestCase):
    def test_every_model_gets_a_whole_page(self):
        rows, pages = D.build_all()
        self.assertEqual(D.check(pages, rows), [])
        self.assertEqual(len(rows) + 1, len(pages))
        self.assertIn('MOD-health-coverage', pages['index.html'])

    def test_pages_follow_their_files(self):
        """A page is generated from the card at build time, so an edit to the card shows up: nothing to drift."""
        rows, pages = D.build_all()
        hc = next(r for r in rows if r['model_id'] == 'MOD-health-coverage')
        card = (D.ROOT / hc['card']).read_text()
        with mock.patch.object(Path, 'read_text', lambda self, *a, **k: (card + '\n\nA new line, added.') if self.name == 'MODEL-CARD.md' and 'health-coverage' in str(self) else Path.read_bytes(self).decode()):
            page = D.model_page(hc, D.read_csv(D.ROOT / 'models' / 'release-criteria.csv'), [])
        self.assertIn('A new line, added.', page)

    def test_day_page_links_only_to_generated_docs(self):
        _, pages = D.build_all()
        content = B.load()
        for s in content['scenes']:
            for m in s['detail'].get('models', []):
                self.assertIn(f'{m}.html', pages)


if __name__ == '__main__':
    unittest.main(verbosity=1)
