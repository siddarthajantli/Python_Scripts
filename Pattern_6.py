n=int(input("Enter the nnumber of rows: "))

for i in range(n):
    for j in reversed(range(n-i)):
        print (j+1,end=" ")
    print ()