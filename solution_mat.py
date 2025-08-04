import numpy as np
r=int(input("enter no.of rows :"))
c=int(input("enter no.of cols:"))
print("enter the matrix elements:")
m=[]
for i in range(r):
  n=[]
  for j in range(c):
    n.append(int(input()))
  m.append(n)
print("the matrix is:")
for i in range(r):
  for j in range(c):
    print(m[i][j],end=" ")
  print()
print("enter the coefficient matrix size:")
r1=int(input())
c1=1
if(r1==r):
  print("the coefficient matrix:")
  m1=[]
  for i in range(r1):
    n1=[]
    for j in range(c1):
      n1.append(int(input()))
    m1.append(n1)
  print("the coefficient matrix:")
  for i in range(r1):
    for j in range(c1):
      print(m1[i][j],end="")
    print()
  A=np.array(m)
  b=np.array(m1)
  s=np.linalg.solve(A,b)
  print("the sol of system of equations is:")
  print(s)
else:
  print("not possible") 