#Prime number check
n1=int(input("Enter a number:"))
flag1=0
for i in range(2,n1):
    if(n1%i==0):
        flag1=flag1+1
if(flag1>0):
    print(n1,"is not a prime number")
else:
    print(n1,"is a prime number")

#Print Prime number within given range
r=int(input("Enter range:"))
for n2 in range(1,r+1):
    flag2=0
    for i in range(2,n2):
        if(n2%i==0):
            flag2=flag2+1
    if(flag2>0):
        pass #To avoid any action in this case to avoid any printing for this condition
    else:
        print(n2)

