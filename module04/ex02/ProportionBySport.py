"""Youngest Fellah"""
import pandas as pd


def proportion_by_sport(df: pd.DataFrame,
                        year: int, sport: str, gender: str) -> float:
    """
    The function returns a dictionary containing the age of the youngest woman
    and man who took part in the Olympics on that year.
    """
    df_year = df[df['Year'] == year]
    min_man = df_year[df_year['Sex'] == 'M']['Age'].min()
    min_woman = df_year[df_year['Sex'] == 'F']['Age'].min()
    return { 'f': min_woman, 'm': min_man}

if __name__ == '__main__':
    
    # Import file loader
    from FileLoader import FileLoader

    loader = FileLoader()
    data = loader.load("../athlete_events.csv")

    print("")

    print(proportion_by_sport(data, 2004, 'Tennis', 'F'), end = "\n\n")
    # output is "0.02307"

    print(proportion_by_sport(data, 2008, 'Hockey', 'F'), end = "\n\n")
    # output is  "0.03284"

    print(proportion_by_sport(data, 1964, 'Biathlon', 'M'), end = "\n\n")
    # output is "0.00659"
