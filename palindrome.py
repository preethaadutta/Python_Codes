#Palindrome check for only numbers
n1=int(input("Enter a number:"))
reverse1=0
temp=n1
while(temp>0):
    rem=temp%10
    reverse1=(reverse1*10)+rem
    temp=temp//10
if(n1==reverse1):
    print("It is a Plindrome number")
else:
    print("It is not a Plindrome number")

#Palindrome check for anything like numbers or words
n2=input("Enter something:")
string1=n2.lower() #Converts any string having uppercase or lowercase to lowercase
#Not specifing starting and ending point in slicing because it'll take entire string and -1 will reverse the string
#-1 indicates that we want to step back towards by 1 so it'll reverse the string so it'll return reverse string
reverse2=string1[::-1]
if(string1==reverse2):
    print("It is palindrome")
else:
    print("It is not palindrome")

