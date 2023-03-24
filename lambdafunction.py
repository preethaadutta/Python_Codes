#Lambda function
#by taking user input
a=int(input("Enter a value="))
b=int(input("Enter a value="))
c=int(input("Enter a value="))
x=lambda a,b,c:a*b*c  #syntax #lambda arguments:expression
print(x(a,b,c))
y="PreethaaDutta"
(lambda y:print(x))(x) #syntax #lambda arguments:expression
