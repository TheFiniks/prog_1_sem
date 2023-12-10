import unittest
from quicksort import quicksort


class TestOrdinaryList(unittest.TestCase):
    def test_quicksort(self):
        self.assertEqual(quicksort([2, 3, 1, 5, 4]), [1, 2, 3, 4, 5], "should be [1,2,3,4,5]")


class TestEmptyList(unittest.TestCase):
    def test_quicksort(self):
        self.assertEqual(quicksort([]), [], "should be []")


class TestSingleElement(unittest.TestCase):
    def test_quicksort(self):
        self.assertEqual(quicksort([10]), [10], "should be [10]")


class TestSortedList(unittest.TestCase):
    def test_quicksort(self):
        self.assertEqual(quicksort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5], "should be [1,2,3,4,5]")


class TestNonUniqueList(unittest.TestCase):
    def test_quicksort(self):
        self.assertEqual(quicksort([5, 3, 6, 2, 5, 1, 2, 1, 4, 5, 6, 7]), [1, 1, 2, 2, 3, 4, 5, 5, 5, 6, 6, 7],
                         "should be [1, 1, 2, 2, 3, 4, 5, 5, 5, 6, 6, 7]")


class TestReversedList(unittest.TestCase):
    def test_quicksort(self):
        self.assertEqual(quicksort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5], "should be [1, 2, 3, 4, 5]")

