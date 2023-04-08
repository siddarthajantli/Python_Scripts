n=int(input("Enter the nnumber of rows: "))

for i in range(n):
    #for j in reversed(range(n-i)):
    for j in range(n-i):
        print (i+j+1,end=" ")
    print ()