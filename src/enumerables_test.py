import unittest
from enumerables import *

class TestEnumerables(unittest.TestCase):
    def test_where(self):
        is_even = lambda x: x % 2 == 0
        result = Enumerable().of(range(10)).where(is_even).to_list()
        expected = [0, 2, 4, 6, 8]
        self.assertEqual(result, expected, f"Expected: {expected}, but got: {result}")

    def test_select(self):
        doubleAddOne = lambda x: x * 2 + 1
        result = Enumerable().of(range(5)).select(doubleAddOne).to_list()
        expected = [1, 3, 5, 7, 9]
        self.assertEqual(result, expected, f"Expected: {expected}, but got: {result}")

    def test_select_many(self):
        result = Enumerable().of([(1, 2), (3, 4)]).select_many(lambda x: x).to_list()
        expected = [1, 2, 3, 4]
        self.assertEqual(result, expected, f"Expected: {expected}, but got: {result}")

    def test_distinct(self):
        result = Enumerable().of([1, 2, 2, 3, 3, 3]).distinct().to_list()
        expected = [1, 2, 3]
        self.assertEqual(result, expected, f"Expected: {expected}, but got: {result}")

    def test_distinct_by(self):
        result = Enumerable().of([(1, 2), (3, 4), (1, 7)]).distinct_by(lambda x: x[0]).to_list()
        expected = [(1, 2), (3, 4)]
        self.assertEqual(result, expected, f"Expected: {expected}, but got: {result}")

    def test_take(self):
        result = Enumerable().of(range(10)).take(5).to_list()
        expected = [0, 1, 2, 3, 4]
        self.assertEqual(result, expected, f"Expected: {expected}, but got: {result}")

    def test_take_while(self):
        is_less_than_five = lambda x: x < 5
        result = Enumerable().of(range(10)).take_while(is_less_than_five).to_list()
        expected = [0, 1, 2, 3, 4]
        self.assertEqual(result, expected, f"Expected: {expected}, but got: {result}")

    def test_skip(self):
        result = Enumerable().of(range(10)).skip(5).to_list()
        expected = [5, 6, 7, 8, 9]
        self.assertEqual(result, expected, f"Expected: {expected}, but got: {result}")

    def test_skip_while(self):
        is_less_than_five = lambda x: x < 5
        result = Enumerable().of(range(10)).skip_while(is_less_than_five).to_list()
        expected = [5, 6, 7, 8, 9]
        self.assertEqual(result, expected, f"Expected: {expected}, but got: {result}")

    def test_aggregate(self):
        result = Enumerable().of(range(1, 6)).aggregate(lambda x, y: x + y)
        expected = 15
        self.assertEqual(result, expected, f"Expected: {expected}, but got: {result}")

    def test_aggregate_with_seed(self):
        result = Enumerable().of(range(1, 6)).aggregate_with_seed(lambda x, y: x + y, 10)
        expected = 25
        self.assertEqual(result, expected, f"Expected: {expected}, but got: {result}")

    def test_count(self):
        result = Enumerable().of(range(10)).count()
        expected = 10
        self.assertEqual(result, expected, f"Expected: {expected}, but got: {result}")

    def test_count_where(self):
        is_even = lambda x: x % 2 == 0
        result = Enumerable().of(range(10)).count_where(is_even)
        expected = 5
        self.assertEqual(result, expected, f"Expected: {expected}, but got: {result}")

    def test_concat(self):
        result = Enumerable().of(range(5)).concat(range(5, 10)).to_list()
        expected = list(range(10))
        self.assertEqual(result, expected, f"Expected: {expected}, but got: {result}")

    def test_first(self):
        result = Enumerable().of(range(10)).first()
        expected = 0
        self.assertEqual(result, expected, f"Expected: {expected}, but got: {result}")

    def test_first_where(self):
        mod_4_minus_3_equals_0 = lambda x: x % 4 - 3 == 0
        result = Enumerable().of(range(10)).first_where(mod_4_minus_3_equals_0)
        expected = 3
        self.assertEqual(result, expected, f"Expected: {expected}, but got: {result}")

    def test_last(self):
        result = Enumerable().of(range(10)).last()
        expected = 9
        self.assertEqual(result, expected, f"Expected: {expected}, but got: {result}")

    def test_last_where(self):
        mod_4_minus_3_equals_0 = lambda x: x % 4 - 3 == 0
        result = Enumerable().of(range(10)).last_where(mod_4_minus_3_equals_0)
        expected = 7
        self.assertEqual(result, expected, f"Expected: {expected}, but got: {result}")

    def test_sort(self):
        result = Enumerable().of(range(10)).sort(lambda x: -x).to_list()
        expected = list(reversed(range(10)))
        self.assertEqual(result, expected, f"Expected: {expected}, but got: {result}")

    def test_sort_by(self):
        result = Enumerable().of(range(10)).sort_by(lambda x: -x).to_list()
        expected = list(reversed(range(10)))
        self.assertEqual(result, expected, f"Expected: {expected}, but got: {result}")

    def test_reverse(self):
        result = Enumerable().of(range(10)).reverse().to_list()
        expected = list(reversed(range(10)))
        self.assertEqual(result, expected, f"Expected: {expected}, but got: {result}")

    def test_any(self):
        result = Enumerable().of(range(10)).any(lambda x: x % 2 == 0)
        expected = True
        self.assertTrue(result, f"Expected: {expected}, but got: {result}")

    def test_all(self):
        result = Enumerable().of(range(10)).all(lambda x: x % 2 == 0)
        expected = False
        self.assertFalse(result, f"Expected: {expected}, but got: {result}")

    def test_is_empty(self):
        result = Enumerable().of(range(10)).is_empty()
        expected = False
        self.assertFalse(result, f"Expected: {expected}, but got: {result}")

    def test_to_list(self):
        result = Enumerable().of(range(10)).to_list()
        expected = list(range(10))
        self.assertEqual(result, expected, f"Expected: {expected}, but got: {result}")

    def test_to_set(self):
        result = Enumerable().of(range(10)).to_set()
        expected = set(range(10))
        self.assertEqual(result, expected, f"Expected: {expected}, but got: {result}")

    def test_zip(self):
        pair_operation = lambda pair: (pair[0]*3, pair[1]/3)

        result = (
            Enumerable()
            .of(range(10))
            .zip(range(10, 20))
            .select(pair_operation)
            .to_list()
        )

        expected = list(pair_operation(pair) for pair in zip(range(10), range(10, 20)))
        self.assertEqual(result, expected, f"Expected: {expected}, but got: {result}")

    def test_piping(self):
        result: int = (
            Enumerable().of(range(10))
            | Selector(lambda x: x * 2)
            | Predicate(lambda x: x > 10)
            | Accumulator(lambda x, y: x + y)
        )
        expected = sum([12, 14, 16, 18])
        self.assertEqual(result, expected, f"Expected: {expected}, but got: {result}")

    def test_intersect(self):
        result = (
            Enumerable()
                .of(range(10))
                .intersect(range(5, 15))
                .to_list()
        )
        expected = list(range(5, 10))
        self.assertEqual(result, expected, f"Expected: {expected}, but got: {result}")

    def test_without(self):
        result = (
            Enumerable()
                .of(range(10))
                .without(range(5, 10))
                .to_list()
        )
        expected = list(range(5))
        self.assertEqual(result, expected, f"Expected: {expected}, but got: {result}")

if __name__ == "__main__":
    unittest.main()
