#!/usr/bin/env python3
"""Tests for library/fetch_public.py's Excel reader: cells land under their own column headers."""
import importlib.util
import unittest
import zipfile
from io import BytesIO
from pathlib import Path

spec = importlib.util.spec_from_file_location('fetch_public', Path(__file__).resolve().parent / 'fetch_public.py')
fp = importlib.util.module_from_spec(spec)
spec.loader.exec_module(fp)

M = 'http://schemas.openxmlformats.org/spreadsheetml/2006/main'
R = 'http://schemas.openxmlformats.org/officeDocument/2006/relationships'


def workbook(sheet_rows):
    """A minimal .xlsx with inline strings; sheet_rows is a list of rows of (ref, value) pairs."""
    def cell(ref, v):
        if isinstance(v, str):
            return f'<c r="{ref}" t="inlineStr"><is><t>{v}</t></is></c>'
        return f'<c r="{ref}"><v>{v}</v></c>'
    rows = ''.join(f'<row r="{i}">' + ''.join(cell(r, v) for r, v in row) + '</row>'
                   for i, row in enumerate(sheet_rows, start=1))
    buf = BytesIO()
    with zipfile.ZipFile(buf, 'w') as z:
        z.writestr('xl/workbook.xml', f'<workbook xmlns="{M}" xmlns:r="{R}"><sheets>'
                                      f'<sheet name="Data" sheetId="1" r:id="rId1"/></sheets></workbook>')
        z.writestr('xl/_rels/workbook.xml.rels',
                   '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
                   '<Relationship Id="rId1" Target="worksheets/sheet1.xml"/></Relationships>')
        z.writestr('xl/worksheets/sheet1.xml', f'<worksheet xmlns="{M}"><sheetData>{rows}</sheetData></worksheet>')
    return buf.getvalue()


class XlsxText(unittest.TestCase):
    def test_sparse_row_keeps_columns(self):
        data = workbook([
            [('A1', 'program'), ('B1', 'units'), ('C1', 'pct_black'), ('D1', 'pct_white')],
            [('A2', 'Vouchers'), ('B2', 100), ('C2', 48), ('D2', 30)],
            [('A3', 'Public Housing'), ('C3', 42), ('D3', 29)],  # B3 empty and omitted
        ])
        lines = fp.xlsx_text(data).splitlines()
        self.assertIn('Public Housing | pct_black = 42', lines)
        self.assertIn('Public Housing | pct_white = 29', lines)
        self.assertIn('Public Housing | units = ', lines)
        self.assertIn('Vouchers | units = 100', lines)

    def test_detection(self):
        self.assertTrue(fp.is_xlsx(workbook([[('A1', 'x')]])))
        other = BytesIO()
        with zipfile.ZipFile(other, 'w') as z:
            z.writestr('word/document.xml', '<x/>')
        self.assertFalse(fp.is_xlsx(other.getvalue()))
        self.assertFalse(fp.is_xlsx(b'%PDF-1.7'))

    def test_column_letters(self):
        self.assertEqual([fp.column_index(c) for c in ('A', 'Z', 'AA', 'BV')], [0, 25, 26, 73])


if __name__ == '__main__':
    unittest.main()
