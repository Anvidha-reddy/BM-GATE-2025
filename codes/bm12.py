import numpy as np
import matplotlib.pyplot as plt
from math import comb, sqrt, pi, exp

N = int(input("Enter N: "))
p = float(input("Enter p: "))

# X values
x = np.arange(N + 1)

# Binomial PMF
pmf = np.array([
    comb(N, i) * p**i * (1-p)**(N-i)
    for i in x
])

# Mean and variance of binomial
mu = N * p
variance = N * p * (1 - p)
sigma = sqrt(variance)

print("Mean =", mu)
print("Variance =", variance)
print("Standard deviation =", sigma)

print("x =", x)
print("PMF =", pmf)

# -----------------------------
# Normal PDF with same mean/variance
# -----------------------------

# Fine x-axis for smooth PDF
x_pdf = np.linspace(
    max(0, mu - 4*sigma),
    min(N, mu + 4*sigma),
    1000
)

pdf = (1 / (sigma * sqrt(2 * pi))) * np.exp(
    -0.5 * ((x_pdf - mu) / sigma)**2
)

# Plot
plt.figure(figsize=(9, 6))

# Binomial PMF
plt.stem(
    x,
    pmf,
    linefmt='C0-',
    markerfmt='C0o',
    basefmt='C0-',
    label='Binomial PMF'
)

# Normal PDF
plt.plot(
    x_pdf,
    pdf,
    'C1-',
    linewidth=2,
    label='Normal PDF (same mean & variance)'
)

plt.xlabel("X")
plt.ylabel("Probability / Density")
plt.title("Binomial PMF and Normal PDF")
plt.legend()
plt.grid(alpha=0.3)

plt.savefig("hi.png", dpi=300, bbox_inches="tight")
