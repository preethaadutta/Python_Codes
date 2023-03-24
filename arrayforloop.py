'''WAP to take user input of all elements of array and print them:-'''
#to take array user input
from array import * #import array as arr #same
array1=array('i',[]) #declaring array name
n=int(input("Enter the length of array=number of elements in array:")) #taking number of elements  user input in array
#taking elements user input in array
for i in range(n):
    x=int(input("Enter element in array:"))
    array1.append(x)

#Method1:-
print("Elements of array are:") #to display elements of array
#for a in array1: will iterate over the entire array
#single for loop in python:-
for a in array1: #a means elements in the array
    print(a)

#Method2:-
#nested for loop in python:-
for b in array1: #a means elements in the array
    for c in array1: #b means for each value of a it'll print all elements of array
        print(c)

#Method3:-
#for d in range(0,n): will iterate over the array starting from 0 index and will iterate till n index of array
#single for loop in python:-
for d in range(0,n): #here d means the index of elements of array
    print(d)

#Method4:-
#the output will be each elements of array
for e in range(0,n):
    print(array1[e])

#Method5:-
#nested for loop in python:-
for d in range(0,n): #here d means the index of elements of array
    for e in range(d+1,n): #here e means the index of elements of array but e will start from d+1 index
        print(array1[e])

'''
#to take array user input
from array import * #import array as arr #same
array1=array('i',[]) #declaring array name
n=int(input("Enter the length of array=number of elements in array:")) #taking number of elements user input in array
#taking elements user input in array
for i in range(n):
    x=int(input("Enter element of 1st array:"))
    array1.append(x)
array2=array('i',[]) #declaring array name
#taking elements user input in array
for j in range(n):
    y=int(input("Enter element of 2nd array:"))
    array2.append(y)
arraysum=array('i',[]) #declaring array name
for e in range(0,n):
    arraysum[e]=array1[e]+array2[e]
    arraysum.append(arraysum[e])
for a in arraysum: #a means elements in the array
    print(a)
'''