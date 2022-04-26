import sys
import string
import textwrap


def text_analyzer(text=''):
    """
    This function counts the number of upper characters, lower characters,
    punctuation and spaces in a given text.
    """
    if type(text) != str:
        print("AssertionError : argument is not a string")
    else:
        while len(text) == 0:
            text = raw_input("What is the text to analyze?\n")
        print(textwrap.dedent("""\
        The text contains {} character(s):
        - {} upper letter(s)
        - {} lower letter(s)
        - {} punctiation mark(s)
        - {} space(s)\
        """.format(
            len(text),
            sum(1 for letter in text if letter.isupper()),
            sum(1 for letter in text if letter.islower()),
            sum(1 for letter in text if letter in string.punctuation),
            sum(1 for letter in text if letter.isspace()),
        )))


if len(sys.argv) > 2:
    print("Usage: python count.py [Argument]")
else:
    text_analyzer(sys.argv[1])
