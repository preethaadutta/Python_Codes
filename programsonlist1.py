#WAP to find largest number of list
list1=[]
n1=int(input("Enter number of elements in list:"))
for i in range(0,n1):
    element1=int(input())
    list1.append(element1)
list1.sort(reverse=True)
print("largest element of the list is",list1[0])

#WAP to find second largest number of list
list2=[]
n2=int(input("Enter number of elements in list:"))
for j in range(0,n2):
    element2=int(input())
    list2.append(element2)
list2.sort(reverse=True)
print("Second largest element of the list is",list2[1])

#WAP to find smallest number of list
list3=[]
n3=int(input("Enter number of elements in list:"))
for k in range(0,n3):
    element3=int(input())
    list3.append(element3)
list3.sort()
print("Smallest element of the list is",list3[0])

#WAP to find second smallest number of list
list4=[]
n4=int(input("Enter number of elements in list:"))
for l in range(0,n4):
    element4=int(input())
    list4.append(element4)
list4.sort()
print("Second smallest element of the list is",list4[1])