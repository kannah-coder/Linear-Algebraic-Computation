# 10)A) 
"""
import sympy as sp
x,y=sp.symbols('x , y')
f=input("enter function: ")
x1=input("x limits: ").split()
y1=input("y limits: ").split()

res=sp.integrate(f,(x,x1),(y,y1))
print("the result of given fucntion is :",res)
"""
"""
#10)B)
import sympy as sp
x,y=sp.symbols('x , y')
f=input("enter function: ")
x1=input("x limits: ").split()
y1=input("y limits: ").split()

res=sp.integrate(f,(y,y1),(x,x1))
print("the result of given fucntion is :",res)
"""
import sympy as sp
x,y,z=sp.symbols('x,y,z')
f=input("enter fucntion: ")
x1=input("enter x limits: ").split()
y1=input("enter y limits: ").split()
z1=input("enter z llimtis: ").split()
resultant=sp.integrate(f,(z,z1),(y,y1),(x,x1))
print("the result is: ",resultant)
