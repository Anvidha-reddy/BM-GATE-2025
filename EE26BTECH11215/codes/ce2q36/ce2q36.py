import sympy as sp

x = sp.symbols('x')
y = sp.Function('y')(x)
eq = y.diff(x), sp.exp(x - y)
de = sp.Eq(y.diff(x), sp.exp(x - y))

sol = sp.dsolve(de)
# print(eq)
print(f"Solution: {sol}\n \n")
sp.pprint(sol)
