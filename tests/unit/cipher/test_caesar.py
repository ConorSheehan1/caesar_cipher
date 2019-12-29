import unittest
from src.cipher.caesar import encrypt


class TestCaesar(unittest.TestCase):
    """
    caesar cipher should move [a-zA-Z] in a circular list.
    it should ignore all other characters, e.g. punctuation. A!, 1 -> B!
    it should preserve capitalization. e.g. AsDf, 2 -> CuFh.
    """

    def __init__(self, methodName="runTest"):
        unittest.TestCase.__init__(self, methodName)
        self.arg_error_msg = (
            "text must be a string (letters and symbols in quotes) e.g. 'Hi'\n"
            "increment must be an integer (whole number) e.g. 1"
        )

    def test_encrypt_case_sensitive(self):
        assert encrypt("Hello World!", 1) == "Ifmmp Xpsme!"

    def test_decrypt(self):
        """Using a negative value for the offset should undo the encryption"""
        assert encrypt("Ifmmp Xpsme!", -1) == "Hello World!"

    def test_circular_offset(self):
        """uses circular list, so 1 is the same as 27 (26 + 1)"""
        assert encrypt("AsDf", 1) == encrypt("AsDf", 27)

    def test_negative_circular_offset(self):
        """uses circular list, so -1 is the same as 25 (26 - 1)"""
        assert encrypt("AsDf", -1) == encrypt("AsDf", 25)

    def test_no_change(self):
        """Using 0 as the offset value should not change the result at all"""
        assert encrypt("asdf", 0) == "asdf"

    def test_numbers(self):
        """numbers should not change, since they are not in [a-zA-Z]"""
        assert encrypt("1234", 1) == "1234"

    def test_invalid_offset(self):
        """args must be (str, int), not (str, str)"""
        assert encrypt("asdf", "asdf") == self.arg_error_msg

    def test_invalid_text(self):
        """args must be (str, int), not (int, int)"""
        assert encrypt(1, 1) == self.arg_error_msg


if __name__ == "__main__":
    unittest.main()
