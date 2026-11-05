# By Nehan mohammad
# 05-October-26, Monday, question no: cubic_polynomial

import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
import subprocess

# Analytical calculations via SymPy
x_sym = sp.symbols('x')
f_sym = x_sym**3 - (15/2)*x_sym**2 + 18*x_sym + 20
df = sp.diff(f_sym, x_sym)
ddf = sp.diff(df, x_sym)

critical_points = sp.solve(df, x_sym)
for pt in critical_points:
    val = ddf.subs(x_sym, pt)
    print(f"x = {float(pt):.2f}, Second Derivative = {float(val):.3f} ({'Local Min' if val > 0 else 'Local Max'})")

# Define numerical function
def f(x):
    return x**3 - (15/2)*x**2 + 18*x + 20

# Generate x values around the critical points
x = np.linspace(-2, 7, 400)
y = f(x)

# Critical points
x_crit = np.array([float(pt) for pt in critical_points])
y_crit = f(x_crit)

# Create the plot
plt.figure(figsize=(8, 5))
plt.plot(x, y, label=r'$f(x) = x^3 - \frac{15}{2}x^2 + 18x + 20$', color='blue', linewidth=0.8)

# Highlight local extrema
plt.scatter(x_crit, y_crit, color='red', zorder=5)
plt.annotate('Local Max (x=2)', (x_crit[0], y_crit[0]), textcoords="offset points", xytext=(-30, 15),  fontsize=8)
plt.annotate('Local Min (x=3)', (x_crit[1], y_crit[1]), textcoords="offset points", xytext=(-30, -25),  fontsize=8)

# Styling the plot
plt.title('Graph of the Cubic Polynomial and Critical Points', fontsize=8 )
plt.xlabel('x', fontsize=7)
plt.ylabel('f(x)', fontsize=7)
plt.axhline(0, color='black', linewidth=0.8, linestyle='-')
plt.axvline(0, color='black', linewidth=0.8, linestyle='-')
plt.grid(True, linestyle='--', linewidth=0.5 )
plt.legend(fontsize=9, loc='upper left')

plt.savefig('figs/cubic.png', dpi=300, bbox_inches='tight')
#subprocess.run(['termux-open', 'cubic.png'])
