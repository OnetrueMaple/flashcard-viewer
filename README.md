## Flashcard Viewer
A set of programs to build and view flashcards for studying things.
Currently the program only loads hardcoded files inside the './data/' directory.

## Features
    * Contains 'flashcard-maker.py', a terminal-based program for creating flashcard content. All data is stored onto one file per runtime.
    * Contains 'flashcard-viewer.py' a program to load the flashcards stored inside of ./data/ and displays them for studying.

## Technologies
    * Python for portability
    * DearPyGUI for GUI

## Usage
To use, download all the python files, then run 'flashcard-maker.py' to display all cards I have included inside of ./data/.

## Preview
```
user@User:~$ python3 flashcard-maker.py
Flashcard generator. Enter 'quit' at any point to quit.
Start from which index?
0
Enter front of card content:
Front of Card
Enter back of card content:
Back of Card
Enter front of card content:
quit
Enter back of card content:
quit
Program ended correctly.
user@User:~$ python3 flashcard-viewer.py

```