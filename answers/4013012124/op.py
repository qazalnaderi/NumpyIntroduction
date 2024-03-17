import numpy as np

print("1.")
array = np.array([[21, 7], [3, 70]])

# Perform SVD on array
U, S, V = np.linalg.svd(array)

# U: Unitary matrix having left singular vectors
# S: Array containing singular values in descending order
# V: Unitary matrix having right singular vectors

# Reconstruct the original array using the SVD components
array_reconstructed = np.dot(U, np.dot(np.diag(S), V))

print("Original matrix:")
print(array)
print("\nReconstructed matrix:")
print(array_reconstructed)
print("\nSingular values:")
print(S)
print("---------------------------------")

# Generate 10 random samples from a uniform distribution between 0 and 1
uniform_samples = np.random.uniform(0, 1, 5)
print("uniform samples: ", uniform_samples)

# Generate 10 random samples from a normal distribution with mean 0 and standard deviation 2
normal_samples = np.random.normal(0, 2, 7)
print("normal samples: ", normal_samples)

# Generate 10 random samples from a binomial distribution with n=5 trials and p=0.5 probability
binomial_samples = np.random.binomial(5, 0.5, 10)
print("binomial samples: ", binomial_samples)

# Generate 8 random samples from a Poisson distribution with lambda=2
poisson_samples = np.random.poisson(2, 8)
print("poisson samples: ", poisson_samples)
# Generate 6 random samples from an exponential distribution with scale parameter beta=4
exponential_samples = np.random.exponential(4, 6)
print("exponential samples: ", exponential_samples)
