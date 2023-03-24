#In-built methods of array:-
from array import *
array1 = array('i', [10,20,30,40,50])
array1.insert(1,60)
array1.remove(40)
for x in array1:
    print(x)
print (array1.index(50))

array2=array('i',[])
n=int(input("Enter length of array: "))
for i in range(n):
    x=int(input("Enter element of array: "))
    array2.append(x)
for x in array2:
    print(x)
n=int(input("Enter the element to search: "))
print (array2.index(n))
k=0
for e in array2:
    if e==n:
       print(k)
    break

