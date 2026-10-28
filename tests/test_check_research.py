import csv
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

SCRIPT = Path(__file__).resolve().parents[1] / 'scripts/check_research.py'


class ResearchChecks(unittest.TestCase):
    def run_check(self, changes=None, details=False):
        tables = {
            'sources': [['id', 'url', 'revision', 'path', 'sha256', 'status', 'reason'],
                        ['S1', 'https://example.org/drawing', 'A', '', '', 'adopted', 'matched']],
            'packages': [['id', 'part', 'variant', 'length_mm', 'width_mm', 'height_mm', 'lead_extents', 'source', 'status'],
                         ['P1', 'Exact maker part', 'A', '1.6', '0.8', '0.6', 'no leads', 'S1', 'verified']],
            'components': [['ref', 'side', 'x_mm', 'y_mm', 'rotation_deg', 'package', 'source', 'status'],
                           ['R1', 'top', '2', '3', '90', 'P1', 'S1', 'verified']],
            'pins': [['connector', 'number', 'signal', 'x_mm', 'y_mm', 'z_mm', 'view', 'source', 'status'],
                     ['J1', '1', 'unknown', '0', '0', '0', 'top USB up', 'S1', 'verified']],
        }
        if changes:
            changes(tables)
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            for name, rows in tables.items():
                with (root / (name + '.csv')).open('w', newline='', encoding='utf-8') as stream:
                    csv.writer(stream).writerows(rows)
            before = {p.name: p.read_bytes() for p in root.iterdir()}
            result = subprocess.run([sys.executable, str(SCRIPT), str(root)] + (['--details'] if details else []), capture_output=True, text=True)
            self.assertEqual(before, {p.name: p.read_bytes() for p in root.iterdir()})
            return result

    def test_valid_tables_are_only_a_data_check(self):
        result = self.run_check()
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn('not CAD verification', result.stdout)

    def test_duplicate_ref_and_bad_source_fail(self):
        def change(t):
            t['components'].append(t['components'][1][:])
            t['components'][1][-2] = 'S404'
        result = self.run_check(change, True)
        self.assertEqual(result.returncode, 1)
        self.assertIn('duplicate', result.stdout)
        self.assertIn('unknown source', result.stdout)

    def test_missing_and_nonfinite_dimensions_fail(self):
        for value in ['', 'nan', '-1', 'inf']:
            with self.subTest(value=value):
                result = self.run_check(lambda t: t['packages'][1].__setitem__(3, value))
                self.assertEqual(result.returncode, 1)

    def test_unresolved_status_is_counted(self):
        result = self.run_check(lambda t: t['components'][1].__setitem__(-1, 'missing'))
        self.assertEqual(result.returncode, 1)
        self.assertIn('unresolved=1', result.stdout)

    def test_missing_file_and_ragged_rows_fail(self):
        result = self.run_check(lambda t: t.pop('pins'), True)
        self.assertEqual(result.returncode, 1)
        result = self.run_check(lambda t: t['pins'][1].append('extra'), True)
        self.assertEqual(result.returncode, 1)

    def test_unknown_package_side_and_status_fail(self):
        for index, value in [(1, 'left'), (5, 'P404'), (7, 'done')]:
            with self.subTest(value=value):
                result = self.run_check(lambda t: t['components'][1].__setitem__(index, value))
                self.assertEqual(result.returncode, 1)

    def test_bad_header_hash_and_unadopted_source_fail(self):
        changes = [
            lambda t: t['pins'][0].__setitem__(0, 'bad'),
            lambda t: t['sources'][1].__setitem__(3, 'download.step'),
            lambda t: t['sources'][1].__setitem__(4, 'wrong-hash'),
            lambda t: t['sources'][1].__setitem__(5, 'reference'),
            lambda t: t['packages'][1].__setitem__(-1, 'unverified'),
        ]
        for change in changes:
            self.assertEqual(self.run_check(change).returncode, 1)

    def test_default_output_is_bounded(self):
        def change(t):
            t['components'].extend([t['components'][1][:] for _ in range(100)])
        result = self.run_check(change)
        self.assertEqual(result.returncode, 1)
        self.assertLess(len(result.stdout), 300)
        self.assertEqual(len(result.stdout.splitlines()), 2)


if __name__ == '__main__':
    unittest.main()
