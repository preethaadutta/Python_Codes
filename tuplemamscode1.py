#the below line is called as packing a tuple.it means creating a tuple and assigning values to that tuple
tuple1=("apple","banana","mango","cherry","pineapple") #declaring and assigning string data type values in a tuple
print(tuple1)
print(tuple1[2:4]) #slicing the tuple
print(tuple1[2:])
print(tuple1[-3:-2]) #negative indexing the tuple
#accessing all the elements of tuple by using for loop
for x in tuple1:
    print(tuple1)
#condition check
if "mango" in tuple1: #this will return boolean value if present then will return True otherwise it'll return False
    print("mango is in the basket")

tp2=("rose","lily","lotus")
tp3=tuple1+tp2 #concatenation of two tuples
print(tp3)
x=tp3.count("rose") #count() method counts the number of occurance of that element in tuple
print(x)

#while taking user input of a tuple if we give space between two numbers then that space also counted as an element
#while taking user input of a tuple if we give a two or three digit number as element then it's each digit will be considered as element of that tuple
tuple2 = tuple(input("Enter the tuple elements ...")) #taking user input of elements of tuple
print(tuple2) #printing that user inputed tuple
print(tuple1[4]) #element of the tuple can be accessed by its index number
print(min(tuple1))



tuple3=(456, 700, 200) #declaring and assigning int data type values in a tuple
print(max(tuple3)) #to find maximum value in that tuple
print(min(tuple3)) #to find minimum value in that tuple
print(type(tuple3)) #to check which data type it is
print(len(tuple3)) #to find length of a tuple. Length means number of elements in that tuple

#tuple is unchangable so we can't update values so to do that we've to follow these steps mentioned below
y = list(tuple3) #converting tuple to list by using list constructor
y[1] = "kiwi" #specifing value by it's index number
y.append(700) #append() method takes a single item as an input parameter and adds that to end of list
x = tuple(y) #then again converting list to tuple by using tuple constructor
print(x) #printing the tuple

#unpacking a tuple:It is the process of assigning different elements of a tuple into a variable.
fruits = ("apple", "banana", "cherry","lichi") #declaring and assigning string data type values in a tuple
(green, yellow, *red) = fruits
print(green) #here apple is assigned to green variable
print(yellow) #here banana is assigned to yellow variable
print(red) #here as *red was there so cherry and lichi both the elements will be assigned to red.it'll be assigned as a list

#another code
mytuple = fruits * 2 #as fruits tuple is multiplied by 2 so all the elements of fruits tuple will be present twice in the new tuple mytuple
print(mytuple) #printing
