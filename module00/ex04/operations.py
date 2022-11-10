"""This module execute basic operations on two integers"""
import sys


def my_sum(A, B):
    """Sum of two integers"""
    return A + B


def my_difference(A, B):
    """Difference between two integers"""
    return A - B


def my_product(A, B):
    """Product of two integers"""
    return A * B


def my_quotient(A, B):
    """Quotient of two integers"""
    if B == 0:
        return "ERROR (division by zero)"
    return float(A / B)


def my_remainder(A, B):
    """Remainder of two integers"""
    if B == 0:
        return "ERROR (modulo by zero)"
    return A % B


if len(sys.argv) == 1:
    print("""Usage: python operations.py <number1> <number2>
Example:
    python operations.py 10 3""")
elif len(sys.argv) < 3:
    print("AssertionError: too few arguments")
elif len(sys.argv) > 3:
    print("AssertionError: too many arguments")
else:
    try:
        VAL = int(sys.argv[1])
        VAL = int(sys.argv[2])
    except ValueError:
        print("AssertionError: only integers")
    else:
        A = int(sys.argv[1])
        B = int(sys.argv[2])
        print(f'Sum:\t\t{my_sum(A, B)}\n'
              f'Difference:\t{my_difference(A, B)}\n'
              f'Product:\t{my_product(A, B)}\n'
              f'Quotient:\t{my_quotient(A, B)}\n'
              f'Remainder:\t{my_remainder(A, B)}'
              )
