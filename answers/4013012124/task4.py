import numpy as np

print("1.")
matrix1 = np.array([[7, 14],
                    [39, 5]])
print("Matrix 1:\n", matrix1, "\n")

matrix2 = np.array([[6, 2],
                    [1, 9]])
print("Matrix 2:\n", matrix2, "\n")

dot_product = np.dot(matrix1, matrix2)
print("\nDot Product Result:\n", dot_product, "\n")

print("___________________________________")
print("2.")
matrix = np.array([[9, 7],
                   [6, 5]])
print("Matrix:\n", matrix, "\n")

determine = np.linalg.det(matrix)
print("Determine:\n", determine, "\n")

inverse = np.linalg.inv(matrix)
print("Inverse:\n", inverse, "\n")

print("___________________________________")

print("3")
square_matrix = np.array([[4, 3],
                          [2, 1]])
print("Square matrix:\n", square_matrix, "\n")

eigenvalues, eigenvectors = np.linalg.eig(square_matrix)
print("Eigenvalues:\n", eigenvalues, "\n")
print("Eigenvectors:", eigenvectors, "\n")
