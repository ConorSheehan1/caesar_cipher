from tkinter import *


class App(object):
    def __init__(self):
        self.root = Tk()
        self.root.wm_title("Ceasar Cipher")

        self.label = Label(self.root, text="Enter a string to convert.")
        self.label.pack()

        self.entrytext = StringVar()
        Entry(self.root, textvariable=self.entrytext, width="400").pack()

        self.label2 = Label(self.root, text="Enter number of letters to shift in the alphabet.")
        self.label2.pack()

        self.entrynumber = StringVar()
        Entry(self.root, textvariable=self.entrynumber, width="400").pack()

        self.buttontext = StringVar()
        self.buttontext.set("Calculate")
        Button(self.root, textvariable=self.buttontext, command=self.clicked).pack()

        self.error = Label(self.root, text="")
        self.error.pack()

        self.result = Text(self.root, height=10, width="400")
        self.result.configure(state="disabled")
        self.result.pack()

        self.root.mainloop()

    def clicked(self):
        # allow text to be inserted
        self.result.configure(state="normal")
        # flush old text
        self.result.delete(1.0, END)

        # handle uppercase letters, ignore any non-alphabetical characters
        user_string = self.entrytext.get()
        try:
            user_increment = int(self.entrynumber.get())
        except ValueError:
            error_message = "please insert a number in the second text box"
            print(error_message)
            self.error.configure(text=error_message)
            # break out of function to ensure no value error converting empty string to int
            return False

        def encrypt(string, increment):
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

        result = str(encrypt(user_string, user_increment))
        if result == "":
            # result is now an error message
            error_message = "please insert a string in the first text box"
            print(error_message)
            self.error.configure(text=error_message)

        # return values in disabled text field to allow users to copy text to clipboard
        self.result.insert(1.0, result)
        self.result.configure(state="disabled")
        return True
App()
