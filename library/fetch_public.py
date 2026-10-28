#!/usr/bin/env python3
"""Save a verbatim text version of a public-domain or openly licensed document into library/text/.

  python3 library/fetch_public.py URL SLUG "Publisher" [--file UPLOAD] [--rights "CC BY 4.0"]

U.S. government hosts are public domain. Any other source needs --rights naming the open license its
publisher states (CC0, CC BY, CC BY-SA and the other Creative Commons licenses), checked on the source
before saving. Licensed, paywalled or all-rights-reserved sources are never saved: catalog them as a
citation row and quote them briefly in the evidence entry (library/README.md).

With --file, the text comes from a copy Espen uploaded (for sites that block agent downloads, such as
HUD's); URL is still the official address, so the copy can be checked against it.

HTML becomes one paragraph per line (tags removed, whitespace collapsed); PDF goes through pdftotext.
An Excel workbook (.xlsx) becomes one line per cell, "row label | column header = value", where the row
label is the row's first text cell, so each figure can be anchored with its row and column.
The header records the address, retrieval date and the original's SHA-256, so the text can be checked
against the original later.
Evidence anchors (dossiers/*/evidence.json) must be exact passages of the saved text.
"""
import argparse
import datetime
import hashlib
import html
import re
import subprocess
import sys
import tempfile
import zipfile
import xml.etree.ElementTree as ET
from io import BytesIO
from pathlib import Path
from urllib.parse import urlparse

OUT = Path(__file__).resolve().parent / 'text'
# Hosts whose documents are U.S. government works. EveryCRSReport republishes CRS reports unchanged.
PUBLIC_HOSTS = ('.gov', '.mil', 'everycrsreport.com')
OPEN = re.compile(r'(CC0|CC BY(-SA|-NC|-ND|-NC-SA|-NC-ND)?|public domain)\b', re.I)


def html_text(raw):
    body = re.sub(r'<(script|style|nav|header|footer)\b.*?</\1>', '', raw, flags=re.S | re.I)
    body = re.sub(r'<(br|/p|/div|/h\d|/li|/tr)\b[^>]*>', '\n', body, flags=re.I)
    text = html.unescape(re.sub(r'<[^>]+>', ' ', body))
    lines = [re.sub(r'\s+', ' ', line).strip() for line in text.split('\n')]
    return '\n'.join(line for line in lines if line) + '\n'


def pdf_text(data):
    with tempfile.NamedTemporaryFile(suffix='.pdf') as f:
        f.write(data)
        f.flush()
        return subprocess.check_output(['pdftotext', f.name, '-'], text=True)


def column_index(letters):
    n = 0
    for ch in letters:
        n = n * 26 + ord(ch) - ord('A') + 1
    return n - 1


def is_xlsx(data):
    if data[:2] != b'PK':
        return False
    try:
        return 'xl/workbook.xml' in zipfile.ZipFile(BytesIO(data)).namelist()
    except zipfile.BadZipFile:
        return False


def xlsx_text(data):
    ns = {'m': 'http://schemas.openxmlformats.org/spreadsheetml/2006/main'}
    rel = '{http://schemas.openxmlformats.org/officeDocument/2006/relationships}id'
    z = zipfile.ZipFile(BytesIO(data))
    shared = []
    if 'xl/sharedStrings.xml' in z.namelist():
        for si in ET.fromstring(z.read('xl/sharedStrings.xml')).findall('m:si', ns):
            shared.append(''.join(t.text or '' for t in si.iter(f"{{{ns['m']}}}t")))
    rels = {r.get('Id'): r.get('Target') for r in ET.fromstring(z.read('xl/_rels/workbook.xml.rels'))}
    out = []
    for sheet in ET.fromstring(z.read('xl/workbook.xml')).find('m:sheets', ns):
        target = rels[sheet.get(rel)].lstrip('/')
        root = ET.fromstring(z.read(target if target.startswith('xl/') else 'xl/' + target))
        rows = []
        for row in root.iter(f"{{{ns['m']}}}row"):
            # Empty cells are usually omitted, so place each cell by its column letters (r="C7"), not its order.
            cells = {}
            for k, c in enumerate(row.findall('m:c', ns)):
                ref = re.match(r'[A-Z]+', c.get('r', ''))
                col = column_index(ref.group(0)) if ref else k
                v = c.find('m:v', ns)
                inline = c.find('m:is', ns)
                if c.get('t') == 's' and v is not None:
                    cells[col] = shared[int(v.text)]
                elif inline is not None:
                    cells[col] = ''.join(t.text or '' for t in inline.iter(f"{{{ns['m']}}}t"))
                else:
                    cells[col] = v.text if v is not None else ''
            rows.append(cells)
        width = max((max(r) + 1 for r in rows if r), default=0)
        rows = [[r.get(j, '') for j in range(width)] for r in rows]
        out.append(f'Sheet: {sheet.get("name")}')
        if not rows:
            continue
        header, body = rows[0], rows[1:]
        # Label rows by the first text column whose values tell the rows apart.
        key = next((j for j in range(width)
                    if all(r[j] and not re.fullmatch(r'-?[\d.]+', r[j]) for r in body)
                    and len({r[j] for r in body}) == len(body)), None)
        for i, cells in enumerate(body, start=2):
            label = cells[key] if key is not None else f'row {i}'
            out += [f'{label} | {h} = {c}' for h, c in zip(header, cells) if h or c]
    return '\n'.join(out) + '\n'


if __name__ == '__main__':
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('url')
    ap.add_argument('slug')
    ap.add_argument('publisher')
    ap.add_argument('--file', dest='upload', help='a copy Espen uploaded, saved under URL')
    ap.add_argument('--rights', help='the open license a non-government source states, e.g. "CC BY 4.0"')
    args = ap.parse_args()
    url, slug, publisher, upload = args.url, args.slug, args.publisher, args.upload
    host = urlparse(url).hostname or ''
    if host.endswith(PUBLIC_HOSTS):
        rights = args.rights or 'public domain (U.S. government work)'
    elif args.rights and OPEN.match(args.rights):
        rights = args.rights
    else:
        sys.exit(f'{host} is not a U.S. government host: give --rights with the open license it states, '
                 'or catalog it as a citation and quote it briefly (library/README.md)')
    # curl, with the environment's proxy and certificates; some government sites refuse other clients.
    data = (Path(upload).read_bytes() if upload else
            subprocess.check_output(['curl', '-sS', '-L', '--fail', '--max-time', '120', url]))
    kind = 'pdf' if data[:5] == b'%PDF-' else 'xlsx' if is_xlsx(data) else 'html'
    text = (xlsx_text(data) if kind == 'xlsx' else
            pdf_text(data) if 'pdf' in kind or url.lower().endswith('.pdf') else html_text(data.decode('utf-8', 'replace')))
    retrieved = datetime.date.today().isoformat() + (' (copy uploaded by Espen)' if upload else '')
    header = (f'Source: {url}\nPublisher: {publisher}\nRetrieved: {retrieved}\n'
              f'Original SHA-256: {hashlib.sha256(data).hexdigest()}\n'
              f'Rights: {rights}\n'
              'Text version made by library/fetch_public.py; passages are verbatim.\n---\n')
    OUT.mkdir(exist_ok=True)
    (OUT / f'{slug}.txt').write_text(header + text)
    print(f'wrote library/text/{slug}.txt ({len(text):,} characters)')
