import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return (x*(np.cos(x))-np.sin(x))/((x**2)*np.sin(x))

x = np.linspace(-0.5, 0.5, 1000)

y = f(x)


plt.plot(x, y, color='blue', linestyle='-', linewidth=2, label='f(x) = Given Function')
plt.axhline(y=-1/3, color='red', linestyle='-', linewidth=2, label='f(x) = -0.33333')

plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True, alpha=0.5)
plt.tight_layout()
plt.legend()

 
plt.show()
