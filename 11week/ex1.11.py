from prime_factors import prime_factors
import unittest


class TestOrdinaryNumber(unittest.TestCase):
    def test_prime_factors(self):
        self.assertEqual(prime_factors('12'), '2^2*3', "should be 2^2*3")


class TestEmptyData(unittest.TestCase):
    def test_prime_factors(self):
        self.assertEqual(prime_factors(''), '-1', "should be -1")


class TestZero(unittest.TestCase):
    def test_prime_factors(self):
        self.assertEqual(prime_factors('0'), '0', "should be 0")


class TestNegativeNumber(unittest.TestCase):
    def test_prime_factors(self):
        self.assertEqual(prime_factors('-6'), '-2*3', "should be -2*3")


class TestWrongAnswer(unittest.TestCase):
    def test_prime_factors(self):
        self.assertNotEqual(prime_factors('1'), '1*1', "should not be 1*1")

