"""NumPy Creator"""

import numpy as np


class NumPyCreator():
    """NumPyCreator class"""

    def __init__(self):
        """Constructor"""
        pass

    def from_list(self, lst: list, dtype=None, *args, **kwargs) -> np.ndarray:
        """Create a numpy array from a list"""
        if args or kwargs:
            print("Error: wrong number of arguments")
            return None
        if not isinstance(lst, list):
            return None
        result = np.array(lst, dtype)
        if len(result.shape) == 1:
            return None
        return result

    def from_tuple(self, tpl: tuple, dtype=None, *args,
                   **kwargs) -> np.ndarray:
        """Create a numpy array from a tuple"""
        if args or kwargs:
            print("Error: wrong number of arguments")
            return None
        if not isinstance(tpl, tuple):
            return None
        return np.array(tpl, dtype)

    def from_iterable(self, itr, dtype=None, *args, **kwargs) -> np.ndarray:
        """Create a numpy array from an iterable"""
        if args or kwargs:
            print("Error: wrong number of arguments")
            return None
        try:
            iter(itr)
        except TypeError:
            return None
        return np.array(itr, dtype)

    def from_shape(self, shape: tuple, value: any = 0,
                   dtype=None, *args, **kwargs) -> np.ndarray:
        """Create a numpy array from shape filled with the value"""
        if args or kwargs:
            print("Error: wrong number of arguments")
            return None
        if not isinstance(shape, tuple):
            return None
        try:
            return np.full(shape, value, dtype)
        except TypeError as exc:
            return exc

    def random(self, shape: tuple, *args, **kwargs) -> np.ndarray:
        """Create a numpy array from shape fille with random values"""
        if args or kwargs:
            print("Error: wrong number of arguments")
            return None
        if not isinstance(shape, tuple):
            return None
        try:
            return np.random.rand(*shape)
        except TypeError as exc:
            return exc

    def identity(self, n: int, *args, **kwargs) -> np.ndarray:
        """Create a numpy array representing the identity matrix of size n"""
        if args or kwargs:
            print("Error: wrong number of arguments")
            return None
        if not isinstance(n, int):
            return None
        return np.identity(n)
