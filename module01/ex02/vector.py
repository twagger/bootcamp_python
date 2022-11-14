"""Vector module"""


class Vector:
    """Vector class"""
    # Constructor
    def __init__(self, values):
        if isinstance(values, list):
            self.values = values
            if len(values) == 1:
                self.shape = (1, len(values[0]))
            else:
                self.shape = (len(values), 1)
        elif isinstance(values, int):
            self.values = [[float(i)] for i in range(0, values)]
            self.shape = (values, 1)
        elif isinstance(values, tuple):
            self.values = [[float(i)] for i in range(values[0], values[1])]
            self.shape = (values[1] - values[0], 1)
        else:
            raise TypeError(f'Wrong type : {type(values)}')

    # Member functions
    def dot(self, v_2):
        """Dot product"""
        if v_2.shape[0] == self.shape[0] and v_2.shape[1] == self.shape[1]:
            if self.shape[1] == 1:
                return sum(self.values[i][0] * v_2.values[i][0]
                           for i in range(len(self.values)))
            else:
                return sum(self.values[0][i] * v_2.values[0][i]
                           for i in range(len(self.values[0])))
        else:
            raise AttributeError("Vectors don't have the same shape")

    def T(self):
        """Transpose vector (row / column)"""
        if self.shape[0] == 1:
            return Vector([[value] for value in self.values[0]])
        return Vector([[value[0] for value in self.values]])

    # Operators overload
    def __add__(self, rhs):
        if rhs.shape[0] == self.shape[0] and rhs.shape[1] == self.shape[1]:
            if self.shape[1] == 1:
                return Vector([[self.values[i][0] + rhs.values[i][0]]
                              for i in range(len(self.values))])
            return Vector([[self.values[0][i] + rhs.values[0][i]
                          for i in range(len(self.values[0]))]])
        raise AttributeError("Vectors don't have the same shape")

    def __radd__(self, rhs):
        if rhs.shape[0] == self.shape[0] and rhs.shape[1] == self.shape[1]:
            if self.shape[1] == 1:
                return Vector([[rhs.values[i][0] + self.values[i][0]]
                              for i in range(len(self.values))])
            return Vector([[rhs.values[0][i] + self.values[0][i]
                              for i in range(len(self.values[0]))]])
        raise AttributeError("Vectors don't have the same shape")

    def __sub__(self, rhs):
        if rhs.shape[0] == self.shape[0] and rhs.shape[1] == self.shape[1]:
            if self.shape[1] == 1:
                return Vector([[self.values[i][0] - rhs.values[i][0]]
                              for i in range(len(self.values))])
            return Vector([[self.values[0][i] - rhs.values[0][i]
                              for i in range(len(self.values[0]))]])
        raise AttributeError("Vectors don't have the same shape")

    def __rsub__(self, rhs):
        if rhs.shape[0] == self.shape[0] and rhs.shape[1] == self.shape[1]:
            if self.shape[1] == 1:
                return Vector([[rhs.values[i][0] - self.values[i][0]]
                              for i in range(len(self.values))])
            return Vector([[rhs.values[0][i] - self.values[0][i]
                              for i in range(len(self.values[0]))]])
        raise AttributeError("Vectors don't have the same shape")

    def __truediv__(self, scalar):
        if scalar == 0:
            raise ArithmeticError("Division by 0.")
        if self.shape[1] == 1:
            return Vector([[value[0] / scalar] for value in self.values])
        return Vector([[value / scalar for value in self.values[0]]])

    def __rtruediv__(self, scalar):
        raise ArithmeticError("Division of a scalar by a Vector"
                              " is not defined here.")

    def __mul__(self, scalar):
        if self.shape[1] == 1:
            return Vector([[value[0] * scalar] for value in self.values])
        return Vector([[value * scalar for value in self.values[0]]])

    def __rmul__(self, scalar):
        if self.shape[1] == 1:
            return Vector([[scalar * value[0]] for value in self.values])
        return Vector([[scalar * value for value in self.values[0]]])

    def __str__(self):
        return f'{self.values}'

    def __repr__(self):
        return f'{self.values}'
