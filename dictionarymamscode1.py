#declaring and assigning values in a dictionary.
#in dictionary all the items are stored as key and value pair
text = {1: "Hello", 2: "all"}
text.clear() #clear() method deletes all the items so after clear() method it'll return empty dictionary
print('text =', text) #printing that cleared dictionary

x = ('key1', 'key2', 'key3') #Assigning keys of a dictionary
y = (10, 20, 30) #Assigning values of that dictionary.Values will be assigned respectively in the order
thisdict = dict.fromkeys(x, y) #creating a dictionary with those keys and values
print(thisdict) #printing that created dictionary

#declaring and assigning values in a dictionary.
#in dictionary all the items are stored as key and value pair
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

car.pop("model") #pop() method deletes an item from dictionary.to delete an item we've to specify just that key then it'll delete both the key and also the value assigned to it.
print(car)
#this popitem() method will delete the last inserted item from dictionary
car.popitem()
print(car)
#setdefault() method is used to add an item to a dictionary
x = car.setdefault("model", "Bronco") #to add an item in a dictionary we've to specify both key and value
print(x) #here x is new added value
print(car) #printing the dictionary after adding new item to it
