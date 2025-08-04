import sympy as sp
x,y,z=sp.symbols('x,y,z')
f=input("enter fucntion: ")

f1,f2,f3=sp.diff(f,x),sp.diff(f,y),sp.diff(f,z)
print("the gradient is :",f1,'i+',f2,'j+',f3,'k')
x1,y1,z1=input("enter points: ").split()
f1,f2,f3=f1.subs({x:x1,y:y1,z:z1}),f2.subs({x:x1,y:y1,z:z1}),f3.subs({x:x1,y:y1,z:z1})
grad=sp.Matrix([f1,f2,f3])
print("the gradient at given point is : ",f1,'i+',f2,"j+",f3,"k")

v1,v2,v3=map(float,input("enter derivative coeff ").split())
vect=sp.Matrix([v1,v2,v3])
norm=sp.sqrt(v1**2+v2**2+v3**2)
unitvector=vect/norm
derivative=grad.dot(unitvector)
print("the directional derivative is : ",derivative)