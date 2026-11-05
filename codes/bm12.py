import os
import shutil
import subprocess
import shlex
from math import comb, sqrt, pi

import numpy as np
import matplotlib.pyplot as plt

# Import custom matrix and vector modules
from CoordGeo.line.funcs import line_gen_num

# Inputs (press Enter to use the defaults N = 64, p = 0.25)
N = int(input("Enter N [64]: ") or 64)
p = float(input("Enter p [0.25]: ") or 0.25)

# Initialize figure
fig, ax = plt.subplots(figsize=(9, 6), layout='constrained')

# X values
x = np.arange(N + 1)

# Binomial PMF
pmf = np.array([comb(N, i) * p**i * (1 - p)**(N - i) for i in x])

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
# Fine x-axis for smooth PDF, generated as points on a line
A_pdf = np.array([max(0, mu - 4 * sigma), 0.0]).reshape(-1, 1)
B_pdf = np.array([min(N, mu + 4 * sigma), 0.0]).reshape(-1, 1)
x_pdf = line_gen_num(A_pdf, B_pdf, 1000)[0, :]

pdf = (1 / (sigma * sqrt(2 * pi))) * np.exp(-0.5 * ((x_pdf - mu) / sigma)**2)

# Binomial PMF
ax.stem(x, pmf, linefmt='C0-', markerfmt='C0o', basefmt='C0-', label='Binomial PMF')

# Normal PDF
ax.plot(x_pdf, pdf, 'C1-', linewidth=2, label='Normal PDF (same mean & variance)')

# Formatting plot area
ax.set_title('Binomial PMF and Normal PDF')
ax.grid(True, linestyle='--', alpha=0.5)

# Remove the outer plot box (spines)
for spine in ax.spines.values():
    spine.set_visible(False)

# Axis labels
ax.set_xlabel('X')
ax.set_ylabel('Probability / Density')

# Legend
ax.legend(bbox_to_anchor=(1.02, 1), loc='upper left', borderaxespad=0., frameon=True)

# Save figure (run from repo root: python3 codes/bm12.py)
os.makedirs('figs', exist_ok=True)
plt.savefig('figs/bm12.png', dpi=300)

# Open the image: termux-open on phone, normal window on laptop/PC
if shutil.which('termux-open'):
    subprocess.run(shlex.split("termux-open figs/bm12.png"))
else:
    plt.show()
