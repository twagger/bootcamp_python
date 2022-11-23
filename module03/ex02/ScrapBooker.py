"""Scrapbooker"""
from typing import Tuple
import numpy as np


class ScrapBooker:
    """Scrapbooker"""

    def crop(self,
             array: np.ndarray,
             dim: Tuple[int, int],
             position=(0, 0)
             ) -> np.ndarray:
        """
        Crops the image as a rectangle via dim arguments (being the new height
        and width of the image) from the coordinates given by position
        arguments.
        Args:
        -----
        array: numpy.ndarray
        dim: tuple of 2 integers.
        position: tuple of 2 integers.
        Return:
        -------
        new_arr: the cropped numpy.ndarray.
        None (if combinaison of parameters not compatible).
        Raise:
        ------
        This function should not raise any Exception.
        """
        try:
            return np.array(array[
                                  position[0]:(position[0] + dim[0]),
                                  position[1]:(position[1] + dim[1]),
                                  :])
        except (TypeError, IndexError):
            return None

    def thin(self,
             array: np.ndarray,
             n: int,
             axis: int) -> np.ndarray:
        """
        Deletes every n-th line pixels along the specified axis (0: Horizontal,
         1: Vertical)
        Args:
        -----
        array: numpy.ndarray.
        n: non null positive integer lower than the number of row/column of the
        array (depending of axis value).
        axis: positive non null integer.
        Return:
        -------
        new_arr: thined numpy.ndarray.
        None (if combinaison of parameters not compatible).
        Raise:
        ------
        This function should not raise any Exception.
        """
        #
        # Example of a function with light parameter check
        #
        try:
            return 'toto'
        except (TypeError, IndexError):
            return None

    def juxtapose(self, array, n, axis):
        """
        Juxtaposes n copies of the image along the specified axis.
        Args:
        -----
        array: numpy.ndarray.
        n: positive non null integer.
        axis: integer of value 0 or 1.
        Return:
        -------
        new_arr: juxtaposed numpy.ndarray.
        None (combinaison of parameters not compatible).
        Raises:
        -------
        This function should not raise any Exception.
        """

    def mosaic(self, array, dim):
        """
        Makes a grid with multiple copies of the array. The dim argument
        specifies the number of repetition along each dimensions.
        Args:
        -----
        array: numpy.ndarray.
        dim: tuple of 2 integers.
        Return:
        -------
        new_arr: mosaic numpy.ndarray.
        None (combinaison of parameters not compatible).
        Raises:
        -------
        This function should not raise any Exception.
        """


# Tests
if __name__ == '__main__':
    sb = ScrapBooker()

    # Crop tests
    print("\033[1;35m--Test 1: Simple crop--\033[0m")
    arr = np.arange(0, 450).reshape(10, 15, 3)
    print(f'Before :\n{arr}\n')
    print(f'After :\n{sb.crop(arr, (1, 1))}')

    print("\n\033[1;35m--Test 2: Crop over dim--\033[0m")
    arr = np.arange(0, 450).reshape(10, 15, 3)
    print(f'Before :\n{arr}\n')
    print(f'After :\n{sb.crop(arr, (42, 42))}')

    print("\n\033[1;35m--Test 3: Crop new position--\033[0m")
    arr = np.arange(0, 450).reshape(10, 15, 3)
    print(f'Before :\n{arr}\n')
    print(f'After :\n{sb.crop(arr, (8, 4), position=(1, 6))}')

    print("\n\033[1;35m--Test 4: Crop over dim with new position--\033[0m")
    arr = np.arange(0, 450).reshape(10, 15, 3)
    print(f'Before :\n{arr}\n')
    print(f'After :\n{sb.crop(arr, (42, 42), position=(6, 6))}')

    print("\n\033[1;35m--Test 4: Crop over dim with out position--\033[0m")
    arr = np.arange(0, 450).reshape(10, 15, 3)
    print(f'Before :\n{arr}\n')
    print(f'After :\n{sb.crop(arr, (42, 42), position=(42, 42))}')

    print("\n\033[1;35m--Test 4: Crop wrong type--\033[0m")
    arr = np.arange(0, 450).reshape(10, 15, 3)
    print(f'Before :\n{arr}\n')
    print(f'After :\n{sb.crop(arr, 42, position=(42, 42))}')
