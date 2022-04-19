import sys
import string
import textwrap

def my_sum(A, B):
	return (A + B)

def my_difference(A, B):
	return (A - B)

def my_product(A, B):
	return (A * B)

def my_quotient(A, B):
	if B == 0:
		return "ERROR (division by zero)"
	else:
		return float(A / B)

def my_remainder(A, B):
	if B == 0:
		return "ERROR (modulo by zero)"
	else:
		return (A % B)

if len(sys.argv) < 3:
	print(textwrap.dedent("""\
	Usage: python operations.py <number1> <number2>
	Example:
		python operations.py 10 3\
	"""))
elif len(sys.argv) > 3:
	print("AssertionError: too many arguments")
else:
	try:
		val = int(sys.argv[1])
		val = int(sys.argv[2])
	except ValueError:
		print("AssertionError: only integers")
	else:
		A = int(sys.argv[1])
		B = int(sys.argv[2])
		print(textwrap.dedent("""\
			Sum:		{}
			Difference:	{}
			Product:	{}
			Quotient:	{}
			Remainder:	{}\
		""".format(
			my_sum(A, B),
			my_difference(A, B),
			my_product(A, B),
			my_quotient(A, B),
			my_remainder(A, B)
		)))
