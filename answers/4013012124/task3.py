import numpy as np

print("1.")
array_1 = np.array([[180, 5, 28],
                    [60, 75, 40]])
array_2 = np.array([[30, 45, 7],
                    [2, 15, 84]])

# Subtract array_2 from array_1
print("A-B:\n", np.subtract(array_1, array_2))

# Add array_1 and array_2
print("A+B:\n", np.add(array_1, array_2))

# Multiply array_1 and array_2 element-wise
print("A*B:\n", np.multiply(array_1, array_2))

# Divide array_1 by array_2 element-wise
print("A/B:\n", np.divide(array_1, array_2))
print("___________________________________")

print("2.")
matrix = np.array([[15, 2, 92],
                   [23, 72, 86],
                   [90, 5, 3]])
vector = np.array([45, 100, 155])

# Add the vector to the matrix using broadcasting
print("Matrix + vector: \n", np.add(matrix, vector))
print("___________________________________")

print("3.")
array_3d = np.array([[[18, 2, 63],
                      [84, 0, 5]],

                     [[15, 54, 12],
                      [60, 71.8, 96]],

                     [[32, 76, 41.2],
                      [89, 67.3, 8]]])

# Reshape the 3D array to a 2D matrix
matrix_2d = array_3d.reshape(-1, 3)
print("Converted to 2D:\n", matrix_2d)

# Flatten the 2D matrix to a 1D array
matrix_1d = matrix_2d.flatten()
print("Flatten:\n", matrix_1d)
