class Vector:

    def __init__(self, values):
        if type(values) is not list:
            raise TypeError
        else:
            self.values = values
            if len(values) == 1:
                self.shape = (1, len(values[0]))
            else:
                self.shape = (len(values), 1)
