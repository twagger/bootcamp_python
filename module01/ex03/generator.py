"""Generator module"""
from random import randrange


def generator(text, sep=" ", option=None):
    '''Splits the text according to sep value and yield the substrings.
       option precise if a action is performed to the substrings before \
       it is yielded.
    '''
    if not isinstance(text, str):
        yield "ERROR"
    elif option is None:
        for word in text.split(sep):
            yield word
    elif option == "shuffle":
        unshuffled = text.split(sep)
        shuffled = []
        for word in unshuffled:
            shuffled.insert(randrange(len(unshuffled)), word)
        for word in shuffled:
            yield word
    elif option == "ordered":
        # Sort by alphabetical order and not ASCII order (default)
        ordered = text.split(sep)
        ordered = sorted(ordered, key=str.lower, reverse=False)
        for word in ordered:
            yield word
    elif option == "unique":
        # Careful not to change the order
        non_unique = text.split(sep)
        unique = sorted(set(non_unique), key=non_unique.index)
        for word in unique:
            yield word
