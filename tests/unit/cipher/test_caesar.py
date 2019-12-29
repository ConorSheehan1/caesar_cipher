import unittest
from src.cipher.caesar import encrypt


class TestCaesar(unittest.TestCase):
    """
    caesar cipher should move [a-zA-Z] in a circular list.
    it should ignore all other characters, e.g. punctuation. A!, 1 -> B!
    it should preserve capitalization. e.g. AsDf, 2 -> CuFh.
    """

    def test_encrypt_case_sensitive(self):
        assert encrypt("Hello World!", 1) == "Ifmmp Xpsme!"

    def test_decrypt(self):
        """Using a negative value for the offset should undo the encryption"""
        assert encrypt("Ifmmp Xpsme!", -1) == "Hello World!"

    def test_no_change(self):
        """Using 0 as the offset value should not change the result at all"""
        assert encrypt("asdf", 0) == "asdf"


if __name__ == "__main__":
    unittest.main()
