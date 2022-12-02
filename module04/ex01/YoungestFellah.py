"""Youngest Fellah"""
import pandas as pd
import numpy as np


def youngestfellah(df: pd.DataFrame, year: int):
    """
    The function returns a dictionary containing the age of the youngest woman
    and man who took part in the Olympics on that year.
    """
    df_year = df[df['Year'] == year]
    min_man = np.min(df_year[df_year['Sex'] == 'M']['Age'])
    min_woman = np.min(df_year[df_year['Sex'] == 'F']['Age'])
    return { 'f': min_woman, 'm': min_man}

if __name__ == '__main__':
    
    # Import file loader
    import sys
    sys.path.insert(1, '../ex00/')
    from FileLoader import FileLoader

    loader = FileLoader()
    data = loader.load("../athlete_events.csv")

    print(youngestfellah(data, 1992))
    # output is: "{'f': 12.0, 'm': 11.0}"

    print(youngestfellah(data, 2004))
    # output is: "{'f': 13.0, 'm': 14.0}"

    print(youngestfellah(data, 2010))
    # output is: "{'f': 15.0, 'm': 15.0}"

    print(youngestfellah(data, 2003))
    # output is: "{'f': nan, 'm': nan}"
