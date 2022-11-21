"""Initiation to very basic statistic notions."""


from typing import Union
from typing import List
import math
import numpy as np

Vector = List[Union[int, float, complex]]


class TinyStatistician():
    """Tiny Statistician"""

    def __init__(self):
        """Constructor"""
        pass

    def mean(self, x: Vector) -> float:
        """Computes the mean of a given non-empty list or array x"""
        # Emptyness check
        if isinstance(x, (list, np.ndarray)) and len(x) == 0:
            return None
        # Computation
        result: float = 0
        for num in x:
            result += num
        return float(result / len(x))

    def median(self, x: Vector) -> float():
        """Computes the median of a given non-empty list or array x"""
        # Emptyness check
        if isinstance(x, (list, np.ndarray)) and len(x) == 0:
            return None
        # Computation
        x.sort()
        position: int = len(x) // 2
        if len(x) % 2 == 0:
            return float((x[position - 1] + x[position]) / 2)
        return float(x[position])

    def quartiles(self, x: Vector) -> Vector:
        """Computes the 1st and 3rd quartiles of a given non-empty array x"""
        # Emptyness check
        if isinstance(x, (list, np.ndarray)) and len(x) == 0:
            return None
        # Computation
        x.sort()
        position: int = len(x) // 2
        return ([
                 float(x[len(x[:position]) // 2]),
                 float(x[-len(x[position:]) // 2])
                ])

    def var(self, x: Vector) -> float:
        """computes the variance of a given non-empty list or array x"""
        # Emptyness check
        if isinstance(x, (list, np.ndarray)) and len(x) == 0:
            return None
        # Computation
        result = 0
        for num in x:
            result += (num - self.mean(x)) ** 2
        return float(result / len(x))


    def std(self, x: Vector) -> float:
        """ computes the standard deviation of a given non-empty list or
        array x"""
        # Emptyness check
        if isinstance(x, (list, np.ndarray)) and len(x) == 0:
            return None
        # Computation
        return math.sqrt(self.var(x))
