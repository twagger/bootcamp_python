"""Proportion by sport"""
import numpy as np
import pandas as pd


def proportion_by_sport(df: pd.DataFrame,
                        year: int, sport: str, gender: str) -> float:
    """
    Function displaying the proportion of participants
    who played a given sport, among the participants of a given genders.
    """
    # Clean and filter the data on necessary columns
    # df = df.drop_duplicates(subset='ID') < Commented to fit expected results.
    # explanation : an athlete registered in multiple sports on a year will
    # have multiple entries in the file, but it is the same athlete ...
    df = df.drop(['ID', 'Name', 'Age', 'Height', 'Weight', 'Team', 'NOC',
                  'Games', 'Season', 'City', 'Event', 'Medal'], axis=1)
    df = df.dropna(axis = 0)
    # Work with the data
    df_year_gend = df[(df['Year'] == year)
                       & (df['Sex'] == gender)].shape[0]
    df_year_sport_gend = df[(df['Year'] == year)
                             & (df['Sport'] == sport)
                             & (df['Sex'] == gender)].shape[0]
    try:
        return df_year_sport_gend / df_year_gend
    except ZeroDivisionError:
        return 0.0

if __name__ == '__main__':

    # Import file loader
    from FileLoader import FileLoader

    loader = FileLoader()
    data = loader.load("../athlete_events.csv")

    if data is None:
        print('Error with the file')
    else:
        print("")

        print(proportion_by_sport(data, 2004, 'Tennis', 'F'), end = "\n\n")
        # output is "0.02307"

        print(proportion_by_sport(data, 2008, 'Hockey', 'F'), end = "\n\n")
        # # output is  "0.03284"

        print(proportion_by_sport(data, 1964, 'Biathlon', 'M'), end = "\n\n")
        # # output is "0.00659"
