from tkinter import *
from cipher.caesar import encrypt


class App(object):
    def __init__(self):
        self.root = Tk()

        self.root.geometry("500x200")
        self.root.wm_title("Ceasar Cipher")

        Label(self.root, text="Enter a string to be encrypted").pack()
        self.entry_text = StringVar()
        Entry(self.root, textvariable=self.entry_text, width="400").pack()

        Label(self.root, text="Enter a number to shift the letters").pack()
        self.entry_number = StringVar()
        Entry(self.root, textvariable=self.entry_number, width="400").pack()

        self.button_text = StringVar()
        self.button_text.set("Calculate")
        Button(self.root, textvariable=self.button_text, command=self.on_click).pack()

        self.error_label = Label(self.root, text="", foreground="red")
        self.error_label.pack()

        self.result = Text(self.root, height=10, width="400")
        self.result.configure(state="disabled")
        self.result.pack()

        self.root.mainloop()

    def append_error(self, error_text):
        self.error_label.configure(
            text=f"{self.error_label.cget('text')} {error_text}\n"
        )

    def on_click(self):
        # allow text to be inserted
        self.result.configure(state="normal")
        # flush old result and errors
        self.result.delete(1.0, END)
        self.error_label.configure(text="")

        user_string = self.entry_text.get()
        try:
            user_increment = int(self.entry_number.get())
        except ValueError:
            self.append_error("please insert a number in the second input")
            user_increment = 0

        result = encrypt(user_string, user_increment)
        if result == "":
            self.append_error("please insert a string in the first input")

        # disable text field so text can be copied, but not modified
        self.result.insert(1.0, result)
        self.result.configure(state="disabled")
        return True


if __name__ == "__main__":
    App()
