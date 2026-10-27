#!/usr/bin/env python3
"""Tests for the public story page: claim tracing, page structure and editorial boundaries."""
import copy
import json
import os
import re
import shutil
import sys
import tempfile
import unittest
from html.parser import HTMLParser
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import build_story as story  # noqa: E402


class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.tags, self.ids, self.hrefs, self.text = [], set(), [], []
        self.skip = 0

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        self.tags.append((tag, a))
        if 'id' in a:
            self.ids.add(a['id'])
        if tag == 'a' and 'href' in a:
            self.hrefs.append(a['href'])
        if tag in ('style', 'script'):
            self.skip += 1

    def handle_endtag(self, tag):
        if tag in ('style', 'script'):
            self.skip -= 1

    def handle_data(self, data):
        if not self.skip:
            self.text.append(data)


# The common runner sets this so that a later edit to a cited source is reported for editorial review
# (build_story.py --report) instead of failing every other pull request.
REPORT_ONLY = os.environ.get('PUBLIC_STORY_REPORT_ONLY') == '1'


def problems_for(content, root=story.ROOT):
    return story.validate(content, root)[1]


class StoryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.content = story.load()
        cls.outputs, cls.live_problems = story.build(cls.content, strict=not REPORT_ONLY)
        cls.html = cls.outputs[story.OUT / 'story.html'].decode()
        cls.page = Page()
        cls.page.feed(cls.html)

    @unittest.skipIf(REPORT_ONLY, 'source drift is reported by build_story.py --report')
    def test_every_claim_traces_to_current_sources(self):
        self.assertEqual(self.live_problems, [])

    def test_committed_outputs_match_the_build(self):
        for path, data in self.outputs.items():
            self.assertEqual(path.read_bytes(), data, f'{path} is stale; run build_story.py')

    def test_essay_count_and_reading_order(self):
        essays = self.content['essays']
        self.assertTrue(5 <= len(essays) <= 8)
        toc = [h[1:] for h in self.page.hrefs if h.startswith('#')]
        self.assertEqual([e['id'] for e in essays], [t for t in dict.fromkeys(toc) if t in {e['id'] for e in essays}])

    def test_essay_length(self):
        for essay in self.content['essays']:
            words = len(story.strip_marks(' '.join(essay['body'])).split())
            self.assertTrue(550 <= words <= 1000, f'{essay["id"]} has {words} words')

    def test_every_number_in_prose_is_cited(self):
        content = copy.deepcopy(self.content)
        content['essays'][0]['body'][0] += ' About 40 million people live this way.'
        self.assertTrue(any('figures without a cited claim' in p and "'40'" in p for p in problems_for(content)))
        content = copy.deepcopy(self.content)
        content['essays'][3]['diagrams'][0]['caption'] += ' Costs reach $9B.'
        self.assertTrue(any('diagram' in p and "'9'" in p for p in problems_for(content)))

    def test_cited_claim_must_carry_the_figure(self):
        content = copy.deepcopy(self.content)
        content['essays'][1]['body'][0] = content['essays'][1]['body'][0].replace('2.3 million', '2.8 million')
        self.assertTrue(any("'2.8'" in p for p in problems_for(content)))

    def test_claim_figure_must_be_in_its_source_passage(self):
        content = copy.deepcopy(self.content)
        content['claims']['hou4a']['figures'].append('300,000')
        self.assertTrue(any('hou4a' in p and '300,000' in p for p in problems_for(content)))

    def test_rounded_figures_follow_from_raw_values(self):
        content = copy.deepcopy(self.content)
        content['claims']['poverty']['rounded'][0]['figure'] = '13.9%'
        self.assertTrue(any('rounded figure' in p for p in problems_for(content)))

    def test_a_moved_source_passage_stops_the_build(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            paths = {s['path'] for c in self.content['claims'].values() for s in c['sources']}
            paths |= {p['path'] for p in self.content['policies'].values()}
            for path in paths:
                (root / path).parent.mkdir(parents=True, exist_ok=True)
                shutil.copy(story.ROOT / path, root / path)
            before = problems_for(self.content, root)
            self.assertFalse(any(p.startswith('claim hou4a:') for p in before))
            housing = root / 'domains/domain-housing.md'
            housing.write_text(housing.read_text().replace('implying 250,000 new awards annually', 'implying 200,000 new awards annually'))
            problems = problems_for(self.content, root)
            self.assertTrue(any(p.startswith('claim hou4a: anchor not found') for p in problems))
            with self.assertRaises(story.ClaimError):
                story.build(self.content, root)
            # Report mode still builds, from the pinned lines, so the page is unchanged until an editor reviews it.
            outputs, _ = story.build(self.content, root, strict=False)
            self.assertEqual(outputs[story.OUT / 'story.html'], self.outputs[story.OUT / 'story.html'])

    def test_unknown_references_are_rejected(self):
        content = copy.deepcopy(self.content)
        content['essays'][2]['policy_ids'].append('LAB-99')
        content['essays'][2]['body'][1] += ' {c:no-such-claim}'
        problems = problems_for(content)
        self.assertTrue(any('unknown policy LAB-99' in p for p in problems))
        self.assertTrue(any('unknown claim no-such-claim' in p for p in problems))

    def test_every_claim_is_used_and_registered_with_lines(self):
        register = json.loads(self.outputs[story.OUT / 'story-claims.json'])
        self.assertEqual(set(register['claims']), set(self.content['claims']))
        for cid, claim in register['claims'].items():
            self.assertTrue(claim['essays'], cid)
            self.assertTrue(all(isinstance(s['line'], int) for s in claim['sources']), cid)
            self.assertIn(claim['basis'], self.content['basis_labels'])
        self.assertTrue(register['left_out'])

    def test_note_links_resolve_and_each_essay_has_notes(self):
        for href in self.page.hrefs:
            if href.startswith('#'):
                self.assertIn(href[1:], self.page.ids, href)
        for essay in self.content['essays']:
            self.assertIn(f'{essay["id"]}-n1', self.page.ids)

    def test_headings_landmarks_and_fiction_labels(self):
        tags = [t for t, _ in self.page.tags]
        self.assertEqual(tags.count('h1'), 1)
        self.assertEqual(tags.count('main'), 1)
        self.assertEqual(self.html.count('class="fiction">Imagined scene</span>'), len(self.content['essays']))
        art = [a for t, a in self.page.tags if t == 'svg' and a.get('aria-label', '').startswith('Imagined scene:')]
        self.assertEqual(len(art), len(self.content['essays']))
        self.assertIn('lang="en"', self.html)
        self.assertIn('class="skip"', self.html)

    def test_policy_ids_stay_in_metadata_not_reading_text(self):
        visible = ' '.join(self.page.text)
        self.assertIsNone(re.search(r'\b(?:FAM|HOU|HLT|LAB|AI|CLI|DEM|INT|CRT|CAP|REV|SS|EDU)-\d', visible))
        marked = {pid for _, a in self.page.tags for pid in a.get('data-policy-ids', '').split() + [a.get('data-policy-id', '')] if pid}
        self.assertTrue(marked <= set(self.content['policies']))
        self.assertTrue({p for e in self.content['essays'] for p in e['policy_ids']} <= marked)

    def test_blueprint_do_not_publish_claims(self):
        visible = ' '.join(self.page.text)
        # These claims may appear only negated (or, for financing, as the rule's stated requirement).
        forbidden = [r'fully (?:paid for|financed)',
                     r'\b(?:makes?|made|keeps?) (?:this|the|a|your) (?:place|town|community|home) safe\b',
                     r'middle[- ]income households (?:will )?come out ahead']
        for pattern in forbidden:
            for m in re.finditer(pattern, visible):
                before = visible[max(0, m.start() - 40):m.start()]
                self.assertRegex(before.lower(), r'\b(?:not|none|never|must be)\b', f'unqualified claim: {m.group(0)!r}')

    def test_self_contained_and_within_budget(self):
        self.assertLess(len(self.html.encode()), 200_000)
        self.assertNotIn('<script', self.html)
        self.assertIsNone(re.search(r'(?:src|href)="(?:https?:)?//[^"]*\.(?:js|css|woff2?)"', self.html))
        self.assertNotRegex(self.html, r'<link[^>]+stylesheet')


if __name__ == '__main__':
    unittest.main(verbosity=1)
