# Requirements
1. Python 3

If you're on linux or osx, you probably already have python 3!  
If you're on windows you'll need to install python 3.  
You can get it here: [https://www.python.org/downloads/](https://www.python.org/downloads/)

# Usage
You can open the program by either:

1. Opening a command prompt and typing "python caesar_cipher.py"
2. Opening the file in an IDE and running it.

The program ignores everything other than characters in the Latin alphabet.

It is possible to shift the text either direction in the alphabet because the program uses a circular list. For example shifting text back 1 letter (1) is equivalent to moving the text forward 25 letters (-25). This also makes it easier to reverse ciphers. If you already know how many letters a piece of text is shifted forward, put a minus in front of that number to unscramble the text. 