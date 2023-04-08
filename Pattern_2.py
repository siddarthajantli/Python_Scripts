n=int(input("Enter the nnumber of rows: "))

#print (n)
k=1

for i in reversed(range(n)):
    #print (i)
    for j in range(1,i+1):
        print (j,end=" ")
    print ()