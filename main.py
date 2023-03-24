String=str(input("Enter a string="))
print(String[11:17])   #positive slicing of a string
print(String[0:17])    #positive slicing of a string
print(String[:17])     #positive slicing of a string
x1=String[-14:-8]       #Slicing by negative indexing
print(x1*3)             #Technique to print any string any number of times
print("python" in String)  #Technique to check whether a word is present in string or not
if "python" in String:     #If condition check in python
    print("True")
x2=String.partition("python") #Function to make partition between the words not all words
print(x2)
x3=String.capitalize()   #Function to do capital of only initial alphabet of the first word in string
print(x3)
x4=String.title()   #Function to do capital all the initial letters of words in string
print(x4)
x5=String.upper()   #Function to do capital all the letters of words in string
print(x5)
x6=String.count("first") #Function to count occurance of that word in string
print(x6)

#We can add strings or any integer or any float or any variable inside a string using format method
#One program: Format method program to add string inside another string
s="string"
txt1="{} has many methods"
print(txt1.format(s))

#Another program: Format method program to add strings inside another string
p1="java"
c="more"
p2="python"
txt2="I like {} {} than {}."
print(txt2.format(p2,c,p1))

#Another program: Format method program to add integer or float variable inside another string
a=10
b=8.5533
txt3="I got {} marks out of {} in semester."
print(txt3.format(b,a))