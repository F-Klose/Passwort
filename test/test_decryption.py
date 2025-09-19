import sys
import os
# anpassen wen funktion verbessert wurde 
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from decryption import decryption
import unittest

class TestDecryption(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(decryption("abc", 3), "xez")
        self.assertEqual(decryption("Hallo", 1), "gbkmn")
        self.assertEqual(decryption("Test123!", 2), "rgqv123!")
        self.assertEqual(decryption("äöü", 1), "zfnftf")

    def test_empty(self):
        self.assertEqual(decryption("", 5), "")

    def test_special_chars(self):
        self.assertEqual(decryption("123!?", 4), "123!?")

if __name__ == "__main__":
    unittest.main()