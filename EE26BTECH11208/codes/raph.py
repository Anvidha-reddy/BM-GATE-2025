import matplotlib.pyplot as plt
import numpy as np
import sympy as sp



x2 = int(input("Input the initial guess: "))
z = int(input("Input the number of new guesses: "))

values = []

for i in range(z):
    y2 = x2 - (2*(x2**3) - 3*(x2**2) +3*(x2)-1)/(6*(x2**2) +(-6*(x2))+3)
    print(f"The Value of x{i+1} is {y2}")
    values.append(y2)
    x2 = y2


#x2 = np.linspace(-1, 3.5, 100)
#y2 = 2*x2**3 - 3*x2**2 + 3*x2-1

#x = np.linspace(1, 3.5, 100)
#y = x**3 - 2*x - 5

#plt.plot(x, y)
plt.plot(4, 2*4**3 - 3*4**2+3*4 - 1,marker='o',color="green",label="Newton Raphson")

for i in range(z):
    plt.plot(values[i], 2*values[i]**3 - 3*values[i]**2+3*values[i] - 1,marker='o',color="green")
    #plt.text(2*values[i]**3 - 3*values[i]**2+3*values[i] - 1,"x" + str(i+1))

plt.axhline(0)
plt.grid()
plt.savefig("nr.png")

X = sp.Symbol('X')


equation = sp.Eq(2*X**3 - 3* X**2 + 3 * X - 1, 0)

# Solve the equation
solutionsther = sp.solve(equation, X)

print("The exact solutions are:", solutionsther)
print("The sum of 2 solutions is 1")

x=np.linspace(-1,4,1000)
y=2*(x**3)-3*(x**2)+3*(x)-1
plt.plot(x,y)
plt.grid(True)
#plt.plot(x2,y2)
plt.title("Working of newton raphson")
plt.plot(solutionsther[0],0,marker='D',color='red',label="Theoretical")
plt.legend()
plt.show()

#root1=
