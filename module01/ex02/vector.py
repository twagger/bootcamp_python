from locale import setlocale


class Vector:

    # Constructor
    def __init__(self, values):
        if type(values) is list:
            self.values = values
            if len(values) == 1:
                self.shape = (1, len(values[0]))
            else:
                self.shape = (len(values), 1)
        elif type(values) is int:
            self.values = [[float(i)] for i in range(0, values)]
            self.shape = (values, 1)
        elif type(values) is tuple:
            self.values = [[float(i)] for i in range(values[0], values[1])]
            self.shape = (values[1] - values[0], 1)
        else:
            raise TypeError("Wrong type : {}".format(type(values)))
    
    # Member functions    
    def dot(self, v2):
        if v2.shape[0] == self.shape[0] and v2.shape[1] == self.shape[1]:
            if self.shape[1] == 1:
                return sum(self.values[i][0] * v2.values[i][0] for i in range(len(self.values))) 
            else:
                return sum(self.values[0][i] * v2.values[0][i] for i in range(len(self.values[0]))) 
        else:
            raise Exception("Vectors don't have the same shape")

    def T(self):
        if self.shape[0] == 1:
            return Vector([[value] for value in self.values[0]])
        else:
            return Vector([[value[0] for value in self.values]])

    # Operators overload
    def __add__(self, rhs):
        if rhs.shape[0] == self.shape[0] and rhs.shape[1] == self.shape[1]:
            if self.shape[1] == 1:
                return Vector([[self.values[i][0] + rhs.values[i][0]] for i in range(len(self.values))]) 
            else:
                return Vector([[self.values[0][i] + rhs.values[0][i] for i in range(len(self.values[0]))]]) 
        else:
            raise Exception("Vectors don't have the same shape")

    def __radd__(self, rhs):
        if rhs.shape[0] == self.shape[0] and rhs.shape[1] == self.shape[1]:
            if self.shape[1] == 1:
                return Vector([[rhs.values[i][0] + self.values[i][0]] for i in range(len(self.values))]) 
            else:
                return Vector([[rhs.values[0][i] + self.values[0][i] for i in range(len(self.values[0]))]]) 
        else:
            raise Exception("Vectors don't have the same shape")

    def __sub__(self, rhs):
        if rhs.shape[0] == self.shape[0] and rhs.shape[1] == self.shape[1]:
            if self.shape[1] == 1:
                return Vector([[self.values[i][0] - rhs.values[i][0]] for i in range(len(self.values))]) 
            else:
                return Vector([[self.values[0][i] - rhs.values[0][i] for i in range(len(self.values[0]))]]) 
        else:
            raise Exception("Vectors don't have the same shape")

    def __rsub__(self, rhs):
        if rhs.shape[0] == self.shape[0] and rhs.shape[1] == self.shape[1]:
            if self.shape[1] == 1:
                return Vector([[rhs.values[i][0] - self.values[i][0]] for i in range(len(self.values))]) 
            else:
                return Vector([[rhs.values[0][i] - self.values[0][i] for i in range(len(self.values[0]))]]) 
        else:
            raise Exception("Vectors don't have the same shape")

    def __truediv__(self, scalar):
        if scalar == 0:
            raise Exception("Division by 0.")
        else:
            if self.shape[1] == 1:
                return Vector([[value[0] / scalar] for value in self.values]) 
            else:
                return Vector([[value / scalar for value in self.values[0]]]) 

    def __rtruediv__(self, scalar):
        raise Exception("Division of a scalar by a Vector is not defined here.")
    
    def __mul__(self, scalar):
        if self.shape[1] == 1:
            return Vector([[value[0] * scalar] for value in self.values]) 
        else:
            return Vector([[value * scalar for value in self.values[0]]])
    
    def __rmul__(self, scalar):
        if self.shape[1] == 1:
            return Vector([[scalar * value[0]] for value in self.values]) 
        else:
            return Vector([[scalar * value for value in self.values[0]]]) 

    def __str__(self):
        return ("{}".format(self.values))

    def __repr__(self):
        return ("{}".format(self.values))
