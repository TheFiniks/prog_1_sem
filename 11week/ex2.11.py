import unittest
from MNK import MNK


class TestOrdinaryLists(unittest.TestCase):
    def test_MNK(self):
        self.assertEqual(MNK([1, 2, 3, 4], [2, 4, 6, 8]), (2.0, 0.0), "should be (2.0, 0.0)")


class TestEmptyLists(unittest.TestCase):
    def test_MNK(self):
        self.assertEqual(MNK((), ()), 'no data', "required data doesn't exist")


class TestListsOfZeros(unittest.TestCase):
    def test_MNK(self):
        self.assertEqual(MNK([0], [0]), (0.0, 0.0), "should be (0.0, 0.0)")


class TestListsWithDifferentLength(unittest.TestCase):
    def test_MNK(self):
        self.assertEqual(MNK([1, 2, 3], [4, 5]), 'dif size', "different amount of data")

