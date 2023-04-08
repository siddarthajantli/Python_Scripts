n=int(input("Enter the nnumber of rows: "))

for i in range(n):
    for j in range (i):
        print (" ",end=" ")
    for j in range(n-i):
        print (1+j,end=" ")
    print ()