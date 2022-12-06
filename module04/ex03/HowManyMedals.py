"""How many medals"""
import numpy as np
import pandas as pd


def how_many_medals(df: pd.DataFrame, name: str) -> dict:
    """
    The function returns a dictionary of dictionaries giving the number and
    type of medals for each year during which the participant won medals.
    The keys of the main dictionary are the Olympic games years.
    In each year's dictionary, the keys are 'G', 'S', 'B' corresponding to the
    type of medals won (gold, silver, bronze).
    The innermost values correspond to the number of medals of a given type won
    for a given year.
    """
    # Filter the data on the name
    df = df[df['Name'] == name]
    # Create a proper dataframe grouped by the necessary infos
    # GroupBy allow me to group data and count number of medal per year and
    # per medal, pd.Categorical on the Year force to display all years even if
    # there is no medal, and the unstack give the table the correct shape for
    # dict transform
    df = df.groupby(["Medal", pd.Categorical(df.Year)])['Medal'].count().unstack()
    # Adding and ordering indexes for medals
    df = df.reindex(['Gold', 'Silver', 'Bronze'], fill_value=0)
    # Renaming indexes
    df = df.rename(index={'Bronze': 'B', 'Gold': 'G', 'Silver': 'S'})
    return df.to_dict()


if __name__ == '__main__':

    # Import file loader
    from FileLoader import FileLoader

    loader = FileLoader()
    data = loader.load("../athlete_events.csv")

    if data is None:
        print('Error with the file')
    else:
        
        print(how_many_medals(data, 'Gary Abraham'))
        #  the output is:
        # "{1976: {'G': 0, 'S': 0, 'B': 0}, 1980: {'G': 0, 'S': 0, 'B': 1}}"

        print(how_many_medals(data, 'Yekaterina Konstantinovna Abramova'))
        #  the output is
        # "{2006: {'G': 0, 'S': 0, 'B': 1}, 2010: {'G': 0, 'S': 0, 'B': 0}}"

        print(how_many_medals(data, 'Kristin Otto'))
        #  the output is:
        # "{1988: {'G': 6, 'S': 0, 'B': 0}}"
        
        print(how_many_medals(data, 'Kjetil Andr Aamodt'))
