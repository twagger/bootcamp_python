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
            inverted[:, :, (0, 1, 2)] = 1 - array[:, :, (0, 1, 2)]
            return inverted
        except (TypeError, IndexError, ValueError, AttributeError):
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
            zeros = np.zeros(array.shape, dtype=int)
            blue = np.dstack((zeros[:, :, :2], array[:, :, 2:]))
            return blue
        except (TypeError, IndexError, ValueError, AttributeError):
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
            green = array.copy()
            green[:, :, (0, 2)] = 0
            return green
        except (TypeError, IndexError, ValueError, AttributeError):
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
            green = self.to_green(array)
            blue = self.to_blue(array)
            red = array.copy()
            red[:, :, (0, 1, 2)] = (array[:, :, (0, 1, 2)]
                                    - green[:, :, (0, 1, 2)]
                                    - blue[:, :, (0, 1, 2)])
            return red
        except (TypeError, IndexError, ValueError, AttributeError):
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
        try:
            cell = array.copy()

            # create 4 multiplicators to create four thresholds of shades
            # here I create 6 value because 0 and 1 will have no effects
            shades = np.linspace(0, 1, 6)

            # apply the multiplicators on the proper pixels
            for level in shades:
                cell[np.sum(cell, axis=2) / 3 < level *
                     100] = cell[np.sum(cell, axis=2) / 3 < level * 100] * level

            return cell

        except (TypeError, IndexError, ValueError, AttributeError):
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
        try:
            grayed = 1 * array

            # mean
            if filter == "m":
                # mean the 3 colors of each pixel
                meaned = np.sum(array[:, :, :3], axis=2) / 3
                for i in range(3):
                    grayed[:, :, i] = meaned

            # weights
            elif filter == "w":
                # manage weights
                weights = [None if key != 'weights' else value
                           for key, value in kwargs.items()]
                if len(weights) == 0:
                    return None

                # Graying the image with the weighs
                dotted = np.sum(array[:, :, :3] * weights[0], axis=2)
                for i in range(3):
                    grayed[:, :, i] = dotted

            else:
                return None

            return grayed

        except (TypeError, IndexError, ValueError, AttributeError):
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
    image2 = ip.load('./not_musk.png')
    celluloid_image = cf.to_celluloid(image2)
    ip.display(celluloid_image)

    # Test : to_celluloid
    image3 = ip.load('./toon_shader.jpg')
    celluloid_image = cf.to_celluloid(image3)
    ip.display(celluloid_image)

    # Test : to_celluloid
    celluloid_image = cf.to_celluloid(image)
    ip.display(celluloid_image)

    # Test : to_grayscale weighted
    grayscale_image_w = cf.to_grayscale(image, "w",
                                        weights=[0.2126, 0.7152, 0.0722])
    ip.display(grayscale_image_w)

    # Test : to_grayscale mean
    grayscale_image_m = cf.to_grayscale(image, "m")
    ip.display(grayscale_image_m)
