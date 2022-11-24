"""Color Filter"""
import numpy as np


class ColorFilter():
    """Color filter"""

    def invert(self, array):
        """
        Inverts the color of the image received as a numpy array.
        Args:
        -----
        array: numpy.ndarray corresponding to the image.
        Return:
        -------
        array: numpy.ndarray corresponding to the transformed image.
        None: otherwise.
        Raises:
        -------
        This function should not raise any Exception.
        """
        try:
            inverted = array.copy()
            for i in range(3):
                inverted[:, :, i] = array[:, :, i] * -1
            return inverted
        except (TypeError, IndexError, ValueError):
            return None

    def to_blue(self, array):
        """
        Applies a blue filter to the image received as a numpy array.
        Args:
        -----
        array: numpy.ndarray corresponding to the image.
        Return:
        -------
        array: numpy.ndarray corresponding to the transformed image.
        None: otherwise.
        Raises:
        -------
        This function should not raise any Exception.
        """
        try:
            zeros = np.zeros(array.shape).astype(int)
            blued = np.dstack((zeros[:, :, :1], array[:, :, 2:]))
            return blued
        except (TypeError, IndexError, ValueError):
            return None

    def to_green(self, array):
        """
        Applies a green filter to the image received as a numpy array.
        Args:
        -----
        array: numpy.ndarray corresponding to the image.
        Return:
        -------
        array: numpy.ndarray corresponding to the transformed image.
        None: otherwise.
        Raises:
        -------
        This function should not raise any Exception.
        """
        try:
            greened = array.copy()
            for i in (0,2):
                greened[:, :, i] = 0
            return greened
        except (TypeError, IndexError, ValueError):
            return None

    def to_red(self, array):
        """
        Applies a red filter to the image received as a numpy array.
        Args:
        -----
        array: numpy.ndarray corresponding to the image.
        Return:
        -------
        array: numpy.ndarray corresponding to the transformed image.
        None: otherwise.
        Raises:
        -------
        This function should not raise any Exception.
        """
        try:
            reded = array.copy()
            for i in (1,2):
                reded[:, :, i] = 0
            return reded
        except (TypeError, IndexError, ValueError):
            return None

    def to_celluloid(self, array):
        """
        Applies a celluloid filter to the image received as a numpy array.
        Celluloid filter must display at least four thresholds of shades.
        Be careful! You are not asked to apply black contour on the object,
        you only have to work on the shades of your images.
        Remarks:
        celluloid filter is also known as cel-shading or toon-shading.
        Args:
        -----
        array: numpy.ndarray corresponding to the image.
        Return:
        -------
        array: numpy.ndarray corresponding to the transformed image.
        None: otherwise.
        Raises:
        -------
        This function should not raise any Exception.
        """
        return None

    def to_grayscale(self, array, filter, **kwargs):
        """
        Applies a grayscale filter to the image received as a numpy array.
        For filter = 'mean'/'m': performs the mean of RBG channels.
        For filter = 'weight'/'w': performs a weighted mean of RBG channels.
        Args:
        -----
        array: numpy.ndarray corresponding to the image.
        filter: string with accepted values in ['m','mean','w','weight']
        weights: [kwargs] list of 3 floats where the sum equals to 1,
        corresponding to the weights of each RBG channels.
        Return:
        -------
        array: numpy.ndarray corresponding to the transformed image.
        None: otherwise.
        Raises:
        -------
        This function should not raise any Exception.
        """
        return None


if __name__ == '__main__':
    # Import image processor
    import sys
    sys.path.insert(1, '../ex01/')
    from ImageProcessor import ImageProcessor
    
    # Initialize objects
    ip = ImageProcessor()
    cf = ColorFilter()

    # Load original image
    image = ip.load('./elon_canaGAN.png')
    ip.display(image)

    # Test : invert
    invert_image = cf.invert(image)
    ip.display(invert_image)

    # Test : to_blue
    blue_image = cf.to_blue(image)
    ip.display(blue_image)

    # Test : to_green
    green_image = cf.to_green(image)
    ip.display(green_image)

    # Test : to_red
    red_image = cf.to_red(image)
    ip.display(red_image)

    # Test : to_celluloid
    celluloid_image = cf.to_celluloid(image)
    ip.display(celluloid_image)

    # Test : to_grayscale
    grayscale_image = cf.to_grayscale(image, "w", weights = [0.2126, 0.7152, 0.0722])
    ip.display(grayscale_image)