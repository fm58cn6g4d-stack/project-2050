#!/usr/bin/env bash
# Regenerate every generated file in index/ from the scripts in index/tools/.
# Usage (from the repo root):   bash index/tools/run-all.sh          # rebuild, show a diff, do not overwrite
#                               bash index/tools/run-all.sh --write  # rebuild and copy outputs into index/
#                               bash index/tools/run-all.sh --fetch  # also re-download CBO's data first
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
TOOLS="$ROOT/index/tools"; DATA="$ROOT/index/data"; BUILD="$ROOT/build"
WRITE=0; FETCH=0
for a in "$@"; do [[ "$a" == "--write" ]] && WRITE=1; [[ "$a" == "--fetch" ]] && FETCH=1; done

rm -rf "$BUILD"; mkdir -p "$BUILD"
cp "$TOOLS"/ledger-build.py "$TOOLS"/ledger-paths.py "$TOOLS"/ledger-make-md.py "$TOOLS"/incidence-make-md.py \
   "$TOOLS"/fiscal-data.py "$TOOLS"/fiscal-profiles.py "$TOOLS"/fiscal-model.py "$TOOLS"/fiscal-make-md.py "$BUILD"/
# the two incidence scripts import each other under their working names
cp "$TOOLS"/incidence-model.py "$BUILD"/incidence.py
cp "$TOOLS"/incidence-years.py "$BUILD"/years.py
# ledger-make-md.py copies two sections from the current ledger, so it needs a copy beside it
cp "$ROOT"/index/2029-trifecta-master-ledger.md "$BUILD"/

cd "$BUILD"
echo "== 1. ledger";            python3 ledger-build.py >/dev/null
echo "== 2. floor paths";       python3 ledger-paths.py >/dev/null
echo "== 3. ledger markdown";   python3 ledger-make-md.py >/dev/null
echo "== 4. incidence";         python3 incidence.py >/dev/null; python3 years.py >/dev/null; python3 incidence-make-md.py >/dev/null
if [[ $FETCH == 1 ]]; then
  echo "== 5a. fetch CBO data";  python3 fiscal-data.py --fetch --cache "$DATA/cbo" --out "$BUILD/fiscal-baseline.csv"
else
  echo "== 5. fiscal baseline";  python3 fiscal-data.py --cache "$DATA/cbo" --out "$BUILD/fiscal-baseline.csv"
fi
echo "== 6. fiscal model";      python3 fiscal-model.py --baseline "$BUILD/fiscal-baseline.csv" | head -1
python3 fiscal-make-md.py --baseline "$BUILD/fiscal-baseline.csv" >/dev/null

declare -A OUT=(
  [2029-trifecta-master-ledger-v2.md]=index/2029-trifecta-master-ledger.md
  [revenue-household-incidence-model.md]=index/revenue-household-incidence-model.md
  [fiscal-long-term-model.md]=index/fiscal-long-term-model.md
  [fiscal-baseline.csv]=index/data/fiscal-baseline.csv
  [fiscal-paths.csv]=index/data/fiscal-paths.csv
)
echo; echo "== changes against the committed files"
for f in "${!OUT[@]}"; do
  if diff -q "$BUILD/$f" "$ROOT/${OUT[$f]}" >/dev/null 2>&1; then echo "  unchanged  ${OUT[$f]}";
  else echo "  CHANGED    ${OUT[$f]}  ($(diff "$BUILD/$f" "$ROOT/${OUT[$f]}" | grep -c '^[<>]') lines differ)"; fi
done
if [[ $WRITE == 1 ]]; then
  for f in "${!OUT[@]}"; do cp "$BUILD/$f" "$ROOT/${OUT[$f]}"; done
  echo "Copied outputs into index/."
else
  echo "Dry run: nothing copied. Rerun with --write to update index/."
fi
