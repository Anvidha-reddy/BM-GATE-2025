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



#Question 12
import numpy as np
import matplotlib.pyplot as plt
from math import comb

N = int(input("Enter N: "))
p = float(input("Enter p: "))

x = np.arange(N + 1)

pmf = np.array([comb(N, i) * p**i * (1-p)**(N-i) for i in x])

print("x =", x)
print("PMF =", pmf)

plt.stem(x, pmf)
plt.xlabel("X")
plt.ylabel("P(X = x)")
plt.title("Binomial PMF")
plt.savefig("pmf.png")

#OR
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



#Question 13
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



#Question 17
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




#Question 18

binary = "10110111"

# Number of bits
n = len(binary)

# Convert binary to decimal
D = int(binary, 2)

# Reference voltage
Vref = 5

# DAC output
Vout = (D / (2**n - 1)) * Vref

print("Decimal value =", D)
print("DAC output =", round(Vout, 2), "V")



#Question 21
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



#Question 23
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



