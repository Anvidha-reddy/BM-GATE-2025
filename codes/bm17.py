import numpy as np
import matplotlib.pyplot as plt

x = np.array([1, 1])
h = np.array([1, 1/2, 1/3])

y = np.convolve(x, h)

n = np.arange(len(y))

print("x[n] =", x)
print("h[n] =", h)
print("y[n] =", y)
print("y[2] =", y[2])

plt.stem(n, y)

plt.xlabel("n")
plt.ylabel("y[n]")
plt.title("Output Signal y[n] = x[n] * h[n]")
plt.xticks(n)
plt.grid()

plt.savefig("/sdcard/Download/convolution_stem.png")
