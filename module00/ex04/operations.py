import sys


def ft_sum(n1, n2):
    print("Sum:\t\t", end='')
    res = int(n1) + int(n2)
    print(res)


def ft_diff(n1, n2):
    print("Difference:\t", end='')
    res = int(n1) - int(n2)
    print(res)


def ft_product(n1, n2):
    print("Product:\t", end='')
    res = int(n1) * int(n2)
    print(res)


def ft_quotient(n1, n2):
    print("Quotient:\t", end='')
    if int(n2) == 0:
        print("ERROR (div by zero)")
    else:
        res = int(n1) / int(n2)
        print("{:.1f}".format(res))


def ft_remainder(n1, n2):
    print("Remainder:\t", end='')
    if int(n2) == 0:
        print("ERROR (modulo by zero)")
    else:
        res = int(n1) % int(n2)
        print(res)


first = True
if len(sys.argv) == 1:
    print("Usage: python operations.py <number1> <number2>")
    print("Example:")
    print("\tpython operations.py 10 3")
elif len(sys.argv) > 3:
    print("InputError: too many arguments")
elif len(sys.argv) == 2:
    print("InputError: too few arguments")
elif len(sys.argv) == 3:
    for arg in sys.argv:
        if first:
            first = False
        elif not arg.strip('-').isdecimal():
            print("InputError: only numbers")
            sys.exit()
    ft_sum(sys.argv[1], sys.argv[2])
    ft_diff(sys.argv[1], sys.argv[2])
    ft_product(sys.argv[1], sys.argv[2])
    ft_quotient(sys.argv[1], sys.argv[2])
    ft_remainder(sys.argv[1], sys.argv[2])
