import sympy as sp

x = sp.Symbol('x')
y = sp.Symbol('y')

print(x*y)

print(sp.diff(x**10, x, 2))  # second derivative
print(sp.integrate(sp.cos(x), x))
print(sp.simplify((x**2 + x**3)/x**2))
print(sp.limit(sp.sin(x)/x, x, 0))
print(sp.solve(5*x - 15, x))
