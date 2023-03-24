#WAP to swap two numbers of a list
#Method 1

#to take list user input
#this will take user input in seperate lines
list1=[]
n1=int(input("Enter number of elements in list:"))
for i in range(0,n1):
    element1=int(input())
    list1.append(element1)

pos1=int(input("Enter a position:"))
pos2=int(input("Enter another position:"))
list1[pos1],list1[pos2]=list1[pos2],list1[pos1]
print(list1)


list2=[]
n2=int(input("Enter number of elements in list:"))
for j in range(0,n2):
    element2=int(input())
    list2.append(element2)
tuple1=tuple(list2)
string1=str(tuple1)
print(string1)