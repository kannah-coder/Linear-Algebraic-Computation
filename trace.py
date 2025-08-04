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
    print("the trace is:")
    trace=0
    for i in range(r):
        for j in range(c):
            if i==j:
                trace=trace+m[i][j]
    print(trace)            
'''
numpy is a module which use d to calculate numerical values its used to calculte the multidimensional arraand matrix
   syntax:
    np.array(n) ,it crewtes a matrix
    np.eye(n) , creats nxn matrix
    np.transpose(matrix),returns trace of matrix
    np.add(a,b),returns addition of (a,b)
    np.sub(a,b),returns subraction of (a,b)
    np.multi(a,b)
    np.linalg.det(a),returns to det of a
    np.linalg,inv(a),inverse of a
    np.linalg.eig(a),it gives eighen values
    np.linalg.matrix_power(A,n)
    np.linalg_solve(A,b), it gives Ax=b
'''


