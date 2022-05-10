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
        result = iterable[0]
        for item in iterable[1:]:
            result = function_to_apply(result, item)
        return result
    except TypeError as e:
        return TypeError(e)