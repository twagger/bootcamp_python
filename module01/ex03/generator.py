from random import randrange


def generator(text, sep=" ", option=None):
    '''Splits the text according to sep value and yield the substrings.
       option precise if a action is performed to the substrings before \
       it is yielded.
    '''
    if type(text) is not str:
        yield ("ERROR")
    elif option is None:
        for word in text.split(sep):
            yield word
    elif option is "shuffle":
        unshuffled = text.split(sep)
        shuffled = []
        for word in unshuffled:
            shuffled.insert(randrange(len(unshuffled)), word)
        for word in shuffled:
            yield word
    elif option is "ordered":
        ordered = text.split(sep)
        ordered.sort()
        for word in ordered:
            yield word
    elif option is "unique":
        for word in set(text.split(sep)):
            yield word
