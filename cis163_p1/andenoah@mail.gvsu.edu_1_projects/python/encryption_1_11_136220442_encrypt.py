"""A module that contains multiple different methods of encryption.
"""

character_map = {
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

class Salting:
    """An encryption method that appends a salt to the unencrypted text.

    Attributes:
        cipher_text (str): The encrypted text.
        salt (str): The salt that is appended to the unencrypted text.
    """

    def __init__(self, text: str, salt: str):
        """Initializes a salt cipher.

        Arguments:
            text (str): The text to salt.
            salt (str): The salt to append to the text.
        """

        if not (isinstance(text, str) and isinstance(salt, str)):
            raise TypeError

        self.cipher_text = text + salt
        self.salt = salt
    
    def __str__(self):
        """Decrypts the encrypted text.

        Returns:
            str
        """

        return self.cipher_text.replace(self.salt, "")

class ReverseCipher1:
    """An encryption method that reverses the unencrypted text.

    Attributes:
        cipher_text (str): The encrypted text.
    """

    def __init__(self, text: str):
        """Initializes a reverse cipher.

        Arguments:
            text (str): The text to encrypt.
        """

        if not isinstance(text, str):
            raise TypeError
        
        self.cipher_text = ReverseCipher1.reverse_text(text)
    
    def __str__(self):
        """Decrypts the encrypted text.

        Returns:
            str
        """

        return ReverseCipher1.reverse_text(self.cipher_text)
    
    def reverse_text(text: str) -> str:
        """Reverses the given text.

        Arguments:
            text (str): The text to reverse.
        
        Returns:
            str
        """

        if not isinstance(text, str):
            raise TypeError

        reversed_text = ""

        for i in range(len(text) - 1, -1, -1):
            reversed_text += text[i]
        
        return reversed_text

class ReverseCipher2:
    """An encryption method that reverses each word of some text.

    Attributes:
        cipher_text (str): The encrypted text.
    """

    def __init__(self, text: str):
        """Initializes a reverse cipher 2.

        Arguments:
            text (str): The text to encrypt.
        """

        if not isinstance(text, str):
            raise TypeError
        
        self.cipher_text = ReverseCipher2.reverse_words(text)
    
    def __str__(self):
        """Decrypts the encrypted text.

        Returns:
            str
        """

        return ReverseCipher2.reverse_words(self.cipher_text)
    
    def reverse_words(text: str) -> str:
        """Reverses each word of the given text.

        Arguments:
            text (str): The text to reverse each word of.
        
        Returns:
            str
        """

        reversed_text = ""

        for word in text.split():
            for i in range(len(word) - 1, -1, -1):
                reversed_text += word[i]
            
            reversed_text += " "
        
        return reversed_text[:-1]

class XORCipher:
    """An encryption method that performs an XOR operation between some text and a key.

    Attributes:
        cipher_text (str): The encrypted text.
        key (str): The key for the text.
    """

    def __init__(self, text: str, key: str):
        """Initializes a XOR cipher.

        Arguments:
            text (str): The text to encrypt.
            key (str): The key to encrypt the text with.
        """

        if not (isinstance(text, str) and isinstance(key, str)):
            raise TypeError
        
        if not key:
            raise ValueError
        
        self.cipher_text = XORCipher.encrypt_text(text, key)
        self.key = key
    
    def __str__(self):
        """Decrypts the encrypted text.

        Returns:
            str
        """

        return XORCipher.encrypt_text(self.cipher_text, self.key)
    
    def encrypt_text(text: str, key: str) -> str:
        """Encrypts the given text by performing an XOR operation between itself and the given key.

        Arguments:
            text (str): The text to encrypt.
            key (str): The key to encrypt the text with.
        """

        if not (isinstance(text, str) and isinstance(key, str)):
            raise TypeError
        
        encrypted_text = ""

        for i in range(len(text)):
            encrypted_text += chr(ord(text[i]) ^ ord(key[i % len(key)]))
        
        return encrypted_text

class CaesarCipher:
    """An encryption method that shifts the value of each letter of some text by some amount.

    Attributes:
        cipher_text (str): The encrypted text.
        key (int): The key for the text.
    """

    def __init__(self, text: str, key: int):
        """Initializes a caesar cipher.

        Arguments:
            text (str): The text to encrypt.
            key (int): The amount to shift the value of each letter of the text by.
        """

        if not (isinstance(text, str) and isinstance(key, int)):
            raise TypeError
        
        self.cipher_text = CaesarCipher.encrypt_text(text, key)
        self.key = key
        
    def __str__(self):
        """Decrypts the encrypted text.

        Returns:
            str
        """

        return CaesarCipher.encrypt_text(self.cipher_text, -self.key)
    
    def encrypt_text(text: str, key: int) -> str:
        """Encrypts the given text by shifting the value of each letter of the text by the given key.

        Arguments:
            text (str): The text to encrypt.
            key (int): The key to encrypt the text with.
        
        Returns:
            str
        """

        if not (isinstance(text, str) and isinstance(key, int)):
            raise TypeError
        
        encrypted_text = ""

        for character in text:            
            if character.isalpha():
                new_character = chr(64 + ((ord(character.upper()) - 64 + key) % 26))

                if character.islower():
                    new_character = new_character.lower()
                
                encrypted_text += new_character
            else:
                encrypted_text += character
    
        return encrypted_text

class VigenereCipher:
    """An encryption method that shifts the value of each letter of some text by the value of each letter of some key.

    Attributes:
        cipher_text (str): The encrypted text.
        key (str): The key for the text.
    """

    def __init__(self, text: str, key: str):
        """Initializes a vigenere cipher.

        Arguments:
            text (str): The text to encrypt.
            key (str): The key to encrypt the text with.
        """

        if not (isinstance(text, str) and isinstance(key, str)):
            raise TypeError
        
        self.cipher_text = VigenereCipher.cipher(text, key)
        self.key = key
    
    def __str__(self):
        """Decrypts the encrypted text.

        Returns:
            str
        """

        return VigenereCipher.cipher(self.cipher_text, self.key, True)
    
    def cipher(text: str, key: str, decrypt: bool = False) -> str:
        """Encrypts or decrypts the given text with the given key.

        Arguments:
            text (str): The text to encrypt or decrypt.
            key (str): The key to encrypt or decrypt the text with.
            decrypt (bool): Whether or not to decrypt the given text. Default is False.
        
        Returns:
            str
        """

        if not (isinstance(text, str) and isinstance(key, str) and isinstance(decrypt, bool)):
            raise TypeError
        
        encrypted_text = ""

        for i in range(len(text)):
            if text[i].isalnum():
                character = key[i % len(key)]
                offset = 0

                if character.isalpha():
                    offset = ord(character.upper()) - 65
                elif character.isnumeric():
                    offset = int(character)
                    
                if decrypt:
                    offset *= -1
                    
                new_character = chr(65 + (ord(text[i].upper()) - 65 + offset) % 26)

                if text[i].islower():
                    new_character = new_character.lower()
                
                encrypted_text += new_character
            else:
                encrypted_text += text[i]

        return encrypted_text

class CustomMappingCipher:
    """An encryption method that, if possible, maps the value of each letter of some text to its corresponding value in a stored map.

    Attributes:
        cipher_text (str): The encrypted text.
    """

    def __init__(self, text: str):
        """Initializes a custom mapping cipher.

        Arguments:
            text (str): The text to encrypt.
        """

        if not isinstance(text, str):
            raise TypeError

        self.cipher_text = CustomMappingCipher.encrypt_text(text)
    
    def __str__(self):
        """Decrypts the encrypted text.

        Returns:
            str
        """

        return self.decrypted()

    def decrypted(self) -> str:
        """Decrypts the encrypted text by, if possible, mapping the value of each letter to its corresponding value in a stored map.

        Returns:
            str
        """

        encrypted_text = ""
        
        for character in self.cipher_text:
            if character in character_map.values():
                found_key = False

                for key, value in character_map.items():
                    if value == character:
                        encrypted_text += key
                        found_key = True
                        break
                
                if not found_key:
                    encrypted_text += character
        
        return encrypted_text
    
    def encrypt_text(text: str) -> str:
        """Encrypts the given text by, if possible, mapping the value of each letter to its corresponding value in a stored map.

        Attributes:
            text (str): The text to encrypt.
        
        Returns:
            str
        """

        if not isinstance(text, str):
            raise TypeError
        
        encrypted_text = ""

        for character in text:
            if character in character_map.keys():
                encrypted_text += character_map[character]
            else:
                encrypted_text += character
        
        return encrypted_text
