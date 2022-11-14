from vector import Vector

# Basic column Vector test
print("\n\033[1;35m--Test 1: Create a basic column vector--\033[0m")
v1 = Vector([[0.0], [1.0], [2.0], [3.0]])
print(f'Shape\t: {v1.shape}\nValues\t: {v1.values}')

# Basic row Vector test
print("\n\033[1;35m--Test 2: Create a basic row vector--\033[0m")
v1 = Vector([[0.0, 1.0, 2.0, 3.0]])
print(f'Shape\t: {v1.shape}\nValues\t: {v1.values}')

# Transpose test Row to Column
print("\n\033[1;35m--Test 3: Transpose a Row vector to a Column--\033[0m")
v1 = Vector([[0.0, 1.0, 2.0, 3.0]])
v2 = v1.T()
print(f'Transposed vector shape is : {v2.shape}')
print(f'Shape\t: {v2.shape}\nValues\t: {v2.values}')

# Transpose test Column to Row
print("\n\033[1;35m--Test 4: Transpose a Column vector to a Row--\033[0m")
v1 = Vector([[0.0], [1.0], [2.0], [3.0]])
v2 = v1.T()
print(f'Transposed vector shape is : {v2.shape}')
print(f'Shape\t: {v2.shape}\nValues\t: {v2.values}')

# Dot product fail
print("\n\033[1;35m--Test 5: Dot product fail--\033[0m")
v1 = Vector([[0.0, 1.0, 2.0, 3.0]])
v2 = Vector([[2.0, 4.0, 8.0, 16.0, 32.0]])
try:
    print(f'Dot product is : {v1.dot(v2)}')
except AttributeError as e:
    print(e)

# Dot product of two column vectors
print("\n\033[1;35m--Test 6: Dot product of two column vectors--\033[0m")
v1 = Vector([[0.0], [1.0], [2.0], [3.0]])
v2 = Vector([[2.0], [4.0], [8.0], [16.0]])
print(f'Dot product is : {v1.dot(v2)}')

# Dot product of two row vectors
print("\n\033[1;35m--Test 7: Dot product of two column vectors--\033[0m")
v1 = Vector([[0.0, 1.0, 2.0, 3.0]])
v2 = Vector([[2.0, 4.0, 8.0, 16.0]])
print(f'Dot product is : {v1.dot(v2)}')

# Addition two row vectors
print("\n\033[1;35m--Test 8: Addition of two row vectors--\033[0m")
v1 = Vector([[0.0, 1.0, 2.0, 3.0]])
v2 = Vector([[2.0, 4.0, 8.0, 16.0]])
print(f'V1\t: {v1.values}')
print(f'V2\t: {v2.values}')
print(f'Result of addition is : {(v1 + v2).values}')

# Addition two column vectors
print("\n\033[1;35m--Test 9: Addition of two column vectors--\033[0m")
v1 = Vector([[0.0], [1.0], [2.0], [3.0]])
v2 = Vector([[2.0], [4.0], [8.0], [16.0]])
print(f'V1\t: {v1.values}')
print(f'V2\t: {v2.values}')
print(f'Result of addition is : {(v1 + v2).values}')

# STR on vector
print("\n\033[1;35m--Test 10: STR on row and column vector--\033[0m")
v1 = Vector([[0.0], [1.0], [2.0], [3.0]])
v1 = Vector([[0.0, 1.0, 2.0, 3.0]])
print(v1)
print(v2)

# init vector with size 3
print("\n\033[1;35m--Test 11: Init vector with size 3--\033[0m")
v1 = Vector(3)
print(v1)
print(f'Shape\t: {v1.shape}')

# init vector with range 10 - 18
print("\n\033[1;35m--Test 12: Init vector with range 10 - 18--\033[0m")
v1 = Vector((10, 18))
print(v1)
print(f'Shape\t: {v1.shape}')

# Substract
print("\n\033[1;35m--Test 13: Substract--\033[0m")
v1 = Vector([[0.0, 1.0, 2.0, 3.0]])
v2 = Vector([[2.0, 4.0, 8.0, 16.0]])
print(v1)
print(v2)
print(v1 - v2)

# RSubstract
print("\n\033[1;35m--Test 14: RSubstract--\033[0m")
v1 = Vector([[0.0, 1.0, 2.0, 3.0]])
v2 = Vector([[2.0, 4.0, 8.0, 16.0]])
print(v1)
print(v2)
print(v1.__rsub__(v2))

# TrueDiv
print("\n\033[1;35m--Test 15: TrueDiv--\033[0m")
v1 = Vector([[0.0, 1.0, 2.0, 3.0]])
v2 = Vector([[0.0], [1.0], [2.0], [3.0]])
print(v1)
print(v1 / 2)
print(v2)
print(v2 / 2)

# RTrueDiv
print("\n\033[1;35m--Test 16: RTrueDiv--\033[0m")
v1 = Vector([[0.0, 1.0, 2.0, 3.0]])
print(v1)
try:
    print(v1.__rtruediv__(2))
except ArithmeticError as e:
    print(e)

# Mul
print("\n\033[1;35m--Test 17: Mul--\033[0m")
v1 = Vector([[0.0, 1.0, 2.0, 3.0]])
v2 = Vector([[0.0], [1.0], [2.0], [3.0]])
print(v1)
print(v1 * 2)
print(v2)
print(v2 * 2)

# RMul
print("\n\033[1;35m--Test 18: RMul--\033[0m")
v1 = Vector([[0.0, 1.0, 2.0, 3.0]])
print(v1)
print(v1.__rmul__(2))
