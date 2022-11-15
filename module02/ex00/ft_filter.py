"""Filter module"""


def ft_filter(function_to_apply, iterable):
    """Filter the result of function apply to all elements of the iterable.
    Args:
        function_to_apply:  a function taking an iterable.
        iterable:           an iterable object (list, tuple, iterator).
    Return:
        An iterable.
        None if the iterable can not be used by the function.
    """
    try:
        if not callable(function_to_apply):
            yield None
        for item in iterable:
            if function_to_apply(item):
                yield item
    except TypeError as exc:
        raise TypeError(exc) from exc
