"""This module filters words in a sentence"""
import sys
import string


def clear_punctuation(word):
    """clear the punctuation from a string"""
    return ''.join([letter for letter in word if letter
                    not in string.punctuation])


def integer_check(integer):
    """Check if the string in param is an integer"""
    if integer.isdigit() is True or ((integer[0] == '-' or integer[0] == '+')
                                     and integer[1:].isdigit() is True):
        return True
    return False


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Error: wrong number of arguments")
    elif integer_check(sys.argv[2]) is False:
        print("Error: Second parameter is not a proper integer")
    else:
        words = sys.argv[1].split(' ')
        words_no_punct = [clear_punctuation(word) for word in words]
        result = [word for word in words_no_punct if len(
            word) > int(sys.argv[2])]
        print(result)
