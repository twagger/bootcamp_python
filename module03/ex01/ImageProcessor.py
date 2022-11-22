"""Image processor"""

import numpy as np
from PIL import Image, ImageShow


class ImageProcessor:
    """ImageProcessor"""

    def __init__(self):
        """Constructor"""
        pass

    def load(self, path: str, *args, **kwargs) -> np.ndarray:
        """opens the PNG file specified by the path argument and returns an
        array with the RGB values of the pixels image"""
        # Error management
        if args or kwargs:
            print("Error: load > wrong number of arguments")
            return None
        if not isinstance(path, str):
            print("Error: load > a string is expected")
            return None
        # Image loading
        try:
           image = Image.open(path)
        except FileNotFoundError as exc:
            print(f"Error: {exc}")
        # Image information
        print(f"Loading image of dimensions {image.size[0]} x {image.size[1]}")
        return np.array(image)

    def display(self, array: np.ndarray, *args, **kwargs):
        """takes a numpy array as an argument and displays the corresponding
        RGB image."""
        # Error management
        if args or kwargs:
            print("Error: load > wrong number of arguments")
            return None
        if not isinstance(array, np.ndarray):
            print("Error: the input is not correct.")
        if len(array) > 0 and isinstance(array[0], list):
            print("Error: incorrect array")
        image = Image.fromarray(array)
        image.show()
