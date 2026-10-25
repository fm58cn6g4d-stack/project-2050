"""Boundary checks for editorial export fidelity, provenance and navigability."""
import csv
import hashlib
from html.parser import HTMLParser
import json
from pathlib import Path
import unittest
from unittest.mock import patch
from urllib.parse import unquote, urlsplit

import build


class Links(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids = []
        self.links = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if 'id' in attrs:
            self.ids.append(attrs['id'])
        if tag == 'a':
            self.links.append(attrs['href'])


class EditionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.products = build.build()
        cls.manifest = json.loads(cls.products['manifest.json'])

    def test_numeric_exports_keep_units_case_and_scope(self):
        with (build.ROOT / 'index/data/fiscal-paths.csv').open() as f:
            row = next(r for r in csv.DictReader(f) if r['scenario'] == 'DEC' and r['year'] == '2040')
        contract = self.manifest['numeric_contracts']['fiscal_gap']
        self.assertEqual(contract['value'], float(row['gf_primary']))
        self.assertEqual(contract['unit'], 'nominal USD billion')
        page = self.products['index.html'].decode()
        self.assertIn('FY2040 general-fund primary gap', page)
        self.assertIn('not forecasts of 2050, full-agenda effects', page)
        source = json.loads((build.ROOT / 'sources/family-comparison-model-checks.json').read_text())
        for case in source['adopted_cases']:
            self.assertIn(f'{100*case["result"]["poor_rate"]:.2f}%', page)

    def test_changed_source_cannot_silently_publish(self):
        with patch.object(build.subprocess, 'check_output', return_value=b'unreviewed drift'):
            with self.assertRaisesRegex(ValueError, 'Source changed'):
                build.build()

    def test_all_links_resolve_to_pinned_files_or_local_targets(self):
        for filename in ('index.html', 'directions.html'):
            parsed = Links()
            parsed.feed(self.products[filename].decode())
            self.assertEqual(len(parsed.ids), len(set(parsed.ids)))
            for href in parsed.links:
                if href.startswith('#'):
                    self.assertTrue(href == '#' or href[1:] in parsed.ids, href)
                elif href.startswith('https://'):
                    prefix = f'https://github.com/fm58cn6g4d-stack/project-2050/blob/{self.manifest["source_commit"]}/'
                    self.assertTrue(href.startswith(prefix), href)
                    path = unquote(urlsplit(href[len(prefix):]).path)
                    self.assertTrue((build.ROOT/path).is_file(), path)
                    self.assertIn(path, self.manifest['sha256'])
                else:
                    self.assertIn(href, self.products)

    def test_manifest_covers_real_bytes(self):
        for path, digest in self.manifest['sha256'].items():
            self.assertEqual(hashlib.sha256((build.ROOT/path).read_bytes()).hexdigest(), digest, path)
        for name, digest in self.manifest['outputs_sha256'].items():
            self.assertEqual(hashlib.sha256(self.products[name]).hexdigest(), digest)


if __name__ == '__main__':
    unittest.main()
