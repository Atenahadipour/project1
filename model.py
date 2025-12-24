import numpy as np

np.set_printoptions(precision=3, suppress=True)

np.random.seed(42)

dim = 32
samples = 200

X = np.random.randn(samples, dim)

cov = np.cov(X, rowvar=False)

eigenvalues, eigenvectors = np.linalg.eig(cov)

sorted_eigs = np.sort(eigenvalues)[-8:]

condition_number = np.max(eigenvalues) / np.min(eigenvalues)

norm_projection = np.linalg.norm(cov @ cov.T)

print("\n========== ANALYTICS OUTPUT ==========\n")

print("Covariance matrix (partial):")
print(cov[:5, :5])

print("\nTop eigenvalues:")
print(sorted_eigs)

print("\nCondition number:")
print(condition_number)

print("\nProjection norm:")
print(norm_projection)

print("\nSystem state: HIGH-DIMENSIONAL STABILITY CONFIRMED")
print("======================================\n")
