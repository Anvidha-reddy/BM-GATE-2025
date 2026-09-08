import matplotlib.pyplot as plt
import numpy as np

# Domain setup for clear stem visualization
x0, x_end = 0, 5
h = 0.2  # Step size
N = int((x_end - x0) / h) + 1

x = np.linspace(x0, x_end, N)

# 1. Discrete Euler Recurrence relation: y_{n+1} = 2*y_n - (1 - h^2/4)*y_{n-1}
y_rec = np.zeros(N)
y_rec[0] = 1.0  # Initial condition: y_0 = 1
y_rec[1] = 1.0 + h  # First forward step: y_1 = y_0 + h*v_0

for n in range(1, N - 1):
    y_rec[n + 1] = 2.0 * y_rec[n] - (1.0 - (h**2) / 4.0) * y_rec[n - 1]

# 2. Exact Theoretical Solution for comparison
y_exact = 1.5 * np.exp(0.5 * x) - 0.5 * np.exp(-0.5 * x)

# 3. Stem Plotting
plt.figure(figsize=(9, 5))

# Stem plot of discrete Euler values y_n
markerline, stemlines, baseline = plt.stem(
    x,
    y_rec,
    linefmt='r-',
    markerfmt='ro',
    basefmt='k-',
    label='Euler Recurrence ($y_n$)',
)
plt.setp(stemlines, linewidth=1.5)
plt.setp(markerline, markersize=6)

# Overlay theoretical curve
plt.plot(
    x,
    y_exact,
    'b--',
    linewidth=2,
    label=r'Theoretical $y(x) = 1.5e^{0.5x} - 0.5e^{-0.5x}$',
)

plt.xlabel('x')
plt.ylabel('y_n')
plt.title(
    r'Stem Plot of Euler Recurrence Relation ($y_{n+1} = 2y_n - (1 - h^2/4)y_{n-1}$)'
)
plt.grid(True, linestyle='--', alpha=0.5)
plt.legend()
plt.tight_layout()
plt.savefig("ForwardDifference",dpi=150)
plt.show()
