import numpy as np

print("1.")
array = np.array([5, 82, 36, 9, 29, 48])
print("Array:\n", array, "\n")
mean = np.mean(array)
print("Mean:", mean, "\n")

median = np.median(array)
print("Median:\n", median, "\n")

variance = np.var(array)
print("Variance:\n", variance, "\n")

standard_devision = np.std(array)
print("Standard deviation:\n", standard_devision,"\n")

print("_________________")
print("2.")


array1 = np.array([6, 10, 14, 16])
print("Array1:\n", array1,"\n")
array2 = np.array([9, 21, 7, 19])
print("Array2:\n", array2,"\n")
correlation_coefficient = np.corrcoef(array1, array2)
print("Correlation Coefficient:\n", correlation_coefficient)
