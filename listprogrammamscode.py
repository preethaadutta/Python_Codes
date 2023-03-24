#Program on List
list1=["rose","lotus","jasmine","tulip"]
print(type(list1))
print(list1[1]) #Slicing on lists
print(list1[-2]) #Slicing on lists
print(list1[2:4]) #Slicing on lists
print(list1[-3:-1]) #Slicing on lists
print(list1[:3]) #Slicing on lists
print(list1[2:]) #Slicing on lists

#For loop on list
list1[3]="sunflower"
for x in list1:
    print(x)

#If on list
l1=[x for x in list1 if "rose" in x]
l2=[x for x in list1]
l3=[x for x in range(10) if x < 10]
if "rose" in list1:
    print("rose exist in the list")
list1.append("tulip")
print(list1)
print(len(list1))
list1.insert(4,"merrygold")
print(list1)
list1.remove("merrygold")
print(list1)
mylist=list(list1)
print(mylist)
list2=["apple","mango","banana"]
list3=list1+list2
list1.extend(list2)
print(list3)
list3.pop()
print(list3)
list3.reverse()
print(list3)
list3.sort(reverse=True)
print(list3)
del list1
list1.clear() #It will give error as all elements are deleted of list1
