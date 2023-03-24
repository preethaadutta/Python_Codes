''' WAP to print maximum and minimum element of array:- '''
import sys
#to take array user input
from array import * #import array as arr #same
array1=array('i',[]) #declaring array name
n=int(input("Enter the length of array=number of elements in array:")) #taking number of elements  user input in array
#taking elements user input in array
for i in range(n):
    x=int(input("Enter element in array:"))
    array1.append(x)
max=0
min=sys.maxsize
for a in array1:
    if a>=max:
        max=a
for b in array1:
    if b<=min:
        min=b
print("Maximum element of array is:",max)
print("Minimum element of array is:",min)

#======================================================================================================#
''' WAP to print sum of elements of 2 arrays:- '''
#to take array user input
from array import * #import array as arr #same
#taking 1st array user input
array1=array('i',[]) #declaring array name
n=int(input("Enter the length of array=number of elements in array:")) #taking number of elements user input in array
#taking elements user input in array
for i in range(n):
    x=int(input("Enter element of 1st array:"))
    array1.append(x)
#taking 2nd array user input
array2=array('i',[]) #declaring array name
#taking elements user input in array
for j in range(n):
    y=int(input("Enter element of 2nd array:"))
    array2.append(y)
arraysum=array('i',[]) #declaring array name
for e in range(n): #for e in range(0,n): #same
    g=array1[e]+array2[e]
    arraysum.append(g)
for a in arraysum: #a means elements in the array
    print(a)

#======================================================================================================#
