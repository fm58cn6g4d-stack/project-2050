#!/usr/bin/env python3
"""Make a deterministic, self-contained research ZIP with integrity hashes."""
import argparse
import hashlib
import zipfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]


def package(destination):
    files = {}
    for path in HERE.rglob("*"):
        if path.is_file() and "__pycache__" not in path.parts and path.suffix != ".pyc":
            files[path.relative_to(ROOT).as_posix()] = path.read_bytes()
    for path in sorted((ROOT/"sources").glob("family-child-poverty-*")):
        if path.is_file() and any(s in path.name for s in ("rebuild", "minimum-microsimulation", "recovery", "comparator", "cps-baseline")):
            files[path.relative_to(ROOT).as_posix()] = path.read_bytes()
    files["README.md"] = ("# Rebuilt Project 2050 child-poverty research package\n\n"
        "Reconstructed implementation, not the missing historical ZIP. Observed CPS baseline included; no national Project policy estimate.\n\n"
        "Run: python3 index/tools/child-poverty/run_validation.py\n\n"
        "See index/tools/child-poverty/README.md for inputs and limits, and "
        "sources/family-child-poverty-rebuild-findings-and-integration.md for findings and integration.\n").encode()
    manifest = "".join(hashlib.sha256(data).hexdigest()+"  "+name+"\n" for name, data in sorted(files.items()))
    files["MANIFEST.sha256"] = manifest.encode()
    destination.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(destination, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as z:
        for name, data in sorted(files.items()):
            info = zipfile.ZipInfo(name, (2026, 10, 24, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            z.writestr(info, data)
    with zipfile.ZipFile(destination) as z:
        if z.testzip() is not None:
            raise ValueError("ZIP integrity failure")
        for name, data in files.items():
            if z.read(name) != data:
                raise ValueError("ZIP round-trip failure: "+name)
    print(f"Packaged {len(files)} files: {destination}")
    print("SHA-256: " + hashlib.sha256(destination.read_bytes()).hexdigest())


if __name__ == "__main__":
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--out", required=True, type=Path)
    package(p.parse_args().out.resolve())
