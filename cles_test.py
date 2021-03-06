import unittest

import numpy as np

import cles


def slow_cles(lessers, greaters):
    """Common-Language Effect Size (quadratic implementation)

    Probability that a random draw from `greater` is in fact greater
    than a random draw from `lesser`.

    This is the naive implementation that actually does every
    comparison. It's slow, but it's easy to see that it's correct.
    Also it doesn't handle edge cases (empty arguments).

    Args:
      lesser, greater: Iterables of comparables.
    """
    numerator = 0
    for lesser in lessers:
        for greater in greaters:
            if lesser < greater:
                numerator += 1
    denominator = len(lessers) * len(greaters)
    return float(numerator) / denominator


class TestPythonTest(unittest.TestCase):

    def test_world_is_sane(self):
        self.assertEqual(2+2, 4)


class TestExceptions(unittest.TestCase):

    def test_raises_if_both_empty_lists(self):
        with self.assertRaises(Exception):
            cles.cles([], [])

    def test_no_raise_if_either_list_nonempty(self):
        cles.cles([1], [])
        cles.cles([], [1, 1])
        cles.cles([1], [2])

    def test_raises_if_both_empty_ndarrays(self):
        with self.assertRaises(Exception):
            cles.cles(np.array([]), np.array([]))

    def test_no_raise_if_either_ndarray_nonempty(self):
        cles.cles(np.array([1, 1]), np.array([]))
        cles.cles(np.array([]), np.array([1, 1]))
        cles.cles(np.array([1, 1]), np.array([1, 1]))


class TestSimpleCases(unittest.TestCase):

    def test_all_lesser(self):
        lessers = [3, 2, 4]
        greaters = [0, 0, 1]
        slow_result = slow_cles(lessers, greaters)
        self.assertEqual(slow_result, 0)
        real_result = cles.cles(lessers, greaters)
        self.assertEqual(real_result, 0)

    def test_all_greater(self):
        lessers = [0, 0, 1]
        greaters = [3, 2, 4]
        slow_result = slow_cles(lessers, greaters)
        self.assertEqual(slow_result, 1)
        real_result = cles.cles(lessers, greaters)
        self.assertEqual(real_result, 1)

    def test_equal_is_not_greater(self):
        lessers = [1, 1, 1]
        greaters = [1, 1, 1]
        slow_result = slow_cles(lessers, greaters)
        self.assertEqual(slow_result, 0)
        real_result = cles.cles(lessers, greaters)
        self.assertEqual(real_result, 0)

    def test_even_mix(self):
        lessers = [0, 1]
        greaters = [1, 2]
        slow_result = slow_cles(lessers, greaters)
        self.assertEqual(slow_result, 0.75)
        real_result = cles.cles(lessers, greaters)
        self.assertEqual(real_result, 0.75)
