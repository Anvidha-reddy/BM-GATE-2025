import sympy as sp

x, y, z = sp.symbols('x y z')
u = sp.Function('u')(x, y)
v = sp.Function('v')(x, y)

# Velocity vector V = u i_hat + v j_hat
# z-component of curl (d(v)/dx - d(u)/dy)
curl_z = sp.diff(v, x) - sp.diff(u, y)
div_v = sp.diff(u, x) + sp.diff(v, y)


print(f"z-component of Curl: ")
sp.pprint(curl_z)
print(f"\n\nDivergence = ")
sp.pprint(div_v)
