n=int(input("Enter the nnumber of rows: "))
k=0
#print (n)

for i in range (n+1):
    k=k+i
#print (k)

for i in range (n):
    #print (i)
    for j in range(i+1): 
        print (format(k,"3"),end=' ')
        k=k-1
    print ()