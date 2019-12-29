from typing import Tuple


def trans_tables(increment: int) -> Tuple[str]:
    to = ""
    frm = "abcdefghijklmnopqrstuvwxyz"
    # create string of alphabet starting at some offset to create transtable
    for i in range(len(frm)):
        # start at index increment, mod by len to wrap back to start of list
        to += frm[(i + increment) % len(frm)]

    # create two tables, one for uppercase letters, one for lower
    # one table would cause problems with lowercase converting to upper and vice versa at intersection
    return str.maketrans(frm, to), str.maketrans(frm.upper(), to.upper())


def encrypt(text: str, increment: int) -> str:
    """
    handle uppercase letters, ignore any non-alphabetical characters
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
