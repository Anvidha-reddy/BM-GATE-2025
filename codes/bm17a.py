import numpy as np
import matplotlib.pyplot as plt

# Range of n
n = np.arange(-5, 11)

# Unit impulse function
def delta(n):
    return (n == 0).astype(int)

# x[n] = delta[n] + delta[n-1]
x = delta(n) + delta(n - 1)

# h[n] = delta[n] + (1/2)delta[n-1] + (1/3)delta[n-2]
h = delta(n) + (1/2)*delta(n - 1) + (1/3)*delta(n - 2)

# Calculate convolution y[n] for all n
y = np.zeros(len(n))

for i in range(len(n)):
    for k in range(len(n)):
        y[i] += x[k] * h[i - k] if 0 <= i-k < len(n) else 0

# Plot
plt.figure(figsize=(8, 8))

plt.subplot(3, 1, 1)
plt.stem(n, x)
plt.xlabel('n')
plt.ylabel('x[n]')
plt.title('Input Signal x[n]')
plt.grid(True)

plt.subplot(3, 1, 2)
plt.stem(n, h)
plt.xlabel('n')
plt.ylabel('h[n]')
plt.title('Impulse Response h[n]')
plt.grid(True)

plt.subplot(3, 1, 3)
plt.stem(n, y)
plt.xlabel('n')
plt.ylabel('y[n]')
plt.title('Output Signal y[n]')
plt.grid(True)

plt.tight_layout()
plt.savefig('bm17a.png', dpi=300)
