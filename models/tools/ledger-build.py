"""Shim: ledger-build.py moved to models/tools/budget/engine/ledger-build.py (stage H step H4, the budget model's release).

This file keeps the old path working for run-all.sh's callers, the bookings and any command a dossier quotes:
run it, or load it by path, and it runs the moved file as that file (its own __file__), unchanged.
"""
import os as _os
_REAL = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), 'budget/engine/ledger-build.py'))
if __name__ == "__main__":
    import runpy as _runpy, sys as _sys
    _sys.argv[0] = _REAL
    _runpy.run_path(_REAL, run_name="__main__")
else:
    __file__ = _REAL
    with open(_REAL, encoding="utf-8") as _f:
        exec(compile(_f.read(), _REAL, "exec"))
