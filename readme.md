# Requirements
1. Python 3
2. tkinter

If you're on linux or osx, you probably already have python 3!  
If you're on windows you'll need to install python 3.  
You can get it here: [https://www.python.org/downloads/](https://www.python.org/downloads/)

Once you have python 3, open up command line and type
"pip install tkinter"

# Usage
You can open the program from the command line by typeing "python caesar_cipher_generator.py" or by opening the file in an IDE and running it.

The program should open up a window in which you can paste text and choose how many letters in the alphabet to shift the text by. The output will appear at the bottom of the window. 

It is possible to shift the text either direction in the alphabet because the program uses a circular list. For example you could shift text back one letter, but it would achieve the same affect as moving the text forward 25 letters. I allowed negative numbers my own ease of use reversing ciphers. Rather than having to do some basic math, if you already know how many letters the text is shifted forward, put a minus in front of that number to unscramble the text. 