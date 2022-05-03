from vector import Vector

# Basic column Vector test
print("\n\033[1;35m--{}: {}--\033[0m".format("Test 1", "Create a basic column vector"))
v1 = Vector([[0.0], [1.0], [2.0], [3.0]])
print("Shape\t: {}\nValues\t: {}".format(v1.shape, v1.values))

# Basic row Vector test
print("\n\033[1;35m--{}: {}--\033[0m".format("Test 2", "Create a basic row vector"))
v1 = Vector([[0.0, 1.0, 2.0, 3.0]])
print("Shape\t: {}\nValues\t: {}".format(v1.shape, v1.values))

# Transpose test Row to Column
print("\n\033[1;35m--{}: {}--\033[0m".format("Test 3", "Transpose a Row vector to a Column"))
v1 = Vector([[0.0, 1.0, 2.0, 3.0]])
v2 = v1.T()
print("Transposed vector shape is : {}".format(v2.shape))
print("Shape\t: {}\nValues\t: {}".format(v2.shape, v2.values))

# Transpose test Column to Row
print("\n\033[1;35m--{}: {}--\033[0m".format("Test 4", "Transpose a Column vector to a Row"))
v1 = Vector([[0.0], [1.0], [2.0], [3.0]])
v2 = v1.T()
print("Transposed vector shape is : {}".format(v2.shape))
print("Shape\t: {}\nValues\t: {}".format(v2.shape, v2.values))

# Dot product fail
print("\n\033[1;35m--{}: {}--\033[0m".format("Test 5", "Dot product fail"))
v1 = Vector([[0.0, 1.0, 2.0, 3.0]])
v2 = Vector([[2.0, 4.0, 8.0, 16.0, 32.0]])
try:
    print("Dot product is : {}".format(v1.dot(v2)))
except Exception as e:
    print(e)

# Dot product of two column vectors
print("\n\033[1;35m--{}: {}--\033[0m".format("Test 6", "Dot product of two column vectors"))
v1 = Vector([[0.0], [1.0], [2.0], [3.0]])
v2 = Vector([[2.0], [4.0], [8.0], [16.0]])
print("Dot product is : {}".format(v1.dot(v2)))

# Dot product of two row vectors
print("\n\033[1;35m--{}: {}--\033[0m".format("Test 7", "Dot product of two column vectors"))
v1 = Vector([[0.0, 1.0, 2.0, 3.0]])
v2 = Vector([[2.0, 4.0, 8.0, 16.0]])
print("Dot product is : {}".format(v1.dot(v2)))

# Addition two row vectors
print("\n\033[1;35m--{}: {}--\033[0m".format("Test 8", "Addition of two row vectors"))
v1 = Vector([[0.0, 1.0, 2.0, 3.0]])
v2 = Vector([[2.0, 4.0, 8.0, 16.0]])
print("V1\t: {}".format(v1.values))
print("V2\t: {}".format(v2.values))
print("Result of addition is : {}".format((v1 + v2).values))

# Addition two column vectors
print("\n\033[1;35m--{}: {}--\033[0m".format("Test 9", "Addition of two column vectors"))
v1 = Vector([[0.0], [1.0], [2.0], [3.0]])
v2 = Vector([[2.0], [4.0], [8.0], [16.0]])
print("V1\t: {}".format(v1.values))
print("V2\t: {}".format(v2.values))
print("Result of addition is : {}".format((v1 + v2).values))