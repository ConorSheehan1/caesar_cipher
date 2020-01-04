import unittest
from src.cipher.caesar import encrypt, trans_tables


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

    def test_trans_tables(self):
        """should return lower and uppercase translation tables"""
        lc_trans_table = {v: v + 2 for v in range(97, 121)}
        lc_trans_table[121] = 97
        lc_trans_table[122] = 98

        uc_trans_table = {v: v + 2 for v in range(65, 89)}
        uc_trans_table[89] = 65
        uc_trans_table[90] = 66

        actual_lc_trans_table, actual_uc_trans_table = trans_tables(2)
        self.assertDictEqual(lc_trans_table, actual_lc_trans_table)
        self.assertDictEqual(uc_trans_table, actual_uc_trans_table)


if __name__ == "__main__":
    unittest.main()
