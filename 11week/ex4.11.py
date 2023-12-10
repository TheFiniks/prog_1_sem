import unittest
from Caesar import Caesar
from random import randint


class TestOrdinaryEncode(unittest.TestCase):
    def test_caesar(self):
        key = 10
        self.assertEqual(Caesar(key).encode('Привет!'), 'Щътлоь!', "should be Щътлоь!")


class TestOrdinaryDecode(unittest.TestCase):
    def test_caesar(self):
        key = 13
        self.assertEqual(Caesar(key).decode('Дсэъмл Ьляъхгм'), 'Черная Пятница', "should be Черная Пятница")


class TestEmptyWord(unittest.TestCase):
    def test_caesar(self):
        key = randint(0, 33)
        self.assertEqual(Caesar(key).encode(''), '', "should be ''")
        self.assertEqual(Caesar(key).decode(''), '', "should be ''")


class TestZeroKey(unittest.TestCase):
    def test_caesar(self):
        key = 0
        self.assertEqual(Caesar(key).encode('Бублик'), 'Бублик', "should be Бублик")
        self.assertEqual(Caesar(key).decode('Дырка'), 'Дырка', "should be Дырка")


class TestDoubleAction(unittest.TestCase):
    def test_caesar(self):
        key = randint(0, 33)
        self.assertEqual(Caesar(key).decode(Caesar(key).encode('Константа')), 'Константа', "should be Константа")


class TestEnglishWord(unittest.TestCase):
    def test_caesar(self):
        key = randint(0, 33)
        self.assertEqual(Caesar(key).encode('Would you like a cup of tea?'), 'Would you like a cup of tea?',
                         "should be Would you like a cup of tea?")

