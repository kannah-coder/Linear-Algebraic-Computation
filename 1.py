import numpy as np
r=int(input("enter the number of rows"))
c=int(input("enter the number of cloumns"))
if r==c:
    print("enter the elements")
    m=[]
    for i in range(r):
        b=[]
        for j in range(c):
          b.append(int(input()))
        m.append(b)  
    print("the matrix is") 
    for i in range(r):
        for j in range(c):
            print(m[i][j],end=" ")
        print()   
    matrix=np.array(m)
    det=np.linalg.det(matrix)
    print("det:",det)