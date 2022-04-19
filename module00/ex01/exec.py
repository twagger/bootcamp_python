import sys

if len(sys.argv) == 1:
	print("Usage: python exec.py [Arguments] ...")
else:
	result = ' '.join(sys.argv[1:])
	result = result[::-1]
	result = result.swapcase();
	print(result)