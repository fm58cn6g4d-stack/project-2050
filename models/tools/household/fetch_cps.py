#!/usr/bin/env python3
"""Download the Census Bureau's CPS ASEC 2026 archive and check its SHA-256.

Role: the household model's data fetch (`MODEL-CARD.md`, "How to run"). Status: working. Standard library only.

The committed extract (`models/data/household/`) lets the model and its tests run without the archive. The archive
(139 MB) is needed only to rebuild the extract (`extract.py`) or to rerun the replicate-weight intervals
(`intervals.py`). This script gets it from the Census Bureau and refuses a file whose SHA-256 is not the recorded one
(`extract.SHA256`, the hash `legacy/sources/family-child-poverty-cps-baseline.md` records), so a changed or truncated
download never reaches the model.

  python3 models/tools/household/fetch_cps.py [--out DIR] [--url URL] [--sha256 HASH]

DIR defaults to `build/cps` (ignored by git). A file already there with the right hash is left alone. The download goes to
a temporary name and is renamed only after the hash matches. Prints the archive's path, which `extract.py --archive` and
`intervals.py --archive` take. Exit 1 on a hash mismatch or a failed download.

The CPS public-use file is a U.S. government work.
"""
import argparse
import hashlib
import os
import sys
import urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from extract import SHA256, SOURCE_URL  # noqa: E402

CHUNK = 1 << 20


def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(CHUNK), b""):
            h.update(chunk)
    return h.hexdigest()


def fetch(out_dir, url=SOURCE_URL, sha256=SHA256, opener=urllib.request.urlopen):
    """The path of the verified archive in `out_dir`, downloading it if it is absent or wrong. Raises SystemExit on a
    mismatch (the bad download is deleted)."""
    os.makedirs(out_dir, exist_ok=True)
    dest = os.path.join(out_dir, os.path.basename(url.split("?")[0]) or "asec.zip")
    if os.path.exists(dest) and sha256_file(dest) == sha256:
        return dest
    tmp = dest + ".part"
    h = hashlib.sha256()
    try:
        with opener(url, timeout=120) as r, open(tmp, "wb") as f:
            for chunk in iter(lambda: r.read(CHUNK), b""):
                h.update(chunk)
                f.write(chunk)
    except OSError as e:
        if os.path.exists(tmp):
            os.remove(tmp)
        raise SystemExit(f"download failed: {e}")
    if h.hexdigest() != sha256:
        os.remove(tmp)
        raise SystemExit(f"{url}: the download's SHA-256 is {h.hexdigest()}, not the recorded {sha256}; nothing was kept")
    os.replace(tmp, dest)
    return dest


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--out", default=os.path.join(HERE, "..", "..", "..", "build", "cps"))
    ap.add_argument("--url", default=SOURCE_URL)
    ap.add_argument("--sha256", default=SHA256)
    a = ap.parse_args(argv)
    print(fetch(os.path.normpath(a.out), a.url, a.sha256))


if __name__ == "__main__":
    main()
