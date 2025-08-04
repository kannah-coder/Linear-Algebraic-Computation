#7b
"""
import sympy as sp
x=sp.Symbol('x')
y=sp.Function('y')
ode=sp.Eq(y(x).diff(x,2)-5*y(x).diff(x)+4*y(x),sp.exp(2*x)+sp.sin(x))
sol=sp.dsolve(ode,y(x))
sp.pprint(sol)
"""
#7a
import sympy as sp
x=sp.Symbol('x')
y=sp.Function('y')
ode=sp.Eq(y(x).diff(x,2)+6*y(x).diff(x)+9*y(x),sp.exp(3*x))
sol=sp.dsolve(ode,y(x))
sp.pprint(sol)