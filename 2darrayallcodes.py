#2D Array basic code in Python
''' WAP to take user input of 2d array and display that:- '''
import numpy as np #actually no error in code have to install numpy package in ide
#to take 2d array user input
outerarray=[] #declaring 2d array name
row=int(input("Enter number of rows: "))
column=int(input("Enter number of columns: "))
#taking elements user input in array
for i in range(row):
    innerarray=[]
    for j in range(column):
        element=int(input("Enter element: "))
        innerarray.append(element)
    outerarray.append(innerarray)
#
array1=np.array(outerarray)
#to display 2d array
#Method1:- print(outerarray)
#Method2:-
for i in range(row):
    for j in range(column):
        print(array1[i][j],end=" ") #elements of innerarray will be printed after one space
    print() #elements of outerarray will be printed in next line
    
print(type(array1)) #Output:- <class 'numpy.ndarray'>

#===========================================================================================================#
''' WAP to print sum of two matrices:- '''

#Process to take Matrix or 2D array user input
row = int(input("Enter number of rows: "))
column = int(input("Enter number of columns: "))
#method means logic which will create Matrix or 2D array
def matrix(row, column):
    outerarray = []  # declaring 2d array name
    for i in range(row):
        innerarray = []
        for j in range(column):
            element = int(input(f"Enter element of position [{i}][{j}]: ")) #using fstring for formatting
            innerarray.append(element)
        outerarray.append(innerarray)
    return outerarray
#this part will take user input of Matrix or 2D array
print("Enter 1st Matrix: ")
Matrix1 = matrix(row, column) #calling the user-defined method
print(Matrix1) #not mandatory
print("Enter 2nd Matrix: ")
Matrix2 = matrix(row, column) #calling the user-defined method
print(Matrix2) #not mandatory

#Main logic to do sum of 2 Matrices
def sum(Matrix1, Matrix2):
    arraysumouterarray = []
    for i in range(len(Matrix1)):  #len(Matrix1) means number of rows
        arraysuminnerarray = []
        for j in range(len(Matrix1[0])): #len(Matrix1[0]) means number of columns
            s=Matrix1[i][j] + Matrix2[i][j]
            arraysuminnerarray.append(s)
        arraysumouterarray.append(arraysuminnerarray)
    return arraysumouterarray

Matrixsum = sum(Matrix1, Matrix2) #calling the user-defined method
print("Sum of 2 Matrices is: ",Matrixsum)

'''
Output:-
Enter number of rows: 2
Enter number of columns: 3
Enter 1st Matrix: 
Enter element of position [0][0]: 1
Enter element of position [0][1]: 2
Enter element of position [0][2]: 2
Enter element of position [1][0]: 1
Enter element of position [1][1]: 3
Enter element of position [1][2]: 2
[[1, 2, 2], [1, 3, 2]]
Enter 2nd Matrix: 
Enter element of position [0][0]: 1
Enter element of position [0][1]: 2
Enter element of position [0][2]: 3
Enter element of position [1][0]: 2
Enter element of position [1][1]: 3
Enter element of position [1][2]: 1
[[1, 2, 3], [2, 3, 1]]
Sum of 2 Matrices is:  [[2, 4, 5], [3, 6, 3]]
'''
#===========================================================================================================#
