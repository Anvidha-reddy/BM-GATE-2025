import matplotlib.pyplot as plt
import numpy as np

# 1. Define the x range (from -10 to 10 with 400 points)
x = np.linspace(-3, 3, 400)


y = x-1/x
y1=2*x-2
# 3. Create the plot figure
plt.figure(figsize=(8, 6))
plt.plot(x, y, color="blue", linewidth=2)
plt.plot(x,y1,color="red", linewidth=2)
# 4. Add labels, grid, and legend
plt.title("Graph of f(x) = x² - 4")
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.axhline(0, color="black", linewidth=1)
plt.axvline(0, color="black", linewidth=1)
plt.grid(True, linestyle="--", alpha=0.7)


# 5. Save the plot as an image file
plt.savefig("ASDFGh.png", dpi=300)

# 6. Display the plot on screen
