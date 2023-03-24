#User defined function on list
def my_function(food):
  for x in food:
    print(x)
fruits = ["apple", "banana", "cherry"]
my_function(fruits)

#Programs on list
listA = ['Mon', 'Tue', 9, 3, 3]
print("Given list : ", listA)
# Adding another element for each element
Newlist = [i for i in listA for n in (0, 1)]
# Result
print("New list after duplication: ", Newlist)
list1 = [456, 700, 200]
print(max(list1))
print(min(list1))
l = [15, 18, 2, 36, 12, 78, 5, 6, 9]
import statistics
print(statistics.mean(l))
