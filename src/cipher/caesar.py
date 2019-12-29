def encrypt(string: str, increment: int) -> str:
    if type(string) != str or type(increment) != int:
        return "string must be a string (letters and symbols in quotes)\n"\
                "increment must be an integer (whole number)"
    to = ""
    frm = "abcdefghijklmnopqrstuvwxyz"
    # create string of alphabet starting at some offset to create transtable
    for i in range(len(frm)):
        # start at index increment, mod by len to wrap back to start of list
        to += frm[(i+increment) % len(frm)]

    # create two tables, one for uppercase letters, one for lower
    # one table would cause problems with lowercase converting to upper and vice versa at intersection
    trans_table = str.maketrans(frm, to)
    trans_table_upper = str.maketrans(frm.upper(), to.upper())

    answer = ""
    for char in string:
        if char.islower():
            answer += char.translate(trans_table)
        elif char.isupper():
            answer += char.translate(trans_table_upper)
        else:
            answer += char
    return answer
    