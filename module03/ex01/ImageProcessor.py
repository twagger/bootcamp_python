"""Image processor"""
import numpy as np
from PIL import Image
from matplotlib import pyplot as plt


class ImageProcessor:
    """ImageProcessor"""

    def load(self, path: str, *args, **kwargs) -> np.ndarray:
        """opens the PNG file specified by the path argument and returns an
        array with the RGB values of the pixels image"""
        # Error management
        if args or kwargs:
            print("Error: load > wrong number of arguments")
            return None
        if path is None or not isinstance(path, str):
            print("Error: load > a string is expected")
            return None
        # Image loading
        try:
            image_arr = np.array(Image.open(path))
        except FileNotFoundError as exc:
            print(f"Error: {exc}")
        # Image information
        print(f"Loading image of dimensions "
              f"{image_arr.shape[0]} x {image_arr.shape[1]}")
        return image_arr

    def display(self, array: np.ndarray, *args, **kwargs):
        """takes a numpy array as an argument and displays the corresponding
        RGB image."""
        # Error management
        if args or kwargs:
            print("Error: load > wrong number of arguments")
            return
        if not isinstance(array, np.ndarray):
            print("Error: the input is not correct.")
            return
        if array.dtype is np.dtype('object'):
            print("Error: incorrect array")
            return
        # Show image
        plt.imshow(array)
        plt.show()


# Tests
if __name__ == '__main__':
    ip = ImageProcessor()
    image_array = ip.load('./42AI.png')
    ip.display(image_array)
