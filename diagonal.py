import sympy as sp
r1=int(input('enter row size mat 1:'))
c1=int(input("enter coloumn size of mat 1:"))
if r1==c1:
    print("enter matrix elements:")
    m1=[]
    for i in range(r1):
        n1=[]
        for j in range(c1):
            n1.append(int(input()))
        m1.append(n1)

    print("the matrix is:")
    for i in range(r1):
        for j in range(c1):
            print(m1[i][j],end=" ")
        print()

    A=sp.Matrix(m1)
    EV=A.eigenvals()
    EVC=A.eigenvects()
    p,d=A.diagonalize()
    print("EIGHEN VALUES:",EV)
    print("EIGHEN VECTORS:",EVC)
    print("MODEL MATRIX:",p)
    print("DIAGONALIZED:",d)

else:
    print("enter sqare matrix")
