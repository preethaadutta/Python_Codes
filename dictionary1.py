#WAP to concatenate or merge three dictionaries
#user input of 1st dictionary
dictionary1={}
n1=int(input("Enter number of elements:"))
for i in range(n1):
    key1=int(input("Enter key:"))
    value1=int(input("Enter value:"))
    dictionary1.update({key1:value1})
#user input of 2nd dictionary
dictionary2={}
n2=int(input("Enter number of elements:"))
for j in range(n2):
    key2=int(input("Enter key:"))
    value2=int(input("Enter value:"))
    dictionary2.update({key2:value2})
#user input of 3rd dictionary
dictionary3={}
n3=int(input("Enter number of elements:"))
for k in range(n3):
    key3=int(input("Enter key:"))
    value3=int(input("Enter value:"))
    dictionary3.update({key3:value3})
dictionary4={}
for d in (dictionary1,dictionary2,dictionary3):
    dictionary4.update(d)
print("Concatenation of three dictionaries",dictionary4)

#WAP to concatenate or merge two dictionaries
#method1
#user input of 1st dictionary
dictionary5={}
n5=int(input("Enter number of elements:"))
for l in range(n1):
    key5=int(input("Enter key:"))
    value5=int(input("Enter value:"))
    dictionary1.update({key5:value5})
#user input of 2nd dictionary
dictionary6={}
n6=int(input("Enter number of elements:"))
for m in range(n6):
    key6=int(input("Enter key:"))
    value6=int(input("Enter value:"))
    dictionary6.update({key6:value6})
dictionary7={**dictionary5,**dictionary6}
print(dictionary7)