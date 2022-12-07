"""Spatio temporal data"""
import pandas as pd


class SpatioTemporalData():
    """SpatioTemporalData"""

    def __init__(self, df: pd.DataFrame):
        """Constructor"""
        self.df = df

    def when(self, location: str) -> str:
        """
        takes a location as an argument and returns a list containing the
        years where games were held in the given location,
        """
        if isinstance(location, str):
            return list(self.df[self.df['City'] == location].Year.unique())

    def where(self, date: int) -> list:
        """
        takes a date as an argument and returns the location where the
        Olympics took place in the given year
        """
        if isinstance(date, int):
            return list(self.df[self.df['Year'] == date].City.unique())


if __name__ == '__main__':

    # Import file loader
    from FileLoader import FileLoader

    loader = FileLoader()
    data = loader.load("../athlete_events.csv")

    if data is None:
        print('Error with the file')
    else:

        sp = SpatioTemporalData(data)

        print(sp.where(2000))
        # output is: ['Sydney']

        print(sp.where(1980))
        # output is: ['Lake Placid', 'Moskva'] If a single of these locations
        # is returned it's ok.

        print(sp.when('London'))
        # output is: [2012, 1948, 1908]
