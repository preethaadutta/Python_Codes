#WAP to
#WAP to count number of repeated or duplicate elements in an array
from array import * #import array as arr #same
array1=array('i',[])
n=int(input("The length of array="))
for i in range(n):
    x=int(input("Enter the element="))
    array1.append(x)
#nested for loop in python
count=0
for d in range(0,n): #here d means the index of elements of array
    for e in range(d+1,n):
        if(array1[d]==array1[e]):
            count=count+1
#print("Number of repeated or duplicate elements is={}".format(count)) #this line will give output as #Number of repeated or duplicate elements is=ans
print("Number of repeated or duplicate elements is=",count)
