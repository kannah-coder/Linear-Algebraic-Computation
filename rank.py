import numpy as np 
r=int(input("size o row:"))
c=int(input("coloumn size:"))
if r==c:
    print("enter the elmements:")
    m=[]
    for i in range (r):
        n=[]
        for j in range(c):
            n.append(int(input()))
        m.append(n)
    print("the matrix :")
    for i in range(r):
        for j in range(c):
            print(m[i][j],end=" ")
        print()
matrix=np.array(m)
print("the rank of the matrix is :")
rank=np.linalg.matrix_rank(matrix)
print(rank)

