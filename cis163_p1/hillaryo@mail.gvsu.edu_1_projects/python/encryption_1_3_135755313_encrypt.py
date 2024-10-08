"""
encrypt.py
This is a collection of classes and functions that all encrypt text in different ways
Owen Hillary, 9/18/24, Version 1
"""
"""---------------------------------------------------------------------------------------------------------------------
----------------- Functions --------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------------------------"""


def find_shift(text: str) -> int:
    """
    Find the shift associated with a letter for Vigenere Cipher

    :param text: a string containing a single numeric or alphabetic character
    :return: integer value 0 - 25 based on the inputs character alphabetic or numeric position
    """

    if text.isnumeric():  # Returns number if input is a number
        return int(text)
    elif text.isalpha():  # Returns number based on  inputs alphabetic position
        return ord(text.upper()) - ord("A")


def looping_alphabet(letter: str, change: int) -> str:
    """
    Shifts a letter based on the changes value, loops back to A or Z when value is shift passed them.
    Does not mutilate input.

    :param letter: Alphabetic letter to be changer
    :param change: Number of shift
    :return: Shifted Alphabetic unit
    """

    if letter.isalpha():  # Ensures letter is alpha in alphabet
        if ord(letter.upper()) + change > ord("Z"):  # Loops letter if change will be greater than alphabet
            change -= 26
        elif ord(letter.upper()) + change < ord("A"):  # Loops letter if change will be less than alphabet
            change += 26

        return chr(ord(letter) + change)  # Returns changed letter
    else:
        return letter


def looping_key(text: str, key: str) -> str:
    """
    Loops input key to match length of text string

    :param text: Text for length reference
    :param key: key to be looped
    :return: String of looped key
    """

    new_key = key  # Value of new key

    while len(new_key) < len(text):  # Loops key until it reaches desired length
        for x in key:
            if len(key) < len(text):
                new_key += x
    return new_key


def owens_reveres(input_str: str) -> str:
    """
    Returns a string that is reversed

    :param input_str: String to be reversed
    :return: Value for reversed string
    """

    temp_string = str()  # Temp Var for changed string
    for x in input_str:
        temp_string = x + temp_string
    return temp_string


def return_key(value: str, dic: dict) -> str:
    """
    Return what key value is associated with an item, in a dictionary where every item has unique key.

    :param value: Unique item
    :param dic: Dictionary being searched
    :return: Key for item
    """
    for key, val in dic.items():
        if value == val:
            return key


def the_caesar_cipher(text: str, key: int) -> str:
    """
    Calls looping_alphabet for each letter in text by value key and returns a whole string

    :param text: Text to be changed
    :param key: Int value to change text by
    :return: String of changed letters
    """

    temp_string = str()  # Temp Var for changed string

    for x in text:
        temp_string += looping_alphabet(x, key)

    return temp_string


def the_vigenere_cipher(text: str, key: str, mod: int = 1) -> str:
    """
    Calls looping_alphabet for each letter in text by the find_shift value of  key value and returns a whole string

    :param text: Text to be changed
    :param key: Int value to change text by
    :param mod: Controls direction of change
    :return: String of changed letters
    """

    temp_string = str()  # Temp Var for changed string

    for x in range(len(text)):
        temp_string += looping_alphabet(text[x], find_shift(key[x]) * mod)
    return temp_string


def the_xor_cipher(text: str, key: str) -> str:
    """
    X or's the binary values of each letter of Text and String, providing a new binary value, that is then convert to a
    charter, that is then added to a string

    :param text: String of text to be ciphered
    :param key: String for text to be compared to
    :return: String of new binary's base ten ASCII character
    """

    temp_string = str()  # Temp Var for changed string

    for x in range(len(text)):

        newBin = str()  # Value for new binary number

        # Converts both letters of the same order to binary, limits to 8 characters, fills to 8 with 0 if less than
        bin1 = f'{(bin(int(str(ord(key[x]))))[2:10:]):0>8}'
        bin2 = f'{(bin(int(str(ord(text[x]))))[2:10:]):0>8}'


        for i in range(len(bin1)):  # X or for each number of bin
            if int(bin1[i]) ^ int(bin2[i]):
                newBin += "1"
            else:
                newBin += "0"

        temp_string += chr(int(newBin, base=2))  # Convertion of new bin to letter

    return temp_string


def valid_type(var: list, val_type):
    """
    Takes multiple input values and raises error if any of them are not instance of val_type

    :param var: List of variables that need to be checked for validity
    :param val_type:
    :return:  none
    """

    if not isinstance(var, list):  # Check to ensure var is list
        raise TypeError


    for x in var:
        if not isinstance(x, val_type):  # Check if x is valid
            raise TypeError


"""---------------------------------------------------------------------------------------------------------------------
----------------- Classes ----------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------------------------"""


class Salting:
    """
    This class encrypts text by "Slating", a process in which adds a random text(called a salt) to the actual text.

        Attributes:
        self.Salt - salt to add on to word
        self.Cipher_text - encrypted text
    """
    def __init__(self, text: str, salt: str):
        valid_type([text, salt], str)

        self.salt: str = salt
        self.cipher_text = text + salt

    def __str__(self):
        return self.cipher_text[0:len(self.cipher_text) - len(self.salt):]  # returns cipher text without salt


class ReverseCipher1:
    """
    This class encrypts text by reversing the whole string.

        Attributes:
        self.Cipher_text - encrypted text
    """

    def __init__(self, text: str):
        valid_type([text], str)

        self.cipher_text = owens_reveres(text)

    def __str__(self):
        return owens_reveres(self.cipher_text)


class ReverseCipher2:
    """
    This class encrypts text by reversing each word of a string.

        Attributes:
        self.Cipher_text - encrypted text
    """

    def __init__(self, text: str):
        valid_type([text], str)
        self.cipher_text = " ".join([owens_reveres(i) for i in text.split()])

    def __str__(self):
        return 


class XORCipher:" ".join([owens_reveres(i) for i in self.cipher_text.split()])
    """
    This class encrypts text by taking a key value and will perform XOR operation between the binary of each character
    of the text
    and the key.

        Attributes:
        self.key - looped input key
        self.Cipher_text - encrypted text

    """

    def __init__(self, text: str, key: str):
        valid_type([text, key], str)

        self.key = looping_key(text, key)
        self.cipher_text = the_xor_cipher(text, self.key)

    def __str__(self):
        return the_xor_cipher(self.cipher_text, self.key)


class CaesarCipher:
    """
    This class encrypts text by shifting character based on a key value.

        Attributes:
        self.key - value of shift
        self.Cipher_text - encrypted text

    """
    def __init__(self, text: str, key: int):
        valid_type([text], str)
        valid_type([key], int)

        self.key = key
        self.cipher_text = the_caesar_cipher(text, key)

    def __str__(self):
        return the_caesar_cipher(self.cipher_text, self.key * -1)


class VigenereCipher:
    """
    This class encrypts text by shifting character based on the values of the charters in an input string.

        Attributes:
        self.key - shifting key
        self.Cipher_text - encrypted text

    """


    def __init__(self, text: str, key: str):
        valid_type([text, key], str)

        self.key = looping_key(text, key).upper()
        self.cipher_text = the_vigenere_cipher(text, self.key)

    def __str__(self):
        return the_vigenere_cipher(self.cipher_text, self.key, -1)


class CustomMappingCipher:
    """
    This class encrypts text by matching each character to a value in a specific map.

        Attributes:
        self.Cipher_text - encrypted text

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

    def __init__(self, text: str):
        valid_type([text], str)
        self.cipher_text = "".join([self.character_map[x] for x in text])

    def __str__(self):
        return "".join([return_key(x, self.character_map) for x in self.cipher_text])
