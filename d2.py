import sympy  as sp
x=sp.Symbol('x')
y=sp.Function('y')
ode=sp.Eq(y(x).diff(x)+2*y(x),sp.exp(x)+x)
sol=sp.dsolve(ode,y(x))
print(sol)