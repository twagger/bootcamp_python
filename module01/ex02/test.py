from vector import Vector

# Basic column Vector test
print("\n\033[1;35m--{}: {}--\033[0m".format("Test 1", "Create a basic column vector"))
v1 = Vector([[0.0], [1.0], [2.0], [3.0]])
print("Shape\t: {}\nValues\t: {}".format(v1.shape, v1.values))

# Basic raw Vector test
print("\n\033[1;35m--{}: {}--\033[0m".format("Test 2", "Create a basic raw vector"))
v1 = Vector([[0.0, 1.0, 2.0, 3.0]])
print("Shape\t: {}\nValues\t: {}".format(v1.shape, v1.values))