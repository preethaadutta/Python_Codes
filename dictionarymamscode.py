#declaring and assigning values in a dictionary.
#in dictionary all the items are stored as key and value pair
thisdict =	{
  "brand": "Maruti", #key:value
  "model": "zen",    #key:value
  "colour": "red",   #key:value
  "year": 1990       #key:value
}
print(thisdict)

x=thisdict.get("brand") #to get value of brand key
print(x) #printing value of brand key

thisdict["model"]=800 #to update value of model key
x=thisdict["model"]
print(x) #printing value of model key

#to access all the keys of a dictionary by using for loop
for x in thisdict:
  print(x)
#to access all the values of a dictionary by using for loop
for x in thisdict.values():
  print(x)
#to access all the keys and values of a dictionary by using for loop
for x, y in thisdict.items():
  print(x, y)
#condition check in dictionary and if yes then printing
if "brand" in thisdict:
  print("Yes, 'brand' is one of the keys in the thisdict dictionary")

#adding a new item in dictionary.new item means adding both key and value in dictionary
  thisdict["price"] = 600000
print(thisdict)
#pop() method deletes an item from dictionary.to delete an item we've to specify just that key then it'll delete both the key and also the value assigned to it.
thisdict.pop("model")
print(thisdict)
#this popitem() method will delete the last inserted item from dictionary
thisdict.popitem()
print(thisdict)
mydict = dict(thisdict) #here we're using dict constructor and storing that dictionary to a new variable
print(mydict)
