import sympy as sp
x,y,z=sp.symbols('x,y,z')
f=input("enter the fucntion: ")
f1,f2,f3=sp.diff(f,x),sp.diff(f,y),sp.diff(f,z)
print("the gradient of given scalar fucntion is : ")
print(f1,'i+',f2,'j+',f3,'k')
x1,y1,z1=input("enter points: ").split()
f1,f2,f3=f1.subs({x:x1,y:y1,z:z1}),f2.subs({x:x1,y:y1,z:z1}),f3.subs({x:x1,y:y1,z:z1})
print("the gradient of given scalr fucntion at point is : ",f1,'i+',f2,'j+',f3,'k')
