import sympy as sp
x,y,z=sp.symbols("x,y,z")
f1=input("enter fucntion: ")
f2=input("enter fucntion2:" )
f3=input("enter fucntion 3: ")
c1=sp.diff(f3,y)-sp.diff(f2,z)
c2=sp.diff(f1,z)-sp.diff(f3,x) 
c3=sp.diff(f2,x)-sp.diff(f1,y)

print("the curl equation is :",c1,"i+",c2,"j+",c3,"k")
x1,y1,z1=input("enter points ").split()
c1,c2,c3=c1.subs({x:x1,y:y1,z:z1}),c2.subs({x:x1,y:y1,z:z1}),c3.subs({x:x1,y:y1,z:z1})
print("the curl at point is :",c1,"i+",c2,"j+",c3,"k")

 
 