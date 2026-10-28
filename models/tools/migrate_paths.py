#!/usr/bin/env python3
"""Move a pre-reset branch's repository paths to the October 28 tree (charter/STANDARDS.md).

index/tools -> models/tools, index/data -> models/data, index/public-2050 -> public/site, and
sources/, domains/, governing/, frameworks/, staging/, archive/ and the rest of index/ -> legacy/.
Rewrites root-relative paths in code and in path components such as ROOT / 'sources'; leaves
relative links (../sources/x.md) alone, since files keep their places relative to each other.
Review the diff: it is a careful text rewrite, not a parser.

  python3 models/tools/migrate_paths.py FILE...
"""
import re
import sys
from pathlib import Path

LEG = r'(sources|domains|governing|frameworks|staging|archive)'
B = r'(?<![A-Za-z0-9_./$-])'   # not inside a longer path, a ../ link or a $ROOT/ shell path


def migrate(t):
    t = re.sub(B + r'index/tools', 'models/tools', t)
    t = re.sub(B + r'index/data', 'models/data', t)
    t = re.sub(B + r'index/public-2050', 'public/site', t)
    t = re.sub(B + r'index/(?=[A-Za-z0-9*{])', 'legacy/index/', t)
    t = re.sub(B + LEG + r'/', r'legacy/\1/', t)
    t = re.sub(r'(\$ROOT/)index/(tools|data)\b', r'\1models/\2', t)
    # Path components: ROOT / 'sources', os.path.join(ROOT, "index", "data"). Never dict keys ('sources':).
    t = re.sub(r'''([/,(]\s?)(["'])index\2(\s*[,/]\s*)(["'])(tools|data)\4''', r'\1\2models\2\3\4\5\4', t)
    t = re.sub(r'''([/,(]\s?)(["'])index\2(?!\s*:)(?!\s*[,/]\s*["'](?:tools|data)["'])''', r'\1\2legacy/index\2', t)
    t = re.sub(r'''([/,(]\s?)(["'])''' + LEG + r'''\2(?!\s*[:)])''', r'\1\2legacy/\3\2', t)
    return t


if __name__ == '__main__':
    for name in sys.argv[1:]:
        path = Path(name)
        text = path.read_text()
        new = migrate(text)
        if new != text:
            path.write_text(new)
            print('migrated', path)
