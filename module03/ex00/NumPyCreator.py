"""NumPy Creator"""

import warnings
import numpy as np

# Filter deprecation warnings of numpy on non matrix shape arrays
warnings.filterwarnings("ignore", category=np.VisibleDeprecationWarning)


class NumPyCreator():
    """NumPyCreator class"""

    def from_list(self, lst: list, *args, dtype=None, **kwargs) -> np.ndarray:
        """Create a numpy array from a list"""
        if args or kwargs:
            print("Error: wrong number of arguments")
            return None
        if not isinstance(lst, list):
            return None
        result = np.array(lst, dtype)
        if result.dtype is np.dtype('object'):
            return None
        return result

    def from_tuple(self, tpl: tuple, *args, dtype=None,
                   **kwargs) -> np.ndarray:
        """Create a numpy array from a tuple"""
        if args or kwargs:
            print("Error: wrong number of arguments")
            return None
        if not isinstance(tpl, tuple):
            return None
        result = np.array(tpl, dtype)
        if result.dtype is np.dtype('object'):
            return None
        return result

    def from_iterable(self, itr, *args, dtype=None, **kwargs) -> np.ndarray:
        """Create a numpy array from an iterable"""
        if args or kwargs:
            print("Error: wrong number of arguments")
            return None
        try:
            iter(itr)
        except TypeError:
            return None
        result = np.array(itr, dtype)
        if result.dtype is np.dtype('object'):
            return None
        return result

    def from_shape(self, shape: tuple, *args, value = 0,
                   dtype=float, **kwargs) -> np.ndarray:
        """Create a numpy array from shape filled with the value"""
        if args or kwargs:
            print("Error: wrong number of arguments")
            return None
        if not isinstance(shape, tuple):
            return None
        try:
            return np.full(shape, value, dtype)
        except (TypeError, ValueError):
            return None

    def random(self, shape: tuple, *args, **kwargs) -> np.ndarray:
        """Create a numpy array from shape fille with random values"""
        if args or kwargs:
            print("Error: wrong number of arguments")
            return None
        if not isinstance(shape, tuple):
            return None
        try:
            return np.random.rand(*shape)
        except (TypeError, ValueError):
            return None

    def identity(self, n: int, *args, **kwargs) -> np.ndarray:
        """Create a numpy array representing the identity matrix of size n"""
        if args or kwargs:
            print("Error: wrong number of arguments")
            return None
        if not isinstance(n, int):
            return None
        try:
            return np.identity(n)
        except (TypeError, ValueError):
            return None
