
class Salting:
    """
    A class to represent the Salting encryption method.

    Attributes:
    
    cipher_text : str
        The encrypted text after adding the salt.
    salt : str
        The salt to be added to the original text.
    """

    def __init__(self, text: str, salt: str):
        if not isinstance(text, str):
            raise TypeError("Text must be a string.")
        if not isinstance(salt, str):
            raise TypeError("Salt must be a string.")
        
        self.cipher_text = text + salt  
        self.salt = salt

    def __str__(self):
        """
        Returns the original text by removing the salt.
        """
        return self.cipher_text[:-len(self.salt)]


class ReverseCipher1:
    """
    A class to represent the Reverse String encryption method.
    """

    def __init__(self, text: str):
        if not isinstance(text, str):
            raise TypeError("Text must be a string.")
        self.cipher_text = self.reverse_text(text)

    def reverse_text(self, text: str) -> str:
        reversed_text = ""
        for char in text:
            reversed_text = char + reversed_text  
        return reversed_text

    def __str__(self):
        """
        Returns the original text by reversing the cipher_text.
        """
        return self.reverse_text(self.cipher_text)


class ReverseCipher2:
    """
    A class to represent the Reverse String encryption method - version 2.
    """

    def __init__(self, text: str):
        if not isinstance(text, str):
            raise TypeError("Text must be a string.")
        self.cipher_text = self.reverse_words(text)

    def reverse_words(self, text: str) -> str:
        words = text.split(' ')  
        reversed_words = []
        
        for word in words:
            reversed_word = ""
            for char in word:
                reversed_word = char + reversed_word  
            reversed_words.append(reversed_word)

        return " ".join(reversed_words)

    def __str__(self):
        """
        Returns the original text by reversing each word in the cipher_text.
        """
        return self.reverse_words(self.cipher_text)


class XORCipher:
    def __init__(self, text: str, key: str):
        if not isinstance(text, str):
            raise TypeError("Text must be a string.")
        if not isinstance(key, str):
            raise TypeError("Key must be a string.")
        self.key = key
        self.cipher_text = self._encrypt(text, key)

    def __str__(self):
        return self._decrypt(self.cipher_text, self.key)

    def _encrypt(self, text: str, key: str) -> str:
        cipher_hex = ''
        key_length = len(key)
        for i, c in enumerate(text):
            xor_val = ord(c) ^ ord(key[i % key_length])
            high_nibble = xor_val // 16
            low_nibble = xor_val % 16
            cipher_hex += self._nibble_to_hex(high_nibble) + self._nibble_to_hex(low_nibble)
        return cipher_hex

    def _decrypt(self, cipher_hex: str, key: str) -> str:
        decrypted_text = ''
        key_length = len(key)
        if len(cipher_hex) % 2 != 0:
            raise ValueError("Invalid cipher hex length. It should be even.")
        for i in range(0, len(cipher_hex), 2):
            hex_pair = cipher_hex[i:i+2]
            byte_val = self._hex_to_byte(hex_pair)
            key_char = key[(i // 2) % key_length]
            decrypted_char = chr(byte_val ^ ord(key_char))
            decrypted_text += decrypted_char
        return decrypted_text

    def _nibble_to_hex(self, nibble: int) -> str:
        if 0 <= nibble <= 9:
            return chr(ord('0') + nibble)
        elif 10 <= nibble <= 15:
            return chr(ord('a') + nibble - 10)
        else:
            raise ValueError("Nibble must be between 0 and 15.")

    def _hex_to_byte(self, hex_pair: str) -> int:
        high_nibble = self._hex_char_to_nibble(hex_pair[0])
        low_nibble = self._hex_char_to_nibble(hex_pair[1])
        return high_nibble * 16 + low_nibble

    def _hex_char_to_nibble(self, char: str) -> int:
        if '0' <= char <= '9':
            return ord(char) - ord('0')
        elif 'a' <= char.lower() <= 'f':
            return ord(char.lower()) - ord('a') + 10
        else:
            raise ValueError(f"Invalid hexadecimal character: {char}")



class CaesarCipher:
    """A class to represent the Caesar Cipher encryption method."""

    def __init__(self, text: str, key: int):
        if not isinstance(text, str):
            raise TypeError("Text must be a string.")
        if not isinstance(key, int):
            raise TypeError("Key must be an integer.")
        self.cipher_text = self._caesar_cipher(text, key)
        self.key = key

    def __str__(self):
        """
        Returns the original text by decrypting the cipher_text.
        """
        return self._caesar_cipher(self.cipher_text, -self.key)

    def _caesar_cipher(self, text: str, key: int) -> str:
        encrypted_text = []
        for char in text:
            if char.isalpha():
                shift = ord('A') if char.isupper() else ord('a')
                encrypted_char = chr((ord(char) - shift + key) % 26 + shift)
                encrypted_text.append(encrypted_char)
            else:
                encrypted_text.append(char)
        return ''.join(encrypted_text)


class VigenereCipher:
    """A class to represent the Vigenère Cipher encryption method."""

    def __init__(self, text: str, key: str):
        if not isinstance(text, str):
            raise TypeError("Text must be a string.")
        if not isinstance(key, str):
            raise TypeError("Key must be a string.")
        self.cipher_text = self._vigenere_cipher(text, key)
        self.key = key

    def __str__(self):
        """
        Returns the original text by decrypting the cipher_text.
        """
        return self._vigenere_decrypt(self.cipher_text, self.key)

    def _vigenere_cipher(self, text: str, key: str) -> str:
        encrypted_text = []
        key_length = len(key)
        key_indices = [self._char_to_shift(k) for k in key]
        for i, char in enumerate(text):
            if char.isalpha():
                shift = ord('A') if char.isupper() else ord('a')
                total_shift = key_indices[i % key_length]
                encrypted_char = chr((ord(char) - shift + total_shift) % 26 + shift)
                encrypted_text.append(encrypted_char)
            else:
                encrypted_text.append(char)
        return ''.join(encrypted_text)

    def _vigenere_decrypt(self, text: str, key: str) -> str:
        decrypted_text = []
        key_length = len(key)
        key_indices = [self._char_to_shift(k) for k in key]
        for i, char in enumerate(text):
            if char.isalpha():
                shift = ord('A') if char.isupper() else ord('a')
                total_shift = key_indices[i % key_length]
                decrypted_char = chr((ord(char) - shift - total_shift) % 26 + shift)
                decrypted_text.append(decrypted_char)
            else:
                decrypted_text.append(char)
        return ''.join(decrypted_text)

    def _char_to_shift(self, char: str) -> int:
        """
        Converts a character to a shift value.
        For letters: A/a=0, B/b=1, ..., Z/z=25
        For digits: '0'=0, '1'=1, ..., '9'=9
        For other characters: defaults to 0.
        """
        if char.isupper() or char.islower():
            return ord(char.upper()) - ord('A')
        elif char.isdigit():
            return ord(char) - ord('0')
        else:
            return 0  


class CustomMappingCipher:
    """A class to represent a Custom Character Mapping Cipher."""

    def __init__(self, text: str):
        if not isinstance(text, str):
            raise TypeError("Text must be a string.")
        self.map = {
            'a': ',', 'b': 'c', 'c': '/', 'd': '&', 'e': 'k', 'f': '}', 'g': '4', 'h': 'w', 
            'i': '>', 'j': 'b', 'k': 'W', 'l': 'P', 'm': 'V', 'n': '$', 'o': '"', 'p': '`', 
            'q': 'U', 'r': 'x', 's': '~', 't': 'o', 'u': 'K', 'v': 'B', 'w': ']', 'x': 'e', 
            'y': '[', 'z': '7', 'A': 'H', 'B': 'i', 'C': 'G', 'D': 's', 'E': ';', 'F': 'A', 
            'G': 'y', 'H': 'g', 'I': 'r', 'J': '%', 'K': 'p', 'L': '^', 'M': 'C', 'N': '6', 
            'O': 'O', 'P': '8', 'Q': '3', 'R': '\\', 'S': '5', 'T': '0', 'U': 'Y', 'V': '1', 
            'W': '+', 'X': '{', 'Y': '2', 'Z': 'D', '0': '(', '1': '=', '2': '?', '3': 'q', 
            '4': '<', '5': 't', '6': 'f', '7': 'L', '8': '|', '9': 'l', '!': 'Q', '"': 'F', 
            '#': 'h', '$': ')', '%': 'X', '&': 'd', "'": 'j', '(': '.', ')': 'v', '*': 'E', 
            '+': "'", ',': '#', '-': '@', '.': '*', '/': 'z', ':': 'S', ';': ':', '<': 'N', 
            '=': 'Z', '>': ' ', '?': 'T', '@': '-', '[': 'R', '\\': 'u', ']': 'M', '^': '9', 
            '_': '_', '`': 'a', '{': 'n', '|': 'I', '}': 'J', '~': '!', ' ': 'm'
        }
        self.cipher_text = self._custom_map(text)
        # Create reverse mapping for decryption
        self.reverse_map = {v: k for k, v in self.map.items()}

    def _custom_map(self, text: str) -> str:
        return ''.join(self.map.get(char, char) for char in text)

    def _reverse_custom_map(self, text: str) -> str:
        return ''.join(self.reverse_map.get(char, char) for char in text)

    def __str__(self):
        """
        Returns the original text by decrypting the cipher_text using the reverse mapping.
        """
        return self._reverse_custom_map(self.cipher_text)
