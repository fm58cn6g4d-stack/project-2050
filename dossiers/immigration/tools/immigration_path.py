#!/usr/bin/env python3
"""Wrapper: immigration_path.py moved to models/tools/immigration/immigration_path.py (stage H step H6, the full model `MOD-immigration`).

The dossier keeps this file so section 6's commands, care's `status_rule.py`, the booking
(`models/bookings/immigration_booking.py`) and `test_immigration_model.py` work unchanged: run it, import it or
load it by path, and it runs the moved file as that file (its own __file__), unchanged. Nothing else lives here;
the model's card, parameters and tests are in `models/tools/immigration/`.
"""
import os as _os
_REAL = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '../../../models/tools/immigration/immigration_path.py'))
if __name__ == "__main__":
    import runpy as _runpy, sys as _sys
    _sys.argv[0] = _REAL
    _runpy.run_path(_REAL, run_name="__main__")
else:
    __file__ = _REAL
    with open(_REAL, encoding="utf-8") as _f:
        exec(compile(_f.read(), _REAL, "exec"))
