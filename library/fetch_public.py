#!/usr/bin/env python3
"""Save a verbatim text version of a public-domain document into library/text/.

  python3 library/fetch_public.py URL SLUG "Publisher"

HTML becomes one paragraph per line (tags removed, whitespace collapsed); PDF goes through pdftotext.
The header records the address, retrieval date and the original's SHA-256, so the text can be checked
against the original later. Use it only for public-domain material (U.S. government works): licensed or
paywalled sources are cited and briefly quoted in an evidence entry, never saved here.
Evidence anchors (dossiers/*/evidence.json) must be exact passages of the saved text.
"""
import datetime
import hashlib
import html
import re
import subprocess
import sys
import tempfile
from pathlib import Path
from urllib.parse import urlparse

OUT = Path(__file__).resolve().parent / 'text'
# Hosts whose documents are U.S. government works; the rights line below is only true for them.
# EveryCRSReport republishes Congressional Research Service reports unchanged.
PUBLIC_HOSTS = ('.gov', '.mil', 'everycrsreport.com')


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


if __name__ == '__main__':
    url, slug, publisher = sys.argv[1:4]
    host = urlparse(url).hostname or ''
    if not host.endswith(PUBLIC_HOSTS):
        sys.exit(f'{host} is not a U.S. government host; cite a licensed or private source instead of saving it')
    # curl, with the environment's proxy and certificates; some government sites refuse other clients.
    data = subprocess.check_output(['curl', '-sS', '-L', '--fail', '--max-time', '120', url])
    kind = 'pdf' if data[:5] == b'%PDF-' else 'html'
    text = pdf_text(data) if 'pdf' in kind or url.lower().endswith('.pdf') else html_text(data.decode('utf-8', 'replace'))
    header = (f'Source: {url}\nPublisher: {publisher}\nRetrieved: {datetime.date.today().isoformat()}\n'
              f'Original SHA-256: {hashlib.sha256(data).hexdigest()}\n'
              'Rights: public domain (U.S. government work)\n'
              'Text version made by library/fetch_public.py; passages are verbatim.\n---\n')
    OUT.mkdir(exist_ok=True)
    (OUT / f'{slug}.txt').write_text(header + text)
    print(f'wrote library/text/{slug}.txt ({len(text):,} characters)')
