"""Publication boundaries: evidence fidelity, human labels and source evolution."""
import copy
import csv
import hashlib
from html.parser import HTMLParser
import json
import unittest
from unittest.mock import patch
from urllib.parse import unquote, urlsplit

import build


class Links(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids, self.links, self.text = [], [], []
        self.hidden = 0

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if 'id' in attrs:
            self.ids.append(attrs['id'])
        if tag == 'a':
            self.links.append(attrs['href'])
        if tag in ('style', 'script'):
            self.hidden += 1

    def handle_endtag(self, tag):
        if tag in ('style', 'script'):
            self.hidden -= 1

    def handle_data(self, data):
        if not self.hidden:
            self.text.append(data)


class EditionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.content = json.loads((build.HERE/'content.json').read_text())
        cls.products = build.build()
        cls.manifest = json.loads(cls.products['manifest.json'])
        cls.mapping = json.loads(cls.products['public-map.json'])

    def test_numeric_exports_keep_units_case_and_scope_in_analysis(self):
        with build.here('index/data/fiscal-paths.csv').open() as f:
            row = next(r for r in csv.DictReader(f) if r['scenario'] == 'DEC' and r['year'] == '2040')
        contract = self.manifest['numeric_contracts']['fiscal_gap']
        self.assertEqual(contract['value'], float(row['gf_primary']))
        self.assertAlmostEqual(contract['gdp_share_percent'], 100*float(row['gf_primary'])/float(row['gdp']))
        self.assertEqual(contract['unit'], 'nominal USD billion')
        self.assertEqual(contract['view'], 'analysis.html#funding')
        page = self.products['analysis.html'].decode()
        self.assertIn('FY2040 general-fund primary gap', page)
        self.assertIn('not forecasts of 2050, full-agenda effects', page)
        source = json.loads(build.here('sources/family-comparison-model-checks.json').read_text())
        for case in source['adopted_cases']:
            self.assertIn(f'{100*case["result"]["poor_rate"]:.2f}%', page)

    def test_public_language_does_not_expose_policy_codes_or_model_results(self):
        page = Links()
        page.feed(self.products['index.html'].decode())
        text = ' '.join(page.text)
        self.assertNotRegex(text, r'\b(?:DEM|FAM|HOU|HLT|CLI|LAB|INT|CAP|EDU|AI)-\d')
        self.assertNotRegex(text, r'53\.69|54B|FY2040|8\.73%')
        for required in ('Freedom you can use', 'Elect a coalition for change', 'Hold leaders and ourselves accountable'):
            self.assertIn(required, text)
        self.assertIn('data-policy-ids="FAM-1"', self.products['index.html'].decode())

    def test_changed_source_cannot_silently_publish(self):
        with patch.object(build.subprocess, 'check_output', return_value=b'unreviewed drift'):
            with self.assertRaisesRegex(ValueError, 'Source changed: .*review .* before advancing'):
                build.build()

    def test_source_change_reports_affected_stories_without_rewriting_them(self):
        original = copy.deepcopy(self.content)
        with patch.object(build.subprocess, 'check_output', side_effect=['a'*40+'\n', 'domains/domain-family.md\nREADME.md\n']):
            report = build.review_changes(self.content, 'origin/main')
        self.assertEqual(report['changed_sources'], ['domains/domain-family.md'])
        self.assertIn('scene:home', report['review_required'])
        self.assertIn('scene:care', report['review_required'])
        self.assertNotIn('scene:climate', report['review_required'])
        self.assertIn('theme:secure-lives', report['review_required'])
        self.assertEqual(self.content, original)

    def test_unknown_policy_reference_is_rejected(self):
        content = copy.deepcopy(self.content)
        content['stops'][0]['steps'][0]['policy_ids'].append('FAM-UNKNOWN')
        with self.assertRaisesRegex(ValueError, 'Unknown policy reference in home'):
            build.content_map(content)

    def test_mapping_preserves_policy_identity_and_full_domain_reach(self):
        domains = {path for record in self.mapping['records'].values() for path in record['source_paths'] if path.startswith('domains/')}
        canonical = {str(p.relative_to(build.ROOT / 'legacy')) for p in (build.ROOT/'legacy/domains').glob('domain-*.md')}
        canonical.add('domains/transportation-moving-america-act-2031-draft-2.md')
        self.assertEqual(domains, canonical)
        self.assertEqual(self.mapping['policies']['FAM-1']['selected_option'], 'FAM-1D')
        self.assertEqual(self.mapping['policies']['HOU-4']['selected_option'], 'HOU-4A')
        self.assertEqual(len(self.mapping['records']['scene:home']['step_ids']), 3)

    def test_all_links_resolve_to_pinned_files_or_local_targets(self):
        pages = {}
        for filename, data in self.products.items():
            if filename.endswith('.html'):
                pages[filename] = Links()
                pages[filename].feed(data.decode())
        for filename, parsed in pages.items():
            self.assertEqual(len(parsed.ids), len(set(parsed.ids)), filename)
            for href in parsed.links:
                if href.startswith('https://'):
                    prefix = f'https://github.com/fm58cn6g4d-stack/project-2050/blob/{self.manifest["source_commit"]}/'
                    self.assertTrue(href.startswith(prefix), href)
                    path = unquote(urlsplit(href[len(prefix):]).path)
                    self.assertTrue(build.here(path).is_file(), path)
                    self.assertIn(path, self.manifest['sha256'])
                else:
                    target = urlsplit(href)
                    name = target.path or filename
                    self.assertIn(name, self.products)
                    if target.fragment:
                        self.assertIn(target.fragment, pages[name].ids, href)

    def test_manifest_covers_real_bytes(self):
        for path, digest in self.manifest['sha256'].items():
            self.assertEqual(hashlib.sha256(build.here(path).read_bytes()).hexdigest(), digest, path)
        for name, digest in self.manifest['outputs_sha256'].items():
            self.assertEqual(hashlib.sha256(self.products[name]).hexdigest(), digest)


if __name__ == '__main__':
    unittest.main()
