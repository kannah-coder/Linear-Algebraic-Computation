import sympy  as sp
x=sp.Symbol('x')
y=sp.Function('y')
ode=sp.Eq(y(x).diff(x)+x,-9*y(x))
sol=sp.dsolve(ode,y(x))
print(sol)