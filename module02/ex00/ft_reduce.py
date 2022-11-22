"""Reduce module"""


def ft_reduce(function_to_apply, iterable):
    """Apply function of two arguments cumulatively.
    Args:
        function_to_apply:  a function taking an iterable.
        iterable:           an iterable object (list, tuple, iterator).
    Return:
        A value, of same type of elements in the iterable parameter.
        None if the iterable can not be used by the function.
    """
    try:
        if not callable(function_to_apply):
            return None
        #iterable check
        try:
            iter(iterable)
        except TypeError as exc:
            raise TypeError("reduce() arg 2 must support iteration")from exc
        result = iterable[0]
        for item in iterable[1:]:
            result = function_to_apply(result, item)
        return result
    except TypeError as exc:
        raise TypeError(exc) from exc
    except IndexError as exc:
        raise TypeError("reduce() of empty iterable with no initial value") from exc
