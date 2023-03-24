#tuples code
#WAP to convert tuple to a string
#this method only applicable for char datatype tuple to string convertion
list1=[] #taking blank list
n1=int(input("Enter number of elements in list:"))
for i in range(n1): #for i in range(0,n1): #same
    element1=input("Enter element:") #will take input of char datatype
    list1.append(element1) #append() method will add elements into the blank list
tuple1=tuple(list1) #converting list into tuple using tuple constructor
string1='' #taking an empty string
for i in tuple1:
    string1=string1+i
print(string1)


#WAP to calculate average of elements of tuple
#Method1
list2=[] #taking blank list
n2=int(input("Enter number of elements in list:"))
for j in range(n2): #for j in range(0,n2): #same
    element2=int(input("Enter element:"))
    list2.append(element2) #append() method will add elements into the blank list1
tuple2=tuple(list2) #converting list into tuple using tuple constructor
sum1=0
for j in range(n2): #for j in range(0,n2): #same
    #sum=sum+j #this will give error as j is index number of each item
    sum1=sum1+list2[j] #sum=sum of each item of tuple
average1=sum1/n2
print(average1)

#Method2
tuple3=() ##taking blank tuple
list3=list(tuple3) #converting tuple into list using list constructor
n3=int(input("Enter number of elements in list:"))
for k in range(n3): #for j in range(0,n3): #same
    element3=int(input("Enter element:"))
    list3.append(element3) #append() method will add elements into the blank list
sum2=0
average2=0
for k in range(n3): #for k in range(0,n3): #same
    # sum=sum+k #this will give error as k is index number of each item
    sum2=sum2+list3[k] #sum=sum of each item of tuple
average2=sum2/n3
print("average is={}".format(average2)) #this line will give output as #average is=ans

#WAP to find the index of an item of a tuple with using index() method
#method1
list5=[] #taking blank list
n5=int(input("Enter number of elements in list:"))
for m in range(n5): #for i in range(0,n1): #same
    element5=int(input("Enter element:"))
    list5.append(element5) #append() method will add elements into the blank list
tuple5=tuple(list5) #converting list into tuple using tuple constructor
value1=int(input("Enter a value whose index you want to find out:"))
index1=tuple5.index(value1)
print(index1)
#method2
tuple4=() #taking blank tuple
list4=list(tuple4) #converting tuple into list using list constructor
n4=int(input("Enter number of elements in list:"))
for l in range(n4): #for l in range(0,n3): #same
    element4=int(input("Enter element:"))
    list4.append(element4) #append() method will add elements into the blank list
value2=int(input("Enter a value whose index you want to find out:"))
index2=list4.index(value2)
print("index is={}".format(index2))