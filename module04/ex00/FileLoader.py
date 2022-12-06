"""File loader"""
import pandas as pd


class FileLoader():
    """Fileloader class"""

    def load(self, path: str, *args, **kwargs) -> pd.DataFrame:
        """
        takes as an argument the file path of the dataset to load, displays a
        message specifying the dimensions of the dataset (e.g. 340 x 500) and
        returns the dataset loaded as a pandas.DataFrame.
        """
        # Error management
        if args or kwargs:
            print("Error: load > wrong number of arguments")
            return None
        if path is None or not isinstance(path, str):
            print("Error: load > a string is expected")
            return None

        # File loading
        try:
            dataset = pd.read_csv(path)
        except FileNotFoundError as exc:
            print(f"Error: {exc}")
            return None
        except (pd.errors.ParserError,
                pd.errors.EmptyDataError,
                pd.errors.ParserWarning,
                pd.errors.DtypeWarning) as exc:
            print(f"Error: {exc}")
            return None

        # Image information
        print(f"Loading dataset of dimensions "
              f"{dataset.shape[0]} x {dataset.shape[1]}")
        return dataset

    def display(self, df: pd.DataFrame, n: int, *args, **kwargs):
        """
        takes a pandas.DataFrame and an integer as arguments, displays the
        first n rows of the dataset if n is positive, or the last n rows
        if n is negative.
        """
        # Error management
        if args or kwargs:
            print("Error: load > wrong number of arguments")
            return None
        if df is None or not isinstance(df, pd.DataFrame):
            print("Error: load > a panda dataframe is expected")
            return None
        if n is None or not isinstance(n, int):
            print("Error: load > an int is expected")
            return None

        if n >= 0:
            print(df.head(n))
        else:
            print(df.tail(-n))
