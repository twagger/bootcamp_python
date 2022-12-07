"""MyPlotLib Module"""
import pandas as pd
import numpy as np


class MyPlotLib():
    """MyPlotLib"""

    def histogram(self, data, features):
        """plots one histogram for each numerical feature in the list"""

    def density(self, data, features):
        """plots the density curve of each numerical feature in the list"""

    def pair_plot(self, data, features):
        """
        plots a matrix of subplots (also called scatter plot matrix). On each
        subplot shows a scatter plot of one numerical variable against another
        one. The main diagonal of this matrix shows simple histograms.
        """

    def box_plot(self, data, features):
        """displays a box plot for each numerical variable in the dataset."""


if __name__ == '__main__':

    import sys
    sys.path.insert(1, '../ex00/')
    from FileLoader import FileLoader

    loader = FileLoader()
    data = loader.load("../athlete_events.csv")

    if data is None:
        print('Error with the file')
    else:
        mpl = MyPlotLib()

        # run the method histogram with one, two and three valid features
        mpl.histogram(data, features)
        mpl.histogram(data, features)
        mpl.histogram(data, features)

        # run the method density with one, two and three valid features
        mpl.density(data, features)
        mpl.density(data, features)
        mpl.density(data, features)

        # run the method pair_plot with one, two and three valid features
        mpl.pair_plot(data, features)
        mpl.pair_plot(data, features)
        mpl.pair_plot(data, features)

        # run the method box_plot with one, two and three valid features
        mpl.box_plot(data, features)
        mpl.box_plot(data, features)
        mpl.box_plot(data, features)
