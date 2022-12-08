"""Komparator module"""
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


class Komparator():
    """Komparator"""

    def __init__(self, df: pd.DataFrame):
        """Constructor"""
        self.df = df

    def compare_box_plots(self, categorical_var: str, numerical_var: str):
        """
        displays a series of box plots to compare how the distribution of the
        numerical variable changes if we only consider the subpopulation which
        belongs to each category.
        There should be as many box plots as categories. For example, with Sex
        and Height, we would compare the height distributions of men vs. women
        with two box plots.
        """
        # type control
        if (not isinstance(categorical_var, str)
                or not isinstance(numerical_var, str)):
            print('Error with parameters')
            return
        # preparing the data
        df_cleaned = self.df[[categorical_var, numerical_var]]
        df_cleaned = df_cleaned.dropna()
        # display (uses SeaBorn)
        sns.boxplot(x=categorical_var, y=numerical_var, data=df_cleaned)
        plt.show()

    def density(self, categorical_var: str, numerical_var: str):
        """
        displays the density of the numerical variable. Each subpopulation
        should be represented by a separate curve on the graph.
        """
        # type control
        if (not isinstance(categorical_var, str)
                or not isinstance(numerical_var, str)):
            print('Error with parameters')
            return
        # preparing the data
        df_cleaned = self.df[[categorical_var, numerical_var]]
        df_cleaned = df_cleaned.dropna()
        # display (uses SciPy)
        values = list(df_cleaned[categorical_var].unique())
        # display plots as subplots
        graph = sns.displot(data=df_cleaned, kind='kde', col=categorical_var,
                            x=numerical_var, col_order=values)
        # Hide the intermediate graph
        plt.close()
        # display subplots on the same graph
        _, ax = plt.subplots()
        sns.kdeplot(data=df_cleaned, x=numerical_var, hue=categorical_var,
                    ax=ax)
        plt.show()

    def compare_histograms(self, categorical_var: str, numerical_var: str):
        """
        plots the numerical variable in a separate histogram for each category.
        As an extra, you can use overlapping histograms with a color code.
        """
        # type control
        if (not isinstance(categorical_var, str)
                or not isinstance(numerical_var, str)):
            print('Error with parameters')
            return
        # preparing the data
        df_cleaned = self.df[[categorical_var, numerical_var]]
        df_cleaned = df_cleaned.dropna()
        # display (uses MatPlotLib)
        values = df_cleaned[categorical_var].unique()
        _, ax = plt.subplots(nrows=1, ncols=len(values))
        for idx, value in enumerate(values):
            df_cleaned[df_cleaned[categorical_var]
                       == value].plot.hist(title=value, ax=ax[idx],
                                           legend=False)
        plt.xlabel(numerical_var)
        plt.show()


if __name__ == '__main__':

    import sys
    sys.path.insert(1, '../ex00/')
    from FileLoader import FileLoader

    loader = FileLoader()
    data = loader.load("../athlete_events.csv")

    if data is None:
        print('Error with the file')
    else:

        kmp = Komparator(data)

        # giving 'Medal' and 'Age' for the method compare_box_plots, you
        # should observe 3 boxes: Bronze. Silver and Gold
        kmp.compare_box_plots('Medal', 'Age')

        # giving 'Medal' and 'Height' for the method compare_histograms, you
        # should observe 3 histograms
        kmp.compare_histograms('Medal', 'Height')

        # giving 'Medal' and 'Weight' for the method density, you should
        # observe 3 curves of density plot
        kmp.density('Medal', 'Weight')
