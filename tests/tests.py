import os
import unittest

import rec


DIR_PATH = os.path.dirname(os.path.abspath(__file__))


def _path(rel_path):
    return os.path.join(DIR_PATH, rel_path)


def _rec_against_sample(test_csv_rel_path):
    return rec.reconcile_csvs(_path('data/sample.csv'), _path(test_csv_rel_path))


class TestAll(unittest.TestCase):
    def test_same_csv(self):
        results = _rec_against_sample('data/sample.csv')
        self.assertEqual(results, {})

    def test_same_data(self):
        results = _rec_against_sample('data/diff_order_same_data.csv')
        self.assertEqual(results, {})

    def test_different_row(self):
        results = _rec_against_sample('data/diff_row.csv')
        self.assertTrue(results.get('rows_diff') is not None)

    def test_different_row_count(self):
        results = _rec_against_sample('data/extra_row.csv')
        self.assertTrue(results.get('row_lengths') is not None)

    def test_different_column_count(self):
        results = _rec_against_sample('data/missing_col.csv')
        self.assertTrue(results.get('header_diff') is not None)

    def test_different_header_length(self):
        results = _rec_against_sample('data/diff_header.csv')
        self.assertTrue(results.get('header_diff') is not None)


if __name__ == '__main__':
    unittest.main()
