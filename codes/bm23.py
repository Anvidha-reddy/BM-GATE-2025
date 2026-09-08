import numpy as np
import matplotlib.pyplot as plt

# Given condition
sigma0 = 2 + 2*np.log(4)

# Time in weeks
t = np.linspace(1, 12, 500)

# Strength equation
sigma = sigma0 - 2*np.log(t)

# Plot
plt.plot(t, sigma)
plt.xlabel("Time (weeks)")
plt.ylabel("Strength (MPa)")
plt.title("Strength of Implanted Suture")
plt.grid(True)

# Mark the given point (4, 2)
plt.plot(4, 2, 'o')

# Mark the strength at 8 weeks
sigma8 = sigma0 - 2*np.log(8)
plt.plot(8, sigma8, 'o')

plt.savefig("strength_graph.png", dpi=300, bbox_inches="tight")
