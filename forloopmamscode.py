#For loop
numbers=[6,5,7,4]
sum=0
for val in numbers:
    sum+=val
print("The sum is",sum)
for x in range(6):
  print(x)
for x in range(2, 6):
  print(x)
for x in range(2,6,2):
  print(x)
#For loop
fruits = ['apple', 'mango', 'banana']
for i in range(len(fruits)):
    print("I like", fruits[i])
else:
    print("No more fruits left")
for x in range(6):
    print(x)
else:
    print("Finally finished!")
for x in range(6):
    if x == 3: break
    print(x)
else:
    print("Finally finished!")
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]
for x in adj:
    for y in fruits:
        print(x, y)
pass