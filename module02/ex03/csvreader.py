"""CSVReader module
This module is about context manager and the with statement.
A nice tutorial is available here :
https://realpython.com/python-with-statement/#managing-resources-in-python
"""


class CsvFileOpenException(BaseException):
    pass


class CsvFileCorruptedException(BaseException):
    pass


class CsvReader():
    """This class host a csv file and add functions to read it"""

    def __init__(self, filename=None, sep=',', header=False, skip_top=0,
                 skip_bottom=0):
        """Constructor"""
        self.filename = filename
        self.sep = sep
        self.header = header
        self.skip_top = skip_top
        self.skip_bottom = skip_bottom
        self.file = None

    def __enter__(self):
        """Setup function"""
        # Open the file
        self.file = open(self.filename, 'r')
        if self.file is None:
            raise CsvFileOpenException("Cannot open file")
        # Check if the file is corrupted
        lines = self.file.readlines()
        previous = None
        for line in lines:
            res = line.split(self.sep)
            current = len(res)
            if any(tst for tst in res if tst is None or tst == '\n'):
                return None
            if previous is not None and previous != current:
                return None
            previous = current
        # File is not corrupted, return the current instance
        return self

    def __exit__(self, exc_type, exc_value, exc_tb):
        """Teardown function"""
        if isinstance(exc_value, CsvFileOpenException):
            return True  # Swallow exception
        if isinstance(exc_value, CsvFileCorruptedException):
            self.file.close()
            return True  # Swallow exception
        self.file.close()

    def getdata(self):
        """ Retrieves the data/records from skip_top to skip bottom.
        Return:
        nested list (list(list, list, ...)) representing the data.
        """
        self.file.seek(0)
        lines = self.file.readlines()
        # Build the resulting list
        result = [line.replace('\n', '').split(self.sep) for idx, line
                  in enumerate(lines[1:])
                  if idx >= self.skip_top and idx <= len(lines)
                  - self.skip_bottom - 1]
        # If Header is True
        if self.header is True and lines[0] is not None:
            result.insert(0, lines[0].replace('\n', '').split(self.sep))
        return result

    def getheader(self):
        """ Retrieves the header from csv file.
        Returns:
        list: representing the data (when self.header is True).
        None: (when self.header is False).
        """
        # read the first line
        self.file.seek(0)
        lines = self.file.readlines()
        if lines[0] is not None:
            cleaned = lines[0].replace('\n', '')
            return cleaned.split(self.sep)
