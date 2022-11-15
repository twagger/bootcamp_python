"""This module checks if the provided argument is even or odd"""
import sys


if __name__ == "__main__":
    # check argument number
    if len(sys.argv) <= 1:
        print("Usage: python whois.py <Argument>")
    elif len(sys.argv) >= 3:
        print("AssertionError: more than one argument are provided")
    else:
        # check argument type
        if not (
            sys.argv[1].isdigit() is True
            or ((sys.argv[1][0] == '-' or sys.argv[1][0] == '+')
                and sys.argv[1][1:].isdigit() is True)):
            print("AssertionError: argument is not an integer")
        # check if even, odd or zero
        elif int(sys.argv[1]) == 0:
            print("I'm Zero.")
        elif int(sys.argv[1]) % 2 == 0:
            print("I'm Even.")
        else:
            print("I'm Odd.")
