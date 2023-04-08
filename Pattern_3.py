n=int(input("Enter the nnumber of rows: "))

for i in range(n):
    #print (i)
    for j in range(n-i):
        print (i+1,end=" ")
    print ()