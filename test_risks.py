import unittest
from risk_register import assess, load


class RiskTests(unittest.TestCase):
    def row(self, likelihood, impact):
        return dict(id='R-1', asset='demo', risk='example', likelihood=likelihood,
                    impact=impact, owner='owner', treatment='review')

    def test_boundaries(self):
        for l, i, expected in [(1, 5, 'low'), (2, 3, 'medium'), (3, 5, 'high'), (4, 5, 'critical')]:
            self.assertEqual(assess(self.row(l, i))['level'], expected)

    def test_reject_out_of_range_and_missing_owner(self):
        for row in [self.row(0, 5), self.row(6, 1), {**self.row(3, 3), 'owner': ''}]:
            with self.assertRaises(ValueError):
                assess(row)

    def test_sample_sorted(self):
        rows = load('sample-risks.csv')
        self.assertEqual([r['score'] for r in rows], [16, 15, 9, 4])


if __name__ == '__main__':
    unittest.main()
