import sympy as sp
x,y,z=sp.symbols('x,y,z')
f1=input("enter func 1: ")
f2=input("enter func 2: ")
f3=input("enter func 3: ")

d1=sp.diff(f3,y)-sp.diff(f2,z)
d2=sp.diff(f1,z)-sp.diff(f3,x)
d3=sp.diff(f2,x)-sp.diff(f1,y)

print("the curl vector is :",d1,'i+',d2,'j+',d3,'k')

x1,y1,z1=input("enter points: ").split()
d1,d2,d3=d1.subs({x:x1,y:y1,z:z1}),d2.subs({x:x1,y:y1,z:z1}),d3.subs({x:x1,y:y1,z:z1})
print("the curl vector a given point is: ",d1,'i+',d2,'j+',d3,'k')
