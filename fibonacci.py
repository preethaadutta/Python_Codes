#Fibonacci series using for loop
r1=int(input("Enter range:"))
a1=0
b1=1
print(a1)
print(b1)
for i in range(1,r1,+1):
    c1=a1+b1
    print(c1)
    a1=b1
    b1=c1

#Fibonacci series using while loop
#Here range is not the count of numbers but range is within that number
#ie. r2=5 means 0 1 1 2 3 5 as 8 is greater than 5 so it'll not print 8 in series
r2=int(input("Enter range:"))
a2=0
b2=1
c2=0
while(c2<=r2):
    print(c2)
    a2=b2
    b2=c2
    c2=a2+b2