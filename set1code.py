#WAP to find maximum and minimum elements in set
#using max() and min() method
set1=set() #taking empty set
n1=int(input("Enter number of elements in set:"))
for i in range(n1): #for i in range(0,n1): #same
    element1=int(input("Enter element:"))
    set1.add(element1) #add() method will add elements into the blank set
maximum=max(set1) #using max() method
print("maximum element is={}".format(maximum)) #maximum element is=ans
minimum=min(set1) #using min() method
print("minimum element is={}".format(minimum)) #minimum element is=ans

#WAP to find set difference
#using difference() method
set2=set() #taking empty set
n2=int(input("Enter number of elements in set:"))
for j in range(n2): #for i in range(0,n1): #same
    element2=int(input("Enter element:"))
    set2.add(element2) #add() method will add elements into the blank set
set3=set() #taking empty set
n3=int(input("Enter number of elements in set:"))
for k in range(n3): #for i in range(0,n1): #same
    element3=int(input("Enter element:"))
    set3.add(element3) #add() method will add elements into the blank set
set4=set2.difference(set3) #(set2-set3)
set5=set3.difference(set2) #(set3-set2)
print(set4)
print(set5)