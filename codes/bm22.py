import numpy as np

import matplotlib.pyplot as plt


x = int(input("Input the initial guess: "))
y = int(input("Input the number of new guesses: "))

values = []

for i in range(y):
    y = x - (x**3 - 2*x - 5)/(3*x**2 - 2)
    print(f"The Value of x{i+1} is {y}")
    values.append(y)
    x = y


x = np.linspace(1, 3.5, 100)
y = x**3 - 2*x - 5

x = np.linspace(1, 3.5, 100)
y = x**3 - 2*x - 5

plt.plot(x, y)

for i in range(3):
    plt.plot(values[i], values[i]**3 - 2*values[i] - 5, 'ro')
    plt.text(values[i], values[i]**3 - 2*values[i] - 5,
             "x" + str(i+1))

plt.axhline(0)
plt.grid()
plt.savefig("bm22.png")
