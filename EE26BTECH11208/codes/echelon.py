import sympy as sp

matrix = sp.Matrix([[2,2],[-3,-3]])
print("Matrix Before Converting:")
print(matrix)
print()
result,pivot = matrix.rref()
print("After Converting to Row Echelon Form:")
print(result)
print()
matrix2 = sp.Matrix([[3,-3],[2,-2]])
print("Matrix Before Converting:")
print(matrix2)
print()
result2,pivot = matrix2.rref()
print("After Converting to Row Echelon Form:")
print(result2)


