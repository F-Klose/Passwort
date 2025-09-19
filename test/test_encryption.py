import sys
import os
<<<<<<< HEAD:test/test_verschlüsselung.py
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from verschluesselung import verschluesselung
import unittest

class TestVerschluesselung(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(verschluesselung("abc", 3), "dyf")
        self.assertEqual(verschluesselung("Hallo", 1), "izmkp")
        self.assertEqual(verschluesselung("Test123!", 2), "vcur123!")
        self.assertEqual(verschluesselung("äöü", 1), "bdpdvd")

    def test_empty(self):
        self.assertEqual(verschluesselung("", 5), "")

    def test_special_chars(self):
        self.assertEqual(verschluesselung("123!?", 4), "123!?")

if __name__ == "__main__":
    unittest.main()
=======
import password_encryption
>>>>>>> 0bc394f219c0e948e0b4a8297c6c9aec5b8e59bf:test/test_encryption.py
