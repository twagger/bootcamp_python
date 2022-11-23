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
                                  position[1]:(position[1] + dim[1])
                                  ])
        except (TypeError, IndexError, ValueError):
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
        try:
            return np.delete(array,
                             list(range(n - 1, array.shape[1 - axis], n)),
                             1 - axis)
        except (TypeError, IndexError, ValueError):
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
        try:
            if axis == 0:
                return np.tile(array, (n, 1))
            if axis == 1:
                return np.tile(array, (1, n))
        except (TypeError, IndexError, ValueError):
            return None

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
        try:
            if len(dim) != 2:
                return None
            first_step = self.juxtapose(array, dim[0], 0)
            return self.juxtapose(first_step, dim[1], 1)
        except (TypeError, IndexError, ValueError):
            return None


# Tests
if __name__ == '__main__':
    sb = ScrapBooker()

    # Crop tests
    print("\033[1;35m--Test 1: Simple crop--\033[0m")
    arr = np.arange(0, 25).reshape(5, 5)
    print(f'Before :\n{arr}\n')
    print(f'After :\n{sb.crop(arr, (3, 1))}')

    print("\n\033[1;35m--Test 2: Crop over dim--\033[0m")
    arr = np.arange(0, 25).reshape(5, 5)
    print(f'Before :\n{arr}\n')
    print(f'After :\n{sb.crop(arr, (42, 42))}')

    print("\n\033[1;35m--Test 3: Crop new position--\033[0m")
    arr = np.arange(0, 25).reshape(5, 5)
    print(f'Before :\n{arr}\n')
    print(f'After :\n{sb.crop(arr, (3, 1), position=(1, 0))}')

    print("\n\033[1;35m--Test 4: Crop over dim with new position--\033[0m")
    arr = np.arange(0, 25).reshape(5, 5)
    print(f'Before :\n{arr}\n')
    print(f'After :\n{sb.crop(arr, (42, 42), position=(1, 0))}')

    print("\n\033[1;35m--Test 4: Crop over dim with out position--\033[0m")
    arr = np.arange(0, 25).reshape(5, 5)
    print(f'Before :\n{arr}\n')
    print(f'After :\n{sb.crop(arr, (42, 42), position=(42, 42))}')

    print("\n\033[1;35m--Test 4: Crop wrong type--\033[0m")
    arr = np.arange(0, 25).reshape(5, 5)
    print(f'Before :\n{arr}\n')
    print(f'After :\n{sb.crop(arr, 42.42, position=(42, 42))}')

    # Thin tests
    print("\n\033[1;35m--Test 5: Thin--\033[0m")
    arr2 = np.array("A B C D E F G H I".split() * 6).reshape(-1,9)
    print(sb.thin(arr2, 3, 0))

    print("\n\033[1;35m--Test 6: Thin--\033[0m")
    arr3 = np.array([[var] * 10 for var in "ABCDEFG"])
    print(sb.thin(arr3, 3, 1))

    # Juxtapose tests
    print("\n\033[1;35m--Test 7: Juxtapose vertical--\033[0m")
    arr4 = np.array([[1, 2, 3],[4, 5, 6],[7, 8, 9]])
    print(sb.juxtapose(arr4, 2, 0))

    print("\n\033[1;35m--Test 7: Juxtapose horizontal--\033[0m")
    arr4 = np.array([[1, 2, 3],[4, 5, 6],[7, 8, 9]])
    print(sb.juxtapose(arr4, 2, 1))

     # Mosaic tests
    print("\n\033[1;35m--Test 8: Mosaic--\033[0m")
    arr4 = np.array([[1, 2, 3],[4, 5, 6],[7, 8, 9]])
    print(sb.mosaic(arr4, (2,3)))

    # Error management
    print("\n\033[1;35m--Test: Error management--\033[0m")
    not_numpy_arr = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
    print(sb.crop(not_numpy_arr, (1,2)))
    print(sb.juxtapose(arr4, -2, 0))
    print(sb.mosaic(arr4, (1, 2, 3)))
