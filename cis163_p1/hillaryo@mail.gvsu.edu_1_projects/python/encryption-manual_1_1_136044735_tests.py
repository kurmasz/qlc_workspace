import encrypt
from encrypt import *
import unittest


class TestCases(unittest.TestCase):

    list_of_invalids = [7, ["kitty"], True]


    # SALT TESTS -------------------------------------------------------------------------------------------------------


    def testSalting1(self):  # Actual

        joe = Salting("Joe", " Biden")

        self.assertEqual("Joe Biden", joe.cipher_text, "Salt, Encryption Failed")  # 1
        self.assertEqual("Joe", str(joe), "Salt, Decryption Failed")  # 2

    def testSalting2(self):  # Invalids
        for x in self.list_of_invalids:
            with self.assertRaises(TypeError, msg="Salt, Type Error Not Raised"):  # 3 - 5
                Salting(x, " Biden")

            with self.assertRaises(TypeError, msg="Salt, Type Error Not Raised"):  # 6 - 8
                Salting("Joe", x)

            with self.assertRaises(TypeError, msg="Salt, Type Error Not Raised"):  # 9 - 11
                Salting(x, x)


    # REV TESTS 1 ------------------------------------------------------------------------------------------------------


    def testRev1(self):  # Actual
        joe = encrypt.ReverseCipher1("Joe Biden")
        self.assertEqual("nediB eoJ", joe.cipher_text, "Rev 1, Encryption Failed")  # 1
        self.assertEqual("Joe Biden", str(joe), "Rev 1, Decryption Failed")  # 2

        joe = encrypt.ReverseCipher1("Joe")
        self.assertEqual("eoJ", joe.cipher_text, "Rev 1, Encryption Failed")  # 3
        self.assertEqual("Joe", str(joe), "Rev 1, Decryption Failed")  # 4

    def testRev1(self):  # Invalids
        for x in self.list_of_invalids:
            with self.assertRaises(TypeError, msg="Rev 1, Type Error Not Raised"):  # 5 - 7
                ReverseCipher1(x)


    # REV TEST 2 -------------------------------------------------------------------------------------------------------


    def testRev3(self):  # Actual
        joe = encrypt.ReverseCipher2("Joe Biden")
        self.assertEqual("eoJ nediB", joe.cipher_text, "Rev 2, Encryption Failed")  # 1
        self.assertEqual("Joe Biden", str(joe), "Rev 2, Decryption Failed")  # 2

        joe = encrypt.ReverseCipher1("Joe")
        self.assertEqual("eoJ", joe.cipher_text, "Rev 1, Encryption Failed")  # 3
        self.assertEqual("Joe", str(joe), "Rev 1, Decryption Failed")  # 4

    def testRev4(self):  # Invalids
        for x in self.list_of_invalids:
            with self.assertRaises(TypeError, msg="Rev 2, Type Error Not Raised"):  # 5 - 7
                ReverseCipher1(x)



    # XOR TESTS --------------------------------------------------------------------------------------------------------


    def testXor1(self):  # Actual
        Joe = XORCipher("Hello, Students", "gvsulakers")
        self.assertEqual("/MK6", Joe.cipher_text,
                         "Encryption, Decryption Failed")  # 1
        self.assertEqual("Hello, Students", str(Joe), "Xor, Decryption Failed")  # 2

        Joe = XORCipher("124ABCXYZ-!@", "poopDOG!")
        self.assertEqual('A][1x*BN0', Joe.cipher_text,
                         "Encryption, Decryption Failed")  # 3
        self.assertEqual("124ABCXYZ-!@", str(Joe), "Xor, Decryption Failed")  # 4

    def testXor2(self):  # Invalids
        for x in self.list_of_invalids:
            with self.assertRaises(TypeError, msg="Xor, Type Error Not Raised"):  # 5 - 7
                XORCipher(x, "Key")

            with self.assertRaises(TypeError, msg="Xor, Type Error Not Raised"):  # 8 - 10
                XORCipher("Text", x)

            with self.assertRaises(TypeError, msg="Xor, Type Error Not Raised"):  # 11 - 13
                XORCipher(x, x)


    # CAESAR TESTS -----------------------------------------------------------------------------------------------------


    def testCaesar1(self):  # Actual
        Joe = CaesarCipher("ABC,XWY abc,xwy", 3)
        self.assertEqual("DEF,AZB def,azb", Joe.cipher_text, "Caesar, Failed Encryption")  # 1
        self.assertEqual("ABC,XWY abc,xwy", str(Joe), "Caesar, Failed Decryption")  # 2

    def testCaesar2(self):  # Invalids
        for x in self.list_of_invalids:
            with self.assertRaises(TypeError, msg="Caesar, Type Error Not Raised"):  # 3 - 5
                CaesarCipher(x, 3)
        temp_lst = ["dog",["taco"]]
        for x in temp_lst:
            with self.assertRaises(TypeError, msg=f"Caesar, Type Error Not Raised"):  # 6 - 7
                CaesarCipher("dog", x)


    # VIGENERE TESTS ---------------------------------------------------------------------------------------------------


    def testVigenere1(self):  # Actual
        Joe = VigenereCipher("Taco cat", "123abc")
        self.assertEqual("Ucfo ebv", Joe.cipher_text, "Vigenere, Failed Encryption")  # 1
        self.assertEqual("Taco cat", str(Joe))  # 2

        Joe = VigenereCipher("123_--_123", "123abc")
        self.assertEqual("123_--_123", Joe.cipher_text, "Vigenere, Failed Encryption")  # 3
        self.assertEqual("123_--_123", str(Joe))  # 4

    def testVigenere2(self):  # Invalids
        for x in self.list_of_invalids:
            with self.assertRaises(TypeError, msg="Vigenere, Type Error Not Raised"):  # 5 - 7
                VigenereCipher(x, "Dog")
            with self.assertRaises(TypeError, msg="Vigenere, Type Error Not Raised"):  # 8 - 10
                 VigenereCipher("Dog", x)
            with self.assertRaises(TypeError, msg="Vigenere, Type Error Not Raised"):  # 11 - 13
                VigenereCipher(x, x)


    # CUSTOM TESTS -----------------------------------------------------------------------------------------------------


    def testCustom1(self):  # Actual
        Joe = CustomMappingCipher("Joe Biden")
        self.assertEqual('%"kmi>&k$', Joe.cipher_text, "Custom, Failed Encryption")  # 1
        self.assertEqual("Joe Biden", str(Joe), "Custom, Failed Decryption")  # 2

    def testCustom2(self):  # Invalids
        for x in self.list_of_invalids:
            with self.assertRaises(TypeError, msg="Custom, Type Error Not Raised"):  # 3 - 5
                CustomMappingCipher(x)


if __name__ == "__main__":
    unittest.main()
