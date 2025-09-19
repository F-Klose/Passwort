import sys
import os
# anpassen wen funktion verbessert wurde
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from encryption import encryption

class TestenEncryption(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(encryption("dyf", 3), "gvi")
        self.assertEqual(encryption("izmkp", 1), "jynjq")
        self.assertEqual(encryption("vcur123!", 2), "xawp123!")
        self.assertEqual(encryption("bfp", 1), "ceq")  



if __name__ == "__main__":
    unittest.main()