thisset = {"apple", "banana", "cherry"} #declaring and assigning values in a set
print(thisset) #printing the set
print("banana" in thisset) #this will return boolean value if that item is present in set then it'll return True or if that item is not present in set then it'll return False
thisset.add("mango") #add() method will add new item to that set but we can't understand that in which place it'll be added because set is unindexed
print(thisset) #printing after adding
#in the below line ["orange","lichi"] is a list. to concatenate two sets or a set and a list we can use update() method
thisset.update(["orange","lichi"]) #update() method will concatenate to that set but we can't understand that in which place it'll be added
#update() method concatenates two sets but after concatenation the values of previous set (here thisset) is changed the whole concatenation is taken place in thisset
print(thisset)
#remove() method throws error if specified item is not present in set
thisset.remove("banana") #remove() method is used to delete that particular item from set
print(thisset)
#discard() method doesn't throw error if specified item is not present in set
thisset.discard("banana") #discard() method is used to delete that particular item from set
print(thisset)
thisset.clear() #clear() method deletes all the elements from set so after clear() method it'll return empty set
print(thisset) #printing that empty set

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2) #union() method also concatenates two sets but after concatenation the values of set1 and set2 are not changed rather after concatenation the whole result is stored in a new set set3
print(set3) #printing the new set after concatenation

set4={"pink","blue","red"}
set5={"violet","brown","red","pink"}
set6=set4.intersection(set5) #intersection() method returns intersection part of 2 sets means common elements of 2 sets
print(set6)
set4.intersection_update(set5) #intersection_update() method updates intersection part of 2 sets in one of the 2 sets
print(set4)
#difference() function calculates set difference
set7=set4.difference(set5) #(set4-set5)
set8=set5.difference(set4) #(set5-set4)
print(set7)
print(set8)