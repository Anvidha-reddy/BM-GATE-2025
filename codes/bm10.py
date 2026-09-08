import numpy as np
import matplotlib.pyplot as plt

# Time values
t = np.linspace(0, 0.1, 5000)

# Given signal
x = (20 * np.sin(100 * np.pi * t)
     + 36 * np.sin(150 * np.pi * t)
     - 2 * np.sin(300 * np.pi * t))

# Plot
plt.figure(figsize=(10, 5))
plt.plot(t, x)

plt.xlabel("Time (seconds)")
plt.ylabel("x(t)")
plt.title("x(t) = 20sin(100πt) + 36sin(150πt) - 2sin(300πt)")
plt.grid(True)

plt.tight_layout()
plt.savefig("graph.png", dpi=150)
