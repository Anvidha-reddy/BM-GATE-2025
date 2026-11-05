# The implementation and plotting scripts are adapted from:
# {https://github.com/Chamarthikrishnamadhur/ID1063/tree/master/10-09-2026}
# MAdhur
# coded on 10-09-26
# import
import math
import shlex
import shutil #required import to run in both termux and ubuntu
import subprocess
import matplotlib.pyplot as plt
import numpy as np
import sympy as sp


# raphson and function solution
def func(x):
    return math.exp(x) - 2


def raph(x):
    return x - ((math.exp(x) - 2) / (math.exp(x)))


# base curve and grid setup
x = 1
x1 = np.linspace(-3, 2, 1000)
y1 = np.exp(x1) - 2
plt.plot(x1, y1)
plt.grid()

# solving using sympy
X = sp.symbols("X")
wq = sp.Eq(sp.exp(X), 2)
sol = sp.solve(wq, X)
plt.axvline(x=sol)
print("The solution is", sol) #priniting soln

# plot all 5 iterations on the same graph and label only first and last
for i in range(5):
    y = func(x)
    plt.plot(x, y, "o")
    if i == 0: #labelling initial guess
        plt.annotate(
            f"({x:.4f}, {y:.4f})",
            (x, y),
            textcoords="offset points",
            xytext=(-10, 10),
            ha="right",
        )
    elif i == 4: #labelling final guess
        plt.annotate(
            f"({x:.4f}, {y:.4f})",
            (x, y),
            textcoords="offset points",
            xytext=(-10, 10),
            ha="right",
        )
    x = raph(x)

print("RAPHSON gave", x)

# saving as PDF
plt.savefig("raph.pdf")
plt.close()

# view PDF (automatically detects xdg-open on Ubuntu or termux-open on Termux)
viewer = "xdg-open" if shutil.which("xdg-open") else "termux-open"
subprocess.run(shlex.split(f"{viewer} raph.pdf"))
