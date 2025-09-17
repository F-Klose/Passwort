import unittest
import sys
import os
import passwort_verschlüsselung

class TestVerschluesselung(unittest.TestCase):
    def test_verschluesselung_und_entschluesselung(self):
        original_passwort = "MeinSicheresPasswort123!"
        verschluesseltes_passwort = passwort_verschlüsselung.verschluesseln(original_passwort)
        entschluesseltes_passwort = passwort_verschlüsselung.entschluesseln(verschluesseltes_passwort)
        self.assertEqual(original_passwort, entschluesseltes_passwort)      