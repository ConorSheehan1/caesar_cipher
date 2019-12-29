from tkinter import *
from cipher.caesar import encrypt


class App(object):
    def __init__(self):
        self.root = Tk()

        self.root.geometry("500x200")
        self.root.wm_title("Ceasar Cipher")

        self.label = Label(self.root, text="Enter a string")
        self.label.pack()

        self.entrytext = StringVar()
        Entry(self.root, textvariable=self.entrytext, width="400").pack()

        self.label2 = Label(
            self.root, text="Enter number of letters to shift in the alphabet"
        )
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

        user_string = self.entrytext.get()
        try:
            user_increment = int(self.entrynumber.get())
        except ValueError:
            error_message = "please insert a number in the second text box"
            print(error_message)
            self.error.configure(text=error_message)
            # break out of function to ensure no value error converting empty string to int
            return False

        result = encrypt(user_string, user_increment)
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
