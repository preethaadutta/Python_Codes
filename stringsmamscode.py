#Strings code
a="Hello everyone"
print(len(a)) #returns length of string #Output: 14
print(a[1]) #Output: e
print(a[2:5]) #slicling on string #Output: llo
print(a[2:]) #Output: llo everyone
print(a[:5]) #Output: Hello
print(a[-5:-2]) #negetive indexing on string #Output: ryo

b=2020
txt="The year is  {}" #format method on string
print(txt.format(b)) #Output: The year is  2020

quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price)) #Output: I want 3 pieces of item 567 for 49.95 dollars.

#iterate over the characters of string:-
for x in "banana":
    print(x) #Output: b a n a n a

#=========================================================================================================#
#Strings code
txt = "welcome to the jungle"
x = txt.split()
print(x) #Output: ['welcome', 'to', 'the', 'jungle']
x = txt.partition("the")
print(x) #Output: ('welcome to ', 'the', ' jungle')

str = 'Python program'
print(str*3) #Output: Python programPython programPython program
print(str[7:9]*3) #Output: prprpr

x = "apple and banana"
print("banana" in x) #Output: True

#=========================================================================================================#
#Strings code
txt = "hello, and welcome to my world."
x = txt.capitalize()
print(x) #Hello, and welcome to my world.
x = txt.title()
print(x) #Hello, And Welcome To My World.

txt = "I love apples, apple are my favorite fruit"
x = txt.count("apple")
print(x) #2
print(txt.upper()) #I LOVE APPLES, APPLE ARE MY FAVORITE FRUIT

txt = "Hello, welcome to my world."
x = txt.index("welcome")
print(x) #7

txt=" "
x = txt.isspace()
print(x) #True

txt = "CompanyX"
x = txt.isalpha()
print(x) #True

n="12"
x=n.isdigit()
print(x) #True

#=========================================================================================================#
#Strings code
x="hello from python"
print(len(x)) #17
print(x.strip()) #hello from python
print(x.upper()) #HELLO FROM PYTHON
print(x.replace("p","j")) #hello from jython
print(x.split(",")) #['hello from python']
if "ello" in x:
    print("found") #found

#=========================================================================================================#
test_str = "Happy new year"
all_freq = {}
for i in test_str:
    if i in all_freq:
        all_freq[i] += 1
    else:
        all_freq[i] = 1
print("Count of all characters in the string :\n " + str(all_freq))

