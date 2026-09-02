#Question 1
import math

# Step ratio factor: 12th root of 2
factor = 2 ** (1 / 12)

# F# is 6 steps away from C (C -> C# -> D -> D# -> E -> F -> F#)
steps = 6

# Ratio of frequencies: f(F#) / f(C)
ratio = factor**steps

print(f"Calculated Ratio: {ratio:.6f}")
print(f"sqrt(2) Value:    {math.sqrt(2):.6f}")



#Question 2
def curve_length(n: int) -> float:
    """Calculates the total length of the curve at iteration n."""
    return (5 / 3) ** n
  
# Example usage
if __name__ == "__main__":
    print("--- Iteration Lengths ---")
    for n in range(6):
        length = curve_length(n)
        print(f"Iteration {n}: Total Length = {length:.4f} or (5/3)^{n}")


#Question 8
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



#Question 9
from statistics import mean, median

#Given Data
data=[-5,1,3,5,11]

print("Data: ",data)
print("Mean: ",mean(data))
print("Median: ",median(data))

#Verify
if mean(data)==3 and median(data)==3:
  print("Therefore, a=3 and b=11")


#Question 10
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
