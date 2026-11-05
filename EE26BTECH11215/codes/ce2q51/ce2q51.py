import numpy as np

# Given data
x = np.array([1, 2, 4, 8])
p = np.array([0.3, 0.1, 0.3, 0.3])

# Calculate mean and mean of squares
mean = np.sum(x * p)
mean_sq = np.sum((x**2) * p)

# Variance and standard deviation
variance = mean_sq - (mean**2)
std_dev = np.sqrt(variance)

print(f"Mean: {mean}")
print(f"Variance: {variance:.2f}")
print(f"Standard Deviation: {std_dev:.1f}")
