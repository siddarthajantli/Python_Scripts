n=int(input("Enter the nnumber of rows: "))

for i in range(n):
    for j in range(n-i):
        print (n-j,end=" ")
    print ()