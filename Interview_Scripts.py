#Python Program:
#---------------------------------------------------------------------------------------------------------------
#Python Reverse a Number:

num = 123456
rev_num = 0

while num != 0:
    rev_num = ( num % 10 ) + ( rev_num * 10 )
    num //= 10

print (rev_num)

num = 123456
print(int(str(num)[::-1]))
#---------------------------------------------------------------------------------------------------------------
#Armstrong number program in python with explanation

or_num = num = 153
ln = len(str(num))
am_num = 0

while num != 0:
    am_num =  am_num + (num % 10) ** ln
    num //=10

if or_num == am_num:
    print ("Given number is armstrong.")
else:
    print ("Given number is not a armstrong.")
#---------------------------------------------------------------------------------------------------------------
#Python Program to find missing number in array

arr = []
n = int(input("enter size of array : "))
for x in range(n-1):
    x=int(input("enter element of array : "))
    arr.append(x)

arr_sum = sum(arr)
print (arr_sum)
arr_cal = (n*(n+1))/2;

print ("Missing number: ",int(arr_cal-arr_sum))
#---------------------------------------------------------------------------------------------------------------
#Regex Script to get the Name and Score from the string

import re

cric_name = '''Ram scores 76 and Sam scores 40 and \nRaju scores 88 and Vaishali scores 99.'''

name = re.findall( r'[A-Z]\w*', cric_name )
scre = re.findall( r'\d{2}', cric_name )
score_dic = {}
for (i, j) in zip(name, scre):
    score_dic[i] = j

print (score_dic)
#---------------------------------------------------------------------------------------------------------------