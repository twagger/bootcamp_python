"""This module analyzes a given text."""
import sys
import string


def text_analyzer(text=''):
    """
    This function counts the number of upper characters, lower characters,
    punctuation and spaces in a given text.
    """
    if not isinstance(text, (str)):
        print("AssertionError : argument is not a string")
    else:
        while len(text) == 0:
            text = input("What is the text to analyze?\n")
        print(f'The text contains {len(text)} character(s):\n'
              f'- {sum(1 for l in text if l.isupper())} upper letter(s)\n'
              f'- {sum(1 for l in text if l.islower())} lower letter(s)\n'
              f'- {sum(1 for l in text if l in string.punctuation)}'
              f' punctiation mark(s)\n'
              f'- {sum(1 for l in text if l.isspace())} space(s)'
              )


if __name__ == "__main__":
    if len(sys.argv) > 2:
        print("Error: Only one argument is expected.")
    elif len(sys.argv) == 2:
        text_analyzer(sys.argv[1])
