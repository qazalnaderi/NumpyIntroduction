import numpy as np


def printInfo(mat):
    print(mat)
    print("Dimensions:", mat.ndim)
    print("Shape:", mat.shape)
    print("Size:", mat.size)
    print("Elements' Type:", mat.dtype)
    print("Sum of elements:", np.sum(mat))
    print("\n\n")


test_list = [54, 78, 100, 28, 3]
array_1D = np.array(test_list)
print("One-dimensional array")
printInfo(array_1D)

print("Two-dimensional matrix with dimensions (3 \\times 4) filled with zeros")
array_2D = np.zeros((3, 4))
printInfo(array_2D)

print("Three-dimensional array with dimensions (2 \\times 3 \\times 4) filled with ones")
array_2D = np.ones((2, 3, 4))
printInfo(array_2D)
