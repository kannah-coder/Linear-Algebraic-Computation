r1=int(input('enter row size mat 1:'))
c1=int(input("enter coloumn size of mat 1:"))
r2=int(input('enter row size mat 1:'))
c2=int(input("enter coloumn size of mat 2:"))

if(c1==r2):
    print("enter the first matrix elemnts:")
    m1=[]
    for i in range (r1):
        n1=[]
        for j in range (c1):
            n1.append(int(input()))
        m1.append(n1)
    print(" the 2nd matrix elements:")
    m2=[]
    for i in range(r2):
        n2=[]
        for j in range (c2):
            n2.append(int(input()))
        m2.append(n2)
    print("the first matrix is :")
    for i in range(r1):
        for j in range(c1):
            print(m1[i][j],end=" ")
        print()
    print("the second mat is :")
    for i in range (r2):
        for j in range (c2):
            print(m2[i][j],end=" ")
        print()
    print("the multiplication of  matrix is :")
    m3=[]
    for i in range (r1):
        n3=[]
        for j in range (c2):
            sum=0
            for k in range (c1):
                sum+=m1[i][k]*m2[k][j]
            n3.append(sum)
        m3.append(n3)
    for i in range (r1):
        for j in range(c2):
            print(m3[i][j],end=" ")
        print()    


else:
    print("Radhu ra ayyah!!")        



        