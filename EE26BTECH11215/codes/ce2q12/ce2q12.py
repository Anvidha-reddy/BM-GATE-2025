import sympy as sp

x = sp.Symbol('x')
integral = sp.integrate(sp.ln(x), x)
print(f"Integral of ln(x) dx = {integral} + Constant")
