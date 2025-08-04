import sympy as sp
x,y,z=sp.symbols('x ,y, z')
u=input("enter fucntion of u:")
v=input("enter the fucntion of v:")
w=input("enter the fucntion of w: ")


r1,r2,r3=(sp.diff(u,x),sp.diff(u,y),sp.diff(u,z))
r4,r5,r6=(sp.diff(v,x),sp.diff(v,y),sp.diff(v,z))
r7,r8,r9=(sp.diff(w,x),sp.diff(w,y),sp.diff(w,z))
m=([r1,r2,r3],[r4,r5,r6],[r7,r8,r9])
matrix=sp.Matrix(m)
jacobian=matrix.det()
print("the jacobian of the given fucntion is: ",jacobian)
if jacobian==0:
    print("u,v,w are dependent fucntion")
else:

    print("it is independent function")



