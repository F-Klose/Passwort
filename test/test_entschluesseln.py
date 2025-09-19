import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from entschluesselung import entschluesselung

class TestEntschluesselung(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(entschluesselung("dyf", 3), "abc")
        self.assertEqual(entschluesselung("izmkp", 1), "hallo")
        self.assertEqual(entschluesselung("vcur123!", 2), "test123!")
        self.assertEqual(entschluesselung("bfp", 1), "ago")  

if __name__ == "__main__":
    unittest.main()