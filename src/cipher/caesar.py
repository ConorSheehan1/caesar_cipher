from typing import Tuple


def trans_tables(increment: int) -> Tuple[str]:
    """
    :return: two tables, one for lowercase letters, one for upper.
    """
    frm = "abcdefghijklmnopqrstuvwxyz"
    # use circular list, then join into string, so that only a-zA-Z chars are shifted.
    to = "".join([frm[(i + increment) % len(frm)] for i in range(len(frm))])

    return str.maketrans(frm, to), str.maketrans(frm.upper(), to.upper())


def encrypt(text: str, increment: int) -> str:
    """
    Shifts a-z and A-Z by increment in a circular list
    :return: shifted cipher text, ignoring non-alphabetical characters
    """

    # TODO: enforce types at runtime?
    if type(text) != str or type(increment) != int:
        return (
            "text must be a string (letters and symbols in quotes) e.g. 'Hi'\n"
            "increment must be an integer (whole number) e.g. 1"
        )

    trans_table, trans_table_upper = trans_tables(increment)

    translated_text = ""
    for char in text:
        if char.islower():
            translated_text += char.translate(trans_table)
        elif char.isupper():
            translated_text += char.translate(trans_table_upper)
        else:
            translated_text += char

    return translated_text
