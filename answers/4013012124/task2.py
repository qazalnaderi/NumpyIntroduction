import numpy as np

print("1.")
# Create a one-dimensional numpy array
array_1D = np.array([8, 64, 51, 90, 17])
print("one-dimensional array: ", array_1D, "\n")

# Access and print the third element of the one-dimensional array
print("Third element of the one-dimensional array is:", array_1D[2],"\n")

# Create a two-dimensional numpy array
array_2D = np.array([[34, 5, 12, 9],
                     [1, 71, 130, 47],
                     [5, 19, 10, 23]])
print("two-dimensional matrix:\n", array_2D,"\n")

# Access and print the element at position (2, 3) in the two-dimensional matrix
element_2D = array_2D[2, 3]
print("Element at position (2, 3) in the two-dimensional matrix is:", element_2D,"\n")
print("___________________________________")

print("2.")
# Extract a sub-matrix from the upper left corner of the two-dimensional matrix
sub_mat = array_2D[:2, :2]
print("Sub-matrix from the upper left corner of two-dimensional matrix is: \n", sub_mat, "\n")

print("3.")
array_3D = [
    [[2, 4], [8, 10]],
    [[3, 6], [9, 12]],
    [[4, 8], [12, 16]]
]

# Iterate over the three-dimensional array
for i in range(len(array_3D)):
    print(f"Section {i + 1}:")
    for row in array_3D[i]:
        print(row)