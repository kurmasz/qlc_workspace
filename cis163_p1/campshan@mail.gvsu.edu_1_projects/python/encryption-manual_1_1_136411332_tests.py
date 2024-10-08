import unittest

# Assuming the cipher classes are defined in the same module or imported appropriately.
# For the purpose of this test code, it's assumed they are accessible.

from encrypt import(
    Salting,
    ReverseCipher1,
    ReverseCipher2,
    XORCipher,
    CaesarCipher,
    VigenereCipher,
    CustomMappingCipher
)


class TestCiphers(unittest.TestCase):
    """
    A unittest.TestCase subclass containing test cases for various cipher classes.
    
    This class includes tests for the following cipher implementations:
    - Salting
    - ReverseCipher1
    - ReverseCipher2
    - XORCipher
    - CaesarCipher
    - VigenereCipher
    - CustomMappingCipher
    """
    
    # Tests for Salting
    def test_salting_valid(self):
        """
        Test that Salting correctly concatenates text and salt,
        and that the decrypted text matches the original text.
        """
        text = "hello"
        salt = "123"
        salting = Salting(text, salt)
        self.assertEqual(salting.cipher_text, "hello123")
        self.assertEqual(str(salting), "hello")
    
    def test_salting_empty_salt(self):
        """
        Test that Salting handles an empty salt correctly,
        resulting in cipher_text equal to the original text.
        """
        text = "hello"
        salt = ""
        salting = Salting(text, salt)
        self.assertEqual(salting.cipher_text, "hello")
        self.assertEqual(str(salting), "hello")
    
    def test_salting_empty_text(self):
        """
        Test that Salting handles an empty original text correctly,
        resulting in cipher_text equal to the salt.
        """
        text = ""
        salt = "123"
        salting = Salting(text, salt)
        self.assertEqual(salting.cipher_text, "123")
        self.assertEqual(str(salting), "")
    
    def test_salting_non_string_text(self):
        """
        Test that initializing Salting with a non-string text
        raises a TypeError.
        """
        with self.assertRaises(TypeError):
            Salting(123, "salt")
    
    def test_salting_non_string_salt(self):
        """
        Test that initializing Salting with a non-string salt
        raises a TypeError.
        """
        with self.assertRaises(TypeError):
            Salting("text", 456)
    
    # Tests for ReverseCipher1
    def test_reverse_cipher1_valid(self):
        """
        Test that ReverseCipher1 correctly reverses the text
        and that decrypting returns the original text.
        """
        text = "hello"
        cipher = ReverseCipher1(text)
        self.assertEqual(cipher.cipher_text, "olleh")
        self.assertEqual(str(cipher), "hello")
    
    def test_reverse_cipher1_empty(self):
        """
        Test that ReverseCipher1 handles an empty string correctly,
        resulting in an empty cipher_text.
        """
        text = ""
        cipher = ReverseCipher1(text)
        self.assertEqual(cipher.cipher_text, "")
        self.assertEqual(str(cipher), "")
    
    def test_reverse_cipher1_non_string(self):
        """
        Test that initializing ReverseCipher1 with a non-string
        raises a TypeError.
        """
        with self.assertRaises(TypeError):
            ReverseCipher1(789)
    
    # Tests for ReverseCipher2
    def test_reverse_cipher2_valid(self):
        """
        Test that ReverseCipher2 correctly reverses each word
        individually and that decrypting returns the original text.
        """
        text = "hello world"
        cipher = ReverseCipher2(text)
        self.assertEqual(cipher.cipher_text, "olleh dlrow")
        self.assertEqual(str(cipher), "hello world")
    
    def test_reverse_cipher2_single_word(self):
        """
        Test that ReverseCipher2 correctly handles a single word,
        reversing it properly.
        """
        text = "hello"
        cipher = ReverseCipher2(text)
        self.assertEqual(cipher.cipher_text, "olleh")
        self.assertEqual(str(cipher), "hello")
    
    def test_reverse_cipher2_empty(self):
        """
        Test that ReverseCipher2 handles an empty string correctly,
        resulting in an empty cipher_text.
        """
        text = ""
        cipher = ReverseCipher2(text)
        self.assertEqual(cipher.cipher_text, "")
        self.assertEqual(str(cipher), "")
    
    def test_reverse_cipher2_non_string(self):
        """
        Test that initializing ReverseCipher2 with a non-string
        raises a TypeError.
        """
        with self.assertRaises(TypeError):
            ReverseCipher2(['h', 'e', 'l', 'l', 'o'])
    
    # Tests for XORCipher
    def test_xor_cipher_valid(self):
        """
        Test that XORCipher correctly encrypts and decrypts text,
        resulting in the original text after decryption.
        """
        text = "hello"
        key = "key"
        cipher = XORCipher(text, key)
        decrypted = str(cipher)
        self.assertEqual(decrypted, text)
    
    def test_xor_cipher_empty_text(self):
        """
        Test that XORCipher handles an empty text correctly,
        resulting in an empty cipher_text and successful decryption.
        """
        text = ""
        key = "key"
        cipher = XORCipher(text, key)
        decrypted = str(cipher)
        self.assertEqual(decrypted, text)
        self.assertEqual(cipher.cipher_text, "")
    
    def test_xor_cipher_empty_key(self):
        """
        Test that XORCipher raises a ZeroDivisionError when initialized
        with an empty key, due to modulo by zero in the encryption process.
        """
        text = "hello"
        key = ""
        with self.assertRaises(ZeroDivisionError):
            # Since key_length will be zero, leading to division by zero in modulo operation
            XORCipher(text, key)
    
    def test_xor_cipher_non_string_text(self):
        """
        Test that initializing XORCipher with a non-string text
        raises a TypeError.
        """
        with self.assertRaises(TypeError):
            XORCipher(12345, "key")
    
    def test_xor_cipher_non_string_key(self):
        """
        Test that initializing XORCipher with a non-string key
        raises a TypeError.
        """
        with self.assertRaises(TypeError):
            XORCipher("hello", 67890)
    
    def test_xor_cipher_invalid_cipher_hex_length(self):
        """
        Test that decrypting an XORCipher with an invalid cipher_hex length
        (odd number of characters) raises a ValueError.
        """
        # Manually create a cipher with odd length
        cipher = XORCipher("hi", "k")
        cipher.cipher_text = "abc"  # Invalid length
        with self.assertRaises(ValueError):
            str(cipher)
    
    # Tests for CaesarCipher
    def test_caesar_cipher_valid(self):
        """
        Test that CaesarCipher correctly encrypts and decrypts text
        with a positive key, resulting in the original text after decryption.
        """
        text = "Hello, World!"
        key = 3
        cipher = CaesarCipher(text, key)
        decrypted = str(cipher)
        self.assertEqual(decrypted, text)
    
    def test_caesar_cipher_negative_key(self):
        """
        Test that CaesarCipher correctly handles a negative key,
        allowing for decryption back to the original text.
        """
        text = "Hello, World!"
        key = -3
        cipher = CaesarCipher(text, key)
        decrypted = str(cipher)
        self.assertEqual(decrypted, text)
    
    def test_caesar_cipher_zero_key(self):
        """
        Test that CaesarCipher with a zero key leaves the text unchanged.
        """
        text = "Hello, World!"
        key = 0
        cipher = CaesarCipher(text, key)
        decrypted = str(cipher)
        self.assertEqual(decrypted, text)
    
    def test_caesar_cipher_non_string_text(self):
        """
        Test that initializing CaesarCipher with a non-string text
        raises a TypeError.
        """
        with self.assertRaises(TypeError):
            CaesarCipher(12345, 3)
    
    def test_caesar_cipher_non_int_key(self):
        """
        Test that initializing CaesarCipher with a non-integer key
        raises a TypeError.
        """
        with self.assertRaises(TypeError):
            CaesarCipher("hello", "3")
    
    def test_caesar_cipher_non_alpha_characters(self):
        """
        Test that CaesarCipher leaves non-alphabetic characters unchanged.
        """
        text = "12345!@#$%"
        key = 5
        cipher = CaesarCipher(text, key)
        decrypted = str(cipher)
        self.assertEqual(decrypted, text)
    
    # Tests for VigenereCipher
    def test_vigenere_cipher_valid(self):
        """
        Test that VigenereCipher correctly encrypts and decrypts text
        with a valid key, resulting in the original text after decryption.
        """
        text = "HELLO WORLD"
        key = "KEY"
        cipher = VigenereCipher(text, key)
        decrypted = str(cipher)
        self.assertEqual(decrypted, text)
    
    def test_vigenere_cipher_empty_text(self):
        """
        Test that VigenereCipher handles an empty text correctly,
        resulting in an empty cipher_text and successful decryption.
        """
        text = ""
        key = "KEY"
        cipher = VigenereCipher(text, key)
        decrypted = str(cipher)
        self.assertEqual(decrypted, text)
        self.assertEqual(cipher.cipher_text, "")
    
    def test_vigenere_cipher_non_string_text(self):
        """
        Test that initializing VigenereCipher with a non-string text
        raises a TypeError.
        """
        with self.assertRaises(TypeError):
            VigenereCipher(12345, "KEY")
    
    def test_vigenere_cipher_non_string_key(self):
        """
        Test that initializing VigenereCipher with a non-string key
        raises a TypeError.
        """
        with self.assertRaises(TypeError):
            VigenereCipher("HELLO", 67890)
    
    def test_vigenere_cipher_with_non_alpha_characters(self):
        """
        Test that VigenereCipher leaves non-alphabetic characters unchanged
        during encryption and decryption.
        """
        text = "HELLO, WORLD!"
        key = "KEY"
        cipher = VigenereCipher(text, key)
        decrypted = str(cipher)
        self.assertEqual(decrypted, text)
    
    # Tests for CustomMappingCipher
    def test_custom_mapping_cipher_valid(self):
        """
        Test that CustomMappingCipher correctly maps and reverses the mapping,
        resulting in the original text after decryption.
        """
        text = "Hello, World!"
        cipher = CustomMappingCipher(text)
        decrypted = str(cipher)
        self.assertEqual(decrypted, text)
    
    def test_custom_mapping_cipher_empty(self):
        """
        Test that CustomMappingCipher handles an empty string correctly,
        resulting in an empty cipher_text and successful decryption.
        """
        text = ""
        cipher = CustomMappingCipher(text)
        decrypted = str(cipher)
        self.assertEqual(decrypted, text)
        self.assertEqual(cipher.cipher_text, "")
    
    def test_custom_mapping_cipher_non_string(self):
        """
        Test that initializing CustomMappingCipher with a non-string
        raises a TypeError.
        """
        with self.assertRaises(TypeError):
            CustomMappingCipher(12345)
    
    def test_custom_mapping_cipher_unmapped_characters(self):
        """
        Test that CustomMappingCipher leaves characters not present in the
        mapping unchanged during encryption and decryption.
        """
        # Characters not in the mapping should remain unchanged
        text = "This is a test: 12345!@#"
        cipher = CustomMappingCipher(text)
        decrypted = str(cipher)
        self.assertEqual(decrypted, text)
    
    def test_custom_mapping_cipher_case_sensitivity(self):
        """
        Test that CustomMappingCipher correctly handles case sensitivity,
        ensuring that both uppercase and lowercase letters are mapped and
        decrypted accurately.
        """
        text = "aAbB"
        cipher = CustomMappingCipher(text)
        decrypted = str(cipher)
        self.assertEqual(decrypted, text)


if __name__ == '__main__':
    unittest.main()
