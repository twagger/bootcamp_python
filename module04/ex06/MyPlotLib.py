"""MyPlotLib Module"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


class MyPlotLib():
    """MyPlotLib"""

    def histogram(self, data: pd.DataFrame, features: list):
        """plots one histogram for each numerical feature in the list"""
        if (not isinstance(data, pd.DataFrame)
            or not isinstance(features, list)):
            print('Error with parameters')
            return
        for feature in features:
            try:
                data[feature].plot.hist(title=feature)
                plt.show()
            except TypeError:
                print(f'Error : no numeric data for {feature}')


    def density(self, data: pd.DataFrame, features: list):
        """plots the density curve of each numerical feature in the list"""
        if (not isinstance(data, pd.DataFrame)
            or not isinstance(features, list)):
            print('Error with parameters')
            return
        for feature in features:
            try:
                data[feature].plot.density(legend=True)
            except TypeError:
                print(f'Error : no numeric data for {feature}')
        plt.show()

    def pair_plot(self, data: pd.DataFrame, features: list):
        """
        plots a matrix of subplots (also called scatter plot matrix). On each
        subplot shows a scatter plot of one numerical variable against another
        one. The main diagonal of this matrix shows simple histograms.
        """
        if (not isinstance(data, pd.DataFrame)
            or not isinstance(features, list)):
            print('Error with parameters')
            return
        try:
            pd.plotting.scatter_matrix(data[features])
        except (TypeError, ValueError):
            print(f'Error : no numeric data for {features}')
        plt.show()

    def box_plot(self, data: pd.DataFrame, features: list):
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
        mpl.histogram(data, ['Year'])
        mpl.histogram(data, ['Year', 'Sex'])
        mpl.histogram(data, ['Age', 'Height', 'Weight'])

        # run the method density with one, two and three valid features
        mpl.density(data, ['Year'])
        mpl.density(data, ['Weight', 'Height'])
        mpl.density(data, ['Age', 'Weight', 'Height'])

        # # run the method pair_plot with one, two and three valid features
        mpl.pair_plot(data, ['Year'])
        mpl.pair_plot(data, ['Weight', 'Height'])
        mpl.pair_plot(data, ['Age', 'Weight', 'Height'])

        # # run the method box_plot with one, two and three valid features
        # mpl.box_plot(data, features)
        # mpl.box_plot(data, features)
        # mpl.box_plot(data, features)
