import unittest
from encrypt import *

class CipherTestCase(unittest.TestCase):
    def test_salting(self):
        self.assertEqual(Salting("Hello, Students", " gvsulakers").cipher_text, "Hello, Students gvsulakers")
        self.assertEqual(Salting("GVSU", " gvsulakers").cipher_text, "GVSU gvsulakers")
    
    def test_reverse_cipher_1(self):
        self.assertEqual(ReverseCipher1("Hello World!").cipher_text, "!dlroW olleH")
        self.assertEqual(ReverseCipher1("GVSULakers").cipher_text, "srekaLUSVG")
    
    def test_reverse_cipher_2(self):
        self.assertEqual(ReverseCipher2("Hello World!").cipher_text, "olleH !dlroW")
        self.assertEqual(ReverseCipher2("GVSULakers").cipher_text, "srekaLUSVG")
    
    def test_xor_cipher(self):
        self.assertEqual(XORCipher("Hello, Students", "gvsu").cipher_text, "/\x13\x1f\x19\x08ZS&\x13\x03\x17\x10\t\x02\x00")
    
    def test_caesar_cipher(self):
        self.assertEqual(CaesarCipher("HELLO", 3).cipher_text, "KHOOR")
        self.assertEqual(CaesarCipher("GvsuLakers", 6).cipher_text, "MbyaRgqkxy")
    
    def test_vigenere_cipher(self):
        self.assertEqual(VigenereCipher("HELLO", "KEYKE").cipher_text, "RIJVS")
        self.assertEqual(VigenereCipher("Hello Students", "163").cipher_text, "Ikomu Tzxekquy")
    
    def test_custom_mapping_cipher(self):
        self.assertEqual(CustomMappingCipher("Hello Students. Welcome to GVSU!").cipher_text, "gkPP\"m5oK&k$o~*m+kP/\"Vkmo\"my15YQ")

def main():
    unittest.main()

if __name__ == "__main__":
    main()
